# Actual-total `T-c0` and `T-c1` rho-unit certificates

Date: 2026-08-27

Status: **PRODUCER-EXACT CANDIDATE, AWAITING DIFFERENT-MODEL SOURCE-PROVENANCE
REVIEW.**  This note proves two polynomial identities from hash-pinned V9
exports.  It does not by itself discharge the exports' upstream literal-source
provenance dependency.

## Frozen input

The exact characteristic-zero grade-10 exports are in

```text
86c535a370adc2c7fb31b6ec8454128d765f581200a1730c506306d8bfa63c0e
  cases/max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_20260826/aws_q_v9/COEFFICIENTS.json

50c88196628dc04407c47c49059849f7f43265ade03afa13c9f27eecc1f928a6
  .../compiled/Tg10_2.poly

6c33503e153a1adda56810a62db220f74b1dfd8c71158d1f3794f128773c503d
  .../compiled/Tg10_4.poly
```

They read

```text
Tg10_2 = (15/64) rho^2 cs^2 rs k
        +(3/8) rho^2 a1 c1
        +(5/1024) rs^3 k
        +(3/32) c1^2
        +(3/8) a0 c0,

Tg10_4 = (3/32) rho^2 c1^2 +(3/32) c0^2.
```

The independently compiled `F_65521` manifest and corresponding two-row
hashes are `dc775709...`, `491dec9e...`, and `75330c39...`.  They are an
encoding control; the displayed rational identities are the theorem
candidates.

## `T-c0`

On the `J1=(rs,cs,c0,c1)` standard chart `D_+(c0)` use

```text
rs=c0*qrs,  cs=c0*qcs,  c1=c0*qc1.
```

The ordered complement of the earlier `rs` and `cs` charts sets
`qrs=qcs=0`.  The fourth row gives the global identity

```text
3*c0^2 = 32*Tg10_4 - 3*rho^2*c1^2.                 (1)
```

Thus `3*c0^2` belongs to `(Tg10_4,rho)` already in the unspecialized total
chart.  Since `c0` is inverted on this chart, (1) makes its `rho=0` fibre
empty.  Equivalently,

```text
(32/(3*c0^2))*Tg10_4 = 1 + rho^2*qc1^2.
```

No radical, normalization, special-fibre base-change equality, or overlap
calculation enters this implication.

## `T-c1`

On `D_+(c1)`, after the ordered closed complement `rs=cs=c0=0`, the second
row gives

```text
3*c1^2 = 32*Tg10_2 - 12*rho^2*a1*c1              (2)
```

in that quotient.  Before taking the quotient, the exact identity is

```text
3*c1^2 = 32*Tg10_2
          - 12*rho^2*a1*c1
          - (15/2)*rho^2*cs^2*rs*k
          - (5/32)*rs^3*k
          - 12*a0*c0.                              (3)
```

Consequently `3*c1^2` belongs to
`(Tg10_2,rho,rs,cs,c0)`.  Localizing at `c1` makes the ordered `rho=0`
fibre empty.  Equivalently in the localized ordered chart,

```text
(32/(3*c1^2))*Tg10_2 = 1 + 4*rho^2*(a1/c1).
```

The occurrence of `a1/c1` is harmless: it is an element of the localization
at `c1`; no claim treats it as a `J1` ratio variable.

## Exact consequence and remaining debt

Conditional only on literal-source provenance for the two exported rows,
(1)--(3) are direct total-family rho-unit certificates for the ordered
`T-c0` and `T-c1` charts on the campaign's existing `D(k)` source stratum.
They are stable under adjoining every later source equation.  The coefficient
`k` is not used by the identities, but this note does not enlarge the source
family beyond its registered `D(k)` scope.

The clean hostile-review discriminator is a source-only rederivation of
`Tg10_2` and `Tg10_4` from the frozen V0R1 emitter, followed by exact expansion
of (1) and (3).  No Groebner basis or AWS algebra is needed.

This note does not settle the pending `T-cs` control/certificate, the
second-stage `a0,a1` charts on `V(J1)`, the terminal `V(J1+J2)` receiver,
closed localizer strata such as `k=0`, the generic deck/square bridge, order
two, maximum twelve, or JC2.
