#!/usr/bin/env python3
from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
COMPILER = HERE / "census_graded_ladder_v38.py"
COMPILER_SHA = "55892916a5f561e6b71ab1ccbb233480ff6dabc96c0ee828ddf0ec8e74e08a14"
PREREG_SHA = "b9ec8a05e17ac1571acd16d8f6c690c366f0a7d589d4fb77d215222ed51eee91"
STATUS = "PASS-A1-GRADED-LADDER-V38-CENSUS"
COMPILER_STATUS = "PASS-A1-GRADED-LADDER-V38-CENSUS-COMPILER"
SCOPE = "combinatorial census of complete fixed-weight products in homogeneous raw ordered-a1 rho-zero row ideal through grade19"
LANE_RE = re.compile(r"max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v38_[0-9]{8}T[0-9]{6}Z_census_(r6d|box01)")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


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


def canonical_json(path: Path):
    raw = path.read_text()
    try:
        value = json.loads(raw)
    except (ValueError, json.JSONDecodeError) as error:
        fail(("JSON parse", str(error)))
    if raw != json.dumps(value, sort_keys=True, indent=2) + "\n":
        fail("noncanonical JSON")
    return value


def load_compiler():
    if digest(COMPILER) != COMPILER_SHA:
        fail("compiler hash")
    spec = importlib.util.spec_from_file_location("v38_census_replay", COMPILER)
    if spec is None or spec.loader is None:
        fail("compiler import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_target(raw, expected, label: str) -> None:
    if type(raw) is not list or len(raw) != len(expected):
        fail((label, "target list"))
    seen = []
    for index, pair in enumerate(raw):
        if type(pair) is not list or len(pair) != 2:
            fail((label, "target pair", index))
        name = exact_str(pair[0], f"{label}.name")
        exponent = exact_int(pair[1], f"{label}.exponent")
        if exponent <= 0:
            fail((label, "positive exponent"))
        seen.append((name, exponent))
    if tuple(seen) != expected:
        fail((label, "target value"))


def stdout_contract(path: Path, censi, result_sha: str) -> None:
    lines = path.read_text().splitlines()
    for weight, census in censi.items():
        token = f"V38_CENSUS_W{weight}={census['component_products']}x{census['component_monomials']}"
        if lines.count(token) != 1:
            fail(("stdout census", weight))
    if lines.count(COMPILER_STATUS) != 1 or lines.count(f"RESULT_SHA256={result_sha}") != 1:
        fail("stdout result binding")
    if sum(line.startswith("RESULT_SHA256=") for line in lines) != 1:
        fail("stdout result multiplicity")


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
    top_keys = {
        "schema_version", "status", "registered_aws_lane", "preregistration_sha256",
        "v37_compiler_sha256", "row_count_named", "row_count_nonzero", "variable_count",
        "row_sha256", "censi", "scope",
    }
    exact_dict(result, top_keys, "result")
    if exact_int(result["schema_version"], "schema_version") != 1:
        fail("schema version")
    if exact_str(result["status"], "status") != COMPILER_STATUS:
        fail("status")
    lane = exact_str(result["registered_aws_lane"], "registered_aws_lane")
    if lane != args.registered_lane or LANE_RE.fullmatch(lane) is None:
        fail("registered lane")
    if exact_str(result["preregistration_sha256"], "preregistration_sha256") != PREREG_SHA:
        fail("preregistration pin")
    if exact_str(result["v37_compiler_sha256"], "v37_compiler_sha256") != compiler.V37_SHA:
        fail("V37 compiler pin")
    if (exact_int(result["row_count_named"], "row_count_named") != 70
            or exact_int(result["row_count_nonzero"], "row_count_nonzero") != 51
            or exact_int(result["variable_count"], "variable_count") != 65):
        fail("source counts")
    if exact_str(result["scope"], "scope") != SCOPE:
        fail("scope")
    row_sha = result["row_sha256"]
    if type(row_sha) is not dict or len(row_sha) != 70:
        fail("row hashes schema")
    for name, value in row_sha.items():
        if type(name) is not str or re.fullmatch(r"Tg(1[0-9])_[1-7]", name) is None:
            fail(("row hash key", name))
        if type(value) is not str or re.fullmatch(r"[0-9a-f]{64}", value) is None:
            fail(("row hash value", name))
    censi = result["censi"]
    if type(censi) is not dict or set(censi) != {str(weight) for weight in compiler.TARGETS}:
        fail("censi keys")
    parser, rows, replay_hashes, variables = compiler.load_v37().load_rows()
    if row_sha != replay_hashes:
        fail("row hash replay")
    replay = compiler.compute_censi(compiler.load_v37(), parser, rows, variables)
    census_keys = {"weight", "target", "products", "support", "component_products", "component_monomials", "component_nnz"}
    for weight in sorted(compiler.TARGETS):
        raw = exact_dict(censi[str(weight)], census_keys, f"W{weight}")
        if exact_int(raw["weight"], f"W{weight}.weight") != weight:
            fail(("weight", weight))
        check_target(raw["target"], compiler.target_monomial(weight), f"W{weight}")
        for key in census_keys - {"target"}:
            exact_int(raw[key], f"W{weight}.{key}")
        if raw != replay[str(weight)]:
            fail(("census replay", weight))
    result_sha = digest(args.result)
    stdout_contract(args.compiler_stdout, censi, result_sha)
    stderr = args.compiler_stderr.read_text()
    if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
        fail("resource contract")
    diagnostics = ("Traceback", "FAIL_", "Killed", "out of memory", "error occurred")
    if any(token in args.compiler_stdout.read_text() or token in stderr for token in diagnostics):
        fail("diagnostic token")
    final = {
        "schema_version": 1,
        "status": STATUS,
        "registered_aws_lane": lane,
        "census_result_sha256": result_sha,
        "compiler_sha256": COMPILER_SHA,
        "preregistration_sha256": PREREG_SHA,
        "compiler_stdout_sha256": digest(args.compiler_stdout),
        "compiler_stderr_sha256": digest(args.compiler_stderr),
        "censi": censi,
        "scope": SCOPE,
    }
    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print(STATUS)
    print(f"RESULT_SHA256={digest(args.output)}")


if __name__ == "__main__":
    main()
