# Erratum review (Fable5): correction of the total-support census in the ordered `T-a1` rho=0-to-total DVR design review

Date: 2026-08-27
Reviewer: Fable5, explicit correction review of its own prior hostile report

Adjudicated artifacts (all re-hashed locally, byte-immutable):

```text
e3d263d5c0006bc4f05c5b7ff17bfcbd68bab52f7c1d3ccb5d323facd94448f7
  xmodel/max12-812-order2-p0-total-rees-j2-a1-rho0-to-total-dvr-design-sol-20260827.md          (producer)
a836a978a6b9f05370322fb39c2cf1c45fa6907c337f10ef3ee9456d2e2f0f6d
  xmodel/max12-812-order2-p0-total-rees-j2-a1-rho0-to-total-dvr-design-hostile-review-fable5-20260827.md  (my prior review)
d322d4177d4592d02100a8eaaa7841c463c44d7cd67b44cbdd6529f4bc721808
  xmodel/max12-812-order2-p0-total-rees-j2-a1-rho0-to-total-dvr-design-erratum-v43-sol-20260827.md  (additive erratum)
```

Session constraints honored: desk-scale exact checks only; no AWS launch, no
web access, no `jc2-lean` contact, no canonical-ledger edit; no campaign
artifact modified other than creating this report.  Review scripts staged
under `/tmp` (hashes in the appendix).  Singular 4.4.1 (arm64-Darwin) used
only for a seconds-scale execution of the generated toy-control preamble.
Unlike the prior review, this session **did** rebuild the full literal-total
row corpus from the pinned V20→V28→V33→V35 emitter chain locally (about four
minutes) and recomputed the complete weight-30 preflight censuses (about
sixteen seconds); nothing below rests on trusting the erratum's numbers.

## Verdict summary

| item | verdict |
|---|---|
| 1. Corpus adjudication: the frozen grade-16–19 files are rho=0 specializations; literal re-emission gives a 66th positive variable `ez9` in the unique term `(3/8)*rho^2*a1*ez9` of `Tg19_2` | **CONFIRMED** (the erratum is right; my prior census claim is withdrawn below) |
| 2. Corrected theorem: total ring `Q[rho,X19^tot]`, 66 positive variables, `rho` sole weight-zero variable; `ez9` a polynomial-extension spectator under specialization; ring/map equivalence survives | **CONFIRMED** |
| 3. Preflight dimensions 59 / 460485 / 1370353 / 224938 / 687758 / 8567907, rho0 26200 / 66076 / 616679, max t-degree 4 | **CONFIRMED** — every number reproduced exactly by independent desk recomputation (provenance caveat in §4: the r6d transcript itself is not archived in-repo) |
| 4. Augmented-module Singular repair implements my prior syntax fix | **CONFIRMED** — verbatim preamble executed and passing on Singular 4.4.1 |
| 5. Dense V37 route unsuitable; registered exact question unchanged | **CONFIRMED** (with two freeze-time recommendations, §6) |

The apparent conflict is fully resolved in the erratum's favor, and the
resolution is *consistent with my own prior transcript*: every rho-carrying
byte my prior script saw lived at grades 10–15, because the grade-16–19
frozen files never contained rho to begin with.  The prior review's
mathematical verdicts all survive after substituting the typed census; the
single load-bearing assertion — `rho` is the only weight-zero variable — is
re-verified and *strengthened* on the corrected 67-variable ring.

## 1. Exact adjudication of the 65-vs-66 conflict — erratum CONFIRMED

**Kill sets, verified on producer bytes.**  The four later-grade producers
all specialize rho away at emission time:

```text
prolong_boundary_g16_v28.py:236   killed = parser.J1 | frozenset({"a0", "rho"})
prolong_boundary_g17_v30.py:136   killed = parser.J1 | frozenset({"a0", "rho"})
prolong_boundary_g18_v33.py:123   killed = parser.J1 | frozenset({"a0", "rho"})
evaluate_grade19_orbit_v35.py:126 killed = parser.J1 | frozenset({"a0", "rho"})
```

whereas the V23 census (grades 10–15) uses `v1.J1 | {"a0"}` — rho retained.
So the 70-file frozen corpus is genuinely general-rho **only at grades
10–15**; the grade-16–19 `*_q.poly` files (V37 `LATER` map: 16→V28, 17→V30,
18→V33, 19→V35) are rho=0 images.  The erratum's statement that loading them
"without an additional rho kill" cannot recover discarded terms is exact:
the terms were never serialized.

**Independent literal re-emission.**  I re-executed the corrected compiler's
`reconstruct_rows` logic in a fresh script (`/tmp/erratum_rebuild_v43_rows.py`)
against the same hash-pinned module chain (V35 `843a6631...`, V37
`ba034c8c...`, and V35's own V33/V28/V20/parser pins), with
`killed = parser.J1 | {"a0"}` — rho alive — and `t=rho^2` conversion.
Results, all independently computed:

- **All 70 rho=0 images bridge byte-exactly** to the frozen rows through the
  V37 loader (`BRIDGE_COUNT=70`), confirming the erratum's bridge claim.
- **59 nonzero total rows**; 51 nonzero at rho=0; the same eight
  general-only-nonzero rows as my prior review (`Tg11_2, Tg11_3, Tg11_5,
  Tg11_7, Tg12_5, Tg12_7, Tg13_7, Tg14_6`).  The 59-row trap stands.
- **66 positive-sigma-weight variables** in the literal total rows;
  `general_only = ['ez9']` exactly; every frozen variable occurs
  (`X19^0 ⊂ X19^tot` strictly); no active variable has non-positive weight;
  `qa1` absent.  `wt(ez9)=14`, consistent with sigma homogeneity of the
  grade-19 term (`0+5+14=19`).
- **The general-only support is exactly one term**: monomial `a1*ez9` in
  `Tg19_2` with t-coefficient `{1: 3/8}`, i.e. `(3/8)*t*a1*ez9 =
  (3/8)*rho^2*a1*ez9`, and `ez9` occurs nowhere else in any of the 59 rows.
- Rows remain even in rho with **maximum t-degree 4** (`rho^8`);
  per-monomial sigma homogeneity holds — both now verified on *regenerated
  literal* content via the hard-failing `total_to_t`, not merely on frozen
  bytes as in my prior review.
- `ez9` is a genuine coefficient variable of the V35 source emitter: line 64
  of `build_source_series_19` defines the series
  `ez = ["c1","e1","ee1", ez3..ez14]`, entering through
  `n1 = shift((1/2)(p·az + ez), 3)` with `p[0] = -2*rho^2`.

**All three erratum hashes verify:**

```text
6cae87a2c5440057750e03a43d558d0f08c93decb35db12520d27454bd15e114  one-record inventory
    (general_only_total_terms.json bytes rebuilt locally; bit-exact match)
cc8957b85398036791e8193bc5864897412bdec6e30f2c363cce7bb345e31209  canonical total-t Tg19_2
    (sha256 of canonical_t_polynomial(Tg19_2), rebuilt locally; match)
c0e3e218aad73bf01373edceed7d83c4e9b0820ea0d9f0b8ab15f903018429dc  frozen rho-zero Tg19_2_q.poly
    (matched twice: direct file hash of V35 aws_q/compiled/Tg19_2_q.poly and V37 loader record)
```

The erratum's characterization of my error is also accurate: my prior
script did load the 70 hash-pinned files without a load-time rho kill, and
its census output (66 distinct variables = 65 positive + rho, no
positive variable in rho-only terms) was a correct census **of those
bytes** — but describing them as "the full frozen general-rho corpus" was
wrong at grades 16–19, and the inference to a literal-total 65-variable
alphabet was invalid.

## 2. Corrected theorem — CONFIRMED

**Total ring and census (mandate item 1).**  The corrected ambient ring is

```text
S = Q[rho, X19^tot],   |X19^tot| = 66,   X19^tot = X19^0 ∪ {ez9},
```

67 variables in all, and — re-verified on the regenerated rows — **`rho` is
still the only weight-zero variable** (`wt(ez9)=14 > 0`).  The load-bearing
hypothesis of the design's four-way equivalence is therefore intact: `S_0 =
Q[rho]` exactly, the weight-zero projection of a unit decomposition in
`K+(rho)` is univariate in rho, and the (1)⇒(3) step of my prior §3 goes
through verbatim with `X_19` read as `X19^tot`.  Even rho parity and sigma
homogeneity — the inputs to (3)⇒(4) — are re-verified on the literal rows.
The fixed-weight `Q[t]` completeness argument of my prior §5 survives with
the multiplier alphabet enlarged from 65 to 66 variables; the mechanism
(weight projection plus even-part extraction; no fresh variables needed
beyond the row alphabet) is unchanged.

**Spectator typing (mandate item 2).**  The specialized ideal is generated
by the 70 rho=0 images, whose supports lie in `X19^0` (verified: the sole
general-only term has t-degree 1, so it dies under `sp`).  Hence
`J0 = J0'·S0` with `J0' ⊂ Q[X19^0]` the frozen 65-variable ideal and
`S0 = Q[X19^0][ez9]` a free polynomial extension.  Writing
`g = Σ_j g_j·ez9^j`, membership `a1^N·g ∈ J0'·S0` holds iff each
`a1^N·g_j ∈ J0'`, because `J0'·S0 = ⊕_j J0'·ez9^j` as `Q[X19^0]`-modules
and `a1` is ez9-free.  Two consequences, both as the erratum states:

- `(J0 : a1^∞) = (J0' : a1^∞)·S0`, so `(J0:a1^∞)=(1)` in the 66-variable
  ring iff `(J0':a1^∞)=(1)` in the 65-variable ring — **V42's rho-zero
  saturation/radical conclusion extends unchanged**;
- `a1^i ∈ J0 ⇔ a1^i ∈ J0'` (contract to the ez9-degree-0 component), so the
  **V38 `N=6` floor transports unchanged** and my prior §6.1 stands.

The erratum's typing note is also correct: `ez9` is not rho-torsion in any
module sense; the accurate statement is that its unique source-row
coefficient is divisible by `rho^2`, so its support disappears under `sp`.
With the typed census substituted, the producer's ring/map theorem — the
four-way equivalence between `K+(rho)=(1)` and typed `a1^N·U(rho^2) ∈ J`,
`U(0)=1` — is **re-confirmed over the corrected ring**, and my prior
verdicts 2–5 (specialization inclusion, equivalence, toy counterexample,
DVR/colon formulation) carry over without further change.

## 3. Preflight dimensions — CONFIRMED by independent recomputation

I recomputed the entire preflight census from my regenerated rows
(`/tmp/erratum_census_v43.py`: int-encoded monomials, exact union-find over
the support-incidence hypergraph, matching the compiler's
`target_component` semantics; every complementary-monomial enumeration
cross-checked against a generating-function DP):

```text
quantity                              erratum    recomputed   match
nonzero total rows                         59            59     yes
all weight-30 products                 460485        460485     yes
all total support monomials           1370353       1370353     yes
total target component products        224938        224938     yes
total target component monomials       687758        687758     yes
total target component incidences     8567907       8567907     yes
rho=0 target component products         26200         26200     yes
rho=0 target component monomials        66076         66076     yes
rho=0 target component incidences      616679        616679     yes
maximum t-degree in a source row            4             4     yes
```

Supporting detail for successors: the complementary censuses over the
66-variable alphabet are `|B_11|=607, |B_12|=1036, |B_13|=1716,
|B_14|=2828, |B_15|=4606, |B_16|=7442, |B_17|=11881, |B_18|=18874,
|B_19|=29662`; the rho=0-nonzero product count (emitted by the compiler,
not quoted in the erratum) is 284766; total-lane incidences over all
products are 18385186.

**Provenance caveat.**  No frozen r6d preflight artifact exists in the
repository (the V43 case still carries no `FREEZE.sha256` and no output
directory), so the erratum's attribution "Registered r6d preflight
returned" is attested only by the erratum text itself.  The dimensions'
*honesty* is nevertheless established here independently: all ten numbers,
and the three hashes of §1, are reproduced from pinned inputs on this desk.
The quoted key set also matches the corrected compiler's census schema
exactly.  Recommendation: archive the r6d preflight `result.json` and
transcript in the case directory before freeze.

## 4. Singular repair — CONFIRMED

The current compiler (`compile_total_dvr_w30_v43.py`, SHA
`c7ed730905592b571ef6746ad369297916810c671e4c6f2e6f1af0995caeade0`)
contains no two-argument `syz` call.  The toy-control preamble now reads

```text
module NEG=(1)*gen(1)+(-t)*gen(2); vector NT=gen(1); module NE=NEG,NT; module NZ=syz(NE);
module POS=(1)*gen(1);            vector PT=gen(1); module PE=POS,PT; module PZ=syz(PE);
```

— exactly the augmented-module repair my prior review §6.4 prescribed and
the erratum §4 quotes.  I executed the verbatim generated preamble on
Singular 4.4.1: the negative toy (the design's specialization/saturation
failure mode) finds no unit last coordinate, the positive toy does, and the
script prints `V43_DVR_TOY_CONTROLS=1`.  The main solve block retains the
already-correct `module E=M,T; module Z=syz(E);` pattern with the unit
normalization, chosen-column replay, and outcome banners unchanged.  The
erratum's containment claim is re-affirmed: the old defect could only stop
a run before a verdict (fail-closed), never fabricate one.

Custody note: the V43 case directory is untracked in git, so the defective
compiler version `90b01406...` is no longer recoverable in-repo; its
content is attested by my prior review's record and the erratum's account,
which agree.  The updated validator
(`validate_total_dvr_w30_v43.py`, SHA `ee01b2c1...`) implements the typed
census — it pins `rho0_positive_variables=65` while requiring
`positive_variables >= 65` and a list-valued `general_only_variables` —
and preserves every fail-closed contract my prior review verified (byte-
equal V42 replay including the corrupted-`Tg19_7` residual `bdbc1c36...`,
single-occurrence banners, rejection of `FAIL_`/`Traceback`/`error
occurred`).

## 5. Sentences of my prior review withdrawn or amended

From `a836a978...`, verbatim:

1. **Withdrawn** (§1, first bullet): "Distinct variables occurring: **66 =
   65 positive-sigma-weight variables plus `rho`**." — as a claim about the
   general-rho/literal-total corpus this is false.  Corrected: the literal
   total rows contain 67 distinct variables = **66 positive + rho**.  The
   sub-claim "`rho` is the **only** weight-zero variable present" is
   re-affirmed and survives.
2. **Withdrawn** (§1, pinned census (i)): "**no positive-weight variable
   occurs only in rho-carrying terms** — the general-rho variable set
   equals the rho=0 set, so `X_19` is the same 65 variables on both
   sides." — false for the literal total: `ez9` occurs only in the
   rho^2-carrying term of `Tg19_2`.  The check was vacuously computed on
   grade-16–19 bytes that were already rho=0-specialized.
3. **Amended** (§0, fifth bullet): "The full 70-file frozen general-rho row
   corpus was independently re-loaded … **without** the rho→0 kill" — the
   70 per-file hash matches stand, but the description "general-rho corpus"
   is wrong at grades 16–19, where the frozen files are rho=0 emissions and
   no load-time choice can recover the discarded terms.
4. **Amended** (§5, completeness bullet): "Multipliers never need `rho` …
   nor variables outside the 65" — read 66 (`X19^tot`); the argument is
   otherwise unchanged.
5. **Amended** (§6.3): "…with the complete complementary-monomial census
   over the 65 variables…" — the complete census must be, and in the
   corrected compiler is, over the 66-variable `X19^tot`; my endorsement of
   the design's/compiler's 65-variable census requirement is withdrawn (it
   is exactly what made the first compiler fail closed on r6d).
   Correspondingly, my verdict-1 confirmation of the producer's "`X_19` …
   65 positive-sigma-weight coefficient variables" (design §1) and of the
   "65-variable census" in the registered run's step 2 (design §5) is
   superseded by the erratum's typed census.
6. **Basis strengthened, statement unchanged** (§1): "Every `rho` exponent
   is **even**; the maximum is `rho^8` … a fact of the bytes, not an
   assumption." — true, but my evidentiary basis was incomplete (the
   grade-16–19 frozen bytes carried no rho content to test); parity and
   homogeneity are now re-verified on the regenerated literal rows.
7. The appendix transcript lines ("total distinct variables in general-rho
   rows: 66 / positive-weight variables: 65 / positive vars occurring only
   in rho-carrying terms: []") stand as faithful output of that script on
   those files; their *interpretation* as a literal-total census is
   withdrawn per items 1–3.

Everything else in the prior review — the chart identification
`K=J:a1^∞`, the specialization inclusion and its strictness, the four-way
equivalence, the toy counterexample, the syzygy-colon identity, the
pruning-exactness analysis, the 59-row trap, the `N=6` floor, the gate
ordering, the fail-closed syntax finding, and the negative-outcome
evidentiary asymmetry — survives unchanged over the corrected ring.

## 6. Dense route and registered question — CONFIRMED, two notes

**Dense unsuitability.**  The exact target component is 687758 monomials ×
224938 products (about 1.5×10^11 dense rational entries); V37's largest
harvested dense solve was weight 20 with 1473 products.  The erratum's
disqualification of the rank-squared dense Flint route as primary exact
solver is plainly right, and its sparsity figure is real (8567907 nonzeros,
about 2.5×10^-4 fill).

**Registered question unchanged.**  `PREREGISTRATION.md` is byte-identical
to the version my prior review consumed (`97fa7074...`), and its "Frozen
question" — existence of `U(rho^2)`, `U(0)=1`, with `a1^6·U(rho^2) ∈ J`
for the ideal `J` of the *literal* total rows — never referenced the
variable census, so the corrected compiler answers the same registered
question.  The complete fixed-weight module remains the definition; the
corrected compiler still builds the full product set and exact component
with no truncation, and its new exact rho=0 lane (leaf-peel dual) either
produces a functional that is replayed against **every** product
(`v37.replay_certificate` full-product dual check) or fails closed
(cyclic core, or replay failure).  Two notes for the freeze:

- Prereg "Required construction" step 1 still says "Require 65
  positive-weight variables" — a stale census sentence (satisfiable only as
  a statement about the rho=0 alphabet).  An additive prereg note citing
  the erratum should accompany the freeze; the frozen question itself needs
  no change.  Likewise the validator could pin `positive_variables == 66`
  and `general_only_variables == ["ez9"]` now that the typed census is
  verified.
- As compiled, the exact-Q lane can emit only rho=0 *nonmembership* (or
  fail closed): a true rho=0 membership would make the leaf-peel functional
  fail its replay, yielding `NO VERDICT` rather than a positive gate.  This
  is fail-closed, not unsound, and is consistent with the erratum's plan to
  route the positive direction through the small `a1=1` cascade unit/lift
  computation (`compile_cascade_dehom_v43.py`, unlaunched, not reviewed in
  depth here; it does not alter the registered question).

## Firewall

This report adjudicates a census/typing erratum only.  It is **not** the
V43 certificate result: `K+(rho)=(1)` remains open, no DVR solve has run,
and nothing here bears on source/landing coverage, the terminal receiver,
Gate T, order two, maximum twelve, or JC2.  A future positive V43 result
would still close only the frozen grade-through-19 ordered `T-a1` chart.
No canonical ledger was edited; no campaign artifact was touched other
than creating this report file.

## Appendix: evidence and hashes

Consumed artifacts (re-hashed locally this session):

```text
e3d263d5c0006bc4f05c5b7ff17bfcbd68bab52f7c1d3ccb5d323facd94448f7  design (producer)
a836a978a6b9f05370322fb39c2cf1c45fa6907c337f10ef3ee9456d2e2f0f6d  prior Fable5 review
d322d4177d4592d02100a8eaaa7841c463c44d7cd67b44cbdd6529f4bc721808  erratum
843a66318dc36ecacee05f1df3616d36e375d8f93f714cf667b1fb67992543dc  V35 evaluate_grade19_orbit_v35.py
ba034c8cebaa27c5630872b9cf06d152e4577170486ac34ad7f695ead871845b  V37 solve_graded_ladder_v37.py
c7ed730905592b571ef6746ad369297916810c671e4c6f2e6f1af0995caeade0  V43 compile_total_dvr_w30_v43.py (repaired)
ee01b2c1529091d05b727f5f479b3b47ec6b6b735b83dee53f1eb91907906619  V43 validate_total_dvr_w30_v43.py (typed census)
97fa7074ef0c116b87feb5d2edeac3b6788db603227361f78715b085468345a0  V43 PREREGISTRATION.md (unchanged)
59ae6db7742c59cd1a2181b42776801803f2ae495cf483dca279b1c254ed471b  V43 MODULE_SYNTAX_PROBE.sing (unchanged)
c0e3e218aad73bf01373edceed7d83c4e9b0820ea0d9f0b8ab15f903018429dc  V35 aws_q/compiled/Tg19_2_q.poly (frozen)
```

Review scripts staged under `/tmp` (not campaign artifacts):

```text
f808477acf6a06774550198d06f33aa8f0fcdae27b1571ee6af6d09fb11ff9d2  /tmp/erratum_rebuild_v43_rows.py
e72221e0d48c17ffdddd663c7ad6f5b73caa8a3a288984a1c2ea52f4f8933921  /tmp/erratum_census_v43.py
70669097eb7d244768a98d054971c9516befc2d5861444199364e0223418d908  /tmp/erratum_v43_controls_verbatim.sing
```

Key transcript excerpts:

```text
# /tmp/erratum_rebuild_v43_rows.py (local, ~242 s)
BRIDGE_COUNT=70   RHO0_NONZERO_ROWS=51   TOTAL_NONZERO_ROWS=59
DEAD_AT_RHO0=['Tg11_2','Tg11_3','Tg11_5','Tg11_7','Tg12_5','Tg12_7','Tg13_7','Tg14_6']
ACTIVE_POSITIVE_VARIABLES=66   GENERAL_ONLY_VARIABLES=['ez9']   EZ9_SIGMA_WEIGHT=14
RECORDS=[{"row":"Tg19_2","grade":19,"monomial":[["a1",1],["ez9",1]],"t_coefficients":[[1,3,8]]}]
INVENTORY_SHA_MATCH=True   TG19_2_TOTAL_T_SHA_MATCH=True   FROZEN_TG19_2_SHA_MATCH=True
TG19_2_EZ9_UNIQUE_TERM_3_8_T_A1_EZ9=True   MAX_T_DEGREE=4

# /tmp/erratum_census_v43.py (local, ~16 s)
ALL_PREFLIGHT_DIMENSIONS_MATCH=True   (all ten quantities, table in §3)

# Singular 4.4.1, verbatim repaired control preamble
V43_DVR_TOY_CONTROLS=1
ERRATUM_REVIEW_PREAMBLE_OK
```

Execution-gap disclosure: the r6d preflight run itself was not replayed
(no AWS launch permitted); its quoted dimensions are instead established
by the independent local recomputation above.  The cascade-dehom and
homogenize-lift auxiliary compilers were inspected only far enough to
confirm they do not alter the registered V43 question.
