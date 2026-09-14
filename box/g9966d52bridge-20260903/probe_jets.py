#!/usr/bin/env python3
"""Bounded stage-7 minor-jet probe for the delta=5/2 joint chart.

This is deliberately a probe, not a bridge-row generator.  It imports the
frozen ``band_engine.py`` and uses only its pure chart builders.  The final 59
joint pivots are reconstructed from the serialized stage-7 RHS ledger.  No
charged artifact is modified and the only output is a JSON record on stdout.

The symbolic work is kept linear: the five chart components K2, A2, A3, B1,
B2 are localized exactly.  Products are then assembled in a support/finite-
field algebra.  Three prime evaluations distinguish structural support from
generic observed support without expanding a 869-variable cubic globally.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import os
import resource
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
RECEIPT = ROOT / "xmodel/g9966-delta52-bridge-sol56-20260903.run.v2"
FROZEN = Path("/tmp/jc2-lane.IAeCOg/inputs")
BAND_ENGINE = FROZEN / "band_engine.py"
STAGE7 = FROZEN / "stage7.json"
FREE_LIST = FROZEN / "stage7-free-coefficients.txt"
F_WINDOW = (189, 233)
G_WINDOW = (126, 170)
PRIMES = (32003, 104729, 1299709)

# The launcher also sets these.  Keep library fan-out at one if the script is
# invoked directly; Python/SymPy itself is single-threaded here.
for _thread_var in (
    "OMP_NUM_THREADS",
    "OPENBLAS_NUM_THREADS",
    "MKL_NUM_THREADS",
    "NUMEXPR_NUM_THREADS",
):
    os.environ.setdefault(_thread_var, "1")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_lines(lines: Iterable[str]) -> str:
    return hashlib.sha256("".join(f"{line}\n" for line in lines).encode()).hexdigest()


def receipt_fields() -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value
    return fields


def verify_frozen(names: Iterable[str]) -> dict:
    fields = receipt_fields()
    count = int(fields["charged_inputs"])
    assert Path(fields["lane_inputs_dir"]) == FROZEN
    expected = {
        fields[f"charged_input_{index}_basename"]:
        fields[f"charged_input_{index}_sha256"]
        for index in range(1, count + 1)
    }
    checked = {}
    for name in names:
        actual = sha256(FROZEN / name)
        assert name in expected and actual == expected[name], f"frozen mismatch: {name}"
        checked[name] = actual
    return {
        "receipt": str(RECEIPT),
        "receipt_charged_input_count": count,
        "checked": checked,
        "all_checked_hashes_match": True,
    }


def load_engine():
    # dataclasses consults sys.modules while decorating Pivot, so register the
    # frozen module before executing it.
    module_name = "g9966_frozen_band_engine_probe_jets"
    spec = importlib.util.spec_from_file_location(module_name, BAND_ENGINE)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


@dataclass
class Clock:
    start: float
    last: float
    events: list[dict]

    @classmethod
    def begin(cls) -> "Clock":
        now = time.perf_counter()
        return cls(now, now, [])

    def stamp(self, label: str, **data) -> None:
        now = time.perf_counter()
        event = {
            "label": label,
            "step_seconds": round(now - self.last, 6),
            "elapsed_seconds": round(now - self.start, 6),
        }
        event.update(data)
        self.events.append(event)
        self.last = now
        print(
            f"[{event['elapsed_seconds']:9.3f}s] {label}",
            file=sys.stderr,
            flush=True,
        )


def parse_joint_map(engine, stage: dict, ambient: set[sp.Symbol]):
    ledger = stage["joint_elimination"]["pivot_ledger"]
    namespace = {str(variable): variable for variable in ambient}
    raw: dict[sp.Symbol, sp.Expr] = {}
    rows = []
    for item in ledger:
        variable = engine.symbol(item["variable"])
        assert variable in ambient and variable not in raw
        coefficient = sp.Rational(item["coefficient"])
        assert coefficient != 0
        rhs = sp.sympify(item["rhs"], locals=namespace)
        raw[variable] = sp.expand(rhs)
        rows.append(f"{item['row']}\t{variable}\t{coefficient}\t{sp.srepr(rhs)}")
    resolved = engine.resolve_map(raw)
    assert len(raw) == stage["joint_elimination"]["Qstar_pivots"] == 59
    assert all(not rhs.free_symbols.intersection(raw) for rhs in resolved.values())
    return raw, resolved, sha256_lines(rows)


def z_power_table(max_q: int, max_delta: int, u: sp.Symbol, v: sp.Symbol):
    """Return coefficients of (-1+u*s^4+v*s^6+pi*s^7)^q.

    ``pi`` is represented by the second key coordinate, so each table entry
    is ``(s_increment, pi_power) -> Q[u,v]``.
    """
    tables: list[dict[tuple[int, int], sp.Expr]] = [{(0, 0): sp.Integer(1)}]
    for _q in range(1, max_q + 1):
        previous = tables[-1]
        terms: dict[tuple[int, int], sp.Expr] = defaultdict(lambda: sp.Integer(0))
        for (delta, pi_power), coefficient in previous.items():
            terms[(delta, pi_power)] -= coefficient
            if delta + 4 <= max_delta:
                terms[(delta + 4, pi_power)] += coefficient * u
            if delta + 6 <= max_delta:
                terms[(delta + 6, pi_power)] += coefficient * v
            if delta + 7 <= max_delta:
                terms[(delta + 7, pi_power + 1)] += coefficient
        expanded = {}
        for key, value in terms.items():
            value = sp.expand(value)
            if value != 0:
                expanded[key] = value
        tables.append(expanded)
    return tables


Local = dict[tuple[int, int], sp.Expr]


def localize_tz(
    item: dict[tuple[int, int], sp.Expr],
    tables: list[dict[tuple[int, int], sp.Expr]],
    n_lo: int,
    n_hi: int,
) -> Local:
    """Exact delta=5/2 pullback of a t,z chart polynomial.

    The frozen engine uses t=s^2 and w=u*s^4+v*s^6+pi*s^7.  Its z=w-1
    conversion is therefore performed directly using ``z_power_table``.
    """
    buckets: dict[tuple[int, int], list[sp.Expr]] = defaultdict(list)
    for (t_power, z_power), coefficient in item.items():
        base = 2 * t_power
        if base > n_hi:
            continue
        for (delta, pi_power), scalar in tables[z_power].items():
            n = base + delta
            if n_lo <= n <= n_hi:
                buckets[(n, pi_power)].append(coefficient * scalar)
    result = {}
    for key, terms in buckets.items():
        value = sp.expand(sp.Add(*terms))
        if value != 0:
            result[key] = value
    return result


def group_local(series: dict[tuple[int, int], object]):
    grouped: dict[int, dict[int, object]] = defaultdict(dict)
    for (n, pi_power), value in series.items():
        grouped[n][pi_power] = value
    return dict(grouped)


def add_grouped(*series, modulus: int | None = None):
    out: dict[int, dict[int, object]] = defaultdict(dict)
    for source in series:
        for n, polynomial in source.items():
            for pi_power, coefficient in polynomial.items():
                prior = out[n].get(pi_power, 0)
                value = prior + coefficient
                if modulus is not None:
                    value %= modulus
                if value:
                    out[n][pi_power] = value
                elif pi_power in out[n]:
                    del out[n][pi_power]
    return {n: polynomial for n, polynomial in out.items() if polynomial}


def multiply_grouped(
    left,
    right,
    n_lo: int,
    n_hi: int,
    combine: Callable[[object, object], object],
    add: Callable[[object, object], object],
    zero,
):
    out: dict[int, dict[int, object]] = defaultdict(dict)
    multiply_adds = 0
    for n1, polynomial1 in left.items():
        for n2, polynomial2 in right.items():
            n = n1 + n2
            if n < n_lo or n > n_hi:
                continue
            target = out[n]
            for k1, coefficient1 in polynomial1.items():
                for k2, coefficient2 in polynomial2.items():
                    key = k1 + k2
                    target[key] = add(
                        target.get(key, zero), combine(coefficient1, coefficient2)
                    )
                    multiply_adds += 1
    cleaned = {
        n: {k: value for k, value in polynomial.items() if value != zero}
        for n, polynomial in out.items()
    }
    return {n: polynomial for n, polynomial in cleaned.items() if polynomial}, multiply_adds


def bitmask_series(local: Local, variable_index: dict[sp.Symbol, int]):
    out = {}
    # A coefficient can be a nonzero constant.  Reserve one bit to distinguish
    # presence from the empty dependency mask used as the product zero.
    present = 1 << len(variable_index)
    for key, expression in local.items():
        mask = 0
        for variable in expression.free_symbols.intersection(variable_index):
            mask |= 1 << variable_index[variable]
        out[key] = mask | present
    return group_local(out)


def abstract_product(left, right, n_lo: int, n_hi: int):
    # OR is both multiplication-dependency union and addition-dependency union.
    return multiply_grouped(left, right, n_lo, n_hi, int.__or__, int.__or__, 0)


def add_abstract(*series):
    out: dict[int, dict[int, int]] = defaultdict(dict)
    for source in series:
        for n, polynomial in source.items():
            for pi_power, mask in polynomial.items():
                out[n][pi_power] = out[n].get(pi_power, 0) | mask
    return dict(out)


def modular_evaluator(values: dict[sp.Symbol, int], prime: int):
    cache: dict[sp.Expr, int] = {}

    def evaluate(expression: sp.Expr) -> int:
        if expression in cache:
            return cache[expression]
        if expression.is_Integer:
            result = int(expression) % prime
        elif expression.is_Rational:
            numerator = int(expression.p) % prime
            denominator = int(expression.q) % prime
            assert denominator
            result = numerator * pow(denominator, -1, prime) % prime
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
            assert exponent.is_Integer
            result = pow(evaluate(base), int(exponent), prime)
        else:
            raise TypeError(f"unsupported modular expression node: {expression.func}")
        cache[expression] = result
        return result

    return evaluate


def evaluate_local(local: Local, evaluate: Callable[[sp.Expr], object]):
    return group_local({key: value for key, expression in local.items() if (value := evaluate(expression))})


def modular_product(left, right, n_lo: int, n_hi: int, prime: int):
    return multiply_grouped(
        left,
        right,
        n_lo,
        n_hi,
        lambda a, b: a * b % prime,
        lambda a, b: (a + b) % prime,
        0,
    )


def assemble_modular(components: dict[str, Local], evaluate, prime: int):
    numeric = {name: evaluate_local(local, evaluate) for name, local in components.items()}
    k = numeric["K2"]
    min_k = min(k)
    k_square, ops_k2 = modular_product(k, k, 2 * min_k, F_WINDOW[1] - min_k, prime)
    k_cube, ops_k3 = modular_product(k_square, k, F_WINDOW[0], F_WINDOW[1], prime)
    a2k, ops_a2k = modular_product(
        numeric["A2"], k, F_WINDOW[0], F_WINDOW[1], prime
    )
    b1k, ops_b1k = modular_product(
        numeric["B1"], k, G_WINDOW[0], G_WINDOW[1], prime
    )
    f = add_grouped(k_cube, a2k, numeric["A3"], modulus=prime)
    g = add_grouped(k_square, b1k, numeric["B2"], modulus=prime)
    f = {n: f.get(n, {}) for n in range(F_WINDOW[0], F_WINDOW[1] + 1)}
    g = {n: g.get(n, {}) for n in range(G_WINDOW[0], G_WINDOW[1] + 1)}
    return f, g, {
        "K2_square": ops_k2,
        "K2_cube": ops_k3,
        "A2_times_K2": ops_a2k,
        "B1_times_K2": ops_b1k,
    }


def assemble_abstract(components: dict[str, Local], variable_index):
    abstract = {
        name: bitmask_series(local, variable_index)
        for name, local in components.items()
    }
    k = abstract["K2"]
    min_k = min(k)
    k_square, ops_k2 = abstract_product(k, k, 2 * min_k, F_WINDOW[1] - min_k)
    k_cube, ops_k3 = abstract_product(k_square, k, F_WINDOW[0], F_WINDOW[1])
    a2k, ops_a2k = abstract_product(abstract["A2"], k, *F_WINDOW)
    b1k, ops_b1k = abstract_product(abstract["B1"], k, *G_WINDOW)
    f = add_abstract(k_cube, a2k, abstract["A3"])
    g = add_abstract(k_square, b1k, abstract["B2"])
    return f, g, {
        "K2_square": ops_k2,
        "K2_cube": ops_k3,
        "A2_times_K2": ops_a2k,
        "B1_times_K2": ops_b1k,
    }


def deterministic_values(free_variables: list[sp.Symbol], prime: int, sample: int):
    values = {}
    for index, variable in enumerate(free_variables):
        payload = f"g9966-d52-jet-probe:{sample}:{variable}".encode()
        value = int.from_bytes(hashlib.sha256(payload).digest()[:8], "big") % prime
        values[variable] = value
    # Keep the localized centre away from c=0 and avoid a misleading all-zero
    # centre in the generic-support samples.
    values[sp.Symbol("c")] = 2 + sample
    values[sp.Symbol("u")] = 5 + sample
    values[sp.Symbol("v")] = 11 + sample
    return values


def expected_p_power(power: int, c_value: int, prime: int):
    # (pi*(pi^2-c))^power
    polynomial = {0: 1}
    base = {3: 1, 1: (-c_value) % prime}
    for _ in range(power):
        product = defaultdict(int)
        for k1, a in polynomial.items():
            for k2, b in base.items():
                product[k1 + k2] = (product[k1 + k2] + a * b) % prime
        polynomial = {k: value for k, value in product.items() if value}
    return polynomial


def difference_polynomial(left: dict[int, int], right: dict[int, int], prime: int):
    return {
        key: (left.get(key, 0) - right.get(key, 0)) % prime
        for key in sorted(set(left) | set(right))
        if (left.get(key, 0) - right.get(key, 0)) % prime
    }


def prefix(name: str) -> str:
    if name in {"u", "v", "c"}:
        return "centre"
    return name.split("c_", 1)[0]


def local_metrics(local: Local, free_set: set[sp.Symbol]):
    used = set().union(
        *(expression.free_symbols.intersection(free_set) for expression in local.values())
    ) if local else set()
    op_counts = [int(sp.count_ops(expression, visual=False)) for expression in local.values()]
    return {
        "coefficient_count": len(local),
        "n_min": min((n for n, _k in local), default=None),
        "n_max": max((n for n, _k in local), default=None),
        "pi_power_min": min((k for _n, k in local), default=None),
        "pi_power_max": max((k for _n, k in local), default=None),
        "free_variables_used": len(used),
        "free_variables_by_prefix": dict(sorted(Counter(prefix(str(v)) for v in used).items())),
        "symbolic_count_ops_sum": sum(op_counts),
        "symbolic_count_ops_max": max(op_counts, default=0),
        "canonical_expression_sha256": sha256_lines(
            f"{n},{k}\t{sp.srepr(local[(n, k)])}" for n, k in sorted(local)
        ),
    }


def window_summary(
    window: tuple[int, int],
    abstract,
    modular_runs: list[dict[int, dict[int, int]]],
    variable_count: int,
):
    rows = []
    total_mask = 0
    for n in range(window[0], window[1] + 1):
        structural = abstract.get(n, {})
        structural_powers = set(structural)
        masks = list(structural.values())
        mask = 0
        for item in masks:
            mask |= item
        variable_mask = mask & ((1 << variable_count) - 1)
        total_mask |= variable_mask
        observed_sets = [set(run.get(n, {})) for run in modular_runs]
        union = set().union(*observed_sets)
        intersection = set.intersection(*observed_sets) if observed_sets else set()
        rows.append({
            "n": n,
            "structural_pi_powers": sorted(structural_powers),
            "observed_pi_powers_union_3_primes": sorted(union),
            "observed_pi_powers_intersection_3_primes": sorted(intersection),
            "structural_free_variable_count": variable_mask.bit_count(),
        })
    return rows, total_mask


def main() -> None:
    clock = Clock.begin()
    custody = verify_frozen(("band_engine.py", "stage7.json", "stage7-free-coefficients.txt"))
    stage = json.loads(STAGE7.read_text(encoding="utf-8"))
    frozen_free_names = FREE_LIST.read_text(encoding="utf-8").splitlines()
    engine = load_engine()
    assert stage["branch"] == "delta52" and stage["stage_spec"]["stage"] == 7
    assert stage["driver_sha256"] == custody["checked"]["band_engine.py"]
    clock.stamp("verified frozen inputs and imported engine")

    k2, inner_free, major_meta = engine.build_major_h2("delta52", 33)
    clock.stamp("rebuilt pure major-h2 chart", k2_tz_terms=len(k2), inner_free=len(inner_free))
    outer, outer_free, outer_meta = engine.outer_state(7)
    clock.stamp("rebuilt pure outer chart through D1 offset 7", outer_free=len(outer_free))

    ambient = set(inner_free) | set(outer_free)
    raw_joint, joint_map, joint_hash = parse_joint_map(engine, stage, ambient)
    remaining = ambient - set(raw_joint)
    computed_names = sorted(map(str, remaining))
    assert len(ambient) == 928 and len(remaining) == 869
    assert computed_names == frozen_free_names
    assert computed_names == stage["unresolved_quotient_generators"]
    assert all(rhs.free_symbols.issubset(remaining) for rhs in joint_map.values())
    clock.stamp("resolved and verified serialized joint pivots", joint_pivots=len(joint_map))

    resolved_outer = {
        block: {
            position: engine.substitute_map(value, joint_map)
            for position, value in coordinates.items()
        }
        for block, coordinates in outer.items()
    }
    assert not set().union(
        *(value.free_symbols.intersection(raw_joint)
          for coordinates in resolved_outer.values() for value in coordinates.values())
    )

    u, v = map(engine.symbol, ("u", "v"))
    max_q = max(q for _r, q in k2)
    max_q = max(
        max_q,
        *(q for coordinates in resolved_outer.values() for _r, q in coordinates),
    )
    tables = z_power_table(max_q, F_WINDOW[1], u, v)
    # Check the direct z-pullback against the frozen engine on a nontrivial toy.
    toy_x = engine.symbol("toy_x")
    toy = {(2, 3): toy_x}
    direct_toy = localize_tz(toy, tables, 0, 35)
    frozen_toy = {
        key: value for key, value in engine.local_rows(toy, "delta52", 35).items()
        if value != 0
    }
    assert direct_toy == frozen_toy
    clock.stamp("built direct localizer and matched frozen delta52 transform", max_q=max_q)

    k_local = localize_tz(k2, tables, 0, F_WINDOW[1])
    min_k = min(n for n, _pi_power in k_local)
    clock.stamp("localized K2 exactly", coefficients=len(k_local), minimum_n=min_k)

    # Only ranges capable of contributing to the requested F/G windows are
    # retained.  K2 itself is kept through 233 because it is shared by both
    # nonlinear powers and outer products.
    a2_tz = engine.outer_effective_tz(resolved_outer, "A2", F_WINDOW[1] // 2)
    a3_tz = engine.outer_effective_tz(resolved_outer, "A3", F_WINDOW[1] // 2)
    b1_tz = engine.outer_effective_tz(resolved_outer, "B1", G_WINDOW[1] // 2)
    b2_tz = engine.outer_effective_tz(resolved_outer, "B2", G_WINDOW[1] // 2)
    components = {
        "K2": k_local,
        "A2": localize_tz(a2_tz, tables, 0, F_WINDOW[1] - min_k),
        "A3": localize_tz(a3_tz, tables, *F_WINDOW),
        "B1": localize_tz(b1_tz, tables, 0, G_WINDOW[1] - min_k),
        "B2": localize_tz(b2_tz, tables, *G_WINDOW),
    }
    clock.stamp(
        "localized all exact linear chart components",
        coefficient_counts={name: len(value) for name, value in components.items()},
    )

    free_variables = sorted(remaining, key=str)
    variable_index = {variable: index for index, variable in enumerate(free_variables)}
    abstract_f, abstract_g, abstract_ops = assemble_abstract(components, variable_index)
    clock.stamp("assembled structural nonlinear support", operation_counts=abstract_ops)

    modular_f = []
    modular_g = []
    modular_meta = []
    leading_checks = []
    for sample, prime in enumerate(PRIMES):
        values = deterministic_values(free_variables, prime, sample)
        evaluate = modular_evaluator(values, prime)
        f_run, g_run, operation_counts = assemble_modular(components, evaluate, prime)
        modular_f.append(f_run)
        modular_g.append(g_run)
        expected_f = expected_p_power(9, values[sp.Symbol("c")], prime)
        expected_g = expected_p_power(6, values[sp.Symbol("c")], prime)
        f_difference = difference_polynomial(f_run[F_WINDOW[0]], expected_f, prime)
        g_difference = difference_polynomial(g_run[G_WINDOW[0]], expected_g, prime)
        leading_checks.append({
            "prime": prime,
            "assignment_rule": f"sha256(sample={sample},variable), centre c={2+sample},u={5+sample},v={11+sample}",
            "F_n189_equals_p9": not f_difference,
            "G_n126_equals_p6": not g_difference,
            "F_first_difference": list(next(iter(f_difference.items()))) if f_difference else None,
            "G_first_difference": list(next(iter(g_difference.items()))) if g_difference else None,
            "F_difference_coefficient_count": len(f_difference),
            "G_difference_coefficient_count": len(g_difference),
        })
        modular_meta.append({"prime": prime, "operation_counts": operation_counts})
        clock.stamp(f"assembled full requested windows modulo {prime}")

    f_rows, f_mask = window_summary(F_WINDOW, abstract_f, modular_f, len(free_variables))
    g_rows, g_mask = window_summary(G_WINDOW, abstract_g, modular_g, len(free_variables))
    all_mask = f_mask | g_mask
    used_variables = [
        str(variable) for index, variable in enumerate(free_variables)
        if all_mask & (1 << index)
    ]
    component_metrics = {
        name: local_metrics(local, remaining) for name, local in components.items()
    }
    clock.stamp("summarized coefficient support and symbolic component complexity")

    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    result = {
        "type": "BOUNDED EXPLORATORY delta52 STAGE7 MINOR-JET PROBE",
        "scope": {
            "F_normalized_n_window": list(F_WINDOW),
            "G_normalized_n_window": list(G_WINDOW),
            "normalization": "F actual s-order=n-198; G actual s-order=n-132",
            "assembly": "F=K2^3+A2*K2+A3; G=K2^2+B1*K2+B2",
            "warning": "structural dependency masks are upper supports; three-prime observed pi supports are generic evaluations, not a symbolic Groebner certificate",
        },
        "custody": custody,
        "stage7_reconstruction": {
            "pure_builder": str(BAND_ENGINE),
            "major_inner_free": len(inner_free),
            "outer_free_after_D1_offset7": len(outer_free),
            "ambient_before_joint_pivots": len(ambient),
            "serialized_joint_pivots": len(joint_map),
            "joint_pivot_prefix_counts": dict(sorted(Counter(prefix(str(v)) for v in joint_map).items())),
            "joint_resolved_rhs_all_zero": all(rhs == 0 for rhs in joint_map.values()),
            "joint_rhs_ledger_sha256": joint_hash,
            "free_after_joint_pivots": len(remaining),
            "free_names_sha256": sha256_lines(computed_names),
            "matches_stage7_json_and_869_line_list": True,
            "major_metadata": major_meta,
            "outer_D1_cumulative_pivots": outer_meta["D1_cumulative_pivots"],
        },
        "component_metrics": component_metrics,
        "support_complexity": {
            "minimum_K2_local_n_after_stage7": min_k,
            "structural_multiply_adds": abstract_ops,
            "modular_runs": modular_meta,
            "requested_window_free_variables_structural_upper_count": len(used_variables),
            "requested_window_free_variables_by_prefix": dict(sorted(Counter(prefix(v) for v in used_variables).items())),
            "requested_window_free_names_sha256": sha256_lines(used_variables),
        },
        "leading_coefficient_test": {
            "expected": {"F_n189": "(pi*(pi^2-c))^9", "G_n126": "(pi*(pi^2-c))^6"},
            "all_three_F_equal": all(item["F_n189_equals_p9"] for item in leading_checks),
            "all_three_G_equal": all(item["G_n126_equals_p6"] for item in leading_checks),
            "tests": leading_checks,
            "interpretation": "Any displayed nonzero good-prime specialization proves the equality is not an identity modulo the reconstructed stage-7 linear quotient.",
        },
        "F_support_by_n": f_rows,
        "G_support_by_n": g_rows,
        "runtime": {
            "events": clock.events,
            "wall_seconds": round(time.perf_counter() - clock.start, 6),
            "peak_rss_kib": rss,
            "thread_environment": {
                key: os.environ.get(key) for key in (
                    "OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"
                )
            },
        },
        "verdict": "PROBE-ONLY",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
