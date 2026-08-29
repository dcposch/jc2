# Exact D16--D22 tail of the deep active-`c2` literal survivor

Date: 2026-08-28  
Status: **EXACT PRODUCER / AWAITING DIFFERENT-MODEL REVIEW**

## Verdict

The independently repaired deep `A|V0`, `c2!=0`, exact-`D=0` lane contains
a rational raw point through D15.  Continuing that *same literal point*
through the complete characteristic schedule and authoritative raw windows
gives a sharp answer:

```text
G16=G17=G18=G19=G20=G21=0,
c16=0,
c18=16369/140737488355328,
c20=0,
g22=(9207/144115188075855872) A^-5.
```

Thus every raw determinant row `D0,...,D21` is exactly zero, but the absent
raw `G22` receiver gives

```text
D22_raw=-L22(g22)=0,
```

not the required endpoint target `1`.  This literal survivor therefore dies
only at the endpoint.  It is not evidence that the deep locus is nonempty at
the endpoint; conversely, one specialization does not prove the entire deep
locus empty.

The calculation is useful because it rules out two tempting shortcuts:

1. D16--D21 need not obstruct the repaired deep branch.
2. A born negative mode need not vanish: `c18` is uniquely forced nonzero
   and makes the literal `G18` window polynomial (indeed zero).

The general successor is the endpoint class modulo the exact homogeneous
kernel `K*A^-5`, not another assumption that later modes vanish.

## Frozen input point

The upstream independently checked point is

```text
A=X^4-1,
V0=A,
T=-A/4,
Z=(1-A)/2,
F4=(Z^2-A)/64,
F5=(A-1)/512,
F6=1/4096,
F7=...=F14=0,
c2=c6=1,
c14=-6139/17179869184,
c4=c8=c10=c12=0.
```

It lies on the exact `D=0`, `E=L=J=0` successor described in the repaired
D8--D13 audit.  The new checker first reconstructs the complete prefix and
replays `D0=...=D15=0`, including `G12=4093/268435456` and
`G13=G14=G15=0`, before inspecting any later row.

## Exact continuation

The checker rebuilds the generalized-binomial recurrence directly after
specializing the raw `F_i`; this avoids a large generic symbolic expansion.
At each born row it solves the single affine scalar mode by exact division by
the needed power of `A` and then enforces the literal lower and upper windows:

```text
G16: X^2..X^8,   G17: X^2..X^7,
G18: X^2..X^6,   G19: X^3..X^5,
G20: X^3..X^4,   G21: X^3.
```

All six resulting polynomials are zero, so every window is satisfied.  A
literal determinant replay with no raw `F15` or later slot and no raw `G22`
then verifies all 23 rows `D0,...,D22` are zero for this homogeneous point.
The endpoint target changes only the last equation to `D22=1`, which the
point cannot satisfy.

After canceling eleven common powers from the initially accumulated
weight-22 fraction, the exact auxiliary coefficient is

```text
g22 = (9207/144115188075855872) / A^5.
```

The universal operator

```text
L22(R)=-40 A^3 A' R-8 A^4 R'
```

annihilates every scalar multiple of `A^-5`.  Mutating `-40` to `-39`
leaves residual scalar `-1`, so the zero endpoint is an exact kernel event,
not accidental numerical cancellation.  A second mutation sets `c18=0`
and leaves a genuine pole at weight 18.

## Custody and scope

Checker:

```text
cases/ggv_8_28_upper_endpoint_active_c2_literal_d16_d22_probe_20260828/
  probe_literal_tail.py
```

Expected marker:

```text
PASS_EXACT_ACTIVE_C2_LITERAL_D16_D22_TAIL
```

The checker pins the frozen repaired-prefix checker, the authoritative raw
compiler, and the complete raw source.  It uses standard-library rational
arithmetic only and takes about eight seconds on the coordinator host.

This proves only a statement about one exact rational specialization.  It is
not a universal deep-locus endpoint theorem, scheme statement, unrestricted
branch-P result, Keller theorem, counterexample, or proof of JC2.

