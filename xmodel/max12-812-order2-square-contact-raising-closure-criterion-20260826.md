# `(8,12)` order-two square fan: contact-raising closure criterion

Date: 2026-08-26

Status: **FORMAL ARCWISE CLOSURE LEMMA / ACCEPTANCE CRITERION.  NO FAN
CERTIFICATES OR SQUARE-BRANCH VERDICT ARE ASSERTED HERE.**

## Why this criterion is needed

A calculation that makes one displayed leading coefficient vanish does not,
by itself, eliminate a formal arc.  It may only show that the contact order is
higher than the normalization used by that calculation.  Conversely, once a
parametric fan covers every finite contact vector, no infinite induction is
needed: a nonzero formal series already has a finite first order, and the
certificate for that order contradicts its nonzero initial coefficient.

The distinction prevents two opposite errors:

1. deleting the zero section by saturating a leading coefficient; and
2. demanding a separate computation at every integer contact order when one
   exact cone certificate is uniform on an unbounded polyhedral cell.

## Arcwise lemma

Let `K` be an algebraically closed characteristic-zero field and let
`R=K[[tau]]`.  Finite ramification causes no change: after replacing
`tau` by `sigma^e`, all rational orders become integral.  Let

```text
x=(x1,...,xn) in R^n
```

be the correction coordinates of a source-typed formal arc, and allow
`ord(xi)=infinity` when `xi=0`.  Suppose the following data have been proved
from the complete source rows.

1. A finite rational polyhedral fan covers every vector of finite orders in
   the registered domain.  Faces, not only maximal open cones, are included.
2. On each cone or face, the exact initial source ideal is formed after
   adjoining the leading units

   ```text
   xi=tau^vi*(ui+higher),  ui!=0
   ```

   for precisely the coordinates declared finite there.  No leading unit is
   silently set to zero or projected out.
3. After localization by the chart assumptions and by the product of those
   `ui`, the initial ideal is the unit ideal; equivalently, the raw initial
   equations force at least one supposedly nonzero `ui` to vanish.
4. Whenever the initial equations instead force a coordinate to be
   identically zero, the corresponding `ord=infinity` face is routed to an
   explicit lower-dimensional receiver.  Every root allocation and chart
   overlap is included in the cover.

Then every source-typed formal arc in the domain lies in one of the registered
`ord=infinity` receivers.  If those receivers are also empty after their own
source, terminal, and Taylor gates, the whole registered branch is empty.

### Proof

Assume an arc does not lie in an infinity receiver.  Every coordinate
declared nonzero on its support has a finite order and a nonzero leading
coefficient.  Its order vector lies in at least one closed fan face by (1).
Substitution into the complete source rows gives a point of that face's raw
initial scheme with every licensed `ui` nonzero by (2).  This contradicts the
localized unit certificate in (3).  Hence at least one coordinate has
infinite order and the arc is routed by (4).  Iterating only across the finite
set of coordinate supports terminates in a registered infinity receiver.
There is no iteration over the numerical contact order.

The same proof works before algebraic closure if each oriented root chart is
paired with its deck conjugate and descent is checked on overlaps.

## What counts as a uniform cone certificate

For an unbounded cell, sampling integer triples is not a certificate.  One of
the following is sufficient:

- a symbolic initial ideal whose generators are independent of the interior
  point after the cone inequalities are imposed;
- a finite residue-class split in the ramification index, with a symbolic
  certificate on every class;
- a homogeneous translation identity showing that shifting a contact order
  only multiplies the complete obstruction rows by a power of `tau` and does
  not change the localized initial scheme.

A radical containment `ui in radical(I)` is enough only after the same raw
ideal `I` is localized by all chart assumptions and by the other declared
leading units.  A reduced-support calculation made before the complete raw
initial ideal is not enough.

## Square-branch instantiation

For the current square campaign, the finite coordinates are drawn from

```text
A, R, C, k10, p-p0
```

and, on the exact-square receiver, from the lower loads and target rows.  The
unit-load fan uses the five primary lower functions in the companion
lower-hull lemma, with its one `RA2` boundary locus.  The positive-order-load
fan uses the seven-function candidate list there.  Opposite-root `AC` and
`RC` allocations are separate oriented charts.  The collision point `p=0`
uses value/derivative jets rather than the etale root chart.

Thus a future statement that “all finite contacts are raised away” is
licensed only when its evidence bundle contains:

1. an exact face/overlap coverage certificate for every rational contact
   vector, including moving-load and moving-`p` faces;
2. one source-typed localized initial-ideal endpoint for every distinct face
   module and root orientation;
3. an explicit routing table for every infinity support; and
4. terminal `[6,2]` and both Taylor polynomiality pullbacks for every
   surviving zero section.

The reviewed fixed-contact cubic separator supplies one face certificate; it
does not yet supply items 1--4.

## Scope firewall

This is a general implication from a completed source fan to formal-arc
coverage.  It neither proves that the current weight list is source-complete
nor supplies any missing face certificate.  It says nothing about landing of
all hypothetical Keller counterexamples into `(8,12)`, the remaining
maximum-twelve cells, or the global cofinal complexity ceiling.
