# Independent probability assessment of the current decision tree

Snapshot: 2026-08-13, about 17:20 PDT. These are my epistemic point
estimates from the checked repository state, rounded to avoid fake
precision. Branch 1 uses the stated 12-hour caps. Unless stated otherwise,
branches 3--8 mean one focused five-working-day push with the present
engines and fleet. Modular `GB = [1]` is evidence; only a characteristic-zero
certificate is proof. The prime lanes are strongly correlated, so I do not
count six launches as six independent chances.

## Probability table

| branch | probability estimate | one-line reasoning |
|---|---:|---|
| **1a. Box02 no-log: at least one main-prime verdict by its 12 h cap** | **55%** | At 1.6 h all three main and three control lanes are healthy at about 18 GiB each, but earlier two-hour runs produced nothing and the nearly identical prime trajectories make runtime risk highly correlated. |
| **1a'. At least two concordant main-prime verdicts by cap** | **40%** (all three: **30%**) | One finishing F4 trajectory makes siblings more likely to finish, but also means a common degree/memory cliff can time out the whole batch. |
| **1b. EMPTY \| a main lane reaches a verdict** | **65%** | Six exact pins remove the known level-42 escape, the differential and every solved affine stratum are inconsistent, and the residual is mildly overdetermined; tier-1 Macaulay consistency and repeated template identities keep this well below 90%. |
| **1c. Characteristic-zero upgrade after two good-prime EMPTY verdicts** | **95%** that char-0 is actually empty; **55%** that a proof certificate lands within the next week | Concordant good-prime `[1]` is powerful evidence, but the exact computation can be much harder than the modular screens; a certified char-0 `[1]` kills residue-A and closes on-axis `td=6` under the promoted template perimeter. |
| **2. Explicit point after a genuine NONEMPTY main verdict** | **60%** for a raw-row-verified finite-field point; **35%** smooth/Hensel-usable; **15%** prompt exact char-0 lift | A completed nonempty GB should permit slicing or an RUR, but positive dimension and singular boundary components can make extraction/lifting substantially harder than the verdict. |
| **3. Toric tier-2 after timeout** | **35%** to complete a purpose-built fixed-fiber rank run in one Box02 day; **20% kill \| completed run**; **<5%** campaign-wide kill per launch | Tier 1 gained rank but remained exactly consistent, while tier 2 is already 135,240 rows, 6.94M columns, and 87.1M nonzeros; moreover a contradiction at `(+,+,1,1)` kills only that fiber without a uniformity theorem. |
| **4. Six-cell `td=7` coefficient gluing** | **32%** significant progress; **6%** full `td=7` closure | Four cells are singleton-route pilots, but the only audited next-tier cell survives, the gluing equations are not yet emitted, and `(10,15,7,5)@3` holds 47/53 routes including all 18 slack routes. |
| **5. Q2 decomposition** | **75%** at least one useful leaf verdict; **45%** complete l8 cover; **25%** complete l4 cover; **15%** both covers | The four-leaf precedent is excellent, but l8/l4 introduce many more low variables and high jet degree than the tiny §13 core, so decomposition may move rather than remove the GB cliff. |
| **5'. Q2 scientific payoff** | **70%** useful independent locus reduction; **18%** full minimal-UU-locus closure from this program | Q2 is genuinely independent of the J-window rows, but l8/l4 are nested support strata: even EMPTY l4 leaves slots 1--3, and NONEMPTY is only a quotient-window germ. |
| **6. D25 / Row 24 bounded probe** | **25%** useful new structural relation; **4%** kill | D23 added ten independent Row-22 conditions but also ten new high tails and stayed consistent; Row 24 alone merits a probe because it is the recorded `h2/b2` resonance. |
| **6'. Unbounded rows 25--41 continuation** | **<10%** significant progress; **<2%** kill | Past Row 20 the equations become more nonlinear while each depth increment supplies new absorbing tails; absent a rank-deficit mechanism this is unfavorable constraint-versus-variable growth. |
| **7. Sound finite refile in one week** | `td=11`: **50%**; `td=13`: **25%** | The old 12/129 cell counts are void and the repaired priced alphabet lacks a completeness bound; `td=13`'s mixed and inner-merge state space is materially worse. |
| **7'. A ported zero-chain/ODE analogue decides most cells \| sound refile** | **35%** (full closure of either prime-`td` book: **8%**) | The `td=7` 56/62 result exploits one shared one-nonzero-orbit normal form; higher books contain multi-orbit, mixed, and nested merges, although each fixed Prop. 8.1(iv) equation remains a promising linear ODE. |
| **8. Overlooked: decompose the exact Q2 l13→l12 cliff first** | **70%** complete modular leaf-cover verdict in 1--2 days; **85%** useful progress | l12 adds only the low triple `uf24,bg42_24,bg21_24` and six level-60 highs to the already-proved-empty l13 object, giving a natural three nonzero charts plus the settled origin chart. |
| **8'. Follow-on: intersect surviving l12 leaves with J/no-log rows** | **45%** significant additional reduction in a focused week | Q2 and J are different necessary row families on the same coefficients, so individual survival does not protect their intersection; leaf reduction should precede this joint build. |

For branch 2, the honest significance stops at a **D21, no-log-pinned,
frozen-chart window-consistency germ**. Even a smooth finite-field point is
not a counterexample: it has not passed the Q2 quotient tier, D23 Row 22 or
deeper J rows, restored B-side freedom/normalization, the other residue-A
branches, or polynomial algebraization.

For branch 5, I value Q2 highly as an orthogonal constraint family and only
moderately as an independent *route*. Its best use is to make a small leaf
cover and then intersect survivors with the no-log/J system. Calling an l8
or l4 NONEMPTY result “residue-A survives” would be the same wrong-object
inflation the campaign has already had to retract elsewhere.

## Top two parallelization picks

### 1. Protect the current Box02 no-log deciders

This is the top pick because the marginal cost is already sunk, the files are
guarded, and a char-0 EMPTY certificate has the largest immediate payoff in
the tree.

First-day plan:

1. Let the three **main** no-log primes reach their 12-hour caps. Treat the
   controls as secondary; if total RSS crosses 1.5 TiB, shed plain/stuck
   jobs first and control lanes second, not the three main lanes.
2. Preserve per-lane command, return code, wall/RSS, output size, input hash,
   and the distinction between a zero-byte timeout and a verdict.
3. On the first main `[1]`, protect a second prime and launch an independently
   hard-substituted twin; prepare the characteristic-zero lane immediately.
   Promotion still waits for the exact certificate.
4. On the first genuine `GB != [1]`, record dimension, take randomized
   zero-dimensional slices, extract a finite-field point, and verify it with
   an independent parser against all 91 original equations before discussing
   a germ.
5. If every main lane times out, stop at the registered cap. Do not buy an
   unmeasured extension and do not immediately pour the box into the naive
   toric tier.

### 2. Q2 l12 first-nonzero leaf cover, not cold l8/l4

This is the best new probability × payoff / cost object. The exact l13→l12
header delta is nine variables: three low slot-12 variables and six
level-60 highs. The origin of the low triple reduces to the already
char-0-empty l13 stratum.

First-day plan:

1. Freeze the l12 object, row subset, saturation semantics, and an exact
   l13-regression guard before elimination.
2. Prove mechanically that the six new high variables occur linearly with
   coefficients in the low triple. Split the remaining locus into the
   disjoint charts
   
   - `uf24 != 0`;
   - `uf24 = 0, bg42_24 != 0`;
   - `uf24 = bg42_24 = 0, bg21_24 != 0`;
   - all three zero, discharged by the l13 char-0 certificate.
3. On each unit chart, row-reduce the 7-by-6 high-variable block,
   bank every invertible pivot and back-map, and pass exact/random-point
   round-trip guards before emission.
4. Emit the three nonorigin leaves at both banked primes with relaxed and
   saturation-only controls. Add the three B-side no-log pins only after
   the already-flagged B-place normalization guard is proved.
5. Run the smallest reduced leaves first. By end of day, either bank early
   verdicts or a measured residual-size table. Continue to l8 only if the
   l12 charts actually reduce the compatibility core; otherwise redesign
   before multiplying leaf counts.

## What I would stop

I would stop the **naive toric tier-2 implementation** outright: do not
materialize 7.8M pair binomials or feed them to msolve. The original nonlinear
screens are mathematically stronger, and the proposed Macaulay object is both
huge and initially only a fixed-fiber test. A compact CSR/block rank pilot is
reasonable only after all main no-log lanes time out and only with a six-hour
feasibility gate.

I would also stop an **unbounded depth-25+ sweep**. Permit exactly one D25
Row-24 resonance probe; if it again adds approximately one independent
condition per new tail direction, park rows 25--41 until a theorem predicts
a deficit.

Finally, I would not start the full `td=13` refile or the 47-route
`(10,15)` gluing core on day one. Give `td=11/13` a one-day normal-form
census and give the three singleton `td=7` cells a bounded gluing pilot,
but neither currently beats l12 decomposition.

## Priority disagreements

1. **Q2 should start at l12, not l8/l4.** l12 is the exact proved/unproved
   frontier and has a three-variable first-nonzero cover; jumping lower
   discards the campaign's best structural information.
2. **“62 cells → 6” does not mean `td=7` is near closure.** Almost all
   remaining route complexity is concentrated in one cell, and the first
   tested survivor passed transport. Coefficient gluing is a good bounded
   orthogonal pilot, not the second main campaign lane.
3. **A Box02 timeout is not evidence for toric priority.** Tier-1
   consistency plus fixed-fiber semantics make tier 2 a low-probability,
   high-engineering detour compared with l12 leaves and then a Q2+J
   intersection.
