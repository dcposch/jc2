# SOL-ALGEBRAIZATION-REVIEW.md — Adversarial review of SOL-ALGEBRAIZATION.md + cases/sol_algebraization.py

Reviewer: Claude (adversarial pass, 2026-08-12). Status: COMPLETE.
Scope: (1) the claimed E5 erratum (TEMPLATE 2c-E5 line 239, 243 vs 729)
and its blast radius across the promoted TEMPLATE record, template_lift,
the R1 cores, the (2,5)/(2,3) chain gates, and TEMPLATE-ATTACK; (2) the
16,443 x 5,461 depth-5,481 Hermite--Pade matrix construction and its
exact certificates; (3) the "no uniform kill" scope statement; (4)
cross-model second referee (Grok) on the E5 factor.  Review-owned
tools: /tmp/e5_exact.py (from-scratch exact adjudication over
Q(sqrt3)[c]/(c^3-a_i), no repo imports, no hand constants trusted),
/tmp/xe5_grok.out (Grok brief + verdict), reruns of the engine's bank /
validate / rank / wiedemann modes on this machine.

Verdicts:
- E5 erratum: **CONFIRMED — Sol is right, TEMPLATE line 239 is wrong by
  exactly a factor 3.** The unsolved transport equation (line 237) is
  correct; its exact solution is w_i^4 = -4 H_M (a_i-b) / (243 s0 S_M^3
  (a1-a2)^4 a_i^2 c_i); the printed -(4/3)/243 = -4/729 is 1/3 of the
  true value.  Adjudicated by a from-scratch exact recomputation (90/90
  checks, sec 1.2) with an INDEPENDENT anchor (the E6 h2-cube identity
  pins the disputed LHS constant 9), and by Grok as second referee
  (concurs: 243, sec 1.5).
- Blast radius: **the wrong 729 row is live in the banked R1 saturation
  systems (r1_q0_gate.py, r1_q2_screen.py, r1_12_sat.py corr rows) but
  flips NO banked verdict** — in every such system H_M/H12 is a fresh
  unit-saturated variable occurring only in the E5/E6-tie rows, so the
  factor is absorbed by a unit rescale; the kill/survival mechanisms
  used only H_M != 0 / s1F != 0.  Smoking gun found: the banked
  "E5-pinned HM" values 71495 / 19010 are EXACTLY 3x Sol's corrected
  H_M = 58944 / 41561 mod both primes (sec 2.2).  template_lift's 46
  checks, the chain gates, the quantum V(b), and the Direction-B strike
  never consume the constant.  TEMPLATE-ATTACK sec 5.1's "ADJUDICATE
  FIRST" demand is hereby discharged on the 243 side.
- Matrix: **CONFIRMED.**  Construction, compression, and certificate
  logic verified line-by-line; dense hash-tail rank reproduced exactly
  (5461/5461, nullity 0, 48.5 s at p=29401); the full exact Wiedemann
  certificate at p=105337 regenerated on this machine and asserted
  byte-identical against the bank (degree 5461, det 30914, both
  SHA-256 hashes).
- Scope statement: **CONFIRMED, and if anything still generous to the
  method** (a dimension-count heuristic says depth-limited rank-drop
  completions are EXPECTED to exist in the unconstrained tail space,
  sec 4.2).  The pilot kills no R1/R2 sub-locus (sec 4.3).
- Promotion: **PROMOTE** the fixed-completion obstruction + the E5
  erratum as banked exact results; template-wide verdict stays
  INCONCLUSIVE exactly as the document itself says.

## 1. Front 1 — the E5 factor (adjudicated: 243)

### 1.1 The dispute, stated exactly

TEMPLATE 2c-E5 displays (all constants at issue):

    lam_i = 9 S_M c_i^4 (a_i-a_j)^2                          (line ~232)
    9 H_M c_i^5 (a1-a2)^2 (a_i-b) = -(3/4) s0 lam_i^3 w_i^4  (line 237)
    w_i^4 = -(4/3) H_M (a_i-b)/(243 s0 S_M^3 (a1-a2)^4 a_i^2 c_i)  (line 239)

lam_i^3 = 729 S_M^3 c_i^12 (a1-a2)^6, so line 237 solves to numerical
prefactor 9 / ((3/4)*729) = 36/2187 = **4/243**, with c_i^7 = a_i^2 c_i.
Line 239's -(4/3)/243 = -4/729 is exactly 1/3 of that.  Lines 237 and
239 are mutually inconsistent; the question is which one is the typo.

### 1.2 From-scratch adjudication (review-owned, exact)

/tmp/e5_exact.py rebuilds everything from the section-1b pattern
definitions plus St 3.9(ii) only, in exact arithmetic over
K = Q(sqrt3), L = K[c]/(c^3 - a_i), with eta and w fully symbolic
(bivariate polynomials over L) — none of the constants 9/27/243/729 is
assumed anywhere; Taylor coefficients are computed by raw binomial
expansion.  Three rational specializations x both poles, 90 checks,
**90 PASS**:

- multiplicities at c_i: 2/3/2/6 for p, p_g, p_h1, p_h2 — as claimed;
- lam_i = 9 S_M c_i^4 (a_i-a_j)^2 and m_i = 27 G_M c_i^6 (a_i-a_j)^3
  (the St 3.9(ii) transports) — recomputed, correct;
- order-2 Taylor coefficient of p_h1,Gm at c_i = 9 H_M c_i^5
  (a1-a2)^2 (a_i-b): **the LHS constant of line 237 is 9, correct**;
- the pole top m_i^2 eta^2 (eta^2-(3/2)w^2)^2 - s0 lam_i^3
  (eta^2-w^2)^3 drops to degree 2 with eta^2-coefficient exactly
  -(3/4) s0 lam_i^3 w^4 and constant s0 lam_i^3 w^6 (z-identity):
  **the RHS of line 237 is correct**;
- cross-multiplied solution test: the 243-candidate satisfies line 237
  exactly; the printed 729-candidate does NOT (both poles, all
  specializations).

### 1.3 The independent anchor (why this is not circular)

An internally-consistent-but-wrong constant would pass self-checks, so
the LHS constant 9 needs an anchor outside the E5 chain.  It has one:
E6's h2-lead transport requires [9 H_M c_i^5 (a1-a2)^2 (a_i-b)]^3 to
equal the order-6 Taylor coefficient of p_h2,Gm at c_i, which reduces
to the closed identity 27 a_i (a_i-b)^3 = sigma^3 (a_i - (3/4)sigma) —
verified exactly over Q(sqrt3) (both sides sigma^4(2 sqrt3-3)/12 at
a_1), and machine-verified in template_lift.py check family 9.  If the
LHS constant were K != 9, the reduced identity would be
K^3 a_i (a_i-b)^3 = 27 sigma^3 (a_i-b2), which FAILS for K != 9.  My
engine re-verifies h1t^3 == [6-Taylor of p_h2,Gm] as a raw polynomial
identity (no reduction step trusted).  So the promoted (F_i) identity
itself pins line 237, and line 239 is the typo.  Given line 237, the
solve is forced arithmetic: 243.

### 1.4 Answer to "who is wrong"

- TEMPLATE line 239: **wrong** (prints 1/3 of the true w_i^4).
- TEMPLATE line 237 + all structural E5 content (z-identity,
  m_i^2 = s0 lam_i^3 automatic, deg-2 drop, solvability): **correct**.
- Sol's erratum as stated in SOL-ALGEBRAIZATION.md 2.2 (cleared-row
  coefficient 243, printed line smaller by 3): **correct**.  One nit:
  the displayed solved formula in 2.2 omits s0 from the denominator
  (harmless in the s0 = 1 gauge used everywhere downstream, but 2.2 is
  phrased as a general erratum; TEMPLATE line 239 carries s0).
- "The same typo in some older R1 saturation code": **confirmed and
  sharpened** — the R1 rows are not an independent typo, they are the
  faithful clearing of the wrong line 239 (4(a_i-b)H_M +
  729 S_M^3 (a1-a2)^4 a_i^2 alpha_i W_i^4 = 0 is exactly line 239
  cross-multiplied).  SHEET6-R1-Q2E5.md 1.4 "hand-verified against
  TEMPLATE 2c-E5. Correct." verified consistency WITH THE TYPO — a
  clean example of the self-check trap this review was told to expect.

### 1.5 Second referee

Grok (timeout 2400, self-contained brief with both candidates,
/tmp/xe5_brief.txt -> /tmp/xe5_grok.out): rederives the order-2 Taylor
coefficient (constant 9 confirmed), the z-identity, the solve
(9/((3/4)*729) = 4/243 shown explicitly), and check 4 (the E6 anchor
identity holds exactly at a_1).  Verdict: "cleared-row constant 243,
Candidate B [Sol] wins."  Two referees + one exact machine derivation,
zero dissent.

## 2. Front 1b — blast radius

### 2.1 Where the constant does NOT enter (verified by reading + grep)

- **template_lift.py (the promoted TEMPLATE record's 46 checks):** E5
  is checked as (i) the z-identity, (ii) m_i^2 = s0 lam_i^3 automatic,
  (iii) SOLVABILITY only ("a_i - b != 0 both poles (w_i^4 pinned,
  nonzero)", line 301).  The printed value of line 239 is never
  machine-verified — which is exactly how the typo survived promotion.
  The 46 checks and every E1-E7 verdict are constant-insensitive.
  TEMPLATE needs a one-line erratum on line 239, nothing else.
- **(2,5)/(2,3) chain gates (r1_chain_sat.py):** phase inventory
  PROVES no E5-analogue row exists on the chains (f is the only
  count-exact member at the chain pole edges); the only E5-adjacent
  input is "pole lead -(3/4) s0 lam_i^3 w_i^4 vanishes iff w_i = 0" —
  nonvanishing only, factor-free.  Corroborated at GB level: in the
  banked (2,5) core GB (SHEET6-R1-25LOCUS.md sec 2) W1/W2 occur ONLY
  in the radical rows 3W_i^2-2HW_i^2.  Unaffected.
- **TEMPLATE-ATTACK quantum V(b):** V(t) = Pi^3(f_top, g_top) is built
  from the merge patterns; V(b) = -878 sigma^9/9261 never consumes
  w_i^4's normalization (grep: 243/729 appear in TEMPLATE-ATTACK.md
  only inside its own sec 5.1 erratum demand).  Unaffected.
- **directionb_strike.py (committed dc0918b, mid-session):** the
  Row_20 kill uses the ratio-pin inconsistency + "w_i^4 != 0"
  (solvability tier).  The committed file contains no 729 constant.
  (An uncommitted intermediate seen early in this session carried a
  729-based `want` comparison; it was dropped before commit.)
  Unaffected.
- **sol_algebraization.py itself:** the matrix consumes only alpha_i,
  beta, w_1, w_2; H_M/H_F/s1 are metadata.  The w_1^4/w_2^4 ratio
  -(9-5r3)alpha2/((9+5r3)alpha1) is constant-free (verified: it equals
  (a_1-b)a_2^2 alpha_2/((a_2-b)a_1^2 alpha_1) by the exact Q(sqrt3)
  identity (5-3r3)(9+5r3) = -(9-5r3)(5+3r3) = -2 r3... both
  cross-products = -2 sqrt3).  So even the E5-side of the pilot's rank
  results is erratum-proof; only the reported H_M/H_F/s1 values depend
  on 243, and those are now the correct ones.

### 2.2 Where the WRONG 729 row is live, and why no verdict flips

The banked R1 saturation layer carries line 239's clearing verbatim:

- r1_q0_gate.py e5e6_rows (Q0-SAT, sec 18.1; also the fam object,
  lines 537/552/887): row 4(a_i-b)HM + 729 S_M^3 (a1-a2)^4 a_i^2
  alpha_i W_i^4 = 0.
- r1_q2_screen.py (Q2 screen rows, lines 578/913): same 729
  normalization (the stratum-13 characteristic-zero-header `[1]` trace
  contains these rows; it is not a Q proof).
- r1_12_sat.py phase corr (SHEET6-R1-Q2E5.md 1.5, the "corrected"
  (1,2) rows) and phase_minsat (cW = 729*7^36*144): same.

**Smoking gun** (numerical, both primes): Q0-SAT's banked "E5-pinned
HM" is 71495 (p=105337) and 19010 (p=105673); Sol's corrected values
are 58944 and 41561.  Exactly 3*58944 = 176832 = 71495 + 105337 and
3*41561 = 124683 = 19010 + 105673.  Same witness W_i, same primes,
ratio exactly 3 — the predicted corruption, observed in the bank.

Why no banked verdict flips (checked per system):

- **Q0-SAT / fam / Q2:** HM enters ONLY via the two E5 rows and the
  E6 cube tie 2^24 HM^3 = 7^48 s1F^3; s1F is Rabinowitsch-saturated.
  Replacing 729 by 243 rescales the pinned (HM, s1F) by 1/3 —
  still nonzero.  The banked kill mechanism at the kill frontier is
  "quotient rows force s1F = 0" vs "tie rows force s1F != 0 (W_i
  units)" (SHEET6-R1.md 19.2, re-verified by SHEET6-R1-Q2E5.md): both
  arms are invariant under the rescale, since 3 is a unit in char 0
  and at both primes.  EMPTY stays EMPTY, NONEMPTY stays NONEMPTY.
  (Rigor note: the 729- and 243-ideals are not literally equal, and
  the banked GB certificates certify the 729-ideal; the transfer is
  the two-line unit-rescale argument above.  A 1-second re-emission
  with 243 would make the bank self-contained — recommended, not
  blocking.)
- **(1,2) corr systems (r1_12sat_corr*.ms):** H12 occurs only in the
  two E5-shaped rows + H12*tH12-1, s1 in no row; H12 -> H12/3 is an
  exact bijection of solution sets.  NONEMPTY verdicts stand.
- **Banked numerics:** the .rows.txt comment values "E5-pinned HM =
  71495/19010" and the implied s1F are 3x (resp. 3x) the true ones —
  cosmetic corruption; flag for the next R1 emission pass.

Bottom line: the erratum is load-bearing for any FUTURE quantitative
use of H_M/w_i^4 (exactly as TEMPLATE-ATTACK sec 5.1 warned), but no
banked kill or survival changes.  SHEET6-R1.md's gauge-section k_i
formula (line ~84, numerator -(4/3), denominator a_i^3-form) inherits
the same factor-3 and should be corrected to -4 alongside line 239.

## 3. Front 2 — the matrix

### 3.1 Construction (read line-by-line; all checks pass)

- Support/depth bookkeeping: 43*127 = 5461 columns, N = 5481, shift
  1764 = 42^2, rows 3*5481 = 16443, dense entry count 16443*5461 =
  89,795,223 — all consistent with TEMPLATE lines 61-64/325-330.
- Entry formula M = [T^(n-1764+42i)] Y_r^j: correct clearing of
  F(x,y)|_{x=T^-42, y=Y_r} by T^1764 (max pole 42i <= 1764).
- **Conjugacy compression is legitimate:** at conjugate k the entry is
  [T^(n-1764+42i)] Y_r(zeta^k T)^j = zeta^(k(n-1764+42i)) * (base), and
  zeta^42 = 1 with 42 | 1764 and 42 | 42i kills all but zeta^(kn):
  conjugate rows at fixed n are unit multiples of the representative
  row.  Rank equivalence of the 126-series system with the compressed
  16443-row system holds exactly as stated.
- The j = 0 guard rows: column (i, 0) is nonzero ONLY in row
  n = 1764-42i (entry 1); in particular column (42, 0) lives only in
  row n = 0 — the documented boundary-kernel trap from dropping orders
  0..19 is real, and the half-open window [0, 5481) is the correct fix.
  rank_sanity() covers the shift/sign conventions.
- Obstruction logic: a genuine f-a of the template is monic-in-y of
  y-degree 126 with exactly these 126 Puiseux branches, hence vanishes
  identically on each series; full column rank at depth 5481 therefore
  excludes any nonzero F on the prescribed support for THAT completion.
  Sound.  (A depth-5481 kernel vector would conversely be necessary,
  not sufficient — reconstruction would still need all-orders checking,
  which the pre-registration correctly anticipated.)
- Specialization direction: stated CORRECTLY in sec 4 — full rank at a
  sample is Zariski-open, so it proves generic full rank on any
  component through the point; algebraization lives in the
  complementary CLOSED determinantal locus, which samples cannot
  empty.  The document does not overclaim (and explicitly refuses the
  "template dies" reading).  This is the right direction for an
  obstruction-only bank.
- Certificate logic: scalar Krylov minpoly | minpoly(B) | charpoly(B),
  all deg <= 5461; BM degree EXACTLY 5461 with 0 recurrence failures
  over the full 10,922-window forces minpoly = charpoly, constant term
  = -det(B) (odd n), det != 0 => B = M^T D M invertible => ker M = 0.
  One-sidedness correctly stated (projection can only lose degree).
  D's weights are drawn in [1, p-1]: genuinely nonzero.  Sound.

### 3.2 Reproduction on this machine

- `--mode bank` + `--mode validate`: PASS (validate additionally
  asserts the corrected-E5 rows vanish at the dense-pilot points; the
  printed-729 residuals are nonzero — 27424/16684 at p=29401,
  253/76368 at p=80557 — i.e. the pilot points visibly violate the
  printed line and satisfy the corrected one).
- `--mode rank --prime 29401` (dense sha256-tail completion):
  rank 5461/5461, nullity 0, blocks P1/P2/B = 5203/258/0, **48.5 s** —
  matches the banked claim (~49 s).
- `--mode wiedemann --prime 105337` (the paper's main certificate,
  sparse completion): regenerated in ~825 s; degree 5461/5461,
  det(M^T D M) = 30914, failures 0, adjoint 38015, and BOTH SHA-256
  hashes (Krylov sequence + recurrence) asserted equal to the bank by
  the engine's own regression gate.  Full independent regeneration.

### 3.3 Nits (non-blocking)

- SPARSE_STATS_BANK (census) and NORM_GUARD_BANK (orbit-norm/Toeplitz
  guard, the 8841x43 tail matrix) are bank-only constants: no engine
  mode regenerates them.  The main certificate does not depend on
  them, but the guard's "independent algebraic factorization" claim is
  currently reproduce-by-trust.  Recommend a --mode normguard in the
  next engine pass.
- The two completions (sparse w1-least-root and sha256-tail) are
  per-prime objects; "the stated completion" is really one completion
  per prime.  The document's phrasing ("an explicitly documented
  completion") is acceptable but could say this outright.
- The B-side one-orbit choice and the B-tail contact bookkeeping
  (4*56/42 + 57/42 = 281/42, e_B = 1: arithmetic checks) are honestly
  flagged as added choices.  Confirmed.

## 4. Front 3 — the scope statement

### 4.1 "No saturated depth-5481 locus exists" — TRUE

TEMPLATE 1c/1d pins the pole generators through slot 37 (seven
dead-stretch coefficients free ON the stated grids, off-grid prefix
zero) and the B-side through slot 12 only; sec 4 lists "B-side/x-side
tail data" among the unknowns and sec 3 R1 keeps the sub-pattern tails
as open conditions.  Nothing in the promoted record constructs tails
to slot 5,480; the banked R1 objects reach the ~slot-60 band tier.
The requested "saturated residue-A locus at depth 5,481" is genuinely
not a defined object.  The refusal to trigger the pre-registered
uniform verdict is correct, and sec 4's statement of what a uniform
kill would require (1 in I_sat,N + I_5461(M)) is the right algebra.

### 4.2 What a uniform version would cost (review addition)

Tails-as-unknowns sizing: 2*5443 pole tails + 5468 B tails ~ 16,354
unknowns; entries of M become polynomials of degree up to 126 in them;
a uniform kill needs the unit-ideal certificate over the (not yet
constructed) saturated ideal.  Heuristic but instructive: the corank-1
locus of a generic 16443x5461 matrix has codimension 10,983, far BELOW
the ~16.4k-dimensional tail space — on naive dimension grounds one
EXPECTS a large rank-drop sub-variety of completions (and the sha256
completion sits at distance 2 checks from it in spirit only).  So
"uniform full rank over ALL completions" was never a plausible
outcome; only the R1-saturated sub-locus (codimension large, size
unknown) could clear it.  Consequence: the decisive object really is
the staged R1 ladder (TEMPLATE sec 4), not a deeper Hermite-Pade
sample — the document's own conclusion, reached here independently.

### 4.3 Does the pilot kill any actual R1/R2 sub-locus? NO

The sparse completion (all stretches zero, pole tails zero past slot
37, B tail delta_56+delta_57) satisfies the pinned prefix genome and
corrected E5, but no R1 band/quotient/cancellation-depth condition was
imposed on or verified for its tails; the concurrent Direction-B
strike (dc0918b, unreviewed) in fact claims zero-window-tail shapes
are J-row-inconsistent, which would place this completion OFF the
eventual jet locus entirely.  The banked content is exactly what the
document says: a full-rank obstruction for two explicit completions
(plus two hash-tail completions), i.e. "the currently-pinned genome
data alone does not force algebraizability" — a generic obstruction
and a working depth-5481 exact-HP engine, not a locus kill.  The
"banked exact result" line is correctly scoped.

## 5. Cross-model referee

Grok, run per protocol on a self-contained two-candidate brief:
constant 9 on the LHS of the transport, cleared-row constant 243,
candidate B (Sol) correct, E6 sanity identity verified at a_1.
Concurs with the review's exact derivation on every sub-question.
Artifacts: /tmp/xe5_brief.txt, /tmp/xe5_grok.out.

## 6. Recommendations

1. PROMOTE SOL-ALGEBRAIZATION.md as banked (fixed-completion
   obstruction + E5 erratum), keeping its own INCONCLUSIVE
   template-wide verdict verbatim.
2. Add the erratum to SHEET6-TEMPLATE.md line 239 (-(4/3) -> -4, i.e.
   cleared constant 243) and to SHEET6-R1.md's k_i gauge formula;
   correct the "E5-pinned HM" comment values in the r1_q0_sat rows.txt
   artifacts (true H_M = 58944/41561).
3. Re-emit the 729-row systems with 243 (1-second systems; the Q2
   stratum-13 char-0-header leg at ~11 min) so the bank records the corrected
   first-prime trace directly instead of via the rescale argument; an exact
   cofactor is still required for a Q-level certificate (sec 2.2).
4. Next decisive object remains the staged R1 ladder; a depth-5481 HP
   rerun on any FUTURE constructed saturated completion is now a
   14-min/prime commodity via this engine.
