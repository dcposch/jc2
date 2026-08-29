# Hostile review: `(8,12)` order-two discriminant half-weight K2 support

Date: 2026-08-26

## Verdict

**REPAIR — analytic K2 theorem otherwise confirmed on its stated open
charts; no source promotion.**

The frozen target is
`xmodel/max12-812-order2-discriminant-halfweight-k2-support-theorem-20260826.md`,
SHA-256
`20fa404c10c6fdafe59247967db8234f3479ae9a06740b521650b8a8aa88e341`.

The required repair is confined to the source firewall at target lines
171--175 and to making the ambient localization in (2.1)--(2.3) explicit.
It does not alter the analytic five-row K2 calculation, its exact-Q support,
or the required retention of the raw nonreduced scheme.  It expressly does
not promote any statement to the frozen full source.

## Custody and exact endpoints

All four charged input/result hashes recompute.  `FREEZE.sha256` and
`RESULTS.sha256` for
`cases/max12_812_order2_disc_halfweight_support_v2_20260826` verify every
listed file.  The exact-Q stdout is the charged
`7de0a587270481736b0b85b76cffce761567d7778d014cc0ddd4cd557ed0cb26`;
the characteristic-32003 stdout is the charged
`9dca3aaaaa628083f60c553823f67d9decfc4664e588828ffdb27be11f72336d`.
Both print the unique pass endpoint and the expected two containment
sentinels.

The exact-Q run prints, after the `m` saturation,

```text
K_NONZERO_UNIT=1
K0_E_NONZERO_UNIT=1
TRIPLE_OPEN_BASIS =
  k, e, 6*b*y^2+m^3+12*h*y, b*m^3-6*h^2,
  m^6+12*h*y*m^3+36*h^2*y^2
TRIPLE_RADICAL_BASIS = k, e, b*y+h, m^3+6*h*y
RADICAL_IN_EXPECTED=1
EXPECTED_IN_RADICAL=1
```

The good-prime stdout reproduces the same dimensions, unit outcomes, raw
basis shape, radical shape, and containments.  I use the characteristic-zero
endpoint for the characteristic-zero assertions; the prime lane is an
independent control, not a replacement for it.

## Formula and chart audit

There is no indexing or scalar mismatch in (1.1).  In the frozen exact-Q
client, the one-indexed storage has `u[3]=u_2=y^2`,
`u[4]=u_3=-2hy-bu_2`, and `c[14]=c_13`.  Its first generated row is therefore
exactly `6*u_3-m^3+16*kappa*c_13`; the next four are
`6*u_n+16*kappa*c_(10+n)` for `n=4,...,7`.  This also checks the displayed
`6` and `16` scalars, rather than merely the final radical.

The `m` localization is licensed.  Under the charged discriminant
parametrization, `n_3=m` while every normal coefficient is a multiple of
`m`, and `k10=0`.  The pullback of the first-contact ideal
`(n0,n1,n2,n3,k10)` is consequently `(m)`.  Thus its contact-one open is
precisely `D(m)`, not an inferred generic restriction.

Scheme-theoretic elimination of the first two complementary rows is also
legitimate on this open.  From the charged Kuranishi expression, the
negative `A^-1,A^-2` coefficients are triangular in the two complementary
constants, with diagonal coefficients a nonzero rational multiple of `m`
and a nonzero rational multiple of `m^2`.  They are units in `R_m`, so the
quotient by those rows is an actual substitution isomorphism over `R_m`, not
only a pointwise solve.  The remaining five rows are exactly the checked
ideal above.

For the raw scheme, put `F=V+6*y*U`.  The last three exact-Q basis elements
are

```text
F,  b*F-6*U^2,  V^2.
```

They generate `(F,U^2)`: the second yields `U^2`, while
`V=F-6*y*U` makes `V^2` belong to `(F,U^2)`.  Conversely the displayed three
elements belong to `(F,U^2)`.  Hence (2.3) holds on the stated localized
chart, and its radical is `(kappa,e,U,V)`.  The square-zero `U` direction is
real; the target correctly forbids replacing it by the radical before the
K3 conormal/kernel computation.  It does not falsely claim that that
conormal computation has already been done.

The `b=0` routing is also correct: `b=4a` and `e=d+3a^2` give
`b=e=0 => a=d=0`, hence `Q=A^2` and `K0=A^4`.  The theorem omits and routes
this square-intersection stratum; it does not call it empty.

## Required repair: source firewall and localization notation

The smallest failing assertion is target lines 173--175:

```text
Its two modular controls verify equality ...
```

The named V2 package is present and its freeze hash does equal the target's
`bbaa31fa...`, but its own `REGISTRATION.md` says
`PREREGISTERED IMMUTABLE V2; NO RESULT`.  It contains no run directory,
stdout, validation, `RESULT.md`, or `RESULTS.sha256`; its two modular lanes
and exact-Q lane are registered, not completed.  Therefore the word
`verify` cannot describe an obtained V2 result.  This is a source-firewall
defect, even though the surrounding sentences correctly withhold exact-Q
promotion.

Replace that sentence with language such as: “Its two registered modular
control lanes and exact-Q promotion lane are designed to test equality
between the seven pulled-back source rows and the seven analytic K2 rows,
and the ordinary matched unit endpoint; no V2 equality result is asserted
here.”  Retain the existing prohibition on source promotion until a frozen,
fail-closed exact-Q V2 endpoint exists.

For exact scheme language, also declare `R_m=Q[b,e,h,y,kappa,m]_m` before
(2.1), and read all three chart claims in that ring (with the further `b`
localization for (2.3)).  The client computes the `kappa=0`/`e!=0` check by
saturating `G+(kappa)` by `m` and then `e`, which is exactly the desired
empty chart after localizing at `m`; stating the ring removes any apparent
claim that adjoining `kappa` commutes with a contraction-level `m`
saturation in the unlocalized polynomial ring.

## Exact confirmed scope

Subject to those wording repairs, the result confirmed here is only the
analytic seven-row half-weight K2 initial-obstruction theorem on `D(m)`,
with the triple-root raw scheme and reduced support on `D(b*m)`.  It does
not cover `m=0` or the routed `b=0` square intersection; it constructs no
K3 lift and supplies no order-two, terminal, Taylor, `(8,12)`, maximum, or
JC2 verdict.  In particular, while the full-source exact-Q V2 endpoint is
pending, none of (2.1)--(2.5) is promoted to a theorem about every frozen
source component.
