# paper2/SCOPE.md — two candidate tables of contents for paper 2, with a recommendation

Date: 2026-08-14, **rev 2 (post-priority-search reshape)**. Sources read:
paper1/main.tex (v2, thm:ode + thm:R absorbed), MATHIEU.md (+ promotion header),
TOWER-UNIFORM.md (STATUS + theorem), README.md, AUDIT.md tail (H5a, lift
retirement, 729 re-emission, four tower kills, panel closure), BOOK-OFFAXIS.md
§11/§11a, CERT-UPGRADE.md, phase0-email-draft.md (GGV thread timing), and
**paper2/PRIORITY.md** (literature priority search, 2026-08-14). Nothing
committed; SCOPE.md and PRIORITY.md are the only artifacts in paper2/.

## 0. Two scoping facts both ToCs must manage

### 0.1 Priority (PRIORITY.md — the controlling fact)

Theorem A's **content is prior art**: Żołądek 2008 (Topology 47, 431–469 —
already in refs/, and already in paper 1's bibliography for the degree bound),
Appendix Lemma A.7, Liouville-credited ("The following results were probably
known already to Liouville"), reaches Theorem A in two lines plus the trivial
perfect-power case: AC′ − wA′C = c ⟹ (C/A^w)′ = c/A^{w+1} ⟹ ∫dy/A^{w+1}
rational (hence Darboux) ⟹ A.7 forbids ≥ 2 distinct roots; a perfect power
dies by evaluating at its root. Żołądek moreover uses the **same ODE inside
the plane JC** (Lemma 3.9/(3.14): ϕψ′ − δϕ′ψ = −1/p in a Newton–Puiseux
chart, §6's "cannot be Darbouxian by Lemma A.7" kill). The w = 1 case is
separately published verbatim (Hermoso–Alcázar, arXiv 2410.18867, Thm 4,
n = 2). Corollary E's *content* is likewise a 2-line corollary of A.7 and
must be cited as such.

House style from here on: the statement is **"the Żołądek–Liouville
rigidity"**; our DvdK-mechanism 4-step proof survives as a remark-length
second proof (integration-free, never leaves F[y], and it — not the Darboux
route — yields the char-p boundary p > (k+1)d2).

Still novel per the search (PRIORITY.md §1.3): the displayed **ODE-pair
formulation** and the integration-free proof; the **char-p boundary**;
**Lemma B** (block ⟺ ODE) and the strip-uniformity consequence (Cor C/D =
paper1 thm:R); **Corollary E as a stated dichotomy**; the **bridge theorem /
M_A codimension-δ structure**; **SC1** (no image-of-(A∂ − kA′) results
anywhere in the univariate MZ corpus). Secondary pre-submission check:
Appelgate–Onishi 1985 / Nowicki–Nakai 1988 (paywalled; can add a citation,
cannot restore a novelty claim).

Collateral ledger corrections that must be folded wherever the MZ frame is
exposed (PRIORITY.md §3): **Mathieu's conjecture is FALSE for SU(2)** (Long,
arXiv 2607.19012) and the **Gaussian Moments Conjecture is FALSE for n ≥ 3**
(Long, arXiv 2607.18186); DvdK (abelian) stands and is all our frame
consumes, but MATHIEU.md §1.3's "nonabelian case: open" line and any SC1
plausibility talk must be rewritten against both facts.

### 0.2 Overlap with paper 1 (+ the v3 rider)

Paper 1 v2 already contains the rigidity statement (thm:ode) and the former
conj:R (thm:R) with full proofs, and the 2026-08-14 GGV follow-up announces
"Thm 6.5". Thm 6.5 = thm:R (strip uniformity) — **still novel; nothing in the
email needs walking back**. But the engine now needs crediting: **RIDER —
paper 1 v3 must add, to thm:ode's remark (rem:sharp) and §functional's
prose, the citations Żołądek 2008 Lemma A.7 (+ Liouville attribution) and
Lemma 3.9/(3.14) (same ODE, same JC context), and Hermoso–Alcázar for
w = 1 — before any further GGV traffic.** GGV plausibly know Żołądek's paper
better than we did; v2 cites it three lines above the bibliography entry that
answers our own novelty question. Both ToCs below stay companions to
paper 1 with explicit mutual citation; do not trim paper 1's §6.

---

## 1. ToC A′ — "TIGHT, REBUILT" (~6–8 pages — a NOTE, not a paper)

Working title: *Mathieu subspaces from weighted derivations of C[y]: a
question, its power ledger, and an application of a lemma of Żołądek*.
Audience: Mathieu–Zhao community. The headline is no longer a theorem; it is
**SC1** — the first ≥3-puncture Mathieu question — carried by the
unconditional small results that survive the priority find (bridge/M_A
structure, Corollary E as stated dichotomy, char-p boundary), with Żołądek
A.7 cited as the engine throughout.

### Sections

**§1. Introduction (1 p.).** SC1 stated on page 1 as the exported question;
the engine credited (Żołądek A.7, Liouville); the provenance told honestly:
the campaign rediscovered the rigidity via the DvdK valuation mechanism while
proving a strip-uniformity theorem (paper 1), and the priority search that
found A.7 is part of the same verification culture. Post-Long framing: with
the nonabelian Mathieu conjecture now false for SU(2) and DvdK's abelian
theorem intact, the natural frontier is abelian-adjacent geometries — SC1 is
the (δ+1)-punctured line sitting one step past DvdK's torus.

**§2. The rigidity statement and its two proofs (1.5 pp).** Display:

> **Żołądek–Liouville rigidity.** Let F have characteristic 0, let w ≥ 1 be
> an integer, and let A, C ∈ F[y] satisfy A·C′ − w·A′·C = c for some
> constant c ∈ F, c ≠ 0. Then deg A ≤ 1. — content: Żołądek 2008, Appendix
> Lemma A.7 ("In the assumptions of Lemma A.6 one has that at least one
> ϑ_i ∉ Z"), via the two-line reduction of PRIORITY.md §1.2; w = 1 also
> Hermoso–Alcázar 2024, Thm 4.

Proof 1 = the two-line Darboux reduction (in-paper, with A.7 quoted). Proof 2
= **one remark-length paragraph**: the integration-free 4-step
leading-coefficient argument (MATHIEU.md §5.1) — genuinely a different proof
(no partial fractions, no rationality of primitives, stays in F[y]),
independently found, recorded because it alone gives the **char-p boundary**
(holds for p > (k+1)d2 in the block instance; fails honestly in small p,
consistent with Mondello's char-2 example).

**§3. The residue dichotomy (1 p.).** Corollary E as a stated dichotomy —
new as a statement, content credited to A.7 (A.4's condition (i) is literally
the residue functional):

> **COROLLARY E.** Let A ∈ C[y] be squarefree with deg A ≥ 2. Then for EVERY
> m ≥ 2 there is a root r of A with Res_r(A^{−m} dy) ≠ 0. (For m = 1 all
> residues 1/A′(r) are nonzero; for deg A ≤ 1 all residues of all powers
> m ≥ 2 vanish.) — MATHIEU.md §5.3; content ⟸ Żołądek A.7 in 2 lines.

Positioned as the multi-puncture analogue of the DvdK 1-D support dichotomy.

**§4. M_A and the Mathieu question (2 pp).** The note's own mathematics:

> **BRIDGE THEOREM** (MATHIEU.md §3, in-paper in full): (a) no element of
> M_A = Im(A∂ − kA′) has y-degree (k+1)δ − 1, so M_A ⊊ C[y]; (b) for
> squarefree A, M_A = ∩_{i=1}^δ ker(f ↦ Res_{r_i}(f·A^{−(k+1)}dy)), of
> codimension exactly δ; (c) if M_A is a Mathieu subspace then 1 ∉ M_A;
> (d) Mathieu-ness for 2 ≤ deg A ≤ d2 implies the rigidity half at (k, d2).

> **SUB-CONJECTURE SC1.** (a) Polynomial form: for every A ∈ C[y] squarefree
> with deg A = δ ≥ 1 and every k ≥ 1, M_A = Im(A∂ − kA′) =
> ∩_{i=1}^δ ker(f ↦ Res_{r_i}(f A^{−(k+1)}dy)) is a Mathieu subspace of
> C[y]. (b) Localized form: Im(d/dy) = ∩_i ker Res_{r_i}(· dy) is a Mathieu
> subspace of C[y, 1/A]. — MATHIEU.md §6

With: Corollary E as SC1's **complete power ledger** (for δ ≥ 2 no power of
1/A lies in M; for δ = 1 all powers m ≥ 2 do and the Mathieu conclusion holds
explicitly); the honest eventual-vs-every-power discussion (why MZ theorems
alone could never prove rigidity); the post-Long plausibility paragraph
(nonabelian Mathieu statements now have counterexamples — SC1's evidence is
abelian-side and per-power, and a counterexample to SC1 would be interesting
in its own right and would damage nothing upstream, since rigidity stands on
A.7).

**§5. Application: strip uniformity (1 p.).** Lemma B displayed (in-paper
proof, it is short); thm:R quoted and **cited to paper 1** (its proof lives
there); one paragraph on what uniformity settled ((3,4),(4,4),(5,4), all
d2 ≥ 5; certificates → corollaries) and the (72,108) connection; one sentence
noting Żołądek's Lemma 3.9 reaches the same ODE from Newton–Puiseux charts —
Lemma B is an independent second route from the GGV polygon side.

**§6. Verification and provenance (0.5 p.).** M1–M5 exact checks
(corroboration only), MATHIEU-REVIEW chain, PRIORITY.md as artifact, DOI.

References (~0.5 p.): Żołądek; Hermoso–Alcázar; DvdK; Zhao (2010, 2012);
van den Essen–Wright–Zhao; van den Essen–Zhao (JPAA 2013, 2016); Long (both
2026 counterexample papers); Muzychuk–Pakovich; Magnus 1955 (genre ancestor);
GGV 1310.8249 (bracket→ODE mechanism); paper 1; Mondello.

### Proven in-paper vs cited (ToC A′)

| item | status |
|---|---|
| Rigidity via A.7 (2-line reduction + perfect-power line) | **in-paper**, content cited to Żołądek/Liouville |
| Integration-free second proof + char-p boundary | **in-paper** (one remark) |
| Corollary E statement + partial-fractions reduction | **in-paper**, content cited to A.7 |
| Bridge theorem (a)–(d), codim-δ structure | **in-paper** (novel) |
| SC1 + power ledger + post-Long discussion | **in-paper** (novel question) |
| Lemma B | **in-paper** (novel) |
| thm:R (strip uniformity) | cited to paper 1 |
| M1–M5, review docs, PRIORITY.md | cited to artifact |
| Appelgate–Onishi / Nowicki–Nakai exact lemma forms | **open pre-submission check** (secondary) |

### Honest standalone assessment

**A′ is a NOTE (6–8 pp), not a paper.** Its only theorem-grade novelties are
the bridge/codimension structure (small), a statement-level dichotomy, a
second proof, and a char-p remark; the headline is a well-posed conjecture
with a complete evidence ledger. That **clears the arXiv-note bar and is
genuinely timely** (the MZ field is re-examining foundations post-Long, and
SC1 is now findable by anyone who reads Żołądek's appendix with MZ eyes — a
planting argument for posting sooner rather than later). It does **not**
clear the bar of a standalone journal *paper*; realistic journal fate is a
short-communications venue, or absorption into B. Referee attack order:
(1) "a citation plus a conjecture" — answered only by the framing above;
(2) "the bridge is elementary" — true, it is structure, not depth; (3) SC1
plausibility post-Long — answered in §4. arXiv: **math.AC primary, math.AG
cross-list** (the MZ audience is the point; endorsement caveat: if the
account's chain is math.AG-only at posting time, flip primary/cross).

---

## 2. ToC B — "FULL ARC" (~28–32 pages) — now the headline candidate

Working title: *Obstruction panels for the plane Jacobian Conjecture: a
rigidity lemma, the off-axis td-7 book, and a machine-verified panel closure*.
Audience: JC specialists + computational algebra. Promoted genome only.

**Reassessment after the priority find: B's standing is unchanged-to-improved.**
B's headline was always the td-7 closure + the methodology, and none of it
touches the rigidity's novelty: the zero-chain law, the E5-corrected census,
the tower uniformity theorem, and the verification culture are the campaign's
own. The citation folds in cleanly — "the Żołądek–Liouville rigidity" becomes
the engine's name throughout, §2 shrinks to statement + citations, and the
Lemma 3.9 connection actively *strengthens* the arc (the same ODE was already
a plane-JC workhorse in Żołądek's chart analysis; the campaign's Lemma B
reaches it independently from the GGV polygon side and then makes it uniform
in (k,d2)). The priority episode itself becomes a §9 exhibit: the
retraction-honest culture audits novelty claims with the same discipline as
proofs, and caught this one pre-submission from the repo's own refs/ folder.

### Sections

**Part I — the rigidity engine.**

**§1. Introduction (2.5 pp).** The campaign shape: GGV reduction → (72,108)
settled → the structural avenues; what a "panel closure" is; the two closed
panels (td ≤ 5, td = 7); the honesty perimeter declared up front (formal-tier
obstruction over a filed route perimeter, trust set explicit). Plane-JC
framing throughout, with the 2026 wave (JC false for all n ≥ 3; the 2-D case
open) cited as motivation for 2-D structure results.

**§2. The Żołądek–Liouville rigidity and strip uniformity (2.5 pp).**
Statement + citations (Żołądek A.7/Liouville; Lemma 3.9/(3.14) as the prior
plane-JC appearance of the same ODE; Hermoso–Alcázar for w = 1); thm:R
quoted with proof cited to paper 1 (and the A′ note, if it exists); why one
rigidity lemma is the homogeneous engine at every weight (depth-D columns,
w = k+D−1).

**Part II — the sheet-6 obstruction framework (promoted genome).**

**§3. The obstruction genome (5 pp).** Entries, chains, charges, multiplicity
law (St 8.4 l | M), budgets and the priced closure at budget 5; the Sigray
trust set declared as named hypotheses (Prop 4.2 ladder/delta descent/alive
dichotomy, Prop 8.1(i)–(v), Cor 6.1, St 8.3(i)+Not 4.1, St 3.9/3.17(i)/
3.11(i)); the errata culture: E1–E10 disclosed, and the H5a repair proved,
not assumed:

> **H5a resolution (AUDIT.md 2026-08-13).** The Notation 3.5 gap at doubly
> realized vertices is resolved at proof tier: the P/coarse reading is
> incoherent (nonintegral D_{h,F} against printed Stmt 3.8; conflict with
> Prop 5.5), so Q/jump/max κ_F = ν_F κ_G / ν_G is the unique uniform repair,
> and Q + printed Stmt 3.17(ii) + Prop 9.3(e) force the E5 transport
> identities. (xmodel/sol-h5a.md; hostile replay SOUND incl. printed-page
> verification, xmodel/grok-h5a-review.md.)

**§4. The generalized zero-chain law (3 pp).** Statement + in-paper proof
(reduced equation from R1.0; both iff directions); effect 62 → 6.

> **Zero-chain law (BOOK-OFFAXIS.md §11, PROMOTED).** With μ = d_p − ν and
> l = (d_q − 1)/ν − 1, the cell's reduced equation admits an admissible
> solution with nonzero RHS constant iff d_p does NOT divide d_q;
> equivalently the cell is T1-DEAD iff
> d_p | d_q ⟺ (μ+ν) | (μ(l+1) − 1) ⟺ M = d_p ⟺ κ̄ ∈ {3,4}.
> On-axis ZCH (ν+1) | l is the μ = 1 specialization.

**§5. The E5-corrected census (4 pp).** The κ̄ pin (I4) with ν_G (not ν_U);
the cap-free (I5a)–(I5d) inversion (no guessed cap); class-B emptiness proved;
the 17-cell table (BOOK-OFFAXIS §11a, reproduced); the two-readings honesty
(forced-ν 2-cell sub-book; both books recorded); completeness gates G1–G5 and
the brute-force sweep.

> **Census (BOOK-OFFAXIS.md §11a, PROMOTED; hostile review SOUND,
> brute-force completeness ν ≤ 400, 0 miss / 0 extra).** Under promoted
> H5a/Q-value + E5: 17 cells, 238 raw routes (202 at equality), 233
> deduplicated (197 eq). Class B is EMPTY even pre-T1.

**Part III — the tower closure.**

**§6. The tower tier and the panel-constant clash (3 pp).** Prop 4.2
approximate-root ladders; the panel constants (level 0 = (2,3), α₁ = 3/2,
pole death gap 5/2; chain-1 frozen at (μ,w,M) = (1,2,1)); the
X/first-charged clash and the universal ν_X ≥ 2 three-case refutation +
N1–N4 insertion closure.

**§7. The four lemmas (4 pp).** In-paper proofs of L-A (chain-1 freeze,
budget-independent), AM (absorbing M = 1; first-charged menu = {(A),(C)}),
WIN in the review-corrected budget-admissible form (ingredients (i′)–(v))
with TERM, and E5F with its closed forms:

> **Lemma E5F (TOWER-UNIFORM.md).** A recorded arrival vertex (ν_U, κ̄_U) of
> a cell (κ̄_G, ν_G) is E5-realizable iff n = ν_U κ̄_G − ν_G κ̄_U ≥ 1
> (printed (h′) positivity; the congruence is automatic).

**§8. The uniform theorem and the witness table (3 pp).** The theorem
verbatim; the frozen 16-row table with the per-row premise checklist; the
stress realizations (self-return, composite insertion); the
what-is-NOT-claimed section verbatim from TOWER-UNIFORM §4.

> **Theorem (td-7 tower uniformity; TOWER-UNIFORM.md, PROMOTED 2026-08-14).**
> Every cell of the E5-corrected td-7 class-B/C book dies at the tower tier.
> Precisely: for each of the 17 cells of the promoted §11a census (238 raw /
> 233 deduplicated routes), no realization of any filed completion route —
> over all recorded arrivals and their M_U classes, all free characteristics,
> all neutral padding, all zero-cost insertions at eligible states, all
> terminals, and rerouting of E5-refuted arrival vertices through their legal
> pads — admits a global Prop 4.2 approximate-root ladder: level 1 of every
> ladder is obstructed by the X/first-charged clash. Class B is empty before
> this tier (§11a). Hence the td-7 off-axis book is EMPTY at the tower tier.

**Part IV — methodology.**

**§9. Verification methodology (4.5 pp).** The novel exposable content: (i)
dual/triple cross-model adversarial review, with the (9,15) kill as the
worked example (Grok SOUND-WITH-ERRATA → Case C repair → Sol BROKEN →
M_U=4/free-char extension → Sol STILL-BROKEN → N1–N4 closure → Sol
CONFIRMED-KILL; seven passes, three model families, 14 errata folded, no
cell resisted); (ii) machine gates as promotion criteria (1559/1559, exact
Fractions, no floats, live-mutation negative controls); (iii) certificate
culture via the CERT-UPGRADE vignette — the honest DEAD verdict on
prime-size certification (5×10⁹-digit primes for the smallest toy; no
theorem can undercut the d^Θ(n) shape) next to the live extraction lane:

> **The 2-row certificate (CERT-UPGRADE.md §2.4).** All four conjE B-subset
> systems share byte-identical nonzero cofactors, dividing by t² to
> (f1n0 − f1n1)² = f13 + w·f21,
> w = −(g2n0−g2n1)²(f2n0−f2n1) − 2(g2n0−g2n1)(f1n0−f1n1) − (g1n0−g1n1)(f2n0−f2n1):
> the square of the P1-difference lies in the ideal (f13, f21) — a 2-row
> emptiness core, integral, height log 2, verified in an independent engine —
> upgrading msolve EMPTY verdicts to unconditional char-0 theorems.

(iv) the retraction ledger as a feature (lift retirement under the
last-chance rule; the 729-row re-emission with why no verdict flips; the
msolve parenthesis and mod-p reduction hazards with the 401-file audit); and
now (v) **novelty audit**: the Theorem-A priority search (PRIORITY.md) as
the same discipline applied to claims of newness — found from the repo's own
refs/, pre-submission, and folded into the record rather than around it.
Framed as engineering that supplements, never replaces, proofs and human
refereeing.

**§10. Open problems (1 p.).** td-11/13 refile + tower port; U_7C; the
coefficient-gluing tier; depth ≥ 3; SC1 (one paragraph, post-Long-corrected
— expanded here if the A′ note is not published separately).

Appendix (1.5 pp): reproduction commands (`tower_check.py`,
`td7_census_e5.py`, `book_offaxis.py`), gate inventories, artifact DOI.

### Proven in-paper vs cited-to-artifact (ToC B)

| item | status |
|---|---|
| Żołądek–Liouville rigidity | **cited** (Żołądek A.7/Liouville; Hermoso–Alcázar w = 1); statement displayed |
| thm:R strip uniformity | cited to paper 1 (/ A′ note) |
| H5a incoherence-of-P + uniqueness-of-Q | **in-paper** (sketch with thesis page cites; full proof cited to xmodel/sol-h5a.md) |
| Zero-chain law, both iff directions | **in-paper** |
| Class-B emptiness; N1 bite (4 cells) | **in-paper** |
| Census enumeration (17 cells, 238/233, cap-free inversion, ν ≤ 400 sweep) | cited to artifact (`cases/td7_census_e5.py`, gates G1–G5) |
| Panel-constant clash + universal A/B/C + N1–N4 | **in-paper** |
| Lemmas L-A, AM, WIN(+TERM), E5F | **in-paper** |
| 16-row witness table + stress realizations | cited to artifact (`cases/tower_check.py`, 1559 gates; table reproduced in-paper) |
| Four per-cell certificates | cited to artifact (cases/towers/ + review docs) |
| Sigray Prop 4.2/8.1/St 8.4/etc. | cited external, declared as hypotheses, errata disclosed |
| 2-row Nullstellensatz certificate | **in-paper** (verbatim, 5 lines) |

### Page estimate: **28–32 pages** (within the 25–35 band).

### Referee risk (hostile referee's attack order — updated)

1. **The Sigray trust set.** "A 30-page tower on an unpublished 2008 thesis in
   which you yourselves catalogued errata E1–E10 and an incoherent notation."
   Pre-empt in §1 and §3. Point to: the H5a proof-tier resolution with
   printed-page hostile replay; the forced-ν 2-cell sub-book killed
   unconditionally across coherent readings; U_7C moot for td-7; every import
   a named hypothesis in the theorem's perimeter sentence. Residual honest
   exposure: conditional architecture — say so in the abstract.
2. **Census completeness.** "Why no 18th cell?" Point to: cap-free inversion
   (no guessed bound), closure-forced termination of the 2/(2k+1) family,
   brute-force ν ≤ 400 (0 miss / 0 extra), gates G1–G5, census-audit-class
   note (n ≥ 1 filter).
3. **WIN's quantifier closure.** "242 path-states is a sample." Point to: Sol
   finding 3 — closure is by lemma ingredients (i′)–(v), enumeration is
   corroboration; the raw-menu 5/2 outlier and its budget block displayed.
4. **Machine-gate opacity.** "I cannot referee 1559 checks." Point to: §9's
   design — named gates, exact arithmetic, negative controls, 4-second local
   reproduction, and the certificate vignette showing machine verdicts get
   upgraded to hand-checkable identities wherever feasible.
5. **"AI reviewed AI."** Point to: adversarial review across model families
   with preserved failure history (BROKEN verdicts kept and answered);
   presented as discipline supplementing human refereeing; the retraction +
   novelty-audit ledger as evidence the process bites against the authors'
   own interests.
6. **Priority of Part I** — now defused by construction (the engine is cited,
   not claimed; the find is disclosed in §9(v)).
7. **Obsolescence/downgrade (internal):** TOWER-UNIFORM is PROMOTED *pending
   coordinator ledger pass*, and td-11/13 refile + tower port is launching —
   the story may strengthen (multi-panel) or shift while B is written.

### arXiv category

**math.AG primary, cross-list math.AC and cs.SC** (the methodology section is
genuine symbolic-computation content; cs.SC signals the §9 audience).

---

## 3. Recommendation (revised after the priority find)

**A′ verdict: NOTE (6–8 pp).** It clears the arXiv-note bar — SC1 is new,
timely post-Long, and now findable by anyone reading Żołądek's appendix with
MZ eyes — but not the standalone journal-paper bar. **ToC B is now paper 2.**

Order of work:

0. **Paper-1 v3 citation rider — immediately, before any GGV reply lands.**
   Add Żołądek A.7 (+ Liouville attribution) and Lemma 3.9/(3.14) to
   thm:ode's remark and §functional's prose; add Hermoso–Alcázar for w = 1;
   soften any language claiming the rigidity phenomenon itself. Thm 6.5
   (thm:R) remains novel — the follow-up email needs no correction, only the
   engine needs crediting. This is reputationally urgent: v2 already cites
   Żołądek for the degree bound, so the omission is conspicuous to exactly
   the readers who have the paper in hand.
1. **Paper 2 = ToC B**, the only candidate carrying headline-grade novelty.
   Gates unchanged: (i) TOWER-UNIFORM coordinator ledger pass, (ii) td-11/13
   verdict or a ~4–6-week timeout, whichever first. Start drafting Parts
   II–IV now — they are independent of both gates except §8's final numbers,
   and if td-11/13 closes, B upgrades to a multi-panel sheet-ladder paper
   (Part II/III structure already accommodates it).
2. **A′ note: write this week, as a 2–3-day byproduct, not blocking B** —
   it plants SC1 with its power ledger before anyone else connects A.7 to
   Mathieu subspaces, gives the deferred endorsement flow a second short,
   unconditional, integrity-forward artifact, and shrinks B's §10. If DC
   prefers zero extra surface while GGV correspondence is live, the fallback
   is fold-into-B (§10 grows ~1 p.) at no mathematical cost — the note is
   opportunistic, not load-bearing.

Required pre-submission checks: Appelgate–Onishi 1985 / Nowicki–Nakai 1988
exact lemma forms (secondary, citation-only); MATHIEU.md §1.3 ledger
corrections (Long ×2) folded into any exposed MZ prose (A′ §4, B §10).
