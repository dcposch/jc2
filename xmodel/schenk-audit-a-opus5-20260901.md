# AUDIT-A-OPUS5 — Hostile audit of Schenk, "A valuation-theoretic proof of the Jacobian conjecture in dimension two" (Zenodo 18622130)

Lane: AUDIT-A-OPUS5 · Date: 2026-09-01 · Stance: default to refutation
Inputs (SHA-256 verified):
- `6ba4088386eb40affbb4abad54bb8e1574de09d00da9d1fbeac9f5c88d160f24` schenk_jc2_zenodo18622130.pdf
- `23fab48635178dd905d67be2b9d0eeb8574b641be0d097c82af4a55bf4fcc7d4` web-sweep-20260901-grok46.md
- `763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9` block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md

## 0. Verdict

## 1. Provenance and physical description of the source

## 2. Reconstructed logical skeleton

## 3. Lemma-by-lemma audit

## 4. The U-HIT boundary-killing step

## 5. The Rees degeneration of affine dicriticals

## 6. The two-form positivity step

## 7. The finite-etale / ZMT endgame

## 8. Cross-check against promoted campaign machinery

## 9. Verdict detail, repairability, and successors

## 10. Execution log and disclosure

---

*(The headers above are the outline. Full text follows.)*

## 0. Verdict

**FATALLY-FLAWED.** The paper does not prove JC2. Four independent defects
are each individually fatal; three of them are located in the two steps the
author himself designates as the load-bearing ones.

**(V1) §10.4, the closing contradiction, rests on a non sequitur.** The
sentence *"D dominates a curve in A², hence meets the affine chart U"* is
false as stated. `D ⊂ X₀` is a curve in the **source-side** normalized
graph; `U ⊂ X₀` is the affine graph, i.e. a copy of the **source** `A²`;
`f(D) ⊂ A²` is in the **target**. Every `D ⊂ X₀` has image in the target
affine chart by construction of `X₀ = π₂⁻¹(A²)`; that says nothing about
`D ∩ U`. The divisors that matter are exactly those with `D ∩ U = ∅`. The
implication needed here is precisely Theorem 5.3 (U-HIT) — which §10.4 does
not cite. Grep confirms Theorem 5.3 is cited **nowhere** in Chapters 6–12.

**(V2) Theorem 5.3 (U-HIT) selects a point from a provably empty set.**
Its proof says "Choose `s ∈ C ∩ S° ∩ S°°`. This intersection is nonempty
since all three sets are dense open." `C = f(D)` is a closed irreducible
**curve**, not a dense open. Worse, I prove in §4 below that
`C ∩ S°° = ∅` **always**, directly from the defining property of `S°°`
(finiteness of `f|_U` over it). The chosen `s` does not exist. What
Lemmas 5.1+5.2 actually establish — `f(X₀∖U) ∩ (S°∩S°°) = ∅` — is a
restatement of the definition of `S°°`, with zero content.

**(V3) Lemma 10.2 ("branch divisors force `a+b>0`") is false.** Its
conclusion, `ord_D(P) + ord_D(Q) > 0`, says the branch curve `C` is
contained in a **target coordinate axis** `{P=0} ∪ {Q=0}`. All hypotheses
are invariant under target translation `(P,Q) ↦ (P−α, Q−β)`, which is again
a Keller map with the same `X`, `X₀`, `U`, `D`, `C` up to translation; the
conclusion is not. Choosing `α, β` with `C ⊄ {P=α}`, `C ⊄ {Q=β}` (possible
for any irreducible curve) yields `a = b = 0`. Its proof repeats the V1
confusion verbatim ("the generic point of `D` lies in this locus").

**(V4) Chapter 9 (Wedge Strictness) is vacuous in its intended
application, and Chapters 7–8 never discharge its hypotheses.** For a
dicritical `D`, `a>0` and `b>0` cannot both hold (they would force
`f(D) ⊆ V(P) ∩ V(Q) = {origin}`), so Case 1 — the only case whose proof
does real differential work — is empty. In Cases 2 and 3 the required
character relation `v₀ⁿ = c ∈ k×` forces `v₀` algebraic over `k`, hence
`v₀ ∈ k` by the paper's own Lemma 8.7; but dicriticality forces `v₀ = Q|_D`
**nonconstant**. So the hypothesis set of Lemma 9.1 is empty at every
divisor Chapter 10 feeds it. Separately, the descent to `c ∈ k×`
(Lemma 8.9 / Cor. 8.10) requires a relation `H ∈ k[U,V]`, which is never
produced and provably fails in Cases 2–3.

Chapter 7's dimension transport is independently broken: Lemma 7.5's
special-fibre identification is a surjection, not an isomorphism;
Lemma 7.7's proof asserts `trdeg_k k(P,Q) = 1` when the correct value is 2;
and Corollary 7.8 has an explicit counterexample at `F = id`.

No repair is available from the campaign's promoted machinery: §8 shows the
step Schenk asserts for free (`ord_D(dP∧dQ) = 0`) is, in our frame,
*equivalent* to `μ_D = 1` — the unramified-dicritical case that our
Theorem 7.B needed a long argument and hypothesis H2 to reach. The paper
silently assumes the hardest hypothesis in the subject.

## 1. Provenance and physical description of the source

- Zenodo record 18622130, file `Jacobi in N=2.pdf`, 569 113 bytes,
  SHA-256 `6ba4088386eb40affbb4abad54bb8e1574de09d00da9d1fbeac9f5c88d160f24`
  (verified against the frozen copy; matches web-sweep item F8).
- PDF metadata: `pdfTeX-1.40.27`, "LaTeX with hyperref", CreationDate
  2026-02-12 09:38:47 PST, 53 pages A4, no Title/Author metadata fields.
- Byline: Philipp Schenk, `PhilippSchenk6@web.de`. No institutional
  affiliation, no acknowledgements, no arXiv posting. 17-item bibliography,
  all textbooks/EGA/SGA/Stacks plus BCW and van den Essen; **no research
  paper on dicritical divisors, Jelonek sets, or the Abhyankar–Moh /
  Orevkov/Miyanishi literature is cited.** For a claimed resolution of JC2
  this is itself a strong prior against soundness.
- Internal hygiene defects consistent with rapid drafting: Lemma 3.4 and
  Lemma 3.5 are verbatim duplicates; bibliography items [11] and [12] are
  the identical Matsumura entry; Lemma 7.4 is captioned "Lemma 7.2a";
  Lemma 7.6's proof cites "Lemma 7.3" which does not exist; Chapter 8
  declares `a, b ∈ Z_{>0}` while Chapters 6/7/9/10 only supply `a, b ≥ 0`;
  Appendix lemmas are numbered `.5`–`.9`. Chapter 9's `R = X₀,η_D` is
  missing its `O`.
- The historical paragraph (p. 1) still records JC2 as open, consistent
  with a February 2026 draft.

Extraction: `pdftotext -layout` and plain `pdftotext` (both 1 935 lines);
displayed formulas were cross-read in both modes to guard against the
known stacked-fraction inversion artefact. No formula relied on below
involves a nested fraction.

## 2. Reconstructed logical skeleton

Notation as in the paper. `F = (P,Q): A² → A²` with `det DF ∈ k×`,
`char k = 0`, `k = k̄`.

| Stage | Object | Statement | Consumes |
|---|---|---|---|
| S1 | `Γ_F ⊂ P²×P²`, `ν: X → Γ_F` normalization | `X` normal projective surface (L2.1, L2.6) | Hartshorne II.6.3 |
| S1 | `X₀ := π₂⁻¹(A²_target)`, `f := π₂\|_{X₀}` | `f` proper, dominant (L3.1, L2.3) | Stacks 01W6 |
| S1 | `U ⊂ X₀` = affine graph `≅ A²_source` | `f\|_U = F` (L2.4) | normalization iso on smooth locus |
| S2 | Stein `f = σ∘ρ` | `ρ` proper connected fibres and **birational**; `σ` finite; `Y₀` normal (P3.2, L3.3, L3.4/3.5) | EGA III 4.3.3 |
| S2 | `d := [k(Y₀):k(A²)]` | `∃ S° ⊂ A²` dense open, `σ` finite flat of rank `d` (L4.1) | generic freeness |
| S2 | — | `∃ S°° ⊂ A²` dense open, `f\|_{U∩f⁻¹(S°°)}` **finite** étale of degree `d` (L4.2) | ZMT |
| S3 | **U-HIT** (T5.3) | no irreducible `D ⊂ X₀∖U` with `dim f(D) = 1` | L5.1 (`length f⁻¹(s)=d` on `S°`), L5.2 (`length f⁻¹(s)∩U=d` on `S°°`), additivity of length |
| S4 | `R = O_{X₀,η_D}`, `t`, `κ(D)`; `a=v(P)`, `b=v(Q)`, `P=tᵃu`, `Q=t^b v`, `u₀,v₀ ∈ κ(D)×` | `gr_v R ≅ κ(D)[T]`; initial forms `F₀=u₀Tᵃ`, `G₀=v₀T^b` (Ch. 6) | DVR theory |
| S4 | Rees `R = R[ts]`, `B = im(k[s][U,V] → R)` | `R`, `B` flat over `k[s]` (L7.1, L7.2); `B` domain, dominant (L7.4) | torsion-free over PID |
| S4 | fibres | `B_η ≅ im(k(P,Q)→Frac R)`, `B₀ ≅ κ(D)[F₀,G₀]` (L7.5) | — |
| S4 | transport | `dim B₀ ≥ dim B_η` (L7.6); `dim B_η ≥ 1` if `D` dicritical (L7.7); hence `dim κ(D)[F₀,G₀] ≥ 1` (C7.8) | EGA IV 5.6.5 |
| S4 | rank dichotomy | **assume** `dim B = 1` ⟹ `ht I = 1` ⟹ `I=(H)` ⟹ `∃(m,n)≠0`, `c ∈ κ(D)×`: `ma+nb=0`, `u₀^m v₀^n = c` (L8.1–T8.3) | UFD, Laurent independence |
| S4 | descent | **if** `∃ H ∈ k[U,V]` with `H(F₀,G₀)=0` **and** `dim κ(D)[F₀,G₀]=1`, then `c ∈ k×` (L8.9, C8.10) | — |
| S5 | **Wedge strictness** (L9.1) | `a,b≥0`, `a+b>0`, plus character relation with `c ∈ k×` ⟹ `ord_D(dP∧dQ) ≥ a+b > 0` | `Ω¹` conormal sequence |
| S5 | branch lift (L10.1) | `σ` not étale ⟹ `∃ D ⊂ X₀` prime, `f(D) = C` a branch component; `D` dicritical | Zariski–Nagata purity + `k(X₀)=k(Y₀)` |
| S5 | (L10.2) | such `D` has `a+b>0` | — |
| S5 | §10.4 | L9.1 gives `ord_D(dP∧dQ) > 0`; Keller gives `ord_D(dP∧dQ)=0` "since `D` meets `U`"; contradiction ⟹ `σ` étale (T10.3) | Keller identity |
| S6 | (T11.1, C11.2) | `π₁^{ét}(A²_k)=0` ⟹ `σ` iso | Riemann existence, SGA 1 XII/XIII |
| S7 | (P12.1, L12.2–12.4) | `f` birational ⟹ `F` birational étale ⟹ ZMT ⟹ `F` iso | ZMT, normality |

Two structural observations before the audit proper.

**(A) U-HIT is not an auxiliary lemma; it is the theorem.** If no component
of `X₀∖U` dominates a curve then, since `U` is affine and dense in the
irreducible surface `X₀`, `X₀∖U` is either empty or pure of codimension one;
in the latter case all its components are contracted, so `T := f(X₀∖U)` is
finite and `F` is finite over `A²∖T`. The non-properness (Jelonek) set of a
dominant polynomial map `A²→A²` is empty or pure of codimension one, so it
is empty; `F` is proper, hence finite, hence — being étale with
`π₁^{ét}(A²)=0` — an isomorphism. Thus **U-HIT ⟹ JC2 with none of
Chapters 6–10.** A proof of U-HIT by generic-locus bookkeeping alone would
be extraordinary, and §4 shows it is not one.

**(B) The Chapters 6–10 core is used to contradict `ord_D(dP∧dQ)=0`, an
identity that itself holds only for divisors meeting `U`.** So the core and
U-HIT are not independent routes: Chapter 10 needs U-HIT, and U-HIT already
suffices. The architecture is circular at the level of what each part
delivers.

## 3. Lemma-by-lemma audit

Verdicts: **V** verified, **G** gap (statement plausible, proof incomplete),
**F** false (countermodel or refutation given), **VAC** true but vacuous in
the intended application.

| # | Verdict | Note |
|---|---|---|
| L2.1–2.6 | V | Standard. `X₀` normal integral surface; codim-1 points are DVRs. |
| L3.1 | V | Proper restricted over an open of the target. |
| P3.2, L3.3 | V | Stein factorization; `Y₀` = normalization of `A²` in `k(X₀)`. |
| L3.4 / L3.5 | V | Duplicated statement. `ρ` birational. The clause "since `f` is dominant, `k(A²) ⊂ k(X₀)` is finite" needs generic finiteness (`f` proper, equidimensional) rather than dominance alone; harmless. |
| L4.1 | V | Generic freeness for the coherent sheaf `σ_*O_{Y₀}`. |
| L4.2 | V | `F` étale hence quasi-finite; ZMT + shrinking. Degree `d` identification correct via `k(U)=k(X₀)=k(Y₀)`. |
| L5.1 | G | `length f⁻¹(s) = d` presumes `f⁻¹(s)` finite and presumes `(f_*O_{X₀})⊗κ(s) ≅ O_{f⁻¹(s)}`. `f` contracts curves in general, so fibres over the (finitely many) images of contracted curves are 1-dimensional and have no finite length; base change also needs `f` finite near `s`. Repairable by shrinking `S°` to the (open, dense) locus where `f` is finite. |
| L5.2 | V | Correct on `S°°`. |
| **T5.3 (U-HIT)** | **F** | Selects `s ∈ C ∩ S° ∩ S°°`; §4 proves `C ∩ S°° = ∅`. See §4. |
| R5.4 | F | The boast that U-HIT needs "no global quasi-finiteness" is exactly the defect: the proof lives entirely on the locus where quasi-finiteness/finiteness of `f\|_U` is a hypothesis. |
| L6.1, L6.2 | V | `P,Q` regular on `X₀` ⟹ `a,b ≥ 0`; constant field of `κ(D)` is `k`. |
| Ch. 6 gr | V | `gr_v R ≅ κ(D)[T]`; initial forms as stated. |
| L7.1, L7.2 | V | Torsion-free over the PID `k[s]` ⟹ flat. Correct. |
| L7.4 | V | `B` domain, dominant over `k[s]`. |
| **L7.5** | **F** | *Special fibre.* `B/(s) ↠ im(B → R/sR)` need not be injective: the kernel is `(B ∩ sR)/sB`. Also `im(k[U,V] → gr_v R) = k[F₀,G₀]`, **not** `κ(D)[F₀,G₀]` — nothing puts the coefficient field `κ(D)` in the image. See §5 for an explicit failure. |
| **L7.7** | **F (proof)** | Concludes `trdeg_k k(P,Q) = 1` from `trdeg ≥ 1` and `k(P,Q) ⊆ k(X₀)`, `trdeg k(X₀)=2`. Non sequitur; the true value is **2**, since `F` is dominant so `P,Q` are algebraically independent. The stated inequality `dim B_η ≥ 1` survives. |
| L7.6 | G | `dim B = dim B_η + 1` is the dimension formula for dominant finite-type morphisms, fine; the fibre inequality is fine. But combined with the correct `dim B_η = 2` it forces `dim B₀ ≥ 2`, which is incompatible with `B₀ ⊆ κ(D)[T,T⁻¹]` (`dim ≤ 1`). The framework is internally inconsistent; the inconsistency localizes in L7.5. |
| **C7.8** | **F** | Counterexample in §5 with `F = id`. |
| L8.1, L8.2 | V | `I` prime of height 1 in a 2-dim UFD is principal. |
| **T8.3** | **V** | Correct *given* `dim B = 1` (which does hold whenever `a+b>0`, since `κ(D)[F₀,G₀] ⊆ κ(D)[T,T⁻¹]` has dimension `≤1` and `=1` iff `(a,b)≠(0,0)`). Note this makes Chapter 7 unnecessary for Chapter 8 — and Chapter 7 is where the errors are. Yields `c ∈ κ(D)×` only. |
| R8.4, R8.5, L8.7, R8.8 | V | Honest and correct; R8.8 correctly warns against false descent. |
| L8.9 / C8.10 | V(conditional) | Correct given a relation `H` with coefficients in `k`. **Hypothesis never discharged**, and §6 shows it provably fails at every divisor Chapter 10 supplies. |
| **L9.1** | **VAC** | Case 1 (`a>0,b>0`) is impossible for dicritical `D`; Cases 2–3 have contradictory hypotheses. See §6. Case-1 algebra, where non-vacuous, is correct. |
| L10.1 | V | Zariski–Nagata purity (`Y₀` normal, `A²` regular) + `k(X₀)=k(Y₀)` + normality of `X₀`. Sound. |
| **L10.2** | **F** | Translation-equivariance refutation, §6. Proof also commits the `U` confusion and the leap "nonzero in `Ω²_{Frac R}` ⟹ nonzero in `Ω²_{R}⊗κ`". |
| **§10.4** | **F** | "`D` dominates a curve in `A²`, hence meets the affine chart `U`" — non sequitur; U-HIT not cited. |
| T10.3 | V(conditional) | Purity step correct once codim-1 ramification is genuinely excluded. |
| T11.1, C11.2 | V | Standard; spreading out, Riemann existence, SGA 1 XIII 2.12. |
| P12.1 | V | — |
| **L12.2** | **F** | "`O(U) = k[x,y]` for every dense open `U ⊂ A²`" is false: `U = A²∖{x=0}` has `O(U) = k[x,y][1/x]`. The cited normality argument extends functions across codimension **≥ 2**, not codimension 1. |
| L12.3 | G | Statement true; proof leans on the false L12.2. Repair: `O(U) = k[y₁,…,y_n]` because `U ≅ A^n` via the birational open immersion, then a nonconstant `f` cannot become a unit. |
| L12.4, §12.4 | V | Standard ZMT endgame. |

## 4. The U-HIT boundary-killing step (Theorem 5.3) — FALSE

### 4.1 The stated proof

Assume `D ⊂ X₀∖U` irreducible with `C := f(D)` a curve. Choose
`s ∈ C ∩ S° ∩ S°°`, "nonempty since all three sets are dense open". Then
`length f⁻¹(s) = d` (L5.1) and `length(f⁻¹(s) ∩ U) = d` (L5.2), so by
additivity `f⁻¹(s) ∩ (X₀∖U) = ∅`, contradicting `D ∩ f⁻¹(s) ≠ ∅`.

### 4.2 The defect

`C` is a **closed irreducible curve**, not a dense open subset. The
justification offered for nonemptiness of the intersection is simply not
about the right kind of set. This alone voids the proof. But the situation
is worse: the intersection is provably empty.

**Proposition 4.1.** Let `S°° ⊂ A²` be any open subset such that
`f|_{U ∩ f⁻¹(S°°)} : U ∩ f⁻¹(S°°) → S°°` is finite (this is exactly the
defining property supplied by Lemma 4.2). Then
`f(X₀ ∖ U) ∩ S°° = ∅`.

*Proof.* Put `V := f⁻¹(S°°)`, open in `X₀`, nonempty because `f` is
surjective (`f` proper and dominant). Then `U ∩ V → S°°` is finite, hence
proper, and `V → S°°` is separated; therefore the inclusion `U ∩ V ↪ V` is
proper (if `g∘h` is proper and `g` separated then `h` is proper; Stacks
Tag 01W6). A proper immersion is a closed immersion, so `U ∩ V` is closed
in `V`. It is also open in `V`, and dense (`U` is dense in the irreducible
`X₀`). An open, closed, nonempty subset of an irreducible space is
everything, so `U ∩ V = V`, i.e. `V ∩ (X₀∖U) = ∅`. Any `s ∈ f(X₀∖U) ∩ S°°`
would give a point of `V ∩ (X₀∖U)`. ∎

**Corollary 4.2.** For every `D ⊂ X₀∖U`, `C = f(D)` satisfies
`C ∩ S°° = ∅`. Hence `C ∩ S° ∩ S°° = ∅` and the point `s` chosen in the
proof of Theorem 5.3 does not exist.

**Corollary 4.3.** The conjunction of Lemmas 5.1 and 5.2 delivers exactly
`f(X₀∖U) ∩ (S° ∩ S°°) = ∅`, which by Proposition 4.1 is already implied by
the definition of `S°°` alone. The fibre-length bookkeeping of Chapter 5
contributes no information whatsoever. Remark 5.4's claim that U-HIT is
"a purely fibre-length theoretic separation argument, independent of any
global quasi-finiteness input" inverts the truth: the argument is confined
to the locus on which finiteness of `f|_U` was *assumed*, and the entire
difficulty of JC2 sits on the complement.

The geometric content of Proposition 4.1 is classical and is the reason
U-HIT cannot be cheap: `A² ∖ S°°` contains the non-properness (Jelonek) set
of `F`, and the image of a horizontal boundary curve **is** a component of
that set. Schenk's `s` is required to lie simultaneously on the
non-properness curve and in a locus where `F` is proper.

### 4.3 U-HIT is equivalent to the theorem

**Proposition 4.4.** If Theorem 5.3 holds for `F`, then `F` is an
automorphism — using only Chapters 11 and 12 of the paper.

*Proof.* Let `Z := X₀ ∖ U`, closed in `X₀`. By U-HIT every irreducible
component of `Z` is either a point or a curve `D` with `dim f(D) = 0`. As
`f` is proper, `T := f(Z)` is a closed set which is a finite union of
points, hence finite. Then `f⁻¹(A²∖T) ∩ Z = ∅`, i.e.
`f⁻¹(A²∖T) ⊆ U`. Writing `W := A²∖T` and using `U ≅ A²_source` with
`f|_U = F`, we get `F⁻¹(W) = f⁻¹(W)`, and `f⁻¹(W) → W` is proper (base
change of the proper `f`) and quasi-finite (`F` is étale), hence finite.
So `F : A² ∖ F⁻¹(T) → A² ∖ T` is finite étale of degree `d`, with
`F⁻¹(T)` finite (`F` is quasi-finite).

Both source and target here are `A²` minus a finite set. Over `C` such a
space is connected and simply connected (removing a real-codimension-4
subset changes neither), so by the argument of Theorem 11.1 verbatim
(spreading out, embedding into `C`, Riemann existence, SGA 1 XIII 2.12) it
has trivial étale fundamental group. A connected finite étale cover of
degree `d` of a space with trivial `π₁^{ét}` forces `d = 1`. Hence `F` is
birational, and birational + étale gives an isomorphism by Chapter 12. ∎

Consequently Chapters 6–10 are logically redundant given Chapter 5, and
Chapter 5 is not an auxiliary separation lemma but a restatement of JC2.
A three-page fibre-length argument establishing it would be prima facie
implausible; §4.2 shows it establishes nothing.

### 4.4 Comparison with the campaign's purity/branch machinery

Nothing in our promoted results conflicts with the *statement* U-HIT — it
is true iff JC2 is true. What our frame supplies, and Schenk lacks, is a
mechanism: the boundary `X₀∖U` is where the dicriticals live, its image is
the curve `A_F` (Jelonek/non-properness set), and controlling it requires
the branch-topology, monodromy, and weighted-budget input of the
block-descent chain (Theorem 7.B and its `Σμ_l ≤ N−2` budget), not generic
freeness. Schenk's only genuine use of purity — Zariski–Nagata in
Lemma 10.1 and Theorem 10.3, with `Y₀` normal and `A²` regular — is
correctly applied and is not the problem.

## 5. The Rees degeneration (Chapter 7) — broken, and inessential

### 5.1 The family does not exist as written

`R := ⊕_{m≥0}(t^m)s^m = R[ts] ⊂ R[s]` is the **ordinary** Rees algebra.
Schenk asserts "the morphism `π : Spec(R) → A¹_k` is induced by the
inclusion `k[s] ⊂ R`" and then localizes at `s ≠ 0`. But `s ∉ R[ts]`:
elements of `R` are polynomials in `ts` with coefficients in `R`, and
`R[ts] ≅ R[τ]` is a polynomial ring in one variable. There is no inclusion
`k[s] ⊂ R`, no structure morphism to `A¹`, and no localization "at `s`".
Likewise `R/(s)` is meaningless as written; the displayed identity
`R/(s) = ⊕(t^m)/(t^{m+1})` is the deformation property of the **extended**
Rees algebra.

*Charitable repair (adopted for the rest of this section).* Take
`A := ⊕_{m∈Z}(t^m)s^m = R[ts, s⁻¹] ⊂ R[s,s⁻¹]` (with `(t^m) := R` for
`m ≤ 0`) and `w := s⁻¹ ∈ A`. Then `k[w] ⊂ A`, `A` is `k[w]`-flat,
`A/wA ≅ gr_v(R) ≅ κ(D)[T]`, and `A[w⁻¹] = R[s,s⁻¹]`. Everything Schenk
writes with `s` becomes correct with `w = 1/s`. Lemmas 7.1, 7.2, 7.4 then
go through as stated.

### 5.2 Lemma 7.5's special fibre is false — two independent errors

With `B := im(k[w][U,V] → A)`, `U ↦ P̃ = s^a u`(`ts`)`^a`, `V ↦ Q̃`:

1. **`B/wB` is not the image of `B` in `gr_v(R)`.** The natural map
   `B/wB ↠ im(B → A/wA)` has kernel `(B ∩ wA)/wB`, which is generally
   nonzero. This is the standard failure "initial forms of a subalgebra do
   not generate the associated graded of the subalgebra".
2. **The image is `k[F₀,G₀]`, not `κ(D)[F₀,G₀]`.** `B` is generated over
   `k[w]` by `P̃, Q̃`; nothing places the residue field `κ(D)` in the image.
   Chapter 8 nevertheless works exclusively with `κ(D)[F₀,G₀]` and with
   `κ(D)`-linear independence of `{T^n}`.

### 5.3 An explicit countermodel to Corollary 7.8

Take `F = id_{A²}`, a Keller map. Then `Γ_F` is the diagonal `≅ P²`, already
normal, `X = P²`, `X₀ = U = A²`, `f = id`, `P = x`, `Q = y`. Take
`D := {x = 5} ⊂ X₀`. Then `f(D) = D` is a curve, so **`D` is dicritical**
in Schenk's sense (Ch. 7 requires nothing more of `D`).

`R = k[x,y]_{(x−5)}`, `t = x−5`, `κ(D) = k(y)`. Since `5 ≠ 0`, `x` and `y`
are both units in `R`, so `a = v(P) = 0`, `b = v(Q) = 0`,
`u₀ = 5`, `v₀ = ȳ`, `F₀ = 5`, `G₀ = ȳ`. Hence

- `κ(D)[F₀,G₀] = κ(D)[5, ȳ] = κ(D)`, of Krull dimension **0**.

Corollary 7.8 asserts this is `≥ 1`. **False.** The same example separates
all three objects Lemma 7.5 identifies: with `B = k[w][x,y] ≅ k[w,x,y]`,

| object | value | dim |
|---|---|---|
| `B_η = B ⊗ k(w)` | `k(w)[x,y]` | **2** |
| `B/wB` | `k[x,y]` | **2** |
| `im(B → gr_v R)` | `k[ȳ] ⊂ κ(D)` | **1** |
| `κ(D)[F₀,G₀]` | `κ(D)` | **0** |

(`x = 5 + t` maps to `5` in `gr` because its degree-0 component reduces to
`x mod t = 5 ∈ κ(D)`.) The dimension-transport chain
`dim B_η ≥ 1 ⟹ dim B₀ ≥ 1 ⟹ dim κ(D)[F₀,G₀] ≥ 1` therefore fails at its
last link.

### 5.4 Lemma 7.7 and an internal inconsistency

Lemma 7.7 argues "`k(P,Q) ⊂ k(X₀)` and `trdeg_k k(X₀) = 2`, so necessarily
`trdeg_k k(P,Q) = 1`". This does not follow, and the true value is **2**:
`f` is dominant, so `P, Q` are algebraically independent over `k`. Hence
`dim B_η = 2` for **every** prime divisor `D`, dicritical or not.

Feeding the correct value into Lemma 7.6 gives `dim B₀ ≥ 2`. If Lemma 7.5
were true, `B₀ = κ(D)[F₀,G₀] ⊆ κ(D)[T,T⁻¹]` would have dimension `≤ 1`.
So the chapter's own lemmas are mutually inconsistent; the inconsistency
localizes exactly at Lemma 7.5, confirming §5.2.

### 5.5 Does the degeneration preserve the Keller condition?

No — and it never tries to. `det DF ∈ k×` is used nowhere in Chapters 6–9;
the degeneration retains only the quadruple `(a, b, u₀, v₀)`. Initial forms
do not commute with `d`, so no statement about `dP∧dQ` can be read off the
special fibre; consistently, Chapter 9 abandons `gr_v(R)` and computes in
`R` itself. The **only** output the rest of the paper takes from
Chapters 7–8 is the character relation of Theorem 8.3.

That relation needs no Rees theory at all. `κ(D)[F₀,G₀] ⊆ κ(D)[T,T⁻¹]` has
transcendence degree `≤ 1` over `κ(D)`, so its dimension is `1` iff
`(a,b) ≠ (0,0)` and `0` otherwise; when `a+b>0` the kernel `I` is a
height-one prime of the UFD `κ(D)[U,V]`, hence principal, and Theorem 8.3
follows in three lines. So the chapter advertised in §1.2 as "the only
genuinely deep algebraic step" is both erroneous and removable. What it
does **not** provide, and what Chapter 9 actually needs, is the descent
`c ∈ k×` — treated next.

## 6. The two-form step (Chapters 9–10) — vacuous, then false

### 6.1 Which case can occur?

**Proposition 6.1.** Let `D ⊂ X₀` be dicritical (`dim f(D) = 1`). Then
`a = v(P)` and `b = v(Q)` are `≥ 0` (Lemma 6.1) and **at most one of them
is positive**.

*Proof.* `a > 0` means `P` vanishes identically on `D`, i.e.
`C := f(D) ⊆ V(P)`, the target line `{first coordinate = 0}`; likewise
`b > 0` gives `C ⊆ V(Q)`. Both would force `C ⊆ V(P) ∩ V(Q) = {(0,0)}`,
contradicting `dim C = 1`. ∎

So **Case 1 of Chapter 9 (`a>0` and `b>0`) is empty for every dicritical
divisor.** Case 1 is the only case whose proof performs a genuine
computation — the `(a,b) = λ(m,n)` proportionality that makes the
`t^{a+b−1}` coefficient `b u₀du₀ − a v₀dv₀` vanish. It is never used.

### 6.2 Cases 2 and 3 have contradictory hypotheses

Take Case 2: `a > 0`, `b = 0` (Case 3 is symmetric). Then `C ⊆ V(P)` and,
`V(P)` being irreducible, `C = V(P)`. Along `D` the map is
`p ↦ (0, Q(p))`, so `dim C = 1` forces `Q|_D` **nonconstant**; since
`b = 0`, `v = Q` and `v₀ = \overline{Q} = Q|_D ∈ κ(D)` is nonconstant, i.e.
`v₀ ∉ k`.

Chapter 9 Case 2 requires the character relation with `c ∈ k×`; the weight
relation `ma + nb = ma = 0` forces `m = 0`, so the relation reduces to
`v₀ⁿ = c ∈ k×` with `n ≠ 0`. But then `v₀` is a root of `X^n − c ∈ k[X]`,
hence algebraic over `k`, hence `v₀ ∈ k` by the paper's own **Lemma 8.7**
(the algebraic closure of `k` in `κ(D)` is `k`). Contradiction.

**Corollary 6.2.** For every dicritical `D` with `a + b > 0`, the hypotheses
of Lemma 9.1 are unsatisfiable. Lemma 9.1 is therefore **true but vacuous**
in its intended application, and Chapter 10's appeal to it establishes
nothing.

**Corollary 6.3.** The hypothesis of Lemma 8.9 (existence of a nonzero
`H ∈ k[U,V]` with `H(F₀,G₀) = 0`) provably **fails** at such `D`: were it
satisfied, Corollary 8.10 would produce the very relation refuted above.
Chapter 10 never verifies it in any case; Remark 8.8 shows the author was
aware the descent is not free, and §10.4 then proceeds as if it were.

### 6.3 Lemma 10.2 is false

Lemma 10.2 claims: if `σ` is not étale and `D` lies over a branch component
`C`, then `a + b > 0`. By Proposition 6.1 this says `C` is one of the two
**target coordinate axes** `{P = 0}`, `{Q = 0}`.

**Proposition 6.4.** Lemma 10.2 is false.

*Proof.* Let `τ` be the translation `(X,Y) ↦ (X−α, Y−β)` of the target and
`F' := τ ∘ F = (P−α, Q−β)`, again a Keller map with `det DF' = det DF`.
`τ` extends to an automorphism `τ̄` of `P²` preserving the line at infinity,
so `id × τ̄` carries `Γ_F` to `Γ_{F'}`, hence `X ≅ X'`, `X₀ ≅ X'₀`,
`U ↔ U'`, `f' = τ∘f`, `σ' = τ∘σ`, and the branch locus of `σ'` is
`τ(branch locus of σ)`. The same divisor `D` lies over the branch component
`τ(C)` for `F'`.

`C ⊆ {P = α}` holds for at most one `α ∈ k` (two such values would give
`C = ∅`), and likewise for `β`. As `k` is infinite, choose `α, β` with
`C ⊄ {P=α}` and `C ⊄ {Q=β}`. Then `ord_D(P−α) = ord_D(Q−β) = 0`, i.e.
`a' = b' = 0` for `F'`, contradicting Lemma 10.2 applied to `F'`. ∎

Its proof fails for a locatable reason: from `a = b = 0` it deduces that
`η_D` maps into the target torus `G_m²`, then writes "Over `A²_{PQ}` the
morphism `f` agrees on the dense open chart `U ≅ A²` with `F` … Since `D`
dominates `C` and `η_D` lies over `A²_{PQ}`, the generic point of `D` lies
in this locus." Lying *over* the target torus is not lying *in* `U`. A
second leap follows: "`dP∧dQ` is nonzero in `Ω²_{Frac(R)/k}`, and its class
in `Ω²_{R/k} ⊗ κ(D)` is nonzero" — the first is automatic (`Ω²` of a
2-dimensional function field is 1-dimensional and `dP∧dQ = c·dx∧dy ≠ 0`)
and does not imply the second, which is precisely the statement
`ord_D(dP∧dQ) = 0` under dispute.

### 6.4 §10.4 and the polar part

The closing contradiction reads: `ord_D(dP∧dQ) > 0` from Chapter 9, versus
`ord_D(dP∧dQ) = 0` because "`D` dominates a curve in `A²`, hence meets the
affine chart `U`". As established in §0(V1) and §4, that implication is the
content of U-HIT and is not available.

On the brief's specific question — whether the positivity bookkeeping
accounts for the polar part of the Jacobian form at the boundary: **it never
reaches the boundary at all.** `dP∧dQ = (det DF)·dx∧dy` is an identity of
rational 2-forms in `Ω²_{k(X₀)/k}`, so
`ord_D(dP∧dQ) = ord_D(dx∧dy)` for **every** prime divisor `D ⊂ X₀`, with
value `0` exactly on divisors meeting `U`. The whole question is the value
of `ord_D(dx∧dy)` on `X₀ ∖ U`, where `x, y` are not coordinates. There
`ord_D` can be negative (on `Bl_p P²` at `p ∈ L_∞`,
`div(dx∧dy) = −3L̃_∞ − 2E`, so `ord_E = −2`), zero, or positive. Schenk
performs no such computation anywhere; he disposes of the boundary by
asserting `D ⊂ U`. There is no sign-convention error to repair, because
there is no boundary calculation.

### 6.5 What the correct value is, in our frame

Under the campaign's promoted Lemma 4.2 (`e = 1 + v(dx∧dy)`, i.e.
`v_l(dx∧dy) = μ_l − 1` at a dicritical `l`), the true value for an
affine-image dicritical is

  `ord_D(dP∧dQ) = ord_D(dx∧dy) = μ_D − 1`.

So `ord_D(dP∧dQ) = 0 ⟺ μ_D = 1`. Schenk's §10.4 therefore asserts, without
argument, that **every affine-image dicritical is unramified** — and his
Chapter 9 conclusion `ord_D(dP∧dQ) > 0` is simply the statement `μ_D ≥ 2`.
The two sides do not contradict each other; they are the two branches of
the `μ_D = 1` / `μ_D ≥ 2` dichotomy, and the paper contains no argument that
excludes either. Under H2 our Theorem 7.B says the `μ = 1` branch is the
impossible one for a noninvertible `F`, i.e. it is Schenk's `ord = 0` side
that fails, and his Chapter 9 side that is (for the wrong reasons) right.

## 7. The finite-étale / ZMT endgame (Chapters 11–12)

**Chapter 11 is correct.** Spreading out to a finitely generated `k₀ ⊂ k`,
embedding `k₀ ↪ C`, Riemann existence (SGA 1 XII), simple connectivity of
`C²`, and invariance of `π₁^{ét}` under extension of algebraically closed
fields (SGA 1 XIII 2.12) give `π₁^{ét}(A²_k) = 0`. Corollary 11.2 then
makes `σ` an isomorphism. This is standard and I found no defect.

**Chapter 12 is correct in substance, with one false lemma.** Lemma 12.2
("every regular function on a dense open `U ⊂ A²` extends; `O(U) = k[x,y]`")
is **false** — `U = A² ∖ {x=0}` has `O(U) = k[x,y][1/x]`. Normality gives
extension across codimension `≥ 2`, not codimension 1. Lemma 12.3 invokes
it, but Lemma 12.3's statement is true and standard: for a birational open
immersion `j : A^n ↪ A^n`, `O(j(A^n)) ≅ k[y₁,…,y_n]` because the image is
isomorphic to `A^n`, and a nonconstant polynomial cannot become a unit
there. Lemma 12.4 and §12.4 are the routine ZMT endgame. Nothing in
Chapters 11–12 rescues the earlier failures: what feeds them is
Theorem 10.3, which is unproved.

## 8. Cross-check against promoted campaign machinery

The reference frame was used as instructed — to locate where a sound proof
must work, not as a completeness assumption.

1. **The `Y = Spec B` construction.** Schenk's `Y₀ = Spec f_*O_{X₀}` is the
   normalization of the target `A²` in `k(X₀)`; this matches our frame and
   Lemmas 3.2–3.5 and 10.1 are sound. No conflict.
2. **`e = 1 + v(dx∧dy)`, Lemma 4.2.** This is the decisive comparison. It
   converts Schenk's `ord_D(dP∧dQ)` into `μ_D − 1`, exposing §10.4's
   `ord = 0` as the unstated hypothesis `μ_D = 1` (§6.5). A proof that
   silently assumes the dicritical is unramified cannot be a proof of JC2.
3. **Theorem 7.B (all-degree B0 under H2).** Our promoted statement is
   *no dicritical with affine image and `μ = 1`*, for noninvertible Keller
   maps of degree `N ≥ 3` with `A_F` irreducible. Schenk's Chapter 10, if
   sound, would exclude affine-image dicriticals **at every `μ` and with no
   H2 hypothesis** — strictly stronger than 7.B, and obtained in three
   pages from generic freeness. That gap in cost is itself diagnostic, and
   §§4–6 locate the reasons.
4. **Ramified dicriticals with `μ ≥ 2` exist in our analysis** (7.B kills
   only `μ = 1`; the weighted budget `Σμ_l ≤ N−2` and `2m ≤ N−2` presuppose
   `μ_l ≥ 2` contributions). Schenk's chain has nothing to say about them:
   for such `D`, Chapter 9's Cases 2–3 are exactly where the argument is
   vacuous (§6.2), and §10.4's `ord = 0` is exactly `μ_D = 1`.
5. **Reducible `A_F` at `N ≥ 5` survives our machinery.** Schenk's argument
   is insensitive to the irreducibility of the non-properness curve; it
   would kill those configurations too. Again consistent with the
   diagnosis that Chapter 10 proves nothing rather than something false
   about the geometry.
6. **Where the frame does *not* condemn him.** Chapters 2–4, 6, 8 (given
   its hypotheses), 10.1, 11, and the ZMT endgame are sound and match our
   picture. The failure is concentrated in Chapters 5, 7, 9-as-applied,
   and 10.2/10.4.

## 9. Verdict detail, repairability, and successors

**Verdict: FATALLY-FLAWED.** Not "repairable-gap". The two designated
load-bearing steps both fail, and each failure is at the point where the
Jacobian conjecture's actual difficulty lives:

- **Chapter 5** proves a statement equivalent to JC2 (Prop. 4.4) by
  choosing a point from a set proved empty (Prop. 4.1). There is no
  local repair: any correct proof of U-HIT is a proof of JC2.
- **Chapter 10** closes with a non sequitur that, decoded through our
  Lemma 4.2, is the hypothesis `μ_D = 1`. Supplying it is at least as hard
  as Theorem 7.B, which we proved only under H2 and only after the
  block-descent chain.
- **Chapter 9** is vacuous at every divisor Chapter 10 produces (Cor. 6.2),
  and **Lemma 10.2**, which supplies its numerical input, is outright false
  (Prop. 6.4).
- **Chapter 7** is erroneous (Lemma 7.5, Lemma 7.7, Cor. 7.8 with an
  explicit countermodel) and simultaneously removable — Theorem 8.3 needs
  none of it.

**Can our promoted machinery fill any of it?** No. Substituting our
Lemma 4.2 for §10.4 replaces the asserted `ord_D = 0` with `μ_D − 1`, which
removes the contradiction rather than supplying one. Substituting
Theorem 7.B for Chapter 10 would import H2, `A_F` irreducible, and `N ≥ 3`,
and would still leave `μ ≥ 2` and the reducible-`A_F` fronts open — i.e.
exactly the campaign's current frontier. Nothing here shortens it.

**Recommended dispositions.**
1. **No THREAT, no scoop.** The sweep's classification of F8 as a
   scoop-claim rather than a threat is correct, and the claim does not
   survive audit. JC2 stands open; Theorem 7.B is unaffected in either
   direction (Schenk neither implies nor contradicts it).
2. Record the `ord_D(dP∧dQ) = μ_D − 1` translation as a reusable audit
   probe: any purported JC2 proof that concludes by asserting
   `ord_D(dP∧dQ) = 0` at an affine-image dicritical is assuming `μ = 1`.
3. Record Proposition 4.1 (`f(X₀∖U) ∩ S°° = ∅` for any finiteness locus
   `S°°`) as a reusable killer of "generic-locus" boundary arguments: the
   boundary image is *always* disjoint from any locus where the affine part
   is finite, so no generic-freeness bookkeeping can see it.
4. Optional, low priority: a short courtesy note to the author covering
   V1–V4. Not initiated here; no outward-facing action was taken.

## 10. Execution log and disclosure

- Inputs verified by `shasum -a 256` before any reading; all three matched.
- Source read via `pdftotext -layout` and plain `pdftotext` (53 pp.,
  1 935 lines, 11 749 words), full text read; chapter/lemma index built by
  `grep`. Cross-mode reading guarded against the stacked-fraction
  extraction artefact; no claim above depends on a nested fraction.
- **No CAS was run and no computation of uncertain duration was
  performed.** All mathematics above is desk-scale and exact: the
  `F = id`, `D = {x=5}` countermodel (§5.3), Propositions 4.1, 4.4, 6.1,
  6.4, and Corollaries 6.2, 6.3 were verified by hand.
- **No additional literature was fetched.** The audit is self-contained:
  every external fact used (Stacks 01W6; SGA 1 XII/XIII; Zariski–Nagata
  purity; ZMT) is one Schenk himself cites, and Prop. 4.4 deliberately uses
  only the paper's own Chapters 11–12 toolkit so that no imported theorem
  is load-bearing. Jelonek's non-properness theorem is mentioned in §4.2 as
  context only and nothing depends on it.
- Campaign statements (Theorem 7.B, Lemma 4.2 / `e = 1 + v(dx∧dy)`, the
  `Σμ_l ≤ N−2` budget) are taken **as given** from the charged integration
  memo and the lane brief; they were not re-derived here, and §§4–6 do not
  depend on them. §6.5 and §8 do.
- Files written: `xmodel/schenk-audit-a-opus5-20260901.md` only. No
  canonical ledger, charged file, or `jc2-lean` was touched or inspected.
- Budget: well inside 6 h; no section was left OPEN.
- Worked alone; no consultation with the parallel lane.

<!-- BODY-END -->
