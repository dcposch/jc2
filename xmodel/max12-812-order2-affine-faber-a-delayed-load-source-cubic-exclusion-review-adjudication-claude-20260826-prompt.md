# Adjudication assignment: conflicting reviews of delayed-load `A` exclusion

Work in `/Users/dc/code/math/jc2`.  Adjudicate the conflict between:

```text
9419c08b4be09fee8ecae9b73c8c9c610770a7166e17a973251312d28b69a695
  xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-20260826.md

0dca581aa2b2e65b964b701695b094c93a2197789e95757066c0b0384e366e4c
  xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-hostile-review-grok-20260826.md

dfb1cc84f4fb30c198dc646ba4416b5cc118b9d74cebead302db9b428594e7b8
  xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-independent-audit-20260826.md

2ca188fc31a1889ecaba5434d927b691f4569a8e986d5a79779a34925ee0e69a
  cases/max12_812_order2_affine_faber_a_source_early_null_20260826/RESULT.md

2db358d86a6a146b23a1a7b635d50761b83611e0493291e2e8540ae25dfaf79e
  cases/max12_812_order2_affine_faber_a_source_early_null_20260826/EVIDENCE.sha256

9f91fe43300017ef09f3886def02a5c16769d7a70778d993f32ca35646eec044
  xmodel/max12-812-order2-affine-faber-total-rees-fitting-import-design-v2-repair-20260826.md
```

Write exactly one report to

```text
xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-review-adjudication-claude-20260826.md
```

Do not edit another file and do not touch `jc2-lean`.  Do not use Singular,
Sage, SymPy, msolve, Lean, or another CAS.  This is an exact hand
adjudication; producer/reviewer verdict tokens are not evidence.

The decisive question is correction completeness.  On `r=0`, independently
expand

```text
Q0=z^2*(z^2+p),
N3=v*z*(z^2+p),
Q(t)=Q0+t*x*z+O(t^2),
E(t)=t^3*N3+t^4*N4+O(t^5),
N4=m3*z^3+m2*z^2+m1*z+m0
```

in the unloaded quadratic receiver `(3/8)E^2/Q(t)`.  Determine the exact
negative `z^-1` coefficient at `t^7` and whether the legal source jet
`m0=v*x/2` cancels it.  Check whether leading `e0=0`, parity, a DVR/domain
argument, or the later normalized `A5` residual forbids that higher jet.
Distinguish a fixed no-further-correction initial form from a formal source
arc with all intermediate `sigma` jets through the loaded and terminal
grades.

Also identify the strongest statements that remain correct: load timing,
first-normal UFD split, printed normalized cubic identities, and direct
rejection of the frozen squarefree rational witness.  Explicitly decide
whether the Grok `CONFIRMED` review is itself valid, or must be quarantined.

End with exactly one standalone adjudication token:
`GROK_CONFIRMED_VALID`, `GROK_REVIEW_REPAIR`, or `GROK_REVIEW_REFUTED`.
