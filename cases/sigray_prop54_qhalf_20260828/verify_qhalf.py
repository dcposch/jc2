#!/usr/bin/env python3
"""Exact controls for the repaired q-half of Sigray Proposition 5.4.

Standard library only.  Coefficients are Fractions and polynomial tuples are
in increasing eta-degree.  The proof in the producer is general; this script
checks nonvacuous fixtures, character transport, kernel dimensions, mutations,
and the sharp alpha=1 control on a bounded exact grid.
"""

from fractions import Fraction as Q
from math import gcd


def trim(p):
    p = list(map(Q, p))
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
    return trim([Q(a) * x for x in p])


def mul(p, q):
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return trim(out)


def power(p, n):
    out = ONE
    for _ in range(n):
        out = mul(out, p)
    return out


def deriv(p):
    return trim([Q(i) * p[i] for i in range(1, len(p))] or [0])


def monomial(j, c=1):
    return trim([0] * j + [Q(c)])


def divmod_poly(a, b):
    a, b = list(trim(a)), trim(b)
    assert not is_zero(b)
    if len(a) < len(b):
        return ZERO, tuple(a)
    out = [Q(0)] * (len(a) - len(b) + 1)
    while not is_zero(a) and len(a) >= len(b):
        j = len(a) - len(b)
        c = a[-1] / b[-1]
        out[j] += c
        for i, bi in enumerate(b):
            a[i + j] -= c * bi
        a = list(trim(a))
    return trim(out), trim(a)


def gcd_poly(a, b):
    a, b = trim(a), trim(b)
    while not is_zero(b):
        _, r = divmod_poly(a, b)
        a, b = b, r
    if is_zero(a):
        return ZERO
    return scale(1 / a[-1], a)


def squarefree(p):
    return degree(gcd_poly(p, deriv(p))) == 0


def bracket(alpha, beta, p, q):
    """alpha*p*q' - beta*p'*q."""
    return sub(scale(alpha, mul(p, deriv(q))),
               scale(beta, mul(deriv(p), q)))


def constant_nonzero(p):
    p = trim(p)
    return degree(p) == 0 and p[0] != 0


def residues(p, nu):
    return {i % nu for i, c in enumerate(trim(p)) if c}


def character(p, nu):
    rs = residues(p, nu)
    if not rs:
        return None
    return next(iter(rs)) if len(rs) == 1 else None


def rref_rank(rows):
    if not rows:
        return 0
    a = [list(map(Q, row)) for row in rows]
    m, n = len(a), len(a[0])
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, m) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        v = a[rank][col]
        a[rank] = [x / v for x in a[rank]]
        for i in range(m):
            if i != rank and a[i][col]:
                v = a[i][col]
                a[i] = [a[i][j] - v * a[rank][j] for j in range(n)]
        rank += 1
        if rank == m:
            break
    return rank


def operator_matrix(alpha, beta, p, cap):
    cols = [bracket(alpha, beta, p, monomial(j))
            for j in range(cap + 1)]
    nrows = max(len(c) for c in cols)
    return [
        [col[i] if i < len(col) else Q(0) for col in cols]
        for i in range(nrows)
    ]


def rhs_consistent(rows, rhs):
    assert len(rows) == len(rhs)
    return rref_rank(rows) == rref_rank([
        list(row) + [Q(b)] for row, b in zip(rows, rhs)
    ])


def deck_factor(nu, a):
    """eta^nu-a."""
    return add(monomial(nu), (-Q(a),))


def pattern_p(nu, epsilon, factors):
    p = X if epsilon else ONE
    for a in factors:
        p = mul(p, deck_factor(nu, a))
    return p


def check_positive_fixtures():
    # (nu, epsilon, alpha, beta, p, q); each bracket is exactly +1.
    fixtures = [
        (2, 0, 2, 3,
         (-1, 0, 1),
         (0, Q(-1, 2), 0, Q(1, 3))),
        (2, 1, 3, 4,
         (0, -1, 0, 1),
         (Q(1, 4), 0, Q(-3, 2), 0, Q(9, 8))),
        (3, 0, 3, 4,
         (-1, 0, 0, 1),
         (0, Q(-1, 3), 0, 0, Q(1, 4))),
        (3, 1, 2, 3,
         (0, -1, 0, 0, 1),
         (Q(1, 3), 0, 0, Q(-4, 3), 0, 0, Q(8, 9))),
    ]
    checks = mutations = 0
    for nu, epsilon, alpha, beta, p, q in fixtures:
        p, q = trim(p), trim(q)
        target = (1 - epsilon) % nu
        assert character(p, nu) == epsilon
        assert character(q, nu) == target
        assert bracket(alpha, beta, p, q) == ONE
        assert squarefree(p) and squarefree(q)
        assert degree(gcd_poly(p, q)) == 0
        assert beta * degree(p) == alpha * degree(q)
        checks += 7

        wrong = (target + 1) % nu
        qm = add(q, monomial(wrong))
        got = bracket(alpha, beta, p, qm)
        assert not constant_nonzero(got)
        assert residues(qm, nu) != {target}
        mutations += 2
    return checks, mutations


def check_character_transport_and_kernel():
    types = ((2, 3), (2, 5), (3, 4), (3, 5), (4, 5), (4, 7), (5, 6))
    grid = transport = 0
    for nu in range(2, 6):
        for epsilon in (0, 1):
            for factors in ((1,), (1, 2)):
                p = pattern_p(nu, epsilon, factors)
                assert degree(p) >= 2
                assert character(p, nu) == epsilon
                assert squarefree(p)
                n = degree(p)
                for alpha, beta in types:
                    assert 2 <= alpha < beta and gcd(alpha, beta) == 1
                    cap = (beta * n) // alpha + 3
                    rows = operator_matrix(alpha, beta, p, cap)
                    # Lemma 4.1: the map is injective on every tested window.
                    assert rref_rank(rows) == cap + 1
                    grid += 1

                    # A pure r input maps to epsilon+r-1, unless it maps to 0.
                    for r in range(nu):
                        for j in range(r, cap + 1, nu):
                            got = bracket(alpha, beta, p, monomial(j))
                            if not is_zero(got):
                                assert residues(got, nu) == {
                                    (epsilon + r - 1) % nu
                                }
                            transport += 1
    return grid, transport


def check_alpha_one_vertex_controls():
    kernel = inconsistent = 0
    for nu in range(2, 6):
        for epsilon in (0, 1):
            for factors in ((1,), (1, 2)):
                p = pattern_p(nu, epsilon, factors)
                n = degree(p)
                assert n >= 2 and squarefree(p)
                for beta in range(2, 6):
                    cap = beta * n + 1
                    rows = operator_matrix(1, beta, p, cap)
                    # One-dimensional kernel, visibly spanned by p^beta.
                    assert is_zero(bracket(1, beta, p, power(p, beta)))
                    assert rref_rank(rows) == cap
                    kernel += 2

                    rhs = [Q(1)] + [Q(0)] * (len(rows) - 1)
                    assert not rhs_consistent(rows, rhs)
                    inconsistent += 1
    return kernel, inconsistent


def check_alpha_one_mixing_control():
    # All local algebraic conditions except the pole-vertex (>1 p-root) gate.
    nu, alpha, beta = 3, 1, 2
    p = X
    q = add(ONE, monomial(2))
    assert bracket(alpha, beta, p, q) == (Q(-2),)
    assert squarefree(p) and squarefree(q)
    assert degree(gcd_poly(p, q)) == 0
    assert beta * degree(p) == alpha * degree(q)
    assert character(p, nu) == 1
    assert residues(q, nu) == {0, 2}
    assert degree(p) == 1  # the one and only charged source failure.
    return 7


def main():
    fixtures, mutations = check_positive_fixtures()
    kernels, transports = check_character_transport_and_kernel()
    alpha1_kernel, alpha1_inconsistent = check_alpha_one_vertex_controls()
    alpha1_mixing = check_alpha_one_mixing_control()
    total = (fixtures + mutations + kernels + transports + alpha1_kernel +
             alpha1_inconsistent + alpha1_mixing)
    print("Sigray Proposition 5.4 q-half checker: PASS")
    print(f"positive fixture assertions:             {fixtures}")
    print(f"wrong-character mutation assertions:     {mutations}")
    print(f"alpha>=2 zero-kernel matrix checks:       {kernels}")
    print(f"deck-character transport checks:         {transports}")
    print(f"alpha=1 kernel assertions:               {alpha1_kernel}")
    print(f"alpha=1 degree>=2 inconsistency checks:   {alpha1_inconsistent}")
    print(f"sharp alpha=1 mixing-control assertions:  {alpha1_mixing}")
    print(f"total grouped exact assertions:          {total}")


if __name__ == "__main__":
    main()
