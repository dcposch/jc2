#!/usr/bin/env python3
from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
COMPILER = HERE / "solve_w19_compatibility_v39.py"
COMPILER_SHA = "a268558d26fcedffb2fd03ba373de3c98bf3f8dc475fc4790c0753b69b1ebc60"
STATUS = "PASS-A1-W19-TG19-7-COMPATIBILITY-V39"
COMPILER_STATUS = "PASS-A1-W19-TG19-7-COMPATIBILITY-V39-COMPILER"
LANE_RE = re.compile(r"max12_812_order2_p0_total_rees_j2_a1_w19_tg19_7_compatibility_v39_[0-9]{8}T[0-9]{6}Z_q(65521|65519)_(r6d|box01)")
HEX_RE = re.compile(r"[0-9a-f]{64}")
HOST_RE = re.compile(r"[A-Za-z0-9.-]+")
UTC_RE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def canonical_json(path: Path):
    raw = path.read_text()
    value = json.loads(raw)
    if raw != json.dumps(value, sort_keys=True, indent=2) + "\n":
        fail(("noncanonical JSON", str(path)))
    return value


def load_compiler():
    if digest(COMPILER) != COMPILER_SHA:
        fail("compiler hash")
    spec = importlib.util.spec_from_file_location("v39_validator_compiler", COMPILER)
    if spec is None or spec.loader is None:
        fail("compiler import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def same_typed(actual, expected, path: str = "payload") -> None:
    if type(actual) is not type(expected):
        fail((path, "type", type(actual).__name__, type(expected).__name__))
    if type(expected) is dict:
        if set(actual) != set(expected):
            fail((path, "keys"))
        for key in expected:
            same_typed(actual[key], expected[key], f"{path}.{key}")
    elif type(expected) is list:
        if len(actual) != len(expected):
            fail((path, "length"))
        for index, (left, right) in enumerate(zip(actual, expected)):
            same_typed(left, right, f"{path}[{index}]")
    elif actual != expected:
        fail((path, "value"))


def parse_launch(path: Path, lane: str, prime: int):
    lines = path.read_text().splitlines()
    if len(lines) != 5 or any("\x00" in line for line in lines):
        fail("launch registration lines")
    parsed = {}
    for line in lines:
        if line.count("=") != 1:
            fail("launch registration syntax")
        key, value = line.split("=", 1)
        if key in parsed:
            fail("launch registration duplicate")
        parsed[key] = value
    if set(parsed) != {"tag", "host", "start_utc", "selector_prime", "source_archive_sha256"}:
        fail("launch registration keys")
    if (parsed["tag"] != lane or HOST_RE.fullmatch(parsed["host"]) is None
            or UTC_RE.fullmatch(parsed["start_utc"]) is None
            or parsed["selector_prime"] != str(prime)
            or HEX_RE.fullmatch(parsed["source_archive_sha256"]) is None):
        fail("launch registration values")
    return parsed


def stdout_contract(path: Path, payload, result_sha: str) -> None:
    lines = path.read_text().splitlines()
    expected = (
        f"V39_OUTCOME={payload['certificate']['kind']}",
        f"V39_EXACT_RANK={payload['certificate']['exact_rank']}",
        f"V39_RESIDUAL_TERMS={payload['residual']['term_count']}",
        COMPILER_STATUS,
        f"RESULT_SHA256={result_sha}",
    )
    for token in expected:
        if lines.count(token) != 1:
            fail(("stdout token", token))
    if sum(line.startswith("RESULT_SHA256=") for line in lines) != 1:
        fail("stdout result multiplicity")


def independent_pristine_target_gate(compiler, payload) -> None:
    # This gate intentionally precedes the expensive deterministic rebuild so
    # the external coefficient-deletion fixture fails immediately.
    _, _, rows, row_hashes, _, bridge = compiler.load_sources()
    target = next(item["polynomial"] for item in rows if item["name"] == compiler.TARGET_NAME)
    target_record = payload.get("target")
    if type(target_record) is not dict:
        fail("target record")
    if (target_record.get("name") != compiler.TARGET_NAME
            or target_record.get("grade") != compiler.TARGET_GRADE
            or target_record.get("q_file_sha256") != row_hashes[compiler.TARGET_NAME]
            or target_record.get("q_rho0_sha256") != compiler.object_hash(compiler.encode_polynomial(target))
            or target_record.get("polynomial") != compiler.encode_polynomial(target)
            or bridge["rows"][compiler.TARGET_NAME]["q_term_count"] != 552):
        fail("target polynomial mutation or bridge failure")


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("--result", type=Path, required=True)
    cli.add_argument("--compiler-stdout", type=Path, required=True)
    cli.add_argument("--compiler-stderr", type=Path, required=True)
    cli.add_argument("--launch-registration", type=Path, required=True)
    cli.add_argument("--selector-prime", type=int, choices=(65521, 65519), required=True)
    cli.add_argument("--registered-lane", required=True)
    cli.add_argument("--output", type=Path, required=True)
    args = cli.parse_args()
    compiler = load_compiler()
    result = canonical_json(args.result)
    top_keys = {"schema_version", "status", "registered_aws_lane", "selector_prime_requested",
                "preregistration_sha256", "row_bridge_sha256", "payload"}
    if type(result) is not dict or set(result) != top_keys:
        fail("result keys")
    if type(result["schema_version"]) is not int or result["schema_version"] != 1:
        fail("schema version")
    if type(result["status"]) is not str or result["status"] != COMPILER_STATUS:
        fail("compiler status")
    lane = result["registered_aws_lane"]
    match = LANE_RE.fullmatch(lane) if type(lane) is str else None
    if (lane != args.registered_lane or match is None or int(match.group(1)) != args.selector_prime
            or type(result["selector_prime_requested"]) is not int
            or result["selector_prime_requested"] != args.selector_prime):
        fail("lane/selector binding")
    if (type(result["preregistration_sha256"]) is not str
            or result["preregistration_sha256"] != compiler.PREREG_SHA
            or type(result["row_bridge_sha256"]) is not str
            or result["row_bridge_sha256"] != compiler.BRIDGE_SHA):
        fail("frozen input pins")
    launch = parse_launch(args.launch_registration, lane, args.selector_prime)
    independent_pristine_target_gate(compiler, result["payload"])

    # Rebuild the complete system and exact-Q certificate under the frozen
    # selector.  Exact type/key recursion makes the emitted schema closed.
    expected_payload = compiler.compute_payload(args.selector_prime)
    same_typed(result["payload"], expected_payload)

    # A separate reconstruction/replay pass checks the identity against all
    # 802 products, rather than accepting the compiler's PASS token.
    v37, parser, rows, _, variables, _ = compiler.load_sources()
    target = next(item["polynomial"] for item in rows if item["name"] == compiler.TARGET_NAME)
    other_rows = [item for item in rows if item["name"] != compiler.TARGET_NAME]
    products = v37.build_products(19, parser, other_rows, variables)
    products.sort(key=lambda item: (item["grade"], item["row"], item["multiplier"]))
    component_indices, _ = compiler.target_component(products, target)
    if len(products) != compiler.EXPECTED_PRODUCTS:
        fail("validator product count")
    compiler.replay_payload(result["payload"], products, component_indices, target)

    result_sha = digest(args.result)
    stdout_contract(args.compiler_stdout, result["payload"], result_sha)
    stdout = args.compiler_stdout.read_text()
    stderr = args.compiler_stderr.read_text()
    if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
        fail("compiler resource contract")
    diagnostics = ("Traceback", "FAIL_", "Killed", "out of memory", "error occurred")
    if any(token in stdout or token in stderr for token in diagnostics):
        fail("compiler diagnostic token")
    final = {
        "schema_version": 1,
        "status": STATUS,
        "registered_aws_lane": lane,
        "selector_prime": args.selector_prime,
        "outcome": result["payload"]["certificate"]["kind"],
        "exact_rank": result["payload"]["certificate"]["exact_rank"],
        "residual_sha256": result["payload"]["residual"]["polynomial_sha256"],
        "residual_term_count": result["payload"]["residual"]["term_count"],
        "compiler_result_sha256": result_sha,
        "compiler_sha256": COMPILER_SHA,
        "preregistration_sha256": compiler.PREREG_SHA,
        "row_bridge_sha256": compiler.BRIDGE_SHA,
        "compiler_stdout_sha256": digest(args.compiler_stdout),
        "compiler_stderr_sha256": digest(args.compiler_stderr),
        "launch_registration_sha256": digest(args.launch_registration),
        "source_archive_sha256": launch["source_archive_sha256"],
        "scope": compiler.SCOPE,
    }
    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print(STATUS)
    print(f"RESULT_SHA256={digest(args.output)}")


if __name__ == "__main__":
    main()
