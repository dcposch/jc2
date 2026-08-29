# Hostile review prompt: two-fibre decision for the total ordered-`a1` chart

Date: 2026-08-27

Act as an adversarial commutative algebraist.  Review the new theorem proposed
in §3.1 and Card F1 of

`xmodel/ideation-20260827T0935Z-fable5.md`

SHA-256

`098b81d19cba6f278e93a809e60a3a4892eea7979758ffe6b0bb2997163b98c0`.

Do not accept the navigation conclusion merely because its constituent total-
rho criterion is already reviewed.

## Charged setting

Let `S=Q[rho,X]`, where every variable in `X` has strictly positive pinned
weight and `rho` has weight zero.  Let `J` be the literal homogeneous total
ordered-`a1` ideal through grade 19 and `K=J:a1^infinity`.  The reviewed
criterion says

```text
K+(rho)=(1)
 iff some a1^N U(rho^2) lies in J with U(0)=1.
```

The candidate sets

```text
T={u(rho) in Q[rho] : u(0) != 0},  S'=T^-1 S
```

and claims the exact equivalences

```text
K+(rho)=(1)
 iff a1 in sqrt(J*S')
 iff [a1 in sqrt(J*Q(rho)[X])] and [a1 in sqrt(J0)]
 iff J|_(a1=1)=(1) over Q(rho) and J0|_(a1=1)=(1) over Q,
```

where `J0=J|_(rho=0)`.  Since a genuine 17-row subideal of the second
dehomogenized ideal is already the unit ideal, it concludes that the one
remaining decisive computation is the *full* dehomogenized generic fibre
over `Q(rho)`.

## Mandatory attacks

1. Prove or refute every equivalence.  Classify primes of `T^-1Q[rho]` and
   check whether contractions `(0)` and `(rho)` really suffice; look for
   embedded primes, vertical fibres at `rho=c!=0`, nilpotents, or failure of
   radical membership to descend/ascend.
2. Compare `a1 in sqrt(J*S')` with `K+(rho)=(1)` directly.  Track denominator
   clearing, saturation exponents, and the positive-weight projection.  Decide
   whether the even factor `U(rho^2)` follows from the reviewed symmetry or is
   an extra hidden hypothesis.
3. Audit the dehomogenization step over non-algebraically-closed `Q(rho)`.
   Check weighted scaling when `wt(a1)=5`, faithful-flat descent from an
   algebraic closure, and whether `a1=1` is a valid slice for radical
   membership.
4. Verify that a selected 17-row *subideal* becoming `(1)` after
   `rho=0,a1=1` soundly proves the full special-fibre condition.  Check that
   those rows are literal members of `J0` and do not import localization,
   chart bilinears, or a stale alphabet.
5. Attack the claimed computational consequences.  A selected-row generic
   unit is one-sided decisive; a selected-row nonunit is not.  Determine
   whether a full-system generic nonunit is genuinely decisive for the frozen
   chart, and whether a full-system unit requires an explicit certificate
   before promotion.
6. Check the toy example and construct counterexamples to any overstrong
   version.  Distinguish the frozen grade-through-19 chart from an all-depth
   source and from Gate T.

Give line-item verdicts `CONFIRMED`, `REPAIRABLE`, or `REFUTED`, identify the
smallest failing implication/hypothesis, and state the strongest exact theorem
and safe compute plan.  No heavy local CAS, AWS launch, web sweep, canonical
ledger edits, or access of any kind to `jc2-lean`.

Write the complete report to exactly
`xmodel/max12-812-order2-p0-total-rees-j2-a1-two-fibre-generic-eliminant-hostile-review-grok-20260827.md`.
Touch no other campaign artifact.
