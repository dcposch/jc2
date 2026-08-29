#!/usr/bin/env python3
"""Compile one complete residual a8/a9 D1 grade-38 R3 cell; AWS only."""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
import importlib.util
from itertools import product
import json
import math
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
R3_PATH = ROOT / "cases/max12_812_order2_square_owner_d1_age10_j38_odd_recurrence3_20260826/compile_age10_j38_r3.py"
R3_FREEZE = ROOT / "cases/max12_812_order2_square_owner_d1_age10_j38_odd_recurrence3_20260826/PRODUCER_FREEZE.sha256"
UNIVERSAL_PROMOTION = ROOT / "xmodel/max12-812-order2-square-universal-odd-pole-recurrence-promotion-20260826.md"
UNIVERSAL_REVIEW = ROOT / "xmodel/max12-812-order2-square-d1-universal-odd-pole-recurrence-hostile-review-grok-20260826.md"
PINS = {
    R3_PATH: "9f0184b1007103478381c474ce6e4c1802ed8a53ab23dee79e7dd77518e0168e",
    R3_FREEZE: "60b2e1d52156f0648f7f39739f06c139d7d274c28fe4147eaba8d7213dfc2f0b",
    UNIVERSAL_PROMOTION: "dbdd2b805e4cf224303474f733cde4553b5cb554be9ccadf05610c30521987f2",
    UNIVERSAL_REVIEW: "0263315e1df7f6044870e6c8fec26f36fe4d6860e44bb015e2ab903bcfae1a7e",
}
MAXIMUM = 38
LOCAL_ATOMS = (
    {"fixed": 2, "denominator": 2, "R": 1, "A": 0, "C": 0, "scalar": 2},
    {"fixed": 4, "denominator": 4, "R": 2, "A": 0, "C": 0, "scalar": 1},
    {"fixed": 5, "denominator": 3, "R": 0, "A": 1, "C": 0, "scalar": 1},
    {"fixed": 5, "denominator": 4, "R": 0, "A": 0, "C": 1, "scalar": 1},
)
LOCAL_SUMMANDS = (
    {"name": "unloaded", "load": None, "alpha": Fraction(3, 2), "fixed": 0},
    {"name": "k10", "load": "k10", "alpha": Fraction(5, 4), "fixed": 4},
    {"name": "k6", "load": "k6", "alpha": Fraction(3, 4), "fixed": 12},
    {"name": "k2", "load": "k2", "alpha": Fraction(1, 4), "fixed": 20},
)
CELLS = {
    (8, 3): {"c": 11, "r": 8, "count": 17, "first_pole4": 41,
             "maxima": {"A": 9, "C": 10, "R": 8, "k10": 8, "k6": 10, "k2": 8, "p": 10,
                        "mu20": 10, "mu4": 6, "mu6": 2}},
    (9, 2): {"c": 11, "r": 9, "count": 13, "first_pole4": 42,
             "maxima": {"A": 8, "C": 10, "R": 7, "k10": 7, "k6": 10, "k2": 7, "p": 10,
                        "mu20": 10, "mu4": 6, "mu6": 2}},
    (9, 3): {"c": 12, "r": 9, "count": 13, "first_pole4": 43,
             "maxima": {"A": 7, "C": 9, "R": 7, "k10": 6, "k6": 9, "k2": 7, "p": 9,
                        "mu20": 10, "mu4": 6, "mu6": 2}},
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("cannot import", str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only residual tail compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only residual tail compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def binomial(alpha: Fraction, degree: int) -> Fraction:
    answer = Fraction(1)
    for index in range(degree):
        answer *= alpha - index
    return answer / math.factorial(degree)


def enumerate_primitives(baseline: dict[str, int], maximum: int, pad: int = 0):
    """Cost-bounded independent expansion of all four source summands."""
    aggregate: defaultdict[tuple[object, ...], Fraction] = defaultdict(Fraction)
    for summand in LOCAL_SUMMANDS:
        budget = maximum - int(summand["fixed"])
        if budget < 0:
            continue
        costs = [
            int(atom["fixed"])
            + baseline["R"] * int(atom["R"])
            + baseline["A"] * int(atom["A"])
            + baseline["C"] * int(atom["C"])
            for atom in LOCAL_ATOMS
        ]
        if any(cost <= 0 for cost in costs):
            fail(("nonpositive atom cost", baseline, costs))
        bounds = [budget // cost + pad for cost in costs]
        alpha = summand["alpha"]
        for counts in product(*(range(bound + 1) for bound in bounds)):
            degree = sum(counts)
            if degree == 0:
                continue
            fixed = int(summand["fixed"])
            denominator = 0
            exponents = {"R": 0, "A": 0, "C": 0}
            scalar = 1
            for count, atom in zip(counts, LOCAL_ATOMS):
                fixed += count * int(atom["fixed"])
                denominator += count * int(atom["denominator"])
                scalar *= int(atom["scalar"]) ** count
                for stem in exponents:
                    exponents[stem] += count * int(atom[stem])
            grade = fixed + sum(baseline[stem] * exponents[stem] for stem in exponents)
            if grade > maximum:
                continue
            pole = denominator - int(4 * alpha)
            if pole <= 0:
                continue
            multinomial = math.factorial(degree)
            for count in counts:
                multinomial //= math.factorial(count)
            coefficient = binomial(alpha, degree) * multinomial * scalar
            key = (summand["name"], summand["load"], fixed,
                   exponents["R"], exponents["A"], exponents["C"], pole)
            aggregate[key] += coefficient
    result = []
    for key, coefficient in aggregate.items():
        if coefficient == 0:
            continue
        name, load_name, fixed, eR, eA, eC, pole = key
        grade = fixed + baseline["R"] * eR + baseline["A"] * eA + baseline["C"] * eC
        result.append({"name": name, "load": load_name, "fixed_sigma": fixed,
                       "R": eR, "A": eA, "C": eC, "pole": pole,
                       "base_grade": grade, "coefficient": fraction_text(coefficient)})
    return sorted(result, key=lambda item: (
        int(item["base_grade"]), str(item["name"]), int(item["pole"]),
        int(item["R"]), int(item["A"]), int(item["C"]),
    ))


def primitive_signature(item) -> tuple:
    return tuple(item[key] for key in (
        "name", "load", "fixed_sigma", "R", "A", "C", "pole", "coefficient", "base_grade"
    ))


def derive_maxima(primitives) -> dict[str, int]:
    maxima = {name: 0 for name in ("A", "C", "R", "k10", "k6", "k2", "p")}
    for item in primitives:
        remaining = MAXIMUM - int(item["base_grade"])
        for stem in ("A", "C", "R"):
            if int(item[stem]):
                maxima[stem] = max(maxima[stem], remaining)
        if item["load"] is not None:
            maxima[str(item["load"])] = max(maxima[str(item["load"])], remaining)
        maxima["p"] = max(maxima["p"], remaining)
    maxima.update(mu20=10, mu4=6, mu6=2)
    return maxima


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65519, 65521), required=True)
    parser.add_argument("--a", type=int, choices=(8, 9), required=True)
    parser.add_argument("--d", type=int, choices=(2, 3), required=True)
    args = parser.parse_args()
    key = (args.a, args.d)
    if key not in CELLS:
        fail(("cell outside preregistration", key))
    tag = require_aws()
    for path, expected in PINS.items():
        actual = digest(path)
        if actual != expected:
            fail(("frozen pin mismatch", str(path), actual, expected))

    r3 = load(R3_PATH, "d1_residual_tail_r3_parent")
    if tuple(r3.ATOMS) != LOCAL_ATOMS or tuple(r3.SUMMANDS) != LOCAL_SUMMANDS:
        fail("independently frozen atom/summand model disagrees with promoted R3 producer")
    for path, expected in r3.PINS.items():
        actual = digest(path)
        if actual != expected:
            fail(("frozen transitive pin mismatch", str(path), actual, expected))
    spec = CELLS[key]
    baseline = {"A": args.a, "C": int(spec["c"]), "R": int(spec["r"])}
    primitives = enumerate_primitives(baseline, MAXIMUM)
    padded1 = enumerate_primitives(baseline, MAXIMUM, pad=1)
    padded2 = enumerate_primitives(baseline, MAXIMUM, pad=2)
    signatures = {primitive_signature(item) for item in primitives}
    if signatures != {primitive_signature(item) for item in padded1} or signatures != {
        primitive_signature(item) for item in padded2
    }:
        fail("cost-bounded padded primitive mismatch")
    if len(primitives) != int(spec["count"]):
        fail(("primitive count", len(primitives), spec["count"]))
    if max(int(item["pole"]) for item in primitives) != 3:
        fail(("grade38 pole ceiling", primitives))
    extended = enumerate_primitives(baseline, 60)
    first_pole4 = min(int(item["base_grade"]) for item in extended if int(item["pole"]) >= 4)
    if first_pole4 != int(spec["first_pole4"]):
        fail(("first pole-four wall", first_pole4, spec["first_pole4"]))
    maxima = derive_maxima(primitives)
    if maxima != spec["maxima"]:
        fail(("mechanical jet maxima", maxima, spec["maxima"]))

    analytic, literal = r3.inventory_monomials(primitives, maxima)
    literal_variables = {
        str(variable) for item in literal for variable in item["variables"]
    }
    licensed_source_jets = {"p"}
    licensed_source_jets.update(f"ell{index}" for index in range(1, maxima["p"] + 1))
    for stem, ceiling in (("a1", maxima["A"]), ("a0", maxima["A"]),
                          ("c1", maxima["C"]), ("c0", maxima["C"]),
                          ("b1", maxima["R"]), ("b0", maxima["R"]),
                          ("k0", maxima["k10"]), ("k60", maxima["k6"]),
                          ("k20", maxima["k2"])):
        licensed_source_jets.update(r3.jet_name(stem, index) for index in range(ceiling + 1))
    missing_source_jets = sorted(licensed_source_jets - literal_variables)
    if missing_source_jets:
        fail(("licensed source jets absent from literal grade38 inventory", missing_source_jets))
    licensed_target_jets = (
        [r3.jet_name("mu20", index) for index in range(maxima["mu20"] + 1)]
        + [r3.jet_name("mu4", index) for index in range(maxima["mu4"] + 1)]
        + [r3.jet_name("mu6", index) for index in range(maxima["mu6"] + 1)]
        + ["J"]
    )
    high_variables = {
        "A": f"a1_{maxima['A']}", "C": f"c1_{maxima['C']}",
        "R": f"b1_{maxima['R']}", "k10": f"k0_{maxima['k10']}",
        "k6": f"k60_{maxima['k6']}", "k2": f"k20_{maxima['k2']}",
        "p": f"ell{maxima['p']}",
    }
    for stem, variable in high_variables.items():
        if not any(int(item["grade"]) == MAXIMUM and variable in item["variables"] for item in literal):
            fail(("mechanical maximum missing at grade38", stem, variable))

    parent = r3.load_parent()
    high_parent = parent.load_parent()
    source_base, tail_base, tails = high_parent.ancestry()
    output = args.output.resolve()
    if output.exists():
        fail("residual tail output already exists")
    output.mkdir(parents=True)
    cell = f"A{args.a}D{args.d}"
    inventory = {
        "status": f"COMPLETE-D1-{cell}-THROUGH-GRADE38",
        "derivation": "independent cost-bounded expansion of all four source summands",
        "baseline": baseline,
        "r_tail": f"R={args.a}+s via eta=sigma^s, s>=0",
        "maximum_grade": MAXIMUM,
        "primitive_families": primitives,
        "primitive_family_count": len(primitives),
        "maximum_pole_through_grade38": 3,
        "first_pole_order_at_least_four_grade": first_pole4,
        "jet_maxima": maxima,
        "high_jet_grade38_sentinels": high_variables,
        "analytic_monomials": analytic,
        "literal_faber_source_monomials": literal,
        "licensed_source_jets": sorted(licensed_source_jets),
        "licensed_target_jets": licensed_target_jets,
        "targets": [
            {"row": 2, "grade": 28 + index, "variable": r3.jet_name("mu20", index), "coefficient": "-1"}
            for index in range(maxima["mu20"] + 1)
        ] + [
            {"row": 4, "grade": 32 + index, "variable": r3.jet_name("mu4", index), "coefficient": "-1"}
            for index in range(maxima["mu4"] + 1)
        ] + [
            {"row": 6, "grade": 36 + index, "variable": r3.jet_name("mu6", index), "coefficient": "-1"}
            for index in range(maxima["mu6"] + 1)
        ] + [{"row": 7, "grade": 38, "variable": "J", "coefficient": "-1/4"}],
    }
    inventory_path = output / "source_inventory.json"
    inventory_path.write_text(json.dumps(inventory, sort_keys=True, indent=2) + "\n")
    inventory_sha = digest(inventory_path)

    variables = ["z", "t", "sigma", "p"]
    variables += [f"ell{index}" for index in range(1, maxima["p"] + 1)]
    variables += ["eta"]
    for stem in ("a1", "a0"):
        variables += [r3.jet_name(stem, index) for index in range(maxima["A"] + 1)]
    for stem in ("c1", "c0"):
        variables += [r3.jet_name(stem, index) for index in range(maxima["C"] + 1)]
    for stem in ("b1", "b0"):
        variables += [r3.jet_name(stem, index) for index in range(maxima["R"] + 1)]
    variables += [r3.jet_name("k0", index) for index in range(maxima["k10"] + 1)]
    variables += [r3.jet_name("k60", index) for index in range(maxima["k6"] + 1)]
    variables += [r3.jet_name("k20", index) for index in range(maxima["k2"] + 1)]
    variables += [r3.jet_name("mu20", index) for index in range(maxima["mu20"] + 1)]
    variables += [r3.jet_name("mu4", index) for index in range(maxima["mu4"] + 1)]
    variables += [r3.jet_name("mu6", index) for index in range(maxima["mu6"] + 1)]
    variables += ["J", "iJ"]
    pp = "p" + "".join(f"+2*sigma^{index}*ell{index}" for index in range(1, maxima["p"] + 1))
    normal = {
        "A": f"sigma^{args.a}*(({r3.series('a1', maxima['A'])})+t*({r3.series('a0', maxima['A'])}))",
        "C": f"sigma^{spec['c']}*(({r3.series('c1', maxima['C'])})+t*({r3.series('c0', maxima['C'])}))",
        "R": f"sigma^{spec['r']}*eta*(({r3.series('b1', maxima['R'])})+t*({r3.series('b0', maxima['R'])}))",
    }
    coeffs = source_base.source_coefficients(
        pp,
        f"sigma^{args.a}*({r3.series('a1', maxima['A'])})",
        f"sigma^{args.a}*({r3.series('a0', maxima['A'])})",
        f"sigma^{spec['c']}*({r3.series('c1', maxima['C'])})",
        f"sigma^{spec['c']}*({r3.series('c0', maxima['C'])})",
        f"sigma^{spec['r']}*eta*({r3.series('b1', maxima['R'])})",
        f"sigma^{spec['r']}*eta*({r3.series('b0', maxima['R'])})",
    )
    loads = {
        "k10": f"({r3.series('k0', maxima['k10'])})",
        "k6": f"({r3.series('k60', maxima['k6'])})",
        "k2": f"({r3.series('k20', maxima['k2'])})",
    }
    targets = {1: "0", 2: r3.series("mu20", maxima["mu20"]), 3: "0",
               4: r3.series("mu4", maxima["mu4"]), 5: "0",
               6: r3.series("mu6", maxima["mu6"]), 7: "J/4"}
    source_rows = {}
    full_rows = {}
    for row in range(1, 8):
        source = tail_base.tail_text(tails[str(row)], row, coeffs, loads).replace("Lambda", "(sigma^2)")
        source_rows[row] = source
        full_rows[row] = source if targets[row] == "0" else f"({source})-sigma^{2*(12+row)}*({targets[row]})"

    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target_path = output / f"square_d1_{cell.lower()}_j38_r3_{label}.sing"
    prefix = f"D1{cell}J38R3"
    lines = [
        f"ring R={args.characteristic},({','.join(variables)}),dp;",
        f'print("{prefix}_SOURCE_HASHES=PASS");',
        f'print("{prefix}_INVENTORY_SHA256={inventory_sha}");',
        f'print("{prefix}_PRIMITIVE_FAMILY_COUNT={len(primitives)}");',
        f'print("{prefix}_MAX_POLE_THROUGH_G38=3");',
        f'print("{prefix}_FIRST_POLE4_GRADE={first_pole4}");',
        f'print("{prefix}_ANALYTIC_MONOMIAL_COUNT={len(analytic)}");',
        f'print("{prefix}_LITERAL_MONOMIAL_COUNT={len(literal)}");',
        f'print("{prefix}_ALL_LICENSED_SOURCE_JETS_IN_INVENTORY=1");',
        f'print("{prefix}_LICENSED_SOURCE_JET_COUNT={len(licensed_source_jets)}");',
        f'print("{prefix}_LICENSED_TARGET_JET_COUNT={len(licensed_target_jets)}");',
        f"ideal {prefix}_S38=std(ideal(sigma^38)); ideal {prefix}_S39=std(ideal(sigma^39));",
    ]
    for row in range(1, 8):
        lines += [f"poly {prefix}_SourcePhi{row}={source_rows[row]};",
                  f"poly {prefix}_FullPhi{row}={full_rows[row]};"]
    lines += [
        f"poly {prefix}_sp=({pp})/2;",
        f"poly {prefix}_Inv1={r3.inverse_series(prefix+'_sp', 1)};",
        f"poly {prefix}_Inv2={r3.inverse_series(prefix+'_sp', 2)};",
        f"poly {prefix}_Inv3={r3.inverse_series(prefix+'_sp', 3)};",
    ]
    hterms = []
    for item in primitives:
        factors = [r3.singular_fraction(str(item["coefficient"])), f"sigma^{item['fixed_sigma']}"]
        if item["load"] is not None:
            factors.append(loads[str(item["load"])])
        for stem in ("R", "A", "C"):
            exponent = int(item[stem])
            if exponent == 1:
                factors.append(f"({normal[stem]})")
            elif exponent > 1:
                factors.append(f"({normal[stem]})^{exponent}")
        numerator_degree = int(item["R"]) + int(item["A"]) + int(item["C"])
        tpower = 2 * int(item["pole"]) - numerator_degree + 1
        if tpower:
            factors.append("t" if tpower == 1 else f"t^{tpower}")
        factors.append(f"{prefix}_Inv{item['pole']}")
        hterms.append("*".join(factors))
    lines += [f"poly {prefix}_H=" + "+".join(hterms) + ";", f"poly {prefix}_D0={prefix}_H;"]
    for derivative in range(1, 9):
        lines.append(f"poly {prefix}_D{derivative}=diff({prefix}_D{derivative-1},t);")
        if derivative >= 2:
            row = derivative - 1
            lines.append(f"poly {prefix}_h{row}=subst({prefix}_D{derivative},t,0)/{math.factorial(derivative)};")
    for row in range(1, 8):
        terms = []
        for source_row in range(1, row + 1):
            coefficient = r3.faber_transform_coefficient(row, source_row)
            if not coefficient:
                continue
            degree = (row - source_row) // 2
            factor = r3.singular_fraction(r3.fraction_text(coefficient))
            if degree:
                factor += f"*(({pp})^{degree})"
            terms.append(f"({factor})*{prefix}_h{source_row}")
        lines.append(f"poly {prefix}_PredPhi{row}=" + "+".join(terms) + ";")
    for row in range(1, 8):
        lines.append(f"int {prefix}_bridge{row}=(reduce({prefix}_SourcePhi{row}-{prefix}_PredPhi{row},{prefix}_S39)==0);")
    bridge_product = "*".join(f"{prefix}_bridge{row}" for row in range(1, 8))
    lines += [f"int {prefix}_full_bridge={bridge_product};",
              f'print("{prefix}_ALL_SEVEN_SOURCE_ROWS_BRIDGED="+string({prefix}_full_bridge));']
    target_checks = []
    for row, stem, ceiling, base_grade in (
        (2, "mu20", maxima["mu20"], 28),
        (4, "mu4", maxima["mu4"], 32),
        (6, "mu6", maxima["mu6"], 36),
    ):
        for index in range(ceiling + 1):
            variable = r3.jet_name(stem, index)
            check = f"{prefix}_target_{stem}_{index}"
            grade = base_grade + index
            lines += [
                f"poly {check}_d=diff({prefix}_FullPhi{row},{variable});",
                f"int {check}=(reduce({check}_d+sigma^{grade},{prefix}_S39)==0);",
            ]
            target_checks.append(check)
    lines += [
        f"poly {prefix}_target_J_d=diff({prefix}_FullPhi7,J);",
        f"int {prefix}_target_J=(reduce({prefix}_target_J_d+(sigma^38)/4,{prefix}_S39)==0);",
    ]
    target_checks.append(f"{prefix}_target_J")
    target_product = "*".join(target_checks)
    lines += [
        f"int {prefix}_all_targets={target_product};",
        f'print("{prefix}_ALL_LICENSED_TARGET_JETS_RETAINED="+string({prefix}_all_targets));',
    ]
    for stem, variable in high_variables.items():
        marker = stem.upper()
        lines.append(f"int {prefix}_{marker}_max_enters=0;")
        for row in range(1, 8):
            lines += [
                f"poly {prefix}_{marker}_d{row}=diff({prefix}_SourcePhi{row},{variable});",
                f"if (reduce({prefix}_{marker}_d{row},{prefix}_S38)==0) {{",
                f" poly {prefix}_{marker}_q{row}={prefix}_{marker}_d{row}/sigma^38;",
                f" if (subst({prefix}_{marker}_q{row},sigma,0)!=0) {{ {prefix}_{marker}_max_enters=1; }}",
                "}",
            ]
    high_product = "*".join(f"{prefix}_{stem.upper()}_max_enters" for stem in high_variables)
    lines += [
        f"int {prefix}_all_maxima_enter={high_product};",
        f'print("{prefix}_ALL_MECHANICAL_JET_MAXIMA_ENTER_G38="+string({prefix}_all_maxima_enter));',
        f"poly {prefix}_source_rel={prefix}_SourcePhi7+(({pp})/4)*{prefix}_SourcePhi5+(3*(({pp})^2)/32)*{prefix}_SourcePhi3+(5*(({pp})^3)/128)*{prefix}_SourcePhi1;",
        f"poly {prefix}_full_rel={prefix}_FullPhi7+(({pp})/4)*{prefix}_FullPhi5+(3*(({pp})^2)/32)*{prefix}_FullPhi3+(5*(({pp})^3)/128)*{prefix}_FullPhi1;",
        f"int {prefix}_source_mod39=(reduce({prefix}_source_rel,{prefix}_S39)==0);",
        f"int {prefix}_eta_safe=(reduce(diff({prefix}_source_rel,eta),{prefix}_S39)==0);",
        f"int {prefix}_div38=(reduce({prefix}_full_rel,{prefix}_S38)==0);",
        f"poly {prefix}_q38={prefix}_full_rel/sigma^38;",
        f"int {prefix}_coeff=(subst({prefix}_q38,sigma,0)+J/4==0);",
        f"int {prefix}_full_mod39=(reduce({prefix}_full_rel+sigma^38*J/4,{prefix}_S39)==0);",
        f"ideal {prefix}_unit=std(ideal(subst({prefix}_q38,sigma,0),iJ*J-1));",
        f"int {prefix}_exact_J_unit=(reduce(1,{prefix}_unit)==0);",
        f'print("{prefix}_SOURCE_R3_MOD_G39="+string({prefix}_source_mod39));',
        f'print("{prefix}_ETA_RTAIL_SAFE="+string({prefix}_eta_safe));',
        f'print("{prefix}_GRADE38_COEFFICIENT_MINUS_J_OVER_4="+string({prefix}_coeff));',
        f'print("{prefix}_FULL_R3_MOD_G39="+string({prefix}_full_mod39));',
        f'print("{prefix}_EXACT_DJ_UNIT="+string({prefix}_exact_J_unit));',
        f"int {prefix}_endpoint={prefix}_full_bridge*{prefix}_all_targets*{prefix}_all_maxima_enter*{prefix}_source_mod39*{prefix}_eta_safe*{prefix}_div38*{prefix}_coeff*{prefix}_full_mod39*{prefix}_exact_J_unit;",
        f'if ({prefix}_endpoint!=1) {{ print("{prefix}_FAIL=SOURCE_CEILING_BRIDGE_OR_R3"); quit; }}',
        f'print("{prefix}_ENDPOINT=PASS_EMPTY_A{args.a}_D{args.d}_RGE{args.a}_ON_DJ");',
        "quit;",
    ]
    target_path.write_text("\n".join(lines) + "\n")
    payload = {
        "status": f"PASS-D1-{cell}-J38-R3-COMPILER",
        "scope": f"A{args.a}_D{args.d}_C{spec['c']}_R_GE_{args.a}_ON_D_P_K0_J_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "input_sha256": digest(target_path),
        "inventory_sha256": inventory_sha,
        "primitive_family_count": len(primitives),
        "first_pole4_grade": first_pole4,
        "jet_maxima": maxima,
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
