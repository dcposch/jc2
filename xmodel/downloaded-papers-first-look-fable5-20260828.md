# Fable5 first-look triage: Matysiak SSRN 7229358 / 7229458

Date: 2026-08-28 UTC.
Role: independent literature triager (not campaign coordinator).  This
report discharges the primary-text audit queued by the 13:48Z 2026-08-27
web-sweep event (`ACTIONABLE-UNAUDITED / BLOCKED-BY-PRIMARY-TEXT-ACCESS`,
sweep `a8a1ae4f...`; standing instruction: audit the dependency theorem and
the first dimension-two step for circular injectivity/properness/UFD or
image-normality assumptions).  Both anticipated failure modes are realized.

Inputs (hashes verified by `shasum -a 256` this session):

```text
d9e567aff6810dace9a22b4d82cc72c48d6ab509fc0007bdbc8ebde839890ab2  /Users/dc/Downloads/ssrn-7229358.pdf  (34 pp.)
32df180419ae5125943bef65f27da65aef72c501962be50a880b61fe51464722  /Users/dc/Downloads/ssrn-7229458.pdf  (19 pp.)
```

Execution disclosure.  Both PDFs were read in full (page-image extraction,
all 34 + 19 pages).  Campaign context read: `PROGRESS.md` (preamble +
2026-08-28/27 entries incl. the 13:48Z event), `APPROACHES.md` (00:41Z and
22:40Z overlays; sweep paragraph at ~line 747; inventory rows 17/35/39),
`notes.md` (13:48Z/13:49Z events, 22:34Z queue), topic greps of `AUDIT.md`.
No web, no AWS, no `jc2-lean` access, no campaign file edited.  All
refutation algebra is desk work; four load-bearing counterexamples were
additionally machine-checked in exact rational arithmetic
(`/tmp/matysiak_audit_checks_20260828.py`, sha256 prefix `f38a09ed...`;
outputs quoted inline below).  Statements about the contents of
Bass–Connell–Wright 1982 and Jędrzejewicz–Zieliński 2017 are from
recollection of those texts and are flagged for web confirmation.

Keyword-collision warning for future greps: the "square-free" in these
papers concerns images of ring endomorphisms.  It is unrelated to the
campaign's GGV `8_28` squarefree-`H` gate conditions (q1/q2 codim laws) and
to the R3/R4 "squarefree modes" cases; no result here touches those lanes.

---

## 1. Paper A — SSRN 7229358 (the 34-page dependency)

**Title/author.**  "The endomorphic condition 5''_s as an algebraic
characterization of constant-Jacobian endomorphisms."  Łukasz Matysiak,
Institute of Mathematics and Cryptology, Military University of Technology,
Warsaw.  No date printed; bibliography contains 2025/2026 items (incl. a
J. Math. Sci. 2026 DOI), so 2026; Alpöge is not cited.  Paper B cites this
item as series part [8] via "Theorem 9.2 in [8]" — the theorem numbers
match even though B's bibliography lists [8] under a different title
("An Endomorphic Monoid Condition Equivalent to the Jacobian Condition");
note the bibliographic drift when citing.

**Claimed theorem.**  For a monoid-factorization condition 5''_s on the
image `R = φ(A)` of a `k`-algebra endomorphism of `A = k[x_1..x_n]`
(char 0) — every factorization `φ(f) = gh` with `g,h ∈ R`, `h` square-free,
has every square-free `q ∈ R` dividing `g` also divide `h` — the paper
claims: (i) Thm 3.4: for Keller φ, *automorphism ⟺ image satisfies 5''_s ⟺
φ preserves square-free polynomials with linear factors*; (ii) Thms
3.8/3.12/4.3: 5''_s is local, composition-stable, conjugation-invariant;
(iii) Thm 8.1: every Družkowski cubic-linear form `x + (Bx)^3` with
nilpotent `B` satisfies 5''_s w.r.t. linear-factor polynomials; (iv) Thm
9.1/9.2 + §8.4: *a constant-Jacobian endomorphism is an automorphism ⟺ its
Družkowski form satisfies 5''_s* — which, combined with (iii) and the
Družkowski reduction, is presented in §8.4 as a "conclusion scheme"
yielding JC(n) for **all** n.

**Classification.  NOT USEFUL.**  The sound fragments are trivial for
Keller maps (see D2) or restatements; every novel load-bearing step is
unsound (D1–D4 below).  Its §8.4 conclusion contradicts the standing
dim-3 counterexample accepted by the same author's Paper B.

**Closest avenues.**  Avenue 17 (BCW/Družkowski/Yagzhev cubic
stabilization) — already scored low with Grok's "category error" dissent;
this audit *vindicates* that score and contributes one cautionary lemma to
that terrain (D3: the cubic-linear class is closed under monomial
similarity only, so any "reduce to Jordan blocks" argument in this genre is
an automatic red flag).  Avenue 39 shares only the étale/unramified
vocabulary.  Nothing touches the live routes (exact-pair two-chart/L3–L5/
landing/`RPMC(C)`/cofinal ceiling, GGV faces, K00, de Rham gates).

**Soundness check (earliest serious gaps).**

- **D1 — earliest fatal step, Thm 3.4 (3)⟹(1), p. 7.**  The proof rests
  on: "Since A is a polynomial ring over a field of characteristic 0,
  every unramified endomorphism is an automorphism (cf. [1])", with [1] =
  Bass–Connell–Wright 1982.  To my knowledge BCW contains no such theorem;
  the quoted statement is a standard étale reformulation of the Jacobian
  Conjecture itself, and in the campaign's accepted post-Alpöge reality it
  is *false* for n ≥ 3.  Every downstream result (Thms 9.1, 9.2, §8.4
  scheme, and Paper B's Twierdzenie 1.1/6.1) inherits this single step.
- **D2 — condition (3) is vacuous for Keller maps.**  Every Keller
  endomorphism preserves square-freeness *automatically*: `V(φ(f)) =
  Φ^{-1}(V(f))` and étale pullback of a reduced divisor is reduced.
  Elementary proof needing no scheme theory: if `p^2 | φ(f)` then `p`
  divides all `∂_i φ(f)`; the chain rule gives `∇(f∘F) = (J_F)^T·(∇f)∘F`
  with `J_F` invertible *over A* (`det ∈ k^*`), so `p | (∂_j f)∘F` for all
  j and `p | f∘F`; hence the codim-1 set `V(p)` lies in
  `Φ^{-1}(Sing V(f))`, impossible since `f` square-free makes
  `Sing V(f)` codim ≥ 2 and étale Φ is quasi-finite.  Consequently the
  entire case apparatus of §§5–7 (diagonal, triangular, Jordan) verifies a
  triviality, and the paper's whole discriminating content sits on the
  miscited D1.  Related smuggling: Thm 3.3 assumes the image `R` is
  *factorially closed* in `A` — for a genuinely non-surjective φ that
  hypothesis typically fails, so the hypothesis quietly restricts the
  theorem to near-automorphism images.
- **D3 — Thm 8.1's Jordan reduction is invalid (machine-checked).**  The
  class `{x + (Bx)^3}` is *not* stable under general linear conjugation —
  coordinatewise cubing commutes only with monomial (diagonal×permutation)
  similarity.  Executed counterexample, `J_3` = 3×3 Jordan block,
  `P = [[1,0,0],[1,1,0],[0,0,1]]`: the true conjugate
  `G = P^{-1}∘F_{J_3}∘P` has second coordinate `x_2 + x_3^3 − (x_1+x_2)^3`
  whose cubic part is not the cube of any linear form (candidate
  `(−x_1−x_2+x_3)^3` refuted by exact expansion), while `det J(G) = 1`; and
  the naive form `F_{B'}` with `B' = P J_3 P^{-1}` (nilpotent, `B'^3 = 0`)
  has `det J(F_{B'}) = 1 + 3x_3^2 + 6x_2x_3 − 6x_1x_3` — **not even
  Keller**.  So "matrix similarity corresponds to composition with an
  automorphism" fails for this class in both directions.  The strictly
  triangular `B` actually analyzed in §§6–7 give evident (triangular)
  automorphisms; every hard Družkowski map lies outside.  If the reduction
  were valid, §8.4 would prove JC(n) for all n — refuted by the standing
  dim-3 counterexample.
- **D4 — full-vs-restricted 5''_s equivocation.**  Thm 9.4 asserts the
  *full* condition citing Thms 4.5/4.6/7.4, which only establish the
  `Sqf_lin`-restricted version.  Lemma 7.2 ("the only square-free divisors
  in R are the variables") is false unrestricted — `x_1 + x_2^3 ∈ R` is an
  irreducible non-linear square-free divisor; Lemma 4.5's premise "every
  irreducible factor of F(f) is a linear form" is false (`x + y^3` is an
  irreducible cubic).  The abstract's unrestricted claims are unlicensed.
- **D5 — dim-2 classification slip, p. 16 (machine-checked).**  "Constant
  Jacobian forces `a_11 = a_22 = 0`, `a_12·a_21 = 0`" is false:
  `B = [[1,−1],[1,−1]]` is nilpotent with `F = (x+(x−y)^3, y+(x−y)^3)` and
  executed `det J(F) = 1`; the proportional-rows branch (`L_1 ∥ L_2`) is
  missed, so "in dimension 2 all Družkowski forms are triangular" is false
  as printed (they are only linearly conjugate to triangular — via exactly
  the conjugation the paper mishandles in D3).  Harmless in dim 2 (the map
  is still an automorphism), but a concrete falsifiable error.

**Recommendation.  MOVE TO REFS** as audited intelligence (the campaign's
standing order was lawful acquisition + audit; `refs/` is the paper store):
`refs/matysiak2026_ssrn7229358_condition5s_endomorphic_characterization_unsound.pdf`.
The `_unsound` suffix is deliberate so no future session credits it without
reading this audit.  Verify the sha256 above after copying.

---

## 2. Paper B — SSRN 7229458 (the claimed JC2 proof)

**Title/author.**  "The Jacobian Conjecture in Dimension Two and the Role
of the Condition 5''_s."  Łukasz Matysiak.  Post-July-2026 (cites Alpöge's
counterexample *announcement* as an x.com link, [1], accessed July 2026);
"third part of a series"; residual Polish labels (Twierdzenie/Definicja/
Wniosek).  19 pages.

**Claimed theorem.**  A *complete proof of JC(2)*, "in two independent
forms": a classical dimension-theoretic argument (Twierdzenie 5.1) and a
structural criterion via 5''_s (Twierdzenie 6.1 + §7), with the framing
that dimension 2 is the unique dimension where JC remains true, and that
every Keller non-automorphism must violate 5''_s (via Paper A's Thm 9.2).

**Classification.  NOT USEFUL as mathematics; high intelligence value.**
Both proofs collapse at their first load-bearing steps (E1, E4).  The
value is closing the 13:48Z `ACTIONABLE-UNAUDITED` item: **JC2 is not
solved by this paper**; no reranking or reallocation is warranted, and the
decision to keep internal exact lanes running was correct.

**Closest avenues.**  The external-claims/intelligence lane (13:48Z sweep
item — discharged by this report).  Avenue 35 (descent of dim-≥3
counterexamples) only negatively: §9's "explanation" of why n ≥ 3 differs
is provably wrong (E2) and contributes nothing to avenue 35's real
mechanisms.  No contact with any live lane.

**Soundness check (earliest serious gaps).**

- **E1 — fatal non sequitur, §5 Twierdzenie 5.1.**  The proof correctly
  (modulo E3) shows `f, g` algebraically independent, i.e. `ker φ = (0)`,
  then concludes: "Consequently φ is a monomorphism, and therefore an
  automorphism."  Ring-monomorphism ⟹ automorphism is precisely what JC
  asks; surjectivity (`k[f,g] = k[x,y]`) is never addressed.  (It is also
  not point-injectivity, so no Cynk–Rusek/Ax–Grothendieck rescue applies.)
  The identical argument runs verbatim in every dimension n, so if valid
  it would prove JC(n) for all n — contradicting the counterexample the
  paper itself accepts.  This is exactly the "circular injectivity"
  failure mode the sweep instructions predicted.
- **E2 — §9's n = 2 vs n ≥ 3 dichotomy is provably false.**  The claim
  that for n ≥ 3 there exist Keller maps with `ker φ ≠ (0)` is wrong in
  char 0: algebraically dependent components force `det Jφ ≡ 0` (apply the
  paper's own §5 gradient computation to a minimal-degree annihilator in n
  variables).  Injectivity is free in *all* dimensions; the dimension
  argument is equally vacuous in all dimensions.  The paper's asserted
  n=2-specialness of its own proof is fictitious.
- **E3 — repairable gap, §5.**  "Vanishing of all partial derivatives
  implies F is constant" needs `F` of minimal degree (`F_U(f,g) = 0` does
  not give `F_U ≡ 0` otherwise).  Standard fix; not fatal.
- **E4 — second "proof" is conditional, vacuous, and circular.**
  Twierdzenie 6.1 assumes "every Keller endomorphism of k[x,y] has image
  satisfying 5''_s" — never proven.  §7 offers only "dimension 2 does not
  admit any *known* mechanisms for violating 5''_s" (prose, not
  mathematics); §8 verifies 5''_s solely for triangular and dual-triangular
  maps *by first proving each is an automorphism* (vacuous — automorphism
  images satisfy 5''_s trivially); Wniosek 6.2 derives "k[f,g] is a UFD"
  *from* the broken Twierdzenie 5.1 (the predicted UFD circularity); and
  the invoked JC–5''_s theorem (Twierdzenie 1.1 = Paper A Thm 9.2)
  inherits D1.  Also note D2: by étale pullback, *every* Keller map
  preserves square-free elements, so all source-side "5''_s evidence" in
  §§7–8 is content-free.
- **E5 — series-level inconsistency.**  Paper B accepts JC false for
  n ≥ 3 while its dependency's §8.4 scheme proves JC(n) for all n; the two
  SSRN items are jointly inconsistent and the author never reconciles them
  (the unacknowledged escape valve is D4's restricted-vs-full
  equivocation).

**Recommendation.  MOVE TO REFS** (same rationale and custody note):
`refs/matysiak2026_ssrn7229458_jc2_claimed_proof_condition5s_unsound.pdf`.

---

## 3. Comparative verdict

Both papers are by the same author, form one dependency chain, and fail at
independently identified, concretely refutable steps.  Paper B is the
headline (a claimed complete JC2 proof — the campaign's exact target) and
is the intelligence priority: verdict **REFUTED-ON-AUDIT** at the first
dimension-two step (E1), with the predicted circular-injectivity and
circular-UFD mechanisms both present.  Paper A is the load-bearing
dependency and fails earlier and more broadly (D1 miscitation equivalent
to assuming JC; D2 vacuity of the verified condition; D3 machine-refuted
Jordan reduction).  Neither paper constrains JC2, branch P, any GGV face,
K00, or any live avenue; neither warrants reranking, AWS time, or review
capacity beyond one different-model spot-check of this audit.  The only
durable mathematical residue is two small *defensive* lemmas produced by
the audit itself (atoms T1/T2 below) and the citation trail to the genuine
peer-reviewed antecedents (T3).

Prioritized follow-up:

1. Coordinator: carry this verdict into the next sealed round in place of
   the unaudited claim; the 13:48Z item's "prominent blind-packet entry"
   should now read REFUTED-ON-AUDIT with the atom list below.
2. One different-model hand check of T1 and T2 before banking either as a
   reusable triage discriminator (campaign review discipline; both are
   short desk arguments, T2 partly machine-checked already).
3. When web access is next available: confirm A1 (BCW contains no
   "unramified ⟹ automorphism" theorem) and pull the exact
   Jędrzejewicz–Zieliński 2017 statements (T3).  Low priority.
4. Watch (low priority) for further SSRN items in this series — the
   bibliographies advertise at least five related papers by the author;
   T1/T2 should make any successor triage a same-day desk kill.
5. No formalization, AWS, or avenue-17 reopening on any 5''_s statement.

## 4. Atomized claims for independent mathematical review

Refutation atoms (status: EXECUTED = exact-ℚ machine check this session;
DESK = hand algebra in this report):

- **A1** (DESK, needs literature confirm): "Every unramified endomorphism
  of `k[x_1..x_n]`, char 0, is an automorphism, cf. BCW 1982" — no such
  theorem in BCW; statement is a known JC reformulation, false for n ≥ 3
  given the standing counterexample.  [Paper A Thm 3.4 (3)⟹(1); kills
  Thms 9.1/9.2 and Paper B Twierdzenie 1.1/6.1.]
- **A2** (EXECUTED): `B = [[1,−1],[1,−1]]` nilpotent, `F = x+(Bx)^3` has
  `det J(F) = 1` but is not of either shape claimed on Paper A p. 16.
- **A3** (EXECUTED): `G = P^{-1}∘F_{J_3}∘P`, `P = [[1,0,0],[1,1,0],[0,0,1]]`,
  has coordinate `x_2 + x_3^3 − (x_1+x_2)^3`, cubic part not a cube of a
  linear form, `det J(G) = 1` — Družkowski class not GL-conjugation-stable.
- **A4** (EXECUTED): `B' = P J_3 P^{-1}` is nilpotent yet
  `det J(x+(B'x)^3) = 1 + 3x_3^2 + 6x_2x_3 − 6x_1x_3` — naive conjugated
  form not Keller.  [A3+A4 kill Paper A Thm 8.1 / §8.4.]
- **A5** (DESK): `x + y^3` is an irreducible cubic — refutes Paper A Lemma
  4.5's "all irreducible factors of F(f) are linear" and Lemma 7.2's
  "only square-free divisors in R are variables"; Thm 9.4's upgrade from
  restricted to full 5''_s is unlicensed.
- **A6** (DESK): Paper B Twierdzenie 5.1 proves only `ker φ = (0)`;
  "monomorphism ⟹ automorphism" is a non sequitur, and the argument is
  dimension-independent.
- **A7** (DESK): algebraically dependent components force `det Jφ ≡ 0` in
  char 0 for every n (minimal annihilator + chain rule) — refutes Paper B
  §9's claim that `ker φ ≠ (0)` can occur for Keller maps when n ≥ 3.
- **A8** (DESK): Paper B's §6–8 second proof is conditional on an unproven
  hypothesis, verified only on automorphism classes (vacuous), and
  Wniosek 6.2 is circular through Twierdzenie 5.1.

Bankable positive by-products of the audit (not claims of the papers):

- **T1** (DESK; propose banking after cross-check): *Every Keller
  endomorphism preserves square-free polynomials, in every dimension* —
  étale pullback of a reduced divisor is reduced; elementary proof via
  `∇(f∘F) = (J_F)^T (∇f)∘F`, invertibility of `J_F` over `A`, and
  quasi-finiteness (full argument in D2).  Triage discriminator: any
  external claim whose evidence is source-side square-freeness
  preservation by a Keller map is verifying a triviality.
- **T2** (EXECUTED core; propose banking): the cubic-linear class
  `{x+(Bx)^3}` is closed under monomial similarity only; "reduce B to
  Jordan form" arguments are automatically invalid there (A3/A4), and the
  strictly-triangular subclass consists of evident automorphisms — any
  proof scheme resting on Jordan representatives of Družkowski forms is
  dead on arrival.  Relevant background for avenue 17's existing low
  score.
- **T3** (reference): Jędrzejewicz–Zieliński, Eur. J. Math. 3 (2017)
  199–207 and J. Pure Appl. Algebra 221 (2017) 2111–2118 — the genuine
  peer-reviewed antecedents for irreducibility/square-freeness
  characterizations of Keller automorphisms (Paper A's refs [8,9]).
  Expectation to verify when pulled: the honest equivalences are
  image-side closure conditions, exactly as hard as surjectivity — i.e.
  a reformulation, not a lever.

## 5. Dispositions

| Item | Verdict | Action |
| --- | --- | --- |
| ssrn-7229358.pdf | NOT USEFUL; dependency of the JC2 claim; unsound (D1–D5) | MOVE TO REFS as `matysiak2026_ssrn7229358_condition5s_endomorphic_characterization_unsound.pdf` |
| ssrn-7229458.pdf | NOT USEFUL as proof; closes 13:48Z item as REFUTED-ON-AUDIT (E1–E5) | MOVE TO REFS as `matysiak2026_ssrn7229458_jc2_claimed_proof_condition5s_unsound.pdf` |

JC2 remains open.  Nothing in either paper changes any live allocation.
