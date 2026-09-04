#!/usr/bin/env python3
"""Build and verify the bounded authoritative K=8/K=9 artifact seal."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "box" / "k4rayk89-20260903"
SEAL = HERE / "authoritative-seal-sol56"
K8_RUN = HERE / "explicit-runs/k8-rho-3prime-exact"
GUIDED = HERE / "driver-audit-artifacts/sparse-rho-guided"
K9_BRANCH_SUMMARIES = {
    "A": GUIDED / "AUTHORITATIVE_K9A_FULL_3P_EXACTQ_V1/summary.json",
    "B": GUIDED / "AUTHORITATIVE_K9B_FULL_3P_EXACTQ_V1/summary.json",
}
K9_COMBINED = GUIDED / "AUTHORITATIVE_K9_CASE_A_COMPLETE_V1/summary.json"
GOOD_PRIMES = (32003, 32009, 32027)


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


def clean_guided_run(run: dict[str, Any]) -> bool:
    main = run["main"]
    return bool(
        run["returncode"] == 0
        and not run["timed_out"]
        and main["accepted"]
        and main["unit"]
        and main["basis_size"] == 1
        and main["dimension"] == -1
        and main["nf_all_zero"]
        and main["missing_markers"] == []
    )


def verify_guided_result(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if len(payload["certificate"]["runs"]) != 1:
        raise AssertionError(f"expected one guided run in {path}")
    run = payload["certificate"]["runs"][0]
    if not clean_guided_run(run):
        raise AssertionError(f"unclean guided unit in {path}")
    files = {}
    for key in ("script", "stdout", "stderr"):
        artifact = Path(run[key])
        declared = run[f"{key}_sha256"]
        actual = sha256(artifact)
        if actual != declared:
            raise AssertionError(f"{key} hash mismatch in {path}")
        files[key] = {"path": str(artifact), "sha256": actual}
    certificate = Path(run["script"]).with_suffix(".guided.json")
    if not certificate.is_file():
        raise AssertionError(f"missing per-run guided certificate {certificate}")
    return {
        "guided_result": str(path),
        "guided_result_sha256": sha256(path),
        "verdict": payload["verdict"],
        "characteristic": run["characteristic"],
        "elapsed_seconds": run["elapsed_seconds"],
        "basis_size": run["main"]["basis_size"],
        "dimension": run["main"]["dimension"],
        "nf_all_zero": run["main"]["nf_all_zero"],
        "files": files,
        "per_run_certificate": str(certificate),
        "per_run_certificate_sha256": sha256(certificate),
    }


def build_k8_summary(runner: Any) -> tuple[Path, dict[str, Any]]:
    source_summary_path = K8_RUN / "summary.json"
    source_summary = json.loads(source_summary_path.read_text(encoding="utf-8"))
    chart_path = K8_RUN / "emitted_Q/explicit-chart.json"
    chart, stages = runner.load_chart(chart_path)
    if source_summary["verdict"] != "UNIT_IDEAL_CHAR0":
        raise AssertionError("K8 source summary is not exact-Q unit")
    if chart["K"] != 8 or chart["branch"] != "single":
        raise AssertionError("unexpected K8 chart identity")
    if source_summary["chart_sha256"] != chart["chart_sha256"]:
        raise AssertionError("K8 source summary/chart fingerprint mismatch")
    if sum(len(stage["expressions"]) for stage in stages) != 61:
        raise AssertionError("unexpected K8 reduced row count")
    run_paths = [
        K8_RUN / f"modular/rho/p{prime}/guided_gb_result.json" for prime in GOOD_PRIMES
    ] + [K8_RUN / "exact/rho/guided_gb_result.json"]
    runs = [verify_guided_result(path) for path in run_paths]
    if [int(run["characteristic"]) for run in runs] != [*GOOD_PRIMES, 0]:
        raise AssertionError("K8 characteristic chain mismatch")
    manifest_path = Path(chart["band_manifest"])
    summary = {
        "type": "K4RAY-K8-D108-NOSPLIT-AUTHORITATIVE",
        "K": 8,
        "census_row": "D=108 no-split (24,16;18;7;4), b=6",
        "verdict": "UNIT_IDEAL_CHAR0",
        "decision": "DEAD",
        "promotion": "K=8 D=108 no-split DEAD; D=108 CLOSED at skeleton level",
        "notify_worthy": False,
        "scope": "terminal recurrence plus exact actual-rho positive-band necessary subsystem",
        "implication": "a unit necessary subsystem is empty, hence the full localized chart is empty",
        "chart": {
            "path": str(chart_path),
            "file_sha256": sha256(chart_path),
            "internal_chart_sha256": chart["chart_sha256"],
            "manifest": str(manifest_path),
            "manifest_sha256": sha256(manifest_path),
            "generator_union_checksum": chart["band_union_checksum"],
            "variable_count": len(chart["variables"]),
            "row_count": sum(len(stage["expressions"]) for stage in stages),
            "band_count": len(stages),
            "denominator_lcm": int(chart["denominator_lcm"]),
            "stage_row_counts": chart["stage_row_counts"],
            "formula_controls": chart["formula_controls"],
            "normalization": chart["normalization"],
        },
        "source_summary": str(source_summary_path),
        "source_summary_sha256": sha256(source_summary_path),
        "modular_chain": runs[:3],
        "exact_q": runs[3],
        "controls": {
            "all_runs_clean_unit": True,
            "all_script_stdout_stderr_hashes_recomputed": True,
            "staged_hash_row_union_checks_replayed": True,
            "modular_promotion_forbidden": True,
            "exact_q_confirmation_present": True,
        },
        "fallacy_v2": {
            "modular_unit": "F_p-only; the promotion uses the exact-Q unit",
            "posdim": "not invoked",
        },
    }
    output = SEAL / "k8-d108-closed-summary.json"
    atomic_write(output, json.dumps(summary, indent=2, sort_keys=True) + "\n")
    return output, summary


def files_from_k9_summary(path: Path) -> set[Path]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    selected = {path, Path(payload["workflow_summary"]), Path(payload["chart"]["path"]), Path(payload["chart"]["manifest"])}
    for run in [payload["probe"], *payload["modular_chain"], payload["exact_q"]]:
        selected.update(
            {
                Path(run["script"]),
                Path(run["stdout"]),
                Path(run["stderr"]),
                Path(run["guided_result"]),
                Path(run["script"]).with_suffix(".guided.json"),
            }
        )
    return selected


def relative(path: Path) -> str:
    return str(path.resolve().relative_to(ROOT.resolve()))


def verify_and_write_manifest(paths: Iterable[Path]) -> tuple[Path, Path]:
    unique = sorted({path.resolve() for path in paths}, key=lambda path: relative(path))
    for path in unique:
        if not path.is_file():
            raise AssertionError(f"authoritative artifact missing: {path}")
    index_payload = {
        "type": "K4RAY-K89-AUTHORITATIVE-ARTIFACT-INDEX",
        "artifact_count_excluding_index": len(unique),
        "artifacts": [
            {"path": relative(path), "sha256": sha256(path), "bytes": path.stat().st_size}
            for path in unique
        ],
    }
    index_path = SEAL / "authoritative-index.json"
    atomic_write(index_path, json.dumps(index_payload, indent=2, sort_keys=True) + "\n")
    unique.append(index_path.resolve())
    unique.sort(key=lambda path: relative(path))
    manifest_path = SEAL / "authoritative-artifacts.sha256"
    manifest_text = "".join(f"{sha256(path)}  {relative(path)}\n" for path in unique)
    atomic_write(manifest_path, manifest_text)
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        expected, name = line.split("  ", 1)
        if sha256(ROOT / name) != expected:
            raise AssertionError(f"post-write manifest verification failed: {name}")
    verification = {
        "type": "K4RAY-K89-AUTHORITATIVE-MANIFEST-VERIFICATION",
        "status": "PASS",
        "manifest": relative(manifest_path),
        "manifest_sha256": sha256(manifest_path),
        "checked_file_count": len(unique),
        "algorithm": "SHA-256",
        "verification": "every listed path was re-read and matched after manifest write",
    }
    verification_path = SEAL / "authoritative-manifest-verification.json"
    atomic_write(verification_path, json.dumps(verification, indent=2, sort_keys=True) + "\n")
    return manifest_path, verification_path


def write_diagnostic_inventory() -> Path:
    entries = [
        (HERE / "recurrence-runs-sol56/QREC_K8_SCREEN/INVALID_CONSTRUCTION.json", "INVALID_CONSTRUCTION", "uncleared finite-field row denominators; ignored and replaced by V2"),
        (HERE / "explicit-runs/k8-rho-p32003/summary.json", "OPEN_INVALID_EARLY_RUN", "early parser/construction run; superseded by k8-rho-3prime-exact"),
        (HERE / "recurrence-runs-sol56/QREC_K8_SCREEN_V2/K8_single/summary.json", "NECESSARY_POSDIM_ONLY", "18-variable recurrence screen; no counterexample inference"),
        (HERE / "explicit-runs/k9A-rho-3prime-exact/modular/rho/p32003/guided_gb_result.json", "TIMEOUT_RAW_51_VARIABLE", "raw unreduced K9 A rho chart timed out"),
        (GUIDED / "DRIVER_AUDIT_RAW_K9A_HBLOCK_P32003_V1/K9_A/probe-progress.json", "TIMEOUT_RAW_STAGED", "raw 51-variable staged diagnostic; workflow intentionally terminated"),
        (GUIDED / "DRIVER_AUDIT_K9A_ALPHA_PREFIX_V6/K9_A/probe-progress.json", "TIMEOUT_ALPHA_PREFIX", "terminal/alpha-only diagnostic; intentionally stopped after decisive full-chart screen"),
        (HERE / "explicit-runs/driver-audit-k9b-terminal-rref-v2/build/explicit-chart.json", "TERMINAL_ONLY", "necessary terminal checkpoint, not a row decision"),
        (HERE / "hensel_reduced_sol56.py", "DEVELOPMENTAL_TIMEOUT_PATH", "generic symbolic reducer was too slow and was not used for promotion"),
        (HERE / "quotient_recurrence_sol56.py", "DEVELOPMENTAL_SCREEN_DRIVER", "necessary-screen/RREF development driver, not authoritative proof output"),
    ]
    payload = {
        "type": "K4RAY-K89-NONAUTHORITATIVE-DIAGNOSTIC-INVENTORY",
        "excluded_from_authoritative_manifest": True,
        "entries": [
            {
                "path": relative(path) if path.exists() else str(path),
                "exists": path.is_file(),
                "sha256": sha256(path) if path.is_file() else None,
                "classification": classification,
                "reason": reason,
            }
            for path, classification, reason in entries
        ],
    }
    output = SEAL / "diagnostic-artifacts-inventory.json"
    atomic_write(output, json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return output


def main() -> None:
    runner = load_runner()
    k8_summary_path, _k8_summary = build_k8_summary(runner)
    combined = json.loads(K9_COMBINED.read_text(encoding="utf-8"))
    if combined["verdict"] != "UNIT_IDEAL_CHAR0" or not combined["notify_worthy"]:
        raise AssertionError("K9 combined promotion summary is not sealed")
    for branch, path in K9_BRANCH_SUMMARIES.items():
        payload = json.loads(path.read_text(encoding="utf-8"))
        if payload["internal_split"] != branch or payload["verdict"] != "UNIT_IDEAL_CHAR0":
            raise AssertionError(f"bad K9 internal split summary {branch}")

    authoritative: set[Path] = {
        k8_summary_path,
        K8_RUN / "summary.json",
        K8_RUN / "stage-progress.json",
        K8_RUN / "emitted_Q/explicit-chart.json",
        K8_RUN / "emitted_Q/bands-manifest.json",
        K8_RUN / "emitted_Q/bands-manifest.sha256",
        K9_COMBINED,
        GUIDED / "AUTHORITATIVE_K9A_FULL96_3P_EXACTQ_V1/summary.json",
        HERE / "controls-artifacts/controls-summary.json",
        HERE / "controls-artifacts/artifacts.sha256",
        HERE / "explicit_bands.py",
        HERE / "sparse_rho_topprobe.py",
        HERE / "sparse_rho_guided_runner_sol56.py",
        HERE / "consolidate_k9a_authoritative_sol56.py",
        HERE / "consolidate_k9_internal_splits_sol56.py",
        HERE / "seal_authoritative_artifacts_sol56.py",
        HERE / "controls-replay.py",
        HERE / "structure-note.md",
        ROOT / "box/lib/guided_gb.py",
        ROOT / "box/lib/staged_band_emitter.py",
    }
    for run_path in [
        *(K8_RUN / f"modular/rho/p{prime}/guided_gb_result.json" for prime in GOOD_PRIMES),
        K8_RUN / "exact/rho/guided_gb_result.json",
    ]:
        record = verify_guided_result(run_path)
        authoritative.add(run_path)
        authoritative.add(Path(record["per_run_certificate"]))
        for item in record["files"].values():
            authoritative.add(Path(item["path"]))
    for path in K9_BRANCH_SUMMARIES.values():
        authoritative.update(files_from_k9_summary(path))
    diagnostic_path = write_diagnostic_inventory()
    manifest_path, verification_path = verify_and_write_manifest(authoritative)
    print(
        json.dumps(
            {
                "k8_summary": relative(k8_summary_path),
                "k8_summary_sha256": sha256(k8_summary_path),
                "k9_combined": relative(K9_COMBINED),
                "k9_combined_sha256": sha256(K9_COMBINED),
                "manifest": relative(manifest_path),
                "manifest_sha256": sha256(manifest_path),
                "verification": relative(verification_path),
                "diagnostic_inventory": relative(diagnostic_path),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
