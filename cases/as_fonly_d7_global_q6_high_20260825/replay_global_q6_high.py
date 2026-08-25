#!/usr/bin/env python3
"""Nested-source and literal-high replay of a global Q6/high SAT model."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT_REPLAY = (ROOT / "cases/as_fonly_d7_global_predecessor_rawq7_20260825"
                 / "replay_model.py")
EXPECTED_PARENT_SHA = (
    "b4acf93af94774e124502f3b6cd20be40b10197a808eb7b8ad0d7c92395b99d4")
payload = PARENT_REPLAY.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA
source = payload.decode()
marker = '\nmodel_path = Path(os.environ["MODEL_OUTPUT"])\n'
assert source.count(marker) == 1
scope = {"__file__": str(PARENT_REPLAY), "__name__": "__q6_high_replay_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(marker, 1)[0], str(PARENT_REPLAY), "exec"), scope)

structural = tuple(scope["structural"])
frob = tuple(scope["frob"])
unknowns = tuple(scope["unknowns"])
predecessor_names = structural + frob + unknowns
matrix, rhs = scope["matrix"], scope["rhs"]
N12, Q11, Q10 = scope["N12"], scope["Q11"], scope["Q10"]
eval_expr = scope["eval_expr"]
canonical_source = scope["canonical_source"]
source_rows = scope["source_rows"]
transition_rows = scope["transition_rows"]
q7_rows = scope["q7_rows"]
state_polynomials = scope["state_polynomials"]
homogeneous_numeric = scope["homogeneous_numeric"]
nadd = scope["nadd"]
nscale = scope["nscale"]
nmul = scope["nmul"]
nderivative = scope["nderivative"]
nbracket = scope["nbracket"]
degree_part = scope["degree_part"]
divide_exact = scope["divide_exact"]
row = scope["row"]


def parse_model(path):
    values = {}
    prefixes = ("pred_", "q9_", "q8_", "q7_", "q6_")
    for line in path.read_text().splitlines():
        fields = line.split()
        if len(fields) == 2 and fields[0].startswith(prefixes):
            assert fields[0] not in values
            values[fields[0]] = int(fields[1])
    expected = ({f"pred_{name}" for name in predecessor_names}
                | {f"q9_{index}" for index in range(32)}
                | {f"q8_{index}" for index in range(32)}
                | {f"q7_{index}" for index in range(18)}
                | {f"q6_{index}" for index in range(16)})
    assert set(values) == expected, (expected - set(values), set(values) - expected)
    assert all(0 <= value <= 2 for value in values.values())
    return values


model_path = Path(os.environ["MODEL_OUTPUT"])
model = parse_model(model_path)
predecessor_values = [model[f"pred_{name}"] for name in predecessor_names]
xvalues = [model[f"q9_{index}"] for index in range(32)]
yvalues = [model[f"q8_{index}"] for index in range(32)]
rvalues = [model[f"q7_{index}"] for index in range(18)]
hvalues = [model[f"q6_{index}"] for index in range(16)]
assignment = dict(zip(predecessor_names, predecessor_values))

parent_rows = []
for row_entries, affine in zip(matrix, rhs):
    value = eval_expr(affine, assignment)
    value += sum(eval_expr(entry, assignment) * assignment[name]
                 for entry, name in zip(row_entries, unknowns))
    parent_rows.append(value % 3)
top_rows = [[eval_expr(expression, assignment) for expression in block]
            for block in (N12, Q11, Q10)]
assert parent_rows == [0] * 20
assert all(not any(block) for block in top_rows)

source_data = canonical_source(assignment)
q9 = source_rows(source_data, xvalues)
q8 = transition_rows(source_data, xvalues, yvalues)
q7 = q7_rows(source_data, xvalues, yvalues, rvalues)
assert q9 == [0] * 23 and q8 == [0] * 22 and q7 == [0] * 19
C, D, W, Z = state_polynomials(source_data, xvalues, yvalues, rvalues)
E = nadd(source_data["L1"], source_data["K"],
         nderivative(C, 0), nderivative(D, 1))
cx, cy = nderivative(C, 0), nderivative(C, 1)
dx, dy = nderivative(D, 0), nderivative(D, 1)
M = nadd(nmul(source_data["A"], dy),
         nmul(cx, source_data["vy"]),
         nscale(-1, nmul(source_data["uy"], dx)),
         nscale(-1, nmul(cy, source_data["vx"])))
N = nbracket(C, D)
T = nadd(nmul(source_data["A"], nderivative(Z, 1)),
         nmul(nderivative(W, 0), source_data["vy"]),
         nscale(-1, nmul(source_data["uy"], nderivative(Z, 0))),
         nscale(-1, nmul(nderivative(W, 1), source_data["vx"])))
Rmix = nadd(nmul(cx, nderivative(Z, 1)),
            nmul(nderivative(W, 0), dy),
            nscale(-1, nmul(cy, nderivative(Z, 0))),
            nscale(-1, nmul(nderivative(W, 1), dx)))
divWZ = nadd(nderivative(W, 0), nderivative(Z, 1))


def G(degree):
    E1 = divide_exact(degree_part(E, degree), 3)
    F = nadd(E1, degree_part(M, degree), degree_part(divWZ, degree))
    F1 = divide_exact(F, 3)
    return nadd(F1, degree_part(N, degree), degree_part(T, degree))


final_g8 = row(G(8), 8)
assert final_g8 == [0] * 9
H7 = homogeneous_numeric(7, hvalues[:8])
J7 = homogeneous_numeric(7, hvalues[8:])
q6 = row(nadd(G(6), nderivative(H7, 0), nderivative(J7, 1)), 6)
assert q6 == [0] * 7
S = nadd(nmul(source_data["A"], nderivative(J7, 1)),
         nmul(nderivative(H7, 0), source_data["vy"]),
         nscale(-1, nmul(source_data["uy"], nderivative(J7, 0))),
         nscale(-1, nmul(nderivative(H7, 1), source_data["vx"])))
recursive = {}
for degree in range(7, 13):
    recursive[degree] = row(nadd(divide_exact(G(degree), 3),
                                  degree_part(S, degree),
                                  degree_part(Rmix, degree)), degree)
assert all(not any(values) for values in recursive.values())

P = nadd({(1, 0): 1, (3, 0): -1}, nscale(3, source_data["U"]),
         nscale(9, C), nscale(27, W), nscale(81, H7))
Q = nadd({(0, 1): 1}, nscale(3, source_data["V"]),
         nscale(9, D), nscale(27, Z), nscale(81, J7))
det_minus_one = nadd(
    nmul(nderivative(P, 0), nderivative(Q, 1)),
    nscale(-1, nmul(nderivative(P, 1), nderivative(Q, 0))),
    {(0, 0): -1})
literal = {degree: row(divide_exact(degree_part(det_minus_one, degree), 243),
                       degree) for degree in range(7, 13)}
assert literal == recursive

result = {
    "status": "PASS-GLOBAL-Q6-HIGH-DIRECT-REPLAY",
    "model_sha256": hashlib.sha256(model_path.read_bytes()).hexdigest(),
    "predecessor_values": predecessor_values,
    "q9_values": xvalues,
    "q8_values": yvalues,
    "q7_values": rvalues,
    "q6_values": hvalues,
    "parent_rows": parent_rows,
    "top_rows": top_rows,
    "q9_rows": q9,
    "q8_rows": q8,
    "q7_rows": q7,
    "final_g8_rows": final_g8,
    "q6_rows": q6,
    "recursive_literal_div243_degrees_12_to_7_agreement": True,
    "terminal_rows": {str(degree): recursive[degree]
                       for degree in range(12, 6, -1)},
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("row_shapes", 20, 5, 12, 11, 23, 22, 19, 9, 7, 63)
print("recursive_literal_div243_degrees_12_to_7_agreement", True)
print("model_sha256", result["model_sha256"])
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-GLOBAL-Q6-HIGH-DIRECT-REPLAY")
