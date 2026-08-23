# Hostile re-review — external-comms tier, round 3

**Targets.** (A) `phase0-mo-answer-draft.md` v3. (B) `dist/jc72108-theory-bundle-v1/SUMMARY.tex` as rebuilt, plus `dist/ZENODO-METADATA-BUNDLE.md`.
**Prior verdicts.** A: `xmodel/grok-mo-review2.md` (FAIL; posting bar N1–N3, N5 can ride, N4 fill-or-cut). B: `xmodel/grok-bundle-review.md` (FAIL; eight defects, minimum ship bar 1–5, 6–8 can ride).
**Sources.** `AUDIT.md`, `REDUCTION.md`, `BOOK-TD12.md`, `CROSSCHECK.md`, `TOWER-UNIFORM.md`, `notes.md`; pointed corroboration in `paper1/main.tex`, `MATHIEU.md`, `xmodel/grok-transport-review.md`. Live DOIs, GitHub, and the MO thread re-checked 2026-08-18. Tarball `dist/jc72108-theory-bundle-v1.tar.gz` byte-compared to the unpacked tree.
**Git:** none. No other file modified.

## Verdicts

| Target | Verdict | Why |
|---|---|---|
| (A) MO draft v3 | **PASS** (text). Do not post until N4 is filled or cut. | N1–N3 and N5 are actually gone. No new text defect from the v3 edits. `[BUNDLE-DOI]` remains a posting-day process item, as commissioned. |
| (B) SUMMARY + bundle metadata | **FAIL.** Do not paste the current Zenodo description. | All eight SUMMARY defects landed, including the `AUDIT.md` td-12 ledger line. The metadata abstract then undoes the G2 hedge the MO draft and SUMMARY just restored. |

---

## Target A — `phase0-mo-answer-draft.md` v3

**PASS** as a MathOverflow answer body. The v3 pass did the four requested edits and the two optional tightenings, and it did not reintroduce a round-1 or round-2 claim. A commenter who clicks the only live Posch DOI, or who quotes the credit paragraph or the book-relative paragraph, no longer has the clean shots N1–N3 gave them.

### Round-2 residual scorecard

| # | Round-2 residual | v3 status | Evidence |
|---|---|---|---|
| N1 | “The bound belongs to that collective record” after Strinz and Leox | **Killed** | Sentence deleted. Credit paragraph now ends: Helali / Suzuki / Ishihara “are the public replicated record for that elimination”; then a separate clause for Strinz (parallel program, own abstract marks case closure open) and Leox (“which I have not checked”). “Collective record” / “bound belongs” are absent. |
| N2 | Helali/Suzuki replays glued to `21894922` | **Killed** | Item 1 is the note and its exact-arithmetic scripts only. Replay moved to the credit paragraph as a first-person claim: “I have replayed the Helali and Suzuki artifacts exactly.” That claim is true (`CROSSCHECK.md`: Helali FULL PASS, 71 s; Suzuki full regen, 21.5 s). It is no longer a participle on the note. Live `21894922` abstract (fetched 2026-08-18) still says the msolve discard “is a separate computation and is not part of this artifact.” |
| N3 | “They kill every configuration in the enumerated books” | **Killed** | Exact suggested wording: “They kill every configuration in the completed books named above, at the tiers stated.” The unfinished \(d=6\) cell, the same residue in larger composite panels, and the open composite single-pole / general off-axis sectors stay in the next sentence. No self-contradiction under the ledger reading of “enumerated.” |
| N4 | `[BUNDLE-DOI]` still in the body; no public theory-bundle record | **Process, not a text defect** | Still in the closer; checklist item 1 is fill-or-cut. Zenodo search 2026-08-18 still finds no public sheet-number / theory-bundle record. Do not post the placeholder. |
| N5 | “Made effective with Horruitiner in arXiv:2204.14178” | **Killed** | Now “raised with Horruitiner in [arXiv:2204.14178] to \(\max(\deg P,\deg Q)\ge 108\).” Matches the suggested sentence. The 108 / below-125 / Prop. 4.3 facts remain from that paper. |

Optional items from round 2 also landed: “among others” on the gap list; Sigray 9.1 kept as “we do not rely,” not “we found incomplete” with no pointer.

### New-defect hunt (v3 edits)

Read the whole answer body against `AUDIT.md`, `REDUCTION.md` HIGH 1–2, `BOOK-TD12.md`, `CROSSCHECK.md`, live Zenodo, and the SE API. Checked for reintroduced round-1 defects 1–5 and 7, 9–12, and for anything the N1–N3/N5 rewrites newly broke.

Nothing new at critical / high / medium.

- Replay is now attached to the *elimination*, which is the right object. It is not attached to the vertex-gap note. No DOI is claimed for the replay (round 2 allowed “omit the pointer”).
- “These three are the public replicated record” plus “I have replayed Helali and Suzuki” does *not* imply an Ishihara replay. Ishihara stays at the same unreplayed-here tier `paper1` already uses.
- “Completed books named above” covers the \(d\le 5\) book, the \(d=7\) off-axis book, and the 14-cell type-(3,5) list. The \(d=11\) object is a conditional certificate, not called a book, so the slogan does not swallow the 411-row wall. The \(u=1\) residual at \(d=12\) is a list-completeness parking, not a surviving configuration; “at the tiers stated” already carries list-relative / fail-closed.
- Word count 619 (whitespace-split answer body), under the ~650 cap. Zero em dashes. \(\mathrm{JC}_2\) / MathJax unchanged.

Low, not required: the replay is a first-person claim with no public pointer until the bundle DOI is live and a reader can find `CROSSCHECK.md`. That file is not in the theory bundle. Fine for this answer; do not glue it back to `21894922`.

### What still holds (do not “fix”)

- Opening refusal to treat any of this as evidence for \(\mathrm{JC}_2\).
- Prop. 4.3 conditionality and “supporting chain partly arXiv-only.”
- Helali first, 21 July, `10.5281/zenodo.21479814` (live). Suzuki `21483636` (live). Ishihara `21757679` (live; unreplayed here).
- Strinz held at his own C0-OPEN abstract. Live `10.5281/zenodo.21633408` (fetched 2026-08-18): “The target claim C0 (case closure) remains OPEN.”
- Vertex-gap + \(R_{k,d_2}\) as a char-0 depth-two description of every strip cell \(k,d_2\ge 2\).
- \(d=11\): conditional emptiness over an audited 411-row quotient, named fail-closed classes.
- 14-cell type-(3,5) at \(d=12\), list-relative.
- Book-relative landing gap: no GGV\(\to\)sheet transport, no upper bound on \(d\), none of this proves \(\mathrm{JC}_2\). Matches `REDUCTION.md` executive verdict and G2/G5.
- Thread facts, re-checked 2026-08-18: Q513413 title; four answers; ratto3423 = a/513493; last activity 2026-07-27T19:00:25Z (Procesi edit); Leox comment 1340394 still on a/513493, score 2; Procesi a/513656 still has tame \(\mathrm{Aut}(\mathbb{A}^2)\) and McKay–Wang. Checklist item 2 remains right.
- AI disclosure and “I take responsibility for every claim.”

### Checks that passed

| Claim | Result |
|---|---|
| Q513413 / a/513493 / a/513656 / Leox comment | Pass (SE API, 2026-08-18) |
| GGHV arXiv:2204.14178; \(\max\ge 108\); below 125 one family; Prop. 4.3 | Pass |
| Helali 21479814, Suzuki 21483636, Ishihara 21757679 | Pass (DOIs resolve) |
| Strinz 21633408, C0 OPEN | Pass (live abstract, exact words) |
| Posch 21894922 resolves; msolve discard not in artifact | Pass (live abstract) |
| Helali/Suzuki exact replay as a first-person claim | Pass (`CROSSCHECK.md`) |
| \(d\le 5\) book 0 survivors; 17 cells at \(d=7\); 411-row \(d=11\); 14-cell type-(3,5) | Pass vs ledgers |
| HIGH 1–2 open sectors named | Pass |
| No em dashes; word count 619 | Pass |
| N1–N3, N5 wording residuals | Pass (absent) |
| Theory-bundle DOI public | Fail (N4 process) |

### Posting bar (A)

The text can post. Fill `[BUNDLE-DOI]` with a resolving theory-bundle DOI and click it, or cut item 2 to “write-ups in preparation” and drop the closer’s bundle sentence. Confirm `10.5281/zenodo.21894922` still resolves that day (it does today). Re-check the thread immediately before posting (still quiet since the 27–28 Jul window). Do not ship a Zenodo abstract that contradicts the G2 hedge in paragraph 4: see target B.

---

## Target B — `SUMMARY.tex` + `ZENODO-METADATA-BUNDLE.md`

**FAIL.** `SUMMARY.tex` / `SUMMARY.pdf` (10 pages, rebuilt 2026-08-18 11:53 PDT) and the matching tarball cleared the eight-defect ship bar. The Zenodo description did not. A MathOverflow reader who believes v3’s “no transport theorem from the GGV normal form into the sheet frame,” then clicks the bundle DOI, will read that a “GGV-Sigray transport theorem” repaired one of the ranked gaps. That is the exact abstract-hygiene failure round 2 warned about.

Tarball hygiene first, because a rebuilt tree with a stale upload is a different bug: `dist/jc72108-theory-bundle-v1.tar.gz` is 8446855 bytes, SHA-256 `be53ce283aa6516906f65cf7b3faa0f06e56ac7700a07220e78756be2ce518a0`, matching the metadata. 302 files. `SUMMARY.tex`, `SUMMARY.pdf`, and `AUDIT.md` inside the tarball are byte-identical to the unpacked tree. The td-12 ledger heading is in the shipped `AUDIT.md`.

### The eight: did the fix actually land?

| # | Prior defect | Landed? | Evidence |
|---|---|---|---|
| 1 | GitHub `https://github.com/dcposch/jc72108` is 404 | **Yes** | No `github` / `dcposch` string in `SUMMARY.tex` or in the metadata. Provenance now points at Zenodo `10.5281/zenodo.21894922` as the canonical public artifact. Live `HEAD` of that GitHub URL is still **404** (2026-08-18 19:00 UTC), so deletion was the correct branch of the fix. Residual: the leftover `paper2/PRIORITY.md in the repository` pointer (R2 below). |
| 2 | G2 written as “partially repaired”; TRANSPORT in a THEOREM slot; gate sold as proof | **Yes** | G2 is AUDIT’s sentence (`SUMMARY.tex:495–499`): “NO transport theorem carries GGV corner data through Sigray’s normalization.” TRANSPORT is a separately scoped prose block, not a theorem environment, “not yet an `AUDIT.md` promotion entry”; `transport_check.py` is “a regression fixture for its worked data, not the proof”; “this is not a G2 closure.” PDF text matches. |
| 3 | Residue-A as the only realized object / *the* live frontier | **Yes** | Abstract and § residue-A now copy `BOOK-TD12.md` §5 and add the four r9/M2 classes, generic off-axis, and every \(td\) above the enumerated range. “Only realized configuration on the entire filed ladder” / “the campaign’s live frontier” are absent from tex and PDF. Body still recites the 4-to-212 single-pole growth. |
| 4 | Abstract “td=7 panel closed” / DS as theorem | **Yes** | Abstract hedge is *before* the list (“every rung book-relative”). Ladder is the requested decompression: book-relative \(td\le 5\); \(td=6\) funnel; \(td=7\) empty at the tower tier on the filed 17-cell perimeter; \(td=11\) conditional 411-row on FC1-R+FC3; \(td=12\) type-(3,5) list-relative first-death refusal (14 cells). DS is “banked depth-stabilization lemma (first-lemma tier)” in the abstract and a `lemma` environment, “not yet an `AUDIT.md` promotion.” |
| 5 | D23 parenthetical “consistent with Row-22 being the killing tier” | **Yes** | Deleted. Public text is: 12-hour lanes timed out; 48-hour extension running; both outcomes pre-registered; “No verdict is claimed here.” `notes.md` 2026-08-18 ~12:00 still has the lanes alive. Lab colour in `notes.md` ~03:30 must not return to the PDF. |
| 6 | Included `REDUCTION.md` contradicts the index on \(td=11\) | **Yes** | Freshness rider at `SUMMARY.tex:481–485`: frozen 2026-08-16; on \(td=11\) later `AUDIT.md` 2026-08-15/17 promotions control; item 8 of REDUCTION §4 superseded. |
| 7 | Prop. 4.2 gap not named | **Yes** | HIGH list (`SUMMARY.tex:509–512`) names “Proposition 4.2’s constant-leading-part gap, which sits directly inside the trust set of the \(td=7\) tower theorem.” The theorem body already consumes Prop. 4.2. |
| 8 | td-12 labeled PROMOTED but missing from the promotion ledger | **Yes** | `AUDIT.md:817–834` (workspace = bundle = tarball, SHA `b7e992cb2485…`): “## td-12 type-(3,5) book (2026-08-18)”, PROMOTED AT THE HONEST / LIST-RELATIVE TIER, 14 cells, 74/78 list, \(u=1\) residual, 14-check gate, `BOOK-TD12.md` source. SUMMARY theorem header cites that exact ledger heading. |

Hunt-item closeout from the prior bundle review, re-run on the rebuild: (1) tier inflation on the quote-ready surfaces is gone from SUMMARY; (2) counts / DOI `21894922` / Żołądek A.7 / dates still replay, and the GitHub 404 is no longer cited; (3) D23 outcome is not presumed; (4) honest-gap inventory, Prop. 4.2, and the AUDIT-vs-TRANSPORT G2 split are on the public page.

### Remaining defects

### R1. Metadata abstract claims a GGV–Sigray transport theorem repaired a REDUCTION gap
- **Severity:** high (hedge contradiction; the one quote-ready surface a Zenodo / MO reader sees first)
- **Where:** `dist/ZENODO-METADATA-BUNDLE.md:59–61`
- **What’s wrong:** After citing `REDUCTION.md` and “the ranked gap list,” the description continues: “the pre-Laurent GGV-Sigray transport theorem repairing one of those gaps.”
  - MO v3, the text this abstract must not outrun: “no transport theorem from the GGV normal form into the sheet frame.”
  - SUMMARY, just restored: G2 is “NO transport theorem… this is not a G2 closure.”
  - `AUDIT.md:806–808` (the ledger SUMMARY says every §§4–6 theorem inherits): “(G2) NO transport theorem carries GGV corner data through Sigray’s normalization — the sheet construction does not consume GGV data as written.”
  - `xmodel/grok-transport-review.md` finding 2: TRANSPORT is a real T2→T4 simultaneous-normalization theorem for the selected pre-Laurent pair; it does **not** repair G2 as REDUCTION CRITICAL 3 defines it; “Do not write ‘G2 repaired.’”
  - Pairing “ranked gap list” with “transport theorem repairing one of those gaps” will be read as G2. That is defect 2, moved from the PDF onto the Zenodo landing page. Round 2 already said: do not let the public Zenodo abstract say anything the MO hedges just walked back.
- **Suggested fix:** Replace the clause with SUMMARY’s scoped sentence. No stronger than: “a pre-Laurent T2-to-T4 simultaneous-normalization theorem for the GGV-selected pair; Conjecture T (corner-to-tree) remains open; this is not a G2 closure.” Do not put the words “transport theorem” and “repairing” in the same phrase as REDUCTION’s gap list.

### R2. `paper2/PRIORITY.md in the repository` is now a dangling pointer
- **Severity:** low (citation hygiene; leftover of defect 1)
- **Where:** `SUMMARY.tex:139` (PDF: “paper2/ PRIORITY.md in the repository”)
- **What’s wrong:** Defect 1 deleted the only public repository URL. `paper2/` is not in the bundle (`PRIORITY.md` count: 0). GitHub is still 404. Theorem A’s priority note already lives in-bundle in `MATHIEU.md` (the same sentence, cited on the same line).
- **Suggested fix:** Drop “`; paper2/PRIORITY.md in the repository`.” Keep `MATHIEU.md`, priority note.

Not a defect: metadata residue-A inventory, “book-relative throughout,” D23 “verdict pending, and stated as pending,” file size / SHA-256, author-name inversion (“Clemens Posch, Dan”), and the “nothing in this bundle claims a proof of JC2” closer. Those match the MO hedges and the SUMMARY rebuild.

### What still holds on SUMMARY (do not “fix”)

The prior “what is sound” table still holds: Theorem A + Żołądek A.7 / Hermoso–Alcázar; DOI `21894922` scoped as paper 1; td≤5 CLOSED; 4 r9/M2 and 4→212; 421/346/75; residue-A genome; 17 cells / 238/233; 1559+21; 411-row stamps; FC1-R+FC3 wall; td-12 14 cells list-relative with \(u=1\) residual; TDBOUND 21-of-22 / 10-of-23 / \(I_\infty=42330\); CORE2 arithmetic; D23 PENDING; 76 `cases/*.py`; gate list; “nothing claims JC2”; `REDUCTION.md` executive verdict quoted. Author “Dan Clemens Posch.” PDF is 10 pages.

### Checks that passed (B)

| Claim | Result |
|---|---|
| Tarball SHA / size / file count vs metadata | Pass |
| Unpacked SUMMARY.tex / .pdf / AUDIT.md = tarball | Pass |
| `AUDIT.md` td-12 ledger entry 2026-08-18 | Pass (workspace = bundle) |
| Defects 1–8 in SUMMARY.tex / SUMMARY.pdf | Pass |
| GitHub URL gone; live URL still 404 | Pass |
| D23 still PENDING on 2026-08-18 afternoon | Pass (`notes.md` ~12:00) |
| Metadata abstract vs MO G2 hedge | **Fail (R1)** |
| Metadata residue-A / book-relative / JC2 hedges | Pass |

### Ship bar (B)

Paste a repaired Description over R1, then upload. R2 can ride. `SUMMARY.pdf` as rebuilt is ready to be the public index. The current `ZENODO-METADATA-BUNDLE.md` Description is not.

---

## Cross-target posting order

1. Fix R1 in the Zenodo Description (one clause).
2. Upload the existing tarball; click the minted bundle DOI.
3. Paste that DOI over `[BUNDLE-DOI]` in the MO draft (N4) and click it.
4. Confirm the live Zenodo abstract still does not say that TRANSPORT repaired G2, or that residue-A is the only live object.
5. Then post v3.

A v3 MO body against a resolving bundle DOI whose Description matches SUMMARY’s G2 sentence should pass a round-4 check without another rewrite of the answer.
