#!/usr/bin/env python3
"""Exact Laurent replay, denominator clearing, and total rehomogenization."""

from __future__ import annotations

import argparse
from fractions import Fraction
from functools import reduce
from hashlib import sha256
import importlib.util
import json
from math import gcd, lcm
import os
from pathlib import Path
import platform
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
G3_CASE = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_full_generic_qt_lift_v43g3_20260827"
G3_RESULT = G3_CASE / "RESULT.md"
G3_RESULT_SHA256 = "6db87ebacaa175c68dca5739dbad35390d36ff62ff914859c82a1d60e79270c4"
G3_FREEZE = G3_CASE / "FREEZE.sha256"
G3_FREEZE_SHA256 = "8f60b30576e1712479e09cc01c3244c6ff5c7053c0d3cd08e9d4fbad8745ca45"
G3_AWS = G3_CASE / "aws_r6a_lift_20260827T110250Z"
G3_COMPILER_RESULT = G3_AWS / "compiled/compiler_result.json"
G3_COMPILER_RESULT_SHA256 = "1c00aef261a3d674cb1b63f4fad18cf0121b9bcb6711a2103e893bab7a83758e"
G3_SCRIPT = G3_AWS / "compiled/generic_qt_tracked_lift.sing"
G3_SCRIPT_SHA256 = "0bca5e57db93e620c8f1f9ad52ea50b3f16ab4d01ad0326cab96009bbe803893"
G3_STDOUT = G3_AWS / "run/max12_812_order2_p0_total_rees_j2_a1_full_generic_qt_lift_v43g3_20260827T110250Z_exact_lift_r6a_singular.stdout"
V43 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827/compile_total_dvr_w30_v43.py"
V43_SHA256 = "0de6a2b279aeeab8c5a635c1d7658958f3f49f0f94f8473355d281cae9438b00"
PREREG = HERE / "PREREGISTRATION.md"
TAG_PREFIX = "max12_812_order2_p0_total_rees_j2_a1_generic_rehom_v43g4_"

Monomial = tuple[tuple[str, int], ...]
Polynomial = dict[Monomial, Fraction]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag.startswith(TAG_PREFIX)
        or "_exact_rehom_" not in tag
    ):
        fail("registered V43G4 AWS exact rehom lane required")
    return tag


def load(path: Path, expected: str, name: str):
    actual = digest(path)
    if actual != expected:
        fail(("module hash", str(path), actual, expected))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("module import", str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def verify_freeze() -> None:
    if digest(G3_FREEZE) != G3_FREEZE_SHA256:
        fail(("G3 freeze hash", digest(G3_FREEZE), G3_FREEZE_SHA256))
    for line in G3_FREEZE.read_text().splitlines():
        expected, relative = line.split(maxsplit=1)
        path = ROOT / relative
        actual = digest(path)
        if actual != expected:
            fail(("G3 frozen file", relative, actual, expected))


def canonical(powers: dict[str, int]) -> Monomial:
    if any(exponent < 0 and name != "t" for name, exponent in powers.items()):
        fail(("negative non-t exponent", powers))
    return tuple(sorted((name, exponent) for name, exponent in powers.items() if exponent))


def add_scaled(target: Polynomial, source: Polynomial, scale: Fraction = Fraction(1)) -> None:
    for monomial, coefficient in source.items():
        value = target.get(monomial, Fraction(0)) + scale * coefficient
        if value:
            target[monomial] = value
        else:
            target.pop(monomial, None)


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            powers = dict(lm)
            for name, exponent in rm:
                powers[name] = powers.get(name, 0) + exponent
            key = canonical(powers)
            value = result.get(key, Fraction(0)) + lc * rc
            if value:
                result[key] = value
            else:
                result.pop(key, None)
    return result


def ordinary_t_polynomial(module_polynomial) -> Polynomial:
    result: Polynomial = {}
    for monomial, tpoly in module_polynomial.items():
        for degree, coefficient in tpoly.items():
            powers = dict(monomial)
            if degree:
                powers["t"] = degree
            key = canonical(powers)
            result[key] = result.get(key, Fraction(0)) + coefficient
    return {key: value for key, value in result.items() if value}


def dehom_a1(polynomial: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for monomial, coefficient in polynomial.items():
        powers = dict(monomial)
        powers.pop("a1", None)
        key = canonical(powers)
        result[key] = result.get(key, Fraction(0)) + coefficient
    return {key: value for key, value in result.items() if value}


def split_top(expression: str, separator: str) -> list[str]:
    pieces = []
    depth = 0
    start = 0
    for index, character in enumerate(expression):
        if character == "(":
            depth += 1
        elif character == ")":
            depth -= 1
            if depth < 0:
                fail(("unbalanced expression", expression))
        elif character == separator and depth == 0:
            pieces.append(expression[start:index])
            start = index + 1
    if depth:
        fail(("unbalanced expression", expression))
    pieces.append(expression[start:])
    return pieces


def additive_terms(expression: str) -> list[str]:
    terms = []
    depth = 0
    start = 0
    for index, character in enumerate(expression):
        if character == "(":
            depth += 1
        elif character == ")":
            depth -= 1
        elif character in "+-" and index > start and depth == 0:
            terms.append(expression[start:index])
            start = index
    if depth:
        fail(("unbalanced additive expression", expression))
    terms.append(expression[start:])
    return [term for term in terms if term]


def parse_scalar(token: str) -> tuple[Fraction, int]:
    match = re.fullmatch(r"([+-]?\d+)(?:/(.+))?", token)
    if match is None:
        fail(("unsupported Laurent scalar", token))
    numerator = int(match.group(1))
    denominator = match.group(2)
    integer_denominator = 1
    t_denominator = 0
    if denominator is not None:
        if denominator.startswith("(") and denominator.endswith(")"):
            denominator = denominator[1:-1]
        for factor in denominator.split("*"):
            if factor.isdigit():
                integer_denominator *= int(factor)
            elif factor == "t":
                t_denominator += 1
            else:
                power = re.fullmatch(r"t\^(\d+)", factor)
                if power is None:
                    fail(("unsupported Laurent denominator", token, factor))
                t_denominator += int(power.group(1))
    return Fraction(numerator, integer_denominator), -t_denominator


def parse_laurent(path: Path) -> Polynomial:
    expression = path.read_text().strip().replace(" ", "")
    if expression == "0":
        return {}
    result: Polynomial = {}
    for term in additive_terms(expression):
        factors = split_top(term, "*")
        coefficient, t_exponent = parse_scalar(factors[0])
        powers: dict[str, int] = {}
        if t_exponent:
            powers["t"] = t_exponent
        for factor in factors[1:]:
            variable = re.fullmatch(r"([A-Za-z_][A-Za-z_0-9]*)(?:\^(\d+))?", factor)
            if variable is None:
                fail(("unsupported Laurent monomial factor", path.name, factor))
            name = variable.group(1)
            exponent = int(variable.group(2) or 1)
            powers[name] = powers.get(name, 0) + exponent
        key = canonical(powers)
        value = result.get(key, Fraction(0)) + coefficient
        if value:
            result[key] = value
        else:
            result.pop(key, None)
    return result


def scale_clear(polynomial: Polynomial, scalar: int, t_power: int) -> Polynomial:
    result: Polynomial = {}
    for monomial, coefficient in polynomial.items():
        powers = dict(monomial)
        powers["t"] = powers.get("t", 0) + t_power
        if powers["t"] < 0:
            fail(("insufficient t clearing", monomial, t_power))
        key = canonical(powers)
        value = coefficient * scalar
        if value.denominator != 1:
            fail(("insufficient rational clearing", coefficient, scalar))
        result[key] = value
    return result


def divide_content(polynomial: Polynomial, content: int) -> Polynomial:
    result = {monomial: coefficient / content for monomial, coefficient in polynomial.items()}
    if any(value.denominator != 1 for value in result.values()):
        fail(("nonintegral content division", content))
    return result


def sigma_weight(parser, monomial: Monomial) -> int:
    return sum((0 if name == "t" else parser.sigma_weight(name)) * exponent
               for name, exponent in monomial)


def encode_polynomial(polynomial: Polynomial):
    return [
        {"monomial": [[name, exponent] for name, exponent in monomial],
         "coefficient": [coefficient.numerator, coefficient.denominator]}
        for monomial, coefficient in sorted(polynomial.items())
    ]


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    args = cli.parse_args()
    tag = require_aws()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)

    if digest(G3_RESULT) != G3_RESULT_SHA256:
        fail("G3 result hash")
    verify_freeze()
    if digest(G3_COMPILER_RESULT) != G3_COMPILER_RESULT_SHA256:
        fail("G3 compiler-result hash")
    if digest(G3_SCRIPT) != G3_SCRIPT_SHA256:
        fail("G3 Singular-script hash")
    stdout = G3_STDOUT.read_text()
    for marker in (
        "V43G3_LIFTSTD_BASIS_REPLAY=1",
        "V43G3_NONZERO_MULTIPLIERS=11",
        "V43G3_GENERIC_UNIT_REPLAY=1",
        "PASS_A1_GENERIC_QT_LIFT_V43G3",
    ):
        if stdout.count(marker) != 1:
            fail(("G3 stdout marker", marker))

    compiler = json.loads(G3_COMPILER_RESULT.read_text())
    if (
        compiler.get("status") != "PASS-A1-GENERIC-QT-LIFT-V43G3-COMPILER"
        or compiler.get("g2_ring_and_all_58_entries_byte_equal") is not True
        or compiler.get("reduced_row_count") != 58
        or len(compiler.get("reduced_variables", [])) != 64
        or compiler.get("pivot_source_row") != "Tg19_2"
        or compiler.get("pivot_multiplier") != "0 in the reconstructed 59-row identity"
    ):
        fail("G3 compiler contract")

    source = load(V43, V43_SHA256, "v43g4_source")
    (parser, _, total_rows, frozen_hashes, total_hashes, variables,
     frozen_variables, general_only, nonzero_general) = source.reconstruct_rows()
    if (len(total_rows), len(variables), len(frozen_variables), general_only) != (59, 66, 65, ["ez9"]):
        fail("literal source census")
    by_name = {item["name"]: item for item in total_rows}
    selected = compiler["reduced_rows"]
    if len(selected) != 58 or "Tg19_2" in selected:
        fail("reduced source map")
    if compiler["reduced_row_sha256"] != {name: total_hashes[name] for name in selected}:
        fail("reduced row hashes")

    multiplier_paths = [G3_AWS / "compiled" / Path(path).name
                        for path in compiler["multiplier_paths"]]
    if len(multiplier_paths) != 58 or not all(path.is_file() for path in multiplier_paths):
        fail("multiplier path census")
    multipliers = [parse_laurent(path) for path in multiplier_paths]
    support = [name for name, multiplier in zip(selected, multipliers) if multiplier]
    if len(support) != 11:
        fail(("multiplier support", support))

    total_source_rows = [ordinary_t_polynomial(by_name[name]["polynomial"]) for name in selected]
    dehom_rows = [dehom_a1(row) for row in total_source_rows]
    raw_replay: Polynomial = {}
    for multiplier, row in zip(multipliers, dehom_rows):
        add_scaled(raw_replay, multiply(multiplier, row))
    if raw_replay != {(): Fraction(1)}:
        fail(("raw Q(t) replay", len(raw_replay)))

    rational_lcm = reduce(lcm, (coefficient.denominator
                                for multiplier in multipliers
                                for coefficient in multiplier.values()), 1)
    minimum_t = min((dict(monomial).get("t", 0)
                     for multiplier in multipliers
                     for monomial in multiplier), default=0)
    t_valuation = max(0, -minimum_t)
    cleared = [scale_clear(multiplier, rational_lcm, t_valuation)
               for multiplier in multipliers]
    integer_coefficients = [abs(coefficient.numerator)
                            for multiplier in cleared
                            for coefficient in multiplier.values()]
    content = reduce(gcd, [rational_lcm, *integer_coefficients])
    if content <= 0:
        fail(("content", content))
    primitive = [divide_content(multiplier, content) for multiplier in cleared]
    unit_scalar = rational_lcm // content
    target_dehom: Polynomial = {canonical({"t": t_valuation}): Fraction(unit_scalar)}
    cleared_replay: Polynomial = {}
    for multiplier, row in zip(primitive, dehom_rows):
        add_scaled(cleared_replay, multiply(multiplier, row))
    if cleared_replay != target_dehom:
        fail(("cleared polynomial replay", len(cleared_replay), target_dehom))

    projected = []
    dropped_terms = 0
    levels = []
    for name, multiplier in zip(selected, primitive):
        grade = int(by_name[name]["grade"])
        keep: Polynomial = {}
        for monomial, coefficient in multiplier.items():
            total_weight = grade + sigma_weight(parser, monomial)
            if total_weight % 5 == 0:
                keep[monomial] = coefficient
                levels.append(total_weight // 5)
            else:
                dropped_terms += 1
        projected.append(keep)
    projected_replay: Polynomial = {}
    for multiplier, row in zip(projected, dehom_rows):
        add_scaled(projected_replay, multiply(multiplier, row))
    if projected_replay != target_dehom or not levels:
        fail(("sigma-residue projection replay", len(projected_replay), dropped_terms))

    exponent = max(levels)
    homogeneous = []
    for name, multiplier in zip(selected, projected):
        grade = int(by_name[name]["grade"])
        lifted: Polynomial = {}
        for monomial, coefficient in multiplier.items():
            total_weight = grade + sigma_weight(parser, monomial)
            deficit = exponent - total_weight // 5
            if deficit < 0 or total_weight % 5:
                fail(("homogenizing deficit", name, monomial, total_weight, exponent))
            powers = dict(monomial)
            if deficit:
                powers["a1"] = powers.get("a1", 0) + deficit
            key = canonical(powers)
            lifted[key] = lifted.get(key, Fraction(0)) + coefficient
        homogeneous.append({key: value for key, value in lifted.items() if value})
    total_replay: Polynomial = {}
    for multiplier, row in zip(homogeneous, total_source_rows):
        add_scaled(total_replay, multiply(multiplier, row))
    target_total = {canonical({"t": t_valuation, "a1": exponent}): Fraction(unit_scalar)}
    if total_replay != target_total:
        fail(("honest total replay", len(total_replay), target_total))

    used = [index for index, multiplier in enumerate(homogeneous) if multiplier]
    mutation_index = used[-1]
    mutation_monomial = sorted(total_source_rows[mutation_index])[0]
    mutation_residual = multiply(homogeneous[mutation_index], {mutation_monomial: Fraction(1)})
    if not mutation_residual:
        fail("corrupted-row negative control")

    cleared_paths = {}
    homogeneous_paths = {}
    for name, dehom_multiplier, total_multiplier in zip(selected, primitive, homogeneous):
        dehom_path = output / f"cleared_dehom_multiplier_{name}.poly"
        total_path = output / f"total_homogeneous_multiplier_{name}.poly"
        dehom_path.write_text(parser.polynomial_text(dehom_multiplier) + "\n")
        total_path.write_text(parser.polynomial_text(total_multiplier) + "\n")
        cleared_paths[name] = {"path": str(dehom_path), "sha256": digest(dehom_path)}
        homogeneous_paths[name] = {"path": str(total_path), "sha256": digest(total_path)}

    certificate = {
        "identity": f"{unit_scalar}*t^{t_valuation}*a1^{exponent}=sum_i H_i*Tg_i",
        "coefficient_field": "Q",
        "polynomial_ring": "Q[t,X19_total], t maps to rho^2",
        "t_valuation": t_valuation,
        "q_t": unit_scalar,
        "q_at_zero": unit_scalar,
        "a1_exponent": exponent,
        "pivot_row": "Tg19_2",
        "pivot_multiplier": [],
        "used_rows": [selected[index] for index in used],
        "multipliers": {name: encode_polynomial(multiplier)
                        for name, multiplier in zip(selected, homogeneous) if multiplier},
    }
    certificate_path = output / "generic_total_t_certificate.json"
    certificate_path.write_text(json.dumps(certificate, sort_keys=True,
                                           separators=(",", ":")) + "\n")
    result = {
        "status": "PASS-A1-GENERIC-REHOM-V43G4",
        "registered_aws_lane": tag,
        "raw_qt_replay": "sum C_i*Tg_i(1)=1",
        "cleared_dehom_identity": f"{unit_scalar}*t^{t_valuation}=sum D_i*Tg_i(1)",
        "honest_total_identity": f"{unit_scalar}*t^{t_valuation}*a1^{exponent}=sum H_i*Tg_i",
        "t_means": "rho^2",
        "rational_denominator_lcm": rational_lcm,
        "t_denominator_exponent": t_valuation,
        "integer_content_removed": content,
        "q_t": unit_scalar,
        "q_at_zero": unit_scalar,
        "a1_exponent": exponent,
        "product_levels": sorted(set(levels)),
        "sigma_projection_dropped_terms": dropped_terms,
        "source_row_count": 59,
        "reduced_row_count": 58,
        "pivot_row": "Tg19_2",
        "pivot_multiplier": "0",
        "used_rows": [selected[index] for index in used],
        "used_row_count": len(used),
        "raw_multiplier_term_counts": {name: len(multiplier)
                                       for name, multiplier in zip(selected, multipliers)},
        "cleared_multiplier_paths": cleared_paths,
        "homogeneous_multiplier_paths": homogeneous_paths,
        "certificate_path": str(certificate_path),
        "certificate_sha256": digest(certificate_path),
        "g3_freeze_sha256": G3_FREEZE_SHA256,
        "g3_compiler_result_sha256": G3_COMPILER_RESULT_SHA256,
        "g3_singular_script_sha256": G3_SCRIPT_SHA256,
        "preregistration_sha256": digest(PREREG),
        "corrupted_row": selected[mutation_index],
        "corrupted_monomial": [[name, exponent] for name, exponent in mutation_monomial],
        "corrupted_residual_term_count": len(mutation_residual),
        "corrupted_residual_sha256": sha256(json.dumps(
            encode_polynomial(mutation_residual), sort_keys=True,
            separators=(",", ":")).encode()).hexdigest(),
        "promotion_gate": ("requires special-certificate converter because t-valuation is positive"
                           if t_valuation else "q(0) is already nonzero"),
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(f"V43G4_DENOMINATOR={rational_lcm}*t^{t_valuation}")
    print(f"V43G4_CONTENT_REMOVED={content}")
    print(f"V43G4_PRODUCT_LEVELS={','.join(map(str, sorted(set(levels))))}")
    print(f"V43G4_TOTAL_IDENTITY={unit_scalar}*t^{t_valuation}*a1^{exponent}")
    print(f"V43G4_USED_ROWS={len(used)}")
    print("PASS-A1-GENERIC-REHOM-V43G4")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
