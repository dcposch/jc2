# Hostile review request: `(8,12)` order-four/order-two coefficient infinity

Act as an independent hostile mathematical reviewer.  Read the immutable
target and every charged source below in full.  Independently rederive or
break each bridge; do not use any producer conclusion or PASS string as
evidence.

Target (immutable):

```text
092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e  xmodel/max12-812-order24-coefficient-infinity-source-audit-20260825.md
```

Required charged sources:

```text
xmodel/as109-partial-y-history-stop-20260824.md
xmodel/max12-partial-y-kummer-preflight-20260824.md
xmodel/max12-partial-y-kummer-preflight-review-claude-20260824.md
xmodel/max12-partial-y-shared-faber-probe-20260824.md
xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md
xmodel/max12-general-faber-exceptional-support-mason-20260825.md
xmodel/max12-general-faber-exceptional-support-mason-review-20260825.md
xmodel/max12-general-faber-exceptional-support-mason-review-grok-20260825.md
```

Audit every load-bearing point, especially:

1. Starting from `a_8=h^2,b_12=h^3,u^4=h` and Kummer class order
   `e=4` or `e=2`, verify the depression, the character of each coefficient,
   Faber constant, and tail.  Check that the target gauges really give
   `g=F12` for `e=4` and exactly the additional `F10,F6,F2` terms for `e=2`.
   Check the complete target-load lists and `8r7'=j/u`.
2. Put `H=4U`, `q=1/x`, and audit both minimal Kummer fields at infinity.
   Is the cover unramified?  Is `t=q^Uu` a unit on a selected sheet?  Does
   `dR7/dq=-(j/8)q^(U-2)t^-1` follow, and does its nonzero residue really
   exclude every nontrivial `H=4` client?  Challenge the finite
   multiplicity-four remark and the claim that all target loads are regular
   for `U>=2`.
3. Recompute the bounded-pole theorem without importing `(9,12)`: the
   source shear making `R0` regular, every coefficient pole estimate for P
   and the full order-two-loaded Q, exact total degrees
   `(8(U+1),12(U+1))`, gcd `4(U+1)`, and the precise GGV consequence.  In
   particular attack the claim that only `U<=2` is closed and that the
   `U>=3` bounded sector remains live.
4. Check the explicit local character descent (including all signs/residue
   exponents), the ordinary etale-sheet equivalence, and the claimed deck
   action `(p,c,r)->(zeta^2p,zeta^3c,r)` / `(p,-c,r)`.  Decide whether this
   theoretical source typing is sufficient despite the absence of an
   `(8,12)` concrete compiler.
5. Verify the tail weights `12+ell`, lower-load weights `2,6,10`, every
   exponent in the Rees equations, and the strict substitution
   `Lambda=q^(U+1)rho`.  Check the order of saturations and the exact logical
   strength of the unit-ideal implication.
6. Independently expand the common-quartic graph, its triangular normal
   coordinates, the `P(2,3,4)` chart cover, and the rational slope
   denominator classification.  Keep Kummer order `e` separate from Rees
   denominator `n`; find any missing projective stratum or cancellation.
7. Check the vanishing first differential of the tail map along `f=K^2`
   and in each order-two Faber-load direction.  Do not promote reduced
   support to reducedness, finite determinacy, lifting, Taylor realization,
   cell closure, or JC2.

Write exactly one report:

```text
xmodel/max12-812-order24-coefficient-infinity-review-grok-20260825.md
```

Include the exact target SHA, model identity, explicit verdict
`CONFIRMED`, `REPAIR`, or `REFUTED`, the smallest failing identity or
missing hypothesis, a full independent proof/attack, and a strict scope
firewall.  Do not edit any other file.  This is source reading and hand
derivation only: run no CAS, solver, substantive Python, Lean, or other
heavy local computation.
