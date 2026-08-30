# Hostile review assignment: quartic zero-cusp braid escape

You are Fable 5, acting as an independent hostile mathematical referee. Work
only from the exact charged files below, plus narrow primary-source checks for
the named braid/algebraization theorems if needed. Do not inspect any sibling
model report, `.log`, `.run`, receipt, live ledger, uncharged file, or excluded
nested workspace. Do not modify Git or any repository file except the single
required report.

Write your complete report to exactly:

`xmodel/block-descent-a1-quartic-cycle0-braid-escape-hostile-review-fable5-20260830.md`

and write no other file. End the mathematical body with a standalone
`<!-- BODY-END -->` line. Do not add a seal; the coordinator will custody-seal
the returned bytes after exit.

## Charged files

```text
e73f8e83c4031e516f0302dea94e168b5f8b8d5f0bcc6cd86f87eb927a682e14
  xmodel/block-descent-a1-quartic-cycle0-projection-propagation-obstruction-sol56-20260830.md
4539f2fafe08ae1c323759036fa0eefb5a3fbb35d038297354b7cd10dbb31004
  xmodel/block-descent-a1-quartic-cycle0-projection-propagation-obstruction-sol56-20260830.md.artifact.json
b9f0352ce63513ce16925f9bf4d7b5be11e0246c9426ecc72cf477cd977103a0
  ops/block_descent_a1_quartic_cycle0_braid_escape_replay.py
cf157e17db8179b590f15808aab84447717df343735416578e005a2085d73d4e
  xmodel/block-descent-a1-quartic-minimal-cycle-nodal-control-threat-map-sol56-20260830.md
5d7df7ce0ad3548e88fd23734917212d6b3fbd3ada4cab81514b12bb76ea64de
  xmodel/block-descent-a1-quartic-branch-topology-coordinator-integration-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
9579d3a1737041f73a973a2ac852471a21cdad879a6d7cf3b1f76251cd5cd595
  xmodel/block-descent-all-degree-acyclic-companion-obstruction-coordinator-integration-sol56-20260830.md
8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f
  refs/chau2004_nonproper_value_set_arxiv_math0305088.pdf
```

First reproduce every hash and the target report seal/manifest. If any
charged byte differs, stop with `CUSTODY_FAIL`.

## Review obligations

Reconstruct rather than paraphrase each item and assign `CONFIRMED`,
`REFUTED`, or `GAP`.

1. Check the exact minimal zero-cusp row and identify precisely what the
   charged branch/ruling theorems do and do not impose on the global branch
   embedding.
2. Reconstruct the right Hurwitz action, its inverse, the fixed-tuple
   Zariski--van Kampen condition, and the local equal-color/disjoint-color
   rules for positive half-twist and node bands. Check all convention-sensitive
   statements.
3. Audit the false normalization-propagation argument. Decide whether
   polynomial normalization transitivity, one place at infinity, positivity,
   or the product relation supplies any extra label equality that the report
   missed.
4. Prove or refute the exact group claim: transport from `(12)` to `(34)` is
   matching-preserving; `Stab(12|34)=D4` is maximal; and any genuinely
   outside-`D4` based meridian data upgrades the node image to `S4`. Separate
   an outside transporter word from a cross-transposition generator.
5. Recompute every word in the explicit `B4` packet, its transported local
   colors, tuple invariance, normalization permutation graph, Euler number,
   boundary-cycle permutation, node packet, and generated quartic group.
   Search for an orientation, sign, or product-order error.
6. Audit the geometric interpretation of the packet. Check whether its
   band count really gives a disk with one boundary component and one positive
   node after collision, and whether all claimed finite local packets remain
   rank two.
7. Check Lee Rudolph's exact theorem and the report's use of it. State the
   maximum algebraic realization it licenses and whether the collision to a
   node is legitimate. Look especially for a gap between quasipositive
   braided surfaces, complex algebraic curves in a bidisc, affine algebraic
   curves, and globally polynomially parametrized `A1` curves.
8. Attack the remaining global firewall. Either derive a Puiseux/splice,
   semigroup, Abhyankar--Moh, link-at-infinity, or polynomial-parametrization
   obstruction to this coloring, or explain exactly why the local packet
   remains a valid control. Do not treat the packet as a global proper block.
9. Run the replay ordinarily, under `-O` and `-OO`, compare exact output
   hashes, run `--mutate-force-matching`, and state precisely what the code
   certifies and what it does not.
10. Give the maximum-safe theorem, correction list, exact blast radius, and
    cheapest decisive successor. Do not infer a rank-four exclusion, block,
    Keller map, counterexample, or JC2 result unless actually established.

No `charge_basis` line is expected unless you assert a genuinely new rational
exit price under the campaign schema; ordinary input hashes and geometry are
not a charge basis.
