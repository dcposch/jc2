# Hostile review: normalized K00 h10=1 closure through G13

You are Opus 5, an independent hostile mathematical and computational
reviewer for the plane Jacobian-conjecture campaign. Work in
`/Users/dc/code/math/jc2` on frozen git basis
`4c91d6fc398d1b4f2b8ca1a11d69c4bb3fef9c0d`.

Review both provisional generations needed for the exact normalized
`e=2,m=2,h10=1` finite-cell claim:

```text
eda4f40b452ef1f68d53d82ff22c5ec6a4a74147b7f6785b3dc9cc1148137db8
  xmodel/k00-ram-e2m2-h10eq1-g12-branch-split-producer-sol56-20260830.md
  body 9501 / b1e79f4643ac1f0151441086056a91694e67cc12a678d7de3565fde073224343
cc8d84f8d5deeb8ee3852901b657e65b7499c397fbff66ba2b8361ad8cd4db15
  xmodel/k00-ram-e2m2-h10eq1-g12-branch-split-replay-sol56-20260830.py
b352e26e7748e6b7eb31b5ae081a6ba6a8ea7843ce58e457c27e3557c5d88e44
  xmodel/k00-ram-e2m2-h10eq1-g13-closure-producer-sol56-20260830.md
  body 9494 / 82c277ca01460a6a1cfe05e79ec5b3ed2cce95b520ad0d287f3b8c62ab088cfd
a508b9853490d82f8a9c7c6242331b5c33298104249a216a9bb418c949e5403d
  xmodel/k00-ram-e2m2-h10eq1-g13-closure-replay-sol56-20260830.py
```

The reviewed parent is:

```text
8ba031e87032a007beade2eda7f97f94802eac0bfa561addf90d8f5fb3df8307
  xmodel/k00-ram-e2m2-h10eq1-g11-coordinator-integration-sol56-20260830.md
  body 3793 / 74d1b34134f92d4a5c80ceb38120c8cb6b2ce9b7e53dec8b2da26cb7f8294019
```

Literal source custody:

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4
  xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py
```

Independently reconstruct and attack:

1. Verify every hash and seal. Reconstruct G12 and G13 from all 569 frozen
   tails and the exact sparse `Q(i)` engine; do not obtain G13 by shifting a
   displayed G12 formula or trust either producer replay as an oracle. Audit
   factorials, row labels, retained surface/normal/K10 slots, and the claim
   that `N9`, `k10[4]`, and unloaded quartics cannot arrive at G13.
2. At G12, rebuild the complete branch split after the promoted G11 parent.
   Verify the death of both old `n=4` rank-one signs and the existence/scope
   of every fresh `n=5` rank-one and rank-two survivor. Check denominators,
   open conditions, recentering, and whether any branch or scheme-valued
   point was silently lost.
3. At G13, derive all seven literal rows and the row-six identity
   `G13_6=(t/8)G11_1-(s/32)G11_2+(35*kappa/2^23)P4`, with
   `P4=s^4-384s^2t^2+4096t^4`. Recheck both Gaussian rank-one signs and the
   substitution `P4=32768t^4`.
4. On rank two, rederive the `Delta`-localized inverses at G11/G12 and retain
   all free `alpha,beta,gamma,eta,kappa2,kappa3`, kernel coordinates, and
   arbitrary `N8`. Verify the N8 image relations, the annihilating combination
   `G13_5+G13_3/8+3G13_1/128`, and exact reduction modulo `P4` to
   `(35*kappa/2^17)s*t*(s^2-64t^2)`. Prove that no projective common point is
   allowed on the stated open; attack every denominator-clearing step.
5. Re-run and independently check both old-pass/new-fail fixtures. Implement
   reviewer-owned exact arithmetic or a mathematically independent
   derivation sufficient to catch shared-code errors; exercise source and
   formula mutations. Explain any unavoidable shared-engine exposure.
6. Decide separately: (a) the maximum exact G12 theorem, (b) the maximum
   exact fresh-`n=5` G13 theorem, and (c) whether together with the promoted
   G11 parent they prove
   `V(G0,...,G13) intersect V(k10[0]) intersect D(k10[1]) intersect D(d[2])`
   empty at field-point scope. Keep finite point sets, nonreduced schemes,
   compatible jets, formal arcs, occurrence/source reachability, attainment,
   algebraization, polynomial maps, counterexamples, and JC2 distinct.

Return an itemized verdict (`CONFIRMED`, `CONFIRM_WITH_CORRECTIONS`, `GAP`, or
`REFUTED`) for G12, G13, and the conditional whole-cell composition. State
precisely the maximum theorem safe to promote and the cheapest next
nonduplicate cell/source gate.

Hard output cap: at most 8,000 tokens and at most 28,000 UTF-8 bytes. Do not
restate long inputs. Do not inspect, list, search, stat, build, modify, or
control `jc2-lean`; the process sandbox also enforces this. Do not run local
heavy CAS or Singular. Seconds-scale exact stdlib computation is permitted.
Do not edit any input, canonical file, script, or dependency. Write exactly
one report:

```text
xmodel/k00-ram-e2m2-h10eq1-g12-g13-closure-hostile-review-opus5-20260830.md
```

End with one standalone `<!-- BODY-END -->` line and no seal block.
