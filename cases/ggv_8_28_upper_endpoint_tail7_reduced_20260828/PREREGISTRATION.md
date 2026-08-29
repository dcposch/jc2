# Preregistration: first endpoint-capable reduced square-tail chart

Date: 2026-08-28

## Charged question

Find a genuine characteristic-zero field point in the frozen branch-P raw
upper windows with the literal equations

```text
D0=...=D21=0,   D22=1,
```

and no `G22` slot.  A class-only point, a formal endpoint particular, a
nonreduced Artin section, or a point outside the frozen 303 raw coordinates
does not count.

The fixed reviewed branch-P fixture is

```text
A=X^4-1,  H=A^2,  F0=H^2,  G0=H^3,
F1=H,     c2=0,
F2=(1+HZ)/4,  F3=(Z+AT)/8.
```

Set every deformation parameter of weight below seven to zero.  Thus the
prefix before weight seven is the exact square family

```text
U=H+t/2,  F=U^2,  G=U^3.
```

Retain every literal raw parameter of weight at least seven.

## History check and minimality

No reviewed artifact contains an exact raw endpoint point.  The frozen
weight-11 and weight-10 positive-search tails returned specialized units.
Fresh exact compilation shows something stronger for the next two rungs:
after the complete prefix nullspace is substituted, the constant coordinate
of `D22-1` is literally `-1` at both cutoffs nine and eight.  These two tails
are therefore empty before any nonlinear solving.

Cutoff seven is the first endpoint-capable square tail.  Its exact prefix
through row 13 has

```text
190 retained raw variables,
rank 102,
nullity 88.
```

In those nullspace coordinates its endpoint constant is exactly

```text
D22[X^0]-1 = -1-p32*p87,
p87=F7[X^0],
p32=G15[X^1].
```

Select the reduced rational chart

```text
p87=1,  p32=-1.
```

This makes `D22[X^0]=1` identically and is the smallest square-tail chart
that does not fail at the constant coordinate.

## Exact reduction

Use only constant-Q row operations and the literal triangular same-row
operators.  Eliminate rows 14 through 21 in order.  Row 14 retains its one
reviewed homogeneous-mode direction; rows 15 through 21 have no free
same-row direction after `p32=-1` is fixed.  Then eliminate every affine
linear compatibility pivot exposed by substitution.

The charged residual has

```text
41 rational parameters,
152 nonzero equations,
maximum total degree 3,
303 exact raw-coordinate reconstruction formulas.
```

The authoritative bytes are

```text
7edd5ccd471e9eb3e27f0f163b0b337e0fb5057126ec69869f988093defba7aa  TAIL7_REDUCED/TAIL_DEFORMATION_SYSTEM.json
770ba6d9b312e235e491b4ad948707c41ad4a622b3a17239fdfe62f353606e11  TAIL7_REDUCED/TAIL7_REDUCED_SYSTEM.json
a90ca7d9b0ed14d335e20d44308830ff6f0d90ca4dab247658cc75842883e93f  TAIL7_REDUCED/tail7_reduced_q.sing
55c1bfe67fe21413f20c5cbf420728552edd3722c536337ea4879eee050f44a9  TAIL7_REDUCED/tail7_reduced_p65521.sing
```

`verify_tail7_reduced.py` must pass before launch.  It independently
recompiles cutoffs seven, eight, and nine; checks the two literal `-1`
failures; checks the tail-seven endpoint chart; replays the exact triangular
compiler; and demands byte identity of both emitted engines.

## AWS lanes

Heavy algebra runs only on audited idle r6d:

```text
instance: i-07eeaf8ba6f0bc419
type:     r6i.16xlarge
public:   100.26.198.153
```

The exact-Q lane uses one core, a 128-GiB virtual-memory cap, a three-hour
wall cap, zero swap, and at least 150 GiB of post-cap headroom at launch.
An independent `F_65521` discovery lane may use one core, a 32-GiB cap, and
one hour.  It is non-evidence in either direction.  Both lanes use fresh
immutable source and output namespaces, pin the EC2 identity and Singular
binary, and emit terminal evidence manifests.

## Stop and continuation rules

* **Positive stop:** obtain exact rational values for all 41 parameters,
  reconstruct all 303 raw coordinates, and pass the independent literal
  `verify_endpoint.py --witness` replay.  Only that object is a genuine raw
  endpoint seed for the next class-to-raw experiment.
* **Unit stop:** an exact-Q unit excludes only this normalized tail-seven
  chart.  It is not evidence against the full branch-P endpoint system.
* **Proper without point:** dimension, a modular point, a partial basis, or
  a proper exact ideal is diagnostic only.  Continue with rational-point
  extraction or an exact number-field point plus a new literal verifier.
* **Resource stop:** timeout, memory exhaustion, swap, a custody mismatch,
  or an incomplete output is operational non-evidence.

No `D23`, q1 image equation, row-34 Artin relation, class-tower equation,
landing assertion, family claim, or JC2 conclusion is admitted in this
case.

## Reviewed source authority

```text
59e9bf2c6713b84ef848bae693a7e88f62c679ff56bad34fce4d3a28548663f3  xmodel/ggv-8_28-raw-global-determinant-d5g-sol-20260827.md
14913814fce76629836da359f630727b92167d3a23912c9fa265ac8d71f800d2  xmodel/ggv-8_28-raw-global-determinant-d5g-hostile-audit-sol-ultra-20260827.md
fd1640420ac389b1b6c3a0ea21243f5d72488bba5d39e4cc2293ab9e7c494681  xmodel/ggv-keller-face-general-multiplicity-endpoint-r5-sol-20260827.md
48fff5d5345cdd74c30367a638a3b5148cb9a02910b186fc7be0585ebc4b6c84  xmodel/ggv-keller-face-general-multiplicity-endpoint-r5-hostile-review-opus5-20260827.md
ed0e3460cc16d0d8b9fb25823dc09f56bb4b1ad41561744bc8713848128fad19  xmodel/ggv-endpoint-survivor-codimension-r6-sol-20260827.md
44d2d8a0433abc8e19cfd127164572aba840d6f2e5a2b0af9b160504c9e890bd  xmodel/ggv-endpoint-survivor-codimension-r6-hostile-audit-sol2-20260827.md
6e3d9104effe39c0dd0e34377bb7bdc6ede4f25f472f9f9c0098706aceffb60a  xmodel/ggv-8_28-upper-cascade-w3-w6-sol-ultra-20260827.md
7358e6623a84ddd6b1aaad1a9b07a1c0c8966f74f75203977c0314bf3588e7ec  xmodel/ggv-8_28-upper-cascade-w3-w6-hostile-review-fable5-20260827.md
43a949b24a3cdec5de41a8b1bf1bf76ed9f3b863d04d99d1b48ddb6040d9c3a5  xmodel/ggv-degree8-r5-survivor-raw-support-analysis-grok-20260827.md
5735ee90e5b7c51444892c011a072bcaaf497f6e446c46934f392fdb08a85ede  xmodel/ggv-degree8-r5-survivor-raw-support-analysis-hostile-audit-sol-ultra-20260827.md
```
