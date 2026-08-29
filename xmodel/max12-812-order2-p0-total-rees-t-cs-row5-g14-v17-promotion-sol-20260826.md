# Promotion: actual-total row-5 grade-14 coefficient export V17

Date: 2026-08-26

Status: **PROMOTED AS A SOURCE-COEFFICIENT LEMMA.**

## Result

For the frozen 89-tail fifth Faber row evaluated on the literal total source

```text
p=-2*rho^2 + sum_{i=1..14} 2*ell_i*sigma^i
```

with all correction and load series live through the registered ceiling, the
grade-10, grade-11, and grade-12 coefficients agree exactly with the frozen V9
exports.  The grade-14 coefficient is the frozen 304-monomial, nonzero,
rho-even polynomial with exact-Q SHA-256
`91d96924696ab19a59cd8661fdd778559ce8dc9c1bc0fbc886dbdf4956e838f7`.
Its odd-sheet specialization is exactly

```text
-(21/320)*b^5*w^2,
```

and changing the load normalization from `12/5` to `11/5` changes the value
to `-(41/640)*b^5*w^2`.

## Evidence and review

- exact-Q result SHA-256: `25d40556618983a350eda99d4fb6aae8d1e5cd2cf328041963b46d61729af543`;
- F65521 result SHA-256: `5ec8fece264a6076c5536f3c2cbb7d9d8f485316036e7e10adf0a7209e2ce166`;
- F65521 polynomial SHA-256: `760d4f3b155decdf0e847a587254ae701f2b5948d8dd6135c52f5f213c10835b`;
- Fable5 hostile-review SHA-256: `b454085829fb2cbcad921749bb3dcd8f0846482d916e19c74bdd242dde3f0dc9`, verdict `CONFIRMED`;
- Opus5 hostile-review SHA-256: `f0d8a9cdabc161e2e462646d94c340d9ce896eda39819b1a749d33632dfe6fae`, verdict `CONFIRMED`.

Both reviewers independently reimplemented the sparse exact arithmetic from
the frozen source specification and reproduced the exported bytes.  The
F65521 lane is an encoding/software control only.  The known V8/V9 doubled-
`TPhi` rebuild occurs after the exported coefficients and cannot affect them.

## Scope and audit note

This promotes one source-honest coefficient export and its low-grade bridge.
It does not by itself form a Rees chart, make an ideal a unit, prove rho a
unit, close Gate T, order two, maximum twelve, or JC2.  The upstream source
specification remains an explicit dependency.

Both reviewers also found a display-only V9 telemetry defect: a leading minus
sign is counted as a term separator.  The coefficient files and all algebraic
identities are unaffected; the controlling correction is recorded in
`max12-812-order2-p0-total-rees-v9-term-telemetry-erratum-sol-20260826.md`.
