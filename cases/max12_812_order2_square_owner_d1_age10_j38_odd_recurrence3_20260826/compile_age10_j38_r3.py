#!/usr/bin/env python3
"""Compile the full uniform D1 a>=10 order-three J38 recurrence; AWS only."""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
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
PARENT_DIR = ROOT / "cases/max12_812_order2_square_owner_d1_age13_j38_odd_recurrence_20260826"
PARENT = PARENT_DIR / "compile_age13_j38.py"
PINS = {
    PARENT: "246f6279b7801d21896936531c706dea3d22f42fa2c702f11eb6ec74e011bff5",
    PARENT_DIR / "REGISTRATION.md": "2dc25ae1ec6ddac96ce828254bc1895649144c729524882d0f735e9cdd13e5c0",
    PARENT_DIR / "FREEZE.sha256": "956090162a137a4afe3f4544f8d41c5622d38ec5627f1669f58a219c45a42358",
    PARENT_DIR / "RESULT.md": "09ca321436f4262b680801b74dc365cdff632c7630b65da50476547e5229139c",
    PARENT_DIR / "EVIDENCE.sha256": "0a65d8b2e792fc7e68e9a7aa17995a51b2eb38f09fe19845b77cbeb343757491",
}
MAXIMUM = 38
BASELINE = {"A": 10, "C": 11, "R": 10}
TARGET_BASE = {"mu20": 28, "mu4": 32, "mu6": 36}

# f=L^4(1+X), with these four independently enumerated summands of X.
ATOMS = (
    {"fixed": 2, "denominator": 2, "R": 1, "A": 0, "C": 0, "scalar": 2},
    {"fixed": 4, "denominator": 4, "R": 2, "A": 0, "C": 0, "scalar": 1},
    {"fixed": 5, "denominator": 3, "R": 0, "A": 1, "C": 0, "scalar": 1},
    {"fixed": 5, "denominator": 4, "R": 0, "A": 0, "C": 1, "scalar": 1},
)
SUMMANDS = (
    {"name": "unloaded", "load": None, "alpha": Fraction(3, 2), "fixed": 0},
    {"name": "k10", "load": "k10", "alpha": Fraction(5, 4), "fixed": 4},
    {"name": "k6", "load": "k6", "alpha": Fraction(3, 4), "fixed": 12},
    {"name": "k2", "load": "k2", "alpha": Fraction(1, 4), "fixed": 20},
)
EXPECTED_PRIMITIVES = {
    ("unloaded", 10, 0, 1, 1, 1, "3/4"),
    ("unloaded", 10, 0, 0, 2, 2, "3/8"),
    ("k10", 11, 1, 0, 1, 1, "5/8"),
    ("k10", 14, 0, 2, 0, 1, "5/32"),
    ("k10", 14, 0, 1, 1, 2, "5/16"),
    ("k10", 14, 0, 0, 2, 3, "5/32"),
    ("k6", 17, 0, 0, 1, 1, "3/4"),
    ("k6", 16, 2, 0, 0, 1, "3/8"),
    ("k2", 22, 1, 0, 0, 1, "1/2"),
    ("k2", 25, 0, 1, 0, 2, "1/4"),
    ("k2", 25, 0, 0, 1, 3, "1/4"),
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only a>=10 J38-R3 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only a>=10 J38-R3 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_parent():
    spec = importlib.util.spec_from_file_location("d1_j38_r3_parent", PARENT)
    if spec is None or spec.loader is None:
        fail("cannot import frozen a>=13 recurrence parent")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def binomial(alpha: Fraction, degree: int) -> Fraction:
    answer = Fraction(1)
    for index in range(degree):
        answer *= alpha - index
    return answer / math.factorial(degree)


def enumerate_primitives(maximum: int) -> list[dict[str, object]]:
    """Independently expand all four binomial summands at baseline a=10."""

    aggregate: defaultdict[tuple[object, ...], Fraction] = defaultdict(Fraction)
    for summand in SUMMANDS:
        alpha = summand["alpha"]
        assert isinstance(alpha, Fraction)
        for counts in product(range(6), repeat=len(ATOMS)):
            degree = sum(counts)
            if degree == 0:
                continue
            fixed = int(summand["fixed"])
            denominator = 0
            exponents = {"R": 0, "A": 0, "C": 0}
            scalar = 1
            for count, atom in zip(counts, ATOMS):
                fixed += count * int(atom["fixed"])
                denominator += count * int(atom["denominator"])
                scalar *= int(atom["scalar"]) ** count
                for stem in exponents:
                    exponents[stem] += count * int(atom[stem])
            grade = fixed + sum(BASELINE[stem] * exponents[stem] for stem in exponents)
            if grade > maximum:
                continue
            pole = denominator - int(4 * alpha)
            if pole <= 0:
                continue
            multinomial = math.factorial(degree)
            for count in counts:
                multinomial //= math.factorial(count)
            coefficient = binomial(alpha, degree) * multinomial * scalar
            key = (
                summand["name"], summand["load"], fixed,
                exponents["R"], exponents["A"], exponents["C"], pole,
            )
            aggregate[key] += coefficient
    primitives: list[dict[str, object]] = []
    for key, coefficient in aggregate.items():
        if coefficient == 0:
            continue
        name, load, fixed, rexponent, aexponent, cexponent, pole = key
        grade = (
            int(fixed) + BASELINE["R"] * int(rexponent)
            + BASELINE["A"] * int(aexponent) + BASELINE["C"] * int(cexponent)
        )
        primitives.append({
            "name": name, "load": load, "fixed_sigma": fixed,
            "R": rexponent, "A": aexponent, "C": cexponent,
            "pole": pole, "base_grade": grade,
            "coefficient": fraction_text(coefficient),
        })
    return sorted(primitives, key=lambda item: (
        int(item["base_grade"]), str(item["name"]), int(item["pole"]),
        int(item["R"]), int(item["A"]), int(item["C"]),
    ))


def primitive_signature(primitive: dict[str, object]) -> tuple[object, ...]:
    return (
        primitive["name"], primitive["fixed_sigma"], primitive["R"],
        primitive["A"], primitive["C"], primitive["pole"],
        primitive["coefficient"],
    )


def derive_jet_maxima(primitives: list[dict[str, object]]) -> dict[str, int]:
    maxima = {"A": 0, "C": 0, "R": 0, "k10": 0, "k6": 0, "k2": 0, "p": 0}
    for primitive in primitives:
        remaining = MAXIMUM - int(primitive["base_grade"])
        for stem in ("A", "C", "R"):
            if int(primitive[stem]):
                maxima[stem] = max(maxima[stem], remaining)
        load = primitive["load"]
        if load is not None:
            maxima[str(load)] = max(maxima[str(load)], remaining)
        maxima["p"] = max(maxima["p"], remaining)
    maxima.update({name: MAXIMUM - grade for name, grade in TARGET_BASE.items()})
    expected = {
        "A": 7, "C": 10, "R": 6, "k10": 6, "k6": 10, "k2": 6,
        "p": 10, "mu20": 10, "mu4": 6, "mu6": 2,
    }
    if maxima != expected:
        fail(("mechanical jet maxima mismatch", maxima, expected))
    return maxima


def jet_name(stem: str, index: int) -> str:
    return stem if index == 0 else f"{stem}_{index}"


def series(stem: str, maximum: int) -> str:
    return "+".join(
        jet_name(stem, index) if index == 0
        else f"sigma^{index}*{jet_name(stem, index)}"
        for index in range(maximum + 1)
    )


def repeated_normal_choices(stem: str, exponent: int, maximum: int):
    """Enumerate numerator component/jet monomials, retaining multiplicity."""

    if exponent == 0:
        return [((), 0, 0, Fraction(1))]
    choices = []
    for component in ("1", "0"):
        for index in range(maximum + 1):
            choices.append((jet_name(stem + component, index), index, component == "0"))
    aggregate: defaultdict[tuple[tuple[str, ...], int, int], Fraction] = defaultdict(Fraction)
    for selected in product(choices, repeat=exponent):
        variables = tuple(sorted(item[0] for item in selected))
        shift = sum(item[1] for item in selected)
        tpower = sum(int(item[2]) for item in selected)
        aggregate[(variables, shift, tpower)] += 1
    return [(variables, shift, tpower, value) for (variables, shift, tpower), value in aggregate.items()]


@lru_cache(maxsize=None)
def connection_choices(degree: int, maximum: int, doubled: bool):
    """Expand sp^degree (doubled=False) or pp^degree (doubled=True)."""

    if degree == 0:
        return (((), 0, Fraction(1)),)
    single = [("p", 0, Fraction(1) if doubled else Fraction(1, 2))]
    for index in range(1, maximum + 1):
        single.append((f"ell{index}", index, Fraction(2) if doubled else Fraction(1)))
    aggregate: defaultdict[tuple[tuple[str, ...], int], Fraction] = defaultdict(Fraction)
    for selected in product(single, repeat=degree):
        variables = tuple(sorted(item[0] for item in selected))
        shift = sum(item[1] for item in selected)
        coefficient = math.prod((item[2] for item in selected), start=Fraction(1))
        aggregate[(variables, shift)] += coefficient
    return tuple((variables, shift, value) for (variables, shift), value in aggregate.items())


def inventory_monomials(primitives: list[dict[str, object]], maxima: dict[str, int]):
    """Explicitly enumerate analytic and literal moving-row monomials."""

    analytic: list[dict[str, object]] = []
    for family_index, primitive in enumerate(primitives):
        base_grade = int(primitive["base_grade"])
        pole = int(primitive["pole"])
        degree = int(primitive["R"]) + int(primitive["A"]) + int(primitive["C"])
        base_t = 2 * pole - degree + 1
        normal_lists = [
            repeated_normal_choices("b", int(primitive["R"]), maxima["R"]),
            repeated_normal_choices("a", int(primitive["A"]), maxima["A"]),
            repeated_normal_choices("c", int(primitive["C"]), maxima["C"]),
        ]
        load = primitive["load"]
        load_choices = [(None, 0)] if load is None else [
            (jet_name({"k10": "k0", "k6": "k60", "k2": "k20"}[str(load)], index), index)
            for index in range(maxima[str(load)] + 1)
        ]
        coefficient0 = Fraction(str(primitive["coefficient"]))
        aggregate: defaultdict[tuple[object, ...], Fraction] = defaultdict(Fraction)
        for rchoice, achoice, cchoice in product(*normal_lists):
            normal_variables = tuple(sorted(rchoice[0] + achoice[0] + cchoice[0]))
            normal_shift = rchoice[1] + achoice[1] + cchoice[1]
            numerator_t = rchoice[2] + achoice[2] + cchoice[2]
            normal_coefficient = rchoice[3] * achoice[3] * cchoice[3]
            for load_variable, load_shift in load_choices:
                variables0 = normal_variables + (() if load_variable is None else (load_variable,))
                for inverse_degree in range(5):
                    inverse_coefficient = Fraction(
                        (-1) ** inverse_degree
                        * math.comb(pole + inverse_degree - 1, inverse_degree)
                    )
                    for connection_variables, connection_shift, connection_coefficient in connection_choices(
                        inverse_degree, maxima["p"], False
                    ):
                        grade = base_grade + normal_shift + load_shift + connection_shift
                        tdegree = base_t + numerator_t + 2 * inverse_degree
                        if grade > MAXIMUM or not (2 <= tdegree <= 8):
                            continue
                        variables = tuple(sorted(variables0 + connection_variables))
                        key = (family_index, grade, tdegree, variables)
                        aggregate[key] += (
                            coefficient0 * normal_coefficient * inverse_coefficient
                            * connection_coefficient
                        )
        for (family, grade, tdegree, variables), coefficient in sorted(aggregate.items()):
            if coefficient:
                analytic.append({
                    "family": family, "grade": grade, "t_degree": tdegree,
                    "variables": list(variables), "theta_power": degree,
                    "eta_power": int(primitive["R"]),
                    "coefficient": fraction_text(coefficient),
                })

    aggregate_literal: defaultdict[tuple[object, ...], Fraction] = defaultdict(Fraction)
    for monomial in analytic:
        source_row = int(monomial["t_degree"]) - 1
        for row in range(source_row, 8, 2):
            connection_degree = (row - source_row) // 2
            rising = Fraction(1)
            for index in range(connection_degree):
                rising *= Fraction(source_row, 2) + index
            transform = rising / math.factorial(connection_degree) / (2 ** connection_degree)
            for connection_variables, connection_shift, connection_coefficient in connection_choices(
                connection_degree, maxima["p"], True
            ):
                grade = int(monomial["grade"]) + connection_shift
                if grade > MAXIMUM:
                    continue
                variables = tuple(sorted(tuple(monomial["variables"]) + connection_variables))
                key = (
                    int(monomial["family"]), row, grade, variables,
                    int(monomial["theta_power"]), int(monomial["eta_power"]),
                )
                aggregate_literal[key] += (
                    Fraction(str(monomial["coefficient"])) * transform * connection_coefficient
                )
    literal: list[dict[str, object]] = []
    for key, coefficient in sorted(aggregate_literal.items()):
        if coefficient:
            family, row, grade, variables, theta_power, eta_power = key
            literal.append({
                "family": family, "row": row, "grade": grade,
                "variables": list(variables), "theta_power": theta_power,
                "eta_power": eta_power, "coefficient": fraction_text(coefficient),
            })
    return analytic, literal


def singular_fraction(value: str) -> str:
    return f"({value})" if "/" in value else value


def inverse_series(name: str, pole: int) -> str:
    terms = []
    for degree in range(5):
        coefficient = Fraction((-1) ** degree * math.comb(pole + degree - 1, degree))
        body = "1" if degree == 0 else (name if degree == 1 else f"({name})^{degree}")
        tpart = "" if degree == 0 else f"*t^{2 * degree}"
        terms.append(f"({fraction_text(coefficient)})*{body}{tpart}")
    return "+".join(terms).replace("+-", "-")


def faber_transform_coefficient(row: int, source_row: int) -> Fraction:
    delta = row - source_row
    if delta < 0 or delta % 2:
        return Fraction(0)
    degree = delta // 2
    coefficient = Fraction(1)
    for index in range(degree):
        coefficient *= Fraction(source_row, 2) + index
    return coefficient / math.factorial(degree) / (2 ** degree)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    for source, expected in PINS.items():
        actual = digest(source)
        if actual != expected:
            fail(("frozen recurrence parent mismatch", str(source), actual, expected))

    primitives = enumerate_primitives(MAXIMUM)
    if {primitive_signature(item) for item in primitives} != EXPECTED_PRIMITIVES:
        fail(("baseline primitive inventory mismatch", primitives))
    extended = enumerate_primitives(60)
    first_pole4 = min(int(item["base_grade"]) for item in extended if int(item["pole"]) >= 4)
    if first_pole4 != 43:
        fail(("first pole-four wall mismatch", first_pole4))
    maxima = derive_jet_maxima(primitives)
    analytic_monomials, literal_monomials = inventory_monomials(primitives, maxima)
    if not any("a1_7" in item["variables"] for item in literal_monomials):
        fail("inventory omitted required A_7 monomial")
    if not any("k0_6" in item["variables"] for item in literal_monomials):
        fail("inventory omitted required k10_6 monomial")

    parent = load_parent()
    high_parent = parent.load_parent()
    source_base, tail_base, tails = high_parent.ancestry()
    output = args.output.resolve()
    if output.exists():
        fail("a>=10 J38-R3 output already exists")
    output.mkdir(parents=True)
    inventory = {
        "status": "COMPLETE-BASELINE-A10-THROUGH-GRADE38",
        "derivation": "independent binomial expansion of all four source summands",
        "baseline": {"A": 10, "C": 11, "R": 10},
        "maximum_grade": MAXIMUM,
        "primitive_families": primitives,
        "primitive_family_count": len(primitives),
        "first_pole_order_at_least_four_grade": first_pole4,
        "jet_maxima": maxima,
        "analytic_monomials": analytic_monomials,
        "literal_faber_source_monomials": literal_monomials,
        "targets": [
            {"row": 2, "grade": 28 + index, "variable": jet_name("mu20", index), "coefficient": "-1"}
            for index in range(maxima["mu20"] + 1)
        ] + [
            {"row": 4, "grade": 32 + index, "variable": jet_name("mu4", index), "coefficient": "-1"}
            for index in range(maxima["mu4"] + 1)
        ] + [
            {"row": 6, "grade": 36 + index, "variable": jet_name("mu6", index), "coefficient": "-1"}
            for index in range(maxima["mu6"] + 1)
        ] + [{"row": 7, "grade": 38, "variable": "J", "coefficient": "-1/4"}],
        "uniform_shift": {
            "theta_power": "R+A+C factor count", "eta_power": "R factor count",
            "substitution": "theta=sigma^n, eta=sigma^s, n,s>=0",
        },
    }
    inventory_path = output / "source_inventory.json"
    inventory_path.write_text(json.dumps(inventory, sort_keys=True, indent=2) + "\n")
    inventory_sha = digest(inventory_path)

    variables = ["z", "t", "sigma", "p"]
    variables += [f"ell{index}" for index in range(1, maxima["p"] + 1)]
    variables += ["theta", "eta"]
    for stem in ("a1", "a0"):
        variables += [jet_name(stem, index) for index in range(maxima["A"] + 1)]
    for stem in ("c1", "c0"):
        variables += [jet_name(stem, index) for index in range(maxima["C"] + 1)]
    for stem in ("b1", "b0"):
        variables += [jet_name(stem, index) for index in range(maxima["R"] + 1)]
    variables += [jet_name("k0", index) for index in range(maxima["k10"] + 1)]
    variables += [jet_name("k60", index) for index in range(maxima["k6"] + 1)]
    variables += [jet_name("k20", index) for index in range(maxima["k2"] + 1)]
    variables += [jet_name("mu20", index) for index in range(maxima["mu20"] + 1)]
    variables += [jet_name("mu4", index) for index in range(maxima["mu4"] + 1)]
    variables += [jet_name("mu6", index) for index in range(maxima["mu6"] + 1)]
    variables += ["J", "iJ"]

    pp = "p" + "".join(f"+2*sigma^{index}*ell{index}" for index in range(1, maxima["p"] + 1))
    normal = {
        "A": f"sigma^10*theta*(({series('a1', maxima['A'])})+t*({series('a0', maxima['A'])}))",
        "C": f"sigma^11*theta*(({series('c1', maxima['C'])})+t*({series('c0', maxima['C'])}))",
        "R": f"sigma^10*theta*eta*(({series('b1', maxima['R'])})+t*({series('b0', maxima['R'])}))",
    }
    az = f"sigma^10*theta*({series('a1', maxima['A'])})"
    ac = f"sigma^10*theta*({series('a0', maxima['A'])})"
    cz = f"sigma^11*theta*({series('c1', maxima['C'])})"
    cc = f"sigma^11*theta*({series('c0', maxima['C'])})"
    rz = f"sigma^10*theta*eta*({series('b1', maxima['R'])})"
    rc = f"sigma^10*theta*eta*({series('b0', maxima['R'])})"
    coeffs = source_base.source_coefficients(pp, az, ac, cz, cc, rz, rc)
    loads = {
        "k10": f"({series('k0', maxima['k10'])})",
        "k6": f"({series('k60', maxima['k6'])})",
        "k2": f"({series('k20', maxima['k2'])})",
    }
    targets = {
        1: "0", 2: series("mu20", maxima["mu20"]), 3: "0",
        4: series("mu4", maxima["mu4"]), 5: "0",
        6: series("mu6", maxima["mu6"]), 7: "J/4",
    }
    source_rows: dict[int, str] = {}
    full_rows: dict[int, str] = {}
    for row in range(1, 8):
        source = tail_base.tail_text(tails[str(row)], row, coeffs, loads).replace(
            "Lambda", "(sigma^2)"
        )
        source_rows[row] = source
        target = targets[row]
        full_rows[row] = source if target == "0" else f"({source})-sigma^{2 * (12 + row)}*({target})"

    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target_path = output / f"square_d1_age10_j38_odd_recurrence3_{label}.sing"
    lines = [
        f"ring R={args.characteristic},({','.join(variables)}),dp;",
        'print("D1J38R3_SOURCE_HASHES=PASS");',
        f'print("D1J38R3_INVENTORY_SHA256={inventory_sha}");',
        f'print("D1J38R3_PRIMITIVE_FAMILY_COUNT={len(primitives)}");',
        f'print("D1J38R3_ANALYTIC_MONOMIAL_COUNT={len(analytic_monomials)}");',
        f'print("D1J38R3_LITERAL_MONOMIAL_COUNT={len(literal_monomials)}");',
        'print("D1J38R3_POLE_GE4_MIN_GRADE=43");',
        'print("D1J38R3_MECHANICAL_JET_MAXIMA=A7_C10_R6_K106_K610_K26_P10");',
        "ideal R3_S38=std(ideal(sigma^38)); ideal R3_S39=std(ideal(sigma^39));",
    ]
    for row in range(1, 8):
        lines.append(f"poly R3_SourcePhi{row}={source_rows[row]};")
        lines.append(f"poly R3_FullPhi{row}={full_rows[row]};")

    lines += [
        f"poly R3_sp=({pp})/2;",
        f"poly R3_Inv1={inverse_series('R3_sp', 1)};",
        f"poly R3_Inv2={inverse_series('R3_sp', 2)};",
        f"poly R3_Inv3={inverse_series('R3_sp', 3)};",
    ]
    hterms = []
    for primitive in primitives:
        factors = [singular_fraction(str(primitive["coefficient"])), f"sigma^{primitive['fixed_sigma']}"]
        if primitive["load"] is not None:
            factors.append(loads[str(primitive["load"])])
        for stem in ("R", "A", "C"):
            exponent = int(primitive[stem])
            if exponent == 1:
                factors.append(f"({normal[stem]})")
            elif exponent > 1:
                factors.append(f"({normal[stem]})^{exponent}")
        numerator_degree = int(primitive["R"]) + int(primitive["A"]) + int(primitive["C"])
        tpower = 2 * int(primitive["pole"]) - numerator_degree + 1
        if tpower:
            factors.append("t" if tpower == 1 else f"t^{tpower}")
        factors.append(f"R3_Inv{primitive['pole']}")
        hterms.append("*".join(factors))
    lines.append("poly R3_H=" + "+".join(hterms) + ";")
    lines.append("poly R3_D0=R3_H;")
    for derivative in range(1, 9):
        lines.append(f"poly R3_D{derivative}=diff(R3_D{derivative - 1},t);")
        if derivative >= 2:
            row = derivative - 1
            lines.append(
                f"poly R3_h{row}=subst(R3_D{derivative},t,0)/{math.factorial(derivative)};"
            )
    for row in range(1, 8):
        summands = []
        for source_row in range(1, row + 1):
            coefficient = faber_transform_coefficient(row, source_row)
            if not coefficient:
                continue
            degree = (row - source_row) // 2
            factor = singular_fraction(fraction_text(coefficient))
            if degree:
                factor += f"*(({pp})^{degree})"
            summands.append(f"({factor})*R3_h{source_row}")
        lines.append(f"poly R3_PredPhi{row}=" + "+".join(summands) + ";")
    bridge_product = "*".join(f"R3_bridge{row}" for row in range(1, 8))
    for row in range(1, 8):
        lines.append(
            f"int R3_bridge{row}=(reduce(R3_SourcePhi{row}-R3_PredPhi{row},R3_S39)==0);"
        )
    lines += [
        f"int R3_full_bridge={bridge_product};",
        'print("D1J38R3_ALL_SEVEN_SOURCE_ROWS_BRIDGED="+string(R3_full_bridge));',
        'if (R3_full_bridge!=1) { print("D1J38R3_FAIL=INDEPENDENT_SOURCE_BRIDGE"); quit; }',
    ]

    for variable, marker in (("a1_7", "A7"), ("k0_6", "K10_6")):
        lines.append(f"int R3_{marker}_enters=0;")
        for row in range(1, 8):
            lines += [
                f"poly R3_{marker}_d{row}=diff(R3_SourcePhi{row},{variable});",
                f"if (reduce(R3_{marker}_d{row},R3_S38)==0) {{",
                f"  poly R3_{marker}_q{row}=R3_{marker}_d{row}/sigma^38;",
                f"  if (subst(R3_{marker}_q{row},sigma,0)!=0) {{ R3_{marker}_enters=1; }}",
                "}",
            ]
        lines.append(f'print("D1J38R3_REQUIRED_{marker}_ENTERS_G38="+string(R3_{marker}_enters));')
        lines.append(
            f'if (R3_{marker}_enters!=1) {{ print("D1J38R3_FAIL=MISSING_{marker}"); quit; }}'
        )

    lines += [
        f"poly R3_source_rel=R3_SourcePhi7+(({pp})/4)*R3_SourcePhi5+(3*(({pp})^2)/32)*R3_SourcePhi3+(5*(({pp})^3)/128)*R3_SourcePhi1;",
        f"poly R3_rel=R3_FullPhi7+(({pp})/4)*R3_FullPhi5+(3*(({pp})^2)/32)*R3_FullPhi3+(5*(({pp})^3)/128)*R3_FullPhi1;",
        "int R3_source_mod39=(reduce(R3_source_rel,R3_S39)==0);",
        "int R3_div38=(reduce(R3_rel,R3_S38)==0);",
        "poly R3_q38=R3_rel/sigma^38;",
        "int R3_coeff=(subst(R3_q38,sigma,0)+J/4==0);",
        "int R3_mod39=(reduce(R3_rel+(sigma^38)*J/4,R3_S39)==0);",
        "int R3_symbolic_safe=(reduce(diff(R3_source_rel,theta),R3_S39)==0 && reduce(diff(R3_source_rel,eta),R3_S39)==0);",
        "ideal R3_unit=std(ideal(subst(R3_q38,sigma,0),iJ*J-1));",
        "int R3_exact_unit=(reduce(1,R3_unit)==0);",
        'print("D1J38R3_SOURCE_RECURRENCE_MOD_G39="+string(R3_source_mod39));',
        'print("D1J38R3_DIVISIBLE_G38="+string(R3_div38));',
        'print("D1J38R3_GRADE38_COEFFICIENT_MINUS_J_OVER_4="+string(R3_coeff));',
        'print("D1J38R3_RECURRENCE_MOD_G39="+string(R3_mod39));',
        'print("D1J38R3_SYMBOLIC_THETA_ETA_SAFE="+string(R3_symbolic_safe));',
        'print("D1J38R3_EXACT_J_CONTACT_UNIT="+string(R3_exact_unit));',
        "if (R3_source_mod39*R3_div38*R3_coeff*R3_mod39*R3_symbolic_safe*R3_exact_unit!=1) { print(\"D1J38R3_FAIL=RECURRENCE_OR_UNIT\"); quit; }",
        "poly R3_Qpell=z^4-1;",
        "poly R3_Ppell=16*R3_Qpell^2+20*R3_Qpell+5;",
        "poly R3_Apell=16*z^10-20*z^6+5*z^2;",
        "int R3_pell=(R3_Apell^2-R3_Qpell*R3_Ppell^2-1==0);",
        'print("D1J38R3_CHEBYSHEV_PELL_CONTROL="+string(R3_pell));',
        'if (R3_pell!=1) { print("D1J38R3_FAIL=PELL_CONTROL"); quit; }',
        'print("D1J38R3_ENDPOINT=PASS_EMPTY_UNIFORM_A_GE_10");',
        "quit;",
    ]
    target_path.write_text("\n".join(lines) + "\n")
    payload = {
        "status": "PASS-D1-AGE10-J38-ODD-RECURRENCE3-COMPILER",
        "scope": "UNIFORM_A_GE_10_C_EQ_A_PLUS_1_R_GE_A_D_J_LITERAL_SOURCE_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "input_sha256": digest(target_path),
        "inventory_sha256": inventory_sha,
        "primitive_family_count": len(primitives),
        "analytic_monomial_count": len(analytic_monomials),
        "literal_monomial_count": len(literal_monomials),
        "jet_maxima": maxima,
    }
    (output / "result.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
