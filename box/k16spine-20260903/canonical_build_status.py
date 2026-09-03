#!/usr/bin/env python3
"""Build a compact, typed status record and checksum manifest.

This script intentionally distinguishes exact frozen-driver reconstruction,
exact tangent/Schur extraction, and finite-field terminal discovery.  It does
not promote a modular calculation to a characteristic-zero theorem.
"""

from __future__ import annotations

import glob
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def digest(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {
        "path": path.name,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def load(name: str) -> dict:
    return json.loads((ROOT / name).read_text())


def verify_charged_manifest() -> dict[str, object]:
    manifest = ROOT / "canonical_manifest.sha256"
    checks = []
    for line in manifest.read_text().splitlines():
        if not line.strip():
            continue
        expected, raw_path = line.split(None, 1)
        path = Path(raw_path.strip())
        actual = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
        checks.append(
            {
                "basename": path.name,
                "expected": expected,
                "actual": actual,
                "ok": actual == expected,
            }
        )
    return {
        "manifest": digest(manifest),
        "checked": len(checks),
        "all_ok": bool(checks) and all(item["ok"] for item in checks),
        "checks": checks,
    }


def post_hc_status() -> dict[str, object]:
    records: dict[str, object] = {}
    t2 = load("canonical_t2_audit.json")
    measured = t2["measured"]
    records["2"] = {
        "typing": t2["typing"],
        "rows": measured["post_rows"],
        "auxiliaries": measured["post_auxiliaries"],
        "expected_rows": 9 * 2 + 2,
        "expected_auxiliaries": 6 * 2 + 2,
        "pattern_checks_all_true": all(t2["pattern_checks"].values()),
        "vector_sha256": t2["post_Hc_vector_sha256"],
        "artifact": digest(ROOT / "canonical_t2_post_hc_rows.tsv"),
    }
    for t in range(3, 7):
        audit = load(f"canonical_t{t}_post_hc_audit.json")
        post = audit["post_Hc"]
        records[str(t)] = {
            "typing": audit["typing"],
            "rows": post["rows"],
            "auxiliaries": post["auxiliaries"],
            "expected_rows": 9 * t + 2,
            "expected_auxiliaries": 6 * t + 2,
            "tag_pattern_checked": post["tag_pattern_checked"],
            "vector_sha256": post["vector_sha256"],
            "artifact": audit["artifact"],
        }
    return records


def second_spine_status() -> dict[str, object]:
    table = load("canonical_pivots_schur_t2_t6.json")
    runs = {}
    for raw_t, run in sorted(table["runs"].items(), key=lambda item: int(item[0])):
        t = int(raw_t)
        runs[raw_t] = {
            "typing": run["status"],
            "pivot_count": run["pivot_count"],
            "expected_pivot_count": 5 * t + 2,
            "all_resultants_nonzero": run["all_resultants_nonzero"],
            "pivots": run["pivots"],
        }
    t2 = load("canonical_t2_audit.json")
    t3_path = ROOT / "terminal_t3_canonical_side-first_exact.json"
    t3 = json.loads(t3_path.read_text())
    nonlinear = {
        "2": {
            "typing": "EXACT_FULL_NONLINEAR_VALIDATED",
            "pivot_count": len(t2["pivots"]),
            "all_pivot_resultants_nonzero": t2["all_pivot_resultants_nonzero"],
            "all_inverse_checks": t2["all_pivot_inverse_checks"],
            "all_substitution_checks": t2["all_pivot_substitution_checks"],
            "terminal_rows": len(t2["terminal"]),
            "terminal_variables": t2["terminal_variables"],
            "artifact": digest(ROOT / "canonical_t2_audit.json"),
        },
        "3": {
            "typing": "EXACT_FULL_NONLINEAR_VALIDATED_SHARED_ARTIFACT",
            "pivot_count": t3["affine"]["pivot_count"],
            "zero_companion_rows": sum(
                row.get("status") == "zero" for row in t3["affine"]["dropped"]
            ),
            "terminal_rows": t3["terminal"]["row_count"],
            "terminal_variables": t3["terminal"]["variables"],
            "artifact": digest(t3_path),
        },
        "4": {
            "typing": "NOT_INDEPENDENTLY_REPLAYED_FULL_NONLINEAR_IN_THIS_LANE",
        },
        "5": {
            "typing": "NOT_FULL_NONLINEAR; EXACT_POST_HC_PLUS_EXACT_SCHUR_AND_MODULAR_TERMINAL_DISCOVERY",
        },
        "6": {
            "typing": "NOT_FULL_NONLINEAR; EXACT_POST_HC_PLUS_EXACT_SCHUR_AND_MODULAR_TERMINAL_DISCOVERY",
        },
    }
    return {
        "typing": table["typing"],
        "table_tsv": digest(ROOT / "canonical_pivots_schur_t2_t6.tsv"),
        "table_json": digest(ROOT / "canonical_pivots_schur_t2_t6.json"),
        "runs": runs,
        "full_nonlinear_validation": nonlinear,
        "t2_nonunit_deferral": {
            "scheduled_band": 3,
            "variable": "a4_0",
            "initial_u_primitive_Q_associate": "5*q5_1 - 1",
            "initial_resultant": "0",
            "policy": "not inverted; deferred deterministically",
            "accepted_after_valid_pivots": 6,
            "accepted_u_primitive_Q_associate": "39*q5_1 - 10",
            "accepted_resultant_H_raw_u": "-3696",
        },
    }


def modular_terminal_status() -> dict[str, object]:
    records: dict[str, object] = {}
    for t in (5, 6):
        paths = sorted(
            Path(path)
            for path in glob.glob(
                str(ROOT / f"canonical_terminal_mod_t{t}_p*_branch*.json")
            )
        )
        branches = []
        for path in paths:
            record = json.loads(path.read_text())
            top_base = ROOT / (
                f"terminal_mod_t{t}_p{record['prime']}_branch{record['branch']}"
            )
            top_output = top_base.with_suffix(".out")
            top_error = top_base.with_suffix(".err")
            top_resource = top_base.with_suffix(".resource")
            top_input = top_base.with_suffix(".sing")
            output_text = top_output.read_text() if top_output.is_file() else ""
            top_verdict = (
                "NONUNIT"
                if "\nNONUNIT\n" in output_text
                else "UNIT"
                if "\nUNIT\n" in output_text
                else "MISSING_OR_UNPARSED"
            )
            branches.append(
                {
                    "prime": record["prime"],
                    "branch": record["branch"],
                    "y": record["y"],
                    "H_split_y_values": record["H_split_y_values"],
                    "full_terminal_row_count": record["full_terminal_row_count"],
                    "terminal_bands": record["terminal_bands"],
                    "jobs": record["singular_jobs"],
                    "top_tail_job": {
                        "verdict": top_verdict,
                        "input": digest(top_input) if top_input.is_file() else None,
                        "output": digest(top_output) if top_output.is_file() else None,
                        "stderr": digest(top_error) if top_error.is_file() else None,
                        "stderr_empty": (
                            top_error.is_file() and top_error.stat().st_size == 0
                        ),
                        "resource": (
                            digest(top_resource) if top_resource.is_file() else None
                        ),
                    },
                    "artifact": digest(path),
                }
            )
        records[str(t)] = {
            "typing": "MEASURED-MODULAR DISCOVERY ONLY",
            "expected_branches": 2,
            "branches": branches,
            "all_four_full_chart_ideals_unit": (
                len(branches) == 2
                and all(
                    len(branch["jobs"]) == 2
                    and all(job["verdict"] == "UNIT" for job in branch["jobs"])
                    for branch in branches
                )
            ),
            "all_six_chart_and_top_tail_ideals_unit": (
                len(branches) == 2
                and all(
                    len(branch["jobs"]) == 2
                    and all(job["verdict"] == "UNIT" for job in branch["jobs"])
                    and branch["top_tail_job"]["verdict"] == "UNIT"
                    and branch["top_tail_job"]["stderr_empty"]
                    for branch in branches
                )
            ),
        }
    return records


def artifact_manifest() -> dict[str, object]:
    # The manifest cannot checksum itself, but it can and should checksum the
    # completed status record written immediately before this call.
    excluded = {"canonical_artifacts.sha256"}
    paths = sorted(
        path
        for path in ROOT.glob("canonical_*")
        if path.is_file() and path.name not in excluded
    )
    manifest_path = ROOT / "canonical_artifacts.sha256"
    text = "".join(
        f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.resolve()}\n"
        for path in paths
    )
    manifest_path.write_text(text)
    return {
        "path": manifest_path.name,
        "entries": len(paths),
        "sha256": hashlib.sha256(text.encode()).hexdigest(),
    }


def main() -> None:
    custody = verify_charged_manifest()
    if not custody["all_ok"]:
        raise SystemExit("charged-input custody verification failed")
    status = {
        "schema": "k16-canonical-extraction-status-v1",
        "scope": "fixed t=2..6 canonical extraction; no all-t theorem asserted",
        "charged_input_custody": custody,
        "canonical_order": load("canonical_t2_audit.json")["canonical_order"],
        "post_Hc_exact": post_hc_status(),
        "second_spine": second_spine_status(),
        "terminal_modular": modular_terminal_status(),
        "qualification": [
            "Finite-field UNIT verdicts are discovery evidence, not a characteristic-zero proof.",
            "Exact Schur pivots at t=4,5,6 are not labeled full nonlinear validations.",
            "No independent full nonlinear canonical t=4 replay completed in this lane.",
        ],
    }
    status_path = ROOT / "canonical_status.json"
    status_path.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n")
    manifest = artifact_manifest()
    print(json.dumps({"status": digest(status_path), "artifact_manifest": manifest}, sort_keys=True))


if __name__ == "__main__":
    main()
