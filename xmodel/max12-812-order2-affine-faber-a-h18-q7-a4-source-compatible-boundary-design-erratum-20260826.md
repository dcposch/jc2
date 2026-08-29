# Erratum: H18/q7/a4 is normalized navigation, not source-compatible

Date: 2026-08-26

Status: **CONTROLLING SCOPE ERRATUM FOR DESIGN SHA
`824b7c80898fe99ef4b598f0a51e21b3f6da2fc56cb0563425f539ab04a274d9`.**

The predecessor design correctly registers a complete normalized
H18/q7/a4 grade-54 computation, but its title and Section 1 overstate
source compatibility.

On the balanced integer slope-four ray, the exact coefficient map puts
not only the monic-square remainder `Delta`, but also the unsplit affine
coordinates

```text
a,E,U,V,R0,W0,M
```

in the literal completed source field `L((tau))`.  After
`tau=s^3,sigma=s^4`, every nonzero finite `sigma`-order of one of these
source-defined coordinates must therefore be divisible by three.  The
H18/q7/a4 cell violates this twice:

```text
ord_sigma(U or V)=7,       ord_sigma(a)=4.
```

Thus the dual-AWS grade-54 client remains a valid normalized support and
software control, but it cannot be used as a rational-source successor on
the balanced slope-four ray.  No source, Taylor, order-two, or JC2 claim
may consume it.

On the equality wall `ord(a)=H-2q`, the first coordinatewise congruent
H18 candidate is

```text
(H,q,ord(a))=(18,6,6).
```

Even that candidate is only valuation-descent compatible.  A literal
global source must additionally keep the Faber loads and scalar targets
constant in the source coordinate and must satisfy both finite Taylor
families.  Those constraints are not consequences of valuation
congruence.
