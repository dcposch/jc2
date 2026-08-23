# Sol completion note — Lean depth-witness definitional layer

Date: 2026-08-20

## Status

COMPLETE for the requested definition-only phase.

Created `/Users/dc/code/math/jc2-lean/depth-witness/` as a new Lean/Lake
project.  Its `lean-toolchain`, `lakefile.toml`, and generated
`lake-manifest.json` are byte-identical to both finished siblings
`theorem-a/` and `vertex-gap/`:

- Lean `v4.34.0-rc1`;
- Mathlib `20bc12820422504f9e52ee6caebf8182a9015336`.

Implemented in namespace `JC72108.DepthWitness`:

- `(72,108)` / td=6 metadata, global template exponents/degrees, the full
  `R <- F_s <- G_m <- P_i` exponent ladder, and the structural
  approximate-root recurrence;
- `Coeff := ZMod 105337`, prime-field instance, and kernel-checked fixed
  embedding constants `r3=795`, `zeta42=2779`, `etaB=24069`,
  `fLead=51107`, `gLead=33066`;
- the unsplit 36-fiber radical/chart equations;
- the exact nine orbit types and their 42/21 sizes, B-freezing, shared
  stretch/merge data, even 21-orbit tails, and six PIN42/no-log equations;
- direct phase-twisted factors and finite Cauchy products defining `phi` and
  `gamma` (seven directions times six or three subbranches per orbit);
- the exact Jacobian row recurrence with the `-42` inhomogeneity at row 20;
- `WindowConditions D`, `HasDepthWitness D`, general `DepthExtension`, and
  the D21->D23 / D23->D25 specializations;
- structural CORE2 metadata: all raw D21 cell supports, 38 residual labels,
  22 exact pivot cells, 18 remaining template coordinates, counts
  `27 vars / 45 equations`, and the corrected D23/D25 tail/frontier lists.

The y-side statement is fail-closed at `D <= 42`, because the source only
certifies rows `0..41` as pure y-side.  Expanded CORE2, Row_22, and Row_24
polynomial lists are deliberately absent; a future witness is to be checked
against the unreduced orbit/row definitions.

Verification completed:

```text
lake build
Build completed successfully (8748 jobs).

./scripts/check_axioms.sh
OK: all depth-witness setup lemmas depend only on permitted axioms.
```

The permitted axioms reported by Mathlib are exactly `propext`,
`Classical.choice`, and `Quot.sound`.  There is no `sorry`, custom axiom,
`native_decide`, `Lean.ofReduceBool`, or `Lean.trustCompiler` in the Lean
sources.  No nonemptiness/emptiness theorem has been asserted.  No git command
was used.

## Line counts

```text
521  Challenge.lean
 16  Solution.lean
128  README.md
145  FIDELITY.md
128  formalization.yaml
 28  comparator.json
 49  scripts/check_axioms.sh
 16  lakefile.toml
  1  lean-toolchain
1032 total (listed text files)
```

`LICENSE` is an unchanged copy of the siblings' Apache-2.0 license;
`lake-manifest.json` is generated and byte-identical to the siblings.

## Verdict-dependent next theorem

- D25 NONEMPTY, after reconstructing an actual F_p-rational point:
  `JC72108.DepthWitness.HasDepthWitness 25` (with D23 survival optionally
  recorded alongside it).
- D25 EMPTY on all 36 fibers, after a checked elimination certificate:
  `HasDepthWitness 23 ∧ ¬ HasDepthWitness 25` at the stated modular chart
  scope.

Neither branch alone states an inverse-limit/formal germ, a characteristic-
zero result, another chart/embedding, or a polynomial Keller pair.

## Open questions

1. What is the final D25 verdict and component mask?
2. If D25 is NONEMPTY, is there an explicit reconstructed point over
   `F_105337`?  A proper ideal only proves geometric nonemptiness over an
   algebraic closure and does not inhabit the current `ZMod 105337`
   existential.
3. For the Solution certificate, should the solver trace be proved equivalent
   to CORE2 and then back-solved, or should the final reconstructed point be
   checked directly against `orbitCoefficient`, `phi`, `gamma`, and
   `jacobianRow`?  Direct raw-row checking is the smaller trust surface.
4. The banked D23 witnesses must be translated into complete `ResidueAData`
   (including every coefficient consumed below depth 23) before
   `HasDepthWitness 23` is proved.
5. Grok should review `FIDELITY.md`, especially the `A1/A2` versus `a1/a2`
   naming distinction, fixed-embedding scope, factor phases, and the
   `<32+D` truncation cutoff.
6. Before registration, confirm the preferred presentation/order of the
   campaign label `(72,108)` versus sources that write `(deg P,deg Q)=(108,72)`;
   no mathematical identification with chart degrees is currently asserted.
