# Exact t=3 normalized quadratic-field certificate

Typing: exact symbolic preprocessing over Q and an exact Singular standard
basis over a degree-two extension of Q.  This is not a modular result and no
finite-t computation is promoted to a generic-t statement.

## Source and constant-pivot reduction

The deterministic source is `triangular_preprocess.py`, whose t=3 reduction
was checked generator by generator against the generic order-chart builder.
Thirteen eliminations have nonzero rational constant pivots.  Each has the
form `a*v+b`, with `a` in Q*, and replaces `v` by `-b/a`; consequently every
step is a quotient-ring isomorphism.  The resulting system has 37 equations
in 23 chart variables including `c`.  The complete map is in
`t3_ring_map.tsv` and its prior audit is in `reduction_audit.json`.

## Grading and the q4_1=1 slice

The driver `t3_normalized_slice.py` mechanically checked every monomial of
all 37 residual equations.  They are homogeneous for the following positive
weights:

```
b1,b2,b3,b4 = 1,2,3,4
a1_0,a2_0 = 4,8
a4_0,a5_0,a6_0,a7_0,a8_0,a9_0 = 16,20,24,28,32,36
q2_0,q3_0,q4_0,q4_1 = 8,12,16,13
q5_0,q5_1,q6_0,q6_1,q7_0,q7_1 = 20,17,24,21,25,26
c = 65
```

The unique row containing `c` is residual source 2 (zero based), and the
checked identity is

```
343*c = 10*q4_1*q7_1*(2*q4_1^2-21*q7_1).
```

Thus `c != 0` forces `x=q4_1 != 0`.  Over the algebraic closure, choose
lambda with `lambda^13*x=1` and map every residual variable `v` to
`lambda^weight(v)*v` (and the Rabinowitsch variable to
`lambda^(-65)*T`).  Homogeneity proves that this maps every saturated
solution to one with `x=1`; the reverse direction is inclusion.  Hence the
normalized slice is existence-equivalent to the original residual system on
the `c != 0` locus.

On this slice, source row 20 is the exact nonzero rational multiple `20/343`
of

```
H = 147*y^2-84*y+11,       y=q7_1,
```

and `c=10*y*(2-21*y)/343`.  The discriminant of `H` is 588, not a square in
Q, so `K=Q[y]/(H)` is a field.  Moreover `H(0)=11` and `H(2/21)=13/3`.
Therefore `y`, `2-21*y`, and the displayed image of `c` are units in `K`.
The driver checked the explicit inverse identities

```
y^(-1) = 84/11-147*y/11,
(2-21*y)^(-1) = 21*y/13-10/13
```

modulo `H`.  Consequently quotienting by `H` and eliminating `c,T` is an
isomorphism from the normalized Rabinowitsch quotient to a polynomial ring
over `K`.

## Quadratic-field affine elimination

After removing the minimal-polynomial row there are 29 distinct nonzero rows
in 20 auxiliary variables.  The deterministic pass finds 17 equations
`a(y)*v+b` with `a(y) != 0` in `K`.  Before each division it computes and
checks an inverse of `a(y)` modulo `H`; after substitution it checks that the
pivot row becomes zero modulo `H`.  The full coefficient, inverse, source
row, and substitution are recorded in `t3_normalized_K_pivots.tsv`.

These quotient isomorphisms leave six equations in exactly three variables
`b3,b4,a2_0`.  Their source rows are 5, 11, 17, 23, 28, and 33 (zero based),
at h-bands 0 through 5 with monomial tag `(0,1)`.  The source-row map,
homogeneity table, base-unit checks, duplicate/zero rows, and residual map
are recorded in `t3_normalized_audit.json`.

## Exact Singular certificate

Both exact algorithms returned the same reduced basis `[1]`:

| algorithm | input SHA-256 | wall | max RSS | exit | result |
|---|---|---:|---:|---:|---|
| `std` | `fc2c504604c51e33e7c63e32bde4a952d0c6741b99fcf5e9c334c63eefb4796b` | 0.04 s | 12,892 KB | 0 | `G[1]=1` |
| `slimgb` | `7f92d0cadce7bf892b6615030c8d28eb972496d459018c1cec63ac2fa9a112dd` | 0.57 s | 13,968 KB | 0 | `G[1]=1` |

Each run passed the actual-pair check `J=gamma`, the coefficient-field `c`
unit check, positive and negative empty/nonempty wrapper controls, and the
declared-ring check.  Standard-basis output and resource measurements are in
the correspondingly named `.out`, `.err`, and `.resource` files.

Since the final ideal is the unit ideal over `K`, the normalized slice has no
point over an algebraic closure.  The quotient isomorphisms and the weighted
normalization then imply that the original exact t=3 `c`-saturated residual
order-chart ideal is the unit ideal.  This proves saturated emptiness for the
necessary order-chart system at t=3.

<!-- BODY-END -->
