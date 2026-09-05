#!/usr/bin/env python3
"""Leading F/G pole-row target: emit coefficient minus the forced face.

Cone-vertex gate §6–§7 / rekill §7 (2026-09-05): raw_minor_support lists the
top pole tag (D=108: F n=96 / G n=64; (99,66) δ=2: 81/54; δ=5/2: 189/126)
and the engines emitted it as a homogeneous ``= 0`` row. That row is
unsatisfiable on the whole chart (it reduces to ``1 = 0``, the top
coefficient of the forced face). The corrected emission is
``coefficient − target``. Every strictly-lower local power is unchanged.

Canonical copies of these functions live in the three engines (and the
frozen g108 ``band_engine.py``) so a driver that imports an engine does not
depend on this path. Keep the copies byte-sync'd with this file's
``d108_*`` / ``g9966_*`` pair.
"""
from __future__ import annotations

from functools import lru_cache

import sympy as sp


def _coeffs(expr, var) -> dict[int, sp.Expr]:
    poly = sp.Poly(sp.expand(expr), var)
    return {int(mon[0]): sp.expand(cf) for mon, cf in poly.terms()}


# ---- D=108 δ=3: p = π²−c; F subtracts p^12 at 96, G subtracts p^8 at 64.

def d108_lead_n(name: str) -> int:
    if name == "F":
        return 96
    if name == "G":
        return 64
    raise ValueError(name)


@lru_cache(maxsize=None)
def d108_target_table(name: str) -> dict[int, sp.Expr]:
    """Coefficients of p^12 (F) or p^8 (G) in π. Rekill §7 / gate §6."""
    pi, c = sp.symbols("pi c")
    p = pi**2 - c
    return _coeffs(p ** (12 if name == "F" else 8), pi)


def d108_pole_coeff(table, n, k, name):
    value = table.get((n, k), sp.Integer(0))
    if n != d108_lead_n(name):
        return value
    return sp.expand(value - d108_target_table(name).get(k, 0))


# ---- (99,66): K3-lead^9 (F) / K3-lead^6 (G). Gate §6 cubes the K3 lead
# to get a_P, then F = a_P^3, G = a_P^2.

def g9966_lead_n(branch: str, name: str) -> int:
    if branch == "delta2":
        return 81 if name == "F" else 54
    if branch == "delta52":
        return 189 if name == "F" else 126
    raise ValueError(branch)


@lru_cache(maxsize=None)
def g9966_target_table(branch: str, name: str) -> dict[int, sp.Expr]:
    exp = 9 if name == "F" else 6
    if branch == "delta2":
        zeta, rho = sp.symbols("zeta rho")
        face = zeta**2 * (zeta + 3 * rho)  # K3 lead at t^9
        return _coeffs(face**exp, zeta)
    if branch == "delta52":
        pi, c = sp.symbols("pi c")
        face = pi * (pi**2 - c)  # K3 lead at τ^21
        return _coeffs(face**exp, pi)
    raise ValueError(branch)


def g9966_pole_coeff(table, n, k, branch, name):
    value = table.get((n, k), sp.Integer(0))
    if n != g9966_lead_n(branch, name):
        return value
    return sp.expand(value - g9966_target_table(branch, name).get(k, 0))
