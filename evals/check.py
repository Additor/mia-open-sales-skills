#!/usr/bin/env python3
"""Check the files and output of one eval case. Usage: check.py <case> <workspace> <output.txt>"""
import csv, glob, hashlib, json, pathlib, sys

case, ws, out = sys.argv[1], pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3])
text = out.read_text(errors="replace")
fails = []

def check(ok, label):
    print(("PASS " if ok else "FAIL ") + label)
    if not ok:
        fails.append(label)

def names():
    with open(ws / "deals.csv") as f:
        return {r["company"] for r in csv.DictReader(f)}

def amounts():
    repo = pathlib.Path(__file__).resolve().parent.parent
    seed = " ".join(f.read_text() for f in (repo / "config").glob("*.md"))
    with open(ws / "deals.csv") as f:
        vals = {int(r["amount"]) for r in csv.DictReader(f) if r["amount"]}
    return {v for v in vals if f"{v:,}" not in seed and str(v) not in seed}

def leaked_amounts(paths):
    hits = []
    for p in paths:
        # Ranges and averages are allowed ("$18,000 to $56,500"); flag an amount on a line that is neither.
        marks = ("–", "—", " to ", "averag", "median", "range", "total", "between")
        lines = [l for l in pathlib.Path(p).read_text(errors="replace").splitlines() if not any(m in l.lower() for m in marks)]
        body = "\n".join(lines)
        hits += [(pathlib.Path(p).name, a) for a in amounts() if f"{a:,}" in body or str(a) in body]
    return hits

def leaked(paths):
    hits = []
    for p in paths:
        body = pathlib.Path(p).read_text(errors="replace")
        hits += [(pathlib.Path(p).name, n) for n in names() if n in body]
    return hits

def reports(skill):
    return glob.glob(str(ws / "mia-reports" / f"*{skill}*"))

if case == "pack-setup":
    pack = ws / "mia-pack"
    need = ["deal-lifecycle", "buyers-and-competition", "market-physics", "winning-plays",
            "team-standards", "scoring-axes", "working-style"]
    check(pack.is_dir(), "mia-pack/ was created")
    for n in need:
        f = pack / f"{n}.md"
        check(f.exists(), f"{n}.md written")
        if f.exists():
            head = f.read_text().split("\n")[:15]
            fm = "\n".join(head)
            check(head[0].strip() == "---" and all(k in fm for k in ("file:", "scope:", "version:", "updated:", "status: seed")),
                  f"{n}.md has seed frontmatter")
    hits = leaked(glob.glob(str(pack / "*.md")))
    check(not hits, f"no buyer names in pack files {hits[:3]}")
    ah = leaked_amounts(glob.glob(str(pack / "*.md")))
    check(not ah, f"no exact deal amounts in pack files {ah[:3]}")

elif case == "weekly-review":
    r = reports("weekly-review")
    check(bool(r), "report saved to mia-reports/")
    check(any("Config:" in pathlib.Path(p).read_text(errors="replace") for p in r), "saved report ends with a Config line")
    check("mia-reports" in text, "reply states the saved path")

elif case == "forecast":
    r = reports("forecast")
    check(any(not p.endswith(".jsonl") for p in r), "report saved to mia-reports/")
    snap = ws / "mia-reports" / "snapshots.jsonl"
    check(snap.exists(), "snapshots.jsonl written")
    if snap.exists():
        lines = [l for l in snap.read_text().splitlines() if l.strip()]
        ok = bool(lines)
        for l in lines:
            try:
                json.loads(l)
            except ValueError:
                ok = False
        check(ok, "every snapshot line is valid JSON")
        check(not leaked([snap]), "no buyer names in snapshots")

elif case == "calibration-small":
    check("directional" in text.lower(), "reply runs a directional replay")
    before = (ws / ".scoring-axes.sha").read_text().strip()
    after = hashlib.sha256((ws / "mia-pack" / "scoring-axes.md").read_bytes()).hexdigest()
    check(before == after, "scoring-axes.md unchanged without approval")

elif case == "calibration-tiny":
    check(not reports("calibration"), "no report built below 8 closed deals")
    low = text.lower()
    check("csv" in low or "closed deals" in low, "reply says what is needed")
    check("replay summary" not in low and "where the criteria disagreed" not in low, "no replay sections on 6 deals")

sys.exit(1 if fails else 0)
