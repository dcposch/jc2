# K00 V27 rank-compressed atlas successor design

Author: Sol Ultra, coordinator  
Date: 2026-08-27  
Lifecycle: **DESIGN / UNRUN / NOT EVIDENCE**

## Purpose

V26R1F proves that the six-variable leading-base rank-`<=4` scheme

```text
J4base = B + I5(A)
```

is proper of dimension three.  A literal chart-by-chart continuation would
launch 1,640 jobs.  The reviewed minor census shows that much of that atlas
is redundant.  This design first determines the intrinsic rank on each
leading-base component and only then introduces the 27 additional prior
variables and the inhomogeneous column.

Nothing below is a V27 result.  Every algebra job is AWS-only and every
positive or empty endpoint needs a fresh exact replay.

## Exact setup

Use the byte-frozen V26 objects without recompilation:

```text
R0 = Q[d0_1,...,d5_1],
R  = Q[the 33 V26 prior variables],
A  = the frozen 7 x 7 newest-variable matrix,
E  = [A|-b],
B  = the six nonzero grade-two rows plus F10,
P6 = the complete 35-generator prior ideal through grade six plus F10.
```

The promoted V24R6R1 identity makes `W` redundant modulo both `B` and `P6`.
V26R1F supplies `I6(A)=0` and the promoted proper, dimension-three ideal
`J4base`.

## Compression 1: classify rank on the coefficient base

For `r=4,3,2,1,0`, define

```text
Jrbase = B + I_(r+1)(A).
```

Starting with the known proper `J4base`, decide `J3base=J4base+I4(A)`.

- If `J3base=(1)`, every geometric point of `V(J4base)` has rank exactly
  four.  No `4 x 4` minor charts are needed downstream.
- If `J3base` is proper, retain it and recurse with `J2base`, etc.  The
  difference `V(Jrbase) \ V(J(r-1)base)` is the exact rank-`r` locus.

The unit implication is elementary: `I_(r+1)(A)=0` gives rank at most `r`,
while `V(Jrbase) intersect V(I_r(A))=empty` gives rank at least `r` at every
point.  Thus a unit result at the next lower rank makes the current closed
base scheme rank-pure.

This is the first AWS job.  It is only a six-variable exact calculation and
should precede every full-`P6` chart.

## Compression 2: collapse the rank-five cover

The reviewed V26R1F census finds that all 54 distinct nonzero `5 x 5`
minors of `A` fall into exactly two proportionality classes.  Before any
rank-five solve:

1. freeze one literal representative and every source label for each class;
2. identify coefficientwise which class contains the promoted witness `W`;
3. replay that the entire `W` class vanishes modulo `B` and `P6`;
4. reduce the other representative `M` modulo `B`.

If `M` also lies in `B`, rank five is absent on the whole base.  Otherwise,
on `V(B)` every nonzero maximal minor is a scalar multiple of `M`, so the
entire rank-five locus is the single chart `D(M)`, not 54 charts.  Its full
grade-seven compatibility decision is

```text
P6 + I6(E) + (z*k10_0*M - 1).
```

This reduction is licensed only after the two-class comparison is replayed
from the full literal minor list; Singular's compacted nine-slot `J` is not
itself evidence of the classification.

## Compression 3: rank-pure full compatibility

Suppose the coefficient-base recursion proves a closed scheme `V(Jrbase)`
is rank-pure of rank `r`.  Because `P6` contains `B`, every full prior point
over it still has rank `r`.  Pointwise solvability of `A*y=b` is then exactly
`rank(E)=r`, equivalently `I_(r+1)(E)=0`.  The whole compatible locus at that
rank is therefore decided by one ideal:

```text
Kr = P6 + I_(r+1)(A) + I_(r+1)(E) + (z*k10_0 - 1).
```

No chosen `r x r` minor is needed.  A proper exact result proves only a
nonempty finite grade-seven compatible scheme over an algebraic closure; a
unit result needs a replayed Bezout identity.

If a coefficient-base scheme is not rank-pure, do **not** use `Kr` as a
positive test.  Without `D(I_r(A))`, `Kr` also contains points with
`rank(A)<rank(E)<=r`.  It is then only a one-sided kill screen: `Kr=(1)`
eliminates all compatible ranks at most `r`, whereas `Kr` proper is no
verdict.  Split by the recursive rank filtration before claiming survival.

## Registered execution order

1. **BASE4:** decide `B+I5(A)+I4(A)` in six variables, with tracked
   standard basis or exact unit certificate.
2. **MAX5CLASS:** reconstruct the two maximal-minor classes, identify the
   `W` class, and decide the other class modulo `B` and `P6`.
3. **LOW-KILL (parallel discovery):** run the exact superlocus
   `P6+I5(A)+I5(E)+(z*k10_0-1)`.  Unit is decisive; proper is explicitly
   `NO_VERDICT` until BASE4 proves rank purity.
4. If BASE4 proves rank exactly four, reinterpret LOW-KILL as the exact
   rank-four compatibility ideal and replay its endpoint.  Otherwise recurse
   on `I3(A),I2(A),I1(A)` before rank-local conclusions.
5. Run the single rank-five chart, if the second maximal-minor class survives.
6. Only after all surviving rank components are named should a later-grade
   prolongation be compiled.

The exact and superlocus jobs may run concurrently because an exact unit from
the latter is useful regardless of rank purity.  A proper superlocus result
must not be promoted speculatively.

## Controls and custody

- Pin the V26 compiled-source manifest, V26R1F producer and Fable5 review,
  the promoted V24R6R1 cross-audit, and this preregistration before algebra.
- Recompute every consumed minor from `A`; retain all source row/column
  labels even after proportionality compression.
- Verify both ideal inclusions whenever a compacted generator set is used.
- Include a mutation replacing one representative by a minor from the other
  class, a `b`-sign mutation that changes `I_(r+1)(E)`, and the restored
  forbidden `k6_0` column control.
- Use `liftstd` only as a certificate proposer.  Fresh replay checks
  `matrix(J)T=matrix(G)`, all Buchberger pairs or an independent standard
  basis, and any unit coefficients entrywise over `Q`.
- Every runner refuses non-EC2 Linux, records the registered lane, hostname,
  exact source hashes, wall/RSS/swap telemetry, and fails closed on warnings,
  caps, empty output, or missing replay bytes.

## Firewall

Even a proper `Kr` gives only a geometric pointwise solution through Lambda
grade seven.  It gives no rational point unless one is exhibited, no
nilpotent or later-grade lift, no compatible jet or arc, no source
reachability, no closure incidence, no counterexample, and no JC2 result.

