# Neutral adjudication: the HC4 ⇒ JC2 dissent (APPROACHES.md row 10)

Adjudicator: Fable (neutral; neither survey text treated as authoritative).
Date: 2026-08-21.
Charge: adjudicate on the mathematics the sharpest dissent in [APPROACHES.md](../APPROACHES.md)
(§3 Dissent item 1): **Sol 9/10, his top pick overall** ([sol-approaches.md](sol-approaches.md) §23)
vs **Grok's structural hostility, no score** ([grok-approaches.md](grok-approaches.md) §12 + cross-cutting judgments).

Verification artifacts used: both source entries in full; RECON.md entries on
arXiv:2607.22198; websweeps 2026-08-16..21; the two 2026 papers themselves
(fetched 2026-08-21); an exact-arithmetic verification script (scratchpad, reproduced in §2.3).

---

## 0. What each party actually claims

**Sol (§23, verbatim in substance).**
(i) The doubling/gradient construction gives HC4 ⇒ JC2; the bridge is *stated* in
Meng–Yang, arXiv:2607.22198. (ii) The quartic HC4 case is proved by Ni,
arXiv:2608.14217, "leaving degree at least five." (iii) Obstruction: "Nilpotence of the
Hessian controls homogeneous layers, but in degree five and above different layers can
cancel; the top form being a cone is not yet enough." (iv) Experiment (9/10 on his
information-yield scale): "Reproduce the quartic cone/Schur argument symbolically,
formulate the exact quintic obstruction module, and decompose its first uncancelled term
under GL_4. This is the strongest adjacent live conjecture with a clean implication to JC2."

**Grok (§12 + cross-cutting).**
Files HC under "Poisson, Gaussian moments, Hessian, and the rest of the Zhao ladder";
index status "dead / ported," **no promise score**. §12(b): "Hessian false except possibly
HC(4) (RECON.md)." §12(c): "These were never JC2 methods. They were hope that a stronger,
more analytic statement would be easier. After July 2026 the ladder above JC(2) is a pile
of counterexamples." Cross-cutting: "The implication-ladder instinct is exhausted.
Mathieu, GMC(n≥3), **Hessian**, PC(2), JC(n≥3) are false. … 'Prove a stronger statement'
has been the wrong bet for thirty years and is now a documented massacre."

Grok writes **no sentence specific to HC4 ⇒ JC2**. The dissent is entirely class-level.

---

## 1. Ground truth on the citations (checked, not trusted)

- **arXiv:2607.22198** (Meng–Yang, July 2026): "A five-variable counterexample to the
  Hessian conjecture, and the low-dimensional status of the Jacobian and Hessian
  conjectures." HC(n) there is the **constant-Hessian-determinant** formulation:
  det Hess h ∈ C^× ⇒ ∇h is injective/an automorphism. Main result: explicit 5-variable,
  degree-14, det Hess = 128 polynomial with non-injective gradient — **HC5 is false** —
  built as a six-variable doubling of the Alpöge dim-3 Jacobian counterexample followed by
  a one-variable Schur descent (partial Legendre transform). The paper's ledger:
  "Exactly two statements remain unsettled, JC2 and HC4, **linked by HC4 ⇒ JC2**."
  RECON.md (lines 62, 74) records this paper as [CONTEXT] with exactly that ledger,
  so the bridge fact was **available to both surveyors**.
- **arXiv:2608.14217** (Ni, Aug 2026): "The Quartic Hessian Conjecture in Dimension
  Four." Proves the degree-4 case of HC4 in the constant-determinant formulation.
  Mechanism, per the paper: top form has det Hess ≡ 0, hence **is a cone by the
  four-dimensional homogeneous Hesse theorem (Gordan–Noether)**; cone representative split
  into three types (ternary/binary/unary quartic); one branch descends to the 3-dimensional
  Hessian conjecture via a **Schur complement**; an isotropic-cone rank analysis kills rank
  two. No obstruction module for degree 5 is defined in the paper.
- **This paper appears nowhere in RECON.md or any websweep through 2026-08-21.**
  Sol surfaced it independently; Grok cannot be faulted for not citing it, but Sol's
  citation is verified accurate, not fabricated.

Sol's two citations check out precisely, including the formulation and the "cone/Schur"
description of Ni's mechanism (with one nuance: Ni's "Schur" is a Schur *complement*;
Sol's proposed GL_4 *Schur-functor* decomposition is his own productive extension, not a
reproduction).

---

## 2. Question 1 — is the implication chain HC4 ⇒ JC2 valid?

**Yes, and it is independently provable in five lines**; it does not rest on trusting
either 2026 paper.

### 2.1 The bridge (Meng-style doubling, constant-determinant formulation)

Let F = (P,Q): C² → C² with det J_F = 1. Define
  h(x₁,x₂,y₁,y₂) := y₁P(x) + y₂Q(x) ∈ C[x₁,x₂,y₁,y₂].

Then in 2×2 block form
  Hess h = [ A   J_Fᵀ ]
           [ J_F   0  ],  A = y₁·Hess P + y₂·Hess Q.

Swapping the two block-rows (2·2 = 4 row transpositions, sign (−1)⁴ = +1) gives
det Hess h = det J_F · det J_Fᵀ = (det J_F)² = **1**, a nonzero constant. So ∇h is a
4-variable gradient Keller map and HC4 applies to h.

If F(a) = F(b) with a ≠ b, then ∇h(a,0) = (J_F(a)ᵀ·0, F(a)) = (0, F(a)) = ∇h(b,0):
any collision of F transfers to a collision of ∇h at y = 0. HC4 ⇒ ∇h injective ⇒ F
injective ⇒ F is an automorphism (injective polynomial self-maps of Cⁿ are automorphisms:
Ax / Białynicki-Birula–Rosenlicht / Cynk–Rusek). ∎

Degree bookkeeping: deg h = deg F + 1, so plane Keller maps of degree d sit inside HC4
at potential degree d+1.

### 2.2 The formulation caveat (this is where the exact citation matters)

The task hypothesis "presumably via the de Bondt–van den Essen symmetric/Hessian
reduction" is **wrong, and importantly so**. Two Hessian statements circulate:

- **(N)** Nilpotent form (de Bondt–van den Essen 2004, *JPAA* 193, 61–70; 2005,
  *Proc. AMS* 133, 2201–2205; Zhao, arXiv:math/0409534): Hess f nilpotent ⇒ x + ∇f
  invertible. The dBvdE reduction proves JC(all n) ⇔ symmetric-nilpotent case (all n,
  quartic homogeneous potentials) — it **raises dimension unboundedly** and yields no
  fixed-dimension bridge.
- **(D)** Constant-determinant form (Meng 2006, *Appl. Math. Lett.* 19, 503–510;
  Meng–Yang 2026): det Hess h ∈ C^× ⇒ ∇h an automorphism.

The doubling of §2.1 lands in **(D)**, not (N): Hess h above is *not* nilpotent in
general ((Hess h)² has diagonal block J_F J_Fᵀ ≠ 0). Under formulation (N), "HC4 ⇒ JC2"
is **not** a theorem by this argument. Meng–Yang and Ni both use (D), so the chain is
sound as cited. Sol's obstruction sentence "Nilpotence of the Hessian controls homogeneous
layers" imports (N)-vocabulary into a (D)-statement — loose, not fatal: the operative
condition on the top homogeneous layer is det Hess ≡ 0 (weaker than nilpotency), which is
exactly what Gordan–Noether consumes.

### 2.3 Computational verification

Exact integer polynomial arithmetic (no CAS trusted; script in session scratchpad):
det Hess(y·F) − (det J_F)² ≡ 0 verified as a *formal* identity for (i) the elementary
automorphism (x, y+x³), (ii) a degree-4 tame product, (iii) three dense random non-Keller
cubic pairs (the identity is formulation-level, not Keller-conditional); collision
transfer verified on F = (x₁², x₂): F(2,5) = F(−2,5) forces ∇h(2,5,0,0) = ∇h(−2,5,0,0).
All pass.

### 2.4 A sharpening neither party states: the sector decomposition

The y-linear sector of HC4 is **exactly** JC2, in both directions: if F is an
automorphism then ∇h is too, with polynomial inverse x = F⁻¹(v),
y = (J_Fᵀ∘F⁻¹)⁻¹u (polynomial because det J_F = 1 makes the adjugate the inverse).
Hence

  **HC4 = JC2 ⊕ (a strictly larger bulk of genuinely 4-dimensional gradient maps).**

Consequences cutting both ways:
- *Pro-Grok:* HC4 is strictly stronger than JC2. Any HC4 proof must re-prove JC2 rung by
  rung, plus extra. Quintic HC4's JC2-relevant sector is plane Keller of degree ≤ 4 —
  classical (Wang 1979 degree 2; Moh ≤ 100). **Rung five, even if proved, yields zero new
  JC2 theorem.** The degree tower in fixed dimension 4 is infinite; the quantification
  over all degrees is the theorem. This is Grok's own §13 Conjecture-E critique, verbatim
  transferable: "holding at the smallest instance is the least surprising thing in the
  world if JC2 is true."
- *Pro-Sol:* the reformulation buys a **degree-uniform structure theorem unavailable in
  the plane formulation**: Gordan–Noether (below) constrains the top form of *every*
  degree at once. That is a real mechanism, not vocabulary.

**Verdict Q1: the chain is VALID as Sol states and cites it** (constant-determinant
formulation), with one flagged imprecision (nilpotence wording) and one unstated but
material structural fact (y-linear sector ⇔ JC2).

---

## 3. Question 1½ — is HC4's survival signal or survivorship?

This is the actual crux of the dissent, and it has a definite mathematical answer:
**the survival boundary is structural, not accidental.**

- Hesse's claim — a homogeneous form with identically vanishing Hessian determinant is a
  cone (drops a variable after linear change) — is a **theorem for n ≤ 4 variables
  (Gordan–Noether 1876)** and **false for n ≥ 5** (Perazzo cubics, e.g.
  x₁x₄² + x₂x₄x₅ + x₃x₅²).
- The 2026 massacre tracks this boundary exactly: HC(2n≥6) false by doubling the dim-3
  counterexample (the §2.1 construction applied to Alpöge/Gao is constructive); HC5 false
  by Meng–Yang's Schur descent 6 → 5; the descent machinery **stalls at 4**, precisely
  where every top form is forced to be a cone in ≤ 3 variables and Ni's case analysis
  becomes available. HC4 is not "the rung the counterexamples haven't reached yet"; it is
  the unique dimension where the Jacobian-side counterexample factory loses its geometric
  room *and* a classical structure theorem switches on. Dimension 4 = 2·2 is also the
  unique doubled dimension relevant to the plane.
- Contrast with the genuinely dead ladder entries (Mathieu/SU(2), GMC(n≥3), PC(2)):
  those had no dimension-specific protective structure; they died wherever tested.

Grok's "documented massacre" framing, applied to HC4, ignores that the massacre's own
mechanism (doubling + Schur descent) is what certifies HC4 as the terminal protected case.
His cross-cutting line "Hessian … false" is, as written, **wrong for n = 4 and
contradicts his own §12(b)** ("false except possibly HC(4)").

---

## 4. Question 2 — is the "quintic obstruction module under GL_4" a well-defined finite object with the claimed computability?

**Well-defined after one formulation step (which Sol's own spec includes as its first
task), finite, and the first-term decomposition is genuinely cheap. The full quintic case
is not guaranteed cheap.** No cited paper defines the module; Ni's paper stops at quartic
with no degree-5 apparatus. "Formulate the exact quintic obstruction module" is honest
labeling by Sol — the object is his to define — and there is a canonical candidate:

**Canonical construction.** Let h = h₂ + h₃ + h₄ + h₅, hᵢ ∈ Symⁱ(C⁴)*, with
det Hess h = c ∈ C^× (no constant/linear part WLOG). Then:
1. Evaluating at 0: det Hess h₂ = c ≠ 0, so h₂ is nondegenerate; GL₄-normalize h₂ to the
   standard quadric, residual gauge O(4,C) (dim 6).
2. Grade det Hess h − c by x-degree: layers k = 12 down to 0. Top layer:
   det Hess h₅ ≡ 0 (in Sym¹²(C⁴)*, dim 455). Gordan–Noether ⇒ h₅ is a cone ⇒ after
   residual rotation h₅ ∈ Sym⁵(C³)* (dim 21), with an isotropic/anisotropic vertex case
   split exactly parallel to Ni's quartic rank analysis.
3. The **obstruction module** is the graded system of remaining layers (k = 11,…,0) of
   det Hess h − c after cone normalization, as modules over the residual reductive gauge;
   its "first uncancelled term" is the lowest layer whose conditions cannot be absorbed by
   the free lower forms h₄, h₃. The layer-11 piece is trilinear in h₅, linear in h₄,
   landing in Sym¹¹(C⁴)* (dim 364).

**Size arithmetic (the computability claim, checked).** Parameter space:
dim(Sym³⊕Sym⁴⊕Sym⁵) = 20+35+56 = 111 (h₂ fixed), ≈105 effective mod residual gauge.
Equations: all coefficients of det Hess h − c, Σ_{k≤12} dim Symᵏ(C⁴) = C(16,4) = **1820**
equations, each of degree ≤ 4 in the 111 parameters. Every layer is a finite
GL₄-equivariant object (det Hess(h∘g) = (det g)²·(det Hess h)∘g, so the locus is
GL₄-stable); the needed plethysms (Sym⁴(Sym⁵C⁴) → Sym¹²C⁴, dim 455 target, etc.) are
seconds in LiE/Sage. The *first uncancelled term and its GL₄ decomposition* — Sol's
actual experiment — is days of work on hardware the campaign already has, no F4 monsters.
The *full* quintic case is a Ni-scale case-tree (his quartic needed three cone types plus
rank analysis; quintic cones give ternary/binary/unary quintics plus isotropy splits) —
a paper-scale effort, not an afternoon.

**Verdict Q2: yes, finite and computable at the first-experiment level; "exact quintic
obstruction module" is a to-be-defined program name with a canonical finite candidate,
not an existing object.** Sol's computability claim holds for what his experiment
actually runs; it would be an overclaim for the full quintic theorem.

---

## 5. Question 3 — is Grok's dissent sound, or a strawman?

Neither exactly; it is a **valid discount attached to an invalid classification, with
zero instance-level engagement.**

What fails:
1. **Misclassification against his own rules.** Grok's stated convention: promise scores
   for every campaign-untried lane. HC4 is untried (Sol: "No executed attack"; nothing in
   the repo contradicts this). Grok avoids scoring by filing it "dead / ported" — while
   his own §12(b) concedes "except possibly HC(4)." Internally inconsistent.
2. **Factual overstatement.** Cross-cutting "Hessian … false" is false for the only case
   under dispute.
3. **No engagement with the distinguishing mathematics.** The HC4 ⇒ JC2 ledger was in
   RECON.md (which he cites in the same sentence); he says nothing about the doubling
   bridge, nothing about Gordan–Noether, nothing about why the counterexample factory
   stalls at n = 4. His dissent attacks the ladder-class; the instance has exactly the
   properties (fixed dimension, proved implication, degree-uniform structural tool,
   finite decidable rungs, built-in falsification channel) his class argument does not
   address. This is not a strawman of Sol's position — he never addresses Sol's position
   at all.

What holds:
4. **The structural discount is correct and important.** HC4 is strictly stronger than
   JC2 (§2.4); the degree tower is infinite with no finite reduction; quintic success
   would carry little JC2 evidence since its JC2-sector is classical. Grok's §13 argument
   applies verbatim — he simply never wrote it down for this lane. A hypothetical plane
   counterexample of degree d kills HC4 at potential degree d+1, so HC4 also inherits all
   of JC2's disproof risk plus its own.
5. His demand elsewhere ("refuse to start until a 10-line definition is written") is,
   ironically, *satisfied* here — §2.1 is that ten lines — but he did not check.

**Verdict Q3: as written, Grok's dissent does not hold against this lane.** Its salvage
value is the score discount in point 4, which is real and which Sol's 9/10 fails to price.

---

## 6. Question 4 — VERDICT

**BOTH-PARTLY, with the mathematics of the disputed object siding with Sol and the
magnitude siding partly with Grok.** Precise partition:

| Sub-question | Winner | Basis |
|---|---|---|
| Implication chain HC4 ⇒ JC2 valid? | **Sol** | §2.1 proof + exact-arithmetic check; citations verified (constant-det formulation) |
| Correct formulation cited (Meng–Yang, not dBvdE-nilpotent)? | **Sol** | §2.2; the nilpotent form would *not* give a fixed-dimension bridge |
| HC4 survival = signal or survivorship? | **Sol** | §3: Gordan–Noether boundary at n = 4 is exactly where the CE factory stalls |
| Quintic obstruction module well-defined/finite/computable? | **Sol, qualified** | §4: canonical finite candidate; "formulate" is part of the work; full quintic ≠ cheap |
| "Nilpotence controls layers" phrasing | **Grok-direction** | §2.2: loose import of the wrong formulation's vocabulary |
| HC4 strictly stronger than JC2; rung-5 gives no new JC2 theorem | **Grok** | §2.4: y-linear sector ⇔ JC2; quintic covers plane deg ≤ 4 only (Wang/Moh) |
| Infinite tower, smallest-rung success weak evidence | **Grok** | his §13 critique transfers verbatim |
| Grok's classification ("dead/ported"), refusal to score, "Hessian false" summary | **Sol** | §5 points 1–3: inconsistent with his own rules and his own §12(b) |
| Sol's 9/10 | **Neither** | inflated; see below |

**Honest promise scores (mine).**
- On **Sol's semantics** (expected research information from the cheapest first
  experiment): **6.5/10**. Top-three untried lane, at or just below the symplectic
  primitives experiment on cost-adjusted information. Not 9: the modal outcome is a hard
  coupled-layer case tree; the two high-information outcomes (a quintic HC4
  counterexample, which kills the bridge's utility while leaving JC2 open; or a visibly
  degree-uniform GN mechanism) are genuine but not modal, and even full quintic success
  adds no new JC2 statement — the JC2 payoff requires the further hop "the bulk mechanism
  is uniform in degree."
- On **Grok's semantics** (P(checkable JC2 proof or char-0 counterexample from this lane
  at multi-year intensity)): **2.5–3/10**. Above his 1–2 dead band — this lane, unlike the
  dead rungs, owns a degree-uniform structural tool and an active 2026 literature — but
  the infinite tower and the strictly-stronger burden dominate.
- The two surveys' numbers are not on one scale (APPROACHES.md already says so); the
  adjudicated dissent is really: *Sol 9 is too high by ~2.5 on his own scale; Grok's
  refusal to score at all was wrong on his own rules, and his implied ≤2 is too low by
  ~1 on his.*

---

## 7. First-experiment spec (viable; est. 3–10 days, no F4 jobs)

**HC4-Q5: quintic obstruction module, first uncancelled term, plus two controls and one
kill-probe.**

- **Step 0 — bridge harness (half a day).** Re-verify det Hess(y·F) = (det J_F)² and the
  collision-transfer lemma in the campaign's exact-arithmetic stack (done once in this
  adjudication's scratchpad; port into `cases/`). Negative control: double Mondello's
  char-2 plane collision — it must produce a 4-variable char-2 gradient-Keller collision
  (the char-2 analog of "HC4 false"), confirming the harness detects failure.
- **Step 1 — quartic replay (1–2 days).** Reproduce Ni's pipeline symbolically for
  degree 4: h₂-normalization, top-form det Hess ≡ 0, Gordan–Noether cone extraction,
  the three cone types, the Schur-complement descent branch. Deliverable: a verified
  executable normal form, not a reading note.
- **Step 2 — quintic module (2–3 days).** Implement §4's construction: cone-normalize
  h₅ ∈ Sym⁵(C³)*, grade det Hess h − c into layers 11…0, and compute the first
  uncancelled term as a module over the residual gauge; decompose it under
  GL₃×GL₁-plethysm (LiE/Sage). Deliverable: the explicit irrep list with multiplicities.
- **Step 3 — discriminator.** (a) If every irrep in the first uncancelled term already
  occurs in the quartic kill list → attempt the degree-induction lemma (the actual prize).
  (b) If new irreps appear → their highest-weight vectors are candidate counterexample
  directions to quintic HC4; Gröbner/numerically test the smallest (bounded: ≤105
  parameters, quartic equations, massive symmetry). A surviving branch is a candidate HC4
  counterexample = bridge-kill = major news either way.
- **Sector control (half a day).** Run the identical machinery on the y-linear sector
  (h = y₁P + y₂Q, deg P,Q ≤ 4) and confirm it reproduces exactly the known plane
  degree-≤4 story. Any mismatch is a bug in the formulation, caught cheaply.
- **Kill-probe (1 day, parallel).** Attempt Meng–Yang's own Schur descent 5 → 4 on their
  degree-14 example and document the *exact* obstruction (expected: GN/isotropy). If the
  descent unexpectedly passes, HC4 is false, the lane closes, and JC2 is untouched —
  the cheapest possible falsification of the entire dispute.

Priority within APPROACHES.md §4: this spec supports keeping the lane at shortlist
position 2 (behind symplectic primitives on cost), with the corrected score 6.5, and
adds the kill-probe as its cheapest first move.

---

## 8. One-paragraph summary for DC

The disputed implication is a theorem: HC4 (constant-Hessian-determinant form) ⇒ JC2, by
the y·F(x) doubling, provable in five lines and machine-verified here; Sol's citations
(Meng–Yang bridge + 5-variable counterexample; Ni's quartic HC4 via Gordan–Noether cones)
check out exactly, including one paper (Ni) absent from all campaign recon. Dimension 4
is structurally protected (Gordan–Noether holds iff n ≤ 4; the 2026 counterexample
factory stalls exactly there), so HC4's survival is signal, not survivorship — Grok's
"dead ladder" filing, his refusal to score an untried lane, and his "Hessian false"
summary line are all wrong on the specifics. But Grok's structural discount is right
where it touches: HC4 is strictly stronger than JC2 (its y-linear sector *is* JC2), the
degree tower is infinite, and the quintic rung's JC2-content is the long-known degree-≤4
plane case, so Sol's 9/10 overprices the first experiment by roughly 2.5 points on his
own scale. Verdict: BOTH-PARTLY — Sol carries the mathematics, Grok carries part of the
score, and the lane is live at 6.5/10 with the spec in §7.
