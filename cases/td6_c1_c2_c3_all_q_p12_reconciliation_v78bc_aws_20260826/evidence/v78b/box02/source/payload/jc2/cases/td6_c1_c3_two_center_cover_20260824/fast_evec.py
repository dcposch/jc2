"""Fast linear arithmetic in E(C) as 18 coordinates over Q(C).

This representation is intended only for operations linear over Q(C).  It
avoids polynomial gcds over the degree-18 field in the dense first-J backsolve.
Conversion back to the canonical Frac representation is exact and replayed.
"""


class EVecFactory:
    def __init__(self, cp):
        self.cp = cp
        self.rt = cp.rt
        self.E = cp.E
        self.K = cp.K

    def e_coords(self, value):
        value = self.E(value)
        out = []
        for a_degree in range(3):
            out.extend(value.coefficients[a_degree].coefficients)
        assert len(out) == 18
        return out

    def coords_e(self, values):
        assert len(values) == 18
        values = [
            self.cp.q_to_fraction(self.rt.rational(value)) for value in values
        ]
        return self.E([
            self.K(values[6 * a_degree: 6 * (a_degree + 1)])
            for a_degree in range(3)
        ])

    def _qpoly_from_e_poly(self, poly):
        poly = self.cp.Poly(poly)
        return self.rt.fmpq_poly([
            self.rt.rational(self.cp.e_to_q(coefficient))
            for coefficient in poly.coefficients
        ])

    def from_frac(self, value):
        value = self.cp.Frac.coerce(value)
        denominator = self._qpoly_from_e_poly(value.denominator)
        numerators = [[] for _ in range(18)]
        for coefficient in value.numerator.coefficients:
            for index, coordinate in enumerate(self.e_coords(coefficient)):
                numerators[index].append(self.rt.rational(coordinate))
        return EVec(self, tuple(
            self.rt.Rat(self.rt.fmpq_poly(entries), denominator)
            for entries in numerators
        ))

    def to_frac(self, vector):
        vector = EVec.coerce(vector, self)
        denominator = self.rt.ONE
        for coordinate in vector.coordinates:
            old = denominator
            common = old.gcd(coordinate.denominator)
            denominator = (old // common) * coordinate.denominator
            if denominator:
                denominator = self.rt.monic(denominator)
        scaled = []
        max_degree = -1
        for coordinate in vector.coordinates:
            quotient = denominator // coordinate.denominator
            numerator = coordinate.numerator * quotient
            scaled.append(numerator)
            max_degree = max(max_degree, numerator.degree())
        # Remove the exact common Q[C] content across all 18 coordinates.
        # This is sufficient for a deterministic linear representation and
        # avoids an extremely expensive gcd over the degree-18 coefficient
        # field in Frac.__init__.
        common = denominator
        for numerator in scaled:
            if numerator:
                common = common.gcd(numerator)
        if common and common.degree() >= 0 and common != self.rt.ONE:
            denominator //= common
            scaled = [numerator // common for numerator in scaled]
            max_degree = max((value.degree() for value in scaled), default=-1)
        coefficients = []
        for degree in range(max_degree + 1):
            coefficients.append(self.coords_e([
                coordinate[degree] if degree <= coordinate.degree() else 0
                for coordinate in scaled
            ]))
        denominator_e = self.cp.Poly([
            self.E(self.cp.q_to_fraction(denominator[degree]))
            for degree in range(denominator.degree() + 1)
        ]) if denominator else self.cp.Poly(1)
        result = self.cp.Frac(
            self.cp.Poly(coefficients), denominator_e, normalized=True
        )
        assert self.from_frac(result) == vector
        return result

    def zero(self):
        return EVec(self, (self.rt.Rat(),) * 18)

    def constant(self, value):
        return self.from_frac(self.cp.Frac(value))


class EVec:
    __slots__ = ("factory", "coordinates")

    def __init__(self, factory, coordinates):
        self.factory = factory
        self.coordinates = tuple(coordinates)
        assert len(self.coordinates) == 18

    @staticmethod
    def coerce(value, factory):
        if isinstance(value, EVec):
            assert value.factory is factory
            return value
        return factory.constant(value)

    def __add__(self, other):
        other = EVec.coerce(other, self.factory)
        return EVec(self.factory, tuple(
            left + right for left, right in zip(self.coordinates, other.coordinates)
        ))

    __radd__ = __add__

    def __neg__(self):
        return EVec(self.factory, tuple(-value for value in self.coordinates))

    def __sub__(self, other):
        return self + (-EVec.coerce(other, self.factory))

    def __rsub__(self, other):
        return EVec.coerce(other, self.factory) - self

    def scale(self, scalar):
        scalar = self.factory.rt.Rat.coerce(scalar)
        return EVec(self.factory, tuple(scalar * value for value in self.coordinates))

    def __bool__(self):
        return any(self.coordinates)

    def __eq__(self, other):
        return (
            isinstance(other, EVec)
            and self.factory is other.factory
            and self.coordinates == other.coordinates
        )

    def __repr__(self):
        return f"EVec({self.coordinates!r})"
