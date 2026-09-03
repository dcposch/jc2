#!/usr/bin/env python3
"""Fail-closed custody and scalable first-page diagnostics for FIXED-N6.

This wrapper does not infer a Puiseux decoration from a Moh skeleton.  Its
``certificate`` command uses one fully declared combinatorial completion,
labelled WITNESS-ONLY in the output.  The completion is useful for checking
matrix scaling and for proving that the requested ranks are not intrinsic to
the numerical skeleton.

The frozen GLOBAL-INTERPOLATION/1.0 emitter accepts ``verified: true`` as an
assertion and does not validate orbit size or a Galois permutation.  The
``validate`` command below is therefore a required custody preflight.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


GOOD_PRIMES = (1009, 1013, 1019)


def choose2(n: int) -> int:
    return n * (n - 1) // 2


def family(L: int) -> dict[str, int | str]:
    if L < 5 or L % 8 != 5:
        raise ValueError("family parameter must satisfy L >= 5 and L = 5 mod 8")
    n = 21 * L
    m = 14 * L
    K = 7 * L
    k = 3 * (5 * L - 1) // 4
    R = math.lcm(12, k)
    delta2 = Fraction(2 * (3 * L - 1), 3 * (5 * L - 1))
    q2 = delta2 * R
    q1 = Fraction(7, 12) * R
    assert q1.denominator == q2.denominator == 1
    proper = 3 * k
    major_total = 15 * L
    major_residual = major_total - proper
    top_minor = 6 * L
    nonproper = major_residual + top_minor
    assert nonproper == 3 * (K - k)
    return {
        "L": L,
        "n": n,
        "m": m,
        "K": K,
        "vanishing_rows": K - 1,
        "degree_rows_with_monic": K,
        "A2": k,
        "k": k,
        "N": str(Fraction(k, 2)),
        "R": R,
        "delta3": "-1",
        "delta2": str(delta2),
        "delta1": "7/12",
        "q3_z": -R,
        "q2_z": int(q2),
        "q1_z": int(q1),
        "first_bottom_gap_z": int(q1 - q2),
        "major_total": major_total,
        "proper": proper,
        "major_residual": major_residual,
        "top_minor": top_minor,
        "nonproper": nonproper,
    }


def canonical_manifest(L: int, requested_k: int | None = None) -> dict:
    f = family(L)
    k = int(f["k"] if requested_k is None else requested_k)
    members = [f"D1_{j:03d}" for j in range(k)]
    generator = {members[j]: members[(j + 1) % k] for j in range(k)} if k else {}
    return {
        "schema": "FIXED-N6-DECORATION/1",
        "typing": "WITNESS-ONLY / UNREVIEWED",
        "family_L": L,
        "single_orbit": True,
        "packet": {
            "kind": "nonzero-(10)",
            "expected_size": k,
            "members": members,
            "generator": generator,
            "V2": 1,
            "bottom_star": {
                "p_g": "pi^3-pi",
                "p_f": "pi^2-2/3",
            },
        },
        "root_blocks": {
            "major_D2_total": int(f["major_total"]),
            "proper_bottom_roots": 3 * k,
            "major_residual_roots": int(f["major_total"]) - 3 * k,
            "top_minor_roots": int(f["top_minor"]),
            "total_nonproper_roots": int(f["n"]) - 3 * k,
        },
        "extra_completion_choices": {
            "status": "not implied by the skeleton or rigid bottom stars",
            "major_residual_subclusters": [
                {
                    "size": int(f["major_total"]) - 3 * k,
                    "centre_at_D2": "0",
                    "first_internal_contact_t": "delta2+1/(6*A2), strictly between delta2 and 2/5",
                    "leading_coefficients": "distinct labels in the valuation-only surrogate",
                }
            ],
            "top_minor_subclusters": [
                {
                    "size": int(f["top_minor"]),
                    "centre_at_D3": "1*t^-1",
                    "first_internal_contact_t": "2",
                    "leading_coefficients": "distinct rational labels",
                }
            ],
            "proper_disc_centres": "one cyclotomic orbit at t^delta2",
            "proper_internal_coordinates": "0,+1,-1 after discwise normalization at t^(7/12)",
            "galois_action": "z -> xi_R*z is supplied only on the displayed proper-disc k-cycle",
            "coefficient_sharing": "proper packet sharing is explicit; nonproper sharing is deliberately unspecified",
            "guard": "valuation-only nonproper surrogate; not a complete globalinterp branch input and no claim of POLY, NO-RESIDUE, or a polynomial g",
        },
    }


def validate_manifest(data: dict) -> dict:
    if data.get("schema") != "FIXED-N6-DECORATION/1":
        raise ValueError("REFUSED[SCHEMA]: missing FIXED-N6-DECORATION/1")
    f = family(int(data["family_L"]))
    packet = data.get("packet", {})
    if data.get("single_orbit") is not True:
        raise ValueError("REFUSED[ORBIT-TYPE]: the proper packet must be one complete orbit")
    if packet.get("kind") != "nonzero-(10)" or packet.get("V2") != 1:
        raise ValueError("REFUSED[PACKET-TYPE]: expected a nonzero (10)-packet with V2=1")
    if packet.get("bottom_star") != {"p_g": "pi^3-pi", "p_f": "pi^2-2/3"}:
        raise ValueError(
            "REFUSED[BOTTOM-STAR]: expected p_g=pi^3-pi and p_f=pi^2-2/3"
        )
    expected = packet.get("expected_size")
    members = list(packet.get("members", []))
    generator = dict(packet.get("generator", {}))
    if not isinstance(expected, int) or expected <= 0:
        raise ValueError("REFUSED[PARTIAL-ORBIT]: expected_size must be a positive integer")
    if len(members) != len(set(members)) or len(members) != expected:
        raise ValueError(
            f"REFUSED[PARTIAL-ORBIT]: expected {expected} distinct members, got {len(set(members))}"
        )
    member_set = set(members)
    if set(generator) != member_set or set(generator.values()) != member_set:
        raise ValueError("REFUSED[PARTIAL-ORBIT]: generator is not a permutation of the members")
    seen: list[str] = []
    current = members[0]
    while current not in seen:
        seen.append(current)
        current = generator[current]
    if current != members[0] or len(seen) != expected:
        raise ValueError(
            f"REFUSED[PARTIAL-ORBIT]: generator has a cycle of length {len(seen)}, expected {expected}"
        )
    required = int(f["A2"])
    if expected != required:
        raise ValueError(
            f"REFUSED[ORBIT-SIZE]: L={f['L']} has (10)-orbit size A2={required}; requested k={expected}"
        )
    blocks = data.get("root_blocks", {})
    expected_blocks = {
        "major_D2_total": int(f["major_total"]),
        "proper_bottom_roots": 3 * expected,
        "major_residual_roots": int(f["major_total"]) - 3 * expected,
        "top_minor_roots": int(f["top_minor"]),
        "total_nonproper_roots": int(f["n"]) - 3 * expected,
    }
    for key, value in expected_blocks.items():
        if blocks.get(key) != value:
            raise ValueError(
                f"REFUSED[ROOT-COUNT]: {key}={blocks.get(key)!r}, expected {value}"
            )
    return {
        "status": "ACCEPTED[PROPER-PACKET-CUSTODY-ONLY]",
        "full_globalinterp_decoration": False,
        "missing_for_full_decoration": [
            "explicit nonproper Puiseux coefficients",
            "complete Galois permutation on all n leaves",
            "tail support and coefficient sharing",
            "precision guard",
        ],
        "family": f,
        "orbit_cycle_length": len(seen),
        "root_blocks": expected_blocks,
    }


def modular_rank(matrix: list[list[int]], p: int) -> int:
    if not matrix:
        return 0
    a = [[entry % p for entry in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(v * inv) % p for v in a[rank]]
        for r in range(rows):
            if r != rank and a[r][col]:
                factor = a[r][col]
                a[r] = [(u - factor * v) % p for u, v in zip(a[r], a[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def confluent_proper_matrix(L: int, p: int) -> list[list[int]]:
    """Rows 0..7L-2; three normalized jets at each rational centre 1..k."""
    f = family(L)
    h, k = int(f["vanishing_rows"]), int(f["k"])
    out: list[list[int]] = []
    for r in range(h):
        row: list[int] = []
        for centre in range(1, k + 1):
            for jet in range(3):
                value = 0 if r < jet else math.comb(r, jet) * pow(centre, r - jet, p)
                row.append(value % p)
        out.append(row)
    return out


def collapsed_matrix(L: int, p: int, add_nonproper: bool) -> list[list[int]]:
    """One rigid-star channel per disc; optionally active residual leaves and top aggregate."""
    f = family(L)
    h, k = int(f["vanishing_rows"]), int(f["k"])
    centres = list(range(1, k + 1))
    if add_nonproper:
        centres.extend(range(k + 1, k + int(f["major_residual"]) + 1))
        centres.append(0)
    return [[pow(c, r, p) for c in centres] for r in range(h)]


def proper_pivot_allocation(L: int) -> list[int]:
    """A square confluent-Vandermonde pivot using only proper columns."""
    f = family(L)
    h, k = int(f["vanishing_rows"]), int(f["k"])
    assert k <= h <= 2 * k
    return [2] * (h - k) + [1] * (2 * k - h)


def proper_pivot_certificate(L: int) -> dict:
    alloc = proper_pivot_allocation(L)
    exponent_by_difference: dict[int, int] = {}
    k = len(alloc)
    for i in range(k):
        for j in range(i + 1, k):
            exponent_by_difference[j - i] = exponent_by_difference.get(j - i, 0) + alloc[i] * alloc[j]
    residues = {}
    for p in GOOD_PRIMES:
        det = 1
        for difference, exponent in exponent_by_difference.items():
            det = det * pow(difference, exponent, p) % p
        residues[str(p)] = det
    return {
        "allocation_by_disc": {
            "two_jets": sum(a == 2 for a in alloc),
            "one_jet": sum(a == 1 for a in alloc),
            "zero_jets": 0,
        },
        "determinant_factorization": "prod_(i<j) (j-i)^(a_i*a_j)",
        "determinant_nonzero_over_Q": True,
        "determinant_mod_good_primes": residues,
    }


def balanced_internal_pairs(selected: int, clusters: int) -> tuple[int, tuple[int, int, int, int], int]:
    """Minimize sum C(a_i,2), 0<=a_i<=3, sum a_i=selected."""
    if not 0 <= selected <= 3 * clusters:
        raise ValueError("selected proper leaves exceed capacity")
    base, extra = divmod(selected, clusters)
    assert 0 <= base <= 3 and base + bool(extra) <= 3
    counts = [0, 0, 0, 0]
    counts[base] = clusters - extra
    if extra:
        counts[base] -= 0
        counts[base + 1] = extra
    pair_count = (clusters - extra) * choose2(base) + extra * choose2(base + 1)
    choices = math.comb(clusters, extra)
    choices *= math.comb(3, base) ** (clusters - extra)
    if extra:
        choices *= math.comb(3, base + 1) ** extra
    return pair_count, tuple(counts), choices


def tropical_minimum(
    L: int,
    rho_major: Fraction | None = None,
    rho_top: Fraction = Fraction(2),
) -> dict:
    """Minimum basis weight of the WITNESS-ONLY scaled GRS parity matrix.

    A basis S has weight val(det(V_S/prod D_i)).  If T is its complement,
    this is -C_all + sum_{i<j in T} contact(i,j), so the finite search is over
    the three declared cluster types.
    """
    f = family(L)
    h = int(f["vanishing_rows"])
    pcount = int(f["proper"])
    rcount = int(f["major_residual"])
    tcount = int(f["top_minor"])
    k = int(f["k"])
    complement_size = int(f["n"]) - h
    d3, d2, d1 = Fraction(-1), Fraction(f["delta2"]), Fraction(7, 12)
    if rho_major is None:
        rho_major = d2 + Fraction(1, 6 * k)
    if not d2 < rho_major < Fraction(2, 5):
        raise ValueError("major-residual nonproper witness requires delta2 < rho_major < 2/5")
    if not d3 < rho_top < Fraction(15 * L - 1, 6 * L - 1):
        raise ValueError("top-minor nonproper witness requires -1 < rho_top < (15L-1)/(6L-1)")

    def contact_sum(xp: int, xr: int, xt: int) -> tuple[Fraction, tuple[int, int, int, int], int]:
        internal_pairs, distribution, proper_choices = balanced_internal_pairs(xp, k)
        major = xp + xr
        value = d2 * choose2(major)
        value += (d1 - d2) * internal_pairs
        value += (rho_major - d2) * choose2(xr)
        value += rho_top * choose2(xt)
        value += d3 * xt * major
        ways = proper_choices * math.comb(rcount, xr) * math.comb(tcount, xt)
        return value, distribution, ways

    best: Fraction | None = None
    minimizers: list[dict] = []
    total_ways = 0
    for xt in range(tcount + 1):
        for xr in range(rcount + 1):
            xp = complement_size - xt - xr
            if not 0 <= xp <= pcount:
                continue
            value, distribution, ways = contact_sum(xp, xr, xt)
            item = {
                "complement": {"proper": xp, "major_residual": xr, "top_minor": xt},
                "basis": {
                    "proper": pcount - xp,
                    "major_residual": rcount - xr,
                    "top_minor": tcount - xt,
                },
                "proper_complement_disc_occupancies_0_1_2_3": list(distribution),
            }
            if best is None or value < best:
                best = value
                minimizers = [item]
                total_ways = ways
            elif value == best:
                minimizers.append(item)
                total_ways += ways

    assert best is not None
    all_contacts, _, _ = contact_sum(pcount, rcount, tcount)
    basis_weight = -all_contacts + best
    witness_R = math.lcm(int(f["R"]), rho_major.denominator, rho_top.denominator)
    return {
        "matrix": "raw scaled GRS rows r=0..7L-2, columns all roots",
        "extra_nonproper_contacts": {
            "major_residual_internal_t": str(rho_major),
            "top_minor_internal_t": str(rho_top),
        },
        "completion_uniformizer_denominator": witness_R,
        "completion_bottom_orders_z": {
            "delta2": str(d2 * witness_R),
            "delta1": str(d1 * witness_R),
            "gap": str((d1 - d2) * witness_R),
        },
        "nonproper_checks": {
            "major_residual_derivative_valuation_t": str(
                (rcount - 1) * rho_major + pcount * d2 - 6 * L
            ),
            "major_residual_frontier_gt_1": (
                (rcount - 1) * rho_major + pcount * d2 - 6 * L < -1
            ),
            "top_minor_derivative_valuation_t": str((tcount - 1) * rho_top - 15 * L),
            "top_minor_frontier_gt_1": (tcount - 1) * rho_top - 15 * L < -1,
        },
        "minimum_basis_weight_t": str(basis_weight),
        "minimum_basis_weight_z": str(basis_weight * witness_R),
        "number_of_composition_minimizers": len(minimizers),
        "minimizers": minimizers,
        "number_of_labelled_minimum_bases": str(total_ways),
        "derivation": "w(S)=-C_all+C(T); exact DP over the complement T",
    }


def certificate(L: int) -> dict:
    manifest = canonical_manifest(L)
    custody = validate_manifest(manifest)
    f = family(L)
    h, k = int(f["vanishing_rows"]), int(f["k"])
    # In GLOBAL-INTERPOLATION/1.0, a branch with valuation -R gets
    # desired_power[r] >= R*m already at qmax >= 0 in moh_total_degree mode.
    # This is a lower bound from top-minor branches and branch-power variables
    # alone; it excludes product, inverse, time, and evaluation variables.
    globalinterp_power_variable_lower_bound = (
        int(f["top_minor"]) * (int(f["m"]) - 1) * (int(f["R"]) * int(f["m"]) + 1)
    )
    prime_ranks = {}
    for p in GOOD_PRIMES:
        raw = confluent_proper_matrix(L, p)
        collapsed = collapsed_matrix(L, p, add_nonproper=False)
        collapsed_np = collapsed_matrix(L, p, add_nonproper=True)
        prime_ranks[str(p)] = {
            "raw_proper_confluent": modular_rank(raw, p),
            "rigid_star_collapsed_proper": modular_rank(collapsed, p),
            "rigid_star_collapsed_plus_active_nonproper_surrogate": modular_rank(collapsed_np, p),
        }
    raw_rank = h
    collapsed_rank = k
    active_nonproper = int(f["major_residual"]) + 1
    collapsed_np_rank = min(h, k + active_nonproper)
    return {
        "typing": "WITNESS-ONLY / PROVED-HERE algebra / UNREVIEWED computation",
        "not_family_intrinsic": (
            "The skeleton, packet size and rigid stars do not determine nonproper contacts, "
            "branch tails, primitive-coordinate sharing, or a first-page filtration."
        ),
        "manifest": manifest,
        "custody": custody,
        "frozen_globalinterp_scale_guard": {
            "qmax_assumption": "qmax >= 0",
            "branch_power_variables_lower_bound": globalinterp_power_variable_lower_bound,
            "derivation": "top_minor*(m-1)*(R*m+1)",
            "status": "REFUSED[RESOURCE-CAP] for the full quadratic lift; use the scalable parity projection",
        },
        "first_page": {
            "homogeneous_DEG_equations": h,
            "raw_leaf_coordinate_model": {
                "unknowns_proper": int(f["proper"]),
                "equations": h,
                "rank_over_Q": raw_rank,
                "cokernel": h - raw_rank,
                "nonproper_incremental_Schur_rank": 0,
                "explanation": "proper confluent Vandermonde already has full row rank",
                "prime_ranks": prime_ranks,
                "pivot": proper_pivot_certificate(L),
            },
            "rigid_star_collapsed_surrogate": {
                "unknowns_proper": k,
                "equations": h,
                "rank_over_Q": collapsed_rank,
                "cokernel": h - collapsed_rank,
                "active_nonproper_columns": active_nonproper,
                "nonproper_block_rank_over_Q": min(h, active_nonproper),
                "rank_with_those_columns": collapsed_np_rank,
                "cokernel_with_those_columns": h - collapsed_np_rank,
                "nonproper_incremental_Schur_rank": collapsed_np_rank - collapsed_rank,
                "qualification": "one amplitude per rigid star, one channel per residual leaf split before delta1, and one unresolved top-minor aggregate",
            },
        },
        "tropical_raw_GRS": tropical_minimum(L),
        "tropical_sensitivity_witness": {
            "changed_extra_choice": "top-minor internal contact t^2 -> t^(5/2)",
            "result": tropical_minimum(L, rho_top=Fraction(5, 2)),
            "conclusion": "minimum basis data are not determined by the charged decoration",
        },
    }


def compact_certificate(L: int) -> dict:
    """Stable, bounded record used by ``all`` and witness-results.json."""
    full = certificate(L)
    page = full["first_page"]
    return {
        "typing": full["typing"],
        "custody": full["custody"],
        "family": full["custody"]["family"],
        "frozen_globalinterp_scale_guard": full["frozen_globalinterp_scale_guard"],
        "raw_leaf_coordinate_model": page["raw_leaf_coordinate_model"],
        "rigid_star_collapsed_surrogate": page["rigid_star_collapsed_surrogate"],
        "tropical_raw_GRS": full["tropical_raw_GRS"],
        "tropical_alternative_top_contact_5_2": full["tropical_sensitivity_witness"]["result"],
    }


def load(path: str) -> dict:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def exact_parity_moment(nodes: list[int], exponent: int) -> Fraction:
    """Evaluate one consecutive GRS moment exactly at distinct Q-nodes."""
    total = Fraction(0)
    for i, node in enumerate(nodes):
        derivative = math.prod(node - other for j, other in enumerate(nodes) if i != j)
        total += Fraction(node**exponent, derivative)
    return total


def page_controls() -> dict:
    """Exact controls for the same direct consecutive-moment projection.

    For g=x+y^k-c2 and H=tau (Jacobian -1), the page entries are
    sum tau_i^(r+1)/g_y(tau_i).  The monic-root identity makes all
    homogeneous rows zero and the following monic row one.  The negative
    fixture records the exact coefficient of t=x^-1 in 1/g_y.
    """
    tame = []
    for degree in (3, 5):
        # A rational specialization of the universal monic-root identity
        # exercises the same consecutive parity matrix without radicals.
        nodes = list(range(1, degree + 1))
        homogeneous_q = [exact_parity_moment(nodes, r + 1) for r in range(degree - 2)]
        monic_q = exact_parity_moment(nodes, degree - 1)
        assert all(value == 0 for value in homogeneous_q)
        assert monic_q == 1
        homogeneous = [int(value) for value in homogeneous_q]
        monic = int(monic_q)
        tame.append(
            {
                "pair": f"(y,x+y^{degree})",
                "homogeneous_moment_indices": list(range(degree - 2)),
                "homogeneous_values": homogeneous,
                "monic_moment_index": degree - 2,
                "monic_value": monic,
                "no_residue": True,
                "status": "PASS",
                "proof": "sum tau_i^s/h'(tau_i)=0 for s<=k-2 and 1 for s=k-1",
                "exact_matrix_specialization": f"nodes=1,...,{degree} over Q",
            }
        )
    negative = {
        "g": "y^2-x^2-x",
        "order_t": 1,
        "residues": ["1/2", "-1/2"],
        "status": "EXPECTED-FAIL[NO-RESIDUE]",
    }
    return {
        "projection": "direct consecutive moment/parity page",
        "tame": tame,
        "negative": negative,
        "status": "PASS",
        "qualification": "controls the scalable raw projection; a full decorated family initial-form emitter remains OPEN",
    }


def selftest() -> dict:
    checks = 0
    for L in (5, 13, 21, 29):
        c = certificate(L)
        f = c["custody"]["family"]
        h = int(f["vanishing_rows"])
        k = int(f["k"])
        raw = c["first_page"]["raw_leaf_coordinate_model"]
        collapsed = c["first_page"]["rigid_star_collapsed_surrogate"]
        assert raw["rank_over_Q"] == h and raw["cokernel"] == 0
        checks += 1
        assert collapsed["rank_over_Q"] == k
        assert collapsed["nonproper_incremental_Schur_rank"] == h - k
        assert collapsed["rank_with_those_columns"] == h
        checks += 1
        for ranks in raw["prime_ranks"].values():
            assert ranks["raw_proper_confluent"] == h
            assert ranks["rigid_star_collapsed_proper"] == k
            assert ranks["rigid_star_collapsed_plus_active_nonproper_surrogate"] == h
            checks += 1
        np_checks = c["tropical_raw_GRS"]["nonproper_checks"]
        assert np_checks["major_residual_frontier_gt_1"]
        assert np_checks["top_minor_frontier_gt_1"]
        checks += 1
        assert (
            c["tropical_raw_GRS"]["minimizers"]
            != c["tropical_sensitivity_witness"]["result"]["minimizers"]
        )
        checks += 1
    try:
        validate_manifest(canonical_manifest(5, requested_k=12))
    except ValueError as exc:
        assert str(exc).startswith("REFUSED[ORBIT-SIZE]")
        checks += 1
    else:
        raise AssertionError("partial orbit k=12 was not refused")
    controls = page_controls()
    assert controls["status"] == "PASS"
    assert all(item["status"] == "PASS" for item in controls["tame"])
    assert controls["negative"]["status"] == "EXPECTED-FAIL[NO-RESIDUE]"
    checks += 3
    return {"status": "PASS", "checks": checks}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    p_manifest = sub.add_parser("manifest")
    p_manifest.add_argument("L", type=int)
    p_manifest.add_argument("--k", type=int)
    p_validate = sub.add_parser("validate")
    p_validate.add_argument("path")
    p_cert = sub.add_parser("certificate")
    p_cert.add_argument("L", type=int)
    sub.add_parser("all")
    sub.add_parser("controls")
    sub.add_parser("selftest")
    args = parser.parse_args(argv)
    try:
        if args.command == "manifest":
            result = canonical_manifest(args.L, args.k)
        elif args.command == "validate":
            result = validate_manifest(load(args.path))
        elif args.command == "certificate":
            result = certificate(args.L)
        elif args.command == "selftest":
            result = selftest()
        elif args.command == "controls":
            result = page_controls()
        else:
            result = {str(L): compact_certificate(L) for L in (5, 13, 21, 29)}
    except (KeyError, TypeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
