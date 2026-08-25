#!/usr/bin/env python3
"""Independent integer license for the vertical D7 E1+M residual.

The predecessor review licensed only degrees nine and eight.  This replay
starts from the integer Jacobian ingredients and proves that in the charged
vertical normal form the full degree-seven part of E1 is exactly the
single-Frobenius K/3 term used by the D7 producer.
"""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
import runpy
from collections import defaultdict
from pathlib import Path


ROOT = Path(os.environ.get("JC2_ROOT", Path(__file__).resolve().parents[2]))
GEN = (ROOT / "cases" /
       "as_fonly_d7_postd10_d98_f3_corrected_20260824" /
       "generate_corrected.py")


def expr(name, coefficient=1):
    return {(name,): coefficient}


def eadd(*items):
    out = defaultdict(int)
    for item in items:
        for monomial, coefficient in item.items():
            out[tuple(sorted(monomial))] += coefficient
    return {m: c for m, c in out.items() if c}


def emul(left, right):
    out = defaultdict(int)
    for lm, lc in left.items():
        for rm, rc in right.items():
            out[tuple(sorted(lm + rm))] += lc * rc
    return {m: c for m, c in out.items() if c}


def padd(*items):
    out = {}
    for item in items:
        for monomial, coefficient in item.items():
            out[monomial] = eadd(out.get(monomial, {}), coefficient)
    return {m: c for m, c in out.items() if c}


def pscale(scalar, poly):
    return {m: {v: scalar * c for v, c in e.items()}
            for m, e in poly.items()}


def pmul(left, right):
    out = {}
    for (i, j), le in left.items():
        for (k, ell), re in right.items():
            key = (i + k, j + ell)
            out[key] = eadd(out.get(key, {}), emul(le, re))
    return {m: c for m, c in out.items() if c}


def derivative(poly, axis):
    out = {}
    for (i, j), coefficient in poly.items():
        exponent = (i, j)[axis]
        if exponent:
            key = (i - 1, j) if axis == 0 else (i, j - 1)
            out[key] = {m: exponent * c for m, c in coefficient.items()}
    return out


def mod3(poly):
    return {xy: {m: c % 3 for m, c in e.items() if c % 3}
            for xy, e in poly.items()
            if any(c % 3 for c in e.values())}


def divided_mod3(poly, divisor):
    for coefficient in poly.values():
        assert all(value % divisor == 0 for value in coefficient.values())
    return mod3({xy: {m: c // divisor for m, c in e.items()}
                 for xy, e in poly.items()})


def homogeneous(prefix, degree):
    return {(i, degree - i): expr(f"{prefix}{degree}_{i}")
            for i in range(degree + 1)}


def degree_part(poly, degree):
    return {xy: e for xy, e in poly.items() if sum(xy) == degree}


def max_degree(poly):
    return max((sum(xy) for xy, e in poly.items() if e), default=-1)


def canonical_hash(poly):
    payload = []
    for xy, coefficient in sorted(poly.items()):
        payload.append([list(xy), [[list(m), c]
                                  for m, c in sorted(coefficient.items())]])
    raw = json.dumps(payload, separators=(",", ":"), sort_keys=False).encode()
    return hashlib.sha256(raw).hexdigest()


# Charged vertical normal form, over Z before any reduction.
U0 = {
    (2, 1): expr("h"),
    (0, 4): expr("p"), (1, 3): expr("r", 2),
    (3, 1): expr("q"), (4, 0): expr("t", 2),
}
V0 = {
    (1, 2): expr("h", 2), (2, 1): {(): 1},
    (0, 4): expr("r"), (1, 3): expr("s"),
    (3, 1): expr("t"), (4, 0): expr("w"),
}
UF = {(0, 6): expr("fua"), (3, 3): expr("fa"),
      (6, 0): expr("fb")}
VF = {(0, 6): expr("fc"), (3, 3): expr("fd"),
      (6, 0): expr("fvb")}
U = padd(U0, UF)
V = padd(V0, VF)
C = padd(homogeneous("c", 6), homogeneous("c", 7))
D = padd(homogeneous("d", 6), homogeneous("d", 7))

ux0, uy0 = derivative(U0, 0), derivative(U0, 1)
vx0, vy0 = derivative(V0, 0), derivative(V0, 1)
ux, uy = derivative(U, 0), derivative(U, 1)
vx, vy = derivative(V, 0), derivative(V, 1)
ufx, ufy = derivative(UF, 0), derivative(UF, 1)
vfx, vfy = derivative(VF, 0), derivative(VF, 1)
cx, cy = derivative(C, 0), derivative(C, 1)
dx, dy = derivative(D, 0), derivative(D, 1)
x2 = {(2, 0): {(): -1}}
A0 = padd(ux0, x2)
A = padd(ux, x2)

L = padd(ux, vy, x2)
L1 = {xy: {m: c // 3 for m, c in e.items()}
      for xy, e in L.items()}
assert all(c % 3 == 0 for e in L.values() for c in e.values())
assert max_degree(L1) <= 5
assert max_degree(padd(cx, dy)) <= 6

K0 = padd(pmul(A0, vy0), pscale(-1, pmul(uy0, vx0)))
K = padd(pmul(A, vy), pscale(-1, pmul(uy, vx)))
Kdouble = padd(pmul(ufx, vfy), pscale(-1, pmul(ufy, vfx)))
Ksingle = padd(
    pmul(ufx, vy0), pmul(A0, vfy),
    pscale(-1, pmul(ufy, vx0)), pscale(-1, pmul(uy0, vfx)),
)
assert padd(K, pscale(-1, K0), pscale(-1, Ksingle),
            pscale(-1, Kdouble)) == {}
assert max_degree(K0) <= 6
assert divided_mod3(Kdouble, 3) == {}

# At total degree seven, E=L/3+K+Cx+Dy has only K.  Its quotient is formal:
# each coefficient of K_7 is divisible by three before any field equation.
K7 = degree_part(K, 7)
E1_7 = divided_mod3(K7, 3)
single_7 = degree_part(divided_mod3(Ksingle, 3), 7)
assert E1_7 == single_7

M = padd(pmul(A, dy), pmul(cx, vy),
         pscale(-1, pmul(uy, dx)), pscale(-1, pmul(cy, vx)))
M0 = padd(pmul(A0, dy), pmul(cx, vy0),
          pscale(-1, pmul(uy0, dx)), pscale(-1, pmul(cy, vx0)))
assert mod3(M) == mod3(M0)
residual7 = degree_part(mod3(padd(M, E1_7)), 7)

# Regression only: compare the independently derived full source residual to
# the frozen D9/D8 generator's formula, then apply its licensed algebraic
# substitutions and assert the eight displayed D7 rows.
os.environ["BRANCH"] = "vertical"
os.environ.pop("ENUMERATE", None)
os.environ.pop("STRUCTURAL", None)
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(GEN))
generated = {xy: ns["esubstitute"](e, ns["normal"])
             for xy, e in ns["Rfull"].items() if sum(xy) == 7}
generated = {xy: e for xy, e in generated.items() if e}
assert residual7 == generated


def solved_row(index):
    e = residual7.get((index, 7 - index), {})
    e = ns["esubstitute"](e, ns["sub_digits"])
    e = ns["esubstitute"](e, ns["normal"])
    e = ns["esubstitute"](e, ns["pivot_sub"])
    e = ns["esubstitute"](e, ns["coord"])
    return e


v = ns["var"]
predicted = [
    ns["escale"](2, ns["emul"](v("fua"), v("h"))),
    ns["eadd"](ns["emul"](v("fc"), v("h")),
               ns["escale"](2, v("fua"))),
    v("fc"),
    ns["eadd"](v("d6_1"),
               ns["escale"](2, ns["emul"](v("fa"), v("h")))),
    ns["eadd"](v("Rr"), ns["emul"](v("fd"), v("h"))),
    ns["escale"](2, v("fd")),
    ns["eadd"](v("d6_4"),
               ns["escale"](2, ns["emul"](v("fb"), v("h")))),
    ns["eadd"](v("Tt"), v("fb"), ns["emul"](v("fvb"), v("h"))),
]
actual = [solved_row(i) for i in range(8)]
assert actual == predicted

print("degree_caps", "L1", max_degree(L1), "Cx+Dy",
      max_degree(padd(cx, dy)), "Kbase", max_degree(K0))
print("double_frobenius_after_div3_mod3", divided_mod3(Kdouble, 3))
print("E1_degree7_term_count", sum(len(e) for e in E1_7.values()))
print("E1_degree7_sha256", canonical_hash(E1_7))
print("full_residual_degree7_term_count",
      sum(len(e) for e in residual7.values()))
print("full_residual_degree7_sha256", canonical_hash(residual7))
for i, row in enumerate(actual):
    print(f"D7_{i}_{7-i}", ns["sexpr"](row))
print("PASS-D7-FULL-E1-DEGREE7-SOURCE-LICENSE")
