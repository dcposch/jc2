#!/usr/bin/env python3
"""AWS-only sparse first-order q2 syzygy lift."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V1 = (
    ROOT / "cases" /
    "max12_912_order3_d1_double_root_control2_q2_first_lift_v1_20260826" /
    "compile_q2_first_lift.py"
)
V1_SHA = "0385b0b1e60b3bd37fa5fbee90dd6c17a454722bdbff424ea83c2ab0fa19df45"


class LiftFailure(RuntimeError):
    pass


def require_aws():
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith(
        "max12_912_order3_d1_double_root_control2_q2_syzygy_lift_v2_"
    ):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load_v1():
    if sha256(V1.read_bytes()).hexdigest() != V1_SHA:
        raise LiftFailure("V1 hash")
    spec = importlib.util.spec_from_file_location("q2_lift_v1_frozen", V1)
    if spec is None or spec.loader is None:
        raise LiftFailure("V1 import")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def sample_weight(base, monomial):
    e = dict(zip(base.NAMES, monomial))
    return (
        4 * e["la"] + e["tau"] + e["rho"] + 23 * e["q2"]
        + 22 * (e["q1"] + e["q0"])
        + 30 * (e["r2"] + e["r1"] + e["r0"])
    )


def component(base, polynomial, weight):
    return base.clean({m: c for m, c in polynomial.items()
                       if sample_weight(base, m) == weight})


def solve_linear(base, sources, target):
    monomials = sorted(set(target).union(*(set(p) for p in sources)))
    matrix = []
    for monomial in monomials:
        matrix.append(
            [p.get(monomial, Fraction(0)) for p in sources]
            + [target.get(monomial, Fraction(0))]
        )
    rows = len(matrix)
    columns = len(sources)
    pivot_columns = []
    pivot_row = 0
    for column in range(columns):
        selected = next(
            (r for r in range(pivot_row, rows) if matrix[r][column]), None
        )
        if selected is None:
            continue
        matrix[pivot_row], matrix[selected] = matrix[selected], matrix[pivot_row]
        pivot = matrix[pivot_row][column]
        matrix[pivot_row] = [x / pivot for x in matrix[pivot_row]]
        for r in range(rows):
            if r == pivot_row or not matrix[r][column]:
                continue
            factor = matrix[r][column]
            matrix[r] = [x - factor * y
                         for x, y in zip(matrix[r], matrix[pivot_row])]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    for row in matrix:
        if all(not row[c] for c in range(columns)) and row[-1]:
            raise LiftFailure(("inconsistent graded system", monomials, matrix))
    solution = [Fraction(0)] * columns
    for r, column in enumerate(pivot_columns):
        solution[column] = matrix[r][-1]
    check = {}
    for scalar, source in zip(solution, sources):
        check = base.add(check, base.scale(scalar, source))
    if check != target:
        raise LiftFailure(("linear solution check", check, target))
    return monomials, matrix, pivot_columns, solution


def singular_source(base, tag, order, base_b, rows, corrected_fs,
                    witness, corrected, correction, solution):
    if order == "A":
        ring = "ring R=0,(s,la,tau,rho,q2,q1,q0,r2,r1,r0),dp;"
        marker = "PASS_Q2_SYZYGY_LIFT_V2_A_DP"
    else:
        ring = "ring R=0,(s,q2,la,tau,rho,q1,q0,r2,r1,r0),(lp(2),dp(8));"
        marker = "PASS_Q2_SYZYGY_LIFT_V2_B_LPDP"
    lines = [
        "// Expanded exact first-order q2 syzygy lift.",
        ring,
        "option(redSB);",
        f'print("AWS_TAG={tag}");',
        f'print("ENCODING={order}_EXPANDED_Q2_SYZYGY_LIFT_V2");',
    ]
    for ell in range(1, 9):
        lines.extend([
            f"poly BASE{ell}={base_b[ell]};",
            f"poly E{ell}={base.render(rows[ell])};",
            f"poly DIFFROW{ell}=subst(E{ell},q2,0)-subst(BASE{ell},s,1);",
            f'if (DIFFROW{ell}!=0) {{ print("FAIL_BASE_ROW_{ell}"); quit; }}',
            f"poly F{ell}={base.render(corrected_fs[ell])};",
        ])
    lines.extend([
        f"poly W={base.render(witness)};",
        f"poly EXPECT={base.render(corrected)};",
        f"poly CORR={base.render(correction)};",
        "poly WQ2=F1*E1+F2*E2+F3*E3+F4*E4+F5*E5+F6*E6+F7*E7+F8*E8;",
        'if (WQ2-EXPECT!=0) { print("FAIL_EXPECTED_CORRECTED_POLYNOMIAL"); quit; }',
        'if (subst(WQ2,q2,0)-W!=0) { print("FAIL_Q2_ZERO_WITNESS"); quit; }',
        'if (WQ2-W-q2*CORR!=0) { print("FAIL_CORRECTION_FACTOR"); quit; }',
        'print("PASS_ALL_EIGHT_BASE_ROWS");',
        'print("PASS_FIRST_ORDER_GRADED_CANCELLATION");',
        'print("SOLUTION_BEGIN");',
    ])
    for ell, scalar in enumerate(solution, start=1):
        lines.append(f'print("g{ell}={base.frac(scalar)}");')
    lines.extend([
        'print("SOLUTION_END");',
        'print("CORRECTION_BEGIN");',
        "print(CORR);",
        'print("CORRECTION_END");',
        'print("FIREWALL=FIRST_ORDER_Q2_SYZYGY_LIFT_FIXED_AXIS_LOAD_ONLY_ITERATE_IF_LOW_TERMS_REMAIN");',
        f'print("{marker}");',
        "quit;",
    ])
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default=".")
    args = parser.parse_args()
    tag = require_aws()
    base = load_v1()
    charged = base.load_charged()
    tails = charged.build()["tails"]
    images = base.coefficient_images()
    rows = {
        ell: base.add(base.substitute(tails[ell], images),
                      base.scale(-1, base.target(ell)))
        for ell in range(1, 9)
    }
    fs = base.multipliers()
    witness = base.old_witness()
    transported = {}
    for ell in range(1, 9):
        transported = base.add(transported, base.mul(fs[ell], rows[ell]))
    first_correction = base.divide_q2(
        base.add(transported, base.scale(-1, witness))
    )
    c1 = base.specialize_q2_zero(first_correction)
    c52 = component(base, c1, 52)
    if not c52 or min(sample_weight(base, m) for m in c1) != 52:
        raise LiftFailure("expected first coefficient weight 52")
    rows0 = [base.specialize_q2_zero(rows[ell]) for ell in range(1, 9)]
    initial52 = [component(base, row, 52) for row in rows0]
    monomials, rref, pivots, solution = solve_linear(
        base, initial52, base.scale(-1, c52)
    )
    # Independent hand extraction from the expanded base_B rows gives
    # C_52=(1/9)in(E2)-(1/12)in(E1).  Pin the canonical free-zero RREF
    # solution so a row-numbering or initial-form drift fails closed.
    expected_solution = [
        Fraction(1, 12), Fraction(-1, 9), Fraction(0), Fraction(0),
        Fraction(0), Fraction(0), Fraction(0), Fraction(0),
    ]
    if solution != expected_solution:
        raise LiftFailure(("unexpected canonical solution", solution))
    explicit_decomposition = base.add(
        base.scale(Fraction(1, 9), initial52[1]),
        base.scale(Fraction(-1, 12), initial52[0]),
    )
    if explicit_decomposition != c52:
        raise LiftFailure("E1/E2 decomposition mismatch")
    corrected_fs = {}
    for ell, scalar in enumerate(solution, start=1):
        corrected_fs[ell] = base.add(fs[ell], base.mon(scalar, q2=1))
    corrected = {}
    for ell in range(1, 9):
        corrected = base.add(corrected,
                             base.mul(corrected_fs[ell], rows[ell]))
    if base.specialize_q2_zero(corrected) != witness:
        raise LiftFailure("corrected q2-zero mismatch")
    correction = base.divide_q2(
        base.add(corrected, base.scale(-1, witness))
    )
    # The coefficient linear in q2 must now have no weight-52 part.
    corrected_c1 = base.specialize_q2_zero(correction)
    if component(base, corrected_c1, 52):
        raise LiftFailure("weight-52 part did not cancel")
    base_b = base.extract_base_b()
    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    a = singular_source(base, tag, "A", base_b, rows, corrected_fs,
                        witness, corrected, correction, solution)
    b = singular_source(base, tag, "B", base_b, rows, corrected_fs,
                        witness, corrected, correction, solution)
    path_a = output / "q2_syzygy_lift_v2_A_dp.sing"
    path_b = output / "q2_syzygy_lift_v2_B_lpdp.sing"
    path_a.write_text(a)
    path_b.write_text(b)
    records = [base.weight_record(m, c) for m, c in sorted(corrected.items())]
    minimum = min(record["sample_weight"] for record in records)
    payload = {
        "tag": tag,
        "v1_sha256": V1_SHA,
        "graded_monomials": [dict(zip(base.NAMES, m)) for m in monomials],
        "graded_rank": len(pivots),
        "graded_pivot_columns_zero_based": pivots,
        "solution": [str(x) for x in solution],
        "independent_decomposition": "C52=(1/9)in52(E2)-(1/12)in52(E1)",
        "first_bad_sha256": base.digest(c52),
        "corrected_q2_lift_sha256": base.digest(corrected),
        "corrected_correction_sha256": base.digest(correction),
        "corrected_terms": len(corrected),
        "corrected_correction_terms": len(correction),
        "sample_min_weight": minimum,
        "sample_min_terms": [r for r in records if r["sample_weight"] == minimum],
        "outputs": {
            path_a.name: sha256(path_a.read_bytes()).hexdigest(),
            path_b.name: sha256(path_b.read_bytes()).hexdigest(),
        },
        "firewall": "first-order q2 correction only; iterate if minimum <= 80",
    }
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS_Q2_SYZYGY_LIFT_V2_COMPILER")


if __name__ == "__main__":
    main()
