# Research lane: structural endgame for the 610 aligned-square chamber

Bounded primary research lane (paper mathematics; read-only). Find the
CLOSING argument for the `(6,10)` scale-two aligned-square chamber, in the
style that closed the 610 linear-root chamber (bounded h-adic tower →
ceiling → `ρ` polynomial vs `ρ' = j/h₀`) and the 68 terminal branch
(exact identity + two-case degree comparison). Order-by-order grinding has
produced many reductions without a `False`; the task is to find the
bounded/structural kill.

## Frozen input

Read at current `origin/master` of `dcposch/jc2-lean`, `max11-partial-y/`:
the committed aligned-square chain — `Grok610AlignedSquareFinalRowScratch`
(exhausted packet + root residual `p₀'(a)q₁(a) − p₁(a)q₀'(a) = j ≠ 0`),
`Grok610AlignedSquareEndgameScratch` (the two-limb split `w₁(a)=0 ∨ (μ=0 ∧
e₁(a)=0)`), `Grok610AlignedSquareNinthLoadsScratch` (the two ninth-load
objects with explicit heads and per-limb residuals), and
`Grok610AlignedSquareMixedPairScratch` (the mixed `(p₁,q₁)` reduction,
theorem `normalized610ScaleTwo_alignedSquare_mixedPairReduction` — an
existential packet with `h₀.natDegree = 1`, `h₀.eval a = 0`, first
integrals of weights 5/30/65/70, and the peeled coordinate ladder
`p₅ = h₀⁴w₁`, `p₄ = h₀²f₂`, `3f₂ − w₁² = h₀e₁`, …). Also the closed
sibling for the method: `Grok610DegreeZeroMixedArmClosureScratch`
(linear-root chamber, the ceiling endgame) and `Grok610PoleCeilingLemmaScratch`.

Setting: scale two, `H = h₀²`, `deg h₀ = 1`, unique root `a`. The Keller
row is inhomogeneous with constant `j ≠ 0`; the aligned first integrals
(weights 5,30,65,70) are the conserved quantities; the coordinate ladder
peels successive `h₀`-powers off `p₅,p₄,…` and `q₉,…`.

## Questions

1. **Is there a bounded tower here too?** The linear-root chamber closed
   because the jet quotient had `h`-degree ≤ 6, so the pole tower
   terminated and `ρ` became a polynomial contradicting `ρ' = j/h₀`.
   Does the aligned-square chamber admit the same structure — a primitive
   whose derivative is `j/h₀` (or `j/h₀^k`) with a computable clearing
   power bounding the peel ladder? If so, state the clearing power, the
   pole order, and the ceiling, and show the peel ladder cannot continue
   past it without forcing `ρ` polynomial.
2. **Or an exact-identity kill?** The 68 terminal branch closed via
   `3dZ + BU − 18γB² + C(C₀) = 0` and a two-case degree comparison. Is
   there an analogous exact polynomial identity among the aligned first
   integrals (weights 5/30/65/70), the coordinate ladder, and the Keller
   row whose two degree cases are both impossible? The conserved weights
   are the natural ingredients.
3. **The `w₁(a)=0` vs `(μ=0 ∧ e₁(a)=0)` limbs.** For each limb, the
   ninth-load residuals are known (`(e₃−6e₁ₙw₁)³ + 9v²w₁ = 0` on μ=0; a
   `(p₂,e₁)` quadratic on w₁=0). Does one more conserved-weight relation
   force `v(a)=0` (μ=0 limb) or collapse the quadratic (w₁=0 limb), and
   then does the Keller row `p₀'q₁ − p₁q₀' = j` at `a` become `0 = j`?
   Trace exactly which peeled coordinates enter `p₀',p₁,q₀',q₁` at `a`.

## Report

`xmodel/max11-610-aligned-square-endgame-grok46-20260901.md`, verdict
`DERIVED` (a referee-checkable closing argument), `PARTIAL` (the exact
missing object named), or `BLOCKED` (a consistent model of the reduced
packet, proving more input is needed). Show all computations; UNVERIFIED
labels where sources could not be read. No overclaims.
