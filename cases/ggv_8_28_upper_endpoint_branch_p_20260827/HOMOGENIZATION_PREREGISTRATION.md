# Preregistration: fixed-fixture weighted endpoint cross-check

Date: 2026-08-27

The authoritative object remains the literal affine raw ideal with SHA-256
`ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0`.
This lane is an exact-`Q` acceleration and cross-check only.

The unrestricted contraction in `xmodel/ideation-20260827T1808Z-sol.md`
does not survive the specialization `F1=H` verbatim: scaling the positive
raw coefficients moves out of that fixed fixture.  Introduce a weight-one
variable `u`, homogenize every monomial of a row-`n` raw generator by the
unique power of `u` making its weight `n`, replace the affine target term in
row 22 by a weight-22 variable `lambda`, and impose

```text
lambda=u^22.
```

Here each `z_*` has weight 2, each `tt_*` has weight 3, and every later raw
`F_n` or `G_n` slot has weight `n`.  Setting `u=lambda=1` must replay all 513
literal affine generators byte-for-byte.  Conversely, on `D(lambda)` the
normalization equation forces `u` to be nonzero; the contracting scaling by
`u^-1` reaches the unique chart `u=lambda=1`.  Thus, for geometric points,
the `lambda`-saturated homogeneous system is equivalent to the charged fixed
affine fixture.  No scheme-level parametrization claim is made.

The compiler must serialize the raw-generator index of every homogenized
generator, all variable weights, the normalization equation, and the
dehomogenization map.  An independent verifier must reconstruct the
homogenization from the literal JSON, check weighted homogeneity and exact
dehomogenization, and reject a missing normalization, a changed `z`/`tt`
weight, or any admitted `G22` slot.

Run exact `Q` saturation by `lambda` only on audited Box03, in a fresh
immutable source/output namespace, with a six-hour wall cap, a 100-GiB VM
cap, one core, `/usr/bin/time -v`, and zero swap.  A proper saturation is not
promotable without a complete rational raw witness.  A unit saturation is
not promotable without a fresh tracked certificate composed all the way back
to the 513 literal affine generators.  No finite-field inference is allowed.
