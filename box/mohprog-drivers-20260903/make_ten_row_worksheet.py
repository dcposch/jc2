#!/usr/bin/env python3
"""Create a deterministic ten-row arithmetic worksheet for (1)--(13)."""

from __future__ import annotations

import json
from fractions import Fraction
from math import gcd
from pathlib import Path

import independent_enumerator as E


HERE = Path(__file__).resolve().parent

PRINTED = [
    (64, 48, (52, 62), ((2, 3), (3, 3)), "printed (64,48)"),
    (84, 56, (64, 82), ((2, 2), (3, 3)), "printed (84,56), M2=64"),
    (84, 56, (72, 82), ((2, 5), (3, 3)), "printed (84,56), M2=72"),
    (75, 50, (55, 73), ((2, 3), (3, 4)), "printed (75,50), V2=3"),
    (75, 50, (55, 73), ((2, 2), (3, 4)), "printed (75,50), V2=2"),
    (99, 66, (77, 97), ((2, 8), (3, 8)), "printed (99,66)"),
]


def f(value):
    return E.frac_text(value if isinstance(value, Fraction) else Fraction(value, 1))


def row_key(record):
    return (
        record["n"], record["m"], tuple(record["M"]),
        tuple(sorted((int(k), value) for k, value in record["V"].items())),
    )


def reconstruct(record):
    n, m = record["n"], record["m"]
    Ms = tuple(record["M"])
    V = {int(k): value for k, value in record["V"].items()}
    s = len(Ms) + 1
    M = {1: -m, **{i + 2: value for i, value in enumerate(Ms)}}
    d = {1: n}
    for r in range(2, s + 2):
        d[r] = gcd(d[r - 1], M[r - 1])
    V[s + 1] = d[s + 1]
    return n, m, Ms, M, V, d, s


def delta_formula(n, M, V, d, s, i):
    factors = []
    num = n - M[i]
    den = n - M[s] - 1
    for j in range(i + 1, s + 1):
        top = V[j] * (n - M[j]) - d[j]
        bottom = V[j] * (n - M[j - 1]) - d[j]
        factors.append({"j": j, "numerator": top, "denominator": bottom})
        num *= top
        den *= bottom
    one_minus = Fraction(num, den)
    return {
        "i": i,
        "n_minus_Mi": n - M[i],
        "normalizer_n_minus_Ms_minus_1": n - M[s] - 1,
        "factors": factors,
        "raw_ratio_numerator": num,
        "raw_ratio_denominator": den,
        "one_minus_delta": f(one_minus),
        "delta": f(1 - one_minus),
        "reduced_denominator": (1 - one_minus).denominator,
    }


def details(record, label):
    n, m, Ms, M, V, d, s = reconstruct(record)
    Vshort = {i: V[i] for i in range(2, s + 1)}
    delta = E.radii(n, m, Ms, Vshort, d)
    L, A = E.increment_data(delta, s)

    c5 = []
    for r in range(2, s + 2):
        prefix = [n] + [M[i] for i in range(1, r)]
        c5.append({"r": r, "gcd_inputs": prefix, "computed_gcd": gcd(*prefix), "d_r": d[r],
                   "pass": gcd(*prefix) == d[r]})

    c7 = []
    for r in range(2, s + 1):
        lo = Fraction(d[r], n - M[r])
        hi = Fraction(V[r + 1] * d[r], d[r + 1])
        c7.append({
            "r": r, "lower_d_r_over_n_minus_M_r": f(lo), "V_r": V[r],
            "upper_V_next_d_r_over_d_next": f(hi),
            "strict_lower_pass": V[r] > lo, "weak_upper_pass": V[r] <= hi,
        })

    c8 = {
        "delta_formula": [delta_formula(n, M, V, d, s, i) for i in range(s, 0, -1)],
        "increments": [
            {"j": j, "denominators_delta_s_through_delta_jplus1":
             [delta[i].denominator for i in range(s, j, -1)],
             "L_j": L[j], "L_j_times_delta_j": f(L[j] * delta[j]), "A_j": A[j]}
            for j in range(s - 1, 0, -1)
        ],
    }

    c9to11 = []
    for j in range(s - 1, 1, -1):
        q_num = V[j + 1] * d[j]
        q_den = d[j + 1]
        assert q_num % q_den == 0
        Q = q_num // q_den
        tri, square = divmod(Q, A[j])
        by10 = V[j] <= tri
        by11 = (V[j] - square) % A[j] == 0
        ell = (V[j] - square) // A[j] if by11 else None
        c9to11.append({
            "r": j + 1, "level_j_equals_r_minus_1": j,
            "Q_numerator_V_r_times_d_prev": q_num, "Q_denominator_d_r": q_den, "Q": Q,
            "A_j": A[j], "triangle": tri, "square": square,
            "division_identity": f"{Q} = {tri}*{A[j]} + {square}",
            "division_identity_pass": Q == tri * A[j] + square and 0 <= square < A[j],
            "V_j": V[j], "condition_10_V_j_le_triangle": by10,
            "condition_11_congruence": by11, "condition_11_integer_multiplier": ell,
            "condition_10_or_11": by10 or by11,
        })

    A1 = A[1]
    ns, ms, v2 = n // d[2], m // d[2], V[2]
    vals = {
        "n_star": ns, "m_star": ms, "V_2": v2, "A_1": A1,
        "condition_12_first": ns * v2,
        "condition_12_first_remainder": (ns * v2) % A1,
        "condition_12_second": ms * v2 - 1,
        "condition_12_second_remainder": (ms * v2 - 1) % A1,
        "condition_12": ns * v2 % A1 == 0 and (ms * v2 - 1) % A1 == 0,
        "condition_13_first": ms * v2,
        "condition_13_first_remainder": (ms * v2) % A1,
        "condition_13_second": ns * v2 - 1,
        "condition_13_second_remainder": (ns * v2 - 1) % A1,
        "condition_13": ms * v2 % A1 == 0 and (ns * v2 - 1) % A1 == 0,
        "p188_identity_value": (ns + ms) * v2 - 1,
        "p188_identity_remainder": ((ns + ms) * v2 - 1) % A1,
    }

    actual_c4 = "UNVERIFIED: tuple arithmetic cannot prove that these are characteristic data of an actual (f,g)"
    pass_arithmetic = (
        m == -M[1] and m < n <= 100 and n % m != 0 and M[s] == n - 2
        and all(x["pass"] for x in c5) and 3 <= s <= 5 and d[s] >= 4
        and all(x["strict_lower_pass"] and x["weak_upper_pass"] for x in c7)
        and all(x["condition_10_or_11"] for x in c9to11)
        and (vals["condition_12"] or vals["condition_13"])
    )
    return {
        "selection_label": label,
        "row": {"n": n, "m": m, "M": [M[i] for i in range(1, s + 1)],
                "V": {str(i): V[i] for i in range(2, s + 1)}, "s": s},
        "condition_1": {"m_equals_minus_M1": m == -M[1], "m_lt_n_le_100": m < n <= 100},
        "condition_2": {"n_mod_m": n % m, "m_does_not_divide_n": n % m != 0,
                        "M_s": M[s], "n_minus_2": n - 2, "M_s_pass": M[s] == n - 2},
        "condition_3": "UNVERIFIED premise: J(f,g)=1 and simultaneous degree irreducibility are not tuple-arithmetic properties",
        "condition_4": {"numeric_order_shadow": all(M[i] < M[i + 1] for i in range(1, s)),
                        "actual_characteristic_data_status": actual_c4},
        "condition_5": c5,
        "condition_6": {"s": s, "three_le_s_le_five": 3 <= s <= 5, "d_s": d[s], "d_s_ge_4": d[s] >= 4},
        "condition_7": c7,
        "condition_8": c8,
        "conditions_9_10_11": c9to11,
        "conditions_12_13_and_p188": vals,
        "arithmetic_verdict": pass_arithmetic,
    }


def markdown(rows):
    out = [
        "# Deterministic ten-row (1)--(13) arithmetic worksheet",
        "",
        "Selection rule: all six p.202 printed rows, followed by the lexicographically first excess row at each observed length s=3,4,5, followed by the lexicographically last excess row. The independent 658-row JSON is sorted by `(n,m,M,V)`.",
        "",
        "Scope warning: conditions (3) and the actual-realizability content of (4) cannot be checked from an integer tuple. Every `PASS` below is therefore an arithmetic-skeleton pass, not a proof that a polynomial pair exists.",
        "",
    ]
    for idx, R in enumerate(rows, 1):
        row = R["row"]
        out += [f"## {idx}. {R['selection_label']}", "",
                f"Tuple: `n={row['n']}, m={row['m']}, M={row['M']}, V={row['V']}, s={row['s']}`.", "",
                f"(1): `m=-M1`={R['condition_1']['m_equals_minus_M1']}; `m<n<=100`={R['condition_1']['m_lt_n_le_100']}.  "
                f"(2): `n mod m={R['condition_2']['n_mod_m']}`; `m∤n`={R['condition_2']['m_does_not_divide_n']}; "
                f"`Ms=n-2={R['condition_2']['n_minus_2']}`={R['condition_2']['M_s_pass']}.", "",
                f"(3): {R['condition_3']}  ",
                f"(4): ordered numeric shadow={R['condition_4']['numeric_order_shadow']}; {R['condition_4']['actual_characteristic_data_status']}.", "",
                "(5) gcd chain: " + "; ".join(
                    f"d{x['r']}=gcd{x['gcd_inputs']}={x['computed_gcd']} ({x['pass']})" for x in R["condition_5"]
                ) + ".", "",
                f"(6): `s={R['condition_6']['s']}` in [3,5]={R['condition_6']['three_le_s_le_five']}; "
                f"`d_s={R['condition_6']['d_s']}>=4`={R['condition_6']['d_s_ge_4']}.", "",
                "(7) windows:", "",
                "| r | lower | V_r | upper | strict/weak pass |", "|---:|---:|---:|---:|:---:|",
        ]
        out += [f"| {x['r']} | {x['lower_d_r_over_n_minus_M_r']} | {x['V_r']} | {x['upper_V_next_d_r_over_d_next']} | {x['strict_lower_pass']}/{x['weak_upper_pass']} |" for x in R["condition_7"]]
        out += ["", "(8) radii (the JSON contains every raw product factor): " + "; ".join(
            f"delta_{x['i']}={x['delta']} (den {x['reduced_denominator']}, 1-delta={x['one_minus_delta']}, raw {x['raw_ratio_numerator']}/{x['raw_ratio_denominator']})"
            for x in R["condition_8"]["delta_formula"]
        ) + ".", "",
        "(8) denominator increments: " + "; ".join(
            f"j={x['j']}: den-list={x['denominators_delta_s_through_delta_jplus1']}, L={x['L_j']}, L*delta={x['L_j_times_delta_j']}, A={x['A_j']}"
            for x in R["condition_8"]["increments"]
        ) + ".", "",
        "(9)--(11):", "",
        "| r/j | Q division | V_j | (10) | (11), multiplier | union |", "|:---:|:---|---:|:---:|:---:|:---:|",
        ]
        out += [f"| {x['r']}/{x['level_j_equals_r_minus_1']} | {x['division_identity']} | {x['V_j']} | {x['condition_10_V_j_le_triangle']} | {x['condition_11_congruence']}, {x['condition_11_integer_multiplier']} | {x['condition_10_or_11']} |" for x in R["conditions_9_10_11"]]
        z = R["conditions_12_13_and_p188"]
        out += ["", f"(12)/(13): `A1={z['A_1']}, n*={z['n_star']}, m*={z['m_star']}, V2={z['V_2']}`. "
                f"(12) tests `{z['condition_12_first']} mod A1={z['condition_12_first_remainder']}`, "
                f"`{z['condition_12_second']} mod A1={z['condition_12_second_remainder']}` => {z['condition_12']}. "
                f"(13) tests `{z['condition_13_first']} mod A1={z['condition_13_first_remainder']}`, "
                f"`{z['condition_13_second']} mod A1={z['condition_13_second_remainder']}` => {z['condition_13']}. "
                f"p.188 check: `{z['p188_identity_value']} mod A1={z['p188_identity_remainder']}`.", "",
                f"Arithmetic-skeleton verdict: **{'PASS' if R['arithmetic_verdict'] else 'FAIL'}**.", ""]
    return "\n".join(out) + "\n"


def main():
    records = json.loads((HERE / "independent-n100-rows.json").read_text())
    bykey = {row_key(record): record for record in records}
    printed_keys = {(n, m, Ms, V) for n, m, Ms, V, _ in PRINTED}
    chosen = [(bykey[(n, m, Ms, V)], label) for n, m, Ms, V, label in PRINTED]

    excess = sorted((record for record in records if row_key(record) not in printed_keys), key=row_key)
    for s in (3, 4, 5):
        record = next(record for record in excess if len(record["M"]) + 1 == s)
        chosen.append((record, f"first lexicographic excess with s={s}"))
    chosen.append((excess[-1], "last lexicographic excess"))

    rows = [details(record, label) for record, label in chosen]
    assert len(rows) == 10 and all(row["arithmetic_verdict"] for row in rows)
    (HERE / "ten-row-worksheet.json").write_text(json.dumps({"selection_rule": "six printed + first excess at s=3,4,5 + last excess", "rows": rows}, indent=2, sort_keys=True) + "\n")
    (HERE / "ten-row-worksheet.md").write_text(markdown(rows))
    print("wrote ten-row-worksheet.json and ten-row-worksheet.md; 10/10 arithmetic PASS")


if __name__ == "__main__":
    main()
