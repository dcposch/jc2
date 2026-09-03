#!/usr/bin/env python3
"""Independent t=2 K16 order-chart Jacobian system.

This intentionally does not import or call the charged generator.  It derives
the t=2 radii, constructs the gauged Theorem 1.2 coefficient spaces, computes
the h-adic Jacobian coefficients, and checks the recurrence by recomposition at
a deterministic numeric parameter point.
"""

import argparse
from fractions import Fraction as F
import sympy as sp


gamma, pi = sp.symbols("gamma pi")


def jac(u, v):
    return sp.diff(u, gamma) * sp.diff(v, pi) - sp.diff(u, pi) * sp.diff(v, gamma)


def t2_data():
    t = 2
    n, m, M2, V2, kjac = 12 * t + 4, 8 * t + 4, 12 * t + 1, 3, 1
    d2, d3 = 4, 1
    e, q = n // d2, m // d2
    raw2 = F(1) - F(n - M2, n - M2 - 1)
    raw1 = F(1) - F((n + m) * (V2 * (n - M2) - d2),
                    (n - M2 - 1) * (V2 * (n + m) - d2))
    phi2, phi1 = (kjac + 1) * raw2, (kjac + 1) * raw1
    lambda_p = 3 * e * phi1 + e * phi2
    lambda_q = 3 * q * phi1 + q * phi2
    assert (n, m, M2, V2, e, q) == (28, 20, 25, 3, 7, 5)
    assert (raw2, raw1) == (F(-1, 2), F(1, 7))
    assert (phi2, phi1) == (F(-1), F(2, 7))
    assert (lambda_p / e, lambda_q / q) == (F(-1, 7), F(-1, 7))
    return {
        "n": n,
        "m": m,
        "M2": M2,
        "V2": V2,
        "e": e,
        "q": q,
        "phi": (phi2, phi1),
        "bound": F(-1, 7),
    }


def basis_spaces(one, z, b_poly, a_poly):
    # Orders at the major root from the two-disc t=2 Phi radii; the minor
    # root imposes no additional exclusions among these five generators.
    major_order = [
        (one, F(0)),
        (a_poly, F(-3, 7)),
        (b_poly, F(-5, 7)),
        (z, F(-1)),
        (gamma, F(-1)),
    ]
    spaces = {}
    for i in range(1, 8):
        threshold = F(-i, 7)
        spaces[i] = [poly for poly, order in major_order if order >= threshold]
    assert [len(spaces[i]) for i in range(1, 8)] == [1, 1, 2, 2, 3, 3, 5]
    return spaces


def coeff(prefix, idx, basis, params):
    terms = []
    for j, base in enumerate(basis):
        var = sp.Symbol(f"{prefix}{idx}_{j}")
        params.append(var)
        terms.append(var * base)
    return sp.Add(*terms) if terms else sp.Integer(0)


def build():
    t2_data()
    b1, b2, b3, b4 = h_params = sp.symbols("b1:5")
    z = pi - gamma
    b_poly = sp.expand(pi * z + b1 * pi + b2)
    a_poly = sp.expand(pi * b_poly + b3)
    h = sp.expand(pi * a_poly + b4)
    spaces = basis_spaces(sp.Integer(1), z, b_poly, a_poly)

    alpha_spaces = {i: list(spaces[i]) for i in range(1, 8)}
    beta_spaces = {i: list(spaces[i]) for i in range(2, 6)}
    # Safe target gauges: alpha_2=0, scalar(beta_5)=0, scalar(alpha_7)=0.
    alpha_spaces[2] = []
    beta_spaces[5] = beta_spaces[5][1:]
    alpha_spaces[7] = alpha_spaces[7][1:]

    params = list(h_params)
    alpha = {i: coeff("p", i, alpha_spaces[i], params) for i in range(1, 8)}
    beta = {i: coeff("q", i, beta_spaces[i], params) for i in range(2, 6)}
    c = sp.Symbol("c")

    p_terms = [(sp.Integer(1), 7)] + [(alpha[i], 7 - i) for i in range(1, 8)]
    q_terms = [(sp.Integer(1), 5)] + [(beta[i], 5 - i) for i in range(2, 6)]
    p_poly = sp.Add(*(coef * h**power for coef, power in p_terms))
    q_poly = sp.Add(*(coef * h**power for coef, power in q_terms))

    by_power = {}
    for q_coef, q_power in q_terms:
        for p_coef, p_power in p_terms:
            same_power = jac(q_coef, p_coef)
            if same_power != 0:
                slot = q_power + p_power
                by_power[slot] = by_power.get(slot, 0) + same_power
            lower_power = (
                p_power * p_coef * jac(q_coef, h)
                + q_power * q_coef * jac(h, p_coef)
            )
            if lower_power != 0:
                slot = q_power + p_power - 1
                by_power[slot] = by_power.get(slot, 0) + lower_power

    level = 0
    while level <= max(by_power):
        quotient, remainder = sp.div(sp.expand(by_power.get(level, 0)), h, pi)
        by_power[level] = sp.expand(remainder)
        if quotient != 0:
            by_power[level + 1] = by_power.get(level + 1, 0) + quotient
        level += 1

    equations = []
    levels = []
    for level in sorted(by_power):
        remainder = by_power[level] - (c * gamma if level == 0 else 0)
        remainder = sp.expand(remainder)
        if remainder:
            levels.append(level)
            poly = sp.Poly(remainder, gamma, pi)
            equations.extend(sp.expand(coef) for _, coef in poly.terms() if coef != 0)

    sample = {param: (idx % 7) - 3 for idx, param in enumerate(params)}
    numeric_h = h.subs(sample)
    direct = jac(q_poly.subs(sample), p_poly.subs(sample))
    recomposed = sum(rem.subs(sample) * numeric_h**level for level, rem in by_power.items())
    assert sp.expand(direct - recomposed) == 0

    return {
        "params": params,
        "c": c,
        "h": h,
        "P": p_poly,
        "Q": q_poly,
        "equations": equations,
        "levels": levels,
        "reconstruction_ok": True,
        "spaces": spaces,
    }


def sstr(expr):
    return str(sp.expand(expr)).replace("**", "^")


def emit_singular(data):
    T = sp.Symbol("T")
    variables = data["params"] + [data["c"], T]
    print("// generated by t2_independent_order_system.py --emit-singular")
    print("// independent h-adic Jacobian computation with numeric recomposition check")
    print("ring R=0,(%s),dp;" % ",".join(map(str, variables)))
    print("option(redSB);")
    print('print("INDEP_START equations=%d parameters=%d plus_T=1");' %
          (len(data["equations"]), len(data["params"]) + 1))
    print("ideal I=%s;" % ",\n".join([sstr(e) for e in data["equations"]] + ["T*c-1"]))
    print("ideal G=std(I);")
    print('print("INDEP_DONE basis_size=");')
    print("size(G);")
    print('if (reduce(1,G)==0) { print("INDEP_SATURATED_EMPTY"); }'
          ' else { print("INDEP_NONTRIVIAL"); }')
    print("G;")
    print("quit;")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit-singular", action="store_true")
    args = parser.parse_args()
    data = build()
    if args.emit_singular:
        emit_singular(data)
        return
    print("Independent t=2 gauged order-chart system")
    print("  h =", data["h"])
    print("  dimensions i=1..7 =", [len(data["spaces"][i]) for i in range(1, 8)])
    print("  parameters including c =", len(data["params"]) + 1)
    print("  remainder levels =", data["levels"])
    print("  equations =", len(data["equations"]))
    print("  equation text bytes =", sum(len(str(e)) for e in data["equations"]))
    print("  numeric recomposition check =", data["reconstruction_ok"])


if __name__ == "__main__":
    main()
