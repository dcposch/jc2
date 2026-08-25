#!/usr/bin/env python3
"""Exact degree-16 Kuranishi lift for the three binary-cubic strata.

This compiler is pure stdlib and is intended for AWS execution only.  It
imports the pinned first-two-band compiler for constant rational linear
algebra and independently implements polynomial-valued brackets and the
degree-17 incidence parameterization.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path


PARENT_PATH = (
    Path(__file__).resolve().parents[1]
    / "max12_912_order1_binary_cubic_bands_aws_20260825"
    / "compile_bands.py"
)
spec = importlib.util.spec_from_file_location("binary_cubic_parent", PARENT_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load pinned parent compiler")
parent = importlib.util.module_from_spec(spec)
spec.loader.exec_module(parent)

Poly = dict[tuple[int, ...], Fraction]


def clean(p: Poly) -> Poly:
    return {m: Fraction(c) for m, c in p.items() if c}


def padd(a: Poly, b: Poly) -> Poly:
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, Fraction(0)) + c
    return clean(out)


def pscale(c: Fraction, a: Poly) -> Poly:
    c = Fraction(c)
    return {} if not c else clean({m: c * v for m, v in a.items()})


def pmul(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            m = tuple(x + y for x, y in zip(ma, mb))
            out[m] = out.get(m, Fraction(0)) + ca * cb
    return clean(out)


def pvar(i: int, n: int) -> Poly:
    e = [0] * n
    e[i] = 1
    return {tuple(e): Fraction(1)}


def bracket_poly(a: list[Poly], b: list[Poly]) -> list[Poly]:
    da = len(a) - 1
    db = len(b) - 1
    out = [{} for _ in range(da + db - 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            exponent = i + j - 1
            factor = i * db - da * j
            if exponent >= 0 and factor:
                out[exponent] = padd(
                    out[exponent], pscale(Fraction(factor), pmul(ai, bj))
                )
    return out


def direct_bracket_poly(a: list[Poly], b: list[Poly]) -> list[Poly]:
    """Independent derivative/dictionary implementation."""
    da = len(a) - 1
    db = len(b) - 1

    def dx(v, d):
        return {(i - 1, d - i): pscale(Fraction(i), c)
                for i, c in enumerate(v) if i and c}

    def dy(v, d):
        return {(i, d - i - 1): pscale(Fraction(d - i), c)
                for i, c in enumerate(v) if d - i and c}

    def mul_hom(p, q):
        out = {}
        for (i, j), c in p.items():
            for (k, ell), d in q.items():
                key = (i + k, j + ell)
                out[key] = padd(out.get(key, {}), pmul(c, d))
        return out

    p = mul_hom(dx(a, da), dy(b, db))
    q = mul_hom(dy(a, da), dx(b, db))
    total = da + db - 2
    return [padd(p.get((i, total - i), {}),
                 pscale(Fraction(-1), q.get((i, total - i), {})))
            for i in range(total + 1)]


def poly_vector_add(a: list[Poly], b: list[Poly]) -> list[Poly]:
    assert len(a) == len(b)
    return [padd(x, y) for x, y in zip(a, b)]


def mat_poly_vec(a: list[list[Fraction]], v: list[Poly]) -> list[Poly]:
    return [sum_polys(pscale(c, p) for c, p in zip(row, v)) for row in a]


def sum_polys(values) -> Poly:
    out: Poly = {}
    for p in values:
        out = padd(out, p)
    return out


def rref_transform(a: list[list[Fraction]]):
    m = [list(map(Fraction, row)) for row in a]
    rows = len(m)
    cols = len(m[0]) if rows else 0
    t = [[Fraction(int(i == j)) for j in range(rows)] for i in range(rows)]
    pivots = []
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        t[r], t[pivot] = t[pivot], t[r]
        unit = m[r][c]
        m[r] = [x / unit for x in m[r]]
        t[r] = [x / unit for x in t[r]]
        for i in range(rows):
            if i != r and m[i][c]:
                scale = m[i][c]
                m[i] = [x - scale * y for x, y in zip(m[i], m[r])]
                t[i] = [x - scale * y for x, y in zip(t[i], t[r])]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    return m, pivots, t


def fresh_matrix(p_degree: int, q_degree: int,
                 p_top: list[Fraction], q_top: list[Fraction]):
    cols = []
    for i in range(p_degree + 1):
        col = parent.bracket(parent.basis_poly(p_degree, i), q_top)
        assert col == parent.direct_bracket(parent.basis_poly(p_degree, i), q_top)
        cols.append(col)
    for j in range(q_degree + 1):
        col = parent.bracket(p_top, parent.basis_poly(q_degree, j))
        assert col == parent.direct_bracket(p_top, parent.basis_poly(q_degree, j))
        cols.append(col)
    rows = p_degree + len(q_top) - 2
    return parent.matrix_from_columns(cols, rows)


def direction_polys(dirs: list[list[Fraction]], start: int,
                    count: int, nvars: int) -> list[Poly]:
    out = []
    for k in range(count):
        p: Poly = {}
        for j, direction in enumerate(dirs):
            if direction[start + k]:
                p = padd(p, pscale(direction[start + k], pvar(j, nvars)))
        out.append(p)
    return out


def primitive(p: Poly) -> Poly:
    p = clean(p)
    if not p:
        return {}
    den = 1
    for c in p.values():
        den = math.lcm(den, c.denominator)
    ints = {m: int(c * den) for m, c in p.items()}
    g = 0
    for c in ints.values():
        g = math.gcd(g, abs(c))
    if g:
        ints = {m: c // g for m, c in ints.items()}
    first = min(ints)
    if ints[first] < 0:
        ints = {m: -c for m, c in ints.items()}
    return {m: Fraction(c) for m, c in ints.items() if c}


def poly_json(p: Poly):
    return [[list(m), parent.fstr(c)] for m, c in sorted(p.items())]


def coefficient_matrix(polys: list[Poly], monomials: list[tuple[int, ...]]):
    return [[p.get(m, Fraction(0)) for m in monomials] for p in polys]


def same_span(a: list[Poly], b: list[Poly]) -> bool:
    mons = sorted({m for p in a + b for m in p})
    ma = coefficient_matrix(a, mons)
    mb = coefficient_matrix(b, mons)
    return parent.rank(ma) == parent.rank(mb) == parent.rank(ma + mb)


def render_poly(p: Poly, names: list[str]) -> str:
    p = primitive(p)
    if not p:
        return "0"
    pieces = []
    for m, raw_c in sorted(p.items()):
        c = int(raw_c)
        mon_parts = []
        for name, e in zip(names, m):
            if e == 1:
                mon_parts.append(name)
            elif e > 1:
                mon_parts.append(f"{name}^{e}")
        mon = "*".join(mon_parts)
        mag = abs(c)
        body = mon if mon and mag == 1 else (f"{mag}*{mon}" if mon else str(mag))
        if not pieces:
            pieces.append(("-" if c < 0 else "") + body)
        else:
            pieces.append(("-" if c < 0 else "+") + body)
    return "".join(pieces)


def sha_matrix(a) -> str:
    return parent.matrix_sha(a)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stratum", choices=sorted(parent.REPRESENTATIVES), required=True)
    ap.add_argument("--algorithm", choices=("std", "slimgb"), required=True)
    ap.add_argument("--outdir", required=True)
    args = ap.parse_args()
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    K = list(map(Fraction, parent.REPRESENTATIVES[args.stratum]))
    P9 = parent.power(K, 3)
    Q12 = parent.power(K, 4)
    assert parent.bracket(P9, Q12) == parent.direct_bracket(P9, Q12)
    assert all(x == 0 for x in parent.bracket(P9, Q12))

    A = fresh_matrix(8, 11, P9, Q12)
    sdirs = parent.nullspace(A)
    assert all(all(sum(A[i][j] * v[j] for j in range(21)) == 0
                       for i in range(19)) for v in sdirs)

    B = fresh_matrix(7, 10, P9, Q12)
    rr, pivots, transform = rref_transform(B)
    rank_b = len(pivots)
    free = [j for j in range(19) if j not in pivots]
    assert parent.rank(transform) == 18
    transformed_b = [[sum(transform[i][k] * B[k][j] for k in range(18))
                      for j in range(19)] for i in range(18)]
    assert transformed_b == rr

    ns = len(sdirs)
    nt = len(free)
    nvars = ns + nt
    P8 = direction_polys(sdirs, 0, 9, nvars)
    Q11 = direction_polys(sdirs, 9, 12, nvars)
    source17 = bracket_poly(P8, Q11)
    assert source17 == direct_bracket_poly(P8, Q11)
    transformed_source = mat_poly_vec(transform, source17)

    v = [{} for _ in range(19)]
    for k, f in enumerate(free):
        v[f] = pvar(ns + k, nvars)
    for row, pivot in enumerate(pivots):
        rhs = pscale(Fraction(-1), transformed_source[row])
        for f in free:
            rhs = padd(rhs, pscale(-rr[row][f], v[f]))
        v[pivot] = rhs

    residual17 = poly_vector_add(mat_poly_vec(B, v), source17)
    transformed_residual = mat_poly_vec(transform, residual17)
    assert all(not transformed_residual[i] for i in range(rank_b))
    assert all(transformed_residual[i] == transformed_source[i]
               for i in range(rank_b, 18))
    obstruction17_raw = [p for p in transformed_source[rank_b:] if p]

    left_b = parent.nullspace(parent.transpose(B))
    obstruction17_left = [
        sum_polys(pscale(ell[i], source17[i]) for i in range(18))
        for ell in left_b
    ]
    obstruction17_left = [p for p in obstruction17_left if p]
    assert same_span(obstruction17_raw, obstruction17_left)

    P7 = v[:8]
    Q10 = v[8:]
    C = fresh_matrix(6, 9, P9, Q12)
    left_c = parent.nullspace(parent.transpose(C))
    source16 = poly_vector_add(
        bracket_poly(P8, Q10), bracket_poly(P7, Q11)
    )
    direct16 = poly_vector_add(
        direct_bracket_poly(P8, Q10), direct_bracket_poly(P7, Q11)
    )
    assert source16 == direct16
    obstruction16_raw = [
        sum_polys(pscale(ell[i], source16[i]) for i in range(17))
        for ell in left_c
    ]
    obstruction16_raw = [p for p in obstruction16_raw if p]

    obstruction17 = [primitive(p) for p in obstruction17_raw]
    obstruction16 = [primitive(p) for p in obstruction16_raw]
    all_obstructions = obstruction17 + obstruction16
    assert all_obstructions and all(not p.get(tuple([0] * nvars), 0)
                                    for p in all_obstructions)

    mon17 = sorted({m for p in obstruction17 for m in p})
    mon16 = sorted({m for p in obstruction16 for m in p})
    result = {
        "schema": "binary-cubic-three-bands-v1",
        "scope": "char0 denominator-free homogeneous bands through degree 16 only",
        "stratum": args.stratum,
        "algorithm": args.algorithm,
        "K": [parent.fstr(x) for x in K],
        "top_zero": True,
        "degree18": {
            "rows": 19, "columns": 21, "rank": parent.rank(A),
            "kernel_dimension": ns, "matrix_sha256": sha_matrix(A),
            "kernel": [[parent.fstr(x) for x in row] for row in sdirs],
        },
        "degree17": {
            "fresh_rows": 18, "fresh_columns": 19, "fresh_rank": rank_b,
            "fresh_kernel_dimension": nt,
            "fresh_cokernel_dimension": 18 - rank_b,
            "matrix_sha256": sha_matrix(B),
            "rref_sha256": sha_matrix(rr),
            "row_transform_sha256": sha_matrix(transform),
            "pivot_columns": pivots, "free_columns": free,
            "nonzero_obstruction_count": len(obstruction17),
            "obstruction_span_rank": parent.rank(
                coefficient_matrix(obstruction17, mon17)
            ),
            "left_projection_span_equal": True,
            "obstructions": [poly_json(p) for p in obstruction17],
        },
        "degree16": {
            "fresh_rows": 17, "fresh_columns": 17,
            "fresh_rank": parent.rank(C),
            "fresh_kernel_dimension": 17 - parent.rank(C),
            "fresh_cokernel_dimension": len(left_c),
            "matrix_sha256": sha_matrix(C),
            "nonzero_obstruction_count": len(obstruction16),
            "obstruction_span_rank": parent.rank(
                coefficient_matrix(obstruction16, mon16)
            ) if obstruction16 else 0,
            "obstructions": [poly_json(p) for p in obstruction16],
        },
        "combined": {
            "parameter_count": nvars,
            "s_parameter_count": ns,
            "t_parameter_count": nt,
            "generator_count": len(all_obstructions),
        },
        "controls": {
            "independent_bracket_agreement": True,
            "invertible_degree17_row_transform": True,
            "degree17_original_incidence_identity": True,
            "degree17_left_projection_span_equal": True,
            "zero_lower_faces_pass": True,
        },
        "refuses": [
            "bands below degree 16", "all-depth lift", "B9 residue preservation",
            "selected Q8 landing", "maximum twelve", "counterexample", "JC2"
        ],
    }
    result_path = outdir / "result.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    names = [f"s{i + 1}" for i in range(ns)] + [f"t{i + 1}" for i in range(nt)]
    rendered = [render_poly(p, names) for p in all_obstructions]
    lines = [
        "// Auto-generated exact three-band obstruction ideal.",
        "option(redSB);",
        f"ring R=0,({','.join(names)}),dp;",
        "ideal I=" + ",\n  ".join(rendered) + ";",
        "ideal G=" + ("std(I);" if args.algorithm == "std" else "slimgb(I);") ,
        f'print("STRATUM {args.stratum}");',
        f'print("ALGORITHM {args.algorithm}");',
        'print("INPUT_GENERATORS "+string(size(I)));',
        'print("GB_GENERATORS "+string(size(G)));',
        'print("DIMENSION "+string(dim(G)));',
        'print("GROEBNER_BEGIN");',
        "print(G);",
        'print("GROEBNER_END");',
        'print("PASS");',
        "quit;",
    ]
    sing_path = outdir / "three_bands.sing"
    sing_path.write_text("\n".join(lines) + "\n")

    print(json.dumps({
        "PASS": True,
        "stratum": args.stratum,
        "algorithm": args.algorithm,
        "degree18_rank_kernel": [parent.rank(A), ns],
        "degree17_rank_kernel_cokernel": [rank_b, nt, 18 - rank_b],
        "degree17_obstructions": len(obstruction17),
        "degree16_rank_kernel_cokernel": [parent.rank(C), 17 - parent.rank(C), len(left_c)],
        "degree16_obstructions": len(obstruction16),
        "combined_parameters_generators": [nvars, len(all_obstructions)],
        "result_sha256": hashlib.sha256(result_path.read_bytes()).hexdigest(),
        "singular_sha256": hashlib.sha256(sing_path.read_bytes()).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()

