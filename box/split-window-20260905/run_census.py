#!/usr/bin/env python3
"""Run box.lib.split_window on the hash-frozen Moh census through n=200."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
LIB = ROOT / "box" / "lib"
sys.path.insert(0, str(LIB))
import split_window as SW  # noqa: E402


DEFAULT_FROZEN = Path("/tmp/jc2-lane.D5nDdq/inputs/moh_skeleton_full.py")
DEFAULT_ATLAS = ROOT / "box" / "recvatlas-20260905" / "cohort" / "inventory.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n")


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("moh_skeleton_full_frozen_split_window", path)
    module = importlib.util.module_from_spec(spec)
    if spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    spec.loader.exec_module(module)
    return module


def compact_profile(result: dict[str, Any], profile_id: str) -> dict[str, Any]:
    finite = result["finite_window"]
    skel = result["skeleton"]
    attribution = Counter("+".join(item["killed_by"]) for item in result["killed"])
    negative_k = sum(
        item["killed_by"] == ["L"] and Fraction(item["k"]) < 0
        for item in result["killed"]
    )
    return {
        "profile_id": profile_id,
        "u_s": skel["u_s"],
        "v_s": skel["v_s"],
        "W": skel["W"],
        "orders": finite["orders"],
        "order_count": finite["order_count"],
        "partition_count": finite["partition_count"],
        "raw_pair_count": finite["raw_pair_count"],
        "galois_admissible_pair_count": finite["galois_admissible_pair_count"],
        "galois_and_xu_pair_count": finite["galois_and_xu_pair_count"],
        "xu_cor_7_5_direct_exclusions_after_G": finite["xu_cor_7_5_direct_exclusions_after_G"],
        "killed_count": result["killed_count"],
        "kill_attribution": dict(sorted(attribution.items())),
        "negative_k_guard_kills_after_G": negative_k,
        "survivor_count": result["survivor_count"],
        "survivors": result["survivors"],
    }


def source_row(view: SW.SkeletonView, result: dict[str, Any], profile_id: str, row_id: int) -> dict[str, Any]:
    finite = result["finite_window"]
    return {
        "row_id": row_id,
        "row_key": repr(view.row_key),
        "n": view.n,
        "m": view.m,
        "s": view.s,
        "M": list(view.M),
        "d": list(view.d),
        "V": {str(i): view.V[i - 2] for i in range(2, view.s + 1)},
        "u_s": view.u,
        "v_s": view.v,
        "mu_s": view.mu_s,
        "W": view.W,
        "profile_id": profile_id,
        "window_count": finite["order_count"],
        "raw_pair_count": finite["raw_pair_count"],
        "galois_admissible_pair_count": finite["galois_admissible_pair_count"],
        "galois_and_xu_pair_count": finite["galois_and_xu_pair_count"],
        "killed_count": result["killed_count"],
        "kill_attribution": dict(sorted(Counter(
            "+".join(item["killed_by"]) for item in result["killed"]
        ).items())),
        "negative_k_guard_kills_after_G": sum(
            item["killed_by"] == ["L"] and Fraction(item["k"]) < 0
            for item in result["killed"]
        ),
        "survivor_count": result["survivor_count"],
        "survivors": result["survivors"],
    }


def calibration_9966(rows_by_key: dict[str, dict[str, Any]]) -> dict[str, Any]:
    selected = [row for row in rows_by_key.values() if row["n"] == 99 and row["m"] == 66]
    s8 = [row for row in selected if row["M"][1] == 77 and row["V"] == {"2": 8, "3": 8}]
    open_five = [row for row in selected if row not in s8]
    return {
        "u_s_ge_2_rows": len(selected),
        "charged_open_five": {
            "row_count": len(open_five),
            "raw_pair_count": sum(row["raw_pair_count"] for row in open_five),
            "killed_count": sum(row["killed_count"] for row in open_five),
            "survivor_count": sum(row["survivor_count"] for row in open_five),
            "pass_66_54_12": (
                len(open_five) == 5
                and sum(row["raw_pair_count"] for row in open_five) == 66
                and sum(row["killed_count"] for row in open_five) == 54
                and sum(row["survivor_count"] for row in open_five) == 12
            ),
        },
        "S8_external_control": {
            "row_count": len(s8),
            "raw_pair_count": sum(row["raw_pair_count"] for row in s8),
            "killed_count": sum(row["killed_count"] for row in s8),
            "survivor_count": sum(row["survivor_count"] for row in s8),
        },
    }


def map_atlas(path: Path, rows_by_key: dict[str, dict[str, Any]]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    if not path.exists():
        return ({"status": "NOT_RUN", "path": str(path)}, [])
    payload = json.loads(path.read_text(encoding="utf-8"))
    mapped = []
    missing = []
    for item in payload["sources"]:
        row_key = item["row_key"]
        row = rows_by_key.get(row_key)
        if row is None:
            missing.append(row_key)
            continue
        mapped.append(
            {
                "atlas_row_key": row_key,
                "complementary_status": item["complementary_source_branch"]["status"],
                "profile_id": row["profile_id"],
                "raw_pair_count": row["raw_pair_count"],
                "galois_admissible_pair_count": row["galois_admissible_pair_count"],
                "galois_and_xu_pair_count": row["galois_and_xu_pair_count"],
                "killed_count": row["killed_count"],
                "kill_attribution": row["kill_attribution"],
                "survivor_count": row["survivor_count"],
                "survivors": row["survivors"],
                "interpretation": "finite necessary leaves; none asserted attained",
            }
        )
    summary = {
        "status": "PASS" if not missing and len(mapped) == 296 else "FAIL",
        "path": str(path),
        "sha256": sha256(path),
        "atlas_source_rows": len(payload["sources"]),
        "mapped_rows": len(mapped),
        "missing_rows": missing,
        "unique_profiles": len({item["profile_id"] for item in mapped}),
        "raw_pair_slots": sum(item["raw_pair_count"] for item in mapped),
        "galois_admissible_slots": sum(item["galois_admissible_pair_count"] for item in mapped),
        "galois_and_xu_slots": sum(item["galois_and_xu_pair_count"] for item in mapped),
        "screen_killed_slots": sum(item["killed_count"] for item in mapped),
        "surviving_necessary_slots": sum(item["survivor_count"] for item in mapped),
        "rows_with_empty_survivor_list": sum(item["survivor_count"] == 0 for item in mapped),
        "survivor_count_histogram": dict(sorted(Counter(
            item["survivor_count"] for item in mapped
        ).items())),
        "kill_attribution": dict(sorted(sum(
            (Counter(item["kill_attribution"]) for item in mapped), Counter()
        ).items())),
    }
    return summary, mapped


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--frozen", type=Path, default=DEFAULT_FROZEN)
    parser.add_argument("--atlas", type=Path, default=DEFAULT_ATLAS)
    parser.add_argument("--n-max", type=int, default=200)
    parser.add_argument("--kmin", type=int, default=2)
    args = parser.parse_args()

    expected_hash = "d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2"
    actual_hash = sha256(args.frozen)
    if actual_hash != expected_hash:
        raise SystemExit(f"frozen skeleton hash mismatch: {actual_hash}")
    moh = load_module(args.frozen)

    profile_cache: dict[tuple[int, int, int], tuple[str, dict[str, Any]]] = {}
    profiles: list[dict[str, Any]] = []
    certificates: list[dict[str, Any]] = []
    rows: list[dict[str, Any]] = []
    total_census = 0
    for n in range(4, args.n_max + 1):
        for m, Ms, V in moh.census(n, Kmin=args.kmin, full=True):
            total_census += 1
            skel = moh.Skel(n, m, list(Ms), V)
            u = skel.d[skel.s] - skel.V[skel.s]
            if u < 2:
                continue
            view = SW.skeleton_view(skel)
            signature = (view.u, view.v, view.W)
            cached = profile_cache.get(signature)
            if cached is None:
                profile_id = f"u{view.u}-v{view.v}-W{view.W}"
                result = SW.screen_view(view)
                profile_cache[signature] = (profile_id, result)
                profiles.append(compact_profile(result, profile_id))
                for killed in result["killed"]:
                    certificates.append({"profile_id": profile_id, **killed})
            else:
                profile_id, result = cached
            rows.append(source_row(view, result, profile_id, len(rows) + 1))

    rows_by_key = {row["row_key"]: row for row in rows}
    if len(rows_by_key) != len(rows):
        raise RuntimeError("row_key collision in frozen census")

    by_u: dict[int, Counter] = defaultdict(Counter)
    by_degree: dict[int, Counter] = defaultdict(Counter)
    partition_lengths = Counter()
    partition_shapes = Counter()
    for row in rows:
        bucket = by_u[row["u_s"]]
        bucket["rows"] += 1
        bucket["raw"] += row["raw_pair_count"]
        bucket["after_G"] += row["galois_admissible_pair_count"]
        bucket["after_G_Xu"] += row["galois_and_xu_pair_count"]
        bucket["killed"] += row["killed_count"]
        bucket["survivors"] += row["survivor_count"]
        degree_bucket = by_degree[row["n"]]
        degree_bucket["rows"] += 1
        degree_bucket["raw"] += row["raw_pair_count"]
        degree_bucket["killed"] += row["killed_count"]
        degree_bucket["survivors"] += row["survivor_count"]
        for leaf in row["survivors"]:
            part = tuple(leaf["partition"])
            partition_lengths[len(part)] += 1
            partition_shapes[str(part)] += 1

    uv_profiles: dict[tuple[int, int], list[dict[str, Any]]] = defaultdict(list)
    for profile in profiles:
        uv_profiles[(profile["u_s"], profile["v_s"])].append(profile)
    w_sensitive = []
    for (u, v), family in sorted(uv_profiles.items()):
        signatures = {
            tuple((leaf["rho"], tuple(leaf["partition"])) for leaf in profile["survivors"])
            for profile in family
        }
        if len(signatures) > 1:
            by_signature: dict[tuple, list[int]] = defaultdict(list)
            for profile in family:
                signature = tuple(
                    (leaf["rho"], tuple(leaf["partition"])) for leaf in profile["survivors"]
                )
                by_signature[signature].append(profile["W"])
            w_sensitive.append(
                {
                    "u_s": u,
                    "v_s": v,
                    "distinct_survivor_lists": len(signatures),
                    "classes": [
                        {
                            "W_values": sorted(values),
                            "survivor_count": len(signature),
                            "survivor_pairs": [[rho, list(part)] for rho, part in signature],
                        }
                        for signature, values in sorted(
                            by_signature.items(), key=lambda item: (len(item[0]), item[0])
                        )
                    ],
                }
            )

    calibration = calibration_9966(rows_by_key)
    if not calibration["charged_open_five"]["pass_66_54_12"]:
        raise RuntimeError(f"(99,66) calibration failed: {calibration}")
    atlas_summary, atlas_rows = map_atlas(args.atlas, rows_by_key)
    if atlas_summary["status"] == "FAIL":
        raise RuntimeError(f"atlas mapping failed: {atlas_summary}")

    summary = {
        "schema": "jc2.split-window-census/v1",
        "scope": {
            "n": f"4..{args.n_max}",
            "Kmin": args.kmin,
            "full": True,
            "meaning": "arithmetic rows satisfying frozen printed conditions (1)-(13); not all-degree census coverage",
        },
        "inputs": {
            "moh_skeleton_full": str(args.frozen),
            "sha256": actual_hash,
        },
        "counts": {
            "all_census_rows": total_census,
            "u_s_ge_2_rows": len(rows),
            "unique_u_v": len(uv_profiles),
            "unique_u_v_W_profiles": len(profiles),
            "raw_pair_slots_per_row_sum": sum(row["raw_pair_count"] for row in rows),
            "galois_admissible_slots_per_row_sum": sum(row["galois_admissible_pair_count"] for row in rows),
            "galois_and_xu_slots_per_row_sum": sum(row["galois_and_xu_pair_count"] for row in rows),
            "killed_slots_per_row_sum": sum(row["killed_count"] for row in rows),
            "surviving_slots_per_row_sum": sum(row["survivor_count"] for row in rows),
            "rows_with_empty_raw_window": sum(row["raw_pair_count"] == 0 for row in rows),
            "rows_with_no_screen_survivors": sum(row["survivor_count"] == 0 for row in rows),
            "negative_k_guard_kills_after_G_per_row_sum": sum(
                row["negative_k_guard_kills_after_G"] for row in rows
            ),
            "rows_using_negative_k_guard": sum(
                row["negative_k_guard_kills_after_G"] > 0 for row in rows
            ),
        },
        "survivor_count_histogram_per_row": dict(sorted(Counter(row["survivor_count"] for row in rows).items())),
        "window_count_histogram_per_row": dict(sorted(Counter(row["window_count"] for row in rows).items())),
        "by_u_s": {str(u): dict(counter) for u, counter in sorted(by_u.items())},
        "by_degree": {str(n): dict(counter) for n, counter in sorted(by_degree.items())},
        "kill_attribution_per_row_sum": dict(sorted(sum(
            (Counter(row["kill_attribution"]) for row in rows), Counter()
        ).items())),
        "surviving_partition_length_histogram_per_row": dict(sorted(partition_lengths.items())),
        "surviving_partition_shape_histogram_per_row": dict(partition_shapes.most_common()),
        "uniformity": {
            "exact_rule": "survivors are exactly the G-and-L feasible pairs and depend only on (u_s,v_s,W)",
            "always_maximal_contact_partitions": False,
            "reason": "the output contains several block counts and partition shapes, including full-distinct and partial partitions",
            "u_v_families_with_W_sensitive_survivor_list": len(w_sensitive),
            "W_sensitive_families": w_sensitive,
            "repair_to_17_iiiiii": "retain W through k=W-t and reject negative low multiplicities",
        },
        "calibration_9966": calibration,
        "atlas_296": atlas_summary,
        "artifacts": {
            "per_row": "census-rows.jsonl",
            "profiles": "profiles.jsonl",
            "kill_certificates": "killed-certificates.jsonl",
            "atlas_map": "atlas-296-map.jsonl",
        },
    }

    profiles.sort(key=lambda row: (row["u_s"], row["v_s"], row["W"]))
    rows.sort(key=lambda row: (row["n"], row["m"], row["M"], sorted(row["V"].items())))
    certificates.sort(key=lambda row: (row["profile_id"], row["rho"], row["partition"]))
    write_jsonl(HERE / "census-rows.jsonl", rows)
    write_jsonl(HERE / "profiles.jsonl", profiles)
    write_jsonl(HERE / "killed-certificates.jsonl", certificates)
    write_jsonl(HERE / "atlas-296-map.jsonl", atlas_rows)
    write_json(HERE / "summary.json", summary)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
