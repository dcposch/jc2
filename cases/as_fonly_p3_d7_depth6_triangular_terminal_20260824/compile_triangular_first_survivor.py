#!/usr/bin/env python3
"""Exact digit-linear compiler for the first triangular p=3,n=6,D=7 survivor.

No SMT/SAT system is used.  The inverse coefficient is eliminated exactly:

  P'(x)=1+3a(x),
  Q_y=T=(1+3a)^(-1) mod 3^6,
  T=1-3a+9a^2-27a^3+81a^4-243a^5.

The cap D=7 is equivalent to all degree >6 coefficients of
  H(a)=a^2-3a^3+9a^4-27a^5
vanishing modulo 3^4.  Source provenance is exactly
  [x^2]a=-1 mod 3, [x^5]a=0 mod 3.

At every new digit a -> a+3^r delta the next obstruction is affine with
linearization 2*a0*delta over F3.  We enumerate only the nullspace of this
fixed map, with deterministic RREF and exact integer carries.
"""
from __future__ import annotations

from itertools import product
import hashlib

P = 3
MAX_DEG = 30
HIGH_START = 7


def add(left, right):
    size = max(len(left), len(right))
    return [(left[i] if i < len(left) else 0) +
            (right[i] if i < len(right) else 0) for i in range(size)]


def scale(c, polynomial):
    return [c * value for value in polynomial]


def mul(left, right):
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def pad(polynomial, size=MAX_DEG + 1):
    return polynomial + [0] * (size - len(polynomial))


def H(a):
    a2 = mul(a, a)
    a3 = mul(a2, a)
    a4 = mul(a3, a)
    a5 = mul(a4, a)
    return pad(add(add(a2, scale(-3, a3)), add(scale(9, a4), scale(-27, a5))))


def linear_map(a0):
    """Rows degree 7..30 of delta -> 2*a0*delta over F3."""
    rows = []
    for degree in range(HIGH_START, MAX_DEG + 1):
        row = []
        for j in range(7):
            i = degree - j
            row.append((2 * a0[i] if 0 <= i < len(a0) else 0) % 3)
        rows.append(row)
    return rows


def affine_solutions(matrix, rhs):
    """Return particular and a deterministic nullspace basis over F3."""
    nvars = 7
    work = [[value % 3 for value in row] + [b % 3]
            for row, b in zip(matrix, rhs)]
    pivots = []
    r = 0
    for c in range(nvars):
        choice = next((i for i in range(r, len(work)) if work[i][c]), None)
        if choice is None:
            continue
        work[r], work[choice] = work[choice], work[r]
        inv = pow(work[r][c], -1, 3)
        work[r] = [(inv * value) % 3 for value in work[r]]
        for i in range(len(work)):
            if i != r and work[i][c]:
                factor = work[i][c]
                work[i] = [(x - factor * y) % 3
                           for x, y in zip(work[i], work[r])]
        pivots.append(c)
        r += 1
        if r == len(work):
            break
    if any(not any(row[:nvars]) and row[-1] for row in work):
        return None, [], len(pivots)
    free = [c for c in range(nvars) if c not in pivots]
    particular = [0] * nvars
    for i, c in enumerate(pivots):
        particular[c] = work[i][-1]
    basis = []
    for f in free:
        vector = [0] * nvars
        vector[f] = 1
        for i, c in enumerate(pivots):
            vector[c] = (-work[i][f]) % 3
        basis.append(vector)
    return particular, basis, len(pivots)


def vector_add(*vectors):
    return [sum(values) % 3 for values in zip(*vectors)]


def extend(a, digit, r):
    return [value + (3 ** r) * d for value, d in zip(a, digit)]


def obstruction_rhs(a, r):
    h = H(a)
    modulus = 3 ** r
    assert all(value % modulus == 0 for value in h[HIGH_START:])
    return [(-(value // modulus)) % 3 for value in h[HIGH_START:]]


def valid(a, modulus):
    return all(value % modulus == 0 for value in H(a)[HIGH_START:])


base_points = []
for c0, c1, c3 in product(range(3), repeat=3):
    a0 = [c0, c1, 2, c3, 0, 0, 0]
    assert valid(a0, 3)
    base_points.append(a0)

counts = {"base": len(base_points)}
digest = hashlib.sha256()
current = base_points
witness = None
for r in (1, 2, 3):
    next_points = []
    rank_hist = {}
    inconsistent = 0
    for a in current:
        a0 = [value % 3 for value in a]
        matrix = linear_map(a0)
        rhs = obstruction_rhs(a, r)
        particular, basis, rank = affine_solutions(matrix, rhs)
        rank_hist[rank] = rank_hist.get(rank, 0) + 1
        if particular is None:
            inconsistent += 1
            digest.update(f"X:{r}:{a}\n".encode())
            continue
        # At the terminal digit, existence of the affine particular solution
        # is already the complete discriminator.  Kernel choices do not need
        # enumeration; retain the lexicographically canonical particular.
        if r == 3:
            candidate = extend(a, particular, r)
            assert valid(candidate, 3 ** (r + 1))
            witness = candidate
            next_points.append(candidate)
            digest.update(f"S:{r}:{candidate}\n".encode())
            break
        for parameters in product(range(3), repeat=len(basis)):
            summands = [particular]
            summands.extend([[coefficient * value % 3 for value in vector]
                             for coefficient, vector in zip(parameters, basis)])
            digit = vector_add(*summands)
            candidate = extend(a, digit, r)
            assert valid(candidate, 3 ** (r + 1))
            next_points.append(candidate)
            digest.update(f"S:{r}:{candidate}\n".encode())
    counts[f"digit_{r}_input"] = len(current)
    counts[f"digit_{r}_output"] = len(next_points)
    counts[f"digit_{r}_inconsistent"] = inconsistent
    counts[f"digit_{r}_rank_hist"] = rank_hist
    current = next_points
    print("stage", r, counts, flush=True)
    if witness is not None:
        break

print("terminal_status", "sat" if witness is not None else "unsat")
print("enumeration_sha256", digest.hexdigest())
if witness is not None:
    print("first_a_mod81", witness)
    # Digits modulo 81 suffice for H mod81.  Set the unused 81 digit to zero.
    a = witness
    inv = [1]
    power_a = [1]
    for k in range(1, 6):
        power_a = mul(power_a, a)
        inv = add(inv, scale((-3) ** k, power_a))
    inv = [value % 729 for value in pad(inv)]
    assert not any(inv[7:])
    print("T_mod729", inv[:7])
    print("PASS-TRIANGULAR-SURVIVOR")
else:
    print("PASS-TRIANGULAR-UNSAT")
