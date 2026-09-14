#!/usr/bin/python3
"""Fable 5.1 gate replay driver: runs charged standalone checkers byte-copied into fresh scratch.
Each arithmetic child: /usr/bin/timeout 30 /usr/bin/prlimit --cpu=25 --as=536870912 /usr/bin/python3 -I -B [-O] script [mode]
"""
import sys
sys.dont_write_bytecode = True
import json, subprocess, hashlib, time, os, re

SCR = os.path.dirname(os.path.abspath(__file__))
PLAN = [
    ("consumer-check.py", [["normal"], ["change-q0"], ["drop-d0-shift"], ["change-quartic"], ["replace-odd-e"]]),
    ("cone-counter-check.py", [["normal"], ["freeze-moving-root"], ["change-central-curve"], ["replace-F"]]),
    ("source-first-contact-check.py", [[], ["positive"], ["--omit-alpha-cross"], ["--omit-gamma"], ["--partial-shear"]]),
]
def sha(b): return hashlib.sha256(b).hexdigest()
runs = []
t0 = time.time()
for script, modes in PLAN:
    path = os.path.join(SCR, script)
    for opt in (False, True):
        for mode in modes:
            argv = ["/usr/bin/timeout", "30", "/usr/bin/prlimit", "--cpu=25", "--as=536870912",
                    "/usr/bin/python3", "-I", "-B"] + (["-O"] if opt else []) + [path] + mode
            t = time.time()
            p = subprocess.run(argv, capture_output=True, cwd=SCR, env={"PATH": "/usr/bin:/bin"})
            err = p.stderr.decode(errors="replace")
            m = re.findall(r"^(\w+Error: .*)$", err, re.M)
            runs.append({"script": script, "script_sha256": sha(open(path, "rb").read()),
                         "mode": mode[0] if mode else "(no-arg positive)", "optimized": opt,
                         "returncode": p.returncode, "wall_seconds": round(time.time() - t, 4),
                         "stdout_sha256": sha(p.stdout), "stdout_bytes": len(p.stdout),
                         "stderr_sha256": sha(p.stderr), "stderr_error_line": (m[-1] if m else ""),
                         "stdout": p.stdout.decode(errors="replace") if p.returncode == 0 else ""})
out = {"driver": "fable5_replay.py", "scratch": SCR, "elapsed_seconds": round(time.time() - t0, 3),
       "caps": {"wall_seconds": 30, "cpu_seconds": 25, "as_bytes": 536870912}, "runs": runs}
json.dump(out, open(os.path.join(SCR, "fable5-replay.json"), "w"), indent=1, sort_keys=True)
for r in runs:
    print(f"{r['script']:32s} {r['mode']:22s} -O={int(r['optimized'])} rc={r['returncode']} out={r['stdout_sha256'][:16]} err={r['stderr_error_line'][:60]}")
