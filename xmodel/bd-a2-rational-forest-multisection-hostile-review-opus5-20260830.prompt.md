# Bounded hostile review: rational-forest first-leg gate

You are Opus 5, an independent hostile mathematical reviewer for the plane
Jacobian-conjecture campaign. Work in `/Users/dc/code/math/jc2` on frozen git
basis `a619157b73c1dee1ca0599db47321ffd7588d748`.

Review this sealed producer in full at its stated narrow scope:

```text
367d8ffa1a374b25ee27ca2a2079721c6b17bd71980a13687b11aa87e86f2986
  xmodel/bd-a2-firstleg-rational-forest-multisection-producer-sol56-20260830.md
  body 8578 / 42aedb00e89804034c3a16f3205c12e18e14133cd9d0dc0189b7e286428ecf64
ff25ba27388c02698013483e2e5537f18ed39e918e5cb0cb4c099a75ef42f298
  xmodel/bd-a2-firstleg-log-kodaira-coordinator-integration-sol56-20260830.md
```

Independently reconstruct and adversarially check:

1. For smooth projective `X` and reduced SNC `D`, derive from residue,
   normalization, and Serre duality
   `barP1=p_g+tau(D)-rank(partial)`, where
   `tau=sum genus(D_i)+b1(dual multigraph)`. Check disconnected divisors and
   parallel edges. Verify the bounds and equality when `q(X)=0`.
2. If a dominant `A2->X\D` exists, justify the rational extension
   `P2 --> X`, unirationality, `p_g=q=0`, and injective pullback of logarithmic
   forms. Decide whether this forces every resolved boundary component to be
   rational and the dual graph a forest, with no missing hypothesis.
3. Audit the multisection bound `barP1 >= g+max(r-1,0)`, especially several
   analytic branches at one boundary point and paths sharing exceptional
   vertices. Check recovery of the reviewed two-section `n=1` formula.
4. Verify the sharp control
   `(P1_z x P1_w) minus ({w=infinity} union {z=w^k}) ~= A2` and the displayed
   coordinate map. Recompute the discrepancy/valuation formula and the
   tangent-two-branch losses `lambda_i=i-1`; keep unibranch cusps distinct.
5. For a smooth irreducible bidegree `(d,3)` incidence surface in
   `P2 x P1`, rederive `K=(d-3)A+B` and
   `p_g=(d-1)(d-2)` for `d>=3`, including restriction cohomology. State the
   presentation/basis dependence and every projective-closure exception.
6. For `d=2`, verify rationality of the smooth conic bundle, generic infinity
   bidegree `(2,3)` and genus two. On the projectively finite smooth locus,
   recompute `R_pi=2A+B`, `H=A`, the genera `2` and `9`, intersection `8`,
   and generic-SNC `barP1=18`. Separate reduced support from ramification and
   discriminant multiplicities.
7. Judge the exact safe nonlinear consequence. Do not promote all quadratic
   coefficients: nonreduced, singular-ambient, projective-basepoint,
   degree-drop, and rational-forest degeneration strata remain.

Return an itemized verdict (`CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or
`REFUTED`), the maximum exact theorem safe to promote, precise repairs, and
the cheapest next classification gate. No general cubic, primitivity,
map-existence, counterexample, or JC2 claim.

Hard output cap: at most 8,000 tokens and at most 28,000 UTF-8 bytes. Do not
restate long inputs. Do not inspect, list, search, stat, build, modify, or
control `jc2-lean`; the process sandbox also enforces this. Do not run local
heavy CAS or Singular. Do not edit any input, canonical file, script, or
dependency. Write exactly one report:

```text
xmodel/bd-a2-rational-forest-multisection-hostile-review-opus5-20260830.md
```

End with one standalone `<!-- BODY-END -->` line and no seal block.
