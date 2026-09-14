#!/usr/bin/env python3
"""Phase 2 of the chart reduction: map the large rows, then pivot again.

Phase 1 (band_reduce.py, byte cap) pivots the cheap rows and produces a
resolved substitution.  Applying that substitution to the expensive h=0/h=1
rows collapses them by one to two orders of magnitude, after which a second
affine-pivot pass runs on the whole reduced system.  The result is the full
chart ideal in the surviving variables --- every original row is consumed ---
which is what goes to guided_gb.
"""
from __future__ import annotations
import argparse, hashlib, json, os, subprocess, time
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "g9966n1b3-20260903"
THREAD_ENV = {"OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1",
              "NUMEXPR_NUM_THREADS": "1", "FLINT_NUM_THREADS": "1"}


def sha256_file(p):
    d = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            d.update(b)
    return d.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reduce-json", required=True)
    ap.add_argument("--char", type=int, default=32003)
    ap.add_argument("--timeout", type=int, default=1200)
    ap.add_argument("--tag", default="phase2")
    ap.add_argument("--no-pivot", action="store_true",
                    help="map the large rows only; defer the second pivot pass")
    a = ap.parse_args()
    rec = json.loads(Path(a.reduce_json).read_text())
    meta = json.loads(Path(rec["meta"]).read_text())
    log = Path(rec["log"]).read_text().splitlines()
    subs = [ln.split("|", 2)[1:] for ln in log if ln.startswith("SUBST|")]
    variables = list(meta["variables"])
    variables.sort(key=lambda n: (0 if n.startswith("A1_") else 1 if n.startswith("A2_")
                                  else 2 if n.startswith("A3_") else 3 if n.startswith("B")
                                  else 4 if n.startswith("h_") else 5, n))
    variables.append("T")
    img = {v: v for v in variables}
    for v, e in subs:
        img[v] = "(" + e + ")"
    cap = rec["cap_bytes"]
    rows = []
    with open(meta["rows_path"]) as f:
        f.readline()
        for line in f:
            s, h, x, y, e = line.rstrip("\n").split("|", 4)
            rows.append((len(e), int(h), int(s), e))
    rows.sort()
    big = [e for L, h, s, e in rows if L > cap]
    stem = Path(rec["meta"]).stem
    d = HERE / "reduced" / stem
    residual2 = d / f"residual_{a.tag}.txt"
    S = [f"ring R={a.char},({','.join(variables)}),dp;", "option(redSB);", "int t0=timer;",
         "ideal IMG = " + ",".join(img[v] for v in variables) + ";",
         "intvec SLOT; int NP=0;", f"int NOPIV={1 if a.no_pivot else 0};",
         "ideal RES; int NR=0; poly gg; poly dd; poly rr; int kk; int hit;",
         "proc addrow(poly g)",
         "{",
         "  map PH = basering, IMG; g = PH(g); kill PH;",
         "  if (g == 0) { return(); }",
         "  int k;",
         ("  if (NOPIV == 1) { NR = NR + 1; RES[NR] = g; return(); }"),
         "  for (k = 1; k <= nvars(basering); k++) {",
         "    dd = diff(g, var(k));",
         "    if (dd != 0) { if (deg(dd) == 0) {",
         "      rr = subst(g, var(k), 0);",
         "      IMG[k] = -rr/dd;",
         "      map PS = basering, IMG; IMG = PS(IMG); kill PS;",
         "      NP = NP + 1; SLOT[NP] = k;",
         "      return();",
         "    } }",
         "  }",
         "  NR = NR + 1; RES[NR] = g;",
         "}"]
    prior = [ln.rstrip(";") for ln in Path(rec["residual_file"]).read_text().splitlines()
             if ln.strip()]
    for i, g in enumerate(prior):
        S.append(f"addrow({g});")
    for i, e in enumerate(big):
        S.append(f"gg = ({e}); addrow(gg);")
        S.append(f'"P2ROW|{i}|"+string(NP)+"|"+string(NR)+"|"+string(timer-t0);')
    S += ["map FIN = R, IMG; RES = simplify(FIN(RES), 2); NR = size(RES);",
          'int z0; for (z0=1; z0<=NP; z0++) '
          '{ "SUBST|"+string(var(SLOT[z0]))+"|"+string(IMG[SLOT[z0]]); }',
          '"PIVOTS2="+string(NP);', '"RESIDUAL_ROWS2="+string(NR);',
          f'link LL=":w {residual2}"; write(LL,"");',
          f'int z2; for (z2=1; z2<=NR; z2++) {{ write(":a {residual2}", string(RES[z2])); }}',
          '"PHASE2_DONE";', "quit;"]
    script = d / f"{a.tag}.sing"
    script.write_text("\n".join(S))
    env = os.environ.copy(); env.update(THREAD_ENV)
    logp = d / f"{a.tag}.log"
    t0 = time.monotonic()
    with open(logp, "w") as o:
        r = subprocess.run(["timeout", str(a.timeout), "stdbuf", "-oL", "Singular", "--cpus=1",
                            "--threads=1", "--flint-threads=1", "--no-rc", "-q", str(script)],
                           cwd=ROOT, env=env, stdout=o, stderr=subprocess.STDOUT, check=False)
    text = logp.read_text(errors="replace")
    get = lambda k: next((ln.split("=", 1)[1] for ln in text.splitlines()
                          if ln.startswith(k + "=")), None)
    piv = [ln.split("|", 2)[1] for ln in text.splitlines() if ln.startswith("SUBST|")]
    out = {"phase": 2, "meta": rec["meta"], "characteristic": a.char,
           "phase1_json": str(a.reduce_json), "phase1_pivots": rec["pivots"],
           "big_rows_mapped": len(big), "prior_residual_rows": len(prior),
           "input_rows": rec["input_rows"], "script": str(script),
           "script_sha256": sha256_file(script), "rows_sha256": rec["rows_sha256"],
           "returncode": r.returncode, "timed_out": r.returncode == 124,
           "elapsed_seconds": round(time.monotonic() - t0, 3),
           "done": "PHASE2_DONE" in text, "errors": text.count("? error"),
           "pivots": len(piv), "pivot_variables": piv,
           "residual_rows": get("RESIDUAL_ROWS2"),
           "residual_file": str(residual2),
           "residual_sha256": sha256_file(residual2) if residual2.exists() else None,
           "surviving_variables": sorted(set(variables) - set(piv)),
           "cap_bytes": cap, "rows_used": rec["input_rows"], "log": str(logp)}
    out["surviving_variable_count"] = len(out["surviving_variables"])
    (d / f"{a.tag}.json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in out.items()
                      if k not in ("pivot_variables", "surviving_variables")}, indent=1))


if __name__ == "__main__":
    main()
