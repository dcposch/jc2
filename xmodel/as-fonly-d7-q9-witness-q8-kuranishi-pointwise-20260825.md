# AS F-only `D=7`: pointwise Q9-to-Q8 Kuranishi obstruction

**Status: PRODUCER EXACT; PROVISIONAL PENDING DIFFERENT-MODEL REVIEW.**

For the first canonical witness emitted by the reviewed Q9 finite-state
gate, the corrected source equations at the next layer split into thirteen
accepted-image rows and nine degree-eight obstruction rows:

```text
E_2,
F_3 = E_3/3 + M_3 + div(W_4,Z_4),
F_5 = E_5/3 + M_5 + div(W_6,Z_6),
G_8 = F_8/3 + {C,D}_8 + T_8.                       (1)
```

All divisions in (1) are asserted over the integers before reduction
modulo three.  With the 32 restored coefficients
`(C_3,D_3,W_4,Z_4,W_6,Z_6)`, the exact affine coefficient matrix has

```text
accepted 13-row rank pair                  (13,13)
accepted-image kernel dimension                  19
full 22-row rank pair                      (13,14)
rank of the Kuranishi map on that kernel          0
Kuranishi cokernel dimension                       9.       (2)
```

The incompatibility has a one-coordinate certificate.  In zero-based row
ordering, `lambda=e_21`, the `x^8` row of `G_8`, satisfies

```text
lambda A = 0,       lambda b = 2 in F3.             (3)
```

Adding one to that RHS coordinate changes the pairing to zero, which checks
the sign and orientation.  The matrix and RHS hashes are respectively
`addcbc1ee35e97e868e6d12984bcbad151dbce3409448574256d48b1d85b1c0a`
and `f2c3b732c4343ffeb6bc4c832569e129a5eaff22a2869f0bb49c6c34da3098fd`.

The calculation ran on Box02 (`ip-172-30-0-186`), tag
`as_q9_q8_kuranishi_v3_20260825T020224Z`, in 10.81 seconds with 20,688 KiB
maximum RSS, return code zero, and empty standard error.  V1 and V2 remain
frozen assertion-failure controls; V3 consumes V2's definition prefix
byte-for-byte and fixes only the partial-row substitution check.

This is strictly a pointwise obstruction for one canonical Q9 coefficient
assignment.  The 16--19 free coordinates in a Q9 affine fibre can alter the
divided-carry/Kuranishi state.  Therefore (2)--(3) do **not** kill its
predecessor, any Q9 rank class, the D7 branch, or an all-depth lift.  The
next exact gate is the induced Kuranishi zero locus on those affine fibres,
together with a cross-rank test of which Bockstein residues must be retained
in a finite transition state.  There is no counterexample or JC2 inference.
