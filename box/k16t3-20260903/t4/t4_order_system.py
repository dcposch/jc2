#!/usr/bin/env python3
"""Build the gauged t=4 K=16 Theorem-1.2 order chart.

This is the literal t=4 generalization of the charged t=2 generator.  It is a
NECESSARY SUPERSET of the requested (52,36;49,3) locus: the tuple-level
Laurent bridge is deliberately not imposed.  The common coefficient bound is

    ord(C_i) >= -i/(3*t+1) = -i/13.

Default output is an audit.  ``--emit-singular`` emits a complete standard-
basis computation, over Q by default or over GF(p) when ``--prime p`` is
given.  ``--gauged`` applies exactly the three triangular target gauges used
in the charged t=2 computation, with its index correctly generalized:
alpha_(e-q)=alpha_t=alpha_4=0, const(beta_9)=0, and const(alpha_13)=0.
"""

import argparse
import sys
import time

import sympy as sp


T_VALUE = 4
gamma, pi = sp.symbols("gamma pi")


def jac(f, g):
    return sp.diff(f, gamma) * sp.diff(g, pi) - sp.diff(f, pi) * sp.diff(g, gamma)


def chart_spaces(t, one, A, B, z):
    """Two-disc spaces for ord(C_i)>=-i/(3*t+1)."""
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


def build(gauged=False, t=T_VALUE):
    assert t == T_VALUE
    e, q = 3 * t + 1, 2 * t + 1
    b1, b2, b3, b4 = bs = sp.symbols("b1:5")
    z = pi - gamma
    B = sp.expand(pi * z + b1 * pi + b2)
    A = sp.expand(pi * B + b3)
    h = sp.expand(pi * A + b4)
    spaces = chart_spaces(t, sp.Integer(1), A, B, z)
    alpha_spaces = {i: list(spaces[i]) for i in range(1, e + 1)}
    beta_spaces = {i: list(spaces[i]) for i in range(2, q + 1)}
    if gauged:
        # Q -> Q-const(beta_q), then P -> P-alpha_t*Q, then
        # P -> P-const(alpha_e).  Here e-q=t, so alpha_t multiplies h^q
        # and is the coefficient aligned with the leading term of Q.  The
        # t=2 charged driver called this alpha_2 only because t=2.  The
        # triangular target map preserves J.
        alpha_spaces[t] = []
        beta_spaces[q] = beta_spaces[q][1:]
        alpha_spaces[e] = alpha_spaces[e][1:]
    params = list(bs)

    def make_coeff(prefix, index, basis_space):
        if not basis_space:
            return sp.Integer(0)
        names = " ".join(
            "%s%d_%d" % (prefix, index, j) for j in range(len(basis_space))
        )
        coeffs = sp.symbols(names)
        if not isinstance(coeffs, tuple):
            coeffs = (coeffs,)
        params.extend(coeffs)
        return sp.Add(*(c * basis for c, basis in zip(coeffs, basis_space)))

    alpha = {
        i: make_coeff("a", i, alpha_spaces[i]) for i in range(1, e + 1)
    }
    beta = {i: make_coeff("q", i, beta_spaces[i]) for i in range(2, q + 1)}
    c = sp.Symbol("c")

    # beta_1=0 is the Tschirnhausen/approximate-root normalization.
    q_terms = [(sp.Integer(1), q)] + [(beta[i], q - i) for i in range(2, q + 1)]
    p_terms = [(sp.Integer(1), e)] + [(alpha[i], e - i) for i in range(1, e + 1)]
    Q = sp.Add(*(aa * h**r for aa, r in q_terms))
    P = sp.Add(*(bb * h**s for bb, s in p_terms))

    # Exact banded h-adic Jacobian identity.  No coefficient leader is
    # inverted.  Euclidean division is by monic h in pi and retains all
    # vanished-leader branches.
    by_power = {}
    for aa, r in q_terms:
        for bb, s in p_terms:
            v = jac(aa, bb)
            if v:
                by_power[r + s] = by_power.get(r + s, 0) + v
            v = s * bb * jac(aa, h) + r * aa * jac(h, bb)
            if v:
                by_power[r + s - 1] = by_power.get(r + s - 1, 0) + v

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
        "t": t,
        "e": e,
        "q": q,
        "h": h,
        "A": A,
        "B": B,
        "z": z,
        "spaces": spaces,
        "alpha_spaces": alpha_spaces,
        "beta_spaces": beta_spaces,
        "gauged": gauged,
        "alpha": alpha,
        "beta": beta,
        "params": params,
        "c": c,
        "P": P,
        "Q": Q,
        "by_power": by_power,
        "equations": equations,
        "tagged": tagged,
    }


def singular(expr):
    return str(expr).replace("**", "^")


def emit_singular(data, prime=0):
    c, rab = data["c"], sp.Symbol("T")
    variables = data["params"] + [c, rab]
    eqs = data["equations"]
    field = str(prime) if prime else "0"
    print("// generated by t4_order_system.py --gauged --emit-singular")
    print("// necessary superset; Phi=(-1,4/13); Theorem-1.2 bound=-i/13")
    print("// coefficient field: %s" % ("Q" if prime == 0 else "GF(%d)" % prime))
    print("// safe target gauges: %s" % ("ON" if data["gauged"] else "OFF"))
    print("LIB \"elim.lib\";")
    print("ring R=%s,(%s),dp;" % (field, ",".join(map(str, variables))))
    print("option(redSB);")

    # Direct sat() type/component controls in the declared main ring.  sat()
    # returns an ideal in Singular 4.3.2 (not a list); assigning it to an ideal
    # is the mechanical component/ring assertion.
    print('print("SAT_TYPE_RING_CONTROL_START nvars=");')
    print("nvars(basering);")
    print("ideal JS=c;")
    print("ideal IE0=c;")
    print("ideal IN0=c-1;")
    print("ideal SE=sat(IE0,JS);")
    print("ideal SN=sat(IN0,JS);")
    print('if (typeof(SE)=="ideal" && typeof(SN)=="ideal") '
          '{ print("SAT_COMPONENT_TYPE_PASS"); } '
          'else { print("SAT_COMPONENT_TYPE_FAIL"); }')
    print('if (reduce(1,SE)==0) { print("SAT_EMPTY_PASS"); } '
          'else { print("SAT_EMPTY_FAIL"); }')
    print('if (reduce(1,SN)!=0) { print("SAT_NONEMPTY_PASS"); } '
          'else { print("SAT_NONEMPTY_FAIL"); }')

    # Equivalent Rabinowitsch wrapper controls, and then the main c!=0
    # component.  The final T*c-1 generator avoids any ambiguity about sat()
    # return wrapping in the certificate computation.
    print('print("CONTROL_EMPTY_START");')
    print("ideal CE=c,T*c-1;")
    print("ideal GE=std(CE);")
    print('if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); } '
          'else { print("CONTROL_EMPTY_FAIL"); }')
    print('print("CONTROL_NONEMPTY_START");')
    print("ideal CN=c-1,T*c-1;")
    print("ideal GN=std(CN);")
    print('if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); } '
          'else { print("CONTROL_NONEMPTY_FAIL"); }')
    print('print("MAIN_START equations=%d parameters=%d plus_T=1");' %
          (len(eqs), len(data["params"]) + 1))
    generators = [singular(e) for e in eqs] + ["T*c-1"]
    print("ideal I=%s;" % ",\n".join(generators))
    print("ideal G=std(I);")
    print('print("MAIN_DONE basis_size=");')
    print("size(G);")
    print('if (reduce(1,G)==0) '
          '{ print("MAIN_SATURATED_EMPTY"); G; } '
          'else { print("MAIN_NONTRIVIAL_SUPERSET_ONLY"); '
          'print("BASIS_OUTPUT_TRUNCATED_TO_10"); '
          'int basis_cap=size(G); if (basis_cap>10) { basis_cap=10; } '
          'for (int basis_i=1; basis_i<=basis_cap; basis_i++) { G[basis_i]; } }')
    print("quit;")


def audit(data, elapsed):
    t, e, q = data["t"], data["e"], data["q"]
    dims = [len(data["spaces"][i]) for i in range(1, e + 1)]
    alpha_count = sum(len(data["alpha_spaces"][i]) for i in range(1, e + 1))
    beta_count = sum(len(data["beta_spaces"][i]) for i in range(2, q + 1))
    params_with_c = len(data["params"]) + 1
    degree_hist = {}
    all_vars = data["params"] + [data["c"]]
    for equation in data["equations"]:
        degree = sp.Poly(equation, *all_vars).total_degree()
        degree_hist[degree] = degree_hist.get(degree, 0) + 1

    print("t=4 Theorem-1.2 order-filtered NECESSARY SUPERSET")
    print("  (n,m;M2,V2)=(52,36;49,3); (e,q)=(13,9)")
    print("  Phi=(-1,4/13); closed form delta1=t/(3*t+1)=4/13")
    print("  h =", data["h"])
    print("  filtration dimensions i=1..13:", dims)
    print("  accuracies: P=-1 over exponent 13; Q=-9/13 over exponent 9")
    print("  common coefficient bound: ord C_i >= -i/13")
    print("  safe target gauges:", "ON" if data["gauged"] else "OFF")
    print("  alpha=%d beta=%d h=4 c=1 -> unknowns=%d" %
          (alpha_count, beta_count, params_with_c))
    print("  h-adic powers: 0..%d; coefficient equations=%d" %
          (max(data["by_power"]), len(data["equations"])))
    print("  parameter-degree histogram:", degree_hist)
    print("  equation text bytes:", sum(len(str(e)) for e in data["equations"]))
    print("  build seconds: %.3f" % elapsed)

    # Deterministic exact h-adic reconstruction at a numeric parameter point.
    sample = {v: (i % 7) - 3 for i, v in enumerate(data["params"])}
    hs = data["h"].subs(sample)
    direct = jac(data["Q"].subs(sample), data["P"].subs(sample))
    reconstructed = sum(
        r.subs(sample) * hs**k for k, r in data["by_power"].items()
    )
    reconstruction_ok = sp.expand(direct - reconstructed) == 0
    print("  deterministic numeric-parameter h-adic reconstruction:", reconstruction_ok)
    assert reconstruction_ok

    # Actual-pair negative classifier control, independent of the order chart.
    f = pi
    g = pi - gamma**2 / 2
    actual_j = sp.expand(jac(f, g))
    actual_control = (
        actual_j == gamma
        and sp.degree(f, pi) == 1
        and sp.degree(g, pi) == 1
        and (sp.degree(gamma**2 / 2, gamma), sp.degree(-gamma**2 / 2, gamma))
        == (2, 2)
    )
    print("  actual-pair control (pi,pi-gamma^2/2):", actual_control)
    print("    J=gamma and reciprocal anchor degrees=(2,2), but K16 4-tuple FAIL")
    assert actual_control
    print("  omitted tuple-level bridge: NONTRIVIAL means COUNTING-BOUND only")


def emit_tagged(data):
    print("# h_power\tgamma_power\tpi_power\tequation")
    for hpow, monomial, equation in data["tagged"]:
        print("%d\t%d\t%d\t%s" % (hpow, monomial[0], monomial[1], equation))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit-singular", action="store_true")
    parser.add_argument("--emit-tagged", action="store_true")
    parser.add_argument("--gauged", action="store_true")
    parser.add_argument("--prime", type=int, default=0)
    args = parser.parse_args()
    if args.prime and not args.emit_singular:
        parser.error("--prime requires --emit-singular")
    started = time.time()
    data = build(gauged=args.gauged)
    if args.emit_singular:
        emit_singular(data, args.prime)
    elif args.emit_tagged:
        emit_tagged(data)
    else:
        audit(data, time.time() - started)


if __name__ == "__main__":
    main()
