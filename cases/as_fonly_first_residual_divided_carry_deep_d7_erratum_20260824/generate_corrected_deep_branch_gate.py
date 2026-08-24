#!/usr/bin/env python3
"""Emit the source-honest first-digit acceptance scheme on the deep D7 branch.

The full first residual is the divided linear carry plus the quadratic carry.
Branch assumptions: degree seven is zero; degree six is Frobenius and hence
derivative-invisible for the cap-boundary and Cartier obstruction.  Retain
every coefficient of U,V in degrees 1..5.
"""
from __future__ import annotations
import os

RADICAL = os.environ.get("RADICAL", "0") == "1"
COVER = os.environ.get("COVER", "0") == "1"
Expr = dict[tuple[str, ...], int]
XYPoly = dict[tuple[int, int], Expr]


def enormal(expr: Expr) -> Expr:
    return {monomial: coefficient % 3 for monomial, coefficient in expr.items()
            if coefficient % 3}


def eadd(*expressions: Expr) -> Expr:
    out: Expr = {}
    for expr in expressions:
        for monomial, coefficient in expr.items():
            out[monomial] = out.get(monomial, 0) + coefficient
    return enormal(out)


def escale(scalar: int, expr: Expr) -> Expr:
    return enormal({monomial: scalar*coefficient
                    for monomial, coefficient in expr.items()})


def emul(left: Expr, right: Expr) -> Expr:
    out: Expr = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            monomial = tuple(sorted(lm+rm))
            out[monomial] = out.get(monomial, 0) + lc*rc
    return enormal(out)


def xadd(*polynomials: XYPoly) -> XYPoly:
    out: XYPoly = {}
    for polynomial in polynomials:
        for xy, expr in polynomial.items():
            out[xy] = eadd(out.get(xy, {}), expr)
    return {xy: expr for xy, expr in out.items() if expr}


def xscale(scalar: int, polynomial: XYPoly) -> XYPoly:
    return {xy: escale(scalar, expr) for xy, expr in polynomial.items()
            if escale(scalar, expr)}


def xmul(left: XYPoly, right: XYPoly) -> XYPoly:
    out: XYPoly = {}
    for (i, j), le in left.items():
        for (k, ell), re in right.items():
            target = (i+k, j+ell)
            out[target] = eadd(out.get(target, {}), emul(le, re))
    return {xy: expr for xy, expr in out.items() if expr}


def derivative(polynomial: XYPoly, variable: int) -> XYPoly:
    out: XYPoly = {}
    for (i, j), expr in polynomial.items():
        exponent = i if variable == 0 else j
        if exponent % 3:
            target = (i-1, j) if variable == 0 else (i, j-1)
            out[target] = eadd(out.get(target, {}), escale(exponent, expr))
    return {xy: expr for xy, expr in out.items() if expr}


def singular_expr(expr: Expr) -> str:
    pieces = []
    for monomial, coefficient in sorted(expr.items()):
        factor = "*".join(monomial) if monomial else "1"
        pieces.append(factor if coefficient == 1 else f"2*{factor}")
    return "+".join(pieces) if pieces else "0"


variables = [f"{side}{degree}_{i}"
             for degree in range(1, 6)
             for side in ("u", "v")
             for i in range(degree+1)]
U: XYPoly = {}
V: XYPoly = {}
for degree in range(1, 6):
    for i in range(degree+1):
        monomial = (i, degree-i)
        U[monomial] = {(f"u{degree}_{i}",): 1}
        V[monomial] = {(f"v{degree}_{i}",): 1}

ux, uy = derivative(U, 0), derivative(U, 1)
vx, vy = derivative(V, 0), derivative(V, 1)
divergence = xadd(ux, vy, {(2, 0): {(): -1}})
K = xadd(xmul(ux, vy), xscale(-1, xmul(uy, vx)),
         xscale(-1, xmul({(2, 0): {(): 1}}, vy)))

rows: list[Expr] = []
row_labels = []
for total in range(5):
    for i in range(total+1):
        expr = divergence.get((i, total-i), {})
        if expr:
            rows.append(expr)
            row_labels.append(f"div_{i}_{total-i}")
for total in (8, 7):
    for i in range(total+1):
        expr = K.get((i, total-i), {})
        if expr:
            rows.append(expr)
            row_labels.append(f"carry_{i}_{total-i}")
bracket_cartier = K.get((2, 2), {})
assert not bracket_cartier
# Over integer representatives, (U_x+V_y-x^2)/3 contributes here.
# Only x^3*y^2 in U and x^2*y^3 in V can contribute.
divided_linear_cartier = {("u5_3",): 1, ("v5_2",): 1}
rows.append(divided_linear_cartier)
row_labels.append("divided_linear_cartier_2_2")

print('ring r=3,(' + ','.join(variables) + '),dp;')
print('LIB "primdec.lib"; option(redSB);')
print('ideal I=' + ','.join(singular_expr(row) for row in rows) + ';')
print('ideal G=std(I);')
print('print("variables/rows/Gsize/dim");')
print(f'print({len(variables)}); print({len(rows)}); print(size(G)); print(dim(G));')
print('print("row_labels"); print("' + ','.join(row_labels) + '");')
if RADICAL:
    print('ideal R=std(radical(I)); ideal IR=reduce(R,G);')
    print('print("radical_size/original_is_radical"); print(size(R));')
    print('if (size(IR)==0) { print(1); } else { print(0); }')
if COVER:
    print('poly q4=u4_3^2*v4_1^2+u4_3*v4_0*v4_1*v4_3'
          '-u4_0*v4_1*v4_3^2-u4_3*v4_0^2*v4_4'
          '+u4_0*u4_3*v4_1*v4_4+u4_0*v4_0*v4_3*v4_4'
          '+u4_0^2*v4_4^2;')
    print('print("separator_q4");print(q4);')
    print('list S0=sat(I,ideal(q4)); ideal Q0=std(S0[1]); int n0=2;')
    print('ideal B=std(I+ideal(q4^n0)); ideal J0=std(intersect(Q0,B));')
    print('list S1=sat(B,ideal(u5_0)); ideal Q1=std(S1[1]); int n1=2;')
    print('ideal E=std(B+ideal(u5_0^n1)); ideal J1=std(intersect(Q1,E));')
    print('ideal J=std(intersect(Q0,J1));')
    print('ideal JI=reduce(J,G); ideal IJ=reduce(G,J);')
    print('ideal J0I=reduce(J0,G); ideal IJ0=reduce(G,J0);')
    print('print("saturation_exponents");print(n0);print(n1);')
    print('print("recursive_piece_dims_sizes");')
    print('print(dim(Q0));print(size(Q0));print(dim(Q1));print(size(Q1));')
    print('print(dim(E));print(size(E));')
    print('print("two_sided_remainders_J0_vs_I");print(size(J0I));print(size(IJ0));')
    print('print("two_sided_remainders_triple_cover_vs_I");print(size(JI));print(size(IJ));')
    print('print("intersection_equalities");')
    print('if(size(J0I)==0 && size(IJ0)==0){print(1);}else{print(0);}')
    print('if(size(JI)==0 && size(IJ)==0){print(1);}else{print(0);}')
    print('if(size(J0I)!=0 || size(IJ0)!=0 || size(JI)!=0 || size(IJ)!=0)'
          '{print("FAIL-COVER");exit(1);}')
print('print("PASS-DEEP-BRANCH");')
