#!/usr/bin/env python3
"""Emit the exact p=3 D7 degree-10 accepted-digit gate."""
from __future__ import annotations
import os

MATRIX = os.environ.get("MATRIX", "0") == "1"
Expr = dict[tuple[str, ...], int]
Poly = dict[tuple[int, int], Expr]


def norm(e: Expr) -> Expr:
    return {m: c % 3 for m, c in e.items() if c % 3}


def eadd(*es: Expr) -> Expr:
    out: Expr = {}
    for e in es:
        for m, c in e.items():
            out[m] = out.get(m, 0) + c
    return norm(out)


def escale(a: int, e: Expr) -> Expr:
    return norm({m: a*c for m, c in e.items()})


def emul(a: Expr, b: Expr) -> Expr:
    out: Expr = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            m = tuple(sorted(ma+mb))
            out[m] = out.get(m, 0) + ca*cb
    return norm(out)


def padd(*ps: Poly) -> Poly:
    out: Poly = {}
    for p in ps:
        for m, e in p.items():
            out[m] = eadd(out.get(m, {}), e)
    return {m: e for m, e in out.items() if e}


def pscale(a: int, p: Poly) -> Poly:
    return {m: escale(a, e) for m, e in p.items() if escale(a, e)}


def pmul(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for (i, j), ea in a.items():
        for (k, ell), eb in b.items():
            m = (i+k, j+ell)
            out[m] = eadd(out.get(m, {}), emul(ea, eb))
    return {m: e for m, e in out.items() if e}


def derivative(p: Poly, var: int) -> Poly:
    out: Poly = {}
    for (i, j), e in p.items():
        n = i if var == 0 else j
        if n % 3:
            m = (i-1, j) if var == 0 else (i, j-1)
            out[m] = eadd(out.get(m, {}), escale(n, e))
    return {m: e for m, e in out.items() if e}


def sexpr(e: Expr) -> str:
    terms = []
    for m, c in sorted(e.items()):
        f = "*".join(m) if m else "1"
        terms.append(f if c == 1 else "2*"+f)
    return "+".join(terms) if terms else "0"


def esubstitute(e: Expr, replacements: dict[str, Expr]) -> Expr:
    out: Expr = {}
    for monomial, coefficient in e.items():
        term: Expr = {(): coefficient}
        for factor in monomial:
            term = emul(term, replacements.get(factor, {(factor,): 1}))
        out = eadd(out, term)
    return out


def coefficient(e: Expr, variable: str) -> Expr:
    out: Expr = {}
    for monomial, value in e.items():
        if variable in monomial:
            reduced = list(monomial)
            reduced.remove(variable)
            m = tuple(reduced)
            out[m] = out.get(m, 0) + value
    return norm(out)


def homogeneous(prefix: str, degree: int) -> tuple[Poly, list[str]]:
    p: Poly = {}
    names = []
    for i in range(degree+1):
        name = f"{prefix}{degree}_{i}"
        names.append(name)
        p[(i, degree-i)] = {(name,): 1}
    return p, names


U: Poly = {}
V: Poly = {}
base_vars: list[str] = []
for degree in (3, 4, 5):
    h, names = homogeneous("u", degree)
    U = padd(U, h)
    base_vars += names
    h, names = homogeneous("v", degree)
    V = padd(V, h)
    base_vars += names
C, cvars = homogeneous("c", 7)
D, dvars = homogeneous("d", 7)
digit_vars = cvars+dvars

ux, uy = derivative(U, 0), derivative(U, 1)
vx, vy = derivative(V, 0), derivative(V, 1)
cx, cy = derivative(C, 0), derivative(C, 1)
dx, dy = derivative(D, 0), derivative(D, 1)
div = padd(ux, vy, {(2, 0): {(): -1}})
A = padd(ux, {(2, 0): {(): -1}})
K = padd(pmul(A, vy), pscale(-1, pmul(uy, vx)))
M = padd(pmul(A, dy), pmul(cx, vy),
         pscale(-1, pmul(uy, dx)), pscale(-1, pmul(cy, vx)))

base_rows: list[Expr] = []
base_labels: list[str] = []
for total in (2, 3, 4):
    for i in range(total+1):
        e = div.get((i, total-i), {})
        if e:
            base_rows.append(e)
            base_labels.append(f"div_{i}_{total-i}")
for total in (8, 7):
    for i in range(total+1):
        e = K.get((i, total-i), {})
        if e:
            base_rows.append(e)
            base_labels.append(f"carry_{i}_{total-i}")
base_rows.append({("u5_3",): 1, ("v5_2",): 1})
base_labels.append("divided_linear_cartier_2_2")

digit_rows: list[Expr] = []
digit_labels: list[str] = []
accepted = padd(K, cx, dy)
for i in range(7):
    e = accepted.get((i, 6-i), {})
    if e:
        digit_rows.append(e)
        digit_labels.append(f"accepted_div_{i}_{6-i}")
for i in range(11):
    e = M.get((i, 10-i), {})
    if e:
        digit_rows.append(e)
        digit_labels.append(f"mixed_carry_{i}_{10-i}")

all_vars = digit_vars+base_vars
rows = base_rows+digit_rows
print('ring r=3,(' + ','.join(all_vars) + '),dp;')
print('LIB "elim.lib"; option(redSB);')
print('ideal Ibase=' + ','.join(sexpr(e) for e in base_rows) + ';')
print('ideal Idigit=' + ','.join(sexpr(e) for e in digit_rows) + ';')
print('ideal I=Ibase+Idigit;')
print('print("base_vars/base_rows/digit_vars/digit_rows");')
print(f'print({len(base_vars)});print({len(base_rows)});'
      f'print({len(digit_vars)});print({len(digit_rows)});')
print('print("base_labels");print("'+','.join(base_labels)+'");')
print('print("digit_labels");print("'+','.join(digit_labels)+'");')
if MATRIX:
    k6 = [K.get((i, 6-i), {}) for i in range(7)]
    free = ["c7_0", "c7_3", "c7_6", "d7_0", "d7_1",
            "d7_3", "d7_4", "d7_6", "d7_7"]
    sub: dict[str, Expr] = {name: {(name,): 1} for name in free}
    sub.update({
        "c7_1": eadd(escale(-1, k6[0]), escale(-1, sub["d7_0"])),
        "c7_2": k6[1],
        "d7_2": k6[2],
        "c7_4": eadd(escale(-1, k6[3]), escale(-1, sub["d7_3"])),
        "c7_5": k6[4],
        "d7_5": k6[5],
        "c7_7": eadd(escale(-1, k6[6]), escale(-1, sub["d7_6"])),
    })
    mixed = [esubstitute(M.get((i, 10-i), {}), sub)
             for i in range(11) if M.get((i, 10-i), {})]
    matrix = [[coefficient(row, f) for f in free] for row in mixed]
    rhs = []
    for row in mixed:
        affine = row
        for f in free:
            affine = eadd(affine, escale(-1, emul(coefficient(row, f), {(f,): 1})))
        rhs.append(affine)
    print('matrix A[8][9]=' + ','.join(sexpr(e) for row in matrix for e in row) + ';')
    print('matrix b[8][1]=' + ','.join(sexpr(e) for e in rhs) + ';')
    augmented = [row+[rhs[i]] for i, row in enumerate(matrix)]
    print('matrix Aug[8][10]=' +
          ','.join(sexpr(e) for row in augmented for e in row) + ';')
    print('print("reduced_matrix_shape/free_vars");print(nrows(A));print(ncols(A));'
          'print("'+','.join(free)+'");')
print('print("PASS-DEGREE10-GATE");')
