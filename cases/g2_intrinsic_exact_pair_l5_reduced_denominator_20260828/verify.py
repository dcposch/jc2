#!/usr/bin/env python3
"""Desk checks for the exact-pair reduced-denominator/deck-orbit lemma.

This is deliberately only a finite group-arithmetic checker.  The local-field
and normalization arguments are proved in the accompanying review.
"""

from __future__ import annotations

from functools import reduce
from itertools import combinations
from math import gcd
import json


def gcd_support(kappa: int, support: tuple[int, ...]) -> int:
    """gcd(kappa, support), with the zero/constant-series convention."""

    return reduce(gcd, support, kappa)


def stabilizer(kappa: int, support: tuple[int, ...]) -> tuple[int, ...]:
    """Deck exponents a for which t -> zeta^a t fixes the series."""

    return tuple(
        a
        for a in range(kappa)
        if all((a * exponent) % kappa == 0 for exponent in support)
    )


def orbit_signatures(kappa: int, support: tuple[int, ...]) -> set[tuple[int, ...]]:
    """Coefficient phase signatures of the orbit of a nonzero-support series."""

    return {
        tuple((a * exponent) % kappa for exponent in support)
        for a in range(kappa)
    }


def reduced_denominator(kappa: int, support: tuple[int, ...]) -> int:
    return kappa // gcd_support(kappa, support)


def exhaustive_group_check() -> int:
    checked = 0
    for kappa in range(1, 13):
        residues = tuple(range(kappa))
        for size in range(kappa + 1):
            for support in combinations(residues, size):
                g = gcd_support(kappa, support)
                stab = stabilizer(kappa, support)
                orbit = orbit_signatures(kappa, support)
                assert len(stab) == g
                assert len(orbit) == kappa // g
                assert len(stab) * len(orbit) == kappa
                assert reduced_denominator(kappa, support) == len(orbit)
                checked += 1
    return checked


def oversized_kummer_control() -> dict[str, object]:
    # Y^2-u over K((u)), embedded by u=t^4.  Its two presentations are
    # t^2 and -t^2.  They form one orbit, hence one normalized place of
    # ramification two; the ambient Kummer index four is not intrinsic.
    kappa = 4
    support = (2,)
    phases = {(2 * a) % kappa for a in range(kappa)}
    assert phases == {0, 2}
    assert len(stabilizer(kappa, support)) == 2
    assert reduced_denominator(kappa, support) == 2
    assert reduced_denominator(kappa, support) != kappa
    # Squaring either coefficient phase gives coefficient one in t^4.
    assert {(2 * phase) % kappa for phase in phases} == {0}
    return {
        "ambient_kappa": kappa,
        "equation": "Y^2-u with u=t^4",
        "orbit_phases_mod_4": sorted(phases),
        "orbit_size": len(phases),
        "reduced_denominator": reduced_denominator(kappa, support),
        "stabilizer_size": len(stabilizer(kappa, support)),
    }


def truncate(series: dict[int, int], cutoff: int) -> dict[int, int]:
    """Keep exponents strictly below cutoff."""

    return {exponent: coefficient for exponent, coefficient in series.items()
            if exponent < cutoff and coefficient != 0}


def premature_leaf_control() -> dict[str, object]:
    # Local x-infinity factors y-u and y-u-u^N come from the squarefree plane
    # polynomial (xy-1)(x^N y-x^(N-1)-1), with u=1/x.
    order = 7
    first = {1: 1}
    second = {1: 1, order: 1}
    assert first != second
    assert truncate(first, order) == truncate(second, order)
    assert truncate(first, order + 1) != truncate(second, order + 1)
    # kappa=1 has no nontrivial deck action, so these are two distinct places.
    assert reduced_denominator(1, (1,)) == 1
    return {
        "global_equation": "(xy-1)(x^7*y-x^6-1)=0",
        "local_roots": ["y=u", "y=u+u^7"],
        "places": 2,
        "prefixes_equal_below_exponent": order,
        "separate_when_exponent_is_included": order,
    }


def main() -> None:
    payload = {
        "exhaustive_support_sets_checked": exhaustive_group_check(),
        "oversized_kummer_control": oversized_kummer_control(),
        "premature_leaf_control": premature_leaf_control(),
        "scope": (
            "finite cyclic-group arithmetic and two exact controls only; "
            "normalization/local-field proof is in the review"
        ),
        "status": "PASS",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
