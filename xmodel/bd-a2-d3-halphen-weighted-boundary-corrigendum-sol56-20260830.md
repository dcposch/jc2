# Corrigendum: D3 weighted-boundary wording and interface

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `ae7d44ea2148980fb1e2d3bd12c413041a0d25d4`  
Lifecycle: **EXACT PRODUCER CORRIGENDUM / NO VERDICT CHANGE**

## 0. Disposition

This packet corrects five overbroad or ambiguous sentences in

```text
58173d4f18a575ca49164fafef91b7ba8b50e670c9e8a39376d55bb647732e2f
  xmodel/bd-a2-d3-halphen-weighted-boundary-obstruction-sol56-20260830.md
```

Its exact weighted face, Hesse quotient, boundary invariant and conditional
row-elimination verdict are unchanged.

## 1. Corrected wording

1. In Section 0, replace "the unique singular point" by "the marked unique
   GR-defect/non-Du-Val point."  The one-point row permits additional Du Val
   singularities; the proof neither excludes nor uses them.
2. In Section 0, read "actual normal finite incidence" as "actual normal
   incidence, locally finite at the marked point."  The proof uses the local
   monic equation `F(t;0,0,1)=s^3t^3`, `s!=0`.  It makes no independent claim
   that an arbitrary projective closure is globally finite.  In the actual
   affine proper block, `g2` is separately promoted finite flat.
3. In Section 3, delete "normalized" from "the normalized weighted strict
   transform is an integral normal surface."  The displayed `S2+R1` argument
   proves that the weighted strict transform itself is normal.  This matters
   because normalizing the exceptional divisor would erase the node one is
   tracking; no such divisor normalization occurs.
4. Replace "the only point on a weighted coordinate axis" by "the only
   weighted coordinate point lying on `C` is `[0:1:0]`."  This is the precise
   projective statement.  Its index-four chart is smooth on the curve and
   quotient resolution adds only rational trees.
5. Delete the sentence claiming that connectedness of a resolution fibre
   alone is equivalent to cycle persistence.  Use the preceding explicit
   local argument: parametric Morse reduction gives `uv+phi(r)=0`; integrality
   and normality force `phi=r^n` times a unit; the `A_(n-1)` resolution chain
   joins the two branches of the same globally irreducible nodal exceptional
   curve.  That chain plus the strict transform creates the cycle.  Later
   boundary blowups only subdivide it or add leaves.

## 2. Maximum-safe interface

If the marked center lies on fixed target infinity, it is boundary a
fortiori.  If it lies in the affine target, the nonzero `t^3` coefficient
makes the incidence monic and locally finite there; normality identifies this
finite germ with the actual intermediate block surface.  Its marked point is
singular and hence outside the image of the everywhere-defined étale first
leg.  The weighted exceptional genus/cycle is therefore genuine first-leg
boundary.

Accordingly the provisional theorem remains: conditional on the promoted D3
row and local gates, literal raw base degree three, and occurrence as the
actual morphic proper-block incidence, every `m=3,T=2t0` critical shard is
impossible.  Mere rational domination of an abstract class-`(3,3)` surface is
insufficient.  No other D3 row, block occurrence, polynomial map or JC2
conclusion follows.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3242`.
- Body SHA-256:
  `aa655872d1f33fa9efbca5768cf00dcdc751afb1753b8b8151cfc3c03e111092`.
- Frozen basis: `ae7d44ea2148980fb1e2d3bd12c413041a0d25d4`.
