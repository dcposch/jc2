#!/usr/bin/env python3
"""Regression controls for the corrected Prop. 4.6(5) route filter.

This replays the frozen 1,420-row operative enumeration through the current
``descend_own`` implementation.  A surviving row is necessary data, not an
attained polynomial pair.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
DEFAULT_FROZEN = Path("/tmp/jc2-lane.fzVFfW/inputs")
DEFAULT_ENUMERATION = ROOT / "box/child-own-v-20260905/enumerated-source-rows.json"
MOH_SKELETON_SHA256 = "d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2"

sys.path.insert(0, str(ROOT))
sys.dont_write_bytecode = True
from box.lib.descend_own import descend_own  # noqa: E402
from box.lib.own_v_routes import (  # noqa: E402
    OwnVRouteTree,
    is_q_power_pattern as pattern_is_q_power,
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module from {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def source_key(n: int, m: int, Ms, V) -> tuple:
    Ms = tuple(int(value) for value in Ms)
    values = tuple(int(V[i]) for i in range(2, len(Ms) + 2))
    return int(n), int(m), Ms, values


def json_default(value):
    if isinstance(value, Q):
        return value.numerator if value.denominator == 1 else str(value)
    if isinstance(value, Path):
        return str(value)
    raise TypeError(type(value))


def audit_exact_route(node, counts: Counter) -> None:
    """Check the exact resonance predicate on a saved route and its children."""
    if "j" not in node:
        counts["bottom_occurrences"] += 1
        return
    counts["internal_node_occurrences"] += 1
    assert node["resonance_filter"] == "exact-p-not-q-power"
    assert not pattern_is_q_power(
        int(node["P"]), int(node["Q"]), int(node["A"]), int(node["z"]),
        tuple(map(int, node["orbits"])),
    )
    children = [node.get("selected_child"), node.get("zero_major_child")]
    children.extend(node.get("nonzero_major_children", {}).values())
    for child in children:
        if child is not None:
            audit_exact_route(child, counts)


def make_source(B, n: int, m: int, Ms, values):
    return B.Skel(n, m, list(Ms),
                  {i + 2: int(value) for i, value in enumerate(values)})


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--frozen-dir", type=Path, default=DEFAULT_FROZEN)
    parser.add_argument("--enumeration", type=Path, default=DEFAULT_ENUMERATION)
    parser.add_argument("--output", type=Path, default=HERE / "controls.json")
    args = parser.parse_args()

    moh_path = args.frozen_dir / "moh_skeleton_full.py"
    moh_hash = sha256(moh_path)
    assert moh_hash == MOH_SKELETON_SHA256
    B = load_module("residual66_frozen_moh_skeleton", moh_path)

    enumeration = json.loads(args.enumeration.read_text())
    assert enumeration["census_count"] == 24063
    assert enumeration["operative_count"] == 1420
    assert enumeration["enumerator_sha256"] == moh_hash
    assert len(enumeration["rows"]) == 1420

    indexed = {}
    records = []
    for row in enumeration["rows"]:
        values = {int(i): int(value) for i, value in row["V"].items()}
        key = source_key(row["n"], row["m"], row["Ms"], values)
        assert key not in indexed
        source = B.Skel(row["n"], row["m"], row["Ms"], values)
        child = descend_own(source)
        assert len(child["V_vectors"]) <= 1
        record = {"row": row, "source": source, "child": child}
        indexed[key] = record
        records.append(record)
    assert len(indexed) == 1420

    route_audit = Counter()
    for record in records:
        for route in record["child"]["full_source_routes"]:
            route_audit["root_witnesses"] += 1
            audit_exact_route(route["source_tree_witness"], route_audit)
    assert route_audit["root_witnesses"] == 91

    size_counts = Counter(len(record["child"]["V_vectors"])
                          for record in records)
    assert size_counts == Counter({0: 1354, 1: 66})
    survivors = [record for record in records
                 if record["child"]["V_vectors"]]
    patched_survivor_keys = {
        source_key(record["row"]["n"], record["row"]["m"],
                   record["row"]["Ms"],
                   {int(i): int(value)
                    for i, value in record["row"]["V"].items()})
        for record in survivors
    }
    survivor_us = Counter(record["child"]["us"] for record in survivors)
    assert survivor_us[1] == 46
    assert sum(count for us, count in survivor_us.items() if us > 1) == 20

    # Replay the historical per-factor predicate without changing descend_own:
    # its outer first-support alternatives precede the source-tree filter.
    legacy_size_counts = Counter()
    legacy_survivor_keys = set()
    for record in records:
        child = record["child"]
        legacy = OwnVRouteTree(record["source"], legacy_resonance_filter=True)
        kept = [choice for choice in child["outer_routes"]
                if legacy.compatible_first_support(choice["first_nonzero"])
                is not None]
        if child["licensed_obstructions"]:
            kept = []
        vectors = {tuple(choice["V"][i]
                         for i in range(2, child["s"] + 1))
                   for choice in kept}
        assert len(vectors) <= 1
        legacy_size_counts[len(vectors)] += 1
        if vectors:
            legacy_survivor_keys.add(source_key(
                record["row"]["n"], record["row"]["m"],
                record["row"]["Ms"],
                {int(i): int(value)
                 for i, value in record["row"]["V"].items()},
            ))
    assert legacy_size_counts == Counter({0: 1355, 1: 65})

    target_key = source_key(168, 112, [140, 160, 166],
                            {2: 3, 3: 21, 4: 3})
    assert patched_survivor_keys - legacy_survivor_keys == {target_key}
    assert not (legacy_survivor_keys - patched_survivor_keys)
    target = indexed[target_key]
    source, child = target["source"], target["child"]
    assert tuple(source.M.values()) == (-112, 140, 160, 166)
    assert (child["n"], child["m"]) == (42, 28)
    assert tuple(child["M"].values()) == (-28, 35, 40)
    assert tuple(child["d"].values()) == (42, 14, 7, 1)
    assert child["V_vectors"] == [(Q(3), Q(7))]
    assert (child["us"], child["vs"], child["ell"]) == (1, 3, 1)
    assert child["route_state"] == "NONEMPTY"
    assert len(child["routes"]) == 1
    route = child["routes"][0]
    assert route["first_nonzero"] == 2
    top = route["source_tree_witness"]
    assert (top["j"], top["delta"], top["A"], top["P"], top["Q"],
            top["z"], top["orbits"], top["mode"]) == (
                3, Q(1, 5), 5, 21, 6, 21, (), "zero")
    level2 = top["selected_child"]
    assert (level2["j"], level2["delta"], level2["A"], level2["P"],
            level2["Q"], level2["z"], level2["orbits"],
            level2["mode"]) == (
                2, Q(3, 10), 10, 42, 21, 2, (3, 1), "nonzero")
    assert level2["selected_child"] == {
        "V2": 3, "delta1": Q(3, 4), "A1": 2, "centre_L": 10}
    assert top["resonance_filter"] == "exact-p-not-q-power"
    assert level2["resonance_filter"] == "exact-p-not-q-power"
    legacy_target = OwnVRouteTree(source, legacy_resonance_filter=True)
    assert [j for j in range(2, source.s)
            if legacy_target.compatible_first_support(j) is not None] == []

    positives = [
        ("p207-64-48", 64, 48, [52, 62], (3, 3), (3,)),
        ("p207-84-56-M2-64", 84, 56, [64, 82], (2, 3), (2,)),
        ("p207-84-56-M2-72", 84, 56, [72, 82], (5, 3), (5,)),
        ("p207-75-50-V2-3", 75, 50, [55, 73], (3, 4), (3,)),
        ("p207-75-50-V2-2", 75, 50, [55, 73], (2, 4), (2,)),
        ("p202-99-66", 99, 66, [77, 97], (8, 8), (8,)),
    ]
    positive_results = []
    positive_keys = set()
    for name, n, m, Ms, values, expected_own_V in positives:
        key = source_key(n, m, Ms, {i + 2: value
                                   for i, value in enumerate(values)})
        positive_keys.add(key)
        result = indexed[key]["child"]
        assert result["route_state"] == "NONEMPTY"
        assert result["V_vectors"] == [tuple(Q(v) for v in expected_own_V)]
        positive_results.append({
            "name": name, "n": n, "m": m, "M": [-m, *Ms],
            "V": list(values), "own_V": list(expected_own_V),
            "us": result["us"],
        })

    negatives = [
        ("6_13/V1_1", 96, 72, [36, 78, 94], (1, 1, 5), "tree"),
        ("6_13/V1_3", 96, 72, [36, 78, 94], (1, 3, 5), "arithmetic"),
        ("6_13/V4_3", 96, 72, [36, 78, 94], (4, 3, 5), "arithmetic"),
        ("2_9/V1_8", 90, 60, [10, 45, 88], (1, 8, 4), "tree"),
        ("2_9/V3_8", 90, 60, [10, 45, 88], (3, 8, 4), "arithmetic"),
        ("12_17/V1_2", 96, 64, [48, 68, 94], (1, 2, 3), "arithmetic"),
        ("12_17/V2_1", 96, 64, [48, 68, 94], (2, 1, 3), "tree"),
        ("12_17/V3_2", 96, 64, [48, 68, 94], (3, 2, 3), "arithmetic"),
        ("m12_m2_5/V1_1_6", 96, 64, [-48, -8, 20, 94],
         (1, 1, 6, 3), "arithmetic"),
        ("9_20/V1_9", 96, 72, [36, 80, 94], (1, 9, 3), "arithmetic"),
        ("9_20/V4_9", 96, 72, [36, 80, 94], (4, 9, 3), "arithmetic"),
        ("m15_14/V1_9", 96, 72, [-60, 56, 94], (1, 9, 3), "arithmetic"),
    ]
    negative_results = []
    negative_kinds = Counter()
    expected_states = {
        "arithmetic": "EMPTY_NECESSARY_FIRST_SUPPORT",
        "tree": "EMPTY_NECESSARY_WHOLE_SOURCE_TREE",
    }
    for name, n, m, Ms, values, kind in negatives:
        key = source_key(n, m, Ms, {i + 2: value
                                   for i, value in enumerate(values)})
        result = indexed[key]["child"]
        assert result["V_vectors"] == []
        assert result["route_state"] == expected_states[kind]
        negative_kinds[kind] += 1
        negative_results.append({
            "name": name, "n": n, "m": m, "M": [-m, *Ms],
            "V": list(values), "kind": kind,
            "route_state": result["route_state"],
        })
    assert negative_kinds == Counter({"arithmetic": 9, "tree": 3})

    low_survivors = {
        source_key(record["row"]["n"], record["row"]["m"],
                   record["row"]["Ms"],
                   {int(i): int(value)
                    for i, value in record["row"]["V"].items()})
        for record in survivors if record["row"]["n"] <= 100
    }
    assert low_survivors == positive_keys
    high_survivors = [record for record in survivors
                      if record["row"]["n"] > 100]
    assert len(low_survivors) == 6
    assert len(high_survivors) == 60
    assert all(100 < record["row"]["n"] <= 200
               for record in high_survivors)

    truth_cases = [
        ("gate-witness-nonpower", 42, 21, 10, 2, (3, 1), False),
        ("same-signature-actual-power", 42, 21, 10, 2, (2, 2), True),
        ("power-without-zero-root", 40, 20, 10, 0, (2, 2), True),
        ("power-with-exponent-one", 21, 21, 10, 1, (1, 1), True),
        ("uniform-but-too-few-roots", 20, 11, 10, 0, (2,), False),
    ]
    truth_results = []
    for name, P, Qdeg, A, z, orbits, expected in truth_cases:
        actual = pattern_is_q_power(P, Qdeg, A, z, orbits)
        assert actual is expected
        truth_results.append({
            "name": name, "P": P, "Q": Qdeg, "A": A, "z": z,
            "orbits": list(orbits), "is_q_power": actual,
        })

    output = {
        "type": "DETERMINED finite necessary-data controls; no attainment claim",
        "inputs": {
            "frozen_dir": args.frozen_dir,
            "moh_skeleton_sha256": moh_hash,
            "enumeration": args.enumeration,
            "enumeration_sha256": sha256(args.enumeration),
            "own_v_routes_sha256": sha256(ROOT / "box/lib/own_v_routes.py"),
        },
        "patched_sweep": {
            "operative_rows": len(records),
            "empty": size_counts[0], "singleton": size_counts[1],
            "singleton_us_eq_1": survivor_us[1],
            "singleton_us_gt_1": sum(count for us, count in survivor_us.items()
                                       if us > 1),
            "route_states": dict(sorted(Counter(
                record["child"]["route_state"] for record in records).items())),
            "exact_route_predicate_audit": dict(sorted(route_audit.items())),
        },
        "legacy_control": {
            "empty": legacy_size_counts[0],
            "singleton": legacy_size_counts[1],
            "target_first_support": [],
            "patched_minus_legacy": [{
                "n": 168, "m": 112, "M": [-112, 140, 160, 166],
                "V": [3, 21, 3],
            }],
            "legacy_minus_patched": [],
        },
        "moved_row": {
            "source": {"n": 168, "m": 112, "M": [-112, 140, 160, 166],
                       "V": [3, 21, 3]},
            "child": {"n": 42, "m": 28, "M": [-28, 35, 40],
                      "d": [42, 14, 7, 1], "own_V": [3, 7],
                      "us": 1, "ell": 1},
            "witness": {
                "top": {"j": 3, "delta": Q(1, 5), "A": 5,
                        "P": 21, "Q": 6, "z": 21, "orbits": []},
                "level2": {"j": 2, "delta": Q(3, 10), "A": 10,
                           "P": 42, "Q": 21, "z": 2,
                           "orbits": [3, 1]},
                "bottom": {"delta1": Q(3, 4), "centre_L": 10,
                           "A1": 2, "V2": 3},
            },
        },
        "positive_controls": positive_results,
        "moh_le_100_negative_fibres": negative_results,
        "n_range": {"survivors_n_le_100": 6,
                    "survivors_100_lt_n_le_200": 60},
        "predicate_truth_table": truth_results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True,
                                      default=json_default) + "\n")
    print(json.dumps(output, indent=2, sort_keys=True, default=json_default))


if __name__ == "__main__":
    main()
