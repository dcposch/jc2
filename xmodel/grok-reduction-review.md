**VERDICT: SOUND-WITH-ERRATA — the advertised Keller→GGV-polygon→sheet→enumerated-book chain is not a theorem in the repository or the cited literature; executive gaps 1, 2, and 5 are real as stated; gap 4 is real for a universal/full-configuration landing map and for the generic `b≥2` grid, but overreaches by treating the td-7 §11a completeness certificate and the 2026-08-15 td-11 conditional-emptiness certificate as if they did not exist.**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-16.
Target: `REDUCTION.md` (2026-08-16 hostile dependency audit / consolidation master).
Claim under review: the campaign end-to-end reduction is not a theorem; five numbered executive claims (the supportable list, which are also the five gap claims); blast radius on the promoted td-7 panel closure and the td-11 census.
Method: line-read of `REDUCTION.md` T1–T10, the executive five-point list, and §3–§4; independent check of the cited repo docs (`SECTION4-AUTOMATION.md`, `SIGRAY-AUDIT.md`, `SHEET6-TDUNIFORM.md`, `SHEET6-DEPTH.md` §§8–9, `SHEET6-MULTIPOLE.md`, `BOOK-ENUM.md` + `cases/book_enum.py`, `BOOK-OFFAXIS.md` §§10–11a, `TOWER-UNIFORM.md` §§0/4, `TOWER-TD11.md` §§10/17–18, `AUDIT.md` 2026-08-14/15 ledger, `xmodel/sol-census-review.md`, `xmodel/sol-census-final.md`, `xmodel/grok-census-review.md`, `xmodel/grok-census11a-review.md`, `paper2/SCOPE.md`, `paper2/main.tex`); external check of Guccione–Guccione–Valqui, arXiv:1401.1784 (journal *J. Algebra* 471), Definition 4.3 / Proposition 4.7 / Corollary 5.21, against Sol's quantifier. No other repo file modified. No git.

---

## Findings, ranked

### 1. Severity: critical — the sequential reduction is not a theorem. Sol's headline stands.

- File: `REDUCTION.md:7-56,630-663`
- Claim: Keller counterexample ⇒ GGV polygon data ⇒ sheet data of degree \(d\) ⇒ an enumerated book entry is **not** a theorem.
- How checked. The four arrows were checked separately against the files that would have to carry them.

  | arrow | what a theorem would need | what exists |
  |---|---|---|
  | CE → GGV-minimal standard polygon | every given CE, or at least a selected one, carries GGV1/GGV5 chain data | GGV Corollary 5.21: *if* JC is false *then there exists* a minimal standard \((m,n)\)-pair. Existential over the set of all counterexamples. |
  | GGV polygon → Sigray sheet | a translation of GGV corners/admissible chains through Sigray Aut + Lemma 2.1 | no file, no cited theorem. Sheet engines start from Sigray type \((\alpha,\beta)\), not from a GGV chain. |
  | sheet → finite entry \(E\) at fixed \(d\) | mass identity + entry arithmetic | T7 / `SHEET6-TDUNIFORM.md` §§1–2, conditional on the repaired Prop. 5.8 package. This arrow *is* a theorem at its stated perimeter. |
  | entry \(E\) → enumerated \(B(d,E)\) | a defined universal endpoint plus a total landing map | three distinct intended objects (`REDUCTION.md:107-120`); `book_enum.py:348-350` `continue`s every off-axis entry; generic off-axis P5 has no completeness certificate; no upper bound on \(d\). |

  The honest diagram is the fork Sol draws at T4, not a chain. Paper 1 is the GGV-farm lane. Paper 2 / the sheet ladder is the Sigray-entry lane. `SHEET6.md:37` even points survivors *back* at the GGV pipeline, which is the reverse of the advertised arrow. No promoted file states the sequential composite as a theorem; the composite is campaign glue. That does not make it a theorem.

- Sol is also right that a proof-by-contradiction of JC2 may start from a *selected* GGV-minimal pair. That repairs the GGV *lane*. It does not repair the sequential claim that *that pair's GGV data* become sheet data and then a book record.

### 2. Severity: critical — Gap 2 is real. There is no GGV-normalization ↔ Sigray-normalization transport.

- File: `REDUCTION.md:25-30,271-336,813-824`; GGV1 Cor. 5.21 and Prop. 4.7; `SIGRAY-AUDIT.md:12` (Lemma 2.1); `SECTION4-AUTOMATION.md:39-67` (the \(\psi_j\) step).
- Claim: any chosen CE can be Sigray-normalized without changing \(td\); no theorem transports GGV corner/admissible-chain data through that second normalization.
- How checked.

  **Sigray half is a theorem if the cited statements are accepted.** Lemma 2.1 is `VERIFIED_WITH_NIT` in `SIGRAY-AUDIT.md`: lex-min \((\deg f,\deg g)\) in the source/target Aut class, then a nondegenerate linear source change (plus a harmless target scaling to restore \(J=1\)) produces rectangular Newton polygons and a type \((\alpha,\beta)\). Polynomial Aut preserve \([\mathbf C(x,y):\mathbf C(f,g)]\). This applies to *any* nonautomorphic pair, including the pair selected by T2.

  **GGV half is a different Aut problem.** GGV Definition 4.3 is an \((m,n)\)-pair in the Laurent ring \(L^{(l)}\) with
  \[
    \frac{v_{1,1}(P)}{v_{1,1}(Q)}=\frac{v_{1,0}(P)}{v_{1,0}(Q)}=\frac{m}{n},\qquad v_{1,-1}(\operatorname{en}_{1,0}(P))<0.
  \]
  Proposition 4.7 produces this shape by some \(\varphi\in\operatorname{Aut}(L)\), citing van den Essen Cor. 10.2.21 for the subrectangular support. Later GGV-farm cuts (`SECTION4-AUTOMATION.md:64-66`) apply \(\psi_j\colon x\mapsto x^{-1},\; y\mapsto x^j y\), which is **not** in \(\operatorname{Aut}\mathbf C[x,y]\) and changes the bracket to a power of \(x\). GGV22 Proposition 4.3 lands at \([P,Q]=x^2\). That object is not a Sigray input.

  **No dictionary.** Repo-wide search for a GGV-corner \(\mapsto\) Sigray-tree map returns none. `SHEET6-TDUNIFORM.md` §1 starts from Sigray Notations 2.3–2.4 / Statements 5.2 / Propositions 5.3–5.8. `BOOK-ENUM.md` reuses `tdu_rows`. Neither consumes a GGV admissible chain. The two type symbols \((m,n)\) and \((\alpha,\beta)\) look similar and are not proved equal, or even simultaneously realizable, after the two normalizations.

  **What would look like a transport and is not.** A Sigray-rectangular pair still *has* a Newton polygon. One could read some GGV-style valuations off it. That is not transport of the GGV-*minimal* admissible-chain / GGV5 farm data, and it is not an input to any sheet engine as written. Sol's sentence “the GGV data are therefore not an input to the sheet construction” is exact.

- Overreach to refuse. Do not read Gap 2 as “Sigray-normalized pairs have no polygon data.” They do. The missing object is a *translation of the GGV-minimal chain through Sigray Aut*.

### 3. Severity: high — Gap 4 is real as a *universal* claim and overreaches as an *off-axis-certificate* claim.

- File: `REDUCTION.md:36-45,597-626,852-868,1036-1043`; `BOOK-OFFAXIS.md:608-630,704-830`; `BOOK-ENUM.md:35,173-176,348-350` of `cases/book_enum.py`; `TOWER-UNIFORM.md:26-58,216-221`; `TOWER-TD11.md:1-11,441-475,671-720`; `AUDIT.md:729-799`; `xmodel/sol-census-review.md:1`; `xmodel/sol-census-final.md:1,69`; `xmodel/grok-census11a-review.md:1-8`; `xmodel/grok-census-review.md:1`.
- Claim (executive point 4 / CRITICAL 5): passage from an entry menu to a complete full-configuration book is not general; the implementation skips every off-axis entry; the generic off-axis audit reports that no completeness certificate exists for any \(b\ge 2\) entry.
- How checked.

  **Real, and Sol did not miss `BOOK-ENUM`.** `cases/book_enum.py:348-350` increments `entries_offaxis` and `continue`s. `BOOK-ENUM.md` §6 and the 2026-08-12 scope rider say the same: prime-\(td\) emptiness is all-\(b=1\) emptiness; off-axis is not enumerated. `SHEET6-DEPTH.md` §8's finite book is the local marked-event object; §9 explicitly leaves mixed \(\mu_e\ge 2\) merges, \(M\ge 2\) suffixes, and P-realizability out. Sol's reading of the on-axis landing theorem as *local* rather than full-configurational is the reading those files themselves force.

  **Real for the generic grid.** `BOOK-OFFAXIS.md:618-621` (P5), verbatim: at a fixed printed budget the post-jump state set has unbounded numerator and \(M\); the grid loop's proved bounds scale with \(\mathrm{num}(w)\cdot M_G\); “no completeness certificate exists for any \(b\ge 2\) entry at any \(td\)”; recount \(0\) DEAD / \(0\) ALIVE / \(2691\) OPEN. Sol quotes this accurately. It is a statement about the *generic grid engine*, not about every off-axis argument in the repo.

  **Overreach: td-7 carries a real enumeration-completeness certificate that Sol files as a parenthetical.** The unique \(td=7\) entry is type \((2,3)\), \((1,1,2)\oplus(1,2,3)\) (`TOWER-UNIFORM.md:67-69`). T7 gives \(s\le d/3\), so \(s\le 2\) at \(d=7\): no three-pole escape. Single-pole is the prime TDU kill. On-axis is empty by the prime partition. What remains is one off-axis two-pole entry. For that entry the repo has:

  1. P3, “\(td=7\) complete arrangement classification — hand-proved” (`BOOK-OFFAXIS.md:521-549`): root merge, chain-1-at-0, unequal-\(\mu\), class A/B/C.
  2. P0-closed 69-state family at budget \(5=td-2\).
  3. §11a cap-free \((I5a)\)–\((I5d)\) inversion, no guessed \(\nu\)-cap; the \(w=2/(2k+1)\) family terminates by closure, not by a cap (`BOOK-OFFAXIS.md:775-778`).
  4. Brute-force \(\nu_G\le 400\): 0 miss / 0 extra (`BOOK-OFFAXIS.md:706`; independently replayed in `xmodel/grok-census11a-review.md:7`, VERDICT SOUND).
  5. Gates G1–G5.

  That is an enumeration-completeness certificate for the class-B/C *merge-cell menu of the unique \(td=7\) entry relative to the filed budget-5 closure*. Sol knows this — T9(c) and CRITICAL 5 call the \(d=7\) inversion “special” and “cap-free inside its hand-proved classification” — and then the executive slogan and CRITICAL 5 headline still read as if off-axis books carry *no* completeness certificate. The precise statement is P5's: the *generic grid* has none. Collapsing that to “off-axis books have none” is the overreach.

  **Overreach / staleness: the td-11 certificate Sol cites as broken was repaired the day before `REDUCTION.md`.**

  | Sol writes (`REDUCTION.md:616-620,771,1038-1043`) | What the ledger actually contains by 2026-08-15 |
  |---|---|
  | “attempted program artifact constructs and stamps 159 diagnostic rows” | `AUDIT.md:785-799`, 2026-08-15: promoted **411-row** instrument-backed quotient; Sol's own scope-hole chart + 5 siblings enter and die OUTER-DEAD |
  | cites `TOWER-TD11.md` §10 (“NOT an emptiness certificate”) and `xmodel/sol-census-review.md` VERDICT BROKEN | omits `xmodel/grok-census-review.md` SOUND-WITH-ERRATA; omits the M_G-scope repair; omits `xmodel/sol-census-final.md` VERDICT EARNED; omits `AUDIT.md` “td-11 CONDITIONAL EMPTINESS CERTIFICATE (2026-08-15) PROMOTED” |
  | ledger 2.4: “beyond-core, nested, and multi-word sectors remain open” | `TOWER-TD11.md:1-11,671-693`: nested 129 CLOSED-AT-TIER; two-word deep families CLOSED by NF-Z† DIE-horn; remaining OPEN named as beyond-core, cap-free closures, NF-P slice, refile |

  `REDUCTION.md` is dated 2026-08-16. The 2026-08-15 promotion is in `AUDIT.md` in the same repo. Citing §10 and the BROKEN review as if they were last word is selective. It does **not** create a complete \(td=11\) census — EARNED is *conditional emptiness of an audited layer*, still on FC1–FC7, and `TOWER-TD11.md` §18 still names FC1-R + FC3 (refile) as the residual wall. Sol's *refusal to promote \(td=11\) to a panel statement* is correct. The claim that no certified census-level certificate exists is not.

### 4. Severity: high — Gap 1 is real. GGV's own Corollary 5.21 is the existential statement Sol says it is.

- File: `REDUCTION.md:20-24,166-222,797-810`; GGV1 (arXiv:1401.1784 / *J. Algebra* 471) §4 and Corollary 5.21.
- Claim: GGV permits selection of *some* globally minimal standard counterexample; this is not a normalization of every given counterexample; the selected pair's \(td\) need not equal the original's.
- How checked. GGV defines
  \[
    B \;=\; \min\bigl\{\gcd\bigl(v_{1,1}(P),v_{1,1}(Q)\bigr) : (P,Q)\text{ a counterexample}\bigr\}
  \]
  (or \(\infty\) if JC is true). “A minimal pair is a counterexample \((P,Q)\) such that \(B=\gcd(v_{1,1}(P),v_{1,1}(Q))\).” Corollary 5.21, quoted:

  > If \(B<\infty\) (i.e., if the Jacobian conjecture is false), then there exists a Jacobian pair \((P,Q)\) and \(m,n\in\mathbf N\) coprime with \(m,n>1\), such that (1) \((P,Q)\) is a standard \((m,n)\)-pair in \(L\), (2) \((P,Q)\) is a minimal pair.

  That is exactly Sol's quantifier. Proposition 4.7 then Aut-moves *a minimal pair* into \((m,n)\)-shape. Nothing in §4 makes an arbitrary counterexample minimal inside its own Aut class. In particular there is no relation between \(td\) of a starting pair and \(td\) of the selected GGV-minimal pair.

- Nit, not a refutation. Sol writes \(B_{\mathrm{GGV}}=\min\{\gcd(\deg P,\deg Q)\}\). GGV's \(B\) is \(\gcd(v_{1,1}(P),v_{1,1}(Q))\). After the subrectangular Aut these often coincide with the degrees; they are not the same symbol. The quantifier claim does not depend on the identification.

### 5. Severity: high — Gap 5 is real. No cited theorem bounds \(td\) above.

- File: `REDUCTION.md:46-48,886-904`; GGV22 as summarized at `REDUCTION.md:242-248,697`; `SHEET6-TDUNIFORM.md:23-29`; `paper1/main.tex:34`.
- Claim: a run over \(td=6,\ldots,14\) cannot be an end-to-end reduction of JC2 even if every one of those books were complete.
- How checked. Żołądek Theorem 6.12 gives \(td\ge 6\). GGV22's “\(\max(\deg P,\deg Q)\ge 125\) or \((72,108)\) or transpose” is a *lower*-bound dichotomy in *polynomial* degree, and only for the GGV-minimal lane. GGV5 Algorithm 8 is complete only under an input bound \(v_{1,1}(A_0)\le M\). `SHEET6-TDUNIFORM.md` §7: no finite residual list uniform in \(d\); composite single-pole searches grow \(4\to 212\) from \(d=6\) to \(d=16\). Moskowicz arXiv:2407.13795 (no prime field-extension degree) is unpublished and unused, correctly. No sheet theorem, no GGV theorem, and no Sigray theorem supplies \(td\le N\).

  Closing every book for \(6\le d\le 14\) would still leave \(d\ge 15\). This is fatal for the sequential “books reduce JC2” reading and is not fatal for a GGV-lane proof that kills the selected minimal pair by polygon/degree methods.

### 6. Severity: clear — the five-point “what IS supportable” list is accurate after two tightenings.

The executive list (`REDUCTION.md:20-48`) is the right residual, with the following amendments.

| # | Sol's supportable claim | Accurate? | Tightening |
|---|---|---|---|
| 1 | JC false ⇒ some GGV-minimal standard CE exists; not a per-CE normalization | **Yes.** GGV Cor. 5.21. | Write \(B=\min\gcd(v_{1,1})\) as GGV does, not \(\gcd(\deg)\). |
| 2 | Any CE has a Sigray NF of the same \(td\); GGV chain data do not transport | **Yes.** Lemma 2.1 + the fork at T4. | Do not deny that the Sigray pair has *a* Newton polygon; deny transport of the GGV-*minimal chain*. |
| 3 | Sigray-normalized CE ⇒ pole/tree data + finite entry menu at each fixed \(td\), after the Prop. 5.8 repair | **Yes, and this is the strongest general finite reduction.** | Keep it inside T7's perimeter: mass identity relative to the audit-corrected pole IDs + Chau 4.4 + the N2 line; entry pin \(M=b\) and the \(\nu\)-menu remain conditional on the corrected Sigray/TDU/MP package. `SOL-PROP58.md`'s header still overstates patch incorporation (`REDUCTION.md:460-464`) — Sol is right about the status drift. |
| 4 | Entry menu ↛ complete full-configuration book in general; on-axis local landing is a theorem; generic off-axis has no completeness certificate; only special sectors are enumerated | **Mostly yes.** | Replace the last two clauses by: generic P5 grid has no completeness certificate; the unique \(td=7\) entry has a perimeter-relative completeness certificate (§11a + P3 + \(\nu\le 400\)); \(td=11\) has a promoted *conditional* layer-emptiness certificate, not a complete census. |
| 5 | No upper bound on \(td\); a \(6..14\) sweep is not a JC2 reduction | **Yes.** | None. |

The “maximal current reduction” boxed at T10 (`REDUCTION.md:649-659`) is the right theorem-shaped residual, once point 4 is tightened as above. It correctly does not use GGV polygon restrictions after selecting the pair.

### 7. Severity: clear — T1 and the “prime \(td\) excludes everything” slogan are false as stated; Sol is right; these are wording bugs, not proof gaps.

- Nonlinear triangular Aut \((x,y+x^2)\) has \(J=1\) and is not linearly equivalent to \((x,y)\). The chain must start from “not a polynomial automorphism” or from “JC2 is false.”
- TDU's prime theorem is single-pole (`SHEET6-TDUNIFORM.md:19-22`). `BOOK-ENUM.md:194-198` already retracted “td 7/11/13 fully excluded.” Older `BOOK-BASH-R2.md` / `TEMPLATE-ATTACK.md` prose that still says those panels are excluded is unsafe to cite (`REDUCTION.md:990-994`).

### 8. Severity: residual — Gap 3's “finite entry menu” is not a free lunch.

Point 3 is supportable and is also the load-bearing general reduction. Its hypotheses are not decorative. `SIGRAY-AUDIT.md` stops at Proposition 6.2; Proposition 6.8 is still unaudited and is used in MP5–MP6; Proposition 4.2's constant-leading-part gap sits inside the tower trust set; `SOL-PROP58.md` still lacks the N2 line its header claims. Sol records all of this (T6–T7, HIGH 3). A referee who accepts T7 and rejects the unaudited §§7–9 package still has a finite *entry list*, not a finite *configuration* list. That distinction is load-bearing for every later book.

---

## Gap-by-gap: real / overreach

### Gap 1 — GGV existential vs universal. **REAL.** No overreach on the quantifier.

Repair is wording. A JC2-contradiction proof may select the GGV-minimal pair and stay in the GGV lane. The campaign may not say “every counterexample carries GGV-minimal data,” and may not transfer that pair's \(td\) to an arbitrary starting CE.

### Gap 2 — GGV ↔ Sigray transport. **REAL.** Slight slogan-risk, not a false claim.

The two normalizations are different Aut problems (GGV: \(\operatorname{Aut}(L)\) plus, in the farm, Laurent \(\psi_j\) leaving \(\operatorname{Aut}\mathbf C[x,y]\); Sigray: source/target polynomial Aut + linear source change). No translation of GGV corners/admissible chains into Sigray pole/tree decorations exists in the repo or in the cited GGV/Sigray texts. The sheet construction does not take GGV data as input. The only overreach is a reader collapsing this to “Sigray pairs have no Newton polygons.”

### Gap 3 — finite entry menu at fixed \(td\). **REAL as a positive; not a break.**

This is the strongest general finite reduction the campaign presently has. It is conditional, and it produces entries, not configurations. Sol says both things.

### Gap 4 — no universal/full-configuration landing; off-axis completeness. **REAL for the universal claim; OVERREACH for “off-axis books carry no completeness certificate.”**

Sol did **not** miss `BOOK-ENUM.md`'s off-axis skip or `SHEET6-DEPTH.md` §9's full-config exclusion. Sol **did** underweight, and in the td-11 ledger omit, completeness statements that are in the cited files:

- `BOOK-OFFAXIS.md` P3 + §11a + `xmodel/grok-census11a-review.md` SOUND: completeness of the unique \(td=7\) class-B/C menu relative to the filed budget-5 closure.
- `AUDIT.md` 2026-08-15 + `xmodel/sol-census-final.md` EARNED: conditional emptiness of a 411-row td-11 class-B/C quotient on FC1–FC7.
- `TOWER-TD11.md` §§15–18: nested 129 and two-word deep families closed at tier after the BROKEN review Sol cites.

None of those is a universal \(B(d,E)\) landing theorem. All of them are more than “no certificate.”

### Gap 5 — no upper bound on \(td\). **REAL.** No overreach.

---

## Triage

| gap | repairable with existing machinery? | genuinely new mathematics? |
|---|---|---|
| **1** (GGV quantifier) | **Yes, editorial.** State Cor. 5.21 as written. For a JC2-contradiction, select the minimal pair and stay in the GGV lane (paper 1). | No. |
| **2** (transport) | **Yes, by abandoning the sequential claim.** Treat GGV-farm and Sigray-sheet as independent lanes — which is already how the two papers are written. | A *dictionary* GGV-chain \(\leftrightarrow\) Sigray-tree, or a proof that one Aut can achieve both NFs at once, is new mathematics and is not needed if the sequential claim is dropped. |
| **3** (entry menu) | **Mostly yes.** Incorporate N2 into `SOL-PROP58.md`; keep the T7 perimeter explicit. Finiteness of \(E\) at fixed \(d\) is then arithmetic. | Replacing the remaining Sigray §§7–9 imports with a standalone package is a large internal reproof, not a new theorem about Keller maps. |
| **4** — typed on-axis landing map | **Yes, specification/compiler.** `SHEET6-DEPTH-REVIEW.md` §6 already specifies `BOOK(s,td)` at the marked-event tier. What is missing is a total typed configuration-to-record map plus fail-closed provenance (`REDUCTION.md:835-849`). | No new invariant. |
| **4** — on-axis post-jump / mixed \(\mu\ge 2\) | **No.** Quarantined in `SHEET6-MULTIPOLE.md` §4, `SHEET6-DEPTH.md` §9, `TEMPLATE-ATTACK.md` §§1c, 6. | Yes: an \(M\ge 2\) analogue of the \(w\)-closure. |
| **4** — generic off-axis completeness | **No.** P5 is the obstruction: unbounded \(\mathrm{num}(w)\) and \(M\) at fixed printed budget; solver bounds scale with them. | Yes: Sol's proposed cap-free \(M\ge 2\) state theorem / monovariant (`REDUCTION.md` §5.2). Budget arithmetic will not do it (td-7 already has zero/low-cost escapes). |
| **4** — td-7 as a *panel* | **Mostly yes, already built.** Unique entry + P3 + §11a + tower uniformity. Remaining hole is “beyond-filed-closure = under-enumeration” (`TOWER-UNIFORM.md:52-53`) plus the Sigray/H5a/E5/Prop. 4.2 trust set. | Proving the filed budget-5 closure exhausts every legal route of the unique entry is a completeness argument in existing grammar, not a new invariant. Accepting the trust set is a documentation/audit problem. |
| **4** — td-11 as a *panel* | **Partially.** Entry-clash at exact-core tier and the 411-row conditional certificate are built. | Completing FC1-R (beyond-core) is a mix of a reachable-numerator invariant or a cap-free closure (new math or heavy computation). FC3 (Q+E5/E5F refile) is the wall named in `TOWER-TD11.md:715-720`: multi-round engineering plus the merged-emission \(w\) law. |
| **5** (no \(td\) bound) | **Not in the sheet lane.** The GGV bounded-degree / \((72,108)\) lane is the existing alternative, and it does not bound \(td\). | An upper bound on \(td(F)\) for a plane Keller counterexample is new mathematics. Without it the sheet ladder cannot finish JC2. |

Highest-leverage repairs, ranked by what they actually buy:

1. **Drop the sequential claim in every public theorem.** Two lanes. This is free and removes Gaps 1–2 as load-bearing.
2. **Define the four endpoints Sol lists** (entry book / local marked-event menu / route book / full-configuration book) and type the existing DEPTH landing map. This decides which current kills are global.
3. **State td-7 as a filed-book theorem**, not as “the \(td=7\) panel is closed.” The mathematics for that wording is already promoted.
4. **Do not advertise \(td=11\) as a panel.** Discharge FC1-R + FC3 or keep the conditional-layer statement.
5. **Only then** spend new mathematics on a cap-free \(M\ge 2\) theorem or a \(td\) bound.

---

## Blast radius on promoted results

Gap 4 does **not** retract the td-7 tower theorem or the td-11 clash/census theorems as written in their own files. It **does** demote every *panel* reading of those theorems to a *book-relative / layer-relative* reading. Paper 2's planned abstract (`paper2/main.tex:36-37`) already knows this for \(td=7\) (“formal-tier obstruction over a filed route perimeter”). `AUDIT.md:729` and `paper2/SCOPE.md:210` (“two closed panels, \(td\le 5\) and \(td=7\)”) do not.

### \(td\le 5\)

**Honest scope (unchanged by this audit).** A complex polynomial Keller map of topological degree \(\le 5\) is invertible (Żołądek, *Topology* 47 (2008), Theorem 6.12). Unconditional, refereed-published. Sigray Theorem 9.1 is not used. This is a genuine panel closure. It is not a campaign theorem.

### \(td=7\)

**Promoted theorem, as written** (`TOWER-UNIFORM.md:26-36`, `AUDIT.md:729-743`). Every cell of the E5-corrected \(td=7\) class-B/C book (17 cells, 238 raw / 233 deduplicated routes) dies at the tower tier: no realization of any *filed* completion route admits a global Prop. 4.2 ladder. Class B is empty before this tier. Reading-independent on the forced-\(\nu\) 2-cell sub-book. Machine gate 1559/1559. Hostile reviews SOUND-WITH-ERRATA / CONFIRMED.

**What Gap 4 demotes.** “The \(td=7\) panel is closed” / “there is no Keller counterexample of topological degree 7.”

**Honest scope.**

> Assume a Sigray-normalized complex Keller counterexample of type \((\alpha,\beta)\) and topological degree 7, inside the declared trust set (H5a Q-value + E5, Prop. 4.2, Prop. 8.1(i)–(v), Cor. 6.1, St. 8.3(i)+Not. 4.1, St. 3.9/3.17(i)/3.11(i), BOOK R1.0–R2.2/P0–P3, repaired Prop. 5.8 / T7). Then: the entry is unique, namely type \((2,3)\) with poles \((1,1,2)\oplus(1,2,3)\); single-pole is excluded by the prime TDU theorem; all-\(b=1\) is empty; every cell of the §11a class-B/C book of that entry, over the filed budget-5 P0 closure, dies at the tower tier. A charged step outside that closure is classified as a §11a under-enumeration, never silently covered (`TOWER-UNIFORM.md:52-53`).

This is a **filed-book theorem for the unique \(td=7\) off-axis entry**, plus two independent entry-layer exclusions (single-pole prime, on-axis empty). It is **not** an unconditional “no \(td=7\) counterexample” theorem. The distance from the filed-book theorem to a true panel is exactly the claim that the filed closure exhausts the unique entry. That claim is stronger than generic P5 (the closure is finite, the inversion is cap-free, \(\nu\le 400\) is empty of extras) and is still a perimeter hypothesis.

### \(td=11\)

**Promoted theorems, as written.**

- Entry-clash at the exact-core tier (`TOWER-TD11.md` status banner; `AUDIT.md:756-771`): the three L6 entries, direct hierarchies, single-word-deep configurations, audited budget-9 cores. OPEN residue named.
- Nested 129 CLOSED-AT-TIER (`AUDIT.md:773-783`; `TOWER-TD11.md:650-693`).
- Conditional emptiness of the audited class-B/C layer, 411-row quotient, on FC1–FC7 (`AUDIT.md:785-799`; `xmodel/sol-census-final.md` EARNED). After later discharges (`TOWER-TD11.md:711-720`) the residual wall is FC1-R + FC3 (refile).

**What Gap 4 demotes.** Any reading of the above as “the \(td=11\) panel is closed” or “the \(td=11\) census is complete.” Sol's 159-row / BROKEN citation is the wrong instrument for this demotion — the later certificate is already *conditional* and already *not a panel*.

**Honest scope.**

> There is no certified complete census of all \(td=11\) sheet configurations. What is promoted is (i) an entry-clash theorem on the exact-core / single-word-deep / direct-hierarchy slice; (ii) a nested-skeleton death-at-tier theorem; (iii) a **conditional emptiness certificate** for an instrument-backed quotient of the audited class-B/C layer, contingent on the named fail-closed classes, of which beyond-core (FC1-R) and the Q+E5/E5F refile (FC3) remain the wall. Configurations outside that layer — beyond-core charged strata, unrefiled Q+E5/E5F realizations, and any entry not in the three L6 packets — are not covered.

This is a **layer-relative / certificate-conditional** statement, not a panel statement and not a book-landing theorem.

### On-axis composite books (\(d=6,8,9,10,12,14\))

Unchanged by Gap 4's off-axis clause, and already demoted by Sol's local-vs-full-config distinction (Gap 4 first half, CRITICAL 6). `TEMPLATE-ATTACK.md` §§2–3 survivors are local/template cells inside the modeled perimeter. Residue-A survives in every nonempty modeled panel. Closing those cells would still leave composite single-pole and off-axis sectors.

### What is *not* in the blast radius

- T5 / Żołądek 6.12.
- T2 / GGV Cor. 5.21 (existential).
- T4 as Aut-invariance of \(td\).
- T7's finite entry menu at fixed \(d\).
- T8 / DEPTH local marked-event landing on the all-\(b=1\) axis.
- TDU prime single-pole exclusion.
- The 17-cell tower kill *as a kill of those 17 cells*.
- Paper 1's strip/ODE theorems (they never claimed the sequential chain).

---

## Claims in `REDUCTION.md` that are themselves stale or too strong

These are the audit's own defects. They do not rescue the sequential chain.

1. **§4 item 8 and ledger 2.4 on \(td=11\).** “No certified complete census; universal certificate broken; nested and multi-word remain open.” Broken-as-of-`sol-census-review.md`, not as-of-2026-08-16. Nested and multi-word were subsequently closed at tier. A conditional 411-row certificate was promoted. Rewrite to the `AUDIT.md` 2026-08-15 sentence.
2. **CRITICAL 5 headline vs P5 body.** Headline: “the off-axis sector has no completeness theorem.” Body: P5 for the generic grid, plus a special \(d=7\) inversion. Keep P5; do not let the headline erase §11a.
3. **\(B_{\mathrm{GGV}}=\gcd(\deg P,\deg Q)\).** GGV's \(B\) is \(\gcd(v_{1,1}(P),v_{1,1}(Q))\).
4. **“Three different objects are called books” is right; “no completeness statement Sol missed” is not.** The completeness statements sit in the files Sol cites. He cited them for the special \(d=7\) case and then under-weighted them; he cited a superseded \(d=11\) review and skipped the next-day promotion.

---

## Bottom line

Sol's executive verdict is the right campaign-level sentence:

> There is no unconditional theorem sending an arbitrary planar Keller counterexample to a configuration in a currently enumerated book \(B(td,\mathrm{entry})\).

The five-point residual is the right residual once point 4 distinguishes the generic P5 grid from the unique-\(td=7\) filed book and from the \(td=11\) conditional layer. Gaps 1, 2, and 5 are breaks in the *sequential* architecture, not in the two lanes taken separately. Gap 4 is a break in any *universal book-landing* claim and is not a break in the promoted td-7 filed-book theorem or in the promoted td-11 conditional-layer certificate. Those two results were never honest panel closures; Gap 4 is what makes that unignorable.

No other repo file modified. No git.
