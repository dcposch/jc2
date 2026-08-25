#!/usr/bin/env python3
"""Complete exact homogeneous incidence through determinant degree 15."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path


THREE_PATH = (
    Path(__file__).resolve().parents[1]
    / "max12_912_order1_binary_cubic_three_bands_aws_20260825"
    / "compile_three_bands.py"
)
spec = importlib.util.spec_from_file_location("binary_cubic_three", THREE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load pinned three-band compiler")
three = importlib.util.module_from_spec(spec)
spec.loader.exec_module(three)
parent = three.parent
Poly = three.Poly


def parameterize_fresh(matrix, source: list[Poly], variable_offset: int,
                       nvars: int):
    rr, pivots, transform = three.rref_transform(matrix)
    rank_value = len(pivots)
    free = [j for j in range(len(matrix[0])) if j not in pivots]
    assert parent.rank(transform) == len(matrix)
    transformed_matrix = [
        [sum(transform[i][k] * matrix[k][j] for k in range(len(matrix)))
         for j in range(len(matrix[0]))]
        for i in range(len(matrix))
    ]
    assert transformed_matrix == rr
    transformed_source = three.mat_poly_vec(transform, source)

    values = [{} for _ in range(len(matrix[0]))]
    for k, f in enumerate(free):
        values[f] = three.pvar(variable_offset + k, nvars)
    for row, pivot in enumerate(pivots):
        rhs = three.pscale(Fraction(-1), transformed_source[row])
        for f in free:
            rhs = three.padd(rhs, three.pscale(-rr[row][f], values[f]))
        values[pivot] = rhs

    residual = three.poly_vector_add(
        three.mat_poly_vec(matrix, values), source
    )
    transformed_residual = three.mat_poly_vec(transform, residual)
    assert all(not transformed_residual[i] for i in range(rank_value))
    assert all(transformed_residual[i] == transformed_source[i]
               for i in range(rank_value, len(matrix)))
    obstruction = [p for p in transformed_source[rank_value:] if p]

    left = parent.nullspace(parent.transpose(matrix))
    projected = [
        three.sum_polys(three.pscale(ell[i], source[i])
                        for i in range(len(matrix)))
        for ell in left
    ]
    projected = [p for p in projected if p]
    assert three.same_span(obstruction, projected)
    return {
        "rr": rr,
        "pivots": pivots,
        "free": free,
        "transform": transform,
        "values": values,
        "obstruction": [three.primitive(p) for p in obstruction],
        "rank": rank_value,
        "cokernel": len(matrix) - rank_value,
        "span_equal": True,
    }


def span_rank(polys: list[Poly]) -> int:
    if not polys:
        return 0
    mons = sorted({m for p in polys for m in p})
    return parent.rank(three.coefficient_matrix(polys, mons))


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
    assert not any(parent.bracket(P9, Q12))

    A = three.fresh_matrix(8, 11, P9, Q12)
    sdirs = parent.nullspace(A)
    B = three.fresh_matrix(7, 10, P9, Q12)
    C = three.fresh_matrix(6, 9, P9, Q12)
    D = three.fresh_matrix(5, 8, P9, Q12)

    ns = len(sdirs)
    nt = len(B[0]) - parent.rank(B)
    nu = len(C[0]) - parent.rank(C)
    nvars = ns + nt + nu

    P8 = three.direction_polys(sdirs, 0, 9, nvars)
    Q11 = three.direction_polys(sdirs, 9, 12, nvars)
    source17 = three.bracket_poly(P8, Q11)
    assert source17 == three.direct_bracket_poly(P8, Q11)
    inc17 = parameterize_fresh(B, source17, ns, nvars)
    assert len(inc17["free"]) == nt
    P7 = inc17["values"][:8]
    Q10 = inc17["values"][8:]

    source16 = three.poly_vector_add(
        three.bracket_poly(P8, Q10), three.bracket_poly(P7, Q11)
    )
    direct16 = three.poly_vector_add(
        three.direct_bracket_poly(P8, Q10),
        three.direct_bracket_poly(P7, Q11),
    )
    assert source16 == direct16
    inc16 = parameterize_fresh(C, source16, ns + nt, nvars)
    assert len(inc16["free"]) == nu
    P6 = inc16["values"][:7]
    Q9 = inc16["values"][7:]

    source15 = three.poly_vector_add(
        three.poly_vector_add(
            three.bracket_poly(P8, Q9), three.bracket_poly(P7, Q10)
        ),
        three.bracket_poly(P6, Q11),
    )
    direct15 = three.poly_vector_add(
        three.poly_vector_add(
            three.direct_bracket_poly(P8, Q9),
            three.direct_bracket_poly(P7, Q10),
        ),
        three.direct_bracket_poly(P6, Q11),
    )
    assert source15 == direct15
    left_d = parent.nullspace(parent.transpose(D))
    obs15 = [
        three.sum_polys(three.pscale(ell[i], source15[i]) for i in range(16))
        for ell in left_d
    ]
    obs15 = [three.primitive(p) for p in obs15 if p]

    obs17 = inc17["obstruction"]
    obs16 = inc16["obstruction"]
    all_obs = obs17 + obs16 + obs15
    zero = tuple([0] * nvars)
    assert all_obs and all(not p.get(zero, 0) for p in all_obs)

    result = {
        "schema": "binary-cubic-four-bands-v1",
        "scope": "char0 denominator-free homogeneous bands through degree 15 only",
        "stratum": args.stratum,
        "algorithm": args.algorithm,
        "K": [parent.fstr(x) for x in K],
        "degree18": {
            "rows": 19, "columns": 21, "rank": parent.rank(A),
            "kernel_dimension": ns, "matrix_sha256": parent.matrix_sha(A),
        },
        "degree17": {
            "fresh_rows": 18, "fresh_columns": 19,
            "fresh_rank": inc17["rank"],
            "fresh_kernel_dimension": len(inc17["free"]),
            "fresh_cokernel_dimension": inc17["cokernel"],
            "matrix_sha256": parent.matrix_sha(B),
            "obstruction_count": len(obs17),
            "obstruction_span_rank": span_rank(obs17),
            "left_projection_span_equal": inc17["span_equal"],
            "obstructions": [three.poly_json(p) for p in obs17],
        },
        "degree16": {
            "fresh_rows": 17, "fresh_columns": 17,
            "fresh_rank": inc16["rank"],
            "fresh_kernel_dimension": len(inc16["free"]),
            "fresh_cokernel_dimension": inc16["cokernel"],
            "matrix_sha256": parent.matrix_sha(C),
            "obstruction_count": len(obs16),
            "obstruction_span_rank": span_rank(obs16),
            "left_projection_span_equal": inc16["span_equal"],
            "obstructions": [three.poly_json(p) for p in obs16],
        },
        "degree15": {
            "fresh_rows": 16, "fresh_columns": 15,
            "fresh_rank": parent.rank(D),
            "fresh_kernel_dimension": 15 - parent.rank(D),
            "fresh_cokernel_dimension": len(left_d),
            "matrix_sha256": parent.matrix_sha(D),
            "obstruction_count": len(obs15),
            "obstruction_span_rank": span_rank(obs15),
            "obstructions": [three.poly_json(p) for p in obs15],
        },
        "combined": {
            "s_parameters": ns, "t_parameters": nt, "u_parameters": nu,
            "base_parameter_count": nvars,
            "generator_count": len(all_obs),
            "full_incidence_adds_degree15_fresh_kernel": 15 - parent.rank(D),
        },
        "controls": {
            "independent_bracket_agreement": True,
            "degree17_original_incidence_identity": True,
            "degree16_original_incidence_identity": True,
            "degree17_left_projection_span_equal": True,
            "degree16_left_projection_span_equal": True,
            "zero_lower_faces_pass": True,
        },
        "refuses": [
            "bands below degree 15", "all-depth lift", "B9 residue preservation",
            "selected Q8 landing", "maximum twelve", "counterexample", "JC2",
        ],
    }
    result_path = outdir / "result.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")

    names = ([f"s{i + 1}" for i in range(ns)]
             + [f"t{i + 1}" for i in range(nt)]
             + [f"u{i + 1}" for i in range(nu)])
    rendered = [three.render_poly(p, names) for p in all_obs]
    lines = [
        "// Auto-generated exact four-band obstruction ideal.",
        "option(redSB);",
        f"ring R=0,({','.join(names)}),dp;",
        "ideal I=" + ",\n  ".join(rendered) + ";",
        "ideal G=" + ("std(I);" if args.algorithm == "std" else "slimgb(I);"),
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
    sing_path = outdir / "four_bands.sing"
    sing_path.write_text("\n".join(lines) + "\n")
    print(json.dumps({
        "PASS": True,
        "stratum": args.stratum,
        "algorithm": args.algorithm,
        "degree17_obstructions": len(obs17),
        "degree16_obstructions": len(obs16),
        "degree15_rank_kernel_cokernel": [
            parent.rank(D), 15 - parent.rank(D), len(left_d)
        ],
        "degree15_obstructions": len(obs15),
        "combined_parameters_generators": [nvars, len(all_obs)],
        "result_sha256": hashlib.sha256(result_path.read_bytes()).hexdigest(),
        "singular_sha256": hashlib.sha256(sing_path.read_bytes()).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()

