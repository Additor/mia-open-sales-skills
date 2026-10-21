#!/usr/bin/env python3
"""Build skills/<name>/ from source/.

SKILL.md is source/skills/<name>.md with source/shared/context.md inserted. Each skill folder
gets only the config and assets files it references (directly or through another file it
carries), so it stands alone. The build fails when a referenced file is missing or a SKILL.md
passes the size limit."""
import pathlib, re, shutil, sys

src = pathlib.Path(__file__).resolve().parent
root = src.parent
out = root / "skills"
LIMIT = 15 * 1024
shared = (src / "shared/context.md").read_text(encoding="utf-8").strip()

ASSET_RE = re.compile(r"assets/[A-Za-z0-9_./-]*[A-Za-z0-9_]\.(?:md|html)")
CONFIG_RE = re.compile(r"config/([A-Za-z0-9-]+)\.md")
PACK = sorted(p.stem for p in (src / "config").glob("*.md") if p.stem not in ("SCHEMA", "TEAM-ROLLOUT"))

def read(path):
    return path.read_text(encoding="utf-8")

errors = []
if out.exists():
    shutil.rmtree(out)

for skill_src in sorted((src / "skills").glob("*.md")):
    name = skill_src.stem
    text = read(skill_src).replace("{{SHARED}}", shared)
    texts = [text]
    assets, config = set(), {"SCHEMA"}

    # Follow asset references through every file the skill carries.
    queue = [text]
    while queue:
        body = queue.pop()
        for ref in ASSET_RE.findall(body):
            if ref in assets:
                continue
            path = src / ref
            if not path.exists():
                errors.append(f"{name}: references missing file {ref}")
                continue
            assets.add(ref)
            content = read(path)
            texts.append(content)
            queue.append(content)

    # Config files: named by path, or by their bare pack file name anywhere in the carried text.
    blob = "\n".join(texts)
    own = blob.replace(shared, "")  # the shared rules name pack files in passing; they do not read them
    for stem in CONFIG_RE.findall(blob):
        if not (src / "config" / f"{stem}.md").exists():
            errors.append(f"{name}: references missing file config/{stem}.md")
        else:
            config.add(stem)
    for stem in PACK:
        if re.search(rf"(?<![\w-]){re.escape(stem)}(?![\w-])", own):
            config.add(stem)

    dest = out / name
    dest.mkdir(parents=True)
    (dest / "SKILL.md").write_text(text, encoding="utf-8")
    for ref in sorted(assets):
        (dest / ref).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src / ref, dest / ref)
    for stem in sorted(config):
        (dest / "config").mkdir(exist_ok=True)
        shutil.copy2(src / "config" / f"{stem}.md", dest / "config" / f"{stem}.md")

    size = len(text.encode("utf-8"))
    over = size > LIMIT
    if over:
        errors.append(f"{name}: SKILL.md is {size} bytes, over the {LIMIT} byte limit")
    files = sum(1 for p in dest.rglob("*") if p.is_file())
    print(f"{name}: {size} bytes, {files} files{'  OVER LIMIT' if over else ''}")

if errors:
    print("\n".join(["", "Build failed:"] + errors), file=sys.stderr)
    sys.exit(1)
