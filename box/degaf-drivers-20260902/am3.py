import sys; sys.path.insert(0,'/tmp/degaf')
from am2 import semigroups, memb_array, sgp_from, am_data
from math import gcd
def n_min_lower(gaps, cap=80):
    """least n admitting: n in Gamma; AM(n,Gamma); delta<=p_a(n); and SOME p in Gamma,
       0<p<n, p not | n, with delta <= p_a(n) - (n-p)(n-p-1)/2   [branch-at-infinity
       multiplicity is exactly n-p, so delta_inf >= (n-p)(n-p-1)/2]."""
    g=len(gaps); N=max(4*g+40,200); M=memb_array(gaps,N)
    for n in range(1,cap+1):
        if not M[n]: continue
        if g>(n-1)*(n-2)//2: continue
        if am_data(gaps,n,N) is None: continue
        okp=False
        for p in range(1,n):
            if not M[p]: continue
            if n%p==0: continue
            if g <= (n-1)*(n-2)//2 - (n-p)*(n-p-1)//2: okp=True; break
        if n==1: okp=True
        if okp: return n
    return None
print(" delta  #Gamma  admissible Gammas          n_min-lower per Gamma       max")
for g in range(0,9):
    SG=semigroups(g); rows=[]
    for gaps in SG:
        v=n_min_lower(gaps)
        if v is not None: rows.append((v,gaps))
    rows.sort()
    mx=max(v for v,_ in rows) if rows else None
    print(f"  {g:2d}   {len(SG):5d}   {len(rows):3d} admissible   "
          f"{sorted(set(v for v,_ in rows))}   max={mx}  (2d+1={2*g+1})")
