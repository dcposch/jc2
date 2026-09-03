#!/usr/bin/env python3
"""Execute charged (6.4) in coefficient pairs for fixed integer t.

Every element is stored as (b,a) = b+a*d in
Q[d]/(3*d**2-(t+1)).  This driver uses only the formulas reproduced in the
frozen k16-terminal-proof report; it does not import an in-progress emitter.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from math import ceil, floor


Pair = tuple[F, F]


class Quad:
    def __init__(self, t: int):
        self.t = t
        self.c = F(t + 1, 3)  # d^2=c
        self.zero: Pair = (F(0), F(0))
        self.one: Pair = (F(1), F(0))

    def q(self, b=0, a=0) -> Pair:
        return (F(b), F(a))

    def add(self, x: Pair, y: Pair) -> Pair:
        return (x[0] + y[0], x[1] + y[1])

    def neg(self, x: Pair) -> Pair:
        return (-x[0], -x[1])

    def sub(self, x: Pair, y: Pair) -> Pair:
        return (x[0] - y[0], x[1] - y[1])

    def mul(self, x: Pair, y: Pair) -> Pair:
        return (x[0] * y[0] + self.c * x[1] * y[1],
                x[0] * y[1] + x[1] * y[0])

    def scale(self, x: Pair, c) -> Pair:
        c = F(c)
        return (c * x[0], c * x[1])

    def inv(self, x: Pair) -> Pair:
        den = x[0] * x[0] - self.c * x[1] * x[1]
        if not den:
            raise ZeroDivisionError(f"nonunit pair at t={self.t}: {x}")
        return (x[0] / den, -x[1] / den)

    def div(self, x: Pair, y: Pair) -> Pair:
        return self.mul(x, self.inv(y))

    def norm3(self, x: Pair) -> F:
        """3*b^2-(t+1)*a^2, the primitive norm used in the report."""
        return 3 * x[0] * x[0] - (self.t + 1) * x[1] * x[1]


def sadd(K: Quad, x: list[Pair], y: list[Pair], n: int) -> list[Pair]:
    return [K.add(x[i] if i < len(x) else K.zero,
                  y[i] if i < len(y) else K.zero) for i in range(n + 1)]


def sscale(K: Quad, x: list[Pair], c: Pair, n: int) -> list[Pair]:
    return [K.mul(c, x[i] if i < len(x) else K.zero) for i in range(n + 1)]


def smul(K: Quad, x: list[Pair], y: list[Pair], n: int) -> list[Pair]:
    out = [K.zero for _ in range(n + 1)]
    for i in range(min(len(x), n + 1)):
        if x[i] == K.zero:
            continue
        for j in range(min(len(y), n + 1 - i)):
            if y[j] != K.zero:
                out[i + j] = K.add(out[i + j], K.mul(x[i], y[j]))
    return out


def Delta(K: Quad, index: int, x: list[Pair], n: int) -> list[Pair]:
    return [K.scale(x[r] if r < len(x) else K.zero, index - 2 * r)
            for r in range(n + 1)]


def pivot_pair(K: Quad, weight: int) -> Pair:
    t = K.t
    q, e, j = 2 * t + 1, 3 * t + 1, weight
    if 1 <= j < t:
        ac = (9*j*j*t + 18*j*j - 54*j*t*t - 81*j*t - 26*j
              + 72*t**3 + 144*t*t + 88*t + 16)
        bc = (-9*j*j*t - 10*j*j + 24*j*t*t + 33*j*t + 10*j
              - 12*t**3 - 20*t*t - 8*t)
        pref = F(3*t*e, (t+1)*(3*t+2)**3*(4*t-2*j+1))
        return K.q(pref * bc, pref * ac)
    if t <= j <= 2*t:
        aq = 12*t*t + 16*t + 4 - j*(3*t+4)
        bq = 2*(t+1)*(j-t)
        pref = F(-3*t*e*(q-j), (t+1)*q*(3*t+2)**2*(4*t-2*j+1))
        return K.q(pref * bq, pref * aq)
    raise ValueError(weight)


def rho_series(K: Quad, chi: list[Pair], ups: list[Pair], n: int) -> list[Pair]:
    t = K.t
    q, e = 2*t+1, 3*t+1
    y = K.q(F(t+1, 2*q), F(1, 2*q))
    g = K.q(F(e*t*2*(t+1), 6*q**3), F(e*t*3, 6*q**3))
    iy = K.inv(y)

    beta = [K.zero for _ in range(n + 1)]
    for r in range(min(floor((t-1)/2), n) + 1):
        scalar = F(3*t+2-6*r, 2*(t-2*r))
        beta[r] = K.scale(K.mul(K.mul(g, iy), chi[r]), scalar)

    du = Delta(K, q, ups, n)
    db = Delta(K, t, beta, n)
    dc = Delta(K, t, chi, n)
    f = sscale(K, du, K.scale(g, 3), n)
    f = sadd(K, f, smul(K, chi, beta, n), n)
    f = sadd(K, f, sscale(K, smul(K, chi, db, n), K.q(-1), n), n)
    f = sadd(K, f, sscale(K, smul(K, dc, beta, n), K.q(2), n), n)

    delta = [K.zero for _ in range(n + 1)]
    for r in range(min(t, n) + 1):
        delta[r] = K.scale(K.mul(f[r], iy), F(1, 4*t-4*r+1))

    dc1 = Delta(K, t+1, chi, n)
    ddq = Delta(K, q, delta, n)
    xinum = smul(K, dc1, delta, n)
    xinum = sadd(K, xinum, sscale(K, smul(K, chi, ddq, n), K.q(-1), n), n)
    xinum = sadd(K, xinum, sscale(K, smul(K, du, beta, n), K.q(2), n), n)
    xi = sscale(K, xinum, K.scale(iy, F(1, 2)), n)
    rho = smul(K, chi, xi, n)
    rho = sadd(K, rho, sscale(K, smul(K, du, delta, n), K.q(-1), n), n)
    return rho


def solve(t: int, verify_pivots: bool = True) -> dict:
    if t < 3:
        raise ValueError("the u2 residual axis exists only for t>=3")
    K = Quad(t)
    n = t + 1
    chi = [K.zero for _ in range(n + 1)]
    ups = [K.zero for _ in range(n + 1)]
    chi[0] = K.one
    ups[0] = ups[1] = K.one
    trace = []

    schedule = [("chi", r, 2*r) for r in range(1, floor((t-1)/2)+1)]
    schedule += [("upsilon", r, 2*r) for r in range(ceil(t/2), t+1)]
    for family, r, weight in schedule:
        target = chi if family == "chi" else ups
        target[r] = K.zero
        rho0 = rho_series(K, chi, ups, n)[r]
        pivot = pivot_pair(K, weight)
        if verify_pivots:
            target[r] = K.one
            rho1 = rho_series(K, chi, ups, n)[r]
            measured = K.sub(rho1, rho0)
            if measured != pivot:
                raise AssertionError((t, family, r, measured, pivot))
        value = K.neg(K.div(rho0, pivot))
        target[r] = value
        if verify_pivots:
            killed = rho_series(K, chi, ups, n)[r]
            if killed != K.zero:
                raise AssertionError((t, family, r, killed))
        trace.append({"family": family, "r": r, "weight": weight,
                      "value": pair_json(value), "pivot": pair_json(pivot)})

    rho = rho_series(K, chi, ups, n)
    if any(rho[r] != K.zero for r in range(1, t+1)):
        raise AssertionError((t, "uncancelled", [pair_json(x) for x in rho]))
    lam = rho[t+1]
    return {
        "t": t,
        "relation": f"3*d^2-{t+1}",
        "lambda_pair_b_plus_a_d": pair_json(lam),
        "norm3": frac_json(K.norm3(lam)),
        "chi": [pair_json(x) for x in chi],
        "upsilon": [pair_json(x) for x in ups],
        "trace": trace,
        "checks": {"pivots_match_2_10_2_11": verify_pivots,
                   "rho_1_through_t_zero": True},
    }


def frac_json(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def pair_json(x: Pair) -> dict[str, str]:
    return {"b": frac_json(x[0]), "a": frac_json(x[1])}


def direct_terminal_check(t: int, solved: dict) -> dict:
    """Reconstruct (2.3)--(2.7) at b3=b4=0 and compare (6.5).

    This is deliberately independent of the h/s compression used by
    ``rho_series``.  Coefficients in X are polynomials in z=u_2 whose scalar
    coefficients are quadratic pairs.
    """
    K = Quad(t)
    q = 2*t + 1
    maxz = t + 1

    def unpair(obj: dict[str, str]) -> Pair:
        return (F(obj["b"]), F(obj["a"]))

    def pzero() -> list[Pair]:
        return [K.zero for _ in range(maxz + 1)]

    def padd(a: list[Pair], b: list[Pair]) -> list[Pair]:
        return [K.add(a[i], b[i]) for i in range(maxz + 1)]

    def pscale(a: list[Pair], c: Pair) -> list[Pair]:
        return [K.mul(c, x) for x in a]

    def pmul(a: list[Pair], b: list[Pair]) -> list[Pair]:
        out = pzero()
        for i, x in enumerate(a):
            if x == K.zero:
                continue
            for j, y0 in enumerate(b[:maxz+1-i]):
                if y0 != K.zero:
                    out[i+j] = K.add(out[i+j], K.mul(x, y0))
        return out

    def mono(r: int, c: Pair) -> list[Pair]:
        out = pzero()
        out[r] = c
        return out

    maxx = 4*t + 2
    zero_x = lambda: [pzero() for _ in range(maxx + 1)]

    chi = [unpair(x) for x in solved["chi"]]
    ups = [unpair(x) for x in solved["upsilon"]]
    C, U = zero_x(), zero_x()
    for r, c0 in enumerate(chi):
        exponent = t-1-2*r
        if exponent >= 0 and c0 != K.zero:
            C[exponent] = padd(C[exponent], mono(r, c0))
    for r, u0 in enumerate(ups):
        exponent = q-2*r
        if exponent >= 0 and u0 != K.zero:
            U[exponent] = padd(U[exponent], mono(r, u0))

    y = K.q(F(t+1, 2*q), F(1, 2*q))
    g = K.q(F((3*t+1)*t*2*(t+1), 6*q**3),
            F((3*t+1)*t*3, 6*q**3))
    iy = K.inv(y)
    B, S = zero_x(), zero_x()
    for m in range(t):
        scalar = F(3*m+5, 2*(m+1))
        B[m+1] = pscale(C[m], K.scale(K.mul(g, iy), scalar))
    for m in range(2*t+1):
        acc = pscale(U[m+1], K.scale(g, 3*(m+1)))
        for a in range(maxx+1):
            b = m-1-a
            if 0 <= b <= maxx:
                acc = padd(acc, pscale(pmul(C[a], B[b]), K.q(3+2*a-b)))
        S[m] = pscale(acc, K.scale(iy, F(1, 2*m+1)))

    V, Y, Z = zero_x(), zero_x(), zero_x()
    for m in range(maxx+1):
        if m >= 2:
            V[m] = C[m-2]
        if m >= 1:
            Y[m] = S[m-1]
            Z[m] = B[m-1]

    N, P0, R = zero_x(), zero_x(), zero_x()
    for m in range(maxx+1):
        acc = pzero()
        for a in range(m+1):
            b = m-a
            if b+1 <= maxx:
                acc = padd(acc, pscale(pmul(V[a], Y[b+1]), K.q(-(b+1))))
            if a+1 <= maxx:
                acc = padd(acc, pscale(pmul(V[a+1], Y[b]), K.q(a+1)))
                acc = padd(acc, pscale(pmul(U[a+1], Z[b]), K.q(2*(a+1))))
        N[m] = acc
    for r in range(maxx):
        P0[r] = pscale(N[r+1], K.scale(iy, F(1, 2)))
    for m in range(maxx+1):
        acc = pzero()
        for a in range(m+1):
            b = m-a
            acc = padd(acc, pmul(V[a], P0[b]))
            if a+1 <= maxx:
                acc = padd(acc, pscale(pmul(U[a+1], Y[b]), K.q(-(a+1))))
        R[m] = acc

    lam = unpair(solved["lambda_pair_b_plus_a_d"])
    expected = mono(t+1, lam)
    if R[2*t-1] != expected:
        raise AssertionError((t, "direct lambda", R[2*t-1], expected))
    for m in range(2*t, 4*t+2):
        if R[m] != pzero():
            raise AssertionError((t, "direct high band", m, R[m]))
    return {"direct_2_3_through_2_7": True,
            "high_X_bands_2t_through_4t_plus_1_zero": True,
            "X_2t_minus_1_equals_lambda_z_t_plus_1": True}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("t", type=int, nargs="+", help="fixed integers, each >=3")
    args = ap.parse_args()
    out = []
    for t in args.t:
        ans = solve(t)
        ans["direct_check"] = direct_terminal_check(t, ans)
        out.append(ans)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
