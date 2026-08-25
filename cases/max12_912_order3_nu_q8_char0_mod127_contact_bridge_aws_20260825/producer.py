#!/usr/bin/env python3
"""Cross-characteristic corrected-Q8 contact/source identity certificate.

This is intentionally an exact producer.  It computes in Q[v]/(Q8), audits
127-integrality coefficient by coefficient, reduces to F_127[v]/(Q8bar), and
compares with the independently frozen full-contact endpoint.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


P = 127
ROOT = Path(__file__).resolve().parents[2]
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
LOCAL_SERIES = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/local_series.py"
FULL_SOURCE = ROOT / "cases/max12_912_order3_nu_q8_p127_full_contact_jacobian_aws_20260825/full_contact.py"
FULL_RESULT = ROOT / "cases/max12_912_order3_nu_q8_p127_full_contact_jacobian_aws_20260825/aws_box02_v1/result.json"

PINS = {
    COMPILER: "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545",
    LOCAL_SERIES: "5e3e3d8605999a21371dbd2aa54c82fbfec510b5e26f3801387c11d450da8957",
    FULL_SOURCE: "08a3d227accbc3c23a384db55bf44a050c5140e0034c70b95666fcd8fd51b6c8",
    FULL_RESULT: "804f9fbb095832e79a4f01ad870ed87a55921b78f34ff9f83ae946da04b70549",
}


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def pin_dependencies() -> None:
    for path, expected in PINS.items():
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))


def fraction_mod_checked(value: Fraction) -> int:
    if value.denominator % P == 0:
        raise RuntimeError(("127-nonintegral scalar", value))
    return value.numerator % P * pow(value.denominator % P, P - 2, P) % P


def nf_exact(value) -> list[list[int]]:
    return [[coefficient.numerator, coefficient.denominator] for coefficient in value.poly]


def nf_reduction(value, F) -> list[int]:
    return F.trim([fraction_mod_checked(coefficient) for coefficient in value.poly])


def nf_denominator_record(name: str, value, F, require_unit: bool = False) -> dict:
    denominators = [coefficient.denominator for coefficient in value.poly]
    if any(denominator % P == 0 for denominator in denominators):
        raise RuntimeError((name, denominators))
    reduced = nf_reduction(value, F)
    common = F.gcd_poly(reduced, F.Q8)
    norm = F.norm(reduced)
    if require_unit and (common != [1] or norm == 0):
        raise RuntimeError((name, "reduction is not a unit", reduced, common, norm))
    return {
        "name": name,
        "all_fraction_denominators_127_units": True,
        "exact_low_to_high": nf_exact(value),
        "reduction_low_to_high": reduced,
        "gcd_with_q8bar": common,
        "norm_mod_127": norm,
        "required_unit": require_unit,
    }


def canonical_row_q(row) -> list:
    entries = []
    for monomial, coefficient in sorted(row.items()):
        coefficient = Fraction(coefficient)
        fraction_mod_checked(coefficient)
        entries.append([list(monomial), coefficient.numerator, coefficient.denominator])
    return entries


def canonical_row_mod(row) -> list:
    entries = []
    for monomial, coefficient in sorted(row.items()):
        reduced = fraction_mod_checked(Fraction(coefficient))
        if reduced:
            entries.append([list(monomial), reduced])
    return entries


def digest_json(value) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return sha256(encoded).hexdigest()


def evaluate_sparse_nf(value, bases, NF):
    total = NF(0)
    powers = []
    for index, base in enumerate(bases):
        maximum = max((monomial[index] for monomial in value), default=0)
        row = [NF(1)]
        for _ in range(maximum):
            row.append(row[-1] * base)
        powers.append(row)
    for monomial, scalar in value.items():
        term = NF(scalar)
        for index, exponent in enumerate(monomial):
            term = term * powers[index][exponent]
        total = total + term
    return total


def linear_normal_system_nf(value, x_bases, NF):
    constant = NF(0)
    coefficients = [NF(0), NF(0), NF(0)]
    for monomial, scalar in value.items():
        if monomial[0]:
            continue
        normal = monomial[1:4]
        if sum(normal) > 1 or any(exponent not in (0, 1) for exponent in normal):
            raise RuntimeError(("nonlinear normal term at w=0", monomial))
        term = NF(scalar)
        for base, exponent in zip(x_bases, monomial[4:], strict=True):
            term = term * (base ** exponent)
        if sum(normal) == 0:
            constant = constant + term
        else:
            coefficients[normal.index(1)] = coefficients[normal.index(1)] + term
    return coefficients, constant


def determinant_field(matrix, NF):
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise RuntimeError("nonsquare determinant")
    data = [list(row) for row in matrix]
    result = NF(1)
    sign = 1
    for column in range(size):
        pivot = next((row for row in range(column, size) if data[row][column]), None)
        if pivot is None:
            return NF(0)
        if pivot != column:
            data[column], data[pivot] = data[pivot], data[column]
            sign = -sign
        pivot_value = data[column][column]
        result = result * pivot_value
        inverse = pivot_value.inverse()
        for row in range(column + 1, size):
            factor = data[row][column] * inverse
            if not factor:
                continue
            for index in range(column, size):
                data[row][index] = data[row][index] - factor * data[column][index]
    return result if sign == 1 else -result


def main() -> None:
    pin_dependencies()
    L = load("q8_cross_local_series", LOCAL_SERIES)
    F = load("q8_cross_full_contact", FULL_SOURCE)
    NF, J = L.NF, L.J

    # Compile independently through the characteristic-zero and mod-127
    # entry points, then compare the exact sparse rows before reduction.
    _, rows_q, imposed_q, names_q = L.Q.compile_quotient("approx")
    Q_mod = F.load_compiler()
    _, rows_mod_source, imposed_mod, names_mod = Q_mod.compile_quotient("approx")
    if imposed_q != imposed_mod or names_q != names_mod:
        raise RuntimeError((imposed_q, imposed_mod, names_q, names_mod))
    if tuple(imposed_q) != (1, 3, 5, 7, 2, 4):
        raise RuntimeError(imposed_q)
    if any(rows_q[index] != rows_mod_source[index] for index in imposed_q):
        raise RuntimeError("the two pinned compiler entry points emitted different Q rows")
    rows_q_payload = {f"e{index}": canonical_row_q(rows_q[index]) for index in imposed_q}
    rows_p_payload = {f"e{index}": canonical_row_mod(rows_q[index]) for index in imposed_q}

    # The monic Q8 modulus itself must have 127-integral coefficients and
    # reduce to the exact frozen Q8bar.
    modulus_reduction = F.trim([fraction_mod_checked(value) for value in L.J.MODULUS])
    if modulus_reduction != F.Q8:
        raise RuntimeError(("Q8 modulus reduction mismatch", modulus_reduction, F.Q8))
    if F.gcd_poly(F.Q8, [index * F.Q8[index] % P for index in range(1, len(F.Q8))]) != [1]:
        raise RuntimeError("Q8bar is not squarefree")

    zero, one, v = NF(0), NF(1), NF((0, 1))
    D = 3 * v ** 2 - 2
    A2 = 3 * v ** 2 + 3 * v + 1
    x5 = -36 * v ** 2 * A2 / D
    x3 = x5 * (v + 2)
    x1 = x5 * (v + 1) + x5 ** 2 * (3 * v + 1) / (9 * v)

    matrix = []
    rhs = []
    for ell in (3, 5, 7):
        coefficients, constant = linear_normal_system_nf(rows_q[ell], [x1, x3, x5], NF)
        matrix.append(coefficients)
        rhs.append(-constant)
    normal_det = determinant_field(matrix, NF)
    c, d2, d4 = J.solve(matrix, rhs)
    localizer_denominator = x5 * (x3 - 2 * x5)
    inv = localizer_denominator.inverse()
    bases = [zero, c, d2, d4, x1, x3, x5]

    row_residuals_q = {f"e{ell}": evaluate_sparse_nf(rows_q[ell], bases, NF) for ell in imposed_q}
    if any(row_residuals_q.values()):
        raise RuntimeError(("characteristic-zero source residual", row_residuals_q))
    v_residual = v * x5 - x3 + 2 * x5
    localizer_residual = inv * localizer_denominator - 1
    if v_residual or localizer_residual:
        raise RuntimeError((v_residual, localizer_residual))

    coordinates = {
        "c": c,
        "d2": d2,
        "d4": d4,
        "x1": x1,
        "x3": x3,
        "x5": x5,
        "inv": inv,
        "v": v,
    }

    # Full relative source Jacobian in precisely the eight-coordinate graph
    # presentation used at p=127.
    source_jacobian = []
    for ell in imposed_q:
        row = [
            evaluate_sparse_nf(L.Q.M.cpartial(rows_q[ell], column), bases, NF)
            for column in range(1, 7)
        ]
        source_jacobian.append(row + [zero, zero])
    localizer_row = [
        zero, zero, zero, zero,
        inv * x5,
        inv * (x3 - 4 * x5),
        localizer_denominator,
        zero,
    ]
    v_definition_row = [zero, zero, zero, zero, -one, v + 2, zero, x5]
    full_jacobian = source_jacobian + [localizer_row, v_definition_row]
    full_determinant = determinant_field(full_jacobian, NF)

    frozen = json.loads(FULL_RESULT.read_text())
    if frozen["compiler_sha256"] != PINS[COMPILER] or frozen["status"] != "PASS":
        raise RuntimeError("frozen full-contact provenance mismatch")
    expected_coordinates = frozen["contact_coordinates_low_to_high"]
    reduced_coordinates = {name: nf_reduction(value, F) for name, value in coordinates.items()}
    if reduced_coordinates != expected_coordinates:
        raise RuntimeError(("contact reduction mismatch", reduced_coordinates, expected_coordinates))
    reduced_full_determinant = nf_reduction(full_determinant, F)
    expected_full_determinant = frozen["full_relative_jacobian"]["determinant_low_to_high"]
    if reduced_full_determinant != expected_full_determinant:
        raise RuntimeError(("full determinant reduction mismatch", reduced_full_determinant, expected_full_determinant))
    if F.gcd_poly(reduced_full_determinant, F.Q8) != [1]:
        raise RuntimeError("full determinant is not a 127-unit")
    if F.norm(reduced_full_determinant) != frozen["full_relative_jacobian"]["determinant_norm_mod_127"]:
        raise RuntimeError("full determinant norm mismatch")

    records = []
    for name, value in coordinates.items():
        records.append(nf_denominator_record(name, value, F, require_unit=name in {"x5", "inv", "v"}))
    records.extend([
        nf_denominator_record("D=3v^2-2", D, F, require_unit=True),
        nf_denominator_record("A2=3v^2+3v+1", A2, F, require_unit=True),
        nf_denominator_record("normal_3x3_determinant", normal_det, F, require_unit=True),
        nf_denominator_record("x3-2x5", x3 - 2 * x5, F, require_unit=True),
        nf_denominator_record("localizer_denominator", localizer_denominator, F, require_unit=True),
        nf_denominator_record("full_8x8_determinant", full_determinant, F, require_unit=True),
    ])

    payload = {
        "case": "max12_912_order3_nu_q8_char0_mod127_contact_bridge_aws_20260825",
        "status": "PASS",
        "prime": P,
        "dependency_sha256": {str(path.relative_to(ROOT)): value for path, value in PINS.items()},
        "scheme": {
            "base": "Z_(127)",
            "variables": ["w", "c", "d2", "d4", "x1", "x3", "x5", "inv", "v"],
            "rows": ["r1/t", "r3/t", "r5/t", "r7/t", "r2", "r4", "v*x5-x3+2*x5", "inv*x5*(x3-2*x5)-1"],
            "localizer_does_not_invert_w": True,
            "generic_Q_open": "after w inversion and elimination of v,inv: reviewed six-row punctured quotient",
            "special_F127_source": "same divided source used by frozen full-contact Jacobian",
            "contact_completion_if_interpreted": "R[[w]] by arithmetic formal IFT",
        },
        "source_rows_Q": rows_q_payload,
        "source_rows_F127": rows_p_payload,
        "source_rows_Q_sha256": digest_json(rows_q_payload),
        "source_rows_F127_sha256": digest_json(rows_p_payload),
        "q8_monic_Q_exact_low_to_high": [[value.numerator, value.denominator] for value in L.J.MODULUS],
        "q8bar_low_to_high": F.Q8,
        "q8bar_squarefree": True,
        "contact_coordinates_Q_exact": {name: nf_exact(value) for name, value in coordinates.items()},
        "contact_coordinates_F127": reduced_coordinates,
        "row_residuals_Q_zero": {name: not bool(value) for name, value in row_residuals_q.items()},
        "v_definition_residual_Q_zero": not bool(v_residual),
        "localizer_residual_Q_zero": not bool(localizer_residual),
        "denominator_and_unit_records": records,
        "full_relative_jacobian": {
            "columns": ["c", "d2", "d4", "x1", "x3", "x5", "inv", "v"],
            "determinant_Q_exact_low_to_high": nf_exact(full_determinant),
            "determinant_F127_low_to_high": reduced_full_determinant,
            "determinant_F127_norm": F.norm(reduced_full_determinant),
            "matches_frozen_full_contact": True,
        },
        "conclusion": (
            "The reviewed characteristic-zero contact is 127-integral and reduces coordinatewise "
            "to the frozen full mod-127 source contact; the same pinned six divided rows and "
            "non-w localizer define both base changes; the full arithmetic relative Jacobian is "
            "a 127-unit. Formal R[[w]] and no-merger consequences remain interpretive and review-charged."
        ),
        "scope": (
            "cross-characteristic contact/source identity only; no global component degree, "
            "all-contact grouping, characteristic-zero no-merger, trajectory, max12, or JC2 claim"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
