#!/usr/bin/env python3
"""Generate the exact Moh p.208 (16,12; J=c*x) coefficient equations.

This is a source-form control: h, alpha_i and beta_i are transcribed from
Moh p.208.  It prints sparse diagnostics and a Singular input file; it does
not treat a timeout or an engine flag as mathematical emptiness.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import sympy as sp


x, y = sp.symbols("x y")
b1, b2, b3, b4 = bs = sp.symbols("b1:5")
a1 = sp.symbols("a1")  # Moh's constant alpha_1
cvars = sp.symbols("c1:14")
jc = sp.symbols("jc")

h = y**3 * (y - x) + b1*y**3 + b2*y**2 + b3*y + b4
A = sp.expand((h - b4) / y)
B = sp.expand((h - b3*y - b4) / y**2)
c = (None,) + cvars
alpha2 = c[1]*A + c[2]
beta2 = c[3]*A + c[4]
alpha3 = c[5]*A + c[6]*B + c[7]
beta3 = c[8]*A + c[9]*B + c[10]
alpha4 = c[11]*A + c[12]*B + c[13]*(y - x)

P = sp.expand(h**4 + a1*h**3 + alpha2*h**2 + alpha3*h + alpha4)
Q = sp.expand(h**3 + beta2*h + beta3)
J = sp.expand(sp.diff(Q, x)*sp.diff(P, y) - sp.diff(Q, y)*sp.diff(P, x))
target = sp.Poly(sp.expand(J - jc*x), x, y)
equations = [sp.factor(v) for v in target.coeffs() if v != 0]
generators = list(bs) + [a1] + list(cvars) + [jc]


def singular_text():
    names = ",".join(str(v) for v in generators) + ",T"
    polys = []
    for equation in equations:
        text = sp.sstr(sp.expand(equation)).replace("**", "^").lstrip()
        if text.startswith("+"):
            text = text[1:].lstrip()
        polys.append(text)
    sat = "T*jc-1"
    return "\n".join([
        f"ring r=0,({names}),dp;",
        "option(redSB);",
        "ideal I0=" + ",\n  ".join(polys) + ";",
        "ideal G0=std(I0);",
        'print("CONTROL_1612_UNSAT_BASIS_SIZE");',
        "size(G0);",
        'print("CONTROL_1612_UNSAT_REDUCE_ONE_REMAINDER");',
        "reduce(1,G0);",
        "ideal I=I0," + sat + ";",
        "ideal G=std(I);",
        'print("CONTROL_1612_BASIS_SIZE");',
        "size(G);",
        'print("CONTROL_1612_SAT_REDUCE_ONE_REMAINDER");',
        "reduce(1,G);",
        "ideal N=jc-1,T*jc-1;",
        "ideal GN=std(N);",
        'print("CONTROL_1612_NEGATIVE_BASIS_SIZE");',
        "size(GN);",
        'print("CONTROL_1612_NEGATIVE_REDUCE_ONE_REMAINDER");',
        "reduce(1,GN);",
        "quit;",
    ]) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--emit-singular", type=Path)
    args = ap.parse_args()
    print("h identity y*A+b4:", sp.expand(h - (y*A+b4)) == 0)
    print("h identity y^2*B+b3*y+b4:", sp.expand(h - (y**2*B+b3*y+b4)) == 0)
    print("degrees P,Q,J:", sp.Poly(P,y).degree(), sp.Poly(Q,y).degree(), sp.Poly(J,y).degree())
    print("variables:", len(generators), [str(v) for v in generators])
    print("coefficient equations:", len(equations))
    print("equations containing jc:", [e for e in equations if e.has(jc)])
    print("zero equations:", sum(e == 0 for e in target.coeffs()))
    if args.emit_singular:
        args.emit_singular.write_text(singular_text())
        print("wrote:", args.emit_singular)


if __name__ == "__main__":
    main()
