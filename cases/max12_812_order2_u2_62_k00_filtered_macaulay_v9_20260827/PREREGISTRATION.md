# Preregistration: exact K00 filtered Macaulay degree 7 V9

Date: 2026-08-27

Status: **FROZEN DEGREE-7 COMPATIBILITY TEST; NO V9 RESULT AT REGISTRATION.**

V8 proved the separate global statement

```text
r7 not in (r1,...,r6) on D(C6)
```

in two exact presentations.  Its global-`dp` normal-form degrees are not
canonical filtered obstructions.  Exact calculations already establish that
the true quadratic and cubic classes are compatibility-dead, and an
independent truncated calculation reports compatibility through degree 6.
V9 independently replays the full cumulative ranks through degree 6 and asks
the first unresolved filtered question at degree 7.

Use the faithfully flat weighted Kummer normalization at the generic K00 ray:

```text
C6=1,
C5=d5, C4=(3+d4)/8, C3=d3,
C2=(1+d2)/16, C1=d1, C0=(1+d0)/256.
```

For each unloaded frozen row write

```text
ri = sum_{m>=2} Ri,m,
```

where `Ri,m` is homogeneous of transverse degree `m`.  At cutoff `D`, form
the complete linear Macaulay map

```text
(h1,...,h6) |-> sum hi*ri mod (d)^({D+1}),
deg(hi)<=D-2,
```

with every equation in degrees 2 through `D`.  This cumulative construction
automatically includes:

- every constant syzygy among `Q1,...,Q6`;
- every new syzygy among corrected degree-3 and later initials;
- every representation of the row-7 quadratic class; and
- all higher homogeneous multiplier corrections allowed through the cutoff.

The exact-Q AWS lane must reproduce these prefix rank/augmented-rank sentinels:

```text
D=2: 4/4
D=3: 28/28
D=4: 106/106
D=5: 294/294
D=6: 676/676.
```

It then computes rank and augmented rank at `D=7`.  A compatible result must
save an exact rational multiplier jet through degree 5 and replay all 1,709
coefficient equations.  An incompatible result must save and replay an exact
left compatibility functional.  A separately serialized good-prime lane is
software/navigation only and cannot replace the rational endpoint.

The same frozen source pass also records, without eliminating any load, the
minimum K00 transverse degree and term counts of each affine load derivative
(`k10,k6,k2`) in every row.  This is a valuation stencil for the next
`Lambda^19` reachability compiler, not a projection or verdict.

If exact rank increases on adjoining row 7 at degree 7, V9 identifies the
first canonical filtered pure-coefficient obstruction.  If ranks remain
equal, it proves compatibility only through degree 7 and raises the next
cutoff to degree 8.  Either outcome is local to the generic normalized K00
coefficient germ and does not decide the mixed `Lambda`/load/target closure,
Taylor realizability, order two, maximum twelve, or JC2.
