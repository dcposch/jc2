# Blind whole-portfolio ideation — `20260828T0702Z` — Fable 5

Date: 2026-08-28  
Model: Claude Fable 5 (`claude-fable-5`), equal-standing blind whole-portfolio
researcher  
Status: **SEALED BLIND SUBMISSION / NO CANONICAL OR CASE FILE TOUCHED**

No proof or counterexample to JC2 is claimed anywhere in this report.  No
model verdict below is mathematical evidence.

---

## 0. Custody, blindness, and execution ledger

**Custody gate: PASS.**  The packet
`xmodel/ideation-20260828T0702Z-packet.md` hashed to the charged
`b0c9110f85ab19965db086f75dbbb08daa0f9ae8ee2b30ce43ea72ed66d00f1c` before
reading.  All 18 Section-0 canonical hashes and all 7 machine-custody hashes
for the two newest producers were recomputed and match the live bytes
exactly.  `git rev-parse HEAD` returns
`418e413593120d19e15e6546eb50c985f4b1f038` as declared.  No mismatch;
nothing failed closed.

**Files read** (via packet license): `APPROACHES.md` in full including the
complete 46-row master union table; the top/current correction blocks of
`AUDIT.md`; the complete 2026-08-28 day of `PROGRESS.md`; the newest live
state and all 2026-08-28 events at the tail of `notes.md`; the prior
synthesis `ideation-20260827T2259Z-synthesis-sol.md`; and all eleven new
reports named in the packet (fullmodes producer, Grok46 hostile review,
endpoint collapse, independent replay, A-dependency audit, q1 D7–D9
producer, translation-gauge audit, van Dobben review, websweep, HENS-CT R0,
tail-3 superseded stop report).  `COORDINATION.md` was hash-verified but not
re-read beyond prior knowledge of the contract.  The `jc2-lean` tree was not
entered, listed, or read.

**Checks run.**  (i) All 26 SHA-256 recomputations above.  (ii) Hand
re-derivations of the q1 producer's load-bearing algebra: `V0=A'R0+2AR0'`
evaluation, `C=gcd(A,V0)=X-1`, `B(X-1)=A`, `K-4V1=-6B`,
`(K-4V1)^2=8B^2Z` at `Z=9/2`, the D7 numerator `2+4X+6X^2`, the proper-`C`
D9 reduction to `-8B^4U^3` in **both** subcases `V1(x0)!=0` and
`V1(x0)=0` (the latter via forced `Z(x0)=0`), the D8 `c6`-kill order
count at `B`-roots including the `U(b0)=0` degenerate case, and the
endpoint sign diagnostic `8N'=A` for `N=X^5/40-X/8`.  (iii) One
standard-library `fractions.Fraction` script (staged in `/tmp`, not in the
repository) machine-confirming: the fixture polynomials, `gcd(B,V1)=1`,
`C|U(K-2UV1)`, `T(AK-2TV0)/A^2=2+4X+6X^2`, the identically-zero D8
residual, the symbolic cancellation
`-12u^2v1^3+24b^2u^2zv1-8b^4u^3 -> -8b^4u^3` under `v1^2->2b^2z`, and
`8N'=A`.  All pass.

**Deliberate non-checks.**  I did **not** execute any producer checker
(`verify_q1_prefix_target.py`, `verify_uniform_d18_d22.py`, …): frozen
PASS banners can be producer-authored, side effects inside `cases/` are not
licensed to me, and my independent hand/`/tmp` algebra is stronger evidence
for this report's purposes.  I did **not** re-derive the complete weight-9
Laurent numerator `N9` (producer eq. 17), its factorization (18), or the
active-c2 `A^-3` class (20); those remain producer-only inputs here (see
§1).  No AWS, Singular, msolve, Sage, Lean, or heavy local algebra was
touched.

**Failed attempts:** none blocking.  One design decision recorded: I
considered and rejected running the frozen checkers (above).

**Contamination:** none.  No file beginning
`xmodel/ideation-20260828T0702Z-` other than the packet and this response
was read, listed, globbed, or grepped.  My session context includes my own
persistent memory index of prior JC2 review sessions (pre-0702Z facts only:
e.g., the D22 endpoint transfer closed form, the de Rham gate codimension
law, cutoff-2 endpoint closed form, GGV q1/q2 gate facts).  That is my own
prior work product, disclosed here; it contains no peer 0702Z content.

**Scope:** the only write of this session is this file.  Everything below
is scoped exactly as stated; no claim exceeds field-valued statements at
their named fixtures.

---

## 1. Independent audit of the significant news (critical question 1)

**Q1 verdict: the D9 repair is PROVISIONALLY CORRECT, with the proper-`C`
stratum now independently re-derived by me at the reduction level, and the
active-c2 stratum still resting on unreplayed producer valuation claims.
Use only with the provisional label; the residual risk is concentrated in
three named places.**

What I independently verified (hand + `/tmp` exact script):

1. **Fixture soundness.**  The escape fixture is genuinely q1-compatible
   and arithmetically exact: `V0=6X^4-4X^3-2`, `C=X-1` (unique shared
   root; `V0(-1)=8`, `V0(±i)=4±4i`), `A` does not divide `T=B`, the D7
   divisor split holds with numerator `2A^2(3X^2+2X+1)`, and the D8 polar
   numerator is identically zero because `K-4V1=-6B` and `8Z=36`.  The
   fixed-slice `V0=1` D7 inference (`D7=0 => A|T`) therefore genuinely
   fails to transport.  This part of the news is, to my satisfaction,
   correct beyond its producer.

2. **Proper-`C` repair reduction, all subcases.**  Conditional on the
   producer's `N9` (17) and factorization (18), the root class at a
   `C`-root with `U!=0` is exactly `-8B^4U^3`:
   - generic subcase `V1(x0)!=0`: D7 gives `D=-2UV1`, D8 gives
     `V1^2=2B^2Z`, and the first two terms of `P9` cancel exactly
     (machine-confirmed as a polynomial identity under `v1^2->2b^2z`);
   - degenerate subcase `V1(x0)=0` (possible: `gcd(A,V0)=C` forces only
     `gcd(B,V1)=1`, **not** `gcd(C,V1)=1`): then D7 gives `K(x0)=0`, the
     D8 core forces `Z(x0)=0` (via `0=8B^2U^2Z`, `B,U` units), and every
     `P9` term except `-8B^4U^3` carries a factor `V1`, `ZD`, `C`, or
     `C^2`, so the same class survives.
   The producer text does not display the degenerate subcase; it is
   handled automatically by the same class.  That is a small robustness
   gap in the write-up, not in the mathematics.
   Since `gcd(B,C)=1` (A squarefree) and `C` squarefree, `C|U` follows
   rootwise, hence `A=CB | BU=T`.  I also confirmed the D8 `c6` kill at
   `B`-roots is order-correct including `U(b0)=0` (the `c6C^2V1^2` term
   still has order one while everything else has order ≥ 2).

3. **What I could not verify and where risk sits.**  (a) The complete
   weight-9 numerator `N9` (17) with all cross terms and the full
   nine/ten-mode schedule — needs the different-model Laurent replay.
   (b) The active-c2 leading class (20) and especially the valuation
   assertion "every c2, F5, and F6 contribution begins only at `A^-2`" —
   note the producer's list **omits `c6`**, which is live on `C=A`
   because `B=1` disables the D8 kill; a hostile reviewer must confirm
   `c6`'s g9 contribution is also ≥ `A^-2` there (my rough indicial
   estimate with `F1=A^3S` says yes, since `(F^(3/4))_1=(3/4)A^2S` is
   already regular, but this is an estimate, not a check).  (c) The
   claim that "the leading D8 equation gives `S^2=2Z`" on the active
   component — the active D8 polar itself is not displayed and must be
   replayed.  Divisor coverage is otherwise complete: `C=1` (D7 already
   forces `A|T`), `1<=deg C<=3` (item 2), and `C=A` covering both
   `c2!=0` and `c2=0∧A|V0` (the (20) class is c2-free, so the c2-zero
   deep sublocus inherits the same argument).

**Mode-valuation checklist for the mandatory hostile review:** replay (17)
with `c2` retained symbolically to confirm it truly cancels on `c2=0`;
replay (20) with all of `c2,c4,c6` live; confirm the active D8 leading
equation; confirm the `V1(x0)=0` subcase explicitly.

---

## 2. The remaining five critical questions

### 2.1 Fastest exact resolution of the post-D9 `W` split and the transport question (question 2)

**Claim: a root-local (one-root) compression exists that would make the
`W` split moot on every stratum with `C != A`.  Call it SRT
(single-root transport); it is my main new mechanism (§5, Card 1).**

Two observations, neither stated in any document I read:

1. **One linear factor suffices.**  The endpoint contradiction never
   needed `D22 in (A)`; it needs only `D22 in (X-x0)` for a **single**
   root `x0`, because the target is the unit polynomial `1`.  Every step
   of the reviewed fixed-slice D7–D22 mechanism is local at a root:
   polynomial windows have no pole at `x0` (locality is automatic, the
   global "cannot store `A^-2`" is stronger than needed); the scalar-mode
   kills (`c18`, `c20`, earlier `c6,c10,c14`) argue "nonzero scalar has a
   pole contribution of strictly lowest local order," which is a one-root
   argument; the square-defect radical steps `ord(Delta^2)>=1 =>
   ord(Delta)>=1` are local; and `L_22` raises local order at `x0` by at
   least one whenever `ord_{x0}(g22)>=-2`.

2. **`B`-roots look locally like the fixed slice.**  At any root `x0`
   with `V0(x0)!=0`, the local indicial data of the general prefix
   (`ord_{x0}F1=2`, unit multiplier) agree with the fixed slice.  So the
   conjecture is: at every `V0`-unit root, the complete mode schedule and
   raw-window constraints force `ord_{x0}(g22)>=-2` — hence
   `D22 = 1` is impossible on **every** stratum that has at least one
   `V0`-unit root, i.e., everything except the deep stratum `A|V0`
   (`C=A`, on q1: `V0=3lambda*A*A'`).

If SRT holds, the `C`-part of `W`, the divisor chart fanout, and even the
D9 repair itself become unnecessary for `C != A`: the entire general-`V0`
endpoint reduces to (i) the SRT lemma and (ii) one deep-stratum cascade in
the single extra parameter `lambda` (plus live `c2,c6`).  The known risk
is that the fixed cascade's quotient objects (`O,P,S,U` at D18–D21) are
global polynomials fed forward; a local version must show the recurrence
closes over the local ring at `x0` without global input.  That is exactly
testable on the frozen escape fixture (which has three `V0`-unit roots
`-1,±i` and dies at D9, consistent with SRT).  See Card 1 for the
discriminator, outcomes, and stop rule.

If SRT fails at a specific row, the fallback for the `W` split, in order
of expected speed: (a) the T_A-cokernel residue calculus of §5.2 (turn the
`C`-part condition into finitely many residue classes at `C`-roots using
the same canonical-reduction technology already promoted for
`M(Y)=4HY'+6H'Y`); (b) only then a per-stratum exact elimination
(`deg C = 1,2,3` plus active), bounded, on one idle node.  I concur with
the producer that an undifferentiated D22 elimination or 16/81-chart
brute force is dominated.

### 2.2 Can the failed translation shear be repaired? (question 3)

**No, and there is a stronger structural reason than the window audit
states: the shear manufactures a `G22` receiver, destroying the very
mechanism the gauge was meant to reach.**

The coefficient formula `(tau_a G)_n = sum_k (-a)^k G_(n-k)^(k)/k!`
applied at `n=22` gives `(tau_a G)_22 ⊇ -a*G21'`; with the single slot
`G21=c*X^3` this is `-3ac*X^2 != 0`.  So the sheared frame does not
merely leak forbidden low-`X` constants into `F9`/`G13` (the reviewed
audit); it also has a **nonzero bound `G22` slot**.  The entire endpoint
contradiction rests on "raw `G22` absent ⇒ `D22_raw=-L22(g22) in (A)`".
In the sheared frame that structural fact is false, and one would have to
re-derive the endpoint using the pinned relations
`G22_bound = -aG21' + (a^2/2)G20'' - …` — which is just the active
cascade in worse coordinates.  Consequences:

- **Solution-locus cancellation**: would need the determinant rows to kill
  every forbidden tail *and* the manufactured `G22`; no such theorem
  exists, and the burden now includes restoring the endpoint receiver
  structure.  Do not assume it.
- **Compensating target automorphism**: impossible in principle — the
  obstruction lives in the `X`-Newton support of the source windows, and
  target automorphisms act in `t` only; they cannot restore
  `X`-support.  A compensating source automorphism in `X` alone (no `t`)
  does not kill the weight-one pair.
- **Enlarge-then-descend**: the enlargement that makes the shear legal
  (adding all shear-tail slots) necessarily adds `G22`, so the enlarged
  family loses the endpoint theorem's engine; descent back to the frozen
  windows is then exactly the unsolved cancellation problem.

Verdict: analyze active `C=A` directly, as the packet directs — with the
added datum that any future gauge proposal must be checked against
**receiver creation at weight 22**, not only against low-window leakage.
This check is one line and should be added to the standing mutation suite.

### 2.3 Theorem-interface composition pass (question 4)

- **Real bridge (candidate): SRT localization** (§2.1) composes the
  reviewed fixed-slice D7–D22 mechanism with the general-`V0` prefix at
  `V0`-unit roots, discharging the fixed theorem's `V0=1` hypothesis
  locally instead of via the missing global compiler.  It is a candidate,
  not a theorem; its discriminator is Card 1.
- **Exact scope mismatch #1**: the fixed cascade's D8 forces the full
  `A | (F4-V/16-Z^2/64)`, while the general q1 D9-repair successor forces
  only the complementary part `B|W`.  The mismatch is precisely the
  `C`-part of `W`; SRT would dissolve it for `C != A`, and nothing
  currently composes for `C=A`.
- **Exact scope mismatch #2 (hypothesis custody)**: q1 is licensed only
  when `D23=0` is carried (the de Rham theorem's condition).  Any
  emptiness statement proved on the q1 cover is an exclusion of the
  *D1–D23* system, not of D1–D22.  Genuine Keller points satisfy all
  rows, so this is safe at points — but every packaged theorem must list
  D23 in its hypothesis block or it will be quoted with the wrong system.
- **Real bridge (small, promoted technology): T_A-cokernel calculus.**
  The producer's operator echo `L9=-4A^3*T_A` identifies the D9 same-row
  operator with the q1 operator `T_A(Q)=2AQ'-3A'Q` (different windows —
  the producer correctly types deg ≤ 12 vs deg ≤ 15).  The campaign
  already owns the complete reduction calculus for the sibling operator
  `M(Y)=4HY'+6H'Y` (seven-dimensional cokernel, closed-form canonical
  reductions) and Opus5's gate law `dim H^1_dR = r-1+k_m`.  Composing
  these gives a finite residue test for `T_A`-image membership questions
  arising in the `W` split (§5.2, Card 3).
- **NO HIT**: raw-to-global landing maps (D5G/D4R1, `H=X^8-1` artificial
  fixture) share no hypothesis with the branch-P `A=X^4-1` endpoint;
  boundary one-vertex `KEF` still fails closed on unpinned `B`/`x` tails
  (as its own review predicts); K00/order-two, AS109, and the collision
  ideal have no interface to the new results; van Dobben's recognition
  theorem discharges nothing in the GGV lane and its plane analogue is
  closed negatively.
- **Endpoint target class note (free observation)**: the endpoint's sign
  diagnostic `N=X^5/40-X/8`, `8N'=A`, says the target `D22=1` is
  realized exactly by the `A^-5` "primitive-of-`A`" Laurent class, which
  the nine-mode continuation provably cannot manufacture (max pole 2
  after relations).  For the active stratum, the analogous question —
  can the shifted indicial family reach pole order five with the
  primitive-of-`A` numerator? — is a compact reformulation of the
  whole deep-stratum endpoint and a good invariant to track while
  compiling Card 2.

### 2.4 Four idle AWS nodes (question 5)

Principle: nothing launches before the D9 hostile review returns except
preregistered, reversible, cheap prepasses; no superseded brute force; no
identical engine/order reruns.

1. **r6d — post-D9 `W`-split per-stratum decision (gated).**  After (and
   only after) the D9 review passes: exact bounded elimination of the
   c2-zero post-repair system per divisor stratum (`deg C=1,2,3`), each a
   small system in the few surviving unknowns, with the D23 row included
   in the hypothesis block.  Preregister targets, 21,600 s cap each,
   freeze + independent review before any successor.  Stop conditions:
   unit certificate (freeze, review), survivor basis (freeze, escalate to
   Card 2 interaction), or cap (`RESOURCE_CAP_NO_VERDICT`, no rerun).
2. **r6a — K00 V27 rank-purity prepasses.**  The preregistered,
   already-designed rank-compressed atlas successor: cheap exact
   prepasses testing whether the surviving coefficient-base component is
   rank-pure, exploiting the reviewed collapse of all 54 maximal minors
   to two scalar classes.  This keeps the strongest non-GGV finite
   falsifier moving with near-zero design cost.  Stop: prepass verdict
   either way, or 6 h cap.
3. **Box03 — ACTIVE-LAMBDA compile/solve overflow only.**  Card 2 is a
   desk computation first; Box03 is reserved for its constraint systems
   only if they exceed desk scale, same caps and freeze rules.
4. **Box02 — hold in reserve** until the D9 review and the first Card
   1/2 outcomes return.  An idle audited node is worth more than a
   fourth speculative lane; this is the explicit anti-explosion control.

`box01` (D43) and `r6b` (LF40) continue unchanged under their existing
custody; `r6c` finishes the HENS-CT control.

### 2.5 Under-resourced or misranked non-GGV avenues (question 6)

1. **Avenue 2 (Sigray backbone: landing, `RPMC(C)`, cofinal ceiling).**
   Every synthesis since 19:37Z calls this the largest proof gap; the
   entire 08-28 day was GGV endpoint.  That is momentum, not ranking —
   the fixed endpoint is a *q1-negative diagnostic*, and even total
   general-`V0` success kills one branch of one face.  Avenue 2 needs at
   least one standing desk lane (the intrinsic two-chart constructor /
   L3–L5 obligations) so the round after next is not starting cold.
2. **Avenue 26 (primitive-monodromy td bound).**  Still the consensus
   best cheap untried test (G:5/S:5), still unexecuted after seven days
   of frontier work.  Stage 1 is a bounded GAP/Magma-style enumeration
   with Orevkov's `(48,64)` td=9 configuration as the built-in negative
   control.  I raise it on cost grounds (my independent call; no new
   mathematical evidence moved it).
3. **K00 (within avenues 4/19/21 cluster).**  Zero cycles today despite
   being the named strongest finite falsifier; the V27 design is written
   and idle — hence the r6a assignment above.

---

## 3. Disposition vector (contract item 1)

Baseline: the 06:23Z superseding overlay plus the 22:59Z round vector.
`G2` is **not** one object: `G2-PSC` (global packet/sheet transport
fidelity) and `G2-BD` (post-residue-A bounded delay) are separate unmet
obligations of avenue 2; both are **unchanged** — no new evidence touches
either, and nothing below merges them.

**Raise (3):**

- **1 (GGV corner families / endpoint march): raise.**  The fixed
  `A=X^4-1,V0=1` endpoint is review-closed empty (289/289 + two replays);
  the genuine q1 escape/repair identifies an exact, small live target
  (post-D9 `W` split; active `C=A`); and the one-root observation (§2.1)
  offers a compression that could collapse the divisor fanout.  Redesign
  inside the raise: SRT + active-lambda + T_A-residue calculus before any
  chart explosion; D23 carried explicitly on every q1-cover statement.
- **16 (D-module / holonomic index, now the de Rham gate + HENS-CT home):
  raise, narrowly and software-conditionally.**  The HENS-CT backend
  crossed `UPSTREAM_PASS` (real nonzero `L,C`, Ore and direct field
  remainders zero on the upstream example) and the rank-one campaign
  control is running.  This unblocks the first executable certificate.
  Everything remains control-scope; no nonvacuity or descent is implied.
- **26 (primitive-monodromy td bound): raise on execution priority.**
  Reason in §2.5; this is a cost-based independent call, flagged as such.

**Unchanged with content notes (7):**

- **2**: unchanged as the primary proof wall (both `G2-PSC` and `G2-BD`
  unchanged); allocation note — under-resourced (§2.5).
- **3**: unchanged; note the `T_A`/`M(Y)`/gate-law connection (§2.3)
  slightly increases its instrument value inside avenue 1.
- **5**: unchanged; note the shear audit is one more datum that
  raw Newton windows are not translation-invariant, cooling any
  gauge-descent instinct.
- **18 / 30**: unchanged; the van Dobben residue stays exactly the filed
  redesigned secondary `KEF-ONE-VERTEX` bridge, fail-closed on incomplete
  graphs.
- **27**: unchanged; shares the KEF residue custody.
- **35**: unchanged; van Dobben *strengthens the negative* (tangent
  `Sym^2` analogue is `A^1 x G_m`, non-tangent has `Pic=Z`), closing the
  last naive descent cleanly.
- **36**: unchanged at its scope-sharpened state (theorem-compressed
  search on named residuals only).

**Unchanged, grouped (36):** 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17,
19, 20, 21, 22, 23, 24, 25, 28, 29, 31, 32, 33, 34, 37, 38, 39, 40, 41,
42, 43, 44, 45, 46 — no new evidence at this freeze touches any of them.
Specifically reaffirmed: 17 and 31 stay unmoved by the refuted Matysiak
papers; 33 stays closed at `COSTUME` with its twisted bookkeeping absorbed
into 1; 44 stays closed as proof input; 45 stays not-reopened; 10 stays
`NO LEVERAGE`; 11 stays refuted.

**Lower: none.  Reopen: none.**  (The retirements demanded by the news —
fixed-endpoint tail/solver lanes — are executions inside avenue 1, not
avenue-level lowers.)

---

## 4. Bottleneck reranking (contract item 2)

**Proof bottlenecks:**

1. **Universal landing/coverage plus the cofinal degree ceiling (avenue 2
   backbone; `G2-PSC` for any hybrid route).**  Unchanged in nature and
   still the gate between *any* family-level exclusion and JC2.  Ranked
   first by probability-of-resolving-JC2, not by tractability.
2. **General-`V0`/q1 branch-P endpoint transport** — concretely: the SRT
   question, the post-D9 `W` split, and the active `C=A` cascade.  Ranked
   second but first by expected information gain per wall-clock hour this
   week.
3. **The parameterized raw compiler bridge** (A-dependency audit items
   1–5: discriminant-localized quartic-`A` compiler, window/kernel
   transport, endpoint unit tracking).  Shared infrastructure that turns
   every fixed-`A` theorem into a family theorem; without it, endpoint
   results stay fixture-bound forever.

**Disproof/counterexample bottlenecks:**

1. **K00 full-`P6` nonzero, source-open, rank-exact point + compatible
   prolongation/receiver** — still the strongest finite falsifier, and
   idle today (hence the r6a assignment).
2. **A surviving deep-stratum family that algebraizes.**  If the active
   `C=A` lambda-cascade (Card 2) does *not* close, its survivor locus is
   the best CE seed the campaign has had since (72,108): q1-compatible,
   window-respecting, and past D9 by construction.  The AS109/max-12
   char-p frontier remains the backup falsifier at its stated scope.

---

## 5. New mechanism and new connection (contract item 3)

### 5.1 New mechanism: SRT — single-root transport

Stated in §2.1.  **Comparison with repository history:** the campaign has
used root-local reasoning tactically (R2's root-local formal Morse
dichotomy; the q1 producer's étale root-algebra language; rootwise steps
inside divisor arguments), and the A-dependency audit analyzed *global*
formal-`A` dependence.  No document I read states either half of SRT: (a)
that the endpoint contradiction needs divisibility by a **single linear
factor**, or (b) that the entire D7–D22 pole/window/mode-kill mechanism
appears to localize at one root, making `V0`-unit roots individually
lethal and reducing general `V0` to the `A|V0` stratum.  The divisor-split
architecture (global `gcd` bookkeeping, `C`-part obligations) is exactly
what SRT would delete.  Failure of SRT is also informative: the first row
where local closure needs global data is precisely a specification line
for the parameterized compiler (bottleneck P3).

### 5.2 New connection: `T_A` cokernel calculus across avenues 1 / 3 / 16

The q1 gate operator `T_A(Q)=2AQ'-3A'Q` (avenue 1 upper face), the
lower-face endpoint operator `M(Y)=4HY'+6H'Y` with its promoted
seven-dimensional cokernel and closed-form canonical reductions (avenues
1/3), and Opus5's rank-one gate law `dim H^1_dR(nabla_m)=r-1+k_m` (avenue
16) are one family of first-order operators whose image/cokernel questions
are decided by residues at the roots.  The producer's own operator echo
`L9=-4A^3*T_A` (verified sign convention; window-typed deg ≤ 15 vs the q1
primitive's deg ≤ 12) is the bridge instance.  Payoff: the missing
`C`-part of `W` and the active-c2 lower-pole blocks should reduce to
finitely many residue classes at `C`-roots computable by the existing
canonical-reduction technology, replacing elimination with linear algebra.
This composition of three already-promoted results has not been attempted.

---

## 6. Strongest next attacks (contract item 4)

**Proof attack.**  Two-step, mostly desk: (A) test-then-prove SRT (Card
1); (B) compile the active `C=A` cascade `V0=3lambda*A*A'` with all modes
live (Card 2).  If both close, the complete q1-compatible c2-cover
branch-P endpoint at `A=X^4-1` is field-empty **with `D23` in the
hypothesis block**; the residual general-`V0` gap is then non-q1 `V0`
(needs either D23-free handling or a compiled D23 row) plus the
parameterized-`A` bridge.  This is the highest information-per-hour proof
work available at this freeze.

**Counterexample/falsification attack.**  Run the gated r6d `W`-split
per-stratum decision (§2.4.1).  Any stratum surviving through D12+ gets
immediate prolongation (depth-stab discipline) rather than a rushed
emptiness hunt: q1-compatible window-respecting survivors past D9 are
exactly the objects a genuine counterexample would shadow.  In parallel,
r6a keeps K00 V27 moving as the standing non-GGV falsifier.

---

## 7. One software acceleration (contract item 5)

**PARAM-RAW: the parameterized raw compiler.**  Extend the frozen branch-P
compiler to symbolic monic quartic `A=X^4+a3X^3+a2X^2+a1X+a0` over
`K[a0..a3,Disc(A)^{-1}]`, standard-library exact, with acceptance gates:
(i) byte-identical specialization to the authoritative 513-generator
fixture at `A=X^4-1`; (ii) a second literal specialization (e.g.
`A=X^4-2`) replaying the D7–D9 general-prefix formulas; (iii) windows and
kernel ranks emitted as certificates over the discriminant localization,
omitted low coefficients retained as equations.  This single artifact
discharges bottleneck P3's infrastructure half, converts every future
fixed-`A` endpoint theorem into a family theorem, and is the natural home
for whichever global data SRT turns out to need.  (The HENS-CT rank-one
control is already running and needs no new decision; it is deliberately
not double-counted here.)

---

## 8. Idea cards (contract item 6 — exactly three)

### Card 1 — `SRT-ONE-ROOT`: root-local endpoint transport

- **Dependencies:** reviewed D1–D6 branch-P prefix; reviewed fixed-slice
  D7–D22 cascade (PASS chain through Grok46 289/289); A-dependency audit
  (formal-`A` scope).  Explicitly does **not** depend on the provisional
  D9 repair — SRT would independently kill every `C != A` stratum, which
  is part of its value.
- **Licensed assumptions:** q1/D23 custody as in §2.3; characteristic
  zero; fixture windows.
- **Cheapest decisive discriminator:** at the frozen escape fixture,
  compute the local order profile of `g7..g14` at the `V0`-unit root
  `X=-1` and compare with the fixed-slice profile; then attempt the local
  D18–D22 window/mode-kill argument purely over the local ring at one
  root.  Standard-library exact; hours.
- **Materially different outcomes:** (a) local profile matches and the
  argument closes ⇒ all `C != A` strata die at every `V0`-unit root;
  general-`V0` collapses to the deep stratum — major compression, feeds
  Card 2 directly.  (b) Local closure fails at a specific row because a
  global quotient object (`O,P,S,U`) is genuinely needed ⇒ the exact
  failure row becomes a written requirement line for PARAM-RAW — still
  valuable.  (c) The fixture's local profile deviates from the fixed
  slice before D9 ⇒ SRT refuted for structural reasons at cost of hours.
- **Stop/rollback:** stop on (c), or if two consecutive rows past D9 need
  non-localizable global input; desk-only, nothing published, no
  rollback surface.
- **Cost:** 1–2 desk days + <1 h replay; review half a day.
- **Expected information gain:** high — decides the *shape* of the
  transport problem either way and deletes or specifies the divisor
  fanout.

### Card 2 — `ACTIVE-LAMBDA`: the deep-stratum cascade

- **Dependencies:** reviewed D1–D6 prefix; the reviewed q1 identity
  `T_A(A^2R0)=A^2V0` fixing `V0=3lambda*A*A'` on the active component;
  the translation-gauge negative audit (must not gauge `lambda` away —
  reinforced by the `G22`-creation argument of §2.2, which should be
  added to its mutation suite).
- **Licensed assumptions:** none provisional; `c2,c6` live throughout;
  all nine/ten modes carried causally.
- **Cheapest decisive discriminator:** compile `g7..g12` on the active
  component with the shifted indicial data (`F1=3lambda*A^3*A'`, local
  order 3+) and determine whether the alternating square-defect/mode-kill
  pattern re-emerges with shifted pole orders; track the §2.3
  "primitive-of-`A` class reachability" invariant.
- **Materially different outcomes:** (a) cascade closes with a
  `D22 in (A)`-type contradiction ⇒ with Card 1, complete q1 c2-cover
  endpoint emptiness at `A=X^4-1` (D23 carried); (b) a survivor family
  persists through D22 ⇒ best current CE seed — pivot to prolongation
  and algebraization (disproof bottleneck D2 becomes primary); (c) some
  row forces `lambda=0` ⇒ the deep stratum collapses onto the already
  closed fixed slice — immediate total q1 closure given Card 1.
- **Stop/rollback:** desk rows are cheap; escalate to Box03 only past
  desk scale with 21,600 s caps; freeze + hostile review before any
  claim; survivors are never promoted to "counterexample candidate"
  language without prolongation evidence.
- **Cost:** 2–4 desk days; 1 review day; AWS optional.
- **Expected information gain:** high — it is the unique surviving q1
  stratum if Card 1 passes, and the best falsification surface if it
  fails to close.

### Card 3 — `TA-COKER`: residue calculus for the `W` split

- **Dependencies:** the provisional D9 producer's operator echo
  `L9=-4A^3*T_A` (named provisional input); promoted `M(Y)` cokernel
  reduction technology; promoted gate law `r-1+k_m`.
- **Licensed assumptions:** window typing as the producer states (deg ≤
  12 q1 primitive vs deg ≤ 15 D9 map — the mismatch is part of the
  card, not an oversight).
- **Cheapest decisive discriminator:** recompute the frozen fixture's D9
  death fraction
  `(25+23X+21X^2-89X^3-6X^4-4X^5-2X^6)/(16384*C^3*B^2)` via residue
  calculus at the `C`-root; exact match certifies the typing.
- **Materially different outcomes:** (a) match + closed forms ⇒ the
  `C`-part of `W` and active-c2 lower blocks become finite linear
  algebra — fastest `W`-split path if SRT stalls; (b) a typed interface
  mismatch ⇒ documents exactly which window data the residue picture
  misses (feeds PARAM-RAW); (c) the calculus generalizes across rows ⇒
  bonus: a uniform row-obstruction language for avenue 16's tower.
- **Stop/rollback:** stop if the discriminator mismatches twice after
  independent re-derivation; desk-only.
- **Cost:** 1–2 desk days.  **Expected information gain:** medium-high;
  independent of Cards 1–2 and cross-checks both.

---

## 9. Lane recommendations (contract item 7)

- **General-q1 GGV:** **CONTINUE, redesigned** — targets are SRT, the
  active-lambda cascade, and the `W` split per §2; mandatory hostile
  review of the D9 repair before promotion or expensive fanout; D23
  carried in every hypothesis block; no undifferentiated D22 elimination.
- **Raw-to-global landing (D5G/D4R1 lineage and landing maps):**
  **CONTINUE at low intensity, redesigned around PARAM-RAW** — the
  compiler bridge is now its highest-value deliverable; no new heavy
  launch until that spec exists.
- **HENS-CT:** **CONTINUE** — let the running rank-one control finish;
  require the complete certificate plus mutation replay before the
  adapter is called evidence-capable; then one campaign fixed-instance
  certificate.  `UPSTREAM_PASS` is software news only.
- **D43 (box01):** **CONTINUE** under existing custody and caps; on cap,
  classify `NO_VERDICT` and do not identically rerun.
- **LF40 (r6b):** **CONTINUE** under existing custody; price stays
  honest — even a unit removes only the conditional `(72,108)` case and
  lifts that conditional bound to 125.
- **Order-two / TD6:** **REDESIGN** — the only funded successor is
  repaired H19R1 certificate emission (38 original-FIRST multipliers,
  denominator-cleared identity with total `F`); no new P12/P13-style
  searches; desk/review slots only.
- **Artin–Schreier (AS109 residual):** **CONTINUE, narrow** — the three
  alpha/beta content strata only; no new support/Newton searches; the
  max-12 frontier statement stands.
- **External intelligence:** **CONTINUE** at cadence — websweeps plus
  primary-source audits; Matysiak stays `REFUTED-ON-AUDIT/NO RERANK`; the
  van Dobben residue is one bounded `KEF-ONE-VERTEX` test if and when a
  fully pinned boundary graph exists (it fails closed today).

---

## 10. Likely-missed insight (contract item 8)

**The endpoint contradiction consumes only one linear factor of `A`, so
endpoint transport is a one-root problem, not a divisor problem.**  Every
document treats `D22_raw in (A)` versus `D22=1` as the unit-versus-ideal
clash; nothing uses more of `(A)` than a single root, and every mechanism
feeding it (windows, scalar-mode kills, radical square-defect steps, the
order-raising `L22`) is local at a root.  If correct, the general-`V0`
question is not "control `gcd(A,V0)`" but "find one root where `V0` is a
unit, or else live on `A|V0`" — deleting the `C`-part of `W`, the divisor
strata, and most of the projected chart fanout in one move.  **Cheapest
test** (hours, desk): walk the reviewed fixed-slice D18–D22 argument
replacing `(A)` by the local ring at `X=1` and confirm no step needs a
second root; then compute the escape fixture's local orders at `X=-1`
through D9 and check they match the fixed-slice profile.  Second-place
candidate, also cheap: the §2.2 observation that the translation shear
manufactures a bound `G22` slot — worth adding to the gauge audit's
mutation suite as a permanent structural firewall.

---

## 11. Epistemic ledger (contract item 9)

**Proved / promoted (different-model-reviewed) facts consumed:** fixed
`A=X^4-1,V0=1` endpoint field-emptiness (Grok46 289/289 + two independent
Sol replays) and the D7–D17 prefix chain (189/499/334/361 checks); tails
4–7 field-empty; rows-30–34 class slice and its zero-tail raw death; the
`nu` law and mod-8 class death; the R5/R6 multiplicity-endpoint and
survivor-codimension theorems at their scopes; the `M(Y)` cokernel
calculus; Opus5's gate law (with the repaired capacities); the bi-face
`v_7=0` separation; V43/T-a1 `N=6`; the K00 V26R1F/V27-adjacent
containments; the Matysiak refutation-on-audit; the van Dobben paper audit
and its closed plane analogue.

**Provisional inputs (named as such wherever used):** the q1 D7/D8 exact
formulas, the escape fixture (now partially independently verified by me —
see below), the D9 repair on both stratum families, the post-repair `W`
target (23), and the operator echo (21) — all awaiting hostile review;
the D9-repair hypothesis block implicitly includes the D1–D6 c2 branch
dichotomy and q1-with-D23 custody.  HENS-CT `UPSTREAM_PASS` is a software
gate only; the rank-one control is running, unfinished.

**My own verification state:** independently re-derived (hand plus a
`/tmp` standard-library exact script): fixture polynomials and gcd
structure, D7 divisor split and full numerator, D8 zero residual, the
proper-`C` D9 reduction to `-8B^4U^3` in both the `V1(x0)!=0` and
`V1(x0)=0` subcases, the D8 `c6`-kill order counting (including
`U(b0)=0`), and `8N'=A`.  **Not** independently verified: the complete
`N9` (17), its factorization (18), the active-c2 class (20) and its
valuation claims (the stated list omits `c6`, flagged in §1), and the
active-c2 D8 leading equation.  No producer checker was executed, by
declared choice.

**Conjectures introduced here (no evidence status):** SRT one-root
transport; the `T_A`-residue formulation of the `W` split; active-lambda
cascade closure; the `G22`-creation argument as stated is a one-line
verified computation (`-a*G21'` term) but its strategic reading
("gauged frame strictly weaker at the endpoint") is interpretation.

**Failed approaches consumed as negative results:** the translation shear
(exact negative audit, reinforced §2.2); the five-mode cutoff-two
truncation (hostile-audited false); the naive `Sym^2` dimension-two
descent (closed by the van Dobben audit); Matysiak (refuted on audit);
prior fixed-tail lanes (retired by supersession, non-evidence stops
correctly classified).

**Hidden assumptions surfaced:** q1 statements silently require D23
(§2.3); "c2 branch cover" completeness is inherited from the reviewed
D1–D6 dichotomy `c2=0 or A|V0`; `gcd(A,V0)=C` does not force
`gcd(C,V1)=1` (my degenerate-subcase check exists because of this); the
fixed-`A` windows/ranks are source-specific certificates, not universal
ones (A-dependency audit); SRT assumes local-ring stability of the
recurrence — untested, and exactly what Card 1 tests first.

**Checks run / failed checks:** §0 lists all 26 hash verifications
(all pass), the hand derivations, and the `/tmp` script (all assertions
pass).  No check failed.  No AWS, CAS, or Lean was used; `jc2-lean` was
not touched; no canonical or case file was modified.

**Contamination:** none (§0).  **Scope:** every mathematical statement
here is confined to its named fixture/stratum/hypothesis block;
no statement in this report is a Keller-pair, scheme-theoretic,
family-level, or JC2 conclusion.
