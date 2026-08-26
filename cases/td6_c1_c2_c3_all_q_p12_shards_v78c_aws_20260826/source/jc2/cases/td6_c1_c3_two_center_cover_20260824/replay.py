#!/usr/bin/env python3
"""Generic exact P12 reduction over E(C,U), dependency-complete prototype."""

from hashlib import sha256
import importlib.util
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
REVERSE_PIVOTS = "--reverse-pivots" in sys.argv
SPARSE_PIVOTS = "--sparse-pivots" in sys.argv
B_LOCAL_PIVOTS = "--b-local-pivots" in sys.argv
STRATUM = next(
    (argument.split("=", 1)[1] for argument in sys.argv if argument.startswith("--stratum=")),
    "generic",
)
SOURCE = HERE / "first_c1_c3_mpoly.py"
spec = importlib.util.spec_from_file_location("td6_c1_c3_first_for_p12", SOURCE)
b = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules["td6_c1_c3_first_for_p12"] = b
spec.loader.exec_module(b)
t, cp, fb, qd, E2 = b.t, b.cp, b.fb, b.qd, b.E2
B_POLY = (
    4*t.C**2*t.U**2 + 24*t.C*t.U**4 - 4*t.C*t.U
    + 20*t.U**6 - 20*t.U**3 + 1
)
B_H_RESULTANT = 128*t.U**6 - 32*t.U**3 + 1


def clean(poly):
    return {monomial: value for monomial, value in poly.items() if value}


def add(left, right, scale=None):
    scale = E2(1) if scale is None else E2.coerce(scale)
    out = dict(left)
    for monomial, coefficient in right.items():
        value = out.get(monomial, E2()) + scale * coefficient
        if value:
            out[monomial] = value
        else:
            out.pop(monomial, None)
    return out


def multiply(left, right):
    out = {}
    for ml, cl in left.items():
        for mr, cr in right.items():
            monomial = tuple(sorted(ml + mr))
            value = out.get(monomial, E2()) + cl * cr
            if value:
                out[monomial] = value
            else:
                out.pop(monomial, None)
    return out


def source_polynomial(row, rhs):
    out = {(): -E2.coerce(rhs)} if rhs else {}
    for variable, coefficient in row.items():
        coefficient = E2.coerce(coefficient)
        if coefficient:
            out[(variable,)] = coefficient
    return out


def scalar_coordinate(value):
    coordinates = scalar_coordinates(value)
    nonzero = [coordinate for coordinate in coordinates if coordinate]
    return nonzero[0] if len(nonzero) == 1 else None


def choose_new_pivot(row):
    if REVERSE_PIVOTS:
        return max(row)
    if not SPARSE_PIVOTS and not B_LOCAL_PIVOTS:
        return min(row)
    candidates = []
    for variable, coefficient in row.items():
        coordinate = scalar_coordinate(coefficient)
        if coordinate is None:
            continue
        b_residual_degree = 0
        if B_LOCAL_PIVOTS:
            resultant = B_POLY.resultant(coordinate.numerator, 0)
            if not resultant:
                b_residual_degree = 10**9
            else:
                _, factors = resultant.factor()
                b_residual_degree = sum(
                    factor.total_degree() * multiplicity
                    for factor, multiplicity in factors
                    if factor != t.U and factor != B_H_RESULTANT
                )
        candidates.append((
            b_residual_degree,
            coordinate.numerator.total_degree(),
            coordinate.denominator.total_degree(),
            len(str(coordinate.numerator)) + len(str(coordinate.denominator)),
            variable,
        ))
    assert candidates, "no scalar-coefficient pivot candidate"
    return min(candidates)[-1]


def solve_cert(rows):
    pivots, factors, incompatibilities = {}, [], []
    source = [
        (key,
         {variable: E2.coerce(value) for variable, value in row.items()},
         E2.coerce(rhs))
        for key, row, rhs in rows
    ]
    for row_index, (key, original_row, original_rhs) in enumerate(source):
        row, rhs = dict(original_row), original_rhs
        combination = {row_index: E2(1)}
        while row:
            pivot = next((variable for variable in pivots if variable in row), None)
            if pivot is None:
                break
            factor = row[pivot]
            old_row, old_rhs, old_combination = pivots[pivot]
            for variable, coefficient in old_row.items():
                value = row.get(variable, E2()) - factor * coefficient
                if value:
                    row[variable] = value
                else:
                    row.pop(variable, None)
            rhs -= factor * old_rhs
            for old_index, coefficient in old_combination.items():
                value = combination.get(old_index, E2()) - factor * coefficient
                if value:
                    combination[old_index] = value
                else:
                    combination.pop(old_index, None)
        if not row:
            replay = {}
            for source_index, scalar in combination.items():
                _, source_row, source_rhs = source[source_index]
                replay = add(
                    replay,
                    source_polynomial(source_row, source_rhs),
                    scalar,
                )
            assert clean(replay) == clean(source_polynomial({}, rhs))
            if rhs:
                incompatibilities.append((row_index, key, rhs, combination))
            continue
        pivot = choose_new_pivot(row)
        lead = row[pivot]
        inverse = lead.inverse()
        pivots[pivot] = (
            {variable: coefficient * inverse for variable, coefficient in row.items()},
            rhs * inverse,
            {index: coefficient * inverse for index, coefficient in combination.items()},
        )
        factors.append((row_index, key, pivot, lead))

    # Exact factorized source replay of every normalized pivot row.
    for pivot, (row, rhs, combination) in pivots.items():
        replay = {}
        for source_index, scalar in combination.items():
            _, source_row, source_rhs = source[source_index]
            replay = add(replay, source_polynomial(source_row, source_rhs), scalar)
        assert clean(replay) == clean(source_polynomial(row, rhs)), pivot
    return pivots, factors, incompatibilities


def divide(polynomial, pivots):
    remainder, quotients = dict(polynomial), {}
    normalized = {
        pivot: source_polynomial(row, rhs)
        for pivot, (row, rhs, _) in pivots.items()
    }
    pivot_order = list(pivots) if (SPARSE_PIVOTS or B_LOCAL_PIVOTS) else sorted(
        pivots, reverse=REVERSE_PIVOTS
    )
    for pivot in pivot_order:
        quotient = {}
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
            remainder = add(remainder, multiply(multiplier, normalized[pivot]), E2(-1))
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
        for row_index, coefficient in combination.items():
            relations[row_index] = add(relations[row_index], quotient, coefficient)
    return relations


def scalar_coordinates(value):
    value = E2.coerce(value).value
    return tuple(
        coordinate
        for kvalue in value.coefficients
        for coordinate in kvalue.coordinates
    )


def scalar_exact(value):
    return tuple(
        (str(coordinate.numerator), str(coordinate.denominator))
        for coordinate in scalar_coordinates(value)
    )


def scalar_digest(value):
    return sha256(repr(scalar_exact(value)).encode()).hexdigest()


def polynomial_digest(poly):
    return sha256(repr(tuple(
        (monomial, scalar_digest(value))
        for monomial, value in sorted(poly.items())
    )).encode()).hexdigest()


def denominator_lcm(values):
    out = t.ONE
    for value in values:
        for coordinate in scalar_coordinates(value):
            denominator = coordinate.denominator
            common = out.gcd(denominator)
            out = (out // common) * denominator
            if out:
                out = out / out.leading_coefficient()
    return out


def monic_polynomial(value):
    if not value:
        return value
    return value / value.leading_coefficient()


def cleared_scalar_gcd(value):
    """Common zero factor of all exact E-coordinate numerators."""
    coordinates = scalar_coordinates(value)
    denominator = denominator_lcm([value])
    cleared = [
        coordinate.numerator * (denominator // coordinate.denominator)
        for coordinate in coordinates if coordinate
    ]
    assert cleared
    common = cleared[0]
    for numerator in cleared[1:]:
        common = common.gcd(numerator)
    common = monic_polynomial(common)
    assert all(not numerator % common for numerator in cleared)
    return denominator, common


def transport_chart_polynomial(events):
    """A conservative exact chart for every fraction-field transport pivot."""
    chart = t.ONE
    for _, _, _, numerator, denominator in events:
        if numerator.total_degree():
            chart *= numerator
        if denominator.total_degree():
            chart *= denominator
    return monic_polynomial(chart)


def as_u_polynomial(poly):
    """Convert a C-free exact Q[C,U] polynomial to Q[U]."""
    data = poly.to_dict()
    assert all(c_degree == 0 for (c_degree, _), _ in data.items()), poly
    degree = max((u_degree for (_, u_degree) in data), default=0)
    coefficients = [t.flint.fmpq(0) for _ in range(degree + 1)]
    for (_, u_degree), coefficient in data.items():
        coefficients[u_degree] = coefficient
    return t.flint.fmpq_poly(coefficients)


def bezout_unit_u(denominator, modulus):
    """Return an exact inverse and Bezout cofactor modulo a U-polynomial."""
    denominator_u = as_u_polynomial(denominator)
    modulus_u = as_u_polynomial(modulus)
    common, inverse, cofactor = denominator_u.xgcd(modulus_u)
    assert common.degree() == 0 and common[0]
    inverse /= common[0]
    cofactor /= common[0]
    one = t.flint.fmpq_poly([1])
    assert inverse * denominator_u + cofactor * modulus_u == one
    return denominator_u, modulus_u, inverse, cofactor


def make_u_quotient_reducer(modulus):
    """Canonical exact E-coordinate reduction in Q[U]/(modulus)."""
    modulus_u = as_u_polynomial(modulus)
    inverse_cache = {}

    def inverse_of(denominator):
        key = str(denominator)
        inverse = inverse_cache.get(key)
        if inverse is None:
            denominator_u, checked_modulus, inverse, _ = bezout_unit_u(
                denominator, modulus
            )
            assert checked_modulus == modulus_u
            inverse %= modulus_u
            assert (denominator_u * inverse) % modulus_u == 1
            inverse_cache[key] = inverse
        return inverse

    def reduce_scalar(value):
        reduced_coordinates = []
        for coordinate in scalar_coordinates(value):
            numerator_u = as_u_polynomial(coordinate.numerator)
            inverse = inverse_of(coordinate.denominator)
            reduced = (numerator_u * inverse) % modulus_u
            reduced_coordinates.append(tuple(
                str(reduced[index]) for index in range(modulus_u.degree())
            ))
        return tuple(reduced_coordinates)

    return modulus_u, reduce_scalar


def quotient_polynomial_exact(poly, reduce_scalar):
    return tuple(
        (monomial, reduce_scalar(value))
        for monomial, value in sorted(poly.items())
        if value
    )


def polynomial_values(polynomials):
    for polynomial in polynomials:
        yield from polynomial.values()


def center_coordinates():
    if STRATUM == "generic":
        return t.Rat2(t.C), t.Rat2(t.U), "C,U independent"
    if STRATUM == "u-zero":
        return t.Rat2(t.C), t.Rat2(0), "U=0 over Q(C)"
    if STRATUM == "h-zero":
        return t.Rat2(3 * t.U**2), t.Rat2(t.U), "C=3U^2 over Q(U)"
    if STRATUM == "intersection":
        return t.Rat2(0), t.Rat2(0), "C=U=0"
    if STRATUM == "generic-control":
        return t.Rat2(1), t.Rat2(2), "C=1,U=2"
    raise ValueError(f"unknown stratum {STRATUM!r}")


def main():
    print(
        "first_pivot_order=" + (
            "B-local-scalar" if B_LOCAL_PIVOTS else
            "sparse-scalar" if SPARSE_PIVOTS else
            "descending" if REVERSE_PIVOTS else "ascending"
        ),
        flush=True,
    )
    center_c, center_u, center_label = center_coordinates()
    print(f"center_stratum={center_label}", flush=True)
    fb.CENTER = (center_c, t.Rat2(1), center_u)
    fb._X_POWER_CACHE.clear()
    nf, rows_f = fb.build_transport(
        15, 60, 3, {15: b.Q(1)}, fb.F1_F_PATTERN, fb.POLE_F_PATTERN
    )
    ng, rows_g = fb.build_transport(
        25, 100, 5, {1: b.Q(1), 25: b.Q(1)}, fb.F1_G_PATTERN, fb.POLE_G_PATTERN
    )
    rows = [(("f",) + key, row, rhs) for key, row, rhs in rows_f]
    rows += [
        (("g",) + key,
         {nf + variable: coefficient for variable, coefficient in row.items()}, rhs)
        for key, row, rhs in rows_g
    ]
    ordered = [row for row in rows if row[0][1] != "X"] + [
        row for row in rows if row[0][1] == "X"
    ]
    transport_pivots, records, transport_events, determinant = t.factor(ordered)
    pivot_rhs, compatibility = t.propagate(ordered, records)
    assert len(transport_pivots) == 3470 and not compatibility
    free = [variable for variable in range(nf + ng) if variable not in transport_pivots]
    free_parameter = {variable: index for index, variable in enumerate(free)}
    assert len(free) == 132
    print("P12 bivariate transport PASS", flush=True)

    bands = {}
    for owner, imax, jmax, offset in (("f", 15, 60, 0), ("g", 25, 100, nf)):
        for exponent in (1, 2, 3):
            forms = []
            for degree in range(16 if owner == "f" else 26):
                row = {
                    offset + variable: coefficient
                    for variable, coefficient in fb.x_chart_coefficient(
                        imax, jmax, exponent, degree
                    ).items()
                }
                forms.append(b.restrict_row(
                    row, transport_pivots, pivot_rhs, free_parameter
                ))
            bands[(owner, exponent)] = forms

    qd.Dual = E2
    qd.Q_PRIME = {0: E2(1), 24: E2(25)}
    first_rows = qd.pack(
        "X-2", qd.first_band_polynomials(bands[("f", 1)], bands[("g", 1)])
    )
    first_pivots, first_factors, first_incompatibilities = solve_cert(first_rows)
    if STRATUM == "generic":
        assert not first_incompatibilities
        assert len(first_pivots) == 38
    print(f"first_rank={len(first_pivots)}/132", flush=True)
    print(f"first_incompatibility_count={len(first_incompatibilities)}", flush=True)
    print("P12 bivariate first/source replay PASS", flush=True)
    if first_incompatibilities:
        transport_chart_denominator = transport_chart_polynomial(transport_events)
        first_source_denominator = denominator_lcm(
            coefficient
            for _, row, rhs in first_rows
            for coefficient in list(row.values()) + [rhs]
        )
        print(f"transport_event_count={len(transport_events)}")
        for event_index, event in enumerate(transport_events):
            row_index, key, pivot, numerator, denominator = event
            print(
                f"transport_event[{event_index}]={row_index},{key},{pivot};"
                f"num=({numerator});den=({denominator})"
            )
        print(
            "transport_chart_denominator="
            f"({transport_chart_denominator})"
        )
        print(
            "transport_chart_denominator_factor="
            f"{transport_chart_denominator.factor()}"
        )
        print(f"first_source_denominator=({first_source_denominator})")
        print(
            "first_source_denominator_factor="
            f"{first_source_denominator.factor()}"
        )
        for index, (row_index, key, residual, combination) in enumerate(
            first_incompatibilities
        ):
            residual_denominator, residual_gcd = cleared_scalar_gcd(residual)
            combination_denominator = denominator_lcm(combination.values())
            certificate_chart_denominator = monic_polynomial(
                transport_chart_denominator
                * first_source_denominator
                * combination_denominator
                * residual_denominator
            )
            print(f"first_incompatibility[{index}]_row_index={row_index}")
            print(f"first_incompatibility[{index}]_key={key}")
            print(
                f"first_incompatibility[{index}]_residual_sha256="
                f"{scalar_digest(residual)}"
            )
            print(
                f"first_incompatibility[{index}]_residual_coordinates="
                f"{scalar_exact(residual)}"
            )
            exact_combination = tuple(
                (
                    source_index,
                    first_rows[source_index][0],
                    scalar_exact(coefficient),
                )
                for source_index, coefficient in sorted(combination.items())
            )
            print(
                f"first_incompatibility[{index}]_source_row_count="
                f"{len(combination)}"
            )
            print(
                f"first_incompatibility[{index}]_source_certificate_sha256="
                f"{sha256(repr(exact_combination).encode()).hexdigest()}"
            )
            print(
                f"first_incompatibility[{index}]_source_certificate_exact="
                f"{exact_combination}"
            )
            print(
                f"first_incompatibility[{index}]_source_certificate_relation="
                "sum(coeff_i*(row_i-rhs_i))=-residual"
            )
            print(
                f"first_incompatibility[{index}]_residual_denominator="
                f"({residual_denominator})"
            )
            print(
                f"first_incompatibility[{index}]_residual_denominator_factor="
                f"{residual_denominator.factor()}"
            )
            print(
                f"first_incompatibility[{index}]_cleared_numerator_gcd="
                f"({residual_gcd})"
            )
            print(
                f"first_incompatibility[{index}]_cleared_numerator_gcd_factor="
                f"{residual_gcd.factor()}"
            )
            print(
                f"first_incompatibility[{index}]_combination_denominator="
                f"({combination_denominator})"
            )
            print(
                f"first_incompatibility[{index}]_combination_denominator_factor="
                f"{combination_denominator.factor()}"
            )
            print(
                f"first_incompatibility[{index}]_certificate_chart_denominator="
                f"({certificate_chart_denominator})"
            )
            print(
                f"first_incompatibility[{index}]_certificate_chart_denominator_factor="
                f"{certificate_chart_denominator.factor()}"
            )
            residual_unit = residual_gcd.total_degree() == 0
            whole_stratum = (
                residual_unit
                and certificate_chart_denominator.total_degree() == 0
            )
            print(
                f"first_incompatibility[{index}]_residual_unit_on_chart="
                f"{str(residual_unit).lower()}"
            )
            print(
                f"first_incompatibility[{index}]_whole_stratum_empty="
                f"{str(whole_stratum).lower()}"
            )
        print("first_incompatibility_original_row_replay=true")
        print("P12_compile_skipped_first_band_empty=true")
        print("family_killed=false")
        print("SP2_killed=false")
        print("JC2_resolved=false")
        print("TD6-C1-C3-FIRST-BAND-INCONSISTENT-STRATUM PASS")
        return

    raw = qd.compile_current(
        *[bands[("f", exponent)] for exponent in (1, 2, 3)],
        *[bands[("g", exponent)] for exponent in (1, 2, 3)],
    )[12]
    polynomial = {
        monomial: E2.coerce(coefficient)
        for monomial, coefficient in raw.items() if coefficient
    }
    assert max(map(len, polynomial)) == 2
    if STRATUM == "generic":
        assert len(polynomial) == 2893
    print("P12 bivariate genuine polynomial PASS", flush=True)

    remainder, quotients = divide(polynomial, first_pivots)
    relations = lift_relations(quotients, first_pivots, len(first_rows))
    source_identity = {}
    for relation, (_, row, rhs) in zip(relations, first_rows):
        source_identity = add(
            source_identity,
            multiply(relation, source_polynomial(row, rhs)),
        )
    source_target = add(polynomial, remainder, E2(-1))
    assert clean(source_identity) == clean(source_target)
    S = E2(qd.uniform.S_FIELD)
    k = E2(252) - 342*S + 144*S**2 - 36*S**3
    expected = -k / 50
    assert remainder == {(): expected}
    relation_denominator = denominator_lcm(polynomial_values(relations))
    raw_denominator = denominator_lcm(polynomial.values())
    first_denominator = denominator_lcm(
        coefficient
        for _, row, rhs in first_rows
        for coefficient in list(row.values()) + [rhs]
    )
    # The relation denominator clears every multiplier.  For a fail-closed
    # termwise polynomial identity, also clear the original first-row
    # coefficients; this certified product need not be the minimal common
    # denominator after cancellations in the summed identity.
    termwise_identity_denominator = relation_denominator * first_denominator
    termwise_identity_denominator /= (
        termwise_identity_denominator.leading_coefficient()
    )
    clear = E2(t.Rat2(relation_denominator))
    for relation in relations:
        for coefficient in relation.values():
            assert all(
                coordinate.denominator == t.ONE
                for coordinate in scalar_coordinates(clear * coefficient)
            )
    assert all(
        coordinate.denominator == t.ONE
        for coordinate in scalar_coordinates(clear * expected)
    )
    clear_first = E2(t.Rat2(first_denominator))
    for _, row, rhs in first_rows:
        for coefficient in list(row.values()) + [rhs]:
            assert all(
                coordinate.denominator == t.ONE
                for coordinate in scalar_coordinates(clear_first * coefficient)
            )
    clear_identity = E2(t.Rat2(termwise_identity_denominator))
    for coefficient in polynomial.values():
        assert all(
            coordinate.denominator == t.ONE
            for coordinate in scalar_coordinates(clear_identity * coefficient)
        )
    assert all(
        coordinate.denominator == t.ONE
        for coordinate in scalar_coordinates(clear_identity * expected)
    )
    source_nonzero_rows = sum(bool(relation) for relation in relations)
    source_multiplier_terms = sum(len(relation) for relation in relations)
    if B_LOCAL_PIVOTS and STRATUM == "generic":
        T_poly = (
            4*t.C**2*t.U**2 + 28*t.C*t.U**4 - 4*t.C*t.U
            + 24*t.U**6 - 24*t.U**3 + 1
        )
        expected_relation_denominator = t.U**2 * T_poly / 4
        expected_termwise_denominator = (
            t.U**3 * (t.C - 3*t.U**2) * T_poly / 4
        )
        assert relation_denominator == expected_relation_denominator
        assert termwise_identity_denominator == expected_termwise_denominator
        assert (source_nonzero_rows, source_multiplier_terms) == (28, 1564)
    print("P12 bivariate reduction PASS", flush=True)
    print(f"raw_terms={len(polynomial)};raw_degree={max(map(len, polynomial))}")
    print(f"raw_sha256={polynomial_digest(polynomial)}")
    print(f"remainder_sha256={polynomial_digest(remainder)}")
    print(f"expected_sha256={scalar_digest(expected)}")
    print(f"source_nonzero_rows={source_nonzero_rows}")
    print(f"source_multiplier_terms={source_multiplier_terms}")
    print("source_relation_original_row_replay=true")
    print(f"source_relation_sha256={sha256(repr(tuple(
        tuple((monomial, scalar_digest(value)) for monomial, value in sorted(relation.items()))
        for relation in relations
    )).encode()).hexdigest()}")
    print(f"raw_denominator=({raw_denominator})")
    print(f"raw_denominator_factor={raw_denominator.factor()}")
    print(f"first_denominator=({first_denominator})")
    print(f"first_denominator_factor={first_denominator.factor()}")
    print(f"relation_denominator=({relation_denominator})")
    print(f"relation_denominator_factor={relation_denominator.factor()}")
    print(f"relation_denominator_sha256={sha256(str(relation_denominator).encode()).hexdigest()}")
    print("cleared_relation_coefficients_polynomial=true")
    print(f"termwise_identity_denominator=({termwise_identity_denominator})")
    print(
        "termwise_identity_denominator_factor="
        f"{termwise_identity_denominator.factor()}"
    )
    print(
        "termwise_identity_denominator_sha256="
        f"{sha256(str(termwise_identity_denominator).encode()).hexdigest()}"
    )
    print("termwise_polynomial_clear_checks=true")
    if B_LOCAL_PIVOTS:
        assert B_POLY.subs({"U": 0}) == t.ONE
        print("B_at_U_zero=1")
        if STRATUM == "generic":
            T_resultant = B_POLY.resultant(T_poly, 0)
            assert T_resultant == 64*t.U**10
            print(f"B_local_T_resultant=({T_resultant})")
            print(f"B_local_T_resultant_factor={T_resultant.factor()}")
        for name, denominator in (
            ("relation", relation_denominator),
            ("termwise", termwise_identity_denominator),
        ):
            resultant = B_POLY.resultant(denominator, 0)
            _, factors = resultant.factor()
            assert all(
                factor == t.U or factor == B_H_RESULTANT
                for factor, _ in factors
            ), (name, resultant.factor())
            print(f"B_local_{name}_resultant=({resultant})")
            print(f"B_local_{name}_resultant_factor={resultant.factor()}")
            if STRATUM == "generic":
                expected_resultant = (
                    4*t.U**14 if name == "relation" else
                    4*t.U**16*B_H_RESULTANT
                )
                assert resultant == expected_resultant
        print("B_local_denominator_unit_off_UH=true")
    if SPARSE_PIVOTS and STRATUM == "h-zero":
        modulus = B_H_RESULTANT
        assert B_POLY.compose(3*t.U**2, t.U) == modulus
        modulus_u = as_u_polynomial(modulus)
        modulus_factorization = modulus_u.factor()
        assert modulus_u.degree() == 6
        assert modulus_u.gcd(modulus_u.derivative()) == 1
        assert (
            len(modulus_factorization[1]) == 1
            and modulus_factorization[1][0][0] == modulus_u
            and modulus_factorization[1][0][1] == 1
        )
        transport_chart = transport_chart_polynomial(transport_events)
        quotient_denominators = (
            ("transport", transport_chart),
            ("raw", raw_denominator),
            ("first", first_denominator),
            ("relation", relation_denominator),
            ("termwise", termwise_identity_denominator),
        )
        print(f"H_B_modulus=({modulus})")
        print(f"H_B_modulus_factor={modulus_factorization}")
        print("H_B_modulus_squarefree=true")
        for name, denominator in quotient_denominators:
            common = as_u_polynomial(denominator).gcd(modulus_u)
            print(f"H_B_{name}_denominator_gcd=({common})")
            assert common.degree() == 0 and common[0]
        (
            termwise_u,
            checked_modulus,
            termwise_inverse,
            termwise_cofactor,
        ) = bezout_unit_u(termwise_identity_denominator, modulus)
        assert checked_modulus == modulus_u
        print(f"H_B_termwise_denominator_u=({termwise_u})")
        print(f"H_B_termwise_bezout_inverse=({termwise_inverse})")
        print(f"H_B_termwise_bezout_cofactor=({termwise_cofactor})")
        print("H_B_termwise_bezout_identity=true")
        checked_modulus, reduce_quotient_scalar = make_u_quotient_reducer(modulus)
        assert checked_modulus == modulus_u
        quotient_relations = tuple(
            tuple(
                (monomial, reduce_quotient_scalar(value))
                for monomial, value in sorted(relation.items())
            )
            for relation in relations
        )
        quotient_source_identity = quotient_polynomial_exact(
            source_identity, reduce_quotient_scalar
        )
        quotient_source_target = quotient_polynomial_exact(
            source_target, reduce_quotient_scalar
        )
        assert quotient_source_identity == quotient_source_target
        assert quotient_source_target
        assert quotient_polynomial_exact({}, reduce_quotient_scalar) != (
            quotient_source_target
        )
        print(
            "H_B_quotient_relation_sha256="
            f"{sha256(repr(quotient_relations).encode()).hexdigest()}"
        )
        print(
            "H_B_quotient_source_identity_sha256="
            f"{sha256(repr(quotient_source_identity).encode()).hexdigest()}"
        )
        print("H_B_quotient_original_row_replay=true")
        print("H_B_quotient_omit_all_relations_negative_control=true")
        print("H_B_specialized_P12=-k/50")
        print("TD6-C1-C3-H-B-QUOTIENT PASS")
    print("TD6-C1-C3-MPOLY-P12-GENERIC PASS")


if __name__ == "__main__":
    main()
