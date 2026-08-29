#!/usr/bin/env python3
"""Fail-closed independent classifier for the closed-successor recursion (R3).

R3 additions over the reviewed R2 classifier (hostile review O-N1/O-N2/O-N6):
the runner-log bytes of every stage are bound (stdout must be exactly the
three SINGULAR_STAGE_* lines consistent with the verified result record,
stderr must be empty); the stage identity record's key set is censused
exactly; and the node standard-basis census is exact (each completed
header-writing stage appends one identical single-line write() block), which
also makes the single-stage EXACT_EMPTY_NODE census non-vacuous.

R2 contract, per the hostile-review C2 repair:

  1. Every dynamic Singular stage script (reduce, every rank size, saturation,
     chart, witness replay) is regenerated from the hash-pinned frozen r5
     builders plus this packet's repaired-template builders and byte-compared
     against the script that actually ran.  A fabricated or copied script of
     any kind refuses.
  2. Every stage must carry a result record and an identity record bound to
     exactly this job: job tag, schema-checked nonce, lease hash, source
     archive hash, exact Singular binary hash, worker/supervisor PIDs and
     start times, PGID/SID, cgroup equality, caps and argv.  The result record
     hashes the identity record.  Missing or copied identities refuse.
  3. Every production directory is closed under an exact expected artifact
     set derived from the stage progression; unexplained extra files refuse.
     Artifacts of a timed-out final stage are the only optional files, and
     only within that stage's statically known write set.
  4. Bounded no-verdicts are re-derived from the exact stage evidence (which
     stage timed out, where the reverse search exhausted, how many nodes
     completed) and the driver's recorded reason and remainder must equal the
     re-derivation; an allowlisted string alone proves nothing.

The classifier restates every expected marker and census and requires exact
agreement with the driver's SUMMARY.json before anything is published.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys


FROZEN_R5_SHA256 = "d679a4d7fb4bf2619fbb3ff47ea6f386ba1c75fdc477276cabf3bec8a2b2cd90"
TRANSCRIPT_GATE_SHA256 = (
    "0e0efd5ada59039a373a731038f2f88a3794b376b208879c2459bff97d0e7316")
DELTA_NODE1_SHA256 = (
    "84b4c2c4c0bfe5aa7414c35813cc1cf63d7d5416358a394b8e8bdc35820f1d02")
NODE2_GENERATOR_SHA256 = (
    "2b9d29b706ce5d7e58e2dc5a28799782f5610c5ccb7b71987ebd694fd8b83206",
    "fecd1d43f3f55e1c65bec858303b7688c0db83dbe9c3a60f51f70130a4149336",
    DELTA_NODE1_SHA256,
)
CLASS_DEAD = "EXACT_ENDPOINT_DEAD_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR_FINITE_COVER"
CLASS_SURVIVOR = ("RING_LEVEL_ENDPOINT_SURVIVOR_ON_TRIPLE02_NODE1_"
                  "CLOSED_SUCCESSOR_CHART_PENDING_NILPOTENCE_RADICAL")
CLASS_NO_VERDICT = "NO_VERDICT_OPEN_REMAINDER_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR"
CLASS_REVERSE = ("REVERSE_CONTAINMENT_SEARCH_EXHAUSTED_NO_VERDICT_ON_"
                 "TRIPLE02_NODE1_CLOSED_SUCCESSOR")
ALLOWED = {CLASS_DEAD, CLASS_SURVIVOR, CLASS_NO_VERDICT, CLASS_REVERSE}
NONCE_RE = re.compile(r"^[a-z0-9]{8,32}$")
START_NODE = 2
MAX_NODES = 6
FINAL_NODE = START_NODE + MAX_NODES - 1
WITNESS_REPLAY_MARKERS = (
    "NODE_INDEX=1",
    "NODE_GENERATOR_COUNT=2",
    "NODE_EMPTY=0",
    "NODE_REDUCER_FIXTURES_PASS=1",
    "NF_RATIONAL_UNIT_PIVOT_COUNT=95",
    "NF_PIVOT_INVARIANT_FAILURES=0",
    "NODE_RESIDUAL_REDUCTION_COMPLETE=1",
    "WITNESS_MINOR_ROWS=1,2,4,7,9,11",
    "WITNESS_MINOR_COLS=1,2,3,5,6,7",
    "WITNESS_DELTA_NF_NONZERO=1",
    "WITNESS_DELTA_EQUALS_ARCHIVED=1",
    "WITNESS_DELTA_NF_STABLE=1",
    "CLOSED_SUCCESSOR_GENERATOR_COUNT=3",
    "CLOSED_SUCCESSOR_CONTAINS_DELTA=1",
    "NODE1_OPEN_SATURATION_ENTERED=0",
    "NODE1_PURE_DELTA_POWER_SEARCH_ENTERED=0",
    "NODE1_PROPER_OPEN_CHART_ENTERED=0",
    "SETTLED_OPEN_ROUTE_NOT_REENTERED=1",
    "WITNESS_REPLAY_COMPLETE=1",
)
STAGE_RESULT_KEYS = (
    "argv", "cap_seconds", "elapsed_seconds", "expected_pgid", "expected_sid",
    "identity_sha256", "job_nonce", "job_tag", "lease_sha256", "returncode",
    "script_sha256", "singular_sha256", "source_archive_sha256", "stage_label",
    "stderr_sha256", "stdout_sha256", "supervisor_starttime", "timed_out",
    "worker_starttime",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def load_pinned(name: str, path: Path, expected_sha: str,
                with_parent_path: bool = False):
    if sha256(path) != expected_sha:
        raise SystemExit(f"PINNED_MODULE_SHA_DRIFT:{name}")
    if with_parent_path:
        sys.path.insert(0, str(path.parent))
    try:
        spec = importlib.util.spec_from_file_location(name, path)
        if spec is None or spec.loader is None:
            raise SystemExit(f"PINNED_MODULE_IMPORT_FAILURE:{name}")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        if with_parent_path:
            sys.path.pop(0)


def load_case_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"CASE_MODULE_IMPORT_FAILURE:{name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Binding:
    """The one-job binding every stage record must carry."""

    def __init__(self, job_tag: str, job_nonce: str,
                 source_archive_sha256: str, singular_sha256: str,
                 singular_path: str, lease: Path, worker_identity: Path,
                 supervisor_identity: Path, fast_cap: int, slow_cap: int):
        if not NONCE_RE.fullmatch(job_nonce):
            raise RuntimeError("CLASSIFIER_JOB_NONCE_SCHEMA")
        if not job_tag.endswith("_" + job_nonce):
            raise RuntimeError("CLASSIFIER_JOB_TAG_NONCE_DISAGREEMENT")
        for digest in (source_archive_sha256, singular_sha256):
            if not re.fullmatch(r"[0-9a-f]{64}", digest):
                raise RuntimeError("CLASSIFIER_BINDING_DIGEST_SCHEMA")
        self.job_tag = job_tag
        self.job_nonce = job_nonce
        self.source_archive_sha256 = source_archive_sha256
        self.singular_sha256 = singular_sha256
        # The stage runner records the resolved binary path; resolve the
        # caller-supplied path the same way (a nonexistent fixture path
        # resolves to itself).
        self.singular_path = str(Path(singular_path).resolve())
        self.lease_sha256 = sha256(lease)
        self.worker = json.loads(worker_identity.read_text())
        self.supervisor = json.loads(supervisor_identity.read_text())
        for record, keys in ((self.worker, ("pid", "pgid", "sid", "starttime")),
                             (self.supervisor, ("pid", "starttime"))):
            if any(not isinstance(record.get(key), int) for key in keys):
                raise RuntimeError("CLASSIFIER_IDENTITY_FILE_SCHEMA")
        self.fast_cap = fast_cap
        self.slow_cap = slow_cap

    def job_binding_block(self) -> dict[str, object]:
        return {
            "job_nonce": self.job_nonce,
            "job_tag": self.job_tag,
            "lease_sha256": self.lease_sha256,
            "singular_sha256": self.singular_sha256,
            "source_archive_sha256": self.source_archive_sha256,
            "supervisor": {"pid": self.supervisor["pid"],
                           "starttime": self.supervisor["starttime"]},
            "worker": {"pid": self.worker["pid"],
                       "starttime": self.worker["starttime"]},
        }


class Ledger:
    """Exact expected-artifact accounting for one production directory."""

    def __init__(self, directory: Path):
        self.directory = directory
        self.required: set[str] = set()
        self.optional: set[str] = set()

    def require(self, *names: str) -> None:
        for name in names:
            self.required.add(name)

    def allow_partial(self, *names: str) -> None:
        for name in names:
            if name not in self.required:
                self.optional.add(name)

    def close(self) -> None:
        actual = {entry.name for entry in self.directory.iterdir()}
        missing = sorted(self.required - actual)
        extra = sorted(actual - self.required - self.optional)
        if missing or extra:
            raise RuntimeError(
                f"ARTIFACT_SET_DRIFT:{self.directory.name}:missing="
                f"{missing}:extra={extra}")


def runner_files(label: str) -> tuple[str, ...]:
    return (f"{label}.stdout.txt", f"{label}.stderr.txt",
            f"{label}.result.json", f"{label}.identity.json",
            f"{label}.runner.stdout.txt", f"{label}.runner.stderr.txt")


def stage_singular_writes(node: int, label: str,
                          rank_bound: int) -> tuple[str, ...]:
    """Statically known Singular write set of one stage script."""
    prefix = f"NODE_{node:03d}"
    sb = f"{prefix}_STANDARD_BASIS.txt"
    if label == "reduce":
        return (sb, f"{prefix}_REDUCE_PIVOTS.tsv",
                f"{prefix}_REDUCE_RESIDUAL.tsv")
    if label.startswith("rank_size_"):
        size = int(label.rsplit("_", 1)[1])
        return (sb, f"{prefix}_SIZE_{size}_MINORS.tsv",
                f"{prefix}_SIZE_{size}_WITNESS.tsv")
    if label == "saturation":
        return (sb, f"{prefix}_OPEN_SAT_STANDARD_BASIS.txt",
                f"{prefix}_REVERSE_CONTAINMENT_ATTEMPTS.tsv",
                f"{prefix}_REVERSE_CONTAINMENT_WITNESSES.tsv",
                f"{prefix}_EMPTY_OPEN_POWER_CERTIFICATE.txt",
                f"{prefix}_NEXT_STANDARD_BASIS.txt")
    if label == "chart":
        return (sb, f"{prefix}_CHART_ACTIVE_STANDARD_BASIS.txt",
                f"{prefix}_CHART_PIVOTS.tsv", f"{prefix}_CHART_RESIDUAL.tsv",
                f"{prefix}_CHART_BASE_CHANGED_RESIDUAL.tsv",
                f"{prefix}_BASE_CHANGED_RIGHT_TRANSFORM.tsv",
                f"{prefix}_CHART_DELTA.txt",
                f"{prefix}_BORDERED_IDENTITIES.tsv",
                f"{prefix}_BORDERED_NONZERO_PLANT.txt",
                f"{prefix}_ADJUGATE_KERNEL_105.tsv",
                f"{prefix}_ENDPOINT_DELTA2_CLEARED_NF.tsv",
                f"{prefix}_ENDPOINT_TWO_SHIFT_PLANT.txt")
    raise RuntimeError(f"UNKNOWN_STAGE_WRITE_SET:{label}")


class Classifier:
    def __init__(self, production: Path, prepared: Path, build: Path,
                 r5, gate, recursor_mod, builder_mod, binding: Binding,
                 scratch: Path):
        self.production = production
        self.prepared = prepared
        self.build = build
        self.r5 = r5
        self.gate = gate
        self.recursor = recursor_mod
        self.builder = builder_mod
        self.binding = binding
        self.scratch = scratch
        self.scratch.mkdir(parents=True, exist_ok=True)
        self.observed_records: list[dict[str, object]] = []
        self.stage_identity_sha256: dict[str, str] = {}
        self.timeout_seen: tuple[object, str] | None = None

    # ---- one bound stage -------------------------------------------------

    def check_stage(self, node_dir: Path, node_key: object, label: str,
                    script_name: str, cap: int, ledger: Ledger,
                    expect_timeout: bool = False) -> list[str]:
        binding = self.binding
        script = node_dir / script_name
        stdout = node_dir / f"{label}.stdout.txt"
        stderr = node_dir / f"{label}.stderr.txt"
        result = node_dir / f"{label}.result.json"
        identity = node_dir / f"{label}.identity.json"
        for path, tag in ((script, "SCRIPT"), (stdout, "STDOUT"),
                          (stderr, "STDERR"), (result, "RESULT"),
                          (identity, "IDENTITY")):
            if not path.is_file():
                raise RuntimeError(f"STAGE_{tag}_MISSING:{label}")
        for name in (f"{label}.runner.stdout.txt",
                     f"{label}.runner.stderr.txt"):
            if not (node_dir / name).is_file():
                raise RuntimeError(f"STAGE_RUNNER_LOG_MISSING:{label}:{name}")
        ledger.require(script_name, *runner_files(label))
        payload = json.loads(result.read_text())
        if sorted(payload) != sorted(STAGE_RESULT_KEYS):
            raise RuntimeError(f"STAGE_RESULT_KEY_CENSUS:{label}")
        if payload["timed_out"] is not (True if expect_timeout else False):
            raise RuntimeError(f"STAGE_TIMEOUT_FLAG_DISAGREEMENT:{label}")
        if not expect_timeout and payload["returncode"] != 0:
            raise RuntimeError(f"STAGE_RETURNCODE_DISAGREEMENT:{label}")
        if (payload["stdout_sha256"] != sha256(stdout)
                or payload["stderr_sha256"] != sha256(stderr)
                or payload["script_sha256"] != sha256(script)):
            raise RuntimeError(f"STAGE_RESULT_CUSTODY_DISAGREEMENT:{label}")
        expected_argv = [binding.singular_path, "-q", str(script.resolve())]
        expected_result = {
            "argv": expected_argv,
            "cap_seconds": cap,
            "expected_pgid": binding.worker["pgid"],
            "expected_sid": binding.worker["sid"],
            "job_nonce": binding.job_nonce,
            "job_tag": binding.job_tag,
            "lease_sha256": binding.lease_sha256,
            "singular_sha256": binding.singular_sha256,
            "source_archive_sha256": binding.source_archive_sha256,
            "stage_label": label,
            "supervisor_starttime": binding.supervisor["starttime"],
            "worker_starttime": binding.worker["starttime"],
        }
        for key, expected in expected_result.items():
            if payload[key] != expected:
                raise RuntimeError(f"STAGE_RESULT_JOB_BINDING_DRIFT:{label}:{key}")
        if payload["identity_sha256"] != sha256(identity):
            raise RuntimeError(f"STAGE_IDENTITY_HASH_DISAGREEMENT:{label}")
        self.recursor.require_runner_logs(
            (node_dir / f"{label}.runner.stdout.txt").read_bytes(),
            (node_dir / f"{label}.runner.stderr.txt").read_bytes(),
            payload, label)
        record = json.loads(identity.read_text())
        if sorted(record) != sorted(self.recursor.IDENTITY_RECORD_KEYS):
            raise RuntimeError(f"STAGE_IDENTITY_KEY_CENSUS:{label}")
        expected_identity = {
            "argv": expected_argv,
            "cap_seconds": cap,
            "expected_pgid": binding.worker["pgid"],
            "expected_sid": binding.worker["sid"],
            "job_nonce": binding.job_nonce,
            "job_tag": binding.job_tag,
            "lease_sha256": binding.lease_sha256,
            "singular_binary_sha256": binding.singular_sha256,
            "singular_path": binding.singular_path,
            "source_archive_sha256": binding.source_archive_sha256,
            "stage_label": label,
        }
        for key, expected in expected_identity.items():
            if record.get(key) != expected:
                raise RuntimeError(
                    f"STAGE_IDENTITY_JOB_BINDING_DRIFT:{label}:{key}")
        for block, expected_pid, expected_start in (
                ("worker", binding.worker["pid"], binding.worker["starttime"]),
                ("supervisor", binding.supervisor["pid"],
                 binding.supervisor["starttime"])):
            live = record.get(block)
            if (not isinstance(live, dict) or live.get("pid") != expected_pid
                    or live.get("starttime") != expected_start):
                raise RuntimeError(
                    f"STAGE_IDENTITY_{block.upper()}_DISAGREEMENT:{label}")
        worker_block = record["worker"]
        if (worker_block.get("pgid") != binding.worker["pgid"]
                or worker_block.get("sid") != binding.worker["sid"]):
            raise RuntimeError(f"STAGE_IDENTITY_WORKER_CONTAINMENT:{label}")
        for block in ("runner", "singular"):
            live = record.get(block)
            if (not isinstance(live, dict)
                    or live.get("pgid") != binding.worker["pgid"]
                    or live.get("sid") != binding.worker["sid"]
                    or not isinstance(live.get("starttime"), int)
                    or live.get("uid") != worker_block.get("uid")):
                raise RuntimeError(
                    f"STAGE_IDENTITY_{block.upper()}_CONTAINMENT:{label}")
        if (not record.get("runner_cgroup")
                or record.get("runner_cgroup") != record.get("singular_cgroup")):
            raise RuntimeError(f"STAGE_IDENTITY_CGROUP_DISAGREEMENT:{label}")
        self.stage_identity_sha256[f"{node_key}:{label}"] = payload[
            "identity_sha256"]
        self.observed_records.append({
            "node": node_key,
            "stage": label,
            "returncode": payload["returncode"],
            "timed_out": payload["timed_out"],
            "script_sha256": payload["script_sha256"],
            "stdout_sha256": payload["stdout_sha256"],
            "stderr_sha256": payload["stderr_sha256"],
            "identity_sha256": payload["identity_sha256"],
            "result_sha256": sha256(result),
        })
        if expect_timeout:
            if self.timeout_seen is not None:
                raise RuntimeError("MULTIPLE_TIMED_OUT_STAGES")
            self.timeout_seen = (node_key, label)
            return []
        lines = stdout.read_text(errors="strict").splitlines()
        self.gate.assert_clean_transcript(stdout, stderr)
        if any(line.startswith("FATAL_") for line in lines):
            raise RuntimeError(f"FATAL_MARKER_IN_STAGE:{label}")
        return lines

    def require_script_bytes(self, node_dir: Path, script_name: str,
                             expected_text: str, label: str) -> None:
        if (node_dir / script_name).read_text() != expected_text:
            raise RuntimeError(f"SCRIPT_REGENERATION_DISAGREEMENT:{label}")

    # ---- census helpers --------------------------------------------------

    @staticmethod
    def require_lines(lines: list[str], markers: tuple[str, ...],
                      label: str) -> None:
        bad = [marker for marker in markers if lines.count(marker) != 1]
        if bad:
            raise RuntimeError(f"MARKER_CENSUS:{label}:{','.join(bad)}")

    @staticmethod
    def parse_exact_int(lines: list[str], key: str) -> int:
        prefix = key + "="
        values = [line[len(prefix):] for line in lines
                  if line.startswith(prefix)]
        if len(values) != 1:
            raise RuntimeError(f"INTEGER_MARKER_CENSUS:{key}:{len(values)}")
        return int(values[0])

    @staticmethod
    def require_file_census(path: Path, header: str, records: int) -> str:
        lines = path.read_text().splitlines()
        if len(lines) != records + 1 or lines[0] != header:
            raise RuntimeError(f"ARTIFACT_CENSUS:{path.name}:{len(lines)}")
        return sha256(path)

    @staticmethod
    def require_exact_match(actual: Path, expected: Path, label: str) -> str:
        if actual.read_bytes() != expected.read_bytes():
            raise RuntimeError(f"EXACT_REPLAY_DISAGREEMENT:{label}")
        return sha256(actual)

    def verify_node_sb(self, node_dir: Path, node_index: int,
                       header_stage_count: int, had_timeout: bool) -> None:
        """Exact append law (R3, O-N1): the node standard basis is exactly
        one identical single-line write() block per completed header-writing
        stage.  A doubled file (two appends per stage) is refused because its
        per-stage block would contain two newlines."""
        path = node_dir / f"NODE_{node_index:03d}_STANDARD_BASIS.txt"
        if had_timeout:
            # A timed-out stage may have appended a partial copy; only
            # presence is decidable.
            if not path.is_file():
                raise RuntimeError(f"NODE_SB_MISSING:{node_index}")
            return
        self.recursor.require_single_line_append_stack(
            path.read_bytes(), header_stage_count,
            f"NODE_{node_index:03d}_STANDARD_BASIS")

    # ---- witness replay --------------------------------------------------

    def classify_witness_replay(self, remaining, generators, label_component,
                                assignment, delta,
                                expect_timeout: bool) -> dict[str, object]:
        witness_dir = self.production / "witness_replay"
        if not witness_dir.is_dir():
            raise RuntimeError("WITNESS_REPLAY_DIRECTORY_MISSING")
        ledger = Ledger(witness_dir)
        build_manifest = json.loads(
            (self.build / "BUILD_MANIFEST.json").read_text())
        expected_script = self.builder.build_witness_replay_script(
            self.r5, remaining, generators, label_component, assignment, delta)
        self.builder.validate_witness_replay_script(expected_script, delta)
        if sha256_text(expected_script) != build_manifest[
                "generated_witness_replay_sha256"]:
            raise RuntimeError("WITNESS_REPLAY_BUILD_MANIFEST_DRIFT")
        if (self.build / "TRIPLE02_NODE1_WITNESS_REPLAY.sing"
                ).read_text() != expected_script:
            raise RuntimeError("WITNESS_REPLAY_BUILD_COPY_DRIFT")
        self.require_script_bytes(witness_dir, "witness_replay.sing",
                                  expected_script, "witness_replay")
        lines = self.check_stage(witness_dir, "witness", "witness_replay",
                                 "witness_replay.sing", self.binding.fast_cap,
                                 ledger, expect_timeout)
        writes = ("NODE_001_STANDARD_BASIS.txt", "NODE_001_REDUCE_PIVOTS.tsv",
                  "NODE_001_REDUCE_RESIDUAL.tsv",
                  "NODE_002_SEED_STANDARD_BASIS.txt")
        if expect_timeout:
            ledger.allow_partial(*writes)
            ledger.close()
            return {"witness_replay_timed_out": True}
        ledger.require(*writes)
        self.require_lines(lines, WITNESS_REPLAY_MARKERS, "witness_replay")
        if sum(line in lines for line in
               ("CLOSED_SUCCESSOR_EMPTY=0", "CLOSED_SUCCESSOR_EMPTY=1")) != 1:
            raise RuntimeError("CLOSED_SUCCESSOR_EMPTY_MARKER_CENSUS")
        produced_sb = (witness_dir / "NODE_001_STANDARD_BASIS.txt").read_bytes()
        archived_sb = (self.prepared
                       / "r3/output/node_001/NODE_001_STANDARD_BASIS.txt"
                       ).read_bytes()
        self.recursor.require_archived_append_copies(
            produced_sb, archived_sb,
            self.recursor.ARCHIVED_NODE1_SB_APPEND_COUNT,
            "NODE_001_STANDARD_BASIS")
        hashes = {"NODE_001_STANDARD_BASIS.txt":
                  hashlib.sha256(produced_sb).hexdigest()}
        for produced, archived in (
                ("NODE_001_REDUCE_PIVOTS.tsv",
                 "r3/output/node_001/NODE_001_REDUCE_PIVOTS.tsv"),
                ("NODE_001_REDUCE_RESIDUAL.tsv",
                 "r3/output/node_001/NODE_001_REDUCE_RESIDUAL.tsv")):
            hashes[produced] = self.require_exact_match(
                witness_dir / produced, self.prepared / archived,
                f"witness:{produced}")
        ledger.close()
        return {"witness_replay_artifact_sha256": hashes,
                "closed_successor_empty_at_seed":
                    "CLOSED_SUCCESSOR_EMPTY=1" in lines}

    # ---- one node --------------------------------------------------------

    def classify_node(self, node_dir: Path, node_index: int,
                      generators: list[str], rank_bound: int,
                      remaining, label_component, assignment,
                      timeout_label: str | None) -> dict[str, object]:
        r5 = self.r5
        ledger = Ledger(node_dir)
        ledger.require("NODE_INPUT.json")
        prefix = f"NODE_{node_index:03d}"
        node_input = json.loads((node_dir / "NODE_INPUT.json").read_text())
        generators_sha = [sha256_text(value) for value in generators]
        if (node_input.get("node") != node_index
                or node_input.get("inherited_rank_upper_bound") != rank_bound
                or node_input.get("generator_sha256") != generators_sha
                or node_input.get("closed_successor_of_node") != node_index - 1
                or node_input.get("generators") != generators):
            raise RuntimeError(f"NODE_INPUT_CHAIN_DRIFT:{node_index}")
        outcome: dict[str, object] = {"node": node_index,
                                      "rank_upper_bound_in": rank_bound}
        header_stages = 0
        had_timeout = False

        def finish(status: str) -> dict[str, object]:
            self.verify_node_sb(node_dir, node_index, max(header_stages, 1),
                                had_timeout)
            ledger.close()
            outcome["status"] = status
            outcome["artifact_census"] = sorted(
                entry.name for entry in node_dir.iterdir())
            return outcome

        # reduce ------------------------------------------------------------
        expected_reduce = r5.build_reduce_script(
            remaining, generators, node_index, label_component, assignment)
        if timeout_label == "reduce":
            had_timeout = True
            self.check_stage(node_dir, node_index, "reduce", "reduce.sing",
                             self.binding.slow_cap, ledger,
                             expect_timeout=True)
            self.require_script_bytes(node_dir, "reduce.sing",
                                      expected_reduce, f"reduce:{node_index}")
            ledger.allow_partial(*stage_singular_writes(
                node_index, "reduce", rank_bound))
            return finish("STAGE_TIMEOUT")
        reduce_lines = self.check_stage(
            node_dir, node_index, "reduce", "reduce.sing",
            self.binding.slow_cap, ledger)
        self.require_script_bytes(node_dir, "reduce.sing", expected_reduce,
                                  f"reduce:{node_index}")
        header_stages += 1
        if "EXACT_EMPTY_NODE=1" in reduce_lines:
            self.require_lines(reduce_lines, (
                f"NODE_INDEX={node_index}",
                f"NODE_GENERATOR_COUNT={len(generators)}",
                "NODE_EMPTY=1",
                "EXACT_EMPTY_NODE=1",
            ), f"reduce:{node_index}")
            ledger.require(f"{prefix}_STANDARD_BASIS.txt")
            return finish("EXACT_EMPTY_NODE")
        self.require_lines(reduce_lines, (
            f"NODE_INDEX={node_index}",
            f"NODE_GENERATOR_COUNT={len(generators)}",
            "NODE_EMPTY=0",
            "NODE_REDUCER_FIXTURES_PASS=1",
            "NF_RATIONAL_UNIT_PIVOT_COUNT=95",
            "NF_PIVOT_INVARIANT_FAILURES=0",
            "NODE_RESIDUAL_REDUCTION_COMPLETE=1",
            "NODE_REDUCE_COMPLETE=1",
        ), f"reduce:{node_index}")
        ledger.require(*stage_singular_writes(node_index, "reduce",
                                              rank_bound))
        self.require_file_census(node_dir / f"{prefix}_REDUCE_PIVOTS.tsv",
                                 "step|source_row|source_col|pivot", 95)
        self.require_file_census(node_dir / f"{prefix}_REDUCE_RESIDUAL.tsv",
                                 "rows|11|cols|10", 110)
        residual = r5.read_residual(node_dir / f"{prefix}_REDUCE_RESIDUAL.tsv")

        # rank census -------------------------------------------------------
        rank = -1
        for size in range(rank_bound, -1, -1):
            stage = f"rank_size_{size}"
            census_scratch = self.scratch / (
                f"{prefix}_rank_size_{size}.support.json")
            expected_script = r5.build_rank_size_script(
                remaining, generators, node_index, residual, size,
                census_scratch)
            if timeout_label == stage:
                had_timeout = True
                self.check_stage(node_dir, node_index, stage, f"{stage}.sing",
                                 self.binding.slow_cap, ledger,
                                 expect_timeout=True)
                self.require_script_bytes(node_dir, f"{stage}.sing",
                                          expected_script,
                                          f"{stage}:{node_index}")
                ledger.require(f"{stage}.support.json")
                if (node_dir / f"{stage}.support.json").read_bytes() != (
                        census_scratch.read_bytes()):
                    raise RuntimeError(
                        f"RANK_CENSUS_REGENERATION_DRIFT:{node_index}:{size}")
                ledger.allow_partial(*stage_singular_writes(
                    node_index, stage, rank_bound))
                return finish("STAGE_TIMEOUT")
            lines = self.check_stage(node_dir, node_index, stage,
                                     f"{stage}.sing", self.binding.slow_cap,
                                     ledger)
            self.require_script_bytes(node_dir, f"{stage}.sing",
                                      expected_script, f"{stage}:{node_index}")
            header_stages += 1
            ledger.require(f"{stage}.support.json",
                           *stage_singular_writes(node_index, stage,
                                                  rank_bound))
            if (node_dir / f"{stage}.support.json").read_bytes() != (
                    census_scratch.read_bytes()):
                raise RuntimeError(
                    f"RANK_CENSUS_REGENERATION_DRIFT:{node_index}:{size}")
            census = json.loads(census_scratch.read_text())
            self.require_lines(lines, (
                f"RANK_SIZE={size}",
                "SUPPORT_REPLAY_FAILURES=0",
                "RANK_SIZE_CENSUS_COMPLETE=1",
            ), f"{stage}:{node_index}")
            found = "RANK_SIZE_WITNESS_FOUND=1" in lines
            self.require_file_census(
                node_dir / f"{prefix}_SIZE_{size}_MINORS.tsv",
                "slot|rows|cols|normal_form", census["support_matchable"])
            self.require_file_census(
                node_dir / f"{prefix}_SIZE_{size}_WITNESS.tsv",
                "rank|rows|cols|normal_form", 1 if found else 0)
            if found:
                rank = size
                break
            if "EVERY_MATCHABLE_MINOR_AT_SIZE_NF_ZERO=1" not in lines:
                raise RuntimeError(
                    f"MISSING_ZERO_SIZE_CERTIFICATE:{node_index}:{size}")
        if rank < 0:
            raise RuntimeError(f"NO_RANK_WITNESS:{node_index}")
        rows, cols, delta = r5.read_witness(
            node_dir / f"{prefix}_SIZE_{rank}_WITNESS.tsv", rank)
        delta_sha = sha256_text(delta)
        if delta_sha == DELTA_NODE1_SHA256 or delta_sha in generators_sha:
            raise RuntimeError(f"NODE_DELTA_ROUTE_GUARD:{node_index}")
        outcome.update({"rank": rank, "delta_sha256": delta_sha})

        # saturation ---------------------------------------------------------
        expected_saturation = self.recursor.build_repaired_saturation_script(
            r5, remaining, generators, node_index, delta)
        self.recursor.validate_saturation_script(
            expected_saturation, node_index, len(generators), delta)
        if timeout_label == "saturation":
            had_timeout = True
            self.check_stage(node_dir, node_index, "saturation",
                             "saturation.sing", self.binding.slow_cap,
                             ledger, expect_timeout=True)
            self.require_script_bytes(node_dir, "saturation.sing",
                                      expected_saturation,
                                      f"saturation:{node_index}")
            ledger.allow_partial(*stage_singular_writes(
                node_index, "saturation", rank_bound))
            return finish("STAGE_TIMEOUT")
        saturation_lines = self.check_stage(
            node_dir, node_index, "saturation", "saturation.sing",
            self.binding.slow_cap, ledger)
        self.require_script_bytes(node_dir, "saturation.sing",
                                  expected_saturation,
                                  f"saturation:{node_index}")
        header_stages += 1
        exhausted = ("REVERSE_CONTAINMENT_WITNESS_SEARCH_EXHAUSTED_"
                     "NO_VERDICT=1") in saturation_lines
        self.require_lines(saturation_lines, (
            "NODE_REDUCER_FIXTURES_PASS=1",
            "SATURATION_OBJECT_TYPE=list",
            "SATURATION_OBJECT_SIZE=1",
            "SATURATION_SLOT1_TYPE=ideal",
            "SATURATION_NODE_INCLUSION_FAILURES=0",
            "SATURATION_STABILITY_FAILURES=0",
            "REVERSE_CONTAINMENT_SEARCH_BOUND=64",
        ), f"saturation:{node_index}")
        reverse_entered = "REVERSE_CONTAINMENT_ENTERED=1" in saturation_lines
        if reverse_entered:
            basis_count = self.parse_exact_int(
                saturation_lines, "REVERSE_CONTAINMENT_BASIS_GENERATOR_COUNT")
            found_count = self.parse_exact_int(
                saturation_lines, "REVERSE_CONTAINMENT_WITNESS_FOUND_COUNT")
            reduction_count = self.parse_exact_int(
                saturation_lines,
                "REVERSE_CONTAINMENT_MEMBERSHIP_REDUCTION_COUNT")
            if (basis_count < 1
                    or not basis_count <= reduction_count <= 65 * basis_count):
                raise RuntimeError(f"REVERSE_CONTAINMENT_COUNTS:{node_index}")
            self.require_file_census(
                node_dir / f"{prefix}_REVERSE_CONTAINMENT_ATTEMPTS.tsv",
                "basis_generator|exponent|normal_form", reduction_count)
            self.require_file_census(
                node_dir / f"{prefix}_REVERSE_CONTAINMENT_WITNESSES.tsv",
                "basis_generator|found|exponent|normal_form", basis_count)
        else:
            for name, header in (
                    (f"{prefix}_REVERSE_CONTAINMENT_ATTEMPTS.tsv",
                     "basis_generator|exponent|normal_form"),
                    (f"{prefix}_REVERSE_CONTAINMENT_WITNESSES.tsv",
                     "basis_generator|found|exponent|normal_form")):
                self.require_file_census(node_dir / name, header, 0)
        if exhausted:
            if not reverse_entered or found_count >= basis_count:
                raise RuntimeError(
                    f"REVERSE_EXHAUSTION_EVIDENCE_DISAGREEMENT:{node_index}")
            if any(line.startswith("SATURATION_CERTIFICATE_COMPLETE=")
                   for line in saturation_lines):
                raise RuntimeError(
                    f"EXHAUSTED_WITH_COMPLETE_MARKER:{node_index}")
            base_writes = set(stage_singular_writes(node_index, "saturation",
                                                    rank_bound))
            base_writes.discard(f"{prefix}_EMPTY_OPEN_POWER_CERTIFICATE.txt")
            base_writes.discard(f"{prefix}_NEXT_STANDARD_BASIS.txt")
            ledger.require(*sorted(base_writes))
            return finish("REVERSE_EXHAUSTED")
        if reverse_entered and found_count != basis_count:
            raise RuntimeError(
                f"REVERSE_INCOMPLETE_WITHOUT_EXHAUSTION:{node_index}")
        self.require_lines(saturation_lines, (
            "SATURATION_CERTIFICATE_COMPLETE=1",
            "OPEN_SATURATION_AND_CLOSED_SUCCESSOR_COMPLETE=1",
        ), f"saturation-complete:{node_index}")
        ledger.require(*stage_singular_writes(node_index, "saturation",
                                              rank_bound))
        if sum(line in saturation_lines for line in
               ("OPEN_CHART_EMPTY=0", "OPEN_CHART_EMPTY=1")) != 1:
            raise RuntimeError(f"OPEN_CHART_EMPTY_CENSUS:{node_index}")
        if sum(line in saturation_lines for line in
               ("NEXT_REMAINDER_EMPTY=0", "NEXT_REMAINDER_EMPTY=1")) != 1:
            raise RuntimeError(f"NEXT_REMAINDER_EMPTY_CENSUS:{node_index}")
        open_empty = "OPEN_CHART_EMPTY=1" in saturation_lines
        next_empty = "NEXT_REMAINDER_EMPTY=1" in saturation_lines
        certificate = r5.validate_empty_open_certificate(
            node_dir / f"{prefix}_EMPTY_OPEN_POWER_CERTIFICATE.txt",
            open_empty)
        outcome.update({"open_chart_empty_by_saturation": open_empty,
                        "next_remainder_empty": next_empty,
                        "empty_open_power_certificate": certificate})
        if open_empty:
            self.require_lines(saturation_lines, (
                "EMPTY_OPEN_POWER_MEMBERSHIP_CERTIFICATE=1",
                "PROPER_OPEN_IDEAL_CERTIFICATE=0",
                "EMPTY_BRANCH_POWER_SEARCH_ENTERED=1",
                "REVERSE_CONTAINMENT_ENTERED=0",
            ), f"saturation-empty:{node_index}")
            ledger.require("NODE_RESULT.json")
            self.verify_node_result(node_dir, node_index, outcome, delta,
                                    chart_ran=False)
            return finish("OPEN_EMPTY")
        self.require_lines(saturation_lines, (
            "EMPTY_OPEN_POWER_MEMBERSHIP_CERTIFICATE=0",
            "PROPER_OPEN_IDEAL_CERTIFICATE=1",
            "EMPTY_BRANCH_POWER_SEARCH_ENTERED=0",
            "REVERSE_CONTAINMENT_ENTERED=1",
        ), f"saturation-proper:{node_index}")

        # chart ---------------------------------------------------------------
        free = 10 - rank
        expected_chart = self.recursor.build_repaired_chart_script(
            r5, remaining, generators, node_index, label_component,
            assignment, residual, rank, rows, cols, delta)
        self.recursor.validate_chart_script(expected_chart, node_index,
                                            len(generators), rank, delta)
        if timeout_label == "chart":
            had_timeout = True
            self.check_stage(node_dir, node_index, "chart", "chart.sing",
                             self.binding.slow_cap, ledger,
                             expect_timeout=True)
            self.require_script_bytes(node_dir, "chart.sing", expected_chart,
                                      f"chart:{node_index}")
            ledger.allow_partial(*stage_singular_writes(
                node_index, "chart", rank_bound))
            return finish("STAGE_TIMEOUT")
        chart_lines = self.check_stage(node_dir, node_index, "chart",
                                       "chart.sing", self.binding.slow_cap,
                                       ledger)
        self.require_script_bytes(node_dir, "chart.sing", expected_chart,
                                  f"chart:{node_index}")
        header_stages += 1
        ledger.require("NODE_RESULT.json",
                       *stage_singular_writes(node_index, "chart", rank_bound))
        self.require_lines(chart_lines, (
            "CHART_SATURATION_OBJECT_TYPE=list",
            "CHART_SATURATION_OBJECT_SIZE=1",
            "CHART_SATURATION_SLOT1_TYPE=ideal",
            "CHART_SATURATION_NODE_INCLUSION_FAILURES=0",
            "CHART_SATURATION_STABILITY_FAILURES=0",
            "CHART_OPEN_PROPER_IDEAL_CERTIFICATE=1",
            "OPEN_CHART_SATURATION_PROPER=1",
            "CHART_PIVOT_REDUCER=NODE_SB",
            "CHART_BASE_CHANGE_REDUCTION_COUNT=11135",
            "RESIDUAL_BASE_CHANGE_ENTRY_COUNT=110",
            "RIGHT_TRANSFORM_ENTRY_COUNT=11025",
            "RIGHT_TRANSFORM_RECORDED_ENTRY_COUNT=11025",
            "FULL_RIGHT_TRANSFORM_RECONSTRUCTED=1",
            "NODE_TRANSFORM_BASE_CHANGED_TO_ACTIVE_SB=1",
            "NF_RATIONAL_UNIT_PIVOT_COUNT=95",
            "NF_PIVOT_INVARIANT_FAILURES=0",
            f"ADJUGATE_KERNEL_VECTOR_COUNT={free}",
            "CHART_DELTA_NF_NONZERO=1",
            "SCANNED_DELTA_REPLAY_EQUAL=1",
            f"COMPLETE_BORDERED_IDENTITY_COUNT={11 * free}",
            "BORDERED_IDENTITY_FAILURES=0",
            "BORDERED_NONZERO_PLANT_NF_NONZERO=1",
            "BORDERED_NONZERO_PLANT_EQUALS_DELTA=1",
            f"FULL_106_ROW_KERNEL_REPLAY_COUNT={106 * free}",
            "FULL_106_ROW_KERNEL_REPLAY_FAILURES=0",
            f"LIFTED_KERNEL_ENTRY_COUNT={105 * free}",
            "ENDPOINT_PLUS_ONE_PLANT_AFFINE_REPLAY=1",
            "ENDPOINT_PLUS_TWO_PLANT_AFFINE_REPLAY=1",
            "ENDPOINT_TWO_SHIFT_AT_LEAST_ONE_NONZERO=1",
            "ENDPOINT_QUADRATIC=x14*x72+x1*x97",
            "ENDPOINT_DELTA2_DENOMINATOR_CLEARED=1",
            f"ENDPOINT_COEFFICIENT_COUNT={free * (free + 1) // 2}",
            "NO_FACTOR_GCD_CONTENT_RADICAL_NORMALIZATION=1",
            "RECURSIVE_ENDPOINT_CHART_COMPLETE=1",
        ), f"chart:{node_index}")
        self.require_file_census(node_dir / f"{prefix}_CHART_PIVOTS.tsv",
                                 "step|source_row|source_col|pivot", 95)
        self.require_exact_match(node_dir / f"{prefix}_CHART_PIVOTS.tsv",
                                 node_dir / f"{prefix}_REDUCE_PIVOTS.tsv",
                                 f"chart-pivots:{node_index}")
        self.require_file_census(node_dir / f"{prefix}_CHART_RESIDUAL.tsv",
                                 "rows|11|cols|10", 110)
        self.require_exact_match(node_dir / f"{prefix}_CHART_RESIDUAL.tsv",
                                 node_dir / f"{prefix}_REDUCE_RESIDUAL.tsv",
                                 f"chart-residual:{node_index}")
        self.require_file_census(
            node_dir / f"{prefix}_CHART_BASE_CHANGED_RESIDUAL.tsv",
            "rows|11|cols|10", 110)
        self.require_file_census(
            node_dir / f"{prefix}_BASE_CHANGED_RIGHT_TRANSFORM.tsv",
            "row|col|normal_form", 11025)
        self.require_file_census(node_dir / f"{prefix}_BORDERED_IDENTITIES.tsv",
                                 "basis|free_col|residual_row|normal_form",
                                 11 * free)
        self.require_file_census(node_dir / f"{prefix}_ADJUGATE_KERNEL_105.tsv",
                                 "coordinate|basis|normal_form", 105 * free)
        self.require_file_census(
            node_dir / f"{prefix}_ENDPOINT_DELTA2_CLEARED_NF.tsv",
            "basis_i|basis_j|normal_form", free * (free + 1) // 2)
        for name in (f"{prefix}_ENDPOINT_TWO_SHIFT_PLANT.txt",
                     f"{prefix}_BORDERED_NONZERO_PLANT.txt",
                     f"{prefix}_CHART_DELTA.txt"):
            if not (node_dir / name).is_file():
                raise RuntimeError(f"CHART_ARTIFACT_MISSING:{node_index}:{name}")
        self.require_exact_match(
            node_dir / f"{prefix}_CHART_ACTIVE_STANDARD_BASIS.txt",
            node_dir / f"{prefix}_OPEN_SAT_STANDARD_BASIS.txt",
            f"active-sb:{node_index}")
        chart_delta = "".join((node_dir / f"{prefix}_CHART_DELTA.txt")
                              .read_text().split())
        if not chart_delta or sha256_text(chart_delta) == DELTA_NODE1_SHA256:
            raise RuntimeError(f"CHART_DELTA_ROUTE_GUARD:{node_index}")
        endpoint_nonzero = self.parse_exact_int(
            chart_lines, "ENDPOINT_COEFFICIENT_NF_NONZERO_COUNT")
        if not 0 <= endpoint_nonzero <= free * (free + 1) // 2:
            raise RuntimeError(f"ENDPOINT_NONZERO_RANGE:{node_index}")
        dead_marker = "CHART_CLASSIFICATION=ENDPOINT_DEAD_ONLY_ON_D_DELTA"
        survivor_marker = ("CHART_CLASSIFICATION=RING_LEVEL_SURVIVOR_ON_CHART_"
                           "PENDING_NILPOTENCE_RADICAL")
        if chart_lines.count(dead_marker) + chart_lines.count(
                survivor_marker) != 1:
            raise RuntimeError(f"CHART_CLASSIFICATION_CENSUS:{node_index}")
        if endpoint_nonzero == 0 and dead_marker in chart_lines:
            status = "CHART_DEAD"
        elif endpoint_nonzero > 0 and survivor_marker in chart_lines:
            status = "CHART_SURVIVOR"
        else:
            raise RuntimeError(f"ENDPOINT_COUNT_CLASSIFICATION:{node_index}")
        outcome["endpoint_coefficient_nf_nonzero_count"] = endpoint_nonzero
        self.verify_node_result(node_dir, node_index, outcome, delta,
                                chart_ran=True)
        return finish(status)

    def verify_node_result(self, node_dir: Path, node_index: int,
                           outcome: dict[str, object], delta: str,
                           chart_ran: bool) -> None:
        record = json.loads((node_dir / "NODE_RESULT.json").read_text())
        expectations = {
            "node": node_index,
            "rank": outcome["rank"],
            "rank_upper_bound_in": outcome["rank_upper_bound_in"],
            "delta_sha256": outcome["delta_sha256"],
            "delta_is_settled_node1_delta": False,
            "open_chart_empty_by_saturation":
                outcome["open_chart_empty_by_saturation"],
            "next_remainder_empty": outcome["next_remainder_empty"],
        }
        for key, expected in expectations.items():
            if record.get(key) != expected:
                raise RuntimeError(f"NODE_RESULT_DRIFT:{node_index}:{key}")
        if "".join(str(record.get("delta", "")).split()) != delta:
            raise RuntimeError(f"NODE_RESULT_DELTA_DRIFT:{node_index}")
        if chart_ran:
            if not isinstance(record.get("saturated_delta_normal_form"), str):
                raise RuntimeError(f"NODE_RESULT_SATURATED_DELTA:{node_index}")

    # ---- whole production tree ------------------------------------------

    def classify(self) -> dict[str, object]:
        r5 = self.r5
        resume_input = json.loads(
            (self.build / "RESUME_NODE_INPUT.json").read_text())
        generators = [r5.clean_poly(value)
                      for value in resume_input["generators"]]
        if (tuple(resume_input.get("generator_sha256", []))
                != NODE2_GENERATOR_SHA256
                or tuple(sha256_text(value) for value in generators)
                != NODE2_GENERATOR_SHA256
                or resume_input.get("inherited_rank_upper_bound") != 6):
            raise RuntimeError("RESUME_NODE_INPUT_DRIFT")
        base = self.prepared / "r3/work/base"
        label_component, zeros, factor, remaining, assignment, counts = (
            r5.source_inputs(base, "triple02"))
        if (label_component != "TRIPLE02"
                or remaining != ["q0", "q2", "c4", "c6"]
                or r5.clean_poly(factor) != generators[0]):
            raise RuntimeError("CLASSIFIER_SOURCE_RECONSTRUCTION_DRIFT")
        node2_expected = r5.build_reduce_script(
            remaining, generators, 2, label_component, assignment)
        if (self.build / "NODE_002_REDUCE_EXPECTED.sing"
                ).read_text() != node2_expected:
            raise RuntimeError("NODE2_REDUCE_BUILD_COPY_DRIFT")
        driver_summary = json.loads(
            (self.production / "SUMMARY.json").read_text())
        driver_verdict = (self.production / "VERDICT.txt").read_text().strip()
        if driver_summary.get("classification") != driver_verdict:
            raise RuntimeError("DRIVER_SUMMARY_VERDICT_DISAGREEMENT")
        if driver_verdict not in ALLOWED:
            raise RuntimeError(f"DRIVER_VERDICT_NOT_ALLOWED:{driver_verdict}")
        for key, expected in (
                ("component", "triple02"),
                ("start_node", START_NODE),
                ("closed_successor_of_node", 1),
                ("settled_open_route", "NEVER_REENTERED"),
                ("delta_node1_sha256", DELTA_NODE1_SHA256),
                ("no_radical_nilpotence_or_geometric_inference", True),
                ("whole_component_or_jc2_inference", False),
                ("job_binding", self.binding.job_binding_block())):
            if driver_summary.get(key) != expected:
                raise RuntimeError(f"DRIVER_SUMMARY_SCOPE_DRIFT:{key}")
        reason = driver_summary.get("no_verdict_reason")
        timeout_node: object = None
        timeout_stage: str | None = None
        if isinstance(reason, str) and reason.startswith("STAGE_TIMEOUT:"):
            _, timeout_node_text, timeout_stage = reason.split(":", 2)
            timeout_node = (int(timeout_node_text)
                            if timeout_node_text.isdigit()
                            else timeout_node_text)
        witness_timeout = (timeout_node == "witness"
                           and timeout_stage == "witness_replay")
        witness_payload = self.classify_witness_replay(
            remaining, generators[:2], label_component, assignment,
            generators[2], witness_timeout)
        node_dirs = sorted(item for item in self.production.iterdir()
                           if item.is_dir() and item.name.startswith("node_"))
        root_ledger = Ledger(self.production)
        root_ledger.require("SUMMARY.json", "VERDICT.txt", "witness_replay",
                            *(item.name for item in node_dirs))
        root_ledger.close()
        if any(item.name == "node_001" for item in node_dirs):
            raise RuntimeError("SETTLED_NODE1_DIRECTORY_PRESENT")
        expected_names = [f"node_{index:03d}"
                          for index in range(2, 2 + len(node_dirs))]
        if [item.name for item in node_dirs] != expected_names:
            raise RuntimeError("NODE_DIRECTORY_NUMBERING_DRIFT")
        if witness_timeout and node_dirs:
            raise RuntimeError("WITNESS_TIMEOUT_WITH_NODE_DIRECTORIES")
        chain_generators = list(generators)
        chain_bound = 6
        outcomes: list[dict[str, object]] = []
        derived: str | None = None
        derived_reason: str | None = None
        summary_generators = list(chain_generators)
        summary_bound = chain_bound
        if witness_timeout:
            derived = CLASS_NO_VERDICT
            derived_reason = "STAGE_TIMEOUT:witness:witness_replay"
        for node_dir in node_dirs:
            node_index = int(node_dir.name.split("_")[1])
            this_timeout = (timeout_stage if timeout_node == node_index
                            else None)
            outcome = self.classify_node(
                node_dir, node_index, chain_generators, chain_bound,
                remaining, label_component, assignment, this_timeout)
            outcomes.append(outcome)
            status = outcome["status"]
            if status == "STAGE_TIMEOUT":
                derived = CLASS_NO_VERDICT
                derived_reason = f"STAGE_TIMEOUT:{node_index}:{timeout_stage}"
                summary_generators = list(chain_generators)
                summary_bound = chain_bound
                break
            if status == "EXACT_EMPTY_NODE":
                derived = CLASS_DEAD
                summary_generators = list(chain_generators)
                summary_bound = chain_bound
                break
            if status == "REVERSE_EXHAUSTED":
                derived = CLASS_REVERSE
                derived_reason = f"REVERSE_CONTAINMENT_EXHAUSTED:{node_index}"
                summary_generators = list(chain_generators)
                summary_bound = chain_bound
                break
            delta = self.node_delta(node_dir, node_index, outcome)
            if status == "CHART_SURVIVOR":
                derived = CLASS_SURVIVOR
                summary_generators = list(chain_generators)
                summary_bound = outcome["rank"]
                break
            if status in ("OPEN_EMPTY", "CHART_DEAD"):
                if outcome["next_remainder_empty"]:
                    derived = CLASS_DEAD
                    summary_generators = chain_generators + [delta]
                    summary_bound = outcome["rank"]
                    break
                chain_generators = chain_generators + [delta]
                chain_bound = outcome["rank"]
                summary_generators = list(chain_generators)
                summary_bound = chain_bound
                continue
            raise RuntimeError(f"UNKNOWN_NODE_STATUS:{status}")
        if derived is None:
            if len(node_dirs) != MAX_NODES:
                raise RuntimeError("LOOP_ENDED_WITHOUT_TERMINAL_OR_EXHAUSTION")
            derived = CLASS_NO_VERDICT
            derived_reason = f"MAX_NODES_EXHAUSTED:{FINAL_NODE}"
        # Bounded no-verdicts are re-derived from stage evidence.
        if derived in (CLASS_NO_VERDICT, CLASS_REVERSE):
            if reason != derived_reason:
                raise RuntimeError(
                    f"NO_VERDICT_REASON_DISAGREEMENT:{reason}:{derived_reason}")
        elif reason is not None:
            raise RuntimeError("UNEXPECTED_NO_VERDICT_REASON")
        if timeout_stage is not None and self.timeout_seen is None:
            raise RuntimeError("TIMEOUT_REASON_WITHOUT_TIMED_OUT_STAGE")
        if self.timeout_seen is not None and (
                timeout_stage is None
                or self.timeout_seen != (timeout_node, timeout_stage)
                or self.observed_records[-1]["timed_out"] is not True):
            raise RuntimeError("TIMED_OUT_STAGE_WITHOUT_MATCHING_REASON")
        if derived != driver_verdict:
            raise RuntimeError(
                f"CLASSIFIER_DRIVER_DISAGREEMENT:{derived}:{driver_verdict}")
        if (derived == CLASS_DEAD
                and any(outcome.get("status") == "CHART_SURVIVOR"
                        for outcome in outcomes)):
            raise RuntimeError("DEAD_VERDICT_WITH_SURVIVOR_NODE")
        if (driver_summary.get("open_remainder_generators")
                != summary_generators
                or driver_summary.get("open_remainder_generator_sha256")
                != [sha256_text(value) for value in summary_generators]
                or driver_summary.get("open_remainder_rank_upper_bound")
                != summary_bound):
            raise RuntimeError("DRIVER_REMAINDER_DISAGREEMENT")
        if driver_summary.get("stage_records") != self.observed_records:
            raise RuntimeError("DRIVER_STAGE_RECORD_DISAGREEMENT")
        return {
            "classification": derived,
            "closed_successor_of_node": 1,
            "component": "triple02",
            "endpoint_quadratic": "x14*x72+x1*x97",
            "final_rank_upper_bound": summary_bound,
            "job_binding": self.binding.job_binding_block(),
            "no_verdict_reason": derived_reason,
            "node_outcomes": outcomes,
            "nodes_processed": len(outcomes),
            "scope": ("TRIPLE02_NODE1_CLOSED_SUCCESSOR_FINITE_CHART_"
                      "RECURSION_ONLY"),
            "settled_open_route_reentered": False,
            "stage_identity_sha256": dict(sorted(
                self.stage_identity_sha256.items())),
            "stage_records": self.observed_records,
            "start_node": START_NODE,
            "whole_component_or_jc2_inference": False,
            **witness_payload,
        }

    def node_delta(self, node_dir: Path, node_index: int,
                   outcome: dict[str, object]) -> str:
        rows, cols, delta = self.r5.read_witness(
            node_dir / (f"NODE_{node_index:03d}_SIZE_"
                        f"{outcome['rank']}_WITNESS.tsv"),
            outcome["rank"])
        if sha256_text(delta) != outcome["delta_sha256"]:
            raise RuntimeError(f"NODE_DELTA_REREAD_DRIFT:{node_index}")
        return delta


def classify(production: Path, prepared: Path, build: Path, r5, gate,
             recursor_mod, builder_mod, binding: Binding,
             scratch: Path) -> dict[str, object]:
    classifier = Classifier(production, prepared, build, r5, gate,
                            recursor_mod, builder_mod, binding, scratch)
    return classifier.classify()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--production", required=True, type=Path)
    parser.add_argument("--prepared", required=True, type=Path)
    parser.add_argument("--build", required=True, type=Path)
    parser.add_argument("--frozen-r5-source", required=True, type=Path)
    parser.add_argument("--case-dir", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--job-tag", required=True)
    parser.add_argument("--job-nonce", required=True)
    parser.add_argument("--source-archive-sha256", required=True)
    parser.add_argument("--singular-sha256", required=True)
    parser.add_argument("--singular-path", required=True)
    parser.add_argument("--lease", required=True, type=Path)
    parser.add_argument("--worker-identity", required=True, type=Path)
    parser.add_argument("--supervisor-identity", required=True, type=Path)
    parser.add_argument("--fast-cap", type=int, default=900)
    parser.add_argument("--slow-cap", type=int, default=3600)
    args = parser.parse_args()
    r5 = load_pinned("frozen_r5_recursor", args.frozen_r5_source.resolve(),
                     FROZEN_R5_SHA256, with_parent_path=True)
    gate = load_pinned(
        "frozen_transcript_gate",
        args.frozen_r5_source.resolve().parent / "transcript_gate.py",
        TRANSCRIPT_GATE_SHA256)
    case_dir = args.case_dir.resolve()
    recursor_mod = load_case_module("classifier_recursor_templates",
                                    case_dir / "resume_recursor.py")
    builder_mod = load_case_module("classifier_builder_templates",
                                   case_dir / "build_resume.py")
    binding = Binding(args.job_tag, args.job_nonce,
                      args.source_archive_sha256, args.singular_sha256,
                      args.singular_path, args.lease.resolve(),
                      args.worker_identity.resolve(),
                      args.supervisor_identity.resolve(),
                      args.fast_cap, args.slow_cap)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    payload = classify(args.production.resolve(), args.prepared.resolve(),
                       args.build.resolve(), r5, gate, recursor_mod,
                       builder_mod, binding, output / "regeneration_scratch")
    payload["case_module_sha256"] = {
        "resume_recursor.py": sha256(case_dir / "resume_recursor.py"),
        "build_resume.py": sha256(case_dir / "build_resume.py"),
    }
    (output / "SUMMARY.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n")
    (output / "VERDICT.txt").write_text(str(payload["classification"]) + "\n")
    print(f"CLASSIFICATION={payload['classification']}")
    print("TRIPLE02_CLOSED_SUCCESSOR_CLASSIFIER_PASS=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
