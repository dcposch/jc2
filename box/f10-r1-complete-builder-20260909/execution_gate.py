"""Metadata-only launch gate; NOT an allocator, supervisor, or authority issuer.

Root must create a separately registered authority on an approved AWS instance.
This module does not authorize its own use. The shipped template is disabled.
"""
import hashlib
import json
import os
from pathlib import Path
import socket
import sys


def authorize(authority_path, script_path, operation):
    path = Path(authority_path).resolve(strict=True)
    if path.stat().st_size > 65536:
        raise RuntimeError("authority too large")
    spec = json.loads(path.read_text())
    if spec.get("schema") != "F10-R1-REGISTERED/v1" or spec.get("enabled") is not True:
        raise RuntimeError("no active registered authority")
    if not spec.get("job_tag") or not spec.get("admissibility_sha256"):
        raise RuntimeError("missing job/admissibility registration")
    if spec.get("operation") != operation:
        raise RuntimeError("wrong registered operation")
    instance = Path("/sys/devices/virtual/dmi/id/board_asset_tag").read_text().strip()
    vendor = Path("/sys/devices/virtual/dmi/id/sys_vendor").read_text().strip()
    if vendor != "Amazon EC2" or not instance.startswith("i-"):
        raise RuntimeError("not AWS EC2")
    if instance != spec.get("instance_id") or socket.gethostname() != spec.get("hostname"):
        raise RuntimeError("not the registered AWS host")
    if not sys.flags.isolated or not sys.flags.dont_write_bytecode:
        raise RuntimeError("require Python -I -B")
    script = Path(script_path).resolve(strict=True)
    expected_child = ["/usr/bin/python3", "-I", "-B", str(script), *sys.argv[1:]]
    if spec.get("child_argv") != expected_child:
        raise RuntimeError("child argv differs from registration")
    parent = Path(f"/proc/{os.getppid()}/cmdline").read_bytes().split(b"\0")
    if parent and parent[-1] == b"":
        parent.pop()
    actual = [os.fsdecode(item) for item in parent]
    expected = spec.get("parent_argv")
    if actual != expected:
        raise RuntimeError("full parent argv differs from registered capped runner")
    runner = str(Path(spec["runner_path"]).resolve(strict=True))
    caps = spec["caps"]
    required = ["/usr/bin/python3", "-I", "-B", runner,
                "--wall-seconds", caps["wall_seconds"],
                "--cpu-seconds", caps["cpu_seconds"],
                "--rss-bytes", caps["rss_bytes"],
                "--rss-sample-seconds", caps["rss_sample_seconds"],
                "--term-grace-seconds", caps["term_grace_seconds"],
                "--cwd", spec["cwd"],
                "--stdout-file", spec["stdout_file"],
                "--stderr-file", spec["stderr_file"],
                "--telemetry-file", spec["telemetry_file"], "--", *expected_child]
    if expected != required or os.getcwd() != spec["cwd"]:
        raise RuntimeError("registration is not the exact required CAPRUN argv")
    for key in ("wall_seconds", "cpu_seconds", "rss_bytes", "rss_sample_seconds", "term_grace_seconds"):
        value = caps[key]
        if not isinstance(value, str) or not value or value.startswith("-") or value == "0":
            raise RuntimeError("invalid registered cap")
    files = spec["file_sha256"]
    for required_file in (str(script), str(Path(__file__).resolve()), runner):
        if required_file not in files:
            raise RuntimeError("missing executable pin")
    if operation == "check" and str(Path(sys.argv[2]).resolve(strict=True)) not in files:
        raise RuntimeError("checker input artifact must be explicitly hash-registered")
    for filename, digest in files.items():
        if hashlib.sha256(Path(filename).read_bytes()).hexdigest() != digest:
            raise RuntimeError("registered file changed: " + filename)
    return {"job_tag": spec["job_tag"], "hostname": socket.gethostname(),
            "instance_id": instance, "authority_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
