#!/usr/bin/env python3
from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
COMPILER = HERE / "solve_graded_ladder_v37.py"
COMPILER_SHA = "ba034c8cebaa27c5630872b9cf06d152e4577170486ac34ad7f695ead871845b"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_compiler():
    if digest(COMPILER) != COMPILER_SHA:
        fail("compiler hash")
    spec = importlib.util.spec_from_file_location("v37_replay", COMPILER)
    if spec is None or spec.loader is None:
        fail("compiler import")
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


def main() -> None:
    cli = argparse.ArgumentParser(); cli.add_argument("--result", type=Path, required=True)
    cli.add_argument("--compiler-stdout", type=Path, required=True); cli.add_argument("--compiler-stderr", type=Path, required=True)
    cli.add_argument("--selector-prime", type=int, choices=(65521, 65519, 65497, 65479), required=True)
    cli.add_argument("--output", type=Path, required=True); args = cli.parse_args()
    compiler = load_compiler(); result = json.loads(args.result.read_text())
    if (result.get("status") != "PASS-A1-GRADED-LADDER-V37-COMPILER"
            or result.get("selector_prime_requested") != args.selector_prime
            or result.get("row_count_named") != 70 or result.get("row_count_nonzero") != 51
            or result.get("variable_count") != 65 or set(result.get("results", {})) != {"17", "18", "19", "20"}):
        fail("result contract")
    parser, rows, row_hashes, variables = compiler.load_rows()
    if row_hashes != result["row_sha256"] or compiler.v27_control(parser, rows, variables) != result["v27_control_products"]:
        fail("upstream replay")
    outcomes = {}
    for weight in sorted(compiler.TARGETS):
        record = result["results"][str(weight)]; target = compiler.target_monomial(weight)
        if compiler.decode_monomial(record["target"]) != target:
            fail(("target", weight))
        products = compiler.build_products(weight, parser, rows, variables)
        component_indices, component_monomials = compiler.target_component(products, target)
        census = {"products": len(products), "support": len({target} | {monomial for item in products for monomial in item["polynomial"]}),
                  "component_products": len(component_indices), "component_monomials": len(component_monomials),
                  "component_nnz": sum(len(products[index]["polynomial"]) for index in component_indices)}
        if any(record.get(key) != value for key, value in census.items()) or census != compiler.EXPECTED[weight]:
            fail(("census", weight))
        compiler.replay_certificate(record, products, component_indices, target)
        outcomes[weight] = record["outcome"]
    stdout = args.compiler_stdout.read_text(); stderr = args.compiler_stderr.read_text()
    for weight, outcome in outcomes.items():
        if stdout.splitlines().count(f"V37_W{weight}={outcome}") != 1:
            fail(("stdout outcome", weight))
    if stdout.splitlines().count("PASS-A1-GRADED-LADDER-V37-COMPILER") != 1:
        fail("compiler pass token")
    if stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1:
        fail("resource contract")
    if any(token in stdout or token in stderr for token in ("FAIL_", "?", "error occurred", "Killed", "out of memory")):
        fail("diagnostic token")
    final = {"status": "PASS-A1-GRADED-LADDER-V37", "selector_prime": args.selector_prime,
             "outcomes": {str(weight): outcome for weight, outcome in outcomes.items()},
             "result_sha256": digest(args.result), "compiler_stdout_sha256": digest(args.compiler_stdout),
             "compiler_stderr_sha256": digest(args.compiler_stderr), "compiler_sha256": COMPILER_SHA,
             "scope": result["scope"]}
    args.output.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-GRADED-LADDER-V37-VALIDATOR")


if __name__ == "__main__":
    main()
