#!/usr/bin/env python3
"""AWS-only exact odd-row direct-unit extraction at H18/q6/a6."""

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
MAX_GRADE = 54
ABS_VALUATIONS = (57, 42, 42, 42, 12, 12, 12, 12, 6, 6, 6, 18, 0, 0)
JET_VARS = (
    *(f"a{i}" for i in range(6, 14)),
    "p", *(f"e{i}" for i in range(1, 13)),
    "m", *(f"m{i}" for i in range(1, 13)),
    *(f"x{i}" for i in range(7)), *(f"y{i}" for i in range(7)),
    *(f"r1{i}" for i in range(7)), *(f"r0{i}" for i in range(7)),
    *(f"s1{i}" for i in range(7)), *(f"s0{i}" for i in range(7)),
    *(f"kk{i}" for i in range(13)),
    *(f"d6{i}" for i in range(7)), *(f"d2{i}" for i in range(7)),
)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only H18/q6 direct-unit client refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only H18/q6 direct-unit client refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_v2():
    if digest(V2) != V2_SHA:
        fail("frozen H17 V2 source mismatch")
    spec = importlib.util.spec_from_file_location("h17q7_v2", V2)
    if spec is None or spec.loader is None:
        fail("cannot import frozen V2 source")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.MAX_GRADE = MAX_GRADE
    module.ABS_VALUATIONS = ABS_VALUATIONS
    module.JET_VARS = JET_VARS
    module.JET_INDEX = {name: index for index, name in enumerate(JET_VARS)}
    return module


def prepare_base(v2):
    base = v2.load_base()
    base.MAX_GRADE = MAX_GRADE
    base.JET_VARS = JET_VARS
    base.JET_INDEX = {name: index for index, name in enumerate(JET_VARS)}
    return base


def source_series(base, field):
    def named(start, names):
        return base.series_from_terms(
            field,
            ((start + i, base.jet_var(field, name)) for i, name in enumerate(names)),
        )

    a = named(6, (f"a{i}" for i in range(6, 14)))
    e = base.series_from_terms(
        field,
        [(0, base.jet_var(field, "p")), *((i, base.jet_var(field, f"e{i}")) for i in range(1, 13))],
    )
    m = base.series_from_terms(
        field,
        [(0, base.jet_var(field, "m")), *((i, base.jet_var(field, f"m{i}")) for i in range(1, 13))],
    )
    x = named(6, (f"x{i}" for i in range(7)))
    y = named(6, (f"y{i}" for i in range(7)))
    r1 = named(12, (f"r1{i}" for i in range(7)))
    r0 = named(12, (f"r0{i}" for i in range(7)))
    s1 = named(12, (f"s1{i}" for i in range(7)))
    s0 = named(12, (f"s0{i}" for i in range(7)))
    kk = named(0, (f"kk{i}" for i in range(13)))
    e2 = base.series_mul(field, e, e)
    e4 = base.series_mul(field, e2, e2)
    d6 = named(6, (f"d6{i}" for i in range(7)))
    d2 = named(6, (f"d2{i}" for i in range(7)))
    k10 = base.series_from_terms(field, ((42 + grade, poly) for grade, poly in enumerate(kk) if poly))
    k6_inner = base.series_add(field, base.series_scale(field, base.series_mul(field, kk, e2), Fraction(15, 32)), d6)
    k2_inner = base.series_add(field, base.series_scale(field, base.series_mul(field, kk, e4), Fraction(15, 256)), d2)
    k6 = base.series_from_terms(field, ((42 + grade, poly) for grade, poly in enumerate(k6_inner) if poly))
    k2 = base.series_from_terms(field, ((42 + grade, poly) for grade, poly in enumerate(k2_inner) if poly))
    lam = base.series_from_terms(field, ((18, base.jet_const(field, 1)),))
    return {
        "J": base.zero_series(), "K2": k2, "K6": k6, "K10": k10,
        "S0": s0, "S1": s1, "R0": r0, "R1": r1,
        "Y": y, "X": x, "a": a, "lambda": lam, "M": m, "E": e,
    }


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
    v2 = load_v2()
    base = prepare_base(v2)
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
    rows = v2.build_abstract_rows(base, field, tails)
    e = base.dense_var(field, "E")
    e2 = base.dense_mul(field, e, e)
    e3 = base.dense_mul(field, e2, e)
    hpoly = base.dense_add(
        field,
        base.dense_scale(field, base.dense_mul(field, e2, rows[3]), 2),
        base.dense_scale(field, base.dense_mul(field, e, rows[5]), 16),
        base.dense_scale(field, rows[7], 64),
        base.dense_scale(field, base.dense_mul(field, e3, rows[1]), Fraction(-1, 2)),
    )
    source = source_series(base, field)
    expanded, survivors = v2.expand_row(base, field, hpoly, source)
    for grade in range(54):
        if expanded[grade]:
            fail(("nonzero H before grade54", grade, expanded[grade]))
    m = base.jet_var(field, "m")
    p = base.jet_var(field, "p")
    expected = base.jet_scale(
        field,
        base.jet_mul(field, base.jet_mul(field, base.jet_mul(field, m, m), m), base.jet_mul(field, p, p)),
        -2,
    )
    if expanded[54] != expected:
        fail(("grade54 direct-unit mismatch", expanded[54], expected))
    payload = {
        "abstract_variables": list(base.ABS_VARS),
        "abstract_support": len(hpoly),
        "survivors_through_grade54": survivors,
        "coefficients": {str(grade): canonical_poly(base, field, expanded[grade]) for grade in range(42, 55)},
    }
    payload_bytes = (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    (output / "hseries_through_g54.json").write_bytes(payload_bytes)
    result = {
        "status": "PASS-A-H18-Q6-A6-G54-DIRECT-UNIT-V1",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "v2_sha256": digest(V2),
        "tails_sha256": digest(base.TAILS),
        "abstract_support": len(hpoly),
        "survivors_through_grade54": survivors,
        "hseries_sha256": sha256(payload_bytes).hexdigest(),
        "lower_zero": 1,
        "grade54_support": len(expanded[54]),
        "elapsed_seconds": time.monotonic() - started,
        "scope": "FIXED_H18_Q6_A6_NORMALIZED_GRAPH_ODD_FUNCTIONAL_G54_ONLY_NO_SOURCE_FIXED_LOCUS_TAYLOR_ORDER2_MAX12_OR_JC2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("A_H18Q6A6_HSERIES_SHA256=" + result["hseries_sha256"])
    print("A_H18Q6A6_ABSTRACT_SUPPORT=" + str(result["abstract_support"]))
    print("A_H18Q6A6_SURVIVORS=" + str(result["survivors_through_grade54"]))
    print("A_H18Q6A6_LOWER_ZERO=1")
    print("A_H18Q6A6_G54=-2*m^3*p^2")
    print("A_H18Q6A6_ENDPOINT=PASS_G54_DIRECT_UNIT")
    print("A_H18Q6A6_DONE=1")
    print("A_H18Q6A6_SCOPE=" + result["scope"])


if __name__ == "__main__":
    main()
