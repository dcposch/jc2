# Result: H17 direct-unit relative cone V9

Date: 2026-08-26

Status: **PASS/PASS producer evidence**, internal normalized graph-support scope.

The exact sparse subtraction

```text
Hseries = G - 32 F
        = 2 E^2 P3 + 16 E P5 + 64 P7 - (E^3/2) P1
```

has 630 nonzero abstract monomials over `Q`.  Its independently generated
`F65521` support is identical and every coefficient is the reduction of the
exact rational coefficient.  The frozen exact support has SHA-256
`60658fb670ea1435e35655d86dc577472ab3213993461837819c1733a673c3df`.

On the H17 equality-wall valuation

```text
ord(lambda)=17,
ord(X)=ord(Y)=q,
ord(Ri)=ord(Si)=2q,
ord(a)=17-2q,
ord(K10)=ord(K6)=ord(K2)=42,
ord(J)=57,
```

all 630 affine weight functions were compared exactly.  Inside the mixed
domain `4<q<17/2`, the monomial

```text
-2 lambda^3 M^3 E^2
```

is uniquely least, at grade 51, exactly on

```text
17/4 < q < 7.
```

Thus, on the internal graph open where the displayed leading coefficients
are units, the coefficient of `Hseries` at grade 51 is a direct unit on this
open interval.  This is a producer-tier relative-cone certificate, not yet a
rational-regrading, literal source, or total-Rees coverage theorem.

The two boundary blocks are finite and explicit:

- At `q=17/4`, five complement terms of weight `34+4q` tie the intrinsic
  term, with coefficients `-9/4, 6, 6, 9/2, -12`.
- At `q=7`, three loaded `a^3` terms of weight `93-6q` tie it:
  `(155/16)K10*a^3*E^7 - 23K6*a^3*E^5 + 40K2*a^3*E^3`.

V7 selected the correct support, interval, and boundary monomials but printed
stale affine-line labels.  V8 repaired the loop and then failed closed on an
incorrect preregistered upper-label check.  V9 is the controlling replay.

Exact-Q lane: Box02 tag
`max12_812_order2_affine_faber_a_h17_direct_unit_cone_v9_20260826T195448Z_qcone`.
`F65521` lane: r6d tag
`max12_812_order2_affine_faber_a_h17_direct_unit_cone_v9_20260826T195448Z_pcone`.
Both validators passed in 0.06 seconds using at most 19 MiB and zero swap.

Explicit nonclaims: no boundary classification at `q=17/4` or `q=7`; no
claim for `q<=17/4` or `q>=7`; no factor-degenerate receiver; no literal
source/Cech/total-Rees exhaustiveness; no order-two, max12, or JC2 verdict.
