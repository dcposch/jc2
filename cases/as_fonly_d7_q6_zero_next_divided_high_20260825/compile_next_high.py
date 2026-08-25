#!/usr/bin/env python3
"""Next divided high carry on the cumulative zero Q7/Q6 branch."""
from __future__ import annotations

import contextlib
import hashlib
import io
import os
from pathlib import Path

ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
Q7 = (ROOT / "cases/as_fonly_d7_q8_survivor_q7_transition_20260825"
      / "compile_q7_transition.py")
EXPECTED_Q7_SHA = "5e181b09772f5aca83b70acff91a23a0ec60944bfe00c6f5480e36850d5a2941"
payload = Q7.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_Q7_SHA
source = payload.decode()
marker = "\nA, b = affine_matrix(q7_rows, len(names))\n"
assert source.count(marker) == 1
scope = {"__file__": str(Q7), "__name__": "__q7_prefix__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source.split(marker, 1)[0], str(Q7), "exec"), scope)

source_data = scope["source_data"]
q9_survivor = scope["q9_survivor"]
q8_survivor = scope["q8_survivor"]
q7_rows = scope["q7_rows"]
restored = scope["restored"]
new_polynomials = scope["new_polynomials"]
y_polynomials = scope["y_polynomials"]
nadd = scope["nadd"]
nscale = scope["nscale"]
nmul = scope["nmul"]
nderivative = scope["nderivative"]
nbracket = scope["nbracket"]
degree_part = scope["degree_part"]
divide_exact = scope["divide_exact"]
row = scope["row"]

q7_zero = (0,) * 18
q6_zero = (0,) * 16
assert q7_rows(q7_zero) == [0] * 19

C2, D2, C4, D4, W7, Z7 = new_polynomials(q9_survivor)
C3, D3, W4, Z4, W6, Z6 = y_polynomials(q8_survivor)
C6, D6, W5, Z5 = restored(q7_zero)
C = nadd(source_data["Cbase"], C2, C3, C4, C6)
D = nadd(source_data["Dbase"], D2, D3, D4, D6)
W = nadd(W4, W5, W6, W7)
Z = nadd(Z4, Z5, Z6, Z7)
H = {}
J = {}

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

G_by_degree = {}
G1_by_degree = {}
for degree in range(7, 13):
    E1d = divide_exact(degree_part(E, degree), 3)
    Fd = nadd(E1d, degree_part(M, degree),
              degree_part(nadd(nderivative(W, 0),
                               nderivative(Z, 1)), degree))
    F1d = divide_exact(Fd, 3)
    Gd = nadd(F1d, degree_part(N, degree), degree_part(T, degree),
              degree_part(nadd(nderivative(H, 0),
                               nderivative(J, 1)), degree))
    G_by_degree[degree] = Gd
    G1_by_degree[degree] = divide_exact(Gd, 3)

S = nadd(nmul(source_data["A"], nderivative(J, 1)),
         nmul(nderivative(H, 0), source_data["vy"]),
         nscale(-1, nmul(source_data["uy"], nderivative(J, 0))),
         nscale(-1, nmul(nderivative(H, 1), source_data["vx"])))
Rmix = nadd(nmul(cx, nderivative(Z, 1)),
            nmul(nderivative(W, 0), dy),
            nscale(-1, nmul(cy, nderivative(Z, 0))),
            nscale(-1, nmul(nderivative(W, 1), dx)))
R_by_degree = {degree: nadd(G1_by_degree[degree],
                           degree_part(S, degree),
                           degree_part(Rmix, degree))
               for degree in range(7, 13)}

# Literal integer determinant through the fourth digit.
P0 = {(1, 0): 1, (3, 0): -1}
Q0 = {(0, 1): 1}
P = nadd(P0, nscale(3, source_data["U"]), nscale(9, C),
         nscale(27, W), nscale(81, H))
Q = nadd(Q0, nscale(3, source_data["V"]), nscale(9, D),
         nscale(27, Z), nscale(81, J))
det_minus_one = nadd(
    nmul(nderivative(P, 0), nderivative(Q, 1)),
    nscale(-1, nmul(nderivative(P, 1), nderivative(Q, 0))),
    {(0, 0): -1},
)
direct_by_degree = {}
for degree in range(7, 13):
    direct = divide_exact(degree_part(det_minus_one, degree), 243)
    direct_by_degree[degree] = direct
    assert row(direct, degree) == row(R_by_degree[degree], degree)

rows_descending = [(degree, row(R_by_degree[degree], degree))
                   for degree in range(12, 6, -1)]
first_nonzero = next(((degree, values) for degree, values in rows_descending
                      if any(values)), None)
payload_recursive = bytes(value for _degree, values in rows_descending
                          for value in values)
payload_direct = bytes(value for degree, _values in rows_descending
                       for value in row(direct_by_degree[degree], degree))
assert payload_recursive == payload_direct

print("cumulative_vectors", list(q9_survivor), list(q8_survivor),
      list(q7_zero), list(q6_zero))
print("source_identity",
      "R=G4/3+S(U,V;H,J)+Rmix(C,D;W,Z), where G4 includes div(H,J)")
for degree, values in rows_descending:
    print(f"R{degree}", values)
print("first_nonzero_high_row", first_nonzero)
print("recursive_rows_sha256", hashlib.sha256(payload_recursive).hexdigest())
print("direct_rows_sha256", hashlib.sha256(payload_direct).hexdigest())
print("verdict", "HIGH_CAP_OBSTRUCTED" if first_nonzero else "HIGH_ROWS_ZERO")
print("PASS-Q6-ZERO-NEXT-DIVIDED-HIGH")
