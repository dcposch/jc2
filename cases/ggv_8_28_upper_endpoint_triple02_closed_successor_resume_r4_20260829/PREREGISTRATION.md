# TRIPLE02 node-1 closed-successor resume R4: mathematical preregistration

Date: 2026-08-29 (packet authored 2026-08-28)

Status: `SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW`

R4 keeps the R1/R2/R3 mathematical recursion fixed and repairs only custody
(the R3 hostile review's O2-B1 single-open archive-authentication finding
and the adjacent O2-N2/O2-N4 findings).  This document is **byte-identical
in its mathematics** to the R3 preregistration; the objective, starting
ideal, recursion contract, terminal classifications, the exact single-line
node standard-basis append law, and every literal binding below are
unchanged and were reviewed in R1, R2 and R3.

## Objective

Settle, by the frozen r5 exact finite Fitting/chart recursion, the TRIPLE02
node-1 **closed successor**

`V(I_node1 + (Delta_node1))  subset  Spec(Q[q0,q2,c4,c6])`  (dp order),

where `I_node1 = (g1, g2)` is the archived node-1 ideal and `Delta_node1` is
the archived node-1 selected rank-six minor normal form.  Nothing else.

## Resumed starting ideal (exact)

Node 2 of the global recursion is exactly the three literals

1. `g1` — TRIPLE02 branch factor, SHA-256
   `2b9d29b706ce5d7e58e2dc5a28799782f5610c5ccb7b71987ebd694fd8b83206`;
2. `g2` — TRIPLE02 root chart delta, SHA-256
   `fecd1d43f3f55e1c65bec858303b7688c0db83dbe9c3a60f51f70130a4149336`;
3. `Delta_node1` — archived node-1 size-6 witness normal form at rows
   `1,2,4,7,9,11`, cols `1,2,3,5,6,7`, SHA-256
   `84b4c2c4c0bfe5aa7414c35813cc1cf63d7d5416358a394b8e8bdc35820f1d02`;

with inherited rank upper bound **6** (provenance: rank archive SHA-256
`b947a2d3e81525902a93500026020c2cf9580f070767757389daadb9a6bbe3b2`,
certificate member SHA-256
`cc6dc1c4edbceeecf31c17b96ab9a0ac9744720100e7bf3f20ba41c4e4cd99d2`).

All three literals are bound by hash to the R3 terminal archive
(`e5bdd2b25cde0dccd8f1e6b8f0e1fcc815d409426308afb49c45df86af53a1e1`, exact
member census **454 = 391 regular files + 63 directories**) and
`Delta_node1` is additionally bound semantically on the host: the witness
replay stage re-runs the exact node-1 reducer (95 rational unit pivots),
byte-compares the pivot log and the residual with the archive, recomputes
`det` of the archived minor, and requires exact equality with the
`Delta_node1` literal and a nonzero normal form mod the node-1 standard
basis.

**Appended-copy law (R2 repair; R3 exact strengthening).**  Singular's
`write()` appends, and the archived node-1 directory ran exactly three
stages (reduce, rank_size_6, saturation) whose shared `node_header` each
wrote the standard basis, so the archived `NODE_001_STANDARD_BASIS.txt`
(SHA-256 `bd95508c...640d`, 14,883 bytes) is exactly **three identical
concatenated copies** of the single-stage write (4,961 bytes).  The witness
replay produces one copy; the R1 rule `produced == archived` was therefore
unsatisfiable on the live host, and R2/R3 require exactly
`archived == produced * 3`.  The pivot and residual TSVs have stage-unique
filenames and remain byte-exact comparisons.  For the resumed nodes, R3
verifies the **exact single-line append law** (the R2 census accepted any
whole multiple, so a doubled file passed): each header-writing stage
appends `string(NODE_SB)` — newline-free content, confirmed on the real
archived 4,961-byte unit, which contains exactly one newline, at its end —
plus the write's trailing newline, so each node's standard-basis file must
split into exactly `header_stage_count` identical blocks each containing
exactly one newline at its end.  A doubled file is refused because its
per-stage block would carry two newlines, and the single-stage
`EXACT_EMPTY_NODE` census is no longer vacuous.  A skipped census remains
only for a node containing the timed-out final stage, whose partial append
is undecidable.

## Why the settled open route cannot be re-entered

The node-1 proper open `D(Delta_node1)` was settled
`EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY` by the reviewed proper-open
resume R5 (terminal archive SHA-256
`4b8ffc1c16828b22b2e76a3aa92a25e8c1f472190a708f30a7b71ba952cbef7e`, exact
member census **574 = 490 regular files + 84 directories**); that archive is
consumed here as routing provenance only, never as a computational input.
Three independent firewalls prevent re-entry:

1. **Algebra.**  `Delta_node1` is a generator of every node ideal from node 2
   onward, so every chart of the resumed recursion lies inside
   `V(Delta_node1)`, which is disjoint from `D(Delta_node1)`.  The adapter
   selfcheck carries a miniature of this fact (`sat(J, Delta_parent)` is the
   unit ideal when `Delta_parent in J`).
2. **Routing.**  Global node numbering starts at 2; no `node_001` stage
   directory may exist; the node-1 open saturation and its 257-step pure
   `Delta_node1`-power search are never generated; the archived
   `NODE_001_OPEN_SAT_STANDARD_BASIS.txt` and `saturation.sing` are never
   even extracted.
3. **Guards.**  Every scanned delta of every node stage is hash-compared
   against `Delta_node1` and must differ; builders, the driver, and the
   classifier reject any violation.

The archived node-1 saturation record (900 s cap, rc 1, `timed_out: true`) is
validated as the frozen frontier and remains `TIMEOUT_NO_VERDICT`; nothing is
resumed from it.

## Recursive contract (per node n >= 2)

Identical to the frozen r5 recursor (SHA-256
`d679a4d7fb4bf2619fbb3ff47ea6f386ba1c75fdc477276cabf3bec8a2b2cd90`), whose
builder functions generate every stage script, with two repaired templates
(byte-identical to the reviewed R1 templates):

- **reduce**: node standard basis, unit/vacuity fixtures, generator NF
  fixtures, mutation fixture, exact 106x105 elimination with 95 rational unit
  pivots and pivot invariants, 11x10 residual in ambient normal form.
- **rank census**: for sizes from the inherited bound down to 0, the complete
  support-matchable minor census (Hall matching on the residual support),
  support replay, either an explicit nonzero witness at the found rank or an
  every-minor-NF-zero certificate for each skipped size.
- **saturation (repaired)**: `sat(NODE_IDEAL, delta_n)` with object-shape
  gates, node-ideal inclusion, two-sided stability
  (`sat(OPEN_SB, delta_n) == OPEN_SB`), plus per-generator reverse-containment
  witnesses `NF(OPEN_SB[i] * delta_n^k) = 0` with reduced intermediates and
  search bound 64 on the proper-open branch (exhaustion is a bounded
  no-verdict, never a fatal claim).  The 257-step pure-delta power search is
  gated to the empty-open branch, where it remains mandatory and produces the
  empty-open power-membership certificate.  The closed successor
  `NEXT = NODE + (delta_n)` and its emptiness marker are computed exactly as
  in r5.
- **chart (repaired)**: fresh saturation with the same gates, elimination with
  reducer `NODE_SB` (repivoting after base change forbidden), full 105x105
  right transform tracked, base-changed and recorded entry-by-entry (11135
  reductions, 11025 recorded entries), scanned-delta determinant replay,
  denominator-cleared adjugate kernel (10-rank vectors), all 11x(10-rank)
  bordered identities, all 106x(10-rank) original-row kernel identities,
  bordered nonzero plant equal to delta, endpoint plus-one and plus-two shift
  plants with affine replays (at least one shift nonzero), and the complete
  symmetric endpoint coefficient census for `E = x14*x72 + x1*x97`
  ((10-rank)(11-rank)/2 coefficients).  The chart ACTIVE standard basis is
  written and must equal the saturation stage's OPEN standard basis
  byte-for-byte.
- **descent**: on an endpoint-dead chart (or an empty open) with a nonempty
  closed remainder, node n+1 is `generators + (delta_n)` with inherited bound
  equal to the found rank.  Maximum 6 new nodes (2 through 7).

No factor/gcd/content/radical/nilpotence normalization anywhere.

## Terminal classification (exactly one)

- `EXACT_ENDPOINT_DEAD_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR_FINITE_COVER` —
  every chart of the finite cover endpoint-dead and the final closed
  remainder empty (or a node ideal exactly the unit ideal).
- `RING_LEVEL_ENDPOINT_SURVIVOR_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR_CHART_PENDING_NILPOTENCE_RADICAL`
  — some chart has a nonzero endpoint coefficient normal form.  This is a
  ring-level statement only; nilpotence/radical/geometric analysis is a
  separate later campaign.
- `NO_VERDICT_OPEN_REMAINDER_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR` — bounded
  no-verdict: max nodes exhausted or a stage timed out; the summary records
  the exact remainder generators, their hashes, and the inherited bound, and
  the classifier re-derives the reason from the stage evidence itself.
- `REVERSE_CONTAINMENT_SEARCH_EXHAUSTED_NO_VERDICT_ON_TRIPLE02_NODE1_CLOSED_SUCCESSOR`
  — the bounded reverse-containment witness search failed to certify the
  computed saturation; no claim is made.
- Any custody, resource, adapter, parser, census, or hash irregularity is
  `CUSTODY_OR_ADAPTER_FAILURE_NO_VERDICT`.

## Epistemic separations (binding)

Ideal equality, saturation equality, ring-level endpoint nonvanishing,
radical membership/nonemptiness, and geometric existence are five different
statements; no artifact of this packet may promote one to another.  Chart
results are chart-local.  No conclusion about the whole TRIPLE02 stratum,
another component, the ambient endpoint problem, or JC2 may be drawn from any
terminal of this packet.  `jc2-lean` is never contacted.
