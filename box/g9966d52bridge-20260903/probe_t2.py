#!/usr/bin/env python3
"""Exact T2 bridge-row probe in the charged delta=5/2 stage-7 chart.

This is deliberately separate from the stage-8 continuation and from the
T2/T3 jet prototype.  It reconstructs the charged stage-7 coordinate maps,
forms the fully normalized T2 expression, and extracts every pi-coefficient
through normalized s-degree 391.
"""

from __future__ import annotations

from collections import defaultdict
import hashlib
import importlib.util
import json
import os
import argparse
from pathlib import Path
import resource
import sys
import time

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
FROZEN = Path("/tmp/jc2-lane.IAeCOg/inputs")
ENGINE = FROZEN / "band_engine.py"
STAGE7 = FROZEN / "stage7.json"
FREE_LIST = FROZEN / "stage7-free-coefficients.txt"
OUTPUT = Path(__file__).with_suffix(".json")
TARGET_S = 391
PRIMES = (32003, 104729, 1299709)


Series = dict[int, dict[int, sp.Expr]]


def stamp(started: float, message: str) -> None:
    print(f"{time.perf_counter() - started:9.3f}s  {message}", flush=True)


def load_engine():
    spec = importlib.util.spec_from_file_location("charged_band_engine_t2", ENGINE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {ENGINE}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def nested(flat: dict[tuple[int, int], sp.Expr], cap: int = TARGET_S) -> Series:
    out: dict[int, dict[int, sp.Expr]] = defaultdict(dict)
    for (n, k), value in flat.items():
        if n <= cap and value != 0:
            out[n][k] = value
    return dict(out)


def add(*items: Series) -> Series:
    out: dict[int, dict[int, sp.Expr]] = defaultdict(dict)
    for item in items:
        for n, band in item.items():
            bucket = out[n]
            for k, value in band.items():
                bucket[k] = bucket.get(k, sp.Integer(0)) + value
    clean: Series = {}
    for n, band in out.items():
        reduced = {k: sp.expand(value) for k, value in band.items()}
        reduced = {k: value for k, value in reduced.items() if value != 0}
        if reduced:
            clean[n] = reduced
    return clean


def scale(item: Series, scalar: sp.Expr | int) -> Series:
    if scalar == 0:
        return {}
    return {
        n: {k: sp.expand(scalar * value) for k, value in band.items()}
        for n, band in item.items()
    }


def shift(item: Series, amount: int) -> Series:
    return {
        n + amount: dict(band)
        for n, band in item.items()
        if n + amount <= TARGET_S
    }


def multiply(left: Series, right: Series, label: str, started: float) -> Series:
    """Exact truncated convolution in (s-degree, pi-degree)."""
    accum: dict[int, dict[int, sp.Expr]] = defaultdict(dict)
    products = 0
    right_degrees = sorted(right)
    for n1 in sorted(left):
        band1 = left[n1]
        for n2 in right_degrees:
            n = n1 + n2
            if n > TARGET_S:
                break
            band2 = right[n2]
            bucket = accum[n]
            for k1, value1 in band1.items():
                for k2, value2 in band2.items():
                    k = k1 + k2
                    bucket[k] = bucket.get(k, sp.Integer(0)) + value1 * value2
                    products += 1
    out: Series = {}
    for n in sorted(accum):
        band = {k: sp.expand(value) for k, value in accum[n].items()}
        band = {k: value for k, value in band.items() if value != 0}
        if band:
            out[n] = band
    stamp(started, f"multiply {label}: scalar-products={products}, slots={slot_count(out)}")
    return out


def slot_count(item: Series) -> int:
    return sum(len(band) for band in item.values())


def series_summary(item: Series) -> dict:
    degrees = sorted(item)
    return {
        "s_degree_min": degrees[0] if degrees else None,
        "s_degree_max": degrees[-1] if degrees else None,
        "s_band_count": len(degrees),
        "pi_slot_count": slot_count(item),
        "pi_degree_max": max((max(band) for band in item.values()), default=None),
    }


def rational_affine_candidates(row: sp.Expr, eligible: set[sp.Symbol]) -> dict[sp.Symbol, sp.Rational]:
    """Find variables whose entire occurrence is a nonzero QQ* multiple of x."""
    linear: dict[sp.Symbol, sp.Expr] = defaultdict(lambda: sp.Integer(0))
    blocked: set[sp.Symbol] = set()
    for term in sp.Add.make_args(row):
        symbols = term.free_symbols.intersection(eligible)
        if len(symbols) == 1:
            variable = next(iter(symbols))
            coefficient = sp.expand(term / variable)
            if variable not in coefficient.free_symbols and coefficient.is_Rational:
                linear[variable] += coefficient
                continue
        blocked.update(symbols)
    out = {}
    for variable, coefficient in linear.items():
        coefficient = sp.Rational(coefficient)
        if variable not in blocked and coefficient != 0:
            out[variable] = coefficient
    return out


def row_digest(rows: list[tuple[tuple[int, int], sp.Expr]]) -> str:
    digest = hashlib.sha256()
    for (n, k), row in rows:
        digest.update(f"{n}\t{k}\t{sp.srepr(row)}\n".encode())
    return digest.hexdigest()


def modular_evaluator(values: dict[sp.Symbol, int], prime: int):
    cache: dict[sp.Expr, int] = {}

    def evaluate(expression: sp.Expr) -> int:
        if expression in cache:
            return cache[expression]
        if expression.is_Integer:
            result = int(expression) % prime
        elif expression.is_Rational:
            result = int(expression.p) * pow(int(expression.q) % prime, -1, prime) % prime
        elif expression.is_Symbol:
            result = values[expression] % prime
        elif expression.is_Add:
            result = sum(evaluate(arg) for arg in expression.args) % prime
        elif expression.is_Mul:
            result = 1
            for arg in expression.args:
                result = result * evaluate(arg) % prime
        elif expression.is_Pow:
            base, exponent = expression.args
            assert exponent.is_Integer and int(exponent) >= 0
            result = pow(evaluate(base), int(exponent), prime)
        else:
            raise TypeError(expression.func)
        cache[expression] = result
        return result

    return evaluate


def numeric_z_tables(max_q: int, cap: int, u: int, v: int, prime: int):
    tables = [{(0, 0): 1}]
    for _ in range(max_q):
        out = defaultdict(int)
        for (delta, k), value in tables[-1].items():
            out[(delta, k)] = (out[(delta, k)] - value) % prime
            if delta + 4 <= cap:
                out[(delta + 4, k)] = (out[(delta + 4, k)] + value * u) % prime
            if delta + 6 <= cap:
                out[(delta + 6, k)] = (out[(delta + 6, k)] + value * v) % prime
            if delta + 7 <= cap:
                out[(delta + 7, k + 1)] = (out[(delta + 7, k + 1)] + value) % prime
        tables.append({key: value for key, value in out.items() if value})
    return tables


def support_z_tables(max_q: int, cap: int):
    tables = [{(0, 0)}]
    for _ in range(max_q):
        out = set()
        for delta, k in tables[-1]:
            out.add((delta, k))
            if delta + 4 <= cap:
                out.add((delta + 4, k))
            if delta + 6 <= cap:
                out.add((delta + 6, k))
            if delta + 7 <= cap:
                out.add((delta + 7, k + 1))
        tables.append(out)
    return tables


def local_numeric(item, tables, evaluate, prime: int):
    out = defaultdict(int)
    for (r, q), expression in item.items():
        coefficient = evaluate(expression)
        if not coefficient:
            continue
        for (delta, k), scalar in tables[q].items():
            n = 2 * r + delta
            if n <= TARGET_S:
                out[(n, k)] = (out[(n, k)] + coefficient * scalar) % prime
    return {key: value for key, value in out.items() if value}


def local_support(item, tables):
    return {
        (2 * r + delta, k)
        for (r, q), expression in item.items()
        if expression != 0
        for delta, k in tables[q]
        if 2 * r + delta <= TARGET_S
    }


def nadd(*items, prime: int):
    out = defaultdict(int)
    for item in items:
        for key, value in item.items():
            out[key] = (out[key] + value) % prime
    return {key: value for key, value in out.items() if value}


def nscale(item, scalar: int, prime: int):
    scalar %= prime
    return {key: value * scalar % prime for key, value in item.items() if value * scalar % prime}


def nshift(item, amount: int):
    return {(n + amount, k): value for (n, k), value in item.items() if n + amount <= TARGET_S}


def nmul(left, right, prime: int):
    out = defaultdict(int)
    for (n1, k1), a in left.items():
        for (n2, k2), b in right.items():
            if n1 + n2 <= TARGET_S:
                key = (n1 + n2, k1 + k2)
                out[key] = (out[key] + a * b) % prime
    return {key: value for key, value in out.items() if value}


def sadd(*items):
    return set().union(*items)


def smul(left, right):
    return {
        (n1 + n2, k1 + k2)
        for n1, k1 in left
        for n2, k2 in right
        if n1 + n2 <= TARGET_S
    }


def sshift(item, amount):
    return {(n + amount, k) for n, k in item if n + amount <= TARGET_S}


def assemble_numeric(component, tvalues, prime: int):
    H, A2, A3, B1, B2 = (component[name] for name in ("H", "A2", "A3", "B1", "B2"))
    H2 = nmul(H, H, prime)
    H3 = nmul(H2, H, prime)
    H4 = nmul(H2, H2, prime)
    EA = nadd(nmul(A2, H, prime), A3, prime=prime)
    EB = nadd(nmul(B1, H, prime), B2, prime=prime)
    EA2 = nmul(EA, EA, prime)
    EB2 = nmul(EB, EB, prime)
    EB3 = nmul(EB2, EB, prime)
    base = nadd(
        nscale(nmul(H4, EB, prime), 3, prime),
        nscale(nmul(H3, EA, prime), -2, prime),
        nscale(nmul(H2, EB2, prime), 3, prime),
        EB3,
        nscale(EA2, -1, prime),
        prime=prime,
    )
    F = nadd(H3, EA, prime=prime)
    G = nadd(H2, EB, prime=prime)
    FG = nmul(F, G, prime)
    result = nadd(
        base,
        nscale(nshift(FG, 66), tvalues["T2_a1"], prime),
        nscale(nshift(G, 264), tvalues["T2_a0"], prime),
        nscale(nshift(F, 198), tvalues["T2_b1"], prime),
        prime=prime,
    )
    return result, F, G


def assemble_support(component):
    H, A2, A3, B1, B2 = (component[name] for name in ("H", "A2", "A3", "B1", "B2"))
    H2 = smul(H, H)
    H3 = smul(H2, H)
    H4 = smul(H2, H2)
    EA = sadd(smul(A2, H), A3)
    EB = sadd(smul(B1, H), B2)
    EA2 = smul(EA, EA)
    EB2 = smul(EB, EB)
    EB3 = smul(EB2, EB)
    F = sadd(H3, EA)
    G = sadd(H2, EB)
    return sadd(
        smul(H4, EB), smul(H3, EA), smul(H2, EB2), EB3, EA2,
        sshift(smul(F, G), 66), sshift(G, 264), sshift(F, 198),
    )


def expected_p5(cvalue: int, prime: int):
    poly = {0: 1}
    base = {3: 1, 1: -cvalue % prime}
    for _ in range(5):
        out = defaultdict(int)
        for k1, a in poly.items():
            for k2, b in base.items():
                out[k1 + k2] = (out[k1 + k2] + a * b) % prime
        poly = {k: value for k, value in out.items() if value}
    return poly


def deterministic_values(symbols: set[sp.Symbol], prime: int, sample: int):
    out = {}
    for variable in symbols:
        payload = f"probe-t2:{prime}:{sample}:{variable}".encode()
        out[variable] = 1 + int.from_bytes(hashlib.sha256(payload).digest()[:8], "big") % (prime - 1)
    out[sp.Symbol("c")] = 2 + sample
    out[sp.Symbol("u")] = 5 + sample
    out[sp.Symbol("v")] = 11 + sample
    return out


def bounded_main() -> None:
    started = time.perf_counter()
    engine = load_engine()
    stage7 = json.loads(STAGE7.read_text(encoding="utf-8"))
    free_names = FREE_LIST.read_text(encoding="utf-8").splitlines()
    k2, inner_free, _ = engine.build_major_h2("delta52", 33)
    outer, outer_free, _ = engine.outer_state(7)
    joint = {engine.symbol(entry["variable"]): 0 for entry in stage7["joint_elimination"]["pivot_ledger"]}
    outer = {
        block: {position: sp.expand(value.xreplace(joint)) for position, value in values.items()}
        for block, values in outer.items()
    }
    free_symbols = set(map(engine.symbol, free_names))
    assert (set(inner_free) | (set(outer_free) - set(joint))) == free_symbols
    items = {"H": k2}
    for block in ("A2", "A3", "B1", "B2"):
        items[block] = engine.outer_effective_tz(outer, block, 99)
    max_q = max(q for item in items.values() for _r, q in item)
    structural_tables = support_z_tables(max_q, TARGET_S)
    structural_components = {name: local_support(item, structural_tables) for name, item in items.items()}
    structural = assemble_support(structural_components)
    structural |= {(TARGET_S, k) for k in (5, 7, 9, 11, 13, 15)}
    stamp(started, f"structural upper support assembled: {len(structural)} slots")

    observed = []
    run_meta = []
    for sample, prime in enumerate(PRIMES):
        values = deterministic_values(free_symbols, prime, sample)
        evaluate = modular_evaluator(values, prime)
        tables = numeric_z_tables(max_q, TARGET_S, values[sp.Symbol("u")], values[sp.Symbol("v")], prime)
        components = {name: local_numeric(item, tables, evaluate, prime) for name, item in items.items()}
        tvalues = {
            name: 1 + int.from_bytes(hashlib.sha256(f"{prime}:{name}".encode()).digest()[:8], "big") % (prime - 1)
            for name in ("T2_a1", "T2_a0", "T2_b1", "T2_b0")
        }
        kt2, F, G = assemble_numeric(components, tvalues, prime)
        p5 = expected_p5(values[sp.Symbol("c")], prime)
        for k, value in p5.items():
            key = (TARGET_S, k)
            kt2[key] = (kt2.get(key, 0) - value) % prime
            if kt2[key] == 0:
                kt2.pop(key)
        support = set(kt2)
        observed.append(support)
        run_meta.append({
            "prime": prime,
            "row_slots": len(support),
            "KT2_min_s": min((n for n, _k in support), default=None),
            "KT2_max_pi": max((k for _n, k in support), default=None),
            "F_slots": len(F),
            "G_slots": len(G),
            "component_slots": {name: len(value) for name, value in components.items()},
        })
        stamp(started, f"modular KT2 sample p={prime}: rows={len(support)}")
    certified_nonzero = set().union(*observed)
    common_observed = set.intersection(*observed)
    assert certified_nonzero <= structural
    exact_support = certified_nonzero == structural
    by_s = defaultdict(int)
    for n, _k in sorted(certified_nonzero):
        by_s[n] += 1
    result = {
        "type": "CONSERVATIVE-EXACT-SUPPORT / FULL-STAGE7-KT2",
        "normalization": {
            "KT2": "t^198*T2; t=s^2",
            "target_s_degree": TARGET_S,
            "target": "(pi*(pi^2-c))^5",
            "Tschirnhausen": "c0=0",
            "adjoined": ["T2_a1", "T2_a0", "T2_b1", "T2_b0"],
            "T2_b0_occurs_through_target": False,
        },
        "stage7": {"free": 869, "joint_pivots_zero": 59},
        "support": {
            "structural_upper_slots": len(structural),
            "modular_certified_nonzero_slots": len(certified_nonzero),
            "three_sample_common_slots": len(common_observed),
            "upper_equals_certified": exact_support,
            "certified_s_min": min((n for n, _k in certified_nonzero), default=None),
            "certified_s_max": max((n for n, _k in certified_nonzero), default=None),
            "certified_pi_max": max((k for _n, k in certified_nonzero), default=None),
            "occupied_s_bands": len(by_s),
            "by_s": {str(n): by_s[n] for n in sorted(by_s)},
        },
        "modular_runs": run_meta,
        "Qstar_feasibility": {
            "full_exact_affine_scan": False,
            "reason": "Expanded unspecialized A2 localization alone took 756.137s; full symbolic rows exceeded the bounded-probe cost envelope.",
            "safe_conclusion": "Support generation is feasible; Q*-pivot count is not certified by modular value samples. Do not reuse the old 167-dimensional linearized rank.",
        },
        "aborted_symbolic_benchmark": {
            "K2": {"seconds": 133.450, "slots": 1657, "s_min": 8, "s_max": 231},
            "A2": {"seconds": 756.137, "slots": 2013, "s_min": 44, "s_max": 292},
            "note": "The first exact-symbolic run was terminated before A3 completed; no process was left running.",
        },
        "resources": {"wall_seconds": round(time.perf_counter() - started, 3), "max_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"support": result["support"], "modular_runs": run_meta, "resources": result["resources"]}, indent=2, sort_keys=True))


def symbolic_main() -> None:
    # Numerical libraries are not needed here; record/enforce the one-core run.
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
    os.environ.setdefault("MKL_NUM_THREADS", "1")
    started = time.perf_counter()
    engine = load_engine()
    stage7 = json.loads(STAGE7.read_text(encoding="utf-8"))
    free_names = FREE_LIST.read_text(encoding="utf-8").splitlines()
    assert stage7["branch"] == "delta52"
    assert stage7["counts"]["exact_Krull_dimension_localized"] == 869
    assert stage7["unresolved_quotient_generators"] == free_names
    stamp(started, "charged stage-7 metadata loaded")

    k2, inner_free, _major = engine.build_major_h2("delta52", 33)
    stamp(started, f"K2 map built: terms={len(k2)}, inner-free={len(inner_free)}")
    outer, outer_free, _outer_meta = engine.outer_state(7)
    stamp(started, f"outer D1 map built: free={len(outer_free)}")

    joint_pivots = {
        engine.symbol(entry["variable"])
        for entry in stage7["joint_elimination"]["pivot_ledger"]
    }
    assert len(joint_pivots) == 59
    assert all(str(variable).startswith("B1c_") for variable in joint_pivots)
    zero_joint = {variable: sp.Integer(0) for variable in joint_pivots}
    for position, value in list(outer["B1"].items()):
        image = sp.expand(value.xreplace(zero_joint))
        outer["B1"][position] = image

    expected_free = set(map(engine.symbol, free_names))
    reconstructed_free = set(inner_free) | (set(outer_free) - joint_pivots)
    assert reconstructed_free == expected_free
    stamp(started, "869-generator endpoint map verified")

    components = {"H": k2}
    for block in ("A2", "A3", "B1", "B2"):
        components[block] = engine.outer_effective_tz(outer, block, 99)

    local: dict[str, Series] = {}
    for name, item in components.items():
        before = time.perf_counter()
        flat = engine.local_rows(item, "delta52", TARGET_S, exact_only=False)
        local[name] = nested(flat)
        stamp(
            started,
            f"local {name}: {series_summary(local[name])}; step={time.perf_counter()-before:.3f}s",
        )

    H = local["H"]
    H2 = multiply(H, H, "H2", started)
    H3 = multiply(H2, H, "H3", started)
    H4 = multiply(H2, H2, "H4", started)
    EA = add(multiply(local["A2"], H, "A2H", started), local["A3"])
    EB = add(multiply(local["B1"], H, "B1H", started), local["B2"])
    EA2 = multiply(EA, EA, "EA2", started)
    EB2 = multiply(EB, EB, "EB2", started)
    EB3 = multiply(EB2, EB, "EB3", started)

    # G^3-F^2 after cancelling the common H^6 exactly at the tower level.
    base = add(
        scale(multiply(H4, EB, "H4EB", started), 3),
        scale(multiply(H3, EA, "H3EA", started), -2),
        scale(multiply(H2, EB2, "H2EB2", started), 3),
        EB3,
        scale(EA2, -1),
    )
    F = add(H3, EA)
    G = add(H2, EB)

    T2_a1, T2_a0, T2_b1, T2_b0 = sp.symbols(
        "T2_a1 T2_a0 T2_b1 T2_b0"
    )
    FG = multiply(F, G, "FG", started)
    kt2 = add(
        base,
        scale(shift(FG, 66), T2_a1),
        scale(shift(G, 264), T2_a0),
        scale(shift(F, 198), T2_b1),
        # t^198*b0 is s^396 and therefore correctly absent through s^391.
    )
    stamp(started, f"KT2 assembled: {series_summary(kt2)}")

    pi = sp.Symbol("pi")
    c = sp.Symbol("c")
    p5 = sp.Poly(sp.expand((pi * (pi**2 - c)) ** 5), pi)
    target_coefficients = {
        monomial[0]: coefficient for monomial, coefficient in p5.terms()
    }

    rows: list[tuple[tuple[int, int], sp.Expr]] = []
    for n in sorted(degree for degree in kt2 if degree < TARGET_S):
        for k in sorted(kt2[n]):
            row = sp.expand(kt2[n][k])
            if row != 0:
                rows.append(((n, k), row))
    target_band = kt2.get(TARGET_S, {})
    for k in sorted(set(target_band) | set(target_coefficients)):
        row = sp.expand(target_band.get(k, 0) - target_coefficients.get(k, 0))
        if row != 0:
            rows.append(((TARGET_S, k), row))
    stamp(started, f"rows materialized: {len(rows)}")

    all_symbols = set().union(*(row.free_symbols for _tag, row in rows)) if rows else set()
    allowed = expected_free | {T2_a1, T2_a0, T2_b1, T2_b0}
    unexpected = sorted(map(str, all_symbols - allowed))
    assert not unexpected, unexpected

    eligible = allowed - {c}
    candidate_rows = []
    candidate_variables: set[sp.Symbol] = set()
    scan_started = time.perf_counter()
    for tag, row in rows:
        candidates = rational_affine_candidates(row, eligible)
        if candidates:
            candidate_variables.update(candidates)
            if len(candidate_rows) < 40:
                candidate_rows.append(
                    {
                        "row": list(tag),
                        "candidates": {str(v): str(a) for v, a in sorted(candidates.items(), key=lambda x: str(x[0]))},
                    }
                )
    stamp(
        started,
        f"QQ* feasibility scan: rows-with-candidate={len(candidate_rows)}+ capped preview, "
        f"unique-vars={len(candidate_variables)}, step={time.perf_counter()-scan_started:.3f}s",
    )

    degrees = [tag[0] for tag, _row in rows]
    by_s = defaultdict(int)
    for (n, _k), _row in rows:
        by_s[n] += 1
    result = {
        "type": "EXACT-T2-STAGE7-SUPPORT-PROBE",
        "charged_stage7": {
            "dimension": 869,
            "generator_count": len(free_names),
            "generator_list_sha256": hashlib.sha256(FREE_LIST.read_bytes()).hexdigest(),
            "joint_Qstar_pivots": len(joint_pivots),
            "joint_resolved_map": "all 59 B1c pivots map to zero",
        },
        "normalization": {
            "KF": "t^99 F",
            "KG": "t^66 G",
            "t": "s^2",
            "KT2": "t^198 T2",
            "target_physical_order": "s^-5 = t^-5/2",
            "target_normalized_s_degree": TARGET_S,
            "target_polynomial": "(pi*(pi^2-c))^5",
            "T2_coefficients": ["T2_a1", "T2_a0", "T2_b1", "T2_b0"],
            "Tschirnhausen": "c0=0",
            "b0_support_note": "t^198*b0 starts at normalized s-degree 396; absent through 391",
        },
        "component_support": {name: series_summary(value) for name, value in local.items()},
        "F_support": series_summary(F),
        "G_support": series_summary(G),
        "KT2_support": series_summary(kt2),
        "rows": {
            "nonzero_coefficient_rows": len(rows),
            "s_degree_min": min(degrees) if degrees else None,
            "s_degree_max": max(degrees) if degrees else None,
            "pi_degree_max": max((tag[1] for tag, _row in rows), default=None),
            "occupied_s_bands": len(by_s),
            "by_s_degree": {str(n): by_s[n] for n in sorted(by_s)},
            "sha256": row_digest(rows),
        },
        "Qstar_feasibility": {
            "rule": "initial exact scan only; variable must occur solely as a nonzero rational multiple",
            "unique_candidate_variables": len(candidate_variables),
            "candidate_variable_names": sorted(map(str, candidate_variables)),
            "preview": candidate_rows,
            "full_greedy_elimination_run": False,
            "interpretation": "A zero count proves no first QQ* pivot. A positive count is only an initial-pivot lower bound; substitutions were not performed.",
        },
        "resources": {
            "wall_seconds": round(time.perf_counter() - started, 3),
            "max_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            "threads": 1,
        },
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    stamp(started, f"wrote {OUTPUT}")
    print(json.dumps({
        "component_support": result["component_support"],
        "F_support": result["F_support"],
        "G_support": result["G_support"],
        "KT2_support": result["KT2_support"],
        "rows": {k: v for k, v in result["rows"].items() if k != "by_s_degree"},
        "Qstar_feasibility": {k: v for k, v in result["Qstar_feasibility"].items() if k != "preview"},
        "resources": result["resources"],
    }, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbolic", action="store_true", help="run the unbounded exact-expression prototype")
    args = parser.parse_args()
    if args.symbolic:
        symbolic_main()
    else:
        bounded_main()


if __name__ == "__main__":
    main()
