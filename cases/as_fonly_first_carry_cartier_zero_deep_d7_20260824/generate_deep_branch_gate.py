#!/usr/bin/env python3
"""Emit the complete first-digit acceptance scheme on the deep D7 branch.

Branch assumptions: degree seven is zero; degree six is Frobenius and hence
derivative-invisible.  Retain every coefficient of U,V in degrees 1..5.
Impose exact divergence, carry degrees 8/7, and the Cartier x^2*y^2 row.
"""
from __future__ import annotations
import os

DECOMP = os.environ.get("DECOMP", "0") == "1"
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
cartier = K.get((2, 2), {})
if cartier:
    rows.append(cartier)
    row_labels.append("cartier_2_2")

print('ring r=3,(' + ','.join(variables) + '),dp;')
print('LIB "primdec.lib"; option(redSB);')
print('ideal I=' + ','.join(singular_expr(row) for row in rows) + ';')
print('ideal G=std(I);')
print('print("variables/rows/Gsize/dim");')
print(f'print({len(variables)}); print({len(rows)}); print(size(G)); print(dim(G));')
print('print("row_labels"); print("' + ','.join(row_labels) + '");')
print('ideal R=std(radical(I)); ideal IR=reduce(R,G);')
print('print("radical_size/original_is_radical"); print(size(R));')
print('if (size(IR)==0) { print(1); } else { print(0); }')
if DECOMP:
    print('list L=minAssChar(I); print("minAss_count"); print(size(L));')
    print('for(int k=1;k<=size(L);k++){ ideal C=std(L[k]);')
    print(' print("component/dim/size");print(k);print(dim(C));print(size(C));}')
    print('poly q4=u4_3^2*v4_1^2+u4_3*v4_0*v4_1*v4_3'
          '-u4_0*v4_1*v4_3^2-u4_3*v4_0^2*v4_4'
          '+u4_0*u4_3*v4_1*v4_4+u4_0*v4_0*v4_3*v4_4'
          '+u4_0^2*v4_4^2;')
    print('print("saturation_separator_q4"); print(q4);')
    print('ideal top5=u5_0,u5_1,u5_2,u5_3,u5_4,u5_5,'
          'v5_0,v5_1,v5_2,v5_3,v5_4,v5_5;')
    print('ideal Z0=reduce(top5,std(L[1]));')
    print('ideal qL0=reduce(ideal(q4),std(L[1]));')
    print('ideal qL1=reduce(ideal(q4),std(L[2]));')
    print('ideal uL0=reduce(ideal(u5_0),std(L[1]));')
    print('ideal uL1=reduce(ideal(u5_0),std(L[2]));')
    print('print("rankzero_and_separator_membership");')
    print('if(size(Z0)==0){print(1);}else{print(0);}')
    print('if(size(qL0)==0){print(1);}else{print(0);}')
    print('if(size(qL1)==0){print(1);}else{print(0);}')
    print('if(size(uL0)==0){print(1);}else{print(0);}')
    print('if(size(uL1)==0){print(1);}else{print(0);}')
    print('list S0=sat(I,ideal(q4)); ideal Q0=std(S0[1]);')
    print('list S1=sat(I,ideal(u5_0)); ideal Q1=std(S1[1]);')
    print('ideal J=std(intersect(Q0,Q1));')
    print('ideal JI=reduce(J,G); ideal IJ=reduce(G,J);')
    print('print("saturation_dims_sizes");')
    print('print(dim(Q0));print(size(Q0));print(dim(Q1));print(size(Q1));')
    print('print("saturation_intersection_equals_original");')
    print('if(size(JI)==0 && size(IJ)==0){print(1);}else{print(0);}')
    print('ideal R0=std(radical(Q0)); ideal R1=std(radical(Q1));')
    print('ideal A00=reduce(R0,std(L[1])); ideal A01=reduce(std(L[1]),R0);')
    print('ideal A10=reduce(R1,std(L[2])); ideal A11=reduce(std(L[2]),R1);')
    print('print("saturation_radicals_match_minimal_primes");')
    print('if(size(A00)==0 && size(A01)==0){print(1);}else{print(0);}')
    print('if(size(A10)==0 && size(A11)==0){print(1);}else{print(0);}')
    print('print("saturation_radical_sizes");print(size(R0));print(size(R1));')
print('print("PASS-DEEP-BRANCH");')
