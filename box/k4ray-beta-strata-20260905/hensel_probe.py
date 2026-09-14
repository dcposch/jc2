#!/usr/bin/env python3
"""Probe: do DIV-band pivot matrices stay in Q when the LEVEL-4 top is 2-scalar?

Specializations:
  pin=q1 : q0=0, q1=1  (complete cover of q0=0 after G_m)
  pin=q0 : q0=1, q1 free-or-zero

A nonconstant pivot in q1 means the 17(bbbbbb) Hensel RREF does not transfer
to the generic q0-chart without working over Q(q1).
"""
from __future__ import annotations

from fractions import Fraction
from math import ceil
import json
from pathlib import Path
import sys

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))


def monomials(total_max: int) -> list[tuple[int, int]]:
    if total_max < 0:
        return []
    return [(i, j) for j in range(total_max + 1) for i in range(total_max - j + 1)]


def product_coefficient(left, right, ti, tj, subs):
    result = sp.Integer(0)
    for (i, j), coefficient in left.items():
        other = right.get((ti - i, tj - j))
        if other is None:
            continue
        if isinstance(coefficient, sp.Symbol):
            coefficient = subs.get(coefficient, coefficient)
        if isinstance(other, sp.Symbol):
            other = subs.get(other, other)
        result += coefficient * other
    return sp.expand(result)


def smin_of(K: int) -> int:
    return ceil(2 * (K - 1) / 3)


def probe(K: int, b: int, mode: str, max_bands: int = 4) -> dict:
    smin = smin_of(K)
    d = b - smin - 1
    rdeg = 3 * b - 2 * K
    x, y = sp.symbols("x y")
    q1 = sp.Symbol("q1")

    if mode == "q1":
        # P = y^{smin}(y-x) * y * x^{d-1} = y^{smin+1}(y-x) x^{d-1}
        Q = (x ** (d - 1) * y) if d >= 1 else sp.Integer(1)
        q1_free = False
    elif mode == "q0_q1zero":
        Q = x**d if d >= 0 else sp.Integer(1)
        q1_free = False
    elif mode == "q0_generic":
        Q = x**d + q1 * x ** (d - 1) * y if d >= 1 else sp.Integer(1)
        q1_free = True
    else:
        raise ValueError(mode)

    P = sp.expand(y**smin * (y - x) * Q)
    Hpoly = sp.expand(y ** (K - 1) * (y - x))
    Btop = sp.expand(2 * P)
    Atop = sp.expand(sp.Poly(P**2, x, y).as_expr() * 4 / Hpoly)
    Atop = sp.expand(sp.div(sp.Poly(4 * P**2, x, y), sp.Poly(Hpoly, x, y))[0].as_expr())
    Rtop = sp.expand(sp.div(sp.Poly(4 * P**3, x, y), sp.Poly(Hpoly**2, x, y))[0].as_expr() / 3)

    def terms_of(expr: sp.Expr) -> dict[tuple[int, int], sp.Expr]:
        out: dict[tuple[int, int], sp.Expr] = {}
        for (i, j), c in sp.Poly(sp.expand(expr), x, y).terms():
            out[(int(i), int(j))] = sp.expand(c)
        return out

    h_terms = terms_of(Hpoly)
    B_terms = terms_of(Btop)
    A_terms = terms_of(Atop)

    symbols_by_kind_degree: dict[tuple[str, int], list[sp.Symbol]] = {}
    all_symbols: list[sp.Symbol] = []

    def add_lower(kind: str, maximum: int, bucket: dict) -> None:
        for i, j in monomials(maximum):
            if kind == "h" and (i, j) == (0, K - 1):
                continue
            if (i, j) in bucket and not isinstance(bucket[(i, j)], sp.Symbol):
                continue
            symbol = sp.Symbol(f"{kind}_{i}_{j}")
            bucket[(i, j)] = symbol
            symbols_by_kind_degree.setdefault((kind, i + j), []).append(symbol)
            all_symbols.append(symbol)

    add_lower("h", K - 1, h_terms)
    add_lower("B", b - 1, B_terms)
    add_lower("A", max(2 * b - K - 1, -1), A_terms)

    def target_r(i: int, j: int) -> sp.Expr:
        poly = sp.Poly(Rtop, x, y)
        return sp.expand(poly.coeff_monomial(x**i * y**j)) if poly.total_degree() >= 0 else sp.Integer(0)

    substitutions: dict[sp.Symbol, sp.Expr] = {}
    audit = []
    start_deg = 2 * b - 1
    bands_done = 0
    for degree in range(start_deg, rdeg - 1, -1):
        if bands_done >= max_bands:
            break
        new_variables: list[sp.Symbol] = []
        # A_top has degree 2b-K, H degree K, so A_new at degree D-K; h_new at D-(2b-K)
        for kind, component_degree in (
            ("h", degree - (2 * b - K)),
            ("A", degree - K),
            ("B", degree - b),
        ):
            new_variables.extend(symbols_by_kind_degree.get((kind, component_degree), []))
        new_variables = [v for v in new_variables if v not in substitutions]

        equations = []
        for i in range(degree + 1):
            j = degree - i
            rforce = target_r(i, j) if degree == rdeg else (sp.Integer(0) if degree > rdeg else None)
            if rforce is None:
                continue
            eq = (
                product_coefficient(B_terms, B_terms, i, j, substitutions)
                - product_coefficient(A_terms, h_terms, i, j, substitutions)
                - rforce
            )
            equations.append(sp.expand(eq))

        zero_new = {v: sp.Integer(0) for v in new_variables}
        n_nonconst = 0
        n_q1dep = 0
        ranks_over_Q = 0
        for equation in equations:
            coeffs = [sp.expand(equation).coeff(v) for v in new_variables]
            if any(c.free_symbols for c in coeffs):
                n_nonconst += 1
                if any(q1 in c.free_symbols for c in coeffs):
                    n_q1dep += 1
            rest = sp.expand(equation.xreplace(zero_new))
            reconstructed = sp.expand(rest + sum((c * v for c, v in zip(coeffs, new_variables)), sp.Integer(0)))
            linear = sp.expand(equation - reconstructed) == 0
            if not linear:
                audit.append({"degree": degree, "error": "nonlinear"})
                return {"K": K, "b": b, "mode": mode, "audit": audit, "status": "NONLINEAR"}
        # constant-matrix rank over Q, ignoring q1-dependent columns
        const_cols = []
        for vi, v in enumerate(new_variables):
            col_ok = True
            for equation in equations:
                c = sp.expand(equation).coeff(v)
                if c.free_symbols:
                    col_ok = False
                    break
            if col_ok:
                const_cols.append(vi)
        audit.append(
            {
                "degree": degree,
                "n_eq": len(equations),
                "n_new": len(new_variables),
                "n_nonconst_rows": n_nonconst,
                "n_q1dep_rows": n_q1dep,
                "n_const_cols": len(const_cols),
                "new": [str(v) for v in new_variables],
            }
        )
        bands_done += 1
        # do not substitute if any nonconst; just report
        if n_nonconst:
            continue
        # constant RREF substitution skipped in the probe; we only classify
    return {
        "K": K,
        "b": b,
        "mode": mode,
        "smin": smin,
        "d": d,
        "rdeg": rdeg,
        "q1_free": q1_free,
        "Rtop_deg": int(sp.Poly(Rtop, x, y).total_degree()),
        "Atop_deg": int(sp.Poly(Atop, x, y).total_degree()),
        "audit": audit,
        "status": "OK",
    }


def main() -> None:
    out = []
    for K, b in ((7, 6), (8, 7), (9, 8)):
        for mode in ("q1", "q0_q1zero", "q0_generic"):
            info = probe(K, b, mode, max_bands=5)
            out.append(info)
            print(
                json.dumps(
                    {
                        "K": info["K"],
                        "b": info["b"],
                        "mode": info["mode"],
                        "status": info["status"],
                        "bands": [
                            {
                                "d": a["degree"],
                                "eq": a.get("n_eq"),
                                "new": a.get("n_new"),
                                "nonconst": a.get("n_nonconst_rows"),
                                "q1dep": a.get("n_q1dep_rows"),
                                "const_cols": a.get("n_const_cols"),
                            }
                            for a in info.get("audit", [])
                        ],
                    },
                    sort_keys=True,
                )
            )
    (HERE / "hensel-probe.json").write_text(json.dumps(out, indent=2, default=str) + "\n")


if __name__ == "__main__":
    main()
