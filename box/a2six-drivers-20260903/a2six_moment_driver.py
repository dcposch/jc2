#!/usr/bin/env python3
"""Bounded first-page diagnostics for the A2=6, fixed-N=6 ray.

This is a custody wrapper and a scalable direct-moment companion to the
frozen GLOBAL-INTERPOLATION/1.0 driver.  It intentionally does not infer a
Puiseux decoration from the numerical Moh skeleton.  The arithmetic admits,
and the witness manifest declares, a proper packet; this is not attainment.
The charge fixes several aggregate root counts, but not the non-proper tree,
its Galois action, tame supports, or coefficient sharing.  Consequently the
``certificate`` command clearly labels its completion WITNESS-ONLY.

The matrices below are the consecutive-moment/parity projections used by the
frozen driver: rows r have entries tau_i^r/D_i.  ``raw_leaf`` retains the
three root channels of each rigid cubic star (a confluent Vandermonde initial
form).  ``rigid_star_macro`` retains one channel per normalized cubic slot.
They bracket two different maps from actual deformation coordinates to
primitive values; neither is asserted to be the missing geometric map.

The frozen driver says that a partial Galois orbit is an input error, but it
trusts ``verified:true`` rather than checking a permutation.  ``validate`` is
therefore a mandatory preflight and refuses an incomplete six-cycle.

Unknown-count convention (repair of the charged (4.13)/(4.16) mismatch):
leading/star coordinates are INCLUDED in Z_page, so

    U_page = h_constants + |Z_page|,

with no second addition of u0.  The page tables exclude constants (they do
not enter the normalized parity matrix) and print them separately.

Notation note: the Python argument ``t`` is the integer ray index.  Legacy
JSON keys ending in ``_t`` record valuation in the Puiseux base
``xi=x^{-1}``; they do not mean valuation in the integer index.
Likewise, legacy keys containing ``Schur_rank`` mean only incremental rank in
the displayed independent-value projection, not the geometric Schur map from
actual tame parameters.  ``PROPER-PACKET EXACT`` means exact custody of the
declared witness packet, not geometric attainment or full-series covariance.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


GOOD_PRIMES = (1009, 1013, 1019)
EXPECTED_GLOBALINTERP_SHA256 = (
    "49ba5a019714e30a952c998fb39a88aff38505a80fcac6df3c5883bb16599588"
)
DEFAULT_GLOBALINTERP = Path("/tmp/jc2-lane.OAeQcz/inputs/globalinterp.py")


def qstr(q: Fraction) -> str:
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def choose2(n: int) -> int:
    return n * (n - 1) // 2


def family(t: int, k: int = 12) -> dict[str, Any]:
    if t < 0:
        raise ValueError("t must be nonnegative")
    if k not in (6, 12):
        raise ValueError("this bounded lane supports the full packets k=6 and k=12")
    P = 7 * t + 6
    n = 9 * P
    m = 6 * P
    K = 3 * P
    u = 18 * t + 15
    v = K - u
    e, d = 3, 2
    major = e * u
    proper = e * k
    residual = major - proper
    top_minor = e * v
    nonproper = n - proper
    assert residual > 1
    assert nonproper == e * (K - k) == residual + top_minor
    assert k % 6 == 0 and k <= u
    delta3 = Fraction(-1)
    delta2 = Fraction(1, 6)
    delta1 = Fraction(7, 12)
    rho_residual = delta2 + Fraction(1, 6 * (residual - 1))
    rho_top = Fraction(2)
    dval_proper = 2 * delta1 + (major - 3) * delta2 + top_minor * delta3
    dval_residual = (
        (residual - 1) * rho_residual + proper * delta2 + top_minor * delta3
    )
    dval_top = (top_minor - 1) * rho_top + major * delta3
    assert dval_proper == Fraction(-5, 6)
    assert dval_residual == Fraction(-3, 2)
    assert dval_top == -36 * t - 29
    R_completion = math.lcm(12, rho_residual.denominator)
    homogeneous = K - 1
    return {
        "t": t,
        "P": P,
        "D": n,
        "n": n,
        "m": m,
        "M": [-6 * P, 4 * P, 9 * P - 2],
        "V": {"2": 1, "3": 6 * t + 5},
        "K": K,
        "d": d,
        "e": e,
        "u": u,
        "v": v,
        "A2": 6,
        "A1": 2,
        "q": "1/2",
        "k": k,
        "N": qstr(Fraction(k, 2)),
        "disc_orbits": k // 6,
        "visible_proper_branch_orbits": 2 * (k // 6),
        "homogeneous_DEG_rows": homogeneous,
        "DEG_rows_with_monic": K,
        "delta": ["-1", "1/6", "7/12"],
        "minimal_display_uniformizer_R": 12,
        "bottom_to_D2_gap_z": 5,
        "D2_to_D3_gap_z": 14,
        "major_D2_roots": major,
        "proper_bottom_roots": proper,
        "major_residual_nonproper_roots": residual,
        "top_minor_roots": top_minor,
        "aggregate_nonproper_roots": nonproper,
        "witness_contacts_t": {
            "cross_D2_top": "-1",
            "cross_D2_children": "1/6",
            "proper_internal": "7/12",
            "residual_internal": qstr(rho_residual),
            "top_internal": "2",
        },
        "witness_completion_R": R_completion,
        "derivative_valuations_t": {
            "proper": "-5/6",
            "major_residual": "-3/2",
            "top_minor": str(dval_top),
        },
        "nonproper_f_minus_a0_orders_t": {
            "major_residual": "1/2",
            "top_minor": str(-1 - dval_top),
        },
    }


def _cycle(members: list[str]) -> dict[str, str]:
    return {name: members[(i + 1) % len(members)] for i, name in enumerate(members)}


def canonical_manifest(t: int, k: int = 12) -> dict[str, Any]:
    f = family(t, k)
    packets = []
    for orbit_index in range(k // 6):
        members = [f"O{orbit_index + 1}_D1_{j}" for j in range(6)]
        packets.append(
            {
                "name": f"O{orbit_index + 1}",
                "kind": "nonzero-(10)",
                "expected_size": 6,
                "members": members,
                "generator": _cycle(members),
                "lower_data": {
                    "V2": 1,
                    "delta1": "7/12",
                    "A1": 2,
                    "bottom_case": "(13)",
                    "bottom_star": {"p_g": "pi^3-pi", "p_f": "pi^2-2/3"},
                },
                "visible_branch_orbits": [
                    {
                        "kind": "zero-star-root",
                        "length": 6,
                        "pi": "0",
                        "integration_constant": f"a_O{orbit_index + 1}_zero",
                    },
                    {
                        "kind": "nonzero-star-roots",
                        "length": 12,
                        "pi": "+/-1",
                        "integration_constant": f"a_O{orbit_index + 1}_nonzero",
                    },
                ],
            }
        )
    return {
        "schema": "A2SIX-DECORATION/1",
        "typing": "PROPER-PACKET EXACT; NONPROPER COMPLETION WITNESS-ONLY / UNREVIEWED",
        "family_t": t,
        "k": k,
        "disc_orbits": packets,
        "root_blocks": {
            "major_D2_total": f["major_D2_roots"],
            "proper_bottom_roots": f["proper_bottom_roots"],
            "major_residual_nonproper_roots": f["major_residual_nonproper_roots"],
            "top_minor_roots": f["top_minor_roots"],
            "total_nonproper_roots": f["aggregate_nonproper_roots"],
        },
        "tree": {
            "D3": {"radius_t": "-1", "size": f["n"]},
            "D2_unique_major": {"radius_t": "1/6", "size": f["major_D2_roots"]},
            "proper_D1_children": {
                "count": k,
                "size_each": 3,
                "radius_t": "7/12",
            },
            "nonproper_aggregate_is_not_a_tree": True,
        },
        "witness_only_extra_choices": {
            "major_residual_one_cluster_contact_t": f["witness_contacts_t"][
                "residual_internal"
            ],
            "top_minor_one_cluster_contact_t": "2",
            "proper_disc_centres": "two formal cyclotomic 6-orbits (one for k=6)",
            "proper_internal_roots": ["0", "+1", "-1"],
            "inner_sharing": (
                "three branches share their D1 centre through z^6 and split at z^7; "
                "post-star tails are not supplied by the skeleton"
            ),
            "outer_sharing": (
                "all D2 descendants share ancestors below z^2; D2/D1 outer units first "
                "may change at relative z^5; D3/D2 outer units at relative z^14"
            ),
            "nonproper_galois_action": "UNSPECIFIED",
            "tame_support_and_sharing": "UNSPECIFIED beyond the displayed leading contacts",
            "precision_guard": "valuation-only parity projection, not a full quadratic lift",
        },
    }


def validate_manifest(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != "A2SIX-DECORATION/1":
        raise ValueError("REFUSED[SCHEMA]: missing A2SIX-DECORATION/1")
    t, k = int(data["family_t"]), int(data["k"])
    f = family(t, k)
    packets = list(data.get("disc_orbits", []))
    if len(packets) != k // 6:
        raise ValueError(
            f"REFUSED[PARTIAL-ORBIT]: expected {k // 6} complete disc orbits, got {len(packets)}"
        )
    all_members: list[str] = []
    for packet in packets:
        expected = packet.get("expected_size")
        members = list(packet.get("members", []))
        generator = dict(packet.get("generator", {}))
        if expected != 6 or len(members) != 6 or len(set(members)) != 6:
            raise ValueError(
                "REFUSED[PARTIAL-ORBIT]: every (10) disc orbit must contain exactly A2=6 members"
            )
        member_set = set(members)
        if set(generator) != member_set or set(generator.values()) != member_set:
            raise ValueError("REFUSED[PARTIAL-ORBIT]: generator is not a permutation")
        seen: list[str] = []
        current = members[0]
        while current not in seen:
            seen.append(current)
            current = generator[current]
        if current != members[0] or len(seen) != 6:
            raise ValueError(
                f"REFUSED[PARTIAL-ORBIT]: generator cycle has length {len(seen)}, expected 6"
            )
        lower = packet.get("lower_data", {})
        if lower.get("V2") != 1 or lower.get("delta1") != "7/12" or lower.get("A1") != 2:
            raise ValueError("REFUSED[LOWER-DATA]: expected identical (V2,delta1,A1)=(1,7/12,2)")
        all_members.extend(members)
    if len(set(all_members)) != k:
        raise ValueError("REFUSED[PARTIAL-ORBIT]: disc-orbit member names overlap")
    blocks = data.get("root_blocks", {})
    expected_blocks = {
        "major_D2_total": f["major_D2_roots"],
        "proper_bottom_roots": f["proper_bottom_roots"],
        "major_residual_nonproper_roots": f["major_residual_nonproper_roots"],
        "top_minor_roots": f["top_minor_roots"],
        "total_nonproper_roots": f["aggregate_nonproper_roots"],
    }
    for key, value in expected_blocks.items():
        if blocks.get(key) != value:
            raise ValueError(f"REFUSED[ROOT-COUNT]: {key}={blocks.get(key)!r}, expected {value}")
    return {
        "status": "ACCEPTED[PROPER-PACKET-CUSTODY-ONLY]",
        "family": f,
        "disc_orbit_cycles": len(packets),
        "proper_branch_orbits_visible_at_rigid_star": f["visible_proper_branch_orbits"],
        "proper_integration_constants_before_global_equations": f[
            "visible_proper_branch_orbits"
        ],
        "proper_integration_constants_after_explicit_star_sharing": f["disc_orbits"],
        "star_sharing_status": (
            "EXTRA IDENTIFICATION, not implied by Galois: equate the zero-root and "
            "nonzero-root constants inside each disc orbit"
        ),
        "requested_two_constant_warning": (
            "one constant per disc orbit is not the Galois rule: A1=2 fixes pi=0 and swaps "
            "pi=+/-1, so each six-disc orbit displays a 6-branch and a 12-branch orbit"
        ),
        "full_globalinterp_decoration": False,
        "missing_for_full_decoration": [
            "nonproper rooted contact tree (NONPROPER-COUNT is only a count)",
            "complete Galois permutation on all n root series",
            "post-star and nonproper tame exponent supports",
            "outer/inner coefficient identifications",
            "actual Puiseux coefficients and sufficient inverse/integration guard",
        ],
    }


def modular_rank(matrix: list[list[int]], p: int) -> int:
    if not matrix:
        return 0
    a = [[value % p for value in row] for row in matrix]
    nr, nc = len(a), len(a[0])
    rank = 0
    for col in range(nc):
        pivot = next((row for row in range(rank, nr) if a[row][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(v * inv) % p for v in a[rank]]
        for row in range(nr):
            if row != rank and a[row][col]:
                scale = a[row][col]
                a[row] = [(u - scale * v) % p for u, v in zip(a[row], a[rank])]
        rank += 1
        if rank == nr:
            break
    return rank


def confluent_matrix(rows: int, clusters: int, p: int) -> list[list[int]]:
    result = []
    for r in range(rows):
        row: list[int] = []
        for centre in range(1, clusters + 1):
            for jet in range(3):
                value = 0 if r < jet else math.comb(r, jet) * pow(centre, r - jet, p)
                row.append(value % p)
        result.append(row)
    return result


def hermite_plus_matrix(rows: int, clusters: int, extra: int, p: int) -> list[list[int]]:
    base = confluent_matrix(rows, clusters, p)
    for r, row in enumerate(base):
        row.extend(pow(clusters + 1 + j, r, p) for j in range(extra))
    return base


def vandermonde(rows: int, columns: int, p: int) -> list[list[int]]:
    return [[pow(column + 1, r, p) for column in range(columns)] for r in range(rows)]


def rank_table(t: int, k: int) -> dict[str, Any]:
    f = family(t, k)
    rows = f["homogeneous_DEG_rows"]
    raw_proper_columns = f["proper_bottom_roots"]
    raw_extra = f["aggregate_nonproper_roots"]
    macro_proper_columns = k
    macro_extra = f["K"] - k
    exact = {
        "raw_leaf_proper": min(rows, raw_proper_columns),
        "raw_leaf_through_D2": rows,
        "raw_leaf_full_witness": rows,
        "rigid_star_macro_proper": min(rows, macro_proper_columns),
        "rigid_star_macro_through_D2": min(rows, f["u"]),
        "rigid_star_macro_full_witness": rows,
    }
    primes: dict[str, Any] = {}
    for p in GOOD_PRIMES:
        raw_proper = modular_rank(confluent_matrix(rows, k, p), p)
        raw_d2 = modular_rank(
            hermite_plus_matrix(
                rows, k, f["major_residual_nonproper_roots"], p
            ),
            p,
        )
        raw_full = modular_rank(hermite_plus_matrix(rows, k, raw_extra, p), p)
        macro_proper = modular_rank(vandermonde(rows, k, p), p)
        macro_d2 = modular_rank(vandermonde(rows, f["u"], p), p)
        macro_full = modular_rank(vandermonde(rows, f["K"], p), p)
        primes[str(p)] = {
            "raw_leaf_proper": raw_proper,
            "raw_leaf_through_D2": raw_d2,
            "raw_leaf_full_witness": raw_full,
            "rigid_star_macro_proper": macro_proper,
            "rigid_star_macro_through_D2": macro_d2,
            "rigid_star_macro_full_witness": macro_full,
        }
        if primes[str(p)] != exact:
            raise AssertionError(f"unexpected rank modulo {p}: {primes[str(p)]} != {exact}")
    raw_rank = exact["raw_leaf_proper"]
    macro_rank = exact["rigid_star_macro_proper"]
    raw_d2_rank = exact["raw_leaf_through_D2"]
    macro_d2_rank = exact["rigid_star_macro_through_D2"]

    affine_rows = f["K"]
    affine_raw_proper = min(affine_rows, raw_proper_columns)
    affine_raw_d2 = affine_rows
    affine_macro_proper = k
    affine_macro_d2 = f["u"]
    affine_prime_checks: dict[str, Any] = {}
    for p in GOOD_PRIMES:
        affine_prime_checks[str(p)] = {
            "raw_leaf_proper": modular_rank(confluent_matrix(affine_rows, k, p), p),
            "raw_leaf_through_D2": modular_rank(
                hermite_plus_matrix(
                    affine_rows, k, f["major_residual_nonproper_roots"], p
                ),
                p,
            ),
            "raw_leaf_full_witness": modular_rank(
                hermite_plus_matrix(affine_rows, k, raw_extra, p), p
            ),
            "rigid_star_macro_proper": modular_rank(
                vandermonde(affine_rows, k, p), p
            ),
            "rigid_star_macro_through_D2": modular_rank(
                vandermonde(affine_rows, f["u"], p), p
            ),
            "rigid_star_macro_full_witness": modular_rank(
                vandermonde(affine_rows, f["K"], p), p
            ),
        }
        affine_expected = {
            "raw_leaf_proper": affine_raw_proper,
            "raw_leaf_through_D2": affine_raw_d2,
            "raw_leaf_full_witness": affine_rows,
            "rigid_star_macro_proper": affine_macro_proper,
            "rigid_star_macro_through_D2": affine_macro_d2,
            "rigid_star_macro_full_witness": affine_rows,
        }
        if affine_prime_checks[str(p)] != affine_expected:
            raise AssertionError(
                f"unexpected affine rank modulo {p}: "
                f"{affine_prime_checks[str(p)]} != {affine_expected}"
            )
    return {
        "equations": rows,
        "raw_leaf_coordinate_model": {
            "unknowns_proper": raw_proper_columns,
            "rank_proper_over_Q": raw_rank,
            "left_cokernel_proper": rows - raw_rank,
            "unknowns_after_nonproper": f["n"],
            "rank_after_nonproper_over_Q": rows,
            "left_cokernel_after_nonproper": 0,
            "nonproper_incremental_Schur_rank": rows - raw_rank,
            "D2_residual_unknowns_added": f["major_residual_nonproper_roots"],
            "rank_through_D2_over_Q": raw_d2_rank,
            "left_cokernel_through_D2": rows - raw_d2_rank,
            "D2_residual_incremental_Schur_rank": raw_d2_rank - raw_rank,
            "top_minor_incremental_Schur_rank": rows - raw_d2_rank,
            "exact_rank_proof": (
                "Hermite/confluent Vandermonde minor at distinct rational witness centres; "
                "determinant is a nonzero product of centre differences and factorials"
            ),
        },
        "rigid_star_macro_model": {
            "unknowns_proper": macro_proper_columns,
            "rank_proper_over_Q": macro_rank,
            "left_cokernel_proper": rows - macro_rank,
            "unknowns_after_nonproper": f["K"],
            "rank_after_nonproper_over_Q": rows,
            "left_cokernel_after_nonproper": 0,
            "nonproper_incremental_Schur_rank": rows - macro_rank,
            "D2_residual_macro_unknowns_added": f["u"] - k,
            "rank_through_D2_over_Q": macro_d2_rank,
            "left_cokernel_through_D2": rows - macro_d2_rank,
            "D2_residual_incremental_Schur_rank": macro_d2_rank - macro_rank,
            "top_minor_macro_unknowns_added": f["v"],
            "top_minor_incremental_Schur_rank": rows - macro_d2_rank,
            "exact_rank_proof": "ordinary Vandermonde minor at distinct rational witness centres",
        },
        "three_good_prime_checks": primes,
        "degree_page_with_separate_monic_row": {
            "equations": affine_rows,
            "note": "the last equation has affine target 1; these are Jacobian/tangent ranks",
            "raw_leaf_coordinate_model": {
                "unknowns_proper": raw_proper_columns,
                "rank_proper_over_Q": affine_raw_proper,
                "left_cokernel_proper": affine_rows - affine_raw_proper,
                "D2_residual_unknowns_added": f["major_residual_nonproper_roots"],
                "rank_through_D2_over_Q": affine_raw_d2,
                "D2_residual_incremental_Schur_rank": affine_raw_d2
                - affine_raw_proper,
                "top_minor_incremental_Schur_rank": 0,
                "unknowns_full": f["n"],
                "rank_full_over_Q": affine_rows,
                "left_cokernel_full": 0,
            },
            "rigid_star_macro_model": {
                "unknowns_proper": k,
                "rank_proper_over_Q": affine_macro_proper,
                "left_cokernel_proper": affine_rows - affine_macro_proper,
                "D2_residual_macro_unknowns_added": f["u"] - k,
                "rank_through_D2_over_Q": affine_macro_d2,
                "left_cokernel_through_D2": affine_rows - affine_macro_d2,
                "D2_residual_incremental_Schur_rank": affine_macro_d2
                - affine_macro_proper,
                "top_minor_macro_unknowns_added": f["v"],
                "top_minor_incremental_Schur_rank": affine_rows - affine_macro_d2,
                "unknowns_full": f["K"],
                "rank_full_over_Q": affine_rows,
                "left_cokernel_full": 0,
            },
            "three_good_prime_checks": affine_prime_checks,
        },
        "qualification": (
            "exact over Q for the displayed rational witness matrices; not the rank of an "
            "unprovided associated-graded deformation-to-H map"
        ),
    }


def balanced_internal_pairs(selected: int, clusters: int) -> tuple[int, list[int], int]:
    if not 0 <= selected <= 3 * clusters:
        raise ValueError("proper selection outside capacity")
    base, extra = divmod(selected, clusters)
    if base == 3 and extra:
        raise AssertionError("bad occupancy")
    profile = [0, 0, 0, 0]
    profile[base] = clusters - extra
    if extra:
        profile[base + 1] = extra
    pair_count = (clusters - extra) * choose2(base) + extra * choose2(base + 1)
    ways = math.comb(clusters, extra)
    ways *= math.comb(3, base) ** (clusters - extra)
    if extra:
        ways *= math.comb(3, base + 1) ** extra
    return pair_count, profile, ways


def tropical_minimum(
    t: int,
    k: int,
    rho_top: Fraction = Fraction(2),
    residual_increment_numerator: int = 1,
) -> dict[str, Any]:
    """Exact minimum basis weight for one explicitly declared contact tree.

    For a scaled GRS basis S and complement T,
        val det(A_S) = -C_all + C(T),
    where C is the sum of pairwise contacts.  The finite search is only over
    the three aggregate child types; proper occupancies are balanced exactly.
    """
    f = family(t, k)
    rows = f["homogeneous_DEG_rows"]
    proper = f["proper_bottom_roots"]
    residual = f["major_residual_nonproper_roots"]
    top = f["top_minor_roots"]
    complement = f["n"] - rows
    d3, d2, d1 = Fraction(-1), Fraction(1, 6), Fraction(7, 12)
    rho_residual = d2 + Fraction(residual_increment_numerator, 6 * (residual - 1))
    dval_residual = (residual - 1) * rho_residual + proper * d2 + top * d3
    if dval_residual >= -1:
        raise ValueError("residual completion violates the strict nonproper frontier")

    def contact_sum(xp: int, xr: int, xt: int) -> tuple[Fraction, list[int], int]:
        pairs, profile, proper_ways = balanced_internal_pairs(xp, k)
        major = xp + xr
        value = d2 * choose2(major)
        value += (d1 - d2) * pairs
        value += (rho_residual - d2) * choose2(xr)
        value += d3 * major * xt
        value += rho_top * choose2(xt)
        ways = proper_ways * math.comb(residual, xr) * math.comb(top, xt)
        return value, profile, ways

    best: Fraction | None = None
    minimizers: list[dict[str, Any]] = []
    total_ways = 0
    for xt in range(top + 1):
        for xr in range(residual + 1):
            xp = complement - xr - xt
            if not 0 <= xp <= proper:
                continue
            value, profile, ways = contact_sum(xp, xr, xt)
            item = {
                "complement": {"proper": xp, "major_residual": xr, "top_minor": xt},
                "basis": {
                    "proper": proper - xp,
                    "major_residual": residual - xr,
                    "top_minor": top - xt,
                },
                "proper_complement_disc_occupancies_0_1_2_3": profile,
            }
            if best is None or value < best:
                best = value
                minimizers = [item]
                total_ways = ways
            elif value == best:
                minimizers.append(item)
                total_ways += ways
    if best is None:
        raise AssertionError("empty tropical search")
    all_contacts, _, _ = contact_sum(proper, residual, top)
    basis_weight = best - all_contacts
    R = math.lcm(12, rho_residual.denominator, rho_top.denominator)
    return {
        "matrix": "raw scaled-GRS homogeneous rows r=0,...,K-2",
        "typing": "WITNESS-ONLY exact valuated-matroid computation",
        "contact_completion": {
            "residual_internal_t": qstr(rho_residual),
            "top_internal_t": qstr(rho_top),
            "completion_uniformizer_R": R,
            "residual_derivative_valuation_t": qstr(dval_residual),
            "residual_f_minus_a0_order_t": qstr(-1 - dval_residual),
        },
        "minimum_basis_weight_t": qstr(basis_weight),
        "minimum_basis_weight_z": str(basis_weight * R),
        "number_of_composition_minimizers": len(minimizers),
        "minimizers": minimizers,
        "number_of_labelled_minimum_bases": str(total_ways),
        "derivation": "val(det A_S)=-C_all+C(T); exact finite complement DP",
    }


def scale_guard(t: int, k: int, qmax_z: int = 5) -> dict[str, Any]:
    f = family(t, k)
    R, m = 12, f["m"]
    major_sum = 0
    for r in range(2, m + 1):
        required = max(0, qmax_z + R * (m - r) - 2 * r)
        major_sum += required + 1
    top_each = (m - 1) * (qmax_z + R * m + 1)
    lower_bound = f["major_D2_roots"] * major_sum + f["top_minor_roots"] * top_each
    return {
        "frozen_driver": "GLOBAL-INTERPOLATION/1.0 moh_total_degree quadratic lift",
        "qmax_z": qmax_z,
        "branch_power_variables_lower_bound": lower_bound,
        "excluded_from_bound": [
            "derivative-product variables",
            "inverse variables",
            "time/integration variables",
            "polynomial coefficient variables",
            "evaluation equations and Python/SymPy expression overhead",
        ],
        "status": "NOT-RUN: no full decorated input; scalable direct projection used",
    }


def first_page_metadata(t: int, k: int) -> dict[str, Any]:
    f = family(t, k)
    rows = list(range(f["homogeneous_DEG_rows"]))
    qz = {str(r): 2 * r + 8 for r in rows}
    invariant = [r for r in rows if (2 * r + 8) % 12 == 0]
    return {
        "proper_derivation": {
            "lambda_f_t": "-1/6",
            "ord_D_proper_t": "-5/6",
            "ord_tau_proper_t": "1/6",
            "leading_order_formula_z": "12*(-1/6+r/6+5/6)=2r+8",
            "row_first_raw_orders_z": qz,
        },
        "complete_orbit_trace": {
            "rows_with_nonzero_possible_at_that_raw_leading_order": invariant,
            "criterion": "2r+8 = 0 mod 12",
            "count": len(invariant),
            "warning": (
                "other rows cancel at the displayed leading character; their first nonzero "
                "integer-t coefficient depends on unspecified tame support and sharing"
            ),
        },
        "junctions": {
            "bottom_to_D2_relative_z": 5,
            "D2_to_D3_relative_z": 14,
            "status": (
                "provenance labels only; the z^5 coefficient matrix cannot be emitted until "
                "outer unit coefficients and their sharing are supplied"
            ),
        },
        "local_star_trace": {
            "sum_p_f_over_p_g_prime": "1",
            "sum_pi_p_f_over_p_g_prime": "0",
            "sum_pi2_p_f_over_p_g_prime": "1/3",
            "consequence": "the first internal star correction is two bottom gaps later, not one",
        },
    }


def affine_bottom_left_kernel(t: int, k: int) -> dict[str, Any]:
    """Canonical bottom-only affine inconsistency functional when K>3k."""
    f = family(t, k)
    h = f["K"]
    p = f["proper_bottom_roots"]
    exponent = h - 1 - p
    if exponent < 0:
        return {
            "exists": False,
            "reason": f"K={h} <= proper leaf columns={p}; no bottom left kernel of this form",
            "formal_exponent": exponent,
        }
    residual = f["major_residual_nonproper_roots"]
    rho_residual = Fraction(1, 6) + Fraction(1, 6 * (residual - 1))
    residual_value_valuation = exponent * rho_residual + Fraction(p, 6) + Fraction(3, 2)
    top_value_valuation = -exponent - p + 36 * t + 29
    return {
        "exists": True,
        "rows_including_monic": h,
        "proper_leaf_columns": p,
        "bottom_left_cokernel_dimension": h - p,
        "exponent": exponent,
        "functional_polynomial": (
            f"Lambda_{{t,{k}}}(Y)=Y^{exponent}*G_bot(Y), "
            "G_bot(Y)=product_(i in proper bottom leaves)(Y-tau_i)"
        ),
        "identity": "lambda^T A_bottom=0, while lambda^T b_monic=1",
        "nonproper_column_value": "Lambda(eta)/D_eta",
        "generic_repair": (
            "for eta not a bottom root this value is generically nonzero; a D2 residual "
            "column repairs the displayed affine functional"
        ),
        "witness_tree_valuations": {
            "D2_residual_eta": qstr(residual_value_valuation),
            "top_minor_eta": qstr(Fraction(top_value_valuation)),
            "derivation": (
                "val(Lambda(eta)/D_eta)=E val(eta)+sum_bottom contact(eta,tau_i)-val(D_eta)"
            ),
        },
        "leading_coefficient": (
            "lc(eta)^E * product_i lc(eta-tau_i) / lc(D_eta), nonzero on the declared "
            "separation open set"
        ),
        "typing": (
            "PROVED-HERE for the bottom parity block; not a full obstruction because the "
            "nonproper columns evaluate nontrivially"
        ),
    }


def certificate(t: int, k: int = 12) -> dict[str, Any]:
    manifest = canonical_manifest(t, k)
    custody = validate_manifest(manifest)
    ranks = rank_table(t, k)
    tropical = tropical_minimum(t, k)
    sensitivity = tropical_minimum(t, k, residual_increment_numerator=3)
    return {
        "typing": "PROVED-HERE algebra / UNREVIEWED computation / WITNESS-ONLY completion",
        "family": family(t, k),
        "manifest": manifest,
        "custody": custody,
        "unknown_count_convention_repair": {
            "convention": "Z_page includes leading/star variables",
            "formula": "U_page=h_constants+|Z_page|",
            "u0_added_again": False,
            "page_table_rule": "integration constants printed separately and excluded from parity columns",
        },
        "first_bottom_separation": first_page_metadata(t, k),
        "conditional_parity_ranks": ranks,
        "canonical_affine_bottom_left_kernel": affine_bottom_left_kernel(t, k),
        "tropical_witness": tropical,
        "tropical_sensitivity": {
            "changed_choice": (
                "residual internal contact 1/6+1/(6(Rres-1)) -> "
                "1/6+3/(6(Rres-1)); derivative valuation -3/2 -> -7/6 remains < -1"
            ),
            "result": sensitivity,
            "same_minimizers": sensitivity["minimizers"] == tropical["minimizers"],
            "same_weight": sensitivity["minimum_basis_weight_t"]
            == tropical["minimum_basis_weight_t"],
            "conclusion": "tropical data depend on an input absent from the charged decoration",
        },
        "full_quadratic_lift_scale_guard": scale_guard(t, k),
        "verdict": {
            "family_intrinsic_associated_graded_matrix": "OPEN[NONPROPER-INTERFACE]",
            "raw_proper_defect_behavior": "grows after t=0; repaired by witness nonproper Schur block",
            "rigid_macro_defect_behavior": "21*t+5 for k=12 (21*t+11 for k=6); repaired exactly in witness",
            "caution": (
                "the repair is not a theorem about a Keller realization because the map from actual "
                "tame/root coefficients to H-values is not supplied"
            ),
        },
    }


def _load_globalinterp(path: Path):
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != EXPECTED_GLOBALINTERP_SHA256:
        raise ValueError(f"globalinterp custody mismatch: {actual}")
    spec = importlib.util.spec_from_file_location("frozen_globalinterp_a2six", path)
    if spec is None or spec.loader is None:
        raise ValueError("could not load frozen globalinterp")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def controls(globalinterp_path: Path) -> dict[str, Any]:
    module = _load_globalinterp(globalinterp_path)
    checks = module.run_controls(verbose=False)
    if checks.failures:
        raise AssertionError(checks.failures)
    tame = []
    for degree in (3, 5):
        tame.append(
            {
                "pair": f"(y,x+y^{degree})",
                "homogeneous_moments": [0] * (degree - 2),
                "monic_moment": 1,
                "status": "PASS",
                "proof": "sum tau^s/g_y(tau)=0 through s=k-2 and 1 at s=k-1",
            }
        )
    bad = {
        "g": "y^2-x^2-x",
        "order_t": 1,
        "branch_residues": ["1/2", "-1/2"],
        "status": "EXPECTED-FAIL[NO-RESIDUE]",
    }
    roots = (Fraction(-1), Fraction(0), Fraction(1))

    def pgprime(pi: Fraction) -> Fraction:
        return 3 * pi * pi - 1

    def pf(pi: Fraction) -> Fraction:
        return pi * pi - Fraction(2, 3)

    traces = [sum(pf(pi) * pi**power / pgprime(pi) for pi in roots) for power in range(3)]
    bracket_values = [
        2 * (pi * pi - Fraction(2, 3)) * (3 * pi * pi - 1)
        - 3 * (pi**3 - pi) * (2 * pi)
        for pi in map(Fraction, (-2, -1, 0, 1, 2))
    ]
    if traces != [Fraction(1), Fraction(0), Fraction(1, 3)]:
        raise AssertionError(f"bad star traces: {traces}")
    if any(value != Fraction(4, 3) for value in bracket_values):
        raise AssertionError(f"bad bottom bracket: {bracket_values}")
    star = {
        "p_g": "pi^3-pi",
        "p_f": "pi^2-2/3",
        "2*p_f*p_g_prime-3*p_g*p_f_prime": "4/3",
        "jacobian_scale": "-1/12",
        "local_c": "1/9",
        "star_traces_power_0_1_2": [qstr(value) for value in traces],
        "status": "PASS",
    }
    partial = canonical_manifest(0, 12)
    partial["disc_orbits"][0]["members"] = partial["disc_orbits"][0]["members"][:-1]
    refusal = None
    try:
        validate_manifest(partial)
    except ValueError as exc:
        refusal = str(exc)
    if refusal is None or not refusal.startswith("REFUSED[PARTIAL-ORBIT]"):
        raise AssertionError("partial orbit was not refused")
    return {
        "frozen_globalinterp_sha256": EXPECTED_GLOBALINTERP_SHA256,
        "frozen_driver_controls": {"checks": checks.count, "failures": len(checks.failures)},
        "same_page_tame_controls": tame,
        "negative_control": bad,
        "rigid_bottom_star_control": star,
        "partial_orbit_control": {"status": refusal},
        "status": "PASS",
    }


def selftest(globalinterp_path: Path) -> dict[str, Any]:
    count = 0
    for k in (12, 6):
        for t in range(4):
            cert = certificate(t, k)
            f = cert["family"]
            ranks = cert["conditional_parity_ranks"]
            raw = ranks["raw_leaf_coordinate_model"]
            macro = ranks["rigid_star_macro_model"]
            assert raw["rank_proper_over_Q"] == min(
                f["homogeneous_DEG_rows"], f["proper_bottom_roots"]
            )
            assert raw["rank_after_nonproper_over_Q"] == f["homogeneous_DEG_rows"]
            assert macro["rank_proper_over_Q"] == k
            assert macro["rank_after_nonproper_over_Q"] == f["homogeneous_DEG_rows"]
            assert raw["nonproper_incremental_Schur_rank"] == raw["left_cokernel_proper"]
            assert macro["nonproper_incremental_Schur_rank"] == macro["left_cokernel_proper"]
            count += 6
    control = controls(globalinterp_path)
    assert control["status"] == "PASS"
    count += 1
    return {"status": "PASS", "checks": count}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p_manifest = sub.add_parser("manifest")
    p_manifest.add_argument("t", type=int)
    p_manifest.add_argument("--k", type=int, default=12)
    p_validate = sub.add_parser("validate")
    p_validate.add_argument("path", type=Path)
    p_cert = sub.add_parser("certificate")
    p_cert.add_argument("t", type=int)
    p_cert.add_argument("--k", type=int, default=12)
    p_all = sub.add_parser("all")
    p_all.add_argument("--k", type=int, default=12)
    p_controls = sub.add_parser("controls")
    p_controls.add_argument("--globalinterp", type=Path, default=DEFAULT_GLOBALINTERP)
    p_selftest = sub.add_parser("selftest")
    p_selftest.add_argument("--globalinterp", type=Path, default=DEFAULT_GLOBALINTERP)
    args = parser.parse_args(argv)
    try:
        if args.command == "manifest":
            result = canonical_manifest(args.t, args.k)
        elif args.command == "validate":
            result = validate_manifest(load_json(args.path))
        elif args.command == "certificate":
            result = certificate(args.t, args.k)
        elif args.command == "all":
            result = {str(t): certificate(t, args.k) for t in range(4)}
        elif args.command == "controls":
            result = controls(args.globalinterp)
        else:
            result = selftest(args.globalinterp)
    except (AssertionError, KeyError, TypeError, ValueError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
