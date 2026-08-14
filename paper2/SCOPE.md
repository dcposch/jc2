# paper2/SCOPE.md — two candidate tables of contents for paper 2, with a recommendation

Date: 2026-08-14. Prepared for DC after paper-2 green-light. Sources read:
paper1/main.tex (v2, thm:ode + thm:R absorbed), MATHIEU.md (+ promotion header),
TOWER-UNIFORM.md (STATUS + theorem), README.md, AUDIT.md tail (H5a, lift
retirement, 729 re-emission, four tower kills, panel closure), BOOK-OFFAXIS.md
§11/§11a, CERT-UPGRADE.md, phase0-email-draft.md (GGV thread timing).
Nothing committed; this file is the only artifact in paper2/.

## 0. A scoping fact both ToCs must manage

Paper 1 v2 **already contains Theorem A** (as `thm:ode`, stated with ν) and the
former conj:R (as `thm:R`), with full proofs, and the 2026-08-14 follow-up email
to GGV announces exactly that upgrade ("Thm 6.5 in the attached v2"). So paper 2
cannot be "the paper where Theorem A first appears"; it must be the paper where
Theorem A gets the treatment paper 1 has no room for. What paper 1 does NOT
contain, and paper 2 owns outright: the Mathieu–Zhao frame (bridge theorem,
1 ∉ M_A), Corollary E (the residue dichotomy), sub-conjecture SC1, the honest
theorem-vs-conjecture ledger of the MZ literature — and, on the ToC-B side, the
entire sheet-6/td-7 panel apparatus and the verification methodology. Both ToCs
below are framed as **companions to paper 1 with explicit mutual citation**
(paper 1 compresses; paper 2 develops). Do not trim paper 1's §6 retroactively —
that version is already in GGV's hands.

---

## 1. ToC A — "TIGHT" (~10–12 pages)

Working title: *A rigidity theorem for the weighted derivation identity
AC′ − wA′C = c, with an application to strip pairs in the plane Jacobian
Conjecture*. Audience: Mathieu–Zhao / affine-algebraic-geometry readers; the JC
application is the showcase, not the load. Everything proved in-paper;
computation appears only as corroboration.

### Sections

**§1. Introduction (1.5 pp).** Theorem A on page 1; what it settles (the former
conj:R, uniformly at every cell k, d2 ≥ 2); one paragraph each on the DvdK
mechanism, the Mathieu–Zhao program, and the (72,108)/paper-1 provenance
(the theorem was found by transporting the DvdK valuation argument to a strip
obstruction problem, not by browsing for ODE lemmas). Companion-note framing
stated here.

**§2. The rigidity theorem (2 pp).** The four-step elementary proof
(leading-coefficient lemma; deg C = wδ pin; kernel element A^w; subtract at top
degree), sharpness (A = 1 + a2y, C = ((1+a2y)^w − 1)/(wa2)), the
valuation-at-infinity reading (DvdK-1D made elementary, no Riemann–Hurwitz),
and the characteristic-p boundary (holds for p > (k+1)d2 in the block instance;
fails honestly in small p, consistent with Mondello's char-2 example).

Main statement, verbatim from MATHIEU.md §5.1 (promoted 2026-08-12,
MATHIEU-REVIEW.md all six fronts CONFIRMED; = paper1 thm:ode with w for ν):

> **THEOREM A (rigidity, all weights).** Let F have characteristic 0, let
> w ≥ 1 be an integer, and let A, C ∈ F[y] satisfy A·C′ − w·A′·C = c for some
> constant c ∈ F, c ≠ 0. Then deg A ≤ 1.

**§3. Strip pairs and the uniformity theorem (3 pp).** Compressed strip setup
(Definition, vertex normalization, block; full details cited to paper 1);
Lemma B in-paper; the outer lemma reproved in-paper via the local residue
pairing (paper1 lem:outer's proof is 15 lines — reproduce, don't cite); the
uniform theorem; the settled-cells ledger ((2,2) pinning; (2,3)/(2,4)
divisibility halves; the (3,3),(4,3),(5,3) resultant certificates; the
formerly OPEN (3,4),(4,4),(5,4) and all d2 ≥ 5); one paragraph on GGV
coverage at degree ≤ 150 and the (8,28) client.

Statements to display, verbatim:

> **LEMMA B (block ⟺ ODE).** Fix k ≥ 2, d2 ≥ 2 and a point
> a = (a2,…,a_{d2+1}), A = 1 + Σ_{i≥1} a_{i+1}y^i. The d2 − 1 inner extras of
> the depth-2 block vanish at a if and only if there exists C ∈ F[y] with
> support in {y,…,y^{kd2}} such that (ODE) A·C′ − k·A′·C = 1.
> — MATHIEU.md §3

> **COROLLARY C (rigidity half, ALL cells).** For every k ≥ 2, d2 ≥ 2, over
> any field of characteristic 0: the inner extras of the depth-2 block vanish
> at a = (a2,…,a_{d2+1}) iff a3 = … = a_{d2+1} = 0. Equivalently
> V(inner extras) = {A binomial}: the inner column forces deg A ≤ 1.
> — MATHIEU.md §5.2

> **THEOREM (log-residue description of the block variety; former conj:R).**
> For every k ≥ 2, d2 ≥ 2, and every reduced strip pair of type (k,d2)
> satisfying (i), over a field of characteristic zero, the variety of the
> extra keys of the depth-two block is
> V(extras) = {A binomial} ∩ ({a2 = 0} ∪ {R_{k,d2} = 0}),
> where "A binomial" means a_{(1,i)} = 0 for 2 ≤ i ≤ d2.
> — paper1 thm:R (= MATHIEU.md Corollary D), with
> R_{k,d2} = Σ_{j=max(k+2,d2)}^{2d2} (−1)^j C(j,k+2) a2^{2d2−j} b_j.

**§4. The residue dichotomy and the Mathieu–Zhao frame (2.5 pp).** Corollary E
with its partial-fractions proof; the bridge theorem (properness of M_A =
Im(A∂ − kA′); the codimension-δ residue description; "Mathieu ⟹ 1 ∉ M_A");
the honest ledger: why DvdK applies literally-but-vacuously on the outer
(binomial-locus torus) side, why the inner side lives on a (δ+1)-punctured
line outside every proved MZ instance, and why MZ theorems alone could never
finish (eventual vanishing vs every-power); SC1 stated as the paper's exported
conjecture — the first ≥3-puncture Mathieu question, with Corollary E as its
complete power ledger.

Statements to display, verbatim from MATHIEU.md:

> **COROLLARY E.** Let A ∈ C[y] be squarefree with deg A ≥ 2. Then for EVERY
> m ≥ 2 there is a root r of A with Res_r(A^{−m} dy) ≠ 0. (For m = 1 all
> residues 1/A′(r) are nonzero; for deg A ≤ 1 all residues of all powers
> m ≥ 2 vanish.) — §5.3

> **BRIDGE THEOREM** (parts (a)–(d): no element of M_A has y-degree
> (k+1)δ − 1, so M_A ⊊ C[y]; for squarefree A, M_A = ∩_i ker μ_i of
> codimension exactly δ, μ_i(f) = Res_{r_i}(f·A^{−(k+1)}dy); if M_A is
> Mathieu then 1 ∉ M_A; hence Mathieu-ness for 2 ≤ deg A ≤ d2 implies the
> rigidity half at (k, d2)). — §3, displayed in full in-paper

> **SUB-CONJECTURE SC1.** (a) Polynomial form: for every A ∈ C[y] squarefree
> with deg A = δ ≥ 1 and every k ≥ 1, M_A = Im(A∂ − kA′) =
> ∩_{i=1}^δ ker(f ↦ Res_{r_i}(f A^{−(k+1)}dy)) is a Mathieu subspace of
> C[y]. (b) Localized form: Im(d/dy) = ∩_i ker Res_{r_i}(· dy) is a Mathieu
> subspace of C[y, 1/A]. — §6

**§5. Verification and provenance (1 p.).** Paper-1-style culture note: exact
arithmetic checks M1–M5 (`cases/residue_check.py mathieu`, exit 0) as
corroboration never load-bearing; the adversarial review chain
(MATHIEU-REVIEW.md); AI-assistance statement in the paper-1 form; artifact DOI.

References (~0.5 p.): DvdK; Zhao (JPAA 2010, J. Algebra 2012); van den
Essen–Wright–Zhao; Muzychuk–Pakovich; paper 1; GGHV; Mondello.

### Proven in-paper vs cited-to-artifact (ToC A)

| item | status |
|---|---|
| Theorem A (4-step proof) | **in-paper** |
| Lemma B, both directions incl. kernel uniqueness | **in-paper** |
| Outer lemma (residue-pairing evaluation of the lowest outer extra) | **in-paper** (reproduce paper1 lem:outer) |
| thm:R / Corollary D assembly | **in-paper** |
| Corollary E, Bridge Theorem (a)–(d) | **in-paper** |
| M1–M5 exact checks, per-cell certificates (15,12)/(26,34)/(40,44) | cited to artifact (corroboration) |
| Strip setup, gap kill, Props A/B, coverage table | cited to paper 1 |
| MZ literature ledger | cited external — **flag: MATHIEU.md §1.3 is from-memory with confidence labels; a real pre-submission literature check is a required task** |

### Page estimate: **10–12 pages.**

### Referee risk (hostile referee's attack order)

1. **"Theorem A is known/folklore."** The single biggest risk: a 15-line
   elementary statement about AC′ − wA′C = c invites a priority hunt
   (Darboux-polynomial literature, polynomial first-order ODEs, Wronskian
   rigidity, van den Essen's book). Mitigation: do the literature sweep BEFORE
   submission (MATHIEU.md's ledger is explicitly no-web, from-memory); frame
   honestly ("elementary, possibly known in other clothing; the contributions
   are the uniform block consequence, Corollary E as the multi-puncture
   DvdK-1D, and SC1"). Point the referee to: the sharpness example, the
   self-contained proof, and Corollary E, which we have not seen stated anywhere.
2. **"Lemma B is where the substance hides."** Point to: full in-paper proof,
   the independent lattice-determinant cross-check, and M5 symbolic ties at 9
   cells including every historically dangerous perfect-power point.
3. **"This is your other paper again."** Point to: the companion framing in §1;
   the disjoint content list of §0 above (bridge/Corollary E/SC1 appear only
   here; the strip apparatus appears only there).
4. **"A conjecture (SC1) is not a result."** Point to: SC1 is the exported
   question, carried by the unconditional Corollary E and the codimension-δ
   structure theorem; the paper stands with §4 read as results-plus-question.
5. **Outer-half provenance** (RESIDUE.md §4b chain S1–S5): defused by reproving
   lem:outer in-paper; no inheritance from unpublished notes.

### arXiv category

**math.AG primary, math.AC cross-list.** Content-wise math.AC (Mathieu
subspaces) is defensible as primary, but the endorsement chain runs through
the GGV correspondents (math.AG for paper 1); keeping one archive keeps one
endorsement. Flip to math.AC primary only if an AC endorser materializes.

---

## 2. ToC B — "FULL ARC" (~28–32 pages)

Working title: *Obstruction panels for the plane Jacobian Conjecture: a
rigidity lemma, the off-axis td-7 book, and a machine-verified panel closure*.
Audience: JC specialists + computational algebra; also the first full
exposition of the campaign's verification culture. Promoted genome only: only
promoted/reviewed items enter (no RUNNING R1 screens, no two-pole branch work,
no retracted material).

### Sections

**Part I — the rigidity engine.**

**§1. Introduction (2.5 pp).** The campaign shape: GGV reduction → (72,108)
settled → the structural avenues; what a "panel closure" is; the two closed
panels (td ≤ 5, td = 7); the honesty perimeter declared up front (formal-tier
obstruction over a filed route perimeter, trust set explicit).

**§2. Theorem A and strip uniformity (3 pp).** Compressed restatement of
Theorem A + thm:R (cite paper 1 / paper 2A for proofs); why one rigidity lemma
is the homogeneous engine at every weight (depth-D columns, w = k+D−1).

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
the 17-cell table (from BOOK-OFFAXIS §11a, reproduced); the two-readings
honesty (forced-ν 2-cell sub-book; both books recorded); completeness gates
G1–G5 and the brute-force sweep.

> **Census (BOOK-OFFAXIS.md §11a, PROMOTED; hostile review SOUND,
> brute-force completeness ν ≤ 400, 0 miss / 0 extra).** Under promoted
> H5a/Q-value + E5: 17 cells, 238 raw routes (202 at equality), 233
> deduplicated (197 eq). Class B is EMPTY even pre-T1.

**Part III — the tower closure.**

**§6. The tower tier and the panel-constant clash (3 pp).** Prop 4.2
approximate-root ladders; the panel constants (level 0 = (2,3), α₁ = 3/2, pole
death gap 5/2; chain-1 frozen at (μ,w,M) = (1,2,1)); the X/first-charged clash
and the universal ν_X ≥ 2 three-case refutation + N1–N4 insertion closure.

**§7. The four lemmas (4 pp).** In-paper proofs of L-A (chain-1 freeze,
budget-independent), AM (absorbing M = 1; first-charged menu = {(A),(C)}),
WIN in the review-corrected budget-admissible form (ingredients (i′)–(v)) with
TERM, and E5F with its closed forms:

> **Lemma E5F (TOWER-UNIFORM.md).** A recorded arrival vertex (ν_U, κ̄_U) of
> a cell (κ̄_G, ν_G) is E5-realizable iff n = ν_U κ̄_G − ν_G κ̄_U ≥ 1
> (printed (h′) positivity; the congruence is automatic).

**§8. The uniform theorem and the witness table (3 pp).** The theorem verbatim;
the frozen 16-row table with the per-row premise checklist; the stress
realizations (self-return, composite insertion); the what-is-NOT-claimed
section verbatim from TOWER-UNIFORM §4.

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

**§9. Verification methodology (4 pp).** The novel exposable content: (i)
dual/triple cross-model adversarial review, with the (9,15) kill as the worked
example (Grok SOUND-WITH-ERRATA → Case C repair → Sol BROKEN → M_U=4/free-char
extension → Sol STILL-BROKEN → N1–N4 closure → Sol CONFIRMED-KILL; seven
passes, three model families, 14 errata folded, no cell resisted); (ii)
machine gates as promotion criteria (1559/1559, exact Fractions, no floats,
live-mutation negative controls); (iii) certificate culture via the
CERT-UPGRADE vignette — the honest DEAD verdict on prime-size certification
(5×10⁹-digit primes needed for the smallest toy; no theorem can undercut the
d^Θ(n) shape) next to the live extraction lane:

> **The 2-row certificate (CERT-UPGRADE.md §2.4).** All four conjE B-subset
> systems share byte-identical nonzero cofactors, dividing by t² to
> (f1n0 − f1n1)² = f13 + w·f21,
> w = −(g2n0−g2n1)²(f2n0−f2n1) − 2(g2n0−g2n1)(f1n0−f1n1) − (g1n0−g1n1)(f2n0−f2n1):
> the square of the P1-difference lies in the ideal (f13, f21) — a 2-row
> emptiness core, integral, height log 2, verified in an independent engine —
> upgrading msolve EMPTY verdicts to unconditional char-0 theorems.

and (iv) the retraction ledger as a feature (lift retirement under the
last-chance rule; the 729-row re-emission with why no verdict flips; the
msolve parenthesis and mod-p reduction hazards with the 401-file audit).
Framed as engineering discipline that supplements, never replaces, proofs
and human refereeing.

**§10. Open problems (1 p.).** td-11/13 refile + tower port; U_7C; the
coefficient-gluing tier; SC1; depth ≥ 3.

Appendix (1.5 pp): reproduction commands (`tower_check.py`,
`td7_census_e5.py`, `book_offaxis.py`), gate inventories, artifact DOI.

### Proven in-paper vs cited-to-artifact (ToC B)

| item | status |
|---|---|
| Theorem A + thm:R | cited to paper 1 / paper 2A (statement only) |
| H5a incoherence-of-P + uniqueness-of-Q | **in-paper** (proof sketch with thesis page cites; full proof cited to xmodel/sol-h5a.md) |
| Zero-chain law, both iff directions | **in-paper** |
| Class-B emptiness; N1 bite (4 cells) | **in-paper** |
| Census enumeration (17 cells, 238/233 routes, cap-free inversion, ν ≤ 400 sweep) | cited to artifact (`cases/td7_census_e5.py`, gates G1–G5) |
| Panel-constant clash + universal A/B/C + N1–N4 | **in-paper** |
| Lemmas L-A, AM, WIN(+TERM), E5F | **in-paper** |
| 16-row witness table + stress realizations | cited to artifact (`cases/tower_check.py`, 1559 gates; frozen table reproduced in-paper) |
| Four per-cell certificates | cited to artifact (cases/towers/ + review docs) |
| Sigray Prop 4.2/8.1/St 8.4/etc. | cited external, declared as hypotheses, errata disclosed |
| 2-row Nullstellensatz certificate | **in-paper** (verbatim, it is 5 lines) |

### Page estimate: **28–32 pages** (within the 25–35 band).

### Referee risk (hostile referee's attack order)

1. **The Sigray trust set.** "A 30-page tower on an unpublished 2008 thesis in
   which you yourselves catalogued errata E1–E10 and an incoherent notation."
   The attack is fair and must be pre-empted in §1 and §3. Point to: the H5a
   proof-tier resolution with printed-page hostile replay; the forced-ν 2-cell
   sub-book killed unconditionally across coherent readings; U_7C moot for
   td-7; the theorem's perimeter sentence making every import a named
   hypothesis. Residual honest exposure: the verdict is conditional
   architecture, and the paper must say so in the abstract.
2. **Census completeness.** "Why is there no 18th cell?" Point to: the cap-free
   inversion (no guessed bound), closure-forced termination of the 2/(2k+1)
   family, brute-force ν ≤ 400 (0 miss / 0 extra), gates G1–G5, and the
   census-audit-class note (n ≥ 1 filter for future consumers).
3. **WIN's quantifier closure.** "242 path-states is a sample." Point to: Sol
   finding 3 handled exactly this — closure is by lemma ingredients (i′)–(v),
   the enumeration is corroboration; the raw-menu 5/2 outlier and its budget
   block are displayed, not hidden.
4. **Machine-gate opacity.** "I cannot referee 1559 checks." Point to: §9's
   design — every gate named, exact arithmetic, negative controls, 4-second
   local reproduction, and the certificate vignette showing the culture
   upgrades machine verdicts to hand-checkable identities wherever feasible.
5. **"AI reviewed AI."** Point to: the review chain is adversarial across
   model families with preserved failure history (BROKEN verdicts kept and
   answered, not overwritten); presented as discipline supplementing human
   refereeing; the retraction ledger as evidence the process bites.
6. **Obsolescence/downgrade risk (internal, not referee):** TOWER-UNIFORM is
   PROMOTED *pending coordinator ledger pass*, and td-11/13 refile + tower
   port is actively launching — the story may strengthen (multi-panel) or
   shift under this paper while it is being written.

### arXiv category

**math.AG primary, cross-list math.AC and cs.SC** (the methodology section is
genuine symbolic-computation content; cs.SC also signals the audience for §9).

---

## 3. Recommendation

**Write ToC A first. Start now; target a compiled draft within days** (most of
the mathematical text exists in MATHIEU.md and paper1 §6; the new writing is
§4's ledger and the intro). Gate ToC B on (i) the TOWER-UNIFORM coordinator
ledger pass and (ii) the td-11/13 verdict or a ~4–6-week timeout, whichever
comes first.

Reasons, in DC's stated decision frame:

1. **GGV correspondence timing.** The 2026-08-14 follow-up just told GGV "the
   rigidity statement is now a theorem (Thm 6.5)". ToC A is the paper-shaped
   version of that exact sentence — striking while the thread is warm gives
   the correspondents something short to read, react to, and (per the phase-0
   plan) endorse from. ToC B has zero GGV surface and was deliberately kept
   out of the correspondence by the phase-0 rule.
2. **Endorsement path.** The endorsement ask is deferred pending a positive
   GGV reaction, and DC is a new arXiv account. A 10–12-page unconditional,
   self-contained note — no unrefereed dependencies, no unpublished-thesis
   trust set, checkable in an afternoon — is the right second paper for that
   flow. ToC B's conditional architecture and AI-methodology section are the
   wrong first impression for moderators; it lands far better as paper 3 from
   an established account.
3. **td-11/13 strengthens B by waiting.** The next rungs (td-11/13 refile +
   tower port) are actively launching, and the td-11 compiler is gated on
   NF-Z. If they close, ToC B upgrades from a one-panel paper to the sheet
   ladder with a genuinely uniform story; if a survivor appears, B's framing
   must change anyway. Writing B now buys rewrite risk either way — and its
   headline theorem is not yet fully banked (pending ledger pass).

Required pre-submission task for A (only real risk): a genuine literature
search on Theorem A priority — MATHIEU.md's §1.3 ledger is explicitly
from-memory. Budget a session with web access before the abstract claims
novelty for the statement rather than for the consequence.

Sequencing bonus: once A exists, ToC B's Part I shrinks to citations, pulling
B toward the low end of its page band.
