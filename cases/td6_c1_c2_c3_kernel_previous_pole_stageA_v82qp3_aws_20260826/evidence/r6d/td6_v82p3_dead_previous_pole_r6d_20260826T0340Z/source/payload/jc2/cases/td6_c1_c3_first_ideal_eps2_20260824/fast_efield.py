"""Exact fast E(C) arithmetic using the tower E=K[A]/(A^3-alpha).

Coordinates lie in FLINT-backed Q(C).  This is a genuine field
representation, unlike fast_evec's linear-only wrapper, and supports the
small E(C)-matrix stages without polynomial gcds over a custom degree-18
coefficient class.
"""


def poly_trim(poly):
    poly = list(poly)
    while poly and not poly[-1]:
        poly.pop()
    return poly


def poly_add(left, right):
    if len(left) < len(right):
        left, right = right, left
    if not left:
        return []
    zero = left[0] - left[0]
    out = list(left) + [zero] * max(0, len(right) - len(left))
    for index, value in enumerate(right):
        out[index] = out[index] + value
    return poly_trim(out)


def poly_neg(poly):
    return [-value for value in poly]


def poly_sub(left, right):
    return poly_add(left, poly_neg(right))


def poly_mul(left, right):
    if not left or not right:
        return []
    zero = left[0] - left[0]
    out = [zero] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        if a:
            for j, b in enumerate(right):
                if b:
                    out[i + j] = out[i + j] + a * b
    return poly_trim(out)


def poly_divmod(left, right):
    left, right = poly_trim(left), poly_trim(right)
    if not right:
        raise ZeroDivisionError
    if not left:
        return [], []
    zero = right[0] - right[0]
    quotient = [zero] * max(0, len(left) - len(right) + 1)
    inverse_lead = right[-1].inverse()
    while len(left) >= len(right):
        degree = len(left) - len(right)
        coefficient = left[-1] * inverse_lead
        quotient[degree] = quotient[degree] + coefficient
        for index, value in enumerate(right):
            left[degree + index] = left[degree + index] - coefficient * value
        left = poly_trim(left)
    return poly_trim(quotient), left


def poly_extended_gcd(left, right):
    left, right = poly_trim(left), poly_trim(right)
    one = next(value for value in (left + right) if value)
    one = one / one
    zero = one - one
    old_r, r = left, right
    old_s, s = [one], []
    old_t, t = [], [one]
    while r:
        quotient, remainder = poly_divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, poly_sub(old_s, poly_mul(quotient, s))
        old_t, t = t, poly_sub(old_t, poly_mul(quotient, t))
    if not old_r:
        return [], [], []
    scale = old_r[-1].inverse()
    return (
        [value * scale for value in old_r],
        [value * scale for value in old_s],
        [value * scale for value in old_t],
    )


class EFieldFactory:
    def __init__(self, cp):
        self.cp = cp
        self.rt = cp.rt
        self.vector_factory = cp.fast_evec.EVecFactory(cp)
        self.k_modulus = tuple(
            self.rt.Rat(self.rt.rational(value)) for value in cp.qd.uniform.F_MONIC
        )
        self.k_zero = KField(self, (self.rt.Rat(),) * 6)
        self.k_one = KField(self, (self.rt.Rat(1),) + (self.rt.Rat(),) * 5)
        self.alpha = self.from_k(cp.qd.uniform.ALPHA)
        self.zero = EField(self, (self.k_zero,) * 3)
        self.one = EField(self, (self.k_one, self.k_zero, self.k_zero))

    def from_k(self, value):
        value = self.cp.K(value)
        return KField(self, tuple(
            self.rt.Rat(self.rt.rational(coordinate))
            for coordinate in value.coefficients
        ))

    def from_e(self, value):
        value = self.cp.E(value)
        return EField(self, tuple(self.from_k(coordinate) for coordinate in value.coefficients))

    def scalar(self, value):
        value = self.rt.Rat.coerce(value)
        kvalue = KField(self, (value,) + (self.rt.Rat(),) * 5)
        return EField(self, (kvalue, self.k_zero, self.k_zero))

    def from_frac(self, value):
        value = self.cp.Frac.coerce(value)
        try:
            vector = self.vector_factory.from_frac(value)
            return self.from_coordinates(vector.coordinates)
        except AssertionError:
            # Canonical Frac normalization may scale a Q(C) denominator by
            # an E-unit.  Evaluate both E[C] polynomials in this field.
            cvalue = self.scalar(self.rt.Rat(self.rt.X))

            def evaluate(poly):
                out = self.zero
                power = self.one
                for coefficient in self.cp.Poly(poly).coefficients:
                    out = out + self.from_e(coefficient) * power
                    power = power * cvalue
                return out

            return evaluate(value.numerator) / evaluate(value.denominator)

    def from_coordinates(self, coordinates):
        assert len(coordinates) == 18
        return EField(self, tuple(
            KField(self, tuple(coordinates[6 * index: 6 * (index + 1)]))
            for index in range(3)
        ))

    def to_frac(self, value):
        value = EField.coerce(value, self)
        coordinates = tuple(
            coordinate
            for kvalue in value.coefficients
            for coordinate in kvalue.coordinates
        )
        return self.vector_factory.to_frac(
            self.cp.fast_evec.EVec(self.vector_factory, coordinates)
        )


class KField:
    __slots__ = ("factory", "coordinates")

    def __init__(self, factory, coordinates):
        self.factory = factory
        self.coordinates = tuple(coordinates)
        assert len(self.coordinates) == 6

    @staticmethod
    def coerce(value, factory):
        if isinstance(value, KField):
            assert value.factory is factory
            return value
        if isinstance(value, factory.rt.Rat):
            return KField(factory, (value,) + (factory.rt.Rat(),) * 5)
        return factory.from_k(value)

    def __add__(self, other):
        other = KField.coerce(other, self.factory)
        return KField(self.factory, tuple(
            left + right for left, right in zip(self.coordinates, other.coordinates)
        ))

    __radd__ = __add__

    def __neg__(self):
        return KField(self.factory, tuple(-value for value in self.coordinates))

    def __sub__(self, other):
        return self + (-KField.coerce(other, self.factory))

    def __rsub__(self, other):
        return KField.coerce(other, self.factory) - self

    def __mul__(self, other):
        other = KField.coerce(other, self.factory)
        zero = self.factory.rt.Rat()
        product = [zero] * 11
        for i, left in enumerate(self.coordinates):
            if left:
                for j, right in enumerate(other.coordinates):
                    if right:
                        product[i + j] = product[i + j] + left * right
        modulus = self.factory.k_modulus
        for degree in range(10, 5, -1):
            coefficient = product[degree]
            if coefficient:
                for index in range(6):
                    product[degree - 6 + index] = (
                        product[degree - 6 + index] - coefficient * modulus[index]
                    )
        return KField(self.factory, tuple(product[:6]))

    __rmul__ = __mul__

    def inverse(self):
        if not self:
            raise ZeroDivisionError
        gcd, coefficient, _ = poly_extended_gcd(
            list(self.coordinates), list(self.factory.k_modulus)
        )
        assert len(gcd) == 1 and gcd[0] == self.factory.rt.Rat(1)
        coordinates = coefficient + [self.factory.rt.Rat()] * (6 - len(coefficient))
        result = KField(self.factory, tuple(coordinates[:6]))
        assert self * result == self.factory.k_one
        return result

    def __truediv__(self, other):
        return self * KField.coerce(other, self.factory).inverse()

    def __rtruediv__(self, other):
        return KField.coerce(other, self.factory) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out = self.factory.k_one
        base = self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return any(self.coordinates)

    def __eq__(self, other):
        return (
            isinstance(other, KField)
            and self.factory is other.factory
            and self.coordinates == other.coordinates
        )

    def __repr__(self):
        return f"KField({self.coordinates!r})"


class EField:
    __slots__ = ("factory", "coefficients")

    def __init__(self, factory, coefficients):
        self.factory = factory
        self.coefficients = tuple(coefficients)
        assert len(self.coefficients) == 3

    @staticmethod
    def coerce(value, factory):
        if isinstance(value, EField):
            assert value.factory is factory
            return value
        if isinstance(value, factory.cp.Frac):
            return factory.from_frac(value)
        if isinstance(value, factory.rt.Rat):
            return factory.scalar(value)
        return factory.from_e(value)

    def __add__(self, other):
        other = EField.coerce(other, self.factory)
        return EField(self.factory, tuple(
            left + right for left, right in zip(self.coefficients, other.coefficients)
        ))

    __radd__ = __add__

    def __neg__(self):
        return EField(self.factory, tuple(-value for value in self.coefficients))

    def __sub__(self, other):
        return self + (-EField.coerce(other, self.factory))

    def __rsub__(self, other):
        return EField.coerce(other, self.factory) - self

    def __mul__(self, other):
        other = EField.coerce(other, self.factory)
        zero = self.factory.k_zero
        product = [zero] * 5
        for i, left in enumerate(self.coefficients):
            if left:
                for j, right in enumerate(other.coefficients):
                    if right:
                        product[i + j] = product[i + j] + left * right
        for degree in range(4, 2, -1):
            if product[degree]:
                product[degree - 3] = (
                    product[degree - 3] + product[degree] * self.factory.alpha
                )
        return EField(self.factory, tuple(product[:3]))

    __rmul__ = __mul__

    def inverse(self):
        if not self:
            raise ZeroDivisionError
        modulus = [-self.factory.alpha, self.factory.k_zero, self.factory.k_zero, self.factory.k_one]
        gcd, coefficient, _ = poly_extended_gcd(list(self.coefficients), modulus)
        assert len(gcd) == 1 and gcd[0] == self.factory.k_one
        coefficients = coefficient + [self.factory.k_zero] * (3 - len(coefficient))
        result = EField(self.factory, tuple(coefficients[:3]))
        assert self * result == self.factory.one
        return result

    def __truediv__(self, other):
        return self * EField.coerce(other, self.factory).inverse()

    def __rtruediv__(self, other):
        return EField.coerce(other, self.factory) / self

    def __pow__(self, exponent):
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out = self.factory.one
        base = self
        while exponent:
            if exponent & 1:
                out *= base
            base *= base
            exponent //= 2
        return out

    def __bool__(self):
        return any(self.coefficients)

    def __eq__(self, other):
        return (
            isinstance(other, EField)
            and self.factory is other.factory
            and self.coefficients == other.coefficients
        )

    def __repr__(self):
        return f"EField({self.coefficients!r})"
