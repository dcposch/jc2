#!/usr/bin/env python3
"""One-shot status of the two endpoint jobs (for the hq monitor)."""
import json, subprocess, pathlib

def live():
    try:
        out = subprocess.check_output(["pgrep", "-af", "replay_engine.py"], text=True)
    except subprocess.CalledProcessError:
        out = ""
    names = []
    for line in out.splitlines():
        if "python3 -u" not in line:
            continue
        if "delta2 --stage 4" in line:
            names.append("d2s4")
        if "delta52 --stage 8" in line:
            names.append("d52s8")
    return names

def load(path):
    p = pathlib.Path(path)
    if not p.exists() or p.stat().st_size < 80:
        return None
    try:
        return json.loads(p.read_text())
    except Exception:
        return None

def last(path):
    p = pathlib.Path(path)
    if not p.exists():
        return ""
    lines = p.read_text(errors="replace").splitlines()
    return lines[-1] if lines else ""

jobs = {
    "d2s4": ("/home/ubuntu/g9966-d2-replay/runs/delta2/stage4.json",
             "/home/ubuntu/g9966-d2-replay/runs/delta2/stage4.err"),
    "d52s8": ("/home/ubuntu/g9966-d2-replay/runs/delta52/stage8.json",
              "/home/ubuntu/g9966-d2-replay/runs/delta52/stage8.err"),
}
running = live()
chunks = []
for name, (jp, err) in jobs.items():
    d = load(jp)
    v = d.get("verdict") if d else None
    dim = (d.get("counts") or {}).get("exact_Krull_dimension_localized") if d else None
    tail = last(err).replace("|", "/")
    chunks.append(f"{name}|{v}|{dim}|{'run' if name in running else 'stop'}|{tail}")
print("::".join(chunks))
