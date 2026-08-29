#!/usr/bin/env python3
"""Inventory old/new certified-nonroot graphs and pole-entry data exactly."""

from __future__ import annotations

import argparse
from collections import deque
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import sys


def atom(value):
    if isinstance(value, (int, str, bool)) or value is None:
        return value
    if isinstance(value, tuple):
        return [atom(v) for v in value]
    if isinstance(value, list):
        return [atom(v) for v in value]
    if isinstance(value, dict):
        return {str(k): atom(v) for k, v in sorted(value.items(), key=lambda x: str(x[0]))}
    if hasattr(value, "numerator") and hasattr(value, "denominator"):
        return [int(value.numerator), int(value.denominator)]
    if hasattr(value, "__dict__"):
        return {k: atom(v) for k, v in sorted(vars(value).items())}
    return repr(value)


def shape(node, sc):
    return atom(node.shape())


def certified_nonroot_graph(sc, step, entries, depth=7):
    """Traverse only M>=2 children; old blanket-M1 and new root terminals vanish.

    This is precisely the graph which the repair report says is invariant.
    Opens are deliberately outside this invariant because the later cap repair
    adds mandatory opens without changing certified-nonroot transitions.
    """
    ledger = []
    per_entry = []
    for name, _lam, _sanct, entry, budget in entries:
        q = deque([(entry, 0, 0)])
        seen = {repr(shape(entry, sc)): 0}
        edges, iv = set(), set()
        while q:
            node, lam, dep = q.popleft()
            if dep >= depth:
                continue
            for outcome in step(node):
                kind = outcome[0]
                if kind == "TERMINAL_IV":
                    iv.add((repr(shape(node, sc)), lam))
                    continue
                if kind != "CONT":
                    continue
                _, dl, child, _why = outcome
                nl = lam + dl
                if nl > budget or child.M < 2:
                    continue
                edge = (repr(shape(node, sc)), lam, int(dl),
                        repr(shape(child, sc)), nl)
                edges.add(edge)
                key = repr(shape(child, sc))
                if key in seen and seen[key] <= nl:
                    continue
                seen[key] = nl
                q.append((child, nl, dep + 1))
        normalized = {
            "name": name,
            "edges": [list(e) for e in sorted(edges)],
            "iv": [list(v) for v in sorted(iv)],
            "states": len(seen),
        }
        per_entry.append(normalized)
        ledger.extend((name,) + e for e in sorted(edges))
    return {"per_entry": per_entry, "all_edges": [list(e) for e in sorted(ledger)]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    sys.path.insert(0, str(args.source.resolve()))
    import sheet6_campaign as sc
    import hiii_compose as hiii
    import monodromy_td as mono

    entry_inventory = {}
    for td in range(3, 81):
        rows = []
        for tag, raw, status, node in sc.tdu_entry_nodes(td):
            rows.append([tag, atom(raw), status,
                         None if node is None else shape(node, sc)])
        entry_inventory[str(td)] = rows

    pinned = {}
    for td in (3, 4, 5, 6):
        capture = io.StringIO()
        with redirect_stdout(capture):
            rows = hiii.pin_entry_nodes(td)
        pinned[str(td)] = [[tag, lam, bool(sanct), shape(node, sc)]
                           for tag, lam, sanct, node in rows]

    census_rows, census_meta = mono.run_census(full_checks=False)
    mono_rows = [atom(row) for row in census_rows]

    entries = []
    for td in (3, 4, 5, 6):
        for name, lam, sanct, node in sc.entry_nodes(td):
            entries.append((f"td{td}:{name}", lam, sanct, node, td - 2))

    sc.IIB_DERIVED = False
    ordinary = certified_nonroot_graph(sc, sc.step, entries)
    sc.IIB_DERIVED = True
    af2 = certified_nonroot_graph(sc, sc.step, entries)
    sc.IIB_DERIVED = True
    hiii_graph = certified_nonroot_graph(sc, hiii.step_e5, entries)

    root_controls = {"available": hasattr(sc, "dispose_m1")}
    if root_controls["available"]:
        from fractions import Fraction as Fr
        root = sc.Node(Fr(1, 2), 1, 1, 1, 1)
        nonroot = sc.Node(Fr(1, 2), 2, 1, 1, 1)
        root_controls.update({
            "root_unqualified": sc.dispose_m1(root),
            "root_certified_pole": sc.dispose_m1(root, certified_nonroot=True),
            "nonroot_unqualified": sc.dispose_m1(nonroot),
            "nonroot_constructed": sc.dispose_constructed_child(nonroot),
        })

    result = {
        "source": str(args.source.resolve()),
        "tdu_entry_inventory": entry_inventory,
        "pinned_entry_inventory": pinned,
        "monodromy_rows": mono_rows,
        "monodromy_metadata": atom(census_meta),
        "ordinary_nonroot_graph": ordinary,
        "af2_nonroot_graph": af2,
        "hiii_nonroot_graph": hiii_graph,
        "root_controls": root_controls,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "tdu_tds": len(entry_inventory),
        "pinned_rows": sum(len(v) for v in pinned.values()),
        "monodromy_rows": len(mono_rows),
        "ordinary_edges": len(ordinary["all_edges"]),
        "af2_edges": len(af2["all_edges"]),
        "hiii_edges": len(hiii_graph["all_edges"]),
        "root_controls": root_controls,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

