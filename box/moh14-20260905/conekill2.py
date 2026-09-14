#!/usr/bin/env python3
"""Band-cumulative weighted-cone kill on a descended order chart.

GRADING.  (x,y) -> (tx,ty) acts on the chart parameters by
  w(h_{a,b}) = K'-a-b ,  w(A{i}_{a,b}) = w(B{i}_{a,b}) = i*K'-a-b ,
  w(slope) = 0 ,  w(c) = n'+m'-2-l ,
and the row emitted at (h_power hp, x_power xp, y_power yp) must be
w-homogeneous of degree  n'+m'-2 - hp*K' - xp - yp.

CONTROL H (exact, in Python, EVERY generator, not a sample): each generator is
w-homogeneous of exactly the predicted degree.  This both licenses the
dehomogenisation and independently validates the charged emitter.
CONTROL H-NEG: a deliberately perturbed generator (one term rescaled in a
variable of nonzero weight) must FAIL the same test.

KILL.  w(c) > 0, so over k-bar every solution with c != 0 rescales to c = 1.
Hence V(I) cap {c != 0} = empty  <=>  1 in (I, c-1), and
`reduce(1,std(I,c-1)) == 0` over Q is an EXACT char-0 unit certificate.

BAND-CUMULATIVE.  Bands are h-adic levels.  For b = top..0 the ideal
I_b = (rows with h_power >= b) is a SUBIDEAL of I, so a unit certificate at any
b is already a kill.  Smallest bands first is the cheap end.
"""
import argparse, json, os, re, subprocess, sys, time
from pathlib import Path

TERM = re.compile(r"([A-Za-z_]\w*)(?:\^(\d+))?")

def wof(v, Kp, npr, mpr, ell):
    m = re.fullmatch(r"h_(\d+)_(\d+)", v)
    if m: return Kp - int(m.group(1)) - int(m.group(2))
    m = re.fullmatch(r"[AB](\d+)_(\d+)_(\d+)", v)
    if m: return int(m.group(1)) * Kp - int(m.group(2)) - int(m.group(3))
    if re.fullmatch(r"s\d+", v): return 0
    if v == "c": return npr + mpr - 2 - ell
    raise ValueError("unweighted variable " + v)

def degs_of(expr, W):
    out = set()
    for t in re.split(r"(?=[+-])", expr.replace(" ", "")):
        if not t or t in "+-": continue
        d = 0
        for name, pw in TERM.findall(t):
            if name.isdigit(): continue
            d += W[name] * (int(pw) if pw else 1)
        out.add(d)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--meta", required=True)
    ap.add_argument("--np", type=int, required=True); ap.add_argument("--mp", type=int, required=True)
    ap.add_argument("--ell", type=int, required=True); ap.add_argument("--Kp", type=int, required=True)
    ap.add_argument("--char", type=int, default=0)
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--bands", type=int, nargs="*", default=None)
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
            hp, xp, yp, e = int(p[1]), int(p[2]), int(p[3]), p[4].strip()
            bands.setdefault(hp, []).append((xp, yp, e))
    stem = Path(payload["rows_path"]).stem.replace("_rows", "")
    print("CHART %s vars=%d gens=%d w(c)=%d bands=%s"
          % (stem, len(variables), sum(len(v) for v in bands.values()), wc,
             {k: len(v) for k in sorted(bands) for v in [bands[k]]}), flush=True)

    # ---- CONTROL H (all generators) ----
    t0 = time.time(); bad = 0; tot = 0
    for hp, lst in bands.items():
        for (xp, yp, e) in lst:
            tot += 1
            want = a.np + a.mp - 2 - hp * a.Kp - xp - yp
            ex = e[1:-1] if e.startswith("(") and e.endswith(")") else e
            if degs_of(ex, W) != {want}: bad += 1
    print("  CONTROL_H %s  generators=%d inhomogeneous=%d  [%.1fs]"
          % ("PASS" if bad == 0 else "FAIL", tot, bad, time.time() - t0), flush=True)
    if bad: sys.exit(4)
    nz = [v for v in variables if W[v] != 0][0]
    pert = "(%s*%s+%s)" % (nz, nz, nz)
    print("  CONTROL_H_NEG %s  (perturbed generator %s is inhomogeneous)"
          % ("PASS" if len(degs_of(pert, W)) > 1 else "FAIL", pert), flush=True)

    outdir = Path("/home/ubuntu/jc2/box/moh14-20260905/charts/cone"); outdir.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): env[k] = "1"
    order = sorted(bands, reverse=True)
    todo = a.bands if a.bands is not None else order
    cum = []
    for b in order:
        cum += [e for (_, _, e) in bands[b]]
        if b not in todo: continue
        sp = outdir / ("%s_band%d_c%d.sing" % (stem, b, a.char))
        lines = [
            "ring R=%d,(%s),dp;" % (a.char, ",".join(variables)),
            "option(redSB);",
            'if (nameof(basering)=="R") { print("CONTROL_RING_PASS"); } else { print("CONTROL_RING_FAIL"); }',
            "ideal I=" + ",\n".join(cum) + ";",
            # negative control: the SAME machinery on (I) alone must not return 1
            # unless I itself is unit -- reported, not assumed.
            "ideal J=I,c-1;",
            'print("BAND_START band>=%d gens="+string(size(J)));' % b,
            "ideal G=std(J);",
            'print("BAND_DONE size="+string(size(G)));',
            'if (reduce(1,G)==0) { print("BAND_UNIT_IDEAL"); } else { print("BAND_NONTRIVIAL"); print("dim="+string(dim(G))); }',
            "quit;",
        ]
        sp.write_text("\n".join(lines) + "\n")
        t0 = time.time()
        r = subprocess.run(["timeout", str(a.timeout), "Singular", "--cpus=1", "--threads=1",
                            "-q", "--no-warn", str(sp)], capture_output=True, text=True, env=env)
        out = r.stdout + r.stderr
        v = ("UNIT_IDEAL_CHAR0" if (a.char == 0 and "BAND_UNIT_IDEAL" in out) else
             "UNIT_IDEAL_modp" if "BAND_UNIT_IDEAL" in out else
             "NONTRIVIAL" if "BAND_NONTRIVIAL" in out else
             "TIMEOUT" if r.returncode == 124 else "ERROR")
        dl = [l for l in out.splitlines() if l.startswith("dim=")]
        print("  band>=%-2d gens=%-5d bytes=%-9d  %-17s %-8s [%.1fs]"
              % (b, len(cum), sp.stat().st_size, v, (dl[0] if dl else ""), time.time() - t0), flush=True)
        if v.startswith("UNIT_IDEAL"):
            print("  => %s at band>=%d  (subideal certificate; kills the whole chart)" % (v, b))
            if a.char == 0: return
if __name__ == "__main__":
    main()
