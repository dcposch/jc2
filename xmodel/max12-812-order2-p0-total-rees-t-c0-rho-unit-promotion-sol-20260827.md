# Promotion — actual-total `T-c0` rho-unit certificate and `T-c1` residual

Date: 2026-08-27

Status: **`T-c0` PROMOTED ON THE FULL REGISTERED CHART; `T-c1` RETAINED
ONLY AS A REVIEWED LOCALIZED PARTIAL WITH A CLOSED RESIDUAL.**

## Custody

- Producer identities:
  `xmodel/max12-812-order2-p0-total-rees-t-c0-c1-rho-unit-producer-sol-20260827.md`,
  SHA-256
  `6a29aac9506fba6ffd7f12a35efedb7501fb149d8f5d7c949740e8b1c2876da6`.
- Different-model hostile review and independent literal-source
  rederivation:
  `xmodel/max12-812-order2-p0-total-rees-t-c0-c1-rho-unit-review-fable5-20260827.md`,
  SHA-256
  `139ecb673995eff3c19f72da54b7a79d0a2a4c9c01f3b8600935f855704066fb`.
- Frozen exact-Q row hashes:
  `Tg10_2.poly` = `50c88196628dc04407c47c49059849f7f43265ade03afa13c9f27eecc1f928a6`,
  `Tg10_4.poly` = `6c33503e153a1adda56810a62db220f74b1dfd8c71158d1f3794f128773c503d`.

Fable5 reimplemented the corrected actual-total V0R1 source emitter without
importing a campaign compiler.  It reproduced all total and frozen
grade-10/11/12 exports for rows 2 and 4, including vanishing through grade
9, deck parity, specialization, and the independent `F_65521` encoding.
This discharges literal-source provenance for the two rows used here.

## Promoted `T-c0` theorem

On the standard Rees chart for `J1=(rs,cs,c0,c1)` with exceptional
coordinate `c0`, introduce the honest ratio `qc1` and bilinear
`c1-c0*qc1`.  The independently rederived row

```text
Tg10_4 = (3/32)c0^2 + (3/32)rho^2 c1^2
```

satisfies the exact polynomial identity

```text
3c0^2(1+rho^2 qc1^2)
 = 32*Tg10_4 - 3rho^2(c1+c0 qc1)(c1-c0 qc1).
```

The exceptional factor `c0^2` is absorbed by the reviewed
kernel-as-saturation presentation; `c0` is **not** treated as a unit.
Therefore `1+rho^2 qc1^2` belongs to the honest chart ideal and `rho` is a
unit on the full registered `T-c0` chart.  Its `rho=0` fibre is empty.
There is no ordered-stratum equation and no genuine localizer, including no
`D(k)` hypothesis.  This is stronger than the producer's mistyped argument.

## Reviewed `T-c1` partial and mandatory residual

On the ordered `T-c1` stratum `rs=cs=c0=0`, the exact identity is

```text
32*Tg10_2 = 3c1(c1+4rho^2 a1).
```

After one free exceptional-factor saturation step this gives
`c1+4rho^2 a1=0`.  It makes the further localization `D(c1)` rho-empty, but
it is not a whole-chart certificate because `a1/c1` is not a `J1` ratio
variable.  The closed locus

```text
V(c1) ∩ (ordered T-c1 stratum) ∩ V(rho)
```

remains an explicit stage-one on-chart obligation and is not covered by an
earlier standard chart.  The next bounded search may use the remaining
grade-10/11/12 rows, especially the `e`-jet terms in `Tg11_4`; it must seek
an exceptional-power certificate of the reviewed form, not invert `c1`.

## Firewall

This promotion closes only the registered actual-total `T-c0` chart and
banks the stated `T-c1` localized partial.  It does not close the whole
`T-c1` or `T-cs` chart, the second-stage `a0/a1` charts, source-localizer
complements, the terminal receiver, the generic deck/square bridge, order
two, maximum twelve, or JC2.  The displayed `Tg10_2` cofactor identity uses
`k`; the correct statement is that neither result localizes at `k`.
