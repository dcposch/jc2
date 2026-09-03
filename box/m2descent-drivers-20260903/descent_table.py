#!/usr/bin/env python3
"""M2-DESCENT step (2): Prop 6.3/6.4 descent applied to Moh's p.202 rows and to
the D = 105 trio.  GATE: the transformed table must reproduce Moh p.207."""
import sys, os
from fractions import Fraction as F
from math import gcd
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from moh_skeleton_full import Skel, census, MOH_TABLE

def descend(S):
    s, ds, Vs = S.s, S.d[S.s], S.V[S.s]
    us, vs = ds - Vs, Vs                       # Moh p.207: u_3 = d_3 - v_3
    # mu_j = lambda_j / d_j ,  lambda_j = sum_{i<=j} q_i d_i ,  q_1 = M_1, q_j = M_j - M_{j-1}
    lam, mus = 0, {}
    for j in range(1, s+1):
        q = S.M[1] if j == 1 else S.M[j]-S.M[j-1]
        lam += q*S.d[j]; mus[j] = F(lam, S.d[j])
    pdeg = {'g': F(us*S.n, ds)}
    for j in range(1, s): pdeg['T%d' % j] = us*(-mus[j])/ds
    return dict(us=us, vs=vs, ds=ds, n2=F(us*S.n, ds), m2=us*(-mus[1])/ds,
                M2=F(S.M[2], ds) if s >= 2 else None,
                V2=S.V[2], jac=vs-us-1, pdeg=pdeg,
                d2=F(S.d[2], ds), d3=(F(S.d[3], ds) if s >= 3 else None))

print("== GATE G1: Moh p.202 rows -> Moh p.207 transformed table ==")
print("  %-22s %5s %5s %5s | %4s %4s %6s %5s %s" %
      ("row","u_s","v_s","d_s","n'","m'","M_2'","V_2'","Jac"))
P207 = {(64,48,52): (16,12,13,3,1), (84,56,64): (21,14,16,2,1),
        (84,56,72): (21,14,18,5,1), (75,50,55): (15,10,11,None,2)}
ok = True
for (n,m,Ms,Vs,lab,_,_,_) in MOH_TABLE:
    S = Skel(n,m,Ms,Vs); D = descend(S)
    print("  %-22s %5d %5d %5d | %4s %4s %6s %5s X^%d" %
          (lab, D['us'], D['vs'], D['ds'], D['n2'], D['m2'], D['M2'], D['V2'], D['jac']))
    key = (n,m,Ms[0])
    if key in P207:
        e = P207[key]
        good = (D['n2']==e[0] and D['m2']==e[1] and D['M2']==e[2] and D['jac']==e[4]
                and (e[3] is None or D['V2']==e[3]))
        ok = ok and good
        if not good: print("      MISMATCH vs p.207:", e)
print("  p.207 (n, m, M_2, Jacobian) columns reproduced on all four u_s=1 rows:", ok)
print("  ((99,66) has u_s = %d: Prop 6.3 does not apply, Moh's p.209 dichotomy instead)"
      % descend(Skel(99,66,[77,97],{3:8,2:8}))['us'])

print("\n== the D = 105 trio under Prop 6.3 ==")
trio = []
for (m, Ms, V) in census(105, Kmin=16, full=True):
    S = Skel(105, m, list(Ms), V)
    if m != 70: continue
    D = descend(S)
    from moh_skeleton_full import uni_hits
    N = sorted(uni_hits([(S.V[2], S.q(), S.u)], 6, 16))
    if not N: continue
    trio.append((S,D,N))
for (S,D,N) in trio:
    print("  M=%s V=%s : u_s=%d v_s=%d d_s=%d -> (n',m')=(%s,%s) M_2'=%s V_2'=%s Jac=X^%d  N=%s"
          % ([S.M[i] for i in range(1,S.s+1)], {i:S.V[i] for i in range(2,S.s+1)},
             D['us'], D['vs'], D['ds'], D['n2'], D['m2'], D['M2'], D['V2'], D['jac'], N))
    print("      full descended pi-degree tower:", {k:str(v) for k,v in D['pdeg'].items()},
          " d_2'=%s d_3'=%s" % (D['d2'], D['d3']),
          " M_2'>m'? %s" % (D['M2'] > D['m2']))

print("\n== OPEN[DESCENT-CLOSURE]: which conditions survive the descent (M_i'=M_i/d_s, d_i'=d_i/d_s, V_i'=V_i) ==")
print("  (2),(3),(5) gcd/definition  : SURVIVE (homogeneous of weight 1 in the data)")
print("  (7) windows V_{i+1}d_i/d_{i+1} >= V_i > d_i/(n-M_i) : SURVIVES (both sides scale by d_s)")
print("  (6) 3<=s<=5 and d_s>=4      : d_s>=4 survives on Moh's rows, but s'=s-1, so 3<=s FAILS")
print("      (Moh's own descended rows have s'=2)  -> (6) does NOT descend")
print("  M_2 > m                     : SURVIVES exactly, in both directions (M_2/d_s > m/d_s)")
print("  (4) M_s = n-2               : FAILS (descended M_2'=13 vs n'-2=14 on Moh's first row)")
print("  (8)-(13) (the A_j increments): depend on delta', NOT reproduced -> OPEN")
