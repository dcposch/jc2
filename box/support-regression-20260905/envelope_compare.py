"""Chart h-support vs the h-support gate's source envelope S_1 = D_1 u G_1.

D_1  : raw centered-D1 floor      { (r,s) : s<K, -r + delta1*s >= B }
G_1  : outer-disc envelope (gate  { (r,s) : s<K, r <= floor(d*(K-s)) },  d = -delta_s
       report section 4)
chart: order_basis_full rule      { (r,s) : s<K, r+s<K, 0<=r<=u', -r+delta1*s >= B }
"""
from fractions import Fraction as F
from math import floor

def compare(name, K, u, V2, d1, d2):
    B = V2*d1 + u*d2
    d = -d2
    chart = {(r,s) for s in range(K) for r in range(0,u+1) if r+s < K and -r+d1*s >= B}
    D1 = {(r,s) for s in range(K) for r in range(0,400) if -r+d1*s >= B}
    G1 = {(r,s) for s in range(K) for r in range(0, floor(d*(K-s))+1)}
    S1 = D1 | G1
    print(f"{name}: K={K} u'={u} V2'={V2} delta1={d1} delta_s={d2} B={B} d={d}")
    print(f"  chart h-support  {len(chart):3d}  {sorted(chart)}")
    print(f"  D_1              {len(D1):3d}")
    print(f"  G_1              {len(G1):3d}")
    print(f"  S_1 = D_1 u G_1  {len(S1):3d}")
    print(f"  MISSING          {len(S1-chart):3d}  {sorted(S1-chart)}")
    print(f"  total-degree cap recoverable from G_1 (needs d<=1)? {'YES' if d <= 1 else 'NO'}")
    print()

# S5: descended (9,6; M'=(-6,2), V2'=1, K'=3, u'=2, ell=8)
compare("S5", 3, 2, 1, F(3,2), F(-3,2))
# S6: descended (9,6; M'=(-6,5), V2'=2, K'=3, u'=1, ell=8); R=9-5-1=3, delta2'=-9/3
compare("S6", 3, 1, 2, F(2,3), F(-3,1))

# k=4 ray, for contrast: delta_s = -(ell+1)/(n'-Ms'-1) = -5/5 = -1 for every K
print("k=4 ray (3K,2K; 3K-6; K-1; 4):")
for K in (7,8,9):
    n2, Ms, ell = 3*K, 3*K-6, 4
    ds = F(-(ell+1), n2-Ms-1)
    print(f"  K={K}: delta_s = {ds}, d = {-ds}  ->  G_1 = {{b+a <= K}} == chart cap  (SOUND)")
print()
print("(99,66) M=(-66,72,97), n=99, ell=0: delta_s =", F(-1, 99-97-1))
print("D=108   M=(-72,81,106), n=108, ell=0: delta_s =", F(-1, 108-106-1))
