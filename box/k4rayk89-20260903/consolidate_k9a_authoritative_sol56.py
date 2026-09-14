#!/usr/bin/env python3
"""Verify and consolidate the authoritative K=9 branch-A kill artifacts."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "box" / "k4rayk89-20260903"
GUIDED_ROOT = HERE / "driver-audit-artifacts" / "sparse-rho-guided"
CHART = (
    HERE
    / "topprobe-artifacts"
    / "sparse-rho"
    / "K9A_SPARSE_RHO_V6"
    / "K9_A"
    / "build"
    / "sparse-rho-chart.json"
)
RUN_FILES = (
    GUIDED_ROOT / "ROOT_K9A_FULL96_P32003_V1" / "guided_gb_result.json",
    GUIDED_ROOT / "ROOT_K9A_FULL96_OTHERPRIMES_V1" / "guided_gb_result.json",
    GUIDED_ROOT / "ROOT_K9A_FULL96_EXACTQ_V1" / "guided_gb_result.json",
)
OUTPUT = GUIDED_ROOT / "AUTHORITATIVE_K9A_FULL96_3P_EXACTQ_V1" / "summary.json"


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
    main = run["main"]
    return bool(
        run["returncode"] == 0
        and not run["timed_out"]
        and main["accepted"]
        and main["unit"]
        and main["dimension"] == -1
        and main["basis_size"] == 1
        and main["nf_all_zero"]
        and main["missing_markers"] == []
    )


def verified_run(run: dict[str, Any], source: Path) -> dict[str, Any]:
    script = Path(run["script"])
    stdout = Path(run["stdout"])
    stderr = Path(run["stderr"])
    checks = {
        "clean_unit": clean_unit(run),
        "script_hash_matches": sha256(script) == run["script_sha256"],
        "stdout_hash_matches": sha256(stdout) == run["stdout_sha256"],
        "stderr_hash_matches": sha256(stderr) == run["stderr_sha256"],
    }
    if not all(checks.values()):
        raise AssertionError(f"run controls failed for {run['label']}: {checks}")
    return {
        "source_result": str(source),
        "source_result_sha256": sha256(source),
        "label": run["label"],
        "characteristic": run["characteristic"],
        "elapsed_seconds": run["elapsed_seconds"],
        "returncode": run["returncode"],
        "timed_out": run["timed_out"],
        "basis_size": run["main"]["basis_size"],
        "dimension": run["main"]["dimension"],
        "unit": run["main"]["unit"],
        "nf_all_zero": run["main"]["nf_all_zero"],
        "accepted": run["main"]["accepted"],
        "missing_markers": run["main"]["missing_markers"],
        "script": str(script),
        "script_sha256": run["script_sha256"],
        "stdout": str(stdout),
        "stdout_sha256": run["stdout_sha256"],
        "stderr": str(stderr),
        "stderr_sha256": run["stderr_sha256"],
        "verification": checks,
    }


def main() -> None:
    runner = load_runner()
    chart, stages = runner.load_chart(CHART)
    chart_file_sha = sha256(CHART)
    manifest_path = Path(chart["band_manifest"])
    manifest_sha = sha256(manifest_path)
    if chart_file_sha != "2f660fdaba37f3199b8bda06084c1d74cb20abfde1ef805c3ae6108988e7760b":
        raise AssertionError("unexpected authoritative chart file hash")
    if manifest_sha != "b13367ee9a25d1760d9b0393adfa0fcc81865f72201c34ba991eef5385b48179":
        raise AssertionError("unexpected authoritative staged manifest hash")
    if chart["chart_sha256"] != "8f8288777cbba48957861ae6a0cfd20a608e284798839dfda9fc922a86b35e29":
        raise AssertionError("unexpected internal chart fingerprint")
    if chart["band_union_checksum"] != "36d1faba5441c338b7abc8082b89eaebf6aa68218c4bc127bb9b9f643821c058":
        raise AssertionError("unexpected generator-union checksum")
    if len(chart["variables"]) != 36 or sum(len(stage["expressions"]) for stage in stages) != 96:
        raise AssertionError("unexpected chart size")
    if any(int(chart["denominator_lcm"]) % prime == 0 for prime in (32003, 32009, 32027)):
        raise AssertionError("selected prime divides the chart denominator lcm")

    result_payloads = [json.loads(path.read_text(encoding="utf-8")) for path in RUN_FILES]
    if [payload["verdict"] for payload in result_payloads] != [
        "MODULAR_ONLY",
        "MODULAR_ONLY",
        "UNIT_IDEAL_CHAR0",
    ]:
        raise AssertionError("unexpected source verdict chain")
    runs: list[dict[str, Any]] = []
    for source, payload in zip(RUN_FILES, result_payloads):
        runs.extend(verified_run(run, source) for run in payload["certificate"]["runs"])
    by_characteristic = {int(run["characteristic"]): run for run in runs}
    if set(by_characteristic) != {0, 32003, 32009, 32027}:
        raise AssertionError("authoritative characteristic set is incomplete")

    payload = {
        "type": "K4RAY-K9A-AUTHORITATIVE-3PRIME-EXACTQ",
        "K": 9,
        "branch": "A",
        "scope": chart["scope"],
        "verdict": "UNIT_IDEAL_CHAR0",
        "promotion": "internal y-factor split chart A DEAD; no census-row promotion without internal split B",
        "notify_worthy": False,
        "chart": {
            "path": str(CHART),
            "file_sha256": chart_file_sha,
            "internal_chart_sha256": chart["chart_sha256"],
            "manifest": str(manifest_path),
            "manifest_sha256": manifest_sha,
            "generator_union_checksum": chart["band_union_checksum"],
            "variables": len(chart["variables"]),
            "rows": sum(len(stage["expressions"]) for stage in stages),
            "bands": len(stages),
            "denominator_lcm": int(chart["denominator_lcm"]),
            "row_family_counts": chart["row_family_counts"],
            "terminal_rref_audit": chart["terminal_rref_audit"],
            "alpha_rref_audit": chart["alpha_rref_audit"],
            "residual_band_audit": chart["residual_band_audit"],
            "formula_controls": chart["formula_controls"],
            "split_coverage": chart["split_coverage"],
        },
        "modular_chain": [by_characteristic[p] for p in (32003, 32009, 32027)],
        "exact_q": by_characteristic[0],
        "controls": {
            "all_four_runs_clean_unit": all(run["verification"]["clean_unit"] for run in runs),
            "all_declared_file_hashes_recomputed": all(
                all(run["verification"].values()) for run in runs
            ),
            "staged_union_and_rows_reverified_by_runner": True,
            "inhomogeneous_localization": "mu*mu_inv-1",
            "modular_promotion_forbidden": True,
            "char0_basis_reduced_one_to_zero": True,
        },
        "fallacy_v2": {
            "modular_unit": "reported as F_p-only until the clean exact-Q unit",
            "posdim": "not used as a counterexample claim",
        },
    }
    atomic_write(OUTPUT, json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(OUTPUT), "sha256": sha256(OUTPUT), "verdict": payload["verdict"]}))


if __name__ == "__main__":
    main()
