# SHEET6-TDUNIFORM.md — does the kill machinery give a td-uniform single-pole exclusion?

Status: PROMOTED (SHEET6-TDU-REVIEW.md all fronts + sec 10 numeric reconciliation: PRIME THEOREM stands — single-pole excluded at entry for every prime td; authoritative composite survivor table td=4..16: 0/4/16/16/23/71/48/87/212, Sigma-lambda=0 counts -/0/0/2/2/2/4/6/4; C1 namespace fix verified, no further edits). Original status: COMPLETE (2026-08-10, this session; unreviewed). Mission: SHEET6 campaign
generalization — for EVERY td >= 3, decide which single-pole leaf-table
entries are excluded by the promoted kill set (entry-M pin SHEET6-AF3, AF2
pricing SHEET6-AF2, E5/N1 SHEET6-III, psi-budget H3q SHEET6-H3), derive the
general gcd/budget pattern, and state the theorem actually provable.
Ground truth read on-page: papers/sigray_full.pdf pp. 23-28, 45-47 (printed
page = pdf page). Engine: cases/sheet6_campaign.py new additive `tduniform`
stage (existing stages untouched; gate re-run PASS).

VERDICT (headline):
- **The leaf table generalizes in closed form** (§1): single-pole rows at
  every td are exactly (alpha,beta,a,b,nu) with (D,Dg) = a(alpha,beta),
  (deg p, deg p_g) = b(alpha,beta), [nu|alpha & nu|b*beta-1 or nu|beta &
  nu|b*alpha-1], td = a*b*alpha*beta/nu.
- **The entry-M pin is td-uniform and equals b** (§2): M_F =
  gcd(deg p_F, deg p_g,F) = b. Every b=1 row dies at entry (Prop 8.4).
- **Theorem TDU (§6): for every PRIME td, ALL single-pole configurations
  are excluded at entry** — the prime-td leaf table is exactly
  {(alpha,p): alpha | p-1, nu=alpha, a=b=1}, all with M=1. Unconditional
  at the entry layer modulo the AF3 trust perimeter (H1-tier only).
- **The full td-uniform exclusion is FALSE at current kill-set strength**:
  every composite td >= 4 has b >= 2 rows (§3: beta = b*alpha-1 always
  works); every composite td in [6,16] has chain survivors, growing
  4 -> 212 from td=6 to td=16 (§4); a td=9 chain survives ALL promoted
  kills with Sum lambda = 0 (§5, hand-verified) — the BOLD premise
  (forced-spend ~ c*Lambda, c > 1) is REFUTED, budgets are a small-td
  weapon. There is NO finite residual list across td (§7).
- Conditional salvage: promoted set + an H3-strong root lemma (new math)
  would close single-pole for all td <= 9 in addition to all primes (§6).
- The td-uniform bottleneck is now the multi-pole M != 1 analogue of
  Prop 8.4 (§8); with it, the entire §1-§3 arithmetic (incl. prime-PART
  kills) transports to every pole vertex of every configuration.

## 1. The general leaf table (page-cited derivation)

Setting: (f,g) a normalized counterexample of type (alpha,beta) (Not 2.4
p. 9: (k_f,k_g) reduced; Lemma 2.1 => 2 <= alpha < beta, gcd(alpha,beta)=1
by definition of type; alpha >= 2 by Lemma 2.1(iv) k_g/k_f not in N*).
F in T_a,pole with multiplicity data (Not 5.3, p. 26): type, (Dg,D), nu,
(deg p, deg p_g). Write P := deg p_F, Pg := deg p_g,F.

- **(R1) Ratio pin** (St 5.2(i), p. 26; from Prop 5.3(ii)/(vii), p. 25):
  D/Dg = P/Pg = alpha/beta. With gcd(alpha,beta)=1 and D,Dg,P,Pg in N*:
      (D, Dg) = a*(alpha,beta),  (P, Pg) = b*(alpha,beta),  a,b in N*.
- **(R2) nu-menu** (St 5.2(ii), p. 26; from Prop 5.4, p. 26):
      (A) nu | alpha and nu | Pg - 1 = b*beta - 1,   or
      (B) nu | beta  and nu | P  - 1 = b*alpha - 1.
  In particular nu <= beta, gcd(nu, b) = 1, and gcd(nu, beta) = 1 in case
  (A), gcd(nu, alpha) = 1 in case (B) (both from nu | b*(other) - 1).
- **(R3) Lambda and td** (Prop 5.6 (19), p. 27; Prop 5.8 (20), p. 28):
      Lambda(F) = Dg*P/nu = a*b*alpha*beta/nu;   td = sum over T_a,pole.
  SINGLE POLE: Lambda = td exactly. Integrality of Lambda is automatic
  (nu | alpha or nu | beta).
- **(R4) Lower bound** (Prop 5.7, p. 27): Lambda >= beta, so beta <= td.
- Entry Q-datum (St 9.1, p. 48): kap-bar = D + Dg = a*(alpha+beta);
  rho = D/P = a/b; entry nu = nu; pcontent = P = b*alpha.

This is exactly the enumeration behind table (23) (Prop 9.1, pp. 45-47,
re-derived row-by-row by the engine gate for Lambda <= 6): the thesis's
possibility lists "(D,Dg) = (2,3),(4,6),(6,9); (P,Pg) = (2,3),(4,6),(6,9)"
are the a- and b-multiples, and its nu-eliminations are (R2)+(R3).
No other constraint on the multiplicity data is printed anywhere in §5.

## 2. The td-uniform gcd pattern (question (a))

The AF3 pin (SHEET6-AF3.md §1: Not 5.2 + Prop 5.1(i)/(iii) + Prop 4.2
h0 = g + Not 8.1, pp. 19-44 — NOTHING in the chain uses td <= 6 or
|T_a,pole| = 1) gives at every pole vertex
    M_F = gcd(deg p_F, deg p_g,F) = gcd(b*alpha, b*beta) = **b**.
So the gcd pattern of table (23) and its extension to every td is: **the
entry M is the p-side multiplier b, full stop.** Kill (Prop 8.4, p. 44,
needs T_a,pole singleton = single-pole hypothesis): b = 1 => excluded.

Row-by-row at Lambda <= 6 this reproduces SHEET6-AF3 §2 exactly (rows
1,2,3,5,6,7,10,11 have b=1: dead; rows 4,8,9 have b=2,3,2: live).

**Prime td.** Let td = p prime. From (R3), a*b*(alpha/nu)*beta = p in case
(A) resp. a*b*alpha*(beta/nu) = p in case (B), all factors in N*.
- Case (B): alpha >= 2 divides the product, so alpha = p and
  a = b = beta/nu = 1; then nu = beta > alpha = p and nu | b*alpha - 1 =
  p - 1 < p < nu — IMPOSSIBLE. Case (B) contributes no row at all.
- Case (A): beta >= 3 divides the product, so beta = p, a = b = 1,
  alpha = nu, and the only condition left is nu = alpha | b*beta - 1 =
  p - 1. Rows: {(alpha, p) : alpha | p-1, 2 <= alpha < p, nu = alpha,
  a = b = 1}, each with (D,Dg) = (P,Pg) = (alpha,p), Lambda = p.
  (Check td=7: (2,7),(3,7),(6,7) — precisely the campaign's Lambda=7 table
  rows, SHEET6-CAMPAIGN §1.)
All prime-td rows have b = 1, hence M = 1: **entry-dead**.

**Composite td.** E(td) := {rows with b >= 2} is NONEMPTY for every
composite td >= 4: write td = a*b*alpha with b, alpha >= 2 (possible iff
td has a composite divisor iff td composite), take beta := b*alpha - 1
and nu := beta (case (B): nu | beta, nu | b*alpha - 1 trivially;
beta > alpha since alpha*(b-1) > 1; gcd(alpha,beta) = 1 since beta = -1
mod alpha; beta >= 3). So entry-level exclusion is exactly the prime td's.

**N1 refinement** (SHEET6-III, mod H5a): gcd(kap-bar, nu) = 1 at every
nu >= 2 vertex. At the entry, kap-bar = a(alpha+beta) and (R2) gives
alpha+beta == alpha (case B) resp. beta (case A) mod nu, both coprime to
nu; hence **N1 at entry <=> gcd(a, nu) = 1**. (Reproduces the row-3 kill:
a=2, nu=2.)

## 3. E(td): the surviving entry menu

E(td) := {(alpha,beta,a,b,nu) rows with b >= 2} (post-pin). Structure:

- **Arithmetic-progression families.** Fixing (alpha,beta,a,nu) and letting
  b run over the congruence class mod nu makes E a union of progressions;
  each td<=6 live row generates one:
  * row-4 family: (2,3), a=1, nu=3, b == 2 (mod 3), td = 2b in {4,10,16,...};
  * row-8 family: (2,5), a=1, nu=5, b == 3 (mod 5), td = 2b in {6,16,26,36,...};
  * row-9 family: (3,5), a=1, nu=5, b == 2 (mod 5), td = 3b in {6,21,36,...};
  * nu=1 rows (case (A), no congruence): td = a*b*alpha*beta, e.g. (2,3)
    a=1 b=2 nu=1 at td=12 — entries with nu=1 exist at every td in 6N with
    b >= 2;
  * the generic "beta = b*alpha - 1" rows of §2 at every composite td.
- Every entry has Q = (D,P,nu,M,kap) = (a*alpha, b*alpha, nu, b,
  a(alpha+beta)), rho = a/b. Note kap is INDEPENDENT of b: families with
  fixed (alpha,beta,a) keep a bounded kap while M = b and td grow without
  bound — the geometry that defeats the budget (§5).
- Census (scan §4): |rows|, pin-dead (b=1), N1-dead (gcd(a,nu)>1), live:

  td   : 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
  rows : 1 2 2 6 3 5 7 11  3 19  5 10 16 17  4 26  5 26
  pin  : 1 1 2 4 3 2 4  7  3  9  5  8 10  5  4 12  5 13
  N1   : 0 0 0 0 0 0 0  0  0  1  0  0  0  0  0  3  0  0
  live : 0 1 0 2 0 3 3  4  0  9  0  2  6 12  0 11  0 13

  td   : 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
  rows : 24 16  3 38 16 17 16 35  5 64  7 22 24 18 20 79  8 14 22 61
  pin  : 14 10  3 14  9 13  7 17  5 31  7  6 14 12 14 25  8 12 16 21
  N1   :  0  0  0  1  0  0  0  0  0 10  0  0  0  0  0  8  0  0  0  0
  live : 10  6  0 23  7  4  9 18  0 23  0 16 10  6  6 46  0  2  6 40

  Every prime td has live = 0 (the §2 theorem, mechanically re-verified);
  every composite td >= 4 has live >= 1 (§2 construction, ditto).

## 3a. Row counts: no closed finite bound

|E(td)| is a divisor-type function (choices of a*b*alpha*(beta or beta/nu)
factorizations x divisors of b*alpha-1 / b*beta-1); it is unbounded along
smooth td (46 live rows at td=36, 40 at td=40) and 0 exactly at primes.

## 4. Mechanical scan td <= 40 (`tduniform` stage)

Engine (all ADDITIVE; existing stages byte-identical, gates re-run PASS):
- `sheet6_campaign.tdu_rows(td)`: the §1 menu at Lambda = td (sweep bounds
  beta <= td [Prop 5.7], b <= td/alpha, nu <= beta — all certified by §1's
  inequalities). GATE: tdu_rows == prop91 slices for td = 3..7 (asserted).
- `tdu_entry_nodes(td)`: pin (M := gcd(P,Pg) = b, asserted) + N1 filter.
- `tdu_scan(tdmax)`: census + step-1 pricing of every live entry under the
  PROMOTED kill set (hiii_compose.step_e5: E5-III + N1 children + AF2
  derived-IIb pricing, IIB_DERIVED=True; KMAX/BUDGET_CAP lifted from the
  hardwired td=6 value 4 to the actual budget td-2 — the old cap silently
  under-explored III children at budget > 4).
- `tdu_bash(td)`: full compose-style BFS (budget td-2, depth cap 7,
  loop-dedup by shape) + h3_check.iv_dispositions ((l)/(m)/psi tests) on
  every IV hit.
- Engine repairs needed at general td (both pure search-window widenings,
  OPEN -> solved only; pin/iib/gate regressions re-run, byte-identical
  verdicts): lf_mod_reduce q-window +-12 -> +-160 (kap up to 50 at td<=40);
  hiii_compose.BUDGET_CAP module var replacing the literal 4.

Results (2026-08-10 runs; exact arithmetic):
- **Step-1 pricing**: EVERY live entry at every td <= 40 (298 entries) has
  a lambda = 0 first step (IIa_0 with M_F >= 2) inside the solver windows.
  Zero entries are step-1-budget-killable. (At td=6 the free steps exist
  too but lead to chains that die downstream — the td<=6 kills were
  genuinely small-budget phenomena.)
- **Full chain runs** (budget td-2, depth 7):

  | td | live entries | IV-survivor (shape,lam) classes | opens | frontier |
  |----|----|----|----|----|
  | 4  | 1 | **0** (r4 closes: psi-kills, as promoted) | 0 | 0 |
  | 6  | 2 | **4** (the AF3 book, reproduced exactly) | 0 | 0 |
  | 8  | 3 | 16 | 0 | 0 |
  | 9  | 3 | 16 (TWO at Sum lambda = 0, §5 + review C2/§10) | 0 | 0 |
  | 10 | 4 | 23 | 1 kind | 0 |
  | 12 | 9 | 71 | 4 kinds | 1 hit |
  | 14 | 2 | 48 | 2 kinds | 0 |
  | 15 | 6 | 87 | 6 kinds | 2 hits |
  | 16 | 12 | 212 | 24 kinds | 6 hits |

  Growth is monotone-ish in the number of live entries and budget; from
  td = 10 the runs also leave OPEN kinds (unlocked parametric III-E5,
  IIb/IIa_0 aperiodic M_F at mu >= 7 — solver-shape limits, not certified
  kills), and from td = 12 the depth-7 cap is hit (frontier > 0): the
  counts at td >= 12 are LOWER bounds on the surviving book.
- Individual entries CAN close at large td — e.g. td=15 (2,3)a1b5nu2 and
  (2,5)a1b3nu2 (M = 5, 3 with nu = 2: the only mu is odd, and every
  odd-mu cell dies or hits M_F = 1), td=16 (2,15)a1b8nu15 — but at every
  scanned composite td >= 6 except td = 4, at least one entry survives
  with a nonempty IV book.

## 5. Budget asymptotics (question (b)) — the honest negative

The BOLD-mission premise was: forced lambda-spend per chain ~ c*Lambda with
c > 1 would kill all large td. **This is REFUTED, by mechanism, not just by
scan.**

- **Where spend comes from** (AF2/SHEET6-AF2 §2): only EXTRA p-roots (k
  orbits, the IIb 0-root, III's forced second orbit) are priced. The IIa_0
  cell (k = 0: p = (eta^nu_F - c^nu_F)^mu, ALL p-roots in the descending
  orbit) prices at lambda = 0 for ANY l >= 0, i.e. the q-side pattern
  q = eta*q~(eta^nu_F) may carry arbitrarily many extra nu_F-orbits FREE:
  q-roots are not p_F-roots, create no directions (St 3.18 prices
  p-directions only), hence no Y(F)-mass. This is the thesis's own printed
  lambda = 0 move (9.6(v)).
- **Free kap-collapse**: an IIa_0 step sends kap -> kap_F = (kap+n)/nu_G
  where n solves mu*nu_F/((l+1)nu_F+1) = mu(rho+n)/(kap+n). The l-freedom
  makes the reachable kap_F set rich; in particular kap_F < nu_F (case-IV
  capability, Prop 9.3 (j)) is reachable in ONE free step from entries
  with small kap. Since kap = a(alpha+beta) does NOT grow with b (= M =
  td*nu/(a*alpha*beta)), the fixed-(alpha,beta,a) progression families of
  §3 keep entry kap bounded while td -> infinity.
- **The td=9 exhibit** (hand-verified, engine-independent, every promoted
  constraint checked exactly):
      entry (3,4), a=1, b=3, nu=4 [4|4, 4|8; Lambda=9]:
        Q = (3,9,4,3,7), rho = 1/3, M = pin = gcd(9,12) = 3, N1 ok
      --mu=3, IIa_0, l=1, nu_F=4: dp=12, dq=9, ratio 4/3 = 3(1/3+n)/(7+n)
        => n = 5 == -kap (mod 4); kap_F = 12/4 = 3; D_F/i = 4; lambda = 0-->
      child (1/3, 4, 3, 3), M_F = gcd(12,9) = 3, N1 ok
      TERMINAL case IV: (j) 3 < 4; (k) d_F = P(1/3+4-3)/4 = P/3 in N;
        (l) R = 3 > 1; (m) M/R = 1 in N*; psi = 2;
        (25): Sum lambda = 0 <= td-1-psi = 6.  SLACK 6.
  A td = 9 single-pole candidate passes the ENTIRE promoted kill set with
  zero spend and slack 6. No budget refinement (any psi < R bound, any
  ceil upgrade) can touch a Sum-lambda = 0 chain.
- **Forced-spend scaling answer**: the minimum spend to reach a consistent
  IV terminal is O(1) (often 0) on the cheap families, while the budget
  td-2 grows linearly. The inequality points the WRONG WAY and worsens
  with td. The only budget-driven closures are small-td accidents
  (td <= 6: kap-collapse cells happen to be unsolvable or M_F = 1 there;
  at td = 4 every IV hit dies by psi because the budget is 2).

## 6. What is actually provable (theorem + perimeter)

**Theorem TDU (td-uniform single-pole ENTRY exclusion).** Let (f,g) be a
normalized counterexample with a single pole vertex (T_a,pole = {F}),
td := td(f,g) = Lambda(F). Then, with trust perimeter = the printed
statements Prop 4.2 (p. 19), Prop 5.1 (pp. 23-24), Props 5.3-5.8
(pp. 25-28), St 5.2 (p. 26), Not 5.2/5.3/8.1 (pp. 24, 26, 39), Prop 8.4
(p. 44) — the AF3 pin perimeter, all H1-tier; NO H2/H3/H4/H5, no AF2, no
chain analysis:
1. The multiplicity data of F is (D,Dg) = a(alpha,beta), (P,Pg) =
   b(alpha,beta) with the (R2) nu-congruences and td = a*b*alpha*beta/nu;
   and M_F = b.
2. If b = 1, contradiction (Prop 8.4). Hence every single-pole
   configuration with (deg p_F, deg p_g,F) primitive is excluded, at
   every td.
3. **If td is PRIME, every single-pole configuration is excluded**: the
   Lambda = td leaf table is exactly {(alpha,td) : alpha | td-1,
   nu = alpha, a = b = 1}, all with b = 1. (§2 proof; mechanically
   re-verified for the 11 primes <= 40.)
4. [+H5a] gcd(a, nu) = 1.

**Theorem TDU-neg (non-generalization).** The promoted kill set (pin +
N1 + AF2-derived pricing incl. IIb + E5-III + St 9.4/9.5 budgets + H3q
psi/(l)/(m)) does NOT extend TDU beyond the entry layer: for every
composite td in [6,16], the single-pole book has >= 4 surviving
(shape,lambda) classes (§4 table), and the td=9 exhibit (§5) survives
with Sum lambda = 0 — no budget-side sharpening can kill it. td = 4 is
the only composite td that closes outright.

**Corollary TDU-c (conditional closure, td <= 9).** Under the promoted
kill set PLUS H3-strong (a root-vertex lemma killing every
psi-consistent case-IV terminal — AF3 §6 route (ii), the one-place/
Abhyankar-Moh candidate; genuinely new math, not located in print), the
single-pole book is EMPTY for every td <= 9 and every prime td: at
td in {4,6,8,9} ALL survivors are IV-terminal classes with opens = 0 and
frontier = 0. This fails at td >= 10 even conditionally: III-tail opens
(td >= 10) and depth-frontier residue (td >= 12) remain.
[Caveat inherited from SHEET6-H3 §7: SF1 (case-I root terminations) is
outside the modeled kill surface at every td; a one-place-type H3-strong
would plausibly cover it, but that is part of the new math.]

## 7. Residual + honest failure modes (question (c))

Residual after the promoted kill set, per composite td: a FINITE list of
(entry, pre-terminal shape, Sum lambda) classes — every one a
psi/(l)/(m)-consistent case-IV terminal with R = nu/(rho+nu-kap) in
(1, M_G] and M_G/R in N — plus, from td = 10, III-tail OPEN kinds, and
from td = 12, depth-cap frontier. Counts: 4, 16, 16, 23, 71, 48, 87, 212
at td = 6, 8, 9, 10, 12, 14, 15, 16. **The residual is NOT finite across
td**: it grows with the number of live entries (~divisor function) times
the reachable IV-shape count (~budget). There is no finite exceptional
list to treat individually; the mission's hoped-for dichotomy fails.

The failure is structural, and exactly the predicted "large gcd AND cheap
chains" corner:
- **F1 (cheap chains)**: IIa_0 steps with q-side orbit dumps (l >= 1) are
  lambda-free and collapse kap arbitrarily; AF2 prices only p-roots. Any
  kill here needs new mass accounting for q-orbits — nothing in §§6-9 of
  the thesis prices them.
- **F2 (large gcd)**: fixed-(alpha,beta,a) progression families keep
  kap = a(alpha+beta) bounded while M = b -> infinity with td, giving
  ever-richer mu-menus; the pin, which killed 8/9 rows at td <= 6, kills
  a SHRINKING fraction of the leaf table as td grows composite-smooth.
- **F3 (budget direction)**: every budget in the machinery (td-2, (25)'s
  td-1-psi, Cor 7.1's td-1) GROWS with td while psi <= M-1 and forced
  spend stay O(1). Budgets are a small-td weapon only.
- **F4 (solver-shape opens, engine not math)**: unlocked parametric
  III-E5 nodes (concrete-kap entries with parametric children), and
  M_F-aperiodic IIb/IIa_0 cells at mu >= 7, first appear at td >= 10;
  each is per-case closable in principle (SHEET6-III §6.2-style) but
  there are unboundedly many.
- **F5 (SF1)**: case-I root terminations remain unmodeled (inherited).

## 8. The multi-pole frontier this leaves

- Rows exist at every Lambda >= 3 ((2,m) nu=2 for odd m; (m-1,m) nu=m-1
  for even m >= 4), so multi-pole configurations (td = sum of >= 2 row
  Lambdas, parts >= 3, Prop 5.8) exist for EVERY td >= 6 — including all
  primes. After TDU, the ladder at prime td rests ENTIRELY on multi-pole
  configurations; at composite td it rests on multi-pole + the §7
  single-pole residual.
- The pin itself is multi-pole-valid (M_F = b_F per pole vertex — AF3's
  derivation never uses the singleton), but the KILL is not: Prop 8.4
  requires T_a,pole = {G}. A multi-dicritical M != 1 analogue
  (SHEET6-CAMPAIGN §6 item 4, the Domrina-Orevkov-type split) is now THE
  bottleneck for every td: with it, every b=1 pole vertex dies and the
  multi-pole layer would inherit the whole §1-§3 arithmetic (including a
  prime-PART kill: any vertex with Lambda(F) prime is b=1 by §2 and would
  die). Without it, nothing td-uniform is available off the entry layer.
- Partition growth: the number of multi-pole shapes at td is the number
  of partitions of td into parts >= 3 with row-realizable part values =
  all values >= 3 — growing sub-exponentially; the two-pole (3,3) case
  (SHEET6-2POLE) is the smallest instance and still open.

## 9. Reproduction

    cd cases && python3 sheet6_campaign.py gate            # PASS (unchanged)
    python3 sheet6_campaign.py tduniform --tdmax 40        # census + step-1
    python3 sheet6_campaign.py tduniform --td 9            # full chain run
    python3 hiii_compose.py pin                            # regression: td6=4

Engine deltas (all additive): sheet6_campaign.py tdu_rows/tdu_gate/
tdu_entry_nodes/tdu_scan/tdu_bash + CLI phase `tduniform`; lf_mod_reduce
q-window +-160; hiii_compose.py BUDGET_CAP module var (default 4 =
legacy). Regressions re-run this session: campaign gate PASS, tdu gate
PASS (tdu_rows == prop91 slices td 3..7 + prime-td closed form asserted
for the 11 primes <= 40), `pin` grand td3 0/td4 0/td5 0/td6 4 with the
same 4 r9 classes, legacy `hiii_compose.py` baseline grand td3 0/td4 0/
td5 2/td6 13 (both = promoted values). The §4 chain counts were re-run
after the q-window widening for td in {4,6,8,9,10,12,14,15}: all
IDENTICAL (0/4/16/16/23/71/48/87); td=16 is pre-widening (flagged lower
bound). Runtimes: census+step1 to td=40 ~3 min; tdu_bash ~1 s (td<=9) to
~15 min (td=16).

## 10. Post-review numeric reconciliation (2026-08-10, second pass)

Mission: reconcile the three-way td=9 discrepancy — §4's printed 16 vs
the pre-fix CLI's 41 (TDU-REVIEW front 4) vs a reported post-fix "10" —
and state the authoritative survivor table. Numbered 10 (the sheet
already has a §7); this is the "post-review numeric reconciliation".

**Verdict: 16 is correct and the committed post-C1-fix CLI prints it.**
There was never a third engine state producing 10.

- **The three configurations, instrumented.** A debug probe at the
  child_from IIb pricing site (sheet6_campaign.py:249, printing
  `__name__` + the effective IIB_DERIVED + both namespace copies) during
  `--td 9` runs:
  * post-C1-fix CLI (`python3 sheet6_campaign.py tduniform --td 9`):
    site executes in module 'sheet6_campaign', flag True, both copies
    True — 888 IIb pricings — **16 classes**;
  * single-namespace import path (`import sheet6_campaign as sc;
    sc.tdu_bash(9)` — how the original §4 runs were made): flag True —
    888 IIb pricings — **16 classes**, byte-identical output;
  * pre-fix CLI (HEAD~1 file as __main__, module copy flag False): site
    reads False while __main__ holds True (the C1 half-state) — 3048 IIb
    events priced flat-1 — **41 classes**.
  The C1 fix does NOT double-apply pricing: it only sets a flag read at
  one site; the increment is computed once. Hypotheses "fix over-kills"
  and "§4's 16 was itself a half-state" are both REFUTED.
- **The "10" was a display artifact, not a count.** `tdu_bash(td,
  show=10)` prints the header "composed IV-survivor (shape,lam) classes:
  16" and then lists only the first show=10 IVSURV lines (sorted by
  shape-string). Counting printed IVSURV lines (e.g. `grep -c IVSURV`)
  gives 10; and exactly 1 of the 10 visible lines has lam=0 because the
  second Sum-lambda=0 class (2/3,3s+2,3,2s+2) sorts 12th. Both review-F5
  Sum-lambda=0 classes are in the full 16 (verified with show=99).
- **Anatomy of 41 vs 16** (same BFS, traces kept, only the flag toggled):
  41 = 13 shared + 8 re-keys (same shape, under-recorded Sum lambda:
  (1/2,2s+3,2,s+2) and the three (1/2,6s+*,·,·) shapes at 5 instead of
  7; (1/3,4,3,3) at 5,6 and (2/3,3s+2,3,2s+2) at 3,4 — phantom copies of
  the two lam=0 classes reached from OTHER entries via cheap IIb) + 20
  phantom classes whose every path has an under-priced IIb step and dies
  at honest prices. 16 = 13 shared + the 3 re-keyed (1/2,6s+*) shapes at
  their honest lam=7.
- **Three hand-checks of the differing arithmetic** (exact, per the
  SHEET6-AF2 derived rule lambda_IIb >= k*max(1,ceil(gap)) +
  max(1,ceil(gap/nu_F)), gap = D_F/i - kap_F):
  1. OFF-only (1/3,7,3,5)@3 [entry (2,3)a1b3nu2, step mu=3 IIb k=2
     nu_F=3 from (1/3,2,3,5)]: n=5, dp=16, dq=10, kap_F=5, D_F/i=8,
     gap=3 => lambda_IIb = 2*3 + 1 = 7 (legacy printed 1). Chain 7+2=9 >
     td-2=7 ((26)); even alone 7 > td-1-psi = 6 (R=3). Correctly ABSENT
     from the 16. KILL arithmetic right.
  2. Re-key (1/2,6s+3,2,3s+2): step mu=7 IIb k=0 nu_F=6t+3 from
     (1/7,2,7,1): gap=18t+9, gap/nu_F = 3 exactly for all t =>
     lambda_IIb = 3 (not 1). Honest key Sum lambda = 4+0+3 = 7; terminal
     R=2, psi=1, (25): 7 <= 9-1-1 = 7 — SURVIVOR with zero slack. The
     derived price is exactly 3 (no over-charge): survivor arithmetic
     right, OFF's @5 key was under-recorded.
  3. (2/3,3s+2,3,2s+2)@0 [second F5 class]: mu=3 IIa_0 l=0 nu_F=3t+2
     from (1/3,4,3,3): child exact for all t, M_F=3, lambda=0 (k=0, no
     extra p-roots; q-orbits unpriced per AF2/St 3.18); terminal s>=1:
     R=3, (m) M/R=1, psi=2, (25): 0 <= 6. SURVIVOR slack 6. Genuinely
     free — the td=9 book has TWO Sum-lambda=0 classes (C2 adopted).
- **Corrections adopted into this sheet**: §4 td=9 row now reads "two at
  Sum lambda = 0" (review C2); §9's committed-command claim is repaired
  by the C1 fix now in tree (review C3).
- **Authoritative table** (committed post-fix CLI, this pass's re-runs):
  see §4; all nine td values re-run via `python3 sheet6_campaign.py
  tduniform --td N` — results below.

  | td | IV-survivor classes | of which Sum-lambda=0 | open kinds | frontier |
  |----|----|----|----|----|
  | 4  | 0  | -  | 0 | 0 |
  | 6  | 4  | 0  | 0 | 0 |
  | 8  | 16 | 0  | 0 | 0 |
  | 9  | 16 | 2  | 0 | 0 |
  | 10 | 23 | 2  | 1 | 0 |
  | 12 | 71 | 2  | 4 | 1 |
  | 14 | 48 | 4  | 2 | 0 |
  | 15 | 87 | 6  | 6 | 2 |
  | 16 | 212 | 4 | 24 | 6 |

  IV-survivor classes 0/4/16/16/23/71/48/87/212 and frontier
  0/0/0/0/0/1/0/2/6: identical to §4 and to the review's fixed-namespace
  reruns — three independent reproductions of the same table. Sum-lambda
  histograms and this table: /tmp logs of this pass; re-derive any cell
  with `sc.tdu_bash(td, show=999)`. Open kinds are per-entry kinds summed
  over entries (the review's aggregation note). td >= 12 counts remain
  LOWER bounds (frontier > 0), as §4 already flags.

- **Engine state**: cases/sheet6_campaign.py needs NO further edit — the
  C1 fix (flag set on both sys.modules['sheet6_campaign'] and __main__,
  lines 664-671/708-713) is correct and sufficient; instrumentation
  confirms the pricing site reads True under both invocation paths. The
  only residual nit is cosmetic: `show=10` truncates the IVSURV listing
  below the printed count (raise via tdu_bash(td, show=N) if full
  listings are wanted; the count line is always authoritative).
