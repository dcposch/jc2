#!/usr/bin/env python3
"""Classify restoration-charged assertion ASTs without assuming a Z3 version."""

import collections
import hashlib
import json
import os
from pathlib import Path
import runpy

import z3


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_global_q5_q4_cartier_20260825"
          / "solve_global_q5_q4_cartier.py")
EXPECTED = "161287467d04d9ba769a09844405d7fcc7f0d90b53099217e836fd4e9febcdaf"
assert hashlib.sha256(PARENT.read_bytes()).hexdigest() == EXPECTED
OUT = Path(os.environ["OUTPUT_DIR"])
OUT.mkdir(parents=True, exist_ok=False)
os.environ["SMT2_OUTPUT"] = str(OUT / "parent_formula.smt2")
os.environ["OUTPUT_JSON"] = str(OUT / "parent_emitter.json")
os.environ["SOLVER_TIMEOUT_MS"] = "1"
for name in ("PIN_PREDECESSOR", "PIN_STRUCTURAL", "OMIT_Q4_CARTIER",
             "OMIT_Q5_GATE"):
    os.environ.pop(name, None)

outer = runpy.run_path(str(PARENT), run_name="__assertion_diagnostic_parent__")
scope = outer["scope"]
while "solver" not in scope:
    scope = scope["scope"]
solver = scope["solver"]
restoration = list(scope["hvars"]) + list(scope["kvars"])
restoration_names = {variable.decl().name() for variable in restoration}


def variables(expression):
    answer = set()
    stack = [expression]
    seen = set()
    while stack:
        node = stack.pop()
        if node.get_id() in seen:
            continue
        seen.add(node.get_id())
        if (z3.is_const(node)
                and node.decl().kind() == z3.Z3_OP_UNINTERPRETED):
            answer.add(node.decl().name())
        else:
            stack.extend(node.children())
    return answer


counts = collections.Counter()
samples = collections.defaultdict(list)
charged_count = 0
for index, assertion in enumerate(solver.assertions()):
    charged = sorted(variables(assertion) & restoration_names)
    if not charged:
        continue
    charged_count += 1
    top = assertion.decl().kind()
    if top == z3.Z3_OP_ULEQ:
        label = "top-ule"
    elif z3.is_eq(assertion):
        left, right = assertion.children()
        nonzero = right if z3.is_bv_value(left) and left.as_long() == 0 else left
        label = f"eq-candidate-kind-{nonzero.decl().kind()}"
    else:
        label = f"top-kind-{top}"
    counts[label] += 1
    if len(samples[label]) < 6:
        samples[label].append({
            "assertion_index": index,
            "charged": charged,
            "sexpr": assertion.sexpr(),
        })

payload = {
    "status": "PASS-AS-FITTING-RESTORATION-ASSERTION-DIAGNOSTIC",
    "z3_version": z3.get_version_string(),
    "assertion_count": len(solver.assertions()),
    "restoration_variable_count": len(restoration),
    "charged_assertion_count": charged_count,
    "shape_counts": dict(sorted(counts.items())),
    "samples": dict(sorted(samples.items())),
}
encoded = json.dumps(payload, sort_keys=True, indent=2).encode() + b"\n"
(OUT / "diagnostic.json").write_bytes(encoded)
print(json.dumps(payload, sort_keys=True))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
