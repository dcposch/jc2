#!/usr/bin/env python3
"""Compile the tied (a,r)=(1,2), closed c>=6 maximal-pole producer; AWS only."""

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
        "9da5bd405e8d454ca9c93ef1151a6e44a76fbdeb51f79b3340ea458dd93e0764",
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
BASELINE = {"A": 1, "C": 6, "R": 2}
CEILING = 16


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only tied c>=6 maximal-pole compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only tied c>=6 maximal-pole compiler refused non-Amazon host")
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
    prefix = "TC6_"
    lines = [
        f"ring Rc6={args.characteristic},({variables}),dp;",
        'print("TC6_SOURCE_HASHES=PASS");',
        'print("TC6_COMPILER_VERSION=V2_ORDINARY_PART_REMAINDER");',
        'print("TC6_SCOPE=A1_R2_CGE6_UNIT_LOAD_G16_ONLY");',
        'print("TC6_PRIMITIVE_COUNT=3");',
        'print("TC6_UNIQUE_MAX_POLE=RA2_POLE2");',
        'print("TC6_PADDED_CUTOFF_IDENTICAL=1");',
    ]
    coeffs = base.source_coefficients(
        "p", "sigma*a1", "sigma*a0", "sigma^6*c1", "sigma^6*c0",
        "sigma^2*b1", "sigma^2*b0",
    )
    loads = {"k10": "k0", "k6": "k6", "k2": "k2load"}
    base.extraction(lines, prefix, tail_base, tails, coeffs, loads, CEILING, CEILING)

    inv1 = "(1-(p/2)*t^2+((p^2)/4)*t^4-((p^3)/8)*t^6+((p^4)/16)*t^8)"
    inv2 = "(1-p*t^2+(3*(p^2)/4)*t^4-((p^3)/2)*t^6+(5*(p^4)/16)*t^8)"
    inv3 = "(1-(3*p/2)*t^2+(3*(p^2)/2)*t^4-(5*(p^3)/4)*t^6+(15*(p^4)/16)*t^8)"
    hshift = base.universal_hshift(
        "sigma*(a1+a0*t)", "sigma^6*(c1+c0*t)",
        "sigma^2*(b1+b0*t)", "k0", inv1, inv2, inv3,
    )
    base.analytic_extract(lines, prefix, hshift, CEILING, CEILING)
    base.row_checks(lines, prefix, v1, CEILING, CEILING)

    lines += [
        "poly TC6_L=z^2+p/2;",
        "poly TC6_A=a1*z+a0; poly TC6_C=c1*z+c0; poly TC6_R=b1*z+b0;",
        "poly TC6_N2=TC6_h16_1*z^3+TC6_h16_2*z^2"
        "+(TC6_h16_3+p*TC6_h16_1)*z+(TC6_h16_4+p*TC6_h16_2);",
        "poly TC6_N2Expected=(5/32)*k0*TC6_A^2*TC6_L+(5/16)*k0*TC6_R^3*TC6_L"
        "-(3/8)*TC6_R*TC6_A^2;",
        "ideal TC6_L2Ideal=std(ideal(TC6_L^2));",
        "poly TC6_OrdinaryQuotient=(TC6_N2Expected-TC6_N2)/(TC6_L^2);",
        "int TC6_common_numerator=(reduce(TC6_N2-TC6_N2Expected,TC6_L2Ideal)==0"
        " && TC6_N2+(TC6_L^2)*TC6_OrdinaryQuotient-TC6_N2Expected==0);",
        "int TC6_recurrence=(TC6_h16_5+p*TC6_h16_3+((p^2)/4)*TC6_h16_1==0"
        " && TC6_h16_6+p*TC6_h16_4+((p^2)/4)*TC6_h16_2==0"
        " && TC6_h16_7+p*TC6_h16_5+((p^2)/4)*TC6_h16_3==0);",
        "poly TC6_PsiPlus=TC6_g16_4+lam*(TC6_g16_3+(p/4)*TC6_g16_1);",
        "poly TC6_PsiMinus=TC6_g16_4-lam*(TC6_g16_3+(p/4)*TC6_g16_1);",
        "poly TC6_DPsiPlus=TC6_g16_3+2*lam*TC6_g16_2-(3*p/4)*TC6_g16_1;",
        "poly TC6_DPsiMinus=TC6_g16_3-2*lam*TC6_g16_2-(3*p/4)*TC6_g16_1;",
        "poly TC6_NPlus=subst(TC6_N2,z,lam); poly TC6_NMinus=subst(TC6_N2,z,-lam);",
        "poly TC6_DN=diff(TC6_N2,z);",
        "poly TC6_DNPlus=subst(TC6_DN,z,lam); poly TC6_DNMinus=subst(TC6_DN,z,-lam);",
        "TC6_PsiPlus=subst(TC6_PsiPlus,p,-2*lam^2);"
        " TC6_PsiMinus=subst(TC6_PsiMinus,p,-2*lam^2);",
        "TC6_DPsiPlus=subst(TC6_DPsiPlus,p,-2*lam^2);"
        " TC6_DPsiMinus=subst(TC6_DPsiMinus,p,-2*lam^2);",
        "TC6_NPlus=subst(TC6_NPlus,p,-2*lam^2); TC6_NMinus=subst(TC6_NMinus,p,-2*lam^2);",
        "TC6_DNPlus=subst(TC6_DNPlus,p,-2*lam^2); TC6_DNMinus=subst(TC6_DNMinus,p,-2*lam^2);",
        "int TC6_root_faber=(TC6_PsiPlus-TC6_NPlus==0 && TC6_PsiMinus-TC6_NMinus==0);",
        "int TC6_derivative_syzygy=(TC6_DPsiPlus-TC6_DNPlus==0 && TC6_DPsiMinus-TC6_DNMinus==0);",
        "poly TC6_Ap=lam*a1+a0; poly TC6_Am=-lam*a1+a0;",
        "poly TC6_Rp=lam*b1+b0; poly TC6_Rm=-lam*b1+b0;",
        "int TC6_maxpole_roots=(TC6_PsiPlus+(3/8)*TC6_Rp*TC6_Ap^2==0"
        " && TC6_PsiMinus+(3/8)*TC6_Rm*TC6_Am^2==0);",
        "int TC6_c_delayed=(diff(TC6_h16_1,c1)==0 && diff(TC6_h16_1,c0)==0"
        " && diff(TC6_h16_2,c1)==0 && diff(TC6_h16_2,c0)==0"
        " && diff(TC6_h16_3,c1)==0 && diff(TC6_h16_3,c0)==0"
        " && diff(TC6_h16_4,c1)==0 && diff(TC6_h16_4,c0)==0"
        " && diff(TC6_h16_5,c1)==0 && diff(TC6_h16_5,c0)==0"
        " && diff(TC6_h16_6,c1)==0 && diff(TC6_h16_6,c0)==0"
        " && diff(TC6_h16_7,c1)==0 && diff(TC6_h16_7,c0)==0);",
        "ideal TC6_Ipp=std(ideal(TC6_PsiPlus,iAp*TC6_Ap-1,iRp*TC6_Rp-1,ilam*lam-1));",
        "ideal TC6_Imm=std(ideal(TC6_PsiMinus,iAm*TC6_Am-1,iRm*TC6_Rm-1,ilam*lam-1));",
        "int TC6_same_root_empty=(reduce(1,TC6_Ipp)==0 && reduce(1,TC6_Imm)==0);",
        "ideal TC6_Ipm=std(ideal(TC6_PsiPlus,TC6_PsiMinus,TC6_DPsiMinus,"
        "iAp*TC6_Ap-1,iRm*TC6_Rm-1,ilam*lam-1,ik0*k0-1));",
        "ideal TC6_Imp=std(ideal(TC6_PsiPlus,TC6_PsiMinus,TC6_DPsiPlus,"
        "iAm*TC6_Am-1,iRp*TC6_Rp-1,ilam*lam-1,ik0*k0-1));",
        "int TC6_opposite_root_empty=(reduce(1,TC6_Ipm)==0 && reduce(1,TC6_Imp)==0);",
        "ideal TC6_EvalUnit=std(ideal(2*lam,ilam*lam-1));",
        "int TC6_evaluation_cover=(reduce(1,TC6_EvalUnit)==0);",
        "poly TC6_L0=z^2-lam^2;",
        "poly TC6_OriPlus=subst(TC6_N2,p,-2*lam^2);",
        "TC6_OriPlus=subst(TC6_OriPlus,a1,au); TC6_OriPlus=subst(TC6_OriPlus,a0,-au*lam);",
        "TC6_OriPlus=subst(TC6_OriPlus,b1,bu); TC6_OriPlus=subst(TC6_OriPlus,b0,bu*lam);",
        "poly TC6_QPlus=TC6_OriPlus/TC6_L0;",
        "int TC6_div_plus=(TC6_L0*TC6_QPlus-TC6_OriPlus==0);",
        "poly TC6_TermPlus=subst(TC6_QPlus,z,lam);",
        "poly TC6_OriMinus=subst(TC6_N2,p,-2*lam^2);",
        "TC6_OriMinus=subst(TC6_OriMinus,a1,au); TC6_OriMinus=subst(TC6_OriMinus,a0,au*lam);",
        "TC6_OriMinus=subst(TC6_OriMinus,b1,bu); TC6_OriMinus=subst(TC6_OriMinus,b0,-bu*lam);",
        "poly TC6_QMinus=TC6_OriMinus/TC6_L0;",
        "int TC6_div_minus=(TC6_L0*TC6_QMinus-TC6_OriMinus==0);",
        "poly TC6_TermMinus=subst(TC6_QMinus,z,-lam);",
        "int TC6_quotient_terminals=(TC6_TermPlus-(5/2)*k0*lam^3*bu^3==0"
        " && TC6_TermMinus+(5/2)*k0*lam^3*bu^3==0);",
        "poly TC6_DerivOriPlus=TC6_DPsiPlus;",
        "TC6_DerivOriPlus=subst(TC6_DerivOriPlus,a1,au);"
        " TC6_DerivOriPlus=subst(TC6_DerivOriPlus,a0,-au*lam);",
        "TC6_DerivOriPlus=subst(TC6_DerivOriPlus,b1,bu);"
        " TC6_DerivOriPlus=subst(TC6_DerivOriPlus,b0,bu*lam);",
        "poly TC6_DerivOriMinus=TC6_DPsiMinus;",
        "TC6_DerivOriMinus=subst(TC6_DerivOriMinus,a1,au);"
        " TC6_DerivOriMinus=subst(TC6_DerivOriMinus,a0,au*lam);",
        "TC6_DerivOriMinus=subst(TC6_DerivOriMinus,b1,bu);"
        " TC6_DerivOriMinus=subst(TC6_DerivOriMinus,b0,-bu*lam);",
        "int TC6_derivative_terminals=(TC6_DerivOriPlus-5*k0*lam^4*bu^3==0"
        " && TC6_DerivOriMinus-5*k0*lam^4*bu^3==0);",
        "ideal TC6_UnitPlus=std(ideal(TC6_TermPlus,ilam*lam-1,ibu*bu-1,ik0*k0-1));",
        "ideal TC6_UnitMinus=std(ideal(TC6_TermMinus,ilam*lam-1,ibu*bu-1,ik0*k0-1));",
        "int TC6_terminal_units=(reduce(1,TC6_UnitPlus)==0 && reduce(1,TC6_UnitMinus)==0);",
        "poly TC6_NoR3=TC6_N2Expected-(5/16)*k0*TC6_R^3*TC6_L;",
        "TC6_NoR3=subst(TC6_NoR3,p,-2*lam^2);",
        "TC6_NoR3=subst(TC6_NoR3,a1,au); TC6_NoR3=subst(TC6_NoR3,a0,-au*lam);",
        "TC6_NoR3=subst(TC6_NoR3,b1,bu); TC6_NoR3=subst(TC6_NoR3,b0,bu*lam);",
        "poly TC6_NoR3Q=TC6_NoR3/TC6_L0;",
        "int TC6_negctrl_no_r3=(TC6_L0*TC6_NoR3Q-TC6_NoR3==0"
        " && subst(TC6_NoR3Q,z,lam)==0);",
        "int TC6_targetfree_all7=TC6_forbidden;",
        "int TC6_endpoint=TC6_divisible*TC6_identities*TC6_forbidden*TC6_analyticDiv*TC6_row16"
        "*TC6_common_numerator*TC6_recurrence*TC6_root_faber*TC6_derivative_syzygy"
        "*TC6_maxpole_roots*TC6_c_delayed*TC6_same_root_empty*TC6_opposite_root_empty*TC6_evaluation_cover"
        "*TC6_div_plus*TC6_div_minus*TC6_quotient_terminals*TC6_derivative_terminals"
        "*TC6_terminal_units*TC6_negctrl_no_r3;",
        'print("TC6_ALL_SEVEN_ROWS_BRIDGED="+string(TC6_row16));',
        'print("TC6_ALL_SOURCE_QUOTIENTS_EXACT="+string(TC6_identities));',
        'print("TC6_TARGETFREE_ALL_SEVEN="+string(TC6_targetfree_all7));',
        'print("TC6_COMMON_N2="+string(TC6_common_numerator));',
        'print("TC6_ORDINARY_PART_QUOTIENT_RETAINED="+string(TC6_common_numerator));',
        'print("TC6_L2_RECURRENCE="+string(TC6_recurrence));',
        'print("TC6_BOTH_ROOT_FABER_IDENTITIES="+string(TC6_root_faber));',
        'print("TC6_DERIVATIVE_ROW_SYZYGY="+string(TC6_derivative_syzygy));',
        'print("TC6_C_DELAYED_BEYOND_G16="+string(TC6_c_delayed));',
        'print("TC6_FOUR_ROOT_VALUE_CHARTS_COVERED="+string(TC6_same_root_empty*TC6_opposite_root_empty*TC6_evaluation_cover));',
        'print("TC6_BOTH_EXACT_L_QUOTIENTS="+string(TC6_div_plus*TC6_div_minus));',
        'print("TC6_QUOTIENT_TERMINALS=PLUS_MINUS_5_OVER_2_K0_LAM3_BU3");',
        'print("TC6_DERIVATIVE_TERMINALS=5_K0_LAM4_BU3");',
        'print("TC6_EXACT_TERMINAL_UNITS="+string(TC6_terminal_units));',
        'print("TC6_NEGCTRL_OMIT_R3_ZERO_TERMINAL="+string(TC6_negctrl_no_r3));',
        'print("TC6_FIRST_POLE_ONLY=ALLOCATION_NOT_ENDPOINT");',
        'if (TC6_endpoint!=1) { print("TC6_FAIL=SOURCE_INVENTORY_ROOT_SYZYGY_OR_UNIT"); quit; }',
        'print("TC6_ENDPOINT=PASS_EMPTY_A1_R2_CGE6_ON_D_P_K0");',
        "quit;",
    ]

    output = args.output.resolve()
    if output.exists():
        fail("tied c>=6 maximal-pole output already exists")
    output.mkdir(parents=True)
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    target = output / f"square_d1_tied_a1r2_cge6_maxpole2_{label}.sing"
    target.write_text("\n".join(lines) + "\n")
    inventory = {
        "status": "PASS-D1-TIED-A1R2-CGE6-MAXPOLE2-COMPILER",
        "scope": "A1_R2_CGE6_UNIT_LOAD_G16_ON_D_P_K0_ONLY",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "ceiling": CEILING,
        "primitive_count": len(primitive),
        "primitive_families": primitive,
        "unique_maximal_pole": "-3/8*R*A^2/L^2",
        "source_jet_count": 5,
        "target_jet_count": 0,
        "input_sha256": digest(target),
    }
    inventory_path = output / "source_inventory.json"
    inventory_path.write_text(json.dumps(inventory, sort_keys=True, indent=2) + "\n")
    print(json.dumps(inventory, sort_keys=True))


if __name__ == "__main__":
    main()
