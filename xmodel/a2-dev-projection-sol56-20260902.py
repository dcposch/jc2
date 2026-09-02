#!/usr/bin/env python3
"""Source-first generator for the fully corrected A2 residual system.

The coefficient polynomial E2 is always ``b*Z*eta**2``.  The residual at
A-degree two is always named ``EQ2_even``.  No retired E1 wall is imposed.

Typical use:

    python3 xmodel/a2-dev-projection-sol56-20260902.py check
    python3 xmodel/a2-dev-projection-sol56-20260902.py system --format json
    python3 xmodel/a2-dev-projection-sol56-20260902.py devbox 2 --branch main
    python3 xmodel/a2-dev-projection-sol56-20260902.py devbox 2 --branch c0 \
        --format msolve
    python3 xmodel/a2-dev-projection-sol56-20260902.py t4ideal g1 --format msolve
    python3 xmodel/a2-dev-projection-sol56-20260902.py control --format msolve

The ``msolve`` format and its payload hash require msolveio 0.2.1; JSON output
remains available without that optional adapter.  The generator uses an
explicit Rabinowitsch equation; it never calls a saturation wrapper.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from typing import Any, Iterable

import sympy as sp


def dz(expr: sp.Expr, order: int = 1) -> sp.Expr:
    return sp.diff(expr, Z, order)


def norm(expr: sp.Expr) -> sp.Expr:
    return sp.cancel(sp.together(sp.expand(expr)))


def coeff(expr: sp.Expr, variable: sp.Symbol, exponent: int) -> sp.Expr:
    return sp.Poly(sp.expand(expr), variable, domain="EX").nth(exponent)


A, Z = sp.symbols("A Z")
a, b, c5, kappa = sp.symbols("a b c5 kappa")
eta = sp.Function("eta")(Z)
s = sp.Function("s")(Z)
p = sp.Function("p")(Z)
C1 = sp.Function("C1")(Z)
q = sp.Function("q")(Z)
r = sp.Function("r")(Z)
G = sp.Function("G")(Z)


def structure(c1_expr: sp.Expr = C1, s_expr: sp.Expr = s) -> dict[str, sp.Expr]:
    E2 = b * Z * eta**2
    D2 = a * Z * eta**3
    C2 = Z * eta * (3 * a * s_expr + c5 * eta) / (2 * b)
    E1 = dz(E2) + G
    D1 = dz(D2) + sp.Rational(3, 2) * a * eta * G / b
    return {"C1": c1_expr, "C2": C2, "D1": D1, "D2": D2,
            "E1": E1, "E2": E2}


def even_odd(st: dict[str, sp.Expr], s_expr: sp.Expr = s) -> tuple[sp.Expr, sp.Expr]:
    PP = p + A * st["C1"] + A**2 * st["C2"]
    QQ = q + A * st["D1"] + A**2 * st["D2"]
    RR = r + A * st["E1"] + A**2 * st["E2"]
    SS = s_expr
    H = A + A**2 * Z
    chi = 2 + 4 * A * Z

    def jac(x: sp.Expr, y: sp.Expr) -> sp.Expr:
        return sp.diff(x, A) * dz(y) - dz(x) * sp.diff(y, A)

    def wa(x: sp.Expr, y: sp.Expr) -> sp.Expr:
        return sp.diff(x, A) * y - x * sp.diff(y, A)

    def wz(x: sp.Expr, y: sp.Expr) -> sp.Expr:
        return dz(x) * y - x * dz(y)

    even = (
        2 * A**2 * (sp.diff(PP, A) * SS - QQ * sp.diff(RR, A))
        + 4 * H * (jac(PP, SS) + jac(QQ, RR))
        + chi * (QQ * dz(RR) - dz(PP) * SS)
    )
    odd = (
        2 * A**2 * wa(QQ, SS) + 4 * jac(PP, RR)
        + 4 * H * jac(QQ, SS) - chi * wz(QQ, SS)
    )
    return sp.expand(even), sp.expand(odd)


def residuals(st: dict[str, sp.Expr], s_expr: sp.Expr = s) -> dict[str, sp.Expr]:
    C1x, C2 = st["C1"], st["C2"]
    D1, D2, E1, E2 = st["D1"], st["D2"], st["E1"], st["E2"]
    rows: dict[str, sp.Expr] = {}
    rows["O0"] = 4 * (C1x * dz(r) - dz(p) * E1) + 2 * (q * dz(s_expr) - dz(q) * s_expr)
    rows["O1"] = (
        8 * (C2 * dz(r) - dz(p) * E2)
        + 4 * (C1x * dz(E1) - dz(C1x) * E1)
        + 6 * D1 * dz(s_expr) - 2 * dz(D1) * s_expr
        + 4 * Z * (q * dz(s_expr) - dz(q) * s_expr)
    )
    rows["O2"] = (
        4 * (C1x * dz(E2) - 2 * dz(C1x) * E2
             + 2 * C2 * dz(E1) - dz(C2) * E1)
        + 10 * D2 * dz(s_expr) - 2 * dz(D2) * s_expr + 2 * D1 * s_expr
        + 8 * Z * D1 * dz(s_expr) - 4 * Z * dz(D1) * s_expr
    )
    rows["E0"] = 2 * (q * dz(r) - dz(p) * s_expr) - kappa
    rows["EQ1_even"] = (
        6 * D1 * dz(r) - 4 * dz(q) * E1 + 2 * q * dz(E1)
        + 4 * C1x * dz(s_expr) - 2 * dz(C1x) * s_expr
        + 4 * Z * (q * dz(r) - dz(p) * s_expr)
    )
    rows["EQ2_even"] = (
        10 * D2 * dz(r) - 8 * dz(q) * E2 + 2 * q * dz(E2)
        + 6 * D1 * dz(E1) - 4 * dz(D1) * E1
        + 2 * C1x * s_expr + 8 * C2 * dz(s_expr) - 2 * dz(C2) * s_expr
        + 8 * Z * D1 * dz(r)
        + 4 * Z * (q * dz(E1) - dz(q) * E1
                   + C1x * dz(s_expr) - dz(C1x) * s_expr)
        - 2 * q * E1
    )
    rows["EQ3_even"] = (
        4 * C2 * s_expr - 4 * q * E2 - 2 * D1 * E1
        + 6 * D1 * dz(E2) - 8 * dz(D1) * E2
        + 10 * D2 * dz(E1) - 4 * dz(D2) * E1
        + Z * (8 * C2 * dz(s_expr) - 4 * dz(C2) * s_expr
               - 8 * dz(q) * E2 + 4 * q * dz(E2)
               + 8 * D1 * dz(E1) - 4 * dz(D1) * E1
               + 12 * D2 * dz(r))
    )
    return {name: sp.expand(value) for name, value in rows.items()}


def source_diffs() -> dict[str, sp.Expr]:
    st = structure()
    even, odd = even_odd(st)
    rows = residuals(st)
    images = {
        "O0": coeff(odd, A, 0),
        "O1": coeff(odd, A, 1),
        "O2": coeff(odd, A, 2),
        "E0": coeff(even, A, 0) - kappa,
        "EQ1_even": coeff(even, A, 1),
        "EQ2_even": coeff(even, A, 2),
        "EQ3_even": coeff(even, A, 3),
    }
    return {name: norm(images[name] - rows[name]) for name in rows}


def corrected_t1_t2_checks() -> dict[str, sp.Expr]:
    d = sp.Rational(3, 2) * a / b
    h = sp.Function("h")(Z)
    h0 = dz(Z * eta) * s

    def M(y: sp.Expr) -> sp.Expr:
        return 2 * Z * eta * dz(y) - eta * y - 4 * Z * dz(eta) * y

    def M2(y: sp.Expr) -> sp.Expr:
        return 2 * Z * eta * dz(y) - eta * y - 2 * Z * dz(eta) * y

    st_h = structure(d * h)
    st_h["C2"] = d * Z * eta * s
    o2_h = residuals(st_h)["O2"]
    t1_rhs = -6 * a * eta * M2(h - h0) + 3 * a * M(s * G) / b

    st_live = structure(d * (dz(Z * eta) * s + s * G / (2 * b * eta)))
    st_live["C2"] = d * Z * eta * s
    eq3 = residuals(st_live)["EQ3_even"]
    Xi = (
        12 * a * b * eta**3 * dz(eta) * (dz(eta) + 2 * Z * dz(eta, 2))
        + 4 * d * s * (eta * dz(s) - dz(eta) * s)
        + 8 * b * eta * (q * dz(eta) - dz(q) * eta)
        + 12 * a * eta**3 * dz(r)
        + 12 * a * eta * ((eta * dz(eta, 2) - dz(eta)**2) * G
                          + eta * dz(eta) * dz(G))
    )
    corrected_bracket = eta * G**2 + 2 * Z * dz(eta) * G**2 - 2 * Z * eta * G * dz(G)
    t2_rhs = Z**2 * Xi - 3 * a * corrected_bracket / b

    rows = residuals(structure())
    E2 = structure()["E2"]
    o1s = (
        8 * s * structure()["C2"] * dz(r) - 8 * E2 * (q * dz(r) - kappa / 2)
        + 4 * s * (C1 * dz(structure()["E1"]) - dz(C1) * structure()["E1"])
        + 6 * structure()["D1"] * s * dz(s) - 2 * dz(structure()["D1"]) * s**2
        + 4 * Z * s * (q * dz(s) - dz(q) * s)
    )
    W = q * dz(s) - dz(q) * s
    T = (
        -(C1 * dz(structure()["E1"]) - dz(C1) * structure()["E1"]) / 2
        - sp.Rational(3, 4) * structure()["D1"] * dz(s)
        + dz(structure()["D1"]) * s / 4 - Z * W / 2
    )
    det_eo = (
        (s * C1 - q * structure()["E1"]) * T
        + W * (s * structure()["C2"] - q * E2) / 2
        + kappa * (structure()["E1"] * structure()["C2"] - C1 * E2) / 2
    )
    R0 = q * dz(r) - s * dz(p) - kappa / 2
    R1 = C1 * dz(r) - structure()["E1"] * dz(p) + W / 2
    R2 = structure()["C2"] * dz(r) - E2 * dz(p) - T
    det_from_residuals = -sp.det(sp.Matrix([
        [q, -s, R0],
        [C1, -structure()["E1"], R1],
        [structure()["C2"], -E2, R2],
    ]))
    return {
        "T1_factorization": norm(o2_h - t1_rhs),
        "T2_corrected": norm(eq3 - t2_rhs),
        "O1s_identity": norm(o1s - (s * rows["O1"] - 4 * E2 * rows["E0"])),
        "DET_EO_syzygy": norm(det_eo - det_from_residuals),
    }


def dev_rows_symbolic() -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Return clearings F1,F2,F3 of EQ1_even/EQ2_even/EQ3_even."""
    X = sp.Function("X")(Z)
    Y = sp.Function("Y")(Z)

    def N(w: sp.Expr) -> sp.Expr:
        return eta * dz(w) - 2 * w * dz(eta)

    E1 = dz(b * Z * eta**2) + G
    V = (
        2 * Z * b * eta**2 * dz(eta, 2) - 2 * Z * b * eta * dz(eta)**2
        + 2 * b * eta**2 * dz(eta) - 2 * G * dz(eta) + eta * dz(G)
    )
    F1 = (
        8 * Z * b**2 * kappa * eta**2
        + 3 * a * (3 * E1 - b * eta**2) * N(X)
        - 4 * E1 * N(Y) + 2 * V * Y
    )

    AX = 3 * a * Z * (4 * Z * b * eta * dz(eta) + 3 * b * eta**2 + 2 * G)
    AY = -2 * Z * (2 * Z * b * eta * dz(eta) + 3 * b * eta**2 + G)
    W2 = (
        4 * Z**2 * b * eta**2 * dz(eta, 2) + 2 * Z * b * eta**2 * dz(eta)
        - 2 * Z * G * dz(eta) + 2 * Z * eta * dz(G) - G * eta
    )
    Psi2 = 6 * a * b * eta**2 * (
        4 * Z**2 * b**2 * eta**3 * dz(eta) * dz(eta, 2)
        - 4 * Z**2 * b**2 * eta**2 * dz(eta)**3
        + 4 * Z * b**2 * eta**3 * dz(eta)**2
        + 2 * Z * b * G * eta**2 * dz(eta, 2)
        - 6 * Z * b * G * eta * dz(eta)**2
        + 2 * Z * b * eta**2 * dz(G) * dz(eta)
        + 2 * b * G * eta**2 * dz(eta)
        - 2 * G**2 * dz(eta) + G * eta * dz(G)
    )
    F2 = AX * N(X) + AY * N(Y) + W2 * Y + Psi2

    Xi0 = (
        12 * a * b * eta**3 * dz(eta) * (dz(eta) + 2 * Z * dz(eta, 2))
        + 12 * a * eta * ((eta * dz(eta, 2) - dz(eta)**2) * G
                          + eta * dz(eta) * dz(G))
    )
    bracket = eta * G**2 + 2 * Z * dz(eta) * G**2 - 2 * Z * eta * G * dz(G)
    F3 = b * Z**2 * Xi0 + Z**2 * (3 * a * N(X) - 2 * N(Y)) - 3 * a * bracket
    return tuple(sp.expand(f) for f in (F1, F2, F3))


def dev_free_checks() -> dict[str, sp.Expr]:
    X = sp.Function("X")(Z)
    Y = sp.Function("Y")(Z)
    d = sp.Rational(3, 2) * a / b
    c1_live = d * (dz(Z * eta) * s + s * G / (2 * b * eta))
    st = structure(c1_live)
    st["C2"] = d * Z * eta * s
    rows = residuals(st)
    rdev = (s**2 + X) / (4 * b * eta**2)
    qdev = (3 * a * s**2 + Y) / (4 * b**2 * eta)
    replacements = {r: rdev, q: qdev}
    eq1_mod = (
        6 * st["D1"] * dz(r) - 4 * dz(q) * st["E1"] + 2 * q * dz(st["E1"])
        + 4 * st["C1"] * dz(s) - 2 * dz(st["C1"]) * s + 2 * kappa * Z
    ).subs(replacements).doit()
    eq2_dev = rows["EQ2_even"].subs(replacements).doit()
    eq3_dev = rows["EQ3_even"].subs(replacements).doit()
    F1, F2, F3 = dev_rows_symbolic()
    return {
        "F1_equals_4b2eta2_EQ1_even": norm(F1 - 4 * b**2 * eta**2 * eq1_mod),
        "F2_equals_2b2eta2_EQ2_even": norm(F2 - 2 * b**2 * eta**2 * eq2_dev),
        "F3_equals_b_EQ3_even": norm(F3 - b * eq3_dev),
    }


def planted_control() -> dict[str, Any]:
    # Raw EO source-identity control after dropping the live kappa != 0 open.
    plant = {
        "a": sp.Integer(1), "b": sp.Integer(1), "eta": Z,
        "s": Z, "p": sp.Integer(0), "C1": sp.Rational(3, 2) * Z**2,
        "q": sp.Rational(3, 4) * Z, "r": sp.Rational(1, 4), "G": -2 * Z**2,
        "c5": sp.Integer(0), "kappa": sp.Integer(0),
    }
    aa, bb = plant["a"], plant["b"]
    et, ss, gg = plant["eta"], plant["s"], plant["G"]
    st = {
        "C1": plant["C1"],
        "C2": Z * et * (3 * aa * ss + plant["c5"] * et) / (2 * bb),
        "E2": bb * Z * et**2,
        "D2": aa * Z * et**3,
    }
    st["E1"] = dz(st["E2"]) + gg
    st["D1"] = dz(st["D2"]) + sp.Rational(3, 2) * aa * et * gg / bb

    global p, q, r, s
    saved = (p, q, r, s)
    try:
        p, q, r, s = plant["p"], plant["q"], plant["r"], plant["s"]
        even, odd = even_odd(st, s_expr=plant["s"])
    finally:
        p, q, r, s = saved
    Xp = sp.expand(4 * plant["b"] * plant["eta"]**2 * plant["r"] - plant["s"]**2)
    Yp = sp.expand(4 * plant["b"]**2 * plant["eta"] * plant["q"]
                   - 3 * plant["a"] * plant["s"]**2)

    def exact_division(dividend: sp.Expr, divisor: sp.Expr) -> dict[str, Any]:
        quotient, remainder = sp.div(
            sp.Poly(sp.expand(dividend), Z, domain=sp.QQ),
            sp.Poly(sp.expand(divisor), Z, domain=sp.QQ),
        )
        return {"holds": remainder.is_zero, "quotient": str(quotient.as_expr()),
                "remainder": str(remainder.as_expr())}

    return {
        "assignment": {key: str(value) for key, value in plant.items()},
        "Even": str(norm(even)), "Odd": str(norm(odd)),
        "divisibilities": {
            "eta2_divides_s2_plus_X": exact_division(
                plant["s"]**2 + Xp, plant["eta"]**2),
            "eta_divides_3as2_plus_Y": exact_division(
                3 * plant["a"] * plant["s"]**2 + Yp, plant["eta"]),
            "s_divides_qrprime_minus_kappa_over_2": exact_division(
                plant["q"] * dz(plant["r"]) - plant["kappa"] / 2, plant["s"]),
        },
        "artifact": "SUBSYSTEM_POINT", "attainment": "NECESSARY",
    }


@dataclass(frozen=True)
class DevBox:
    e: int
    branch: str
    variables: tuple[sp.Symbol, ...]
    equations: tuple[sp.Expr, ...]
    row_degrees: tuple[int, int, int]
    licensed_cap: bool
    specialization: str


def polynomial_coefficients(expr: sp.Expr) -> list[sp.Expr]:
    poly = sp.Poly(sp.expand(expr), Z, domain="EX")
    if poly.is_zero:
        return []
    return [sp.expand(poly.nth(j)) for j in range(poly.degree() + 1)
            if poly.nth(j) != 0]


def make_devbox(e: int, branch: str = "main") -> DevBox:
    if e < 1:
        raise ValueError("DEV-PROJECTION is declared only for e >= 1")
    eta_cs = sp.symbols(f"eta0:{e}")
    g_cs = sp.symbols(f"G0:{2 * e}")
    x_cs = sp.symbols(f"X0:{4 * e}")
    y_cs = sp.symbols(f"Y0:{4 * e}")
    kap, tt, c = sp.symbols("kappa tt c")
    eta_p = sum(eta_cs[j] * Z**j for j in range(e)) + Z**e
    c_value: sp.Expr | None
    if branch == "main":
        c_value = None
        specialization = "Chamber II: c free, c*kappa*(c+2e) != 0"
        licensed = True
    elif branch == "c0":
        c_value = sp.Integer(0)
        specialization = "Chamber III specialization c=0"
        licensed = True
    elif branch == "cminus2e":
        c_value = sp.Integer(-2 * e)
        specialization = "exception c=-2e; capped probe only"
        licensed = False
    elif branch == "cminus2e1":
        c_value = sp.Integer(-(2 * e + 1))
        specialization = "separate c=-(2e+1) stratum"
        licensed = True
    elif branch == "walla":
        c_value = -sp.Rational(2, 3) * (1 + 3 * e)
        specialization = "separate Wall A: 3c+6e+2=0"
        licensed = True
    else:
        raise ValueError(f"unknown branch {branch!r}")
    c_top = c if c_value is None else c_value
    G_p = sum(g_cs[j] * Z**j for j in range(2 * e)) + c_top * Z**(2 * e)
    X_p = sum(x_cs[j] * Z**j for j in range(4 * e))
    Y_p = sum(y_cs[j] * Z**j for j in range(4 * e))

    F = dev_rows_symbolic()
    Xf, Yf = sp.Function("X")(Z), sp.Function("Y")(Z)
    subs = {a: 1, b: 1, eta: eta_p, G: G_p, Xf: X_p, Yf: Y_p, kappa: kap}
    rows = tuple(sp.expand(f.subs(subs).doit()) for f in F)
    equations: list[sp.Expr] = []
    for row in rows:
        equations.extend(polynomial_coefficients(row))
    if branch == "main":
        equations.append(sp.expand(kap * c * (c + 2 * e) * tt - 1))
        variables = tuple(eta_cs + g_cs + x_cs + y_cs + (kap, tt, c))
    else:
        equations.append(sp.expand(kap * tt - 1))
        variables = tuple(eta_cs + g_cs + x_cs + y_cs + (kap, tt))
    return DevBox(
        e=e, branch=branch, variables=variables, equations=tuple(equations),
        row_degrees=tuple(sp.Poly(row, Z).degree() for row in rows),
        licensed_cap=licensed, specialization=specialization,
    )


def msolve_string(box: DevBox) -> str:
    return emit_msolve_system(box.variables, box.equations)


def emit_msolve_system(
    variables: tuple[sp.Symbol, ...], equations: tuple[sp.Expr, ...]
) -> str:
    try:
        from msolveio import emit_system
    except ImportError as exc:
        raise RuntimeError("msolve format requires msolveio==0.2.1") from exc
    # msolveio deliberately rejects divisions inside a term.  Clear the
    # rational content of each generator first; over QQ this preserves its
    # zero set and keeps every coefficient literal parser-safe.
    polys = []
    for generator in equations:
        poly = sp.Poly(generator, *variables, domain=sp.QQ)
        _, integral = poly.clear_denoms(convert=True)
        polys.append(sp.sstr(sp.expand(integral.as_expr())).replace("**", "^"))
    return emit_system(polys, variables=[str(v) for v in variables], characteristic=0)


def optional_msolve_metadata(
    variables: tuple[sp.Symbol, ...], equations: tuple[sp.Expr, ...]
) -> dict[str, str | None]:
    """Return payload custody when msolveio is present without breaking JSON."""
    try:
        payload = emit_msolve_system(variables, equations)
    except RuntimeError as exc:
        if not isinstance(exc.__cause__, ImportError):
            raise
        return {
            "msolve_sha256": None,
            "msolve_adapter": "unavailable; install msolveio==0.2.1 for payload emission",
        }
    return {
        "msolve_sha256": hashlib.sha256(payload.encode()).hexdigest(),
        "msolve_adapter": "msolveio==0.2.1",
    }


def make_t4_ideal(stratum: str) -> tuple[tuple[sp.Symbol, ...], tuple[sp.Expr, ...]]:
    gamma, K, tt = sp.symbols("gamma K tt")
    if stratum == "g2":
        return (gamma, K, tt), (6 * K, gamma * K * tt - 1)
    if stratum != "g1":
        raise ValueError("T4 stratum must be g1 or g2")
    x1, y0, y1, u0, u1 = sp.symbols("x1 y0 y1 u0 u1")
    variables = (gamma, K, x1, y0, y1, u0, u1, tt)
    equations = (
        2 * x1 - 4 * y1 + gamma**2,
        2 * gamma * y0 - gamma**2,
        2 * gamma * y1 - gamma**3 + 4 * K,
        gamma * x1 - 2 * K,
        gamma**2 * u0**2,
        2 * gamma**4 * u0 * u1 + K * gamma**3 - 4 * K**2,
        gamma * K * tt - 1,
    )
    return variables, equations


def make_positive_control_ideal() -> tuple[tuple[sp.Symbol, ...], tuple[sp.Expr, ...]]:
    """A pinned nonempty control for the corrected e=0 s-free subsystem."""
    gamma, K, x0, x1, y0, y1, tt = sp.symbols("gamma K x0 x1 y0 y1 tt")
    gg = gamma * Z
    xx = x0 + x1 * Z
    yy = y0 + y1 * Z
    ii = dz(xx) - 2 * dz(yy)
    F1 = 2 * ii + 3 * gg * dz(xx) - 4 * gg * dz(yy) + 2 * yy * dz(gg) + 2 * K * Z
    F2 = (3 * Z * ii + 2 * Z * gg * dz(xx) - 2 * Z * gg * dz(yy)
          + (2 * Z * dz(gg) - gg) * yy + gg * dz(gg))
    F3 = 2 * Z**2 * ii - gg**2 + 2 * Z * gg * dz(gg)
    equations: list[sp.Expr] = []
    for row in (F1, F2, F3):
        equations.extend(polynomial_coefficients(row))
    equations.extend((
        gamma * K * tt - 1,
        gamma - 1, 12 * K - 1, x0 - 7, 6 * x1 - 1,
        2 * y0 - 1, 3 * y1 - 1, tt - 12,
    ))
    return (gamma, K, x0, x1, y0, y1, tt), tuple(sp.expand(g) for g in equations)


def system_record() -> dict[str, Any]:
    st = structure()
    even, odd = even_odd(st)
    rows = residuals(st)
    source = {
        "O0": coeff(odd, A, 0), "O1": coeff(odd, A, 1),
        "O2": coeff(odd, A, 2), "E0": coeff(even, A, 0) - kappa,
        "EQ1_even": coeff(even, A, 1), "EQ2_even": coeff(even, A, 2),
        "EQ3_even": coeff(even, A, 3),
    }
    return {
        "coefficient_field": "QQ(a,b,c5,kappa)",
        "derivative": "d/dZ",
        "coefficient_polynomials": {name: sp.sstr(value) for name, value in st.items()},
        "source_to_residual": [
            {"name": name, "source": sp.sstr(source[name]),
             "residual": sp.sstr(rows[name]),
             "exact_diff": sp.sstr(norm(source[name] - rows[name]))}
            for name in rows
        ],
    }


def run_checks() -> dict[str, Any]:
    st = structure()
    even, odd = even_odd(st)
    rows = residuals(st)
    diffs = source_diffs()
    other = corrected_t1_t2_checks()
    dev = dev_free_checks()
    whole_odd = norm(odd - rows["O0"] - A * rows["O1"] - A**2 * rows["O2"])
    whole_even = norm(
        even - kappa - rows["E0"] - A * rows["EQ1_even"]
        - A**2 * rows["EQ2_even"] - A**3 * rows["EQ3_even"]
    )
    old_eq2 = rows["EQ2_even"] + 2 * q * st["E1"]
    canary = norm(coeff(even, A, 2) - old_eq2)
    checks = {**diffs, **other, **dev,
              "whole_Odd": whole_odd, "whole_Even": whole_even,
              "A3_Odd": coeff(odd, A, 3), "A4_Even": coeff(even, A, 4),
              "A5_Even": coeff(even, A, 5)}
    failures = {key: value for key, value in checks.items() if norm(value) != 0}
    expected_canary = norm(canary + 2 * q * st["E1"])
    if expected_canary != 0 or canary == 0:
        failures["old_EQ2_even_canary"] = canary
    planted = planted_control()
    if planted["Even"] != "0" or planted["Odd"] != "0":
        failures["planted_control"] = planted
    failed_divisions = {
        name: record for name, record in planted["divisibilities"].items()
        if not record["holds"]
    }
    if failed_divisions:
        failures["planted_divisibilities"] = failed_divisions
    t4_bases: dict[str, list[str]] = {}
    for stratum in ("g1", "g2"):
        variables, equations = make_t4_ideal(stratum)
        basis = sp.groebner(equations, *variables, order="grevlex", domain=sp.QQ)
        t4_bases[stratum] = [str(poly.as_expr()) for poly in basis.polys]
        if t4_bases[stratum] != ["1"]:
            failures[f"T4_{stratum}_unit"] = t4_bases[stratum]
    control_variables, control_equations = make_positive_control_ideal()
    control_point = {
        str(name): value for name, value in zip(
            control_variables,
            (1, sp.Rational(1, 12), 7, sp.Rational(1, 6),
             sp.Rational(1, 2), sp.Rational(1, 3), 12),
        )
    }
    control_remainders = [
        norm(g.subs({v: control_point[str(v)] for v in control_variables}))
        for g in control_equations
    ]
    if any(value != 0 for value in control_remainders):
        failures["positive_control_ideal"] = control_remainders
    control_basis = sp.groebner(
        control_equations, *control_variables, order="grevlex", domain=sp.QQ
    )
    if len(control_basis.polys) == 1 and control_basis.polys[0].as_expr() == 1:
        failures["positive_control_nonunit"] = "unexpected unit ideal"
    return {
        "status": "PASS" if not failures else "FAIL",
        "zero_checks": sorted(checks),
        "old_EQ2_even_actual_minus_old": sp.sstr(canary),
        "planted_control": planted,
        "T4_finite_bases": t4_bases,
        "solver_positive_control": {
            "point": {key: str(value) for key, value in control_point.items()},
            "all_generator_values_zero": all(value == 0 for value in control_remainders),
            "sympy_unit_ideal": (len(control_basis.polys) == 1
                                  and control_basis.polys[0].as_expr() == 1),
            "artifact": "SUBSYSTEM_POINT", "attainment": "NECESSARY",
        },
        "failures": {key: str(value) for key, value in failures.items()},
        "sympy": sp.__version__,
    }


def dump_json(value: Any) -> None:
    print(json.dumps(value, sort_keys=True, indent=2))


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check")
    ps = sub.add_parser("system")
    ps.add_argument("--format", choices=("json", "text"), default="json")
    pd = sub.add_parser("devbox")
    pd.add_argument("e", type=int)
    pd.add_argument(
        "--branch",
        choices=("main", "c0", "cminus2e", "cminus2e1", "walla"),
        default="main",
    )
    pd.add_argument("--format", choices=("json", "msolve"), default="json")
    pt = sub.add_parser("t4ideal")
    pt.add_argument("stratum", choices=("g1", "g2"))
    pt.add_argument("--format", choices=("json", "msolve"), default="json")
    pc = sub.add_parser("control")
    pc.add_argument("--format", choices=("json", "msolve"), default="json")
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.command == "check":
        result = run_checks()
        dump_json(result)
        return 0 if result["status"] == "PASS" else 1
    if args.command == "system":
        record = system_record()
        if args.format == "json":
            dump_json(record)
        else:
            for row in record["source_to_residual"]:
                print(f"{row['name']}: {row['residual']} = 0")
        return 0

    if args.command == "t4ideal":
        variables, equations = make_t4_ideal(args.stratum)
        if args.format == "msolve":
            payload = emit_msolve_system(variables, equations)
            print(payload, end="")
        else:
            record = {
                "stratum": args.stratum,
                "coefficient_field": "QQ",
                "variables": [str(v) for v in variables],
                "equations": [str(g) for g in equations],
                "rabinowitsch": str(equations[-1]),
            }
            record.update(optional_msolve_metadata(variables, equations))
            dump_json(record)
        return 0

    if args.command == "control":
        variables, equations = make_positive_control_ideal()
        if args.format == "msolve":
            payload = emit_msolve_system(variables, equations)
            print(payload, end="")
        else:
            record = {
                "kind": "corrected_s_free_shifted_positive_control",
                "variables": [str(v) for v in variables],
                "equations": [str(g) for g in equations],
                "point": {"gamma": "1", "K": "1/12", "x0": "7",
                          "x1": "1/6", "y0": "1/2", "y1": "1/3", "tt": "12"},
                "artifact": "SUBSYSTEM_POINT", "attainment": "NECESSARY",
            }
            record.update(optional_msolve_metadata(variables, equations))
            dump_json(record)
        return 0

    box = make_devbox(args.e, args.branch)
    if args.format == "msolve":
        print(msolve_string(box), end="")
    else:
        record = {
            "e": box.e, "branch": box.branch,
            "coefficient_field": "QQ",
            "order": ("two blocks: all non-c variables first; c last"
                      if box.branch == "main"
                      else "single grevlex block; c is specialized and absent"),
            "variables": [str(v) for v in box.variables],
            "generator_count": len(box.equations), "row_degrees": box.row_degrees,
            "licensed_cap": box.licensed_cap, "specialization": box.specialization,
            "rabinowitsch": str(box.equations[-1]),
            "equations": [str(g) for g in box.equations],
        }
        record.update(optional_msolve_metadata(box.variables, box.equations))
        dump_json(record)
    return 0


if __name__ == "__main__":
    sys.exit(main())
