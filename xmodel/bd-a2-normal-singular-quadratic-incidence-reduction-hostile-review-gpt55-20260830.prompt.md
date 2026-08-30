# Hostile review: normal singular quadratic incidence reduction

You are GPT-5.5 xhigh, an independent hostile algebraic-geometric reviewer
for the plane Jacobian-conjecture campaign. Work in
`/Users/dc/code/math/jc2` on frozen git basis
`296bc55f8bd94b258337a874c94fc70c95b384a0`.

Read and review this sealed exact provisional producer in full:

```text
f7d1c8cb42d5afd29474eb0975ffae518b0c82620f598649c2ac3d5d59064f94
  xmodel/bd-a2-normal-singular-quadratic-incidence-reduction-sol56-20260830.md
  body 19112 / b2a5c3b5e063333abd544be5c6a5d4b4b6dff1cd9a362b3471160a395ef03fea
  manifest 3a868fca72c94509ae0ae522447092d9fcd7da818e9fd0a7270b1e8512855f3d
```

Its frozen authorship basis is `145f96d65021ef364a5189c4ca385fe09d7b4f46`;
its producer commit is the review basis above. Read every charged input named
in Section 0 and enforce its exact scope.

Independently reconstruct and attack:

1. Compute all cohomology in the hypersurface sequence. Audit the Leray
   five-term bridge and exactly what is needed to conclude rational
   singularities; reject any use of `H^1(O_X)=H^2(O_X)=0` alone.
2. Check both rationality routes. For the conic route, prove or refute that
   normality forces the generic plane conic to be smooth, including rank-two
   and rank-one generic quadrics; then check Tsen, extension of a rational
   point to a section, connected fibres, and rationality of the resolution.
3. Verify Gorenstein+rational=>Du Val, crepancy, `K=-A+B`, `K^2=-1`,
   `e=13`, and `rho=11`, with all characteristic-zero and normality inputs.
4. Rebuild the relative MMP over `P1`: absence of multiple fibres, contraction
   of vertical `-1` curves, endpoint `F_e`, exactly nine blowups (including
   infinitely near centres), and the integral total-transform NS basis.
   Check `A=2S+(e+3)F-sum E_i` and the claimed bound `0<=e<=3`.
5. Derive the orthogonal complement integrally. Audit primitivity of
   `<A,F>`, the parity condition, determinant/discriminant form, and the exact
   isometry to `D9(-1)`. In particular test whether `E8(-1) direct-sum <-4>`
   or a hidden overlattice remains possible, and check the root-count argument
   excluding an `E8` exceptional singularity.
6. Audit the normal-surface ramification section and connectedness of an
   effective ample Cartier divisor. Verify the equality between the
   ramification divisor of `pi o r` and the total Cartier pullback, occurrence
   of every exceptional curve, and all intersection numbers.
7. Check the local ADE equations `n=C_ADE m`, including signs, positivity,
   why every `m_i>=1`, and why `n` is nonzero. Decide exactly what these data
   do and do not imply about physical boundary attachments.
8. State the maximum theorem safe to promote and the smallest finite successor.
   Keep nonnormal incidences, effectivity/classification of ADE-decorated
   infinity/different, basis coverage, polynomial maps, counterexamples, and
   JC2 separate.

Return an itemized verdict (`CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or
`REFUTED`), precise repairs, and cheapest decisive successors. Hard cap: 8,000
tokens and 28,000 UTF-8 bytes. Do not inspect, list, search, stat, build,
modify, or control `jc2-lean`; the process sandbox also enforces this. Do not
run local heavy CAS or Singular. Do not edit inputs, canonical files, scripts,
or dependencies. Write exactly one report:

```text
xmodel/bd-a2-normal-singular-quadratic-incidence-reduction-hostile-review-gpt55-20260830.md
```

End with one standalone `<!-- BODY-END -->` line and no seal block.
