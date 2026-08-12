# TEMPLATE-ATTACK.md — the seven rigid templates under the five-angle composite attack (multi-pole book td = 6..14: 27 → 23)

Status: SYNTHESIS (judge-adjudicated), 2026-08-12. Ground: BOOK-BASH.md +
BOOK-BASH-R2.md §§0–3 (the fully adjudicated 22-class/75-instance book, 7
surviving template classes / 27 instances), SHEET6-TEMPLATE.md (genome),
SHEET6-L1.md (§5 rigid solve, §7.2 global layer), SHEET6-CLASSICAL.md,
SHEET6-MULTIPOLE.md (MP0–MP9), SHEET6-DEPTH.md (DS1–DS4), SHEET6-R1.md
(§16–17), SIGRAY-AUDIT.md, thesis refs/sigray_full.pdf. Five angles were
fired at the shared rigid-template mechanism and adversarially reviewed
(3 votes each): **four banked** (Galois/rationality OBSTRUCTION, panel-budget
OBSTRUCTION, classical battery KILL, Weyl-quantization OBSTRUCTION — the
last on a 2–1 split, riders in §6), **one refuted** (L1 §7.2 global
branch-budget sum; §4). All arithmetic exact (int/Fraction); every harness
gated on the promoted td=6 residue-A record (gate PASS in every run); no
repo files modified.

## 0. Verdict

**The live multi-pole book shrinks 27 → 23 instances. Four panel
instances are DEAD by a new, shared, review-confirmed (3 votes)
topological mechanism** — e-ladder primitivity (Def 3.1(ii):
gcd(k̄_V, ν_V) = 1 at every characteristic vertex) composed with the
MP6(b) equal-quotient synchronization (one common i = b_e·α·∏ν_seg
across the r merge edges):

1. **IIa(2,3,1)M2@w4, m=3 td12** — 2-adic i-sync disjointness (pole side
   v₂ = 1 vs cascade side v₂ ≥ 2).
2. **IIa(2,7,1)M2@w4, m=3 td12** — same 2-adic mechanism.
3. **IIa(3,5,1)M3@w2, m=3 td14** — parity disjointness (odd ∏ν at the
   n3-poles vs forced-even via the unique (ν,n) = (2,2) 3→2 contraction
   at the n2-pole; r = m = 3 forces all three at the jump).
4. **ZCH(2,3,2)M2@w6, m=2 td12** — mod-3 vs coprime-to-6 (0-chain needs
   3 | ∏ν by the case-III handshake ν_last·w_last = 6; the s-chain at
   w0 = 6 forces ∏ν coprime to 6; no common i exists).

The same laws prune **7 (2,3)-type a=2,ν=2 pole entries book-wide**
(k̄_P = a(α+β) = 10, gcd(10,2) = 2: pole vertex imprimitive) plus 2
residue-A entries by parity sync — residue-A loses 6 entries across 5
panels without losing a panel; the @w4 m=2 td12 panels survive on
narrowed entry sets.

**Equally load-bearing: three independent shield theorems now delimit
where the closing kill can live.** Galois descent, full-configuration
budget composition, branch/count arithmetic, and vertex-local
quantization are each PROVED to have zero traction against the rigid
templates — the discriminating content of the whole program is pinned to
the coefficient tier at the resonant direction (L1 §7.2: R1 staged
Puiseux transport + R2 x-side cancellation-depth window), and that
target now carries three new exact constraints (§1c). One structural
argument there closes td ≤ 14 multi-pole outright. No new td becomes
fully excluded (td = 7, 11, 13 remain the only ones): residue-A survives
in all 10 of its panels.

## 1. The composite result

### 1a. Kill layer (classical battery; review-confirmed 3/3)

New law **L6** (printed tier, on-page verified): at every characteristic
vertex the e-sequence must drop by exactly ν, forcing
**gcd(k̄_V, ν_V) = 1**, with k̄_P = κ_P(1−π_P) = a(α+β) at poles (Prop
4.1 equality) and k̄ = w(ν+1) at w-conserving segment vertices (DS2,
n = 1). Composed with **L5** (MP6(b)/St 3.17(i)/Prop 8.1(i): common
i = b_e·α·∏ν_seg across merge edges):

- at w = 2, 4 every segment ν is odd; at w = 6 coprime to 6; at w = 3
  the unique one-step 3→2 contraction vertex is (ν,n) = (2,2) — these
  cap-free divisibility invariants produce the four panel kills above
  (exhaustive attach searches confirm within engine caps; the 2-adic /
  mod-3 / parity kills themselves are cap-free given L6);
- the a2ν2-(2,3) pole entry dies outright everywhere (gcd(10,2) = 2).

Zero-slack control: the battery's T2a Jacobian-valuation test is proved
IDENTICALLY equivalent to Prop 4.1 (ord_u f_y = −(d_P + π_P) at a simple
pattern root), so it passes for all seven templates by construction —
the battery kills nothing by accident, and the four kills are genuinely
new content. Engine /tmp/classical6.py, 80 checks, 12 FAIL = the kills;
gate = residue-A td6 + m2td12 mixed entry reproduced cell-for-cell
(common i = 10, cross-pole Ξ = 20 both routes).

### 1b. Shield layer (three negative results, banked)

**(S1) Galois/rationality (74 exact checks, 0 FAIL).** All seven
templates are exactly conjugation-equivariant: τ: √d → −√d (resp. the
S3/S4 orbit action) maps the complete pinned data set onto itself with
pole chains swapped; every swap-invariant forced constant lies in
Q·σ^weight. Forced a priori: the defining laws are polynomial systems
over Q, their solution sets are Galois-stable, and rigidity forces
self-conjugacy up to pole swap. **Galois descent can never kill a rigid
template derived from rational laws.** Census: merge fields Q(√ν) for
the r = 2 cells (disc = σ²/ν); (3,5): irreducible cubic
50t³−50t²+15t−1, Galois S3, one real direction; (4,7): the recorded
quartic re-derived, Galois S4 three independent ways — maximally
generic orbits, no subfield available to any future descent.

**(S2) Panel-budget transparency (28/28 witnesses).** On the all-b=1
axis every object above the jump cell (pole rows, M=1 segments,
resonant contractions, all-μ=1 cascade merges) carries λ = 0 by the MP8
Euler-equality itemization — the R1/R2 suffix budgets td−2 / td−1−ψ
WERE the full-configuration budgets; the stated slacks are real.
Every feeding entry of all 27 instances is b = 1 (b ≥ 2 rows live only
in the off-axis multisets and feed no cell), and "b ≥ 2 forces a second
jump" is unprovable at printed tier (Prop 8.3 propagates only M = 1
downward). Explicit full-configuration witnesses exist for all 28 book
instances of the 7 classes: **composition arithmetic can never kill
these panels.**

**(S3) Quantum vertex transparency (Weyl gauge; 2–1 banked).** Chart
transport is quantum-exact (conjugation by exp(φ(x))); the first
invariant Moyal correction lands exactly 2κ̄_F below every bracket-window
top, and every rigid pinning equation (merge solve, suffix B = (3/2)A,
pole ODE ⊖ = 3λmw⁴, E1–E7 transports) is the top of its own window:
**the seven templates satisfy the quantum vertex equations with
identical coefficients**, and the 48 killed instances die identically in
A₁ (top-level T1 solves, correction-free). Direction of implication
honest: JC₂ ⇒ DC₁ only — this is delimitation, not a kill path.

### 1c. Active data extracted for the remaining layer

1. **Covariance selection rule (S1):** any correctly derived pinned
   datum of the §7.2 layer / R1 transport / per-panel E-ladders must be
   a single rational function evaluated along the direction orbit
   (S3/S4-equivariant for (3,5)/(4,7)), and any swap-invariant forced
   constant must be rational in the scale. Kill-certificate searches may
   be restricted WLOG to the τ-invariant rational subring; a
   non-covariant or irrational-invariant output is an automatic error
   certificate. (Retroactively explains the failed R1 13.1-bracket kill:
   an exact τ-conjugate pair, identically zero.)
2. **Quantum deg-0 datum (S3):** criticality census D_crit =
   D_F + D_g − 3κ̄ makes residue-A@w2 and @w4 (2,3)-entries the UNIQUE
   exactly-critical cells (D_crit = 0); ZCH@w6 is fully
   quantum-transparent (D_crit = −10). At the residue-A merge the
   parameter-free correction V(t) = Π³(f_top, g_top) is degree 9,
   divisible by the pattern p (V(aᵢ) = 0 — the pinned handoffs are not
   charged), and **nonzero exactly at the resonant direction:
   V(b = 2σ/3) = −878σ⁹/9261**. The entire first-order quantum
   divergence concentrates in the deg-0 stratum at b — the same single
   direction as the L1 §7.2 layer. Quantum-R1 = classical-R1 +
   (1/24)p·W: a zero-slack classical closure of §7.2 kills the quantum
   shadow outright, and conversely at (2,3)-critical panels.
3. **Two-jump quarantine narrowed (S2, conditional):** the attainable
   M=1 branch-arrival alphabet across all 10 surviving panels is exactly
   {2,3,4,6}, while five of seven templates emit strictly fractional
   child closures — **all two-jump (mixed-merge) trees die at m = 3**;
   at m = 4, td = 12 the only shape not w-killed is the double-residue-A
   pair-jump joining at w = 3/2, whose unique continuation cell
   IIa(2,5,1)M2 κ̄ = 4 is per-edge consistent (n_e = 7, D/i = 5/2).
   Conditional on extending case-II transport along the emitted M ≥ 2
   chain; μ_e = 2 arrivals stay quarantined.
4. **New coefficient pins for the unrun E-ladders (S2):** IIa l=0
   cascades are T1-rigid — pt = t^r + p₀, c̃ = ρp₀ ≠ 0, forcing
   c_e^{rν} equal across the arriving orbit (r = 2: c₁^ν = −c₂^ν);
   I(ν=1, l=1) forces b = σ/2, c̃ = −disc/6.

## 2. Updated survivor table (per class / per panel)

| class | cell / child | panels before | killed this round | surviving panels (23 total) | entry narrowing / notes |
|---|---|---|---|---|---|
| IIa(2,3,1)M2@w2 residue-A | κ̄5, (5,3,1/2) | 10 | 0 | m=2 td6,8,9,10,12,14; m=3 td9,12,14; m=4 td12 | 6 entries dead across 5 panels (a2ν2-imprimitive ×4: m2td9 e2, m2td12 e3/e4, m3td12 e2; parity-sync ×2); all shields apply; (2,3)-entries exactly quantum-critical |
| IIa(2,3,1)M2@w4 | κ̄10, (10,6,1) | 4 | **m=3 td12** | m=2 td12; m=4 td12; m=2 td14 | m2td12 entries e2/e3 dead (a2ν2); (2,3)-entries quantum-critical (D_crit = 0) |
| IIa(2,7,1)M2@w4 | κ̄11, (11,7,1/2) | 4 | **m=3 td12** | m=2 td12; m=4 td12; m=2 td14 | m2td12 entries e2/e3 dead (a2ν2); super-critical (D_crit = +2) |
| IIa(2,5,1)M2@w3 | κ̄8, (8,5,1/2) | 3 | 0 | m=2 td10,12,14 | passes the full classical battery (i-sync consistent, valid splice, parity); also the unique w = 3/2 two-jump continuation cell |
| IIa(3,5,1)M3@w2 | κ̄7, (7,5,1/3) | 3 | **m=3 td14** | m=3 td12; m=4 td12 | m3td12 entry 2 dead; W-deg-2 lever (§5) now kills 2 panels, not 3; S3 merge orbit, 1 real direction |
| IIa(4,7,1)M4@w2 | κ̄9, (9,7,1/4) | 1 | 0 | m=4 td12 | battery PASS (κ = 42, pairs (3,1)(7,5)(2,13), μ even); 2 OPEN tier-2 μ=3 III-E5 nodes still unresolved; S4 merge orbit |
| ZCH(2,3,2)M2@w6 | κ̄10, (10,4,1) | 2 | **m=2 td12** | m=4 td12 | survives via 3-pole cascade witness (r′=3, ν₁=3, i=18); fully quantum-transparent (D_crit = −10) |

## 3. Census and per-td ledger after this round

    panel      survivors before | killed here | survivors after
    m=2,td= 6         1         |     0       |   1 (residue-A)
    m=2,td= 8         1         |     0       |   1 (residue-A)
    m=2,td= 9         1         |     0       |   1 (residue-A)
    m=3,td= 9         1         |     0       |   1 (residue-A)
    m=2,td=10         2         |     0       |   2
    m=2,td=12         5         |     1       |   4 (residue-A, 231@w4, 271@w4, 251@w3)
    m=3,td=12         4         |     2       |   2 (residue-A, 351@w2)
    m=4,td=12         6         |     0       |   6 (all seven classes' m4 instances)
    m=2,td=14         4         |     0       |   4 (residue-A, 231@w4, 271@w4, 251@w3)
    m=3,td=14         2         |     1       |   1 (residue-A)
    TOTAL            27         |     4       |  23

Book totals: DEAD 48 → **52 of 75**. Per-td multi-pole residue: td6 = 1,
td8 = 1, td9 = 2, td10 = 2, td12 = 15 → **12**, td14 = 6 → **5**.
Fully excluded td: **7, 11, 13 unchanged** (residue-A survives in every
non-empty panel; composite td independently blocked by the TDU
single-pole residual).

## 4. Refuted attempts (one line each)

- **L1 §7.2 global h-branch budget sum** (this round): REFUTED 2–1 —
  the td=6 zero-slack closures (deg h1 = 224 = 168+56, deg h2 = 552 =
  414+138, total x-ray resonance, δ-law) verified by all three referees,
  but the headline corner-erratum was filed against the wrong document
  and the class-universal "no branch-count kill exists" overclaimed past
  the banked records; demoted to unbanked corroboration that the §7.2
  layer is coefficient-tier, not count-tier.
- **Galois descent kill:** structurally impossible — rigid solutions of
  rational laws are self-conjugate up to pole swap (a-priori theorem +
  74 checks); retained as checksum only.
- **Panel-budget squeeze / full-configuration pricing:** empty — MP8
  makes every pre-cell object a zero λ-row; suffix budgets were already
  full budgets (28/28 witnesses).
- **"b ≥ 2 entry forces a second jump":** unprovable at printed tier
  (Prop 8.3 is M=1-only downward) and vacuous on the book axis (all
  feeding entries b = 1).
- **Weyl vertex-tier quantum kill:** zero traction — every rigid solve
  is the top of its bracket window, corrections land 2κ̄ lower.
- **T2a Jacobian-valuation test vs ladder-consistent templates:** no
  kill power — identically Prop 4.1.
- **R1 13.1-bracket kill (prior session):** its bracket sum is an exact
  τ-conjugate pair with zero rational part, identically zero — failure
  now explained, not just observed.

## 5. Errata / adjudications required before the next build

1. **SHEET6-TEMPLATE.md 2c-E5, line 237 vs 239: exact factor 3** in the
   w_i⁴ denominator (81 vs 243), verified at two gauges; the R1 sat rows
   (SHEET6-R1-Q2E5.md §1.5, 729-normalization) sit on the 239 side, and
   §1.3's stray "81·7¹² not 243·7¹²" remark corroborates the conflict.
   Rational and pole-symmetric (Galois-irrelevant) but load-bearing for
   any R1 rerun with E5 quartic rows. ADJUDICATE FIRST.
2. **h2 corner spec discrepancy** ((7/2)(126,42) = (441,147) vs
   (23/7)(126,42) = (414,138)): the arithmetic conflict is real per all
   referees of the refuted angle, but its claimed location was
   misattributed — re-locate the (441,147) spec in the banked R2 window
   documents and adjudicate before staging the window (27 spurious rows
   / 9 spurious columns otherwise).

## 6. Honest riders

1. The Weyl shield (S3) is banked on a 2–1 split; the dissent flagged
   (i) loose wording in the "48 instances die in A₁" corollary against
   the kill book and (ii) one unproven step in the pattern-tier
   cleanness theorem. Its computational core (V(t), criticality census)
   was verified by all three referees, including a full independent
   reimplementation. Treat the deg-0 datum as solid, the theorem-tier
   prose as needing one tightening pass.
2. The classical-battery kills carry the stated caveats: multi-step
   w-contraction routes swept within engine caps (the deciding
   2-adic/mod-3/parity invariants are cap-free given L6); ZCH 0-root
   multiplicity taken at δ = 0 per the book's own dp-accounting;
   hierarchy panels with sub-jump merges marked ALIVE conservatively.
3. Claim 1c.3 (two-jump narrowing) is conditional on case-II/handshake
   transport along the emitted M ≥ 2 chain; μ_e = 2-arrival
   normalization remains quarantined — the perimeter is narrowed, not
   closed.
4. Survival remains superset-sound (P-realizability untracked); the
   per-direction E5/E6 context ladders for (2,5), (2,7), (3,5), (4,7)
   are still UNRUN — the covariance rule of 1c.1 is a falsifiable
   checksum on those future runs.

## 7. The sharpest remaining frontier — and the next step

**Frontier.** The shared mechanism is now triangulated from three
independent directions: the closing kill cannot be descent (S1), cannot
be composition/budget arithmetic (S2), cannot be vertex-local — classical
or quantum (S3, plus the whole T1–T4 record) — and (unbanked but
thrice-verified) is not a branch-count identity at infinity. What
remains is exactly the **L1 §7.2 global layer in its coefficient-tier
form: the R1 staged Puiseux transport and the R2 x-side
cancellation-depth window of h1 at the resonant direction b = 2σ/3**,
where (i) the R1 mod-p program has already killed one witness family at
depth 84 (SHEET6-R1 §17, strong-evidence tier), (ii) the quantum
divergence concentrates with explicit nonzero inhomogeneity
V(b) = −878σ⁹/9261, and (iii) the covariance rule cuts the search space
to the τ-invariant rational subring with a built-in error certificate.
A kill there at td=6 propagates by frame-homogeneity to all 10
residue-A panels and to the @w4 classes sharing the merge solve — and
with the (3,5,1) lever below, to effectively the whole book.

**Concrete next step (one sequenced session):**
1. Adjudicate erratum §5.1 (E5 factor 3) — blocking, pure arithmetic.
2. Re-locate and fix the h2 corner spec (§5.2).
3. Build the R2 h1 x-side window for the td=6 gate panel: the 70
   staged cancellation-depth columns at the undisputed h1 corner
   (56,168), exact arithmetic mod p at depth 84, restricted WLOG to the
   τ-invariant rational subring, targeting the resonant-direction
   column block; monitor with the covariance checksum (any
   non-covariant pinned output = error certificate). A rank deficit in
   the b-block is the kill.

**Secondary lever (cheap, parallel):** the IIa(3,5,1)M3@w2 TEMPLATE-
genome run — its W-residual sits at deg 2 vs the residue-A-pattern
demand deg ≤ 1; a per-panel absolute κ-ladder through the μ=3, ν_F=1
first suffix vertex demanding deg ≤ 1 kills both remaining (3,5,1)
panels at once (m=3 and m=4, td12), shrinking the book to 21 and
emptying the S3-orbit class.

Artifacts (session, outside repo): /tmp/galois_audit/{audit,covariance}.py,
/tmp/panel_squeeze.py, /tmp/classical6.py (+ /tmp/c6_full.log),
/tmp/qvertex2.py, /tmp/qvertex3.py, /tmp/qcensus.py,
/tmp/global_h1_sum.py (refuted-angle record, retained for salvage).
Repo grounds read-only throughout.