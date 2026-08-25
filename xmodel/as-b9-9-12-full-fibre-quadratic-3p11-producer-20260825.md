# Producer report: normalized B9 complete-family first quadratic gate

Date: 2026-08-25  
Status: **PROVISIONAL PRODUCER; DIFFERENT-MODEL SOURCE REVIEW PENDING**

## Exact claim

Fix the displayed B9 mod-243 parent consumed through normalized mod-729
source SHA-256
`d0c6fd4b62350b0d115aefd60846613ca7484dd3e5bdafdcd9339316b944a848`.
Its complete coefficient-box calculation with
`deg(P)<=9, deg(Q)<=12` gives a `3^145` family modulo `3^10=59049`.
The complete transition of that displayed family to
`3^11=177147` is nonempty.

More precisely, after introducing every one of the 146 fresh coefficient
digits and all 276 determinant rows, the liftable predecessor projection has
cardinality `3^101`; every projected predecessor has `3^61` fresh lifts.
Hence the displayed mod-`3^11` solution set has exactly `3^162` points.

## Exact divided equation

Write the map as `F=F5+243*T`.  The parent arrays `base_integer` and
`matrix_integer` have already divided the determinant equation by the outer
factor `243=3^5`.  The first nonlinear divided equation therefore uses the
remaining divisor `3^5=243`:

```text
(base_integer + matrix_integer*T)/3^5 + det J(T) + A*W = 0 (mod 3).
```

Before that stored predivision the same equation is

```text
(D5 + 243*A*T)/3^10 + det J(T) + A*W = 0 (mod 3).
```

Thus `243^2 det J(T)` vanishes through modulus `3^10` and first contributes
to the divided carry for `3^10 -> 3^11`.  This is the first genuinely
quadratic transition of the displayed family.

## Complete elimination certificate

The fresh operator is the complete `276 x 146` determinant matrix over
`F3`.  It has rank 85, right-kernel dimension 61, and left-cokernel
dimension 191.  An invertible change of the 145 predecessor coordinates
separates:

- 17 directions visible in `T mod 3`, which carry every quadratic term;
- 128 exact directions divisible by three.

The 128 spectators have rank 44 in the fresh cokernel and kernel dimension
84.  The compiler projects the constant coefficient, all 17 linear
coefficients, all 17 diagonal quadratic coefficients, and all 136 cross
coefficients to that cokernel.  Their combined coefficient span has rank 15.
Adjoining every coefficient to the spectator image leaves rank exactly 44.
Consequently the post-elimination quadratic system has **zero equations**.
This is coefficientwise containment of the complete degree-two polynomial,
not sampling of the `3^17` active assignments.

The predecessor projection exponent is therefore
`17+(128-44)=101`, and adjoining the 61-dimensional fresh kernel gives total
exponent `162`.

## Literal witness and degree scope

At the zero active assignment, the compiler constructs an exact spectator
particular and fresh-digit particular.  Literal integer expansion verifies
all 276 coefficients of `det J(P,Q)-1` modulo `177147`; the determinant
payload SHA-256 is
`3dc78ec4fa6f312837b8f6c512ce1625e7842929a37104763c62f905f746e16d`.

Measured modulo the target, both the partial-y and total-degree pairs are
exactly `(9,12)`.  No coefficient outside the normalized monomial boxes is
introduced.

## Custody and controls

Box02 and Box03 compiled the same source-hashed closure and emitted
byte-identical result SHA-256
`984dbcf57ce181c5f07308f80950b38a9c78174cd9c802c868b46ce337e90539`.
The exact ANF and SMT payload SHA-256 values are, respectively,
`2a65d00367451476f31941426f086de0fef53bc0b73478e4eb9fa87fb2cf913e`
and
`4868d7e0b88855c6a9f751b3ad42a8a1c4a08694f5ffb76baad1784123ecf8bd`.

The compiler also source-replays the complete parent linear-window result at
SHA-256
`8c4060e8e48978492e115955af167e11149d6ba18be83ee3c82121834d617667`.
Dual-host byte equality is deployment evidence, not an independent
mathematical vote.

## Refusal scope

This proves only the complete `3^10 -> 3^11` transition of the displayed
normalized family over one fixed B9 mod-243 parent.  It does not cover the
complete earlier mod-243 fibre, prove a mod-`3^12` lift, produce an
inverse-limit or characteristic-zero point, establish common-cubic landing,
prove a maximum-twelve theorem, give a counterexample, or prove JC2.
