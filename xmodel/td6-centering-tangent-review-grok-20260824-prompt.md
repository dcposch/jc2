# Hostile different-model review — TD6 full-cokernel centering tangent

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`1e60fcedc8626650c7c7544ad296c3624173415f`. Read in full:

- `xmodel/td6-centering-tangent-gate-20260824.md`;
- every payload in `cases/td6_centering_tangent_20260824/MANIFEST.sha256`;
- the reviewed parent adjoint producer/review;
- the reviewed whole-`B` boundary-pencil producer/review named by the report.

Frozen hashes:

- producer report:
  `15b08835512839d044c049b11ba889be1fbf06c52dc9ad6487e714910ac774d3`;
- replay / canonical stdout:
  `6b56865611cd44c506ea9cc665e0efb6616f512b8ddf611b3149d95c18ffa87e` /
  `c78b7fbbb4d3bb1ba7f5a63498efe35bc3cee51463a130f42113743d943144e8`;
- quotient/orbit audit / stdout:
  `4377e3079d109807dc7a0325ae1896205e58d31ff8ab84a3549af534619978db` /
  `5967696f796c6b0520186ca944ee64a9a2539ba52ba2de8c109424742698e68a`;
- README:
  `f9a0b614ec3cdb90acfa4cab07d44f36602bb64885317b13634b69668075c83b`;
- manifest and freeze:
  `983da3aca0f5018d00b72cf750285422b569e2f5afffe147d913f0552fa479c0`.

Verify the freeze from the repository root. Rerun the registered programs:

```text
python3 cases/td6_centering_tangent_20260824/replay.py
python3 cases/td6_centering_tangent_20260824/orbit_audit.py
```

These are regressions, not independent evidence. Then attack every
load-bearing claim with a genuinely separate exact reconstruction:

1. **Scope and quotient.** Reconstruct the registered normalized TD6
   section, the degree-18 field, all rectangles/charts/boundary/F1/pole pins,
   and the three center jets. Derive at fixed global `(x,y)` the center
   tangents `delta t=-dc1*s^-3-dc2*s^-2-dc3*s^-1`. Independently enumerate
   every regular source reparametrization and rectangle-preserving
   determinant-one target gauge. Test whether any omitted gauge absorbs a
   center direction. The qualifier “in this registered normalized section”
   is load-bearing.
2. **Matrix-changing differentiation.** Do not reuse a stale particular
   solution. Independently differentiate the 3,602-column transport system,
   solve `A0 dx=-dA x0` in all three directions, and verify every dependent
   transport row. Rebuild both later parameterizations and the current band.
   Check ranks `3470/3602 -> 38/132 -> 38/94 -> 25/56` and all derivative
   rank-change flags.
3. **Varying left-null space.** Reconstruct all ten current compatibilities,
   including differentiation of their left-null vectors. Test explicitly
   that the calculation contains the `lambda'` contribution and is not merely
   `lambda0(db-dA*x0)`. Independently compare the three coordinate
   sensitivities of the first `t^4` residue.
4. **Full cokernel ranks.** Form the exact `10 x 3` sensitivity map over the
   field `E`. Verify rank three and kernel zero with an independently chosen
   nonzero `3 x 3` minor. Form `[D C|-C0]`, verify rank four with a nonzero
   `4 x 4` minor, and independently solve the affine equation to confirm no
   common linearized root. Attack dependence on row order, pivot choice, and
   field-reduction conventions.
5. **Orbit/source audit.** Recheck that the earlier `(S,D,L,A)` source block
   has rank four, `q'(t)` is a unit on the boundary section, the four target
   gauges have zero center projection, and no chart/pole/F1 tangent creates a
   hidden quotient direction. If a larger legitimate global equivalence is
   found, state the smallest correction and recompute the rank.
6. **Logical meaning.** The base normalized control is already affine
   inconsistent. Decide whether injective `D C` is only sensitivity at a
   nonsolution, not a tangent-space or nonlinear family kill. Attack every
   inference to absence of remote/nonlinear center roots, uniformity in other
   moduli, SP-2, a terminal class, or JC2. Assess whether an exact
   matrix-changing `c1=C,c2=c3=1` pencil is the smallest licensed successor.

Use exact arithmetic. Producer replay plus prose comparison is not
independent evidence. Do not edit producer, case, canonical, ladder, notes,
prompt, log, run, or erratum files and do not launch AWS. Keep scratch work
outside tracked paths. Write exactly one report:

`xmodel/td6-centering-tangent-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
hashes, independent derivations, the smallest failing identity if any,
precise promotion scope, and quarantine language at both ends.
