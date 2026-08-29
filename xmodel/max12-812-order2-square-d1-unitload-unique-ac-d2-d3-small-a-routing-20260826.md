# Routing: residual unit-load unique-`AC` `d=2,3` cells

Date: 2026-08-26

Status: **EXACT FAN ROUTING AND PREREGISTRATION DESIGN; NO NEW EMPTINESS
VERDICT.**

## 1. Exact residual after the high-contact source ceiling

In the normalized integral unit-load unique-`AC` cell put

```text
d=c-a in {1,2,3},  s=r-a>=0,  a+3*s>d,
a>=1, r>=2, c>=3.
```

The promoted ladder closes `d=1`.  The frozen, separately reviewed
`C>=a+1` source-ceiling corollary, if confirmed and promoted, closes every
`d=2,3` point with `a>=10`.  The exact remaining thresholds are then:

```text
d=2:
  a=1,2  with s>=1;
  a=3..9 with s>=0.

d=3:
  a=1..3 with s>=1;
  a=4..9 with s>=0.
```

These statements include the domain condition `r>=2`.  The excluded lower
values are equality faces, not missing strict-cell points: at `d=2,a=2,s=0`
one has `a+3s=d`, and at `d=3,a=3,s=0` likewise.

Thus an apparently unbounded residue has exactly eighteen baseline blocks,
one for each `(a,d)` with `1<=a<=9,d in {2,3}`.  Put

```text
s_min(a,2)=1 for a<=2, else 0;
s_min(a,3)=1 for a<=3, else 0;
R=sigma^(a+s_min)*eta*Rbar.
```

The homogeneous substitution `eta=sigma^u`, `u>=0`, covers the complete
unbounded `s` tail of each block without inversion.  No separate finite box
in `r` is legitimate or needed.

## 2. Exact grade windows

The first unique-`AC` grade and the `C^2` target are

```text
G_AC(a,d)=10+2*a+d,
G_C2(a,d)=10+2*a+2*d=G_AC+d.
```

Across the eighteen blocks the complete replay ceiling is only grade 34:

```text
16 <= G_C2(a,2) <= 32,
18 <= G_C2(a,3) <= 34.
```

Consequently `mu2` and `mu4` target jets and all lower-load terms licensed
through grade 34 must be retained.  `mu6` and `J` begin at grades 36 and 38
and cannot enter.  Target parity is still to be checked from the literal
rows, not assumed from this timing table.

## 3. Controlling local invariant

The first `AC/L` source equation allocates opposite roots of the squarefree

```text
L=(z-lambda)*(z+lambda),  p=-2*lambda^2,
```

so, up to deck swap,

```text
A0=alpha*(z-lambda),  C0=gamma*(z+lambda),
alpha*gamma*lambda!=0.
```

At the `A0` root the target term is

```text
(3/8)*C0^2/L^2=(3/8)*gamma^2/(z-lambda)^2,
```

with nonzero local double-pole coefficient `3*gamma^2/8`.  The promoted
universal row functional at terminal row seven and pole ceiling one is

```text
W_(3,1)=(1-(p/2)*x)^(3/2),
[Phi7,Phi5,Phi3,Phi1]
  coefficients [1,-3*p/4,3*p^2/32,p^3/128].
```

It annihilates the complete moving simple-pole block.  A source-aware client
must additionally enumerate every pole-two-or-higher family which reaches
`G_C2` and check its **local** order at the allocated root.  Global
denominator order is not enough.

The existing hand pole audit predicts one and only one dangerous baseline:

```text
(a,d,s)=(1,3,1), equivalently (a,c,r)=(1,4,2).     (E)
```

There `R*A^2/L^2` begins at gap one, and its second correction can contain
`R0*A1^2/L^2` at the gap-three target with no `A0` factor.  It can therefore
carry a genuine local double pole.  Away from (E), every correction of
`R*A^2/L^2`, `A^3/L^3`, `k10*R^2*A/L^2`, and any lower-load higher-pole
family which reaches the target must retain enough allocated-root factors
to have local pole order at most one.  This prediction is not promoted until
the complete source replay verifies it.

## 4. One batch producer, not forty serial clients

The next AWS producer should compile all eighteen `(a,d)` baselines in one
source-frozen package and use `eta` for their `s` tails.  It must:

1. mechanically binomial-expand all four source summands separately for
   each baseline through `G_C2`, derive every normal/load/moving-`p`/target
   jet ceiling, and give a canonical primitive/monomial inventory;
2. rebuild all seven frozen literal Faber rows through that ceiling and
   compare them coefficientwise with the independent analytic inventory;
3. verify the complete moving `W_(3,1)` simple-block annihilation and both
   root orientations;
4. after `z=lambda+u`, clear only powers of the unit `u+2*lambda`, certify
   the local pole order of every non-simple family, and extract the exact
   `u^-2` coefficient at `G_C2`;
5. return the nonzero `3*gamma^2/8` coefficient on all safe blocks, but
   deliberately reject (E) as a negative control because its `RA2`
   correction can also contribute at order two;
6. test the fan inequalities symbolically and require exactly the eighteen
   baselines and the displayed `s_min` table, rather than accepting a sampled
   integer box;
7. run exact Q on one AWS host and a good-prime software control on a second,
   with fresh tags, fail-closed validators, full custody, and zero swap.

If this producer and hostile review pass, seventeen of the eighteen
small-`a` baseline tails close at once.  The only remaining unique-`AC`
strict cell is the dedicated exact successor (E), plus equality faces that
were never in the strict unique-`AC` list.

## 5. Priority after the batch

1. Run a dedicated complete-source successor for (E), retaining the competing
   `C^2` and second `RA2` correction rather than applying the simple-block
   lemma.
2. In parallel adapt the same local row-syzygy miner to the already isolated
   safe subcone of unique `RC`; it has the same `C^2` double-pole target but a
   different correction wall.
3. Only then spend broad CAS on tied leading faces.  The leading-face triage
   predicts immediate kills for every `C2`-incident face, unique `A2`, unique
   `R3`, and most of the exceptional `RA2` boundary, but high-contact lower
   loads must be stratified before those hand claims can be promoted.
4. Positive-order `k10` needs a rebuilt complete fan including delayed
   `k6,k2` support and `A3`; the old seven-form Z3 census is navigation only.

## Firewall

This file is routing and a producer acceptance design.  It does not promote
the hand simple-block theorem, close any `d=2,3` cell, treat an equality face,
or import the still-reviewed high-contact corollary.  It says nothing about
`p=0`, `k0=0`, positive load, zero/infinity, terminal/Taylor landing, the
whole square component, order two, maximum twelve, or JC2.
