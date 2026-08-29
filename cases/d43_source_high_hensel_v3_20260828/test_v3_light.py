#!/usr/bin/python3
"""Bounded fail-closed tests for the D43 high-Hensel v3 packet.

The default suite performs no real D43 context construction, CAS work, AWS
call, or p^3+ lift.  The corrected real p2-kernel attack is separately gated
by ``JC2_D43_V3_REAL_FIXTURE=1`` and is preregistered for independent AWS
review; the producer did not run it while sealing this packet.
"""

from __future__ import annotations

import copy
import hashlib
import json
import os
import pickle
import stat
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock


HERE = Path(__file__).resolve().parent
CASES = HERE.parent
ROOT = CASES.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(CASES))

import runner_v3 as H
import aws_supervisor_v3 as S


class HostilePickle:
    def __reduce__(self):
        return os.system, ("touch /tmp/D43_V3_PICKLE_ESCAPE",)


class LoaderTests(unittest.TestCase):
    def test_real_d21_restricted_census(self):
        payload = H.load_sealed_d21(ROOT / "directionb_tails_D21.pkl")
        self.assertEqual(payload["D"], 21)
        self.assertEqual(len(payload["vars"]), 183)
        self.assertEqual(sum(len(rows) for rows in payload["byk"].values()), 77)

    def test_hostile_pickle_cannot_execute(self):
        escape = Path("/tmp/D43_V3_PICKLE_ESCAPE")
        if escape.exists():
            self.skipTest("host sentinel pre-exists")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "hostile.pkl"
            raw = pickle.dumps(HostilePickle())
            path.write_bytes(raw)
            with self.assertRaises(pickle.UnpicklingError):
                H.load_sealed_d21(path, hashlib.sha256(raw).hexdigest())
        self.assertFalse(escape.exists())

    def test_d21_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            link = Path(directory) / "input.pkl"
            link.symlink_to(ROOT / "directionb_tails_D21.pkl")
            with self.assertRaisesRegex(ValueError, "symlink"):
                H.load_sealed_d21(link)

    def test_ambient_directionb_state_rejected(self):
        with mock.patch.dict(os.environ, {"DIRECTIONB_STATE": "/tmp/evil"}):
            with self.assertRaisesRegex(RuntimeError, "DIRECTIONB_STATE"):
                H.install_sealed_directionb_loaders(
                    ROOT / "directionb_tails_D21.pkl", H.EXPECTED_D21_SHA256)

    def test_runtime_guard_rejects_tmp(self):
        with tempfile.TemporaryDirectory(dir=str(ROOT)) as allowed:
            with tempfile.NamedTemporaryFile(dir="/tmp") as outside:
                with self.assertRaises(PermissionError):
                    with H.RuntimeReadGuard((Path(allowed),)):
                        Path(outside.name).read_bytes()

    def test_runtime_guard_is_process_global_across_threads(self):
        failures = []
        with tempfile.TemporaryDirectory(dir=str(ROOT)) as allowed:
            with tempfile.NamedTemporaryFile(dir="/tmp") as outside:
                def hostile_open():
                    try:
                        Path(outside.name).read_bytes()
                    except Exception as error:
                        failures.append(error)
                with H.RuntimeReadGuard((Path(allowed),)):
                    thread = __import__("threading").Thread(target=hostile_open)
                    thread.start()
                    thread.join()
        self.assertEqual(len(failures), 1)
        self.assertIsInstance(failures[0], PermissionError)

    def test_target64_custody_invariants_are_path_independent(self):
        observed = []
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for lane in ("n16", "n64"):
                execution = root / lane / "execution"
                private = root / lane / "private"
                certificate = execution / "cases" / "certificate.json"
                d21 = private / "directionb_tails_D21.pkl"
                certificate.parent.mkdir(parents=True)
                private.mkdir(parents=True)
                certificate.write_text("{}")
                d21.write_bytes(b"sealed")
                observed.append(H.portable_runtime_read_trace(
                    [str(certificate), str(d21)], execution, private, d21))
        self.assertEqual(observed[0], observed[1])
        self.assertEqual(observed[0], [
            "execution/cases/certificate.json",
            "job-private/directionb_tails_D21.pkl",
        ])


class EnvironmentTests(unittest.TestCase):
    def test_normalized_marker_environment_has_no_fixed_point(self):
        clean = {
            "HOME": "/job/home", "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8",
            "PATH": "/usr/bin:/bin", "TZ": "UTC", "PYTHONHASHSEED": "0",
            "PYTHONNOUSERSITE": "1", "PYTHONDONTWRITEBYTECODE": "1",
            "OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1",
            "MKL_NUM_THREADS": "1", "NUMEXPR_NUM_THREADS": "1",
            "VECLIB_MAXIMUM_THREADS": "1",
            "SHLVL": "0",
            "JC2_D43_HENSEL_AWS_AUTH": "/job/marker.json",
            "JC2_D43_HENSEL_AWS_AUTH_SHA256": "a" * 64,
        }
        with mock.patch.dict(os.environ, clean, clear=True):
            observed = H.sanitized_environment_snapshot(normalized=True)
        self.assertEqual(observed["JC2_D43_HENSEL_AWS_AUTH"],
                         H.AUTH_PATH_SENTINEL)
        self.assertEqual(observed["JC2_D43_HENSEL_AWS_AUTH_SHA256"],
                         H.AUTH_SHA_SENTINEL)
        self.assertEqual(observed["SHLVL"], "0")

    def test_path_bash_env_and_loader_injections_rejected(self):
        for key in ("BASH_ENV", "LD_PRELOAD", "LD_AUDIT",
                    "GLIBC_TUNABLES", "PYTHONPATH", "DIRECTIONB_STATE"):
            environment = dict(S.SUPERVISOR_REQUIRED_ENV)
            environment[key] = "/hostile"
            with self.subTest(key=key), mock.patch.dict(
                    os.environ, environment, clear=True):
                with self.assertRaises(S.CustodyFault):
                    S.reject_inherited_environment()
        bad_path = dict(S.SUPERVISOR_REQUIRED_ENV)
        bad_path["PATH"] = "/hostile"
        with mock.patch.dict(os.environ, bad_path, clear=True):
            with self.assertRaises(S.CustodyFault):
                S.reject_inherited_environment()


class PacketSealTests(unittest.TestCase):
    def test_manifest_prereg_and_core23_closure(self):
        manifest = HERE / "PAYLOAD.sha256"
        entries = S.parse_hash_manifest(ROOT, manifest)
        prereg = S.verify_preregistration(
            HERE / "preregistration_v3.json", entries,
            S.sha256_path(manifest))
        self.assertEqual(entries["cases/directionb_core23_p105337.ms"],
                         H.EXPECTED_CORE23_SHA256)
        self.assertEqual(entries["directionb_tails_D21.pkl"],
                         H.EXPECTED_D21_SHA256)
        self.assertEqual(prereg["status"], "V3_REVIEW_FROZEN_NO_AWS_LAUNCH")
        self.assertNotIn(
            "cases/d43_source_high_hensel_v3_20260828/PAYLOAD.sha256",
            entries)
        self.assertNotIn(
            "cases/d43_source_high_hensel_v3_20260828/preregistration_v3.json",
            entries)

    def test_authorization_template_includes_canonical_worker_path(self):
        template = json.loads((HERE / "authorization_template_v3.json").read_text())
        self.assertEqual(
            template["paths"]["worker"],
            "cases/d43_source_high_hensel_v3_20260828/aws_worker_v3.sh")

    def test_template_or_caller_self_authorization_rejected(self):
        template_path = HERE / "authorization_template_v3.json"
        template = json.loads(template_path.read_text())
        identity = template["expected_host_identity"]
        observed_sha = S.sha256_path(template_path)
        with mock.patch.object(
                S, "live_ec2_identity_and_tag",
                return_value=(identity, {"key": S.AUTHORIZATION_TAG_KEY,
                                         "value": "f" * 64})):
            with self.assertRaises(S.CustodyFault):
                S.load_live_authorization(template_path)
        # Even a tag matching these template bytes cannot activate a frozen
        # template; schema validation/status are independent gates.
        with mock.patch.object(
                S, "live_ec2_identity_and_tag",
                return_value=(identity, {"key": S.AUTHORIZATION_TAG_KEY,
                                         "value": observed_sha})):
            with self.assertRaises(S.CustodyFault):
                S.load_live_authorization(template_path)


def _write(path: Path, value: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value)


class CgroupAndTerminalTests(unittest.TestCase):
    def _cgroup_fixture(self, directory: Path):
        unit_root = directory / "units"
        cgroup_root = directory / "cgroups"
        unit = "jc2-d43-v3-test.service"
        cgroup_path = "/system.slice/" + unit
        cgroup = cgroup_root / cgroup_path.lstrip("/")
        environment = ["Environment=%s=%s" % item
                       for item in S.SUPERVISOR_REQUIRED_ENV.items()]
        supervisor = directory / "supervisor.py"
        authorization = directory / "authorization.json"
        bash = directory / "bash"
        python = directory / "python"
        for path in (supervisor, authorization, bash, python):
            _write(path, path.name)
        start = [str(python), "-I", "-B", str(supervisor),
                 "--authorization", str(authorization)]
        stop = start + ["--terminalize"]
        fragment_text = "\n".join([
            "[Service]", "Type=exec", "ExecStart=" + " ".join(start),
            "ExecStopPost=" + " ".join(stop),
            "MemoryMax=%d" % S.RSS_LIMIT_BYTES, "MemorySwapMax=0",
            "TasksMax=%d" % S.TASKS_LIMIT,
            "RuntimeMaxSec=%d" % S.TIMEOUT_SECONDS,
            "KillMode=control-group", "Delegate=no", "NoNewPrivileges=yes",
            "PrivateTmp=yes", "SendSIGKILL=yes", "OOMPolicy=stop",
            "MemoryOOMGroup=yes", "TimeoutStopSec=60",
            "ProtectControlGroups=yes", "ProtectKernelTunables=yes",
            "PrivateDevices=yes", "ProtectSystem=strict",
            "ProtectHome=read-only", "RestrictSUIDSGID=yes",
            "LockPersonality=yes", "RestrictNamespaces=yes", "UMask=0077",
            "WorkingDirectory=/", "User=jc2d43", "Group=jc2d43",
            "SetLoginEnvironment=no",
            "UnsetEnvironment=" + " ".join(S.PREEXEC_UNSET_ENVIRONMENT),
            "InaccessiblePaths=/tmp /var/tmp /dev/shm",
            "ReadWritePaths=" + str(directory),
        ] + environment) + "\n"
        fragment = unit_root / unit
        _write(fragment, fragment_text)
        os.chmod(fragment, 0o444)
        values = {
            "memory.max": str(S.RSS_LIMIT_BYTES), "memory.swap.max": "0",
            "pids.max": str(S.TASKS_LIMIT), "cgroup.subtree_control": "",
            "cgroup.type": "domain", "cgroup.procs": str(os.getpid()),
            "pids.current": "1", "pids.events": "max 0",
            "memory.events": (
                "low 0\nhigh 0\nmax 0\noom 0\noom_kill 0\n"
                "oom_group_kill 0"),
        }
        for name, value in values.items():
            _write(cgroup / name, value + "\n")
        os.chmod(cgroup, 0o755)
        systemd = {
            "unit_name": unit, "cgroup_path": cgroup_path,
            "unit_fragment_path": str(fragment),
            "unit_fragment_sha256": S.sha256_path(fragment),
            "exec_start_argv": start, "exec_stop_post_argv": stop,
        }
        runtime = {"python_path": str(python)}
        return systemd, runtime, supervisor, authorization, cgroup_root, unit_root, cgroup

    def _verify(self, fixture):
        systemd, runtime, supervisor, authorization, croot, uroot, _ = fixture
        return S.verify_cgroup_contract(
            systemd, runtime, supervisor, authorization,
            Path(authorization).parent, cgroup_root=croot,
            unit_root=uroot, observed_path_override=systemd["cgroup_path"],
            dropin_roots=[uroot], require_root_owner=False,
            require_dedicated_uid=False)

    def test_systemd_cgroup_contract_and_hostile_mutations(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._cgroup_fixture(Path(directory))
            self.assertEqual(self._verify(fixture)["initial_pids"],
                             [os.getpid()])
            systemd, _runtime, _supervisor, _auth, _cr, uroot, cgroup = fixture
            dropin = uroot / (systemd["unit_name"] + ".d")
            dropin.mkdir()
            with self.assertRaisesRegex(S.CustodyFault, "drop-ins"):
                self._verify(fixture)
            dropin.rmdir()
            fragment = Path(systemd["unit_fragment_path"])
            original_fragment = fragment.read_text()
            os.chmod(fragment, 0o644)
            fragment.write_text(original_fragment + "ExecStartPre=/bin/false\n")
            os.chmod(fragment, 0o444)
            systemd["unit_fragment_sha256"] = S.sha256_path(fragment)
            with self.assertRaisesRegex(S.CustodyFault, "unregistered"):
                self._verify(fixture)
            os.chmod(fragment, 0o644)
            fragment.write_text(original_fragment)
            os.chmod(fragment, 0o444)
            systemd["unit_fragment_sha256"] = S.sha256_path(fragment)
            _write(cgroup / "memory.swap.max", "1\n")
            with self.assertRaisesRegex(S.CustodyFault, "limits"):
                self._verify(fixture)
            _write(cgroup / "memory.swap.max", "0\n")
            _write(cgroup / "cgroup.procs", "%d\n999999\n" % os.getpid())
            _write(cgroup / "pids.current", "2\n")
            with self.assertRaisesRegex(S.CustodyFault, "sole initial"):
                self._verify(fixture)
            _write(cgroup / "cgroup.procs", "%d\n" % os.getpid())
            _write(cgroup / "pids.current", "1\n")
            os.chmod(fragment, 0o644)
            text = fragment.read_text().replace(
                "KillMode=control-group", "KillMode=process")
            fragment.write_text(text)
            os.chmod(fragment, 0o444)
            systemd["unit_fragment_sha256"] = S.sha256_path(fragment)
            with self.assertRaisesRegex(S.CustodyFault, "KillMode"):
                self._verify(fixture)

    def test_cgroup_membership_sees_setsid_doublefork_by_membership(self):
        with tempfile.TemporaryDirectory() as directory:
            cgroup = Path(directory)
            for name, value in {
                    "cgroup.procs": "%d\n999998\n" % os.getpid(),
                    "pids.current": "2\n", "pids.events": "max 0\n",
                    "memory.current": "0\n", "memory.peak": "0\n",
                    "memory.swap.current": "0\n",
                    "memory.events": (
                        "max 0\noom 0\noom_kill 0\n"
                        "oom_group_kill 0\n")}.items():
                _write(cgroup / name, value)
            with mock.patch.object(S, "pid_start_time", return_value=123), \
                    mock.patch.object(
                        S, "processes_for_uid",
                        return_value={os.getpid(), 999998}), \
                    mock.patch.object(S, "meminfo_swap_used_bytes", return_value=0):
                snapshot = S.cgroup_snapshot(cgroup)
            self.assertEqual(snapshot["pids"], [os.getpid(), 999998])

    def test_memory_and_tasks_limit_events_fail_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = self._cgroup_fixture(Path(directory))
            cgroup = fixture[-1]
            _write(cgroup / "memory.events",
                   "low 0\nhigh 0\nmax 1\noom 0\noom_kill 0\n"
                   "oom_group_kill 0\n")
            with self.assertRaisesRegex(S.CustodyFault, "resource-limit"):
                self._verify(fixture)
            _write(cgroup / "memory.events",
                   "low 0\nhigh 0\nmax 0\noom 0\noom_kill 0\n"
                   "oom_group_kill 0\n")
            _write(cgroup / "pids.events", "max 1\n")
            with self.assertRaisesRegex(S.CustodyFault, "resource-limit"):
                self._verify(fixture)

    def test_timeout_swap_oom_and_late_bundle_are_no_verdict(self):
        with self.assertRaisesRegex(S.CustodyFault, "1200-second"):
            S.lifecycle_gate(time.monotonic() - 1)
        with mock.patch.object(S, "meminfo_swap_used_bytes", return_value=1):
            with self.assertRaisesRegex(S.CustodyFault, "swap"):
                S.lifecycle_gate(time.monotonic() + 10)
        with tempfile.TemporaryDirectory() as directory:
            run = Path(directory)
            core = {"status": "FINITE_SOURCE_RESULT_CUSTODY_PASS",
                    "mathematical_outcome": "FINITE_SOURCE_LIFT_ONLY"}
            calls = {"count": 0}
            def late_gate():
                calls["count"] += 1
                if calls["count"] == 5:
                    raise S.CustodyFault("LATE", "x")
            with self.assertRaises(S.CustodyFault):
                S.publish_terminal_bundle(run, core, gate=late_gate)
            self.assertGreaterEqual(calls["count"], 5)
            provisional = (run / "PROVISIONAL_TERMINAL_CORE.json").read_text()
            self.assertNotIn("FINITE_SOURCE_RESULT_CUSTODY_PASS", provisional)
            self.assertIn("PENDING_TERMINAL_CUSTODY_NO_AUTHORITY", provisional)
            terminal = S.emergency_no_verdict(run, core,
                                              S.CustodyFault("LATE", "x"))
            self.assertTrue(terminal["status"].startswith("NO_VERDICT"))
            with self.assertRaises((FileExistsError, S.CustodyFault)):
                S.publish_terminal_bundle(run, core)


class BindingTests(unittest.TestCase):
    def test_live_authorization_change_rejected_at_terminal_gate(self):
        identity = {"instance_id": "i-bound"}
        tag = {"key": S.AUTHORIZATION_TAG_KEY, "value": "a" * 64}
        with mock.patch.object(
                S, "load_live_authorization",
                return_value=({}, identity, tag, "b" * 64)):
            with self.assertRaisesRegex(S.CustodyFault, "changed"):
                S.revalidate_live_authorization(
                    "/root/auth.json", "a" * 64, identity, tag)

    def test_poststop_never_adopts_foreign_run_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            run = parent / "registered-run"
            run.mkdir()
            foreign = run / "TERMINAL.json"
            foreign.write_text(json.dumps({
                "schema": S.TERMINAL_SCHEMA,
                "status": "FINITE_SOURCE_RESULT_CUSTODY_PASS",
                "job_id": "foreign",
            }))
            original = foreign.read_bytes()
            authorization = {
                "bindings": {
                    "job_id": "job-bound", "target_exponent": 16,
                    "lane_tag": S.TARGET_TAGS[16],
                },
                "paths": {
                    "run_dir": str(run),
                    "state_output_path": str(run / "STATE.p16.json"),
                },
            }
            (run / "RUN_OWNERSHIP.json").write_text(json.dumps(
                S.run_ownership_payload(
                    run, authorization, "a" * 64, "d" * 32)))
            identity = {"instance_id": "i-bound"}
            tag = {"key": S.AUTHORIZATION_TAG_KEY, "value": "a" * 64}
            with mock.patch.object(S, "reject_inherited_environment"), \
                    mock.patch.object(
                        S, "registered_invocation_id",
                        return_value="c" * 32), \
                    mock.patch.object(
                        S, "load_live_authorization",
                        return_value=(authorization, identity, tag,
                                      "a" * 64)):
                terminal, code = S.poststop_terminalize("/root/auth.json")
            self.assertEqual(code, 125)
            self.assertEqual(terminal["authority_kind"],
                             "PRE_RUN_REJECTION_SIDECAR")
            self.assertEqual(foreign.read_bytes(), original)
            self.assertTrue((parent /
                ".registered-run.NO_VERDICT.aaaaaaaaaaaaaaaa."
                "cccccccccccccccc.json").is_file())

    def test_snapshot_untrusted_file_binds_one_read(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, snapshot = root / "source", root / "snapshot"
            source.write_bytes(b"semantic bytes")
            digest = S.snapshot_untrusted_file(source, snapshot)
            self.assertEqual(digest, S.sha256_path(snapshot))
            source.write_bytes(b"later mutation")
            self.assertEqual(snapshot.read_bytes(), b"semantic bytes")

    def test_target64_incomplete_provenance_rejected_before_reads(self):
        with tempfile.TemporaryDirectory() as directory:
            paths = {"target16_terminal_path": "/abs/missing",
                     "target16_manifest_path": "/abs/missing",
                     "target16_archive_path": "/abs/missing"}
            with self.assertRaisesRegex(S.CustodyFault, "provenance"):
                S.validate_target16_handoff(paths, {"achieved_exponent": 16},
                                            Path(directory))

    def test_deep_gate_rejects_state_report_history_mismatch(self):
        payload = {
            "schema": S.STATE_SCHEMA, "status": "FINITE_SOURCE_LIFT_ONLY",
            "scope": S.SCOPE, "exponent": 16, "history_sha256": "1" * 64,
            "template_relation_gate": {"pass": True},
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            state = root / "state.json"
            envelope = {"payload": payload,
                        "payload_sha256": S.sha256_json(payload)}
            state.write_text(json.dumps(envelope))
            marker = {"marker": True}
            report = {
                "status": payload["status"], "scope": S.SCOPE,
                "claims_certified": S.CERTIFIED_CLAIM,
                "claims_forbidden": S.FORBIDDEN_CLAIMS,
                "requested_exponent": 16, "achieved_exponent": 16,
                "state_payload_sha256": envelope["payload_sha256"],
                "history_sha256": "2" * 64,
                "necessary_template_relation_gate": {"pass": True},
                "aws_lane": marker, "state_path": str(state.resolve()),
                "source_rows": 184, "essential_coordinates": 182,
                "jacobian_rank_mod_p": 129, "left_cokernel_dimension": 55,
            }
            validation = {
                "status": "SEMANTIC_STATE_CHAIN_VALID", "scope": S.SCOPE,
                "claims_certified": S.CERTIFIED_CLAIM,
                "claims_forbidden": S.FORBIDDEN_CLAIMS,
                "validated_exponent": 16,
                "state_payload_sha256": envelope["payload_sha256"],
                "history_sha256": payload["history_sha256"],
            }
            report_path, validation_path = root / "report.json", root / "v.json"
            report_path.write_text(json.dumps(report))
            validation_path.write_text(json.dumps(validation))
            with self.assertRaisesRegex(S.CustodyFault, "report/state"):
                S._deep_output_gate(report_path, validation_path, state,
                                    marker, 16)


@unittest.skipUnless(os.environ.get("JC2_D43_V3_REAL_FIXTURE") == "1",
                     "real D43 fixture is AWS-review opt-in")
class CorrectRealKernelFixture(unittest.TestCase):
    @staticmethod
    def kernel_for_free_column(context, free_column):
        kernel = [0] * len(context["essential_labels"])
        kernel[free_column] = 1
        for row, pivot in enumerate(context["factor"]["pivot_columns"]):
            kernel[pivot] = -context["factor"]["rref"][row][free_column] \
                % H.PRIME
        direct = [sum(matrix_row[index] * kernel[index]
                      for index in range(len(kernel))) % H.PRIME
                  for matrix_row in context["essential_jacobian"]]
        if any(direct):
            raise AssertionError("constructed digit is not in source kernel")
        return kernel

    def test_deterministic_p2_plus_p_kernel_rejected_semantically(self):
        context = H.prepare_d43_context(
            CASES / "d43_full_certificate_p105337.json",
            CASES / "d43_char0_lift_p105337.json",
            d21_path=ROOT / "directionb_tails_D21.pkl",
            core23_path=CASES / "directionb_core23_p105337.ms",
            execution_root=ROOT)
        initial = H._initial_payload(context)
        deterministic_p2 = H.lift_one_point_digit(context, initial)
        self.assertEqual(deterministic_p2["status"], H.STATUS_FINITE)
        modulus, frame, selected = H.PRIME ** 2, \
            H._frame_from_payload(deterministic_p2), None
        for free_column in context["factor"]["free_columns"]:
            kernel = self.kernel_for_free_column(context, free_column)
            shifted = copy.deepcopy(deterministic_p2)
            for label, digit in zip(context["essential_labels"], kernel):
                key = H.coordinate_key(label)
                shifted["coordinates"][key] = (
                    deterministic_p2["coordinates"][key] + H.PRIME * digit
                ) % modulus
            rows = H.source_rows_with_x(
                context, shifted["coordinates"], frame, modulus)
            self.assertEqual(rows, [0] * 184)
            self.assertTrue(any(
                shifted["coordinates"][key] !=
                deterministic_p2["coordinates"][key]
                for key in shifted["coordinates"]))
            gate = H.template_relation_gate(
                shifted["coordinates"], frame, modulus)
            if gate["pass"]:
                shifted["template_relation_gate"] = gate
                selected = shifted
                break
        self.assertIsNotNone(selected, "registered single-kernel fixture drift")
        with self.assertRaisesRegex(ValueError,
                                   "semantic state-chain replay mismatch"):
            H.validate_resume_payload(selected, context)
        # Isolate the two history-hash attacks on an otherwise completely
        # valid deterministic p2 state; they must not merely rediscover the
        # stale-coordinate rejection above.
        for mutation in ("delete", "change"):
            hostile = copy.deepcopy(deterministic_p2)
            if mutation == "delete":
                del hostile["history"][-1]["coordinate_point_sha256"]
            else:
                hostile["history"][-1]["coordinate_point_sha256"] = "0" * 64
            with self.subTest(mutation=mutation), self.assertRaisesRegex(
                    ValueError, "history|record|semantic"):
                H.validate_resume_payload(hostile, context)


if __name__ == "__main__":
    unittest.main(verbosity=2)
