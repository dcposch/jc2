#!/usr/bin/env python3
"""Focused light regression suite for CAPRUN/v1."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest

import run_capped as caprun

try:
    import resource as _resource
except ImportError:
    _resource = None


RUNNER = Path(__file__).with_name("run_capped.py")
PS = Path("/bin/ps") if Path("/bin/ps").exists() else Path("/usr/bin/ps")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def process_is_live_non_zombie(pid: int) -> bool:
    result = subprocess.run(
        [str(PS), "-o", "state=", "-p", str(pid)],
        check=False,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=2,
    )
    state = result.stdout.strip()
    return bool(state) and not state.startswith("Z")


def wait_not_live(pid: int, seconds: float = 2.0) -> bool:
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        if not process_is_live_non_zombie(pid):
            return True
        time.sleep(0.02)
    return not process_is_live_non_zombie(pid)


def cleanup_test_sleep_marker(marker: Path) -> None:
    """Best-effort exact-PID cleanup if a descendant regression aborts a test."""

    if not marker.exists():
        return
    try:
        pid = int(marker.read_text(encoding="ascii").strip())
    except (OSError, ValueError):
        return
    observed = subprocess.run(
        [str(PS), "-o", "command=", "-p", str(pid)],
        check=False,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=2,
    ).stdout
    if "time.sleep(30)" not in observed:
        return
    try:
        os.kill(pid, signal.SIGKILL)
    except ProcessLookupError:
        return
    wait_not_live(pid)


class CapRunTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(prefix="caprun-test-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.counter = 0

    def run_cap(
        self,
        child_argv,
        *,
        wall: float = 2.0,
        grace: float = 0.15,
        stdin_file: Path = None,
        extra_options=(),
    ):
        self.counter += 1
        prefix = self.root / ("run-%02d" % self.counter)
        stdout_path = Path(str(prefix) + ".stdout")
        stderr_path = Path(str(prefix) + ".stderr")
        telemetry_path = Path(str(prefix) + ".json")
        argv = [
            sys.executable,
            str(RUNNER),
            "--wall-seconds",
            str(wall),
            "--term-grace-seconds",
            str(grace),
            "--stdout-file",
            str(stdout_path),
            "--stderr-file",
            str(stderr_path),
            "--telemetry-file",
            str(telemetry_path),
        ]
        if stdin_file is not None:
            argv.extend(["--stdin-file", str(stdin_file)])
        argv.extend(extra_options)
        argv.append("--")
        argv.extend(child_argv)
        started = time.monotonic()
        result = subprocess.run(
            argv,
            check=False,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=wall + grace + 5.0,
        )
        elapsed = time.monotonic() - started
        telemetry = json.loads(telemetry_path.read_text(encoding="utf-8"))
        return result, telemetry, stdout_path, stderr_path, elapsed

    def test_devnull_delivers_eof_promptly(self) -> None:
        code = (
            "import sys; data=sys.stdin.buffer.read(); "
            "print('EOF:%d' % len(data), flush=True)"
        )
        result, telemetry, stdout_path, _, elapsed = self.run_cap(
            [sys.executable, "-c", code], wall=1.0
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertLess(elapsed, 0.5)
        self.assertEqual(stdout_path.read_bytes(), b"EOF:0\n")
        self.assertEqual(telemetry["stdin"]["mode"], "devnull")
        self.assertEqual(telemetry["status"], "NORMAL_EXIT")

    def test_regular_stdin_file_is_explicit(self) -> None:
        input_path = self.root / "input.txt"
        input_path.write_bytes(b"literal input\n")
        code = "import sys; sys.stdout.buffer.write(sys.stdin.buffer.read())"
        result, telemetry, stdout_path, _, _ = self.run_cap(
            [sys.executable, "-c", code], stdin_file=input_path
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(stdout_path.read_bytes(), input_path.read_bytes())
        self.assertEqual(telemetry["stdin"]["mode"], "regular_file")
        self.assertEqual(telemetry["stdin"]["path"], str(input_path))

    def test_stdout_stderr_exit_status_and_hashes(self) -> None:
        code = (
            "import sys; sys.stdout.write('out\\n'); sys.stdout.flush(); "
            "sys.stderr.write('err\\n'); sys.stderr.flush(); raise SystemExit(7)"
        )
        result, telemetry, stdout_path, stderr_path, _ = self.run_cap(
            [sys.executable, "-c", code]
        )
        self.assertEqual(result.returncode, 7, result.stderr)
        self.assertEqual(telemetry["status"], "NORMAL_EXIT")
        self.assertEqual(telemetry["child_exit_code"], 7)
        self.assertEqual(stdout_path.read_bytes(), b"out\n")
        self.assertEqual(stderr_path.read_bytes(), b"err\n")
        self.assertEqual(telemetry["stdout"]["sha256"], digest(b"out\n"))
        self.assertEqual(telemetry["stderr"]["sha256"], digest(b"err\n"))
        self.assertEqual(telemetry["pid"], telemetry["pgid"])
        self.assertTrue(telemetry["start_identity"])
        self.assertTrue(telemetry["argv_sha256"])

    def test_early_exit_is_authoritative(self) -> None:
        result, telemetry, _, _, elapsed = self.run_cap(
            [sys.executable, "-c", "raise SystemExit(23)"], wall=0.5
        )
        self.assertEqual(result.returncode, 23, result.stderr)
        self.assertEqual(telemetry["status"], "NORMAL_EXIT")
        self.assertEqual(telemetry["child_returncode"], 23)
        self.assertLess(elapsed, 0.5)

    def test_timeout_cleans_child_and_grandchild(self) -> None:
        marker = self.root / "grandchild.pid"
        self.addCleanup(cleanup_test_sleep_marker, marker)
        code = """
import pathlib, subprocess, sys, time
grand = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(30)'])
pathlib.Path(sys.argv[1]).write_text(str(grand.pid), encoding='ascii')
print('ready', flush=True)
time.sleep(30)
"""
        result, telemetry, stdout_path, _, _ = self.run_cap(
            [sys.executable, "-c", code, str(marker)], wall=0.3
        )
        self.assertEqual(result.returncode, 124, result.stderr)
        self.assertEqual(telemetry["status"], "WALL_TIMEOUT")
        self.assertEqual(telemetry["termination"]["reason"], "wall_timeout")
        self.assertTrue(telemetry["termination"]["term_sent"])
        self.assertEqual(stdout_path.read_bytes(), b"ready\n")
        grandchild_pid = int(marker.read_text(encoding="ascii"))
        self.assertTrue(wait_not_live(grandchild_pid))

    def test_exited_leader_cannot_orphan_same_group_descendant(self) -> None:
        marker = self.root / "orphan-resistant-grandchild.pid"
        self.addCleanup(cleanup_test_sleep_marker, marker)
        grandchild = (
            "import signal,time; "
            "signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(30)"
        )
        code = """
import pathlib, subprocess, sys
grand = subprocess.Popen([sys.executable, '-c', sys.argv[2]])
pathlib.Path(sys.argv[1]).write_text(str(grand.pid), encoding='ascii')
raise SystemExit(0)
"""
        result, telemetry, _, _, elapsed = self.run_cap(
            [sys.executable, "-c", code, str(marker), grandchild],
            wall=0.3,
            grace=0.1,
        )
        self.assertEqual(result.returncode, 124, result.stderr)
        self.assertGreaterEqual(elapsed, 0.25)
        self.assertEqual(telemetry["status"], "WALL_TIMEOUT")
        self.assertEqual(telemetry["child_returncode"], 0)
        self.assertTrue(telemetry["termination"]["term_sent"])
        self.assertTrue(telemetry["termination"]["kill_sent"])
        stages = [item["stage"] for item in telemetry["identity_checks"]]
        self.assertIn("before-term", stages)
        self.assertIn("before-kill", stages)
        grandchild_pid = int(marker.read_text(encoding="ascii"))
        self.assertTrue(wait_not_live(grandchild_pid))

    def test_term_ignoring_group_reaches_validated_kill(self) -> None:
        marker = self.root / "ignoring-grandchild.pid"
        self.addCleanup(cleanup_test_sleep_marker, marker)
        grandchild = (
            "import signal,time; "
            "signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(30)"
        )
        code = """
import pathlib, signal, subprocess, sys, time
signal.signal(signal.SIGTERM, signal.SIG_IGN)
grand = subprocess.Popen([sys.executable, '-c', sys.argv[2]])
pathlib.Path(sys.argv[1]).write_text(str(grand.pid), encoding='ascii')
print('ignoring', flush=True)
time.sleep(30)
"""
        result, telemetry, _, _, _ = self.run_cap(
            [sys.executable, "-c", code, str(marker), grandchild],
            wall=0.25,
            grace=0.1,
        )
        self.assertEqual(result.returncode, 124, result.stderr)
        self.assertEqual(telemetry["child_signal"], signal.SIGKILL)
        self.assertTrue(telemetry["termination"]["term_sent"])
        self.assertTrue(telemetry["termination"]["kill_sent"])
        stages = [item["stage"] for item in telemetry["identity_checks"]]
        self.assertIn("before-term", stages)
        self.assertIn("before-kill", stages)
        grandchild_pid = int(marker.read_text(encoding="ascii"))
        self.assertTrue(wait_not_live(grandchild_pid))

    def test_dead_term_leader_remains_identity_anchor_for_grandchild_kill(self) -> None:
        marker = self.root / "term-dead-leader-grandchild.pid"
        self.addCleanup(cleanup_test_sleep_marker, marker)
        grandchild = (
            "import signal,time; "
            "signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(30)"
        )
        code = """
import pathlib, subprocess, sys, time
grand = subprocess.Popen([sys.executable, '-c', sys.argv[2]])
pathlib.Path(sys.argv[1]).write_text(str(grand.pid), encoding='ascii')
time.sleep(30)
"""
        result, telemetry, _, _, _ = self.run_cap(
            [sys.executable, "-c", code, str(marker), grandchild],
            wall=0.25,
            grace=0.1,
        )
        self.assertEqual(result.returncode, 124, result.stderr)
        self.assertEqual(telemetry["child_signal"], signal.SIGTERM)
        self.assertTrue(telemetry["termination"]["term_sent"])
        self.assertTrue(telemetry["termination"]["kill_sent"])
        checks = {
            item["stage"]: item["result"]
            for item in telemetry["identity_checks"]
            if item["stage"] in ("before-term", "before-kill")
        }
        self.assertEqual(checks["before-term"], "MATCH")
        self.assertEqual(checks["before-kill"], "MATCH")
        grandchild_pid = int(marker.read_text(encoding="ascii"))
        self.assertTrue(wait_not_live(grandchild_pid))

    @unittest.skipUnless(os.name == "posix", "SIGCHLD inheritance is POSIX")
    def test_inherited_sigchld_ignore_is_reset_for_zombie_anchor(self) -> None:
        prefix = self.root / "sigchld-ignore"
        stdout_path = Path(str(prefix) + ".stdout")
        stderr_path = Path(str(prefix) + ".stderr")
        telemetry_path = Path(str(prefix) + ".json")
        marker = self.root / "sigchld-grandchild.pid"
        self.addCleanup(cleanup_test_sleep_marker, marker)
        grandchild = (
            "import signal,time; "
            "signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(30)"
        )
        child = """
import pathlib, subprocess, sys
grand = subprocess.Popen([sys.executable, '-c', sys.argv[2]])
pathlib.Path(sys.argv[1]).write_text(str(grand.pid), encoding='ascii')
raise SystemExit(0)
"""
        wrapper = (
            "import os,signal,sys; "
            "signal.signal(signal.SIGCHLD, signal.SIG_IGN); "
            "os.execv(sys.executable, [sys.executable, sys.argv[1]] + sys.argv[2:])"
        )
        result = subprocess.run(
            [
                sys.executable,
                "-c",
                wrapper,
                str(RUNNER),
                "--wall-seconds",
                "0.3",
                "--term-grace-seconds",
                "0.1",
                "--stdout-file",
                str(stdout_path),
                "--stderr-file",
                str(stderr_path),
                "--telemetry-file",
                str(telemetry_path),
                "--",
                sys.executable,
                "-c",
                child,
                str(marker),
                grandchild,
            ],
            check=False,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=3,
        )
        self.assertEqual(result.returncode, 124, result.stderr)
        telemetry = json.loads(telemetry_path.read_text(encoding="utf-8"))
        self.assertEqual(telemetry["status"], "WALL_TIMEOUT")
        self.assertEqual(telemetry["child_returncode"], 0)
        self.assertTrue(telemetry["termination"]["kill_sent"])
        grandchild_pid = int(marker.read_text(encoding="ascii"))
        self.assertTrue(wait_not_live(grandchild_pid))

    def test_decoy_same_executable_survives_and_source_has_no_broad_kill(self) -> None:
        decoy = subprocess.Popen(
            [sys.executable, "-c", "import time; time.sleep(30)"],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )

        def clean_decoy() -> None:
            if decoy.poll() is None:
                decoy.terminate()
                try:
                    decoy.wait(timeout=2)
                except subprocess.TimeoutExpired:
                    decoy.kill()
                    decoy.wait(timeout=2)

        self.addCleanup(clean_decoy)
        result, telemetry, _, _, _ = self.run_cap(
            [sys.executable, "-c", "import time; time.sleep(30)"], wall=0.2
        )
        self.assertEqual(result.returncode, 124, result.stderr)
        self.assertEqual(telemetry["status"], "WALL_TIMEOUT")
        self.assertIsNone(decoy.poll(), "same-executable decoy was signalled")

        source = RUNNER.read_text(encoding="utf-8")
        forbidden = (
            "".join(("kill", " -0")),
            "".join(("p", "grep")),
            "".join(("p", "kill")),
            "".join(("os", ".system")),
            "".join(("shell", "=True")),
        )
        for pattern in forbidden:
            with self.subTest(pattern=pattern):
                self.assertNotIn(pattern, source)

    def test_spawn_failure_is_typed_and_outputs_are_hashed(self) -> None:
        missing = str(self.root / "definitely-not-an-executable")
        result, telemetry, _, _, _ = self.run_cap([missing])
        self.assertEqual(result.returncode, 70, result.stderr)
        self.assertEqual(telemetry["status"], "RUNNER_FAILURE")
        self.assertIn("FileNotFoundError", telemetry["error"])
        self.assertEqual(telemetry["stdout"]["bytes"], 0)
        self.assertEqual(telemetry["stderr"]["bytes"], 0)

    def test_overwrite_hardlink_collision_preserves_input(self) -> None:
        original = b"must survive validation\n"
        for alias_name in ("stdout", "stderr", "telemetry"):
            with self.subTest(alias=alias_name):
                root = self.root / alias_name
                root.mkdir()
                input_path = root / "preserve-input.txt"
                paths = {
                    "stdout": root / "run.stdout",
                    "stderr": root / "run.stderr",
                    "telemetry": root / "run.json",
                }
                marker = root / "child-started"
                input_path.write_bytes(original)
                os.link(input_path, paths[alias_name])
                result = subprocess.run(
                    [
                        sys.executable,
                        str(RUNNER),
                        "--wall-seconds",
                        "1",
                        "--stdin-file",
                        str(input_path),
                        "--stdout-file",
                        str(paths["stdout"]),
                        "--stderr-file",
                        str(paths["stderr"]),
                        "--telemetry-file",
                        str(paths["telemetry"]),
                        "--overwrite",
                        "--",
                        sys.executable,
                        "-c",
                        "import pathlib,sys; pathlib.Path(sys.argv[1]).touch()",
                        str(marker),
                    ],
                    check=False,
                    stdin=subprocess.DEVNULL,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    timeout=2,
                )
                self.assertEqual(result.returncode, 70)
                self.assertEqual(input_path.read_bytes(), original)
                self.assertEqual(paths[alias_name].read_bytes(), original)
                self.assertFalse(marker.exists())

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFO requires POSIX")
    def test_fifo_output_fails_before_wall_without_starting_child(self) -> None:
        stdout_path = self.root / "blocked.fifo"
        stderr_path = self.root / "fifo.stderr"
        telemetry_path = self.root / "fifo.json"
        marker = self.root / "fifo-child-started"
        os.mkfifo(stdout_path)
        started = time.monotonic()
        result = subprocess.run(
            [
                sys.executable,
                str(RUNNER),
                "--wall-seconds",
                "0.1",
                "--stdout-file",
                str(stdout_path),
                "--stderr-file",
                str(stderr_path),
                "--telemetry-file",
                str(telemetry_path),
                "--overwrite",
                "--",
                sys.executable,
                "-c",
                "import pathlib,sys; pathlib.Path(sys.argv[1]).touch()",
                str(marker),
            ],
            check=False,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=0.8,
        )
        elapsed = time.monotonic() - started
        self.assertEqual(result.returncode, 70)
        self.assertLess(elapsed, 0.5)
        self.assertFalse(marker.exists())

    def test_runner_signal_is_typed_and_forwarded_to_validated_group(self) -> None:
        prefix = self.root / "forwarded"
        stdout_path = Path(str(prefix) + ".stdout")
        stderr_path = Path(str(prefix) + ".stderr")
        telemetry_path = Path(str(prefix) + ".json")
        runner = subprocess.Popen(
            [
                sys.executable,
                str(RUNNER),
                "--wall-seconds",
                "5",
                "--term-grace-seconds",
                "0.1",
                "--stdout-file",
                str(stdout_path),
                "--stderr-file",
                str(stderr_path),
                "--telemetry-file",
                str(telemetry_path),
                "--",
                sys.executable,
                "-c",
                "import time; print('ready', flush=True); time.sleep(30)",
            ],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        deadline = time.monotonic() + 2.0
        while time.monotonic() < deadline:
            if stdout_path.exists() and stdout_path.read_bytes() == b"ready\n":
                break
            time.sleep(0.01)
        else:
            runner.kill()
            runner.wait(timeout=2)
            self.fail("child did not become ready for forwarding test")
        runner.send_signal(signal.SIGTERM)
        runner_stdout, runner_stderr = runner.communicate(timeout=3)
        self.assertEqual(runner.returncode, 128 + signal.SIGTERM, runner_stderr)
        telemetry = json.loads(telemetry_path.read_text(encoding="utf-8"))
        self.assertEqual(telemetry["status"], "SIGNAL")
        self.assertEqual(telemetry["runner_signal"], signal.SIGTERM)
        self.assertEqual(telemetry["termination"]["reason"], "forwarded_signal")
        self.assertTrue(telemetry["termination"]["term_sent"])
        self.assertIn("status=SIGNAL", runner_stdout)

    def test_signal_during_popen_is_latched_until_handle_assignment(self) -> None:
        prefix = self.root / "popen-latch"
        stdout_path = Path(str(prefix) + ".stdout")
        stderr_path = Path(str(prefix) + ".stderr")
        telemetry_path = Path(str(prefix) + ".json")
        parsed = caprun.parser().parse_args(
            [
                "--wall-seconds",
                "2",
                "--term-grace-seconds",
                "0.1",
                "--stdout-file",
                str(stdout_path),
                "--stderr-file",
                str(stderr_path),
                "--telemetry-file",
                str(telemetry_path),
                "--",
                sys.executable,
                "-c",
                "import time; time.sleep(30)",
            ]
        )
        command = list(parsed.command)
        if command and command[0] == "--":
            command = command[1:]

        original_popen = caprun.subprocess.Popen
        fired = [False]

        def signal_once_then_spawn(*args, **kwargs):
            if not fired[0]:
                fired[0] = True
                os.kill(os.getpid(), signal.SIGTERM)
            return original_popen(*args, **kwargs)

        caprun.subprocess.Popen = signal_once_then_spawn
        try:
            returncode = caprun.execute(parsed, command)
        finally:
            caprun.subprocess.Popen = original_popen

        self.assertTrue(fired[0])
        self.assertEqual(returncode, 128 + signal.SIGTERM)
        telemetry = json.loads(telemetry_path.read_text(encoding="utf-8"))
        self.assertEqual(telemetry["status"], "SIGNAL")
        self.assertEqual(telemetry["runner_signal"], signal.SIGTERM)
        self.assertTrue(telemetry["termination"]["term_sent"])
        self.assertTrue(wait_not_live(telemetry["pid"]))

    @unittest.skipUnless(
        os.name == "posix"
        and _resource is not None
        and hasattr(_resource, "RLIMIT_CPU")
        and hasattr(signal, "SIGXCPU"),
        "detectable RLIMIT_CPU/SIGXCPU requires POSIX support",
    )
    def test_cpu_cap_is_typed_only_on_sigxcpu(self) -> None:
        result, telemetry, _, _, _ = self.run_cap(
            [sys.executable, "-c", "while True: pass"],
            wall=4.0,
            extra_options=("--cpu-seconds", "1"),
        )
        self.assertEqual(result.returncode, 125, result.stderr)
        self.assertEqual(telemetry["status"], "RESOURCE_CAP")
        self.assertEqual(telemetry["resource"], "cpu")
        self.assertEqual(telemetry["child_signal"], signal.SIGXCPU)

    @unittest.skipUnless(os.name == "posix" and PS.exists(), "ps RSS required")
    def test_sampled_exact_group_rss_cap_is_typed(self) -> None:
        code = "import time; x=bytearray(80000000); print(len(x)); time.sleep(4)"
        result, telemetry, _, _, _ = self.run_cap(
            [sys.executable, "-c", code],
            wall=4.0,
            extra_options=(
                "--rss-bytes",
                "25000000",
                "--rss-sample-seconds",
                "0.02",
            ),
        )
        self.assertEqual(result.returncode, 125, result.stderr)
        self.assertEqual(telemetry["status"], "RESOURCE_CAP")
        self.assertEqual(telemetry["resource"], "rss")
        self.assertGreater(telemetry["max_observed_group_rss_bytes"], 25000000)


if __name__ == "__main__":
    unittest.main()
