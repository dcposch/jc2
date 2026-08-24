# Hostile different-model review — GCD3 `(6,9)` coverage composition

You are the fresh independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`1e60fcedc8626650c7c7544ad296c3624173415f`. Read in full:

- `xmodel/gcd3-69-coverage-composition-20260824.md`;
- every payload named by
  `cases/gcd3_69_coverage_composition_20260824/FREEZE.sha256`;
- every producer/review pair in the composition report's dependency ledger.

Frozen hashes:

- producer report:
  `7eda0a469585247479d46c8f5f2ce95d2643ae8541f0d7f9c80e1c8537fffb0c`;
- registration:
  `b3d8cdec442d2199bfa973f10d2dcf67fb674cc9d8f359924d69236728a2db85`;
- replay:
  `6f255691fa348d0b458933aee01f2cc823298209a6a77ef0863ca06176dde30c`;
- manifest / freeze:
  `afe95b5fbd9ad6df3831e3c79a70137be5c5128c158d3a82bae8c761af17ee8a` /
  `9388b4cdd0b4ded3078cdce07fe1f30b8affd536a7f28c01c8fa914d92dbd87b`;
- canonical replay payload:
  `d7e030685c84e7c7366524e4b28f8516a5bf9d5060c3ebdba3990ca2e243ecd4`.

Verify the freeze from the repository root and rerun:

```text
shasum -a 256 -c cases/gcd3_69_coverage_composition_20260824/FREEZE.sha256
python3 cases/gcd3_69_coverage_composition_20260824/replay.py
```

Those checks are regression only. Independently and adversarially audit the
mathematical composition. A prose comparison or replay PASS is not enough.

1. **Exact landing and scope.** Starting from a characteristic-zero Keller
   pair of actual partial `y`-degrees `(6,9)` in the `3|H` residue, verify
   that the reviewed history and first common-cubic theorem really emit every
   premise consumed here: `a6=alpha*h^2`, `b9=beta*h^3`, `s^3=h`, constant
   `delta=3A-2B`, the original Taylor boundaries, and all needed jets. Check
   that target swaps/scalings and extension to an algebraic closure preserve
   actual degrees and boundaries. Distinguish coefficient-field depression
   from a polynomial source automorphism.
2. **Exhaustive field dichotomy.** Prove that `h` cube/noncube in `k(x)` is
   exhaustive and disjoint. On the cube side, reconstruct the valuation/Gauss
   argument that a polynomial `h` which is a rational-function cube becomes
   `c*s^3` with `s in k[x]`, and state exactly where algebraic closedness of
   constants absorbs `c`. Check zero and constant-core edge cases.
3. **Noncube handoff.** Reconstruct the nontrivial cubic Kummer action and
   verify that a base-field constant `delta` of weight one satisfies
   `delta=omega*delta`, hence vanishes, without assuming the conclusion.
   Verify exactly—and only—the vanishing of `c7,c5,c4,c2,c1`; audit the
   handling of `c6,c0,c3`, the terminal Jacobian row, and both original
   boundaries. Confirm that this data matches the reviewed aligned
   lower-Pfaffian theorem byte-for-byte in hypotheses and normalization, with
   no illicit full-cubic boundary or source-depression import.
4. **Cube handoff and second partition.** Verify that no Kummer-weight
   vanishing is imported when `h=s^3`. Reconstruct the complete Faber landing,
   all retained constants, `r1'=...=r4'=0`, `6r5'=j/s`, and the finite-pole
   conclusion `s` constant or a single-root power. Then check separately the
   exhaustive `d=-delta/2` branches `d!=0` and `d=0` against the exact
   hypotheses of the reviewed trajectory closure. In particular reconstruct
   the mixed `rho3,rho4` split and confirm that no target load or high constant
   disappears in either branch. Search specifically for an omitted third
   mixed-`h`, reducible-Kummer, repeated-root, or constant-`s` case.
5. **Adversarial typing controls.** Independently evaluate
   `h=x(x-1)(x-2)`: use a divisor valuation to prove noncube and derive rather
   than initialize `delta=0`. Independently evaluate
   `h=(x^2+1)^3,d=0,c7=1`: confirm `3|deg(h)`, retention of nonzero `c7`, and
   routing to the full separate `d=0` cube quotient. Decide whether either
   control can pass while the real mathematical branch typing is wrong.
6. **Degree recursion.** Independently classify all unordered
   `0<=m<=n<=11` using the exact reviewed routes `Z/G/D/E/X`. Check every
   premise of the large-shear and prime/`2p` total-gcd routes, especially the
   relation between actual partial degrees, total degrees after shearing, and
   common-core degree `H`. For each `D/E` edge prove strict decrease of the
   stated lexicographic measure and recursively audit every possible child.
   Verify 78 unordered/144 ordered pairs, uniqueness of the pre-composition
   primitive `(6,9),3|H`, and the frontier-only statement that maximum twelve
   first introduces exactly `(8,12),(9,12)`.
7. **Field theorem and descent.** Check that emptiness after algebraic closure
   descends for the `(6,9)` residue, and that automorphy of all classical
   leaves descends to the original characteristic-zero field via uniqueness
   of the inverse or faithful flatness. Attack inseparability, nonclosed
   constants, leading-coefficient cancellation, and target-swap edge cases.
8. **Logical boundary.** Determine the strongest theorem actually supported.
   Do not permit an inference to arbitrary support, total-degree at most
   eleven, maximum twelve, a polynomial counterexample, or JC2. If any leaf
   dependency is only computationally sampled, provisional, or mismatched,
   identify the smallest exact missing obligation instead of averaging it
   away.

Use exact algebra and independent derivations wherever feasible. Do not edit
producer, case, canonical, ladder, notes, prompt, log, run, or erratum files;
do not launch AWS. Keep scratch work outside tracked paths. Write exactly one
report:

`xmodel/gcd3-69-coverage-composition-review-claude-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
all checked hashes, the independent degree table or a reproducible generator,
the smallest failing identity/handoff if any, precise promotion language, and
explicit quarantine language at both ends.
