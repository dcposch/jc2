#!/usr/bin/env python3
"""Regression tests for the launchd-backed external-lane supervisor."""

from __future__ import annotations

import json
import os
from pathlib import Path
import plistlib
import shutil
import subprocess
import sys
import tempfile
import time
import unittest


SOURCE = Path(__file__).resolve().parent / "lane_detach.py"
MATCHER_SOURCE = Path(__file__).resolve().parent / "lane_process_pid.awk"


@unittest.skipUnless(sys.platform == "darwin" and shutil.which("launchctl"), "macOS only")
class LaneDetachIntegrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="jc2-lane-detach-test.")
        # macOS exposes the temporary root through both /var and /private/var.
        # Match the supervisor's canonical script-parent spelling.
        self.root = Path(self.temporary.name).resolve()
        (self.root / "ops" / "adapters").mkdir(parents=True)
        (self.root / "xmodel").mkdir()
        shutil.copy2(SOURCE, self.root / "ops" / "lane_detach.py")
        shutil.copy2(MATCHER_SOURCE, self.root / "ops" / "lane_process_pid.awk")
        (self.root / "ops" / "adapters" / "fake.sh").write_text(
            "#!/bin/sh\nexit 0\n", encoding="utf-8"
        )
        os.chmod(self.root / "ops" / "adapters" / "fake.sh", 0o755)
        (self.root / "ops" / "lane.sh").write_text(
            """#!/bin/sh
set -eu
adapter=$1
tag=$2
prompt=$3
receipt=xmodel/$tag.run.v2
marker=xmodel/$tag.marker
printf 'initial_status=RUNNING\\n' > "$receipt"
chmod 000 "$receipt"
printf 'started %s %s\\n' "$adapter" "$(wc -c < "$prompt" | tr -d ' ')" > "$marker"
case "$tag" in
  *-fail) sleep 1; lane_rc=7 ;;
  *) sleep 2; lane_rc=0 ;;
esac
chmod 600 "$receipt"
printf 'final_status=%s\\nexit_code=%s\\n' "$( [ "$lane_rc" -eq 0 ] && printf DONE || printf FAILED )" "$lane_rc" >> "$receipt"
printf 'finished %s\\n' "$lane_rc" >> "$marker"
exit "$lane_rc"
""",
            encoding="utf-8",
        )
        os.chmod(self.root / "ops" / "lane.sh", 0o755)
        self.prompt = self.root / "prompt.md"
        self.prompt.write_text("bounded fake prompt\n", encoding="utf-8")
        self.loaded_tags: set[str] = set()

    def tearDown(self) -> None:
        for tag in self.loaded_tags:
            record_path = self.root / ".lane-jobs" / tag / "launch.v1.json"
            if not record_path.exists():
                continue
            record = json.loads(record_path.read_text(encoding="utf-8"))
            subprocess.run(
                ["launchctl", "bootout", f"{record['domain']}/{record['label']}"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False,
            )
        self.temporary.cleanup()

    def run_tool(self, *arguments: str, timeout: float = 15) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, os.fspath(self.root / "ops" / "lane_detach.py"), *arguments],
            cwd=self.root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
        )

    def launch(self, tag: str) -> subprocess.CompletedProcess[str]:
        result = self.run_tool("launch", "fake", tag, os.fspath(self.prompt), "--json")
        if result.returncode == 0:
            self.loaded_tags.add(tag)
        return result

    def wait_for_state(self, tag: str, wanted: set[str], timeout: float = 8) -> dict[str, object]:
        deadline = time.monotonic() + timeout
        last: dict[str, object] = {}
        while time.monotonic() < deadline:
            result = self.run_tool("status", tag, "--json")
            self.assertEqual(result.returncode, 0, result.stderr)
            last = json.loads(result.stdout)
            if last["state"] in wanted:
                return last
            time.sleep(0.05)
        self.fail(f"state did not reach {wanted}: {last}")

    def test_survives_launch_client_and_status_never_reads_active_receipt(self) -> None:
        tag = f"detach-{os.getpid()}-ok"
        launched = self.launch(tag)
        self.assertEqual(launched.returncode, 0, launched.stderr)
        # The launch client has already exited.  The launchd-owned lane remains
        # observable even though its active receipt is mode 000.
        active = self.wait_for_state(tag, {"RUNNING"})
        self.assertIsNotNone(active["pid"])
        live_rows = subprocess.run(
            ["pgrep", "-fl", "[o]ps/lane[.]sh"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(live_rows.returncode, 0, live_rows.stderr)
        matched = subprocess.run(
            [
                "awk",
                "-v",
                f"tag={tag}",
                "-f",
                os.fspath(self.root / "ops" / "lane_process_pid.awk"),
            ],
            input=live_rows.stdout,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(matched.returncode, 0, matched.stderr)
        self.assertEqual(matched.stdout.strip(), str(active["pid"]))
        prefix = tag.removesuffix("-ok")
        prefix_match = subprocess.run(
            [
                "awk",
                "-v",
                f"tag={prefix}",
                "-f",
                os.fspath(self.root / "ops" / "lane_process_pid.awk"),
            ],
            input=live_rows.stdout,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(prefix_match.returncode, 0, prefix_match.stderr)
        self.assertEqual(prefix_match.stdout, "")
        status = self.run_tool("status", tag, "--json")
        self.assertEqual(status.returncode, 0, status.stderr)
        terminal = self.run_tool(
            "wait", tag, "--timeout", "8", "--interval", "0.05", "--json", timeout=12
        )
        self.assertEqual(terminal.returncode, 0, terminal.stderr)
        final = json.loads(terminal.stdout)
        self.assertEqual(final["state"], "SUCCEEDED")
        self.assertEqual(final["lane_exit_code"], 0)
        marker = (self.root / "xmodel" / f"{tag}.marker").read_text(encoding="utf-8")
        self.assertIn("finished 0", marker)

        unload = self.run_tool("unload", tag)
        self.assertEqual(unload.returncode, 0, unload.stderr)
        self.loaded_tags.discard(tag)
        retained = self.root / ".lane-jobs" / tag / "launch.v1.json"
        self.assertTrue(retained.exists())

    def test_nonzero_lane_exit_is_terminal_failure(self) -> None:
        tag = f"detach-{os.getpid()}-fail"
        launched = self.launch(tag)
        self.assertEqual(launched.returncode, 0, launched.stderr)
        terminal = self.run_tool(
            "wait", tag, "--timeout", "8", "--interval", "0.05", "--json", timeout=12
        )
        self.assertEqual(terminal.returncode, 1, terminal.stderr)
        final = json.loads(terminal.stdout)
        self.assertEqual(final["state"], "FAILED")
        self.assertEqual(final["lane_exit_code"], 7)

    def test_duplicate_tag_and_symlink_prompt_fail_closed(self) -> None:
        tag = f"detach-{os.getpid()}-duplicate"
        first = self.launch(tag)
        self.assertEqual(first.returncode, 0, first.stderr)
        second = self.launch(tag)
        self.assertNotEqual(second.returncode, 0)
        self.assertIn("duplicate tag", second.stderr)

        symlink_prompt = self.root / "prompt-link.md"
        symlink_prompt.symlink_to(self.prompt)
        rejected = self.run_tool(
            "launch", "fake", f"detach-{os.getpid()}-symlink", os.fspath(symlink_prompt)
        )
        self.assertNotEqual(rejected.returncode, 0)
        self.assertIn("path component must not be a symlink", rejected.stderr)

    def test_intermediate_symlink_is_rejected_without_reaching_target(self) -> None:
        # The target intentionally does not exist.  A component-wise lstat
        # walk must reject `link` itself before looking up link/prompt.md.
        intermediate = self.root / "link"
        intermediate.symlink_to(self.root / "jc2-lean")
        rejected = self.run_tool(
            "launch",
            "fake",
            f"detach-{os.getpid()}-intermediate-link",
            os.fspath(intermediate / "prompt.md"),
        )
        self.assertNotEqual(rejected.returncode, 0)
        self.assertIn("path component must not be a symlink", rejected.stderr)

    def test_plist_is_one_shot_and_sidecar_hashes_it(self) -> None:
        tag = f"detach-{os.getpid()}-plist"
        launched = self.launch(tag)
        self.assertEqual(launched.returncode, 0, launched.stderr)
        directory = self.root / ".lane-jobs" / tag
        record = json.loads((directory / "launch.v1.json").read_text(encoding="utf-8"))
        with (directory / "job.plist").open("rb") as handle:
            job = plistlib.load(handle)
        self.assertIs(job["KeepAlive"], False)
        self.assertIs(job["RunAtLoad"], True)
        self.assertEqual(job["ProgramArguments"][1], os.fspath(self.root / "ops" / "lane.sh"))
        self.assertNotIn("ANTHROPIC_API_KEY", job["EnvironmentVariables"])
        import hashlib

        self.assertEqual(
            record["plist_sha256"], hashlib.sha256((directory / "job.plist").read_bytes()).hexdigest()
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
