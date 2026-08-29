# Producer result: vertical `c=3,r>=2` thin divisibility gate

Date: 2026-08-26

Status: **DUAL-AWS PRODUCER PASS; HOSTILE REVIEW REQUIRED BEFORE PROMOTION.**

## Endpoint

The frozen compiler and fail-closed validator passed independently over
exact Q and `F_65521`.  Both engines returned `rc=0`; both validators printed
`PASS_SQUARE_C3_VERTICAL_THIN`.  Exact-Q stdout SHA is
`af96bae652206831e66737c63c490f036fdea962c22c618467a5d04096dac62c`;
the modular stdout SHA is
`feba24463e9443631b4d008cc6ed4819835457bc5b2d179ca1987b97ac529186`.

Every required sentinel passed:

- all seven complete source rows and grade-13--15 quotient identities;
- exact lower-unitriangular source/Faber-to-Laurent row identities;
- the common-numerator bridge to the displayed `H13,H14,H15` formulas;
- both etale/deck root allocations;
- `D2`: `L^2 H14 = -(3/8)B2 A0^2 (mod L)`;
- the `r=2` complementary-factor constraint on `B2`;
- `D4`: `L^3 H15 = -(1/16)A0^3 (mod v)` after that constraint;
- symbolic independence from `B3`, so the same contradiction covers all
  `r>=3` without sampling;
- omitted-connection and wrong-cubic-coefficient negative controls.

The exact-Q compiled input SHA is
`ca1f0692893ba485e2407a6c3a49a397422abb075f97467da0923fdd4b682d29`;
the `F_65521` input SHA is
`5b2a7a24ae0fea5fb016e603804779f985672f2556fdd40ec6ffa118d152cadf`.
Frozen source manifest SHA is
`a13d10fb845c1b5cafe249eb700af2e8dd49f3d847c9092478c7f121306fda24`.

## Producer theorem, pending review

Assume the reviewed generic-square first-normal setup and work on
`D(p*k0)`.  A finite-order arc whose leading `A` direction is nonzero and
normalized to order zero cannot have `ord(C)=3` and `ord(R)>=2`.

Indeed grade 13 gives `L|A0 E3`, so over the faithfully flat etale splitting
algebra `L=uv`, and, up to deck exchange, `A0=alpha*u`, `E3=gamma*v` with
`alpha*gamma!=0`.  Grade 14 gives
`L^2 H14=-(3/8)B2 A0^2 (mod L)`, hence at the complementary root `v=0`
the `r=2` branch forces `v|B2`; for `r>=3`, `B2=0` already.  Grade 15 then
gives `L^3 H15=-(1/16)A0^3 (mod v)`, nonzero on this chart, contradicting
polynomiality.  The exact source bridge identifies these rational
coefficients with the seven necessary tail rows.

## Firewall

This is a producer-tier elimination only of vertical
`a=0,c=3,r>=2` faces on `D(p*k0)`.  It does not address `r=1`, horizontal
`a>0`, `p=0`, `k0=0`, ramified slopes, zero/infinity supports, the whole
square stratum, exact order two, maximum twelve, or JC2.  The modular run is
a software control, not a characteristic-zero proof.

The duplicate remote source trees created during evidence retrieval were
moved intact to `/tmp/max12_812_c3_{q,f}_retrieved_source_20260826T1018Z`;
the canonical frozen source and complete run evidence remain in this case.
