#!/usr/bin/env python3
"""Independent exact homogeneous-centralizer check for K=x*y*(x-y)."""

from fractions import Fraction
import hashlib
import json


def bracket(a, b):
    da = len(a) - 1
    db = len(b) - 1
    out = [Fraction(0) for _ in range(da + db - 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            e = i + j - 1
            factor = i * db - da * j
            # The two formal endpoint exponents outside the homogeneous
            # degree range always have zero derivative factor.
            if factor and 0 <= e < len(out):
                out[e] += ai * bj * factor
    return out


def rank(matrix):
    m = [[Fraction(x) for x in row] for row in matrix]
    rows = len(m)
    cols = len(m[0]) if rows else 0
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        u = m[r][c]
        m[r] = [x / u for x in m[r]]
        for i in range(rows):
            if i != r and m[i][c]:
                q = m[i][c]
                m[i] = [x - q * y for x, y in zip(m[i], m[r])]
        r += 1
    return r


def multiply(a, b):
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def power(a, n):
    out = [Fraction(1)]
    for _ in range(n):
        out = multiply(out, a)
    return out


def main():
    # Coefficient index i means x^i*y^(d-i).
    K = [Fraction(0), Fraction(-1), Fraction(1), Fraction(0)]
    rows = []
    for d in range(19):
        columns = []
        for i in range(d + 1):
            basis = [Fraction(0) for _ in range(d + 1)]
            basis[i] = Fraction(1)
            columns.append(bracket(K, basis))
        matrix = [list(row) for row in zip(*columns)]
        r = rank(matrix)
        kernel = d + 1 - r
        expected = 1 if d % 3 == 0 else 0
        assert kernel == expected, (d, r, kernel, expected)
        if expected:
            kd = power(K, d // 3)
            assert all(x == 0 for x in bracket(K, kd))
        rows.append({"degree": d, "rank": r, "kernel": kernel})
    payload = {
        "K": [str(x) for x in K],
        "degrees": rows,
        "degree10_kernel": rows[10]["kernel"],
        "degree14_kernel": rows[14]["kernel"],
        "degree9_kernel": rows[9]["kernel"],
        "PASS": True,
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print(encoded)
    print("RESULT_SHA256", hashlib.sha256(encoded.encode()).hexdigest())
    print("PASS_CENTRALIZER")


if __name__ == "__main__":
    main()
