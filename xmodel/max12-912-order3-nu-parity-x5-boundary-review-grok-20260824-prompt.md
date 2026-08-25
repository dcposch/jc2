# Hostile different-model review — max12 order-three parity x5 boundary

Work in `/Users/dc/code/math/jc2`.  Read in full:

- `xmodel/max12-912-order3-nu-parity-x5-boundary-20260824.md`;
- every file named by
  `cases/max12_912_order3_nu_parity_x5_boundary_20260824/MANIFEST.sha256`;
- the reviewed maximum-twelve order-three preflight/Faber inputs named by the
  package; and
- the current spectral-Wronskian report only for its already frozen
  coordinate and terminal-row conventions.

Charged hashes are:

```text
producer report  9f62c226b0bb9ce3ec7ce9d96543ebae5cb6f6ee4bcfd32c00d25f4f27fe51e7
MANIFEST         be8dd3efa89cb5e767e63b25080322cdeddc506c39aca8f2f313f2dd0ba92ace
FREEZE           b572ed0d90de10a6e0068ee36bd6632f9c356860cbce7bc1308d63648f9876b4
```

Verify the manifest and rerun the registered replay as regression only.
Independently reconstruct and attack:

1. From `K=z^3+pz+q` and the exact F12 construction, prove or refute that
   `q=x0=x2=x4=k=0` makes `f` odd, `g` even, and
   `r1=r3=r5=r7=0` identically, with no hidden characteristic or normalization
   assumption.
2. Recompute `r2,r4,r6,r8` over Q.  On `x5=0`, check separately the `x3=0`
   and `x3!=0` branches and verify
   `x1=p*x3`, `r6=-4*x3^3/81=nu`, and `r8=0`.
3. Audit the passage from a coefficient-fibre component to an actual
   trajectory.  Check the exact terminal equation `9*r8'=j/u`, its field and
   nonvanishing hypotheses, and whether `r8=0` is genuinely contradictory.
4. Put `A=x3-2*p*x5`.  Independently substitute `A=0` into `r2`, derive
   `r2=-4*p*x5^3/81`, exhaust all resulting branches, and prove or refute
   `nu!=0 => A!=0` without dividing by a possibly zero quantity.
5. Independently compute `Res_x1(r2,r4)`, including the scalar, `x5` factor,
   and residual factor.  Check that the remaining chart is exactly
   `A*x5!=0` and that no statement about that chart has been smuggled into
   the producer conclusion.
6. Enforce scope: this is only a parity component probe.  It does not prove
   parity exhausts loaded solutions, does not close `A*x5!=0`, any generic
   loaded component, all `(9,12)`, maximum-twelve, a counterexample, or JC2.

Use exact arithmetic and independent scratch work outside tracked paths.  Do
not edit producer, case, canonical, prompt/log/run, coordination, ladder, or
predecessor files.  Do not launch AWS.  Write exactly:

`xmodel/max12-912-order3-nu-parity-x5-boundary-review-grok-20260824.md`

Give one overall and per-item verdict from `CONFIRMED`, `GAP`, or `REFUTED`,
checked hashes, the smallest failing identity or missing hypothesis, precise
promotion language, and precise quarantine language.

