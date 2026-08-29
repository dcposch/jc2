#!/usr/bin/env python3
"""Prove the registered single-PGID containment model with a dummy tree."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path


HERE = Path(__file__).resolve().parent
GUARD = HERE / "process_group_guard.py"
DUMMY = HERE / "dummy_process_tree.py"


def run_json(command):
    completed = subprocess.run(command, check=True, text=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return json.loads(completed.stdout)


def matching_marker_processes(marker):
    matches = []
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit():
            continue
        try:
            command = (entry / "cmdline").read_bytes().replace(b"\0", b" ").decode(
                errors="replace")
        except (FileNotFoundError, PermissionError):
            continue
        if marker in command:
            matches.append(int(entry.name))
    return sorted(matches)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--keep-temp", action="store_true")
    arguments = parser.parse_args()
    assert sys.platform.startswith("linux") and Path("/proc").is_dir()
    temporary = Path(tempfile.mkdtemp(prefix="jc2-pgid-regression-"))
    marker = str(temporary.resolve())
    process = subprocess.Popen([
        sys.executable, str(DUMMY), "--marker", marker, "--depth", "2",
    ], start_new_session=True)
    try:
        assert process.pid == os.getpgid(process.pid)
        time.sleep(1)
        stat_text = Path(f"/proc/{process.pid}/stat").read_text()
        suffix = stat_text[stat_text.rfind(")") + 2:].split()
        starttime = int(suffix[19])
        registry = temporary / "groups.tsv"
        registry.write_text(
            f"dummy\t{process.pid}\t{process.pid}\t{starttime}\t{marker}\t"
            f"{'0' * 64}\n")
        before = run_json([
            sys.executable, str(GUARD), "snapshot", "--registry", str(registry),
        ])
        group = before["groups"][0]
        assert group["validated"]
        assert group["member_count"] >= 3
        assert group["group_rss_kib"] > group["leader_rss_kib"] + 8 * 1024
        stopped = run_json([
            sys.executable, str(GUARD), "stop", "--registry", str(registry),
            "--grace-seconds", "2",
        ])
        assert stopped["status"] == "STOP_VALIDATED"
        assert len(stopped["events"]) == 1
        event = stopped["events"][0]
        assert event["validated"] and event["term_sent"] and not event["remaining"]
        process.wait(timeout=5)
        time.sleep(0.2)
        after = run_json([
            sys.executable, str(GUARD), "snapshot", "--registry", str(registry),
        ])
        assert after["groups"][0]["member_count"] == 0
        assert not matching_marker_processes(marker)
        print(json.dumps({
            "status": "PROCESS_GROUP_REGRESSION=PASS",
            "actual_descendant_rss_included": True,
            "member_count_before_stop": group["member_count"],
            "group_rss_kib_before_stop": group["group_rss_kib"],
            "leader_rss_kib_before_stop": group["leader_rss_kib"],
            "term_to_validated_pgid_only": True,
            "kill_escalation_used": event["kill_sent"],
            "matching_namespace_processes_after": [],
            "unvalidated_pid_or_pgid_signalled": False,
        }, sort_keys=True))
    finally:
        if process.poll() is None:
            try:
                os.killpg(process.pid, 9)
            except ProcessLookupError:
                pass
        if arguments.keep_temp:
            print(f"kept_temp={temporary}")
        else:
            shutil.rmtree(temporary)


if __name__ == "__main__":
    main()
