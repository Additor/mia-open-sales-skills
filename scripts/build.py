#!/usr/bin/env python3
"""Build skills/<name>/SKILL.md from src/skills/*.md, inserting src/shared/context.md.
Each skill folder also receives assets/ and config/ so it stands alone."""
import pathlib, shutil, sys

root = pathlib.Path(__file__).resolve().parent.parent
shared = (root / "src/shared/context.md").read_text(encoding="utf-8").strip()
out = root / "skills"
if out.exists():
    shutil.rmtree(out)
LIMIT = 15 * 1024
for src in sorted((root / "src/skills").glob("*.md")):
    name = src.stem
    text = src.read_text(encoding="utf-8").replace("{{SHARED}}", shared)
    dest = out / name
    dest.mkdir(parents=True)
    (dest / "SKILL.md").write_text(text, encoding="utf-8")
    # copy assets, keeping only this skill's schema and reference files, plus shared-* reference files
    def skip(d, names, name=name):
        d = pathlib.Path(d)
        if d.name in ("schemas", "ref"):
            return [n for n in names if not (n.startswith(name) or (d.name == "ref" and n.startswith("shared-")))]
        return []
    shutil.copytree(root / "assets", dest / "assets", ignore=skip)
    shutil.copytree(root / "config", dest / "config")
    size = len(text.encode("utf-8"))
    flag = "  OVER LIMIT" if size > LIMIT else ""
    print(f"{name}: {size} bytes{flag}")
