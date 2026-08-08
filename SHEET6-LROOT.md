# SHEET6-LROOT.md — the λ_root ≥ 1 lemma, decided (the 8→4 kill attempt)

Status: COMPLETE (2026-08-07, this session; UNREVIEWED). Target:
SHEET6-A3L1-REVIEW.md final note / SHEET6-CAMPAIGN.md header "next kills":
does the root vertex (0,y) necessarily carry λ_root ≥ 1 — one unit of the
St 9.4 budget charged at the root beyond the ψ-certificate — killing the 4
slack-0 classes and cutting the survivor book 8 → 4? Ground truth:
papers/sigray_full.pdf read on-page (printed page = pdf page; §3 pp. 10-18,
§5 pp. 23-28, §7 pp. 35-39, §9 pp. 48-51). Engine: cases/lroot_ledger.py
(NEW, additive, standalone; no existing engine or gate touched; campaign
gate re-run PASS).

VERDICT: **(b) REFUTED — and not merely unprovable: λ_root = 0 is FORCED
for every case-IV terminal, i.e. for all 8 survivors.** Case IV's own
hypothesis (0,y) ∉ V_{1,a} ∪ V_{2,a} (Prop 9.3, p. 50) says, by Definition
3.4 (p. 11), that no two y-side punctures have contact 0; so no branch of
the tree separates from the characteristic path AT the root, and the root's
Y-set (Not 9.3, p. 49, E9 branch-at-F reading) is EMPTY. There is no second
cv-branch at the root because case IV *is* the hypothesis that the root has
a single Puiseux direction. The AF3 §5 negative ("λ_root already charged as
ψ") is confirmed and strengthened: the ψ-charge lives in the OTHER
component of the tree (St 3.3: T_a* has two components), so no
double-charge was ever possible — but no y-side root charge exists to add.
The full Euler-characteristic ledger (Prop 7.5 (22)) balances exactly at
λ_root = 0 for an explicit minimal instantiation of every survivor
(§4). **Book stays 8.** Positive yield (§5): the ledger FORCES, for all 8
classes, a single x-side cv vertex with κ_G = 1 (the x-side of any carrier
is one unsplit Puiseux cluster below height R ≥ 3) — a new rigid datum for
the coefficient-template lift — and, for the 4 slack-0 classes, TOTAL
budget rigidity: every inequality in (22) is an equality, including
δ_a = 0 for EVERY fiber a ∈ C. One new thesis erratum (E10, §6).

## 1. The budget identity, itemized (the exact ledger)

All from §7 of the thesis, read on-page.

- Not 7.1 (p. 35): T_a,cv := {F ∈ T_a^0 : d_{g,F} = 0}, where T_a^0 =
  {d_F = 0} (Not 3.14, p. 16). So a cv vertex sits at the unique (St 3.13,
  p. 16) d = 0 point of its ray, with d_g = 0 there too. St 7.1 (p. 35):
  π(F) > 1 for F ∈ T_a,cv; with κ_F(π(F)−1) ∈ N (St 9.4's proof line,
  p. 49) every cv vertex carries mass κ_F(π(F)−1) ≥ 1.
- Prop 7.2 (p. 36): g(P) ∈ C ⟺ the ray of P carries a cv vertex
  F̂_P := I_P(u) (Not 7.2). Prop 7.3 (pp. 36-38): the punctures continuing
  from a cv vertex F in one direction c (p_F(c) = a) carry total Λ-mass
  ≥ κ_F π(F) − κ_F, with equality iff mult(p_F − a, c) = 1.
- Prop 7.5 (p. 38), identity (22): for T_{a0,cv} = {F_1,…,F_s},

      td(f,g) = 1 + Σ_{i=1}^s κ_{F_i}(π(F_i) − 1) + Σ_{a∈C} δ_{F_i,a},

  δ ≥ 0 (Prop 7.4), = 0 at generic a. Proof = Euler characteristic of C²
  computed against the value-curves (p_{F_i}(c), p_{g,F_i}(c)) ≅ C: each cv
  VERTEX is charged ONCE (χ(C) = 1), regardless of how many punctures or
  directions sit above it. Cor 7.1 (p. 39) is the subset inequality:
  any {F_1,…,F_n} ⊂ T_a,cv gives td ≥ 1 + Σ κ_{F_i}(π(F_i)−1).

So the EXACT budget is: **td − 1 = Σ_{cv vertices of a generic-a tree}
κ(π−1) + Σδ**, and every spend is a cv vertex (or δ-excess). Where can cv
vertices sit, for a survivor carrier? The tree T_a* has exactly two
components (St 3.3, p. 11): the y-component rooted at (0,y) (all rays pass
I_P(0) = (0,y); root data d = l_f, deg p = k_f, searrow by Thm 6.1) and
the x-component rooted at (0,x) (d = k_f, deg p = l_f, nearrow). The
partition of T_{a,cv}:

1. **Chain vertices: never.** The characteristic path F_0 … F_n = (0,y)
   lies in T_a^+ (d_{F_0} > 0 at the pole vertex, and d is monotone
   decreasing in u, St 3.10(i), so d ≥ d_{F_0} > 0 along the whole path
   down to d_{(0,y)} = l_f > 0). T_a,cv ⊂ T_a^0: disjoint. The ψ- and
   λ-spends are structurally off-path rows of (22) — no overlap possible.
2. **Above the pole vertex/vertices: never.** Prop 5.3(v)/(vi) (p. 25):
   at a pole vertex p_F and p_{g,F} are coprime; its proof shows
   deg(p_{g,G}) = 0 and d_{g,G} = d_{g,F} > 0 for EVERY G above F. By the
   value dichotomy (St 3.15 with corrected labels, E10 §6: d_h frozen
   positive ⟺ h(P) = ∞) every puncture above a pole vertex is a g-pole;
   by Prop 7.2 no cv vertex sits there. Pole clusters are PURE. (Sanity:
   Prop 5.8 (20) already allocates ALL td units of pole mass to T_a,pole,
   so no pole hides anywhere else either — in particular the x-component
   carries NO poles, since a T_a,pole vertex's characteristic sequence
   descends searrow to (0,y) (Prop 8.4's proof, p. 44) and an x-side
   sequence would land on the nearrow (0,x).)
3. **y-side branches leaving the path at F_i, i ≤ n−1: the chain λ's.**
   Every y-ray passes through (0,y), hence meets the path; consecutive
   path vertices are F_{i+1} = F_i°, so separation happens exactly AT some
   F_i (V_2,a separation points are vertices, Def 3.4). Punctures leaving
   strictly below F_0 are g-finite (their F_P* would otherwise be a second
   pole vertex off the path), so each leaving cluster carries ≥ 1 cv
   vertex; St 9.3 (24) (p. 49) prices it — this is exactly λ_{F_i} under
   the E9 branch-at-F reading, ≥ the AF2 orbit minima. These are the Σλ
   the campaign charges.
4. **y-side branches leaving AT (0,y): λ_root. This is the lemma's slot.**
   Adjudicated in §2: EMPTY in case IV.
5. **x-side cv vertices: the ψ-certificate, quantized.** Every x-side
   puncture is g-finite (item 2), so every x-ray carries a cv vertex; by
   the slope law (St 3.10: d ≥ k_f − u·l_f since deg p ≤ deg p_{(0,x)} =
   l_f, Lemma 2.1(i) + St 3.12) its height is ≥ k_f/l_f, so each DISTINCT
   x-side cv vertex costs κ(π−1) ≥ κ·(k_f/l_f − 1) ≥ ψ. St 9.4 (p. 49)
   charges one such vertex; §3 shows one is all a survivor can afford.
6. **δ-excess: Σ_a δ_a ≥ 0**, zero at generic fibers; not known to be
   forced positive anywhere (§5c).

## 2. λ_root = 0 is forced at every case-IV terminal

**Lemma LR1.** Let the characteristic sequence terminate at (0,y) via
Prop 9.3 case (IV). Then, under the E9/H2 branch-at-F reading of Not 9.3,
Y((0,y)) = ∅ and λ_{(0,y)} = 0.

Proof. Case IV's hypothesis is F = (0,y) ∉ V_{1,a} ∪ V_{2,a} (p. 50).
By Def 3.4 (p. 11), (0,y) ∈ V_{2,a} iff (0,y) = I_P(O(P,P*)) for two
punctures, i.e. iff two y-side punctures have contact O(P,P*) = 0
(x-side pairs give O = −1, not a vertex; cross-component pairs likewise —
Def 3.2, St 3.3). So in case IV every pair of y-side punctures has contact
> 0: all y-side Puiseux series share their first coefficient, i.e.
p_{(0,y)} = ⊖(η−c)^{k_f} has a single root (Prop 3.1(∗∗), p. 14, at level
0), and every y-ray runs THROUGH the first path vertex G = (0,y)+c above
the root. No ray separates from the path at (0,y); a branch-at-(0,y) cv
vertex would need one. ∎

Remarks.
- Under the LITERAL Y-definition λ_{(0,y)} would instead be the whole
  y-side cv mass (every y-ray passes I_P(0)) — the E9 double-count, under
  which St 9.5 is false as printed; either way no NEW unit appears at the
  root. The lemma's hoped-for content does not exist in any reading.
- LR1 also re-derives why the terminal ψ is sharp: single root ⇒
  k_f = deg p_{(0,y)} = mult(p_{(0,y)}, c) = deg p_G (St 3.17(i), p. 18),
  so k_f/l_f = deg p_G/d_F = R EXACTLY — the AF3 §5 ψ-upgrade blocker,
  now with the exact equality forced rather than merely unobstructed. In
  particular R ∈ N for all 8 classes (R ∈ {3,4}) and ψ = R − 1.
- Contrapositive (the lemma's true, useless content): λ_root ≥ 1 DOES hold
  whenever (0,y) ∈ V_{2,a} — a second root direction carries g-finite
  punctures (no second pole cluster in single-pole configs; poles are one
  cluster) whose cv mass ≥ 1 charges the root slot. But (0,y) ∈ V_{2,a} is
  exactly NOT case IV: the sets are complementary. This retroactively
  double-kills SF1-type case-I/II/III root terminations (H3 §7) — already
  vacuous in the pinned book (their entries are AF3-entry-dead) — since a
  V_2-root termination pays #(root directions) − 1 extra units.

## 3. The x-side quantum: one cv vertex, κ_G = 1, for all 8

**Lemma LR2.** For any survivor-class carrier (all have ψ ≥ 2, Σλ = 2,
slack ≤ 1): the x-component of T_a carries EXACTLY ONE cv vertex G, with
κ_G = 1 and π_G ∈ [R, R + slack]; equivalently, all l_f x-side Puiseux
series form a single cluster (pairwise contact ≥ π_G ≥ R) with no
characteristic exponent below π_G, and both p- and g-patterns unsplit
below π_G on that ray in the slack-0 case (where π_G = R exactly).

Proof. By §1 items 1-5, (22) gives td − 1 ≥ Σλ + Σ_{x-cv vertices}κ(π−1).
Each x-side cv vertex costs ≥ ψ = R−1 ≥ 2 (§1 item 5 + integrality); two
would cost ≥ 2ψ > ψ + 1 ≥ ψ + slack = (td−1) − Σλ. So one vertex;
κ_G ≥ 2 would likewise cost ≥ 2(R−1) > ψ + slack. A split of the x-side
f-tree below height π_G would put punctures in ≥ 2 subtrees with no common
vertex above the split, hence ≥ 2 cv vertices: excluded. In the slack-0
case κ_G(π_G−1) = ψ exactly forces π_G = R = k_f/l_f = k_g/l_g (Lemma
2.1(ii)), which by the slope law needs deg p_{·} ≡ l_f and deg p_{g,·} ≡
l_g below G (any early split lowers a slope and pushes π_G up). ∎

Note the pleasant mechanism: on the x-ray, d_{f−a}(u) = k_f − u·l_f and
d_g(u) = k_g − u·l_g vanish at the SAME height k_f/l_f = k_g/l_g — the
normalization (Lemma 2.1(ii)) makes f and g exhaust together on the
x-side, which is exactly Prop 7.2's requirement (cv vertices live in
T^0 ∩ {d_g = 0}). The x-side charge is the St 9.4 ψ, now localized: it is
the unique d = 0 point of the single x-cluster.

## 4. Per-class ledgers (engine: cases/lroot_ledger.py, all asserts pass)

Budget td − 1 = 5. Spend rows: [x-side] + [y-side orbit clusters = Σλ] +
[λ_root] + [pole clusters] + [δ]. Forced rows in **bold**.

| class | terminal parent Q | k_f, l_f | type; (k_g,l_g) | x | y | root | pole | δ | slack |
|---|---|---|---|---|---|---|---|---|---|
| SP-1 (1/3,7,3,5)@2 R3 | (21,63,7,3,5) | 63, 21 | (3,5); (105,35) | ≥2 | 2 | **0** | **0** | ≥0 | 1 |
| SP-2 (1/4,5,4,4)@2 R4 | (15,60,5,4,4) | 60, 15 | (3,5); (100,25) | **3** | **2** | **0** | **0** | **0** | 0 |
| SP-3 (2/3,3s+2,…)@2 R3 | SP-1 node + IIa_0 | s-scaled, R3 | (3,5) | ≥2 | 2 | **0** | **0** | ≥0 | 1 |
| SP-4 (3/4,4s+3,…)@2 R4 | SP-2 node + IIa_0 | s-scaled, R4 | (3,5) | **3** | **2** | **0** | **0** | **0** | 0 |
| 2P-R3a (1/3,7,3,5)@2 | (42,126,7,3,5) | 126, 42 | (2,3); (189,63) | ≥2 | 2 | **0** | **0** | ≥0 | 1 |
| 2P-R3b (2/3,…)@2 | R3a node + IIa_0 | s-scaled, R3 | (2,3) | ≥2 | 2 | **0** | **0** | ≥0 | 1 |
| 2P-R4a (1/4,5,4,4)@2 | k=2 suffix step | shape-level, R4 | (2,3) | **3** | **2** | **0** | **0** | **0** | 0 |
| 2P-R4b (3/4,…)@2 | R4a node + IIa_0 | s-scaled, R4 | (2,3) | **3** | **2** | **0** | **0** | **0** | 0 |

Itemization details (single-pole; entries exact, table (23) row 9 =
(3,5),(6,10),ν5, Q = (3,6,5,2,8) — no j-unit at the entry, since Λ =
D_g·deg p/ν = 6 = td pins the absolute sizes):

- **SP-2 (the sharpest slack-0 case), full series audit.** Chain F_0 =
  (3,6,5,2,8) → F_1 = (15,60,5,4,4) (μ=2 IIa k=2, n=12) → (0,y).
  k_f = deg p_{F_1} = 60, l_f = d_F = 60(1/4+5−4)/5 = 15 (Prop 9.3(k)),
  R = 4, ψ = 3. Root split of the full pattern at F_1 (reduced
  (η⁵−c⁵)²·Π₂, i = 3): chain orbit 5 dirs × mult 6 — of which ONE
  direction's 6 series continue to F_0 (deg p_{F_0} = 6 = mult(p_{F_1},c),
  St 3.17(i)) and 24 are conjugates of the same pole punctures — plus two
  extra orbits 2 × (5 × 3) = 30 series of g-finite punctures:
  60 = 30 + 30 ✓. Pole cluster: 6 directions above F_0, p_g coprime
  (AF3 §4's explicit p = η(η⁵−A), p_g = B(η¹⁰−(5/3)Aη⁵+(5/9)A²)): all
  pole, 0 cv mass. y-side cv mass: the two orbit clusters, (24)-price
  D/i − κ̄ = 15/3 − 4 = 1 each: exactly 1 + 1 = Σλ = 2 required. x-side:
  15 series, one cluster, κ_G = 1, π_G = 4: exactly 3. Total
  3 + 2 + 0 + 0 + 0 = 5 = td − 1. Balanced; NOTHING left to force.
- **SP-1 (slack 1)**: F_1 = (21,63,7,3,5), k_f = 63 = 42 (chain orbit,
  7×6) + 21 (one extra orbit, price 21/3 − 5 = 2); l_f = 21, R = 3,
  ψ = 2. Spends 2 + 2 = 4 ≤ 5: the free unit may sit in the x-side
  (κ_G(π_G−1) ∈ {2,3}, π_G ≥ 3), in a third y-side cv vertex above a
  cluster, or in δ — nothing pins it, nothing kills it.
- **SP-3/SP-4**: one extra λ-free IIa_0 (k=0) chain step below the SP-1/2
  node: single-orbit pattern, NO series leave (all conjugates), no new cv
  mass — ledger identical to SP-1/SP-2, s-uniformly.
- **Two-pole (residue A)**: both poles row 1, Q = (2,2,2,2,5), Λ = 3+3.
  L1a is re-derived by the ledger: pre-merge chain patterns are single
  simple orbits, so NO punctures leave pre-merge (zero y-side cv mass
  above G_m — λ = 0 structurally, matching L1 §2); at the merge
  G_m = (6,12,3,2,5) the resonant q-orbit direction b is not a root of
  p_{G_m}, carries NO punctures, hence NO cv vertex and NO budget charge —
  (22) confirms from the budget side why l ≥ 1 at the merge is invisible
  to every printed counting statement (L1 §3's blind spot, now exhibited
  as an empty ledger row rather than a missing lemma). Suffix as in
  single-pole: 2P-R3a through (42,126,7,3,5): k_f = 126 = 84 (chain,
  7×12) + 42 (orbit, price 42/6 − 5 = 2); l_f = 42, type (2,3),
  (k_g,l_g) = (189,63), R = 3 ✓ slack 1. R4 pair: k=2-type suffix
  (2 orbits × 1), R = 4, ψ = 3, slack 0 — rigid as SP-2.

## 5. Consequences

### 5a. The book stays 8; the A3L1 kill route is closed

The λ_root ≥ 1 lemma is DEAD as a kill: its content is empty on exactly
the survivor set (case-IV terminals), by the survivors' own terminal
hypothesis. SHEET6-CAMPAIGN header "next kills" should drop it; the
counterexample template is instead STRENGTHENED (5b). No class dies; no
class is resurrected; canonical book unchanged: td ≤ 5: 0; td = 6: 4
single-pole r9/M2 + two-pole residue A (4 IV classes).

### 5b. New forced rigidity (the ledger's positive product)

For EVERY one of the 8 (LR2): the x-side of a carrier is a single
Puiseux cluster — one cv vertex, κ_G = 1, no x-side splitting or
characteristic exponent below height R ≥ 3. This is a new, checkable
constraint feeding the coefficient-template lift (the campaign's other
endgame thread): any candidate (f,g) must have its ENTIRE x-side Newton
structure trivial to depth R.

For the 4 slack-0 classes additionally (every ledger row exact):
1. x-side: π_G = R exactly; both p- and g-patterns unsplit below R
   (full slopes l_f, l_g the whole way);
2. y-side: each priced orbit cluster carries exactly ONE cv vertex of
   mass exactly its (24)-price (e.g. SP-2: κ_H = 1, π_H = 2, twice);
   no further y-side cv vertex anywhere (pole clusters pure — forced;
   orbit subtrees unsplit below their cv vertices);
3. δ_a = 0 for EVERY a ∈ C: no fiber in the whole pencil may carry any
   g-finite puncture with Λ(P) > κ_{F̂_P}(π(F̂_P)−1) — total
   non-degeneracy of every direction family at every special value.

### 5c. The surviving attack surfaces (precise, none printed)

1. **δ-strictness at direction collisions.** The x-family's direction
   polynomial has degree deg p_G = l_f ≥ 15 (single-pole) at the cv
   vertex, so a* with mult(p_G − a*, c) ≥ 2 EXIST (critical values of a
   nonconstant polynomial). Prop 7.3 proves Λ-mass ≥ κπ−κ with equality
   iff mult = 1 but does NOT prove strictness at mult ≥ 2. A strict
   version (one extra unit of δ at some collision fiber) would kill all
   four slack-0 classes at once — this is the exact quantitative question
   the ledger isolates. Genuinely new mathematics (a local excess formula
   for Prop 7.4's δ); nothing in §7 decides it.
2. **x-side realizability vs the templates.** LR2's single-cluster/κ=1/
   unsplit-to-height-R x-side must coexist with the pinned y-side
   patterns (AF3 §4 entry family; L1 §5 rigid merge template) inside one
   polynomial pair of the given type. This is the same Puiseux-transport
   tier as L1 §7(ii), now with BOTH ends of the tree pinned.
3. **h₁-branch budget (unchanged, L1 §7(i))**: the (22)-ledger charges
   only g-critical-value vertices; h₁-branches at non-p directions remain
   outside every printed budget — confirmed here as a structural gap of
   the counting frame, not closable by re-partitioning (22).

## 6. Errata and reading notes banked

- **E10 (St 3.15, p. 17 — label swap)**: cases (i) and (iii) are
  interchanged as printed: d_{h,F} > 0 frozen gives |h| → ∞ (pole), and
  d_{h,F} < 0 gives h(P) = 0 — as the thesis's own usage has it
  everywhere (Prop 5.2's no-pole conclusion, Prop 5.3(ii) d_g > 0 AT pole
  vertices with the §5 title "The poles of g", Prop 7.3's proof computing
  Λ(P) = −κ_F d_{g−b,G} > 0 from d < 0 at a puncture where g − b → 0).
  With the printed labels, Prop 5.2/5.3/7.3 would all be false; with the
  swap, everything is consistent. Label-level; no downstream change (the
  campaign never used 3.15(i)/(iii), only (ii), which is reading-neutral).
- Reading note (St 9.5, p. 50): the printed sum starts at i = 1 (omitting
  λ_{F_0}) while its proof applies St 9.4 to all of F_0,…,F_n; as printed
  it is true but weaker than its own proof. The campaign's all-i charging
  is the proof's version. Not an erratum.
- Reading note (Not 7.1): T_a^0 is Not 3.14's {d_F = 0} — cv vertices lie
  on the d = 0 waterline. This makes "no cv vertex on the characteristic
  path" (§1 item 1) immediate and disjointness of ψ from every λ
  structural: E9's branch-at-F reading is thereby CONSISTENT with St
  9.4's proof for free (the charged sets live in T^0, the path in T^+).

## 7. Trust perimeter

Printed statements used: Def 3.2/3.3/3.4, St 3.3, Prop 3.1(∗)(∗∗),
St 3.9-3.13, St 3.15 (E10-corrected), St 3.16-3.18, Lemma 2.1, Thm 6.1,
Prop 5.1/5.3/5.8, Not 5.1/5.2, §7 complete (Not 7.1-7.3, St 7.1-7.3,
Prop 7.1-7.5, Cor 7.1), St 9.1/9.2/9.3(24)/9.4(25), Prop 9.2/9.3,
Prop 8.4's proof (descent). Standing campaign hypotheses inherited: H1
(Prop 9.3 arithmetic), H2 = E9 branch-at-F reading (load-bearing here, as
in every budget statement; adjudicated by A3L1 front 8), H4, AF2 minima
(for the y-side prices only — the REFUTATION does not need them: λ_root =
0 is reading-independent, §2). LR1 is hypothesis-free modulo H1's case
labels. LR2 uses (22) + integrality only. The §4 balance exhibits are
Q-level consistency statements (necessary conditions), same tier as every
campaign survivor.

## 8. Reproduction

    cd cases && python3 lroot_ledger.py      # ledger audit, all 8 classes,
                                             # exact arithmetic, asserts
    python3 sheet6_campaign.py gate          # unchanged: PASS
    python3 hiii_compose.py pin              # unchanged: td6 = 4 (r9/M2)
    python3 twopole_check.py l1only          # unchanged: A + 4 IV classes
