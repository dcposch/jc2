#!/usr/bin/env python3
"""Exact controls for the R2 pole-degree pin and sharp boundary cases.

Standard library only. Polynomials are tuples of Fraction coefficients in
increasing eta-degree. These finite controls exercise the algebra used in
Lemma 2.1 and the independent nonconstant fixture; they do not replace the
source-typing argument.
"""

from collections import defaultdict
from fractions import Fraction as Q
from math import gcd


COUNTS = defaultdict(int)


def check(group, condition, detail=""):
    if not condition:
        raise AssertionError(f"{group}: {detail}")
    COUNTS[group] += 1


def trim(p):
    p = [Q(c) for c in p]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


ZERO = (Q(0),)
ONE = (Q(1),)
X = (Q(0), Q(1))


def is_zero(p):
    return trim(p) == ZERO


def degree(p):
    return -1 if is_zero(p) else len(trim(p)) - 1


def add(p, q):
    n = max(len(p), len(q))
    return trim([
        (p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0)
        for i in range(n)
    ])


def sub(p, q):
    n = max(len(p), len(q))
    return trim([
        (p[i] if i < len(p) else 0) - (q[i] if i < len(q) else 0)
        for i in range(n)
    ])


def scale(a, p):
    return trim([Q(a) * c for c in p])


def mul(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def power(p, n):
    out = ONE
    base = trim(p)
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n //= 2
    return out


def deriv(p):
    return trim([i * p[i] for i in range(1, len(p))] or [0])


def linear(root):
    return (-Q(root), Q(1))


def divmod_poly(a, b):
    a, b = list(trim(a)), trim(b)
    if is_zero(b):
        raise ZeroDivisionError
    if len(a) < len(b):
        return ZERO, tuple(a)
    out = [Q(0)] * (len(a) - len(b) + 1)
    while not is_zero(a) and len(a) >= len(b):
        shift = len(a) - len(b)
        coeff = a[-1] / b[-1]
        out[shift] += coeff
        for i, bi in enumerate(b):
            a[i + shift] -= coeff * bi
        a = list(trim(a))
    return trim(out), trim(a)


def gcd_poly(a, b):
    a, b = trim(a), trim(b)
    while not is_zero(b):
        _, remainder = divmod_poly(a, b)
        a, b = b, remainder
    return ZERO if is_zero(a) else scale(1 / a[-1], a)


def squarefree(p):
    return degree(gcd_poly(p, deriv(p))) == 0


def multiplicity(p, root):
    factor = linear(root)
    p = trim(p)
    answer = 0
    while not is_zero(p):
        quotient, remainder = divmod_poly(p, factor)
        if not is_zero(remainder):
            break
        answer += 1
        p = quotient
    return answer


def bracket(alpha, beta, p, q):
    return sub(scale(alpha, mul(p, deriv(q))),
               scale(beta, mul(deriv(p), q)))


def constant_nonzero(p):
    p = trim(p)
    return degree(p) == 0 and p[0] != 0


def residues(p, nu):
    return {j % nu for j, coeff in enumerate(trim(p)) if coeff}


def check_primitives():
    check("primitive", constant_nonzero((3,)), "nonzero constant")
    check("primitive", not constant_nonzero((0, 1)), "nonconstant")
    check("primitive", squarefree((-1, 0, 1)), "eta^2-1")
    check("primitive", not squarefree((0, 0, 1)), "eta^2")
    check("primitive", degree(gcd_poly((-1, 0, 1), (-1, 1))) == 1,
          "nontrivial gcd")


def check_degree_transport():
    """Model q_G^alpha=p_G^beta and transport root multiplicities."""
    types = ((2, 3), (2, 5), (3, 4), (3, 5),
             (4, 5), (4, 7), (5, 6), (5, 7))
    root_pairs = ((0, 1), (1, -2), (Q(-3, 2), Q(2, 3)))
    for alpha, beta in types:
        check("degree-type", gcd(alpha, beta) == 1 and 2 <= alpha < beta)
        for t in range(1, 5):
            for c, d in root_pairs:
                # r has multiplicity t at c and a harmless second root.
                r = mul(power(linear(c), t), linear(d))
                p_g = power(r, alpha)
                q_g = power(r, beta)
                check("degree-equality",
                      power(q_g, alpha) == power(p_g, beta),
                      f"type={(alpha, beta)}, t={t}, c={c}")
                mp = multiplicity(p_g, c)
                mq = multiplicity(q_g, c)
                check("degree-multiplicity", mp == alpha * t)
                check("degree-multiplicity", mq == beta * t)
                check("degree-pin", alpha * mq == beta * mp)
                check("degree-pin", mp >= alpha >= 2)
                check("degree-mutation", alpha * (mq + 1) != beta * mp)
                check("degree-mutation",
                      power(add(q_g, ONE), alpha) != power(p_g, beta))


def check_linear_constant_branch():
    """The branch omitted by the printed proof of Proposition 5.3(iv)."""
    types = ((2, 3), (2, 5), (3, 4), (3, 5), (4, 7), (5, 6))
    parameters = ((0, 1, 1), (2, -3, 5),
                  (Q(-1, 2), Q(7, 3), Q(-4, 5)))
    for alpha, beta in types:
        for a, aa, bb in parameters:
            p = scale(aa, linear(a))
            q = (Q(bb),)
            got = bracket(alpha, beta, p, q)
            check("linear-constant", got == (-Q(beta) * Q(aa) * Q(bb),))
            check("linear-constant", constant_nonzero(got))
            check("linear-constant", degree(p) == 1 and degree(q) == 0)
            check("linear-constant", squarefree(p))


def check_alpha_one_family():
    """Verify the displayed full linear family and its character mixers."""
    parameters = (
        (0, 1, 1, 0),
        (0, -2, 3, Q(5, 7)),
        (Q(3, 2), Q(4, 3), Q(-5, 2), Q(-7, 4)),
    )
    for beta in range(2, 8):
        for a, aa, c, lam in parameters:
            p = scale(aa, linear(a))
            q = add((-Q(c) / (Q(beta) * Q(aa)),),
                    scale(lam, power(p, beta)))
            got = bracket(1, beta, p, q)
            check("alpha1-family", got == (Q(c),))
            check("alpha1-family", constant_nonzero(got))

        # For a=0 and lambda!=0, q has characters 0 and beta. It mixes
        # whenever nu does not divide beta.
        p = X
        q = add((-Q(1, beta),), power(p, beta))
        for nu in range(2, 8):
            expected = {0, beta % nu}
            check("alpha1-character", residues(q, nu) == expected)
            if beta % nu:
                check("alpha1-mixer", len(residues(q, nu)) == 2)
                check("alpha1-mixer", bracket(1, beta, p, q) == ONE)


def check_two_orbit_fixture():
    """Independent nonconstant control with two nonzero nu=2 deck orbits."""
    for aa in (Q(1), Q(2), Q(-3), Q(1, 2), Q(7, 5), Q(8)):
        p = (aa * aa / 8, 0, aa, 0, 1)
        q = (0, 5 * aa * aa / 16, 0, 5 * aa / 4, 0, 1)
        got = bracket(4, 5, p, q)
        check("two-orbit", got == (5 * aa**4 / 32,))
        check("two-orbit", constant_nonzero(got))
        check("two-orbit", degree(p) == 4 and degree(q) == 5)
        check("two-orbit", 5 * degree(p) == 4 * degree(q))
        check("two-orbit", residues(p, 2) == {0})
        check("two-orbit", residues(q, 2) == {1})
        check("two-orbit", squarefree(p) and squarefree(q))
        check("two-orbit", degree(gcd_poly(p, q)) == 0)

        mutated = add(q, ONE)
        check("two-orbit-mutation", residues(mutated, 2) == {0, 1})
        check("two-orbit-mutation",
              not constant_nonzero(bracket(4, 5, p, mutated)))


def main():
    check_primitives()
    check_degree_transport()
    check_linear_constant_branch()
    check_alpha_one_family()
    check_two_orbit_fixture()
    total = sum(COUNTS.values())
    groups = ", ".join(f"{name}={COUNTS[name]}" for name in sorted(COUNTS))
    print(f"PASS: {total} exact assertions ({groups})")


if __name__ == "__main__":
    main()
