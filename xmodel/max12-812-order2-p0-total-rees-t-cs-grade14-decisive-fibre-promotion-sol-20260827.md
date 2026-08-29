# Promotion — grade 14 is decisive on the registered `T-cs` special fibre

Date: 2026-08-27

Status: **PROMOTED AT THE FROZEN LOCALIZED SPECIAL-FIBRE SCOPE ONLY.**

## Custody

- Producer / exact witness (Opus5):
  `xmodel/max12-812-order2-p0-total-rees-t-cs-drop-g14-witness-opus5-20260827.md`,
  SHA-256
  `d9e5f43954240eee13311c5f386231f9ed506c4bbe978211cdfa711e3e8c86d9`.
- Different-model hostile review (Grok 4.6):
  `xmodel/max12-812-order2-p0-total-rees-t-cs-drop-g14-witness-hostile-review-grok-20260827.md`,
  SHA-256
  `7fbd9423b6840e4f3017687897e0dad373a04d2683589ccb432682553053c3cf`.
- Stopped-engine custody note:
  `cases/max12_812_order2_p0_total_rees_t_cs_rho_unit_v18_20260826/ABORTED_V18R1_NEGATIVE_CONTROL_SUPERSEDED_20260827.md`,
  SHA-256
  `0708935c2cf4b27914f02d1bd05295cba0ac8aca49f24d1158397aa3a72dfc3d`.

The reviewer independently parsed the frozen raw V9/V17 polynomials,
applied the compiler chart map monomial by monomial, recovered all 42 ring
variables, and checked exact rational and coefficientwise F65521 identities.
No Groebner basis or AWS output is load-bearing.

## Exact negative-control witness

After the literal `T-cs` substitution

```text
rs=cs*qrs,  c0=cs*qc0,  c1=cs*qc1,
```

assign every compiler-ring variable zero except

```text
cs=1,  e1=1,  k=12/5,  u=1,  v=5/12.
```

All 21 grade-10--12 rows and
`qrs,rho,1-u*cs,1-v*k` vanish exactly, while

```text
Tg14_5 = -21/320 != 0.
```

Consequently the frozen drop-grade-14 ideal is proper over `Q`.  The same
point reduces to the registered F65521 lane, where the omitted row is
`20680`.  This replaces the term-order-dependent V18R1 negative-control
computation mathematically; it does not turn either aborted engine into a
validator PASS.

## Complete prefix fibre and decisive row

On `qrs=rho=0` and `D(cs*k)`, the grade-10--12 equations force

```text
qc0=qc1=e0=a0=ell1=0.
```

Nineteen rows then vanish identically.  The two survivors are

```text
12e1^2 = 5cs^4 k
```

and one equation linear in `ell2` with unit coefficient
`-(5/16)cs^3 k`.  The remaining 29 variables are free, so this prefix fibre
is an irreducible rational 31-dimensional variety.  On it,

```text
Tg14_5 = -(21/320)cs*e1^2 = -(7/256)cs^5*k,
```

which never vanishes on `D(cs*k)`.  Hence the frozen grade-10--12 plus
grade-14 localized special-fibre ideal is the unit ideal over `Q`; this is a
Nullstellensatz/faithful-flatness conclusion and supplies no explicit
cofactors.

## Operational consequence

After confirming that both V18R1 stdout files had already printed the
provisional positive token, the coordinator terminated only their two
negative-control process trees at `2026-08-27T01:09Z`.  Remote partial logs
remain preserved and are explicitly not PASS artifacts.  V19 continues
independently because its exact 26-generator cofactor lift is not supplied
by this theorem.

## Firewall

This promotion is conditional on the frozen V9/V17 row bytes and retains
their upstream literal-source provenance debts.  It proves the registered
localized **special-fibre** statement on `D(cs*k)`.  It does not by itself
produce a direct total-family certificate of the staged rho-unit form:
after V19 returns, its inverse-variable cofactors must be cleared and checked
for the required exceptional-power/genuine-localizer/rho-cofactor typing.
Absent that check, no special-fibre base-change equality or positive-rho DVR
exclusion may be inferred.  Nothing here closes the full `T-cs` chart,
`k=0`, later charts, the terminal receiver, Gate T, order two, maximum
twelve, or JC2.
