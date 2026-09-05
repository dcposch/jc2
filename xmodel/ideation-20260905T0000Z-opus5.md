# Ideation round 20260905T0000Z — blind submission (Opus 5)

lane `ideation-20260905T0000Z-opus5` · basis `2358a71e` · charged inputs verified
(4/4 `sha256sum -c` OK, manifest generated mechanically from
`xmodel/ideation-20260905T0000Z-opus5.run.v2`). Read order: sealed packet →
AUDIT 17(ppppp)–(dddddd) → notes.md LIVE STATE 2026-09-04T08:22Z + the EVENT
tail → the 12:00Z synthesis → `g9966-n1-batch2-sol56-20260903.md` (sealed,
`final_status=DONE`). NOT read: any `ideation-20260905T0000Z-*` submission
(including the coordinator's); `g9966-n1-batch3-opus5-20260903.md` (receipt has
`initial_status=RUNNING`, no `final_status` — receipt only).

Everything below marked **PROVED-HERE** was computed in this lane at desk scale
and is replayable; everything marked **CLAIM** is typed with its cheapest test.

---

## 0. Disposition vector (changes only)

| # | Item | Packet/synthesis position | My position | Why |
|---|---|---|---|---|
| D1 | Q2 route: "kill the 5 remaining skeletons S1–S4,S7" | five independent u_s≥2 joint charts, 2271–3441 coeffs each | **REDESIGN — there are only FOUR descended data, not eight, and the eight skeletons sit on one explicit line 2K′+3ℓ=30** | PROVED-HERE §2.1: u_s = d_s − V_s, (n′,m′) = ((n/d_s)u_s,(m/d_s)u_s), ℓ = d_s−1−2u_s. Regenerated from the frozen enumerator, matches the batch-2 table row for row. |
| D2 | The k=4 ray is "the" unifying object of (H2) | ray in K at fixed k=4 | **DEMOTE to a slice.** The right object is the **(K,ℓ) lattice**; (99,66) is the anti-diagonal 2K+3ℓ=30, D=108 is the point (K,ℓ)=(8,4). The ray was a coincidence of which rows got charted first. | §2.1, §5 |
| D3 | 17(ppppp) DEGREE-BLIND ("no degree-only argument can prove dim 0", witness t=2's two roots) | a refutation of the degree route | **RE-TYPE.** The t=2 witness is not a witness against "weights + a₀ ∈ A_t^×": at the failing root **α_2 = 0 exactly**. The only known (V0) failure is a failure of the TAIL-SPLIT hypothesis itself. | §1.2 |
| D4 | (V0) has a "wrong-root" hazard for all t | implicit in "√(…)=m FACTORWISE" (17(wwwww)) | **NARROW.** A_t = Q(√(3(t+1))) is a **field** unless t+1 = 3m². For t ∉ {2,11,26,47,74,…} the two roots are Galois-conjugate and the verdict is forced to agree. Factorwise ≠ over-A_t only at the sparse split indices. | §1.1 PROVED-HERE |
| D5 | "Lemma SQUARE / Res_w(R_1..R_{t−1}) ≠ 0 in A_t" (17(wwww)) is the uniform target | a target awaiting a closed form | **RE-TYPE as ill-posed until normalised.** The resultant is *not* invariant under rescaling the tail generators: at t=3 its norm carries 59^180·73^60 in the denominator. Pattern-hunting on it cannot work as posed. | §1.3 PROVED-HERE |
| D6 | Q3 path through the (H1) census | 296 rows / 166 groups, per-row | **Batch by descended class.** Over the whole 16≤n≤200 skeleton census the u_s≥2 rows compress **6209 → 1359** distinct (n′,m′,ℓ,V₂′) (4.57×), or **→ 586** if V₂′ is carried as a parameter (10.6×). | §3 PROVED-HERE |
| D7 | Program scope | already corrected 17(qqqqq) to "two-point M_s=n−2 stratum, conditional on the routing maps" | **AGREE, no change.** I add one leak the synthesis did not name: the *degree-wide* obligation is not (99,66)-shaped — see §4. | §4 |

Unchanged and endorsed: (H1) has no arithmetic/disc/coprimality shortcut
(17(ooooo),(ttttt)); (8.1) is the JC2-relevant K16 target, (V0) is a fixed-t
instrument; guided_gb + staged emitter is the right systems spine.

---

## 1. Q1 — K16: the standing atom

The packet asks for a *new structural idea* for
`OPEN[K16-Q-NONVANISHING-ON-GAMMA]`. My answer has three parts: two results
that change the shape of the question (§1.1, §1.2), one that kills a target the
campaign is still carrying (§1.3), and the idea I would actually run (§1.4,
Card K16-A).

### 1.1 PROVED-HERE: A_t = Q(√(3(t+1))), and GALOIS-RIGIDITY

The four banked minimal polynomials (`box/k16brcr-20260903/brcr_t{3,4,5,6}_exact.sing`)
are 588y²−336y+44, 972y²−540y+70, 1452y²−792y+102, 2028y²−1092y+140. They fit a
closed form exactly:

> **H_t(y) = 12(2t+1)² y² − 12(t+1)(2t+1) y + (t+1)(3t+2)**,
> disc H_t = 48(t+1)(2t+1)², so **A_t = Q[y]/(H_t) ≅ Q(√(3(t+1)))**,
> with roots y_± = σ(σ±1)/(6(2t+1)), σ := √(3(t+1)).

Checks: t=3 → Q(√3); t=4 → Q(√15); t=5 → Q(√2); t=6 → Q(√21); and
t=2 → H_2 = 300y²−180y+24 = 12(5y−1)(5y−2) ⇒ roots **1/5, 2/5**, reproducing the
charged split base exactly. This is consistent with, and sharper than, the banked presentation
A_t = Q[d]/(3d²−(t+1)) (17(cccc)): d = 2(2t+1)y − (t+1) = ±σ/3.

> **A_t is a FIELD unless 3(t+1) is a perfect square, i.e. unless t + 1 = 3m².
> Split indices: t = 2, 11, 26, 47, 74, 107, 146, 191, …**

**LEMMA GALOIS-RIGIDITY (PROVED-HERE, formal).** The tail system
{T_{t,k}}_{k=t}^{2t−1} has coefficients in A_t and variables carrying no field
data. Hence J_t^tail is an ideal of A_t[b₃,b₄,q_{2,0..t−1,0}] and
dim A_t[…]/J_t^tail, its length, and the verdict (V0) are invariants of the
A_t-scheme. For non-split t the two complex embeddings A_t ↪ C are exchanged by
Gal(A_t/Q), so **the two "roots of H_t" give isomorphic-up-to-conjugation
schemes and cannot disagree.**

Consequences (this is the part that matters):

1. The measured "t = 3, 4 both roots dim 0" (17(ppppp)) was **not two
   independent confirmations** — it is one confirmation each, forced.
2. The 17(wwwww) instruction "√(I₂(N)+(W_r)) = m **factorwise**" is only
   *operative* at split indices. For every non-split t, factorwise = over A_t.
3. **The disagreement observed at t = 2 is structurally impossible except at
   t ∈ {2, 11, 26, 47, …}.** So the "wrong root" hazard is not a general hazard;
   it is a hazard at eight indices below t = 200.

### 1.2 PROVED-HERE (from the banked audit): the t=2 failure IS a₀ = 0 — re-type DEGREE-BLIND

`box/k16hsop-20260903/alpha_norm_audit.{py,out}` gives
α_t ∝ A_b d + B_b with A_b = 27t³−30t²+t−2, B_b = 6t³+13t²−3t+2, and

> N_{A_t/Q}(α_t-numerator) = −4(t−2)(2t+1)²(3t−1)²(3t+2)(27t³+17t²+t+2),

whose only positive integer root is **t = 2**; the run prints
`alpha_2 at y=1/5: 0`, `alpha_2 at y=2/5: 28/625`. So:

> **The unique known failure of (V0) — t=2, y=1/5, "dim 1, the b₃-axis" — is
> exactly the point where a₀ = α_t vanishes**, i.e. where the top row
> T_{t,2t−1} = a₀b₃² + b₀b₃ + c₀ degenerates from a *quadratic* to a *linear*
> form in b₃ and TAIL-SPLIT's free-rank-2 conclusion is void.

17(ppppp) already identified "the minimal extra input is a UNIT statement". The
sharper reading is stronger and changes the target: **DEGREE-BLIND refutes
"weights ⇒ dim 0", but it does NOT refute "weights + a₀ ∈ A_t^× ⇒ dim 0",
because the sole witness violates the second hypothesis.** That second
statement is not on any lane's target list and is not refuted by anything in
the banked record. Its honest status is **untested**, and it is testable: see
Card K16-B.

Note the two facts compose: a₀ is a unit for *every* t ≥ 3 including the split
indices (the norm above is nonzero at t = 11, 26, …), so the t=2 degeneration
does not recur at t=11. The split indices are dangerous for a *different*
reason (§1.1) and only there.

### 1.3 PROVED-HERE: the "Res_w ≠ 0 in A_t" target is not normalisation-invariant

Reconstructing W_r = a₀C_r² − b₀B_rC_r + c₀B_r² at t = 3 from the frozen
explicit tail (`box/k16brcr-20260903/explicit_tail_t3_exact.txt`, sympy, exact
over Q[yy]/(H_3)):

- weights: W_1 has weight 18, W_2 weight 20 — matching 4t+4+2r with
  wt(b₄)=1, wt(q_{2,0})=2. ✔
- **W_1|_{b₄=0} = 0 and W_2|_{b₄=0} = (nonzero)·q_{2,0}¹⁰** — an *independent*
  reproduction of the 17(wwwww) GAMMA CORRECTION (the q_{2,0}-axis is a
  denominator-zero of the W_1 chart, not a (V0) failure). ✔
- Dehomogenising at b₄ = 1 (legitimate: the b₄=0 locus is settled by the line
  above) the square system becomes two univariate polynomials of q-degrees 8
  and 10 over A_3, and **Res_q(W_1,W_2) ≠ 0, computed exactly in 4.9 s**.
  This is a **non-Gröbner certificate of the tail hsop at t = 3** (hence of
  (V0) at t = 3 through the banked 17(ppppp) ELIMINANT and 17(rrrrr)
  DEPENDENCY chain). Legitimacy of the b₄=1 chart: the weighted C*-action is
  (b₄,q) ↦ (s·b₄, s²·q), every orbit with b₄ ≠ 0 has a unique b₄=1
  representative, and both leading coefficients in q are nonzero constants, so
  Res ≠ 0 ⟺ no common root.
- **But:** N_{A_3/Q}(Res) is a positive rational whose numerator is
  3³³²·13²⁴·37·(2357-bit residual) and whose denominator is
  2³⁷⁸·5²⁰·7³⁷⁶·11²²·**59¹⁸⁰·73⁶⁰**·(819-bit residual).

The primes 59 and 73 are not functions of t in any plausible ansatz; they are
artefacts of the *scaling* of B_r, C_r (which are a₀-combinations of rows, each
carrying its own denominators). **Res_w(R_1..R_{t−1}) ∈ A_t is defined only up
to a product of unit multiples of the generators, so "find its closed form in
t" is ill-posed.** This is, I believe, the reason four lanes have failed to
produce a formula.

**Fix (cheap, and it makes the target well-posed):** take the resultant of the
*primitive integral* rows. Concretely, clear content over Z from each
T_{t,2t−1−r} (not from G_r), take the Macaulay/weighted resultant of the t rows
{T_{t,k}} themselves, and hunt the pattern on that. Price: t = 3 is the 4.9 s
run above re-done on primitive rows; t = 4 needs one 3-variable weighted
resultant (iterated elimination, minutes); t = 5, 6 need guided_gb-scale
elimination. Two clean data points would already discriminate an ansatz built
from the α_t ingredients (t−2), (2t+1), (3t−1), (3t+2), (27t³+17t²+t+2).

### 1.4 The typed Q1 answer

**Where the coordinator's framing is wrong.** The packet asks for "a valuation
on Γ, a specialization argument, an intersection-theory count, a deformation".
Three of those four are already excluded by the banked record and I would not
spend a lane on them:

- *Intersection-theory count* is dead by 17(uuuuu)'s KEY FINDING: LENGTH-SPLIT
  (L_t = 2C(2t,t−1) + (2t+2)d_Γ(t)) is a consequence of the nonvanishing, not a
  proof of it. Any count of the d_Γ(t) points of Γ has the same defect — the
  count is only valid on the locus where the thing to be proved already holds.
- *Deformation/specialization to a monomial or degree-generic model* is dead by
  DEGREE-BLIND **only in its degree-only form**; but §1.2 shows the honest
  residual is "weights + a₀ unit", which is not dead. Re-open it, but as the
  precise statement, not as "Fröberg".
- *A valuation on Γ* is the one live suggestion, and §1.1 tells you which one:
  not a geometric valuation on Γ but the **arithmetic** of A_t = Q(√(3(t+1))).

**CLAIM Q1-A (typed).** For every non-split t (t+1 ∉ 3·squares), (V0) at t is
equivalent to a single statement over the *field* A_t, with no root selection;
and a dim-0 verdict modulo any prime p that is inert or split in A_t promotes
to char 0 under the properness instrument. Bounded quantity: the number of
indices t ≤ T at which the factorwise/over-A_t distinction is operative is
⌊√((T+1)/3)⌋ — **8 indices below t = 200**. Cheapest test: none needed
(GALOIS-RIGIDITY is formal); the *use* is Card K16-A.

**CLAIM Q1-B (typed, the actual new target).** (V0) at t follows from
[weights of the tail] + [a₀ ∈ A_t^×] alone. Bounded quantity: the tail has t
rows of weights 2t+2..3t+1 in t+1 variables of weights (t+1, 1, 2, …, t−1) with
exactly one weight-0 coefficient. Status: **untested; not refuted by anything
banked** (§1.2). Cheapest decisive test: at t = 2 take the *generic* system with
the t=2 weight data and a₀ ≠ 0 — 3 rows, 2 variables, ≤ 20 free coefficients —
and compute whether {dim > 0} ∩ {a₀ ≠ 0} is empty. If it is empty at t = 2, run
t = 3 (the 4.9 s resultant of §1.3 becomes a resultant with symbolic
coefficients). If it is *nonempty* at t = 2, Q1-B is dead in one run and the
campaign stops looking for a genericity argument forever. **This is the single
cheapest high-information K16 experiment available and no lane has run it.**

**CLAIM Q1-C (typed, negative).** "Find a closed form in t for
Res_w(R_1..R_{t−1}) ∈ A_t" (17(wwww)'s NEW UNIFORM TARGET, still carried) is
ill-posed as stated. Bounded quantity: at t = 3 the norm's denominator contains
59¹⁸⁰·73⁶⁰ (§1.3). Cheapest test: recompute the same resultant after replacing
G_r by primitive integral T_{t,2t−1−r} and check whether 59 and 73 disappear —
≈ 10 minutes, and it either repairs the target or confirms the refutation.

**On the weaker (8.1).** I endorse the 12:00Z demotion of (V0) to a fixed-t
instrument. But note (8.1) inherits nothing from §1.1–§1.3 automatically: the
Galois rigidity argument applies verbatim (τ_t and I_{t,+} are defined over
A_t), so **(8.1) also cannot be root-dependent at non-split t** — which
means the t=8 b₄=1 z-chart timeout in 17(uuuuu) need only be run on *one*
embedding, halving that cost. That is a free 2× on the standing (8.1) frontier.

---

## 2. Q2 — the degree-wide (99,66) theorem / N1

**Short answer: the packet's framing ("kill the 5 remaining skeletons") is
right in outcome and wrong in shape. There is a uniform structure across the
eight V-assignments, it is explicit, and it collapses the remaining work.**

### 2.1 PROVED-HERE: the descent law, and the eight skeletons on one line

I regenerated the enumeration independently from the frozen census
(`box/mohprog-drivers-20260903/repro/moh_skeleton_full.py`,
`census(99, Kmin=2, full=True)` → exactly 8 rows, matching 17(cccccc)) and
recovered the batch-2 descended data **row for row** from three identities:

> **u_s = d_s − V_s,  v_s = V_s,  (n′, m′) = ((n/d_s)·u_s, (m/d_s)·u_s),
> ℓ = v_s − u_s − 1 = d_s − 2u_s − 1,  M′ = M·u_s/d_s,  u′ = K′ − V₂′.**

At (99,66): d = (99,33,11,1), s = 3, d_s = 11, so **u_s + v_s = 11 for all
eight**, u_s ∈ {1,2,3,4}, and

| u_s | v_s | (n′,m′) | K′ | ℓ | skeletons | V₂′ | status |
|---|---|---|---|---|---|---|---|
| 1 | 10 | (9,6) | 3 | 8 | S5, S6 | 1, 2 | **both DEAD** (17(dddddd)) |
| 2 | 9 | (18,12) | 6 | 6 | S1 | 1 | OPEN |
| 3 | 8 | (27,18) | 9 | 4 | S4, S8 | 1, 8 | S8 **DEAD**; S4 OPEN |
| 4 | 7 | (36,24) | 12 | 2 | S2, S3, S7 | 1, 5, 8 | all OPEN |

and (eliminating u_s between K′ = 3u_s and ℓ = 10 − 2u_s):

> **2K′ + 3ℓ = 30 — every (1)–(13)-admissible (99,66) skeleton descends onto
> ONE LINE in the (K′, ℓ) plane.** In general, for m/n = 2/3,
> **(6d_s/n)·K′ + ℓ = d_s − 1.**

Verification: reproduced `18,36,36,27,9,9,36,27` for n′ and `6,2,2,4,8,8,2,4`
for ℓ, identical to the batch-2 table; regenerated the (u_s,v_s) pairs
`(2,9),(4,7),(4,7),(3,8),(1,10),(1,10),(4,7),(3,8)` identically. Independent
cross-check at D = 108: the banked no-split datum (24,16; 18; 7; k=4) forces
d_s = 9, u_s = 2 ⇒ n′ = (108/9)·2 = 24 ✔, ℓ = 7−2−1 = 4 ✔.

### 2.2 What this changes

1. **The five open skeletons are three descended charts, not five.** S2, S3, S7
   share (n′,m′,ℓ) = (36,24,2) and differ only in V₂′ ∈ {1,5,8} (hence
   u′ = 12−V₂′ ∈ {11,7,4}). One V₂′-parametrised (36,24; ℓ=2) builder covers all
   three. S1 is (18,12; ℓ=6). S4 is (27,18; ℓ=4) with V₂′=1.
2. **S4 sits on the k=4 ray at exactly the K=9 point already killed** — but at
   the *opposite end* of the V₂′-line from S8: S8 has (V₂′,u′) = (8,1), S4 has
   (1,8). So S4 is **not** discharged by the case-(A) certificate; it is the
   conjugate point of the same descended degree, and the k=4 machinery (the
   17(zzzzz) K+6 theorem, the LEVEL-4 pin, the 36-var lower-band
   parametrisation) transports to it with only V₂′ changed. Cheapest test:
   re-run the banked K=9 pinned builder with V₂′=1, u′=8 — hours, not a lane.
3. **The campaign's "k=4 ray" is the horizontal line ℓ = 4 of a lattice.**
   (99,66) is an anti-diagonal of that lattice; D = 108 is the single point
   (K,ℓ) = (8,4) where the two cross. That is why case (A) and D = 108
   collapsed together — not because the ray is canonical, but because both
   happened to have ℓ = 4. **The reusable object is the (K,ℓ)-lattice chart.**
4. The uniform theorem the packet asks for ("a single obstruction parameterised
   by V") therefore exists in the following typed form:

> **CLAIM Q2-A (UNSPLIT-LATTICE).** For the two-point unsplit configuration at
> (3K, 2K) with descended Jacobian exponent ℓ, the composite arm (17(vvvvv):
> B₂ ∈ k ⇒ h | J ⇒ composite) and the degree identity
> deg(g²−f³−λf) = K + ℓ + 2 (17(zzzzz) at ℓ=4; the general-ℓ form is the
> band-chase on E = g²−f³) hold **uniformly in (K, ℓ)**, and the LEVEL pin
> collapses the top band to one scalar for every (K, ℓ) on the line
> 2K + 3ℓ = const. Bounded quantity: for (99,66) the whole N1 no-split half is
> **4 lattice points**, of which 2 are already dead.

Cheapest test of Q2-A: verify deg(g²−f³−λf) = K+ℓ+2 at (K,ℓ) = (6,6) and
(12,2) symbolically (sympy, < 5 min each, no Gröbner) — the identity is a
band-chase, and if it fails off ℓ=4 the lattice claim degrades to "one builder
per ℓ", which is still 3 builders, not 5 charts.

### 2.3 Is Moh's (1)–(13)-completeness citable, or itself a gap?

**It is a citable enumeration and a NON-citable selection, and the packet
should stop calling the whole thing "N1".** Split it:

- **N1a (citable).** "Every degree-(99,66) two-point Keller pair has
  characteristic data satisfying (1)–(13)" is Moh's printed derivation and the
  frozen enumerator is a faithful decision procedure for it (8 rows,
  reproduced here from a clean import). Nothing is owed.
- **N1b (NOT citable, a real hole).** "…and therefore V = (8,8)" — the
  selection of S8 from the eight — is Moh's private-program assertion. This is
  the genuine gap, and it is *not* a gap in his theorem statement: THEOREM 8.1
  as the campaign has assembled it (necessity 17(hhhhh) + gauges 17(jjjjj) +
  classification 17(sssss) + three configuration kills) is a **complete
  unconditional theorem about the skeleton V = (8,8)**, which is exactly what
  Moh's published argument covers if his selection step is granted.

So the honest paper-grade statement available **today** is: *"there is no
Keller pair of degrees (99,66) with characteristic data S8"*, unconditional.
The degree-wide statement needs S1–S4, S7. I would publish the first now and
keep the second as the running obligation — and I would **say in the writeup
that the eight-row enumeration is reproducible from Moh's printed (1)–(13)**,
because that sentence is what converts a private assertion into a checkable
finite task.

---

## 3. Q3 — the (H1) census: pricing the three options

The packet offers three: a batched guided_gb sweep, a uniform
pin+parametrization theorem, an augmented-Schur-row theorem. **The third is
dead, the second is a systems change not a theorem, and the first is right but
should be batched on the wrong axis from the one proposed.**

### 3.1 The augmented-Schur-row theorem: do not fund it

17(lllll) proved the killing augmented row is **not determined by skeleton
data**; 17(ooooo) killed disc; 17(ttttt) killed NONRES with 0/274 kills by
predicate alone. Three refutations of three different uniform mechanisms is
enough evidence: the exit price of "one more uniform (H1) mechanism" is a lane
with a prior well under 20%. **STOP** funding uniform (H1) mechanisms.

### 3.2 PROVED-HERE: batch by DESCENDED CLASS, not by row — a measured 4.6×

Running the descent law of §2.1 over the whole frozen census 16 ≤ n ≤ 200:

| quantity | count |
|---|---|
| skeleton rows (Kmin=2, full) | 24,063 |
| of which u_s ≥ 2 | **6,209** |
| distinct descended classes (n′, m′, ℓ, V₂′) | **1,359** (4.57× compression) |
| distinct (n′, m′, ℓ) if V₂′ is carried as a chart parameter | **586** (10.6×) |
| n′ integral in all 6,209 rows | yes (0 exceptions) |

ℓ-histogram over the 1,359 classes is front-loaded: ℓ=0 → 274 classes,
ℓ=1 → 227, ℓ=2 → 178, ℓ=3 → 138, ℓ=4 → 97, ℓ≥5 → 445. **ℓ = 0 is the single
biggest class and is the cheapest**: ℓ=0 means the descended Jacobian target is
J − c·x⁰ = J − c, a *constant* subtraction — no x-power to chase, the smallest
possible order-basis. Nobody has charted it; it is 20% of the compressed
census.

This is the answer to "price it": the sharpened Xu-ok cohort is 296 rows / 166
groups, and the same map applied to *that* cohort is the number the coordinator
should compute before scheduling anything (5 minutes with the frozen
enumerator). On the raw census the compression is 4.57×; there is no reason to
expect the sharpened cohort to behave differently, which would turn 296 rows
into ≈ 65 charts.

### 3.3 The efficient path, typed

> **CLAIM Q3-A.** The efficient (H1) path is a **descended-class sweep**:
> (i) map every cohort row to (n′, m′, ℓ, V₂′); (ii) build ONE
> (n′,m′,ℓ)-parametrised chart per class with V₂′ symbolic; (iii) run guided_gb
> with the 17(bbbbbb) recipe (top pin + exact lower-band parametrisation → ≈36
> ring variables) per class; (iv) sweep ℓ upward from 0.
> Bounded quantities: ≈1,359 classes at D ≤ 200 (≈65 for the sharpened
> cohort); measured per-chart cost once built, from the banked kills, is
> **2.4–9.2 s exact-Q** (S5 components) to **8.2 s** (K=7 pinned) — the cost is
> entirely in the BUILD, which is exactly what class-batching amortises.

That is why "a uniform pin+parametrization theorem" is the wrong frame: the pin
is not a theorem to prove once, it is a *builder* to parametrise once. The K+6
theorem plus the LEVEL pin is already that builder at ℓ = 4; generalising it in
ℓ (§2.2) is the whole job.

**One caution, per FALLACY-v2 (flag/place/series).** Equal descended data does
**not** entail equal joint charts: the split/no-split branch depends on δ versus
v_s/u_s per skeleton, and V₂′ enters the gauge. A class-level kill discharges
the **no-split/descent half only**; each row still needs its own split-branch
disposition (the batch-2 §"split-unsplit triage" columns are the right input).
I would report class kills as `DEAD[DESCENT-HALF]`, never as `DEAD`.

---

## 4. Q4 — the finish. Challenging the framing.

**Does the (99,66) closure method generalise to a degree-wide program for all
two-point degrees? Yes as a method, no as a proof — and the packet's implicit
arithmetic is wrong by an unbounded factor.**

### 4.1 The method generalises; the finiteness does not

The (99,66) method is: enumerate the (1)–(13)-admissible skeletons at a fixed
degree, descend each, kill each descended chart. §2.1 shows the descent is a
closed formula, so the *enumeration and descent* generalise perfectly. What
does **not** generalise is termination: "all two-point degrees" is an infinite
family and §3.2 measures the cost — 6,209 u_s≥2 rows at n ≤ 200 alone, growing
(n = 144 alone has 2,295 skeleton rows). **A degree-by-degree program is not a
proof of the two-point stratum; it is an unbounded verification.** The packet's
Q4 sentence ("does that … constitute a complete proof of the two-point
stratum") should be answered: **no, not even in principle**, unless a
uniform-in-degree theorem replaces the sweep.

### 4.2 So what is the uniform-in-degree object? The (K, ℓ) lattice

§2.1 gives it. Every u_s ≥ 2 two-point skeleton at any degree lands, after
Prop 6.3 descent, on a point (K′, ℓ) with V₂′ — and the *whole* infinite family
of degrees maps into a **two-dimensional lattice of descended charts**, with
each degree contributing one line (6d_s/n)K′ + ℓ = d_s − 1. Killing the lattice
row-by-row is still infinite; but a theorem uniform in **K at fixed ℓ**
(what the k=4-ray lanes were reaching for, and 17(zzzzz) showed saturates) plus
a theorem uniform in **ℓ at fixed K** would tile it. Neither exists. The honest
statement:

> **CLAIM Q4-A.** The two-point M_s = n−2 stratum reduces (modulo the unproved
> routing maps) to: for every (K, ℓ, V₂′) with K ≥ 2, 0 ≤ ℓ, the unsplit
> descended chart at (3K, 2K; ℓ; V₂′) is empty. The campaign has this at
> ℓ = 4, K ∈ {7,8,9} (17(aaaaaa),(bbbbbb)) and at ℓ = 8, K = 3 (S5/S6) — **four
> lattice points out of an infinite lattice.** No K-uniform and no ℓ-uniform
> theorem is in hand; 17(zzzzz) proved the pure-degree tower cannot supply the
> K-uniform one.

That is the true residual, and it is much larger than "5 skeletons".

### 4.3 The leaks, re-counted

The 12:00Z synthesis named four (one-place/Abhyankar–Moh; N1; U-NEGATIVE
V₂′>d₂′; s′>2 residual) plus the routing maps. I add one and sharpen one:

- **NEW LEAK (scope of the descent) — PROVED-HERE, and it is not small.**
  Prop 6.3 is stated under a radius hypothesis, and
  `box/g9966n1b2-20260903/enumeration.json` records `prop63_automatic` per row.
  Reading all eight: **True exactly for S5, S6 (u_s = 1); False for S1, S2, S3,
  S4, S7 AND S8 (u_s ≥ 2).** So the flag tracks u_s = 1 precisely — which means
  **every u_s ≥ 2 descent in the campaign is non-automatic**, including the
  banked S8/case-(A) kill and the D = 108 no-split kill that closed D = 108 at
  skeleton level. The kills are not thereby wrong (17(fffff) sourced the
  (γ,π)-map), but the hypothesis-discharge is an obligation that has never been
  audited row-by-row. Type it `OPEN[PROP63-RADIUS-DISCHARGE]`. Cheapest test:
  read Moh p.197 Prop 6.3's hypothesis once, then evaluate it on the four
  descended classes of §2.1 — one hour, source read plus arithmetic, no CAS.
  **I would run this before publishing anything about (99,66) or D = 108.**
- **SHARPENED (N1).** Split into N1a (citable enumeration) and N1b
  (non-citable selection) per §2.3; only N1b is a hole, and it is a hole in the
  *degree-wide* claim, not in THEOREM 8.1.

### 4.4 The single most valuable object

Not the five skeletons, and not K16. It is:

> **the (K, ℓ, V₂′)-parametrised unsplit descended chart builder + the general-ℓ
> degree identity deg(g²−f³−λf) = K+ℓ+2.**

It closes S1–S4,S7 (§2.2), it is the (H1) census sweep instrument (§3.3), it
subsumes the k=4 ray, and it is the only object in the campaign that is
uniform in *anything* on the (H2) side. K16, by contrast, is now one atom with
four exhausted attacks and — per §1 — a cheaper reframing but no proof; it
should get one experiment (Card K16-B), not a lane series.

---

## 5. Three idea cards

### Card A — **LATTICE-BUILDER**: the (K, ℓ, V₂′) unsplit descended chart

*Type:* instrument (builder), not a theorem. *Target:* Q2 (S1–S4,S7), Q3
(census sweep), Q4 (the only uniform (H2) object).

**Content.** Generalise the three banked k=4 ingredients in ℓ:
(1) the composite arm B₂ ∈ k ⇒ h | J ⇒ composite (17(vvvvv)) — already
chart-free, check it is ℓ-free;
(2) the degree identity deg(g²−f³−λf) = K+ℓ+2 (17(zzzzz) proved ℓ=4 ⇒ K+6) —
re-derive the band chase with ℓ symbolic;
(3) the LEVEL pin β_b = μ·y^{K−3}(y−x) — its exponent should become
K−(ℓ−1) or similar; derive, do not guess.
Then emit the chart at (K,ℓ,V₂′) with the 17(bbbbbb) recipe (top pin + exact
lower-band parametrisation → ≈36 ring variables) and hand it to guided_gb.

**Bounded quantities.** Covers all four (99,66) classes (§2.1); 1,359 classes
at D ≤ 200; per-chart GB cost 2.4–9.2 s exact-Q once built.
**Cheapest test.** Re-derive (2) at (K,ℓ) = (6,6) and (12,2) in sympy over Q,
no Gröbner, < 5 min each. If K+ℓ+2 survives both, the builder is real; if not,
fall back to one builder per ℓ (still 3, not 5, for N1).
**Kill condition.** If the pin exponent has no closed form in ℓ, the card
degrades to "port the k=4 builder by hand per ℓ" — still a win over five
independent joint charts, but not a lattice.

### Card B — **A₀-GENERICITY**: is "weights + a₀ ∈ A_t^×" already enough?

*Type:* decisive experiment. *Target:* Q1 (K16), and it is cheap enough to be
a sub-task, not a lane.

**Content.** §1.2 shows the sole known (V0) failure is a₀ = 0. Form the
**universal** tail with the t = 2 weight data — three rows
T ∈ {wt 6, 7, (8)}, variables b₃ (wt 3), b₄ (wt 1), coefficients free — and
compute whether {systems with dim > 0} ∩ {a₀ ≠ 0} = ∅. Then t = 3 (add
q_{2,0} wt 2; the §1.3 4.9 s resultant becomes a resultant with symbolic
coefficients).

**Bounded quantities.** t=2: 3 rows × ≤ 6 coefficients ≈ 18 parameters, one
elimination. t=3: 3 rows × 9 = 27 parameters, one 18×18 Sylvester determinant
with symbolic entries.
**Cheapest test.** Exactly the t = 2 run above, ≤ 15 min.
**Why it matters either way.** If the intersection is **empty**, the K16
uniform statement is a *genericity theorem in the weights* and the whole
Γ/Eagon-Northcott apparatus becomes an unnecessary detour. If it is
**nonempty**, no genericity argument can ever work and every future K16 lane
must use a₀-specific arithmetic — which retires a whole class of proposals.
This is the highest information-per-minute experiment I can see in the
campaign right now.

### Card C — **NORMALISED RESULTANT**: repair 17(wwww)'s uniform target

*Type:* repair + pattern hunt. *Target:* Q1.

**Content.** §1.3: Res_w(R_1..R_{t−1}) is not scale-invariant (t=3 norm
denominator carries 59¹⁸⁰·73⁶⁰), so its "closed form in t" cannot exist as
posed. Recompute using **primitive integral** rows T_{t,2t−1−r} over Z rather
than the a₀-combinations G_r, take the weighted Macaulay resultant of the t
rows, and hunt the pattern against the α_t ansatz basis
{(t−2), (2t+1), (3t−1), (3t+2), (27t³+17t²+t+2)} — the same ingredients that
gave the α_t norm its closed form.

**Bounded quantities.** t=3: 2 forms of weights 18, 20 in 2 variables — 4.9 s
measured. t=4: 3 forms of weights 22, 24, 26 in 3 variables — iterated
elimination, minutes to tens of minutes. t=5: needs guided_gb.
**Cheapest test.** Redo t = 3 primitively and check whether 59 and 73 vanish
from the norm (≈ 10 min). If they persist, the non-invariance is intrinsic and
**17(wwww)'s NEW UNIFORM TARGET should be formally retired**, which is itself
worth banking.
**Risk.** Two data points cannot confirm an ansatz; this card produces a
*candidate*, and the candidate must then be checked at t = 5 by an independent
route before any promotion.

---

## 6. The single first lane

> **`h2-lattice-builder-<adapter>` — Card A.**
> Derive the general-ℓ degree identity deg(g²−f³−λf) = K+ℓ+2 and the general-ℓ
> LEVEL pin; build the (K,ℓ,V₂′)-parametrised unsplit descended chart; run it
> at the two (99,66) classes the running lane is least likely to reach —
> **(18,12; ℓ=6; V₂′=1) = S1** and **(36,24; ℓ=2; V₂′ ∈ {1,5,8}) = S2/S3/S7** —
> and at **(27,18; ℓ=4; V₂′=1) = S4** as a calibration against the banked K=9
> case-(A) certificate (same descended degree, conjugate V₂′).

**Why this and not K16.** K16 has had four deep structural lanes in one day,
each sharpening and none closing; §1 gives it two cheap experiments (Cards B,
C) that belong inside another lane's budget, not in a lane of their own. The
lattice builder, by contrast, is the only object that pays three ways at once
(N1, the (H1) census, the Q4 uniform target) and it has a **measured**
7-second-per-chart back end already shipped.

**Success criterion.** UNIT_IDEAL_CHAR0 (exact-Q, ≥3 modular fibres + exact
[1]) on at least the (36,24; ℓ=2) class, reported as `DEAD[DESCENT-HALF]`.
**Failure criterion.** If the general-ℓ identity does not exist, report the
per-ℓ builder and say so — do not paper over it with the ℓ=4 pin.

**Deconfliction with the running lane.** `g9966-n1-batch3-opus5` is building
and killing S1–S4,S7 by the per-row route. This lane is the *class* route and
would supersede it only if the general-ℓ pin exists. If batch3 lands first with
kills, this lane's value shifts entirely to Q3/Q4 (the census sweep) — still
worth running, and the calibration at S4 remains a useful cross-check of two
independent instruments on one descended degree.

---

## 7. Running lane: `g9966-n1-batch3-opus5` — **CONTINUE**

Receipt only (`xmodel/g9966-n1-batch3-opus5-20260903.run.v2`):
`tag=g9966-n1-batch3-opus5-20260903`, `start_utc=2026-09-04T23:43:29Z`,
`initial_status=RUNNING`, **no `final_status`** — report not opened, per the
prompt.

**CONTINUE.** Reasons: (i) its task (build + kill S1–S4,S7) is on the critical
path for the degree-wide (99,66) theorem regardless of §2's compression; (ii)
the method it is running is the validated 17(bbbbbb) recipe with a measured
back end; (iii) §2.1's compression makes its job *easier*, not obsolete —
S2/S3/S7 share a descended degree, so if it builds one of them the other two
should follow cheaply.
**One caveat to hand the synthesis, not the lane:** if batch3 reports S4 as
independently killed, cross-check it against the banked S8 certificate — same
(n′,m′,ℓ) = (27,18,4), conjugate (V₂′,u′) = (1,8) vs (8,1). Agreement is a free
two-instrument confirmation; disagreement is a bug in one of them.

---

## 8. One systems upgrade

> **`ops/descend.py` — a single frozen implementation of the Prop 6.3 descent
> map, with its hypothesis flag, wired into the census tooling.**

Today the descent arithmetic is re-derived per lane, and it has already
produced one erratum of exactly this kind: 17(cccccc) used
ℓ = n′−M₂′−2 instead of ℓ = v_s−u_s−1, voiding an S6 certificate
(caught in 17(dddddd)). The map is four lines (§2.1) and is fully determined by
(n, m, M, V, d):

```
u_s = d_s − V_s ;  v_s = V_s ;  ell = v_s − u_s − 1
(n', m') = ((n/d_s)·u_s, (m/d_s)·u_s) ;  M' = M·u_s/d_s
V2' = V_2 ;  u' = K' − V2'    (K' = n'/3 on the m/n = 2/3 line)
prop63_automatic  (measured: true iff u_s = 1)
```

Ship it with: the eight (99,66) rows as a golden test (the batch-2 table is the
fixture); a negative control (the void ℓ = n′−M₂′−2 assignment must fail the
fixture); and a `--classes` mode emitting the (n′,m′,ℓ,V₂′) partition of any
cohort — which is Card A's input and §3.2's measurement in one command.

**Why this one and not more compute.** guided_gb + the staged emitter already
removed the compute wall (17(xxxxx),(bbbbbb)); the remaining recurring failure
mode is *arithmetic drift in the descent*, which has cost one erratum and one
void certificate in twenty-four hours. A 60-line frozen module with a golden
test removes that class of error permanently.

---

## OPENS RAISED

- `OPEN[PROP63-RADIUS-DISCHARGE]` — the Proposition 6.3 radius hypothesis is
  discharged for **at most** the u_s = 1 descended skeleton rows; measured on
  the frozen (99,66) enumeration, `prop63_automatic` is true for exactly 2 of
  the 8 skeleton rows and false for **at least** 6 including S8 and the D = 108
  no-split row, so every u_s >= 2 descent kill carries an unaudited hypothesis
  obligation.
- `OPEN[LATTICE-DEGREE-IDENTITY]` — the uniform unsplit descended identity
  deg(g^2 - f^3 - lambda f) = K + ell + 2 is proved only at descended Jacobian
  exponent ell = 4; the count of distinct descended Jacobian exponents ell
  required by the eight (99,66) admissible skeletons is **at least** 3 distinct
  descended Jacobian exponents ell (namely ell = 2, 6, 8 beyond ell = 4), so
  an ell-uniform derivation is owed before any descended-class sweep.
- `OPEN[A0-GENERICITY]` — whether the tail weight data together with a nonzero
  weight-0 coefficient a_0 forces dimension = 0; the sole banked failure at
  t = 2 has a_0 = 0 exactly, and the free coefficient count of the universal
  weighted tail at t = 2 is **at most** 18, so this genericity question is
  decidable by one small elimination.
- `OPEN[RESULTANT-NORMALISATION]` — the weighted resultant of the eliminant
  square system is not invariant under rescaling the tail generators; the norm
  of the t = 3 resultant carries primes 59 and 73 with exponents **at least**
  60, so the target "closed form in t for the resultant" is ill-posed until the
  generator rows are made primitive over the integers.
- `OPEN[DESCENT-CLASS-SPLIT-HALF]` — a kill at the level of a descended class
  discharges the no-split descent half only; the number of skeleton rows with
  u_s >= 2 in the census range n <= 200 is 6209 while the number of descended
  classes is bounded by 1359, so **at least** 4850 rows would still owe an
  individual split-branch disposition after a complete class sweep.

**OPENs endorsed unchanged** (raised elsewhere, not re-raised here):
`OPEN[K16-Q-NONVANISHING-ON-GAMMA]`, `OPEN[8.1-VS-V0]`,
`OPEN[MOH-CENSUS-N1]` (retype: N1a citable / N1b hole, §2.3),
`OPEN[ROUTING-MAPS]`, `OPEN[U-NEGATIVE-CONFIG]`, `OPEN[DESCENT-STATE-S3]`,
`OPEN[B4-GLOBAL]`.

**OPENs I would retire:** `OPEN[H1-NONRES-PREDICATE]` — refuted 0/274 by
17(ttttt); keep the census, drop the predicate.

### Collision scan

`python3 ops/open_collision.py xmodel/ideation-20260905T0000Z-opus5.md --root .`
→ exit 0, `status: CANDIDATES`, 43 candidate lines over 5 raised OPENs.

- `OPEN[PROP63-RADIUS-DISCHARGE]` — **NONE**. New.
- `OPEN[A0-GENERICITY]` — **NONE**. New.
- `OPEN[LATTICE-DEGREE-IDENTITY]` — 30 candidates, **all lexical false
  positives** (as109/quintic/gcd3 "degree identity" and "`y`-degree" lines from
  the 20260824–27 corpus; none mentions the descent, the k=4 ray, or the K+6
  theorem). Reviewed and dismissed; the OPEN stands as new.
- `OPEN[RESULTANT-NORMALISATION]` — 3 candidates: AUDIT 17(hhhhh), 17(jjjjj)
  (both about the (99,66) gauge normalisations N3/N4 — a different
  "normalisation") and `k16-t5t6-grok46` prompt line 1 (the A_t = Q[y]/(H_t)
  normalisation chain — **adjacent but not the same claim**: that line is about
  the promoted pivot normalisation, not about the scale-dependence of the
  resultant). Reviewed; the OPEN stands as new, with 17(wwww) named as the
  target it repairs.
- `OPEN[DESCENT-CLASS-SPLIT-HALF]` — 9 candidates, all the
  QUALIFICATION[17(tttt)] / configuration-trichotomy family. **Adjacent and
  worth the reviewer's eye**: this OPEN is the census-scale generalisation of
  the same split/unsplit bookkeeping that produced the case-(A) qualification.
  It is not subsumed by it (that qualification was about one row; this is about
  ≈4,850 rows), but a merge is defensible if the coordinator prefers one entry.

Same-round submissions and the running lane's unsealed report are excluded from
the corpus automatically by the 2026-09-04T08:40Z scanner guard.

---

## Replay

Everything marked PROVED-HERE is desk-scale (< 10 min, < 4 GB) and reproducible
from frozen inputs only. No canonical ledger was edited; `jc2-lean` was not
inspected; no lane report of the running lane was opened.

| § | Claim | Inputs | Cost |
|---|---|---|---|
| 1.1 | H_t = 12(2t+1)²y²−12(t+1)(2t+1)y+(t+1)(3t+2); A_t = Q(√(3(t+1))) | the four `minpoly=` lines of `box/k16brcr-20260903/brcr_t{3,4,5,6}_exact.sing` + the charged t=2 roots | fit + 4 checks, seconds |
| 1.2 | α_2 = 0 at y=1/5 | `box/k16hsop-20260903/alpha_norm_audit.out` (banked, re-read) | 0 |
| 1.3 | W_r weights 18/20; W_1\|_{b₄=0}=0; W_2\|_{b₄=0}≠0; Res_q(W_1,W_2)≠0; its norm's prime content | `box/k16brcr-20260903/explicit_tail_t3_exact.txt`, sympy, exact over Q[yy]/(H_3) | 4.9 s (resultant) + ~60 s (norm content) |
| 2.1 | u_s = d_s−V_s; (n′,m′)=((n/d_s)u_s,(m/d_s)u_s); ℓ = d_s−2u_s−1; 2K′+3ℓ=30 | `box/mohprog-drivers-20260903/repro/moh_skeleton_full.py` (clean import into /tmp) + the batch-2 table as fixture | < 5 s |
| 3.2 | 24,063 rows / 6,209 u_s≥2 / 1,359 classes / 586 (n′,m′,ℓ); ℓ-histogram | same enumerator, 16 ≤ n ≤ 200 | ~90 s |
| 4.3 | `prop63_automatic` true iff u_s = 1 on all 8 rows | `box/g9966n1b2-20260903/enumeration.json` | 0 |

**FALLACY-v2 self-check.** No exit-price assertion is made, so no
`charge_basis=` line is required or given. Flag/place/series: the descended
4-tuple, the (K,ℓ) lattice point, and the joint chart are kept distinct
throughout — §3.3 and §2.2 state explicitly that equal descended data does not
entail equal charts and that a class kill is `DEAD[DESCENT-HALF]` only.
Floor/attainment: §3.2's compression figures are counts of an exact partition,
not bounds on lane cost; the per-chart 2.4–9.2 s figures are cited as *measured
banked* costs of *other* charts, not as predictions for these. Variable/ring
map: §1.3 declares the ring (A_3 = Q[yy]/(588yy²−336yy+44)), the weights
(b₄:1, q_{2,0}:2, b₃:t+1), and the dehomogenisation chart (b₄=1, with the b₄=0
locus settled separately) before using them. `sat()` is not used. No claim
here promotes a modular result to characteristic zero.

---

## Summary in one paragraph

K16 does not need another structural lane; it needs two cheap experiments and
one retirement. A_t is the quadratic field Q(√(3(t+1))), so the "wrong root"
hazard exists only at the eight split indices t = 3m²−1 below 200, and the one
observed failure (t=2, y=1/5) is exactly a₀ = 0 — which means the untested
question "do the weights plus a₀ ≠ 0 already force dim 0?" is the live one, and
the resultant target that four lanes chased is ill-posed because the resultant
is not scale-invariant. On the other side, the (99,66) N1 problem is smaller
than the packet thinks and the k=4 ray is less canonical: the eight admissible
skeletons obey u_s = d_s − V_s and descend onto **one line, 2K′+3ℓ = 30**, with
only four distinct descended degrees, of which two are already dead; the ray is
the slice ℓ = 4. Building the (K, ℓ, V₂′) descended chart once — instead of five
joint charts — closes N1's descent half, compresses the u_s ≥ 2 skeleton census at n ≤ 200 by 4.6×
(6,209 rows → 1,359 descended classes, measured), and is the only object in the campaign that is
uniform in anything on the (H2) side. Before any of that is published, someone
should discharge Prop 6.3's radius hypothesis: it is automatic exactly when
u_s = 1, and every u_s ≥ 2 kill the campaign owns — including D = 108 — is
sitting on it.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `42641`.
- Body SHA-256:
  `0c417cddd5e31e12bf3d582438995ab7e94cb3017c372c02956c90db1ea12918`.
- Frozen basis: `2358a71e8c4c034ac2447aec6af88fb882842e6f`.
