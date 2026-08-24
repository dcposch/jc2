#!/usr/bin/env python3
"""Exact integer audit for the partial-y-degree history stop.

This checks only the arithmetic and finite degree-pair bookkeeping in
``xmodel/as109-partial-y-history-stop-20260824.md``.  The cited
characteristic-zero total-degree theorems remain literature inputs.
"""

from __future__ import annotations

from functools import lru_cache
from math import gcd, isqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for p in range(3, isqrt(n) + 1, 2):
        if n % p == 0:
            return False
    return True


def next_progression_prime(h0: int, d0: int, lower_l: int) -> tuple[int, int]:
    """Find a sample Dirichlet prime h0+d0*L above a finite lower bound."""
    assert gcd(h0, d0) == 1
    for L in range(lower_l + 1, lower_l + 200_000):
        q = h0 + d0 * L
        if is_prime(q):
            return L, q
    raise AssertionError((h0, d0, lower_l))


def check_shear_arithmetic(m: int, n: int, H: int, lower_l: int) -> int:
    """Return g=gcd(H,d) after checking the exact total-degree formula."""
    d = gcd(m, n)
    a, b = m // d, n // d
    g = gcd(H, d)
    h0, d0 = H // g, d // g
    L, q = next_progression_prime(h0, d0, lower_l)
    common = H + d * L
    total_m = a * common
    total_n = b * common
    assert L > lower_l
    assert common == g * q
    assert gcd(a, b) == 1
    assert gcd(total_m, total_n) == common
    return g


# The proof is symbolic.  This finite sweep is a regression control for the
# formula, including H=0 (constant common leading core) and arbitrary lower-row
# degree bounds.
for m in range(1, 31):
    for n in range(m, 31):
        for H in range(0, 25):
            for lower_l in (0, 3, 19):
                g = check_shear_arithmetic(m, n, H, lower_l)
                if gcd(m, n) <= 2:
                    assert g in (1, 2)


def universal_shear_closed(m: int, n: int) -> bool:
    """Whether the prime/2-prime shear closes every possible core degree H."""
    return gcd(m, n) <= 2


@lru_cache(maxsize=None)
def covered_through_eight(m: int, n: int) -> bool:
    """Finite reduction audit for unordered 0<=m<=n<=8."""
    if m > n:
        m, n = n, m
    if m == 0:
        # Moskowicz Proposition 2.1: a Keller pair with one y-degree zero is
        # triangular (so alleged incompatible degree labels are empty).
        return True
    if universal_shear_closed(m, n):
        return True
    if m == n:
        # Constant target GL_2 cancels one leading y coefficient.  Every
        # possible strictly smaller successor must be covered.
        return all(covered_through_eight(r, n) for r in range(n))
    if n % m == 0:
        # A polynomial target shear strictly lowers the larger y-degree.
        return all(covered_through_eight(m, r) for r in range(n))
    return False


unordered_le8 = [(m, n) for n in range(9) for m in range(n + 1)]
ordered_le8 = [(m, n) for m in range(9) for n in range(9)]
unordered_le7 = [(m, n) for n in range(8) for m in range(n + 1)]
ordered_le7 = [(m, n) for m in range(8) for n in range(8)]
assert len(unordered_le7) == 36
assert len(ordered_le7) == 64
assert len(unordered_le8) == 45
assert len(ordered_le8) == 81
assert all(covered_through_eight(m, n) for m, n in unordered_le7)
assert all(covered_through_eight(min(m, n), max(m, n)) for m, n in ordered_le7)
assert all(covered_through_eight(m, n) for m, n in unordered_le8)
assert all(covered_through_eight(min(m, n), max(m, n)) for m, n in ordered_le8)


def max_nine_status(m: int) -> str:
    """Classify the unordered pair (m,9), 0<=m<=9."""
    n = 9
    if m == 0:
        return "zero-coordinate"
    if m == n:
        return "derivative-of-(6,9)-only"
    if n % m == 0:
        return "divisible-target-shear"
    if gcd(m, n) <= 2:
        return "prime-or-2prime-source-shear"
    assert m == 6 and gcd(m, n) == 3
    return "closed-if-3-not-divide-H; fundamental-open-if-3-divides-H"


max9 = {m: max_nine_status(m) for m in range(10)}
assert [m for m, status in max9.items() if "fundamental-open" in status] == [6]
assert [m for m, status in max9.items() if "derivative" in status] == [9]

# Explicitly check both residue classes of the first open pair.
for H in range(0, 30):
    g = check_shear_arithmetic(6, 9, H, 17)
    assert g == (3 if H % 3 == 0 else 1)

# Every consecutive positive pair has gcd one, including the proposed (6,7)
# computation and the constant-core case H=0.
for m in range(1, 101):
    assert universal_shear_closed(m, m + 1)
    for H in (0, 1, 2, 17):
        assert check_shear_arithmetic(m, m + 1, H, 23) == 1

# Cubic Kummer weights of the exact (6,9) stop: z,r have weight 1, u has
# weight 2, and v has weight 0.  Every monomial of K=z^3+u*z+v is invariant.
assert {(3 * 1) % 3, (2 + 1) % 3, 0} == {0}

print("PASS-PARTIAL-Y-HISTORY-COVERAGE")
print("consecutive_pairs=KNOWN_BY_PRIME-GCD-SHEAR")
print("max_actual_y_degree_le_7=ALL_64_ORDERED_PAIRS_COVERED")
print("max_actual_y_degree_le_8=ALL_81_ORDERED_PAIRS_COVERED")
print("max9_fundamental_open=(6,9) with 3|H")
print("max9_derivative_open=(9,9) via target-GL2 successor (6,9)")
print("preflight_target=(6,9),3|H")
