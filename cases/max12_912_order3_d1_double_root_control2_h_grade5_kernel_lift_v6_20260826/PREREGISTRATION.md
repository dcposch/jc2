# Preregistration: eta-five h-linear correction inside the Q-R kernel

Date: 2026-08-26 UTC

Reconstruct the frozen V5 scalar h-correction from source.  Let `A_QR` be the
complete eight-column map from scalar row-multiplier corrections to the
h-linear Q-R component.  Require exact rank 3, the reviewed free-zero solution
`g0=(11/6,-11/12,0,...,0)`, and a complete five-vector rational basis of
`ker(A_QR)`.

After applying `g0`, extract the entire next closed-corner grade: every pure
R-square and pure Q-cubic monomial in the h-linear coefficient.  These are
exactly the terms with pre-h margin `-5` at
`alpha=15/2,beta=delta=5`.  Map all five Q-R-kernel basis vectors to this
grade and solve

```text
sum_j a_j * grade5(sum_i kernel[j,i] E_i(0))
    = -grade5(C1 + sum_i g0_i E_i(0)).
```

Use exact RREF with free columns zero.  If inconsistent, emit a checked
left-cokernel functional.  Such a result obstructs only scalar h corrections;
polynomial multiplier corrections remain open.  If solvable, set
`g=g0+sum a_j kernel_j`, form the exact full witness
`sum_i(F_i'+h*g_i)E_i(h)`, require both the Q-R and grade-five h-linear
pieces to vanish, and recompute the complete eta threshold.

Run forward/reverse encodings on two registered AWS hosts under explicit
caps.  No local exact computation.  No eta-face, general multiplier-support,
h-adic, moving-source/load, whole-fan, D1, or JC2 inference beyond the exact
certificate.
