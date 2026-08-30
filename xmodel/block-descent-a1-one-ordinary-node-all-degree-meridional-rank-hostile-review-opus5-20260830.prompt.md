# Hostile review assignment: all-degree one-node meridional-rank obstruction

You are Opus 5, acting as an independent hostile mathematical referee. Work
only from the exact charged files below, plus narrow checks of the explicitly
named primary topology sources. You may obtain the primary papers or books
from authoritative online sources if they are absent locally. Do not inspect
any sibling model report, `.log`, `.run`, receipt, live ledger, uncharged file,
or excluded nested workspace. Do not modify Git or any repository file except
the single required report.

Write your complete report to exactly:

`xmodel/block-descent-a1-one-ordinary-node-all-degree-meridional-rank-hostile-review-opus5-20260830.md`

and write no other file. End the mathematical body with a standalone
`<!-- BODY-END -->` line. Do not add a seal; the coordinator will custody-seal
the returned bytes after exit.

## Charged files

```text
c61f0cebdc06bdca88ad76f3714047a1998ff7aeb885a79e84b060a091c23329
  xmodel/block-descent-a1-one-ordinary-node-all-degree-meridional-rank-obstruction-sol56-20260830.md
6e21fa6cc4623e3e19a683e0b4e8a2b4d4d776ce04d4141e0630463dce6aa224
  xmodel/block-descent-a1-one-ordinary-node-all-degree-meridional-rank-obstruction-sol56-20260830.md.artifact.json
a6b000430e872e372c6c4cad9d694baa522746717eeef837e52884b206eff6fa
  ops/block_descent_one_node_all_degree_meridional_rank_replay.py
e72a78f7dd027626b38ace5d770bf3b9be386b6626a2033fbb9d3ef81d79a444
  xmodel/block-descent-a1-quartic-cycle0-all-minimal-packets-graph-knot-obstruction-sol56-20260830.md
2200c712df980bc7ddc0e2c6d86be45878180f88b26851eec25dd39db51f5419
  xmodel/block-descent-a1-quartic-cycle0-all-minimal-packets-graph-knot-obstruction-sol56-20260830.md.artifact.json
e1d0472bfbd5203d1e75582c3be5b44b50d9db4987d27b97b2864cee4931522f
  ops/block_descent_a1_quartic_cycle0_all_minimal_packets_replay.py
```

First reproduce every hash and both producer seals/manifests. Replay the two
scripts in ordinary, `python3 -O`, and `python3 -OO` modes and exercise their
documented negative controls. If any charged byte differs, stop with
`CUSTODY_FAIL`.

## Primary theorem interfaces to audit

- Eisenbud--Neumann, *Three-Dimensional Link Theory and Invariants of Plane
  Curve Singularities* (1985).
- Neumann, “Complex algebraic plane curves via their links at infinity,”
  Invent. Math. 98 (1989), especially Theorem 1.
- Neumann--Rudolph, “Unfoldings in knot theory,” Math. Ann. 278 (1987), with
  the 1988 corrigendum and corrected Lemma 7.1.
- Schubert, “Knoten und Vollringe,” Acta Math. 90 (1953).
- Standard Zariski--van Kampen and Artin closed-braid presentations.

## Review obligations

Reconstruct rather than paraphrase every major implication and mark it
`CONFIRMED`, `REFUTED`, or `GAP`.

1. Check exactly when normalization `A1` implies one place and a knot at
   infinity. Audit every hypothesis of corrected Neumann--Rudolph Lemma 7.1,
   including reducedness, “good polynomial,” regularity at infinity, and
   whether the stated direction is valid for this fibre.
2. Verify that a small nearby regular fibre differs only by smoothing the
   sole ordinary node. Check absence of hidden affine or infinity vanishing
   cycles, connectedness, the Euler/gluing calculation, and the conclusion
   that the compact core has genus one and the same boundary knot.
3. Read Neumann’s 1989 theorem in the primary source and determine whether it
   really identifies this regular-fibre core as a minimal (or unique minimal)
   Seifert surface. Separate what is needed from any stronger wording.
4. Verify that every relevant polynomial knot at infinity is a graph knot and
   that the only genus-one graph knots are the two trefoils. Check graph-link
   conventions, connected sums, cabling parameters, exceptional/degenerate
   satellites, orientation, and Schubert’s genus formulas.
5. Audit the direction and meridian preservation of
   `pi1(S3-K_infinity) ->> pi1(A2-B)`. Reconstruct it topologically and from
   braid presentations. Check the closed-braid/axis distinction, product
   ordering, projective/infinity relations, and whether individual affine
   braid relations really imply the single infinity relation.
6. Verify the trefoil two-meridian presentation for both mirrors and exhaust
   transposition pairs satisfying the relation in `S_d`. Confirm that every
   such image moves at most three letters and that transitivity is impossible
   for all `d>=4`.
7. Check the theorem’s cover interpretation: connectedness versus transitive
   monodromy, simple branch versus transposition meridians, possible singular
   branch values, and whether additional unrecorded branch components would
   invalidate the application.
8. Audit the degree-three firewall. Decide precisely what the trefoil `S3`
   quotient does and does not say about a local `(2,2)` node packet.
9. Try hard to produce a counterexample to any interface or a missing
   hypothesis. State the exact blast radius of every defect. Do not accept a
   citation label as proof.
10. If the theorem survives, seek the strongest safe extension toward the
    remaining tangential, unibranch, reducible, or higher-genus horns. In
    particular assess whether graph-knot bridge/meridional rank yields a
    degree bound from total delta or genus. Clearly distinguish theorem from
    conjectural successor.

Conclude with a maximum-safe theorem, corrections, and the cheapest next
attack. Do not infer JC2 or exclusion outside the stated branch-curve class.

No `charge_basis` line is expected unless you assert a genuinely new rational
exit price under the campaign schema; ordinary hashes and topology are not a
charge basis.
