#!/usr/bin/env python3
"""Deterministic Rabin certificate for a good irreducible Q8 reduction."""

from __future__ import annotations

import json


# Report sign: leading coefficient +999, constant -24, ascending order.
Q8 = [-24, -296, -1548, -4428, -7320, -6498, -1782, 1539, 999]


def trim(a, p):
    a = [x % p for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def divmod_poly(a, b, p):
    a = trim(a, p)
    b = trim(b, p)
    if b == [0]:
        raise ZeroDivisionError
    q = [0] * max(1, len(a) - len(b) + 1)
    inv = pow(b[-1], p - 2, p)
    while a != [0] and len(a) >= len(b):
        degree = len(a) - len(b)
        scalar = a[-1] * inv % p
        q[degree] = scalar
        for i, value in enumerate(b):
            a[i + degree] = (a[i + degree] - scalar * value) % p
        a = trim(a, p)
    return trim(q, p), a


def gcd_poly(a, b, p):
    a, b = trim(a, p), trim(b, p)
    while b != [0]:
        _, r = divmod_poly(a, b, p)
        a, b = b, r
    inv = pow(a[-1], p - 2, p)
    return trim([inv * x for x in a], p)


def mulmod(a, b, modulus, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = (out[i + j] + x * y) % p
    return divmod_poly(out, modulus, p)[1]


def powmod(a, exponent, modulus, p):
    out = [1]
    base = divmod_poly(a, modulus, p)[1]
    while exponent:
        if exponent & 1:
            out = mulmod(out, base, modulus, p)
        base = mulmod(base, base, modulus, p)
        exponent >>= 1
    return trim(out, p)


def primes(limit):
    out = []
    for n in range(2, limit + 1):
        if all(n % q for q in out if q * q <= n):
            out.append(n)
    return out


def certificate(p):
    f = trim(Q8, p)
    if len(f) != 9:
        return None
    inv = pow(f[-1], p - 2, p)
    f = trim([inv * x for x in f], p)
    x = [0, 1]
    xp4 = powmod(x, p ** 4, f, p)
    delta4 = xp4[:]
    if len(delta4) < 2:
        delta4 += [0] * (2 - len(delta4))
    delta4[1] = (delta4[1] - 1) % p
    delta4 = trim(delta4, p)
    g = gcd_poly(f, delta4, p)
    xp8 = powmod(x, p ** 8, f, p)
    delta8 = xp8[:]
    if len(delta8) < 2:
        delta8 += [0] * (2 - len(delta8))
    delta8[1] = (delta8[1] - 1) % p
    delta8 = trim(delta8, p)
    return {
        "prime": p,
        "monic_q8_ascending": f,
        "gcd_p4_ascending": g,
        "xp8_minus_x_remainder_ascending": delta8,
        "irreducible": g == [1] and delta8 == [0],
    }


def main():
    tests = []
    for p in primes(1000):
        if p < 5:
            continue
        row = certificate(p)
        if row is not None:
            tests.append(row)
            if row["irreducible"]:
                payload = {
                    "status": "PASS",
                    "criterion": "Rabin degree 8; only prime divisor of 8 is 2",
                    "least_good_prime": p,
                    "tested_primes": len(tests),
                    "certificate": row,
                }
                print(json.dumps(payload, indent=2, sort_keys=True))
                print("Q8_IRREDUCIBLE_PRIME_SEARCH_PASS")
                return
    raise RuntimeError("no irreducible reduction through 1000")


if __name__ == "__main__":
    main()
