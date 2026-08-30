#!/usr/bin/env python3
"""Optimization-safe exact replay for the unbalanced singular-F5 table.

Every verification uses an explicit exception and is therefore active under
ordinary Python, ``-O``, and ``-OO``.  ``--deliberate-mutation`` corrupts the
D5 contact vector and must terminate unsuccessfully in every interpreter
mode; it is a negative control for the verifier itself.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product
from typing import NoReturn


class ReplayFailure(RuntimeError):
    """An exact replay invariant failed."""


def fail(message: str) -> NoReturn:
    raise ReplayFailure(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


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
    require(rank >= 4, "D Cartan input must have rank at least four")
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
    require(bool(a0), "U3 requires a0 nonzero")
    require(bool(c1), "U3 requires c1 nonzero")
    cusp_constant = a0 / (c1 * c1)
    smooth_u_coefficient = Fraction(1, 4) / c1
    require(bool(cusp_constant), "U3 cusp edge coefficient vanished")
    require(bool(smooth_u_coefficient), "U3 smooth-branch coefficient vanished")
    return cusp_constant, smooth_u_coefficient


def d_cell_leading(
    a0: Fraction, b1: Fraction, c2: Fraction
) -> tuple[str, tuple[int, ...], tuple[Fraction, ...]]:
    require(bool(a0), "D cell requires a0 nonzero")
    delta = b1 + c2
    if delta:
        roots = (Fraction(0), -delta / a0)
        lift = Fraction(1, 4) / delta
        require(roots[0] != roots[1], "D5 pair roots collided")
        require(bool(lift), "D5 cubic lift vanished")
        require(bool(delta * delta), "D5 normal-form coefficient vanished")
        return "U5/D5", (2, 3, 3), (roots[1], lift, delta * delta)

    pair_square = Fraction(1, 4) / a0
    require(bool(pair_square), "D6 degree-five coefficient vanished")
    # K(z)/z has constant a0 when delta=0, so no higher-D jump is possible.
    require(bool(a0), "D6 forced next normal-form coefficient vanished")
    return "U6/D6", (3, 5), (pair_square, a0)


def verify(*, deliberate_mutation: bool = False) -> None:
    u3_m = (2, 2, 1)
    d5_m = (2, 4, 5, 3, 3)
    d6_m = (2, 4, 5, 6, 3, 3)
    u3_n = (2, 1, 0)
    d5_n = (0, 1, 0, 1, 1)
    d6_n = (0, 1, 0, 1, 0, 0)
    if deliberate_mutation:
        d5_n = (1, 0, 0, 0, 2)

    require(cartan_a(u3_m) == u3_n, "U3 Cartan/contact mismatch")
    require(cartan_d(d5_m) == d5_n, "D5 Cartan/contact mismatch")
    require(cartan_d(d6_m) == d6_n, "D6 Cartan/contact mismatch")

    nonzero = tuple(Fraction(value) for value in (-3, -2, -1, 1, 2, 3))
    for a0, c1 in product(nonzero, repeat=2):
        u3_leading(a0, c1)

    seen: set[str] = set()
    for a0, b1, c2_integer in product(nonzero, nonzero, range(-3, 4)):
        tag, partition, controls = d_cell_leading(
            a0, b1, Fraction(c2_integer)
        )
        require(sum(partition) == 8, f"{tag} partition does not sum to eight")
        require(all(controls), f"{tag} has a zero leading control")
        seen.add(tag)
    require(seen == {"U5/D5", "U6/D6"}, "D-cell grid missed a named cell")

    rows = (
        ("U3/A3", (4, 4), u3_m, u3_n),
        ("U5/D5", (2, 3, 3), d5_m, d5_n),
        ("U6/D6", (3, 5), d6_m, d6_n),
    )
    for tag, partition, exceptional, contact in rows:
        print(
            f"{tag}: partition={'+'.join(map(str, partition))} "
            f"m={exceptional} n={contact}"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--deliberate-mutation",
        action="store_true",
        help="corrupt the D5 contact vector; this run must fail",
    )
    return parser.parse_args()


def main() -> None:
    arguments = parse_args()
    verify(deliberate_mutation=arguments.deliberate_mutation)


if __name__ == "__main__":
    main()
