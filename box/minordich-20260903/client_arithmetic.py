#!/usr/bin/env python3
"""Exact arithmetic for the two live u_s>1 clients.

This driver deliberately separates the Definition 5.1 major radii from the
actual minor radius delta*.  Moh's displayed radius-2 pi-root for (99,66) is a
probe for g inside the named minor disc; the text does not identify it as the
general point of the combined-product disc.  All common-polynomial profiles
below are explicitly conditional on having a distribution detector.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction as F
from math import gcd


def text(q: F) -> str:
    return str(q.numerator) if q.denominator == 1 else str(q)


def skeleton(n: int, m: int, mids: list[int], vs: list[int]) -> dict:
    M = [-m] + mids
    s = len(M)
    d = [n]
    for value in M:
        d.append(gcd(d[-1], value))
    V = {i + 2: value for i, value in enumerate(vs)}
    V[s + 1] = d[s]

    def delta(i: int) -> F:
        num = F(n - M[i - 1])
        den = F(n - M[s - 1] - 1)
        for j in range(i + 1, s + 1):
            num *= V[j] * (n - M[j - 1]) - d[j - 1]
            den *= V[j] * (n - M[j - 2]) - d[j - 1]
        return 1 - num / den

    v_top = V[s]
    d_top = d[s - 1]
    u_top = d_top - v_top
    lam = 0
    mus: list[int] = []
    for j, value in enumerate(M):
        qj = value if j == 0 else value - M[j - 1]
        lam += qj * d[j]
        assert lam % d[j] == 0
        mus.append(lam // d[j])
    t_numerators = [u_top * (-mu) for mu in mus[: s - 1]]
    assert all(value % d_top == 0 for value in t_numerators)
    t_degrees = [value // d_top for value in t_numerators]
    return {
        "n": n,
        "m": m,
        "s": s,
        "M_1_to_M_s": M,
        "d_1_to_d_splus1": d,
        "V_2_to_V_s": vs,
        "v_s": v_top,
        "u_s": u_top,
        "v_s_over_u_s": text(F(v_top, u_top)),
        "mu_1_to_mu_s": mus,
        "Def5.1_major_delta_1_to_delta_s": [text(delta(i)) for i in range(1, s + 1)],
        "Prop6.1_minor_floor": ">=1",
        "minor_radius_from_skeleton": None,
        "Prop6.3_if_minor_bound_holds": {
            "pi_degrees_g_then_T_1_to_T_sminus1": [
                u_top * n // d_top,
                *t_degrees,
            ],
            "Jacobian_gamma_exponent": v_top - u_top - 1,
        },
    }


def ord_g_at(row: dict, radius: int) -> int:
    n = row["n"]
    ds, us, vs = row["d_1_to_d_splus1"][-2], row["u_s"], row["v_s"]
    return (n // ds) * (us * radius - vs)


def detector_profile(row: dict) -> dict:
    n = row["n"]
    ds, us = row["d_1_to_d_splus1"][-2], row["u_s"]
    global_degrees = [row["n"]] + [
        -value for value in row["mu_1_to_mu_s"][:-1]
    ]
    global_gcd = 0
    for degree in global_degrees:
        global_gcd = gcd(global_gcd, degree)
    exponents = [degree // global_gcd for degree in global_degrees]
    full_minor_g_multiplicity = us * n // ds
    assert full_minor_g_multiplicity % exponents[0] == 0
    base_degree = full_minor_g_multiplicity // exponents[0]
    local_numerators = [us * degree for degree in global_degrees]
    assert all(value % ds == 0 for value in local_numerators)
    local_degrees = [value // ds for value in local_numerators]
    assert local_degrees == [base_degree * value for value in exponents]
    return {
        "licensing_condition": (
            "common pi-root is a distribution detector for "
            "g,T_1,...,T_sminus1"
        ),
        "global_degrees": global_degrees,
        "global_gcd": global_gcd,
        "full_minor_g_multiplicity_from_Prop6.2": full_minor_g_multiplicity,
        "local_leading_degrees": local_degrees,
        "common_base_degree": base_degree,
        "common_base_powers": exponents,
    }


def main() -> None:
    r99 = skeleton(99, 66, [77, 97], [8, 8])
    r108 = skeleton(108, 72, [81, 106], [7, 7])
    r99.update(
        {
            "actual_minor_radius": None,
            "Prop6.3_status": "UNDETERMINED",
            "p209_radius_2_g_probe": {
                "radius": 2,
                "scope": (
                    "g roots selected in D_2*; not a certified combined-disc "
                    "boundary or common detector"
                ),
                "ord_g_at_probe": ord_g_at(r99, 2),
                "g_leading_degree": 27,
            },
            "conditional_common_detector_check": detector_profile(r99),
            "conditional_if_probe_is_combined_boundary": "FAILS: 2 < 8/3",
            "p209_row_specific_branches": {
                "A": {
                    "profile": "linear power: one distinct g_sigma root",
                    "combined_minor_radius": "UNDETERMINED",
                },
                "B": {
                    "profile": "ninth power of a cubic with two distinct roots: counts 18+9",
                    "combined_minor_radius": "<=2",
                    "Prop6.3_status": "FAILS: delta* <= 2 < 8/3",
                },
            },
        }
    )
    r108.update(
        {
            "actual_minor_radius": None,
            "Prop6.3_status": "UNDETERMINED",
            "conditional_actual_minor_detector_profile": detector_profile(r108),
            "conditional_u2_branches_if_actual_minor_radius_lt_7_over_2": {
                "A": "H has one distinct root; g_sigma is a linear 24th power",
                "B": "H has two distinct roots; g_sigma=H^12 and counts are 12+12",
            },
        }
    )

    assert r99["d_1_to_d_splus1"] == [99, 33, 11, 1]
    assert r99["mu_1_to_mu_s"][:2] == [-66, -55]
    assert r99["Def5.1_major_delta_1_to_delta_s"] == ["4/9", "1/3", "-1"]
    assert r99["p209_radius_2_g_probe"]["ord_g_at_probe"] == -18
    assert r108["d_1_to_d_splus1"] == [108, 36, 9, 1]
    assert r108["mu_1_to_mu_s"][:2] == [-72, -63]
    assert r108["Def5.1_major_delta_1_to_delta_s"] == ["3/8", "1/4", "-1"]
    assert r108["conditional_actual_minor_detector_profile"][
        "common_base_powers"
    ] == [12, 8, 7]
    assert r108["Prop6.3_if_minor_bound_holds"] == {
        "pi_degrees_g_then_T_1_to_T_sminus1": [24, 16, 14],
        "Jacobian_gamma_exponent": 4,
    }
    json.dump({"99_66": r99, "108_72": r108}, fp=sys.stdout,
              indent=2, sort_keys=True)
    print()


if __name__ == "__main__":
    main()
