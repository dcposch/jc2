#!/usr/bin/env python3
"""Standalone exact-Q replay for the D=108, delta=3 certificate slice.

The script rebuilds the common-h3 expansion through local t-power 8,
performs the seven rational Q* pivots while carrying row-operation lifts,
and checks both the reduced and pre-pivot certificates.  It intentionally
does not import a campaign engine or read a ledger.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from math import ceil, comb, factorial
import json

import sympy as sp


jet1, jet2, pi, c, Zc = sp.symbols("jet1 jet2 pi c Zc")


def h3_template() -> tuple[dict[tuple[int, int], sp.Expr], list[sp.Symbol]]:
    """Return the seven-coordinate post-major h3 chart in z=w-1."""
    h3: dict[tuple[int, int], sp.Expr] = {
        (0, 7): sp.Integer(1),
        (0, 8): sp.Integer(2),
        (0, 9): sp.Integer(1),
    }
    variables: list[sp.Symbol] = []
    for r in range(1, 10):
        vmin = max(0, ceil((43 - 4 * r) / 6))
        cap = 9 - r
        for degree in range(vmin, cap + 1):
            variable = sp.Symbol(f"Hc_{r}_{degree}")
            variables.append(variable)
            # z^vmin*w^(degree-vmin), expanded in z using w=1+z.
            for q in range(vmin, degree + 1):
                h3[(r, q)] = h3.get((r, q), 0) + variable * comb(
                    degree - vmin, q - vmin
                )
    expected = [
        "Hc_1_7", "Hc_1_8", "Hc_2_6", "Hc_2_7",
        "Hc_3_6", "Hc_4_5", "Hc_5_4",
    ]
    assert [str(v) for v in variables] == expected
    return {key: sp.expand(value) for key, value in h3.items()}, variables


def z_to_w(h3: dict[tuple[int, int], sp.Expr]) -> dict[tuple[int, int], sp.Expr]:
    """Convert t^r z^q to t^r w^j, using z=w-1."""
    result: dict[tuple[int, int], sp.Expr] = defaultdict(lambda: sp.Integer(0))
    for (r, q), coefficient in h3.items():
        for j in range(q + 1):
            result[(r, j)] += coefficient * comb(q, j) * (-1) ** (q - j)
    return {key: sp.expand(value) for key, value in result.items() if value != 0}


def incidence_rows() -> list[tuple[str, sp.Expr]]:
    """Substitute w=jet1*t^2+jet2*t^3+pi*t^4 through t^8."""
    h3, _ = h3_template()
    wbasis = z_to_w(h3)
    collected: dict[tuple[int, int], sp.Expr] = defaultdict(lambda: sp.Integer(0))
    for (r, j), coefficient in wbasis.items():
        for a in range(j + 1):
            for b in range(j - a + 1):
                k = j - a - b
                power = r + 2 * a + 3 * b + 4 * k
                if power > 8:
                    continue
                multinomial = factorial(j) // (
                    factorial(a) * factorial(b) * factorial(k)
                )
                collected[(power, k)] += (
                    coefficient * multinomial * jet1**a * jet2**b
                )

    # w^2(w-1)^7=-w^2+O(w^3), hence K3=t^8(c-pi^2)+O(t^9).
    collected[(8, 0)] -= c
    collected[(8, 2)] += 1
    rows = [
        (f"minor_n{power}_pi{k}", sp.expand(value))
        for (power, k), value in sorted(collected.items())
    ]
    assert len(rows) == 13
    assert sum(value != 0 for _, value in rows) == 12
    assert dict(rows)["minor_n8_pi2"] == 0
    return rows


@dataclass(frozen=True)
class Pivot:
    row: str
    variable: sp.Symbol
    coefficient: sp.Rational
    rhs_at_pivot: sp.Expr


def qstar_with_lifts(
    raw_rows: list[tuple[str, sp.Expr]], eligible: list[sp.Symbol]
) -> tuple[
    list[tuple[str, sp.Expr, dict[str, sp.Expr]]],
    list[Pivot],
    dict[sp.Symbol, sp.Expr],
]:
    """Rational Q* elimination, retaining identities in the raw rows."""
    raw = dict(raw_rows)
    work = [
        [label, sp.expand(row), {label: sp.Integer(1)}]
        for label, row in raw_rows
        if row != 0
    ]
    available = set(eligible)
    pivots: list[Pivot] = []

    while True:
        selected = None
        for index, (label, row, _lift) in enumerate(work):
            for variable in sorted(row.free_symbols.intersection(available), key=str):
                coefficient = sp.diff(row, variable)
                remainder = sp.expand(row - coefficient * variable)
                if (
                    coefficient.is_Rational
                    and coefficient != 0
                    and variable not in remainder.free_symbols
                ):
                    selected = (
                        index, label, variable, sp.Rational(coefficient), remainder
                    )
                    break
            if selected is not None:
                break
        if selected is None:
            break

        index, label, variable, coefficient, remainder = selected
        pivot_label, pivot_row, pivot_lift = work.pop(index)
        assert pivot_label == label
        rhs = sp.cancel(-remainder / coefficient)
        pivots.append(Pivot(label, variable, coefficient, rhs))
        available.remove(variable)

        reduced = []
        for old_label, old_row, old_lift in work:
            multiplier = sp.diff(old_row, variable) / coefficient
            assert variable not in sp.expand(
                old_row - sp.diff(old_row, variable) * variable
            ).free_symbols
            new_row = sp.expand(old_row - multiplier * pivot_row)
            keys = set(old_lift).union(pivot_lift)
            new_lift = {
                key: sp.expand(
                    old_lift.get(key, 0) - multiplier * pivot_lift.get(key, 0)
                )
                for key in keys
            }
            new_lift = {key: value for key, value in new_lift.items() if value != 0}
            assert variable not in new_row.free_symbols
            assert all(variable not in value.free_symbols for value in new_lift.values())
            assert sp.expand(
                sum(value * raw[key] for key, value in new_lift.items()) - new_row
            ) == 0
            if new_row != 0:
                reduced.append([old_label, new_row, new_lift])
        work = reduced

    substitutions = {pivot.variable: pivot.rhs_at_pivot for pivot in pivots}
    for _ in range(len(substitutions) + 2):
        changed = False
        for variable, rhs in list(substitutions.items()):
            others = {key: value for key, value in substitutions.items() if key != variable}
            image = sp.expand(rhs.subs(others, simultaneous=True))
            if image != rhs:
                substitutions[variable] = image
                changed = True
        if not changed:
            break
    return [(label, row, lift) for label, row, lift in work], pivots, substitutions


def expression_text(value: sp.Expr) -> str:
    return str(sp.factor(value))


def main() -> None:
    rows = incidence_rows()
    raw = dict(rows)
    _, hvars = h3_template()
    residual_rows, pivots, substitutions = qstar_with_lifts(rows, hvars)
    residual = {label: sp.expand(value) for label, value, _ in residual_rows}

    expected_residual = {
        "minor_n6_pi0": -jet2**2,
        "minor_n7_pi0": 2 * jet1**2 * jet2,
        "minor_n7_pi1": -2 * jet2,
        "minor_n8_pi0": -c - jet1**4 + 9 * jet1 * jet2**2,
        "minor_n8_pi1": 2 * jet1**2,
    }
    assert residual == expected_residual
    expected_substitutions = {
        "Hc_1_7": "0",
        "Hc_1_8": "0",
        "Hc_2_6": "0",
        "Hc_2_7": "2*jet1",
        "Hc_3_6": "0",
        "Hc_4_5": "jet1**2",
        "Hc_5_4": "0",
    }
    assert {str(key): str(value) for key, value in substitutions.items()} == expected_substitutions

    wrapper = Zc * c - 1
    # The human-readable certificate follows the charged three-line argument.
    readable_reduced_coefficients = {
        "minor_n7_pi1": -sp.Rational(9, 2) * jet1 * jet2 * Zc,
        "minor_n8_pi0": -Zc,
        "minor_n8_pi1": -sp.Rational(1, 2) * jet1**2 * Zc,
    }
    readable_reduced_identity = -wrapper + sum(
        readable_reduced_coefficients.get(label, 0) * value
        for label, value in residual.items()
    )
    assert sp.expand(readable_reduced_identity) == 1

    # Strict support pruning in the reduced ideal removes r71.  These three
    # coefficients give 1 from (r80,r81,L), and none of those three generators
    # may be dropped (explicit witnesses are checked below).
    minimal_reduced_coefficients = {
        "minor_n8_pi0": -9 * jet1 * jet2**2 * Zc**2 - Zc,
        "minor_n8_pi1": (
            -sp.Rational(9, 2) * jet1**3 * jet2**2 * Zc**2
            + sp.Rational(81, 2) * jet2**4 * Zc**2
            - sp.Rational(1, 2) * jet1**2 * Zc
        ),
    }
    minimal_wrapper_coefficient = -9 * jet1 * jet2**2 * Zc - 1
    minimal_reduced_identity = minimal_wrapper_coefficient * wrapper + sum(
        minimal_reduced_coefficients.get(label, 0) * value
        for label, value in residual.items()
    )
    assert sp.expand(minimal_reduced_identity) == 1

    # Back-substitute both certificates through the row-operation lifts,
    # removing every zero coefficient.
    def lift_certificate(coefficients: dict[str, sp.Expr]) -> dict[str, sp.Expr]:
        lifted = {label: sp.Integer(0) for label, _ in rows}
        for label, _value, lift in residual_rows:
            multiplier = coefficients.get(label, 0)
            for raw_label, lift_coefficient in lift.items():
                lifted[raw_label] = sp.expand(
                    lifted[raw_label] + multiplier * lift_coefficient
                )
        return {label: coefficient for label, coefficient in lifted.items() if coefficient != 0}

    readable_raw_coefficients = lift_certificate(readable_reduced_coefficients)
    readable_raw_identity = -wrapper + sum(
        readable_raw_coefficients[label] * raw[label]
        for label in readable_raw_coefficients
    )
    assert sp.expand(readable_raw_identity) == 1
    assert len(readable_raw_coefficients) == 10

    minimal_raw_coefficients = lift_certificate(minimal_reduced_coefficients)
    minimal_raw_identity = minimal_wrapper_coefficient * wrapper + sum(
        minimal_raw_coefficients[label] * raw[label]
        for label in minimal_raw_coefficients
    )
    assert sp.expand(minimal_raw_identity) == 1
    assert len(minimal_raw_coefficients) == 9

    # Inclusion-minimality of (r80,r81,L): after deleting any one generator,
    # the remaining two have the displayed common zero.
    drop_witnesses = {
        "minor_n8_pi0": {jet1: 0, jet2: 0, c: 1, Zc: 1},
        "minor_n8_pi1": {jet1: 1, jet2: 0, c: -1, Zc: -1},
        "Zc*c-1": {jet1: 0, jet2: 0, c: 0, Zc: 0},
    }
    minimal_three = {
        "minor_n8_pi0": residual["minor_n8_pi0"],
        "minor_n8_pi1": residual["minor_n8_pi1"],
        "Zc*c-1": wrapper,
    }
    for dropped, witness0 in drop_witnesses.items():
        assert all(
            sp.expand(value.subs(witness0)) == 0
            for label, value in minimal_three.items()
            if label != dropped
        )

    # Every recorded Q* pivot lies in the dependency closure of either the
    # readable three-residue support or the strictly pruned two-residue support.
    pivot_by_variable = {pivot.variable: pivot.row for pivot in pivots}
    pending = set().union(
        *(raw[label].free_symbols.intersection(hvars) for label in minimal_reduced_coefficients)
    )
    pivot_closure: set[str] = set()
    while pending:
        variable = pending.pop()
        pivot_label = pivot_by_variable[variable]
        if pivot_label in pivot_closure:
            continue
        pivot_closure.add(pivot_label)
        pending.update(raw[pivot_label].free_symbols.intersection(hvars))
    assert pivot_closure == {pivot.row for pivot in pivots}

    # Perturb the n=8, pi^0 incidence row by deleting its -c term.  The
    # displayed certificate ceases to be 1, and the explicit point below
    # satisfies every perturbed support row plus the localization wrapper.
    perturbed_raw = dict(raw)
    perturbed_raw["minor_n8_pi0"] = sp.expand(raw["minor_n8_pi0"] + c)
    perturbed_identity = minimal_wrapper_coefficient * wrapper + sum(
        minimal_raw_coefficients[label] * perturbed_raw[label]
        for label in minimal_raw_coefficients
    )
    assert sp.expand(perturbed_identity - 1) != 0
    witness = {**{variable: 0 for variable in hvars}, jet1: 0, jet2: 0, c: 1, Zc: 1}
    assert all(
        sp.expand(perturbed_raw[label].subs(witness)) == 0
        for label in minimal_raw_coefficients
    )
    assert sp.expand(wrapper.subs(witness)) == 0

    output = {
        "case": "D108-delta3",
        "ring": "Q[Hc_1_7,Hc_1_8,Hc_2_6,Hc_2_7,Hc_3_6,Hc_4_5,Hc_5_4,jet1,jet2,c,Zc]",
        "provenance": {"incidence": 9, "localization": 1, "outer": 0, "pole": 0, "Jacobian": 0},
        "deepest_t_power": 8,
        "raw_label_count": len(rows),
        "raw_nonzero_count": sum(value != 0 for _, value in rows),
        "qstar_pivots": [
            {
                "row": pivot.row,
                "variable": str(pivot.variable),
                "coefficient": str(pivot.coefficient),
                "resolved_value": str(substitutions[pivot.variable]),
            }
            for pivot in pivots
        ],
        "pivot_dependency_closure": sorted(pivot_closure),
        "residual": {label: str(value) for label, value in residual.items()},
        "readable_three_residue_certificate": {
            **{label: expression_text(value) for label, value in readable_reduced_coefficients.items()},
            "Zc*c-1": "-1",
        },
        "readable_prepivot_certificate": {
            **{label: expression_text(value) for label, value in readable_raw_coefficients.items()},
            "Zc*c-1": "-1",
        },
        "minimal_reduced_certificate": {
            **{label: expression_text(value) for label, value in minimal_reduced_coefficients.items()},
            "Zc*c-1": expression_text(minimal_wrapper_coefficient),
        },
        "minimal_prepivot_certificate": {
            **{label: expression_text(value) for label, value in minimal_raw_coefficients.items()},
            "Zc*c-1": expression_text(minimal_wrapper_coefficient),
        },
        "minimal_prepivot_support_rows": len(minimal_raw_coefficients) + 1,
        "readable_prepivot_support_rows": len(readable_raw_coefficients) + 1,
        "identity": str(sp.expand(minimal_raw_identity)),
        "outer_A2_A3_B2_touched": False,
        "T2_T3_bridge_touched": False,
        "perturbation_control": {
            "change": "minor_n8_pi0 := minor_n8_pi0 + c",
            "certificate_still_one": False,
            "nonempty_witness": {str(key): str(value) for key, value in witness.items()},
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
