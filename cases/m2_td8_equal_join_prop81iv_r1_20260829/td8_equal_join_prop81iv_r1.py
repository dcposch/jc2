#!/usr/bin/env python3
"""Exact Prop. 8.1(iv) certificate for the td=8 equal-join affine family.

For t >= 0 put nu = 4+3t and x = eta.  The reduced patterns

    p = (x^(2*nu) + 1)^3,
    q = x * (x^(2*nu) + 1)

have the charged degrees, two nu-orbits of p-roots of multiplicity three,
and the forced simple eta-root of q.  With delta=X=4*nu and
one_minus_u=kbar=2*(2*nu+1)/3, the printed identity is

    delta*p*q' - one_minus_u*p'*q = delta*p.

All arithmetic below is sparse and exact over Q.  This is a local formal
pattern certificate only; it does not claim exact lambda, landing, or
geometric realizability.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import gcd


Poly = dict[int, Fraction]


def _clean(p: Poly) -> Poly:
    return {e: c for e, c in p.items() if c}


def add(a: Poly, b: Poly) -> Poly:
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, Fraction(0)) + c
    return _clean(out)


def scale(a: Poly, c: int | Fraction) -> Poly:
    c = Fraction(c)
    return _clean({e: c * v for e, v in a.items()})


def mul(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            out[ea + eb] = out.get(ea + eb, Fraction(0)) + ca * cb
    return _clean(out)


def power(a: Poly, n: int) -> Poly:
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("power must be a nonnegative integer")
    out: Poly = {0: Fraction(1)}
    base = a
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n //= 2
    return out


def deriv(a: Poly) -> Poly:
    return _clean({e - 1: e * c for e, c in a.items() if e})


def degree(a: Poly) -> int:
    if not a:
        raise ValueError("zero polynomial has no degree")
    return max(a)


def patterns(nu: int) -> tuple[Poly, Poly]:
    if isinstance(nu, bool) or not isinstance(nu, int) or nu < 1:
        raise ValueError("nu must be a positive integer")
    # (1+x^(2nu))^3 and x(1+x^(2nu)).
    p = {0: Fraction(1), 2 * nu: Fraction(3),
         4 * nu: Fraction(3), 6 * nu: Fraction(1)}
    q = {1: Fraction(1), 2 * nu + 1: Fraction(1)}
    return p, q


def orbit_factor(nu: int, root: int | Fraction) -> Poly:
    return {0: -Fraction(root), nu: Fraction(1)}


def two_orbit_patterns(nu: int, root_a: int | Fraction,
                       root_b: int | Fraction, mult_a: int,
                       mult_b: int) -> tuple[Poly, Poly]:
    if Fraction(root_a) == 0 or Fraction(root_b) == 0 or root_a == root_b:
        raise ValueError("orbit roots must be distinct and nonzero")
    fa, fb = orbit_factor(nu, root_a), orbit_factor(nu, root_b)
    p = mul(power(fa, mult_a), power(fb, mult_b))
    q = mul({1: Fraction(1)}, mul(fa, fb))
    return p, q


def two_orbit_residual(nu: int, root_a: int | Fraction,
                       root_b: int | Fraction, mult_a: int, mult_b: int,
                       delta: int, one_minus_u: int,
                       rhs_constant: int | Fraction) -> Poly:
    p, q = two_orbit_patterns(nu, root_a, root_b, mult_a, mult_b)
    lhs = add(scale(mul(p, deriv(q)), delta),
              scale(mul(deriv(p), q), -one_minus_u))
    return add(lhs, scale(p, -rhs_constant))


def fixed_route_certificates() -> dict[str, object]:
    """The two fixed local consumers surrounding the affine merge."""
    incoming = {
        "nu": 7, "roots_T": [2, 3], "multiplicities": [2, 1],
        "delta_equals_X": 7, "one_minus_u_equals_kbar": 5,
        "rhs_constant": 42, "degrees": [21, 15], "M": 3,
    }
    trunk = {
        "nu": 17, "roots_T": [3, 4], "multiplicities": [3, 2],
        "delta_equals_X": 17, "one_minus_u_equals_kbar": 7,
        "rhs_constant": 204, "degrees": [85, 35], "M": 5,
    }
    for name, item in (("incoming_21_15", incoming), ("trunk_85_35", trunk)):
        p, q = two_orbit_patterns(item["nu"], *item["roots_T"],
                                  *item["multiplicities"])
        residual = two_orbit_residual(
            item["nu"], *item["roots_T"], *item["multiplicities"],
            item["delta_equals_X"], item["one_minus_u_equals_kbar"],
            item["rhs_constant"])
        if residual:
            raise ValueError(name + " Prop. 8.1(iv) residual is nonzero")
        if [degree(p), degree(q)] != item["degrees"]:
            raise ValueError(name + " degree mismatch")
        if gcd(degree(p), degree(q)) != item["M"]:
            raise ValueError(name + " M mismatch")
        item["identity_ok"] = True
    return {"each_incoming_21_15": incoming, "trunk_85_35": trunk}


def identity_residual(nu: int, *, delta: int | None = None,
                      one_minus_u: int | None = None) -> Poly:
    p, q = patterns(nu)
    delta = 4 * nu if delta is None else delta
    if one_minus_u is None:
        if (2 * (2 * nu + 1)) % 3:
            raise ValueError("one_minus_u is nonintegral off nu=1 mod 3")
        one_minus_u = 2 * (2 * nu + 1) // 3
    lhs = add(scale(mul(p, deriv(q)), delta),
              scale(mul(deriv(p), q), -one_minus_u))
    return add(lhs, scale(p, -delta))


def certificate(t: int) -> dict[str, object]:
    if isinstance(t, bool) or not isinstance(t, int) or t < 0:
        raise ValueError("t must be a nonnegative integer")
    nu = 4 + 3 * t
    delta = 4 * nu
    one_minus_u = 2 * (2 * nu + 1) // 3
    p, q = patterns(nu)
    dp, dq = degree(p), degree(q)
    M = gcd(dp, dq)
    residual = identity_residual(nu)

    checks = {
        "affine_nu": nu == 4 + 3 * t,
        "affine_degrees": (dp, dq) == (24 + 18 * t, 9 + 6 * t),
        "affine_frame": (M, one_minus_u, delta) ==
                        (3, 6 + 4 * t, 16 + 12 * t),
        "top_ratio": Fraction(delta, one_minus_u) == Fraction(dp, dq),
        "prop81iv": residual == {},
        "rhs_nonzero": delta != 0,
        "two_nonzero_nu_orbits": nu >= 2,
        "p_root_multiplicity": 3 * dq > dp and dp != 3 * dq,
        "eta_simple_q_only": p.get(0) == 1 and q.get(1) == 1,
        "gcd_M": M == 3,
        "frame_rho": Fraction(delta, dp) == Fraction(2, 3),
        "frame_w": Fraction(one_minus_u, nu) - Fraction(2, 3 * nu)
                   == Fraction(4, 3),
        "fixed_route_consumers": all(
            x["identity_ok"] for x in fixed_route_certificates().values()),
    }
    if not all(checks.values()):
        bad = sorted(k for k, v in checks.items() if not v)
        raise ValueError("certificate check failed: " + ",".join(bad))

    return {
        "schema": "m2-td8-equal-join-prop81iv-r1",
        "t": t,
        "nu": nu,
        "degrees": {"p": dp, "q": dq, "M": M},
        "frame": {
            "delta_equals_X": delta,
            "one_minus_u_equals_kbar": one_minus_u,
            "rho_book": "2/3",
            "w": "4/3",
        },
        "patterns": {
            "p": "(eta^(2*nu)+1)^3",
            "q": "eta*(eta^(2*nu)+1)",
            "p_orbits": 2,
            "arrival_multiplicity_each": 3,
            "q_common_root_multiplicity": 1,
            "q_forced_eta_multiplicity": 1,
        },
        "identity": "delta*p*q'-(1-u)*p'*q=delta*p",
        "rhs_constant": delta,
        "fixed_route_consumers": fixed_route_certificates(),
        "checks": checks,
        "claim_firewall": {
            "local_formal_prop81iv_survival": True,
            "exact_lambda": False,
            "source_landing": False,
            "geometric_realizability": False,
            "degree_ceiling": False,
            "jc2": False,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--t", type=int, default=0)
    parser.add_argument("--scan", type=int, default=0,
                        help="also certify t=0..N inclusive")
    args = parser.parse_args()
    if args.scan < 0:
        raise SystemExit("--scan must be nonnegative")
    certs = [certificate(t) for t in range(args.scan + 1)] if args.scan else [certificate(args.t)]
    print(json.dumps({"certificates": certs}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
