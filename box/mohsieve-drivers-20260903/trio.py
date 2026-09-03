import sys
sys.path.insert(0,'box')
import moh_skeleton_full as MS
def Av(S): return [S.A(j) for j in range(1,S.s)]
print("== D=105 trio + all 14 (1)-(13) groups: which clause kills ==")
for (m,Ms,V) in MS.census(105,Kmin=16,full=True):
    S=MS.Skel(105,m,Ms,V)
    A=Av(S); i=all(a>=2 for a in A); a10=S.any10()
    tag="TRIO" if (m==70 and set(Ms)<= {28,40,103} and S.V[S.s] in (4,5,6)) else "    "
    print(f" {tag} m={m:>3} M={list(Ms)} V={dict(sorted(V.items()))} A={A} INCR={i} any10={a10} V2={S.V[2]} q={S.q()} -> {i and a10 and S.V[2]>=2}")
print("\n== D=117 (4 groups survive pinned-N) ==")
for (m,Ms,V) in MS.census(117,Kmin=16,full=True):
    S=MS.Skel(117,m,Ms,V); A=Av(S)
    print(f"  m={m} M={list(Ms)} V={dict(sorted(V.items()))} A={A} INCR={all(a>=2 for a in A)} any10={S.any10()} V2={S.V[2]} -> {all(a>=2 for a in A) and S.any10() and S.V[2]>=2}")
