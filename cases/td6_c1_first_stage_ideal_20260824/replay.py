#!/usr/bin/env python3
"""Lift the TD6 c1 current obstruction through the first-stage ideal.

This is deliberately not the rejected all-stage affine model.  The current
row is kept as its genuine sparse polynomial in the 94 first-stage
parameters.  We divide that polynomial by the exact normalized linear
previous/pole echelon, retain polynomial quotient multipliers, lift those
multipliers back to the original previous/pole rows, clear only C-denominators,
and replay the resulting polynomial-ideal identity exactly.

The output is a discriminator on the generic transport+first chart.  It
retains both the previous-stage checkpoint and the stronger lift through the
original first-band ideal.  The emitted gcd data isolates, but does not solve,
the remaining first-stage exceptional cubic.  Raw-transport exceptional
fibres are handled by a separate adaptive certificate.
"""

from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


PRIVATE = Path(__file__).resolve().parent
SOURCE = PRIVATE / "c1_pencil.py"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


cp = load("td6_c1_previous_ideal_source", SOURCE)
qd, rt, fb, nr = cp.qd, cp.rt, cp.fb, cp.nr
FF = cp.FAST_FIELD


def scalar(value):
    if isinstance(value, cp.FScalar):
        return value.value
    if isinstance(value, cp.fast_efield.EField):
        assert value.factory is FF
        return value
    return FF.from_frac(cp.Frac.coerce(value))


def clean(poly):
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}


def add(left, right, scale=None):
    scale = FF.one if scale is None else scalar(scale)
    out = dict(left)
    for monomial, coefficient in right.items():
        value = out.get(monomial, FF.zero) + scale * scalar(coefficient)
        if value:
            out[monomial] = value
        else:
            out.pop(monomial, None)
    return out


def scale(poly, coefficient):
    coefficient = scalar(coefficient)
    if not coefficient:
        return {}
    return clean({monomial: coefficient * scalar(value) for monomial, value in poly.items()})


def multiply(left, right):
    out = {}
    for monomial_left, coefficient_left in left.items():
        for monomial_right, coefficient_right in right.items():
            monomial = tuple(sorted(monomial_left + monomial_right))
            value = (
                out.get(monomial, FF.zero)
                + scalar(coefficient_left) * scalar(coefficient_right)
            )
            if value:
                out[monomial] = value
            else:
                out.pop(monomial, None)
    return out


def source_linear_polynomial(row, rhs):
    out = {(): -scalar(rhs)} if rhs else {}
    for variable, coefficient in row.items():
        value = scalar(coefficient)
        if value:
            out[(variable,)] = value
    return out


def canonical_poly(poly):
    return tuple(
        (monomial, cp.reduce_frac_fast(FF.to_frac(coefficient)))
        for monomial, coefficient in sorted(poly.items())
    )


def poly_sha(poly):
    return sha256(repr(canonical_poly(poly)).encode()).hexdigest()


def forms_from_pivots(nvariables, pivots):
    free = [variable for variable in range(nvariables) if variable not in pivots]
    parameter_of = {variable: index for index, variable in enumerate(free)}
    forms = [None] * nvariables
    for variable in reversed(range(nvariables)):
        if variable in parameter_of:
            forms[variable] = (FF.zero, {parameter_of[variable]: FF.one})
            continue
        row, rhs, _ = pivots[variable]
        constant = rhs
        coefficients = {}
        for other, coefficient in row.items():
            if other == variable:
                continue
            inner_constant, inner_coefficients = forms[other]
            constant -= coefficient * inner_constant
            for parameter, inner_coefficient in inner_coefficients.items():
                value = (
                    coefficients.get(parameter, FF.zero)
                    - coefficient * inner_coefficient
                )
                if value:
                    coefficients[parameter] = value
                else:
                    coefficients.pop(parameter, None)
        forms[variable] = (constant, coefficients)
    return [
        (
            FF.to_frac(constant),
            {parameter: FF.to_frac(coefficient) for parameter, coefficient in coefficients.items()},
        )
        for constant, coefficients in forms
    ], free


def replay_affine(rows, forms):
    field_forms = [
        (
            scalar(constant),
            {parameter: scalar(coefficient) for parameter, coefficient in coefficients.items()},
        )
        for constant, coefficients in forms
    ]
    for key, row, rhs in rows:
        constant = FF.zero
        coefficients = {}
        for variable, coefficient in row.items():
            coefficient = scalar(coefficient)
            inner_constant, inner_coefficients = field_forms[variable]
            constant += coefficient * inner_constant
            for parameter, inner_coefficient in inner_coefficients.items():
                value = (
                    coefficients.get(parameter, FF.zero)
                    + coefficient * inner_coefficient
                )
                if value:
                    coefficients[parameter] = value
                else:
                    coefficients.pop(parameter, None)
        assert constant == scalar(rhs), ("affine constant replay", key)
        assert not coefficients, ("affine direction replay", key)


def divide_by_linear_echelon(polynomial, pivots):
    """Return remainder and Q_p with P=rem+sum Q_p*G_p exactly."""
    remainder = dict(polynomial)
    quotients = {}
    normalized = {}
    for pivot in sorted(pivots):
        row, rhs, _ = pivots[pivot]
        normalized[pivot] = source_linear_polynomial(row, rhs)
        assert normalized[pivot][(pivot,)] == FF.one
        quotient = {}
        iterations = 0
        while True:
            targets = sorted(monomial for monomial in remainder if pivot in monomial)
            if not targets:
                break
            monomial = targets[0]
            coefficient = remainder[monomial]
            reduced = list(monomial)
            reduced.remove(pivot)
            multiplier = {tuple(reduced): coefficient}
            quotient = add(quotient, multiplier)
            remainder = add(remainder, multiply(multiplier, normalized[pivot]), -FF.one)
            iterations += 1
            assert iterations < 100000, ("division did not terminate", pivot)
        if quotient:
            quotients[pivot] = quotient
    replay = dict(remainder)
    for pivot, quotient in quotients.items():
        replay = add(replay, multiply(quotient, normalized[pivot]))
    assert clean(replay) == clean(polynomial), "normalized-echelon polynomial replay"
    return remainder, quotients, normalized


def lift_to_source_relations(quotients, pivots, nrows):
    relations = [{} for _ in range(nrows)]
    for pivot, quotient in quotients.items():
        _, _, combination = pivots[pivot]
        assert combination is not None
        for row_index, coefficient in combination.items():
            relations[row_index] = add(relations[row_index], quotient, scalar(coefficient))
    return relations


def replay_source_identity(polynomial, remainder, relations, rows):
    replay = dict(remainder)
    for relation, (_, row, rhs) in zip(relations, rows):
        if relation:
            replay = add(replay, multiply(relation, source_linear_polynomial(row, rhs)))
    assert clean(replay) == clean(polynomial), "original-row polynomial replay"


def all_coefficients(polynomials):
    for polynomial in polynomials:
        for coefficient in polynomial.values():
            yield cp.reduce_frac_fast(FF.to_frac(coefficient))


def clear_denominators(polynomial, remainder, relations, rows):
    values = list(all_coefficients([remainder] + relations))
    common = cp.ONE_POLY
    for value in values:
        common = cp.poly_lcm_fast(common, value.denominator)

    def cleared(source):
        out = {}
        for monomial, coefficient in source.items():
            value = cp.reduce_frac_fast(FF.to_frac(coefficient))
            out[monomial] = value.numerator * cp.poly_exact_div(
                common, value.denominator
            )
        return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}

    cleared_remainder = cleared(remainder)
    cleared_relations = [cleared(relation) for relation in relations]
    content = common
    for source in [cleared_remainder] + cleared_relations:
        for coefficient in source.values():
            content = cp.poly_gcd_fast(content, coefficient)
            if content.degree == 0:
                break
        if content.degree == 0:
            break
    content = cp.poly_monic(content)
    primitive_p = cp.poly_exact_div(common, content)

    def primitive(source):
        return {
            monomial: cp.poly_exact_div(coefficient, content)
            for monomial, coefficient in source.items()
        }

    primitive_remainder = primitive(cleared_remainder)
    primitive_relations = [primitive(relation) for relation in cleared_relations]

    # Replay the primitive E[C]-identity after embedding into E(C).
    embedded_p = FF.from_frac(cp.Frac(primitive_p))
    left = scale(polynomial, embedded_p)
    right = {
        monomial: FF.from_frac(cp.Frac(coefficient))
        for monomial, coefficient in primitive_remainder.items()
    }
    for relation, (_, row, rhs) in zip(primitive_relations, rows):
        embedded_relation = {
            monomial: FF.from_frac(cp.Frac(coefficient))
            for monomial, coefficient in relation.items()
        }
        right = add(right, multiply(embedded_relation, source_linear_polynomial(row, rhs)))
    assert clean(left) == clean(right), "primitive E[C] identity replay"
    return {
        "common_denominator": common,
        "content": content,
        "p_coefficient": primitive_p,
        "remainder": primitive_remainder,
        "relations": primitive_relations,
    }


def polynomial_record(polynomial):
    return {
        "term_count": len(polynomial),
        "parameter_degree": max((len(monomial) for monomial in polynomial), default=-1),
        "sha256": sha256(
            repr(sorted((monomial, cp.poly_record(coefficient)) for monomial, coefficient in polynomial.items())).encode()
        ).hexdigest(),
        "coefficients": [
            {"monomial": list(monomial), "coefficient": cp.poly_record(coefficient)}
            for monomial, coefficient in sorted(polynomial.items())
        ],
    }


def main():
    Cq = rt.Rat(rt.X)
    fb.CENTER = (Cq, rt.Rat(1), rt.Rat(1))
    fb._X_POWER_CACHE.clear()
    nf, rows_f = fb.build_transport(
        15, 60, 3, {15: cp.Q(1)}, fb.F1_F_PATTERN, fb.POLE_F_PATTERN
    )
    ng, rows_g = fb.build_transport(
        25, 100, 5, {1: cp.Q(1), 25: cp.Q(1)}, fb.F1_G_PATTERN, fb.POLE_G_PATTERN
    )
    transport = [(('f',) + key, row, rhs) for key, row, rhs in rows_f]
    transport += [
        (('g',) + key, {nf + variable: coefficient for variable, coefficient in row.items()}, rhs)
        for key, row, rhs in rows_g
    ]
    transport_pivots, transport_records, transport_exceptional, _ = rt.factor(transport)
    pivot_rhs, compatibility = cp.propagate(transport_records)
    assert not compatibility and len(transport_pivots) == 3470
    free = [variable for variable in range(nf + ng) if variable not in transport_pivots]
    free_parameter = {variable: index for index, variable in enumerate(free)}
    assert len(free) == 132
    print("ideal transport PASS", flush=True)

    bands132 = {
        (owner, exponent): cp.section_forms(
            15 if owner == "f" else 25,
            60 if owner == "f" else 100,
            exponent,
            16 if owner == "f" else 26,
            0 if owner == "f" else nf,
            transport_pivots, pivot_rhs, free_parameter,
        )
        for owner in ("f", "g") for exponent in (1, 2, 3)
    }
    pole_f132 = cp.pole_forms(15, 60, -2, 61, 0, transport_pivots, pivot_rhs, free_parameter)
    pole_g132 = cp.pole_forms(25, 100, -4, 101, nf, transport_pivots, pivot_rhs, free_parameter)
    print("ideal transport sections PASS", flush=True)

    cp.configure_qd()
    first_rows = qd.pack(
        "X-2", qd.first_band_polynomials(bands132[("f", 1)], bands132[("g", 1)])
    )
    forms94, free94, factors_first = cp.parameterize_qmatrix(132, first_rows)
    assert (len(factors_first), len(free94)) == (38, 94)
    print("ideal first PASS", flush=True)

    bands94 = {key: cp.compose(forms, forms94) for key, forms in bands132.items()}
    pole_f94 = cp.compose(pole_f132, forms94)
    pole_g94 = cp.compose(pole_g132, forms94)
    cp.configure_qd_fast()
    fast_bands94 = {key: cp.fast_forms(forms) for key, forms in bands94.items()}
    previous_rows = cp.pack_fast(
        "X-1",
        qd.compile_previous(
            fast_bands94[("f", 1)], fast_bands94[("f", 2)],
            fast_bands94[("g", 1)], fast_bands94[("g", 2)],
        ),
    )
    previous_rows += cp.pack_fast(
        "P1", qd.compile_pole_previous(cp.fast_forms(pole_f94), cp.fast_forms(pole_g94))
    )
    previous_pivots, factors_previous, dependent = cp.solve_efield(
        94, previous_rows, certificates=True
    )
    assert len(previous_pivots) == 38
    assert all(not residual for _, _, residual, _ in dependent)
    forms56, free56 = forms_from_pivots(94, previous_pivots)
    assert len(free56) == 56
    replay_affine(previous_rows, forms56)
    print("ideal previous affine/certificates PASS", flush=True)

    raw_current = qd.compile_current(
        *[fast_bands94[("f", exponent)] for exponent in (1, 2, 3)],
        *[fast_bands94[("g", exponent)] for exponent in (1, 2, 3)],
    )
    polynomial = {monomial: scalar(coefficient) for monomial, coefficient in raw_current[12].items()}
    # The all-stage 132-variable system is genuinely nonlinear, but this
    # particular current row may simplify to affine after the licensed first
    # substitution.  Record the actual degree; do not impose one.
    assert polynomial
    remainder, quotients, _ = divide_by_linear_echelon(polynomial, previous_pivots)
    relations = lift_to_source_relations(quotients, previous_pivots, len(previous_rows))
    replay_source_identity(polynomial, remainder, relations, previous_rows)
    assert set(remainder).issubset({()}), ("unexpected free-parameter remainder", remainder.keys())
    assert remainder.get((), FF.zero), "expected nonzero current obstruction"
    exact = clear_denominators(polynomial, remainder, relations, previous_rows)
    print("ideal nonlinear lift/clear/replay PASS", flush=True)

    # Lift the same exact row one stage farther.  Here the raw current row is
    # retained as its genuine polynomial in all 132 transport-free variables;
    # only the licensed first-band linear ideal is used for reduction.
    fast_bands132 = {key: cp.fast_forms(forms) for key, forms in bands132.items()}
    raw_current132 = qd.compile_current(
        *[fast_bands132[("f", exponent)] for exponent in (1, 2, 3)],
        *[fast_bands132[("g", exponent)] for exponent in (1, 2, 3)],
    )
    polynomial132 = {
        monomial: scalar(coefficient)
        for monomial, coefficient in raw_current132[12].items()
    }
    first_pivots, first_field_factors, first_dependent = cp.solve_efield(
        132, first_rows, certificates=True
    )
    assert len(first_pivots) == 38
    assert all(not residual for _, _, residual, _ in first_dependent)
    remainder132, quotients132, _ = divide_by_linear_echelon(
        polynomial132, first_pivots
    )
    relations132 = lift_to_source_relations(
        quotients132, first_pivots, len(first_rows)
    )
    replay_source_identity(polynomial132, remainder132, relations132, first_rows)
    assert set(remainder132).issubset({()})
    assert remainder132.get((), FF.zero)
    exact_first = clear_denominators(
        polynomial132, remainder132, relations132, first_rows
    )
    assert cp.reduce_frac_fast(FF.to_frac(remainder132[()])) == cp.reduce_frac_fast(
        FF.to_frac(remainder[()])
    )
    print("ideal first-stage nonlinear lift/clear/replay PASS", flush=True)

    previous_numerators = []
    seen = set()
    for _, _, _, lead in factors_previous:
        numerator = cp.reduce_frac_fast(lead).numerator
        if numerator.degree <= 0 or repr(numerator) in seen:
            continue
        seen.add(repr(numerator))
        previous_numerators.append(numerator)
    rhs = exact["remainder"][()]
    factor_gcds = [cp.poly_gcd_fast(rhs, numerator) for numerator in previous_numerators]
    first_numerators = []
    seen = set()
    for _, _, _, lead in first_field_factors:
        numerator = cp.reduce_frac_fast(lead).numerator
        if numerator.degree <= 0 or repr(numerator) in seen:
            continue
        seen.add(repr(numerator))
        first_numerators.append(numerator)
    first_rhs = exact_first["remainder"][()]
    first_factor_gcds = [
        cp.poly_gcd_fast(first_rhs, numerator) for numerator in first_numerators
    ]
    output = {
        "verdict": "TD6-C1-FIRST-STAGE-LOCALIZED-IDEAL-CERTIFICATE",
        "scope": {
            "transport_chart": "C*(C-3)!=0",
            "first_stage_chart": (
                "(C-3)*(4*C^3+8*C^2-59*C-3)!=0; on the transport chart, "
                "4*C^3+8*C^2-59*C-3!=0"
            ),
            "previous_pivot_roots_covered": all(gcd.degree == 0 for gcd in factor_gcds),
            "first_pivot_roots_covered": all(gcd.degree == 0 for gcd in first_factor_gcds),
            "remaining_first_exceptional_stratum": "4*C^3+8*C^2-59*C-3=0",
            "transport_exceptional_fibres_covered": False,
            "affine_all_stage_assumption_used": False,
            "family_killed": False,
            "SP2_killed": False,
            "JC2_resolved": False,
        },
        "ranks": {
            "transport": [len(transport_pivots), nf + ng],
            "first": [len(factors_first), 132],
            "previous_pole": [len(previous_pivots), 94],
        },
        "raw_current_t12": {
            "term_count": len(polynomial),
            "parameter_degree": max(map(len, polynomial), default=-1),
            "sha256": poly_sha(polynomial),
        },
        "raw_current_t12_before_first": {
            "term_count": len(polynomial132),
            "parameter_degree": max(map(len, polynomial132), default=-1),
            "sha256": poly_sha(polynomial132),
        },
        "reduction": {
            "normalized_quotient_count": len(quotients),
            "source_relation_count": sum(bool(relation) for relation in relations),
            "source_relation_term_count": sum(len(relation) for relation in relations),
            "rational_remainder": cp.frac_record(FF.to_frac(remainder[()])),
        },
        "cleared_identity": {
            "common_denominator": cp.poly_record(exact["common_denominator"]),
            "removed_content": cp.poly_record(exact["content"]),
            "current_row_coefficient": cp.poly_record(exact["p_coefficient"]),
            "rhs": cp.poly_record(rhs),
            "relations": [
                {"row_index": index, "key": list(previous_rows[index][0]), **polynomial_record(relation)}
                for index, relation in enumerate(exact["relations"]) if relation
            ],
            "identity_sha256": sha256(
                repr((
                    exact["p_coefficient"],
                    sorted(exact["remainder"].items()),
                    [sorted(relation.items()) for relation in exact["relations"]],
                )).encode()
            ).hexdigest(),
        },
        "previous_exceptional": {
            "distinct_pivot_numerator_count": len(previous_numerators),
            "pivot_numerators": [cp.poly_record(value) for value in previous_numerators],
            "rhs_gcds": [cp.poly_record(value) for value in factor_gcds],
        },
        "first_stage_cleared_identity": {
            "common_denominator": cp.poly_record(exact_first["common_denominator"]),
            "removed_content": cp.poly_record(exact_first["content"]),
            "current_row_coefficient": cp.poly_record(exact_first["p_coefficient"]),
            "rhs": cp.poly_record(first_rhs),
            "relations": [
                {"row_index": index, "key": list(first_rows[index][0]), **polynomial_record(relation)}
                for index, relation in enumerate(exact_first["relations"]) if relation
            ],
            "identity_sha256": sha256(
                repr((
                    exact_first["p_coefficient"],
                    sorted(exact_first["remainder"].items()),
                    [sorted(relation.items()) for relation in exact_first["relations"]],
                )).encode()
            ).hexdigest(),
        },
        "first_exceptional": {
            "distinct_pivot_numerator_count": len(first_numerators),
            "pivot_numerators": [cp.poly_record(value) for value in first_numerators],
            "rhs_gcds": [cp.poly_record(value) for value in first_factor_gcds],
        },
    }
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
