# Hostile different-model review — shared maximum-12 Faber compiler

You are the fresh independent different-model reviewer.  Work in
`/Users/dc/code/math/jc2` at committed basis
`1e60fcedc8626650c7c7544ad296c3624173415f`.  Read in full:

- `xmodel/max12-partial-y-shared-faber-probe-20260824.md`;
- every file named by
  `cases/max12_high_row_probe_20260824/FREEZE.sha256`;
- every input pinned by the replay, including the full frozen max-12
  preflight and the reviewed history pair.

Frozen hashes:

```text
report       d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036
registration 1ba83d340efa28ca6d24237e97065253571ee94774a273a80ed83c4593de2d91
replay       69f9e12c0fa1e98bb7bc4dda87ab00c7f87ce2fd9c80a4bf210d216ee1bd2d9f
manifest     0b086f312627b81fcc09a884681ca31b0c88ed95151556b5d751b68dd20f3882
freeze       3a25edb31a53ecee9c96e039ab4a947908ebc0542123fb131447e1a661f45a28
payload      abbd72dc33aecd86d648696c138bcf5c919db6781a30447223fd184492d66a2d
```

First verify and rerun:

```sh
shasum -a 256 -c cases/max12_high_row_probe_20260824/FREEZE.sha256
python3 cases/max12_high_row_probe_20260824/shared_faber_probe.py
```

Treat those as regression only.  Independently audit:

1. **Faber basis and uniqueness.**  For arbitrary monic depressed `f` of
   degree `m`, prove that `F_j=[f^(j/m)]_+` are triangular and give a unique
   expansion of monic `g`.  Check all field and formal-Laurent hypotheses.
2. **Differential identity and sign.**  Derive at fixed `w=f^(1/m)` the exact
   identity
   `D=-f_z sum h_j'w^j+f_z sum r_l'w^-l`.  Attack the sign, the distinction
   between fixed `z` and fixed `w`, and the claim that `deg_z D<=m-2`
   descendingly forces every lower `h_j` to be a differential constant.
   Audit constant-field enlargement in the Kummer extensions.
3. **Lower triangular terminal.**  Derive
   `A_l=[f_z w^-l]_+`, its leading term and vanishing boundary, and the
   determinant `m^(m-1)`.  Check that `J_(x,y)=uD=j` gives the positive
   equation `m r_(m-1)'=j/u`, with all earlier derivatives zero.
4. **Independent specializations.**  Reconstruct the first two `(8,12)` and
   `(9,12)` rows exactly.  Independently verify all eleven high rows, ideally
   with a separate exact implementation.  Check the finite binomial cutoff
   and the reported support totals.
5. **Two-Laurent-row control.**  Independently revert `f(z)=w^m` far enough
   for `r_1,r_2`, check that `n+1` inverse terms suffice, and compare every
   per-branch digest or print a failing polynomial.  The two-row ranks are
   local controls only; reject any global component inference.
6. **Target quotient.**  Re-derive `P->P+q` for `n<2m`, including all signs
   and affected coefficients.  Check legality and independence of the
   slices `(h_m,h_0,h_(n-m))`, their compatibility with every Kummer class,
   and the exact remaining constant indices.
7. **Widths and allocation.**  Verify quotient widths `7,10,16` and `9,17`,
   two-row local widths `5,8,14` and `7,15`, and the aggregate arithmetic.
   Enforce the stated distinction: the aggregate route-cost heuristic may
   allocate `(9,12)` next, but no overall simpler-cell theorem follows.
8. **Scope and boundaries.**  Check that both complete Taylor-boundary
   families remain charged.  Do not permit promotion to a lower-fibre
   classification, a rational trajectory, emptiness of either frontier,
   maximum-twelve automorphy, a counterexample, or JC2.

Use independent exact algebra and keep scratch work outside tracked paths.
Do not edit producer, case, canonical, ladder, coordination, prompt, log, or
run files; do not launch AWS.  Write exactly one report:

`xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim, with
checked hashes, exact outputs, the smallest failing identity if any, precise
promotion language, and explicit quarantine language.
