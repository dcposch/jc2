#!/usr/bin/env python3
"""Explicit original-FIRST multipliers and total-F lift of P13 coordinate 12.

Stages 4 and 5 of the independent H19 design.  Every algebraic primitive is
imported from the frozen V85/V86/V87/H5/H6/H10/H10T/H11/H12/H15/H19R1 chain;
this client only composes them, polarizes the literal degree-13 parent against
the reconstructed original FIRST inverse, and clears denominators.
"""

import ast
from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent

REQUIRED_ENVIRONMENT = (
    ("TD6_Q_EXPONENT", "2"),
    ("TD6_Q_SCOPE", "q2-q14-q16-q24"),
    ("TD6_PIVOT_POLICY", "ascending"),
    ("TD6_PIVOT_SCOPE", "all-staged"),
    ("TD6_F_SPECIALIZATION", "exact-C-equals-V2-minus-U3-over-U"),
    ("OMP_NUM_THREADS", "1"),
    ("OPENBLAS_NUM_THREADS", "1"),
)
TAG_PREFIX = "td6_v89h19r2_p13_c12_first_total_"
FORBIDDEN_MODULES = ("sage", "sympy", "singular", "PySingular", "sage.all")

H19R1_PATH = HERE / "replay_v89h19r1_raw_p13_coordinate12_audit.py"
H19R1_SHA = "7919aa9d3a769e456abadd54eea12008b0a9121760b8382bbf8bdc72b3ec1784"
H19R1_MANIFEST = HERE / "SOURCE_RAW_P13_COORDINATE12_AUDIT_R1.sha256"
H15_ARCHIVE_SHA = (
    "2c13bd51601a64f3c2410bf4d36460f9f8741312aeef649299a22eb4fae3ff81"
)
PINNED_FILES = {
    "PREREGISTRATION_P13_COORDINATE12_ORIGINAL_FIRST_TOTAL_F.md":
        "7ecdeae31448e29f1b5ba102db58c2f180f32b9df07ffb831f6b15b06e65753a",
    "H19R2_V1_FORBIDDEN_MODULE_PROBE_ERRATUM.md":
        "19c30dc78f007235553c35c422185f697eec4c4c158b23d01036099210bdaf29",
    "run_v89h19r2_p13_coordinate12_original_first_total_f.sh":
        "db85757ab43afd15305a81550c2356a33a37f62696926318bf181c666d74b030",
    "SOURCE_RAW_P13_COORDINATE12_AUDIT_R1.sha256":
        "a60d6fdb1e503caad7861cf1acd7ebc22a39eaac3ae53f1e1499514937f9c7d5",
    "PREREGISTRATION_RAW_P13_COORDINATE12_AUDIT_R1.md":
        "c578f6124f41fe69fa94be4b9cb02c56353b294f57d37a0c862d39405b1d836e",
    "run_v89h19r1_raw_p13_coordinate12_audit.sh":
        "11d3c15d39e6a0155b74f46eb7e8abcfe9d4e4fc84bac6954e2206e34eb0e9f4",
    "P13_RAW_COORDINATE12_AUDIT_R1_RESULT.md":
        "6573626441e58560935e6c4efac15f7a2cda873afc42f56e42ae5f4ca56837e8",
    "P13_RAW_COORDINATE12_AUDIT_R1_FREEZE.sha256":
        "35368feef910383f6199c9c95e91d4adb1ac0819cd6f1e3f930bd14b78c7d6a4",
    "RAW_P13_COORDINATE12_R1.tsv":
        "7ed98587b0c42de16ada758263707cd273f1c5356b4893e106c85f337abe7eae",
    "RAW_P13_COORDINATE12_ACTIVE_ADDENDS_R1.tsv":
        "40d186434a1aa73c2c770663accb200f3ae6215e0fc9f00d6495ac7b2a7ce0d4",
    "replay_v89h15_allq_p13_full_normal_form.py":
        "6c06bed1dde0062d4eeed09b26f9cee11b10259f824fecd319fb3ae0c7a4fc7f",
    "P13_FULL_NORMAL_FORM_RESULT.md":
        "29d5723b0d920840dbdfe72398624cfc0672843dbbf1d713b2fdd29dea52712c",
    "P13_FULL_NORMAL_FORM_FREEZE.sha256":
        "4048419e15f366baeb03d242f546f096ee22d4529e6c6fededf58b2aea951c18",
    "P13_FULL_NORMAL_FORM_EVIDENCE.sha256":
        "7c77bf767eea783d8d25a4c99c9201d039ed24d3a9037a1d2034accba569aa67",
    "P13_FULL_NORMAL_FORM_VECTOR_RECORD_ERRATUM.md":
        "27d8289d7215d16806d1f1197b137acc7d49b0d75a05c766833eaaa38db44418",
    "P13_COORDINATE12_UNIT.tsv":
        "c5d136d942177882424a75a47c631fbd386d7fff6dbb09187effd32f1be4687f",
    "P13_COORDINATE12_UNIT_RESULT.md":
        "0f152a88ba6422b04a3b4274ad5a0e71996c1c65395c7518b6e725321ab32d7f",
    "P13_COORDINATE12_UNIT_FREEZE.sha256":
        "0d3a9a6aad58635e9f02f160a3012b28dc351ecdbbafd97e59b7c1c2cda44974",
    "P13_COORDINATE12_UNIT_EVIDENCE.sha256":
        "bc9590017fb0f6942c9b7d396ba2b95e56fd1cbad2fc8c2b84e2b753bf79932d",
}

EXPECTED_NORMAL_FORM_SHA = (
    "9af3240d4016ad99766122303465d2cea7a10dc5e71b489f62564b9c3540c2d8"
)
EXPECTED_UNIT_RECORD = (((), (), "3500000000/9*U", "V"),)
EXPECTED_RAW_CENSUS_SHA = (
    "7ed98587b0c42de16ada758263707cd273f1c5356b4893e106c85f337abe7eae"
)
EXPECTED_ADDEND_CENSUS_SHA = (
    "40d186434a1aa73c2c770663accb200f3ae6215e0fc9f00d6495ac7b2a7ce0d4"
)
KAPPA_NUMERATOR = 3500000000
KAPPA_DENOMINATOR = 9


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def verify_manifest(path):
    rows = 0
    for line in path.read_text().splitlines():
        expected, relative = line.split(maxsplit=1)
        target = HERE / relative
        assert target.is_file(), target
        assert digest(target) == expected, target
        rows += 1
    return rows


assert sys.flags.optimize == 0, sys.flags.optimize
for name, value in REQUIRED_ENVIRONMENT:
    assert os.environ.get(name) == value, (name, os.environ.get(name))
assert os.environ.get("AWS_RUN_TAG", "").startswith(TAG_PREFIX)
for name in FORBIDDEN_MODULES:
    assert name not in sys.modules, name
    try:
        forbidden_spec = importlib.util.find_spec(name)
    except ModuleNotFoundError:
        forbidden_spec = None
    assert forbidden_spec is None, name

H15_ARCHIVE = Path(os.environ["TD6_H15_ARCHIVE"]).resolve()
assert digest(H15_ARCHIVE) == H15_ARCHIVE_SHA, H15_ARCHIVE
assert digest(H19R1_PATH) == H19R1_SHA
for name, expected in PINNED_FILES.items():
    assert digest(HERE / name) == expected, name
H19R1_MANIFEST_ROWS = verify_manifest(H19R1_MANIFEST)

spec = importlib.util.spec_from_file_location(
    "td6_v89h19r2_h19r1_parent", H19R1_PATH
)
h19r1 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = h19r1
spec.loader.exec_module(h19r1)

h15 = h19r1.h15
h12, h11 = h15.h12, h15.h11
h5, h6, v87, v85, m, t = h15.h5, h15.h6, h15.v87, h15.v85, h15.m, h15.t
p = h11.p
QPoly, E3 = h15.QPoly, h15.E3
Rat3 = h6.Rat3
C, V, U, F, H, B3 = h6.C, h6.V, h6.U, h6.F, h6.H, h6.B3
SPECIAL_HF = v85.SPECIAL_HF
ALL_Q = h15.ALL_Q
EXPECTED_N_SHA256 = h15.EXPECTED_N_SHA256
EXPECTED_AFFINE_SHA = h15.EXPECTED_AFFINE_SHA
UNIT_COORDINATES = m.r.scalar_coordinates(E3(1))
UNIT_INDEX = next(index for index, value in enumerate(UNIT_COORDINATES) if value)
ALLOWED_F0_FACTORS = (("U", U), ("V", V), ("HF", SPECIAL_HF))

ZERO_POLYNOMIAL = F - F

assert len(ALL_Q) == 22 and 15 not in ALL_Q
assert U * H - (V**2 - 4 * U**3) - F == ZERO_POLYNOMIAL
assert B3 - V**4 - F * 4 * U * (C + 5 * U**2) == ZERO_POLYNOMIAL


def embed_scalar(value):
    """Scalar embedding Rat3 -> E3; a ring map with C-free structure constants."""
    return E3(Rat3.coerce(value))


def unembed_scalar(value):
    value = E3.coerce(value)
    coordinates = m.r.scalar_coordinates(value)
    scalar = coordinates[UNIT_INDEX] / UNIT_COORDINATES[UNIT_INDEX]
    assert embed_scalar(scalar) == value
    return scalar


def coordinate12(polynomial):
    """Coordinate-12 projection, keyed by (parameter monomial, q monomial)."""
    out = {}
    for parameter_monomial, value in polynomial.items():
        for q_monomial, coefficient in QPoly.coerce(value).coefficients.items():
            coordinate = m.r.scalar_coordinates(coefficient)[12]
            if coordinate:
                out[(parameter_monomial, q_monomial)] = embed_scalar(coordinate)
    return out


def flatten_coefficients(label, polynomials):
    """Flatten QPoly-valued polynomials into a dict of bare E3 coefficients."""
    out = {}
    for index, polynomial in enumerate(polynomials):
        for parameter_monomial, value in polynomial.items():
            for q_monomial, coefficient in QPoly.coerce(value).coefficients.items():
                out[(label, index, parameter_monomial, q_monomial)] = coefficient
    return out


def polarize(polynomial, images, pivot_position):
    """Cofactors g with polynomial - polynomial o affine = sum_i g_i (x_i-x_aff_i)."""
    cofactors = [{} for _ in range(38)]
    scanned = 0
    for monomial, coefficient in sorted(polynomial.items()):
        scanned += 1
        if scanned % 500 == 0:
            print(f"polarization_terms_scanned={scanned}", flush=True)
        value = QPoly.coerce(coefficient)
        assert len(monomial) <= 2
        if not monomial:
            continue
        if len(monomial) == 1:
            position = pivot_position.get(monomial[0])
            if position is not None:
                cofactors[position] = v87.add(cofactors[position], {(): value})
            continue
        left, right = monomial
        if left == right:
            position = pivot_position.get(left)
            if position is not None:
                cofactors[position] = v87.add(
                    cofactors[position],
                    v87.add({(left,): value}, v87.scale(images[left], value)),
                )
            continue
        position = pivot_position.get(right)
        if position is not None:
            cofactors[position] = v87.add(cofactors[position], {(left,): value})
        position = pivot_position.get(left)
        if position is not None:
            cofactors[position] = v87.add(
                cofactors[position], v87.scale(images[right], value)
            )
    assert scanned == len(polynomial)
    return [v87.clean(cofactor) for cofactor in cofactors]


def expand_first(multipliers, sources, label):
    """sum_k multiplier_k * FIRST_k, retaining the per-row terms."""
    total, terms = {}, []
    for index, (multiplier, source) in enumerate(zip(multipliers, sources)):
        if not multiplier:
            terms.append({})
            continue
        term = v87.multiply(multiplier, source)
        terms.append(term)
        total = v87.add(total, term)
        print(
            f"{label}_expansion_row={index};term_parameter_terms={len(term)};"
            f"running_parameter_terms={len(total)}",
            flush=True,
        )
    return v87.clean(total), terms


def write_inverse_columns(path, pivots, columns):
    lines = [
        "pivot_row\tpivot_variable\tbasis_column\tparameter_monomial\t"
        "q_monomial\tcoefficient_exact"
    ]
    for row, pivot in enumerate(pivots):
        for column, solution in enumerate(columns):
            value = QPoly.coerce(solution[row])
            for q_monomial, coefficient in sorted(value.coefficients.items()):
                lines.append(
                    f"{row}\t{pivot}\t{column}\t{()!r}\t{q_monomial!r}\t"
                    f"{m.e3_exact(coefficient)}"
                )
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest(), len(lines) - 1


def write_first_multipliers(path, multipliers, first):
    lines = [
        "first_index\tfirst_key\tparameter_monomial\tq_monomial\t"
        "coefficient_exact"
    ]
    for index, (multiplier, (key, _, _)) in enumerate(zip(multipliers, first)):
        for parameter_monomial, value in sorted(multiplier.items()):
            for q_monomial, coefficient in sorted(value.coefficients.items()):
                lines.append(
                    f"{index}\t{key!r}\t{parameter_monomial!r}\t{q_monomial!r}\t"
                    f"{m.e3_exact(coefficient)}"
                )
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest(), len(lines) - 1


def write_scalar_records(path, sections, header):
    lines = [header]
    for side, index, polynomial in sections:
        for (parameter_monomial, q_monomial), value in sorted(polynomial.items()):
            scalar = unembed_scalar(value)
            lines.append(
                f"{side}\t{index}\t{parameter_monomial!r}\t{q_monomial!r}\t"
                f"{scalar.numerator}\t{scalar.denominator}"
            )
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest(), len(lines) - 1


def write_addend_census(path, sections):
    lines = [
        "stage\tlabel\tparameter_monomial\tq_monomial\tcoordinate\t"
        "numerator\tdenominator"
    ]
    for stage, label, polynomial in sections:
        for parameter_monomial, value in sorted(polynomial.items()):
            for q_monomial, coefficient in sorted(value.coefficients.items()):
                for index, coordinate in enumerate(
                    m.r.scalar_coordinates(coefficient)
                ):
                    if coordinate:
                        lines.append(
                            f"{stage}\t{label}\t{parameter_monomial!r}\t"
                            f"{q_monomial!r}\t{index}\t{coordinate.numerator}\t"
                            f"{coordinate.denominator}"
                        )
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest(), len(lines) - 1


def write_total_multipliers(path, p13_scalar, first_multipliers, first, quotient):
    lines = [
        "kind\tindex\tkey\tparameter_monomial\tq_monomial\tcoefficient_exact"
    ]
    lines.append(
        f"P13\t0\tcoordinate12_P13_generic\t{()!r}\t{()!r}\t"
        f"{m.e3_exact(p13_scalar)}"
    )
    for index, (multiplier, (key, _, _)) in enumerate(
        zip(first_multipliers, first)
    ):
        for parameter_monomial, value in sorted(multiplier.items()):
            for q_monomial, coefficient in sorted(value.coefficients.items()):
                lines.append(
                    f"FIRST\t{index}\t{key!r}\t{parameter_monomial!r}\t"
                    f"{q_monomial!r}\t{m.e3_exact(coefficient)}"
                )
    for (parameter_monomial, q_monomial), coefficient in sorted(quotient.items()):
        lines.append(
            f"F\t0\tliteral_base_F\t{parameter_monomial!r}\t{q_monomial!r}\t"
            f"{m.e3_exact(coefficient)}"
        )
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest(), len(lines) - 1


def read_unit_record(path):
    lines = path.read_text().splitlines()
    assert lines[0] == (
        "coordinate\tparameter_monomial\tq_monomial\tnumerator\tdenominator"
    )
    assert len(lines) == 2
    coordinate, parameter, q_monomial, numerator, denominator = lines[1].split("\t")
    assert coordinate == "12"
    return ((
        ast.literal_eval(parameter), ast.literal_eval(q_monomial),
        numerator, denominator,
    ),)


def f0_denominator_exponents(common):
    unit, factors = common.factor()
    exponents = {name: 0 for name, _ in ALLOWED_F0_FACTORS}
    for factor, multiplicity in factors:
        monic_factor = v85.monic(factor)
        matched = [
            name for name, value in ALLOWED_F0_FACTORS
            if v85.monic(value) == monic_factor
        ]
        assert len(matched) == 1, (str(factor), str(common))
        exponents[matched[0]] += multiplicity
    return unit, exponents


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    print("producer=TD6-V89H19R2-P13-COORDINATE12-ORIGINAL-FIRST-TOTAL-F")
    print(f"h19r1_client_sha256={H19R1_SHA}")
    print(f"h15_archive_sha256={H15_ARCHIVE_SHA}")
    print(f"h19r1_manifest_rows={H19R1_MANIFEST_ROWS}")
    print("retained_q_exponents=" + ",".join(map(str, ALL_Q)))
    print("q15_absent_target_shear=true")
    print("licensed_identity_UH_minus_V2minus4U3_equals_F=true")
    print("licensed_identity_B3_minus_V4_equals_F_times_4U_C_plus_5U2=true")
    print("dense_132_column_matrix_used=false")
    print("groebner_or_singular_engine_used=false", flush=True)

    # Stage 4.2 -- one transport, retaining every generic object for Stage 5.
    events, bands, seen = v87.build_bands()
    first = v87.compile_first(bands)
    p13 = h15.compile_current_degree(bands, 13)
    assert events == 2 and len(first) == 38
    assert set(seen) == set(ALL_Q) and all(seen[exponent] == 1 for exponent in ALL_Q)
    generic_sources = [v87.source_polynomial(row, rhs) for _, row, rhs in first]
    assert all(
        all(len(monomial) <= 1 for monomial in source)
        for source in generic_sources
    )
    assert len(p13) == 2757 and max(map(len, p13), default=0) <= 2
    _, raw_common = v87.assert_denominators_allowed([p13, *generic_sources])
    assert raw_common == U * H and raw_common.gcd(F).total_degree() == 0
    print("literal_transport_FIRST_P13_rebuilt=true")
    print(f"literal_P13_parameter_terms={len(p13)}")
    print(f"raw_source_common_denominator=({raw_common})")
    print("raw_source_denominator_coprime_F=true", flush=True)

    probe = sorted(p13)[0]
    left = p13[probe].coefficients[sorted(p13[probe].coefficients)[0]]
    right = E3(Rat3(C))
    assert v85.specialize_e3(left * right) == (
        v85.specialize_e3(left) * v85.specialize_e3(right)
    )
    assert v85.specialize_e3(E3(Rat3(F))) == E3()
    assert v85.specialize_e3(E3(Rat3(U))) == E3(Rat3(U))
    print("F0_specialization_multiplicative_probe=true", flush=True)

    # Stage 4.3 -- full-E3 source-addend census.
    contributions = h19r1.raw_degree_contributions(bands, 13)
    assert h19r1.sum_contributions(contributions) == p13
    active = []
    for label, contribution in contributions:
        records = h19r1.coordinate_records(h6.specialize_polynomial(contribution))
        if records:
            active.append((label, contribution, records))
    assert tuple(label for label, _, _ in active) == h19r1.EXPECTED_ACTIVE_LABELS
    addend_text = h19r1.records_text(
        tuple((label, records) for label, _, records in active)
    )
    assert sha256(addend_text.encode()).hexdigest() == EXPECTED_ADDEND_CENSUS_SHA
    census_sections = []
    for label, contribution, _ in active:
        census_sections.append(("total", label, contribution))
        census_sections.append(("F0", label, h6.specialize_polynomial(contribution)))
    census_sha, census_rows = write_addend_census(
        outdir / "P13_ADDEND_FULL_E3_CENSUS.tsv", census_sections
    )
    omitted_label = h19r1.EXPECTED_OMISSION_LABEL
    assert active[0][0] == omitted_label
    assert sum(label == omitted_label for label, _ in contributions) == 1
    omitted_addend = active[0][1]
    addend_multiple_of_29 = all(29 in monomial for monomial in omitted_addend)
    print(f"literal_source_addend_count={len(contributions)}")
    print("source_addend_sum_equals_frozen_H15_compiler=true")
    print(f"addend_full_e3_census_sha256={census_sha};rows={census_rows}")
    print("active_source_addends_equal_frozen_H19R1=true")
    print(f"omitted_addend_full_e3_terms={len(omitted_addend)}")
    print(
        "omitted_addend_is_multiple_of_transport_variable_29="
        f"{str(addend_multiple_of_29).lower()}",
        flush=True,
    )

    omitted_contributions = tuple(
        item for item in contributions if item[0] != omitted_label
    )
    omitted_parent = h19r1.sum_contributions(omitted_contributions)
    assert omitted_parent != p13
    omitted_specialized = h6.specialize_polynomial(omitted_parent)

    # Stage 4.4 -- specialize and replay the frozen H15 path.
    specialized_first = h6.specialize_first(first)
    specialized_p13 = h6.specialize_polynomial(p13)
    special_sources = [
        v87.source_polynomial(row, rhs) for _, row, rhs in specialized_first
    ]
    for index, (generic, special) in enumerate(
        zip(generic_sources, special_sources)
    ):
        assert h6.specialize_polynomial(generic) == special, index
    print("literal_base_change_FIRST_exact=true", flush=True)

    observed_variables = set()
    for _, row, _ in specialized_first:
        observed_variables.update(row)
    for monomial in specialized_p13:
        observed_variables.update(monomial)
    assert observed_variables == set(range(132)), len(observed_variables)
    pivots = h5.base_pivot_columns(specialized_first)
    pivot_set = set(pivots)
    all_variables = set(range(132))
    for _, row, _ in specialized_first:
        assert set(row) <= all_variables
    for monomial in specialized_p13:
        assert set(monomial) <= all_variables
    free_variables = tuple(sorted(all_variables - pivot_set))
    assert len(pivots) == len(pivot_set) == 38 and len(free_variables) == 94
    print("pivot_variables=" + ",".join(map(str, pivots)))
    print("free_variables=" + ",".join(map(str, free_variables)))
    print("complete_free_variable_inventory_count=94", flush=True)

    A0 = [
        [row.get(pivot, QPoly()).constant() for pivot in pivots]
        for _, row, _ in specialized_first
    ]
    A = [
        [row.get(pivot, QPoly()) for pivot in pivots]
        for _, row, _ in specialized_first
    ]
    D = [
        [row.get(variable, QPoly()) for variable in free_variables]
        for _, row, _ in specialized_first
    ]
    rhs = [rhs for _, _, rhs in specialized_first]
    assert len(A) == 38 and all(len(row) == 38 for row in A)
    inverse_A0 = h5.inverse_constant_matrix(A0)
    B = h5.matmul_constant_q(inverse_A0, A)
    identity_q = p.identity_matrix(38)
    N = [[B[i][j] - identity_q[i][j] for j in range(38)] for i in range(38)]
    n_sha, n_entries, n_terms, n_degree = p.matrix_stats(N)
    assert n_sha == EXPECTED_N_SHA256
    assert (n_entries, n_terms, n_degree) == (532, 6069, 1)
    print(f"N_sha256={n_sha}", flush=True)

    S_full, inverse_S_full, order, upper_N = h11.reconstruct_flag(N, outdir)
    W = [[S_full[i][order[j]] for j in range(38)] for i in range(38)]
    inverse_W = [[inverse_S_full[order[i]][j] for j in range(38)] for i in range(38)]
    assert h5.matmul_constant(W, inverse_W) == h11.identity_constant(38)
    assert h5.matmul_constant(inverse_W, W) == h11.identity_constant(38)
    print("flag_basis_and_permutation_two_sided=true", flush=True)

    def solve_original(right_side, label):
        """H15's main()-local closure, recomposed from frozen h12 primitives."""
        base = h12.matvec_constant_q(inverse_A0, right_side)
        triangular = h12.matvec_constant_q(inverse_W, base)
        solution = h12.solve_upper_labeled(upper_N, triangular, label)
        return h12.matvec_constant_q(W, solution)

    constant_solution = solve_original(rhs, "constant")
    assert h12.matvec_q(A, constant_solution) == rhs
    direction_solutions = []
    for column, variable in enumerate(free_variables):
        solution = solve_original(
            [-D[row][column] for row in range(38)], f"free_{variable}"
        )
        replay = h12.matvec_q(A, solution)
        assert all(replay[row] + D[row][column] == QPoly() for row in range(38))
        direction_solutions.append(solution)
    print("all_free_directions_original_FIRST_replay=true", flush=True)

    affine_sha, affine_rows = h12.write_affine_pivot_map(
        outdir / "P13_AFFINE_PIVOT_MAP.tsv", pivots, free_variables,
        constant_solution, direction_solutions,
    )
    assert affine_sha == EXPECTED_AFFINE_SHA
    print(f"affine_pivot_map_sha256={affine_sha};rows={affine_rows}")
    print("affine_pivot_map_equals_frozen_H12=true", flush=True)

    pivot_position = {variable: index for index, variable in enumerate(pivots)}
    free_position = {variable: index for index, variable in enumerate(free_variables)}
    images = {}
    for variable in all_variables:
        if variable in free_position:
            images[variable] = {(variable,): QPoly(1)}
            continue
        position = pivot_position[variable]
        image = {(): constant_solution[position]} if constant_solution[position] else {}
        for free_index, free_variable in enumerate(free_variables):
            value = direction_solutions[free_index][position]
            if value:
                image[(free_variable,)] = value
        images[variable] = v87.clean(image)
    assert pivots[13] == 29 and images[29] == {}
    print("affine_image_of_pivot_position_13_variable_29_is_zero=true", flush=True)

    normal_form, scanned = h15.affine_substitute(specialized_p13, images)
    assert scanned == len(specialized_p13)
    assert all(set(monomial) <= set(free_variables) for monomial in normal_form)
    normal_form_sha = h12.write_polynomial(
        outdir / "ALLQ_P13_FULL_NORMAL_FORM.tsv", normal_form
    )
    assert normal_form_sha == EXPECTED_NORMAL_FORM_SHA
    unit_record = read_unit_record(HERE / "P13_COORDINATE12_UNIT.tsv")
    assert unit_record == EXPECTED_UNIT_RECORD
    assert h19r1.coordinate_records(normal_form) == unit_record
    print(f"full_normal_form_sha256={normal_form_sha}")
    print("full_normal_form_equals_frozen_H15=true")
    print("coordinate12_equals_frozen_H18_unit=true", flush=True)

    raw_census_text = h19r1.records_text((
        ("total", h19r1.coordinate_records(p13)),
        ("F0", h19r1.coordinate_records(specialized_p13)),
        ("F0_OMIT_SOURCE_ADDEND", h19r1.coordinate_records(omitted_specialized)),
    ))
    assert sha256(raw_census_text.encode()).hexdigest() == EXPECTED_RAW_CENSUS_SHA
    print("raw_coordinate12_census_equals_frozen_H19R1=true", flush=True)

    # Stage 4.5 -- 38 original-row inverse columns.
    inverse_columns = []
    for index in range(38):
        basis = [QPoly(1 if row == index else 0) for row in range(38)]
        column = solve_original(basis, f"inverse_{index}")
        assert h12.matvec_q(A, column) == basis
        inverse_columns.append(column)
    inverse_A = [
        [inverse_columns[column][row] for column in range(38)] for row in range(38)
    ]
    assert h5.matmul_q(A, inverse_A) == identity_q
    assert h5.matmul_q(inverse_A, A) == identity_q
    inverse_sha, inverse_rows = write_inverse_columns(
        outdir / "P13_ORIGINAL_FIRST_INVERSE.tsv", pivots, inverse_columns
    )
    print(f"original_FIRST_inverse_sha256={inverse_sha};rows={inverse_rows}")
    print("original_FIRST_inverse_replay=true", flush=True)

    differences = []
    for position, pivot in enumerate(pivots):
        difference = v87.add({(pivot,): QPoly(1)}, images[pivot], -1)
        combination = h5.linear_combination(
            [inverse_A[position][k] for k in range(38)], special_sources
        )
        assert v87.clean(difference) == v87.clean(combination), position
        differences.append(v87.clean(difference))
    print("pivot_difference_equals_inverse_times_FIRST=true", flush=True)

    # Stage 4.6 / 4.7 -- polarization and the load-bearing expansion.
    cofactors = polarize(specialized_p13, images, pivot_position)
    polarized = {}
    for cofactor, difference in zip(cofactors, differences):
        if cofactor:
            polarized = v87.add(polarized, v87.multiply(cofactor, difference))
    assert v87.add(specialized_p13, v87.clean(polarized), -1) == normal_form
    print("polarization_matches_normal_form=true", flush=True)

    multipliers = [
        v87.clean(h5.linear_combination(
            [inverse_A[position][index] for position in range(38)], cofactors
        ))
        for index in range(38)
    ]
    expansion, special_terms = expand_first(multipliers, special_sources, "special")
    assert v87.add(specialized_p13, expansion, -1) == normal_form
    assert h19r1.coordinate_records(
        v87.add(specialized_p13, expansion, -1)
    ) == unit_record
    multiplier_sha, multiplier_rows = write_first_multipliers(
        outdir / "P13_COORDINATE12_FIRST_MULTIPLIERS.tsv", multipliers, first
    )
    nonzero_multipliers = sum(1 for value in multipliers if value)
    print(f"first_multipliers_sha256={multiplier_sha};rows={multiplier_rows}")
    print(f"nonzero_first_multipliers={nonzero_multipliers}")
    print("original_FIRST_expansion_equals_NF=true", flush=True)

    identity_sections = [("P13_special", -1, coordinate12(specialized_p13))]
    identity_sections.append(("H18_unit", -1, coordinate12(normal_form)))
    special_terms_c12 = [coordinate12(term) for term in special_terms]
    for index, term in enumerate(special_terms_c12):
        if term:
            identity_sections.append(("FIRST_term", index, term))
    identity_sha, identity_rows = write_scalar_records(
        outdir / "P13_COORDINATE12_FIRST_IDENTITY_C12.tsv", identity_sections,
        "side\tindex\tparameter_monomial\tq_monomial\tnumerator\tdenominator",
    )
    print(f"coordinate12_identity_sha256={identity_sha};rows={identity_rows}",
          flush=True)

    # Stage 4.8 -- genuine H19R1 source-addend omission.
    assert omitted_specialized != specialized_p13
    omitted_normal_form, omitted_scanned = h15.affine_substitute(
        omitted_specialized, images
    )
    assert omitted_scanned == len(omitted_specialized)
    omitted_cofactors = polarize(omitted_specialized, images, pivot_position)
    omitted_multipliers = [
        v87.clean(h5.linear_combination(
            [inverse_A[position][index] for position in range(38)],
            omitted_cofactors,
        ))
        for index in range(38)
    ]
    omitted_expansion, _ = expand_first(
        omitted_multipliers, special_sources, "omitted"
    )
    assert v87.add(omitted_specialized, omitted_expansion, -1) == omitted_normal_form
    omitted_endpoint = h19r1.coordinate_records(omitted_normal_form)
    omission_changes_endpoint = omitted_endpoint != unit_record
    omission_changes_cofactor = omitted_multipliers != multipliers
    assert omission_changes_endpoint or omission_changes_cofactor
    omission_sha, omission_rows = write_first_multipliers(
        outdir / "P13_OMISSION_MULTIPLIERS.tsv", omitted_multipliers, first
    )
    print(f"source_omission_label={omitted_label}")
    print("source_omission_applied_before_aggregation=true")
    print(f"omission_multipliers_sha256={omission_sha};rows={omission_rows}")
    print(f"omission_changes_endpoint={str(omission_changes_endpoint).lower()}")
    print(f"omission_changes_cofactor={str(omission_changes_cofactor).lower()}",
          flush=True)

    # Stage 4.9 -- FIRST-row omission.
    first_nonzero = min(index for index, value in enumerate(multipliers) if value)
    dropped_term = special_terms[first_nonzero]
    assert dropped_term
    broken = v87.add(expansion, dropped_term, -1)
    assert broken != expansion
    assert v87.add(specialized_p13, broken, -1) != normal_form
    print(f"FIRST_row_omission_index={first_nonzero}")
    print("FIRST_row_omission_negative_control=true", flush=True)

    # Stage 5 -- denominator clearing on F=0.
    kappa = Rat3(KAPPA_NUMERATOR * U, KAPPA_DENOMINATOR * V)
    assert str(kappa.numerator) == unit_record[0][2]
    assert str(kappa.denominator) == unit_record[0][3]
    f0_values = list(v87.all_coefficients([*multipliers, specialized_p13]))
    f0_values.append(embed_scalar(kappa))
    f0_label, f0_count, f0_common, f0_factorization, f0_allowed = (
        t.denominator_record("F0_membership_family", f0_values)
    )
    assert f0_allowed, f0_factorization
    unit_constant, exponents = f0_denominator_exponents(f0_common)
    a, e, c = exponents["U"], exponents["V"], exponents["HF"]
    assert e >= 1, exponents
    clearer = U**a * V**e * SPECIAL_HF**c
    assert v85.monic(clearer) == f0_common, (str(clearer), str(f0_common))
    clearing = KAPPA_DENOMINATOR * clearer
    clearing_scalar = embed_scalar(Rat3(clearing))
    middle_value = Rat3(
        KAPPA_NUMERATOR * U**(a + 1) * V**(e - 1) * SPECIAL_HF**c
    )
    assert Rat3(clearing) * kappa == middle_value
    middle = {((), ()): embed_scalar(middle_value)}
    print(f"F0_denominator_common=({f0_common})")
    print(f"F0_denominator_factorization={f0_factorization}")
    print(f"F0_denominator_exponents=U^{a}*V^{e}*(V^2-4U^3)^{c}")
    print(f"F0_denominator_audited_values={f0_count};label={f0_label}")
    print(f"F0_denominator_unit_constant={unit_constant}")
    print("F0_denominators_in_U_V_V2minus4U3=true", flush=True)

    betas = [v87.scale(multiplier, clearing_scalar) for multiplier in multipliers]
    beta_coefficients = flatten_coefficients("beta", betas)
    v85.assert_polynomial_coordinates([beta_coefficients], "cleared_F0_multipliers")
    special_lhs = v85.scale(coordinate12(specialized_p13), clearing_scalar)
    special_rhs = v85.scale(coordinate12(expansion), clearing_scalar)
    assert v85.add(special_lhs, middle, -1) == v85.clean(special_rhs)
    print(f"cleared_F0_multiplier_coefficients={len(beta_coefficients)}")
    print("cleared_F0_identity_exact=true", flush=True)

    display_text = (
        "key\tvalue\n"
        "display_only\ttrue\n"
        f"F0_clearing_factor\t{KAPPA_DENOMINATOR}*U^{a}*V^{e}*(V^2-4*U^3)^{c}\n"
        f"F0_display_clearing_factor\t{KAPPA_DENOMINATOR}*U^{a + c}*H^{c}"
        f"*B3^{e // 4}*V^{e % 4}\n"
        "licensed_after_F0_UH_equals_V2minus4U3\ttrue\n"
        "licensed_after_F0_B3_equals_V4\ttrue\n"
        "total_ring_UH_minus_V2minus4U3_equals_F\ttrue\n"
        "total_ring_B3_minus_V4_equals_F_times_4U_C_plus_5U2\ttrue\n"
    )
    (outdir / "P13_COORDINATE12_F0_DISPLAY.tsv").write_text(display_text)
    display_sha = sha256(display_text.encode()).hexdigest()
    print(f"F0_display_sha256={display_sha}")
    print("B3_eq_V4_only_after_F=true")
    print("UH_eq_V2minus4U3_only_after_F=true", flush=True)

    # Stage 5 -- lift to the total ring and divide by F.
    generic_terms_c12 = []
    generic_expansion_c12 = {}
    for index, (beta, source) in enumerate(zip(betas, generic_sources)):
        if not beta:
            generic_terms_c12.append({})
            continue
        term = v87.multiply(beta, source)
        projected = coordinate12(term)
        generic_terms_c12.append(projected)
        generic_expansion_c12 = v85.add(generic_expansion_c12, projected)
        print(
            f"generic_expansion_row={index};term_parameter_terms={len(term)};"
            f"coordinate12_records={len(projected)}",
            flush=True,
        )
    assert v85.specialize_polynomial(generic_expansion_c12) == v85.clean(
        special_rhs
    )
    print("generic_expansion_specializes_to_cleared_F0_expansion=true", flush=True)

    generic_lhs = v85.scale(coordinate12(p13), clearing_scalar)
    assert v85.specialize_polynomial(generic_lhs) == v85.clean(special_lhs)
    print("generic_P13_coordinate12_specializes_to_F0=true", flush=True)
    residual = v85.add(v85.add(generic_lhs, middle, -1), generic_expansion_c12, -1)
    assert residual, "total_F_residual_vanished"
    assert v85.specialize_polynomial(residual) == {}
    quotient, division_count = v85.divide_polynomial_by_f(residual)
    assert quotient
    replayed = v85.add(generic_expansion_c12, middle)
    replayed = v85.add(replayed, v85.scale(quotient, E3(Rat3(F))))
    assert replayed == v85.clean(generic_lhs)
    print(f"total_F_residual_terms={len(residual)}")
    print(f"total_F_quotient_terms={len(quotient)}")
    print(f"total_F_division_coordinate_count={division_count}")
    print("total_F_division_exact=true")
    print("total_F_not_inverted=true", flush=True)

    audit_values = list(v87.all_coefficients([*betas, p13, *generic_sources]))
    audit_values += list(quotient.values())
    audit_values += [value for term in generic_terms_c12 for value in term.values()]
    audit_values += list(generic_lhs.values()) + list(middle.values())
    audited_count, coordinate_count, delta = v85.assert_denominators_allowed(
        audit_values, "total_family"
    )
    assert delta.gcd(F).total_degree() == 0
    delta_scalar = embed_scalar(Rat3(delta))
    cleared_betas = [v87.scale(beta, delta_scalar) for beta in betas]
    cleared_terms = [v85.scale(term, delta_scalar) for term in generic_terms_c12]
    cleared_quotient = v85.scale(quotient, delta_scalar)
    cleared_lhs = v85.scale(generic_lhs, delta_scalar)
    cleared_middle = v85.scale(middle, delta_scalar)
    cleared_identity = dict(cleared_middle)
    for term in cleared_terms:
        cleared_identity = v85.add(cleared_identity, term)
    f_term = v85.scale(cleared_quotient, E3(Rat3(F)))
    cleared_identity = v85.add(cleared_identity, f_term)
    assert cleared_identity == v85.clean(cleared_lhs)
    cleared_coefficients = flatten_coefficients("cleared_beta", cleared_betas)
    polynomial_count = v85.assert_polynomial_coordinates(
        [cleared_coefficients, *cleared_terms, cleared_quotient,
         cleared_lhs, cleared_middle],
        "cleared_total_family",
    )
    assert f_term and cleared_identity
    assert v85.add(cleared_identity, f_term, -1) != v85.clean(cleared_lhs)
    print(f"denominator_audited_value_count={audited_count}")
    print(f"denominator_audited_scalar_coordinate_count={coordinate_count}")
    print(f"total_family_common_denominator=({delta})")
    print(f"total_family_common_denominator_factor={delta.factor()}")
    print("total_family_denominator_radical_subset_U_H_B3=true")
    print(f"cleared_polynomial_scalar_coordinate_count={polynomial_count}")
    print("cleared_total_family_identity_exact=true")
    print("P13_omission_negative_control=true")
    print("F_omission_negative_control=true", flush=True)

    total_scalar = E3(Rat3(delta * clearing))
    total_sha, total_rows = write_total_multipliers(
        outdir / "P13_COORDINATE12_TOTAL_F_MULTIPLIERS.tsv",
        total_scalar, cleared_betas, first, cleared_quotient,
    )
    h_sha, h_rows = write_scalar_records(
        outdir / "P13_COORDINATE12_TOTAL_F_H.tsv",
        [("F", 0, cleared_quotient)],
        "side\tindex\tparameter_monomial\tq_monomial\tnumerator\tdenominator",
    )
    print(f"total_F_multipliers_sha256={total_sha};rows={total_rows}")
    print(f"total_F_h_sha256={h_sha};rows={h_rows}", flush=True)

    result = (
        f"h19r1_client_sha256={H19R1_SHA}\n"
        f"h15_archive_sha256={H15_ARCHIVE_SHA}\n"
        f"literal_P13_parameter_terms={len(p13)}\n"
        f"N_sha256={n_sha}\n"
        f"affine_pivot_map_sha256={affine_sha}\n"
        f"full_normal_form_sha256={normal_form_sha}\n"
        f"original_FIRST_inverse_sha256={inverse_sha}\n"
        f"first_multipliers_sha256={multiplier_sha}\n"
        f"nonzero_first_multipliers={nonzero_multipliers}\n"
        f"coordinate12_identity_sha256={identity_sha}\n"
        f"addend_full_e3_census_sha256={census_sha}\n"
        f"omission_multipliers_sha256={omission_sha}\n"
        f"total_F_multipliers_sha256={total_sha}\n"
        f"total_F_h_sha256={h_sha}\n"
        f"F0_display_sha256={display_sha}\n"
        f"F0_denominator_exponents=U^{a}*V^{e}*(V^2-4U^3)^{c}\n"
        f"total_family_common_denominator=({delta})\n"
        f"total_F_residual_terms={len(residual)}\n"
        f"total_F_quotient_terms={len(quotient)}\n"
        f"FIRST_row_omission_index={first_nonzero}\n"
        f"source_omission_label={omitted_label}\n"
        "omitted_addend_is_multiple_of_transport_variable_29="
        f"{str(addend_multiple_of_29).lower()}\n"
        "q15_absent_target_shear=true\n"
        "affine_pivot_map_equals_frozen_H12=true\n"
        "full_normal_form_equals_frozen_H15=true\n"
        "coordinate12_equals_frozen_H18_unit=true\n"
        "original_FIRST_inverse_replay=true\n"
        "original_FIRST_expansion_equals_NF=true\n"
        f"omission_changes_endpoint={str(omission_changes_endpoint).lower()}\n"
        f"omission_changes_cofactor={str(omission_changes_cofactor).lower()}\n"
        "F0_denominators_in_U_V_V2minus4U3=true\n"
        "total_F_division_exact=true\n"
        "total_F_not_inverted=true\n"
        "total_family_denominator_radical_subset_U_H_B3=true\n"
        "B3_eq_V4_only_after_F=true\n"
        "UH_eq_V2minus4U3_only_after_F=true\n"
        "independent_total_F_unit_claim=true\n"
        "whole_TD6_killed=false\n"
        "source_landing_composed=false\n"
        "JC2_resolved=false\n"
    )
    (outdir / "P13_COORDINATE12_FIRST_TOTAL_F_RESULT.txt").write_text(result)
    print(result, end="")
    print(f"result_sha256={sha256(result.encode()).hexdigest()}")
    print("TD6-V89H19R2-P13-COORDINATE12-ORIGINAL-FIRST-TOTAL-F PASS")
    v85.restore_base_qd_state()


if __name__ == "__main__":
    main()
