# Producer report: actual-total all-row grade-13/14 export V20

Date: 2026-08-27

Status: **PRODUCER-CHECKED EXACT-Q + F65521 RESULT; HOSTILE REVIEW REQUIRED.**

## Frozen basis and custody

Case:
`cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827/`.

```text
FREEZE.sha256                 9c72580ca4be922bcd746e87cb22eba713319813f9f960e8cac4cce8af0220b7
Q RESULT.json                 b23ffacd1e4e26abccaeb94a5e83f301cd98a9918a3a84e207fc462a880fe68d
F65521 RESULT.json            266130872a10983724a7f9a080b36fef33981ff52192cbdf6c713a75bb7cd07a
Q EVIDENCE.sha256             4c945846a5e6cd0a901bd44b21b2800f46ef8a3ea22dab7413f8093253a55ac4
F65521 EVIDENCE.sha256        8e6562bd78f372d4cac91ee130d60d70fae04c50d54dd70f8fe49d479c615c3b
Q compiler result             b37b95646e5deb381de1edfd3a15a336065855402267c3044f111ca63c3b0f9e
F65521 compiler result        3e763bd4ae482494e11ca351b11619aa5d734c4c35e6f55b61146fa7021830ce
```

The two independent AWS jobs used one core each and the same hash-pinned
source archive.  Exact host paths, timings, memory, and post-harvest checks
are in `HARVEST_CUSTODY.md`.  Every harvested evidence entry rehashed.

## Result

The producer reconstructed all 569 canonical tails in all seven rows, with
row-weight contracts `13,14,15,16,17,18,19`.  In both characteristics it:

1. reproduced all 21 reviewed V9 coefficients at grades 10--12 in an
   ordinary Singular ring;
2. reproduced the reviewed V17 `Tg14_5` polynomial byte-for-byte;
3. passed one frozen-tail `+1` source-sensitivity control per row;
4. exported all fourteen new coefficients `Tg13_1..Tg14_7`; and
5. confirmed rho-deck evenness of every coefficient.

Every new coefficient is nonzero.  Exact sparse term counts are

```text
grade 13: 50, 72, 103, 30, 141, 32, 156
grade 14: 85, 134, 201, 71, 304, 90, 364.
```

The exact-Q hashes are

```text
Tg13: 3bcb17b0..., 00dcbf28..., df5953ca..., a4df324f...,
       61fd4b8b..., 1544f802..., 7ec47572...
Tg14: 8e745264..., d8526752..., dc70e191..., 0ff74965...,
       91d96924..., b05ece17..., 635c6546...
```

## Decisive section test

For each of the fourteen new exact-Q rows, all four evaluations in
`Q[rho]` are zero:

```text
CS0: cs=1, every other source name except rho zero;
A00: a0=1, every other source name except rho zero;
A10: a1=1, every other source name except rho zero;
Z00: every source name except rho zero.
```

Thus the three previously reviewed prefix sections and the terminal-origin
section persist through **every** actual-total row at grades 13 and 14.
A separate restricted-AST replay, independent of the producer evaluator,
confirmed all 56 exact section evaluations and all fourteen coefficientwise
Q-to-F65521 reductions.

## Provisional interpretation

Conditional on hostile review, the actual-total source through grade 14
cannot empty either standard `J2` chart, the terminal receiver, or the `CS0`
off-family point.  This raises the first possible section-breaking source
grade to at least 15.  It does not say that grade 15 breaks a section.

The result is stronger than “the new coefficients vanish”: all fourteen
polynomials are nonzero, often large, but their monomial supports contain no
term that survives any of the four named evaluations.  A stage-two solver on
rows only through grade 14 would therefore be deciding false emptiness
statements.  The next bounded source task is either an exact grade-15 section
evaluation/export or a proof that the jet/load structure preserves these
sections to all grades.

## Scope firewall

This is an exported-prefix result.  It does not prove that the four
assignments extend to full formal source arcs; it does not include grades 15
or higher, unwritten Rees equations, additional genuine localizers, even-sheet
rows, Keep remainders, full source coverage, Gate T, order two, maximum
twelve, or JC2.  `CS0` is outside the named unit-`k10` family on `D(k)` and
does not weaken the promoted direct `T-cs` theorem.

