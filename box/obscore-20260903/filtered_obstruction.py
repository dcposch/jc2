#!/usr/bin/env python3
"""Exact checks for the symbolic first-point block of the obstruction map.

This is deliberately a matrix/ODE check, not a new chart computation.  It
instantiates Fable's L_n on coefficient vectors and verifies the claimed
kernel in the two skeletons used by the certificate slice.
"""

from __future__ import annotations

import json
import sympy as sp
from sympy.polys.matrices import DomainMatrix


w = sp.symbols("w")


def coefficient_vector(poly: sp.Expr, degree: int) -> sp.Matrix:
    expanded = sp.Poly(sp.expand(poly), w, domain=sp.QQ)
    return sp.Matrix([expanded.nth(index) for index in range(degree + 1)])


def first_point_matrix(
    d2: int, d3: int, u3: int, v3: int, level: int
) -> tuple[sp.Matrix, sp.Expr, sp.Expr]:
    """Matrix of L_level on Q[w]_{<=d2} in ascending monomial bases."""
    assert d2 % d3 == 0
    assert u3 + v3 == d3
    degree_f = 3 * d2
    top_h3 = w**u3 * (w - 1) ** v3
    A0 = sp.expand(top_h3 ** (d2 // d3))

    def L(poly: sp.Expr) -> sp.Expr:
        return sp.expand(
            degree_f * A0 * sp.diff(poly, w)
            - (degree_f - 3 * level) * sp.diff(A0, w) * poly
        )

    image_degree = 2 * d2 - 1
    columns = [coefficient_vector(L(w**index), image_degree) for index in range(d2 + 1)]
    matrix = sp.Matrix.hstack(*columns)

    # Check the closed coefficient formula.  If A0=sum_a p_a*w^a, then
    # [w^ell]L(w^k)=(N*k-(N-3n)*a)*p_a, a=ell-k+1.
    A_poly = sp.Poly(A0, w, domain=sp.QQ)
    for ell in range(image_degree + 1):
        for k in range(d2 + 1):
            a = ell - k + 1
            p_a = A_poly.nth(a) if 0 <= a <= d2 else 0
            expected = (degree_f * k - (degree_f - 3 * level) * a) * p_a
            assert matrix[ell, k] == expected
    return matrix, top_h3, A0


def kernel_case(d2: int, d3: int, u3: int, v3: int, level: int) -> dict:
    matrix, top_h3, _A0 = first_point_matrix(d2, d3, u3, v3, level)
    rank = DomainMatrix.from_Matrix(matrix).to_field().rank()
    expected_dimension = 1 if level % d3 == 0 and level <= d2 else 0
    kernel_dimension = matrix.cols - rank
    assert kernel_dimension == expected_dimension
    expected_generator = None
    if expected_dimension:
        exponent = d2 // d3 - level // d3
        expected_generator = sp.expand(top_h3**exponent)
        expected_vector = coefficient_vector(expected_generator, d2)
        assert matrix * expected_vector == sp.zeros(matrix.rows, 1)
        # The rank computation gives nullity one, so membership proves equality
        # of the two one-dimensional spans without computing a costly rref.
    return {
        "d2": d2,
        "d3": d3,
        "u3": u3,
        "v3": v3,
        "level": level,
        "matrix_shape": list(matrix.shape),
        "rank": rank,
        "kernel_dimension": kernel_dimension,
        "kernel_generator": None if expected_generator is None else str(sp.factor(expected_generator)),
    }


def schur_identity() -> str:
    """Verify the scalar block-elimination identity used in the report."""
    a, b, c0, d = sp.symbols("a b c0 d", nonzero=True)
    obstruction = sp.Matrix([[a, b], [c0, d]])
    eliminator = sp.Matrix([[1, 0], [-c0 / a, 1]])
    reduced = sp.simplify(eliminator * obstruction)
    assert reduced == sp.Matrix([[a, b], [0, d - c0 * b / a]])
    assert sp.factor(obstruction.det()) == sp.factor(a * (d - c0 * b / a))
    return "det([[A,B],[C,D]])=det(A)*det(D-C*A^(-1)*B)"


def main() -> None:
    cases = [
        kernel_case(33, 11, 3, 8, 4),
        kernel_case(33, 11, 3, 8, 11),
        kernel_case(36, 9, 2, 7, 9),
    ]
    output = {
        "operator": "L_n(B)=N*A0*B'-(N-3*n)*A0'*B, N=3*d2, A0=(top_h3)^(d2/d3)",
        "entry_formula": "L[n]_(ell,k)=(N*k-(N-3*n)*(ell-k+1))*[w^(ell-k+1)]A0",
        "schur_identity": schur_identity(),
        "cases": cases,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
