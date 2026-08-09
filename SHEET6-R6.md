# SHEET6-R6 — deeper-tower window of the sheet-6 two-pole template (m_{G_m} = 2)

Status: PARTIALLY CLOSED, REVIEW-CORRECTED (SHEET6-R6-REVIEW.md: fronts 1-3,6 CONFIRMED; front 4 REFUTED — d_h1@P = 1/7 per the promoted table, (2,3)/(2,5) NOT dead, corrected (D) = k1<=l1 passes whole window; window itself incomplete: ninth case (1,2)). NET: 6/9 DEAD doubly printed-tier; m_Gm>=3 closed by review scope patch; OPEN: (2,3)->forced echo (6,17), (2,5)->forced echo (6,23) [next recursion rung not run], (1,2) = minimal-reindexed DISJOINT R1 branch (needs k1=1 exclusion or R1 enumeration). R1 label: per-branch until the three close.
Mission was: close or characterize the survivors of the
R6 window. Level-0 kills already banked in SHEET6-TEMPLATE.md §3 R6:
(k1,l1)=(1,3) dead (level contradiction), l1 > 3k1 dead (h2-count at pole edges).

## 0. Window sanity check (bounds 4/3 < l1/k1 < 3, integrality 6·l1/k1 ∈ N)

All 8 pass: 4/3 < r < 3 strict, 6r ∈ N, gcd(k1,l1) = 1 (Prop 4.2(i)).
Verified in cases/r6_window.py main(); layer-2 laws L1-L5 + orbit frame are
documented in layer2()'s docstring (page refs; L4 = the p.40 dead-member
mult law, cross-checked EXACT against level-0 E4 (39) and E5 ('pq: 1+1')).

## 1. Per-case ledgers (Q-ladder with m_{G_m}=2, then E3/E4/E5/E6/N1 analogues)

### 1.1 Case (k1,l1) = (2,3) — DEAD (E5-analogue: h2 count at pole edges)

m=2 patterns. G_m (M*=6, i=2; orbit fit forces mu_i=1, p_red = P =
(eta^3-a1)(eta^3-a2), NOTHING else in p_red): p_f = P^2, p_g = (-)P^3,
p_h1 = (-)P^3 (deg 18; h1 repeats g's resonance, (k1,l1) = (k0,l0)),
p_h2 = P^4·q [Prop 8.1(ii): k = i(mu2-1) = 4, mu2 = 3/2 + (k1-1)r = 3],
q ⊇ H·eta^s·P·(eta^3-b)^{m_b}: the b-orbit relocates into h2's pattern
(TEMPLATE §3 R6 note) and mult(q,c_i) = 1 (L4 coherence: 4+1 = 5). F_s
(m>=3): i_Fs ∈ {2,6} (sub-branch by (k2,l2); m1 = 12/i_Fs ∈ N kills
i ∈ {14,18,42,126}); p_h1 = p_red^{i·3/2} deg 189; p_h2 = p_red^{i·r2}.
(ii) St 8.3(ii) h1 suffix EQUALITY: mult(p_h1@Fs,c_m) = i·r·m1 =
r·(i·m1) = r·12 = 18 = deg p_h1@Gm — PASSES as an identity (L2 vertex
transport mult(p_Fs,c_m) = deg p_Gm = 12 + L5). Not the discriminator.
(iii) E5-analogue: h1@P: h0 ALIVE at G_m -> (g+)^2 = s0(f+)^3 transports
-> m_i^2 = s0·lam_i^3 automatic -> pole-ODE z-identity -> p_h1@P =
-(3/4)s0·lam^3·w^4(eta^2-(4/3)w^2), deg 2 <= 2r = 3 OK, d_h1@P = 1/21.
h2@P: levels k1/21 < l1/21 (l1 > k1): f-side wins, p_h2@P =
(-)s1·lam^3(eta^2-w^2)^3, deg 6 EXACT (pure power, no drop possible).
Count (St 3.11 + L4): 6 <= mult(p_h2@Gm,c_i) = (mu2-1)·2+1 = 5: FALSE.
VERDICT: DEAD. Arithmetic: 2·l1 = 6 > 5 = 2·mu2 - 1.
(E4-analogue moot; it would pin deg q = 12(r2-2), minimal q-shape ->
r2 = 17/6 = mu2 - 1/6 — a self-similar genome echo that dies here anyway.)
Premerge-depth-1 escape CLOSED: an intermediate Q_i needs deg p_f@Q =
mult(p_f@Gm,c_i) = 2 -> M*_Q = gcd(2,3) = 1, i_Q = 2 -> p_red,Q deg 1,
single root — St 3.16 (>1 root at non-pole chain vertices) violated.
Merge legs are direct edges G_m -> P_i; the kill stands.

### 1.2 Case (k1,l1) = (2,5) — DEAD (E5-analogue: h2 count at pole edges)

Same structure as 1.1: mu2 = 4, p_h2@Gm = P^6·q (k = 6), p_h1@Gm = (-)P^5
(deg 30 = mult(p_h1@Fs,c_m), (ii) passes as identity); h1@P deg 2 <= 2r=5;
h2@P = (-)s1·lam^5(eta^2-w^2)^5 deg 10 EXACT vs mult(p_h2@Gm,c_i) =
2·mu2-1 = 7: 10 <= 7 FALSE. VERDICT: DEAD (10 > 7). Premerge escape
closed as in 1.1; E4-analogue moot (would force r2 = 23/6).
### 1.3-1.8 Cases (3,5),(3,7),(3,8),(6,11),(6,13),(6,17) — ALL DEAD
### (merge-edge transport infeasible at G_m: i_Gm = 6 vs deg p_f@P = 2)

Shared kill (test A, BEFORE the banked "binding" suffix test can bind):
M*_Gm = gcd(12, 18, 12r) = 2 for all six (12r ∈ {20,28,32,22,26,34},
none ≡ 0 mod 3 or 4 against 6), so i_Gm = 6 and p_f@Gm = p_red^6 with
deg p_red = 2 (Prop 8.1(i)). The merge-edge vertex transport (L2, p.41,
St 3.9+3.16, EXACT) demands mult(p_f@Gm, c_i) = deg p_f@P_i = 2; but
every root mult of p_red^6 lies in 6N: 6·mu_i >= 6 != 2. DEAD.
Equivalent geometric forms (each independently fatal):
  - orbit fit: a pole direction is a full eta^3-orbit factor
    (eta^3-c_i^3)^{mu_i} of p_red (Not/Prop 9.3, 2POLE §2b(2)):
    eta-degree 3·mu_i >= 3 > 2 = deg p_red;
  - deg-2 pattern in eta^s·C[eta^3] must be c·eta^2: SINGLE root,
    St 3.16 (>1 root at non-pole chain vertices) violated;
  - axis escape c_i = 0: one root cannot host two distinct pole
    directions, and pole paths through the axis are excluded (St 7.2);
  - L4 corroboration: mult(p_h2@Gm,c_i) = (mu2-1)·2+1 =
    {26/3, 34/3, 38/3, 61/3, 71/3, 91/3} ∉ N — the merge data cannot
    even be written down.
Robust to premerge depth 1 (TEMPLATE §3 note): the obstruction sits in
G_m's OWN pattern; directions toward any intermediate Q_i need the same
orbit factors in the same deg-2 p_red.
F_s side is clean for all six (i_Fs = 6 forced: M*_Fs | 21 and
m1 = 12/i_Fs ∈ N kill {18,42,126}; p_red,Fs = phi^2·psi-type deg 21,
m1 = 2), and the banked suffix targets are met as identities:
mult(p_h1@Fs, c_m) = 6r·2 = 12r = deg p_h1@Gm ∈ {20,28,32,22,26,34} —
test (ii) PASSES for all six; death is purely at the merge edges.
Had (A) been feasible, the (D)-inequality 2l1 <= 2+2l1-2l1/k1 <=>
l1 <= k1 (TEMPLATE §3's own form, now binding for all l1 > k1 since
d_h1@P = 1/21 is pinned by the m=2 transport) kills them again.

## 2. Summary table

| (k1,l1) | l1/k1 | 6·l1/k1 | in window? | verdict | killing test / genome |
|---------|-------|---------|------------|---------|-----------------------|
| (2,3)   | 3/2   | 9       | yes        | DEAD    | h2@pole count: 6 > 5 = 2·mu2-1 (St 3.11 + p.40 L4) |
| (2,5)   | 5/2   | 15      | yes        | DEAD    | h2@pole count: 10 > 7 = 2·mu2-1 |
| (3,5)   | 5/3   | 10      | yes        | DEAD    | merge transport: i_Gm = 6, mult(p_f@Gm,c_i) ∈ 6N != 2 |
| (3,7)   | 7/3   | 14      | yes        | DEAD    | same (M*_Gm = 2, St 3.9/3.16 + St 3.16) |
| (3,8)   | 8/3   | 16      | yes        | DEAD    | same                  |
| (6,11)  | 11/6  | 11      | yes        | DEAD    | same                  |
| (6,13)  | 13/6  | 13      | yes        | DEAD    | same                  |
| (6,17)  | 17/6  | 17      | yes        | DEAD    | same                  |

Note on the banked "binding test": the St 8.3(ii) h1 suffix EQUALITY
(targets {20,28,32,22,26,34} and 18, 30) PASSES for all 8 as an identity
— mult(p_h1@Fs,c_m) = r·mult(p_Fs,c_m) = r·deg p_Gm = 12r (L2+L5) — so
it is a coherence gate, not the discriminator. The discriminating edge
in R6 is the MERGE edge (the E2-shape count contradiction relocates from
the suffix edge (m=1 story) to the merge edges (m=2 story)).

## 3. Consequence

**R6 CLOSED — R1 decisive for the whole residue-A configuration.**
All 8 window cases are DEAD at layer 2 (no SURVIVES, no
ISOMORPHIC-GENOME: the (2,3) self-similar echo r2 = mu2 - 1/6 dies at
the pole edges before reproducing a genome). Together with the level-0
kills ((1,3) level contradiction; l1 > 3k1 h2-count), the alternative
m_{G_m} = 2 is eliminated entirely: the minimal assignment m_{G_m} = 1
with (k1,l1) = (3,4) (SHEET6-TEMPLATE E3) is FORCED. The two-pole
residue-A configuration has exactly one live genome, and the
template-constrained series experiment R1 (TEMPLATE §4) is now decisive
for the entire configuration.

## Layer-1 ledger (parent session, cases/r6_window.py — mechanical arithmetic)

All 8 window cases pass ladder integrality (deg p_h1 integral at R/F_s/G_m).
Discriminating layer-1 data:
- (2,3), (2,5): M*_Fs = 63, i_Fs = 2 — the SAME geometry E2 killed at m=1
  (16 <= 7 count contradiction shape). Layer-2 check expected fatal, but the
  m>=3 pattern form at F_s must be computed before claiming the kill.
- (3,5),(3,7),(3,8),(6,11),(6,13),(6,17): M*_Fs = 21, i_Fs = 6 (level-0
  geometry); binding test = suffix-edge St 8.3(ii) EQUALITY
  deg p_h1@Gm in {20,28,32,22,26,34} == mult(p_h1@Fs, c_m), plus the
  E4-analogue collapse at the NEW dead level (h3 top at G_m) and the
  E5-analogue pole-edge drops with the m=2 patterns.

LAYER 2 (DONE 2026-08-08, this session; executable checks in
cases/r6_window.py layer2(), all printed): the m=2 pattern forms flip the
expected kill pattern — the "E2-killed geometry smell" cases (2,3),(2,5)
in fact pass the G_m merge geometry (i_Gm = 2, mu_i = 1, level-0-like
p_red = P) and die at the h2 POLE-EDGE count (the p.40 dead-member mult
law 2·mu2 - 1 vs the forced pure-power deg 2·l1; the m=2 transport pins
d_h1@P = 1/21, upgrading TEMPLATE §3's l1 > 3k1 kill to all l1 > k1),
while the six k1 ∈ {3,6} cases (whose banked "binding" suffix equality
passes identically) die one edge EARLIER: M*_Gm = 2 makes the merge-edge
vertex transport mult(p_f@Gm,c_i) = 2 infeasible (i_Gm = 6). Premerge
depth 1 closed off in both shapes (St 3.16 at any intermediate vertex /
obstruction at G_m itself). ALL 8 DEAD; see §1-§3.

Status: LAYERS 1+2 BANKED; R6 CLOSED — R1 decisive for the whole
residue-A configuration.

## Post-review corrections (SHEET6-R6-REVIEW.md, applied)

- (D) corrected: d_h1@P = 1/7 (nonzero deg-2 pattern = no level drop;
  St 3.9(iii) drops d only via mult along steps). h1-side wins h2's pole
  top on the whole window (r < 3): p_h2@P = (p_h1@P)^{k1}, deg 2k1; test
  2k1 <= 2mu2-1 <=> k1 <= l1 PASSES (slack 2(k1-1)(r-1), equality at k1=1).
- Window completeness: independent re-enumeration gives NINE candidates;
  (1,2) was missing from all prior banks. Its layer-2: (A) passes (i=2),
  (D) at equality, suffix equality forces (k2,l2) = (3,4): the minimal
  genome re-indexed (2,3),(1,2),(3,4) — BUT disjoint R1 constraints
  (d_h1@Gm = 12/21, quotient ~ P^4 vs minimal 8/21, quotient pq).
- Echoes forced and OPEN: r2 = mu2 - 1/6 exact => (2,3) -> (6,17),
  (2,5) -> (6,23); the six-case (A) kill does NOT directly apply at the
  echo level (different vertex data, m_Gm = 2 still); next rung required.
- m_Gm >= 3 scope patch (review 5(i), printed-tier): (a) six shapes: M*
  stays <= 2, same kill any depth; (b) (2,3) depth 3: delta_2 window
  empty; (c) (2,5) depth 3: 12r2 in {56,58} => M*_Gm = 2 => six-case kill.
- Cite fix: the six-case kill equality is St 3.17(i) p. 18 (verbatim in
  St 8.3's proof p. 41); decorative St 7.2 miscite removed (weightless).
