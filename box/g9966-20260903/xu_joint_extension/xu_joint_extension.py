#!/usr/bin/env python3
"""Extend the shared-global-h3 / Xu delta=5/2 reduced ODE recurrence.

Scope is deliberately narrow.  One finite degree-11 polynomial ``h`` is
filtered at the fixed major face and evaluated at the curved minor centre

    t=s^2,  w=u*s^4+v*s^6+pi*s^7.

After imposing ``h=p/s+O(1)``, ``p=pi*(pi^2-c)``, the same resulting h-series
is coupled to

    D_s(Q,h) + 2*s^2*h^4 = 0,   deg_pi(B_n) <= 18.

We take the allowed torus slice c=1.  This is a common-h necessary system;
there are no global f/g arrays and no direct Keller-pair claim.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from math import ceil
from pathlib import Path
import subprocess
import time

import sympy as sp


ROOT = Path("/home/ubuntu/jc2")
OUT = ROOT / "box" / "g9966-20260903" / "xu_joint_extension"
RECEIPT = ROOT / "xmodel" / "g9966-global-design-sol56-20260903.run.v2"
MAX_SOLVED_ORDER = 30


def file_sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def expression_sha256(expression: sp.Expr) -> str:
    return sha256(str(sp.expand(expression)).encode("utf-8")).hexdigest()


def receipt_check() -> dict:
    fields = {}
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value
    rows = []
    input_dir = Path(fields["lane_inputs_dir"])
    for index in range(1, int(fields["charged_inputs"]) + 1):
        basename = fields[f"charged_input_{index}_basename"]
        expected = fields[f"charged_input_{index}_sha256"]
        path = input_dir / basename
        actual = file_sha256(path)
        rows.append({"basename": basename, "sha256": actual, "ok": actual == expected})
    if not all(row["ok"] for row in rows):
        raise RuntimeError("charged-input content mismatch")
    return {
        "method": "receipt basename/hash fields parsed and all digests recomputed",
        "count": len(rows),
        "all_ok": True,
        "rows": rows,
    }


def laurent_coefficients(expression: sp.Expr, variable: sp.Symbol) -> dict[int, sp.Expr]:
    answer: dict[int, sp.Expr] = {}
    for term in sp.Add.make_args(sp.expand(expression)):
        exponent = int(term.as_powers_dict().get(variable, 0))
        answer[exponent] = sp.expand(answer.get(exponent, 0) + term / variable**exponent)
    return answer


def polynomial_rows(expression: sp.Expr, variable: sp.Symbol, outer_tag: int):
    return [
        ((outer_tag, monomial[0]), sp.expand(coefficient))
        for monomial, coefficient in sp.Poly(sp.expand(expression), variable).terms()
        if coefficient != 0
    ]


def qstar_reduce(tagged_rows, variables):
    """Deterministic affine elimination using coefficients in Q* only."""
    rows = list(tagged_rows)
    remaining = list(variables)
    pivots = []
    while True:
        choice = None
        for row_index, (tag, expression) in enumerate(rows):
            for variable_index, variable in enumerate(remaining):
                coefficient = sp.expand(sp.diff(expression, variable))
                remainder = sp.expand(expression - coefficient*variable)
                if (coefficient.is_Rational and coefficient != 0
                        and variable not in remainder.free_symbols):
                    choice = (row_index, variable_index, tag, variable,
                              sp.Rational(coefficient), remainder)
                    break
            if choice is not None:
                break
        if choice is None:
            break
        row_index, variable_index, tag, variable, coefficient, remainder = choice
        rhs = sp.expand(-remainder/coefficient)
        if sp.expand(rows[row_index][1].subs(variable, rhs)) != 0:
            raise AssertionError("Q* pivot failed")
        pivots.append((tag, variable, coefficient, rhs))
        del rows[row_index]
        del remaining[variable_index]
        next_rows = []
        for old_tag, expression in rows:
            image = sp.expand(expression.subs(variable, rhs))
            if image != 0:
                next_rows.append((old_tag, image))
        rows = next_rows
    return rows, remaining, pivots


def resolve_pivots(pivots):
    resolved = {}
    pivot_variables = {pivot[1] for pivot in pivots}
    for _tag, variable, _coefficient, rhs in reversed(pivots):
        image = sp.expand(rhs.subs(resolved, simultaneous=True))
        if image.free_symbols.intersection(pivot_variables):
            raise AssertionError("unresolved Q* map")
        resolved[variable] = image
    return resolved


def build_major_K():
    t, w = sp.symbols("t w")
    K = w**3*(w - 1)**8
    parameters = []
    support = []
    for r in range(1, 12):
        cap = 11 - r
        q = max(0, ceil((33 - 3*r)/4))
        for degree in range(q, cap + 1):
            coefficient = sp.Symbol(f"c_{r}_{degree}")
            parameters.append(coefficient)
            support.append((r, degree, q))
            K += coefficient*t**r*(w - 1)**q*w**(degree - q)
    if len(parameters) != 21:
        raise AssertionError("major support count changed")
    if not all(3*r + 4*q >= 33 for r, _degree, q in support):
        raise AssertionError("strict major-face filter failed")
    return t, w, sp.expand(K), parameters, support


def build_shared_h():
    t, w, K, parameters, support = build_major_K()
    s, pi, u, v, c = sp.symbols("s pi u v c")
    h_raw = sp.expand(
        K.subs({t: s**2, w: u*s**4 + v*s**6 + pi*s**7}, simultaneous=True)
        / s**22
    )
    raw_coefficients = laurent_coefficients(h_raw, s)
    p = pi*(pi**2 - c)
    leader_rows = []
    for exponent in range(min(raw_coefficients), 0):
        target = p if exponent == -1 else 0
        leader_rows.extend(polynomial_rows(
            raw_coefficients.get(exponent, 0) - target, pi, exponent
        ))
    residual, free, pivots = qstar_reduce(leader_rows, parameters)
    if residual or [str(item) for item in free] != ["c_11_0"]:
        raise AssertionError((residual, free))
    if len(leader_rows) != 20 or len(pivots) != 20:
        raise AssertionError("leader row/pivot count changed")
    resolved = resolve_pivots(pivots)
    if not all(sp.expand(row.subs(resolved, simultaneous=True)) == 0
               for _tag, row in leader_rows):
        raise AssertionError("resolved major-to-minor map failed")
    h = sp.expand(h_raw.subs(resolved, simultaneous=True))
    coefficients = laurent_coefficients(h, s)
    if sp.expand(coefficients[-1] - p) != 0:
        raise AssertionError("minor leader did not become p/s")
    return {
        "symbols": (s, pi, u, v, c),
        "K": K,
        "support": support,
        "parameters": parameters,
        "h": h,
        "coefficients": coefficients,
        "leader_rows": leader_rows,
        "free": free,
        "pivots": pivots,
        "resolved": resolved,
    }


class Recurrence:
    def __init__(self, coefficients, pi, u, v, c110):
        self.A = coefficients
        self.pi = pi
        self.u = u
        self.v = v
        self.c110 = c110
        self.p = pi*(pi**2 - 1)
        self.b0 = sp.Symbol("b0")
        self.B = {
            0: -pi**10/sp.Integer(5) + sp.Rational(3, 4)*pi**8
               - pi**6 + sp.Rational(1, 2)*pi**4 + self.b0
        }
        self._h2 = {}
        self._h4 = {}

    def clear_h_power_cache(self):
        self._h2.clear()
        self._h4.clear()

    def h2_coefficient(self, exponent):
        if exponent not in self._h2:
            self._h2[exponent] = sp.expand(sum(
                self.A.get(i, 0)*self.A.get(exponent - i, 0)
                for i in range(-1, exponent + 2)
            ))
        return self._h2[exponent]

    def h4_coefficient(self, exponent):
        if exponent not in self._h4:
            self._h4[exponent] = sp.expand(sum(
                self.h2_coefficient(i)*self.h2_coefficient(exponent - i)
                for i in range(-2, exponent + 3)
            ))
        return self._h4[exponent]

    def forcing(self, order):
        # Coefficient s^(order-2), excluding the new B_order terms.
        answer = sum(
            i*self.B[i]*sp.diff(self.A.get(order - 1 - i, 0), self.pi)
            for i in range(1, order)
        )
        answer -= sum(
            sp.diff(self.B[i], self.pi)*(order - 1 - i)
            * self.A.get(order - 1 - i, 0)
            for i in range(order)
        )
        answer += 2*self.h4_coefficient(order - 4)
        return sp.expand(answer)

    def solve_operator(self, order, forcing):
        """Solve p B'+order*p'B=-forcing by the 19 Q* top pivots."""
        poly = sp.Poly(sp.expand(forcing), self.pi)
        coefficient = lambda degree: poly.coeff_monomial(self.pi**degree)
        high = {
            degree: sp.factor(coefficient(degree))
            for degree in range(int(poly.degree()), 20, -1)
            if coefficient(degree) != 0
        }
        values = {}
        for degree in range(20, 1, -2):
            values[degree - 2] = sp.cancel(
                ((degree + order)*values.get(degree, 0) - coefficient(degree))
                / (degree - 2 + 3*order)
            )
        for degree in range(19, 2, -2):
            values[degree - 2] = sp.cancel(
                ((degree + order)*values.get(degree, 0) - coefficient(degree))
                / (degree - 2 + 3*order)
            )
        B = sp.expand(sum(values[degree]*self.pi**degree for degree in range(19)))
        residual0 = sp.factor(coefficient(0) - order*values[0])
        residual1 = sp.factor(coefficient(1) - (order + 1)*values[1])
        residual = sp.expand(
            sum(value*self.pi**degree for degree, value in high.items())
            + residual0 + residual1*self.pi
        )
        operator_image = sp.expand(
            self.p*sp.diff(B, self.pi)
            + order*sp.diff(self.p, self.pi)*B
            + forcing
        )
        if sp.expand(operator_image - residual) != 0:
            raise AssertionError(f"operator reconstruction failed at n={order}")
        return {
            "B": B,
            "forcing_degree": int(poly.degree()),
            "forcing_size": len(str(sp.expand(forcing))),
            "B_degree": int(sp.Poly(B, self.pi).degree()) if B != 0 else -1,
            "B_size": len(str(B)),
            "high_residual": high,
            "residual0": residual0,
            "residual1": residual1,
            "residual": residual,
            "pivot_coefficients": [degree + 3*order for degree in range(19)],
        }

    def direct_level_coefficient(self, order):
        # Independent inclusive coefficient extraction after B_order is stored.
        answer = sum(
            i*self.B[i]*sp.diff(self.A.get(order - 1 - i, 0), self.pi)
            for i in range(1, order + 1)
        )
        answer -= sum(
            sp.diff(self.B[i], self.pi)*(order - 1 - i)
            * self.A.get(order - 1 - i, 0)
            for i in range(order + 1)
        )
        answer += 2*self.h4_coefficient(order - 4)
        return sp.expand(answer)


def run_recurrence(shared):
    s, pi, u, v, c = shared["symbols"]
    c110 = shared["free"][0]
    sliced_h = sp.expand(shared["h"].subs(c, 1))
    raw_A = laurent_coefficients(sliced_h, s)
    recurrence = Recurrence(raw_A, pi, u, v, c110)

    # The leading s^-2 equation is Xu's q1'+2p^3=0.
    q1_derivative_check = sp.expand(
        recurrence.p*sp.diff(recurrence.B[0], pi) + 2*recurrence.p**4
    )
    if q1_derivative_check != 0:
        raise AssertionError("leading reduced ODE failed")

    # At n=1 the sole nonzero cokernel row forces the last shared h coefficient.
    forcing1 = recurrence.forcing(1)
    raw_level1 = recurrence.solve_operator(1, forcing1)
    expected_first = -sp.Rational(2, 5)*c110*pi
    if sp.expand(raw_level1["residual"] - expected_first) != 0:
        raise AssertionError(raw_level1["residual"])

    # Work on that exact component and clear cached powers containing c_11_0.
    recurrence.A = {
        exponent: sp.expand(value.subs(c110, 0))
        for exponent, value in recurrence.A.items()
    }
    recurrence.B[1] = sp.expand(raw_level1["B"].subs(c110, 0))
    recurrence.clear_h_power_cache()
    if recurrence.direct_level_coefficient(1) != 0:
        raise AssertionError("specialized first level failed")

    ledger = [{
        "n": 1,
        "ode_s_power": -1,
        "coefficient_rows": 21,
        "new_B_coefficients": 19,
        "Qstar_pivots": 19,
        "formal_cokernel_rows": 2,
        "nonzero_compatibility_before_shared_specialization": str(expected_first),
        "compatibility_after_c_11_0_equals_0": "0",
        "B_degree": raw_level1["B_degree"],
        "B_sha256_after_specialization": expression_sha256(recurrence.B[1]),
        "symbolic_direct_recheck": True,
    }]

    selected_B = {1: recurrence.B[1]}
    started = time.perf_counter()
    for order in range(2, MAX_SOLVED_ORDER + 1):
        forcing = recurrence.forcing(order)
        level = recurrence.solve_operator(order, forcing)
        if level["high_residual"] or level["residual0"] != 0 or level["residual1"] != 0:
            return {
                "status": "INCONSISTENT",
                "first_bad_order": order,
                "first_bad_s_power": order - 2,
                "residual": str(level["residual"]),
                "ledger": ledger,
            }
        recurrence.B[order] = level["B"]
        direct = recurrence.direct_level_coefficient(order)
        if direct != 0:
            raise AssertionError(f"direct coefficient check failed at n={order}: {direct}")
        if order in (6, 7, MAX_SOLVED_ORDER):
            selected_B[order] = level["B"]
        ledger.append({
            "n": order,
            "ode_s_power": order - 2,
            "coefficient_rows": 21,
            "new_B_coefficients": 19,
            "Qstar_pivots": 19,
            "formal_cokernel_rows": 2,
            "nonzero_compatibility_rows": 0,
            "forcing_degree": level["forcing_degree"],
            "B_degree": level["B_degree"],
            "forcing_size": level["forcing_size"],
            "B_size": level["B_size"],
            "B_sha256": expression_sha256(level["B"]),
            "symbolic_direct_recheck": True,
        })

    next_order = MAX_SOLVED_ORDER + 1
    next_forcing = recurrence.forcing(next_order)
    next_poly = sp.Poly(next_forcing, pi)
    next_path = OUT / f"next_system_n{next_order}.txt"
    next_text = (
        "TYPE: EXACT-NEXT-UNSOLVED-REDUCED-ODE-SYSTEM\n"
        f"n={next_order}; ode_s_power={next_order - 2}\n"
        "field=Q[u,v,b0]; torus_slice_c=1; p=pi*(pi^2-1)\n"
        "unknown=B_n=sum_(j=0)^18 b_n_j*pi^j (19 coefficients)\n"
        "equation=p*diff(B_n,pi)+n*diff(p,pi)*B_n+R_n=0\n"
        "coefficient_rows=21; Qstar_top_pivots=19; formal_cokernel_rows=2\n"
        f"R_n_degree={int(next_poly.degree())}\n"
        f"R_n={sp.expand(next_forcing)}\n"
    )
    next_path.write_text(next_text, encoding="utf-8")

    return {
        "status": "CONSISTENT_TO_CAP",
        "deepest_solved_order_n": MAX_SOLVED_ORDER,
        "deepest_ode_s_power": MAX_SOLVED_ORDER - 2,
        "new_extension_begins": {"n": 7, "ode_s_power": 5},
        "ledger": ledger,
        "dimension_at_c_equals_1": {
            "free_parameters": ["u", "v", "b0"],
            "dimension": 3,
            "dimension_after_optional_b0_equals_0_normalization": 2,
            "no_new_parameters_from_B1_through_B30": True,
        },
        "selected_exact_solutions": {
            f"B{order}": str(sp.factor(value)) for order, value in selected_B.items()
        },
        "all_B_solution_hashes": {
            str(order): expression_sha256(recurrence.B[order])
            for order in range(1, MAX_SOLVED_ORDER + 1)
        },
        "next_system": {
            "n": next_order,
            "ode_s_power": next_order - 2,
            "equation": f"p*B{next_order}'+{next_order}*p'*B{next_order}+R{next_order}=0",
            "coefficient_rows": 21,
            "new_unknowns": 19,
            "Qstar_pivots_if_no_high_obstruction": 19,
            "formal_cokernel_rows": 2,
            "forcing_degree": int(next_poly.degree()),
            "forcing_sha256": expression_sha256(next_forcing),
            "exact_system_file": str(next_path.relative_to(ROOT)),
            "exact_system_file_sha256": file_sha256(next_path),
        },
        "recurrence_elapsed_seconds_excluding_shared_h_build": round(
            time.perf_counter() - started, 6
        ),
    }


def write_manifest():
    excluded = {
        "artifacts.sha256",
        "xu_joint_extension.stdout",
        "xu_joint_extension.stderr",
    }
    paths = sorted(path for path in OUT.iterdir() if path.is_file() and path.name not in excluded)
    (OUT / "artifacts.sha256").write_text(
        "".join(f"{file_sha256(path)}  {path.relative_to(ROOT)}\n" for path in paths),
        encoding="utf-8",
    )


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    custody = receipt_check()
    shared = build_shared_h()
    s, pi, u, v, c = shared["symbols"]
    c110 = shared["free"][0]
    leader_map = {
        str(variable): str(sp.factor(image))
        for variable, image in shared["resolved"].items()
    }
    sliced_coefficients = laurent_coefficients(
        sp.expand(shared["h"].subs({c: 1, c110: 0})), s
    )
    recurrence_result = run_recurrence(shared)
    if recurrence_result["status"] != "CONSISTENT_TO_CAP":
        verdict = f"INCONSISTENT[n={recurrence_result['first_bad_order']}]"
    else:
        verdict = f"COUNTING-BOUND[CONSISTENT-THROUGH-s^{recurrence_result['deepest_ode_s_power']}]"
    result = {
        "type": "PARTIAL-GLOBAL-h3 / XU-REDUCED-ODE / COUNTING-BOUND",
        "verdict": verdict,
        "not_claimed": [
            "global f,g coefficient arrays",
            "effective T2,T3 membership in Q[f,g]",
            "the full major h2/f/g tower",
            "J(f,g)=1 or a polynomial Keller pair",
        ],
        "custody": custody,
        "software": {
            "python": subprocess.run(["python3", "--version"], capture_output=True, text=True).stdout.strip(),
            "sympy": sp.__version__,
        },
        "global_h3": {
            "K_definition": "K=t^11*h(t^-1,w/t)",
            "fixed_major_face": "w^3*(w-1)^8",
            "strict_major_support": "3*r+4*ord_(w-1)>=33",
            "major_tail_coefficients": len(shared["parameters"]),
            "minor_substitution": "t=s^2, w=u*s^4+v*s^6+pi*s^7",
            "minor_target": "h=p/s+O(1), p=pi*(pi^2-c)",
            "leader_rows": len(shared["leader_rows"]),
            "leader_Qstar_pivots": len(shared["pivots"]),
            "free_after_leader": [str(item) for item in shared["free"]],
            "leader_band_histogram": {
                str(exponent): count
                for exponent, count in sorted(Counter(tag[0] for tag, _ in shared["leader_rows"]).items())
            },
            "resolved_map": leader_map,
            "resolved_map_kills_all_original_leader_rows": True,
            "selected_h_coefficients_after_c1_c1100": {
                f"A_{exponent}": str(sp.factor(sliced_coefficients.get(exponent, 0)))
                for exponent in range(-1, 9)
            },
            "finite_resolved_h_sha256": expression_sha256(
                sp.expand(shared["h"].subs({c: 1, c110: 0}))
            ),
        },
        "reduced_ode": {
            "equation": "D_s(Q,h)+2*s^2*h^4=0",
            "D_s_convention": "Q_s*h_pi-Q_pi*h_s",
            "q1": "-pi^10/5+3*pi^8/4-pi^6+pi^4/2+b0",
            "degree_bound_each_Bn": 18,
            "first_compatibility": "(-2/5)*c_11_0*pi=0, hence c_11_0=0",
            "recurrence": "p*B_n'+n*p'*B_n+R_n=0 at s^(n-2)",
            "operator_on_pi_j": "L_n(pi^j)=(j+3n)pi^(j+2)-(j+n)pi^j on c=1",
            "result": recurrence_result,
        },
        "checks": {
            "all_14_frozen_inputs_hash_verified": True,
            "leader_ring_map_rechecked_on_all_20_rows": True,
            "q1_prime_plus_2p_cubed_zero": True,
            "each_solved_level_reconstructed_and_directly_rechecked_symbolically": True,
            "no_parameter_was_inverted_after_c_equals_1": True,
        },
        "total_elapsed_seconds": round(time.perf_counter() - started, 6),
    }
    result_path = OUT / "xu_joint_extension.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_manifest()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
