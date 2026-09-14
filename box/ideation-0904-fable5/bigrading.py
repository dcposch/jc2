#!/usr/bin/env python3
"""E1: does the K16 cone ideal I_(t,+) admit a second grading?  For each t,
load the banked exact rows (box/k16toptail-20260903/rows_t{t}_exact.sing) in
Singular, dump every monomial exponent vector per row, and compute over Q the
null space of all within-row exponent differences.  Rank of that null space =
number of independent gradings for which every row is homogeneous."""
import subprocess, sys, json
from fractions import Fraction
HERE="/home/ubuntu/jc2/box/k16toptail-20260903"
def Ht(t):
    q=2*t+1; return f"{12*q*q}*yy^2-{12*q*(t+1)}*yy+{(t+1)*(3*t+2)}"
def run(t):
    vars_=["b4"]+[f"q{j}_0" for j in range(2,t)]+["b3"]
    wts=[1]+list(range(2,t))+[t+1]
    sing=f"""ring W=(0,yy),({",".join(vars_)}),wp({",".join(map(str,wts))});
minpoly={Ht(t)};
execute(read("{HERE}/rows_t{t}_exact.sing"));
int i; int j; intvec e;
for (i=1;i<=size(TT);i++) {{
  for (j=1;j<=size(TT[i]);j++) {{ e=leadexp(TT[i][j]); print("ROW "+string(i)+" "+string(e)); }}
}}
quit;
"""
    open(f"bigrading_t{t}.sing","w").write(sing)
    out=subprocess.run(["timeout","300","Singular","-q","--no-rc","bigrading_t{}.sing".format(t)],capture_output=True,text=True).stdout
    open(f"bigrading_t{t}.out","w").write(out)
    rows={}
    for line in out.splitlines():
        if line.startswith("ROW "):
            p=line.split(); r=int(p[1]); e=[int(x) for x in p[2].split(",")]
            rows.setdefault(r,[]).append(e)
    if "error" in out.lower(): print("SINGULAR ERROR at t=",t); print(out[:2000]); return
    n=len(vars_); diffs=[]
    for r,es in rows.items():
        e0=es[0]
        for e in es[1:]: diffs.append([Fraction(a-b) for a,b in zip(e,e0)])
    # null space over Q via row reduction
    M=[d[:] for d in diffs]; piv=[]; rnk=0
    for c in range(n):
        pr=None
        for i in range(rnk,len(M)):
            if M[i][c]!=0: pr=i; break
        if pr is None: continue
        M[rnk],M[pr]=M[pr],M[rnk]
        pv=M[rnk][c]; M[rnk]=[x/pv for x in M[rnk]]
        for i in range(len(M)):
            if i!=rnk and M[i][c]!=0:
                f=M[i][c]; M[i]=[a-f*b for a,b in zip(M[i],M[rnk])]
        piv.append(c); rnk+=1
    free=[c for c in range(n) if c not in piv]
    basis=[]
    for fc in free:
        v=[Fraction(0)]*n; v[fc]=Fraction(1)
        for i,pc in enumerate(piv): v[pc]=-M[i][fc]
        basis.append(v)
    # check the known weight vector is in the null space
    w=[Fraction(x) for x in wts]
    ok=all(sum(a*b for a,b in zip(d,w))==0 for d in diffs)
    nterms={r:len(es) for r,es in rows.items()}
    print(f"t={t} vars={vars_} rows={len(rows)} terms/row={[nterms[k] for k in sorted(nterms)]} diffs={len(diffs)} rank={rnk} nullity={len(basis)} w_in_null={ok}")
    for v in basis: print("   grading:", [str(x) for x in v])
    json.dump({"t":t,"vars":vars_,"nullity":len(basis),"basis":[[str(x) for x in v] for v in basis],"w_in_null":ok,"terms":nterms},open(f"bigrading_t{t}.json","w"))
for t in [3,4,5,6]:
    run(t)
