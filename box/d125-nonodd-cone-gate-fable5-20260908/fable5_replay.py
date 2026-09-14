"""Replay the charged nonodd checker byte-copy from fresh scratch, 10 modes, explicit limits."""
import hashlib, json, subprocess, sys, time, os
box = os.path.dirname(os.path.abspath(__file__))
script = os.path.join(box, "scratch", "nonodd-check.py")
modes = ["positive", "--omit-b4", "--omit-b2", "--partial-constant-shear", "--wrong-f"]
runs = []
t0 = time.time()
for opt in (False, True):
    for m in modes:
        argv = ["/usr/bin/timeout", "30", "/usr/bin/prlimit", "--cpu=25", "--as=536870912",
                "/usr/bin/python3", "-I", "-B"] + (["-O"] if opt else []) + [script] + ([] if m == "positive" else [m])
        t = time.time()
        p = subprocess.run(argv, capture_output=True, text=True, cwd=os.path.join(box, "scratch"))
        err_line = [l for l in p.stderr.splitlines() if l.startswith("ValueError")]
        runs.append({"argv": argv, "mode": m, "optimized": opt, "rc": p.returncode,
                     "wall_seconds": time.time() - t,
                     "stdout": p.stdout, "stdout_sha256": hashlib.sha256(p.stdout.encode()).hexdigest(),
                     "stderr": p.stderr, "stderr_sha256": hashlib.sha256(p.stderr.encode()).hexdigest(),
                     "error_line": err_line[-1] if err_line else ""})
out = {"script_sha256": hashlib.sha256(open(script, "rb").read()).hexdigest(),
       "elapsed": time.time() - t0, "runs": runs}
json.dump(out, open(os.path.join(box, "fable5-replay.json"), "w"), indent=1, sort_keys=True)
for r in runs:
    print(r["mode"], "-O" if r["optimized"] else "  ", "rc=%d" % r["rc"], "%.2fs" % r["wall_seconds"], r["stdout"].strip() or r["error_line"])
