#!/usr/bin/env python3
"""Top-tail quadratics on b4=1 and their b3-resultants (lane k16toptail).

Reuses the charged recurrence emitter (singular_terminal_driver.emit, copied
unchanged into this box) to build the exact terminal rows T_(t,k) with b4
FREE, then appends an analysis block:
  (A) weighted-homogeneity of every positive row in the declared wp ring;
  (B) b3-degree and the b3^2/b3^1/b3^0 coefficients of the top tail
      (band k=t..2t-1), with weighted degrees and supports;
  (C) Res_b3(T_(2t-1), T_k) for k=1..2t-2 with b4 free: homogeneity and
      weight 8t+2-2k;
  (D) b4=1: the ideal of top-tail resultants, of all resultants, and the full
      chart; unit tests (reduce(1,std)) and dims;
  (E) b4=0: top-weight parts of the resultants, dim in the q-ring;
      also the b4=0 top-tail cone.
Every std call is exact over the declared coefficient field (minpoly encoding
in --mode exact; rational fibre in --mode split-exact).  T[k] here is the
question convention T=[X^k]E (driver sign).
"""
from __future__ import annotations
import argparse, json, pathlib, subprocess, time, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from singular_terminal_driver import emit, ring_header  # charged emitter, unchanged

HERE = pathlib.Path(__file__).resolve().parent

def analysis(t: int, mode: str, prime, branch, do_full: bool, do_lower: bool) -> str:
    q = 2*t+1
    resid = ["b4"] + [f"q{j}_0" for j in range(2, t)] + ["b3"]
    wts = [1] + list(range(2, t)) + [t+1]
    qv = [f"q{j}_0" for j in range(2, t)]
    hdrW, _ = ring_header(t, mode, prime, branch, resid)
    hdrW = [l.replace("ring R=", "ring W=", 1).replace(",dp;", f",wp({','.join(map(str,wts))});") for l in hdrW]
    hdrQ, _ = ring_header(t, mode, prime, branch, qv if qv else ["dummy"])
    hdrQ = [l.replace("ring R=", "ring Wq=", 1) for l in hdrQ]
    hdrB, _ = ring_header(t, mode, prime, branch, qv + ["b3"])
    hdrB = [l.replace("ring R=", "ring Wb=", 1) for l in hdrB]
    L = ["// ---- k16toptail analysis ----",
         "ideal TTR=" + ",".join(f"T{k}" for k in range(1, 2*t)) + ";",
         "ideal T0R=T0;",
         *hdrW,
         "ideal TT=imap(R,TTR);", "ideal T0=imap(R,T0R);",
         f"int tt={t}; int k; int r; string s1; string s2; int ii; int mm; int NN;",
         "// (A) homogeneity in the wp ring; and eliminated variables absent",
         "for (k=1; k<=2*tt-1; k++) {",
         "  s1=string(deg(TT[k])); s2=string(homog(TT[k]));",
         "  print(\"ROW band=\"+string(k)+\" wdeg=\"+s1+\" homog=\"+s2+\" size=\"+string(size(TT[k])));",
         "}",
         "poly tau=T0[1]-jet(T0[1],0); print(\"TAU wdeg=\"+string(deg(tau))+\" homog=\"+string(homog(tau))+\" T0const=\"+string(jet(T0[1],0)));",
         "// (B) b3-structure of the top tail",
         "matrix CM;",
         "for (k=tt; k<=2*tt-1; k++) {",
         "  r=2*tt-1-k;",
         "  CM=coeffs(TT[k],b3);",
         "  print(\"TOP band=\"+string(k)+\" r=\"+string(r)+\" deg_b3=\"+string(nrows(CM)-1));",
                  "  for (ii=1; ii<=nrows(CM); ii++) {",
         "    print(\"  COEF b3^\"+string(ii-1)+\" wdeg=\"+string(deg(CM[ii,1]))+\" homog=\"+string(homog(CM[ii,1]))+\" size=\"+string(size(CM[ii,1]))+\" vars=\"+string(variables(CM[ii,1])));",
         "  }",
         "  if (nrows(CM)==3) { if (r<=2) { print(\"  A_COEF r=\"+string(r)+\" : \"+string(CM[3,1])); } else { print(\"  A_COEF r=\"+string(r)+\" lead: \"+string(lead(CM[3,1]))+\" ... nterms=\"+string(size(CM[3,1]))); } }",
                  "}",
         "// (C) resultants with b4 free",
         "ideal RS; int nr=0;",
         "for (k=1; k<=2*tt-2; k++) {",
         "  poly rk=resultant(TT[2*tt-1],TT[k],b3);",
         "  nr++; RS[nr]=rk;",
         "  print(\"RES band=\"+string(k)+\" wdeg=\"+string(deg(rk))+\" expected=\"+string(8*tt+2-2*k)+\" homog=\"+string(homog(rk))+\" size=\"+string(size(rk)));",
         "  kill rk;",
         "}",
         "// RS[k] = Res(T_(2t-1), T_k), k=1..2t-2",
         "ideal RStop; ideal RSlow; int m1=0; int m2=0;",
         "for (k=tt; k<=2*tt-2; k++) { m1++; RStop[m1]=RS[k]; }",
         "for (k=1; k<=tt-1; k++) { m2++; RSlow[m2]=RS[k]; }",
         "// (D) b4=1",
         "ideal RStop1=subst(RStop,b4,1); ideal RSlow1=subst(RSlow,b4,1);",
         "ideal TT1=subst(TT,b4,1);",
         "// (E) b4=0 top-weight parts",
         "ideal RStop0=subst(RStop,b4,0); ideal RSlow0=subst(RSlow,b4,0);",
         "ideal TT0=subst(TT,b4,0);",
         *hdrQ,
         "ideal Ktop=imap(W,RStop1); ideal Klow=imap(W,RSlow1);",
         "ideal Ktop0=imap(W,RStop0); ideal Klow0=imap(W,RSlow0);",
         "option(redSB);",
         "int tm=timer;",
         "ideal Gt=std(Ktop);",
         "print(\"D1 RES_TOP_B4_1 unit=\"+string(reduce(1,Gt)==0)+\" dim=\"+string(dim(Gt))+\" size=\"+string(size(Gt))+\" time=\"+string(timer-tm));",
        ]
    if do_lower:
        L += ["tm=timer; ideal Ga=std(Ktop+Klow);",
              "print(\"D2 RES_ALL_B4_1 unit=\"+string(reduce(1,Ga)==0)+\" dim=\"+string(dim(Ga))+\" size=\"+string(size(Ga))+\" time=\"+string(timer-tm));"]
    L += ["tm=timer; ideal Gt0=std(Ktop0);",
          "print(\"E1 RES_TOP_B4_0 dim=\"+string(dim(Gt0))+\" size=\"+string(size(Gt0))+\" lead=\"+string(lead(Gt0))+\" time=\"+string(timer-tm));",
          "tm=timer; ideal Ga0=std(Ktop0+Klow0);",
          "print(\"E2 RES_ALL_B4_0 dim=\"+string(dim(Ga0))+\" size=\"+string(size(Ga0))+\" time=\"+string(timer-tm));",
          *hdrB,
          "ideal J1top=imap(W,TT1); ideal J0=imap(W,TT0);",
          "ideal Jtop=0; ideal Jtop0=0; mm=0;",
          "for (k=tt; k<=2*tt-1; k++) { mm++; Jtop[mm]=J1top[k]; Jtop0[mm]=J0[k]; }",
          "option(redSB);",
          "tm=timer; ideal G0t=std(Jtop0);",
          "print(\"E3 TOPTAIL_B4_0_CONE dim=\"+string(dim(G0t))+\" size=\"+string(size(G0t))+\" lead=\"+string(lead(G0t))+\" time=\"+string(timer-tm));",
          "tm=timer; ideal G0a=std(J0);",
          "print(\"E4 ALLROWS_B4_0_CONE dim=\"+string(dim(G0a))+\" size=\"+string(size(G0a))+\" time=\"+string(timer-tm));",
          ]
    if do_full:
        L += ["setring W; option(redSB); tm=timer; ideal GW=std(TT);",
              "print(\"F1 CONE dim=\"+string(dim(GW))+\" size=\"+string(size(GW))+\" time=\"+string(timer-tm));",
              "NN=0; for (k=1; k<=8*tt+4; k++) { if (reduce(b4^k,GW)==0) { NN=k; break; } }",
              "print(\"F2 B4_POWER_IN_I N=\"+string(NN));",
              "NN=0; for (k=1; k<=4*tt+2; k++) { if (reduce(b3^k,GW)==0) { NN=k; break; } }",
              "print(\"F3 B3_POWER_IN_I N=\"+string(NN));",
              "setring Wb;",
              "tm=timer; ideal Gtt=std(Jtop);",
              "print(\"D3 TOPTAIL_B4_1 unit=\"+string(reduce(1,Gtt)==0)+\" dim=\"+string(dim(Gtt))+\" size=\"+string(size(Gtt))+\" time=\"+string(timer-tm));",
              "tm=timer; ideal Gj=std(J1top);",
              "print(\"D4 FULLCHART_B4_1 unit=\"+string(reduce(1,Gj)==0)+\" dim=\"+string(dim(Gj))+\" size=\"+string(size(Gj))+\" time=\"+string(timer-tm));"]
    L += ["print(\"TOPTAIL_DONE\");", "quit;"]
    return "\n".join(L) + "\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("t", type=int)
    ap.add_argument("--mode", default="exact", choices=("exact","split-exact","mod"))
    ap.add_argument("--prime", type=int)
    ap.add_argument("--branch", type=int, choices=(0,1))
    ap.add_argument("--full", action="store_true", help="also run the b4=1 top-tail and full-chart std")
    ap.add_argument("--lower", action="store_true", help="also std the lower-row resultants on b4=1")
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--run", action="store_true")
    a = ap.parse_args()
    src, meta = emit(a.t, a.mode, a.prime, a.branch, "none", "std", None, False, None)
    src = src.replace('print("DRIVER_DONE");\nquit;\n', "")
    src += analysis(a.t, a.mode, a.prime, a.branch, a.full, a.lower)
    suffix = a.mode + (f"_p{a.prime}" if a.prime else "") + (f"_b{a.branch}" if a.branch is not None else "")
    stem = f"toptail_t{a.t}_{suffix}"
    (HERE/f"{stem}.sing").write_text(src)
    meta.update({"lane": "k16toptail-20260903", "stem": stem, "timeout": a.timeout})
    if a.run:
        t0 = time.monotonic()
        try:
            res = subprocess.run(["timeout", "--kill-after=10s", f"{a.timeout}s", "Singular", "-q", str(HERE/f"{stem}.sing")],
                                 capture_output=True, text=True)
            out, err, rc = res.stdout, res.stderr, res.returncode
        except Exception as e:
            out, err, rc = "", repr(e), -1
        el = time.monotonic()-t0
        (HERE/f"{stem}.out").write_text(out); (HERE/f"{stem}.err").write_text(err)
        errmark = ("error occurred" in out) or ("error occurred" in err) or ("div. by 0" in out) or ("div by 0" in out)
        status = "PASS" if (rc==0 and "TOPTAIL_DONE" in out and not errmark) else ("INCONCLUSIVE_TIMEOUT" if rc==124 else "FAIL")
        meta.update({"status": status, "returncode": rc, "elapsed_seconds": el, "error_marker": errmark})
    (HERE/f"{stem}.json").write_text(json.dumps(meta, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"stem": stem, "status": meta.get("status","EMITTED"), "elapsed": meta.get("elapsed_seconds")}))

if __name__ == "__main__":
    main()
