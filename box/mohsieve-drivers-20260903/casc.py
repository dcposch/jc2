import sys
from fractions import Fraction as F
sys.path.insert(0,'box')
import moh_skeleton_full as MS
def A(S): return [S.A(j) for j in range(1,S.s)]
def incr(S): return all(a>=2 for a in A(S))

print("== (75,50): who survives what ==")
for (m,Ms,V) in MS.census(75,Kmin=1,full=True):
    if m!=50: continue
    S=MS.Skel(75,m,Ms,V)
    print(f"  M={list(Ms)} V2={V[2]:>2}  A={A(S)}  any10={str(S.any10()):>5}  INCR={str(incr(S)):>5}  "
          f"BOTH={str(incr(S) and S.any10()):>5}  V2>=2={V[2]>=2}   <-- MOH KEEPS M2=55")

print("\n== cascade at n<=100 (Moh space) with V_2>=2 added ==")
c={'raw':0,'I':0,'IA':0,'IAV':0}
cls={'raw':set(),'IA':set(),'IAV':set()}
for n in range(4,101):
    for (m,Ms,V) in MS.census(n,Kmin=1,full=True):
        S=MS.Skel(n,m,Ms,V); c['raw']+=1; cls['raw'].add((n,m))
        if not incr(S): continue
        c['I']+=1
        if not S.any10(): continue
        c['IA']+=1; cls['IA'].add((n,m))
        if V[2]>=2: c['IAV']+=1; cls['IAV'].add((n,m))
print(f"  raw (1)-(13)           {c['raw']:6d}  cls {len(cls['raw'])}")
print(f"  + INCR                 {c['I']:6d}")
print(f"  + NOT-ALL-(11)         {c['IA']:6d}  cls {len(cls['IA'])}")
print(f"  + V_2 >= 2             {c['IAV']:6d}  cls {len(cls['IAV'])}")
print(f"  classes at last stage: {sorted(cls['IAV'])}")
