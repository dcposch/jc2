#!/usr/bin/env python3
"""Incremental band-wise weighted-cone kill (the productive shape).

Same grading, controls and dehomogenisation licence as conekill2.py.  The
difference is the solve: instead of one std over all 261 expanded generators,
the bands are added h-adically top-down, each new band REDUCED modulo the
running standard basis before it is joined.  This is the band-wise elimination
[[order-chart-rows-are-dense]] recommends; the expanded monolith is the known
input-size failure mode.

Every intermediate ideal is a subideal of the full chart ideal, so a unit
certificate at ANY stage kills the whole chart.
"""
import argparse, json, os, re, subprocess, sys, time
from pathlib import Path
sys.path.insert(0, "/home/ubuntu/jc2/box/moh14-20260905")
from conekill2 import wof, degs_of

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--meta", required=True)
    ap.add_argument("--np", type=int, required=True); ap.add_argument("--mp", type=int, required=True)
    ap.add_argument("--ell", type=int, required=True); ap.add_argument("--Kp", type=int, required=True)
    ap.add_argument("--char", type=int, default=0)
    ap.add_argument("--timeout", type=int, default=2400)
    a = ap.parse_args()
    payload = json.loads(Path(a.meta).read_text())
    variables = payload["variables"]
    W = {v: wof(v, a.Kp, a.np, a.mp, a.ell) for v in variables}
    wc = a.np + a.mp - 2 - a.ell
    assert wc > 0
    rows_path = Path("/home/ubuntu/jc2") / payload["rows_path"]
    bands = {}
    with open(rows_path, encoding="utf-8") as f:
        next(f)
        for line in f:
            p = line.rstrip("\n").split("|")
            if len(p) < 5: continue
            bands.setdefault(int(p[1]), []).append((int(p[2]), int(p[3]), p[4].strip()))
    stem = Path(payload["rows_path"]).stem.replace("_rows", "")
    print("CHART %s vars=%d gens=%d w(c)=%d" % (stem, len(variables),
          sum(len(v) for v in bands.values()), wc), flush=True)
    bad = 0
    for hp, lst in bands.items():
        for (xp, yp, e) in lst:
            ex = e[1:-1] if e.startswith("(") and e.endswith(")") else e
            if degs_of(ex, W) != {a.np + a.mp - 2 - hp * a.Kp - xp - yp}: bad += 1
    print("  CONTROL_H %s inhomogeneous=%d" % ("PASS" if bad == 0 else "FAIL", bad), flush=True)
    if bad: sys.exit(4)

    outdir = Path("/home/ubuntu/jc2/box/moh14-20260905/charts/cone"); outdir.mkdir(parents=True, exist_ok=True)
    sp = outdir / ("%s_inc_c%d.sing" % (stem, a.char))
    order = sorted(bands, reverse=True)
    L = ["ring R=%d,(%s),dp;" % (a.char, ",".join(variables)),
         "option(redSB);",
         'if (nameof(basering)=="R") { print("CONTROL_RING_PASS"); } else { print("CONTROL_RING_FAIL"); }',
         "ideal G=c-1;", "ideal NB; ideal RD; int i;"]
    for b in order:
        gens = [e for (_, _, e) in bands[b]]
        L += ["NB=" + ",\n".join(gens) + ";",
              'print("INC_BAND %d gens="+string(size(NB)));' % b,
              "RD=reduce(NB,G);",
              'print("INC_REDUCED nonzero="+string(size(simplify(RD,2))));',
              "G=std(G+RD);",
              'print("INC_STD band=%d size="+string(size(G)));' % b,
              'if (reduce(1,G)==0) { print("INC_UNIT_IDEAL band=%d"); quit; }' % b,
              'print("INC_DIM band=%d dim="+string(dim(G)));' % b]
    L += ['print("INC_END_NONTRIVIAL");', "quit;"]
    sp.write_text("\n".join(L) + "\n")
    env = dict(os.environ)
    for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): env[k] = "1"
    t0 = time.time()
    r = subprocess.run(["timeout", str(a.timeout), "Singular", "--cpus=1", "--threads=1",
                        "-q", "--no-warn", str(sp)], capture_output=True, text=True, env=env)
    out = r.stdout + r.stderr
    for ln in out.splitlines():
        if any(t in ln for t in ("INC_", "CONTROL_", "error", "?")): print("   " + ln, flush=True)
    v = ("UNIT_IDEAL_CHAR0 (chart DEAD)" if (a.char == 0 and "INC_UNIT_IDEAL" in out) else
         "UNIT_IDEAL_modp" if "INC_UNIT_IDEAL" in out else
         "POSDIM/NONTRIVIAL" if "INC_END_NONTRIVIAL" in out else
         "TIMEOUT" if r.returncode == 124 else "ERROR")
    print("VERDICT %s [%.1fs] script=%s" % (v, time.time() - t0, sp), flush=True)
main()
