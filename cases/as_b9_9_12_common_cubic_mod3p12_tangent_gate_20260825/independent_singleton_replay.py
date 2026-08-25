#!/usr/bin/env python3
"""Independent literal replay of the singleton x^2*y^2 obstruction."""

from __future__ import annotations

import hashlib
import json
import os
import platform
from pathlib import Path


assert platform.system() == "Linux", "AWS-only replay refuses non-Linux host"
job_tag = os.environ.get("AWS_JOB_TAG", "")
assert job_tag.startswith("as_b9_common_cubic_mod3p12_replay_"), job_tag

OLD = 3 ** 11
NEW = 3 ** 12
witness_path = Path(os.environ["WITNESS_JSON"])
witness_bytes = witness_path.read_bytes()
assert hashlib.sha256(witness_bytes).hexdigest() == os.environ[
    "EXPECTED_WITNESS_SHA256"]
witness = json.loads(witness_bytes)
P0 = {tuple(entry[:2]): int(entry[2])
      for entry in witness["P_support_mod177147"]}
Q0 = {tuple(entry[:2]): int(entry[2])
      for entry in witness["Q_support_mod177147"]}
support_p = [(i, degree - i) for degree in range(10)
             for i in range(degree + 1)]
support_q = [(i, degree - i) for degree in range(13)
             for i in range(degree + 1)]


def deriv(poly, axis):
    answer = {}
    for (i, j), coefficient in poly.items():
        exponent = i if axis == 0 else j
        if exponent:
            xy = (i - 1, j) if axis == 0 else (i, j - 1)
            answer[xy] = answer.get(xy, 0) + exponent * coefficient
    return answer


def coefficient_of_product(left, right, target):
    return sum(a * right.get((target[0] - i, target[1] - j), 0)
               for (i, j), a in left.items())


def row22(P, Q):
    Px, Py = deriv(P, 0), deriv(P, 1)
    Qx, Qy = deriv(Q, 0), deriv(Q, 1)
    return (coefficient_of_product(Px, Qy, (2, 2))
            - coefficient_of_product(Py, Qx, (2, 2)))


base = row22(P0, Q0)
assert base % OLD == 0
assert base % NEW != 0
base_divided_mod3 = (base // OLD) % 3
assert base_divided_mod3 == 1

effects = []
for owner, support in (("P", support_p), ("Q", support_q)):
    for xy in support:
        P = dict(P0)
        Q = dict(Q0)
        target = P if owner == "P" else Q
        target[xy] = target.get(xy, 0) + OLD
        effect = ((row22(P, Q) - base) // OLD) % 3
        effects.append([owner, *xy, effect])
assert len(effects) == 146
assert all(entry[-1] == 0 for entry in effects)
# H does not enter the determinant; record its three zero columns explicitly.
effects.extend([["H", index, 0, 0] for index in range(1, 4)])
assert len(effects) == 149
assert OLD * OLD % NEW == 0

result = {
    "status": "PASS-AS-B9-COMMON-CUBIC-MOD3P12-SINGLETON-REPLAY",
    "aws_job_tag": job_tag,
    "witness_sha256": hashlib.sha256(witness_bytes).hexdigest(),
    "row": ["det", 2, 2],
    "base_integer_coefficient": base,
    "base_div3p11_mod3": base_divided_mod3,
    "fresh_column_count": len(effects),
    "all_fresh_columns_zero_mod3": True,
    "fresh_fresh_terms_zero_mod3p12": True,
    "effects": effects,
    "scope": "one literal witness and one determinant coefficient",
    "refusal_scope": [
        "not the complete mod3^11 family or common-cubic locus",
        "not all-depth, maximum12, counterexample, or JC2",
    ],
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("row_base_div3p11_mod3", base_divided_mod3)
print("fresh_zero_columns", len(effects))
print("result_sha256", hashlib.sha256(encoded).hexdigest())
print(result["status"])
