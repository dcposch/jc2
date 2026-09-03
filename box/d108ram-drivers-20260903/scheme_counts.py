#!/usr/bin/env python3
"""Combinatorial sizes for the dense and Kummer-graded coefficient schemes."""
from __future__ import annotations

from math import comb


def bucket(total_degree, modulus=4, fixed_monic=True):
    out = [0] * modulus
    for gamma_degree in range(total_degree + 1):
        out[gamma_degree % modulus] += total_degree - gamma_degree + 1
    if fixed_monic:
        out[0] -= 1  # coefficient of pi^total_degree is fixed to one
    return out


def main():
    p = comb(20, 2) - 1
    q = comb(14, 2) - 1
    jac = comb(30, 2)
    print("dense P,Q,c,total:", p, q, 1, p+q+1)
    print("Jacobian coefficient upper bound:", jac)
    print("P character buckets mod 4:", bucket(18))
    print("Q character buckets mod 4:", bucket(12))
    print("Jacobian monomial buckets mod 4:", bucket(28, fixed_monic=False))
    print("h-normal counts h,beta,A,B,c,total:", 27, 63, 63, 99, 1,
          27+63+63+99+1)
    print("degree-two reparse z,u,v:", 5, 9, 13, "sum", 5+9+13)
    print("extra-normalized h,beta,R,c,total:", 27, 63, 99, 1, 27+63+99+1)


if __name__ == "__main__":
    main()
