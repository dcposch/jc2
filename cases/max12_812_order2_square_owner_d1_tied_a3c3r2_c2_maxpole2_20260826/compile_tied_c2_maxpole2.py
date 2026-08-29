#!/usr/bin/env python3
"""Compile the fourfold tied (a,c,r)=(3,3,2) C2 maximal-pole producer; AWS only."""

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
        "b012917ca9480b59ad1c5d2cb0945091b2184b9a1b80e7d5deb9ad911e16dffd",
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
BASELINE = {"A": 3, "C": 3, "R": 2}
CEILING = 16


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only tied a3c3r2 C2 maximal-pole compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only tied a3c3r2 C2 maximal-pole compiler refused non-Amazon host")
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
    answer = Fraction(1)
    for index in range(degree):
        answer *= alpha - index
    return answer / math.factorial(degree)


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def enumerate_primitives(pad: int = 0) -> list[dict[str, object]]:
    """Independent cost-bounded enumeration from all four binomial summands."""

    aggregate: defaultdict[tuple[object, ...], Fraction] = defaultdict(Fraction)
    for summand in SUMMANDS:
        budget = CEILING - int(summand["fixed"])
        if budget < 0:
            continue
        costs = [
            int(atom["fixed"])
            + BASELINE["R"] * int(atom["R"])
            + BASELINE["A"] * int(atom["A"])
            + BASELINE["C"] * int(atom["C"])
            for atom in ATOMS
        ]
        if any(cost <= 0 for cost in costs):
            fail(("nonpositive atom cost", costs))
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
            grade = fixed + sum(BASELINE[stem] * exponents[stem] for stem in exponents)
            if grade > CEILING:
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
    answer: list[dict[str, object]] = []
    for key, coefficient in aggregate.items():
        if coefficient == 0:
            continue
        name, load_name, fixed, rexp, aexp, cexp, pole = key
        grade = (
            int(fixed) + BASELINE["R"] * int(rexp)
            + BASELINE["A"] * int(aexp) + BASELINE["C"] * int(cexp)
        )
        answer.append({
            "summand": name, "load": load_name, "fixed_sigma": fixed,
            "R": rexp, "A": aexp, "C": cexp, "pole": pole,
            "coefficient": fraction_text(coefficient), "first_grade": grade,
        })
    return sorted(answer, key=lambda item: (
        int(item["first_grade"]), str(item["summand"]), int(item["pole"]),
        int(item["R"]), int(item["A"]), int(item["C"]),
    ))


def signature(item: dict[str, object]) -> tuple[object, ...]:
    return tuple(item[key] for key in (
        "summand", "load", "fixed_sigma", "R", "A", "C", "pole",
        "coefficient", "first_grade",
    ))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65519, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    check(PINS)

    base = load(BASE, "d1_tied_source_base")
    check(base.PINS)
    v1 = base.load_v1()
    check(v1.EXPECTED)
    tails = json.loads(v1.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != v1.EXPECTED_ALL_TAILS:
        fail("canonical all-tail digest mismatch")
    tail_base = v1.load_base()

    primitive = enumerate_primitives()
    padded = enumerate_primitives(pad=1)
    if {signature(item) for item in primitive} != {signature(item) for item in padded}:
        fail(("padded inventory mismatch", primitive, padded))
    expected = {
        ("unloaded", None, 10, 0, 1, 1, 1, "3/4", 16),
        ("unloaded", None, 10, 0, 0, 2, 2, "3/8", 16),
        ("k10", "k10", 10, 3, 0, 0, 1, "5/16", 16),
        ("k10", "k10", 11, 1, 0, 1, 1, "5/8", 16),
    }
    if {signature(item) for item in primitive} != expected:
        fail(("tied primitive census mismatch", primitive))
    pole2 = [item for item in primitive if int(item["pole"]) == 2]
    if len(pole2) != 1 or signature(pole2[0]) != (
        "unloaded", None, 10, 0, 0, 2, 2, "3/8", 16,
    ):
        fail(("unique maximal-pole signature mismatch", pole2))

    variables = (
        "z,t,sigma,p,a1,a0,c1,c0,b1,b0,k0,k6,k2load,mu2,mu4,mu6,J,"
        "lam,ic1,ic0,ilam,ik0"
    )
    prefix = "F433_"
    lines = [
        f"ring R433={args.characteristic},({variables}),dp;",
        'print("F433_SOURCE_HASHES=PASS");',
        'print("F433_SCOPE=A3_C3_R2_UNIT_LOAD_G16_ONLY");',
        'print("F433_PRIMITIVE_COUNT=4");',
        'print("F433_UNIQUE_MAX_POLE=C2_POLE2");',
        'print("F433_PADDED_CUTOFF_IDENTICAL=1");',
    ]
    coeffs = base.source_coefficients(
        "p", "sigma^3*a1", "sigma^3*a0", "sigma^3*c1", "sigma^3*c0",
        "sigma^2*b1", "sigma^2*b0",
    )
    loads = {"k10": "k0", "k6": "k6", "k2": "k2load"}
    base.extraction(lines, prefix, tail_base, tails, coeffs, loads, CEILING, CEILING)

    inv1 = "(1-(p/2)*t^2+((p^2)/4)*t^4-((p^3)/8)*t^6+((p^4)/16)*t^8)"
    inv2 = "(1-p*t^2+(3*(p^2)/4)*t^4-((p^3)/2)*t^6+(5*(p^4)/16)*t^8)"
    inv3 = "(1-(3*p/2)*t^2+(3*(p^2)/2)*t^4-(5*(p^3)/4)*t^6+(15*(p^4)/16)*t^8)"
    hshift = base.universal_hshift(
        "sigma^3*(a1+a0*t)", "sigma^3*(c1+c0*t)",
        "sigma^2*(b1+b0*t)", "k0", inv1, inv2, inv3,
    )
    base.analytic_extract(lines, prefix, hshift, CEILING, CEILING)
    base.row_checks(lines, prefix, v1, CEILING, CEILING)

    lines += [
        "poly F433_L=z^2+p/2;",
        "poly F433_A=a1*z+a0; poly F433_C=c1*z+c0; poly F433_R=b1*z+b0;",
        "poly F433_N2=F433_h16_1*z^3+F433_h16_2*z^2"
        "+(F433_h16_3+p*F433_h16_1)*z+(F433_h16_4+p*F433_h16_2);",
        "poly F433_N2Expected=(3/4)*F433_A*F433_C*F433_L+(3/8)*F433_C^2"
        "+(5/16)*k0*F433_R^3*F433_L+(5/8)*k0*F433_R*F433_C*F433_L;",
        "ideal F433_L2Ideal=std(ideal(F433_L^2));",
        "poly F433_OrdinaryQuotient=(F433_N2Expected-F433_N2)/(F433_L^2);",
        "int F433_common_numerator=(reduce(F433_N2-F433_N2Expected,F433_L2Ideal)==0"
        " && F433_N2+(F433_L^2)*F433_OrdinaryQuotient-F433_N2Expected==0);",
        "int F433_recurrence=(F433_h16_5+p*F433_h16_3+((p^2)/4)*F433_h16_1==0"
        " && F433_h16_6+p*F433_h16_4+((p^2)/4)*F433_h16_2==0"
        " && F433_h16_7+p*F433_h16_5+((p^2)/4)*F433_h16_3==0);",
        "poly F433_PsiPlus=F433_g16_4+lam*(F433_g16_3+(p/4)*F433_g16_1);",
        "poly F433_PsiMinus=F433_g16_4-lam*(F433_g16_3+(p/4)*F433_g16_1);",
        "poly F433_NPlus=subst(F433_N2,z,lam); poly F433_NMinus=subst(F433_N2,z,-lam);",
        "F433_PsiPlus=subst(F433_PsiPlus,p,-2*lam^2);"
        " F433_PsiMinus=subst(F433_PsiMinus,p,-2*lam^2);",
        "F433_NPlus=subst(F433_NPlus,p,-2*lam^2); F433_NMinus=subst(F433_NMinus,p,-2*lam^2);",
        "int F433_root_faber=(F433_PsiPlus-F433_NPlus==0 && F433_PsiMinus-F433_NMinus==0);",
        "poly F433_Cp=lam*c1+c0; poly F433_Cm=-lam*c1+c0;",
        "int F433_maxpole_roots=(F433_PsiPlus-(3/8)*F433_Cp^2==0"
        " && F433_PsiMinus-(3/8)*F433_Cm^2==0);",
        "ideal F433_Ic1=std(ideal(F433_PsiPlus,F433_PsiMinus,ic1*c1-1,ilam*lam-1));",
        "ideal F433_Ic0=std(ideal(F433_PsiPlus,F433_PsiMinus,ic0*c0-1,ilam*lam-1));",
        "int F433_exact_C_empty=(reduce(1,F433_Ic1)==0 && reduce(1,F433_Ic0)==0);",
        "ideal F433_EvalUnit=std(ideal(2*lam,ilam*lam-1));",
        "int F433_evaluation_cover=(reduce(1,F433_EvalUnit)==0);",
        "poly F433_NoC2=F433_N2Expected-(3/8)*F433_C^2;",
        "poly F433_NoPlus=subst(subst(F433_NoC2,z,lam),p,-2*lam^2);",
        "poly F433_NoMinus=subst(subst(F433_NoC2,z,-lam),p,-2*lam^2);",
        "int F433_negctrl_no_c2=(F433_NoPlus==0 && F433_NoMinus==0);",
        "int F433_targetfree_all7=F433_forbidden;",
        "int F433_endpoint=F433_divisible*F433_identities*F433_forbidden*F433_analyticDiv*F433_row16"
        "*F433_common_numerator*F433_recurrence*F433_root_faber*F433_maxpole_roots"
        "*F433_exact_C_empty*F433_evaluation_cover*F433_negctrl_no_c2;",
        'print("F433_ALL_SEVEN_ROWS_BRIDGED="+string(F433_row16));',
        'print("F433_ALL_SOURCE_QUOTIENTS_EXACT="+string(F433_identities));',
        'print("F433_TARGETFREE_ALL_SEVEN="+string(F433_targetfree_all7));',
        'print("F433_COMMON_N2="+string(F433_common_numerator));',
        'print("F433_ORDINARY_PART_QUOTIENT_RETAINED="+string(F433_common_numerator));',
        'print("F433_L2_RECURRENCE="+string(F433_recurrence));',
        'print("F433_BOTH_ROOT_FABER_IDENTITIES="+string(F433_root_faber));',
        'print("F433_MAXPOLE_ROOTS_C2_SQUARES="+string(F433_maxpole_roots));',
        'print("F433_BOTH_EXACT_C_CHARTS_UNIT="+string(F433_exact_C_empty));',
        'print("F433_EVALUATION_DETERMINANT_UNIT="+string(F433_evaluation_cover));',
        'print("F433_NEGCTRL_OMIT_C2_ZERO_ROOTS="+string(F433_negctrl_no_c2));',
        'if (F433_endpoint!=1) { print("F433_FAIL=SOURCE_ROOT_OR_UNIT"); quit; }',
        'print("F433_ENDPOINT=PASS_EMPTY_A3_C3_R2_ON_D_P_K0");',
        "quit;",
    ]

    output = args.output.resolve()
    if output.exists():
        fail("tied a3c3r2 C2 maximal-pole output already exists")
    output.mkdir(parents=True)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_d1_tied_a3c3r2_c2_maxpole2_{label}.sing"
    target.write_text("\n".join(lines) + "\n")
    inventory = {
        "status": "PASS-D1-TIED-A3C3R2-C2-MAXPOLE2-COMPILER",
        "scope": "A3_C3_R2_UNIT_LOAD_G16_ON_D_P_K0_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "ceiling": CEILING,
        "primitive_count": len(primitive),
        "primitive_families": primitive,
        "unique_maximal_pole": "3/8*C^2/L^2",
        "source_jet_count": 7,
        "target_jet_count": 0,
        "input_sha256": digest(target),
    }
    inventory_path = output / "source_inventory.json"
    inventory_path.write_text(json.dumps(inventory, sort_keys=True, indent=2) + "\n")
    print(json.dumps(inventory, sort_keys=True))


if __name__ == "__main__":
    main()
