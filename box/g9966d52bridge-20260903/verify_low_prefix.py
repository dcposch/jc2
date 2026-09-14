#!/usr/bin/env python3
"""Emit a small exact Singular check from a completed low-prefix Q* ledger."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
AMBIENT = 907


def sx(expression: sp.Expr) -> str:
    return str(sp.expand(expression)).replace("**", "^")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cap", type=int, required=True)
    args = parser.parse_args()
    result_path = HERE / f"t2-prefix-s{args.cap}.json"
    result = json.loads(result_path.read_text(encoding="utf-8"))
    if result["rows"]["residual_count"] != 0:
        raise RuntimeError("this verifier requires a zero Q* residue")

    entries = []
    relations = []
    for line in (HERE / f"t2-prefix-s{args.cap}-pivots.jsonl").read_text(encoding="utf-8").splitlines():
        entry = json.loads(line)
        entries.append(entry)
        variable = sp.Symbol(entry["variable"])
        rhs = sp.sympify(entry["rhs"])
        relations.append(sp.expand(variable - rhs))
    assert len(relations) == result["rows"]["Qstar_pivots"]

    c, wrapper = sp.symbols("c Zc")
    active = set().union(*(relation.free_symbols for relation in relations)) | {c}
    inactive = AMBIENT - len(active)
    ring_names = sorted(active, key=str) + [wrapper]
    generators = [sx(relation) for relation in relations] + ["Zc*c-1"]
    script = f"""// Exact Q* low-prefix check reconstructed from the pivot ledger.
// cap={args.cap} ambient={AMBIENT} active_ambient={len(active)} inactive={inactive}
ring R=0,({','.join(map(str, ring_names))}),dp;
ideal I={','.join(generators)};
ideal G=std(I);
print("BEGIN_RESULT");
print("unit_remainder="+string(reduce(1,G)));
print("active_localized_dimension="+string(dim(G)));
print("full_localized_dimension="+string(dim(G)+{inactive}));
ideal I1=I,c-1;
ideal G1=std(I1);
print("c1_full_dimension="+string(dim(G1)+{inactive}));
print("END_RESULT");
ideal Czero=c,Zc*c-1;
ideal Cone=c-1,Zc*c-1;
print("BEGIN_CONTROLS");
print(reduce(1,std(Czero)));
print(reduce(1,std(Cone)));
print("END_CONTROLS");
quit;
"""
    script_path = HERE / f"t2-prefix-s{args.cap}-Q.sing"
    script_path.write_text(script, encoding="utf-8")
    metadata = {
        "type": "EXACT SINGULAR CHECK / LOW T2 PREFIX",
        "status": "EMITTED",
        "cap": args.cap,
        "pivots": len(relations),
        "active_ambient": len(active),
        "inactive_ambient": inactive,
        "script": str(script_path.relative_to(HERE.parents[1])),
        "script_sha256": hashlib.sha256(script_path.read_bytes()).hexdigest(),
    }
    metadata_path = HERE / f"t2-prefix-s{args.cap}-singular.json"
    metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(metadata, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
