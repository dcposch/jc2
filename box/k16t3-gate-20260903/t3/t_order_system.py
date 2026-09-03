#!/usr/bin/env python3
"""Build the order-filtered K=16-ray Jacobian system for a fixed t.

The chart is a NECESSARY SUPERSET of the requested
  (12*t+4, 8*t+4; 12*t+1, 3; J=c*gamma)
locus.  It uses Phi radii (-1,t/(3*t+1)), the common fourth
approximate-root chart, and both major/minor order filtrations.  Theorem
1.2 gives the common coefficient bound ord C_i >= -i/(3*t+1).

The --gauged chart applies the three safe triangular target gauges:
  alpha_t=0, const(beta_(2*t+1))=0, const(alpha_(3*t+1))=0.

The Singular emitter uses elim.lib's sat() and explicitly extracts the
ideal component returned in its list.  It asserts the ideal type and current
ring, and runs empty/nonempty saturation controls plus the independent
monomial-Jacobian actual-pair control before the main computation.

The tuple-level Laurent bridge is deliberately not imposed, so a nonempty
chart would only be a counting bound.  Unit ideal for this necessary
superset, however, proves fixed-t nonexistence on the c != 0 component.
"""

import argparse
import sys
import time

import sympy as sp


gamma, pi = sp.symbols("gamma pi")


def jac(f, g):
    return sp.diff(f, gamma) * sp.diff(g, pi) - sp.diff(f, pi) * sp.diff(g, gamma)


def chart_spaces(t, one, A, B, z):
    """Both-disc Theorem-1.2 filtration for denominator e=3*t+1."""
    e = 3 * t + 1
    spaces = {}
    for i in range(1, e + 1):
        if i <= t:
            spaces[i] = [one]
        elif i <= 2 * t:
            spaces[i] = [one, A]
        elif i <= 3 * t:
            spaces[i] = [one, A, B]
        else:
            assert i == e
            spaces[i] = [one, gamma, A, B, z]
    return spaces


def build(t=3, gauged=False):
    if not isinstance(t, int) or t < 1:
        raise ValueError("t must be a positive integer")
    e, q = 3 * t + 1, 2 * t + 1
    b1, b2, b3, b4 = bs = sp.symbols("b1:5")
    z = pi - gamma
    B = sp.expand(pi * z + b1 * pi + b2)
    A = sp.expand(pi * B + b3)
    # The nonzero second top-line coefficient has been normalized to -1.
    h = sp.expand(pi * A + b4)
    spaces = chart_spaces(t, sp.Integer(1), A, B, z)
    alpha_spaces = {i: list(spaces[i]) for i in range(1, e + 1)}
    beta_spaces = {i: list(spaces[i]) for i in range(2, q + 1)}
    if gauged:
        # Q -> Q-const(beta_q), then P -> P-alpha_t*Q, then
        # P -> P-const(alpha_e).  This triangular target map preserves J.
        alpha_spaces[t] = []
        beta_spaces[q] = beta_spaces[q][1:]
        alpha_spaces[e] = alpha_spaces[e][1:]
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

    alpha = {i: make_coeff("a", i, alpha_spaces[i]) for i in range(1, e + 1)}
    beta = {i: make_coeff("q", i, beta_spaces[i]) for i in range(2, q + 1)}
    c = sp.Symbol("c")

    # Q has h-degree q and its h^(q-1) coefficient is zero by the
    # Tschirnhausen/approximate-root normalization.  P has h-degree e.
    q_terms = [(sp.Integer(1), q)] + [(beta[i], q - i) for i in range(2, q + 1)]
    p_terms = [(sp.Integer(1), e)] + [(alpha[i], e - i) for i in range(1, e + 1)]
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
                # Convention: (h-power, (gamma-degree, pi-degree), equation).
                tagged.append((hpow, monomial, coefficient))

    return {
        "t": t, "e": e, "q": q,
        "h": h, "A": A, "B": B, "z": z, "spaces": spaces,
        "alpha_spaces": alpha_spaces, "beta_spaces": beta_spaces,
        "gauged": gauged,
        "alpha": alpha, "beta": beta, "params": params, "c": c,
        "P": P, "Q": Q,
        "by_power": by_power, "equations": equations, "tagged": tagged,
    }


def singular(expr):
    return str(expr).replace("**", "^")


def emit_singular(data, characteristic=0):
    variables = data["params"] + [data["c"]]
    eqs = data["equations"]
    print("// generated by t_order_system.py --emit-singular")
    print("// t=%d; necessary superset; Phi=(-1,%d/%d); bound=-i/%d" %
          (data["t"], data["t"], data["e"], data["e"]))
    print("// safe target gauges: %s" % ("ON" if data["gauged"] else "OFF"))
    print('LIB "elim.lib";')
    # Actual-pair semantic control.  This pair has J=gamma but does not carry
    # the K=16 four-tuple; it checks the Jacobian convention only.
    print("ring RAC=%d,(gamma,pi),dp;" % characteristic)
    print("poly FAC=pi;")
    # Parentheses prevent Singular from coercing the exponent token while
    # parsing division in positive characteristic.
    print("poly GAC=pi-(gamma^2)/2;")
    print("poly JAC=diff(FAC,gamma)*diff(GAC,pi)-diff(FAC,pi)*diff(GAC,gamma);")
    print('if (JAC==gamma) { print("CONTROL_ACTUAL_PAIR_PASS J=gamma"); }'
          ' else { print("CONTROL_ACTUAL_PAIR_FAIL"); }')
    print("ring R=%d,(%s),dp;" % (characteristic, ",".join(map(str, variables))))
    print("option(redSB);")
    print('if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); }'
          ' else { print("CONTROL_RING_FAIL"); }')
    print("ideal C=c;")
    print('print("CONTROL_EMPTY_START");')
    print("ideal CE=c;")
    print("list LE=sat(CE,C);")
    print("ideal SE=LE[1];")
    print('if (typeof(SE)=="ideal" && nameof(basering)=="R")'
          ' { print("CONTROL_EMPTY_EXTRACT_RING_PASS"); }'
          ' else { print("CONTROL_EMPTY_EXTRACT_RING_FAIL"); }')
    print("ideal GE=std(SE);")
    print('if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); }'
          ' else { print("CONTROL_EMPTY_FAIL"); }')
    print('print("CONTROL_NONEMPTY_START");')
    print("ideal CN=c-1;")
    print("list LN=sat(CN,C);")
    print("ideal SN=LN[1];")
    print('if (typeof(SN)=="ideal" && nameof(basering)=="R")'
          ' { print("CONTROL_NONEMPTY_EXTRACT_RING_PASS"); }'
          ' else { print("CONTROL_NONEMPTY_EXTRACT_RING_FAIL"); }')
    print("ideal GN=std(SN);")
    print('if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); }'
          ' else { print("CONTROL_NONEMPTY_FAIL"); }')
    print('print("MAIN_START equations=%d chart_unknowns=%d characteristic=%d");' %
          (len(eqs), len(data["params"]) + 1, characteristic))
    generators = [singular(e) for e in eqs]
    print("ideal I=%s;" % ",\n".join(generators))
    print("list LS=sat(I,C);")
    print("ideal S=LS[1];")
    print('if (typeof(S)=="ideal" && nameof(basering)=="R")'
          ' { print("MAIN_EXTRACT_RING_PASS"); }'
          ' else { print("MAIN_EXTRACT_RING_FAIL"); }')
    print("ideal G=std(S);")
    print('print("MAIN_DONE basis_size=");')
    print("size(G);")
    print('if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); }'
          ' else { print("MAIN_NONTRIVIAL_SUPERSET_ONLY"); }')
    print("G;")
    print("quit;")


def audit(data, elapsed):
    t, e, q = data["t"], data["e"], data["q"]
    dims = [len(data["spaces"][i]) for i in range(1, e + 1)]
    alpha_count = sum(len(data["alpha_spaces"][i]) for i in range(1, e + 1))
    beta_count = sum(len(data["beta_spaces"][i]) for i in range(2, q + 1))
    params_with_c = len(data["params"]) + 1
    degree_hist = {}
    level_hist = {}
    all_vars = data["params"] + [data["c"]]
    for hpow, _monomial, equation in data["tagged"]:
        degree = sp.Poly(equation, *all_vars).total_degree()
        degree_hist[degree] = degree_hist.get(degree, 0) + 1
        level_hist[hpow] = level_hist.get(hpow, 0) + 1
    print("t=%d Theorem-1.2 order-filtered NECESSARY SUPERSET" % t)
    print("  tuple=(%d,%d;%d,3), (e,q)=(%d,%d)" %
          (12 * t + 4, 8 * t + 4, 12 * t + 1, e, q))
    print("  Phi radii=(-1,%d/%d)" % (t, e))
    print("  h =", data["h"])
    print("  filtration dimensions i=1..%d:" % e, dims)
    print("  accuracies: P=-1 over exponent %d; Q=-%d/%d over exponent %d" %
          (e, q, e, q))
    print("  common coefficient bound: ord C_i >= -i/%d" % e)
    print("  safe target gauges:", "ON" if data["gauged"] else "OFF")
    print("  alpha=%d beta=%d h=4 c=1 -> unknowns=%d" %
          (alpha_count, beta_count, params_with_c))
    print("  h-adic powers: 0..%d; coefficient equations=%d" %
          (max(data["by_power"]), len(data["equations"])))
    print("  h-level equation histogram:", level_hist)
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
    print("  tagged convention: (h_power,(gamma_degree,pi_degree),equation)")
    print("  omitted tuple-level bridge; NONTRIVIAL is COUNTING-BOUND only")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--t", type=int, default=3)
    parser.add_argument("--emit-singular", action="store_true")
    parser.add_argument("--gauged", action="store_true")
    parser.add_argument("--characteristic", type=int, default=0)
    args = parser.parse_args()
    if args.t < 1:
        parser.error("--t must be positive")
    if args.characteristic < 0:
        parser.error("--characteristic must be zero or a positive prime")
    if args.characteristic == 2:
        parser.error("characteristic 2 is incompatible with actual-pair control")
    started = time.time()
    data = build(t=args.t, gauged=args.gauged)
    if args.emit_singular:
        emit_singular(data, characteristic=args.characteristic)
    else:
        audit(data, time.time() - started)


if __name__ == "__main__":
    main()
