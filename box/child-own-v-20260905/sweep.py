#!/usr/bin/env python3
"""Fresh frozen-enumerator replay and typed own-child descent of every row."""
import argparse
import hashlib
import importlib.util
import json
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
FROZEN = Path("/tmp/jc2-lane.wwyG4k/inputs")
sys.path.insert(0, str(ROOT))
sys.dont_write_bytecode = True
from box.lib.descend_own import descend_own


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def default(value):
    if isinstance(value, Fraction):
        return value.numerator if value.denominator == 1 else str(value)
    if isinstance(value, Path):
        return str(value)
    raise TypeError(type(value))


def dump(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2, default=default,
                                      sort_keys=True) + "\n")


def key(n, m, M, V):
    return (n, m, tuple(M), tuple(sorted((int(i), v) for i, v in V.items())))


def compare_value(values, copied):
    values = set(values)
    if not values:
        return "SET-VALUED_EMPTY"
    if len(values) == 1:
        return "DETERMINED_SAME" if values == {copied} else "DETERMINED_DIFFERENT"
    return "SET-VALUED_MIXED" if copied in values else "SET-VALUED_ALL_DIFFERENT"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reuse-enumeration", action="store_true")
    args = parser.parse_args()
    started = time.monotonic()
    B = module("moh_skeleton_full_frozen", FROZEN / "moh_skeleton_full.py")
    treepath = ROOT / "box/centre-gate-20260903/opus5_probe.py"
    T = module("own_v_frozen_operative_tree", treepath)
    assert T.B is B
    if args.reuse_enumeration:
        enum = json.loads((OUT / "enumerated-source-rows.json").read_text())
    else:
        rows, count = [], 0
        for n in range(16, 201):
            for m, M, V in B.census(n, Kmin=2, full=True):
                count += 1
                tree = T.Tree(n, m, M, gate=False, ode=True, capacity=False,
                              passport=False, recenter=True)
                if tree.embeds(V) is not None:
                    rows.append(dict(n=n, m=m, Ms=list(M), V=V))
        assert count == 24063 and len(rows) == 1420
        enum = dict(type="DETERMINED", census_count=count, operative_count=len(rows),
                    rows=rows, enumerator_sha256=hashlib.sha256(
                        (FROZEN / "moh_skeleton_full.py").read_bytes()).hexdigest(),
                    tree_sha256=hashlib.sha256(treepath.read_bytes()).hexdigest())
        dump("enumerated-source-rows.json", enum)
    regenerated = {key(r["n"], r["m"], r["Ms"], r["V"]): r for r in enum["rows"]}
    assert len(regenerated) == 1420
    old = json.loads((ROOT / "box/ctop-gate-20260905/r2-enum-audit.json").read_text())
    previous = {key(r["n"], r["m"], r["Ms"], r["V"]): r for r in old["operative_rows"]}
    inventory = json.loads((ROOT / "box/operative-sweep-20260905/inventory.json").read_text())
    inv = {key(r["n"], r["m"], r["M"], r["V"]): r for r in inventory["rows"]}
    assert regenerated.keys() == previous.keys() == inv.keys()
    hardpath = ROOT / "box/operative-sweep-20260905/hard-rows.jsonl"
    hard = [json.loads(line) for line in hardpath.read_text().splitlines()]
    hardkeys = Counter((r["class_id"], r["parent_n"], r["parent_m"]) for r in hard)
    invkeys = Counter((r["class_id"], r["n"], r["m"]) for r in inv.values())
    assert hardkeys == invkeys and len(hard) == 1420

    levels = defaultdict(Counter)
    rawlevels = defaultdict(Counter)
    locallevels = defaultdict(Counter)
    stages = Counter()
    partition = Counter()
    old_to_new = Counter()
    top = Counter()
    localtop = Counter()
    records = []
    for rowkey, row in regenerated.items():
        source = B.Skel(row["n"], row["m"], row["Ms"],
                        {int(k): v for k, v in row["V"].items()})
        prior = previous[rowkey]
        child = descend_own(source)
        assert list(child["raw_M"].values()) == prior["raw_M"]
        assert list(child["raw_d"].values()) == prior["raw_d"]
        assert (child["n"], child["m"], child["ell"], child["us"], child["dropped"]) == (
            prior["n1"], prior["m1"], prior["ell"], prior["u_s"], bool(prior["drops"]))
        stages[("V_set_size", len(child["V_vectors"]))] += 1
        stages[("outer_V_set_size", len(child["outer_V_vectors"]))] += 1
        stages[("full_source_route_count", len(child["full_source_routes"]))] += 1
        stages[("route_state", child["route_state"])] += 1
        stages[("us", child["us"])] += 1
        stages[("drop", child["dropped"])] += 1
        for i in range(2, child["s"] + 1):
            levels[i][compare_value(child["V"][i]["values"], source.V[i])] += 1
        for i in range(2, child["s_raw"] + 1):
            rawlevels[i][compare_value((v[i - 2] for v in child["raw_V_vectors"]), source.V[i])] += 1
            locallevels[i][compare_value(child["local_V"][i]["values"], source.V[i])] += 1
        uneg = child["u_negative"]["value"]
        # U2 identity is an independent necessary consequence even on empty routes.
        assert uneg == prior["U_NEG"]
        if uneg:
            bucket = "U_NEG_US1" if child["us"] == 1 else "U_NEG_US2_RADIUS_CONDITIONAL"
        elif child["licensed_obstructions"]:
            bucket = "PROP6.3_FINITE_POLE_US1"
        elif not child["V_vectors"]:
            bucket = "EMPTY_NECESSARY_DATA_US1" if child["us"] == 1 else "EMPTY_NECESSARY_DATA_US_GE2"
        else:
            bucket = "OWN_V_CANDIDATES_US1" if child["us"] == 1 else "OWN_V_CANDIDATES_US_GE2"
        partition[bucket] += 1
        old_to_new[(inv[rowkey]["tier"], bucket)] += 1
        tests = {v[child["s"] - 2] <= child["d"][child["s"]]
                 for v in child["V_vectors"]}
        top[(child["top_license"], tuple(sorted(tests)))] += 1
        local_values = child["local_V"][child["s"]]["values"]
        local_tests = tuple(sorted({v <= child["d"][child["s"]] for v in local_values}))
        localtop[(child["us"] == 1, child["dropped"],
                  "DETERMINED_V" if len(local_values) == 1 else "SET-VALUED_V",
                  local_tests)] += 1
        records.append(dict(source_row=row, frozen_class_id=inv[rowkey]["class_id"],
                            frozen_tier=inv[rowkey]["tier"], partition=bucket,
                            own=child))
    with (OUT / "own-rows.jsonl").open("w") as handle:
        for record in records:
            handle.write(json.dumps(record, sort_keys=True, default=default) + "\n")
    summary = dict(
        counts_type="DETERMINED arithmetic on finite necessary sets; no attainment claim",
        operative_rows=len(records), stages={str(k): v for k, v in stages.items()},
        per_effective_level=levels, per_raw_level=rawlevels, per_local_implication_level=locallevels,
        partition=partition, old_to_new={str(k): v for k, v in old_to_new.items()},
        ctop={str(k): v for k, v in top.items()},
        local_top_predicates={str(k): v for k, v in localtop.items()},
        verifications=dict(fresh_enumerator_count=enum["census_count"],
            full_source_rows_match_gate=True, full_source_rows_match_inventory=True,
            hard_rows_multiset_match=True, characteristic_labels_match_every_row=True,
            U2_identity_predicate_matches_legacy_arithmetic=True),
        elapsed_seconds=round(time.monotonic() - started, 3))
    dump("summary.json", summary)
    dump("set-valued-rows.json", [r for r in records if len(r["own"]["V_vectors"]) > 1])
    dump("outer-set-valued-rows.json", [r for r in records if len(r["own"]["outer_V_vectors"]) > 1])
    dump("determined-changed-rows.json", [r for r in records
        if len(r["own"]["V_vectors"]) == 1 and any(
            r["own"]["V_vectors"][0][i - 2] != r["own"]["copied_V"][i]
            for i in range(2, r["own"]["s"] + 1))])
    print(json.dumps(summary, indent=2, default=default))


if __name__ == "__main__":
    main()
