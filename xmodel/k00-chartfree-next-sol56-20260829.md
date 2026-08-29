# K00 chart-free successor: the exact-rank-two branch is obstructed at grade three

Author: Sol 5.6  
Date: 2026-08-29 UTC  
Lifecycle: **PROVISIONAL EXACT DESK THEOREM / INDEPENDENT REPLAY REQUIRED /
NO CANONICAL PROMOTION YET**  
Frozen campaign basis: `92ebe92ad5986a47f01af9ed901260595dfed869`

## 0. Executive verdict

The six-hour full-`P6` selected-chart computation was aimed too far
downstream.  There is a chart-free obstruction already in the seven literal
Lambda-grade-three rows.

Let `A` be the frozen V26 grade-seven newest-variable matrix and let

```text
J2 = B + I3(A)
```

in `Q[d0_1,...,d5_1]`; the promoted V27 containments identify this with
`B+I5(A)+I4(A)+I3(A)`.  If `P3(x,u)=0` denotes the seven grade-three rows,
with

```text
x = (d0_1,...,d5_1),
u = (d0_2,...,d5_2),
```

then exact extraction from the frozen compiler gives

```text
P3(x,u) = C(x) u + c3(x),
C(x) = A(x)[:,1..6].
```

Set `E3=[C|c3]` and `H=J2+I3(E3)`.  The desk calculation proves, for every
literal `2 x 2` minor `q` of `A`,

```text
q^4 in H.
```

Therefore `I2(A) subset sqrt(H)` and

```text
sqrt(H) = sqrt(J2+I2(A)).
```

Any rank-exactly-two leading point that lifted through grade three would lie
in `V(H)`, while the displayed radical containment forces every point of
`V(H)` to have `rank(A)<=1`.  This is impossible.  Subject to an independent
exact replay of the fourth-power memberships, the conclusion is:

> **No rank-exactly-two point of the V27 coefficient base lifts even through
> Lambda grade three.  Hence the rank-two part of the full `P6` incidence is
> empty, on every minor chart, before grades four through six are used.**

This supplies the mathematical verdict that the capped selected-minor run
could not reach: its target ideal is the unit ideal.  It does not yet supply
the tracked Bezout certificate required to promote that executable endpoint.

## 1. Authoritative frontier before this check

The reviewed V26/V27 facts used here are only the following.

1. In the six leading variables, `J2=B+I3(A)` is proper homogeneous of
   affine dimension three, and every point has `rank(A)<=2`.
2. `J1=J2+I2(A)` is proper of affine dimension two.  The reviewed census is
   291 nonzero `2 x 2` minors outside `J2` and 60 inside; the rank-exactly-two
   geometric difference is nonempty at this leading-base tier.
3. The deterministic selected minor is the `(rows 5,7; columns 6,7)` minor,
   but the repaired full-`P6` chart
   `P6+I3(A)+(z*m-1)` ended at `RESOURCE_CAP_NO_VERDICT` after 21,000 seconds,
   about 16.1 GB maximum RSS, and zero swap.  That run emitted neither a
   basis nor a mathematical endpoint and must not be repeated with the same
   engine/order.

Frozen inputs used in the desk derivation are:

```text
d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501
  ATLAS_EXACT_POLYNOMIALS.json
c8aa23e46f909e70c2c8d302ca67a415496df9a969f99817d2ef593f60f614c0
  BASE3_R2_STANDARD_BASIS.txt
738f46030a73fea2a06a8e3139ed9aa5e2001b72a579e459357af81f6801647a
  xmodel/k00-v27-base4-base3-base2-hostile-review-fable5-20260827.md
4780282b40a8bb0c83da3b3cd887c8e2edb5af99816203e8188a253f1174d6d8
  cases/max12_812_order2_u2_62_k00_aws_custody_20260828/CUSTODY.sha256
```

The seven polynomials selected from the nonzero prior list were checked to
equal, object-for-object, the seven literal source-labelled rows with
`Lambda_grade=3` and row labels `1,...,7`; the slice was not inferred merely
from a term count.

## 2. Exact grade-three factorization

In the full 33-variable frozen ring, differentiate the seven labelled
grade-three rows with respect to the six variables `d0_2,...,d5_2`.  The
following three coefficientwise checks returned zero failures:

```text
SECOND_DERIVATIVE_BAD=0
AFFINE_RECONSTRUCTION_BAD=0
C_A_MISMATCH=0
```

Thus every grade-three row is affine linear in `u`, its reconstruction as
`C*u+c3` is exact, and `C` is byte-derived from the same source as the first
six columns of `A`.  The seventh column of `A`, belonging to the later
`k10` newest variable, is correctly absent at grade three.

This identity is the key compression.  A full prior point of rank two must
first solve this seven-by-six affine system; no grade-four, grade-five,
grade-six, `k10_0`, selected minor, or 33-variable Groebner basis is needed
to test the resulting necessary condition.

## 3. Chart-free Fitting obstruction

For any geometric leading point `x`, solvability of `C(x)u=-c3(x)` implies

```text
rank([C(x)|c3(x)]) = rank(C(x)).
```

On the rank-`<=2` base this implies `I3(E3)=0`, regardless of whether
`rank(C)` is two, one, or zero.  Hence every actual grade-three lift in the
rank-`<=2` branch projects into `V(H)`.

The exact characteristic-zero desk pass reconstructed all stored minors and
reported:

```text
I3E_NCOLS=813
I3E_SIZE=813
I3E_OUTSIDE=399        # nonzero normal forms modulo J2
H_DIM=2
H_NCOLS=20
H1_DIM=2
H1_NCOLS=10
```

Here `H1=H+I2(A)`.  Algebraically, every `3 x 3` minor of `[C|c3]` is already
in `I2(C)` after expansion along its last column (and the minors not using
that column are in `I2(C)` as well).  Thus

```text
H subset J2+I2(A) = J1.
```

The reverse set-theoretic containment is supplied by the exact power test.
Across all 351 nonzero stored `2 x 2` minors of `A` (with the other 90
literal slots identically zero), the number whose indicated power retained a
nonzero normal form modulo a freshly computed standard basis of `H` was

```text
power 1: 291
power 2:  60
power 3:  36
power 4:   0
```

Consequently every generator of `I2(A)` lies in `sqrt(H)`, and the two
radicals are equal.  This is stronger than a dimension coincidence and does
not select, sample, or assume a successful `2 x 2` minor.

The run was a bounded local exact check: 2.28 seconds wall, about 23.9 MB
maximum RSS, zero swap, one Singular process.  A transcript containing the
markers plus the complete deterministic serializations of the 20-element
`H` basis and 10-element `H1` basis has SHA-256

```text
0990f7dd2ced2449b8b391b4e74fb36df1f267a07181f2dce29574529e31d2c7.
```

This transcript hash is custody, not an independent proof.  The exact
normal-form pass proposed the theorem; promotion still requires frozen
source code, labelled transforms or membership columns, mutations, and a
different implementation/model replay.

## 4. The theorem and its full-`P6` corollary

Assume `x` lies in `V(J2)` and `rank A(x)=2`.  If some `u` solves the seven
grade-three equations, then all `3 x 3` minors of `E3(x)` vanish, so
`x in V(H)`.  But `I2(A) subset sqrt(H)` makes every `2 x 2` minor of
`A(x)` vanish.  Hence `rank A(x)<=1`, a contradiction.

Every solution of the complete prior ideal `P6` contains a solution of its
grade-three subsystem.  It follows that, over an algebraic closure,

```text
V(P6+I3(A)) intersect D(I2(A)) = empty.
```

Equivalently, the chart-free rank-two saturation is the unit ideal.  In
particular, for every literal `2 x 2` minor `m`, not only the previously
selected one,

```text
P6 + I3(A) + (z*m-1) = (1).
```

The equality is a mathematical consequence of the radical certificate and
the Nullstellensatz; no explicit full-ring Bezout column was computed here.
The old capped target should therefore be classified as **mathematically
predicted unit, executable certificate still absent**, never retroactively
relabeled as an engine success.

## 5. Smallest promotion packet: `K00-G3-R2-CHARTFREE/v1`

The immediate successor is not another full-`P6` run.  Freeze a desk-scale
producer/reviewer packet with the following exact contract.

### Inputs

- the V26 atlas and its compiler/source manifests;
- the reviewed V27 `J2` basis and R1--R3 review;
- all seven literal `(Lambda_grade,row)=(3,1..7)` source labels;
- all 1,225 literal `3 x 3` labels for `E3` and all 441 literal `2 x 2`
  labels for `A` (zeros retained as labels).

### Producer outputs

1. Rebuild `P3=C*u+c3`, with all second derivatives, affine reconstruction,
   and `C=A[:,1..6]` checked coefficientwise.
2. Build `H=J2+I3(E3)` from the raw labelled generators.  Emit a tracked
   exact standard basis and rederive properness and dimension two without a
   status-attribute shortcut.
3. For every nonzero literal `2 x 2` minor `q_j`, serialize and freshly
   replay a rational coefficient identity

   ```text
   q_j^4 = sum_k h_(j,k) Hraw_k.
   ```

   Scalar-proportional minors may share a normalized certificate only after
   both scalar directions and every source label are frozen.
4. Verify `I3(E3) subset I2(C) subset I2(A)` independently by labelled
   Laplace identities, and bind the complete ordinary output.

### Adversarial controls

- a changed coefficient in one `c3` row must change a named augmented minor;
- a changed entry of `C` must trip the `C=A[:,1..6]` equality;
- deleting or perturbing one nonzero coefficient in each selected
  fourth-power certificate must break that identity;
- adding `1` must trigger the unit control and `(d0_1)` must remain the known
  proper control;
- all positional loops use `ncols()`, never `size()`;
- a fresh process and a different implementation/model must reconstruct the
  minors, basis criterion, and all power memberships without trusting the
  producer's status strings.

### Outcomes and stop rules

```text
PASS_K00_G3_R2_CHARTFREE_OBSTRUCTED
FAIL_K00_G3_R2_POWER_OR_SOURCE_IDENTITY
DEPENDENCY_OR_REPLAY_FAILURE
```

- On `PASS`, promote the grade-three rank-two obstruction, stop every
  full-`P6` rank-two minor chart and do not spend AWS time extracting a
  redundant full-ring Bezout certificate unless archival software closure
  is specifically valuable.
- If even one labelled fourth-power identity fails independently, withdraw
  this theorem and retain that exact minor as the only named diagnostic;
  do not fall back to all-minor brute force.
- Any source-label, affine-reconstruction, or `C=A[:,1..6]` mismatch is a
  dependency failure, not a geometric result.

Measured producer scale is under 3 seconds and 24 MB on one local process,
so this is a desk computation under the campaign policy and needs no AWS.
If operational isolation is desired, a 2-vCPU/4-GB instance with a
two-minute wall cap is ample; no large-memory machine is justified.

## 6. Research allocation after promotion

The result removes only the lower-locus rank-two branch.  It does not remove
the following distinct work.

1. **Rank five:** finish the registered `MAX5CLASS` comparison.  The two
   proportionality classes of maximal minors reduce the rank-five base to at
   most one nonredundant surviving class after the `W` class is accounted
   for.  Do not infer that V27 treated this branch; it did not.
2. **Rank at most one:** on `J1`, grade-three compatibility must use the
   lower Fitting strata, not `I3(E3)`.  Split chart-freely into
   `rank(C)=1`, requiring `I2(E3)=0`, and `rank(C)=0`, requiring `C=0` and
   `c3=0`.  Do not infer a lift from `sqrt(H)=sqrt(J1)`; on rank one,
   `I3(E3)=0` is only the automatic weak condition `rank(E3)<=2`.
3. **Later source open:** `k10_0` first enters after this grade-three gate.
   Retain `k10_0!=0` at the first rank-one successor where it is actually
   typed; do not project away the normalized source-open requirement.

These branches may run in parallel after the independent replay.  Neither
needs to wait for a review of unrelated proof-side lanes.

## 7. Scope firewall

This report is a same-model provisional producer result.  It proves no
rank-five statement, no rank-one or rank-zero lift, no grade-seven
compatibility, no grades 8--19 jet, no `Jdet`-open source reachability, no
formal or convergent arc, no closure incidence, no order-two or
maximum-twelve conclusion, no polynomial Keller map, no counterexample, and
no result on JC2.

It also does not turn the historical `RESOURCE_CAP_NO_VERDICT` run into
evidence.  The new argument supersedes its target mathematically only after
the independent labelled fourth-power replay is accepted.

## Seal

- Body length: `11951` bytes (all bytes before this heading).
- Body SHA-256:
  `6e7bacc0e0d338847ff59fb92d77c071edc998ecd297185ca6706737c73bbed5`.
