#!/usr/bin/env python3
"""Exact first-two homogeneous Jacobian bands for binary cubic strata.

Pure stdlib.  All algebra is over Q via fractions.Fraction.  The script emits
complete matrices, nullspaces, projected quadratic obstructions, and a
Singular input; it does not invoke Singular itself.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


REPRESENTATIVES = {
    # coefficient index i means x^i*y^(3-i)
    "triple": [1, 0, 0, 0],
    "double": [0, 1, 0, 0],
    "squarefree": [0, -1, 1, 0],
}


def conv(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def power(a: list[Fraction], n: int) -> list[Fraction]:
    out = [Fraction(1)]
    for _ in range(n):
        out = conv(out, a)
    return out


def bracket(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    """Homogeneous bracket, coefficient index is the x exponent."""
    da = len(a) - 1
    db = len(b) - 1
    out = [Fraction(0) for _ in range(da + db - 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            exponent = i + j - 1
            coeff = i * db - da * j
            if exponent >= 0 and coeff:
                out[exponent] += coeff * ai * bj
    return out


def direct_bracket(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    """Independent derivative/dictionary implementation."""
    da = len(a) - 1
    db = len(b) - 1

    def dx(v, d):
        return {(i - 1, d - i): c * i for i, c in enumerate(v) if i and c}

    def dy(v, d):
        return {(i, d - i - 1): c * (d - i)
                for i, c in enumerate(v) if d - i and c}

    def mul(p, q):
        out = {}
        for (i, j), c in p.items():
            for (k, ell), d in q.items():
                key = (i + k, j + ell)
                out[key] = out.get(key, Fraction(0)) + c * d
        return out

    p = mul(dx(a, da), dy(b, db))
    q = mul(dy(a, da), dx(b, db))
    total = da + db - 2
    return [p.get((i, total - i), Fraction(0))
            - q.get((i, total - i), Fraction(0))
            for i in range(total + 1)]


def transpose(a):
    return [list(row) for row in zip(*a)] if a else []


def rref(a):
    m = [list(map(Fraction, row)) for row in a]
    rows = len(m)
    cols = len(m[0]) if rows else 0
    pivots = []
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        unit = m[r][c]
        m[r] = [x / unit for x in m[r]]
        for i in range(rows):
            if i != r and m[i][c]:
                scale = m[i][c]
                m[i] = [x - scale * y for x, y in zip(m[i], m[r])]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    return m, pivots


def nullspace(a):
    rr, pivots = rref(a)
    cols = len(a[0]) if a else 0
    free = [j for j in range(cols) if j not in pivots]
    out = []
    for f in free:
        v = [Fraction(0) for _ in range(cols)]
        v[f] = Fraction(1)
        for row, p in enumerate(pivots):
            v[p] = -rr[row][f]
        out.append(v)
    return out


def rank(a):
    return len(rref(a)[1])


def matrix_from_columns(cols, rows):
    return [[cols[j][i] for j in range(len(cols))] for i in range(rows)]


def basis_poly(degree, index):
    out = [Fraction(0) for _ in range(degree + 1)]
    out[index] = Fraction(1)
    return out


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), Fraction(0))


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def matrix_sha(a) -> str:
    payload = json.dumps([[fstr(x) for x in row] for row in a],
                         separators=(",", ":"), sort_keys=False).encode()
    return hashlib.sha256(payload).hexdigest()


def primitive_polynomial(poly):
    if not poly:
        return []
    den = 1
    for value in poly.values():
        den = math.lcm(den, value.denominator)
    ints = {key: int(value * den) for key, value in poly.items() if value}
    g = 0
    for value in ints.values():
        g = math.gcd(g, abs(value))
    if g:
        ints = {key: value // g for key, value in ints.items()}
    first_key = min(ints)
    if ints[first_key] < 0:
        ints = {key: -value for key, value in ints.items()}
    return [[i, j, ints[(i, j)]] for i, j in sorted(ints)]


def render_term(i, j, coeff):
    mon = []
    if i == j:
        mon.append(f"s{i + 1}^2")
    else:
        mon.extend([f"s{i + 1}", f"s{j + 1}"])
    monomial = "*".join(mon) if mon else "1"
    if coeff == 1:
        return monomial
    if coeff == -1:
        return "-" + monomial
    return f"{coeff}*{monomial}"


def render_poly(terms):
    if not terms:
        return "0"
    raw = "+".join(render_term(i, j, c) for i, j, c in terms)
    return raw.replace("+-", "-")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stratum", choices=sorted(REPRESENTATIVES), required=True)
    ap.add_argument("--outdir", required=True)
    args = ap.parse_args()
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    K = list(map(Fraction, REPRESENTATIVES[args.stratum]))
    P9 = power(K, 3)
    Q12 = power(K, 4)
    top = bracket(P9, Q12)
    assert top == direct_bracket(P9, Q12)
    assert all(x == 0 for x in top)

    # Degree 18: P8 (9 coefficients), Q11 (12 coefficients).
    band1_cols = []
    for i in range(9):
        col = bracket(basis_poly(8, i), Q12)
        assert col == direct_bracket(basis_poly(8, i), Q12)
        band1_cols.append(col)
    for j in range(12):
        col = bracket(P9, basis_poly(11, j))
        assert col == direct_bracket(P9, basis_poly(11, j))
        band1_cols.append(col)
    A = matrix_from_columns(band1_cols, 19)
    ker = nullspace(A)
    for v in ker:
        assert all(sum(A[i][j] * v[j] for j in range(21)) == 0
                   for i in range(19))

    # Degree 17 fresh operator: P7 (8), Q10 (11).
    band2_cols = []
    for i in range(8):
        col = bracket(basis_poly(7, i), Q12)
        assert col == direct_bracket(basis_poly(7, i), Q12)
        band2_cols.append(col)
    for j in range(11):
        col = bracket(P9, basis_poly(10, j))
        assert col == direct_bracket(P9, basis_poly(10, j))
        band2_cols.append(col)
    B = matrix_from_columns(band2_cols, 18)
    left = nullspace(transpose(B))
    for ell in left:
        assert all(sum(ell[i] * B[i][j] for i in range(18)) == 0
                   for j in range(19))

    # Quadratic source projected to the complete fresh cokernel.
    pdirs = [v[:9] for v in ker]
    qdirs = [v[9:] for v in ker]
    equations = []
    for ell in left:
        poly = {}
        for i in range(len(ker)):
            for j in range(i, len(ker)):
                source = bracket(pdirs[i], qdirs[j])
                assert source == direct_bracket(pdirs[i], qdirs[j])
                if i != j:
                    other = bracket(pdirs[j], qdirs[i])
                    assert other == direct_bracket(pdirs[j], qdirs[i])
                    source = [a + b for a, b in zip(source, other)]
                value = dot(ell, source)
                if value:
                    poly[(i, j)] = value
        if poly:
            equations.append(poly)

    monomials = sorted({key for eq in equations for key in eq})
    eq_matrix = [[eq.get(key, Fraction(0)) for key in monomials]
                 for eq in equations]
    primitive = [primitive_polynomial(eq) for eq in equations]

    # Registered negative: perturb Q12 by x^12.
    perturb = list(Q12)
    perturb[12] += 1
    neg = bracket(P9, perturb)
    assert neg == direct_bracket(P9, perturb)
    assert any(neg)

    result = {
        "schema": "binary-cubic-bands-v1",
        "stratum": args.stratum,
        "K": [fstr(x) for x in K],
        "P9": [fstr(x) for x in P9],
        "Q12": [fstr(x) for x in Q12],
        "top_row_count": len(top),
        "top_zero": True,
        "band1": {
            "rows": 19, "columns": 21, "rank": rank(A),
            "kernel_dimension": len(ker), "matrix_sha256": matrix_sha(A),
            "matrix": [[fstr(x) for x in row] for row in A],
            "kernel": [[fstr(x) for x in row] for row in ker],
        },
        "band2_fresh": {
            "rows": 18, "columns": 19, "rank": rank(B),
            "kernel_dimension": 19 - rank(B),
            "cokernel_dimension": len(left), "matrix_sha256": matrix_sha(B),
            "matrix": [[fstr(x) for x in row] for row in B],
            "left_cokernel": [[fstr(x) for x in row] for row in left],
        },
        "quadratic_obstruction": {
            "parameter_count": len(ker),
            "nonzero_cokernel_equations": len(equations),
            "equation_span_rank": rank(eq_matrix) if eq_matrix else 0,
            "monomial_count": len(monomials),
            "equations_primitive": primitive,
        },
        "controls": {
            "direct_bracket_agreement": True,
            "zero_lower_faces_pass_both_bands": True,
            "perturbed_Q12_top_nonzero": True,
            "perturbed_top": [fstr(x) for x in neg],
        },
        "scope": "first two char0 denominator-free homogeneous bands only",
    }
    result_path = outdir / "result.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    names = ",".join(f"s{i + 1}" for i in range(len(ker)))
    sing = [
        "// Auto-generated exact obstruction ideal.",
        "option(redSB);",
        f"ring R=0,({names}),dp;",
    ]
    rendered = [render_poly(eq) for eq in primitive]
    if rendered:
        sing.append("ideal I=" + ",\n  ".join(rendered) + ";")
    else:
        sing.append("ideal I=0;")
    sing.extend([
        "ideal G=std(I);",
        f'print("STRATUM {args.stratum}");',
        'print("INPUT_GENERATORS "+string(size(I)));',
        'print("GB_GENERATORS "+string(size(G)));',
        'print("DIMENSION "+string(dim(G)));',
        'print("GROEBNER_BEGIN");',
        "print(G);",
        'print("GROEBNER_END");',
        'print("PASS");',
        "quit;",
    ])
    (outdir / "obstruction.sing").write_text("\n".join(sing) + "\n")
    print(json.dumps({
        "PASS": True,
        "stratum": args.stratum,
        "band1_rank_kernel": [result["band1"]["rank"], len(ker)],
        "band2_rank_kernel_cokernel": [result["band2_fresh"]["rank"],
                                           result["band2_fresh"]["kernel_dimension"],
                                           len(left)],
        "obstruction_equations_rank": [len(equations),
                                         result["quadratic_obstruction"]["equation_span_rank"]],
        "result_sha256": hashlib.sha256(result_path.read_bytes()).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()

