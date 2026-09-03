#!/usr/bin/env python3
"""Build exact constant-residue certificates for the two declared branches."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "box/g9966s8-20260903"
STAGE8 = BASE / "runs/delta52/stage8.json"
STAGE8_SINGULAR_INPUT = BASE / "runs/delta52/stage8.sing"
STAGE8_SINGULAR = BASE / "stage8-singular-replay.out"
DELTA2 = Path("/tmp/jc2-lane.OZ2xWA/inputs/stage4.json")
DELTA2_SINGULAR_INPUT = ROOT / "box/g9966band-20260903/runs/delta2/stage4.sing"
DELTA2_SINGULAR = BASE / "delta2-stage4-singular-replay.out"
ENGINE = ROOT / "box/g9966band-20260903/band_engine.py"


def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_bytes(), object_pairs_hook=reject_duplicates)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def singular_sections(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    def section(name: str) -> str:
        match = re.search(rf"BEGIN_{name}\n(.*?)\nEND_{name}", text, re.DOTALL)
        require(match is not None, f"missing Singular section {name}: {path}")
        return match.group(1).strip()
    result = {"dimension": int(section("DIM")), "basis": section("GB"),
              "controls": section("CONTROLS").splitlines(),
              "output_sha256": digest(path)}
    require(result["dimension"] == -1, f"Singular dimension is not -1: {path}")
    require(result["basis"] == "1", f"Singular basis is not 1: {path}")
    require(result["controls"] == ["0", "1", "0"], f"Singular controls failed: {path}")
    return result


def verify_singular_input(stage: dict[str, Any], path: Path) -> dict[str, Any]:
    expressions = [sp.expand(sp.sympify(row["expression"]))
                   for row in stage["joint_elimination"]["residual_rows"]]
    variables = sorted(set().union(*(expr.free_symbols for expr in expressions)), key=str)
    localized = sp.Symbol("rho" if stage["branch"] == "delta2" else "c")
    wrapper = sp.Symbol("Zrho" if stage["branch"] == "delta2" else "Zc")
    if localized not in variables:
        variables.append(localized)
        variables.sort(key=str)
    ringvars = variables + [wrapper]
    singular_expr = lambda expr: str(expr).replace("**", "^")
    ideal_entries = [singular_expr(expr) for expr in expressions] + [f"{wrapper}*{localized}-1"]
    expected = (
        f"ring R=0,({','.join(map(str, ringvars))}),dp;\n"
        f"ideal I={','.join(ideal_entries)};\n"
        "ideal S=std(I);\n"
        'print("BEGIN_DIM"); print(dim(S)); print("END_DIM");\n'
        'print("BEGIN_GB"); print(S); print("END_GB");\n'
        f"ideal EmptyControl={localized},{wrapper}*{localized}-1;\n"
        f"ideal PointControl={localized}-1,{wrapper}*{localized}-1;\n"
        f"ideal RawControl={','.join(singular_expr(expr) for expr in expressions)};\n"
        'print("BEGIN_CONTROLS"); print(reduce(1,std(EmptyControl))); '
        'print(reduce(1,std(PointControl))); print(reduce(1,std(RawControl))); '
        'print("END_CONTROLS");\n'
        "quit;\n"
    )
    require(path.read_text(encoding="utf-8") == expected,
            f"emitted Singular input does not match stage JSON: {path}")
    return {"path": str(path), "sha256": digest(path),
            "byte_identical_reconstruction_from_stage_json": True}


def constant_certificate(stage: dict[str, Any], expected_branch: str,
                         expected_stage: int, expected_label: str,
                         expected_constant: int, singular_input: Path,
                         singular_output: Path) -> dict[str, Any]:
    require(stage["branch"] == expected_branch, "branch mismatch")
    require(stage["stage_spec"]["stage"] == expected_stage, "stage mismatch")
    require(stage["driver_sha256"] == digest(ENGINE), "engine hash mismatch")
    rows = stage["joint_elimination"]["residual_rows"]
    selected = [row for row in rows if row["label"] == expected_label]
    require(len(selected) == 1, f"missing unique residue row: {expected_label}")
    value = sp.sympify(selected[0]["expression"])
    require(not value.free_symbols and value == expected_constant, "constant residue mismatch")
    inverse = sp.Rational(1, expected_constant)
    require(sp.cancel(inverse * value) == 1, "unit-ideal membership check failed")

    pivots = stage["joint_elimination"]["pivot_ledger"]
    for pivot in pivots:
        coefficient = sp.Rational(pivot["coefficient"])
        require(coefficient != 0, f"zero pivot coefficient: {pivot['row']}")
        localized = "rho" if expected_branch == "delta2" else "c"
        require(pivot["variable"] != localized, "localization parameter used as pivot")

    exact = stage["joint_elimination"]["singular"]
    require(exact["unit_ideal"] is True and exact["dimension"] == -1,
            "embedded exact Singular result is not unit")
    require(exact["basis_preview"] == ["1"] and exact["raw_residue_unit_ideal"] is True,
            "embedded exact basis/raw-unit status mismatch")
    return {
        "branch": expected_branch,
        "stage": expected_stage,
        "stage_spec": stage["stage_spec"],
        "reduced_row": expected_label,
        "constant": str(value),
        "membership_witness_over_Q": f"1 = ({inverse})*{expected_label}",
        "residual_count": stage["joint_elimination"]["residual_count"],
        "residual_sha256": stage["joint_elimination"]["residual_hash"],
        "Qstar_pivot_count": len(pivots),
        "Qstar_pivots_checked_nonzero_rational": True,
        "localization_parameter_excluded_from_pivots": True,
        "wrapper": exact["wrapper"],
        "raw_residue_unit_ideal": True,
        "localized_unit_ideal": True,
        "embedded_singular": exact,
        "emitted_singular_input": verify_singular_input(stage, singular_input),
        "independent_singular_replay": singular_sections(singular_output),
        "verdict": stage["verdict"],
    }


def main() -> None:
    delta52 = load_json(STAGE8)
    delta2 = load_json(DELTA2)
    c52 = constant_certificate(delta52, "delta52", 8,
                               "stage8_G_local16_coord0", 64,
                               STAGE8_SINGULAR_INPUT, STAGE8_SINGULAR)
    c2 = constant_certificate(delta2, "delta2", 4,
                              "stage4_J_d159_k35", 6264,
                              DELTA2_SINGULAR_INPUT, DELTA2_SINGULAR)
    require(c52["localized_unit_ideal"] and c2["localized_unit_ideal"],
            "not all declared branches are dead")
    print(json.dumps({
        "schema": "g9966-declared-joint-chart-constant-unit-certificate-v1",
        "coefficient_field": "Q",
        "engine": {"path": str(ENGINE), "sha256": digest(ENGINE)},
        "delta52_stage8_json": {"path": str(STAGE8), "sha256": digest(STAGE8)},
        "delta2_stage4_json": {"path": str(DELTA2), "sha256": digest(DELTA2)},
        "certificates": [c2, c52],
        "all_declared_branches_dead": True,
        "typed_chart_verdict": "NO-SURVIVING-BRANCH[DECLARED-(99,66)-JOINT-CHART]",
        "scope_warning": "Depends on chart necessity, branch exhaustiveness, and the imported coordinate/branch gates; not unrestricted JC2.",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
