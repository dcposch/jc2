# Ideation round 20260905T0000Z — Fable 5 blind submission

Lane `ideation-20260905T0000Z-fable5`; basis `2358a71e`; adapter claude (Fable 5.1).
Desk artifacts: `box/ideation-20260905T0000Z-fable5/` (screen replay, p-adic profiles,
degeneration scripts and Singular transcripts).

**Custody.** The manifest was generated mechanically from
`xmodel/ideation-20260905T0000Z-fable5.run.v2` (`awk -F=` pairing
`charged_input_<i>_sha256=` / `charged_input_<i>_basename=`) and checked with
`sha256sum -c`: **4/4 OK** (packet, 12:00Z synthesis, FALLACY-v2, COORDINATION); no digit
retyped. Read afterwards: AUDIT.md deltas 17(ppppp)–(dddddd) and the load-bearing older
deltas 17(p)/(r)/(gg)/(hh)/(ll), notes.md newest LIVE STATE and every EVENT of 2026-09-04,
APPROACHES.md overlays and master table, PROGRESS.md, the sealed reports named in the
packet (k16-hsop/rank/nzd/brcr, k4ray-unsplit/K89, g9966-n1-skeletons/batch2), Moh 1983
pp.183–186, 194, 196–198, 200–202 (pdftotext text layer). NOT read: any
`ideation-20260905T0000Z-*` submission (including the coordinator's committed one);
the running lane `g9966-n1-batch3-opus5-20260903` (receipt has no `final_status`; no `.md`
exists yet) — receipt only. No ledger edited; no `jc2-lean`.

**FALLACY-v2 posture.** No exit-price assertion is made anywhere below, so no
`charge_basis` line is due. Every "closed"/"dead" statement below is either a consumption of
a promoted delta (cited) or a desk replay of a charged driver (path given), never a new
promotion.

## 0. Headline — direct answers, and where the packet's framing is wrong

Four direct answers, then two framing corrections that change what the round should launch.

**Q1 (K16 atom).** I do not have the uniform proof, and I say so first. What I add is (a) a
reformulation that is the right *language* for any valuation/specialization argument — (V0)_t
is the statement that the t−1 forms G_r = B_r X + C_r are an hsop of the **double cover**
R_t = P_t[X]/(a_0X² + b_0X + c_0), with W_r = a_0·N_{R/P}(G_r) the norms and the X_rs of FITT the
mixed traces; (b) a **new mechanism, tested at the desk and not closing**: a p-adic (valuative)
Gröbner degeneration at the top-index prime p = 4t+1, motivated by a MEASURED arithmetic
regularity (§1.2: on one fibre above 4t+1 every b_r, c_r is 𝔭-divisible while a_r ≡ u_r·b4^r;
t = 3, 4). The first weight (b3-weight 1/2) gives an initial system of dimension 1 (t = 3)
and 2 (t = 4), so that instance is dead; the mechanism itself (initial ideals w.r.t. a
valuation are immune to NO-COPRIME-LEADERS and DEGREE-BLIND) stays typed OPEN with a
minutes-scale cheapest test; (c) a **falsification target the ledger has not decided**: t = 11
has rational fibres (t+1 = 3·2²) exactly like t = 2, and the b4 = 1 chart at t = 11 timed out
in both t11 lanes — the d = −k fibre is where t = 2 failed. Decide it before spending another
structural lane. Recommendation: the JC2-relevant target is (8.1), an *inconsistency* of the
affine b4 = 1 chart, and the honest instrument for it is a unit certificate (guided_gb, exact
Q), not a dim-0 certificate; K16 stays fixed-t until the t = 11 datum is in.

**Q2 (degree-wide (99,66)).** The packet's N1 framing is wrong in a way that costs lanes. I
replayed the charged whole-tree screen driver (`box/centre-gate-20260903/rerun_screens.py`,
imports unmodified) on the eight (1)–(13)-admissible (99,66) rows: **seven of eight are DEAD
under the PROMOTED operative screen** (17(r) whole-major-tree necessity; 17(hh)
LEMMA[ZERO-FACTOR-CENTRE], ungated Prop 5.6; 17(ll) operative C_FULL_TREE_POLYNOMIAL_ODE) and
only the printed row S8 = V(8,8) survives. S1, S4, S5, S6 die already at the gap-free
partition level (Theorem p.200 (4)–(7)); S2, S3, S7 die under ungated Prop 5.6. So N1 is
closed **by citation of promoted deltas**, not by five joint-chart Gröbner kills; the running
batch-3 lane is a redundant instrument cross-check. Moh's "private program" is not private:
it is the p.200 Theorem (4)–(7) plus Props 5.5/5.6, which the campaign's second reader
recovered on 2026-09-03 ("s = 3 EXACT at n ≤ 100 — Moh's six", 17(ll)). Completeness of
(1)–(13) *plus* the tree conditions is citable to printed theorems. What is NOT citable is
"Moh's ≤ 100 theorem resolved": the operative screen leaves **14 excess rows at n ≤ 100**
((90,60)×4, (96,64)×4, (96,72)×6, all s ≥ 4, u_s = 1; OPEN[MOH-PROGRAM-ARTIFACT], 17(ll)),
so the ≤ 100 statement needs those fourteen u_s = 1 descents killed too.

**Q3 ((H1) census).** No uniform theorem: 17(lllll)/(ooooo)/(ttttt) closed all three
candidate shortcuts, and the K+6 pin theorem is ray-specific. The efficient path is a
batched guided_gb sweep whose cost is dominated by *chart construction* (pin + exact
lower-band parametrization), not by std: K = 7 died in 8 s once reduced, K = 8, 9 in
minutes at 36 variables after failing at 58–74. Price: 166 groups × (one reduction script
per shape) — the reductions are shape-generic (the h-adic tower is the same for every
e = 3, q = 2 row), so the sweep is one compiler plus ~2 lane-hours per shape class, not
per row (§3). Before sweeping, re-screen the cohort with the same whole-tree driver: the
Q2 replay shows that screen kills 7/8 at one degree; it will thin the 296 rows.

**Q4 (the finish).** Two corrections to the coordinator's framing, in opposite directions.
(i) *Under*-read: the 12:00Z "one-place leak" is closed for a minimal counterexample by
Moh's own **Prop 5.4 + Lemma 5.3** (p.183, p.185, read here): if the smallest disc has
logarithmic radius > −1 then either k[f,g] = k[x,y] or an automorphism reduces the degrees
of f, g and T_1* simultaneously; a counterexample of minimal total degree therefore has
radius −1, hence M_s = n−2 with two points at infinity. So the two-point line is not a
stratum of plane JC2 — for minimal counterexamples it *is* plane JC2, conditional on Prop
5.4's proof and the normalization (3) of p.200. (ii) *Over*-read: the degree-wide method
(enumerate admissible skeletons at a degree, kill each) is a per-degree algorithm; it
extends Moh's bound (≤ 100 → ≤ 150 → …) but can never produce the all-degree theorem,
because admissible skeletons come in infinite rays (K16, k = 4) and both rays are stuck at
exactly "uniform in the index". The single most valuable next object is therefore not a
row and not a census: it is **the scope theorem** (Prop 5.4 + Lemma 5.3 + the minimality
normalization, one lane-hour, typed) — it decides whether the endgame is "two-point stratum"
or "plane JC2", which changes every allocation below — followed by a uniform-in-index kill
on one ray.

## 1. Q1 — K16: the atom, one new mechanism tested at the desk, and what to do instead

### 1.1 The atom, restated in the language a structural proof needs

Consumed (17(ppppp)/(rrrrr)/(uuuuu)/(wwwww)): with P_t = A_t[b4, q_{2,0..t−1,0}] (weights
1..t−1), S_t = P_t[b3] (weight t+1), the top row T_{t,2t−1} = a_0b3² + b_0b3 + c_0 with a_0
a unit, and G_r = B_r b3 + C_r. Two observations that are not in the ledger and that I think
are the right frame for any valuation/specialization idea:

* **Double cover.** M_t = S_t/(T_{t,2t−1}) is the quadratic P_t-algebra
  R_t := P_t[X]/(q(X)), q = a_0X² + b_0X + c_0, i.e. the ring of the double cover
  Y_t → Spec P_t branched along disc(q) = b_0² − 4a_0c_0. The G_r are X-linear elements of
  R_t, and (V0)_t ⟺ (G_1..G_{t−1}) is an hsop of the (t−1)-dimensional CM ring R_t. The
  eliminants are norms, W_r = a_0·N_{R/P}(G_r) (direct check: N(B_rX + C_r) =
  B_r²XX' + B_rC_r(X+X') + C_r² = (c_0B_r² − b_0B_rC_r + a_0C_r²)/a_0), and the FITT cross
  terms X_rs are the mixed traces Tr(G_rG_s^σ). So criterion RANK's clause (ii) says: no
  point of Y_t \ 0 is a common zero of the G_r. This is the statement to which a
  valuation on Γ, a sheet-involution argument, or a norm certificate would apply; the
  Gröbner view hides it.
* **Real target is inhomogeneous.** The ledger's chain ends at (8.1), and (8.1) at the chart
  level is: the affine system {T_{t,k} = 0, k = 0..2t−1} ∩ {τ_t = c} is EMPTY, i.e. the
  b4 = 1 chart of I_{t,+} together with τ_t − c is the UNIT ideal (τ_t has positive weight,
  so a nonzero cone point with τ_t ≠ 0 rescales to a solution of τ_t = c). This is a
  unit-ideal question — a Nullstellensatz certificate 1 = Σ h_k T_{t,k} + h·(τ_t − c) — and
  every unit-ideal question is a *finite linear algebra problem* in bounded degree
  (effective Nullstellensatz), which is exactly what guided_gb's UNIT_IDEAL_CHAR0 route
  answers. The four deep lanes went after dim-0 of a homogeneous ideal (stronger, and
  provably resistant to leading-term methods); the JC2-relevant question is weaker and
  has a different instrument. The b4 = 0 half is already cheap at t = 8 (34 s, 17(kkkkk)).

### 1.2 The new mechanism: arithmetic degeneration at p = 4t+1 — measured, tested, not closing

The packet asks for "a valuation, a specialization argument". A p-adic Gröbner degeneration
is both, and it is immune to the two impossibility theorems: for a homogeneous ideal J over
a valued field and any weight ω on the variables, the initial ideal in_ω(J) over the
residue field has the same Hilbert function as J (flat degeneration over the valuation
ring), while the initial forms of the *generators* are polynomials over F_p, not
monomials — so NO-COPRIME-LEADERS (which needs pure powers) and DEGREE-BLIND (which
ignores coefficient arithmetic) do not bite. If for some (p, ω) the initial forms of the t
tail rows already cut out {0} over F̄_p, then (V0)_t holds in characteristic zero.

**Measured (desk, sealed rows of 17(wwwww) in `box/k16brcr-20260903/explicit_tail_t{3,4}_exact.txt`,
scripts `padic_profile*.py`, `padic_abc.py`).** Hensel-lifting each root of H_t mod p and
taking p-adic valuations of every coefficient (a·yy + b) at that root:

| t | p | fibre (yy mod p) | a_r | b_r, c_r | initial monomials of T_{2t−1−r} |
|---|---|---|---|---|---|
| 3 | 13 = 4t+1 | 10 | units, initial term b4^r | ALL valuation exactly +1 | b3², b4·b3², b4²·b3² |
| 3 | 13 | 11 (conjugate) | units | ALL valuation −1 (poles) | dense |
| 4 | 17 = 4t+1 | 13 | units, initial b4^r | ALL valuation exactly +1 | b3², b4b3², b4²b3², b4³b3² |
| 4 | 17 | 14 (conjugate) | a_0 has valuation +1; a_r poles −r | poles | — |
| 3 | 23, 37 (generic split) | both | units | units, dense | dense |
| 5 | 7 (7 | 21 = 4t+1) | 2 | mostly units | mixed 0/−1/−2 | not clean |

So above the **top-index prime 4t+1** (the w-degree of the top row) one fibre has the
whole b3-linear and constant tail divisible by 𝔭 with a_r ≡ u_r·b4^r, and the conjugate
fibre has the mirror poles. This is a genuine arithmetic regularity of the spine (a
scan of all split primes below 200 at t = 3 finds it only at p = 11 = 3t+2 (a denominator
prime, poles) and p = 13, plus one deep-pole prime 59). At t = 4 the conjugate fibre even
has a_0 ≡ 0 mod 𝔭 — a mod-p shadow of the t = 2, y = 1/5 degeneration where a_0 = 0
exactly. It is not clean at t = 5 with the composite 4t+1 = 21.

**Tested and negative (first weight).** With b3-weight λ = 1/2 the initial forms at the
good fibre are u_r b4^r b3² + c̄_r(b4, q) (c̄_r = (c_r/p) mod p; the b_r b3 terms drop out,
valuation ≥ 3/2). Eliminating Z = b3² gives t−1 b3-free forms D_r = u_0c̄_r − u_r b4^r c̄_0;
Singular over F_13 / F_17 (`degen_t3_p13_y10.sing`, `degen_t4_p17_y13.sing`): dim = 1 (t = 3),
dim = 2 (t = 4) — the initial system of the generators is positive-dimensional
(c̄_0 is a single monomial and every c̄_r is b4-divisible), so this weight proves nothing.
Other weights (λ ≠ 1/2, or weights on the q's) and the full initial ideal (the tropical
prevariety of the tail at 𝔭) are untested; that is the OPEN in §9 with a minutes-scale test.
I record the mechanism because it is the only route named in this round that is not
already refuted by a theorem, and because the 4t+1 regularity is new data about the spine
that a closed form for b_r, c_r (17(wwwww)'s missing enabler) must reproduce.

### 1.3 The falsification the ledger has not decided: t = 11

t = 2 has rational fibres because 3(t+1) = 9 is a square, and one fibre (d = −1, y = 1/5)
fails (V0). The next rational cases are t + 1 = 3k²: t = 11 (d = ±2, y = 7/23, 5/23), 26, 47.
Both t11 lanes (`k16-t11-cone-gpt55`, `k16-t11-modular-gpt55`) report the b4 = 1 chart
INCONCLUSIVE_TIMEOUT at t = 11 on both fibres; only the array recurrence passed. So
(V0)_11 on the d = −2 fibre is *undecided*, and it is the one place a uniform statement can
cheaply die. Cheapest test (≤ 1 lane-hour): tail rows only (t = 11 rows in 11 variables,
already emitted mod 1009/53 in `box/k16t11-20260903/`), b4 = 0 slice first (expected
seconds), then the b4 = 1 chart under guided_gb with the CI Hilbert hint
(1+s¹²)·[34 choose 10]_s (CI-SERIES gives the exact hint). Outcomes: dim 0 on both fibres →
the t = 2 failure is the a_0 = 0 accident and the all-t statement stays plausible; POSDIM on
d = −2 → (V0)-for-all-t is FALSE and only (8.1) remains as target (as at t = 2, y = 1/5, where
(8.1) holds while (V0) fails — check τ_11 on the surviving component).

### 1.4 Recommendation

Stop launching all-t (V0) lanes until 1.3 is decided; if it survives, the next structural
lane should be the double-cover/valuation frame of 1.1 with the 4t+1 data of 1.2 as its
input, targeting a closed form for b_r, c_r *modulo 𝔭_{4t+1}* first (the reduction kills
the q-terms of a_r and makes c̄_0 a monomial — a far smaller object than the exact
recursion of 17(wwwww)). For JC2 itself, keep the fixed-t (T) ladder (t ≤ 7) and price
t = 8 via the unit-ideal instrument of 1.1, not the cone.

## 2. Q2 — degree-wide (99,66): N1 is already closed by the campaign's own promoted screen

### 2.1 The desk replay: seven of the eight admissible skeletons die under the promoted screen

`box/ideation-20260905T0000Z-fable5/screen_9966_rows.py` imports, unmodified, the machinery of
the charged centre-gate driver `box/centre-gate-20260903/rerun_screens.py`
(`moh_skeleton_full_frozen.census`, `opus5_probe.Tree`, the same `ok()` call and window
test), restricts to n = 99, m = 66 (exactly the 8 rows of 17(cccccc)'s enumeration —
same M, d, V), and runs the same five screens the driver runs at n ≤ 100:

| id | M₂ | V=(V₂,V₃) | u_s | PARTITION (gap-free tree, no Prop 5.6) | PARTITION_ODE | UNGATED (Prop 5.6 ungated) | UNGATED_ODE = C_FULL_TREE_POLYNOMIAL_ODE | UNGATED_PASS |
|---|---|---|---|---|---|---|---|---|
| S1 | −22 | (1,9) | 2 | DEAD | DEAD | DEAD | DEAD | DEAD |
| S2 | 22 | (1,7) | 4 | survives | survives | DEAD | DEAD | DEAD |
| S3 | 22 | (5,7) | 4 | survives | survives | DEAD | DEAD | DEAD |
| S4 | 22 | (1,8) | 3 | DEAD | DEAD | DEAD | DEAD | DEAD |
| S5 | 22 | (1,10) | 1 | DEAD | DEAD | DEAD | DEAD | DEAD |
| S6 | 55 | (2,10) | 1 | DEAD | DEAD | DEAD | DEAD | DEAD |
| S7 | 77 | (8,7) | 4 | survives | survives | DEAD | DEAD | DEAD |
| S8 | 77 | (8,8) | 3 | survives | survives | survives | survives | survives |

Corroboration from the frozen enumerator itself (`box/moh_skeleton_full.py`, `Skel.any10`,
"the numerical shadow of Moh's Prop 5.6 remark"): S3 and S7 pass (10)/(11) at j = 2 only
through the (11) branch (α = 0), i.e. `any10 = False`; all other rows have `any10 = True`.
So the two u_s = 4 rows with V₂ ∈ {5, 8} are exactly the ones the printed Prop 5.6 remark
("(11) can not always happen") targets, and the tree screen kills them for that reason.

**Provenance of the kill (all promoted; nothing new is promoted here).** (i) Whole-major-tree
necessity — every above-threshold factor at every node must extend — PROVED-IN-SOURCE from
Moh's Theorem p.200 (4)–(7) and Props 4.6/5.3 (17(p), Sol second reader; two independent
tree implementations) and PROMOTED as a named derived necessary filter after a
different-model gate (17(r)). This alone kills S1, S4, S5, S6. (ii) The ungated Prop 5.6
zero-chain kill is a theorem for all still-centred all-zero major chains —
LEMMA[ZERO-FACTOR-CENTRE], PROMOTED 17(hh) (gated by GPT-5.5 with a proof correction);
the 204 → 55 restoration at n ≤ 100 is its measured signature. This kills S2, S3, S7.
(iii) The resulting operative screen C_FULL_TREE_POLYNOMIAL_ODE was re-based on every live
target in 17(ll) with the explicit statement "s = 3 EXACT at n ≤ 100 (Moh's six)" — which
already *implies* the table above, since all eight (99,66) rows have s = 3 and Moh's six
contain one (99,66) row. Nobody drew the implication on 2026-09-04.

### 2.2 What this does to N1, to "not source-closable", and to the running lane

* **N1 is closed by citation**, with the chain: (99,66) Keller pair, normalized as p.200
  (1)–(3) ⇒ characteristic data satisfy (4)–(13) [Moh, printed] and the whole-major-tree
  obligation [Moh Theorem p.200 (4)–(7) + Prop 5.6, as PROMOTED in 17(r)/(hh)] ⇒ one of
  S1..S8 [enumerator, 17(cccccc), reproduced here] ⇒ S8 [table above] ⇒ dead in all three
  configurations [17(pppp), 17(tttt), 17(bbbbbb)]. The 12:00Z verdict "N1 is NOT
  source-closable" (mine among the three) was wrong: it took Moh's (1)–(13) for the whole
  printed sieve. The p.200 Theorem's disc-tower conditions are printed and were already
  sourced by the campaign a day earlier. Moh's "private program assertion" is not private.
* **The remaining N1 obligation is paper-grade, not mathematical**: the Theorem 8.1 dossier
  (17(hhhhh)) must cite the screen kill explicitly per skeleton (which condition kills which
  row, with the tree witness the driver already prints), and the whole-tree screen's
  promotion record must be attached. That is a dossier lane of ≤ 2 hours, not a compute lane.
* **Running lane g9966-n1-batch3-opus5**: its five joint-chart kills (2271–3441 coefficients)
  are *redundant* with a promoted theorem. They retain one value — an independent
  instrument agreeing with the screen at a degree where the screen's whole content is
  exercised (all three kill mechanisms fire among S1–S7). Recommendation in §7: REDESIGN to
  one skeleton as a cross-check, stop the rest.
* **Uniform argument across the eight V-assignments (Q2's actual question): YES, and it
  already exists** — it is not a Jacobian obstruction parameterised by V but the disc-tower
  necessity, whose parameter is exactly V. S1/S4/S5/S6 fail because a V-assignment must
  extend a consistent major tree at every node; S2/S3/S7 fail because their surviving
  chains are all-zero and still centred (Prop 5.6). Killing S1–S4, S7 by Gröbner would prove
  the same thing a second time with a weaker instrument.

### 2.3 Is (1)–(13)-completeness citable, or a gap? — Citable, with two named caveats

Completeness = "every degree-(99,66) Keller pair, normalized as p.200 (1)–(3), has one of the
eight skeletons". The numerical conditions (4)–(13) are stated on p.200–201 with their
sources (Def 5.1, Prop 5.5 for (12)/(13), Prop 5.6 for the (11) remark, Cor 6.1 for d_s ≥ 4),
and the enumerator implements them verbatim with Moh's table as a fail-closed control
(control 4). Two caveats, both typed and both cheap:

1. **The normalization (3)** "J = 1 and the degrees of f and g cannot be reduced
   simultaneously" is a minimality assumption. A degree-wide statement "no Keller pair of
   degrees (99,66)" therefore reads, honestly, "no Keller pair of degrees (99,66) whose
   degrees are not simultaneously reducible"; the unrestricted statement follows only if
   every simultaneously-reducible (99,66) pair reduces to a pair of smaller degree that is
   itself dead — i.e. only inside a "≤ 100" induction. That is Moh's framing, and it is
   why the theorem to state is "≤ 100", not "(99,66)".
2. **The "≤ 100" theorem is not closed by (99,66) alone.** Under the operative screen the
   n ≤ 100 census keeps 20 rows / 7 classes: Moh's six plus **14 excess rows** in (90,60)×4,
   (96,64)×4, (96,72)×6, all s ≥ 4, u_s = 1 (17(ll); OPEN[MOH-PROGRAM-ARTIFACT] = 14). Each
   is a Prop 6.3/6.4 descent (u_s = 1, automatic radius) to a monomial-Jacobian pair — the
   receiver world of row 1 — and the Appendix II compiler found the analogous excess rows
   to be s' > 2 (17(bb)), i.e. OPEN[DESCENT-STATE-S3]. So the packet's "the published open
   case of Moh's ≤100 theorem RESOLVED" is an overclaim on two counts: the (99,66) closure
   was already in hand by citation, and ≤ 100 needs fourteen more rows. Cheapest test: the
   compiler on the 14 rows (≤ 1 lane-hour to type each as dead / s' > 2 / open).

Also citable and relevant to the same theorem: Moh's M_s = n−2 restriction on p.194 is not
an assumption but Prop 5.4 + Lemma 5.3 (§4.1), so the two-point census is exhaustive for
pairs satisfying (3). One-place (99,66) pairs are excluded by the same printed theorem.

## 3. Q3 — the (H1) census: pricing the three paths

### 3.1 The three named paths, priced against the banked timings

The banked method (17(zzzzz)/(aaaaaa)/(bbbbbb)) has three stages with very different costs:

| stage | what | measured cost | scales with |
|---|---|---|---|
| A. structural pin | LEVEL-4 pin β_b = μ·y^{K−3}(y−x) from the K+6 theorem | derivation, minutes (sympy) | ray-specific: needs e = 3, q = 2 and the two-point form y^{K−1}(y−x) |
| B. exact lower-band parametrization | solve the injective bands by hand-built scripts → 36 ring variables | the whole lane (Sol, ~2 h) per row | the row's band structure; *reusable across rows of one shape* |
| C. guided_gb | std with Hilbert hint, 3 primes + exact Q | 8 s (K = 7), minutes (K = 8, 9) at 36 vars; timeout at 58–74 vars | number of surviving parameters after B |

So "batched guided_gb sweep" is the cheap part and is not the bottleneck; "uniform
pin + parametrization theorem" is the expensive part and is the bottleneck; the
"augmented-Schur-row theorem" is dead as a uniform mechanism (17(lllll): the killing row is
not skeleton-determined; 17(ooooo)/(ttttt): disc and NONRES refuted). Pricing:

* **Batched sweep as-is (per-row hand reduction):** 166 groups × ~2 lane-hours ≈ 330
  lane-hours. Not a plan.
* **Shape-class compiler (my recommendation):** the u_s ≥ 2 census rows descend to pairs
  (n', m') = u_s·(n/d_s, m/d_s) with J = c·γ^{v_s−u_s−1}; stage A/B depend only on the
  descended *shape* (e, q, k, the two-point multiplicities (V₂', K'−V₂')), not on the
  original degree. The (99,66)/D=108/δ₁'=0 rows were one shape class (e,q,k) = (3,2,4) at
  three K's. Count shape classes in the 296-row cohort first (desk, minutes: group by
  (e, q, k, V₂'/K')); my expectation from the enumeration data is a few dozen. Then one
  compiler that emits the pin + lower-band reduction from the shape (the h-adic tower
  f = h² + 2β, g = h³ + 3βh + (3/2)α is generic in e = 3, q = 2; other (e,q) need their own
  approximate-root tower) and guided_gb per row. Price: ~1 lane-day to write and validate
  the compiler on the three banked kills (replay K = 7, 8, 9 exactly — the control), then
  ~10 min compute per row. That turns 330 lane-hours into ~2 lane-days.
* **Uniform theorem:** none is in sight; 17(zzzzz) shows the degree tower saturates at
  c = 3 even on the best-understood ray. Do not price a lane for it this round.

### 3.2 Re-screen before you sweep

The Q2 replay is a warning for the cohort: the "sharpened Xu-ok cohort = 296 rows / 166
groups" was audited under the operative screen (17(ttttt) says so), but it was assembled
as a u_s ≥ 2 *two-point* cohort and the (99,66) rows S1–S4, S7 — all u_s ≥ 2, all
Xu-consistent (17(cccccc) built face charts for them) — die under the whole-tree screen.
Cheapest test (minutes, the script of §2.1 generalised to the cohort's (n,m) list): run
`rerun_screens`'s UNGATED_ODE on all 296 rows and count survivors. Interpretation: if a
large fraction dies, the census deliverable shrinks before any chart is built; if none
dies, the cohort was already screened and the compiler plan stands as priced.

### 3.3 What the census cannot deliver, stated once

Even at 296/296 dead, (H1) is closed only at D ≤ 200. The all-degree (H1) needs the
per-shape argument to become uniform in K within each shape class (the ray problem
again). The census is worth its two lane-days as a *regression client* for the compiler
and as the empirical base for a uniform-in-K conjecture per shape class; it is not a
proof program, and §4 prices it as such.

## 4. Q4 — the finish: the framing, corrected in both directions

### 4.1 The under-read: the one-place leak is closed for minimal counterexamples by Moh's Prop 5.4

The 12:00Z synthesis (Grok's leak (1), accepted 4/5 with my vote) typed "(H1)∧(H2) reduces
the TWO-POINT M_s = n−2 stratum ALONG MOH'S LINE, NOT all of plane JC2; one-place is a
different program". I read the source this round (pdftotext layer of pp.183–186, 194):

> **Prop 5.4** (p.183): "Suppose g(x,y) is monic in y with y-degree n > 1 and a tower of major
> discs D_s ⊇ … ⊇ D_1 is constructed. Then the smallest disc which contains all roots of
> g(y)T_1*(y) is the D_i with [displayed index]. Moreover if δ_i > −1 then either
> k[x,y] = k[T_1*, g] = k[f, g] or there exists an automorphism of k[x,y] which reduces the
> degrees of T_1*(f,g), g and f simultaneously."
> **Lemma 5.3** (p.185): "the smallest disc which contains all roots of g(y)T_1*(y) is of
> logarithmic radius −1 iff M_s = n − 2 and the highest homogeneous form of g(x,y) has two
> roots with one root having multiplicity v_s …" (proof: "It follows from Proposition 5.4
> and 5.3 … Thus M_s = n−2"), with the one-place case flagged on p.183 as "(cf. [A.1], p.14)
> 'one point at infinite'".
> p.194: "As pointed out in Proposition 5.4 and Lemma 5.3 we shall only consider the case
> M_s = n−2 and the highest homogeneous form of g equals [(y−ax)^{v_s}(y−bx)^{u_s}]^{n/d_s}."

So for a Keller pair that is not an automorphism and whose degrees cannot be reduced
simultaneously (Moh's normalization (3), p.200 — satisfied by a counterexample of minimal
total degree), the smallest disc has radius −1, hence M_s = n−2 and two points at
infinity with multiplicities (v_s, u_s). The one-place configuration is not a *separate
program*; it is the alternative branch of Prop 5.4 and it terminates in "automorphism or
degree reduction" — by [A.1], the Abhyankar–Moh one-place theorem, which is exactly the
tool the ledger says the program "never ate". It ate it on p.183. **Typed:** a READING of
printed theorems, CONDITIONAL on (i) Prop 5.4's proof (the campaign's ledger consumes Prop
5.4's "polynomial translation" but I find no delta consuming the "Moreover" clause) and
(ii) the elementary argument that a minimal-total-degree counterexample satisfies (3). It
is not promoted here; §9 raises OPEN[PROP-5.4-MINIMALITY] with a one-lane-hour test.
Consequence if it holds: (H1)∧(H2) plus the routing maps is a program for **plane JC2**, not
for a stratum — the coordinator's 00:00Z sentence was right and the 12:00Z correction
over-corrected; the remaining leaks are U-NEGATIVE (V₂' > d₂'), s' > 2, and the unproved
routing maps (first-separation, route-to-state, ordinary-support, receiver coverage), all of
which are *inside* the two-point program.

### 4.2 The over-read: the degree-wide method is an algorithm, not a theorem-generator

"Enumerate admissible skeletons at a degree, kill each" is, by construction, a decision
procedure for one (n,m) at a time. It generalises trivially to any finite range and
composes with Moh's induction to give "JC2 for deg ≤ N" for any N at which every admissible
skeleton has been killed (≤ 100 needs the 14 excess rows of §2.3; the census says ≤ 200
has 459 operative rows after POLY, 17(ll)). It cannot give the all-degree theorem, for a
reason the ledger already proved twice: admissible skeletons come in **infinite rays**
(K16 is cofinal, 17(w); the fixed-N = 6 family of 2026-09-03; the k = 4 ray), and on both
rays the campaign now has fixed-index kills (t ≤ 7; K ≤ 9) and a proved *saturation* of the
uniform methods tried (degree tower at c = 3; Gröbner/degree/resultant on K16). The
all-degree program is therefore exactly: **prove one uniform-in-index kill on one ray**, then
show every ray has the same mechanism. Nothing in the (99,66) closure moves that; it is a
milestone of the finite program.

### 4.3 The single most valuable next object

1. **The scope theorem** (Prop 5.4 + Lemma 5.3 + minimality ⇒ M_s = n−2 for a minimal
   counterexample): one lane-hour, decides whether the program is plane JC2 or a stratum, and
   retypes every allocation. Nothing else this cheap changes the campaign's *type*.
2. **A uniform-in-index kill on one ray**, and my pick is the k = 4 ray rather than K16:
   its tower is fixed-shape (only deg h grows), it has a proved uniform theorem
   (deg(g² − f³ − λf) = K + 6) and a proved uniform pin, and its residual is a *bounded
   family of charts indexed by (K, b)* with b in a window of width ~4K/3 — a two-parameter
   family in which the p-adic/valuative degeneration of §1.2 can be tried on honest
   polynomials over Q (no A_t, no spine). K16's residual is a curve of 3^{3t} algebraic
   points with A_t-coefficients; it is the harder of the two to make uniform.
3. Only then the census (§3), as regression for the ray mechanism.

### 4.4 Counterexample side, stated once

A real Keller pair would first appear as POSDIM + J = const on a *promoted-screen survivor*.
The screen replay of §2.1 says the (99,66) survivors are exactly S8's three configurations,
all dead; the honest places to look are the 14 u_s = 1, s ≥ 4 rows at n ≤ 100 (unvisited
descents, s' > 2) and the t = 11 rational fibre (§1.3). Neither has a SURVIVES today.

## 5. Disposition vector (changes only) and bottleneck reranking

Rows are APPROACHES.md's master union table (1–46) with the 2026-09-03/04 overlays; changes only.

* Row 1 (GGV corner / monomial-Jacobian receiver, [P,Q] = x^k): **unchanged** at flagship
  receiver, but **RETARGET** its next clients to the 14 excess u_s = 1 rows at n ≤ 100 (§2.3)
  — they are the only unvisited receiver data below Moh's bound and the only honest
  counterexample slots there.
* Row 3 (vertex-gap / strip ODEs): **LOWER one notch** — N2 is discharged (17(sssss)); the
  face-ODE instrument has no open client this round.
* Row 6 (Abhyankar–Moh one-place / coordinate recognition): **RAISE** — not as a route but
  as the *consumed* input of Moh's Prop 5.4 (§4.1); the row's "wrong object" verdict
  (fibres multi-place) does not touch Prop 5.4's use of [A.1] on the smallest disc. Re-read
  the row's essence as "the one-place branch of Prop 5.4 ends in automorphism/reduction".
* Row 5 (Jung–van der Kulk degree descent): **RAISE from "No" to "Partial (as normalization)"**
  — the minimality normalization (3) that §4.1 needs is precisely a JvdK-type statement
  ("no automorphism reduces both degrees"); it is load-bearing for the scope theorem.
* Row 20 (reduction mod p / p-curvature formalism): **REOPEN, retargeted** — not as the
  Belov–Kontsevich bridge (dead) but as the *valuative Gröbner degeneration* instrument of
  §1.2: the K16 tail has a measured arithmetic regularity at p = 4t+1, and initial ideals
  w.r.t. a p-adic valuation are the one degeneration not refuted by 17(ppppp)/(rrrrr).
* Row 36 (guided CE search): **RETARGET** to the t = 11 rational fibre (§1.3) and the 14
  excess rows; drop the R_4 residual (closed at K = 7, 8, 9).
* Row 46 (Lean / formal certification): **unchanged**.
* Program rows (overlay): "(99,66) skeleton verdict complete modulo N1" — **RETYPE to
  "complete; N1 closed by citation of 17(r)/(hh)/(ll), dossier pending"** (§2); "N1 = finite
  kill list of 5" — **LOWER to instrument cross-check**; "(H1)∧(H2) reduces the two-point
  stratum only" — **REOPEN as "plane JC2 for minimal counterexamples, conditional on
  OPEN[PROP-5.4-MINIMALITY]"** (§4.1); K16 all-t (V0) — **LOWER until t = 11 is decided**
  (§1.3); k = 4 ray uniform kill — **RAISE to the #1 all-degree object** (§4.3).
* All other rows (2, 4, 7–19, 21–35, 37–45): unchanged, no new evidence this round.

**Bottlenecks reranked (proof side).** (P1) OPEN[PROP-5.4-MINIMALITY] — one lane-hour,
decides the program's type. (P2) a uniform-in-K kill on the k = 4 ray (the (K, b)-family of
pinned charts; try the valuative degeneration there first, on honest Q-polynomials). (P3)
the t = 11 K16 datum (falsification-first). (P4) the N1 citation dossier + the 14 excess
rows (finishes "≤ 100" as a theorem). (P5) the shape-class compiler for the (H1) census
(regression, not proof). STOP: joint-chart Gröbner kills of S1–S4, S7 beyond one cross-check;
all-t (V0) lanes before (P3); any further arithmetic-shortcut hunt for (H1).

**Disproof side.** (C1) POSDIM + J = const on one of the 14 excess u_s = 1 rows at n ≤ 100
(their descents are unvisited, s' > 2). (C2) a (V0) failure at t = 11, d = −2 that is *not*
z-type (check τ_11 on the component). (C3) nothing on (99,66): every admissible skeleton is
dead by promoted screen or promoted chart.

## 6. Idea cards (three)

### Card A — SCOPE: Prop 5.4 + Lemma 5.3 + minimality ⇒ the two-point line is all of plane JC2 (NEW connection: row 6 ↔ the program's scope)

* **Target obstruction:** the typed leak OPEN[ROUTING-MAPS]'s outer wall — "one-place is a
  different program" — which caps the program at a stratum.
* **Mechanism:** Moh Prop 5.4's "Moreover" clause (p.183): smallest disc of radius > −1 ⇒
  automorphism or simultaneous degree reduction of (f, g, T_1*); Lemma 5.3 (p.185): radius
  −1 ⟺ M_s = n−2 with two points at infinity. Combined with "a counterexample of minimal
  total degree admits no simultaneous degree reduction" (elementary; a JvdK-type
  normalization, row 5) it gives: every minimal counterexample lies on the two-point line.
* **Dependencies:** a source read of pp.183–186 (Prop 5.4's proof uses [A.1] = Abhyankar–Moh
  and Prop 5.3); the (3)-normalization argument; nothing computational.
* **Cheapest discriminator (≤ 1 lane-hour):** a reader lane that (i) transcribes Prop 5.4's
  statement and the two branches of its proof from the 300-dpi renderings (the text layer
  drops the displayed index), (ii) checks that "reduces the degrees of T_1*(f,g), g and f
  simultaneously" is a strict decrease of deg g (the induction variable of the ≤ 100
  theorem) and (iii) writes the three-line minimality argument.
* **Outcomes:** PASS → retype the program to "plane JC2 for minimal counterexamples,
  conditional on the routing maps"; the 12:00Z leak (1) is withdrawn; every ray kill gains
  its full meaning. FAIL (Prop 5.4 needs an extra hypothesis, e.g. δ_i > −1 at a *selected*
  disc only) → the leak stands and its exact hypothesis is typed for the first time.
* **Stop condition:** the reader's verdict. **Information gain:** maximal per hour in this
  round — it is the only cheap object that changes the program's type.

### Card B — N1-BY-CITATION dossier + one instrument cross-check (KNOWN mechanism, NEW use)

* **Target:** OPEN[MOH-CENSUS-N1] and the "≤ 100" overclaim.
* **Mechanism:** §2.1's replay is a desk fact; the deliverable is the per-skeleton citation
  table (which promoted condition kills which row, with the tree witness the driver prints),
  appended to the Theorem 8.1 dossier; plus ONE independent-instrument agreement (the
  smallest joint chart, S1 at 2271 coefficients, from the running lane) as the screen's
  negative control at a degree where all three kill mechanisms fire.
* **Dependencies:** 17(r), 17(hh), 17(ll) promotion records; 17(cccccc)'s enumeration; the
  driver in `box/centre-gate-20260903/`.
* **Cheapest discriminator (30 min):** rerun `screen_9966_rows.py` with the tree witnesses
  printed (the `Tree` object exposes the failing node), and diff against the enumerator's
  `any10` column (S3, S7 must be the (11)-branch rows).
* **Outcomes:** agreement → N1 CLOSED-BY-CITATION, dossier complete, batch-3 lane stopped
  after S1; disagreement between screen and joint chart on any skeleton → the screen's
  promotion is challenged (a review candidate of the highest value, since the same screen
  cut the whole census 658 → 60).
* **Stop condition:** the dossier table is written and one cross-check is banked.
* **Information gain:** converts ~10 lane-hours of compute into a citation; exposes the
  14-row "≤ 100" residual as the true remaining obligation.

### Card C — VALUATIVE DEGENERATION of a ray family (NEW mechanism; first on the k = 4 ray, then K16)

* **Target obstruction:** "uniform in the index" — the shared wall of both rays
  (17(zzzzz) saturation; 17(uuuuu)/(wwwww) atom).
* **Mechanism:** p-adic (Gauss-valuation) initial ideals: for a homogeneous ideal J over a
  valued field and a weight ω, in_ω(J) over the residue field has the same Hilbert function
  as J; if the initial forms of the *generators* already cut out {0} (or already generate
  the unit ideal in the dehomogenised chart), the char-0 statement follows. Unlike monomial
  orders, the initial forms are polynomials over F_p, so NO-COPRIME-LEADERS and DEGREE-BLIND
  do not apply. The desk datum motivating it: at p = 4t+1 on one fibre the K16 tail
  degenerates to b3²·u_r b4^r + 𝔭(…) (§1.2), an arithmetic simplification no monomial order
  can see. First instance tested (b3-weight 1/2): initial system positive-dimensional at
  t = 3, 4 — dead. The card is the systematic version: scan the weight cone (the tropical
  prevariety of the tail at 𝔭) for a weight whose initial ideal of the generators is
  m-primary; and do the same on the k = 4 ray's pinned charts over Q at primes dividing
  the pin scalar's denominators.
* **Dependencies:** the sealed explicit rows (t ≤ 6) and the K = 7, 8, 9 pinned charts
  (`box/k4rayk89-20260903/`); Singular over F_p; `gfan`-style tropical prevariety is not
  installed — use a finite weight lattice scan (weights in {0, ½, 1, 3/2, 2}^t, ~10³ std
  calls of seconds each at t = 3, 4).
* **Cheapest discriminator (≤ 1 lane-hour):** at t = 3, p = 13: is there any weight ω with
  V(in_ω(T_5), in_ω(T_4), in_ω(T_3)) = {0} over F̄_13? Interpretation: YES → a proof of
  (V0)_3 by a new mechanism; repeat at t = 4, 5 and look for the pattern in the winning ω
  (the uniform candidate). NO at t = 3 → the mechanism cannot see (V0) at the top-index
  prime; try the k = 4 ray charts (honest Q-coefficients, more primes) before abandoning.
* **Stop condition:** two indices without a winning weight on either ray.
* **Information gain:** high variance; it is the only mechanism proposed this round that is
  not already refuted by a banked theorem, and its negative is cheap.

**Labels for the synthesis:** Card A — NEW (a printed theorem the ledger never consumed at
the "Moreover" clause); Card B — KNOWN mechanism, NEW consequence (closes an OPEN by
citation); Card C — NEW mechanism (tested negative at its first weight, typed OPEN).

## 7. Lanes — the running lane; the single first lane

**Running lane `g9966-n1-batch3-opus5-20260903` (receipt only: `start_utc=2026-09-04T23:43:29Z`,
`initial_status=RUNNING`, no `final_status`, no `.md` on disk): REDESIGN.** Its five joint-chart
kills duplicate a promoted theorem (§2.1). Keep the smallest skeleton (S1, 2271 coefficients)
as the independent-instrument cross-check of Card B and stop S2, S3, S4, S7; if the lane has
already built more, bank the extra kills as confirmations, not as the closure. The lane's
verdict template ("if all 5 fall ⇒ … Moh's ≤100 theorem RESOLVED") must not be harvested as
written: N1 closes by citation and "≤ 100" needs the 14 excess rows (§2.3).

**The single first lane: `scope-prop54-minimality` (Card A), 1–2 lane-hours, any careful
reader model.** Inputs: Moh pp.183–186, 194, 200 (300-dpi renderings), AUDIT 17(p)/(r) for
the campaign's existing reading of Prop 5.4's translation clause, FALLACY-v2. Deliverable: a
typed statement "every Keller pair of minimal total degree that is not an automorphism has
M_s = n−2 with two points at infinity of multiplicities (v_s, u_s)" with the proof chain
(Prop 5.4 "Moreover" + Lemma 5.3 + minimality), or the exact hypothesis under which it
fails. Second lane (same hour, independent): Card B's dossier + the whole-tree re-screen of
the 296-row cohort (§3.2). Third: the t = 11 rational-fibre datum (§1.3). Card C after those.

**Continue:** nothing else is running. **Stop (do not relaunch):** all-t (V0) structural
lanes before the t = 11 datum; (H1) arithmetic-shortcut lanes; monolithic joint charts.

## 8. Campaign-systems check — UPGRADE

**Rotation slot: claim/review propagation.** **Verdict: UPGRADE.**

**Failure observed.** At 12:00Z I raised OPEN[9966-OTHER-V-ROWS] with QUANTITY "number of
the eight (1)–(13)-admissible (99,66) V-assignments surviving the operative screen, to be
shown 0" and CHEAPEST TEST "the census driver on the seven non-printed rows; minutes". The
coordinator's harvest did not attempt it; instead three lanes (17(cccccc), 17(dddddd), the
running batch-3) and the 00:00Z packet's Q2 treated all eight as open and spent ~8
lane-hours on Gröbner kills of rows a promoted screen already kills. The scanner
(`ops/open_collision.py`) could not have caught it — it is lexical and the promoted deltas
17(r)/(hh)/(ll) never name (99,66) — and the cheapest-test rule (COORDINATION 2026-09-03) is
enforced only by hand at freeze.

**Smallest useful implementation (≤ 1 hour, `ops/open_cheapest.py`).** Parse every sealed
`xmodel/*.md` for `OPEN[...]` entries under an OPENS RAISED heading together with their
"Cheapest test" line; extract the wall-clock estimate (regex on `min|lane-hour|s\b`);
emit, at round freeze, a checklist of live OPENs with estimate ≤ 60 min, each with the
verbatim test line and a `attempted_by=` slot; fail the packet build (non-zero exit) if any
such OPEN is *named as a question in the packet* without an attempt receipt or an explicit
`DEFERRED: <reason>`. The round packet's §2 is then generated only after the checklist is
resolved. **Smallest test:** run it on the five 12:00Z submissions: it must list
OPEN[9966-OTHER-V-ROWS] (minutes), OPEN[K16-TAU-CERTIFICATE-SHAPE] (≤ 10 min) and
OPEN[N2-FOUR-ORDERS] (2 lane-hours → excluded), and it must fail the 00:00Z packet build
because Q2 names N1 without an attempt on the first.

**Regression risk:** none to mathematics (read-only, fails closed on a missing "Cheapest
test" line only for reports newer than 2026-09-03, older reports pass with a warning).
**Measured benefit:** this round's Q2 — the single most expensive redundant thread of the
day — would have been a two-minute desk check twelve hours earlier.

## 9. OPENs raised, FALLACY-v2 check, typed block

OPENS RAISED

- `OPEN[PROP-5.4-MINIMALITY]` — Moh Prop 5.4 (p.183) "Moreover" clause + Lemma 5.3 (p.185)
  + the minimal-total-degree normalization (3) of p.200. QUANTITY: the number of
  configurations of a Keller pair of minimal total degree, not an automorphism, with
  smallest-disc logarithmic radius > −1 (equivalently with M_s < n−2 or one point at
  infinity), to be shown = 0. Cheapest test: reader lane on pp.183–186 (300-dpi
  renderings; the text layer drops the displayed disc index), verify the two branches of
  Prop 5.4's proof and that the reduction is a strict decrease of deg g; ≤ 1 lane-hour.
- `OPEN[9966-SCREEN-INDEPENDENCE]` — agreement of an independent instrument with the
  promoted whole-tree screen at (99,66). QUANTITY: the number of skeletons among S1–S4, S7
  on which the joint-chart verdict (guided_gb) disagrees with the screen's DEAD, to be
  shown = 0 (any disagreement is a review candidate against 17(r)/(hh)). Cheapest test:
  the running batch-3 lane's S1 chart (2271 coefficients) — one chart, ≤ 2 lane-hours; the
  screen side is `box/ideation-20260905T0000Z-fable5/screen_9966_rows.py` (seconds).
- `OPEN[MOH-100-EXCESS-14]` — the fourteen operative-screen survivors at n ≤ 100 outside
  Moh's six ((90,60)×4, (96,64)×4, (96,72)×6; s ≥ 4, u_s = 1). QUANTITY: the number of these
  rows alive after the Prop 6.3/6.4 descent and the receiver kill, to be shown = 0 (else
  each is an honest counterexample slot below 100 and "≤ 100" is not a theorem). Cheapest
  test: the Appendix II compiler (`box/appendix2/compile.py`) on the 14 rows, typing each as
  dead / s' > 2 / open; ≤ 1 lane-hour.
- `OPEN[K16-VALUATIVE-DEGENERATION]` — p-adic initial ideals of the K16 tail at the
  top-index prime 𝔭 | (4t+1). QUANTITY: the dimension of the ideal generated by the
  𝔭-adic initial forms of T_{t,t..2t−1} for the best weight ω in the lattice
  {0, 1/2, 1, 3/2, 2}^t, to be shown = 0 at t = 3 (it is 1 at t = 3 and 2 at t = 4 for
  ω = (0,…,0,1/2), measured here). Cheapest test: the finite weight scan over F_13 at t = 3
  with the sealed rows (`padic_degeneration.py` generalised to all ω; ~10³ std calls of
  seconds); ≤ 1 lane-hour.
- `OPEN[K16-T11-RATIONAL-FIBRE]` — (V0)_11 on the rational fibre d = −2 (y = 5/23), the
  analogue of the failing t = 2 fibre. QUANTITY: dim of the tail cone V(T_{11,11..21}) on
  that fibre, to be shown = 0 (it is 1 at the t = 2 analogue). Cheapest test: tail rows only
  (already emitted mod 1009/53 in `box/k16t11-20260903/`), b4 = 0 slice then the b4 = 1
  chart under guided_gb with the CI hint (1+s¹²)·[34 choose 10]_s; ≤ 1 lane-hour.
- `OPEN[K16-4T+1-REGULARITY]` — the arithmetic shape of the spine at p = 4t+1. QUANTITY:
  the 𝔭-adic valuation of b_r and c_r on the good fibre, to be shown ≥ 1 for all t with
  4t+1 prime (measured = 1 exactly at t = 3, 4; unclear at the composite 21). Cheapest
  test: `padic_abc.py` on the sealed t = 5, 6 rows at p = 7, 5 and the t = 7 rows (4t+1 = 29,
  prime) if regenerated; ≤ 30 min.
- Closed here, not re-raised: `OPEN[9966-OTHER-V-ROWS]` (12:00Z, mine): answer 0 survivors
  besides S8 under the operative screen (§2.1). `OPEN[MOH-CENSUS-N1]` should be retyped
  CLOSED-BY-CITATION pending Card B's dossier, not re-raised.

**FALLACY-v2 check.** No exit-price assertion; no `charge_basis` line due. Flag/place/series:
the two points at infinity of Lemma 5.3 (y − ax, y − bx) are the top form's roots, kept
distinct from the cover series of the disc tower; nothing identifies them with Jacobian
lines. Per-ray/exit-set charge: none. Carrier/attainment: the screen replay is a
NECESSITY verdict (a dead skeleton), never an attainment; a screen SURVIVES (S8) is
REPRESENTATIVE and says nothing about existence. Pole/interior: none used. Floor/attainment:
the p-adic initial-ideal dimensions (1, 2) are exact std results over F_p of the *generators'*
initial forms — a floor on nothing and an attainment of nothing; the flatness statement is
about the full initial ideal and is invoked only in the direction "generators' initial
forms m-primary ⇒ J dim 0", never the converse. `sat()`: not used. Raw remainder degree:
not used. Variable/ring map: `screen_9966_rows.py` calls the charged `Tree` with the
enumerator's own (n, m, Ms, V) tuples — no re-encoding; `padic_*.py` parse the sealed
Singular text into sympy with the file's own variable names (b4, q2_0, q3_0, b3, yy) and
weights (1, 2, 3, t+1) as declared in 17(rrrrr) §2, and evaluate yy at a Hensel-lifted root
of H_t mod p^24 (valuations capped at 22). Prime label/derivative: none. Merge-free /
M-descent and target/arrival index: not touched. Every "dead" above is a consumption of a
promoted delta or a replay of a charged driver, cited in place; the two new readings
(Prop 5.4 scope; N1 by citation) are typed as readings with their sources and are not
promoted here.

```text
SUBMISSION   ideation-20260905T0000Z-fable5 (Fable 5.1), basis 2358a71e, packet fc2a0cb7 (4/4 OK)
Q1           no uniform proof; atom re-framed as "G_r hsop of the double cover R_t = P_t[X]/(q)"
             (W_r = norms, X_rs = mixed traces); NEW mechanism = p-adic valuative degeneration at
             p = 4t+1 (measured: b_r, c_r all 𝔭-divisible, a_r ≡ u_r b4^r on one fibre, t = 3, 4);
             first weight tested NEGATIVE (initial system dim 1, 2); falsification target t = 11
             rational fibre UNDECIDED (both t11 lanes timed out); JC2 target (8.1) = unit-ideal
             instrument, not dim-0
Q2           N1 CLOSED BY CITATION: 7/8 admissible (99,66) skeletons DEAD under the PROMOTED
             whole-tree screen (17(r) tree necessity, 17(hh) ungated Prop 5.6, 17(ll) operative);
             only S8 = V(8,8) survives (desk replay of the charged centre-gate driver); running
             batch-3 is redundant → cross-check only; "Moh ≤ 100 resolved" needs 14 excess
             u_s = 1, s ≥ 4 rows at (90,60), (96,64), (96,72)
Q3           no uniform theorem; batched guided_gb with a SHAPE-CLASS compiler (pin + lower-band
             reduction is shape-generic): ~2 lane-days instead of ~330 lane-hours; re-screen the
             296-row cohort with the whole-tree driver first
Q4           framing corrected both ways: one-place leak CLOSED for minimal counterexamples by
             Moh Prop 5.4 + Lemma 5.3 (read; conditional, typed OPEN); degree-wide method is a
             per-degree algorithm, never the all-degree theorem; most valuable object = the scope
             theorem, then a uniform-in-index kill on the k = 4 ray
FIRST LANE   scope-prop54-minimality (Card A); then Card B dossier + cohort re-screen; then t = 11
RUNNING      g9966-n1-batch3-opus5: REDESIGN (S1 only as cross-check; stop S2–S4, S7)
SYSTEMS      UPGRADE ops/open_cheapest.py — enforce the cheapest-test rule at packet build
DESK         box/ideation-20260905T0000Z-fable5/{screen_9966_rows.py, padic_profile.py,
             padic_profile2.py, padic_abc.py, padic_degeneration.py, degen_t3_p13_y10.sing,
             degen_t4_p17_y13.sing}; python3/sympy 1.12, Singular 4.3.2, one core, all foreground,
             every job < 5 min, < 1 GB
```

Reproduction: `python3 box/ideation-20260905T0000Z-fable5/screen_9966_rows.py` (≈ 1 min);
`python3 box/ideation-20260905T0000Z-fable5/padic_profile2.py 3 200` and `... 4 60` (≈ 3 min);
`python3 box/ideation-20260905T0000Z-fable5/padic_degeneration.py 3 13` and `... 4 17` (≈ 3 min).

Collision scan run at seal time with `python3 ops/open_collision.py --root . xmodel/ideation-20260905T0000Z-fable5.md | grep -v "ideation-20260905T0000Z-"` (same-round lines filtered in the shell; the scanner's corpus guard already excludes same-round submissions and unsealed reports). Hits are lexical review candidates, never closures; none of the hits below names the same object as its OPEN (the PROP-5.4 hits are boundary-instrument reviews, the EXCESS-14 hits are the census history the OPEN cites). Full output: `box/ideation-20260905T0000Z-fable5/collisions.out`.

## COLLISIONS

status: CANDIDATES

### OPEN[PROP-5.4-MINIMALITY]

- `xmodel/b3-boundary-instrument-review-grok46-20260902.md:95` — The producer's verification of `(H-∞)` at `N=4` ("the unique contracted tail sits at the affine cusp, not at `p̃`") conflates these. It does **not** prove `(H-∞)`. That is OPEN even at `N=4`, as a bounded yes/no: whether a F-constant com...
- `xmodel/b3-boundary-instrument-review-grok46-20260902.md:131` — BE Prop 3.1: each of the `r_p` punctures over `p` carries places of `E` at infinity of total degree `a-a_p=(r_p-1)W+K_p`. The `r_p` fibres are disjoint. In the contracted model (BR binding repair: `Φ` finite of degree `μ_t` at `t∈l'` onl...
- `xmodel/landing-ledger-primary-research-fable5-hostile-review-grok46-20260829.md:36` — - **`M = gcd(dp,dq)`.** Prop 8.1(v), used as MULTIPOLE D6(d) and R2.2(D). At entry, `(deg p, deg p_g)=b(alpha,beta)` gives `gcd(b alpha, b beta)=b` (MP4/D4). After a jump or dirty step the child `M` is the gcd of the *child* shape, not a...

- `OPEN[9966-SCREEN-INDEPENDENCE]` (report:596): NONE

### OPEN[MOH-100-EXCESS-14]

- `AUDIT.md:15502` — s ≤ 5 fails at D ≤ 200 (first s = 6 at n = 192). Moh's six rows pass
- `AUDIT.md:15860` — rows / 11 classes = six printed + 49 excess (OPEN[MOH-PROGRAM-ARTIFACT]:
- `AUDIT.md:16143` — ## INTEGRATION #17 DELTA (v) (2026-09-03T12:20Z, MEASURED + PROVED-HERE/UNREVIEWED): THE SCREENED CENSUS IS COFINALLY NONEMPTY — THE K = 16 RAY THROUGH MOH'S (64,48); THE OPERATIVE NUMBERS; THE FIRST D = 108 TARGET
- `AUDIT.md:16329` — ## INTEGRATION #17 DELTA (bb) (2026-09-03T12:44Z, MEASURED / instrument, producer Grok): THE APPENDIX II COMPILER EXISTS (box/appendix2/compile.py) — descent + Φ + (8)–(13) + Moh's SHAPE rule + exact Gröbner; FAIL-CLOSED on Moh's six; ev...
- `AUDIT.md:16538` — s ≥ 4, u_s = 1); s = 3 EXACT at n ≤ 100 (Moh's six); 48 ≤ D ≤ 200: 1,420 / 686 / 459;
- `notes.md:20770` — Genus-0 admissible cover of Moh's major-disc dual graph with STAR-ABC at bottom vertices and Prop 4.6 leading-form pairs at internal vertices (after Moh A.4 → A.3 the internal pair is also a three-point cover, so every vertex contributes...
- `notes.md:20777` — ## 2026-09-03T11:15Z EVENT — CRITICAL: MOH-PROGRAM second reader sealed (Sol, 46KB): WHOLE-MAJOR-TREE necessity recovered from Props 4.6/5.3/5.6 + p.200 — every above-threshold factor at every node must extend; C_FULL_TREE cuts 658 → 60 ...
- `notes.md:20785` — ## 2026-09-03T11:44Z EVENTS — whole-tree Grok gate CONFIRMED → delta 17(r) PROMOTED (frontier: D = 105 and 117 empty on the screened census; both fixed-N rays dead; D = 108 first screened survivor); NEXT-COEFF/PS review → delta 17(s). DC...
- `notes.md:20793` — ## 2026-09-03T12:20Z EVENT — SCREENED CENSUS sealed (Grok, 26KB): the screened census is COFINALLY NONEMPTY — the K = 16 ray n = 48t + 16, m = 32t + 16, M = (−m, n − 12, n − 2), V = (3, 3) survives TREE + ODE + nested for all t ≥ 1 with ...
- `notes.md:20803` — ## 2026-09-03T12:32Z EVENT — `k16-ray-gate-gpt55` sealed (11KB): six items ALL CONFIRMED for all t ≥ 1 (symbolic (1)–(13) with exact integer coprimality 3d − 2e = 1; census emission; gap-free whole-tree screens incl. gated Prop 5.6; nest...
- `notes.md:20819` — ## 2026-09-03T12:44Z EVENT — `appendix2-compiler-grok46` sealed (30KB): compiler built (box/appendix2/compile.py), fail-closed on Moh's six; SATURATED-EMPTY on all in-budget two-point printed rows incl. (21,14; V₂ = 5) and (16,12) [new m...
- `notes.md:20833` — ## 2026-09-03T13:03Z EVENT — `centre-support-gate-gpt55-v2` sealed (11KB): CONFIRMED with a proof correction (full ancestor Puiseux Galois, general L; multiplicity b irrelevant; packet definition p.180). → AUDIT delta 17(hh) PROMOTED: LE...
- `notes.md:20841` — ## 2026-09-03T13:04Z EVENT — launched `post-poly-census-grok46-20260903` (re-base every live target on the operative screen C_FULL_TREE_POLYNOMIAL_ODE; K = 16 ray and (d,e)-fixed ray under POLY; rigid 19; D = 108; D ≤ 200 residue by u_s ...
- `xmodel/dessin-tower-dim-grok46-20260903.md:44` — It is \(\ge 0\) on Moh's six printed rows at every UNI integer-\(N\)
- `xmodel/dessin-tower-dim-grok46-20260903.md:549` — min-over-\(k\), 8 of them still zero at \(N\ge 6\)). Moh's six are **not**
- `xmodel/dessin-tower-dim-grok46-20260903.prompt.md:1` — # Research lane: DESSIN-TOWER expected dimension — admissible covers of Moh's major-disc tree with a Davenport–Stothers (STAR-ABC) passport at every bottom vertex and Prop 4.6 passports at internal vertices; the integer expdim(S, k) per ...
- `xmodel/dessin-tower-dim-grok46-20260903.prompt.md:27` — (a) Moh's six p.202 rows — must be ≥ 0 (Appendix II kills them by a
- `xmodel/ideation-20260903T1015Z-gpt55.md:550` — at `n <= 100`** while keeping Moh's six rows; at `(75,50)`, cut
- `xmodel/ideation-20260903T1015Z-gpt55.md:554` — `(1)-(13)` rows at `n <= 100`**, with the six Moh rows as positive source
- `xmodel/ideation-20260903T1015Z-gpt55.md:578` — - `AUDIT.md:15502` -- s <= 5 fails at D <= 200 (first s = 6 at n = 192). Moh's six rows pass
- `xmodel/ideation-20260903T1015Z-gpt55.md:583` — - `xmodel/census-rebase-opus5-20260902.md:353` -- (1)-(13) survivors at n <= 100 : 658 rows in 63 (n,m) classes [Moh: 6 rows, 4 classes]
- `xmodel/ideation-20260903T1015Z-gpt55.md:589` — - `xmodel/census-rebase-opus5-20260902.raw.md:353` -- (1)-(13) survivors at n <= 100 : 658 rows in 63 (n,m) classes [Moh: 6 rows, 4 classes]
- `xmodel/ideation-20260903T1015Z-gpt55.md:594` — - `xmodel/ideation-20260903T1015Z-packet.md:70` -- FAILS above D = 120 (first s = 6 at n = 192). Moh's six rows pass
- `xmodel/ideation-20260903T1015Z-grok46.md:507` — it on (i) Moh's six (must be `≥ 0` before Appendix II's further
- `xmodel/ideation-20260903T1015Z-opus5.md:760` — | `OPEN[RES-SHED]` — the value of the shed term `Σ_i (1 − δ⁰_i)⁻ = N − deg_x Res_y(g−c_2,f)` per skeleton | **1,908 MOH-4 groups at `48 ≤ D ≤ 200`** (14,016 if MOH-4 is not adopted) | derive `deg_x Res` from the tree on one group and com...
- `xmodel/ideation-20260903T1015Z-packet.md:70` — FAILS above D = 120 (first s = 6 at n = 192). Moh's six rows pass
- `xmodel/ideation-20260903T1200Z-fable5.md:41` — * **At s = 3 the screen is EXACT.** All 52 excess rows have s ∈ {4 (37), 5 (15)}; the six s = 3
- `xmodel/ideation-20260903T1200Z-fable5.md:42` — survivors of C_FULL_TREE_ODE at n ≤ 100 are Moh's six. OPEN[MOH-PROGRAM-ARTIFACT] is therefore a
- `xmodel/ideation-20260903T1200Z-fable5.md:75` — **1.1 The 52 excess rows.** `full-tree-ode-excess-witnesses.json` (52 rows = 58 − Moh's six):
- `xmodel/ideation-20260903T1200Z-fable5.md:144` — condition and it is satisfied by Moh's six (b_min = 0, 0, 1 ≤ 7/3, 0, 0, 0) and by infinitely many
- `xmodel/ideation-20260903T1200Z-opus5-coordinator.md:146` — II's formula. Discriminator: expdim_tree on Moh's six (must be ≥ 0) vs
- `xmodel/ideation-20260903T1200Z-synthesis.md:49` — n ≤ 100 = 14 rows, all s ≥ 4, u_s = 1; at s = 3 the screen is EXACT (Moh's six). If the
- `xmodel/p202-ten-rows-gate-audit-grok46-20260903.prompt.md:1` — # Source + measurement lane: the P202-10 audit — Sol's sharpest candidate gate (M_2 > n − d_2 ∧ forced-(10) at every level) leaves Moh's six rows plus four extras; reconstruct the factor data of those ten rows from Props 5.3/5.6 and Appe...
- `xmodel/p202-ten-rows-gate-audit-grok46-20260903.prompt.md:9` — classes = Moh's six + four extras: (96,64) M = (68,94) V = (2,3);
- `xmodel/post-poly-census-grok46-20260903.md:267` — 20 POLY+ODE rows / 7 classes: Moh's six (`s=3`) plus 14 excess, all
- `xmodel/post-poly-census-grok46-20260903.md:269` — `s=3` at `n≤100` is exactly Moh's six. None of the 14 is two-point
- `xmodel/post-poly-census-grok46-20260903.md:325` — | Operative screen | `C_FULL_TREE_POLYNOMIAL_ODE`; n≤100 20/7 (14 excess); D≤200 1420/686/459 |
- `xmodel/recenter-gate-opus5-20260903.prompt.md:23` — s ≥ 4, u_s = 1); at s = 3 the screen is then EXACT (Moh's six). Task: (1) open
- `xmodel/screened-census-grok46-20260903.md:397` — `n≤100` are Moh's six (five of those also have `u_s=1`; `(99,66)` has
- `xmodel/screened-census-grok46-20260903.md:442` — Moh six, for the record: `(64,48)` `u_s=1` (10); `(84,56) M₂=64`
- `xmodel/screened-census-grok46-20260903.md:504` — 23/20; Moh six on every screen; FT=TI row-for-row;
- `xmodel/screened-census-grok46-20260903.raw.md:397` — `n≤100` are Moh's six (five of those also have `u_s=1`; `(99,66)` has
- `xmodel/screened-census-grok46-20260903.raw.md:442` — Moh six, for the record: `(64,48)` `u_s=1` (10); `(84,56) M₂=64`
- `xmodel/screened-census-grok46-20260903.raw.md:504` — 23/20; Moh six on every screen; FT=TI row-for-row;
- `xmodel/sibling-coefficients-sol56-20260903.prompt.md:18` — bounded target; Moh's six are the positive controls (Appendix II kills them
- `xmodel/sibling-coefficients-sol56-20260903.prompt.md:32` — (2) CALIBRATE on Moh's six: for (64,48) (tree 1 core + k bottoms, s = 3)

- `OPEN[K16-VALUATIVE-DEGENERATION]` (report:608): NONE

### OPEN[K16-T11-RATIONAL-FIBRE]

- `AUDIT.md:17678` — ### 17(wwww) (PROVED-HERE, producer Fable): Theorem TOPTAIL (uniform in t ≥ 3): on b₄ = 1 the rows T_{t,2t−1−r}, r = 0..t−1, are quadratics Q_r = a_r b₃² + b_r b₃ + c_r with a_r, b_r, c_r the b₄ = 1 images of weighted forms of weights r,...
- `AUDIT.md:17714` — ## INTEGRATION #17 DELTA (kkkkk) (2026-09-04T10:03Z, Card C, producer Fable; a structural identity that re-targets the whole K16 (V0) question): DEP (Fable's own round §1.2 conjecture) is REFUTED at t = 2 (exact, PROVED-HERE): on the b₃-...

- `OPEN[K16-4T+1-REGULARITY]` (report:620): NONE

## Seal

Sections 0–9 and the COLLISIONS block are on disk; nothing follows the marker.

<!-- BODY-END -->
