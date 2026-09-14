#!/usr/bin/env python3
"""Printed-closure screen on all 1,420 operative rows.

Reuses CountingClosure / summarize from
box/integrality-table-20260906/integrality_table.py, which itself reuses
box/exact-contact-gate-20260906/{census_replay.py,closure_fixed.py}.
Identities are not rewritten. Only the row source is parametrized.

A configuration is not a polynomial pair. N = 0 is typed
DEAD-mod-[printed fixed-list + D1 residues] and is not promoted.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
import time
from collections import Counter
from fractions import Fraction as F
from math import gcd
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
HERE = Path(__file__).resolve().parent
GATE = ROOT / "box" / "exact-contact-gate-20260906"
IT_PATH = ROOT / "box" / "integrality-table-20260906" / "integrality_table.py"
ENUM_PATH = ROOT / "box" / "child-own-v-20260905" / "enumerated-source-rows.json"
OWN_PATH = ROOT / "box" / "child-own-v-20260905" / "own-rows.jsonl"
FROZEN_JSON = ROOT / "box" / "integrality-table-20260906" / "integrality-table.json"

LANE_CANDIDATES = [
    Path("/tmp/jc2-lane.rMDzWM/inputs"),
    Path("/tmp/jc2-lane.IaL1Mu/inputs"),
    Path("/tmp/jc2-lane.QKyQBy/inputs"),
    Path("/tmp/jc2-lane.e1ztmS/inputs"),
]


def lane_dir() -> Path:
    for p in LANE_CANDIDATES:
        if (p / "roster.jsonl").is_file():
            return p
    residual = ROOT / "box" / "residual66-20260905"
    if (residual / "roster.jsonl").is_file():
        return residual
    raise FileNotFoundError("roster.jsonl")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def load_gate(name: str, path: Path, replacements: list[tuple[str, str]]):
    text = path.read_text()
    for old, new in replacements:
        if old not in text:
            raise RuntimeError(f"{path.name}: replacement anchor not found: {old!r}")
        text = text.replace(old, new)
    spec = importlib.util.spec_from_loader(name, loader=None)
    mod = importlib.util.module_from_spec(spec)
    mod.__file__ = str(path)
    mod.__name__ = name
    sys.modules[name] = mod
    exec(compile(text, str(path), "exec"), mod.__dict__)
    return mod


def load_integrality_table(roster: Path, lane: Path):
    load_gate(
        "census_replay",
        GATE / "census_replay.py",
        [
            (
                "INPUT=Path('/tmp/jc2-lane.QKyQBy/inputs/roster.jsonl')",
                f"INPUT=Path('{roster}')",
            )
        ],
    )
    load_gate(
        "closure_fixed",
        GATE / "closure_fixed.py",
        [
            (
                "ROOT=Path('/tmp/jc2-lane.QKyQBy/inputs')",
                f"ROOT=Path('{lane}')",
            )
        ],
    )
    text = IT_PATH.read_text()
    old = """        Path("/tmp/jc2-lane.IaL1Mu/inputs/roster.jsonl"),
        Path("/tmp/jc2-lane.QKyQBy/inputs/roster.jsonl"),"""
    new = f"""        Path("{roster}"),
        Path("/tmp/jc2-lane.IaL1Mu/inputs/roster.jsonl"),
        Path("/tmp/jc2-lane.QKyQBy/inputs/roster.jsonl"),"""
    if old not in text:
        raise RuntimeError("integrality_table.py roster candidates not found")
    text = text.replace(old, new)
    spec = importlib.util.spec_from_loader("integrality_table", loader=None)
    mod = importlib.util.module_from_spec(spec)
    mod.__file__ = str(IT_PATH)
    mod.__name__ = "integrality_table"
    sys.modules["integrality_table"] = mod
    exec(compile(text, str(IT_PATH), "exec"), mod.__dict__)
    return mod


def qstr(x) -> str:
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else str(x)


def make_source(n: int, m: int, Ms, Vmap) -> dict:
    """Skel/Def 5.1(3) source dict; matches the residual-66 roster on all 66 keys."""
    if isinstance(Vmap, dict):
        keys = sorted(int(k) for k in Vmap)
        Vlist = [int(Vmap[str(i)] if str(i) in Vmap else Vmap[i]) for i in keys]
        s = keys[-1]
        if keys != list(range(2, s + 1)):
            raise ValueError(f"V keys {keys}")
    else:
        Vlist = [int(v) for v in Vmap]
        s = 1 + len(Vlist)
    full = [-int(m)] + [int(x) for x in Ms]
    if len(full) != s:
        raise ValueError(f"M length {len(full)} != s={s}")
    d = [int(n)]
    for M in full:
        d.append(gcd(d[-1], M))
    V = {i + 2: Vlist[i] for i in range(len(Vlist))}
    V[s + 1] = d[s]
    Md = {i + 1: full[i] for i in range(s)}
    dd = {i + 1: d[i] for i in range(len(d))}
    delta = []
    for i in range(1, s + 1):
        num = F(n - Md[i])
        den = F(n - Md[s] - 1)
        for j in range(i + 1, s + 1):
            num *= V[j] * (n - Md[j]) - dd[j]
            den *= V[j] * (n - Md[j - 1]) - dd[j]
        delta.append(qstr(1 - num / den))
    return {
        "n": int(n),
        "m": int(m),
        "s": s,
        "M": full,
        "V": Vlist,
        "d": d,
        "delta": delta,
        "u_s": dd[s] - V[s],
        "v_s": V[s],
    }


def source_key(src: dict) -> tuple:
    return (src["n"], src["m"], tuple(src["M"]), tuple(src["V"]))


def idx(mapping, i):
    if i in mapping:
        return mapping[i]
    return mapping[str(i)]


def own_source_key(own_src: dict) -> tuple:
    s = int(own_src["s"])
    M = [int(idx(own_src["M"], i)) for i in range(1, s + 1)]
    V = [int(idx(own_src["V"], i)) for i in range(2, s + 1)]
    return (int(own_src["n"]), int(own_src["m"]), tuple(M), tuple(V))


def compact_rec(rec: dict, src: dict, extra: dict) -> dict:
    out = {
        "row_id": rec["row_id"],
        "enum_index": extra["enum_index"],
        "n": src["n"],
        "m": src["m"],
        "s": src["s"],
        "M": src["M"],
        "V": src["V"],
        "u_s": src["u_s"],
        "v_s": src["v_s"],
        "n_complete": rec["n_complete"],
        "n_integral": rec["n_integral"],
        "n_IM_ge_Im": rec["n_IM_ge_Im"],
        "n_survive": rec["n_survive"],
        "zero_survivors": rec["zero_survivors"],
        "n_distinct_pairs": rec["n_distinct_pairs"],
        "survivor_pairs": rec["survivor_pairs"],
        "own_bucket": extra["own_bucket"],
        "own_partition": extra["own_partition"],
        "roster": extra["roster"],
    }
    keep_pairs = rec["n_complete"] > 0 and rec["n_distinct_pairs"] <= 16 and (
        extra["roster"]
        or extra["own_bucket"] == "empty"
        or rec["n_survive"] == 0
    )
    if keep_pairs:
        out["pairs"] = rec["pairs"]
        out["minor_base"] = rec["minor_base"]
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--rows",
        choices=("operative", "roster"),
        default="operative",
        help="row source: 1420 operative census or the 66-row roster control",
    )
    args = parser.parse_args()

    lane = lane_dir()
    roster_path = lane / "roster.jsonl"
    it = load_integrality_table(roster_path, lane)

    roster = [json.loads(line) for line in roster_path.read_text().splitlines()]
    assert [r["row_id"] for r in roster] == [f"R{i:03d}" for i in range(1, 67)]
    roster_by_key = {source_key(r["source"]): r for r in roster}
    assert len(roster_by_key) == 66

    frozen = json.loads(FROZEN_JSON.read_text())
    frozen_compact = {r["row_id"]: r for r in frozen["compact"]}

    own_by_key = {}
    with OWN_PATH.open() as fh:
        for line in fh:
            rec = json.loads(line)
            key = own_source_key(rec["own"]["source"])
            vecs = rec["own"].get("V_vectors") or []
            own_by_key[key] = {
                "partition": rec["partition"],
                "bucket": "singleton" if vecs else "empty",
                "n_vectors": len(vecs),
                "route_state": rec["own"].get("route_state"),
            }
    assert len(own_by_key) == 1420
    n_empty = sum(1 for v in own_by_key.values() if v["bucket"] == "empty")
    n_live = sum(1 for v in own_by_key.values() if v["bucket"] == "singleton")
    if (n_empty, n_live) != (1354, 66):
        raise AssertionError(f"own-data partition {n_empty}/{n_live}")
    if set(roster_by_key) != {k for k, v in own_by_key.items() if v["bucket"] == "singleton"}:
        raise AssertionError("roster keys != own-data singletons")

    enum_blob = json.loads(ENUM_PATH.read_text())
    enum_rows = enum_blob["rows"]
    if len(enum_rows) != 1420 or enum_blob.get("operative_count") != 1420:
        raise AssertionError(len(enum_rows))

    if args.rows == "roster":
        work = [
            {
                "enum_index": None,
                "row_id": r["row_id"],
                "source": r["source"],
                "roster": True,
            }
            for r in roster
        ]
    else:
        work = []
        seen = set()
        for i, raw in enumerate(enum_rows):
            src = make_source(raw["n"], raw["m"], raw["Ms"], raw["V"])
            key = source_key(src)
            if key in seen:
                raise AssertionError(f"duplicate enumerated key {key}")
            seen.add(key)
            ros = roster_by_key.get(key)
            work.append(
                {
                    "enum_index": i,
                    "row_id": ros["row_id"] if ros else f"E{i:04d}",
                    "source": src if not ros else ros["source"],
                    "roster": ros is not None,
                    "key": key,
                }
            )
        if len(seen) != 1420:
            raise AssertionError(len(seen))
        if sum(1 for w in work if w["roster"]) != 66:
            raise AssertionError("roster overlay")

    started = time.perf_counter()
    table = []
    for item in work:
        src = item["source"]
        key = source_key(src)
        own = own_by_key[key]
        C = it.CountingClosure(src)
        minor_base, counter = C.run_counted()
        rec = it.summarize(counter)
        rec.update(
            {
                "row_id": item["row_id"],
                "n": src["n"],
                "m": src["m"],
                "s": src["s"],
                "minor_base": str(minor_base),
                "finite_major_levels": src["s"] - 1,
            }
        )
        rec["zero_survivors"] = rec["n_survive"] == 0
        extra = {
            "enum_index": item["enum_index"],
            "own_bucket": own["bucket"],
            "own_partition": own["partition"],
            "roster": item["roster"],
        }
        table.append((compact_rec(rec, src, extra), rec, src, extra, own))
    elapsed = time.perf_counter() - started

    # Frozen 66-row control: every roster overlay must match the banked table.
    control_mismatches = []
    roster_hits = [t for t in table if t[3]["roster"]]
    if args.rows == "operative" and len(roster_hits) != 66:
        raise AssertionError(len(roster_hits))
    for compact, rec, src, extra, own in table:
        if not extra["roster"]:
            continue
        rid = rec["row_id"]
        fr = frozen_compact[rid]
        for field in (
            "n_complete",
            "n_integral",
            "n_IM_ge_Im",
            "n_survive",
            "zero_survivors",
            "n_distinct_pairs",
            "survivor_pairs",
        ):
            if rec[field] != fr[field]:
                control_mismatches.append(
                    {"row_id": rid, "field": field, "got": rec[field], "frozen": fr[field]}
                )
    if control_mismatches:
        raise AssertionError(control_mismatches)

    n0 = [t[0] for t in table if t[0]["n_complete"] == 0]
    zsv = [t[0] for t in table if t[0]["n_survive"] == 0]
    n0_ids = [r["row_id"] for r in n0]
    zsv_ids = [r["row_id"] for r in zsv]

    singleton = [t[0] for t in table if t[0]["own_bucket"] == "singleton"]
    empty = [t[0] for t in table if t[0]["own_bucket"] == "empty"]
    singleton_n0 = [r for r in singleton if r["n_complete"] == 0]
    singleton_zsv = [r for r in singleton if r["n_survive"] == 0]
    empty_n_gt0 = [r for r in empty if r["n_complete"] > 0]
    empty_zsv_but_complete = [
        r for r in empty if r["n_complete"] > 0 and r["n_survive"] == 0
    ]

    def brief(rows):
        out = []
        for r in rows:
            item = {
                "row_id": r["row_id"],
                "enum_index": r["enum_index"],
                "n": r["n"],
                "m": r["m"],
                "s": r["s"],
                "M": r["M"],
                "V": r["V"],
                "u_s": r["u_s"],
                "v_s": r["v_s"],
                "n_complete": r["n_complete"],
                "n_integral": r["n_integral"],
                "n_IM_ge_Im": r["n_IM_ge_Im"],
                "n_survive": r["n_survive"],
                "own_bucket": r["own_bucket"],
                "own_partition": r["own_partition"],
                "survivor_pairs": r["survivor_pairs"],
            }
            if "pairs" in r:
                item["pairs"] = r["pairs"]
            out.append(item)
        return out

    s_dist = Counter(t[0]["s"] for t in table)
    N_hist = Counter(t[0]["n_complete"] for t in table)
    own_part_n0 = Counter(r["own_partition"] for r in n0)
    own_part_ngt0 = Counter(
        t[0]["own_partition"] for t in table if t[0]["n_complete"] > 0
    )

    payload = {
        "schema": "jc2.printed-closure-screen/v1",
        "calculus": "box/integrality-table-20260906/integrality_table.py CountingClosure; box/exact-contact-gate-20260906/{census_replay.py,closure_fixed.py}",
        "printed": {
            "I_def": "Xu §2: I(f_xi,g)=deg_x Res_y(f_xi,g) in Z",
            "Thm_5_1": "Xu p.7: I(f_xi,g)=I_M for a Jacobian pair",
            "Cor_5_3": "I_M >= I_m (unsplit minor is a floor)",
            "closure": "Moh Def 5.1(4) p.179; Prop 5.3 p.180; D1 final by Prop 4.6 p.170",
        },
        "fallacy_v2": "A missing configuration is not a pair. N=0 is a kill only if the printed closure is a proved necessity — leave that to the gate. Typed DEAD-mod-[printed fixed-list + D1 residues], not promoted.",
        "row_source": args.rows,
        "custody": {
            "lane": str(lane),
            "roster_sha256": sha256_file(roster_path),
            "enumerated_source_rows_sha256": sha256_file(ENUM_PATH),
            "own_rows_sha256": sha256_file(OWN_PATH),
            "integrality_table_py_sha256": sha256_file(IT_PATH),
            "census_replay_sha256": sha256_file(GATE / "census_replay.py"),
            "closure_fixed_sha256": sha256_file(GATE / "closure_fixed.py"),
            "frozen_table_json_sha256": sha256_file(FROZEN_JSON),
        },
        "control": {
            "roster_rows": len(roster_hits),
            "frozen_table_match": not control_mismatches,
            "mismatches": control_mismatches,
            "R063_N": next(r["n_complete"] for r in singleton if r["row_id"] == "R063")
            if any(r["row_id"] == "R063" for r in singleton)
            else None,
            "R001_N": next(r["n_complete"] for r in singleton if r["row_id"] == "R001")
            if any(r["row_id"] == "R001" for r in singleton)
            else None,
            "R009_R050": {
                r["row_id"]: {
                    "n_complete": r["n_complete"],
                    "n_survive": r["n_survive"],
                    "survivor_pairs": r["survivor_pairs"],
                }
                for r in singleton
                if r["row_id"] in ("R009", "R050")
            },
        },
        "elapsed_seconds": round(elapsed, 6),
        "totals": {
            "rows": len(table),
            "complete_configurations": sum(t[0]["n_complete"] for t in table),
            "integral_configurations": sum(t[0]["n_integral"] for t in table),
            "IM_ge_Im_configurations": sum(t[0]["n_IM_ge_Im"] for t in table),
            "surviving_configurations": sum(t[0]["n_survive"] for t in table),
            "rows_with_N_gt_0": sum(1 for t in table if t[0]["n_complete"] > 0),
            "rows_with_N_eq_0": len(n0),
            "rows_with_a_survivor": sum(1 for t in table if t[0]["n_survive"] > 0),
            "rows_with_zero_survivors": len(zsv),
            "s_dist": {str(k): s_dist[k] for k in sorted(s_dist)},
            "N_histogram": {str(k): N_hist[k] for k in sorted(N_hist)},
        },
        "cross_tab": {
            "own_empty": 1354,
            "own_singleton": 66,
            "singleton_N_eq_0": len(singleton_n0),
            "singleton_N_eq_0_ids": [r["row_id"] for r in singleton_n0],
            "singleton_zero_survivors": len(singleton_zsv),
            "singleton_zero_survivors_ids": [r["row_id"] for r in singleton_zsv],
            "empty_N_gt_0": len(empty_n_gt0),
            "empty_N_eq_0": sum(1 for r in empty if r["n_complete"] == 0),
            "empty_zero_survivors": sum(1 for r in empty if r["n_survive"] == 0),
            "empty_complete_but_zero_survivors": len(empty_zsv_but_complete),
            "N0_by_own_partition": dict(own_part_n0),
            "Ngt0_by_own_partition": dict(own_part_ngt0),
        },
        "N0_row_ids": n0_ids,
        "zero_survivor_ids": zsv_ids,
        "N0_rows_interesting": brief(singleton_n0),
        "zero_survivor_rows_with_N_gt_0": brief(
            [r for r in zsv if r["n_complete"] > 0]
        ),
        "empty_own_with_N_gt_0": brief(empty_n_gt0),
        "singleton_N0": brief(singleton_n0),
        "singleton_zero_survivors": brief(singleton_zsv),
        "rows": [t[0] for t in table],
    }

    out_path = HERE / "printed-closure-screen.json"
    out_path.write_text(json.dumps(payload, separators=(",", ":")) + "\n")
    summary = {
        "json_bytes": out_path.stat().st_size,
        "elapsed_seconds": payload["elapsed_seconds"],
        "totals": payload["totals"],
        "control": payload["control"],
        "cross_tab": {
            k: payload["cross_tab"][k]
            for k in payload["cross_tab"]
            if k
            not in (
                "N0_by_own_partition",
                "Ngt0_by_own_partition",
            )
        }
        | {
            "N0_by_own_partition": payload["cross_tab"]["N0_by_own_partition"],
            "Ngt0_by_own_partition": payload["cross_tab"]["Ngt0_by_own_partition"],
        },
        "singleton_N0": payload["cross_tab"]["singleton_N_eq_0_ids"],
        "singleton_zero_survivors": payload["cross_tab"]["singleton_zero_survivors_ids"],
        "empty_N_gt_0_ids": [r["row_id"] for r in empty_n_gt0],
        "N0_count": len(n0_ids),
        "zero_survivor_count": len(zsv_ids),
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
