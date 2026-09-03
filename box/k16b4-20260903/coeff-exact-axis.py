#!/usr/bin/env python3
"""Exact fixed-t b4-axis evaluator for the charged coefficient recurrence.

Elements of A_t are stored as pairs (constant, d coefficient), with
3*d^2=t+1.  The residual variables and b3 are zero and b4 is one, so the
returned terminal values are exactly the coefficients c_{t,k} in
T_{t,k}|axis=c_{t,k} b4^(4t+1-k).
"""

from __future__ import annotations

import argparse
import math
from fractions import Fraction as F


class QD:
    __slots__ = ("b", "a", "t")

    def __init__(self, b=0, a=0, t=None):
        self.b, self.a, self.t = F(b), F(a), t

    def _q(self, other):
        return other if isinstance(other, QD) else QD(other, 0, self.t)

    def __add__(self, other):
        other = self._q(other)
        return QD(self.b + other.b, self.a + other.a, self.t)

    __radd__ = __add__

    def __neg__(self):
        return QD(-self.b, -self.a, self.t)

    def __sub__(self, other):
        return self + (-self._q(other))

    def __rsub__(self, other):
        return self._q(other) - self

    def __mul__(self, other):
        other = self._q(other)
        h = F(self.t + 1, 3)
        return QD(self.b * other.b + h * self.a * other.a,
                  self.b * other.a + self.a * other.b, self.t)

    __rmul__ = __mul__

    def inverse(self):
        h = F(self.t + 1, 3)
        norm = self.b * self.b - h * self.a * self.a
        if norm == 0:
            raise ZeroDivisionError((self.t, self.b, self.a))
        return QD(self.b / norm, -self.a / norm, self.t)

    def __truediv__(self, other):
        return self * self._q(other).inverse()

    def __rtruediv__(self, other):
        return self._q(other) / self

    def __eq__(self, other):
        other = self._q(other)
        return self.b == other.b and self.a == other.a

    def __repr__(self):
        return f"({self.a})*d+({self.b})"


def zeroes(n, t):
    return [QD(0, 0, t) for _ in range(n)]


def conv(left, right, degree, t):
    out = QD(0, 0, t)
    for i in range(degree + 1):
        if i < len(left) and degree - i < len(right):
            out += left[i] * right[degree - i]
    return out


def shift_to_l(coeffs, maximum, t):
    out = zeroes(maximum + 1, t)
    for exponent, coefficient in coeffs.items():
        for degree in range(exponent + 1):
            out[degree] += coefficient * math.comb(exponent, degree)
    return out


def pivot(t, j, d, g, y):
    q, e = 2 * t + 1, 3 * t + 1
    if j < t:
        ac = (9*j*j*t + 18*j*j - 54*j*t*t - 81*j*t - 26*j
              + 72*t**3 + 144*t*t + 88*t + 16)
        bc = (-9*j*j*t - 10*j*j + 24*j*t*t + 33*j*t + 10*j
              - 12*t**3 - 20*t*t - 8*t)
        return 3*t*e*(ac*d + bc) / ((t+1)*(3*t+2)**3*(4*t-2*j+1))
    if j <= 2*t:
        aq = 12*t*t + 16*t + 4 - j*(3*t+4)
        bq = 2*(t+1)*(j-t)
        return (-3*t*e*(q-j)*(aq*d+bq)
                / ((t+1)*q*(3*t+2)**2*(4*t-2*j+1)))
    return g*d/(2*y)


def l_arrays(t, solved_c, solved_u, b2):
    q, e, top = 2*t+1, 3*t+1, 4*t+1
    one, d = QD(1, 0, t), QD(0, 1, t)
    y = (d + t + 1)/(2*q)
    g = e*t*(3*d + 2*(t+1))/(6*q**3)
    ux = {q: one}
    for i in range(t, 2*t+1):
        ux[q-i] = solved_u.get(i, QD(0, 0, t))
    cx = {t-1: one}
    for j in range(1, t):
        cx[t-1-j] = solved_c.get(j, QD(0, 0, t))
    uu = shift_to_l(ux, q, t)
    cc = shift_to_l(cx, t-1, t)

    bb = zeroes(t+1, t)
    for m in range(t):
        bb[m+1] = g*(3*m+5)*cc[m]/(2*y*(m+1))

    ss = zeroes(2*t+1, t)
    for m in range(2*t+1):
        value = 3*g*(m+1)*(uu[m+1] if m+1 < len(uu) else 0)
        for aa in range(t):
            bi = m-1-aa
            if 0 <= bi < len(bb):
                value += (3+2*aa-bi)*cc[aa]*bb[bi]
        ss[m] = value/(y*(2*m+1))

    vv = zeroes(t+2, t)
    for degree in range(2, t+2):
        vv[degree] = cc[degree-2]
    yy = zeroes(2*t+2, t)
    yy[0] = -g*b2
    for degree in range(1, len(yy)):
        yy[degree] = ss[degree-1]
    zz = zeroes(t+2, t)
    for degree in range(1, len(zz)):
        zz[degree] = bb[degree-1] if degree-1 < len(bb) else QD(0, 0, t)

    vp = [(i+1)*vv[i+1] for i in range(len(vv)-1)]
    yp = [(i+1)*yy[i+1] for i in range(len(yy)-1)]
    up = [(i+1)*uu[i+1] for i in range(len(uu)-1)]
    nn = zeroes(e+1, t)
    for degree in range(e+1):
        nn[degree] = (-conv(vv, yp, degree, t)
                      + conv(vp, yy, degree, t)
                      + 2*conv(up, zz, degree, t))
    pp = [nn[degree+1]/(2*y) for degree in range(e)]
    rr = zeroes(top+1, t)
    for degree in range(top+1):
        rr[degree] = conv(vv, pp, degree, t) - conv(up, yy, degree, t)
    rr[0] -= y*g

    rx = zeroes(top+1, t)
    for degree in range(top+1):
        for higher in range(degree, top+1):
            rx[degree] += (math.comb(higher, degree)
                           * (-1)**(higher-degree) * rr[higher])
    return rr, rx


def terminal(t):
    q, top = 2*t+1, 4*t+1
    d = QD(0, 1, t)
    y = (d+t+1)/(2*q)
    g = (3*t+1)*t*(3*d+2*(t+1))/(6*q**3)
    solved_c, solved_u = {}, {}
    b2 = QD(0, 0, t)
    for j in range(1, 2*t+2):
        _rr, rx = l_arrays(t, solved_c, solved_u, b2)
        rho = rx[top-j]
        value = -rho/pivot(t, j, d, g, y)
        if j < t:
            solved_c[j] = value
        elif j <= 2*t:
            solved_u[j] = value
        else:
            b2 = value
    _rr, rx = l_arrays(t, solved_c, solved_u, b2)
    assert all(rx[k] == 0 for k in range(2*t, top+1))
    return [-rx[k] for k in range(2*t)], solved_c, solved_u, b2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("t", type=int, nargs="+", default=[2, 3, 4, 5])
    ap.add_argument("--rows", default="1,2,-1,-2,-3")
    args = ap.parse_args()
    for t in args.t:
        vals, _c, _u, _b2 = terminal(t)
        indices = []
        for token in args.rows.split(','):
            k = int(token)
            indices.append(k if k >= 0 else 2*t+k)
        print(f"t={t}")
        for k in indices:
            if 0 <= k < 2*t:
                print(f"  k={k} c={vals[k]}")


if __name__ == "__main__":
    main()
