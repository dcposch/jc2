# Hostile different-model review — TD6 smallest q-boundary deformation

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
artifacts on top. Read in full:

- `xmodel/td6-boundary-q2-deformation-gate-20260824.md`
- every payload named in
  `cases/td6_boundary_q2_deformation_20260824/FREEZE.sha256`
- the frozen parent producer/review chain for the two-chart first band,
  next row, moduli uniformity, paired third band, and uniform third band
  imported by the scripts

Frozen hashes:

- producer report:
  `f098dea46ca99ed26bb0ad541efe2135c78c3c1f47da8d92096a91dfece4fcc0`
- base replay:
  `0ba184470dc051fad50640647c4b78ea869b8a4153219026b23abdcf0652d357`
- exact `B=1` replay:
  `8834cd9b365a9a20d058c3ef6b0ef927c6aee05c895b650b6bc2b927ed6250ca`
- exact adaptive replay:
  `ca09d8dc6d154eec7a0fe39747c6ea348fc5e7cccd26bae7bdadae148cd51be5`
- `B=1` / adaptive stdout:
  `68863a4c0deb4eb0d2745714612bfb8ea7b445dd7355833181cf5178241ef2bd` /
  `b5cf24e87e84900f796affb8c78a63af805bb0c68c0fdab03d0ef99fa318aceb`
- freeze manifest:
  `1cc169979ee610649f87be1c7069a3517564752e8d3417f764dc09a7d22916a9`

Verify the manifest from the repository root and rerun both exact probes.
Then independently attack:

1. **Source typing.** Check that `p=t^15`,
   `q_B=t+B*t^2+t^25` retains precisely the stated degree, origin, and
   derivative data; distinguish this bounded deformation from a complete
   SP-2 boundary normal form. Verify all retained center, dead-stretch, F1,
   r9, sextic, and degree-18 field hypotheses against the frozen parents.
2. **No stale matrix.** Re-derive the first centered row
   `f1*(1+2*B*t+25*t^24)-15*t^14*g1=0`. Audit that every later x-boundary
   formula consumes this derivative and that no `B=0` right-hand side,
   echelon parameterization, or pole datum is silently reused where it
   depends on `B`.
3. **Exact `B=1` branch.** Independently verify ranks `3508/3602`,
   `36/94`, and `25/58`, failure at the degree-four centered row, and the
   exact residue `rho_1`. Recompute the frozen `B=0` residue `rho_0` from the
   parent and confirm `rho_1-rho_0=-14012/145`. Check nonzero status in the
   degree-18 field, not by floating point or a single embedding.
4. **Adaptive candidate.** Check that
   `B_*=rho_0/(14012/145)` is well-defined in the exact field and does not
   degenerate the registered q-boundary. Confirm the adaptive program fully
   rebuilds transport and the `B`-dependent first/previous/current bands,
   includes the inherited opposite-side pole row, and does not assume affine
   dependence on `B`.
5. **Adaptive ranks and obstruction.** Independently verify the staged
   ranks/dimensions `3470/3602 -> 132`, `+38 -> 94`, `+38 -> 56`, tangent
   rank `25/56`, and affine inconsistency at `t^4`. Verify that the final
   residue has genuinely nonzero `1,A,A^2` components in the exact field.
6. **Logical scope.** Decide whether the only licensed conclusion is that
   `B=1` and the adaptive secant-cancellation point are empty and the
   degree-four obstruction is `B`-sensitive. Explicitly attack any inference
   to arbitrary `B`, generic rank, other q-jets, centering/dead stretch/F1
   patterns, SP-2, a terminal class, or JC2.
7. **Successor.** State the smallest source-honest next test. Decide whether
   it really requires symbolic one-parameter elimination with pivot/rank-jump
   strata, or whether an adjoint/jet-orbit formulation can certify the same
   question more cheaply. Do not license sample interpolation as proof.

Use a second exact implementation or independently reconstructed row
reductions for the load-bearing claims; a prose reread or producer replay
alone is insufficient. Do not edit producer, case, canonical, or ladder
files and do not launch AWS. Write exactly one report:

`xmodel/td6-boundary-q2-deformation-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim, with
hashes, independent checks, the smallest failing statement if any, exact
scope, and promotion advice.
