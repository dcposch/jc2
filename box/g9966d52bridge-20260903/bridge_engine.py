#!/usr/bin/env python3
"""Exact stage-7 delta=5/2 effective-T2/T3 bridge engine.

The charged band engine stores the chart in (t,z=w-1).  This driver rebuilds
its pure coordinate maps, applies the charged 59 stage-7 pivots, pushes the
minor substitution t=s^2, w=u*s^4+v*s^6+pi*s^7 through each *factor*, and only
then multiplies truncated nonnegative local series.  This avoids a global
z-basis expansion before restriction to the minor root.

Every truncation is by an upper s-degree in a nonnegative series, hence exact
for the requested coefficient rows.  No pi-degree cap is used.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import importlib.util
import json
from math import comb, factorial
from pathlib import Path
import resource
import signal
import sys
import time
from typing import Iterable

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
FROZEN = Path("/tmp/jc2-lane.IAeCOg/inputs")
RECEIPT = ROOT / "xmodel/g9966-delta52-bridge-sol56-20260903.run.v2"
STAGE7 = FROZEN / "stage7.json"
FREE_LIST = FROZEN / "stage7-free-coefficients.txt"
NEXT = FROZEN / "next-stage8-system.json"
CHARGED_ENGINE = FROZEN / "band_engine.py"

T2_TARGET_S = 391
T3_TARGET_S = 1178
PRIMES = (32003, 104729, 1299709)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def row_hash(rows: Iterable[tuple[str, sp.Expr]]) -> str:
    digest = hashlib.sha256()
    for label, expr in rows:
        digest.update(label.encode())
        digest.update(b"\t")
        digest.update(sp.srepr(expr).encode())
        digest.update(b"\n")
    return digest.hexdigest()


def load_charged_module():
    spec = importlib.util.spec_from_file_location("charged_band_engine", CHARGED_ENGINE)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load charged band engine")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def verify_frozen() -> dict:
    fields: dict[str, str] = {}
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value
    count = int(fields["charged_inputs"])
    assert count == 21
    assert Path(fields["lane_inputs_dir"]) == FROZEN
    checked = []
    for index in range(1, count + 1):
        name = fields[f"charged_input_{index}_basename"]
        expected = fields[f"charged_input_{index}_sha256"]
        actual = sha256(FROZEN / name)
        if actual != expected:
            raise RuntimeError(f"charged input mismatch: {name}")
        checked.append({"basename": name, "sha256": actual})
    return {"count": count, "all_match": True, "checked": checked}


def load_endpoint(band) -> tuple[dict, list[str], dict[sp.Symbol, sp.Expr], object, object, dict]:
    stage = json.loads(STAGE7.read_text(encoding="utf-8"))
    nxt = json.loads(NEXT.read_text(encoding="utf-8"))
    free_names = FREE_LIST.read_text(encoding="utf-8").splitlines()
    assert stage["branch"] == "delta52"
    assert stage["stage_spec"]["stage"] == 7
    assert stage["counts"]["exact_Krull_dimension_localized"] == 869
    assert stage["joint_elimination"]["residual_count"] == 0
    assert stage["joint_elimination"]["Qstar_pivots"] == 59
    assert free_names == stage["unresolved_quotient_generators"]
    assert free_names == nxt["unresolved_quotient_generators"]
    assert len(free_names) == len(set(free_names)) == 869

    # Full K2 has t-degree 33.  Products are taken only after local restriction.
    k2, inner_free, major_meta = band.build_major_h2("delta52", 33)
    outer, outer_free, outer_meta = band.outer_state(7)

    # Parse and independently resolve the charged joint ledger.  In this stage
    # every chain ends at zero, but that fact is checked rather than assumed.
    locals_map = {name: sp.Symbol(name) for name in set(free_names)}
    for item in stage["joint_elimination"]["pivot_ledger"]:
        locals_map.setdefault(item["variable"], sp.Symbol(item["variable"]))
        for token in sp.sympify(item["rhs"]).free_symbols:
            locals_map.setdefault(str(token), sp.Symbol(str(token)))
    raw_map: dict[sp.Symbol, sp.Expr] = {}
    for item in stage["joint_elimination"]["pivot_ledger"]:
        variable = sp.Symbol(item["variable"])
        raw_map[variable] = sp.sympify(item["rhs"], locals=locals_map)
    resolved = band.resolve_map(raw_map)
    assert len(resolved) == 59
    assert all(value == 0 for value in resolved.values())

    reconstructed = (set(inner_free) | set(outer_free)) - set(resolved)
    assert sorted(map(str, reconstructed)) == free_names
    assert outer_meta["D1_cumulative_pivots"] == 176
    assert outer_meta["outer_free_count"] == 826
    assert major_meta["major_output_free_count"] == 99

    meta = {
        "stage7_sha256": sha256(STAGE7),
        "free_list_sha256": sha256(FREE_LIST),
        "next_manifest_sha256": sha256(NEXT),
        "charged_driver_sha256": sha256(CHARGED_ENGINE),
        "free_count": len(free_names),
        "family_counts": {
            prefix: sum(name.startswith(prefix) for name in free_names)
            for prefix in ("A2c_", "A3c_", "B1c_", "B2c_", "K2c_")
        }
        | {"centre": sum(name in {"c", "u", "v"} for name in free_names)},
        "outer_D1_pivots": outer_meta["D1_cumulative_pivots"],
        "joint_pivots": len(resolved),
        "joint_all_zero": True,
        "joint_pivot_variables": sorted(map(str, resolved)),
        "coordinate_field": "Q",
        "coordinate_order": "charged lexicographic symbol names",
    }
    return stage, free_names, resolved, k2, outer, meta


# A local series is (s degree, pi degree) -> coefficient in the chart ring.
LS = dict[tuple[int, int], sp.Expr]


@dataclass
class ArithmeticStats:
    localized_terms: int = 0
    products_considered: int = 0
    products_retained: int = 0


def _sum_terms(values: list[sp.Expr]) -> sp.Expr:
    if not values:
        return sp.Integer(0)
    # Chunking avoids very deep binary Add trees while retaining a compact DAG.
    level = values
    while len(level) > 256:
        level = [sp.Add(*level[i : i + 256]) for i in range(0, len(level), 256)]
    return sp.Add(*level)


def ls_clean(item: LS) -> LS:
    return {key: value for key, value in item.items() if value != 0}


def ls_add(*items: LS) -> LS:
    buckets: dict[tuple[int, int], list[sp.Expr]] = defaultdict(list)
    for item in items:
        for key, value in item.items():
            if value != 0:
                buckets[key].append(value)
    out = {}
    for key, values in buckets.items():
        value = sp.expand(_sum_terms(values))
        if value != 0:
            out[key] = value
    return out


def ls_scale(item: LS, scalar: sp.Expr | int) -> LS:
    scalar = sp.sympify(scalar)
    if scalar == 0:
        return {}
    return {key: scalar * value for key, value in item.items() if value != 0}


def ls_shift(item: LS, amount: int, cap: int) -> LS:
    return {(n + amount, k): value for (n, k), value in item.items() if n + amount <= cap}


def ls_mul(left: LS, right: LS, cap: int, stats: ArithmeticStats) -> LS:
    if not left or not right:
        return {}
    by_n_left: dict[int, list[tuple[int, sp.Expr]]] = defaultdict(list)
    by_n_right: dict[int, list[tuple[int, sp.Expr]]] = defaultdict(list)
    for (n, k), value in left.items():
        by_n_left[n].append((k, value))
    for (n, k), value in right.items():
        by_n_right[n].append((k, value))
    buckets: dict[tuple[int, int], list[sp.Expr]] = defaultdict(list)
    for n1, poly1 in by_n_left.items():
        for n2, poly2 in by_n_right.items():
            stats.products_considered += len(poly1) * len(poly2)
            n = n1 + n2
            if n > cap:
                continue
            for k1, a in poly1:
                for k2, b in poly2:
                    buckets[(n, k1 + k2)].append(a * b)
                    stats.products_retained += 1
    out = {}
    for key, values in buckets.items():
        value = sp.expand(_sum_terms(values))
        if value != 0:
            out[key] = value
    return out


def ls_pow(item: LS, exponent: int, cap: int, stats: ArithmeticStats) -> LS:
    if exponent == 0:
        return {(0, 0): sp.Integer(1)}
    result: LS = {(0, 0): sp.Integer(1)}
    base = item
    power = exponent
    while power:
        if power & 1:
            result = ls_mul(result, base, cap, stats)
        power >>= 1
        if power:
            base = ls_mul(base, base, cap, stats)
    return result


def z_power_tables(maximum: int, cap: int) -> list[LS]:
    """Powers of z=-1+u*s^4+v*s^6+pi*s^7, coefficient-split in pi."""
    u, v = sp.symbols("u v")
    tables: list[LS] = [{(0, 0): sp.Integer(1)}]
    for _ in range(maximum):
        old = tables[-1]
        buckets: dict[tuple[int, int], list[sp.Expr]] = defaultdict(list)
        for (n, k), coefficient in old.items():
            buckets[(n, k)].append(-coefficient)
            if n + 4 <= cap:
                buckets[(n + 4, k)].append(u * coefficient)
            if n + 6 <= cap:
                buckets[(n + 6, k)].append(v * coefficient)
            if n + 7 <= cap:
                buckets[(n + 7, k + 1)].append(coefficient)
        tables.append({key: sp.expand(_sum_terms(values)) for key, values in buckets.items()})
    return tables


def localize_tz(
    item,
    tables: list[LS],
    cap: int,
    joint_map: dict[sp.Symbol, sp.Expr],
    stats: ArithmeticStats,
) -> LS:
    """Apply t=s^2 and the precomputed z=w-1 powers to a TZ series."""
    buckets: dict[tuple[int, int], list[sp.Expr]] = defaultdict(list)
    for (r, q), raw_coefficient in item.items():
        coefficient = raw_coefficient.xreplace(joint_map)
        if coefficient == 0:
            continue
        for (delta, k), factor in tables[q].items():
            n = 2 * r + delta
            if n <= cap:
                buckets[(n, k)].append(coefficient * factor)
                stats.localized_terms += 1
    out = {}
    for key, values in buckets.items():
        value = sp.expand(_sum_terms(values))
        if value != 0:
            out[key] = value
    return out


def series_summary(item: LS) -> dict:
    if not item:
        return {"terms": 0, "s_min": None, "s_max": None, "pi_max": None}
    return {
        "terms": len(item),
        "s_min": min(n for n, _k in item),
        "s_max": max(n for n, _k in item),
        "pi_max": max(k for _n, k in item),
        "bands": len({n for n, _k in item}),
    }


def block_series(band, k2, outer, cap: int, joint_map, stats: ArithmeticStats) -> dict[str, LS]:
    effective = {
        name: band.outer_effective_tz(outer, name, 200)
        for name in ("A2", "A3", "B1", "B2")
    }
    max_q = max(q for _r, q in k2)
    max_q = max(max_q, *(q for item in effective.values() for _r, q in item))
    tables = z_power_tables(max_q, cap)
    blocks = {"H": localize_tz(k2, tables, cap, joint_map, stats)}
    for name in ("A2", "A3", "B1", "B2"):
        blocks[name] = localize_tz(effective[name], tables, cap, joint_map, stats)
    return blocks


def build_FG_from_blocks(blocks: dict[str, LS], cap: int, stats: ArithmeticStats) -> tuple[LS, LS, LS, LS]:
    H, A2, A3, B1, B2 = (blocks[name] for name in ("H", "A2", "A3", "B1", "B2"))
    H2 = ls_mul(H, H, cap, stats)
    H3 = ls_mul(H2, H, cap, stats)
    EF = ls_add(ls_mul(A2, H, cap, stats), A3)
    EG = ls_add(ls_mul(B1, H, cap, stats), B2)
    return ls_add(H3, EF), ls_add(H2, EG), EF, EG


def monic_t2_and_FG(
    blocks: dict[str, LS], cap: int, stats: ArithmeticStats
) -> tuple[LS, LS, LS, LS, LS]:
    """Return G^3-F^2, F, G, EF, EG after cancelling H^6 structurally."""
    H, A2, A3, B1, B2 = (blocks[name] for name in ("H", "A2", "A3", "B1", "B2"))
    H2 = ls_mul(H, H, cap, stats)
    H3 = ls_mul(H2, H, cap, stats)
    H4 = ls_mul(H3, H, cap, stats)
    EF = ls_add(ls_mul(A2, H, cap, stats), A3)
    EG = ls_add(ls_mul(B1, H, cap, stats), B2)
    EG2 = ls_mul(EG, EG, cap, stats)
    EG3 = ls_mul(EG2, EG, cap, stats)
    EF2 = ls_mul(EF, EF, cap, stats)
    monic = ls_add(
        ls_scale(ls_mul(H4, EG, cap, stats), 3),
        ls_scale(ls_mul(H2, EG2, cap, stats), 3),
        EG3,
        ls_scale(ls_mul(H3, EF, cap, stats), -2),
        ls_scale(EF2, -1),
    )
    return monic, ls_add(H3, EF), ls_add(H2, EG), EF, EG


def build_t2(blocks: dict[str, LS], cap: int, stats: ArithmeticStats) -> tuple[LS, dict]:
    assert cap == T2_TARGET_S
    H = blocks["H"]
    a1, a0, b1, _b0 = sp.symbols("T2_a1 T2_a0 T2_b1 T2_b0")
    Hpow = [{(0, 0): sp.Integer(1)}, H]
    for _ in range(2, 6):
        Hpow.append(ls_mul(Hpow[-1], H, cap, stats))
    monic, F, G, EF, EG = monic_t2_and_FG(blocks, cap, stats)
    # FG=H^5+H^3 EG+H^2 EF+EF EG.
    FG = ls_add(
        Hpow[5],
        ls_mul(Hpow[3], EG, cap, stats),
        ls_mul(Hpow[2], EF, cap, stats),
        ls_mul(EF, EG, cap, stats),
    )
    out = ls_add(
        monic,
        ls_scale(ls_shift(FG, 66, cap), a1),
        ls_scale(ls_shift(G, 264, cap), a0),
        ls_scale(ls_shift(F, 198, cap), b1),
        # T2_b0 begins at s^396 and is intentionally absent through the leader.
    )
    return out, {
        "H": series_summary(H),
        "EF": series_summary(EF),
        "EG": series_summary(EG),
        "F": series_summary(F),
        "G": series_summary(G),
        "U2": series_summary(out),
        "T2_b0_first_s": 396,
    }


def consecutive_powers(item: LS, maximum: int, cap: int, stats: ArithmeticStats) -> list[LS]:
    powers = [{(0, 0): sp.Integer(1)}]
    for _ in range(maximum):
        powers.append(ls_mul(powers[-1], item, cap, stats))
    return powers


def t3_coefficient_names() -> list[str]:
    names = []
    for i in range(2, 10):
        for m in range((2 * i) // 3 + 1):
            if (i, m) == (9, 6):
                continue
            names.append(f"T3_a{i}_m{m}")
    assert len(names) == 34
    return names


def build_t3(blocks: dict[str, LS], cap: int, stats: ArithmeticStats) -> tuple[LS, dict]:
    assert cap == T3_TARGET_S
    monic2, F, G, _EF, _EG = monic_t2_and_FG(blocks, cap, stats)
    Fpow = consecutive_powers(F, 6, cap, stats)
    Gpow = consecutive_powers(G, 7, cap, stats)

    # G^9-F^6=(G^3-F^2)(G^6+G^3 F^2+F^4), so the H^18 face is
    # cancelled before any ninth/sixth power is expanded.
    factor = ls_add(
        Gpow[6],
        ls_mul(Gpow[3], Fpow[2], cap, stats),
        Fpow[4],
    )
    out = ls_mul(monic2, factor, cap, stats)

    names = []
    column_summaries = {}
    for i in range(2, 10):
        for m in range((2 * i) // 3 + 1):
            if (i, m) == (9, 6):
                continue
            name = f"T3_a{i}_m{m}"
            names.append(name)
            shift = 132 * i - 198 * m
            available = cap - shift
            term = ls_mul(Fpow[m], Gpow[9 - i], available, stats)
            term = ls_shift(term, shift, cap)
            column_summaries[name] = series_summary(term) | {"shift": shift}
            out = ls_add(out, ls_scale(term, sp.Symbol(name)))
    assert names == t3_coefficient_names()
    return out, {
        "F": series_summary(F),
        "G": series_summary(G),
        "monic_G9_minus_F6": series_summary(ls_mul(monic2, factor, cap, stats)),
        "U3": series_summary(out),
        "coefficient_count": len(names),
        "coefficient_columns": column_summaries,
    }


# Univariate t series used only to recover the genuine degree-zero Jacobian
# scalar.  Coefficients remain in the chart ring.
US = dict[int, sp.Expr]


def us_add(*items: US) -> US:
    buckets: dict[int, list[sp.Expr]] = defaultdict(list)
    for item in items:
        for degree, value in item.items():
            if value != 0:
                buckets[degree].append(value)
    return {degree: _sum_terms(values) for degree, values in buckets.items()}


def us_scale(item: US, scalar: int | sp.Expr) -> US:
    return {degree: sp.sympify(scalar) * value for degree, value in item.items() if value != 0}


def us_mul(left: US, right: US, cap: int) -> US:
    buckets: dict[int, list[sp.Expr]] = defaultdict(list)
    for d1, a in left.items():
        for d2, b in right.items():
            if d1 + d2 <= cap:
                buckets[d1 + d2].append(a * b)
    return {degree: _sum_terms(values) for degree, values in buckets.items()}


def tz_at_z(item, joint_map, derivative: bool = False) -> US:
    buckets: dict[int, list[sp.Expr]] = defaultdict(list)
    for (r, q), raw in item.items():
        value = raw.xreplace(joint_map)
        if derivative:
            if q == 0:
                continue
            value *= q * ((-1) ** (q - 1))
        else:
            value *= (-1) ** q
        if value != 0:
            buckets[r].append(value)
    return {degree: _sum_terms(values) for degree, values in buckets.items()}


def jacobian_scalar(band, k2, outer, joint_map) -> sp.Expr:
    """Coefficient [t^163 w^0] of the charged normalized Jacobian."""
    pieces = {"H": k2}
    for name in ("A2", "A3", "B1", "B2"):
        pieces[name] = band.outer_effective_tz(outer, name, 200)
    val = {name: tz_at_z(item, joint_map, False) for name, item in pieces.items()}
    dz = {name: tz_at_z(item, joint_map, True) for name, item in pieces.items()}
    H, A, C, B, D = (val[n] for n in ("H", "A2", "A3", "B1", "B2"))
    Hz, Az, Cz, Bz, Dz = (dz[n] for n in ("H", "A2", "A3", "B1", "B2"))
    H2 = us_mul(H, H, 163)
    H3 = us_mul(H2, H, 163)
    F = us_add(H3, us_mul(A, H, 163), C)
    G = us_add(H2, us_mul(B, H, 163), D)
    Fz = us_add(
        us_scale(us_mul(H2, Hz, 163), 3),
        us_mul(Az, H, 163), us_mul(A, Hz, 163), Cz,
    )
    Gz = us_add(
        us_scale(us_mul(H, Hz, 163), 2),
        us_mul(Bz, H, 163), us_mul(B, Hz, 163), Dz,
    )
    terms = []
    for r, fr in F.items():
        other = 163 - r
        if other in Gz:
            terms.append((99 - r) * fr * Gz[other])
    for r, fzr in Fz.items():
        other = 163 - r
        if other in G:
            terms.append((other - 66) * fzr * G[other])
    return _sum_terms(terms)


def target_polynomials() -> tuple[dict[int, sp.Expr], dict[int, sp.Expr]]:
    pi, c, kappa = sp.symbols("pi c kappa")
    p = pi * (pi**2 - c)
    q1 = sp.integrate(-2 * p**3, pi)
    p5 = sp.Poly(sp.expand(p**5), pi)
    p10q1 = sp.Poly(sp.expand(kappa * p**10 * q1), pi)
    return (
        {int(power[0]): coefficient for power, coefficient in p5.terms()},
        {int(power[0]): coefficient for power, coefficient in p10q1.terms()},
    )


def coefficient_rows(series: LS, target_s: int, target: dict[int, sp.Expr], prefix: str) -> list[tuple[str, sp.Expr]]:
    keys = {(n, k) for n, k in series if n <= target_s}
    keys.update((target_s, k) for k in target)
    rows = []
    for n, k in sorted(keys):
        if n > target_s:
            continue
        expr = series.get((n, k), sp.Integer(0))
        if n == target_s:
            expr = expr - target.get(k, sp.Integer(0))
        if expr != 0:
            rows.append((f"{prefix}_s{n}_pi{k}", expr))
    return rows


def checkpoint(data: dict) -> None:
    data = dict(data)
    data["checkpoint_utc_epoch"] = time.time()
    HERE.joinpath("checkpoint.json").write_text(json.dumps(data, indent=2, sort_keys=True, default=str) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--phase", choices=("map", "t2"), default="t2")
    args = parser.parse_args()
    started = time.perf_counter()
    stats = ArithmeticStats()
    custody = verify_frozen()
    band = load_charged_module()
    stage, free_names, joint_map, k2, outer, endpoint = load_endpoint(band)
    result = {
        "type": "EXACT-Q DELTA52 STAGE7 EFFECTIVE BRIDGE",
        "phase": args.phase,
        "custody": {"count": custody["count"], "all_match": custody["all_match"]},
        "endpoint": endpoint,
        "normalization": {
            "KF": "t^99 F", "KG": "t^66 G", "t": "s^2",
            "minor_substitution": "w=u*s^4+v*s^6+pi*s^7",
            "T2_target_s": T2_TARGET_S,
            "T3_target_s": T3_TARGET_S,
            "T2_coefficients": ["T2_a1", "T2_a0", "T2_b1", "T2_b0"],
            "T2_alpha1": "c0=0",
            "T3_coefficient_count": 34,
        },
    }
    checkpoint(result | {"status": "endpoint-loaded"})
    if args.phase == "map":
        result["status"] = "COMPLETE[MAP]"
    else:
        blocks = block_series(band, k2, outer, T2_TARGET_S, joint_map, stats)
        result["blocks"] = {name: series_summary(value) for name, value in blocks.items()}
        checkpoint(result | {"status": "localized-blocks"})
        U2, t2_meta = build_t2(blocks, T2_TARGET_S, stats)
        target2, _target3 = target_polynomials()
        rows = coefficient_rows(U2, T2_TARGET_S, target2, "T2")
        rational_nonzero = [
            (label, str(expr)) for label, expr in rows if expr.is_Rational and expr != 0
        ]
        active = sorted(set().union(*(expr.free_symbols for _label, expr in rows)), key=str) if rows else []
        result.update({
            "status": "COMPLETE[T2-ROWS-NOT-YET-QSTAR]",
            "t2": t2_meta | {
                "row_count": len(rows),
                "first_row": rows[0][0] if rows else None,
                "last_row": rows[-1][0] if rows else None,
                "active_symbol_count": len(active),
                "active_symbols_head": list(map(str, active[:30])),
                "rational_nonzero_rows": rational_nonzero[:20],
                "row_hash_dag_srepr": row_hash(rows),
            },
        })
        # Bounded row serialization: tags and expression-size diagnostics only.
        HERE.joinpath("t2-row-labels.txt").write_text("".join(label + "\n" for label, _ in rows))
    result["arithmetic"] = stats.__dict__
    result["resources"] = {
        "wall_seconds": round(time.perf_counter() - started, 3),
        "max_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    }
    HERE.joinpath("bridge-results.json").write_text(json.dumps(result, indent=2, sort_keys=True, default=str) + "\n")
    checkpoint(result)
    print(json.dumps(result, indent=2, sort_keys=True, default=str))


if __name__ == "__main__":
    main()
