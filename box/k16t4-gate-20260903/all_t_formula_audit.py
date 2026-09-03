#!/usr/bin/env python3
"""Symbolic Q(t) audit for the all-t K=16 normalizer lemma."""

from __future__ import annotations

import hashlib
import json
import pathlib

import sympy as sp


OUT = pathlib.Path("/home/ubuntu/jc2/box/k16t4-gate-20260903")


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def no_positive_integer_root_factorization(expr: sp.Expr, t: sp.Symbol) -> bool:
    factors = sp.factor_list(sp.factor(expr))[1]
    for factor, _power in factors:
        poly = sp.Poly(factor, t, domain=sp.QQ)
        if poly.degree() == 1:
            root = -poly.nth(0) / poly.nth(1)
            if root.is_integer and root > 0:
                return False
        elif poly.degree() == 0:
            continue
        else:
            for root in sp.roots(poly.as_expr(), t):
                if root.is_integer and root > 0:
                    return False
    return True


def main() -> None:
    t, x, y, c = sp.symbols("t x y c")
    q = 2*t + 1
    e = 3*t + 1
    r = e/q
    C2 = r*(r - 1)/2
    C3 = r*(r - 1)*(r - 2)/6
    g1 = r*x
    g2 = r*y + C2*x**2
    g3 = 2*C2*x*y + C3*x**3

    E1 = q*g1 - e*x
    E2 = 2*q*g2 - (e - q)*x*g1 - 2*e*y
    E3 = 3*q*g3 - (e - 2*q)*x*g2 - (2*e - q)*y*g1
    E4 = (e - 3*q)*x*g3 + (2*e - 2*q)*y*g2
    E0 = c + y*g3

    Hhat = 12*q**2*y**2 - 12*q*(t + 1)*x**2*y + (t + 1)*(3*t + 2)*x**4
    cimage = t*e*x*y*((t + 1)*x**2 - 6*q*y) / (6*q**3)
    H = sp.expand(Hhat.subs(x, 1))
    ct = sp.factor(cimage.subs(x, 1))
    numerator_ct = sp.factor(t*e*y*((t + 1) - 6*q*y))

    checks = {
        "E1_zero": sp.factor(E1) == 0,
        "E2_zero": sp.factor(E2) == 0,
        "E3_zero": sp.factor(E3) == 0,
        "E4_equals_H_multiple": sp.factor(E4 - t*e*Hhat/(6*q**3)) == 0,
        "E0_gives_C": sp.factor(E0.subs(c, cimage)) == 0,
        "disc_y_H": sp.factor(sp.discriminant(H, y)) == 48*q**2*(t + 1),
        "C_forces_x_if_c_nonzero": sp.factor(cimage.subs(x, 0)) == 0,
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    res_y = sp.factor(sp.resultant(H, y, y))
    linear = (t + 1) - 6*q*y
    res_linear = sp.factor(sp.resultant(H, linear, y))
    res_num = sp.factor(sp.resultant(H, numerator_ct, y))
    expected_res_num = sp.factor((t*e)**2 * res_y * res_linear)
    if sp.factor(res_num - expected_res_num) != 0:
        raise AssertionError((res_num, expected_res_num))

    specializations = []
    for value in range(1, 13):
        Hv = sp.Poly(H.subs(t, value), y, domain=sp.QQ)
        content, primitive = Hv.primitive()
        specializations.append({
            "t": value,
            "content": str(content),
            "primitive_H": str(primitive.as_expr()),
            "raw_discriminant": str(sp.discriminant(Hv.as_expr(), y)),
            "primitive_discriminant": str(sp.discriminant(primitive.as_expr(), y)),
            "primitive_factorization": str(sp.factor(primitive.as_expr())),
        })

    displayed_H4 = sp.expand(H.subs(t, 4))
    displayed_H4_poly = sp.Poly(displayed_H4, y, domain=sp.QQ)
    displayed_H4_content, primitive_H4 = displayed_H4_poly.primitive()

    record = {
        "typing": "EXACT-SYMPY-Q(t)-FORMULA-AUDIT",
        "symbols": {"q": str(q), "e": str(e), "r": str(r)},
        "g": {"g1": str(sp.factor(g1)), "g2": str(sp.factor(g2)), "g3": str(sp.factor(g3))},
        "checks": checks,
        "Hhat": str(Hhat),
        "H_normalized": str(H),
        "ct": str(ct),
        "numerator_ct_for_resultant": str(numerator_ct),
        "disc_y_H": str(sp.factor(sp.discriminant(H, y))),
        "H_at_y0": str(sp.factor(H.subs(y, 0))),
        "H_at_second_c_factor_root": str(sp.factor(H.subs(y, (t + 1)/(6*q)))),
        "Res_H_y": str(res_y),
        "Res_H_second_factor": str(res_linear),
        "Res_H_numerator_ct": str(res_num),
        "Res_H_numerator_ct_has_no_positive_integer_root": no_positive_integer_root_factorization(res_num, t),
        "content_note": "Specializing H_t may introduce content; nonzero content does not change roots or unit gcd in Q[y].",
        "specializations_t_1_to_12": specializations,
        "t4_content_check": {
            "displayed_H4_from_formula": str(displayed_H4),
            "displayed_H4_content": str(displayed_H4_content),
            "displayed_H4_discriminant": str(sp.discriminant(displayed_H4, y)),
            "primitive_H4": str(primitive_H4.as_expr()),
            "primitive_H4_discriminant": str(sp.discriminant(primitive_H4.as_expr(), y)),
        },
        "grading_formula": {
            "x_weight": "4*t+1",
            "y_weight": "8*t+2=2*(4*t+1)",
            "c_weight": "20*t+5=5*(4*t+1)",
            "positive_for_t_ge_1": True,
        },
    }
    path = OUT / "all_t_formula_audit.json"
    path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "audit": path.name,
        "sha256": sha256(path),
        "checks": checks,
        "Res_H_numerator_ct": str(res_num),
        "no_positive_integer_root": record["Res_H_numerator_ct_has_no_positive_integer_root"],
        "t4_primitive_H": record["t4_content_check"]["primitive_H4"],
        "t4_displayed_content": record["t4_content_check"]["displayed_H4_content"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
