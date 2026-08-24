# Hostile different-model review — TD6 centered global compatibility control

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
producer artifacts on top.

Read in full:

- `xmodel/td6-global-compatibility-gate-20260824.md`
- `cases/td6_global_compatibility_20260824/replay.py`
- `xmodel/d73-strict-or-equality-20260824.md` and its hostile review
- the cited LR2/SP-2 portions of `ladder/SHEET6-LROOT.md`,
  `ladder/SHEET6-LT-REVIEW.md`, and the terminal ledger

Frozen producer hashes:

- report: `b53064c877a4f0b741f23f036b2323195bef825ccc72b6722b98f1fc2d2eec17`
- replay: `d5d0d4d4209ef115b952571082c37252eb0f1e032e02f182cdccf516b29519d9`

The report has a typographical omission in displayed equation (8): the raw
text `-left(` is intended to be `-\\left(` in both lines. Treat this as a
formatting erratum only; recover the exact polynomials from the replay and
report any mathematical mismatch.

Independently rerun and attack exactly:

1. Prove the bare-chart monomial divisibility lemma and resulting Jacobian
   contradiction under its explicit hypothesis that both polynomials are
   holomorphic in the same bare chart `x=t*s^R,y=s^-1`.
2. Audit the Sigray/LR2 typing: does the terminal data permit a shared
   unramified `y^-1` truncation, with no split/characteristic exponent below
   height four? Does `T=xy^4-y^3` correctly represent the centered variable?
   If this source claim is not established, return GAP at exactly that point.
3. Independently expand `f3,g3`, their supports, exact Jacobian, centered
   valuation, special-fiber normalization, three branches, contacts, and
   Lambda sum. Check that this matches only the SP-2 x-side/local mechanism
   and is not a Keller realization.
4. Recover `f6,g6` from code/intended equation (8), verify both fixed Newton
   rectangles and that centered valuation of `J-1` is exactly six. Check no
   stronger fixed-rectangle order is asserted.
5. Audit the formal `Q[T][[x]]` recursion: coordinate Jacobian factor,
   coefficient equation, Bezout identity, characteristic-zero divisions,
   arbitrary finite solvability, truncation order, composition back to
   `Q[x,y]`, and degree growth. Distinguish `Q[T,x]` from the full
   polynomial-origin completion.
6. Scope: the formal construction is one-sided, cap-dropped, finite-order,
   with no convergence/algebraization/opposite-side chart. Decide whether it
   validly stops the bare-divisibility attack but kills or realizes no td6
   class and leaves the two-chart fixed-rectangle exact-J gate open.

Use independent exact algebra and primary source text; do not trust verdict
strings. Identify the smallest failing identity or hidden local-to-global
step. Do not edit producer/canonical files or launch D43/new-book searches.

Write exactly one file:

`xmodel/td6-global-compatibility-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
replay/hashes, source caveats, the formatting erratum, scope exclusions, and
promotion advice.
