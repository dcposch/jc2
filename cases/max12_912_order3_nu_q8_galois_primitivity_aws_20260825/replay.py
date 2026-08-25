#!/usr/bin/env python3
"""Exact finite-field certificates for primitivity of the Q8 Galois action."""

from __future__ import annotations

import json
from math import gcd, isqrt


# Coefficients low-to-high.  This is the corrected Q8 from the reviewed
# genuine-x1 determinant, with sign normalized to positive leading term.
Q8_Z = [-24, -296, -1548, -4428, -7320, -6498, -1782, 1539, 999]


def trim(f):
    f = list(f)
    while len(f) > 1 and f[-1] == 0:
        f.pop()
    return f


def monic(f, p):
    f = trim([a % p for a in f])
    if f == [0]:
        return f
    inv = pow(f[-1], -1, p)
    return trim([(a * inv) % p for a in f])


def add(f, g, p):
    n = max(len(f), len(g))
    return trim([((f[i] if i < len(f) else 0) +
                  (g[i] if i < len(g) else 0)) % p for i in range(n)])


def sub(f, g, p):
    n = max(len(f), len(g))
    return trim([((f[i] if i < len(f) else 0) -
                  (g[i] if i < len(g) else 0)) % p for i in range(n)])


def mul(f, g, p):
    out = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            out[i + j] = (out[i + j] + a * b) % p
    return trim(out)


def divmod_poly(f, g, p):
    f = trim([a % p for a in f])
    g = trim([a % p for a in g])
    if g == [0]:
        raise ZeroDivisionError
    if len(f) < len(g):
        return [0], f
    q = [0] * (len(f) - len(g) + 1)
    inv = pow(g[-1], -1, p)
    while f != [0] and len(f) >= len(g):
        shift = len(f) - len(g)
        coeff = f[-1] * inv % p
        q[shift] = coeff
        for i, value in enumerate(g):
            f[i + shift] = (f[i + shift] - coeff * value) % p
        f = trim(f)
    return trim(q), f


def mod_poly(f, modulus, p):
    return divmod_poly(f, modulus, p)[1]


def gcd_poly(f, g, p):
    f = trim([a % p for a in f])
    g = trim([a % p for a in g])
    while g != [0]:
        _, r = divmod_poly(f, g, p)
        f, g = g, r
    return monic(f, p)


def powmod_poly(base, exponent, modulus, p):
    out = [1]
    base = mod_poly(base, modulus, p)
    while exponent:
        if exponent & 1:
            out = mod_poly(mul(out, base, p), modulus, p)
        base = mod_poly(mul(base, base, p), modulus, p)
        exponent >>= 1
    return out


def derivative(f, p):
    if len(f) <= 1:
        return [0]
    return trim([(i * f[i]) % p for i in range(1, len(f))])


def primes(limit):
    out = []
    for n in range(2, limit + 1):
        if all(n % q for q in out if q <= isqrt(n)):
            out.append(n)
    return out


def irreducible_certificate(f, p):
    """Rabin irreducibility criterion, returning all exact residues."""
    f = monic(f, p)
    n = len(f) - 1
    prime_divisors = [q for q in primes(n) if n % q == 0]
    x = [0, 1]
    checks = []
    for q in prime_divisors:
        xp = powmod_poly(x, p ** (n // q), f, p)
        g = gcd_poly(f, sub(xp, x, p), p)
        checks.append({"q": q, "gcd": g})
        if g != [1]:
            return False, checks, None
    final = sub(powmod_poly(x, p ** n, f, p), x, p)
    final = mod_poly(final, f, p)
    return final == [0], checks, final


def pattern_8(p):
    if Q8_Z[-1] % p == 0:
        return None
    f = monic(Q8_Z, p)
    if gcd_poly(f, derivative(f, p), p) != [1]:
        return None
    ok, checks, final = irreducible_certificate(f, p)
    if not ok:
        return None
    return {"prime": p, "monic_q8": f, "checks": checks,
            "final_residue": final, "factor_degrees": [8]}


def pattern_1_7(p):
    if Q8_Z[-1] % p == 0:
        return None
    f = monic(Q8_Z, p)
    if gcd_poly(f, derivative(f, p), p) != [1]:
        return None
    roots = [a for a in range(p) if mod_poly(f, [(-a) % p, 1], p) == [0]]
    if len(roots) != 1:
        return None
    linear = [(-roots[0]) % p, 1]
    quotient, remainder = divmod_poly(f, linear, p)
    if remainder != [0] or len(quotient) - 1 != 7:
        raise AssertionError((p, roots, remainder, quotient))
    ok, checks, final = irreducible_certificate(quotient, p)
    if not ok:
        return None
    if monic(mul(linear, quotient, p), p) != f:
        raise AssertionError("factor reconstruction failed")
    return {"prime": p, "monic_q8": f, "linear_root": roots[0],
            "degree7_factor": quotient, "checks": checks,
            "final_residue": final, "factor_degrees": [1, 7]}


def main():
    content = 0
    for coefficient in Q8_Z:
        content = gcd(content, abs(coefficient))
    if content != 1:
        raise AssertionError(("Q8 is not primitive over Z", content))
    cert8 = None
    cert17 = None
    for p in primes(1000):
        if cert8 is None:
            cert8 = pattern_8(p)
        if cert17 is None:
            cert17 = pattern_1_7(p)
        if cert8 is not None and cert17 is not None:
            break
    if cert8 is None or cert17 is None:
        raise RuntimeError("required Frobenius patterns not found below 1000")
    payload = {
        "case": "max12_912_order3_nu_q8_galois_primitivity_aws_20260825",
        "q8_coefficients_low_to_high": Q8_Z,
        "q8_integer_content": content,
        "certificate_8_cycle": cert8,
        "certificate_7_cycle": cert17,
        "deduction": {
            "irreducible_over_Q": True,
            "galois_action_transitive": True,
            "contains_7_cycle": True,
            "primitive": True,
            "imprimitive_block_sizes_to_exclude": [2, 4],
            "block_wreath_orders": {"2_by_4": 384, "4_by_2": 1152},
            "seven_divides_either_wreath_order": False,
            "component_partition_options": [[8], [1, 1, 1, 1, 1, 1, 1, 1]],
        },
        "scope": (
            "exact Q8 Galois-primitivity and component-partition reducer only; "
            "does not choose between one eight-contact component and eight "
            "one-contact conjugate components"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
