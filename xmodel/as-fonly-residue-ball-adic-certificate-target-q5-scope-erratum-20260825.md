# Erratum: Q5/H6 scope in the adic-certificate strategy note

Status: **NONMUTATING SCOPE CORRECTION**

Date: 2026-08-25

Parent note (bytes preserved):

```text
xmodel/as-fonly-residue-ball-adic-certificate-target-20260825.md
SHA-256 7ad06a4ff0e27cae151bb32c76de9b76b7c73b9ffc12a8014f131a83c93ffbf4
```

Section 4's phrase “the current complete chronological chart” is retracted.
The exact frozen Q5/H6 preregistration says that its 142-trit, 197-row gate
is **not a complete chronological map modulo 243**.  It is complete only for
its displayed accepted Q6/high + Q5 row set:

```text
20 + 5 + 12 + 11 + 23 + 22 + 19 + 9 + 7 + 6 + 63 rows.
```

The corrected V2 replay checks those rows and literal `/243` agreement only
in degrees 12 through 7, together with the six Q5 rows in degree five.  It
does not restore the missing degree-four-through-zero source rows.

Therefore a Q5/H6 SAT model has exactly this scope:

```text
survives the complete displayed Q5/high filtered-source gate;
not yet det J=1 mod 243 as a full polynomial identity.
```

The residue-ball collision theorem cannot attach at Q5.  The chronological
successor must adjoin homogeneous order-81 pieces and restore, with exact
source carries and terminal recomputation,

```text
Q4/H5,J5, then Q3/H4,J4, Q2/H3,J3, Q1/H2,J2, and Q0/H1,J1,
```

or an exactly equivalent full-row compiler.  Only a final direct integer
replay showing that **every** coefficient of `det J(P,Q)-1` vanishes modulo
243 licenses the automatic moving-collision corollary.

The analytic certificate target itself remains unchanged: a complete fixed-
support residue-tube ideal, or a disjoint exhaustive transition DAG whose
leaves reconstruct complete determinant equations.  Q5 is one internal DAG
node, not the whole tube.
