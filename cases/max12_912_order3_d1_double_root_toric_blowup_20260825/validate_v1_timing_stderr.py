#!/usr/bin/env python3
"""AWS-only fail-closed adjudicator for the frozen v1 timing/stderr mixup."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import re


class CustodyFailure(RuntimeError):
    pass


TIME_KEYS = (
    "Command being timed: ",
    "User time (seconds): ",
    "System time (seconds): ",
    "Percent of CPU this job got: ",
    "Elapsed (wall clock) time (h:mm:ss or m:ss): ",
    "Average shared text size (kbytes): ",
    "Average unshared data size (kbytes): ",
    "Average stack size (kbytes): ",
    "Average total size (kbytes): ",
    "Maximum resident set size (kbytes): ",
    "Average resident set size (kbytes): ",
    "Major (requiring I/O) page faults: ",
    "Minor (reclaiming a frame) page faults: ",
    "Voluntary context switches: ",
    "Involuntary context switches: ",
    "Swaps: ",
    "File system inputs: ",
    "File system outputs: ",
    "Socket messages sent: ",
    "Socket messages received: ",
    "Signals delivered: ",
    "Page size (bytes): ",
    "Exit status: ",
)


def require_aws(tag: str) -> None:
    if platform.system() != "Linux":
        raise CustodyFailure("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise CustodyFailure("REFUSE_NON_AWS_EC2")
    if os.environ.get("JC2_AWS_TAG") != tag:
        raise CustodyFailure("REFUSE_TAG_MISMATCH")
    if not tag.startswith("max12_912_order3_d1_double_root_toric_"):
        raise CustodyFailure("REFUSE_UNREGISTERED_TAG")


def parse_time_only(text: str, expected_input: str) -> dict[str, str]:
    lines = [line.strip() for line in text.splitlines()]
    if len(lines) != len(TIME_KEYS):
        raise CustodyFailure(("timing line count", len(lines)))
    values = {}
    for line, key in zip(lines, TIME_KEYS):
        if not line.startswith(key):
            raise CustodyFailure(("timing key/order", key, line))
        values[key] = line[len(key):]
    expected_command = f'"/usr/bin/Singular -q {expected_input}"'
    if values[TIME_KEYS[0]] != expected_command:
        raise CustodyFailure(("command", values[TIME_KEYS[0]], expected_command))
    if values[TIME_KEYS[-1]] != "0":
        raise CustodyFailure(("time exit", values[TIME_KEYS[-1]]))
    if not re.fullmatch(r"[0-9]+(?:\.[0-9]+)?", values[TIME_KEYS[1]]):
        raise CustodyFailure("user time format")
    if not re.fullmatch(r"[0-9]+(?:\.[0-9]+)?", values[TIME_KEYS[2]]):
        raise CustodyFailure("system time format")
    if not re.fullmatch(r"[0-9]+%", values[TIME_KEYS[3]]):
        raise CustodyFailure("cpu format")
    if not re.fullmatch(r"[0-9]+(?::[0-9]+)+(?:\.[0-9]+)?", values[TIME_KEYS[4]]):
        raise CustodyFailure("elapsed format")
    for key in TIME_KEYS[5:-1]:
        if not re.fullmatch(r"[0-9]+", values[key]):
            raise CustodyFailure(("integer timing format", key, values[key]))
    return values


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def exactly_one(text: str, marker: str) -> bool:
    return sum(line == marker for line in text.splitlines()) == 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--job", required=True)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--encoding", choices=("A", "B"), required=True)
    args = parser.parse_args()
    require_aws(args.tag)
    job = Path(args.job).resolve()
    expected_job = Path("/home/ubuntu/jobs") / args.tag
    if job != expected_job:
        raise CustodyFailure(("job", str(job), str(expected_job)))

    if args.encoding == "A":
        input_name = "compiled/toric_A_factored_sat_dp.sing"
        marker = "PASS_D1_DOUBLE_ROOT_TORIC_A"
    else:
        input_name = "compiled/toric_B_expanded_inverse_lpdp.sing"
        marker = "PASS_D1_DOUBLE_ROOT_TORIC_B"

    required = (
        "compiler.rc", "compiler.stderr", "compile_source.check",
        "solve_source.check", input_name, "singular.rc", "singular.stdout",
        "singular.stderr",
    )
    for name in required:
        if not (job / name).is_file():
            raise CustodyFailure(("missing", name))
    if (job / "compiler.rc").read_text().strip() != "0":
        raise CustodyFailure("compiler rc")
    if (job / "compiler.stderr").read_bytes():
        raise CustodyFailure("compiler stderr")
    if (job / "singular.rc").read_text().strip() != "0":
        raise CustodyFailure("singular rc")
    for check_name in ("compile_source.check", "solve_source.check"):
        check_lines = (job / check_name).read_text().splitlines()
        if not check_lines or any(not line.endswith(": OK") for line in check_lines):
            raise CustodyFailure(("source check", check_name))

    stdout = (job / "singular.stdout").read_text()
    if not exactly_one(stdout, marker):
        raise CustodyFailure("PASS marker")
    if "FAIL_" in stdout:
        raise CustodyFailure("FAIL marker")
    verdicts = re.findall(r"^D1_DOUBLE_ROOT_TORIC_H_IS_UNIT=([01])$", stdout, re.M)
    if len(verdicts) != 1:
        raise CustodyFailure(("verdict count", verdicts))

    timing = (job / "singular.stderr").read_text()
    parse_time_only(timing, input_name)
    # Exact negative controls for the parser itself.
    try:
        parse_time_only(timing + "\nCAS_ERROR", input_name)
    except CustodyFailure:
        pass
    else:
        raise CustodyFailure("parser accepted extra CAS stderr")
    bad_exit = timing.rsplit("Exit status: 0", 1)[0] + "Exit status: 1\n"
    try:
        parse_time_only(bad_exit, input_name)
    except CustodyFailure:
        pass
    else:
        raise CustodyFailure("parser accepted bad exit")

    payload = {
        "tag": args.tag,
        "job": str(job),
        "encoding": args.encoding,
        "input_sha256": digest(job / input_name),
        "stdout_sha256": digest(job / "singular.stdout"),
        "timing_stderr_sha256": digest(job / "singular.stderr"),
        "unit_verdict": int(verdicts[0]),
        "adjudication": (
            "v1 singular.stderr consists exactly of the ordered 23-line GNU "
            "time block; logical CAS stderr is empty"
        ),
    }
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS_D1_DOUBLE_ROOT_TORIC_V1_TIMING_CUSTODY_REPAIR")


if __name__ == "__main__":
    main()

