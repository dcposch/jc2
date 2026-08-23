# Hostile review — external-comms tier

**Target:** `phase0-mo-answer-draft.md` (MathOverflow answer for Dan Posch, Q513413).
**Sources:** `AUDIT.md`, `paper1/main.tex`, `REDUCTION.md`; DOIs and the live thread checked against Zenodo records and the Stack Exchange API (2026-08-18).
**Git:** none. No other file modified.

## Verdict

**FAIL.** Do not post as written. The book-relative hedge in paragraph 4 is the right voice and should be kept; it does not save the earlier ladder sentences or the closing “every window is empty” line. Several claims are false, or will be read as false, by a commenter who only has the public artifacts and the thread.

Defects below are ordered by how badly they fail on this thread. Severity: **critical** / **high** / **medium** / **low**.

---

## Defects

### 1. Closing sentence: “every finite window examined so far is empty, in independently replicated, machine-checked form”
- **Severity:** critical
- **Where:** last sentence of the mathematical body, before the Zenodo/AI closer.
- **What’s wrong:** This is the sentence a hostile commenter will quote. It is false on the draft’s own terms and false against the ledgers.
  - Two sentences earlier the draft says the live front is residue A with a computation still in progress. Those cannot both be true.
  - `REDUCTION.md` HIGH 1–2: composite single-pole classes survive at every composite \(d\) in the table (4 at \(d=6\), then 16/16/23/71/48/…); modeled on-axis survivors remain at \(d=6,8,9,10,12,14\), all carrying residue A. Those are examined windows that are not empty.
  - `notes.md` / `SHEET6-DIRECTIONB.md` / the 2026-08-17 CORE2 run: the residue-A depth-21 fiber is **nonempty** at three primes (397-element Gröbner basis). A window that was examined and is not empty is already on disk.
  - “Independently replicated” is true of the (72,108) computational exclusion (Helali, Suzuki, and Ishihara). It is not true of the sheet ladder. Dual-model adversarial review is not an independent mathematical replication. Conflating the two is exactly the overclaim this thread will punish.
- **Suggested fix:** Delete the sentence. Replace with something no stronger than: the GGV supports below 125, and the completed books named above, are empty at the tiers stated; several examined windows (residue A, composite single-pole, other composite on-axis panels) are not decided.

### 2. Strinz listed as part of the public elimination of both supports
- **Severity:** high (factual / attribution)
- **Where:** credit paragraph, the Helali–Suzuki–Strinz–Ishihara list.
- **What’s wrong:** Helali (`10.5281/zenodo.21479814`, 21 Jul 2026) and Suzuki (`21483636`, 22 Jul 2026) do exclude both Prop. 4.3 supports; Ishihara (`21757679`) is a later exact-computational replication. Strinz (`21633408`, v1.0.0, 28 Jul 2026) does **not** sit at that tier. The current Zenodo abstract says, in those words, “The target claim C0 (case closure) remains OPEN.” The campaign’s own 17 Aug sweep already recorded the discrepancy: internal registry `closed: true` at self-assessed **“claimed”** evidence, below `exact-checked`, with five “zero margin” inputs. `paper1/main.tex` already treats Strinz/Ishihara as unreplayed. Putting Strinz in the same “elimination of both supports, hence the bound 125” list as Helali is a claim Strinz himself did not make at this DOI. He, or anyone who clicks the link, will say so.
- **Suggested fix:** Helali (first), Suzuki, Ishihara for the replicated exclusion. Mention Strinz only as a parallel audited program, at his own “claimed / C0 OPEN” tier, or drop him from this sentence. Do not write “hence the bound 125” over a four-name list that includes a record whose abstract says the case is open.

### 3. “The 14-cell \(d=12\) book closes at the same conditional tier”
- **Severity:** high (tier-inflation / underspecification)
- **Where:** numbered item 2, after the \(d=11\) certificate.
- **What’s wrong:** There is a 14-cell object, and `BOOK-TD12.md` does promote it as list-relative tower-dead, conditional on seven fail-closed classes. It is the **type-(3,5) off-axis entry book** (poles \(2\times(6,1,2,5)\)), not “the \(d=12\) book.” `REDUCTION.md` HIGH 2 still has **12** modeled on-axis survivors at \(d=12\); TDU still has **71** single-pole survivor classes at \(d=12\). Parallel construction with “the \(d\le 5\) book closes” and “at \(d=7\), all 17 cells close” invites the reading that \(d=12\) is closed. `BOOK-TD12.md` also parks a load-bearing unrefused \(u=1\) residual (gap \(1/3\)); “closes” overstates even that special book.
- **Suggested fix:** “A 14-cell type-(3,5) book at \(d=12\) is empty on its enumerated list, at the same fail-closed-conditional tier as the \(d=11\) certificate.” Do not let the sentence be readable as a \(d=12\) exclusion.

### 4. “The live open front is \(d=6\), where the remaining obstruction is a residue condition (residue A)”
- **Severity:** high (overclaim)
- **Where:** paragraph after the book-relative hedge.
- **What’s wrong:** Residue A on the on-axis two-pole template is *a* live obstruction at \(d=6\), and it is the campaign’s current compute target. It is not the remaining obstruction at \(d=6\), and \(d=6\) is not the live front.
  - `REDUCTION.md` HIGH 1 and `SHEET6-TDUNIFORM.md`: \(d=6\) still has **4** surviving single-pole search classes.
  - `REDUCTION.md` HIGH 2: residue A also survives at \(d=8,9,10,12,14\) (23 modeled on-axis cells, 22 of them at composite \(d>6\)).
  - Same ledger: composite single-pole, generic off-axis, \(d=11\) FC1–FC7, and \(d=13\) are open; there is no upper bound on \(d\).
- **Suggested fix:** “The smallest unfinished on-axis two-pole cell is at \(d=6\), a residue condition (residue A) on a depth ladder; a computation aimed at the current subcase is in progress. The same residue survives in several larger composite panels, and the composite single-pole and general off-axis sectors are not closed.”

### 5. “The \(d\le 5\) book closes with zero survivors, recovering the low-sheet exclusions (Orevkov, Domrina and Orevkov, Żołądek, Sigray) in machine-checked form”
- **Severity:** high (tier-inflation / false recovery claim)
- **Where:** numbered item 2, first ladder sentence.
- **What’s wrong:** The enumerated \(d\le 5\) book in Sigray’s frame has 0 survivors (`SHEET6-CAMPAIGN.md`). That is a book-relative emptiness result. It is not a machine-checked recovery of the published proofs.
  - `REDUCTION.md` T5: the clean published \(d\ge 6\) theorem is Żołądek, Topology 47 (2008), Thm 6.12. Sigray’s Thm 9.1 is **not used**; the campaign found the printed §9 elimination incomplete.
  - `SHEET6-CAMPAIGN.md` G3 (the campaign’s own words): Sigray’s \(td\ge 6\) proof is incomplete as printed; “independent reproof needs qualification.”
  - Nobody machine-checked Orevkov 1987, Domrina–Orevkov 1998, or Żołądek 2008. Those are different formalisms (splice diagrams; Newton–Puiseux charts). A book with zero rows in a repaired Sigray frame is consistent with those theorems; it does not recover them.
  - Naming Sigray in the recovery list is the worst of the four: it cites an incomplete thesis proof as if it had been formalized.
- **Suggested fix:** “The enumerated \(d\le 5\) book in Sigray’s frame has zero survivors, consistent with the published low-sheet exclusions (Orevkov; Domrina–Orevkov; Żołądek, Thm 6.12). We do not rely on Sigray’s Thm 9.1.” Drop “in machine-checked form” for other people’s theorems.

### 6. “Mine is now archived” vs what 21894922 actually contains
- **Severity:** medium
- **Where:** opening sentence; numbered item 1 (DOI `10.5281/zenodo.21894922`); closer (`[BUNDLE-DOI]`).
- **What’s wrong:** `10.5281/zenodo.21894922` resolves (Posch, 11 Aug 2026, paper-1 artifact). Its own abstract says the msolve discard of the remaining (72,108) strata is **not** in the bundle, and the sheet ladder is not in it either. The opening “mine is now archived” is true of the vertex-gap note and false of half the answer. The ladder is pointed at a placeholder. GitHub `dcposch/jc72108` is still 404. A commenter who clicks the only real DOI and then asks for the \(d=7/11/12\) gate suites will find none.
- **Suggested fix:** Split the archive claims. Vertex-gap note: 21894922 (confirm it still resolves on posting day). Ladder: only if the theory-bundle DOI is live; otherwise cut item 2 down to a one-line “write-ups in preparation” or do not mention the ladder on MO yet. Never post `[BUNDLE-DOI]` literally.

### 7. Prior art on the “elementary lemma” omitted
- **Severity:** medium (attribution)
- **Where:** numbered item 1, the \(AC'-\nu A'C\) lemma.
- **What’s wrong:** The statement matches `paper1/main.tex` Thm 6.5 / the abstract. The same paper, v4, already records prior art: Żołądek 2008, Appendix A.7 (via the same ODE, Lem. 3.9 / (3.14)), and Hermoso–Alcázar arXiv:2410.18867 for \(\nu=1\). This thread already cites degree bounds from that literature (KConrad; Moh in the comments). “An elementary lemma,” with no pointer, on a Jacobian thread where Żołądek is the published \(d\le 5\) source, will be read as a novelty claim. Combined with defect 5 it is worse: recover Żołądek in machine-checked form, then restate his lemma as the engine.
- **Suggested fix:** One clause: the rigidity input is the polynomial ODE lemma (also in Żołądek, App. A.7; \(\nu=1\) in Hermoso–Alcázar); the new content is the vertex-gap / \(R_{k,d_2}\) package.

### 8. Leox’s comment treated as a replication in “the collective record”
- **Severity:** medium
- **Where:** “plus the independent elimination reported in the comments here. The bound belongs to that collective record.”
- **What’s wrong:** The comment exists (Leox on a/513493, score 2): independent computer-assisted elimination of both Prop. 4.3 supports, “exact certificate based on weighted transport equations and finite-field Macaulay rank computations.” That method description is Suzuki’s method (weighted Macaulay minor, \(\det=21\bmod 23\); Bézout on the smaller support). There is no Leox artifact. Folding an unreproduced comment into the record the bound “belongs to,” next to four DOIs, is record inflation. If Leox is Suzuki, it is double-counting; if not, it is an unchecked third-party claim.
- **Suggested fix:** “Leox reports a further independent elimination in the comments on ratto3423’s answer; I have not checked it.” Do not put it in the same clause as Helali/Suzuki/Ishihara.

### 9. Procesi’s AI question is about Alpoge’s \(\mathbb{C}^3\) example, not this work
- **Severity:** medium (thread hygiene)
- **Where:** closer, “Since another answer asks about the role of AI.”
- **What’s wrong:** Procesi (a/513656) asks what role AI played in discovering the dimension-three counterexample. The draft answers as if the question were about the plane-case campaign. The disclosure itself is right and should stay (the meta-thread Q514380 is live). The pointing is wrong.
- **Suggested fix:** “Since the role of AI has been asked about on this page: the work below was produced in close collaboration with Claude, with GPT and Grok as adversarial reviewers, and I take responsibility for every claim.”

### 10. Degree-pair order flip; transpose dropped
- **Severity:** low
- **Where:** credit paragraph: \((\deg P,\deg Q)=(108,72)\), then “Everything at \((72,108)\).”
- **What’s wrong:** `paper1/main.tex` and `CROSSCHECK.md` use \((\deg P,\deg Q)=(108,72)\) for \(A_0=(8,28)\), \((m,n)=(3,2)\). ratto3423, Helali, Suzuki, and `REDUCTION.md` T3 write \((72,108)\) “or its transpose” / “up to interchange.” Both orders in one paragraph, with the transpose omitted, is a gift. Not a mathematical error if the family is unordered, but it looks careless on a thread whose other computational answer uses \((72,108)\).
- **Suggested fix:** One convention, matching ratto3423: the pair \(\{72,108\}\), or “\((72,108)\) up to order.”

### 11. \(d=7\) “all 17 enumerated cells close” is the one ladder line that is close to honest
- **Severity:** low (perimeter understated, not false)
- **Where:** numbered item 2.
- **What’s wrong:** Count 17 is right (`AUDIT.md` TD-7 panel closure; `TOWER-UNIFORM.md`). Prime \(d\) kills single-pole and empties the on-axis multi-pole panel, so those 17 cells *are* the remaining \(d=7\) book. `REDUCTION.md` T9(c) still has the theorem **conditional on the filed route/classification perimeter**. The later book-relative paragraph covers this if a careful reader continues. A quoted excerpt of sentence 2 alone does not.
- **Suggested fix:** “At \(d=7\), all 17 cells of the enumerated off-axis book die under the uniform tower theorem, relative to the filed route perimeter.” Optional; the book-relative paragraph may be enough if defects 3–5 are fixed.

### 12. Pre-post checklist still schedules Helali/Suzuki coordination emails
- **Severity:** low (process; not in the answer body)
- **Where:** checklist item 5.
- **What’s wrong:** `notes.md` / `phase0-email-draft.md` (18 Aug): Helali dedicated send **dropped**. Item 5 still sequences “Helali/Suzuki coordination emails referencing the posted answer.” Internal contradiction, not a public-math defect.
- **Suggested fix:** Strike Helali from the send sequence. Suzuki remains a maybe via Zenodo comment, not an email.

---

## What to keep

These are accurate against the three sources and should survive a rewrite:

- Opening refusal to treat any of this as evidence for \(\mathrm{JC}_2\).
- Prop. 4.3 conditionality and “supporting chain partly arXiv-only” (`AUDIT.md` claim 8; `REDUCTION.md` T3; `paper1` §computation). This is *more* honest than ratto3423’s unconditional \(\ge 125\).
- Helali first, 21 July, DOI `10.5281/zenodo.21479814`. Suzuki `21483636`, Ishihara `21757679`. Those three DOIs resolve as claimed.
- Vertex-gap + \(R_{k,d_2}\) as a depth-two char-0 description of every strip cell \(k,d_2\ge 2\); generic-chart Gröbner replaced by a proof. Matches `paper1` abstract / Thm R / Thm 22.
- Helali and Suzuki exact replays (`CROSSCHECK.md`: Helali 71 s PASS; Suzuki full regen 21.5 s, byte-identical). Do not extend this to Strinz/Ishihara (`paper1` already says those are unreplayed).
- \(d=11\): conditional emptiness over an audited 411-row quotient, conditional on named fail-closed classes. Matches `AUDIT.md` 2026-08-15 entry.
- Book-relative paragraph: no GGV\(\to\)sheet transport, no upper bound on \(d\), none of this proves \(\mathrm{JC}_2\). Matches `REDUCTION.md` executive verdict and G2/G5.
- Thread facts: title of Q513413; ratto3423 = a/513493, “write-up in preparation”; tame generation of \(\mathrm{Aut}(\mathbb{A}^2)\) and McKay–Wang inversion (Procesi, a/513656, citing McKay–Wang, JPAA 40 (1986)).
- AI disclosure and “I take responsibility for every claim.” Keep, with defect 9’s pointing fix.

## Checks that passed

| Claim | Result |
|---|---|
| Q513413 title / a/513493 exists | Pass |
| GGHV arXiv:2204.14178; \(\max\ge 108\); below 125 one family; Prop. 4.3 \(\to\) two supports, \([P,Q]=x^2\) | Pass (community baseline; conditionality correctly attached to the (72,108) step) |
| Helali 21479814, 21 Jul 2026, both supports | Pass |
| Suzuki 21483636, both supports | Pass |
| Ishihara 21757679 | Pass (replication artifact) |
| Posch 21894922 resolves | Pass (scope narrower than the answer; see defect 6) |
| Lemma statement vs `paper1` | Pass (prior art omitted; see defect 7) |
| 17 cells at \(d=7\) | Pass (perimeter: defect 11) |
| 411-row \(d=11\) certificate, fail-closed | Pass |
| McKay–Wang / tame \(\mathrm{Aut}(\mathbb{A}^2)\) | Pass (Procesi) |
| No em dashes; \(\mathrm{JC}_2\) / MathJax | Pass (style; not re-counted) |

## Posting bar

Rewrite until defects 1–5 are gone. Defects 6–9 should be gone before a public post; 10–12 can ride in the same pass. Re-check the thread immediately before posting (checklist item 2 still right: last activity on the question is still the 28 Jul window). Do not post with `[BUNDLE-DOI]` in the body.
