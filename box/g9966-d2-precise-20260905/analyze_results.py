#!/usr/bin/env python3
"""Validate completed stage artifacts and summarize exact-Q verdict evidence."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re

import sympy as sp


HERE = Path(__file__).resolve().parent
PATCHED_SHA = hashlib.sha256((HERE / "band_engine.py").read_bytes()).hexdigest()
EXPECTED = {"delta2": range(5), "delta52": range(9)}
EXPECTED_INNER = {"delta2": 105, "delta52": 103}
CONTROL = json.loads((HERE / "certificates/control-validation.json").read_text())
assert CONTROL["status"] == "PASS"


def parse_time(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    def field(pattern: str) -> str | None:
        match = re.search(pattern, text, re.MULTILINE)
        return match.group(1).strip() if match else None
    return {
        "elapsed": field(r"^\s*Elapsed \(wall clock\) time.*\):\s*(\S+)\s*$"),
        "maximum_rss_kib": int(field(r"^\s*Maximum resident set size \(kbytes\):\s*(\d+)$") or -1),
        "exit_status": int(field(r"^\s*Exit status:\s*(\d+)$") or -1),
    }


def inspect(branch: str, stage: int) -> dict:
    stem = HERE / "runs" / branch / f"stage{stage}"
    required = [stem.with_suffix(f".{suffix}") for suffix in ("json", "err", "sing", "time", "rc")]
    missing = [str(path.relative_to(HERE)) for path in required if not path.exists()]
    if missing:
        return {"stage": stage, "status": "INCOMPLETE", "missing": missing}
    rc = int(stem.with_suffix(".rc").read_text().strip())
    timing = parse_time(stem.with_suffix(".time"))
    if rc != 0:
        return {"stage": stage, "status": "FAILED", "rc": rc, "time": timing}
    data = json.loads(stem.with_suffix(".json").read_text())
    assert data["type"] == "EXACT-Q JOINT GLOBAL BAND / FALLACY-v2"
    assert data["branch"] == branch and data["stage_spec"]["stage"] == stage
    assert data["driver_sha256"] == PATCHED_SHA
    assert data["custody"]["all_hashes_match"] is True
    assert data["charged_endpoint"]["charged_driver_sha256"] == CONTROL[
        "original_engine_sha256"
    ]
    assert data["counts"]["inner_free_before_outer"] == EXPECTED_INNER[branch]
    assert data["precise_gauge_repair"]["new_free_dimensions"] == 1
    assert data["major"]["centre"]["minor_constant"] == "free"
    assert "jet0" in data["major"]["h3_free"]
    if branch == "delta52":
        assert data["major"]["centre"]["Hc_11_0"] == "fixed_zero_retained"
        assert "Hc_11_0" not in data["major"]["h3_free"]
    else:
        assert "Hc_11_0" in data["major"]["h3_free"]
    raw = data["raw_minor_support_control"]
    assert raw == {"delta2_F": 1134, "delta2_G": 513, "delta52_F": 1316, "delta52_G": 594}
    joint = data["joint_elimination"]
    localized = sp.Symbol("rho" if branch == "delta2" else "c")
    for pivot in joint["pivot_ledger"]:
        coefficient = sp.sympify(pivot["coefficient"])
        assert coefficient.is_Rational and coefficient != 0
        assert pivot["variable"] != str(localized)
    constants = []
    for row in joint["residual_rows"]:
        expression = sp.sympify(row["expression"])
        if expression.is_Rational and expression != 0:
            constants.append({
                "label": row["label"],
                "value": str(expression),
                "inverse": str(1 / expression),
                "identity": f"1=({1 / expression})*{row['label']}",
            })
    unit = joint["singular"]["unit_ideal"]
    point = data["necessary_chart_rational_point"]
    if point["status"] == "FOUND":
        localized_value = sp.Rational(point["localized_value"])
        jet0_value = sp.Rational(point["jet0_value"])
        wrapper_value = sp.Rational(point["localization_wrapper_value"])
        assert unit is False
        assert localized_value != 0 and localized_value * wrapper_value == 1
        assert point["jet0_nonzero"] is True and jet0_value != 0
        assert point["raw_rows_verified_zero"] == joint[
            "input_row_labels_excluding_preeliminated_major_rows"
        ]
        assert point["raw_rows_hash"] == joint["all_labeled_rows_hash"]
        assert point["gauge_ledger"]["minor_jet0_pin_released"] is True
        assert point["gauge_ledger"]["delta52_Hc_11_0_retained"] is (
            branch == "delta52"
        )
    if constants:
        assert unit is True
    if unit:
        assert data["verdict"] == "DEAD"
        assert joint["singular"]["dimension"] == -1
        assert joint["singular"]["basis_preview"] == ["1"]
    else:
        assert data["verdict"] == "COUNTING-BOUND"
    return {
        "stage": stage,
        "status": "COMPLETE",
        "verdict": data["verdict"],
        "unit_ideal": unit,
        "Qstar_pivots": joint["Qstar_pivots"],
        "residual_count": joint["residual_count"],
        "dimension": data["counts"]["exact_Krull_dimension_localized"],
        "linear_free_before_residue": data["counts"]["linear_free_before_residue"],
        "constant_unit_generators": constants,
        "necessary_chart_rational_point": point,
        "row_hash": joint["all_labeled_rows_hash"],
        "residual_hash": joint["residual_hash"],
        "json_sha256": hashlib.sha256(stem.with_suffix(".json").read_bytes()).hexdigest(),
        "singular_sha256": hashlib.sha256(stem.with_suffix(".sing").read_bytes()).hexdigest(),
        "stderr_bytes": stem.with_suffix(".err").stat().st_size,
        "time": timing,
    }


summary = {
    "schema": "g9966-precise-stage-summary-v1",
    "coefficient_field": "Q",
    "patched_engine_sha256": PATCHED_SHA,
    "pristine_control_status": CONTROL["status"],
    "branches": {},
}
for branch, stages in EXPECTED.items():
    requested = list(stages)
    records = [inspect(branch, stage) for stage in requested]
    complete = [record for record in records if record["status"] == "COMPLETE"]
    units = [record for record in complete if record["unit_ideal"]]
    all_complete = len(complete) == len(requested)
    terminal = records[-1]
    terminal_nonunit = bool(
        all_complete and not units and terminal["status"] == "COMPLETE"
        and not terminal["unit_ideal"]
    )
    terminal_point = (
        terminal["necessary_chart_rational_point"]
        if terminal["status"] == "COMPLETE" else None
    )
    load_bearing_ready = bool(
        terminal_nonunit and terminal_point is not None
        and terminal_point["status"] == "FOUND" and CONTROL["status"] == "PASS"
    )
    old_kill_stage = {"delta2": 4, "delta52": 8}[branch]
    re_certified_dead_ready = bool(
        units
        and units[0]["stage"] >= old_kill_stage
        and all(record["status"] == "COMPLETE" for record in records[:units[0]["stage"] + 1])
        and CONTROL["status"] == "PASS"
    )
    if re_certified_dead_ready:
        branch_verdict = "RE-CERTIFIED DEAD"
    elif load_bearing_ready:
        branch_verdict = "GAUGE PAYMENT WAS LOAD-BEARING"
    else:
        branch_verdict = "COMPUTE-BOUND"
    summary["branches"][branch] = {
        "stages": records,
        "first_unit_stage": units[0]["stage"] if units else None,
        "all_requested_complete": all_complete,
        "terminal_exact_nonunit": terminal_nonunit,
        "terminal_rational_point_status": terminal_point["status"] if terminal_point else None,
        "re_certified_dead_ready": re_certified_dead_ready,
        "load_bearing_ready": load_bearing_ready,
        "branch_verdict": branch_verdict,
    }
print(json.dumps(summary, indent=2, sort_keys=True))
