#!/usr/bin/env python3
"""Witness-first exact next-high search at one deterministic combined state."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path

ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_q8state_next_high_samples_20260825"
          / "compile_state.py")
EXPECTED_PARENT_SHA = (
    "abfd5cfa79edb87e16e2df706f7466dcf335302d889cb71bf06bcdfb9609588e")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA
source = payload.decode()
family_marker = '\nfamily = os.environ["STATE_FAMILY"]\n'
restored_marker = "\ndef restored(values):\n"
result_marker = '\nresult = {"family": family, "sample_index": sample_index,\n'
assert source.count(family_marker) == 1
assert source.count(restored_marker) == 1
assert source.count(result_marker) == 1
scope = {"__file__": str(PARENT), "__name__": "__witness_first_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(family_marker, 1)[0], str(PARENT), "exec"), scope)
fragment = (restored_marker
            + source.split(restored_marker, 1)[1].split(result_marker, 1)[0])
exec(compile(fragment, str(PARENT), "exec"), scope)

source_data = scope["source_data"]
source_rows = scope["source_rows"]
transition_rows = scope["transition_rows"]
matrix_and_rhs = scope["matrix_and_rhs"]
q9_origin = tuple(scope["q9_origin"])
q9_kernel = tuple(scope["q9_kernel"])
q8_variable_count = scope["q8_variable_count"]
add_vector = scope["add_vector"]
rref_solve = scope["rref_solve"]
kernel_basis = scope["kernel_basis"]
affine_matrix = scope["affine_matrix"]
q7_rows = scope["q7_rows"]
recursive_high = scope["recursive_high"]
direct_high = scope["direct_high"]

sample_index = int(os.environ["SAMPLE_INDEX"])
sample_count = int(os.environ["SAMPLE_COUNT"])
assert sample_count == 24 and 0 <= sample_index < sample_count
forced = {10: 0, 11: 0, 12: 0, 13: 0, 15: 0, 17: 1}
free_q9 = tuple(index for index in range(19) if index not in forced)
assert len(free_q9) == 13

def deterministic_trits(label: str, width: int) -> list[int]:
    if sample_index == 0:
        return [0] * width
    seed = hashlib.sha256(
        f"AS-WITNESS-FIRST-V1:{label}:{sample_index}".encode()).digest()
    integer = int.from_bytes(seed, "big")
    answer = []
    for _ in range(width):
        answer.append(integer % 3)
        integer //= 3
    return answer

q9_parameters = deterministic_trits("Q9", 13)
q9_parameters[6] = 0
q9_parameters[8] = 0
t = [0] * 19
for index, value in forced.items():
    t[index] = value
for index, value in zip(free_q9, q9_parameters):
    t[index] = value
xvalues = add_vector(q9_origin, q9_kernel, t, reduce=True)
assert source_rows(source_data, xvalues) == [0] * 23
state_index = sum(value * 3 ** index
                  for index, value in enumerate(q9_parameters))

A8, b8 = matrix_and_rhs(transition_rows, xvalues, q8_variable_count)
rank8, augmented8, _p8, _w8, y0 = rref_solve(A8, b8)
assert (rank8, augmented8) == (13, 13) and y0 is not None
kernel_rank8, kernel8 = kernel_basis(A8)
assert kernel_rank8 == rank8 and len(kernel8) == 19
q8_parameters = deterministic_trits("Q8", 19)
q8_parameters[15] = 0
q8_parameters[17] = 0
yvalues = add_vector(y0, kernel8, q8_parameters, reduce=True)
assert transition_rows(xvalues, yvalues) == [0] * 22
scope["xvalues"] = xvalues
scope["yvalues"] = yvalues

A7, b7 = affine_matrix(q7_rows, 18)
rank7, augmented7, _p7, _w7, q7_particular = rref_solve(A7, b7)
result = {
    "sample_index": sample_index,
    "sample_count": sample_count,
    "q9_state_index": state_index,
    "q9_parameters": q9_parameters,
    "q8_parameters": q8_parameters,
    "xvalues": list(xvalues),
    "q8_canonical_particular": list(y0),
    "yvalues": list(yvalues),
    "q8_rank_pair": [rank8, augmented8],
    "q7_rank_pair": [rank7, augmented7],
    "q7_compatible": q7_particular is not None,
    "scope": "one deterministic combined Q9/Q8 state",
}

if q7_particular is not None:
    kernel_rank7, kernel7 = kernel_basis(A7)
    assert kernel_rank7 == rank7 == 9 and len(kernel7) == 9
    total = 3 ** 9
    stream = hashlib.sha256()
    zero_witnesses = []
    direct_mismatch_count = 0
    for index in range(total):
        quotient = index
        parameters = []
        for _ in range(9):
            parameters.append(quotient % 3)
            quotient //= 3
        assert quotient == 0
        q7_values = add_vector(q7_particular, kernel7, parameters, reduce=True)
        assert q7_rows(q7_values) == [0] * 19
        C, D, W, Z, recursive = recursive_high(q7_values)
        direct = direct_high(C, D, W, Z)
        if recursive != direct:
            direct_mismatch_count += 1
            raise AssertionError("recursive/direct mismatch")
        high = tuple(value for degree in range(12, 8, -1)
                     for value in recursive[degree])
        stream.update(bytes(high))
        if not any(high):
            zero_witnesses.append({
                "q7_fibre_index": index,
                "q7_parameters": parameters,
                "q7_values": list(q7_values),
            })
    result.update({
        "q7_fibre_dimension": 9,
        "q7_states_exhausted": total,
        "recursive_direct_mismatch_count": direct_mismatch_count,
        "high_zero_count": len(zero_witnesses),
        "high_zero_witnesses": zero_witnesses[:32],
        "high_stream_sha256": stream.hexdigest(),
    })

encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("sample_state", sample_index, state_index)
print("rank_pairs", result["q8_rank_pair"], result["q7_rank_pair"])
print("q7_compatible", result["q7_compatible"])
print("q7_states_exhausted", result.get("q7_states_exhausted", 0))
print("high_zero_count", result.get("high_zero_count"))
print("output_sha256", hashlib.sha256(encoded).hexdigest())
print("PASS-AS-WITNESS-FIRST-DIVERSE-SAMPLE")
