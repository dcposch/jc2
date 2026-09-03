# Ideation round 20260903T1015Z — coordinator's own blind submission (Opus 5, cloud seat)

Written before opening any other submission of this round (all five lanes
live and unread; the three research/review lanes' reports unread). Packet
99c940d1, basis f5aa1caf. Everything below is PROPOSAL unless it cites a
bound integration.

## 0. Verdict up front

1. **The all-degree program is now an arithmetic-plus-realisability
   statement about an infinite census, and the census is the wrong
   object to attack head-on.** (1)–(13) + integral pinned N leaves 670
   groups at D ≤ 120 and 14,016 at D ≤ 200, growing with the divisor
   structure of D. Moh's own program left 6 rows at n ≤ 100 from the same
   printed list: his kill ratio beyond the list is ~100x. Whatever he
   used is the campaign's single most valuable unknown, because it is
   the only mechanism in the record that has ever emptied a degree
   range by a uniform numerical filter. Q1 therefore outranks Q2 by a
   wide margin; the D = 105 trio is a calibration target, not a
   flagship.
2. **Direct candidate for Q1, checkable today: the second point at
   infinity.** `box/moh_skeleton_full.py` builds ONE tower — at the
   L_1 point, with u = V_s K / d_s roots — and never enumerates the
   tower at L_2 (v roots, H = L_1^u L_2^v, u > v). The (1)–(13) list is
   printed for "a hypothetically existing tower of major discs"; Moh's
   program, if it did what §6 of his paper does for the survivors,
   would have imposed the same tower analysis at BOTH points at
   infinity, with the shared data (n, m, d_j chain) and a second,
   independent V-sequence and δ-sequence at L_2 whose (7)–(13) must
   hold with u ↔ v. Cheapest test: enumerate the L_2 tower for the
   658 rows at n ≤ 100 and demand joint admissibility; a kill of ~650
   with Moh's six surviving (his rows have small v) would settle Q1
   without reading Appendix II. SOURCE-UNVERIFIED (the coordinator has
   not read pp.198–202 in the images; the Sol lane is charged with it).
   Second candidate, if the first fails: the root count at every level
   of Def 5.1(1) must be an INTEGER for both p_f and p_g at every disc,
   not only for the tower's major discs (§5 of the rebase says
   integrality of the Def 5.1(1) counts is automatic — but for the
   f-family? TF-0 says p_f has dV_2 simple roots; the f-root counts at
   levels j ≥ 2 are (m/n)-scaled and their integrality at every level
   is a separate condition worth one line of code).
3. **The interpolation instrument has a closed form the campaign has
   not written down, and it is a TRACE identity.** For a Keller pair
   in the monic gauge and any h ∈ C[x,y], along the fibre g = c:
   ∂_x Tr_{A_c/C[x]}(h) = Tr(∂_x h + ∂_y h · τ') = Tr(([h,g]/g_y)).
   With h = f^{j}: ∂_x Tr(f^{j}) = j·Tr(f^{j−1}/g_y). Since Tr(h/g_y) is
   the y^{n−1}-coefficient of h reduced mod (g − c), it VANISHES whenever
   deg_y h ≤ n − 2. Hence **TRACE-CONSTANCY: for every j with
   (j−1)m ≤ n − 2, the power sum p_j(x, c) = Σ_i f(x, τ_i(x; c))^j lies in
   C[c]** — it is independent of x. This is exactly the y^{n−1} block of
   the global interpolation conditions (packet item 6(a)) in symmetric-
   function form, and it is a condition that couples ALL branches and
   all Galois orbits of the fibre in one line: writing the branch
   expansions F_O(x) per orbit O (F conjugate within an orbit), the
   positive-integral-exponent part of Σ_O |O|·[F_O^j]_{x^k, k ≥ 1} must
   vanish. Under (UNI) with one orbit: every positive integer power of
   x in F(x)^j cancels for the branch series F = ∫dx/g_y(τ). NEGATIVE
   CONTROL (immediate): g = y² − x² − x is not a Keller mate of any f
   because NO-RESIDUE already fails; TRACE-CONSTANCY gives a second,
   independent coefficient-level gate on g alone — take f := the
   interpolant of ∫dx/g_y and ask whether Σ_i F_i² has an x-term. For the
   D = 105 trio (n = 105, m = 70) only j = 2 applies; the y^{n−1−k}
   blocks for k = 1..n−m−2 = 33 are the corresponding statements with
   f·s_k(τ̂_i) in place of f (s_k the elementary symmetric functions of
   the OTHER roots), each again a trace identity. So the n − m − 1
   degree conditions are: Tr(f · s_k(other roots) / g_y) = 0,
   k = 0..n−m−2 — thirty-four exact identities among power sums of the
   branch data at D = 105, before any polynomiality condition is
   imposed. This is the cheapest exact discriminator for Q2 (idea card
   1), and it is what the Sol framework lane should find; if it does
   not, this is the delta to add.
4. **Q3: the skeleton frame is right for the SIEVE and wrong for the
   THEOREM.** The sieve (census + pinned N + trace/interpolation orders)
   is how one empties D ≤ 200, 400, … by machine; it cannot be the
   proof because nothing in it is monotone in D (PIN-NOT-CEILING). A
   uniform theorem must use a datum that grows with D. The one such
   datum visible in the interpolation identity is the ORDER of the
   Picard–Fuchs / Gauss–Manin connection of the pencil g = c: the
   traces p_j(x, c) satisfy, as functions of c, a linear ODE whose rank
   is bounded by the genus data of the generic fibre (which grows with
   D: the pencil genus is the anticanonical defect, integration #12), while
   TRACE-CONSTANCY forces p_j to be a POLYNOMIAL in c of degree ≤ jm/n
   for the small j — a polynomial solution of a Picard–Fuchs equation
   of large rank with singular points at the atypical values. This is
   candidate (a) of the packet made concrete: the cofinal invariant is
   the irregularity/rank of the Gauss–Manin system of the pencil at
   c = ∞ versus the degree of the polynomial solutions the Jacobian
   condition forces. I rate it the strongest proof attack the record
   has not tried (card 2).
5. **Counterexample side (Q3(e)).** For the first time the campaign
   has a finite, exact, machine-checkable realisation list above
   D = 100 (the trio) and an exact order-by-order instrument. The
   honest disproof lane is a numerical Newton–Puiseux solve of the
   interpolation system at one D = 105 group to order ~50 over
   Q(ζ_{105}) or a large prime field — a solution surviving to the D_2
   junction would be the first positive signal above D = 100 in the
   campaign's history; a kill by counting at a stated order is the
   D_min ≥ 108 result. Same engine as card 1.

## 1. Disposition vector (changes only)

APPROACHES rows: 2 (sheet ladder / boundary trees): RETYPE — the
boundary computes N (integration #17); the route's all-degree content
is the census sieve, not a ceiling. 3 (strip ODEs): RAISE — BOTTOM-ODE
is the one-variable Keller equation at the bottom of Moh's tower;
Żołądek A.7 rigidity should be re-read as the k = 1 disc case of the
dessin-tower rigidity (card 3). 4 (formal-germ / algebraization): RAISE
as the DISPROOF engine — the D = 105 realisation is exactly a
formal-germ certification with the tree prescribed. 8/9 (formal
inverse, Conjecture E): unchanged (low). 20 (char-p formalism): LOWER
— the interpolation identity mod p is Keller-but-not-invertible
(x − x^p); Cartier gives no lower bound on y-degree that survives
lifting; retain only as a sieve accelerator (work over F_p in card 1).
25/26 (monodromy / primitive group): RAISE via cross-connection C2
below. 28 (log surfaces / BMY): unchanged, dead as built. 33
(symplectic primitives): unchanged (COSTUME). 29 (LND / Gauss–Manin
κ(P)): RAISE — the Gauss–Manin framing of card 2 is the same
[dx∧dy] = 0 statement seen from the g-pencil side. Everything else:
unchanged.
Q3 candidates: (a) RAISE (card 2); (b) RAISE as a lemma target
(card 3); (c) LOWER (sieve accelerator only); (d) REOPEN as a Q1
candidate only if the second-point test fails; (e) RAISE (the disproof
lane); (f) unchanged — expected true for the printed list, and it is
what makes Q1 decisive.
Queued fronts: DISC-COUPLING relaunch — REDESIGN into card 1 (do not
relaunch the resonance-order machinery; use the trace identities at
the y^{n−1−k} blocks, which are exact and global); branch-orbits v2 —
CONTINUE (the orbit structure is the datum TRACE-CONSTANCY couples).

## 2. Bottlenecks reranked

Proof: (1) Moh's missing elimination in uniform form (Q1); (2) a
D-monotone invariant on the pencil (card 2); (3) the dessin-tower
rigidity (card 3). Disproof: (1) an exact solver for the interpolation
system at a fixed skeleton (card 1 / (e)); (2) the orbit structure at
D = 105 (branch-orbits v2); (3) nothing else — every other disproof
lane in the record is below D = 100 and classically closed.

## 3. New avenue (required): TRACE-CONSTANCY as a g-only gate at all orders

Stated in §0.3. NEW relative to the record: NO-RESIDUE is the j = 1
statement ([x^{−1}] of 1/g_y vanishes on every branch, i.e. F_i has no
log term); TRACE-CONSTANCY is the j = 2 (and, at small m/n, higher-j)
statement, and the s_k-weighted versions supply all n − m − 1 degree
conditions as trace identities. Bounded OPEN[TRACE-GATE]: the number
of D = 105 trio groups (0..3) that fail the thirty-four exact trace
identities at leading orders with the bottom dessin fixed.

## 4. New cross-connection (required)

C1: TRACE-CONSTANCY ↔ ORTHO-DEFECT. Both are quadratic forms in the
branch data: 2deN = Σ(e m_ν − d m'_ν)² is the LEADING-order shadow of
Σ_i F_i² ∈ C[c] (the x-exponent of F_i² at the top order is 2(1 − δ⁰_i)
and its cancellation across conjugates is the same root-of-unity sum
that makes the ORTHO terms vanish at proportional points). If exact,
ORTHO-DEFECT is the order-0 case of an infinite tower of trace
identities — the higher orders are new.
C2: the Galois-orbit datum of OPEN[BRANCH-ORBITS] is the monodromy
datum of row 26 (primitive group bound): the orbits of bottom-major
discs under t ↦ ζt are the orbits of the inertia group at x = ∞ of the
cover (fibre of g) → (x-line); (UNI) across orbits is a statement about
the inertia action on the sheets, and the primitive-group database can
be queried for it directly.

## 5. Strongest attacks

Proof: card 2 (Gauss–Manin rank vs polynomial solutions forced by
TRACE-CONSTANCY). Counterexample: card 1 run to the D_2 junction at
the (105, 70, [28,103], V_s = 5, q = 1/2) group, the one with the
widest N-window (6..12).

## 6. Software / decisive experiment: the ALL-DEGREE INTERPOLATION ENGINE (Q4)

`box/interp_engine.py` (UPGRADE card, smallest useful version):
input a (1)–(13) group and an orbit structure; build the branch ansatz
τ_i(x) as Puiseux series with the skeleton's exponents fixed and tame
coefficients as unknowns over Q(ζ) (or GF(p), p ≡ 1 mod the ramification
lcm, for speed); compute F_i = ∫dx/g_y(τ_i) formally; impose (i)
NO-RESIDUE, (ii) the n − m − 1 trace identities Tr(f s_k / g_y) = 0
order by order, (iii) polynomiality of the m + 1 surviving coefficients;
report at each t-order unknowns / conditions / rank / solution-set
dimension. Gates: automorphisms (y, x + y^k), (y + x², x + (y + x²)²)
pass with the expected free parameters; the composition
(x + y⁵, y + (x + y⁵)³) passes; y² − x² − x and the two-tower rows fail
at a stated order (negative control that catches a vacuous pass: mutate
one Keller control's g by one coefficient and confirm the failure order
is reported). Then run over the D = 105 trio, then all 670 alive groups
at D ≤ 120 to a fixed order; a kill-by-counting typed per group. This is
the machine version of Moh's Appendix II. Cost: one Sol lane to build
(2 h), one core per group. Campaign-systems check: UPGRADE — the same
engine replaces DISC-COUPLING, the endgame's order-2 recurrence, and
the star Nullstellensatz as separate tools.

## 7. Idea cards

CARD 1 — TRACE-GATE at D = 105. Dependencies: D1-PIN, STAR-ABC, the
(1)–(13) trio (reviewed), NO-RESIDUE. Discriminator: the thirty-four
trace identities at the first two t-orders beyond the bottom star.
Outcomes: inconsistent ⇒ the group dies (D_min ≥ 108 after all three);
consistent with free parameters ⇒ continue to the D_2 junction (card 1
becomes the disproof lane); determined ⇒ evaluate the junction. Stop:
the junction reached or the system exceeds 10⁶ unknowns. Gain: high —
first exact verdict on a survivor above D = 100.
CARD 2 — GAUSS–MANIN RANK vs FORCED POLYNOMIAL PERIODS. Dependencies:
TRACE-CONSTANCY (card 1's identities, provable in one page), the
pencil-genus ledger (integration #12). Discriminator: compute, for the
Keller controls and for one D = 105 group's generic-fibre model, the
rank of the Gauss–Manin system on the traces and the degree in c of
p_2; look for an inequality rank ≤ φ(N, deg_c) that the census violates
at large D. Outcomes: an inequality that grows with D ⇒ the first
D-monotone invariant on the proof side; none ⇒ close (a) honestly.
Stop: 4 h desk. Gain: very high if positive, moderate as a negative
(retires candidate (a)).
CARD 3 — DESSIN-TOWER RIGIDITY. Dependencies: STAR-ABC, TF-DESSIN
passport, the orbit count (branch-orbits v2). Discriminator: for k ≥ 2
conjugate bottom stars glued at the D_2 level, the gluing forces the k
Belyi maps to share the D_2-level coefficients; count the moduli of
Davenport–Stothers pairs of the trio's profile ((2,3), V_2 = 5, 6, 4)
against the shared coefficients; a negative count is a kill. Outcomes:
kill ⇒ a NEW uniform condition (candidate (16)) to run over the census;
no kill ⇒ the dessin data are free and card 1 must carry the weight.
Stop: 3 h desk. Gain: moderate–high.

## 8. Lane recommendations

global-interpolation (Sol): CONTINUE; on landing, compare with §0.3 —
if the trace form is absent, add it as a delta before building the
engine. reducible-branch review: CONTINUE. websweep: CONTINUE.
moh-program review (Sol): CONTINUE and add the SECOND-POINT test of
§0.2 as an explicit charge in the next micro-round if it has not
already checked it. branch-orbits v2: CONTINUE. DISC-COUPLING: STOP as
designed; REDESIGN into the engine (§6). Box01: stopped (correct);
restart only for the engine's census-wide run.
Single first lane with a frontier seat: the ENGINE (§6), built by Sol,
with the D = 105 trio as its first payload — it serves Q2, Q4 and the
disproof side at once, and it is the object Q1's answer will be run
through.

## 9. Campaign-systems check

UPGRADE (adopted before this round): Linux launcher + systemd
detachment (regression PASS). NO further change proposed this round;
measured latency from handoff read to five blind lanes live: 85 min.

## 10. OPENs raised (bounded)

OPEN[TRACE-GATE]: number of D = 105 trio groups failing the trace
identities at orders ≤ 2 (0..3). OPEN[SECOND-POINT]: number of the 658
(1)–(13) rows at n ≤ 100 admitting a jointly admissible L_2 tower
(0..658; Moh's six must survive). OPEN[GM-RANK]: whether an inequality
between the Gauss–Manin rank of the pencil and deg_c p_2 holds on the
Keller controls (yes/no, with the inequality).

<!-- BODY-END -->
