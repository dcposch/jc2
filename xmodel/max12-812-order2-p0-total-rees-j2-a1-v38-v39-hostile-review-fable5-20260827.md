# Fable5 hostile review: V38 graded ladder and V39 `Tg19_7` W19 compatibility

Date: 2026-08-27
Reviewer: Fable5 (different-model adversarial lane; producer was Sol)
Reviewed artifacts (pins verified against the prompt):

```text
97e3af988719fca94b23243652deebc3ad80dd5a51fc4978e65c0e3776f74f19
  xmodel/max12-812-order2-p0-total-rees-j2-a1-graded-ladder-v38-producer-sol-20260827.md
dbec09d2021e81549c8305bc19d0a46a00cf9721aade9a7e530b6daeec77bfd6
  xmodel/max12-812-order2-p0-total-rees-j2-a1-w19-tg19-7-compatibility-v39-producer-sol-20260827.md
```

Overall verdicts: **V38 CONFIRMED. V39 CONFIRMED.** No material claim is
refuted; no material gap remains.  Every mathematical statement in both
reports was independently re-derived on this host with reviewer-written
code (own weight table, own monomial enumerator, own product construction,
own exact-rational elimination, own dual evaluation), not by re-running the
producers' PASS paths.  Both artifacts are promotion-ready under the
campaign's different-model rule, with the scope qualifiers already present
in the frozen records; see Section 6.

---

## 1. Custody verification (all pins checked, none failed)

* Both report SHA-256 values match the prompt's pins.
* `FREEZE.sha256` for V38 (17 entries) and V39 (16 entries) verify from the
  repo root, covering both frozen program sets and the pinned upstream
  sources (V37 solver `ba034c8c…`, V23 parser+result, V28/V30/V33/V35
  compiled results, `ops/aws_exact_lane.sh`).
* V38 `FREEZE_CENSUS.sha256` (13 entries), `FREEZE_CONTROL_CENSUS.sha256`
  (13 entries), `FREEZE_LAUNCH_V2.sha256` (2 entries) all verify.
* Every hash printed in the V38 report was recomputed and matches: the six
  primary-census pins, six control-census pins (including both
  `EVIDENCE.sha256` manifests), the six frozen-decision pins, the harvest
  TSV `0d63a122…`, `verify_harvest_v38.py` `63820a1c…`,
  `LAUNCH_ERRATUM.md` `a0a28005…`, `launch_host_v2.sh` `ccf0e940…`, and the
  launch-v2 pin manifest `7c30d05d…`.
* Every hash printed in the V39 report was recomputed and matches: case
  manifest `debff1ba…`, both lanes' `RESULT.json` / compiler result /
  evidence manifest, and the target raw-file hash `6049a936…`.  The
  solver's internal pins (`ROW_BRIDGE.json` `d119796f…`, bridge builder
  `657cd20d…`, preregistration `eac2819c…`) and the validator's compiler
  pin `a268558d…` all match on disk.
* The V38 report's 9×6 primary lane-hash table matches the verified
  `HARVEST_VERIFICATION.tsv` cell for cell (54/54 hashes).
* Relocatable evidence: all 32 V38 decision manifests (11/11 files each),
  both V38 census manifests, and both V39 manifests (17/17 files each)
  replay clean with literal `sha256sum -c` from inside each job directory;
  every path is `./`-relative.
* Every job directory's `freeze_check.stdout` contains only `OK` lines.
* All four replay commands printed in the V38 report were executed:
  both freeze checks pass, `verify_harvest_v38.py` ends
  `PASS-V38-HARVEST-32-LANES`, and its fresh output diffs clean against the
  frozen TSV.  `selector_prime_used == selector_prime_requested` is
  enforced per lane, confirming "no fallback was needed."

## 2. Independent mathematical replay — method

Dual-host agreement and validator PASS tokens were treated as determinism
evidence only.  The mathematical weight of this review rests on
reviewer-written code staged in `/tmp` (not in the repo):

1. **Own weight table**, hand-transcribed from the `sigma_weight` spec and
   compared name-by-name against the parser for all 65 registered
   variables; all weights positive (no weight-0 cofactor blowup is
   possible).  Every one of the 51 nonzero rows was re-verified homogeneous
   of its grade against this independent table.
2. **Own monomial enumerator** (iterative DP, structurally different from
   the producers' recursion), proven equal to the producer enumeration for
   every needed cofactor weight 0–14, then used to build **my own**
   fixed-weight product lists for every decision.
3. **Own dual evaluation.**  For each claimed nonmembership, the emitted
   rational functional was evaluated on the target (must be 1) and on
   *every* product in my independently built fixed-weight system (must be
   0), in exact `Fraction` arithmetic.
4. **Own sparse exact-rational elimination** for every claimed exact rank,
   plus a second, functional-independent nonmembership proof: adjoining the
   target to the component must raise the exact rank by one.
5. **Raw-bytes hand check** for the V39 headline (Section 4).

The spectator-variable omission (cofactors restricted to the 65 registered
variables) is sound: the full polynomial ring is free, hence faithfully
flat, over the subring on the registered variables, so extension and
contraction of the row ideal cannot create membership of a target supported
on registered variables.  For weights ≤ 19 the fixed-weight finality
argument is exact: all unfrozen rows are homogeneous of weight ≥ 20 and
cannot meet a weight-≤19 graded piece.

## 3. V38 audit (verdict: **CONFIRMED**)

Independent replay results, all 16 labels (my counts, from my enumeration):

```text
label  W  products  component      claimed/verified rank   dual   outcome
i1_j0   5       0   0 x 1; 0 nnz    0 / 0                  1 crd  nonmember, isolated
i1_j1   9       0   0 x 1; 0        0 / 0                  1      nonmember, isolated
i2_j0  10       0   0 x 1; 0        0 / 0                  1      nonmember, isolated
i1_j2  13      11   0 x 1; 0        0 / 0                  1      nonmember, isolated
i2_j1  14      24   0 x 1; 0        0 / 0                  1      nonmember, isolated
i3_j0  15      53   6 x 46; 79      6 / 6   (+target 7)    2      nonmember
i1_j3  17     217   0 x 1; 0        0 / 0                  1      nonmember, isolated (W17 control)
i2_j2  18     426   0 x 1; 0        0 / 0                  1      nonmember, isolated (W18 control)
i3_j1  19     803   50 x 696; 2086  50 / 50 (+target 51)   5      nonmember
i4_j0  20    1473   161 x 982; 2951 156 / 156 (+t 157)     14     nonmember
i1_j4  21    2661   0 x 1; 0        0 / 0                  1      nonmember, isolated
i2_j3  22    4716   0 x 1; 0        0 / 0                  1      nonmember, isolated
i3_j2  23    8219   336 x 5485;16117 333 / 333 (+t 334)    32     nonmember
i4_j1  24   14144   1158 x 8533;35643 1111 / 1111 (+t 1112) 159   nonmember
i1_j5  25   23994   0 x 1; 0        0 / 0                  1      nonmember, isolated
i5_j0  25   23994   2695 x 9395;65518 2286 / 2286 (+t 2287) 316   nonmember
```

Claim-by-claim:

* **Sixteen nonmemberships `a1^i*k^j ∉ I_19` for `i≥1, j≥0, 5i+4j≤25`:
  CONFIRMED.**  For every label, the emitted functional evaluates to 1 on
  the target and to exactly 0 on every product of my own complete
  fixed-weight enumeration (up to 23,994 products at W25).  Independently
  of the functionals, my own exact-`Q` elimination shows that adjoining the
  target monomial strictly raises the rank of its component in all six
  nonzero-component cases — a second proof through a different mechanism.
* **Completeness: CONFIRMED.**  No cofactor-degree cap exists: my
  enumerator generates every monomial of the complementary weight and was
  proven identical to the producer enumeration on all used weights; the
  faithful-flatness argument covers omitted spectators.
* **Connected components: CONFIRMED.**  My own BFS reproduces every
  component census.  Component restriction is anyway not load-bearing for
  the negatives, because both the producers' contract and my replay check
  the dual against the *full* product list.
* **Exact rank/span: CONFIRMED, fully, on this host.**  All six claimed
  ranks (6, 50, 156, 333, 1111, 2286) were reproduced by my own exact
  rational elimination (largest case 4.5 s), and additionally mod fresh
  primes 999983 and 1000003 (neither is a selector prime).  Nothing rests
  on the AWS flint span replay.
* **Rational duals / schemas: CONFIRMED.**  All 16 functionals decode under
  the strict schema (reduced fractions, positive denominators, sorted
  canonical monomials); the ten isolated targets carry exactly the
  one-coordinate functional, and I verified isolation directly: the target
  monomial occurs in no product's support.  W17/W18 isolation is enforced
  in both compiler and validator, as claimed.
* **Canonical agreement: CONFIRMED.**  For each label the two lanes'
  compiled records are byte-identical after removing only
  `selector_prime_requested`/`selector_prime_used` (checked with my own
  diff, not just `verify_harvest_v38.py`), and I re-derived the canonical
  core hash construction for `i3_j1` from scratch; it matches the TSV.
  Note the two lanes run identical code with different selector primes, so
  their agreement alone is not independent mathematics; this review's
  replay supplies that independence.
* **Launcher erratum: CONFIRMED additive-only.**  `diff launch_host.sh
  launch_host_v2.sh` shows exactly: a tarball name suffix, bundling of the
  two v2 files plus a v2 freeze check, and the missing remote `cd "$root"`
  before `run_aws.sh` — the claimed cwd orchestration fix.  No frozen
  mathematical program differs; the restarted jobs verify against the
  original `FREEZE.sha256` (in-job freeze stdouts clean).
* **Negative controls: CONFIRMED as designed.**  The V27 cross-dual
  (`a1^3 ↦ 1`, `a1*aa0*rs2 ↦ −1/3`) annihilates all 53 W15 products in my
  replay; the divisor-anchor implication direction is sound (membership of
  a divisor times a power of `k` would force membership of the refuted
  anchor), and all six anchored shapes were *also* decided by explicit
  jobs, so the implication is a cross-check, not a dependency.  V38 has no
  external mutation fixture analogous to V39's; see observations.
* **Crucial scope distinction: PRESERVED.**  W17–W19 negatives are
  fixed-weight final (later rows have weight ≥ 20); W20–W25 negatives are
  only relative to rows through grade 19.  The frozen records encode this
  (`globally_final_nonmembership` true exactly for weight ≤ 19; the W≥20
  `negative_scope` string is validator-enforced), and the report's
  mandatory warning states it correctly.  Membership statements would be
  monotone-final; none occurred.

## 4. V39 audit (verdict: **CONFIRMED**)

* **Target exclusion: CONFIRMED.**  Generators are the 69 named / 50
  nonzero rows other than `Tg19_7`; my product list is built only from
  those and contains 802 products (= 803 with the target row, matching the
  symbol report's sizing 803/13,388: 13,388 − 552 target terms = 12,836).
* **Census: CONFIRMED** by my independent enumeration: 802 products,
  12,836 nonzero coefficients, union support 5,078 including the 552-term
  target; target-seeded component 98 products × 563 monomials, 1,917 nnz;
  the component is closed and separated (no outside product touches any
  component monomial), and the seeding used all 552 target monomials.
* **Exact rank 92: CONFIRMED** by my own exact rational elimination;
  adjoining `Tg19_7` gives rank 93, independently proving nonmembership.
* **Four-coordinate dual: CONFIRMED at three levels.**  (i) The dual as
  printed in the report was hand-transcribed and shown to take `Tg19_7` to
  1 and every one of the 802 products to 0 in exact arithmetic over my own
  enumeration.  (ii) Both lanes' emitted functionals equal that
  transcription exactly.  (iii) **Raw-bytes hand check:** the frozen
  `Tg19_7_q.poly` (SHA `6049a936…`, exactly 552 `+`-separated terms)
  contains each dual coordinate exactly once, with coefficients
  `(3/128)`, `(3/256)`, `(−3/64)`, `(15/8192)`, and

  ```text
  (3/128)(−128/9) + (3/256)(−128/9) + (−3/64)(−64/3) + (15/8192)(4096/15)
    = −1/3 − 1/6 + 1 + 1/2 = 1,
  ```

  so `lambda(Tg19_7)=1` holds straight from the frozen bytes with no
  parser in the loop.  All four dual monomials have sigma weight 19.
* **24-term residual: CONFIRMED.**  Replaying the 66 recorded row
  multiples against my own products reproduces, coefficient for
  coefficient, exactly the 24-term `R19` printed in the report (the
  report's transcription is exact); 5 of its 24 terms are supported on the
  V34 set `{a1, ell2, cs1, rs2, aa0, ee1, ec3}`; `lambda(R19)=1`; the
  canonical hash is `4a839249…` under my own reconstruction of the
  serialization; and `Tg19_7 − R19` lies in the exact span of the 98
  component products (rank stays 92 when it is adjoined).
* **Controls: CONFIRMED.**  Running the frozen `exact_controls` locally
  reproduces the AWS payload exactly (stationary matrix hash `28363457…`,
  88 nonzero entries).  Beyond that, I hand-extracted entries directly
  from the parsed rows: `Tg19_1[ec9]=(3/8)a1`,
  `Tg19_2[k6_1]=(3/8)e0+(3/128)rs1²`, `Tg19_3[ell8]=−(3/16)a1·e0`,
  `Tg19_3[ez8]=(3/16)e0`, rows 4–7 contain no grade-19 newcomer, and
  `Tg11_1=(3/8)a1·e0`.  Both Bezout identities were verified by hand
  algebra: with `X=−32A²`, `Y=5kr²`, `S=r³`,
  `(X+Y)(X²−XY+Y²) − 125k³S² = X³ + Y³ − 125k³r⁶ = X³`, and
  `q − (5/8)k·(3/128)r² = −(3/32)A²`.  The `e0=0` consequence is applied
  only inside the control (the membership system uses the literal rows,
  which retain `e0` terms), exactly as stated.
* **External coefficient-deletion control: CONFIRMED.**  The deleted term
  `(3/128)a1*aaa0*rs1*rs2` is present in the frozen target;
  `lambda(mutated) = 4/3 ≠ 1`; the mutated-target hash matches the
  recorded control; and on both hosts the harvested mutation lane shows
  validator exit status 1, no PASS token, the required
  `target polynomial mutation or bridge failure` stderr line, and no
  forbidden output file.
* **Row bridge: CONFIRMED.**  `ROW_BRIDGE.json` replays bit-identically
  from the frozen builder on this host; the target's raw-file and
  canonical `rho=0` hashes match the report and my own hash of the parsed
  polynomial.
* **Cross-lane agreement: CONFIRMED, with a recipe note.**  The two lanes'
  payloads are byte-identical after deleting `certificate.selector_prime`.
  The pinned value `70aca1cc…` reproduces as SHA-256 of the sorted
  *compact* JSON of that normalized payload **without** a trailing
  newline; the report does not spell out this serialization, which cost a
  short search (see observations).
* **Scope: PRESERVED.**  The result is ordinary, unsaturated, homogeneous
  W19 membership only; fixed-weight final because later rows have weight
  ≥ 20.  The report explicitly declines radical, `a1`-saturation
  (`a1^N*Tg19_7` remains open), honest-chart, Rees, Gate-T, and JC2
  readings, and does not infer nonemptiness.  Resource figures (1.37 s /
  ~43 MiB on r6d; 0.98 s / ~43 MiB on Box01) match the harvested
  `time -v` stderr.

## 5. Consistency with the symbol report and the V37 erratum

* **Symbol report** (`…first-occurrence-symbol-spencer-design-sol-20260827.md`):
  V39 is a faithful implementation of its Section 6 design — same frozen
  question, same expected sizing (803 → 802 on target removal), and all
  seven required controls (row-hash freeze, newcomer census, stationary
  matrix, `Tg11_1`, both Bezout identities, complete all-term-seeded
  component, dual selector primes, deletion fixture, deterministic
  outside-V34-first residual).  I verified the symbol report's exact
  support facts on the frozen target: 28 of 552 monomials supported in
  `S`, and zero monomials with exactly one outside coordinate name.  My
  hand checks of the stationary entries confirm its rank-two-on-chart
  analysis: row 3's only newcomer entries are proportional to `e0`, rows
  4–7 have none, so no grade-19 newcomer can cancel `Tg19_7` — consistent
  with, and now complemented by, V39's stronger statement that the *old*
  rows through grade 19 cannot produce it at weight 19 either.
* **V37 erratum** (`…graded_ladder_v37_20260827/ERRATUM.md`): V38 is the
  demanded hardened successor and discharges every listed requirement:
  strict schema/pin/scope validation (verified in code and against the
  frozen records), canonical fraction encodings, repeated W17/W18 and V27
  controls, relocatable `./`-relative evidence (replayed 32/32 locally),
  and validator-enforced completeness/scope text.  V38's W17–W20 numbers
  reproduce V37's exactly (ranks 0/0/50/156; dual coordinate counts
  1/1/5/14), so the immutable V37 record and its erratum remain accurate.
* **What V39 adds:** `Tg19_7` is *not redundant* — it is a genuinely new
  raw compatibility condition at ordinary weight 19, now with a 24-term
  equivalent representative `R19` modulo the other rows.  **What V38 rules
  out:** any monomial localizer certificate `a1^i*k^j` (`i≥1`,
  `5i+4j≤25`) inside the grade-≤19 row ideal — finally at W17–W19, and
  relative to `I_19` at W20–W25.  Neither result asserts the raw `rho=0`
  locus on `D(a1)` or `D(a1*k)` is nonempty; nonmembership of an emptiness
  certificate is not a nonemptiness proof, and both reports say so.  This
  is consistent with the prior J2 stage-two status (minimal typed `T-a1`
  certificate at `a1^4` requires genuinely grade-20 rows, or mixed shapes
  at weight ≥ 21 — now sharpened to: no `a1^i k^j` shape through weight 25
  from grade-≤19 rows).

## 6. Verdicts and promotion readiness

| # | Claim | Verdict |
|---|---|---|
| V38-1 | All sixteen `a1^i*k^j ∉ I_19` (`i≥1, 5i+4j≤25`) | **CONFIRMED** |
| V38-2 | Censi, components, ten isolated 0×1 targets | **CONFIRMED** |
| V38-3 | Exact `Q` ranks 6/50/156/333/1111/2286 | **CONFIRMED** (independent exact elimination) |
| V38-4 | Duals annihilate every full fixed-weight product | **CONFIRMED** (independent enumeration) |
| V38-5 | W17–W19 fixed-weight final vs W20–W25 `I_19`-relative | **CONFIRMED**, correctly stated and machine-enforced |
| V38-6 | Harvest custody, canonical dual-lane agreement, relocatable evidence | **CONFIRMED** |
| V38-7 | Launch erratum additive-only, no frozen-math mutation | **CONFIRMED** |
| V39-1 | `Tg19_7 ∉ (J_other)_19` over `Q` | **CONFIRMED** (dual + rank 92→93 + raw-bytes hand identity) |
| V39-2 | Census 69/50/802/12836/5078; component 98/563/1917; all-term seeding | **CONFIRMED** |
| V39-3 | Four-coordinate dual exactly as printed | **CONFIRMED** |
| V39-4 | 24-term `R19`, 66 multiples, 5 V34-supported terms, pinned hash | **CONFIRMED** |
| V39-5 | Controls incl. stationary matrix, Bezout, deletion fixture | **CONFIRMED** |
| V39-6 | Ordinary unsaturated scope; no radical/saturation/Rees/Gate-T/JC2 inference | **CONFIRMED** (preserved) |
| X-1 | Consistency with symbol report and V37 erratum | **CONFIRMED** |

**Promotion:** Both artifacts are promotion-ready under the different-model
rule.  This review (a different model from the Sol producer lanes)
independently rebuilt the complete product systems and re-proved every
verdict, including full exact-rank replays; promotion text must retain the
frozen qualifiers — `I_19`-relative for W20–W25, ordinary-unsaturated W19
for V39 — and must not present either nonmembership as evidence of chart
nonemptiness.

Non-blocking observations (no soundness impact; recorded for successors):

1. The V39 validator omits the EC2 lane guard that the V38 validator has
   (it binds the lane string but would run off-EC2).  Both harvested runs
   executed on the registered EC2 lanes per their meta/registration files.
2. The V39 report's cross-lane pin `70aca1cc…` requires the undocumented
   serialization "compact sorted JSON of payload minus
   `certificate.selector_prime`, no trailing newline"; a successor report
   should state the recipe next to the hash.
3. V38 carries no external mutation fixture analogous to V39's; its
   negative controls (isolated one-coordinate functionals, V27 cross-dual,
   divisor anchors) are adequate, and this review's independent replay
   closes the residual risk, but the V39 fixture pattern is the better
   template.
4. AWS environment attestations (EC2 vendor, hostnames, wall/RSS) were
   accepted from harvested metadata; no mathematical conclusion rests on
   them because all mathematics was re-derived locally.
5. Upstream row provenance (V23 parse chain and the V28/V30/V33/V35
   grade-16–19 emissions) is hash-pinned and was reviewed in the earlier
   V34–V36 hostile review; this review re-verified the pins, re-parsed the
   rows, re-proved homogeneity against an independently transcribed weight
   table, and hand-checked stationary entries and the `Tg19_7` bytes, but
   did not re-derive those rows from the order-2 geometry.

## 7. File/tool/edit disclosure

* Tools: Read, Grep, Glob, Bash (local only), Write.  No network, no
  browsing, no AWS, no heavy CAS; largest local computation was a sparse
  exact-rational elimination on the 2695×9395 W25 component (~4.5 s) and
  full product enumerations up to 23,994 products per weight.
* Reviewer scripts staged outside the repo in `/tmp`: `v39_replay.py`,
  `v39_controls.py`, `v38_replay.py`, plus inline one-shot snippets for
  hash-table comparison, serialization-recipe search, raw-byte term
  census, and metadata checks.
* Files read (representatives; all hash-verified where pinned): both
  producer reports; V38 case — all three preregistrations, four freeze
  manifests, `solve_graded_ladder_v38.py`, `validate_graded_ladder_v38.py`,
  `verify_harvest_v38.py`, `run_aws.sh`, both launch scripts,
  `LAUNCH_ERRATUM.md`, `HARVEST_VERIFICATION.tsv`, both census compiled/
  validated results and evidence, all 32 decision-lane compiled/validated
  results, evidence manifests, run stdouts/meta, freeze-check stdouts;
  V39 case — preregistration, freeze manifest, `build_row_bridge_v39.py`,
  `ROW_BRIDGE.json`, `solve_w19_compatibility_v39.py`,
  `validate_w19_compatibility_v39.py`, `mutate_target_v39.py`,
  `run_aws.sh`, both lanes' results/evidence/mutation/run artifacts;
  upstream — V37 solver/report/`ERRATUM.md`, V23 parser
  `census_j2_typed_v23.py`, pinned V23/V28/V30/V33/V35 result objects and
  row coefficient files (including raw `Tg19_7_q.poly`), and the
  first-occurrence symbol report.
* Writes/edits: exactly one repository file was created — this report,
  `xmodel/max12-812-order2-p0-total-rees-j2-a1-v38-v39-hostile-review-fable5-20260827.md`.
  No campaign artifact was edited, moved, or deleted.
* `jc2-lean` was not read, entered, built, status-inspected, edited,
  staged, cleaned, or otherwise touched.
