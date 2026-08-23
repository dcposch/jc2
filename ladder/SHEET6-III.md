# SHEET6-III — Case-III structural admissibility (St 3.16/3.18 extraction)

Status: COMPLETE + PROMOTED (2026-08-07, SHEET6-HIII-REVIEW.md: E5/N1
CONFIRMED with p.53 subscript-slip corroboration; the residual book is
SUPERSEDED by the composition, cases/hiii_compose.py).
Mission: SHEET6-CAMPAIGN.md §6 item 3. Extract
the case-III side conditions of Prop 9.3 (St 3.16/3.18 + the Puiseux jump
structure they encode) from refs/sigray_full.pdf, translate them into
Q-datum arithmetic, and run them as a filter (`tails3` stage) over the ~15
case-III parametric s-tails left open by the td=6 bash. NOT in scope: H3 /
IV-terminals (separate thread).

HEADLINE: two new structural conditions were extracted — **N1** (every ν ≥ 2
vertex has gcd(κ̄, ν) = 1; a theorem of Def 3.1 + Not 3.4/3.5) and the
**E5-corrected case-III update** (printed Prop 9.3 (g)/(h) are inconsistent
with the thesis's own definitions unless ν_F = ν_G; either coherent reading
gives λ_III ≥ ceil(μ(κ̄_G − ρ)/ν_G) = ceil(μρ) on every tail node). Result
(`tails3`, conditional on H1-H4 + AF2 + new H5a/H5b): **10 of the 13
sanctioned td=6 case-III s-tails die for ALL s** (9 by the λ-bound against
the St 9.4 budget, 1 more instance-set by N1); entries **r6 and r9 become
fully EXCLUDED mod H3+H5**, and the td≤5 G3-residues **row 5 and row 10/M2
close completely**. Across all 32 (shape,μ,occurrence) classes incl. AF3-
superset runs: 23 killed, 9 survive with explicit s-free residual children.
Bonus: N1 kills the td=6 row-3 ENTRY outright (ν=2, κ̄=10), independent of H3.

## 1. Extracted statements (verbatim, page-cited; all read on-page)

- **Def 3.1 (p.10)** (Puiseux characteristics): e0 := κ; β_i := min{j : c_j ≠ 0
  and e_{i−1} ∤ j}; e_i := gcd(e_{i−1}, β_i); ends at e_m = 1. α_j := β_j/κ;
  "For technical reasons, we use the notation α_0 = 0."
- **Def 3.4 (p.11)**: V_{1,a} := {I_P(u) : u = α_{j,P}}; V_{2,a} := {I_P(u) :
  u = O(P,P*)}; V_a := V_{1,a} ∪ V_{2,a} ∪ (0,x) ∪ (0,y).
- **Not 3.4 (p.12)**: "Set F ∈ V_a. Define ν_F ∈ N* … In the case F ∉ V_{1,a},
  then let ν_F := 1. Set F ∈ V_{1,a}. Then F = I_P(α_j) for some P ∈ R̄_a\R_a,
  where (κ, β_1, …, β_m) is the Puiseux characteristics of P, and α_j = β_j/κ.
  Set ν_F := e_{j−1}/e_j." [So ν_F ≥ 2 ⟺ F ∈ V_{1,a}: e_j properly divides
  e_{j−1} at a jump.]
- **Not 3.5 (p.12)**: "Set F ∈ V_a. Assume F = I_P(u) … characteristics of P is
  (κ, β_1, …, β_s). Set κ_F := κ/e_j, where α_j ≤ u < α_{j+1}."
- **Not 3.8 (p.12)**: F ∗ c := I_P((n+1)/κ) where n := κπ(F) and P is chosen
  with "The Puiseux series Ω(P) is in the form (3) or (4) with c_n = c."
  [Direction c ↔ the Puiseux COEFFICIENT of P at exponent π(F).]
- **St 3.16 (p.17)**: "Set F ∈ T_a \ {(0,x),(0,y)}. Then F ∈ V_{1,a} ∪ V_{2,a}
  if and only if p_F has more than one root. Set F ∈ V_a and let ν := ν_F. Then
  there exists a polynomial p̃ and l ∈ N such that p_F(η) = η^l p̃(η^ν)."
- **St 3.17 (p.18)**: F = G + c ⟹ (i) deg(p_F) = mult(p_G, c);
  (ii) d_F = d_G − (π(F) − π_G) deg(p_F).
- **St 3.18 (p.18)**: "Let F ∈ T_a, κ ∈ N* be suitable such that κπ(F) ∈ N.
  Then, if F ∗ c exists, then c is a root of p_F. If 0 is a root of p_F, then
  F ∗ 0 exists. If c ∈ C* is a root of p_F, then there exists a unique ν_F-th
  root of unity, ε such that F ∗ c exists." [Last clause: "F ∗ εc" evidently
  intended; cosmetic slip.]
- **Prop 9.3 (pp.50-51)**, step G = F + c (F = G° the new node), π(F) = u,
  π(G) = v = α_j = β_j/κ for some P: exactly one of
  (I) F ∈ V_{2,a}\V_{1,a}; (II) F ∈ V_{1,a}, u = α_{j−1};
  **(III) F ∈ V_{1,a} and u > α_{j−1}**; (IV) F = (0,y) ∉ V_{1,a} ∪ V_{2,a}.
  Case III, "Let ν := ν_F. Then there exists n ∈ N* such that
  (e) u = v − n/(νκ_G); (f) deg(p)/deg(q) = (νD_G + n deg(p_G))/(i(νκ_G(1−v)+n));
  (g) D_F = (νD_G + n deg(p_G))/ν_F; (h) κ_F(1−π(F)) = (ν(1−π(G))κ_G + n)/ν_F."
  Proof proves (a)-(d) only [via κ_F = κ_G/ν_G and St 3.17], then "The
  remaining Statements can be proved the same way as above."
- **Thesis usage of case III** (the only places it is ever engaged):
  9.6 proof (p.53) and 9.11 proof (p.60), μ = 2: "Consider the type (III) of
  Proposition 9.3. Then by Statements 3.16 and 8.2 one has p(η) = η²(η^ν −
  c_1^ν)…(η^ν − c_k^ν) and q(η) = η(η^ν − c_1^ν)…(η^ν − c_k^ν). In this case,
  by (v) of Proposition 8.1 one has M_F = 1." 9.7 proof (p.54), any μ: "In the
  case (III) of Proposition 9.3 there exists c* ∈ C* such that H := F + c*
  exists. By the regularity condition, H ∈ T_a%. Therefore λ_F ≥ 1." (9.8-9.10
  cite this "same way", p.55-57.) The (e)-(h) arithmetic is exercised NOWHERE
  in the thesis on a single number.

## 2. Structural analysis of case III (every inference justified)

Setting: step G = F + c, F = G° the new node, u = π(F) ∈ (α_{j−1}(P), α_j(P))
strictly (case III), v = π(G) = α_j(P). F ∈ V_{1,a} via a second root Q:
F = I_Q(α_{j'}(Q)), so O(P,Q) ≥ u (Def 3.3), and ν_F = e_{j'−1}(Q)/e_{j'}(Q) ≥ 2.

- **Common-grid identity**: P and Q share all coefficients at exponents < u,
  and β_1(P),…,β_{j−1}(P) < κ_P u, β_1(Q),…,β_{j'−1}(Q) < κ_Q u all lie in the
  shared support. Hence the lattice generated by the shared exponents is
  e_{j−1}(P)/κ_P-integral = e_{j'−1}(Q)/κ_Q-integral:
  **κ_com := κ_P/e_{j−1}(P) = κ_Q/e_{j'−1}(Q)** (Def 3.1 only).
- **(S1) c = 0 is forced** [Not 3.8 + Def 3.1 + St 3.18]: the direction from F
  to G is F ∗ c with c = c_n(P), n = κ_P u (Not 3.8: G lies on I_P above u).
  If c ≠ 0 then, since n < β_j(P) and β_j is the MINIMAL exponent with c ≠ 0
  off the e_{j−1}-grid, e_{j−1}(P) | n, i.e. κ_com·u ∈ Z. But u = α_{j'}(Q) is
  a jump of Q: κ_com·u = β_{j'}(Q)/e_{j'−1}(Q) ∉ Z (e_{j'−1} ∤ β_{j'} by Def
  3.1(i)); its exact denominator is ν_F (gcd(β_{j'}, e_{j'−1}) = e_{j'}).
  Contradiction ⟹ c_n(P) = 0 ⟹ **c = 0**, and 0 is a root of p_F (St 3.18,
  since F ∗ 0 = direction of G exists), with mult(p_F, 0) = deg(p_G)
  (St 3.17(i)); in Prop-8.1-reduced form mult(p, 0) = μ := deg(p_G)/i, μ | M_G
  (St 8.4). μ = 1 is impossible: regularity would leave p = η with one root,
  contradicting St 3.16 (F ∈ V_{1,a} ⟹ >1 root).
- **(S2) O(P,Q) = u and a second (nonzero) root is forced** [St 3.18]: if
  O(P,Q) > u then c_n(P) = c_{n'}(Q) ≠ 0 (jump coefficient of Q at u is ≠ 0 by
  Def 3.1(i)), contradicting (S1). So O(P,Q) = u: **F ∈ V_{1,a} ∩ V_{2,a}**,
  two roots separate exactly at F. Q realizes a direction F ∗ c* with
  c* = c_{n'}(Q) ≠ 0 ⟹ c* is a nonzero root of p_F (St 3.18) ⟹ k ≥ 1 in the
  pattern, and under regularity the branch H := F + c* ∈ T_a% gives the
  thesis's λ_F ≥ 1 (St 9.3/9.4). [This is the thesis's entire printed use.]
  Side effect: St 8.5 (M-divisibility, p.42) requires parent ∉ V_{2,a}, so it
  can NEVER be applied against case III — no extra kill from 8.5.
- **(S3) p-pattern** [St 3.16 part 2]: p_F(η) = η^l p̃(η^{ν_F}) with l =
  mult(p_F,0), nonzero roots in full ν_F-orbits, exactly one direction per
  orbit (St 3.18 unique-ε). Regularity (St 6.2): other existing directions have
  mult < μ; thesis pattern takes the k orbits simple:
  **p(η) = η^μ (η^ν − c_1^ν)…(η^ν − c_k^ν)**, deg p = μ + kν, ν := ν_F.
- **(S4) q-pattern** [Prop 8.1(iv)]: ord_0 of δpq′ − (1−u)p′q = p forces
  mult(q, 0) = 1 exactly (l_q ≥ 2 gives ord > μ, l_q = 0 gives ord μ−1 with
  non-cancelling coefficient), and the Galois structure gives q = η q̃(η^ν):
  **deg q ≡ 1 (mod ν_F)**. The thesis (p.53/60) additionally takes q's orbit
  set equal to p's (deg q = 1 + kν, cited to St 8.2); the engine inherits that
  (pre-existing, part of H1/AF surface — unchanged here).

(S1)-(S4) confirm the engine's III degree pattern (deg p, deg q) =
(μ + kν, 1 + kν), k ≥ 1, μ ≥ 2, and M_F = gcd(μ−1, 1+kν) (Prop 8.1(v)) —
in particular μ = 2 ⟹ M_F = 1 KILL, exactly the thesis's p.53/p.60 move.

## 3. The jump-grid arithmetic: N1 and the (g)/(h) discrepancy (E5)

**N1 (node admissibility).** Let G be any vertex with ν_G ≥ 2, i.e. G =
I_P(α_j) ∈ V_{1,a}. Then κ_G = κ/e_j (Not 3.5, index j since α_j ≤ v < α_{j+1}),
κ̄_G := κ_G(1−v) = (κ − β_j)/e_j ∈ Z, and since e_{j−1} | κ:
gcd(κ̄_G, ν_G) = gcd(κ − β_j, e_{j−1})/e_j = gcd(β_j, e_{j−1})/e_j = e_j/e_j:
**gcd(κ̄_G, ν_G) = 1 at every ν ≥ 2 vertex.** (Def 3.1 + Not 3.4/3.5 only;
case-agnostic. It refines the thesis's own possibility lists: e.g. 9.7(iv)'s
node (2/3, 3s+2, 3, 2s+2) has gcd(ν, κ̄) = gcd(s,2)·(unit) ⟹ only odd s are
realizable; similarly 9.9's node dies at s ≡ 0 (mod 3). Also kills the td=6
row-3 entry outright: ν = 2, κ̄ = 10.)

**Fine κ at the new vertex.** In case III, F carries TWO Not-3.5 values: via P
(u non-jump: κ_P/e_{j−1} = κ_com = κ_G/ν_G) and via Q (u a jump: κ_Q/e_{j'} =
ν_F κ_com). Only the Q-value makes κ̄_F ∈ Z (the P-value gives κ̄ with exact
denominator ν_F), and every integer κ̄ with ν ≥ 2 in the thesis's own Q-data
(9.6-9.11) uses the jump-realizing root. Adopted (flag H5a): κ_F = ν_F κ_G/ν_G.

**Corrected (g')/(h') [E5].** Repeating the thesis's own (c)/(d) proof line
(D_F = κ_F d_F, St 3.17(ii), (e): κ_G(v−u) = n/ν_F) with κ_F = ν_F κ_G/ν_G:
  (g') D_F = (ν_F D_G + n deg p_G)/ν_G   (h') κ̄_F = (ν_F κ̄_G + n)/ν_G.
The PRINTED (g)/(h) (denominator ν_F) equal (g')/(h') iff ν_F = ν_G
(equivalently κ_F = κ_G). As printed they are dimensionally inconsistent with
Not 3.4/3.5 + St 3.17 for ν_F ≠ ν_G — new erratum-class item **E5** (same
family as E1-E4; "proved the same way as above" with the ν-weights slipped).
Ratio (f) is reading-independent: deg p/deg q = D_F/(iκ̄_F) = μ(ν_F ρ + n)/
(ν_F κ̄_G + n), so the campaign's solved instances (s ≤ 5 kills) are unaffected;
only the CHILD data and the n-congruence change:
  printed: ν_F | n, κ̄_F = κ̄_G + n/ν_F     E5: n ≡ −ν_F κ̄_G (mod ν_G).

**The λ lower bound.** Solving (f) for n: n(μ−1)k = (μ+kν_F)κ̄_G − μ(1+kν_F)ρ.
Substituting into (h') and (g') gives closed forms
  κ̄_F = μ(1+kν_F)(κ̄_G − ρ)/(k(μ−1)ν_G),  D_F/i = μ(μ+kν_F)(κ̄_G − ρ)/(k(μ−1)ν_G),
  gap := D_F/i − κ̄_F = μ(κ̄_G − ρ)/(k ν_G)   [E5; printed has ν_F in place of ν_G].
With AF2 (λ ≥ k·max(1, ceil(gap))) this yields, INDEPENDENT of k and ν_F:
  **λ_III ≥ ceil(Λ), Λ := μ(κ̄_G − ρ)/ν_G.**
Under the printed reading with its forced ν_F = ν_G the SAME bound holds; the
bound fails only for the incoherent mixed reading (printed formulas + ν_F free),
which is what the pre-extraction engine conservatively ran.

**Lock structure of the tail nodes.** Every one of the ~15 open III-tail nodes
satisfies κ̄_G(s) = ρ(ν_G(s) + 1) identically (they are λ=0-family children;
verified exactly in `tails3`). Hence Λ = μρ, an s-FREE constant, and
  ρ_F = μρ/(k(μ−1)), κ̄_F = ρ_F(1+kν_F), D_F/i = ρ_F(μ+kν_F)
are s-free: the entire case-III step out of a tail node is pinned by (μ, k, ν_F)
up to the n ≥ 1 window. Kills: (K1) budget: ceil(μρ) > 4 − λ_spent;
(K2) N1@G: gcd(ν_G(s), κ̄_G(s)) > 1 (kills s-residues; periodic mod the
resultant |a_ν b_κ − a_κ b_ν|); (K3) no (k, ν_F) with κ̄_F ∈ N, M_F =
gcd(μ−1, 1+kν_F) ≥ 2 (Prop 8.4), gcd(κ̄_F, ν_F) = 1 (N1@F), λ ≤ budget.

## 4. Per-tail verdict table (`tails3` output, exact arithmetic)

Verdicts are conditional on the stack of §5 (H1-H4 + AF2 + H5a/H5b). B = 4 −
λ_spent (td≤5 rows: (td−2) − λ_spent). Λ = μρ on every (locked) tail. A shape is
dead only if it dies at its weakest-budget occurrence; per-occurrence below.

**Sanctioned td=6 layer (the campaign's §5 open list, 13 tails):**

| entry | tail (ρ,ν(s),M,κ̄(s)) | μ | B | Λ=μρ | verdict |
|---|---|---|---|---|---|
| r6/M3 | (2/3,3s+2,3,2s+2) | 3 | 1 | 2 | **KILLED-BY-3.18** (E5 budget: 2>1) |
| r6/M3 | (3,3s+2,3,9s+9) | 3 | 4 | 9 | **KILLED-BY-3.18** (9>4) |
| r8/M2 | (2/9,9s+8,3,2s+2) | 3 | 1 | 2/3 | SURVIVES-EXTRACTION (odd s only; residual k=1, ν_F≡5 (6), child (1/3,ν_F,2,(ν_F+1)/3), λ=1) |
| r8/M2 | (8/9,9s+8,3,8s+8) | 3 | 2 | 8/3 | **KILLED-BY-3.18** (3>2) |
| r9/M3 | (3/2,6s+5,3,9s+9) | 3 | 4 | 9/2 | **KILLED-BY-3.18** (5>4) |
| r11/M5 | (1/3,3s+2,3,s+1) | 3 | 2 | 1 | SURVIVES-EXTRACTION (residual k=1, ν_F odd, child (1/2,ν_F,2,(ν_F+1)/2), λ=1) |
| r11/M5 | (10/3,3s+2,3,10s+10) | 3 | 2 | 10 | **KILLED-BY-3.18** (10>2) |
| r11/M5 | (2/3,3s+2,3,2s+2) | 3 | 1 | 2 | **KILLED-BY-3.18** (2>1) |
| r11/M5 | (4/3,3s+2,3,4s+4) | 3 | 2 | 4 | **KILLED-BY-3.18** (4>2) |
| r11/M5 | (1/2,4s+3,4,2s+2) | 4 | 2 | 2 | SURVIVES-EXTRACTION (residual k=1, ν_F≡2 (3), child (2/3,ν_F,3,2(ν_F+1)/3), λ=2 exact) |
| r11/M5 | (5/2,4s+3,4,10s+10) | 4 | 3 | 10 | **KILLED-BY-3.18** (10>3) |
| r11/M5 | (2,5s+4,5,10s+10) | 5 | 4 | 10 | **KILLED-BY-3.18** (10>4) |
| r11/M5 | (2/5,5s+4,5,2s+2) | 5 | 1 | 2 | **KILLED-BY-3.18** (2>1) |

→ 10 of 13 sanctioned td=6 tails die; **r6 and r9 sanctioned entries are now
fully EXCLUDED mod (H1-H4 + H3 + H5)** — same status as r2/r3.

**td≤5 validation rows (G3 residue):**

| entry | tail | μ | B | Λ | verdict |
|---|---|---|---|---|---|
| r5 td4 M3 | (2,3s+2,3,6s+6) | 3 | 2 | 6 | **KILLED-BY-3.18** (6>2) → row 5 CLOSED mod stack |
| r10 td5 M2 | (4/3,3s+2,3,4s+4) | 3 | 1 | 4 | **KILLED-BY-3.18** (4>1) → r10/M2 CLOSED mod stack |
| r10 td5 M4 | (8/3,…8s+8), (2,4s+3,4,8s+8), (4/3,…4s+4) | 3,4,3 | 2,3,1 | 8,8,4 | **KILLED-BY-3.18** |
| r10 td5 M4 | (1/3,3s+2,3,s+1); (2/3,3s+2,3,2s+2) | 3 | 2 | 1; 2 | SURVIVE (latter odd s only, N1) |

**Superset (AF3-ext) occurrences**: 32 (shape,μ) pairs total across all
entries/budgets: **23 KILLED at every occurrence** (22 by the E5 λ-bound, 1 —
(4/3,6s+2,3,8s+4), ν and κ̄ both always even — by **N1 alone, all s**,
i.e. KILLED-BY-3.16/Def 3.1: the node violates gcd(κ̄,ν)=1 identically),
**9 survive** at ≥1 occurrence: (2/9,9s+8,3,2s+2)μ3, (1/3,3s+2,3,s+1)μ3,
(1/2,4s+3,4,2s+2)μ4, (2/3,3s+2,3,2s+2)μ3 [odd s], (2/5,5s+4,5,2s+2)μ5 [odd s],
(1/4,4s+3,4,s+1)μ4, (1/5,5s+4,5,s+1)μ5, (4/3,3s+2,3,4s+4)μ3 [odd s, B=4 r8-ext
only, λ=4 exact], (4/3,6s+5,6,8s+8)μ3 [B=4, λ=4 exact]. N1 additionally
restricts four of these to odd s only (kills the even half of each family).

Attribution note: "KILLED-BY-3.18" = the E5-corrected (g')/(h') λ-bound, whose
ingredients are the c=0/jump structure of §2 (St 3.18 + Not 3.8) and the fine-κ
convention (§3); "KILLED-BY-3.16" = the N1 gcd condition (Def 3.1 route; St
3.16 is the statement tying ν to the vertex's jump structure). No tail needed
the k≥1/μ≥3 conditions beyond what the engine already enforced.

## 5. Honesty section — interpretation steps and new hypotheses (§0c style)

- **H5a (Notation 3.5 convention at double-realized vertices)**: Not 3.5
  defines κ_F via "some P" with α_j ≤ u < α_{j+1}; at a case-III vertex F the
  value is P-dependent (κ_com via P, ν_F·κ_com via the jump root Q). Adopted:
  the Q-value (fine). Support: it is the only reading with κ̄_F ∈ Z (the
  P-value gives exact denominator ν_F ≥ 2, while every ν ≥ 2 entry in the
  thesis's own Q-data 9.6-9.11 has integer κ̄); it is the value the NEXT chain
  step needs (F is then the "G = I_Q(α_{j'})" of Prop 9.3); and N1 (a clean
  theorem under it) is consistent with all thesis-printed Q-data. Interpretive
  step nonetheless: flagged as a standing hypothesis.
- **H5b (= erratum E5, printed Prop 9.3 (g)/(h))**: as printed ((g)/(h)
  denominators ν_F) the case-III update is consistent with Not 3.4/3.5 + St
  3.17 iff ν_F = ν_G. Adopted: the corrected (g')/(h') (denominators ν_G),
  re-derived by the thesis's own (c)/(d) proof line. The printed-literal
  alternative (ν_F = ν_G forced) yields the SAME λ-bound Λ = μ(κ̄_G−ρ)/ν_G, so
  every KILL-BUDGET-E5 verdict holds under either coherent reading. What is
  NOT covered: the pre-extraction mixed reading (printed formulas, ν_F free ≠
  ν_G) — that is the engine's old conservative superset, which H5a/H5b assert
  is not a theorem of the thesis's own definitions. E5 was never exercised
  numerically in the thesis (case III is engaged only via M_F=1 at μ=2 and the
  λ≥1 shortcut), so no printed computation discriminates the readings.
- **AF2 dependence**: the λ-bound uses the campaign's reverse-engineered
  λ-rule (λ ≥ k·max(1, ceil(D_F/i − κ̄_F))). Only the WEAKER consequence
  λ ≥ ceil(gap) with gap summed over ALL extra roots is needed; still AF2-
  conditional (campaign §6.5 audit item). The k≥1 part (λ ≥ 1) is thesis-solid
  (p.54: forced second root + St 9.3/9.4).
- **Theorem-solid vs interpreted**: N1's gcd computation, the common-grid
  identity, c = 0 (S1), O(P,Q) = u (S2), q's mult(q,0)=1 (S4) are proofs from
  Def 3.1/Not 3.4/3.5/3.8/St 3.16/3.17/3.18/Prop 8.1 as printed — no
  interpretation beyond H5a's convention. The q-orbit-set = p-orbit-set (l=0
  in deg q = 1+kν) is inherited from the thesis's p.53/p.60 pattern (cited
  there to St 8.2, whose printed statement does not obviously imply it) — a
  pre-existing engine assumption (H1 surface), unchanged by this extraction
  and load-bearing only for the ratio equation, not for the kills.
- **Possibility-list semantics**: N1 refines the thesis's own lemmas (9.6(v)
  only s ≢ 1 mod 3; 9.7(iv)/9.10 node only odd s; 9.9's node only s ≢ 0 mod
  3; row-3 td=6 entry killed outright: ν=2, κ̄=10). Legitimate because St
  9.6-9.11 state possibility supersets; no thesis statement is contradicted.
- **Scope**: verdicts inherit the campaign's H1-H4/AF3 stack; IV-terminals
  (H3) untouched. Survivor children were NOT chased further (each SURVIVES row
  reports the explicit s-free child Q-datum, so §6.2's per-shape closure now
  has concrete, finite targets).

## 6. Reproduction

    cd cases && python3 sheet6_campaign.py tails3   # this doc's §4 (~4-6 min)
    python3 sheet6_campaign.py gate                 # must still PASS (verified)

`tails3` is purely additive (new functions + CLI branch; no existing stage
touched). Internal certificates: the κ̄=ρ(ν+1) lock is asserted per tail; N1
residue sets are sample-asserted out to 3× the resultant period; every
survivor witness is PIT-asserted against (f)+(h') at three s-values; the
budget kill is an exact linear-form positivity check over all s ≥ 0. Exact
int/Fraction arithmetic throughout; runtime dominated by re-running `bash`.
