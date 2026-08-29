#!/usr/bin/env python3
"""AWS-only sparse replay of the H17/q7/a3 grade-48 predecessor."""

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
BASE = ROOT / "cases/max12_812_order2_affine_faber_a_h16_q6_a4_g48_sparse_dag_v4_20260826/compute_sparse_dag_v4.py"
BASE_SHA = "c539fad9a47299faa4a9afe1dbf3ee6ac868f3e8ef7cdbe7bd277c1ddd4d36d2"
TAILS_SHA = "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848"
CANONICAL_SHA = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"
MAX_GRADE = 48
ABS_VALUATIONS = (57, 42, 42, 42, 14, 14, 14, 14, 7, 7, 3, 17, 0, 0)
JET_VARS = (
    "d4", "dm", "d2", "d6", "s0", "s1", "r0", "r1", "y", "x", "m",
    *(f"m{i}" for i in range(1, 7)), "p", *(f"e{i}" for i in range(1, 7)),
    *(f"a{i}" for i in range(3, 10)), *(f"kk{i}" for i in range(7)),
)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only H17/q7 sparse replay refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only H17/q7 sparse replay refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def load_base():
    if digest(BASE) != BASE_SHA:
        fail("frozen sparse engine mismatch")
    spec = importlib.util.spec_from_file_location("h16_sparse", BASE)
    if spec is None or spec.loader is None:
        fail("cannot import frozen sparse engine")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.MAX_GRADE = MAX_GRADE
    module.JET_VARS = JET_VARS
    module.JET_INDEX = {name: index for index, name in enumerate(JET_VARS)}
    return module


def build_abstract_rows(base, field, tails):
    variables = {name: base.dense_var(field, name) for name in base.ABS_VARS}
    a, e, m = variables["a"], variables["E"], variables["M"]
    x, y = variables["X"], variables["Y"]
    r1, r0, s1, s0 = variables["R1"], variables["R0"], variables["S1"], variables["S0"]
    lam = variables["lambda"]
    a2 = base.dense_mul(field, a, a)
    qp = base.dense_add(field, e, base.dense_scale(field, a2, -6))
    qc = base.dense_add(
        field,
        base.dense_scale(field, base.dense_mul(field, a, base.dense_add(field, base.dense_scale(field, a2, 4), base.dense_scale(field, e, -1))), 2),
        x, r1,
    )
    qr = base.dense_add(
        field,
        base.dense_mul(field, a2, base.dense_add(field, e, base.dense_scale(field, a2, -3))),
        r0,
        base.dense_scale(field, base.dense_mul(field, a, base.dense_add(field, x, r1)), -1),
    )
    n3 = base.dense_mul(field, lam, m)
    n2 = base.dense_mul(field, lam, base.dense_mul(field, a, m))
    n1 = base.dense_mul(field, lam, base.dense_add(field, base.dense_mul(field, base.dense_add(field, e, base.dense_scale(field, a2, -5)), m), y, s1))
    n0 = base.dense_mul(
        field, lam,
        base.dense_add(
            field,
            base.dense_scale(field, base.dense_mul(field, base.dense_mul(field, a, base.dense_add(field, e, base.dense_scale(field, a2, -3))), m), -1),
            base.dense_scale(field, base.dense_mul(field, a, y), -1),
            base.dense_scale(field, base.dense_mul(field, m, x), Fraction(1, 2)),
            s0,
            base.dense_scale(field, base.dense_mul(field, a, s1), -1),
        ),
    )
    factors = (
        base.dense_add(field, base.dense_mul(field, qr, qr), n0),
        base.dense_add(field, base.dense_scale(field, base.dense_mul(field, qc, qr), 2), n1),
        base.dense_add(field, base.dense_mul(field, qc, qc), base.dense_scale(field, base.dense_mul(field, qp, qr), 2), n2),
        base.dense_add(field, base.dense_scale(field, base.dense_mul(field, qp, qc), 2), n3),
        base.dense_add(field, base.dense_mul(field, qp, qp), base.dense_scale(field, qr, 2)),
        base.dense_scale(field, qc, 2), base.dense_scale(field, qp, 2),
        variables["K10"], variables["K6"], variables["K2"],
    )
    power_cache = {}
    term_cache = {}

    def factor_power(index, exponent):
        key = (index, exponent)
        if key not in power_cache:
            power_cache[key] = base.dense_pow(field, factors[index], exponent)
        return power_cache[key]

    def tail_term(exponents):
        if exponents not in term_cache:
            term = base.dense_const(field, 1)
            for index, exponent in enumerate(exponents):
                if exponent:
                    term = base.dense_mul(field, term, factor_power(index, exponent))
            term_cache[exponents] = term
        return term_cache[exponents]

    rows = {}
    for number in range(1, 8):
        result = {}
        entries = tails[str(number)]
        for offset, (raw_exponents, coefficient) in enumerate(entries, 1):
            exponents = tuple(int(value) for value in raw_exponents)
            result = base.dense_add(field, result, base.dense_scale(field, tail_term(exponents), coefficient))
            if offset % 40 == 0 or offset == len(entries):
                print(f"H17Q7_ABSTRACT_ROW={number}:{offset}/{len(entries)}:support={len(result)}", flush=True)
        rows[number] = result
    return rows


def source_series(base, field):
    def named(start, names):
        return base.series_from_terms(field, ((start + i, base.jet_var(field, name)) for i, name in enumerate(names)))

    a = named(3, (f"a{i}" for i in range(3, 10)))
    e = base.series_from_terms(field, [(0, base.jet_var(field, "p")), *((i, base.jet_var(field, f"e{i}")) for i in range(1, 7))])
    m = base.series_from_terms(field, [(0, base.jet_var(field, "m")), *((i, base.jet_var(field, f"m{i}")) for i in range(1, 7))])
    x = named(7, ("x",)); y = named(7, ("y",))
    r1 = named(14, ("r1",)); r0 = named(14, ("r0",))
    s1 = named(14, ("s1",)); s0 = named(14, ("s0",))
    kk = named(0, (f"kk{i}" for i in range(7)))
    e2 = base.series_mul(field, e, e)
    e4 = base.series_mul(field, e2, e2)
    e6 = base.series_mul(field, e4, e2)
    d6 = named(6, ("d6",)); d2 = named(6, ("d2",)); dm = named(6, ("dm",))
    k10 = base.series_from_terms(field, ((42 + grade, poly) for grade, poly in enumerate(kk) if poly))
    k6_inner = base.series_add(field, base.series_scale(field, base.series_mul(field, kk, e2), Fraction(15, 32)), d6)
    k2_inner = base.series_add(field, base.series_scale(field, base.series_mul(field, kk, e4), Fraction(15, 256)), d2)
    mu2_inner = base.series_add(field, base.series_scale(field, base.series_mul(field, kk, e6), Fraction(-5, 4096)), dm)
    k6 = base.series_from_terms(field, ((42 + grade, poly) for grade, poly in enumerate(k6_inner) if poly))
    k2 = base.series_from_terms(field, ((42 + grade, poly) for grade, poly in enumerate(k2_inner) if poly))
    mu2 = base.series_from_terms(field, ((42 + grade, poly) for grade, poly in enumerate(mu2_inner) if poly))
    mu4 = named(48, ("d4",))
    lam = base.series_from_terms(field, ((17, base.jet_const(field, 1)),))
    abstract = {
        "J": base.zero_series(), "K2": k2, "K6": k6, "K10": k10,
        "S0": s0, "S1": s1, "R0": r0, "R1": r1,
        "Y": y, "X": x, "a": a, "lambda": lam, "M": m, "E": e,
    }
    return abstract, mu2, mu4


def expand_row(base, field, poly, source):
    one = base.series_from_terms(field, ((0, base.jet_const(field, 1)),))
    power_cache = {}

    def power(name, exponent):
        key = (name, exponent)
        if key not in power_cache:
            result = one
            factor = source[name]
            remaining = exponent
            while remaining:
                if remaining & 1:
                    result = base.series_mul(field, result, factor)
                remaining //= 2
                if remaining:
                    factor = base.series_mul(field, factor, factor)
            power_cache[key] = result
        return power_cache[key]

    result = base.zero_series()
    survivors = 0
    for monomial, coefficient in poly.items():
        if sum(exponent * valuation for exponent, valuation in zip(monomial, ABS_VALUATIONS)) > MAX_GRADE:
            continue
        survivors += 1
        term = one
        for name, exponent in zip(base.ABS_VARS, monomial):
            if exponent:
                term = base.series_mul(field, term, power(name, exponent))
        result = base.series_add(field, result, base.series_scale(field, term, coefficient))
    return result, survivors


def expected_rows(base, field):
    v = lambda name: base.jet_var(field, name)
    mul = lambda *items: _mul_many(base, field, items)
    add = lambda *items: base.jet_add(field, *items)
    scale = lambda item, q: base.jet_scale(field, item, q)
    p, m, x, y = v("p"), v("m"), v("x"), v("y")
    r0, r1, s0 = v("r0"), v("r1"), v("s0")
    d6, d2, dm, d4 = v("d6"), v("d2"), v("dm"), v("d4")
    return {
        1: add(scale(mul(r1, m, m), Fraction(-3, 8)), scale(mul(s0, m), Fraction(3, 4))),
        2: add(scale(mul(d6, p, p, p, p), Fraction(3, 128)), scale(mul(r0, m, m), Fraction(-3, 8)), scale(mul(d2, p, p), Fraction(-1, 8)), scale(mul(y, y), Fraction(3, 8)), scale(dm, -1)),
        3: add(scale(mul(r1, m, m, p), Fraction(-3, 32)), scale(mul(x, y, m), Fraction(-3, 8)), scale(mul(s0, m, p), Fraction(3, 16))),
        4: add(scale(mul(x, x, m, m), Fraction(3, 32)), scale(mul(r0, m, m, p), Fraction(-3, 16)), scale(mul(y, y, p), Fraction(-3, 16)), scale(d4, -1)),
        5: add(scale(mul(r1, m, m, p, p), Fraction(-3, 256)), scale(mul(x, y, m, p), Fraction(3, 32)), scale(mul(s0, m, p, p), Fraction(3, 128))),
        6: add(scale(mul(d6, p, p, p, p, p, p), Fraction(-1, 512)), scale(mul(r0, m, m, p, p), Fraction(-3, 64)), scale(mul(d2, p, p, p, p), Fraction(1, 128)), scale(mul(y, y, p, p), Fraction(3, 64))),
        7: add(scale(mul(r1, m, m, p, p, p), Fraction(3, 1024)), scale(mul(x, y, m, p, p), Fraction(-3, 256)), scale(mul(s0, m, p, p, p), Fraction(-3, 512))),
    }


def _mul_many(base, field, items):
    result = base.jet_const(field, 1)
    for item in items:
        result = base.jet_mul(field, result, item)
    return result


def evaluate_rows(base, field, rows, values):
    return {number: base.jet_eval(field, poly, values) for number, poly in rows.items()}


def canonical_rows(base, field, rows):
    return {
        str(number): {
            "variables": list(JET_VARS),
            "terms": [
                {"monomial": [[JET_VARS[index], exponent] for index, exponent in monomial], "coefficient": field.text(coefficient)}
                for monomial, coefficient in sorted(poly.items())
            ],
        }
        for number, poly in rows.items()
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    tag = require_aws()
    base = load_base()
    field = base.Field(args.characteristic)
    if digest(base.TAILS) != TAILS_SHA:
        fail("frozen tails mismatch")
    tails = json.loads(base.TAILS.read_text())
    canonical_tails = json.dumps(tails, sort_keys=True, separators=(",", ":"))
    if sha256(canonical_tails.encode()).hexdigest() != CANONICAL_SHA:
        fail("canonical tails mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    abstract_rows = build_abstract_rows(base, field, tails)
    source, mu2, mu4 = source_series(base, field)
    expanded = {}
    survivor_counts = {}
    for number in range(1, 8):
        expanded[number], survivor_counts[number] = expand_row(base, field, abstract_rows[number], source)
    expanded[2] = base.series_add(field, expanded[2], base.series_scale(field, mu2, -1))
    expanded[4] = base.series_add(field, expanded[4], base.series_scale(field, mu4, -1))
    for number in range(1, 8):
        for grade in range(48):
            if expanded[number][grade]:
                fail(("nonzero predecessor below grade48", number, grade, expanded[number][grade]))
    rows = {number: expanded[number][48] for number in range(1, 8)}
    expected = expected_rows(base, field)
    for number in range(1, 8):
        if rows[number] != expected[number]:
            fail(("grade48 formula mismatch", number, rows[number], expected[number]))
    p = base.jet_var(field, "p")
    relation5 = base.jet_add(field, base.jet_scale(field, base.jet_mul(field, base.jet_mul(field, p, p), rows[1]), Fraction(3, 32)), base.jet_scale(field, base.jet_mul(field, p, rows[3]), Fraction(-1, 4)))
    relation7 = base.jet_add(field, base.jet_scale(field, base.jet_mul(field, base.jet_mul(field, p, p), rows[3]), Fraction(1, 32)), base.jet_scale(field, base.jet_mul(field, base.jet_mul(field, base.jet_mul(field, p, p), p), rows[1]), Fraction(-1, 64)))
    if relation5 != rows[5] or relation7 != rows[7]:
        fail("odd-row redundancy mismatch")
    zero = field.value(0)
    witness_x = {name: 0 for name in JET_VARS}
    witness_x.update({"p": 1, "m": 1, "x": 1, "d4": Fraction(3, 32)})
    witness_y = {name: 0 for name in JET_VARS}
    witness_y.update({"p": 1, "m": 1, "y": 1, "d2": -6, "dm": Fraction(9, 8), "d4": Fraction(-3, 16)})
    if any(value != zero for value in evaluate_rows(base, field, rows, witness_x).values()):
        fail("D(x) witness failed")
    if any(value != zero for value in evaluate_rows(base, field, rows, witness_y).values()):
        fail("D(y) witness failed")
    negative = dict(witness_x); negative["d4"] = field.value(Fraction(1, 8))
    negative_values = evaluate_rows(base, field, rows, negative)
    if negative_values[4] == zero:
        fail("omission negative control failed")
    payload = canonical_rows(base, field, rows)
    payload_bytes = (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()
    (output / "grade48_rows.json").write_bytes(payload_bytes)
    result = {
        "status": "PASS-A-H17-Q7-A3-G48-SPARSE-V2",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "base_sha256": digest(BASE),
        "tails_sha256": digest(base.TAILS),
        "row_supports": {str(number): len(rows[number]) for number in range(1, 8)},
        "abstract_survivors": {str(number): survivor_counts[number] for number in range(1, 8)},
        "grade48_rows_sha256": sha256(payload_bytes).hexdigest(),
        "lower_zero_rows": 7,
        "odd_redundancies": 2,
        "projective_zero_witnesses": 2,
        "negative_control_row4": field.text(negative_values[4]),
        "elapsed_seconds": time.monotonic() - started,
        "scope": "FIXED_H17_Q7_A3_NORMALIZED_GRAPH_GRADE48_PREDECESSOR_ONLY_NO_RATIONAL_REGRADING_SOURCE_REES_ORDER2_MAX12_OR_JC2_VERDICT",
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("A_H17Q7S_ROWS_SHA256=" + result["grade48_rows_sha256"])
    print("A_H17Q7S_LOWER_ZERO=1")
    print("A_H17Q7S_FORMULAS=1")
    print("A_H17Q7S_REDUNDANCIES=1")
    print("A_H17Q7S_WITNESS_X=1")
    print("A_H17Q7S_WITNESS_Y=1")
    print("A_H17Q7S_NEGATIVE_CONTROL=1")
    print("A_H17Q7S_ENDPOINT=PASS_COMPLETE_GRADE48_PREDECESSOR")
    print("A_H17Q7S_DONE=1")
    print("A_H17Q7S_SCOPE=" + result["scope"])


if __name__ == "__main__":
    main()
