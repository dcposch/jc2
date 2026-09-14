#!/usr/bin/env python3
"""Affine pivot reduction of an order chart, run natively in Singular.

These charts are dense (the S1 [5] chart is 51 MB of generators), so a
monolithic std() never returns.  This reducer streams the rows in increasing
size --- which is essentially the h-adic band order, top band first --- pushing
each row through the accumulated substitution before looking for a new pivot.

A row whose derivative in some variable v is a nonzero CONSTANT equals
c*v + (terms free of v), so v = -(row|_{v=0})/c exactly.  Eliminating v is a
triangular ring automorphism of Q[vars], hence ideal preserving: the residual
system generates the same ideal after the change of variables, and in
particular is the unit ideal iff the original chart is.  There is no choice, no
localization, and no support truncation.

Substitutions are applied with a Singular ``map``, i.e. one evaluation pass per
row rather than one pass per pivot.
"""
from __future__ import annotations

import argparse, hashlib, json, os, subprocess, time
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "g9966n1b3-20260903"
THREAD_ENV = {"OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1",
              "NUMEXPR_NUM_THREADS": "1", "FLINT_NUM_THREADS": "1"}

PROLOG = r"""
int t0 = timer;
ideal IMG = maxideal(1);          // resolved substitution, as a self-map of R
intvec SLOT; int NP = 0;
ideal RES; int NR = 0;
poly gg; poly dd; poly rr; int kk; int aa; int hit;

proc record(int slot, poly rhs)
{
  IMG[slot] = rhs;                                  // then resolve chains
  map PSI = basering, IMG;
  IMG = PSI(IMG);
  kill PSI;
  map CHI = basering, IMG;
  RES = simplify(CHI(RES), 2);
  kill CHI;
  NR = size(RES);
  NP = NP + 1;
  SLOT[NP] = slot;                    // publish the RESOLVED image, not this rhs
}
"""

ROW_BLOCK = r"""
gg = %(EXPR)s;
map MP%(N)s = R, IMG; gg = MP%(N)s(gg); kill MP%(N)s;
if (gg != 0) {
  hit = 0;
  for (kk = 1; kk <= nvars(basering); kk++) {
    dd = diff(gg, var(kk));
    if (dd != 0) { if (deg(dd) == 0) {
      rr = subst(gg, var(kk), 0);
      record(kk, -rr/dd);
      hit = 1;
      break;
    } }
  }
  if (hit == 0) { NR = NR + 1; RES[NR] = gg; }
}
"ROW|%(N)s|"+string(NP)+"|"+string(NR)+"|"+string(timer-t0);
"""


def sha256_file(p):
    d = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            d.update(b)
    return d.hexdigest()


def read_rows(path):
    out = []
    with open(path) as src:
        assert src.readline().rstrip("\n") == "source_index|h_power|x_power|y_power|expr"
        for line in src:
            if line.strip():
                s, h, x, y, e = line.rstrip("\n").split("|", 4)
                out.append({"i": int(s), "h": int(h), "x": int(x), "y": int(y), "expr": e})
    return out


def build_script(meta_path, characteristic, residual_out, order, cap):
    payload = json.loads(Path(meta_path).read_text())
    variables = list(payload["variables"])
    if order == "coefficient-first":
        variables.sort(key=lambda n: (0 if n.startswith("A1_") else 1 if n.startswith("A2_")
                                      else 2 if n.startswith("A3_") else 3 if n.startswith("B")
                                      else 4 if n.startswith("h_") else 5, n))
    variables = variables + ["T"]
    rows = read_rows(payload["rows_path"])
    rows.sort(key=lambda r: (len(r["expr"]), -r["h"], r["i"]))
    used = [r for r in rows if not cap or len(r["expr"]) <= cap]
    parts = [f"ring R={characteristic},({','.join(variables)}),dp;", "option(redSB);", PROLOG]
    parts.append(ROW_BLOCK % {"EXPR": f"T*({payload['sat']})-1", "N": "0"})
    for n, r in enumerate(used, 1):
        parts.append(ROW_BLOCK % {"EXPR": f"({r['expr']})", "N": str(n)})
    parts.append('int z0; for (z0=1; z0<=NP; z0++) '
                 '{ "SUBST|"+string(var(SLOT[z0]))+"|"+string(IMG[SLOT[z0]]); }')
    parts.append('"PIVOTS="+string(NP);')
    parts.append('"RESIDUAL_ROWS="+string(NR);')
    parts.append(f'link LL = ":w {residual_out}"; write(LL, "");')
    parts.append(f'int z2; for (z2=1; z2<=NR; z2++)'
                 f' {{ write(":a {residual_out}", string(RES[z2])); }}')
    parts.append('ideal GB = std(RES); "RES_UNIT="+string(size(reduce(1,GB))==0);')
    parts.append('"RES_DIM="+string(dim(GB)); "RES_SIZE="+string(size(GB));')
    parts.append('"REDUCE_DONE";')
    parts.append("quit;")
    return "\n".join(parts), payload, variables, rows, used


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--meta", required=True)
    ap.add_argument("--char", type=int, default=0)
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--order", default="coefficient-first")
    ap.add_argument("--tag", default="")
    ap.add_argument("--cap", type=int, default=0)
    args = ap.parse_args()
    stem = Path(args.meta).stem
    tag = args.tag or ("Q" if args.char == 0 else f"p{args.char}")
    out_dir = HERE / "reduced" / stem
    out_dir.mkdir(parents=True, exist_ok=True)
    residual_out = out_dir / f"residual_{tag}.txt"
    script, payload, variables, rows, used = build_script(args.meta, args.char, residual_out,
                                                          args.order, args.cap)
    script_path = out_dir / f"reduce_{tag}.sing"
    script_path.write_text(script)
    env = os.environ.copy(); env.update(THREAD_ENV)
    log = out_dir / f"reduce_{tag}.log"
    t0 = time.monotonic()
    with open(log, "w") as o:
        r = subprocess.run(["timeout", str(args.timeout), "stdbuf", "-oL", "Singular",
                            "--cpus=1", "--threads=1", "--flint-threads=1", "--no-rc", "-q",
                            str(script_path)], cwd=ROOT, env=env, stdout=o,
                           stderr=subprocess.STDOUT, check=False)
    text = log.read_text(errors="replace")
    get = lambda k: next((ln.split("=", 1)[1] for ln in text.splitlines()
                          if ln.startswith(k + "=")), None)
    piv = [ln.split("|", 2)[1] for ln in text.splitlines() if ln.startswith("SUBST|")]
    rec = {"meta": str(args.meta), "characteristic": args.char, "order": args.order,
           "cap_bytes": args.cap, "script": str(script_path),
           "script_sha256": sha256_file(script_path),
           "rows_sha256": sha256_file(payload["rows_path"]),
           "input_rows": len(rows), "rows_used": len(used), "variables_in": len(variables),
           "returncode": r.returncode, "timed_out": r.returncode == 124,
           "elapsed_seconds": round(time.monotonic() - t0, 3),
           "done": "REDUCE_DONE" in text, "errors": text.count("? error"),
           "pivots": len(piv), "pivot_variables": piv,
           "residual_rows": get("RESIDUAL_ROWS"),
           "residual_unit": get("RES_UNIT"), "residual_dim": get("RES_DIM"),
           "residual_basis_size": get("RES_SIZE"),
           "residual_file": str(residual_out),
           "residual_sha256": sha256_file(residual_out) if residual_out.exists() else None,
           "surviving_variables": sorted(set(variables) - set(piv)),
           "log": str(log)}
    rec["surviving_variable_count"] = len(rec["surviving_variables"])
    (out_dir / f"reduce_{tag}.json").write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in rec.items()
                      if k not in ("pivot_variables", "surviving_variables")}, indent=1))


if __name__ == "__main__":
    main()
