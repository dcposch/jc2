#!/usr/bin/env python3
"""Literal total-(F,all licensed q) raw P12/FIRST certificate.

Substantive execution is AWS-gated by the wrapper.  QPoly is an untruncated
sparse multivariate polynomial ring over the exact V85 E3 coefficient field.
Only raw FIRST and the literal degree-12 raw CURRENT formula are consumed.
"""

from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
V86_PATH = HERE / "replay_v86tfq2_total_f_q2.py"
V86_SHA256 = "5b160a2bd18434e6142c33be6775e0c212c22ebc67a52d08b246dd0223decd7c"
assert sha256(V86_PATH.read_bytes()).hexdigest() == V86_SHA256
spec = importlib.util.spec_from_file_location("td6_v87_v86_parent", V86_PATH)
v86 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = v86
spec.loader.exec_module(v86)

v85 = v86.v85
m = v85.m
E3, Rat3 = v85.E3, v85.Rat3
C, V, U = v85.C, v85.V, v85.U
F, H, B3 = v85.F, v85.H, v85.B3
TOTAL_TARGET = v85.TOTAL_TARGET
Q_EXPONENTS = tuple(list(range(2, 15)) + list(range(16, 25)))
Q_ORDER = {exponent: index for index, exponent in enumerate(Q_EXPONENTS)}
assert len(Q_EXPONENTS) == 22 and 15 not in Q_EXPONENTS
EXPECTED_V85_H_SHA256 = (
    "7434b0a7434288e421ad300e93c5da8084f69f19a801298ec6ec05bf9b85bb70"
)


class QPoly:
    """Sparse exact E3[q_e : e in Q_EXPONENTS], with no degree cutoff."""

    __slots__ = ("coefficients",)

    def __init__(self, value=0, coefficients=None):
        if isinstance(value, QPoly):
            data = dict(value.coefficients)
        else:
            coefficient = E3.coerce(value)
            data = {(): coefficient} if coefficient else {}
        if coefficients:
            for monomial, coefficient in coefficients.items():
                monomial = tuple(sorted(monomial, key=Q_ORDER.__getitem__))
                assert all(exponent in Q_ORDER for exponent in monomial)
                coefficient = E3.coerce(coefficient)
                total = data.get(monomial, E3()) + coefficient
                if total:
                    data[monomial] = total
                else:
                    data.pop(monomial, None)
        self.coefficients = data

    @staticmethod
    def coerce(value):
        return value if isinstance(value, QPoly) else QPoly(value)

    @staticmethod
    def variable(exponent, coefficient=1):
        assert exponent in Q_ORDER
        return QPoly(0, {(exponent,): E3.coerce(coefficient)})

    def constant(self):
        return self.coefficients.get((), E3())

    def __add__(self, other):
        other = QPoly.coerce(other)
        return QPoly(self, other.coefficients)

    __radd__ = __add__

    def __neg__(self):
        return QPoly(0, {
            monomial: -coefficient
            for monomial, coefficient in self.coefficients.items()
        })

    def __sub__(self, other):
        return self + (-QPoly.coerce(other))

    def __rsub__(self, other):
        return QPoly.coerce(other) - self

    def __mul__(self, other):
        other = QPoly.coerce(other)
        out = {}
        for left_monomial, left in self.coefficients.items():
            for right_monomial, right in other.coefficients.items():
                monomial = tuple(sorted(
                    left_monomial + right_monomial,
                    key=Q_ORDER.__getitem__,
                ))
                total = out.get(monomial, E3()) + left*right
                if total:
                    out[monomial] = total
                else:
                    out.pop(monomial, None)
        return QPoly(0, out)

    __rmul__ = __mul__

    def inverse(self):
        assert set(self.coefficients).issubset({()}), (
            "attempted_q_polynomial_inverse", tuple(self.coefficients)
        )
        constant = self.constant()
        if not constant:
            raise ZeroDivisionError("zero q-polynomial constant")
        return QPoly(constant.inverse())

    def __truediv__(self, other):
        return self * QPoly.coerce(other).inverse()

    def __rtruediv__(self, other):
        return QPoly.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base = QPoly(1), self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.coefficients)

    def __eq__(self, other):
        return self.coefficients == QPoly.coerce(other).coefficients

    def __repr__(self):
        return "QPoly(" + repr(sorted(self.coefficients.items())) + ")"


# Reuse V86's section-polynomial arithmetic after replacing its coefficient
# type.  These functions resolve BPoly dynamically in the V86 module.
v86.BPoly = QPoly
clean = v86.clean
add = v86.add
scale = v86.scale
multiply = v86.multiply
embed = v86.embed
source_polynomial = v86.source_polynomial


def q_constant(polynomial):
    return {
        monomial: value.constant()
        for monomial, value in polynomial.items() if value.constant()
    }


def max_q_degree(polynomials):
    return max(
        (
            len(q_monomial)
            for polynomial in polynomials
            for value in polynomial.values()
            for q_monomial in QPoly.coerce(value).coefficients
        ),
        default=0,
    )


def coefficient_term_count(polynomial):
    return sum(len(value.coefficients) for value in polynomial.values())


def full_digest(polynomial):
    lines = []
    for parameter_monomial, value in sorted(polynomial.items()):
        for q_monomial, coefficient in sorted(value.coefficients.items()):
            lines.append(
                f"{parameter_monomial!r}\t{q_monomial!r}\t"
                f"{m.e3_exact(coefficient)}"
            )
    return sha256(("\n".join(lines) + "\n").encode()).hexdigest()


def source_value(key):
    value = QPoly(m.from_vector(m.r.t.source_vector(key)))
    if (
        len(key) == 4 and key[0] == "g" and key[1] == "X"
        and key[2] == 0 and key[3] in Q_ORDER
    ):
        value += QPoly.variable(key[3])
    return value


def propagate_all_q(rows, records):
    pivot_rhs, compatibility = {}, []
    seen = {exponent: 0 for exponent in Q_EXPONENTS}
    for source_row, record in zip(rows, records):
        source_key, _, _ = source_row
        key, kind, pivot, lead, factors = record
        assert source_key == key
        if (
            len(key) == 4 and key[0] == "g" and key[1] == "X"
            and key[2] == 0 and key[3] in seen
        ):
            seen[key[3]] += 1
        value = source_value(key)
        for old, factor in factors:
            value -= QPoly(m.scalar(factor))*pivot_rhs[old]
        if kind == "pivot":
            pivot_rhs[pivot] = QPoly(m.scalar(lead.inverse()))*value
        elif value:
            compatibility.append((key, value))
    assert set(seen.values()) == {1}, seen
    return pivot_rhs, compatibility, seen


def configure_qd(omit_direct=None):
    qd = m.r.qd
    qd.Dual = QPoly
    qd.B = QPoly.variable(2)
    qd.S = QPoly(E3(qd.uniform.S_FIELD))
    qd.D = QPoly(E3(qd.uniform.D_FIELD))
    qd.L = QPoly(E3(qd.uniform.L_FIELD))
    qd.A = QPoly(E3(qd.uniform.A_FIELD))
    qd.Q_PRIME = {0: QPoly(1), 24: QPoly(25)}
    for exponent in Q_EXPONENTS:
        if exponent != omit_direct:
            qd.Q_PRIME[exponent - 1] = QPoly.variable(exponent, exponent)
    qd.R = qd.multiply(
        qd.multiply([QPoly(-1), QPoly(1)], [QPoly(-1), QPoly(1)]),
        [qd.D, -qd.S, QPoly(1)],
    )
    qd.R3, qd.R5 = qd.power(qd.R, 3), qd.power(qd.R, 5)
    qd.POLE_F = {1: -(qd.L**3)*qd.A, 6: qd.L**3}
    qd.POLE_G = {
        0: QPoly(m.r.b.Q(5, 9))*qd.L**5*qd.A**2,
        5: QPoly(m.r.b.Q(-5, 3))*qd.L**5*qd.A,
        10: qd.L**5,
    }


def compile_first(bands, omit_direct=None):
    configure_qd(omit_direct)
    qd = m.r.qd
    return qd.pack(
        "X-2", qd.first_band_polynomials(
            bands[("f", 1)], bands[("g", 1)]
        )
    )


def compile_current_degree12(bands):
    """Literal degree-12 extraction of frozen compile_x_current."""
    configure_qd(None)
    qd, nr = m.r.qd, m.r.qd.nr
    f1, f2, f3 = (bands[("f", power)] for power in (1, 2, 3))
    g1, g2, g3 = (bands[("g", power)] for power in (1, 2, 3))
    degree = 12
    equation = {}
    for i, left in enumerate(f1):
        j = degree - i + 1
        if 1 <= j < len(g2):
            equation = nr.add_polynomial(
                equation,
                nr.multiply_affine(left, nr.scale_affine(g2[j], j)),
            )
    for i, left in enumerate(f2):
        j = degree - i + 1
        if 1 <= j < len(g1):
            equation = nr.add_polynomial(
                equation,
                nr.multiply_affine(left, nr.scale_affine(g1[j], j)),
                2,
            )
    for i, form in enumerate(f3):
        multiplier = qd.Q_PRIME.get(degree - i, QPoly())
        if multiplier:
            equation = nr.add_polynomial(
                equation, nr.affine_polynomial(form), 3*multiplier
            )
    g_degree = degree - 14
    if 0 <= g_degree < len(g3):
        equation = nr.add_polynomial(
            equation, nr.affine_polynomial(g3[g_degree]), -45
        )
    for i in range(1, len(f1)):
        j = degree - (i - 1)
        if 0 <= j < len(g2):
            equation = nr.add_polynomial(
                equation,
                nr.multiply_affine(nr.scale_affine(f1[i], i), g2[j]),
                -2,
            )
    for i in range(1, len(f2)):
        j = degree - (i - 1)
        if 0 <= j < len(g1):
            equation = nr.add_polynomial(
                equation,
                nr.multiply_affine(nr.scale_affine(f2[i], i), g1[j]),
                -1,
            )
    return clean({monomial: QPoly.coerce(value) for monomial, value in equation.items()})


def build_bands():
    v85.restore_base_qd_state()
    m.r.fb.CENTER = (Rat3(C), Rat3(V), Rat3(U))
    m.r.fb._X_POWER_CACHE.clear()
    nf, rows_f = m.r.fb.build_transport(
        15, 60, 3, {15: m.r.b.Q(1)},
        m.r.fb.F1_F_PATTERN, m.r.fb.POLE_F_PATTERN,
    )
    ng, rows_g = m.r.fb.build_transport(
        25, 100, 5, {1: m.r.b.Q(1), 25: m.r.b.Q(1)},
        m.r.fb.F1_G_PATTERN, m.r.fb.POLE_G_PATTERN,
    )
    rows = [(("f",) + key, row, rhs) for key, row, rhs in rows_f]
    rows += [
        (
            ("g",) + key,
            {nf + variable: coefficient for variable, coefficient in row.items()},
            rhs,
        )
        for key, row, rhs in rows_g
    ]
    ordered = [row for row in rows if row[0][1] != "X"] + [
        row for row in rows if row[0][1] == "X"
    ]
    pivots, records, events, _ = m.tri.factor_transport(ordered)
    pivot_rhs, compatibility, seen = propagate_all_q(ordered, records)
    assert not compatibility and len(pivots) == 3470
    free = [variable for variable in range(nf + ng) if variable not in pivots]
    assert len(free) == 132
    free_parameter = {variable: index for index, variable in enumerate(free)}

    def restrict(row):
        return v86.restrict_row(row, pivots, pivot_rhs, free_parameter)

    bands = {}
    for owner, imax, jmax, offset in (
        ("f", 15, 60, 0), ("g", 25, 100, nf)
    ):
        for power in (1, 2, 3):
            forms = []
            for degree in range(16 if owner == "f" else 26):
                row = {
                    offset + variable: coefficient
                    for variable, coefficient in m.r.fb.x_chart_coefficient(
                        imax, jmax, power, degree
                    ).items()
                }
                forms.append(restrict(row))
            bands[(owner, power)] = forms
    return len(events), bands, seen


def remove_q(value, exponent):
    value = QPoly.coerce(value)
    return QPoly(0, {
        monomial: coefficient
        for monomial, coefficient in value.coefficients.items()
        if exponent not in monomial
    })


def omit_transport_path(bands, exponent):
    return {
        key: [
            (
                remove_q(constant, exponent),
                {
                    variable: remove_q(coefficient, exponent)
                    for variable, coefficient in row.items()
                    if remove_q(coefficient, exponent)
                },
            )
            for constant, row in forms
        ]
        for key, forms in bands.items()
    }


def family_map(first):
    return {
        key: source_polynomial(row, rhs)
        for key, row, rhs in first
    }


def omission_record(full, omitted):
    keys = sorted(set(full) | set(omitted))
    changed = [key for key in keys if full.get(key, {}) != omitted.get(key, {})]
    assert changed
    key = changed[0]
    difference = add(full.get(key, {}), omitted.get(key, {}), -1)
    assert difference
    return len(changed), key, full_digest(difference)


def decompose_q_residual(polynomial):
    quotients = {exponent: {} for exponent in Q_EXPONENTS}
    coefficient_count = 0
    for parameter_monomial, value in polynomial.items():
        assert not value.constant(), ("q_nondivisible", parameter_monomial)
        for q_monomial, coefficient in value.coefficients.items():
            assert q_monomial
            exponent = q_monomial[0]
            rest = q_monomial[1:]
            contribution = QPoly(0, {rest: coefficient})
            old = quotients[exponent].get(parameter_monomial, QPoly())
            total = old + contribution
            if total:
                quotients[exponent][parameter_monomial] = total
            else:
                quotients[exponent].pop(parameter_monomial, None)
            coefficient_count += 1
    replay = {}
    for exponent in Q_EXPONENTS:
        replay = add(replay, scale(
            quotients[exponent], QPoly.variable(exponent)
        ))
    assert replay == clean(polynomial)
    return quotients, coefficient_count


def all_coefficients(polynomials):
    for polynomial in polynomials:
        for value in polynomial.values():
            yield from QPoly.coerce(value).coefficients.values()


def assert_denominators_allowed(polynomials):
    coefficients = list(all_coefficients(polynomials))
    common = v85.monic(m.denominator_for(coefficients))
    assert v85.factors_allowed(common), common.factor()
    assert common.gcd(F).total_degree() == 0
    return coefficients, common


def assert_polynomial_after_clear(coefficients, common):
    count = 0
    scalar = E3(Rat3(common))
    for coefficient in coefficients:
        cleared = scalar*coefficient
        for coordinate in m.r.scalar_coordinates(cleared):
            count += 1
            assert coordinate.denominator == m.tri.ONE
    return count


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    print("producer=TD6-V87TFAQ-LITERAL-TOTAL-F-ALLQ-RAW-P12-SOURCE")
    print("q_exponents=" + ",".join(map(str, Q_EXPONENTS)))
    print("q15_fixed_zero=true")
    print("q_ring=untruncated_sparse_multivariate_E3")
    print("total_ring=Q[C,V,U,q_e] localized at U*H*B3")
    print("raw_current_degree12_extracted_literal=true")
    print("staged_CURRENT_used=false")
    print("PREVIOUS_POLE_used=false", flush=True)

    event_count, bands, seen = build_bands()
    total_first = compile_first(bands)
    total_p12 = compile_current_degree12(bands)
    total_sources = [source_polynomial(row, rhs) for _, row, rhs in total_first]
    total_family = family_map(total_first)
    print(f"transport_event_count={event_count}")
    print("transport_source_path_counts=" + ",".join(
        f"q{exponent}:{seen[exponent]}" for exponent in Q_EXPONENTS
    ))
    print("all_transport_q_paths_retained=true")
    print("all_direct_qprime_paths_retained=true", flush=True)

    omission_lines = [
        "q_exponent\ttransport_changed_rows\ttransport_first_key"
        "\ttransport_difference_sha256\tdirect_changed_rows"
        "\tdirect_first_key\tdirect_difference_sha256"
    ]
    for exponent in Q_EXPONENTS:
        no_transport = family_map(compile_first(
            omit_transport_path(bands, exponent)
        ))
        transport_record = omission_record(total_family, no_transport)
        no_direct = family_map(compile_first(bands, omit_direct=exponent))
        direct_record = omission_record(total_family, no_direct)
        omission_lines.append(
            f"{exponent}\t{transport_record[0]}\t{transport_record[1]!r}\t"
            f"{transport_record[2]}\t{direct_record[0]}\t"
            f"{direct_record[1]!r}\t{direct_record[2]}"
        )
        print(
            f"omission_q{exponent}=transport:{transport_record[0]};"
            f"direct:{direct_record[0]}", flush=True
        )
    omission_text = "\n".join(omission_lines) + "\n"
    omission_path = outdir / "TOTAL_F_ALLQ_OMISSION_INVENTORY.tsv"
    omission_path.write_text(omission_text)
    omission_sha = sha256(omission_text.encode()).hexdigest()
    print("all_q_path_omission_controls=true", flush=True)

    generic_p12 = q_constant(total_p12)
    generic_sources = [q_constant(source) for source in total_sources]
    assert len(total_first) == len(generic_sources) == 38
    assert len(generic_p12) == 2893
    v85_p12_digest, v85_first_digests = v86.read_v85_inventory()
    assert m.polynomial_digest(generic_p12) == v85_p12_digest
    for index, source in enumerate(generic_sources):
        assert m.polynomial_digest(source) == v85_first_digests[index]
    print("all_q_zero_raw_FIRST_matches_frozen_V85_inventory=true")
    print("all_q_zero_raw_P12_matches_frozen_V85_inventory=true")

    labels = set()
    for polynomial in [total_p12, *total_sources]:
        for monomial in polynomial:
            labels.update(monomial)
    assert labels == set(range(132))
    print("all_132_transport_free_section_coordinates_retained=true")

    p12_multiplier, first_multipliers, used_keys = (
        v85.read_frozen_multipliers(total_first)
    )
    q_p12_multiplier = embed(p12_multiplier)
    q_first_multipliers = [embed(value) for value in first_multipliers]
    special_p12 = v85.specialize_polynomial(generic_p12)
    special_sources = [
        v85.specialize_polynomial(source) for source in generic_sources
    ]
    special_identity = v85.multiply(p12_multiplier, special_p12)
    for multiplier, source in zip(first_multipliers, special_sources):
        if multiplier:
            special_identity = v85.add(
                special_identity, v85.multiply(multiplier, source)
            )
    assert special_identity == {(): E3(Rat3(v85.SPECIAL_CLEARER))}
    print("frozen_V82QST3_special_identity_replayed=true")

    total_terms = [multiply(q_p12_multiplier, total_p12)]
    total_identity = dict(total_terms[0])
    for multiplier, source in zip(q_first_multipliers, total_sources):
        if multiplier:
            term = multiply(multiplier, source)
            total_terms.append(term)
            total_identity = add(total_identity, term)
    target = {(): QPoly(E3(Rat3(TOTAL_TARGET)))}
    residual = add(target, total_identity, -1)
    residual_q_zero = q_constant(residual)
    h_f, f_division_count = v85.divide_polynomial_by_f(residual_q_zero)
    assert m.polynomial_digest(h_f) == EXPECTED_V85_H_SHA256
    positive_residual = {
        monomial: QPoly(0, {
            q_monomial: coefficient
            for q_monomial, coefficient in value.coefficients.items()
            if q_monomial
        })
        for monomial, value in residual.items()
    }
    positive_residual = clean(positive_residual)
    h_q, q_division_count = decompose_q_residual(positive_residual)
    rhs = add(total_identity, scale(embed(h_f), QPoly(E3(Rat3(F)))))
    for exponent in Q_EXPONENTS:
        rhs = add(rhs, scale(h_q[exponent], QPoly.variable(exponent)))
    assert rhs == target
    print(f"total_residual_terms={len(residual)}")
    print(f"total_q_degree={max_q_degree([total_p12, *total_sources])}")
    print(f"residual_q_degree={max_q_degree([residual])}")
    print(f"F_division_coordinate_count={f_division_count}")
    print(f"q_partition_coefficient_count={q_division_count}")
    print("V85_all_q_zero_hF_hash_reproduced=true")
    print("F_allq_decomposition_exact=true")
    print("F_not_inverted=true")
    print("no_q_variable_inverted=true", flush=True)

    active_index = min(used_keys)
    active_term = multiply(
        q_first_multipliers[active_index], total_sources[active_index]
    )
    correction = scale(embed(h_f), QPoly(E3(Rat3(F))))
    for exponent in Q_EXPONENTS:
        correction = add(
            correction, scale(h_q[exponent], QPoly.variable(exponent))
        )
    assert add(add(total_identity, active_term, -1), correction) != target
    assert add(add(total_identity, total_terms[0], -1), correction) != target
    print(f"FIRST_omission_negative_control_index={active_index}")
    print("FIRST_omission_negative_control=true")
    print("P12_omission_negative_control=true", flush=True)

    audited = [
        q_p12_multiplier, *q_first_multipliers,
        total_p12, *total_sources, *total_terms,
        embed(h_f), *[h_q[exponent] for exponent in Q_EXPONENTS],
    ]
    coefficients, common = assert_denominators_allowed(audited)
    cleared_count = assert_polynomial_after_clear(coefficients, common)
    common_scalar = QPoly(E3(Rat3(common)))
    assert scale(rhs, common_scalar) == scale(target, common_scalar)
    print(f"audited_E3_coefficient_count={len(coefficients)}")
    print(f"total_family_common_denominator=({common})")
    print(f"total_family_common_denominator_factor={common.factor()}")
    print("denominator_radical_subset_U_H_B3=true")
    print(f"cleared_polynomial_scalar_coordinate_count={cleared_count}")
    print("cleared_total_identity_exact=true", flush=True)

    source_lines = [
        "kind\tindex\tkey\tfull_sha256\tall_q_zero_sha256"
    ]
    source_lines.append(
        f"P12\t12\t('X0_RAW', 12)\t{full_digest(total_p12)}\t"
        f"{m.polynomial_digest(generic_p12)}"
    )
    for index, ((key, _, _), source, generic) in enumerate(
        zip(total_first, total_sources, generic_sources)
    ):
        source_lines.append(
            f"FIRST\t{index}\t{key!r}\t{full_digest(source)}\t"
            f"{m.polynomial_digest(generic)}"
        )
    source_text = "\n".join(source_lines) + "\n"
    source_path = outdir / "TOTAL_F_ALLQ_SOURCE_INVENTORY.tsv"
    source_path.write_text(source_text)
    source_sha = sha256(source_text.encode()).hexdigest()

    h_lines = [
        "generator\tparameter_terms\tcoefficient_terms\tfull_sha256"
    ]
    h_lines.append(
        f"F\t{len(h_f)}\t{len(h_f)}\t{full_digest(embed(h_f))}"
    )
    for exponent in Q_EXPONENTS:
        quotient = h_q[exponent]
        h_lines.append(
            f"q{exponent}\t{len(quotient)}\t"
            f"{coefficient_term_count(quotient)}\t{full_digest(quotient)}"
        )
    h_text = "\n".join(h_lines) + "\n"
    h_path = outdir / "TOTAL_F_ALLQ_H_INVENTORY.tsv"
    h_path.write_text(h_text)
    h_sha = sha256(h_text.encode()).hexdigest()

    result_lines = [
        f"v86_parent_sha256={V86_SHA256}",
        f"v85_parent_sha256={v86.V85_SHA256}",
        f"generic_parent_sha256={v85.TARGET_SHA256}",
        f"special_certificate_sha256={v85.CERTIFICATE_SHA256}",
        "q_exponents=" + ",".join(map(str, Q_EXPONENTS)),
        f"target={TOTAL_TARGET}",
        f"common={common}",
        f"total_p12_sha256={full_digest(total_p12)}",
        f"hF_sha256={full_digest(embed(h_f))}",
        f"source_inventory_sha256={source_sha}",
        f"h_inventory_sha256={h_sha}",
        f"omission_inventory_sha256={omission_sha}",
    ]
    result_text = "\n".join(result_lines) + "\n"
    result_path = outdir / "TOTAL_F_ALLQ_EXACT_RESULT.txt"
    result_path.write_text(result_text)
    print(f"source_inventory_sha256={source_sha}")
    print(f"h_inventory_sha256={h_sha}")
    print(f"omission_inventory_sha256={omission_sha}")
    print(f"exact_result_sha256={sha256(result_text.encode()).hexdigest()}")
    print("positive_F_and_all_licensed_q_arcs_on_this_slice_excluded=true")
    print("q15_totalized=false")
    print("other_dead_correction_orbit_pole_center_boundary_totalized=false")
    print("whole_fixed_A3_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-V87TFAQ-LITERAL-TOTAL-F-ALLQ-RAW-P12-SOURCE PASS")
    v85.restore_base_qd_state()


if __name__ == "__main__":
    main()
