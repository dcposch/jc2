# Full chronological Q4 68-row affine gate

The five degree-four rows alone are not a chronological lift: adjoining
homogeneous degree-five fourth-digit polynomials `(H5,J5)` also changes the
sixty-three terminal divided-carry rows in total degrees 7 through 12.

For each source-replayed Q5 SAT model, construct the exact F3 affine system

```text
div(H5,J5) = -G4                     (5 rows),
fourth_digit_cross(H5,J5) = 0        (63 rows, degrees 7..12),
```

in all twelve coefficients of `(H5,J5)`.  Row-reduce the full 68-by-12
matrix without generic localization; record rank, augmented rank, a
particular solution and the complete kernel.  If consistent, reconstruct the
integer map and directly verify all five Q4 rows modulo 243 and all 63
terminal rows modulo 729, after the parent replay has checked all 197 input
rows.  If inconsistent, emit the exact RREF contradiction row.

The previously frozen Q4-only divergence sections are positive controls for
the first five rows and mandatory negative controls against omitting the
terminal 63.  Strict scope is pointwise in each exact SAT model.  No global
Q5-fibre, lower-row, complete-map, all-depth, or JC2 inference is licensed.
All substantive execution is AWS-only.

