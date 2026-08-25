#!/usr/bin/env python3
"""Classify one predecessor state through its entire Q7 high-carry fibre."""
from __future__ import annotations

import contextlib
import hashlib
import io
import itertools
import json
import os
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
FIBRE = (ROOT / "cases/as_fonly_d7_q9_fibre_kuranishi_q8_20260825"
         / "compile_fibre_kuranishi.py")
EXPECTED_FIBRE_SHA = "cc75c22f1330f6d8a272941200d35199a3cdbecbaa33551b52217970c1f0018d"
payload = FIBRE.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_FIBRE_SHA
source = payload.decode()
marker = "\nparameter_count = len(q9_kernel)\n"
assert source.count(marker) == 1
kscope = {"__file__": str(FIBRE), "__name__": "__fibre_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(marker, 1)[0], str(FIBRE), "exec"), kscope)

vscope = kscope["scope"]
source_data = kscope["source_data"]
source_rows = kscope["source_rows"]
transition_rows = kscope["transition_rows"]
matrix_and_rhs = kscope["matrix_and_rhs"]
q9_origin = tuple(kscope["q9_vector"])
q9_kernel = tuple(kscope["q9_kernel"])
q8_kernel_at_origin = tuple(kscope["top_kernel"])
q8_variable_count = len(kscope["y_names"])
add_vector = kscope["add_vector"]
rref_solve = kscope["rref_solve"]
kernel_basis = kscope["kernel_basis"]
affine_matrix = kscope["affine_matrix"]

new_polynomials = vscope["new_polynomials"]
y_polynomials = vscope["y_polynomials"]
homogeneous_numeric = vscope["homogeneous_numeric"]
nadd = vscope["nadd"]
nscale = vscope["nscale"]
nmul = vscope["nmul"]
nderivative = vscope["nderivative"]
nbracket = vscope["nbracket"]
degree_part = vscope["degree_part"]
divide_exact = vscope["divide_exact"]
row = vscope["row"]

family = os.environ["STATE_FAMILY"]
sample_index = int(os.environ["SAMPLE_INDEX"])

forced = {10: 0, 11: 0, 12: 0, 13: 0, 15: 0, 17: 1}
free_q9 = tuple(i for i in range(19) if i not in forced)
assert len(free_q9) == 13

if family == "q8_kernel":
    assert 0 <= sample_index < 39
    t = [0] * 19
    t[17] = 1
    xvalues = add_vector(q9_origin, q9_kernel, t, reduce=True)
    A22, b22 = matrix_and_rhs(transition_rows, xvalues, q8_variable_count)
    rank22, augmented22, _p, _w, y0 = rref_solve(A22, b22)
    assert (rank22, augmented22) == (13, 13) and y0 == (0,) * 32
    full_rank, full_kernel = kernel_basis(A22)
    assert full_rank == 13 and len(full_kernel) == 19
    assert full_kernel == q8_kernel_at_origin
    q8_parameters = [0] * 19
    if sample_index:
        direction = (sample_index - 1) // 2
        scalar = 1 + (sample_index - 1) % 2
        q8_parameters[direction] = scalar
    yvalues = add_vector(y0, full_kernel, q8_parameters, reduce=True)
    state_parameters = q8_parameters
elif family == "q9_locus":
    assert 0 <= sample_index < 27
    t = [0] * 19
    t[17] = 1
    if sample_index:
        direction = (sample_index - 1) // 2
        scalar = 1 + (sample_index - 1) % 2
        t[free_q9[direction]] = scalar
    xvalues = add_vector(q9_origin, q9_kernel, t, reduce=True)
    A22, b22 = matrix_and_rhs(transition_rows, xvalues, q8_variable_count)
    rank22, augmented22, _p, _w, yvalues = rref_solve(A22, b22)
    state_parameters = t
else:
    raise AssertionError(family)

assert source_rows(source_data, xvalues) == [0] * 23
q8_compatible = yvalues is not None
if q8_compatible:
    assert transition_rows(xvalues, yvalues) == [0] * 22


def restored(values):
    assignment = dict(zip(
        ("c6_0", "c6_3", "c6_6", "d6_0", "d6_3", "d6_6")
        + tuple(f"w5_{i}" for i in range(6))
        + tuple(f"z5_{i}" for i in range(6)), values))
    C6 = homogeneous_numeric(6, [assignment["c6_0"], 0, 0,
        assignment["c6_3"], 0, 0, assignment["c6_6"]])
    D6 = homogeneous_numeric(6, [assignment["d6_0"], 0, 0,
        assignment["d6_3"], 0, 0, assignment["d6_6"]])
    W5 = homogeneous_numeric(5, [assignment[f"w5_{i}"] for i in range(6)])
    Z5 = homogeneous_numeric(5, [assignment[f"z5_{i}"] for i in range(6)])
    return C6, D6, W5, Z5


def state_polynomials(q7_values):
    C2, D2, C4, D4, W7, Z7 = new_polynomials(xvalues)
    C3, D3, W4, Z4, W6, Z6 = y_polynomials(yvalues)
    C6, D6, W5, Z5 = restored(q7_values)
    C = nadd(source_data["Cbase"], C2, C3, C4, C6)
    D = nadd(source_data["Dbase"], D2, D3, D4, D6)
    W = nadd(W4, W5, W6, W7)
    Z = nadd(Z4, Z5, Z6, Z7)
    return C, D, W, Z


def q7_rows(q7_values):
    C, D, W, Z = state_polynomials(q7_values)
    E = nadd(source_data["L1"], source_data["K"],
             nderivative(C, 0), nderivative(D, 1))
    E1_4 = divide_exact(degree_part(E, 4), 3)
    E1_5 = divide_exact(degree_part(E, 5), 3)
    E1_7 = divide_exact(degree_part(E, 7), 3)
    cx, cy = nderivative(C, 0), nderivative(C, 1)
    dx, dy = nderivative(D, 0), nderivative(D, 1)
    M = nadd(nmul(source_data["A"], dy), nmul(cx, source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], dx)),
             nscale(-1, nmul(cy, source_data["vx"])))
    F4 = nadd(E1_4, degree_part(M, 4),
              degree_part(nadd(nderivative(W, 0), nderivative(Z, 1)), 4))
    F5 = nadd(E1_5, degree_part(M, 5),
              degree_part(nadd(nderivative(W, 0), nderivative(Z, 1)), 5))
    F7 = nadd(E1_7, degree_part(M, 7))
    F1_7 = divide_exact(F7, 3)
    N7 = degree_part(nbracket(C, D), 7)
    T = nadd(nmul(source_data["A"], nderivative(Z, 1)),
             nmul(nderivative(W, 0), source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], nderivative(Z, 0))),
             nscale(-1, nmul(nderivative(W, 1), source_data["vx"])))
    G7 = nadd(F1_7, N7, degree_part(T, 7))
    return row(F5, 5) + row(F4, 4) + row(G7, 7)


def recursive_high(q7_values):
    C, D, W, Z = state_polynomials(q7_values)
    E = nadd(source_data["L1"], source_data["K"],
             nderivative(C, 0), nderivative(D, 1))
    cx, cy = nderivative(C, 0), nderivative(C, 1)
    dx, dy = nderivative(D, 0), nderivative(D, 1)
    M = nadd(nmul(source_data["A"], dy), nmul(cx, source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], dx)),
             nscale(-1, nmul(cy, source_data["vx"])))
    N = nbracket(C, D)
    T = nadd(nmul(source_data["A"], nderivative(Z, 1)),
             nmul(nderivative(W, 0), source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], nderivative(Z, 0))),
             nscale(-1, nmul(nderivative(W, 1), source_data["vx"])))
    Rmix = nadd(nmul(cx, nderivative(Z, 1)), nmul(nderivative(W, 0), dy),
                nscale(-1, nmul(cy, nderivative(Z, 0))),
                nscale(-1, nmul(nderivative(W, 1), dx)))
    result = {}
    for degree in range(9, 13):
        E1 = divide_exact(degree_part(E, degree), 3)
        F = nadd(E1, degree_part(M, degree),
                 degree_part(nadd(nderivative(W, 0),
                                  nderivative(Z, 1)), degree))
        F1 = divide_exact(F, 3)
        G = nadd(F1, degree_part(N, degree), degree_part(T, degree))
        result[degree] = row(nadd(divide_exact(G, 3),
                                  degree_part(Rmix, degree)), degree)
    return C, D, W, Z, result


def direct_high(C, D, W, Z):
    P0 = {(1, 0): 1, (3, 0): -1}
    Q0 = {(0, 1): 1}
    P = nadd(P0, nscale(3, source_data["U"]), nscale(9, C), nscale(27, W))
    Q = nadd(Q0, nscale(3, source_data["V"]), nscale(9, D), nscale(27, Z))
    determinant = nadd(nmul(nderivative(P, 0), nderivative(Q, 1)),
        nscale(-1, nmul(nderivative(P, 1), nderivative(Q, 0))), {(0, 0): -1})
    return {degree: row(divide_exact(degree_part(determinant, degree), 243), degree)
            for degree in range(9, 13)}


def ternary(index, width):
    values = []
    for _ in range(width):
        values.append(index % 3)
        index //= 3
    assert index == 0
    return tuple(values)


result = {"family": family, "sample_index": sample_index,
          "state_parameters": state_parameters,
          "xvalues": list(xvalues),
          "yvalues": list(yvalues) if yvalues is not None else None,
          "q8_rank_pair": [rank22, augmented22],
          "q8_compatible": q8_compatible}

if q8_compatible:
    A7, b7 = affine_matrix(q7_rows, 18)
    rank7, augmented7, _p7, _w7, q7_particular = rref_solve(A7, b7)
    result["q7_rank_pair"] = [rank7, augmented7]
    result["q7_compatible"] = q7_particular is not None
    if q7_particular is not None:
        _rank7, q7_kernel = kernel_basis(A7)
        dimension = len(q7_kernel)
        result["q7_fiber_dimension"] = dimension
        if dimension <= 10:
            total = 3 ** dimension
            records = {}
            zero_indices = []
            stream = hashlib.sha256()
            for index in range(total):
                parameters = ternary(index, dimension)
                q7_values = add_vector(q7_particular, q7_kernel, parameters,
                                       reduce=True)
                assert q7_rows(q7_values) == [0] * 19
                C, D, W, Z, recursive = recursive_high(q7_values)
                direct = direct_high(C, D, W, Z)
                assert recursive == direct
                high = tuple(value for degree in range(12, 8, -1)
                             for value in recursive[degree])
                records[index] = high
                stream.update(bytes(high))
                if not any(high):
                    zero_indices.append(index)
            width = len(records[0])
            pairs = list(itertools.combinations(range(dimension), 2))
            constant = records[0]
            linear = [[0] * dimension for _ in range(width)]
            square = [[0] * dimension for _ in range(width)]
            cross = [[0] * len(pairs) for _ in range(width)]
            for variable in range(dimension):
                one = [0] * dimension
                one[variable] = 1
                f1 = records[sum(one[i] * 3 ** i for i in range(dimension))]
                one[variable] = 2
                f2 = records[sum(one[i] * 3 ** i for i in range(dimension))]
                for coordinate in range(width):
                    linear[coordinate][variable] = (f2[coordinate] - f1[coordinate]) % 3
                    square[coordinate][variable] = (f1[coordinate] - constant[coordinate]
                        - linear[coordinate][variable]) % 3
            for pair_index, (left, right) in enumerate(pairs):
                both = [0] * dimension
                both[left] = both[right] = 1
                fb = records[sum(both[i] * 3 ** i for i in range(dimension))]
                for coordinate in range(width):
                    cross[coordinate][pair_index] = (fb[coordinate]
                        - constant[coordinate] - linear[coordinate][left]
                        - square[coordinate][left] - linear[coordinate][right]
                        - square[coordinate][right]) % 3

            def predict(parameters):
                answer = []
                for coordinate in range(width):
                    value = constant[coordinate]
                    value += sum(linear[coordinate][i] * parameters[i]
                        + square[coordinate][i] * parameters[i] ** 2
                        for i in range(dimension))
                    value += sum(cross[coordinate][k] * parameters[left]
                        * parameters[right] for k, (left, right) in enumerate(pairs))
                    answer.append(value % 3)
                return tuple(answer)

            quadratic = all(predict(ternary(index, dimension)) == records[index]
                            for index in range(total))
            coefficient_payload = bytes(value for line in
                (list(constant), *linear, *square, *cross) for value in line)
            result.update({
                "q7_states_exhausted": total,
                "high_zero_count": len(zero_indices),
                "high_zero_first_indices": zero_indices[:20],
                "high_stream_sha256": stream.hexdigest(),
                "quadratic_exact": quadratic,
                "quadratic_coefficients_sha256": hashlib.sha256(
                    coefficient_payload).hexdigest(),
                "quadratic_nonzero_coefficient_count": sum(
                    bool(value) for value in coefficient_payload),
            })
        else:
            result["q7_states_exhausted"] = 0

encoded = (json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("family_sample", family, sample_index)
print("q8_rank_pair_compatible", result["q8_rank_pair"], q8_compatible)
print("q7_rank_pair_compatible", result.get("q7_rank_pair"),
      result.get("q7_compatible"))
print("q7_fiber_dimension_states", result.get("q7_fiber_dimension"),
      result.get("q7_states_exhausted"))
print("high_zero_count", result.get("high_zero_count"))
print("quadratic_exact_nonzero_count", result.get("quadratic_exact"),
      result.get("quadratic_nonzero_coefficient_count"))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-Q8STATE-NEXT-HIGH-SAMPLE")
