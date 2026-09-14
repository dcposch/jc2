#!/usr/bin/env python3
"""Cheap-subideal kill test on an emitted order chart.

SOUNDNESS.  If J subset I and (J : sat^inf) = (1), then (I : sat^inf) = (1).
So a SATURATED-EMPTY on a SUBSET of the emitted generators is a valid kill of
the full chart.  The converse is not used: a non-unit subideal proves nothing.
Rows are taken smallest-first (shortest expanded expression), which is where the
monomial and few-term rows live.
"""
import argparse, json, os, subprocess, sys, time
from pathlib import Path

def read_rows(p):
    out = []
    with open(p, encoding="utf-8") as f:
        next(f)
        for line in f:
            parts = line.rstrip("\n").split("|")
            if len(parts) >= 5:
                out.append({"i": int(parts[0]), "h": int(parts[1]),
                            "x": int(parts[2]), "y": int(parts[3]), "e": parts[4]})
    return out

def run(script, timeout):
    env = dict(os.environ)
    for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
        env[k] = "1"
    t0 = time.time()
    r = subprocess.run(["timeout", str(timeout), "Singular", "--cpus=1", "--threads=1",
                        "-q", "--no-warn", str(script)],
                       capture_output=True, text=True, env=env)
    return r.returncode, r.stdout + r.stderr, time.time() - t0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--meta", required=True)
    ap.add_argument("--take", type=int, nargs="+", default=[40, 80, 140])
    ap.add_argument("--char", type=int, default=0)
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--tag", default="sub")
    a = ap.parse_args()

    payload = json.loads(Path(a.meta).read_text())
    rows_path = Path("/home/ubuntu/jc2") / payload["rows_path"]
    rows = read_rows(rows_path)
    rows.sort(key=lambda r: len(r["e"]))
    variables = payload["variables"] + ["T"]
    sat = payload["sat"]
    outdir = Path("/home/ubuntu/jc2/box/moh14-20260905/charts/sub")
    outdir.mkdir(parents=True, exist_ok=True)
    stem = Path(payload["rows_path"]).stem.replace("_rows", "")
    print("CHART %s  rows=%d unknowns=%d sat=%s" % (stem, len(rows), len(payload["variables"]), sat), flush=True)

    for take in a.take:
        sel = rows[:take]
        gens = [r["e"] for r in sel] + ["T*(%s)-1" % sat]
        sp = outdir / ("%s_%s_take%d_c%d.sing" % (stem, a.tag, take, a.char))
        lines = [
            "ring R=%d,(%s),dp;" % (a.char, ",".join(variables)),
            "option(redSB);",
            'if (nameof(basering)=="R") { print("CONTROL_RING_PASS"); } else { print("CONTROL_RING_FAIL"); }',
            "ideal CE=(%s),T*(%s)-1;" % (sat, sat),
            'if (reduce(1,std(CE))==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }',
            "ideal CN=(%s)-1,T*(%s)-1;" % (sat, sat),
            'if (reduce(1,std(CN))!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }',
            'print("SUB_START take=%d maxlen=%d");' % (take, max(len(r["e"]) for r in sel)),
            "ideal I=" + ",\n".join(gens) + ";",
            "ideal G=std(I);",
            'print("SUB_DONE size="+string(size(G)));',
            'if (reduce(1,G)==0) { print("SUB_UNIT_IDEAL"); } else { print("SUB_NONTRIVIAL"); print("dim="+string(dim(G))); }',
            "quit;",
        ]
        sp.write_text("\n".join(lines) + "\n")
        rc, out, dt = run(sp, a.timeout)
        verdict = ("UNIT_IDEAL" if "SUB_UNIT_IDEAL" in out else
                   "NONTRIVIAL" if "SUB_NONTRIVIAL" in out else
                   "TIMEOUT" if rc == 124 else "ERROR")
        ctl = [t for t in ("CONTROL_RING_PASS", "CONTROL_EMPTY_PASS", "CONTROL_NONEMPTY_PASS") if t in out]
        dimline = [l for l in out.splitlines() if l.startswith("dim=")]
        print("  take=%-4d bytes=%-9d  %-11s  controls=%d/3  %s  [%.1fs]"
              % (take, sp.stat().st_size, verdict, len(ctl),
                 (dimline[0] if dimline else ""), dt), flush=True)
        if verdict == "UNIT_IDEAL":
            print("  => KILL: subideal of %d generators is already the unit ideal after saturation" % take)
            return
main()
