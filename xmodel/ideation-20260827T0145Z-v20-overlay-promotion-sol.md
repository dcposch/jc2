# Promotion: reviewed V20 overlay corrections and grade-13 routing

Date: 2026-08-27

Lifecycle: **PROMOTED AT THE EXACT SCOPES BELOW.**

Primary alternate adjudication and different-model hostile review:

```text
xmodel/ideation-20260827T0145Z-crosspollination-hostile-review-fable5.md
SHA-256 1481d3cadc30ee024c7d4e07e746a6e15ce000a52358e589a1fdf5add3e755c1

xmodel/ideation-20260827T0145Z-v20-overlay-hostile-review-opus5.md
SHA-256 d73eeb59958fea0a3db3c2046e2b0cdb87604e94f35dda5b8404d7b9fcf1bd91
Verdict: no load-bearing overlay claim falls; corrections below confirmed.
```

The underlying V20 grade-13/14 bytes are independently promoted in
`max12-812-order2-p0-total-rees-allrows-g13-g14-v20-promotion-sol-20260827.md`.

## 1. Grade-13 delayed-load kill

Over `Z[1/2]`, the literal 32-term row and the grade-11 row satisfy the exact
27-term membership

```text
Tg13_6 + (1/2)*cs*rho^2*Tg11_1
        - (35/128)*cs^4*k1*rho^4  in  (k,rs,c0,c1).
```

Let `F` be a field of characteristic outside `{2,3,5,7}`.  On the honest
ordered `T-cs` stratum, `qrs=0` is a chart generator and hence `rs=0`.
At a point with `k=0`, vanishing of `Tg10_1..Tg10_4` forces
`c0=c1=0` set-theoretically.  Vanishing also of `Tg11_1,Tg13_6` then forces

```text
cs^4*k1*rho^4 = 0.
```

Consequently
`V(k) intersect D(cs*k1*rho)` is empty in this ordered 36-row stratum.  The
conclusion is set-theoretic: the `c0,c1` step is radical-only and supplies no
direct certificate or cofactors.  The equation `qrs=0` is load-bearing.

The exact delayed-load point of the frozen 22-row prefix remains valid but is
not a point of the enlarged system: 13 of the 14 V20 rows are nonzero there,
with `Tg13_6=35/128`; only `Tg14_5` remains zero.

## 2. Shifted-core correction

Write `p=rho^2`.  On both `V(J1)` and the stated `V(k)` restriction, the
correct fourth core combination is

```text
(16/3)*(Tg12_3-(p/2)*Tg12_1) + (8/3)*ell1*Tg11_1.
```

The superseded formula used half the second cofactor.  Its exact residual is

```text
-(1/2)*ell1*[(8/3)*Tg11_1]
```

after the relevant restriction; on `V(k)` this includes the corresponding
load term.  Do not copy the differently normalized residual printed in the
Fable report.

## 3. Grade-14 row-5 scope correction

After setting `J1=(rs,cs,c0,c1)=0`, `Tg14_5` has 62 terms and 12 terms
containing `k`, with

```text
Tg14_5 = -(5/128)*a0*a1*k*rho^4
         mod (cs1,cs2,rs1,rs2,e0,e1).
```

The corrections are not all `cs1`-divisible.  Six of the 12 `k`-terms are
not divisible by `cs1`, and 11 survive after `a1=0`.  Therefore the earlier
sentence that the load row dies on `qa1=0` is retired.  A00/A10 controls rest
on the independently promoted section theorem, not on that sentence.

## 4. Certificate typing gate

For an honest polynomial `T-cs` certificate

```text
cs^N*k^M*(1+rho*W) in K,
```

one must have `M>=1`.  Evaluation at the promoted CS0 section kills every
honest generator, sends `cs` to 1 and `k` to 0, and at `M=0` would leave a
polynomial with constant term 1.  This proof replaces the refuted `deg_2`
argument and remains valid after adjoining all 14 V20 rows.  Certificate
typing must retain, not drop, this gate.

## 5. RS0 and remaining check

RS0 (`rs=1`, every other non-rho source name zero) kills all 36 rows
termwise and is compatible with the raw-row `T-rs` bilinears at
`qcs=qc0=qc1=0`.  It is not a point of the `T-cs` chart.  Transfer to the
promoted four-divided-row `T-rs` relation list remains a one-line open check
and is not promoted here.

## Scope

These are statements about the frozen 36-row actual-total prefix and the
named honest chart equations.  They inherit the single-emitter source
provenance debt.  They prove neither J2 chart, a terminal receiver, source
completeness above grade 14, Gate T, order two, maximum twelve, nor JC2.
