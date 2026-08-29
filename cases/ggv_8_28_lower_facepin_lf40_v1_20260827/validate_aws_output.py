#!/usr/bin/env python3
"""Fail-closed validator for the sequential exact-Q LF40 producer run."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys

from lf40_common import fail, write_json


EXPECTED_COUNTS = [0, 35, 34, 33, 32, 32, 31, 30, 29, 29, 28, 27, 26, 26,
                   25, 24, 23, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13,
                   12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def main() -> int:
    if len(sys.argv) != 5:
        fail("usage: validate_aws_output.py COMPILER_RESULT SOLVER_STDOUT SOLVER_RC OUTPUT_JSON")
    compiler = json.loads(Path(sys.argv[1]).read_text())
    stdout_path = Path(sys.argv[2])
    solver_rc = int(sys.argv[3])
    output_path = Path(sys.argv[4])
    text = stdout_path.read_text(encoding="utf-8", errors="replace") if stdout_path.is_file() else ""

    for key, expected in (
        ("status", "PASS-LF40-COMPILER-CUSTODY"),
        ("compute_variables", 408),
        ("target_generators", 740),
        ("raw_coefficient_generators", 774),
    ):
        if compiler.get(key) != expected:
            fail(("compiler custody mismatch", key, compiler.get(key), expected))
    if compiler.get("rabinowitsch") != {
        "variables": 409,
        "equations": 741,
        "equation": "w*a*b*rho*f_0_8*g_0_12-1",
    }:
        fail("Rabinowitsch custody mismatch")

    base = {
        "schema": "GGV-8_28-LF40-sequential-exact-AWS-result-v1",
        "solver_rc": solver_rc,
        "field": "QQ exact",
        "representation": "substituted 408/740 plus one Rabinowitsch variable/equation = 409/741",
        "producer_result_not_promoted_evidence": True,
    }
    if solver_rc in (124, 137, 143):
        base.update({"status": "RESOURCE_CAP_NO_VERDICT", "completed_rows": []})
        write_json(output_path, base)
        print(base["status"])
        return 0
    if solver_rc != 0:
        base.update({"status": "DEPENDENCY_SOURCE_REPLAY_OR_ENGINE_FAILURE", "reason": "nonzero solver rc"})
        write_json(output_path, base)
        print(base["status"])
        return 90
    required_headers = (
        "LF40_FIELD=QQ_EXACT",
        "LF40_VARIABLES=409",
        "LF40_TARGET_GENERATORS=740",
        "LF40_RABINOWITSCH_EQUATIONS=1",
        "LF40_SYNTHETIC_CONTROLS=PASS",
    )
    missing = [marker for marker in required_headers if marker not in text]
    if missing or "LF40_FATAL_" in text or "?" in text:
        base.update({"status": "DEPENDENCY_SOURCE_REPLAY_OR_ENGINE_FAILURE",
                     "reason": {"missing_headers": missing, "fatal_or_question_marker": True}})
        write_json(output_path, base)
        print(base["status"])
        return 90

    completed = [int(value) for value in re.findall(r"LF40_STAGE_ROW_(\d+)_END", text)]
    inconsistency = [int(value) for value in re.findall(r"LF40_FIRST_EXACT_INCONSISTENCY_ROW=(\d+)", text)]
    full = "LF40_FULL_PROPER_IDEAL_FIXTURE_ROWS_0_THROUGH_40" in text
    if len(inconsistency) > 1 or (inconsistency and full):
        fail(("contradictory terminal markers", inconsistency, full))
    if inconsistency:
        row = inconsistency[0]
        if completed != list(range(row + 1)):
            fail(("did not stop at first sequential unit stage", completed, row))
        expected_cumulative = sum(EXPECTED_COUNTS[:row + 1])
        listed = re.findall(r"LF40_LISTED_EQUATIONS_AT_STOP=(\d+)", text)
        if listed != [str(expected_cumulative + 1)]:
            fail(("listed-equation stop count", listed, expected_cumulative + 1))
        base.update({
            "status": "FIRST_EXACT_INCONSISTENCY_PRODUCER_UNREVIEWED",
            "first_inconsistent_row": row,
            "last_proper_prefix_row": row - 1,
            "completed_rows": completed,
            "target_generators_at_stop": expected_cumulative,
            "listed_equations_at_stop": expected_cumulative + 1,
            "meaning": "conditional actual-GGV lower FACEPIN exclusion only after independent review",
        })
    elif full:
        if completed != list(range(41)):
            fail(("full marker without all rows", completed))
        listed = re.findall(r"LF40_LISTED_EQUATIONS_AT_STOP=(\d+)", text)
        if listed != ["741"]:
            fail(("full listed equation count", listed))
        base.update({
            "status": "FULL_PROPER_IDEAL_FIXTURE_PRODUCER_UNREVIEWED",
            "completed_rows": completed,
            "target_generators_at_stop": 740,
            "listed_equations_at_stop": 741,
            "meaning": "full lower necessary-system survivor, not a chain point or counterexample",
        })
    else:
        base.update({"status": "DEPENDENCY_SOURCE_REPLAY_OR_ENGINE_FAILURE",
                     "reason": "no licensed terminal marker", "completed_rows": completed})
        write_json(output_path, base)
        print(base["status"])
        return 90
    write_json(output_path, base)
    print(base["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

