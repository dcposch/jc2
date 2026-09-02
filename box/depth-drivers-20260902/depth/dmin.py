#!/usr/bin/env python3
"""
MOH-SHARP-2 : which degrees D can be the minimal degree D_min of a Jacobian
counterexample, from refs/-verified constraints only.

  (F1) D = K*e, K = gcd(deg P, deg Q), e = max(d,e) >= 3, gcd(d,e)=1, d>=2
       [ (LF)+(MIN); Moh Prop 5.4/5.5; GGV Rem 4.2 ]
  (F2) K >= 16                              [ GGV Cor 6.6 ]
  (F3) K has a divisor c with 4 <= c < K    [ Moh Cor 6.1 (d_s>=4) + Prop 5.5 (s>=3) ]
  (F4) K is neither p nor 2p (p prime)      [ GGV Cor 7.9's argument at K = a+b ]
  (F5) D >= 101                             [ Moh 1983, Appendix II ]
"""
from sympy import isprime, divisors

def kmin_ok(K, f3=True, f4=True):
    if K < 16: return False
    if f3 and not any(4 <= c < K for c in divisors(K)): return False
    if f4:
        if isprime(K): return False
        if K % 2 == 0 and isprime(K//2): return False
    return True

def admissible(D, f3=True, f4=True):
    good=[]
    for K in divisors(D):
        e = D//K
        if e < 3: continue
        if not kmin_ok(K, f3, f4): continue
        # need some d with 2 <= d < e, gcd(d,e)=1
        from math import gcd
        if any(gcd(d,e)==1 for d in range(2,e)):
            good.append(K)
    return good

if __name__=="__main__":
    for label,(f3,f4) in [("MOH-SHARP (MKS: K>=16, K<=D/3)",(False,False)),
                          ("+ (F3) Moh d_s>=4, s>=3      ",(True,False)),
                          ("+ (F4) GGV Cor 7.9 at K      ",(True,True))]:
        adm = [D for D in range(101,141) if admissible(D,f3,f4)]
        print(f"{label}: admissible D in [101,140] = {adm}")
        print(f"{'':38}  => D_min >= {adm[0] if adm else '-'}")
    print()
    print("admissible D in [101,200] under all of (F1)-(F5):")
    adm = [D for D in range(101,201) if admissible(D)]
    print(" ", adm)
    print("  count:", len(adm), "of 100")
    print()
    print("K-menu for the first few admissible D:")
    for D in adm[:10]:
        print(f"   D={D:4d}  K in {admissible(D)}")
    print()
    print("check: Moh's four surviving degree pairs pass (F1)-(F4)?")
    for (n,m) in [(64,48),(84,56),(75,50),(99,66)]:
        from math import gcd
        K=gcd(n,m)
        print(f"   (n,m)=({n},{m}) K={K} e={n//K} d={m//K} "
              f"F2:{K>=16} F3:{any(4<=c<K for c in divisors(K))} "
              f"F4:{not isprime(K) and not (K%2==0 and isprime(K//2))}")
