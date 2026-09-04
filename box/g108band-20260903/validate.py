#!/usr/bin/env python3
"""Validate the bounded final artifact set for the D=108 joint-band lane.

The five primary JSON paths are explicit command-line inputs.  No directory is
scanned recursively: companion replay/custody artifacts have fixed names or
are named by their owning JSON.  Successful validation writes only
``validation.json`` and ``artifact-manifest.sha256`` below ``--output-dir``.

The no-split computation is deliberately two-tiered.  Its compiler may return
a conditional unit ideal, but the only promotable status accepted here is
``OPEN[DESCENT-SUPPORT/VARIABLE-MAP]`` until the stated map/support gap closes.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
from typing import Any, Iterable

import sympy as sp


EXPECTED_RESIDUE = {
    "minor_n6_pi0": "-jet2**2",
    "minor_n7_pi0": "2*jet1**2*jet2",
    "minor_n7_pi1": "-2*jet2",
    "minor_n8_pi0": "-c - jet1**4 + 9*jet1*jet2**2",
    "minor_n8_pi1": "2*jet1**2",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path, role: str) -> dict[str, Any]:
    require(path.is_file(), f"missing {role}: {path}")
    value = json.loads(
        path.read_bytes(),
        object_pairs_hook=reject_duplicate_keys,
    )
    require(isinstance(value, dict), f"{role} is not a JSON object: {path}")
    return value


def atomic_write(path: Path, payload: str) -> None:
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)


def expect(mapping: dict[str, Any], key: str, value: Any, context: str) -> None:
    require(key in mapping, f"missing {context}.{key}")
    require(
        mapping[key] == value,
        f"{context}.{key}: expected {value!r}, got {mapping[key]!r}",
    )


def expect_true_values(mapping: dict[str, Any], context: str) -> None:
    require(mapping, f"empty Boolean control map: {context}")
    for key, value in mapping.items():
        require(value is True, f"failed control {context}.{key}: {value!r}")


def validate_datum(datum: dict[str, Any], context: str) -> None:
    expect(datum, "degrees", [108, 72], context)
    expect(datum, "M", [-72, 81, 106], context)
    expect(datum, "d", [108, 36, 9, 1], context)
    expect(datum, "V", [7, 7], context)
    expect(datum, "u3", 2, context)
    expect(datum, "v3", 7, context)
    split = datum["split"]
    expected_split = {
        "delta": 3,
        "partition": [1, 1],
        "p": "pi^2-c",
        "q": "p^23*U",
        "U_prime": "5*p^2",
        "degree_U": 5,
        "mod_gauge": "one parameter e0",
        "tree": "24 -> 12+12; final order 4 on both children",
    }
    require(split == expected_split, f"{context}.split mismatch")


def validate_tower(tower: dict[str, Any], context: str) -> None:
    raw = {
        "H": 54,
        "C2": 135,
        "C3": 216,
        "C4": 297,
        "A2": 1998,
        "A3": 3294,
        "B1": 702,
        "B2": 1998,
    }
    fixed = {
        "H": 45,
        "C2": 126,
        "C3": 207,
        "C4": 288,
        "A2": 1962,
        "A3": 3258,
        "B1": 666,
        "B2": 1962,
    }
    expect(tower, "raw_blocks", raw, context)
    expect(tower, "fixed_top_blocks", fixed, context)
    expect(tower, "fixed_top_total", 8514, context)
    require(sum(raw.values()) == 8694, "raw tower total is not 8694")
    require(sum(fixed.values()) == 8514, "fixed tower total is not 8514")
    expect(tower, "h3", "P; degree 9; top y^2*(y-x)^7", context)
    expect(tower, "h2", "P^4+C2*P^2+C3*P+C4; degree 36", context)
    expect(tower, "F", "h2^3+A2*h2+A3; degree 108", context)
    expect(tower, "G", "h2^2+B1*h2+B2; degree 72", context)


def validate_major(major: dict[str, Any], context: str) -> None:
    h3 = major["h3_D2"]
    for key, value in {
        "fixed_top_lower_ambient": 45,
        "strict_order_rows": 36,
        "strict_order_rank": 36,
        "face_incidence_rows": 2,
        "face_incidence_rank": 2,
        "surviving_count": 7,
    }.items():
        expect(h3, key, value, f"{context}.h3_D2")
    expect(h3, "equality_sites", [[3, 5], [6, 3]], f"{context}.h3_D2")
    expect(
        h3,
        "surviving_coordinates",
        [[1, 7], [1, 8], [2, 6], [2, 7], [3, 6], [4, 5], [5, 4]],
        f"{context}.h3_D2",
    )

    h2d2 = major["h2_D2"]
    for key, value in {
        "nominal_rows": 566,
        "strict_Theorem_1_2_rows": 558,
        "face_incidence_rows": 8,
        "rank": 565,
        "residual_rows": 0,
        "dimension_after_D2": 63,
    }.items():
        expect(h2d2, key, value, f"{context}.h2_D2")
    expect(h2d2, "unit_pivots", {"C2": 79, "C3": 198, "C4": 288}, f"{context}.h2_D2")
    expect(h2d2, "identity_sites", [[1, 27]], f"{context}.h2_D2")

    h2d1 = major["h2_D1"]
    for key, value in {
        "raw_rows": 4,
        "rank": 4,
        "residual_rows": 0,
        "primitive_weight": 85,
        "full_weight": 170,
        "face_leading_exponent": 344,
        "chosen_minor_determinant": "64",
    }.items():
        expect(h2d1, key, value, f"{context}.h2_D1")
    expect(h2d1, "row_exponents", [340, 341, 342, 343], f"{context}.h2_D1")
    expect(h2d1, "chosen_q_values", [25, 23, 21, 19], f"{context}.h2_D1")

    analogue = major["post_h3_ambient_516_analogue"]
    expect(analogue, "total", 628, f"{context}.post_h3_ambient_516_analogue")
    require(
        analogue == {"H": 7, "C2": 126, "C3": 207, "C4": 288, "total": 628},
        "628-row analogue block accounting mismatch",
    )
    joint = major["joint_major"]
    expected_joint = {
        "fixed_inner_ambient": 666,
        "post_h3_ambient": 628,
        "free_h3_projection_dimension": 7,
        "h3_D2_rank": 38,
        "h2_D2_rank": 565,
        "h2_D1_rank": 4,
        "total_rank_from_fixed_inner": 607,
        "free_dimension": 59,
    }
    require(joint == expected_joint, f"{context}.joint_major mismatch")
    require(38 + 565 + 4 == 607 and 666 - 607 == 59, "major rank arithmetic failed")
    expect_true_values(major["controls"], f"{context}.controls")


def validate_outer(outer: dict[str, Any], context: str) -> None:
    expect(outer, "type", "EXACT-Q / OUTER-THEOREM-1.2-BANDS / D108", context)
    totals = outer["totals"]
    expected_totals = {
        "fixed_outer_ambient": 7848,
        "D2_rank": 7656,
        "retained_after_D2": 192,
        "D1_raw_rows": 92,
        "D1_rank": 54,
        "D1_dependent_rows": 38,
        "rank_D2_plus_D1": 7710,
        "outer_free_dimension": 138,
        "redundant_D1_labels_on_D2_deleted_support": 16057,
    }
    require(totals == expected_totals, f"{context}.totals mismatch")
    require(7848 - 7656 == 192, "outer D2 arithmetic failed")
    require(192 - 54 == 138, "outer D1 arithmetic failed")
    require(92 - 54 == 38, "outer dependency arithmetic failed")

    expect(
        outer,
        "primitive_weight_offsets",
        [
            {"offset": 0, "raw_rows": 40, "rank": 20},
            {"offset": 1, "raw_rows": 28, "rank": 16},
            {"offset": 2, "raw_rows": 16, "rank": 10},
            {"offset": 3, "raw_rows": 8, "rank": 8},
        ],
        context,
    )
    expected_blocks = {
        "A2": (71, 1962, 166, 1920, 42, 680, 40, 21, 19, 3983),
        "A3": (107, 3258, 250, 3258, 0, 1024, 0, 0, 0, 6992),
        "B1": (35, 666, 82, 558, 108, 336, 12, 12, 0, 1099),
        "B2": (71, 1962, 166, 1920, 42, 680, 40, 21, 19, 3983),
    }
    require(set(outer["blocks"]) == set(expected_blocks), f"{context}.blocks keys mismatch")
    for name, expected_values in expected_blocks.items():
        block = outer["blocks"][name]
        d2 = block["D2"]
        d1 = block["D1"]
        actual_values = (
            block["fixed_top_degree"],
            block["ambient"],
            d2["primitive_threshold"],
            d2["rank"],
            d2["retained"],
            d1["exponent_threshold"],
            d1["raw_rows"],
            d1["rank"],
            d1["dependent_rows"],
            block["redundant_D1_labels_on_D2_deleted_support"],
        )
        require(actual_values == expected_values, f"{context}.blocks.{name} mismatch")
        require(d2["strict_coordinate_rows"] == d2["rank"], f"{name} D2 row/rank mismatch")
    expect_true_values(outer["controls"], f"{context}.controls")


def verify_incidence_certificate(minor: dict[str, Any], context: str) -> None:
    expect(minor, "residual", EXPECTED_RESIDUE, context)
    expect(minor, "residual_count", 5, context)
    qstar = minor["Qstar"]
    expect(qstar, "rank", 7, f"{context}.Qstar")
    expect(qstar, "dependent_zero_rows", 1, f"{context}.Qstar")
    expect(qstar, "excluded", ["jet1", "jet2", "c", "e0", "Zc"], f"{context}.Qstar")
    require(len(qstar["pivots"]) == 7, "minor Q* pivot ledger length mismatch")
    excluded = set(qstar["excluded"])
    pivot_variables: set[str] = set()
    for pivot in qstar["pivots"]:
        variable = pivot["variable"]
        require(variable not in excluded, f"excluded minor parameter pivoted: {variable}")
        require(variable not in pivot_variables, f"duplicate minor pivot: {variable}")
        pivot_variables.add(variable)
        require(Fraction(pivot["coefficient"]) != 0, f"zero/nonrational pivot: {pivot}")

    certificate = minor["certificate"]
    expect(certificate, "wrapper", "Zc*c - 1", f"{context}.certificate")
    expect(certificate, "localized_unit_ideal", True, f"{context}.certificate")
    expect(certificate, "expanded_identity", "1", f"{context}.certificate")
    jet1, jet2, c, Zc = sp.symbols("jet1 jet2 c Zc")
    local_symbols = {"jet1": jet1, "jet2": jet2, "c": c, "Zc": Zc}
    total = sp.Integer(0)
    coefficients = certificate["coefficients"]
    for label, expression in EXPECTED_RESIDUE.items():
        coefficient = sp.sympify(coefficients[label], locals=local_symbols)
        row = sp.sympify(expression, locals=local_symbols)
        total += coefficient * row
    total += sp.sympify(
        coefficients["localization_Zc_c_minus_1"], locals=local_symbols
    ) * (Zc * c - 1)
    require(sp.expand(total) == 1, "minor incidence membership certificate failed")


def validate_custody(owner: dict[str, Any], directory: Path, context: str) -> tuple[Path, Path]:
    custody = owner["custody"]
    expect(custody, "all_hashes_match", True, context)
    expect(custody, "charged_inputs", 18, context)
    expect(custody, "sha256sum_check_lines", 18, context)
    expect(
        custody,
        "manifest_sha256",
        "530034c276bc8e84b9a3d4a3078d023d6d13d61bd8547c2172091784567d60a7",
        context,
    )
    expect(
        custody,
        "receipt_sha256",
        "aab531983bfb7b96982261d285024a29ce38b7118ca551d99a9370d88cdb4c37",
        context,
    )
    checked = custody["checked"]
    require(len(checked) == 18, f"{context}.checked length mismatch")
    require(len({item["basename"] for item in checked}) == 18, f"{context}.checked duplicate names")

    manifest_path = directory / "inputs.sha256"
    check_path = directory / "inputs.sha256.check.log"
    require(manifest_path.is_file(), f"missing custody manifest: {manifest_path}")
    require(check_path.is_file(), f"missing custody check log: {check_path}")
    require(sha256(manifest_path) == custody["manifest_sha256"], "custody manifest hash mismatch")
    manifest_rows = []
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        require(match is not None, f"malformed custody manifest row: {line!r}")
        expected_hash, filename = match.groups()
        source = Path(filename)
        require(source.is_file(), f"missing frozen charged input: {source}")
        require(sha256(source) == expected_hash, f"charged input hash mismatch: {source}")
        manifest_rows.append((source.name, expected_hash))
    require(len(manifest_rows) == 18, "custody manifest does not have 18 rows")
    require(
        manifest_rows == [(item["basename"], item["sha256"]) for item in checked],
        "custody JSON/manifest order or digest mismatch",
    )
    check_lines = check_path.read_text(encoding="utf-8").splitlines()
    require(len(check_lines) == 18, "custody check log does not have 18 lines")
    require(all(line.endswith(": OK") for line in check_lines), "custody check log has failures")
    return manifest_path, check_path


def validate_skeleton(skeleton: dict[str, Any], path: Path) -> tuple[Path, Path]:
    expect(skeleton, "type", "D108-JOINT-BAND-ENGINE / EXACT-Q", "skeleton")
    expect(skeleton, "mode", "skeleton-only", "skeleton")
    validate_datum(skeleton["datum"], "skeleton.datum")
    validate_tower(skeleton["tower"], "skeleton.tower")
    validate_major(skeleton["major_structure"], "skeleton.major_structure")
    validate_outer(skeleton["outer"], "skeleton.outer")
    verify_incidence_certificate(skeleton["minor_incidence"], "skeleton.minor_incidence")
    stage = skeleton["stage"]
    for key, value in {
        "stage": 0,
        "branch": "delta3",
        "status": "COMPILED-SKELETON",
        "reached": False,
        "fixed_chart_coordinates": 8514,
        "ambient_before_wrapper": 8518,
        "major_order_rank": 607,
        "outer_D2_rank": 7656,
        "outer_D1_rank": 54,
        "outer_rank": 7710,
        "dimension_before_minor_incidence": 201,
        "joint_Qstar_pivots_new": 7,
        "joint_Qstar_pivots_cumulative": 8324,
        "dimension_after_Qstar_before_residue": 194,
        "nonlinear_residue_rows": 5,
        "exact_localized_dimension": None,
        "killing_family": None,
        "stop_reason": None,
    }.items():
        expect(stage, key, value, "skeleton.stage")
    expect(stage, "branch_parameters", ["jet1", "jet2", "c", "e0"], "skeleton.stage")
    expect(stage, "residue", EXPECTED_RESIDUE, "skeleton.stage")
    require(8518 - 607 - 7710 == 201, "pre-incidence dimension arithmetic failed")
    require(201 - 7 == 194, "post-Q* dimension arithmetic failed")
    expect(skeleton["Singular"], "status", "not run in skeleton-only mode", "skeleton.Singular")
    fallacy = skeleton["FALLACY_v2"]
    for key in (
        "flag_place_series_separated",
        "strict_below_and_at_level_separated",
    ):
        expect(fallacy, key, True, "skeleton.FALLACY_v2")
    expect(fallacy, "representative_claimed", False, "skeleton.FALLACY_v2")
    expect(fallacy, "exit_price_assertion_made", False, "skeleton.FALLACY_v2")
    return validate_custody(skeleton, path.parent, "skeleton.custody")


def validate_stage0(
    stage0: dict[str, Any],
    skeleton: dict[str, Any],
    path: Path,
) -> tuple[Path, Path, Path, Path]:
    expect(stage0, "type", "D108-JOINT-BAND-ENGINE / EXACT-Q", "stage0")
    expect(stage0, "mode", "stage-0", "stage0")
    for key in (
        "datum",
        "tower",
        "major_structure",
        "outer",
        "minor_incidence",
        "continuation_metadata",
        "FALLACY_v2",
    ):
        require(stage0[key] == skeleton[key], f"stage0/skeleton mismatch in {key}")
    stage = stage0["stage"]
    for key, value in {
        "stage": 0,
        "branch": "delta3",
        "status": "DEAD",
        "reached": True,
        "exact_localized_dimension": -1,
        "killing_family": "common-h3 minor incidence",
        "stop_reason": "explicit localized unit certificate",
        "major_order_rank": 607,
        "outer_D2_rank": 7656,
        "outer_D1_rank": 54,
        "outer_rank": 7710,
        "joint_Qstar_pivots_new": 7,
        "joint_Qstar_pivots_cumulative": 8324,
        "nonlinear_residue_rows": 5,
    }.items():
        expect(stage, key, value, "stage0.stage")
    expect(stage, "residue", EXPECTED_RESIDUE, "stage0.stage")
    expect(
        stage,
        "scheduled_but_unreached",
        [
            "prior six direct F/G pole rows",
            "prior ten Jacobian rows",
            "stage-0 F/G local-power-4 rows",
            "stage-0 Jacobian w^25 row",
        ],
        "stage0.stage",
    )

    singular = stage0["Singular"]
    require(
        singular["main"] == {"basis_size": 1, "dimension": -1, "normal_form_of_1": 0},
        "stage0 Singular main result mismatch",
    )
    controls = singular["controls"]
    require(
        controls["empty_c_and_c_invertible"] == {"dimension": -1, "normal_form_of_1": 0},
        "stage0 empty localization control mismatch",
    )
    require(
        controls["point_c_equals_1"]["dimension"] == 2
        and controls["point_c_equals_1"]["normal_form_of_1"] == 1,
        "stage0 point control mismatch",
    )
    require(
        controls["raw_without_localization"]["dimension"] == 1
        and controls["raw_without_localization"]["normal_form_of_1"] == 1,
        "stage0 raw control mismatch",
    )
    expect(controls, "lift_printed", True, "stage0.Singular.controls")
    script_path = path.parent / "death_replay.sing"
    log_path = path.parent / "death_replay.log"
    require(script_path.is_file() and log_path.is_file(), "missing stage0 death replay")
    require(sha256(script_path) == singular["script_sha256"], "stage0 replay script hash mismatch")
    require(sha256(log_path) == singular["log_sha256"], "stage0 replay log hash mismatch")
    log = log_path.read_text(encoding="utf-8")
    for fragment in (
        "MAIN_DIM\n-1",
        "MAIN_SIZE\n1",
        "MAIN_NF1\n0",
        "RAW_DIM\n1",
        "RAW_NF1\n1",
        "EMPTY_CONTROL_DIM\n-1",
        "EMPTY_CONTROL_NF1\n0",
        "POINT_CONTROL_DIM\n2",
        "POINT_CONTROL_NF1\n1",
    ):
        require(fragment in log, f"stage0 replay log missing {fragment!r}")
    custody_paths = validate_custody(stage0, path.parent, "stage0.custody")
    return script_path, log_path, *custody_paths


def validate_controls(controls: dict[str, Any], path: Path) -> list[Path]:
    expect(controls, "schema", "g108band-exact-Q-controls-v1", "controls")
    expect(controls, "controls_pass", True, "controls")
    parent = controls["parent_reduction"]
    expected_parent = {
        "parent_degrees": [64, 48],
        "M_1_through_M_3": [-48, 52, 62],
        "d_1_through_d_4": [64, 16, 4, 2],
        "V_2_V_3": [3, 3],
        "d_s": 4,
        "v_s": 3,
        "u_s": 1,
        "descent_factor": 4,
        "reduced_degrees": [16, 12],
        "bridge": "TRIVIAL[u_s=1]",
    }
    require(parent == expected_parent, "Appendix-II parent reduction mismatch")
    appendix = controls["appendix_ii"]
    expect(appendix, "both_exact_Q_localizations_empty", True, "controls.appendix_ii")
    variants = appendix["variants"]
    require(
        {variant["variant"] for variant in variants}
        == {"printed_repeated_c5", "absorbed_alpha1_distinct_c6"},
        "Appendix-II variant set mismatch",
    )
    scripts: list[Path] = []
    expected_control_values = {
        "raw_reduce_1": "1",
        "localized_reduce_1": "0",
        "empty_c_and_wrapper_reduce_1": "0",
        "point_c1_and_wrapper_reduce_1": "1",
        "localized_unit_lift_recomposition": "1",
    }
    for variant in variants:
        for key, value in {
            "field": "Q",
            "ordering": "dp",
            "n_coefficient_variables": 17,
            "n_unknowns_before_wrapper": 18,
            "n_J_coefficient_rows": 77,
            "wrapper": "Zc*c-1",
            "raw_origin_c0_verified": True,
            "localized_dimension": -1,
            "localized_basis": "1",
            "verdict": "SATURATED-EMPTY[P208-COMMON-POLYNOMIAL-ANSATZ/Q]",
        }.items():
            expect(variant, key, value, f"controls.{variant['variant']}")
        require(variant["controls"] == expected_control_values, "Appendix-II control values mismatch")
        script_name = variant["singular_script"]
        require(Path(script_name).name == script_name, "unsafe controls replay basename")
        script_path = path.parent / script_name
        require(script_path.is_file(), f"missing controls replay script: {script_path}")
        require(sha256(script_path) == variant["singular_script_sha256"], "controls script hash mismatch")
        scripts.append(script_path)
    tame = controls["tame_automorphism"]
    expect(tame, "survives", True, "controls.tame_automorphism")
    expect(tame["pair"], "J", "1", "controls.tame_automorphism.pair")
    expect(tame["slice_A2_C1"], "J", "1", "controls.tame_automorphism.slice")
    expect_true_values(tame["checks"], "controls.tame_automorphism.checks")
    return scripts


def status_text(value: Any) -> str:
    if isinstance(value, str):
        return value
    return json.dumps(value, sort_keys=True)


def validate_descent(descent: dict[str, Any], path: Path) -> list[Path]:
    expect(descent, "schema", "g108-prop63-descent-v1", "descent")
    datum = descent["datum"]
    expected_datum = {
        "n": 24,
        "m": 16,
        "M": [-16, 18],
        "d": [24, 8, 2],
        "V": [7, 2],
        "k": 4,
        "height_defect": 6,
        "jet_height": 7,
        "s_prime": 2,
        "u_prime": 1,
        "v_prime": 7,
    }
    for key, value in expected_datum.items():
        expect(datum, key, value, "descent.datum")
    support = descent["source_support_audit"]
    expect(support, "strict_below_exponents", [0, 2, 4, 6], "descent.source_support_audit")
    expect(support, "at_level_exponent", 7, "descent.source_support_audit")
    expect(support, "restricts_enlarged_diagnostic", False, "descent.source_support_audit")
    compiler = descent["compiler"]
    for key, value in {
        "n_coefficient_unknowns": 13,
        "n_ring_generators": 14,
        "n_raw_J_rows": 26,
        "n_charged_equations": 26,
        "n_localized_equations_including_wrapper": 27,
        "h_adic_row_split": [18, 8],
        "jacobian_coefficient_mode": "h-adic-monic-y-normal-form",
    }.items():
        expect(compiler, key, value, "descent.compiler")
    local_symbols = {
        name: sp.Symbol(name)
        for name in [*compiler["generator_order"], "x", "y"]
    }
    h_poly = sp.sympify(compiler["h"], locals=local_symbols)
    beta_poly = sp.sympify(compiler["beta"], locals=local_symbols)
    alpha_poly = sp.sympify(compiler["alpha_quotient"], locals=local_symbols)
    quotient, _remainder = sp.div(
        sp.Poly(sp.expand(beta_poly**2), local_symbols["y"]),
        sp.Poly(h_poly, local_symbols["y"]),
        local_symbols["y"],
    )
    require(
        sp.expand(quotient.as_expr() - alpha_poly) == 0,
        "descent alpha_quotient is not quotient_y(beta^2,h)",
    )

    expect(descent, "conditional_only", True, "descent")
    expect(
        descent,
        "promoted_status",
        "OPEN[DESCENT-SUPPORT/VARIABLE-MAP]",
        "descent",
    )
    singular = descent["singular"]
    allowed_outcomes = {
        "UNIT[CONDITIONAL-ENLARGED-CHARGED-COMPILER]",
        "NONUNIT[CONDITIONAL-ENLARGED-CHARGED-COMPILER]",
        "NOT-RUN[SINGULAR-NOT-FOUND]",
        "BUDGET[SINGULAR-TIMEOUT]",
        "ERROR[SINGULAR-NONZERO-EXIT]",
    }
    outcome = singular["outcome"]
    require(outcome in allowed_outcomes, f"unknown descent Singular outcome: {outcome}")
    unit_ideal = singular["unit_ideal"]
    if outcome == "UNIT[CONDITIONAL-ENLARGED-CHARGED-COMPILER]":
        expect(singular, "ran", True, "descent.singular")
        expect(singular, "returncode", 0, "descent.singular")
        expect(singular, "unit_ideal", True, "descent.singular")
        expect(singular, "localized_dimension", -1, "descent.singular")
        expect(singular, "localized_basis", "1", "descent.singular")
        require(singular["unit_lift"].strip(), "conditional descent unit lift is empty")
        expected_controls = {
            "raw_reduce_1": "1",
            "localized_reduce_1": "0",
            "empty_c_and_wrapper_reduce_1": "0",
            "point_c1_and_wrapper_reduce_1": "1",
            "localized_unit_lift_recomposition": "1",
        }
        require(singular["controls"] == expected_controls, "conditional descent controls mismatch")
        require(
            descent["diagnostic_status"]
            == "DEAD[CONDITIONAL-ENLARGED-CHARGED-COMPILER]",
            "conditional unit not typed with the exact diagnostic DEAD status",
        )
        # This is the central non-promotion guard.
        require(
            descent["promoted_status"] == "OPEN[DESCENT-SUPPORT/VARIABLE-MAP]",
            "conditional descent unit was improperly promoted",
        )
    elif outcome == "NONUNIT[CONDITIONAL-ENLARGED-CHARGED-COMPILER]":
        expect(singular, "ran", True, "descent.singular")
        expect(singular, "returncode", 0, "descent.singular")
        expect(singular, "unit_ideal", False, "descent.singular")
        require(
            descent["diagnostic_status"] == "OPEN[CONDITIONAL-COMPILER-NONUNIT]",
            "conditional nonunit diagnostic status mismatch",
        )
    else:
        require(unit_ideal is None, "unfinished/error descent run has a promoted unit status")
        require(
            descent["diagnostic_status"] == outcome,
            "unfinished/error descent diagnostic must equal its Singular outcome",
        )

    companions = [
        path.parent / "descent-system.txt",
        path.parent / "descent-replay.sing",
        path.parent / "descent-singular.log",
    ]
    for companion in companions:
        require(companion.is_file(), f"missing descent companion: {companion}")
    return companions


def bounded_artifacts(items: Iterable[tuple[str, Path]]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    seen: set[Path] = set()
    for role, path in items:
        resolved = path.resolve()
        require(resolved not in seen, f"duplicate artifact path: {resolved}")
        require(resolved.is_file(), f"missing artifact {role}: {resolved}")
        seen.add(resolved)
        records.append(
            {
                "role": role,
                "path": str(resolved),
                "bytes": resolved.stat().st_size,
                "sha256": sha256(resolved),
            }
        )
    require(len(records) <= 24, f"artifact list is not bounded: {len(records)} entries")
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skeleton", type=Path, required=True)
    parser.add_argument("--stage0", type=Path, required=True)
    parser.add_argument("--outer", type=Path, required=True)
    parser.add_argument("--controls", type=Path, required=True)
    parser.add_argument("--descent", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    skeleton = load_json(args.skeleton, "skeleton JSON")
    stage0 = load_json(args.stage0, "stage-0 JSON")
    outer = load_json(args.outer, "outer-band JSON")
    controls = load_json(args.controls, "controls JSON")
    descent = load_json(args.descent, "descent JSON")

    skeleton_custody = validate_skeleton(skeleton, args.skeleton)
    stage_companions = validate_stage0(stage0, skeleton, args.stage0)
    validate_outer(outer, "outer")
    require(outer == skeleton["outer"], "standalone outer JSON differs from engine outer block")
    controls_scripts = validate_controls(controls, args.controls)
    descent_companions = validate_descent(descent, args.descent)

    driver_dir = Path(__file__).resolve().parent
    driver_paths = [
        driver_dir / "band_engine.py",
        driver_dir / "outer_order_bands.py",
        driver_dir / "controls.py",
        driver_dir / "descent_engine.py",
        driver_dir / "validate.py",
    ]
    for driver_path in driver_paths:
        require(driver_path.is_file(), f"missing local driver: {driver_path}")
    for owner, context in ((skeleton, "skeleton"), (stage0, "stage0")):
        provenance = owner["driver_provenance"]
        require(
            provenance["band_engine_sha256"] == sha256(driver_paths[0]),
            f"{context} band_engine source hash mismatch",
        )
        require(
            provenance["outer_order_bands_sha256"] == sha256(driver_paths[1]),
            f"{context} outer_order_bands source hash mismatch",
        )

    death_certificate_path = args.stage0.parent / "death_certificate.json"
    death_certificate = load_json(death_certificate_path, "death certificate")
    expect(death_certificate, "status", "DEAD", "death_certificate")
    expect(death_certificate, "ring", "Q[jet1,jet2,c,Zc]", "death_certificate")
    require(
        death_certificate["residual"] == stage0["minor_incidence"]["residual"],
        "death certificate residue differs from stage0",
    )
    require(
        death_certificate["certificate"] == stage0["minor_incidence"]["certificate"],
        "death certificate identity differs from stage0",
    )
    independent_replay = args.stage0.parent / "death_replay.independent.log"
    require(independent_replay.is_file(), "missing independent death replay")
    require(
        independent_replay.read_bytes() == stage_companions[1].read_bytes(),
        "independent death replay differs from engine replay",
    )

    artifact_items: list[tuple[str, Path]] = [
        ("skeleton_json", args.skeleton),
        ("skeleton_inputs_manifest", skeleton_custody[0]),
        ("skeleton_inputs_check", skeleton_custody[1]),
        ("stage0_json", args.stage0),
        ("stage0_singular_script", stage_companions[0]),
        ("stage0_singular_log", stage_companions[1]),
        ("stage0_independent_singular_log", independent_replay),
        ("stage0_death_certificate", death_certificate_path),
        ("stage0_inputs_manifest", stage_companions[2]),
        ("stage0_inputs_check", stage_companions[3]),
        ("outer_json", args.outer),
        ("controls_json", args.controls),
        ("controls_printed_singular", controls_scripts[0]),
        ("controls_compiler_singular", controls_scripts[1]),
        ("descent_json", args.descent),
        ("descent_system", descent_companions[0]),
        ("descent_singular_script", descent_companions[1]),
        ("descent_singular_log", descent_companions[2]),
        ("band_engine_source", driver_paths[0]),
        ("outer_order_bands_source", driver_paths[1]),
        ("controls_source", driver_paths[2]),
        ("descent_engine_source", driver_paths[3]),
        ("validator_source", driver_paths[4]),
    ]
    artifacts = bounded_artifacts(artifact_items)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    validation_path = args.output_dir / "validation.json"
    manifest_path = args.output_dir / "artifact-manifest.sha256"
    protected = {validation_path.resolve(), manifest_path.resolve()}
    require(
        not any(Path(item["path"]) in protected for item in artifacts),
        "validation outputs cannot be input artifacts",
    )
    manifest = "".join(f"{item['sha256']}  {item['path']}\n" for item in artifacts)
    result = {
        "schema": "g108-joint-band-validation-v1",
        "status": "VALIDATED",
        "split_branch": {
            "stage": 0,
            "status": "DEAD",
            "killing_family": "common-h3 minor incidence",
            "exact_localized_dimension": -1,
        },
        "outer_ranks": {
            "D2": 7656,
            "D1": 54,
            "total": 7710,
            "remaining": 138,
        },
        "major_ranks": {"h3_D2": 38, "h2_D2": 565, "h2_D1": 4, "total": 607},
        "control_status": {
            "appendix_II_exact_Q": "SATURATED-EMPTY[both readings]",
            "tame_automorphism": "SURVIVES",
        },
        "no_split_alternative": {
            "conditional_diagnostic": descent["diagnostic_status"],
            "conditional_only": True,
            "promoted_status": "OPEN[DESCENT-SUPPORT/VARIABLE-MAP]",
        },
        "artifact_manifest": {
            "path": str(manifest_path.resolve()),
            "entry_count": len(artifacts),
            "sha256": hashlib.sha256(manifest.encode("utf-8")).hexdigest(),
            "entries": artifacts,
        },
        "fallacy_v2": {
            "representative_claimed": False,
            "exit_price_assertion_made": False,
            "conditional_descent_not_promoted": True,
        },
    }
    validation = json.dumps(result, indent=2, sort_keys=True) + "\n"
    atomic_write(validation_path, validation)
    atomic_write(manifest_path, manifest)
    print(validation, end="")


if __name__ == "__main__":
    main()
