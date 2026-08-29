# Promotion: order-two generic-square vertical `c=3,r>=2` gate

Date: 2026-08-26

Status: **HOSTILE-REVIEW CONFIRMED; NARROW ARCWISE THEOREM.**

## Promoted statement

In the reviewed generic-square first-normal setup, work on the principal open
`D(p*k0)`.  Let a finite-order arc have nonzero leading `A` direction,
normalized by `ord_sigma(A)=0`.  Then the valuation face

```text
ord_sigma(C)=3,    ord_sigma(R)>=2
```

is empty.

The seven complete source/Faber rows through absolute grades 13--15 are an
invertible lower-unitriangular transform of the rational negative-tail rows.
Grade 13 gives `L | A0*E3`.  After the faithfully flat etale splitting
`L=u*v`, root allocation gives, up to deck exchange,
`A0=alpha*u`, `E3=gamma*v`, with `alpha*gamma != 0`.  The exact grade-14
identity

```text
L^2*H14 = -(3/8)*B2*A0^2  (mod L)
```

forces the complementary factor `v | B2` in the `ord(R)=2` case; for
`ord(R)>=3`, `B2=0` already.  The complete grade-15 identity then gives

```text
L^3*H15 = -(1/16)*A0^3  (mod v),
```

which is nonzero on the allocated chart and contradicts polynomiality.  The
deck-conjugate chart gives the same contradiction.  Symbolic independence
from the next `R` coefficient makes the argument uniform for every
`ord(R)>=3`, not a finite sampling assertion.

## Evidence and custody

- producer:
  `cases/max12_812_order2_square_owner_c3_vertical_thin_20260826/RESULT.md`,
  SHA-256
  `c03ad20443cc24c1346e779d98172583bb9193beb89826d327e85f203d574557`;
- producer evidence manifest SHA-256
  `cb474217cfaef16773d296318973833edbbc133d4930bb74695f233719674551`;
- frozen source manifest SHA-256
  `a13d10fb845c1b5cafe249eb700af2e8dd49f3d847c9092478c7f121306fda24`;
- exact-Q compiled input/stdout SHAs
  `ca1f0692893ba485e2407a6c3a49a397422abb075f97467da0923fdd4b682d29`
  / `af96bae652206831e66737c63c490f036fdea962c22c618467a5d04096dac62c`;
- independent `F_65521` compiled input/stdout SHAs
  `5b2a7a24ae0fea5fb016e603804779f985672f2556fdd40ec6ffa118d152cadf`
  / `feba24463e9443631b4d008cc6ed4819835457bc5b2d179ca1987b97ac529186`;
- hostile review:
  `xmodel/max12-812-order2-square-c3-vertical-thin-review-grok-20260826.md`,
  SHA-256
  `af10cf34c147b8321fad49d32a84ebf224e1e8f42f70df3dd27256cd20c223a4`,
  verdict `ORDER2_SQUARE_C3_VERTICAL_CONFIRMED`.

Both AWS engines returned `rc=0` and both fail-closed validators printed
`PASS_SQUARE_C3_VERTICAL_THIN`.  Exact Q carries the characteristic-zero
claim; the finite-field run is an independent software control.

## Firewall

This is an arcwise/set-theoretic exclusion only for the vertical face
`a=0,c=3,r>=2` on `D(p*k0)`.  It does not give scheme structure.  It does not
cover `r=1`, horizontal `a>0`, `p=0`, `k0=0`, ramified slopes,
zero/infinity supports, fan exhaustiveness, the whole square stratum, exact
order two, maximum twelve, or JC2.
