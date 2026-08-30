# Hostile review assignment: quartic one-cusp pseudo-plane funnel

You are Opus 5, acting as an independent hostile mathematical referee. Work
only from the exact charged files below, plus narrow primary-source checks for
named theorems if needed. Do not inspect any sibling model report, `.log`,
`.run`, receipt, live ledger, uncharged file, or excluded nested workspace.
Do not modify Git or any repository file except the single required report.

Write your complete report to exactly:

`xmodel/block-descent-a1-quartic-cycle1-pseudoplane-companion-hostile-review-opus5-20260830.md`

and write no other file. End the mathematical body with a standalone
`<!-- BODY-END -->` line. Do not add a seal; the coordinator will custody-seal
the returned bytes after exit.

## Charged files

```text
7d40e7ee6d5970c51d62f73bafaf11670cb32c06bd51859876ab526f0fdf8bab
  xmodel/block-descent-a1-quartic-cycle1-pseudoplane-companion-threat-map-sol56-20260830.md
c75951528ed3b2d5aa3ebe15b5186893e4da3aac131ca1ca931eee4968ba631c
  xmodel/block-descent-a1-quartic-cycle1-pseudoplane-companion-threat-map-sol56-20260830.md.artifact.json
0b01b3901363097e25e03fe67d0644c287ee3ef1701acd4e9ee1e166da05ca54
  ops/block_descent_a1_quartic_cycle1_pseudoplane_replay.py
cf157e17db8179b590f15808aab84447717df343735416578e005a2085d73d4e
  xmodel/block-descent-a1-quartic-minimal-cycle-nodal-control-threat-map-sol56-20260830.md
5d7df7ce0ad3548e88fd23734917212d6b3fbd3ada4cab81514b12bb76ea64de
  xmodel/block-descent-a1-quartic-branch-topology-coordinator-integration-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
2e6d82035df6717d1a39f31dc19b23b7c727bb940d4730d2c7ea9400e5433cce
  xmodel/block-descent-a1-cubic-affine-survivor-funnel-sol56-20260830.md
9e32b0fe8835b6ea6002036b95e2261a612754d73d796cb10edda347cf3cf65e
  xmodel/block-descent-a1-cubic-affine-survivor-funnel-hostile-review-gpt55-20260830.md
38baa55d6e2d54bf3fa5329e1623d983b4e6ac6eaddf7fd7dbb60b2cd1675578
  ladder/SHEET6.md
88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad
  refs/zoladek2008_official.pdf
```

First reproduce every hash and the report seal/manifest. If any charged byte
differs, stop with `CUSTODY_FAIL`.

## Review obligations

Reconstruct rather than paraphrase each item and assign
`CONFIRMED`, `REFUTED`, or `GAP`.

1. Check the exact minimal row and the deduction
   `C=A1,Q=0,e(U)=1`.
2. Audit every pseudo-plane step: at most one multiple fibre, the
   no-multiple implication `U≅A2`, legitimate use and exact scope of the
   promoted topological-degree-at-most-five theorem, the formula
   `Pic(U)=Z/mu`, rational acyclicity, and `K_U=0`. Identify any hidden
   smoothness, flatness, irreducibility, or classification assumption.
3. Reconstruct the proof that `U-g1(A2)` is finite. Check the units/localization
   exact sequence carefully. Reconstruct `g1^*(t-a)=cP^mu`, the Kummer
   irreducibility step, and `mu|d1`; look for a primitive-divisor or
   residue-degree escape.
4. Independently derive the companion curve `T=U×B`: etaleness,
   reduced/principal Cartier status, fibre counts `2/1/0`, `e(T)=-3`,
   `e(U-T)=4`, connectedness of the complement, and
   `pi(U)=A2-{node}`. Check compact-support Euler use on singular/reducible B.
5. Audit the height-one equations
   `div_Y(pi^*b_i)=2R_i+S_i`, `[S_i]=-2[R_i]`, the boundary-class injection,
   localization quotient, different, and the claim that `S_i` is
   nonprincipal on Y but principal after deleting R. Treat residue degree and
   multiple ramification components literally.
6. Recompute all 36 transporter parity sets and the cusp/node group packet.
   Decide whether any determinant, orientation, discriminant, sign, norm,
   resolvent, or infinity relation canonically removes the claimed ambiguity.
7. Attack the proposed curve/ruling control and every firewall. Search for an
   overlooked contradiction coupling `rho` and `pi`, a second ruling defect,
   purity, Hartogs, Picard torsion, the omitted node, or the polynomial pair
   `(rho∘g1,b∘F)`. Equally, give a sharp control if the funnel genuinely
   survives.
8. Run the replay in ordinary, `-O`, and `-OO` modes, compare exact output
   hashes, run `--mutate-force-companion-parity`, and state precisely what the
   software does and does not certify.
9. State a maximum-safe theorem, exact blast radius, and the cheapest decisive
   successor. Do not infer a rank-four exclusion, block occurrence, map, or
   JC2 result unless actually proved.

No `charge_basis` line is expected unless you assert a genuinely new rational
exit price under the campaign schema; ordinary input hashes and geometry are
not a charge basis.

