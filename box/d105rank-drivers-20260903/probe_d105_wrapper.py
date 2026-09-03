#!/usr/bin/env python3
"""JSON preflight for D105-RANK-GATE, without inventing a global decoration.

The output contains only computations justified by the frozen inputs:

* the mandatory eight-file SHA-256 gate;
* exact A/B/C Moh level data and the D_2 junction;
* the exact restricted one-disc linearized operator at that junction;
* the blind submission's 2k-versus-35 table, explicitly typed COUNTING-BOUND;
* the sealed GLOBAL-INTERPOLATION controls/self-test; and
* a Galois-covariant non-vacuity mutation of (y,x+y^3) rejected by the
  polynomial-input guard at t-order 1.

It intentionally emits no D105 global rank.  Such a rank requires the complete
105-leaf decorated skeleton demanded by section 4.1 of the sealed report.
"""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

import sympy as sp


INPUT_ROOT = Path("/tmp/jc2-lane.syVtTr/inputs")
EXPECTED_HASHES = {
    "global-interpolation-sol56-20260902.md": "20d554a0b19c563093ec35caad58664f800d7517490f530a07f511d7042393b6",
    "globalinterp.py": "49ba5a019714e30a952c998fb39a88aff38505a80fcac6df3c5883bb16599588",
    "census-rebase-opus5-20260902.md": "fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948",
    "survivors-D48-120.txt": "47f59906927ff9d2b38b25b11c2e46cef3c472b3d8db300f12c12f22906848e1",
    "ideation-20260903T1015Z-gpt55.md": "5e1646f507e946b831dcb77d542f7ab367eb398227a3032b96bcd7a45d2f320d",
    "time-function-endgame-review-sol56-20260902.md": "9e485492940818ea25b955af1713de53bc823af78f9f00a8991aaba9372f527d",
    "bottomode.py": "69ff5bdea265adc37c9518f381eccfe6a6162c430a51075b6c2069f709894473",
    "moh_skeleton_full.py": "d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2",
}

GROUPS = {
    "A": {"M2": 28, "V3": 5, "q": Fraction(1, 2), "u": 25, "N": list(range(6, 13))},
    "B": {"M2": 28, "V3": 6, "q": Fraction(9, 13), "u": 30, "N": [9]},
    "C": {"M2": 40, "V3": 4, "q": Fraction(9, 17), "u": 28, "N": [9]},
}


def qstr(value: Fraction | int | sp.Rational | sp.Expr) -> str:
    if isinstance(value, Fraction):
        return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    return sp.sstr(sp.factor(value))


def hash_gate() -> dict[str, Any]:
    rows = []
    for name, expected in EXPECTED_HASHES.items():
        got = hashlib.sha256((INPUT_ROOT / name).read_bytes()).hexdigest()
        rows.append({"file": name, "expected": expected, "actual": got, "match": got == expected})
    passed = all(row["match"] for row in rows)
    if not passed:
        mismatches = [row["file"] for row in rows if not row["match"]]
        raise SystemExit("HASH MISMATCH: " + ", ".join(mismatches))
    return {"status": "PASS", "files": rows}


def load_framework():
    path = INPUT_ROOT / "globalinterp.py"
    spec = importlib.util.spec_from_file_location("sealed_globalinterp_d105_probe", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def skeleton_delta(i: int, n: int, M: dict[int, int], d: dict[int, int], V: dict[int, int]) -> Fraction:
    """Moh Def. 5.1(3), copied as rational arithmetic from the frozen census."""
    s = max(M)
    numerator = Fraction(n - M[i], 1)
    denominator = Fraction(n - M[s] - 1, 1)
    for j in range(i + 1, s + 1):
        numerator *= V[j] * (n - M[j]) - d[j]
        denominator *= V[j] * (n - M[j - 1]) - d[j]
    return 1 - numerator / denominator


def local_matrix(mu: Fraction, E: Fraction) -> sp.Matrix:
    """Restricted (2,3,V2=1) L_E in columns u0,u1,u2,v0,v1,v2,v3."""
    m = sp.Rational(mu.numerator, mu.denominator)
    e = sp.Rational(E.numerator, E.denominator)
    return sp.Matrix(
        [
            [2 * m - e, 0, 0, 0, sp.Rational(4, 3) * m, 0, 0],
            [0, -e - m, 0, 6 * m - 2 * e, 0, sp.Rational(8, 3) * m, 0],
            [3 * e - 6 * m, 0, -e - 4 * m, 0, 4 * m - 2 * e, 0, 4 * m],
            [0, 3 * e - 3 * m, 0, 0, 0, 2 * m - 2 * e, 0],
            [0, 0, 3 * e, 0, 0, 0, -2 * e],
        ]
    )


def derive_group(label: str, raw: dict[str, Any]) -> dict[str, Any]:
    n, m, K, dsmall, esmall = 105, 70, 35, 2, 3
    M = {1: -m, 2: int(raw["M2"]), 3: n - 2}
    d = {1: n}
    for i in range(1, 4):
        d[i + 1] = math.gcd(d[i], M[i])
    V = {2: 1, 3: int(raw["V3"]), 4: d[4]}
    delta = {i: skeleton_delta(i, n, M, d, V) for i in range(1, 4)}
    q_expected = (1 - delta[1]) * Fraction(dsmall * esmall, dsmall + esmall)
    if q_expected != raw["q"]:
        raise AssertionError(f"{label}: q mismatch {q_expected} != {raw['q']}")
    u_expected = Fraction(V[3] * K, d[3])
    if u_expected != raw["u"]:
        raise AssertionError(f"{label}: u mismatch {u_expected} != {raw['u']}")

    a = [Fraction(n * V[r + 1], d[r + 1]) for r in range(1, 4)]
    b = [Fraction(m * V[r + 1], d[r + 1]) for r in range(1, 4)]
    if any(value.denominator != 1 for value in a + b):
        raise AssertionError(f"{label}: nonintegral cluster size")
    J2 = delta[1] - delta[2]
    R = math.lcm(*(value.denominator for value in delta.values()))
    mu = Fraction(1 - delta[1], dsmall + esmall)
    kappa = Fraction(4, 3)
    jacobian_for_fixed_star = kappa * raw["q"] / (dsmall * esmall)
    matrix = local_matrix(mu, J2)
    rank = int(matrix.rank())
    kernel = matrix.nullspace()

    # A_2 is the denominator increment controlling the local cover-factor
    # automorphism.  It is not, without route-to-tree data, a physical disc
    # or fibre-root orbit size.
    A2 = delta[2].denominator
    Q2 = V[3] * d[2] // d[3]
    triangle, square = divmod(Q2, A2)
    A1 = (math.lcm(delta[2].denominator, delta[3].denominator) * delta[1]).denominator

    k_rows = []
    for N in raw["N"]:
        k = Fraction(N, 1) / raw["q"]
        if k.denominator != 1:
            raise AssertionError(f"{label}: nonintegral k at N={N}")
        kk = int(k)
        unknowns = 2 * kk
        k_rows.append(
            {
                "N": N,
                "k": kk,
                "local_kernel_unknowns": unknowns,
                "degree_moment_equations": n - m,
                "equation_minus_unknown_count": n - m - unknowns,
                "overdetermined_by_count": n - m > unknowns,
                "typing": "COUNTING-BOUND",
                "qualification": "This is the GPT-5.5 first-order count, not a matrix rank or ideal height.",
            }
        )

    return {
        "group": label,
        "skeleton": {
            "n": n,
            "m": m,
            "K": K,
            "d_e": [dsmall, esmall],
            "M": [M[1], M[2], M[3]],
            "V": [V[2], V[3], V[4]],
            "d_chain": [d[i] for i in range(1, 5)],
            "delta": [qstr(delta[i]) for i in range(1, 4)],
            "a_r": [int(value) for value in a],
            "b_r": [int(value) for value in b],
            "q": qstr(q_expected),
            "u": int(u_expected),
            "bottom_star": {
                "p_g": "pi^3-pi",
                "p_f": "pi^2-2/3",
                "kappa": qstr(kappa),
                "jacobian_c_for_this_fixed_normalisation": qstr(jacobian_for_fixed_star),
            },
        },
        "junction_D2": {
            "J2_t": qstr(J2),
            "minimal_uniformizer_denominator_from_delta": R,
            "J2_z": int(J2 * R),
        },
        "galois_arithmetic": {
            "A1": A1,
            "A2": A2,
            "Q2": Q2,
            "Q2_divmod_A2": [triangle, square],
            "maximal_level2_scalar_factor_pattern": [A2] * triangle + [square],
            "pattern_qualification": (
                "Each A2 entry is a possible free nonzero factor orbit in the local cover polynomial p(pi). "
                "The remainder is multiplicity at its fixed zero.  Neither object is thereby identified "
                "with a physical bottom-disc packet or fibre-branch orbit."
            ),
            "V2_satisfies_branch_10_nonzero_root": V[2] <= triangle,
            "V2_satisfies_branch_11_zero_root": (V[2] - square) % A2 == 0,
            "qualification": (
                "A1 and A2 govern formal/local cover actions.  In particular, A2 distinct "
                "conjugate factors of p(pi) are forced for its selected nonzero root.  "
                "Route-to-tree and head-eigencharacter data are required before turning "
                "either action into a physical-disc stabilizer or fibre-branch orbit."
            ),
        },
        "restricted_local_operator_at_J2": {
            "basis_columns": ["u0", "u1", "u2", "v0", "v1", "v2", "v3"],
            "target_rows": ["pi^0", "pi^1", "pi^2", "pi^3", "pi^4"],
            "mu": qstr(mu),
            "E": qstr(J2),
            "E_over_mu": qstr(J2 / mu),
            "matrix": [[qstr(entry) for entry in matrix.row(i)] for i in range(matrix.rows)],
            "rank": rank,
            "kernel_dimension": len(kernel),
            "cokernel_dimension": matrix.rows - rank,
            "kernel_basis": [[qstr(entry) for entry in vector] for vector in kernel],
            "resonance_set_E": [qstr(j * mu) for j in range(4)],
            "typing": "PROVED-HERE/UNREVIEWED local restricted computation",
            "qualification": "Local rank 5 and a two-dimensional kernel per bottom disc do not give a global interpolation rank.",
        },
        "first_order_count_table": k_rows,
    }


def sealed_checks(gi) -> dict[str, Any]:
    controls = gi.run_controls(verbose=False)
    selftest = gi._selftest(verbose=False)
    return {
        "controls": {"checks": controls.count, "failures": len(controls.failures), "expected": "40/0"},
        "selftest": {"checks": selftest.count, "failures": len(selftest.failures), "expected": "50/0"},
        "status": "PASS" if not controls.failures and not selftest.failures else "FAIL",
    }


def requested_k(raw: dict[str, Any]) -> list[int]:
    values = []
    for N in raw["N"]:
        k = Fraction(N, 1) / raw["q"]
        if k.denominator != 1:
            raise AssertionError(f"nonintegral k at N={N}")
        values.append(int(k))
    return values


def unavailable_global_metrics() -> dict[str, Any]:
    reason = "The full decorated root system and invariant retained support are absent."
    return {
        "intrinsic_unknowns_U_4_13": {"status": "NOT_COMPUTED", "reason": reason},
        "intrinsic_equations_C_4_11": {"status": "NOT_COMPUTED", "reason": reason},
        "ambient_or_sampled_global_rank": {"status": "NOT_COMPUTED", "reason": reason},
        "global_row_cokernel_dimension": {"status": "NOT_COMPUTED", "reason": reason},
        "saturated_ideal": {
            "status": "NOT_COMPUTED",
            "empty": "NOT_COMPUTED",
            "reason": "There is no global ideal component or declared coefficient ring to saturate.",
        },
    }


def decoration_manifest(derived_groups: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_label = {row["group"]: row for row in derived_groups}
    output = []
    for label, raw in GROUPS.items():
        group = by_label[label]
        A2 = int(group["galois_arithmetic"]["A2"])
        a2 = int(group["skeleton"]["a_r"][1])
        r2 = int(Fraction(group["skeleton"]["delta"][1]) * group["junction_D2"]["minimal_uniformizer_denominator_from_delta"])
        r1 = int(Fraction(group["skeleton"]["delta"][0]) * group["junction_D2"]["minimal_uniformizer_denominator_from_delta"])
        R = int(group["junction_D2"]["minimal_uniformizer_denominator_from_delta"])
        for k in requested_k(raw):
            leaves_inside = 3 * k
            residual_leaves = 105 - leaves_inside
            for mode in ("UNI", "SPLIT"):
                if mode == "UNI":
                    status = "OPEN[D105-FULL-DECORATION]"
                    closure = (
                        f"UNI requests one orbit of k={k} physical bottom discs.  The chain gives an A2={A2} "
                        "orbit of factors of a local cover polynomial, but supplies no theorem identifying "
                        "those factors with this disc packet."
                    )
                else:
                    status = "OPEN[SPLIT-ORBIT-DATA]"
                    closure = (
                        f"No several-orbit partition of the k={k} physical discs is supplied by the d-chain. "
                        f"The local cover-factor increment A2={A2} does not fill that missing route."
                    )
                output.append(
                    {
                        "group": label,
                        "k": k,
                        "decoration": mode,
                        "status": status,
                        "A2": A2,
                        "cover_factor_arithmetic_vs_disc_orbit": closure,
                        "bottom_star": {
                            "disc_count_requested": k,
                            "leaves_per_disc": 3,
                            "leaves_inside_requested_stars": leaves_inside,
                            "residual_leaves_not_in_requested_stars": residual_leaves,
                            "p_g": "pi^3-pi",
                            "p_f": "pi^2-2/3",
                        },
                        "rooted_cluster_tree": {
                            "known_distinguished_cluster_sizes_a_r": group["skeleton"]["a_r"],
                            "if_all_marked_stars_lie_in_the_distinguished_D2": {
                                "marked_leaves": leaves_inside,
                                "unmarked_leaves_inside_D2": a2 - leaves_inside,
                                "leaves_outside_D2": 105 - a2,
                                "qualification": "The containment is a completion assumption, not supplied route-to-tree data.",
                            },
                            "full_105_leaf_partition": "MISSING",
                        },
                        "cyclic_galois_action": {
                            "requested_mode": mode,
                            "permutation_on_105_leaves": "MISSING",
                            "coefficient_covariance_check": "NOT_RUN",
                        },
                        "puiseux_templates": {
                            "known_internal_star_coefficients": ["-1", "0", "1"],
                            "group_level_conditional_cover_star_copy_ansatz_unrelated_to_packet_k": {
                                "formula": (
                                    f"tau_(j,c)(z)=w_<delta2(zeta^j*z)+b*zeta^({r2}j)*z^{r2}"
                                    f"+c*zeta^({r1}j)*z^{r1}+higher; j mod A2={A2}, c in {{-1,0,1}}"
                                ),
                                "extra_closure_assumptions": [
                                    "w_<delta2>(zeta^A2*z)=w_<delta2>(z)",
                                    "every higher coefficient obeys the compatible A2-step wrap",
                                ],
                                "displayed_leading_label_cycles_if_closed": [A2, 2 * A2],
                            },
                            "minimal_uniformizer": f"x=z^-{R}",
                            "ansatz_qualification": (
                                "Test-only group-level copy of the local cover action, unrelated to the "
                                "requested k until a route is supplied.  Even the displayed leading-label "
                                "cycles require the printed prefix/tail closure assumptions."
                            ),
                            "disc_centres_ancestor_coefficients_and_tails": "MISSING",
                        },
                        "shared_coefficient_declarations": {
                            "conditional_covariance_schema": "u_(j+1,c,r)=zeta^r*u_(j,c,r), with wrap c<->-c",
                            "actual_active_symbols_and_ancestor_sharing": "MISSING",
                        },
                        "valuation_guard": "MISSING",
                        "orders": {
                            "first_nonvacuous_global_order_Q_star": "UNKNOWN",
                            "first_global_system_emitted": False,
                            "D2_junction_t": group["junction_D2"]["J2_t"],
                            "D2_global_emission": "NOT_REACHED",
                        },
                        "global_metrics": unavailable_global_metrics(),
                        "blind_count_only": {
                            "local_kernel_unknowns": 2 * k,
                            "degree_moment_slots": 35,
                            "equation_minus_unknown_count": 35 - 2 * k,
                        },
                        "verdict": "COUNTING-BOUND",
                        "qualification": (
                            "This is not a section-4.1 decoration until the route from cover factors to discs and every missing global field are supplied."
                        ),
                    }
                )
    return output


def cubic_tame_mutation() -> dict[str, Any]:
    """Mutate one independent, Galois-covariant cubic root-tail coefficient."""
    z, yvar, tame = sp.symbols("z y_mut a")
    omega = (-1 + sp.sqrt(3) * sp.I) / 2
    original = [-omega ** (-j) / z for j in range(3)]
    # One independent q=1 coefficient; covariance forces its two conjugates.
    mutated = [original[j] + tame * omega**j * z for j in range(3)]
    covariance = [
        sp.simplify(mutated[j].subs(z, omega * z) - mutated[(j + 1) % 3]) == 0
        for j in range(3)
    ]
    fibre_polynomial = sp.simplify(sp.expand(sp.prod(yvar - root for root in mutated)))
    expected_fibre = yvar**3 + 3 * tame * yvar + z**-3 - tame**3 * z**3
    if sp.simplify(fibre_polynomial - expected_fibre) != 0 or not all(covariance):
        raise AssertionError("cubic mutation covariance/reconstruction failed")
    forbidden_t1 = -tame**3
    sat_witness = sp.symbols("sat_witness")
    saturation_basis = sp.groebner(
        [forbidden_t1, sat_witness * tame - 1],
        tame,
        sat_witness,
        order="lex",
        domain=sp.QQ,
    )
    basis_strings = [sp.sstr(polynomial.as_expr()) for polynomial in saturation_basis.polys]
    return {
        "control": "(f,g)=(y,x+y^3)",
        "reference_fibre": "c2=0",
        "uniformizer": "x=z^-3, so t=x^-1=z^3",
        "mutation": "tau_j=-omega^(-j)z^-1 -> tau_j+a*omega^j*z; one independent q=1 coefficient",
        "omega": "(-1+sqrt(3)*I)/2",
        "cyclic_covariance": {
            "rule": "tau_j(omega*z)=tau_(j+1)(z)",
            "checks": covariance,
            "status": "PASS",
        },
        "branches_after_mutation": [sp.sstr(value) for value in mutated],
        "reconstructed_monic_fibre_polynomial": sp.sstr(expected_fibre),
        "failed_guard": "coefficient polynomiality of g-c2 over C[t^-1]",
        "failed_coefficient": "[t^1][y^0] product_j(y-tau_j) = -a^3",
        "failure_order_z": 3,
        "failure_order_t": "1",
        "saturation_open_condition": "a != 0",
        "rabinowitsch_saturation": {
            "ring": "QQ[a,sat_witness], lex(a,sat_witness)",
            "ideal": ["a^3", "sat_witness*a-1"],
            "groebner_basis": basis_strings,
            "empty": basis_strings == ["1"],
        },
        "closed_stratum_positive_witness": "a=0 reconstructs the original valid c2=0 fibre polynomial y^3+x",
        "open_stratum_negative_result": "a!=0 has no point satisfying the polynomial-input coefficient a^3=0",
        "fixed_open_factors": "the mutated leading branch separations and monic cubic degree leader are nonzero units",
        "fails_on_open_set": forbidden_t1 != 0 and basis_strings == ["1"],
        "status": "EXPECTED-FAIL",
        "qualification": (
            "The covariant root set fails the required polynomial-input guard at t^1 and is "
            "rejected before the finite decorated interpolation emitter.  This is a same-wrapper "
            "vacuity/input-control check, not a DEG/POLY failure in that emitter."
        ),
    }


def bad_g_negative_control() -> dict[str, Any]:
    z = sp.symbols("z")
    tau_plus = z**-1 * sp.sqrt(1 + z)
    W_plus = sp.series(1 / (2 * tau_plus), z, 0, 4).removeO().expand()
    residue_plus = sp.factor(W_plus.coeff(z, 1))
    residue_minus = -residue_plus
    return {
        "g": "y^2-x^2-x",
        "uniformizer": "x=z^-1=t^-1",
        "no_residue_coefficients": [qstr(residue_plus), qstr(residue_minus)],
        "failure_order_z": 1,
        "failure_order_t": "1",
        "status": "EXPECTED-FAIL",
    }


def positive_controls_at_target_orders(gi) -> dict[str, Any]:
    orders = ["7/36", "7/26", "11/34"]
    x, y, c2 = gi.x, gi.y, gi.c2
    controls = [
        ("(y,x+y^3)", y, x + y**3),
        ("(y,x+y^5)", y, x + y**5),
        ("(x+y^5,y+(x+y^5)^3)", x + y**5, y + (x + y**5) ** 3),
    ]
    additive = sp.Symbol("a_common")
    rows = []
    for label, f, g in controls:
        recovered = gi.quotient_interpolant(sp.expand(g - c2), f + additive)
        exact = sp.expand(recovered - f - additive) == 0
        if not exact:
            raise AssertionError(f"positive control interpolation failed: {label}")
        rows.append(
            {
                "map": label,
                "exact_recovered_interpolant": sp.sstr(recovered),
                "exact_all_order_check": exact,
                "status_at_every_listed_order": "SURVIVES-TO-Q",
                "execution_mode": "exact automorphism/quotient identity; not the finite decorated-emitter path",
                "reason": "The exact polynomial interpolant and NO-RESIDUE identities hold to all orders.",
                "expected_free_parameters": {
                    "before_common_additive_gauge": 1,
                    "after_fixing_common_additive_gauge": 0,
                    "qualification": "analytic expectation for fixed exact roots: one transitive branch orbit gives one common integration constant; no free-tail dimension was measured",
                },
            }
        )
    return {
        "orders_t": orders,
        "controls": rows,
    }


def formal_global_system_schema() -> dict[str, Any]:
    return {
        "status": "FORMAL-SCHEMA-NOT-EMITTED",
        "assumptions": [
            "all 105 tau_i are a complete separable fibre-root packet of one polynomial g-c2",
            "Galois descent and coefficient covariance have been verified",
            "DEG is imposed before using the unit-triangular moment form of POLY",
            "the inverse/integration valuation guard is closed",
        ],
        "definitions": [
            "D_i=product_(j!=i)(tau_i-tau_j)",
            "W_i=D_i^-1",
            "[z^R]W_i=0 (NO-RESIDUE, one independent row per verified branch orbit)",
            "q*H_i[q]=-c*R*W_i[q+R] for q!=0; H_i[0]=a_orbit",
            "M_r=sum_i H_i*tau_i^r*W_i",
        ],
        "degree_block_at_each_retained_exponent": {
            "rows": 35,
            "equations": "[z^q]M_r=0 for r=0..33 and [z^q]M_34=KroneckerDelta(q,0)",
        },
        "additional_poly_block_at_a_forbidden_positive_invariant_exponent": {
            "rows": 70,
            "equations": "[z^q]M_r=0 for r=35..104 (unit-triangular equivalent form)",
        },
        "first_nonvacuous_exponent": "UNKNOWN without ell(M_r-target_r), beta_j, and the invariant support",
        "D2_warning": "J2 is a relative tree-activation gap, not automatically an actual global coefficient exponent.",
    }


def trusted_orbit_audit(gi) -> dict[str, Any]:
    data = copy.deepcopy(gi.example_config())
    data["branches"][1]["terms"]["-1"] = "-2*I"
    result = gi.GlobalInterpolationSystem(data).result(rank_method="none")
    return {
        "non_equivariant_verified_orbit_was_accepted": True,
        "effective_no_log_count": result["direct_conditions"]["no_log"]["effective_over_base_field"],
        "integration_constants_after_descent": result["direct_conditions"]["integration_constants"][
            "variables_after_verified_orbit_descent"
        ],
        "leading_difference": result["contacts"]["plus,minus"]["leading_difference"],
        "consequence": "The D105 wrapper must validate the actual cyclic permutation and coefficient covariance before orbit reduction.",
    }


def main() -> int:
    gate = hash_gate()
    gi = load_framework()
    checks = sealed_checks(gi)
    if checks["status"] != "PASS":
        raise SystemExit("sealed controls/selftest failed")
    groups = [derive_group(label, raw) for label, raw in GROUPS.items()]
    result = {
        "driver": "D105-RANK-GATE/probe-preflight-1",
        "typing": "PROVED-HERE/UNREVIEWED finite exact computations; no global D105 rank claimed",
        "hash_gate": gate,
        "sealed_framework_checks": checks,
        "groups": groups,
        "formal_global_system_schema": formal_global_system_schema(),
        "decoration_manifest": decoration_manifest(groups),
        "positive_controls_at_D105_orders": positive_controls_at_target_orders(gi),
        "negative_control": bad_g_negative_control(),
        "vacuity_guard": cubic_tame_mutation(),
        "framework_interface_audit": trusted_orbit_audit(gi),
        "global_rank": {
            "status": "OPEN[D105-FULL-DECORATION]",
            "bounded_quantity": "For each charged (group,k,orbit decoration), supply and validate 105 labelled root series through the requested guard, then compute 35 first-order moment rows and the J2 continuation.",
            "missing": [
                "rooted cluster tree on all 105 labelled leaves",
                "placement and Puiseux centres of the 105-3k leaves not internal to the charged three-root bottom stars",
                "cyclic action/permutation with checked orbit and stabilizer covariance",
                "leading separation coefficients at every ancestor",
                "tame exponent support and explicit sharing equivalence classes",
                "enough tail coefficients for the inverse-denominator valuation guard",
            ],
            "warning": "The 2k-versus-35 table is a COUNTING-BOUND and must not be relabelled as rank, cokernel, ideal height, or emptiness.",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
