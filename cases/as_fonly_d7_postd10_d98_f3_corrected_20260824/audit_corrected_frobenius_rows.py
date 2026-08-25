#!/usr/bin/env python3
"""Independent symbolic-integer audit of the corrected divided K cross."""
from __future__ import annotations

import contextlib
import io
import os
import runpy
from collections import defaultdict
from pathlib import Path

path = str(Path(__file__).with_name("generate_corrected.py"))


def expr(name, coefficient=1):
    return {(name,): coefficient}


def eaddz(*items):
    out = defaultdict(int)
    for item in items:
        for monomial, coefficient in item.items():
            out[tuple(sorted(monomial))] += coefficient
    return {m: c for m, c in out.items() if c}


def emulz(left, right):
    out = defaultdict(int)
    for lm, lc in left.items():
        for rm, rc in right.items():
            out[tuple(sorted(lm+rm))] += lc*rc
    return {m: c for m, c in out.items() if c}


def paddz(*items):
    out = {}
    for item in items:
        for monomial, coefficient in item.items():
            out[monomial] = eaddz(out.get(monomial, {}), coefficient)
    return {m: c for m, c in out.items() if c}


def pscalez(scalar, poly):
    return {m: {v: scalar*c for v, c in e.items()}
            for m, e in poly.items()}


def pmulz(left, right):
    out = {}
    for (i, j), le in left.items():
        for (k, ell), re in right.items():
            key = (i+k, j+ell)
            out[key] = eaddz(out.get(key, {}), emulz(le, re))
    return {m: c for m, c in out.items() if c}


def dz(poly, axis):
    out = {}
    for (i, j), coefficient in poly.items():
        exponent = (i, j)[axis]
        if exponent:
            key = (i-1, j) if axis == 0 else (i, j-1)
            out[key] = {m: exponent*c for m, c in coefficient.items()}
    return out


def normalize_mod3(poly):
    return {xy: {m: c % 3 for m, c in e.items() if c % 3}
            for xy, e in poly.items()
            if any(c % 3 for c in e.values())}


def divided_mod3(poly, divisor):
    for coefficient in poly.values():
        assert all(value % divisor == 0 for value in coefficient.values())
    return normalize_mod3({xy: {m: c//divisor for m, c in e.items()}
                           for xy, e in poly.items()})


def build(branch):
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
    if branch == "g":
        U0[(0, 4)] = {}
        U0[(3, 1)] = {}
        V0[(5, 0)] = expr("g")
    U0 = {m: e for m, e in U0.items() if e}
    V0 = {m: e for m, e in V0.items() if e}
    UF = {
        (0, 6): expr("fua"), (3, 3): expr("fa"), (6, 0): expr("fb")
    }
    VF = {
        (0, 6): expr("fc"), (3, 3): expr("fd"), (6, 0): expr("fvb")
    }
    A0 = paddz(dz(U0, 0), {(2, 0): {(): -1}})
    AF = dz(UF, 0)
    U0y, UFy = dz(U0, 1), dz(UF, 1)
    V0x, VFx = dz(V0, 0), dz(VF, 0)
    V0y, VFy = dz(V0, 1), dz(VF, 1)
    K0 = paddz(pmulz(A0, V0y), pscalez(-1, pmulz(U0y, V0x)))
    Kfull = paddz(
        pmulz(paddz(A0, AF), paddz(V0y, VFy)),
        pscalez(-1, pmulz(paddz(U0y, UFy), paddz(V0x, VFx))),
    )
    diff = paddz(Kfull, pscalez(-1, K0))
    quotient = divided_mod3(diff, 3)

    os.environ["BRANCH"] = "vertical"
    with contextlib.redirect_stdout(io.StringIO()):
        ns = runpy.run_path(path)
    normal = dict(ns["normal"])
    if branch == "g":
        normal.update({"u4_0": {}, "u4_3": {}, "v5_5": {("g",): 1}})
    generated = {xy: ns["esubstitute"](e, normal)
                 for xy, e in ns["KFdiv"].items()}
    generated = {xy: e for xy, e in generated.items() if e}
    assert quotient == generated, (branch, quotient, generated)
    high = sorted((xy, e) for xy, e in quotient.items() if sum(xy) >= 8)
    print(branch, "max_degree", max(map(sum, quotient), default=-1))
    print(branch, "high_terms", high)
    return quotient


vertical = build("vertical")
gendpoint = build("g")
assert max(map(sum, vertical), default=-1) == 8
assert max(map(sum, gendpoint), default=-1) == 9
print("PASS-CORRECTED-DIVIDED-FROBENIUS-ROWS")
