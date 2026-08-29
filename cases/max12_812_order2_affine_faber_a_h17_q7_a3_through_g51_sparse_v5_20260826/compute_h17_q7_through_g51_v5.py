#!/usr/bin/env python3
"""AWS-only complete H17/q7/a3 row recursion through grade 51."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V2 = ROOT / "cases/max12_812_order2_affine_faber_a_h17_q7_a3_predecessor_g48_sparse_v2_20260826/compute_h17_q7_g48_sparse.py"
V2_SHA = "1ee515a8da4bc86ade10a86dae6a526c57d58eea0061158b977eab2b76020cf4"
MAX_GRADE = 51
JET_VARS = (
    *(f"d4{i}" for i in range(4)), *(f"dm{i}" for i in range(4)),
    *(f"d2{i}" for i in range(4)), *(f"d6{i}" for i in range(4)),
    *(f"s0{i}" for i in range(4)), *(f"s1{i}" for i in range(4)),
    *(f"r0{i}" for i in range(4)), *(f"r1{i}" for i in range(4)),
    *(f"y{i}" for i in range(4)), *(f"x{i}" for i in range(4)),
    "m", *(f"m{i}" for i in range(1, 10)),
    "p", *(f"e{i}" for i in range(1, 10)),
    *(f"a{i}" for i in range(3, 13)), *(f"kk{i}" for i in range(10)),
)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_v2():
    if digest(V2) != V2_SHA:
        fail("frozen V2 source mismatch")
    spec = importlib.util.spec_from_file_location("h17q7_v2", V2)
    if spec is None or spec.loader is None:
        fail("cannot import V2 source")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.MAX_GRADE = MAX_GRADE
    return module


def prepare_base(v2):
    base = v2.load_base()
    base.MAX_GRADE = MAX_GRADE
    base.JET_VARS = JET_VARS
    base.JET_INDEX = {name: index for index, name in enumerate(JET_VARS)}
    return base


def source_series(base, field):
    def named(start, names):
        return base.series_from_terms(field, ((start + i, base.jet_var(field, name)) for i, name in enumerate(names)))

    a = named(3, (f"a{i}" for i in range(3, 13)))
    e = base.series_from_terms(field, [(0, base.jet_var(field, "p")), *((i, base.jet_var(field, f"e{i}")) for i in range(1, 10))])
    m = base.series_from_terms(field, [(0, base.jet_var(field, "m")), *((i, base.jet_var(field, f"m{i}")) for i in range(1, 10))])
    x = named(7, (f"x{i}" for i in range(4))); y = named(7, (f"y{i}" for i in range(4)))
    r1 = named(14, (f"r1{i}" for i in range(4))); r0 = named(14, (f"r0{i}" for i in range(4)))
    s1 = named(14, (f"s1{i}" for i in range(4))); s0 = named(14, (f"s0{i}" for i in range(4)))
    kk = named(0, (f"kk{i}" for i in range(10)))
    e2 = base.series_mul(field, e, e)
    e4 = base.series_mul(field, e2, e2)
    e6 = base.series_mul(field, e4, e2)
    d6 = named(6, (f"d6{i}" for i in range(4)))
    d2 = named(6, (f"d2{i}" for i in range(4)))
    dm = named(6, (f"dm{i}" for i in range(4)))
    k10 = base.series_from_terms(field, ((42 + grade, poly) for grade, poly in enumerate(kk) if poly))
    k6_inner = base.series_add(field, base.series_scale(field, base.series_mul(field, kk, e2), Fraction(15, 32)), d6)
    k2_inner = base.series_add(field, base.series_scale(field, base.series_mul(field, kk, e4), Fraction(15, 256)), d2)
    mu2_inner = base.series_add(field, base.series_scale(field, base.series_mul(field, kk, e6), Fraction(-5, 4096)), dm)
    k6 = base.series_from_terms(field, ((42 + grade, poly) for grade, poly in enumerate(k6_inner) if poly))
    k2 = base.series_from_terms(field, ((42 + grade, poly) for grade, poly in enumerate(k2_inner) if poly))
    mu2 = base.series_from_terms(field, ((42 + grade, poly) for grade, poly in enumerate(mu2_inner) if poly))
    mu4 = named(48, (f"d4{i}" for i in range(4)))
    lam = base.series_from_terms(field, ((17, base.jet_const(field, 1)),))
    abstract = {
        "J": base.zero_series(), "K2": k2, "K6": k6, "K10": k10,
        "S0": s0, "S1": s1, "R0": r0, "R1": r1,
        "Y": y, "X": x, "a": a, "lambda": lam, "M": m, "E": e,
    }
    return abstract, mu2, mu4


def canonical_poly(base, field, poly):
    return {
        "variables": list(JET_VARS),
        "terms": [
            {"monomial": [[JET_VARS[index], exponent] for index, exponent in monomial], "coefficient": field.text(coefficient)}
            for monomial, coefficient in sorted(poly.items())
        ],
    }


def mul_many(base, field, *items):
    result = base.jet_const(field, 1)
    for item in items:
        result = base.jet_mul(field, result, item)
    return result


def corrected_grade48(base, field, v2):
    rename = {
        "d4": "d40", "dm": "dm0", "d2": "d20", "d6": "d60",
        "s0": "s00", "s1": "s10", "r0": "r00", "r1": "r10",
        "y": "y0", "x": "x0", "m": "m", "p": "p", "a3": "a3", "kk0": "kk0",
    }
    old_vars = base.JET_VARS
    old_index = base.JET_INDEX
    small_vars = v2.JET_VARS
    base.JET_VARS = small_vars
    base.JET_INDEX = {name: index for index, name in enumerate(small_vars)}
    small = v2.expected_rows(base, field)
    sv = lambda name: base.jet_var(field, name)
    center2 = mul_many(base, field, sv("kk0"), sv("a3"), sv("a3"), sv("p"), sv("p"), sv("p"), sv("p"), sv("p"))
    center6 = base.jet_mul(field, center2, base.jet_mul(field, sv("p"), sv("p")))
    small[2] = base.jet_add(field, small[2], base.jet_scale(field, center2, Fraction(15, 128)))
    small[6] = base.jet_add(field, small[6], base.jet_scale(field, center6, Fraction(-15, 1024)))
    base.JET_VARS = old_vars
    base.JET_INDEX = old_index
    result = {}
    for number, poly in small.items():
        converted = {}
        for monomial, coefficient in poly.items():
            names = tuple(sorted((old_index[rename[small_vars[index]]], exponent) for index, exponent in monomial))
            converted[names] = coefficient
        result[number] = converted
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    v2 = load_v2()
    base = prepare_base(v2)
    tag = v2.require_aws()
    field = base.Field(args.characteristic)
    if digest(base.TAILS) != v2.TAILS_SHA:
        fail("frozen tails mismatch")
    tails = json.loads(base.TAILS.read_text())
    canonical_tails = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical_tails.encode()).hexdigest() != v2.CANONICAL_SHA:
        fail("canonical tails mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    abstract_rows = v2.build_abstract_rows(base, field, tails)
    source, mu2, mu4 = source_series(base, field)
    rows = {}
    survivors = {}
    for number in range(1, 8):
        rows[number], survivors[number] = v2.expand_row(base, field, abstract_rows[number], source)
    rows[2] = base.series_add(field, rows[2], base.series_scale(field, mu2, -1))
    rows[4] = base.series_add(field, rows[4], base.series_scale(field, mu4, -1))
    for number in range(1, 8):
        for grade in range(48):
            if rows[number][grade]:
                fail(("nonzero row below grade48", number, grade, rows[number][grade]))
    expected48 = corrected_grade48(base, field, v2)
    for number in range(1, 8):
        if rows[number][48] != expected48[number]:
            fail(("grade48 control mismatch", number, rows[number][48], expected48[number]))
    add = lambda *items: base.series_add(field, *items)
    mul = lambda left, right: base.series_mul(field, left, right)
    scale = lambda item, scalar: base.series_scale(field, item, scalar)
    a, e = source["a"], source["E"]
    b = scale(a, 4)
    b2 = mul(b, b); b3 = mul(b2, b); b4 = mul(b2, b2)
    e2 = mul(e, e); e3 = mul(e2, e)
    h3 = add(rows[3], scale(mul(b, rows[2]), Fraction(-1, 2)), mul(add(scale(b2, Fraction(5, 32)), scale(e, Fraction(-1, 4))), rows[1]))
    h5 = add(
        rows[5], scale(mul(b, rows[4]), -1),
        mul(add(scale(b2, Fraction(21, 32)), scale(e, Fraction(-3, 4))), rows[3]),
        mul(add(scale(b3, Fraction(-5, 16)), scale(mul(b, e), Fraction(3, 4))), rows[2]),
        mul(add(scale(b4, Fraction(195, 2048)), scale(mul(b2, e), Fraction(-45, 128)), scale(e2, Fraction(5, 32))), rows[1]),
    )
    kfun = add(mul(e, h3), h5)
    hseries = add(scale(mul(e2, rows[3]), 2), scale(mul(e, rows[5]), 16), scale(rows[7], 64), scale(mul(e3, rows[1]), Fraction(-1, 2)))
    for grade in range(51):
        if hseries[grade]:
            fail(("Hseries unexpectedly below grade51", grade, hseries[grade]))
    v = lambda name: base.jet_var(field, name)
    expected_h51 = base.jet_add(
        field,
        base.jet_scale(field, mul_many(base, field, v("m"), v("m"), v("m"), v("p"), v("p")), -2),
        base.jet_scale(field, mul_many(base, field, v("kk0"), v("a3"), v("a3"), v("a3"), v("p"), v("p"), v("p"), v("p"), v("p"), v("p"), v("p")), Fraction(5, 4)),
    )
    if hseries[51] != expected_h51:
        fail(("Hseries grade51 mismatch", hseries[51], expected_h51))
    row_payload = {
        str(grade): {str(number): canonical_poly(base, field, rows[number][grade]) for number in range(1, 8)}
        for grade in range(48, 52)
    }
    function_payload = {
        "K51": canonical_poly(base, field, kfun[51]),
        "Hseries51": canonical_poly(base, field, hseries[51]),
    }
    row_bytes = (json.dumps(row_payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    function_bytes = (json.dumps(function_payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    (output / "rows_g48_g51.json").write_bytes(row_bytes)
    (output / "functionals_g51.json").write_bytes(function_bytes)
    result = {
        "status": "PASS-A-H17-Q7-A3-THROUGH-G51-V5",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v2_sha256": digest(V2),
        "tails_sha256": digest(base.TAILS),
        "abstract_survivors": {str(number): survivors[number] for number in range(1, 8)},
        "row_supports": {str(grade): {str(number): len(rows[number][grade]) for number in range(1, 8)} for grade in range(48, 52)},
        "K51_support": len(kfun[51]),
        "Hseries51_support": len(hseries[51]),
        "rows_sha256": sha256(row_bytes).hexdigest(),
        "functionals_sha256": sha256(function_bytes).hexdigest(),
        "lower_zero_rows": 7,
        "grade48_control": 1,
        "Hseries51_control": 1,
        "mu6_first_grade": 54,
        "J_first_grade": 57,
        "elapsed_seconds": time.monotonic() - started,
        "scope": "FIXED_H17_Q7_A3_NORMALIZED_GRAPH_ROWS_G48_TO_G51_DIAGNOSTIC_ONLY_NO_ELIMINATION_RATIONAL_REGRADING_SOURCE_REES_ORDER2_MAX12_OR_JC2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("A_H17Q7G51_ROWS_SHA256=" + result["rows_sha256"])
    print("A_H17Q7G51_FUNCTIONALS_SHA256=" + result["functionals_sha256"])
    print("A_H17Q7G51_LOWER_ZERO=1")
    print("A_H17Q7G51_GRADE48_CONTROL=1")
    print("A_H17Q7G51_HSERIES51_CONTROL=1")
    print("A_H17Q7G51_ENDPOINT=PASS_COMPLETE_ROWS_THROUGH_GRADE51")
    print("A_H17Q7G51_DONE=1")
    print("A_H17Q7G51_SCOPE=" + result["scope"])


if __name__ == "__main__":
    main()
