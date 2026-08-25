#!/usr/bin/env python3
"""Emit the g!=0 chart of the exact D7 degree-10 pointwise gate."""
from __future__ import annotations

import contextlib
import io
import os
import runpy

os.environ["MATRIX"] = "1"
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(
        os.path.join(os.path.dirname(__file__), "generate_degree10_gate.py")
    )

eadd, escale, emul = ns["eadd"], ns["escale"], ns["emul"]
esubstitute, sexpr = ns["esubstitute"], ns["sexpr"]


def var(name):
    return {(name,): 1}


def power(name, exponent):
    return {tuple([name] * exponent): 1} if exponent else {(): 1}


def product(*expressions):
    out = {(): 1}
    for expression in expressions:
        out = emul(out, expression)
    return out


linear = {
    "u3_1": {}, "u3_2": var("h"),
    "v3_1": escale(2, var("h")), "v3_2": {(): 1},
    "u4_0": var("p"), "u4_1": escale(2, var("r")),
    "u4_2": {}, "u4_3": var("q"), "u4_4": escale(2, var("t")),
    "v4_0": var("r"), "v4_1": var("s"), "v4_2": {},
    "v4_3": var("t"), "v4_4": var("w"),
    "u5_0": var("a"), "u5_1": var("b"), "u5_2": var("c"),
    "u5_3": var("d"), "u5_4": var("e"), "u5_5": var("f"),
    "v5_0": var("b"), "v5_1": var("c"),
    "v5_2": escale(2, var("d")), "v5_3": var("e"),
    "v5_4": var("f"), "v5_5": var("g"),
}

kz = lambda n: product(var("k"), power("z", n))
chart = {
    "g": var("k"), "f": kz(1), "e": kz(2), "d": kz(3),
    "c": escale(2, kz(4)), "b": escale(2, kz(5)),
    "a": escale(2, kz(6)),
    "p": eadd(product(var("s"), power("z", 2)),
                  escale(2, product(var("r"), var("z")))),
    "q": eadd(product(var("w"), power("z", 2)),
                  escale(2, product(var("t"), var("z")))),
}


def sub(expression):
    return esubstitute(esubstitute(expression, linear), chart)


matrix = [[sub(entry) for entry in row] for row in ns["matrix"]]
rhs = [sub(entry) for entry in ns["rhs"]]
allowed = {"h", "r", "s", "t", "w", "k", "z"}
for expression in rhs + [entry for row in matrix for entry in row]:
    for monomial in expression:
        assert set(monomial) <= allowed, (monomial, set(monomial)-allowed)

print("ring R=3,(h,r,s,t,w,k,z),dp;")
print('LIB "elim.lib"; option(redSB);')
print("matrix A[8][9]=" + ",".join(sexpr(e) for row in matrix for e in row) + ";")
print("matrix bvec[8][1]=" + ",".join(sexpr(e) for e in rhs) + ";")
augmented = [row + [rhs[i]] for i, row in enumerate(matrix)]
print("matrix Aug[8][10]=" + ",".join(
    sexpr(e) for row in augmented for e in row
) + ";")
print("ideal A4=minor(A,4);ideal A3=minor(A,3);ideal Aug4=minor(Aug,4);")
print("ideal GA4=std(A4);ideal GA3=std(A3);")
print('print("A4_size_A3_size");print(size(GA4));print(size(GA3));')
print("list S=sat(Aug4,ideal(k));ideal J=std(S[1]);")
print('print("compatibility_size_dim");print(size(J));print(dim(J));print(J);')
print('print("g_chart_rhs");print(bvec);')
print('print("PASS-MAIN-G-CHART");')
