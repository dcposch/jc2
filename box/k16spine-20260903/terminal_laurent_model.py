#!/usr/bin/env python3
"""Lean exact recurrence for the K=16 terminal family.

Put r=pi^(-1), s=h-b4.  After the proved first spine the chart has

  Q=U+V*r+W*r^2,       P=X+Y*r+Z*r^2+T*r^3,

and J(h,r)=r^(-1).  Hence J(Q,P)=c*gamma is equivalent to one polynomial
identity in r.  This script uses its r^4,r^2,r^1,r^0 coefficients to build
the second spine and its terminal r^0 remainder without expanding the
original gamma,pi chart.

This is currently a discovery/checking driver.  Every division in A_t is
checked by multiplication modulo H_t, and every affine substitution is
checked on its pivot row.
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
class BandRow:
    band: int
    expr: sp.Expr


class Algebra:
    def __init__(self, t, y, polynomial_variables):
        self.t = t
        self.y = y
        q = 2*t+1
        self.H = sp.expand(
            12*q*q*y*y-12*q*(t+1)*y+(t+1)*(3*t+2)
        )
        self.variables = list(polynomial_variables)
        self.domain = sp.QQ[tuple(self.variables)]
        self.hpoly = sp.Poly(self.H, y, domain=self.domain)

    def reduce(self, expr):
        numerator, denominator = sp.cancel(expr).as_numer_denom()
        npoly = sp.Poly(sp.expand(numerator), self.y, domain=self.domain)
        dpoly = sp.Poly(sp.expand(denominator), self.y, domain=self.domain)
        nrem = npoly.rem(self.hpoly)
        drem = dpoly.rem(self.hpoly)
        # In this driver all non-rational denominators are A_t scalars.
        if drem.degree() > 0:
            dinv = sp.invert(
                sp.Poly(drem.as_expr(), self.y, domain=sp.QQ),
                sp.Poly(self.H, self.y, domain=sp.QQ),
            ).as_expr()
            answer = nrem.as_expr()*dinv
        else:
            answer = nrem.as_expr()/drem.as_expr()
        return sp.expand(
            sp.Poly(sp.expand(answer), self.y, domain=self.domain)
            .rem(self.hpoly).as_expr()
        )

    def inverse(self, expr):
        expr = self.reduce(expr)
        if expr == 0 or expr.free_symbols - {self.y}:
            raise ZeroDivisionError(expr)
        inverse = sp.invert(
            sp.Poly(expr, self.y, domain=sp.QQ),
            sp.Poly(self.H, self.y, domain=sp.QQ),
        ).as_expr()
        inverse = self.reduce(inverse)
        if self.reduce(expr*inverse-1) != 0:
            raise AssertionError("bad inverse")
        return inverse


def coefficients(expr, variable):
    poly = sp.Poly(sp.expand(expr), variable)
    return {monomial[0]: coefficient for monomial, coefficient in poly.terms()}


def euler_inverse(rhs, s, yinv, algebra):
    """Solve y*(D+2*s*D')=rhs coefficientwise in the s basis."""
    answer = 0
    for power, coefficient in coefficients(rhs, s).items():
        answer += algebra.reduce(coefficient*yinv/sp.Integer(2*power+1))*s**power
    answer = algebra.reduce(answer)
    if algebra.reduce((answer+2*s*sp.diff(answer, s))/yinv-rhs) != 0:
        raise AssertionError("Euler inverse check failed")
    return answer


def affine_decompose(expr, variable, algebra):
    derivative = algebra.reduce(sp.diff(expr, variable))
    remainder = algebra.reduce(expr-derivative*variable)
    if variable in derivative.free_symbols or variable in remainder.free_symbols:
        return None
    if derivative == 0 or derivative.free_symbols - {algebra.y}:
        return None
    if algebra.reduce(expr-derivative*variable-remainder) != 0:
        raise AssertionError("affine decomposition check failed")
    return derivative, remainder


def build(t: int):
    if t < 2:
        raise ValueError("stable model begins at t=2")
    started = time.monotonic()
    e, q, N = 3*t+1, 2*t+1, 4*t+1
    h, s = sp.symbols("h s")
    y = sp.Symbol("q%d_1" % q)
    b1, b2, b3, b4 = sp.symbols("b1 b2 b3 b4")
    uvars = [sp.Symbol("q%d_0" % j) for j in range(2, 2*t+1)]
    cvars = [sp.Symbol("C%d" % j) for j in range(1, t)]
    beta0 = sp.Symbol("B0")
    allvars = [h, s, b1, b2, b3, b4, beta0] + uvars + cvars
    algebra = Algebra(t, y, allvars)
    yinv = algebra.inverse(y)

    d = 2*q*y-(t+1)
    g1 = sp.Rational(e, q)
    g2 = algebra.reduce(sp.Rational(e, q)*y + sp.Rational(e*t, 2*q*q))
    g = algebra.reduce(
        sp.Rational(e*t, q*q)*y-sp.Rational(e*t*(t+1), 6*q**3)
    )
    c = algebra.reduce(-y*g)

    U_h = h**q + sum(u*h**(q-j) for j, u in enumerate(uvars, start=2))
    C_h = h**(t-1) + sum(
        variable*h**(t-1-j) for j, variable in enumerate(cvars, start=1)
    )
    U = sp.expand(U_h.subs(h, s+b4))
    C = sp.expand(C_h.subs(h, s+b4))
    A = sp.expand(s*C)

    Bprime = algebra.reduce(g*yinv*(5*C+3*s*sp.diff(C, s))/2)
    B = beta0
    for power, coefficient in coefficients(Bprime, s).items():
        B += coefficient*s**(power+1)/sp.Integer(power+1)
    B = algebra.reduce(B)
    if algebra.reduce(sp.diff(B, s)-Bprime) != 0:
        raise AssertionError("B recurrence failed")
    if algebra.reduce(sp.Poly(B, s).LC()-g2) != 0:
        raise AssertionError("B leading coefficient disagrees with normalizer")

    rhs_D = algebra.reduce(
        3*g*sp.diff(U, s)
        + A*B-s*A*sp.diff(B, s)+2*s*sp.diff(A, s)*B
        + g*b3*(A/s+sp.Rational(5, 2)*sp.diff(A, s))
    )
    D = euler_inverse(rhs_D, s, yinv, algebra)
    if algebra.reduce(sp.Poly(D, s).LC()-g1) != 0:
        raise AssertionError("D leading coefficient disagrees with normalizer")

    V = algebra.reduce(s*A-y*b3)
    W = y*s
    Y = algebra.reduce(s*D-b3*B-g*b2)
    Z = algebra.reduce(s*B-g*b3)
    T = g*s

    # r^1 identity: choose b1 so its numerator is divisible by s, then X'.
    numerator = algebra.reduce(
        y*g*b1-V*sp.diff(Y, s)+sp.diff(V, s)*Y+2*sp.diff(U, s)*Z
    )
    constant = algebra.reduce(numerator.subs(s, 0))
    affine_b1 = affine_decompose(constant, b1, algebra)
    if affine_b1 is None:
        raise AssertionError("b1 divisibility condition is not affine-unit")
    b1_coefficient, b1_remainder = affine_b1
    b1_inverse = algebra.inverse(b1_coefficient)
    b1_rhs = algebra.reduce(-b1_inverse*b1_remainder)
    numerator = algebra.reduce(numerator.subs(b1, b1_rhs))
    quotient, remainder = sp.div(sp.Poly(numerator, s), sp.Poly(s, s))
    if algebra.reduce(remainder.as_expr()) != 0:
        raise AssertionError("r^1 numerator is not divisible by s")
    Xprime = algebra.reduce(quotient.as_expr()*yinv/2)
    if algebra.reduce(sp.Poly(Xprime, s).LC()-e) != 0:
        raise AssertionError("X' leading coefficient disagrees")

    # alpha_t=0 means [h^(q-1)]X'=0.  It eliminates the free constant of B.
    Xprime_h = algebra.reduce(Xprime.subs(s, h-b4))
    gauge = algebra.reduce(sp.Poly(Xprime_h, h).coeff_monomial(h**(q-1)))
    affine_B0 = affine_decompose(gauge, beta0, algebra)
    if affine_B0 is None:
        raise AssertionError("X gauge is not affine-unit in B0")
    B0_coefficient, B0_remainder = affine_B0
    B0_inverse = algebra.inverse(B0_coefficient)
    B0_rhs = algebra.reduce(-B0_inverse*B0_remainder)

    substitutions = {beta0: B0_rhs}
    U = algebra.reduce(U.subs(substitutions))
    C = algebra.reduce(C.subs(substitutions))
    A = algebra.reduce(A.subs(substitutions))
    B = algebra.reduce(B.subs(substitutions))
    D = algebra.reduce(D.subs(substitutions))
    V = algebra.reduce(V.subs(substitutions))
    Y = algebra.reduce(Y.subs(substitutions))
    Z = algebra.reduce(Z.subs(substitutions))
    Xprime = algebra.reduce(Xprime.subs(substitutions))
    b1_rhs = algebra.reduce(b1_rhs.subs(substitutions))
    if algebra.reduce(gauge.subs(substitutions)) != 0:
        raise AssertionError("X gauge substitution failed")

    # r^0 identity.  Its high h-coefficients form the remaining affine spine;
    # its bands 0..2t-1 are the terminal family.
    R_s = algebra.reduce(V*Xprime-sp.diff(U, s)*Y-y*g)
    R_h = algebra.reduce(R_s.subs(s, h-b4))
    coeff = coefficients(R_h, h)
    rows = [BandRow(k, algebra.reduce(coeff.get(k, 0))) for k in range(N+1)]

    eliminate = cvars + [sp.Symbol("q%d_0" % j) for j in range(t, 2*t+1)] + [b2]
    pivot_record = []
    active = rows
    while eliminate:
        chosen = None
        # Highest band first; variable order is fixed above.
        for row_index, row in sorted(enumerate(active),
                                     key=lambda item: (-item[1].band, item[0])):
            if row.expr == 0 or row.band < 2*t:
                continue
            for variable_index, variable in enumerate(eliminate):
                affine = affine_decompose(row.expr, variable, algebra)
                if affine is None:
                    continue
                try:
                    inverse = algebra.inverse(affine[0])
                except Exception:
                    continue
                chosen = (row_index, variable_index, row, variable,
                          affine[0], affine[1], inverse)
                break
            if chosen is not None:
                break
        if chosen is None:
            raise RuntimeError({
                "reason": "no high affine unit pivot",
                "remaining": list(map(str, eliminate)),
                "nonzero_high": [(row.band, str(row.expr)) for row in active
                                 if row.band >= 2*t and row.expr != 0],
            })
        row_index, variable_index, row, variable, coefficient, rem, inverse = chosen
        rhs = algebra.reduce(-inverse*rem)
        if algebra.reduce(row.expr.subs(variable, rhs)) != 0:
            raise AssertionError("high pivot substitution failed")
        del active[row_index]
        del eliminate[variable_index]
        active = [
            BandRow(item.band, algebra.reduce(item.expr.subs(variable, rhs)))
            for item in active
        ]
        pivot_record.append({
            "band": row.band,
            "variable": str(variable),
            "coefficient": str(coefficient),
            "inverse": str(inverse),
            "resultant": str(sp.factor(sp.resultant(algebra.H, coefficient, y))),
            "rhs": str(rhs),
        })

    nonzero_high = [row for row in active if row.band >= 2*t and row.expr != 0]
    if nonzero_high:
        raise AssertionError(
            "unresolved high rows: %s" % [(row.band, row.expr) for row in nonzero_high]
        )
    terminal = sorted(
        [row for row in active if row.band < 2*t and row.expr != 0],
        key=lambda row: row.band,
    )
    if [row.band for row in terminal] != list(range(2*t)):
        raise AssertionError("terminal bands differ")
    residual_variables = [b3, b4] + uvars[:max(0, t-2)]
    if any(row.expr.free_symbols - ({y} | set(residual_variables)) for row in terminal):
        raise AssertionError("eliminated variable remains in terminal")
    record = {
        "typing": "exact Laurent/Euler recurrence in A_t",
        "t": t,
        "H": str(algebra.H),
        "d": str(d),
        "normalizer": {"g1": str(g1), "g2": str(g2), "g3": str(g), "c": str(c)},
        "b1_divisibility_pivot": {
            "coefficient": str(b1_coefficient), "inverse": str(b1_inverse),
            "rhs": str(b1_rhs),
        },
        "B0_gauge_pivot": {
            "coefficient": str(B0_coefficient), "inverse": str(B0_inverse),
            "rhs": str(B0_rhs),
        },
        "high_pivots": pivot_record,
        "terminal_variables": list(map(str, residual_variables)),
        "terminal": [{"band": row.band, "expr": str(row.expr)} for row in terminal],
        "elapsed_seconds": time.monotonic()-started,
    }
    return record


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("t", type=int, nargs="+")
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    for t in args.t:
        record = build(t)
        path = OUT/("terminal_laurent_t%d.json" % t)
        path.write_text(json.dumps(record, indent=2, sort_keys=True)+"\n",
                        encoding="utf-8")
        print(json.dumps({
            "t": t, "pivots": len(record["high_pivots"])+2,
            "terminal_rows": len(record["terminal"]),
            "terminal_variables": record["terminal_variables"],
            "elapsed_seconds": record["elapsed_seconds"], "path": str(path),
        }, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
