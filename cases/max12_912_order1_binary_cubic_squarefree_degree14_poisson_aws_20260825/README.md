# Squarefree degree-14 Poisson gate

Dual AWS exact replay verifies, from the complete original degree-14 bracket
row,

```text
E14=3*K*[K,Z10],
729*R=324*C*W  modulo Z10,
```

and verifies the corrected denominator-cleared `Q7` formula.  The old
`(lambda/3)*V` shear term is explicitly nonzero and is retained as a negative
control.  Together with the separately verified zero degree-ten centralizer,
the reduced-point consequence is `K|C*W`, hence eight squarefree root
allocations.  Predicted dimensions are `19+5=24`.

Accepted tags are
`max12_912_order1_squarefree_degree14_poisson_v2_r6d_20260825T1927Z`
and
`max12_912_order1_squarefree_degree14_poisson_v2_box02_20260825T1929Z`.
Their verifier stdout is byte-identical; peak RSS is 11,700/11,464 KiB.

V1 is fail-closed diagnostic custody: Singular parsed `A^2/3` as a
nonintegral exponent and the hardened wrapper returned rc96.  It is not
evidence.  The theorem is reduced-point/radical scope only, not a nilpotent
scheme equality or a full Keller result.  Run `python3 replay.py`.
