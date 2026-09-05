#!/usr/bin/env python3
"""Prop 6.3 radius hypothesis: the exact residual window per skeleton row.

RADIUS DICHOTOMY (derived from Moh Prop 6.1(2), Prop 4.6(1) and the definition
of delta*_{s-1}; this is Moh's own Prop 6.4 proof with the gcd computed at
general u_s):

    either  delta*_{s-1} >= v_s/u_s          [Prop 6.3 licensed]
    or      the minor cluster splits at delta = delta*_{s-1} in [1, v_s/u_s)
            with leading polynomial p(pi), deg p | u_s, and q = #{distinct
            roots of p} >= 2 ;  hence u_s >= 2, and (Galois) den(delta*) | q
            or | q-1, so den(delta*) <= u_s   [= N5].

So the residual obligation on a u_s >= 2 row is exactly: every candidate split
order in the window is excluded or separately killed.
"""
from fractions import Fraction as F

def window(u_s, v_s, open_at_one=True):
    """candidate split orders delta in (1, v_s/u_s) [or [1,...) ] with den <= u_s."""
    hi = F(v_s, u_s)
    out = []
    for den in range(1, u_s+1):
        num = den if open_at_one else den   # start scan at delta = 1
        d = F(num, den)
        while d < hi:
            if d.denominator <= u_s and (d > 1 or not open_at_one) and d not in out:
                out.append(d)
            num += 1; d = F(num, den)
    return sorted(set(out))

def divisors(n): return [k for k in range(1, n+1) if n % k == 0]

ROWS = [
    # tag, n, m, d_s, v_s, u_s, descended (n',m'), ell
    ("D=108 no-split  (108,72) M=(-72,81,106) V=(7,7)   [17(fffff),(ssss)]",
     108, 72, 9, 7, 2, (24,16), 4),
    ("(99,66) case (A) M=(-66,77,97) V=(8,8)  S8         [17(bbbbbb)]",
     99, 66, 11, 8, 3, (27,18), 4),
    ("(99,66) sibling  M=(-66,22,97) V=(1,8)  S4",
     99, 66, 11, 8, 3, (27,18), 4),
    ("k=4 ray K=7      (147,98) all 6 rows, u_s=1",
     147, 98, 7, 6, 1, (21,14), 4),
    ("k=4 ray K=8      (168,112) 277 rows,  u_s=1",
     168, 112, 7, 6, 1, (24,16), 4),
    ("k=4 ray K=9      (189,126) 78 rows,   u_s=1",
     189, 126, 7, 6, 1, (27,18), 4),
]

if __name__ == "__main__":
    for tag, n, m, ds, vs, us, np_, ell in ROWS:
        assert us == ds - vs, (tag, us, ds, vs)
        assert (n//ds)*us == np_[0] and (m//ds)*us == np_[1], tag
        assert vs - us - 1 == ell, tag
        print(f"\n{tag}")
        print(f"  n={n} m={m}  d_s={ds} v_s={vs} u_s={us}  ->  ({np_[0]},{np_[1]}) ell={ell}")
        print(f"  Prop 6.3 hypothesis : delta*_(s-1) >= v_s/u_s = {F(vs,us)}")
        if us == 1:
            print("  Prop 6.4 (p.198)    : u_s = 1  =>  AUTOMATIC.  residual window = {} (empty)")
            continue
        degp = [k for k in divisors(us) if k >= 2]
        w = window(us, vs)
        print(f"  Prop 6.4            : N/A (u_s >= 2)")
        print(f"  deg p | u_s, deg p >= 2 => deg p in {degp}; q distinct centres, 2 <= q <= {us}")
        print(f"  N5 den(delta) <= u_s = {us};  Xu Prop 7.3 opens the window at 1")
        print(f"  RESIDUAL WINDOW ({len(w)}): " + ", ".join(str(d) for d in w))
