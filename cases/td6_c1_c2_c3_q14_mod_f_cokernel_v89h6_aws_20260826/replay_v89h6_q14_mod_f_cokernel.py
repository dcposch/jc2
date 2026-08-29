#!/usr/bin/env python3
"""Splitting-independent q14 cokernel class after exact F=0 specialization."""

from fractions import Fraction
from hashlib import sha256
import importlib.util
import os
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
H5_PATH = HERE / "replay_v89h5_q14_high_unimodular_total_f_v1.py"
H5_SHA256 = "a81c358b58f8b97ec0dfd97128d0f9539782eda70e66a6747a4c2827a1539b9b"
assert sha256(H5_PATH.read_bytes()).hexdigest() == H5_SHA256
spec = importlib.util.spec_from_file_location("td6_v89h6_h5_parent", H5_PATH)
h5 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = h5
spec.loader.exec_module(h5)

v87, v85, m = h5.v87, h5.v85, h5.m
QPoly, E3, Rat3 = h5.QPoly, h5.E3, h5.Rat3
C, V, U, F, H, B3 = h5.C, h5.V, h5.U, h5.F, h5.H, h5.B3
TAIL = h5.TAIL
PRIME = 1000003
BASE_C, BASE_V, BASE_U = 8, 3, 1


def specialize_qpoly(value):
    value = QPoly.coerce(value)
    return QPoly(0, {
        monomial: v85.specialize_e3(coefficient)
        for monomial, coefficient in value.coefficients.items()
        if v85.specialize_e3(coefficient)
    })


def specialize_polynomial(polynomial):
    return v87.clean({
        monomial: specialize_qpoly(value)
        for monomial, value in polynomial.items()
        if specialize_qpoly(value)
    })


def specialize_first(first):
    return [
        (
            key,
            {
                variable: specialize_qpoly(coefficient)
                for variable, coefficient in row.items()
                if specialize_qpoly(coefficient)
            },
            specialize_qpoly(rhs),
        )
        for key, row, rhs in first
    ]


def invert_full_q_pivot(first, pivots):
    """Invert the full pivot block over E3[q], SCC by SCC, without q division."""
    A0 = [
        [row.get(pivot, QPoly()).constant() for pivot in pivots]
        for _, row, _ in first
    ]
    A = [
        [row.get(pivot, QPoly()) for pivot in pivots]
        for _, row, _ in first
    ]
    inverse_A0 = h5.inverse_constant_matrix(A0)
    B = h5.matmul_constant_q(inverse_A0, A)
    assert all(
        B[i][j].constant() == (E3(1) if i == j else E3())
        for i in range(38) for j in range(38)
    )
    N = [
        [B[i][j] - QPoly(1 if i == j else 0) for j in range(38)]
        for i in range(38)
    ]
    graph = {
        i: {j for j in range(38) if N[i][j]}
        for i in range(38)
    }
    components, cyclic = h5.strongly_connected(graph)

    D = [[QPoly(1 if i == j else 0) for j in range(38)] for i in range(38)]
    inverse_D = [row[:] for row in D]
    block_lines = ["component\tsize\tdeterminant_digest"]
    for component in cyclic:
        block = [[B[i][j] for j in component] for i in component]
        determinant, inverse = h5.adjugate_unit_inverse(block)
        assert determinant == QPoly(1)
        block_lines.append(
            f"{component!r}\t{len(component)}\t{h5.qpoly_digest(determinant)}"
        )
        for local_i, i in enumerate(component):
            for local_j, j in enumerate(component):
                D[i][j] = block[local_i][local_j]
                inverse_D[i][j] = inverse[local_i][local_j]
    assert h5.is_identity(h5.matmul_q(D, inverse_D))
    assert h5.is_identity(h5.matmul_q(inverse_D, D))

    reduced = h5.matmul_q(inverse_D, B)
    order, condensation = h5.condensation_order(graph, components)
    permuted = [
        [reduced[order[i]][order[j]] for j in range(38)]
        for i in range(38)
    ]
    assert all(
        permuted[i][i] == QPoly(1)
        and all(not permuted[i][j] for j in range(i))
        for i in range(38)
    )
    inverse_reduced = h5.polynomial_matrix_inverse(reduced, order)
    inverse_B = h5.matmul_q(inverse_reduced, inverse_D)
    assert h5.is_identity(h5.matmul_q(B, inverse_B))
    assert h5.is_identity(h5.matmul_q(inverse_B, B))
    T = h5.matmul_q(inverse_B, [
        [QPoly(value) for value in row] for row in inverse_A0
    ])
    assert h5.is_identity(h5.matmul_q(T, A))
    telemetry = {
        "edges": sum(map(len, graph.values())),
        "components": components,
        "cyclic": cyclic,
        "order": order,
        "condensation_edges": sum(map(len, condensation.values())),
        "block_text": "\n".join(block_lines) + "\n",
    }
    return T, telemetry


def original_relations(quotients, T):
    relations = []
    for source_index in range(38):
        relation = {}
        for quotient, row in zip(quotients, T):
            if row[source_index]:
                relation = v87.add(
                    relation, v87.scale(quotient, row[source_index])
                )
        relations.append(relation)
    return relations


def positive_part(polynomial):
    return v87.clean({
        monomial: QPoly(0, {
            q_monomial: coefficient
            for q_monomial, coefficient in value.coefficients.items()
            if q_monomial
        })
        for monomial, value in polynomial.items()
    })


def qpoly_support(polynomial):
    return sorted({
        q_monomial
        for value in polynomial.values()
        for q_monomial in value.coefficients
        if q_monomial
    })


def fmpq_mod(value, prime):
    fraction = Fraction(str(value))
    denominator = fraction.denominator % prime
    assert denominator
    return (fraction.numerator % prime) * pow(denominator, prime - 2, prime) % prime


def polynomial_mod(polynomial, prime, cvalue, vvalue, uvalue):
    out = 0
    for exponents, coefficient in polynomial.to_dict().items():
        ec, ev, eu = exponents
        term = fmpq_mod(coefficient, prime)
        term = term * pow(cvalue, ec, prime) % prime
        term = term * pow(vvalue, ev, prime) % prime
        term = term * pow(uvalue, eu, prime) % prime
        out = (out + term) % prime
    return out


def rat3_mod(value, prime, cvalue, vvalue, uvalue):
    value = Rat3.coerce(value)
    numerator = polynomial_mod(value.numerator, prime, cvalue, vvalue, uvalue)
    denominator = polynomial_mod(value.denominator, prime, cvalue, vvalue, uvalue)
    assert denominator, ("bad_prime_denominator", value)
    return numerator * pow(denominator, prime - 2, prime) % prime


class EModFactory:
    def __init__(self, prime, tensor, one_coordinates):
        self.prime = prime
        self.tensor = tensor
        self.zero = EMod(self, (0,) * 18)
        self.one = EMod(self, one_coordinates)

    def scalar(self, value):
        return self.one * (value % self.prime)


class EMod:
    __slots__ = ("factory", "coordinates")

    def __init__(self, factory, coordinates):
        self.factory = factory
        self.coordinates = tuple(value % factory.prime for value in coordinates)
        assert len(self.coordinates) == 18

    @staticmethod
    def coerce(value, factory):
        if isinstance(value, EMod):
            assert value.factory is factory
            return value
        return factory.scalar(int(value))

    def __add__(self, other):
        other = EMod.coerce(other, self.factory)
        return EMod(self.factory, tuple(
            left + right for left, right in zip(self.coordinates, other.coordinates)
        ))

    __radd__ = __add__

    def __neg__(self):
        return EMod(self.factory, tuple(-value for value in self.coordinates))

    def __sub__(self, other):
        return self + (-EMod.coerce(other, self.factory))

    def __rsub__(self, other):
        return EMod.coerce(other, self.factory) - self

    def __mul__(self, other):
        if isinstance(other, int):
            return EMod(self.factory, tuple(other * value for value in self.coordinates))
        other = EMod.coerce(other, self.factory)
        prime = self.factory.prime
        out = [0] * 18
        for i, left in enumerate(self.coordinates):
            if not left:
                continue
            for j, right in enumerate(other.coordinates):
                if not right:
                    continue
                scale = left * right
                for k, structure in enumerate(self.factory.tensor[i][j]):
                    if structure:
                        out[k] = (out[k] + scale * structure) % prime
        return EMod(self.factory, tuple(out))

    __rmul__ = __mul__

    def inverse(self):
        if not self:
            raise ZeroDivisionError
        columns = []
        for index in range(18):
            basis = [0] * 18
            basis[index] = 1
            columns.append((self * EMod(self.factory, tuple(basis))).coordinates)
        matrix = [
            [columns[column][row] for column in range(18)]
            + [self.factory.one.coordinates[row]]
            for row in range(18)
        ]
        prime = self.factory.prime
        for column in range(18):
            pivot = next(
                (row for row in range(column, 18) if matrix[row][column]), None
            )
            assert pivot is not None, ("nonunit_mod_prime", self.coordinates)
            if pivot != column:
                matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            scale = pow(matrix[column][column], prime - 2, prime)
            matrix[column] = [(entry * scale) % prime for entry in matrix[column]]
            for row in range(18):
                if row == column or not matrix[row][column]:
                    continue
                scale = matrix[row][column]
                matrix[row] = [
                    (left - scale * right) % prime
                    for left, right in zip(matrix[row], matrix[column])
                ]
        result = EMod(self.factory, tuple(matrix[row][-1] for row in range(18)))
        assert self * result == self.factory.one
        return result

    def __truediv__(self, other):
        return self * EMod.coerce(other, self.factory).inverse()

    def __bool__(self):
        return any(self.coordinates)

    def __eq__(self, other):
        if isinstance(other, int):
            other = self.factory.scalar(other)
        return (
            isinstance(other, EMod)
            and self.factory is other.factory
            and self.coordinates == other.coordinates
        )

    def __repr__(self):
        return f"EMod({self.coordinates!r})"


def build_mod_factory():
    # Trial division is deterministic and cheap at this preregistered prime.
    assert PRIME > 2 and all(PRIME % divisor for divisor in range(2, int(PRIME**0.5) + 1))
    basis = []
    for index in range(18):
        coordinates = [Rat3() for _ in range(18)]
        coordinates[index] = Rat3(1)
        basis.append(m.from_vector(tuple(coordinates)))

    def evaluate_e3(value):
        return tuple(
            rat3_mod(coordinate, PRIME, BASE_C, BASE_V, BASE_U)
            for coordinate in m.r.scalar_coordinates(E3.coerce(value))
        )

    tensor = [
        [evaluate_e3(left * right) for right in basis]
        for left in basis
    ]
    factory = EModFactory(PRIME, tensor, evaluate_e3(E3(1)))
    return factory, evaluate_e3


def evaluate_qpoly(value, evaluate_e3, factory, q14):
    value = QPoly.coerce(value)
    out = factory.zero
    for monomial, coefficient in value.coefficients.items():
        scalar = 1
        for exponent in monomial:
            scalar = scalar * (q14 if exponent == 14 else 0) % PRIME
        if scalar:
            out += EMod(factory, evaluate_e3(coefficient)) * scalar
    return out


def evaluate_polynomial(polynomial, evaluate_e3, factory, q14):
    return {
        monomial: coefficient
        for monomial, value in polynomial.items()
        if (coefficient := evaluate_qpoly(value, evaluate_e3, factory, q14))
    }


def evaluate_first(first, evaluate_e3, factory, q14):
    return [
        (
            key,
            {
                variable: coefficient
                for variable, value in row.items()
                if (coefficient := evaluate_qpoly(value, evaluate_e3, factory, q14))
            },
            evaluate_qpoly(rhs, evaluate_e3, factory, q14),
        )
        for key, row, rhs in first
    ]


def invert_matrix_field(matrix, factory):
    size = len(matrix)
    work = [
        list(row)
        + [factory.one if i == j else factory.zero for j in range(size)]
        for i, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column]), None
        )
        assert pivot is not None, ("singular_prime_FIRST", column)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
        inverse = work[column][column].inverse()
        work[column] = [value * inverse for value in work[column]]
        for row in range(size):
            if row == column or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                left - factor * right
                for left, right in zip(work[row], work[column])
            ]
    inverse = [row[size:] for row in work]
    for i in range(size):
        for j in range(size):
            left = sum(
                (matrix[i][k] * inverse[k][j] for k in range(size)),
                factory.zero,
            )
            right = sum(
                (inverse[i][k] * matrix[k][j] for k in range(size)),
                factory.zero,
            )
            expected = factory.one if i == j else factory.zero
            assert left == expected and right == expected
    return inverse


def poly_add(left, right, coefficient, factory):
    out = dict(left)
    coefficient = EMod.coerce(coefficient, factory)
    for monomial, value in right.items():
        total = out.get(monomial, factory.zero) + coefficient * value
        if total:
            out[monomial] = total
        else:
            out.pop(monomial, None)
    return out


def poly_scale(polynomial, coefficient, factory):
    coefficient = EMod.coerce(coefficient, factory)
    return {
        monomial: coefficient * value
        for monomial, value in polynomial.items()
        if coefficient * value
    }


def poly_multiply(left, right, factory):
    out = {}
    for left_monomial, left_value in left.items():
        for right_monomial, right_value in right.items():
            monomial = tuple(sorted(left_monomial + right_monomial))
            total = out.get(monomial, factory.zero) + left_value * right_value
            if total:
                out[monomial] = total
            else:
                out.pop(monomial, None)
    return out


def prime_remainder(first, p12, pivots, evaluate_e3, factory, q14):
    evaluated_first = evaluate_first(first, evaluate_e3, factory, q14)
    sources = []
    for _, row, rhs in evaluated_first:
        source = {(): -rhs} if rhs else {}
        source.update({(variable,): coefficient for variable, coefficient in row.items()})
        sources.append(source)
    evaluated_p12 = evaluate_polynomial(p12, evaluate_e3, factory, q14)
    matrix = [
        [row.get(pivot, factory.zero) for pivot in pivots]
        for _, row, _ in evaluated_first
    ]
    inverse = invert_matrix_field(matrix, factory)
    normalized = []
    for row in inverse:
        value = {}
        for coefficient, source in zip(row, sources):
            if coefficient:
                value = poly_add(value, source, coefficient, factory)
        normalized.append(value)
    for i, source in enumerate(normalized):
        for j, pivot in enumerate(pivots):
            assert source.get((pivot,), factory.zero) == (
                factory.one if i == j else factory.zero
            )

    remainder = dict(evaluated_p12)
    for pivot, source in zip(pivots, normalized):
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
            remainder = poly_add(
                remainder, poly_multiply(multiplier, source, factory), -1, factory
            )
    assert all(not set(monomial).intersection(pivots) for monomial in remainder)
    return remainder


def write_prime_polynomial(path, polynomial):
    lines = ["parameter_monomial\tcoordinates_mod_p"]
    lines.extend(
        f"{monomial!r}\t{coefficient.coordinates!r}"
        for monomial, coefficient in sorted(polynomial.items())
    )
    text = "\n".join(lines) + "\n"
    path.write_text(text)
    return sha256(text.encode()).hexdigest()


def main():
    outdir = Path(os.environ["TD6_OUTPUT_DIR"]).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    assert os.environ.get("AWS_RUN_TAG", "").startswith(
        "td6_v89h6_q14_mod_f_cokernel_"
    )
    print("producer=TD6-V89H6-Q14-MOD-F-COKERNEL")
    print(f"h5_parent_sha256={H5_SHA256}")
    print("tail_q_exponents=" + ",".join(map(str, TAIL)))
    print("low_q_specialized_zero=true")
    print("q15_absent_target_shear=true")
    print("exact_Q_and_independent_good_prime=true", flush=True)

    events, bands, seen = v87.build_bands()
    total_first = v87.compile_first(bands)
    total_p12 = v87.compile_current_degree12(bands)
    first = h5.project_first(total_first)
    p12 = h5.project_polynomial(total_p12)
    assert events == 2 and len(first) == 38
    assert all(seen[exponent] == 1 for exponent in TAIL)
    original_sources = [
        v87.source_polynomial(row, rhs) for _, row, rhs in first
    ]
    raw_coefficients, raw_common = v87.assert_denominators_allowed(
        [p12, *original_sources]
    )
    assert raw_common.gcd(F).total_degree() == 0
    print("literal_transport_FIRST_P12_rebuilt=true")
    print(f"raw_source_common_denominator=({raw_common})")
    print(f"raw_source_common_denominator_factor={raw_common.factor()}")
    print("raw_source_denominator_coprime_F=true", flush=True)

    assert v85.specialize_e3(E3(Rat3(F))) == E3()
    specialized_first = specialize_first(first)
    specialized_p12 = specialize_polynomial(p12)
    specialized_sources = [
        v87.source_polynomial(row, rhs) for _, row, rhs in specialized_first
    ]
    pivots = h5.base_pivot_columns(specialized_first)
    T, telemetry = invert_full_q_pivot(specialized_first, pivots)
    normalized = [
        h5.linear_combination(T[i], specialized_sources) for i in range(38)
    ]
    for i, source in enumerate(normalized):
        for j, pivot in enumerate(pivots):
            assert source.get((pivot,), QPoly()) == QPoly(1 if i == j else 0)
    remainder, quotients = h5.divide_by_normalized_first(
        specialized_p12, normalized, pivots
    )
    relations = original_relations(quotients, T)
    replay = {}
    for relation, source in zip(relations, specialized_sources):
        replay = v87.add(replay, v87.multiply(relation, source))
    assert replay == v87.add(specialized_p12, remainder, -1)
    assert all(not set(monomial).intersection(pivots) for monomial in remainder)

    base_remainder = v87.q_constant(remainder)
    assert set(base_remainder) == {()}
    base_unit = base_remainder[()]
    base_unit.inverse()
    positive = positive_part(remainder)
    support = qpoly_support(positive)
    assert positive and support == [(14,)]
    remainder_sha = h5.write_polynomial(
        outdir / "Q14_MOD_F_CANONICAL_REMAINDER.tsv", remainder
    )
    positive_sha = h5.write_polynomial(
        outdir / "Q14_MOD_F_POSITIVE_COKERNEL_CLASS.tsv", positive
    )
    block_path = outdir / "Q14_MOD_F_SCC_BLOCKS.tsv"
    block_path.write_text(telemetry["block_text"])
    block_sha = sha256(telemetry["block_text"].encode()).hexdigest()
    print(f"specialized_FIRST_graph_edges={telemetry['edges']}")
    print(f"specialized_FIRST_cyclic_components={telemetry['cyclic']!r}")
    print(f"specialized_FIRST_condensation_edges={telemetry['condensation_edges']}")
    print(f"specialized_FIRST_SCC_blocks_sha256={block_sha}")
    print("specialized_full_q_pivot_inverse_two_sided=true")
    print("specialized_normalized_original_FIRST_replay=true")
    print("q_zero_remainder_scalar_unit=true")
    print(f"positive_q_support={support!r}")
    print(f"positive_parameter_records={len(positive)}")
    print(f"canonical_remainder_sha256={remainder_sha}")
    print(f"positive_cokernel_class_sha256={positive_sha}")
    print("positive_q14_cokernel_class_zero=false", flush=True)

    factory, evaluate_e3 = build_mod_factory()
    assert (BASE_C * BASE_U - BASE_V**2 + BASE_U**3) % PRIME == 0
    assert (BASE_C - 3 * BASE_U**2) % PRIME == 5
    b3_value = polynomial_mod(B3, PRIME, BASE_C, BASE_V, BASE_U)
    assert b3_value == 81
    prime_zero = prime_remainder(
        first, p12, pivots, evaluate_e3, factory, 0
    )
    prime_one = prime_remainder(
        first, p12, pivots, evaluate_e3, factory, 1
    )
    prime_delta = poly_add(prime_one, prime_zero, -1, factory)
    expected_delta = {
        monomial: coefficient
        for monomial, value in positive.items()
        if (coefficient := evaluate_qpoly(value, evaluate_e3, factory, 1))
    }
    assert prime_delta == expected_delta
    assert prime_delta
    prime_sha = write_prime_polynomial(
        outdir / "Q14_MOD_F_GOOD_PRIME_WITNESS.tsv", prime_delta
    )
    first_prime_monomial = min(prime_delta)
    first_prime_coordinates = prime_delta[first_prime_monomial].coordinates
    print(f"good_prime={PRIME}")
    print(f"good_prime_base_C_V_U={BASE_C},{BASE_V},{BASE_U}")
    print(f"good_prime_H={5}")
    print(f"good_prime_B3={b3_value}")
    print("good_prime_independent_FIRST_inverses_q14_0_q14_1=true")
    print("good_prime_delta_matches_exact_positive_class=true")
    print(f"good_prime_first_nonzero_parameter_monomial={first_prime_monomial!r}")
    print(f"good_prime_first_nonzero_coordinates={first_prime_coordinates!r}")
    print(f"good_prime_witness_sha256={prime_sha}", flush=True)

    exact_lines = [
        f"h5_parent_sha256={H5_SHA256}",
        f"raw_common={raw_common}",
        "F_specialization=C=(V^2-U^3)/U",
        f"pivots={pivots!r}",
        f"cyclic_components={telemetry['cyclic']!r}",
        f"canonical_remainder_sha256={remainder_sha}",
        f"positive_class_sha256={positive_sha}",
        f"positive_records={len(positive)}",
        "positive_q_support=(14,)",
        "positive_q14_cokernel_class_zero=false",
        f"good_prime={PRIME}",
        f"good_prime_base={BASE_C},{BASE_V},{BASE_U}",
        f"good_prime_witness_sha256={prime_sha}",
        "claim=splitting_independent_nonzero_q14_class_mod_F_over_fraction_field",
    ]
    exact_text = "\n".join(exact_lines) + "\n"
    exact_path = outdir / "Q14_MOD_F_COKERNEL_EXACT_RESULT.txt"
    exact_path.write_text(exact_text)
    exact_sha = sha256(exact_text.encode()).hexdigest()
    print(f"exact_result_sha256={exact_sha}")
    print("P12_FIRST_F_unit_ideal_claim=false")
    print("source_point_claim=false")
    print("low_q_unit_charts_covered=false")
    print("whole_fixed_A3_killed=false")
    print("whole_TD6_killed=false")
    print("JC2_resolved=false")
    print("TD6-V89H6-Q14-MOD-F-COKERNEL NONZERO-CLASS-PASS")
    v85.restore_base_qd_state()


if __name__ == "__main__":
    main()
