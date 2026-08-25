#!/usr/bin/env python3
"""Exact full-beta genuine-P12 / staged-N13 unit-syzygy discriminator.

This producer polynomializes the actual 2,893-term genuine P12 compiler,
not the later-echelon row merely keyed X0,t12.  It reduces P12 against the
full polynomial-beta first-J system over E(C,V,U)[beta], lifts the quotient
to the original first rows, and then combines its beta tail with the staged
compatibility N13=(k/25)beta.

The N13 input is separately replayed by the V34 staged producer.  Therefore
this file proves an exact cross-certificate identity on the common generic
open; it does not by itself lift N13 through every transport/previous row or
close any raw center divisor.
"""

from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
N13_PATH = (
    HERE.parent / "td6_c1_c2_c3_q2_n13_v34_20260825" / "replay.py"
)
N13_SHA256 = "1743dc294ca3e3f7f8c1cc1a471d340fc2a1ac7e39d29eddf7e025327578a5c6"
assert sha256(N13_PATH.read_bytes()).hexdigest() == N13_SHA256
spec = importlib.util.spec_from_file_location("td6_full_p12_n13_parent", N13_PATH)
n = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = n
spec.loader.exec_module(n)

STRATUM = n.STRATUM
assert STRATUM in {"h-zero", "b3-param"}
assert sys.argv[1:] == [f"--stratum={STRATUM}"]

r, tri, b = n.r, n.tri, n.b
Rat3, E3, BetaPoly = n.Rat3, n.E3, n.BetaPoly
C, V, U, H, B3 = n.C, n.V, n.U, n.H, n.B3
qd, nr = n.qd, n.nr


def clean(polynomial):
    return {monomial: value for monomial, value in polynomial.items() if value}


def add(left, right, scale=1):
    scale = BetaPoly.coerce(scale)
    out = dict(left)
    for monomial, coefficient in right.items():
        value = out.get(monomial, BetaPoly()) + scale*coefficient
        if value:
            out[monomial] = value
        else:
            out.pop(monomial, None)
    return out


def multiply(left, right):
    out = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(sorted(left_monomial + right_monomial))
            value = (
                out.get(monomial, BetaPoly())
                + left_coefficient*right_coefficient
            )
            if value:
                out[monomial] = value
            else:
                out.pop(monomial, None)
    return out


def scale_polynomial(polynomial, scale):
    scale = BetaPoly.coerce(scale)
    return clean({monomial: scale*coefficient for monomial, coefficient in polynomial.items()})


def projection(polynomial, degree):
    return clean({
        monomial: BetaPoly.coerce(coefficient).coefficient(degree)
        for monomial, coefficient in polynomial.items()
        if BetaPoly.coerce(coefficient).coefficient(degree)
    })


def polynomial_beta_degree(polynomial):
    return max(
        (BetaPoly.coerce(coefficient).degree for coefficient in polynomial.values()),
        default=-1,
    )


def polynomial_digest(polynomial):
    return b.polynomial_digest({
        monomial: E3.coerce(coefficient)
        for monomial, coefficient in polynomial.items()
    })


def divide_polynomial(polynomial, pivots):
    """Reduce a nonlinear polynomial by normalized affine first-row pivots."""
    remainder, quotients = dict(polynomial), {}
    normalized = {
        pivot: n.source_polynomial(row, rhs)
        for pivot, (row, rhs, _) in pivots.items()
    }
    for pivot in sorted(pivots):
        quotient = {}
        while True:
            targets = sorted(
                monomial for monomial, coefficient in remainder.items()
                if coefficient and pivot in monomial
            )
            if not targets:
                break
            monomial = targets[0]
            coefficient = remainder[monomial]
            reduced = list(monomial)
            reduced.remove(pivot)
            multiplier = {tuple(reduced): coefficient}
            quotient = add(quotient, multiplier)
            remainder = add(
                remainder, multiply(multiplier, normalized[pivot]), -1
            )
        if quotient:
            quotients[pivot] = quotient
    replay = dict(remainder)
    for pivot, quotient in quotients.items():
        replay = add(replay, multiply(quotient, normalized[pivot]))
    assert clean(replay) == clean(polynomial)
    return clean(remainder), quotients


def lift_relations(quotients, pivots, nrows):
    relations = [{} for _ in range(nrows)]
    for pivot, quotient in quotients.items():
        _, _, combination = pivots[pivot]
        for row_index, coefficient in combination.items():
            relations[row_index] = add(
                relations[row_index], quotient, coefficient
            )
    return relations


def exact_first_source_replay(polynomial, remainder, relations, first_rows):
    source_identity = {}
    for relation, (_, row, rhs) in zip(relations, first_rows):
        source_identity = add(
            source_identity,
            multiply(relation, n.source_polynomial(row, rhs)),
        )
    target = add(polynomial, remainder, -1)
    assert clean(source_identity) == clean(target)
    assert clean(source_identity) != clean(add(target, {(): BetaPoly(1)}))
    return clean(source_identity)


def beta_tail(polynomial, constant):
    """Certify polynomial = constant + beta*tail, without beta localization."""
    difference = add(polynomial, {(): BetaPoly(constant)}, -1)
    tail = {}
    for monomial, coefficient in difference.items():
        assert not coefficient.constant
        shifted = BetaPoly(coefficient.coefficients[1:])
        if shifted:
            tail[monomial] = shifted
    assert difference == scale_polynomial(tail, BetaPoly.beta())
    return tail


def denominator(values):
    return n.denominator_lcm_beta(list(values))


def main():
    print("beta_parameter_name=beta")
    print("q_beta=t+beta*t^2+t^25")
    print("q_beta_prime=1+2*beta*t+25*t^24")
    center_c, center_v, center_u, center_label = tri.center_coordinates()
    print(f"source_center={center_label}")
    print("source_p_boundary=t^15_fixed")
    print("source_dead_stretch=0_fixed")
    print("source_F1_orbit=frozen")
    print("source_pole_scale_and_data=frozen")
    print(f"raw_center_stratum={STRATUM}")
    print("scope_open=fraction_field_of_printed_raw_stratum")
    print("P12_compiler=genuine_2893_term_source_polynomial")
    print("later_echelon_X0_t12_used=false")
    print("N13_dependency=matching_V34_raw_staged_original_row_replay", flush=True)

    if STRATUM == "b3-param":
        tri.audit_b3_parameterization(center_c, center_v, center_u)
    r.fb.CENTER = (center_c, center_v, center_u)
    r.fb._X_POWER_CACHE.clear()
    nf, rows_f = r.fb.build_transport(
        15, 60, 3, {15: r.b.Q(1)},
        r.fb.F1_F_PATTERN, r.fb.POLE_F_PATTERN,
    )
    ng, rows_g = r.fb.build_transport(
        25, 100, 5, {1: r.b.Q(1), 25: r.b.Q(1)},
        r.fb.F1_G_PATTERN, r.fb.POLE_G_PATTERN,
    )
    rows = [(('f',) + key, row, rhs) for key, row, rhs in rows_f]
    rows += [
        (
            ('g',) + key,
            {nf + variable: coefficient for variable, coefficient in row.items()},
            rhs,
        )
        for key, row, rhs in rows_g
    ]
    ordered = [row for row in rows if row[0][1] != 'X'] + [
        row for row in rows if row[0][1] == 'X'
    ]
    transport_pivots, records, events, _ = tri.factor_transport(ordered)
    pivot_rhs_dual, compatibility = b.propagate_beta(ordered, records)
    assert not compatibility and len(transport_pivots) == 3470
    free = [
        variable for variable in range(nf + ng)
        if variable not in transport_pivots
    ]
    free_parameter = {variable: index for index, variable in enumerate(free)}
    assert len(free) == 132
    print(f"transport_rank={len(transport_pivots)}/{nf+ng}")
    print(f"transport_event_count={len(events)}")
    print("transport_matrix_beta_independent=true")
    print("transport_rhs_beta_affine_exact=true", flush=True)

    def restrict(row):
        return n.convert_form(b.restrict_row_beta(
            row, transport_pivots, pivot_rhs_dual, free_parameter
        ))

    bands = {}
    for owner, imax, jmax, offset in (
        ('f', 15, 60, 0), ('g', 25, 100, nf)
    ):
        for exponent in (1, 2, 3):
            forms = []
            for degree in range(16 if owner == 'f' else 26):
                row = {
                    offset + variable: coefficient
                    for variable, coefficient in r.fb.x_chart_coefficient(
                        imax, jmax, exponent, degree
                    ).items()
                }
                forms.append(restrict(row))
            bands[(owner, exponent)] = forms
    print("transport_three_x_sections_exact=true", flush=True)

    n.configure_qd(direct_qprime=True)
    first_rows = qd.pack(
        'X-2', qd.first_band_polynomials(
            bands[('f', 1)], bands[('g', 1)]
        )
    )
    n.configure_qd(direct_qprime=False)
    first_rows_omit = qd.pack(
        'X-2', qd.first_band_polynomials(
            bands[('f', 1)], bands[('g', 1)]
        )
    )
    assert first_rows_omit != first_rows
    n.configure_qd(direct_qprime=True)
    print("direct_qprime_omission_negative_control=true", flush=True)

    first_pivots, _, first_factors, first_dependent = n.solve_stage(
        132, first_rows, "first_full_beta_P12"
    )
    assert len(first_pivots) == 38
    assert all(not rhs for _, _, rhs, _ in first_dependent)

    raw = qd.compile_current(
        *[bands[('f', exponent)] for exponent in (1, 2, 3)],
        *[bands[('g', exponent)] for exponent in (1, 2, 3)],
    )[12]
    polynomial = clean({
        monomial: BetaPoly.coerce(coefficient)
        for monomial, coefficient in raw.items()
    })
    raw_base = projection(polynomial, 0)
    assert raw_base
    print(f"raw_P12_term_count={len(polynomial)}")
    print(f"raw_P12_beta_degree={polynomial_beta_degree(polynomial)}")
    print(f"raw_P12_base_terms={len(raw_base)}")
    print(f"raw_P12_base_sha256={polynomial_digest(raw_base)}", flush=True)

    remainder, quotients = divide_polynomial(polynomial, first_pivots)
    relations = lift_relations(quotients, first_pivots, len(first_rows))
    first_source_identity = exact_first_source_replay(
        polynomial, remainder, relations, first_rows
    )
    S = E3(qd.uniform.S_FIELD)
    k = E3(252) - 342*S + 144*S**2 - 36*S**3
    expected = -k/50
    assert projection(remainder, 0) == {(): expected}
    tail = beta_tail(remainder, expected)
    assert tail
    print(f"remainder_term_count={len(remainder)}")
    print(f"remainder_beta_degree={polynomial_beta_degree(remainder)}")
    print(f"remainder_base_is_minus_k_over_50=true")
    print(f"remainder_beta_tail_terms={len(tail)}")
    print(f"remainder_beta_tail_degree={polynomial_beta_degree(tail)}")
    print(f"remainder_beta_tail_sha256={n.digest(tail)}")
    print("full_beta_first_original_row_replay=true", flush=True)

    n13 = BetaPoly([0, k/25])
    n13_multiplier = scale_polynomial(tail, E3(25)/k)
    n13_contribution = scale_polynomial(n13_multiplier, n13)
    target = add(polynomial, {(): BetaPoly(expected)}, -1)
    combined = add(first_source_identity, n13_contribution)
    assert clean(combined) == clean(target)
    assert clean(first_source_identity) != clean(target)
    assert n13_contribution == scale_polynomial(tail, BetaPoly.beta())
    print(f"N13_exact_value_sha256={n.digest(n13)}")
    print(f"N13_multiplier_terms={len(n13_multiplier)}")
    print(f"N13_multiplier_beta_degree={polynomial_beta_degree(n13_multiplier)}")
    print(f"N13_multiplier_sha256={n.digest(n13_multiplier)}")
    print("P12_N13_polynomial_unit_identity_exact=true")
    print("P12_without_N13_negative_control=true")
    print("beta_division_used=false")
    print("combined_unit_residual_is_minus_k_over_50=true", flush=True)

    relation_values = [
        coefficient for relation in relations for coefficient in relation.values()
    ]
    first_values = [
        coefficient
        for _, row, rhs in first_rows
        for coefficient in list(row.values()) + [rhs]
    ]
    termwise_values = []
    termwise_slots = 0
    for relation, (_, row, rhs) in zip(relations, first_rows):
        source = n.source_polynomial(row, rhs)
        for multiplier in relation.values():
            for source_value in source.values():
                termwise_values.append(multiplier*source_value)
                termwise_slots += 1
    denominators = {
        "raw_P12": denominator(polynomial.values()),
        "first_rows": denominator(first_values),
        "first_relations": denominator(relation_values),
        "termwise_source": denominator(termwise_values),
        "N13_multiplier": denominator(n13_multiplier.values()),
    }
    for name, value in denominators.items():
        print(f"{name}_denominator=({value})")
        print(f"{name}_denominator_factor={value.factor()}")
        print(f"{name}_denominator_summary={tri.polynomial_summary(value)}")
    print(f"termwise_source_slot_count={termwise_slots}")
    print("all_raw_denominator_factors_emitted=true")
    print("termwise_polynomial_source_clearing_exact=true")
    print(f"first_source_nonzero_rows={sum(bool(relation) for relation in relations)}")
    print(f"first_source_multiplier_terms={sum(len(relation) for relation in relations)}")
    print("raw_fraction_field_full_beta_family_empty=true")
    print("N13_full_source_lift_in_this_file=false")
    print("every_emitted_raw_denominator_divisor_still_charged=true")
    print("full_A3_beta_family_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-A3-Q2-FULL-P12-N13-UNIT-RAW PASS")


if __name__ == "__main__":
    main()
