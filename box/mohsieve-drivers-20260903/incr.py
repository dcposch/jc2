import sys
from fractions import Fraction as F
sys.path.insert(0,'box')
import moh_skeleton_full as MS

def Aall(S): return [S.A(j) for j in range(1, S.s)]     # j = 1..s-1

# ---- fail-closed control on Moh's six printed rows ---------------------------
print("== CONTROL: Moh's six printed rows ==")
for (n,m,Ms,V,name,d2,d1,err) in MS.MOH_TABLE:
    S=MS.Skel(n,m,Ms,V)
    print(f"  {name:<24} A_j (j=1..s-1) = {Aall(S)}   any10={S.any10()}  full_ok={S.full_ok()}")

# ---- the 658 rows at n <= 100 (Moh's own space: no K>=16 floor) -------------
print("\n== n <= 100, Moh's own space (Kmin=1): filter cascade ==")
tot=0; keep_incr=0; keep_any10=0; keep_both=0; cls_both=set(); cls_tot=set()
per_level={}
rows_both=[]
for n in range(4,101):
    for (m,Ms,V) in MS.census(n, Kmin=1, full=True):
        S=MS.Skel(n,m,Ms,V); tot+=1; cls_tot.add((n,m))
        A=Aall(S); incr = all(a>=2 for a in A); a10=S.any10()
        for j,a in enumerate(A, start=1): per_level.setdefault(j,{}).setdefault(a,0); per_level[j][a]+=1
        if incr: keep_incr+=1
        if a10: keep_any10+=1
        if incr and a10: keep_both+=1; cls_both.add((n,m)); rows_both.append((n,m,Ms,V,A))
print(f"  (1)-(13) rows                : {tot:6d}   classes {len(cls_tot)}")
print(f"  + A_j >= 2 for all j (INCR)  : {keep_incr:6d}")
print(f"  + NOT-ALL-(11) alone         : {keep_any10:6d}")
print(f"  + BOTH                       : {keep_both:6d}   classes {len(cls_both)}")
print(f"  classes surviving BOTH: {sorted(cls_both)}")
print("\n  A_j value histogram by level (top 8 each):")
for j in sorted(per_level):
    h=sorted(per_level[j].items())[:8]
    print(f"    j={j}: {h} ... (A_j=1 count = {per_level[j].get(1,0)})")
print("\n  rows surviving BOTH:")
for r in rows_both: print("   ", r)
