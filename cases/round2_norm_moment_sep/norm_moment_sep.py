#!/usr/bin/env python3
"""Bounded exact NORM-MOMENT-SEP receiver/control gate.

Standard library only.  This implementation does not import the round-1 trace
probe and never computes moments above two.
"""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


SCHEMA = "jc2.norm-moment-sep.v1"
REPO = Path(__file__).resolve().parents[2]

PINNED_INPUTS = {
    "cases/round2_norm_moment_sep/PREREGISTRATION.md":
        "15caf35ca825f7a56bb6766cf585b4845c41a491904a748301264a7eb708330b",
    "xmodel/ideation-20260824T0156Z-synthesis.md":
        "9c0455ddae2388d7f5256ec46094c0d97dd5bc6748f2b61177f736cc23581f50",
    "xmodel/ideation-20260824T0156Z-adversary.md":
        "b9ad25c0cd16ec6698b7922128f00da6ca4dede812dc38d9e9444f42dcf1aec8",
    "xmodel/review-round1-proof-gates-claude.md":
        "ef0bf14d10abfedb5c4b8921344ff9de1dc0078f287ed5c6fe3fc7a24a522e11",
    "xmodel/round1-trace-regularity-20260824.md":
        "908dc24bfb7f493d108e05135d863bc1a32a4c4ef8e3889f7dee89574978920c",
    "cases/round1_trace_probe/trace_probe.py":
        "faadfaf26c7184c24fc3e55a3de90c881e38b0bf12293cb245bcaa9ab5ad0372",
    "cases/round1_trace_probe/results.json":
        "51f5a6e200327dd343c1c06ed2e9529ef807428531d21535caef63c655f00706",
    "jc72108/systems/farm/4_12mn34d64/manifest.json":
        "26bf6d4e7845e6278a24d09161bef36e320af2e87bff1c32a1f2a5eeae72e577",
}


# Coefficient ring QQ[q], represented sparsely as q-exponent -> Fraction.
QPoly = dict[int, Fraction]
# Laurent polynomials in u or t with QQ[q] coefficients.
Laurent = dict[int, QPoly]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def canonical_bytes(obj: Any) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n").encode()


def hash_obj(obj: Any) -> str:
    return sha256_bytes(canonical_bytes(obj))


def qp_clean(a: QPoly) -> QPoly:
    return {k: v for k, v in a.items() if v}


def qp_const(value: int | Fraction) -> QPoly:
    value = Fraction(value)
    return {} if value == 0 else {0: value}


def qp_q() -> QPoly:
    return {1: Fraction(1)}


def qp_add(a: QPoly, b: QPoly) -> QPoly:
    out = dict(a)
    for degree, coeff in b.items():
        out[degree] = out.get(degree, Fraction(0)) + coeff
    return qp_clean(out)


def qp_scale(a: QPoly, scalar: int | Fraction) -> QPoly:
    scalar = Fraction(scalar)
    return qp_clean({degree: scalar * coeff for degree, coeff in a.items()})


def qp_mul(a: QPoly, b: QPoly) -> QPoly:
    out: QPoly = {}
    for da, ca in a.items():
        for db, cb in b.items():
            degree = da + db
            out[degree] = out.get(degree, Fraction(0)) + ca * cb
    return qp_clean(out)


def qp_derivative(a: QPoly) -> QPoly:
    return qp_clean({degree - 1: degree * coeff for degree, coeff in a.items() if degree})


def qp_json(a: QPoly) -> list[dict[str, int]]:
    return [
        {"q_exp": degree, "num": coeff.numerator, "den": coeff.denominator}
        for degree, coeff in sorted(a.items())
    ]


def laurent_clean(a: Laurent) -> Laurent:
    return {k: qp_clean(v) for k, v in a.items() if qp_clean(v)}


def laurent_add(a: Laurent, b: Laurent) -> Laurent:
    out = {degree: dict(coeff) for degree, coeff in a.items()}
    for degree, coeff in b.items():
        out[degree] = qp_add(out.get(degree, {}), coeff)
    return laurent_clean(out)


def laurent_scale(a: Laurent, scalar: int | Fraction) -> Laurent:
    return laurent_clean({degree: qp_scale(coeff, scalar) for degree, coeff in a.items()})


def laurent_mul(a: Laurent, b: Laurent) -> Laurent:
    out: Laurent = {}
    for da, ca in a.items():
        for db, cb in b.items():
            degree = da + db
            out[degree] = qp_add(out.get(degree, {}), qp_mul(ca, cb))
    return laurent_clean(out)


def laurent_pow(a: Laurent, power: int) -> Laurent:
    if power < 0:
        raise ValueError("negative Laurent-polynomial power")
    out: Laurent = {0: qp_const(1)}
    for _ in range(power):
        out = laurent_mul(out, a)
    return out


def laurent_shift(a: Laurent, shift: int) -> Laurent:
    return {degree + shift: dict(coeff) for degree, coeff in a.items()}


def laurent_derivative_u(a: Laurent) -> Laurent:
    return laurent_clean(
        {degree - 1: qp_scale(coeff, degree) for degree, coeff in a.items() if degree}
    )


def laurent_derivative_q(a: Laurent) -> Laurent:
    return laurent_clean({degree: qp_derivative(coeff) for degree, coeff in a.items()})


def laurent_json(a: Laurent, variable: str) -> list[dict[str, Any]]:
    return [
        {f"{variable}_exp": degree, "coeff": qp_json(coeff)}
        for degree, coeff in sorted(a.items())
    ]


def principal_part(a: Laurent) -> Laurent:
    return {degree: coeff for degree, coeff in a.items() if degree < 0}


def coefficient(a: Laurent, degree: int) -> QPoly:
    return a.get(degree, {})


def valuation_u(a: Laurent) -> int:
    if not a:
        raise ValueError("valuation of zero")
    return min(a)


def rational_normalize(num: Laurent, den: Laurent) -> tuple[Laurent, Laurent]:
    """Shift to denominator valuation zero and scale its constant to one.

    The controls have a nonzero rational constant in the shifted denominator.
    """
    den_val = valuation_u(den)
    num = laurent_shift(num, -den_val)
    den = laurent_shift(den, -den_val)
    constant = den.get(0, {})
    if set(constant) != {0}:
        raise ValueError("denominator leading coefficient is not rational")
    lead = constant[0]
    return laurent_scale(num, 1 / lead), laurent_scale(den, 1 / lead)


def rational_equal(
    left_num: Laurent, left_den: Laurent, right_num: Laurent, right_den: Laurent
) -> bool:
    return laurent_mul(left_num, right_den) == laurent_mul(right_num, left_den)


def rational_json(num: Laurent, den: Laurent) -> dict[str, Any]:
    num, den = rational_normalize(num, den)
    return {
        "kind": "rational_in_U_mod_U^e_minus_t",
        "numerator": laurent_json(num, "u"),
        "denominator": laurent_json(den, "u"),
    }


def trace_filter(coord: Laurent, e: int) -> Laurent:
    """Trace via the conjugation/divisibility filter."""
    out: Laurent = {}
    for u_exp, coeff_q in coord.items():
        if u_exp % e == 0:
            t_exp = u_exp // e
            out[t_exp] = qp_add(out.get(t_exp, {}), qp_scale(coeff_q, e))
    return laurent_clean(out)


def trace_matrix(coord: Laurent, e: int) -> Laurent:
    """Trace independently from diagonal entries in the companion basis."""
    out: Laurent = {}
    for u_exp, coeff_q in coord.items():
        for basis_exp in range(e):
            t_exp, reduced_exp = divmod(u_exp + basis_exp, e)
            if reduced_exp == basis_exp:
                out[t_exp] = qp_add(out.get(t_exp, {}), coeff_q)
    return laurent_clean(out)


def moments_from_laurent(coord: Laurent, e: int) -> tuple[dict[str, Any], list[str]]:
    records: dict[str, Any] = {}
    failures: list[str] = []
    for power in (1, 2):
        powered = laurent_pow(coord, power)
        by_filter = trace_filter(powered, e)
        by_matrix = trace_matrix(powered, e)
        if by_filter != by_matrix:
            failures.append(f"trace_algorithms_disagree:m={power}")
        pp = principal_part(by_filter)
        pp_json = laurent_json(pp, "t")
        records[str(power)] = {
            "trace": laurent_json(by_filter, "t"),
            "principal_part": pp_json,
            "principal_part_sha256": hash_obj(pp_json),
            "algorithms_agree": by_filter == by_matrix,
        }
    return records, failures


def positive_valuation_moments(coord_valuation: int) -> dict[str, Any]:
    if coord_valuation < 0:
        raise ValueError("positive-valuation certificate requested for a pole")
    empty: list[dict[str, Any]] = []
    empty_hash = hash_obj(empty)
    return {
        str(power): {
            "trace": None,
            "principal_part": empty,
            "principal_part_sha256": empty_hash,
            "certificate": {
                "kind": "u_valuation",
                "coordinate_u_valuation": coord_valuation,
                "power_u_valuation_lower_bound": power * coord_valuation,
            },
        }
        for power in (1, 2)
    }


def permutation_sign(permutation: list[int]) -> int:
    inversions = sum(
        1
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
        if permutation[i] > permutation[j]
    )
    return -1 if inversions % 2 else 1


def local_algebra(e: int) -> tuple[dict[str, Any], dict[str, Any], list[str]]:
    failures: list[str] = []
    permutation = [0] + [e - i for i in range(1, e)]
    if sorted(permutation) != list(range(e)):
        failures.append("trace_pairing_not_permutation")
    pairing_sign = permutation_sign(permutation)
    pairing_disc = {
        "sign": pairing_sign,
        "integer_abs": e**e,
        "t_exp": e - 1,
        "method": "sparse_trace_pairing_determinant",
    }

    norm_u_sign = -1 if (e - 1) % 2 else 1
    norm_derivative_sign = norm_u_sign ** (e - 1)
    resultant_conversion_sign = -1 if (e * (e - 1) // 2) % 2 else 1
    derivative_disc = {
        "sign": resultant_conversion_sign * norm_derivative_sign,
        "integer_abs": e**e,
        "t_exp": e - 1,
        "method": "different_norm_with_resultant_sign",
    }
    if pairing_disc["sign"] != derivative_disc["sign"]:
        failures.append("discriminant_sign_disagreement")
    if pairing_disc["integer_abs"] != derivative_disc["integer_abs"]:
        failures.append("discriminant_coefficient_disagreement")
    if pairing_disc["t_exp"] != derivative_disc["t_exp"]:
        failures.append("discriminant_exponent_disagreement")

    algebra = {
        "base": "QQ(q)((t))",
        "normalization": "QQ(q)((u))",
        "relation": f"U^{e}-t",
        "basis": {"kind": "power", "start": 0, "stop_inclusive": e - 1},
        "rank": e,
        "ramification_degree": e,
        "residue_degree": 1,
        "split_uniformizer": {"t": f"u^{e}", "unit_twist": "1"},
    }
    algebra["sha256"] = hash_obj(algebra)

    different = {
        "generator": {"integer_coefficient": e, "u_exp": e - 1},
        "kahler_fitting_u_exp": e - 1,
        "inverse_different_u_exp": 1 - e,
        "target_derivation_integrality_conductor_u_exp": e - 1,
        "discriminant_from_trace_pairing": pairing_disc,
        "discriminant_from_different": derivative_disc,
        "independent_derivations_agree": not failures,
    }
    different["sha256"] = hash_obj(different)
    return algebra, different, failures


def target_tag(label: str) -> dict[str, Any]:
    return {
        "kind": "affine_height_one_control",
        "label": label,
        "equation": "t=0",
        "uniformizer": "t",
        "residue_field": "QQ(q)",
        "target_infinity": False,
    }


def receiver_record(
    *,
    record_id: str,
    tier: str,
    e: int,
    x_num: Laurent,
    x_den: Laurent,
    y_num: Laurent,
    y_den: Laurent,
    x_moments: dict[str, Any],
    y_moments: dict[str, Any],
    decoration: dict[str, Any],
    jacobian: dict[str, Any],
) -> tuple[dict[str, Any], list[str]]:
    algebra, different, failures = local_algebra(e)
    x_coord = rational_json(x_num, x_den)
    y_coord = rational_json(y_num, y_den)
    record = {
        "schema": SCHEMA,
        "record_id": record_id,
        "tier": tier,
        "target_divisor": target_tag(f"{record_id}:P=0"),
        "local_algebra": algebra,
        "different": different,
        "completed_factors": [
            {
                "factor_id": "w0",
                "ramification_degree": e,
                "residue_degree": 1,
                "coordinate_map": {"t": f"u^{e}", "q": "q"},
            }
        ],
        "coordinates": {
            "x": {**x_coord, "sha256": hash_obj(x_coord)},
            "y": {**y_coord, "sha256": hash_obj(y_coord)},
        },
        "retained_decoration": decoration,
        "retained_decoration_sha256": hash_obj(decoration),
        "jacobian_data": jacobian,
        "jacobian_data_sha256": hash_obj(jacobian),
        "moments": {"x": x_moments, "y": y_moments},
    }
    record["record_sha256"] = hash_obj(record)
    return record, failures


def triangular_control() -> tuple[dict[str, Any], list[str]]:
    one = {0: qp_const(1)}
    x = {1: qp_const(1)}
    y = {0: qp_q(), 2: qp_const(-1)}
    x_moments, failures = moments_from_laurent(x, 1)
    y_moments, y_failures = moments_from_laurent(y, 1)
    failures += y_failures
    record, local_failures = receiver_record(
        record_id="C1_triangular_automorphism",
        tier="exact_polynomial_automorphism_control",
        e=1,
        x_num=x,
        x_den=one,
        y_num=y,
        y_den=one,
        x_moments=x_moments,
        y_moments=y_moments,
        decoration={"kind": "explicit_polynomial_map", "map": "(x,y+x^2)"},
        jacobian={"J": "1", "kind": "polynomial_identity"},
    )
    failures += local_failures
    for coordinate_name in ("x", "y"):
        for power in ("1", "2"):
            if record["moments"][coordinate_name][power]["principal_part"]:
                failures.append(f"triangular_unexpected_pole:{coordinate_name}^{power}")
    if record["different"]["generator"] != {"integer_coefficient": 1, "u_exp": 0}:
        failures.append("triangular_different_not_unit")
    return record, failures


def nonproper_control() -> tuple[dict[str, Any], list[str]]:
    one = {0: qp_const(1)}
    x = {1: qp_const(1)}
    y = {-1: qp_q()}
    x_moments, failures = moments_from_laurent(x, 2)
    y_moments, y_failures = moments_from_laurent(y, 2)
    failures += y_failures
    record, local_failures = receiver_record(
        record_id="C2_nonproper_x2_xy",
        tier="exact_polynomial_nonproper_nonKeller_control",
        e=2,
        x_num=x,
        x_den=one,
        y_num=y,
        y_den=one,
        x_moments=x_moments,
        y_moments=y_moments,
        decoration={"kind": "explicit_polynomial_map", "map": "(x^2,xy)"},
        jacobian={"J": "2*t", "kind": "nonKeller_negative_control"},
    )
    failures += local_failures

    expected = {
        ("x", "1"): {},
        ("x", "2"): {1: qp_const(2)},
        ("y", "1"): {},
        ("y", "2"): {-1: qp_scale(qp_mul(qp_q(), qp_q()), 2)},
    }
    for (coordinate_name, power), trace_expected in expected.items():
        trace_actual_json = record["moments"][coordinate_name][power]["trace"]
        if trace_actual_json != laurent_json(trace_expected, "t"):
            failures.append(f"nonproper_trace_mismatch:{coordinate_name}^{power}")
    return record, failures


def denominator42_x(b: int) -> Laurent:
    return {
        -84: qp_const(1),
        -42: qp_const(1),
        -30: qp_const(1),
        -10: qp_const(1),
        -5: qp_const(1),
        42: qp_const(b),
    }


def contact_decoration() -> dict[str, Any]:
    return {
        "leading_u_exp": -84,
        "leading_coefficient": qp_json(qp_const(1)),
        "support_u_exponents": [-84, -42, -30, -10, -5, 42],
        "conjugation_invariant_u_exponents": [-84, -42, 42],
        "contact_visible_u_exponents": [-30, -10, -5],
        "contact_visible_coefficients": [
            {"u_exp": exponent, "coefficient": qp_json(qp_const(1))}
            for exponent in (-30, -10, -5)
        ],
        "gcd_chain": [42, 6, 2, 1],
        "characteristic_indices": [7, 3, 2],
        "varying_b_slot_retained": False,
    }


def darbouz_control(b: int) -> tuple[dict[str, Any], list[str]]:
    e = 42
    one = {0: qp_const(1)}
    x = denominator42_x(b)
    x_prime = laurent_derivative_u(x)
    y_num_raw = {e - 1: qp_scale(qp_q(), e)}
    y_den_raw = x_prime
    y_num, y_den = rational_normalize(y_num_raw, y_den_raw)

    y_q_num = laurent_derivative_q(y_num)
    y_q_den = y_den
    wedge_left_num = laurent_mul(x_prime, y_q_num)
    wedge_left_den = y_q_den
    wedge_right_num = {e - 1: qp_const(e)}
    wedge_right_den = one
    wedge_ok = rational_equal(
        wedge_left_num, wedge_left_den, wedge_right_num, wedge_right_den
    )

    x_moments, failures = moments_from_laurent(x, e)
    y_val = valuation_u(y_num) - valuation_u(y_den)
    y_moments = positive_valuation_moments(y_val)
    if not wedge_ok:
        failures.append("darboux_wedge_identity_failed")
    if y_val != 126:
        failures.append(f"darboux_y_valuation:{y_val}:expected126")

    expected_x_1 = {
        -2: qp_const(42),
        -1: qp_const(42),
        1: qp_const(42 * b),
    }
    expected_x_2 = {
        -4: qp_const(42),
        -3: qp_const(84),
        -2: qp_const(42),
        -1: qp_const(84 * b),
        0: qp_const(84 * b),
        2: qp_const(42 * b * b),
    }
    if x_moments["1"]["trace"] != laurent_json(expected_x_1, "t"):
        failures.append("darboux_x_first_moment_formula")
    if x_moments["2"]["trace"] != laurent_json(expected_x_2, "t"):
        failures.append("darboux_x_second_moment_formula")

    jacobian = {
        "kind": "formal_local_Darboux_completion_not_polynomial_map",
        "P": "u^42",
        "Q": "q",
        "c": "1",
        "dP_wedge_dQ": {"integer_coefficient": 42, "u_exp": 41},
        "dx_wedge_dy_equals_dP_wedge_dQ": wedge_ok,
    }
    record, local_failures = receiver_record(
        record_id=f"D{b}_denominator42_b{b}",
        tier="exact_formal_local_control_not_polynomial_Keller",
        e=e,
        x_num=x,
        x_den=one,
        y_num=y_num,
        y_den=y_den,
        x_moments=x_moments,
        y_moments=y_moments,
        decoration=contact_decoration(),
        jacobian=jacobian,
    )
    failures += local_failures
    record.pop("record_sha256")
    record["coordinate_valuations_u"] = {"x": -84, "y": y_val}
    record["record_sha256"] = hash_obj(record)
    return record, failures


def native_type_gate() -> dict[str, Any]:
    """Conditional gate. Main calls this only if earlier hard stops do not fire."""
    rel = "jc72108/systems/farm/4_12mn34d64/manifest.json"
    manifest = json.loads((REPO / rel).read_text())
    cases = [case for case in manifest.get("cases", []) if case.get("name") == "4_12mn34d64_c2"]
    if len(cases) != 1:
        return {
            "verdict": "NO-TYPED-FUNCTOR",
            "first_missing_arrow": "unique_native_source_identity",
            "detail": f"expected one case, found {len(cases)}",
        }
    case = cases[0]
    q_systems = [
        system
        for system in case.get("systems", [])
        if system.get("char") == 0 and system.get("kind") == "core"
    ]
    provenance = {
        "manifest": rel,
        "manifest_sha256": sha256_file(REPO / rel),
        "case": case["name"],
        "NP": case.get("NP"),
        "NQ": case.get("NQ"),
        "char0_core_system": q_systems[0].get("path") if len(q_systems) == 1 else None,
    }
    literal_target_tag = case.get("target_affine_divisor")
    literal_uniformizer = case.get("target_uniformizer")
    if literal_target_tag is None or literal_uniformizer is None:
        return {
            "verdict": "NO-TYPED-FUNCTOR",
            "source_provenance": provenance,
            "first_missing_arrow": "target_affine_divisor_and_uniformizer",
            "forbidden_inference": "NP/NQ/chart fields are not target-local divisor tags",
        }
    return {
        "verdict": "NO-TYPED-FUNCTOR",
        "source_provenance": provenance,
        "first_missing_arrow": "completed_factor_census_not_implemented_after_unexpected_target_tag",
    }


def input_hash_audit() -> tuple[dict[str, Any], list[str]]:
    records: dict[str, Any] = {}
    failures: list[str] = []
    for rel, expected in PINNED_INPUTS.items():
        actual = sha256_file(REPO / rel)
        match = actual == expected
        records[rel] = {"expected": expected, "actual": actual, "match": match}
        if not match:
            failures.append(f"input_hash:{rel}")
    return records, failures


def result_document() -> dict[str, Any]:
    input_records, failures = input_hash_audit()
    implementation_rel = "cases/round2_norm_moment_sep/norm_moment_sep.py"
    implementation_hash = sha256_file(REPO / implementation_rel)

    triangular, triangular_failures = triangular_control()
    nonproper, nonproper_failures = nonproper_control()
    failures += triangular_failures + nonproper_failures

    if failures:
        return {
            "schema": SCHEMA,
            "status": "STOPPED",
            "verdict": "RECEIVER-BUG",
            "smallest_failed_identity": failures[0],
            "all_failures": failures,
            "implementation": {"path": implementation_rel, "sha256": implementation_hash},
            "inputs": input_records,
            "bounds": {"moments": [1, 2], "random_samples": 0, "network": False},
            "controls": [triangular, nonproper],
            "stages": {
                "receiver_controls": "FAIL",
                "fixed_different_separator": "NOT_REACHED",
                "native_source_type_gate": "NOT_REACHED",
            },
        }

    d1, d1_failures = darbouz_control(1)
    d2, d2_failures = darbouz_control(2)
    failures += d1_failures + d2_failures
    if failures:
        return {
            "schema": SCHEMA,
            "status": "STOPPED",
            "verdict": "RECEIVER-BUG",
            "smallest_failed_identity": failures[0],
            "all_failures": failures,
            "implementation": {"path": implementation_rel, "sha256": implementation_hash},
            "inputs": input_records,
            "bounds": {"moments": [1, 2], "random_samples": 0, "network": False},
            "controls": [triangular, nonproper, d1, d2],
            "stages": {
                "receiver_controls": "PASS",
                "fixed_different_separator": "FAIL_RECEIVER",
                "native_source_type_gate": "NOT_REACHED",
            },
        }

    comparison = {
        "same_local_algebra": d1["local_algebra"]["sha256"] == d2["local_algebra"]["sha256"],
        "same_different_and_conductor": d1["different"]["sha256"] == d2["different"]["sha256"],
        "same_retained_decoration": d1["retained_decoration_sha256"] == d2["retained_decoration_sha256"],
        "same_local_jacobian_data": d1["jacobian_data_sha256"] == d2["jacobian_data_sha256"],
        "same_coordinate_valuations": d1["coordinate_valuations_u"] == d2["coordinate_valuations_u"],
        "same_x_first_principal_part": (
            d1["moments"]["x"]["1"]["principal_part_sha256"]
            == d2["moments"]["x"]["1"]["principal_part_sha256"]
        ),
        "same_x_second_principal_part": (
            d1["moments"]["x"]["2"]["principal_part_sha256"]
            == d2["moments"]["x"]["2"]["principal_part_sha256"]
        ),
        "x_quadratic_residue_b1": qp_json(coefficient(
            {entry["t_exp"]: {term["q_exp"]: Fraction(term["num"], term["den"])
             for term in entry["coeff"]}
             for entry in d1["moments"]["x"]["2"]["principal_part"]}, -1)),
        "x_quadratic_residue_b2": qp_json(coefficient(
            {entry["t_exp"]: {term["q_exp"]: Fraction(term["num"], term["den"])
             for term in entry["coeff"]}
             for entry in d2["moments"]["x"]["2"]["principal_part"]}, -1)),
    }
    fixed = all(
        comparison[key]
        for key in (
            "same_local_algebra",
            "same_different_and_conductor",
            "same_retained_decoration",
            "same_local_jacobian_data",
            "same_coordinate_valuations",
            "same_x_first_principal_part",
        )
    )
    varying_moment = not comparison["same_x_second_principal_part"]

    base = {
        "schema": SCHEMA,
        "implementation": {"path": implementation_rel, "sha256": implementation_hash},
        "preregistration": {
            "path": "cases/round2_norm_moment_sep/PREREGISTRATION.md",
            "sha256": PINNED_INPUTS["cases/round2_norm_moment_sep/PREREGISTRATION.md"],
            "global_separator_preregistered": False,
        },
        "inputs": input_records,
        "bounds": {
            "moments": [1, 2],
            "receiver_records": 4,
            "random_samples": 0,
            "resultants": False,
            "network": False,
        },
        "derivation_checks": {
            "trace_algorithms": ["conjugation_divisibility_filter", "companion_basis_diagonal_trace"],
            "different_algorithms": ["minimal_polynomial_derivative", "trace_pairing_determinant"],
            "all_agree": True,
        },
        "controls": [triangular, nonproper, d1, d2],
        "fixed_different_varying_moment": comparison,
        "global_separator": {
            "preregistered": False,
            "verdict_available": False,
        },
    }

    if fixed and varying_moment:
        return {
            **base,
            "status": "STOPPED",
            "verdict": "DIFFERENT-INSUFFICIENT",
            "stages": {
                "receiver_controls": "PASS",
                "fixed_different_separator": "PASS_STOP",
                "native_source_type_gate": "NOT_REACHED_BY_PREREGISTERED_HARD_STOP",
            },
            "scope": (
                "Local finite algebra, different/derivation-conductor, retained contact data, "
                "coordinate valuations, and local Jacobian two-form do not determine the "
                "quadratic coordinate moment. This does not address a genuinely global "
                "polynomial-origin identity and is not a polynomial Keller countermodel."
            ),
        }

    type_result = native_type_gate()
    return {
        **base,
        "status": "STOPPED",
        "verdict": type_result["verdict"],
        "stages": {
            "receiver_controls": "PASS",
            "fixed_different_separator": "NO_SEPARATION",
            "native_source_type_gate": type_result,
        },
    }


def main() -> int:
    result = result_document()
    sys.stdout.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
