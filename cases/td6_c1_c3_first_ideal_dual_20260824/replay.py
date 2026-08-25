#!/usr/bin/env python3
"""Exact first-ideal dc3 discriminator along the full nonlinear c1 line.

This is deliberately smaller than the live all-current dual calculation.  It
retains the genuine quadratic current t^12 polynomial in all 132 transport
parameters and reduces it through the *varying* original first-band linear
ideal over E(C)[eps]/eps^2.  Differentiating the echelon itself retains the
lambda-prime contribution.  The result is sensitivity/projective-escape data,
not bivariate coverage or a family theorem.
"""

from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "c1_c3_thickening.py"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


m = load("td6_c1_c3_dual_source_for_first_ideal", SOURCE)
cp, qd, rt, fb = m.cp, m.qd, m.rt, m.fb
FPair = m.FPair
ZERO, ONE = m.FAST_FIELD.zero, m.FAST_FIELD.one


def clean(poly):
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}


def add(left, right, scale=None):
    scale = FPair(ONE, ZERO) if scale is None else FPair.coerce(scale)
    out = dict(left)
    for monomial, coefficient in right.items():
        value = out.get(monomial, FPair()) + scale * FPair.coerce(coefficient)
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
                out.get(monomial, FPair())
                + FPair.coerce(coefficient_left) * FPair.coerce(coefficient_right)
            )
            if value:
                out[monomial] = value
            else:
                out.pop(monomial, None)
    return out


def source_polynomial(row, rhs):
    out = {(): -FPair.from_edual(rhs)} if rhs else {}
    for variable, coefficient in row.items():
        coefficient = FPair.from_edual(coefficient)
        if coefficient:
            out[(variable,)] = coefficient
    return out


def divide(polynomial, pivots):
    remainder = dict(polynomial)
    quotients = {}
    normalized = {}
    for pivot in sorted(pivots):
        row, rhs, _ = pivots[pivot]
        normalized[pivot] = source_polynomial(row, rhs)
        assert normalized[pivot][(pivot,)] == FPair(ONE, ZERO)
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
            remainder = add(remainder, multiply(multiplier, normalized[pivot]), FPair(-ONE, ZERO))
            iterations += 1
            assert iterations < 100000
        if quotient:
            quotients[pivot] = quotient
    replay = dict(remainder)
    for pivot, quotient in quotients.items():
        replay = add(replay, multiply(quotient, normalized[pivot]))
    assert clean(replay) == clean(polynomial)
    return remainder, quotients


def lift_relations(quotients, pivots, nrows):
    relations = [{} for _ in range(nrows)]
    for pivot, quotient in quotients.items():
        _, _, combination = pivots[pivot]
        assert combination is not None
        for row_index, coefficient in combination.items():
            relations[row_index] = add(
                relations[row_index], quotient, FPair.coerce(coefficient)
            )
    return relations


def replay_source(polynomial, remainder, relations, rows):
    replay = dict(remainder)
    for relation, (_, row, rhs) in zip(relations, rows):
        if relation:
            replay = add(replay, multiply(relation, source_polynomial(row, rhs)))
    assert clean(replay) == clean(polynomial)


def pair_digest(poly):
    payload = tuple(
        (monomial, repr(value.value), repr(value.derivative))
        for monomial, value in sorted(poly.items())
    )
    return sha256(repr(payload).encode()).hexdigest()


def component(poly, derivative=False):
    return {
        monomial: (value.derivative if derivative else value.value)
        for monomial, value in poly.items()
        if (value.derivative if derivative else value.value)
    }


def field_record(value):
    return cp.frac_record(
        cp.reduce_frac_fast(m.FAST_FIELD.to_frac(value))
    )


def component_record(poly):
    degrees = [len(monomial) for monomial in poly]
    preview = []
    for monomial, value in sorted(poly.items())[:12]:
        preview.append({"monomial": list(monomial), "coefficient": field_record(value)})
    return {
        "term_count": len(poly),
        "parameter_degree": max(degrees, default=-1),
        "sha256": sha256(
            repr(tuple((monomial, repr(value)) for monomial, value in sorted(poly.items()))).encode()
        ).hexdigest(),
        "preview": preview,
    }


def main():
    Cq = rt.Rat(rt.X)
    fb.CENTER = (m.QDual(Cq), m.QDual(1), m.QDual(1, 1))
    fb._X_POWER_CACHE.clear()
    nf, rows_f = fb.build_transport(
        15, 60, 3, {15: m.Q(1)}, fb.F1_F_PATTERN, fb.POLE_F_PATTERN
    )
    ng, rows_g = fb.build_transport(
        25, 100, 5, {1: m.Q(1), 25: m.Q(1)}, fb.F1_G_PATTERN, fb.POLE_G_PATTERN
    )
    transport = [(('f',) + key, row, rhs) for key, row, rhs in rows_f]
    transport += [
        (('g',) + key, {nf + variable: coefficient for variable, coefficient in row.items()}, rhs)
        for key, row, rhs in rows_g
    ]
    data = m.factor_transport(transport)
    pivot_rhs, compatibility = m.propagate(data["records"])
    assert not compatibility and len(data["pivots"]) == 3470
    free = [variable for variable in range(nf + ng) if variable not in data["pivots"]]
    free_parameter = {variable: index for index, variable in enumerate(free)}
    assert len(free) == 132
    print("first-ideal dual transport PASS", flush=True)

    bands132 = {
        (owner, exponent): m.section_forms(
            15 if owner == "f" else 25,
            60 if owner == "f" else 100,
            exponent,
            16 if owner == "f" else 26,
            0 if owner == "f" else nf,
            data["pivots"], pivot_rhs, free_parameter,
        )
        for owner in ("f", "g") for exponent in (1, 2, 3)
    }
    m.configure_qd()
    first_rows = qd.pack(
        "X-2", qd.first_band_polynomials(bands132[("f", 1)], bands132[("g", 1)])
    )
    first_pivots, first_factors, dependent = m.solve(132, first_rows, certificates=True)
    assert len(first_pivots) == 38
    assert all(not residual for _, _, residual, _ in dependent)
    first_pivot_dc3_count = sum(bool(lead.derivative) for _, _, _, lead in first_factors)
    assert first_pivot_dc3_count > 0, "negative control: first matrix was frozen"
    print("first-ideal dual first echelon PASS", flush=True)

    fast_bands132 = {key: m.fast_forms(forms) for key, forms in bands132.items()}
    m.configure_qd_fast()
    raw_current132 = qd.compile_current(
        *[fast_bands132[("f", exponent)] for exponent in (1, 2, 3)],
        *[fast_bands132[("g", exponent)] for exponent in (1, 2, 3)],
    )
    polynomial = {
        monomial: FPair.coerce(coefficient)
        for monomial, coefficient in raw_current132[12].items()
        if coefficient
    }
    assert max(map(len, polynomial)) == 2
    raw_dc3 = component(polynomial, derivative=True)
    assert raw_dc3, "negative control: raw P12 coefficient variation was omitted"
    remainder, quotients = divide(polynomial, first_pivots)
    relations = lift_relations(quotients, first_pivots, len(first_rows))
    replay_source(polynomial, remainder, relations, first_rows)
    base, dc3 = component(remainder), component(remainder, derivative=True)
    assert set(base).issubset({()}) and base.get(())
    print("first-ideal dual reduction/source replay PASS", flush=True)

    output = {
        "verdict": "TD6-C1-C3-FIRST-IDEAL-DUAL-DISCRIMINATOR",
        "scope": {
            "line": "(c1,c2,c3)=(C,1,1)",
            "direction": "dc3",
            "ring": "E(C)[eps]/eps^2",
            "full_bivariate_coverage": False,
            "projective_escape_theorem": False,
            "SP2_killed": False,
            "JC2_resolved": False,
        },
        "ranks": {"transport": [3470, nf + ng], "first": [38, 132]},
        "raw_t12": {
            "term_count": len(polynomial),
            "parameter_degree": max(map(len, polynomial)),
            "pair_sha256": pair_digest(polynomial),
        },
        "negative_control": {
            "raw_t12_dc3": component_record(raw_dc3),
            "first_pivot_dc3_nonzero_count": first_pivot_dc3_count,
            "omitted_coefficient_variation_detected": True,
        },
        "remainder": {
            "pair_sha256": pair_digest(remainder),
            "base": component_record(base),
            "dc3": component_record(dc3),
            "dc3_has_free_parameter_terms": any(monomial for monomial in dc3),
        },
        "source_lift": {
            "nonzero_original_first_rows": sum(bool(relation) for relation in relations),
            "multiplier_terms": sum(len(relation) for relation in relations),
            "pair_sha256": sha256(
                repr(tuple(
                    tuple((monomial, repr(value.value), repr(value.derivative))
                          for monomial, value in sorted(relation.items()))
                    for relation in relations
                )).encode()
            ).hexdigest(),
        },
        "first_pivot_count": len(first_factors),
        "family_killed": False,
    }
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
