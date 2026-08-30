#!/usr/bin/env python3
"""Exact stdlib replay for the unbalanced singular-F5 polar table.

This is a deterministic arithmetic check of the leading Newton systems and
Cartan-vector calculations in the accompanying report.  It is not evidence
for analytic realization or for the existence of a polynomial map.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def cartan_a(values: tuple[int, ...]) -> tuple[int, ...]:
    out: list[int] = []
    for index, value in enumerate(values):
        adjacent = (values[index - 1] if index else 0) + (
            values[index + 1] if index + 1 < len(values) else 0
        )
        out.append(2 * value - adjacent)
    return tuple(out)


def cartan_d(values: tuple[int, ...]) -> tuple[int, ...]:
    """D_r numbering 1--...--(r-2), with spins r-1,r at r-2."""

    rank = len(values)
    assert rank >= 4
    out: list[int] = []
    for vertex, value in enumerate(values, start=1):
        if vertex == 1:
            neighbors = (2,)
        elif vertex < rank - 2:
            neighbors = (vertex - 1, vertex + 1)
        elif vertex == rank - 2:
            neighbors = (rank - 3, rank - 1, rank)
        else:
            neighbors = (rank - 2,)
        out.append(2 * value - sum(values[item - 1] for item in neighbors))
    return tuple(out)


def u3_leading(a0: Fraction, c1: Fraction) -> tuple[Fraction, Fraction]:
    """Return the two nonzero coefficients controlling the U3 germs."""

    assert a0 and c1
    # Cusp edge: 2*v*z^2 + cusp_constant*v^4 = 0.
    cusp_constant = a0 / (c1 * c1)
    # Pair-midpoint branch: u = smooth_u_coefficient*z^4 + higher.
    smooth_u_coefficient = Fraction(1, 4) / c1
    assert cusp_constant and smooth_u_coefficient
    return cusp_constant, smooth_u_coefficient


def d_cell_leading(
    a0: Fraction, b1: Fraction, c2: Fraction
) -> tuple[str, tuple[int, ...], tuple[Fraction, ...]]:
    """Classify the D cell and return its partition and nonzero controls."""

    assert a0
    delta = b1 + c2
    if delta:
        # Pair roots in U=u/z^2 are 0 and -delta/a0.  The zero root lifts to
        # u=(1/(4*delta))*z^3+..., so neither root nor lift can collide.
        roots = (Fraction(0), -delta / a0)
        lift = Fraction(1, 4) / delta
        assert roots[0] != roots[1] and lift
        # K(0)=delta^2 is the D5 normal-form coefficient.
        assert delta * delta
        return "U5/D5", (2, 3, 3), (roots[1], lift, delta * delta)

    # When delta=0, K(z)/z has constant a0: the named cell is exactly D6,
    # not a higher-D degeneration.  Its pair germ has u^2=(1/(4*a0))*z^5.
    pair_square = Fraction(1, 4) / a0
    assert pair_square and a0
    return "U6/D6", (3, 5), (pair_square, a0)


def main() -> None:
    assert cartan_a((2, 2, 1)) == (2, 1, 0)
    assert cartan_d((2, 4, 5, 3, 3)) == (0, 1, 0, 1, 1)
    assert cartan_d((2, 4, 5, 6, 3, 3)) == (0, 1, 0, 1, 0, 0)

    # Exact rational controls over a grid exercise both D cells and all signs.
    nonzero = tuple(Fraction(value) for value in (-3, -2, -1, 1, 2, 3))
    for a0, c1 in product(nonzero, repeat=2):
        u3_leading(a0, c1)

    seen: set[str] = set()
    for a0, b1, c2 in product(nonzero, nonzero, range(-3, 4)):
        tag, partition, controls = d_cell_leading(a0, b1, Fraction(c2))
        assert sum(partition) == 8 and all(controls)
        seen.add(tag)
    assert seen == {"U5/D5", "U6/D6"}

    rows = (
        ("U3/A3", (4, 4), (2, 2, 1), (2, 1, 0)),
        ("U5/D5", (2, 3, 3), (2, 4, 5, 3, 3), (0, 1, 0, 1, 1)),
        ("U6/D6", (3, 5), (2, 4, 5, 6, 3, 3), (0, 1, 0, 1, 0, 0)),
    )
    for tag, partition, exceptional, contact in rows:
        print(
            f"{tag}: partition={'+'.join(map(str, partition))} "
            f"m={exceptional} n={contact}"
        )


if __name__ == "__main__":
    main()
