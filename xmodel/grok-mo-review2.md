# Hostile re-review — external-comms tier, round 2

**Target:** `phase0-mo-answer-draft.md` v2 (2026-08-18 rewrite).
**Round 1:** `xmodel/grok-mo-review.md` (FAIL, 12 defects).
**Sources:** `AUDIT.md`, `REDUCTION.md`, `paper1/main.tex`; also `BOOK-TD12.md`, `CROSSCHECK.md`, `SHEET6-CAMPAIGN.md`, `dist/ZENODO-METADATA.md`, `dist/ZENODO-METADATA-BUNDLE.md`. DOIs and the live thread re-checked against Zenodo records and the Stack Exchange API (2026-08-18).
**Git:** none. No other file modified.

## Verdict

**FAIL.** Do not post as written. The round-1 rewrite did what it was asked to do at the sentence level: defects 1–5 and 7, 9–12 are gone, and 6 and 8 are mostly gone. The remaining problems are narrower, and two of them were introduced by the rewrite. A commenter who clicks the only live Posch DOI, or who quotes the “collective record” / “enumerated books” sentences, still has a clean shot.

Posting bar: kill N1–N3 below. N4 is fill-or-cut, not a wording rewrite. N5 can ride in the same pass.

---

## Round-1 scorecard (the 12)

| # | Round-1 defect | v2 status | Evidence |
|---|---|---|---|
| 1 | Closing “every finite window… empty, independently replicated, machine-checked” | **Fixed** | Sentence deleted. Replacement names the unfinished \(d=6\) residue cell, larger composite residue panels, and unclosed composite single-pole / general off-axis sectors. Matches the suggested fix in substance. |
| 2 | Strinz in the “elimination of both supports, hence the bound 125” list | **Fixed** | Helali / Suzuki / Ishihara only for the replicated exclusion. Strinz is a parallel program; live abstract still says “The target claim C0 (case closure) remains OPEN” (`10.5281/zenodo.21633408`, fetched 2026-08-18). |
| 3 | “The 14-cell \(d=12\) book closes” | **Fixed** | Now “a 14-cell type-(3,5) book at \(d=12\) is empty on its enumerated list at the same conditional tier.” Matches `BOOK-TD12.md` (14 cells, poles \(2\times(6,1,2,5)\), list-relative, seven fail-closed classes). The parked \(u=1\) residual is inside that fail-closed parking, not silently closed. |
| 4 | “The live open front is \(d=6\)”, residue A as *the* remaining obstruction | **Fixed** | Uses the suggested sentence: smallest unfinished on-axis two-pole cell at \(d=6\); same residue in larger composite panels; composite single-pole and general off-axis not closed. Matches `REDUCTION.md` HIGH 1–2. |
| 5 | \(d\le 5\) book “recovers” Orevkov / Domrina–Orevkov / Żołądek / Sigray in machine-checked form | **Fixed** | “zero survivors, consistent with… (Orevkov; Domrina and Orevkov; Żołądek, Thm 6.12); we do not rely on Sigray’s Thm 9.1.” Matches `SHEET6-CAMPAIGN.md` (`td<=5: 0`) and `REDUCTION.md` T5. |
| 6 | `21894922` scoped as if it archived the whole answer; `[BUNDLE-DOI]` | **Mostly fixed; residuals N2, N4** | Archive claims are split: vertex-gap note → `21894922`; ladder → “theory bundle below.” The Helali/Suzuki replay clause was then glued back onto `21894922` (N2). `[BUNDLE-DOI]` is still in the body (N4). |
| 7 | Prior art on the \(AC'-\nu A'C\) lemma omitted | **Fixed** | Żołądek 2008, Appendix A.7; \(\nu=1\) in Hermoso–Alcázar, arXiv:2410.18867; novelty restricted to the vertex-gap / \(R_{k,d_2}\) package. Matches `paper1/main.tex` abstract + the prior-art paragraph after Thm 6.5 / `thm:ode`. |
| 8 | Leox folded into “the collective record” the bound belongs to | **Mostly fixed; residual N1** | Leox is now “reports… which I have not checked.” The next sentence still says “The bound belongs to that collective record.” |
| 9 | Procesi’s AI question treated as about this work | **Fixed** | “Since the role of AI has been asked about on this page.” Procesi (a/513656) still asks about the dimension-three example; the pointing no longer hijacks that question. |
| 10 | Degree-pair order flip; transpose dropped | **Fixed** | Single convention: \((72,108)\) up to order. Matches ratto3423 and `REDUCTION.md` T3. |
| 11 | \(d=7\) 17-cell line understated the perimeter | **Fixed** | “all 17 cells of the enumerated off-axis book die under a uniform tower theorem, relative to the filed route perimeter.” Matches `AUDIT.md` TD-7 panel closure and `REDUCTION.md` T9(c). |
| 12 | Checklist still scheduled Helali/Suzuki coordination emails | **Fixed** | Item 5: “Helali coordination email struck per 2026-08-18 decision.” |

Style checks from round 1 still hold: no em dashes; \(\mathrm{JC}_2\) / MathJax; answer body ~613 words (under the ~650 cap).

---

## Remaining / new defects

Ordered by how badly they fail on this thread. Severity: **critical** / **high** / **medium** / **low**.

### N1. “The bound belongs to that collective record” still follows Strinz and Leox
- **Severity:** medium (record inflation; residual of defect 8)
- **Where:** credit paragraph, last sentence.
- **What’s wrong:** The rewrite correctly split Helali/Suzuki/Ishihara from Strinz and Leox. It then kept the original overclaim sentence immediately after the mixed clause. “That collective record” will be read as the whole preceding list, which now includes a DOI whose abstract marks C0 OPEN and a comment the author says he has not checked. That is the same inflation defect 8 asked to kill, one sentence later.
  - Live Strinz abstract (`10.5281/zenodo.21633408`): “The target claim C0 (case closure) remains OPEN.”
  - Live Leox comment (on a/513493, score 2): independent computer-assisted elimination, no artifact. Still unchecked, as the draft now says.
- **Suggested fix:** Delete the sentence. If a closer is needed, put it *before* Strinz/Leox: “Helali, Suzuki, and Ishihara are the public replicated record for that elimination.” Do not let “the bound belongs to…” quantify over Strinz or Leox.

### N2. Helali and Suzuki replays glued to `21894922`
- **Severity:** medium (archive-scope; introduced by the rewrite; residual of defect 6)
- **Where:** numbered item 1, first sentence.
- **What’s wrong:** “A note on the minimal cell, archived with re-runnable exact-arithmetic verification at [21894922], cross-checked by exact replays of the Helali and Suzuki artifacts.” Both participles modify the note. A commenter who clicks the only live Posch DOI will not find those replays.
  - Live `21894922` abstract (fetched 2026-08-18): the artifact is the vertex-gap / \(R_{k,d_2}\) certificate bundle; “The msolve Groebner-basis discard of the remaining (72,108) strata … is a separate computation and is not part of this artifact.” File is 258.3 kB. Helali’s replay alone is ~90 MB.
  - `CROSSCHECK.md` does record exact Helali and Suzuki replays (Helali PASS; Suzuki full regen byte-identical). Those live in the campaign repo, not at `21894922`. `paper1/main.tex` already says this: Helali and Suzuki “replayed exactly in the campaign repository.”
  - Helali/Suzuki are computational exclusions of *both* Prop. 4.3 supports. They do not cross-check the vertex-gap theorem. Attaching them to the note is the wrong object, at the wrong DOI.
- **Suggested fix:** Keep `21894922` for the note and its exact-arithmetic scripts only. Move the replay clause to the credit paragraph, as a first-person claim that is true: “I have replayed Helali and Suzuki exactly.” Point those replays at the theory-bundle DOI once it is live, or omit the pointer.

### N3. “They kill every configuration in the enumerated books”
- **Severity:** medium (internal contradiction; introduced by the rewrite)
- **Where:** book-relative paragraph, first two sentences.
- **What’s wrong:** `REDUCTION.md` HIGH 2 still has modeled on-axis survivors at \(d=6,8,9,10,12,14\) (23 cells; the \(d=6\) cell is the residue-A two-pole the next sentence calls unfinished). `BOOK-ENUM.md` enumerated those books. HIGH 1 still has surviving composite single-pole search classes at every composite \(d\) in the table. So “every configuration in the enumerated books” is false if “enumerated” means what it means in the ledgers.
  - The intended reading is the `AUDIT.md` 2026-08-17 slogan: promoted ladder results are book-relative, i.e. the *completed* books named in item 2 die at the tiers stated. That slogan does not travel. Item 2 just used “enumerated” for the \(d\le 5\) book, the \(d=7\) off-axis book, and the \(d=12\) list. The next paragraph then universalizes it.
  - Two sentences later the draft correctly says the \(d=6\) on-axis two-pole cell is unfinished. Those cannot both be true under the ledger reading of “enumerated books.” This is a smaller version of defect 1’s self-contradiction, not a return of “every window is empty.”
- **Suggested fix:** “They kill every configuration in the completed books named above, at the tiers stated.” Keep the landing-gap and unfinished-cell sentences.

### N4. `[BUNDLE-DOI]` is still in the answer body; no theory-bundle record exists
- **Severity:** high as a posting blocker; not a mathematical rewrite of items 1–2
- **Where:** closer; item 2 (“archived in the theory bundle below”).
- **What’s wrong:** Defect 6’s instruction was: ladder only if the theory-bundle DOI is live; never post `[BUNDLE-DOI]` literally. v2 split the claims and left the placeholder, with checklist item 1 to fill it. That is acceptable as a draft process. It is not acceptable as a post.
  - Zenodo search on 2026-08-18 finds no public “sheet-number / theory bundle” record for this campaign. `dist/ZENODO-METADATA-BUNDLE.md` is still suggested metadata, not a minted DOI.
  - Item 2’s “Each promoted statement ships with an executable gate suite” is true locally (`AUDIT.md`: td-7 `tower_check.py` 1559/1559; `td11_census.py` 8/8; `BOOK-TD12.md`: `cases/td12_book.py` 14 checks). It is a dangling claim until the bundle DOI resolves and actually contains those suites.
- **Suggested fix:** Do not post until a resolving theory-bundle DOI is pasted over the placeholder *and* clicked. If the DOI is not live on posting day, cut item 2 down to a one-line “write-ups in preparation” or drop the ladder from this answer. Confirm `10.5281/zenodo.21894922` still resolves that day (it does today).

### N5. “Made effective with Horruitiner in arXiv:2204.14178”
- **Severity:** low (citation compression)
- **Where:** credit paragraph, first sentence.
- **What’s wrong:** `paper1/main.tex` intro separates the two Horruitiner papers: the program is “made algorithmic in [GGV4]” (arXiv:1708.07936), and “with Horruitiner they raised the degree bound from 100 to 108 [GGHV]” (arXiv:2204.14178). The 108 / below-125 / Prop. 4.3 facts that follow *are* from 2204.14178. Only “made effective … in 2204.14178” attaches the wrong paper.
- **Suggested fix:** Drop “made effective.” “The baseline is the Newton-polygon program of Guccione, Guccione and Valqui, raised with Horruitiner in [arXiv:2204.14178] to \(\max(\deg P,\deg Q)\ge 108\)…” is enough.

---

## Optional, not required for PASS

- **Sigray 9.1 “we found incomplete.”** True (`REDUCTION.md` T5). Stronger than the round-1 suggested clause, and it has no pointer. A Sigray reader will ask where. Point at the theory bundle, or drop back to “we do not rely on Sigray’s Thm 9.1.”
- **Parenthetical gap list.** “the gaps are named in the write-ups (no transport theorem …, no upper bound on \(d\))” names G2 and G5. `REDUCTION.md` also has G1 (existential vs normalization) and no universal book-landing even after transport. The unfinished-cell sentence covers the operational remainder. Optional: “among others.”
- **Bundle-abstract hygiene, posting day.** `dist/ZENODO-METADATA-BUNDLE.md` currently writes a “\(td=6\) funnel to the unique two-pole residue-A template” and a nonempty depth-21 fiber. That is consistent with the draft if read carefully, and more detailed than MO needs. Do not let the public Zenodo abstract of `[BUNDLE-DOI]` say anything the MO hedges just walked back.

---

## What still holds (do not “fix” these)

- Opening refusal to treat any of this as evidence for \(\mathrm{JC}_2\).
- Prop. 4.3 conditionality and “supporting chain partly arXiv-only.” Still right: Prop. 4.3 lives in arXiv:2204.14178; GGV1 is published; a 2026-07-28 journal successor of GGV2 exists and has not been diffed (`REDUCTION.md` T3 / source table). More honest than ratto3423’s unconditional \(\ge 125\).
- Helali first, 21 July, `10.5281/zenodo.21479814` (live: excludes both transcribed systems; bound still conditional on the reduction). Suzuki `21483636` (live: excludes both alternatives). Ishihara `21757679` (live: independent exact-computational route for both systems; unreplayed by this campaign, as `paper1` already says).
- Strinz held at his own C0-OPEN abstract. Correct, and *more* honest than `paper1`’s “subsequent independent replications by Strinz and Ishihara.”
- Vertex-gap + \(R_{k,d_2}\) as a char-0 depth-two description of every strip cell \(k,d_2\ge 2\); generic-chart Gröbner replaced by a proof. Matches `paper1` abstract / Thm R.
- \(d=11\): conditional emptiness over an audited 411-row quotient, named fail-closed classes. Matches `AUDIT.md` 2026-08-15.
- Book-relative landing gap: no GGV\(\to\)sheet transport, no upper bound on \(d\), none of this proves \(\mathrm{JC}_2\). Matches `REDUCTION.md` executive verdict and G2/G5.
- Thread facts, re-checked 2026-08-18: Q513413 title; four answers; ratto3423 = a/513493 still states \(\ge 125\) with “Write-up in preparation”; last activity 2026-07-27 (Procesi edit); Leox comment still on a/513493; Procesi a/513656 still has tame \(\mathrm{Aut}(\mathbb{A}^2)\) and McKay–Wang, JPAA 40 (1986). Checklist item 2 remains right.
- AI disclosure and “I take responsibility for every claim.”

## Checks that passed

| Claim | Result |
|---|---|
| Q513413 title / a/513493 / a/513656 / Leox comment | Pass (SE API, 2026-08-18) |
| GGHV arXiv:2204.14178; \(\max\ge 108\); below 125 one family; Prop. 4.3 \(\to\) two supports, \([P,Q]=x^2\) | Pass |
| Helali 21479814, 21 Jul 2026, both supports | Pass (live abstract) |
| Suzuki 21483636, both supports | Pass (live abstract) |
| Ishihara 21757679 | Pass as a replication artifact; still unreplayed here |
| Strinz 21633408, C0 OPEN | Pass (live abstract, exact words) |
| Posch 21894922 resolves; msolve discard not in artifact | Pass (live abstract; see N2) |
| Lemma + Żołądek A.7 + Hermoso–Alcázar | Pass vs `paper1` |
| \(d\le 5\) book 0 survivors | Pass (`SHEET6-CAMPAIGN.md`) |
| 17 cells at \(d=7\), filed route perimeter | Pass |
| 411-row \(d=11\) certificate, fail-closed | Pass |
| 14-cell type-(3,5) at \(d=12\), list-relative | Pass (`BOOK-TD12.md`) |
| HIGH 1–2 open sectors named | Pass |
| McKay–Wang / tame \(\mathrm{Aut}(\mathbb{A}^2)\) | Pass (Procesi) |
| No em dashes; word count ~613 | Pass |
| Theory-bundle DOI public | Fail (see N4) |

## Posting bar

Rewrite until N1–N3 are gone. Fill or cut N4 before any post; do not ship `[BUNDLE-DOI]`. N5 can ride in the same pass. Re-check the thread immediately before posting (still quiet since the 27–28 Jul window). A v3 that only does those edits, and that is posted against a resolving bundle DOI whose abstract does not outrun this text, should pass a round-3 check.
