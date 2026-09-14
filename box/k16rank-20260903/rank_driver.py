#!/usr/bin/env python3
"""Criterion RANK driver (lane k16-rank-criterion-fable5-20260903).

Reads the exact tail rows dumped by the charged singular_terminal_driver.py
(TROW band=k lines of terminal_t{t}_exact_none.out, or the split-exact t=2
files), and emits/runs a Singular job that

  STRUCT : a_r,b_r,c_r = [b3^2],[b3],[b3^0] of T_{t,2t-1-r};  B_r=a0 b_r-a_r b0,
           C_r=a0 c_r-a_r c0, G_r=B_r b3+C_r (checked == a0 T_{2t-1-r}-a_r T_{2t-1}),
           W_r=a0 C_r^2-b0 B_r C_r+c0 B_r^2 (checked against the ELIMINANT certificate);
           weights, term counts, wp-leaders, axis (pure-power) coefficients.
  PARTI  : dim/vdim of (B_1..B_{t-1},C_1..C_{t-1}) in P_t; of (B) alone; of (C) alone.
  CURVE  : I2 = 2x2 minors of N=(C_r,B_r); dim, mult; I2+(W): dim; Fitting ideal
           F = I2+(W)+(X_rs): dim, vdim;  (W) alone: dim, vdim.
  JTAIL  : dim/vdim of J_t^tail in S_t (control; expensive for t>=5 exact).
  SUBSETS: every (t-1)-subset of {B_r,C_r}: dim 0 or not (modular only).
  PRIMDEC: primary decomposition of I2 (modular), with W-vanishing per component.

Ring map (declared): S_t = K[b4,q2_0,..,q{t-1}_0,b3], wp(1,2,..,t-1,t+1);
P_t = K[b4,q2_0,..,q{t-1}_0], wp(1,..,t-1); K = Q(yy)/(H_t) (exact, minpoly),
Q with yy a rational root (split-exact, t=2), or GF(p) with yy a root of H_t mod p.
"""
import argparse, pathlib, re, subprocess, sys, time, itertools, json
import sympy as sp

HERE = pathlib.Path(__file__).resolve().parent

def Hpoly(t):
    q = 2*t+1
    return f"{12*q*q}*yy^2-{12*q*(t+1)}*yy+{(t+1)*(3*t+2)}"

def mod_roots(t, p):
    q = 2*t+1
    return sorted(r for r in range(p) if (12*q*q*r*r - 12*q*(t+1)*r + (t+1)*(3*t+2)) % p == 0)

def read_rows(t, mode, branch):
    if mode == 'split-exact':
        path = HERE / f"terminal_t{t}_split-exact_branch{branch}_none.out"
    else:
        path = HERE / f"terminal_t{t}_exact_none.out"
    txt = path.read_text()
    assert "RECURRENCE_PASS" in txt and "DRIVER_DONE" in txt, f"rows file incomplete: {path}"
    assert "error" not in txt and "div. by 0" not in txt, f"error marker in {path}"
    rows = {}
    lines = txt.splitlines()
    for i, ln in enumerate(lines):
        m = re.match(r"TROW band=(\d+)", ln)
        if m:
            rows[int(m.group(1))] = lines[i+1].strip()
    assert len(rows) == 2*t, (len(rows), 2*t)
    return rows

def emit(t, rows, mode, prime, branch, tests):
    vars_P = ["b4"] + [f"q{j}_0" for j in range(2, t)]
    wts_P = [1] + list(range(2, t))
    vars_S = vars_P + ["b3"]
    wts_S = wts_P + [t+1]
    L = []
    def ring(name, vs, ws):
        if mode == 'exact':
            L.append(f"ring {name}=(0,yy),({','.join(vs)}),wp({','.join(map(str,ws))});")
            L.append(f"minpoly={Hpoly(t)};")
        elif mode == 'split-exact':
            val = {0: "1/5", 1: "2/5"}[branch]  # t=2 only
            L.append(f"ring {name}=0,({','.join(vs)}),wp({','.join(map(str,ws))});")
            L.append(f"number yy={val};")
        else:
            root = mod_roots(t, prime)[branch]
            L.append(f"ring {name}=({prime}),({','.join(vs)}),wp({','.join(map(str,ws))});")
            L.append(f"number yy={root};")
    L.append(f'print("RANKDRIVER t={t} mode={mode} prime={prime} branch={branch}");')
    L.append(f'print("RING S_t: vars {",".join(vars_S)} weights {",".join(map(str,wts_S))}");')
    ring("S", vars_S, wts_S)
    L.append("option(redSB);")
    for r in range(t):
        k = 2*t-1-r
        L.append(f"poly T{k}={rows[k]};")
    # structure
    L.append("int r; intvec b3wt=" + ",".join(["0"]*(t-1)+["1"]) + ";")
    for r in range(t):
        k = 2*t-1-r
        L += [f"poly cc{r}=subst(T{k},b3,0);",
              f"poly bb{r}=subst(diff(T{k},b3),b3,0);",
              f"poly aa{r}=subst(diff(diff(T{k},b3),b3),b3,0)/2;",
              f"if (T{k}-(aa{r}*b3^2+bb{r}*b3+cc{r})!=0) {{ print(\"FAIL b3-split r={r}\"); }}",
              f"print(\"STRUCT r={r} k={k}: wt(T)=\"+string(deg(T{k}))+\" homog=\"+string(homog(T{k}))+\" deg_b3=\"+string(deg(T{k},b3wt)));",
              ]
        L += [f"print(\"  a{r}: wt=\"+string(deg(aa{r}))+\" size=\"+string(size(aa{r}))+\" homog=\"+string(homog(aa{r})));",
              f"print(\"  b{r}: wt=\"+string(deg(bb{r}))+\" size=\"+string(size(bb{r}))+\" homog=\"+string(homog(bb{r})));",
              f"print(\"  c{r}: wt=\"+string(deg(cc{r}))+\" size=\"+string(size(cc{r}))+\" homog=\"+string(homog(cc{r})));"]
    L.append('print("A0VALUE: "+string(aa0));')
    L.append('if (aa0==0) { print("A0_ZERO: split unavailable (a0=0)"); }')
    for r in range(1, t):
        k = 2*t-1-r
        L += [f"poly B{r}=aa0*bb{r}-aa{r}*bb0;", f"poly C{r}=aa0*cc{r}-aa{r}*cc0;", f"poly G{r}=B{r}*b3+C{r};",
              f"if (G{r}-(aa0*T{k}-aa{r}*T{2*t-1})!=0) {{ print(\"FAIL G-identity r={r}\"); }}",
              f"poly W{r}=aa0*C{r}^2-bb0*B{r}*C{r}+cc0*B{r}^2;",
              f"if (W{r}-(B{r}^2*T{2*t-1}-G{r}*(aa0*G{r}-2*aa0*C{r}+bb0*B{r}))!=0) {{ print(\"FAIL eliminant certificate r={r}\"); }}",
              f"print(\"SPLIT r={r}: B{r} wt=\"+string(deg(B{r}))+\" size=\"+string(size(B{r}))+\" homog=\"+string(homog(B{r}))+\" lead=\"+string(leadmonom(B{r}))+\" | C{r} wt=\"+string(deg(C{r}))+\" size=\"+string(size(C{r}))+\" homog=\"+string(homog(C{r}))+\" lead=\"+string(leadmonom(C{r}))+\" | W{r} wt=\"+string(deg(W{r}))+\" size=\"+string(size(W{r}))+\" homog=\"+string(homog(W{r})));"]
    # axis coefficients: restrict each of B_r, C_r, b_r, c_r to each coordinate axis of P_t
    if 'struct' in tests:
        for r in range(0, t):
            for nm in (f"bb{r}", f"cc{r}") + ((f"B{r}", f"C{r}") if r >= 1 else ()):
                for v in vars_P:
                    others = [w for w in vars_S if w != v]
                    sub = nm
                    for w in others:
                        sub = f"subst({sub},{w},0)"
                    L.append(f"print(\"AXIS {nm} on {v}-axis: \"+string({sub}));")
        # also: number of monomials of the allowed weight (full support test) = size
    # ---- P_t ----
    L.append(f'print("RING P_t: vars {",".join(vars_P)} weights {",".join(map(str,wts_P))}");')
    ring("P", vars_P, wts_P)
    L.append("option(redSB);")
    for r in range(1, t):
        L += [f"poly B{r}=imap(S,B{r});", f"poly C{r}=imap(S,C{r});", f"poly W{r}=imap(S,W{r});"]
    L += ["poly a0=imap(S,aa0); poly b0=imap(S,bb0); poly c0=imap(S,cc0);"]
    Bl = ",".join(f"B{r}" for r in range(1, t)); Cl = ",".join(f"C{r}" for r in range(1, t)); Wl = ",".join(f"W{r}" for r in range(1, t))
    L += [f"ideal Bs={Bl};", f"ideal Cs={Cl};", f"ideal Ws={Wl};", "ideal BC=Bs+Cs;"]
    if 'parti' in tests:
        L += ['int tm=timer;', "ideal gBC=std(BC);",
              'print("PARTI (B,C): dim="+string(dim(gBC))+" vdim="+string(vdim(gBC))+" gbsize="+string(size(gBC))+" time="+string(timer-tm));',
              "ideal gB=std(Bs);", 'print("PARTI (B) alone: dim="+string(dim(gB))+" vdim="+string(vdim(gB)));',
              "ideal gC=std(Cs);", 'print("PARTI (C) alone: dim="+string(dim(gC))+" vdim="+string(vdim(gC)));',
              ]
        # pure powers in lead(gBC)
        L += ["int iv; poly lm; ideal LBC=lead(gBC);",
              "for (iv=1; iv<=nvars(P); iv++) { int e; int found=0; for (e=1; e<=200; e++) { if (reduce(var(iv)^e,gBC)==0) { found=e; break; } } print(\"PARTI purepower \"+string(var(iv))+\"^\"+string(found)+\" in (B,C)\"); kill e; kill found; }"]
    if 'curve' in tests:
        rowsN = ",".join(f"C{r},B{r}" for r in range(1, t))
        L += [f"matrix N[{t-1}][2]={rowsN};", "ideal I2=minor(N,2);",
              'int tm2=timer;', "ideal gI2=std(I2);",
              'print("CURVE I2=minors(N,2): ngens="+string(size(I2))+" dim="+string(dim(gI2))+" mult="+string(mult(gI2))+" gbsize="+string(size(gI2))+" time="+string(timer-tm2));',
              "ideal gI2W=std(I2+Ws);",
              'print("CURVE I2+(W): dim="+string(dim(gI2W))+" vdim="+string(vdim(gI2W)));',
              ]
        # Fitting ideal: X_rs = a0 C_r C_s - b0 B_s C_r + c0 B_r B_s
        Xl = []
        for r in range(1, t):
            for s in range(r+1, t):
                L.append(f"poly X{r}_{s}=a0*C{r}*C{s}-b0*B{s}*C{r}+c0*B{r}*B{s};")
                Xl.append(f"X{r}_{s}")
        L += [f"ideal Xs={','.join(Xl) if Xl else '0'};", "ideal Fitt=I2+Ws+Xs;", "ideal gF=std(Fitt);",
              'print("CURVE Fitting F=I2+(W)+(X): dim="+string(dim(gF))+" vdim="+string(vdim(gF))+" gbsize="+string(size(gF)));',
              "ideal gW=std(Ws);",
              'print("CURVE (W) alone: dim="+string(dim(gW))+" vdim="+string(vdim(gW)));']
        # Hilbert series numerator of P/I2 (for the Eagon-Northcott comparison)
        L += ["intvec wv=" + ",".join(map(str, wts_P)) + ";",
              'print("CURVE hilb(P/I2) weighted numerator:"); hilb(gI2,1,wv);',
              'print("CURVE hilb(P/(B,C)) weighted numerator:"); if (defined(gBC)) { hilb(gBC,1,wv); }']
    if 'primdec' in tests:
        L += ['LIB "primdec.lib";', "list pd=primdecGTZ(I2);",
              'print("PRIMDEC I2: ncomponents="+string(size(pd)));',
              "int ic; ideal Pc; ideal Qc; for (ic=1; ic<=size(pd); ic++) { Pc=std(pd[ic][2]); Qc=std(pd[ic][1]); "
              "print(\"PRIMDEC comp \"+string(ic)+\": prime dim=\"+string(dim(Pc))+\" mult(primary)=\"+string(mult(Qc))+\" mult(prime)=\"+string(mult(Pc))+\" ngens(prime)=\"+string(size(pd[ic][2]))+\" W-vanish: dim(P+W)=\"+string(dim(std(Pc+Ws)))+\" T-lift: dim(P+Fitt)=\"+string(dim(std(Pc+Fitt)))); "
              "print(\"PRIMDEC comp \"+string(ic)+\" prime = \"+string(pd[ic][2])); }"]
    if 'subsets' in tests:
        names = [f"B{r}" for r in range(1, t)] + [f"C{r}" for r in range(1, t)]
        L.append('print("SUBSETS: (t-1)-subsets of {B_r,C_r} that are sops (dim 0) in P_t");')
        for comb in itertools.combinations(names, t-1):
            L.append(f"if (dim(std(ideal({','.join(comb)})))==0) {{ print(\"SUBSET SOP {' '.join(comb)}\"); }} else {{ print(\"SUBSET notsop {' '.join(comb)}\"); }}")
    if 'jtail' in tests:
        L += ["setring S;", f"ideal Jt={','.join(f'T{k}' for k in range(t, 2*t))};", "int tm3=timer; ideal gJ=std(Jt);",
              'print("JTAIL: dim="+string(dim(gJ))+" vdim="+string(vdim(gJ))+" time="+string(timer-tm3));']
    if 'gcurve' in tests:
        # the CI curve V(G_1..G_{t-1}) in S_t: dimension, primary decomposition, b3-axis multiplicity,
        # T_{2t-1} nonvanishing on each component; local multiplicity of the axis via a weighted local order.
        L += ["setring S;", f"ideal Gs={','.join(f'G{r}' for r in range(1, t))};", "ideal gGs=std(Gs);",
              'print("GCURVE (G_1..G_{t-1}) in S_t: dim="+string(dim(gGs))+" mult="+string(mult(gGs)));',
              'LIB "primdec.lib"; list pg=primdecGTZ(Gs);',
              'print("GCURVE ncomponents="+string(size(pg)));',
              f"ideal axis={','.join(vars_P)};",
              "int ig; ideal Pg; ideal Qg; for (ig=1; ig<=size(pg); ig++) { Pg=std(pg[ig][2]); Qg=std(pg[ig][1]); "
              f"print(\"GCURVE comp \"+string(ig)+\": dim(prime)=\"+string(dim(Pg))+\" mult(primary)=\"+string(mult(Qg))+\" mult(prime)=\"+string(mult(Pg))+\" is_b3axis=\"+string(size(reduce(axis,Pg))==0 && size(reduce(Pg,std(axis)))==0)+\" dim(prime+T_top)=\"+string(dim(std(Pg+ideal(T{2*t-1}))))+\" b3-value: NF(b3,prime)=\"+string(reduce(b3,Pg))); }}",
              ]
        L.append(f'print("GCURVE local multiplicity of the b3-axis point (chart b3=1, weighted local order ws):");')
        if mode == 'mod':
            root = mod_roots(t, prime)[branch]
            L.append(f"ring Ploc=({prime}),({','.join(vars_P)}),ws({','.join(map(str,wts_P))}); number yy={root};")
        else:
            L.append(f"ring Ploc=(0,yy),({','.join(vars_P)}),ws({','.join(map(str,wts_P))}); minpoly={Hpoly(t)};")
        L += ["ideal Gloc;", "setring S;", "ideal Gb3one=" + ",".join(f"subst(G{r},b3,1)" for r in range(1, t)) + ";",
              "setring Ploc;", "Gloc=imap(S,Gb3one);", "ideal gloc=std(Gloc);",
              'print("GCURVE axis local multiplicity vdim(ws)="+string(vdim(gloc))+"  (predicted binom(2t,t-1) if (B) is an sop)");']
    if 'dump' in tests:
        L.append("setring P;")
        for r in range(1, t):
            L += [f'print("DUMP B{r} = "+string(B{r}));', f'print("DUMP C{r} = "+string(C{r}));']
        L += ['print("DUMP a0 = "+string(a0));', 'print("DUMP b0 = "+string(b0));', 'print("DUMP c0 = "+string(c0));']
    L.append('print("RANKDRIVER_DONE");')
    L.append("quit;")
    return "\n".join(L) + "\n"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("t", type=int)
    ap.add_argument("--mode", choices=("exact", "split-exact", "mod"), default="exact")
    ap.add_argument("--prime", type=int)
    ap.add_argument("--branch", type=int, default=0)
    ap.add_argument("--tests", default="struct,parti,curve")
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--tag", default="")
    ap.add_argument("--run", action="store_true")
    a = ap.parse_args()
    rows = read_rows(a.t, "split-exact" if a.mode == "split-exact" else "exact", a.branch)
    tests = set(a.tests.split(","))
    src = emit(a.t, rows, a.mode, a.prime, a.branch, tests)
    stem = f"rank_t{a.t}_{a.mode}" + (f"_p{a.prime}" if a.prime else "") + (f"_b{a.branch}" if a.mode != "exact" else "") + (f"_{a.tag}" if a.tag else "")
    (HERE / f"{stem}.sing").write_text(src)
    meta = dict(t=a.t, mode=a.mode, prime=a.prime, branch=a.branch, tests=sorted(tests), timeout=a.timeout,
                ring_S=f"K[b4,q2_0..q{a.t-1}_0,b3] wp(1..{a.t-1},{a.t+1})", ring_P=f"K[b4,q2_0..q{a.t-1}_0] wp(1..{a.t-1})",
                K=("Q(yy)/(H_t)" if a.mode == "exact" else ("Q, yy=1/5|2/5" if a.mode == "split-exact" else f"GF({a.prime}), yy=root#{a.branch}")))
    if a.run:
        t0 = time.monotonic()
        outp = HERE / f"{stem}.out"; errp = HERE / f"{stem}.err"
        with open(outp, "w") as fo, open(errp, "w") as fe:
            try:
                res = subprocess.run(["Singular", "-q", str(HERE / f"{stem}.sing")], stdout=fo, stderr=fe, text=True, timeout=a.timeout)
                status = "RAN"
            except subprocess.TimeoutExpired:
                status = "INCONCLUSIVE_TIMEOUT"
        out = outp.read_text()
        if status == "RAN":
            status = "PASS" if "RANKDRIVER_DONE" in out and "FAIL" not in out and "error" not in out and "div. by 0" not in out else "FAIL"
        meta.update(status=status, elapsed=time.monotonic()-t0)
    (HERE / f"{stem}.json").write_text(json.dumps(meta, indent=1))
    print(json.dumps({"stem": stem, "status": meta.get("status", "EMITTED"), "elapsed": meta.get("elapsed")}))

if __name__ == "__main__":
    main()
