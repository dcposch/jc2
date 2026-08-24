#!/usr/bin/env python3
"""Emit the Singular primary-decomposition gate for the top D7 first digit.

Let u,v be homogeneous degree-seven parts over F3.  The first determinant
digit imposes div(u,v)=0.  The degree-twelve part of the next carry is
det D(u,v), because the fixed -x^2 term has lower degree.  This generator
emits the exact linear plus quadratic coefficient ideal in 16 variables.
"""
from __future__ import annotations
import os

M = int(os.environ.get("M", "7"))
assert 1 <= M <= 7
BRIEF = os.environ.get("BRIEF", "0") == "1"
DO_PRIMARY = os.environ.get("DO_PRIMARY", "0") == "1"


def term(coefficient, left, right=None):
    coefficient %= 3
    if not coefficient:
        return None
    monomial = left if right is None else f"{left}*{right}"
    return monomial if coefficient == 1 else f"2*{monomial}"


def expression(terms):
    kept = [value for value in terms if value is not None]
    return "+".join(kept) if kept else "0"


# Derivative dictionaries: xy monomial -> list (coefficient, variable).
ux, uy, vx, vy = {}, {}, {}, {}
for i in range(M+1):
    j = M-i
    if i % 3:
        ux.setdefault((i-1, j), []).append((i, f"a{i}"))
        vx.setdefault((i-1, j), []).append((i, f"b{i}"))
    if j % 3:
        uy.setdefault((i, j-1), []).append((j, f"a{i}"))
        vy.setdefault((i, j-1), []).append((j, f"b{i}"))


def product(left, right, sign=1):
    out = {}
    for (i, j), lterms in left.items():
        for (k, ell), rterms in right.items():
            target = (i+k, j+ell)
            for lc, lv in lterms:
                for rc, rv in rterms:
                    out.setdefault(target, []).append((sign*lc*rc, lv, rv))
    return out


det = product(ux, vy, 1)
for monomial, terms in product(uy, vx, -1).items():
    det.setdefault(monomial, []).extend(terms)

variables = [f"a{i}" for i in range(M+1)] + [f"b{i}" for i in range(M+1)]
equations = []
for i in range(M):
    # coefficient x^i y^(M-1-i) of ux+vy
    equations.append(expression([
        term(i+1, f"a{i+1}"),
        term(M-i, f"b{i}"),
    ]))
for i in range(2*M-1):
    monomial = (i, 2*M-2-i)
    equations.append(expression([
        term(coefficient, left, right)
        for coefficient, left, right in det.get(monomial, [])
    ]))
equations = [equation for equation in equations if equation != "0"]

print('ring r=3,(' + ','.join(variables) + '),dp;')
print('LIB "primdec.lib";')
print('option(redSB);')
print('ideal I=' + ','.join(equations) + ';')
print('ideal G=std(I);')
print('print("variables/equations/Gsize");')
print(f'print({len(variables)}); print({len(equations)}); print(size(G));')
print('print("dimension"); print(dim(G));')
print('list L=minAssGTZ(I);')
print('print("minimal_associated_count"); print(size(L));')
print('ideal origin=' + ','.join(variables) + '; ideal incidence;')
print('for (int k=1; k<=size(L); k++) {')
print('  ideal A=std(L[k]);')
if BRIEF:
    print('  print("component"); print(k); print(dim(A)); print(size(A));')
else:
    print('  print("component"); print(k); print(dim(A)); print(vdim(A)); print(A);')
print('  incidence=reduce(A,std(origin));')
print('  print("origin_on_component"); if (size(incidence)==0) { print(1); } else { print(0); }')
print('}')
print('ideal R=std(radical(I));')
print('if (size(L)==2) {')
print('  ideal K=std(intersect(L[1],L[2]));')
print('  print("radical/intersection_sizes"); print(size(R)); print(size(K));')
print('  ideal RK=reduce(R,K); ideal KR=reduce(K,R);')
print('  print("radical_equals_minimal_intersection");')
print('  if (size(RK)==0 && size(KR)==0) { print(1); } else { print(0); }')
print('}')
print('ideal IR=reduce(R,G);')
print('print("original_is_radical");')
if BRIEF:
    print('if (size(IR)==0) { print(1); } else { print(0); }')
else:
    print('if (size(IR)==0) { print(1); } else { print(0); print(IR); }')
if DO_PRIMARY:
    print('list PD=primdecGTZ(I);')
    print('print("primary_component_count"); print(size(PD));')
    print('ideal qideal; ideal pideal;')
    print('for (int q=1; q<=size(PD); q++) {')
    print('  qideal=std(PD[q][1]); pideal=std(PD[q][2]);')
    print('  print("primary/prime dims and sizes"); print(q);')
    print('  print(dim(qideal)); print(size(qideal)); print(dim(pideal)); print(size(pideal));')
    if not BRIEF:
        print('  print("primary ideal"); print(qideal);')
    print('}')
print('print("PASS-TOP-COMPONENTS");')
