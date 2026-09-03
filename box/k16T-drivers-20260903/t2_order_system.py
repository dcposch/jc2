#!/usr/bin/env python3
"""Build the t=2 two-disc order-filtered Jacobian system.

The chart is a NECESSARY SUPERSET of the requested (28,20;25,3) locus.
It uses Phi radii (-1,2/7), the common fourth approximate-root chart, and
both major/minor order filtrations.  Theorem 1.2 uses coherent-system
accuracy divided by the h-exponent: here P has accuracy -1 and exponent 7,
while Q has accuracy -5/7 and exponent 5, so both coefficient bounds are
ord C_i >= -i/7.  (Using -i*delta_1=-2i/7 would be a weaker 54-variable
superset.)  This file does not impose the still-missing tuple-level Laurent bridge
(expected p_17 != 0 under the reciprocal exponent dictionary), so a nonempty result
is not a candidate pair.  The Lemma-2.1 anchor in this parameter is p_19, not p_17.

Default: print audited counts.  --gauged uses the three safe triangular target
gauges alpha_2=0, const(beta_5)=0, const(alpha_7)=0.  --emit-singular writes a
complete Singular program to stdout.  The program uses a Rabinowitsch equation
T*c-1 and also runs tiny empty/nonempty wrapper controls before the main basis.
"""

import argparse
import sys
import time
import sympy as sp


gamma, pi = sp.symbols("gamma pi")


def jac(f, g):
    return sp.diff(f, gamma) * sp.diff(g, pi) - sp.diff(f, pi) * sp.diff(g, gamma)


def chart_spaces(one, A, B, z):
    """Both-disc filtration from Theorem 1.2's bound ord C_i >= -i/7."""
    return {
        1: [one],
        2: [one],
        3: [one, A],
        4: [one, A],
        5: [one, A, B],
        6: [one, A, B],
        7: [one, gamma, A, B, z],
    }


def build(gauged=False):
    b1, b2, b3, b4 = bs = sp.symbols("b1:5")
    z = pi - gamma
    B = sp.expand(pi * z + b1 * pi + b2)
    A = sp.expand(pi * B + b3)
    # The nonzero second top-line coefficient has been normalized to -1.
    h = sp.expand(pi * A + b4)
    spaces = chart_spaces(sp.Integer(1), A, B, z)
    alpha_spaces = {i: list(spaces[i]) for i in range(1, 8)}
    beta_spaces = {i: list(spaces[i]) for i in range(2, 6)}
    if gauged:
        # Q -> Q-const(beta_5), then P -> P-alpha_2*Q, then
        # P -> P-const(alpha_7).  This triangular target map preserves J.
        alpha_spaces[2] = []
        beta_spaces[5] = beta_spaces[5][1:]
        alpha_spaces[7] = alpha_spaces[7][1:]
    params = list(bs)

    def make_coeff(prefix, index, basis_space):
        if not basis_space:
            return sp.Integer(0)
        names = " ".join("%s%d_%d" % (prefix, index, j)
                         for j in range(len(basis_space)))
        coeffs = sp.symbols(names)
        if not isinstance(coeffs, tuple):
            coeffs = (coeffs,)
        params.extend(coeffs)
        return sp.Add(*(c * basis for c, basis in zip(coeffs, basis_space)))

    alpha = {i: make_coeff("a", i, alpha_spaces[i]) for i in range(1, 8)}
    beta = {i: make_coeff("q", i, beta_spaces[i]) for i in range(2, 6)}
    c = sp.Symbol("c")

    # Q has degree 20 and h-degree 5; its h^4 coefficient is zero by the
    # Tschirnhausen/approximate-root normalization.  P has degree 28.
    q_terms = [(sp.Integer(1), 5)] + [(beta[i], 5 - i) for i in range(2, 6)]
    p_terms = [(sp.Integer(1), 7)] + [(alpha[i], 7 - i) for i in range(1, 8)]
    Q = sp.Add(*(aa * h**r for aa, r in q_terms))
    P = sp.Add(*(bb * h**s for bb, s in p_terms))

    # Exact h-adic Jacobian calculation.  For F=a*h^r and G=b*h^s,
    # J(F,G)=h^(r+s)J(a,b)+h^(r+s-1)(s*b*J(a,h)+r*a*J(h,b)).
    by_power = {}
    for aa, r in q_terms:
        for bb, s in p_terms:
            v = jac(aa, bb)
            if v:
                by_power[r + s] = by_power.get(r + s, 0) + v
            v = s * bb * jac(aa, h) + r * aa * jac(h, bb)
            if v:
                by_power[r + s - 1] = by_power.get(r + s - 1, 0) + v

    # Monic division makes the h-adic normal form exact.  Keep every branch:
    # no coefficient leader is divided out or assumed nonzero here.
    k = 0
    while k <= max(by_power):
        quotient, remainder = sp.div(sp.expand(by_power.get(k, 0)), h, pi)
        by_power[k] = sp.expand(remainder)
        if quotient != 0:
            by_power[k + 1] = by_power.get(k + 1, 0) + quotient
        k += 1

    equations = []
    tagged = []
    for hpow in sorted(by_power):
        remainder = by_power[hpow]
        if hpow == 0:
            remainder = sp.expand(remainder - c * gamma)
        poly = sp.Poly(remainder, gamma, pi)
        for monomial, coefficient in poly.terms():
            coefficient = sp.expand(coefficient)
            if coefficient != 0:
                equations.append(coefficient)
                tagged.append((hpow, monomial, coefficient))

    return {
        "h": h, "A": A, "B": B, "z": z, "spaces": spaces,
        "alpha_spaces": alpha_spaces, "beta_spaces": beta_spaces,
        "gauged": gauged,
        "alpha": alpha, "beta": beta, "params": params, "c": c,
        "P": P, "Q": Q,
        "by_power": by_power, "equations": equations, "tagged": tagged,
    }


def singular(expr):
    return str(expr).replace("**", "^")


def emit_singular(data):
    c, T = data["c"], sp.Symbol("T")
    variables = data["params"] + [c, T]
    eqs = data["equations"]
    print("// generated by t2_order_system.py --emit-singular")
    print("// necessary superset; Phi=(-1,2/7); Theorem-1.2 bound=-i/7")
    print("// safe target gauges: %s" % ("ON" if data["gauged"] else "OFF"))
    print("ring R=0,(%s),dp;" % ",".join(map(str, variables)))
    print("option(redSB);")
    print('print("CONTROL_EMPTY_START");')
    print("ideal CE=c,T*c-1;")
    print("ideal GE=std(CE);")
    print('if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); }'
          ' else { print("CONTROL_EMPTY_FAIL"); }')
    print('print("CONTROL_NONEMPTY_START");')
    print("ideal CN=c-1,T*c-1;")
    print("ideal GN=std(CN);")
    print('if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); }'
          ' else { print("CONTROL_NONEMPTY_FAIL"); }')
    print('print("MAIN_START equations=%d parameters=%d plus_T=1");' %
          (len(eqs), len(data["params"]) + 1))
    generators = [singular(e) for e in eqs] + ["T*c-1"]
    print("ideal I=%s;" % ",\n".join(generators))
    print("ideal G=std(I);")
    print('print("MAIN_DONE basis_size=");')
    print("size(G);")
    print('if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); }'
          ' else { print("MAIN_NONTRIVIAL_SUPERSET_ONLY"); }')
    print("G;")
    print("quit;")


def audit(data, elapsed):
    dims = [len(data["spaces"][i]) for i in range(1, 8)]
    alpha_count = sum(len(data["alpha_spaces"][i]) for i in range(1, 8))
    beta_count = sum(len(data["beta_spaces"][i]) for i in range(2, 6))
    params_with_c = len(data["params"]) + 1
    degree_hist = {}
    all_vars = data["params"] + [data["c"]]
    for equation in data["equations"]:
        degree = sp.Poly(equation, *all_vars).total_degree()
        degree_hist[degree] = degree_hist.get(degree, 0) + 1
    print("t=2 Theorem-1.2 order-filtered NECESSARY SUPERSET")
    print("  h =", data["h"])
    print("  filtration dimensions i=1..7:", dims)
    print("  accuracies: P=-1 over exponent 7; Q=-5/7 over exponent 5")
    print("  common coefficient bound: ord C_i >= -i/7")
    print("  safe target gauges:", "ON" if data["gauged"] else "OFF")
    print("  alpha=%d beta=%d h=4 c=1 -> unknowns=%d" %
          (alpha_count, beta_count, params_with_c))
    print("  h-adic powers: 0..%d; coefficient equations=%d" %
          (max(data["by_power"]), len(data["equations"])))
    print("  parameter-degree histogram:", degree_hist)
    print("  equation text bytes:", sum(len(str(e)) for e in data["equations"]))
    print("  build seconds: %.3f" % elapsed)
    sample = {v: (i % 7) - 3 for i, v in enumerate(data["params"])}
    hs = data["h"].subs(sample)
    direct = jac(data["Q"].subs(sample), data["P"].subs(sample))
    reconstructed = sum(r.subs(sample) * hs**k for k, r in data["by_power"].items())
    reconstruction_ok = sp.expand(direct - reconstructed) == 0
    print("  deterministic numeric-parameter h-adic reconstruction:", reconstruction_ok)
    assert reconstruction_ok
    print("  omitted tuple-level bridge: expected p_17 != 0 plus earlier non-4 exponents")
    print("  distinct Lemma-2.1 anchor in this parameter: p_19")
    print("  therefore NONTRIVIAL is COUNTING-BOUND, never REPRESENTATIVE")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit-singular", action="store_true")
    parser.add_argument("--gauged", action="store_true")
    args = parser.parse_args()
    started = time.time()
    data = build(gauged=args.gauged)
    if args.emit_singular:
        emit_singular(data)
    else:
        audit(data, time.time() - started)


if __name__ == "__main__":
    main()
