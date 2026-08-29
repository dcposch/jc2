# Adjudication V2: explicit higher-jet falsifier for delayed-load `A` review

Work in `/Users/dc/code/math/jc2`.  A prior Grok review at SHA
`0dca581aa2b2e65b964b701695b094c93a2197789e95757066c0b0384e366e4c`
returned `CONFIRMED` on producer SHA
`9419c08b4be09fee8ecae9b73c8c9c610770a7166e17a973251312d28b69a695`.
Adversarially review that verdict against the exact countercertificate:

```text
2ca188fc31a1889ecaba5434d927b691f4569a8e986d5a79779a34925ee0e69a
  cases/max12_812_order2_affine_faber_a_source_early_null_20260826/RESULT.md
2db358d86a6a146b23a1a7b635d50761b83611e0493291e2e8540ae25dfaf79e
  cases/max12_812_order2_affine_faber_a_source_early_null_20260826/EVIDENCE.sha256
dfb1cc84f4fb30c198dc646ba4416b5cc118b9d74cebead302db9b428594e7b8
  xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-independent-audit-20260826.md
```

Write exactly one report to

```text
xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-review-adjudication-grok-v2-20260826.md
```

Edit no other file and do not touch `jc2-lean`.  Use no CAS.  Do not trust
either verdict token.  Independently expand, on `r=0`,

```text
Q0=z^2(z^2+p), N3=vz(z^2+p),
Q=Q0+t*x*z+O(t^2), E=t^3N3+t^4N4+O(t^5),
N4=m3z^3+m2z^2+m1z+m0
```

and calculate `[t^7 z^-1](3/8 E^2/Q)`.  Decide whether `m0=v*x/2` is a
legal higher coefficient after the leading normalized coordinate `e0=0`,
whether parity or a DVR forbids it, and whether a later normalized `A5`
unit can be imposed without solving all intermediate source grades through
`sigma^57`.  Rehash the charged result/evidence and state whether its dual
exact rows directly contradict the prior review's correction-completeness
claim.

Preserve every exact identity that still survives and give the narrowest
valid theorem.  End with exactly one standalone token:
`PRIOR_REVIEW_VALID`, `PRIOR_REVIEW_REPAIR`, or `PRIOR_REVIEW_REFUTED`.
