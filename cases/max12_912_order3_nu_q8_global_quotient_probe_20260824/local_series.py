#!/usr/bin/env python3
"""High-order local series on the approximate-cubic quotient at Q8."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
COMPILER = Path(__file__).with_name("quotient_compiler.py")
DESCENT = ROOT / "cases/max12_912_order3_nu_q8_leaf4_descent_jet_20260824/replay.py"
DESCENT_SHA256 = "5dcb0a67d79859c04d83d2c20ff8518a148a78c1229f42b00169c5842d5e7256"


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


if sha256(DESCENT.read_bytes()).hexdigest() != DESCENT_SHA256:
    raise RuntimeError("descent dependency hash mismatch")
Q = load("q8_high_quotient", COMPILER)
D = load("q8_high_descent", DESCENT)
J = D.J
P, M, G = J.P, J.M, J.G
NF = J.NF
ZERO, ONE = J.ZERO, J.ONE
ORDER = 6  # coefficients through w^5


@dataclass(frozen=True)
class Series:
    coefficients: tuple[NF, ...]

    def __init__(self, coefficients=()):
        values = [NF(value) for value in coefficients]
        values.extend([ZERO] * (ORDER - len(values)))
        object.__setattr__(self, "coefficients", tuple(values[:ORDER]))

    @staticmethod
    def constant(value):
        return Series((value,))

    def __add__(self, other):
        other = other if isinstance(other, Series) else Series.constant(other)
        return Series([a + b for a, b in zip(self.coefficients, other.coefficients)])

    __radd__ = __add__

    def __neg__(self):
        return Series([-value for value in self.coefficients])

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return Series.constant(other) - self

    def __mul__(self, other):
        other = other if isinstance(other, Series) else Series.constant(other)
        out = [ZERO] * ORDER
        for i, left in enumerate(self.coefficients):
            for k, right in enumerate(other.coefficients):
                if i + k < ORDER:
                    out[i + k] = out[i + k] + left * right
        return Series(out)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out, base, power = Series.constant(1), self, exponent
        while power:
            if power & 1:
                out = out * base
            base = base * base
            power >>= 1
        return out

    def inverse(self):
        if not self.coefficients[0]:
            raise ZeroDivisionError
        out = [ZERO] * ORDER
        out[0] = self.coefficients[0].inverse()
        for degree in range(1, ORDER):
            correction = sum((
                self.coefficients[index] * out[degree - index]
                for index in range(1, degree + 1)
            ), ZERO)
            out[degree] = -out[0] * correction
        result = Series(out)
        assert (self * result).coefficients == (ONE,) + (ZERO,) * (ORDER - 1)
        return result

    def __truediv__(self, other):
        other = other if isinstance(other, Series) else Series.constant(other)
        return self * other.inverse()


def evaluate(poly, bases):
    powers = []
    for index, base in enumerate(bases):
        maximum = max((monomial[index] for monomial in poly), default=0)
        row = [Series.constant(1)]
        for _ in range(maximum):
            row.append(row[-1] * base)
        powers.append(row)
    total = Series.constant(0)
    for monomial, scalar in poly.items():
        term = Series.constant(scalar)
        for index, exponent in enumerate(monomial):
            term = term * powers[index][exponent]
        total = total + term
    return total


def digest(value):
    return [J.digest(coefficient) for coefficient in value.coefficients]


def pade_test(value, numerator_degree, denominator_degree):
    """Fit a normalized denominator and expose every unused residual."""
    coefficients = value.coefficients
    equations = []
    rhs = []
    for degree in range(numerator_degree + 1,
                        numerator_degree + denominator_degree + 1):
        equations.append([
            coefficients[degree - index]
            for index in range(1, denominator_degree + 1)
        ])
        rhs.append(-coefficients[degree])
    try:
        denominator_tail = J.solve(equations, rhs)
    except RuntimeError:
        return {"fit": "SINGULAR"}
    residuals = []
    for degree in range(numerator_degree + denominator_degree + 1, ORDER):
        residual = coefficients[degree] + sum((
            denominator_tail[index - 1] * coefficients[degree - index]
            for index in range(1, denominator_degree + 1)
        ), ZERO)
        residuals.append({"degree": degree, **J.digest(residual)})
    return {
        "fit": "SOLVED",
        "denominator_tail": [J.digest(value) for value in denominator_tail],
        "unused_residuals": residuals,
        "all_unused_zero": all(not item["nonzero"] for item in residuals),
    }


def fraction_mod(value, prime):
    return value.numerator % prime * pow(value.denominator % prime, -1, prime) % prime


def modular_rank(matrix, prime):
    data = [[entry % prime for entry in row] for row in matrix]
    rows = len(data)
    columns = len(data[0]) if rows else 0
    rank = 0
    for column in range(columns):
        pivot = next((row for row in range(rank, rows) if data[row][column]), None)
        if pivot is None:
            continue
        data[rank], data[pivot] = data[pivot], data[rank]
        inverse = pow(data[rank][column], -1, prime)
        data[rank] = [value * inverse % prime for value in data[rank]]
        for row in range(rows):
            if row == rank or not data[row][column]:
                continue
            factor = data[row][column]
            data[row] = [
                (left - factor * right) % prime
                for left, right in zip(data[row], data[rank])
            ]
        rank += 1
        if rank == rows:
            break
    return rank


def bidegree_search(value):
    powers = [Series.constant(1)]
    for _ in range(10):
        powers.append(powers[-1] * value)
    primes = (1000003, 1000033)
    results = []
    for z_degree in range(1, 11):
        for w_degree in range(0, 5):
            columns = []
            for wi in range(w_degree + 1):
                for zi in range(z_degree + 1):
                    shifted = [ZERO] * ORDER
                    for degree in range(ORDER - wi):
                        shifted[degree + wi] = powers[zi].coefficients[degree]
                    columns.append(shifted)
            if len(columns) > ORDER * 8:
                continue
            nullities = []
            for prime in primes:
                matrix = []
                for w_index in range(ORDER):
                    for v_index in range(8):
                        matrix.append([
                            fraction_mod(
                                column[w_index].poly[v_index]
                                if v_index < len(column[w_index].poly)
                                else Fraction(0),
                                prime,
                            )
                            for column in columns
                        ])
                nullities.append(len(columns) - modular_rank(matrix, prime))
            if any(nullities):
                results.append({
                    "z_degree": z_degree,
                    "w_degree": w_degree,
                    "columns": len(columns),
                    "nullity_mod_primes": nullities,
                })
    return results


def rectangular_search(left, right, maximum_degree=4):
    left_powers = [Series.constant(1)]
    right_powers = [Series.constant(1)]
    for _ in range(maximum_degree):
        left_powers.append(left_powers[-1] * left)
        right_powers.append(right_powers[-1] * right)
    primes = (1000003, 1000033)
    results = []
    for left_degree in range(1, maximum_degree + 1):
        for right_degree in range(1, maximum_degree + 1):
            column_count = (left_degree + 1) * (right_degree + 1)
            if column_count > ORDER * 8:
                continue
            columns = [
                left_powers[i] * right_powers[j]
                for i in range(left_degree + 1)
                for j in range(right_degree + 1)
            ]
            nullities = []
            for prime in primes:
                matrix = []
                for w_index in range(ORDER):
                    for v_index in range(8):
                        matrix.append([
                            fraction_mod(
                                column.coefficients[w_index].poly[v_index]
                                if v_index < len(column.coefficients[w_index].poly)
                                else Fraction(0),
                                prime,
                            )
                            for column in columns
                        ])
                nullities.append(column_count - modular_rank(matrix, prime))
            if any(nullities):
                results.append({
                    "left_degree": left_degree,
                    "right_degree": right_degree,
                    "columns": column_count,
                    "nullity_mod_primes": nullities,
                })
    return results


def main():
    ring, rows, imposed, names = Q.compile_quotient("approx")
    assert names == Q.APPROX_NAMES

    # Recover the Q8 tangent in the x0-parameter chart from the frozen raw
    # normal tangent.  q=t*c, x2=t*d2, x4=t*d4.
    compiled = P.compile_fibre()
    tails = compiled["tails"]
    v = NF((Fraction(0), Fraction(1)))
    D0 = 3 * v ** 2 - 2
    A20 = 3 * v ** 2 + 3 * v + 1
    x5 = -36 * v ** 2 * A20 / D0
    x3 = x5 * (v + 2)
    x1 = x5 * (v + 1) + x5 ** 2 * (3 * v + 1) / (9 * v)
    raw_base = [ZERO, x1, ZERO, ONE + x3, ZERO, NF(3) + x5, ZERO, NF(3), ZERO]
    normals = (0, 2, 4, 6)
    odd = (3, 5, 7)
    matrix = [
        [J.nf_eval(M.cpartial(tails[ell], column), raw_base)
         for column in normals[1:]]
        for ell in odd
    ]
    rhs = [
        -J.nf_eval(M.cpartial(tails[ell], 0), raw_base)
        for ell in odd
    ]
    a2_t, a4_t, a6_t = J.solve(matrix, rhs)
    c0 = a6_t / 3
    d20 = a2_t - a6_t
    d40 = a4_t - 2 * a6_t
    constants = [c0, d20, d40, x1, x3, x5]

    w = Series((ZERO, ONE))
    variables = [Series.constant(value) for value in constants]
    equation_rows = [rows[ell] for ell in imposed]
    unknown_names = names[1:]
    step_digests = {}
    for degree in range(1, ORDER):
        bases = [w] + variables
        origin = [evaluate(row, bases).coefficients[degree] for row in equation_rows]
        columns = []
        for column in range(6):
            changed = list(variables)
            coefficients = list(changed[column].coefficients)
            coefficients[degree] = ONE
            changed[column] = Series(coefficients)
            image = [
                evaluate(row, [w] + changed).coefficients[degree]
                for row in equation_rows
            ]
            columns.append([
                image[row] - origin[row] for row in range(6)
            ])
        linear = [[columns[column][row] for column in range(6)] for row in range(6)]
        solution = J.solve(linear, [-entry for entry in origin])
        for index, coefficient in enumerate(solution):
            values = list(variables[index].coefficients)
            values[degree] = coefficient
            variables[index] = Series(values)
        step_digests[f"w^{degree}"] = {
            name: J.digest(value)
            for name, value in zip(unknown_names, solution)
        }

    bases = [w] + variables
    for row in equation_rows:
        assert not any(evaluate(row, bases).coefficients)
    n = evaluate(rows[6], bases)  # n=r6/p^9; p=1 on this quotient chart.
    q = evaluate(rows[8], bases)  # q_tail=r8/p^10; p=1.
    Z = q ** 9 / n ** 10
    assert n.coefficients[0] and q.coefficients[0]
    assert J.digest(n.coefficients[0])["sha256"] == (
        "06823a513df67730e83894fdd95227eb5bdaa5968acd1faf2719620aa09ccd71"
    )
    assert J.digest(q.coefficients[0])["sha256"] == (
        "96515608dcfae3970795ad7ef99542a1713ab01c9517aaa827428fe59f7a8c88"
    )
    assert J.digest(q.coefficients[1])["sha256"] == (
        "87b80678a4a92f8e768bc4cd4f118a425bc797cef61f720392e0ae8a716590cc"
    )

    payload = {
        "case": "max12_912_order3_nu_q8_global_quotient_local_series_20260824",
        "chart": (
            "p=1; K=z^3+z+q_cubic; t=x0; q_cubic=t*c; "
            "x2=t*d2; x4=t*d4; w=t^2"
        ),
        "field": "Q[v]/(Q8)",
        "order": "through w^5",
        "six_rows": "PASS",
        "coefficient_digests": step_digests,
        "outputs": {
            "n=r6/p^9": digest(n),
            "q=r8/p^10": digest(q),
            "Z=q^9/n^10": digest(Z),
        },
        "low_degree_rational_falsifiers": {
            label: {
                f"[{m}/{d}]": pade_test(value, m, d)
                for m, d in ((1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (1, 3))
            }
            for label, value in (("n", n), ("q", q), ("Z", Z))
        },
        "bounded_Q_bidegree_search_for_Z": {
            "series_equations": 48,
            "primes": [1000003, 1000033],
            "range": "1<=deg_Z<=10, 0<=deg_w<=4, at most 48 columns",
            "nonzero_nullities": bidegree_search(Z),
        },
        "bounded_Q_relation_search_n_q": {
            "series_equations": 48,
            "primes": [1000003, 1000033],
            "range": (
                "1<=deg_n,deg_q<=4"
            ),
            "nonzero_nullities": rectangular_search(n, q),
        },
        "actual_fixed_load_reconstruction": {
            "pi=p^9": "nu/n",
            "S=r8^9": "nu^10*Z",
            "terminal": "nu^10*h^3*(Z')^9=j^9*Z^8",
        },
        "scope": (
            "high-order formal series only; no guessed global relation is "
            "accepted without an exact polynomial replay"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
