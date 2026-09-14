#!/usr/bin/env python3
"""Reproduce the sparse, fixed-weight q1^3 membership screen.

This is deliberately not a Groebner-basis computation.  It treats the
weighted-homogeneous input rows as vectors in the finite-dimensional space of
polynomials of weight 15, constructs every eligible monomial multiple, and
performs sparse Gaussian elimination over four prime fields.  It also checks
the small integer polynomial identities found during the static row audit.

The modular non-membership result is a screen, not a proof of non-membership
over Q: a prime can be bad for a rational linear system.  Agreement at four
primes is reproducible evidence that no obvious minimal-weight q1^3 identity
is present.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Iterable


EXPECTED_SOURCE_SHA256 = (
    "66bb78cfec123e11c5b9c780056b5949aa1c5c198caeb3c668aab1973d6697eb"
)
PRIMES = (31991, 32003, 65521, 1000003)
EXPECTED_MULTIPLIER_COUNTS = {0: 1, 1: 7, 2: 35, 3: 139, 4: 481}
EXPECTED_ROW_COUNTS = {11: 5, 12: 18, 13: 22, 14: 22, 15: 22}
EXPECTED_COLUMN_COUNT = 5853
EXPECTED_INITIAL_NNZ = 198105
EXPECTED_RANK = 2418
EXPECTED_REMAINDER_NNZ = 688
EXPECTED_REMAINDER_LEAD = ((62, 1), (63, 1))
EXPECTED_PURE_Q3_TERMS = ((32, 4), (33, -4), (86, -116), (87, 244), (88, -128))


# A monomial is a sorted tuple of (zero-based v-index, positive exponent).
Monomial = tuple[tuple[int, int], ...]
Polynomial = dict[Monomial, int]

SIGNED_TERM = re.compile(r"([+-]?)([^+-]+)")
VARIABLE_FACTOR = re.compile(r"v(\d+)(?:\^(\d+))?\Z")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_msolve_input(path: Path) -> tuple[list[str], int, list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if len(lines) < 3:
        raise ValueError("msolve input has fewer than three lines")
    variables = lines[0].strip().split(",")
    characteristic = int(lines[1].strip())
    body = "\n".join(lines[2:]).strip()
    if body.endswith(","):
        body = body[:-1]
    generators = [item.strip() for item in body.split(",\n") if item.strip()]
    return variables, characteristic, generators


def parse_polynomial(text: str) -> Polynomial:
    """Parse the integer-coefficient syntax emitted for this msolve file."""
    result: Polynomial = {}
    consumed = 0
    for match in SIGNED_TERM.finditer(text):
        if match.start() != consumed:
            raise ValueError(f"unparsed polynomial text at byte {consumed}")
        consumed = match.end()
        sign, term = match.groups()
        coefficient = -1 if sign == "-" else 1
        factors = term.split("*")
        if factors[0].isdigit():
            coefficient *= int(factors.pop(0))
        powers: dict[int, int] = {}
        for factor in factors:
            found = VARIABLE_FACTOR.fullmatch(factor)
            if found is None:
                raise ValueError(f"unsupported factor {factor!r} in {term!r}")
            index = int(found.group(1))
            exponent = int(found.group(2) or 1)
            powers[index] = powers.get(index, 0) + exponent
        monomial = tuple(sorted(powers.items()))
        result[monomial] = result.get(monomial, 0) + coefficient
    if consumed != len(text):
        raise ValueError(f"unparsed polynomial suffix at byte {consumed}")
    return {monomial: value for monomial, value in result.items() if value}


def monomial_product(left: Monomial, right: Monomial) -> Monomial:
    powers = dict(left)
    for index, exponent in right:
        powers[index] = powers.get(index, 0) + exponent
    return tuple(sorted(powers.items()))


def polynomial_sum(*summands: tuple[int, Polynomial]) -> Polynomial:
    result: Polynomial = {}
    for scale, polynomial in summands:
        for monomial, coefficient in polynomial.items():
            result[monomial] = result.get(monomial, 0) + scale * coefficient
    return {monomial: value for monomial, value in result.items() if value}


def polynomial_product(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            monomial = monomial_product(lm, rm)
            result[monomial] = result.get(monomial, 0) + lc * rc
    return {monomial: value for monomial, value in result.items() if value}


def polynomial_power(polynomial: Polynomial, exponent: int) -> Polynomial:
    result: Polynomial = {(): 1}
    factor = polynomial
    while exponent:
        if exponent & 1:
            result = polynomial_product(result, factor)
        exponent >>= 1
        if exponent:
            factor = polynomial_product(factor, factor)
    return result


def variable(index: int) -> Polynomial:
    return {((index, 1),): 1}


def weighted_degree(monomial: Monomial, weights: list[int]) -> int:
    return sum(weights[index] * exponent for index, exponent in monomial)


def homogeneous_degree(polynomial: Polynomial, weights: list[int]) -> int:
    degrees = {weighted_degree(monomial, weights) for monomial in polynomial}
    if len(degrees) != 1:
        raise ValueError(f"row is not weighted homogeneous: degrees={sorted(degrees)}")
    return next(iter(degrees))


def monomials_of_weight(
    target: int,
    eligible_indices: tuple[int, ...],
    weights: list[int],
    start: int = 0,
) -> Iterable[Monomial]:
    """Yield exponent tuples once, using nondecreasing variable indices."""
    if target == 0:
        yield ()
        return
    for position in range(start, len(eligible_indices)):
        index = eligible_indices[position]
        weight = weights[index]
        if weight > target:
            continue
        for tail in monomials_of_weight(
            target - weight, eligible_indices, weights, position
        ):
            powers = dict(tail)
            powers[index] = powers.get(index, 0) + 1
            yield tuple(sorted(powers.items()))


def multiply_by_monomial(polynomial: Polynomial, multiplier: Monomial) -> Polynomial:
    return {
        monomial_product(monomial, multiplier): coefficient
        for monomial, coefficient in polynomial.items()
    }


def reduce_vector(
    vector: dict[Monomial, int],
    basis: dict[Monomial, dict[Monomial, int]],
    prime: int,
) -> dict[Monomial, int]:
    """Reduce with lexicographically maximal tuple as the vector-space pivot."""
    while vector:
        pivot = max(vector)
        reducer = basis.get(pivot)
        if reducer is None:
            break
        scale = vector[pivot]
        for monomial, coefficient in reducer.items():
            value = (vector.get(monomial, 0) - scale * coefficient) % prime
            if value:
                vector[monomial] = value
            else:
                vector.pop(monomial, None)
    return vector


def modular_span_result(
    columns: list[tuple[int, Monomial, Polynomial]],
    target: Polynomial,
    prime: int,
) -> dict[str, object]:
    basis: dict[Monomial, dict[Monomial, int]] = {}
    for _generator_index, _multiplier, integer_column in columns:
        vector = {
            monomial: coefficient % prime
            for monomial, coefficient in integer_column.items()
            if coefficient % prime
        }
        reduce_vector(vector, basis, prime)
        if not vector:
            continue
        pivot = max(vector)
        inverse = pow(vector[pivot], -1, prime)
        basis[pivot] = {
            monomial: coefficient * inverse % prime
            for monomial, coefficient in vector.items()
        }

    remainder = {
        monomial: coefficient % prime
        for monomial, coefficient in target.items()
        if coefficient % prime
    }
    reduce_vector(remainder, basis, prime)
    return {
        "prime": prime,
        "rank": len(basis),
        "remainder_nnz": len(remainder),
        "remainder_lead": list(max(remainder)) if remainder else None,
        "target_in_span": not remainder,
    }


def verify_small_identities(generators: list[str], q_index: int, r_index: int) -> list[str]:
    cache: dict[int, Polynomial] = {}

    def g(index_1based: int) -> Polynomial:
        if index_1based not in cache:
            cache[index_1based] = parse_polynomial(generators[index_1based - 1])
        return cache[index_1based]

    q = variable(q_index)
    r = variable(r_index)
    one: Polynomial = {(): 1}
    v = variable
    localizer = g(330)

    checks: dict[str, Polynomial] = {}
    checks["g2 = g3 + g1"] = polynomial_sum((1, g(2)), (-1, g(3)), (-1, g(1)))
    checks["g36 = 99*g3 + 227*g1"] = polynomial_sum(
        (1, g(36)), (-99, g(3)), (-227, g(1))
    )
    checks["g37 = 211*g3 + 120*g1"] = polynomial_sum(
        (1, g(37)), (-211, g(3)), (-120, g(1))
    )
    checks["g38 = v7*g1"] = polynomial_sum(
        (1, g(38)), (-1, polynomial_product(v(7), g(1)))
    )
    checks["g39 = 3*v7*g3 + (3*v7-v14)*g1"] = polynomial_sum(
        (1, g(39)),
        (-3, polynomial_product(v(7), g(3))),
        (-1, polynomial_product(polynomial_sum((3, v(7)), (-1, v(14))), g(1))),
    )
    checks["g40 = 5*g4 + (7*v7-3*v14)*g3 - (3*v14+v20)*g1"] = polynomial_sum(
        (1, g(40)),
        (-5, g(4)),
        (-1, polynomial_product(polynomial_sum((7, v(7)), (-3, v(14))), g(3))),
        (1, polynomial_product(polynomial_sum((3, v(14)), (1, v(20))), g(1))),
    )

    a_poly = polynomial_sum(
        (1, polynomial_product(q, g(4))),
        (4, polynomial_product(v(55), g(1))),
        (-4, polynomial_product(polynomial_product(v(20), q), g(1))),
    )
    checks["A = q*g4 + 4*v55*g1 - 4*v20*q*g1 = q*v45^2"] = polynomial_sum(
        (1, a_poly),
        (-1, polynomial_product(q, polynomial_power(v(45), 2))),
    )
    b_poly = polynomial_sum(
        (1, a_poly),
        (
            -1,
            polynomial_product(
                polynomial_sum((1, v(45)), (1, polynomial_product(v(14), q))),
                g(3),
            ),
        ),
    )
    checks["B = A - (v45+v14*q)*g3 = v14^2*q^3"] = polynomial_sum(
        (1, b_poly),
        (-1, polynomial_product(polynomial_power(v(14), 2), polynomial_power(q, 3))),
    )

    qr = polynomial_product(q, r)
    checks["v7 localized identity"] = polynomial_sum(
        (1, polynomial_product(polynomial_power(r, 2), g(1))),
        (
            -1,
            polynomial_product(
                polynomial_product(v(7), polynomial_sum((1, qr), (1, one))),
                localizer,
            ),
        ),
        (-1, v(7)),
    )
    checks["v45^2 localized identity"] = polynomial_sum(
        (1, polynomial_product(r, a_poly)),
        (-1, polynomial_product(polynomial_power(v(45), 2), localizer)),
        (-1, polynomial_power(v(45), 2)),
    )
    geometric_sum = polynomial_sum(
        (1, polynomial_power(qr, 2)), (1, qr), (1, one)
    )
    checks["v14^2 localized identity"] = polynomial_sum(
        (1, polynomial_product(polynomial_power(r, 3), b_poly)),
        (
            -1,
            polynomial_product(
                polynomial_product(polynomial_power(v(14), 2), geometric_sum),
                localizer,
            ),
        ),
        (-1, polynomial_power(v(14), 2)),
    )

    failed = [label for label, residual in checks.items() if residual]
    if failed:
        raise AssertionError(f"failed exact identities: {failed}")
    return list(checks)


def main() -> None:
    lane = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source", type=Path, default=lane / "input" / "K8_B11_Q1_p0.ms"
    )
    parser.add_argument(
        "--metadata",
        type=Path,
        default=lane / "custody" / "round2-K8_B11_Q1.json",
    )
    args = parser.parse_args()

    metadata = json.loads(args.metadata.read_text(encoding="utf-8"))
    source_digest = sha256(args.source)
    if source_digest != EXPECTED_SOURCE_SHA256:
        raise AssertionError(f"unexpected source SHA-256: {source_digest}")
    if metadata["ms_p0_sha256"] != source_digest:
        raise AssertionError("metadata/input SHA-256 mismatch")

    variables, characteristic, generators = load_msolve_input(args.source)
    weights = [int(value) for value in metadata["weights"]]
    if characteristic != 0:
        raise AssertionError(f"expected characteristic zero, got {characteristic}")
    if len(variables) != 97 or len(weights) != 97 or len(generators) != 330:
        raise AssertionError("expected 97 variables, 97 weights, and 330 generators")
    if variables != [f"v{index}" for index in range(len(variables))]:
        raise AssertionError("unexpected variable order")

    q_name = metadata["alias_sample"]["q1"]
    q_index = int(q_name[1:])
    r_index = int(metadata["alias_sample"]["q1_inv"][1:])
    target_weight = 3 * weights[q_index]
    if (q_index, r_index, target_weight) != (95, 96, 15):
        raise AssertionError("unexpected q1/q1_inv indices or q1^3 weight")
    base_count = int(metadata["markers"]["PRE__NROWS"])
    if base_count != 328:
        raise AssertionError(f"expected 328 homogeneous base rows, got {base_count}")

    verified_identities = verify_small_identities(generators, q_index, r_index)

    candidate_rows: list[tuple[int, int, Polynomial]] = []
    row_counts: dict[int, int] = {}
    for index_1based, text in enumerate(generators[:base_count], 1):
        # The first term is enough to exclude a row because metadata records
        # PRE__HOMOG_I=1.  Candidate rows are fully parsed and rechecked here.
        first_term = SIGNED_TERM.match(text)
        if first_term is None:
            raise ValueError(f"could not read first term of g{index_1based}")
        first_polynomial = parse_polynomial(first_term.group(0))
        degree = homogeneous_degree(first_polynomial, weights)
        if degree > target_weight:
            continue
        polynomial = parse_polynomial(text)
        checked_degree = homogeneous_degree(polynomial, weights)
        if checked_degree != degree:
            raise AssertionError(f"first-term degree mismatch in g{index_1based}")
        candidate_rows.append((index_1based, degree, polynomial))
        row_counts[degree] = row_counts.get(degree, 0) + 1

    if row_counts != EXPECTED_ROW_COUNTS:
        raise AssertionError(f"unexpected candidate-row counts: {row_counts}")

    q3_monomial: Monomial = ((q_index, 3),)
    pure_q3_terms = tuple(
        (index_1based, polynomial[q3_monomial])
        for index_1based, _degree, polynomial in candidate_rows
        if q3_monomial in polynomial
    )
    if pure_q3_terms != EXPECTED_PURE_Q3_TERMS:
        raise AssertionError(f"unexpected pure q1^3 terms: {pure_q3_terms}")

    # Exclude v96: the question tested is q1^3 membership in the homogeneous
    # geometric row ideal before adjoining the localization equation.
    eligible_indices = tuple(
        index
        for index, weight in enumerate(weights)
        if index != r_index and weight <= target_weight
    )
    differences = sorted({target_weight - degree for _, degree, _ in candidate_rows})
    multipliers = {
        difference: list(
            monomials_of_weight(difference, eligible_indices, weights)
        )
        for difference in differences
    }
    multiplier_counts = {key: len(value) for key, value in multipliers.items()}
    if multiplier_counts != EXPECTED_MULTIPLIER_COUNTS:
        raise AssertionError(f"unexpected multiplier counts: {multiplier_counts}")

    columns: list[tuple[int, Monomial, Polynomial]] = []
    for index_1based, degree, polynomial in candidate_rows:
        for multiplier in multipliers[target_weight - degree]:
            columns.append(
                (
                    index_1based,
                    multiplier,
                    multiply_by_monomial(polynomial, multiplier),
                )
            )
    # This fixes the incremental pivot basis deterministically.
    columns.sort(key=lambda item: (len(item[2]), item[0], item[1]))
    initial_nnz = sum(len(polynomial) for _, _, polynomial in columns)
    if len(columns) != EXPECTED_COLUMN_COUNT or initial_nnz != EXPECTED_INITIAL_NNZ:
        raise AssertionError(
            f"unexpected matrix shape: columns={len(columns)}, nnz={initial_nnz}"
        )

    target = polynomial_power(variable(q_index), 3)
    modular_results = [
        modular_span_result(columns, target, prime) for prime in PRIMES
    ]
    for result in modular_results:
        lead = tuple(tuple(pair) for pair in result["remainder_lead"] or [])
        if (
            result["rank"] != EXPECTED_RANK
            or result["remainder_nnz"] != EXPECTED_REMAINDER_NNZ
            or lead != EXPECTED_REMAINDER_LEAD
            or result["target_in_span"]
        ):
            raise AssertionError(f"unexpected modular result: {result}")

    output = {
        "source": str(args.source.resolve()),
        "source_sha256": source_digest,
        "metadata": str(args.metadata.resolve()),
        "characteristic": characteristic,
        "variable_count": len(variables),
        "generator_count": len(generators),
        "base_row_count": base_count,
        "weight_source": "metadata.weights",
        "q": q_name,
        "q_inverse": metadata["alias_sample"]["q1_inv"],
        "target": f"{q_name}^3",
        "target_weight": target_weight,
        "candidate_row_counts_by_weight": row_counts,
        "multiplier_counts_by_weight": multiplier_counts,
        "candidate_column_count": len(columns),
        "candidate_initial_nnz": initial_nnz,
        "rows_with_pure_q1_cubed_term": [
            {"generator": index, "coefficient": coefficient}
            for index, coefficient in pure_q3_terms
        ],
        "pivot_orientation": "lexicographically maximal exponent tuple",
        "verified_integer_identities": verified_identities,
        "modular_results": modular_results,
        "interpretation": (
            "Four-prime screen finds q1^3 outside the minimal-weight span; "
            "this is not a proof of non-membership over Q."
        ),
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
