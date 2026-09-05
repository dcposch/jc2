#!/usr/bin/env python3
"""k16galois emitter (lane k16-gamma-galois-fable5-20260905).

Builds Singular jobs on the top-tail rows T_{t,2t-1-r}, r=0..t-1, read from the frozen
rank-lane row dumps box/k16rank-20260903/terminal_t{t}_exact_none.out (TROW band=k lines;
these are the charged singular_terminal_driver.py --dump-rows outputs, unchanged).

Rings (declared):  S = K[b4,q2_0,..,q{t-1}_0,b3], wp(1,2,..,t-1,t+1)
                   P = K[b4,q2_0,..,q{t-1}_0],    wp(1,2,..,t-1)
K = Q(yy)/(H_t) (mode exact, minpoly) or GF(p) with yy = a root of H_t mod p (mode mod, branch 0|1).
Split: T_{t,2t-1-r} = a_r b3^2 + b_r b3 + c_r;  B_r = a0 b_r - a_r b0;  C_r = a0 c_r - a_r c0;
G_r = B_r b3 + C_r (checked == a0 T_{2t-1-r} - a_r T_{2t-1});  W_r = a0 C_r^2 - b0 B_r C_r + c0 B_r^2
(checked against the ELIMINANT certificate);  N = ((C_r,B_r))_r;  I2 = minor(N,2);  Gamma = V(I2).
Jobs: pattern | exactchart | boundary | colon | msolve
"""
import argparse, pathlib, re, sys
ROWS = pathlib.Path('/home/ubuntu/jc2/box/k16rank-20260903')
HERE = pathlib.Path(__file__).resolve().parent

def Hpoly(t):
    q = 2*t+1
    return f"{12*q*q}*yy^2-{12*q*(t+1)}*yy+{(t+1)*(3*t+2)}"

def mod_roots(t, p):
    q = 2*t+1
    return sorted(r for r in range(p) if (12*q*q*r*r - 12*q*(t+1)*r + (t+1)*(3*t+2)) % p == 0)

def read_rows(t):
    path = ROWS / f"terminal_t{t}_exact_none.out"
    txt = path.read_text()
    assert "RECURRENCE_PASS" in txt and "DRIVER_DONE" in txt, path
    assert "error" not in txt and "div. by 0" not in txt, path
    rows = {}
    lines = txt.splitlines()
    for i, ln in enumerate(lines):
        m = re.match(r"TROW band=(\d+)", ln)
        if m:
            rows[int(m.group(1))] = lines[i+1].strip()
    assert len(rows) == 2*t, (len(rows), 2*t)
    return rows

def prefix(t, mode, prime, branch, tag):
    rows = read_rows(t)
    vars_P = ["b4"] + [f"q{j}_0" for j in range(2, t)]
    wts_P = [1] + list(range(2, t))
    vars_S = vars_P + ["b3"]
    wts_S = wts_P + [t+1]
    L = []
    def ring(name, vs, ws):
        if mode == 'exact':
            L.append(f"ring {name}=(0,yy),({','.join(vs)}),wp({','.join(map(str,ws))});")
            L.append(f"minpoly={Hpoly(t)};")
        else:
            roots = mod_roots(t, prime)
            assert len(roots) == 2, (t, prime, roots)
            L.append(f"ring {name}=({prime}),({','.join(vs)}),wp({','.join(map(str,ws))});")
            L.append(f"number yy={roots[branch]};")
    L.append(f'print("K16GALOIS {tag} t={t} mode={mode} prime={prime} branch={branch}");')
    L.append('LIB "linalg.lib";')
    ring("S", vars_S, wts_S)
    L.append("option(redSB);")
    L.append(f'print("RING S: {",".join(vars_S)} wp {",".join(map(str,wts_S))}  H_t={Hpoly(t)}");')
    for r in range(t):
        k = 2*t-1-r
        L.append(f"poly T{k}={rows[k]};")
    L.append("intvec b3wt=" + ",".join(["0"]*(t-1)+["1"]) + ";")
    for r in range(t):
        k = 2*t-1-r
        L += [f"poly cc{r}=subst(T{k},b3,0);",
              f"poly bb{r}=subst(diff(T{k},b3),b3,0);",
              f"poly aa{r}=subst(diff(diff(T{k},b3),b3),b3,0)/2;",
              f"if (T{k}-(aa{r}*b3^2+bb{r}*b3+cc{r})!=0) {{ print(\"FAIL b3-split r={r}\"); }}",
              f"if (homog(T{k})==0 || deg(T{k})!={2*t+2+r}) {{ print(\"FAIL weight r={r}\"); }}"]
    L.append('print("A0VALUE: "+string(aa0));')
    L.append('if (aa0==0) { print("FAIL A0_ZERO"); }')
    for r in range(1, t):
        k = 2*t-1-r
        L += [f"poly B{r}=aa0*bb{r}-aa{r}*bb0;", f"poly C{r}=aa0*cc{r}-aa{r}*cc0;", f"poly G{r}=B{r}*b3+C{r};",
              f"if (G{r}-(aa0*T{k}-aa{r}*T{2*t-1})!=0) {{ print(\"FAIL G-identity r={r}\"); }}",
              f"poly W{r}=aa0*C{r}^2-bb0*B{r}*C{r}+cc0*B{r}^2;",
              f"if (W{r}-(B{r}^2*T{2*t-1}-G{r}*(aa0*G{r}-2*aa0*C{r}+bb0*B{r}))!=0) {{ print(\"FAIL eliminant r={r}\"); }}"]
    L.append(f"ideal Gs={','.join(f'G{r}' for r in range(1,t))};")
    L.append(f"poly Ttop=T{2*t-1};")
    L.append('print("PREFIX_S_OK");')
    # ---- P ----
    ring("P", vars_P, wts_P)
    L.append("option(redSB);")
    for r in range(1, t):
        L += [f"poly B{r}=imap(S,B{r});", f"poly C{r}=imap(S,C{r});", f"poly W{r}=imap(S,W{r});"]
    L += ["poly a0=imap(S,aa0); poly b0=imap(S,bb0); poly c0=imap(S,cc0);"]
    L.append(f"ideal Ws={','.join(f'W{r}' for r in range(1,t))};")
    L.append(f"ideal Bs={','.join(f'B{r}' for r in range(1,t))};")
    rowsN = ",".join(f"C{r},B{r}" for r in range(1, t))
    L += [f"matrix N[{t-1}][2]={rowsN};", "ideal I2=minor(N,2);",
          'print("PREFIX_P_OK ngens(I2)="+string(size(I2)));']
    # evaluation helper and the probe proc
    L += [
        "proc ev(poly f, list pt) { int i; poly g=f; for(i=1;i<=size(pt);i++){ g=subst(g,var(i),pt[i]); } return(g); }",
        "list PT; int PTOK=0;",
        "proc probe(ideal J, int fv, list fixed, string tag)",
        "{",
        "  int tm=timer; ideal gJ=std(J); int vd=vdim(gJ);",
        '  print(tag+" vdim="+string(vd)+" dim="+string(dim(gJ))+" time="+string(timer-tm));',
        "  if (vd<=0) { return(0); }",
        "  tm=timer; ideal U=finduni(gJ); poly m=U[fv]; int w=fv;",
        "  int dm=deg(m) div w; poly gg=gcd(m,diff(m,var(fv)));",
        '  print(tag+" minpoly var="+string(var(fv))+" ordinary_degree="+string(dm)+" squarefree="+string(deg(gg)==0)+" time="+string(timer-tm));',
        "  int i; int j;",
        '  for (i=fv; i<=nvars(basering); i++) { print(tag+" unideg var="+string(var(i))+" ordinary_degree="+string(deg(U[i]) div i)); }',
        '  write(":w "+MFILE+"_"+string(var(fv))+".txt", string(m));',
        "  tm=timer; list FL=factorize(m); string s=\"\"; number v; int have=0;",
        "  for (i=1;i<=size(FL[1]);i++) {",
        "    if (deg(FL[1][i])>0) {",
        '      s=s+" "+string(deg(FL[1][i]) div w)+"^"+string(FL[2][i]);',
        "      if ((deg(FL[1][i]) div w)==1 && have==0) { v=-leadcoef(subst(FL[1][i],var(fv),0))/leadcoef(FL[1][i]); have=1; }",
        "    }",
        "  }",
        '  print(tag+" PATTERN"+s+" factortime="+string(timer-tm));',
        '  if (have==0) { print(tag+" NO_RATIONAL_POINT"); return(0); }',
        "  ideal F=gJ+ideal(var(fv)-v); ideal gF=std(F);",
        '  print(tag+" fibre "+string(var(fv))+"="+string(v)+" vdim="+string(vdim(gF)));',
        '  if (vdim(gF)!=1) { print(tag+" FIBRE_NOT_SIMPLE"); return(0); }',
        "  list pt=fixed; pt[fv]=v; poly rr;",
        '  for (i=fv+1;i<=nvars(basering);i++) { rr=reduce(var(i),gF); if (deg(rr)>0) { print(tag+" NONCONSTANT_COORD"); return(0); } pt[i]=leadcoef(rr); }',
        "  PT=pt; PTOK=1; return(1);",
        "}",
        # evaluation of everything at PT; freecols = intvec of free variable indices
        "proc evalpoint(intvec freecols, string tag)",
        "{",
        '  int i; int j; string ps=""; for(i=1;i<=size(PT);i++){ ps=ps+string(PT[i])+","; } print(tag+" POINT=("+ps+")");',
        "  int mz=1; for(i=1;i<=size(I2);i++){ if (ev(I2[i],PT)!=0) { mz=0; } }",
        '  print(tag+" MINORS_ZERO="+string(mz));',
        "  matrix Jc=jacob(I2); matrix Jp[nrows(Jc)][ncols(Jc)];",
        "  for(i=1;i<=nrows(Jc);i++){ for(j=1;j<=ncols(Jc);j++){ Jp[i,j]=ev(Jc[i,j],PT); } }",
        "  matrix Js=submat(Jp,1..nrows(Jp),freecols);",
        '  print(tag+" JACRANK_FREE="+string(mat_rk(Js))+" expected="+string(size(freecols)));',
        "  number Bv; number Cv; number beta; int rb=0; number tt;",
    ]
    for r in range(1, t):
        L += [f"  Bv=leadcoef(ev(B{r},PT)); Cv=leadcoef(ev(C{r},PT));",
              f'  print(tag+" r={r}: B="+string(Bv)+" C="+string(Cv));',
              f"  if (Bv!=0 && rb==0) {{ beta=-Cv/Bv; rb={r}; }}"]
    L += [
        "  if (rb>0) {",
        "    tt=leadcoef(a0)*beta^2+leadcoef(ev(b0,PT))*beta+leadcoef(ev(c0,PT));",
        '    print(tag+" BETA="+string(beta)+" (from r="+string(rb)+") TTOP_AT_LIFT="+string(tt));',
        "    int cons=1;",
    ]
    for r in range(1, t):
        L += [f"    if (leadcoef(ev(C{r},PT))+beta*leadcoef(ev(B{r},PT))!=0) {{ cons=0; }}"]
    L += ['    print(tag+" KERNEL_CONSISTENT="+string(cons));',
          '  } else { print(tag+" ALL_B_ZERO kernel (0:1)"); }',
          "  int wnz=0; number Wv;"]
    for r in range(1, t):
        L += [f"  Wv=leadcoef(ev(W{r},PT)); if (Wv!=0) {{ wnz=1; }}",
              f'  print(tag+" W{r}="+string(Wv)+" FITTcheck="+string(Wv==leadcoef(ev(B{r},PT))^2*tt));']
    L += ['  print(tag+" W_NONZERO_AT_POINT="+string(wnz));',
          "  return(wnz);",
          "}"]
    return L, vars_P

def job_pattern(t, L, vars_P, mfile, do_cone, dim_only=False):
    L.append(f'string MFILE="{mfile}";')
    if do_cone:
        L += ["int tmc=timer; ideal gI2=std(I2);",
              'print("CONE I2: dim="+string(dim(gI2))+" mult="+string(mult(gI2))+" time="+string(timer-tmc));']
    L += ["ideal Sl=subst(I2,b4,0)+ideal(b4); ideal gSl=std(Sl);",
          'print("SLICE b4=0 cone: dim="+string(dim(gSl)));']
    # main chart b4=1
    if dim_only:
        L += ["ideal J1=I2+ideal(b4-1); int tmd=timer; ideal gJ1=std(J1);",
              'print("MAIN vdim="+string(vdim(gJ1))+" dim="+string(dim(gJ1))+" time="+string(timer-tmd));',
              'write(":w "+MFILE+"_chartgb.txt", string(gJ1));',
              f'print("PATTERN_DONE t={t} (dim-only)");', "quit;"]
    L += ["ideal J1=I2+ideal(b4-1); list fx; fx[1]=number(1);",
          'int ok=probe(J1,2,fx,"MAIN");',
          f'if (ok==1) {{ evalpoint(2..{t-1},"MAIN"); }}']
    # boundary strata: b4=0, q2..q_{j-1}=0, q_j=1 for j=2..t-1
    for j in range(2, t):
        fixed = ["number(0)"] + ["number(0)"]*(j-2) + ["number(1)"]
        eqs = ["b4"] + [f"q{i}_0" for i in range(2, j)] + [f"q{j}_0-1"]
        L += [f"ideal Bd{j}=I2+ideal({','.join(eqs)}); list fx{j}; " + " ".join(f"fx{j}[{i+1}]={v};" for i, v in enumerate(fixed)),
              f'print("BDRY{j} stratum b4=0,q<{j}=0,q{j}=1");']
        if j < t-1:
            fc = ",".join(str(i) for i in range(1, t) if i != j)
            L += [f'ok=probe(Bd{j},{j+1},fx{j},"BDRY{j}");',
                  f'if (ok==1) {{ evalpoint(intvec({fc}),"BDRY{j}"); }}']
        else:
            # last stratum: the q_{t-1}-axis point; no free variables: check membership directly
            L += [f"ideal gBd{j}=std(Bd{j});",
                  f'print("BDRY{j} axis point in Gamma: "+string(vdim(gBd{j})));',
                  f"if (vdim(gBd{j})>=1) {{ PT=fx{j}; PTOK=1; evalpoint(intvec({','.join(str(i) for i in range(1,t) if i != j)}),\"BDRY{j}\"); }}"]
    L.append(f'print("PATTERN_DONE t={t}");')

def job_exactchart(t, L, vars_P, mfile, factor, nfmod=False):
    L.append(f'string MFILE="{mfile}";')
    if nfmod:
        L += ['LIB "nfmodstd.lib";', "ideal J1=I2+ideal(b4-1); int tm=timer; ideal gJ1=nfmodStd(J1); attrib(gJ1,\"isSB\",1);"]
    else:
        L += ["ideal J1=I2+ideal(b4-1); int tm=timer; ideal gJ1=std(J1);"]
    L += [
          'print("EXACT chart b4=1: vdim="+string(vdim(gJ1))+" dim="+string(dim(gJ1))+" gbsize="+string(size(gJ1))+" time="+string(timer-tm));',
          'write(":w "+MFILE+"_gb.txt", string(gJ1));',
          "tm=timer; ideal U=finduni(gJ1); poly m=U[2];",
          'print("EXACT minpoly q2: ordinary_degree="+string(deg(m) div 2)+" size="+string(size(m))+" time="+string(timer-tm));',
          'write(":w "+MFILE+"_q2_0.txt", string(m));',
          "poly gg=gcd(m,diff(m,q2_0));",
          'print("EXACT minpoly q2 squarefree="+string(deg(gg)==0));',
          'print("EXACT_MINPOLY_WRITTEN");']
    if factor:
        L += ["tm=timer; list FL=factorize(m); string s=\"\"; int i;",
              '  for (i=1;i<=size(FL[1]);i++) { if (deg(FL[1][i])>0) { s=s+" "+string(deg(FL[1][i]) div 2)+"^"+string(FL[2][i]); } }',
              'print("EXACT FACTOR_PATTERN over A_t:"+s+" time="+string(timer-tm));']
    L.append(f'print("EXACTCHART_DONE t={t}");')

def job_boundary(t, L, vars_P, mfile):
    L.append(f'string MFILE="{mfile}";')
    L += ["ideal Sl=subst(I2,b4,0)+ideal(b4); int tm=timer; ideal gSl=std(Sl);",
          'print("BOUNDARY slice b4=0 cone: dim="+string(dim(gSl))+" time="+string(timer-tm));']
    for j in range(2, t):
        eqs = ["b4"] + [f"q{i}_0" for i in range(2, j)] + [f"q{j}_0-1"]
        L += [f"ideal Bd{j}=I2+ideal({','.join(eqs)}); tm=timer; ideal gBd{j}=std(Bd{j});",
              f'print("BOUNDARY stratum j={j}: vdim="+string(vdim(gBd{j}))+" dim="+string(dim(gBd{j}))+" time="+string(timer-tm));',
              f"if (vdim(gBd{j})>0) {{",
              f"  ideal BW{j}=Bd{j}+Ws; ideal gBW{j}=std(BW{j});",
              f'  print("BOUNDARY stratum j={j} + (W): vdim="+string(vdim(gBW{j}))+"  (0 <=> W nonvanishing at every geometric point of the stratum)");']
        if j < t-1:
            L += [f"  ideal U{j}=finduni(gBd{j}); int i{j}; int k{j}; poly m{j}; list FL{j}; string s{j};",
                  f"  for (k{j}={j+1}; k{j}<={t-1}; k{j}++) {{ m{j}=U{j}[k{j}]; FL{j}=factorize(m{j}); s{j}=\"\";",
                  f'    for (i{j}=1;i{j}<=size(FL{j}[1]);i{j}++) {{ if (deg(FL{j}[1][i{j}])>0) {{ s{j}=s{j}+" "+string(deg(FL{j}[1][i{j}]) div k{j})+"^"+string(FL{j}[2][i{j}]); }} }}',
                  f'    print("BOUNDARY stratum j={j} minpoly "+string(var(k{j}))+" ordinary_degree="+string(deg(m{j}) div k{j})+" FACTOR_PATTERN:"+s{j}+"  minpoly="+string(m{j}));',
                  f"  }}"]
        L += ["}"]
    L.append(f'print("BOUNDARY_DONE t={t}");')

def job_colon(t, L, vars_P):
    # work in S
    L += ["setring S;",
          "int tm=timer; ideal gG=std(Gs);",
          'print("COLON (G): dim="+string(dim(gG))+" mult="+string(mult(gG))+" time="+string(timer-tm));',
          "tm=timer; ideal Q=quotient(Gs,ideal(Ttop));",
          'print("COLON (G):Ttop computed: ngens="+string(size(Q))+" time="+string(timer-tm));',
          "ideal Qr=reduce(Q,gG); int eq=(size(Qr)==0);",
          'print("COLON (G):Ttop == (G) : "+string(eq));',
          "if (eq==0) { ideal gQ=std(Q); print(\"COLON quotient: dim=\"+string(dim(gQ))+\" mult=\"+string(mult(gQ))); }",
          # control: b3 must be a zerodivisor? No: (C) hsop <=> b3 nzd. Control instead with a known zerodivisor: G1 itself is in (G) so (G):G1 = S (unit)
          "ideal Qc=quotient(Gs,ideal(G1)); print(\"COLON control (G):G1 is unit: \"+string(reduce(1,std(Qc))==0));",
          # second control: the axis coordinate b4 (zerodivisor iff a component lies in b4=0; the b3-axis does!) so (G):b4 != (G) expected
          "ideal Qa=quotient(Gs,ideal(b4)); ideal Qar=reduce(Qa,gG); print(\"COLON control (G):b4 == (G) (expected 0, the b3-axis lies in b4=0): \"+string(size(Qar)==0));",
          f'print("COLON_DONE t={t}");']

def job_verifypoint(t, L, vars_P, point):
    vals = point.split(',')
    assert len(vals) == len(vars_P), (len(vals), len(vars_P))
    L += ["list fxv;"] + [f"fxv[{i+1}]=number({v});" for i, v in enumerate(vals)]
    L += ["PT=fxv; PTOK=1;",
          "ideal J1=I2+ideal(b4-1); ideal Fp=J1; int i;",
          "for (i=2;i<=nvars(basering);i++) { Fp=Fp+ideal(var(i)-PT[i]); }",
          "ideal gFp=std(Fp);",
          'print("VERIFY local vdim of the chart scheme at the point (1 <=> the point lies on Gamma and is simple): "+string(vdim(gFp)));',
          f'evalpoint(2..{t-1},"VERIFY");',
          f'print("VERIFYPOINT_DONE t={t}");']

def job_msolve(t, L, vars_P, outfile, system):
    # export the chart system mod p in msolve format; variables renamed q2..q{t-1} (and b3 for the CI system)
    if system == 'ci':
        L += ["setring S;",
              "ideal Sys=subst(Gs,b4,1);",
              f"string vs=\"{','.join([f'q{j}' for j in range(2,t)]+['b3'])}\";"]
    else:
        L += ["ideal Sys=subst(I2,b4,1);",
              f"string vs=\"{','.join([f'q{j}' for j in range(2,t)])}\";"]
    L += [f'string fn="{outfile}";',
          'write(":w "+fn, vs);',
          'write(":a "+fn, string(char(basering)));',
          "int i; string s;",
          "for (i=1;i<=size(Sys);i++) {",
          "  s=string(Sys[i]);",
          ]
    for j in range(2, t):
        L.append(f'  s=replaceall(s, "q{j}_0", "q{j}");' if False else f'  while (find(s,"q{j}_0")>0) {{ s=s[1,find(s,"q{j}_0")-1]+"q{j}"+s[find(s,"q{j}_0")+{len(f"q{j}_0")},size(s)]; }}')
    L += ['  if (i<size(Sys)) { s=s+","; }',
          '  write(":a "+fn, s);',
          "}",
          'print("MSOLVE_EXPORT_DONE ngens="+string(size(Sys)));']

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("t", type=int)
    ap.add_argument("--mode", choices=("exact", "mod"), default="mod")
    ap.add_argument("--prime", type=int)
    ap.add_argument("--branch", type=int, default=0)
    ap.add_argument("--job", choices=("pattern", "exactchart", "boundary", "colon", "msolve", "verifypoint"), required=True)
    ap.add_argument("--point")
    ap.add_argument("--no-cone", action="store_true")
    ap.add_argument("--dim-only", action="store_true")
    ap.add_argument("--factor", action="store_true")
    ap.add_argument("--nfmod", action="store_true")
    ap.add_argument("--system", choices=("ci", "minors"), default="ci")
    ap.add_argument("--outdir", default=str(HERE))
    a = ap.parse_args()
    outdir = pathlib.Path(a.outdir)
    stem = f"{a.job}_t{a.t}_{a.mode}" + (f"_p{a.prime}_b{a.branch}" if a.mode == 'mod' else "")
    if a.job == 'msolve': stem += f"_{a.system}"
    if a.job == 'exactchart' and a.nfmod: stem += '_nfmod'
    L, vars_P = prefix(a.t, a.mode, a.prime, a.branch, stem)
    mfile = str(outdir / f"minpoly_{stem}")
    if a.job == 'pattern': job_pattern(a.t, L, vars_P, mfile, not a.no_cone, a.dim_only)
    if a.job == 'pattern' and a.dim_only: stem += '_dimonly'
    elif a.job == 'exactchart': job_exactchart(a.t, L, vars_P, mfile, a.factor, a.nfmod)
    elif a.job == 'boundary': job_boundary(a.t, L, vars_P, mfile)
    elif a.job == 'colon': job_colon(a.t, L, vars_P)
    elif a.job == 'msolve': job_msolve(a.t, L, vars_P, str(outdir / f"{stem}.ms"), a.system)
    elif a.job == 'verifypoint': job_verifypoint(a.t, L, vars_P, a.point)
    L.append('print("JOB_DONE");')
    L.append("quit;")
    path = outdir / f"{stem}.sing"
    path.write_text("\n".join(L) + "\n")
    print(path)

if __name__ == '__main__':
    main()
