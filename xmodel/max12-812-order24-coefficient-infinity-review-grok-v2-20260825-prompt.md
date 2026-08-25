# Fresh hostile review request — `(8,12)` coefficient infinity V2

Act as an independent hostile mathematical reviewer.  Read the immutable
original target, its narrow erratum, and the first hostile review in full.
Do not use any producer or reviewer verdict string as evidence.  The V2
theorem is the original target with exactly the erratum's replacement of §7
`(7.2)` and its adjacent load-direction sentence.

Immutable charged files:

```text
092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e
  xmodel/max12-812-order24-coefficient-infinity-source-audit-20260825.md
aa90155ec8a182f4f451c77fc9548cf8035889efc230afdaea622f84eb18c495
  xmodel/max12-812-order24-coefficient-infinity-source-audit-erratum-v2-20260825.md
2f0a03a99ba6563034cdaf84ffc06f6d78ddd377144201d40aa4352ac71c6b55
  xmodel/max12-812-order24-coefficient-infinity-review-grok-20260825.md
```

Required audit:

1. Recompute the repaired load derivative directly from the definition
   `H_F(w)-g(z(w))`: at `f=K^2`, is `w=K^(1/4)`, and is the `k_j` derivative
   exactly the strictly negative Laurent part of `K^(j/4)` for
   `j=2,6,10`?  Check the sign and whether no variation of `w` is hidden.
2. Prove or break the equivalence between vanishing of any of those three
   negative parts and `K` being a polynomial square.  For
   `K=z^4+pz^2+cz+r`, verify the exact square locus `c=0,p^2=4r`, including
   degenerate quartics.
3. Recheck the coefficient-direction variation `(7.1)` and the exact rank
   conclusions: zero first differential for the order-four client and rank
   at most three for the seven order-two tail rows.  Decide whether the
   non-transversality conclusion survives without any finite-determinacy
   promotion.
4. Check that the erratum is genuinely narrow: it must not alter or silently
   strengthen §§0--6, the raw unloaded exceptional fibre, bounded-degree
   split, common-quartic support, Rees equations, chart/denominator audit, or
   the original scope firewall.  Report any residual conflict between the
   original prose and the erratum.

Write exactly one report and do not edit any other file:

```text
xmodel/max12-812-order24-coefficient-infinity-review-grok-v2-20260825.md
```

Include all three exact charged hashes, model identity, an explicit verdict
`CONFIRMED`, `REPAIR`, or `REFUTED`, the smallest failing identity or missing
hypothesis, a full independent derivation, and a strict scope firewall.  This
is source reading and hand derivation only: run no CAS, solver, substantive
Python, Lean, or other heavy local computation.
