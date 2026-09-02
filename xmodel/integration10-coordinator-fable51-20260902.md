# INTEGRATION #10 — coordinator binding (Fable 5.1, 2026-09-02)

Basis 5964c9cd. Supplements integration #9 (6a3148a5) and its deltas (a)
(E2 P0, coordinator-recomputed) and (b) (E2 P0 gated; C32 T2 sign P0;
A2 retractions). Different-model hostile review satisfied on every
PROMOTED item; hashes are the sealed report files' SHA-256 prefixes as
recorded in notes.md.

## A. The (B3) source-curve theorem set (producer opus 87fa5cb2; reviewer
## grok 12dea79f — eight for eight CONFIRMED, three binding repairs)

**PROMOTED — LEMMA E-ETALE.** For a noninvertible Keller map F of
geometric degree N with non-properness set A_F, the restriction
A^2 \ E -> A^2 \ A_F, E = F^{-1}(A_F), is a connected finite étale cover
of degree N.
**PROMOTED — THEOREM E-BMY-VACUITY** (BINDING REPAIR: log-smooth
compactifications so that K + D is Q-Cartier; c_2-bar scales by N
independently of compactification, c_1-bar^2 by N on log-minimal models
of the normalisation pair). kappa-bar(A^2 \ E) = kappa-bar(A^2 \ A_F) and
both log Chern numbers scale by N, so log-BMY on the source pair holds
iff it holds on the target pair, at every N and every profile. Binding
consequence: every "BMY on E" or "orbifold BMY on the Galois closure"
route is VOID (not blocked); the only different instrument is the
orbifold pair on the TARGET, which needs deg A_F-bar and a non-cyclic
boundary model at L_infty (OPEN[ORBIFOLD-BMY-AT-INFINITY]).
**PROMOTED — PROP 3.1 / LOC-1 and COR 3.2** (BINDING REPAIR: g is the
arithmetic genus of the compactified normalisation). No place of E at
infinity lies over a smooth point of A_F; n_infty(E) = (R − 1)a + 2 − 2g
− sum_p a_p r_p and chi_c(E) = a(1 − R) + sum_p a_p, degree-free;
matches B3-N4 at every (k, k_odd), k <= 8.
**PROMOTED — THEOREM E-CHARGE** (BINDING REPAIR: Orevkov's contracted
model, Phi finite of degree mu_t at t): Orevkov's excess k_t bounds the
same-branch contact degrees of E's places at infinity, with equality at
unibranch points; a − a_p = K_p is carried entirely by places of E at
infinity. At a cusp the link-at-infinity ledger of E is the (K) ledger.
**PROMOTED — B3-E-GENUS** (2g <= 1 − a + sum_p r_p max(0, (r_p − 1)W +
K_p − 1); g <= k − 1 attained at N = 4) and **B3-E-NOCROSS** at G-ANTI
scope (minimal (B3) profile: max cap 2g <= N − 3 independent of a; the
covering window is nonempty at every N = 4..20; no counting-vs-covering
crossing; the number of double points, i.e. delta_aff, is the unique
gate).
**PROMOTED — WITNESS E_0** as a REPRESENTATIVE numerical-type witness
(point names repaired: ordinary triple point delta = 3 at [1:0:0],
tacnode delta = 2 at [0:1:0]): a rational plane quintic with five places
at infinity, one ordinary (2,3) cusp at (15,1), no other affine
singularity, chi_c = −3 — the N = 4, k = 1, k_odd = 1 numerical type of
E. NOT a Keller preimage. Binding consequence: there is no embedding
obstruction for that type.
**PROMOTED — the section-6 identification:** the (B3) N = 4 object is
Orevkov's one-dicritical profile (mu, corr) = (2,1), killed by
Domrina–Orevkov I §§2–7 as a lemma SET on the determinant package; NOT
N-uniform (finiteness is sum Deg a~ = 4); DO's argument is a BOUNDARY
argument disjoint from the affine cage — the reason the cage is
rigid-but-not-empty. NO KILL of (B3) at any N. The lane's proposed
successor (an intersection number E-bar_X · l against Orevkov
determinants) is NOT well-posed (reviewer) and is not promoted.
RECORDED: OPEN[E-INFINITY-SPLICE-DEGREE] (deg E-bar unpinned; blocks
every splice test); OPEN[ORBIFOLD-BMY-AT-INFINITY].

## B. The degree gate in invariant form (producer opus d7cff053; reviewer
## gpt55 50f62fae — PROMOTE with repairs)

**PROMOTED — THEOREM SG-INV** (REPAIR: invariance under affine
reparametrisation as well as target automorphisms; #gaps = dim_C
C[t]/C[a,b]): the semigroup at infinity Gamma = {deg_t f(a,b)} of the
one-place parametrisation of A_F is Aut(C^2)-invariant and its gap count
equals delta_aff = sum_{p in Sing A_F} delta_p; n = max(deg a, deg b) lies
in Gamma. **BUDGET=IDENT:** the delta-budget computes delta_infty from
gauge data and constrains no invariant.
**PROMOTED — DEG-DELTA(a):** delta_aff <= (n − 1)(n − 2)/2 in every
gauge. **DEG-DELTA(b)** with its b_1 | b_0 escape: n <= 2 delta_aff + b_1
− 1 <= 3 delta_aff, sharp at (t^2, t^{2d+1}) (exact (AM-SG) is the banked
delta-sequence theorem; Tschirnhausen removes only represented
principal coordinate-degree cases). Together: bounding n_min in N and
bounding delta_aff in N are equivalent up to explicit constants
(OPEN[MIN-EMBED-DEGREE] the residual). **(R1)–(R4)** as necessary
filters on a minimal gauge.
**PROMOTED — MERIDIAN-FLOOR** (the first N-monotone statement in the
record): n_min >= ceil((N − 1)/(W − sum_l s_l)) >= ceil((N − 1)/(W − 1)),
W = N − a; at W = 2, n_min >= N − 1. Uses only the generic meridian
cycle type and transitivity; compatible with CUSP-PARITY and
ORBIFOLD-CAGE. Consequence: the lower half of OPEN[N-VS-MAPDEG],
max(deg P, deg Q) >= ceil((N − 1)/(W − 1)).
**PROMOTED — consequences:** in (B2), beta <= floor(delta_aff/2), so
(B2) at 5 <= N <= 10 dies iff delta_aff <= 3 and at 11 <= N <= 16 iff
delta_aff <= 1 — delta_infty never enters (OPEN[DELTA-INFTY-NOT-
NUMERICAL] is off this critical path); in (B3), k <= delta_aff −
delta_c; the row n = 4, (2,3), k = 1 of the Chau lane's list is EMPTY
(delta_aff = 2 forces n_min = 5); fixed-N non-derivability of any upper
bound from the banked ledger (a satisfying assignment with k -> infinity);
the cusp + k-nodes family as AFFINE-singularity representatives (k = 2,
3, 5 re-verified: degrees 4, 5, 7).
**CROSSING PRICE (binding reading):** a cell (N, W) is EMPTY as soon as an
upper bound n_min <= C holds with C < ceil((N − 1)/(W − 1)); at W = 2 any
C < N − 1 kills the column at every N. No reviewed statement supplies an
upper bound of that shape for any profile.
RETYPED: OPEN[DEG-AF-VS-N] -> OPEN[DELTA-AFF-VS-N] (raw form FALSE by the
banked NO-DEG-CAP [D]); OPEN[N-VS-MAPDEG] keeps only its upper half.
Literature (repaired): Jelonek 1993, Theorem 15, bounds the degree of
the non-properness set in the coordinate degrees, not in N.
DO NOT PROMOTE: any upper bound on n_min or delta_aff in N; the formula
2g(E) = 1 + N nu − n_infty(E) in disconnected cells; any Keller
realisation of the representative curves.

## C. Records (not promoted)

The (B3) boundary instrument (`b3-boundary-instrument-opus5-20260902`,
e9f26dde; review running): nine degree-free bridges between the affine
cage and the DO boundary ledger, two controls passed, no kill at N = 5,
6, the census closed form as the uniformity obstruction, and
GAP-CANDIDATE[BI-ATTACH] on the (m,n) split of the dicritical-incident
block (assigned to review against the checked N = 4 chain) — binds at
#11. Systems (`systems-collision-preflight-sol56-20260902`, 54ece042):
ops/open_collision.py and box/preflight.py with 27/27 tests and the
EQ2_even-omission canary; the COORDINATION authoring rule for raised
OPENs. The 0.2-stack cutover. Round 20260902T0741Z synthesis (DEGRADED
on timing; five submissions). The A2 line: reissue lane running on the
corrected system (EQ2_even with −2qE1; corrected T2 bracket).

## D. Standing fronts after this integration

1. **The all-degree ceiling in invariant form:** bound delta_aff (or
   n_min, or the Aut-minimal coordinate degrees) in N. Every banked
   constraint is satisfiable with k -> infinity; a NEW mechanism is
   required. Lanes: `n-vs-mapdeg` (boundary / semigroup / negative
   route), `meridian-floor-sharpen` (raise the floor with the group).
2. **The (B3) horn:** affine cage saturated by theorem; boundary
   instrument built; the census (plane-tree growth) is the obstruction;
   BI-ATTACH to settle; then OPEN[BI-CENSUS-DEG5-DEG6] with the bridges
   substituted.
3. **(B2) at 5 <= N <= 16:** now a statement about delta_aff alone
   (<= 3, resp. <= 1); the Aut-minimal degree of A_F for (B2) profiles
   (degree 3 empty; degree 4 first cell).
4. **Reducible branch:** OPEN[COMPANION-R0-REALISATION] elsewhere than
   coordinate degrees (9,6); the cap as prefilter.
5. **A2 (untyped):** reissue and c-pinning; T4 repair.
6. **Counterexample side:** profile-driven census design with PREFLIGHT
   as a hard gate; B3-PARAM-SEARCH on the re-indexed n <= 8 list.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8409`.
- Body SHA-256:
  `20cb472d54e008aa76396013c4b94c890223602bb09930b785d422264d2e099e`.
- Frozen basis: `5964c9cdee917bf8fb96fae8675e1af13c91cb10`.
