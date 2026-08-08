# SHEET6-2POLE.md — the two-pole (3,3) configuration at td = 6

Status: PROMOTED (2026-08-07, SHEET6-A2P-REVIEW.md: mathematical core
CONFIRMED on all fronts; three bookkeeping fixes applied — derived IIb
pricing now engine default, 95.6% histogram, §2d M_pole pin; survivor book
= residue A + 2 boundary classes). Target: SHEET6-CAMPAIGN.md §6 item 4,
the last structural gap of the td=6 program (single-pole side closed by
SHEET6-HIII-REVIEW.md: sanctioned residual 0). Ground truth read on-page:
papers/sigray_full.pdf (printed page = pdf page). Engine:
cases/twopole_check.py (new, additive; reuses sheet6_campaign.py step/cost
machinery read-only). Literature: papers/do.pdf (Domrina-Orevkov I),
SHEET6.md §Domrina, RECON.md.

VERDICT: **CONSISTENT-EXHIBIT (Q-level)** — the configuration is NOT
excluded; the budget obstruction fails structurally (min two-pole spend
is 0 through the merge, §5a); an explicit exhibit passing every located
printed constraint + the composed kill set exists and is hand-verified
(§6a): two row-1 poles first-step-merging into (D,deg p,ν,M,κ̄) =
(6,12,3,2,5), suffix to the St-9.7 shape (42,126,7,3,5), case-IV terminal
with R=3, Σλ = 2 <= 3 (slack 1). Root merges ARE excluded (§5b phase 3).
Residual book: 3 merge classes / 9 IV-classes, cap-stable; 2 survive even
the λ-root strengthening. Missing lemma for EXCLUDED: §6c (L1 merged-
pattern inadmissibility is the highest-value target — it would close the
whole book at once). Until then, td=6 exclusion is conditional on closing
THIS configuration, and §6a is the distinguished counterexample template.

## 1. Extraction: Prop 8.4 and where one-dicritical-ness enters

### 1a. Statement (p. 44, verbatim)

"Proposition 8.4. Let (f,g) be a normalized counterexample of the Jacobian
conjecture. Assume that T_{a,pole} = {G}. Then for any F in Ta& cap Va one
has M_F != 1."  The singleton hypothesis is EXPLICIT in the statement; it is
the only place in the printed thesis where the pole-vertex COUNT is used.

### 1b. Proof anatomy (pp. 44-45) and the exact entry point

The proof builds F_0 = F, F_{j+1} = F_j° down to F_n = (0,y), H := F_{n-1},
then: "From Proposition 8.3, and by induction we have M_H = 1", Bezout
(St 8.1) at H, transport of (k,l) to the root, k = 1, l = l_f/k_f in N,
contra Thm 6.1 (l_f < k_f). The singleton hypothesis is NEVER mentioned in
the proof body. It enters exactly once, silently, through Prop 8.3's
hypothesis (p. 44, verbatim): "Assume that for any H in Ta& cap (Va\{(0,y)})
one has G != H°" — as printed this contradicts G := F° (take H = F); the
coherent reading (= Notation 9.2's "G regular over F", p. 48) is: F is the
UNIQUE Ta&-Va-predecessor of G. The induction needs regularity at EVERY step.
Why singleton-pole => regularity: Prop 6.8 (p. 34, verbatim): every
F in Ta& with deg(p_F) != 1 lies under a pole vertex ("there exist P, v >= u
with I_P(v) in T_{a,pole}"). If some chain vertex G had two distinct
predecessors H != H' in Va cap Ta& (deg p >= 2 each, St 3.16), the two
disjoint subtrees above G would each contain a pole vertex (Prop 6.8), so
|T_{a,pole}| >= 2. Contrapositive: one pole => every ° step of every chain is
regular => Prop 8.3 applies inductively => Prop 8.4. Secondary uses of
regularity in the same proof: Prop 8.3(ii) gives the single-orbit root
pattern p_G = ⊖(η^ν−c^ν)^M, and 8.3(iii) gives p_{(0,y)} = (η−c)^k
(one root), which is what makes deg = mult at (0,y) in the k-computation.

### 1c. What survives with two poles: the merge trichotomy

Let T_{a,pole} = {P1, P2} (both row 1, §2). Both characteristic sequences
(Prop 9.2) are °-descents ending at (0,y); ° is deterministic, so they
coalesce at a unique meet G_m and share the suffix from G_m to (0,y).
Structure facts (all from printed statements):
- (i) G_m is NOT a pole vertex: Prop 5.3(v) (p. 25) makes p squarefree at
  pole vertices, while the incoming chain orbit has mult(p_{G_m}, c_i) =
  deg(p_{H_i}) >= 2 (St 3.17(i), p. 18; H_i in Va so deg p_{H_i} >= 2 by
  St 3.16). So each pre-merge segment has >= 1 edge (H_i = P_i allowed).
- (ii) Regularity fails EXACTLY at G_m (over both H_1, H_2) and nowhere
  else: a second regularity failure would manufacture a third pole via
  Prop 6.8. Two sub-cases: interior merge (G_m != (0,y), G_m in V_{2,a})
  or root merge (G_m = (0,y); then p_{(0,y)} has >= 2 roots, so (0,y) in
  V_{2,a} — (0,y) in V_{1,a} is impossible — and BOTH terminal steps are
  Prop 9.3 case (I), never case (IV): the case-IV hypothesis
  "F not in V_{1,a} cup V_{2,a}" fails).
- (iii) M=1 kill PARTIALLY RESTORED: for F on {G_m} cup (suffix), the
  descent from F is regular at every step and (0,y) is regular over the
  shared H := F_{n-1} (a second predecessor of any suffix vertex would be a
  third pole), so Prop 8.3's induction + the p. 45 Bezout run verbatim:
  M_F = 1 is contradictory ON THE SHARED SUFFIX AND AT G_m (interior case).
  Above G_m (pre-merge segments) the propagation stops at the non-regular
  step: M = 1 is NOT killable there. In the root-merge case 8.3(iii) fails
  at the last step (p_{(0,y)} has two roots, deg != mult), so no M=1 kill
  anywhere.

## 2. Configuration layer: what each pole inherits, what ties them

### 2a. Both poles are row 1 (pp. 27-28, 45-46)

Prop 5.8 (20) (p. 28): td = Σ_{F in T_{a,pole}} Λ(F), Λ(F) = D_{g,F}
deg(p_F)/ν_F. Prop 5.7 (p. 27): Λ(F) >= β for the global type (α,β).
Prop 9.1's proof line (p. 45): 1 < α < β <= 6, gcd(α,β) = 1. Two poles at
td = 6 force Λ = 3 + 3, so β <= 3, so (α,β) = (2,3) — the GLOBAL type of
(f,g) is pinned — and the only Λ=3 row of table (23) (p. 46) is row 1:
(D_F, D_{g,F}) = (2,3), (deg p_F, deg p_{g,F}) = (2,3), ν_F = 2. These are
ABSOLUTE degrees (no j-unit: Λ(F) = 3·2/2 = 3 exactly). St 9.1 (p. 48):
κ̄_F := κ_F(1−π(F)) = D_F + D_{g,F} = 5. So EACH pole enters the chain
calculus with the campaign's row-1 shape
    Q(P_i) = (D=2, deg p=2, ν=2, M_i, κ̄=5),  ρ_i = 1,   i = 1,2.
Per-pole facts inherited from §5: p_{P_i} squarefree, one ν-orbit
(Prop 5.3(v) + 5.4: p = η²−c², c != 0); every puncture above P_i has
g = ∞ (Prop 5.5), so λ_{P_i} = 0 automatically (St 7.2: cv-vertices never
share a puncture path with a pole; Not 9.3's Y(P_i) is empty).

### 2b. Global ties between the two poles

1. SHARED TYPE: one (α,β) = (2,3) for the single normalized pair (f,g)
   (Lemma 2.1, p. 8); both poles' multiplicity data refer to it (St 5.2).
2. SHARED TREE + MERGE CONSISTENCY: both chains live in ONE Eggers-Wall
   tree T_a and share the suffix below the meet G_m. At G_m the two
   incoming step equations (Prop 9.3 (b)-(d) per edge) must produce the
   SAME Q(G_m): with per-edge data (ρ_i, ν_i, κ̄_i, μ_i, n_i),
       κ̄(G_m) = (κ̄_1+n_1)/ν_1 = (κ̄_2+n_2)/ν_2 in N,
       D(G_m)  = (D_1+n_1 P_1)/ν_1 = (D_2+n_2 P_2)/ν_2,
       i(G_m)  = P_1/μ_1 = P_2/μ_2   (full mult of each orbit = i·μ_i =
                 P_i = deg p_{H_i}, St 3.17(i)),
   and p_{G_m} must contain BOTH incoming orbits: in reduced-pattern
   coordinates p = (η^ν−c_1^ν)^{μ_1}(η^ν−c_2^ν)^{μ_2}·Π_k. This
   two-equation consistency is the resultant-type relation tying the
   poles; it replaces "splice/linking data" in the Eggers-Wall frame.
3. SHARED BUDGET: St 9.4 (p. 49) applies to ANY pairwise-different
   F_1..F_n in Va cap Ta&, hence to the UNION of both chains (shared
   suffix counted once):
       Σ_{F in C_1 ∪ C_2} λ_F  <=  td − 1 − ψ  =  5 − ψ,   ψ >= 1,
   i.e. Σλ <= 4 SHARED, not per-pole. The ψ upgrade (SHEET6-H3 §4a /
   HIII-REVIEW §6 psi-at-root) also transports: ρ_root = l_f/k_f exactly,
   so ψ = ceil(k_f/l_f) − 1 at any root-termination, and k_f =
   deg(p_{(0,y)}) >= i_1μ_1 + i_2μ_2 (both arrival orbits) in the
   root-merge case.
4. NO OTHER PRINTED TIE: §§5-9 were swept for statements coupling two pole
   vertices; Prop 5.8/5.7, the shared tree/budget and Lemma 2.1's global
   normalization are the complete list. (Prop 7.5's Euler-characteristic
   identity (22) is the source of Cor 7.1 and is already counted in 3.)

### 2c. Entry M-menu without Prop 8.4

M_F := gcd(deg p_F, deg p_{h_j,F} family) (Not 8.1, p. 38). The campaign
menu (AF3) is M | gcd(D,P) = gcd(2,2) = 2, i.e. M in {1,2}. Single-pole
runs drop M=1 (Prop 8.4); here BOTH M_i in {1,2} are live at entry, and by
§1c(iii) M=1 nodes are killable only at/below the merge. St 8.4 (p. 42)
still pins the chain-orbit multiplicity per edge: μ_i | M_{G_i} at every
step, so M=1 ancestry forces μ=1 patterns (§4c).

### 2d. M_pole pin (added per SHEET6-A2P-REVIEW front 7)

Not 8.1 + Prop 5.1(iii) pin the pole entry multiplicity: M_{P_i} =
gcd(P, P_g) computed from the global (2,3)-type data; it is NOT a free
label from the §2c menu. Consequence: the residue-B entry labels (M = 2
at both poles with the §6 B-pattern) are inconsistent with the pin;
residue B dies at entry. Composed with the derived IIb pricing (A2P
fix 1), the true survivor book is residue A + the 2 boundary classes.

## 3. Literature analogue: Domrina-Orevkov's multi-dicritical split

Read: papers/do.pdf (intro + §2); SHEET6.md §history; Domrina II metadata
(mathnet im273). DO's stratification variable is the number of DICRITICAL
COMPONENTS of the resolution at infinity (components of L~ on which F is
non-constant with image not in L) — a finer/different count than Sigray's
T_{a,pole} vertices (Sigray's poles carry Λ >= β >= 3 each; DO dicriticals
carry >= 1 sheet each; at td=4 DO already faces multi-dicritical cases
while Sigray's frame allows two poles first at td=6). The ANALOGY is
structural, not an identification: in both frames the flagship kill is
proved under a uniqueness hypothesis (DO paper I, p. 1: "we prove a
particular case ... namely when f has ONE dicritical component. The
complete proof will appear in the next paper"; Sigray: Prop 8.4's
T_{a,pole} = {G}).

How DO actually handled the split at td = 4: NOT by transferring the
one-dicritical argument. Domrina's paper II ("Four-sheeted polynomial
mappings of C². II. The general case", Izv. Math. 64 (2000)) redoes the
whole case analysis over splice-diagram combinatorics (~19 configurations
-> 8 final diagrams, killed by unimodularity/negative-definiteness/
canonical-class arithmetic; SHEET6.md). Two lessons transfer:
1. The multi-dicritical case is a GENUINE separate enumeration, roughly
   the same size as the single case — matching what §§4-5 find here (a
   new merge-step calculus, not a corollary of Prop 8.4).
2. Their method has a PROVABLE ceiling (Orevkov's exotic-covering
   examples, minimal degree 9; Egorov's 5-sheet example killed the
   quasi-topological method at td=5 entirely) — so at td >= 5 the
   analytic layer (Abhyankar/Puiseux arithmetic = Sigray's engine, or the
   2008 proofs) is forced. There is NO ready-made multi-dicritical
   argument at td=5 to imitate: td <= 5 never needs one in Sigray's frame
   (3+3 > 5), and DO's td=4 multi-dicritical treatment is splice-diagram
   arithmetic with no Eggers-Wall translation on record. What would be
   td-specific input: the merge-vertex pattern lemma of §4a (two searrow
   orbits in one root polynomial) — no analogue exists in DO because
   their gluing is along divisor chains, not root polynomials.

## 4. The two-pole chain calculus (new lemma content)

Conventions as in the campaign engine (reduced patterns p,q of Prop 8.1;
child F = G°, parent G = F + c; St 8.2 (p. 41) is the searrow test at a
root c: G' := F + c in Ta& iff deg(q)·mult(p,c) > deg(p), northeast iff <).

### 4a. Merge-step patterns (hypothesis M-PAT, the H1/H4-extension)

At F = G_m both incoming directions are searrow, so p has TWO orbits
passing the St 8.2 test, plus k northeast extras (λ-charged via St 9.3 as
in AF2), i.e. per branch shape (ν := ν_F):
    IIa-like: dp = (μ_1+μ_2+k)ν,   dq = (k+2)ν + 1
    I-like  : dp = μ_1+μ_2+k,      dq = k+2          (ν = 1)
    IIb-like: dp = (μ_1+μ_2+k)ν+1, dq = (k+2)ν + 1
    III-like: dp = μ_1+μ_2+kν,     dq = 2 + kν
with each searrow orbit once in q (same per-root rule that puts the chain
orbit once in q in the thesis's own patterns — this extension of the
single-pole pattern zoo is flagged M-PAT; same trust tier as H1/H4).
Two ratio equations must hold simultaneously (one per edge, Prop 9.3(b)):
    dp/dq = μ_1(ρ_1+n_1)/(κ̄_1+n_1) = μ_2(ρ_2+n_2)/(κ̄_2+n_2),
n_i >= 1, n_i ≡ −κ̄_i mod ν_i, plus the §2b.2 consistency (same κ̄, D, i).
λ(merge) = k·max(1, ceil(D/i − κ̄)) — the OTHER chain's orbit is never
λ-charged (it is searrow: no cv vertex hangs there, St 9.3 needs
F + c in Ta%). The single-pole engine has no such step: its k extras are
all northeast and all charged. Searrow-orbit multiplicity floor: μ_i ≥ 1
with i·μ_i = deg p_{H_i} (full), and μ_i > dp/dq whenever dp > dq.

### 4b. Kill set for the two-pole BFS

- Pre-merge segments: NO M=1 kill (§1c(iii)); all other campaign kills
  (budget, no-applicable-case, loop closure) stand.
- Merge child: M(G_m) = gcd(dp, dq) (Prop 8.1(v)); if = 1 the §1c(iii)
  restored kill fires (interior merge) — KILLED.
- Suffix: full single-pole kill set (M=1, budget, H3q IV-dispositions of
  hiii_compose/h3_check) with the λ already spent by both pre-merge
  segments + merge.
- Root merge: terminal step is the I-like merge pattern with child
  (ν,κ̄,D) = (1, 1, l_f) (St 9.2), so κ̄_i + n_i = ν_i, i.e. BOTH parents
  need κ̄ < ν (the case-IV condition (j) reappears); ψ = ceil(k_f/l_f)−1
  with k_f = i(μ_1+μ_2+k)·[+ other roots], l_f = D_root.

### 4c. Two rigidity facts inside the calculus (exact)

1. μ = 1 chains are λ-free but IIa_0-only: with μ = 1 the searrow test
   for the chain orbit reads dq > dp, while a northeast extra needs
   dq < dp — so k = 0 and the only admissible shapes are IIa_0-like
   (dp = ν, dq = (l+1)ν+1), λ = 0. (I/IIb/III-like shapes force
   dp/dq = 1 = ratio, impossible since ρ < κ̄.) Consequence: M=1 ancestry
   (μ=1 forced, §2c) descends λ-free — the budget CANNOT kill M=1
   pre-merge segments; only the merge-time M-kill (§4b) can.
2. Root-merge ratio rigidity at μ_1 = μ_2 = 1: the I-like merged ratio is
   (2+k)/(k+2) = 1 — impossible. So two M=1 chains can never terminate
   together at (0,y); an M=1 chain must merge INTO an interior vertex.
   Root merges need μ_1 + μ_2 + k > k + 2, i.e. some μ_i >= 2, i.e. at
   least one chain arrives with M >= 2 at a κ̄ < ν vertex.

## 5. Budget arithmetic and engine runs (cases/twopole_check.py)

### 5a. The obstruction attack FAILS: minimum spend is 0, not > 4

Per-pole pre-merge minimum: 0 (λ_{pole} = 0 automatically, §2a; H_i = P_i
allowed, §1c(i): the chains may merge at the FIRST step). Merge minimum: 0
(k = 0 merged patterns carry no northeast extras; the other chain's orbit
is searrow and never λ-charged, §4a). So min(Σλ) = 0 + 0 + 0 + suffix, and
the shared budget Σλ <= 4 (§2b.3) kills nothing a priori. The arithmetic
reason the single-pole engine's μ=1 auto-kill (M_F = gcd(ν, (l+1)ν+1) = 1)
fails here: at a merge vertex the second orbit doubles the p-degree,
M(G_m) = gcd(2ν, (l+2)ν+1) = 2 for ν odd, l odd — the M=1 cascade that
disposes of every μ=1 branch in the single-pole bash is broken exactly at
V_{2,a} vertices. This is THE mechanism by which the two-pole configuration
escapes the machine.

### 5b. Engine phases and results (exact; caps in file header)

Phase 1 (pre-merge BFS, M=1 kill OFF, μ=1 IIa_0 + μ=2 I/IIb/III children
added): 163 reachable shapes at λ<=4 (228 at raised caps) incl. the λ-free
μ=1/M=1 trees; 5 OPEN case-III branch kinds inherited from the campaign's
III-tail limitation (flagged; all on parametric λ0/λ2+ nodes). Min λ for an
M>=2, κ̄<ν (IV/root-capable) shape: 3.

Phase 2 (interior merges, hyp M-PAT + per-edge Prop 9.3(b)-(d), doc §4a;
suffix = composed single-pole engine with restored M=1 kill, N1, E5-III,
H3q IV dispositions): 52 389 merge children solved (216 390 at raised
caps); kill histogram: 95.6% M=1-at-merge (restored Prop 8.4; percentage
corrected per SHEET6-A2P-REVIEW), 2.6% suffix DEAD, 0.6% N1. RESIDUE under
the DERIVED IIb pricing (now the engine default, A2P fix 1): **2 (child,Σλ)
residue classes + 6 IV classes** (the legacy-priced 3+9 book in §6 is
superseded; A′ repriced out, B halved — and B dies at entry under the §2d
M_pole pin, leaving A + 2 boundary classes as the true survivor set).

Phase 3 (root merges = meet at (0,y)): ZERO solutions, two independent
structural grounds: (i) any edge with μ_i = 1 fails the St 8.2 searrow
test at an I-like root pattern (μ_i·(k+2) > μ_1+μ_2+k forces μ_i >= 2 −
k/(k+2) > 1), and μ_1 = μ_2 = 1 forces ratio (2+k)/(k+2) = 1, impossible
(§4c.2); (ii) (μ_1,μ_2) >= (2,2) needs both parents M>=2 with κ̄ < ν,
whose min combined pre-merge cost is 3+3 = 6 > 4 >= 5−ψ. So a two-pole
counterexample MUST merge at an interior vertex of V_{2,a} and terminate
through the shared suffix. (Engine confirms: 0 solutions at both cap
levels even before budget filtering.)

## 6. Outcome: CONSISTENT-EXHIBIT (Q-level), the distinguished target

### 6a. The exhibit (hand-verified exact; every datum ABSOLUTE, no j-unit)

    P1 = P2 :  Q = (D, deg p, ν, M, κ̄) = (2, 2, 2, 2, 5)      λ = 0 each
       |            (row 1 of (23); p = η²−c_i², type (2,3))
       | merged case-II step (hyp M-PAT), μ=(1,1), n=(5,5), λ=0:
       |   p_{G_m} ⊃ (η³−c₁³)(η³−c₂³)   [dp=6]
       |   q_{G_m} ⊃ η(η³−c₁³)(η³−c₂³)(η³−e³)   [dq=10, l=1 resonant orbit]
       |   ratio 6/10 = 1·(1+5)/(5+5) both edges; searrow: 10 > 6 both
       v
    G_m :  Q = (6, 12, 3, 2, 5)   [κ̄=(5+5)/2, D=(2+5·2)/2·(2/1), M=gcd(6,10)=2]
       |     merge = FIRST step of both chains; i₀ = P_i/μ_i = 2 both edges
       |     (i-consistency REALIZED absolutely — no unchecked P-caveat);
       |     mult(p_{G_m}, c_i) = i₀μ_i = 2 = deg p_{P_i}  (St 3.17(i))
       | single-pole suffix step, μ=2, IIa k=1 (n₀=1, m=3, n=10), λ=2:
       |   dp/dq = 21/15 = 2(1/2+10)/(5+10)
       v
    F  :  Q = (42, 126, 7, 3, 5)      [the St 9.7 hypothesis shape, Σλ = 2]
       | terminal, Prop 9.3 case IV:
       |   (j) 5 < 7; (k) d_F = (42+2·126)/7 = 42 ∈ N; (l) 42 < 126, R = 3;
       |   (m) 42·3/126 = 1 ∈ N*.
       v
    (0,y):  d = l_f = 42, k_f = deg p_{(0,y)} = 126 (single root);
            (k_g, l_g) = (3/2)(126, 42) = (189, 63) ∈ N²  [type (2,3)];
            l_f < k_f (Thm 6.1) ✓; k_g/k_f = 3/2 ∉ N* (Lemma 2.1(iv)) ✓;
            ψ = ceil(k_f/l_f) − 1 = 2;  St 9.4(25): Σλ = 2 ≤ 6−1−2 = 3 ✓
            — SLACK 1: robust even under a λ_{(0,y)} >= 1 strengthening.

No printed statement of the thesis located in this audit (or in
SHEET6-H3/HIII's sweeps) is violated. Same necessary-condition tier as
the campaign's other survivors: unchecked = Puiseux realizability
(St 3.16/3.18 side conditions, H4), h-family realizability, AF2 λ-minima,
plus the new M-PAT (merged-pattern shape rule, §4a).

### 6b. The full residue book (cap-stable at 2 cap levels)

3 merge-residue classes; 9 IV-survivor (shape,Σλ) classes on them:
- A: G_m = (1/2,3,2,5)@Σλ0 (the exhibit): (1/3,7,3,5)@2 R3,
  (2/3,3s+2,3,2s+2)@2 R3, (1/4,5,4,4)@2 R4, (3/4,4s+3,4,3s+3)@2 R4.
- A': same child @Σλ1 (asymmetric parent (1,3,1,7)@1): the two R3 shapes
  at Σλ=3.
- B: G_m = (1/5,6,5,5)@Σλ1 via μ=(2,2), k=1, l=1 (dp/dq=30/25, M_m=5):
  itself IV @1 R5, (4/5,5s+4,5,4s+4)@1 R5, (1/3,4,3,3)@3 R3,
  (2/3,3s+2,3,2s+2)@3 R3.
Under the λ_{(0,y)} >= 1 strengthening (HIII-REVIEW §5 candidate (b)),
the boundary classes die and the book narrows to the 2 slack-1 classes of
residue A — both R = 3, both on the λ=0 first-step merge child.

### 6c. What is missing for EXCLUDED (the precise lemma alternatives)

Any ONE of the following closes the two-pole configuration:
- (L1) MERGED-PATTERN INADMISSIBILITY: at a V_{2,a} merge vertex with two
  simple searrow orbits (μ=(1,1)), the resonant q-orbit family l >= 1 is
  impossible (l = 0 gives M(G_m) = gcd(2ν, 2ν+1) = 1, killed by restored
  8.4; the exhibit needs exactly l = 1). Nature: Puiseux/ODE analysis of
  Prop 8.1(iv) at two-orbit patterns — thesis §3-level work, the M-PAT
  zone. This would kill residues A, A' AND B (B uses l=1 too): the whole
  book. HIGHEST-VALUE TARGET.
- (L2) TWO-POLE M-OBSTRUCTION: a Prop 8.4 analogue transporting Bezout
  data from BOTH branches through G_m (St 8.3 holds edge-wise with no M=1
  hypothesis; the merged h-family at G_m sees gcd of both sides). Would
  need to contradict M(G_m) = 2 with M=1-ancestry on both edges. Genuine
  new mathematics; no printed template.
- (L3) λ-charge at merge vertices: show a merge vertex forces a cv vertex
  (λ(G_m) >= 1) — e.g. via δ_a > 0 (Prop 7.4) at non-generic a. Would
  push residue A to Σλ=3 (still <= 3: NOT sufficient alone for the R3
  classes; kills only the boundary book). Weakest.

## 7. Consequences for the td=6 theorem statement

1. The composed HIII headline "td=6 sanctioned residual = 0" is a
   SINGLE-POLE statement. With the configuration layer included, the
   correct current statement is: **td(f,g) = 6 is excluded conditional on
   {H1, H2, H4, AF2, AF3, H5a/b, H3q} EXCEPT on the two-pole (3,3)
   configuration, where the residual book is §6b** (2 robust + 7 boundary
   IV-classes, all pinned with exact Q-data). No unconditional td=6
   theorem can be claimed until L1/L2 (or a counterexample) resolves it.
2. The thesis's printed td>=6 proof (St 9.12 + G1-G3 as repaired) is
   silent on the two-pole configuration entirely: Prop 5.8's (20) makes
   the 3+3 split explicit, Prop 8.4 excludes it from its own hypotheses,
   and no §9 statement addresses a second pole. This is a FOURTH
   structural gap (beyond G2/G3/E2-E4) in the printed td=6 claim — and
   unlike G2 it is not repairable from printed statements located so far.
3. Counterexample search guidance (the "distinguished place"): a td=6
   counterexample compatible with all current knowledge must have TWO
   g-pole branches at infinity of local degree 3 each (type (2,3),
   row-1 data), whose Eggers-Wall chains merge IMMEDIATELY (first °-step)
   at a V_{2,a} vertex with data (D, deg p, ν, M, κ̄) = (6, 12, 3, 2, 5)
   [or the (1/5,6,5,5)-child variant], then run the §6a suffix. Root
   merges are impossible (§5b phase 3). Any Puiseux-data search should
   start from exactly this template.
4. Domrina-Orevkov parallel (§3): as at td=4, the multi-dicritical/
   multi-pole case is a separate enumeration of comparable size, not a
   corollary — but here it is also where the exclusion currently FAILS,
   which is consistent with the historical pattern that uniqueness-of-
   dicritical is the load-bearing simplification in every generation of
   these proofs.

## 8. Trust perimeter and limitations

- Everything is Q-level necessary-condition arithmetic (campaign tier):
  H1 (Prop 9.3 (a)-(m)), H2 (kill set incl. Y-disjointness in St 9.4),
  H4 (patterns/regularity for SINGLE-pole steps), AF2 (λ-rule), AF3
  (entry menu, here {1,2}), H5a/b (E5-III in the suffix), H3q (IV
  dispositions) — plus NEW: M-PAT (§4a merged shapes; per-root rules
  mirrored from the thesis's own patterns; flagged, unproven).
- Engine caps (all runs cap-clean, residues stable when caps raised
  ~2x): family params s,t <= 5..7, depth 6..7, merge ν <= 48/96, k <= 4
  (λ > 4 kill), l <= 4/8, μ=1-child ν_F <= 24/36. The 5 pre-merge OPEN
  case-III branches (§5b) are the same III-tail debt as campaign §6
  item 2-3 and could only ADD merge parents (all M=1-descended; their
  merges fall in the already-analyzed μ=(1,1) family).
- Not modeled: π-positivity along chains (H1 tier), absolute-degree
  realizability for ASYMMETRIC merges (residue A' only; A and B are
  symmetric with i₀ = 2 realized), λ_{(0,y)} contributions (would
  narrow the book to residue A's 2 classes, §6b).

## 9. Reproduction

    cd cases && python3 twopole_check.py     # ~3 min, exact arithmetic
    # phase 1: 163 shapes; phase 2: 52389 merges -> 3 residue classes
    # (kill histogram: 50097 restored-8.4 / 1373 suffix-dead / 336 N1);
    # phase 3: 0 root merges. Raised-caps stability run: see SHEET6-2POLE
    # session log (216390 merges, same 3 classes).
