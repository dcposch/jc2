# Hostile review (Opus 5): V43 weight-30 exact-Q rho-zero dual at exponent six

Date: 2026-08-27
Reviewer: Claude Opus 5 (adversarial), local desk session with working shell.
Mandate: eight attacks, line-item `PASS` / `REPAIRABLE` / `FAIL`.
Constraints honoured: no AWS launch, no heavy local computation, no web
sweep, no canonical-ledger edit, `jc2-lean` never entered, read, built,
status-inspected, or modified. The only repository file written by this
review is this report.

## Execution disclosure

This session had a working local shell. Every hash below was computed live
with `shasum -a 256`. Scratch scripts were staged under `/tmp/v43rev/`
(not campaign artifacts). The heaviest computation performed was a
616,678-nonzero exact integer replay of the frozen component system, which
completed in **1.35 s** of wall time — desk-scale by any measure. No row
reconstruction from the literal emitter chain was attempted locally; that
boundary is disclosed precisely in Item 4 and in the residual-risk section.

## Verdict table

| # | Attack | Verdict |
|---|--------|---------|
| 1 | Rings, alphabet, row/variable censuses, `wt(a1^6)=30` | **PASS** |
| 2 | Completeness of the unrestricted weight-30 Macaulay span | **PASS** |
| 3 | Literal rows/products; 284,766 and component censuses; component used only to solve | **PASS** |
| 4 | Solution/certificate parsed and replayed without trusting the validator | **PASS** |
| 5 | Validator byte-level audit; full-product iteration; `Tg15_3` mutation control | **PASS** on full-product iteration; **REPAIRABLE** on the mutation control |
| 6 | Source custody, termination, exact-Q arithmetic, serializer-error sweep | **PASS** on soundness; **REPAIRABLE** on three custody/disclosure gaps |
| 7 | Logical conclusion from `rho -> 0`; scope over exponents | **PASS**, and strengthened (see 7.3) |
| 8 | Smallest failing identity; firewall preservation | **PASS** |

No `FAIL`. The headline claim `a1^6 notin J0` survives adversarial review.

---

## 0. Hash recomputation

All five pins named in the review prompt recomputed live and matched:

```text
7345d4a8dda7afd9f45dd6b938a5ec0e15ff642e4809da5434ef35eb505f446d  xmodel/max12-812-order2-p0-total-rees-j2-a1-w30-n6-rho0-dual-nonmembership-v43-sol-20260827.md
3ddea4ae8b172fcc43136494f1080756f5d04f183ac61a7a8dcd13b1d4e2f737  cases/.../aws_r6d_rho0_dual_compiler_20260827T085739Z/HARVEST.sha256
98b41d273b8a4ab20749e702ad14490f52ac772908a6d7b9df29a6302cbee0ab  cases/.../aws_r6d_rho0_dual_exact_resume_20260827T091000Z/HARVEST.sha256
acb72647ac1e0a9e6adfdd802a3769f6beb211033b1b93aa4fb67bbe63ea529f  cases/.../aws_r6d_rho0_dual_exact_resume_20260827T091000Z/EVIDENCE.sha256
0de6a2b279aeeab8c5a635c1d7658958f3f49f0f94f8473355d281cae9438b00  cases/.../compile_total_dvr_w30_v43.py
ae8ecf1887a62afd873fc795d0eeec50ff0aac6e4954813931d09a34c8bfc31a  xmodel/max12-812-order2-p0-total-rees-j2-a1-v43-compiler-postreview-delta-hostile-review-fable5-20260827.md
```

`shasum -a 256 -c` over both `HARVEST.sha256` manifests: **13/13 OK** in the
compiler harvest, **21/21 OK** in the exact-resume harvest. `EVIDENCE.sha256`
is a subset of `HARVEST.sha256` and agrees entrywise.

Additional pins traced out of the artifacts themselves and recomputed live —
all matched:

```text
ba034c8cebaa27c5630872b9cf06d152e4577170486ac34ad7f695ead871845b  .../solve_graded_ladder_v37.py                     (V37, compiler line 28)
843a66318dc36ecacee05f1df3616d36e375d8f93f714cf667b1fb67992543dc  .../evaluate_grade19_orbit_v35.py                  (V35, compiler line 26)
14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501  .../census_j2_typed_v23.py                         (parser, v37 line 18)
f4ec72933793bf08aabc600df7cdcd47b8de2c54f45c0d30341e13ac0b676459  .../replay_a1_cascade_closure_v42.py               (compiler line 30)
5d4c42fff1ad563586e8ae8736c3938efb1ae48467dfab96ae7fd9b861e7037f  xmodel/...radical-cascade-closure-v42-sol...md     (compiler line 32)
e3d263d5c0006bc4f05c5b7ff17bfcbd68bab52f7c1d3ccb5d323facd94448f7  xmodel/...rho0-to-total-dvr-design-sol...md        (compiler line 34)
a836a978a6b9f05370322fb39c2cf1c45fa6907c337f10ef3ee9456d2e2f0f6d  xmodel/...design-hostile-review-fable5...md        (compiler line 36)
d322d4177d4592d02100a8eaaa7841c463c44d7cd67b44cbdd6529f4bc721808  xmodel/...design-erratum-v43-sol...md              (compiler line 38)
97fa7074ef0c116b87feb5d2edeac3b6788db603227361f78715b085468345a0  .../PREREGISTRATION.md                             (manifest line 427)
8fdc63505428265ee583cc1eb5d03406f5dec82b9d8a2b868ab0953ca3b60ccb  .../validate_rho0_dual_linbox_v43.py               (manifest line 436)
c07d0efe851f729368d1e092f67adcc731aaf02df4a8cbfe7ca23d3ed87aa8b1  .../compile_rho0_dual_linbox_v43.py                (manifest line 429)
b70858f5a69fdedf3dfdf383b365f5c42ec8f5f45abded4f953a4bc17d5312ec  .../rho0_dual_linbox_v43.cpp                       (manifest line 433)
```

The launched-source custody chain therefore closes: the three files that
actually ran (`compile_rho0_dual_linbox_v43.py`, `rho0_dual_linbox_v43.cpp`,
`validate_rho0_dual_linbox_v43.py`) plus the imported
`compile_total_dvr_w30_v43.py` are byte-identical to the entries in
`AWS_SOURCE_MANIFEST.sha256` (`8654abe5...`, itself pinned by
`launch_registration.txt:source_manifest_sha256`).

**Custody note, non-defect:** `RESULT.json` and `validated/result.json` share
SHA `d063cdef...`; they are one file copied, i.e. **one** attestation, not
two. I treat them as one throughout.

---

## 1. Rings, alphabet, censuses — PASS

### 1.1 Sigma weights and `wt(a1^6)`

`census_j2_typed_v23.py:128-145` defines `sigma_weight`. Directly:
`sigma_weight("a1") = 5` (line 131), hence `wt(a1^6) = 30`. **Confirmed.**
`sigma_weight("rho") = 0` (line 130), so `rho` is weight-zero, as claimed.
`ez9` falls to the `("ez", 5)` prefix rule (line 140) giving
`wt(ez9) = 5 + 9 = 14`.

### 1.2 The 65/66 split, reconstructed from frozen evidence

I did not take the alphabet from the report. I read the 66,075 unknown
monomials out of the frozen coordinate map
`compiled/rho0_dual_unknown_monomials.json` (`afa01925...`) and took the
variables occurring in them. Result: **exactly 65 distinct variables**, with
this weight profile:

```text
w= 1 (1): ell1
w= 2 (1): ell2
w= 3 (3): cs1 ell3 rs1
w= 4 (4): cs2 ell4 k rs2
w= 5 (5): a1 cs3 ell5 k1 rs3
w= 6 (8): aa0 aa1 cs4 e0 e1 ell6 k2c rs4
w= 7 (8): aaa0 aaa1 cs5 ee0 ee1 ell7 k10_3 rs5
w= 8 (8): ac3 az3 cs6 ec3 ell8 ez3 k10_4 rs6
w= 9 (7): ac4 az4 cs7 ec4 ez4 k10_5 rs7
w=10 (5): ac5 az5 ec5 ez5 k10_6
w=11 (4): ac6 az6 ec6 ez6
w=12 (5): ac7 az7 ec7 ez7 k6
w=13 (5): ac8 az8 ec8 ez8 k6_1
w=14 (1): ec9
```

Every one of the 65 has **strictly positive** sigma weight, and `ez9` is
absent while `ez3..ez8` and `ec9` are present — precisely the
`X19^tot = X19^0 union {ez9}`, `|X19^0| = 65` structure. This also confirms
that `parser.specialize` kills by **exact name** (`census_j2_typed_v23.py:151`,
`any(name in killed for name, _ in monomial)`), so `rs=cs=c0=c1=a0=0` kills
the bare generators only and the indexed `rs1..rs7`, `cs1..cs7` correctly
survive. Had it killed by prefix, this alphabet would be impossible.

### 1.3 `ez9` is a spectator after specialization — PASS, structurally enforced

Two independent confirmations:

1. **Empirical.** `ez9` occurs **0 times** across all 66,075 component
   monomials. Since `a1^6` is `ez9`-free and no `rho=0` row carries `ez9`,
   every `ez9`-bearing product has `ez9` in *every* monomial and is therefore
   in a different incidence component. Exactly as observed.
2. **Enforced, not assumed.** The spectator property is a *consequence* of
   checks that ran, not a producer assertion. `compile_total_dvr_w30_v43.py:424-426`
   requires `parser.specialize(face, {"rho"}, {}) == frozen_by_name.get(name, {})`
   for all 70 rows; `solve_graded_ladder_v37.py:150-152` requires the frozen
   rows to use exactly 65 variables. Hence no `t^0` term can carry `ez9`.
   A row with an `ez9` term at `rho^0` would have failed the bridge.

The report's finer claim that the sole occurrence is `(3/8)*rho^2*a1*ez9` in
`Tg19_2` is **not attested by either harvested lane**: the
`general_only_total_terms.json` emitter lives in
`compile_total_dvr_w30_v43.py:466-483`, inside `main()`, which neither
harvested lane executes (see 6.2). It is weight-consistent
(`wt(a1*ez9) = 5+14 = 19 = ` grade of `Tg19_2`) and it is pinned by the
census addendum, but in *this* evidence chain it is inherited, not verified.
This does not affect the verdict, because the spectator property itself is
enforced as above.

### 1.4 Row census: 70 named / 59 nonzero / 51 nonzero at `rho=0` — PASS

`compiler_result.json` carries `frozen_row_sha256` and `total_t_row_sha256`,
each with **70** entries over identical name sets, 7 rows in each of grades
10–19. Both maps have exactly **60 distinct** hash values. The collision
structure is decisive:

```text
total_t_row_sha256: 4f53cda18c2baa0c...  x11:
    Tg10_1..Tg10_7  Tg11_4  Tg11_6  Tg12_6  Tg13_6
```

and `printf '[]' | shasum -a 256` = `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`,
which is exactly `canonical_t_polynomial({})` (`compile_total_dvr_w30_v43.py:93-102`
on an empty polynomial). So **precisely 11 of the 70 total rows are
identically zero**, giving `70 - 11 = 59` nonzero total rows. This
independently reproduces the `nonzero_general != 59` gate at
`compile_rho0_dual_linbox_v43.py:110` without trusting it.

Separately, `solve_graded_ladder_v37.py:45` pins
`ROW_COUNTS = {10:0, 11:1, 12:4, 13:5, 14:6, 15:7, 16:7, 17:7, 18:7, 19:7}`,
summing to **51** nonzero rows at `rho=0` (gated at v37 line 139-140,
`len(rows) != 51`). The arithmetic closes: 70 named = 51 nonzero at `rho=0`
+ 8 rows that are nonzero but `rho`-divisible + 11 identically zero, and
`51 + 8 = 59`. Note the *frozen file* hash map collides on the same 11 names,
i.e. 11 coefficient files are literally zero while the other 8 vanishing rows
have nonzero, `rho`-divisible file content — self-consistent.

### 1.5 The 66th variable is really in the multiplier alphabet

`reconstruct_rows` returns `active` (line 433-434, 440) as the variable list,
and `compile_rho0_dual_linbox_v43.py:111` gates `len(variables) != 66`. That
this is the *operative* alphabet, not a decorative assertion, is proved by
the census recomputation in Item 3.2, which discriminates 65 vs 66 vs 67.

**Verdict 1: PASS.**

---

## 2. Completeness of the unrestricted weight-30 span — PASS

### 2.1 The enumeration has no cutoff

`solve_graded_ladder_v37.py:156-172` (`monomials_of_weight`) is a plain
complete recursion: for each eligible variable it ranges the exponent over
`0 .. remaining // variable_weight` and recurses on the residual weight,
returning every monomial of weight **exactly** `weight`. There is no
total-degree bound, no support-size bound, and no coefficient filter. The
only filter, `sigma_weight(name) <= weight` (line 157), is vacuous: a
variable heavier than the target weight cannot occur.

`compile_total_dvr_w30_v43.py:130-147` (`build_products`) forms, for every
one of the 59 nonzero total rows, the product with **every** monomial of
weight `30 - grade`. `complement < 0` is skipped; with grades 10–19 no row is
skipped. Products are appended to a **list**, so coincident products are
retained as separate equations, never collapsed (see 6.5).

### 2.2 The passage from homogeneous component to polynomial-ideal membership

The report's one-sentence justification is correct but loose. The clean
argument, which I verified is fully supported by the code:

Let `V` be the 66 active variables, `R0 = Q[V]`, `g_1..g_70` the specialized
rows, `J0 = (g_1,...,g_70) R0`.

* **`J0` is genuinely an ideal, and `sp(J) = J0`.** `sp : S -> R0`,
  `rho |-> 0`, is a *surjective* ring homomorphism, so the set image of the
  ideal `J = (g_i)S` is exactly the ideal generated by the images:
  `sp(sum a_i g_i) = sum sp(a_i) sp(g_i)` and every element of `R0` is some
  `sp(a)`. No flatness or base-change hypothesis is needed for this.
* **The grading is positive on `R0`.** `compile_total_dvr_w30_v43.py:438`
  fails the run if `any(parser.sigma_weight(name) <= 0 for name in active)`.
  Verified independently in 1.2: min weight is 1 (`ell1`). `rho` is *not* in
  `active` by construction — `total_to_t` (lines 109-122) pops `"rho"` out of
  the monomial into the `t`-degree, so `t`-form monomials are `rho`-free.
  This is exactly the "no omitted zero-weight variable" requirement: the two
  weight-zero symbols in the parser table, `rho` and `qa1`, are both absent
  from `active` (`qa1` would have tripped line 438).
* **Each `g_i` is sigma-homogeneous of weight = its grade.**
  `total_to_t` line 117-118 raises on any monomial of the wrong weight, and
  v37 line 146-147 does the same for the frozen rows. Both ran clean.
* **Therefore** `J0` is a graded ideal and
  `(J0)_30 = span_Q { m * g_i : wt(m) = 30 - grade_i }` = `C30`, so
  `a1^6 in J0  <=>  a1^6 in C30`. Homogeneous-component membership decides
  the unrestricted polynomial question.

**A strengthening the report does not state, worth recording.** Even if the
"true" ambient ring were larger than `R0` — carrying extra variables `v`
(possibly of weight zero) that occur in no row — the conclusion is unchanged:
given `a1^6 = sum f_i g_i` over the larger ring, apply the ring map `v |-> 0`;
neither `a1^6` nor any `g_i` involves `v`, so `a1^6 = sum (f_i|_{v=0}) g_i`.
Iterating reduces to `R0`, where the positive grading applies. So the
restriction to the 66 active variables costs nothing, and the completeness
claim is robust to any dispute about the ambient alphabet.

### 2.3 "No row beyond grade 19"

Within the frozen corpus this is definitional: `reconstruct_rows` iterates
`for grade in range(10, 20)` (line 420) and `J` is *defined* as the ideal on
those 70 rows (`PREREGISTRATION.md`, "Frozen question"). Rows of grade > 30
could not contribute to weight 30 in any case (`complement < 0`). The
substantive limitation — that the *true* geometric ideal may have generators
beyond grade 19, and nonmembership does **not** ascend to a larger ideal — is
correctly quarantined by the report's §5 firewall and by Item 8 below.

**Verdict 2: PASS.**

---

## 3. Rows, products, censuses — PASS

### 3.1 Component censuses verified directly against frozen bytes

Parsing `rho0_dual_full_component.sms` (`8e043129...`) and
`rho0_dual_full_component.rhs` (`be700f99...`) locally:

```text
sms header                       : "26200 66075 M"      -> 26,200 x 66,075   MATCH
nonzeros counted to sentinel     : 616,678                                    MATCH
coordinate map records           : 66,075                                     MATCH
component monomials incl. target : 66,075 + 1 = 66,076                        MATCH
rhs entries                      : 26,200, of which exactly 1 nonzero         MATCH
column index range               : 1 .. 66,075  (every column occupied)
```

All four match `compiler_result.json` (`25f58091...`) fields
`component_equations`, `matrix_nnz`, `unknowns_excluding_target`,
`component_monomials_including_target`, `target_incident_equations`.

**`target_incident_equations = 1` is forced by weight combinatorics**, which
is a genuinely independent check. A product `g * m` can carry the monomial
`a1^6` only if `g` contains a pure power `a1^j` with `5j = grade`, so
`grade in {10, 15}` within the corpus; grade 10 has `ROW_COUNTS[10] = 0`
nonzero rows; so `grade = 15`, `j = 3`, multiplier `a1^3`. `RESULT.json`
records `row = "Tg15_3"`, `grade = 15` — exactly the unique combinatorial
possibility, and consistent with exactly one grade-15 row carrying `a1^3`.

### 3.2 The 284,766 census, recomputed from scratch — the strongest check

I recomputed the product count with **no reference to any AWS output**, using
only (a) the 66-variable weighted alphabet of 1.2, (b) the hash-pinned
`ROW_COUNTS` from v37 line 45, and (c) the complementary-weight rule
`multiplier weight = 30 - grade`. Writing `N(w)` for the number of monomials
of sigma-weight exactly `w` in the 66 variables (ordinary generating function
`prod 1/(1 - x^{w(v)})`):

```text
N(11)=607   N(12)=1036   N(13)=1716   N(14)=2828   N(15)=4606
N(16)=7442  N(17)=11881  N(18)=18874  N(19)=29662

  1*N(19) + 4*N(18) + 5*N(17) + 6*N(16) + 7*[N(15)+N(14)+N(13)+N(12)+N(11)]
=  29,662  +  75,496 +  59,405 +  44,652 + 7*10,793
=  29,662  +  75,496 +  59,405 +  44,652 +  75,551
=  284,766
```

matching `all_rho0_products = 284766` **exactly**. Note the sum runs over the
51 rows with nonzero `rho=0` part; the 8 `rho`-divisible rows contribute
products whose `t^0` part is empty and which `specialize_t0`
(`compile_total_dvr_w30_v43.py:171-173`) correctly drops.

This count is **sharply discriminating**, which is what makes it evidence
rather than coincidence:

```text
alphabet = 65 (rho=0 support only)  -> 284,657
alphabet = 66 (adding ez9)          -> 284,766   <-- claimed
alphabet = 67 (adding a probe var)  -> 284,819
```

So the frozen census simultaneously certifies that (i) the multiplier
alphabet is the 66-variable one — `ez9` really is enumerated, the stale
65-variable census would have produced a different number; (ii) the
enumeration is of *exact* complementary weight; (iii) **no support or
total-degree cutoff was applied** — any cutoff would strictly reduce the
count below the free value.

### 3.3 Component restriction is used only to solve — PASS

* `compile_rho0_dual_linbox_v43.py:78-104` writes the `.sms`/`.rhs` from
  `component` alone. That is the *solve* artifact.
* `validate_rho0_dual_linbox_v43.py:132` calls
  `v37.replay_certificate(certificate, special_products, component_indices, TARGET)`
  passing the **full** `special_products` list.
* `solve_graded_ladder_v37.py:310-331`: in the `nonmember` branch (lines
  323-329) the iteration is `for product in products` — the full list.
  `component_products` (line 311) is built but used **only** in the `member`
  branch. The component indices are inert in the branch that fired.

So the final replay is not weakened by the component restriction.

**Moreover the restriction is mathematically lossless**, which I verified from
the BFS itself (`solve_graded_ladder_v37.py:194-210`): a product index enters
`product_indices` iff the product touches a monomial already in `monomials`,
and every monomial of every entered product is added to `monomials`. Hence
for `p` outside the component, *no* monomial of `p` lies in
`component_monomials`. Since `supp(Lambda)` is by construction a subset of
`{target} u unknown_monomials = component_monomials`, `Lambda(p) = 0`
automatically for all 284,766 - 26,200 = 258,566 non-component products. The
full replay is therefore a genuine *check of the BFS*, and its success is not
in tension with solving only on the component.

**Verdict 3: PASS.**

---

## 4. Solution and certificate parsed independently — PASS

I parsed `rho0_dual_exact.solution` (`d0c04857...`) and the coordinate map
directly, never invoking or trusting the validator.

```text
framing        : line0 "V43_RHO0_DUAL_LINBOX_EXACT", line-1 "PASS_A1_..._LINBOX",
                 66,079 lines = 66,075 + 4                       OK
denominator    : 34670334774018800828908752076800000             MATCH (report / RESULT.json)
count field    : 66075 = len(numerators)                          OK
target         : (("a1",6),) absent from the 66,075 coordinates   OK
Lambda(a1^6)   : 1  (exactly, imposed at validator line 100)
non-target supp: 3,394                                            MATCH
total support  : 3,395                                            MATCH
```

Two checks beyond what the producer claims:

* **The printed denominator is the true common denominator.** The lcm of the
  3,395 reduced denominators of `Lambda` equals `34670334774018800828908752076800000`
  exactly (ratio 1). A padded or spurious denominator would not be minimal.
* **The frozen certificate is a faithful decode, not a re-derivation.**
  `validated/rho0_dual_exact_certificate.json` (`6674abaa...`) decodes to a
  3,395-key map that is **equal as a dictionary** to the `Lambda` I rebuilt
  from `solution x coordinates`. So no drift entered the encode/decode round
  trip.

### 4.1 Independent exact sparse replay

I replayed `Lambda` against the frozen compiled system over `Z`:

```text
for each i in 1..26,200 :   sum_j A[i][j] * numerator[j]  ==  denominator * rhs[i]
result: ALL 26,200 EQUATIONS HOLD EXACTLY          (1.35 s, Python big ints)
```

Since `compile_rho0_dual_linbox_v43.py:96-103` writes
`rhs = -coeff(p, target) * scale` and `A[i][j] = coeff(p, m_j) * scale` for
`m_j != target`, this identity is *equivalent* to
`sum_m coeff(p,m) * Lambda(m) = 0` given `Lambda(target) = 1` — the sign
convention is right, and a flipped target column would have shown residual
`2*coeff(p,target) != 0`.

Combined with the disjointness argument of 3.3, this is a **complete
desk-scale verification of `Lambda(p) = 0` for all 284,766 products**,
conditional only on the frozen `.sms` being a faithful serialization of the
reconstructed products (see residual risk, 6.6).

Two self-imposed non-vacuity controls on my own replay:

```text
columns shifted by one : 5,160 / 26,200 equations fail
numerator[0] += 1      :     13 / 26,200 equations fail
```

so the replay is sensitive to both the coordinate map and the solution values
and is not passing trivially.

**Verdict 4: PASS.**

---

## 5. Validator audit — PASS on full-product iteration; REPAIRABLE on the mutation control

### 5.1 Reconstruction and decoding (lines 42-51, 88-104) — sound

`load_source()` hard-pins `TOTAL_COMPILER_SHA256 = 0de6a2b2...` (line 18) and
compares the live digest **before** `exec_module` (lines 43-45), so the
validator cannot import a different emitter. The compiler-result status gate
(line 89) demands `PASS-A1-TOTAL-DVR-W30-V43-RHO0-DUAL-LINBOX-COMPILER`,
which `compile_total_dvr_w30_v43.py` never emits (it emits
`...-V43-COMPILER`, line 530) — correctly forcing the artifact to come from
`compile_rho0_dual_linbox_v43.py:118`. Lines 91-94 re-digest the matrix, rhs
and coordinate files against the compiler's recorded hashes. Line 97 rejects
the run if `TARGET` appears among the coordinates or the count is wrong.
`output.mkdir(..., exist_ok=False)` (line 85) forbids overwriting a prior
result. `fail()` raises an uncaught `RuntimeError` (lines 26-27), so every
gate is fail-closed with a nonzero exit; `lanes.log` records `rc=0`.

### 5.2 Does it truly evaluate all 284,766 freshly reconstructed products? — YES

Chain of custody for that number, all verified by reading bytes:

1. Line 106-109: `special_products` is built **fresh** from
   `source.reconstruct_rows()` + `source.build_products()` +
   `source.specialize_t0()`. It reads no cached product file; the `.sms` is
   hash-checked but never parsed for values.
2. Line 119: `len(special_products) != compiler["all_rho0_products"]` -> fail.
   So the fresh list has 284,766 entries or the run dies.
3. Line 132 -> `solve_graded_ladder_v37.py:328`:
   `any(evaluate_functional(product["polynomial"], functional) for product in products)`.
   `products` is the full `special_products`. `any` short-circuits only on a
   **failure**; on success all 284,766 are evaluated.
4. Line 160 reports `full_product_replay_count = len(special_products)`, a
   computed value, not a literal. (The `"scope"` string at line 152 *is* a
   hard-coded literal and is decorative — I give it no evidential weight,
   though it happens to agree.)

**Resource corroboration.** The validator burned **357.16 s user CPU** at
14.0 GB peak RSS. My replay of the 26,200-equation component alone took
1.35 s. The total term count of the full product set is
`sum_g TERM_COUNTS[g] * N(30-g) ~ 8.12e6` monomial terms (using v37 line 46),
so a genuine reconstruct-and-multiply pass is exactly the right order of
magnitude, and a cached or component-only shortcut would have been ~100x
faster. The timing is consistent with the claim and inconsistent with a
subselected replay.

### 5.3 Vacuity of the functional is excluded

A real hazard exists in principle: `functional[TARGET]` is set literally at
line 100, *not* read from the coordinate file, so a wholly malformed
coordinate encoding would leave `Lambda = 1 * delta_{a1^6}` and still pass the
`dual target` check at v37 line 326. It is excluded three ways:

* the 66,075 coordinate records are **all canonical** — name-sorted, distinct
  names, strictly positive exponents (I checked all of them) — matching the
  `merge_monomials` normal form (`solve_graded_ladder_v37.py:86-90`), so
  `functional.get(monomial)` lookups cannot silently miss;
* **all 66,075 have sigma-weight exactly 30**, and all 3,394 support columns
  occur in the matrix (0 unconstrained), so the support is live;
* structurally: one product *does* carry a nonzero `a1^6` coefficient
  (validator line 134-137 would raise `StopIteration` otherwise, and
  `target_incident_equations = 1`), and its residual is required to be
  **zero** (line 143). A target-only `Lambda` would leave that residual
  nonzero. So genuine non-target support is exercised.

### 5.4 The `Tg15_3` mutation control — REPAIRABLE

Validator lines 134-144:

```python
target_product_index = next(i for i,p in enumerate(special_products) if p["polynomial"].get(TARGET))
original_residual  = v37.evaluate_functional(special_products[i]["polynomial"], functional)
corrupted          = dict(...); corrupted[TARGET] = corrupted.get(TARGET, 0) + 1
corrupted_residual = v37.evaluate_functional(corrupted, functional)
if original_residual != 0 or corrupted_residual != 1: fail(...)
```

**It is not vacuous, but it is very nearly tautological.** Perturbing the
`a1^6` coefficient by `+1` shifts the residual by exactly `1 * Lambda(a1^6)`,
and `Lambda(a1^6) = 1` is hard-set at line 100 while `original_residual = 0`
is separately required in the same `if`. So `corrupted_residual == 1` is an
algebraic *consequence* of the two conditions it is bundled with. Its
detection power is confined to "`evaluate_functional` reads the target
coefficient". It cannot detect a wrong coordinate map, wrong row data, wrong
products, a transposed matrix, or omitted products.

Two further accuracy notes on the report's §2 wording:

* the product is not *chosen* as a `Tg15_3` product — the code takes the
  first product with a nonzero `a1^6` coefficient, and (per 3.1) that is
  forced to be the unique `Tg15_3 * a1^3` product. Calling it "deliberate"
  overstates the design;
* the preregistration's actual control ("its fixed mutation of `Tg19_7` must
  leave a nonzero residual", `PREREGISTRATION.md`, Controls) is a **row-data**
  mutation, which is far stronger. This validator does not implement one.

I quantified how much is lost. Perturbing the coefficient of monomial `m` in
any equation shifts that residual by `Lambda(m)`, so the mutation is detected
iff `m in supp(Lambda)`:

```text
single non-target coefficient mutations detected: 26,464 / 616,678 = 4.29 %
  => a mutation control on a randomly chosen non-target coefficient
     would be VACUOUS 95.71 % of the time
```

This is why the target-coefficient choice is the *only* single-coefficient
mutation guaranteed to register — and why it is also the only one that
registers for a trivial reason. The correct repair is a **row-level**
mutation as in V42: changing a coefficient of monomial `mu` in row `g`
perturbs every one of the `N(30 - grade(g))` products `g*m` by
`Lambda(mu*m)`, so detection is essentially certain, and it genuinely
exercises `reconstruct_rows`.

**Verdict 5: PASS on full-product iteration (the load-bearing claim);
REPAIRABLE on the mutation control, which should be replaced by a row-data
mutation. The main result does not depend on the control.**

---

## 6. Custody, termination, exact arithmetic, serializer sweep

### 6.1 Termination and resources — PASS

```text
build   09:11:28Z -> 09:11:43Z  rc=0   14.3 s CPU,  0.86 GB peak
solver  09:11:43Z -> 09:20:54Z  rc=0  537.9 s CPU, 34.94 GB peak
valid.  09:20:54Z -> 09:26:56Z  rc=0  357.2 s CPU, 14.01 GB peak
total elapsed 928 s; outcome=exact-Q-nonmembership
```

All three lanes exited 0 (`lanes.log`, all three `*.meta` `rc=` fields, and
`Exit status: 0` in each `/usr/bin/time -v` block). Wall budget 21,600 s
against 928 s used; memory cap 201,326,592 KiB (192 GiB) against a 34.9 GB
peak. Grepping the exact-resume harvest for `Killed|OOM|out of memory|
Terminated|Segmentation|Traceback|RuntimeError|FAIL_` returns **no genuine
hits** — every match is either the literal string `timeout` inside a `timeout
21585 ...` argv line, or `Command being timed:` from `/usr/bin/time`. The
preregistered caps were respected and no `N>6` or higher-weight lane was
launched before the freeze.

### 6.2 REPAIRABLE — the custody-hash block never executed in this chain

`compile_total_dvr_w30_v43.py:454-462` verifies `V42_REPLAY`, `V42_REPORT`,
`DESIGN`, `DESIGN_REVIEW`, `DESIGN_ERRATUM`, and digests `PREREG` (line 535).
**All of this sits inside `main()`**, and neither harvested lane calls it:
`compile_rho0_dual_linbox_v43.py:65-71` and
`validate_rho0_dual_linbox_v43.py:106-112` import the module via `importlib`
under a non-`__main__` name and call only `reconstruct_rows`,
`build_products`, `specialize_t0`. Fable5's Item 5 (`ae8ecf18...`)
independently establishes the same import surface.

Consequences:

* those five theorem pins were **inert** at runtime for this result. I have
  verified all five by hand (Section 0) and they match, so nothing is
  *wrong* — but the enforcement is by this review, not by the run;
* the preregistered control **"Run the pinned V42 replay first ... its fixed
  mutation of `Tg19_7` must leave a nonzero residual"** has **no evidence of
  having been discharged** in either harvest. It may have run in an
  unharvested preflight lane. As frozen, it is an open obligation.

The preregistration's *other* controls (the two univariate toy modules,
`compile_total_dvr_w30_v43.py:342-349`) are correctly not required here: they
live in `write_singular`, reachable only when the `rho=0` gate returns
`member` (line 585), and the preregistration explicitly stages the DVR
syzygy step as "only after a positive `t=0` gate".

### 6.3 REPAIRABLE — compiler harvest has no source manifest, and carries an undisclosed `rc=1`

* `aws_r6d_rho0_dual_compiler_20260827T085739Z/launch_registration.txt` names
  `source_manifest_sha256=033213c1d59bd77b6a4d7bd68faf714a4a62db16515b02a58d4f6e2c9c080a25`,
  but **no `AWS_SOURCE_MANIFEST.sha256` is harvested in that directory**. The
  source custody of the lane that produced the `.sms`/`.rhs`/coordinates rests
  on a hash pointing at a file not in the frozen evidence. (Mitigated: the
  in-consumer digest gate at `compile_rho0_dual_linbox_v43.py:36-38` pins the
  emitter regardless, and — decisively — the correctness of the conclusion
  does not depend on that lane at all; see 6.6.)
* That harvest's `run/lanes.log` records
  `..._r6d_build rc=1`, with 747 KB of `ld: undefined reference to
  Givaro::Integer::...` in `build.stderr` — the first build omitted
  `-lgivaro -lgmpxx -lgmp`. This is why the job was resumed; the resume build
  (`build.meta` argv) adds the libraries and returns `rc=0`. Benign, and the
  compiler lane itself was `rc=0`.

  **Disclosure gap:** the report §3 says "There is no failure marker in the
  text logs", scoped to "The exact run". Technically accurate, but an auditor
  grepping `rc=[1-9]` across the pinned evidence will find one, unexplained.
  The report should say so and explain it.

### 6.4 The census addendum is absent from the shipped manifest — not a violation

`PREREGISTRATION_CENSUS_ADDENDUM.md` imposes: "Every V43 source freeze created
after this note must include both `PREREGISTRATION.md` and this addendum in
its source manifest." It is **absent** from `AWS_SOURCE_MANIFEST.sha256`
(`8654abe5...`), which carries `PREREGISTRATION.md` at line 427 only.

This is **not** a breach: the local clock is PDT (UTC-7; calibrated by the
producer report's own mtime 02:29:50 PDT = 09:29:50 UTC, three minutes after
the run ended at 09:26:56Z). The addendum's mtime is 02:17:56 PDT =
**09:17:56 UTC**, i.e. *after* the 09:10:00Z freeze and 09:11:28Z launch. The
freeze predates the note, so the note's own rule does not reach it.

Substantively the shipped tree is not stale anyway: the addendum's correction
is the 66-vs-65 alphabet, and `compile_rho0_dual_linbox_v43.py:111` already
gates `len(variables) != 66`. **Forward obligation only:** the next V43 freeze
must include the addendum.

### 6.5 Serializer-error sweep — PASS

| Hazard | Finding |
|---|---|
| transposed matrix | `.sms` header `26200 66075` = equations x unknowns; `rhs` has `rowdim` entries; `A*x = b` with `x` of length `coldim`. Verified by my own row-indexed replay. |
| target-column sign | `rhs = -coeff*scale`, `A = +coeff*scale` (lines 96, 100). Verified consistent; a flip yields residual `2*coeff != 0`, caught by the from-source replay. |
| one-based indexing | SMS is 1-based; observed column range is exactly `1..66075`; my shift-by-one control breaks 5,160 equations, so the convention is pinned. |
| duplicate product collapse | **146** of 26,200 equations are byte-identical in support+coefficients — coincidences after integer clearing (which drops the target column and the overall scale). Nothing is *collapsed*: `build_products` appends to a list and each pair is its own equation. Harmless (a repeated linear constraint). The 284,766 count is over `(row, multiplier)` pairs and my generating-function recomputation matches it exactly, so there is no inflation or deflation. |
| stale coordinates | **Self-correcting.** A permuted or stale coordinate map yields a *different* functional `Lambda`, which the from-source replay would then reject. Since the replay accepted, whatever `Lambda` is, it annihilates every reconstructed product and takes value 1 on `a1^6` — which is all the theorem needs. |
| wrong RHS | Exactly one nonzero rhs entry, at 0-based equation 20,671, value 32; forced by the combinatorial uniqueness argument of 3.1. |
| integer clearing | `scale = lcm` over **all** coefficients of the polynomial including the target (lines 91-92), so `int(coefficient * scale)` is exact, never a floor; `fail("integer clearing produced zero")` (line 102) guards the degenerate case. |
| inexact arithmetic | No `float`, `round`, `numpy`, or `decimal` anywhere in the certifying path. Python side is `fractions.Fraction` throughout; C++ side is `Givaro::ZRing<Givaro::Integer>` (GMP) with an integer numerator vector plus common denominator. |
| `-DNDEBUG` disabling the solver's self-check | **Attack fails.** `rho0_dual_linbox_v43.cpp:38-44` verifies `A*numerator == denominator*rhs` with `MatrixDomain`/`VectorDomain` and `return 129` — an ordinary branch, **not** an `assert`, so `-DNDEBUG` cannot elide it. The `PASS_...` banner (line 51) is producer-authored but is written only downstream of that branch. |

### 6.6 "Replayed against the same faulty serializer?" — NO, and this is the architectural strength

The two paths are genuinely separated:

```text
(a)  reconstruct_rows -> build_products -> specialize_t0 -> component
        -> .sms/.rhs/coordinates -> LinBox -> solution        [SOLVE]
(b)  reconstruct_rows -> build_products -> specialize_t0
        -> replay of Lambda over all 284,766 products          [CERTIFY]
```

Path (b) **never reads** `.sms` or `.rhs`. `Lambda` is transported from (a) to
(b) only through the coordinate JSON. Therefore *any* error confined to (a) —
transpose, sign, index base, scale, LinBox itself — can only produce a wrong
`Lambda`, which (b) then rejects. Soundness rests on (b) alone. Conversely my
independent replay (Item 4.1) exercises (a)'s serialization, which (b) never
touches. The two together cover both.

**Residual single point of failure, stated plainly:** paths (a) and (b) share
`reconstruct_rows` / `build_products` (same pinned bytes `0de6a2b2...`). A
defect there would corrupt both. This review attacks that shared component
directly and finds it sound: `build_products`/`monomials_of_weight`
completeness is verified by code reading *and* confirmed numerically by the
independent 284,766 recomputation (3.2); `reconstruct_rows` is constrained by
the 70-row bridge check (line 425), the 65/66 alphabet gates, the positive-
weight gate, the sigma-homogeneity gates, and the frozen row-hash maps, whose
collision structure I reproduced from first principles (1.4). What this
review does **not** do is re-derive the literal row coefficients from the
V20/V28/V35 emitter chain — that is inherited from the V35/V37/V38/V39-era
reviews and from the hash-pinned frozen coefficient files.

**Verdict 6: PASS on soundness, exact-Q arithmetic, and termination.
REPAIRABLE on (i) the inert custody block and the undischarged V42 control,
(ii) the compiler harvest's missing source manifest, (iii) the undisclosed
`rc=1` build failure in the compiler harvest.**

---

## 7. The logical conclusion from `rho -> 0` — PASS, and strengthened

### 7.1 The implication needs nothing beyond a ring map

`sp : S = Q[rho, X19^tot] -> R0 = Q[X19^tot]`, `rho |-> 0`, is a surjective
`Q`-algebra homomorphism. If `a1^6 * V in J` for some `V in S`, then
`a1^6 * sp(V) = sp(a1^6 V) in sp(J) = J0`. If moreover `sp(V) = 1`, then
`a1^6 in J0`, contradicting the theorem. Applying this with:

* `V = U(rho^2)`, `U(0) = 1`: `sp(V) = U(0) = 1`. Excluded.
* `V = 1 + rho*W`, **any** `W in S`: `sp(V) = 1 + 0 * sp(W) = 1`. Excluded.

The report's claim that no even-`rho` (parity) assumption on `W` is needed is
**correct**, and I confirm the stronger reading: the argument works for *any*
`V` with `sp(V) = 1`, i.e. any `V in 1 + rho*S`.

Explicitly **not** used: saturation/localization interchange, a
flatness or base-change converse, Hensel lifting, or any parity hypothesis.
Only the trivial direction "membership descends along a ring map" and
"`sp` surjective => `sp(J)` is the ideal on the images" (proved in 2.2).

The even-`rho` structure *does* appear elsewhere — `total_to_t` line 114
raises on any odd `rho` exponent, so the frozen rows genuinely lie in
`Q[t][X]`, `t = rho^2` — but that is used only to package the `t`-module for
the (unreached) DVR stage, never in the negative implication.

### 7.2 One inherited hinge, named

The negative result is a statement about **literal** membership in the frozen
`J`. Its bearing on "an honest closure-first ordered-chart certificate
`a1^6*(1 + rho*W)`" is supplied by the ring/map theorem of the pinned design
report `e3d263d5...` (+ review `a836a978...`, erratum `d322d417...`), which
this review verifies by hash only and does not re-adjudicate. If that theorem
were to require membership in a *saturation* or *localization* of `J` rather
than in `J` itself, the specialization argument would not transfer. Named as
the single inherited dependency of the interpretation, not of the computation.

### 7.3 Scope over exponents — the report under-claims and mis-attributes

The report says: "Together with V38 it excludes powers at most six."
**The appeal to V38 is unnecessary for pure powers.** Since `J0` is an ideal,
for `1 <= i <= 6`:

```text
a1^i in J0  =>  a1^6 = a1^(6-i) * a1^i in J0,
```

so `a1^6 notin J0` *immediately* gives `a1^i notin J0` for **every**
`i <= 6`, and hence `a1^i * V notin J` for every `V in 1 + rho*S` and every
`i <= 6`. This is a one-line consequence of the single computed fact and
carries no dependence on V38's separate result.

V38 remains independently valuable for what this argument does **not** give:
the mixed monomials `a1^i k^j`. The report should attribute accordingly.

I also flag a related nuance for the record: V42's certificate is
`a1^8 in I_A1` where `I_A1` is the *branch* ideal (`rho=0` **plus** `rs1=0`),
per `5d4c42ff...` §Headline. It is **not** `a1^8 in J0`, so it does not bound
the pure-power frontier in `J0` from above. The frontier for pure powers in
`J0` is therefore: `i <= 6` excluded, `i >= 7` open.

**Verdict 7: PASS.**

---

## 8. Smallest failing identity; firewall — PASS

### 8.1 The strongest theorem that survives

> **Theorem (V43-N6).** Let `X19^tot` be the 66 strictly-positive-sigma-weight
> variables of §1.2 together with `ez9`, `R0 = Q[X19^tot]`,
> `S = Q[rho, X19^tot]`, and `sp : S -> R0` the `Q`-algebra map `rho |-> 0`.
> Let `g_1,...,g_70 in S` be the literal actual-total ordered-`a1` source rows
> of grades 10..19 after `rs = cs = c0 = c1 = a0 = 0` (59 nonzero in `S`, 11
> identically zero, 51 with nonzero image under `sp`), and let
> `J = (g_1,...,g_70) S`, `J0 = sp(J) = (sp g_1,...,sp g_70) R0`. Then
>
> ```text
> a1^6 notin J0.
> ```
>
> Consequently, for every `1 <= i <= 6` and every `V in 1 + rho*S` — in
> particular `V = U(rho^2)` with `U(0) = 1`, and `V = 1 + rho*W` for arbitrary
> `W in S` —
>
> ```text
> a1^i * V notin J.
> ```

*Witness.* The exact rational functional `Lambda` on the weight-30 component,
support 3,395, common denominator `34670334774018800828908752076800000`,
`Lambda(a1^6) = 1`, `Lambda(m * sp(g)) = 0` for all 284,766
complementary-weight products.

*Evidence tier.* Two replay paths: the AWS from-source reconstruction over all
284,766 products (`validate_rho0_dual_linbox_v43.py:132` ->
`solve_graded_ladder_v37.py:328`, 357 s CPU, `rc=0`), and this review's
independent exact integer replay of the 26,200-equation component against the
frozen `.sms`/`.rhs` plus the disjointness argument covering the remaining
258,566.

### 8.2 Smallest failing identity / missing hypothesis

There is no missing hypothesis in the negative direction — the argument is
complete as stated in 7.1. The *smallest* refuted identity is
`a1 * (1 + rho*W) in J`; the smallest one the producer actually targeted is
`a1^6 * U(rho^2) in J`. Nothing weaker survives, and nothing stronger is
implied: the first identity **not** excluded is `a1^7 * U(rho^2) in J`
(weight 35), which is exactly where the frontier now sits.

### 8.3 Firewall — preserved

Nothing here supports: any `a1` power `>= 7`; the selected-row dehomogenized
cascade lane; chart closure; Gate T; source/landing coverage; the terminal
receiver; order two; maximum twelve; or JC2. Because the result is a
**non**membership, it also does **not** ascend: adding generators beyond
grade 19, or passing to a saturation, closure, or localization of `J`, could
make `a1^6` a member, and this computation says nothing about those ideals.
The report's §5 firewall states this correctly.

I confirm no canonical ledger and no `jc2-lean` artifact was touched by this
review.

---

## 9. Cheapest next computation and review obligations

**Free (no computation).** Land the 7.3 corollary: `a1^i notin J0` for all
`i <= 6` follows from the ideal property alone. Correct the report's
attribution to V38, and correct the V42 `a1^8` statement to the branch ideal
`I_A1`.

**Cheapest real computation.** Finish and harvest the `F_65519` modular lane.
The sources already exist (`rho0_dual_linbox_modp_v43.cpp`,
`validate_rho0_dual_linbox_modp_v43.py`,
`resume_rho0_dual_linbox_modp_aws.sh`); no `aws_*` modp harvest exists under
the case as of this review, so the preregistered independent-prime
corroboration is currently **undelivered**. It is cheap and discharges a
preregistered control. It remains corroboration only; the exact-Q lane is
authoritative and already sufficient.

**Next discriminator, sized.** Exponent seven at weight 35. Using the same
generating function over the 66-variable alphabet:

```text
weight 30 (N=6):    284,766 products      (frozen: 928 s, 34.9 GB peak)
weight 35 (N=7):  2,715,310 products      ~9.5x
weight 40 (N=8): 21,933,775 products      ~77x
```

Exponent seven is plausibly within the 6 h / 192 GiB caps but the component
and the LinBox solve grow superlinearly; run **preflight + modular screen
first** to size the target component before committing an exact-Q solve.
Exponent eight looks out of reach for this exact-Q architecture.

**Review obligations, in priority order.**

1. Replace the tautological target-coefficient mutation control
   (`validate_rho0_dual_linbox_v43.py:134-144`) with a **row-data** mutation
   in the style of the preregistered V42 `Tg19_7` control. Present detection
   power is ~0; a random non-target coefficient mutation would be vacuous
   95.71 % of the time; a row mutation perturbs `N(30-grade)` products at once
   and genuinely exercises `reconstruct_rows`.
2. Either run the pinned V42 replay in the lane and harvest it, or move the
   custody-hash block out of `main()` so the theorem pins are enforced by the
   consumers that actually run (`compile_total_dvr_w30_v43.py:454-462` is
   currently unreachable from both harvested lanes).
3. Harvest `AWS_SOURCE_MANIFEST.sha256` for compiler-only lanes, or re-point
   the compiler harvest's `launch_registration.txt` at a frozen manifest.
4. Disclose the `rc=1` compiler-harvest build failure in the producer report,
   with the one-line explanation (missing `-lgivaro -lgmpxx -lgmp`, fixed on
   resume).
5. Include `PREREGISTRATION_CENSUS_ADDENDUM.md` in the next V43 source freeze,
   per its own freeze rule.
6. Re-derive the literal row coefficients from the V20/V28/V35 emitter chain
   in some future review. It is the one component shared by the solve and
   certify paths and the only part of the chain this review did not attack
   independently.
