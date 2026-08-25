#!/usr/bin/env python3
"""Independent literal-integer replay of a global-predecessor Boolector model."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
Q9 = (ROOT / "cases/as_fonly_d7_vertical_q9_state_gate_20260825"
      / "compile_shard.py")
EXPECTED_Q9_SHA = (
    "54d05ebf86af9d75da0cc509e3094ce2e26516b84c73b8a50a36e71dbc9282b2")
payload = Q9.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_Q9_SHA
source = payload.decode()
marker = '\nshard_count = int(os.environ.get("SHARD_COUNT", "27"))\n'
assert source.count(marker) == 1
scope = {"__file__": str(Q9), "__name__": "__global_model_replay_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(marker, 1)[0], str(Q9), "exec"), scope)

structural = tuple(scope["structural"])
frob = tuple(scope["frob"])
unknowns = tuple(scope["unknowns"])
predecessor_names = structural + frob + unknowns
matrix = scope["matrix"]
rhs = scope["rhs"]
N12, Q11, Q10 = scope["N12"], scope["Q11"], scope["Q10"]
eval_expr = scope["eval_expr"]
canonical_source = scope["canonical_source"]
source_rows = scope["source_rows"]
new_polynomials = scope["new_polynomials"]
nadd = scope["nadd"]
nscale = scope["nscale"]
nmul = scope["nmul"]
nderivative = scope["nderivative"]
nbracket = scope["nbracket"]
degree_part = scope["degree_part"]
divide_exact = scope["divide_exact"]
homogeneous_numeric = scope["homogeneous_numeric"]
row = scope["row"]


def parse_model(path):
    values = {}
    for line in path.read_text().splitlines():
        fields = line.split()
        if len(fields) == 2 and (fields[0].startswith("pred_")
                                 or fields[0].startswith("q9_")
                                 or fields[0].startswith("q8_")
                                 or fields[0].startswith("q7_")):
            assert fields[0] not in values
            values[fields[0]] = int(fields[1])
    expected = ({f"pred_{name}" for name in predecessor_names}
                | {f"q9_{index}" for index in range(32)}
                | {f"q8_{index}" for index in range(32)}
                | {f"q7_{index}" for index in range(18)})
    assert set(values) == expected, (sorted(expected - set(values)),
                                     sorted(set(values) - expected))
    assert all(0 <= value <= 2 for value in values.values())
    return values


def y_polynomials(values):
    return (
        homogeneous_numeric(3, values[0:4]),
        homogeneous_numeric(3, values[4:8]),
        homogeneous_numeric(4, values[8:13]),
        homogeneous_numeric(4, values[13:18]),
        homogeneous_numeric(6, values[18:25]),
        homogeneous_numeric(6, values[25:32]),
    )


def restored(values):
    return (
        homogeneous_numeric(6, [values[0], 0, 0, values[1], 0, 0,
                                values[2]]),
        homogeneous_numeric(6, [values[3], 0, 0, values[4], 0, 0,
                                values[5]]),
        homogeneous_numeric(5, values[6:12]),
        homogeneous_numeric(5, values[12:18]),
    )


def core_intermediates(source_data, C, D, W, Z):
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
    return E, M, N, T, Rmix


def transition_rows(source_data, xvalues, yvalues):
    C2, D2, C4, D4, W7, Z7 = new_polynomials(xvalues)
    C3, D3, W4, Z4, W6, Z6 = y_polynomials(yvalues)
    C = nadd(source_data["Cbase"], C2, C3, C4)
    D = nadd(source_data["Dbase"], D2, D3, D4)
    W = nadd(W4, W6, W7)
    Z = nadd(Z4, Z6, Z7)
    E, M, N, T, _ = core_intermediates(source_data, C, D, W, Z)
    E1_3 = divide_exact(degree_part(E, 3), 3)
    E1_5 = divide_exact(degree_part(E, 5), 3)
    F3 = nadd(E1_3, degree_part(M, 3), nderivative(W4, 0),
              nderivative(Z4, 1))
    F5 = nadd(E1_5, degree_part(M, 5), nderivative(W6, 0),
              nderivative(Z6, 1))
    F1_8 = divide_exact(degree_part(M, 8), 3)
    G8 = nadd(F1_8, degree_part(N, 8), degree_part(T, 8))
    return row(E, 2) + row(F3, 3) + row(F5, 5) + row(G8, 8)


def state_polynomials(source_data, xvalues, yvalues, rvalues):
    C2, D2, C4, D4, W7, Z7 = new_polynomials(xvalues)
    C3, D3, W4, Z4, W6, Z6 = y_polynomials(yvalues)
    C6, D6, W5, Z5 = restored(rvalues)
    C = nadd(source_data["Cbase"], C2, C3, C4, C6)
    D = nadd(source_data["Dbase"], D2, D3, D4, D6)
    W = nadd(W4, W5, W6, W7)
    Z = nadd(Z4, Z5, Z6, Z7)
    return C, D, W, Z


def q7_rows(source_data, xvalues, yvalues, rvalues):
    C, D, W, Z = state_polynomials(source_data, xvalues, yvalues, rvalues)
    E, M, N, T, _ = core_intermediates(source_data, C, D, W, Z)
    E1_4 = divide_exact(degree_part(E, 4), 3)
    E1_5 = divide_exact(degree_part(E, 5), 3)
    E1_7 = divide_exact(degree_part(E, 7), 3)
    divWZ = nadd(nderivative(W, 0), nderivative(Z, 1))
    F4 = nadd(E1_4, degree_part(M, 4), degree_part(divWZ, 4))
    F5 = nadd(E1_5, degree_part(M, 5), degree_part(divWZ, 5))
    F1_7 = divide_exact(nadd(E1_7, degree_part(M, 7)), 3)
    G7 = nadd(F1_7, degree_part(N, 7), degree_part(T, 7))
    return row(F5, 5) + row(F4, 4) + row(G7, 7)


def recursive_high(source_data, xvalues, yvalues, rvalues):
    C, D, W, Z = state_polynomials(source_data, xvalues, yvalues, rvalues)
    E, M, N, T, Rmix = core_intermediates(source_data, C, D, W, Z)
    divWZ = nadd(nderivative(W, 0), nderivative(Z, 1))
    result = {}
    for degree in range(9, 13):
        E1 = divide_exact(degree_part(E, degree), 3)
        F = nadd(E1, degree_part(M, degree), degree_part(divWZ, degree))
        F1 = divide_exact(F, 3)
        G = nadd(F1, degree_part(N, degree), degree_part(T, degree))
        result[degree] = row(nadd(divide_exact(G, 3),
                                  degree_part(Rmix, degree)), degree)
    return C, D, W, Z, result


def direct_high(source_data, C, D, W, Z):
    P0 = {(1, 0): 1, (3, 0): -1}
    Q0 = {(0, 1): 1}
    P = nadd(P0, nscale(3, source_data["U"]), nscale(9, C),
             nscale(27, W))
    Q = nadd(Q0, nscale(3, source_data["V"]), nscale(9, D),
             nscale(27, Z))
    determinant = nadd(
        nmul(nderivative(P, 0), nderivative(Q, 1)),
        nscale(-1, nmul(nderivative(P, 1), nderivative(Q, 0))),
        {(0, 0): -1})
    return {degree: row(divide_exact(degree_part(determinant, degree), 243),
                        degree) for degree in range(9, 13)}


model_path = Path(os.environ["MODEL_OUTPUT"])
model = parse_model(model_path)
predecessor_values = [model[f"pred_{name}"] for name in predecessor_names]
xvalues = [model[f"q9_{index}"] for index in range(32)]
yvalues = [model[f"q8_{index}"] for index in range(32)]
rvalues = [model[f"q7_{index}"] for index in range(18)]
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
assert q9 == [0] * 23
assert q8 == [0] * 22
assert q7 == [0] * 19
C, D, W, Z, recursive = recursive_high(
    source_data, xvalues, yvalues, rvalues)
direct = direct_high(source_data, C, D, W, Z)
assert recursive == direct
high = [value for degree in range(12, 8, -1)
        for value in recursive[degree]]
expect_zero = os.environ.get("EXPECT_TERMINAL_ZERO", "0") == "1"
if expect_zero:
    assert not any(high)
else:
    assert any(high)

result = {
    "model_sha256": hashlib.sha256(model_path.read_bytes()).hexdigest(),
    "predecessor_values": predecessor_values,
    "q9_values": xvalues,
    "q8_values": yvalues,
    "q7_values": rvalues,
    "predecessor_rows": parent_rows,
    "top_rows": top_rows,
    "q9_rows": q9,
    "q8_rows": q8,
    "q7_rows": q7,
    "recursive_literal_div243_agreement": True,
    "terminal_high_vector_degrees_12_to_9": high,
    "terminal_nonzero_indices": [index for index, value in enumerate(high)
                                 if value],
    "expect_terminal_zero": expect_zero,
    "source_q9_sha256": EXPECTED_Q9_SHA,
    "status": "PASS-DIRECT-INTEGER-SOURCE-REPLAY",
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("model_sha256", result["model_sha256"])
print("row_shapes", len(parent_rows), *(len(block) for block in top_rows),
      len(q9), len(q8), len(q7), len(high))
print("terminal_nonzero_indices", result["terminal_nonzero_indices"])
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
