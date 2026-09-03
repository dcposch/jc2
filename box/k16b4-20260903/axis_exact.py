#!/usr/bin/env python3
"""Exact b4-axis evaluator for the charged coefficient-array recurrence.

The implementation is specialized to b4=1, b3=q_(2,0)=...=q_(t-1,0)=0.
Elements of A_t=Q[d]/(3*d^2-(t+1)) are stored as ``a*d+b`` pairs.  The
terminal convention here is the question/Sol convention T=[X^k]E; the frozen
Laurent JSON stores the negative of these rows.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from fractions import Fraction


@dataclass(frozen=True)
class Q2:
    """a*d+b in Q[d]/(d^2-(t+1)/3)."""

    t: int
    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    @staticmethod
    def coerce(t: int, value: object) -> "Q2":
        if isinstance(value, Q2):
            if value.t != t:
                raise ValueError("coefficient algebras differ")
            return value
        return Q2(t, Fraction(0), Fraction(value))

    def __add__(self, other: object) -> "Q2":
        z = self.coerce(self.t, other)
        return Q2(self.t, self.a + z.a, self.b + z.b)

    __radd__ = __add__

    def __neg__(self) -> "Q2":
        return Q2(self.t, -self.a, -self.b)

    def __sub__(self, other: object) -> "Q2":
        return self + (-self.coerce(self.t, other))

    def __rsub__(self, other: object) -> "Q2":
        return self.coerce(self.t, other) - self

    def __mul__(self, other: object) -> "Q2":
        z = self.coerce(self.t, other)
        square = Fraction(self.t + 1, 3)
        return Q2(self.t,
                  self.a * z.b + self.b * z.a,
                  self.b * z.b + self.a * z.a * square)

    __rmul__ = __mul__

    def field_norm(self) -> Fraction:
        return self.b * self.b - Fraction(self.t + 1, 3) * self.a * self.a

    def inverse(self) -> "Q2":
        norm = self.field_norm()
        if norm == 0:
            raise ZeroDivisionError(f"nonunit {self}")
        return Q2(self.t, -self.a / norm, self.b / norm)

    def __truediv__(self, other: object) -> "Q2":
        return self * self.coerce(self.t, other).inverse()

    def __rtruediv__(self, other: object) -> "Q2":
        return self.coerce(self.t, other) / self

    def __bool__(self) -> bool:
        return bool(self.a or self.b)

    def as_json(self) -> dict[str, str]:
        return {
            "d_coefficient": str(self.a),
            "constant_coefficient": str(self.b),
            "field_norm": str(self.field_norm()),
            "resultant_y": str(4 * (2 * self.t + 1) ** 2 * 3 * self.field_norm()),
        }


def convolve(left: list[Q2], right: list[Q2], degree: int, zero: Q2) -> Q2:
    return sum((left[i] * right[degree - i]
                for i in range(degree + 1)
                if i < len(left) and degree - i < len(right)), zero)


def shift_to_l(coefficients: dict[int, Q2], maximum: int, one: Q2) -> list[Q2]:
    answer = [Q2(one.t) for _ in range(maximum + 1)]
    for exponent, coefficient in coefficients.items():
        for degree in range(exponent + 1):
            answer[degree] += coefficient * math.comb(exponent, degree)
    return answer


def l_arrays(t: int, solved_c: dict[int, Q2], solved_u: dict[int, Q2],
             b2: Q2) -> tuple[list[Q2], list[Q2]]:
    q, e, top = 2 * t + 1, 3 * t + 1, 4 * t + 1
    zero, one = Q2(t), Q2(t, b=Fraction(1))
    y = Q2(t, Fraction(1, 2 * q), Fraction(t + 1, 2 * q))
    g = Q2(t, Fraction(e * t, 2 * q**3),
           Fraction(e * t * (t + 1), 3 * q**3))

    ux = {q: one}
    for index in range(t, 2 * t + 1):
        ux[q - index] = solved_u.get(index, zero)
    cx = {t - 1: one}
    for index in range(1, t):
        cx[t - 1 - index] = solved_c.get(index, zero)
    uu = shift_to_l(ux, q, one)
    cc = shift_to_l(cx, t - 1, one)

    bb = [zero for _ in range(t + 1)]
    for degree in range(t):
        bb[degree + 1] = g * (3 * degree + 5) * cc[degree] / (2 * y * (degree + 1))

    ss = [zero for _ in range(2 * t + 1)]
    for degree in range(2 * t + 1):
        value = 3 * g * (degree + 1) * (uu[degree + 1] if degree + 1 < len(uu) else zero)
        for aa in range(t):
            bindex = degree - 1 - aa
            if 0 <= bindex < len(bb):
                value += (3 + 2 * aa - bindex) * cc[aa] * bb[bindex]
        ss[degree] = value / (y * (2 * degree + 1))

    vv = [zero for _ in range(t + 2)]
    for degree in range(2, t + 2):
        vv[degree] = cc[degree - 2]
    yy = [zero for _ in range(2 * t + 2)]
    yy[0] = -g * b2
    for degree in range(1, len(yy)):
        yy[degree] = ss[degree - 1]
    zz = [zero for _ in range(t + 2)]
    for degree in range(1, len(zz)):
        zz[degree] = bb[degree - 1] if degree - 1 < len(bb) else zero

    vp = [(i + 1) * vv[i + 1] for i in range(len(vv) - 1)]
    yp = [(i + 1) * yy[i + 1] for i in range(len(yy) - 1)]
    up = [(i + 1) * uu[i + 1] for i in range(len(uu) - 1)]
    nn = [zero for _ in range(e + 1)]
    for degree in range(e + 1):
        nn[degree] = (-convolve(vv, yp, degree, zero)
                      + convolve(vp, yy, degree, zero)
                      + 2 * convolve(up, zz, degree, zero))
    pp = [nn[degree + 1] / (2 * y) for degree in range(e)]
    rr = [zero for _ in range(top + 1)]
    for degree in range(top + 1):
        rr[degree] = (convolve(vv, pp, degree, zero)
                      - convolve(up, yy, degree, zero))
    rr[0] -= y * g

    rx = [zero for _ in range(top + 1)]
    for degree in range(top + 1):
        rx[degree] = sum((math.comb(higher, degree) * (-1) ** (higher - degree)
                                  * rr[higher]
                                  for higher in range(degree, top + 1)), zero)
    return rr, rx


def axis_rows(t: int) -> tuple[list[Q2], list[dict[str, object]]]:
    zero, one = Q2(t), Q2(t, b=Fraction(1))
    solved_c: dict[int, Q2] = {}
    solved_u: dict[int, Q2] = {}
    b2 = zero
    pivots: list[dict[str, object]] = []
    top = 4 * t + 1
    for weight in range(1, 2 * t + 2):
        def at(value: Q2) -> Q2:
            trial_c, trial_u, trial_b2 = dict(solved_c), dict(solved_u), b2
            if weight < t:
                trial_c[weight] = value
            elif weight <= 2 * t:
                trial_u[weight] = value
            else:
                trial_b2 = value
            return l_arrays(t, trial_c, trial_u, trial_b2)[1][top - weight]

        rho = at(zero)
        pivot = at(one) - rho
        value = -rho / pivot
        if weight < t:
            solved_c[weight] = value
            variable = f"C_{weight}"
        elif weight <= 2 * t:
            solved_u[weight] = value
            variable = f"q_{{{weight},0}}"
        else:
            b2 = value
            variable = "b2"
        pivots.append({"weight": weight, "variable": variable,
                       "coefficient": pivot.as_json(), "value": value.as_json()})
    _rl, rx = l_arrays(t, solved_c, solved_u, b2)
    assert not any(rx[degree] for degree in range(2 * t, top + 1))
    # rr/rx are the frozen-record sign R=-E.  Return T=E.
    return [-rx[degree] for degree in range(2 * t)], pivots


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("t", type=int, nargs="+", help="integer parameters >=2")
    parser.add_argument("--include-pivots", action="store_true")
    args = parser.parse_args()
    for t in args.t:
        if t < 2:
            raise ValueError("stable recurrence starts at t=2")
        rows, pivots = axis_rows(t)
        payload: dict[str, object] = {
            "t": t,
            "algebra": f"Q[d]/(3*d^2-{t+1})",
            "specialization": {"b4": 1, "b3": 0,
                               **{f"q_{j},0": 0 for j in range(2, t)}},
            "sign": "question convention T=[X^k]E; frozen JSON is -T",
            "rows": [{"k": k, "weight": 4 * t + 1 - k, **row.as_json()}
                     for k, row in enumerate(rows)],
        }
        if args.include_pivots:
            payload["pivots"] = pivots
        print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
