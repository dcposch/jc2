#!/usr/bin/env python3
"""Weighted-cone kill test on an emitted descended order chart.

GRADING.  The chart's solution set is invariant under (x,y) -> (tx,ty), which
acts on the parameters by  w(h_{a,b}) = K'-a-b,  w(A{i}_{a,b}) = w(B{i}_{a,b})
= i*K'-a-b,  w(slope) = 0,  w(c) = n'+m'-2-l.  Singular verifies homog(I,W)
INDEPENDENTLY -- a free self-check on the emitter, not an assumption.

KILL.  w(c) > 0, so over k-bar any solution with c != 0 can be rescaled to c=1
(solve t^{w(c)} = 1/c).  Hence
      V(I) cap {c != 0} = empty   <=>   1 in (I, c-1).
`reduce(1, std(I, c-1)) == 0` over Q is therefore an EXACT char-0 certificate
(no modular step, no properness argument).  See [[homogeneous-cone-unit-test]],
[[k4ray-chart-grading-and-kill-test]].
"""
import argparse, json, os, re, subprocess, sys, time
from pathlib import Path

def weights(variables, Kp, npr, mpr, ell):
    W = []
    for v in variables:
        m = re.fullmatch(r"h_(\d+)_(\d+)", v)
        if m: W.append(Kp - int(m.group(1)) - int(m.group(2))); continue
        m = re.fullmatch(r"[AB](\d+)_(\d+)_(\d+)", v)
        if m: W.append(int(m.group(1)) * Kp - int(m.group(2)) - int(m.group(3))); continue
        if re.fullmatch(r"s\d+", v): W.append(0); continue
        if v == "c": W.append(npr + mpr - 2 - ell); continue
        raise ValueError("unweighted variable " + v)
    return W

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--meta", required=True)
    ap.add_argument("--np", type=int, required=True)
    ap.add_argument("--mp", type=int, required=True)
    ap.add_argument("--ell", type=int, required=True)
    ap.add_argument("--Kp", type=int, required=True)
    ap.add_argument("--char", type=int, default=0)
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--algorithm", default="std")
    a = ap.parse_args()

    payload = json.loads(Path(a.meta).read_text())
    rows_path = Path("/home/ubuntu/jc2") / payload["rows_path"]
    variables = payload["variables"]
    W = weights(variables, a.Kp, a.np, a.mp, a.ell)
    wc = a.np + a.mp - 2 - a.ell
    assert wc > 0, "w(c) must be positive for the dehomogenisation"
    assert min(W) >= 1, "wp ordering needs strictly positive weights; min=%s" % min(W)
    gens = []
    with open(rows_path, encoding="utf-8") as f:
        next(f)
        for line in f:
            p = line.rstrip("\n").split("|")
            if len(p) >= 5: gens.append(p[4])
    outdir = Path("/home/ubuntu/jc2/box/moh14-20260905/charts/cone"); outdir.mkdir(parents=True, exist_ok=True)
    stem = Path(payload["rows_path"]).stem.replace("_rows", "")
    sp = outdir / ("%s_cone_c%d_%s.sing" % (stem, a.char, a.algorithm))
    alg = "std(J)" if a.algorithm == "std" else "slimgb(J)"
    lines = [
        "intvec W=%s;" % ",".join(map(str, W)),
        # CONTROL ring: positive weighted ordering; homog() there is the real
        # weighted-homogeneity test (homog(I,intvec) is NOT that signature).
        "ring RW=%d,(%s),wp(W);" % (a.char, ",".join(variables)),
        "ideal IW=" + ",\n".join(gens) + ";",
        'if (homog(IW)==1) { print("CONTROL_HOMOG_PASS"); } else { print("CONTROL_HOMOG_FAIL"); }',
        "ideal IWP=IW,c-1;",
        'if (homog(IWP)==0) { print("CONTROL_PERTURB_PASS"); } else { print("CONTROL_PERTURB_FAIL"); }',
        "ring R=%d,(%s),dp;" % (a.char, ",".join(variables)),
        "option(redSB);",
        "ideal I=imap(RW,IW);",
        'print("CONE_VARS="+string(nvars(R))+" GENS="+string(size(I))+" WC=%d");' % wc,
        'print("CONE_START");',
        "ideal J=I,c-1;",
        "ideal G=%s;" % alg,
        'print("CONE_DONE size="+string(size(G)));',
        'if (reduce(1,G)==0) { print("CONE_UNIT_IDEAL_CHAR0"); } else { print("CONE_NONTRIVIAL"); print("dim="+string(dim(G))); }',
        "quit;",
    ]
    sp.write_text("\n".join(lines) + "\n")
    env = dict(os.environ)
    for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): env[k] = "1"
    t0 = time.time()
    r = subprocess.run(["timeout", str(a.timeout), "Singular", "--cpus=1", "--threads=1",
                        "-q", "--no-warn", str(sp)], capture_output=True, text=True, env=env)
    out = r.stdout + r.stderr
    dt = time.time() - t0
    for ln in out.splitlines():
        if any(t in ln for t in ("CONE_", "CONTROL_", "dim=", "error", "?")): print("   " + ln)
    v = ("UNIT_IDEAL_CHAR0 (row/chart DEAD)" if "CONE_UNIT_IDEAL_CHAR0" in out else
         "POSDIM/NONTRIVIAL" if "CONE_NONTRIVIAL" in out else
         "TIMEOUT" if r.returncode == 124 else "ERROR")
    print("VERDICT %s  [%.1fs]  script=%s" % (v, dt, sp))
main()
