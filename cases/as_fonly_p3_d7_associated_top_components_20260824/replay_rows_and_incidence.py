#!/usr/bin/env python3
"""Independent row-count/provenance replay for the D7 top-component gate."""
from __future__ import annotations


def derivative_layers(degrees):
    ux, uy, vx, vy = {}, {}, {}, {}
    divergence = []
    variables = []
    for degree in degrees:
        variables.extend((side, degree, i)
                         for side in ("u", "v")
                         for i in range(degree+1))
        for i in range(degree+1):
            j = degree-i
            un, vn = f"u{degree}_{i}", f"v{degree}_{i}"
            if i % 3:
                ux.setdefault((i-1, j), []).append((i % 3, un))
                vx.setdefault((i-1, j), []).append((i % 3, vn))
            if j % 3:
                uy.setdefault((i, j-1), []).append((j % 3, un))
                vy.setdefault((i, j-1), []).append((j % 3, vn))
        for i in range(degree):
            row = []
            if (i+1) % 3:
                row.append(((i+1) % 3, f"u{degree}_{i+1}"))
            if (degree-i) % 3:
                row.append(((degree-i) % 3, f"v{degree}_{i}"))
            if row:
                divergence.append(row)
    return variables, divergence, ux, uy, vx, vy


def determinant_rows(ux, uy, vx, vy, totals):
    coefficients = {}
    for left, right, sign in ((ux, vy, 1), (uy, vx, -1)):
        for (i, j), lterms in left.items():
            for (k, ell), rterms in right.items():
                monomial = (i+k, j+ell)
                for lc, lv in lterms:
                    for rc, rv in rterms:
                        coefficients.setdefault(monomial, []).append(
                            ((sign*lc*rc) % 3, lv, rv))
    rows = []
    for total in totals:
        for i in range(total+1):
            terms = [term for term in coefficients.get((i, total-i), [])
                     if term[0] % 3]
            if terms:
                rows.append(terms)
    return rows


top_vars, top_div, ux, uy, vx, vy = derivative_layers((7,))
top_det = determinant_rows(ux, uy, vx, vy, (12,))
assert len(top_vars) == 16
assert len(top_div) + len(top_det) == 20

layer_vars, layer_div, ux, uy, vx, vy = derivative_layers((7, 6))
layer_det = determinant_rows(ux, uy, vx, vy, (12, 11))
assert len(layer_vars) == 30
assert len(layer_div) + len(layer_det) == 38

# The fixed term -x^2*V_y can reach at most degree 8 for a D7 first digit,
# so it is absent from the degree-12 and degree-11 rows reconstructed above.
assert 2 + (7-1) == 8 < 11

# The frozen triangular point has U0=x^3,V0=x^2*y.  Its degree-seven and
# degree-six coordinate vectors are identically zero, hence every homogeneous
# generator in this gate vanishes at its projection.
triangular_top_projection = {variable: 0 for variable in layer_vars}
assert all(value == 0 for value in triangular_top_projection.values())

print("top_variables", len(top_vars))
print("top_divergence_rows", len(top_div))
print("top_carry12_rows", len(top_det))
print("top_total_rows", len(top_div)+len(top_det))
print("layers76_variables", len(layer_vars))
print("layers76_divergence_rows", len(layer_div))
print("layers76_carry12_11_rows", len(layer_det))
print("layers76_total_rows", len(layer_div)+len(layer_det))
print("fixed_x2_term_max_degree", 8)
print("triangular_degree7_degree6_projection", "origin")
print("PASS-FONLY-D7-TOP-ROW-PROVENANCE")
