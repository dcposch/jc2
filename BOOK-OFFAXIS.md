# BOOK-OFFAXIS.md — Off-axis (b >= 2) sector adjudication

Mission: adjudicate the off-axis sector flagged by both external reviewers and
the BOOK-ENUM.md closing erratum. The book enumerated only all-b=1 entry
configurations; entries with b_i >= 2 propagate M = b_i down their chains and
can meet in MIXED MERGES (all mu_e >= 2, legal at m >= 3). The prime-td
multi-pole exclusion was retracted pending this adjudication.

Status: COMPLETE + CLOSURE LEMMAS PROVED (2026-08-12, two sessions).
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
- **td 7 (m=2)** [SUPERSEDED by §8: R1 is now proved and the panel is
  CLOSED — exclusion RESTORED]: one off-axis entry survives L6: (2,3),
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
- **R3 (budget silence)**: MP8 transparency does NOT extend off-axis
  (Cor 8.1's M=1 hypothesis; V_{2,a} escape §2(c1)) — but neither is a
  λ ≥ 1 charge proved. Either resolution is progress: transparency ⟹
  suffix budgets stay td−2; a charge ⟹ new kills at small td.
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

## 8. THE td = 7 KILL (R1 + R2 ⟹ prime-td exclusion RESTORED at td = 7)

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

## 9. STAGE-R RECOUNT (engine: cases/book_offaxis.py, additive stage)

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

## Reproducibility

    cd cases && python3 book_offaxis.py    # ~0.2 s, exit 0

Script: cases/book_offaxis.py (additive over book_enum.py, imports its
entries/tdu_rows/set_partitions verbatim; exact integer arithmetic; no
floats). Gates, all mandatory before output: (1) book_enum.gate() —
on-axis td=6 record reproduced unchanged (PASS); (2) MP4 sanity — prime
and β-minimal Λ force b = 1 in tdu_rows (PASS); (3) L6 ≡ N1 equivalence
asserted per entry row; (4) stage-R assert: td=7 cells all DEAD (the §8
kill reproduced mechanically).
