# BOOK-OFFAXIS.md — Off-axis (b >= 2) sector adjudication

Mission: adjudicate the off-axis sector flagged by both external reviewers and
the BOOK-ENUM.md closing erratum. The book enumerated only all-b=1 entry
configurations; entries with b_i >= 2 propagate M = b_i down their chains and
can meet in MIXED MERGES (all mu_e >= 2, legal at m >= 3). The prime-td
multi-pole exclusion was retracted pending this adjudication.

Status: MIXED AFTER TRIPLE REVIEW (2026-08-12, BOOK-OFFAXIS-REVIEW.md;
Fable + Grok + GPT converged on identical verdicts): R1.0-R1.2 (rigidity
lemma, orbit-degree transport, l-fold cancellation) + R2 (all handshakes,
searrow law) CONFIRMED and promotable after fix cycle; R1.3-R1.5 REFUTED
(dirty-vertex menu omits the printed St 9.6(II)(b) eta-family; the
M-descent law contradicts St 9.6(iii)/(iv)); td=7 RESTORATION RETRACTED
AGAIN (honest state: 4 DEAD / 2 ALIVE at td=7, incl. the exact (7,5)
eps-cell d^2=(3/2)c^2 -> live equal-w join); sections 8-9 recount
UNCERTIFIED. Repair route: lambda-budget per the review — **EXECUTED
(2026-08-12, this session, §10): the priced menu P0 (AF2-derived λ per
St 9.6-family step), the shared-budget composition P1 (St 9.4 (25) +
H3-psi at the trunk terminal, ψ = ⌈1/(1−w)⌉ − 1), and the exhaustive
td-7 adjudication P3/P4. RESULT: the G2/ε reopening (the review's star
(7,5) cell → equal-w join) is PRICED OUT (0 fitting routes), the L2 cell
dies by the corrected St 8.4 transport, but td = 7 does NOT close: the
printed St 9.6(iii) (A)-jump feeds 62 budget-fitting merge cells (1689
routes, 1390 at exact budget equality), all fully pinned T1-rigidity
targets. §8's "CLOSED" theorem stays RETRACTED; §9's recount is
superseded by the §10 stage-R′/P recount.** 
Original status [PROVENANCE ONLY — its §8/§9 claims are RETRACTED, see
above and §10]: COMPLETE + CLOSURE LEMMAS PROVED (2026-08-12, two sessions).
VERDICT (updated): **R1 (off-axis w-law) and R2 (general-μ merge
anatomy) are now PROVED (§6–§7)** at H1 tier (Prop 9.3 arithmetic over
promoted MP0–MP8). Consequences: **the td = 7 prime-td exclusion is
RESTORED (§8)** — the single off-axis td=7 entry dies at every merge
configuration; the stage-R recount (§9) kills 2251 of the 2691 merge
cells (0 open), leaving 440: td 11 keeps 12, td 13 keeps 129 — the
td = 11/13 panels are NOT yet restored. Earlier findings unchanged:
23/27 entries pass L6; 700 mixed cells; the erratum's "mixed merges
legal only at m ≥ 3" stays corrected (false at m = 2 off-axis).
Sections §1–§5 are the first session verbatim (their td-7 rows are
superseded by §8–§9).

## 0. Sources consulted

- BOOK-ENUM.md: erratum (all-b=1 axis only; prime-td retraction), §1 layer-E
  (entries reuse sheet6_campaign.tdu_rows(Λ_i) filtered to global type; MP4
  pin M_i = b_i; any b_i >= 2 => off-axis class, 27 entry multisets, never
  cell-expanded; prime-td panels 100% off-axis), §6 perimeter.
- SHEET6-MULTIPOLE.md MP4 (entry pin: (deg p, deg p_g) = b(α,β), M = b;
  b = 1 forced iff Λ β-minimal or Λ prime), MP5 (M=1 propagation), MP6
  (merge anatomy; k = 0 needs some μ_e = 1), MP7 (l = 0 kill; resonant
  jumps), MP8 (budget transparency proved on the pure M=1 forest ONLY),
  line 120: mixed merges all-μ_e >= 2 obey only MP6(b)/(d) subadditivity,
  legal only m >= 3 downstream of an earlier jump.
- TEMPLATE-ATTACK.md §1a: L6 law + i-sync. SHEET6-DEPTH.md DS1 (§2).
- SHEET6-TDUNIFORM.md §1 menu / tdu_rows b-parameterization.

## 1. Entry census (b >= 2, td <= 14, L6 + MP4 pin)

Engine: cases/book_offaxis.py (reuses book_enum.entries/tdu_rows verbatim;
gate = book_enum.gate() PASS, on-axis td=6 record unchanged; MP4 sanity
PASS: prime/β-minimal Λ force b = 1 arithmetically in tdu_rows).

**27 raw off-axis entry multisets** (matches BOOK-ENUM §5 count) across
td = 6..14, m = 2..⌊td/3⌋; **23 survive the L6 pole filter**
gcd(a(α+β), ν) = 1 (≡ N1 gcd(a,ν) = 1, equivalence asserted per row).
The 4 L6 kills all share the same bad pole (2,3)-L6 a=2, b=1, ν=2
(gcd(2·5, 2) = 2 — the TEMPLATE-ATTACK "a2ν2-(2,3) dies everywhere" row):
td10 m2 L4b2+L6a2; td13 m3 L3+L4b2+L6a2; td14 m2 L6a2+L8a2b2;
td14 m3 L4b2+L4b2+L6a2.
Full surviving table with per-pole M = b and w0 in the engine output;
headline rows (M-vectors): td7 m2: [1,2]; td8 m2: [2,2]; td12 m3:
[2,2,2]; td13 m2: [2,5],[2,3],[2,1],[1,3]; td14 m2: [2,5].
Only types (2,3),(2,5),(3,5),(3,4) occur; b ∈ {2,3,5}.

### 1a. Prime-td check (td = 7, 11, 13)

**NOT emptied at entry level**: L6 survivors 1 / 3 / 6 at td = 7 / 11 / 13.
The prime-td restoration must therefore come from the chain/merge layer
(§2–§3), not the entry layer. Witness at td = 7 (m = 2):
(2,3) with Λ = (3,4), poles (a,b,ν) = (1,1,2) ⊕ (1,2,3), M = (1,2),
w0 = (2, 3/2). NOTE: every td=7/11/13 survivor with m = 2 has at least
one b = 1 pole EXCEPT none — inspect: td7 [1,2]; td11 [1,2],[1,3],[1,2,2];
td13 [1,5],[2,3],[2,1],[1,3],[1,2,1],[1,1,1,2]. Only td13 m2 (2,3)
Λ=(4,9) M=[2,3] has NO b=1 pole; all other prime-td survivors carry a
forced μ = 1 arrival (MP5), so their G* obeys full MP6 anatomy.

## 2. Off-axis chain calculus (M = b >= 2 segments)

Thesis pp. 41-45 read verbatim (sigray_full.pdf):

(a) **M-divisibility needs no M=1** (St 8.5, p. 42): F ∈ T_a^↘ ∩ V_a,
G = F°, G ∉ V_{2,a} ⟹ M_G | M_F. So down every merge-free segment the
M-value divides b_i non-increasingly, and arrivals obey μ_e | M (St 8.4,
p. 42, mult(p,c) | M_G — verbatim, no M=1 hypothesis). A b ≥ 2 chain MAY
still arrive with μ_e = 1 (any divisor).

(b) **Pattern shape** (St 3.18, used in St 8.5's proof): at a non-merge
chain vertex G ∉ V_{2,a}, p_G = ⊖(η^ν − c^ν)^l, c ≠ 0 — the l-fold
thickened ν-orbit; Prop 8.3(ii) is its l = 1 (M = 1) specialization.
DS1(a)-(d) (SHEET6-DEPTH §2) generalizes VERBATIM to l ≥ 2: the proof
uses only the root SET {ζc} (≥ 2 roots ⟹ ν ≥ 2, c ≠ 0), Not 3.4/3.5
integrality, and the characteristic-exponent descent — never simplicity.
So off-axis segment vertices ∉ V_{2,a} are still consecutive
characteristic vertices of their own pole with case-(II) edges.

(c) **The two genuine breaks**:
  (c1) V_{2,a} escape: MP5's exclusion of separating rays used M = 1
  (Cor 8.1 ⟹ G ∉ V_{2,a}; Cor 8.1 needs M_F = 1). For M ≥ 2 the printed
  record does NOT exclude segment vertices in V_{2,a} (Prop 8.2 gives
  only the conditional d_F ≤ deg(p_F)((1−v)/M + v − u) descent). Hence
  the MP8 zero-row itemization does not extend: off-axis chains can
  carry Y(F) ≠ ∅ / λ > 0 — but a POSITIVE lower bound is not printed
  either (transparency fails in both directions; see §3 budget).
  (c2) DS2 w-conservation FAILS as printed: its proof takes Prop 9.3(b)
  dp_F/dq_F = (ρ_G+n_e)/(κ̄_G+n_e) "both sides in lowest terms" via
  gcd(ν, nν+1) = 1 — for M ≥ 2 gcd(dp,dq) = M ≥ 2, the lowest-terms
  step breaks, t is determined only up to the M-fold ambiguity, and the
  M ≥ 2 chain q-shape is not printed. NO w-alphabet, NO equal-w join
  law, NO root w<1 window on off-axis chains at printed tier.

## 3. Mixed-merge cells

Engine: merge_cells/merge_census in cases/book_offaxis.py — for each L6
entry: all merge hierarchies (MP1: Σ(r−1) = m−1 automatic), all
μ-assignments (leaf μ_e | b_i by St 8.4/8.5; inner μ_e | emitted M), all
emitted M_G | Σμ_e (subadditivity — the ONLY (d)-law valid at mixed
merges, MP-REVIEW l.120), MP2 (interior G* emits M ≥ 2; G* = (0,y)
root-merge cells kept, tagged). Conservative superset: no l/ν expansion,
no non-ZCH M | r cap, no root-merge St 9.2 arithmetic.

**2691 merge cells over the 23 entries: 700 contain a MIXED (all-μ_e ≥ 2)
merge, 1991 are pure MP6-anatomy** (some μ_e = 1 at every merge — full
MP6(a)-(e) applies there). Highlights:
- **ERRATUM CORRECTION (sharpening)**: mixed merges are structurally
  available already at **m = 2** (both b_i ≥ 2, both μ_e = 2: td8 [2,2]
  5 cells; td12 [2,2],[3,3],[2,2]; td13 [2,3] 3 cells; td14 [2,5]).
  The BOOK-ENUM erratum's parenthetical "legal at m ≥ 3" is an all-b=1
  relic (there μ ≥ 2 needs an upstream jump, consuming a merge); off-axis
  it is FALSE — the gap is wider than stated, not narrower.
- Prime td: td7: 6 cells, ALL MP6-anatomy (the b=1 pole forces a μ=1
  edge at G*); td11: m=2 rows all MP6 (14 cells), m=3 row 103 cells of
  which 25 mixed; td13: m=2: 38 cells (3 mixed, all in the all-b≥2 row
  Λ=(4,9) M=[2,3]), m=3: 50 (5 mixed), m=4: 598 (78 mixed).
- Kills actually firing at this tier: MP2 (M=1 interior emission) only.
  L6 fired at entry layer (§1). No MP7-analogue exists for mixed merges
  (the l ≥ 1 forcing needs a μ=1 edge); no λ-charge is printed (§2(c1)),
  and MP8 transparency is equally unavailable — budget status of every
  off-axis cell is UNKNOWN, in both directions.

## 4. Per-td verdicts

- **td 6, 9 (all m); m=4 td 12**: off-axis sector EMPTY (0 raw entries).
  The book's panels there are COMPLETE as printed; at td = 6 the
  multi-pole story remains exactly Theorem O's residue-A cell.
- **td 7 (m=2)** [SUPERSEDED TWICE: §8's "CLOSED" was retracted by the
  triple review; §10's λ-budget adjudication now gives the honest state:
  OPEN with 62 explicitly pinned budget-fitting cells]: one off-axis
  entry survives L6: (2,3),
  Λ=(3,4), M=(1,2), 6 merge cells, all with full MP6 anatomy (μ=1 edge
  forced); the b=2 chain carries w ≡ 3/2 (frozen, §8 Step 2) against
  the b=1 chain's w ≡ 2, and every join/root configuration dies.
- **td 11**: not restored. 3 entries; m=2 cells (14) all MP6-anatomy —
  same single missing lemma R1; m=3 row adds 25 genuinely mixed cells
  (rider R2 also needed).
- **td 13**: not restored; the worst prime panel. 6 entries incl. the
  only all-b≥2 prime-td row (2,3) Λ=(4,9) M=[2,3] (its 3 mixed cells
  need R2); plus b=5 chains (Λ=10 rows) — largest per-pole M in sweep.
- **td 8, 10, 12, 14 (composite)**: off-axis cells exist and are open
  (same riders); they sit BESIDE the book's on-axis survivors, so these
  panels were open anyway — the off-axis sector adds breadth, not a
  first counterexample-channel.
- **Global**: no (m, td) panel in 6..14 is closed by the off-axis sweep
  alone; conversely NO printed-tier statement kills any of the 2691
  cells beyond MP2/L6. The sector is a true frontier, exactly as the
  reviewers flagged.

## 5. Riders / honest caveats

- **R1 (off-axis w-law)** — DISCHARGED: proved as §6 (q-shape R1.1,
  transport R1.2, dirty vertices R1.3–R1.4, closure R1.5). The
  prediction was optimistic in one respect: equal-w join holds only
  edge-wise per μ (R2.1), so pure-MP6 cells with matching w survive
  stage R (they need the DS4 menu rerun); td=7 nonetheless closed (§8).
- **R2 (mixed-merge anatomy)** — DISCHARGED: proved as §7. The k=0
  analogue is the searrow law R2.2(S) (μ_min·dq > dp; non-chain orbits
  only when dq < dp); MP6(c) generalizes as R1.0 q-rigidity; MP7's
  survivor is R2.3 (q ∝ p^h dies; l = 0 no-resonance fails but is
  (S)-pruned to ν = 1).
- **R3 (budget silence)** — RESOLVED IN THE CHARGE DIRECTION (§10 P0/P2,
  2026-08-12): every dirty/ε step and every merge NE-orbit/free 0-root
  carries a derived λ ≥ 1 (regularity-free for gap > 0), priced by the
  promoted AF2 rule; the shared budget is St 9.4 (25) with the P1
  ψ-certificate. New kills at td = 7 per §10 P4 (partial: 62 cells fit).
- **R4 (conservative superset)**: the merge census imposes no l/ν
  window, no i-sync (always solvable: segment ν-products are free
  integers ≥ 1, DS1-R1 gives no (m,td) bound), no root-merge St 9.2
  arithmetic, no P-realizability. Counts are upper-bound structure, not
  existence claims.
- **R5 (inherited)**: Prop 5.8 td = ΣΛ generic-a rider (SIGRAY-AUDIT)
  carries through the entry layer; everything here consumes it.

## 6. LEMMA R1 (off-axis w-law) — PROVED (2026-08-12, this session)

Setting: pole P_i entry (a,b,ν), M = b ≥ 2; chain vertices F below with
r(F) = 1 (single arriving edge); i-normalized frames ρ_F := D_F/deg(p_F)
(full pattern), κ̄_F := κ_F(1−π(F)), **w_F := (κ̄_F − ρ_F)/ν_F** (DEPTH §1).
All page cites = refs/sigray_full.pdf, printed = pdf page.

**R1.0 (q-multiplicity rigidity — new, fully general).** At EVERY vertex
F ∈ T_a↘ ∩ V_a (chain or merge, any multiplicities): in Prop 8.1(iv)
(p. 40) δpq′ − (1−u)p′q = ⊖p, every root of p is a **simple** root of q,
every q-root off p is simple, and if ν_F ≥ 2 then η ‖ q, hence
**dq ≡ 1 (mod ν) and gcd(M_F, ν_F) = 1 always** (Prop 8.1(v)).
*Proof.* Let ξ be a p-root of multiplicity μ★ ≥ 1. η-adically at ξ:
v(δpq′) = μ★ + v(q) − 1 = v((1−u)p′q); RHS ⊖p has v = μ★ exactly.
v(q) = 0 gives LHS-v = μ★ − 1 < μ★; v(q) ≥ 2 gives LHS-v ≥ μ★ + 1 > μ★
(cancellation only raises v): both impossible, so v(q) = 1, and the
order-μ★ coefficient q′(ξ)(δ − (1−u)μ★) = ⊖ ≠ 0 also forces
**dp ≠ μ★·dq** (δ/(1−u) = dp/dq, St 8.2's proof p. 41). At a q-root ξ₀
with p(ξ₀) ≠ 0 and v(q) ≥ 2 the ODE gives 0 = ⊖p(ξ₀) ≠ 0: simple. At
η = 0 with p(0) ≠ 0, ν ≥ 2: semi-invariance q = η^{e₀}s(η^ν) (St 8.5's
proof step via Prop 4.6, p. 43 — M-free); e₀ = 0 forces q′(0) = 0 and
p′(0) = 0, so the order-0 term of (iv) is 0 ≠ ⊖p(0); e₀ ≥ 2 likewise
kills order 0; so e₀ = 1. If p(0) = 0 the first part gives v_0(q) = 1. ∎

**R1.1 (off-axis chain q-shape).** At a chain vertex F ∉ V_{2,a} with
M_F = M ≥ 1: p_red = ⊖(η^ν − c^ν)^l, c ≠ 0, l ≥ 1 (St 3.18, p. 18;
St 8.5's proof p. 43 — no M = 1 used; l = mult of the arriving root =
μ_edge | M_parent by St 8.4 p. 42), and
**q = ⊖η·Π_{s=1}^{n}(η^ν − b_s^ν)**, all roots simple, c^ν ∈ {b_s^ν},
n ≥ 1; (dp, dq) = (lν, nν + 1); **M_F = gcd(l, nν+1)**; in particular
M_F | l and nν ≡ −1 (mod M_F).
*Proof.* Write P := η^ν − c^ν (squarefree). Divide (iv) by P^{l−1}:
δPq′ − l(1−u)P′q = ⊖P. By R1.0, q = P·R, R squarefree, gcd(R,P) = 1,
η ‖ q, extras in ν-orbits (semi-invariance), so q = η·(n ν-orbits) with
P | q; n = 0 would force dq = 1 < deg(PR) ≥ ν + 1. gcd(lν, nν+1) =
gcd(l, nν+1) since gcd(ν, nν+1) = 1. ∎

**R1.2 (clean transport law — DS2 verbatim in orbit degree).** Let
G → F be a chain edge (G parent above, F = child ∉ V_{2,a} as in R1.1,
arrival mult l_F). The edge is Prop 9.3 case (II) (§2(b): DS1(a)–(d)
generalize verbatim). Then with **Δ_F := (n_F − 1)ν_F + 1 = dq_F − ν_F**
(orbit-degree delta, NOT dq − dp):

    t := (κ̄_G − ρ_G)/Δ_F = w_Gν_G/Δ_F,  n_e = tν_F − ρ_G ∈ ℕ*,
    κ̄_F = t·dq_F/ν_G,   ρ_F = t/ν_G,   **w_F = w_G·n_F/Δ_F.**

The l-fold thickening CANCELS: n_F = 1 conserves w for every (ν_F, l_F);
n_F ≥ 2 contracts w by ≤ 2/3 and needs **Δ_F | num(w_G) and
den(w_G) | dq_F** (both from κ̄_F = w_G·dq_F/Δ_F ∈ ℤ, DS1(c),
gcd(Δ_F, dq_F) = 1). This repairs §2(c2): the lowest-terms step of DS2 is
replaced by the exact proportion — Prop 9.3(b) (p. 50), i-normalized with
deg(p_G) = i_F·l_F (St 8.3(ii) + Prop 8.1(i)), reads
l_Fν_F/(n_Fν_F+1) = l_F(ρ_G + n_e)/(κ̄_G + n_e), and l_F cancels, giving
(ρ_G + n_e) : (κ̄_G + n_e) = ν_F : dq_F with gcd(ν_F, dq_F) = 1; (c),(d)
close in (ρ, κ̄) exactly as in DS2 (deg p_F = i_F l_F ν_F). ∎

**R1.3 (dirty vertices: the V_{2,a} escape is the printed St 9.6(II)(a)
family).** §2(c1)'s escape is real but RIGID. Let F be a chain vertex
(r = 1) with arrival mult μ = 2. If F carries any non-chain root, then
(i) every non-chain orbit is northeast with q·mult < deg p (St 8.2
p. 41: searrow iff dq·mult > dp; searrow non-chain roots are excluded
by the M-free D5(c)/Prop 6.8 pole-manufacture, which would make F a
merge); (ii) mult < dp/dq < μ = 2 forces ALL non-chain orbits simple;
(iii) R1.0 + semi-invariance force **p = ⊖(η^ν−c^ν)²Π₁^k(η^ν−d_j^ν),
q = ⊖η(η^ν−c^ν)Π₁^k(η^ν−d_j^ν)** — extras l_ex = 0 forced by dq < dp —
i.e. (dp, dq) = ((k+2)ν, (k+1)ν+1), k ≥ 1: EXACTLY the thesis's own
St 9.6 case (II)(a) shape with l = 0 (p. 52). For μ = 1 arrivals no
dirty vertex exists (dq > dp makes every root searrow: D5(b), M-free).
General arrival mult μ = l ≥ 2: non-chain mults m_j ≤ l − 1,
m_j·dq < dp < l·dq, dp = ν(l + Σm_j), dq = (1 + k + l_ex)ν + 1.

**R1.4 (dirty transport).** Across a dirty vertex F (arrival mult l,
shape R1.3) the case-(II) equations give, verbatim as R1.2 with the
proportion (ρ_G+n) : (κ̄_G+n) = dp : (l·dq),

    κ̄_F = l·w_G·dq/(l·dq − dp) ∈ ℤ,   ρ_F = κ̄_F/dq,
    **w_F = w_G · l·(dq−1)/(ν(l·dq − dp))**,

(l = 2, R1.3-exact shape: w_F = w_G·2(k+1)/(kν+2): ν = 2 neutral,
ν ≥ 3 contracts by ≤ 4/5). Integrality bounds the menu:
l·dq − dp | l·num(w_G)·M_F and M_F = gcd(dp,dq) | M_parent, so
ν(k + l·l_ex) + l ≤ l·num(w_G)·M_F — finitely many dirty steps per w. ∎

**R1.5 (off-axis w-closure).** W_off(w₀, b) := closure of {w₀} under
(clean resonant steps R1.2) ∪ (dirty steps R1.4 with l | b, l ≥ 2).
Finite (every non-neutral multiplier ≤ 4/5; neutral steps fix w), and
every frame reachable from the pole carries w ∈ W_off(w₀, b). Arrival
constraint (used at merges): an edge of mult μ_e ≥ 2 leaving a depth ≥ 1
chain vertex H needs μ_e | M_H | gcd(·, dq_H), dq_H ≡ 1 (mod ν_H), so
**gcd(ν_H, μ_e) = 1**; at depth 0, ν_H = ν_i (entry).

## 7. LEMMA R2 (general-μ merge anatomy) — PROVED (2026-08-12)

Merge G, r ≥ 2 arriving edges H_e → G, mult μ_e = mult(p_G^red, c_e)
(μ_e | M_{H_e}, St 8.4). X_G := D_G/i_G. Edges classified by Prop 9.3
(p. 50): non-0 arrivals at G ∈ V_{1,a} are case (II) (DS1(d) argument,
M-free), G ∈ V_{2,a}\V_{1,a} case (I), 0-direction case (III), G = (0,y)
case (IV) — exhaustive.

**R2.1 (generalized handshake; the equal-w join law is the μ = 1
shadow).** For every case-(I)/(II) edge, Prop 9.3(c),(d) i-normalized by
deg(p_{H_e}) = i_G·μ_e give κ̄_G = (κ̄_e + n_e)/ν_e and
X_G = μ_e(ρ_e + n_e)/ν_e, hence eliminating n_e = ν_eκ̄_G − κ̄_e ∈ ℕ*:

    **X_G = μ_e·(κ̄_G − w_e)**        (case I/II)
    **X_G = μ₀·(κ̄_G − ν_e·w_e)**     (case III, 0-edge; DEPTH §5c gen.)
    **w_e = 1 − D_{(0,y)}/(μ_e·i₀) < 1** (case IV root, D = l_f ≥ 1;
        n_e = ν_e − κ̄_e forced, κ̄_e < ν_e both parents — DEPTH §5d gen.)

and Prop 9.3(b) is the consistency X_G/κ̄_G = dp_G/dq_G. Consequences:
(i) two arrivals with equal μ and both non-0 share w (DS4 5a is μ ≡ 1);
(ii) unequal μ PIN the frame: κ̄_G = (μ_aw_a − μ_bw_b)/(μ_a − μ_b);
(iii) κ̄_G > 0, X_G > 0 are hard filters; (iv) **root merges kill every
arriving chain with w ≥ 1, off-axis included, for any μ_e**.

**R2.2 (pattern equation and gcd menu).** p_red =
⊖η^ε·Π_e(η^ν−c_e^ν)^{μ_e}·Π_{j=1}^{k}(η^ν−d_j^ν)^{m_j} (ε = μ₀ if a
0-chain arrives, else 0 — MP6(a)'s k = 0 does NOT survive all-μ ≥ 2);
q = ⊖η·(each distinct nonzero p-orbit ONCE)·Π_{l}(extras, simple)
(R1.0), so dq = (r₀ + k + l)ν + 1, **dq ≡ 1 (mod ν), gcd(M_G, ν) = 1
at every merge** — the MP6(d) backbone survives. New hard laws:
  (S) searrow law: **μ_e·dq > dp for every arriving edge** (St 8.2);
      non-chain orbits need m_j·dq < dp (else the M-free D5(c)/Prop 6.8
      manufacture makes them chains), so **k > 0 forces dq < dp** and
      every arriving μ_e > every non-chain m_j;
  (R) root-mult law: dp ≠ μ★·dq for every mult μ★ of p (R1.0);
  (D) M_G = gcd(dp, dq); subadditivity **M_G | Σμ_e holds iff ε = 0 and
      k = 0** (then dp = νΣμ_e, gcd(M,ν) = 1); in particular it is
      GROUNDED whenever dq > dp, and remains a rider when dq < dp —
      the §3 census's use of it (MP-REVIEW l.120) inherits this rider.

**R2.3 (MP7 analogue: what survives).** (i) q with root set ⊆ roots(p)
and PROPORTIONAL multiplicities (q = ⊖η^{2h/dp·dq}... i.e. q = ⊖p^h·η^s
patterns) is impossible: (iv) collapses to p^{h−1}p′(δh − (1−u)) = ⊖,
degree ≥ 1 ≠ 0 (h = 1, l = 0, ZCH/ν=1 is MP7's own kill). (ii) The full
l = 0 no-resonance FAILS at mixed merges: l = 0, k = 0, ε = 0 gives
q = η·rad(p), M_G = gcd(Σμ_e, rν+1), which is ≥ 2 on a nonempty
arithmetic family — BUT (S) prunes it hard: e.g. r = 2, μ = (2,3) needs
2(2ν+1) > 5ν, i.e. ν = 1 only. (iii) T1-style rigidity solves for
survivors of (S)+(R)+(D)+R2.1 are cell-finite per (m, td) (κ̄_G pinned
or 1-parameter); executed per-cell in the §9 engine stage rather than as
a closed form. Full MP6(a)/(e) (k = 0, λ = 0) remain FALSE in general
at mixed merges: northeast orbits are budget objects (R3), not banned.

## 8. THE td = 7 KILL — **RETRACTED (review) / re-adjudicated in §10**
## (Steps 1, 3, 4 stand as conditional kills; Step 2's M-law is refuted;
## the honest priced verdict is §10 P4: OPEN, 62 cells)

Witness (§1a, the ONLY off-axis td = 7 entry): m = 2, type (2,3),
Λ = (3,4), poles (a,b,ν) = (1,1,2) ⊕ (1,2,3), M = (1,2),
w₀ = (2, 3/2). MP1: exactly one merge G*, r = 2, both chains arrive.

**Step 1 (chain 1 rigid).** b = 1: MP5 clean chain, w-alphabet
W(2) = {2} (DS3: resonance needs Δ | 2, Δ ≥ 3 — none; no dirty vertices
by R1.3 at μ = 1). Chain 1 arrives with μ₁ = 1, w₁ = 2, ν_{H₁} ≥ 2.

**Step 2 (chain 2 frozen at 3/2).** Clean resonance (R1.2) needs
Δ | num(3/2) = 3 ⟹ Δ = 3 ⟹ (n,ν) = (2,2), and den = 2 | dq = 5 FAILS:
no clean resonant step ever. Dirty steps (R1.4, l = 2): κ̄_F =
3((k+1)ν+1)/(kν+2) ∈ ℤ ⟹ (kν+2) | 3(ν−1): k = 1 ⟹ ν+2 | 9 ⟹ ν = 7,
cell (21,15), M_G = 3 ∤ M_H = 2 — dead (St 8.5); k = 2 ⟹ ν = 5, cell
(20,16), M_G = 4 ∤ 2 — dead; k ≥ 3 impossible; ν = 2 needs 2k+2 | 3 —
dead. (These are literally St 9.6's Diophantine cells (A),(C), p. 52,
re-killed by M-divisibility.) So w₂ ≡ 3/2 at every depth, μ₂ ∈ {1,2}.

**Step 3 (interior merge dies).** All 0-arrangements, all μ₂, any cell:
- both non-0 (cases I/II), μ = (1,1): R2.1(i) forces 2 = 3/2 — dead.
- both non-0, μ = (1,2): R2.1(ii): κ̄ = (1·2 − 2·(3/2))/(1−2) = 1,
  X = κ̄ − 2 = −1 < 0 — dead (cell-shape-independent).
- chain 1 at 0 (case III): κ̄ − X = 2ν_{H₁} ≥ 4; edge 2 gives κ̄ − X =
  3/2 (μ₂=1) — dead; or X = 2κ̄ − 3 (μ₂=2) ⟹ κ̄ = 3 − 2ν_{H₁} < 0 — dead.
- chain 2 at 0, μ₀ = 1: subtracting handshakes: ν_{H₂} = w₁/w₂ = 4/3
  ∉ ℤ — dead.
- chain 2 at 0, μ₀ = 2: κ̄ = 3ν_{H₂} − 2, X = 3ν_{H₂} − 4 > 0 with
  ν_{H₂} odd (R1.5 arrival law gcd(ν_{H₂}, 2) = 1; depth 0 gives
  ν_i = 3). ZCH shape (ε = 2, one μ=1-orbit, R1.0/R2.2):
  dp = ν_G + 2, dq = (l+1)ν_G + 1, X/κ̄ = dp/dq ⟹ with A := 3ν_{H₂} − 2:
  ν_G = (A+2)/(l(A−2) − 2); ν_G ≥ 2 forces l = 1, A−4 | 6, A ≡ 1 (3),
  A ∈ {7, 10}; A = 10 has ν_{H₂} = 4 even — dead; A = 7: (ν_G, l) =
  (3,1), cell (dp,dq) = (5,7), M_G = gcd(5,7) = 1 — dead by MP2
  (interior trunk M ≠ 1). Variant q-shapes are excluded by R1.0
  (doubled orbits in q impossible), and k > 0 needs dq < dp = FALSE here
  (κ̄ − X = 2 > 0 ⟹ dq > dp), so the shape list is exhaustive.
- family I (ν_G = 1, case (I) all edges): same handshakes as I/II rows
  above — dead identically.

**Step 4 (root merge dies).** G* = (0,y): R2.1 case IV: every arriving
edge needs w_e = 1 − l_f/(μ_e i₀) < 1 (l_f = d_{(0,y)} ≥ 1, D8/MP9);
chain 1 arrives with w = 2 ≥ 1 — dead. ∎

**Theorem (td = 7 panel closed).** With BOOK-ENUM's on-axis record, the
off-axis sector at td = 7 is EMPTY at H1 tier (Prop 9.3 arithmetic over
promoted MP0–MP8 + R1 + R2). The prime-td exclusion at td = 7 is
RESTORED. (td = 11, 13 remain partially open: see §9 recount.)

## 9. STAGE-R RECOUNT — **UNCERTIFIED (review findings 1-2: the W_off
## alphabet embeds the refuted M-law and omits the ε-cells; kept for
## provenance; superseded by §10 P5's stage R′)**

Filters implemented (each cites its proof): per-pole w-alphabet
W_off(w₀,b) (R1.5; clean R1.2 + dirty R1.4 steps); per-merge-node
R2.1 handshakes with all 0-direction arrangements (leaf or inner edge
at 0; case III with the R1.5 arrival law gcd(ν_H, μ₀) = 1 ∪ {ν_i});
R2.1(ii) pins (κ̄, X) at any unequal-μ pole pair, then the cell equation
X/κ̄ = dp/dq forces **(dp, dq) = M_G·(d₀, q₀)** (lowest terms) and the
R2.2 shape solve runs exactly: searrow (S), NE m_j·dq < dp, dq ≡ 1 (ν),
κ̄ ∈ ℤ at ν_G ≥ 2, ε/0-chain accounting; root cells die per-edge when
every w ∈ W_i has w ≥ 1 (R2.1 case IV). Inner-merge arrivals keep known
μ_e (used in (S) and w_e > 0) but unknown w_e — never used to kill.
Loop bounds (proved): 0-edge vs equal-(μ,w) partners with μ₀ < μ has
κ̄ > 0 only for ν_H < μw/(μ₀w₀) (finite menu, exhaustive); μ = 1
partners: dq − dp | num(w)·M_G (κ̄ = w·dq/(dq−dp) ∈ ℤ at ν_G ≥ 2, and
the ν_G = 1 family needs dq ∈ (dp, dp·κ̄/(κ̄−w)) ∩ ℤ ≠ ∅ so κ̄ ≤
w(dp+1)), Σm = 0 (dq > dp), ν_G | μ₀ + (dq−dp) − 1, dp ≤ μ₀ + ν_G·Σμ:
all reachable ν_H are enumerated. μ₀ > μ ≥ 2 partners use cap 500 and
return OPEN if undecided — the final run has **zero OPEN cells**.

**RECOUNT (gate: on-axis td=6 unchanged; MP4 sanity PASS; td=7 kill
reproduced mechanically):** of the 2691 step-3 cells,
**2251 DEAD, 440 alive, 0 open**. Per td (alive):
  - **td 7: 0 — CLOSED (prime-td exclusion restored)**;
  - td 8: 3; td 10: 9; td 11: 12 (m2: 2+1, m3: 9) — NOT restored;
  - td 12: 60; td 13: 129 (m2: 4+3+2+3, m3: 10, m4: 107) — NOT
    restored; td 14: 227.
Survivor anatomy (instrumented run): surviving cells are (i) equal-μ
equal-w joins (κ̄ underdetermined at stage R — exactly the cells for an
off-axis rerun of the DS4 jump-cell menu per w ∈ W_off), (ii) nodes
with inner-merge arrivals (w unknown at stage R: needs the merge-child
w-formula w_child = (κ̄_G − X_G/dp_G)/ν_G composed down inter-merge
segments — the natural R1 continuation), and (iii) 14 solver-level
pinned unequal-μ joins that PASS the exact shape solve, e.g.
(μ,w) = (1,2) ⊕ (2,3): (κ̄, X) = (4,2), M = 3, family-I cell
(dp, dq) = (3,6); all type-(iii) survivors carry fully pinned
(κ̄, X, dp, dq, M) — they are the concrete T1-rigidity targets of
R2.3(iii) (solve Prop 8.1(iv) exactly on the pinned cell).

Honesty riders (stage R): inherits R4 superset semantics (alive ≠
existent); the §3 subadditivity census law is now GROUNDED at merges
with dq > dp, ε = 0 and remains a rider when dq < dp (R2.2(D));
MP6-anatomy cells with equal w were NOT deep-solved here (DS4 menu +
suffix machinery not rerun off-axis); λ/budget of NE orbits still
unpriced (R3 unchanged).

## 10. LAMBDA-BUDGET REPAIR — EXECUTED (2026-08-12; St 9.3 (24) pricing
## of the off-axis escapes against the shared St 9.4 budget)

Route (BOOK-OFFAXIS-REVIEW §7/§9.3): the R1.3-R1.5 escapes are the
printed St 9.6-family transitions and carry PRINTED λ-costs; price every
off-axis chain against the shared St 9.4 budget. Machinery consumed:
CONFIRMED R1.0-R1.2 + R2 (review Fronts 1-2), promoted AF2 λ-rule
(SHEET6-AF2 §2, derived from St 9.3 (24) with the E6 sign fix), promoted
H3-psi (SHEET6-H3 §4a), MP2/MP5/MP8, St 8.4, St 9.4 (25)/(26) p. 49.

**P0 (priced step menu — replaces R1.3-R1.5).** At a chain vertex F with
arriving mult l (l | M_parent, St 8.4 p. 42), the full pattern is
p = ⊖η^ε (η^ν−c^ν)^l Π_j (η^ν−d_j^ν)^{m_j}, q = ⊖η·(simple orbits)
(R1.0; ε-extended R1.3 per review §3b: St 9.6(II)(a)+(b) and general-l
analogues; NE laws ε·dq < dp, m_j·dq < dp STRICT — equality is the
root-mult law (R)). Transport (R1.2/R1.4 proportion, l-cancellation):
with E := l·dq − dp > 0 (searrow of the own edge):
    κ̄_F = l·w_G·dq/E ∈ ℤ (ν ≥ 2),  w_F = l·w_G(dq−1)/(νE),
    M_F = gcd(dp, dq).
λ-price of the step (AF2 rule; every extra direction climbs
REGULARITY-FREE since its gap = X_F/mult − κ̄_F > 0 ⟺ NE, X_F = κ̄_F·dp/dq):
    **λ_F ≥ Σ_j max(1, ⌈X_F/m_j − κ̄_F⌉) + [ε ≥ 1]·max(1, ⌈(X_F/ε − κ̄_F)/ν⌉).**
Clean/neutral steps (ε = 0, k = 0) cost 0 (St 9.6(v) is the λ = 0 family).
Finiteness WITHOUT R1.5: (i) extras present (C := l(k+lex) − Sm ≥ 1):
    E | l·num(w_G)·T,  T := Sm + l − ε(1+k+lex) ≥ 1
(T = 0 ⟺ dp = ε·dq, excluded by (R)); so E ≤ l·num(w_G)·T — a finite
Diophantine menu per (w, l), generalizing R1.4's bound; (ii) pure-(b)
(k = lex = Sm = 0, 1 ≤ ε ≤ l−1): C = 0, ν free, but the step COLLAPSES:
    w_F = l·w_G/(l−ε) (expansion), M_F = gcd(l−ε, ν+1) | l−ε,
    λ_F ≥ ⌈l·w_G/ε⌉  (e.g. the review's doubling family: l=2, ε=1,
    λ ≥ ⌈2w⌉ = 3 at w = 3/2; its (7,5) cell is (i) with k=1: λ = 3).
Every non-clean step costs λ ≥ 1, so the St 9.4 budget bounds the number
of non-clean steps: R1.5's refuted finiteness is REPLACED by budget-
boundedness. Sanity (this session, cases/scratch_offaxis_pricing/px2.py):
the complete one-step menu from the td-7 chain-2 state (3/2, 2) is EXACTLY
    (A) (21,15): w → 2/3, M → 3, λ ≥ 2   [printed λ ≥ 2, St 9.6 p. 53]
    (C) (20,16): w → 3/4, M → 4, λ ≥ 2   [printed λ ≥ 2, St 9.6 p. 53]
    ε (7,5):     w → 2,   M → 1, λ ≥ 3   [review §3b / codex λ = 3]
    pure-b:      w → 3,   M → 1, λ ≥ 3   [doubling family]
— the review's four escapes, now all priced.

**P1 (terminal ψ-certificate — H3-psi at the trunk).** Let G be the last
↘-vertex above (0,y) (trunk chain vertex or the merge itself), any shape.
Case IV (Prop 9.3 (k), i-normalized; ρ_G = X_G/dp_G, w_G = (κ̄_G − ρ_G)/ν_G):
    d_F/deg(p_G) = (ρ_G + ν_G − κ̄_G)/ν_G = 1 − w_G,
so H3-psi's R = deg(p_G)/d_F = **1/(1 − w_G)**, shape-independently, and
St 9.4 (25) applies with **ψ = ⌈1/(1−w_G)⌉ − 1**:
    **Σ λ ≤ td − 1 − ψ  over ALL pairwise-distinct ↘-vertices of the
    configuration** (St 9.4's F_i are arbitrary pairwise-different
    elements of V_a ∩ T_a↘ — both chains, all merges and the trunk
    share ONE budget; this is the composition the review §7 prescribed).
Terminal laws: w_G < 1 (R2.1 IV), M_G ≥ 2 (MP2: trunk M ≠ 1), and 9.3(m)
i-normalizes to **j := M_G·(1 − w_G) ∈ ℕ***, i.e. w_G = 1 − j/M_G and
ψ = ⌈M_G/j⌉ − 1. Consequence: terminating NEAR w = 1 is expensive
(w = 2/3: ψ = 2, budget td − 3; w = 3/4: ψ = 3, budget td − 4);
terminating at w ≤ 1/2 keeps ψ = 1 (budget td − 2, = St 9.5).

**P2 (merge pricing).** At a merge cell (R2.2 shape), every NE orbit
prices max(1, ⌈X_G/m_j − κ̄_G⌉) and a FREE 0-root (ε ≥ 1 with no arriving
0-chain) prices max(1, ⌈(X_G/ε − κ̄_G)/ν_G⌉) — same (24) mechanism,
regularity-free (gaps > 0). NE directions cannot lead to poles (all pole
branches arrive as chain edges of the fixed hierarchy), so St 7.3 forces
a T_{a,cv} vertex on them: they are Y(G)-objects. Arriving edges and
q-extras price 0 (MP8 rows). The trunk below the merge starts at
w_tr = (κ̄_G − X_G/dp_G)/ν_G, M = M_G and evolves by P0 (l | M_G).
Review finding 2 fix: arrival mults are μ_e | M_{H_e} of the CURRENT
arriving state (post-jump), not divisors of the entry b_i.
Arrival law (refines R1.5's): an edge of mult μ can leave a chain vertex
of state (w, M) only at a vertex (ν_H, M_H) with μ | M_H, where M_H =
gcd(l, ν_H + 1) at a neutral vertex (l | M) — so **ν_H ≡ −1 (mod μ)** —
or (ν_H, M_H) is the landing cell of the state-creating step itself
(e.g. μ₀ = 3 arrivals at ν_H = 7 direct from the (21,15) (A)-cell), or
the entry (ν_i, μ | b). This kills, e.g., (ν_H, μ₀) = (4, 3): no vertex
with ν = 4 carries M = 3 at w = 2/3 (neutral cells have dq = ν + 1;
resonance from 2/3 needs Δ | 2 — none).

**P3 (td = 7 complete arrangement classification — hand-proved).**
Chain 1 is frozen at (μ, w, M) = (1, 2, 1), λ = 0 (MP5/MP8/DS3; §8 Step 1
unchanged). Chain 2's priced states are P0-closed from (3/2, 2). At the
single merge G (r = 2), with X = κ̄ − 2 from chain-1's case-II handshake:
- Root merge: DEAD (w₁ = 2 ≥ 1, R2.1(iv)) — §8 Step 4 unchanged.
- Chain-1 at 0: needs w₂ = 2ν_{H₁} ≥ 4 (μ₂ = 1) or w₂ > 2 (μ₂ ≥ 2):
  no priced state reaches w > 3, and w = 3 has M = 1 (μ₂ = 1 only): DEAD.
- Unequal-μ non-0 pairs: κ̄ = (μ₂w₂ − 2)/(μ₂ − 1) with X > 0 forces
  w₂ > 2: DEAD (same argument).
- **Class A (equal-(1,2) join)**, chain 2 arrives (1, 2) after the ε-step
  (λ = 3): κ̄ free; realizing cells with Σm = 0 forced (dq > dp since
  X < κ̄): ν_G ≥ 2: dp = 2ν_G, c := dq − dp: ν_G | c − 1, c(κ̄−2) = 4ν_G
  ⟹ (ν_G + 1) | 4: EXACTLY (6,10) M2 (κ̄ = 5, w_tr = 3/2) — codex's cell;
  ν_G = 1 (κ̄ ∈ ℚ legal): dp = 2, dq = 2t: the **(2,2t) M2 tail** (t ≥ 2),
  w_tr = 2 + 1/(t−1); 0-slot variants (case I at ν_G = 1, finding 4) give
  the same cells.
- **Class B (chain-2 at 0, μ₀ = 1, case III, ν_G ≥ 2)**: ν_{H₂}w₂ = 2;
  cheapest state w₂ = 2/3 (λ = 2, ν_H = 3); cells: dp = 1 + ν_G,
  ν_G | c ⟹ ν_G | 2: EXACTLY (3,9) M3 (κ̄ = 3, w_tr = 4/3) and (3,5) M1
  (MP2-dead). This is the review's live cell L1.
- **Class C (chain-2 at 0, μ₀ ≥ 2, case III, ν_G ≥ 2)**: post-jump
  arrivals (the grid never saw these): κ̄ = (μ₀ν_{H₂}w₂ − 2)/(μ₀ − 1)
  pinned; cells dp = μ₀ + ν_G, dq = κ̄dp/(κ̄−2), ν_G | (μ₀ + c − 1):
  FINITE, with κ̄ ≥ 5 ⟹ c ≤ (4μ₀−2)/(κ̄−4), so ν_{H₂} is bounded per
  (μ₀, w₂) — a complete Diophantine menu. (ν_G = 1 would need case I:
  w₂ > 2, dead.)
All class A-C cells carry λ_merge = 0 (Σm = 0, ε = μ₀ arriving: no
climbing extras). The verdict per route: λ_chain2 + λ_trunk ≤ 6 − ψ(w_t)
with P1's terminal laws, trunk priced by P0 (M ≥ 2 throughout, MP2).

**P4 (td = 7 VERDICT: NOT closed — but the two review holes are now
priced, one shut, one survives, and the honest cell set is recut).**
Exhaustive priced adjudication (this session,
cases/scratch_offaxis_pricing/px5.py; engine stage adjudicate_td7();
the class A/B cell lists and the class-C ν₂-bound are the hand-proved
P3 closed forms; the (2,2t) tail is closed by first-step inversion
u | 2dq / u | dq — no caps hit):

- **G2 route (the review's STAR cell) is PRICED OUT.** The ε-step (7,5)
  costs λ = 3 (P0; = codex's λ); the doubling family costs 3 and lands
  M = 1 (dead on any trunk, MP2). The equal-w join then needs the (6,10)
  cell (w_tr = 3/2, M2) or a (2,2t)-tail cell: EVERY completion
  overruns: 3 + 2 = 5 > 4 = 6 − ψ at the ψ = 2 terminals (w_t = 2/3),
  5 > 3 at ψ = 3 (3/4), and ψ = 1 terminals need ≥ 3 more units
  (6 > 5). **Class A + tail: 0 budget-fitting routes.** The review's
  "second, independent reopening" is closed by the printed budget.
- **The review's L2 cell ((6,9) M3 via w₂ = 4/9, μ₀ = 2) is DEAD by the
  corrected transport alone**: 4/9 needed an l = 2 dirty step BELOW the
  M: 2→3 jump — illegal under St 8.4 (l | M); the legal priced closure
  from (3/2, 2) never reaches 4/9 (its λ ≤ 5 states are listed in the
  engine; the review's 3/16, 3/8, 4/9 were l|b-conflation artifacts).
- **G1 route SURVIVES**: class B's (3,9) cell (the review's L1) fits:
  λ = 2 ((A)-step, printed St 9.6 λ ≥ 2) + trunk (4/3, M3) descending
  at λ = 2 (e.g. via the l = 3 cell (35,15): κ̄ 6, gap 1, λ 1, w → 4/5,
  M → 5; then an l = 5 step) to terminals w_t = 2/3 (ψ = 2, total
  4 = 6 − ψ exact) or w_t = 2/5, M 5 (ψ = 1, total 4 ≤ 5, slack 1);
  18 fitting routes on this cell.
- **Post-jump class C opens 61 NEW cells** the grid never enumerated
  (review finding 2: arrival μ₀ | M-state, e.g. μ₀ = 3 after the M→3
  jump). Sharpest: the **(10,15) exact-fit route**: entry → (A)-cell
  (21,15) [λ ≥ 2 printed, w → 2/3, M → 3, ν_H = 7] → arrives μ₀ = 3 at
  the 0-direction of (dp,dq) = (10,15), ν_G = 7, κ̄ = 6, X = 4,
  M_G = 5 → child = (0,y) directly with w_G = 4/5: 9.3(k) d_F/i = 2,
  (m) M(1−w) = 1, R = 5, ψ = 4: budget 6 − 4 = **2 = Σλ**. Every
  printed law is satisfied with EQUALITY in St 9.4 (25); nothing
  printed kills it. Similarly (8,16) (Σλ 2 ≤ 3), (7,21), (5,15), ...
- **Totals: 1689 budget-fitting routes (1713 raw; engine
  adjudicate_td7 = 1713, A/tail = 0, B = 18 — match); 62 distinct
  surviving merge cells as (dp,dq,ν,M)-tuples (1 class-B + 61 class-C,
  over 45 distinct (dp,dq)); minimal total λ = 2.**

**td = 7 verdict: the prime-td exclusion at td = 7 is NOT restored by
the λ-budget** — of the review's two live cells, L2 dies (transport),
L1 survives, the G2/ε reopening dies (budget), but the printed
St 9.6(iii) (A)-jump feeds 61 further budget-fitting case-III cells the
old grid never enumerated. td = 7 stays OPEN, now with an
EXPLICIT finite survivor book: every survivor is a fully pinned
(κ̄, X, dp, dq, ν, M) cell + terminal, i.e. a T1-rigidity target
(R2.3(iii)): the next kill must come from exact Prop 8.1(iv) solves on
the 62 cells (as grok did FOR the (7,5) cell — but these are different
cells), not from budget arithmetic. Honesty: survivors are
superset-alive (alive ≠ existent); Σλ values are LOWER bounds — 1390 of
the 1689 routes fit with EQUALITY (Σλ = td − 1 − ψ), so any new printed
unit of λ anywhere on them (e.g. a positive price for the St 9.6(iii)
child's own 0-direction, or ψ-sharpening k_f > deg p_G) kills them; only
the 299 slack routes are robust to a single extra unit.

**P5 (the full recount, td ≤ 14 — stage R′).** The §9 stage-R recount
(2251 DEAD / 440 alive / 0 open) is VOID: its kills consumed the
refuted W_off alphabet (G1 M-law + missing ε-cells + the l | b
conflation). Under the corrected priced alphabet the honest grid-level
statement, now implemented as stage_rp_census, is:
- the per-pole state set is bounded ONLY by the St 9.4 budget (P0
  replaced R1.5's refuted finiteness by budget-boundedness), and at
  budget td − 2 ≥ 5 it already contains post-jump states of unbounded
  numerator and M (e.g. the (3/2, 2) closure at budget 5 has 70 states
  up to M = 25; b = 3, 5 poles are worse);
- the §9 grid solve's PROVEN loop bounds scale with num(w)·M_G, so no
  completeness certificate exists for any b ≥ 2 entry at any td;
- hence **NO off-axis grid cell is certifiably DEAD at printed tier:
  the recount is 0 DEAD / 0 ALIVE / 2691 OPEN** (superset semantics;
  per-entry rows in the engine output, all CAPPED), and panel decisions
  must come from per-route pricing. Executed for td = 7 (P4: G2 shut,
  62 cells budget-fitting). At td ≥ 8 the budget td − 2 ≥ 6 exceeds
  the ≤ 5-unit cost of the td-7-style escape routes, so budget pricing
  alone cannot close any td ≥ 8 panel — those panels need either the
  T1-rigidity solves or new printed λ/ψ units. td = 11/13 remain open
  (as before the repair), now with the sharper diagnosis that their
  stage-R "12/129 alive" figures were alphabet-artifacts in BOTH
  directions (kills unsound, post-jump cells missing).

**Trust perimeter of §10** (all pre-existing/promoted, no new standing
hypothesis): corrected St 9.3 (24) with the E6 sign fix + St 6.1/6.2 +
Prop 6.7 + St 7.1/7.3 + Not 9.3 (the AF2 rule; gap > 0 parts
regularity-free, ⌈·⌉ rides the St 9.4-proof integrality line); St 9.4
(25)/(26) with H3-psi's chart transport (Lemma 2.1(i)/St 3.12/St 3.17(i)
— pole-count-free, k_f/l_f are root invariants); St 8.4 (l | M); MP2
(trunk M ≠ 1), MP5/MP8 (b = 1 chains free), R1.0-R1.2 + R2 as
review-confirmed; Prop 9.3 (i)-(m) + St 9.2 at terminals. Honesty
riders: (i) per-state λ is the MIN over paths — arrivals through direct
step-cell realizations may under-price (superset-safe: no false kills);
(ii) n_e ∈ ℕ* and i-sync are never used to kill (stage-R policy kept);
(iii) NE-orbit prices use the minimizing mult partition; (iv) the P3
class lists and the (2,2t) tail inversion are td-7-specific proofs —
other panels use the capped generic engine (P5); (v) the arrival law's
"direct" list is a superset (recorded along any in-budget path).

## 11. GENERALIZED ZERO-CHAIN LAW — PROMOTED (2026-08-13): the td-7
## book collapses 62 -> 6

A closed-form decision law for the Prop. 8.1(iv) local rigid solve on
the full 62-cell td-7 class-B/C book (found by GPT-5.6-Sol, proof +
census in xmodel/sol-td7-law.md): with mu = d_p - nu and
l = (d_q-1)/nu - 1, the cell's reduced equation admits an admissible
solution with nonzero RHS constant iff d_p does NOT divide d_q;
equivalently the cell is T1-DEAD iff

    d_p | d_q   <=>   (mu+nu) | (mu(l+1)-1)   <=>   M = d_p
                <=>   kbar in {3,4}.

On-axis ZCH (nu+1)|l is the mu = 1 specialization. Merge arity r = 2
never enters; lambda-data select routes but not this vertex-local
verdict. Dual verification before promotion: (a) zero-shared-reasoning
engine check, 62/62 agreement (xmodel/td7-law-engine-check.md —
independent derivation of the reduced equation
(rho-mu)(t-A)s + (rho-1)nu t s + rho nu t(t-A)s' = C from R1.0, exact
solves over QQ(A) with admissibility C != 0, s(0) != 0, s(A) != 0,
squarefree); (b) Grok hostile audit SOUND, both iff directions +
census + all six survivor substitutions replayed
(xmodel/grok-td7-law-review.md).

RESULT: 56/62 cells DEAD by theorem (class-B (3,9,2,3) + 55 class-C),
removing 1636/1689 deduplicated routes. LIVE: six class-C cells, all
certified LOCAL T1 survivors with explicit admissible solutions —

    (d_p,d_q,nu,M) x mu:  (9,15,7,3)@2  (10,15,7,5)@3  (15,25,8,5)@7
                          (15,25,12,5)@3 (18,27,13,9)@5 (39,65,32,13)@7

carrying 53 routes (35 budget-equality). The 62-cell T1 bash workflow
is superseded; the open td-7 problem is the next tier (transport /
global / coefficient) on these six cells only.
[SUPERSEDED 2026-08-13: this six-cell list is the BOOK-pin
(mixed-reading) census; the E5-corrected re-enumeration replaces it as
the post-E5 book — see §11a.]

ADDENDUM (2026-08-13, dual-certified): the smallest cell (9,15,7,3)@2
PROVABLY SURVIVES the transport tier as well — explicit local solution
passes every filed handshake and both deduplicated budget-equality
completions (case IV at (2/3,3,2); trunk (35,15,7,5) at (2/5,5,1)).
Proof: xmodel/sol-sixcells.md; hostile replay SOUND (exact vertex
substitutions, px5 census, P1 case-IV line-reads, min-cost DAG):
xmodel/grok-sixcells-review.md. Integerized AF2 sharpness proven
(sandwich); the extra-unit contradiction is open (CONJECTURE). The
remaining instrument for the six is the coefficient-gluing tier
(emitter build est. 3-5 days, solve cost unbounded a priori).

### 11a. E5-CORRECTED CENSUS — EXECUTED (2026-08-13): the class-B/C
### menu re-solved under the corrected zero-edge pin; the six-cell
### record is SUPERSEDED (promoted H5a: 17 cells; forced-ν: 2 cells)

Provenance. xmodel/sol-gluing-design.md §2.2 derived the E5 preflight
(I3)-(I5) and claimed a cell-level shrink 6 → 2 by rejecting four
recorded arrivals. The hostile review (xmodel/grok-gluing-preflight-
review.md, VERDICT SOUND-WITH-ERRATA) verified every displayed number
exactly but refuted the shrink at cell level: (I4) contains ν_G, not
the arrival vertex ν_U, so a cell dies only if NO admissible arrival
realizes (I4)=(I5) (finding 1), and the class-C menu was never
re-enumerated under the E5 pin (finding 2). This subsection is that
re-solve: engine cases/td7_census_e5.py (exit 0, gates G1-G5 below all
PASS; px5 machinery — closure, arrival law, feasible/budget — reused
read-only).

The pin. px5.py:244 pinned κ̄ = (μ₀ν_Uw_U − 2)/(μ₀ − 1) from the
ARRIVAL vertex ν_U — the mixed reading that corresponds to neither
Notation 3.5 value. E5 + the chain-1 freeze pin
    κ̄ = (μ₀ν_Gw_U − 2)/(μ₀ − 1)                        (I4)
with ν_U free (any legal vertex). Equivalently: a cell
(d_p,d_q,ν_G,M)@μ₀ with κ̄ = 2d_q/(d_q−d_p) is E5-realizable iff
    w_U^req = (κ̄(μ₀−1) + 2)/(μ₀ν_G)
is a priced state (w_U^req, M_U) of the filed chain-2 closure
(69 states, budget 5) with μ₀ | M_U (St 8.4) and a P2-legal arrival
vertex (neutral ν ≡ −1 (mod μ₀) / direct stored step-cell / entry).
Enumeration is CAP-FREE via the sol-gluing-design (I5a)-(I5d)
inversion (c = d_q−d_p strictly decreasing in ν_G; finite integer
c-window per (μ₀, w_U)): under E5 there is no ν_U to bound, so the
old (μ₀,w₂) ↦ ν₂-bound mechanism (κ̄ ≤ 4μ₀+2) is replaced entirely,
and no guessed cap is introduced. The corrected book's κ̄ values are
{5,6,7} against the six-cell record's {5,6}. Class B (μ₀ = 1): corrected H6
gives ν_Gw_U = 2, and g | c, c | 2(1+g) force ν_G = 2, w_U = 1; the
w = 1 states are priced (λ 4/5) but admit no budget-fitting
completion, so class B is EMPTY even pre-T1 (its only M ≥ 2 cell
(3,9,2,3) was T1-dead anyway).

Unchanged filters, exactly as the §11 book: T1 zero-chain law
(d_p | d_q kills ⟺ κ̄ ∈ {3,4}); N1/L6 primitivity gcd(κ̄,ν_G) = 1
(SHEET6-III:121-129) — previously a passing sanity check on all 62
cells, it NOW BITES: four E5-realizable T1-alive cells die by N1 alone
((14,21,10,7)@4, (22,33,16,11)@6, (30,45,22,15)@8, (38,57,28,19)@10 —
κ̄ = 6, even ν_G); MP2 (M_G ≥ 2); budget via px5.feasible with
λ_pre = closure cost of the arrival state.

**RESULT (promoted H5a/Q-value + E5 — the reading the campaign lives
on): 17 cells, 238 raw routes (202 at equality), 233 deduplicated
(197 eq).**

| cell @ μ₀ | κ̄ | E5 arrival w_U (λ, M_U) | arrival vertices | routes raw(eq) | status |
|---|---:|---|---|---|---|
| `(9,15,7,3)@2` | 5 | `1/2` (4; M2,4) | neutral ν≡1(2) [rec. ν=7 legal] | 4 (4) | kept, arrival unchanged |
| `(10,15,7,5)@3` | 6 | `2/3` (2; M3) | direct (4,3),(7,3) [rec. ν=7]; neutral ν≡2(3) | 47 (29) | kept, arrival unchanged |
| `(15,25,12,5)@3` | 5 | `1/3` (5; M3,6) | neutral ν≡2(3) | 2 (2) | kept, ARRIVAL REPLACED (was `(1/2,ν8)`) |
| `(18,27,13,9)@5` | 6 | `2/5` (3; M5) | direct (2,5),(7,5),(12,5); neutral ν≡4(5) | 37 (33) | kept, ARRIVAL REPLACED (was `(2/15,ν39)`) |
| `(21,35,17,7)@4` | 5 | `1/4` (5; M4,8) | neutral ν≡3(4) | 2 (2) | NEW |
| `(25,35,17,5)@8` | 7 | `3/8` (4; M8) | direct (5,8); neutral ν≡7(8) | 3 (2) | NEW (the only κ̄=7 cell) |
| `(26,39,19,13)@7` | 6 | `2/7` (3; M7) | direct (3,7),(10,7),(17,7); neutral ν≡6(7) | 63 (53) | NEW |
| `(27,45,22,9)@5` | 5 | `1/5` (5; M5,10) | neutral ν≡4(5) | 2 (2) | NEW |
| `(34,51,25,17)@9` | 6 | `2/9` (4; M9) | direct (4,9),(13,9); neutral ν≡8(9) | 18 (17) | NEW |
| `(42,63,31,21)@11` | 6 | `2/11` (4; M11) | direct (5,11),(16,11); neutral ν≡10(11) | 23 (22) | NEW |
| `(50,75,37,25)@13` | 6 | `2/13` (4; M13) | direct (19,13); neutral ν≡12(13) | 31 (30) | NEW |
| `(58,87,43,29)@15` | 6 | `2/15` (5; M15) | direct (7,15),(37,15); neutral | 1 (1) | NEW (family) |
| `(66,99,49,33)@17` | 6 | `2/17` (5; M17) | direct (25,17); neutral | 1 (1) | NEW (family) |
| `(74,111,55,37)@19` | 6 | `2/19` (5; M19) | direct (9,19),(47,19); neutral | 1 (1) | NEW (family) |
| `(82,123,61,41)@21` | 6 | `2/21` (5; M21) | direct (31,21); neutral | 1 (1) | NEW (family) |
| `(90,135,67,45)@23` | 6 | `2/23` (5; M23) | direct (11,23); neutral | 1 (1) | NEW (family) |
| `(98,147,73,49)@25` | 6 | `2/25` (5; M25) | direct (37,25); neutral | 1 (1) | NEW (family) |

The last six rows are the w = 2/(2k+1) family (μ₀ = 15..25 odd,
κ̄ = 6, one exact-fit route each); it TERMINATES at μ₀ = 25 because
the closure contains no state with w ≤ 2/27 at budget 5 —
closure-forced, not a cap.

Diff vs the §11 six-cell record: KEPT unchanged `(9,15,7,3)@2`,
`(10,15,7,5)@3`; KEPT with arrival replaced `(15,25,12,5)@3`,
`(18,27,13,9)@5` (their recorded mixed-engine arrivals fail
(I4)=(I5), exactly as §2.2 proved — but the cells are E5-realizable
through the arrivals above, as the review predicted); REMOVED
`(15,25,8,5)@7` and `(39,65,32,13)@7` (E5-required w_U = 4/7, 1/7
absent from the priced closure — these two cell kills of §2.2 STAND);
ADDED 13 cells. Three further pre-T1 κ̄ = 3 candidates the old book
never had appear and are T1-killed ((37,111,22,37)@15,
(47,141,28,47)@19, (57,171,34,57)@23).

H5a conditionality (both readings executed). Under printed (g)/(h) +
forced ν_G = ν_U — the other coherent reading of the grok-review
trichotomy — the arrival vertex must BE ν_G and be legal: the book is
then EXACTLY **2 cells, `(9,15,7,3)@2` and `(10,15,7,5)@3`, carrying
49 deduplicated routes (31 eq; 51 raw / 33 eq)** — precisely §2.2's
"49/31 (51/33)" filtered-record figures, hereby identified as the
forced-ν book, NOT the E5 book. The two books DIFFER, so the H5a
caveat does NOT evaporate: both books are recorded, and every cell
beyond the two equal-ν passers is conditional on the promoted Q-value
reading of H5a. Under the P-value reading, (H5)/(H6)/(I4) are not
theorems and no zero-edge matching census is derivable at this tier
(St 3.8 also fails as printed): rider only, not enumerated.

Controls and gates (mandatory, engine exits 0): G1 exact replay of the
review's six-row (I3)/(I4)/(I5)/BOOK + X-handshake table on the
recorded arrivals; G2 per-cell E5 re-solve reproduces the review's
finding-1 table exactly (states, λ, routes 4(4)/47(29)/0/2(2)/
37(33)/0, N1); G3 BOOK-pin parity — the engine replays px5's own
class-B/C loops in-engine and reproduces the 62-cell book and the
six-cell 53/35 record; G4 positive controls — `(9,15)@2` and
`(10,15)@3` present with their recorded arrivals in BOTH readings;
G5 negative controls — none of the 56 law-dead cells is alive in
either reading (30 reappear pre-T1 and are re-killed by T1; the other
26, incl. class-B (3,9,2,3), are not E5-realizable at all).

SUPERSESSION AND SCOPE. The §11 six-cell list (53/35 routes) is the
BOOK-pin census and is superseded as the post-E5 record; §2.2's
cell-level "6 → 2" and its 49/31 census are superseded per the review
(the four REJECTs remain true of the recorded arrivals; 49/31 is the
forced-ν book). The open td-7 problem at the next tier
(transport/global/coefficient) is on the 17 promoted-reading cells,
of which 2 are unconditional across the coherent readings. Honesty
riders inherited from §10: survivors are superset-alive (arrival law
is a superset, λ is min over paths — no false kills); route λ values
are lower bounds; the census is conditional on CONJECTURE H5a
(promoted Q-value) + promoted E5 + P3's one-orbit class-B/C
classification, and on the P0-closed reachable-state family at
budget 5 (the closure itself, as in §10). The §11 ADDENDUM transport
result for `(9,15,7,3)@2` is unaffected (equal-ν special case,
arrival unchanged).

Reproduction:

    python3 cases/td7_census_e5.py    # < 1 min, exit 0
    # prints both books, per-cell arrivals/routes, the diff vs §11,
    # and gates G1-G5 (grok replay, E5 re-solve, BOOK parity 62 cells
    # + 53/35, positive controls, negative controls)

## Reproducibility

    cd cases && python3 book_offaxis.py    # ~25 min with stage P, exit 0
    # (full run 2026-08-12: all gates PASS; stage R' 0/0/2691; td-7
    #  adjudication 1713 routes, A/tail 0, B 18, exact-fit 1413, min 2)

Script: cases/book_offaxis.py (additive over book_enum.py, imports its
entries/tdu_rows/set_partitions verbatim; exact integer arithmetic; no
floats). Gates, all mandatory before output: (1) book_enum.gate() —
on-axis td=6 record reproduced unchanged (PASS); (2) MP4 sanity — prime
and β-minimal Λ force b = 1 in tdu_rows (PASS); (3) L6 ≡ N1 equivalence
asserted per entry row; (4) stage-R assert: td=7 cells all DEAD (the §8
kill — kept as a PROVENANCE gate only, superseded by stage P);
(5) NEW gate_review_42: the review-§3a patched pre-pricing state
(W_off(3/2,2) = {3/16,3/8,4/9,2/3,3/4,3/2}; td-7: 4 DEAD / 2 ALIVE)
reproduced in-engine BEFORE pricing (PASS); (6) stage P
(adjudicate_td7 + stage_rp_census) as §10. Session scratch engines
(cases/scratch_offaxis_pricing/px{1,2,5}.py) reproduce the review-patch
gate, the P0 menu/closure, and the P4 survivor book standalone
(px5: 1689 routes, EXIT 0).
