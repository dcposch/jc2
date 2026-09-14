#!/usr/bin/env python3
"""Exact partial common-jet probe for the (99,66) campaign.

This driver deliberately stops at the degree-11 approximate root ``h``.  It
uses one finite set of coefficients for

    K(x,w) = x^11 h(x^-1,w/x)

at the major direction and then expands that *same* K at either the delta=2
or the delta=5/2 minor direction.  Thus its equalities really are shared-jet
equalities.  It does not contain global f/g coefficient arrays, the missing
4/9 centre, h_2, or the effective T_2/T_3 recurrences, and therefore is not a
joint Keller system.

All arithmetic is exact SymPy arithmetic over Q and polynomial parameter
rings.  The program writes nothing; its JSON result goes to stdout.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import json
from math import ceil
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RECEIPT = ROOT / "xmodel/g9966-global-design-sol56-20260903.run.v2"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def check_frozen_inputs() -> dict:
    """Parse the lane receipt and verify every frozen input named by it."""
    receipt_fields = {}
    for raw_line in RECEIPT.read_text(encoding="utf-8").splitlines():
        if "=" in raw_line:
            key, value = raw_line.split("=", 1)
            receipt_fields[key] = value
    count = int(receipt_fields["charged_inputs"])
    lane_inputs = Path(receipt_fields["lane_inputs_dir"])
    checked = {}
    for index in range(1, count + 1):
        basename = receipt_fields[f"charged_input_{index}_basename"]
        expected = receipt_fields[f"charged_input_{index}_sha256"]
        if Path(basename).name != basename:
            raise AssertionError(f"receipt basename is not a basename: {basename}")
        frozen_path = lane_inputs / basename
        actual = sha256(frozen_path)
        if actual != expected:
            raise AssertionError(f"frozen charged-input hash mismatch: {basename}")
        checked[str(index)] = {
            "basename": basename,
            "sha256": actual,
            "frozen_path": str(frozen_path),
        }
    assert len(checked) == count == 14
    return {
        "receipt": str(RECEIPT),
        "lane_inputs_dir_from_receipt": str(lane_inputs),
        "charged_inputs": count,
        "all_hashes_match": True,
        "files": checked,
    }


def laurent_coefficients(expression: sp.Expr, variable: sp.Symbol) -> dict[int, sp.Expr]:
    """Return an exact exponent -> coefficient map, allowing negative powers."""
    answer: dict[int, sp.Expr] = {}
    for term in sp.Add.make_args(sp.expand(expression)):
        exponent = int(term.as_powers_dict().get(variable, 0))
        answer[exponent] = sp.expand(
            answer.get(exponent, 0) + term / variable**exponent
        )
    return answer


def polynomial_rows(
    expression: sp.Expr, variable: sp.Symbol, outer_tag: int
) -> list[tuple[tuple[int, int], sp.Expr]]:
    return [
        ((outer_tag, monomial[0]), sp.expand(coefficient))
        for monomial, coefficient in sp.Poly(sp.expand(expression), variable).terms()
        if coefficient != 0
    ]


def qstar_reduce(
    tagged_rows: list[tuple[tuple[int, int], sp.Expr]],
    variables: list[sp.Symbol],
) -> tuple[
    list[tuple[tuple[int, int], sp.Expr]],
    list[sp.Symbol],
    list[tuple[tuple[int, int], sp.Symbol, sp.Rational, sp.Expr]],
]:
    """Deterministically eliminate only affine pivots in Q*."""
    rows = list(tagged_rows)
    remaining = list(variables)
    pivots = []
    while True:
        choice = None
        for row_index, (tag, expression) in enumerate(rows):
            for variable_index, variable in enumerate(remaining):
                coefficient = sp.expand(sp.diff(expression, variable))
                remainder = sp.expand(expression - coefficient * variable)
                if (
                    coefficient.is_Rational
                    and coefficient != 0
                    and variable not in remainder.free_symbols
                ):
                    choice = (
                        row_index,
                        variable_index,
                        tag,
                        variable,
                        sp.Rational(coefficient),
                        remainder,
                    )
                    break
            if choice is not None:
                break
        if choice is None:
            break
        row_index, variable_index, tag, variable, coefficient, remainder = choice
        rhs = sp.expand(-remainder / coefficient)
        assert sp.expand(rows[row_index][1].subs(variable, rhs)) == 0
        pivots.append((tag, variable, coefficient, rhs))
        del rows[row_index]
        del remaining[variable_index]
        reduced_rows = []
        for old_tag, expression in rows:
            image = sp.expand(expression.subs(variable, rhs))
            if image != 0:
                reduced_rows.append((old_tag, image))
        rows = reduced_rows
    return rows, remaining, pivots


def resolve_pivots(
    pivots: list[tuple[tuple[int, int], sp.Symbol, sp.Rational, sp.Expr]]
) -> dict[sp.Symbol, sp.Expr]:
    resolved: dict[sp.Symbol, sp.Expr] = {}
    pivot_variables = {pivot[1] for pivot in pivots}
    for _tag, variable, _coefficient, rhs in reversed(pivots):
        image = sp.expand(rhs.subs(resolved, simultaneous=True))
        assert not image.free_symbols.intersection(pivot_variables)
        resolved[variable] = image
    return resolved


def build_major_K():
    x, w = sp.symbols("x w")
    K = w**3 * (w - 1) ** 8
    parameters = []
    support = []
    for r in range(1, 12):
        cap = 11 - r
        vanish_at_one = max(0, ceil((33 - 3 * r) / 4))
        for degree in range(vanish_at_one, cap + 1):
            coefficient = sp.Symbol(f"c_{r}_{degree}")
            parameters.append(coefficient)
            support.append((r, degree, vanish_at_one))
            K += (
                coefficient
                * x**r
                * (w - 1) ** vanish_at_one
                * w ** (degree - vanish_at_one)
            )
    K = sp.expand(K)
    assert len(parameters) == 21
    return x, w, K, parameters, support


def delta2_probe(x, w, K, parameters):
    z, a, u = sp.symbols("z a u")
    H = sp.expand(z**2 * (z + 3 * a))
    expansion = sp.Poly(sp.expand(K.subs(w, u * x**2 + x**3 * z)), x, z)
    tagged_rows = []
    for x_degree in range(10):
        for z_degree in range(12):
            coefficient = expansion.coeff_monomial(x**x_degree * z**z_degree)
            target = H.coeff(z, z_degree) if x_degree == 9 else 0
            equation = sp.expand(coefficient - target)
            if equation != 0:
                tagged_rows.append(((x_degree, z_degree), equation))

    residual, free, pivots = qstar_reduce(tagged_rows, parameters)
    resolved = resolve_pivots(pivots)
    assert not residual
    assert [str(item) for item in free] == ["c_7_4", "c_10_1", "c_11_0"]
    assert len(tagged_rows) == len(pivots) == 18
    assert all(
        sp.expand(expression.subs(resolved, simultaneous=True)) == 0
        for _tag, expression in tagged_rows
    )

    # Exact shared h-jet in the straightened u=0 slice.  In particular the
    # fixed W_3 and W_6 used by the branch-B lift are recovered mechanically.
    straight = sp.expand(
        K.subs(resolved, simultaneous=True).subs({w: x**3 * z, u: 0}) / x**9
    )
    straight_bands = laurent_coefficients(straight, x)
    assert sp.expand(straight_bands[0] - H) == 0
    assert sp.expand(straight_bands[3] - (-8 * z**4 - 18 * a * z**3)) == 0
    assert sp.expand(straight_bands[6] - (28 * z**5 + 45 * a * z**4)) == 0

    # Positive and negative controls use an exact rational point.  The
    # negative control changes a Q* pivot and must violate at least one row.
    positive = {a: 2, u: 3, free[0]: 5, free[1]: 7, free[2]: 11}
    for variable, rhs in resolved.items():
        positive[variable] = sp.expand(rhs.subs(positive, simultaneous=True))
    assert all(sp.expand(row.subs(positive, simultaneous=True)) == 0
               for _tag, row in tagged_rows)
    negative = dict(positive)
    negative[sp.Symbol("c_1_8")] = 1
    assert any(sp.expand(row.subs(negative, simultaneous=True)) != 0
               for _tag, row in tagged_rows)

    raw_by_band = Counter(tag[0] for tag, _row in tagged_rows)
    pivot_by_band = Counter(tag[0] for tag, *_rest in pivots)
    cumulative_rank = 0
    ledger = []
    for band in sorted(raw_by_band):
        cumulative_rank += pivot_by_band[band]
        ledger.append({
            "minor_x_band": band,
            "new_rows": raw_by_band[band],
            "new_Qstar_rank": pivot_by_band[band],
            "cumulative_rank": cumulative_rank,
            "dimension_including_a_u": 21 + 2 - cumulative_rank,
        })

    return {
        "scope": "COMMON-GLOBAL-h-JET ONLY; major 1/3 filter plus delta=2 face",
        "ambient": {
            "major_h_coefficients": 21,
            "face_parameters": ["a", "u=a1"],
            "dimension_before_minor_rows": 23,
        },
        "rows": len(tagged_rows),
        "Qstar_rank": len(pivots),
        "free_h_coefficients": [str(item) for item in free],
        "final_dimension_including_a_u": len(free) + 2,
        "band_ledger": ledger,
        "shared_straight_h_bands": {
            "x^0": str(sp.factor(straight_bands[0])),
            "x^1": str(sp.factor(straight_bands[1])),
            "x^2": str(sp.factor(straight_bands[2])),
            "x^3": str(sp.factor(straight_bands[3])),
            "x^6": str(sp.factor(straight_bands[6])),
        },
        "controls": {
            "resolved_map_kills_every_row": True,
            "positive_rational_point": True,
            "perturbed_Qstar_pivot_is_rejected": True,
        },
    }


def delta52_probe(x, w, K, parameters):
    # The curved principal-minor prefix is retained.  K, rather than h=K/s^22,
    # is used for coefficient extraction so Poly.coeff_monomial never sees a
    # Laurent polynomial.  In particular, do not use Expr.coeff on the target:
    # for the unexpanded expression pi*(pi**2-c), Expr.coeff(pi,1) has the
    # wrong semantics for this task.
    s, pi, u, v, c = sp.symbols("s pi u v c")
    minor_w = u * s**4 + v * s**6 + pi * s**7
    minor_K = sp.Poly(sp.expand(K.subs({x: s**2, w: minor_w})), s, pi)
    target = sp.Poly(pi * (pi**2 - c), pi)
    assert target.coeff_monomial(pi) == -c
    assert target.coeff_monomial(pi**3) == 1

    tagged_leader_rows = []
    for s_degree in range(22):
        for pi_degree in range(12):
            coefficient = minor_K.coeff_monomial(s**s_degree * pi**pi_degree)
            wanted = target.coeff_monomial(pi**pi_degree) if s_degree == 21 else 0
            equation = sp.expand(coefficient - wanted)
            if equation != 0:
                tagged_leader_rows.append(((s_degree, pi_degree), equation))

    residual, h_free, h_pivots = qstar_reduce(tagged_leader_rows, parameters)
    h_map = resolve_pivots(h_pivots)
    assert not residual
    assert len(tagged_leader_rows) == len(h_pivots) == 20
    assert [str(item) for item in h_free] == ["c_11_0"]
    assert sp.expand(h_map[sp.Symbol("c_7_4")] - (c - 3 * u**2 * v)) == 0
    assert all(
        sp.expand(expression.subs(h_map, simultaneous=True)) == 0
        for _tag, expression in tagged_leader_rows
    )

    # Positive and negative target controls.  The positive point retains the
    # free c_11_0; the negative point perturbs one resolved global h
    # coefficient and therefore must miss the requested target.
    positive = {u: 2, v: 3, c: 5, h_free[0]: 7}
    for variable, rhs in h_map.items():
        positive[variable] = sp.expand(rhs.subs(positive, simultaneous=True))
    assert all(sp.expand(row.subs(positive, simultaneous=True)) == 0
               for _tag, row in tagged_leader_rows)
    negative = dict(positive)
    negative[sp.Symbol("c_7_4")] += 1
    assert any(sp.expand(row.subs(negative, simultaneous=True)) != 0
               for _tag, row in tagged_leader_rows)

    h = sp.expand(K.subs(h_map, simultaneous=True).subs({x: s**2, w: minor_w}) / s**22)
    h_coefficients = laurent_coefficients(h, s)
    A = {index: h_coefficients.get(index, sp.Integer(0)) for index in range(-1, 6)}
    assert sp.expand(A[-1] - pi * (pi**2 - c)) == 0

    # Compute only the six h^4 coefficients needed below.  The three explicit
    # indices are ordered, and the determined fourth index preserves the
    # ordered-quadruple multiplicities of a literal expansion.
    h4_coefficients = {}
    indices = range(-1, 6)
    for wanted_degree in range(-3, 3):
        terms = []
        for i1 in indices:
            for i2 in indices:
                for i3 in indices:
                    i4 = wanted_degree - i1 - i2 - i3
                    if i4 in A:
                        terms.append(A[i1] * A[i2] * A[i3] * A[i4])
        h4_coefficients[wanted_degree] = sp.expand(sum(terms, sp.Integer(0)))

    # Xu's reduced equation is D_s(Q,h)+2*s^2*h^4=0, with
    # D_s(Q,h)=Q_s*h_pi-Q_pi*h_s.  If Q=sum_j Q_j*s^j and
    # h=sum_i A_i*s^i, its coefficient at s^(n-2) is the following finite
    # recurrence.  Degree(B_n)<=18 gives nineteen fresh Q coefficients.
    q1 = -pi**10 / 5 + 3 * c * pi**8 / 4 - c**2 * pi**6 + c**3 * pi**4 / 2
    Q = {0: q1}
    B_variables = {}
    ode_map: dict[sp.Symbol, sp.Expr] = {}
    raw_recurrences = {}
    ode_ledger = []
    c110 = h_free[0]
    for n in range(1, 7):
        B_variables[n] = list(sp.symbols(f"b{n}_0:19"))
        Q[n] = sum(B_variables[n][degree] * pi**degree for degree in range(19))
        recurrence = 2 * h4_coefficients[n - 4]
        for j in range(n + 1):
            i = n - 1 - j
            if i in A:
                recurrence += (
                    j * Q[j] * sp.diff(A[i], pi)
                    - i * sp.diff(Q[j], pi) * A[i]
                )
        raw_recurrences[n] = sp.expand(recurrence)
        current = sp.expand(recurrence.subs(ode_map, simultaneous=True))
        tagged_rows = polynomial_rows(current, pi, n)
        variables = list(B_variables[n]) + ([c110] if n == 1 else [])
        level_residual, level_free, level_pivots = qstar_reduce(tagged_rows, variables)
        level_map = resolve_pivots(level_pivots)
        localized_rows = []
        if n == 1:
            assert [str(item) for item in level_free] == ["c_11_0"]
            assert len(level_residual) == 1
            compatibility = sp.factor(level_residual[0][1])
            assert sp.expand(compatibility + sp.Rational(2, 5) * c**4 * c110) == 0
            localized_rows = [str(compatibility)]
            # c is nonzero on the split stratum, so this is exactly c_11_0=0.
            level_map = {
                variable: sp.expand(rhs.subs(c110, 0))
                for variable, rhs in level_map.items()
            }
            level_map[c110] = sp.Integer(0)
        else:
            assert not level_residual and not level_free
        assert len(tagged_rows) == 21
        assert len(level_pivots) == 19
        # Complete symbolic ring-map check on every row at this level.
        assert all(
            sp.expand(row.subs(level_map, simultaneous=True)) == 0
            for _tag, row in tagged_rows
        )
        ode_map.update(level_map)
        ode_ledger.append({
            "n": n,
            "ode_s_power": n - 2,
            "new_Q_coefficients": 19,
            "coefficient_rows": len(tagged_rows),
            "Qstar_rank": len(level_pivots),
            "old_localized_compatibility_rank": 1 if n == 1 else 0,
            "localized_compatibility": localized_rows,
            "cumulative_dimension_including_u_v_c_excluding_q1_constant": 3,
            "dimension_after_c_equals_1_excluding_q1_constant": 2,
        })

    # Recheck every uneliminated recurrence through s^4 under the final map,
    # not only the pivot rows used to obtain that map.
    assert all(
        sp.expand(recurrence.subs(ode_map, simultaneous=True)) == 0
        for recurrence in raw_recurrences.values()
    )
    positive_ode = {u: 1, v: 2, c: 3}
    positive_ode.update({
        variable: sp.expand(rhs.subs(positive_ode, simultaneous=True))
        for variable, rhs in ode_map.items()
    })
    assert all(
        sp.expand(recurrence.subs(positive_ode, simultaneous=True)) == 0
        for recurrence in raw_recurrences.values()
    )
    negative_ode = dict(positive_ode)
    negative_ode[c110] = 1
    assert sp.expand(raw_recurrences[1].subs(negative_ode, simultaneous=True)) != 0

    leader_counter = Counter(tag[0] for tag, _row in tagged_leader_rows)
    pivot_counter = Counter(tag[0] for tag, *_rest in h_pivots)
    cumulative_rank = 0
    leader_ledger = []
    for s_degree in range(22):
        cumulative_rank += pivot_counter[s_degree]
        leader_ledger.append({
            "K_s_power": s_degree,
            "new_rows": leader_counter[s_degree],
            "new_Qstar_rank": pivot_counter[s_degree],
            "cumulative_rank": cumulative_rank,
            "dimension_including_u_v_c": 21 + 3 - cumulative_rank,
        })

    shared_specialization = {
        "c_11_0": "0",
        "b1_9": str(sp.factor(ode_map[sp.Symbol("b1_9")])),
        "b2_8": str(sp.factor(ode_map[sp.Symbol("b2_8")])),
        "b4_8": str(sp.factor(ode_map[sp.Symbol("b4_8")])),
        "b6_8": str(sp.factor(ode_map[sp.Symbol("b6_8")])),
    }

    return {
        "scope": (
            "FIXED-MAJOR-FACE H-ORDER-SPACE; same global h3 at major 1/3 "
            "and curved delta=5/2 minor chart; not the full tower/global pair"
        ),
        "coordinates": {
            "K": "x^11*h(x^-1,w/x)",
            "x": "s^2",
            "w": "u*s^4+v*s^6+pi*s^7",
            "target": "coefficients below s^21 vanish; [s^21]K=pi*(pi^2-c)",
            "open_stratum": "c != 0",
        },
        "leader": {
            "ambient_major_h_coefficients": 21,
            "rows": len(tagged_leader_rows),
            "Qstar_rank": len(h_pivots),
            "free_h_coefficients": [str(item) for item in h_free],
            "dimension_including_u_v_c": 4,
            "dimension_after_c_equals_1": 3,
            "selected_shared_map": {
                "c_2_9": str(sp.factor(h_map[sp.Symbol("c_2_9")])),
                "c_3_8": str(sp.factor(h_map[sp.Symbol("c_3_8")])),
                "c_7_4": str(sp.factor(h_map[sp.Symbol("c_7_4")])),
                "c_10_1": str(sp.factor(h_map[sp.Symbol("c_10_1")])),
            },
            "band_ledger": leader_ledger,
        },
        "shared_h_coefficients": {
            f"A_{index}": str(sp.factor(A[index])) for index in range(-1, 6)
        },
        "ode": {
            "equation": "D_s(Q,h)+2*s^2*h^4=0",
            "normalization": "q1 additive constant b0 fixed to zero",
            "ledger": ode_ledger,
            "shared_specialization_of_uncoupled_Xu_parameters": shared_specialization,
            "final_dimension_including_u_v_c_excluding_b0": 3,
            "final_dimension_including_u_v_c_and_restored_b0": 4,
            "final_dimension_at_c_equals_1_excluding_b0": 2,
            "final_dimension_at_c_equals_1_including_restored_b0": 3,
            "first_uncomputed_equation": "n=7, coefficient s^5 of D_s(Q,h)+2*s^2*h^4",
        },
        "controls": {
            "Poly_coeff_monomial_target_coefficients_checked": True,
            "shared_map_kills_every_leader_row": True,
            "positive_curved_target_point": True,
            "perturbed_global_h_coefficient_rejected": True,
            "all_ODE_rows_rechecked_under_final_ring_map": True,
            "positive_ODE_point": True,
            "c_11_0_perturbation_rejected_at_s^-1": True,
        },
    }


def main() -> None:
    frozen_input_verification = check_frozen_inputs()
    x, w, K, parameters, support = build_major_K()
    output = {
        "type": "PARTIAL-H-JET-JOINT / COUNTING-BOUND",
        "not_claimed": [
            "global f,g shared-coefficient system",
            "the major 4/9 centre or h2 tower",
            "T2,T3 in K[f,g] recurrences",
            "J(f,g)=1 or a polynomial Keller pair",
        ],
        "frozen_input_verification": frozen_input_verification,
        "major_ansatz": {
            "K": "x^11*h(x^-1,w/x)",
            "fixed_face": "w^3*(w-1)^8",
            "strict_filter": "3*r+4*ord_(w-1)>=33",
            "coefficient_count": len(parameters),
            "support": [list(item) for item in support],
        },
        "delta2": delta2_probe(x, w, K, parameters),
        "delta52": delta52_probe(x, w, K, parameters),
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
