# DOMRINA-GAP-REPAIR: the two named first-half gaps

**Lane:** repair-or-refute of the two `GAP-CANDIDATE` obligations left by the
charged replay of Domrina II, §§1–4.  **Headline:** both are **REPAIRED**.
Neither implication is false; no countermodel exists inside the replay's own
state space, and I exhibit the reason rather than merely failing to find one.
The repairs are desk proofs from Domrina's own §1–§2 apparatus (admissible
route (a)), plus one auxiliary lemma proved here from scratch which removes a
standing hypothesis from her Lemma 2.12.

## 0. Custody, scope, and verdict vocabulary

Custody was run before either charged input was read.  Recomputed digests:

```text
b838a2860c88d64d2a2162fd1a157e345db027bf4c7e95d2abae899dba9dc5de  inputs/domrina-ii-replay1-sol56-20260901.md
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc  inputs/block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
0be24c5c6a9cc9423c3049c3402f2c98e44bac5f1c6018b3999989e0f32e5018  refs/domrina2000_izv64_four_sheeted_general_case.pdf
88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad  refs/zoladek2008_official.pdf
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
7c3ba931d9cf2152a18c2a1b2c0f62c2cddec73e61927751813b449fe4b6d726  refs/orevkov1990_sb65_fundamental_group_complement.pdf
```

All six equal the charged values.  Two further files were opened and are
declared: `refs/do.pdf`, SHA-256
`6ca30d797810400ddfcddb5b92b046796b3fdda5c1fb8f0ba378511506bbfed3`, which is
Domrina–Orevkov, part I, i.e. reference `[4]` of the audited paper (its
bibliography, p. 33, names it), opened solely to recover the *notation and
numbered formulas* that Domrina II cites but does not restate; and
`refs/domrina2000_im273_russian.pdf`, the Russian original, opened solely to
adjudicate two ambiguous glyphs in the English typesetting.  Neither is used to
supply a mathematical step.  The three pinned literature files (Żołądek,
Sigray, Orevkov 1990) were hash-verified but **not needed**: route (c) was
never invoked, and I do not claim their support.  Route (b) — promoted campaign
machinery from the charged rowkill integration — was likewise **not needed**;
the S₄ row-kill theorem and the Eisenbud–Neumann/splice determinant apparatus
of the block-descent campaign are orthogonal to a root-position question inside
Domrina's own graph, and I decline to borrow authority I do not use.

Verdict vocabulary is fixed as charged: **REPAIRED** (a self-contained proof of
the missing implication is supplied here), **UNREPAIRED-LIKELY-TRUE**,
**IMPLICATION-FALSE**.

No exit-price assertion is made anywhere in this report, so the FALLACY-v2
`charge_basis` declaration is inapplicable.  Where I consume a promoted or
replayed statement I name it and its scope; where I prove something new I say
so and prove it.

## 1. Reconstructed apparatus

All page numbers are the printed English pages of the audited PDF, which agree
with its PDF page numbers.

### 1.1 Graph notation ([4], Notation (1.1))

For a tree Γ and distinct vertices a, b:

- `br_a(b)` — the connected component of Γ − a containing b (the *branch at a
  towards b*);
- `(ab) = br_a(b) ∩ br_b(a)` — the open interval: the interior path vertices
  **together with every subtree hanging off them**;
- `[ab) = (ab) ∪ {a}`, `[ab] = [ab) ∪ {b}`;
- `⟨ab⟩` — the minimal connected subgraph containing a and b, i.e. the closed
  path, **path vertices only**;
- `δ(ab) = [ab] − ⟨ab⟩` — exactly the subtrees hanging off the *interior*
  vertices of the path.

`det Q` always means `det(−A_Q)` for the intersection matrix, with
`det ∅ = 1`.  Every such determinant is a rational integer.

Cited results of [4], with their part-I internal numbers, so that no reader has
to trust my paraphrase:

- **[4], Lemma 2** = (1.4): if `det Γ = 1` the branch determinants at a common
  vertex are pairwise coprime.
- **[4], Lemma 3** = (1.6): for the root v and any s ≠ v, the determinants of
  all branches at s *other than* `br_s(v)` equal 1 with at most one exception;
  all branches at v have determinant 1.
- **[4], Lemma 4** = (1.7): `v ∉ Q ⟹ det Q > 0`.
- **[4], Lemma 5** = (1.19)–(1.21): the constant-degree determinant transfer.
- **[4], (2)** = (1.3), the edge formula
  `det(ab)·det Γ = det br_a(b)·det br_b(a) − det(Γ−[ab])·(det δ(ab))²`.
- **[4], (3)** = (1.9), the canonical-coefficient formula; **[4], (4)** =
  (1.12); **[4], (5)** = (1.13) Riemann–Hurwitz; **[4], (6)** = (1.18).

Consistency check on the sign convention: substituting Γ = L̃ into [4], (2) in
the second display of Domrina's Lemma 2.12 proof (p. 7) reproduces the printed
identity **only** with `det L̃ = −1`.  That is the same normalisation as
Proposition 1.3, 2)d) (`det L = −1`, p. 3) and confirms that part I's
`det Γ_L = 1` is an OCR-lost minus sign in `refs/do.pdf`, not a different
convention.  This matters: the whole argument below turns on signs.

### 1.2 The state space (replay §1, restated for root questions)

`L̃ = L̃∞ + g̃₁ + g̃₂` (Proposition 1.2, 2), p. 2), with `m(g̃₁) = n(g̃₁) = 1`,
`m(g̃₂) = 1`, `n(g̃₂) = 2`.  Each g̃ᵢ meets L̃∞ transversally at one point
(Proposition 1.3, 1)), so **g̃₁ and g̃₂ are leaves of the tree L̃**.  The root ṽ
of L̃ lies in L̃∞ (p. 3).  In the target, `U := U_h` is the branch of L carrying
the g₁-arrowhead, and `U⁰ := F⁻¹(U)`.  Proposition 1.3, 2)a) gives
`det U_a = 1`, `det R_a > 1` for a ∈ U, and `det R_a = 1`, `det D_a > 1`,
`det L_a > 1` for nodal a ∈ L − U, a ≠ h; 2)b),c) add `det R_h = 1` in
types 1 and 2, and in type 3 via Fig. 1b′ h *is* the root of L, so
`det R_h = 1` there by [4], Lemma 3.

Two glyph adjudications against the Russian original (p. 11 of that file):

1. Corollary 3.8 a) reads, in Russian, "смежным с одной вершиной **h̃ ∈ h′**",
   i.e. the unique attaching vertex of a U⁰-component is named as lying in h⁰.
   The English translation drops "h̃ ∈ h⁰".  I use the Russian, stronger form;
   it is also what Lemma 3.7 a) actually proves.
2. Corollary 3.8 b)'s second clause is printed, in both languages, as "all
   nodal vertices of **δ(g̃₁ṽ) ∩ Ũ** are inessential".  Definition 2.2 (p. 3)
   defines essential/inessential only for nodal `q̃ ∈ ⟨g̃₁ṽ⟩`, and vertices of
   `δ(g̃₁ṽ)` are by construction *off* that path.  The clause is therefore
   ill-typed as printed.  Lemma 3.15 states the parallel clause with the
   correct bracket, "every nodal vertex of **⟨ṽg̃₂⟩ ∩ Δ**".  Repair:
   `TYPO[COR-3.8b-delta-TO-angle]`; read `⟨g̃₁ṽ⟩ ∩ Ũ`.  Everything downstream
   (e.g. the uses at Russian pp. 21, 22 that read off `det δ(g̃₁h̃) = 1`) is
   consistent only with that reading.

## 2. A new unconditional lemma: `det L̃∞ ⩽ 0`

Domrina's Lemma 2.12 (p. 7) is the only root-*location* engine in §2 that
concludes something positive rather than deriving a contradiction, and it is
the engine both repairs below will run.  Its statement:

> **Lemma 2.12.** Suppose ã ∈ ⟨g̃₁g̃₂⟩.  Put Q₁ := br_ã(g̃₁), Q₂ := br_ã(g̃₂),
> and let Q₃ be the subgraph consisting of all connected components of
> δ(g̃₁g̃₂) incident to ã.  Suppose that `det L̃∞ ⩽ 0`, `det Q₃ > 0`, and
> `det(ãg̃ᵢ) ⩽ (det δ(ãg̃ᵢ))²·det Q₃` for some i = 1, 2.  Then ṽ ∈ Q₁ ∪ Q₂.

The charged replay types this **REPLAYED-SOUND** (its R-8), and I have
re-verified both displayed applications of [4], (2) line by line; in
particular `det br_{g̃₂}(ã)` inside `br_{g̃₁}(ã)` is `det(L̃ − g̃₁ − g̃₂) =
det L̃∞`, which is where the first hypothesis enters.

That first hypothesis is *stated, never proved* in the paper: it is discharged
case by case in §§5–7.  Both of my repairs need it at a point where no case
analysis is yet available, so I prove it once and for all.

> **Lemma DET-LINF.** `det L̃∞ ⩽ 0`, unconditionally.

*Proof.* Two steps.

**(i) X̃ − L̃∞ is affine.**  X̃ − L̃∞ = F⁻¹(X − L) = F⁻¹(C²).  F : X̃ → X is a
morphism of projective varieties, hence proper, so F⁻¹(C²) → C² is proper.  Its
fibres are finite: a positive-dimensional fibre would contain a complete curve
C ⊂ F⁻¹(C²); C ⊄ L̃ is impossible because X̃ − L̃ = C̃² is affine and contains no
complete curve, while C ⊆ L̃ with C ⊄ L̃∞ forces C ∈ {g̃₁, g̃₂}, on which F is
non-constant by Proposition 1.2, 1), so C is not contracted.  A proper
quasi-finite morphism is finite, and the total space of a finite morphism to an
affine variety is affine.

**(ii) Sign.**  Since X̃ − L̃ = C̃² ≅ C², Pic(X̃) is freely generated by the
components of L̃, so the intersection form on the span of the components of L̃∞
is the restriction of the intersection form of X̃, which by the Hodge index
theorem has signature (1, ρ−1).  Hence `A_{L̃∞}` has at most one positive
eigenvalue.  For a nondegenerate symmetric form with p positive eigenvalues,
`det(−A) = (−1)^p ∏|λᵢ|`.  So `det L̃∞ > 0` would force p = 0, i.e. `A_{L̃∞}`
negative definite.

Suppose it were.  L̃∞ = L̃ − g̃₁ − g̃₂ is connected (L̃ is a tree and the g̃ᵢ are
leaves) and consists of nonsingular rational curves (p. 2).  By Grauert's
criterion L̃∞ contracts analytically to a normal point on a normal compact
complex surface Z, with X̃ − L̃∞ ≅ Z − {finitely many points}.  Any regular
function on X̃ − L̃∞ descends to a holomorphic function on Z minus finitely
many points; by normality and the Riemann extension theorem it extends
holomorphically over those points, and Z compact connected forces it to be
constant.  So `O(X̃ − L̃∞) = C`, contradicting (i), since an affine variety of
dimension 2 has a coordinate ring of transcendence degree 2.  Hence
`det L̃∞ ⩽ 0`. ∎

Two remarks.  First, this is strictly stronger than anything the paper
establishes; it is reusable in §§5–7, where `det L̃∞ ⩽ 0` is currently
re-derived per case.  Second, it is a *floor*, not an attainment claim: I do
not assert `det L̃∞ < 0`, and Lemma 2.12 does not need strictness.

## 3. GAP-CANDIDATE[ROOT-U-LAST-CHAIN] — Corollary 3.8 b), p. 10

### 3.1 The exact obligation

Printed statement and proof, p. 10:

> **Corollary 3.8.** a) Every connected component Ũ ⊂ U⁰ is an "edge type"
> subgraph incident to one vertex [h̃ ∈ h⁰] of the graph L̃∞ + g̃₂.
> b) If Ũ is incident to g̃₁, then **ṽ ∉ δ(g̃₁h̃)**, and all nodal vertices of
> ⟨g̃₁ṽ⟩ ∩ Ũ are inessential for g̃₁.
>
> *Proof.* Assertion a) follows from Lemma 3.7 a).  Assertion b) follows from
> Lemmas 2.3, 2.4 and 3.7 b).

The replay's objection is exact and correct: Lemmas 2.3 and 2.4 each require,
at a *selected* vertex q̃, the two path determinants
`det(q̃g̃₁) = det δ(q̃g̃₁) = 1`, and Lemma 3.7 b) delivers neither; it delivers
a determinant for a whole lifted U-component and positivity only for one
exceptional branch.  Nothing on the page selects q̃ or verifies those two
numbers.

### 3.2 Structural facts I consume

From Lemma 3.7 (typed REPLAYED-SOUND by the charged replay) and its Fig. 6, at
a vertex c̃ ∈ c⁰ over a nodal c ∈ U:

- **(F1)** every connected component Λ of F⁻¹(U_c) has `det Λ = 1`;
- **(F2)** all branches of L̃∞ at c̃ except two lie in F⁻¹(U_c); of the two, one
  contains h⁰ and the other is linear with **positive** determinant.

I also use the elementary consequence of [4], (4) and (5) that a vertex of L̃∞
lying over a vertex of valency 2 in Γ_{L,g} is itself linear: if s has two
neighbouring directions, each carrying k₁, k₂ preimage points on s̃ with
`Σ m_{p_j}(s̃) = m(s̃) = m` in each direction, Riemann–Hurwitz gives
`2(m−1) = (m−k₁) + (m−k₂)`, so `k₁ = k₂ = 1` and ν(s̃) = 2.  Hence every
*nodal* vertex of L̃ inside Ũ lies over a vertex of U of valency ⩾ 3 in
Γ_{L,g}, i.e. is one of the c̃ ∈ c⁰ produced by Lemma 3.7 a)'s induction.  This
closes the only gap between "branch vertex of Ũ" and "vertex to which (F1),
(F2) apply".

### 3.3 The repair

> **Theorem R1.** Let Ũ ⊂ U⁰ be a connected component incident to g̃₁, attached
> to h̃ ∈ h⁰.  Then ṽ ∉ δ(g̃₁h̃).

*Proof.*  Suppose ṽ ∈ δ(g̃₁h̃).  By the definition of δ there is a unique
interior vertex q̃ of the path ⟨g̃₁h̃⟩ such that ṽ lies in a branch at q̃ off
that path; write `B := br_q̃(ṽ)`.  Being a branch point, q̃ is nodal, and by
§3.2 it is one of the c̃ ∈ c⁰; write q := F(q̃) ∈ U.  Note also that Ũ is
incident to exactly one vertex of L̃∞ + g̃₂ (Corollary 3.8 a)), namely h̃, so
every branch hanging off the interior of ⟨g̃₁h̃⟩ is contained in Ũ; in
particular B ⊂ Ũ.

Since g̃₂ lies beyond h̃, the path ⟨g̃₁g̃₂⟩ runs g̃₁ → Ũ → h̃ → … → g̃₂ and
therefore contains q̃.  Apply Lemma 2.12 at ã := q̃.  Then
`Q₁ = br_q̃(g̃₁)`, `Q₂ = br_q̃(g̃₂) = br_q̃(h̃)`, and Q₃ is precisely the union
of the remaining branches at q̃ — which is where B sits.  Four checks.

**(1) `det(q̃g̃₁) = 1`.**  Since g̃₁ is a leaf, `br_{g̃₁}(q̃) = L̃ − g̃₁`, so
`(q̃g̃₁) = br_q̃(g̃₁) − g̃₁`, a branch of L̃∞ at q̃.  It is not the branch
containing h⁰ (that is Q₂, a different branch, because q̃ separates g̃₁ from
h̃).  It is not the linear branch of (F2) either: that branch maps into R_q,
whereas `(q̃g̃₁)` contains the vertex t̃ carrying the g̃₁-arrowhead, and
F(t̃) is the top vertex of U, which lies in U_q, not in R_q.  (If g̃₁ is
attached to q̃ itself then `(q̃g̃₁) = ∅` and the determinant is 1 trivially.)
So by (F2) it is a connected component of F⁻¹(U_q), and by (F1) its
determinant is 1.

**(2) `det δ(q̃g̃₁) ⩾ 1`.**  `δ(q̃g̃₁) ⊆ (q̃g̃₁)`, which does not contain ṽ
(ṽ ∈ B, a different branch at q̃).  By [4], Lemma 4 its determinant is
positive, hence a positive integer.

**(3) `det Q₃ ⩾ 1`.**  Q₃ is the disjoint union of the branches at q̃ other
than Q₁, Q₂, so `det Q₃` is the product of their determinants.  Every such
branch except B avoids ṽ, hence has determinant ⩾ 1 by [4], Lemma 4.  For B
itself, (F2) leaves exactly two possibilities: B is a connected component of
F⁻¹(U_q), whence `det B = 1` by (F1); or B is the linear branch, whence
`det B > 0`.  Either way `det B ⩾ 1`, so `det Q₃ ⩾ 1 > 0`.

**(4) The inequality (2.13) with i = 1.**  By (1)–(3),
`det(q̃g̃₁) = 1 ⩽ (det δ(q̃g̃₁))²·det Q₃`, since the right-hand side is a
product of positive integers.

With Lemma DET-LINF supplying `det L̃∞ ⩽ 0`, Lemma 2.12 applies and yields
ṽ ∈ Q₁ ∪ Q₂.  But ṽ ∈ B ⊆ Q₃, and Q₁, Q₂, Q₃ are pairwise disjoint.
Contradiction. ∎

Three features of this proof deserve to be said plainly, because they are
exactly what the printed one-line citation lacked.  It **selects** q̃ (the
unique hanging vertex), it **computes** the two determinants that the printed
route needed, and it **routes around** Lemmas 2.3/2.4 altogether: the missing
implication is supplied by Lemma 2.12, which is in the same section, proved,
and independent.  In particular the residual that the replay flagged — that
Lemma 3.7 b) supplies positivity only for the branch not containing h⁰ — is
dissolved, not patched: (F1) supplies determinant **1** for the other
candidate branches, and both candidates are needed only as a floor
(`det B ⩾ 1`), never as an attainment.

### 3.4 The second clause, and what it yields downstream

> **Theorem R1′.** Every nodal vertex of ⟨g̃₁ṽ⟩ ∩ Ũ is inessential for g̃₁.

*Proof.*  Let s̃₁, s̃₂, … be those vertices in order from g̃₁; by §3.2 each is a
c̃ ∈ c⁰, and by the argument of (1) above `det(s̃_j g̃₁) = 1` for every j.  The
branches at s̃_j other than the two path branches are, by (F2), the remaining
components of F⁻¹(U_{s_j}) (determinant 1 by (F1)) together with the linear
branch R̃_{s̃_j}.  Induct on j.  For j = 1 there is no nodal vertex strictly
between g̃₁ and s̃₁, so `δ(s̃₁g̃₁) = ∅` and `det δ(s̃₁g̃₁) = 1`; Lemma 2.3
applies and s̃₁ is inessential for g̃₁, which says exactly that every branch at
s̃₁ off ⟨g̃₁ṽ⟩ has determinant 1 — in particular `det R̃_{s̃₁} = 1`.  For the
step, `δ(s̃_j g̃₁)` is the disjoint union of the off-path branches at
s̃₁,…,s̃_{j−1}, all of determinant 1 by the inductive hypothesis, so
`det δ(s̃_j g̃₁) = 1`, Lemma 2.3 applies again, and s̃_j is inessential. ∎

Combining R1 and R1′: if ṽ ∉ ⟨g̃₁h̃⟩ then every interior vertex of ⟨g̃₁h̃⟩ is
covered by R1′ and `det δ(g̃₁h̃) = 1`, which is the form actually consumed at
Russian pp. 21–22 (English §5, cases with ṽ ∈ (ãg̃₂) and ṽ ∈ (h̃ã)).  If
instead ṽ lies *on* ⟨g̃₁h̃⟩, R1′ covers only the segment ⟨g̃₁ṽ⟩; the vertices
between ṽ and h̃ are not covered, and `det δ(g̃₁h̃) = 1` is **not** claimed for
that configuration.  This scope restriction is real and I flag it: the paper's
own §5 uses of `det δ(g̃₁h̃) = 1` occur in branches where ṽ has already been
placed elsewhere, so it is not consumed out of scope there, but a future audit
of §§5–7 must check each use against this boundary rather than treating
`det δ(g̃₁h̃) = 1` as unconditional.

**Verdict: REPAIRED.**  Both printed conclusions are proved; the first
unconditionally, the second as stated (on ⟨g̃₁ṽ⟩), with the printed δ replaced
by ⟨ ⟩ per `TYPO[COR-3.8b-delta-TO-angle]`.

## 4. GAP-CANDIDATE[ROOT-DELTA-G2-APPLICATION] — Lemma 3.15, pp. 14–15

### 4.1 The exact obligation

> **Lemma 3.15.** Suppose that a ∈ L − U is nodal, ã ∈ a⁰, Δ is the branch of
> L̃∞ of degree 2 incident to ã such that F(Δ) = R_a, and Δ is incident to g̃₂
> and non-incident to g̃₁.  Then **ṽ ∉ δ(ãg̃₂)** and every nodal vertex of
> ⟨ṽg̃₂⟩ ∩ Δ is inessential.

The printed proof establishes a structure package and then says "Applying
Lemmas 3.7 b), 2.5 and 2.6, we get the result".  I take the structure package
as licensed — the replay disputed the *inference*, not these steps:

- **(S1)** `det δ(ãg̃₂) > 0`;
- **(S2)** every connected component of `δ(ãg̃₂) − U⁰` is linear;
- **(S3)** every nodal s̃ ∈ ⟨ãg̃₂⟩ that is not a fork has `det(s̃g̃₂) = 2`;
- **(S4)** the only possible fork of Δ is h̃ ∈ h⁰, and then the determinants of
  the U⁰-components incident to h̃ are all 1.

(S3) is also independently reconstructible: a non-fork s̃ has m(s̃) = 1, so by
Proposition 3.4 c) any linear chain at s̃ has degree n(s̃); the chain towards
g̃₂ has degree 2 by Lemma 1.5, so n(s̃) = 2; Definition 3.2 b) then gives
`det(s̃g̃₂) = (n(s̃)·n(g̃₂)/Deg)·det R_s = (2·2/2)·1 = 2`, using
`det R_s = 1` from Proposition 1.3, 2)a) (and 2)b),c) if s = h).

The replay's three objections were: `det δ(s̃g̃₂) = 1` is never established for
the selected s̃; the corrected g₂-essential hypothesis of Lemma 2.6 is never
checked; and the negative branch determinant of Lemma 2.6 is never confronted
with positivity.  All three are answered below.

### 4.2 The repair

> **Theorem R2.** Under the hypotheses of Lemma 3.15, ṽ ∉ δ(ãg̃₂).

*Proof.*  Suppose ṽ ∈ δ(ãg̃₂).  Let q̃ be the interior vertex of ⟨ãg̃₂⟩ off
which ṽ hangs and `B := br_q̃(ṽ)`, a connected component of δ(ãg̃₂).  Since
g̃₁ ∉ Δ while g̃₂ ∈ Δ and Δ is a branch at ã, the path ⟨g̃₁g̃₂⟩ contains ã and
then all of ⟨ãg̃₂⟩; in particular **q̃ ∈ ⟨g̃₁g̃₂⟩**, so Lemma 2.12 is available
at ã := q̃, with Q₃ ∋ B.  By (S1) and [4], Lemma 4 every component of δ(ãg̃₂)
other than B has positive determinant, so `det B > 0` too, and as in §3.3(3)
`det Q₃ ⩾ 1`.  `det L̃∞ ⩽ 0` holds by Lemma DET-LINF.  By (S2) and (S4), B is
either linear or a U⁰-component, and in the latter case q̃ = h̃ is the unique
fork of Δ.

**Case A: q̃ is not a fork** (so B is linear by (S2)).  Then `det(q̃g̃₂) = 2` by
(S3).  Split on `det δ(q̃g̃₂)`, a positive integer (it avoids ṽ, [4], Lemma 4).

*A1: `det δ(q̃g̃₂) ⩾ 2`.*  Then
`(det δ(q̃g̃₂))²·det Q₃ ⩾ 4 > 2 = det(q̃g̃₂)`, so (2.13) holds with i = 2 and
Lemma 2.12 gives ṽ ∈ Q₁ ∪ Q₂, contradicting ṽ ∈ B ⊆ Q₃.

*A2: `det δ(q̃g̃₂) = 1`.*  Now Lemma 2.5's hypotheses hold verbatim at q̃
(`det(q̃g̃₂) = 2`, `det δ(q̃g̃₂) = 1`, and q̃ ∈ ⟨g̃₂ṽ⟩ because ṽ hangs off q̃),
so **q̃ is inessential for g̃₂**.  Since B is linear and `(ṽq̃) ⊆ B`, the
subgraph (ṽq̃) is linear, so ⟨q̃ṽ⟩ has no nodal vertex other than q̃ and ṽ; ṽ
is never essential (Definition 2.2 attaches no δ-component to a path endpoint)
and q̃ is inessential for g̃₂ by the previous sentence.  Hence the extra
hypothesis of Lemma 2.6 holds, **in its corrected g₂-form**
(`REPAIRED[LEMMA-2.6-g1-TO-g2]`, consumed from the charged replay's R-4).
Lemma 2.6 gives `det br_q̃(ṽ) < 0`, i.e. `det B < 0`, contradicting
`det B > 0`.

**Case B: q̃ = h̃ is the fork of Δ, B a U⁰-component.**  By (S4),
`det B = 1`.  Compute `det(h̃g̃₂)`.  Since h̃ is the only fork of Δ, the chain
from h̃ to g̃₂ has constant degree, equal to 2 by Lemma 1.5; hence by
Definition 3.2 b), `det(h̃g̃₂) = (n(h̃)·n(g̃₂)/2)·det R_h = n(h̃)`, using
`det R_h = 1`.  Also `Deg(h̃g̃₂) = m_p(h̃)·n(h̃) = 2` by [4], (1.16).

*B1: n(h̃) = 1.*  Then `det(h̃g̃₂) = 1 ⩽ (det δ(h̃g̃₂))²·det Q₃`, since both
factors are ⩾ 1 (the first avoids ṽ; the second by the paragraph above).
Lemma 2.12 applies and contradicts ṽ ∈ Q₃ exactly as in Case A1.

*B2: n(h̃) = 2.*  This case is **empty**.  Indeed then `m_p(h̃) = 1` on the
g̃₂-side, and the chain from ã to h̃ is fork-free of constant degree 2, so the
left edge at h̃ also has degree `m_{p′}(h̃)·n(h̃) = 2`, i.e. `m_{p′}(h̃) = 1`.
By [4], (4) the multiplicities over each of the two horizontal directions sum
to m(h̃), so each of those two directions carries at least two preimage points.
Riemann–Hurwitz [4], (5) at h̃ reads
`2(m(h̃) − 1) = Σ_{all p_j}(m_{p_j}(h̃) − 1) = ν(h)·m(h̃) − Σ_i k_i`, where the
sum runs over the ν(h) directions at h in Γ_{L,g} and k_i is the number of
preimage points in direction i.  With n(h̃) = 2, Deg(h̃) = 2m(h̃) ⩾ 4, so (3.1)
forces `Deg(h̃) = 4`, `m(h̃) = 2`, and `h⁰ = {h̃}`.  If ν(h) = 3 the identity
gives `Σ k_i = 4`, impossible since the two horizontal directions already
contribute k ⩾ 2 each and the up-direction contributes k ⩾ 1.  If ν(h) = 4
(Fig. 1a) it gives `Σ k_i = 6`, so with k_left = k_right = 2 we get
k_up = k_down = 1: **h̃ carries exactly one U⁰-component**, namely B.  But g̃₁
is incident to some U⁰-component, which by Corollary 3.8 a) attaches at a
vertex of h⁰ = {h̃}; so g̃₁ is incident to B ⊆ Δ, contradicting the hypothesis
that Δ is non-incident to g̃₁.  Hence B2 does not occur. ∎

> **Theorem R2′.** Every nodal, non-fork vertex of ⟨ṽg̃₂⟩ ∩ Δ is inessential.

*Proof.*  Identical induction to R1′, run from g̃₂ inwards with Lemma 2.5 in
place of Lemma 2.3, using `det(s̃g̃₂) = 2` from (S3) as the base numerical
input and building `det δ(s̃_j g̃₂) = 1` from the inessentiality of
s̃₁,…,s̃_{j−1}. ∎

**Scope note on R2′.**  At the fork h̃ (Case B1, n(h̃) = 1) one has
`det(h̃g̃₂) = 1`, not 2, so Lemma 2.5 does **not** apply there and h̃'s
inessentiality is not delivered by this argument.  This is not a gap I can
paper over by analogy: running Lemma 2.3's computation with `det(q̃g̃₂) = 1`
and `k_{g̃₂} = 1` yields `p₁ = d(Σ − 1) − 1`, which is ≡ −1 mod d and therefore
raises **no** contradiction with [4], Lemma 2.  The inessentiality clause of
Lemma 3.15 is therefore established here for the non-fork vertices of
⟨ṽg̃₂⟩ ∩ Δ and left **typed OPEN at the fork vertex h̃**:
`OPEN[LEMMA-3.15-INESSENTIAL-AT-FORK]`.  The charged obligation was the first
conclusion ("The exact first conclusion is: 'Then ṽ ∉ δ(ãg̃₂)'"), which is
fully repaired; I record the fork residual of the *second* clause rather than
claim more than I proved.

**Verdict: REPAIRED** for the charged obligation (ṽ ∉ δ(ãg̃₂)), with the
companion inessentiality clause repaired at every non-fork vertex and a named
`OPEN` at the fork.

## 5. Countermodel analysis: why neither implication is false

Item (2) of the charge asks, if a repair fails, for a countermodel to the
*implication*.  Both repairs succeeded, but the countermodel space is worth
recording because it explains why the printed one-line proofs were not merely
terse but genuinely under-determined, and because a reader is entitled to know
that "no countermodel" here is a theorem, not a failed search.

The state space is: a weighted tree L̃ = L̃∞ + g̃₁ + g̃₂ with `det L̃ = −1`, a
distinguished root ṽ ∈ L̃∞, leaf dicriticals g̃₁, g̃₂ with (m,n) = (1,1), (1,2),
a degree function Deg with `Σ_{ã ∈ a⁰} Deg(ã) = 4`, and the target graph L with
Proposition 1.3's determinant pattern.  A countermodel to Corollary 3.8 b)
would be such a configuration with ṽ inside a branch hanging off the interior
of ⟨g̃₁h̃⟩.  Theorem R1 shows the space contains none, and it is instructive
that the obstruction is *not* local: the two branch types available at q̃ by
(F1)/(F2) both have positive determinant, so no local sign argument can kill
the configuration, and indeed the naive route through Lemmas 2.3/2.4 stalls at
exactly that point, because Lemma 2.4's conclusion `det br_q̃(ṽ) < 0` needs an
extra hypothesis over the segment ⟨q̃ṽ⟩ which is unavailable when
`br_q̃(ṽ)` is a lifted U-component (that component may be a nonlinear tree).
What kills the configuration is *global*: the sign of `det L̃∞`, which is a
statement about the affineness of X̃ − L̃∞ and not about the graph at all.
Hence: the implication is true, the printed proof was insufficient, and the
missing ingredient was a global one that no amount of local determinant
bookkeeping would have produced.

The same remark applies to Lemma 3.15, with the extra wrinkle that its
genuinely awkward configuration (the root inside a lifted U-component at the
fork of Δ) is eliminated not by a determinant inequality at all but by a
counting argument — Riemann–Hurwitz plus (3.1) plus the hypothesis that Δ
misses g̃₁ — which forces h⁰ to be a singleton and then contradicts that same
hypothesis.  A countermodel would have to violate one of (3.1), [4], (4)/(5),
or the non-incidence hypothesis; none is negotiable.

I record one honest limitation on all of this.  My repairs consume the
structure packages (F1), (F2), (S1)–(S4) as *licensed inputs* — (F1)/(F2) from
Lemma 3.7, typed REPLAYED-SOUND by the charged replay, and (S1)–(S4) from the
undisputed portion of Lemma 3.15's own proof.  I re-derived (S3) but not
(S1), (S2), (S4).  If a later audit overturns any of those, the corresponding
repair must be rerun, not assumed.

## 6. Corrections and typings produced by this lane

| tag | content |
|---|---|
| `LEMMA[DET-LINF-NONPOS]` | `det L̃∞ ⩽ 0` unconditionally; removes the first hypothesis of Lemma 2.12 everywhere, including its §§5–7 uses |
| `TYPO[COR-3.8b-delta-TO-angle]` | Corollary 3.8 b) second clause must read ⟨g̃₁ṽ⟩ ∩ Ũ; as printed (δ) it is ill-typed against Definition 2.2 |
| `TRANSLATION[COR-3.8a-h0]` | the English drops "h̃ ∈ h⁰" present in the Russian; the attaching vertex is in h⁰, and the repair uses that |
| `SIGN[DO-I-DET-MINUS-ONE]` | part I's `det Γ_L = 1` is an OCR-lost minus sign; `det L̃ = det L = −1`, confirmed by re-deriving both displays of Lemma 2.12's proof |
| `OPEN[LEMMA-3.15-INESSENTIAL-AT-FORK]` | the inessentiality clause of Lemma 3.15 at the fork h̃, where `det(h̃g̃₂) = 1` and Lemma 2.5 is inapplicable; the Lemma 2.3-style computation provably raises no contradiction there |
| `SCOPE[COR-3.8b-ON-PATH-ROOT]` | `det δ(g̃₁h̃) = 1` follows from R1+R1′ only when ṽ ∉ ⟨g̃₁h̃⟩; §§5–7 uses must be checked against this boundary |

## 7. Consequence paragraph for the campaign soundness ledger

**Effect on DOMRINA-II-SOUNDNESS.**  The charged replay withheld promotion of
DOMRINA-II-SOUNDNESS on exactly two grounds, both root-location gaps in the
first half.  Both are now repaired: Corollary 3.8 b) in full, and Lemma 3.15
in the conclusion that was charged, with a named and characterised residual in
its companion inessentiality clause at a single fork vertex.  The correct
ledger move is therefore narrow and should be stated narrowly:
`DOMRINA-II-FIRST-HALF-ROOT-LEDGER = CLOSED`, and, combining with the replay's
already-typed `LEMMA 3.12 = REPAIRED`, `LEMMA 3.13 = REPAIRED`,
`LEMMA 3.14 = REPAIRED`, the disposition
`DOMRINA-II §§1–4 = SOUND-AFTER-REPAIRS` may be promoted, subject to the three
carried dependencies named below.  `DOMRINA-II-SOUNDNESS` as a whole
**remains unpromoted**, and the reason has changed rather than disappeared:
the blocker is no longer "two named gaps in the first half" but (i) §§5–7 are
unaudited — including the forward consumers of Lemma 3.15, Lemma 7.10 and the
omitted §7 arithmetic; (ii) the Domrina–Orevkov I inheritance is only
partially bound, since campaign Proposition 4.1 replaces part I's defective
unique-μ=1 inference and nothing else, so the "number of dicritical components
is greater than 1" entry to Proposition 1.2 still rides part I's separate
unique-μ=2 analysis, which no lane has re-audited; and (iii) the three
structure packages (F1)/(F2) and (S1)/(S2)/(S4) are consumed, not re-derived.
Anyone quoting this report should quote all three.

**Effect on the N=4-LITERATURE-CLOSED reception line.**  Unchanged, and this
matters more than the headline.  Repairing two first-half gaps does not make
Domrina II a checked proof of the N=4 case; it makes the first half checked
and the second half untouched.  `N=4-LITERATURE-CLOSED` therefore stays
**NOT ASSERTED**.  What has changed is the shape of the residual risk: before
this lane, a reader could reasonably have suspected that the paper's root
ledger was structurally defective, in which case the whole route would have
been in question; that suspicion is now retired, and the residual risk is
localised in §§5–7 and in the part-I μ=2 inheritance.  The campaign's
independent N=4 chain — the S₄ row-kill theorem, the six (8,6)/(9,6)
AM-numerical types under exact msolve decision, and the ROW-NF exhaustiveness
dependency that the closure review keeps labelled PROVISIONAL — remains the
load-bearing path to B0 at N=4, exactly as before.  Nothing here strengthens
or weakens it; the two efforts are independent, and it would be a mistake to
let a repaired Domrina lemma relax the exhaustiveness obligation on the
campaign side.  Conversely, had either implication turned out false, the
campaign chain would have become the *only* live path; it did not, and I
record that soberly: the honest summary is that a literature route which was
in doubt is now, in its first half, in better shape than the campaign had
assumed, and in its second half exactly as unknown as before.

**One reusable asset.**  Lemma DET-LINF (`det L̃∞ ⩽ 0`) is proved here
unconditionally from properness plus Hodge index plus Grauert contraction, and
is stronger than anything in the paper.  It discharges a hypothesis that
Domrina re-verifies case by case in §§5–7, so it is worth banking on its own
account for the sibling lane auditing those sections.

## 8. Disposition

```text
GAP-CANDIDATE[ROOT-U-LAST-CHAIN]        = REPAIRED  (Theorem R1, Theorem R1')
GAP-CANDIDATE[ROOT-DELTA-G2-APPLICATION]= REPAIRED  (Theorem R2; R2' non-fork)
COUNTERMODEL-TO-EITHER-IMPLICATION      = NONE-EXISTS (proved, not searched)
NEW-LEMMA[DET-LINF-NONPOS]              = PROVED, UNCONDITIONAL
RESIDUALS                               = OPEN[LEMMA-3.15-INESSENTIAL-AT-FORK],
                                          SCOPE[COR-3.8b-ON-PATH-ROOT]
DOMRINA-II §§1-4                        = SOUND-AFTER-REPAIRS (3 dependencies)
DOMRINA-II-SOUNDNESS                    = STILL UNPROMOTED (SS5-7 unaudited)
N=4-LITERATURE-CLOSED                   = NOT ASSERTED (unchanged)
```
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `32825`.
- Body SHA-256:
  `29a2bf6aa10402cb9fa2fa9c28b58729fa8dcb052ba13d03cf3d26f2994fe032`.
- Frozen basis: `21cf7ed1fb00b23def6c1546511bfdfeee4ca362`.
