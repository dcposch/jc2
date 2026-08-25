# JC2 full-spectrum ideation packet — 2026-08-25T04:27Z

Status: **SEALED BLIND INPUT**  
Trigger: producer-exact closure of the fixed source-typed TD6 three-center
trivariate atlas, an explicit full-round trigger in the preceding synthesis.  
Prior full synthesis:
`xmodel/ideation-20260825T0126Z-synthesis.md`, SHA-256
`843f9ffd9293b2abebd3a0edb22ae843745a258a1669f258cd5d1ced22e1b2a0`.  
Basis commit: `2e6104a417cfe15a93a901aa0a9129094a2ae11b` plus the dirty,
hash-pinned artifacts below.  The worktree is intentionally not a clean
commit while AWS producers are live.

## Canonical state to read

Read `APPROACHES.md` in full, including every numbered avenue, plus the
current top sections of `PROGRESS.md`, `AUDIT.md`, and `notes.md`.  Packet-time
hashes are:

```text
APPROACHES.md 22391999922e33e648de43a83363c918295b87209fef3b0679f517249b30f423
AUDIT.md      f5c83c1ab1d76851557d6ae0a0e1d64022f6995590dcafd993868cbf12df4329
PROGRESS.md   7cd5fa41e761905c35f0092f803e51003c0e17a54638d39ceac4b474c44f9a0c
COORDINATION  ed1b18e51d5c68f3ca8f44ff296b187e5db74f3d6b7bc446104d01677b4d9b73
```

Do not read another `ideation-20260825T0427Z-*.md` submission before writing
your own.  Prior-round files may be read.

## New evidence since the prior round

### Q8 selected maximum-twelve lane

- Different-model review confirms the primitive contact partition is either
  one all-eight component or eight singletons, and the all-eight component
  cannot carry a registered actual trajectory.  Singleton remains open.
- Pure Singular completed all 126 nonzero `F_127` fibres.  There are 123
  squarefree primitive degree-190 fibres, with exact exceptional holdout at
  `w=39,56,125`.  Candidate `H(w,v)` is monic of v-degree 190 and coefficient
  w-degree at most 21.  At `w=0`, `H=Q8bar*C`, with Q8bar simple and coprime
  to the degree-182 cofactor.  All 123 primitive fibres have exact
  eight-polynomial shape bases and zero original-row remainders.
- The candidate is not yet proved to be a quotient component.  The first
  123-fibre rational reconstruction exhausted total degree below 122 with
  aliases only.  A moving-v Hensel recurrence in
  `F_127[s,v]/(s^N,H(25+s,v))` now passes order eight with `final_fail=0`,
  47,644 KiB RSS, and stdout SHA `66fc2454...`; orders 16/32/64 run on AWS,
  with Padé plus direct modulo-H substitution planned.  The superseded
  full-series-matrix implementation exceeded 50 GiB at order eight.
- The conditional good-reduction/no-merger lemma is
  `xmodel/max12-912-order3-nu-q8-good-reduction-no-merger-lemma-20260825.md`,
  SHA `ef011950...`; hostile review is active.  Full coordinate membership,
  all eight contact limits, mod-127 full-source local uniqueness, and branch
  specialization remain charged.

### AS characteristic-three counterexample lane

- Hostile review now promotes one fixed canonical state as terminal:
  predecessor `c5_5=2`, Q9 `w7_7=z7_6=1`, Q8 vector zero.  Its rank-nine Q7
  kernel and every Q6/lower completion have the nonzero high carry
  `R10=x^10`; review SHA `02d1c6f2...`.
- On the explicit unreduced affine-lift chart, an independently reproduced
  exact global quadratic design has only
  `kappa=(s15,2t6,s17,2t8)` and a 28-dimensional compatibility subspace;
  report SHA `fdd9ff90...`.  It is not a canonical-digit theorem.
- A 64-state canonical sampler directly verifies 64 Q7-compatible witnesses
  at zero RREF fibre coordinate.  A fail-closed audit corrected the wording:
  13 affine Q8 particulars are zero and 51 nonzero; erratum SHA
  `c76214b6...`.  Its fitted `3^17` count is model-only without a canonical
  carry degree theorem.  Correct V3 exhausts all `3^9` Q7 states below each
  actual particular and finds no next-high survivor, but the remaining 17
  Q8 directions are untouched.  A full `3^13` census will group exact integer
  carry signatures, then run one honest fibre design per signature.

### TD6 proof/exclusion lane

- Two hostile reviews confirm the whole `H=P3=0` raw curve and hence the
  former `H=0` debt in the fixed source-typed trivariate section.
- Exact V27/V22/V26 covers close generic `B3=0`, its quadratic factor, and
  `tau=1/2`; both clean V26 pivot orders are rc zero.  Combining whole
  `B3=0` with `D(UHB3)`, whole `U=0`, and whole `H=0` producer-exactly
  empties the fixed normalized section
  `(c1,c2,c3)=(C,V,U) in A^3`.  Report SHA `eb127a58...`; package manifest
  `86102e8c...`; clean-ascending supplement report `d30a979d...`.  Hostile
  review of the cross-package union is queued, so this is not yet promoted.
- The smallest source-proven transverse parameter is q-boundary class q2,
  denoted `beta` to avoid collision with `B3`.  A generic-center dual-number
  adjoint is launching on AWS.  Dead stretch d6 is the next matrix-changing
  fallback.  No neighborhood, full TD6, SP-2, landing, or degree-bound claim
  follows from fixed A3.

### Operations and review debt

- All substantive computation is AWS-only.  Seven nodes provide 512 vCPUs;
  local activity is editing, orchestration, hashing, status, and one bounded
  cloud-review client.  Producer successors do not wait for reviews.
- Immediate review queue: Q8 no-merger/checklist (active), TD6 fixed-A3
  union, AS global unreduced chart, then any canonical carry theorem.
- Full proof walls remain exhaustive landing/coverage and an absolute or
  cofinal complexity bound.  Full disproof walls remain an all-depth bounded
  state, characteristic-zero algebraization, collision, and a genuine
  polynomial Keller pair.

## Required independent submission

Follow `COORDINATION.md` exactly:

1. Give a compact disposition over all numbered avenues (`unchanged`,
   `raise`, `lower`, `reopen`), with reasons for every change.
2. Rerank the principal proof and counterexample bottlenecks.
3. Supply at least one genuinely new avenue/mechanism and one new connection
   between existing avenues.
4. Name the strongest proof attack, strongest counterexample/falsification
   attack, and one software acceleration or decisive experiment.
5. Give at most three detailed idea cards, each with dependencies, cheapest
   discriminator, interpretation of every outcome, stop condition, and
   expected information gain.
6. Recommend `continue`, `redesign`, or `stop` for Q8, AS, TD6, and the main
   background lanes.  Attack scope inflation and seek a route that changes
   the global JC2 bottleneck rather than merely adding another fixed case.

No submission may claim a proof or counterexample from the provisional facts
above.  Keep any computation proposed in the response AWS-only.
