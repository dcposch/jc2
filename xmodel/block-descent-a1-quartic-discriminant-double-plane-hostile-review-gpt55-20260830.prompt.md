# Hostile review assignment: quartic discriminant double-plane gate

You are GPT-5.5, acting as an independent hostile mathematical referee. Work
only from the exact charged files below, plus narrow primary-source checks for
named standard results if needed. Do not inspect any sibling model report,
`.log`, `.run`, receipt, live ledger, uncharged file, or excluded nested
workspace. Do not modify Git or any repository file except the single required
report.

Write your complete report to exactly:

`xmodel/block-descent-a1-quartic-discriminant-double-plane-hostile-review-gpt55-20260830.md`

and write no other file. End the mathematical body with a standalone
`<!-- BODY-END -->` line. Do not add a seal; the coordinator will custody-seal
the returned bytes after exit.

## Charged files

```text
1939c55467f5795c5bb3a264f5516c666c82e34849bc4d74f190c95d18a016bb
  xmodel/block-descent-a1-quartic-discriminant-double-plane-etale3-gate-sol56-20260830.md
5544c05bee8ffeab1791084d7d58b70ca6a45d44079efcc2f8d4535834da0216
  xmodel/block-descent-a1-quartic-discriminant-double-plane-etale3-gate-sol56-20260830.md.artifact.json
2ce87f135a1e91da8e43bc5e4cf3e37ce29f27cff6c6aacabdd08c4b75a1cde8
  ops/block_descent_a1_quartic_discriminant_double_plane_replay.py
5d7df7ce0ad3548e88fd23734917212d6b3fbd3ada4cab81514b12bb76ea64de
  xmodel/block-descent-a1-quartic-branch-topology-coordinator-integration-sol56-20260830.md
cf157e17db8179b590f15808aab84447717df343735416578e005a2085d73d4e
  xmodel/block-descent-a1-quartic-minimal-cycle-nodal-control-threat-map-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
9579d3a1737041f73a973a2ac852471a21cdad879a6d7cf3b1f76251cd5cd595
  xmodel/block-descent-all-degree-acyclic-companion-obstruction-coordinator-integration-sol56-20260830.md
```

First reproduce every hash and the target report seal/manifest. If any
charged byte differs, stop with `CUSTODY_FAIL`.

## Review obligations

Reconstruct rather than paraphrase each item and assign `CONFIRMED`,
`REFUTED`, or `GAP`.

1. Reconstruct the field tower
   `S4 -> S3=S4/V4 -> C2`, the integral normalizations `W,D`, and the claim
   `D=Spec C[x,y,s]/(s^2-q_B)`. Audit square classes, factoriality, purity,
   normality, and connectedness.
2. Derive the point-stabilizer criterion for `W->D` and independently check
   the complete local image table for quartic fibres `(211),(22),(31),(4)`.
   Treat decomposition groups, inertia, residue degrees, singular branch
   points, and quotient points literally.
3. Prove or refute that the `m=0` minimal horn makes `W->D` finite etale at
   every affine point, not merely in codimension one. Search for hidden
   ramification over a branch singularity or a normalization/conductor point.
4. Check connectedness of the `C3` torsor, the nonzero class in
   `H^1_et(D,Z/3)`, its anti-invariance under the double-plane involution, and
   the Kummer exact sequence. Separate units, `Pic[3]`, `Cl[3]`, and local
   extension residues.
5. Reconstruct the `m=1` ordinary-cusp quotient control and decide exactly
   why the cyclic cover is quasi-etale but not etale at the unique `(31)`
   point. Do not generalize the analytic type without proof.
6. Audit the named nodal double plane
   `uv=x^2(x+1)`: normality, constant units, Nagata class-group calculation,
   the injection `Pic->Cl`, and the conclusion `H^1_et(D,Z/3)=0`. Look for
   torsion or a missed unit.
7. Recompute the connected positive `S3` control: branch parametrization and
   smoothness, normalization `Gm`, cubic irreducibility and nonsquare
   discriminant, invariant ring, freeness of the `mu3` action, and actual
   finite-etale connected cover. State whether it really saturates the gate.
8. Explore the proposed successor. Determine whether the one-place
   polynomial-curve condition plus one two-point identification forces
   vanishing of the anti-invariant mod-3 class, or identify an exact counter-
   control. Distinguish punctured/link classes from covers extending over
   singularities.
9. Run the replay ordinarily, under `-O` and `-OO`, compare exact output
   hashes, run `--mutate-cusp-as-etale`, and state precisely what the code
   certifies and omits.
10. Give a maximum-safe theorem, all corrections, exact blast radius, and the
    cheapest decisive successor. Do not infer a rank-four exclusion, proper
    block, Keller map, counterexample, or JC2 result unless actually proved.

No `charge_basis` line is expected unless you assert a genuinely new rational
exit price under the campaign schema; ordinary input hashes and geometry are
not a charge basis.
