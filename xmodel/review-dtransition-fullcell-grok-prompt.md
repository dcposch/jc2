You are the hostile different-model reviewer for the producer-checked modular
D2 full-cell result `NONEMPTY-SINGULAR-OR-LOWER-RANK`. Work in
`/Users/dc/code/math/jc2`. Adjudicate only its registered scope and write only
`xmodel/review-dtransition-fullcell-grok.md`; do not edit source, data, shared
ledgers, or launch descendants.

Read in full:

- `cases/round1_dtransition_fullcell/PREREG.md`
- `xmodel/round1-dtransition-fullcell-20260824.md`
- `cases/round1_dtransition_fullcell/fullcell_compat.py`
- `cases/round1_dtransition_fullcell/results.json`
- `xmodel/round1-dtransition-20260824.md`
- `xmodel/review-dtransition-grok.md`
- every source/input named in the result manifest that is needed to reconstruct
  the selected promoted D25 cell and band-26 source block.

Attack these clauses separately:

1. On the stated `p=105337`, `a00pp`, cell-0 `A^14`, the six compatibility
   functions are actually the canonical left-cokernel contractions of the
   unreduced source-defined band-26 equations after exact D25 and band-24
   triangular reconstruction; simultaneous vanishing is equivalent to affine
   solvability in the ten new coordinates. No D43 object enters.
2. The origin is a certified common zero. Its exact six-by-fourteen Jacobian
   has rank five, including the displayed nonzero 5x5 minor 39793, and no 6x6
   minor is asserted.
3. The deterministic free-coordinate point 1..14 is on the same promoted cell
   after exact completion, has the reported nonzero function vector, and its
   Jacobian has rank five with the displayed minor 104469.
4. The constant vector `mu=(104372,48519,44983,31248,84848,1)` annihilates the
   values and Jacobians at the two registered points. The producer correctly
   labels this a structural signal, not a polynomial identity or generic
   rank-five upper bound.
5. The only legitimate conclusion is: this modular full-cell compatibility
   locus is nonempty and the generic differential rank is at least five; the
   preregistered rank-six-at-origin gate failed. No dimension/component,
   persistence, band-28, inverse-limit, germ, characteristic-zero,
   algebraization, polynomial-map, or JC2 inference follows.

Inspect code/provenance rather than trusting JSON verdict strings. Run
`--selftest`, then `--run --out` into a fresh `mktemp -d` and demand
byte-identity. Independently recompute the two function vectors, modular ranks,
the two displayed determinants, and `mu` pairings without using stored rank or
verdict fields as authority. Inspect the tangent propagation through the D25,
D21/Row-22, prefix, and band-24 frontier solves; try to falsify the
`1-C_k` shared-prefix derivative and the claim that the band-26 coefficient
matrix is constant/rank four on this selected leading cell. Check that the
source manifest is current and that no stale or D43-derived object enters.

The producer attempted but did not obtain a global symbolic identity for the
observed `mu` dependency. Do not require that identity for the scoped lower-rank
at registered points result, and do not infer it yourself from samples.

Return exactly `CONFIRMED`, `CONFIRMED WITH GAPS`, `GAPS`, or `REFUTED`, with
the smallest failing witness if applicable. Record reviewer/model/CLI, UTC,
basis and dirty-state perimeter, exact commands, hashes, independent checks,
gaps, promotion guidance, and final verdict near the top.
