#!/usr/bin/env python3
"""Source-independent literal verifier for the B9 common-cubic witness."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path


MODULUS = 3 ** 11
PARENT_MODULUS = 3 ** 5
source = Path(os.environ["WITNESS_JSON"])
payload = source.read_bytes()
assert hashlib.sha256(payload).hexdigest() == os.environ["EXPECTED_SHA256"]
witness = json.loads(payload)


def clean(poly, modulus=None):
    answer = {}
    for xy, value in poly.items():
        if modulus is not None:
            value %= modulus
        if value:
            answer[xy] = value
    return answer


def add(*polys):
    answer = {}
    for poly in polys:
        for xy, value in poly.items():
            answer[xy] = answer.get(xy, 0) + value
    return clean(answer)


def scale(scalar, poly):
    return clean({xy: scalar * value for xy, value in poly.items()})


def mul(left, right):
    answer = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            xy = (i + k, j + ell)
            answer[xy] = answer.get(xy, 0) + a * b
    return clean(answer)


def power(poly, exponent):
    answer = {(0, 0): 1}
    for _ in range(exponent):
        answer = mul(answer, poly)
    return answer


def deriv(poly, axis):
    answer = {}
    for (i, j), value in poly.items():
        exponent = i if axis == 0 else j
        if exponent:
            xy = (i - 1, j) if axis == 0 else (i, j - 1)
            answer[xy] = answer.get(xy, 0) + exponent * value
    return clean(answer)


def jac(left, right):
    return add(mul(deriv(left, 0), deriv(right, 1)),
               scale(-1, mul(deriv(left, 1), deriv(right, 0))))


def convolution(left, right):
    answer = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            answer[i + j] += a * b
    return answer


P = {(i, j): value for i, j, value in witness["P_support_mod177147"]}
Q = {(i, j): value for i, j, value in witness["Q_support_mod177147"]}
H = list(witness["H_coefficients_mod177147"])
assert H[0] == 1 and all(value % 3 == 0 for value in H[1:])
assert max(sum(xy) for xy in P) == 9
assert max(sum(xy) for xy in Q) == 12
assert all(sum(xy) <= 9 for xy in P)
assert all(sum(xy) <= 12 for xy in Q)

determinant = jac(P, Q)
determinant_mod = clean(determinant, MODULUS)
assert determinant_mod == {(0, 0): 1}

h2 = convolution(H, H)
h3 = convolution(h2, H)
h4 = convolution(h3, H)
ptop = [P.get((i, 9 - i), 0) for i in range(10)]
qtop = [Q.get((i, 12 - i), 0) for i in range(13)]
assert ptop[0] % 3 and qtop[0] % 3
assert all((value - ptop[0] * coefficient) % MODULUS == 0
           for value, coefficient in zip(ptop, h3))
assert all((value - qtop[0] * coefficient) % MODULUS == 0
           for value, coefficient in zip(qtop, h4))

# Fixed-parent check from the displayed integer B9 formula, independent of
# every parent/compiler source file.
x = {(1, 0): 1}
y = {(0, 1): 1}
u = add(x, power(y, 3))
parent_p = add(u, scale(-1, power(u, 3)), scale(18, mul(u, y)),
               scale(81, add(scale(2, mul(u, y)), mul(x, power(y, 2)))))
parent_q = add(y, power(u, 4), scale(3, mul(power(u, 2), y)),
               scale(72, power(y, 2)),
               scale(81, add(power(y, 2), mul(power(x, 4), power(y, 2)),
                             mul(x, power(y, 11)))))
assert clean(P, PARENT_MODULUS) == clean(parent_p, PARENT_MODULUS)
assert clean(Q, PARENT_MODULUS) == clean(parent_q, PARENT_MODULUS)

result = {
    "status": "PASS-AS-B9-COMMON-CUBIC-INDEPENDENT-WITNESS-REPLAY",
    "witness_sha256": os.environ["EXPECTED_SHA256"],
    "modulus": MODULUS,
    "determinant_rows_zero_except_constant_one": True,
    "determinant_support_size_before_reduction": len(determinant),
    "top_form_rows": 23,
    "common_cubic_rows_passed": True,
    "leading_units_mod3": [ptop[0] % 3, qtop[0] % 3],
    "H_coefficients_mod177147": H,
    "degrees_total": [max(sum(xy) for xy in P), max(sum(xy) for xy in Q)],
    "fixed_displayed_B9_parent_mod243": True,
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print(json.dumps(result, sort_keys=True))
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
