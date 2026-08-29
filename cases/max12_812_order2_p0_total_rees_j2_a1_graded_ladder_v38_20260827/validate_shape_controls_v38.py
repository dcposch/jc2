#!/usr/bin/env python3
from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
COMPILER = HERE / "census_shape_controls_v38.py"
COMPILER_SHA = "6dbbca14dd385825d394d422ed65b0e0c2a97cb7df4b6ca74c4b0c7954958353"
PREREG_SHA = "19dc957d1b327c33e8a8d5853e65db7714b5ea640418236f8485b467e60f03e9"
COMPILER_STATUS = "PASS-A1-GRADED-LADDER-V38-CONTROL-CENSUS-COMPILER"
STATUS = "PASS-A1-GRADED-LADDER-V38-CONTROL-CENSUS"
LANE_RE = re.compile(r"max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v38_[0-9]{8}T[0-9]{6}Z_control_census_(r6d|box01)")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def canonical_json(path: Path):
    raw = path.read_text()
    value = json.loads(raw, parse_constant=lambda token: fail(("JSON constant", token)))
    if raw != json.dumps(value, sort_keys=True, indent=2) + "\n":
        fail("noncanonical JSON")
    return value


def exact_dict(value, keys, label: str):
    if type(value) is not dict or set(value) != set(keys):
        fail((label, "keys"))
    return value


def exact_int(value, label: str) -> int:
    if type(value) is not int:
        fail((label, "integer"))
    return value


def exact_str(value, label: str) -> str:
    if type(value) is not str:
        fail((label, "string"))
    return value


def load_compiler():
    if digest(COMPILER) != COMPILER_SHA:
        fail("compiler hash")
    spec = importlib.util.spec_from_file_location("v38_control_replay", COMPILER)
    if spec is None or spec.loader is None:
        fail("compiler import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_monomial(raw, expected, label: str) -> None:
    if type(raw) is not list:
        fail((label, "list"))
    decoded = []
    for pair in raw:
        if type(pair) is not list or len(pair) != 2:
            fail((label, "pair"))
        decoded.append((exact_str(pair[0], label), exact_int(pair[1], label)))
    if tuple(decoded) != expected or any(exponent <= 0 for _, exponent in decoded):
        fail((label, "value"))


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("--result", type=Path, required=True)
    cli.add_argument("--compiler-stdout", type=Path, required=True)
    cli.add_argument("--compiler-stderr", type=Path, required=True)
    cli.add_argument("--registered-lane", required=True)
    cli.add_argument("--output", type=Path, required=True)
    args = cli.parse_args()
    compiler = load_compiler()
    result = canonical_json(args.result)
    top_keys = {"schema_version", "status", "registered_aws_lane", "preregistration_sha256",
                "primary_census_compiler_sha256", "row_count_named", "row_count_nonzero",
                "variable_count", "row_sha256", "censi", "scope"}
    exact_dict(result, top_keys, "result")
    if exact_int(result["schema_version"], "schema_version") != 1:
        fail("schema version")
    if exact_str(result["status"], "status") != COMPILER_STATUS:
        fail("status")
    lane = exact_str(result["registered_aws_lane"], "lane")
    if lane != args.registered_lane or LANE_RE.fullmatch(lane) is None:
        fail("lane")
    if exact_str(result["preregistration_sha256"], "prereg") != PREREG_SHA:
        fail("preregistration pin")
    if exact_str(result["primary_census_compiler_sha256"], "primary pin") != compiler.PRIMARY_SHA:
        fail("primary compiler pin")
    if exact_str(result["scope"], "scope") != compiler.SCOPE:
        fail("scope")
    if [exact_int(result[key], key) for key in ("row_count_named", "row_count_nonzero", "variable_count")] != [70, 51, 65]:
        fail("source counts")
    if type(result["row_sha256"]) is not dict or len(result["row_sha256"]) != 70:
        fail("row hashes")
    for name, value in result["row_sha256"].items():
        if type(name) is not str or re.fullmatch(r"Tg(1[0-9])_[1-7]", name) is None:
            fail(("row name", name))
        if type(value) is not str or re.fullmatch(r"[0-9a-f]{64}", value) is None:
            fail(("row hash", name))
    censi = result["censi"]
    if type(censi) is not dict or set(censi) != set(compiler.TARGETS):
        fail("censi labels")
    primary = compiler.load_primary()
    v37 = primary.load_v37()
    parser, rows, row_hashes, variables = v37.load_rows()
    if row_hashes != result["row_sha256"]:
        fail("row hash replay")
    replay = compiler.compute_censi(primary, v37, parser, rows, variables)
    census_keys = {"label", "weight", "a1_exponent", "k_exponent", "target", "products", "support",
                   "component_products", "component_monomials", "component_nnz"}
    for label in sorted(compiler.TARGETS):
        raw = exact_dict(censi[label], census_keys, label)
        if exact_str(raw["label"], f"{label}.label") != label:
            fail((label, "label"))
        for key in census_keys - {"label", "target"}:
            exact_int(raw[key], f"{label}.{key}")
        check_monomial(raw["target"], compiler.target_monomial(label), f"{label}.target")
        if raw != replay[label]:
            fail((label, "replay"))
    result_sha = digest(args.result)
    lines = args.compiler_stdout.read_text().splitlines()
    for label, census in censi.items():
        token = f"V38_CONTROL_{label}_W{census['weight']}={census['component_products']}x{census['component_monomials']}"
        if lines.count(token) != 1:
            fail((label, "stdout"))
    if lines.count(COMPILER_STATUS) != 1 or lines.count(f"RESULT_SHA256={result_sha}") != 1:
        fail("stdout result binding")
    if sum(line.startswith("RESULT_SHA256=") for line in lines) != 1:
        fail("stdout result multiplicity")
    stderr = args.compiler_stderr.read_text()
    if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
        fail("resource contract")
    diagnostics = ("Traceback", "FAIL_", "Killed", "out of memory", "error occurred")
    if any(token in args.compiler_stdout.read_text() or token in stderr for token in diagnostics):
        fail("diagnostic token")
    final = {"schema_version": 1, "status": STATUS, "registered_aws_lane": lane,
             "census_result_sha256": result_sha, "compiler_sha256": COMPILER_SHA,
             "preregistration_sha256": PREREG_SHA, "compiler_stdout_sha256": digest(args.compiler_stdout),
             "compiler_stderr_sha256": digest(args.compiler_stderr), "censi": censi, "scope": compiler.SCOPE}
    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print(STATUS)
    print(f"RESULT_SHA256={digest(args.output)}")


if __name__ == "__main__":
    main()
