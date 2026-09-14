#!/usr/bin/env python3
"""Small exact-integer audit for the T2/T3 defect arithmetic and supports."""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent


def lines_hash(values):
    return hashlib.sha256("".join(f"{v}\n" for v in values).encode()).hexdigest()


def arithmetic(n, m, M):
    d = [n]
    seen = [n]
    for value in M:
        seen.append(value)
        d.append(math.gcd(*seen))
    ratios = [d[i] // d[i + 1] for i in range(len(d) - 1)]
    q = [M[0]] + [M[i] - M[i - 1] for i in range(1, len(M))]
    Lambda = []
    running = 0
    for qi, di in zip(q, d):
        running += qi * di
        Lambda.append(running)
    D = [-Lambda[i] // d[i] for i in range(len(M))]
    assert all(Lambda[i] % d[i] == 0 for i in range(len(M)))
    return {"n": n, "m": m, "M": M, "d": d, "n_i": ratios,
            "q": q, "Lambda": Lambda, "D": D}


cases = {
    "99": arithmetic(99, 66, [-66, 77, 97]),
    "108": arithmetic(108, 72, [-72, 81, 106]),
}
for name, row in cases.items():
    n, m = row["n"], row["m"]
    D2, D3 = row["D"][1], row["D"][2]
    M2, M3 = row["M"][1], row["M"][2]
    n2 = row["n_i"][1]
    raw = n + m - 2
    t2_bound = n + D2 - 2
    B2 = 2 * m
    defect = t2_bound - B2
    recursive = n2 * D2 - D3
    physical_t2_depth = row["q"][1]
    assert defect == recursive == row["q"][2]
    assert raw - physical_t2_depth == defect
    B3 = D3 + M3
    t3_bound = n + D3 - 2
    assert B3 == t3_bound
    row.update({
        "raw_J_depth": raw,
        "T2_physical_depth": physical_t2_depth,
        "B2_y_degree": B2,
        "J_F_T2_upper_degree": t2_bound,
        "j_defect_after_T2": defect,
        "recursive_T3_defect": recursive,
        "B3_y_degree": B3,
        "J_F_T3_upper_degree": t3_bound,
        "j_degree_after_T3_if_nonzero": 0,
    })

supports = {
    "99": [
        ["F*G", 0], ["F*T2", 11], ["G^2", 33], ["G*T2", 44],
        ["T2^2", 55], ["F", 66], ["G", 99], ["T2", 110], ["1", 165],
    ],
    "108": [
        ["F*G^2", 0], ["F*G*T2", 9], ["F*T2^2", 18], ["F^2", 36],
        ["G^2*T2", 45], ["G*T2^2", 54], ["T2^3", 63], ["F*G", 72],
        ["F*T2", 81], ["G^2", 108], ["G*T2", 117], ["T2^2", 126],
        ["F", 144], ["G", 180], ["T2", 189], ["1", 252],
    ],
}
assert [x for x in supports["99"] if x[1] <= 20] == [["F*G", 0], ["F*T2", 11]]
assert [x for x in supports["108"] if x[1] <= 25] == [
    ["F*G^2", 0], ["F*G*T2", 9], ["F*T2^2", 18]
]

targets = {
    "99_T2": [0] * 40 + [math.comb(15, i) for i in range(16)],
    "99_T3": [0] * 105 + [math.comb(40, i) for i in range(41)],
    "108_T2": [0] * 49 + [math.comb(14, i) for i in range(15)],
    "108_T3": [0] * 176 + [math.comb(51, i) for i in range(52)],
}

record = {
    "field": "Q",
    "cases": cases,
    "T3_standard_support_by_shift": supports,
    "target_vectors": {
        key: {"slots": len(value), "nonzero": sum(bool(x) for x in value),
              "sha256": lines_hash(value)}
        for key, value in targets.items()
    },
    "derivative_leaders": {
        "99": "9*lambda2^2*(y^3*(y-x)^8)^22; total degree 242",
        "108": "12*lambda2^3*(y^2*(y-x)^7)^37; total degree 333",
    },
    "family_C_conditional_identity": {
        "weight_formula": "w_d(j)=n-M-1-(ell+1)/d",
        "license_condition": "d*(n-M-1)=ell+1",
        "conclusion": "w_d(j)=0",
        "status_without_child_attainment_and_lift": "OPEN",
    },
}
(HERE / "math-audit.json").write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
print(json.dumps(record, indent=2, sort_keys=True))
