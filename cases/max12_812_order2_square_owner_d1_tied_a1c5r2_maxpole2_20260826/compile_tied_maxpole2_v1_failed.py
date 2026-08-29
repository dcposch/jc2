#!/usr/bin/env python3
"""Compile the exact tied (a,c,r)=(1,5,2) maximal-pole producer; AWS only."""

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
        "ad7a8a3bde1d1d0adbe1454f3efba9cf2211005f1e7b26f43df3b1c5df556533",
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
BASELINE = {"A": 1, "C": 5, "R": 2}
CEILING = 16


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only tied maximal-pole compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only tied maximal-pole compiler refused non-Amazon host")
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
        ("unloaded", None, 12, 1, 2, 0, 2, "-3/8", 16),
        ("k10", "k10", 10, 3, 0, 0, 1, "5/16", 16),
        ("k10", "k10", 14, 0, 2, 0, 1, "5/32", 16),
    }
    if {signature(item) for item in primitive} != expected:
        fail(("tied primitive census mismatch", primitive))
    pole2 = [item for item in primitive if int(item["pole"]) == 2]
    if len(pole2) != 1 or signature(pole2[0]) != (
        "unloaded", None, 12, 1, 2, 0, 2, "-3/8", 16,
    ):
        fail(("unique maximal-pole signature mismatch", pole2))

    variables = (
        "z,t,sigma,p,a1,a0,c1,c0,b1,b0,k0,k6,k2load,mu2,mu4,mu6,J,"
        "lam,au,bu,ilam,iau,ibu,ik0,iAp,iAm,iRp,iRm"
    )
    prefix = "T15_"
    lines = [
        f"ring Rtied={args.characteristic},({variables}),dp;",
        'print("T15_SOURCE_HASHES=PASS");',
        'print("T15_SCOPE=A1_C5_R2_UNIT_LOAD_G16_ONLY");',
        'print("T15_PRIMITIVE_COUNT=4");',
        'print("T15_UNIQUE_MAX_POLE=RA2_POLE2");',
        'print("T15_PADDED_CUTOFF_IDENTICAL=1");',
    ]
    coeffs = base.source_coefficients(
        "p", "sigma*a1", "sigma*a0", "sigma^5*c1", "sigma^5*c0",
        "sigma^2*b1", "sigma^2*b0",
    )
    loads = {"k10": "k0", "k6": "k6", "k2": "k2load"}
    base.extraction(lines, prefix, tail_base, tails, coeffs, loads, CEILING, CEILING)

    inv1 = "(1-(p/2)*t^2+((p^2)/4)*t^4-((p^3)/8)*t^6+((p^4)/16)*t^8)"
    inv2 = "(1-p*t^2+(3*(p^2)/4)*t^4-((p^3)/2)*t^6+(5*(p^4)/16)*t^8)"
    inv3 = "(1-(3*p/2)*t^2+(3*(p^2)/2)*t^4-(5*(p^3)/4)*t^6+(15*(p^4)/16)*t^8)"
    hshift = base.universal_hshift(
        "sigma*(a1+a0*t)", "sigma^5*(c1+c0*t)",
        "sigma^2*(b1+b0*t)", "k0", inv1, inv2, inv3,
    )
    base.analytic_extract(lines, prefix, hshift, CEILING, CEILING)
    base.row_checks(lines, prefix, v1, CEILING, CEILING)

    lines += [
        "poly T15_L=z^2+p/2;",
        "poly T15_A=a1*z+a0; poly T15_C=c1*z+c0; poly T15_R=b1*z+b0;",
        "poly T15_N2=T15_h16_1*z^3+T15_h16_2*z^2"
        "+(T15_h16_3+p*T15_h16_1)*z+(T15_h16_4+p*T15_h16_2);",
        "poly T15_N2Expected=(3/4)*T15_A*T15_C*T15_L"
        "+(5/32)*k0*T15_A^2*T15_L+(5/16)*k0*T15_R^3*T15_L"
        "-(3/8)*T15_R*T15_A^2;",
        "int T15_common_numerator=(T15_N2-T15_N2Expected==0);",
        "int T15_recurrence=(T15_h16_5+p*T15_h16_3+((p^2)/4)*T15_h16_1==0"
        " && T15_h16_6+p*T15_h16_4+((p^2)/4)*T15_h16_2==0"
        " && T15_h16_7+p*T15_h16_5+((p^2)/4)*T15_h16_3==0);",
        "poly T15_PsiPlus=T15_g16_4+lam*(T15_g16_3+(p/4)*T15_g16_1);",
        "poly T15_PsiMinus=T15_g16_4-lam*(T15_g16_3+(p/4)*T15_g16_1);",
        "poly T15_DPsiPlus=T15_g16_3+2*lam*T15_g16_2-(3*p/4)*T15_g16_1;",
        "poly T15_DPsiMinus=T15_g16_3-2*lam*T15_g16_2-(3*p/4)*T15_g16_1;",
        "poly T15_NPlus=subst(T15_N2,z,lam); poly T15_NMinus=subst(T15_N2,z,-lam);",
        "poly T15_DN=diff(T15_N2,z);",
        "poly T15_DNPlus=subst(T15_DN,z,lam); poly T15_DNMinus=subst(T15_DN,z,-lam);",
        "T15_PsiPlus=subst(T15_PsiPlus,p,-2*lam^2);"
        " T15_PsiMinus=subst(T15_PsiMinus,p,-2*lam^2);",
        "T15_DPsiPlus=subst(T15_DPsiPlus,p,-2*lam^2);"
        " T15_DPsiMinus=subst(T15_DPsiMinus,p,-2*lam^2);",
        "T15_NPlus=subst(T15_NPlus,p,-2*lam^2); T15_NMinus=subst(T15_NMinus,p,-2*lam^2);",
        "T15_DNPlus=subst(T15_DNPlus,p,-2*lam^2); T15_DNMinus=subst(T15_DNMinus,p,-2*lam^2);",
        "int T15_root_faber=(T15_PsiPlus-T15_NPlus==0 && T15_PsiMinus-T15_NMinus==0);",
        "int T15_derivative_syzygy=(T15_DPsiPlus-T15_DNPlus==0 && T15_DPsiMinus-T15_DNMinus==0);",
        "poly T15_Ap=lam*a1+a0; poly T15_Am=-lam*a1+a0;",
        "poly T15_Rp=lam*b1+b0; poly T15_Rm=-lam*b1+b0;",
        "int T15_maxpole_roots=(T15_PsiPlus+(3/8)*T15_Rp*T15_Ap^2==0"
        " && T15_PsiMinus+(3/8)*T15_Rm*T15_Am^2==0);",
        "ideal T15_Ipp=std(ideal(T15_PsiPlus,iAp*T15_Ap-1,iRp*T15_Rp-1,ilam*lam-1));",
        "ideal T15_Imm=std(ideal(T15_PsiMinus,iAm*T15_Am-1,iRm*T15_Rm-1,ilam*lam-1));",
        "int T15_same_root_empty=(reduce(1,T15_Ipp)==0 && reduce(1,T15_Imm)==0);",
        "ideal T15_Ipm=std(ideal(T15_PsiPlus,T15_PsiMinus,T15_DPsiMinus,"
        "iAp*T15_Ap-1,iRm*T15_Rm-1,ilam*lam-1,ik0*k0-1));",
        "ideal T15_Imp=std(ideal(T15_PsiPlus,T15_PsiMinus,T15_DPsiPlus,"
        "iAm*T15_Am-1,iRp*T15_Rp-1,ilam*lam-1,ik0*k0-1));",
        "int T15_opposite_root_empty=(reduce(1,T15_Ipm)==0 && reduce(1,T15_Imp)==0);",
        "ideal T15_EvalUnit=std(ideal(2*lam,ilam*lam-1));",
        "int T15_evaluation_cover=(reduce(1,T15_EvalUnit)==0);",
        "poly T15_L0=z^2-lam^2;",
        "poly T15_OriPlus=subst(T15_N2,p,-2*lam^2);",
        "T15_OriPlus=subst(T15_OriPlus,a1,au); T15_OriPlus=subst(T15_OriPlus,a0,-au*lam);",
        "T15_OriPlus=subst(T15_OriPlus,b1,bu); T15_OriPlus=subst(T15_OriPlus,b0,bu*lam);",
        "poly T15_QPlus=T15_OriPlus/T15_L0;",
        "int T15_div_plus=(T15_L0*T15_QPlus-T15_OriPlus==0);",
        "poly T15_TermPlus=subst(T15_QPlus,z,lam);",
        "poly T15_OriMinus=subst(T15_N2,p,-2*lam^2);",
        "T15_OriMinus=subst(T15_OriMinus,a1,au); T15_OriMinus=subst(T15_OriMinus,a0,au*lam);",
        "T15_OriMinus=subst(T15_OriMinus,b1,bu); T15_OriMinus=subst(T15_OriMinus,b0,-bu*lam);",
        "poly T15_QMinus=T15_OriMinus/T15_L0;",
        "int T15_div_minus=(T15_L0*T15_QMinus-T15_OriMinus==0);",
        "poly T15_TermMinus=subst(T15_QMinus,z,-lam);",
        "int T15_quotient_terminals=(T15_TermPlus-(5/2)*k0*lam^3*bu^3==0"
        " && T15_TermMinus+(5/2)*k0*lam^3*bu^3==0);",
        "poly T15_DerivOriPlus=T15_DPsiPlus;",
        "T15_DerivOriPlus=subst(T15_DerivOriPlus,a1,au);"
        " T15_DerivOriPlus=subst(T15_DerivOriPlus,a0,-au*lam);",
        "T15_DerivOriPlus=subst(T15_DerivOriPlus,b1,bu);"
        " T15_DerivOriPlus=subst(T15_DerivOriPlus,b0,bu*lam);",
        "poly T15_DerivOriMinus=T15_DPsiMinus;",
        "T15_DerivOriMinus=subst(T15_DerivOriMinus,a1,au);"
        " T15_DerivOriMinus=subst(T15_DerivOriMinus,a0,au*lam);",
        "T15_DerivOriMinus=subst(T15_DerivOriMinus,b1,bu);"
        " T15_DerivOriMinus=subst(T15_DerivOriMinus,b0,-bu*lam);",
        "int T15_derivative_terminals=(T15_DerivOriPlus-5*k0*lam^4*bu^3==0"
        " && T15_DerivOriMinus-5*k0*lam^4*bu^3==0);",
        "ideal T15_UnitPlus=std(ideal(T15_TermPlus,ilam*lam-1,ibu*bu-1,ik0*k0-1));",
        "ideal T15_UnitMinus=std(ideal(T15_TermMinus,ilam*lam-1,ibu*bu-1,ik0*k0-1));",
        "int T15_terminal_units=(reduce(1,T15_UnitPlus)==0 && reduce(1,T15_UnitMinus)==0);",
        "poly T15_NoR3=T15_N2Expected-(5/16)*k0*T15_R^3*T15_L;",
        "T15_NoR3=subst(T15_NoR3,p,-2*lam^2);",
        "T15_NoR3=subst(T15_NoR3,a1,au); T15_NoR3=subst(T15_NoR3,a0,-au*lam);",
        "T15_NoR3=subst(T15_NoR3,b1,bu); T15_NoR3=subst(T15_NoR3,b0,bu*lam);",
        "poly T15_NoR3Q=T15_NoR3/T15_L0;",
        "int T15_negctrl_no_r3=(T15_L0*T15_NoR3Q-T15_NoR3==0"
        " && subst(T15_NoR3Q,z,lam)==0);",
        "int T15_targetfree_all7=T15_forbidden;",
        "int T15_endpoint=T15_divisible*T15_identities*T15_forbidden*T15_analyticDiv*T15_row16"
        "*T15_common_numerator*T15_recurrence*T15_root_faber*T15_derivative_syzygy"
        "*T15_maxpole_roots*T15_same_root_empty*T15_opposite_root_empty*T15_evaluation_cover"
        "*T15_div_plus*T15_div_minus*T15_quotient_terminals*T15_derivative_terminals"
        "*T15_terminal_units*T15_negctrl_no_r3;",
        'print("T15_ALL_SEVEN_ROWS_BRIDGED="+string(T15_row16));',
        'print("T15_ALL_SOURCE_QUOTIENTS_EXACT="+string(T15_identities));',
        'print("T15_TARGETFREE_ALL_SEVEN="+string(T15_targetfree_all7));',
        'print("T15_COMMON_N2="+string(T15_common_numerator));',
        'print("T15_L2_RECURRENCE="+string(T15_recurrence));',
        'print("T15_BOTH_ROOT_FABER_IDENTITIES="+string(T15_root_faber));',
        'print("T15_DERIVATIVE_ROW_SYZYGY="+string(T15_derivative_syzygy));',
        'print("T15_FOUR_ROOT_VALUE_CHARTS_COVERED="+string(T15_same_root_empty*T15_opposite_root_empty*T15_evaluation_cover));',
        'print("T15_BOTH_EXACT_L_QUOTIENTS="+string(T15_div_plus*T15_div_minus));',
        'print("T15_QUOTIENT_TERMINALS=PLUS_MINUS_5_OVER_2_K0_LAM3_BU3");',
        'print("T15_DERIVATIVE_TERMINALS=5_K0_LAM4_BU3");',
        'print("T15_EXACT_TERMINAL_UNITS="+string(T15_terminal_units));',
        'print("T15_NEGCTRL_OMIT_R3_ZERO_TERMINAL="+string(T15_negctrl_no_r3));',
        'print("T15_FIRST_POLE_ONLY=ALLOCATION_NOT_ENDPOINT");',
        'if (T15_endpoint!=1) { print("T15_FAIL=SOURCE_INVENTORY_ROOT_SYZYGY_OR_UNIT"); quit; }',
        'print("T15_ENDPOINT=PASS_EMPTY_A1_C5_R2_ON_D_P_K0");',
        "quit;",
    ]

    output = args.output.resolve()
    if output.exists():
        fail("tied maximal-pole output already exists")
    output.mkdir(parents=True)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_d1_tied_a1c5r2_maxpole2_{label}.sing"
    target.write_text("\n".join(lines) + "\n")
    inventory = {
        "status": "PASS-D1-TIED-A1C5R2-MAXPOLE2-COMPILER",
        "scope": "A1_C5_R2_UNIT_LOAD_G16_ON_D_P_K0_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "ceiling": CEILING,
        "primitive_count": len(primitive),
        "primitive_families": primitive,
        "unique_maximal_pole": "-3/8*R*A^2/L^2",
        "source_jet_count": 7,
        "target_jet_count": 0,
        "input_sha256": digest(target),
    }
    inventory_path = output / "source_inventory.json"
    inventory_path.write_text(json.dumps(inventory, sort_keys=True, indent=2) + "\n")
    print(json.dumps(inventory, sort_keys=True))


if __name__ == "__main__":
    main()
