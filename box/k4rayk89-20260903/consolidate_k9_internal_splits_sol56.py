#!/usr/bin/env python3
"""Verify both internal K=9 split kills and emit the census-row promotion."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "box" / "k4rayk89-20260903"
GUIDED = HERE / "driver-audit-artifacts" / "sparse-rho-guided"
GOOD_PRIMES = (32003, 32009, 32027)
SOURCES = {
    "A": {
        "chart": HERE / "topprobe-artifacts/sparse-rho/K9A_SPARSE_RHO_V6/K9_A/build/sparse-rho-chart.json",
        "summary": GUIDED / "DRIVER_AUDIT_K9A_FULL96_3P_EXACTQ_V1/K9_A/summary.json",
        "expected_file_sha256": "2f660fdaba37f3199b8bda06084c1d74cb20abfde1ef805c3ae6108988e7760b",
        "expected_internal_sha256": "8f8288777cbba48957861ae6a0cfd20a608e284798839dfda9fc922a86b35e29",
        "expected_union": "36d1faba5441c338b7abc8082b89eaebf6aa68218c4bc127bb9b9f643821c058",
        "expected_rows": 96,
    },
    "B": {
        "chart": HERE / "topprobe-artifacts/sparse-rho/K9B_SPARSE_RHO_V6/K9_B/build/sparse-rho-chart.json",
        "summary": GUIDED / "DRIVER_AUDIT_K9B_FULL98_3P_EXACTQ_V1/K9_B/summary.json",
        "expected_file_sha256": "4312d20c5c7f986dd7ce81321d4afe12e49b6ff3da4dbeab702eb98b29b499b2",
        "expected_internal_sha256": "b9ba580e7f81991a9dae0e08efe17271a68e884535b45e97c1bd9d96b236c1ff",
        "expected_union": "75ee6f378fe22d1fe2ff8760724435f5af632a34e0ce83a172d18311fcfa5951",
        "expected_rows": 98,
    },
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def load_runner() -> Any:
    path = HERE / "sparse_rho_guided_runner_sol56.py"
    spec = importlib.util.spec_from_file_location("sparse_rho_guided_runner_sol56", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load sparse runner")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def clean_unit(run: dict[str, Any]) -> bool:
    return bool(
        run["returncode"] == 0
        and not run["timed_out"]
        and run["unit"]
        and run["basis_size"] == 1
        and run["dimension"] == -1
        and run["nf_all_zero"]
        and run["accepted"]
        and run["missing_markers"] == []
    )


def verify_run_files(run: dict[str, Any]) -> dict[str, Any]:
    script = Path(run["script"])
    stdout = Path(run["stdout"])
    if sha256(script) != run["script_sha256"] or sha256(stdout) != run["stdout_sha256"]:
        raise AssertionError(f"script/stdout hash mismatch for {run['label']}")
    result_path = script.parent / "guided_gb_result.json"
    result_payload = json.loads(result_path.read_text(encoding="utf-8"))
    matching = [item for item in result_payload["certificate"]["runs"] if item["label"] == run["label"]]
    if len(matching) != 1:
        raise AssertionError(f"guided result does not contain unique run {run['label']}")
    source = matching[0]
    stderr = Path(source["stderr"])
    if sha256(stderr) != source["stderr_sha256"]:
        raise AssertionError(f"stderr hash mismatch for {run['label']}")
    if not clean_unit(run):
        raise AssertionError(f"run is not a clean unit: {run['label']}")
    return {
        **run,
        "guided_result": str(result_path),
        "guided_result_sha256": sha256(result_path),
        "stderr": str(stderr),
        "stderr_sha256": source["stderr_sha256"],
        "hashes_recomputed": True,
    }


def verify_branch(branch: str, source: dict[str, Any], runner: Any) -> dict[str, Any]:
    chart_path = Path(source["chart"])
    summary_path = Path(source["summary"])
    chart, stages = runner.load_chart(chart_path)
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    if sha256(chart_path) != source["expected_file_sha256"]:
        raise AssertionError(f"K9{branch} chart file hash mismatch")
    if chart["chart_sha256"] != source["expected_internal_sha256"]:
        raise AssertionError(f"K9{branch} internal chart hash mismatch")
    if chart["band_union_checksum"] != source["expected_union"]:
        raise AssertionError(f"K9{branch} generator union mismatch")
    row_count = sum(len(stage["expressions"]) for stage in stages)
    if row_count != source["expected_rows"] or len(chart["variables"]) != 36:
        raise AssertionError(f"K9{branch} chart size mismatch")
    if chart["split_coverage"]["this_chart"] != branch:
        raise AssertionError(f"K9{branch} split label mismatch")
    if chart["split_coverage"]["union"] != "exhaustive because y is prime; intersection retained in both":
        raise AssertionError("internal split coverage statement changed")
    if summary["verdict"] != "UNIT_IDEAL_CHAR0" or summary["start_index"] != len(stages) - 1:
        raise AssertionError(f"K9{branch} workflow did not decide the full reduced prefix")
    if summary["chart_sha256"] != chart["chart_sha256"]:
        raise AssertionError(f"K9{branch} workflow/chart fingerprint mismatch")
    probe = verify_run_files(summary["progress"][-1]["runs"][0])
    modular = [verify_run_files(run) for run in summary["confirmation"]["runs"]]
    exact = verify_run_files(summary["exact"]["runs"][0])
    if [int(run["characteristic"]) for run in modular] != list(GOOD_PRIMES):
        raise AssertionError(f"K9{branch} modular confirmation prime order mismatch")
    if exact["characteristic"] != 0:
        raise AssertionError(f"K9{branch} exact replay is not over Q")
    if any(int(chart["denominator_lcm"]) % prime == 0 for prime in GOOD_PRIMES):
        raise AssertionError(f"K9{branch} selected a bad modular prime")
    manifest_path = Path(chart["band_manifest"])
    branch_payload = {
        "type": "K4RAY-K9-INTERNAL-SPLIT-AUTHORITATIVE",
        "K": 9,
        "internal_split": branch,
        "verdict": "UNIT_IDEAL_CHAR0",
        "promotion": f"internal y-factor split chart {branch} DEAD",
        "notify_worthy": False,
        "chart": {
            "path": str(chart_path),
            "file_sha256": sha256(chart_path),
            "internal_chart_sha256": chart["chart_sha256"],
            "manifest": str(manifest_path),
            "manifest_sha256": sha256(manifest_path),
            "generator_union_checksum": chart["band_union_checksum"],
            "variable_count": len(chart["variables"]),
            "row_count": row_count,
            "band_count": len(stages),
            "denominator_lcm": int(chart["denominator_lcm"]),
            "terminal_rref_audit": chart["terminal_rref_audit"],
            "alpha_rref_audit": chart["alpha_rref_audit"],
            "residual_band_audit": chart["residual_band_audit"],
            "formula_controls": chart["formula_controls"],
            "split_coverage": chart["split_coverage"],
        },
        "workflow_summary": str(summary_path),
        "workflow_summary_sha256": sha256(summary_path),
        "probe": probe,
        "modular_chain": modular,
        "exact_q": exact,
        "controls": {
            "all_runs_clean_unit": all(clean_unit(run) for run in [probe, *modular, exact]),
            "all_script_stdout_stderr_hashes_recomputed": True,
            "staged_hash_row_union_checks_replayed": True,
            "good_primes_checked_against_denominator_lcm": True,
            "modular_promotion_forbidden": True,
            "exact_q_confirmation_present": True,
        },
        "fallacy_v2": {
            "modular_unit": "F_p-only; promotion rests on the exact-Q unit",
            "posdim": "no POSDIM-to-counterexample inference",
        },
    }
    output = GUIDED / f"AUTHORITATIVE_K9{branch}_FULL_3P_EXACTQ_V1" / "summary.json"
    atomic_write(output, json.dumps(branch_payload, indent=2, sort_keys=True) + "\n")
    return {"path": str(output), "sha256": sha256(output), "payload": branch_payload}


def main() -> None:
    runner = load_runner()
    branches = {branch: verify_branch(branch, source, runner) for branch, source in SOURCES.items()}
    combined = {
        "type": "K4RAY-K9-CENSUS-CASE-A-INTERNAL-SPLITS-COMPLETE",
        "K": 9,
        "census_row": "(99,66) case (A): (27,18;21;8;4), b=7",
        "verdict": "UNIT_IDEAL_CHAR0",
        "decision": "DEAD",
        "promotion": "K=9 census case (A) DEAD; (99,66) SKELETON verdict COMPLETE for all three configurations modulo N1",
        "notify_worthy": True,
        "internal_split_cover": {
            "reason": "y is prime, so y divides v*((y-x)*v^2-12*mu*p2) iff internal split A or B holds; their intersection is retained",
            "A": {"summary": branches["A"]["path"], "sha256": branches["A"]["sha256"], "verdict": "UNIT_IDEAL_CHAR0"},
            "B": {"summary": branches["B"]["path"], "sha256": branches["B"]["sha256"], "verdict": "UNIT_IDEAL_CHAR0"},
        },
        "implication_chain": [
            "any full K=9 census-case-(A) point satisfies the pinned recurrence and actual positive rho-band identities",
            "the recurrence forces internal y-factor split A or internal y-factor split B",
            "terminal constant-matrix RREF and alpha-band RREF are equivalences in the mu*mu_inv-1 localization",
            "each internal reduced necessary ideal is the unit ideal over Q",
            "therefore the original localized census row is empty",
        ],
        "fallacy_v2": {
            "modular_runs": "supporting F_p screens only",
            "promotion_basis": "clean exact-Q UNIT_IDEAL for both exhaustive internal splits",
            "posdim": "not invoked",
        },
    }
    output = GUIDED / "AUTHORITATIVE_K9_CASE_A_COMPLETE_V1" / "summary.json"
    atomic_write(output, json.dumps(combined, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "A_summary": branches["A"]["path"],
                "A_sha256": branches["A"]["sha256"],
                "B_summary": branches["B"]["path"],
                "B_sha256": branches["B"]["sha256"],
                "combined": str(output),
                "combined_sha256": sha256(output),
                "verdict": "UNIT_IDEAL_CHAR0",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
