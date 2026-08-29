#!/usr/bin/env python3
"""Turn an exact dehomogenized V43 lift into an ordinary a1-power identity."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V37 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v37_20260827/solve_graded_ladder_v37.py"
V37_SHA256 = "ba034c8cebaa27c5630872b9cf06d152e4577170486ac34ad7f695ead871845b"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_v37():
    if digest(V37) != V37_SHA256:
        fail(("V37 hash", digest(V37), V37_SHA256))
    spec = importlib.util.spec_from_file_location("v43_homogenize_v37", V37)
    if spec is None or spec.loader is None:
        fail("V37 import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require_aws(order: str) -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2"
            or not tag.startswith("max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_")
            or f"_dehom_{order}_" not in tag):
        fail("registered V43 dehom AWS lane required")
    return tag


def add_scaled(parser, target, source, scale=Fraction(1)) -> None:
    if not scale:
        return
    updated = parser.add(target, {monomial: scale * coefficient
                                  for monomial, coefficient in source.items()})
    target.clear()
    target.update(updated)


def encode_polynomial(polynomial):
    return [
        {
            "monomial": [[name, exponent] for name, exponent in monomial],
            "coefficient": [coefficient.numerator, coefficient.denominator],
        }
        for monomial, coefficient in sorted(polynomial.items())
    ]


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("--compiler-result", type=Path, required=True)
    cli.add_argument("--singular-stdout", type=Path, required=True)
    cli.add_argument("--singular-stderr", type=Path, required=True)
    cli.add_argument("--order", choices=("dp", "lp"), required=True)
    cli.add_argument("--output", type=Path, required=True)
    args = cli.parse_args()
    tag = require_aws(args.order)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)

    compiler = json.loads(args.compiler_result.read_text())
    if (compiler.get("status") != "PASS-A1-TOTAL-DVR-W30-V43-DEHOM-COMPILER"
            or compiler.get("registered_aws_lane") != tag
            or compiler.get("order") != args.order
            or compiler.get("v37_sha256") != V37_SHA256):
        fail("compiler result contract")
    singular_script = Path(compiler["singular_script"])
    if digest(singular_script) != compiler["singular_script_sha256"]:
        fail("Singular source hash")
    stdout = args.singular_stdout.read_text()
    stderr = args.singular_stderr.read_text()
    required = (
        "V43_DEHOM_OUTCOME=unit",
        "V43_DEHOM_LIFT_REPLAY=1",
        "PASS_A1_TOTAL_DVR_W30_V43_DEHOM",
    )
    if any(stdout.count(token) != 1 for token in required):
        fail("Singular stdout contract")
    if (stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1
            or any(token in stdout or token in stderr
                   for token in ("FAIL_", "Traceback", "Killed", "out of memory", "error occurred"))):
        fail("Singular resource/diagnostic contract")

    v37 = load_v37()
    parser, row_items, row_hashes, _ = v37.load_rows()
    rows = {item["name"]: item for item in row_items}
    selected_names = compiler["selected_rows"]
    multiplier_paths = [Path(path) for path in compiler["multiplier_paths"]]
    if len(selected_names) != len(multiplier_paths) or len(set(selected_names)) != len(selected_names):
        fail("multiplier census")
    multipliers = [parser.parse(path) for path in multiplier_paths]

    filtered = []
    dehom_sum = {}
    levels = []
    for name, multiplier in zip(selected_names, multipliers):
        grade = int(rows[name]["grade"])
        keep = {}
        for monomial, coefficient in multiplier.items():
            total_weight = grade + sum(parser.sigma_weight(variable) * exponent
                                       for variable, exponent in monomial)
            if total_weight % 5 == 0:
                keep[monomial] = coefficient
                levels.append(total_weight // 5)
        filtered.append(keep)
        dehom_row = parser.specialize(rows[name]["polynomial"], frozenset(), {"a1": ()})
        add_scaled(parser, dehom_sum, parser.multiply(keep, dehom_row))
    if dehom_sum != {(): Fraction(1)} or not levels:
        fail(("Z/5 projected dehom replay", parser.polynomial_text(dehom_sum)))

    exponent = max(levels)
    homogeneous_multipliers = []
    for name, multiplier in zip(selected_names, filtered):
        grade = int(rows[name]["grade"])
        homogeneous = {}
        for monomial, coefficient in multiplier.items():
            total_weight = grade + sum(parser.sigma_weight(variable) * power
                                       for variable, power in monomial)
            a1_power = exponent - total_weight // 5
            if a1_power < 0:
                fail(("negative homogenizing exponent", name, monomial))
            factor = () if not a1_power else (("a1", a1_power),)
            lifted = v37.merge_monomials(monomial, factor)
            homogeneous[lifted] = homogeneous.get(lifted, Fraction(0)) + coefficient
        homogeneous_multipliers.append({key: value for key, value in homogeneous.items() if value})

    replay = {}
    for name, multiplier in zip(selected_names, homogeneous_multipliers):
        if any(sum(parser.sigma_weight(variable) * power for variable, power in monomial)
               != 5 * exponent - int(rows[name]["grade"]) for monomial in multiplier):
            fail(("multiplier homogeneity", name))
        add_scaled(parser, replay, parser.multiply(multiplier, rows[name]["polynomial"]))
    target = {(('a1', exponent),): Fraction(1)}
    if replay != target:
        fail(("ordinary certificate replay", len(replay), parser.polynomial_text(replay)))

    used = [index for index, multiplier in enumerate(homogeneous_multipliers) if multiplier]
    if not used:
        fail("empty certificate")
    mutation_index = used[-1]
    mutation_name = selected_names[mutation_index]
    mutated_row = dict(rows[mutation_name]["polynomial"])
    mutation_monomial = sorted(mutated_row)[0]
    mutated_row[mutation_monomial] += 1
    mutation_residual = parser.multiply(
        homogeneous_multipliers[mutation_index],
        parser.add(mutated_row, {monomial: -coefficient
                                 for monomial, coefficient in rows[mutation_name]["polynomial"].items()}),
    )
    if not mutation_residual:
        fail("corrupted-row control")

    multiplier_records = {}
    multiplier_hashes = {}
    for name, multiplier in zip(selected_names, homogeneous_multipliers):
        path = output / f"homogeneous_multiplier_{name}.poly"
        path.write_text(parser.polynomial_text(multiplier) + "\n")
        multiplier_records[name] = str(path)
        multiplier_hashes[name] = digest(path)
    certificate = {
        "target": [["a1", exponent]],
        "multipliers": {
            name: encode_polynomial(multiplier)
            for name, multiplier in zip(selected_names, homogeneous_multipliers)
            if multiplier
        },
    }
    certificate_path = output / "ordinary_a1_power_certificate.json"
    certificate_path.write_text(json.dumps(certificate, sort_keys=True, indent=2) + "\n")
    result = {
        "status": "PASS-A1-TOTAL-DVR-W30-V43-DEHOM-HOMOGENIZED",
        "registered_aws_lane": tag,
        "order": args.order,
        "rho0_global_a1_exponent": exponent,
        "identity": f"a1^{exponent} lies in the full raw rho-zero ideal via the seventeen selected cascade rows",
        "used_rows": [selected_names[index] for index in used],
        "used_row_count": len(used),
        "multiplier_term_counts": {name: len(multiplier) for name, multiplier
                                   in zip(selected_names, homogeneous_multipliers)},
        "multiplier_paths": multiplier_records,
        "multiplier_sha256": multiplier_hashes,
        "certificate_sha256": digest(certificate_path),
        "compiler_result_sha256": digest(args.compiler_result),
        "singular_script_sha256": digest(singular_script),
        "singular_stdout_sha256": digest(args.singular_stdout),
        "singular_resource_sha256": digest(args.singular_stderr),
        "corrupted_row": mutation_name,
        "corrupted_monomial": [[name, power] for name, power in mutation_monomial],
        "corrupted_residual_term_count": len(mutation_residual),
        "corrupted_residual_sha256": sha256(
            json.dumps(encode_polynomial(mutation_residual), sort_keys=True,
                       separators=(",", ":")).encode()
        ).hexdigest(),
        "scope": "exact ordinary-polynomial rho-zero ideal membership; no unspecialized-rho or honest-chart conclusion",
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(f"V43_DEHOM_GLOBAL_A1_EXPONENT={exponent}")
    print("PASS-A1-TOTAL-DVR-W30-V43-DEHOM-HOMOGENIZED")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
