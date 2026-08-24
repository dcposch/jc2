# Hostile different-model review — AS109 specification gate

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`c17bd2542b40f3178ec619ae4a73501550555336`, with frozen uncommitted producer
artifacts on top.

Read in full:

- `xmodel/as109-support-gate-20260824.md`
- every file under `cases/as109_support_20260824/`

Frozen report hash:

`b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5`

Independently rerun the replay and attack exactly these claims:

1. The preregistration and manifest hashes were frozen before enumeration,
   and no enumerator was run.
2. The displayed `E1`, `E2`, monomial bracket, and nonlinear `N` formulas are
   the exact expansion modulo `109^3`.
3. For every `m>=1`, `A_0=y^m`, `B_0=x^108 y` is a two-slot,
   collision-preserving `E1` solution, arising from the exact triangular
   source gauge `G_m=(x+109 y^m,y)`.
4. The nonlinear residual and transported successor formulas are exact;
   transport adds three slots, remains collision-preserving, and is not a
   same-slot cycle.
5. Therefore the monomial-count cap alone does not make literal exponent
   enumeration finite, and the current gauge quotient does not define an
   invariant finite graph. Check that `NO-FROZEN-GRAMMAR` is justified at
   exactly this scope; it must not be read as nonexistence of cap-eight lifts.
6. Hensel nonautomorphy lemma: any exact integral `Z_109` polynomial lift of
   `(x-x^109,y)` with determinant one maps each residue ball bijectively onto
   its target residue ball, hence has 109 distinct preimages for targets over
   `(0,b)` and is noninjective over `Q_109`; the finite-coefficient/collision
   field embeds in `C`, giving a genuine complex Keller counterexample.
7. Closed-support contraction: if a finite gauge-fixed coefficient module
   has `N(U')` in its residual module and `L` a unit inverse/right inverse,
   the displayed map is a strict 109-adic contraction and yields an exact
   lift. Check every module/ball hypothesis and the combination with claim 6.
8. The canonical and five-slot controls fail closure at `x^216`/`x^324`;
   no support core, exact lift, or characteristic-zero counterexample was
   found or inferred.

Use exact arithmetic and identify the smallest missing hypothesis or
overclaim. Do not invent a grammar, widen the cap, enumerate a rectangle, or
edit any producer/canonical file.

Write exactly one file:

`xmodel/as109-support-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
replay/hashes, explicit scope, and promotion advice separately for the
negative grammar verdict and the positive Hensel/contraction lemmas.
