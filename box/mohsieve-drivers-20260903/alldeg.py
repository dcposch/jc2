import sys
from fractions import Fraction as F
sys.path.insert(0,'box')
import moh_skeleton_full as MS
def Av(S): return [S.A(j) for j in range(1,S.s)]
def incr(S): return all(a>=2 for a in Av(S))
def M3(S): return incr(S) and S.any10() and S.V[2]>=2      # MOH-3: the triple filter

print("== CONTROL (fail-closed): Moh's six printed rows under MOH-3 ==")
ok=True
for (n,m,Ms,V,name,d2,d1,err) in MS.MOH_TABLE:
    S=MS.Skel(n,m,Ms,V); r=M3(S); ok &= r
    print(f"  {name:<24} INCR={incr(S)} any10={S.any10()} V2={S.V[2]}  -> {r}")
print("  ALL SIX KEPT:", ok)

print("\n== campaign space D=48..200 (Kmin=16): groups under (1)-(13) vs MOH-3 ==")
print(f"{'D':>5} {'grp13':>6} {'grpM3':>6} {'rows13':>7} {'rowsM3':>7}")
tot13=totM3=g13=gM3=0; empties=[]
for n in range(48,201):
    G13=set(); GM3=set(); r13=rM3=0
    for (m,Ms,V) in MS.census(n,Kmin=16,full=True):
        S=MS.Skel(n,m,Ms,V); r13+=1; G13.add((m,Ms,S.V[S.s]))
        if M3(S): rM3+=1; GM3.add((m,Ms,S.V[S.s]))
    tot13+=r13; totM3+=rM3; g13+=len(G13); gM3+=len(GM3)
    if r13 and not rM3: empties.append(n)
    if n<=125 or r13:
        print(f"{n:>5} {len(G13):>6} {len(GM3):>6} {r13:>7} {rM3:>7}")
print(f"TOTAL 48-200: groups {g13} -> {gM3} ; rows {tot13} -> {totM3}")
print("DEGREES EMPTIED BY MOH-3 (had a (1)-(13) skeleton, none survives):", empties)
