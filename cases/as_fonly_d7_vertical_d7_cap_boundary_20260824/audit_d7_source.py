#!/usr/bin/env python3
"""Independent symbolic-integer source audit of the corrected D7 rows."""
from __future__ import annotations

import contextlib
import io
import os
import runpy
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GEN = (ROOT / "cases" /
       "as_fonly_d7_postd10_d98_f3_corrected_20260824" /
       "generate_corrected.py")
os.environ["BRANCH"] = "vertical"
os.environ.pop("ENUMERATE", None)
os.environ.pop("STRUCTURAL", None)
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(GEN))


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
            out[tuple(sorted(lm+rm))] += lc*rc
    return {m: c for m, c in out.items() if c}


def padd(*items):
    out = {}
    for item in items:
        for monomial, coefficient in item.items():
            out[monomial] = eadd(out.get(monomial, {}), coefficient)
    return {m: c for m, c in out.items() if c}


def pscale(scalar, poly):
    return {m: {v: scalar*c for v, c in e.items()}
            for m, e in poly.items()}


def pmul(left, right):
    out = {}
    for (i, j), le in left.items():
        for (k, ell), re in right.items():
            key = (i+k, j+ell)
            out[key] = eadd(out.get(key, {}), emul(le, re))
    return {m: c for m, c in out.items() if c}


def derivative(poly, axis):
    out = {}
    for (i, j), coefficient in poly.items():
        exponent = (i, j)[axis]
        if exponent:
            key = (i-1, j) if axis == 0 else (i, j-1)
            out[key] = {m: exponent*c for m, c in coefficient.items()}
    return out


def mod3(poly):
    return {xy: {m: c % 3 for m, c in e.items() if c % 3}
            for xy, e in poly.items()
            if any(c % 3 for c in e.values())}


def divided_mod3(poly, divisor):
    for coefficient in poly.values():
        assert all(value % divisor == 0 for value in coefficient.values())
    return mod3({xy: {m: c//divisor for m, c in e.items()}
                 for xy, e in poly.items()})


def homogeneous(prefix, degree):
    return {(i, degree-i): expr(f"{prefix}{degree}_{i}")
            for i in range(degree+1)}


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
UF = {(0, 6): expr("fua"), (3, 3): expr("fa"), (6, 0): expr("fb")}
VF = {(0, 6): expr("fc"), (3, 3): expr("fd"), (6, 0): expr("fvb")}
C = padd(homogeneous("c", 6), homogeneous("c", 7))
D = padd(homogeneous("d", 6), homogeneous("d", 7))

ux, uy = derivative(U0, 0), derivative(U0, 1)
vx, vy = derivative(V0, 0), derivative(V0, 1)
cx, cy = derivative(C, 0), derivative(C, 1)
dx, dy = derivative(D, 0), derivative(D, 1)
A0 = padd(ux, {(2, 0): {(): -1}})

# Literal mixed second-digit term M modulo three.
M = mod3(padd(
    pmul(A0, dy), pmul(cx, vy),
    pscale(-1, pmul(uy, dx)), pscale(-1, pmul(cy, vx)),
))

# Exact integer single-Frobenius cross in K, divided by three before mod 3.
AF = derivative(UF, 0)
UFy = derivative(UF, 1)
VFx = derivative(VF, 0)
VFy = derivative(VF, 1)
K0 = padd(pmul(A0, vy), pscale(-1, pmul(uy, vx)))
Kfull = padd(
    pmul(padd(A0, AF), padd(vy, VFy)),
    pscale(-1, pmul(padd(uy, UFy), padd(vx, VFx))),
)
KFdiv = divided_mod3(padd(Kfull, pscale(-1, K0)), 3)
R = mod3(padd(M, KFdiv))

# Compare the independently generated source polynomial before any solved-row
# substitution.
generated = {xy: ns["esubstitute"](e, ns["normal"])
             for xy, e in ns["Rfull"].items()}
generated = {xy: e for xy, e in generated.items() if e}
assert R == generated


def solved_row(poly, index):
    e = poly.get((index, 7-index), {})
    e = ns["esubstitute"](e, ns["sub_digits"])
    e = ns["esubstitute"](e, ns["normal"])
    e = ns["esubstitute"](e, ns["pivot_sub"])
    e = ns["esubstitute"](e, ns["coord"])
    return e


v = ns["var"]
predicted = [
    ns["escale"](2, ns["emul"](v("fua"), v("h"))),
    ns["eadd"](ns["emul"](v("fc"), v("h")), ns["escale"](2, v("fua"))),
    v("fc"),
    ns["eadd"](v("d6_1"), ns["escale"](2, ns["emul"](v("fa"), v("h")))),
    ns["eadd"](v("Rr"), ns["emul"](v("fd"), v("h"))),
    ns["escale"](2, v("fd")),
    ns["eadd"](v("d6_4"), ns["escale"](2, ns["emul"](v("fb"), v("h")))),
    ns["eadd"](v("Tt"), v("fb"), ns["emul"](v("fvb"), v("h"))),
]
actual = [solved_row(R, i) for i in range(8)]
assert actual == predicted, (actual, predicted)

# Negative control: omitting the divided Frobenius source while retaining the
# corrected accepted-row/pivot transformations changes every final row, so
# the old source cannot recover this gate.
old = [solved_row(M, i) for i in range(8)]
changed = [i for i, (a, b) in enumerate(zip(old, actual)) if a != b]
assert changed == list(range(8)), changed

print("source_row_count", len(actual))
for i, row in enumerate(actual):
    print(f"D7_{i}_{7-i}", ns["sexpr"](row))
print("omit_KFdiv_changed_rows", changed)
print("PASS-D7-INTEGER-SOURCE-AUDIT")
