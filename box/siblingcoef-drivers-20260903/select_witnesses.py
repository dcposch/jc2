#!/usr/bin/env python3
"""Reproduce the two rows selected for the sibling-coefficient audit.

The frozen ``candidate-results.json`` contains aggregate degree counts rather
than individual survivor rows.  Therefore the D=108 row is regenerated from
the frozen skeleton and full-tree modules.  Nothing in the frozen input
directory is written.
"""

from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
import sys
from pathlib import Path


INPUTS = Path("/tmp/jc2-lane.XU3OWR/inputs")
EXPECTED = {
    "full-tree-ode-excess-witnesses.json":
        "334e6fd87521741d2c7c35e647fad28a8d9cd245c0daf33b9f6151ef85b154d5",
    "candidate-results.json":
        "01a5341fec7e5f26a31671c5227b3851bf6635f6ef0f3f1f9f00d0172431ffd2",
    "full_tree_partition.py":
        "875c098a2a9465e146c77757e3d197be8af35f46ee4e772321acf8ca33b5fef8",
    "moh_skeleton_full.py":
        "d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


for name, expected in EXPECTED.items():
    got = sha256(INPUTS / name)
    if got != expected:
        raise SystemExit(f"hash mismatch for {name}: {got} != {expected}")


excess = json.loads((INPUTS / "full-tree-ode-excess-witnesses.json").read_text())
keys_90 = sorted(ast.literal_eval(k) for k in excess if ast.literal_eval(k)[:2] == (90, 60))
if not keys_90:
    raise SystemExit("no (90,60) excess witness")
key_90 = keys_90[0]
print("lex-first-(90,60):", key_90)
print("witness:", json.dumps(excess[repr(key_90)], sort_keys=True))


# Load the frozen skeleton under the name expected by full_tree_partition.py.
spec_m = importlib.util.spec_from_file_location(
    "moh_skeleton_full", INPUTS / "moh_skeleton_full.py"
)
assert spec_m and spec_m.loader
M = importlib.util.module_from_spec(spec_m)
sys.modules["moh_skeleton_full"] = M
spec_m.loader.exec_module(M)

spec_f = importlib.util.spec_from_file_location(
    "full_tree_partition", INPUTS / "full_tree_partition.py"
)
assert spec_f and spec_f.loader
F = importlib.util.module_from_spec(spec_f)
spec_f.loader.exec_module(F)

target = (108, 72, (81, 106), ((2, 7), (3, 7)))
found = None
for m, Ms, V in M.census(108, Kmin=16, full=True):
    key = (108, m, tuple(Ms), tuple(sorted(V.items())))
    if key == target:
        found = M.Skel(108, m, list(Ms), V)
        break
if found is None:
    raise SystemExit(f"D=108 target absent: {target}")

base = json.loads((INPUTS / "candidate-results.json").read_text())
full_tree_ode_record = next(
    record for record in base["results"] if record["name"] == "C_FULL_TREE_ODE"
)
selected_counts = full_tree_ode_record["D_48_200"]["selected_degree_counts"]
if "108" not in selected_counts:
    raise SystemExit("frozen aggregate has no D=108 survivor count")

ok, witness_108 = F.evaluator(found, ode_nondegenerate=True).embeds(found)
if not ok:
    raise SystemExit("D=108 target fails the frozen full-tree-ODE evaluator")
print("selected-D108:", target)
print("aggregate-D108:", json.dumps(selected_counts["108"], sort_keys=True))
print("full-tree-ODE-witness:", json.dumps(witness_108, sort_keys=True))
