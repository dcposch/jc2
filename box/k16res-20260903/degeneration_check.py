#!/usr/bin/env python3
"""Torus-degeneration obstruction.  For a weight c not proportional to w, let J = argmax_j c_j/w_j (dominant set), K = complement.
For a weight-d_r form, c.e = mu*d_r - sum_{k in K} delta_k e_k with delta_k>0, so in_c(R_r) is spanned by the monomials of R_r of
minimal deficiency sum delta_k e_k.  If every x_J-free monomial m of R_r is dominated by a monomial m' of R_r with e_J(m')!=0 and
e_K(m') <= e_K(m) componentwise (not equal), then for EVERY c with dominant set J, in_c(R_r) lies in the ideal (x_j : j in J),
hence V(in_c R_1..R_n) contains the coordinate subspace V(x_J) of dimension |K| >= 1.  This script checks the domination
condition on the actual supports for every proper nonempty J and every r."""
import sys, itertools
sys.path.insert(0,'.')
from macaulay_window import parse_ideal, terms
import re
def support(poly, vars_):
    S=set()
    for tm in terms(poly):
        m=re.match(r"([+-]?)\s*(\([^)]*\)|[0-9/]+)?\*?(.*)$", tm); mon=m.group(3)
        e=[0]*len(vars_)
        if mon:
            for f in mon.split("*"):
                if "^" in f: v,k=f.split("^"); k=int(k)
                else: v,k=f,1
                e[vars_.index(v)]+=k
        S.add(tuple(e))
    return S
def check(t, path):
    n=t-1; vars_=["b4"]+[f"q{j}_0" for j in range(2,t)]
    polys=parse_ideal(path); R={t-m:support(pl,vars_) for m,pl in enumerate(polys,start=1)}
    bad=[]
    for size in range(1,n):
        for J in itertools.combinations(range(n),size):
            K=[k for k in range(n) if k not in J]
            for r in range(1,n):
                S=R[r]; withJ=[e for e in S if any(e[j] for j in J)]
                for m in S:
                    if any(m[j] for j in J): continue
                    dom=any(all(mp[k]<=m[k] for k in K) and any(mp[k]<m[k] for k in K) for mp in withJ)
                    if not dom: bad.append((J,r,m)); break
    return bad
for t,path in [(3,"/home/ubuntu/jc2/box/k16toptail-20260903/restop_t3_exact.sing"),(4,"/home/ubuntu/jc2/box/k16toptail-20260903/restop_t4_exact.sing"),
               (5,"/home/ubuntu/jc2/box/k16toptail-20260903/restop_t5_exact.sing"),(6,"/home/ubuntu/jc2/box/k16toptail-20260903/restop_t6_exact.sing"),
               (7,"restop_t7_mod_p32059_r4425.sing")]:
    bad=check(t,path)
    print(f"t={t}: domination condition holds for all proper J and all r: {not bad}; violations={bad[:5]}")
