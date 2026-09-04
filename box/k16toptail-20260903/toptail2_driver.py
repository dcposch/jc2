#!/usr/bin/env python3
"""Two-stage top-tail driver (lane k16toptail-20260903).

Stage A (--stage A): charged recurrence emitter -> exact rows T_(t,k) (b4 free)
  in the weighted ring W = A_t[b4,q_(2,0..t-1,0),b3], wp(1,2,..,t-1,t+1);
  prints homogeneity, b3-structure of the top tail, the b3^2 coefficients for
  r<=2 in full; computes Res_b3(T_(2t-1),T_k) for top-tail k by the explicit
  quadratic-resultant formula (a1c2-a2c1)^2-(a1b2-a2b1)(b1c2-b2c1) and for the
  lower rows by Singular's resultant(); checks weight 8t+2-2k; writes
  Singular-parsable files rows_t{t}.sing, restop_t{t}.sing, reslow_t{t}.sing.
Stage B (--stage B --test NAME): one std test per process under `timeout`:
  D1 top-tail resultants, b4=1, unit?        E1 same at b4=0: dim in q-ring
  D2 all resultants, b4=1, unit?             E2 same at b4=0
  E3 top-tail rows at b4=0: cone dim          E4 all rows at b4=0: cone dim
  F1 full homogeneous cone: dim, b4^N and b3^N membership
  D3 top-tail rows at b4=1: unit?             D4 all rows at b4=1: unit?
"""
from __future__ import annotations
import argparse, json, pathlib, subprocess, time, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from singular_terminal_driver import emit, ring_header
HERE = pathlib.Path(__file__).resolve().parent

def headers(t, mode, prime, branch):
    resid = ["b4"] + [f"q{j}_0" for j in range(2, t)] + ["b3"]
    wts = [1] + list(range(2, t)) + [t+1]
    qv = [f"q{j}_0" for j in range(2, t)]
    hW, _ = ring_header(t, mode, prime, branch, resid)
    hW = [l.replace("ring R=", "ring W=", 1).replace(",dp;", f",wp({','.join(map(str,wts))});") for l in hW]
    hQ, _ = ring_header(t, mode, prime, branch, qv if qv else ["dummy"])
    hQ = [l.replace("ring R=", "ring Wq=", 1) for l in hQ]
    hB, _ = ring_header(t, mode, prime, branch, qv + ["b3"])
    hB = [l.replace("ring R=", "ring Wb=", 1) for l in hB]
    return hW, hQ, hB

def stageA(t, mode, prime, branch, tag):
    hW, _, _ = headers(t, mode, prime, branch)
    L = ["// ---- k16toptail stage A ----",
         "ideal TTR=" + ",".join(f"T{k}" for k in range(1, 2*t)) + ";", "ideal T0R=T0;",
         *hW, "ideal TT=imap(R,TTR); ideal T0=imap(R,T0R);",
         f"int tt={t}; int k; int r; int ii; int tm; string s1; string s2;",
         "for (k=1; k<=2*tt-1; k++) { s1=string(deg(TT[k])); s2=string(homog(TT[k]));",
         "  print(\"ROW band=\"+string(k)+\" wdeg=\"+s1+\" homog=\"+s2+\" size=\"+string(size(TT[k]))+\" vars=\"+string(variables(TT[k]))); }",
         "poly tau=T0[1]-jet(T0[1],0); print(\"TAU wdeg=\"+string(deg(tau))+\" homog=\"+string(homog(tau))+\" T0const=\"+string(jet(T0[1],0)));",
         "matrix CM; list AC; list BC; list CC;",
         "for (k=tt; k<=2*tt-1; k++) { r=2*tt-1-k; CM=coeffs(TT[k],b3);",
         "  print(\"TOP band=\"+string(k)+\" r=\"+string(r)+\" deg_b3=\"+string(nrows(CM)-1));",
         "  for (ii=1; ii<=nrows(CM); ii++) {",
         "    print(\"  COEF b3^\"+string(ii-1)+\" wdeg=\"+string(deg(CM[ii,1]))+\" homog=\"+string(homog(CM[ii,1]))+\" size=\"+string(size(CM[ii,1]))+\" vars=\"+string(variables(CM[ii,1]))); }",
         "  if (nrows(CM)==3) { AC[k]=CM[3,1]; BC[k]=CM[2,1]; CC[k]=CM[1,1];",
         "    if (r<=2) { print(\"  A_COEF r=\"+string(r)+\" : \"+string(CM[3,1])); } else { print(\"  A_COEF r=\"+string(r)+\" lead: \"+string(lead(CM[3,1]))+\" nterms=\"+string(size(CM[3,1]))); } }",
         "  else { AC[k]=poly(0); BC[k]=CM[2,1]; CC[k]=CM[1,1]; }",
         "}",
         "// resultants: top tail by the explicit formula, lower rows by resultant()",
         "poly a1=AC[2*tt-1]; poly b1=BC[2*tt-1]; poly c1=CC[2*tt-1];",
         "ideal RStop; ideal RSlow; int m1=0; int m2=0; poly rk;",
         "for (k=tt; k<=2*tt-2; k++) { tm=timer;",
         "  rk=(a1*CC[k]-AC[k]*c1)^2-(a1*BC[k]-AC[k]*b1)*(b1*CC[k]-BC[k]*c1);",
         "  m1++; RStop[m1]=rk;",
         "  print(\"RES band=\"+string(k)+\" wdeg=\"+string(deg(rk))+\" expected=\"+string(8*tt+2-2*k)+\" homog=\"+string(homog(rk))+\" size=\"+string(size(rk))+\" time=\"+string(timer-tm)); }",
         "for (k=1; k<=tt-1; k++) { tm=timer; rk=resultant(TT[2*tt-1],TT[k],b3); m2++; RSlow[m2]=rk;",
         "  print(\"RESLOW band=\"+string(k)+\" wdeg=\"+string(deg(rk))+\" expected=\"+string(8*tt+2-2*k)+\" homog=\"+string(homog(rk))+\" size=\"+string(size(rk))+\" time=\"+string(timer-tm)); }",
         f"write(\":w {HERE}/rows_{tag}.sing\", \"ideal TT=\"+string(TT)+\";\");",
         f"write(\":w {HERE}/restop_{tag}.sing\", \"ideal RStop=\"+string(RStop)+\";\");",
         f"write(\":w {HERE}/reslow_{tag}.sing\", \"ideal RSlow=\"+string(RSlow)+\";\");",
         "print(\"STAGEA_DONE\");", "quit;"]
    return "\n".join(L) + "\n"

def yvar_headers(t):
    import sympy as sp
    from singular_terminal_driver import h_polynomial
    H = str(h_polynomial(t, sp.Symbol("yy"))).replace("**","^")
    resid = ["b4"] + [f"q{j}_0" for j in range(2, t)] + ["b3"]
    wts = [1] + list(range(2, t)) + [t+1]
    qv = [f"q{j}_0" for j in range(2, t)]
    hW = [f"ring W=0,({','.join(resid)},yy),(wp({','.join(map(str,wts))}),dp(1));", f"poly HT={H};"]
    hQ = [f"ring Wq=0,({','.join(qv if qv else ['dummy'])},yy),dp;", f"poly HT={H};"]
    hB = [f"ring Wb=0,({','.join(qv+['b3'])},yy),dp;", f"poly HT={H};"]
    return hW, hQ, hB

def stageB(t, mode, prime, branch, tag, test, enc="minpoly"):
    hW, hQ, hB = headers(t, mode, prime, branch) if enc == "minpoly" else yvar_headers(t)
    HT = "+HT" if enc == "yvar" else ""
    L = [*hW, f"int tt={t}; int k; int NN; int tm; int mm;", "option(redSB);",
         f"execute(read(\"{HERE}/rows_t{t}_exact.sing\"));",
         f"execute(read(\"{HERE}/restop_t{t}_exact.sing\"));",
         f"execute(read(\"{HERE}/reslow_t{t}_exact.sing\"));",
         "ideal RStop1=subst(RStop,b4,1); ideal RSlow1=subst(RSlow,b4,1); ideal TT1=subst(TT,b4,1);",
         "ideal RStop0=subst(RStop,b4,0); ideal RSlow0=subst(RSlow,b4,0); ideal TT0=subst(TT,b4,0);"]
    if test in ("D1","D2","E1","E2"):
        L += [*hQ, "ideal Ktop=imap(W,RStop1); ideal Klow=imap(W,RSlow1); ideal Ktop0=imap(W,RStop0); ideal Klow0=imap(W,RSlow0); option(redSB);"]
        src = {"D1":"Ktop","D2":"Ktop+Klow","E1":"Ktop0","E2":"Ktop0+Klow0"}[test]
        L += [f"tm=timer; ideal G=std({src}{HT});",
              f"print(\"{test} unit=\"+string(reduce(1,G)==0)+\" dim=\"+string(dim(G))+\" size=\"+string(size(G))+\" time=\"+string(timer-tm));",
              "if (size(G)<=12) { print(\"LEAD \"+string(lead(G))); }"]
    elif test in ("E3","E4","D3","D4"):
        L += [*hB, "ideal J1=imap(W,TT1); ideal J0=imap(W,TT0); ideal Jtop=0; ideal Jtop0=0; mm=0;",
              "for (k=tt; k<=2*tt-1; k++) { mm++; Jtop[mm]=J1[k]; Jtop0[mm]=J0[k]; }", "option(redSB);"]
        src = {"E3":"Jtop0","E4":"J0","D3":"Jtop","D4":"J1"}[test]
        L += [f"tm=timer; ideal G=std({src}{HT});",
              f"print(\"{test} unit=\"+string(reduce(1,G)==0)+\" dim=\"+string(dim(G))+\" size=\"+string(size(G))+\" time=\"+string(timer-tm));",
              "if (size(G)<=12) { print(\"LEAD \"+string(lead(G))); }"]
    elif test == "F1":
        L += [f"tm=timer; ideal GW=std(TT{HT});",
              "print(\"F1 CONE dim=\"+string(dim(GW))+\" size=\"+string(size(GW))+\" time=\"+string(timer-tm));",
              "NN=0; for (k=1; k<=8*tt+4; k++) { if (reduce(b4^k,GW)==0) { NN=k; break; } } print(\"F2 B4_POWER_IN_I N=\"+string(NN));",
              "NN=0; for (k=1; k<=8*tt+4; k++) { if (reduce(b3^k,GW)==0) { NN=k; break; } } print(\"F3 B3_POWER_IN_I N=\"+string(NN));"]
    elif test == "F4":
        L += ["ideal Jt=0; mm=0; for (k=tt; k<=2*tt-1; k++) { mm++; Jt[mm]=TT[k]; }",
              f"tm=timer; ideal GW=std(Jt{HT});",
              "print(\"F4 TOPCONE dim=\"+string(dim(GW))+\" size=\"+string(size(GW))+\" time=\"+string(timer-tm));",
              "int vv; string pw=\"\";",
              "for (vv=1; vv<=nvars(basering); vv++) { NN=0; for (k=1; k<=8*tt+4; k++) { if (reduce(var(vv)^k,GW)==0) { NN=k; break; } } pw=pw+string(var(vv))+\"^\"+string(NN)+\" \"; }",
              "print(\"F5 PURE_POWERS_IN_TOPCONE \"+pw);"]
    L += [f"print(\"STAGEB_DONE {test}\");", "quit;"]
    return "\n".join(L) + "\n"

def run(path, timeout):
    t0 = time.monotonic()
    res = subprocess.run(["timeout", "--kill-after=10s", f"{timeout}s", "Singular", "-q", str(path)], capture_output=True, text=True)
    el = time.monotonic()-t0
    out, err = res.stdout, res.stderr
    errmark = ("error occurred" in out) or ("error occurred" in err) or ("div. by 0" in out)
    return res.returncode, el, out, err, errmark

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("t", type=int); ap.add_argument("--stage", choices=("A","B"), required=True)
    ap.add_argument("--test", default="D1"); ap.add_argument("--mode", default="exact", choices=("exact","split-exact","mod"))
    ap.add_argument("--prime", type=int); ap.add_argument("--branch", type=int, choices=(0,1))
    ap.add_argument("--timeout", type=int, default=600); ap.add_argument("--enc", default="minpoly", choices=("minpoly","yvar"))
    a = ap.parse_args()
    tag = f"t{a.t}_{a.mode}" + (f"_p{a.prime}" if a.prime else "") + (f"_b{a.branch}" if a.branch is not None else "")
    if a.stage == "A":
        src, meta = emit(a.t, a.mode, a.prime, a.branch, "none", "std", None, False, None)
        src = src.replace('print("DRIVER_DONE");\nquit;\n', "") + stageA(a.t, a.mode, a.prime, a.branch, tag)
        stem = f"stageA_{tag}"; done = "STAGEA_DONE"
    else:
        src = stageB(a.t, a.mode, a.prime, a.branch, tag, a.test, a.enc); meta = {"t": a.t, "mode": a.mode, "branch": a.branch, "prime": a.prime, "enc": a.enc}
        stem = f"stageB_{a.test}_{tag}" + ("_yvar" if a.enc == "yvar" else ""); done = f"STAGEB_DONE {a.test}"
    (HERE/f"{stem}.sing").write_text(src)
    rc, el, out, err, errmark = run(HERE/f"{stem}.sing", a.timeout)
    (HERE/f"{stem}.out").write_text(out); (HERE/f"{stem}.err").write_text(err)
    status = "PASS" if (rc == 0 and done in out and not errmark) else ("INCONCLUSIVE_TIMEOUT" if rc == 124 else "FAIL")
    meta.update({"lane": "k16toptail-20260903", "stem": stem, "status": status, "returncode": rc, "elapsed_seconds": el, "timeout": a.timeout, "error_marker": errmark})
    (HERE/f"{stem}.json").write_text(json.dumps(meta, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"stem": stem, "status": status, "elapsed": round(el,2)}))

if __name__ == "__main__":
    main()
