# Blind whole-portfolio ideation — Claude lane — round `20260824T1358Z`

- Lane: Claude (Anthropic, Fable 5), blind independent scan.
- Authored: 2026-08-24, after the packet cutoff; no event after the cutoff is
  consumed except the immutable packet itself.
- Blindness: no other `ideation-20260824T1358Z-*` submission, prompt, log, or
  run file was read. Inputs were exactly the packet and the canonical/report
  files it requires.

## 0. Packet, cutoff, and hashes actually consumed

Packet: `xmodel/ideation-20260824T1358Z-packet.md`.
Cutoff: `2026-08-24T13:57:56Z`. Clean charged basis
`6f2e49e63d74493910fa357a8adc82f0e40d219a`; parent evidence bank
`99ae7ecca2aedbd6a80a56b8660141fb5845af4c`.

Canonical files read in full from the working tree, with the packet's
at-cutoff SHA-256 values I relied on:

```text
fca178eea62a2c6577edd834a6059879ba0610253652138be3cc3ac10acf2890  APPROACHES.md
b760c05928c8f6d839bab6d7bf555fab035ff38c651cf2f5bfb3a77a60d519e2  AUDIT.md
9115568028ed9395697909755190a7bc8df407c2924da82042196f43dd955c05  PROGRESS.md
67763472d3d669a1ae4c97c301918f623c5724d05ff064011bf0a1641a6a6def  notes.md
b41f4ffca4a528038a1a226d46612b25067f5b777f270ad5781eca7327f30060  COORDINATION.md
f0fca49811349483c437d674ab819065eb09500330516d161978868c71bf6371  ladder/REDUCTION.md
```

Delta reports read in full, with the packet's SHA-256 values:

```text
2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b  xmodel/as109-bounded-polar-conductor-gate-20260824.md
bda4dda7d24d36bf75b6c55b566f708ee300c80aeb3344c4bb724bfc7e7787fa  xmodel/as109-bounded-polar-conductor-review-grok-20260824.md
f63bf74fd1013c74645f9f7fe9292db69199572b390b5b19d160c5ed13b373e8  xmodel/gcd3-69-common-cubic-first-gate-20260824.md
```

Verification caveat, stated for honesty: this lane's session had no shell
tool, so SHA-256 values could not be recomputed independently. I consumed the
working-tree bytes at the listed paths and rely on the packet's attestations,
which are consistent with the independent repetitions of the same hashes in
`AUDIT.md` (polar-conductor entry) and the `2026-08-24 13:55Z LIVE STATE`
(`(6,9)` gate SHA). TD6 q2 producer/review hashes (`f098dea4...`,
`6df0d9c9...`) were consumed via their `AUDIT.md` entry; the underlying gate
files were not re-read this round.

Evidence-tier tags used below: **[THEOREM]** promoted dual-confirmed;
**[EXACT]** exact frozen computation, hostile review open (provisional
lifecycle); **[PROV]** exact interim/unfrozen producer evidence (reversible
use only); **[ANALOGY]** structural parallel, no transported statement;
**[SPEC]** speculation, explicitly marked.

---

## 1. Disposition vector over all 46 avenues

Baseline is the current `APPROACHES.md` overlay (reviewed through
2026-08-24 13:52Z). Changes: **raise 19, raise 25, lower/narrow 21,
reopen/narrow 22**; all others unchanged.

| # | Avenue | Disposition | Reason |
|--:|---|---|---|
| 1 | GGV corner farm | unchanged | No delta touches it; bounded lane, bridge-conditional as filed. |
| 2 | Sheet ladder / td=6 | unchanged | Still the #1 proof backbone. The q2 deformation kill is two exact points [THEOREM]; the licensed successor (fraction-free `E[B]` with rank-jump strata) is already canonical. TD6 adjoint progress is [PROV] and within-lane. |
| 3 | Strip / residue ODEs | unchanged | No rank change, but note: its mechanism (valuation-rigid ODE from a face row) is exactly what closed the pure-DS branch of `(6,9)` (`(lambda^7)'=j/(81s)` plus valuations). Credit the mechanism; the avenue itself stays scope-limited. |
| 4 | Formal-germ / D-series | unchanged | Held at `NO-TYPED-STATIONARITY` and `NO-TYPED-SOURCE/NO-QUOTIENT`; nothing in this delta supplies the missing typed source. |
| 5 | JvdK degree descent | unchanged | Cusp leading-form block stands. |
| 6 | Abhyankar–Moh | unchanged | Category error stands; A(F) place data still unpinned. |
| 7 | Nonproperness / A(F) | unchanged | `JUMP-ONLY / TYPE-FAIL` stop stands; no new typed object this round. |
| 8 | Formal-inverse combinatorics | unchanged | No delta. |
| 9 | Lee–Li Conjecture E | unchanged | No delta. |
| 10 | HC4 bridge | unchanged | Stopped `NO LEVERAGE`; no new observable named. |
| 11 | Mathieu/GMC/Zhao ladder | unchanged | Dead (refuted inputs). |
| 12 | Face isolation / p-adic multinomials | unchanged | No delta. |
| 13 | Dixmier DC(2) | unchanged | No delta. |
| 14 | End(A_1) / Zheglov audit | unchanged | Defensive recon posture stands. |
| 15 | Commuting PDOs | unchanged | No delta. |
| 16 | D-module / holonomic index | unchanged | Still no concrete invariant named. |
| 17 | BCW cubic stabilization | unchanged | No delta. |
| 18 | Graded / GIT | unchanged | Closed as CE hunt. |
| 19 | Char-p + Witt lifting | **raise** | Polar conductor is now fully promoted [THEOREM]: no polynomial Keller right map cancels the exterior polar divisor; `kappa_n -> infinity`; caps `p,p` die at depth three. On top of that, the packet's provisional explicit gauge `Phi_F=(A, Q*D(A))` with `A-A^p=P` [PROV; re-derived independently in §3.1 below] converts the licensed quantitative successor from an open-ended search into a concrete finite program (gauge elimination, min-cap profile). The lane keeps disproof-backbone rank with strictly sharper tools. |
| 20 | p-curvature formalism | unchanged | Bridge still consumes false statements. |
| 21 | p-adic Hensel / model theory | **lower (narrowed)** | One of its three named live clients is retired: a "bounded analytic-gauge representative" cannot exist — the promoted theorem makes the canonical gauge degree/support unbounded for any polynomial lift [THEOREM]. Remaining clients: negative-weight `A_infinity` discriminator and rational graph-factor/deck descent. Rank otherwise as filed. |
| 22 | Integral points / heights on fibers | **reopen (narrow, conditional)** | Not the number-field Siegel reading (stays low). The `(6,9)` lower-row structure [PROV] makes the aligned branch a family of curves (invariant fibers) that a trajectory must map into from the Kummer cover `s^3=h`. Function-field integral-point rigidity — Lüroth/de Franchis genus obstructions plus per-fiber valuation ODE analysis — is a live, scoped, cheap client (Card 2). Conditional on hostile review of the `(6,9)` gate and of the lower-row integration. |
| 23 | Analytic global inverse | unchanged | No delta. |
| 24 | Real / Pinchuk | unchanged | No delta. |
| 25 | Monodromy / dessins / passports | **raise (scoped)** | First concrete consumable client since the passport generosity verdict: the constant-Wronskian bypass of the gcd-3 frontier is exactly extremal Davenport–Stothers theory, whose classification is dessin/Riemann-existence mathematics (Stothers 1981; Zannier 1995; Shioda 2005 — already primary-source-checked by the frozen gate [EXACT]). The `(6,9)` gate's "unique DS curve" is `St(3)=1`. Forward prediction: at the next remainders the bypass components are the `St(4)`-type finite lists ((8,12): common quartic, ratio 2:3; (9,12): common cubic, ratio 3:4) [ANALOGY until computed]. Consume as primary-source finiteness theorems, not as passports. |
| 26 | Primitive-group td bound | unchanged | Held without a proved support bound. |
| 27 | Links at infinity | unchanged | No delta. |
| 28 | Log surfaces / BMY | unchanged | No delta. |
| 29 | LND / Hamiltonian mate | unchanged | Stopped after the scoped family theorem. |
| 30 | ML invariant / classification | unchanged | No delta. |
| 31 | Integrality / ZMT | unchanged | Rank two/three known-closed; no rank-`>=4` descendant licensed (Domrina/Żołądek make six the first open sheet degree). |
| 32 | Collision ideal / injectivity | unchanged | Secant accelerator banked; both children `COSTUME`; missing saturated boundary datum unchanged. |
| 33 | Symplectic residues | unchanged | Untwisted residues `COSTUME`; no new twisted class this round. |
| 34 | 2D tangent sweep / pole removal | unchanged | No delta. |
| 35 | Dim-3 descent | unchanged | No delta. |
| 36 | Guided search / SAT / sparse | unchanged (stopped) | `NO-FROZEN-GRAMMAR` stands. Note without reopening: the canonical identity-branch gauge is a genuine gauge **section** for right-composition orbits (§3.1), which is the object whose absence the stop cited; but degrees transform under the polynomial right action (`A(F∘G)=A(F)∘G`), so a minimal-orbit invariant is still missing. No search is licensed. |
| 37 | Finite-field census | unchanged | No delta. |
| 38 | Tropical | unchanged | No delta. |
| 39 | Cohomological cluster | unchanged | Unrestricted completed cohomology stays `GAUGE-TRIVIAL / CONTROL-ONLY`. |
| 40 | Free-associative lift | unchanged | No delta. |
| 41 | Naive scaling deformation | unchanged | Dead. |
| 42 | Markus–Yamabe | unchanged | No delta. |
| 43 | Ritt decomposition | unchanged | No delta. |
| 44 | Moskowicz prime td | unchanged | `REFUTED-AS-PROOF`; the repaired `xy`-membership client is separately closed (`xy` outside the target field). |
| 45 | Differential Galois / Liouvillian | unchanged | The `(6,9)` fiber ODEs are a potential future client, but the in-house valuation method (as in gate §7.1) is currently strictly cheaper than any Kovacic-style import. |
| 46 | Lean / formalization | unchanged | No delta. |

---

## 2. Reranked principal bottlenecks

### Proof side

1. **`(6,9)` lower-weight closure** — the four lower Pfaffian rows, terminal
   row, boundary provenance at the true minimal factor `m_rho`, and the
   cube-mismatch branch `delta != 0`. This is now the sharpest *finite*
   proof-side question in the campaign: it is the unique fundamental
   remainder of the bounded partial-`y` history at maximum nine [THEOREM],
   the high rows are already reduced to five moving coefficients plus one
   essential constant `kappa` [EXACT], and the lower rows provisionally
   integrate to first integrals pinned by Kummer weights [PROV]. Closing it
   re-arms the historical induction: maximum actual `y`-degree 10 and 11 then
   go classical by the same shear/coverage arguments, and the frontier moves
   to `(8,12)` with `4|H` and `(9,12)` with `3|H` (checked against the
   promoted shear theorem's covering moves; see §3.3).
2. **TD6 `E[B]` elimination** — the licensed fraction-free elimination over
   the degree-18 field with every pivot/rank-jump stratum separate; the
   adjoint jets are accelerators only [THEOREM scope]. Behind it: the eight
   terminal classes, global realizability/opposite-side balance.
3. **Foundational coverage** — `G2-PSC`, universal landing/coverage, absent
   td ceiling (`ladder/REDUCTION.md` CRITICAL 3–7). Unchanged, long-horizon,
   and still the reason no finite kill closes JC2 by itself.
4. Composite single-pole and off-axis books — unchanged, behind the above.

### Disproof side

1. **The two global AS109 keys** — `A_infinity=0` (integral finiteness of the
   formal fibre algebra) or rational deck descent. Unchanged as the endgame
   gap [THEOREM scope of the ledger].
2. **Quantitative gauge growth** — newly concrete: with the explicit
   algebraic gauge [PROV], the licensed successor "lower growth law for
   `kappa_n`" becomes a finite, per-depth-checkable min-cap program (§3.1,
   Card 1). This is now the most attackable disproof-side bottleneck.
3. **The `(6,9), 3|H` habitat** — conditionally on an exact lift, maximum
   actual `y`-degree nine forces exactly this family [THEOREM]. So the same
   finite system is simultaneously proof bottleneck #1 and the cheapest
   currently-named place a counterexample could live. A pincer: any decisive
   `(6,9)` outcome moves both backbones.
4. A genuinely coupled `CLOSED-SUPPORT + UNIT-L` certificate — still no
   candidate support; unchanged.

---

## 3. New mechanisms and new cross-avenue connections

### 3.1 New mechanism (disproof lane): gauge elimination via the explicit Artin–Schreier–Hensel root

The packet's provisional observation is that the unique identity-branch gauge
of the promoted completed-orbit theorem is explicitly

```text
Phi_F = (A, Q*D(A)),    A - A^p = P,    D(T) = 1 - p*T^(p-1),
```

for any exact lift `F=(P,Q)`. I re-derived this independently rather than
consuming it blind [PROV, my verification]:

- `A` exists and is unique in `Z_p<x,y>` with `A == x mod p`: Hensel in the
  complete Tate algebra, since `T - T^p - P` vanishes at `T=x` modulo `p` and
  its derivative `D(x) == 1 mod p` is a unit.
- `C_p(A, Q*D(A)) = (A - A^p, Q*D(A)/D(A)) = (P, Q) = F` exactly.
- Differentiating `A - A^p = P` gives `grad A = grad P / D(A)`, hence
  `det J(Phi_F) = D(A)*det(grad A, grad Q) = det J(F) = 1`; the
  `Q*D'(A)*grad A` term dies against `grad A` in the determinant.
- Identity branch and uniqueness then force `Phi_F` to *be* this map, by the
  promoted wild theorem.

Consequences that are new relative to the packet's own speculation list:

1. **Gauge elimination.** Every bounded-cap system `B_(p,n)(D_F,D_phi)`
   currently searches over map and gauge coefficients jointly. But the gauge
   is a *deterministic function of `F`* (Newton digits of `A` from `P`
   alone). So the honest object is an **F-only tower**: fix `p` and a total
   degree `D_F`; at depth `n` the finite system is just
   `deg F <= D_F`, `F == (x-x^p, y) mod p`, `det J(F) == 1 mod p^n` — no
   gauge unknowns at all — and `kappa_n(F)` is *computed*, not searched.
   König's lemma (exactly as in the reviewed gate §5) gives: for each
   `(p, D_F)`, either an exact `Z_p` lift of degree `<= D_F` exists, or the
   F-only tower is empty at some computable finite depth. This is an exact
   decision procedure for bounded-degree lift existence, per prime — it
   terminates on the empty side, and persistent nonemptiness is a tracking
   signal, never a proof.
2. **Built-in negative controls.** The promoted bounded-`y` field theorems
   [THEOREM] already imply the F-only tower must die for every `D_F <= 8`
   (a lift of `y`-degree `<= 8` would be an automorphism, contradicting
   109-ball noninjectivity; the ball argument is reviewed at `p=109` and its
   proof is p-uniform — a one-page freeze should restate it at general odd
   `p` before use elsewhere [PROV until frozen]). Measured death-depths for
   `D_F <= 8` calibrate the method before the live frontier `D_F >= 9`.
3. **Growth law = plateau bound = min-cap sequence.** Define the conductor
   profile `gamma_(p,D_F)(n) = min kappa_n(F)` over depth-`n` points of the
   F-only tower. A plateau of `deg_n(A)` at degree `C` through depth `m`
   is exactly a depth-`m` approximate lift whose canonical gauge truncates at
   degree `C` — i.e., a nonempty capped system. So the packet's speculative
   exact law "minimum simultaneous cap at depth `n` is `(n-1)(p-1)+1`"
   (known `n=2,3`) is equivalent to a plateau bound on the digit degrees of
   one explicit algebraic function, and each instance is a finite exact
   computation. The natural proof schema is a **universal top-monomial
   induction**: the depth-`n` composition digit inherits the geometric-series
   top term `x^((n-1)(p-1))*y` with unit coefficient — the depth-3 forbidden
   monomial `x^(2p-2)y` [THEOREM] is its `n=3` case — and the induction claim
   is that below the cotangent slope no digit cascade can cancel it. [SPEC
   as a theorem; finite per-depth checks are exact.]

Scope honesty: none of this excludes an unbounded-degree lift; it makes the
*bounded* frontier effective and pins the extremal geometry of the completed
orbit's polynomial-gauge stratification to the cotangent control.

### 3.2 New mechanism (proof lane): Lüroth/genus rigidity on the `(6,9)` invariant fibers

Conditional on the provisional lower-row integration [PROV]: the four zero
rows integrate to `I_4=I_3=I_1=0`, `I_2=mu`, so every aligned trajectory lies
on a fiber `V_(mu,kappa)` — generically a **curve** in `(a_0,...,a_4)`-space
(five coordinates, four independent integrals), on which the terminal row
induces a single rational ODE, exactly as `(lambda^7)'=j/(81s)` on the DS
fiber. A trajectory is a nonconstant `k`-morphism from the Kummer cover
`X_h: s^3=h(x)` (aligned noncube branch; coefficients have Kummer weights
`-i mod 3`) into `V_(mu,kappa)`. Two consequences:

- **Genus triage.** A nonconstant morphism of smooth projective curves needs
  `genus(X_h) >= genus(V_(mu,kappa))`. If the generic fiber has geometric
  genus `>= 1`, then for each fixed `h` all but finitely many/special fibers
  and rank-drop strata are instantly empty of nonconstant trajectories, and
  low-degree `h` (small cover genus: e.g. `h=x^2(x-1)` gives genus 0,
  squarefree cubic `h` gives genus 1) is strongly constrained. [SPEC on the
  generic genus value; the mechanism is classical.]
- **Uniform per-fiber kill.** Whatever the genus, the finishing move is the
  gate's own §7.1 pattern per fiber: valuation bookkeeping of the induced
  ODE forces the support of the moving parameter onto the zeros of `h`, then
  the two polynomial boundary values (1.6) close the branch. Genus decides
  how many fibers need the full treatment.

This does not duplicate the active noninterruptible `(6,9)` worker: their
registered task list is fiber/strata classification and boundary provenance;
this supplies the rigidity tool for the "generic rational trajectories" step
and a triage order. See Card 2.

### 3.3 New cross-avenue connections

1. **`(6,9)`/gcd-d frontier ↔ avenue 25 (dessins) [primary new connection].**
   The identity `f*H' - 3*f'*H = -(2*f*g_z - 3*f_z*g)*g`, `H=f^3-g^2` [EXACT]
   makes the constant-Wronskian bypass at degrees `(6,9)` exactly the
   extremal Davenport–Stothers locus; its uniqueness is `St(3)=1`, a
   dessin/Riemann-existence count (Stothers; Zannier). The same structure
   recurs at every future fundamental remainder of the bounded-`y` ladder:
   after `(6,9)`, maxima 10 and 11 are classical by the promoted shear
   coverage (all `gcd >= 3` pairs there are divisible/equal, hence reduced by
   the filed target moves), and the next remainders are `(8,12)` with `4|H`
   (ratio 2:3, common **quartic**, same `2fg'-3f'g` Wronskian, `St(4)`-type
   bypass list) and `(9,12)` with `3|H` (ratio 3:4, `3fg'-4f'g` against
   `H=f^4-g^3`, Zannier's general-signature theory). So avenue 25's
   dessin-classification literature becomes a *consumable finiteness input*
   that pre-classifies the nonlinear bypass components of every future gate
   in this ladder — one uniform theory instead of bespoke primary
   decompositions. [ANALOGY tier until each instance is computed; the (6,9)
   instance is already exact.]
2. **`(6,9)` invariant fibers ↔ avenue 22 (integral points), function-field
   form.** As in §3.2: trajectories are integral/rational points of fiber
   curves over the Kummer cover, and the operative theorems are Lüroth/
   de Franchis/Riemann–Hurwitz plus explicit valuation analysis — the
   tractable function-field shadow of the avenue's number-field instinct.
3. **AS109 ↔ `(6,9)` pincer (sharpening an existing link).** The promoted
   corollary already reduces a maximum-nine lift to `(6,9), 3|H`. The new
   content: because the bounded-`y` theorems are field theorems, closing
   `(6,9)` over all characteristic-zero fields simultaneously raises the
   AS109 correction floor at *every* odd prime to `y`-degree `>= 10` — and,
   with maxima 10/11 classical, to `>= 12` — with no new p-adic work. The
   same exact computation is therefore both backbones' cheapest next step.

---

## 4. Strongest attacks

### Strongest proof attack

Close the aligned `(6,9)` branch by the fiber program: (i) hostile-review and
freeze the lower-row triangular integration and first-integral pinning
(currently [PROV]); (ii) classify invariant fibers and rank-drop strata
(active worker); (iii) genus triage per §3.2, then the §7.1-style valuation
ODE plus both polynomial boundaries on each surviving fiber; (iv) boundary
provenance strictly at the minimal factor `m_rho` (the gate's `TYPE-FAIL`
discipline); then (v) the cube-mismatch branch `delta != 0` by the same
machinery with its larger constant set (Card 3). In parallel keep TD6 `E[B]`
elimination as the independent backbone. Payoff if it lands: first true
closure of the bounded-`y` ladder's fundamental remainder, frontier moves to
`(8,12)/(9,12)` with the DS/dessin bypass lists pre-identified, AS109 floor
rises to `>= 12` everywhere.

### Strongest counterexample / falsification attack

Drive the *least constrained live finite system* to a decision, giving the
counterexample every chance: the `(6,9)` cube-mismatch branch (`h` a cube,
no Kummer forcing, integration constants `c_j` alive, `delta != 0`
permitted) plus non-DS invariant fibers of the aligned branch. Any
nonconstant trajectory surviving valuations *and* both polynomial boundary
conditions is a concrete max-`y`-nine Keller candidate — the nearest named
habitat for a counterexample anywhere in the portfolio. Secondary attack:
the p=3/5 F-only towers (§3.1) run *without* gauge caps — if some
`D_F >= 9` tower refuses to die at depths well beyond the `D_F <= 8`
calibration curve, that is the first honest positive tracking signal for an
exact lift; its coefficient trace then feeds the `(6,9)` normal form
directly. Both attacks are falsification-first: the expected outcome is
closure, and the design makes a survivor maximally informative.

---

## 5. Software accelerator / decisive experiment

**Canonical-gauge digit compiler** (bounded, exact, no AWS, no `p=109`):

1. Implement the AS-Hensel Newton digit recursion for `A` from `P` over
   `Z/p^n` (sparse integer dicts, exact; the digit layers are linear once
   lower digits are fixed, as the reviewed gate records).
2. Expose `kappa_n(F)` and `deg_n(A)` as deterministic functions of `(P,Q)`.
3. Rebuild the existing cap systems as F-only towers (gauge unknowns
   eliminated); rerun the frozen `p=3,5` depth-3 controls as regression.
4. Decisive experiment: compute `gamma_(3,*)(4)` — the exact minimum
   simultaneous cap at depth 4 for `p=3` — testing the packet's provisional
   law `(n-1)(p-1)+1 = 7`. Then the `D_F<=8` death-depth calibration curve.

Every outcome is informative (see Card 1). Cost: one lane, standard library,
days not weeks; same replay discipline as `cases/as109_bounded_polar_conductor_20260824/`.

---

## 6. Idea cards (exactly three)

### Card 1 — AS109 conductor-growth law via gauge elimination

- **Claim targeted.** For fixed `(p, D_F)`: the F-only tower's minimal
  canonical gauge degree obeys `gamma(n) >= (n-1)(p-1)+1 - c(D_F)`;
  ideally the exact law `min-cap(n) = (n-1)(p-1)+1` [SPEC].
- **Dependencies.** Promoted polar-conductor + wild gates [THEOREM]; the
  explicit gauge identity `Phi_F=(A, Q*D(A))` — currently [PROV], needs a
  one-page producer freeze plus hostile review (my independent re-derivation
  is in §3.1); the p-uniform restatement of the ball-noninjectivity lemma
  [PROV until frozen].
- **Cheapest discriminator.** Exact `gamma_(3)(4)` at `p=3` via the digit
  compiler (§5): is the depth-4 minimum simultaneous cap exactly 7?
- **Outcomes.** `=7`: law supported; attempt the universal top-monomial
  induction (the `x^((n-1)(p-1))y` unit coefficient as the uncancellable
  digit), aiming at an all-`n` theorem — which would make the first failing
  depth an explicit function of the caps, the review's named successor.
  `<7`: the exact law is false; the surviving `F`'s exhibit unexpected gauge
  flexibility — study them as potential lift trackers (falsification-side
  information). `>7`: growth is faster than the cotangent slope; revise the
  law upward — even stronger exclusion geometry.
- **Stop condition.** If the top-monomial cancellation is structurally
  possible at depth 4 (an explicit cascade found), stop the induction route
  and keep only per-depth computation; hard stop after one review cycle of
  effort or if the gauge-identity freeze is refuted.
- **Expected information gain.** High: converts the promoted gate's
  qualitative `kappa_n -> infinity` into the first quantitative invariant of
  the completed orbit; any outcome strictly sharpens the polynomial-gauge
  stratification; no outcome is wasted (calibration data feeds the towers).

### Card 2 — `(6,9)` invariant-fiber rigidity (genus triage + per-fiber valuation kill)

- **Claim targeted.** Every nonconstant aligned `(6,9)` trajectory lies on an
  invariant fiber curve `V_(mu,kappa)`; fibers with genus exceeding the
  Kummer cover's genus carry none; each surviving fiber dies (or survives
  explicitly) under the §7.1 valuation ODE plus both polynomial boundaries.
- **Dependencies.** Frozen `(6,9)` gate [EXACT, review active]; the lower-row
  triangular integration and Kummer pinning [PROV — must be frozen and
  hostile-reviewed first]; the active worker's fiber/strata classification
  (this card is sequenced *after* their freeze, not concurrent).
- **Cheapest discriminator.** Exact genus of the generic fiber
  `V_(mu,kappa)` (Singular `normal.lib`/genus on the explicit first-integral
  equations; hours).
- **Outcomes.** Generic genus `>= 1`: the aligned branch collapses to
  rank-drop strata, finitely many special fibers, and small-`h` covers —
  enumerate and kill per fiber. Generic genus 0: uniformize rationally; the
  terminal row becomes one explicit rational ODE family; run the valuation/
  boundary analysis uniformly (the DS case §7 is the worked template).
  Reducible/nonreduced fibers: feeds the strata map; treat components
  separately (the gate's own discipline for the nonreduced common
  component).
- **Stop condition.** Refutation of the lower-row integration at review kills
  the card; two non-informative fiber analyses on the same representation
  force redesign per protocol.
- **Expected information gain.** Very high: this is bottleneck P1 = D3 (the
  pincer). Either a major collapse of the aligned branch's freedom, or an
  explicit surviving trajectory family — a counterexample lead at maximum
  `y`-degree nine.

### Card 3 — Cube-mismatch branch normal form (`delta != 0`)

- **Claim targeted.** The cube branch (`h` a polynomial cube, `s in k[x]`,
  no nontrivial Kummer action) integrates to the same Pfaffian shape with a
  finite surviving constant set (`delta`, the un-killed `c_j`), so the fiber
  machinery of Card 2 applies uniformly; or it exhibits a genuinely
  different structure that must be flagged before anyone treats "aligned"
  results as covering `(6,9)`.
- **Dependencies.** Frozen `(6,9)` gate section 1 [EXACT, review active];
  nothing from the aligned lower-row [PROV] is consumed — this branch is
  independent by construction.
- **Cheapest discriminator.** One exact SymPy session: depress with
  `z=sy+r`, keep the `z^8` coefficient `-delta/2 != 0`, integrate the high
  rows, and count surviving constants; check whether any high row forces
  `delta=0` (branch merge) or obstructs triangular integration.
- **Outcomes.** Triangular with finite constants: uniform treatment — Card 2
  machinery extends; write the joint fiber map. A row forces `delta=0`: the
  branches merge and the aligned analysis is exhaustive — a significant
  simplification, promote after review. Integration obstructed: genuinely
  new structure; stop and redesign with the obstruction as the new object
  (do not force the aligned template).
- **Stop condition.** Review refutation of gate section 1; or the
  discriminator session exceeds one day without a clean trichotomy — then
  file as `NEEDS-NORMAL-FORM` and hand to the next full round.
- **Expected information gain.** Medium-high and cheap: the cube branch is
  currently the least constrained live piece of the `(6,9)` remainder (and
  hence of the counterexample habitat); any trichotomy outcome materially
  changes the closure plan.

---

## 7. Continue / redesign / stop for current major lanes

| Lane | Recommendation | Reason |
|---|---|---|
| `(6,9)` lower rows / invariant fibers (exact worker) | **continue** | Bottleneck P1=D3; provisional integration is the right object; freeze early so Cards 2–3 can sequence. |
| TD6 adjoint + staged `E[B]` pencil (exact worker) | **continue** | Licensed successor; keep the adjoint strictly as accelerator, all rank-jump strata separate, per the confirmed review scope. |
| AS109 polar-conductor successor | **redesign (light)** | Of the two licensed successors, take quantitative growth *first* (the explicit gauge makes it finite and cheap — Card 1); the `A_infinity` comparison second, as an independent theorem, exactly as the review insists. First deliverable: freeze the gauge identity. |
| Hostile review of the frozen `(6,9)` gate | **continue (top review priority)** | Highest downstream fanout in this round: Cards 2–3 and the pincer logic all consume it. |
| Blind ideation / outer loop / event rounds | **continue** | Protocol working as designed; this round's trigger discipline was correct. |
| Broad web sweep #9 (due 21:25Z) | **continue (mandatory)** | Add targeted queries: Davenport–Stothers/Zannier/Shioda signature-(2,3)/(3,4) extremal pairs, "common cubic Jacobian pair", polynomial-Pell/Chebyshev function-field literature; the gate's DS history check was negative but the connection is now load-bearing. |
| Stopped/held lanes (generic sparse search, exponent rectangles, `p=109` brute force, B=168, D75, new book cells, unrestricted Witt depth, AWS expansion, D-series beyond current stops) | **stop (keep stopped)** | No delta reopens any of them; the canonical gauge does not license a support search (§1 row 36). Box01's protected `build_tails43.py` core untouched; boxes 02/03 stay stopped. |

---

## 8. Source-honesty ledger for this report

- [THEOREM] consumed: polar conductor (all eight claims, dual-confirmed);
  wild-symplectic completed orbit; bounded-`y` field theorems through the
  history stop (`<=8` classical; `(6,9),3|H` sole max-9 remainder); TD6
  fixed-family emptiness and q2 two-point kill; AS109 Hensel degree/split
  ledger; TD6 q2 confirmed inputs.
- [EXACT, review open] consumed: the frozen `(6,9)` common-cubic gate's
  eight stated conclusions at their stated scopes, including the conditional
  pure-DS exclusion and the five-plus-`kappa` reduction.
- [PROV] consumed reversibly: `(6,9)` lower-row triangular integration and
  Kummer pinning; DS-locus `kappa=0` forcing and the determinant restriction;
  TD6 adjoint interim replays; the explicit algebraic gauge
  `Phi_F=(A,Q*D(A))` (independently re-derived here but still requiring
  freeze + hostile review before promotion).
- [ANALOGY]: the DS/dessins uniformity of future gcd-d remainders; the
  function-field integral-point framing.
- [SPEC], explicitly: the `(n-1)(p-1)+1` all-`n` min-cap law; the universal
  top-monomial induction; generic genus `>= 1` of the invariant fibers; any
  expectation about F-only tower behavior at `D_F >= 9`.
- Nothing here proves or disproves JC2; no stopped lane is reopened beyond
  the two scoped dispositions (22 narrow-reopen, 25 scoped raise) recorded
  in §1.
