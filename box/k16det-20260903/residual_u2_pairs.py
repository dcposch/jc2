#!/usr/bin/env python3
"""Exact coefficient-pair execution of terminal report (6.4).

For a fixed integer t, elements of Q[d]/(3*d^2-(t+1)) are stored as
(a,b) = a*d+b with Fraction coefficients.  This avoids symbolic quadratic
reductions and exposes the numerator pair and denominator of lambda_2.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Pair:
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    def __add__(self, other: "Pair") -> "Pair":
        return Pair(self.a + other.a, self.b + other.b)

    def __neg__(self) -> "Pair":
        return Pair(-self.a, -self.b)

    def __sub__(self, other: "Pair") -> "Pair":
        return self + (-other)

    def scale(self, scalar: Fraction | int) -> "Pair":
        scalar = Fraction(scalar)
        return Pair(self.a * scalar, self.b * scalar)


class Quad:
    def __init__(self, t: int):
        self.t = t
        self.d2 = Fraction(t + 1, 3)
        self.zero = Pair()
        self.one = Pair(b=Fraction(1))
        self.d = Pair(a=Fraction(1))

    def mul(self, x: Pair, y: Pair) -> Pair:
        return Pair(x.a * y.b + x.b * y.a,
                    x.b * y.b + x.a * y.a * self.d2)

    def inv(self, x: Pair) -> Pair:
        den = x.b * x.b - x.a * x.a * self.d2
        if den == 0:
            raise ZeroDivisionError((self.t, x))
        return Pair(-x.a / den, x.b / den)

    def div(self, x: Pair, y: Pair) -> Pair:
        return self.mul(x, self.inv(y))


def add(x: list[Pair], y: list[Pair], n: int) -> list[Pair]:
    z = Pair()
    return [(x[i] if i < len(x) else z) +
            (y[i] if i < len(y) else z) for i in range(n)]


def scale(x: list[Pair], c: Fraction | int, n: int) -> list[Pair]:
    z = Pair()
    return [(x[i].scale(c) if i < len(x) else z) for i in range(n)]


def qscale(K: Quad, x: list[Pair], c: Pair, n: int) -> list[Pair]:
    z = Pair()
    return [K.mul(x[i], c) if i < len(x) else z for i in range(n)]


def mul(K: Quad, x: list[Pair], y: list[Pair], n: int) -> list[Pair]:
    out = [Pair() for _ in range(n)]
    for i, xi in enumerate(x[:n]):
        if xi == Pair():
            continue
        for j, yj in enumerate(y[:n-i]):
            if yj != Pair():
                out[i+j] = out[i+j] + K.mul(xi, yj)
    return out


def delta(x: list[Pair], degree: int, n: int) -> list[Pair]:
    z = Pair()
    return [(x[i].scale(degree - 2*i) if i < len(x) else z)
            for i in range(n)]


def p_c(K: Quad, j: int) -> Pair:
    t = K.t
    e = 3*t + 1
    ac = (9*j*j*t + 18*j*j - 54*j*t*t - 81*j*t - 26*j
          + 72*t**3 + 144*t*t + 88*t + 16)
    bc = (-9*j*j*t - 10*j*j + 24*j*t*t + 33*j*t + 10*j
          - 12*t**3 - 20*t*t - 8*t)
    scalar = Fraction(3*t*e, (t+1)*(3*t+2)**3*(4*t-2*j+1))
    return Pair(Fraction(ac), Fraction(bc)).scale(scalar)


def p_q(K: Quad, j: int) -> Pair:
    t = K.t
    q, e = 2*t + 1, 3*t + 1
    aq = 12*t*t + 16*t + 4 - j*(3*t+4)
    bq = 2*(t+1)*(j-t)
    scalar = Fraction(-3*t*e*(q-j),
                      (t+1)*q*(3*t+2)**2*(4*t-2*j+1))
    return Pair(Fraction(aq), Fraction(bq)).scale(scalar)


def rho_series(K: Quad, chi: list[Pair], ups: list[Pair], n: int) -> list[Pair]:
    """Return rho[0:n] from (6.4)."""
    t = K.t
    q, e = 2*t + 1, 3*t + 1
    y = Pair(Fraction(1, 2*q), Fraction(t+1, 2*q))
    g = Pair(Fraction(e*t*3, 6*q**3),
             Fraction(e*t*2*(t+1), 6*q**3))

    beta = [Pair() for _ in range(n)]
    for r in range(min((t-1)//2, n-1) + 1):
        numerator = K.mul(g, chi[r]).scale(3*t + 2 - 6*r)
        beta[r] = K.div(numerator, y).scale(Fraction(1, 2*(t-2*r)))

    dqu = delta(ups, q, n)
    dtb = delta(beta, t, n)
    dtc = delta(chi, t, n)
    f = qscale(K, dqu, g.scale(3), n)
    f = add(f, mul(K, chi, beta, n), n)
    f = add(f, scale(mul(K, chi, dtb, n), -1, n), n)
    f = add(f, scale(mul(K, dtc, beta, n), 2, n), n)

    delta_series = [Pair() for _ in range(n)]
    for r in range(n):
        delta_series[r] = K.div(f[r], y).scale(Fraction(1, 4*t-4*r+1))

    term = mul(K, delta(chi, t+1, n), delta_series, n)
    term = add(term,
               scale(mul(K, chi, delta(delta_series, q, n), n), -1, n), n)
    term = add(term, scale(mul(K, dqu, beta, n), 2, n), n)
    xi = qscale(K, term, K.inv(y).scale(Fraction(1, 2)), n)

    return add(mul(K, chi, xi, n),
               scale(mul(K, dqu, delta_series, n), -1, n), n)


def solve_state(t: int, audit: bool = True) -> tuple[Pair, list[Pair], list[Pair]]:
    if t < 2:
        raise ValueError("t must be at least 2")
    K = Quad(t)
    n = t + 2
    chi = [Pair() for _ in range(n)]
    ups = [Pair() for _ in range(n)]
    chi[0] = K.one
    ups[0] = K.one
    ups[1] = K.one

    for r in range(1, (t-1)//2 + 1):
        chi[r] = K.one
        probe1 = rho_series(K, chi, ups, r+1)[r]
        chi[r] = K.zero
        probe0 = rho_series(K, chi, ups, r+1)[r]
        observed = probe1 - probe0
        expected = p_c(K, 2*r)
        if audit and observed != expected:
            raise AssertionError(("p_C", t, r, observed, expected))
        chi[r] = K.div(-probe0, expected)
        if audit and rho_series(K, chi, ups, r+1)[r] != K.zero:
            raise AssertionError(("kill_C", t, r))

    for r in range((t+1)//2, t+1):
        ups[r] = K.one
        probe1 = rho_series(K, chi, ups, r+1)[r]
        ups[r] = K.zero
        probe0 = rho_series(K, chi, ups, r+1)[r]
        observed = probe1 - probe0
        expected = p_q(K, 2*r)
        if audit and observed != expected:
            raise AssertionError(("p_Q", t, r, observed, expected))
        ups[r] = K.div(-probe0, expected)
        if audit and rho_series(K, chi, ups, r+1)[r] != K.zero:
            raise AssertionError(("kill_Q", t, r))

    rho = rho_series(K, chi, ups, n)
    if audit and any(rho[r] != K.zero for r in range(1, t+1)):
        raise AssertionError(("high_rows", t))
    return rho[t+1], chi, ups


def lambda2(t: int, audit: bool = True) -> Pair:
    return solve_state(t, audit)[0]


def encode(t: int, value: Pair) -> dict[str, object]:
    den = math.lcm(value.a.denominator, value.b.denominator)
    aa, bb = int(value.a * den), int(value.b * den)
    common = math.gcd(math.gcd(abs(aa), abs(bb)), den)
    aa, bb, den = aa // common, bb // common, den // common
    norm = 3*bb*bb - (t+1)*aa*aa
    return {
        "t": t,
        "A": aa,
        "B": bb,
        "D": den,
        "norm_numerator": norm,
        "norm_nonzero": norm != 0,
        "digits": max(len(str(abs(aa))), len(str(abs(bb))), len(str(den))),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("t", nargs="+", type=int)
    ap.add_argument("--no-audit", action="store_true")
    args = ap.parse_args()
    results = [encode(t, lambda2(t, not args.no_audit)) for t in args.t]
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
