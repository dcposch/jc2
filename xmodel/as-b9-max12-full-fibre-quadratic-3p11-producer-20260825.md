# Producer report: B9 full-family first quadratic gate at `3^11`

Date: 2026-08-25  
Status: **PROVISIONAL PRODUCER; DIFFERENT-MODEL SOURCE REVIEW PENDING**

## Exact claim

Fix the displayed B9 mod-243 point consumed by parent source SHA-256
`0bf4766d8e4840fb89661eaba6b8cb4661b554c7f8944f5eb55bac37298f2ac7`.
Its complete fixed-total-degree-12 linear-window calculation gives a
`3^165` family modulo `3^10=59049`.  The complete transition of that family
to modulus `3^11=177147` is nonempty.

More precisely, after introducing all 182 fresh coefficient digits and all
276 determinant rows, the liftable predecessor projection has cardinality
`3^109`; each predecessor has `3^74` fresh lifts.  Hence the displayed
mod-`3^11` solution set has exactly `3^183` points.

## Source equation and the off-by-five firewall

Write the map as `F=F5+243*T`.  The stored arrays `base_integer` and
`matrix_integer` have already divided the determinant equation by the outer
factor `243=3^5`.  Therefore the first nonlinear divided equation uses the
remaining divisor `3^5=243`:

```text
(base_integer + matrix_integer*T)/3^5 + det J(T) + A*W = 0 (mod 3).
```

Equivalently, before the stored predivision this is

```text
(D5 + 243*A*T)/3^10 + det J(T) + A*W = 0 (mod 3).
```

The quadratic `243^2 det J(T)` is zero through modulus `3^10` and first
appears in this divided carry for `3^10 -> 3^11`.  No `3^10`/`3^5`
interchange is being made.

## Exact elimination certificate

The complete fresh operator is the same `276 x 182` matrix of rank 108 over
`F3`; its left cokernel has dimension 168 and its right kernel dimension 74.
An invertible change of the 165 predecessor coordinates splits them into:

- 18 directions visible in `T mod 3`, which carry the quadratic terms;
- 147 exact directions divisible by three, whose image in the fresh
  cokernel has rank 56 and kernel dimension 91.

The compiler projects the constant, all 18 linear coefficients, all 18
diagonal quadratic coefficients, and all 153 cross coefficients to the
fresh cokernel.  Their combined coefficient span has rank 16.  Adjoining
all of them to the rank-56 spectator image leaves rank exactly 56.  Thus
every coefficient lies in the spectator image, coefficientwise, and the
post-elimination quadratic system has **zero equations**.  This is a full
polynomial identity, not a sample of the `3^18` active assignments.

It follows that the predecessor projection has exponent
`18+(147-56)=109`, while adding the fresh kernel gives total exponent
`109+74=183`.

## Literal witness and degree scope

The zero active assignment admits an exact spectator particular with 16
nonzero coordinates and a fresh particular with 46 nonzero coordinates.
All 276 coefficients of `det J(P,Q)-1` vanish modulo `177147`; determinant
payload SHA-256 is
`6c0156ef3a1305bc3532d3cc9506f28e710f6d69150453ce51ab341595953324`.

Measured modulo `177147`, both the partial-y degree pair and total-degree
pair are honestly `(12,12)`.  In particular, the P coefficient at `(0,12)`
is nonzero modulo the target.  This result belongs to the broader D12 lane,
not the normalized `(9,12)` coefficient box.

## Independent endpoints and controls

Box02 and Box03 compiled the same pinned 183-file source closure and emitted
byte-identical result SHA-256
`7a1b5da26974ee5e5f4fb42ade1575abc0b18d9de54349c8fdcc08ab4a267379`.
The exact ANF and SMT payload SHAs are respectively
`60f645cf7d03100eed6d56c7269a2138a628a498d105bae492acd6ab8b64575f`
and `616f406a35ef99e3d6540d4321787be1dc8153af4c6810a64c4ccf59aaf4ecfc`.

The emitted four-bit BV arithmetic was cross-checked against the direct ANF
evaluator on a 190-point degree-two design; every intermediate product and
iterated sum is reduced before it can overflow.  Z3 4.16 and Boolector both
returned the all-zero active model, which matches the literal-replay witness.
Boolector required a custody transform deleting unsupported `set-option` and
`get-model` commands; the transformed formula is separately hashed.

Two failed predecessors are retained, not used as evidence:

- V2 failed because a degree helper was not exported by the dynamic parent;
- V3 correctly failed an over-strict assertion that the lifted map remained
  `(9,12)/(11,12)`.  That failure exposed the genuine `(12,12)` support.

## Refusal scope

This proves only the complete `3^10 -> 3^11` transition of one displayed
fixed-D12 family over one fixed B9 mod-243 parent.  It does not prove a
mod-`3^12` lift, an inverse-limit or characteristic-zero point, coverage of
the complete earlier mod-243 fibre, a maximum-twelve theorem, a
counterexample, or JC2.
