**VERDICT: SOUND-WITH-ERRATA — the synchronized direct (9,15,7,3)@μ0=2 td-7 route family is dead at the tower tier; a per-pole-branching reading of Prop 4.2 does not dissolve the clash; the written 15-stack two-case exhaustion is incomplete (non-killing intermediate levels are legal in print) but the missing case dies by the same exponent/integrality squeeze; the “trunk is untouched” scope sentence is too strong (the clash lives on the pole-to-merge subtree, which the trunk completion shares).**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-13.
Target: `TOWER-9-15.md` + `cases/towers/t9_15_direct.json` + `cases/tower_check.py`.
Kill under review: the decorated spine of the design §3.2 synchronized direct completion admits no global Prop 4.2 ladder, because level 1 is claimed by both the (H8)-forced chain-1 pole-adjacent vertex X (gap (ν_X+1)/(2ν_X) > 1/2, ν_X | 11305 odd) and F1 (gap 2/5, i_F1=2 capping k_1 | 2) with incompatible death data; 15-stack two-case exhaustion all refuted.
Attacks, in the order requested: (1) global-single-ladder reading of Prop 4.2 vs a per-pole-branching tower; (2) aliveness trichotomy at non-killed levels; (3) death equation g_m = κ̄/D_f; (4) replay of the 15-stack exhaustion, including the checker’s obstruction block and negative controls; (5) kill scope vs the promoted §11a book and the trunk completion; (6) the §6 parity kill lemma and its claimed reach.
Method: `pdftotext -layout` of `refs/sigray_full.pdf` pp. 19–22 (Prop 4.2, Not 4.1–4.2, Prop 4.4–4.5), p. 32 (Cor 6.1), pp. 39–41 (Not 8.1, Prop 8.1, St 8.3); line-read of `SHEET6-TEMPLATE.md` §1, `SHEET6-R6.md:10` and §4.0, `SHEET6-LT-REVIEW.md:139-147`, `BOOK-OFFAXIS.md` R1.2 / P3 / §11a, `xmodel/sol-gluing-design.md` §3.2 and the §3.5 literal block, `xmodel/sol-sixcells.md` completions; `python3 cases/tower_check.py` (exit 0); independent exact `Fraction` replay of every death gap, all 15 Case A/B rows, T_a^& membership, the three Case C level-1 candidates, and the delayed-death integrality obstruction. No other repo file modified. No git.

---

## Findings (worst first)

### 1. Severity: erratum — the written Case A/B dichotomy is not exhaustive; a non-killing level 1 is printed-legal and delta-integral. The missing case still dies. The kill stands.

- File: `TOWER-9-15.md:221-244`; `cases/tower_check.py:469-521`; certificate `tower.obstruction`
- Claim: “ladder level 1 belongs either to X or (impossibly) to F1”; both cases refuted for all 15 stacks; “no global ladder exists.”
- How checked.

  **The slide.** Doc §3: “Since δ_j(v) = D_{f,v} g_j − κ̄_v must be strictly decreasing in j at every vertex (in particular at G, which sees all levels), the levels are globally sorted by gap, descending.” Decreasing δ_j(G) sorts the *ladder gaps* g_j. It does not force every g_j to equal some vertex’s death gap κ̄/D_f. Prop 4.2 produces (k_j, l_j) at vertices where J(f^+, h_j^+)=0 (alive), uniquely, from the leftover after the previous cancellation — not from a requirement that someone die at every index.

  The campaign’s own template work forbids the slide. `SHEET6-R6.md` is precisely the study of (k_1,l_1) *other than* the G_m-death pair (3,4), under the hypothesis m_{G_m}=2: level 1 does not kill G_m. `SHEET6-R6.md:10` and §4.3 treat (1,2) as printed-legal (k_j ∈ ℕ^*, no k=1 exclusion). A formalization calibrated on that genome cannot turn around and assume every ladder step is a vertex death.

  **Case C exists as a level-1 arithmetic possibility.** While both X and F1 are alive, Prop 4.2(iii) plus F1’s pattern p_f = S[(t−A)^2(t−B)(t−D)]^2 (certified T1 row; disc R1 = −3A^2 ≠ 0) forces k_j | 2. Independently, Prop 8.1’s printed line (p. 40) “i ℓ_j/k_j ∈ ℕ” at i_{F1}=2 with gcd(k,ℓ)=1 is the same cap. The pairs with gcd=1, k∈{1,2}, and gap(X) < g_1 < g_0=5/2 are exactly

  | (k_1,ℓ_1) | g_1 | δ_1 at F1, F2, F3, H2, G, N |
  |---|---|---|
  | (1,2) | 3/2 | 11, 250, 4842, 33911, 101740, 45218 |
  | (2,3) | 1 | 6, 165, 3227, 22606, 67825, 22608 |
  | (2,5) | 2 | 16, 335, 6457, 45216, 135655, 67828 |

  All six δ_1 values are positive integers for each of the three pairs (independent `Fraction` replay). The checker never enumerates these rows. Injecting any of them as a “surviving stack” would not trip C3.

  **The missing case still dies.** A non-killing prefix cannot continue forever (δ_j ∈ ℕ strictly decreasing). The next death after the poles cannot be F1: g = 2/5 < gap(X) makes δ(X) < 0. No vertex has a death gap in (gap(X), 5/2). Intermediate chain-1 vertices Y (rootward of X) have *smaller* gaps than X: for a clean n=1 stack, gap(Y) = (ν_Y+1)/(2 ν_X ν_Y) < gap(X) (checked on a lattice of (ν_X, ν_Y) dividing 11305). So the first subsequent death is X, at some m ≥ 1, with F1 still alive.

  While both are alive every prior step has k_j ∈ {1,2}. Starting from α_1 = 3/2, a k=1 step adds 0 to α and a k=2 step adds ℓ/2 with ℓ odd, hence α_m = 3/2 + r/2 + ℤ after r prior k=2 steps. X-death then demands

  ```
  ℓ_m / k_m  =  gap(X) + α_m − 1  =  α_m − 1/2 + 1/(2ν_X),
  ```

  and F1-alive demands k_m | 2.

  - k_m = 1 ⇒ ℓ_m = 1 + r/2 + ℤ + 1/(2ν_X) ∉ ℤ (ν_X ≥ 5).
  - k_m = 2 ⇒ ℓ_m = 2 + r + 2ℤ + 1/ν_X ∉ ℤ.

  Exhausted over every 15-stack ν_X and every tuple of odd addends of length < 4 (and the two closed forms cover all lengths). No integer ℓ_m. The m=1 instance is exactly the written Case A (k_1 = 2ν_X ≥ 10, which already refuses k_1 | 2). Case B remains impossible because it skips X’s gap.

  **Erratum to write.** Replace “level 1 belongs to X or F1” by: every finite ladder is a (possibly empty) non-killing prefix with k_j | 2, followed by X-death while F1 is still alive; the prefix is printed-legal and delta-integral; the subsequent X-death never has ℓ_m ∈ ℕ. The checker’s obstruction block must grow a Case C loop or the “15-stack two-case” sentence is a false description of what was machine-checked.

  The kill *claim* — no global (k_j, ℓ_j) ladder for any synchronized direct representative — survives this patch. That is why this is an erratum and not a break.

### 2. Severity: erratum — scope: §11a as a cell census is untouched; the trunk *completion* of this cell is not a genuine escape

- File: `TOWER-9-15.md:305-325`; certificate `obstruction.scope`; `BOOK-OFFAXIS.md:693-757`; `xmodel/sol-gluing-design.md:971-972, 1243-1308`; `xmodel/sol-sixcells.md:7, 295-296`
- Claim: killed = the tower tier of every synchronized representative of the *direct* (2/3,3,2) completion in design §3.2; not killed = the (9,15,7,3)@2 cell, because its trunk completion (35,15,7,5)@(2/5,5,1) “has a different terminal frame (ψ=1, budget 5) and a different synchronization problem.”
- How checked.

  **What §11a actually lists.** Promoted H5a/Q+E5 book: 17 cells, 233 deduplicated routes. The cell `(9,15,7,3)@2` contributes 4 raw / 4 equality / 2 deduplicated records (`BOOK-OFFAXIS.md:757`, design table at `:971`). The two equality endpoints are exactly the pair already dual-certified in `sol-sixcells.md` and `grok-sixcells-review.md`:

  | completion | (w,M,ψ) | λ | §11a status after this kill |
  |---|---|---:|---|
  | direct case-IV | (2/3, 3, 2) | 4 | tower-dead (this certificate) |
  | one trunk step through (35,15,7,5) | (2/5, 5, 1) | 5 | still listed; see below |

  The other 16 §11a cells are not examined. The arrival census row itself (w_U=1/2, rec. ν=7, λ=4) is arrival-tier and correctly untouched. Milestone 2 emission for the *direct* route is correctly moot.

  **What the kill actually removes from the book.** It removes the *coefficient/tower* life of 1 of the 2 deduplicated `(9,15)` equality routes (2 of the 4 raw M2=2/M2=4 arrivals to the (2/3,3,2) terminal). It does **not** remove the cell from the 17-cell §11a list. The writeup’s “route-family-scoped, not cell-scoped” sentence is the right cell-level claim.

  **The trunk is not a different synchronization problem.** (H8) at G toward H2 is `deg p_{f,H2} = i_G · μ_e = 22610 · 2 = 45220`, read *up from the priced chain-2*, independent of whether the rootward neighbour of G is R0 or the trunk vertex (35,15,7,5). A direct G—P1 edge would need `2 = 22610 · μ_e`, μ_e not an integer: chain 1 is still forced, the f-degree ladder is still 2 → 22610, the product of characteristics is still 11305, F1 is still the same (20,16) vertex with i=2, both poles are still type (2,3), and the death-gap table on {X, F1, F2, F3, H2, G} is the same. The obstructing clash lives entirely on the pole-to-merge subtree, which the two completions share.

  Budget does not open an escape: trunk λ = 4+1 = 5 = 6−ψ saturates the new budget, so chain 1 is still uncharged (`sol-sixcells.md:295-296`). R1.2 still forbids a return to w=2 after an n≥2 clean step (Δ = (n−1)ν+1, n/Δ < 1 on the n≥2, ν≥2 lattice; printed `BOOK-OFFAXIS.md:242-246`).

  A trunk vertex inserted *rootward* of G has a death gap at most on the order of G’s 1/13566, far below gap(X). It cannot claim a level between 5/2 and gap(X), and it does not change α_1 = 3/2.

  **Erratum.** Replace “different synchronization problem; nothing here examines its tower” with: the written certificate does not *re-run* C3 on a trunk spine, but the clash arithmetic is terminal-independent, so either the trunk completion of this cell is dead by the same proof or the authors must name a terminal-dependent escape that changes i_G, the chain-1 product, i_{F1}, or the type. “Untouched” is only honest as a statement of what was machine-checked, not as a survival claim. The other 16 cells remain genuinely unexamined.

### 3. Severity: clear — Attack (1) fails. The printed theory does not allow a per-pole-branching (k_j, ℓ_j) at a shared alive level; that reading would not dissolve the clash

- File: `TOWER-9-15.md:277-285`; `refs/sigray_full.pdf` pp. 19–22, 32, 41; `SHEET6-TEMPLATE.md:50-80`; `SHEET6-R6.md:10`; `SHEET6-A3L1-REVIEW.md:42-55`
- Claim: Prop 4.2 is one global sequence h_0, h_1, … of polynomials; a per-branch tower would be a new reading.
- How checked.

  **What the page actually says.** Prop 4.2 opens “Set F ∈ T_a^+” and produces *per-vertex* data m_F, K_F, L_F, S_F, h_{j,F}. Notation 4.1 defines F ≼ G by “m_F ≤ m_G and K_F (resp. L_F, S_F) is a prefix of K_G.” This is not, by itself, one sequence for the whole tree.

  Prop 4.4’s “in particular, for any F ∈ T_a^+, either F ≼ F′ or F′ ≼ F” is *not* totality of ≼ on all of T_a^+. The proof starts “Set F = F_j ∗ c … c is a root of p := p_{F′}”: F′ is the adjacent vertex along the characteristic, the same pair Prop 4.4’s uniqueness (k,ℓ,s) is about. Compare Prop 4.5, which specialises the same sentence to the two roots. A referee who took “F′” as an arbitrary second vertex would be misreading the proof.

  **What glues the two poles.** St 8.3 (p. 41), verbatim: if F ∈ T_a^& ∩ (V_a \ {(0,y)}) equals G ∗ c, then for 0 ≤ j ≤ m_F one has h_{j,F} = h_{j,G}, and for j < m_F the pairs (k_j, ℓ_j, s_j) agree. Cor 6.1 (p. 32) plus the LT-review on-page reading (`SHEET6-LT-REVIEW.md:139-141`) give F ≺ F′ at every searrow V_a vertex other than (0,y). Every non-pole vertex of this route is in T_a^&:

  ```
  (1−π) deg p_f / d_f  =  15 (G), 11306 (N), 8 (H2), 6 (F3), 35 (F2), 16 (F1)  > 1.
  ```

  (Independent replay of the printed criterion on p. 32.) St 3.16 puts the non-pole chain vertices in V_a. So N ≺ G and H2 ≺ G. Prefix transitivity: K_N and K_{H2} are both prefixes of K_G, hence they agree on min(m_N, m_{H2}) steps. While both branches are alive they share one (k_j, ℓ_j, s_j) and, by St 8.3(i), the *same polynomials* h_j. After one branch dies it no longer produces a next pair. There is nothing left to “branch per pole” at a shared alive index.

  **The suggested escape therefore does not exist.** A per-pole-branching tower with different (k_1, ℓ_1) on chain 1 vs chain 2 *while both are alive* contradicts St 8.3(i) + Cor 6.1. If only one is alive, that is Case A/B (or the patched Case C), already refuted. The clash does not dissolve.

  **Citations: upgrade, do not drop.** `SHEET6-R6.md:10` is a weak witness. It is a window filter `gcd(k_1,ℓ_1)=1` on *candidate genomes* for one template tree, not a proof that two poles of one pair share a ladder. The td=6 template (`SHEET6-TEMPLATE.md:59-80`) does use one ladder (2,3), (3,4), (7,23) at both poles, and C2 reproduces that genome with zero free parameters — calibration, not a uniqueness theorem. The printed uniqueness is St 8.3 + Cor 6.1 + Not 4.1, which the certificate’s `dependencies` list under-cites (it names Prop 4.2 and the campaign formalization, not St 8.3(i)).

  The formalization “one global ladder whose prefixes are the per-vertex K_F” is the correct reading *for this route*. It is slightly stronger than “the h_j are global polynomials” and slightly weaker than “≼ is a total order on all of T_a^+.” Both of those slogans should be retired.

### 4. Severity: clear — Attack (2) fails. Prop 4.2’s proof is a dichotomy, not a trichotomy; “alive ⇔ δ_j > 0” is the printed reading

- File: `TOWER-9-15.md:286-290`; `refs/sigray_full.pdf` pp. 19–20; `SHEET6-TEMPLATE.md:50-53`; `SHEET6-R6.md:126`
- Claim: a state with δ_j > 0 but without the leading-part identity would reopen Case A/B.
- How checked. Printed (10), p. 19: J(f_F^+, h_{j,F}^+) equals (f_F^+)^{α_j} ξ^{−u} on equality of d_F + d_{h_j,F} = α_j d_F + 1 − u, and equals 0 on the strict inequality. The next page defines δ_j := κ(d_F + d_{h_j,F} − α_j d_F − 1 + u) ∈ ℕ and proves it strictly decreasing. So

  ```
  δ_j = 0  ⇔  equality in (10)  ⇔  set m := j (dead),
  δ_j > 0  ⇔  strict inequality  ⇔  J = 0  ⇔  unique (k_j,ℓ_j,s_j) with (iii) (alive).
  ```

  There is no printed third state. The identity (iii) is not an extra assumption piled on “δ>0”; it is the J=0 case of the same dichotomy. `SHEET6-R6.md:126` (“h2 ALIVE at F_s” as the δ_2>0 reading) and `SHEET6-TEMPLATE.md:51-53` match the page. The template exhibits no intermediate state, and the proof leaves no room to invent one.

  One wording nit, not load-bearing: the certificate’s `laws.alive` writes p_{h_j} = H · p_f^{ℓ/k} “with every factor exponent a nonnegative integer.” The printed (iii) is the leading-part identity; the factor-exponent form is the chart translation. Prop 8.1 p. 40 already gives the weaker (and here equivalent) integrality i ℓ/k ∈ ℕ. Fine as a gloss.

### 5. Severity: clear — Attack (3) fails. The death equation is the alive-rewrite of printed δ together with (10); Cor 6.1 is a cousin, not the source

- File: `TOWER-9-15.md:140-144, 291-294`; certificate `tower.laws.death_gap`; `cases/tower_check.py:189-207, 429-464`; `refs/sigray_full.pdf` pp. 19–20, 32, 39–40
- Claim: δ_m=0 ⇔ g_m = κ̄/D_f, equivalent to Cor 6.1’s q-law plus f-transport; three interlocking printed derivations of one number.
- How checked.

  **Printed δ and the alive rewrite.** Prop 4.2 defines δ_j from (d_f, d_{h_j}, α_j, π). On the alive range j < m one has d_{h_j} = (ℓ_j/k_j) d_f by (iii), hence

  ```
  δ_j  =  κ( (ℓ/k + 1 − α) d_f − (1−π) )  =  D_f · g_j − κ̄,
  g_j  :=  ℓ_j/k_j + 1 − α_j.
  ```

  C2 checks this identity at every template (vertex, j) against the filed δ-tables (104,34,4)/(100,30,0)/(10,0)/(0). Independent replay of the two death specialisations: g_1(G_m) = κ̄/D = 5/6 and g_2(F_s) = 5/42, matching (k,ℓ) = (3,4) and (7,23). On this route every certificate death gap equals κ̄/D_f at that vertex (C3, re-derived).

  **Why m is the first j with g_j = κ̄/D_f.** For j < m the rewrite applies and g_j is strictly decreasing (δ decreasing at any vertex that sees the whole prefix; in particular at G, and already from the printed δ-descent). So δ_j > 0 iff g_j > κ̄/D_f. At j = m the printed (10)-equality forces δ_m = 0 by definition of m. Therefore a vertex dies at the first ladder index whose global g_j equals its own κ̄/D_f. That is the death equation. It does *not* require the alive identity d_h = (ℓ/k) d_f at the dying index (where (k_m, ℓ_m) is not even produced). Both expressions vanish for different printed reasons; they agree because they are both zero, not because the intermediate identity persists.

  **Cor 6.1 is not the q-law.** Printed Cor 6.1, p. 32: for F ∈ T_a^& ∩ V_a \ {(0,y)}, deg(p_{h,F}) = (d_{h,F}/d_F) deg(p_F), and therefore F ≺ F′. The certificate’s “q-law d_q = κ̄ deg p_f / D_f” is the θ-identity / Prop 8.1 frame rewrite d_q = d_p · κ̄ · i / D_f, which C1 checks at all six non-pole non-root vertices and which I re-derived as an exact identity on those six. It is consistent with Cor 6.1 plus Prop 8.1(ii) at a dead member (p_h = S p^k q, k = i(μ−1), d_h = (μ−1)d_f + (1−π)), but it is not a sentence Cor 6.1 prints. Citation cleanup, not a broken equation.

  An error in the death equation would have to break either printed (10) or the alive rewrite of δ, both of which C2 locks to the template genome. Attack (3) does not open a route.

### 6. Severity: clear — Attack (4): the checker’s Case A/B block is arithmetically exact; C6 catches its own listed perturbations; it does not implement Case C and contains one tautology

- File: `cases/tower_check.py`; `cases/towers/t9_15_direct.json`
- Claim: 258 checks, exit 0, 15-stack two-case exhaustion all refuted, 7-case negative-perturbation self-test.
- How checked.

  **Ran.** `python3 cases/tower_check.py` from the repo root: exit 0, status `TOWER-OBSTRUCTED`, every C1–C6 family printed PASS, including C5 token-for-token against the literal `### 3.5` block of `xmodel/sol-gluing-design.md` and C5b on all 74 regenerated rows at the exact rational anchor (including the 7^{22610}-sized scale values, evaluated as integers).

  **Independent Case A/B replay, all 15 divisors of 11305 = 5·7·17·19:**

  | ν_X | gap | (k_1,ℓ_1) | δ_1(F1) | F1-alive (k_1 | 2) |
  |---:|---|---|---|---|
  | 5 | 3/5 | (10,11) | 2 ∈ ℕ | no (22/5, 11/5) |
  | 7 | 4/7 | (14,15) | 12/7 | no |
  | 17 | 9/17 | (34,35) | 22/17 | no |
  | 19 | 10/19 | (38,39) | 24/19 | no |
  | 35 | 18/35 | (70,71) | 8/7 | no |
  | 85 | 43/85 | (170,171) | 18/17 | no |
  | 95 | 48/95 | (190,191) | 20/19 | no |
  | 119 | 60/119 | (238,239) | 124/119 | no |
  | 133 | 67/133 | (266,267) | 138/133 | no |
  | 323 | 162/323 | (646,647) | 328/323 | no |
  | 595 | 298/595 | (1190,1191) | 120/119 | no |
  | 665 | 333/665 | (1330,1331) | 134/133 | no |
  | 1615 | 808/1615 | (3230,3231) | 324/323 | no |
  | 2261 | 1131/2261 | (4522,4523) | 2266/2261 | no |
  | 11305 | 5653/11305 | (22610,22611) | 2262/2261 | no |

  Case B: (k_1,ℓ_1)=(10,9), alive exponent at X is 9/5 ∉ ℕ, death needs ν_X=−5. Matches the checker line-for-line, including the ν_X=5 specialisation (only integral δ_1(F1), dies on exponents).

  **Forcing lemmas, replayed.**
  - 11305 odd ⇒ every ν_X ≥ 5 odd; gap(X) = (ν_X+1)/(2ν_X) ∈ (1/2, 3/5].
  - R1.2 Δ = (n−1)ν+1 (`BOOK-OFFAXIS.md:242`); n/Δ < 1 for all n≥2, ν≥2 (lattice n<20, ν<40, 0 failures). Chain 1 frozen at w=2 cannot use a clean n≥2 step and return. Budget 4=6−ψ (`arrival.lambda_steps` sums to 4) forbids a charged/dirty chain-1 step. Pure n=1 neutrals, product of characteristics 22610/2=11305, is forced.
  - Pole-adjacent shape: deg p_{f,X} = 2ν_X and d_{q,X} = ν_X+1 from root law + pole multiplicity 2 + μ_e=1, independent of the reduced p-shape. Intermediate stack vertices have strictly smaller death gaps (Finding 1), so they do not steal level 1.
  - Both poles satisfy the type-(2,3) death equation g_0 = 5/2; the P1/P2 leading collapses of g^2−f^3 replay by exact η-calculus at two A-samples each (C3), and Prop 4.1 closes at both poles (re-derived: d_f+d_g = 1−π).

  **C6.** All seven listed perturbations raise ≥1 failure (2, 2, 2, 7, 4, 1, 1). Extra hostile probes the suite does *not* contain:
  - a Case C “survivor” record (Finding 1): C3 would still pass;
  - flipping only `obstruction.status` while leaving `checked_stacks=15`: the checker tests the integer 15 and the status string, so a status-only flip *is* caught; a semantically wrong but well-formed obstruction (e.g. claiming Case C was checked) is not;
  - the tautology at `tower_check.py:454-455`, `3 == 3`, labelled “F1→P2 h1 count.” That line does not compute `mult(η(t−A)^3 R1^2, c_{f1})`. The surrounding P2 collapse to degree 3 is real; this particular assert is not.

  **m_2 corroboration is weaker than the main kill.** `m_G=1` is a genuine St 3.11(i) comparison (22611 > 11306) and does not need St 8.3(ii). The two drop-window checks verify the *claimed numerical identities at the claimed s* (33915·22611 − 45222 = 33913·22611; 3·11309 − 11309 = 2·11309). They do not derive the window bounds from St 3.11. This block is corroboration for the design’s own one-vertex representative, not a second proof of the 15-stack kill.

  **Spine / local / pilot, since the kill is scoped on top of them.** C1 closes every advertised (F3)/(F4), R1.2, R2.1-II, E5-III with the Q-value κ_{H2}=7 (not 49), (J4)/(J5), Cor 6.1 q-law, (H7)/(H8), both pole Prop 4.1 identities, and the (R1)–(R3) package. C4 regenerates every T1 C̃ at A∈{5, −3/7} and both pole Wronskians at two further samples. C5/C5b match the design block and the anchor. I did not re-litigate H5a or the six-cell T1 substitutions; those are promoted SOUND (`grok-h5a-review.md`, `grok-sixcells-review.md`) and C6’s κ_{H2}=49 / mixed-n perturbations confirm this certificate actually uses the Q+E5 pin. No CONJECTURE beyond the promoted set enters the kill.

### 7. Severity: suggestion — the §6 parity lemma is sound as a *mechanism* for this cell; it is not a theorem that kills the trunk or the other 16 §11a cells

- File: `TOWER-9-15.md:317-325`
- Claim: type-(2,3) forces α_1=3/2; a pole-adjacent odd-ν chain-1 vertex produces k_1=2ν_X even and large; a tiny-i vertex on the other chain (here i_{F1}=2 from the (1,2,3) pole) caps k_1 | 2. “Candidate general kill lemma for the trunk route and the other 16 cells.”
- How checked. For *this* direct family the mechanism is exactly Finding 1’s squeeze, and it is printed-tier once the Case C patch is written. Ingredients that are *not* automatic on a random §11a route:

  - **Type (2,3) at both poles.** Global by Lemma 2.1 *for a given pair*, and standing for the td-7 two-pole campaign, but a cell whose priced chain-2 ends at a different pole type changes (k_0,ℓ_0) and α_1.
  - **Odd chain-1 characteristic product.** Here it is 11305 because i_G=22610 is even and the P1 multiplicity is 2. Other merges have other i_G; an even ν_X can drop gap(X) to ≤ 1/2 and change the order against chain-2 gaps.
  - **A chain-2 vertex with i | 2 still alive when X dies.** i_{F1}=2 is forced by this priced (20,16)→(1,2,3) handoff, not by §11a membership. A cell whose cheapest chain-2 vertex has large i leaves k | i too loose to contradict k=2ν_X.
  - **Budget saturation forbidding a charged chain-1 step.** Several §11a rows have slack (λ < 6−ψ). A charged or dirty chain-1 step can change w, the degree product, and the pole-adjacent gap formula.

  The trunk completion of *this* cell happens to share every one of those ingredients (Finding 2), so the lemma *does* apply to it — which is the opposite of the writeup’s “candidate for the trunk” flavour, and should be stated as a corollary, not a conjecture. For the other 16 cells the right next move is a one-page checklist (type, i_G parity, min i on the priced chain-2, chain-1 budget residual, pole-adjacent gap vs smallest chain-2 gap), not a slogan.

### 8. Severity: nit — small documentary and checker inaccuracies that do not move the verdict

- `TOWER-9-15.md:4-7` and `:331` advertise “258 checks.” I did not independently recount the `check()` calls (C2+C1+C1b+C4+C3+C5+C5b plus the 7 perturbations, each perturbation re-running the whole suite quietly). The exit-0 transcript is consistent with a count of that order. Do not treat 258 as a theorem.
- Certificate `tower.ladder[1].kl = "OBSTRUCTED"` is a status, not a pair; harmless if read as such.
- C3’s w-monotonicity lattice is n<12, ν<24, not a proof that n/Δ<1 for all n,ν≥2. The inequality is immediate from Δ−n = (n−1)(ν−1) ≥ 1. Cite the one-line identity, drop the lattice.
- `laws.counts` correctly refuses St 8.3(ii) at a dead member (`SHEET6-R6.md:137-140`). The kill never needs it.
- Fiber-zero PLUS orientation (h_0=g, base f, L rootward) matches Prop 4.2’s T_a^+ setup and the template gauge. No side error.

---

## Attack ledger (requested order)

| # | Attack | Result |
|---|---|---|
| 1 | Global-single-ladder reading of Prop 4.2 is not the printed one; per-pole branching dissolves the clash | **Fails.** Prop 4.2 is per-vertex; St 8.3(i)+Cor 6.1 identify K_F and the polynomials h_j along both merge edges; shared-alive (k,ℓ) cannot differ by pole. `SHEET6-R6.md:10` is usage, not the proof; upgrade the citation. |
| 2 | Aliveness is not a dichotomy; a between-state reopens A/B | **Fails.** Printed (10) is J=0 vs J=(f^+)^{α}ξ^{−u}; δ>0 iff alive with (iii). |
| 3 | Death equation g_m=κ̄/D_f is a campaign invention | **Fails.** Alive rewrite of printed δ, plus (10) at m. Cor 6.1 is a cousin; the literal q-law is the Prop 8.1/θ rewrite. C2 locks the identity to the template. |
| 4 | 15-stack exhaustion is wrong or the checker is theatrical | **A/B exact; C missing.** Independent replay confirms every A/B row and both forcing lemmas. C6 catches its seven listed perturbations. Case C is untested in the engine; `3==3` is a tautology. Patch in Finding 1. |
| 5 | Scope creep: this quietly kills the cell / the §11a book / or, conversely, the trunk is a live escape | **Cell and the other 16 §11a cells survive as stated. Direct (2/3,3,2) family dies. Trunk completion of this cell shares the clash and is not a demonstrated escape.** Removes 1 of 2 deduplicated `(9,15)` equality routes from *tower* life; does not change the 17-cell arrival census. |
| 6 | Parity lemma is unsound, or it already kills the trunk and the rest of 11a | **Sound as the mechanism of *this* squeeze; corollary for the trunk of this cell; not a theorem for the other 16.** |

---

## What would actually break the kill

The list in doc §5 is almost the right attack surface. After this review, the live ways out are:

1. A printed construction of a *third* J-state, or a reading of (iii) that does not force iℓ/k ∈ ℕ at F1. Neither is on pp. 19–20 or p. 40.
2. A demonstration that Cor 6.1 or St 8.3 fails at N or H2 (they do not: both are searrow V_a). That is the only printed door to a genuine per-branch (k_1,ℓ_1).
3. A charged or dirty chain-1 step that is budget-legal on the *direct* completion (it is not: 4=6−ψ).
4. A pole-adjacent gap formula other than (ν+1)/(2ν) for some admissible stack shape. Root law + pole multiplicity 2 close the degree and d_q; the gap does not see the rest of the shape.
5. Reverting H5a from Q+E5. Different perimeter; this certificate does not claim that book.

A non-killing level 1, which §5 does not list, looked like a sixth door and is not one (Finding 1).

---

## Bottom line

Promote the *kill of the design §3.2 synchronized direct family* after the Case C paragraph is written into `TOWER-9-15.md` §3 and a Case C loop is added to C3. Do not promote the sentence that the trunk completion is a live remaining object without either running C3 on a trunk spine or recording the terminal-independence corollary. Do not promote §6 as a 17-cell theorem. The spine, local T1 layer, LEAD-PILOT regeneration, and Q+E5 transport of this certificate are not in doubt.
