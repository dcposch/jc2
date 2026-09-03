#!/usr/bin/env python3
"""Finite-field discovery version of terminal_laurent_model.py.

For each requested t this chooses a good prime for which H_t splits, runs the
Laurent/Euler recurrence on both y fibres, and emits the top-t invariant
terminal subsystem for Singular.  These runs are discovery evidence only.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import pathlib
import time

import sympy as sp


OUT = pathlib.Path("/home/ubuntu/jc2/box/k16spine-20260903")


@dataclasses.dataclass
class Row:
    band: int
    expr: sp.Expr


class Field:
    def __init__(self, prime, variables):
        self.p = int(prime)
        self.variables = list(variables)

    def reduce(self, expr):
        numerator, denominator = sp.cancel(expr).as_numer_denom()
        if denominator.free_symbols:
            raise ZeroDivisionError("non-scalar modular denominator")
        denominator_mod = int(denominator) % self.p
        if denominator_mod == 0:
            raise ZeroDivisionError("bad modular denominator")
        inverse = pow(denominator_mod, -1, self.p)
        return sp.Poly(sp.expand(numerator)*inverse, *self.variables,
                       modulus=self.p).as_expr()

    def scalar(self, expr):
        value = self.reduce(expr)
        if value.free_symbols or value == 0:
            raise ZeroDivisionError(value)
        return int(value) % self.p

    def inverse(self, expr):
        value = self.scalar(expr)
        inverse = pow(value, -1, self.p)
        answer = self.reduce(inverse)
        if self.reduce(expr*answer-1) != 0:
            raise AssertionError("finite-field inverse failed")
        return answer


def coeffs(expr, variable, field):
    poly = sp.Poly(field.reduce(expr), variable, *[v for v in field.variables
                                                   if v != variable],
                   modulus=field.p)
    answer = {}
    for monomial, coefficient in poly.terms():
        power = monomial[0]
        rest = sp.Integer(coefficient)
        for variable2, exponent in zip(
                [v for v in field.variables if v != variable], monomial[1:]):
            rest *= variable2**exponent
        answer[power] = answer.get(power, 0)+rest
    return {power: field.reduce(value) for power, value in answer.items()}


def affine(expr, variable, field):
    coefficient = field.reduce(sp.diff(expr, variable))
    remainder = field.reduce(expr-coefficient*variable)
    if (variable in coefficient.free_symbols or variable in remainder.free_symbols
            or coefficient == 0 or coefficient.free_symbols):
        return None
    return coefficient, remainder


def choose_prime_and_roots(t, start):
    p = int(sp.nextprime(start-1))
    while True:
        if p not in {2, 3} and (2*t+1) % p and all(k % p for k in range(1, 8*t+20)):
            square = (t+1)*pow(3, -1, p) % p
            roots = sp.sqrt_mod(square, p, all_roots=True)
            if len(roots) == 2:
                q = 2*t+1
                ys = sorted({((root+t+1)*pow(2*q, -1, p)) % p for root in roots})
                if len(ys) == 2:
                    return p, roots, ys
        p = int(sp.nextprime(p+1))


def build_fibre(t, p, yvalue):
    started = time.monotonic()
    e, q, N = 3*t+1, 2*t+1, 4*t+1
    h, s = sp.symbols("h s")
    b1, b2, b3, b4 = sp.symbols("b1 b2 b3 b4")
    beta0 = sp.Symbol("B0")
    uvars = [sp.Symbol("q%d_0" % j) for j in range(2, 2*t+1)]
    cvars = [sp.Symbol("C%d" % j) for j in range(1, t)]
    z = sp.Symbol("z")
    rs = [sp.Symbol("r%d" % i) for i in range(2, t)]
    variables = [h, s, b1, b2, b3, b4, beta0]+uvars+cvars+[z]+rs
    F = Field(p, variables)
    y = sp.Integer(yvalue)
    yinv = F.inverse(y)
    g1 = F.reduce(sp.Rational(e, q))
    g2 = F.reduce(sp.Rational(e, q)*y+sp.Rational(e*t, 2*q*q))
    g = F.reduce(sp.Rational(e*t, q*q)*y-sp.Rational(e*t*(t+1), 6*q**3))

    U_h = h**q+sum(u*h**(q-j) for j, u in enumerate(uvars, start=2))
    C_h = h**(t-1)+sum(v*h**(t-1-j) for j, v in enumerate(cvars, start=1))
    U = F.reduce(U_h.subs(h, s+b4))
    C = F.reduce(C_h.subs(h, s+b4))
    A = F.reduce(s*C)
    Bprime = F.reduce(g*yinv*(5*C+3*s*sp.diff(C, s))/2)
    B = beta0
    for power, coefficient in coeffs(Bprime, s, F).items():
        B += coefficient*s**(power+1)*pow(power+1, -1, p)
    B = F.reduce(B)
    if F.reduce(sp.diff(B, s)-Bprime) != 0:
        raise AssertionError("B derivative")
    if F.reduce(sp.Poly(B, s).LC()-g2) != 0:
        raise AssertionError("B leading")

    rhs = F.reduce(3*g*sp.diff(U, s)+A*B-s*A*sp.diff(B, s)
                   +2*s*sp.diff(A, s)*B
                   +g*b3*(A/s+sp.Rational(5, 2)*sp.diff(A, s)))
    D = 0
    for power, coefficient in coeffs(rhs, s, F).items():
        D += coefficient*yinv*pow(2*power+1, -1, p)*s**power
    D = F.reduce(D)
    if F.reduce(y*(D+2*s*sp.diff(D, s))-rhs) != 0:
        raise AssertionError("D Euler")
    if F.reduce(sp.Poly(D, s).LC()-g1) != 0:
        raise AssertionError("D leading")

    V = F.reduce(s*A-y*b3)
    Y = F.reduce(s*D-b3*B-g*b2)
    Z = F.reduce(s*B-g*b3)
    numerator = F.reduce(y*g*b1-V*sp.diff(Y, s)+sp.diff(V, s)*Y
                         +2*sp.diff(U, s)*Z)
    condition = F.reduce(numerator.subs(s, 0))
    ab1 = affine(condition, b1, F)
    if ab1 is None:
        raise AssertionError("b1 pivot")
    b1rhs = F.reduce(-F.inverse(ab1[0])*ab1[1])
    numerator = F.reduce(numerator.subs(b1, b1rhs))
    numerator_coefficients = coeffs(numerator, s, F)
    if F.reduce(numerator_coefficients.get(0, 0)) != 0:
        raise AssertionError("s divisibility")
    quotient = sum(value*s**(power-1) for power, value
                   in numerator_coefficients.items() if power > 0)
    Xprime = F.reduce(quotient*yinv/2)
    if F.reduce(sp.Poly(Xprime, s).LC()-e) != 0:
        raise AssertionError("X leading")
    Xh = F.reduce(Xprime.subs(s, h-b4))
    gauge = F.reduce(coeffs(Xh, h, F).get(q-1, 0))
    aB0 = affine(gauge, beta0, F)
    if aB0 is None:
        raise AssertionError("B0 gauge")
    B0rhs = F.reduce(-F.inverse(aB0[0])*aB0[1])
    sub = {beta0: B0rhs}
    U, V, Y, Xprime = [F.reduce(item.subs(sub)) for item in (U, V, Y, Xprime)]
    R = F.reduce((V*Xprime-sp.diff(U, s)*Y-y*g).subs(s, h-b4))
    cd = coeffs(R, h, F)
    rows = [Row(k, F.reduce(cd.get(k, 0))) for k in range(N+1)]

    eliminate = cvars+[sp.Symbol("q%d_0" % j) for j in range(t, 2*t+1)]+[b2]
    pivots = []
    active = rows
    deferrals = 0
    while eliminate:
        chosen = None
        for ri, row in sorted(enumerate(active), key=lambda item: -item[1].band):
            if row.band < 2*t or row.expr == 0:
                continue
            for vi, variable in enumerate(eliminate):
                aa = affine(row.expr, variable, F)
                if aa is None:
                    continue
                try:
                    inverse = F.inverse(aa[0])
                except ZeroDivisionError:
                    deferrals += 1
                    continue
                chosen = ri, vi, row, variable, aa, inverse
                break
            if chosen:
                break
        if chosen is None:
            raise RuntimeError("no modular high pivot")
        ri, vi, row, variable, aa, inverse = chosen
        rhs = F.reduce(-inverse*aa[1])
        del active[ri]
        del eliminate[vi]
        active = [Row(item.band, F.reduce(item.expr.subs(variable, rhs)))
                  for item in active]
        pivots.append({"band": row.band, "variable": str(variable),
                       "coefficient": str(aa[0])})
    if any(row.expr != 0 for row in active if row.band >= 2*t):
        raise AssertionError("nonzero modular high remainder")
    terminal = sorted([row for row in active if row.band < 2*t and row.expr != 0],
                      key=lambda row: row.band)
    if [row.band for row in terminal] != list(range(2*t)):
        raise AssertionError("modular terminal bands")
    residual = [b3, b4]+uvars[:max(0, t-2)]

    # The top t terminal rows are homogeneous after b3=z*b4^(t+1),
    # q_i=r_i*b4^i.  Set b4=1 to record their invariant factors.
    invariants = []
    for row in terminal:
        if row.band < t:
            continue
        subscale = {b4: 1, b3: z}
        subscale.update({u: r for u, r in zip(uvars[:max(0, t-2)], rs)})
        invariants.append((row.band, F.reduce(row.expr.subs(subscale))))
    return {
        "t": t, "prime": p, "y": yvalue,
        "pivots": pivots, "deferrals": deferrals,
        "terminal": [{"band": row.band, "expr": str(row.expr)} for row in terminal],
        "invariant_variables": list(map(str, [z]+rs)),
        "top_invariants": [{"band": band, "expr": str(expr)}
                           for band, expr in invariants],
        "elapsed_seconds": time.monotonic()-started,
    }


def emit_singular(record):
    variables = record["invariant_variables"]
    rows = [item["expr"].replace("**", "^") for item in record["top_invariants"]]
    return "\n".join([
        "// modular discovery only",
        "ring R=%d,(%s),dp;" % (record["prime"], ",".join(variables)),
        "option(redSB);",
        'print("MAIN t=%d y=%d top_rows=%d");'
        % (record["t"], record["y"], len(rows)),
        "ideal I=%s;" % ",\n".join(rows),
        "ideal G=std(I);",
        'if (reduce(1,G)==0) { print("UNIT"); } else { print("NONUNIT"); }',
        "size(G);",
        "quit;",
    ])+"\n"


def emit_b4_specialization(record, value):
    t = record["t"]
    variables = ["b3"]+["q%d_0" % i for i in range(2, t)]
    b4 = sp.Symbol("b4")
    local = {"b4": b4}
    local.update({name: sp.Symbol(name) for name in variables})
    rows = []
    for item in record["terminal"]:
        expr = sp.sympify(item["expr"], locals=local).subs(b4, value)
        expr = sp.Poly(sp.expand(expr), *[local[name] for name in variables],
                       modulus=record["prime"]).as_expr()
        rows.append(str(expr).replace("**", "^"))
    return "\n".join([
        "// modular discovery; all terminal rows with b4=%d" % value,
        "ring R=%d,(%s),dp;" % (record["prime"], ",".join(variables)),
        "option(redSB);",
        'print("MAIN t=%d y=%d b4=%d rows=%d");'
        % (t, record["y"], value, len(rows)),
        "ideal I=%s;" % ",\n".join(rows),
        "ideal G=std(I);",
        'if (reduce(1,G)==0) { print("UNIT"); } else { print("NONUNIT"); }',
        "size(G);",
        "quit;",
    ])+"\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("t", type=int, nargs="+")
    parser.add_argument("--prime-start", type=int, default=100003)
    args = parser.parse_args()
    for t in args.t:
        p, ds, ys = choose_prime_and_roots(t, args.prime_start)
        print("PARAM", t, p, ds, ys, flush=True)
        for branch, y in enumerate(ys):
            record = build_fibre(t, p, y)
            path = OUT/("terminal_mod_t%d_p%d_branch%d.json" % (t, p, branch))
            path.write_text(json.dumps(record, indent=2, sort_keys=True)+"\n",
                            encoding="utf-8")
            sing = OUT/("terminal_mod_t%d_p%d_branch%d.sing" % (t, p, branch))
            sing.write_text(emit_singular(record), encoding="utf-8")
            for b4value in (0, 1):
                special = OUT/("terminal_mod_t%d_p%d_branch%d_b4_%d.sing"
                              % (t, p, branch, b4value))
                special.write_text(emit_b4_specialization(record, b4value),
                                   encoding="utf-8")
            print(json.dumps({"t": t, "p": p, "branch": branch, "y": y,
                              "seconds": record["elapsed_seconds"],
                              "singular": str(sing)}, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
