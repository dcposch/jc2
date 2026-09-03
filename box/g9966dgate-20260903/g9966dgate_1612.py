#!/usr/bin/env python3
"""Replay Moh p.208 (16,12) ansatz: printed-c5 reading, J=kappa, T*kappa-1.

Coefficient ring is Q; Groebner is over GF(32003) and, if cheap, Q.
Positive control: drop the wrapper (kappa=0 origin may survive).
Negative control: <kappa, T*kappa-1> is [1] in the same ring.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
P = 32003


def build_system(repeated_c5: bool):
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
        # printed (4): c5 on both A and B, no distinct c6
        alpha3 = c5 * A + c5 * Bpoly + c7
        gens = [b1, b2, b3, b4, a1, c1, c2, c3, c4, c5, c7, c8, c9, c10, c11, c12, c13, kappa, T]
        alpha1 = a1
    else:
        # compiler: distinct c6, absorb alpha1
        alpha3 = c5 * A + c6 * Bpoly + c7
        gens = [b1, b2, b3, b4, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, kappa, T]
        alpha1 = 0
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
    eqs.append(T * kappa - 1)
    return gens, eqs, f, g


def groebner_modp(eqs, gens, p=P):
    Fp = sp.GF(p)
    reduced = []
    for e in eqs:
        pe = sp.Poly(e, gens, domain=sp.QQ)
        # clear denominators then reduce mod p
        pe = pe.set_domain(sp.ZZ)
        content = pe.content()
        if content != 0:
            pe = pe.quo_ground(content)
        pe = pe.set_modulus(p)
        if pe != 0:
            reduced.append(pe.as_expr())
    if not reduced:
        return [0]
    G = sp.groebner(reduced, gens, domain=Fp, order="grevlex")
    return [sp.expand(g) for g in G]


def main() -> None:
    out = {"type": "SATURATED-EMPTY[P208-COMMON-POLYNOMIAL-ANSATZ] / REPLAY"}
    gens, eqs, f, g = build_system(repeated_c5=True)
    out["printed_c5"] = {
        "n_gens_incl_T_kappa": len(gens),
        "n_coeff_plus_wrapper": len(eqs),
        "n_J_rows": len(eqs) - 1,
        "coeff_variables": 17,
    }
    # wrapper controls in the (kappa,T) ring
    k, T = sp.symbols("kappa T")
    G_neg = sp.groebner([k, T * k - 1], [k, T], domain=sp.QQ)
    G_pos = sp.groebner([k - 1, T * k - 1], [k, T], domain=sp.QQ)
    out["wrapper_controls"] = {
        "negative_kappa_and_Tkappa_minus_1": [str(g) for g in G_neg],
        "positive_kappa_minus_1_and_wrapper": [str(g) for g in G_pos],
        "negative_is_one": list(G_neg) == [1],
        "positive_not_one": list(G_pos) != [1],
    }
    assert list(G_neg) == [1]
    assert list(G_pos) != [1]

    Gmod = groebner_modp(eqs, gens)
    out["printed_c5"]["modp"] = P
    out["printed_c5"]["gb_modp"] = [str(g) for g in Gmod[:8]]
    out["printed_c5"]["gb_is_one"] = Gmod == [1]
    out["printed_c5"]["gb_len"] = len(Gmod)

    gens2, eqs2, _, _ = build_system(repeated_c5=False)
    out["compiler_c6_absorb_alpha1"] = {
        "n_gens_incl_T_kappa": len(gens2),
        "n_J_rows": len(eqs2) - 1,
        "coeff_variables": 17,
    }
    Gmod2 = groebner_modp(eqs2, gens2)
    out["compiler_c6_absorb_alpha1"]["gb_modp"] = [str(g) for g in Gmod2[:8]]
    out["compiler_c6_absorb_alpha1"]["gb_is_one"] = Gmod2 == [1]
    out["compiler_c6_absorb_alpha1"]["gb_len"] = len(Gmod2)

    path = HERE / "results_1612.json"
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
