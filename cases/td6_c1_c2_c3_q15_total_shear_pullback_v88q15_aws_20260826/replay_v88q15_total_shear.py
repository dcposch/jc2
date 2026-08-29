#!/usr/bin/env python3
"""Exact total q15 target-shear pullback of frozen TD6 V87.

Substantive execution is AWS-gated.  The client proves the full coefficient
map and original transport compatibility before checking raw FIRST/P12
invariance over an untruncated 23-variable exact polynomial ring.
"""

from ast import literal_eval
import csv
from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
V87_PATH = HERE / "replay_v87tfaq_total_f_allq.py"
V87_SHA256 = "7c0890abbce996a221f9389372fa3705742d6ecd72531891bfeb5dfc2f1b9463"
V87_SOURCE_INVENTORY = HERE / "V87_TOTAL_F_ALLQ_SOURCE_INVENTORY.tsv"
V87_SOURCE_INVENTORY_SHA256 = (
    "079447d97638f18b7807cdd84b1178f9969d3f93727c7ab40588079586160a68"
)
V87_EXACT_RESULT = HERE / "V87_TOTAL_F_ALLQ_EXACT_RESULT.txt"
V87_EXACT_RESULT_SHA256 = (
    "5b27705017fce762b8622f32978dfbd6d13bcb75c1ffe2b85e156c003f94f570"
)
V87_RESULT = HERE / "V87_RESULT.md"
V87_RESULT_SHA256 = (
    "6e22c6ac16f9e164b760367cf65b970649e9235f185e8ec82f8e28dbd6859bda"
)
V87_FREEZE = HERE / "V87_FREEZE.sha256"
V87_FREEZE_SHA256 = (
    "ef39fef7983ed3251bc21b3dd4f53db075f816cd95ffb7a38511956d7d9c60b9"
)

for path, expected in (
    (V87_PATH, V87_SHA256),
    (V87_SOURCE_INVENTORY, V87_SOURCE_INVENTORY_SHA256),
    (V87_EXACT_RESULT, V87_EXACT_RESULT_SHA256),
    (V87_RESULT, V87_RESULT_SHA256),
    (V87_FREEZE, V87_FREEZE_SHA256),
):
    assert sha256(path.read_bytes()).hexdigest() == expected, path

assert os.environ.get("AWS_RUN_TAG", "").startswith(
    "td6_v88q15_total_shear_"
)
assert os.environ.get("TD6_Q_EXPONENT") == "2"
assert os.environ.get("TD6_PIVOT_POLICY") == "ascending"
assert os.environ.get("TD6_PIVOT_SCOPE") == "all-staged"

spec = importlib.util.spec_from_file_location("td6_v88_v87_parent", V87_PATH)
v87 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = v87
spec.loader.exec_module(v87)

v86, v85, m = v87.v86, v87.v85, v87.m
E3, Rat3 = v87.E3, v87.Rat3
C, V, U = v87.C, v87.V, v87.U
F, H, B3 = v87.F, v87.H, v87.B3
TRANSVERSE = tuple(list(range(2, 15)) + list(range(16, 25)))
ALL_Q = tuple(range(2, 25))
Q_ORDER = {exponent: index for index, exponent in enumerate(ALL_Q)}
assert len(TRANSVERSE) == 22 and len(ALL_Q) == 23 and 15 not in TRANSVERSE


class Q23:
    """Sparse exact E3[q2,...,q24], without a degree cutoff."""

    __slots__ = ("coefficients",)

    def __init__(self, value=0, coefficients=None):
        if isinstance(value, Q23):
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
        return value if isinstance(value, Q23) else Q23(value)

    @staticmethod
    def variable(exponent, coefficient=1):
        assert exponent in Q_ORDER
        return Q23(0, {(exponent,): E3.coerce(coefficient)})

    def constant(self):
        return self.coefficients.get((), E3())

    def __add__(self, other):
        other = Q23.coerce(other)
        return Q23(self, other.coefficients)

    __radd__ = __add__

    def __neg__(self):
        return Q23(0, {
            monomial: -coefficient
            for monomial, coefficient in self.coefficients.items()
        })

    def __sub__(self, other):
        return self + (-Q23.coerce(other))

    def __rsub__(self, other):
        return Q23.coerce(other) - self

    def __mul__(self, other):
        other = Q23.coerce(other)
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
        return Q23(0, out)

    __rmul__ = __mul__

    def inverse(self):
        assert set(self.coefficients).issubset({()}), (
            "attempted_q23_polynomial_inverse", tuple(self.coefficients)
        )
        constant = self.constant()
        if not constant:
            raise ZeroDivisionError("zero q23 polynomial constant")
        return Q23(constant.inverse())

    def __truediv__(self, other):
        return self * Q23.coerce(other).inverse()

    def __rtruediv__(self, other):
        return Q23.coerce(other) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base = Q23(1), self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return bool(self.coefficients)

    def __eq__(self, other):
        return self.coefficients == Q23.coerce(other).coefficients

    def __repr__(self):
        return "Q23(" + repr(sorted(self.coefficients.items())) + ")"


def lift22(value):
    value = v87.QPoly.coerce(value)
    return Q23(0, value.coefficients)


def lift_form(form):
    constant, row = form
    return (
        lift22(constant),
        {variable: lift22(value) for variable, value in row.items()},
    )


def add_form(left, right, coefficient=1):
    coefficient = Q23.coerce(coefficient)
    lc, lr = left
    rc, rr = right
    out = dict(lr)
    for variable, value in rr.items():
        total = out.get(variable, Q23()) + coefficient*value
        if total:
            out[variable] = total
        else:
            out.pop(variable, None)
    return lc + coefficient*rc, out


def zero_form():
    return Q23(), {}


def configure_qd(include_b):
    qd = m.r.qd
    qd.Dual = Q23
    qd.B = Q23.variable(2)
    qd.S = Q23(E3(qd.uniform.S_FIELD))
    qd.D = Q23(E3(qd.uniform.D_FIELD))
    qd.L = Q23(E3(qd.uniform.L_FIELD))
    qd.A = Q23(E3(qd.uniform.A_FIELD))
    qd.Q_PRIME = {0: Q23(1), 24: Q23(25)}
    for exponent in TRANSVERSE:
        qd.Q_PRIME[exponent - 1] = Q23.variable(exponent, exponent)
    if include_b:
        qd.Q_PRIME[14] = Q23.variable(15, 15)
    qd.R = qd.multiply(
        qd.multiply([Q23(-1), Q23(1)], [Q23(-1), Q23(1)]),
        [qd.D, -qd.S, Q23(1)],
    )
    qd.R3, qd.R5 = qd.power(qd.R, 3), qd.power(qd.R, 5)
    qd.POLE_F = {1: -(qd.L**3)*qd.A, 6: qd.L**3}
    qd.POLE_G = {
        0: Q23(m.r.b.Q(5, 9))*qd.L**5*qd.A**2,
        5: Q23(m.r.b.Q(-5, 3))*qd.L**5*qd.A,
        10: qd.L**5,
    }


def clean(polynomial):
    return {
        monomial: Q23.coerce(value)
        for monomial, value in polynomial.items() if value
    }


def source_polynomial(row, rhs):
    return v86.source_polynomial(row, rhs)


def compile_first(bands, include_b):
    configure_qd(include_b)
    return m.r.qd.pack(
        "X-2", m.r.qd.first_band_polynomials(
            bands[("f", 1)], bands[("g", 1)]
        )
    )


def compile_p12(bands, include_b):
    configure_qd(include_b)
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
        multiplier = qd.Q_PRIME.get(degree - i, Q23())
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
    return clean(equation)


def family_map(rows):
    return {key: source_polynomial(row, rhs) for key, row, rhs in rows}


def full_digest(polynomial):
    lines = []
    for parameter_monomial, value in sorted(polynomial.items()):
        for q_monomial, coefficient in sorted(value.coefficients.items()):
            lines.append(
                f"{parameter_monomial!r}\t{q_monomial!r}\t"
                f"{m.e3_exact(coefficient)}"
            )
    return sha256(("\n".join(lines) + "\n").encode()).hexdigest()


def omission_record(full, omitted):
    keys = sorted(set(full) | set(omitted))
    changed = [key for key in keys if full.get(key, {}) != omitted.get(key, {})]
    assert changed
    digest = sha256()
    for key in changed:
        digest.update(key.__repr__().encode())
        digest.update(full_digest(full.get(key, {})).encode())
        digest.update(full_digest(omitted.get(key, {})).encode())
    return len(changed), changed[0], digest.hexdigest()


def read_v87_inventory():
    p12 = None
    first = {}
    with V87_SOURCE_INVENTORY.open(newline="") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row["kind"] == "P12":
                assert p12 is None and int(row["index"]) == 12
                p12 = row["full_sha256"]
            else:
                assert row["kind"] == "FIRST"
                index = int(row["index"])
                assert literal_eval(row["key"]) == ("X-2", index)
                first[index] = row["full_sha256"]
    assert p12 and set(first) == set(range(38))
    return p12, first


def transport_row_audit(outdir):
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
    assert nf == 16*61 == 976
    assert ng == 26*101 == 2626
    f_rows = {}
    for key, row, rhs in rows_f:
        assert key not in f_rows
        f_rows[key] = (row, rhs)
    lines = [
        "index\tkey\tg_terms\tshared_terms\tf_terms\tshared_equals_f"
        "\tf_rhs_nonzero"
    ]
    nonzero_extra = []
    for index, (key, row, _) in enumerate(rows_g):
        shared = {}
        for variable, coefficient in row.items():
            i, j = divmod(variable, 101)
            if i <= 15 and j <= 60:
                shared[i*61 + j] = coefficient
        f_row, f_rhs = f_rows.get(key, ({}, m.r.b.Q(0)))
        assert shared == f_row, (key, len(shared), len(f_row))
        if f_rhs:
            nonzero_extra.append((key, f_rhs))
        lines.append(
            f"{index}\t{key!r}\t{len(row)}\t{len(shared)}\t{len(f_row)}"
            f"\ttrue\t{str(bool(f_rhs)).lower()}"
        )
    assert nonzero_extra == [(('X', 0, 15), m.r.b.Q(1))], nonzero_extra
    text = "\n".join(lines) + "\n"
    path = outdir / "Q15_TRANSPORT_ROW_AUDIT.tsv"
    path.write_text(text)
    return nf, ng, len(rows_f), len(rows_g), sha256(text.encode()).hexdigest()


def coefficient_map_inventory(outdir):
    lines = ["i\tj\tf_index\tg_index\tforward\tinverse"]
    seen_f, seen_g = set(), set()
    for i in range(16):
        for j in range(61):
            f_index = i*61 + j
            g_index = i*101 + j
            assert f_index not in seen_f and g_index not in seen_g
            seen_f.add(f_index)
            seen_g.add(g_index)
            lines.append(
                f"{i}\t{j}\t{f_index}\t{g_index}\t"
                "g_raw=g_bar+b*f_bar\tg_bar=g_raw-b*f_raw"
            )
    assert len(seen_f) == len(seen_g) == 976
    text = "\n".join(lines) + "\n"
    path = outdir / "Q15_COEFFICIENT_MAP.tsv"
    path.write_text(text)
    return sha256(text.encode()).hexdigest()


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    print("producer=TD6-V88Q15-EXACT-TOTAL-TARGET-SHEAR-PULLBACK")
    print("q_ring=untruncated_sparse_multivariate_E3_q2_through_q24")
    print("q15_symbol=b")
    print("q15_not_inverted=true")
    print("map=q_raw=q_bar+b*p;f_raw=f_bar;g_raw=g_bar+b*f_bar")
    print("inverse=q_bar=q_raw-b*p;f_bar=f_raw;g_bar=g_raw-b*f_raw")
    print("coordinate_map_triangular_jacobian_one=true", flush=True)

    map_sha = coefficient_map_inventory(outdir)
    nf, ng, f_rows, g_rows, transport_sha = transport_row_audit(outdir)
    print(f"global_f_coefficient_count={nf}")
    print(f"global_g_coefficient_count={ng}")
    print(f"global_total_coefficient_count={nf+ng}")
    print("shared_f_to_g_monomial_count=976")
    print("coefficient_map_two_sided_exact=true")
    print(f"original_f_transport_row_count={f_rows}")
    print(f"original_g_transport_row_count={g_rows}")
    print("all_original_g_shared_rows_equal_corresponding_f_rows=true")
    print("unique_induced_q15_boundary_key=('g','X',0,15)")
    print("q15_transport_rhs_omission_negative_control=true", flush=True)

    # Build the frozen 22-q normalized source before replacing its coefficient
    # type.  Then embed it faithfully in the larger 23-variable ring.
    v86.BPoly = v87.QPoly
    event_count, bands22, seen = v87.build_bands()
    assert event_count == 2 and set(seen.values()) == {1}
    bands_bar = {
        key: [lift_form(form) for form in forms]
        for key, forms in bands22.items()
    }
    del bands22
    v86.BPoly = Q23
    b = Q23.variable(15)
    bands_raw = {}
    for power in (1, 2, 3):
        bands_raw[("f", power)] = list(bands_bar[("f", power)])
        f_forms = bands_bar[("f", power)]
        bands_raw[("g", power)] = [
            add_form(
                form,
                f_forms[degree] if degree < len(f_forms) else zero_form(),
                b,
            )
            for degree, form in enumerate(bands_bar[("g", power)])
        ]
        for degree, raw_form in enumerate(bands_raw[("g", power)]):
            recovered = add_form(
                raw_form,
                f_forms[degree] if degree < len(f_forms) else zero_form(),
                -b,
            )
            assert recovered == bands_bar[("g", power)][degree]
    print("all_transported_band_coordinate_maps_two_sided_exact=true", flush=True)

    norm_first_rows = compile_first(bands_bar, False)
    norm_p12 = compile_p12(bands_bar, False)
    raw_first_rows = compile_first(bands_raw, True)
    raw_p12 = compile_p12(bands_raw, True)
    norm_first = family_map(norm_first_rows)
    raw_first = family_map(raw_first_rows)
    assert raw_first == norm_first
    assert raw_p12 == norm_p12
    assert len(norm_first) == 38 and len(norm_p12) == 2893
    assert all(
        15 not in q_monomial
        for polynomial in [raw_p12, *raw_first.values()]
        for value in polynomial.values()
        for q_monomial in value.coefficients
    )
    print("all_38_raw_FIRST_exactly_target_shear_invariant=true")
    print("literal_raw_P12_exactly_target_shear_invariant=true")
    print("raw_source_q15_degree=0", flush=True)

    direct_only = family_map(compile_first(bands_bar, True))
    shear_only = family_map(compile_first(bands_raw, False))
    direct_record = omission_record(raw_first, direct_only)
    shear_record = omission_record(raw_first, shear_only)
    print(
        f"section_shear_omission=changed:{direct_record[0]};"
        f"first:{direct_record[1]!r};sha256:{direct_record[2]}"
    )
    print(
        f"direct_q15_omission=changed:{shear_record[0]};"
        f"first:{shear_record[1]!r};sha256:{shear_record[2]}"
    )
    print("both_q15_receiver_omission_controls=true", flush=True)

    expected_p12, expected_first = read_v87_inventory()
    assert full_digest(norm_p12) == expected_p12
    source_lines = ["kind\tindex\tkey\tnormalized_sha256\traw_sha256"]
    source_lines.append(
        f"P12\t12\t{('X0_RAW', 12)!r}\t{full_digest(norm_p12)}\t"
        f"{full_digest(raw_p12)}"
    )
    for index, key in enumerate(sorted(norm_first)):
        assert key == ("X-2", index)
        nd = full_digest(norm_first[key])
        rd = full_digest(raw_first[key])
        assert nd == rd == expected_first[index]
        source_lines.append(f"FIRST\t{index}\t{key!r}\t{nd}\t{rd}")
    source_text = "\n".join(source_lines) + "\n"
    source_path = outdir / "Q15_SOURCE_INVARIANCE.tsv"
    source_path.write_text(source_text)
    source_sha = sha256(source_text.encode()).hexdigest()
    print("b_zero_and_full_pullback_match_frozen_V87_source_inventory=true")

    source_coefficients = [
        coefficient
        for polynomial in [raw_p12, *raw_first.values()]
        for value in polynomial.values()
        for coefficient in value.coefficients.values()
    ]
    common = v85.monic(m.denominator_for(source_coefficients))
    assert v85.factors_allowed(common)
    assert common.gcd(F).total_degree() == 0
    print(f"audited_raw_source_E3_coefficient_count={len(source_coefficients)}")
    print(f"raw_source_common_denominator=({common})")
    print(f"raw_source_common_denominator_factor={common.factor()}")
    print("raw_source_denominator_radical_subset_U_H_B3=true")
    print("target_shear_map_introduces_no_denominator=true", flush=True)

    result_lines = [
        f"v87_client_sha256={V87_SHA256}",
        f"v87_result_sha256={V87_RESULT_SHA256}",
        f"v87_freeze_sha256={V87_FREEZE_SHA256}",
        f"v87_source_inventory_sha256={V87_SOURCE_INVENTORY_SHA256}",
        f"v87_exact_result_sha256={V87_EXACT_RESULT_SHA256}",
        f"coefficient_map_sha256={map_sha}",
        f"transport_row_audit_sha256={transport_sha}",
        f"source_invariance_sha256={source_sha}",
        f"raw_source_common_denominator={common}",
        "q15_pullback_remainder=0",
    ]
    result_text = "\n".join(result_lines) + "\n"
    result_path = outdir / "Q15_EXACT_RESULT.txt"
    result_path.write_text(result_text)
    result_sha = sha256(result_text.encode()).hexdigest()
    print(f"coefficient_map_sha256={map_sha}")
    print(f"transport_row_audit_sha256={transport_sha}")
    print(f"source_invariance_sha256={source_sha}")
    print(f"exact_result_sha256={result_sha}")
    print("frozen_V87_identity_pulls_back_with_q15_remainder_zero=true")
    print("q15_arbitrary_including_unit_on_this_fixed_p_component=true")
    print("other_22_transverse_unit_q_charts_covered=false")
    print("dead_correction_pole_center_deck_torsion_boundary_covered=false")
    print("whole_fixed_A3_killed=false")
    print("whole_TD6_killed=false")
    print("SP2_killed=false")
    print("JC2_resolved=false")
    print("TD6-V88Q15-EXACT-TOTAL-TARGET-SHEAR-PULLBACK PASS")


if __name__ == "__main__":
    main()
