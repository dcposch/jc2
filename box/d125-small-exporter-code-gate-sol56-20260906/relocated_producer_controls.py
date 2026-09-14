#!/usr/bin/env python3
"""Run the frozen tiny producer test from owned fresh paths; never production."""
import argparse
import hashlib
import json
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time


AS_LIMIT = 512 * 1024**2
PINS = {
    "baseline.py": "ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53",
    "exporter.py": "9fd003e420f3ee069f1ed1c06a365e5b4500d361bc3951f2f8f17ef733ab3703",
    "test_exporter.py": "331e97c84f22592a1a28842df7c11e84e4f72355a906c156403eb5eaca490b2b",
}
MUTATIONS = ("missing_low", "field_split", "target", "fixed_zero", "guard", "resynced")


def digest(path):
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def limits():
    resource.setrlimit(resource.RLIMIT_AS, (AS_LIMIT, AS_LIMIT))
    resource.setrlimit(resource.RLIMIT_CPU, (25, 25))


def child(arguments):
    limits()
    signal.alarm(30)
    inputs = Path(arguments.inputs).resolve()
    virtual = Path(arguments.virtual_file).resolve()
    sys.path.insert(0, str(inputs))
    sys.argv = [str(virtual), "--output", str(Path(arguments.test_output).resolve())]
    if arguments.mutation:
        sys.argv += ["--mutation", arguments.mutation]
    source = (inputs / "test_exporter.py").read_bytes()
    namespace = {
        "__name__": "__main__",
        "__file__": str(virtual),
        "__package__": None,
        "__cached__": None,
        "__builtins__": __builtins__,
    }
    exec(compile(source, str(virtual), "exec"), namespace)


def parent(arguments):
    limits()
    signal.alarm(30)
    started = time.monotonic()
    inputs = Path(arguments.inputs).resolve()
    outdir = Path(arguments.outdir).resolve()
    receipt = Path(arguments.receipt).resolve()
    if outdir.exists() or receipt.exists():
        raise RuntimeError("fresh output paths required")
    outdir.mkdir(parents=False)
    observed = {name: digest(inputs / name) for name in PINS}
    if observed != PINS:
        raise RuntimeError("frozen pin mismatch")
    runs = []
    for optimized in (False, True):
        for mutation in (None,) + MUTATIONS:
            label = ("optimized" if optimized else "normal") + "-" + (mutation or "pass")
            output = outdir / (label + ".json")
            argv = [sys.executable]
            if optimized:
                argv.append("-O")
            argv += [str(Path(__file__).resolve()), "--child", "--inputs", str(inputs),
                     "--virtual-file", str(outdir / "test_exporter.py"),
                     "--test-output", str(output)]
            if mutation:
                argv += ["--mutation", mutation]
            before = time.monotonic()
            run = subprocess.run(argv, text=True, capture_output=True, timeout=30,
                                 preexec_fn=limits)
            expected = 1 if mutation else 0
            if run.returncode != expected:
                raise RuntimeError("unexpected exit: " + label)
            if mutation and "ValueError: strict full stream replay mismatch at " not in run.stderr:
                raise RuntimeError("mutation rejected for wrong reason: " + label)
            checks = None
            if not mutation:
                result = json.loads(output.read_text(encoding="utf-8"))
                if result["status"] != "PASS" or result["check_count"] != 53:
                    raise RuntimeError("positive control mismatch: " + label)
                checks = result["check_count"]
            runs.append({"label": label, "returncode": run.returncode,
                         "expected_returncode": expected, "check_count": checks,
                         "wall_seconds": time.monotonic() - before,
                         "intended_rejection": bool(mutation)})
    result = {"status": "PASS", "pins": observed, "runs": runs,
              "positive_checks_each_mode": 53, "repaired_footer_mutations_each_mode": 6,
              "all_children_terminal": True, "production_rows_generated": 0,
              "cas_sympy_aws_network": False,
              "limits_per_command": {"wall_seconds": 30, "cpu_seconds": 25,
                                     "address_space_bytes": AS_LIMIT},
              "elapsed_seconds": time.monotonic() - started}
    with receipt.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, sort_keys=True, indent=2)
        stream.write("\n")
    print(json.dumps({"status": "PASS", "runs": len(runs),
                      "seconds": result["elapsed_seconds"]}))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--child", action="store_true")
    parser.add_argument("--inputs", required=True)
    parser.add_argument("--outdir")
    parser.add_argument("--receipt")
    parser.add_argument("--virtual-file")
    parser.add_argument("--test-output")
    parser.add_argument("--mutation", choices=MUTATIONS)
    arguments = parser.parse_args()
    if arguments.child:
        child(arguments)
    else:
        if not arguments.outdir or not arguments.receipt:
            parser.error("--outdir and --receipt are required")
        parent(arguments)


if __name__ == "__main__":
    main()
