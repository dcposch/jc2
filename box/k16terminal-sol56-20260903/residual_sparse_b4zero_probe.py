#!/usr/bin/env python3
"""Sparse finite-field b4=0 specialization of the proved Laurent recurrence.

This is a checking driver: it uses the proved high-pivot formulas, verifies
each pivot row after substitution, and can compare its output with a banked
modular terminal record.  It deliberately keeps the two split fibres separate.
Artifact lane: k16terminal-sol56-20260903.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


class SparseProbe:
    def __init__(self, t: int, prime: int, yvalue: int):
        self.t, self.p, self.y = t, prime, yvalue % prime
        self.m = t - 1
        self.zero = {}
        self.one = {(0,) * self.m: 1}
        self.e, self.q, self.N = 3 * t + 1, 2 * t + 1, 4 * t + 1
        self.b3 = self.var(0)
        self.us = {j: self.var(j - 1) for j in range(2, t)}
        self.g1 = self.e * self.inv(self.q) % self.p
        self.g2 = (
            self.e * self.inv(self.q) * self.y
            + self.e * t * self.inv(2 * self.q * self.q)
        ) % self.p
        self.g = (
            self.e * t * self.inv(self.q * self.q) * self.y
            - self.e * t * (t + 1) * self.inv(6 * self.q**3)
        ) % self.p
        self.C = self.hzero(t - 1)
        self.C[t - 1] = dict(self.one)
        self.U = self.hzero(self.q)
        self.U[self.q] = dict(self.one)
        for j, variable in self.us.items():
            self.U[self.q - j] = variable
        self.b2 = self.zero

    def inv(self, value):
        return pow(value % self.p, -1, self.p)

    def var(self, index):
        exponent = [0] * self.m
        exponent[index] = 1
        return {tuple(exponent): 1}

    def padd(self, left, right):
        answer = dict(left)
        for exponent, coefficient in right.items():
            value = (answer.get(exponent, 0) + coefficient) % self.p
            if value:
                answer[exponent] = value
            elif exponent in answer:
                del answer[exponent]
        return answer

    def pscale(self, polynomial, scalar):
        scalar %= self.p
        if not scalar:
            return {}
        return {
            exponent: coefficient * scalar % self.p
            for exponent, coefficient in polynomial.items()
            if coefficient * scalar % self.p
        }

    def pneg(self, polynomial):
        return self.pscale(polynomial, -1)

    def psub(self, left, right):
        return self.padd(left, self.pneg(right))

    def pmul(self, left, right):
        if not left or not right:
            return {}
        answer = {}
        for left_exponent, left_coefficient in left.items():
            for right_exponent, right_coefficient in right.items():
                exponent = tuple(
                    a + b for a, b in zip(left_exponent, right_exponent)
                )
                value = (
                    answer.get(exponent, 0)
                    + left_coefficient * right_coefficient
                ) % self.p
                if value:
                    answer[exponent] = value
                elif exponent in answer:
                    del answer[exponent]
        return answer

    def hzero(self, degree):
        return [{} for _ in range(degree + 1)]

    def hadd(self, left, right):
        size = max(len(left), len(right))
        answer = self.hzero(size - 1)
        for index in range(size):
            answer[index] = self.padd(
                left[index] if index < len(left) else self.zero,
                right[index] if index < len(right) else self.zero,
            )
        while len(answer) > 1 and not answer[-1]:
            answer.pop()
        return answer

    def hscale(self, polynomial, scalar):
        return [self.pscale(coefficient, scalar) for coefficient in polynomial]

    def hneg(self, polynomial):
        return self.hscale(polynomial, -1)

    def hsub(self, left, right):
        return self.hadd(left, self.hneg(right))

    def hmul(self, left, right):
        max_degree = 4 * self.t + 2
        answer = self.hzero(min(max_degree, len(left) + len(right) - 2))
        for left_degree, left_coefficient in enumerate(left):
            if not left_coefficient:
                continue
            for right_degree, right_coefficient in enumerate(right):
                degree = left_degree + right_degree
                if degree >= len(answer):
                    break
                if right_coefficient:
                    answer[degree] = self.padd(
                        answer[degree],
                        self.pmul(left_coefficient, right_coefficient),
                    )
        while len(answer) > 1 and not answer[-1]:
            answer.pop()
        return answer

    def hshift(self, polynomial, count=1):
        return [self.zero] * count + [dict(value) for value in polynomial]

    def hderivative(self, polynomial):
        return [
            self.pscale(polynomial[index], index)
            for index in range(1, len(polynomial))
        ] or [self.zero]

    def coefficient(self, polynomial, degree):
        return polynomial[degree] if 0 <= degree < len(polynomial) else self.zero

    def build_core(self, B0):
        t, y, g = self.t, self.y, self.g
        A = self.hshift(self.C)
        B = self.hzero(t)
        B[0] = B0
        for degree, coefficient in enumerate(self.C):
            B[degree + 1] = self.pscale(
                coefficient,
                g * (3 * degree + 5) * self.inv(2 * y * (degree + 1)),
            )

        rhs = self.hscale(self.hderivative(self.U), 3 * g)
        rhs = self.hadd(rhs, self.hmul(A, B))
        rhs = self.hsub(rhs, self.hshift(self.hmul(A, self.hderivative(B))))
        rhs = self.hadd(
            rhs,
            self.hscale(self.hshift(self.hmul(self.hderivative(A), B)), 2),
        )
        last = self.hadd(
            self.C, self.hscale(self.hderivative(A), 5 * self.inv(2))
        )
        rhs = self.hadd(
            rhs, self.hscale([self.pmul(self.b3, value) for value in last], g)
        )
        D = [
            self.pscale(value, self.inv(y * (2 * degree + 1)))
            for degree, value in enumerate(rhs)
        ]

        V = self.hshift(A)
        V[0] = self.padd(V[0], self.pscale(self.b3, -y))
        Y = self.hsub(
            self.hshift(D), [self.pmul(self.b3, value) for value in B]
        )
        Y[0] = self.padd(Y[0], self.pscale(self.b2, -g))
        Z = self.hshift(B)
        Z[0] = self.padd(Z[0], self.pscale(self.b3, -g))
        numerator = self.hadd(
            self.hsub(
                self.hmul(self.hderivative(V), Y),
                self.hmul(V, self.hderivative(Y)),
            ),
            self.hscale(self.hmul(self.hderivative(self.U), Z), 2),
        )
        Xprime = [
            self.pscale(
                self.coefficient(numerator, degree + 1), self.inv(2 * y)
            )
            for degree in range(max(1, len(numerator) - 1))
        ]
        return V, Y, Xprime

    def current_R(self):
        # The terminal expression is invariant under B -> B+constant:
        # delta Y=V/y, delta X'=U'/y, so delta(VX'-U'Y)=0.
        V, Y, Xprime = self.build_core(self.zero)
        answer = self.hsub(
            self.hmul(V, Xprime), self.hmul(self.hderivative(self.U), Y)
        )
        answer[0] = self.padd(answer[0], self.pscale(self.one, -self.y * self.g))
        return answer

    def c_pivot(self, index):
        t, e, q, y = self.t, self.e, self.q, self.y
        d = (2 * q * y - (t + 1)) % self.p
        A = (
            9 * index**2 * t + 18 * index**2 - 54 * index * t**2
            - 81 * index * t - 26 * index + 72 * t**3 + 144 * t**2
            + 88 * t + 16
        )
        B = (
            -9 * index**2 * t - 10 * index**2 + 24 * index * t**2
            + 33 * index * t + 10 * index - 12 * t**3 - 20 * t**2 - 8 * t
        )
        return (
            3 * t * e * (A * d + B)
            * self.inv((t + 1) * (3 * t + 2) ** 3 * (4 * t - 2 * index + 1))
        ) % self.p

    def q_pivot(self, index):
        t, e, q, y = self.t, self.e, self.q, self.y
        d = (2 * q * y - (t + 1)) % self.p
        A = 12 * t**2 + 16 * t + 4 - index * (3 * t + 4)
        B = 2 * (t + 1) * (index - t)
        return (
            -3 * t * e * (q - index) * (A * d + B)
            * self.inv(
                (t + 1) * q * (3 * t + 2) ** 2 * (4 * t - 2 * index + 1)
            )
        ) % self.p

    def solve(self):
        R = self.current_R()
        pivot_trace = []
        for index in range(1, self.t):
            band = self.N - index
            pivot = self.c_pivot(index)
            if not pivot:
                raise ZeroDivisionError(("C", index))
            rhs = self.pscale(self.coefficient(R, band), -self.inv(pivot))
            self.C[self.t - 1 - index] = rhs
            R = self.current_R()
            if self.coefficient(R, band):
                raise AssertionError(("C", index, "pivot row nonzero"))
            pivot_trace.append((band, f"C{index}", pivot))
        for index in range(self.t, 2 * self.t + 1):
            band = self.N - index
            pivot = self.q_pivot(index)
            if not pivot:
                raise ZeroDivisionError(("q", index))
            rhs = self.pscale(self.coefficient(R, band), -self.inv(pivot))
            self.U[self.q - index] = rhs
            R = self.current_R()
            if self.coefficient(R, band):
                raise AssertionError(("q", index, "pivot row nonzero"))
            pivot_trace.append((band, f"q{index}_0", pivot))
        band = 2 * self.t
        d = (2 * self.q * self.y - (self.t + 1)) % self.p
        pivot = self.g * d * self.inv(2 * self.y) % self.p
        if not pivot:
            raise ZeroDivisionError("b2")
        self.b2 = self.pscale(self.coefficient(R, band), -self.inv(pivot))
        R = self.current_R()
        if self.coefficient(R, band):
            raise AssertionError(("b2", "pivot row nonzero"))
        pivot_trace.append((band, "b2", pivot))
        if any(self.coefficient(R, degree) for degree in range(2 * self.t, self.N + 1)):
            raise AssertionError("nonzero high row")
        return [self.coefficient(R, degree) for degree in range(2 * self.t)], pivot_trace

    def compare_record(self, rows, path):
        record = json.loads(Path(path).read_text(encoding="utf-8"))
        variables = [sp.Symbol("b3")] + [
            sp.Symbol(f"q{index}_0") for index in range(2, self.t)
        ]
        b4 = sp.Symbol("b4")
        local = {str(variable): variable for variable in variables + [b4]}
        for item in record["terminal"]:
            expression = sp.sympify(item["expr"], locals=local).subs(b4, 0)
            polynomial = sp.Poly(sp.expand(expression), *variables, modulus=self.p)
            wanted = {
                monomial: int(coefficient) % self.p
                for monomial, coefficient in polynomial.terms()
                if int(coefficient) % self.p
            }
            if rows[int(item["band"])] != wanted:
                raise AssertionError(("record mismatch", item["band"]))


def render(polynomial, variable_names, prime):
    terms = []
    for exponent, coefficient in sorted(polynomial.items(), reverse=True):
        signed = coefficient if coefficient <= prime // 2 else coefficient - prime
        monomial = "*".join(
            name + (f"^{power}" if power != 1 else "")
            for name, power in zip(variable_names, exponent) if power
        ) or "1"
        terms.append(f"({signed})*{monomial}")
    return "+".join(terms) or "0"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("t", type=int)
    parser.add_argument("prime", type=int)
    parser.add_argument("y", type=int)
    parser.add_argument("--compare")
    parser.add_argument("--singular-positive", action="store_true")
    parser.add_argument("--singular-output")
    args = parser.parse_args()
    probe = SparseProbe(args.t, args.prime, args.y)
    rows, trace = probe.solve()
    if args.compare:
        probe.compare_record(rows, args.compare)
        print("COMPARE_PASS")
    print("ROW_TERM_COUNTS", [len(row) for row in rows])
    print("PIVOTS", trace)
    if args.singular_positive or args.singular_output:
        names = ["b3"] + [f"q{index}_0" for index in range(2, args.t)]
        positive = [render(row, names, args.prime) for row in rows[1:] if row]
        lines = [
            "// RESIDUAL-ZERO finite-field check; b4=0, bands 1..2t-1",
            f"// t={args.t} prime={args.prime} y={args.y % args.prime}",
            f"ring R={args.prime},({','.join(names)}),dp;",
            "option(redSB);",
            "ideal I=" + ",\n".join(positive) + ";",
            "ideal G=std(I);",
            'print("BASIS_SIZE"); size(G);',
            f'reduce(b3^{args.t},G);',
        ]
        previous = "G"
        prior_variable = None
        for step, variable in enumerate(reversed(names[1:]), 1):
            add = "b3" if step == 1 else prior_variable
            lines.extend([
                f"ideal J{step}={previous},{add};",
                f"ideal G{step}=std(J{step});",
                f'print("STEP_{variable}"); size(G{step});',
                f"reduce({variable}^{args.t + 1},G{step});",
            ])
            previous = f"G{step}"
            prior_variable = variable
        lines.append("quit;")
        singular_text = "\n".join(lines) + "\n"
        if args.singular_output:
            Path(args.singular_output).write_text(singular_text, encoding="utf-8")
            print("SINGULAR_OUTPUT", args.singular_output)
        else:
            print(singular_text, end="")


if __name__ == "__main__":
    main()
