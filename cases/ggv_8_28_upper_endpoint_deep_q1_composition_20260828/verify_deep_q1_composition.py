#!/usr/bin/env python3
"""Exact q1 composition and four-root face-rank checks.

This checker pins the preceding Newton/kernel packet, verifies the q1 active
collapse and constant source-shear coefficient, and computes over Q the full
linearization of the 20-equation four-root leading-face system at its square
homogeneous seed for A=X^4-1.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
import hashlib
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PREVIOUS = (
    ROOT
    / "cases/ggv_8_28_upper_endpoint_deep_newton_kernel_family_20260828"
    / "verify_deep_newton_kernel_family.py"
)
PREVIOUS_SHA256 = "0b873f2b4e0cdd4f55312dea6bf2d69d4fcbb3bb03c5725c082028148847c99f"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_previous():
    assert sha256(PREVIOUS) == PREVIOUS_SHA256
    spec = importlib.util.spec_from_file_location("deep_newton_frozen", PREVIOUS)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@dataclass(frozen=True)
class Jet:
    value: Q
    derivative: tuple[Q, ...]

    def _coerce(self, other):
        if isinstance(other, Jet):
            return other
        return Jet(Q(other), (Q(0),) * len(self.derivative))

    def __add__(self, other):
        other = self._coerce(other)
        return Jet(
            self.value + other.value,
            tuple(a + b for a, b in zip(self.derivative, other.derivative)),
        )

    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.value, tuple(-a for a in self.derivative))

    def __sub__(self, other):
        return self + (-self._coerce(other))

    def __rsub__(self, other):
        return self._coerce(other) - self

    def __mul__(self, other):
        other = self._coerce(other)
        return Jet(
            self.value * other.value,
            tuple(self.value * b + other.value * a
                  for a, b in zip(self.derivative, other.derivative)),
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self._coerce(other)
        assert other.value
        return Jet(
            self.value / other.value,
            tuple((a * other.value - self.value * b) / (other.value ** 2)
                  for a, b in zip(self.derivative, other.derivative)),
        )

    def __rtruediv__(self, other):
        return self._coerce(other) / self

    def __eq__(self, other):
        if isinstance(other, Jet):
            return self.value == other.value and self.derivative == other.derivative
        return self.value == other and all(not value for value in self.derivative)

    def __bool__(self):
        return bool(self.value) or any(self.derivative)


def jet_variable(value, index, size):
    derivative = [Q(0)] * size
    derivative[index] = Q(1)
    return Jet(Q(value), tuple(derivative))


def face_rows(previous):
    """Return the exact Jet coefficients z^7,...,z^11 of C(z)."""
    names = ["q", "e", "f"] + [f"d{k}" for k in range(1, 11)]
    size = len(names)
    index = {name: position for position, name in enumerate(names)}
    q = jet_variable(1, index["q"], size)
    e = jet_variable(0, index["e"], size)
    f = jet_variable(0, index["f"], size)
    literal = {
        1: Q(1), 2: Q(0), 3: Q(1), 4: Q(0), 5: Q(0), 6: Q(0),
        7: Q(-6139, 17179869184), 8: Q(0),
        9: Q(16369, 140737488355328), 10: Q(0),
    }
    modes = {
        k: jet_variable(literal[k], index[f"d{k}"], size)
        for k in range(1, 11)
    }
    zero = Jet(Q(0), (Q(0),) * size)
    one = Jet(Q(1), (Q(0),) * size)
    p = [one, -q / 8, q * q / 256, e / 2048, f] + [zero] * 7
    result = previous.series_power(p, Q(3, 2), 11)
    for k in range(1, 11):
        power = previous.series_power(p, Q(6 - k, 4), 11 - k)
        for degree, coefficient in enumerate(power):
            result[degree + k] += modes[k] * coefficient
    assert all(result[r].value == 0 for r in range(7, 11))
    assert result[11].value == Q(9207, 144115188075855872)
    return names, [result[r] for r in range(7, 12)]


def matrix_rank(matrix):
    rows = [list(row) for row in matrix]
    rank = 0
    columns = len(rows[0]) if rows else 0
    for column in range(columns):
        pivot = next((r for r in range(rank, len(rows)) if rows[r][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = rows[rank][column]
        rows[rank] = [value / scale for value in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][column]:
                factor = rows[r][column]
                rows[r] = [a - factor * b for a, b in zip(rows[r], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def main():
    previous = load_previous()
    tail = previous.load_tail()
    up = tail.load_upstream()

    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    Aprime = up.p_derivative(A)
    lam = Q(5, 7)
    R0 = up.p_scale(lam, A)
    V0 = up.p_add(
        up.p_mul(Aprime, R0),
        up.p_scale(2, up.p_mul(A, up.p_derivative(R0))),
    )
    assert V0 == up.p_scale(3 * lam, up.p_mul(A, Aprime))
    S = up.p_scale(3 * lam, Aprime)
    F0 = up.p_power(A, 4)
    F1 = up.p_mul(up.p_power(A, 3), S)
    shear = 3 * lam / 4
    assert F1 == up.p_scale(shear, up.p_derivative(F0))

    # The four-root leading system is represented in E=Q[X]/(X^4-1).
    # Variables: Q mod A (degrees 0..2), e1 mod A, F8 mod A,
    # ten global modes, and gamma.
    local_names, face = face_rows(previous)
    local_index = {name: i for i, name in enumerate(local_names)}
    local_qef = [
        [
            jet.derivative[local_index[name]]
            for name in ("q", "e", "f")
        ]
        for jet in face
    ]
    local_regularity_rank = matrix_rank(local_qef[:4])
    local_endpoint_augmented_rank = matrix_rank([
        row + [Q(1) if index == 4 else Q(0)]
        for index, row in enumerate(local_qef)
    ])
    columns = (
        [f"Q{j}" for j in range(3)]
        + [f"e{j}" for j in range(4)]
        + [f"f{j}" for j in range(4)]
        + [f"d{k}" for k in range(1, 11)]
        + ["gamma"]
    )
    column_index = {name: i for i, name in enumerate(columns)}
    matrix = []
    rhs = []
    for face_offset, jet in enumerate(face):
        r = 7 + face_offset
        dq = jet.derivative[local_index["q"]]
        de = jet.derivative[local_index["e"]]
        df = jet.derivative[local_index["f"]]
        for x_degree in range(4):
            row = [Q(0)] * len(columns)
            if x_degree <= 2:
                row[column_index[f"Q{x_degree}"]] = dq
            row[column_index[f"e{x_degree}"]] = de
            row[column_index[f"f{x_degree}"]] = df
            if x_degree == 0:
                for k in range(1, 11):
                    row[column_index[f"d{k}"]] = jet.derivative[
                        local_index[f"d{k}"]
                    ]
                if r == 11:
                    row[column_index["gamma"]] = -1
            matrix.append(row)
            # For A=X^4-1, I_A/8 = X^5/40-X/8 = -X/10 mod A.
            rhs.append(Q(-1, 10) if r == 11 and x_degree == 1 else Q(0))

    rank = matrix_rank(matrix)
    augmented_rank = matrix_rank([row + [value] for row, value in zip(matrix, rhs)])
    assert len(matrix) == 20 and len(columns) == 22
    assert local_regularity_rank == 3
    assert local_endpoint_augmented_rank == 4
    assert rank == 13 and augmented_rank == 14

    # A homogeneous q1 square seed realizes all four regularity equations;
    # its constant rho cannot meet the nonconstant primitive class -X/10.
    assert any(rhs)

    print("q1_active=R0_lambda_A;S=3lambda_Aprime")
    print("constant_source_shear=3lambda/4;kills_F1=true")
    print("lambda0_face_system=20_equations_22_variables")
    print(
        f"local_regularity_rank={local_regularity_rank};"
        f"local_endpoint_augmented_rank={local_endpoint_augmented_rank}"
    )
    print(f"four_root_rank={rank};augmented_rank={augmented_rank}")
    print("square_face_tangent_to_endpoint=OBSTRUCTED")
    print("PASS_EXACT_DEEP_Q1_COMPOSITION")


if __name__ == "__main__":
    main()
