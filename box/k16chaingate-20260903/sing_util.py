#!/usr/bin/env python3
"""Emit a homogeneous std+dim Singular job and run it with an explicit timeout."""
from __future__ import annotations

import subprocess
from pathlib import Path

import sympy as sp

HERE = Path("/home/ubuntu/jc2/box/k16chaingate-20260903")


def clear_poly(expr: sp.Expr, gens) -> sp.Expr:
    expr = sp.together(sp.expand(expr))
    num, den = sp.fraction(expr)
    num = sp.expand(num)
    den = sp.expand(den)
    if den == 0:
        raise ValueError("zero denominator")
    # drop a content denominator in Q
    return sp.numer(sp.together(num))


def to_sing(expr: sp.Expr, y: sp.Symbol) -> str:
    s = str(sp.expand(expr)).replace(str(y), "Y").replace("**", "^")
    return s


def write_and_run(name: str, varnames: list[str], gens: list[str], timeout: int) -> str:
    body = ",\n".join(gens)
    lines = [
        "ring R=0,(%s),dp;" % ",".join(varnames),
        "ideal I=",
        body + ";",
        "ideal G=std(I);",
        'printf("NAME=%s DIM=%%s NGENS=%%s", dim(G), size(G));' % name,
        'printf("LEADMON=%s", lead(G));',
        "quit;",
    ]
    p = HERE / f"{name}.sing"
    p.write_text("\n".join(lines) + "\n")
    outp = HERE / f"{name}.out"
    errp = HERE / f"{name}.err"
    proc = subprocess.run(
        ["timeout", str(timeout), "Singular", "-q", str(p)],
        capture_output=True,
        text=True,
    )
    outp.write_text(proc.stdout)
    errp.write_text(proc.stderr)
    print("SING", name, "rc", proc.returncode, "stdout:", proc.stdout.strip()[:400])
    if proc.stderr.strip():
        print("  stderr:", proc.stderr.strip()[:300])
    return proc.stdout
