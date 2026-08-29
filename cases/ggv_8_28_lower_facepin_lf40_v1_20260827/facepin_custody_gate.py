#!/usr/bin/env python3
"""Desk-scale exact custody gate for the reviewed actual-GGV lower FACEPIN."""

from __future__ import annotations

from math import comb, gcd
from pathlib import Path
import shutil
import sys

from lf40_common import (
    PRIMARY_SOURCE_PINS,
    canonical_bytes,
    fail,
    freeze_directory,
    univariate_add_scaled,
    univariate_derivative,
    univariate_mul,
    univariate_pow,
    verify_source_pins,
    write_json,
)


BiPoly = dict[tuple[int, int], int]


def bi_add_term(poly: BiPoly, exponent: tuple[int, int], coefficient: int) -> None:
    value = poly.get(exponent, 0) + coefficient
    if value:
        poly[exponent] = value
    else:
        poly.pop(exponent, None)


def bi_mul(left: BiPoly, right: BiPoly) -> BiPoly:
    out: BiPoly = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            bi_add_term(out, (i + k, j + ell), a * b)
    return out


def bi_pow(poly: BiPoly, exponent: int) -> BiPoly:
    out: BiPoly = {(0, 0): 1}
    for _ in range(exponent):
        out = bi_mul(out, poly)
    return out


def bi_derivative(poly: BiPoly, axis: int) -> BiPoly:
    out: BiPoly = {}
    for (i, j), coefficient in poly.items():
        degree = (i, j)[axis]
        if degree:
            exponent = (i - 1, j) if axis == 0 else (i, j - 1)
            bi_add_term(out, exponent, degree * coefficient)
    return out


def bi_add(left: BiPoly, right: BiPoly, right_scale: int = 1) -> BiPoly:
    out = dict(left)
    for exponent, coefficient in right.items():
        bi_add_term(out, exponent, right_scale * coefficient)
    return out


def determinant_direct(f: BiPoly, g: BiPoly) -> dict[int, dict[int, int]]:
    jacobian = bi_add(
        bi_mul(bi_derivative(f, 0), bi_derivative(g, 1)),
        bi_mul(bi_derivative(f, 1), bi_derivative(g, 0)),
        -1,
    )
    rows: dict[int, dict[int, int]] = {n: {} for n in range(41)}
    for (p, q), coefficient in jacobian.items():
        row = 17 - 4 * p + q
        if not 0 <= row <= 40:
            fail(("control term outside LF40", p, q, row))
        rows[row][p] = rows[row].get(p, 0) - coefficient
        if rows[row][p] == 0:
            del rows[row][p]
    return rows


def chart_rows(poly: BiPoly, shift: int, ceiling: int) -> dict[int, dict[int, int]]:
    rows: dict[int, dict[int, int]] = {n: {} for n in range(ceiling + 1)}
    for (i, j), coefficient in poly.items():
        row = shift - 4 * i + j
        if not 0 <= row <= ceiling:
            fail(("control chart row out of range", shift, i, j, row))
        rows[row][i] = rows[row].get(i, 0) + coefficient
    return rows


def determinant_recurrence(f: BiPoly, g: BiPoly) -> dict[int, dict[int, int]]:
    f_rows = chart_rows(f, 8, 16)
    g_rows = chart_rows(g, 12, 24)
    out: dict[int, dict[int, int]] = {n: {} for n in range(41)}
    for r, fr in f_rows.items():
        for s, gs in g_rows.items():
            target = out[r + s]
            univariate_add_scaled(target, univariate_mul(univariate_derivative(fr), gs), 12 - s)
            univariate_add_scaled(target, univariate_mul(fr, univariate_derivative(gs)), r - 8)
    return out


def base_polynomial() -> BiPoly:
    # B=x(x*y^4-1)^7, expanded literally.
    return {(q + 1, 4 * q): comb(7, q) * ((-1) ** (7 - q)) for q in range(8)}


def control_pairs() -> dict[str, tuple[BiPoly, BiPoly]]:
    b = base_polynomial()
    b2, b3 = bi_pow(b, 2), bi_pow(b, 3)
    native_f = bi_add(b2, {(1, 0): -1, (0, 8): -1})
    native_g = bi_add(b3, {(2, 2): -2, (0, 12): 1, (1, 15): 1})
    artificial_f = bi_add(b2, {(8, 32): -2, (0, 8): 1})
    artificial_g = bi_add(b3, {(16, 60): -3, (8, 36): 3, (0, 12): -1})
    return {"native_lambda_1": (native_f, native_g), "artificial_D3": (artificial_f, artificial_g)}


def first_nonzero(rows: dict[int, dict[int, int]]) -> int | None:
    return next((row for row in range(41) if rows[row]), None)


def symbolic_face_power(power: int) -> dict[int, tuple[int, int]]:
    # xi^power*(xi-rho)^(7*power): degree -> (integer coefficient, rho power).
    return {
        i: (comb(7 * power, i - power) * ((-1) ** (8 * power - i)), 8 * power - i)
        for i in range(power, 8 * power + 1)
    }


def expand_symbolic_k(power: int) -> dict[int, tuple[int, int]]:
    # Every convolution at fixed xi degree has the same rho degree.
    k = {i: (comb(7, i - 1) * ((-1) ** (8 - i)), 8 - i) for i in range(1, 9)}
    out = {0: (1, 0)}
    for _ in range(power):
        nxt: dict[int, tuple[int, int]] = {}
        for i, (a, ar) in out.items():
            for j, (b, br) in k.items():
                degree, rho_degree = i + j, ar + br
                old = nxt.get(degree)
                if old is not None and old[1] != rho_degree:
                    fail(("nonhomogeneous rho degree", degree))
                nxt[degree] = ((old[0] if old else 0) + a * b, rho_degree)
        out = {i: pair for i, pair in nxt.items() if pair[0]}
    return out


def dtil0_for_k(k: dict[int, int]) -> dict[int, int]:
    f0, g0 = univariate_pow(k, 2), univariate_pow(k, 3)
    out: dict[int, int] = {}
    univariate_add_scaled(out, univariate_mul(univariate_derivative(f0), g0), 12)
    univariate_add_scaled(out, univariate_mul(f0, univariate_derivative(g0)), -8)
    return out


def main() -> int:
    if len(sys.argv) != 3:
        fail("usage: facepin_custody_gate.py SOURCE_ROOT OUTPUT_DIR")
    root = Path(sys.argv[1]).resolve()
    output = Path(sys.argv[2]).resolve()
    if output.exists():
        fail(("output must be fresh", str(output)))
    output.mkdir(parents=True)

    source_hashes = verify_source_pins(root)
    sys.path.insert(0, str(root / "lib"))
    from families import (  # pylint: disable=import-outside-toplevel
        C1,
        Edge,
        chain_dirs_pq,
        chain_path,
        get_complete_chains,
        get_mn_families,
        get_pllc,
        get_starting_edges,
        is_admissible,
        is_simple,
    )

    pllc = get_pllc(25)
    candidates = []
    for edge in get_starting_edges(8, 28, pllc):
        for chain in get_complete_chains(edge, pllc):
            if not is_admissible(chain):
                continue
            for family in get_mn_families(chain.final):
                for family_index in range(10):
                    mn = (family.m0 + family_index * family.d1,
                          family.n0 + family_index * family.d2)
                    if mn == (3, 2):
                        candidates.append((edge, chain, family, family_index))
    if len(candidates) != 1:
        fail(("(3,2) 8_28 chain is not unique", len(candidates)))
    edge, chain, family, family_index = candidates[0]
    if edge != Edge(C1(8, 28), C1(1, 0)):
        fail(("wrong starting edge", edge))
    if chain_path(chain) != ((8, 28), (11 / 4, 7)):
        # Fractions compare exactly to this dyadic rational, but retain an explicit tuple check below.
        if not (chain.final.a == 11 and chain.final.l == 4 and chain.final.b == 7):
            fail(("wrong chain", chain_path(chain)))
    if chain_dirs_pq(chain) != [(4, -1, 3, 4)]:
        fail(("wrong step", chain_dirs_pq(chain)))
    if is_simple(edge):
        fail("8_28 edge unexpectedly classified simple")

    rho_direction, sigma_direction = 4, -1
    gap = rho_direction // gcd(rho_direction, edge.A.l)
    gamma_max = min((edge.A.b - edge.Ap.b) // gap, edge.A.b - 1)
    gamma = chain.final.b
    l1 = edge.A.l * rho_direction // gcd(edge.A.l, rho_direction)
    a1 = (edge.A.a * (l1 // edge.A.l)
          + (gamma - edge.A.b) * (-sigma_direction) * (l1 // rho_direction))
    if (gap, gamma_max, gamma, a1, l1) != (4, 7, 7, 11, 4):
        fail(("generated-corner arithmetic", gap, gamma_max, gamma, a1, l1))
    flipped_a1 = 28 + 4 * (gamma - 8)
    m_lambda = 3 * gamma
    deg_pbar = 3 * (28 - 0) // gap
    if (flipped_a1, m_lambda, deg_pbar) != (24, 21, 21):
        fail(("full-root bridge", flipped_a1, m_lambda, deg_pbar))

    square_expanded = expand_symbolic_k(2)
    cube_expanded = expand_symbolic_k(3)
    if square_expanded != symbolic_face_power(2) or cube_expanded != symbolic_face_power(3):
        fail("square/cube coefficient expansion mismatch")
    face_relations = []
    for side, power, scalar, expanded in (
        ("F", 2, "a", square_expanded), ("G", 3, "b", cube_expanded)
    ):
        shift = 8 if side == "F" else 12
        prefix = "f" if side == "F" else "g"
        for i, (coefficient, rho_power) in sorted(expanded.items()):
            face_relations.append({
                "side": side,
                "slot": f"{prefix}_{i}_{4 * i - shift}",
                "xi_degree": i,
                "scalar": scalar,
                "integer_coefficient": coefficient,
                "rho_power": rho_power,
            })
    if len(face_relations) != 37:
        fail(("FACEPIN relation count", len(face_relations)))

    single_root_k = {i: comb(7, i - 1) * ((-1) ** (8 - i)) for i in range(1, 9)}
    two_root_k = univariate_mul(
        {1: 1},
        univariate_mul(univariate_pow({1: 1, 0: -1}, 6), {1: 1, 0: -2}),
    )
    smoke_gamma6_k = univariate_mul({1: 1}, univariate_pow({1: 1, 0: -1}, 6))
    rho_zero_k = {8: 1}
    if dtil0_for_k(single_root_k) or dtil0_for_k(two_root_k):
        fail("Dtil_0 UFD power identity failed")
    if (min(two_root_k), max(two_root_k), two_root_k[min(two_root_k)], two_root_k[max(two_root_k)]) != (1, 8, -2, 1):
        fail(("two-root mutation lost degree/order/endpoints", two_root_k))
    if max(smoke_gamma6_k) != 7 or min(rho_zero_k) != 8:
        fail("cheap mutation did not break its intended endpoint check")

    controls_result = {}
    expected_control_rows = {
        "native_lambda_1": [4, 6, 10, 16, 22, 23, 24, 27, 28, 39],
        "artificial_D3": [8, 16, 24],
    }
    for name, (f, g) in control_pairs().items():
        recurrence = determinant_recurrence(f, g)
        direct = determinant_direct(f, g)
        if recurrence != direct:
            fail(("control engines disagree", name))
        live = [row for row in range(41) if direct[row]]
        if live != expected_control_rows[name]:
            fail(("control live rows", name, live))
        if direct[17] or direct[40]:
            fail(("negative control hits target/ceiling", name))
        if name == "native_lambda_1" and direct[39] != {0: -8}:
            fail(("native Dtil_39", direct[39]))
        controls_result[name] = {
            "first_nonzero_row": first_nonzero(direct),
            "nonzero_rows": live,
            "Dtil_17": [],
            "Dtil_39": sorted(direct[39].items()),
            "Dtil_40": [],
            "recurrence_equals_direct": True,
        }

    derivation = {
        "schema": "GGV-8_28-FACEPIN-CUSTODY-v1-reviewed-repair",
        "source_hashes": source_hashes,
        "primary_source_gzip_pins": PRIMARY_SOURCE_PINS,
        "family_reconstruction": {
            "api_route": ["get_pllc", "get_starting_edges", "get_complete_chains", "get_mn_families"],
            "candidate_count_for_mn_3_2": 1,
            "A0": [8, 1, 28],
            "A0_prime": [1, 1, 0],
            "step": [4, -1, 3, 4],
            "final": [11, 4, 7],
            "family": list(family),
            "family_index": family_index,
            "mn": [3, 2],
            "S": [[0, 0], [1, 0], [8, 28], [0, 4]],
            "degs_PQ_early_source_labels": [108, 72],
            "rhs_exp_after_psi4_only": 2,
        },
        "review_repair": {
            "edge_is_simple": False,
            "simple_equality_route_forbidden": True,
            "gap": gap,
            "gamma_max": gamma_max,
            "generated_corner_gamma": gamma,
            "A_gamma_unflipped": [a1, l1, gamma],
            "A_gamma_flipped": [flipped_a1, 1, gamma],
            "m": 3,
            "m_lambda": m_lambda,
            "deg_pbar": deg_pbar,
            "single_root_reason": "m_lambda=21=deg(pbar), hence pbar has one nonzero root of full multiplicity",
        },
        "source_errata": {
            "GGV22_tex_line_1132": {
                "printed_mixed_frame_edge": [[28, 8], [1, 0]],
                "typed_flipped_edge": [[28, 8], [0, 1]],
                "basis": "same sentence next clause and y(x^4*y-alpha)^7 geometry",
            },
            "silent_P_Q_relabel": {
                "early_proof": "P=3S,Q=2S",
                "from_line_1110": "P=2S,Q=3S",
                "compiler_rule": "orient by polygon: f in 2S, g in 3S; never orient by source letter",
            },
            "orientation_sign": {
                "flip_phi1_jacobian": -1,
                "normalization": "scale f by a nonzero constant so J(f,g)=1; this only rescales saturated a",
                "compiler_target": "Dtil_17=-1",
            },
        },
        "flip_unflip": {
            "flipped_shape_edge": "y*(x^4*y-rho)^7",
            "unflipped_shape_edge": "x*(x*y^4-rho)^7",
            "chart": "x=tau^-4*xi,y=tau",
            "K_rho": "xi*(xi-rho)^7",
        },
        "face_relations": face_relations,
        "relation_count": len(face_relations),
        "saturation": {
            "policy": "exactly; no additional factor without a family-wide nonvanishing proof",
            "factors": ["a", "b", "rho", "f_0_8", "g_0_12"],
        },
        "base_ring": "QQ[a,b,rho,405 positive-weight raw slots]",
        "modular_status": "heuristic only; never a characteristic-zero verdict",
        "input_side_firewall": "LF40 owes neither G2-PSC nor G2-BD because it remains in raw GGV coordinates",
    }
    mutations = {
        "schema": "GGV-8_28-FACEPIN-MUTATIONS-v1",
        "degree_preserving_two_root": {
            "K_prime": "xi*(xi-1)^6*(xi-2)",
            "degree": max(two_root_k),
            "order_at_xi_0": min(two_root_k),
            "constant_residual_factor": two_root_k[min(two_root_k)],
            "leading_coefficient": two_root_k[max(two_root_k)],
            "Dtil_0_identically_zero": not dtil0_for_k(two_root_k),
            "lattice_and_endpoint_gate": "PASS",
            "family_single_root_gate": "EXPECTED_REJECTION",
            "reason": "two distinct nonzero roots; only the generated-corner m_lambda=deg(pbar) bridge excludes it",
        },
        "gamma6_degree_drop_smoke": {
            "K_prime": "xi*(xi-1)^6",
            "degree": max(smoke_gamma6_k),
            "expected": "REJECT_DEGREE",
        },
        "rho_zero": {
            "K_prime": "xi^8",
            "order_at_xi_0": min(rho_zero_k),
            "expected": "REJECT_ENDPOINT_AND_SATURATION",
        },
    }
    result = {
        "status": "PASS_FACEPIN_CUSTODY_GATE_REVIEWED_REPAIR",
        "edge_is_simple": False,
        "gamma": 7,
        "m_lambda_equals_deg_pbar": [21, 21],
        "face_relations": 37,
        "two_root_mutation": "EXPECTED_REJECTION_FAMILY_SINGLE_ROOT_ONLY",
        "controls": {name: data["first_nonzero_row"] for name, data in controls_result.items()},
        "lifecycle": "PRODUCER_UNREVIEWED_NOT_PROMOTED_EVIDENCE",
    }
    write_json(output / "facepin_derivation.json", derivation)
    write_json(output / "mutations.json", mutations)
    write_json(output / "negative_controls.json", controls_result)
    write_json(output / "RESULT.json", result)
    freeze_directory(output, "DESK_GATE_EVIDENCE.sha256")
    print(result["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
