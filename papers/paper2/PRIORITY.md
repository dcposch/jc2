# paper2/PRIORITY.md — literature priority search for Theorem A

**VERDICT: PRIOR ART FOUND (in substance, different clothing) — H. Żołądek, "An application of Newton–Puiseux charts to the Jacobian problem", Topology 47 (2008) 431–469, Appendix Lemma A.7 (with Lemmas A.4/A.6 and Lemma 3.9). Reduction distance to Theorem A: two lines + one trivial case. The verbatim ODE-pair statement, Lemma B, Corollary D, the bridge/SC1, and the char-p boundary are NOT in the literature; Corollary E's content is also a 2-line corollary of Żołądek's A.7 and must be cited. The w = 1 case of Theorem A is separately published verbatim (Hermoso–Alcázar 2024).**

Date: 2026-08-14. Search executed with web access (WebSearch/WebFetch; arXiv, MSP/Math Scand archive,
Project Euclid surface, ScienceDirect surface, local refs/ PDFs). Mission: determine whether Theorem A
(MATHIEU.md §5.1: char 0, w ≥ 1 integer, A, C ∈ F[y], A·C′ − w·A′·C = c ≠ 0 ⟹ deg A ≤ 1) or a
trivially-equivalent statement is already published. Criterion used, per mission: a published statement
implying Theorem A with ≤ 2 lines of reduction counts as priority.

---

## 1. The find

### 1.1 What Żołądek proves

Żołądek 2008 (the paper is **already in this repo at refs/zoladek2008_official.pdf**; SCOPE.md referee-risk
item 1 is answered out of the campaign's own reference folder), Appendix "Schwarz–Christoffel integrals",
studies Ψ(u) = ∫^u ∏_{i=1}^{s+1}(v−u_i)^{ϑ_i} dv (distinct u_i, rational exponents, s ≥ 1, ϑ_i ∈ Q∖Z_+)
and asks when Ψ is a **Darboux function** (const·∏(u−u_i)^{β_i}) modulo an additive constant. Verbatim
chain (pages 466–468):

- **Lemma A.4.** Ψ Darboux ⟺ (i) at every ϑ_i ∈ Z_−∖0 the residue Res_{u_i}Φ = 0, and (ii) all
  "values" Ψ(u_i) coincide. [The residue-vanishing obstruction — the same functional as Corollary E.]
- **Lemma A.6.** If Ψ is Darboux then s + (1 + deg Φ) ∈ Z_−, deg R = −s − deg Φ; introduced with the
  sentence *"The following results were probably known already to Liouville."* Its proof is the
  valuation-at-infinity budget count (Ψ ~ u^{1+d} at ∞ vs. deg R + s + 1 + d) — the SAME mechanism as
  Theorem A's Steps 1–4 / the ord_∞ reading in MATHIEU.md §5.1.
- **Lemma A.7.** *"In the assumptions of Lemma A.6 one has that at least one ϑ_i ∉ Z."* I.e.: **if all
  exponents are negative integers and there are ≥ 2 distinct roots (s ≥ 1), the primitive is never a
  Darboux function.** Proof: normalize Ψ(∞) = 0, then Ψ = R·∏(u−u_i)^{ϑ_i+1} forces deg R = −s < 0,
  contradiction. (Four lines; identical shape to Theorem A's Step 4.)

Over C every rational function is a Darboux function (split the numerator into linear factors), and A.4–A.7
work "modulo an additive constant"; so A.7 says: **∫ dv/A(v)^m is never a rational function when A has at
least two distinct roots, for any m ≥ 1** (exponents −m·e_i ∈ Z_−).

Żołądek also uses this *inside the Jacobian problem in exactly Theorem A's role*: his Lemma 3.9 derives, from
Jac = 1 in a Newton–Puiseux chart, the linear inhomogeneous ODE (3.14) (ψ̃_N)′ = δ(ϕ′/ϕ)ψ̃_N − 1/(pϕ) —
i.e. **ϕ·ψ′ − δ·ϕ′·ψ = −1/p, our (ODE) with (generally rational) weight δ** — solves it as
ψ̃_N = −(1/p)ϕ^δ ∫ϕ^{−δ−1}, and imposes rationality of the mate ⟹ the Schwarz–Christoffel integral must be
Darboux. At §6 (p. 462, integer-exponent case): *"If s_{N−1} = 1, then we have an integral of a rational
function and by Lemma A.7 (in the Appendix) c_{N−1} cannot be Darbouxian."* — the integer-weight kill,
stated and used.

### 1.2 The reduction (Żołądek ⟹ Theorem A)

1. Suppose A·C′ − w·A′·C = c ≠ 0. Then (C/A^w)′ = c/A^{w+1}, so ∫dy/A^{w+1} = C/(cA^w) is rational,
   hence Darboux; Lemma A.7 (exponents −(w+1)e_i ∈ Z_−) forbids this whenever A has ≥ 2 distinct roots.
2. Remaining case A = α(y−r)^δ, δ ≥ 2: evaluate the equation at y = r (A(r) = A′(r) = 0) to get c = 0,
   contradiction. Hence deg A ≤ 1. ∎

Line 2 is genuinely outside A.7 (perfect powers have one root) but is a one-line evaluation; under the
mission's ≤ 2-line criterion this is priority. Corollary E similarly: if all residues of A^{−m} vanished
(A squarefree, deg ≥ 2), partial fractions + termwise integration give a rational primitive, contradicting
A.7 — so Corollary E's content is also covered-in-substance (the per-power residue *statement* is not
displayed in Żołądek; it is a 2-line corollary of A.7, and A.4's condition (i) is literally the residue
functional).

### 1.3 What is NOT in Żołądek (or anywhere found)

- The **ODE-pair formulation** "A·C′ − w·A′·C = c ≠ 0 ⟹ deg A ≤ 1" as a displayed theorem about
  polynomial pairs (his weights are rational chart exponents; the polynomial-pair statement is implicit).
- **Lemma B** (block ⟺ ODE), Corollary C/D (strip uniformity), and everything downstream in paper 1.
- The **characteristic-p boundary** (p > (k+1)d2 sufficiency; honest failure in small p).
- **Corollary E as a stated dichotomy** ("for EVERY m ≥ 2 some root has Res ≠ 0"), and the MZ reading.
- The **bridge theorem, M_A codimension structure, and SC1** (the ≥ 3-puncture Mathieu question) — the
  univariate MZ literature (van den Essen–Zhao JPAA 2013; JPAA 2016) has no image-of-(A∂ − kA′) results;
  Zhao's image-conjecture corpus stays at constant leading coefficients. SC1 remains new.

### 1.4 Consequence for paper 2

Theorem A survives as a *statement worth displaying with a self-contained 15-line proof*, but the abstract
and §1 must NOT claim novelty for the rigidity phenomenon itself. Required reframing: (a) cite Żołądek 2008
Lemma A.7 (+ his Liouville attribution) as the prior form of the content, and Lemma 3.9/(3.14) as the prior
appearance of the same ODE inside the plane JC; (b) cite Hermoso–Alcázar (arXiv 2410.18867) Theorem 4 for
the w = 1 case; (c) let the paper's claimed contributions be: the uniform pair formulation with the
elementary 4-step proof, the char-p boundary, Lemma B + the block application (Corollaries C/D), Corollary E
as the multi-puncture DvdK-1D dichotomy, the bridge/M_A structure, and SC1. (d) The "found by transporting
the DvdK mechanism" provenance paragraph stays honest and is now corroborated: the mechanism IS the
classical Liouville/valuation argument, independently rediscovered.

---

## 2. Search log

Queries run (WebSearch unless noted), with outcome:

| # | Query / fetch | Outcome |
|---|---|---|
| 1 | polynomials "constant Wronskian" degree bound fg′−f′g | **HIT**: arXiv 2410.18867 (Hermoso–Alcázar); rest Wronski-map/Schubert literature, unrelated |
| 2 | integral 1/p(x)^n rational antiderivative residues squarefree | classical "rationally integrable ⟺ residues vanish" only; telescoper literature (Chen, Bostan et al.) — no rigidity statement |
| 3 | Duistermaat van der Kallen constant term Laurent Mathieu degree pair | DvdK 1998 confirmed; Erman–Smith–Várilly (Eulerian numbers, regular sequences — unrelated); **HIT**: 2026 SU(2) counterexample paper |
| 4 | Magnus 1955 polynomial solutions differential equation JC | located Magnus, Math. Scand. 3 (1955) 255–260; + "Magnus' formula revisited I–IV" (arXiv 2201.06613 etc.) |
| 5 | Jacobian conjecture counterexample 2026 arXiv | **wave mapped**: Alpöge 7/19 (dim 3), Gallagher 7/20 (family), Speyer 7/23 (tangent-sweep geometry), Gao arXiv 2608.00222 (all dims > 2, five explicit maps); 2D case explicitly still open; Tao + Secret Blogging Seminar digests |
| 6 | images of derivations / order-one operators univariate Mathieu | van den Essen–Zhao arXiv 1012.2017 (JPAA 2013); JPAA 2016 strong-radical paper; Zhao 0902.0210 (constant leading coefficients); no A∂−kA′ results |
| 7 | WebFetch arXiv 2410.18867 full text (local pdftotext) | **n = 2 Theorem 4 = exactly Theorem A's w = 1 case**; n ≥ 3 = span{1,…,t^{n−1}} characterization; refs are CAGD/geometry only (Castelnuovo 1886, Veronese 1882, Bostan–Dumas); no weighted variant |
| 8 | WebFetch Magnus 1955 PDF (MSP mscand archive, journals.msp.org/mscand/article/view/2880, DOI 10.7146/math.scand.a-10443) — read all 6 pages | **NOT prior art**: "differential equation" = the 2-variable Jacobian PDE u_{z1}v_{z2}−u_{z2}v_{z1} = k; theorem = coprime-degrees case (m,n ≥ 2 coprime ⟹ k = 0, u,v ∈ K[h]); proof via homogeneous-piece recurrences/generating functions (Legendre-like P_μ); no 1-variable ODE lemma |
| 9 | WebFetch arXiv 2511.16561 (Zwart, Nov 2025, "Mathieu's approach to the JC") | expository (Mathieu 1997 SU(N) ⟹ JC); no univariate lemmas |
| 10 | WebFetch arXiv 2607.18186 (Long) | Gaussian Moments Conjecture FALSE (n ≥ 3): E(P^m)=0, E(QP^m)=m!. No 1-variable content |
| 11 | WebFetch arXiv 2607.19012 (Long) | **Mathieu Conjecture FALSE for SU(2)** + xz-conjecture false (Laurent f=(1−z^{-1})((1−x)+xz), I(f^n)=0, I(z^{-1}f^n)≠0). DvdK (abelian, proved) unaffected. No 1-variable ODE content |
| 12 | GGV Poisson bracket homogeneous classification | arXiv 1401.1784 fetched + pdftotext-greped: Prop 2.1 ([P,Q]=0 homogeneous ⟹ P = λ_P R^m, Q = λ_Q R^n — Step 3's kernel, attributed to earlier lit.); Lemma 2.2/Thm 2.6 (Joseph-style F-element, [F,ℓP]=ℓP); no ODE-rigidity lemma |
| 13 | WebFetch arXiv 1310.8249 (GGV, "A differential equation for polynomials related to the JC") | title on-the-nose but content = B=16 case reduced to an **Abel equation of the second kind** (nonlinear); same bracket-column→ODE mechanism as Lemma B, different equation, no rigidity theorem, explicitly unsolved |
| 14 | Heitmann 1990 / Moh 1983 edge ODE lemmas | statements located (B ≥ 16; deg < 100); genus-zero/exact-differential reformulation noted; no Theorem-A-form lemma surfaced at abstract level |
| 15 | Nakai–Baba 1977 (generalization of Magnus) | Project Euclid paywalled; statement (prime/4/2p degree cases via weighted gradings) confirmed via citers; method = weighted Taylor expansions; no indication of our ODE statement |
| 16 | van den Essen "Amazing Image Conjecture" 1006.5801 (pdftotext) | univariate MZ examples are moment-type (∫₀¹, Laguerre/e^{-t}); 1-property = MATHIEU.md §1.1 lemma; nothing about non-constant leading coefficients |
| 17 | Pakovich moment problem / orthogonal to all powers | thematic cousin only (composition conditions for ∫P^k q; Cauchy-type integrals on curves); non-implying |
| 18 | Davenport–Lewis–Schinzel; Mason/Stothers | different family (f(x)=g(y), deg(f³−g²) bounds); non-implying |
| 19 | arXiv math.AC listings 2026-07, 2026-08 (WebFetch) | only: 2608.12294 (real JC note), 2607.12162 (McDaniel, Hessians/Wronskians — Lefschetz theory, unrelated). Reaction wave lives in math.AG; no univariate rigidity preprint found |
| 20 | "all residues vanish" / rational antiderivative of 1/f^n phrasings (3 variants) | classical equivalence only; **no published statement of the 1/A^m dichotomy found outside Żołądek A.4–A.7** |
| 21 | Local refs/ sweep (pdftotext + grep): chau1999 (Ann. Pol. Math. 71), jc86 = Orevkov 3-sheeted, do = Domrina–Orevkov 4-sheeted, sigray_full, zoladek2008 | **THE FIND**: Żołądek Lemma 3.9/(3.13)/(3.14) + Appendix A.4–A.7 + §6 usage line ("integral of a rational function … cannot be Darbouxian by Lemma A.7"). Others: Newton–Puiseux/topological, no ODE rigidity |
| 22 | Nowicki–Nakai "On Appelgate–Onishi's lemmas" JPAA 51 (1988) 305–310 (+ correction JPAA 58 (1989) 101) | located, Elsevier-paywalled — **unresolved secondary**; per Żołądek Remark 3.10, Appelgate–Onishi [+ Abhyankar 1977, van den Essen book, Oka 1983] "also encountered the problem of determining ψ̃_N … using algebraic tools", so AO's lemmas likely contain the rationality condition in algebraic form. Check before submission; does not change the verdict (Żołądek already suffices) |

Dead ends / access notes: zbMATH 403; Springer article page 303-redirects (Y. Stein, "The Jacobian problem
as a system of ODEs", Israel J. Math 89 (1995) — surface only, reduction-to-ODE-system framing, no
indication of our lemma); export.arxiv.org API returned empty from sandbox; Wenhua Zhao's ISU publications
page 410 (he died 2023; arXiv listing used instead); mscand.dk old OJS paths 404 (journal moved to MSP —
resolved via journals.msp.org/mscand search); Project Euclid OJM 1977 paywalled; ScienceDirect 403 on JPAA
1988 (0022404988901156).

---

## 3. Nearest-neighbor list (one-line distances)

**Class 1 — implying / priority-relevant:**

1. **Żołądek 2008, Topology 47, Appendix Lemma A.7 (+ A.4, A.6, Lemma 3.9, §6 use).** Distance:
   2-line reduction + trivial perfect-power case; same mechanism, same JC context, rational-weight chart
   form; he credits the circle to Liouville. **= the prior art.**
2. **Hermoso–Alcázar, arXiv 2410.18867 (2024), Theorem 4 with n = 2.** Distance: zero for w = 1
   (pq′−p′q = c ≠ 0 ⟹ both degrees ≤ 1); no route to w ≥ 2 (their Wronskian is unweighted); their n ≥ 3
   and Laurent results are orthogonal.
3. **Classical two-branch-point rigidity (Riemann–Hurwitz / cyclic-covering folklore; also DvdK-1D's
   valuation mechanism).** Distance: ~5-line derivation (t = C/A^w has critical values ⊆ {∞, t(∞)}; fiber
   over ∞ = δ points ⟹ δ = 1); no citable pair-statement found anywhere — mechanism-level only, already
   acknowledged in MATHIEU.md §5.1.

**Class 2 — thematic, non-implying:**

4. **Magnus 1955 (Math. Scand. 3, 255–260)** — read in full: 2-var Jacobian PDE, coprime degrees, k = 0
   conclusion; recurrence/generating-function proof. Ancestor of the "bracket forces collapse" genre only.
5. **GGV corpus**: 1401.1784 Prop 2.1 (homogeneous [P,Q] = 0 ⟹ common-power structure — Step 3's kernel,
   classical), Lemma 2.2/Thm 2.6 (F-element machinery); 1310.8249 (bracket-column → first-order ODE
   reduction; nonlinear Abel equation, open). Same program (paper 1's ancestry), no rigidity lemma.
6. **DvdK 1998** — the 1-D support dichotomy that inspired the proof; no pair/ODE statement.
7. **Univariate MZ literature**: van den Essen–Zhao JPAA 2013 (radical characterization); JPAA 2016
   (non-zero strong radical); Zhao 2010 J. Algebra (constant leading coefficients); van den Essen survey
   1006.5801 (moment-type univariate examples). SC1 confirmed outside all of it.
8. **Muzychuk–Pakovich / Pakovich** moment problems ("orthogonal to all powers") — all-power vanishing ⟹
   composition structure; different functional and geometry.
9. **Heitmann 1990 (JPAA 64 + corr. JPAA 90)**, **Appelgate–Onishi 1985 (JPAA 37)**, **Nowicki–Nakai 1988
   (JPAA 51)**, **Abhyankar 1977 (TIFR)**, **Oka 1983 (Kodai 6)** — the "algebraic tools" treatments of the
   same chart-rationality condition (per Żołądek Remark 3.10); AO/NN unresolved at statement level
   (paywall), flagged for pre-submission check.
10. **Abramov-style algorithmics** (rational/polynomial solutions of first-order linear ODEs) — decides
    instances, states no uniform rigidity.
11. **Nowicki, Nagoya Math. J. 109 (1988)** (J(f,g) = 0 classification) — kernel case only.
12. **McDaniel arXiv 2607.12162** (Hessians/Wronskians, Lefschetz) — name overlap only.

**Collateral intelligence for paper 2's ledger (MATHIEU.md §1.3 corrections, 2026 wave):**

- **JC itself is FALSE in every dimension n ≥ 3** (Alpöge 7/19/2026; Gallagher family; Speyer tangent-sweep
  explanation; Gao arXiv 2608.00222). **The 2-D case — this campaign's case — remains open.** Paper 2's
  framing must say "plane JC" everywhere and may cite the wave as motivation for 2-D structure results.
- **Mathieu's conjecture is FALSE for SU(2)** (Long, arXiv 2607.19012; also kills van den Essen's
  xz-conjecture reduction target), and the **Gaussian Moments Conjecture is FALSE for n ≥ 3** (Long, arXiv
  2607.18186). §1.3's lines "Mathieu's conjecture for nonabelian compact G: open" and the EWZ Gaussian-
  moment evidence chain must be rewritten; DvdK (abelian case) is a proved theorem and unaffected; the MZ
  frame of paper 2 (bridge, SC1) consumes only DvdK-side machinery and survives, but SC1's plausibility
  discussion should acknowledge that Mathieu-type statements now have nonabelian counterexamples.
- Zwart arXiv 2511.16561 (Nov 2025): modern exposition of Mathieu 1997 (SU(N) ⟹ JC(C^N)) — citable for
  the frame; note the implication's hypothesis is now known false for SU(2) while its JC conclusion is
  false in n ≥ 3 — the frame paragraph should be rewritten against both facts.

---

## 4. Bottom line for the write-up

Theorem A's *content* = Żołądek 2008 Lemma A.7 (who says Liouville probably knew it) + a one-line
perfect-power case; its *statement*, elementary proof, char-p analysis, block bridge (Lemma B/Cor C/D),
Corollary E as a residue dichotomy, and the MZ/SC1 frame remain available as paper 2's contributions.
Cite: Żołądek (Lemma A.7 + Lemma 3.9/(3.14)), Hermoso–Alcázar (w = 1), Magnus 1955 (genre ancestor),
GGV 1310.8249 (bracket→ODE mechanism), DvdK. Pre-submission task remaining: obtain Appelgate–Onishi 1985 /
Nowicki–Nakai 1988 to fix their lemmas' exact form (secondary; cannot restore a novelty claim, can only
add a citation). Not committed to git.
