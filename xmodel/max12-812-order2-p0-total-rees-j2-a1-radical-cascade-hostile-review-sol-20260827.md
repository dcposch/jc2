# Hostile review of Opus5 ordered-`T-a1` radical cascade

Date: 2026-08-27  
Reviewer: Sol (different model from the Opus5 producer)  
Verdict: **CONFIRMED WITH SCOPE CORRECTION**

## Exact replay

The reviewer independently parsed the 70 hash-pinned frozen ordered-`a1`,
`rho=0` row files and checked fifteen coefficientwise polynomial identities
covering every displayed step of Opus5's cascade, including the terminal
`Tg16_5` contradiction and both A2 relations.

Producer report:

```text
0fbb452456a34b24b28b35a9fd0f99fc6ac86f81edab7a704369aeba0b7881da
  xmodel/ideation-20260827T0635Z-opus5.md
```

Replay:

```text
e82811f46d8dac635201935b34748d4ffc278010c3256feb1207216711a3f009
  cases/max12_812_order2_p0_total_rees_j2_a1_radical_cascade_review_v41_20260827/replay_cascade_review.py
ba034c8cebaa27c5630872b9cf06d152e4577170486ac34ad7f695ead871845b
  cases/max12_812_order2_p0_total_rees_j2_a1_graded_ladder_v37_20260827/solve_graded_ladder_v37.py
```

```sh
python3 cases/max12_812_order2_p0_total_rees_j2_a1_radical_cascade_review_v41_20260827/replay_cascade_review.py
```

The exact identities confirm the following field-point argument over any
field of characteristic not `2,3,5`, on `rho=0,D(a1)`:

1. `Tg11_1=(3/8)a1*e0`, so `e0=0`.
2. `Tg12_2=(3/32)e1(e1-4a1*ell1)`.  The second branch, together with
   `Tg12_1`, gives `ee0=-4aa0*ell1`; then
   `Tg13_4=-(3/2)a1^2*ell1^3`, so it collapses to `ell1=e1=ee0=0`.
   The first branch gives `e1=ee0=0` directly.
3. With `e0=e1=ee0=0`, the reviewed identities give
   `ell1*rs1=0` and `aa0*rs1=2a1*cs1*ell1`.
4. On `D(ell1)`, the exact sequence
   `rs1=cs1=ee1=ec3=rs2=ez3=0`, `ec4=a1*cs2`,
   `a1=6cs2*ell1`, and
   `Tg16_5=(27/2)cs2^3*ell1^4` forces `cs2=0`, hence `a1=0`, a
   contradiction.  Thus `ell1=0` at every such field point.
5. Therefore `aa0*rs1=0`.  On the `D(rs1)` branch, exact factors in
   `Tg13_2` and `Tg15_4` give
   `aa0=0`, `k*rs1^2=(96/5)a1^2`, and `ee1=a1*ell2`.

No algebraic error or hidden division was found.  The divisions are exactly
by the displayed opens `a1`, then `ell1` in the branch being contradicted,
and `rs1` in A2, together with the characteristic exclusions.

## Correct scope

The confirmed conclusion is a **radical/field-point reduction of the frozen
raw `rho=0` rows through grade 16**:

```text
e0=e1=ee0=ell1=0,  aa0*rs1=0,
```

with the A2 relations above.  It is chart-wide only in the narrow sense that
it did not assume V32's six-coordinate support.  It is not:

- a polynomial ideal-membership certificate or a nilpotence exponent;
- a statement about the unspecialized `rho` family;
- closure of either A1 or A2;
- an honest saturated-Rees/base-change or Gate-T result.

The result is fully compatible with the exact rank-two first-occurrence
symbol theorem: both begin with the ideal identity `a1*e0=0`; the cascade
reduces old-variable field points, while the symbol theorem describes the
five later compatibility rows.  V36 remains only the death of one ansatz
inside A1.

## Disclosure

The reviewer read the Opus5 report, the V37 loader, and frozen row corpus;
ran only desk-scale exact `Fraction` polynomial arithmetic; used no CAS, AWS,
network, or `jc2-lean`; and wrote only the replay script and this report.
