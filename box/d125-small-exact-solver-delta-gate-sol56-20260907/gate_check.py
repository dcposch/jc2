#!/usr/bin/env python3
"""Relocatable stdlib-only delta checks for the repaired exact.py."""
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import sys


def need(condition, message):
    if not condition:
        raise RuntimeError(message)


def load_exact(path):
    spec = importlib.util.spec_from_file_location("delta_frozen_exact", path)
    need(spec is not None and spec.loader is not None, "cannot load exact.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def replaced_once(data, old, new):
    need(data.count(old) == 1, "mutation anchor count is not one")
    return data.replace(old, new)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    inputs = args.inputs.resolve()
    exact_path = inputs / "exact.py"
    control_path = inputs / "control.stdout"
    for path in (exact_path, control_path):
        need(path.is_file(), "missing input: " + str(path))

    exact_source = exact_path.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")
    need(not any(isinstance(node, ast.Assert) for node in ast.walk(ast.parse(exact_source))),
         "exact.py contains removable Assert")
    need(not any(isinstance(node, ast.Assert) for node in ast.walk(ast.parse(self_source))),
         "gate_check.py contains removable Assert")
    need("need(stderr == b'', 'nonempty stderr')" in exact_source,
         "literal-stderr repair is absent")
    need("engine_size == sum(bool(row) for row in engine)" in exact_source,
         "nonzero-position count repair is absent")

    exact = load_exact(exact_path)
    control = control_path.read_bytes()
    need(hashlib.sha256(control).hexdigest() ==
         "fff5dfd6b2be427844ea898b95c8e159937761085ec2905b0327dc6871939922",
         "control.stdout pin mismatch")
    first = control.splitlines()[0].decode("ascii").split()
    need(len(first) == 4 and first[:2] == ["JC2CERT", "1"], "bad control header")
    source_hash = first[2]
    variables = ["x"]
    need(first[3] == exact.ring_id(variables), "control ring id mismatch")

    checks = []

    def accepted(name, stdout, stderr, inspect=None):
        value = exact.parse_result(stdout, stderr, variables, source_hash)
        if inspect is not None:
            inspect(value)
        checks.append({"name": name, "outcome": "accepted"})
        return value

    def rejected(name, stdout, stderr, reason):
        try:
            exact.parse_result(stdout, stderr, variables, source_hash)
        except ValueError as exc:
            need(str(exc) == reason, name + " rejected for wrong reason: " + str(exc))
        else:
            raise RuntimeError(name + " unexpectedly accepted")
        checks.append({"name": name, "outcome": "rejected", "reason": reason})

    def inspect_actual(value):
        engine, basis, cofactors = value
        need(len(engine) == 6, "actual I indexed-row count is not six")
        need(sum(bool(row) for row in engine) == 3, "actual nonzero-position count is not three")
        need([i + 1 for i, row in enumerate(engine) if row] == [2, 4, 5],
             "actual nonzero positions changed")
        need(engine[1] == engine[3] and bool(engine[1]), "duplicate x positions not preserved")
        need(len(basis) == 1 and cofactors is not None and len(cofactors) == 6,
             "actual G/T indexed-row counts changed")

    accepted("actual_empty_stderr_size_3", control, b"", inspect_actual)
    rejected("actual_whitespace_stderr", control, b" \n\t", "nonempty stderr")
    rejected("actual_size_down_3_to_0",
             replaced_once(control, b"I_SIZE 3\n", b"I_SIZE 0\n"), b"",
             "engine size/nonzero count mismatch")
    rejected("actual_size_up_3_to_4",
             replaced_once(control, b"I_SIZE 3\n", b"I_SIZE 4\n"), b"",
             "engine size/nonzero count mismatch")

    all_zero = ("JC2CERT 1 " + source_hash + " " + exact.ring_id(variables) + "\n"
                "I_SIZE 0\nI_BEGIN 3\nI 1 0\nI 2 0\nI 3 0\nI_END\n"
                "G_BEGIN 0\nG_END\nEND NONUNIT\n").encode("ascii")

    def inspect_zero(value):
        engine, basis, cofactors = value
        need(len(engine) == 3 and not any(engine), "all-zero indexed rows changed")
        need(basis == [] and cofactors is None, "all-zero parser fixture framing changed")

    accepted("all_zero_size_0_parser_scope_only", all_zero, b"", inspect_zero)

    result = {
        "status": "PASS",
        "optimized": not __debug__,
        "inputs": str(inputs),
        "exact_sha256": hashlib.sha256(exact_path.read_bytes()).hexdigest(),
        "control_sha256": hashlib.sha256(control).hexdigest(),
        "checks": checks,
        "certificate_functions_invoked_for_all_zero": False,
        "assert_nodes": {"exact.py": 0, "gate_check.py": 0},
    }
    encoded = (json.dumps(result, sort_keys=True, indent=2) + "\n").encode("utf-8")
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("xb") as stream:
            stream.write(encoded)
    sys.stdout.buffer.write(encoded)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print("FAIL: " + str(exc), file=sys.stderr)
        raise SystemExit(1)
