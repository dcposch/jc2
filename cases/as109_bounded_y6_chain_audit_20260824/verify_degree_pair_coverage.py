#!/usr/bin/env python3
"""Exact finite audit of actual y-degree pairs through degree six.

This enumerates degree pairs, not monomial supports or coefficients.  It
records the strict target reduction and the reviewed/provisional leaf on
which each pair depends.
"""

from functools import lru_cache


CONFIRMED_EMPTY_LEAVES = {
    (2, 3): "CUBIC-(2,3)",
    (3, 4): "QUARTIC-(3,4)",
    (2, 5): "QUINTIC-(2,5)",
    (3, 5): "QUINTIC-(3,5)",
    (4, 5): "QUINTIC-(4,5)",
}
PROVISIONAL_EMPTY_LEAVES = {
    (4, 6): "SEXTIC-(4,6)",
    (5, 6): "SEXTIC-(5,6)",
}
ALL_GENUINE_LEAVES = CONFIRMED_EMPTY_LEAVES | PROVISIONAL_EMPTY_LEAVES


def ordered(m: int, n: int) -> tuple[int, int]:
    return (m, n) if m <= n else (n, m)


@lru_cache(maxsize=None)
def route(m: int, n: int) -> tuple[str, tuple[tuple[int, int], ...], frozenset]:
    """Return (reduction, possible children, provisional leaves required)."""
    m, n = ordered(m, n)
    assert 0 <= m <= n <= 6

    if m == 0:
        if n == 0:
            return ("J=0: impossible", (), frozenset())
        if n == 1:
            return ("degree-zero/affine triangular automorphism", (), frozenset())
        return ("a_0'(x) g_y constant forces n=1: impossible", (), frozenset())

    if m == 1:
        return ("affine-in-y triangular reduction", (), frozenset())

    pair = (m, n)
    if pair in CONFIRMED_EMPTY_LEAVES:
        return (CONFIRMED_EMPTY_LEAVES[pair] + " empty (CONFIRMED)", (), frozenset())
    if pair in PROVISIONAL_EMPTY_LEAVES:
        return (
            PROVISIONAL_EMPTY_LEAVES[pair] + " empty (PROVISIONAL)",
            (),
            frozenset({pair}),
        )

    if m == n:
        # A constant target GL2 operation cancels one top coefficient.  The
        # surviving coordinate still has degree n, while the other can have
        # any actual degree r<n.
        children = tuple((r, n) for r in range(n))
        needed = frozenset().union(*(route(*child)[2] for child in children))
        return ("equal-degree target GL2", children, needed)

    if n % m == 0:
        # g-k f^(n/m) cancels the top y^n coefficient.  Both resulting
        # actual degrees are <n; enumerate every possible lowered degree.
        children = tuple(sorted({ordered(m, r) for r in range(n)}))
        needed = frozenset().union(*(route(*child)[2] for child in children))
        return (f"divisible-degree target shear g-k f^{n // m}", children, needed)

    raise AssertionError(f"unclassified genuine degree pair {(m, n)}")


def main() -> None:
    unordered = [(m, n) for n in range(7) for m in range(n + 1)]
    assert len(unordered) == 28
    assert set(ALL_GENUINE_LEAVES) == {
        (2, 3), (3, 4), (2, 5), (3, 5), (4, 5), (4, 6), (5, 6)
    }

    results = {pair: route(*pair) for pair in unordered}
    unresolved = {pair for pair, value in results.items() if value[2]}
    assert unresolved == {(4, 6), (5, 6), (6, 6)}
    assert results[(6, 6)][2] == frozenset({(4, 6), (5, 6)})
    assert all(not results[pair][2] for pair in unordered if pair[1] <= 5)

    print("PASS-BOUNDED-Y6-DEGREE-PAIR-COVERAGE")
    print(f"unordered_pairs={len(unordered)}")
    print(f"ordered_pairs={7 * 7}")
    print("confirmed_genuine_leaves=" + ",".join(map(str, CONFIRMED_EMPTY_LEAVES)))
    print("provisional_genuine_leaves=" + ",".join(map(str, PROVISIONAL_EMPTY_LEAVES)))
    print("confirmed_only_unresolved_pairs=" + ",".join(map(str, sorted(unresolved))))
    print("fundamental_unreviewed_blockers=(4, 6),(5, 6)")
    print("conditional_on_both_closures=ALL_49_ORDERED_PAIRS_COVERED")


if __name__ == "__main__":
    main()
