#!/usr/bin/env python3
"""Synthetic acceptance/refusal tests for summarize_results.py."""

from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest


MODULE_PATH = Path(__file__).resolve().parents[1] / "summarize_results.py"
SPEC = importlib.util.spec_from_file_location("gi_summarize_results", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
SUMMARY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SUMMARY)


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def artifact(path: Path) -> dict[str, object]:
    return SUMMARY.file_artifact(path)


class SummaryFixture:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.manifest = []
        counts = (70, 109, 127, 171, 341, 455)
        for class_id, unknowns in zip(SUMMARY.EXPECTED_CLASS_IDS, counts, strict=True):
            self.manifest.append(
                {
                    "class_id": class_id,
                    "canonical_stem": f"{class_id}_G",
                    "unknowns_without_T": unknowns,
                    "unknowns_with_T": unknowns + 1,
                    "jacobian_coefficient_generator_count": 2,
                    "generator_count_including_inverse": 3,
                }
            )
        write_json(root / "classes_manifest.json", self.manifest)
        source_root = MODULE_PATH.parent
        for name in ("solve_class.py", "gi_only_emit.py", "time_singular.sh", "fleet_lane.sh"):
            shutil.copyfile(source_root / name, root / name)
        self.receipt = {
            "status": "PASS",
            "all_blockwise_subset": True,
            "all_specializations": True,
            "all_orientation_checks": True,
            "all_native_zero_specializations": True,
            "all_production_sign_isomorphisms": True,
            "all_production_coordinate_only_specializations": True,
            "results": [],
        }
        for class_id in SUMMARY.EXPECTED_CLASS_IDS:
            class_result = self.class_verification(class_id)
            self.receipt["results"].append(class_result)
            job = root / "classes" / class_id / "jobs" / f"{class_id}_G_fleet.sh"
            job.parent.mkdir(parents=True, exist_ok=True)
            job.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
        write_json(root / "verification.json", self.receipt)
        self.sparse_extractor = root / "sparse_hadic_extract.py"
        self.sparse_extractor.write_text("# synthetic exact sparse extractor\n", encoding="utf-8")
        self.sparse_receipt = root / "sparse-extraction-custody.json"
        sparse_classes = []
        self.sparse_candidate_receipts: dict[str, Path] = {}
        for class_id in SUMMARY.SPARSE_EXTRACTION_CLASSES:
            class_dir = root / "classes" / class_id
            rows = class_dir / "rows" / f"{class_id}_G_rows.tsv"
            builder = class_dir / "builders" / f"{class_id}_G_builder.sing"
            rows.parent.mkdir(parents=True, exist_ok=True)
            builder.parent.mkdir(parents=True, exist_ok=True)
            rows.write_text(
                "source_index|h_power|x_power|y_power|expr\n0|0|0|0|c\n1|0|1|0|c-1\n",
                encoding="utf-8",
            )
            builder.write_text("ring R=0,(y,x,c),dp;\n", encoding="utf-8")
            candidate_receipt = root / "sparse-candidates" / class_id / "extraction.json"
            write_json(
                candidate_receipt,
                {
                    "schema": "moh-gi-only-sparse-hadic-extraction-experiment-v1",
                    "status": "PASS",
                    "class_id": class_id,
                    "coefficient_generators": 2,
                    "rows_sha256": SUMMARY.sha256_file(rows),
                    "elapsed_seconds": 0.25,
                    "peak_rss_kib": 2048,
                },
            )
            self.sparse_candidate_receipts[class_id] = candidate_receipt
            sparse_classes.append(
                {
                    "class_id": class_id,
                    "stem": f"{class_id}_G",
                    "status": "PASS",
                    "candidate_receipt": artifact(candidate_receipt),
                    "candidate_rows": artifact(rows),
                    "canonical_builder": artifact(builder),
                    "coefficient_generators": 2,
                    "generators_including_Tc_minus_1": 3,
                    "all_G_coordinates_retained": True,
                    "coordinate_specializations": 0,
                    "auxiliary_variables": 0,
                    "literal_orientation": "J(P,Q)-c*x^ell",
                    "inverse_generator": "T*c-1",
                    "activation": {"action": "ATOMIC_INSTALL", "canonical_rows": artifact(rows)},
                }
            )
        write_json(
            self.sparse_receipt,
            {
                "schema": "moh-gi-only-sparse-extraction-activation-custody-v1",
                "status": "PASS",
                "sparse_extractor": artifact(self.sparse_extractor),
                "frozen_builder_fix": artifact(Path(SUMMARY.__file__).resolve().parents[1] / "moh14-charts-20260905" / "builder_fix.py"),
                "all_native_exact_controls_passed": True,
                "classes": sparse_classes,
            },
        )
        for index, item in enumerate(self.manifest):
            verdict = "DEAD" if index == 0 else "BASIS_FOUND" if index == 1 else "COMPUTE_BOUND"
            self.write_result(item, verdict)

    @staticmethod
    def class_verification(class_id: str) -> dict[str, object]:
        return {
            "class_id": class_id,
            "canonical_stem": f"{class_id}_G",
            "status": "PASS",
            "blockwise_subset_verified": True,
            "specialization_verified": True,
            "orientation_verified": True,
            "production_sign_isomorphism_verified": True,
            "production_coordinate_only_specialization_verified": True,
        }

    def write_result(self, manifest: dict[str, object], verdict: str) -> Path:
        class_id = str(manifest["class_id"])
        class_dir = self.root / "classes" / class_id
        solve_dir = class_dir / "solve"
        solve_dir.mkdir(parents=True, exist_ok=True)
        rows = class_dir / "rows" / f"{class_id}_G_rows.tsv"
        guided = class_dir / "jobs" / f"{class_id}_G_Q_guided.sing"
        stdout = solve_dir / f"{class_id}_G_Q.stdout"
        stderr = solve_dir / f"{class_id}_G_Q.stderr"
        meta = class_dir / "meta" / f"{class_id}_G.json"
        builder = class_dir / "builders" / f"{class_id}_G_builder.sing"
        complete = verdict in {"DEAD", "BASIS_FOUND"}
        unit = verdict == "DEAD"
        rows.parent.mkdir(parents=True, exist_ok=True)
        builder.parent.mkdir(parents=True, exist_ok=True)
        builder.write_text("ring R=0,(y,x,c),dp;\n", encoding="utf-8")
        rows.write_text(
            "source_index|h_power|x_power|y_power|expr\n0|0|0|0|c\n1|0|1|0|c-1\n",
            encoding="utf-8",
        )
        meta_value: dict[str, object] = {
            "class_id": class_id,
            "gi_only": True,
            "parameter_count": manifest["unknowns_without_T"],
            "jacobian_coefficient_generator_count": 2,
            "generator_count_including_inverse": 3,
        }
        if class_id in SUMMARY.SPARSE_EXTRACTION_CLASSES:
            meta_value["coefficient_rows_extraction_custody"] = {
                "method": "exact_sparse_monic_y_division",
                "status": "PASS",
                "custody_receipt": artifact(self.sparse_receipt),
                "sparse_extractor": artifact(self.sparse_extractor),
                "canonical_rows": artifact(rows),
                "canonical_builder_sha256": SUMMARY.sha256_file(builder),
                "literal_J_PQ_controls_passed": True,
                "native_literal_row_controls_passed": True,
                "no_coordinate_specialization": True,
                "no_auxiliary_variables": True,
            }
        write_json(meta, meta_value)
        guided.write_text("ring R=0,(c,T),dp;\nideal I=c,T*c-1;\n", encoding="utf-8")
        stdout_lines = [
            "CONTROL_RING_PASS R",
            "CONTROL_EMPTY_PASS",
            "CONTROL_NONEMPTY_PASS",
            "GG__GENERATOR_COUNT main 3",
        ]
        if complete:
            stdout_lines.append("GG__STD_SECONDS main 1")
            stdout_lines.extend(f"GG__NF_ZERO main {index} 1" for index in range(3))
            stdout_lines.extend(
                [
                    "GG__NF_ALL_ZERO main 1",
                    f"GG__UNIT main {int(unit)}",
                    "GG__BASIS_SIZE main 1",
                    f"GG__DIM main {-1 if unit else 0}",
                    "GG__VDIM main NONTERMINATING",
                    f"GG__LEAD_DIM main {-1 if unit else 0}",
                    "GG__LEAD_VDIM main NONTERMINATING",
                    "GG__ACCEPT main 1",
                    "GG__SCRIPT_DONE main 1",
                ]
            )
        stdout.write_text("\n".join(stdout_lines) + "\n", encoding="utf-8")
        stderr.write_text("synthetic GNU time output\n", encoding="utf-8")
        controls = {
            "complete": complete,
            "expected_generators_including_Tc_minus_1": 3,
            "guided_generator_counts": [3],
            "guided_main": {
                "accepted": complete,
                "basis_size": 1 if complete else None,
                "dimension": -1 if unit else 0 if complete else None,
                "lead_dim": -1 if unit else 0 if complete else None,
                "lead_vdim": None,
                "missing_markers": [] if complete else [
                    "NF_ALL_ZERO",
                    "UNIT",
                    "DIM",
                    "BASIS_SIZE",
                    "LEAD_DIM",
                    "ACCEPT",
                    "NF_ZERO",
                ],
                "nf_all_zero": complete,
                "unit": unit,
                "vdim": None,
                "vdim_matches_predicted": None,
            },
            "named": {
                name: {"pass_count": 1, "fail_count": 0}
                for name in ("ring", "empty", "nonempty")
            },
            "named_controls_pass": True,
            "nf_generator_rows": 3 if complete else 0,
            "script_done_count": 1 if complete else 0,
            "singular_error_lines": [],
            "std_seconds_markers": [1] if complete else [],
        }
        run = {
            "watchdog_seconds": 600,
            "timed_out": not complete,
            "returncode": 0 if complete else -15,
            "elapsed_seconds": 1.25 if complete else 600.01,
            "gnu_time_elapsed": "0:01.25" if complete else None,
            "peak_rss_kib": 4096,
            "peak_rss_source": "gnu_time" if complete else "sampled_process_group_100ms",
            "stdout": artifact(stdout),
            "stderr": artifact(stderr),
        }
        rows_artifact = artifact(rows)
        rows_artifact["header"] = "source_index|h_power|x_power|y_power|expr"
        result: dict[str, object] = {
            "schema": "moh-gi-only-exact-q-solve-v1",
            "state": "FINISHED",
            "class_id": class_id,
            "canonical_stem": f"{class_id}_G",
            "class_uniform_chart": True,
            "one_chart_per_class_suffices": True,
            "promotion_scope": "EXACT_Q_ONLY",
            "modular_policy": "SCREEN_ONLY_NEVER_PROMOTED",
            "unknowns_without_T": manifest["unknowns_without_T"],
            "solver_variables_with_T": manifest["unknowns_with_T"],
            "coefficient_generators": 2,
            "ideal_generators_including_Tc_minus_1": 3,
            "verdict": verdict,
            "verdict_detail": "synthetic",
            "report_label": {
                "DEAD": "DEAD — EXACT-Q UNIT ON THE FULL G_i CHART",
                "BASIS_FOUND": "BASIS FOUND — NONEMPTY EXACT-Q SAMPLE POINT VERIFIED (LOUD)",
                "COMPUTE_BOUND": "COMPUTE-BOUND — NO EXACT-Q UNIT OR VERIFIED SAMPLE POINT",
            }[verdict],
            "exact_q": {"run": run, "controls": controls},
            "rows": rows_artifact,
            "guided_script": artifact(guided),
            "meta_postemit": artifact(meta),
            "inputs": {"builder": artifact(builder)},
            "software": {
                "guided_gb": artifact(Path(SUMMARY.__file__).resolve().parents[1] / "lib" / "guided_gb.py"),
                "singular": {
                    "path": "/usr/bin/Singular",
                    "sha256": SUMMARY.sha256_file(Path("/usr/bin/Singular")),
                    "version_head": ["synthetic test uses installed binary hash"],
                },
            },
            "verification": {
                "receipt": artifact(self.root / "verification.json"),
                "class_result": self.class_verification(class_id),
            },
            "modular_screen": {
                "schema": "moh-gi-only-modular-screen-v1",
                "label": "MODULAR SCREEN ONLY — NEVER A CHARACTERISTIC-ZERO KILL",
                "promotion_allowed": False,
                "state": "FINISHED",
                "screen_signal": "MODULAR_INCONCLUSIVE_SCREEN",
                "characteristic": 1073741827,
                "public_effect": "none",
                "run": {
                    "watchdog_seconds": 600,
                    "timed_out": True,
                    "returncode": -15,
                    "elapsed_seconds": 600.01,
                    "gnu_time_elapsed": None,
                    "peak_rss_kib": 8192,
                    "peak_rss_source": "sampled_process_group_100ms",
                },
            },
        }
        if verdict == "BASIS_FOUND":
            sample_dir = solve_dir / "sample" / "point-0-synthetic"
            sample_dir.mkdir(parents=True, exist_ok=True)
            sample_stdout = sample_dir / "sample-point-check.stdout"
            sample_stderr = sample_dir / "sample-point-check.stderr"
            sample_script = sample_dir / "sample-point-check.sing"
            sample_stdout.write_text(
                "".join(f"GI__POINT_NF_ZERO {index} 1\n" for index in range(3))
                + "GI__POINT_ALL_ZERO 1\nGI__POINT_C_NONZERO 1\n",
                encoding="utf-8",
            )
            sample_stderr.write_text("", encoding="utf-8")
            sample_script.write_text("ring R=0,(c,T),dp;\n", encoding="utf-8")
            coordinates = {
                **{f"p_{index}": "0" for index in range(int(manifest["unknowns_without_T"]) - 1)},
                "c": "1",
                "T": "1",
            }
            result["dimension"] = 0
            result["sample_point"] = {
                "verified": True,
                "selected": {
                    "verified": True,
                    "kind": "exact_rational_full_assignment",
                    "coordinates": coordinates,
                    "residual_count": 3,
                    "expected_residual_count_including_Tc_minus_1": 3,
                    "script": artifact(sample_script),
                    "run": {
                        "watchdog_seconds": 60,
                        "timed_out": False,
                        "returncode": 0,
                        "elapsed_seconds": 0.01,
                        "peak_rss_kib": 1024,
                        "stdout": artifact(sample_stdout),
                        "stderr": artifact(sample_stderr),
                    },
                },
            }
        path = solve_dir / "solve-result.json"
        write_json(path, result)
        return path


class SummarizeResultsTest(unittest.TestCase):
    def test_accepts_six_and_rejects_verdict_tamper(self) -> None:
        with tempfile.TemporaryDirectory(prefix="gi-summary-test-") as temporary:
            root = Path(temporary)
            fixture = SummaryFixture(root)
            output = root / "final-solve-summary.json"
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                self.assertEqual(SUMMARY.main(["--bundle-root", str(root), "--output", str(output)]), 0)
            summary = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(summary["status"], "PASS")
            self.assertEqual(summary["verdict_counts"], {"DEAD": 1, "BASIS_FOUND": 1, "COMPUTE_BOUND": 4})

            first = fixture.manifest[0]
            path = root / "classes" / str(first["class_id"]) / "solve" / "solve-result.json"
            final_result = json.loads(path.read_text(encoding="utf-8"))
            worker_id = "i-0889ee47ceb889561"
            final_result["host"] = {"hostname": SUMMARY.LANE_WORKERS[worker_id]}
            write_json(path, final_result)
            campaign = root / "fleet" / worker_id / str(first["class_id"])
            final_snapshot = campaign / "class" / "solve" / "solve-result.json"
            final_snapshot.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, final_snapshot)
            shutil.copyfile(path, campaign / f"{first['class_id']}_G.dispatch.log")
            attempt2 = campaign / "attempt2" / "class" / "solve" / "solve-result.json"
            attempt2.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, attempt2)
            shutil.copyfile(path, campaign / "attempt2" / f"{first['class_id']}_G.dispatch.log")
            attempt1 = campaign / "attempt1" / "class" / "solve" / "solve-result.json"
            write_json(
                attempt1,
                {
                    "schema": "moh-gi-only-exact-q-solve-v1",
                    "state": "FINISHED",
                    "class_id": first["class_id"],
                    "canonical_stem": f"{first['class_id']}_G",
                    "verdict": "COMPUTE_BOUND",
                    "verdict_detail": "synthetic superseded extraction attempt",
                },
            )
            summary_with_retry = SUMMARY.aggregate(root)
            self.assertEqual(len(summary_with_retry["classes"][0]["superseded_attempts"]), 2)

            tampered = json.loads(path.read_text(encoding="utf-8"))
            tampered["verdict"] = "COMPUTE_BOUND"
            write_json(path, tampered)
            with self.assertRaisesRegex(SUMMARY.SummaryError, "mirror differs"):
                SUMMARY.aggregate(root)


if __name__ == "__main__":
    unittest.main()
