# Hostile review: TD6 raw `H=P3=0` quotient-field closure

| Field | Value |
|---|---|
| Reviewer | claude (different-model hostile reviewer) |
| Date | 2026-08-25 |
| Report under review | `xmodel/td6-c1-c2-c3-p3-raw-curve-aws-20260825.md` |
| Case under review | `cases/td6_c1_c2_c3_p3_raw_curve_aws_20260825/` |
| Origin dependency read | `cases/td6_c1_c2_c3_trivariate_checkpoint_20260825/` (README, `B_LOCAL_RESULTANT_STRATA` context, MANIFEST, FREEZE, v14 `origin.stdout`/`origin.meta`, v11 `tricenter-h-zero`/`tricenter-u-zero`, v12 `tricenter-u-h-zero`, v15 `v-h-zero`) plus `xmodel/td6-c1-c2-c3-trivariate-checkpoint-erratum-20260825.md` and `xmodel/td6-c1-c2-c3-trivariate-checkpoint-20260825.md` |
| Source-typing parents | the CONFIRMED two-center review `xmodel/td6-c1-c3-two-center-cover-review-claude-20260825.md` and its parent chain (jet coefficients `(c1,c2,c3)` of `x = c1·s + c2·s² + c3·s³ + t·s⁴`, tail `t` a system unknown; `K=Q[S]/(F)`, `E=K[A]/(A³−ALPHA)`; `k = 252−342S+144S²−36S³`), plus the sibling frozen lanes `td6_c1_c3_two_center_cover_20260824/evidence/v6,v7` for producer conventions |
| Overall verdict | **CONFIRMED** (no false identity, no missing stratum, no missing hypothesis; every hand-checkable printed identity re-derived and exact; two wording defects and the usual archived-producer residuals disclosed below, none charged to the mathematics) |

Every file in the case directory except the binary archive was read in full,
together with the charged report, the erratum, the origin dependency, and the
prior-certificate lanes needed for the cross-package union.  No PASS marker
was accepted without either hand re-derivation of the printed data or an
explicit disclosure below.  No repository byte was modified other than the
creation of this file.

## 1. Charged hashes and cross-pin audit

All ten charged hashes are internally consistent across every frozen record
that states them:

- report `a15c85c5…` = `FREEZE.sha256` line 2; manifest `9586…` =
  `FREEZE.sha256` line 1; dependency pin `6d366b00…` = `MANIFEST.sha256`
  line 1.  The freeze file `ddbf7dff…` is the root of trust and is pinned
  only by the charge itself (normal for this repo's layout).
- archive `b207bbba…` = `MANIFEST.sha256` line 3 = `archive_sha256` in both
  lane metas = README; source manifest `7b00ab87…` and producer `1b492ad2…`
  appear identically in both lane metas and the README.
- ascending stdout `c38471a0…` and reverse stdout `900c3829…` each match,
  simultaneously, `MANIFEST.sha256`, the corresponding `.meta`
  `stdout_sha256`, the README custody table, and the report.
- prior origin stdout `c31a0f60…` = `DEPENDENCIES.sha256` line 3 = the
  checkpoint's own `MANIFEST.sha256` line 32 = the README citation.  The
  checkpoint MANIFEST hash `d70e8942…` in `DEPENDENCIES.sha256` equals the
  checkpoint `FREEZE.sha256` line 1; the v14 archive hash `d37407c8…` equals
  `origin.meta` `archive_sha256` and the checkpoint README's V14 row; the
  erratum is itself pinned in `DEPENDENCIES.sha256` (`048ba9b4…`), so the
  package cites the erratum-corrected state of its dependency.

`MANIFEST.sha256` covers exactly the 17 non-manifest files present — the
case directory contains 19 files, and only the self-referential pair
`MANIFEST.sha256`/`FREEZE.sha256` is outside the manifest, the first pinned
by the second.  All `supervisor.*` and `source-check.stderr` hashes are
`e3b0c442…`, the SHA-256 of the empty byte string (a known constant), so the
empty-stream claims are exact.  The two nonempty lane stderrs were read:
pure `/usr/bin/time -v` reports ending `Exit status: 0`, whose embedded
command lines equal the meta `command=` fields byte-for-byte, and whose
wall-clock values (39:04.05, 44:15.15) equal the meta UTC intervals
(02:30:29→03:09:33, 02:30:29→03:14:44) to the second.  Both lanes ran the
same pinned archive on distinct AWS hosts (`ip-172-30-0-45`,
`ip-172-30-0-186`) with identical on-host source-check output (24 `OK`
lines including the producer, hash `2dc8d330…` in both lanes).

## 2. Execution disclosure (reviewer-side, mandatory)

This review session has no shell: no Bash tool and no local computation.
Consequently (i) **no hash above was recomputed** — all matching is frozen
text against frozen text; (ii) the v17 and v14 tar.gz archives could not be
extracted, so the two theorem-producing programs —
`c1_c2_c3_p3_quotient.py` (`1b492ad2…`) and the v14 origin producer
(`ca6afb3d…`, from `origin.meta`) — were **not read**; their bytes are
pinned by lane metas and verified on-host against the hash-pinned
`SOURCE.sha256`.  What was read instead: both complete lane stdouts, all
metadata and stderr, the dependency lattice, and the sibling frozen lanes
(v6/v7 two-center, v11/v12/v14/v15 three-center) that fix the producer
conventions.  Every algebraic identity the frozen bytes make checkable was
re-derived by hand (sections 4–7).  A probe is staged at
`/tmp/td6_p3_raw_curve_probe_claude.py`; it recomputes every charged and
manifest hash, extracts both archives, verifies `SOURCE.sha256`, pins the
producers, lists the exact semantic points to read in the producer, and
re-derives the tower algebra.  The verdict rests on the hand algebra, the
frozen attestations, and the cross-pinned custody lattice, with section 11
naming what only a shell-bearing session can close.

## 3. Charge 1 — source typing and specialization

The lanes print `center_stratum=H=C-3U^2=0, P3=0 over Frac(Q[U,V]/P3)` and
`weighted_scaling_used=false`; the run is over a genuine generic point of
the curve, not a numeric sample — a point sample could not produce the
symbolic `U`-power charts, the termwise polynomial clearing counts, or the
transport event norms below.  Identity with the licensed three-center
system is corroborated on four independent axes against the checkpoint's
v11 `H=0` surface lane (`C=3U²` over `Q(V,U)`, a *different* field
implementation): identical transport rank `3470/3602`, identical first rank
`38/132`, identical genuine-P12 term count `2885`, and — decisively — the
two transport events occur at the same rows with the same keys and pivot
columns (`4804, ('f','X',-1,2), 194` and `5282, ('g','X',0,1), 1185`), and
the P3 lanes print exactly the degree-4 field norms of v11's printed pivots
`-V` and `2U` (hand-checked in section 4).  The certificate is expressed
against **original transported first rows**
(`source_relation_original_first_row_replay=true` with a plus-one negative
control), so no echelon artifact enters the lift; the transported rows
trace to the same frozen source modules whose bytes the on-host
source-check verified (including `first_c1_c3_mpoly.py`,
`transport_c1_c3_mpoly.py`, `c1_pencil.py`).  A re-run of the two-center
v7 code path instead of the three-center curve is excluded: v7's field is
`Q[U]/(128U⁶−32U³+1)` with `KP_inverse_count=7590` and no `V` variable,
while these lanes carry the `(U,V)`-tower, `-V`-pivot norms, three
inversion counters at `7589` (matching v11's `Rat3_inverse_count=7589`
exactly), and the distinct marker `TD6-C1-C2-C3-P3-QUOTIENT PASS`.

## 4. Charge 2 — function-field fidelity (all hand-verified)

Let `q(Z) = Z²−32Z+128` and `P3 = V⁴−32V²U³+128U⁶`.

- **Layer 1 is a field.**  `disc(q) = 1024−512 = 512`, and `√512 = 16√2 ∉
  Q`, as printed (`Z_discriminant=512`, nonsquare).  Irreducibility over
  `Q(U)` follows because `Q` is algebraically closed in `Q(U)`: a rational
  function with `f² = 32f−128` is integral over `Q[U]`, hence a polynomial,
  hence constant by degree, hence a rational root of `q` — none exists.
- **Layer 2 is a field.**  `v_U(ZU³) = 3` is odd (`Z` is a nonzero
  constant of `Q(U)(Z)`), and every square in `Q(Z)(U)` has even
  `U`-valuation, so `V²−ZU³` is irreducible — as printed
  (`ZU3_U_valuation=3`).  Total degree `4` over `Q(U)`.
- **It is the function field of `P3`, with irreducibility derived, not
  assumed.**  In the tower, `V⁴ = Z²U⁶ = (32Z−128)U⁶ = 32U³·V²−128U⁶`, so
  `P3(U,V)=0`; conversely `Z = V²U^{−3} ∈ Q(U)[V]`, so the tower equals
  `Q(U)(V)` and the minimal polynomial of `V` has degree 4.  Since `P3` is
  monic of degree 4 and annihilates `V`, it **is** the minimal polynomial,
  hence irreducible over `Q(U)`; by Gauss (content of `P3` in `V` over
  `Q[U]` is 1), `P3` is irreducible in `Q[U,V]`.  Equivalently
  `Res_Z(q, ZU³−V²) = P3` — the conjugate product
  `(V²−Z₁U³)(V²−Z₂U³) = V⁴ − (Z₁+Z₂)U³V² + Z₁Z₂U⁶` with `Z₁+Z₂ = 32`,
  `Z₁Z₂ = 128` reproduces `P3` monomial-for-monomial.  So there is exactly
  one component, no set-theoretic loss, and the tower is a field, hence
  reduced: no nilpotent adapter.  The printed flags state exactly these two
  layer facts plus `P3_relation_exact=true` and a
  `P3_plus_one_negative_control` that perturbs the relation and must fail —
  evidence the modulus is genuinely used.
- **Implementation cross-checks.**  The transport event norms are exact:
  `N(−V) = N(V) = (V·(−V))·(V'·(−V')) = V²V'² = (Z₁U³)(Z₂U³) = 128U⁶` and
  `N(2U) = (2U)⁴ = 16U⁴`, matching `norm_num=(128*x^6)` and `(16*x^4)`
  byte-for-byte, at the same rows/keys/columns as v11's pivots `-V`, `2U`.
  Inverting `-V` clears exactly this norm denominator
  (`1/V = V(32−Z)/(128U³)` since `Z(32−Z)=128`), so the only exception
  locus is `U=0` — and on the curve `V=0` already forces `U=0`.  The three
  layer counters `RatU/Quad/Curve_inverse_count=7589` are equal (consistent
  with 1:1:1 norm descent) and equal v11's single-layer count for the same
  elimination.
- **Robustness note.**  The base coefficients live over
  `E = K[A]/(A³−ALPHA)`; whether `q` stays irreducible over `E` is not
  needed and not claimed (the printed degree statement is over `Q(U)`,
  where it is proved): the kill rests on the cleared identity of section 6,
  which specializes componentwise even through an étale (split) scalar
  extension, with `−k/50` a unit in every component.

## 5. Charge 3 — the compatibility certificate

- **Ranks.**  `3470/3602` and `38/132` in both lanes, with
  `transport_compatibility_count=0` and `first_incompatibility_count=0` —
  on this curve the band is consistent and the kill genuinely needs P12,
  exactly as on the parent `H=0` surface (v11, same ranks).
- **Genuine P12.**  `raw_terms=2885` equals the v11 `H=0` count — no
  band-variable term collapses on the curve — and the lanes carry the
  `genuine P12 PASS` marker of the reviewed lineage.  `raw_sha256` differs
  from v11's, as it must (different coefficient representation).
- **`remainder_sha256 ≠ expected_sha256` is not a defect.**  The same
  inequality-with-`remainder_is_expected_constant=true` pattern appears in
  every frozen PASS sibling (v7, v11, v15 all print `93121eef…` vs
  `b9445255…`): the two hashes pin different serializations (computed
  remainder object vs expected constant), and equality is asserted by exact
  field comparison.  The V14 b-local lane shows the flag is honest — there
  it printed `false` on a 1,681-term remainder.  The P3 lanes' pair
  (`12df78ff…`/`84fd09d5…`) differs from the siblings' because the tower
  serializes differently; both lanes print the identical remainder hash,
  which is meaningful since they share one representation.
- **`−k/50` is a unit.**  From the CONFIRMED two-center review:
  `k = 252−342S+144S²−36S³` is a nonzero polynomial of degree `3 < 6 =
  deg F` in `K = Q[S]/(F)` with `F` irreducible (Rabin certificate audited
  there), so `k ∈ K^×`; a unit's image under any ring map into the
  `E`-extended tower (or any residue algebra of it) stays a unit.
- **Original rows and controls.**  Ascending lifts through 28 nonzero
  original transported first rows with 1,540 multiplier terms; reverse
  through 38 rows with 2,152 terms; both print
  `source_relation_original_first_row_replay=true` and a plus-one negative
  control — in both pivot orders, as charged.  The 28-row ascending support
  matches the rigid 28-row support of every ascending H-restricted parent
  (v7: 28/1,540; v11: 28/1,515; generic checkpoint: 28/1,489).
- **Independence verdict.**  The two lanes are genuinely independent **at
  the first-band/P12 stage**: different pivot orders produced materially
  different certificates (28 vs 38 rows, 1,540 vs 2,152 terms, relation
  denominators `U⁵` vs `U⁷`, termwise `U⁷` vs `U⁹`, slot counts 31,976 vs
  60,121, charts `U¹⁷` vs `U¹⁹`) converging on the same unit.  They are
  **not** independent at the transport, tower-arithmetic, or P12-compile
  stages: those are the same producer bytes and the transport phases are
  byte-identical.  This shared failure mode is real but mitigated outside
  the package: transport structure, ranks, event locations, and term counts
  are reproduced by the checkpoint's v11 lane over a different field
  implementation, the event norms re-derive by hand, and each lane carries
  its own representation-independent original-row replay with plus-one
  control.  The README's own wording ("two deterministic exact **first-stage**
  pivot orders") scopes the claim correctly.

## 6. Charge 4 — localization and clearing

Every printed denominator is a pure power of `U`
(`only_U_exception=true`): raw `U²`, first `U²`, relation `U⁵`/`U⁷`,
termwise `U⁷`/`U⁹` (relation divides termwise in both lanes, as it must),
transport chart `U⁶` (the lcm of the two event norm denominators `U⁶`,
`U⁴`).  The certificate charts decompose exactly as
`6+2+2+7 = 17` and `6+2+2+9 = 19` — transport + raw + first + termwise —
so `U¹⁷` and `U¹⁹` are complete and conservative.  The printed exponents
are internally verified by the termwise clearing checks (31,976 and 60,121
cleared source slots: each product `chart · mᵢ · rowᵢ` checked to be a
polynomial), and for the theorem only the radical matters: the excluded
locus is `{U=0}` either way.

**Why this licenses all of `D(U)`, not only the generic point.**  The
frozen flags (`cleared_relation_coefficients_polynomial=true`,
`termwise_polynomial_clear_checks=true`, original-first-row replay) assert
a denominator-cleared, coefficientwise polynomial identity
`U^N·P12 = U^N·(−k/50) + Σ U^N·mᵢ·rᵢ` in
`(E ⊗ Q[U,V]/(P3))[1/U]`, affine-linear in the band variables.  For any
point `p=(u₀,v₀)` of the curve over any extension field `Ω` with `u₀≠0`,
evaluation `U↦u₀, V↦v₀, Z↦v₀²/u₀³` is a well-defined ring map — both tower
relations evaluate to `0` at every curve point off `U=0`
(`q(v₀²/u₀³) = P3(u₀,v₀)/u₀⁶ = 0`), which is why component loss is
structurally impossible here — and the row entries specialize (their
denominators are `U`-powers).  Dividing by `u₀^N ≠ 0`: any band assignment
solving the first band at `p` makes every `rᵢ` vanish, forcing
`P12(p) = −k/50`, a unit, while the gate demands `P12 = 0`.  Contradiction
at every point of `D(U)` over every field extension.  Nothing restricts to
rational points, and no chart gap exists between `D(U)` and the pure-`U`
certificate divisors.

## 7. Charge 5 — the raw complement at `U=0`

- **Hand-exact complement.**  On `H=P3=0` with `U=0`: `P3(0,V) = V⁴`
  forces `V=0` set-theoretically, then `H = C−3·0 = C` forces `C=0`.  The
  complement is exactly the raw center origin `(C,V,U)=(0,0,0)` — the same
  point and section as the v14 lane's `center_stratum=C=V=U=0`.  Embedded
  multiplicity (`V⁴`) is precisely what the explicitly *set-theoretic*
  claim waives.
- **The origin certificate.**  `origin.stdout` (`c31a0f60…`, pinned in the
  checkpoint MANIFEST and DEPENDENCIES) is a **transport-band**
  incompatibility: rank `3468/3602`, one incompatibility with a fully
  printed 21-original-row certificate, all coefficients `±1`, combination
  and residual denominators `(1)`, certificate chart `(1)` (a unit chart —
  no localization at all), residual an explicitly printed constant vector
  of the degree-18 field `E` with leading coordinate `1` (nonzero, hence a
  unit since `E` is a field per the audited parent certificates),
  `original_row_replay=true`, plus-one negative control,
  `whole_stratum_killed=true`, first band and P12 skipped as the transport
  is already inconsistent.  Its meta pins archive `d37407c8…` and producer
  `ca6afb3d…`, rc=0.
- **Erratum impact: none.**  The V14 B3 erratum narrows only the b-local
  lane's interpretation (its 1,681-term non-constant remainder and the
  non-complete resultant cover); the origin is a separate lane
  (`--stratum=origin`) whose printed content stands alone, and the erratum
  itself states the raw `U=0` closures are unaffected.  The package pins
  the erratum hash, so the citation is erratum-aware.
- **Wording defect (flagged, non-blocking).**  Both the charged report
  ("killed by a unit-chart **first-band** certificate") and the case README
  ("proved it **first-band** inconsistent with a unit chart") misname the
  band: the frozen origin certificate is a *transport*-band
  incompatibility (`first_band_and_P12_skipped_transport_empty=true`).
  The cited file, hash, unit chart, and emptiness conclusion are all
  correct, and the transport gate is if anything earlier and stronger, so
  no promoted statement depends on the mislabel — but a successor erratum
  line should correct the word.

## 8. Charge 6 — composition and scope

- **Whole-curve union.**  `{H=P3=0} = {H=P3=0, U≠0} ∪ {origin}`; the first
  piece is this package (both pivot orders), the second the v14 origin
  certificate.  Both frozen, both at the same source-typed gate of the
  same section.  The set-theoretic whole-curve conclusion is valid.
- **`H=0` debt removal.**  Within the fixed section's `H=0` surface, the
  frozen cover is exact and was verified lane-by-lane: `{H=0, UVP3≠0}` by
  v11 `tricenter-h-zero` (its certificate chart factors exactly as
  `V⁵·U⁶·P3`, hand-matching the claimed exception divisor `U·V·P3`);
  `{H=0, V=0} = {V=H=0}` off `U` by v15 `v-h-zero` (chart `U¹²`, remainder
  `−k/50`), whose `U=0` point is the origin; `{H=0, U=0} = {C=U=0}` split
  as `V≠0` by v12 `tricenter-u-h-zero` (chart `V³`, constant residual
  `−9+3S` block identical to the v11 `u-zero` lane, same row 13, key
  `('X-2',14)`, matching the two-center lineage) plus the origin; and
  `{H=0, P3=0}` by this package plus the origin.  Every piece survives the
  erratum by the erratum's own scope statement.  So the claim "no
  remaining producer-exact raw debt on the fixed-section `H=0` divisor" is
  exactly right — while generic `B3=0` remains open, it is a different
  divisor and the package nowhere claims it (PROGRESS records "Raw B3
  remains").
- **Honest flags and scope.**  Both lane stdouts print
  `P3_generic_open_killed=true` but `P3_whole_curve_killed=false`,
  `full_three_center_family_killed=false`, `SP2_killed=false`,
  `JC2_resolved=false` — the producer claims only the open; the whole-curve
  and whole-`H=0` statements are correctly presented as cross-package
  compositions in the README/report, which also disclaim neighborhood,
  full-centering, boundary/dead-stretch, SP-2, maximum-degree, and JC2
  claims.  The strongest statement is exactly the fixed source-typed
  three-center section, as charged.
- **Custody remarks.**  (i) The checkpoint README called the P3 replay
  "the live V16 successor", and the delivered archive is v17; no frozen
  v16 artifact or mention exists anywhere in the repo.  Given this
  project's record of disclosing failed versions (V10, V13), the likeliest
  reading is a skipped handoff build; the delivered v17 lanes carry their
  own on-host source checks and internal controls, so nothing rests on
  version continuity — but a one-line note in a successor would close the
  question.  (ii) Unlike the origin's fully printed 21-coefficient
  certificate, the P3 lanes freeze only aggregate lift data (row/term/slot
  counts, booleans, hashes), not the 1,540/2,152 multiplier terms; this
  matches the accepted v7/v11 convention, and the replay flags plus
  negative controls stand in for the unprinted bytes.  (iii) The producer
  and `SOURCE.sha256` exist only inside the pinned archive (see section 2).

## 9. Smallest defect found

**No false identity, missing stratum, or missing hypothesis was found.**
Every checkable printed identity re-derived exactly: the two tower-layer
irreducibility facts, `Res_Z(q, ZU³−V²) = P3` with `Z₁+Z₂=32`, `Z₁Z₂=128`,
the derived (not assumed) irreducibility of `P3` over `Q(U)` and `Q[U,V]`,
both transport event norms `128U⁶` and `16U⁴` against v11's pivots `-V` and
`2U`, the chart decompositions `17 = 6+2+2+7` and `19 = 6+2+2+9`, relation
| termwise divisibility, `U=0 ⇒ V=0 ⇒ C=0`, the nonzeroness of `k` in `K`,
the unit-ness of `−k/50` under every scalar extension in scope, the
nonzero constancy of the origin residual, the empty-string stderr constant,
and the second-exact agreement of meta intervals with the `time -v`
reports.  The smallest actual defect is the **"first-band" mislabel of the
v14 origin transport certificate** in the charged report and README
(section 7), a wording error about a dependency's mechanism that changes no
conclusion; after it come the disclosed custody softnesses: archived-only
producers (bytes pinned, semantics unread here), no reviewer-side hash
recomputation (no shell), aggregate-only lift freezing, and the v16→v17
numbering gap.  None of these blocks the theorem at its claimed scope.

## 10. Promotable sentence and strict scope

> Under the frozen TD6 three-center source typing of archive `b207bbba…` —
> the reviewed transport patterns, rhs normalization, pole data, and
> centering jet `x = c1·s + c2·s² + c3·s³ + t·s⁴` with section
> `(c1,c2,c3) = (C,V,U)` and tail `t` a system unknown — the set-theoretic
> curve `H = C−3U² = 0`, `P3 = V⁴−32V²U³+128U⁶ = 0` contains, over every
> field extension of `Q`, no parameter point admitting a solution of the
> transported system at the first-band/genuine-P12 gate: off `U=0`, two
> independently frozen first-stage pivot orders reduce the 2,885-term
> genuine P12 — over the degree-4 function field
> `Q(U)[Z,V]/(Z²−32Z+128, V²−ZU³)` of the irreducible curve — through 28-
> and 38-original-transported-first-row lifts whose every denominator is a
> power of `U` (complete charts `U¹⁷`, `U¹⁹`, termwise-cleared over 31,976
> and 60,121 slots, plus-one controls passing) to the constant unit
> `−k/50` with `k = 252−342S+144S²−36S³ ∈ K^× = (Q[S]/(F))^×`, and the
> single remaining point `U=0`, namely the origin `C=V=U=0`, is
> transport-inconsistent by the separately frozen 21-original-row
> unit-chart certificate `c31a0f60…`; consequently the fixed section's
> `H=0` divisor carries no remaining producer-exact raw debt, its frozen
> cover `{UVP3≠0} ∪ {V=0} ∪ {U=0} ∪ {P3=0}` now being closed lane by lane.

Strict scope: this fixed, source-typed, normalized three-center section
only, at the producer's gate, conditional on the frozen parent chain and on
the archived producers meaning what their printed certificates and controls
say (section 11).  Not promotable: any neighborhood or full-centering
statement, the generic `B3=0` divisor (still open per the erratum),
boundary/dead-stretch moduli, SP-2, maximum-degree, or JC2.

## 11. Residual conditions

A shell-bearing session should run, from the repository root,
`python3 /tmp/td6_p3_raw_curve_probe_claude.py`, which closes: every
charged and manifest byte hash (this session recomputed none), extraction
of the v17 and v14 archives with full `SOURCE.sha256` verification, the
producer pins (`1b492ad2…`, `ca6afb3d…`), and independent re-derivation of
the tower algebra.  It should then read, inside the extracted v17 archive,
`c1_c2_c3_p3_quotient.py` to confirm: `remainder_is_expected_constant` is
an exact field equality against `−k/50`; `remainder_is_constant_unit`
exhibits an inverse; the `RatU/Quad/Curve` inversions are unit-asserted at
the point of use; the termwise clearing covers every slot of every cleared
product; `--reverse-first` permutes only the first-stage pivot order; and
the `P3_relation_exact`/plus-one controls are implemented as advertised —
and, in the v14 archive, the `--stratum=origin` path of the origin
producer.  Every relation checkable by reading in this session is
consistent; a failure of any listed check would reopen this review.

CONFIRMED
