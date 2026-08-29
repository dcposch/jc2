# `(8,12)` order two: delayed-load parity/Fitting design V2 repair

Date: 2026-08-26

Status: **NONMUTATING REPAIR OF THE V1 DESIGN.  THE HIGH-CONTACT
RANK-ONE GATE SURVIVES ON A STRICT OPEN; THE `A` FACE IS NOT CLOSED.  THE
CORRECTION-COMPLETE MIDDLE CONE AND THE REPEATED-ROOT PREDECESSOR TOWER ARE
THE LIVE OBJECTS.  NO TOTAL-REES OR ORDER-TWO EXCLUSION IS CLAIMED.**

## 0. Supersession and new audit

This note does not alter

```text
5308b76ae02e50e5845b4799a192ee94f195f606d43f94dfe131f0384874e4a1
  xmodel/max12-812-order2-affine-faber-total-rees-fitting-import-design-20260826.md
```

It supersedes only V1 Sections 5--7 wherever they treat the primitive
`A`-face cubic as a source-complete leaf certificate.  The independent
audit is

```text
dfb1cc84f4fb30c198dc646ba4416b5cc118b9d74cebead302db9b428594e7b8
  xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-independent-audit-20260826.md
```

and returns `REPAIR` on

```text
9419c08b4be09fee8ecae9b73c8c9c610770a7166e17a973251312d28b69a695
  xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-20260826.md.
```

The delayed-load timing, first-normal UFD split, normalized cubic forms,
and the exact Fitting matrices in V1 remain valid.  What fails is
correction completeness on the repeated-root `A` branch and, more
generally, the inference from a normalized cubic residual to the literal
source at the unit-terminal grade.

## 1. Smallest omitted correction

On the repeated-root divisor

```text
r=0,                 Q0=z^2*(z^2+p),
D=p^2/4 != 0,        N3=v*z*(z^2+p),                (1.1)
```

the leading quadratic receiver is polynomial because

```text
N3^2/Q0=v^2*(z^2+p).                               (1.2)
```

Retain the next normal and the leading odd square tangent:

```text
Q(t)=Q0+t*x*z+O(t^2),
E(t)=t^3*N3+t^4*N4+O(t^5),
N4=m3*z^3+m2*z^2+m1*z+m0.                         (1.3)
```

The exact first unloaded row at `t^7` is

```text
R1[t^7]=(3/4)*v*m0-(3/8)*v^2*x.                   (1.4)
```

Thus the legal even correction

```text
m0=v*x/2                                           (1.5)
```

cancels the proposed post-null pole.  Setting the leading normalized
coordinate `e0` to zero does not remove (1.5): it is a higher coefficient
of `e0(t)`.  Under the primitive tie

```text
Lambda=sigma^3,                  t=sigma^5,         (1.6)
```

the source has arbitrary square-normal, square-tangent, load, and target
corrections through the unit-terminal grade `sigma^57`.  The normalized
`A5` residual is therefore a zero-higher-correction control, not a source
unit.

The specific squarefree rational lift with `Q0=z^4-1` remains rejected by
its first nonzero unloaded rows.  That pointwise rejection is not an
`A`-component theorem.

## 2. Exact range of the surviving rank-one gate

Retain the V1 notation

```text
e=v(Lambda),                 H=v(C-K^2),
q0=D*(5D+2s)/32,
m_c=(q0,-p*q0/4,q0*B0)^t,
v_c=q0*B7.                                         (2.1)
```

On the unit-`J` delayed-load ray, the common loaded face and terminal are
at valuations `14e` and `19e`.  The unloaded normal contribution is
`O(2H)`, while the loaded linear normal contribution is `O(14e+H)`.
Therefore the literal rows through the terminal see only the square-
tangent `c` column whenever

```text
2H>19e.                                            (2.2)
```

Condition (2.2) also implies `14e+H>19e`.  On `D(q0)`, the exact `4 x 2`
block of V1 (3.11) then applies coefficient by coefficient.  Parity makes
its residual column zero after the lower `c` coefficients have been
removed; its last minor forces the leading capitalized `J` coefficient to
zero.  This contradicts the **unit-`J`** chart.

This is a strict inequality.  At

```text
2H=19e                                             (2.3)
```

the first unloaded term can enter the same row and grade as `J`, so the
rank-one block alone gives no exclusion.  For `14e<=2H<19e`, unloaded
Kuranishi terms occur between the central face and terminal; for
`2H<=14e`, the normalized pure-face quotient is not available without a
predecessor solve.

On the normalized `K` resonance

```text
5D-2s=0,                     D!=0,                  (2.4)
```

one has

```text
q0=5D^2/16 != 0.                                  (2.5)
```

Hence the `4 x 2` gate excludes exactly the part of the `K` resonance
satisfying (2.2), on `D(K10*D)` and with capitalized `J` a unit.  It also
includes the exact-square case `H=infinity`.  It does **not** exclude the
`K` resonance at or below (2.3), positive-valuation capitalized `J`, or a
chart with an additional odd center/torsion coordinate.  Lower-contact
`K` points may eventually die in the correction fan, but not from the
rank-one matrix by itself.

The same statement holds on the generic affine open `D(q0)`.  No part of
the `A` face `q0=0` is covered by this matrix.

## 3. Correct finite valuation skeleton

The V1 four-letter split was too coarse because a nominal first term of
valuation `2H` can lie in the first-normal null module and disappear from
the tails without raising `H`.  The corrected skeleton separates target
ties and coefficient-null strata.

For the nominal quadratic valuation `W=2H`, the target walls are

```text
14e          central affine/mu2 face,
16e          mu4 target,
18e          mu6 target,
19e          unit-J target.                        (3.1)
```

Thus the finite coarse cones are

```text
P0: W<14e,
F14: W=14e,
Q14-16: 14e<W<16e,       Q16: W=16e,
Q16-18: 16e<W<18e,       Q18: W=18e,
Q18-19: 18e<W<19e,       Q19: W=19e,
H19: W>19e.                                      (3.2)
```

`H19 intersect D(q0)` is the rank-one leaf of Section 2.  Every other cone
must retain the raw unloaded rows before division, as well as the target
that ties on its boundary.  The open intervals in (3.2) are rational
polyhedral cones after homogenizing by `e`; they are not integer contact
boxes.

Each cone in (3.2) must be refined by the parity valuations

```text
H_plus = min v(n2,n0),          H_minus=min v(u,n3),
2H_plus, H_plus+H_minus, 2H_minus,                 (3.3)
```

because the odd unloaded rows first see mixed even/odd products, while the
even rows can see the two squares.  A coefficient that vanishes sends its
valuation to infinity.  It must also be refined by the two first-normal
coefficient strata:

```text
S: r!=0, where Q0 is squarefree and Q0|N^2 forces N=0;
R: r=0,  where the cubic null module is
         k*z*(z^2+p).                              (3.4)
```

On `R`, a leading coefficient in that null module does not advance the
nominal valuation `W`; it starts a correction recursion.  Formula
(1.4)--(1.5) is the first mandatory transition in that recursion.  The
state of a fan leaf must therefore include the raw predecessor ideal and
its null-module label, not just the weight vector.

The immediately live middle object is the correction-complete union

```text
14e <= 2H <= 19e,                                  (3.5)
```

with the target-wall, parity, `S/R`, `q0!=0/A`, and boundary refinements
above.  It is finite at the level of initial supports, but no emptiness
claim follows until every cone has a two-sided source-equivalent chart.

## 4. The `A`-face live charts

Put

```text
A=5D+2s,                    a=v(c),       d=v(A).   (4.1)
```

When all normal contributions are absent through `19e`, the normalized
odd support gives the primitive leading balance

```text
d=2a,                       3a=5e,
(e,a,d)=(3,5,10).                                  (4.2)
```

Equation (4.2) remains a valid Newton-ray label.  It is **not** an empty
leaf: a source client must retain every correction at the intervening
uniformizer grades and continue through `sigma^57`.  The repaired cubic
producer supplies initial-form identities and omission controls only.

The audit exposes a second mandatory `A` state on the repeated-root stratum:

```text
r=0,              H=5e,
N_H=v*z*(z^2+p),                                 (4.3)
```

because in (1.6) the leading odd normal has valuation `15=5e`.  Its nominal
quadratic at `10e` is polynomial and hence invisible to the tails.  The
next state includes (1.3)--(1.5), and then all arbitrary `sigma` corrections
through grade `57`.  This `A/R/H=5e` chart lies in the nominal predecessor
cone `P0`, so merely routing `P0` to the first-normal UFD test is not a
closure argument.

More generally, every repeated-root first-normal null direction in `P0`
must remain live until a source theorem proves that its valuation is forced
to (4.3) or supplies the additional finite cone labels.  V2 makes no such
reduction.  The minimum immediate AWS target is the exact primitive chart
(4.2)--(4.3), with the `m0=v*x/2` positive control and all grades through
`57`; it must not specialize away higher normal, tangent, load, or target
jets.

## 5. Corrected exhaustiveness requirement

A useful fixed-ray theorem must prove all of the following.

1. **Literal support.**  Emit the complete source through the relevant
   terminal grade and list every valuation form.  The list must contain at
   least (3.1), (3.3), the generic `c` column, the `A*c` and `c^3` modes,
   and every mixed term generated by a repeated-root null coefficient and
   its corrections.
2. **Finite fan.**  Build the rational polyhedral fan of that literal
   support and a finite Hilbert-basis list after arbitrary ramification.
   The coarse cells (3.2) and refinements (3.3)--(3.4) are mandatory
   sentinels, not a proof that no further support wall exists.
3. **Source-equivalent charts.**  Give a two-sided flat Rees chart for every
   cone, retaining the complete nonreduced predecessor ideal, all loads and
   targets, and every coefficient correction.  Projection of quotient
   variables is forbidden.
4. **Null transitions.**  Whenever an initial coefficient lies in a UFD
   null module, compute the next source grade rather than declaring the
   nominal cone empty.  Equations (1.4)--(1.5) are the first regression
   test.
5. **Overlap and arc coverage.**  Check pairwise chart overlaps and prove
   that their union covers the original unit-`J`, `D(K10*D)` arc functor,
   including nilpotents and ramified arcs.

Only after those five items may the rank-one `H19` leaf, any middle-cone
Fitting units, and any correction-complete `A` residual be united into a
fixed delayed-load ray theorem.

## 6. Immediate source client

The smallest proof-discriminating client is not another normalized cubic
solve.  On AWS, compile the primitive `A/R/H=5e` chart through `sigma^57`
from the frozen `Phi_l` rows and retain:

```text
K(sigma)              every quartic tangent jet,
C-K(sigma)^2          all four normal jets,
K10,K6,K2             every allowed delayed-load jet from sigma^42,
mu2,mu4,mu6,J         target jets at sigma^42,48,54,57,
the ordinary Faber connection at every grade.       (6.1)
```

The required positive control is (1.4)--(1.5).  The required negative
control omits `m0` and reproduces the false residual
`-(3/8)*v^2*x`.  A mathematical endpoint is either a raw localized unit or
a frozen survivor with its complete correction series; timeout and solver
failure are no verdict.

In parallel, the middle-cone compiler should instantiate the finite walls
in (3.2), beginning with `Q19` because it directly tests whether the first
unloaded normal row can carry the unit terminal on the `K` resonance.

## 7. Firewall

The exact delayed-load identities, normalized block `M`, row-seven vector,
and rank-one Fitting formulas remain design inputs.  Section 2 gives only a
conditional source replay on the strict high-contact open.  This repair
does not prove the finite fan exhaustive, eliminate `A`, eliminate the
middle cone, or classify repeated-root null towers.  It does not cover
unequal effective load valuations, positive capitalized-`J` valuation,
`K10=0`, `D=0`, terminal `[6,2]`, or either finite Taylor family.  It does
not close the square branch, order two, `(8,12)`, maximum twelve, or JC2.
