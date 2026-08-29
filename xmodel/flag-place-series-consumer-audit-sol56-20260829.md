# Campaign-wide audit: critical-value flags/places versus conjugate Puiseux series

Date: 2026-08-29  
Author: Sol 5.6  
Status: sealed bounded consumer audit; no canonical edit in this file

## Executive verdict

The newly exposed shortcut is genuinely present in three report families:

1. the td8 trunk producer and one of its hostile rereviews;
2. the td12 U1 first-trunk producer; and
3. the promoted td6 LR2 proof sentence that derives an unsplit x-side
   Puiseux cluster from one critical-value flag.

The shortcut is:

> one critical-value flag, or one place/ray, implies that all conjugate
> Puiseux series stay together; equivalently, every loss of Puiseux series
> creates a second critical-value flag.

That implication is false.  The Eggers--Wall tree has one ray per
**place/puncture**, while a place can have several Galois-conjugate Puiseux
series.  Conjugate shedding at a characteristic exponent changes the
denominator and can decrease the series count (N) while leaving one place,
one ray, and one orbit-level critical-value flag.

The correct exhaustive split is:

- a parting into distinct places/direction-orbits gives distinct later flags
  once the contact level is strictly below the cv level; or
- conjugate shedding inside one place gives no second flag but forces a
  denominator jump (q=\kappa_H/\kappa_F\ge2).

After applying this dichotomy:

- the reviewed td8 affine equal-join route is still killed;
- the td12 U1 B-charge is still exactly (8), and its depth-(24) gate
  remains valid;
- the td6 LR2 conclusion -- one x-side cv flag, (\kappa_G=1), and one
  unsplit series cluster through the cv level -- remains valid;
- no currently live route is resurrected or newly killed.

One evidence-status statement does change: the td8 route kill has one sound
different-model repair in the Opus review.  The Grok rereview reaches the
same verdict but repeats the place/series conflation in its load-bearing
single-flag argument, so it is not a second independent correct proof of
that step unless repaired.

The older td8 claims that the affine route could survive with three
per-ray charges equal to (2), and that its cv set then had exactly four
vertices, are false and already superseded by the reviewed trunk kill.

## 1. Scope and search perimeter

This was a read-only mathematical consumer audit over only the authorized
campaign paths:

```text
AUDIT.md  APPROACHES.md  PROGRESS.md  notes.md  ladder/  xmodel/  ops/
```

Repository ignore rules were honored.  The prohibited
`ideation-20260829T0820Z` lane submission was excluded and not read.  No web,
AWS, heavy computation, canonical edit, round-artifact edit, commit, or push
was used.

The search included the direct phrases “one/single cv flag,” “unsplit
cluster,” “split creates distinct flags,” “no remerging,” “conjugate
shedding,” every direct reference to LR2, and the first-separation/orbit
attachment packets.  Incidental uses of “sheet” in unrelated algebraic
calculations were not treated as consumers.

## 2. Exact type dictionary

The following distinctions are load-bearing.

1. A puncture (P\in\bar R_a\setminus R_a) is a place and supplies one ray
   (u\mapsto I_P(u)) in the tree.
2. A place can be represented on a suitable cover by several conjugate
   Puiseux series.  Proposition 3.1 counts these series in
   (\deg p_{I_P(u)}); it does not count cv flags.
3. Definition 3.3's no-remerging law applies to distinct **places/rays**.
   It does not turn conjugate representatives of one place into different
   rays.
4. A characteristic exponent sheds conjugate series within one place.
   Notation 3.5 records it by a strict denominator increase.  Thus, along a
   selected ray,

   \[
   q:=\frac{\kappa_H}{\kappa_F}>1
   \]

   whenever such shedding occurs between (F) and (H).
5. Distinct place/direction-orbit branches with contact
   (O(P,Q)<\pi(H)) give distinct flags at height (\pi(H)).  If the
   contact is exactly (\pi(H)), the places may share the endpoint flag
   and split above it; endpoint language must therefore be strict.

This dictionary is stated correctly in the Opus td8 review
`m2-td8-trunk-exact-charge-r1-hostile-review-opus5-20260829.md:39-55,
214-230,320-334` and in the Fable td12 review
`m2-td12-u1-next-trunk-discriminator-r1-hostile-review-fable5-20260829.md:
116-165`.

## 3. Live/reviewed consumer ledger

### 3.1 td12 U1 B-direction

| consumer | citation | classification | effect and smallest fix |
|---|---:|---|---|
| Sol producer | `xmodel/m2-td12-u1-next-trunk-discriminator-r1-sol56-20260829.md:130-157,194,345-349` | **REPAIRABLE; ALREADY SUPERSEDED BY REVIEW** | “A sheet split creates two flags” covers distinct-place/orbit splits only. Insert the Fable two-case proof. Charge (8), exclusion of (9), and the depth-(24) gate do not change. |
| Fable hostile review | `xmodel/m2-td12-u1-next-trunk-discriminator-r1-hostile-review-fable5-20260829.md:54-67,116-165,210-229,271-279,336-361` | **SOUND** | It explicitly separates distinct-orbit parting from conjugate shedding and repairs the proof without changing a number. |
| Current overlays | `AUDIT.md:48-66`; `PROGRESS.md:8-19`; `APPROACHES.md:27-35`; `notes.md:12799-12811` | **SOUND, WITH ONE ENDPOINT WORDING NIT** | The overlays use the repaired dichotomy. Replace “a split is first allowed at level 25” by “a distinct-place/orbit split may first occur at level 25; conjugate shedding there is still excluded by (q\ge2).” The finite gate remains levels (1,\ldots,24). |

The repaired proof is short.  Unconditionally,

\[
\tau_0\ge D_F/i=25,
\qquad
\operatorname{wt}(H)=q(\tau_0-17).
\]

If (q\ge2), one flag costs at least (16), contradicting
(12\ge1+\operatorname{wt}(H)).  If (q=1), conjugate shedding is
impossible; any genuine pre-cv loss is then a distinct-place/orbit split and
gives two flags, each priced at least (8), again contradicting (td=12).
Thus there is no loss, (N\equiv i), (\tau_0=25), (q=1), and the exact
price is (8).

### 3.2 td8 trunk-arity kill

| consumer | citation | classification | effect and smallest fix |
|---|---:|---|---|
| Sol trunk producer | `xmodel/m2-td8-trunk-exact-charge-r1-sol56-20260829.md:111-151,176-180,231-243` | **REPAIRABLE; ALREADY SUPERSEDED BY OPUS** | The statements “later split produces distinct flags” and “one flag implies all (2i) series agree” are false without a place/conjugate case split. Replace §3 by the Opus ramification dichotomy. The lower bound (\lambda_{tr}\ge3) and route kill remain true. |
| Opus hostile review | `xmodel/m2-td8-trunk-exact-charge-r1-hostile-review-opus5-20260829.md:39-55,434-529,604-619,650-700` | **SOUND** | It identifies the exact defect and proves the corrected (q\ge2) versus (q=1) lemma. This is the load-bearing hostile validation. |
| Grok hostile rereview | `xmodel/m2-td8-trunk-exact-charge-r1-hostile-rereview-grok46-20260829.md:13-21,109-129,220-280,350-357` | **REPAIRABLE AS MATHEMATICS; NOT AN INDEPENDENT VALIDATION AS SEALED** | Its single-flag argument treats series as tree ends and its countermodel table says sharing one flag means no split. Replace Charges 3--5 by the Opus lemma. Its numerical conclusion remains right. |
| Current overlays | `AUDIT.md:8-43`; `PROGRESS.md:21-35`; `APPROACHES.md:9-21`; `notes.md:12778-12796` | **SOUND MATHEMATICALLY** | They state the repaired (q)-dichotomy. The prose claiming two independent correct reconstructions should be softened: only Opus repairs the key type error; Grok agrees on the verdict but not with a sound sealed proof of this step. |

For the td8 trunk, every flag satisfies

\[
\tau_0\ge17/2,
\qquad
\operatorname{wt}(H)=q(\tau_0-7),
\qquad
\operatorname{wt}(H)\in\mathbb N_{>0}.
\]

If any (q\ge2), that flag costs at least (3).  If (q=1), no conjugate
shedding occurs.  Were there only one flag, all distinct places would also
stay together, whence (N\equiv2i), (\tau_0=17/2), and the flag weight
would be the impossible integer (3/2).  Hence there are at least two
distinct flags, each of weight at least (2), and total at least (4).
This proves the trunk floor (3) without conflating flags and series.

The displayed (2i\to i) profile at (q=1) really does create two flags:
with no characteristic jump it is a distinct-place/contact split.  Thus that
specific sentence remains true after its missing (q=1) premise is stated.

### 3.3 Promoted td6 LR2 x-side pin

| consumer | citation | classification | effect and smallest fix |
|---|---:|---|---|
| LR2 primary text | `ladder/SHEET6-LROOT.md:158-174,182,253-255` | **REPAIRABLE; CONCLUSION UNCHANGED** | The proof sentence “a split ... gives at least two cv vertices” handles distinct places only. First derive the unique flag (G) and (\kappa_G=1) from the budget, then exclude place splits by no-remerging and conjugate shedding by (\kappa_G=1). |
| LR2 review | `ladder/SHEET6-LT-REVIEW.md:82-89,359-360` | **REPAIRABLE** | It independently rederives “one flag” and (\kappa_G=1), but does not spell out the two-mode implication to all series. Add the same two sentences. |
| Section 7 integration | `xmodel/sigray-section7-weighted-euler-canonical-integration-map-terra-20260828.md:402-429,445` | **SOUND FOR ONE FLAG + (\kappa=1); INCOMPLETE FOR THE SERIES COROLLARY** | Its preserved statement is exactly the part needed for the repair. Add Notation 3.5 before exporting “single series cluster.” |

Here is the complete repaired LR2 implication.  Let (G) be the sole
x-side cv flag.  The actual-weight budget establishes (\kappa_G=1)
without using any no-split assertion.

- If two distinct x-side places separate below (G), Definition 3.3 makes
  their flags at (G)'s height distinct, contradicting uniqueness of (G).
- If conjugate series of one place shed below or at (G), Notation 3.5
  makes the denominator at (G) strictly larger than the root denominator
  (1), contradicting (\kappa_G=1).

Therefore all x-side places and all of their conjugate series agree through
the LR2 interval.  The advertised single-cluster/no-characteristic conclusion
is valid; only its printed proof order was incomplete.

There is a second wording defect in the same file:
`ladder/SHEET6-LROOT.md:224` says a single-orbit chain node has “NO series
leave (all conjugates).”  What is established and needed is only:

> no distinct place/direction-orbit exits at that node, hence no new cv exit
> mass there.

Conjugate shedding is not excluded by a single-orbit statement alone.  It
does not create a new orbit-level exit charge, so the displayed ledger and
the `lambda=0` conclusion do not change.

### 3.4 Direct LR2 descendants

The following live or provisional consumers import the LR2
single-cluster/no-characteristic conclusion.  Once LR2 is repaired as in
§3.3, their consumed premise is valid and none of their conclusions changes.

| group | exact consumers | classification |
|---|---|---|
| canonical template and topology | `ladder/SHEET6-TEMPLATE.md:307`; `ladder/GROK-MONODROMY.md:7,55,133-146,373-431`; `ladder/SHEET6-CLASSICAL.md:47-50,196-208,333`; `ladder/AM-CHECK.md:158-163` | **SOUND AFTER ROOT REPAIR**.  GROK-MONODROMY separately derives 42 distinct generic places from a squarefree degree-42 coefficient equation; it does not infer 42 places merely from one flag. |
| canonical coefficient machinery | `ladder/SHEET6-R1.md:39-40,2065-2079`; `ladder/SHEET6-DIRECTIONB.md:712`; `ladder/SHEET6.md:54` | **SOUND CONDITIONAL CONSUMERS**.  Their shared-centering and future x-side rows use the repaired common truncation only. |
| centering/two-chart controls | `xmodel/td6-global-compatibility-gate-20260824.md:65-78`; its review `:122-165`; `xmodel/td6-two-chart-first-band-20260824.md:60-75`; its review `:111-147`; `xmodel/td6-two-chart-next-row-review-grok-20260824.md:117`; `xmodel/td6-moduli-uniformity-review-grok-20260824.md:126` | **SOUND AFTER ROOT REPAIR**.  The common unramified truncation follows from the repaired LR2 conclusion; the numerical centering remains a chosen control, not terminal-forced data. |
| local equality controls | `xmodel/d73-strict-or-equality-20260824.md:48,150-166`; review `xmodel/d73-strict-or-equality-review-grok-20260824.md:127-155` | **SOUND AFTER ROOT REPAIR**.  These files also explicitly construct the common truncation and first contact, so their local examples do not depend solely on the flawed sentence. |
| bounded boundary controls | `xmodel/td6-boundary-q2-deformation-gate-20260824.md:16`; review `:70,144` | **SOUND/CONTROL-SPECIFIC**.  “Single cluster” is an explicit selected specialization, not a deduction from one flag. |
| future specifications | `xmodel/sol-xside-spec.md:159-161,374,427,978-1084`; `xmodel/sol-h29-dichotomy.md:371-386,635-652`; `xmodel/weighted-d-source-review-grok-20260824.md:219` | **SOUND AS CONDITIONAL/CONJECTURAL USES**.  No theorem there is promoted merely from the shortcut. |

### 3.5 General first-separation and multipole consumers

These nearby consumers were checked because their prose uses no-remerging
and distinct cv witnesses.  They are **sound**: their units are distinct
place/direction-orbits, not individual conjugate series.

- `ladder/SHEET6-AF2.md:27-28,117-130` sums distinct alternative-direction
  subtrees, one cyclic orbit at a time.
- `ladder/SHEET6-H3.md:217-224` and
  `ladder/SHEET6-A3L1-REVIEW.md:296-304` assign orbit-level cv flags to a
  unique first-separation exit set.
- `ladder/SHEET6-MULTIPOLE.md:109-122,157-181` uses “ray” for a place ray.
  Its `M=1` statement “no ray separates” is not a claim that no conjugate
  representative changes.
- `xmodel/sigray-section9-source-audit-sol-ultra-20260828.md:296-324`
  explicitly says cyclically conjugate roots in one orbit count as one
  direction and proves distinctness only for different directions.
- `xmodel/sigray-multipole-selected-orbit-attachment-repair-gpt56-20260828.md:
  50-70,118-170,200-210` proves injectivity for distinct selected cyclic
  direction-orbits in the actual contact quotient.

No repair is needed in this group.  Their statements should not be
strengthened from “distinct direction-orbits give distinct flags” to
“distinct Puiseux series give distinct flags.”

## 4. False but already superseded td8 consumers

The following artifacts contain conclusions that are now false, rather than
merely proofs needing a local reorder.  They are not live after the reviewed
trunk kill.

| artifact | citation | classification and current disposition |
|---|---:|---|
| early exact-lambda primary | `xmodel/m2-td8-equal-join-exact-lambda-primary-grok46-20260829.md:288-305,452-466` | **FALSE CONSUMER; SUPERSEDED.** “One orbit, typically one flag” was used to deny a uniform trunk (\ge3) theorem. The repaired ramification dichotomy proves that theorem. |
| first-extra-jet primary | `xmodel/m2-td8-first-extra-jet-exact-lambda-primary-opus5-20260829.md:65-74,460-478` | **PER-RAY LAW SOUND; THEOREM-F SURVIVAL CONSUMER FALSE AND SUPERSEDED.** The trunk (2i\to i) selected-ray profile was undercounted at the exit-set level. |
| Fable review of that primary | `xmodel/m2-td8-first-extra-jet-exact-lambda-primary-hostile-review-fable5-20260829.md:320-341,405-425` | **FALSE REVIEWED CONSUMER; SUPERSEDED.** It confirmed Theorem F and the four-vertex census before the exit-set correction. Its exact descent and jet-freedom results remain valid. |
| cv/contact gate primary and review | `xmodel/m2-td8-cv-weight-contact-gate-primary-grok46-20260829.md:130-180`; `xmodel/m2-td8-cv-weight-contact-gate-hostile-review-fable5-20260829.md:120-158,350-365` | **FALSE ROUTE-SURVIVAL/CENSUS CONSUMER; SUPERSEDED.** The local tower controls remain historical mathematics, but the route is already dead. |

Historical `notes.md:290` and its copied `xmodel/codex-eval-20260812.md`
occurrences preserve the old LROOT wording and quarantined `(22)` ledger.
They are **HISTORICAL-ONLY**, already overridden by the 2026-08-28
supersession banners and the current 2026-08-29 overlays.  They are not live
policy or evidence.

## 5. Minimal campaign fixes

No numerical recomputation or new source datum is needed.  The smallest
consistent patch set is textual.

1. Add this standing type rule near the current top of `AUDIT.md`:

   ```text
   A decrease in a Puiseux-series count has two modes.  A distinct-place/
   direction-orbit split gives distinct later cv flags; conjugate shedding
   within one place gives one flag and a strict kappa jump.  No-remerging
   applies only to the first mode.
   ```

2. Treat the Fable td12 repair, not the producer's §2 sentence, as the proof
   of exact charge (8).  Qualify the level-25 endpoint as a possible
   distinct-place split only.
3. Treat the Opus td8 review, not the Sol Case B or Grok rereview, as the
   proof of the trunk floor (3).  Do not count Grok's sealed rereview as an
   independent correct reconstruction of the type distinction.
4. In LR2, derive unique (G) and (\kappa_G=1) first, then append the two
   bullets of §3.3.  All direct descendants can continue citing LR2.
5. Replace LROOT's “NO series leave” at line 224 by “no distinct
   place/direction-orbit exit; no new cv exit mass.”
6. Mark the four td8 artifacts in §4 as superseded for budget/census use;
   retain their explicitly per-ray descent and local coefficient results.

## 6. Downstream consequence audit

| downstream item | before audit | after audit |
|---|---|---|
| td8 affine equal-join family | killed by trunk exit arity | **unchanged: killed** |
| td8 trunk minimum | at least (3) | **unchanged**; proof authority is Opus repair |
| td12 U1 B-charge | exactly (8), not (9) | **unchanged** |
| td12 source gate | pure-power/constant-denominator levels (1\ldots24) | **unchanged**; endpoint conjugate split excluded |
| td6 LR2 x-side geometry | one flag, (\kappa=1), one unsplit cluster | **unchanged after two-mode proof completion** |
| td6 template, monodromy, classical, D73, centering, and two-chart controls | consume LR2 | **unchanged** |
| multipole first-exit inequality | distinct selected orbit witnesses | **unchanged and sound** |
| number of sound independent td8 hostile reconstructions of the key type step | recorded as two | **one as sealed (Opus); Grok needs repair** |
| JC2, any degree ceiling, source landing, or polynomial realization | not proved | **unchanged** |

No live engine output changes because none of the affected computations
encoded “one flag implies no conjugate shedding” as an arithmetic
constraint; the issue is in theorem consumption and proof prose.

## 7. Review risks

1. The denominator convention must be the post-characteristic convention
   of Notation 3.5.  This is independently checked in both the Opus td8 and
   Fable td12 reviews.
2. Endpoint equality matters: Definition 3.3 identifies two place rays at
   height equal to their contact.  Only a split strictly below a cv level
   forces two cv flags.
3. A conjugate split at the cv endpoint can still raise (\kappa_H), so
   “split allowed at the endpoint” must be qualified by split type.
4. LR2 uses that the x-side root denominator is (1).  This is the root
   normalization already consumed by its slope/budget proof.
5. The general first-exit packets are safe only at their written
   orbit-level scope.  A future series-level refinement must carry the
   denominator-jump term rather than duplicate cv flags.

## 8. Load-bearing hashes observed in this audit

```text
7cb5d4a8a3a4162a8a204facb79e68a9ef4f353275912d440170ae9898cd41f8  AUDIT.md
27a208c58af3eb192bff51b2dc8f58cb9f6efcbd22816f88de6c9d428595a05b  APPROACHES.md
3a6298d30a59b7a5ebf9416d1e178d6b1757553b54fa728b5f065b889ad5a9ec  PROGRESS.md

3c2c9a7ed79cc6d05ec3ba7098c1dc89cabb3547791d777c4bf8971d1ae28e39  xmodel/m2-td8-trunk-exact-charge-r1-sol56-20260829.md
d9db244079c521a2e3643c824b715adb4c934d843f9da18e9140c80d6758f012  xmodel/m2-td8-trunk-exact-charge-r1-hostile-review-opus5-20260829.md
a5c342e49aaa0ede12b857ed7742c6474737becabab0dcf7a10fbdedb26a8978  xmodel/m2-td8-trunk-exact-charge-r1-hostile-rereview-grok46-20260829.md

2a151eef1e661464ada47b0e387051733f9c2cb39cc7893366f5b1e09e15e829  xmodel/m2-td12-u1-next-trunk-discriminator-r1-sol56-20260829.md
3f214db8c12d022c2852dfadbbc268d105484343a8f6d4664765a08d3efcea03  xmodel/m2-td12-u1-next-trunk-discriminator-r1-hostile-review-fable5-20260829.md

0a1a649289dc48715b93c34df3c93337ab42a6fce5e923b4cd1dabd81239890c  ladder/SHEET6-LROOT.md
26b9bbf69a581885c62926cf0a8411463e70ea64f2c0e3b6f717f8a920eb4702  ladder/SHEET6-LT-REVIEW.md
850bc9687966e0f871753540532f803d8a69e84217d67d6ed4260be0c00c4273  ladder/SHEET6-TEMPLATE.md
a45ffd7577809c5e9ced861d10c6cd1d7c7e9286c6e257c3f4f0c2ced1acbd6c  ladder/GROK-MONODROMY.md
459bfe8e3e8e57cf554c019d8051475e74d1e8f44e23991f87ae4cbe26030a2e  ladder/SHEET6-CLASSICAL.md
ad63701bc1614dfd53edf99ade0e5c1743ceada3c9a9cdac38ef29a5e9701fe9  ladder/SHEET6-R1.md

f3e468f415fdd7bd1aa85962090d34a55bf6ff15d469c28373347cf1c7cc42ac  xmodel/td6-global-compatibility-review-grok-20260824.md
90546ffb50b5cf8325195dc04a4e39b550e4075c057049529e29d8d188b698de  xmodel/d73-strict-or-equality-20260824.md
3c0df2009432646bc6b93fa36f4c688b24af9e8df22629755303e89fde0fac3a  xmodel/d73-strict-or-equality-review-grok-20260824.md

2763d9708e25ff5f6f51754e678f0b5fd7f785a236d64e89eee4aa6189459933  xmodel/sigray-section9-source-audit-sol-ultra-20260828.md
9f4526f209366098f12bbe60387a190c6d2942a374c05fad092917bc79145f14  xmodel/sigray-multipole-selected-orbit-attachment-repair-gpt56-20260828.md
```

Superseded td8 consumer hashes:

```text
99b136da9930c76f833de66c437ffb7ef8b07ab017e0e6719fbb7c888c16e919  xmodel/m2-td8-equal-join-exact-lambda-primary-grok46-20260829.md
991e1b350ad2f8b2b82808fdc84dec71154f9ae17250c18953a36ac8f6588508  xmodel/m2-td8-first-extra-jet-exact-lambda-primary-opus5-20260829.md
ec3557953c6387ce35dcf4efe1df267fb828771119c479eb00c8f1793e0ee370  xmodel/m2-td8-first-extra-jet-exact-lambda-primary-hostile-review-fable5-20260829.md
93c58d63af6ff9e000531c077b10c86ef1a9d4d6f54b6b343d1f98c7d6183ecd  xmodel/m2-td8-cv-weight-contact-gate-primary-grok46-20260829.md
34bd7b357166d6a6860bf7714ffd2c5a3343eee361fabc234a927580673e836d  xmodel/m2-td8-cv-weight-contact-gate-hostile-review-fable5-20260829.md
```

## Seal

Body SHA-256 (all bytes before this `## Seal` heading): `300a0efff1960a15335c2e61a8f42bcd2d9ea27dab99b4694480f0fa572b9444`
