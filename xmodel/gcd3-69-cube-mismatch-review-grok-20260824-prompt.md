# Hostile different-model review — GCD3 `(6,9)` cube-mismatch gate

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`1e4480c14f2ab9c4145eb6f6c74f0ac348baf76a`, with frozen uncommitted
artifacts on top. Read in full:

- `xmodel/gcd3-69-cube-mismatch-gate-20260824.md`;
- every payload named in
  `cases/gcd3_69_cube_mismatch_gate_20260824/FREEZE.sha256`;
- the frozen first common-cubic producer/review and the target-translation
  erratum/review on which this successor depends.

Frozen hashes:

- producer report:
  `6a2799dfe46828c70462d51a842a3fc0adf0515b8ded7a576cdb837d81847d20`;
- preregistration:
  `acec70acf71b187ec953df9977b23ad04d3df9f0f6582fc37a166b34115be48d`;
- exact replay:
  `39246c1329c534adce2339ca940962cbb83951d7044b4888a8c7ea04fbd514dd`;
- manifest:
  `3bca39faee225aef205b909914ff39594088ab0dcc19ec911466a053e63be5b5`;
- freeze file:
  `48bf4432f17be451291117e5fbc4a1545640f3bbb6aa18cd5fbd9232e4d20684`.

Verify the freeze and rerun the registered replay. Then independently attack
every load-bearing statement:

1. **Source normalization and scope.** Starting from cube core `h=s^3`,
   reconstruct the depression `z=sy+r`, `d=-delta/2`, and
   `J_(x,y)=s J_(x,z)`. Check that no polynomial source automorphism is being
   inferred and that the full boundary-jet conditions
   `s^ell f^(ell)(r)/ell! in k[x]` and their g analogues are retained.
   Distinguish `d!=0`, the separate `d=0` cube core, and the previously
   excluded aligned nontrivial-Kummer branch.
2. **Complete Faber high-row form.** By a second exact implementation or
   independent triangular integration, prove or refute that all eight high
   rows and only those solutions have
   `g=[H(f^(1/6))]_+`, with all nine constants
   `d,c7,c6,c5,c4,c3,c2,c1,c0` before quotient. Check all omitted lower
   Faber coefficients, not only the four displayed b-rows, and ensure no
   Kummer weight vanishing is smuggled into the cube core.
3. **Target quotient.** Independently derive the full action of `P->P+q` on
   `a0,c3,c2,c1,c0`, as well as the Q-shear and Q-translation. Verify the
   `d!=0` invariants `8d*c3-9c2` and `8d*c1-7c7*c2`; verify that division by
   d is avoided at `d=0` and that `9c1-7c7*c3` is invariant there. Attack
   whether any retained target operation violates the frozen degree/monicity
   pins or a source/target-value pin.
4. **Five lower rows.** Reconstruct the negative Laurent coefficients
   `r1,...,r5` and independently derive
   `A1,...,A5`, including determinant `6^5`. Decide whether the remaining
   Keller equation is genuinely equivalent to
   `r1'=...=r4'=0, 6r5'=j/s`, rather than a necessary projection. Check signs
   in the fixed-w derivative and all possible contributions from deeper
   Laurent terms.
5. **Finite-pole theorem.** Audit every valuation and divisor step proving
   that rational exactness of `dx/s`, for polynomial nonconstant s, forces
   `s=C(x-a)^m`, `m>=2`, and the stated formula for r5. Explicitly test
   simple roots, multiple roots, infinity, constants, and degree one. Check
   that `r5 in k(x)` is licensed and identify precisely where the boundary
   equations—not just the r-invariants—control possible poles of the
   coefficient path.
6. **Controls and exceptional strata.** Independently recompute the regular
   local point, its five-by-five determinant and terminal velocity. Audit
   the weighted d-deformation ranks and the DS first correction. Decide
   whether these only prove local formal survival and failure of ordinary
   first-order arcs, leaving ramified/Puiseux arcs and polynomiality open.
7. **Logical closure.** Try hard to close or break the frozen survivor, but
   do not silently add hypotheses. Decide whether the strongest licensed
   conclusion is only the Faber–Laurent reduction plus the constant/single-
   root-core dichotomy. Explicitly attack any inference to d-nonzero
   emptiness, d-zero emptiness, full `(6,9)` exclusion, a Keller pair, or
   JC2. State the smallest exact successor, including whether constant-s,
   monomial-s, d-zero, and ramified common strata must be separate.

Use exact arithmetic throughout; producer replay plus prose comparison is
not independent evidence. Do not edit producer, case, canonical, ladder, or
erratum files and do not launch AWS. Write exactly one report:

`xmodel/gcd3-69-cube-mismatch-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
hashes, independent derivations, the smallest failing identity if any,
precise promotion scope, and quarantine language at both ends.
