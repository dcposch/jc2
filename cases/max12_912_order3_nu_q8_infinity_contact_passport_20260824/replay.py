#!/usr/bin/env python3
"""Light exact replay for the selected-Q8 infinity-contact passport gate."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PINS = {
    "xmodel/max12-912-order3-nu-q8-formal-branch-review-grok-20260824.md":
        "32750e4e350919d7d52984feab06d3cd2d801386caec5848f7c5750bf9e8e846",
    "xmodel/max12-912-order3-nu-q8-normalization-jet-review-claude-20260824.md":
        "e85c20f3cfc0ac76583c1b7152bc6c1d2963b00178a8bbe2acac8d14677572b7",
    "xmodel/max12-912-order3-nu-q8-leaf4-descent-jet-review-grok-20260824.md":
        "58fafc556fd916ff5cbe3c19b2effe95ef30fd8e4bc00d2bfbf35401b7f6ed8f",
    "xmodel/max12-912-order3-nu-q8-global-quotient-gate-review-claude-20260824.md":
        "49e8d9092e257a003f39171d0ec53fca91cc8f5c6e02841816f88aad127e6b39",
    "xmodel/max12-912-order3-terminal-belyi-classification-review-claude-20260824.md":
        "713e41def64d0fc313d254cae5d660e412f5ba9b69bd4d7c0e6c212a4688c52b",
    "cases/max12_912_order3_nu_q8_normalization_jet_20260824/FREEZE.txt":
        "807ad9dacbc477972c3c30b3770d84ca27340b5771ec2aad3efc90d7eb3e5b50",
    "cases/max12_912_order3_nu_q8_leaf4_descent_jet_20260824/FREEZE.txt":
        "700ddb29d01de5075de3f5a4f7cc2df00f8b35aa6a59803e778ee3c87edb7de2",
    "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/FREEZE.txt":
        "c34fff2b838ca4803872b709857ae7becb1751a7e1ce261c9fa8c7e6d8b46c97",
    "cases/max12_912_order3_terminal_belyi_classification_20260824/FREEZE.txt":
        "0c5b862fd4f784e3e258881c39a16dbd14d3c53f9aafe9426cfec8102f5018d9",
}


def trim(poly):
    value = tuple(Fraction(c) for c in poly)
    while len(value) > 1 and value[-1] == 0:
        value = value[:-1]
    return value


ZERO = trim((0,))
ONE = trim((1,))
X = trim((0, 1))


def padd(a, b):
    return trim(tuple(
        (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
        for i in range(max(len(a), len(b)))
    ))


def pneg(a):
    return trim(tuple(-c for c in a))


def psub(a, b):
    return padd(a, pneg(b))


def pmul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return trim(out)


def pscale(a, scalar):
    return trim(tuple(Fraction(scalar) * c for c in a))


def ppow(a, exponent):
    out, base = ONE, a
    power = exponent
    while power:
        if power & 1:
            out = pmul(out, base)
        power //= 2
        if power:
            base = pmul(base, base)
    return out


def pder(a):
    return trim(tuple(i * a[i] for i in range(1, len(a))) or (0,))


def pdivmod(a, b):
    if b == ZERO:
        raise ZeroDivisionError
    rem = list(a)
    quotient = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while trim(rem) != ZERO and len(trim(rem)) >= len(b):
        rem = list(trim(rem))
        shift = len(rem) - len(b)
        scalar = rem[-1] / b[-1]
        quotient[shift] += scalar
        for i, value in enumerate(b):
            rem[i + shift] -= scalar * value
    return trim(quotient), trim(rem)


def pmonic(a):
    if a == ZERO:
        return ZERO
    return pscale(a, 1 / a[-1])


def pgcd(a, b):
    left, right = a, b
    while right != ZERO:
        left, right = right, pdivmod(left, right)[1]
    return pmonic(left)


def pdegree(a):
    return len(a) - 1


def radical_degree(a):
    if a == ZERO:
        raise ValueError("zero polynomial")
    return pdegree(a) - pdegree(pgcd(a, pder(a)))


class Rat:
    def __init__(self, numerator, denominator=ONE):
        self.n = trim(numerator)
        self.d = trim(denominator)
        if self.d == ZERO:
            raise ZeroDivisionError

    @classmethod
    def scalar(cls, value):
        return cls((Fraction(value),))

    def __add__(self, other):
        other = other if isinstance(other, Rat) else Rat.scalar(other)
        return Rat(padd(pmul(self.n, other.d), pmul(other.n, self.d)),
                   pmul(self.d, other.d))

    __radd__ = __add__

    def __neg__(self):
        return Rat(pneg(self.n), self.d)

    def __sub__(self, other):
        return self + (-other if isinstance(other, Rat) else -Rat.scalar(other))

    def __rsub__(self, other):
        return (other if isinstance(other, Rat) else Rat.scalar(other)) - self

    def __mul__(self, other):
        other = other if isinstance(other, Rat) else Rat.scalar(other)
        return Rat(pmul(self.n, other.n), pmul(self.d, other.d))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = other if isinstance(other, Rat) else Rat.scalar(other)
        return Rat(pmul(self.n, other.d), pmul(self.d, other.n))

    def __pow__(self, exponent):
        if exponent < 0:
            return Rat(ppow(self.d, -exponent), ppow(self.n, -exponent))
        return Rat(ppow(self.n, exponent), ppow(self.d, exponent))

    def derivative(self):
        return Rat(psub(pmul(pder(self.n), self.d), pmul(self.n, pder(self.d))),
                   ppow(self.d, 2))

    def __eq__(self, other):
        other = other if isinstance(other, Rat) else Rat.scalar(other)
        return pmul(self.n, other.d) == pmul(other.n, self.d)


def ext_add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def ext_scale(value, scalar):
    scalar = scalar if isinstance(scalar, Rat) else Rat.scalar(scalar)
    return tuple(coefficient * scalar for coefficient in value)


def ext_mul(left, right, modulus):
    out = [Rat.scalar(0), Rat.scalar(0), Rat.scalar(0)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            exponent = i + j
            coefficient = a * b
            if exponent >= 3:
                exponent -= 3
                coefficient = coefficient * modulus
            out[exponent] = out[exponent] + coefficient
    return tuple(out)


def ext_pow(value, exponent, modulus):
    out = (Rat.scalar(1), Rat.scalar(0), Rat.scalar(0))
    base = value
    power = exponent
    while power:
        if power & 1:
            out = ext_mul(out, base, modulus)
        power //= 2
        if power:
            base = ext_mul(base, base, modulus)
    return out


def ext_derivative(value, modulus):
    log_derivative = modulus.derivative() / (3 * modulus)
    return tuple(
        coefficient.derivative() + i * log_derivative * coefficient
        for i, coefficient in enumerate(value)
    )


def ext_scalar(value):
    return (value if isinstance(value, Rat) else Rat.scalar(value),
            Rat.scalar(0), Rat.scalar(0))


def main():
    for relative, expected in PINS.items():
        got = sha256((ROOT / relative).read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((relative, got, expected))

    # Exact e_pass=2 control.
    A = padd(ONE, ppow(X, 2))
    B = ppow(X, 2)
    C = psub(A, B)
    W = psub(pmul(pder(A), B), pmul(A, pder(B)))
    assert W == pscale(X, -2)
    assert pgcd(A, B) == ONE
    assert pgcd(A, C) == ONE and pgcd(B, C) == ONE

    T = Rat(A, B)
    assert T.derivative() == Rat(W, ppow(B, 2))
    h = Rat(pmul(ppow(A, 2), ppow(B, 4)), ppow(W, 3))
    h_expected = Rat(pscale(padd(ppow(X, 9),
                                  pscale(ppow(X, 7), 2),
                                  ), Fraction(-1, 8)))
    # The previous line deliberately builds x^9+2x^7 first; add x^5 here.
    h_expected = h_expected + Rat(pscale(ppow(X, 5), Fraction(-1, 8)))
    assert h == h_expected
    Z = T ** 3
    assert h ** 3 * Z.derivative() ** 9 == (3 ** 9) * Z ** 8

    e_pass = pdegree(B) - pdegree(C)
    r = radical_degree(A)
    s = radical_degree(B)
    rad_degree = radical_degree(pmul(pmul(A, B), C))
    assert (e_pass, r, s, rad_degree) == (2, 2, 1, 3)
    assert r + s == e_pass + 1
    assert rad_degree == pdegree(A) + 1

    # Exact terminal/Kummer lift over xi^3=T, with nu=1, j=3.
    xi = (Rat.scalar(0), Rat.scalar(1), Rat.scalar(0))
    u = ext_scale(ext_pow(xi, 2, T), Rat(pscale(ppow(X, 3), Fraction(-1, 2))))
    r8 = xi
    R = Rat((4,), pmul(ppow(X, 4), A))
    assert ext_pow(u, 3, T) == ext_scalar(h)
    assert ext_scale(ext_pow(u, 2, T), R) == r8
    assert ext_pow(r8, 9, T) == ext_scalar(Z)
    assert ext_scale(ext_mul(ext_derivative(r8, T), u, T), 9) == ext_scalar(3)

    payload = {
        "status": "PASS",
        "scope": (
            "reviewed-parent contact/passport consequences and exact "
            "terminal-Kummer positive control; not coefficient realization"
        ),
        "reviewed_parent_sha256": PINS,
        "contact": {
            "surjectivity_input": "nonconstant P1_x map to selected projective normalization",
            "finite_contact_exclusion": "forces the selected Q8 preimage to x=infinity",
            "local_order_identity": "e_pass=ord_infinity(T-lambda)=2*ord_infinity(a0)",
            "passport_e_is_even": True,
        },
        "mason": {
            "identity": "deg(rad(A*B*(A-lambda*B)))=D+1",
            "meaning": "Mason-Stothers equality, not an obstruction",
        },
        "positive_control": {
            "T": "(x^2+1)/x^2",
            "Z": "T^3",
            "h": "-x^5*(x^2+1)^2/8",
            "W": "-2*x",
            "D": 2,
            "e_pass": e_pass,
            "passport": {"0": [1, 1], "infinity": [2], "1": [2]},
            "h_degree": 9,
            "h_finite_multiplicities": [5, 2, 2],
            "h_is_noncube": True,
            "radical_degree": rad_degree,
            "terminal_constants": {"nu": 1, "j": 3},
            "kummer": {
                "extension": "xi^3=T",
                "u": "-x^3*xi^2/2",
                "r8": "xi",
                "R": "4/(x^4*(x^2+1))",
                "u_cubed_is_h": True,
                "r8_is_u_squared_R": True,
                "r8_ninth_is_Z": True,
                "nine_r8_prime_is_j_over_u": True,
                "characters_under_sigma_xi=zeta^2_xi": {
                    "u": 1, "r8": 2, "R": 0,
                },
            },
        },
        "charged": [
            "global selected-component identification",
            "lift through the original seven-row coefficient fibre",
            "both complete Taylor polynomiality families at r=A_source/9",
            "all projective boundaries and coprimality conditions",
        ],
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
