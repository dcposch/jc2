from fractions import Fraction as Q
np_,mp_=42,28; Mp={1:-28,2:35,3:40}; dp={1:42,2:14,3:7,4:1}; H=2
lam2=Q(-1,3-0)/1; lam2=Q(Q(-1,3)-H, np_-Mp[2]); W=70; d2=Q(-1,3)
def S_of(a):
    rhoP=Q(mp_*a,dp[2]); kappa=mp_*lam2+rhoP*(H-d2)
    if kappa<=0: return ("below/at average -> sink or excluded", Q(0), kappa)
    dfin=H-Q(W*kappa,W*rhoP-mp_); return (f"delta_fin={dfin}", Q(np_,np_+mp_)*rhoP*(H-dfin), kappa)
print("If the forbidden-average rule were DROPPED, the z=2 competitor pi^2(pi^3-c1)^3(pi^3-c2)^1:")
tot=Q(0)
for name,a,mult in [("zero",2,1),("orbitA",3,3),("orbitB",1,3)]:
    txt,S,k=S_of(a); tot+=mult*S; print(f"  {name:8s} x{mult} a={a}: kappa={k}  {txt}  S={S}")
print(f"  => sum {tot}  INTEGRAL={tot.denominator==1}   <-- would SURVIVE")
print("\nSo the z=2 exclusion (multiplicity == P/Q = 2) is load-bearing for the R063 kill.")
