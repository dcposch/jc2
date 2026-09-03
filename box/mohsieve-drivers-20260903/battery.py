import sys
from fractions import Fraction as F
sys.path.insert(0,'box')
import moh_skeleton_full as MS
def Av(S): return [S.A(j) for j in range(1,S.s)]
def incr(S): return all(a>=2 for a in Av(S))
BASE=lambda S: incr(S) and S.any10()

CL = {
 "V2>=2":         lambda S: S.V[2]>=2,
 "Vj>=2 all j":   lambda S: all(S.V[j]>=2 for j in range(2,S.s+1)),
 "A_1<=e":        lambda S: S.A(1)<=S.e,
 "A_1>=3":        lambda S: S.A(1)>=3,
 "A_1<=e & V2>=2":lambda S: S.A(1)<=S.e and S.V[2]>=2,
 "eV2>=A_1*V2+1": lambda S: S.e*S.V[2] >= S.A(1)*S.V[2]+1,
 "u_s=1":         lambda S: S.d[S.s]-S.V[S.s]==1,
 "q>=1/2":        lambda S: S.q()>=F(1,2),
 "V2>=2|s>=4":    lambda S: S.V[2]>=2 or S.s>=4,
 "d_{s+1}=1":     lambda S: S.d[S.s+1]==1,
}
# fail-closed on the six + the (75,50) discriminator
print(f"{'clause':<16} {'keeps 6/6':>9} {'(75,50) kills{5,10,40,60}&keeps 55':>36} {'n<=100 rows':>12}")
for name,f in CL.items():
    six = all(f(MS.Skel(n,m,Ms,V)) for (n,m,Ms,V,_,_,_,_) in MS.MOH_TABLE)
    keptM2=set(); n7550=0
    for (m,Ms,V) in MS.census(75,Kmin=1,full=True):
        if m!=50: continue
        S=MS.Skel(75,m,Ms,V)
        if BASE(S) and f(S): keptM2.add(Ms[0]); n7550+=1
    disc = (keptM2=={55} and n7550==2)
    tot=0
    for n in range(4,101):
        for (m,Ms,V) in MS.census(n,Kmin=1,full=True):
            S=MS.Skel(n,m,Ms,V)
            if BASE(S) and f(S): tot+=1
    print(f"{name:<16} {str(six):>9} {str(disc)+' (M2 kept '+str(sorted(keptM2))+', '+str(n7550)+' rows)':>36} {tot:>12}")
