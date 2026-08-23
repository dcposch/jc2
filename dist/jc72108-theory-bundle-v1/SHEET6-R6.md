# SHEET6-R6 — deeper-tower window of the sheet-6 two-pole template (m_{G_m} = 2)

Status: CLOSED AS A PRINT CAMPAIGN (echo-rung session 2026-08-09, §4; engine cases/r6_window.py echo_rung(), all asserts green). NET: 6/9 window cases DEAD (banked, doubly printed-tier); the three open branches ALL SURVIVE the printed tier — (i) (2,3)→(6,17) echo: level-3 W₂-collapse PASSES IDENTICALLY (its 3 conditions are absorbed by the Prop 8.1(iv) ODE pin b = (2/3)(a1+a2), a1a2 = (a1+a2)²/6, s2' = H⁶; deg p_h3@Gm = 195 saturates the L4@Fs bound); (ii) (2,5)→(6,23): same, 267; rung 4 kills every k3 ≥ 2 continuation, forces a FINITE (1,l)-tail (p.20 hierarchy: l's strictly descend) — no death, no infinite recursion; (iii) (1,2): NO k1 = 1 exclusion in print (legality h1⁺ = s1(f⁺)² is pattern-consistent at R/F_s/G_m, vacuous at P) — minimal-reindexed DISJOINT branch, R1 delta-spec written. R6 yields NO further printed-tier kills: R1 label is PER-BRANCH on {minimal (3,4), (1,2), (2,3)-chain, (2,5)-chain}. Prior status (review-corrected partial closure) preserved below.
Mission was: close or characterize the survivors of the
R6 window. Level-0 kills already banked in SHEET6-TEMPLATE.md §3 R6:
(k1,l1)=(1,3) dead (level contradiction), l1 > 3k1 dead (h2-count at pole edges).

## 0. Window sanity check (bounds 4/3 < l1/k1 < 3, integrality 6·l1/k1 ∈ N)

All 8 pass: 4/3 < r < 3 strict, 6r ∈ N, gcd(k1,l1) = 1 (Prop 4.2(i)).
Verified in cases/r6_window.py main(); layer-2 laws L1-L5 + orbit frame are
documented in layer2()'s docstring (page refs; L4 = the p.40 dead-member
mult law, cross-checked EXACT against level-0 E4 (39) and E5 ('pq: 1+1')).

## 1. Per-case ledgers (Q-ladder with m_{G_m}=2, then E3/E4/E5/E6/N1 analogues)

### 1.1 Case (k1,l1) = (2,3) — [VERDICT WITHDRAWN by review front 4; final: SURVIVES-IN-PRINT, see §4]

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

### 1.2 Case (k1,l1) = (2,5) — [VERDICT WITHDRAWN by review front 4; final: SURVIVES-IN-PRINT, see §4]

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
| (1,2)   | 2     | 12      | yes (5(iv))| SURVIVES-IN-PRINT | no k1=1 exclusion; disjoint R1 branch (§4.3) |
| (2,3)   | 3/2   | 9       | yes        | SURVIVES-IN-PRINT | forced echo (6,17); level-3 rung passes (§4.2) |
| (2,5)   | 5/2   | 15      | yes        | SURVIVES-IN-PRINT | forced echo (6,23); level-3 rung passes (§4.2) |
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

## 3. Consequence [rewritten 2026-08-09]

**R6 print campaign CLOSED — three survivors, R1 per-branch.** The six
k1 ∈ {3,6} cases are DEAD (doubly printed-tier, review-confirmed) and
the level-0 kills stand ((1,3); l1 > 3k1), but m_{G_m} = 2 is NOT
eliminated: (2,3), (2,5) (as forced echo chains) and (1,2) survive
every printed-tier test (§4). The two-pole residue-A live structure
set is {minimal (3,4) genome, (1,2) re-indexed, (2,3)-chain,
(2,5)-chain}; R1 (TEMPLATE §4) must run and be labeled per-branch,
with its enumeration extended by the delta-specs in §4.2-4.3.
R1-UNSOLVABLE on all four branches would close the configuration.

## 4. Echo rungs (level 3) and the ninth case — session 2026-08-09

Engine: cases/r6_window.py echo_rung() (additive; layer2() output
unchanged; exact Fraction arithmetic, all asserts green).

### 4.0 Membership at the echo level (Prop 4.2 pp. 19-20, Cor 6.1 p. 32)

m_P = 0 (g first-dead at P; h1, h2, h3 are NON-members at pole edges —
St 3.11(i) only, which legalizes the banked 3→2 and 1-branch leaks);
m_Gm = 2 (h2 first-dead: L4 + Prop 8.1(ii) shape P^{i(mu2-1)}·q);
m_Fs ≥ 3 (strict m-growth: h2 ALIVE at F_s); m_R > m_Fs. Prop 4.2's
proof (p. 20) makes delta_j = kappa(d_F + d_{h_j,F} - alpha_j·d_F - 1
+ u) ∈ N STRICTLY decreasing: every tower is FINITE — an infinite echo
recursion is impossible at any vertex, a priori. mu-recursion ((9),
p. 19): mu_{j+1} = mu_j + (k_j - 1)·l_j/k_j, so mu3 = 3 + 5·(17/6) =
103/6 for (2,3)@(6,17) and 4 + 5·(23/6) = 139/6 for (2,5)@(6,23);
L4 at F_s, root c_m (mult(p_Fs,c_m) = 12): mult(p_h3@Fs, c_m) =
(mu3-1)·12 + 1 = 195 resp. 267 (the rung bounds; generic G_m tops
6·34 = 204 resp. 6·46 = 276, so a ≥ 9-degree, i.e. 3-coefficient,
collapse is demanded).

CORRECTION to the review's derivation (verdicts unchanged): St 8.3(ii)
equality at j = m_child is NOT printed-safe — at level 0 it would read
deg p_h1@Gm = 16 = mult(p_h1@Fs,c_m) = 18, false for the LIVE minimal
genome. The echo forcing is re-derived printed-tier: St 3.11(i) lower
bound 12r2 ≥ deg p_h2@Gm + p. 20 hierarchy r2 < l1 + grid 6r2 ∈ N
(i_Fs·r2 ∈ N, Prop 8.1 proof) + WINNER-CONSISTENCY: for every non-tie
r2 in the menu the f-side wins h3's top at G_m (6r2 > 6mu2 - 1) and
deg p_h3@Gm = 12·l2 > (mu3-1)·12 + 1, killing it. Unique survivors:
r2 = mu2 - 1/6 exactly — (6,17) and (6,23) CONFIRMED forced (and the
same mechanism re-forces (k2,l2) = (3,4) for (1,2), §4.3).

### 4.1 New printed tool: the Prop 8.1(iv) ODE pins q at G_m

delta·p·q' - (1-u)·p'·q = (nonzero const)·p at G_m with the shared
m_Gm = 2 vertex data (i = 2, p = P = (eta³-a1)(eta³-a2), delta = d/i =
3/21, 1-u = 5/21, kappa·u = 16). Consequences (exact, engine-verified):
deg q = deg p·(1-u)/delta = 10 (top cancellation of the ODE — the
review's "deg q = 10 forced by d-arithmetic alone", now with the law
named); P | q; and the polynomial solution is UNIQUE in shape:
  q = H·eta·P·(eta³ - b),  b = (2/3)(a1+a2),  a1·a2 = (a1+a2)²/6,
with a1+a2 = 0 excluded (it would force const = 0). So the pole-orbit
moduli are pinned to a2/a1 = 2 ± √3 already at layer 2, for ALL
m_Gm = 2 survivors — and, cross-check, the level-0 minimal genome's E4
collapse solves to the SAME b and the same orbit relation: the pin is
vertex-structural, not a discriminator. b ∉ {a1,a2} is automatic.

### 4.2 The echo rungs for (2,3)@(6,17) and (2,5)@(6,23): ALL TESTS PASS

(A') Enlarged-family gcds: M*_Fs = gcd(126,189,189,357) = 21 resp.
gcd(126,189,315,483) = 21, i_Fs = 6, m1 = 2 ∈ N — supersedes the
layer-1 "M*_Fs = 63, i_Fs = 2" smell (review nit 6c). G_m side
unchanged: M* = 6, i = 2, mu_i = 1, two-pole orbit fit 3+3 ≤ 6 exact.
(B') Level-2 suffix data: r2 unique (§4.0); mult(p_h2@Fs,c_m) =
6·r2·2 = 34 resp. 46 = deg p_h2@Gm — coherent.
(C'/D') Pole edges, corrected d-arithmetic: d_h2@P = 2/7 = k1·(1/7);
h3's top at P: k2·(2/7) = 12/7 > l2/21 — the h2-side wins, p_h3@P =
(p_h2@P)^6 = (p_h1@P)^12, deg 24, pure power; count: 24 ≤
mult(p_h3@Gm,c_i) = 24+6 = 30 resp. 36+6 = 42. PASS (leaks legal,
m_P = 0).
(RUNG) The 3-coefficient W2-collapse: p_h3@Gm = (P^{e/6·...}q)^6 -
s2'·P-power = P^{24}(q^6 - s2'P^{10}) resp. P^{36}(q^6 - s2'P^{10}) —
the residual q^6 - s2'P^{10} is IDENTICAL for both cases (q is
case-independent, §4.1). Conditions t^20, t^19, t^18 = 0 (t = eta³):
t^20 pins s2' = H^6; t^19 ⟺ b = (2/3)(a1+a2); t^18 ⟺ a1a2 =
(a1+a2)²/6 — the latter two are EXACTLY the ODE pin: identically
satisfied. 3 conditions, 2 unknowns (s2, b), 0 kills: the
overdetermination the review flagged is absorbed by Prop 8.1(iv).
t^17 ≠ 0 (engine): deg p_h3@Gm = 144+51 = 195 resp. 216+51 = 267,
saturating the L4@Fs bound EXACTLY. The rung PASSES.
(E) Rung 4 and termination: a level-4 tie at G_m needs 6r3 = 195/2
resp. 267/2 ∉ N — impossible; for every grid value r3 < l2 (6r3 ∈ N):
f-side winners die (12l3 > (mu4-1)·12+1 ⟺ 12r3 > bound, their own
regime); h3-side winners with k3 ≥ 2 die ((k3-1)(bound - 12r3) > 0);
ONLY k3 = 1 survives, AT EQUALITY, with mu4 = mu3 frozen and
d_h3@Gm unchanged — so the same arithmetic repeats and the chain
continues only through (1, l3), (1, l4), ... with l3 > l4 > ... ∈ N
strictly descending (p. 20 hierarchy r_{j+1} < l_j): the tail is
FINITE (≤ 16 resp. ≤ 22 steps), and delta_j(R) strict descent ends the
tower at a finite m_R regardless. (If instead m_Fs = 3 with the tower
ending there, the branch is just the finite 3-level tower — simpler.)
No rung contradicts; no infinite recursion exists.

VERDICTS: (2,3)-chain and (2,5)-chain SURVIVE-IN-PRINT as finite
forced towers (2,3),(k1,l1),(6,17|6,23),(1,l3),...,(1,l_M). R1
delta-specs — staged G_m depths (units deg/42): (2,3)-chain: 18/42 →
34/42 (P^4·q) → 195/42 (P^24(q^6-H^6P^10), 3-coeff collapse) → finite
(1,l)-tail at equality; (2,5)-chain: 30/42 → 46/42 (P^6·q) → 267/42 →
same tail; both with the §4.1 moduli pin a2/a1 = 2 ± √3, q =
H·eta·P·(eta³ - (2/3)(a1+a2)), s2 = H^6/(transport const).

### 4.3 The ninth case (1,2): no print exclusion — disjoint R1 branch

Prop 4.2(iii) at k1 = 1 reads h1⁺ = s1·(f⁺)² EXACTLY (contributes 0
to mu). Where it bites: only at vertices where the level-1 tie holds,
i.e. where h1 is ALIVE (R, F_s, G_m). There the patterns are pure
powers — p_h1 = p_red^{2i} vs (p_f)² = p_red^{2i} — CONSISTENT, no
contradiction available. At P the tie FAILS (levels 3/21 > 2/21), so
the level-0 nonzero deg-2 pattern p_h1@P = -(3/4)s0·lam³w⁴(eta²-
(4/3)w²) (two simple roots, not a square — the hoped-for killer) is
simply NOT constrained by the k1 = 1 legality: NO exclusion exists in
print; the condition is an R1-tier series constraint. Downstream the
winner-consistency forcing (§4.0) gives r2 = 4/3, (k2,l2) = (3,4):
tower (2,3),(1,2),(3,4),... — the minimal genome re-indexed, with
dead-member data at G_m byte-identical (P·q, deg 16, d = 8/21, same
ODE pin) but a DISJOINT constraint set: d_h1@Gm = 12/21 with quotient
∝ P^4 (vs minimal 8/21, quotient p·q) — mutually exclusive values.
R1 DELTA-SPEC: insert ONE staged resonance level at G_m: 18/21 →
12/21 (h1 stage, quotient const·P^4, legality h1⁺ = s1(f⁺)²) → 8/21
(h2 stage, quotient P·q) → (3,4)-continuation identical to the
minimal genome's L1c layer downstream.

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

Status [historical, superseded — see header + §4]: LAYERS 1+2 BANKED;
R6 CLOSED — R1 decisive for the whole residue-A configuration.

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
