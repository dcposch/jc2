Status: PROVED for the nonroot chain-depth closure and the all-`M=1`
root-meet layer, with the corrected case-I proof below. Mixed-`mu`/off-axis
root completeness is outside this theorem. Historical 2026-08-12 status:
SHEET6-DEPTH-REVIEW confirmed the then-filed package with one `d0` fix.

# SHEET6-DEPTH.md — the Chain-Depth Closure Lemma: the M=1 jump-cell menu is depth-invariant

> **2026-08-28 ROOT-SCOPE REPAIR.** A genuine root merge has contact zero,
> hence `(0,y) in V_{2,a} \ V_{1,a}` and Proposition 9.3 case (I), not case
> (IV). The prior rollback stopped too early: at a root case-I edge,
> equations (c),(d), Proposition 8.1(i), Statement 3.17 and Statement 9.2
> give `X_root=mu(1-w)`, so every such edge still requires `w<1`. For an
> all-`mu=1`, `r`-way root meet with reduced degrees `(r,r+l)`, `l>=1`,
> top-degree cancellation in Proposition 8.1(iv) gives
> `w=l/(r+l) in (0,1)`. Thus `td=6,m=2`, whose reviewed alphabet is
> `W={2}`, has no all-`M=1` root meet. This does not restore a root clause
> in Proposition 8.4: root `M=1` is legal and the local `r=2,l=1`, `w=1/3`
> cell is real. The old engine's omitted `l>=1`, silently capped MU1
> families, and root-before-`M=1` ordering remain genuine software errors;
> AWS recensus is diagnostic for the broader SF1/mixed-root scope, not a
> dependency of this analytic exclusion. Evidence: producer `b8d6e686...`,
> GPT-5.5 hostile review `656c257e...`, integration `d534f083...`.

**Historical status: PROVED (2026-08-12), H1 tier (Prop 9.3 printed-step arithmetic) over
the then-promoted MP package; machine-verified (cases/depth_closure_check.py, 13/13
exact checks). It then claimed that the demoted "finite book per (m, td)" rider of
Theorem MP (SHEET6-MULTIPOLE.md §0/§5; demotion SHEET6-MP-REVIEW.md Front 5)
was restored in corrected, sharper form (§8); the root-scope repair above
retains its all-`M=1` root layer while leaving mixed-`mu`/off-axis roots out
of scope. Two engine-model corrections
found en route: the ZCH 0-edge is Prop 9.3 case (III), not (a)–(d) (§5c),
and the historical case-(IV) root label is false for a genuine merge; the
correct case-I identity is filed in §5d.**

Ground truth: refs/sigray_full.pdf (printed page = pdf page), re-read
on-page this session: Def 3.1/3.2, St 3.1–3.2 (p. 10); Def 3.3–3.4,
Not 3.1–3.2, St 3.3 (p. 11); Not 3.3–3.8, St 3.4–3.6 (pp. 12–13); Not
3.9–3.11, St 3.7 (p. 13); Prop 3.1, Not 3.12, St 3.8 (p. 14); St 3.9
(p. 15); St 3.16, Prop 3.2, St 3.17 (pp. 17–18); Prop 5.3(iv)–(v) (p. 25);
St 5.2, Props 5.5–5.6 (pp. 26–27); Props 5.7–5.8, Def 5.1 (pp. 27–28);
Prop 8.1 (pp. 39–41); St 8.2/8.4 (pp. 41–42); Not 9.1, St 9.1–9.2 (p. 48);
Prop 9.2, Prop 9.3 (pp. 50–51); St 9.6 + proof (pp. 51–52). Promoted
priors: SHEET6-MULTIPOLE.md (MP0–MP9, Theorem O), SHEET6-MP-REVIEW.md
(esp. §5a/§5c), SHEET6-2POLE.md, SHEET6-L1.md. Engine cross-checked:
cases/twopole_check.py phase 4.

---

## 0. Verdict in one paragraph

The M=1 pre-merge chain step conserves a single rational invariant. Write
each chain frame in the i-normalized coordinates ρ := D_F/deg(p_F) (full
pattern degree) and set **w_F := (κ̄_F − ρ_F)/ν_F** with κ̄ := κ_F(1−π(F)).
Then (i) every M=1 segment vertex is a *Puiseux characteristic vertex* of
its own pole's series, with ν ≥ 2, and every chain edge is Prop 9.3 case
(II) (§2); (ii) the chain step multiplies w by n/Δ, Δ := (n−1)ν_child + 1,
where (ν_child, n) is the child's single-orbit pattern — so the infinite
"l = 0" direction (n = 1) that makes depth unbounded **fixes w**, while
every resonant step (n ≥ 2) requires Δ | num(w) and contracts w by a factor
≤ 2/3 (§3–4); (iii) the entire jump-cell layer factors through w: for every
μ = 1 edge into a merge, **κ̄_merge − D_merge/i = w** (the handshake), the
merged-child data is (κ̄, D/i, ρ) = w·(dq, dp, 1)/(dq−dp), the join forces
all arriving chains to share w, and per w the admissible cells are finite
with ν_cell *determined* by (κ̄_merge, l) (§5). Hence the set of w-values
over all depths is the finite computable closure W(w₀), and the map
(segment depth) → (reachable jump-cell menu) stabilizes by the proved safe
bound d₀ ≤ 2·gen(W)+2; the sharper `gen(W)+2` remains empirical in general.
Thus the map is
**constant beyond d₀**: DEPTH-INVARIANCE (Lemma, §6). For the nonroot jump
layer at td = 6, m = 2:
W = {2}, d₀ = 2, and the menu is *exactly* the promoted residue cell
IIa (r,ν,l) = (2,3,1), M = 2, child (κ̄, D/i) = (5,3) — i.e. Q =
(6,12,3,2,5) — reproducing the 351/351 empirical nonroot
depth-invariance. Every all-`M=1` root meet instead requires
`w=l/(r+l)<1`, so that root layer is empty at `td=6`. This statement does
not cover mixed-`mu`/off-axis roots or exclude the interior residue cell.

---

## 1. Setting and normalization

Notation as in SHEET6-MULTIPOLE.md §1. Fix a pole P_i ∈ T_{a,pole} with
entry datum (a_i, b_i, ν_i) of type (α,β) (MP4: Q(P_i) = (a_iα, b_iα, ν_i,
b_i, a_i(α+β)), St 5.2 + Not 8.1 + St 9.1 pp. 26/39/48). An **M=1 segment**
is a maximal run F_0 → F_1 → … → F_d of the characteristic sequence
(Prop 9.2, p. 50) with M ≡ 1, starting at the pole vertex (b_i = 1, forced
at β-minimal and prime Λ_i by MP4) or at an M=1-emitting merge child, and
ending at the last vertex before a merge vertex G (r(G) ≥ 2) or before
(0,y). By MP5, every F_j with j ≥ 1 has reduced pattern a single simple
ν-orbit: (dp, dq) = (ν_j, n_jν_j + 1), n_j ≥ 1, M = 1, λ = 0.

Frames are taken **i-normalized** ("shape space" of the engines, P-free):

- Q-datum (Not 9.1, p. 48): Q(F) = (D_F, deg(p_F), ν_F, M_F, κ̄_F),
  κ̄_F := κ_F(1−π(F)).
- ρ_F := D_F/deg(p_F) with deg(p_F) the FULL f-pattern degree (Not 3.10/
  3.13, pp. 13/16); by Prop 8.1(i) (p. 40) p_full = ⊖(ξ^δ p_red)^i, so
  deg(p_F) = i_F·deg(p_red) and ρ_F = (D_F/i_F)/deg(p_red).
- **w_F := (κ̄_F − ρ_F)/ν_F.**

ρ < κ̄ at every segment vertex (St 8.2, p. 41: deg q > deg p at μ = 1
arrivals, and dp/dq = i-normalized slope ratio, Prop 9.3(b)), so w > 0.

Equal-quotient transport (used throughout): for any edge F = G + c
(F above G; Prop 3.2/St 3.17(i), pp. 17–18), deg(p_F) = mult(p_G, c) =
i_G·mult(p_G^red, c) = i_G·μ_e, and μ_e | M_F = 1 by St 8.4 (p. 42) on M=1
ancestry, so **deg(p_parent) = i_child** on every segment edge and every
all-μ=1 merge edge. This is MP6(b) read at chain edges; it is what makes
the (b)-equation of Prop 9.3 close in the ρ-coordinate.

---

## 2. DS1 (characteristic rigidity): every segment vertex is a V_{1,a} characteristic vertex of its own pole, and every chain edge is Prop 9.3 case (II)

**Claim.** For 1 ≤ j ≤ d: (a) ν_j ≥ 2 and the orbit base c ≠ 0; (b)
F_j ∈ V_{1,a}; (c) κ̄_{F_j} ∈ ℤ; (d) π(F_j) is a characteristic exponent of
P_i's own Puiseux series, the segment vertices are *consecutive*
characteristic vertices I_{P_i}(α_s), and each edge F_{j-1} → F_j is case
(II) of Prop 9.3 (p. 50), so its (a)–(d) equations hold verbatim.

*Proof.* (a) F_j ∈ V_a ∩ Ta& \ {(0,x),(0,y)} (MP0), and St 3.16 (p. 17) is
an iff: p_{F_j} has more than one root. The single simple ν-orbit has root
set {ζc : ζ^ν = 1} — more than one root forces ν ≥ 2 and c ≠ 0. (This is
the thesis's own step: St 9.6's proof, p. 52, "by Statements 3.16 and 3.18
one has p(η) = ⊖(η^ν − c^ν) for some ν = ν_F".)

(b) Not 3.4 (p. 12): ν_F := 1 unless F ∈ V_{1,a}; so ν_j ≥ 2 ⟹ F_j ∈
V_{1,a}, i.e. F_j = I_{P′}(α′_{j′}) at a characteristic value of some
P′ ∈ R̄_a\R_a (Def 3.4, p. 11), with ν_j = e′_{j′−1}/e′_{j′} ≥ 2 strictly
(Def 3.1(ii), p. 10: e_i = gcd(e_{i−1}, β_i) < e_{i−1}).

(c) Not 3.5 (p. 12): κ_{F_j} = κ′/e′_{j′} and π(F_j) = β′_{j′}/κ′ with
e′_{j′} | β′_{j′} (Def 3.1(ii)), so κ_{F_j}π(F_j) = β′_{j′}/e′_{j′} ∈ ℤ and
κ̄_{F_j} ∈ ℤ.

(d) P_i's branch passes through F_j, so its series coefficient at the
exponent u := π(F_j) is a root of p_{F_j} (Prop 3.1(**), p. 14: pattern
roots = continuation coefficients of the fiber branches). By (a) the root
set contains no 0, so c_u(P_i) ≠ 0. Since F_j = I_{P′}(α′_{j′}), the series
P′ and P_i agree strictly below u (Def 3.3, p. 11: u ≤ O(P_i, P′)), so
they generate the same exponent lattice L below u; u ∉ L because β′_{j′}
is not divisible by e′_{j′−1} (Def 3.1(i)). A nonzero coefficient of P_i
at an exponent outside its running lattice is, by Def 3.1(i), exactly the
next characteristic exponent of P_i: u = α_s(P_i) for some s. Every V_a
vertex on I_{P_i}([0, π(P_i-vertex)]) is enumerated by the descent (Not
3.3, p. 12), every characteristic value of P_i is a V_a vertex (Def 3.4),
and every segment vertex is characteristic by the above — so consecutive
segment vertices sit at consecutive characteristic exponents of P_i. The
edge F_{j−1} → F_j then has parent at α_s(P_i), child at α_{s−1}(P_i):
with P = P_i this is literally case (II) of Prop 9.3 ("F ∈ V_{1,a} and
u = α_{j−1}"), and the case-(I)/(II) equations (a)–(d) apply. ∎

**Remarks.** (R1) The depth of an M=1 segment below its pole vertex is
therefore at most the number m_i of characteristic exponents of P_i, so
Π_j ν_j ≤ e_0 = κ_i and d ≤ log₂ κ_i. This is finite for every actual
(f,g) but κ_i is NOT bounded by (m, td) — td is the topological degree
(Def 5.1, p. 28), which does not control the Puiseux denominator at
infinity. This is the honest reason a depth CAP (option (a)) is
unavailable and depth-invariance is the right statement. (R2) The
phase-4 "zch chain children" of cases/twopole_check.py (ν_F = 1, p = η^i)
have a single distinct root, hence are NOT V_a vertices (St 3.16 iff) —
engine over-generation, harmless there (they produced no residue and, by
§3 R3 below, they conserve w anyway).

---

## 3. DS2 (the orbit map and its conserved quantity)

**Claim.** Let G → F be a segment edge (G = parent, F = G° single simple
(ν_F, n_Fν_F+1)-orbit, μ = 1). Then, with Δ_F := (n_F−1)ν_F + 1 = dq−dp:

    t     := (κ̄_G − ρ_G)/Δ_F        [edge scale]
    n_e   =  t·ν_F − ρ_G  ∈ ℕ*       [Prop 9.3(a)-(b) edge parameter]
    κ̄_F  =  (κ̄_G + n_e)/ν_G = t·dq_F/ν_G = w_G·dq_F/Δ_F
    ρ_F   =  t/ν_G,      κ̄_F = ρ_F·dq_F
    w_F   =  w_G · n_F/Δ_F.

In particular: **n_F = 1 ("l = 0" step, the unbounded direction) fixes
w_F = w_G for every admissible ν_F; n_F ≥ 2 ("resonant" step) contracts
w_F ≤ (2/3)·w_G** (since ν_F ≥ 2 gives Δ_F ≥ 2n_F − 1).

*Proof.* Case (II) applies (DS1(d)). Prop 9.3(b) (p. 50), i-normalized by
deg(p_G) = i_F (§1, μ_e = 1): dp_F/dq_F = (ρ_G + n_e)/(κ̄_G + n_e). Both
sides in lowest terms (gcd(ν_F, n_Fν_F+1) = 1), so ρ_G + n_e = tν_F and
κ̄_G + n_e = t·dq_F with t = (κ̄_G − ρ_G)/(dq_F − dp_F) = w_Gν_G/Δ_F.
Prop 9.3(d): κ̄_F = (κ̄_G + n_e)/ν_G = t·dq_F/ν_G. Prop 9.3(c) with
deg(p_F) = deg(p_G)·ν_F = i_Fν_F: ρ_F = (ρ_G + n_e)/(ν_Gν_F) = t/ν_G.
Then w_F = (κ̄_F − ρ_F)/ν_F = t(dq_F − 1)/(ν_Gν_F) = t·n_F/ν_G =
w_G·n_F/Δ_F. Contraction: n_F/Δ_F = n_F/((n_F−1)ν_F+1) ≤ n_F/(2n_F−1)
≤ 2/3 for n_F, ν_F ≥ 2. ∎

**Remarks.** (R3) Robustness: a hypothetical ν_F = 1 step has Δ = n_F, so
w_F = w_G for ALL n_F — the conservation does not even need DS1's
exclusion of such steps (they conserve w trivially; DS1 is what grounds
the case-(II) equations). (R4) The identity κ̄_F = ρ_F·dq_F means every
post-entry frame satisfies κ̄ = ρ·(own dq); equivalently ρ = w/n and
κ̄ = w(nν+1)/n: the frame is coded by (w, ν, n). (R5) The printed record
itself displays the conservation: St 9.6(v) (p. 51), the thesis's own
λ = 0 suffix family Q = ((6s+3)j, (4s+2)j, 2s+1, 2, 3s+3), has w ≡ 3/2
for every s (machine check 5).

---

## 4. DS3 (the resonance budget: finitely many w-values)

**Claim.** Write w_G = a/b in lowest terms. A resonant step (n_F ≥ 2)
requires **Δ_F | a**; consequently ν_F ≤ a − 1, n_F ≤ (a+1)/2, there are
at most as many resonant options as factorizations Δ − 1 = (n−1)ν with
Δ | a, and num(w_F) ≤ (2/3)·a. Hence along ANY segment, of ANY depth, the
number of resonant steps is < log_{3/2} num(w_0) + 1, and the set of
w-values reachable from w_0 (over all depths) lies in the finite,
explicitly computable closure

    W(w_0) := closure of {w_0} under w ↦ w·n/Δ,  Δ | num(w), Δ ≥ 3,
              Δ = (n−1)ν + 1, n ≥ 2, ν ≥ 2.

*Proof.* κ̄_F ∈ ℤ (DS1(c)) and κ̄_F = t·dq_F/ν_G = w_G·dq_F/Δ_F =
a·dq_F/(bΔ_F). Now gcd(Δ_F, dq_F) = gcd(Δ_F, dq_F − Δ_F) = gcd(Δ_F, ν_F)
= gcd((n_F−1)ν_F + 1, ν_F) = 1, so bΔ_F | a·dq_F forces Δ_F | a. Then
Δ_F ≥ ν_F + 1 and Δ_F ≥ 2n_F − 1 give the ranges, and num(w_F) divides
a·n_F/Δ_F ≤ (2/3)a. A strictly decreasing chain of positive integers
contracting by ≥ 1/3 per step has length < log_{3/2}(a_0) + 1. W(w_0) is
finite because each generation divides-and-contracts the numerator. ∎

**Entry values.** w_0 = (a_i(α+β) − a_i/b_i)/ν_i = a_i(b_i(α+β)−1)/(b_iν_i)
(MP4 entry pin); on the M=1 axis b_i = 1: w_0 = a_i(α+β−1)/ν_i. Λ_i =
a_ib_iαβ/ν_i ≤ td and mβ ≤ td bound a_i, α, β, ν_i, so num(w_0) ≤ td²/2
crudely; everything downstream is computable per (m, td). At td = 6:
w_0 = 1·(2+3−1)/2 = 2, and W(2) = {2} — no divisor Δ ≥ 3 of 2 exists, so
**no resonant step is admissible at all** (machine check 2).

---

## 5. DS4 (the jump-cell menu factors through w)

Let G be a merge with arriving all-μ=1 edges from last-segment vertices
H_e, and let (dp_c, dq_c) be the merged reduced pattern (MP6(d) menu:
IIa (rν, (r+l)ν+1); ZCH ((r−1)ν+1, (r−1+l)ν+1); I (r, r+l)),
Δ_c := dq_c − dp_c.

### 5a. The handshake

For every μ_e = 1 edge governed by the case-(I)/(II) equations:

    κ̄_G = (κ̄_e + n_e)/ν_e,   D_G/i := μ_e(ρ_e + n_e)/ν_e = (ρ_e + n_e)/ν_e
    ⟹  **κ̄_G − D_G/i = (κ̄_e − ρ_e)/ν_e = w_e.**

One line, cell-independent. Consequences: (i) the join condition (common
(κ̄_G, D/i) across edges, SHEET6-MP-REVIEW §5c layer J) forces **all
arriving chains to carry the same w**; (ii) solving the edge equation
against the cell exactly as in §3 gives

    κ̄_G = w·dq_c/Δ_c,   D_G/i = w·dp_c/Δ_c,   ρ_G = w/Δ_c,

so the **entire merged-child datum depends only on (w, cell)** — not on
the segment depth, not on (ν_e, n_e, κ̄_e) separately. (The per-edge
admissibility n_e ∈ ℕ*, n_e ≡ −κ̄_e (mod ν_e) does depend on the state
(w, ν_e, n_e); see §6 for why this does not spoil stabilization.)

### 5b. Cells are finite per w

For jump cells (l ≥ 1, MP7) one has dq_c ≤ (r+1)Δ_c in all three families
(elementary: e.g. IIa: (r+1)(lν+1) − ((r+l)ν+1) = r(lν+1−ν) ≥ 0), so
**w < κ̄_G ≤ (r+1)w, κ̄_G ∈ ℤ**. Fixing κ̄_G in this finite window and
setting Di := κ̄_G − w:

- IIa: ν(wr − Di·l) = Di ⟹ ν determined per l < wr/Di;
- ZCH: ν(l·Di − w(r−1)) = w ⟹ ν determined per l ≤ wr/Di;
- I: l = wr/Di (ν = 1).

Finitely many (family, ν, l, M = gcd) per (w, r ≤ m) — the SHEET6-MP-REVIEW
§5a per-frame finiteness, now *uniform in depth*. Cascade cells (l = 0,
M = 1 emission) are the infinite ν-family, but their child is again an
M=1 segment entry with **w_child = w·(r+l)/(lν+1)** (= r·w at l = 0),
ν-independent at l = 0; with MP1's Σ(r−1) = m−1 the composed closure
multiplies at most m−1 such factors — still a finite computable w-set.

### 5c. Correction: the ZCH 0-edge is case (III)

The 0-direction chain's own pole has coefficient 0 at π(G) (that is what
"chain at the 0-direction" means), so π(G) is NOT a characteristic
exponent of that pole's series, while G ∈ V_{1,a} whenever ν_G ≥ 2
(ν ≥ 2 forces V_1 membership, Not 3.4; π(G) is off-lattice, realized as a
characteristic value of the branch that does jump there). For the 0-edge
Prop 9.3 case (III) applies ("F ∈ V_{1,a} and u > α_{j−1}"), equations
(e)–(h) with ν := ν_F: i-normalized, κ̄_G = κ̄_e + n′, D_G/i = ρ_e + n′
with n′ = n/ν_G ∈ (1/ν_G)ℕ*, hence handshake

    **κ̄_G − D_G/i = κ̄_e − ρ_e = ν_e·w_e   (0-edge, case III).**

The join then demands w_other = ν_e·w_{0-chain} with ν_e ≥ 2: **ZCH cells
are reachable only when the arriving chains carry w's in an integer ratio
ν_e ≥ 2**. In particular, at td = 6 (single value w = 2) ZCH is
unreachable outright, and the corrected pre-suffix jump menu is exactly
{IIa (2,3,1), M = 2} — the promoted residue (machine check 7; the engine's
(a)–(d)-modelled ZCH child (M=3, κ̄=3) was suffix-killed in the promoted
record, so no promoted conclusion changes, but the book spec should carry
the corrected ZCH reach equation). The non-0 edges of a ZCH merge, and
all IIa edges, are case (II) (DS1(d) argument at the merge: nonzero
arrival coefficient at an off-lattice exponent = characteristic exponent
of the arriving pole's series); I-family merges (ν_G = 1) are case (I)
(V_{2,a}\V_{1,a}, lattice meet). All non-0 edges keep the §5a handshake.

### 5d. Correct root edge: case I and the all-`mu=1` formula

A genuine root merge has contact zero, so `(0,y) in V_{2,a}\V_{1,a}` and
Proposition 9.3 selects case I. Here `V_1` uses actual characteristic
indices `j>=1`; admitting the technical `alpha_0=0` would make Notation 3.4
ask for undefined `e_{-1}`. Work with lower/rootward `F=(0,y)`, upper parent
`G=F+c`, and the promoted hypotheses `F,G in V_a cap T_a^searrow`.

Put `P_G=deg(p_G)`, `rho_G=D_G/P_G`,
`w_G=(kappa-bar_G-rho_G)/nu_G`, and let
`mu=mult(p_F^red,c)`. Proposition 8.1(i) at the root and Statement 3.17
derive `P_G=i*mu`. Case-I equations (c),(d), together with Statement 9.2
`K_F=1`, give

    D_F=(D_G+n P_G)/nu_G,     1=(K_G+n)/nu_G,
    X_F:=D_F/i=mu(1-w_G).

Since `D_F,i,mu>0`, every such root edge requires

    **w_G=1-X_F/mu<1.**

For an all-`mu=1`, `r`-way meet, MP6/MP7 give the reduced root degrees
`(dp,dq)=(r,r+l)`, `r>=2`, `l>=1`. At `u=0`, top-degree cancellation in
Proposition 8.1(iv) gives `X_F=dp/dq=r/(r+l)`, hence

    **w_G=l/(r+l) in (0,1).**

Therefore `W={2}` excludes the all-`M=1` root layer at `td=6,m=2`, without
an AWS census. This is not a root-`M=1` kill: the exact local `r=2,l=1`
cell has `w=1/3` and `M_root=1`. The old case-IV equations remain relevant
only to a root endpoint satisfying their distinct non-`V_2` hypothesis;
mixed-`mu`/off-axis root completeness remains outside this theorem.

---

## 6. The Chain-Depth Closure Lemma

**Lemma (chain-depth closure / depth-invariance).** Let (m, td) be given,
and let E be an M=1 segment entry (pole entry via MP4, or M=1-emitting
merge child), with invariant w_0 = w(E). Let Menu_{≤d}(E) be the set of
jump-cell data (family, ν, l, M, κ̄_G, D_G/i) reachable at the end of a
segment of depth ≤ d from E (per-edge Prop 9.3 reach, all-μ=1, MP6/MP7
anatomy). Then:

1. (finite w-alphabet) every frame reachable from E at any depth has
   w ∈ W(w_0), the finite closure of §4, and each segment performs fewer
   than log_{3/2} num(w_0) + 1 resonant steps; all other steps fix w;
2. (menu factorization) Menu_{≤d}(E) ⊆ Menu(W(w_0)) :=
   ∪_{w ∈ W(w_0)} Menu(w), which is finite by §5b, with the case-(III)
   ZCH constraint of §5c and the all-`mu=1` case-I root law of §5d;
3. (stabilization) Menu_{≤d}(E) = Menu_{≤d₀}(E) for all d ≥ d₀ where
   the proved safe bound is `d₀ ≤ 2·gen(W(w_0))+2`: **the map
   depth ↦ reachable jump-cell menu is constant beyond such a d₀.**  The
   sharper `gen(W)+2` bound is machine-verified through generation four but
   lacks a complete chaining proof in general.

*Proof.* 1 is DS1–DS3 (§2–§4). 2 is DS4 (§5): each edge's contribution to
the merged child is a function of `(w_e,cell)` alone; joins force shared
handshakes. For 3, neutral `l=0` steps preserve `w`, while each resonant
step advances one generation of the finite closure. Replaying a deep path
may require one neutral alignment step between consecutive resonant steps,
and one terminal alignment step, which gives the safe
`2·gen(W)+2` bound. The earlier compression to one neutral step total did
not prove `gen(W)+2`; see SHEET6-DEPTH-REVIEW §4. ∎

**Nonroot layer at td = 6, m = 2** (entry (ρ, ν, κ̄) = (1, 2, 5)): W = {2}, gen = 0,
d₀ = 2; reachable frames are exactly {(2, ν, 2ν+2) : ν ≥ 2} (the
phase-4 record's 24 μ1-shapes; check 6); the menu is constant from depth 1
and equals the promoted record: jump cell IIa (2,3,1), M = 2, child
(κ̄, D/i, ρ) = (5, 3, 1/2) = Q(6,12,3,2,5) at i = 2 — explaining the
351/351 pair depth-invariance — plus the suffix-dead engine-model ZCH
(2,3) cell, which the corrected §5c model removes pre-suffix; ν = 1 cells
only l ∈ {1,2,4} in that historical diagnostic. All-`M=1` root meets are
also excluded: case I requires `w=l/(r+l)<1`, whereas `W={2}`.

---

## 7. Mechanical verification

cases/depth_closure_check.py — exact (int/Fraction), self-contained except
check 6, ~seconds; 13/13 PASS this session:

1. **Step laws** on every BFS edge (td=6 depth ≤ 12; all entries depth 8):
   w′ = w·n/Δ; Δ | num(w) at resonant steps; contraction ≤ 2/3.
2. **td=6 nonroot record**: W = {2}; no resonant step exists (Δ | 2 empty);
   cumulative jump menu constant depths 1–12; equals promoted cell + the
   suffix-dead ZCH; ν=1 diagnostic cells l ∈ {1,2,4}; `w>=1` excludes
   every all-`M=1` root edge by the corrected case-I law of §5d.
3. **All m=2, b=1 entries with td ≤ 12** (10 entries, types (2,3)…(5,6)):
   BFS w-sets ⊆ W(w_0); menus empirically stabilized at d₀ = gen+2 vs
   depth 8, while the theorem uses the safe `2·gen+2` bound.
   Sample: w_0 = 4 gives W = {4, 2} (gen 1), w_0 = 6 gives W = {6, 4, 2}.
4. **Closed-form Menu(w)** (§5b ν-determination) ⊇ every swept frame menu.
5. **St 9.6(v) cross-check**: the printed λ=0 family has w ≡ 3/2 (s ≤ 20).
6. **Engine cross-check**: all 26 promoted twopole_check phase-4 shapes
   have w = 2 at every instance (including the ν=1 zch over-generation).
7. **Corrected ZCH case-(III) model**: 403 per-edge solves at td=6, none
   joinable (needs w′ = ν_G·w ∈ W): corrected menu = {IIa (2,3,1)} exactly.

Reproduction: `cd cases && python3 depth_closure_check.py` (exit 0 iff all
pass); `python3 twopole_check.py l1only` for the phase-4 baseline.

---

## 8. Finite all-`M=1` book; broader root sectors remain separate

The 2026-08-12 packet's all-`M=1` pattern book is retained after replacing
its false case-IV root label by the case-I theorem in §5d and replacing its
sharp stabilization proof by the safe bound. This does not promote a mixed-
`mu`/off-axis or coefficient-realizability book. Layer C is

    C′. Chain layer (CLOSED; H1): an M=1 segment is coded, up to
        menu-equivalence, by its invariant w; per entry w_0 =
        a(b(α+β)−1)/(bν) and the finite closure W(w_0) (§4); segments of
        arbitrary depth realize no jump-cell data beyond the safe bound
        d₀ ≤ 2·gen(W)+2 (Lemma §6); M=1-emitting merges map w by
        ·(r+l)/(lν+1) (§5b), composed ≤ m−1 times (MP1).

and layer J indexed by `(w,cell)` instead of `(frame,cell)`, with the added
filters: join implies equal handshakes; ZCH implies `w`-ratio `nu_e>=2`
across edges (§5c); an all-`mu=1` case-I root meet has at most one
`l=r*w/(1-w) in N*` for each fixed `(w,r)` (§5d). Since `W` is finite and
`r<=m`, this root layer is finite. Layers E, T and the all-`M=1` jump/root
layer therefore form a finite pattern book. Mixed-`mu`/off-axis root
packages and coefficient/Puiseux realizability are not covered. ∎

Required engine fixes when the book is next run (no promoted conclusion
changes): (i) l1_merges/all_merges: ZCH edges must use the case-(III)
solve (n′ ∈ (1/ν)ℕ*, handshake ν_e·w_e) — the current (a)–(d) model
over-generates (its td=6 extras were suffix-dead); (ii) phase-4
zch_children (ν_F = 1 chain steps) can be deleted (DS1, St 3.16 iff);
(iii) a genuine all-`M=1` root meet must be modeled as case I with
`w=l/(r+l)<1`; retain `l>=1`, recognize root before applying the nonroot
`M=1` kill, and do not use a finite `l` cap as completeness evidence.

---

## 9. Honest perimeter

- **Tier.** DS1 is printed-tier over promoted MP5 (St 3.16 iff + Not
  3.4/3.5 + Def 3.1 + Prop 3.1 + St 3.17(i); the lattice argument in
  DS1(d) is elementary arithmetic of Defs 3.1–3.3). DS2–DS4 are H1
  (Prop 9.3 (a)–(h), (i)–(m) printed-step arithmetic), the tier already
  sanctioned for MP9's root clause and the review's §5a bounds. No new
  hypotheses beyond MP's P1/P2/P3/P4 + H1; E9/H2 not used.
- **Entry edge.** The first step out of a pole vertex with ν_pole = 1
  (Prop 5.5 case (i), pole vertex ∈ V_{2,a}) is grounded as in MP/the
  engines (H1 per-edge use from the entry frame); DS1 applies from F_1
  down regardless. Entry vertices with ν ≥ 2 are themselves V_1 (Prop 5.5
  case (ii)) and need no special treatment.
- **Scope.** The lemma closes the M=1 axis — exactly the F5 demotion. Out
  of scope, as in MP: mixed merges with all μ_e ≥ 2 (m ≥ 3, quarantined),
  the coefficient layer (Prop 8.1(iv) rigid solve vs ratio match, MP §8
  item 3), m ≥ 3 reachability of Theorem O's pattern-level escape, and
  M ≥ 2 suffix chains — though check 5 (St 9.6(v) conserves w = 3/2)
  strongly suggests the same closure mechanism governs the suffix; the
  suffix engine (hiii_compose) is anyway kill-complete per instance.
- **Menus.** "Stabilizes" is proved for the cumulative menu (what the
  book enumerates); per-depth menus can only shed transient-w items after
  d₀, never gain. Caps in the checker (ν ≤ 24/48, l ≤ 8/12, n_pat ≤ 8)
  affect only which INSTANCES are swept, not the menu conclusions, which
  are cap-free via §5b's determination equations; the resonance test
  Δ | num(w) is exact and cap-free.
- **Not claimed.** No bound on segment depth itself (impossible from
  (m, td): §2 R1); no claim that every W-value or menu cell is REALIZED
  by an absolute (f,g) — the book remains conservative (P-realizability
  untracked), exactly as in the promoted engines.
