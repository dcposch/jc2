# Canonical integration map: weighted Section 7 repair and Section 9 dependency

**Date:** 2026-08-28  
**Author:** GPT-5.6 Terra / Codex  
**Task:** read-only canonical consumer audit; no canonical file edited

## 0. Exact theorem packet and disposition

The exact producer/review pair integrated here is:

```text
c253bd12d205eed7c01e42a21204c5735d0f5cba70dce1d962fb8744dbd95eb6
  xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md

727f58506af4ff36f6a8c39bb83420c5077c2e4872e6e48bd42ec165c2323aa8
  xmodel/sigray-section7-weighted-euler-inequality-hostile-review-terra-20260828.md
```

The amended producer is **PASS**.  The original producer hash
`5036f9a2...` is **FAIL** because it multiplied the generic weight by the
ramification multiplicity of `P_i` at the special quotient point.  Nearby
ramification indices over different moving `Q_i`-values cannot be added.

The exact promoted replacement is:

```text
d-N = sum_i (phi_i)_! w_i,
d-1 = sum_i integral_(U_i) w_i dchi_c,
integral_(U_i) w_i dchi_c >= b_i^+,
b_i^+ = kappa_i^+(u_i-1),
kappa_(F_i on a_0)*(u_i-1) <= b_i^+.
```

Consequently, for every prescribed fibre and every set `S` of pairwise
distinct critical-value flags on that fibre,

```text
td(f,g) >= 1 + sum_(F in S) kappa_F(pi(F)-1).       (C7.1*)
```

This restores the exact numerical content of Corollary 7.1.  It does so by
integrating actual cluster weights.  It does **not** assert that the actual
vertex decoration `kappa_F` is constant across fibres.

### Green / red / amber boundary

| item | status after this packet |
|---|---|
| repaired Proposition 7.3 proper-tube cluster inequality | **GREEN** |
| actual-weight pointwise pushforward and Euler identity | **GREEN** |
| Corollary 7.1 inequality for distinct flags | **GREEN** |
| singleton-chain first-separation budgets (25)/(26) | **GREEN** |
| repaired Section 9 row-4 exclusion | **GREEN**, after the reviewed Section 9 corrections |
| corrected theorem `counterexample => td>=6` | **GREEN at the internal reviewed-repair tier** |
| any Section 9 exclusion of `td=6` | **RED / not claimed** |
| literal per-puncture `delta_a` and Proposition 7.4 | **RED / unproved** |
| printed Proposition 7.5 equation (22) | **RED / source proof invalid; global statement unproved** |
| fixed-weight `(22-cl)` from cross-fibre `kappa` transport | **RED / unproved** |
| cross-fibre equality of jump/max `kappa_F` | **RED / inference refuted** |
| old multiplicity-strengthened `w(z_0)>=r_0 b_i^+` | **RED / locally refuted** |
| literal nested `Y(F)` sums in Section 9 | **RED / double-counting** |
| slack-zero `delta_a=0 on every fibre` claims | **AMBER / not supplied by the promoted theorem as stated** |
| multipole sums of several chain charges | **AMBER until their exit sets are proved globally disjoint** |

The phrase “fixed baseline” needs precision.  The new `b_i^+` is a fixed
**comparison floor for actual cluster mass**.  It is not declared to be the
actual vertex weight on every fibre.  What is quarantined is the old claim
that a fixed reference value `kappa_(F_i)(u_i-1)` transports as the actual
baseline and yields `(22-cl)`.

## 1. Section 9 status after discharging the Section 7 rider

The reviewed Section 9 packet is:

```text
2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933
  xmodel/sigray-section9-source-audit-sol-ultra-20260828.md

0729a5765729a9e3a6f99720a638cc94a3d3a7837e3946412e13c4233e6b5bad
  xmodel/sigray-section9-source-audit-hostile-review-gpt55-20260828.md
```

Its only live mathematical rider was repaired Corollary 7.1 plus honest
first-separation/no-duplication.  The weighted packet now discharges that
rider.  The corrected Section 3--8 stack named by the Section 9 review is
also review-closed at its stated scope.  Therefore the current status is:

```text
Printed Section 9 proof:                 INVALID / incomplete.
Corrected internal reconstruction:       REVIEW-CLOSED.
No normalized counterexample has td<=5:  PROVED at the internal repair tier.
Hence counterexample => td>=6:            PROVED at that tier.
Exclusion of td=6:                        NOT PROVED and not part of Thm 9.1.
Root Proposition 8.4:                     NOT USED in the corrected proof.
```

The producer's broad sentence “IIa `k>0` forces `l=0`” must still be read
with the hostile review's correction: it is safe in the actual `mu=2`
branches solved there; it is not a universal IIa theorem.  This correction
is non-load-bearing for row 4 and `td>=6`.

### Exact repaired assembly

1. For `td<=5`, every-fibre Proposition 5.8 and `Lambda>=3` force a single
   pole and table row in `{1,4,5,7,10}`.
2. Rows `1,5,7,10` have pinned `M=1` at the pole.  Pole vertices are
   nonroot, so corrected Proposition 8.4 kills them.
3. Row 4 is closed by the corrected transition lists, first-separation
   exit budget, H3-psi, finite characteristic-sequence termination,
   nonroot `M=1` exits, and the case-IV `(m)` integrality obstruction.
4. Root terminations use `(m)` or H3-psi, never root Proposition 8.4.

The ongoing root-aware engine rerun is therefore irrelevant to the truth of
this `td>=6` reconstruction.  It remains essential for claimed exhaustive
`td=6` survivor counts.

## 2. Proof-dependency caveats canonical prose must retain

1. **Distinct sets, not multisets.**  `(C7.1*)` applies to pairwise
   distinct critical-value flags.  The singleton-pole Section 9 repair
   proves this by first-separation sets
   `E_i=Y_lit(F_i)\Y_lit(F_(i-1))` and by putting the x-side `psi` vertex in
   the other tree component.
2. **Multipole chains need an extra disjointness check.**  Corollary 7.1
   itself is now unconditional, but adding charges from two or more pole
   chains is valid only after proving that the corresponding exit sets are
   disjoint after shared suffixes are identified.  The singleton Section 9
   theorem does not automatically prove that multipole version.
3. **Actual weights, not transported decorations.**  Pushforward formulas
   must use `w_i(z)=sum_(P in C(i,z)) Lambda(P)`.  Never substitute an
   allegedly transported actual `kappa_i(a)`.
4. **The one-point tube bound has no multiplicity factor.**  One nearby
   simple direction has local degree `b_i^+` and is bounded by the special
   tube's total degree.  Several nearby points may have distinct `Q` values.
5. **Zero is not a simple-low counterexample.**  If
   `kappa_i^+>kappa_i^-`, then the effective cover order `m_i>1`, and the
   covered root `eta=0` is multiple.  The simple-direction equality cannot
   assign it the low weight.
6. **Slack equalities require a separately stated corollary.**  The passed
   theorem proves an inequality and the exact actual-weight integral.  It
   does not name or promote the historical `delta_a`.  If the campaign
   wants to recover a global slack-zero statement from equality in
   `d-1=sum integral w_i >= sum b_i^+`, it should state that as a new
   actual-weight saturation lemma and hostile-review it before canonical
   use.
7. **Evidence tier.**  “Unconditional” below means no remaining campaign
   hypothesis inside the corrected normalized-counterexample theorem
   stack.  These are internal reviewed repairs of an unrefereed thesis,
   not new external peer review.

## 3. Top-level canonical files

Line numbers below refer to the read-only snapshot hashed in Section 8.

### `AUDIT.md`

**Current scope:** lines 17--50.

Exact replacement:

- Change the heading from “repair active” to “weighted repair passed;
  consumer integration active.”
- Preserve the quarantine paragraph for printed `(22)`, `(22-cl)`, and
  fixed `kappa` transport.
- Replace the candidate/conditional paragraph at lines 42--49 by:

```text
The actual-weight repair c253bd12... passes exact Terra hostile review
727f5850....  Its one-point proper-tube specialization proves
w_i(z_0)>=b_i^+ without transporting kappa and without a ramification
multiplicity factor.  Compact-Euler integration therefore proves repaired
Corollary 7.1 for every distinct cv set.  This discharges the final rider
on the reviewed Section 9 reconstruction 2763d970... / 0729a576...:
inside the corrected Sections 3--9 stack, counterexample => td>=6 is now
review-closed and does not use root Proposition 8.4.  Section 9 still does
not exclude td=6.  Printed (22), literal delta_a and fixed-weight (22-cl)
remain quarantined.
```

### `PROGRESS.md`

**Current scope:** lines 18--31.

The mathematical summary is already accurate.  Replace “therefore
provisionally promotes” by “therefore review-closes/promotes at the internal
repair tier.”  Retain the sentence that `td=6` is not excluded and that MP8's
strong literal-`(22)` claim is not restored.

### `notes.md`

Do not rewrite historical events at lines 11420ff.  Append a new event and
new LIVE STATE recording:

```text
WEIGHTED SECTION 7 GATE PASSED.  c253bd12... / 727f5850... restore only
Corollary 7.1 via actual weights.  Printed (22), delta_a, (22-cl), and
cross-fibre kappa invariance remain quarantined.  The Section 9 rider is
discharged, so the corrected td>=6 theorem is review-closed; td=6 remains
open.  Canonical equality/slack claims and multipole no-duplication are
being scoped separately.
```

The earlier 2026-08-07 entries are provenance, not current truth.  They
must not be cited without the new supersession event.

### `APPROACHES.md`

**Current scope:** lines 85--92.

Replace “after the remaining Section 7 source perimeter is reviewed” by a
statement that the Corollary 7.1 perimeter is now closed, while exact
per-puncture/slack identities remain unavailable.  No avenue ranking needs
to change solely from this repair; the repaired theorem strengthens the
Sigray backbone and removes a source-trust blocker.

## 4. Core Sigray ledgers

### `ladder/SIGRAY-AUDIT.md`

This file presently ends its statement census at Section 6.  Add a
supplementary Section 7 ledger without altering the 72-item count:

| item | source verdict | corrected campaign verdict |
|---|---|---|
| St 7.1 | verified | `pi(F)>1` |
| St 7.2 | proof absent | repaired by Prop 5.1 sidedness/non-leakage |
| St 7.3 / Prop 7.2 | proof absent | repaired local statements |
| Prop 7.1 | proof errata | repaired |
| Prop 7.3 | proof/typing gaps | proper local-tube cluster inequality repaired |
| Not 7.3 | indexing incompatible with Prop 7.3 | literal per-puncture delta quarantined |
| Prop 7.4 | not proved literally | not promoted |
| Prop 7.5 (22) | invalid proof / wrong ledger | not promoted |
| Cor 7.1 | printed proof invalid | replaced by `c253bd12...`, review `727f5850...` |

Exact source chain to cite: full audit `0159cdf1...`, hostile review
`af1ce600...`, quotient final delta `758c0226...`, weighted producer/review
`c253bd12...` / `727f5850...`.

Also amend the current Tier-3 Statement 3.14 note: the cyclic quotient and
transport `tau` repair exact coordinate twisting, but Statement 3.14 does
not transport the set of zero/nonzero roots across different fibre values
and hence does not transport jump/max `kappa`.

A second supplementary entry may record Section 9: printed proof fails;
corrected theorem `td>=6` review-closed via `2763d970...` / `0729a576...`
after the Section 7 packet; no `td=6` exclusion.

### `ladder/REDUCTION.md`

Required replacements:

1. **Frontier overlay, lines 25--29:** remove the statement that Sections
   7--9 audits are still queued.  Say Sections 7--9 are audited at their
   corrected scopes; remaining gaps are landing/coverage, `RPMC(C)`, and a
   cofinal `td`/complexity ceiling, not Corollary 7.1.
2. **Section 2.3 Section-7 row, line 806:** replace “no standalone promoted
   replacement” by the exact green/red boundary above.
3. **Section-8 row:** record nonroot-only Proposition 8.4 separately from
   the Section 7 change.
4. **Section-9 row:** cite `2763d970...` / `0729a576...`; list first-exit
   `Y` repair, sign E6, E2--E4, and corrected theorem.
5. **Theorem 9.1 row:** retain “printed proof incomplete,” then add that the
   internal corrected reconstruction now proves the same `td>=6`
   conclusion.  The published Zoladek theorem remains independent support.
6. **Section 2.4 internal sources:** add one row for the weighted Section 7
   packet and one for the Section 9 reconstruction.
7. **Trust-set paragraph:** replace raw Statement 9.4/literal `Y` by the
   first-separation exit-set version consuming repaired Corollary 7.1.

Suggested exact Section-7 table cell:

```text
Full audit finds the printed per-puncture delta and Proposition 7.5 (22)
unproved.  Fixed-weight (22-cl) also fails because jump/max kappa varies
across fibres.  The actual-weight replacement c253bd12..., hostile-reviewed
at 727f5850..., proves Corollary 7.1 for every distinct cv set.  Do not cite
(22), literal delta_a, or cross-fibre kappa invariance.
```

## 5. Singleton-pole / Section 9 consumer files

### `ladder/SHEET6.md`

Lines 69--77 already distinguish the incomplete printed proof from later
campaign work.  Add the two exact hashes and change “campaign repairs” to
“review-closed corrected reconstruction.”  In the method skeleton around
line 87, define the budget using first-separation exit charges rather than
literal `lambda_F=sum_(H in Y(F))`.

### `ladder/SHEET6-PILOT.md`

At lines 85--89, mark the Corollary 7.1/generalized-lambda item as resolved:
the weighted theorem supplies the global inequality, and the Section 9
first-separation theorem supplies disjoint singleton-chain charges.  Keep
`td=6` termination/coverage open.

### `ladder/SHEET6-CAMPAIGN.md`

This file needs a scoped supersession block, not isolated word swaps.

1. **Header, lines 7--30.**  Upgrade `td<=5` from “zero in recomposition”
   to the review-closed corrected theorem, while retaining “not complete as
   printed.”  Replace every assertion of a full `(22)` ledger or
   `delta_a=0 on every fibre` by Corollary 7.1 budget language.  Keep the
   local first-exit result `lambda_root^exit=0`; do not justify it through
   `(22)`.
2. **Assembly, lines 41--45.**  Write
   `sum lambda_i^exit <= td-2`, not literal nested `lambda_F`; corrected
   Proposition 8.4 applies to nonroot down vertices.
3. **Pattern template, lines 55--64.**  Restrict “IIa `k>0=>l=0`” to the
   actual `mu=2` branches certified in the Section 9 review.
4. **H2, lines 92ff.**  Replace the standing reading hypothesis by the
   proved singleton-chain first-separation construction.  H2 is discharged
   for the `td<=5` theorem.
5. **G3, lines 300ff.**  Preserve the source criticism, then say the
   corrected theorem now closes rows `1,5,7,10` at nonroot pole entries and
   row 4 by the repaired transition proof.
6. Keep every `td=6` survivor count subject to the separate root-aware
   rerun; Section 7's promotion does not certify those counts.

### `ladder/SHEET6-REVIEW.md`

This is a historical review of the printed-source defects.  Add a banner:

```text
SUPERSESSION 2026-08-28: G2/G3 remain valid diagnoses of the printed
thesis.  The corrected Section 9 reconstruction now closes row 4 and rows
1,5,7,10 using the weighted Corollary 7.1, first-separation exit sets,
nonroot pole-entry M=1 kills, and H3-psi.  Thus td>=6 is review-closed in
the corrected internal stack, although the printed proof remains invalid.
```

Do not rewrite the historical attack details.

### `ladder/SHEET6-AF2.md`

At lines 59--67, replace literal Notation 9.3 support by local
first-separation exit sets.  The corrected `(24)` price attaches a distinct
cv flag to each alternative direction subtree.

### `ladder/SHEET6-AF3.md`

The pole pin and entry kills are unchanged.  At lines 95--110, add that the
row-selection layer plus repaired row-4 closure now proves `td>=6` inside
the reviewed stack.  At lines 200--210, replace E9's “branch-at-F reading”
by the proved first-separation definition.  Root `M` comments must remain
separate: root Proposition 8.4 is unavailable.

### `ladder/SHEET6-A2P-REVIEW.md`

Front 4's **conclusion** (one shared global budget) survives.  Replace its
source at lines 164--169:

```text
The shared budget follows directly from weighted Corollary 7.1 applied once
to the union of pairwise distinct first-separation exit flags plus the
x-side psi flag.  It does not follow from printed (22) or delta_a.
```

The rider at lines 180ff is resolved for a singleton chain.  For the
two-pole union, preserve the requirement to prove cross-chain disjointness
after shared suffixes are deduplicated; the old assertion should not be
upgraded merely from the singleton theorem.

### `ladder/SHEET6-A3L1-REVIEW.md`

Front 8's diagnosis of literal E9 remains correct, but H2 is no longer a
reading hypothesis on singleton chains.  Replace lines 280--287 by the
first-separation theorem and the weighted Corollary 7.1 citation.  The
four-class `td=6` book is not certified exhaustive by this change because
the root-aware rerun is separate.

### `ladder/SHEET6-H3.md`

H3-psi survives and becomes cleanly typed.  Required exact changes:

- replace `lambda_F` in the theorem by `lambda_i^exit`;
- define the pairwise disjoint `E_i` first;
- apply `(C7.1*)` once to `(disjoint union E_i) union {x-side G}`;
- remove “uses only printed thesis statements”; it uses the reviewed
  Section 7 replacement;
- preserve all numeric psi kills;
- update the row-4 conclusion to the fully reviewed Section 9 closure.

The theorem then has no Section 7 rider.  Its applications to arbitrary
vertex lists still require actual distinctness.

### `ladder/SHEET6-HIII-REVIEW.md`

Add a supersession banner.  Front 1's psi arithmetic and row-4 numerics
survive; “printed-statement-solid” and “printed data only” do not.  Replace
them with “review-closed under the corrected Section 7 first-separation
package.”  H2 is discharged for the singleton row-4 chain.

## 6. Equality/slack-heavy files

### `ladder/SHEET6-LROOT.md`

This file has the largest Section 7 blast radius.

**Survives:**

- the local case-IV fact that no y-side branch first separates at the root,
  hence `lambda_root^exit=0`;
- the x-side `psi` charge;
- LR2's “one x-side cv flag with `kappa=1`” conclusion, because it uses only
  the Corollary 7.1 inequality and positivity;
- fixed-fibre statements that selected positive charges exhaust the full
  `td-1` budget.

**Must be withdrawn or separately reproved:**

- every claim that Proposition 7.5 `(22)` was itemized or balanced;
- the per-class `delta` column as literal Sigray `delta_a`;
- “`delta_a=0` on every fibre”;
- “every inequality in `(22)` is equality”;
- the statement that no refinement of the Euler equality can ever create a
  charge;
- per-puncture nondegeneracy conclusions.

Exact replacements:

1. Header lines 20--31: say the Corollary 7.1 budget saturates at the
   selected carrier-fibre flags; remove `(22)` and `delta_a` language.
2. Section 1 lines 51--65: replace printed Proposition 7.5 by `(C7.1*)`
   and the actual-weight formulas.  Do not call it an exact fixed-weight
   vertex ledger.
3. LR2 line 150: cite `(C7.1*)`, not `(22)`.
4. Section 4: rename the `delta` column `unspent C7.1 budget`; zero means no
   further positive cv flag on that fibre, not literal `delta_a=0`.
5. Section 5b item 3: quarantine.  If desired, formulate a new
   actual-weight saturation lemma from equality in
   `d-1=sum integral w_i>=sum b_i^+`; review it separately.
6. Section 5c item 1: the correct strictness target is
   `w_i(z)>b_i^+` at an exceptional quotient point, not `delta_a>0` or a
   per-puncture excess.  The local equality model still shows that
   multiplicity alone does not force this strictness.
7. Trust perimeter: replace “Section 7 complete / LR2 uses (22)” by the
   exact weighted packet.

### `ladder/SHEET6-LT-REVIEW.md`

Add a strong supersession banner:

- Front 1's local `lambda_root^exit=0` and LR2 inequality survive.
- Its claimed `(22)` itemization and per-puncture `delta` completeness do
  not survive.
- Front 2 must be renamed from “delta strictness” to “actual-weight strict
  specialization `w_i(z)>b_i^+`.”
- The local collision/equality controls remain valuable negative evidence.

The historical review should no longer be cited as hostile confirmation of
printed Proposition 7.5.

## 7. Multipole files

### `ladder/SHEET6-2POLE.md`

1. The shared-budget conclusion at lines 117--132 survives only after a
   global distinctness proof for the union of both chains' exit sets.  Cite
   weighted Corollary 7.1, not Proposition 7.5 `(22)`.
2. Replace “no other printed tie” with “no other tie from the corrected
   reviewed package.”
3. At Section 6c, replace the `delta_a>0` merge-charge proposal by strict
   actual-weight specialization or by a direct new cv-exit lemma.
4. Section 7 item 2 conflates `td>=6` with exclusion of `td=6`.  A two-pole
   `3+3` configuration is allowed by Theorem 9.1 and is not a gap in its
   proof.  It is a gap only in the separate campaign attempting to exclude
   degree exactly six.
5. Root-merge counts remain pending the separate root-aware rerun.

### `ladder/SHEET6-MULTIPOLE.md`

MP8's local core survives but its Euler-equality rhetoric does not.

- Define a global first-exit partition of cv flags relative to the chain
  tree `U`, including shared suffix deduplication.
- Prove the pure `M=1` forest and all-`M=1` merges have no such exit flags.
- Then conclude their **Corollary 7.1 charge is zero**.
- Remove “itemizing equality (22),” “identically zero rows of (22),” and
  “no refinement can ever charge” unless a new actual-weight saturation
  theorem is supplied.

Theorem O's concrete zero-spend witness and the local `lambda=0` anatomy
survive.  Separately, MP2 must exclude the root from its Proposition 8.4
scope; that is a Section 8 correction, not caused by this packet.

### `ladder/SHEET6-MP-REVIEW.md`

The review's “MP8 stands as printed” is no longer current.  Replace it by:

```text
MP8 local no-exit/zero-Corollary-7.1-charge core survives after a global
first-exit disjointness proof.  Its literal (22) itemization and categorical
no-refinement conclusion are demoted.
```

The finite-book and root-scope caveats are independent.

### `ladder/SHEET6-TDUNIFORM.md`

The uses of the `td-1` and `td-1-psi` inequalities remain valid.  Replace
their dependency citation by weighted Corollary 7.1/first-separation where
appropriate.  Do not introduce exact `delta` or `(22)` language.  The
structural finding that these budgets grow with `td` is unchanged.

## 8. Snapshot custody

The read-only snapshot used for the line-scoped map was:

```text
f7c6665729862beeb6f688391af1fd875dedc5cf0c58175e955dd04f4185c3e3  AUDIT.md
99244fc3d51056d0170ef606e6aa654363d23f7f0fc946c2ff63a75a3d6f6ab6  PROGRESS.md
c78d3aac10fad01ec4cb95154128cdfe68b348ae5ffce5791b94b663ee689351  notes.md
87c0731a4743f79a44271690d7d899fdb6e0036a98ba5c12762aa83760981014  APPROACHES.md
f1da7026320b3dedd47534428aa53e6df66c698888c398e4f7eb5288d89b0748  ladder/SIGRAY-AUDIT.md
dd3eee2f98e7757ab375a4ae243da256941c15e06a9e762e958cc647c70d52a9  ladder/REDUCTION.md
5ea8003685a8be0c2554f6966987cbd492583bf9c07603ccb984da48b3ac04f2  ladder/SHEET6.md
0cc1120726bde58a79cd011c969922119247a48fae08f4f8c82a76c966fadf18  ladder/SHEET6-PILOT.md
086a475927b5cdec68dcdffc836bf06c0418616113aa3ccc91bc98d9eafb1678  ladder/SHEET6-CAMPAIGN.md
89d6303c28908274521b5247891cc643be066eeac2ec05bd13618c378b5ed97c  ladder/SHEET6-REVIEW.md
a0d71267314471e976dff11f6243f6a4e83b92579bdc9e246eafc891a5718384  ladder/SHEET6-H3.md
aaaf1dbaba44128200814dfb576f64a9f073e08c01ccfa11230a0b79f97fe86e  ladder/SHEET6-HIII-REVIEW.md
905988471cf1458b5be949b7dfa2636f8e6b29a114cb7c2f1e30df11deb18d34  ladder/SHEET6-AF2.md
555363fde61291a0c689bbf9d789c01f73734e0c403d350d85ae2fd0ddab8099  ladder/SHEET6-AF3.md
cf84555a61c9e69a33dc6abe67bbe5d79463d4deb15a1fb31743d13b3134a61e  ladder/SHEET6-A2P-REVIEW.md
6c045f36686e5dd73c6f067597d8a01857094a1add06288b955ef0e06b6aa44b  ladder/SHEET6-A3L1-REVIEW.md
9ff5d00567d7b6752ecc79892bb41959a450ddff3837bdb26179899ad2dfad5a  ladder/SHEET6-LROOT.md
82d94e1a43ae9ec315189b4892faafa840027f4f1696dba6a394866331aa22c6  ladder/SHEET6-LT-REVIEW.md
2cc7c194b9dceacb4e900626677930941ecd46103da259bb2159b4a0314e1bda  ladder/SHEET6-2POLE.md
78215e1ff847f10ee4df26615443f56ab49c9e21366137898c0742525d78decc  ladder/SHEET6-MULTIPOLE.md
04247d669dcd7aab64b1f89a363f0aa7087afbec83dd6ef723588aef188b4e88  ladder/SHEET6-MP-REVIEW.md
```

No canonical file was edited.  No heavy computation was run.  No file or
directory under `jc2-lean` was accessed, listed, searched, built, modified,
statused, or controlled.
