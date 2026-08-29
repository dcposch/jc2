#!/usr/bin/env python3
"""Static and AWS fail-closed preflight for the frozen sign target."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path


HERE = Path(__file__).resolve().parent
TARGET = HERE / "sign_branch_elimination_target.json"
BUILDER = HERE / "build_target.py"
RENDERER = HERE / "render_singular.py"
VALIDATOR = HERE / "validate_point.py"
TARGET_SHA256 = "3ba44de18e8ce15f9675734319d4dee2cee8cc795b796292a0d40838a6bda072"
SINGULAR_SHA256 = "90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_builder():
    specification = importlib.util.spec_from_file_location("sign_target_builder", BUILDER)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


def parse_branches(target, mode, encoded):
    if encoded == "all":
        assert mode == "modular", "exact-unit forbids all; use an explicit ordered subset"
        return list(target["branch_order"])
    branches = encoded.split(",")
    assert branches and all(branches) and len(set(branches)) == len(branches)
    assert all(branch in target["branch_order"] for branch in branches)
    return branches


def static_preflight():
    assert digest(TARGET) == TARGET_SHA256
    target = json.loads(TARGET.read_text())
    calculated = load_builder().calculate_target()
    assert calculated == target
    assert target["branch_order"] == [
        "+---", "+--+", "+-+-", "+-++", "++--", "++-+", "+++-", "++++", "J0"
    ]
    with tempfile.TemporaryDirectory(prefix="jc2-sign-static-") as temporary:
        temporary = Path(temporary)
        for branch in target["branch_order"]:
            for field in ("mod", "q"):
                output = temporary / f"{branch.replace('+', 'p').replace('-', 'm')}.{field}.sing"
                subprocess.run([
                    sys.executable, str(RENDERER), "--target", str(TARGET),
                    "--branch", branch, "--field", field, "--output", str(output),
                ], check=True)
                rendered = output.read_text()
                assert f"BRANCH={branch}" in rendered
                assert f"target_sha256={TARGET_SHA256}" in rendered
        for branch in ("++++", "J0"):
            completed = subprocess.run([
                sys.executable, str(VALIDATOR), "--target", str(TARGET),
                "--branch", branch, "--use-frozen-seed",
            ], check=True, text=True, stdout=subprocess.PIPE)
            assert json.loads(completed.stdout)["status"] == "POINT_CHECK=PASS"
    return target


def instance_id():
    board_asset = Path("/sys/devices/virtual/dmi/id/board_asset")
    if board_asset.is_file():
        value = board_asset.read_text().strip()
        if value.startswith("i-"):
            return value
    request = urllib.request.Request(
        "http://169.254.169.254/latest/api/token", method="PUT",
        headers={"X-aws-ec2-metadata-token-ttl-seconds": "60"})
    with urllib.request.urlopen(request, timeout=2) as response:
        token = response.read().decode()
    request = urllib.request.Request(
        "http://169.254.169.254/latest/meta-data/instance-id",
        headers={"X-aws-ec2-metadata-token": token})
    with urllib.request.urlopen(request, timeout=2) as response:
        return response.read().decode().strip()


def meminfo():
    values = {}
    for line in Path("/proc/meminfo").read_text().splitlines():
        key, rest = line.split(":", 1)
        values[key] = int(rest.split()[0])
    return values


def heavy_processes():
    matches = []
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit() or int(entry.name) == os.getpid():
            continue
        try:
            command = (entry / "cmdline").read_bytes().replace(b"\0", b" ").decode(
                errors="replace")
        except (FileNotFoundError, PermissionError):
            continue
        lowered = command.lower()
        if "/usr/bin/singular" in lowered or "sage" in lowered:
            matches.append({"pid": int(entry.name), "cmdline": command})
    return matches


def aws_preflight(arguments, target):
    assert sys.platform.startswith("linux") and Path("/proc").is_dir()
    branches = parse_branches(target, arguments.mode, arguments.branches)
    assert arguments.expected_instance_id.startswith("i-")
    actual_instance_id = instance_id()
    assert actual_instance_id == arguments.expected_instance_id
    singular = Path(arguments.singular).resolve()
    assert singular == Path("/usr/bin/Singular") and singular.is_file()
    assert digest(singular) == SINGULAR_SHA256
    for executable in ("/usr/bin/time", "/usr/bin/timeout", "/usr/bin/prlimit",
                       "/usr/bin/setsid"):
        assert Path(executable).is_file(), executable
    memory = meminfo()
    assert memory["MemAvailable"] >= 150 * 1024 * 1024
    assert memory["SwapTotal"] == 0 and memory["SwapFree"] == 0
    arguments.run_root.mkdir(parents=True, exist_ok=True)
    disk = shutil.disk_usage(arguments.run_root)
    required_disk = (50 + 2 * min(4, len(branches))) * 1024 ** 3
    assert disk.free >= required_disk
    heavy = heavy_processes()
    assert not heavy, heavy
    return {
        "status": "AWS_PREFLIGHT=PASS",
        "target_sha256": TARGET_SHA256,
        "mode": arguments.mode,
        "branches": branches,
        "instance_id": actual_instance_id,
        "singular_sha256": SINGULAR_SHA256,
        "mem_available_kib": memory["MemAvailable"],
        "swap_total_kib": memory["SwapTotal"],
        "disk_available_bytes": disk.free,
        "run_root": str(arguments.run_root.resolve()),
        "heavy_processes": [],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--static", action="store_true")
    parser.add_argument("--aws", action="store_true")
    parser.add_argument("--mode", choices=("modular", "exact-unit"))
    parser.add_argument("--branches")
    parser.add_argument("--expected-instance-id")
    parser.add_argument("--run-root", type=Path)
    parser.add_argument("--singular", default="/usr/bin/Singular")
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    assert arguments.static ^ arguments.aws
    target = static_preflight()
    if arguments.static:
        result = {"status": "STATIC_PREFLIGHT=PASS", "target_sha256": TARGET_SHA256,
                  "branch_count": len(target["branch_order"]),
                  "frozen_seed_points_checked": ["++++", "J0"]}
    else:
        assert all((arguments.mode, arguments.branches,
                    arguments.expected_instance_id, arguments.run_root))
        result = aws_preflight(arguments, target)
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if arguments.output:
        arguments.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
