# Hostile scope review: fixed-total-D12 classical closure

Date: 2026-08-25  
Reviewer: AS owner (independent replacement for the quota-failed Claude lane)  
Target: `xmodel/sol-fixed-total-d12-classical-closure-v2-20260825.md`  
Target SHA-256: `def1c2a141a6843f11886940d1a9c71f09adba0edee1088cbcbf0fa0c693c4a8`

## Verdict

**CONFIRMED.**  The target's corrected broad-envelope conclusion is valid:
every characteristic-zero Keller pair with
`deg_total(P),deg_total(Q) <= 12` is an automorphism.  This closes every
finite fixed-total-D12 B8/B9 envelope as a counterexample client, not merely
the exact degree pairs `(9,12)` and `(8,12)`.  Only the partial-`y` families
with unbounded coefficient-`x` degree (hence unbounded total degree) remain
outside this classical closure argument.

## Primary-source check

Guccione--Guccione--Valqui, arXiv:1401.1784v3, explicitly begin with an
arbitrary field `K` of characteristic zero and define the plane Jacobian
conjecture for pairs `P,Q in K[x,y]` with nonzero constant Jacobian; see the
[Introduction, lines 51--54](https://arxiv.org/html/1401.1784v3).  Their
abstract states the Heitmann condition

```text
gcd(deg(P), deg(Q)) >= 16
```

for every counterexample; the Introduction then defines `B` using
`v_(1,1)`, i.e. ordinary total degrees, and records `B >= 16`; see
[lines 63--66](https://arxiv.org/html/1401.1784v3).

Thus for a Keller pair in any total-D12 envelope, both coordinates are
nonconstant and

```text
1 <= gcd(deg_total(P),deg_total(Q)) <= 12 < 16.
```

It cannot be a counterexample.  This argument does not require the actual
degree pair to equal the partial-`y` bounds, nor any leading-form or
common-core hypothesis.  In particular the broad B9 cell
`deg_total(P)<=11, deg_total(Q)<=12`, the broad B8 D12 cell, and every
degree-drop stratum inside them are all closed.  The exact pairs `(9,12)` and
`(8,12)` merely give the stronger numerical controls `gcd=3` and `gcd=4`.

The field scope is also correct.  The paper states the theorem over arbitrary
characteristic-zero `K`, so it applies directly to `Q_3` and its finite
extensions; no algebraic-closure-only hypothesis is being smuggled in.

## Firewall

This review confirms only the classical routing implication and the target's
conditional compactness consequence for a *single fixed nested complete
scheme*.  It does not provide an effective death depth, join unrelated
finite-precision points into a tower, validate an incomplete carry scheme,
or close a family with bounded partial-`y` degree but unbounded total degree.
Completed fixed-D12 Kuranishi calculations remain valid method/custody
controls, but they are not live JC2 counterexample searches.
