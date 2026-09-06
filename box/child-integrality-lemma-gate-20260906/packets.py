from fractions import Fraction as Q
from math import lcm
np_, mp_ = 42, 28
Mp = {1:-28, 2:35, 3:40}; dp = {1:42,2:14,3:7,4:1}; Vp={2:3,3:7}
H = 2
# level 3
P3 = Vp[3]*dp[3]//dp[4]; Q3 = P3*(np_-Mp[3])//dp[3]
print(f"r=3: P={P3} Q={Q3} delta=-2 A0=den(1*-2)={Q(-2).denominator} P/Q={Q(P3,Q3)}")
# level 2
P2 = Vp[3]*dp[2]//dp[3]; Q2 = P2*(np_-Mp[2])//dp[2]
d2 = Q(-1,3); A0 = (1*d2).denominator
print(f"r=2: P={P2} Q={Q2} delta={d2} A0={A0} avg P/Q={Q(P2,Q2)} == d'_2/(n'-M'_2)={Q(dp[2],np_-Mp[2])}")
print(" enumerate z with A0|(P-z), 0<=z<=P, partitions containing multiplicity V'_2=3:")
def parts(n, mx=None):
    if mx is None: mx=n
    if n==0: yield (); return
    for k in range(min(n,mx),0,-1):
        for rest in parts(n-k,k): yield (k,)+rest
for z in range(0, P2+1):
    if (P2-z)%A0: continue
    ok=[]
    for pa in parts((P2-z)//A0):
        if 1*(z>0)+A0*len(pa) > Q2: continue
        if 3 not in pa and z!=3: continue          # selected multiplicity 3 must occur
        if z==Q(P2,Q2) or any(a==Q(P2,Q2) for a in pa): continue   # forbidden average
        ok.append(pa)
    print(f"   z={z:3d}: {ok if ok else 'NONE'}")
print("\n=== PACKETS from p'_2 = pi^5 (pi^3-c)^3 ===")
lam2 = Q(d2-H, np_-Mp[2]); W = np_-Mp[1]
print(f" lambda_2=({d2}-{H})/({np_}-{Mp[2]})={lam2}   W=n'-M'_1={W}")
tot=Q(0); tp=0; tq=0
for name,a,mult in [("zero",5,1),("nonzero",3,3)]:
    rhoP = Q(mp_*a, dp[2]); rhoQ = Q(np_*a, dp[2])
    kappa = mp_*lam2 + rhoP*(H-d2)
    dfin = H - Q(W*kappa, W*rhoP - mp_)
    S = Q(np_, np_+mp_)*rhoP*(H-dfin)
    L = 1 if name=="zero" else lcm(1, d2.denominator)
    mod = (L*dfin).denominator
    res = (rhoP % mod, rhoQ % mod)
    print(f" {name:8s} x{mult}: a={a} rhoP={rhoP} rhoQ={rhoQ} kappa={kappa} delta_fin={dfin} S={S} | L={L} mod={mod} residue={res} pass={res in [(0,1),(1,0)]}")
    tot += mult*S; tp += mult*rhoP; tq += mult*rhoQ
print(f" root conservation: sum rhoP={tp} (m'={mp_}) sum rhoQ={tq} (n'={np_})")
print(f" ===> I'_M = {tot}   integral? {tot.denominator==1}")
