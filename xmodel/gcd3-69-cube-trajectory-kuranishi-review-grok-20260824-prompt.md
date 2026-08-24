# Hostile different-model review — GCD3 `(6,9)` cube-core trajectory closure

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`c327bdc8d02472feba42573760325099f34b8cdf`, with frozen uncommitted
artifacts on top. Read in full:

- `xmodel/gcd3-69-cube-trajectory-kuranishi-20260824.md`;
- every payload named by
  `cases/gcd3_69_cube_trajectory_kuranishi_20260824/FREEZE.sha256`;
- the frozen cube-mismatch Faber--Laurent producer/review;
- the target-translation erratum/review; and
- the lower-Pfaffian producer/review, only for the universal invariant-fibre
  decomposition explicitly consumed by this successor.

Frozen hashes:

- producer report:
  `069f6280332b44d93dcad17801dc7136d4a79fb06ace101c2dce8a4e746b5e7b`;
- registration:
  `7e629e46167d445d74cbdeb3ffbc4f76b26a214c504f938fb1bdf74fac66f557`;
- SymPy replay:
  `db14f5a43462317143afa0ec3a56d5fcccb23fe94f5f2f701b14996b06675766`;
- Singular replay:
  `f6e56bc185c780e3af445fa0de6ea7d23972981a8228ea9fc20b22a2a8ba0c78`;
- manifest:
  `6391c23c79dac869a0a11442e5df2dfda496b51602e8796442c31e22721bb766`;
- freeze file:
  `5637ac20df1302f0b8817788c6c88f85429cabbfe3edac2150fd8abddb4d241b`.

Verify every hash and rerun all three registered commands. Those are
regression evidence only. Then independently attack every load-bearing
claim, using separate exact algebra, alternate elimination orders, and
complete derivations rather than trusting producer PASS strings:

1. **Scope and exhaustion perimeter.** Confirm that the theorem starts only
   after the reviewed polynomial cube-core Faber--Laurent landing, treats
   separately `s in k*` and `s=C(x-a)^m, m>=2`, treats `d!=0` and `d=0`
   separately, retains all legal target constants and both original
   polynomial boundary values, and imports no nontrivial-Kummer weight or
   descent hypothesis. Identify any ramified, rank-zero, component-crossing,
   zero-load, or infinity stratum omitted by the proposed weighted cover.
2. **Weighted balances and terminal exponents.** Re-derive the Kuranishi/Faber
   weights, the common-component rank strata, and the uniform pole laws
   `(14-k)p=1` and `(14-k)p=m-1`. Check that every leading component is
   projectively covered and that a necessary initial ideal is never mistaken
   for a reconstructed arc. Independently audit all exact source-boundary
   values used to exclude the DS and common-cubic components.
3. **The `d!=0` exceptional orbits.** Recompute the two values
   `q=(45+-3 sqrt(195))/2`, the length-eight localized normal scheme,
   squarefreeness/rank claims, reconstruction rows, resultants, and `Q5`
   units. Attack every denominator, exceptional orbit, chart boundary, and
   source-boundary exclusion. Decide whether both finite-pole terminal
   branches are genuinely empty.
4. **The `d=0` high-constant strata.** Recompute the first-nonzero rows for
   `c7,c5,c4,c2,c1`, every projective orbit, resultant/unit certificate, and
   boundary or degree contradiction. Check separately all chart boundaries,
   intersections, and the all-high-constants-zero degeneration.
5. **Target-load ordering.** Independently derive the `rho1,rho2,rho3,rho4`
   balances. Verify the exclusions for `rho1` and `rho2`, and verify that the
   `rho4`-first calculation is not incorrectly used to set a later `rho4` to
   zero after `rho3!=0`. Confirm that the remaining mixed fiber really has
   parameters `mu=6rho3`, `nu=6rho4` and that `nu=0` versus `nu!=0` is an
   exhaustive split.
6. **Mixed `rho3/rho4` fiber.** Starting from the original invariant
   numerators, independently prove or refute the localization `nu!=0 => A!=0`
   and the reversible coordinate change yielding
   `72 V^2-3 A^3-512 mu=0`, `A^2 B=-256 nu/9`, and
   `r5=A^2 V/1024-256 nu^2/(27 A^3)`. Check both directions of ideal equality,
   all localized denominators, singularities, points at infinity, and lost
   `A=0` solutions. For `mu!=0`, verify smooth genus one and justify rigorously
   that a rational coefficient path from `P1` is constant. For `mu=0`, verify
   the normalization `A=24 lambda^2,V=24 lambda^3`, the exact two-term formula
   for `r5`, nonconstancy, surjectivity/pole pullback, and incompatibility with
   each allowed one-pole terminal form. Explicitly test `rho3=0,rho4!=0`.
7. **Unmixed fiber, reconstruction, and logical closure.** Audit the use of
   the independently reviewed two-sheet decomposition when `nu=0`, including
   the zero-bracket, elliptic, cusp/DS, constant, and boundary cases. Then
   trace every surviving rational pole back through the original Faber
   coefficient and source-boundary equations. Decide whether the strongest
   licensed conclusion is exactly: conditional on the reviewed cube-core
   landing, both finite-pole alternatives are empty for the polynomial cube
   core. Do not infer arbitrary `(6,9)`, full partial-`y` coverage, a Keller
   pair, or JC2 without separately proving those dependencies.

Use exact arithmetic throughout. Put scratch work outside tracked paths. Do
not edit producer, case, canonical, ladder, notes, prompt, run, or erratum
files, and do not launch AWS. Write exactly one report:

`xmodel/gcd3-69-cube-trajectory-kuranishi-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
hashes, independent derivations, the smallest failing identity if any,
precise promotion scope, and quarantine language at both ends.
