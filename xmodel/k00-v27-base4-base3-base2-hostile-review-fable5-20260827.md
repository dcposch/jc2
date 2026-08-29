# Hostile different-model review: K00 V27 rank filtration R1/R2/R3 (BASE4, BASE3, BASE2)

Reviewer: **Fable 5** (`claude-fable-5`, Anthropic), hostile exact-algebra
review, different model from the producer chain.
Date: 2026-08-27.

Reviewed frozen producer reports, in dependency order:

| # | report | SHA-256 |
|---|---|---|
| 1 | `cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827/RESULT_V27_BASE4_R1_EXACT_PREPASS.md` | `19c8795589ce076c2414474a6341c7929d578958ea122a6745f26ea6ab46bd9c` |
| 2 | `.../RESULT_V27_BASE3_R2_EXACT_PREPASS.md` | `c42c0482f0b5861f5099e6e121c60a93d018c87a9619749ee1844f5954545c39` |
| 3 | `.../RESULT_V27_BASE2_R3_EXACT_PREPASS.md` | `5f9700c7e67eaa5255ef642ff4e784983d71da9f8c5394d6cb01245c9c0a873d` |

Review manifests, full bytes verified on disk (the abbreviated reminders in
the tasking match these):

- `REVIEW_PACKET_BASE4_R1.sha256` = `41d1107589f33b7f7fab4ec5cac6e47ffc72368dfeeb93981ae2e921a9eb0205`
- `REVIEW_PACKET_BASE3_R2.sha256` = `e3cd6586c2db1b51aabedb613f3de5a18c81a14b26bd8a6f9ae42af4b68626f3`
- `REVIEW_PACKET_BASE2_R3.sha256` = `86c561915a5336792674c7c7c3fd5e181d626b470ae9a4302166dad824adadcd`

Method: all verdict-bearing algebra was re-derived on the reviewer's desk in
pure Python exact rational arithmetic (own sparse-polynomial engine, own
Laplace-expansion minors, own Buchberger completion and independent
Buchberger-criterion checker, own leading-term-ideal dimension computation),
with **no trust in any producer status string, marker, or prior standard
basis**.  The frozen Singular replays were inspected line by line; one small
**read-only census diagnostic** (composed from the frozen R3 branch script
prefix plus print statements, SHA-256
`5f3f5a6a5296f6eb4b4bf0ef52c5ec0b0422b0e365f35b2705a2b3e8b230dc64`) was
executed on the audited idle producing node itself (AWS r6a
`i-02cb2b4a379ffcc64` = `ip-172-30-0-34`, load 0.00, Singular 4.3.2, same
engine build as the frozen runs; diagnostic file removed after use).  No case
file was modified; `jc2-lean` was not entered.

## Verdict summary

| item | verdict |
|---|---|
| R1 (BASE4): `I4(A) ⊆ B+I5(A)`, `J3base = J4base` proper, affine dim 3 | **CONFIRMED** |
| R2 (BASE3): `I3(A) ⊆ J3base`, `J2base = J3base = J4base` proper, dim 3 | **CONFIRMED** |
| R3 (BASE2): `J1base` proper, dim 2; `I2(A) ⊄ J2base`; strict cut `J1base ≠ J2base`; origin correction | **CONFIRMED WITH REPAIR** — the preregistered "exact `I2OUTSIDE` count" recorded as **237 is REFUTED; the true census is 291 of 351** (60 inside).  Mechanism proven below.  All ideal-theoretic and geometric conclusions survive and are, if anything, strengthened. |
| R0 fail-closed history + erratum | **CONFIRMED** (quarantine complete; one imprecise mechanism sentence in the erratum, noted below, repair itself correct) |
| Coordinator scope correction (trivial homogeneous origin point) | **CONFIRMED** |
| Producer refusal to over-infer from `J1 ≠ J2` | **CONFIRMED** as stated at producer tier; post-review corollaries stated precisely below |

No SCOPE-CONFLICT was found: every consumed input is inside the frozen
six-variable chart, and no run consumed a sampled-pencil claim, `b`, or the
prior compiler.

## 1. Custody and hash audit (complete)

All of the following replayed **clean, zero mismatches**, against current
bytes:

- The three review packets (15 + 16 + 13 entries), including the chained V26
  atlas/compiler pins, the V26R1F producer report and its hostile review, and
  the V27 successor design.
- Source-freeze manifests `SOURCE_FREEZE_BASE4.sha256` (8 entries),
  `SOURCE_FREEZE_BASE3_R2.sha256` (46 entries, as the R2 report claims),
  `SOURCE_FREEZE_BASE2_R3.sha256` (22 entries), plus the two auxiliary
  freezes (origin, constant-kernel).
- Portable harvest manifests: `HARVEST_REPLAY_BASE4_R1.sha256` (24 lines),
  `HARVEST_REPLAY_BASE3_R2.sha256` (26), `HARVEST_REPLAY_BASE2_R3.sha256`
  (26), plus origin and constant-kernel harvests.
- On-node `EVIDENCE.sha256` for R1 (20), R2 (25), R3 (25), R0, origin,
  constant-kernel.
- Path coverage: R2/R3 evidence manifests cover **every** file in their
  trees except themselves; harvest = evidence entries + the evidence manifest
  itself (25+1=26), exactly as reported.  R1's on-node evidence manifest
  omits three files (launcher pid, outer stdout/stderr, written after
  manifest creation); the 24-line portable harvest covers them, matching the
  R1 report's wording.  R2/R3 close this gap on-node via the
  `evidence_finalization.txt` copy-then-rehash step.
- Every custody hash quoted in the three reports (source freeze, immutable
  archive, endpoint `RESULT.json`, evidence manifest, portable manifest,
  standard basis, tracked transform, label set) matches the on-disk bytes and
  the launch registrations.
- Remote custody: the four immutable source archives on the producing node
  (`/home/ubuntu/jobs/<tag>_source.tar.gz` for R0, R1, R2, R3) hash exactly
  to the registered `source_archive_sha256` values
  (`7538ef57…`, `ec7763ab…`, `1a002197…`, `598df222…`).
- The byte-identity claim for the nine-element basis is verified **as
  custody only**: `BASE4_STANDARD_BASIS.txt` (R1), `BASE3_R2_STANDARD_BASIS.txt`
  (R2), and the reviewed V26R1F `EXACT_PREPASS_STANDARD_BASIS.txt` all hash to
  `c8aa23e46f909e70c2c8d302ca67a415496df9a969f99817d2ef593f60f614c0`.  No
  proof weight rests on this identity anywhere in this review.
- Telemetry: `FINAL.validation` for R1/R2/R3 shows rc 0, walls 3.28 s /
  3.62 s / 3.65 s, max RSS 509,120 / 509,168 / 508,948 KiB, `swaps=0` — all
  exactly as the reports state.  Caps in the launch registrations
  (21,600 s outer / 21,000 s inner / 402,653,184 KiB VM) match the reports.
  All Singular stderr streams and all outer streams hash to the empty string.
  Endpoint statuses are members of the preregistered allowed-outcome lists.

## 2. Reconstruction of `A`, `B`, and every literal minor; censuses

From the byte-frozen V26 atlas (`ATLAS_EXACT_POLYNOMIALS.json`,
`d7ec6d18…`) I independently parsed the `exact_terms` sparse forms and,
separately, the `singular` string forms of all 49 entries of `A`, the six
grade-2 rows (row 6 is literally zero), and `F10`; the two atlas encodings
agree, `B = (G2_row1..G2_row5, G2_row7, F10)` matches the claimed provenance,
and the literal `A` and `B` embedded in **all ten** frozen `.sing` scripts
(R0 + 3×{branch, tracked, replay}) are polynomial-identical to the atlas.
Every script's ring line is `ring R=0,(d0_1,…,d5_1),dp` (exact Q, degrevlex).

Structure verified: every entry of `A` is homogeneous (degree 1 in columns
1–6, degree 2 in column 7; row 6 zero except its column-7 quadratic); `B` is
homogeneous of degrees (2,2,2,2,2,2,4).  The auxiliary constant-kernel
identities were re-proved in my own arithmetic:
`(5/1024, 0, 3/128, 0, 1/8, 0, 1)·A = 0` and
`A·(2,0,1,0,1,0,0)^T = A·(0,1/16,0,1/2,0,1,0)^T = 0`.  Two independent
constant right-kernel vectors force `rank A ≤ 5` identically, which is a
structural proof that all 49 six-by-six determinants vanish.

I then computed **every** literal determinant myself (Laplace expansion with
subset dynamic programming, exact `Fraction` arithmetic; engine self-tested
against a naive cofactor determinant and a textbook Gröbner example):

| ideal | labels (= C(7,k)²) | nonzero | zero | unique nonzero |
|---|---:|---:|---:|---:|
| `I6(A)` | 49 | 0 | 49 | 0 |
| `I5(A)` | 441 | 90 | 351 | 54 |
| `I4(A)` | 1,225 | 594 | 631 | 491 |
| `I3(A)` | 1,225 | 813 | 412 | 725 |
| `I2(A)` | 441 | 351 | 90 | 326 |

Every figure matches the reports and the R3 preregistration table, including
the unique-nonzero column.  The Singular `+`-dedup censuses were also
re-derived: counting scalar-proportionality classes of
{`B` ∪ nonzero minors} gives exactly **7 → 9 → 74 → 354 → 541** after
adding `B`, `I5`, `I4`, `I3`, `I2` — reproducing `NGEN=74/354/541`
independently (and 9 = the V26R1F `B+I5(A)` generator count).

Row/column-label completeness: all four frozen label files (R1 ranks 4–6, R0
ranks 4–6 byte-identical to R1's, R2 ranks 3–6, R3 ranks 2–6) list **every**
row/column subset exactly once per rank.  Verified as sets against the full
combinatorial enumeration.

## 3. The containments, the 351 normal forms, and the strict cut — proved independently

I computed my own characteristic-zero degrevlex Gröbner basis of
`J4base = B + I5(A)` from scratch (Buchberger with interreduction; final
basis passes my independent S-pair criterion checker): **9 elements**, LM
degrees {2,2,2,2,3,3,4,5,5}, `NF(1) = 1` (proper), and
`dim R/J4base = 3` by maximal-independent-set computation on the
leading-term ideal (valid since the order is global and the ideal is
homogeneous).  All 7 `B` generators and all 90 stored `I5` minors reduce to
zero against it.

- **`I4(A) ⊆ B+I5(A)`: PROVED.** All 594 stored nonzero 4×4 determinants
  (and trivially the 631 zero ones) have zero normal form modulo my basis.
  Hence `J3base = J4base` as ideals, proper, affine dimension three.  R1's
  headline is confirmed: the promoted rank-≤4 coefficient-base scheme is
  already rank-≤3 scheme-theoretically; BASE4 does **not** prove rank purity
  at four.
- **`I3(A) ⊆ B+I5(A)+I4(A)`: PROVED.** All 813 stored nonzero 3×3
  determinants have zero normal form.  Hence
  `J2base = J3base = J4base`, proper, dimension three.  R2 confirmed.
- **`I2(A)` normal forms: all 351 recomputed — the claimed outside count
  237 is REFUTED; the true count is 291.**  Exactly **60** of the 351 stored
  nonzero 2×2 determinants lie in `J2base` and **291** do not.  This was
  established twice, by two disjoint reduction paths: (i) normal forms
  against my own criterion-verified basis, and (ii) normal forms against the
  producer's own nine-element basis, which I first verified independently to
  be a Gröbner basis (all S-pairs reduce to zero) of the same ideal (mutual
  reduction of generators in both directions).  Membership is
  basis-independent, and both paths give 60/291.  The 60 interior minors have
  a clean pattern: row pairs drawn from ten of the 21 row pairs and column
  pairs concentrated on the six pairs containing column 7 plus six others.
- **Mechanism of the wrong 237, proven on the producer's own engine.**  The
  R3 counting loop is
  `for (mi=1; mi<=size(I2MOD); mi++) { if (I2MOD[mi]!=0) { i2outside++; } }`.
  In Singular, `reduce(I2A, SJ2)` preserves the slot structure
  (`ncols = 441`, zeros included), while `size()` counts only nonzero slots.
  The read-only diagnostic on the producing node (same host, same Singular
  4.3.2, frozen script prefix) returned:

  ```text
  DIAG_NCOLS_I2A=441          DIAG_SIZE_I2A=351
  DIAG_NCOLS_I2MOD=441        DIAG_SIZE_I2MOD=291
  DIAG_TRUE_NONZERO_OVER_NCOLS=291
  DIAG_PRODUCER_STYLE_LOOP_COUNT=237
  DIAG_NGEN_J1=541
  ```

  So the loop iterated only over the first 291 slots and found 237 nonzero
  there; the correct census over all slots is **291**, agreeing exactly with
  my desk computation.  The frozen marker `K00_V27_R3_I2OUTSIDE=237`, the
  endpoint field `I2_entries_nonzero_mod_fresh_J2base_basis: 237`, and the
  report sentence "237 of 351 stored nonzero I2(A) entries have nonzero
  normal form" are all wrong as censuses and must be corrected to 291 by a
  registered erratum before any successor consumes a per-slot count.
  The qualitative claims are unaffected (any positive count yields
  `I2(A) ⊄ J2base` and the strict cut; 291 > 237 makes the cut claim
  stronger, in the conservative direction).
- **`J1base = J2base + I2(A)`: proper of affine dimension 2 — PROVED.**  My
  own Gröbner basis of `J1base` (10 elements, criterion-verified) has
  `NF(1)=1` and leading-term dimension 2.  The producer's ten-element
  `BASE2_R3_STANDARD_BASIS.txt` passes my criterion check and generates the
  same ideal (mutual reduction both ways); its LMs also give dimension 2.
- **Strict ideal cut `J1base ≠ J2base`: PROVED**, with 291 explicit
  witnesses (each a 2×2 minor in `J1base` whose normal form modulo a
  criterion-verified basis of `J2base` is nonzero — a valid non-membership
  certificate).  The dimension drop 3 → 2 independently forces strictness.

## 4. Tracked transform identities and fresh bases

- **R1 (74×9) and R2 (354×9): VERIFIED ENTRYWISE in my own arithmetic.**
  Reconstructing the generator slot lists (B, then nonzero minors in
  row-major ascending subset order, first-occurrence scalar dedup — 74 and
  354 slots) and multiplying by the frozen transforms reproduces the frozen
  nine-generator `Graw` exactly, all columns.  The embedded replay-script
  `Graw` equals the serialized basis files byte-for-byte in content, and the
  R2 `Graw` is identical to R1's (consistent with equal file SHAs).  This is
  a complete membership certificate for the nine generators in the
  respective ideals: every slot polynomial is by construction a genuine
  determinant of the frozen `A` (or `B` generator).
- **R3 (541×10): VERIFIED via sparse-slot solution.**  My product-order slot
  reconstruction does not reproduce Singular's internal `I2A` slot content —
  the on-node diagnostic shows Singular's `minor(A,2)` object retains all
  441 slots (zeros included) and stores some entries as exact scalar
  multiples of the raw determinants (observed factors −1 and −2, an artifact
  of Singular's recursive minor expansion; scalar multiples generate the
  same ideal and do not affect any census, membership, or class count).  The
  frozen `T` is extremely sparse (nine nonzero rows across ten columns:
  slots 2, 6, 7 of `B` and six `I2`-block slots).  I solved the six
  `I2`-block slot polynomials exactly from the sparse system (columns 3–8 of
  the identity), verified **each is an exact scalar multiple of a specific
  2×2 determinant of `A`** (labels (4,6)×(4,5), (3,4)×(4,5)≡(3,6)×(0,1),
  (0,1)×(0,1)·(−1), (0,1)×(0,3)·(−1), (1,4)×(0,2)·(−2), (1,2)×(0,3)), and
  then verified the four remaining identity columns (1, 2, 9, 10) as
  nontrivial consistency checks — **all hold exactly**.  Together with the
  independent membership proofs of Section 3, the R3 certificate is fully
  verified.  The `TPICK` mutation coordinates ((1,1), (1,1), (2,1)) match my
  parses: the named entries are nonzero, so the preregistered drop/add
  mutations necessarily break the exact identities.
- **Fresh standard bases and dimensions**: recomputed from scratch by me
  (not replayed): properness and affine dimension **three** at the R1 stage
  (`J3base`), **three** at the R2 stage (`J2base`), **two** at the R3 stage
  (`J1base`) — exactly as claimed.

## 5. Controls, R0 audit, and a latent guard defect

- Deletion controls (first nonzero `I4`/`I3`/`I2` slot zeroed, slot must
  change), transform drop/add, forced-unit (`J,1` → unit), known-proper
  (`(d0_1)`), full-literal reverse inclusion, census guards, source-freeze
  refusals, caps, and zero-swap: all present in the frozen scripts, all
  fired per the frozen stdout streams, telemetry consistent, and each
  control's logic inspected and sound (the deletion controls are
  Singular-assignment checks, weak but harmless).  Origin add-one mutations
  in R3 are sound (adding 1 makes the constant term nonzero).
- **R0**: failed closed at `I6_LITERAL_CENSUS` in 1.87 s, before any target
  standard-basis computation, with `engine_rc=1` and validator
  `DEPENDENCY_SOURCE_REPLAY_OR_ENGINE_FAILURE`.  The diff between the R0 and
  R1 branch scripts is exactly the three census-guard constants
  (49→0, 441→90, 1225→594) — nothing else, confirming the erratum.  R0
  produced no basis, no transform, no endpoint JSON; its only output beyond
  streams is a labels file byte-identical to R1's, which I re-verified
  independently.  **R0 cannot contaminate R1/R2**: no artifact of R0 is
  consumed anywhere, and every R1/R2 quantity was re-derived here from the
  atlas alone.  One imprecision: the erratum sentence "`minor(A,r)` omits
  zero polynomial entries from the stored ideal" conflates `size()`
  semantics with storage — the diagnostic shows `ncols(I2A)=441` (zero slots
  are retained; `size()` skips them).  The repair itself (guards on the
  nonzero counts) is correct.
- **Latent guard defect (repair required before successors)**: the same
  `size()`-bounded loop pattern is used in the reverse-inclusion checks of
  all three replay scripts (`BNF`/`I5NF`/`I4NF`/`I3NF`) and in the
  `i4outside`/`i3outside`/`i2outside` counters.  Whenever a reduction
  introduces new zero slots, such a loop inspects only the first `size()`
  slots and can **false-pass** (a nonzero normal form hiding beyond the
  bound would be missed).  In R1/R2 every relevant normal form is genuinely
  zero (proved here), so all recorded numbers are true and the defect is
  unrealized; in R3 it produced the wrong 237.  Successor runners must bound
  these loops by `ncols()`.

## 6. Scope correction: the homogeneous origin is a trivial rational point — CONFIRMED

I verified homogeneity of every generator myself (Section 2).  Every ideal
in this filtration (`B`, all minors, hence `J4base ⊇ … ⊇` and
`J1base`) is homogeneous, so the affine origin lies in `V(J)` for every one
of them: **the existence of a rational point is trivially true and carries
zero information**.  The coordinator's scope correction is mathematically
correct and correctly propagated into the R3 preregistration
("a unit endpoint is a contradiction, not a purity pass" — indeed a unit
ideal would contradict the origin membership).  The next useful point target
must be **nonzero/projective**, and to bear on the campaign it must
additionally satisfy the source-open and/or full-`P6` compatibility
requirements; a bare `Q`-point of the six-variable base ideal is not
informative.  R3 proves none of those, exactly as it states.

## 7. Refusal audit and the next discriminator — do not launch

The producer refuses to infer from `J1base ≠ J2base` either distinct
radicals or a rank-exactly-two geometric point.  **This refusal is correct
at the producer's evidence tier**: strict ideal inclusion alone does not
separate radicals (e.g. `(x²) ⊊ (x)`), and no point is exhibited.  Post
review, two corollaries now hold rigorously and may be promoted with the
results themselves, stated exactly:

- Since dimension depends only on the radical and I have independently
  confirmed `dim R/J2base = 3 ≠ 2 = dim R/J1base`, the radicals **are**
  distinct, and `V(J2base)(Q̄) ⊄ V(J1base)(Q̄)`.  At any geometric point of
  the difference, all 3×3 minors vanish (`I3(A) ⊆ J2base`, proved) while
  some 2×2 minor does not: the six-variable coefficient-base scheme has a
  **nonempty rank-exactly-two stratum over `Q̄`** — nonconstructively.  No
  explicit point, no rational point, no source-open or full-`P6`
  compatibility is implied.
- The correct next cheap discriminator is the preregistered one-minor
  Rabinowitsch chart: freeze **one specific** 2×2 minor `m` from the 291
  with nonzero normal form (by row/column label and exact polynomial), pass
  to `Q[d0_1,…,d5_1,z]`, and decide `J2base·R[z] + (z·m − 1)`.  Exact
  interpretation: this ideal is proper **iff** `m ∉ √(J2base)` **iff** the
  principal open `D(m)` meets `V(J2base)`, i.e. iff `m` witnesses a
  rank-exactly-two point on its own chart; its dimension is the dimension of
  the rank-two stratum piece `V(J2base) ∩ D(m)`.  Note the per-minor caveat:
  an individual `m` outside `J2base` may still lie in the radical, so a unit
  answer for one minor is not a contradiction; the dimension corollary above
  guarantees only that at least one of the 291 succeeds.  **I did not launch
  this job.**  (Observation, no verdict: two later
  `v27_r3_minor_selection*` lane directories, timestamped 19:23Z/19:27Z,
  exist on the producing node; they are outside the three frozen packets
  under review and are not consumed, reviewed, or blessed here.)

## 8. What may be promoted, and the firewall

Eligible for promotion (six-variable coefficient-base chart
`R = Q[d0_1,…,d5_1]`, frozen V26 `A` and `B`, subject to the campaign's
normal promotion process, and for R3 subject to the census erratum):

1. The full minor censuses of Section 2, including `I6(A) = 0` identically
   (with the constant-kernel structural proof) and the unique-nonzero and
   dedup (`74/354/541`) counts.
2. `I4(A) ⊆ B+I5(A)` and `I3(A) ⊆ B+I5(A)`; hence
   `B+I5(A) = B+I5(A)+I4(A) = B+I5(A)+I4(A)+I3(A)`, one proper homogeneous
   ideal of affine dimension three; equivalently, every geometric point of
   the promoted rank-≤4 base scheme `V(B+I5(A))` has `rank A ≤ 2`.  Neither
   BASE4 nor BASE3 proves rank purity at any rank.
3. `I2(A) ⊄ J2base`, with corrected census **291 outside / 60 inside** of
   the 351 stored nonzero 2×2 minors; `J1base = J2base + I2(A)` proper of
   affine dimension two; the strict scheme-theoretic cut
   `J1base ⊋ J2base`; distinct radicals and the nonconstructive nonempty
   rank-exactly-two `Q̄`-stratum as dimension corollaries (Section 7), with
   no explicit or rational point.
4. The trivial-origin scope correction (Section 6) and the corrected useful
   point target.
5. Required repairs: registered erratum correcting `I2OUTSIDE`/endpoint 237
   → 291 wherever consumed, and the `ncols()` loop-bound fix for all
   successor guards (Section 5).

**Forbidden inferences — none of the following is decided or supported by
these results**: the full prior ideal `P6` (the 27 remaining variables and
the inhomogeneous column `-b`), any grade-seven or later-grade
compatibility, any rank-five chart statement, rank purity at any rank,
rank-0 versus rank-1 separation (`I1(A)` untested), any nilpotent or
later-grade lifting, any finite jet, any formal or convergent arc, any
receiver/K00 later-grade statement, source reachability, closure incidence,
any order-two statement, any maximum-twelve statement, any sampled-pencil
claim, any explicit or rational rank-two point, any counterexample, and JC2
itself.  Until promotion review completes, the three producer endpoints
remain speculative and rollback-tagged as labeled.

## Closing block

- Output path: `xmodel/k00-v27-base4-base3-base2-hostile-review-fable5-20260827.md`
  (this file; its own SHA-256 is reported alongside delivery, since a file
  cannot contain its own hash).
- Reviewed-artifact SHA-256s: reports
  `19c87955…`, `c42c0482…`, `5f9700c7…`; review packets `41d11075…`,
  `e3cd6586…`, `86c56191…`; atlas `d7ec6d18…`; shared 9-gen basis
  `c8aa23e4…`; R3 10-gen basis `a840c9b6…`; transforms `88e306e9…`,
  `b86238ea…`, `1d045d57…`; label sets `69d274d5…`, `02bea82c…`,
  `f1017843…`; diagnostic script `5f3f5a6a…`.
- Model identity: **Fable 5 (`claude-fable-5`)**, hostile reviewer, distinct
  from the producer chain.
- Checks run: full rehash of all packets/freezes/harvests/evidence manifests
  with path-coverage audit; remote archive custody on the producing node;
  independent exact reconstruction of `A`, `B`, all 3,381 literal minors and
  all five censuses (totals, nonzero, unique, dedup classes); label-set
  completeness at ranks 2–6; homogeneity and constant-kernel structure;
  independent Buchberger bases of `J4base` and `J1base` with independent
  S-pair criterion verification of both producer bases; 594 + 813 + 351
  normal-form recomputations under two disjoint reducer paths; properness
  and dimensions 3/3/2; strict-cut witnesses; entrywise verification of all
  three tracked transform identities (R1/R2 by full reconstruction, R3 by
  sparse-slot solution plus consistency columns); control and mutation
  replay; R0 quarantine diff; on-node read-only census diagnostic proving
  the 237→291 loop-bound artifact; timeline and preregistration conformance.
- Scope firewall: this review promotes nothing by itself; it confirms,
  repairs, and refutes exactly as stated above, **within the six-variable
  coefficient-base chart only**, and forbids every inference to full `P6`,
  later grades, an arc, a receiver statement, order two, maximum twelve, a
  counterexample, or JC2.
