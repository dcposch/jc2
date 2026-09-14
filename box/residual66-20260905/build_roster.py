#!/usr/bin/env python3
"""Build the deterministic 66-row necessary-configuration roster.

Inputs are the patched own-child sweep and the independently emitted G_i chart
counts.  This driver deliberately reruns the source split-window screen.  It
does not turn a necessary source row, a retained child prefix, or a surviving
ES leaf into an attained polynomial pair.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from copy import deepcopy
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Mapping


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.dont_write_bytecode = True

from box.lib.split_window import screen_skeleton  # noqa: E402


DEFAULT_OWN_ROWS = ROOT / "box/child-own-v-20260905/own-rows.jsonl"
DEFAULT_CHART_COUNTS = HERE / "chart-counts.json"
DEFAULT_JSONL = HERE / "roster.jsonl"
DEFAULT_MARKDOWN = HERE / "roster.md"

SCHEMA = "jc2.residual66.roster/v1"
CHART_SCHEMA = "jc2.residual66.gi-chart-counts/v1"
PROP_RADIUS_OPEN = "OPEN[PROP6.3-RADIUS-US>1]"
CHILD_TERMINAL_OPEN = "OPEN[CHILD-TERMINAL-SUPPORT-US>1]"
EXACT_Q_DEMO_THRESHOLD = 60


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        value = json.loads(raw)
        if not isinstance(value, dict):
            raise AssertionError(f"{path}:{line_number}: row is not an object")
        rows.append(value)
    return rows


def indexed(mapping: Mapping[Any, Any], index: int) -> Any:
    if index in mapping:
        return mapping[index]
    return mapping[str(index)]


def indexed_list(mapping: Mapping[Any, Any], first: int, last: int) -> list[Any]:
    return [indexed(mapping, i) for i in range(first, last + 1)]


def source_key_from_parts(
    n: int, m: int, M: Iterable[int], V: Iterable[int]
) -> tuple[int, int, tuple[int, ...], tuple[int, ...]]:
    return int(n), int(m), tuple(map(int, M)), tuple(map(int, V))


def source_key(own: Mapping[str, Any]) -> tuple[int, int, tuple[int, ...], tuple[int, ...]]:
    source = own["source"]
    s = int(source["s"])
    return source_key_from_parts(
        source["n"],
        source["m"],
        indexed_list(source["M"], 1, s),
        indexed_list(source["V"], 2, s),
    )


def receiver_tuple(value: Mapping[str, Any]) -> tuple[int, int, int, int]:
    return (
        int(value["n_prime"]),
        int(value["m_prime"]),
        int(value["M_terminal_prime"]),
        int(value["ell"]),
    )


def child_receiver_tuple(own: Mapping[str, Any]) -> tuple[int, int, int, int]:
    s_prime = int(own["s"])
    return (
        int(own["n"]),
        int(own["m"]),
        int(indexed(own["M"], s_prime)),
        int(own["ell"]),
    )


def collect_values(node: Any, key: str) -> list[Any]:
    out: list[Any] = []
    if isinstance(node, dict):
        if key in node:
            out.append(node[key])
        for value in node.values():
            out.extend(collect_values(value, key))
    elif isinstance(node, list):
        for value in node:
            out.extend(collect_values(value, key))
    return out


def chart_index(path: Path) -> tuple[dict[tuple[int, int, int, int], dict[str, Any]], dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema") != CHART_SCHEMA:
        raise AssertionError(f"unexpected chart schema {payload.get('schema')!r}")
    classes = payload.get("classes")
    if not isinstance(classes, list):
        raise AssertionError("chart-counts.json must contain a classes list")
    answer: dict[tuple[int, int, int, int], dict[str, Any]] = {}
    required = (
        "unknowns_without_T",
        "unknowns_with_T",
        "coefficient_generators",
        "generators_including_Tc_minus_1",
    )
    for item in classes:
        key = receiver_tuple(item["receiver_key"])
        if key in answer:
            raise AssertionError(f"duplicate receiver chart key {key}")
        for name in required:
            if name not in item or not isinstance(item[name], int) or item[name] < 0:
                raise AssertionError(f"bad chart field {name} at {key}")
        if item["unknowns_with_T"] != item["unknowns_without_T"] + 1:
            raise AssertionError(f"T unknown count mismatch at {key}")
        if item["generators_including_Tc_minus_1"] != item["coefficient_generators"] + 1:
            raise AssertionError(f"inverse generator count mismatch at {key}")
        answer[key] = item
    return answer, payload


P207_CONTROLS = {
    source_key_from_parts(64, 48, (-48, 52, 62), (3, 3)): (
        "MOH_P207_POSITIVE",
        (16, 12, (-12, 13), (3,)),
    ),
    source_key_from_parts(84, 56, (-56, 64, 82), (2, 3)): (
        "MOH_P207_POSITIVE",
        (21, 14, (-14, 16), (2,)),
    ),
    source_key_from_parts(84, 56, (-56, 72, 82), (5, 3)): (
        "MOH_P207_POSITIVE",
        (21, 14, (-14, 18), (5,)),
    ),
    source_key_from_parts(75, 50, (-50, 55, 73), (3, 4)): (
        "MOH_P207_POSITIVE",
        (15, 10, (-10, 11), (3,)),
    ),
    source_key_from_parts(75, 50, (-50, 55, 73), (2, 4)): (
        "MOH_P207_POSITIVE",
        (15, 10, (-10, 11), (2,)),
    ),
}

CONTROL_9966 = source_key_from_parts(99, 66, (-66, 77, 97), (8, 8))
RESONANCE_FIX_ROW = source_key_from_parts(
    168, 112, (-112, 140, 160, 166), (3, 21, 3)
)

NEGATIVE_CONTROLS = {
    source_key_from_parts(96, 72, (-72, 36, 78, 94), (1, 1, 5)),
    source_key_from_parts(96, 72, (-72, 36, 78, 94), (1, 3, 5)),
    source_key_from_parts(96, 72, (-72, 36, 78, 94), (4, 3, 5)),
    source_key_from_parts(90, 60, (-60, 10, 45, 88), (1, 8, 4)),
    source_key_from_parts(90, 60, (-60, 10, 45, 88), (3, 8, 4)),
    source_key_from_parts(96, 64, (-64, 48, 68, 94), (1, 2, 3)),
    source_key_from_parts(96, 64, (-64, 48, 68, 94), (2, 1, 3)),
    source_key_from_parts(96, 64, (-64, 48, 68, 94), (3, 2, 3)),
    source_key_from_parts(96, 64, (-64, -48, -8, 20, 94), (1, 1, 6, 3)),
    source_key_from_parts(96, 72, (-72, 36, 80, 94), (1, 9, 3)),
    source_key_from_parts(96, 72, (-72, 36, 80, 94), (4, 9, 3)),
    source_key_from_parts(96, 72, (-72, -60, 56, 94), (1, 9, 3)),
}


def validate_own_sweep(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if len(rows) != 1420:
        raise AssertionError(f"expected 1420 operative rows, got {len(rows)}")
    keyed: dict[tuple[int, int, tuple[int, ...], tuple[int, ...]], dict[str, Any]] = {}
    for row in rows:
        key = source_key(row["own"])
        if key in keyed:
            raise AssertionError(f"duplicate source configuration {key}")
        keyed[key] = row

    live = [row for row in rows if row["own"].get("V_vectors")]
    empty = [row for row in rows if not row["own"].get("V_vectors")]
    if (len(empty), len(live)) != (1354, 66):
        raise AssertionError(f"expected 1354/66 empty/singleton, got {len(empty)}/{len(live)}")
    if any(len(row["own"]["V_vectors"]) != 1 for row in live):
        raise AssertionError("every residual own-data set must be a singleton")
    if Counter(row["own"]["us"] == 1 for row in live) != {True: 46, False: 20}:
        raise AssertionError("expected 46 u_s=1 and 20 u_s>1 singleton rows")

    for key, (_, expected) in P207_CONTROLS.items():
        row = keyed.get(key)
        if row is None or not row["own"]["V_vectors"]:
            raise AssertionError(f"Moh p.207 positive control missing/nonempty failure: {key}")
        own = row["own"]
        got = (
            int(own["n"]),
            int(own["m"]),
            tuple(map(int, indexed_list(own["M"], 1, int(own["s"])))),
            tuple(map(int, own["V_vectors"][0])),
        )
        if got != expected:
            raise AssertionError(f"Moh p.207 child mismatch at {key}: {got} != {expected}")

    row_9966 = keyed.get(CONTROL_9966)
    if row_9966 is None or not row_9966["own"]["V_vectors"]:
        raise AssertionError("(99,66) positive control is not a retained singleton")
    own_9966 = row_9966["own"]
    got_9966 = (
        int(own_9966["n"]),
        int(own_9966["m"]),
        tuple(map(int, indexed_list(own_9966["M"], 1, int(own_9966["s"])))),
        tuple(map(int, own_9966["V_vectors"][0])),
    )
    if got_9966 != (27, 18, (-18, 21), (8,)):
        raise AssertionError(f"(99,66) child-prefix mismatch: {got_9966}")

    negative_states: Counter[str] = Counter()
    for key in NEGATIVE_CONTROLS:
        row = keyed.get(key)
        if row is None:
            raise AssertionError(f"negative control absent from operative sweep: {key}")
        if row["own"].get("V_vectors"):
            raise AssertionError(f"Moh <=100 negative control became nonempty: {key}")
        if row["own"].get("route_state") not in {
            "EMPTY_NECESSARY_FIRST_SUPPORT",
            "EMPTY_NECESSARY_WHOLE_SOURCE_TREE",
        }:
            raise AssertionError(f"unexpected negative-control route state at {key}")
        negative_states[row["own"]["route_state"]] += 1
    if negative_states != {
        "EMPTY_NECESSARY_FIRST_SUPPORT": 9,
        "EMPTY_NECESSARY_WHOLE_SOURCE_TREE": 3,
    }:
        raise AssertionError(f"negative-control state counts drifted: {negative_states}")

    fixed = keyed.get(RESONANCE_FIX_ROW)
    if fixed is None or not fixed["own"].get("V_vectors"):
        raise AssertionError("the corrected (168,112) resonance row is not nonempty")
    fixed_own = fixed["own"]
    fixed_child = (
        int(fixed_own["n"]),
        int(fixed_own["m"]),
        tuple(map(int, indexed_list(fixed_own["M"], 1, int(fixed_own["s"])))),
        tuple(map(int, indexed_list(fixed_own["d"], 1, int(fixed_own["s"]) + 1))),
        tuple(map(int, fixed_own["V_vectors"][0])),
    )
    expected_fixed = (42, 28, (-28, 35, 40), (42, 14, 7, 1), (3, 7))
    if fixed_child != expected_fixed:
        raise AssertionError(f"corrected resonance child mismatch: {fixed_child}")
    markers = collect_values(fixed_own.get("routes", []), "resonance_filter")
    if not markers or set(markers) != {"exact-p-not-q-power"}:
        raise AssertionError(f"corrected route lacks exact resonance marker: {markers}")

    low = {source_key(row["own"]) for row in live if int(row["own"]["source"]["n"]) <= 100}
    expected_low = set(P207_CONTROLS) | {CONTROL_9966}
    if low != expected_low:
        raise AssertionError(f"n<=100 residual mismatch: {low ^ expected_low}")
    high = [row for row in live if int(row["own"]["source"]["n"]) > 100]
    if len(high) != 60 or not all(100 < int(r["own"]["source"]["n"]) <= 200 for r in high):
        raise AssertionError("expected exactly 60 residual rows with 100<n<=200")
    return live


def compact_leaf(item: Mapping[str, Any]) -> dict[str, Any]:
    leaf = {
        "type": "ES_NECESSARY_LEAF_NOT_ATTAINMENT",
        "rho": item["rho"],
        "lambda": list(item["partition"]),
        "Q": int(item["Q"]),
        "t": item["t"],
        "k": item["k"],
        "galois_zero_choices": item["galois_zero_choices"],
        "optimal_low_multiplicities": item["optimal_low_multiplicities"],
        "forced_high_multiplicities": item["forced_high_multiplicities"],
    }
    return leaf


def split_record(own: Mapping[str, Any]) -> dict[str, Any]:
    us = int(own["us"])
    if us == 1:
        return {
            "applies": False,
            "status": "NOT_APPLICABLE_U_S_EQ_1",
            "reason": "D1: a degree-one principal minor has no genuine split partition",
            "scope": "source split classification; no attainment assertion",
        }

    result = screen_skeleton(own["source"])
    skeleton = result["skeleton"]
    if (int(skeleton["u_s"]), int(skeleton["v_s"])) != (us, int(own["vs"])):
        raise AssertionError("split-window/source-own profile mismatch")
    leaves = [compact_leaf(item) for item in result["survivors"]]
    if len(leaves) != int(result["survivor_count"]):
        raise AssertionError("split-window survivor-count mismatch")
    for leaf in leaves:
        rho = Fraction(str(leaf["rho"]))
        if sum(leaf["lambda"]) != us:
            raise AssertionError("ES partition does not sum to u_s")
        if not (1 < rho < Fraction(int(own["vs"]), us)):
            raise AssertionError("ES radius is outside the strict split window")
        if rho.denominator != leaf["Q"] or leaf["Q"] > us:
            raise AssertionError("ES radius denominator certificate mismatch")
    forced = not leaves
    return {
        "applies": True,
        "screen_schema": result["schema"],
        "status": "DESCENT_FORCED_D2" if forced else "TYPED_ES_LEAVES_PLUS_D2_BRANCH",
        "descent_forced": forced,
        "D2_branch": "FORCED" if forced else "REMAINS_AS_ALTERNATIVE",
        "finite_window_predicate": result["finite_window"]["predicate"],
        "orders": result["finite_window"]["orders"],
        "raw_pair_count": result["finite_window"]["raw_pair_count"],
        "killed_count": result["killed_count"],
        "leaf_count": len(leaves),
        "leaves": leaves,
        "scope": result["scope"],
    }


def descent_record(own: Mapping[str, Any], split: Mapping[str, Any]) -> dict[str, Any]:
    if int(own["us"]) == 1:
        if own["descent_license"] != "DETERMINED_PROP6.4":
            raise AssertionError("u_s=1 row lacks its Prop. 6.4 licence")
        if own["characteristic_scope"] != "effective complete chain":
            raise AssertionError("u_s=1 child must be an effective complete chain")
        return {
            "route": "D1",
            "status": "LICENSED_AND_FORCED",
            "forced": True,
            "license": "Moh Proposition 6.4 supplies the radius; Proposition 6.3 supplies descent",
            "child_data_scope": "EFFECTIVE_COMPLETE_CHAIN",
            "prefix_only": False,
            "dependencies": [],
        }

    if own["descent_license"] != "CONDITIONAL_PROP6.3_RADIUS":
        raise AssertionError("u_s>1 row unexpectedly claims an unconditional radius")
    if own["characteristic_scope"] != "retained prefix only":
        raise AssertionError("u_s>1 child must remain prefix-only")
    if own["top_license"] != "OPEN_CHILD_TERMINAL_IDENTIFICATION":
        raise AssertionError("u_s>1 prefix silently acquired a terminal label")
    return {
        "route": "D2",
        "status": (
            "CONDITIONAL_FORCED_PREFIX" if split["descent_forced"]
            else "CONDITIONAL_PREFIX; D2_NOT_FORCED_BECAUSE_ES_LEAVES_REMAIN"
        ),
        "forced": bool(split["descent_forced"]),
        "license": own["descent_license"],
        "child_data_scope": "RETAINED_PREFIX_ONLY_NOT_A_PROVED_TERMINAL_CHAIN",
        "prefix_only": True,
        "dependencies": [PROP_RADIUS_OPEN, CHILD_TERMINAL_OPEN],
    }


def controls_record(key: tuple[int, int, tuple[int, ...], tuple[int, ...]]) -> dict[str, Any]:
    tags: list[str] = []
    if key in P207_CONTROLS:
        tags.append("MOH_P207_POSITIVE")
    if key == CONTROL_9966:
        tags.append("MOH_P202_9966_POSITIVE")
    if key == RESONANCE_FIX_ROW:
        tags.append("RESONANCE_FILTER_FIX_DELTA_ROW")
    return {
        "tags": tags,
        "n_le_100_positive_control": key in set(P207_CONTROLS) | {CONTROL_9966},
        "necessary_configuration_not_pair": True,
    }


def make_roster_row(
    raw: Mapping[str, Any], chart: Mapping[str, Any]
) -> dict[str, Any]:
    own = raw["own"]
    source = own["source"]
    source_s = int(source["s"])
    s_prime = int(own["s"])
    key = source_key(own)
    split = split_record(own)
    descent = descent_record(own, split)
    child_M = indexed_list(own["M"], 1, s_prime)
    child_d = indexed_list(own["d"], 1, s_prime + 1)
    own_V = list(own["V_vectors"][0])
    radius = own["child_radii"][0]
    delta_prime = indexed_list(radius["delta"], 1, s_prime)
    if int(child_M[0]) != -int(own["m"]):
        raise AssertionError(f"root-replacement normalization M'_1=-m' failed at {key}")
    if int(child_M[-1]) > int(own["n"]) - 2:
        raise AssertionError(f"retained terminal label exceeds n'-2 at {key}")
    if Fraction(str(delta_prime[-1])) != -Fraction(str(chart["d"])):
        raise AssertionError(f"terminal radius/chart d mismatch at {key}")
    if len(own_V) != max(0, s_prime - 1):
        raise AssertionError(f"own V' length mismatch at {key}")
    if len(child_M) != s_prime or len(child_d) != s_prime + 1:
        raise AssertionError(f"child chain length mismatch at {key}")
    if int(own["us"]) == 1 and int(child_d[-1]) != 1:
        raise AssertionError(f"complete u_s=1 child does not close at gcd 1: {key}")
    if int(own["us"]) > 1 and int(child_d[-1]) != int(own["us"]):
        raise AssertionError(f"retained prefix gcd is not u_s: {key}")

    chart_copy = deepcopy(chart)
    chart_copy.update(
        {
            "support_theorem": "17(fffffff) G_i-only source receiver",
            "size_sort_field": "unknowns_without_T",
            "unknown_count_convention": (
                "coefficient coordinates plus c; excludes structural x,y and excludes T"
            ),
            "size_is_not_difficulty_proof": True,
            "coverage_status": (
                "PROVED_RECEIVER_FOR_COMPLETE_CHILD_CHAIN"
                if int(own["us"]) == 1
                else "CONDITIONAL_ON_RETAINED_LAST_LABEL_BEING_ACTUAL_EFFECTIVE_TERMINAL"
            ),
            "V_independence_scope": (
                "same G_i for V-labelled fibres at fixed (n',m',M'_last,ell); "
                "m' fixes K=gcd(n',m')"
            ),
            "task_shorthand_key": {
                "n_prime": int(own["n"]),
                "M_terminal_prime": int(child_M[-1]),
                "ell": int(own["ell"]),
                "fixed_degree_context_m_prime": int(own["m"]),
            },
        }
    )

    return {
        "schema": SCHEMA,
        "row_id": None,
        "semantic_type": "NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR",
        "source": {
            "n": int(source["n"]),
            "m": int(source["m"]),
            "M": indexed_list(source["M"], 1, source_s),
            "d": indexed_list(source["d"], 1, source_s + 1),
            # descend_own appends the source convention V_(s+1); it is excluded here.
            "V": indexed_list(source["V"], 2, source_s),
            "s": source_s,
            "u_s": int(own["us"]),
            "v_s": int(own["vs"]),
            "delta": indexed_list(source["delta"], 1, source_s),
        },
        "own_child": {
            "n_prime": int(own["n"]),
            "m_prime": int(own["m"]),
            "M_prime": child_M,
            "d_prime": child_d,
            "V_prime": own_V,
            "s_prime": s_prime,
            "ell": int(own["ell"]),
            "delta_prime": delta_prime,
            "delta_prime_index_order": "delta'_1 through delta'_(s_prime)",
            "first_nonzero_source_index": int(radius["first_nonzero"]),
            "radius_basis": radius["basis"],
            "characteristic_scope": own["characteristic_scope"],
            "descent_license": own["descent_license"],
            "top_license": own["top_license"],
        },
        "descent": descent,
        "receiver_chart": chart_copy,
        "split_window": split,
        "controls": controls_record(key),
        "provenance": {
            "own_schema": own["schema"],
            "historical_frozen_class_id": raw["frozen_class_id"],
            "historical_frozen_tier": raw["frozen_tier"],
            "own_route_state": own["route_state"],
        },
    }


def roster_sort_key(row: Mapping[str, Any]) -> tuple[Any, ...]:
    source = row["source"]
    chart = row["receiver_chart"]
    return (
        chart["unknowns_without_T"],
        chart["coefficient_generators"],
        source["n"],
        source["m"],
        tuple(source["M"]),
        tuple(source["V"]),
    )


def vector(values: Iterable[Any]) -> str:
    return "(" + ",".join(map(str, values)) + ")"


def source_label(key: tuple[int, int, tuple[int, ...], tuple[int, ...]]) -> str:
    n, m, M, V = key
    return f"({n},{m}); M={vector(M)}; V={vector(V)}"


def split_label(value: Mapping[str, Any]) -> str:
    if not value["applies"]:
        return "D1 / n.a."
    if value["descent_forced"]:
        return "D2 forced"
    leaves = "; ".join(
        f"{leaf['rho']}:{vector(leaf['lambda'])}" for leaf in value["leaves"]
    )
    return f"ES[{leaves}] + D2"


def markdown(rows: list[dict[str, Any]], chart_payload: Mapping[str, Any]) -> str:
    us = Counter(row["source"]["u_s"] == 1 for row in rows)
    low = [row for row in rows if row["source"]["n"] <= 100]
    split_rows = [row for row in rows if row["split_window"]["applies"]]
    forced = sum(row["split_window"]["descent_forced"] for row in split_rows)
    leaf_count = sum(row["split_window"]["leaf_count"] for row in split_rows)
    minimum = rows[0]["receiver_chart"]["unknowns_without_T"]
    cheapest = [row for row in rows if row["receiver_chart"]["unknowns_without_T"] == minimum]
    demo_triggered = minimum <= EXACT_Q_DEMO_THRESHOLD
    cheapest_labels = "; ".join(
        source_label(source_key_from_parts(
            row["source"]["n"],
            row["source"]["m"],
            row["source"]["M"],
            row["source"]["V"],
        ))
        for row in cheapest
    )

    lines = [
        "# Residual-66 attack roster",
        "",
        "This is a roster of **necessary tower configurations, not polynomial pairs**. "
        "An ES leaf survives only a necessary finite screen; it is not attained. "
        "Unknown/generator totals are chart sizes, not proofs of computational difficulty.",
        "",
        "## Mechanical summary",
        "",
        f"- Rows: **{len(rows)}** = **{us[True]}** with `u_s=1` + **{us[False]}** retained prefixes with `u_s>1`.",
        f"- Source degrees: **{len(low)}** rows have `n<=100`; **{len(rows)-len(low)}** have `100<n<=200`.",
        f"- Split screen on the {len(split_rows)} `u_s>1` rows: **{forced}** D2-forced, **{len(split_rows)-forced}** with **{leaf_count}** typed ES leaves plus the D2 branch.",
        f"- Cheapest proved G_i chart size: **{minimum}** unknowns without `T`, on **{len(cheapest)}** roster row(s).",
        f"- Cheapest source row(s): {cheapest_labels}.",
        (
            f"- Exact-Q demonstration trigger: **active** because the minimum is at most "
            f"{EXACT_Q_DEMO_THRESHOLD} unknowns."
            if demo_triggered
            else f"- Exact-Q demonstration trigger: **not active**; {minimum} exceeds the "
            f"{EXACT_Q_DEMO_THRESHOLD}-unknown threshold, so no guided-GB kill is requested."
        ),
        f"- Chart-count input schema: `{chart_payload['schema']}`.",
        "",
        "The chart key is `(n',m',M'_last,ell)`. The three-field shorthand "
        "`(n',M'_last,ell)` is valid only inside a fixed receiver degree pair: "
        "`m'` fixes `K=gcd(n',m')` and can change the chart size.",
        "",
        "## Roster, sorted by G_i unknowns then generators and source",
        "",
        "`U` is unknowns without/with the saturation variable `T`; it includes `c` and excludes structural `x,y`. "
        "`E` is nonzero Jacobian coefficient generators / total after adjoining `T*c-1`. "
        "Each displayed `delta'` is ordered by indices `1..s'`.",
        "",
        "| id | source `(n,m); M; d; V` | `s; (u_s,v_s)` | child `(n',m'); M'; d'; own V'` | `s'; ell; delta'` | descent / scope | receiver key | U | E | split status | controls |",
        "|---|---|---|---|---|---|---|---:|---:|---|---|",
    ]
    for row in rows:
        src, child = row["source"], row["own_child"]
        chart, descent = row["receiver_chart"], row["descent"]
        controls = ", ".join(row["controls"]["tags"]) or "-"
        source_text = (
            f"({src['n']},{src['m']}); M={vector(src['M'])}; "
            f"d={vector(src['d'])}; V={vector(src['V'])}"
        )
        child_text = (
            f"({child['n_prime']},{child['m_prime']}); M'={vector(child['M_prime'])}; "
            f"d'={vector(child['d_prime'])}; V'={vector(child['V_prime'])}"
        )
        receiver = chart["receiver_key"]
        receiver_text = (
            f"({receiver['n_prime']},{receiver['m_prime']},"
            f"{receiver['M_terminal_prime']},{receiver['ell']})"
        )
        lines.append(
            "| " + " | ".join(
                [
                    row["row_id"],
                    source_text,
                    f"{src['s']}; ({src['u_s']},{src['v_s']})",
                    child_text,
                    f"{child['s_prime']}; {child['ell']}; {vector(child['delta_prime'])}",
                    f"{descent['route']} — {descent['status']}",
                    receiver_text,
                    f"{chart['unknowns_without_T']}/{chart['unknowns_with_T']}",
                    f"{chart['coefficient_generators']}/{chart['generators_including_Tc_minus_1']}",
                    split_label(row["split_window"]),
                    controls,
                ]
            ) + " |"
        )

    lines.extend(
        [
            "",
            "## The six `n<=100` controls",
            "",
            "The first five are Moh's printed p.207 descendants. `(99,66)` is the additional printed-data control; its child is a conditional retained prefix, not a p.207 descendant.",
            "",
            "| source configuration | child own data | role |",
            "|---|---|---|",
        ]
    )
    for row in sorted(low, key=lambda r: (r["source"]["n"], r["source"]["m"], r["source"]["M"], r["source"]["V"])):
        src, child = row["source"], row["own_child"]
        role = ", ".join(row["controls"]["tags"])
        lines.append(
            f"| ({src['n']},{src['m']}); M={vector(src['M'])}; V={vector(src['V'])} "
            f"| ({child['n_prime']},{child['m_prime']}); M'={vector(child['M_prime'])}; "
            f"V'={vector(child['V_prime'])}; delta'={vector(child['delta_prime'])} | {role} |"
        )

    lines.extend(
        [
            "",
            "## Negative controls and typing",
            "",
            "The builder also asserts that all twelve Moh `n<=100` residual fibres remain empty in the patched 1,420-row input: nine have `EMPTY_NECESSARY_FIRST_SUPPORT` and three have `EMPTY_NECESSARY_WHOLE_SOURCE_TREE`. They therefore do not appear in this 66-row roster.",
            "",
            "Every `u_s=1` row has D1 licensed by Proposition 6.4 (then Proposition 6.3 descent). Every `u_s>1` row is kept as retained-prefix data and explicitly carries both `OPEN[PROP6.3-RADIUS-US>1]` and `OPEN[CHILD-TERMINAL-SUPPORT-US>1]`. No last retained prefix label is promoted to an actual child terminal label.",
            "",
            "Machine-readable records, including the full split leaves and exact chart-count certificates, are in `roster.jsonl`.",
            "",
        ]
    )
    return "\n".join(lines)


def atomic_write(path: Path, text: str) -> None:
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--own-rows", type=Path, default=DEFAULT_OWN_ROWS)
    parser.add_argument("--chart-counts", type=Path, default=DEFAULT_CHART_COUNTS)
    parser.add_argument("--jsonl", type=Path, default=DEFAULT_JSONL)
    parser.add_argument("--markdown", type=Path, default=DEFAULT_MARKDOWN)
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()

    all_rows = read_jsonl(args.own_rows)
    residual = validate_own_sweep(all_rows)
    charts, chart_payload = chart_index(args.chart_counts)
    needed = {child_receiver_tuple(row["own"]) for row in residual}
    if set(charts) != needed:
        raise AssertionError(
            f"chart key mismatch: missing={sorted(needed-set(charts))}, "
            f"extra={sorted(set(charts)-needed)}"
        )

    roster = [make_roster_row(row, charts[child_receiver_tuple(row["own"])]) for row in residual]
    roster.sort(key=roster_sort_key)
    for index, row in enumerate(roster, 1):
        row["row_id"] = f"R{index:03d}"

    if len(roster) != 66 or len({source_key_from_parts(
        row["source"]["n"], row["source"]["m"], row["source"]["M"], row["source"]["V"]
    ) for row in roster}) != 66:
        raise AssertionError("roster rows are not 66 distinct source configurations")
    split_rows = [row for row in roster if row["split_window"]["applies"]]
    if len(split_rows) != 20:
        raise AssertionError("expected split-window records for exactly 20 u_s>1 rows")
    if sum(row["split_window"]["descent_forced"] for row in split_rows) != 0:
        raise AssertionError("current residual unexpectedly contains a D2-forced row")
    if sum(row["split_window"]["leaf_count"] for row in split_rows) != 36:
        raise AssertionError("expected exactly 36 typed ES leaves on the 20 prefix rows")
    if Counter(row["split_window"]["leaf_count"] for row in split_rows) != {
        1: 13,
        2: 3,
        3: 1,
        4: 2,
        6: 1,
    }:
        raise AssertionError("residual split-leaf histogram drifted")

    chart_minimum = min(
        row["receiver_chart"]["unknowns_without_T"] for row in roster
    )
    chart_maximum = max(
        row["receiver_chart"]["unknowns_without_T"] for row in roster
    )
    expected_chart_summary = {
        "status": "PASS",
        "residual_rows": 66,
        "distinct_receiver_classes": len(needed),
        "minimum_unknowns_without_T": chart_minimum,
        "maximum_unknowns_without_T": chart_maximum,
        "exact_q_demo_threshold": EXACT_Q_DEMO_THRESHOLD,
        "exact_q_demo_triggered": chart_minimum <= EXACT_Q_DEMO_THRESHOLD,
    }
    for field, expected in expected_chart_summary.items():
        if chart_payload.get(field) != expected:
            raise AssertionError(
                f"chart summary mismatch for {field}: "
                f"{chart_payload.get(field)!r} != {expected!r}"
            )

    jsonl_text = "".join(
        json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n" for row in roster
    )
    markdown_text = markdown(roster, chart_payload)
    if args.check_only:
        if args.jsonl.read_text(encoding="utf-8") != jsonl_text:
            raise AssertionError(f"recorded JSONL differs from regeneration: {args.jsonl}")
        if args.markdown.read_text(encoding="utf-8") != markdown_text:
            raise AssertionError(f"recorded Markdown differs from regeneration: {args.markdown}")
    else:
        args.jsonl.parent.mkdir(parents=True, exist_ok=True)
        args.markdown.parent.mkdir(parents=True, exist_ok=True)
        atomic_write(args.jsonl, jsonl_text)
        atomic_write(args.markdown, markdown_text)

    print(
        json.dumps(
            {
                "status": "PASS",
                "schema": SCHEMA,
                "operative_rows": len(all_rows),
                "empty": len(all_rows) - len(residual),
                "roster_rows": len(roster),
                "u_s_1": sum(row["source"]["u_s"] == 1 for row in roster),
                "u_s_gt_1": len(split_rows),
                "split_descent_forced": sum(
                    row["split_window"]["descent_forced"] for row in split_rows
                ),
                "typed_ES_leaves": sum(row["split_window"]["leaf_count"] for row in split_rows),
                "n_le_100": sum(row["source"]["n"] <= 100 for row in roster),
                "n_gt_100": sum(row["source"]["n"] > 100 for row in roster),
                "unique_receiver_charts": len(needed),
                "minimum_unknowns_without_T": chart_minimum,
                "exact_q_demo_threshold": EXACT_Q_DEMO_THRESHOLD,
                "exact_q_demo_triggered": chart_minimum <= EXACT_Q_DEMO_THRESHOLD,
                "wrote_outputs": not args.check_only,
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
