# Preregistration: simultaneous `beta=5` equality face

Fix the same exact cubic, loads, and eight-row finite coefficient ideal as
control 2. Use primitive integral weight

```text
(Lambda,tau,rho,q1,q0,r2,r1,r0)=(4,1,1,20,20,30,30,30),
```

the `alpha=15/2, beta=5` boundary where all six nontrivial witness walls meet.
The face initial form of the explicit witness has seven terms: `Lambda^20`,
`q1*q0^3`, and the five `q*r*r` monomials; `Lambda^20*tau` is higher.

Compile the complete expanded rows directly from the pinned independent
reconstruction. Race two exact contractions:

- A: direct `sat(I,<s>)`, global `dp`, then direct torus saturation;
- B: inverse `u*s-1` contraction and inverse `v*TORUS-1` localization in an
  `lp/dp` block order.

Both must verify membership of the seven-term witness face in the full
special fibre, report whether the entire eight-coordinate torus localization
is unit, and separately report survival of the formerly displayed residue.
Unit excludes the whole face/support; nonunit is a survivor variety requiring
further classification. Disagreement or any hash/parser/CAS/rc/resource
failure is inconclusive. This is only the simultaneous control-2 boundary,
not every witness facet or the full Newton fan.
