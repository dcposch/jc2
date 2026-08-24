# Hostile different-model review — maximum-12 partial-`y` Kummer preflight

You are the fresh independent different-model reviewer.  Work in
`/Users/dc/code/math/jc2` at committed basis
`1e60fcedc8626650c7c7544ad296c3624173415f`.  Read in full:

- `xmodel/max12-partial-y-kummer-preflight-20260824.md`;
- every payload named by
  `cases/max12_partial_y_preflight_20260824/FREEZE.sha256`;
- the two frozen history inputs named in the report, in full.

Frozen producer hashes:

```text
report       30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07
registration c6562834437aed42b61207c215a9d8196cf33d297f0a94503f42e4204caaf18a
replay       9239addecd3db4c2b5c656d8c1625d2761ab61bd83930ac17f926432a4da2cb4
manifest     ac686b584b93e1b5bf69f36402c4f99deeec0ec8d7557704053531e7619aa13d
freeze       59ef0712aea2424ea57b6f1727031018e769701b0f2e2384eb4638f4286ea558
payload      eb1e72d69193cded40438981907f62972725945c39a18e34891dd8f5b3645bf1
```

Verify the freeze and rerun:

```sh
shasum -a 256 -c cases/max12_partial_y_preflight_20260824/FREEZE.sha256
python3 cases/max12_partial_y_preflight_20260824/replay.py
```

Those are regression only.  Independently and adversarially audit every
load-bearing statement:

1. **Source-honest residual route.**  Starting only from the reviewed
   shear/UFD history, reconstruct why the primitive maximum-twelve cells are
   `(8,12)` and `(9,12)`, and why their still-unclosed history residues are
   respectively exactly `4|H` and `3|H`, including `H=0`.  Reject any silent
   use of the later maximum-eleven composition or a `(6,9)` exclusion.
2. **General next row.**  For `(m,n)=(dr,ds)`, independently expand the
   coefficient of `y^(m+n-2)` after `a_m=u^m`, `b_n=u^n`.  Check the power of
   `u`, every integer coefficient, cancellation of all logarithmic terms,
   `delta=sA-rB`, depression `z=uy+A/m`, and mismatch `-delta/r`.  Challenge
   normalization constants and the constant field.
3. **Full Kummer-class audit.**  Prove or refute that if the class of `h` in
   `k(x)^*/k(x)^{*d}` has order `e|d`, the minimal root extension has degree
   `e` after adjoining roots of unity, and `A,B,delta` have character one.
   Check the proper order-two class for `d=4` in detail.  Verify the five
   divisor examples, Gauss on the trivial class, constants, repeated roots,
   and any reducible-binomial edge case.
4. **Boundary and constant provenance.**  Re-derive every Taylor identity at
   the original `y=0` boundary.  Verify that both coordinates, all derivative
   orders, and all powers/factorials are correct.  Audit the lower target
   character filter; in particular the depressed `z^11` coefficient may not
   be counted as a later constant, and the order-two leaf may retain every
   even lower weight.
5. **Binary umbrella.**  Independently derive the homogeneous Euler identity,
   `W=r f g_z-s f_z g`, the exact common-power equivalence, and the displayed
   `D=f^s-g^r` identity.  Check monicity, depressions, zero-polynomial cases,
   UFD constants, and the degree of `K`.  Enforce the producer's explicit
   conditionality: no high-row Faber landing for either new cell has been
   proved.
6. **Widths and tangent ranks.**  Build an independent exact rational
   coefficient matrix at `K=z^d+z+1` for both cells.  Verify ambient variable
   counts, positive-degree W rows, ranks 11/11, kernels 7/8, and common-K
   tangent dimensions 3/2.  Decide whether the point is squarefree and whether
   the local calculation supports any global component claim.  It must not.
7. **Ranking and reuse.**  Check the two-metric statement: raw W width favors
   `(8,12)`, while Kummer branch count favors `(9,12)`; reject any overall
   cheaper-cell conclusion.  Audit exactly which `(6,9)` mechanisms are
   formal templates and which coefficients, Faber potentials, Pfaffian
   components, resultants, or trajectory exclusions type-fail.
8. **Strongest licensed conclusion.**  Give the smallest failing identity or
   missing hypothesis if any.  Do not promote this preflight to a high-row
   reduction, emptiness of either cell, maximum-twelve automorphy, arbitrary
   support, a counterexample, or JC2.

Use independent exact derivations and, if useful, a small script outside
tracked paths.  Do not edit producer, case, canonical, ladder, coordination,
prompt, log, run, or erratum files.  Do not launch AWS.  Write exactly one
report:

`xmodel/max12-partial-y-kummer-preflight-review-claude-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim.  Include
checked hashes, exact independent outputs, precise promotion language, and
explicit quarantine language.
