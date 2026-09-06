#!/usr/bin/env python3
"""Small mock-directory tests for summarize_worker.py."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import tempfile
import unittest

import summarize_worker as summary


MS_SHA = "a" * 64
SING_SHA = "b" * 64


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build_meta(
    path: Path, certificate: bool = False,
    face_subset_indices: list[int] | None = None,
) -> None:
    payload = {
        "schema": "T2T3_DIRECT_BUILD/v1",
        "status": "EMITTED_EXACT_Q_AND_MODULAR_NOT_RUN",
        "case": "99-delta2",
        "field": "Q",
        "modular_prime": 1073741827,
        "semantic_variable_count": 449,
        "solver_variable_count": 449,
        "graph_variables_emitted": 0,
        "constraint_variables_pivoted": 0,
        "raw_row_counts": {
            "T2_upper": 462, "T2_strict": 1263, "T2_face": 56,
            "T3_recurrence": 1, "T3_strict": 2539, "T3_face": 146,
            "inverse": 3,
        },
        "identically_zero_after_substitution": {
            "T2_face": 39, "T3_strict": 1577, "T3_face": 100,
        },
        "emitted_nonzero_counts": {
            "T2_upper": 462, "T2_strict": 1263, "T2_face": 17,
            "T3_recurrence": 1, "T3_strict": 962, "T3_face": 46,
            "inverse": 3,
        },
        "emitted_generator_count": 2754,
        "input_sha256": "1" * 64,
        "driver_sha256": "2" * 64,
        "semantic_variable_order_sha256": "4" * 64,
        "alias_order_sha256": "5" * 64,
        "raw_row_labels_sha256": "6" * 64,
        "emitted_row_labels_sha256": "7" * 64,
        "original_name_generator_text_sha256": "8" * 64,
        "labels_file_sha256": "9" * 64,
        "variable_map_sha256": "0" * 64,
        "no_Jacobian_variable_or_tail_rows": True,
        "primitive_integer_rows": True,
        "canonical_primitive_generator_sequence_sha256": "c" * 64,
        "singular_file": "99-delta2.sing",
        "singular_file_bytes": 234,
        "singular_file_sha256": SING_SHA,
        "msolve_file": "99-delta2.ms",
        "msolve_file_bytes": 123,
        "msolve_file_sha256": MS_SHA,
        "solver_variable_order_sha256": "d" * 64,
        "order": {
            "singular": "(M(two-site 446x446),dp(3))",
            "matrix_flat_sha256": "e" * 64,
            "site_r_sha256": "f" * 64,
            "site_z_sha256": "0" * 64,
        },
    }
    if certificate or face_subset_indices is not None:
        payload.update({
            "schema": "T2T3_DIRECT_T2_CERTIFICATE/v1",
            "classification_scope": (
                "literal full-direct-ideal generator subset; UNIT is conclusive for the full ideal, "
                "NONUNIT is inconclusive"
            ),
            "selected_blocks": ["source_residual", "T2_upper", "T2_face", "inverse"],
            "omitted_blocks": ["T2_strict", "T3_recurrence", "T3_strict", "T3_face"],
            "graph_variables_emitted": 0,
            "constraint_variables_pivoted": 0,
            "emitted_generator_count": 482,
            "raw_row_counts": {"T2_upper": 462, "T2_face": 56, "inverse": 3},
            "identically_zero_after_substitution": {"T2_face": 39},
            "emitted_nonzero_counts": {"T2_upper": 462, "T2_face": 17, "inverse": 3},
            "input_sha256": "1" * 64,
            "driver_sha256": "2" * 64,
            "shared_emitter_driver_sha256": "3" * 64,
            "semantic_variable_order_sha256": "4" * 64,
            "alias_order_sha256": "5" * 64,
            "raw_row_labels_sha256": "6" * 64,
            "emitted_row_labels_sha256": "7" * 64,
            "original_name_generator_text_sha256": "8" * 64,
            "labels_file_sha256": "9" * 64,
            "variable_map_sha256": "0" * 64,
        })
    if face_subset_indices is not None:
        face_count = len(face_subset_indices)
        payload.update({
            "schema": "T2T3_DIRECT_T2_FACE_SUBSET/v1",
            "selected_blocks": [
                "source_residual", "T2_upper", "T2_face_subset", "inverse",
            ],
            "selected_T2_face_indices": face_subset_indices,
            "complete_T2_face": False,
            "emitted_generator_count": 465 + face_count,
            "raw_row_counts": {
                "T2_upper": 462, "T2_face": face_count, "inverse": 3,
            },
            "identically_zero_after_substitution": {},
            "emitted_nonzero_counts": {
                "T2_upper": 462, "T2_face": face_count, "inverse": 3,
            },
        })
    path.write_text(json.dumps(payload, sort_keys=True) + "\n", encoding="utf-8")


def caprun(path: Path, status: str = "NORMAL_EXIT", rc: int = 0) -> None:
    payload = {
        "schema": "CAPRUN/v1",
        "status": status,
        "runner_exit_code": rc,
        "child_returncode": 0 if rc == 0 else -15,
        "child_signal": None if rc == 0 else 15,
        "runner_signal": None,
        "wall_elapsed_seconds": 12.5,
        "max_observed_group_rss_bytes": 987654321,
        "argv_sha256": "1" * 64,
        "stdout": {"bytes": 99, "sha256": "2" * 64, "path": "solver.stdout"},
        "stderr": {"bytes": 88, "sha256": "3" * 64, "path": "solver.stderr"},
        "termination": {
            "reason": None if rc == 0 else "wall_timeout",
            "cleanup_complete": None if rc == 0 else True,
        },
    }
    path.write_text(json.dumps(payload) + "\n", encoding="utf-8")


def run_custody(run: Path, mode: str, digest: str, input_name: str) -> None:
    input_path = f"/worker/presentations/{input_name}"
    if mode == "msolve":
        limit_lines = (
            "limit_kind=RLIMIT_AS",
            "limit_value=419430400",
            "limit_units=KiB",
        )
        write(run / "limit.txt", (
            "LIMIT_KIND=RLIMIT_AS LIMIT_KIB=419430400\n"
            "PROC_LIMIT=Max address space         429496729600"
            "         429496729600         bytes     \n"
        ))
    else:
        limit_lines = (
            "limit_kind=sampled_aggregate_PGID_RSS",
            "limit_value=214748364800",
            "limit_units=bytes",
        )
    write(run / "custody.txt", "\n".join((
        "schema=T2T3_WORKER_RUN/v1",
        f"mode={mode}",
        f"input={input_path}",
        f"input_sha256={digest}",
        "solver_sha256=" + "4" * 64,
        "wrapper_sha256=" + "5" * 64,
        "caprun_sha256=" + "6" * 64,
        *limit_lines,
    )) + "\n")
    write(run / "postflight.sha256", f"{digest}  {input_path}\n")
    write(run / "runner.rc", "0\n")
    write(run / "time.txt", (
        "\tElapsed (wall clock) time (h:mm:ss or m:ss): 0:12.50\n"
        "\tMaximum resident set size (kbytes): 123456\n"
    ))


def seal_solver_outputs(run: Path) -> None:
    cap = json.loads((run / "caprun.json").read_text())
    lines = []
    for name in ("solver.stdout", "solver.stderr"):
        path = run / name
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        cap[name.split(".")[1]] = {
            "bytes": path.stat().st_size, "sha256": digest, "path": str(path),
        }
        lines.append(f"{digest}  {path}\n")
    (run / "caprun.json").write_text(json.dumps(cap) + "\n", encoding="utf-8")
    for name in ("custody.txt", "caprun.json", "time.txt", "limit.txt"):
        path = run / name
        if not path.is_file():
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        lines.append(f"{digest}  {path}\n")
    with (run / "postflight.sha256").open("a", encoding="utf-8") as handle:
        handle.writelines(lines)


class SummarizeWorkerTests(unittest.TestCase):
    def test_certificate_schema_validation_rejects_scope_tamper(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            meta = Path(temporary) / "build.json"
            build_meta(meta, certificate=True)
            payload = json.loads(meta.read_text())
            self.assertTrue(summary.build_is_valid(payload))
            payload["omitted_blocks"].remove("T3_face")
            self.assertFalse(summary.build_is_valid(payload))

    def test_certificate_exact_unit_certifies_full_after_modular_signal(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            meta, mrun, srun, out = root / "build.json", root / "m", root / "s", root / "out.json"
            build_meta(meta, certificate=True)

            mrun.mkdir()
            caprun(mrun / "caprun.json")
            run_custody(mrun, "msolve", MS_SHA, "99-delta2.ms")
            write(mrun / "basis.ms", (
                "#Reduced Groebner basis data\n"
                "#field characteristic: 1073741827\n"
                "#length of basis: 1 element\n#---\n[1]:\n"
            ))
            basis_sha = hashlib.sha256((mrun / "basis.ms").read_bytes()).hexdigest()
            with (mrun / "postflight.sha256").open("a", encoding="utf-8") as handle:
                handle.write(f"{basis_sha}  {mrun / 'basis.ms'}\n")
            write(mrun / "solver.stdout", "")
            write(mrun / "solver.stderr", (
                "#equations 482\n"
                "#invalid equations 0\n"
                "msolve overall time 1.0 sec (elapsed) / 2.0 sec (cpu)\n"
            ))
            seal_solver_outputs(mrun)

            srun.mkdir()
            caprun(srun / "caprun.json")
            run_custody(srun, "singular", SING_SHA, "99-delta2.sing")
            write(srun / "solver.stdout", "\n".join((
                "ALL_ROWS_PARSED", "BEGIN_STD", "END_STD", "BEGIN_RESULT",
                "REDUCE_ONE=0", "DIMENSION=-1", "BASIS_SIZE=1", "END_RESULT",
            )) + "\n")
            write(srun / "solver.stderr", "")
            seal_solver_outputs(srun)

            summary.main([
                "--build-meta", str(meta), "--msolve-run", str(mrun),
                "--singular-run", str(srun), "--output", str(out),
            ])
            payload = json.loads(out.read_text())
            self.assertTrue(payload["build"]["valid"])
            self.assertEqual(payload["build"]["kind"], "T2_SUBSET_UNIT_CERTIFICATE")
            self.assertEqual(payload["msolve"]["verdict"], "MODULAR_UNIT_SIGNAL_ONLY")
            self.assertEqual(payload["singular"]["verdict"], "EXACT_Q_UNIT")
            self.assertEqual(
                payload["combined_verdict"],
                "EXACT_Q_T2_SUBSET_UNIT_CERTIFIES_FULL_DIRECT_IDEAL_AFTER_MODULAR_SIGNAL",
            )

    def test_certificate_exact_nonunit_is_inconclusive_for_full_ideal(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            meta, srun, out = root / "build.json", root / "s", root / "out.json"
            build_meta(meta, certificate=True)
            srun.mkdir()
            caprun(srun / "caprun.json")
            run_custody(srun, "singular", SING_SHA, "99-delta2.sing")
            write(srun / "solver.stdout", "\n".join((
                "ALL_ROWS_PARSED", "BEGIN_STD", "END_STD", "BEGIN_RESULT",
                "REDUCE_ONE=1", "DIMENSION=4", "BASIS_SIZE=23", "END_RESULT",
            )) + "\n")
            write(srun / "solver.stderr", "")
            seal_solver_outputs(srun)
            summary.main([
                "--build-meta", str(meta), "--singular-run", str(srun),
                "--output", str(out),
            ])
            payload = json.loads(out.read_text())
            self.assertTrue(payload["build"]["valid"])
            self.assertEqual(payload["singular"]["verdict"], "EXACT_Q_NONUNIT_BASIS")
            self.assertEqual(
                payload["combined_verdict"],
                "OPEN_T2_SUBSET_NONUNIT_INCONCLUSIVE_FOR_FULL_DIRECT_IDEAL",
            )
            self.assertTrue(
                payload["guardrails"]["certificate_nonunit_has_no_force_for_full_ideal"]
            )
            self.assertNotIn("SAMPLE_POINT", payload["combined_verdict"])

    def test_face_subset_schema_validation_rejects_index_and_ledger_tamper(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            meta = Path(temporary) / "build.json"
            build_meta(meta, face_subset_indices=[40, 41])
            original = json.loads(meta.read_text())
            self.assertTrue(summary.build_is_valid(original))
            downgraded = json.loads(json.dumps(original))
            downgraded["schema"] = "T2T3_DIRECT_BUILD/v1"
            self.assertFalse(summary.build_is_valid(downgraded))
            self.assertEqual(
                summary.combined_verdict(
                    {"verdict": "NOT_RUN"},
                    {"verdict": "EXACT_Q_NONUNIT_BASIS"}, downgraded,
                ),
                "OPEN_INVALID_BUILD_METADATA",
            )
            for key in (
                "classification_scope", "selected_blocks", "omitted_blocks",
                "selected_T2_face_indices", "complete_T2_face",
                "shared_emitter_driver_sha256",
            ):
                downgraded.pop(key, None)
            self.assertFalse(summary.build_is_valid(downgraded))
            self.assertEqual(
                summary.combined_verdict(
                    {"verdict": "MODULAR_NONUNIT_BASIS_SIGNAL"},
                    {"verdict": "NOT_RUN"}, original,
                ),
                "OPEN_T2_FACE_SUBSET_NONUNIT_INCONCLUSIVE_FOR_FULL_DIRECT_IDEAL",
            )
            self.assertEqual(
                summary.combined_verdict(
                    {"verdict": "MODULAR_UNIT_SIGNAL_ONLY"},
                    {"verdict": "NOT_RUN"}, original,
                ),
                "OPEN_MODULAR_T2_FACE_SUBSET_UNIT_SIGNAL_ONLY",
            )
            mutations = {
                "empty": lambda value: value.update(selected_T2_face_indices=[]),
                "duplicate": lambda value: value.update(selected_T2_face_indices=[40, 40]),
                "out_of_range": lambda value: value.update(selected_T2_face_indices=[40, 56]),
                "not_canonical_order": lambda value: value.update(selected_T2_face_indices=[41, 40]),
                "claims_complete": lambda value: value.update(complete_T2_face=True),
                "complete_index_set": lambda value: value.update(
                    selected_T2_face_indices=list(range(56)),
                    raw_row_counts={"T2_upper": 462, "T2_face": 56, "inverse": 3},
                    identically_zero_after_substitution={"T2_face": 39},
                    emitted_nonzero_counts={
                        "T2_upper": 462, "T2_face": 17, "inverse": 3,
                    },
                    emitted_generator_count=482,
                ),
                "wrong_selected_ledger": lambda value: value.update(
                    selected_blocks=["source_residual", "T2_upper", "T2_face", "inverse"]
                ),
                "incoherent_face_count": lambda value: value["raw_row_counts"].update(T2_face=1),
                "mandatory_upper_omitted": lambda value: value.update(
                    raw_row_counts={"T2_face": 2, "inverse": 3},
                    emitted_nonzero_counts={"T2_face": 2, "inverse": 3},
                    emitted_generator_count=5,
                ),
                "target_rows_falsely_zero": lambda value: value.update(
                    identically_zero_after_substitution={"T2_face": 2},
                    emitted_nonzero_counts={"T2_upper": 462, "inverse": 3},
                    emitted_generator_count=465,
                ),
                "more_nonzero_rows_than_full_face": lambda value: value.update(
                    selected_T2_face_indices=list(range(18)),
                    raw_row_counts={"T2_upper": 462, "T2_face": 18, "inverse": 3},
                    emitted_nonzero_counts={
                        "T2_upper": 462, "T2_face": 18, "inverse": 3,
                    },
                    identically_zero_after_substitution={},
                    emitted_generator_count=483,
                ),
                "wrong_case_variable_count": lambda value: value.update(
                    semantic_variable_count=448, solver_variable_count=448,
                ),
            }
            for label, mutate in mutations.items():
                with self.subTest(label=label):
                    payload = json.loads(json.dumps(original))
                    mutate(payload)
                    self.assertFalse(summary.build_is_valid(payload))

    def test_face_subset_exact_unit_certifies_full_direct_ideal(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            meta, srun, out = root / "build.json", root / "s", root / "out.json"
            build_meta(meta, face_subset_indices=[40, 41])
            srun.mkdir()
            caprun(srun / "caprun.json")
            run_custody(srun, "singular", SING_SHA, "99-delta2.sing")
            write(srun / "solver.stdout", "\n".join((
                "ALL_ROWS_PARSED", "BEGIN_STD", "END_STD", "BEGIN_RESULT",
                "REDUCE_ONE=0", "DIMENSION=-1", "BASIS_SIZE=1", "END_RESULT",
            )) + "\n")
            write(srun / "solver.stderr", "")
            seal_solver_outputs(srun)
            summary.main([
                "--build-meta", str(meta), "--singular-run", str(srun),
                "--output", str(out),
            ])
            payload = json.loads(out.read_text())
            self.assertTrue(payload["build"]["valid"])
            self.assertEqual(payload["build"]["kind"], "T2_FACE_SUBSET_UNIT_CERTIFICATE")
            self.assertEqual(payload["build"]["selected_T2_face_indices"], [40, 41])
            self.assertEqual(payload["singular"]["verdict"], "EXACT_Q_UNIT")
            self.assertEqual(
                payload["combined_verdict"],
                "EXACT_Q_T2_FACE_SUBSET_UNIT_CERTIFIES_FULL_DIRECT_IDEAL",
            )

    def test_face_subset_nonunit_stays_open_for_full_direct_ideal(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            meta, srun, out = root / "build.json", root / "s", root / "out.json"
            build_meta(meta, face_subset_indices=[40, 41])
            srun.mkdir()
            caprun(srun / "caprun.json")
            run_custody(srun, "singular", SING_SHA, "99-delta2.sing")
            write(srun / "solver.stdout", "\n".join((
                "ALL_ROWS_PARSED", "BEGIN_STD", "END_STD", "BEGIN_RESULT",
                "REDUCE_ONE=1", "DIMENSION=7", "BASIS_SIZE=31", "END_RESULT",
            )) + "\n")
            write(srun / "solver.stderr", "")
            seal_solver_outputs(srun)
            summary.main([
                "--build-meta", str(meta), "--singular-run", str(srun),
                "--output", str(out),
            ])
            payload = json.loads(out.read_text())
            self.assertEqual(payload["singular"]["verdict"], "EXACT_Q_NONUNIT_BASIS")
            self.assertEqual(
                payload["combined_verdict"],
                "OPEN_T2_FACE_SUBSET_NONUNIT_INCONCLUSIVE_FOR_FULL_DIRECT_IDEAL",
            )
            self.assertTrue(payload["combined_verdict"].startswith("OPEN_"))
            self.assertNotIn("SAMPLE_POINT", payload["combined_verdict"])

    def test_modular_unit_and_exact_unit_with_f4_partial(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            meta, mrun, srun, out = root / "build.json", root / "m", root / "s", root / "out.json"
            build_meta(meta)
            mrun.mkdir()
            caprun(mrun / "caprun.json")
            run_custody(mrun, "msolve", MS_SHA, "99-delta2.ms")
            write(mrun / "basis.ms", (
                "#Reduced Groebner basis data\n"
                "#field characteristic: 1073741827\n"
                "#length of basis:      1 element\n#---\n[1]:\n"
            ))
            basis_sha = hashlib.sha256((mrun / "basis.ms").read_bytes()).hexdigest()
            with (mrun / "postflight.sha256").open("a", encoding="utf-8") as handle:
                handle.write(f"{basis_sha}  {mrun / 'basis.ms'}\n")
            write(mrun / "solver.stderr", (
                "#equations                    2754\n"
                "#invalid equations               0\n"
                "deg sel pairs mat density new data time(rd)\n"
                "  2 10 20 30 x 40 12.30% 5 new 0 zero 1.20 | 2.30\n"
                "  3  7 15 100 x 200 4.00%\n"
                "reduce final basis 500 x 600 0.10% 7 new 0 zero----------------\n"
            ))
            write(mrun / "solver.stdout", "")
            seal_solver_outputs(mrun)

            srun.mkdir()
            caprun(srun / "caprun.json")
            run_custody(srun, "singular", SING_SHA, "99-delta2.sing")
            write(srun / "solver.stdout", "\n".join((
                "ALL_ROWS_PARSED", "BEGIN_STD", "END_STD", "BEGIN_RESULT",
                "REDUCE_ONE=0", "DIMENSION=-1", "BASIS_SIZE=1", "END_RESULT",
            )) + "\n")
            write(srun / "solver.stderr", "")
            seal_solver_outputs(srun)

            rc = summary.main([
                "--build-meta", str(meta), "--msolve-run", str(mrun),
                "--singular-run", str(srun), "--output", str(out),
            ])
            self.assertEqual(rc, 0)
            payload = json.loads(out.read_text())
            self.assertLessEqual(out.stat().st_size, summary.MAX_JSON_BYTES)
            self.assertEqual(payload["msolve"]["verdict"], "MODULAR_UNIT_SIGNAL_ONLY")
            self.assertEqual(payload["msolve"]["f4"]["max_selected_degree"], 3)
            self.assertEqual(payload["msolve"]["f4"]["max_completed_degree"], 2)
            self.assertEqual(payload["msolve"]["f4"]["largest_f4_round_matrix"]["rows"], 100)
            self.assertEqual(
                payload["msolve"]["f4"]["largest_completed_f4_round_matrix"]["rows"], 30
            )
            self.assertEqual(
                payload["msolve"]["f4"]["largest_matrix_including_final_reduction"]["kind"],
                "final_reduction",
            )
            self.assertEqual(payload["msolve"]["f4"]["reduce_final"]["stage"], "linalg")
            self.assertEqual(payload["msolve"]["f4"]["trailing_diagnostic_count"], 0)
            self.assertEqual(payload["msolve"]["f4"]["accepted_interleave_count"], 1)
            self.assertEqual(payload["msolve"]["time"]["elapsed"], "0:12.50")
            self.assertEqual(payload["singular"]["verdict"], "EXACT_Q_UNIT")
            self.assertEqual(
                payload["combined_verdict"],
                "EXACT_Q_UNIT_CONFIRMED_AFTER_MODULAR_SIGNAL",
            )
            self.assertTrue(payload["generator_custody"]["both_solver_inputs_match_build"])

    def test_exact_nonunit_is_typed_but_does_not_invent_point(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            meta, srun, out = root / "build.json", root / "s", root / "out.json"
            build_meta(meta)
            srun.mkdir()
            caprun(srun / "caprun.json")
            run_custody(srun, "singular", SING_SHA, "99-delta2.sing")
            write(srun / "solver.stdout", "\n".join((
                "ALL_ROWS_PARSED", "BEGIN_STD", "END_STD", "BEGIN_RESULT",
                "REDUCE_ONE=1", "DIMENSION=2", "BASIS_SIZE=17", "END_RESULT",
            )) + "\n")
            write(srun / "solver.stderr", "")
            seal_solver_outputs(srun)
            summary.main([
                "--build-meta", str(meta), "--singular-run", str(srun),
                "--output", str(out),
            ])
            payload = json.loads(out.read_text())
            self.assertEqual(payload["singular"]["verdict"], "EXACT_Q_NONUNIT_BASIS")
            self.assertEqual(
                payload["combined_verdict"],
                "EXACT_Q_NONUNIT_BASIS_REQUIRES_SAMPLE_POINT_REPORT",
            )
            self.assertTrue(payload["guardrails"]["nonunit_basis_is_not_a_sample_point"])

    def test_timeout_and_hash_mismatch_cannot_promote_unit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            meta, mrun, out = root / "build.json", root / "m", root / "out.json"
            build_meta(meta)
            mrun.mkdir()
            caprun(mrun / "caprun.json", status="WALL_TIMEOUT", rc=124)
            run_custody(mrun, "msolve", "9" * 64, "99-delta2.ms")
            write(mrun / "runner.rc", "124\n")
            write(mrun / "basis.ms", (
                "#Reduced Groebner basis data\n"
                "#field characteristic: 1073741827\n"
                "#length of basis: 1 element\n[1]:\n"
            ))
            write(mrun / "solver.stderr", "deg sel pairs mat density new data time(rd)\n 4 2 9\n")
            write(mrun / "solver.stdout", "")
            seal_solver_outputs(mrun)
            summary.main([
                "--build-meta", str(meta), "--msolve-run", str(mrun),
                "--output", str(out),
            ])
            payload = json.loads(out.read_text())
            self.assertEqual(payload["msolve"]["basis"]["classification"], "UNIT")
            self.assertEqual(payload["msolve"]["verdict"], "OPEN_INCOMPLETE_OR_CAPPED")
            self.assertEqual(payload["combined_verdict"], "OPEN")

    def test_garbage_reduce_one_and_singular_diagnostic_fail_closed(self) -> None:
        for reduce_one, extra, expected in (
            ("garbage", "", "OPEN_NO_VALID_RESULT_BLOCK"),
            ("0", "   ? simulated runtime error\n", "OPEN_SOLVER_DIAGNOSTIC"),
        ):
            with self.subTest(reduce_one=reduce_one, extra=extra):
                with tempfile.TemporaryDirectory() as temporary:
                    root = Path(temporary)
                    meta, srun, out = root / "build.json", root / "s", root / "out.json"
                    build_meta(meta)
                    srun.mkdir()
                    caprun(srun / "caprun.json")
                    run_custody(srun, "singular", SING_SHA, "99-delta2.sing")
                    dimension = "-1" if reduce_one == "0" else "2"
                    basis_size = "1" if reduce_one == "0" else "17"
                    write(srun / "solver.stdout", extra + "\n".join((
                        "ALL_ROWS_PARSED", "BEGIN_STD", "END_STD", "BEGIN_RESULT",
                        f"REDUCE_ONE={reduce_one}", f"DIMENSION={dimension}",
                        f"BASIS_SIZE={basis_size}", "END_RESULT",
                    )) + "\n")
                    write(srun / "solver.stderr", "")
                    seal_solver_outputs(srun)
                    summary.main([
                        "--build-meta", str(meta), "--singular-run", str(srun),
                        "--output", str(out),
                    ])
                    payload = json.loads(out.read_text())
                    self.assertEqual(payload["singular"]["verdict"], expected)

    def test_msolve_basis_requires_header_grammar_and_declared_count(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            malformed = root / "malformed.ms"
            write(malformed, (
                "#Reduced Groebner basis data\n"
                "#field characteristic: 1073741827\n"
                "#length of basis: 1 element\n"
                "[this is not a polynomial]:\n"
            ))
            parsed = summary.parse_msolve_basis(malformed, 449)
            self.assertEqual(parsed["classification"], "INCOMPLETE")
            self.assertFalse(parsed["grammar_valid"])

            wrong_count = root / "wrong-count.ms"
            write(wrong_count, (
                "#Reduced Groebner basis data\n"
                "#field characteristic: 1073741827\n"
                "#length of basis: 2 elements\n"
                "[1]:\n"
            ))
            parsed = summary.parse_msolve_basis(wrong_count, 449)
            self.assertEqual(parsed["classification"], "INCOMPLETE")
            self.assertFalse(parsed["declared_count_matches_body"])

    def test_normal_fglm_interleave_is_not_a_diagnostic(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            log = Path(temporary) / "solver.stdout"
            write(log, (
                "deg sel pairs mat density new data time(rd)\n"
                "11 322 322 1461 x 2681 49.70% 0 new 328 zero 0.15 | 0.27\n"
                "reduce final basis 617 x 2165 62.45% 613 new 0 zero"
                "Dimension of quotient: 1548\n"
            ))
            parsed = summary.parse_f4(log)
            self.assertEqual(parsed["trailing_diagnostic_count"], 0)
            self.assertEqual(parsed["accepted_interleave_count"], 1)
            self.assertEqual(parsed["reduce_final"]["rows"], 617)

    def test_duplicate_custody_and_changed_log_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            meta, mrun, out = root / "build.json", root / "m", root / "out.json"
            build_meta(meta)
            mrun.mkdir()
            caprun(mrun / "caprun.json")
            run_custody(mrun, "msolve", MS_SHA, "99-delta2.ms")
            with (mrun / "custody.txt").open("a", encoding="utf-8") as handle:
                handle.write(f"input_sha256={MS_SHA}\n")
            write(mrun / "basis.ms", (
                "#field characteristic: 1073741827\n"
                "#length of basis: 1 element\n[1]:\n"
            ))
            basis_sha = hashlib.sha256((mrun / "basis.ms").read_bytes()).hexdigest()
            with (mrun / "postflight.sha256").open("a", encoding="utf-8") as handle:
                handle.write(f"{basis_sha}  {mrun / 'basis.ms'}\n")
            write(mrun / "solver.stderr", (
                "#equations 2754\n"
                "#invalid equations 0\n"
                "deg sel pairs mat density new data time(rd)\n"
                "2 1 1 2 x 2 50.00% 1 new 0 zero 0.1 | 0.1\n"
            ))
            write(mrun / "solver.stdout", "")
            seal_solver_outputs(mrun)
            with (mrun / "solver.stderr").open("a", encoding="utf-8") as handle:
                handle.write("postflight mutation\n")
            summary.main([
                "--build-meta", str(meta), "--msolve-run", str(mrun),
                "--output", str(out),
            ])
            payload = json.loads(out.read_text())
            self.assertIn(
                payload["msolve"]["verdict"],
                {"OPEN_CUSTODY_PARSE_ERRORS", "OPEN_RUN_ARTIFACT_CUSTODY_MISMATCH"},
            )


if __name__ == "__main__":
    unittest.main()
