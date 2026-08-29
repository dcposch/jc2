#!/usr/bin/env python3
"""AWS-only complete H18/q7/a4 row diagnostic through grade 54."""

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
V5 = ROOT / "cases/max12_812_order2_affine_faber_a_h17_q7_a3_through_g51_sparse_v5_20260826/compute_h17_q7_through_g51_v5.py"
V5_SHA = "4f2fcf2430ed789d76418a5448990c24d2fd8e3dba6d740a978dd60fa6a91eee"
MAX_GRADE = 54
JET_VARS = (
    *(f"d4{i}" for i in range(7)), "nu60",
    *(f"dm{i}" for i in range(5)), *(f"d2{i}" for i in range(5)),
    *(f"d6{i}" for i in range(5)),
    *(f"s0{i}" for i in range(5)), *(f"s1{i}" for i in range(5)),
    *(f"r0{i}" for i in range(5)), *(f"r1{i}" for i in range(5)),
    *(f"y{i}" for i in range(5)), *(f"x{i}" for i in range(5)),
    "m", *(f"m{i}" for i in range(1, 19)),
    "p", *(f"e{i}" for i in range(1, 19)),
    *(f"a{i}" for i in range(4, 19)), *(f"kk{i}" for i in range(13)),
)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only H18/q7 diagnostic refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only H18/q7 diagnostic refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v5():
    if digest(V5) != V5_SHA:
        fail("frozen H17 V5 source mismatch")
    spec = importlib.util.spec_from_file_location("h17q7_v5", V5)
    if spec is None or spec.loader is None:
        fail("cannot import frozen H17 V5 source")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.MAX_GRADE = MAX_GRADE
    module.JET_VARS = JET_VARS
    return module


def prepare(v5):
    v2 = v5.load_v2()
    v2.MAX_GRADE = MAX_GRADE
    base = v2.load_base()
    base.MAX_GRADE = MAX_GRADE
    base.JET_VARS = JET_VARS
    base.JET_INDEX = {name: index for index, name in enumerate(JET_VARS)}
    return v2, base


def source_series(base, field):
    def named(start, names):
        return base.series_from_terms(
            field,
            ((start + i, base.jet_var(field, name)) for i, name in enumerate(names)),
        )

    a = named(4, (f"a{i}" for i in range(4, 19)))
    e = base.series_from_terms(
        field,
        [(0, base.jet_var(field, "p")), *((i, base.jet_var(field, f"e{i}")) for i in range(1, 19))],
    )
    m = base.series_from_terms(
        field,
        [(0, base.jet_var(field, "m")), *((i, base.jet_var(field, f"m{i}")) for i in range(1, 19))],
    )
    x = named(7, (f"x{i}" for i in range(5)))
    y = named(7, (f"y{i}" for i in range(5)))
    r1 = named(14, (f"r1{i}" for i in range(5)))
    r0 = named(14, (f"r0{i}" for i in range(5)))
    s1 = named(14, (f"s1{i}" for i in range(5)))
    s0 = named(14, (f"s0{i}" for i in range(5)))
    kk = named(0, (f"kk{i}" for i in range(13)))
    e2 = base.series_mul(field, e, e)
    e4 = base.series_mul(field, e2, e2)
    e6 = base.series_mul(field, e4, e2)
    d6 = named(8, (f"d6{i}" for i in range(5)))
    d2 = named(8, (f"d2{i}" for i in range(5)))
    dm = named(8, (f"dm{i}" for i in range(5)))
    k10 = base.series_from_terms(field, ((42 + grade, poly) for grade, poly in enumerate(kk) if poly))
    k6_inner = base.series_add(field, base.series_scale(field, base.series_mul(field, kk, e2), Fraction(15, 32)), d6)
    k2_inner = base.series_add(field, base.series_scale(field, base.series_mul(field, kk, e4), Fraction(15, 256)), d2)
    mu2_inner = base.series_add(field, base.series_scale(field, base.series_mul(field, kk, e6), Fraction(-5, 4096)), dm)
    k6 = base.series_from_terms(field, ((42 + grade, poly) for grade, poly in enumerate(k6_inner) if poly))
    k2 = base.series_from_terms(field, ((42 + grade, poly) for grade, poly in enumerate(k2_inner) if poly))
    mu2 = base.series_from_terms(field, ((42 + grade, poly) for grade, poly in enumerate(mu2_inner) if poly))
    mu4 = named(48, (f"d4{i}" for i in range(7)))
    mu6 = named(54, ("nu60",))
    lam = base.series_from_terms(field, ((18, base.jet_const(field, 1)),))
    abstract = {
        "J": base.zero_series(), "K2": k2, "K6": k6, "K10": k10,
        "S0": s0, "S1": s1, "R0": r0, "R1": r1,
        "Y": y, "X": x, "a": a, "lambda": lam, "M": m, "E": e,
    }
    return abstract, mu2, mu4, mu6


def mul_many(base, field, *items):
    result = base.jet_const(field, 1)
    for item in items:
        result = base.jet_mul(field, result, item)
    return result


def expected_grade50(base, field):
    v = lambda name: base.jet_var(field, name)
    add = lambda *items: base.jet_add(field, *items)
    scale = lambda item, scalar: base.jet_scale(field, item, scalar)
    p, m, x, y, a4, kk = v("p"), v("m"), v("x0"), v("y0"), v("a4"), v("kk0")
    r0, r1, s0 = v("r00"), v("r10"), v("s00")
    d6, d2, dm, d42 = v("d60"), v("d20"), v("dm0"), v("d42")
    c1 = add(scale(mul_many(base, field, r1, m, m), Fraction(-3, 8)), scale(mul_many(base, field, s0, m), Fraction(3, 4)))
    c2 = add(
        scale(mul_many(base, field, d6, p, p, p, p), Fraction(3, 128)),
        scale(mul_many(base, field, r0, m, m), Fraction(-3, 8)),
        scale(mul_many(base, field, d2, p, p), Fraction(-1, 8)),
        scale(mul_many(base, field, y, y), Fraction(3, 8)), scale(dm, -1),
        scale(mul_many(base, field, kk, a4, a4, p, p, p, p, p), Fraction(15, 128)),
    )
    c3 = add(
        scale(mul_many(base, field, r1, m, m, p), Fraction(-3, 32)),
        scale(mul_many(base, field, m, x, y), Fraction(-3, 8)),
        scale(mul_many(base, field, s0, m, p), Fraction(3, 16)),
    )
    c4 = add(
        scale(mul_many(base, field, m, m, x, x), Fraction(3, 32)),
        scale(mul_many(base, field, p, m, m, r0), Fraction(-3, 16)),
        scale(mul_many(base, field, p, y, y), Fraction(-3, 16)), scale(d42, -1),
    )
    c5 = add(scale(mul_many(base, field, p, p, c1), Fraction(3, 32)), scale(mul_many(base, field, p, c3), Fraction(-1, 4)))
    c6 = add(
        scale(mul_many(base, field, d6, p, p, p, p, p, p), Fraction(-1, 512)),
        scale(mul_many(base, field, r0, m, m, p, p), Fraction(-3, 64)),
        scale(mul_many(base, field, d2, p, p, p, p), Fraction(1, 128)),
        scale(mul_many(base, field, y, y, p, p), Fraction(3, 64)),
        scale(mul_many(base, field, kk, a4, a4, p, p, p, p, p, p, p), Fraction(-15, 1024)),
    )
    c7 = add(scale(mul_many(base, field, p, p, c3), Fraction(1, 32)), scale(mul_many(base, field, p, p, p, c1), Fraction(-1, 64)))
    return {1: c1, 2: c2, 3: c3, 4: c4, 5: c5, 6: c6, 7: c7}


def canonical_poly(base, field, poly):
    return {
        "variables": list(JET_VARS),
        "terms": [
            {"monomial": [[JET_VARS[index], exponent] for index, exponent in monomial], "coefficient": field.text(coefficient)}
            for monomial, coefficient in sorted(poly.items())
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    v5 = load_v5()
    v2, base = prepare(v5)
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
    source, mu2, mu4, mu6 = source_series(base, field)
    rows = {}
    survivors = {}
    for number in range(1, 8):
        rows[number], survivors[number] = v2.expand_row(base, field, abstract_rows[number], source)
    rows[2] = base.series_add(field, rows[2], base.series_scale(field, mu2, -1))
    rows[4] = base.series_add(field, rows[4], base.series_scale(field, mu4, -1))
    rows[6] = base.series_add(field, rows[6], base.series_scale(field, mu6, -1))
    for number in range(1, 8):
        for grade in range(42):
            if rows[number][grade]:
                fail(("nonzero row below grade42", number, grade, rows[number][grade]))
        for grade in range(42, 48):
            if rows[number][grade]:
                fail(("affine graph failed below mu4", number, grade, rows[number][grade]))
    zero = base.jet_const(field, 0)
    for grade, name in ((48, "d40"), (49, "d41")):
        for number in range(1, 8):
            expected = base.jet_scale(field, base.jet_var(field, name), -1) if number == 4 else zero
            if rows[number][grade] != expected:
                fail(("mu4 predecessor mismatch", number, grade, rows[number][grade], expected))
    expected50 = expected_grade50(base, field)
    for number in range(1, 8):
        if rows[number][50] != expected50[number]:
            fail(("grade50 formula mismatch", number, rows[number][50], expected50[number]))
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
    for grade in range(54):
        if hseries[grade]:
            fail(("Hseries unexpectedly below grade54", grade, hseries[grade]))
    v = lambda name: base.jet_var(field, name)
    expected_h54 = base.jet_add(
        field,
        base.jet_scale(field, mul_many(base, field, v("m"), v("m"), v("m"), v("p"), v("p")), -2),
        base.jet_scale(field, mul_many(base, field, v("kk0"), v("a4"), v("a4"), v("a4"), v("p"), v("p"), v("p"), v("p"), v("p"), v("p"), v("p")), Fraction(5, 4)),
    )
    if hseries[54] != expected_h54:
        fail(("Hseries grade54 mismatch", hseries[54], expected_h54))
    nu_key = ((base.JET_INDEX["nu60"], 1),)
    if rows[6][54].get(nu_key) != field.value(-1):
        fail(("mu6 first-target coefficient mismatch", rows[6][54].get(nu_key)))
    for number in (1, 2, 3, 4, 5, 7):
        if nu_key in rows[number][54]:
            fail(("mu6 leaked into wrong row", number))
    row_payload = {
        str(grade): {str(number): canonical_poly(base, field, rows[number][grade]) for number in range(1, 8)}
        for grade in range(42, 55)
    }
    function_payload = {
        "K54": canonical_poly(base, field, kfun[54]),
        "Hseries54": canonical_poly(base, field, hseries[54]),
    }
    row_bytes = (json.dumps(row_payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    function_bytes = (json.dumps(function_payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    (output / "rows_g42_g54.json").write_bytes(row_bytes)
    (output / "functionals_g54.json").write_bytes(function_bytes)
    result = {
        "status": "PASS-A-H18-Q7-A4-THROUGH-G54-V1",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v5_sha256": digest(V5),
        "tails_sha256": digest(base.TAILS),
        "abstract_survivors": {str(number): survivors[number] for number in range(1, 8)},
        "row_supports": {str(grade): {str(number): len(rows[number][grade]) for number in range(1, 8)} for grade in range(42, 55)},
        "K54_support": len(kfun[54]),
        "Hseries54_support": len(hseries[54]),
        "rows_sha256": sha256(row_bytes).hexdigest(),
        "functionals_sha256": sha256(function_bytes).hexdigest(),
        "lower_zero_rows": 7,
        "affine_graph_through_grade47": 1,
        "mu4_predecessors": 2,
        "grade50_control": 1,
        "Hseries54_control": 1,
        "mu6_first_grade": 54,
        "J_first_grade": 57,
        "elapsed_seconds": time.monotonic() - started,
        "scope": "FIXED_H18_Q7_A4_NORMALIZED_GRAPH_ROWS_G42_TO_G54_DIAGNOSTIC_ONLY_NO_SEQUENTIAL_ELIMINATION_SOURCE_ATLAS_TAYLOR_ORDER2_MAX12_OR_JC2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("A_H18Q7G54_ROWS_SHA256=" + result["rows_sha256"])
    print("A_H18Q7G54_FUNCTIONALS_SHA256=" + result["functionals_sha256"])
    print("A_H18Q7G54_LOWER_ZERO=1")
    print("A_H18Q7G54_AFFINE_GRAPH47=1")
    print("A_H18Q7G54_MU4_PREDECESSORS=1")
    print("A_H18Q7G54_GRADE50_CONTROL=1")
    print("A_H18Q7G54_HSERIES54_CONTROL=1")
    print("A_H18Q7G54_MU6_FIRST=54")
    print("A_H18Q7G54_J_FIRST=57")
    print("A_H18Q7G54_ENDPOINT=PASS_COMPLETE_ROWS_THROUGH_GRADE54")
    print("A_H18Q7G54_DONE=1")
    print("A_H18Q7G54_SCOPE=" + result["scope"])


if __name__ == "__main__":
    main()
