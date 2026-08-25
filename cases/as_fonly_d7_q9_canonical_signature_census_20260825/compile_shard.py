#!/usr/bin/env python3
"""Exhaust one deterministic shard of the canonical 3^13 Q9 signature chart."""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
import struct
from collections import Counter
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
PARENT = (ROOT / "cases/as_fonly_d7_q8state_next_high_samples_20260825"
          / "compile_state.py")
EXPECTED_PARENT_SHA = (
    "abfd5cfa79edb87e16e2df706f7466dcf335302d889cb71bf06bcdfb9609588e")
parent_payload = PARENT.read_bytes()
assert hashlib.sha256(parent_payload).hexdigest() == EXPECTED_PARENT_SHA
parent_source = parent_payload.decode()

# Load the source-honest state construction without executing any sampled
# family or its 3^9 successor enumeration.
family_marker = '\nfamily = os.environ["STATE_FAMILY"]\n'
restored_marker = "\ndef restored(values):\n"
recursive_marker = "\ndef recursive_high(q7_values):\n"
assert parent_source.count(family_marker) == 1
assert parent_source.count(restored_marker) == 1
assert parent_source.count(recursive_marker) == 1
scope = {"__file__": str(PARENT), "__name__": "__signature_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(parent_source.split(family_marker, 1)[0], str(PARENT), "exec"),
         scope)
q7_fragment = (restored_marker
    + parent_source.split(restored_marker, 1)[1].split(recursive_marker, 1)[0])
exec(compile(q7_fragment, str(PARENT), "exec"), scope)

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
new_polynomials = scope["new_polynomials"]
y_polynomials = scope["y_polynomials"]
restored = scope["restored"]

nadd = scope["nadd"]
nscale = scope["nscale"]
nmul = scope["nmul"]
nderivative = scope["nderivative"]
nbracket = scope["nbracket"]
degree_part = scope["degree_part"]
divide_exact = scope["divide_exact"]

TOTAL = 3 ** 13
RECORD_BYTES = 4 * 32
forced = {10: 0, 11: 0, 12: 0, 13: 0, 15: 0, 17: 1}
free_q9 = tuple(index for index in range(19) if index not in forced)
assert len(free_q9) == 13


def ternary(index: int, width: int) -> tuple[int, ...]:
    answer = []
    for _ in range(width):
        answer.append(index % 3)
        index //= 3
    assert index == 0
    return tuple(answer)


def update_scalar(hasher, label: str, value: int) -> None:
    encoded = label.encode()
    hasher.update(struct.pack(">H", len(encoded)))
    hasher.update(encoded)
    raw = str(value).encode()
    hasher.update(struct.pack(">H", len(raw)))
    hasher.update(raw)


def update_vector(hasher, label: str, values) -> None:
    encoded = label.encode()
    hasher.update(struct.pack(">H", len(encoded)))
    hasher.update(encoded)
    values = tuple(int(value) for value in values)
    hasher.update(struct.pack(">I", len(values)))
    for value in values:
        raw = str(value).encode()
        hasher.update(struct.pack(">H", len(raw)))
        hasher.update(raw)


def update_matrix(hasher, label: str, matrix) -> None:
    rows = tuple(tuple(int(value) for value in line) for line in matrix)
    update_scalar(hasher, label + ":rows", len(rows))
    update_scalar(hasher, label + ":cols", len(rows[0]) if rows else 0)
    update_vector(hasher, label + ":flat",
                  (value for line in rows for value in line))


def update_poly(hasher, label: str, poly) -> None:
    encoded = label.encode()
    hasher.update(struct.pack(">H", len(encoded)))
    hasher.update(encoded)
    items = sorted((int(i), int(j), int(value))
                   for (i, j), value in poly.items() if value)
    hasher.update(struct.pack(">I", len(items)))
    for i, j, value in items:
        hasher.update(struct.pack(">hh", i, j))
        raw = str(value).encode()
        hasher.update(struct.pack(">H", len(raw)))
        hasher.update(raw)


def source_trace(xvalues) -> bytes:
    """Hash exact charged Q9 source rows before their final mod-3 reduction."""
    C2, D2, C4, D4, W7, Z7 = new_polynomials(xvalues)
    C = nadd(source_data["Cbase"], C2, C4)
    D = nadd(source_data["Dbase"], D2, D4)
    E = nadd(source_data["L1"], source_data["K"],
             nderivative(C, 0), nderivative(D, 1))
    cx, cy = nderivative(C, 0), nderivative(C, 1)
    dx, dy = nderivative(D, 0), nderivative(D, 1)
    M = nadd(nmul(source_data["A"], dy), nmul(cx, source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], dx)),
             nscale(-1, nmul(cy, source_data["vx"])))
    F6 = nadd(source_data["E1_6"], degree_part(M, 6),
              nderivative(W7, 0), nderivative(Z7, 1))
    N9 = degree_part(nbracket(C, D), 9)
    T = nadd(nmul(source_data["A"], nderivative(Z7, 1)),
             nmul(nderivative(W7, 0), source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], nderivative(Z7, 0))),
             nscale(-1, nmul(nderivative(W7, 1), source_data["vx"])))
    G9 = nadd(source_data["F1_9"], N9, degree_part(T, 9))
    h = hashlib.sha256(b"AS-Q9-EXACT-SOURCE-TRACE-V1")
    for label, poly in (("E1", degree_part(E, 1)),
                        ("E3", degree_part(E, 3)),
                        ("M6", degree_part(M, 6)),
                        ("F6", F6), ("N9", N9),
                        ("T9", degree_part(T, 9)), ("G9", G9)):
        update_poly(h, label, poly)
    return h.digest()


def q8_trace(xvalues, yvalues) -> bytes:
    """Hash every exact integer quotient/carry used at the Q8 particular."""
    C2, D2, C4, D4, W7, Z7 = new_polynomials(xvalues)
    C3, D3, W4, Z4, W6, Z6 = y_polynomials(yvalues)
    C = nadd(source_data["Cbase"], C2, C3, C4)
    D = nadd(source_data["Dbase"], D2, D3, D4)
    W = nadd(W4, W6, W7)
    Z = nadd(Z4, Z6, Z7)
    E = nadd(source_data["L1"], source_data["K"],
             nderivative(C, 0), nderivative(D, 1))
    cx, cy = nderivative(C, 0), nderivative(C, 1)
    dx, dy = nderivative(D, 0), nderivative(D, 1)
    M = nadd(nmul(source_data["A"], dy), nmul(cx, source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], dx)),
             nscale(-1, nmul(cy, source_data["vx"])))
    E3, E5 = degree_part(E, 3), degree_part(E, 5)
    E1_3, E1_5 = divide_exact(E3, 3), divide_exact(E5, 3)
    assert degree_part(E, 8) == {}
    F3 = nadd(E1_3, degree_part(M, 3),
              nderivative(W4, 0), nderivative(Z4, 1))
    F5 = nadd(E1_5, degree_part(M, 5),
              nderivative(W6, 0), nderivative(Z6, 1))
    F8 = degree_part(M, 8)
    F1_8 = divide_exact(F8, 3)
    N8 = degree_part(nbracket(C, D), 8)
    T = nadd(nmul(source_data["A"], nderivative(Z, 1)),
             nmul(nderivative(W, 0), source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], nderivative(Z, 0))),
             nscale(-1, nmul(nderivative(W, 1), source_data["vx"])))
    T8 = degree_part(T, 8)
    G8 = nadd(F1_8, N8, T8)
    h = hashlib.sha256(b"AS-Q8-EXACT-CARRY-TRACE-V1")
    for label, poly in (("E2", degree_part(E, 2)), ("E3", E3),
                        ("E1_3", E1_3), ("M3", degree_part(M, 3)),
                        ("F3", F3), ("E5", E5), ("E1_5", E1_5),
                        ("M5", degree_part(M, 5)), ("F5", F5),
                        ("F8", F8), ("F1_8", F1_8), ("N8", N8),
                        ("T8", T8), ("G8", G8)):
        update_poly(h, label, poly)
    return h.digest()


def q7_trace(xvalues, yvalues, q7values) -> bytes:
    """Hash every exact integer quotient/carry used at the Q7 particular."""
    C2, D2, C4, D4, W7, Z7 = new_polynomials(xvalues)
    C3, D3, W4, Z4, W6, Z6 = y_polynomials(yvalues)
    C6, D6, W5, Z5 = restored(q7values)
    C = nadd(source_data["Cbase"], C2, C3, C4, C6)
    D = nadd(source_data["Dbase"], D2, D3, D4, D6)
    W = nadd(W4, W5, W6, W7)
    Z = nadd(Z4, Z5, Z6, Z7)
    E = nadd(source_data["L1"], source_data["K"],
             nderivative(C, 0), nderivative(D, 1))
    cx, cy = nderivative(C, 0), nderivative(C, 1)
    dx, dy = nderivative(D, 0), nderivative(D, 1)
    M = nadd(nmul(source_data["A"], dy), nmul(cx, source_data["vy"]),
             nscale(-1, nmul(source_data["uy"], dx)),
             nscale(-1, nmul(cy, source_data["vx"])))
    E4, E5, E7 = (degree_part(E, degree) for degree in (4, 5, 7))
    E1_4, E1_5, E1_7 = (divide_exact(poly, 3)
                         for poly in (E4, E5, E7))
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
    T7 = degree_part(T, 7)
    G7 = nadd(F1_7, N7, T7)
    h = hashlib.sha256(b"AS-Q7-EXACT-CARRY-TRACE-V1")
    for label, poly in (("E4", E4), ("E1_4", E1_4),
                        ("M4", degree_part(M, 4)), ("F4", F4),
                        ("E5", E5), ("E1_5", E1_5),
                        ("M5", degree_part(M, 5)), ("F5", F5),
                        ("E7", E7), ("E1_7", E1_7),
                        ("M7", degree_part(M, 7)), ("F7", F7),
                        ("F1_7", F1_7), ("N7", N7),
                        ("T7", T7), ("G7", G7)):
        update_poly(h, label, poly)
    return h.digest()


def rref_digest(label, A, b, rank, augmented, pivots, work,
                particular, kernel) -> bytes:
    h = hashlib.sha256(label.encode())
    update_matrix(h, "A", A)
    update_vector(h, "b", b)
    update_scalar(h, "rank", rank)
    update_scalar(h, "augmented", augmented)
    update_vector(h, "pivots", pivots)
    update_matrix(h, "work", work)
    update_vector(h, "particular", particular)
    update_matrix(h, "kernel", kernel)
    return h.digest()


shard_count = int(os.environ["SHARD_COUNT"])
shard_index = int(os.environ["SHARD_INDEX"])
assert 1 <= shard_count <= TOTAL and 0 <= shard_index < shard_count
start = TOTAL * shard_index // shard_count
end = TOTAL * (shard_index + 1) // shard_count
results_dir = Path(os.environ["RESULTS_DIR"])
results_dir.mkdir(parents=True, exist_ok=True)

records_path = results_dir / f"records_{shard_index:03d}.bin"
classes = Counter()
first_index = {}
q8_rref_counts = Counter()
q7_rref_counts = Counter()
carry_counts = Counter()
state_stream = hashlib.sha256()

with records_path.open("wb") as records:
    for state_index in range(start, end):
        parameters = ternary(state_index, 13)
        t = [0] * 19
        for index, value in forced.items():
            t[index] = value
        for index, value in zip(free_q9, parameters):
            t[index] = value
        xvalues = add_vector(q9_origin, q9_kernel, t, reduce=True)
        assert source_rows(source_data, xvalues) == [0] * 23

        A8, b8 = matrix_and_rhs(transition_rows, xvalues, q8_variable_count)
        rank8, augmented8, pivots8, work8, y0 = rref_solve(A8, b8)
        assert (rank8, augmented8) == (13, 13) and y0 is not None
        kernel_rank8, kernel8 = kernel_basis(A8)
        assert kernel_rank8 == 13 and len(kernel8) == 19
        assert transition_rows(xvalues, y0) == [0] * 22

        scope["xvalues"] = xvalues
        scope["yvalues"] = y0
        A7, b7 = affine_matrix(q7_rows, 18)
        rank7, augmented7, pivots7, work7, q7part = rref_solve(A7, b7)
        assert (rank7, augmented7) == (9, 9) and q7part is not None
        kernel_rank7, kernel7 = kernel_basis(A7)
        assert kernel_rank7 == 9 and len(kernel7) == 9
        assert q7_rows(q7part) == [0] * 19

        q9_digest = source_trace(xvalues)
        q8_carry = q8_trace(xvalues, y0)
        q7_carry = q7_trace(xvalues, y0, q7part)
        carry_hasher = hashlib.sha256(b"AS-COMBINED-EXACT-CARRY-V1")
        carry_hasher.update(q9_digest + q8_carry + q7_carry)
        carry_digest = carry_hasher.digest()
        rref8 = rref_digest("AS-Q8-RREF-V1", A8, b8, rank8, augmented8,
                            pivots8, work8, y0, kernel8)
        rref7 = rref_digest("AS-Q7-RREF-V1", A7, b7, rank7, augmented7,
                            pivots7, work7, q7part, kernel7)
        full_hasher = hashlib.sha256(b"AS-Q9-ZERO-SECTION-SIGNATURE-V1")
        full_hasher.update(carry_digest + rref8 + rref7)
        signature = full_hasher.digest()
        record = signature + carry_digest + rref8 + rref7
        assert len(record) == RECORD_BYTES
        records.write(record)
        signature_hex = signature.hex()
        classes[signature_hex] += 1
        first_index.setdefault(signature_hex, state_index)
        q8_rref_counts[rref8.hex()] += 1
        q7_rref_counts[rref7.hex()] += 1
        carry_counts[carry_digest.hex()] += 1
        update_vector(state_stream, "t", parameters)
        update_vector(state_stream, "x", xvalues)
        state_stream.update(record)

assert records_path.stat().st_size == (end - start) * RECORD_BYTES
classes_path = results_dir / f"classes_{shard_index:03d}.tsv"
with classes_path.open("w") as handle:
    for signature in sorted(classes):
        handle.write(f"{signature}\t{classes[signature]}\t{first_index[signature]}\n")

summary = {
    "shard_count": shard_count,
    "shard_index": shard_index,
    "start": start,
    "end": end,
    "state_count": end - start,
    "record_bytes": RECORD_BYTES,
    "records_sha256": hashlib.sha256(records_path.read_bytes()).hexdigest(),
    "state_record_stream_sha256": state_stream.hexdigest(),
    "class_count": len(classes),
    "q8_rref_class_count": len(q8_rref_counts),
    "q7_rref_class_count": len(q7_rref_counts),
    "carry_class_count": len(carry_counts),
    "parent_sha256": EXPECTED_PARENT_SHA,
}
summary_bytes = (json.dumps(summary, sort_keys=True, separators=(",", ":"))
                 + "\n").encode()
(results_dir / f"summary_{shard_index:03d}.json").write_bytes(summary_bytes)
print("shard_range_count", shard_index, start, end, end - start)
print("class_counts", len(classes), len(carry_counts),
      len(q8_rref_counts), len(q7_rref_counts))
print("records_sha256", summary["records_sha256"])
print("state_record_stream_sha256", summary["state_record_stream_sha256"])
print("summary_sha256", hashlib.sha256(summary_bytes).hexdigest())
print("PASS-AS-Q9-CANONICAL-SIGNATURE-SHARD")
