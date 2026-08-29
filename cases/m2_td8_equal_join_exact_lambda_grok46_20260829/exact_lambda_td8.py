#!/usr/bin/env python3
"""Finite identities for the td=8 equal-join exact-lambda gate.

This packet certifies recorded AF2 floors, linear-model predictions, the
two rigid Prop. 8.1(iv) extra-orbit ratios, the i-chain, and t-independence
of reduced gaps.  It does not compute kappa_H(pi(H)-1).
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import ceil


SCHEMA = "m2-td8-equal-join-exact-lambda-grok46-r1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def ft(x: Fraction | int) -> str:
    q = Fraction(x)
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def pmul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    r = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r


def padd(*ps: list[Fraction]) -> list[Fraction]:
    n = max(len(p) for p in ps)
    r = [Fraction(0)] * n
    for p in ps:
        for i, x in enumerate(p):
            r[i] += x
    return r


def pscale(a: list[Fraction], c: Fraction) -> list[Fraction]:
    return [x * c for x in a]


def pderiv(a: list[Fraction]) -> list[Fraction]:
    return [a[i] * i for i in range(1, len(a))]


def pshift(a: list[Fraction]) -> list[Fraction]:
    return [Fraction(0)] + list(a)


def ptrim(a: list[Fraction]) -> list[Fraction]:
    while len(a) > 1 and a[-1] == 0:
        a = a[:-1]
    return a


def poly_from_roots(roots: list[tuple[Fraction, int]]) -> list[Fraction]:
    p = [Fraction(1)]
    for val, m in roots:
        lin = [-val, Fraction(1)]
        for _ in range(m):
            p = pmul(p, lin)
    return p


def E_raw(
    pt: list[Fraction], w: list[Fraction], nu: int, rho: Fraction
) -> list[Fraction]:
    t1 = pscale(pmul(pt, w), rho)
    t2 = pscale(pshift(pmul(pt, pderiv(w))), nu * rho)
    t3 = pscale(pshift(pmul(pderiv(pt), w)), -nu)
    return ptrim(padd(t1, t2, t3))


def ode_holds(
    pt: list[Fraction], w: list[Fraction], nu: int, rho: Fraction
) -> Fraction | None:
    E = E_raw(pt, w, nu, rho)
    if len(E) != len(pt) or pt[-1] == 0:
        return None
    ctilde = E[-1] / pt[-1]
    if ctilde == 0:
        return None
    if any(E[i] != ctilde * pt[i] for i in range(len(pt))):
        return None
    return ctilde


def a_step_closed_form(A: Fraction = Fraction(1)) -> dict[str, object]:
    """Family C: p=(t-A)^2(t-B), w=(t-A)(t-B), nu=7, rho=21/15.

    After Cor. 6.1 the t^2 coefficient of E/pt vanishes identically.  The
    t^1 coefficient is A*(-21/5)+B*(14/5), hence B=(3/2)A uniquely.  Then
    ctilde = rho*A*B = (21/10) A^2.
    """
    nu = 7
    rho = Fraction(21, 15)
    t2 = rho + 2 * nu * rho - 3 * nu
    require(t2 == 0, "A-step Cor. 6.1 t^2 identity failed")
    coeff_A = -rho * (1 + nu) + nu
    coeff_B = -rho * (1 + nu) + 2 * nu
    require(coeff_A == Fraction(-21, 5), "A-step t^1 A-coefficient")
    require(coeff_B == Fraction(14, 5), "A-step t^1 B-coefficient")
    require(coeff_A + coeff_B * Fraction(3, 2) == 0, "A-step ratio does not cancel t^1")
    B = Fraction(3, 2) * A
    require(B != A and B != 0, "A-step extra coincides with continuation or 0")
    ctilde = rho * A * B
    require(ctilde == Fraction(21, 10) * A * A, "A-step constant term")
    pt = poly_from_roots([(A, 2), (B, 1)])
    w = poly_from_roots([(A, 1), (B, 1)])
    c_chk = ode_holds(pt, w, nu, rho)
    require(c_chk == ctilde, "A-step polynomial ODE failed at the closed form")
    return {
        "nu": nu,
        "rho": ft(rho),
        "A": ft(A),
        "B": ft(B),
        "ratio_B_over_A": "3/2",
        "ctilde": ft(ctilde),
    }


def trunk_closed_form(C: Fraction = Fraction(1)) -> dict[str, object]:
    """Trunk: p=(t-C)^3(t-D)^2, w=(t-C)(t-D), nu=17, rho=85/35.

    t^2 coefficient of E/pt is rho+2*nu*rho-5*nu=0.  t^1 coefficient is
    C*(-68/7)+D*(51/7), hence D=(4/3)C uniquely.  Then
    ctilde = rho*C*D = (68/21) C^2.
    """
    nu = 17
    rho = Fraction(85, 35)
    t2 = rho + 2 * nu * rho - 5 * nu
    require(t2 == 0, "trunk Cor. 6.1 t^2 identity failed")
    coeff_C = -rho * (1 + nu) + 2 * nu
    coeff_D = -rho * (1 + nu) + 3 * nu
    require(coeff_C == Fraction(-68, 7), "trunk t^1 C-coefficient")
    require(coeff_D == Fraction(51, 7), "trunk t^1 D-coefficient")
    require(coeff_C + coeff_D * Fraction(4, 3) == 0, "trunk ratio does not cancel t^1")
    D = Fraction(4, 3) * C
    require(D != C and D != 0, "trunk extra coincides with continuation or 0")
    ctilde = rho * C * D
    require(ctilde == Fraction(68, 21) * C * C, "trunk constant term")
    pt = poly_from_roots([(C, 3), (D, 2)])
    w = poly_from_roots([(C, 1), (D, 1)])
    c_chk = ode_holds(pt, w, nu, rho)
    require(c_chk == ctilde, "trunk polynomial ODE failed at the closed form")
    return {
        "nu": nu,
        "rho": ft(rho),
        "C": ft(C),
        "D": ft(D),
        "ratio_D_over_C": "4/3",
        "ctilde": ft(ctilde),
    }


def recorded_floors() -> dict[str, object]:
    # Incoming (21,15): unique extra of reduced multiplicity 1.
    X_A, kbar_A, m_A = 7, 5, 1
    gap_A = Fraction(X_A, m_A) - kbar_A
    floor_A = max(1, ceil(gap_A))
    require(gap_A == 2, "A-step gap is not 2")
    require(floor_A == 2, "A-step AF2 floor is not 2")
    require(gap_A.denominator == 1, "A-step linear prediction is not integral")

    # Trunk (85,35): unique extra of reduced multiplicity 2.
    X_F, kbar_F, m_F = 17, 7, 2
    gap_F = Fraction(X_F, m_F) - kbar_F
    floor_F = max(1, ceil(gap_F))
    wrong_simple = max(1, ceil(X_F - kbar_F))
    require(gap_F == Fraction(3, 2), "trunk general gap is not 3/2")
    require(floor_F == 2, "trunk AF2 floor is not 2")
    require(wrong_simple == 10, "simple-orbit X-kbar ceiling is not 10")
    require(gap_F.denominator == 2, "trunk linear prediction is integral")

    psi = 1
    budget = 8 - 1 - psi
    recorded_sum = 2 + 2 + 0 + 2
    require(recorded_sum == budget == 6, "recorded budget equality failed")
    return {
        "A_step": {
            "dp_dq": [21, 15],
            "X": X_A,
            "kbar": kbar_A,
            "m_extra": m_A,
            "gap_linear": ft(gap_A),
            "af2_floor": floor_A,
            "linear_in_N": True,
        },
        "trunk": {
            "dp_dq": [85, 35],
            "X": X_F,
            "kbar": kbar_F,
            "m_extra": m_F,
            "gap_linear": ft(gap_F),
            "af2_floor": floor_F,
            "simple_orbit_ceiling": wrong_simple,
            "linear_in_N": False,
        },
        "merge_p2_exact": 0,
        "recorded_sum": recorded_sum,
        "td_minus_1_minus_psi": budget,
    }


def i_chain(t: int) -> dict[str, object]:
    require(isinstance(t, int) and t >= 0, "t must be a nonnegative integer")
    deg_pole = 4
    l_A = 2
    require(deg_pole % l_A == 0, "pole degree not divisible by A-arrival")
    i_A = deg_pole // l_A
    require(i_A == 2, "i_A is not 2")
    full_A = i_A * 21
    require(full_A == 42, "full A-step degree is not 42")
    mu_G = 3
    require(full_A % mu_G == 0, "A-step full degree not divisible by merge mu")
    i_G = full_A // mu_G
    require(i_G == 14, "i_G is not 14")
    nu_G = 4 + 3 * t
    dp_G = 6 * nu_G
    full_G = i_G * dp_G
    l_F = 3
    require(full_G % l_F == 0, "merge full degree not divisible by trunk l")
    i_F = full_G // l_F
    require(i_F == 28 * (4 + 3 * t), "i_F closed form failed")
    X_A, X_F = 7, 17
    require(Fraction(i_A * X_A, i_A * 1) == 7, "A-step D/(i m) failed")
    require(Fraction(i_F * X_F, i_F * 2) == Fraction(17, 2), "trunk D/(i m) t-dependence")
    n_arr = 7 * (6 + 4 * t) - 5
    n_tr = nu_G * 7 - (6 + 4 * t)
    require(n_arr == 37 + 28 * t, "incoming label")
    require(n_tr == 22 + 17 * t, "trunk label")
    return {
        "t": t,
        "i_A": i_A,
        "i_G": i_G,
        "i_F": i_F,
        "nu_G": nu_G,
        "D_over_im_A": 7,
        "D_over_im_trunk": "17/2",
        "n_arr": n_arr,
        "n_trunk": n_tr,
    }


def mp1_two_extras_independent() -> dict[str, object]:
    """m=2 forces exactly one 2-ary merge, so extra branches cannot reconverge."""
    m = 2
    merge_excess = m - 1
    require(merge_excess == 1, "MP1 for m=2 is not one 2-ary merge")
    return {
        "m": m,
        "sum_r_minus_1": merge_excess,
        "shared_first_separation_forbidden_by_MP1": True,
        "extra_is_not_merge_arrival": True,
        "A_extra_ratio": "3/2",
        "merge_orbit_ratio": "-1",
    }


def uniqueness_scan_A(A: Fraction = Fraction(1), bound: int = 12) -> int:
    hits = []
    for num in range(-bound, bound + 1):
        for den in range(1, bound + 1):
            B = Fraction(num, den)
            if B in (0, A):
                continue
            pt = poly_from_roots([(A, 2), (B, 1)])
            w = poly_from_roots([(A, 1), (B, 1)])
            c = ode_holds(pt, w, 7, Fraction(21, 15))
            if c is not None:
                hits.append(B)
    uniq = set(hits)
    require(uniq == {Fraction(3, 2) * A}, f"A-step uniqueness failed: {uniq}")
    return len(hits)


def uniqueness_scan_trunk(C: Fraction = Fraction(1), bound: int = 12) -> int:
    hits = []
    for num in range(-bound, bound + 1):
        for den in range(1, bound + 1):
            D = Fraction(num, den)
            if D in (0, C):
                continue
            pt = poly_from_roots([(C, 3), (D, 2)])
            w = poly_from_roots([(C, 1), (D, 1)])
            c = ode_holds(pt, w, 17, Fraction(85, 35))
            if c is not None:
                hits.append(D)
    uniq = set(hits)
    require(uniq == {Fraction(4, 3) * C}, f"trunk uniqueness failed: {uniq}")
    return len(hits)


def certificate() -> dict[str, object]:
    floors = recorded_floors()
    a_form = a_step_closed_form(Fraction(1))
    a_form2 = a_step_closed_form(Fraction(2))
    tr_form = trunk_closed_form(Fraction(1))
    tr_form2 = trunk_closed_form(Fraction(3))
    chains = [i_chain(t) for t in (0, 1, 2, 10, 100)]
    mp1 = mp1_two_extras_independent()
    nA = uniqueness_scan_A()
    nT = uniqueness_scan_trunk()
    cert = {
        "schema": SCHEMA,
        "verdict": "PARTIAL",
        "exact_lambda_two_proved": False,
        "route_killed_by_strict_lambda": False,
        "configuration_realizable": False,
        "source_landing": False,
        "jc2": False,
        "floors": floors,
        "A_step_ratio": a_form,
        "A_step_ratio_scale_2": a_form2,
        "trunk_ratio": tr_form,
        "trunk_ratio_scale_3": tr_form2,
        "i_chain_samples": chains,
        "mp1": mp1,
        "uniqueness_A_hits": nA,
        "uniqueness_trunk_hits": nT,
        "linear_model": {
            "A_step_predicts": 2,
            "A_step_compatible_with_St94_integrality": True,
            "trunk_predicts": "3/2",
            "trunk_compatible_with_St94_integrality": False,
            "equality_in_St93_not_proved": True,
        },
    }
    blob = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
    digest = hashlib.sha256(blob).hexdigest()
    cert["certificate_sha256"] = digest
    return cert


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    cert = certificate()
    if args.json:
        print(json.dumps(cert, sort_keys=True, separators=(",", ":")))
        return
    print("TD8_EXACT_LAMBDA_GROK46_CERT")
    print("verdict", cert["verdict"])
    print("A_gap", cert["floors"]["A_step"]["gap_linear"])
    print("trunk_gap", cert["floors"]["trunk"]["gap_linear"])
    print("A_ratio", cert["A_step_ratio"]["ratio_B_over_A"])
    print("trunk_ratio", cert["trunk_ratio"]["ratio_D_over_C"])
    print("certificate_sha256", cert["certificate_sha256"])


if __name__ == "__main__":
    main()
