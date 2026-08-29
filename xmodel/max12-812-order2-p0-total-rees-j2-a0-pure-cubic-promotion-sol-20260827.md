# Promotion — pure cubic closes the registered `T-a0` chart

Date: 2026-08-27

## Verdict

**PROMOTED at the literal registered actual-total source/chart tier.**  In the
V23R1 `T-a0` chart over `V(J1)`, the pure exceptional power `a0^3` lies in the
ideal of thirteen frozen source rows.  Therefore saturation by the exceptional
coordinate makes the chart ideal the unit ideal.  The whole registered
`T-a0` chart is empty; there is no `rho=0` restriction and no residual
localizer stratum.

Evidence:

```text
Fable5 producer / discovery   0a7e904b484bd08414573d3f22ec2080d327625916fd589a243b1b483586f4e2
Grok hostile review           c6bb46ae51f7ce2a4f4adc61f0a818f1e5bc46512f0718d025923057b93b5b09
Opus5 independent review      1ddb4fcb583440c07abc2a4cf1872ecb4f10a0a071d98c1d175bb113d7739f6d
V23R1 result                  ce4d0adbbe94e1337bed5047da0417e3b17cb86530715fb62316086cabd14641
```

Grok independently reparsed and rehashed all charged bytes, replayed the
identity exactly over `Q` and coefficientwise over `F_65521`, checked every
cofactor's complementary sigma weight, and ran deletion/mutation controls.
Opus5 independently regenerated both charts from the unspecialized rows,
confirmed the six-row identity and the stronger pure-power identity, and
audited the chart typing.  Root separately replayed the displayed thirteen-row
combination by an exact sparse expansion with zero residual.

## Exact identity

In the ordinary polynomial ring of the specialized chart
`J1=(rs,cs,c0,c1)=0`, `a1=a0*qa1`, one has

```text
a0^3
 = (6*cs1*ell1 + (9/4)*cs1*ell1*qa1^2*rho^2
    -3*cs2*qa1^2*rho^4 - 8*cs2*rho^2
    +(27/2)*ell1*ell3*qa1*rho^2 +(27/4)*ell2^2*qa1*rho^2
    -9*ell4*qa1*rho^4 +(27/8)*qa1*rho^2*rs2) * Tg11_1
   +(9*cs2*qa1*rho^2 -(3/4)*qa1^2*rho^2*rs2 -2*rs2) * Tg11_2
   +(-(9/4)*cs1*qa1^2*rho^4 -6*cs1*rho^2
     +(27/2)*ell1*ell2*qa1*rho^2 -(27/2)*ell3*qa1*rho^4
     +(27/8)*qa1*rho^2*rs1) * Tg12_1
   +(9*cs1*qa1*rho^2 -(3/4)*qa1^2*rho^2*rs1 -2*rs1) * Tg12_2
   +(-4*cs1 -(3/2)*cs1*qa1^2*rho^2 +9*ell3*qa1*rho^2) * Tg12_3
   +((27/4)*ell1^2*qa1*rho^2 -(27/2)*ell2*qa1*rho^4) * Tg13_1
   +(9*ell2*qa1*rho^2) * Tg13_3
   -((27/2)*ell1*qa1*rho^4) * Tg14_1
   +(9*ell1*qa1*rho^2) * Tg14_3
   +((27/4)*qa1*rho^6) * Tg15_1
   -(9*qa1*rho^4) * Tg15_3
   +(18*qa1*rho^2) * Tg15_5
   +(-16 - 6*qa1^2*rho^2) * Tg15_6.
```

The residual is the zero polynomial.  All cofactors are polynomials; none
inverts `a0`, `qa1`, `rho`, `k`, or a jet, and no divided row is used.  Every
term has sigma weight 15.  In staged-certificate notation the type is

```text
f=a0, N=3, genuine localizer s=1, rho-unit factor 1+rho*W=1 (W=0).
```

Thus `a0^3 in I`, so `1 in (I:a0^infinity)`.  Adding later registered source
rows only enlarges `I`; the conclusion persists beyond the grade-15 prefix.

## Evidence repairs and exclusions

- The chart has 31 nonzero specialized row files.  Three are exact even-`rho`
  multiples of `Tg11_1`, leaving 28 independent generators of the same ideal.
  The producer's phrase “28 nonzero rows” is repaired accordingly.
- The earlier six-row identity
  `a0^3*(1+3*qa1^2*rho^2) in I` is also exact, but its parenthesized factor is
  the permitted `1+rho*W`, not a genuine localizer.  The pure identity above
  is strictly stronger and has `W=0`.
- V24's rational-function lift is not evidence for this promotion: it was
  computed over `Q(qa1,rho)`, clears a pure power of `rho`, and its bounded
  basis emitted warnings.  The displayed denominator-free identity and the
  independent byte-level replays carry the theorem.
- Ordered `T-a1` is a different chart.  Its primary cubic certificate shape is
  obstructed, but the chart is not closed by this result.

## Scope firewall

This promotion closes one second-stage node of the registered staged landing
tree.  It does not close ordered `T-a1`, `V(J1+J2)`, the off-family load fan,
the deck/square bridge, Gate T, all order-two types, maximum twelve, or JC2.
