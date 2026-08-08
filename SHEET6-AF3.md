# SHEET6-AF3.md — the entry-M sanction, decided (campaign §6 item 6)

Status: COMPLETE + PROMOTED (SHEET6-A3L1-REVIEW.md: pin airtight, all gcds re-derived, kill-hunt negative) (2026-08-07, this session). Target: SHEET6-CAMPAIGN.md §6
item 6 (AF3 entry-M menu), the last conditionality on the single-pole td=6
book. Ground truth read on-page: papers/sigray_full.pdf (printed page = pdf
page). Engine: cases/hiii_compose.py new additive `pin` mode (existing `iib`
mode and both gates unchanged and re-run: PASS).

VERDICT (headline): **AF3 as formulated is REFUTED — and its refutation
CLOSES the sanction question while KEEPING the 4 classes.** The thesis's
entry rule is not a menu at all: at every pole vertex, M_F **equals**
gcd(deg p_F, deg p_g,F) (the "M-pin", §1 — the same Not 8.1 + Prop 5.1(iii)
argument as SHEET6-A2P-REVIEW front 7(c)/SHEET6-2POLE §2d, which transports
verbatim; single-pole entries ARE pole vertices). The pin agrees with AF3's
M | gcd(D,P) at row 4 only — the one row the thesis works, whence the
false "row-4 usage" pedigree. At the two live td=6 rows they DISAGREE:
r8 pin = 3 (AF3 said 2), r9 pin = 2 (AF3 said 3). The 4 residual classes
ride r9/M2 — the pinned value. So route (a) inverts: the superset classes
are not ill-formed; they are the unique thesis-consistent entries. Route
(b) (§4-§5): all four survive every located printed statement; the two R=4
classes sit at exact budget boundary. **Final single-pole td=6 residual =
4 classes, now UNCONDITIONAL at the entry layer** (§6). Consolation prizes:
td≤5 rows 1,5,7,10 and td6 rows 2,3,6,11 die AT ENTRY (M=1 vs Prop 8.4),
closing G3's mathematical content and making the td≤5 sanctioned residual 0
independent of AF2 (§3).

## 1. The M-pin at pole vertices (page-cited derivation)

Claim (AF3′): for every F ∈ T_a,pole of a normalized counterexample,

    M_F = gcd(deg p_F, deg p_g,F)   — an equality, not a divisor menu.

Chain, all printed statements:
1. T_a,pole := {F_P* : P ∈ R̄_a \ R_a} ∩ T_a+ (Not 5.2, p. 24), where
   F_P* := I_P(u) with u as in Prop 5.1 (Not 5.1, p. 24).
2. Prop 5.1(i)/(iii) (pp. 23-24): m_{F} = 0 for F = I_P(u*) at every
   u* ≥ u; in particular m_{F_P*} = 0. (m_F is the Prop 4.2 invariant of
   the vertex; intrinsic, not ray-dependent.)
3. Prop 4.2 (p. 19), for F ∈ T_a+: h_0 = g, and the family h_0,…,h_{m_F}
   uniquely defined. With m_F = 0 the family is exactly {h_0} = {g}.
4. Not 8.1 (p. 39): M_F := gcd(deg p_F, deg p_{h_0,F},…,deg p_{h_m,F}).
   With m = 0: M_F = gcd(deg p_F, deg p_{g,F}). ∎
5. Both gcd arguments are PRINTED per row in table (23) (p. 46), which
   lists (deg(p_F), deg(p_g,F)) for all 11 rows at Λ ≤ 6.

Nothing in 1-4 uses |T_a,pole| = 1 or 2: the A2P front-7(c) "pole pin" and
this "row-entry pin" are the same statement. The single-pole chain entry
F_0 is the pole vertex itself (Prop 9.2, p. 50; entry Q per St 9.1, p. 48),
so the entry M is pinned. Kill usage (M=1 ⇒ dead) additionally needs
Prop 8.4 (p. 44, requires T_a,pole = {G}) — available in every single-pole
configuration by definition.

Trust perimeter: Prop 4.2 + Prop 5.1 + Not 8.1 + Prop 9.1's table — all
inside the campaign's standing H1-tier trust. One cite-slip found in Prop
5.1's proof (§7, E8): "By Proposition 8" should read "by (8)" (Prop 4.1's
dichotomy, p. 18); the proof is otherwise sound (monotone ρ argument).

## 2. Row-by-row consequences (table (23) p. 46 → pinned M)

| row | type | (D,Dg) | (deg p, deg p_g) | ν | Λ | pinned M | fate at entry |
|----|------|--------|------------------|---|---|----------|----------------|
| 1  | (2,3)| (2,3)  | (2,3)  | 2 | 3 | 1 | DEAD (Prop 8.4) [single-pole td3] |
| 2  | (2,3)| (2,3)  | (2,3)  | 1 | 6 | 1 | DEAD (was: ψ-killed) |
| 3  | (2,3)| (4,6)  | (2,3)  | 2 | 6 | 1 | DEAD (was: N1) |
| 4  | (2,3)| (2,3)  | (4,6)  | 3 | 4 | **2** | = St 9.6's hypothesis M=2 (p. 51) ✓ |
| 5  | (3,4)| (3,4)  | (3,4)  | 3 | 4 | 1 | DEAD |
| 6  | (3,4)| (3,4)  | (3,4)  | 2 | 6 | 1 | DEAD |
| 7  | (2,5)| (2,5)  | (2,5)  | 2 | 5 | 1 | DEAD |
| 8  | (2,5)| (2,5)  | (6,15) | 5 | 6 | **3** | live; chain closes (0 survivors) |
| 9  | (3,5)| (3,5)  | (6,10) | 5 | 6 | **2** | live; carries the 4 classes |
| 10 | (4,5)| (4,5)  | (4,5)  | 4 | 5 | 1 | DEAD (r10/M4 td5 residuals VACUOUS) |
| 11 | (5,6)| (5,6)  | (5,6)  | 5 | 6 | 1 | DEAD |

(row labels follow pilot numbering. Values confirm A2P
front 7(c) exactly; the (2,3)-rows' gcd(2,3)=1 also matches 2POLE §2d.)

AF3 refutation in detail: AF3 sanctioned M | gcd(D_F, deg p_F) and the
superset ran M | deg p_F. Against the pin: at r8 AF3's menu is {2} but the
truth is 3 (a SANCTIONED config was spurious); at r9 AF3's menu is {3} but
the truth is 2 (the TRUE entry was ext-only — this is why the superset run
"found" the 4 classes). No printed statement anywhere derives entry M from
(D, deg p); the only printed entry-M mechanism is Not 8.1, i.e. the pin.
The row-4 agreement gcd(2,4) = 2 = gcd(4,6) is coincidence. Downstream
menu note: the first-step root multiplicity obeys μ | M_pin (St 8.4,
p. 42), so r9 forces μ=2 first steps (μ=1 is the M_F=1 kill) — exactly the
routes the 4 classes use.

## 3. Pinned recomposition (engine `pin` mode, additive)

`python3 cases/hiii_compose.py pin` (asserts pin values against the
engine's Prop 9.1 table, itself gate-checked against (23); IIB_DERIVED
default as per A2P fix 1):

- td=3: r1 entry-dead. **0 classes.**
- td=4: r5 entry-dead; r4/Mpin2 runs 5 IV hits, 0 survivors. **0.**
- td=5: r7, r10 entry-dead — no entry even starts. **0.** The td≤5
  sanctioned residual (2 classes on r10/M4) is now killed at ENTRY,
  independently of SHEET6-AF2's derived-IIb kill (doubly covered; A2P
  front 7(c)(i) adjudicated in the kill direction).
- td=6: r2, r3, r6, r11 entry-dead; r8/Mpin3: 0 IV hits, 0 opens, 0
  frontier; r9/Mpin2: 8 IV hits → **4 survivor (shape,λ) classes** (same
  four as `iib`'s AF3-ext book; the r9/M6 and r8/M6 duplicates die with
  their entries). Grand: td3 0, td4 0, td5 0, **td6 4**.

G3 closure (new): the thesis's silence on rows 1,5,7,10 is mathematically
benign — pin + Prop 8.4 kills them with no chain analysis. §9's row-4-only
treatment is thereby COMPLETE for td ≤ 5 at the row-selection layer
(the thesis still never prints this argument: G3 stands as a presentation
gap only, no longer a mathematical one). Same at td=6: rows 2,3,6,11 die
at entry, so any future printed td=6 bash needs chain analysis for rows
8,9 only.

## 4. The four classes — identity and per-class verdict

All four live on the forced entry Q(F_0) = (D,P,ν,M,κ̄) = (3,6,5,2,8)
(row 9; ρ = 1/2). A hypothetical carrier is a normalized counterexample of
GLOBAL type (3,5) (Not 2.4 p. 9 + Not 5.3(i) p. 26: the (α,β) in (23) is
the type of (f,g), so (k_g,l_g) = (5/3)(k_f,l_f) at the root). Shapes are
(ρ, ν, M, κ̄) at the last pre-terminal vertex; R := deg p_G/d_F at the
case-IV step; ψ = ceil(R)−1; budget = td−1−ψ (St 9.4 (25), p. 49).

| # | class (shape@Σλ) | route from entry | R | ψ | budget | verdict |
|---|------------------|------------------|---|---|--------|---------|
| 1 | (1/3, ν=7, M=3, κ̄=5)@2 | μ=2 IIa_k k=1 (λ≥2) | 3 | 2 | 3 | **SURVIVES, slack 1** |
| 2 | (1/4, ν=5, M=4, κ̄=4)@2 | μ=2 IIa_k k=2 (λ≥2) | 4 | 3 | 2 | **SURVIVES, slack 0 (boundary)** |
| 3 | (2/3, ν=3s+2, M=3, κ̄=2s+2)@2 | class-1 node + μ=3 IIa_0 (λ≥0), s-family | 3 | 2 | 3 | **SURVIVES, slack 1** |
| 4 | (3/4, ν=4s+3, M=4, κ̄=3s+3)@2 | class-2 node + μ=4 IIa_0 (λ≥0), s-family | 4 | 3 | 2 | **SURVIVES, slack 0 (boundary)** |

These are the thesis's own four IV-terminal shapes (St 9.6(iii)/(iv) nodes
and their 9.7(iv)/9.9-type s-children, pp. 51-58) reached from the r9
entry at td=6 budgets. Checks passed by all four (engine + hand): Prop 9.3
(k)/(l)/(m) at the terminal ((m) evaluates to 1 ∈ N in all four); ψ-budget
at ψ = ceil(R)−1; N1 (H5a) at every ν ≥ 2 vertex; E5-priced III (none on
the surviving routes); AF2 derived-IIb pricing (none on the routes: pure
IIa); μ | M at each step; M ≠ 1 along the chain INCLUDING the terminal:
by St 8.5 (p. 42; applicable since case IV has (0,y) ∉ V_2,a) M_{(0,y)}
divides M_G, and Prop 8.4 (p. 44 — (0,y) ∈ T_a& ∩ V_a) forbids 1, forcing
M_{(0,y)} = 3 (classes 1,3) resp. ∈ {2,4} (classes 2,4) — satisfiable,
adds only divisibility on k_f.

Entry realizability (new, positive): the pinned r9 entry exists at the
pattern layer. Prop 5.3(iii)/(v)/(vi) + Prop 5.4(ii) (pp. 24-26) force,
up to units, p = η(η⁵−A), p_g = B(η¹⁰ − (5/3)Aη⁵ + (5/9)A²) (A,B ≠ 0):
then 3pp_g′ − 5p′p_g = (25/9)A³B (constant ✓), both squarefree, coprime,
Prop 5.4(ii) parity (e,e_g) = (1,0) — the unique admissible parity (e_g=5
puts a common root at 0 vs (vi); e_g=10 violates (v)). A one-parameter
family, exactly analogous to SHEET6-L1's coefficient-level checks. The
residual is NOT vacuous at the leaf-pattern layer.

## 5. Kill attempts on the four (route (b)) — all negative, documented

- **ψ-upgrade via root-count at (0,y)**: if p_{(0,y)} had ≥ 2 distinct
  roots, St 3.17 (p. 18) would give k_f = deg p_{(0,y)} > mult(p_{(0,y)},c)
  = deg p_G = R·l_f strictly, licensing ψ = R and killing classes 2,4
  (budget 1 < 2). BLOCKED: St 3.16 (p. 17) explicitly EXCLUDES (0,y) from
  the root-count↔V_{1,a}∪V_{2,a} equivalence; worse, case IV's hypothesis
  (0,y) ∉ V_{1,a} ∪ V_{2,a} points (if 3.16 extended) at a SINGLE root,
  i.e. k_f = R·l_f exactly and ψ = ceil(R)−1 is sharp. No printed upgrade.
- **λ_{(0,y)} ≥ 1**: would kill 2,4 (2+1 > 2); λ_root ≥ 2 would kill all
  four. NOT derivable: St 9.4's proof (p. 49) charges the root's x-branch
  cv-mass AS the ψ term (G ∈ T_a,cv ∩ T_a,x with κ_G(π(G)−1) ≥ ψ, then
  Cor 7.1) — the ψ-budget IS the located root-branch charge, already
  counted. A further charge needs a second cv-branch at the root; no
  printed statement produces one (and case IV's ∉V_2,a militates against).
  This is HIII-REVIEW "WHAT WOULD CLOSE (b)", still open.
- **Root-data/global-type arithmetic**: type (3,5) forces 3 | l_f, 3 | k_f,
  l_f < k_f (Thm 6.1 p. 28), k_f ≥ R·l_f from the terminal; d_F = l_f =
  P_G/R propagates back to j-divisibility on the entry unit (3 | j′ for
  classes 1,3; 2 | j′-type for 2,4) — constraints, not contradictions.
- **Prop 8.4/8.5 at the terminal**: see §4 — consistent, no kill.
- Conclusion: SHEET6-H3 §4b's finding extends verbatim to td=6: a
  ψ-consistent case-IV terminal is killed by NO located printed statement.

## 6. Final single-pole td=6 statement

**Single-pole td=6 residual = exactly the 4 classes of §4, on the forced
entry r9 Q=(3,6,5,2,8) of a type-(3,5) normalized counterexample — now
UNCONDITIONAL at the entry layer** (the AF3 conditionality is resolved:
no sanction hypothesis remains in the stack; standing hypotheses now
{H1, H2, H4, AF2-derivation, H5a/b} + proved H3q/ψ-budget). All other
single-pole configurations at every td ≤ 6 are entry-dead (pin + Prop 8.4)
or chain-closed (r4/M2, r8/M3). SF1 residual stays 0 (its last class rode
r8/M6, now entry-dead — doubly covered with AF2's kill). Two-pole (3,3)
unaffected (Prop 8.4 unavailable there; see SHEET6-2POLE §2d/SHEET6-L1).

What would close the four: (i) a second-cv-branch-at-root lemma
(λ_root ≥ 1: kills 2,4; ≥ 2: kills all); (ii) an Abhyankar-Moh/one-place
argument at a single-rooted p_{(0,y)} (= H3-strong; kills every IV
terminal); (iii) coefficient-level (Prop 8.1(iv) ODE) analysis of the
μ=2 IIa_k patterns over the §4 entry family, L1-style. All genuine new
math; none located in print.

## 7. Corrections and errata banked

- **CAMPAIGN §2/§6-item-6 amendment**: "M-menu per AF3: M | deg p_F
  (thesis-sanctioned subset: M | gcd(D,P))" is wrong in both directions;
  replace by the pin (§1). HIII-REVIEW's "13 AF3-superset classes (vanish
  if AF3's sanction is proved)" and AF2 §5's "4 classes (r9/M2 ∪ r9/M6)"
  carry the same moot conditionality: the pinned book is r9/M2 alone.
- **A2P front 7(c)**: adjudicated — all three consequences (i)-(iii)
  CONFIRMED (r10 vacuous; r8→M3, r9→M2, book stays 4; 2POLE residue-B
  entry kill), now derived rather than observed.
- **E8 (thesis, p. 24, cosmetic)**: Prop 5.1's proof cites "Proposition 8"
  twice; no such proposition exists — read "(8)" (Prop 4.1, p. 18).
- **E9 (thesis, Not 9.3, p. 49 — definition/usage mismatch)**: Y(F) as
  printed puts every H ∈ T_a,cv on a ray through EVERY ancestor of H (all
  rays pass I_P(0) = (0,y)), so Σλ_{F_i} would double-count and (25) would
  fail as stated. Every §9 usage (and St 9.4's own proof via Cor 7.1,
  which needs a plain cv-subset) requires the branch-at-F reading: λ_F =
  cv-mass of branches leaving the characteristic path at F. This is the
  campaign's H2 reading; flagged because the pin argument's neighbors
  (St 9.4/9.5) lean on it.
- Engine: hiii_compose.py `pin` mode + PIN_EXPECT assertion table
  (additive; `iib` output byte-identical; both gates PASS).

## 8. Reproduction

    cd cases && python3 sheet6_campaign.py gate     # PASS (unchanged)
    python3 hiii_compose.py iib                     # unchanged: td6: 4
    python3 hiii_compose.py pin                     # pinned entries:
                                                    # td3 0, td4 0, td5 0,
                                                    # td6 4 (r9/Mpin2)

Exact arithmetic throughout; pdf pages cited = printed pages.
