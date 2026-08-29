# Affine-Faber `A`: the `a=3,q=6` graph-predecessor composition

Date: 2026-08-26

Status: **PROVISIONAL CORRECTED EXACT HAND COMPOSITION; FULL GRADE-42
PREDECESSOR REVIEW PENDING.**

## 1. Cell and timing

Use the fixed delayed schedule

```text
normal:15,   center a:3,   U:V:6,   complements:12,
all leading loads and mu2:42.                         (1.1)
```

Impose at grade 42 the corrected exceptional affine graph

```text
K6/K10=15*E^2/32,
K2/K10=15*E^4/256,
mu2/K10=-5*E^6/4096,                                (1.2)
```

with `K10,E,M` units and graph deviations of strictly positive excess.
The corrected ordinary-Faber support and its hostile review prove that the
seven pure-load/target rows in (1.2) vanish.

At the same grade, the normal/kernel contribution is quadratic:

```text
2*15+2*6=42.                                        (1.3)
```

There is no cross term at grade 42:

```text
center*load: 3+42=45,
normal*load: 15+42=57,
intrinsic normal cubic: 3*15=45,
center*kernel quadratic: 3+42=45.                  (1.4)
```

Higher graph deviations and `mu4` occur later by hypothesis.

## 2. Exact grade-42 decomposition

Because the source rows are polynomial and the ordinary connection is
linear, (1.3)--(1.4) give coefficientwise

```text
row_i[42]=affine_graph_i+lambda^2*G_i.              (2.1)
```

Modulo the graph predecessor, the complete seven-row block is

```text
G1=-3*r1*M^2/8+3*s0*M/4,
G2=-3*r0*M^2/8+3*y^2/8,
G3=-3*E*r1*M^2/32-3*M*x*y/8+3*E*s0*M/16,
G4= 3*M^2*x^2/32-3*E*M^2*r0/16-3*E*y^2/16,
G5=-3*E^2*r1*M^2/256+3*E*M*x*y/32+3*E^2*s0*M/128,
G6=-3*E^2*M^2*r0/64+3*E^2*y^2/64,
G7= 3*E^3*r1*M^2/1024-3*E^2*M*x*y/256
    -3*E^3*s0*M/512.                              (2.2)
```

These are the exact center-independent kernel rows; no `a=5` specialization
is used.  Three exact dependencies show that `G1,G3,G4,G6` are sufficient
on `D(E)`:

```text
G6=(E^2/8)*G2,
G5=(3*E^2/32)*G1-(E/4)*G3,
G7=(E^2/32)*G3-(E^3/64)*G1.                       (2.3)
```

The further combinations

```text
G3-(E/4)*G1=-(3/8)*M*x*y,
G6=0 => r0*M^2=y^2                                (2.4)
```

kill both residue charts.  On `D(x)`, `y=r0=0` and
`G4=3*M^2*x^2/32`.  On `D(y)`, `x=0`, `r0=y^2/M^2`, and
`G4=-3*E*y^2/8`.  Hence the projective kernel face at grade 42 is empty.

## 3. Why the raw grade-45 tie is unreachable

The dual-AWS graph-relative V2 support calculation finds at
`(a,q)=(3,6)` the exact
nondeviation weight-45 terms

```text
-E*M^3*lambda^3/16
-3*X^2*a*lambda^2*M^2/8
+3*E*Y^2*a*lambda^2/2.                             (3.1)
```

Equation (3.1) is a valid raw-support sentinel, but (2.2)--(2.4) show that
no projective kernel residue survives grade 42 to reach it.  Thus it cannot
be used as either a direct unit or a survivor equation before predecessor
reduction.

## 4. Cell composition

Subject to exact source confirmation of (2.1), the `v(a)=3` kernel fan is
finite:

```text
0<q<6:  center-independent quadratic two-chart block;
q=6:    the graph-predecessor composition (2.1)--(2.4);
q>6:    graph-relative direct unit from the frozen support analysis.
```

The same exact support calculation gives the direct intrinsic unit for
`v(a)>3,q>=6`; all center-bearing competitors then have strictly larger
weight.  This does **not** remove the equality debt: `(a,q)=(3,6)` is the
only point where (3.1) ties and must be killed by (2.1)--(2.4), not by a
raw-support uniqueness claim.

Increasing `v(a)` above 3 raises every center-bearing raw competitor, so
the same composition is the expected receiver for `3<=v(a)<5`; exact
monotonicity must be charged in the graph-relative review rather than
assumed from this sentence.

## 5. Custody and firewall

This hand composition consumes

```text
5e8e82b3a29f2bdbb1d0c90130bbc7496808582ac0bc7148924b23df1a59bf25
  xmodel/max12-812-order2-affine-faber-a-low-kernel-center-independence-lemma-20260826.md
c467fc5454eda943721c60f599f9e005f158a2fa3f934b64c694df116b1d6bbd
  xmodel/max12-812-order2-affine-faber-a-load-graph-functional-cancellation-20260826.md
4ddc0e4837e1581129fddad70fc7b5c029d642e644f4fd8ab478a4dec59bded3
  xmodel/max12-812-order2-exact-square-affine-mu2-faber-connection-hostile-review-grok-20260826.md
```

The root-owned dual-AWS grade-42 predecessor producer remains controlling
for exact source support, decomposition (2.1), and omissions.  This note
does not prove that a literal raw
source arc reaches graph (1.2), cover `v(a)<3`, another normal/load slope,
factor degeneracies, total-Rees/saturation, terminal/Taylor, order two,
maximum twelve, or JC2.
