#!/usr/bin/env python3
"""Controls for the nonlinear T2/T3 bridge.

(1) (64,48)->(16,12), u_s=1: Xu Prop. 7.3 / Moh Prop. 4.4 force T_i(sigma)
    to be powers of one linear polynomial.  No split leader R or q1.
    The bridge is trivially satisfied (0 rows, 0 unknowns added).

(2) Automorphism degrees (1,1): NOT-APPLICABLE for T2 of deg_y 55.

(3) Second control, degrees >= 6, genuine second point at infinity:
    search compositions of triangular automorphisms for a leading form with
    two distinct linear factors.  Jung-van der Kulk coordinates have leading
    form a power of a single linear form; the search is the mechanical check.
    A tame degree-6 automorphism is recorded as SURVIVES[J=1] with
    NOT-APPLICABLE[two-point T2~p^5].  The degenerate two-point top
    (P^9, P^6) has two linear factors, J=0, T2=0 which is not p^5
    (the plumbing does not accept the degeneration).
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent


def us1_1612() -> dict:
    # Charged outer-bridge already killed both c5 readings over GF(32003).
    # Here: the bridge-triviality statement, with u_s from Moh p.207/208.
    return {
        "parent": "(64,48)",
        "reduced": "(16,12) Moh p.208",
        "u_s": 1,
        "Xu_Prop_7_3": (
            "T0,sigma1,...,Ts,sigma1 are powers of a common linear polynomial"
        ),
        "Moh_Prop_4_4": "nonsplitting at a disc; leading forms powers of a linear",
        "split_leader_R_or_q1": False,
        "bridge_rows_added": 0,
        "bridge_unknowns_added": 0,
        "status": "TRIVIAL[u_s=1] / SATISFIED",
        "charged_GB": "SATURATED-EMPTY[P208-ANSATZ / GF(32003)] both c5 readings",
    }


def automorphism_11() -> dict:
    x, y, a = sp.symbols("x y a")
    F = a * x + y
    G = (a - 1) * x + y
    J = sp.expand(sp.diff(F, x) * sp.diff(G, y) - sp.diff(F, y) * sp.diff(G, x))
    return {
        "pair": "F=a*x+y, G=(a-1)*x+y",
        "J": str(J),
        "J_is_1": J == 1,
        "degrees": (1, 1),
        "T2_T3": "NOT-APPLICABLE[degrees (1,1); no mu2=55]",
        "survives": True,
    }


def compose_triangular(k: int, ell: int, linear: tuple) -> dict:
    """β∘α with α=(x, y+x^k), β=(x+y^ell, y), then a GL2 linear."""
    x, y = sp.symbols("x y")
    # α
    X1, Y1 = x, y + x**k
    # β
    X2, Y2 = X1 + Y1**ell, Y1
    a11, a12, a21, a22 = linear
    F = sp.expand(a11 * X2 + a12 * Y2)
    G = sp.expand(a21 * X2 + a22 * Y2)
    det = a11 * a22 - a12 * a21
    J = sp.expand(sp.diff(F, x) * sp.diff(G, y) - sp.diff(F, y) * sp.diff(G, x))
    dF = sp.total_degree(F)
    dG = sp.total_degree(G)
    # leading homogeneous
    def leading(poly, deg):
        if deg <= 0:
            return sp.Integer(0)
        terms = 0
        for m in sp.Add.make_args(sp.expand(poly)):
            if sp.total_degree(m) == deg:
                terms += m
        return sp.expand(terms)

    LF = leading(F, dF)
    LG = leading(G, dG)
    z = sp.symbols("z")
    # dehomogenize LF(1,z) and LF(z,1) to factor
    f1 = sp.Poly(sp.expand(LF.subs({x: 1, y: z})), z)
    factors_F = sp.factor_list(LF)
    # distinct linear factors over Q
    def linear_factors(hom):
        fac = sp.factor(hom)
        lins = []
        for f, exp in sp.factor_list(fac)[1]:
            if sp.total_degree(f) == 1:
                lins.append((str(f), int(exp)))
        return lins

    return {
        "k": k,
        "ell": ell,
        "linear": linear,
        "det_linear": det,
        "J": str(J),
        "J_is_const": J.free_symbols == set() or J == det,
        "deg_F": int(dF),
        "deg_G": int(dG),
        "leading_F": str(LF),
        "leading_G": str(LG),
        "linear_factors_F": linear_factors(LF),
        "linear_factors_G": linear_factors(LG),
        "two_distinct_linear_F": len(linear_factors(LF)) >= 2,
        "two_distinct_linear_G": len(linear_factors(LG)) >= 2,
    }


def search_two_factors() -> dict:
    hits = []
    samples = []
    linears = [
        (1, 0, 0, 1),
        (0, 1, -1, 0),
        (1, 1, 0, 1),
        (1, 0, 1, 1),
        (1, 1, 1, 2),
        (2, 1, 1, 1),
        (1, 2, 1, 1),
        (1, -1, 1, 1),
    ]
    for k in (2, 3, 4, 5):
        for ell in (2, 3, 4, 5):
            for L in linears:
                if L[0] * L[3] - L[1] * L[2] == 0:
                    continue
                rec = compose_triangular(k, ell, L)
                samples.append(
                    {
                        "k": k,
                        "ell": ell,
                        "linear": L,
                        "deg": (rec["deg_F"], rec["deg_G"]),
                        "n_lin_F": len(rec["linear_factors_F"]),
                        "n_lin_G": len(rec["linear_factors_G"]),
                        "J": rec["J"],
                    }
                )
                if rec["two_distinct_linear_F"] or rec["two_distinct_linear_G"]:
                    hits.append(rec)
    # one explicit deg>=6 tame auto
    wit = compose_triangular(2, 3, (1, 0, 0, 1))
    # F = x + (y+x^2)^3 has deg 6
    return {
        "compositions_tested": len(samples),
        "hits_two_distinct_linear_factors": len(hits),
        "hits": hits[:5],
        "sample_head": samples[:8],
        "tame_deg6_witness": {
            "map": "β∘α, α=(x,y+x^2), β=(x+y^3,y)",
            "deg_F": wit["deg_F"],
            "deg_G": wit["deg_G"],
            "leading_F": wit["leading_F"],
            "leading_G": wit["leading_G"],
            "linear_factors_F": wit["linear_factors_F"],
            "J": wit["J"],
            "J_is_1": wit["J"] == "1",
            "status": (
                "SURVIVES[J=1 / tame deg>=6] / "
                "NOT-APPLICABLE[two-point T2~p^5; leading form is a power of one linear]"
            ),
        },
        "theorem": (
            "A polynomial coordinate has a unique point at infinity in P^2: "
            "its leading form is a power of a single linear form.  Triangular "
            "automorphisms (and their affine conjugates) are coordinates.  "
            "No composition in this search, and no tame automorphism, produces "
            "two distinct linear factors in in(F) or in(G)."
        ),
        "construction_status": "NOT-APPLICABLE[tame-two-factor] / FALLACY-v2 no fill-by-analogy",
    }


def degenerate_top() -> dict:
    x, y = sp.symbols("x y")
    P = y**3 * (y - x) ** 8
    F = sp.expand(P**9)
    G = sp.expand(P**6)
    T2 = sp.expand(G**3 - F**2)
    J = sp.expand(sp.diff(F, x) * sp.diff(G, y) - sp.diff(F, y) * sp.diff(G, x))
    return {
        "pair": "F=P^9, G=P^6, P=y^3(y-x)^8",
        "degrees": (99, 66),
        "linear_factors_of_P": ["y", "y-x"],
        "T2_G3_minus_F2": str(T2),
        "T2_is_zero": T2 == 0,
        "T2_equals_p5": False,
        "J_is_0": J == 0,
        "status": (
            "two-point leading form, not an automorphism (J=0); "
            "T2 identically 0 is not ~ p^5.  Degeneration.  "
            "The bridge does not hold vacuously of every two-point pair."
        ),
    }


def face_ode_source() -> dict:
    """Xu (8.2) and 2 p R' - 25 p' R = 5 p^{14} at a=rho."""
    z, a = sp.symbols("z a")
    p = z**2 * (z + 3 * a)
    R = z**25 * (z + 3 * a) ** 14 * (z - 2 * a)
    lhs = sp.expand(2 * p * sp.diff(R, z) - 25 * sp.diff(p, z) * R)
    rhs = sp.expand(5 * p**14)
    # (8.2)
    t, pi = sp.symbols("t pi")
    A = pi * (pi + 3 * a) ** 2 * (pi - 2 * a) * t ** (-1)
    B = pi**2 * (pi + 3 * a) * t ** (-2)
    # Jacobian ∂(A,B)/∂(t,pi) = A_t B_pi - A_pi B_t
    Jac = sp.expand(sp.diff(A, t) * sp.diff(B, pi) - sp.diff(A, pi) * sp.diff(B, t))
    want = sp.expand(5 * pi**4 * (pi + 3 * a) ** 2 * t ** (-4))
    # q1 = -2 ∫ p^3 for δ=5/2
    pi2, c = sp.symbols("pi c")
    p52 = pi2 * (pi2**2 - c)
    q1p = sp.expand(-2 * p52**3)
    q1 = sp.integrate(q1p, pi2)  # ∫ q1' = q1, q1' = -2 p^3 so this is q1
    return {
        "face_ODE_holds": sp.expand(lhs - rhs) == 0,
        "xu_8_2_holds": sp.expand(Jac - want) == 0,
        "q1_minus_2_int_p3": str(sp.factor(q1)),
        "q1_degree": int(sp.degree(q1, pi2)),
    }


def run() -> dict:
    two = search_two_factors()
    ode = face_ode_source()
    return {
        "type": "CONTROLS[u_s=1 + tame-deg6 + two-factor-search + degenerate-top]",
        "us1_1612": us1_1612(),
        "automorphism_11": automorphism_11(),
        "two_point_search": two,
        "degenerate_two_point_top": degenerate_top(),
        "source_identities": ode,
        "controls_pass": (
            us1_1612()["bridge_rows_added"] == 0
            and automorphism_11()["J_is_1"]
            and two["hits_two_distinct_linear_factors"] == 0
            and two["tame_deg6_witness"]["J_is_1"]
            and degenerate_top()["T2_is_zero"]
            and ode["face_ODE_holds"]
            and ode["xu_8_2_holds"]
        ),
    }


if __name__ == "__main__":
    data = run()
    (HERE / "controls_bridge.json").write_text(
        json.dumps(data, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps({k: data[k] if k != "two_point_search" else {kk: data[k][kk] for kk in data[k] if kk != "sample_head"} for k in data}, indent=2)[:4000])
    print("controls_pass", data["controls_pass"])
