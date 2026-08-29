#!/usr/bin/env python3
"""AWS-only sparse extraction of E^2 P3+16 E P5+96 P7 at grade 48."""

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
ENGINE = ROOT / "cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_sparse_dag_v4_20260826/compute_sparse_dag_v4.py"
ENGINE_SHA = "c539fad9a47299faa4a9afe1dbf3ee6ac868f3e8ef7cdbe7bd277c1ddd4d36d2"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only secondary odd DAG refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only secondary odd DAG refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_engine():
    if digest(ENGINE) != ENGINE_SHA:
        fail("frozen sparse engine mismatch")
    spec = importlib.util.spec_from_file_location("sparse_dag_v4", ENGINE)
    if spec is None or spec.loader is None:
        fail("cannot import frozen sparse engine")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build_functional(engine, field, tails):
    v = {name: engine.dense_var(field, name) for name in engine.ABS_VARS}
    add, mul = engine.dense_add, engine.dense_mul
    scale = engine.dense_scale
    a, e, m = v["a"], v["E"], v["M"]
    x, y, r1, r0, s1, s0, lam = (v[name] for name in ("X", "Y", "R1", "R0", "S1", "S0", "lambda"))
    a2 = mul(field, a, a)
    qp = add(field, e, scale(field, a2, -6))
    qc = add(field, scale(field, mul(field, a, add(field, scale(field, a2, 4), scale(field, e, -1))), 2), x, r1)
    qr = add(field, mul(field, a2, add(field, e, scale(field, a2, -3))), r0, scale(field, mul(field, a, add(field, x, r1)), -1))
    n3 = mul(field, lam, m)
    n2 = mul(field, lam, mul(field, a, m))
    n1 = mul(field, lam, add(field, mul(field, add(field, e, scale(field, a2, -5)), m), y, s1))
    n0 = mul(field, lam, add(
        field,
        scale(field, mul(field, mul(field, a, add(field, e, scale(field, a2, -3))), m), -1),
        scale(field, mul(field, a, y), -1), scale(field, mul(field, m, x), Fraction(1, 2)),
        s0, scale(field, mul(field, a, s1), -1),
    ))
    factors = (
        add(field, mul(field, qr, qr), n0),
        add(field, scale(field, mul(field, qc, qr), 2), n1),
        add(field, mul(field, qc, qc), scale(field, mul(field, qp, qr), 2), n2),
        add(field, scale(field, mul(field, qp, qc), 2), n3),
        add(field, mul(field, qp, qp), scale(field, qr, 2)),
        scale(field, qc, 2), scale(field, qp, 2), v["K10"], v["K6"], v["K2"],
    )
    power_cache = {}
    term_cache = {}
    def power(index, exponent):
        key = (index, exponent)
        if key not in power_cache:
            power_cache[key] = engine.dense_pow(field, factors[index], exponent)
        return power_cache[key]
    def term(exponents):
        key = tuple(exponents)
        if key not in term_cache:
            value = engine.dense_const(field, 1)
            for index, exponent in enumerate(key):
                if exponent:
                    value = mul(field, value, power(index, exponent))
            term_cache[key] = value
        return term_cache[key]
    def row(number):
        result = {}
        entries = tails[str(number)]
        for offset, (exponents, coefficient) in enumerate(entries, 1):
            result = add(field, result, scale(field, term(exponents), coefficient))
            if offset % 20 == 0 or offset == len(entries):
                print(f"SECONDARY_ROW_PROGRESS={number}:{offset}/{len(entries)}:support={len(result)}", flush=True)
        return result
    p3, p5, p7 = row(3), row(5), row(7)
    e2 = mul(field, e, e)
    functional = add(
        field, mul(field, e2, p3), scale(field, mul(field, e, p5), 16),
        scale(field, p7, 96), scale(field, v["J"], -24),
    )
    return functional, {
        "row_supports": {"3": len(p3), "5": len(p5), "7": len(p7)},
        "abstract_functional_support": len(functional),
        "factor_power_cache_entries": len(power_cache),
        "tail_term_cache_entries": len(term_cache),
    }


def raw_scalar(engine, field, tails, values):
    def val(name): return field.value(values.get(name, 0))
    add, mul = field.add, field.mul
    def scale(value, scalar): return mul(value, field.value(scalar))
    a, e, m = val("a"), val("E"), val("M")
    x, y, r1, r0, s1, s0, lam = (val(name) for name in ("X", "Y", "R1", "R0", "S1", "S0", "lambda"))
    a2 = mul(a, a)
    qp = add(e, scale(a2, -6))
    qc = add(add(scale(mul(a, add(scale(a2, 4), scale(e, -1))), 2), x), r1)
    qr = add(add(mul(a2, add(e, scale(a2, -3))), r0), scale(mul(a, add(x, r1)), -1))
    n3 = mul(lam, m)
    n2 = mul(lam, mul(a, m))
    n1 = mul(lam, add(add(mul(add(e, scale(a2, -5)), m), y), s1))
    n0 = mul(lam, add(add(add(add(scale(mul(mul(a, add(e, scale(a2, -3))), m), -1), scale(mul(a, y), -1)), scale(mul(m, x), Fraction(1, 2))), s0), scale(mul(a, s1), -1)))
    factors = (
        add(mul(qr, qr), n0), add(scale(mul(qc, qr), 2), n1),
        add(add(mul(qc, qc), scale(mul(qp, qr), 2)), n2), add(scale(mul(qp, qc), 2), n3),
        add(mul(qp, qp), scale(qr, 2)), scale(qc, 2), scale(qp, 2),
        val("K10"), val("K6"), val("K2"),
    )
    def row(number):
        total = field.value(0)
        for exponents, coefficient in tails[str(number)]:
            item = field.value(coefficient)
            for factor, exponent in zip(factors, exponents):
                if exponent:
                    item = mul(item, pow(factor, exponent) if field.p == 0 else pow(factor, exponent, field.p))
            total = add(total, item)
        return total
    return add(add(add(mul(mul(e, e), row(3)), scale(mul(e, row(5)), 16)), scale(row(7), 96)), scale(val("J"), -24))


def null_values(engine, chart):
    values = engine.witness_values(chart)
    if chart == "x":
        values.update({"d60": 20, "d20": 8})
    else:
        values.update({"d60": -70, "d20": Fraction(-59, 2)})
    return values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    engine = load_engine()
    if digest(engine.TAILS) != engine.TAILS_SHA:
        fail("frozen tails mismatch")
    tails = json.loads(engine.TAILS.read_text())
    canonical = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical.encode()).hexdigest() != engine.TAILS_CANONICAL_SHA:
        fail("canonical tails mismatch")
    if {row: len(tails[row]) for row in ("3", "5", "7")} != {"3": 58, "5": 89, "7": 131}:
        fail(("tail counts", {row: len(tails[row]) for row in ("3", "5", "7")}))
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    field = engine.Field(args.characteristic)
    started = time.monotonic()
    functional, abstract_metrics = build_functional(engine, field, tails)
    print("SECONDARY_ABSTRACT_SECONDS=%.3f" % (time.monotonic() - started), flush=True)
    for offset in range(3):
        values = {name: (index + 3) * (offset + 2) - 5 for index, name in enumerate(engine.ABS_VARS)}
        if engine.dense_eval(field, functional, values) != raw_scalar(engine, field, tails, values):
            fail(("abstract scalar control", offset))
    source = engine.source_series(field)
    grade48, extraction_metrics = engine.extract_grade48(field, functional, source)
    expected_old = field.value(-3)
    expected_null = field.value(-2)
    controls = {}
    for chart in ("x", "y"):
        controls[f"old_{chart}"] = engine.jet_eval(field, grade48, engine.witness_values(chart))
        controls[f"null_{chart}"] = engine.jet_eval(field, grade48, null_values(engine, chart))
    expected = {"old_x": expected_old, "old_y": expected_old, "null_x": expected_null, "null_y": expected_null}
    if controls != expected:
        fail(("fixed Singular controls", controls, expected))
    abstract_payload = engine.canonical_dense(field, functional)
    grade48_payload = engine.canonical_jet(field, grade48)
    abstract_bytes = (json.dumps(abstract_payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    grade48_bytes = (json.dumps(grade48_payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    (output / "abstract_secondary_support.json").write_bytes(abstract_bytes)
    (output / "grade48_secondary_sparse.json").write_bytes(grade48_bytes)
    result = {
        "status": "PASS-A-H16-G48-SECONDARY-ODD-DAG-V6",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "engine_sha256": digest(ENGINE),
        "tails_sha256": digest(engine.TAILS),
        "abstract_metrics": abstract_metrics,
        "extraction_metrics": extraction_metrics,
        "abstract_sha256": sha256(abstract_bytes).hexdigest(),
        "grade48_sha256": sha256(grade48_bytes).hexdigest(),
        "controls": {name: field.text(value) for name, value in controls.items()},
        "elapsed_seconds": time.monotonic() - started,
        "scope": "FIXED_H16_Q6_A4_RAW_ROWS_3_5_7_SECONDARY_G48_ONLY_NO_PREDECESSOR_REDUCTION_RATIONAL_REGRADING_REES_ORDER2_MAX12_OR_JC2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("A_H16_SECONDARY_ABSTRACT_SUPPORT=" + str(abstract_metrics["abstract_functional_support"]))
    print("A_H16_SECONDARY_VALUATION_SURVIVORS=" + str(extraction_metrics["valuation_survivor_count"]))
    print("A_H16_SECONDARY_G48_SUPPORT=" + str(extraction_metrics["grade48_support"]))
    for name, value in controls.items(): print("A_H16_SECONDARY_CONTROL_" + name.upper() + "=" + field.text(value))
    print("A_H16_SECONDARY_G48_SHA256=" + result["grade48_sha256"])
    print("A_H16_SECONDARY_ENDPOINT=PASS_COEFFICIENT_ONLY_GRADE48")
    print("A_H16_SECONDARY_DONE=1")
    print("A_H16_SECONDARY_SCOPE=" + result["scope"])


if __name__ == "__main__":
    main()
