# Producer report: pointwise common-cubic obstruction at `3^12`

Date: 2026-08-25  
Status: **PROVISIONAL PRODUCER; DIFFERENT-MODEL REVIEW PENDING**

## Complete one-point gate

At the normalized common-cubic witness with SHA-256
`a39bc9185a21df92173b356c027a00650ced4b92cfc15d587a91b39c8aca299a`,
the source consumes all 299 equations and all 149 fresh coefficient/core
digits in

```text
J(w) u = -F(w)/3^11  (mod 3).
```

The exact ranks are

```text
rank J                    = 94
rank [J | -F/3^11]        = 95
kernel dimension          = 55
exact-gauge dimension     = 3
non-gauge kernel dimension= 52
left-cokernel dimension   = 205.
```

There are 31 nonzero coordinates in the emitted left-cokernel projection, so
the full fresh system is inconsistent.

## Singleton Cartier obstruction

The first emitted obstruction basis vector is the singleton determinant row

```text
row index 12 = [x^2 y^2].
```

Its entire 149-entry fresh row is zero modulo 3, while the right-hand side is
`2` (equivalently, the literal determinant coefficient divided by `3^11` is
`1` modulo 3).  Thus no simultaneous choice of fresh digits repairs this
row.

An independent source implementation does not consume the primary matrix or
Gaussian solver.  It rebuilds `[x^2 y^2]` from the literal `P,Q`, perturbs
each of the 146 P/Q coefficients by `3^11`, records the three H columns as
source-zero, and checks all 149 effects vanish modulo 3.  It also checks
`(3^11)^2=0 mod 3^12`, so cross-effects between fresh digits cannot evade the
linear certificate.  Independent result SHA-256 is
`f89426d35ff08561d14172b7b42203eb65e6b37402f6a39df37186ad1523cf72`.

## Custody and scope

The complete Box03 gate completed rc0 in 0.07s with maximum RSS 19,968 KiB.
Primary source SHA-256 is
`020ad0858e170c7b3e04242526106c9795c2abcf15cd7df9d28f32c2b1d7a8ed`;
result SHA-256 is
`9f4964a1a1f4250561e64869466d2c168969107814c5a7d759023fc20db9e1e4`;
the compressed full kernel/cokernel certificate is
`fad11a18d785c6520e477141f0f18094561a714cbc282e6ba9a5900e6d65a4e5`.
The independent r6d replay completed rc0 in 0.03s with maximum RSS 15,820
KiB.

This excludes only this one literal mod-`3^11` witness.  It does not exclude
the complete `3^150` family above the fixed mod-243 parent, the normalized
common-cubic locus, B9, an all-depth branch elsewhere, maximum twelve, a
counterexample, or JC2.  The next required gate is the exact scalar carry on
the entire finite family.
