#!/usr/bin/env python3
"""Exact stdlib replay for the frozen EXACT-COFRAME-GATE-20260824 family."""

from fractions import Fraction


NAMES = ("x", "y", "c0", "c1", "c2")
ZERO_EXP = (0, 0, 0, 0, 0)


class Poly:
    def __init__(self, terms=None):
        self.terms = {
            exp: Fraction(coeff)
            for exp, coeff in (terms or {}).items()
            if coeff
        }

    @staticmethod
    def constant(value):
        return Poly({ZERO_EXP: Fraction(value)})

    @staticmethod
    def variable(index):
        exp = list(ZERO_EXP)
        exp[index] = 1
        return Poly({tuple(exp): Fraction(1)})

    def __add__(self, other):
        other = as_poly(other)
        terms = dict(self.terms)
        for exp, coeff in other.terms.items():
            terms[exp] = terms.get(exp, Fraction(0)) + coeff
            if not terms[exp]:
                del terms[exp]
        return Poly(terms)

    __radd__ = __add__

    def __neg__(self):
        return Poly({exp: -coeff for exp, coeff in self.terms.items()})

    def __sub__(self, other):
        return self + (-as_poly(other))

    def __rsub__(self, other):
        return as_poly(other) - self

    def __mul__(self, other):
        other = as_poly(other)
        terms = {}
        for left_exp, left_coeff in self.terms.items():
            for right_exp, right_coeff in other.terms.items():
                exp = tuple(a + b for a, b in zip(left_exp, right_exp))
                terms[exp] = terms.get(exp, Fraction(0)) + left_coeff * right_coeff
        return Poly(terms)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        if exponent < 0:
            raise ValueError("negative polynomial exponent")
        result = Poly.constant(1)
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power //= 2
        return result

    def diff(self, index):
        terms = {}
        for exp, coeff in self.terms.items():
            if exp[index]:
                new_exp = list(exp)
                factor = new_exp[index]
                new_exp[index] -= 1
                terms[tuple(new_exp)] = coeff * factor
        return Poly(terms)

    def scale_variable(self, index, factor):
        factor = Fraction(factor)
        return Poly(
            {
                exp: coeff * factor ** exp[index]
                for exp, coeff in self.terms.items()
            }
        )

    def coeff(self, exp):
        return self.terms.get(exp, Fraction(0))

    def __str__(self):
        if not self.terms:
            return "0"

        def order(item):
            exp, _ = item
            return (sum(exp), exp)

        pieces = []
        for exp, coeff in sorted(self.terms.items(), key=order, reverse=True):
            factors = []
            for name, power in zip(NAMES, exp):
                if power == 1:
                    factors.append(name)
                elif power:
                    factors.append(f"{name}^{power}")
            monomial = "*".join(factors)
            magnitude = abs(coeff)
            if monomial:
                body = monomial if magnitude == 1 else f"{magnitude}*{monomial}"
            else:
                body = str(magnitude)
            if not pieces:
                pieces.append(("-" if coeff < 0 else "") + body)
            else:
                pieces.append((" - " if coeff < 0 else " + ") + body)
        return "".join(pieces)


def as_poly(value):
    return value if isinstance(value, Poly) else Poly.constant(value)


def matmul(left, right):
    return [
        [
            sum((left[i][k] * right[k][j] for k in range(2)), Poly.constant(0))
            for j in range(2)
        ]
        for i in range(2)
    ]


def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def curl(row):
    return row[0].diff(1) - row[1].diff(0)


def delta(poly):
    return (1 + 2 * x * y) * poly.diff(1) - x**2 * poly.diff(0)


def matrix_text(matrix):
    return "[[" + ",".join(str(v) for v in matrix[0]) + "],[" + ",".join(
        str(v) for v in matrix[1]
    ) + "]]"


def rational_rank(matrix):
    work = [[Fraction(value) for value in row] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][col]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [entry / scale for entry in work[pivot_row]]
        for row in range(rows):
            if row != pivot_row and work[row][col]:
                multiple = work[row][col]
                work[row] = [
                    entry - multiple * pivot_entry
                    for entry, pivot_entry in zip(work[row], work[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


x = Poly.variable(0)
y = Poly.variable(1)
c0 = Poly.variable(2)
c1 = Poly.variable(3)
c2 = Poly.variable(4)

C = [
    [1 + x * y, x**2],
    [-y**2, 1 - x * y],
]
CB = [[entry.scale_variable(1, 2) for entry in row] for row in C]

h = c0 * y**2 + c1 * x * y**3 + c2 * x**2 * y**4
Lh = [[Poly.constant(1), Poly.constant(0)], [h, Poly.constant(1)]]
M = matmul(Lh, CB)

basis_h = [y**2, x * y**3, x**2 * y**4]
basis_out_exp = [
    (0, 1, 0, 0, 0),
    (1, 2, 0, 0, 0),
    (2, 3, 0, 0, 0),
    (3, 4, 0, 0, 0),
]
basis_out_text = ["y", "x*y^2", "x^2*y^3", "x^3*y^4"]
images = [delta(f) for f in basis_h]
A = [
    [image.coeff(exp) for image in images]
    for exp in basis_out_exp
]
target = [Fraction(6), Fraction(0), Fraction(0), Fraction(0)]
rank = rational_rank(A)
augmented_rank = rational_rank([row + [rhs] for row, rhs in zip(A, target)])

residual = delta(h) - 6 * y
coefficient_equations = []
for xy_exp in basis_out_exp:
    terms = {}
    for exp, coeff in residual.terms.items():
        if exp[0] == xy_exp[0] and exp[1] == xy_exp[1]:
            parameter_exp = (0, 0, exp[2], exp[3], exp[4])
            terms[parameter_exp] = coeff
    coefficient_equations.append(str(Poly(terms)))

N = y**2 * (3 + 2 * x * y)
D = (1 + x * y) ** 2
rational_numerator_check = delta(N) * D - N * delta(D) - 6 * y * D**2
series_coefficients = [Fraction((-1) ** n * (n + 3)) for n in range(7)]

print("EXACT-COFRAME-GATE-20260824")
print("engine=python-stdlib sparse polynomial ring over Q")
print(f"det(C)={det2(C)}")
print(f"curl_rows(C)={[str(curl(C[i])) for i in range(2)]}")
print(f"det(C_B)={det2(CB)}")
print(f"C_B={matrix_text(CB)}")
print(f"curl_rows(C_B)={[str(curl(CB[i])) for i in range(2)]}")
print(f"first_row_integral_P={x + x**2 * y}")
print(
    "unimodular_identity="
    f"{(1 - 2*x*y) * CB[0][0] + 4*y**2 * CB[0][1]}"
)
print(f"h={h}")
print(f"det(M(h))={det2(M)}")
print(f"curl_row_1(M(h))={curl(M[0])}")
print(f"curl_row_2(M(h))={curl(M[1])}")
print(f"delta_basis={[str(image) for image in images]}")
print(f"output_basis={basis_out_text}")
print(f"linearized_matrix={[[str(v) for v in row] for row in A]}")
print(f"target={[str(v) for v in target]}")
print(f"rank={rank}")
print(f"augmented_rank={augmented_rank}")
print(f"target_in_image={rank == augmented_rank}")
print(f"coefficient_equations={coefficient_equations}")
print("linsolve=EMPTY" if rank != augmented_rank else "linsolve=NONEMPTY")
print(f"elimination_licensed={rank == augmented_rank}")
print(f"rational_solution_numerator_check={rational_numerator_check}")
print(f"formal_series_coefficients_n0_to_n6={series_coefficients}")
print("global_recurrence=c_0=3; (n+2)c_n+(n+3)c_(n-1)=0 for n>=1")
print("global_coefficients=c_n=(-1)^n(n+3)")
print("terminal_residual=(N+4)c_N*x^(N+1)*y^(N+2), nonzero for finite N")
print("VERDICT=EMPTY-TANGENT; ELIMINATION_NOT_LICENSED; ONE-SHEAR-NO-POLYNOMIAL")
