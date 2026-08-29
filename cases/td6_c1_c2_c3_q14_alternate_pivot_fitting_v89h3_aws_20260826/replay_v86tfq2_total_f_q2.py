#!/usr/bin/env python3
"""Literal total-(F,q2) lift of the raw P12/FIRST certificate.

Substantive execution is AWS-gated by the wrapper.  The beta coefficient
ring is sparse and untruncated.  The client imports the frozen V85TF1 source
custodian, rebuilds the affine transport beta path and the direct q-prime
path, and emits

    s = aP*P12 + sum ai*FIRST_i + F*hF + beta*hbeta.
"""

from hashlib import sha256
import importlib.util
import csv
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
V85_PATH = HERE / "replay_v85tf1_total_f.py"
V85_SHA256 = "ab9753073d694242d4359dc1edc86774724f62d28d15b7c671ba0b796262100e"
assert sha256(V85_PATH.read_bytes()).hexdigest() == V85_SHA256
spec = importlib.util.spec_from_file_location("td6_v86tfq2_v85_parent", V85_PATH)
v85 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = v85
spec.loader.exec_module(v85)

m = v85.m
E3, Rat3 = v85.E3, v85.Rat3
C, V, U = v85.C, v85.V, v85.U
F, H, B3 = v85.F, v85.H, v85.B3
TOTAL_TARGET = v85.TOTAL_TARGET
ALLOWED = v85.ALLOWED
EXPECTED_V85_H_SHA256 = (
    "7434b0a7434288e421ad300e93c5da8084f69f19a801298ec6ec05bf9b85bb70"
)
V85_INVENTORY = HERE / "V85_TOTAL_F_SOURCE_INVENTORY.tsv"
V85_INVENTORY_SHA256 = (
    "9a612bb64ee974a506a1f3b7fcb471fb8924220ca6d24320af0fc9b8a7de6b7a"
)
assert sha256(V85_INVENTORY.read_bytes()).hexdigest() == V85_INVENTORY_SHA256


class BPoly:
    """Sparse exact E3[beta], with no degree cutoff."""

    __slots__ = ("coefficients",)

    def __init__(self, value=0, coefficients=None):
        if isinstance(value, BPoly):
            data = dict(value.coefficients)
        else:
            coefficient = E3.coerce(value)
            data = {0: coefficient} if coefficient else {}
        if coefficients:
            for degree, coefficient in coefficients.items():
                assert isinstance(degree, int) and degree >= 0
                coefficient = E3.coerce(coefficient)
                total = data.get(degree, E3()) + coefficient
                if total:
                    data[degree] = total
                else:
                    data.pop(degree, None)
        self.coefficients = data

    @staticmethod
    def coerce(value):
        return value if isinstance(value, BPoly) else BPoly(value)

    @staticmethod
    def beta(coefficient=1):
        return BPoly(0, {1: E3.coerce(coefficient)})

    def constant(self):
        return self.coefficients.get(0, E3())

    def positive(self):
        return BPoly(0, {
            degree: coefficient
            for degree, coefficient in self.coefficients.items()
            if degree > 0
        })

    def __add__(self, other):
        other = BPoly.coerce(other)
        return BPoly(self, other.coefficients)

    __radd__ = __add__

    def __neg__(self):
        return BPoly(0, {
            degree: -coefficient
            for degree, coefficient in self.coefficients.items()
        })

    def __sub__(self, other):
        return self + (-BPoly.coerce(other))

    def __rsub__(self, other):
        return BPoly.coerce(other) - self

    def __mul__(self, other):
        other = BPoly.coerce(other)
        out = {}
        for left_degree, left in self.coefficients.items():
            for right_degree, right in other.coefficients.items():
                degree = left_degree + right_degree
                total = out.get(degree, E3()) + left*right
                if total:
                    out[degree] = total
                else:
                    out.pop(degree, None)
        return BPoly(0, out)

    __rmul__ = __mul__

    def inverse(self):
        # The raw compiler is polynomial in beta.  Any nonconstant inversion
        # is a forbidden hidden beta localization.
        assert set(self.coefficients).issubset({0}), (
            "attempted_beta_polynomial_inverse", self.coefficients.keys()
        )
        constant = self.constant()
        if not constant:
            raise ZeroDivisionError("zero beta-polynomial constant")
        return BPoly(constant.inverse())

    def __truediv__(self, other):
        return self * BPoly.coerce(other).inverse()

    def __rtruediv__(self, other):
        return BPoly.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base = BPoly(1), self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.coefficients)

    def __eq__(self, other):
        return self.coefficients == BPoly.coerce(other).coefficients

    def __repr__(self):
        return "BPoly(" + repr(sorted(self.coefficients.items())) + ")"


def clean(polynomial):
    return {
        monomial: BPoly.coerce(coefficient)
        for monomial, coefficient in polynomial.items()
        if BPoly.coerce(coefficient)
    }


def add(left, right, coefficient=1):
    coefficient = BPoly.coerce(coefficient)
    out = dict(left)
    for monomial, value in right.items():
        total = out.get(monomial, BPoly()) + coefficient*BPoly.coerce(value)
        if total:
            out[monomial] = total
        else:
            out.pop(monomial, None)
    return out


def scale(polynomial, coefficient):
    coefficient = BPoly.coerce(coefficient)
    return clean({
        monomial: coefficient*BPoly.coerce(value)
        for monomial, value in polynomial.items()
    })


def multiply(left, right):
    out = {}
    for left_monomial, left_value in left.items():
        for right_monomial, right_value in right.items():
            monomial = tuple(sorted(left_monomial + right_monomial))
            total = (
                out.get(monomial, BPoly())
                + BPoly.coerce(left_value)*BPoly.coerce(right_value)
            )
            if total:
                out[monomial] = total
            else:
                out.pop(monomial, None)
    return out


def embed(polynomial):
    return clean({monomial: BPoly(value) for monomial, value in polynomial.items()})


def beta_coefficient(polynomial, degree):
    return {
        monomial: value.coefficients[degree]
        for monomial, value in polynomial.items()
        if degree in value.coefficients and value.coefficients[degree]
    }


def max_beta_degree(polynomials):
    return max(
        (
            degree
            for polynomial in polynomials
            for value in polynomial.values()
            for degree in BPoly.coerce(value).coefficients
        ),
        default=0,
    )


def divide_by_beta(polynomial):
    out = {}
    count = 0
    for monomial, value in polynomial.items():
        assert not value.constant(), ("beta_nondivisible", monomial)
        shifted = {
            degree - 1: coefficient
            for degree, coefficient in value.coefficients.items()
        }
        assert all(degree >= 0 for degree in shifted)
        out[monomial] = BPoly(0, shifted)
        count += len(shifted)
    quotient = clean(out)
    assert scale(quotient, BPoly.beta()) == clean(polynomial)
    return quotient, count


def source_polynomial(row, rhs):
    out = {(): -BPoly.coerce(rhs)} if rhs else {}
    for variable, coefficient in row.items():
        coefficient = BPoly.coerce(coefficient)
        if coefficient:
            out[(variable,)] = coefficient
    return out


def source_value(key, include_transport_beta):
    value = BPoly(m.from_vector(m.r.t.source_vector(key)))
    if include_transport_beta and key == ("g", "X", 0, 2):
        value += BPoly.beta(E3(1))
    return value


def propagate_beta(rows, records, include_transport_beta):
    pivot_rhs, compatibility = {}, []
    for source_row, record in zip(rows, records):
        source_key, _, _ = source_row
        key, kind, pivot, lead, factors = record
        assert source_key == key
        value = source_value(key, include_transport_beta)
        for old, factor in factors:
            value -= BPoly(m.scalar(factor))*pivot_rhs[old]
        if kind == "pivot":
            pivot_rhs[pivot] = BPoly(m.scalar(lead.inverse()))*value
        elif value:
            compatibility.append((key, value))
    return pivot_rhs, compatibility


def restrict_row(original_row, pivots, pivot_rhs, free_parameter):
    row = {
        variable: Rat3.coerce(coefficient)
        for variable, coefficient in original_row.items() if coefficient
    }
    constant = BPoly()
    # This producer is frozen to the ascending transport policy.  The raw
    # trivariate pivot dictionary need not itself be inserted in variable
    # order, so reduce by sorted variable index exactly as the reviewed q2
    # beta client does.  Reverse/sparse policies require their separate
    # insertion-order DAG and are outside this client.
    for pivot in sorted(pivots):
        factor = row.pop(pivot, None)
        if factor is None or not factor:
            continue
        constant += BPoly(m.scalar(factor))*pivot_rhs[pivot]
        for variable, coefficient in pivots[pivot].items():
            if variable == pivot:
                continue
            value = row.get(variable, Rat3()) - factor*coefficient
            if value:
                row[variable] = value
            else:
                row.pop(variable, None)
    assert all(variable in free_parameter for variable in row)
    return (
        constant,
        {
            free_parameter[variable]: BPoly(m.scalar(coefficient))
            for variable, coefficient in row.items()
        },
    )


def strip_beta_bands(bands):
    return {
        key: [
            (
                BPoly(constant.constant()),
                {
                    variable: BPoly(coefficient.constant())
                    for variable, coefficient in row.items()
                    if coefficient.constant()
                },
            )
            for constant, row in forms
        ]
        for key, forms in bands.items()
    }


def configure_qd(include_direct_qprime):
    qd = m.r.qd
    qd.Dual = BPoly
    qd.B = BPoly.beta()
    qd.S = BPoly(E3(qd.uniform.S_FIELD))
    qd.D = BPoly(E3(qd.uniform.D_FIELD))
    qd.L = BPoly(E3(qd.uniform.L_FIELD))
    qd.A = BPoly(E3(qd.uniform.A_FIELD))
    qd.Q_PRIME = {0: BPoly(1), 24: BPoly(25)}
    if include_direct_qprime:
        qd.Q_PRIME[1] = BPoly.beta(2)
    qd.R = qd.multiply(
        qd.multiply([BPoly(-1), BPoly(1)], [BPoly(-1), BPoly(1)]),
        [qd.D, -qd.S, BPoly(1)],
    )
    qd.R3, qd.R5 = qd.power(qd.R, 3), qd.power(qd.R, 5)
    qd.POLE_F = {1: -(qd.L**3)*qd.A, 6: qd.L**3}
    qd.POLE_G = {
        0: BPoly(m.r.b.Q(5, 9))*qd.L**5*qd.A**2,
        5: BPoly(m.r.b.Q(-5, 3))*qd.L**5*qd.A,
        10: qd.L**5,
    }


def compile_first(bands, include_direct_qprime):
    configure_qd(include_direct_qprime)
    return m.r.qd.pack(
        "X-2", m.r.qd.first_band_polynomials(
            bands[("f", 1)], bands[("g", 1)]
        )
    )


def compile_source(bands, include_direct_qprime):
    first = compile_first(bands, include_direct_qprime)
    raw = m.r.qd.compile_current(
        *[bands[("f", power)] for power in (1, 2, 3)],
        *[bands[("g", power)] for power in (1, 2, 3)],
    )[12]
    p12 = clean({monomial: BPoly.coerce(value) for monomial, value in raw.items()})
    return first, p12


def build_total_source():
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
    pivot_rhs, compatibility = propagate_beta(ordered, records, True)
    assert not compatibility and len(pivots) == 3470
    free = [variable for variable in range(nf + ng) if variable not in pivots]
    assert len(free) == 132
    free_parameter = {variable: index for index, variable in enumerate(free)}

    def restrict(row):
        return restrict_row(row, pivots, pivot_rhs, free_parameter)

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
    first, p12 = compile_source(bands, True)
    first_no_direct = compile_first(bands, False)
    first_no_transport = compile_first(
        strip_beta_bands(bands), True
    )
    v85.restore_base_qd_state()
    return (
        len(events), bands, first, p12,
        first_no_direct, first_no_transport,
    )


def full_digest(polynomial):
    lines = []
    for monomial, value in sorted(polynomial.items()):
        for degree, coefficient in sorted(value.coefficients.items()):
            lines.append(f"{monomial!r}\t{degree}\t{m.e3_exact(coefficient)}")
    return sha256(("\n".join(lines) + "\n").encode()).hexdigest()


def all_coefficients(polynomials):
    for polynomial in polynomials:
        for value in polynomial.values():
            yield from BPoly.coerce(value).coefficients.values()


def assert_denominators_allowed(polynomials):
    coefficients = list(all_coefficients(polynomials))
    common = v85.monic(m.denominator_for(coefficients))
    assert v85.factors_allowed(common), common.factor()
    assert common.gcd(F).total_degree() == 0
    return coefficients, common


def assert_polynomial_coefficients(polynomials):
    count = 0
    for coefficient in all_coefficients(polynomials):
        for coordinate in m.r.scalar_coordinates(coefficient):
            count += 1
            assert coordinate.denominator == m.tri.ONE
    return count


def serialize(path, polynomial):
    lines = ["parameter_monomial\tbeta_degree\tcoefficient_exact"]
    for monomial, value in sorted(polynomial.items()):
        for degree, coefficient in sorted(value.coefficients.items()):
            lines.append(f"{monomial!r}\t{degree}\t{m.e3_exact(coefficient)}")
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest(), len(lines) - 1


def read_v85_inventory():
    p12_digest = None
    first_digests = {}
    with V85_INVENTORY.open(newline="") as handle:
        rows = csv.DictReader(handle, delimiter="\t")
        assert rows.fieldnames == [
            "kind", "index", "key", "generic_sha256", "special_sha256"
        ]
        for record in rows:
            kind = record["kind"]
            index = int(record["index"])
            if kind == "P12":
                assert index == 12 and p12_digest is None
                p12_digest = record["generic_sha256"]
            else:
                assert kind == "FIRST" and index not in first_digests
                first_digests[index] = record["generic_sha256"]
    assert p12_digest and set(first_digests) == set(range(38))
    return p12_digest, first_digests


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    print("producer=TD6-V86TFQ2-LITERAL-TOTAL-F-Q2-RAW-P12-SOURCE")
    print("q_parameter=beta")
    print("q_beta=t+beta*t^2+t^25")
    print("q_beta_prime=1+2*beta*t+25*t^24")
    print("beta_ring=untruncated_sparse_E3[beta]")
    print("total_ring=Q[C,V,U,beta] localized at U*H*B3")
    print("staged_CURRENT_used=false")
    print("PREVIOUS_POLE_used=false", flush=True)

    (
        event_count, bands, total_first, total_p12,
        first_no_direct, first_no_transport,
    ) = build_total_source()
    del bands
    total_sources = [source_polynomial(row, rhs) for _, row, rhs in total_first]
    no_direct_sources = [
        source_polynomial(row, rhs) for _, row, rhs in first_no_direct
    ]
    no_transport_sources = [
        source_polynomial(row, rhs) for _, row, rhs in first_no_transport
    ]
    assert total_sources != no_direct_sources
    assert total_sources != no_transport_sources
    print(f"transport_event_count={event_count}")
    print("transport_beta_rhs_retained=true")
    print("direct_qprime_beta_retained=true")
    print("transport_beta_omission_negative_control=true")
    print("direct_qprime_omission_negative_control=true", flush=True)

    generic_p12 = beta_coefficient(total_p12, 0)
    generic_sources = [beta_coefficient(source, 0) for source in total_sources]
    special_p12 = v85.specialize_polynomial(generic_p12)
    special_sources = [
        v85.specialize_polynomial(source) for source in generic_sources
    ]
    assert len(total_first) == len(generic_sources) == len(special_sources) == 38
    assert len(generic_p12) == len(special_p12) == 2893
    v85_p12_digest, v85_first_digests = read_v85_inventory()
    assert m.polynomial_digest(generic_p12) == v85_p12_digest
    for index, source in enumerate(generic_sources):
        assert m.polynomial_digest(source) == v85_first_digests[index]
    print("beta_zero_raw_FIRST_matches_frozen_V85_inventory=true")
    print("beta_zero_raw_P12_matches_frozen_V85_inventory=true")
    print("F_beta_zero_raw_source_matches_V82QST3=true", flush=True)

    labels = set()
    for polynomial in [total_p12, *total_sources]:
        for monomial in polynomial:
            labels.update(monomial)
    assert labels == set(range(132))
    print("all_132_transport_free_section_coordinates_retained=true")

    p12_multiplier, first_multipliers, used_keys = (
        v85.read_frozen_multipliers(total_first)
    )
    bp_p12_multiplier = embed(p12_multiplier)
    bp_first_multipliers = [embed(value) for value in first_multipliers]
    special_identity = v85.multiply(p12_multiplier, special_p12)
    for multiplier, source in zip(first_multipliers, special_sources):
        if multiplier:
            special_identity = v85.add(
                special_identity, v85.multiply(multiplier, source)
            )
    assert special_identity == {(): E3(Rat3(v85.SPECIAL_CLEARER))}
    print("frozen_V82QST3_special_identity_replayed=true")

    total_terms = [multiply(bp_p12_multiplier, total_p12)]
    total_identity = dict(total_terms[0])
    for multiplier, source in zip(bp_first_multipliers, total_sources):
        if multiplier:
            term = multiply(multiplier, source)
            total_terms.append(term)
            total_identity = add(total_identity, term)
    target = {(): BPoly(E3(Rat3(TOTAL_TARGET)))}
    residual = add(target, total_identity, -1)
    residual_beta_zero = beta_coefficient(residual, 0)
    h_f, f_division_count = v85.divide_polynomial_by_f(residual_beta_zero)
    assert m.polynomial_digest(h_f) == EXPECTED_V85_H_SHA256
    positive_residual = {
        monomial: value.positive()
        for monomial, value in residual.items() if value.positive()
    }
    h_beta, beta_division_count = divide_by_beta(positive_residual)
    rhs = add(total_identity, scale(embed(h_f), BPoly(E3(Rat3(F)))))
    rhs = add(rhs, scale(h_beta, BPoly.beta()))
    assert rhs == target
    print(f"total_residual_terms={len(residual)}")
    print(f"total_beta_degree={max_beta_degree([total_p12, *total_sources])}")
    print(f"residual_beta_degree={max_beta_degree([residual])}")
    print(f"F_division_coordinate_count={f_division_count}")
    print(f"beta_division_coefficient_count={beta_division_count}")
    print("V85_beta_zero_hF_hash_reproduced=true")
    print("F_beta_decomposition_exact=true")
    print("F_not_inverted=true")
    print("beta_not_inverted=true", flush=True)

    active_index = min(used_keys)
    active_term = multiply(
        bp_first_multipliers[active_index], total_sources[active_index]
    )
    correction = add(
        scale(embed(h_f), BPoly(E3(Rat3(F)))),
        scale(h_beta, BPoly.beta()),
    )
    assert add(add(total_identity, active_term, -1), correction) != target
    assert add(add(total_identity, total_terms[0], -1), correction) != target
    print(f"FIRST_omission_negative_control_index={active_index}")
    print("FIRST_omission_negative_control=true")
    print("P12_omission_negative_control=true")

    audited = [
        bp_p12_multiplier, *bp_first_multipliers,
        total_p12, *total_sources, *total_terms,
        embed(h_f), h_beta,
    ]
    coefficients, common = assert_denominators_allowed(audited)
    common_scalar = BPoly(E3(Rat3(common)))
    cleared = [scale(polynomial, common_scalar) for polynomial in audited]
    cleared_target = scale(target, common_scalar)
    cleared_rhs = scale(rhs, common_scalar)
    assert cleared_rhs == cleared_target
    polynomial_count = assert_polynomial_coefficients(cleared)
    print(f"audited_E3_coefficient_count={len(coefficients)}")
    print(f"total_family_common_denominator=({common})")
    print(f"total_family_common_denominator_factor={common.factor()}")
    print("denominator_radical_subset_U_H_B3=true")
    print(f"cleared_polynomial_scalar_coordinate_count={polynomial_count}")
    print("cleared_total_identity_exact=true")

    cleared_h_f = scale(embed(h_f), common_scalar)
    cleared_h_beta = scale(h_beta, common_scalar)
    h_f_path = outdir / "TOTAL_F_Q2_HF_CLEARED.tsv"
    h_beta_path = outdir / "TOTAL_F_Q2_HBETA_CLEARED.tsv"
    h_f_sha, h_f_terms = serialize(h_f_path, cleared_h_f)
    h_beta_sha, h_beta_terms = serialize(h_beta_path, cleared_h_beta)
    inventory_lines = ["kind\tindex\tkey\tfull_sha256\tbeta_zero_sha256"]
    inventory_lines.append(
        f"P12\t12\t('X0_RAW', 12)\t{full_digest(total_p12)}\t"
        f"{m.polynomial_digest(generic_p12)}"
    )
    for index, ((key, _, _), source, generic) in enumerate(
        zip(total_first, total_sources, generic_sources)
    ):
        inventory_lines.append(
            f"FIRST\t{index}\t{key!r}\t{full_digest(source)}\t"
            f"{m.polynomial_digest(generic)}"
        )
    inventory_text = "\n".join(inventory_lines) + "\n"
    inventory_path = outdir / "TOTAL_F_Q2_SOURCE_INVENTORY.tsv"
    inventory_path.write_text(inventory_text)
    inventory_sha = sha256(inventory_text.encode()).hexdigest()
    result_lines = [
        f"v85_parent_sha256={V85_SHA256}",
        f"generic_parent_sha256={v85.TARGET_SHA256}",
        f"special_certificate_sha256={v85.CERTIFICATE_SHA256}",
        f"target={TOTAL_TARGET}",
        f"common={common}",
        f"total_p12_sha256={full_digest(total_p12)}",
        f"hF_sha256={full_digest(embed(h_f))}",
        f"hbeta_sha256={full_digest(h_beta)}",
        f"cleared_hF_file_sha256={h_f_sha}",
        f"cleared_hbeta_file_sha256={h_beta_sha}",
        f"source_inventory_sha256={inventory_sha}",
    ]
    result_text = "\n".join(result_lines) + "\n"
    result_path = outdir / "TOTAL_F_Q2_EXACT_RESULT.txt"
    result_path.write_text(result_text)
    print(f"hF_cleared_terms={h_f_terms}")
    print(f"hF_cleared_sha256={h_f_sha}")
    print(f"hbeta_cleared_terms={h_beta_terms}")
    print(f"hbeta_cleared_sha256={h_beta_sha}")
    print(f"source_inventory_sha256={inventory_sha}")
    print(f"exact_result_sha256={sha256(result_text.encode()).hexdigest()}")
    print("positive_F_and_beta_arcs_on_this_slice_excluded=true")
    print("other_q_dead_correction_orbit_pole_center_boundary_totalized=false")
    print("whole_fixed_A3_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-V86TFQ2-LITERAL-TOTAL-F-Q2-RAW-P12-SOURCE PASS")


if __name__ == "__main__":
    main()
