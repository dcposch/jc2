#!/usr/bin/env python3
"""Compile the D1 target-free primary-C2 closed cell for 3<=c<=7; AWS only."""

from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import product
import importlib.util
import json
import math
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE_DIR = ROOT / "cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_20260826"
BASE = BASE_DIR / "compile_r1_d1_ac.py"
PINS = {
    BASE: "e024a13d24a11519f70b535d4b47c47c62538a684b8bc71e79216410cd8ecb7c",
    BASE_DIR / "FREEZE.sha256":
        "34b0f3254410e39abfc9843febd3c053f965a30dfa948d9e0367c0fb094611a6",
    ROOT / "xmodel/max12-812-order2-square-maximal-pole-row-syzygy-miner-spec-20260826.md":
        "c4eba2d79521d6c621223dc1b36bb298e7a805bf1cd595b593f444d14f148358",
    HERE / "PREREGISTRATION.md":
        "12939b0b3f0cddf6829f0e4dbcb920b1e4567509194f48e66dc3eee803dba09a",
}

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
CONTACTS = tuple(range(3, 8))


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only D1 C2 c3c7 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only D1 C2 c3c7 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("cannot import", str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check(mapping) -> None:
    for path, expected in mapping.items():
        actual = digest(path)
        if actual != expected:
            fail(("frozen pin mismatch", str(path), actual, expected))


def binomial(alpha: Fraction, degree: int) -> Fraction:
    result = Fraction(1)
    for index in range(degree):
        result *= alpha - index
    return result / math.factorial(degree)


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def enumerate_primitives(c: int, pad: int = 0) -> list[dict[str, object]]:
    baseline = {"A": c, "C": c, "R": c - 1}
    maximum = 10 + 2 * c
    aggregate: defaultdict[tuple[object, ...], Fraction] = defaultdict(Fraction)
    for summand in SUMMANDS:
        budget = maximum - int(summand["fixed"])
        costs = [
            int(atom["fixed"])
            + baseline["R"] * int(atom["R"])
            + baseline["A"] * int(atom["A"])
            + baseline["C"] * int(atom["C"])
            for atom in ATOMS
        ]
        bounds = [budget // cost + pad for cost in costs]
        alpha = summand["alpha"]
        assert isinstance(alpha, Fraction)
        for counts in product(*(range(bound + 1) for bound in bounds)):
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
            key = (
                summand["name"], summand["load"], fixed,
                exponents["R"], exponents["A"], exponents["C"], pole, grade,
            )
            aggregate[key] += coefficient
    result = []
    for key, coefficient in aggregate.items():
        if coefficient:
            name, load_name, fixed, rexp, aexp, cexp, pole, grade = key
            result.append({
                "summand": name, "load": load_name, "fixed_sigma": fixed,
                "R": rexp, "A": aexp, "C": cexp, "pole": pole,
                "coefficient": fraction_text(coefficient), "first_grade": grade,
            })
    return sorted(result, key=lambda item: (
        int(item["first_grade"]), str(item["summand"]), int(item["pole"]),
        int(item["R"]), int(item["A"]), int(item["C"]),
    ))


def signature(item: dict[str, object]) -> tuple[object, ...]:
    return tuple(item[key] for key in (
        "summand", "load", "fixed_sigma", "R", "A", "C", "pole",
        "coefficient", "first_grade",
    ))


def expected(c: int) -> set[tuple[object, ...]]:
    grade = 10 + 2 * c
    result = {
        ("unloaded", None, 10, 0, 1, 1, 1, "3/4", grade),
        ("unloaded", None, 10, 0, 0, 2, 2, "3/8", grade),
        ("k10", "k10", 11, 1, 0, 1, 1, "5/8", grade),
    }
    if c == 3:
        result.add(("k10", "k10", 10, 3, 0, 0, 1, "5/16", grade))
    if c == 7:
        result.add(("k6", "k6", 17, 0, 0, 1, 1, "3/4", grade))
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65519, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    check(PINS)

    base = load(BASE, "d1_c2_c3c7_source_base")
    check(base.PINS)
    v1 = base.load_v1()
    check(v1.EXPECTED)
    tails = json.loads(v1.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v1.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    tail_base = v1.load_base()

    inventories: dict[str, list[dict[str, object]]] = {}
    for c in CONTACTS:
        primitive = enumerate_primitives(c)
        if {signature(item) for item in primitive} != expected(c):
            fail(("C2 source census mismatch", c, primitive, expected(c)))
        if {signature(item) for item in enumerate_primitives(c, 1)} != expected(c):
            fail(("padded C2 source census mismatch", c))
        pole2 = [item for item in primitive if int(item["pole"]) == 2]
        if len(pole2) != 1 or (int(pole2[0]["C"]), str(pole2[0]["coefficient"])) != (2, "3/8"):
            fail(("unique C2 maximal pole mismatch", c, pole2))
        # Raising a or r adds n*Aexp+s*Rexp with n,s>=0 to every grade.
        if any(int(item["A"]) < 0 or int(item["R"]) < 0 for item in primitive):
            fail(("nonmonotone A/R exponent", c, primitive))
        inventories[str(c)] = primitive

    variables = (
        "z,t,sigma,p,a1,a0,c1,c0,b1,b0,k0,k60,k20,mu2,mu4,mu6,J,"
        "lam,ic1,ic0,ilam"
    )
    lines = [
        f"ring RC2={args.characteristic},({variables}),dp;",
        'print("C2C3C7_SOURCE_HASHES=PASS");',
        'print("C2C3C7_CONTACT_COUNT=5");',
        'print("C2C3C7_MONOTONE_A_R_CLOSED_TAIL=1");',
        'print("C2C3C7_C8_MOVING_K6C_WALL_EXCLUDED=1");',
    ]
    inv1 = "(1-(p/2)*t^2+((p^2)/4)*t^4-((p^3)/8)*t^6+((p^4)/16)*t^8)"
    inv2 = "(1-p*t^2+(3*(p^2)/4)*t^4-((p^3)/2)*t^6+(5*(p^4)/16)*t^8)"
    inv3 = "(1-(3*p/2)*t^2+(3*(p^2)/2)*t^4-(5*(p^3)/4)*t^6+(15*(p^4)/16)*t^8)"
    loads = {"k10": "k0", "k6": "k60", "k2": "k20"}
    target_names = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    endpoints = []

    for c in CONTACTS:
        grade = 10 + 2 * c
        prefix = f"C2T{c}_"
        A = f"sigma^{c}*(a1+a0*t)"
        C = f"sigma^{c}*(c1+c0*t)"
        R = f"sigma^{c-1}*(b1+b0*t)"
        coeffs = base.source_coefficients(
            "p", f"sigma^{c}*a1", f"sigma^{c}*a0",
            f"sigma^{c}*c1", f"sigma^{c}*c0",
            f"sigma^{c-1}*b1", f"sigma^{c-1}*b0",
        )
        lines += [
            f"ideal {prefix}S=std(ideal(sigma^{grade}));",
            f"ideal {prefix}S1=std(ideal(sigma));",
            f"ideal {prefix}Snext=std(ideal(sigma^{grade+1}));",
            f"int {prefix}source_exact=1; int {prefix}targetfree=1;",
        ]
        for row in range(1, 8):
            source = tail_base.tail_text(tails[str(row)], row, coeffs, loads).replace("Lambda", "(sigma^2)")
            full = source if target_names[row] == "0" else f"({source})-sigma^{2*(12+row)}*({target_names[row]})"
            lines += [
                f"poly {prefix}SourcePhi{row}={source};",
                f"poly {prefix}FullPhi{row}={full};",
                f"if (reduce({prefix}SourcePhi{row},{prefix}S)!=0) {{ {prefix}source_exact=0; }}",
                f"poly {prefix}Q{grade}_{row}={prefix}SourcePhi{row}/sigma^{grade};",
                f"if (sigma^{grade}*{prefix}Q{grade}_{row}-{prefix}SourcePhi{row}!=0) {{ {prefix}source_exact=0; }}",
                f"poly {prefix}g{grade}_{row}=subst({prefix}Q{grade}_{row},sigma,0);",
                f"if (diff({prefix}g{grade}_{row},k20)!=0 || diff({prefix}g{grade}_{row},mu2)!=0"
                f" || diff({prefix}g{grade}_{row},mu4)!=0 || diff({prefix}g{grade}_{row},mu6)!=0"
                f" || diff({prefix}g{grade}_{row},J)!=0) {{ {prefix}targetfree=0; }}",
                f"if (reduce({prefix}FullPhi{row}-{prefix}SourcePhi{row},{prefix}Snext)!=0) {{ {prefix}targetfree=0; }}",
            ]

        hshift = base.universal_hshift(A, C, R, "k0", inv1, inv2, inv3)
        hshift += f"+(3/4)*sigma^17*t^2*k60*({C})*({inv1})"
        lines += [
            f"poly {prefix}Hshift={hshift};",
            f"int {prefix}analytic_exact=(reduce({prefix}Hshift,{prefix}S)==0);",
            f"poly {prefix}HQ={prefix}Hshift/sigma^{grade};",
            f"if (sigma^{grade}*{prefix}HQ-{prefix}Hshift!=0) {{ {prefix}analytic_exact=0; }}",
            f"poly {prefix}H{grade}=subst({prefix}HQ,sigma,0);",
            f"poly {prefix}D{grade}_0={prefix}H{grade};",
        ]
        for derivative in range(1, 9):
            lines.append(f"poly {prefix}D{grade}_{derivative}=diff({prefix}D{grade}_{derivative-1},t);")
            if derivative >= 2:
                row = derivative - 1
                lines.append(
                    f"poly {prefix}h{grade}_{row}=subst({prefix}D{grade}_{derivative},t,0)/{math.factorial(derivative)};"
                )
        base.row_checks(lines, prefix, v1, grade, grade)

        lines += [
            f"poly {prefix}L=z^2+p/2;",
            f"poly {prefix}A=a1*z+a0; poly {prefix}C=c1*z+c0; poly {prefix}R=b1*z+b0;",
            f"poly {prefix}N2={prefix}h{grade}_1*z^3+{prefix}h{grade}_2*z^2"
            f"+({prefix}h{grade}_3+p*{prefix}h{grade}_1)*z"
            f"+({prefix}h{grade}_4+p*{prefix}h{grade}_2);",
        ]
        expected_terms = [
            f"(3/4)*{prefix}A*{prefix}C*{prefix}L",
            f"(3/8)*{prefix}C^2",
            f"(5/8)*k0*{prefix}R*{prefix}C*{prefix}L",
        ]
        if c == 3:
            expected_terms.append(f"(5/16)*k0*{prefix}R^3*{prefix}L")
        if c == 7:
            expected_terms.append(f"(3/4)*k60*{prefix}C*{prefix}L")
        expected_n2 = "+".join(expected_terms)
        lines += [
            f"poly {prefix}N2Expected={expected_n2};",
            f"ideal {prefix}L2=std(ideal({prefix}L^2));",
            f"poly {prefix}OrdinaryQuotient=({prefix}N2Expected-{prefix}N2)/({prefix}L^2);",
            f"int {prefix}common=(reduce({prefix}N2-{prefix}N2Expected,{prefix}L2)==0"
            f" && {prefix}N2+({prefix}L^2)*{prefix}OrdinaryQuotient-{prefix}N2Expected==0);",
            f"int {prefix}recurrence=({prefix}h{grade}_5+p*{prefix}h{grade}_3+((p^2)/4)*{prefix}h{grade}_1==0"
            f" && {prefix}h{grade}_6+p*{prefix}h{grade}_4+((p^2)/4)*{prefix}h{grade}_2==0"
            f" && {prefix}h{grade}_7+p*{prefix}h{grade}_5+((p^2)/4)*{prefix}h{grade}_3==0);",
            f"poly {prefix}PsiPlus={prefix}g{grade}_4+lam*({prefix}g{grade}_3+(p/4)*{prefix}g{grade}_1);",
            f"poly {prefix}PsiMinus={prefix}g{grade}_4-lam*({prefix}g{grade}_3+(p/4)*{prefix}g{grade}_1);",
            f"poly {prefix}NPlus=subst({prefix}N2,z,lam); poly {prefix}NMinus=subst({prefix}N2,z,-lam);",
            f"{prefix}PsiPlus=subst({prefix}PsiPlus,p,-2*lam^2); {prefix}PsiMinus=subst({prefix}PsiMinus,p,-2*lam^2);",
            f"{prefix}NPlus=subst({prefix}NPlus,p,-2*lam^2); {prefix}NMinus=subst({prefix}NMinus,p,-2*lam^2);",
            f"int {prefix}root_faber=({prefix}PsiPlus-{prefix}NPlus==0 && {prefix}PsiMinus-{prefix}NMinus==0);",
            f"poly {prefix}Cp=lam*c1+c0; poly {prefix}Cm=-lam*c1+c0;",
            f"int {prefix}root_squares=({prefix}PsiPlus-(3/8)*{prefix}Cp^2==0"
            f" && {prefix}PsiMinus-(3/8)*{prefix}Cm^2==0);",
            f"ideal {prefix}Ic1=std(ideal({prefix}PsiPlus,{prefix}PsiMinus,ic1*c1-1,ilam*lam-1));",
            f"ideal {prefix}Ic0=std(ideal({prefix}PsiPlus,{prefix}PsiMinus,ic0*c0-1,ilam*lam-1));",
            f"int {prefix}charts=(reduce(1,{prefix}Ic1)==0 && reduce(1,{prefix}Ic0)==0);",
            f"ideal {prefix}Eval=std(ideal(2*lam,ilam*lam-1));",
            f"int {prefix}eval_cover=(reduce(1,{prefix}Eval)==0);",
            f"poly {prefix}NoC2={prefix}N2Expected-(3/8)*{prefix}C^2;",
            f"poly {prefix}NoPlus=subst(subst({prefix}NoC2,z,lam),p,-2*lam^2);",
            f"poly {prefix}NoMinus=subst(subst({prefix}NoC2,z,-lam),p,-2*lam^2);",
            f"int {prefix}omit_c2=({prefix}NoPlus==0 && {prefix}NoMinus==0);",
            f"int {prefix}endpoint={prefix}source_exact*{prefix}targetfree*{prefix}analytic_exact"
            f"*{prefix}row{grade}*{prefix}common*{prefix}recurrence*{prefix}root_faber"
            f"*{prefix}root_squares*{prefix}charts*{prefix}eval_cover*{prefix}omit_c2;",
            f'print("C2C3C7_C{c}_PRIMITIVE_COUNT={len(inventories[str(c)])}");',
            f'print("C2C3C7_C{c}_SOURCE_EXACT="+string({prefix}source_exact));',
            f'print("C2C3C7_C{c}_ANALYTIC_EXACT="+string({prefix}analytic_exact));',
            f'print("C2C3C7_C{c}_ALL_SEVEN_ROWS="+string({prefix}row{grade}));',
            f'print("C2C3C7_C{c}_TARGETFREE="+string({prefix}targetfree));',
            f'print("C2C3C7_C{c}_COMMON_N2="+string({prefix}common));',
            f'print("C2C3C7_C{c}_L2_RECURRENCE="+string({prefix}recurrence));',
            f'print("C2C3C7_C{c}_ROOT_FABER="+string({prefix}root_faber));',
            f'print("C2C3C7_C{c}_ROOT_SQUARES="+string({prefix}root_squares));',
            f'print("C2C3C7_C{c}_BOTH_C_CHARTS_UNIT="+string({prefix}charts));',
            f'print("C2C3C7_C{c}_EVALUATION_COVER="+string({prefix}eval_cover));',
            f'print("C2C3C7_C{c}_OMIT_C2_ROOTS_ZERO="+string({prefix}omit_c2));',
        ]
        endpoints.append(f"{prefix}endpoint")

    lines += [
        "int C2C3C7_endpoint=" + "*".join(endpoints) + ";",
        'if (C2C3C7_endpoint!=1) { print("C2C3C7_FAIL=SOURCE_BRIDGE_OR_ROOT_CHART"); quit; }',
        'print("C2C3C7_ENDPOINT=PASS_EMPTY_PRIMARY_C2_C3_TO_C7_CLOSED_A_R_TAILS");',
        "quit;",
    ]

    output = args.output.resolve()
    if output.exists():
        fail("D1 C2 c3c7 output already exists")
    output.mkdir(parents=True)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_d1_c2_targetfree_c3c7_{label}.sing"
    target.write_text("\n".join(lines) + "\n")
    inventory_path = output / "source_inventory.json"
    payload = {
        "status": "PASS-D1-C2-TARGETFREE-C3C7-COMPILER",
        "scope": "C_EQ_3_TO_7_A_GE_C_R_GE_C_MINUS_1_ON_D_P_K0_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "contact_count": len(CONTACTS),
        "inventories": inventories,
        "monotone_closed_A_R_tails": True,
        "c8_moving_k6c_wall_excluded": True,
        "input_sha256": digest(target),
    }
    inventory_path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
