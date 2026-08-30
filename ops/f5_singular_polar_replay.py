#!/usr/bin/env python3
"""Seconds-scale exact replay for the balanced singular-F5 B_s polar table.

This script is a deterministic arithmetic check, not analytic-realization
evidence.  It verifies the A_{s-1} exceptional coefficient/contact vectors
used in the accompanying local-polar report.
"""

from __future__ import annotations


def cartan_a_times(values: tuple[int, ...]) -> tuple[int, ...]:
    out = []
    for index, value in enumerate(values):
        adjacent = 0
        if index:
            adjacent += values[index - 1]
        if index + 1 < len(values):
            adjacent += values[index + 1]
        out.append(2 * value - adjacent)
    return tuple(out)


def expected_contact(s: int) -> tuple[int, ...]:
    rank = s - 1
    out = [0] * rank
    out[0] = 1
    if s % 2:
        # Two distinct smooth germs on E_{(s-1)/2}.
        out[(s - 1) // 2 - 1] += 2
    else:
        # One irreducible germ through E_{(s-2)/2} cap E_{s/2}.
        out[(s - 2) // 2 - 1] += 1
        out[s // 2 - 1] += 1
    return tuple(out)


def row(s: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    m = tuple(min(index + 1, s - index) for index in range(1, s))
    n = cartan_a_times(m)
    assert n == expected_contact(s)
    assert sum(n) == 3
    return m, n


def main() -> None:
    for s in range(5, 10):
        m, n = row(s)
        if s % 2:
            partition = "2+3+3"
            strict_germs = 3
        else:
            partition = "2+6"
            strict_germs = 2
        print(
            f"B{s}/A{s - 1}: m={m} n={n} "
            f"partition={partition} strict_germs={strict_germs}"
        )

    # The decisive A7 row.
    m8, n8 = row(8)
    assert m8 == (2, 3, 4, 4, 3, 2, 1)
    assert n8 == (1, 0, 1, 1, 0, 0, 0)


if __name__ == "__main__":
    main()
