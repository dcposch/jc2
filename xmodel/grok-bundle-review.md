# Hostile review — external-comms tier

**Target:** `dist/jc72108-theory-bundle-v1/SUMMARY.tex` (the 10-page public index for the Zenodo theory bundle, upload day 2026-08-18).
**Sources of truth (as commissioned):** `AUDIT.md`, `REDUCTION.md`, `TOWER-UNIFORM.md`, `BOOK-TD12.md`. Pointed corroboration only where those four name a file (`VERIFICATION.md`, `TRANSPORT.md`, `DEPTH-STAB.md`, `TDBOUND.md`, `SHEET6-DIRECTIONB.md`, `notes.md`, `xmodel/grok-transport-review.md`, `xmodel/sol-census-final.md`).
**Git:** none. No other file modified.

## Verdict

**FAIL.** Do not upload `SUMMARY.pdf` as written. The body is the most careful public statement the campaign has produced — book-relative banner, `REDUCTION.md` included, D23 stated as PENDING, `u=1` residual named, no JC2 claim — and that honesty does not save the abstract, the residue-A headline, the G2 sentence, or the GitHub URL. Those four surfaces are what a Zenodo reader, a MathOverflow commenter, or a referee who never opens the `.md` corpus will quote.

Severity: **critical** / **high** / **medium** / **low**. Defects are ordered by how badly they fail on a public timestamp.

---

## What is sound (do not “fix” these)

Cross-check of every numbered theorem, every advertised count I could replay from the four sources plus the named gates, and the residue-A arithmetic:

| claim in `SUMMARY.tex` | source | status |
|---|---|---|
| Theorem A, char 0, `AC'−wA'C` nonzero constant ⇒ `deg A ≤ 1` | `MATHIEU.md` §5.1; Żołądek, Topology 47 (2008), App. Lemma A.7; Hermoso–Alcázar 2024 `w=1` | Pass |
| DOI `10.5281/zenodo.21894922` is the paper-1 artifact | live Zenodo record, 11 Aug 2026, “Artifact for: A Vertex-Gap Obstruction…” | Pass (scope is paper 1, which is how SUMMARY cites it) |
| Author “Dan Clemens Posch”; paper title | `paper1/main.tex`; Zenodo creator “Posch, Dan Clemens” | Pass |
| td≤5 book CLOSED, 0 survivors, independent of AF2 | `SHEET6-CAMPAIGN.md`; section is marked book-relative | Pass |
| td=6 single-pole: 4 r9/M2 classes; composite survivors 4→212 over td=6..16 | `SHEET6-CAMPAIGN.md`; `SHEET6-TDUNIFORM.md`; `REDUCTION.md` HIGH 1 | Pass |
| On-axis books td=6..14: 421 / 346 / 75, 0 ROOT | `BOOK-ENUM.md` | Pass |
| Residue-A genome: child `(6,12,3,2,5)`, `σ=6`, `a1/a2=2±√3`, `κ=42` | `SHEET6-TEMPLATE.md` §0–1a; `SHEET6-DIRECTIONB.md` | Pass (`a1/a2=(√3+1)/(√3−1)=2+√3`) |
| Zero-chain: 56 of 62 T1-dead, `d_p∣d_q` iff `κ̄∈{3,4}` | `AUDIT.md` 2026-08-12 ledger (62→6 live) | Pass |
| 17 cells, 238 raw / 233 dedup; H5a 2026-08-13; U_7C moot | `TOWER-UNIFORM.md` §0; `AUDIT.md` H5a + second-cell kill | Pass |
| td-7 theorem text, 16-row witness table, 1559 checks + 21 perturbations, PROMOTED 2026-08-14, 14 errata | `TOWER-UNIFORM.md` status + §0 + §4 + §5; `AUDIT.md` TD-7 PANEL CLOSURE | Pass (theorem body matches the source, including the filed-perimeter rider) |
| td-11 entry-clash 66 checks; nested 129 = 62+31+12+3+21; 411-row census; stamps 185/133/63/12/11/7 (=411) | `VERIFICATION.md`; `AUDIT.md` 2026-08-14/15; `xmodel/sol-census-final.md` | Pass (AUDIT’s older 58/58 and 8/8 are ledger drift; SUMMARY matches the live gate) |
| FC2/4/5/6/7 discharged; residual wall FC1-R + FC3; 595-state partial | `TOWER-TD11.md` §18; `notes.md` 2026-08-17 ~12:25 | Pass |
| td-12: 14 cells, 6 spine + 8 first-death, 74 unique / 78 raw, list-relative, `u=1` gap `1/3` UNREFUSED load-bearing, 14 checks, honest-tier 2026-08-17 | `BOOK-TD12.md` status + §2–4 | Pass (this is the one panel SUMMARY does *not* oversell in the body) |
| TDBOUND: 21 of 22 construction-forced; 10 of 23 adjudicated; `I_∞=168·252−6=42330` | `TDBOUND.md` round-2 errata + §2 | Pass |
| CORE2 27 var / 45 eq / ≈6311 terms; GB 397; 13-dim; `W1^4=57673`, `W2^4=53212` mod 105337; 12/12 points, 0/12 survive D23, 36/36; D23-core 87/77; rank-4 Schur → 6 rows `c=Lb`; 12h timeout + 48h extension | `SHEET6-DIRECTIONB.md` §§7.S3–8.S2; `notes.md` 2026-08-18 ~03:30 | Pass as arithmetic; see defect 5 for the parenthetical |
| Manifest: 76 `cases/*.py`; five tower JSONs | counted in the bundle | Pass |
| Gate list 1559+21, 24, 14, 39, 22, 25, 10, 14, 6, 21 | `VERIFICATION.md` | Pass |
| “Nothing in this bundle claims a proof of JC2 or of the sheet-number exclusion”; `REDUCTION.md` executive verdict quoted | `REDUCTION.md:7–16, 50–56`; `AUDIT.md` FOUNDATIONS SCOPE 2026-08-17 | Pass as a sentence; see defects 2 and 3 for the surrounding compression |

The four hunt items, in one line each: (1) tier inflation is real, concentrated in the abstract and the residue-A / G2 headlines, not in the td-7 or td-12 theorem environments; (2) the advertised counts, the paper-1 DOI, the author name, and the Żołądek/Hermoso citations are clean; (3) D23 is correctly PENDING except one parenthetical that presumes the killing tier; (4) the honest-gap section exists and quotes the executive verdict, but it is missing the live-frontier inventory that `BOOK-TD12.md` §5 and `REDUCTION.md` HIGH 1–2 already have.

---

## Defects

### 1. The only public repository URL is a 404
- **Severity:** high (wrong URL / missing artifact)
- **Where:** `SUMMARY.tex:59–60` (and the same URL in `dist/ZENODO-METADATA-BUNDLE.md`, out of scope to edit)
- **What’s wrong:** `https://github.com/dcposch/jc72108` is **404** as of this review (2026-08-18, upload day). A Zenodo reader who clicks the one repository the summary names will find nothing. `xmodel/grok-mo-review.md` already recorded this; it has not been repaired. Whether the repo is private or the path is wrong does not matter for a public timestamp: the cited object is not there.
- **Fix:** Make the repo public under that exact URL in the same hour as the upload, **or** delete the GitHub sentence and point only at the Zenodo records that actually resolve. Do not ship a 404 as “the campaign repository.”

### 2. G2 is written as “partially repaired.” The dual-adjudicated ledger still says there is no transport theorem.
- **Severity:** high (tier inflation / ledger contradiction)
- **Where:** `SUMMARY.tex:447–456` (the transport paragraph) and `SUMMARY.tex:472–473` (the gap list: “now partially repaired by `TRANSPORT.md` at the pre-Laurent layer”); inherited-scope claim at `SUMMARY.tex:491–493`
- **What’s wrong:**
  - `AUDIT.md:801–815`, **FOUNDATIONS SCOPE ENTRY (2026-08-17, dual-adjudicated)** — the very entry SUMMARY cites as controlling every theorem in §§4–6 — still reads: “**(G2) NO transport theorem** carries GGV corner data through Sigray’s normalization — the sheet construction does not consume GGV data as written.” There is no TRANSPORT promotion line in the ledger.
  - `REDUCTION.md:25–30` and CRITICAL 3 (`REDUCTION.md:813–824`): the missing object is a GGV-chain → Sigray-tree (or at least a dictionary). Post-Laurent `[P,Q]=x^j` objects remain ill-typed.
  - `TRANSPORT.md` (same date) proves a real T2→T4 simultaneous-normalization theorem for the *selected pre-Laurent* GGV pair. That is the T4 *normalization fork*, not CRITICAL 3. `xmodel/grok-transport-review.md` finding 2, already on disk: “it does **not** repair G2 as REDUCTION CRITICAL 3 defines it (no corner-to-tree map)… Do not write ‘G2 repaired.’”
  - SUMMARY then says this scope discipline “is inherited by every theorem in Sections 4 to 6” *and* that G2 is now partially repaired. A reader who opens the cited `AUDIT.md` entry will say the summary silently overrode the ledger it claims to inherit.
  - The same paragraph says `TRANSPORT.md` “(THEOREM, 2026-08-17; gate `cases/transport_check.py`) **proves**” the two-chart form. The prior transport review: that gate does not verify Theorems 1.1 / 2.1 / 3.1. Pairing “THEOREM” with “gate” on a public page is the classic fixture-as-proof hazard.
- **Fix:** Restore AUDIT’s G2 sentence. Move TRANSPORT to a separately scoped line: “a pre-Laurent T2→T4 simultaneous-normalization theorem for the GGV-*selected* pair; Conjecture T (corner-to-tree) remains open; this is not a G2 closure.” Do not put TRANSPORT in a THEOREM slot until `AUDIT.md` has a promotion entry. Call `transport_check.py` a regression fixture, not the proof.

### 3. Residue-A is written as the only realized object and the campaign’s live frontier
- **Severity:** high (missing honest-gap disclosure / overclaim)
- **Where:** abstract `SUMMARY.tex:43–46`; ladder funnel `SUMMARY.tex:167–170`; residue-A open `SUMMARY.tex:366–368`; HIGH compression `SUMMARY.tex:483–485`
- **What’s wrong:** “the only realized configuration on the entire filed ladder and the campaign’s live frontier” will be read as “everything else is dead.” The four sources say otherwise.
  - `BOOK-TD12.md:117–119`, the document SUMMARY is indexing: “the filed ladder’s live frontier is exactly {residue-A} **plus the unadjudicated above-bound entries (td 8, 10, 12-(2,3)/(2,5), 14).**”
  - `REDUCTION.md` HIGH 1: composite single-pole search classes survive at every composite `d` in the table (4 at `d=6`, then 16/16/23/71/48/87/212). SUMMARY itself recites “4 to 212” two pages earlier, then forgets them at the frontier sentence.
  - `REDUCTION.md` HIGH 2: **no on-axis panel is completely killed at `d=8,9,10,12,14`**; 23 modeled local survivors, 22 of them at composite `d>6`. Residue-A is one cell in that table, not the table.
  - `REDUCTION.md` CRITICAL 7 / `AUDIT.md` G5: no upper bound on `td`. A finite-range run cannot reduce JC2.
  - “Realized” is internal jargon (has a coefficient-tier template). On a public page it reads as “exists / is the remaining counterexample shape.” The 4 r9/M2 classes at `td=6` are live search classes on the same sheet.
- **Fix:** Copy `BOOK-TD12.md` §5 verbatim into the residue-A open and into the abstract: residue-A is the unique *coefficient-tier* two-pole template and the current compute target; the live inventory is residue-A **plus** the 4 single-pole r9/M2 classes at `td=6`, the unadjudicated above-bound on-axis entries, generic off-axis, and every `td` above the enumerated range. Do not write “the” live frontier.

### 4. Abstract compression: “td=7 panel closed” and “depth-stabilization theorem”
- **Severity:** medium (tier inflation; the body is better)
- **Where:** abstract `SUMMARY.tex:35–43`; Theorem DS environment `SUMMARY.tex:413–433`
- **What’s wrong:**
  - “the `td=7` panel closed by a uniform tower theorem, 17 of 17 cells” is the sentence that will be pasted. `TOWER-UNIFORM.md:216–221` and the theorem’s own §4: obstruction over the **filed route perimeter**, not convergence, not P-realizability, not existence away from the represented charts. `REDUCTION.md:865–868`: “the final tower theorem still declares the filed route perimeter as a hypothesis.” `AUDIT.md:812–814`: promoted ladder results are **book-relative**. The hedge “book-relative where that is all that is proved” sits *after* the list and says “below,” which a skimmer will not apply to the list itself.
  - Parallel construction with “the `td≤5` closure” and “the `td=12` first-death-refusal book” invites the reading that those rungs are closed in the same sense. The body of the td-12 theorem is correctly list-relative; the abstract does not say so.
  - “the depth-stabilization theorem” is in the abstract’s theorem stack. `DEPTH-STAB.md` status line: **BANKED 2026-08-17, first-lemma tier**. It is not in `AUDIT.md`. Wrapping it in `\begin{theorem}` in a public PDF promotes it one grade. The body does say BANKED; the abstract does not.
- **Fix:** Abstract ladder, no stronger than: “book-relative `td≤5` emptiness; `td=6` funnel to residue-A; `td=7` off-axis book empty at the tower tier on the filed 17-cell perimeter; `td=11` conditional 411-row certificate on FC1-R+FC3; `td=12` type-(3,5) list-relative first-death refusal (14 cells).” Demote DS to “banked lemma (first-lemma tier)” in the abstract and change `\begin{theorem}` to a remark or a named lemma environment.

### 5. D23 parenthetical presumes the killing tier
- **Severity:** medium (hunt item 3: pending computation, presumed outcome)
- **Where:** `SUMMARY.tex:405–410` (“timed out at their 12-hour caps **(consistent with Row-22 being the killing tier)** and a 48-hour extension lane is running”)
- **What’s wrong:** The rest of the item is clean: PENDING, both outcomes pre-registered, “No verdict is claimed here.” The parenthetical is not. A timeout is consistent with a hard nonempty system just as well as with an EMPTY killing tier. `notes.md` 2026-08-18 ~03:30 uses the same phrase as lab colour; a public PDF must not. `SHEET6-DIRECTIONB.md:1218–1222` pre-registers EMPTY *and* NONEMPTY. Suggesting which one the timeout “confirms” is a verdict by innuendo.
- **Fix:** Delete the parenthetical. Keep: 12-hour lanes timed out; a 48-hour extension is running; both outcomes are pre-registered; no verdict is claimed.

### 6. The included `REDUCTION.md` still contradicts the index on td=11
- **Severity:** medium (bundle-internal contradiction on a timestamped page)
- **Where:** SUMMARY td-11 certificate `SUMMARY.tex:247–266`; `REDUCTION.md:867–868, 1039–1043` (shipped in the same tarball)
- **What’s wrong:** SUMMARY (following `AUDIT.md` 2026-08-15 and the 2026-08-17 foundations entry) correctly advertises a promoted 411-row *conditional* emptiness certificate. `REDUCTION.md` (2026-08-16), which SUMMARY calls “the campaign’s own verdict on its foundations,” still says there is “no analogous completed census at `d=11`” and, in the “claims that are wrong” list, “at `d=11` an attempted 159-row diagnostic artifact exists, but no certified complete census does; its universal certificate is broken.” `xmodel/grok-reduction-review.md` already flagged this staleness. A reader who does what the summary asks — open `REDUCTION.md` — will find the index and the audit disagree about a promoted object. That is the opposite of a clean timestamp.
- **Fix:** In SUMMARY’s audit paragraph, add one rider: “`REDUCTION.md` is frozen at 2026-08-16; on `td=11` the later `AUDIT.md` 2026-08-15/17 promotion controls (conditional 411-row certificate, residual wall FC1-R+FC3). Item 8 of REDUCTION §4 is superseded.” Do not silently pick the later reading while telling the reader REDUCTION is the verdict.

### 7. The tower trust-set gap (Proposition 4.2) is not named
- **Severity:** medium (missing honest-gap disclosure)
- **Where:** foundations HIGH list `SUMMARY.tex:483–485`; td-7 theorem `SUMMARY.tex:203–228`
- **What’s wrong:** `REDUCTION.md:967–968` HIGH 3, load-bearing for the object SUMMARY calls a THEOREM: “Proposition 4.2’s constant-leading-part gap, directly inside the tower trust set.” `TOWER-UNIFORM.md:46–51` lists Prop 4.2 in the trust set. SUMMARY’s HIGH line compresses this to “the Sigray replacement is not end to end.” That is true and too vague for a document whose headline theorem consumes Prop 4.2 at every cell.
- **Fix:** Name Prop 4.2’s constant-leading-part gap in the HIGH list, in the same sentence as the td-7 theorem’s trust-set perimeter.

### 8. td-12 is labeled PROMOTED; it is not in the promotion ledger
- **Severity:** low (process / citation hygiene)
- **Where:** `SUMMARY.tex:282–284`
- **What’s wrong:** `BOOK-TD12.md` self-promotes at the honest tier after `xmodel/grok-td12-review.md` SOUND-WITH-ERRATA. `AUDIT.md` is the document SUMMARY calls “the promotion ledger,” and it has no td-12 entry (it ends at the 2026-08-17 foundations note). The mathematical claim is the one `BOOK-TD12.md` actually makes and is not inflated. The label “PROMOTED” on a public page, with `AUDIT.md` named as the ledger, is a process miss.
- **Fix:** “Recorded in `BOOK-TD12.md` at the honest / list-relative tier (2026-08-17); not yet a numbered `AUDIT.md` promotion line.” Or add the ledger line first, then ship.

---

## Hunt-item closeout

| hunt | result |
|---|---|
| (1) tier inflation | **Hit.** Defects 2, 3, 4, 8. The td-7 and td-12 *theorem bodies* are scoped correctly; the abstract, the G2 sentence, the residue-A headline, and the BANKED-as-theorem DS environment are not. |
| (2) wrong counts / DOIs / names / dates | **Mostly clean.** 17 / 238 / 233 / 411 / 185+133+63+12+11+7 / 74+78 / 14 / 1559+21 / 66 / 24 / 421+346+75 / 4→212 / 21-of-22 / 10-of-23 / 42330 / 27+45+6311 / 397 / 13 / 87+77 / 76 / 5 / DOI 21894922 / Żołądek 2008 A.7 / H5a 2026-08-13 / tower 2026-08-14 / census 2026-08-15 / td-12 2026-08-17 all replay. **The GitHub URL does not resolve (defect 1).** AUDIT’s stale 58-check / 8-check figures are ledger drift, not a SUMMARY error. |
| (3) D23 outcome presumed | **Hit, one clause.** PENDING + both-outcomes + “no verdict claimed” is honest. “consistent with Row-22 being the killing tier” is not (defect 5). As of `notes.md` 2026-08-18 ~07:10 the 48-hour lane is still grinding; SUMMARY is not stale on the running-computation fact. |
| (4) missing honest-gap disclosure | **Hit.** The executive “not a theorem” sentence is present and correct. Missing from the quote-ready surfaces: the `BOOK-TD12.md` §5 live-frontier inventory, the HIGH 1–2 survivor tables, Prop 4.2 in the tower trust set, and the AUDIT-vs-TRANSPORT G2 split (defects 2, 3, 7). |

## Minimum ship bar

Before `SUMMARY.pdf` is the public face of a Zenodo record:

1. Fix or drop the GitHub URL (defect 1).
2. Revert G2 to AUDIT’s sentence; re-scope TRANSPORT (defect 2).
3. Replace the residue-A “only realized / the live frontier” sentences with the `BOOK-TD12.md` §5 inventory (defect 3).
4. De-compress the abstract ladder and demote DS (defect 4).
5. Delete the D23 “killing tier” parenthetical (defect 5).

Defects 6–8 can ride in a one-paragraph rider if 1–5 are done. As written: **do not upload.**
