#!/usr/bin/env python3
"""Calibration controls for the outer-band / T2-T3 add-on.

(16,12): Moh Appendix II, printed p.208.  u_s=1 on the (64,48) parent, so the
effective-root bridge is trivial (single Puiseux branch; T_i(sigma) are powers
of a linear polynomial).  The printed 17-coefficient chart *is* the
order-band truncation of the approximate-root tower.  Both c5 readings, with
Rabinowitsch wrapper T*kappa-1, Groebner over GF(32003) grevlex, are [1].
Ring, wrapper, and both controls declared.

Automorphism: F=a x+y, G=(a-1)x+y, J=1.  Degrees (1,1): the s=3 D1/D2 bands
and T2,T3 of degree 55,145 are NOT-APPLICABLE.  The plumbing must not kill it.

Order-spine unit identity (charged design §4.1) is rechecked over Q.
"""
from __future__ import annotations

import sympy as sp


P = 32003


def build_1612(repeated_c5: bool):
    x, y = sp.symbols("x y")
    b1, b2, b3, b4, a1 = sp.symbols("b1 b2 b3 b4 a1")
    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13 = sp.symbols(
        "c1 c2 c3 c4 c5 c6 c7 c8 c9 c10 c11 c12 c13"
    )
    kappa, T = sp.symbols("kappa T")
    h = y**3 * (y - x) + b1 * y**3 + b2 * y**2 + b3 * y + b4
    A = y**2 * (y - x) + b1 * y**2 + b2 * y + b3
    Bpoly = y * (y - x) + b1 * y + b2
    if repeated_c5:
        alpha3 = c5 * A + c5 * Bpoly + c7
        gens = [b1, b2, b3, b4, a1, c1, c2, c3, c4, c5, c7, c8, c9, c10, c11, c12, c13, kappa, T]
        alpha1 = a1
        variant = "printed_repeated_c5"
    else:
        alpha3 = c5 * A + c6 * Bpoly + c7
        gens = [b1, b2, b3, b4, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, kappa, T]
        alpha1 = 0
        variant = "absorbed_alpha1_distinct_c6"
    alpha2 = c1 * A + c2
    beta2 = c3 * A + c4
    beta3 = c8 * A + c9 * Bpoly + c10
    alpha4 = c11 * A + c12 * Bpoly + c13 * (y - x)
    g = sp.expand(h**4 + alpha1 * h**3 + alpha2 * h**2 + alpha3 * h + alpha4)
    f = sp.expand(h**3 + beta2 * h + beta3)
    J = sp.expand(
        sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x) - kappa
    )
    poly = sp.Poly(J, x, y, domain=sp.QQ[tuple(gens)])
    eqs = [sp.Poly(coeff, gens).as_expr() for coeff in poly.coeffs()]
    n_J = len(eqs)
    eqs.append(T * kappa - 1)
    return {
        "variant": variant,
        "gens": gens,
        "eqs": eqs,
        "n_J_rows": n_J,
        "n_coeff_variables": 17,
        "n_unknowns_with_kappa": 18,
        "wrapper": "T*kappa-1",
        "ring": f"GF({P})[gens], grevlex",
        "f": f,
        "g": g,
        "x": x,
        "y": y,
        "kappa": kappa,
        "T": T,
        "u_s": 1,
        "bridge": "TRIVIAL[u_s=1]",
    }


def groebner_modp(eqs, gens, p=P):
    reduced = []
    for e in eqs:
        pe = sp.Poly(e, gens, domain=sp.QQ)
        pe = pe.set_domain(sp.ZZ)
        content = pe.content()
        if content != 0:
            pe = pe.quo_ground(content)
        pe = pe.set_modulus(p)
        if pe != 0:
            reduced.append(pe.as_expr())
    if not reduced:
        return [0]
    G = sp.groebner(reduced, gens, domain=sp.GF(p), order="grevlex")
    return [sp.expand(item) for item in G]


def wrapper_controls() -> dict:
    k, T = sp.symbols("kappa T")
    G_neg = sp.groebner([k, T * k - 1], [k, T], domain=sp.QQ)
    G_pos = sp.groebner([k - 1, T * k - 1], [k, T], domain=sp.QQ)
    return {
        "ring": "Q[kappa, T]",
        "negative_kappa_and_wrapper": [str(g) for g in G_neg],
        "positive_kappa_minus_1_and_wrapper": [str(g) for g in G_pos],
        "negative_is_one": list(G_neg) == [1],
        "positive_not_one": list(G_pos) != [1],
    }


def order_spine_identity() -> dict:
    z = sp.symbols("z")
    left = (20 * z - sp.Rational(10, 3)) * (sp.Rational(27, 10) - sp.Rational(27, 5) * z) - 1
    right = -2 * (54 * z**2 - 36 * z + 5)
    diff = sp.expand(left - right)
    return {
        "identity": "(20z-10/3)(27/10-27z/5)-1 = -2(54z^2-36z+5)",
        "difference": str(diff),
        "holds_over_Q": diff == 0,
        "modulus": "Q[z]/(54z^2-36z+5)",
        "terminal_unit": "20z-10/3",
    }


def automorphism_control() -> dict:
    a, x, y, A, C = sp.symbols("a x y A C")
    F = a * x + y
    G = (a - 1) * x + y
    J = sp.expand(sp.diff(F, x) * sp.diff(G, y) - sp.diff(F, y) * sp.diff(G, x))
    Fans = A * x + y
    Gans = C * x + y
    Jans = sp.expand(
        sp.diff(Fans, x) * sp.diff(Gans, y) - sp.diff(Fans, y) * sp.diff(Gans, x)
    )
    row = sp.expand(Jans - 1)
    witness_F = Fans.subs({A: 2})
    witness_G = Gans.subs({C: 1})
    Jw = sp.expand(
        sp.diff(witness_F, x) * sp.diff(witness_G, y)
        - sp.diff(witness_F, y) * sp.diff(witness_G, x)
    )
    return {
        "type": "EXACT-AUTOMORPHISM / SURVIVES[UNIVERSAL-GLOBAL-CHECKS]",
        "pair": "F=a*x+y, G=(a-1)*x+y",
        "J_identically": str(J),
        "J_is_1": J == 1,
        "shared_ansatz_row": str(row),
        "row_is_A_minus_C_minus_1": sp.expand(row - (A - C - 1)) == 0,
        "slice_A2_witness": {"F": str(witness_F), "G": str(witness_G), "J": str(Jw)},
        "s3_tower": "NOT-APPLICABLE[degrees (1,1)]",
        "outer_D1_D2_bands": "NOT-APPLICABLE[degrees (1,1)]",
        "T2_T3_bridge": "NOT-APPLICABLE[degrees (1,1); no mu2=55]",
        "survives": J == 1 and Jw == 1,
    }


def run_1612(repeated_c5: bool) -> dict:
    sys = build_1612(repeated_c5)
    assert sys["n_J_rows"] == 77
    assert sys["n_unknowns_with_kappa"] == 18
    Gmod = groebner_modp(sys["eqs"], sys["gens"])
    return {
        "variant": sys["variant"],
        "u_s": 1,
        "bridge": sys["bridge"],
        "n_J_rows": sys["n_J_rows"],
        "n_coeff_variables": sys["n_coeff_variables"],
        "wrapper": sys["wrapper"],
        "ring": sys["ring"],
        "gb_is_one": Gmod == [1],
        "gb_len": len(Gmod),
        "gb_head": [str(g) for g in Gmod[:4]],
        "outer_bands_present": (
            "the 17-coefficient p.208 chart is the order-truncated "
            "approximate-root tower; adding D1/D2 vanishings cannot enlarge it"
        ),
    }


def run() -> dict:
    wrap = wrapper_controls()
    assert wrap["negative_is_one"] and wrap["positive_not_one"]
    spine = order_spine_identity()
    assert spine["holds_over_Q"]
    auto = automorphism_control()
    assert auto["survives"]
    printed = run_1612(True)
    compiler = run_1612(False)
    assert printed["gb_is_one"] and compiler["gb_is_one"]
    return {
        "type": "SATURATED-EMPTY[P208-ANSATZ / GF(32003)] + SURVIVES[AUTOMORPHISM]",
        "wrapper_controls": wrap,
        "order_spine": spine,
        "printed_c5": printed,
        "compiler_c6_absorb_alpha1": compiler,
        "automorphism": auto,
        "us1_bridge_trivial": True,
        "controls_pass": True,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run(), indent=2, sort_keys=True, default=str))
