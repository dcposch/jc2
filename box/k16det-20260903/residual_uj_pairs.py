#!/usr/bin/env python3
"""Fixed-(t,j) coefficient-pair probe for the b4=b3=0, u_j axis.

This generalizes terminal report (6.4) by replacing Delta_n=n-2*Theta
with Delta_n=n-j*Theta.  It is deliberately typed as an axis probe, not an
ideal-membership certificate.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction

from residual_u2_pairs import Pair, Quad, add, scale, qscale, mul, p_c, p_q


def op_delta(x: list[Pair], degree: int, j: int, n: int) -> list[Pair]:
    z = Pair()
    return [(x[i].scale(degree-j*i) if i < len(x) else z) for i in range(n)]


def p_b2(K: Quad) -> Pair:
    t = K.t
    q, e = 2*t+1, 3*t+1
    return Pair(Fraction(3*q), Fraction(t+1)).scale(
        Fraction(t*e, 6*q*q*(3*t+2)))


def rho_series(K: Quad, j: int, chi: list[Pair], ups: list[Pair],
               b2: list[Pair], n: int) -> list[Pair]:
    t = K.t
    q, e = 2*t+1, 3*t+1
    y = Pair(Fraction(1, 2*q), Fraction(t+1, 2*q))
    g = Pair(Fraction(e*t*3, 6*q**3),
             Fraction(e*t*2*(t+1), 6*q**3))

    beta = [Pair() for _ in range(n)]
    for r in range(min((t-1)//j, n-1)+1):
        numerator = K.mul(g, chi[r]).scale(3*t+2-3*j*r)
        beta[r] = K.div(numerator, y).scale(Fraction(1, 2*(t-j*r)))

    dqu = op_delta(ups, q, j, n)
    dtb = op_delta(beta, t, j, n)
    dtc = op_delta(chi, t, j, n)
    f = qscale(K, dqu, g.scale(3), n)
    f = add(f, mul(K, chi, beta, n), n)
    f = add(f, scale(mul(K, chi, dtb, n), -1, n), n)
    f = add(f, scale(mul(K, dtc, beta, n), 2, n), n)

    ds = [Pair() for _ in range(n)]
    for r in range(n):
        ds[r] = K.div(f[r], y).scale(Fraction(1, 4*t-2*j*r+1))

    # Y=h^q*eta, eta=delta-g*b2_series.
    eta = add(ds, scale(qscale(K, b2, g, n), -1, n), n)
    term = mul(K, op_delta(chi, t+1, j, n), eta, n)
    term = add(term,
               scale(mul(K, chi, op_delta(eta, q, j, n), n), -1, n), n)
    term = add(term, scale(mul(K, dqu, beta, n), 2, n), n)
    xi = qscale(K, term, K.inv(y).scale(Fraction(1, 2)), n)
    return add(mul(K, chi, xi, n),
               scale(mul(K, dqu, eta, n), -1, n), n)


def solve(t: int, j: int, audit: bool = True) -> tuple[Pair, int]:
    if not 2 <= j < t:
        raise ValueError("require 2 <= j < t")
    K = Quad(t)
    r_first = (2*t+1)//j + 1
    n = r_first+1
    chi = [Pair() for _ in range(n)]
    ups = [Pair() for _ in range(n)]
    b2 = [Pair() for _ in range(n)]
    chi[0] = K.one
    ups[0] = K.one
    ups[1] = K.one

    for r in range(1, (t-1)//j+1):
        chi[r] = K.one
        one = rho_series(K,j,chi,ups,b2,r+1)[r]
        chi[r] = K.zero
        zero = rho_series(K,j,chi,ups,b2,r+1)[r]
        expected = p_c(K,j*r)
        if audit and one-zero != expected:
            raise AssertionError(("p_C",t,j,r,one-zero,expected))
        chi[r] = K.div(-zero,expected)

    for r in range((t+j-1)//j, (2*t)//j+1):
        ups[r] = K.one
        one = rho_series(K,j,chi,ups,b2,r+1)[r]
        ups[r] = K.zero
        zero = rho_series(K,j,chi,ups,b2,r+1)[r]
        expected = p_q(K,j*r)
        if audit and one-zero != expected:
            raise AssertionError(("p_Q",t,j,r,one-zero,expected))
        ups[r] = K.div(-zero,expected)

    q = 2*t+1
    if q % j == 0:
        r=q//j
        b2[r]=K.one
        one=rho_series(K,j,chi,ups,b2,r+1)[r]
        b2[r]=K.zero
        zero=rho_series(K,j,chi,ups,b2,r+1)[r]
        expected=p_b2(K)
        if audit and one-zero != expected:
            raise AssertionError(("p_b2",t,j,r,one-zero,expected))
        b2[r]=K.div(-zero,expected)

    rho=rho_series(K,j,chi,ups,b2,n)
    if audit and any(rho[r] != K.zero for r in range(1,r_first)):
        raise AssertionError(("high_rows",t,j))
    return rho[r_first],r_first


def encode(t: int,j: int,value: Pair,r: int) -> dict[str,object]:
    den=math.lcm(value.a.denominator,value.b.denominator)
    aa,bb=int(value.a*den),int(value.b*den)
    common=math.gcd(math.gcd(abs(aa),abs(bb)),den)
    aa,bb,den=aa//common,bb//common,den//common
    norm=3*bb*bb-(t+1)*aa*aa
    return {"t":t,"j":j,"power":r,"band":4*t+1-j*r,
            "A":aa,"B":bb,"D":den,"norm_numerator":norm,
            "norm_nonzero":norm != 0}


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("t",type=int)
    ap.add_argument("--j",nargs="*",type=int)
    args=ap.parse_args()
    js=args.j or list(range(2,args.t))
    out=[]
    for j in js:
        value,r=solve(args.t,j)
        out.append(encode(args.t,j,value,r))
    print(json.dumps(out,indent=2))


if __name__=="__main__":
    main()
