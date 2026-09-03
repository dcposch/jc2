#!/usr/bin/env python3
"""Xu (99,66), delta=5/2: reduced ODE and bounded local lift.

This is not a full Keller-pair construction.  It mechanizes the part of Xu
Section 8 that is explicit, then prolongs the factored local equation

    D_s(Q,h) = -2*s^2*h^4,      s^2=t,

where h starts with p(pi)/s and Q starts with q1(pi).  The h-coefficient
supports are the monomial supports of a straightened degree-11 polynomial
h(x,y), evaluated at x=s^-2, y=pi*s^5, through the requested orders.
The Q-coefficients are capped polynomial unknowns; non-emptiness is therefore
a necessary/local counting result, not a full original-coordinate decision.
"""

from __future__ import annotations

import json
import pathlib
from dataclasses import dataclass
from typing import Any

import sympy as sp


HERE = pathlib.Path(__file__).resolve().parent
LANE = HERE.parent
RESULTS = LANE / "results"

s, pi, c = sp.symbols("s pi c")


def conv(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {str(k): conv(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [conv(v) for v in obj]
    if isinstance(obj, (sp.Basic,)):
        return str(sp.factor(obj))
    return obj


def jac_s(a: sp.Expr, b: sp.Expr) -> sp.Expr:
    return sp.diff(a, s) * sp.diff(b, pi) - sp.diff(a, pi) * sp.diff(b, s)


def p_poly() -> sp.Expr:
    return pi * (pi**2 - c)


def q1_poly() -> sp.Expr:
    p = p_poly()
    return sp.integrate(-2 * p**3, pi)


def reduced_ode_check() -> dict[str, Any]:
    p = p_poly()
    q1 = q1_poly()
    reduced = sp.factor(jac_s(q1, p / s) + 2 * s**2 * (p / s) ** 4)
    return {
        "p": p,
        "q1": sp.expand(q1),
        "degree_q1": sp.degree(q1, pi),
        "q1_prime_plus_2p3": sp.factor(sp.diff(q1, pi) + 2 * p**3),
        "Ds_check": reduced,
        "verdict": "PASS" if reduced == 0 else "FAIL",
    }


def wrapper_controls() -> dict[str, Any]:
    t = sp.Symbol("T")
    empty = sp.groebner([c, t * c - 1], c, t, order="lex")
    nonempty = sp.groebner([c - 1, t * c - 1], c, t, order="lex")
    empty_unit = any(g.as_expr() == 1 for g in empty.polys)
    nonempty_unit = any(g.as_expr() == 1 for g in nonempty.polys)
    return {
        "ring": "Q[c,T]",
        "empty_control_generators": ["c", "T*c-1"],
        "empty_control_unit": empty_unit,
        "nonempty_control_generators": ["c-1", "T*c-1"],
        "nonempty_control_unit": nonempty_unit,
        "verdict": "PASS" if empty_unit and not nonempty_unit else "FAIL",
    }


def delta_7_3_control() -> dict[str, Any]:
    """Xu's non-exception branch, checked for delta=7/3 after q=p^13(pi-d)."""
    d, k, rab = sp.symbols("d k T")
    p = p_poly()
    pp = sp.diff(p, pi)
    delta = sp.Rational(7, 3)
    a = -105 + 40 * delta
    b = -72 + 27 * delta
    q = p**13 * (pi - d)
    expr = sp.expand(9 * a * q * pp - b * p * sp.diff(q, pi) - k * p**14)
    reduced = sp.factor(expr / p**13)
    coeffs = sp.Poly(sp.expand(reduced), pi).all_coeffs()
    sat = sp.groebner(coeffs + [rab * c - 1], d, k, c, rab, order="lex")
    unit = any(g.as_expr() == 1 for g in sat.polys)
    return {
        "delta": "7/3",
        "a_T3_exponent": a,
        "b_g_exponent": b,
        "reduced_polynomial": reduced,
        "coefficient_equations": coeffs,
        "saturation": "c != 0 via T*c-1",
        "groebner_basis": [g.as_expr() for g in sat.polys],
        "verdict": "EXCLUDED" if unit else "NOT_EXCLUDED",
    }


def delta_2_three_root_control() -> dict[str, Any]:
    return {
        "delta": "2",
        "branch": "[1,1,1]",
        "equation": "2*p*q' - 25*p'*q = k*p^14",
        "reason": (
            "At each simple root of p, if q has multiplicity r then the "
            "left side has multiplicity r because 2*r-25 != 0 for integer r. "
            "The right side has multiplicity 14, so r=14 at all three roots."
        ),
        "degree_lower_bound": 42,
        "degree_q_from_Xu": 40,
        "saturation": "c != 0 makes p=pi*(pi^2-c) squarefree",
        "verdict": "EXCLUDED",
    }


def h_support(power: int) -> list[int]:
    """pi-powers in [s^power] h(s,pi) from deg<=11 monomials x^i y^j."""
    out: list[int] = []
    for j in range(12):
        num = 5 * j - power
        if num % 2:
            continue
        i = num // 2
        if i >= 0 and i + j <= 11:
            out.append(j)
    return out


def symbols(prefix: str, count: int) -> tuple[sp.Symbol, ...]:
    return tuple(sp.Symbol(f"{prefix}_{i}") for i in range(count))


def generated_symbols(expr: sp.Expr, prefixes: tuple[str, ...]) -> list[sp.Symbol]:
    return sorted(
        [
            v
            for v in expr.free_symbols
            if any(str(v).startswith(prefix) for prefix in prefixes)
        ],
        key=str,
    )


@dataclass
class LocalLift:
    max_order: int = 4
    q_degree_cap: int = 18

    def run(self) -> dict[str, Any]:
        p = p_poly()
        q1 = q1_poly()
        h_terms: dict[int, sp.Expr] = {-1: p}
        q_terms: dict[int, sp.Expr] = {0: q1}
        substitutions: dict[sp.Symbol, sp.Expr] = {}
        free_symbols: list[sp.Symbol] = []
        order_records: list[dict[str, Any]] = []

        # Pre-create all coefficients so names are deterministic.
        for order in range(-1, self.max_order + 1):
            hp = order + 1
            qp = order + 2
            if hp >= 0 and hp not in h_terms:
                h_terms[hp] = sp.Add(
                    *(
                        sp.Symbol(f"a{hp}_{j}") * pi**j
                        for j in h_support(hp)
                    )
                )
            if qp >= 1 and qp not in q_terms:
                bs = symbols(f"b{qp}", self.q_degree_cap + 1)
                q_terms[qp] = sp.Add(*(bs[j] * pi**j for j in range(len(bs))))

        for order in range(-1, self.max_order + 1):
            hp = order + 1
            qp = order + 2
            h = sp.Add(*(expr * s**r for r, expr in h_terms.items() if r <= hp))
            q = sp.Add(*(expr * s**r for r, expr in q_terms.items() if r <= qp))
            expr = sp.together(jac_s(q, h) + 2 * s**2 * h**4).expand()
            expr = sp.expand(expr.subs(substitutions))
            coeff = sp.Poly(sp.expand(expr.coeff(s, order)), pi)
            equations = [sp.expand(e) for e in coeff.all_coeffs() if e != 0]

            newvars: list[sp.Symbol] = []
            if hp >= 0:
                newvars.extend(generated_symbols(h_terms[hp], (f"a{hp}_",)))
            if qp >= 1:
                newvars.extend(generated_symbols(q_terms[qp], (f"b{qp}_",)))
            newvars = [v for v in newvars if v not in substitutions]

            solutions = sp.solve(
                equations, newvars, dict=True, simplify=False, rational=False
            )
            if not solutions:
                order_records.append(
                    {
                        "s_power": order,
                        "equations": len(equations),
                        "new_variables": [str(v) for v in newvars],
                        "verdict": "INCONSISTENT_OR_BRANCH_NEEDED",
                    }
                )
                return {
                    "verdict": "STOPPED",
                    "stop_order": order,
                    "orders": order_records,
                }

            sol = solutions[0]
            substitutions.update(sol)
            free_now = [v for v in newvars if v not in sol]
            free_symbols.extend(free_now)

            # Verify the just-solved coefficient.
            checked = sp.expand(coeff.as_expr().subs(sol))
            checked = sp.expand(checked.subs(substitutions))

            h_solution = {}
            if hp >= 0:
                h_solution = {
                    str(v): sp.factor(substitutions[v])
                    for v in generated_symbols(h_terms[hp], (f"a{hp}_",))
                    if v in substitutions
                }

            order_records.append(
                {
                    "s_power": order,
                    "pi_equations": len(equations),
                    "new_variable_count": len(newvars),
                    "solved_variable_count": len(sol),
                    "free_new_variables": [str(v) for v in free_now],
                    "h_support_pi_powers": h_support(hp) if hp >= 0 else [],
                    "h_solution": h_solution,
                    "coefficient_rechecks_to_zero": checked == 0,
                    "verdict": "CONSISTENT",
                }
            )

        free_set = sorted({v for v in free_symbols if v not in substitutions}, key=str)
        denom_factors = set()
        for value in substitutions.values():
            den = sp.factor(sp.denom(sp.together(value)))
            if den != 1:
                denom_factors.add(str(den))
        return {
            "equation": "D_s(Q,h)+2*s^2*h^4=0",
            "s_relation": "s^2=t",
            "h_leader": "p(pi)/s",
            "q_leader": "q1(pi)",
            "q_degree_cap_each_new_B": self.q_degree_cap,
            "h_support_rule": "x=s^-2, y=pi*s^5, deg h<=11, exponent=5*j-2*i",
            "orders": order_records,
            "free_parameters_excluding_c": [str(v) for v in free_set],
            "dimension_including_c_localized": len(free_set) + 1,
            "dimension_after_c_equals_1_slice": len(free_set),
            "localized_denominators_seen": sorted(denom_factors),
            "verdict": "CONSISTENT_THROUGH_s^%d" % self.max_order,
        }


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    data = {
        "reduced_ode": reduced_ode_check(),
        "wrapper_controls": wrapper_controls(),
        "controls": {
            "delta_2_three_simple_roots": delta_2_three_root_control(),
            "delta_7_3": delta_7_3_control(),
        },
        "local_lift": LocalLift(max_order=4, q_degree_cap=18).run(),
    }
    out = RESULTS / "xu52_reduced_lift.json"
    out.write_text(json.dumps(conv(data), indent=2, sort_keys=True) + "\n")
    print(json.dumps(conv(data), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
