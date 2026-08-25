#!/usr/bin/env python3
"""Exact adaptive raw-transport fibres C=0,3 for the TD6 c1 line.

For each requested rational C this rebuilds the 3,602-column two-chart
transport echelon after specialization, pulls back only the six licensed x
bands, and compiles the genuine current t^12 polynomial.  It then reduces
that polynomial through an independently rebuilt adaptive first-band
echelon, retaining and replaying the complete original-row polynomial
certificate.  No previous/pole or current parameterization is used.
"""

from fractions import Fraction as Q
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


cp = load("td6_c1_special_t12_source", SOURCE)
qd, rt, fb = cp.qd, cp.rt, cp.fb
FF = cp.FAST_FIELD
ORIGINAL_QD_STATE = {
    name: getattr(qd, name)
    for name in (
        "Dual", "B", "S", "D", "L", "A", "Q_PRIME", "R", "R3", "R5",
        "POLE_F", "POLE_G",
    )
}


def scalar(value):
    if isinstance(value, cp.FScalar):
        return value.value
    if isinstance(value, cp.fast_efield.EField):
        return value
    return FF.from_frac(cp.Frac.coerce(value))


def polynomial_record(poly):
    canonical = [
        (monomial, cp.reduce_frac_fast(FF.to_frac(scalar(coefficient))))
        for monomial, coefficient in sorted(poly.items()) if coefficient
    ]
    constant = next((coefficient for monomial, coefficient in canonical if not monomial), None)
    return {
        "term_count": len(canonical),
        "parameter_degree": max((len(monomial) for monomial, _ in canonical), default=-1),
        "sha256": sha256(repr(canonical).encode()).hexdigest(),
        "constant": cp.frac_record(constant) if constant is not None else None,
        "parameter_free_nonzero": len(canonical) == 1 and canonical[0][0] == (),
    }


def clean(poly):
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}


def add(poly, other, scale=None):
    scale = FF.one if scale is None else scalar(scale)
    out = dict(poly)
    for monomial, coefficient in other.items():
        value = out.get(monomial, FF.zero) + scale * scalar(coefficient)
        if value:
            out[monomial] = value
        else:
            out.pop(monomial, None)
    return out


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


def linear_polynomial(row, rhs):
    out = {(): -scalar(rhs)} if rhs else {}
    for variable, coefficient in row.items():
        if coefficient:
            out[(variable,)] = scalar(coefficient)
    return out


def divide_by_echelon(polynomial, pivots):
    remainder = dict(polynomial)
    quotients = {}
    normalized = {}
    for count, pivot in enumerate(sorted(pivots), 1):
        row, rhs, _ = pivots[pivot]
        normalized[pivot] = linear_polynomial(row, rhs)
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
            assert iterations < 100000
        if quotient:
            quotients[pivot] = quotient
        if count % 8 == 0:
            print(
                f"special first reduction pivots={count}/{len(pivots)};terms={len(remainder)}",
                flush=True,
            )
    replay = dict(remainder)
    for pivot, quotient in quotients.items():
        replay = add(replay, multiply(quotient, normalized[pivot]))
    assert clean(replay) == clean(polynomial)
    return remainder, quotients


def lift_quotients(quotients, pivots, nrows):
    relations = [{} for _ in range(nrows)]
    for pivot, quotient in quotients.items():
        _, _, combination = pivots[pivot]
        for row_index, coefficient in combination.items():
            relations[row_index] = add(relations[row_index], quotient, scalar(coefficient))
    return relations


def replay_source(polynomial, remainder, relations, rows):
    replay = dict(remainder)
    for relation, (_, row, rhs) in zip(relations, rows):
        if relation:
            replay = add(replay, multiply(relation, linear_polynomial(row, rhs)))
    assert clean(replay) == clean(polynomial)
    canonical = [
        (
            index,
            tuple(
                (monomial, cp.reduce_frac_fast(FF.to_frac(coefficient)))
                for monomial, coefficient in sorted(relation.items())
            ),
        )
        for index, relation in enumerate(relations) if relation
    ]
    return {
        "source_relation_count": len(canonical),
        "source_relation_term_count": sum(len(relation) for _, relation in canonical),
        "source_relation_sha256": sha256(repr(canonical).encode()).hexdigest(),
        "identity": "raw_current_t12 = reduced_t12 + sum(multiplier_i * first_row_i)",
        "source_relations": [
            {
                "row_index": index,
                "key": list(rows[index][0]),
                "terms": [
                    {
                        "monomial": list(monomial),
                        "coefficient": cp.frac_record(coefficient),
                    }
                    for monomial, coefficient in relation
                ],
            }
            for index, relation in canonical
        ],
    }


def compile_current_degree(degree, f1, f2, f3, g1, g2, g3):
    """Exact single-degree specialization of the frozen current compiler."""
    equation = {}
    for i, left in enumerate(f1):
        j = degree - i + 1
        if 1 <= j < len(g2):
            equation = cp.nr.add_polynomial(
                equation,
                cp.nr.multiply_affine(left, cp.nr.scale_affine(g2[j], Q(j))),
            )
    for i, left in enumerate(f2):
        j = degree - i + 1
        if 1 <= j < len(g1):
            equation = cp.nr.add_polynomial(
                equation,
                cp.nr.multiply_affine(left, cp.nr.scale_affine(g1[j], Q(j))),
                Q(2),
            )
    for i, form in enumerate(f3):
        multiplier = qd.Q_PRIME.get(degree - i, cp.FScalar())
        if multiplier:
            equation = cp.nr.add_polynomial(
                equation, cp.nr.affine_polynomial(form), Q(3) * multiplier
            )
    g_degree = degree - 14
    if 0 <= g_degree < len(g3):
        equation = cp.nr.add_polynomial(
            equation, cp.nr.affine_polynomial(g3[g_degree]), Q(-45)
        )
    for i in range(1, len(f1)):
        j = degree - (i - 1)
        if 0 <= j < len(g2):
            equation = cp.nr.add_polynomial(
                equation,
                cp.nr.multiply_affine(cp.nr.scale_affine(f1[i], Q(i)), g2[j]),
                Q(-2),
            )
    for i in range(1, len(f2)):
        j = degree - (i - 1)
        if 0 <= j < len(g1):
            equation = cp.nr.add_polynomial(
                equation,
                cp.nr.multiply_affine(cp.nr.scale_affine(f2[i], Q(i)), g1[j]),
                Q(-1),
            )
    if degree == 0:
        equation = cp.nr.add_polynomial(equation, {(): Q(-1)})
    return equation


def run(value):
    for name, original in ORIGINAL_QD_STATE.items():
        setattr(qd, name, original)
    center = rt.Rat(Q(value))
    fb.CENTER = (center, rt.Rat(1), rt.Rat(1))
    fb._X_POWER_CACHE.clear()
    nf, rows_f = fb.build_transport(
        15, 60, 3, {15: Q(1)}, fb.F1_F_PATTERN, fb.POLE_F_PATTERN
    )
    ng, rows_g = fb.build_transport(
        25, 100, 5, {1: Q(1), 25: Q(1)}, fb.F1_G_PATTERN, fb.POLE_G_PATTERN
    )
    transport = [(('f',) + key, row, rhs) for key, row, rhs in rows_f]
    transport += [
        (('g',) + key, {nf + variable: coefficient for variable, coefficient in row.items()}, rhs)
        for key, row, rhs in rows_g
    ]
    pivots, records, exceptional, selected_minor = rt.factor(transport)
    pivot_rhs, compatibility = cp.propagate(records)
    assert not compatibility
    free = [variable for variable in range(nf + ng) if variable not in pivots]
    free_parameter = {variable: index for index, variable in enumerate(free)}
    print(f"special C={value} transport rank={len(pivots)} free={len(free)}", flush=True)

    bands = {
        (owner, exponent): cp.section_forms(
            15 if owner == "f" else 25,
            60 if owner == "f" else 100,
            exponent,
            16 if owner == "f" else 26,
            0 if owner == "f" else nf,
            pivots, pivot_rhs, free_parameter,
        )
        for owner in ("f", "g") for exponent in (1, 2, 3)
    }
    cp.configure_qd_fast()
    fast_bands = {key: cp.fast_forms(forms) for key, forms in bands.items()}
    raw_t12 = compile_current_degree(
        12,
        *[fast_bands[("f", exponent)] for exponent in (1, 2, 3)],
        *[fast_bands[("g", exponent)] for exponent in (1, 2, 3)],
    )
    raw_t12 = {monomial: scalar(coefficient) for monomial, coefficient in raw_t12.items()}
    t12 = polynomial_record(raw_t12)
    constant_nonzero = t12["parameter_free_nonzero"]

    first_rows = cp.pack_fast(
        "X-2",
        qd.first_band_polynomials(fast_bands[("f", 1)], fast_bands[("g", 1)]),
    )
    first_pivots, first_factors, first_dependent = cp.solve_efield(
        len(free), first_rows, certificates=True
    )
    first_incompatibility = [entry for entry in first_dependent if entry[2]]
    if first_incompatibility:
        reduced_t12 = None
        source_certificate = None
        fibre_empty = True
        first_reason = "first-band affine inconsistency"
    else:
        remainder, quotients = divide_by_echelon(raw_t12, first_pivots)
        relations = lift_quotients(quotients, first_pivots, len(first_rows))
        source_certificate = replay_source(raw_t12, remainder, relations, first_rows)
        reduced_t12 = polynomial_record(remainder)
        fibre_empty = reduced_t12["parameter_free_nonzero"]
        first_reason = "parameter-free nonzero t12 after adaptive first-band reduction" if fibre_empty else None
    print(
        f"special C={value} first rank={len(first_pivots)} empty={fibre_empty}",
        flush=True,
    )
    return {
        "C": str(value),
        "transport_rank": [len(pivots), nf + ng],
        "transport_free_dimension": len(free),
        "transport_compatibility_count": len(compatibility),
        "adaptive_transport_exceptional_factors": dict(exceptional),
        "adaptive_selected_minor": cp.frac_record(cp.lift_rat(selected_minor)),
        "raw_current_t12": t12,
        "raw_current_t12_parameter_free_nonzero": constant_nonzero,
        "adaptive_first_rank": [len(first_pivots), len(free)],
        "adaptive_first_incompatibility_count": len(first_incompatibility),
        "reduced_current_t12": reduced_t12,
        "first_source_certificate": source_certificate,
        "fibre_empty_reason": first_reason,
        "fibre_empty_in_fixed_normalized_scope": fibre_empty,
    }


def main():
    values = [Q(argument) for argument in sys.argv[1:]] or [Q(0), Q(3)]
    assert values and all(value in (Q(0), Q(3)) for value in values)
    results = [run(value) for value in values]
    output = {
        "verdict": "TD6-C1-RAW-TRANSPORT-FIBRES-FIRST-T12-EMPTY",
        "scope": {
            "centers": [f"({value},1,1)" for value in values],
            "adaptive_first_band_echelon_used": True,
            "previous_pole_or_current_parameterizations_used": False,
            "both_global_transport_charts_used": True,
            "fixed_normalized_section_only": True,
            "family_killed": False,
            "SP2_killed": False,
            "JC2_resolved": False,
        },
        "results": results,
        "all_requested_fibres_empty": all(
            result["fibre_empty_in_fixed_normalized_scope"] for result in results
        ),
    }
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
