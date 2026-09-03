#!/usr/bin/env python3
"""Build the gauged K=16 order-chart family at a fixed integer t.

This is a family driver, not a uniform certificate: the polynomial ring grows
with t.  Besides the full system it can emit a low h-adic tail cutoff.  In
reverse (h-power) indexing those fixed low levels are literally independent
of t once the filtration spaces involved have stabilized.

The chart and the three gauges are the ones in the frozen charged t=2 driver:
  const(beta_(2t+1)) = 0,
  alpha_t = 0,
  const(alpha_(3t+1)) = 0.
No parameter-dependent leading coefficient is divided out.
"""

import argparse
import collections
import json
import sys
import time

import sympy as sp


gamma, pi = sp.symbols("gamma pi")


def jac(f, g):
    return sp.diff(f, gamma) * sp.diff(g, pi) - sp.diff(f, pi) * sp.diff(g, gamma)


def coefficient_space(i, t, one, A, B, z):
    """The common both-disc space at h-deficit i."""
    if 1 <= i <= t:
        return [one]
    if t < i <= 2 * t:
        return [one, A]
    if 2 * t < i <= 3 * t:
        return [one, A, B]
    if i == 3 * t + 1:
        return [one, gamma, A, B, z]
    raise ValueError("deficit outside 1..3t+1: %s" % i)


def build(t, gauged=True):
    if not isinstance(t, int) or t < 2:
        raise ValueError("this family driver is audited for integer t >= 2")
    e, q = 3 * t + 1, 2 * t + 1
    b1, b2, b3, b4 = bs = sp.symbols("b1:5")
    z = pi - gamma
    B = sp.expand(pi * z + b1 * pi + b2)
    A = sp.expand(pi * B + b3)
    h = sp.expand(pi * A + b4)
    one = sp.Integer(1)

    alpha_spaces = {i: coefficient_space(i, t, one, A, B, z)
                    for i in range(1, e + 1)}
    beta_spaces = {j: coefficient_space(j, t, one, A, B, z)
                   for j in range(2, q + 1)}
    if gauged:
        # P -> P-alpha_t Q is safe because alpha_t is scalar.  The other
        # two gauges are scalar target translations.
        alpha_spaces[t] = []
        beta_spaces[q] = beta_spaces[q][1:]
        alpha_spaces[e] = alpha_spaces[e][1:]

    params = list(bs)

    def make_coeff(prefix, index, basis_space):
        if not basis_space:
            return sp.Integer(0)
        coeffs = sp.symbols(" ".join(
            "%s%d_%d" % (prefix, index, k) for k in range(len(basis_space))))
        if not isinstance(coeffs, tuple):
            coeffs = (coeffs,)
        params.extend(coeffs)
        return sp.Add(*(co * basis for co, basis in zip(coeffs, basis_space)))

    alpha = {i: make_coeff("a", i, alpha_spaces[i]) for i in range(1, e + 1)}
    beta = {j: make_coeff("q", j, beta_spaces[j]) for j in range(2, q + 1)}
    c = sp.Symbol("c")

    q_terms = [(one, q)] + [(beta[j], q - j) for j in range(2, q + 1)]
    p_terms = [(one, e)] + [(alpha[i], e - i) for i in range(1, e + 1)]
    Q = sp.Add(*(aa * h**r for aa, r in q_terms))
    P = sp.Add(*(bb * h**s for bb, s in p_terms))

    # Banded exact identity.  The raw coefficient at a fixed h-level only
    # sees pairs with r+s or r+s-1 equal to that level.
    raw_by_power = {}
    for aa, r in q_terms:
        for bb, s in p_terms:
            value = jac(aa, bb)
            if value:
                raw_by_power[r + s] = raw_by_power.get(r + s, 0) + value
            value = s * bb * jac(aa, h) + r * aa * jac(h, bb)
            if value:
                raw_by_power[r + s - 1] = raw_by_power.get(r + s - 1, 0) + value

    # Monic h-division is a t-independent linear carry from level k to k+1.
    by_power = dict(raw_by_power)
    k = 0
    while k <= max(by_power):
        quotient, remainder = sp.div(sp.expand(by_power.get(k, 0)), h, pi)
        by_power[k] = sp.expand(remainder)
        if quotient != 0:
            by_power[k + 1] = by_power.get(k + 1, 0) + quotient
        k += 1

    tagged = []
    for hpow in sorted(by_power):
        remainder = sp.expand(by_power[hpow] - (c * gamma if hpow == 0 else 0))
        for monomial, coefficient in sp.Poly(remainder, gamma, pi).terms():
            coefficient = sp.expand(coefficient)
            if coefficient != 0:
                tagged.append((hpow, monomial, coefficient))

    equations = [eq for _, _, eq in tagged]
    return {
        "t": t, "e": e, "q": q, "h": h, "A": A, "B": B, "z": z,
        "alpha_spaces": alpha_spaces, "beta_spaces": beta_spaces,
        "alpha": alpha, "beta": beta, "params": params, "c": c,
        "P": P, "Q": Q, "raw_by_power": raw_by_power,
        "by_power": by_power, "tagged": tagged, "equations": equations,
        "gauged": gauged,
    }


def singular(expr):
    return str(sp.expand(expr)).replace("**", "^")


def selected_equations(data, low_h_max=None, high_h_min=None):
    if low_h_max is not None and high_h_min is not None:
        raise ValueError("choose only one h-level cutoff")
    tagged = data["tagged"]
    if low_h_max is not None:
        tagged = [row for row in tagged if row[0] <= low_h_max]
    if high_h_min is not None:
        tagged = [row for row in tagged if row[0] >= high_h_min]
    return tagged


def emit_singular(data, tagged, modulus=0, controls=False, print_basis=True):
    T = sp.Symbol("T")
    variables = data["params"] + [data["c"], T]
    characteristic = str(modulus) if modulus else "0"
    print("// generated by generic_order_system.py")
    print("// t=%d, safe gauges=%s" % (data["t"], "ON" if data["gauged"] else "OFF"))
    print("ring R=%s,(%s),dp;" % (characteristic, ",".join(map(str, variables))))
    print("option(redSB);")
    if controls:
        print('print("CONTROL_EMPTY_START");')
        print("ideal CE=c,T*c-1; ideal GE=std(CE);")
        print('if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); }'
              ' else { print("CONTROL_EMPTY_FAIL"); }')
        print('print("CONTROL_NONEMPTY_START");')
        print("ideal CN=c-1,T*c-1; ideal GN=std(CN);")
        print('if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); }'
              ' else { print("CONTROL_NONEMPTY_FAIL"); }')
    generators = [singular(eq) for _, _, eq in tagged] + ["T*c-1"]
    print('print("MAIN_START equations=%d chart_unknowns=%d plus_T=1");' %
          (len(tagged), len(data["params"]) + 1))
    print("ideal I=%s;" % ",\n".join(generators))
    print("ideal G=std(I);")
    print('print("MAIN_DONE basis_size="); size(G);')
    print('if (reduce(1,G)==0) { print("SATURATED_EMPTY"); }'
          ' else { print("NONTRIVIAL"); }')
    if print_basis:
        print("G;")
    print("quit;")


def audit(data, tagged, elapsed):
    by_h = collections.Counter(hp for hp, _, _ in tagged)
    alpha_count = sum(map(len, data["alpha_spaces"].values()))
    beta_count = sum(map(len, data["beta_spaces"].values()))
    print("K16 gauged fixed-t order chart")
    print("  t=%d e=%d q=%d" % (data["t"], data["e"], data["q"]))
    print("  alpha=%d beta=%d b=4 c=1 chart_unknowns=%d" %
          (alpha_count, beta_count, len(data["params"]) + 1))
    print("  equations=%d h_histogram=%s" %
          (len(tagged), json.dumps(dict(sorted(by_h.items())))))
    print("  build_seconds=%.3f" % elapsed)
    # Exact deterministic reconstruction check on the full by-power identity.
    sample = {v: (k % 7) - 3 for k, v in enumerate(data["params"])}
    hs = data["h"].subs(sample)
    direct = jac(data["Q"].subs(sample), data["P"].subs(sample))
    rebuilt = sum(rem.subs(sample) * hs**hp for hp, rem in data["by_power"].items())
    ok = sp.expand(direct - rebuilt) == 0
    print("  h_adic_reconstruction=%s" % ok)
    assert ok


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--t", type=int, required=True)
    parser.add_argument("--ungauged", action="store_true")
    parser.add_argument("--low-h-max", type=int)
    parser.add_argument("--high-h-min", type=int)
    parser.add_argument("--emit-singular", action="store_true")
    parser.add_argument("--modulus", type=int, default=0)
    parser.add_argument("--controls", action="store_true")
    parser.add_argument("--no-basis", action="store_true")
    args = parser.parse_args()
    started = time.time()
    data = build(args.t, gauged=not args.ungauged)
    tagged = selected_equations(data, args.low_h_max, args.high_h_min)
    if args.emit_singular:
        emit_singular(data, tagged, args.modulus, args.controls,
                      print_basis=not args.no_basis)
    else:
        audit(data, tagged, time.time() - started)


if __name__ == "__main__":
    main()
