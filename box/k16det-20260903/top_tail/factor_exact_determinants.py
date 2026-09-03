#!/usr/bin/env python3
"""Factor exact determinant coordinates and their quadratic norms."""

from __future__ import annotations

import pathlib
import hashlib
import sympy as sp


HERE = pathlib.Path(__file__).resolve().parent


def determinant_line(path: pathlib.Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    return lines[lines.index("PROBE_DELTA") + 1]


def reduce_rational(value: sp.Rational, prime: int) -> int:
    return (int(value.p) % prime) * pow(int(value.q), -1, prime) % prime


def show(t: int, filename: str, minpoly_constant: int) -> None:
    a = sp.Symbol("a")
    path = HERE / filename
    value = sp.cancel(sp.sympify(determinant_line(path).replace("^", "**")))
    poly = sp.Poly(value, a)
    coeff_a = sp.Rational(poly.coeff_monomial(a))
    coeff_1 = sp.Rational(poly.coeff_monomial(1))
    norm = sp.cancel(coeff_1 * coeff_1 - minpoly_constant * coeff_a * coeff_a)
    prime = 1009
    a_roots = [root for root in range(prime) if (root * root - minpoly_constant) % prime == 0]
    values = [(reduce_rational(coeff_a, prime) * root + reduce_rational(coeff_1, prime)) % prime
              for root in a_roots]
    print(f"t={t}")
    print(f"  output_sha256={hashlib.sha256(path.read_bytes()).hexdigest()}")
    print(f"  coordinate_digits=A({len(str(abs(int(coeff_a.p))))},{len(str(coeff_a.q))}) "
          f"B({len(str(abs(int(coeff_1.p))))},{len(str(coeff_1.q))})")
    print(f"  norm_nonzero={norm != 0} norm_sign={sp.sign(norm)}")
    print(f"  mod_{prime}_a_roots={a_roots} determinant_values={values} norm={values[0]*values[1]%prime}")


def main() -> None:
    show(3, "probe_t3_exact_bNone.out", 12)


if __name__ == "__main__":
    main()
