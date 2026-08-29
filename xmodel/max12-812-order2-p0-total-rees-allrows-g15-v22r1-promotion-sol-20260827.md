# Promotion: actual-total all-row grade-15 export V22R1

Date: 2026-08-27

Lifecycle: **PROMOTED WITH EVIDENCE REPAIRS.**

Producer report:

```text
xmodel/max12-812-order2-p0-total-rees-allrows-g15-export-v22r1-producer-sol-20260827.md
SHA-256 199254792a117f4ab6ae02d02fd652a0227ada6576b5c1d1ed3310cd89c6d287
```

Different-model hostile review:

```text
xmodel/max12-812-order2-p0-total-rees-allrows-g15-v22r1-hostile-review-grok-20260827.md
SHA-256 f49329ceeffe20cea673a927afae5b4b7bfeac56b8d2a17abaefc09603eda80b
Verdict CONFIRMED WITH REPAIRS
```

Evidence erratum:

```text
cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/POST_REVIEW_ERRATUM.md
```

## Promoted statement

Let the frozen seven-row actual-total source be the reviewed 569-entry tail
table and V20 generic moving-p emitter, with the sparse cutoff raised to 15
before construction and the preregistered head lists extended through that
cutoff.  Then all source coefficients below grade 10 vanish, the coefficients
at grades 10--14 are exactly the reviewed V9/V20 exports, and the seven
grade-15 coefficients are the harvested exact-Q polynomials with term counts

```text
133,224,355,140,585,200,759.
```

All seven grade-15 polynomials are nonzero, rho-even, and sigma-homogeneous of
weight 15.  No exact-Q coefficient vanishes modulo 65521, and coefficientwise
reduction reproduces each F65521 serialization exactly.  A clean-room
reimplementation reproduced all fourteen serialized files byte-for-byte and
all 35 historical grade-10--14 bridges as exact polynomial identities.

On the named rho-free point sections, all grade-10--14 rows vanish.  At grade
15:

```text
CS0 = Z00 = 0;
A00: row 6 = -1/16, all other rows = 0;
A10: row 3 = -1/16, row 5 = -(3/32)rho^2,
     row 7 = -(3/128)rho^4, all other rows = 0.
```

These values agree with the separately promoted all-depth V21 section theorem.

## Repairs incorporated

The promotion treats the two AWS lanes as custody executions of one exact-Q
reconstruction, not as two independent algebraic derivations.  It does not
use the unharvested V1 failure trees, overstate the sensitivity mutation, or
treat the homogeneous CS0/Z00 zeros as discriminating grade-15 controls.  The
latent modular term-count defect is recorded and untriggered.  Full details are
in the adjacent post-review erratum and the hostile review.

## Scope

This promotes literal finite-source coefficient exports and the stated named
section evaluations.  It does not prove either J2 chart empty, supply an
unwritten Rees relation, construct or exclude a formal arc, or establish Gate
T, order two, maximum twelve, or JC2.  V23 and every certificate search based
on these rows remain downstream design work rather than consequences of this
promotion.
