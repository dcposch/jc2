# Preregistration: sparse first-order `q2` syzygy lift

Date: 2026-08-26 UTC

Consume the frozen V1 transported identity only through its exact source and
canonical reconstruction.  Let `C_<80` be the five-term weight-75 correction
at `D=23`.  In the q2=0 row ideal, extract the complete weight-52 initial
forms of all eight rows and solve the graded rational linear problem

```text
sum_i g_i * in_52(E_i|q2=0) = - C_52
```

for constant `g_i`.  Free columns are set to zero after exact RREF; print the
full matrix rank, pivots, solution, and a literal equality check.  Then set

```text
F_i^(1) = F_i + q2*g_i,
W^(1)   = sum_i F_i^(1) E_i(full q2).
```

Independently pin the expanded-row decomposition

```text
C_52 = (1/9) in_52(E_2) - (1/12) in_52(E_1),
```

so the canonical free-zero correction must be `g_1=1/12`, `g_2=-1/9`,
and `g_3=...=g_8=0`.  The previously recorded `GH3/GH5/GH6` expression is
an equivalent representation in the special-fibre Groebner basis, not a
different row-module correction.

Require `W^(1)|q2=0=W`, exact divisibility of `W^(1)-W` by `q2`, and print
the entire corrected polynomial, correction, canonical hashes, and affine
weights.  At the sample weight, report every least-weight term.

This is only the first-order lift modulo the first bad graded piece.  If the
new correction is still of weight at most 80, iterate one graded layer at a
time; do not infer failure.  If the rational system is inconsistent, this
run gives no obstruction until a separately checked left-cokernel functional
is emitted.

Run two frozen expanded-source checks on AWS only: Box03 global `dp` and r6d
`(lp(2),dp(8))`.  Hash-pin V1, its charged source, and reviewed expanded B;
never consume the invalid factored-A row.  Any rc/stderr/diagnostic/hash or
cross-host canonical disagreement is no verdict.

Scope remains fixed axis/cusp and loads `k=nu=0,mu=2/3`; no full-support,
fan, D1, or JC2 claim.
