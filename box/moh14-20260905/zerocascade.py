#!/usr/bin/env python3
"""Zero-cascade reduction of an emitted order chart, then the cone kill.

SOUNDNESS.  If a variable v lies in the ideal I (Singular reports v as a
generator of std(J) for a SUBideal J of I), then every point of V(I) has v = 0,
so substituting v := 0 in every generator leaves V(I) unchanged.  Substituting
ZERO is a purely textual operation -- drop every term containing v -- so it
costs nothing even on 51 KB rows, unlike a general pivot substitution
([[order-chart-rows-are-dense]]: a Singular subst loop on these ideals did not
finish one pass in 540 s).

Iterate: cheap bands -> new zero variables -> shrink all rows -> repeat.
Terminates when no new variable is forced to zero.  Then run the licensed cone
kill 1 in (I, c-1) on the reduced system over Q.
"""
import argparse, json, os, re, subprocess, sys, time
from pathlib import Path

TERMSPLIT = re.compile(r"(?=[+-])")
NAME = re.compile(r"[A-Za-z_]\w*")

def strip_paren(e):
    return e[1:-1] if e.startswith("(") and e.endswith(")") else e

def subst_zero(expr, zeros):
    if not zeros: return expr
    keep = []
    for t in TERMSPLIT.split(expr.replace(" ", "")):
        if not t or t in "+-": continue
        if any(n in zeros for n in NAME.findall(t)): continue
        keep.append(t)
    if not keep: return "0"
    s = "".join(k if k[0] in "+-" else "+" + k for k in keep)
    return s[1:] if s[0] == "+" else s

def sing(script, timeout):
    env = dict(os.environ)
    for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): env[k] = "1"
    r = subprocess.run(["timeout", str(timeout), "Singular", "--cpus=1", "--threads=1",
                        "-q", "--no-warn", str(script)], capture_output=True, text=True, env=env)
    return r.returncode, r.stdout + r.stderr

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--meta", required=True)
    ap.add_argument("--np", type=int, required=True); ap.add_argument("--mp", type=int, required=True)
    ap.add_argument("--ell", type=int, required=True); ap.add_argument("--Kp", type=int, required=True)
    ap.add_argument("--char", type=int, default=0)
    ap.add_argument("--seed-bands", type=int, default=2, help="bands >= this seed the cascade")
    ap.add_argument("--band-timeout", type=int, default=300)
    ap.add_argument("--final-timeout", type=int, default=1200)
    a = ap.parse_args()

    payload = json.loads(Path(a.meta).read_text())
    variables = payload["variables"]
    wc = a.np + a.mp - 2 - a.ell
    assert wc > 0
    rows_path = Path("/home/ubuntu/jc2") / payload["rows_path"]
    rows = []
    with open(rows_path, encoding="utf-8") as f:
        next(f)
        for line in f:
            p = line.rstrip("\n").split("|")
            if len(p) >= 5: rows.append((int(p[1]), strip_paren(p[4].strip())))
    stem = Path(payload["rows_path"]).stem.replace("_rows", "")
    outdir = Path("/home/ubuntu/jc2/box/moh14-20260905/charts/zero"); outdir.mkdir(parents=True, exist_ok=True)
    print("CHART %s vars=%d gens=%d w(c)=%d bytes=%d"
          % (stem, len(variables), len(rows), wc, sum(len(e) for _, e in rows)), flush=True)

    zeros, rnd = set(), 0
    while True:
        rnd += 1
        seed = [subst_zero(e, zeros) for (hp, e) in rows if hp >= a.seed_bands]
        seed = [g for g in seed if g != "0"]
        sp = outdir / ("%s_seed_r%d_c%d.sing" % (stem, rnd, a.char))
        sp.write_text("\n".join([
            "ring R=%d,(%s),dp;" % (a.char, ",".join(variables)), "option(redSB);",
            "ideal I=" + ",\n".join(seed) + ";", "ideal G=std(I);",
            'print("ZC_SIZE="+string(size(G)));',
            'int i; for (i=1;i<=size(G);i++) { if (deg(G[i])==1 && size(G[i])==1) { print("ZC_VAR "+string(G[i])); } }',
            'if (reduce(1,G)==0) { print("ZC_SEED_UNIT"); }',
            'print("ZC_DIM="+string(dim(G)));', "quit;"]) + "\n")
        rc, out = sing(sp, a.band_timeout)
        new = set()
        for ln in out.splitlines():
            if ln.startswith("ZC_VAR "):
                v = ln.split(None, 1)[1].strip()
                if v in variables: new.add(v)
        dim = [l for l in out.splitlines() if l.startswith("ZC_DIM")]
        print("  round %d: seed gens=%-4d zeros_before=%-3d new_zero_vars=%-3d %s %s"
              % (rnd, len(seed), len(zeros), len(new - zeros), (dim[0] if dim else ""),
                 "TIMEOUT" if rc == 124 else ""), flush=True)
        if not (new - zeros) or rnd > 6: break
        zeros |= new
    print("  zeros found: %d/%d  %s" % (len(zeros), len(variables), sorted(zeros)[:14]), flush=True)

    red = [(hp, subst_zero(e, zeros)) for (hp, e) in rows]
    red = [(hp, e) for (hp, e) in red if e != "0"]
    print("  reduced: gens %d -> %d ; bytes %d -> %d"
          % (len(rows), len(red), sum(len(e) for _, e in rows), sum(len(e) for _, e in red)), flush=True)
    live = [v for v in variables if v not in zeros]
    sp = outdir / ("%s_final_c%d.sing" % (stem, a.char))
    sp.write_text("\n".join([
        "ring R=%d,(%s),dp;" % (a.char, ",".join(live)), "option(redSB);",
        'if (nameof(basering)=="R") { print("CONTROL_RING_PASS"); } else { print("CONTROL_RING_FAIL"); }',
        "ideal I=" + ",\n".join(e for _, e in red) + ";",
        "ideal J=I,c-1;",
        'print("ZC_FINAL_START gens="+string(size(J))+" vars="+string(nvars(R)));',
        "ideal G=std(J);",
        'print("ZC_FINAL_SIZE="+string(size(G)));',
        'if (reduce(1,G)==0) { print("ZC_UNIT_IDEAL"); } else { print("ZC_NONTRIVIAL"); print("dim="+string(dim(G))); }',
        "quit;"]) + "\n")
    t0 = time.time(); rc, out = sing(sp, a.final_timeout)
    for ln in out.splitlines():
        if any(t in ln for t in ("ZC_", "CONTROL_", "dim=", "error")): print("   " + ln, flush=True)
    v = ("UNIT_IDEAL_CHAR0 (chart DEAD)" if (a.char == 0 and "ZC_UNIT_IDEAL" in out) else
         "UNIT_IDEAL_modp" if "ZC_UNIT_IDEAL" in out else
         "POSDIM/NONTRIVIAL" if "ZC_NONTRIVIAL" in out else
         "TIMEOUT" if rc == 124 else "ERROR")
    print("VERDICT %s [%.1fs] script=%s" % (v, time.time() - t0, sp), flush=True)

if __name__ == "__main__":
    main()
