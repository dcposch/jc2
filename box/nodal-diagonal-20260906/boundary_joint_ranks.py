#!/usr/bin/env python3
"""Exact current-band ranks for Jacobian plus upper characteristic rows.

These are coordinate counts after Q-unit pivots, not ideal dimensions. Older
compatibility equations and all later bands remain explicit obligations.
"""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
import time
import sympy as sp

from boundary_counts import SPECS
from boundary_jacobian_ranks import boundary, term_polynomial


def matrix_rows(columns):
    terms = [(c, a, b) for col in columns for c, a, b in col if c]
    if not terms:
        return [], [0, 0]
    W, Z = min(a for _, a, _ in terms), min(b for _, _, b in terms)
    polynomials = [term_polynomial(col, W, Z) for col in columns]
    count = max((max(p, default=-1) for p in polynomials), default=-1) + 1
    return [[p.get(i, 0) for p in polynomials] for i in range(count)], [W, Z]


def run(Fspec, Gspec):
    name, n, d, hF, poleF, scale = Fspec
    _, m, _, hG, poleG, _ = Gspec
    k = n // 3
    pF, qF = (24, 84) if n == 108 else (27, 72)
    pG, qG = (16, 56) if n == 108 else (18, 48)
    pP, qP = pF // 3, qF // 3
    initial = total_rank = remaining = 0
    digest, blocks = sha256(), []
    for r in range(1, n + 1):
        LF, MF, freeF = boundary(n, d, hF, poleF, scale, n-r)
        LG, MG, freeG = boundary(m, d, hG, poleG, scale, m-r)
        Jcols, Rcols, labels = [], [], []
        for j in range(freeF):
            a, b = LF+j, MF
            Jcols.append([((n-r)*pG-m*a, a+pG-1, b+qG),
                          ((n-r)*qG-m*b, a+pG, b+qG-1)])
            Rcols.append([(-2, a, b)])
            labels.append(["F", j])
        for j in range(freeG):
            a, b = LG+j, MG
            Jcols.append([(n*a-(m-r)*pF, a+pF-1, b+qF),
                          (n*b-(m-r)*qF, a+pF, b+qF-1)])
            Rcols.append([(3, a+pP, b+qP)])
            labels.append(["G", j])
        new_scalar = {k:"b", 2*k:"a", 3*k:"c"}.get(r)
        if new_scalar:
            Jcols.append([])
            power = 3-r//k
            Rcols.append([(1, power*pP, power*qP)])
            labels.append(["target", new_scalar])
        jrows, jfactor = matrix_rows(Jcols)
        rrows, rfactor = matrix_rows(Rcols)
        rows = jrows+rrows
        matrix = sp.Matrix(rows) if rows else sp.zeros(0, len(labels))
        reduced, pivots = matrix.rref()
        rank, kernel = len(pivots), len(labels)-len(pivots)
        assert kernel == freeG + bool(new_scalar), (name, r, kernel, freeG, new_scalar)
        initial += len(labels)
        total_rank += rank
        remaining += kernel
        digest.update(repr((r, labels, jfactor, rfactor, rows, pivots)).encode())
        blocks.append(dict(depth=r, current_F_generators=freeF,
                           current_G_generators=freeG, introduced_target_scalar=new_scalar,
                           J_common_factor=jfactor, R_factor_after_P_cubed=rfactor,
                           J_rows=len(jrows), characteristic_rows=len(rrows),
                           columns=len(labels), rank=rank, kernel=kernel,
                           pivot_columns=list(pivots), all_compatibility_rows_retained=True))
    return dict(client=name.removesuffix("_F"),
                boundary_FG_plus_b_a_c_generators=initial,
                rational_current_band_pivots=total_rank,
                remaining_generators_before_target_constant_e0=remaining,
                d_introduction_depth=4*k, d_new_generators=1, d_rational_pivots=1,
                d_net_generators=0,
                e0_status="Independent target constant if retained: adds one; does not enter any upper, face, or Jacobian equation",
                maximum_combined_rows=max(b["J_rows"]+b["characteristic_rows"] for b in blocks),
                maximum_columns=max(b["columns"] for b in blocks),
                matrices_and_pivots_sha256=digest.hexdigest(), blocks=blocks)


def main():
    started=time.monotonic()
    clients=[run(SPECS[i],SPECS[i+1]) for i in (0,2,4)]
    out=dict(coefficient_field="Q", current_characteristic_linear_part="P^3*(3*P*g-2*f)",
             source_target_family="R=G^3-F^2+a*G^2+b*F*G+c*F+d*G+e0",
             scope="Coordinate counts after rational pivots; retained compatibility equations unevaluated; no dimension/properness verdict",
             elapsed_seconds=round(time.monotonic()-started,3),clients=clients)
    Path(__file__).with_suffix(".json").write_text(json.dumps(out,separators=(",", ":"))+"\n")
    print(json.dumps({**{k:v for k,v in out.items() if k!="clients"},
                      "clients":[{k:v for k,v in c.items() if k!="blocks"} for c in clients]},indent=2))


if __name__=="__main__":
    main()
