#!/usr/bin/env python3
"""Homogenize an exact literal-total a1=1 lift to an honest total certificate."""

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
TOTAL_COMPILER = HERE / "compile_total_dvr_w30_v43.py"
TOTAL_COMPILER_SHA256 = "0de6a2b279aeeab8c5a635c1d7658958f3f49f0f94f8473355d281cae9438b00"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_source():
    actual = digest(TOTAL_COMPILER)
    if actual != TOTAL_COMPILER_SHA256:
        fail(("total compiler hash", actual, TOTAL_COMPILER_SHA256))
    spec = importlib.util.spec_from_file_location("v43_total_homogenize_source", TOTAL_COMPILER)
    if spec is None or spec.loader is None:
        fail("total compiler import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2"
            or not tag.startswith("max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_")
            or "_totaldehom_exact_lift_" not in tag):
        fail("registered exact V43 total-dehom lift AWS lane required")
    return tag


def add_scaled(parser, target, polynomial, scale=Fraction(1)) -> None:
    updated = parser.add(target, {monomial: scale * coefficient
                                  for monomial, coefficient in polynomial.items()})
    target.clear()
    target.update(updated)


def ordinary_t_polynomial(module_polynomial):
    result = {}
    for monomial, tpoly in module_polynomial.items():
        for degree, coefficient in tpoly.items():
            powers = dict(monomial)
            if degree:
                powers["t"] = degree
            key = tuple(sorted((name, power) for name, power in powers.items() if power))
            result[key] = result.get(key, Fraction(0)) + coefficient
    return {key: value for key, value in result.items() if value}


def dehom_a1(polynomial):
    result = {}
    for monomial, coefficient in polynomial.items():
        key = tuple((name, power) for name, power in monomial if name != "a1")
        result[key] = result.get(key, Fraction(0)) + coefficient
    return {key: value for key, value in result.items() if value}


def weight(parser, monomial) -> int:
    return sum((0 if name == "t" else parser.sigma_weight(name)) * power
               for name, power in monomial)


def encode_polynomial(polynomial):
    return [
        {"monomial": [[name, power] for name, power in monomial],
         "coefficient": [coefficient.numerator, coefficient.denominator]}
        for monomial, coefficient in sorted(polynomial.items())
    ]


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("--compiler-result", type=Path, required=True)
    cli.add_argument("--singular-stdout", type=Path, required=True)
    cli.add_argument("--singular-stderr", type=Path, required=True)
    cli.add_argument("--output", type=Path, required=True)
    args = cli.parse_args()
    tag = require_aws()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    compiler_result_path = args.compiler_result.resolve()
    compiler = json.loads(compiler_result_path.read_text())
    if (compiler.get("registered_aws_lane") != tag or compiler.get("mode") != "exact"
            or compiler.get("phase") != "lift"
            or compiler.get("prime") != 65521
            or compiler.get("status") not in (
                "PASS-A1-TOTAL-DVR-W30-V43-TOTAL-DEHOM-COMPILER",
                "PASS-A1-TOTAL-DVR-W30-V43-TOTAL-DEHOM-LITERAL-COMPILER",
            )):
        fail("compiler result contract")
    script_path = Path(compiler["singular_script"])
    if digest(script_path) != compiler["singular_script_sha256"]:
        fail("Singular source hash")
    stdout = args.singular_stdout.read_text()
    stderr = args.singular_stderr.read_text()
    required = (
        "V43_TOTAL_DEHOM_SPECIAL_UNIT=1",
        "V43_TOTAL_DEHOM_OUTCOME=unit-eliminant",
        "V43_TOTAL_DEHOM_UNIT_CONSTANT=1",
        "V43_TOTAL_DEHOM_LIFT_REPLAY=1",
        "PASS_A1_TOTAL_DVR_W30_V43_TOTAL_DEHOM",
    )
    if any(stdout.count(token) != 1 for token in required):
        fail("Singular stdout contract")
    if (stderr.count("Command being timed:") != 1 or stderr.count("Exit status: 0") != 1
            or any(token in stdout or token in stderr
                   for token in ("FAIL_", "Traceback", "Killed", "out of memory", "error occurred"))):
        fail("Singular resource/diagnostic contract")

    source = load_source()
    (parser, v37, total_rows, frozen_hashes, total_hashes, variables,
     frozen_variables, general_only, nonzero_general) = source.reconstruct_rows()
    by_name = {item["name"]: item for item in total_rows}
    selected = compiler["selected_rows"]
    if (compiler["selected_total_t_sha256"] != {name: total_hashes[name] for name in selected}
            or any(name not in by_name for name in selected)):
        fail("selected total-row custody")
    multiplier_paths = [Path(path) for path in compiler["multiplier_paths"]]
    if len(multiplier_paths) != len(selected):
        fail("multiplier census")
    multipliers = [parser.parse(path) for path in multiplier_paths]
    unit_path = Path(compiler["unit_path"])
    unit = parser.parse(unit_path)
    if (not unit or any(any(name != "t" for name, _ in monomial) for monomial in unit)
            or unit.get((), Fraction(0)) != 1):
        fail(("unit-factor contract", unit))

    rows = [ordinary_t_polynomial(by_name[name]["polynomial"]) for name in selected]
    filtered = []
    total_levels = []
    dehom_replay = {}
    for name, multiplier, row in zip(selected, multipliers, rows):
        grade = int(by_name[name]["grade"])
        keep = {}
        for monomial, coefficient in multiplier.items():
            total_weight = grade + weight(parser, monomial)
            if total_weight % 5 == 0:
                keep[monomial] = coefficient
                total_levels.append(total_weight)
        filtered.append(keep)
        add_scaled(parser, dehom_replay, parser.multiply(keep, dehom_a1(row)))
    if dehom_replay != unit or not total_levels:
        fail(("residue-zero dehom replay", len(dehom_replay), len(unit)))

    homogenizing_weight = max(total_levels)
    exponent = homogenizing_weight // 5
    homogeneous_multipliers = []
    for name, multiplier in zip(selected, filtered):
        grade = int(by_name[name]["grade"])
        homogeneous = {}
        for monomial, coefficient in multiplier.items():
            deficit = homogenizing_weight - grade - weight(parser, monomial)
            if deficit < 0 or deficit % 5:
                fail(("homogenizing deficit", name, monomial, deficit))
            powers = dict(monomial)
            if deficit:
                powers["a1"] = powers.get("a1", 0) + deficit // 5
            lifted = tuple(sorted((variable, power) for variable, power in powers.items() if power))
            homogeneous[lifted] = homogeneous.get(lifted, Fraction(0)) + coefficient
        homogeneous_multipliers.append({key: value for key, value in homogeneous.items() if value})

    replay = {}
    for multiplier, row in zip(homogeneous_multipliers, rows):
        add_scaled(parser, replay, parser.multiply(multiplier, row))
    target = {}
    for monomial, coefficient in unit.items():
        powers = dict(monomial)
        powers["a1"] = powers.get("a1", 0) + exponent
        key = tuple(sorted(powers.items()))
        target[key] = target.get(key, Fraction(0)) + coefficient
    if replay != target:
        fail(("honest total-t homogenized replay", len(replay), len(target)))

    used = [index for index, multiplier in enumerate(homogeneous_multipliers) if multiplier]
    if not used:
        fail("empty certificate")
    mutation_index = used[-1]
    mutation_row = dict(rows[mutation_index])
    mutation_monomial = sorted(mutation_row)[0]
    mutation_residual = parser.multiply(homogeneous_multipliers[mutation_index],
                                        {mutation_monomial: Fraction(1)})
    if not mutation_residual:
        fail("corrupted-row control")

    multiplier_hashes = {}
    multiplier_outputs = {}
    for name, multiplier in zip(selected, homogeneous_multipliers):
        path = output / f"total_t_homogeneous_multiplier_{name}.poly"
        path.write_text(parser.polynomial_text(multiplier) + "\n")
        multiplier_outputs[name] = str(path)
        multiplier_hashes[name] = digest(path)
    unit_output = output / "unit_factor_t.poly"
    unit_output.write_text(parser.polynomial_text(unit) + "\n")
    certificate = {
        "identity": f"a1^{exponent}*U(t)=sum_i H_i(t,X)*Tg_i(t,X), U(0)=1",
        "t_means": "rho^2",
        "a1_exponent": exponent,
        "unit_factor": encode_polynomial(unit),
        "multipliers": {name: encode_polynomial(multiplier)
                        for name, multiplier in zip(selected, homogeneous_multipliers)
                        if multiplier},
    }
    certificate_path = output / "honest_total_t_a1_certificate.json"
    certificate_path.write_text(json.dumps(certificate, sort_keys=True,
                                           separators=(",", ":")) + "\n")
    result = {
        "status": "PASS-A1-TOTAL-DVR-W30-V43-TOTAL-DEHOM-HOMOGENIZED",
        "registered_aws_lane": tag,
        "scope": "exact Q[t] identity in the literal regenerated total rows; t maps injectively to rho^2",
        "identity": f"a1^{exponent}*U(rho^2) lies in the literal total-rho selected-row ideal, with U(0)=1",
        "a1_exponent": exponent,
        "homogeneous_sigma_weight": homogenizing_weight,
        "unit_factor_t_path": str(unit_output),
        "unit_factor_t_sha256": digest(unit_output),
        "used_rows": [selected[index] for index in used],
        "used_row_count": len(used),
        "multiplier_term_counts": {name: len(multiplier)
                                   for name, multiplier in zip(selected, homogeneous_multipliers)},
        "multiplier_paths": multiplier_outputs,
        "multiplier_sha256": multiplier_hashes,
        "certificate_path": str(certificate_path),
        "certificate_sha256": digest(certificate_path),
        "compiler_result_sha256": digest(compiler_result_path),
        "singular_script_sha256": digest(script_path),
        "singular_stdout_sha256": digest(args.singular_stdout),
        "singular_resource_sha256": digest(args.singular_stderr),
        "corrupted_row": selected[mutation_index],
        "corrupted_monomial": encode_polynomial({mutation_monomial: Fraction(1)})[0]["monomial"],
        "corrupted_residual_term_count": len(mutation_residual),
        "corrupted_residual_sha256": sha256(json.dumps(
            encode_polynomial(mutation_residual), sort_keys=True,
            separators=(",", ":")).encode()).hexdigest(),
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(f"V43_TOTAL_DEHOM_A1_EXPONENT={exponent}")
    print("PASS-A1-TOTAL-DVR-W30-V43-TOTAL-DEHOM-HOMOGENIZED")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
