# Sol instrument decision: residual-32 nolog

**Date:** 2026-08-16  
**Decision horizon:** one focused week, at most $5,000 of cloud credit  
**Object:** the D21 residue-A no-log window, 84 variables, 85 main equations
(91 in the append-only pinned file), with 42 occurring high tails affine-linear.

## Verdict

The next instrument is **C: exact symbolic band elimination**, followed by a
solver bakeoff on the compressed system. Do **not** launch a fresh raw
24-hour `p105337` monolith on 6 TB today. Such a run would repeat only the
first half of a trajectory that already timed out at 48 hours, while using
almost none of the extra memory.

My preferred portfolio is a modified hybrid, **G\***:

1. compile the six no-log pins and the band-triangular unit pivots, producing
   the 32-condition compatibility ideal;
2. A/B-test `msolve` and GamBa (Magma if a license is immediately available)
   on that compressed object;
3. in parallel, build the Q2-`l12`/J common-variable intersection map and run
   only the bounded D25/Row-24 resonance probe;
4. buy one 6 TB run only if the compressed pilot or alternate engine shows a
   pre-registered improvement of at least 3x.

This converges with Fable's preference for a hybrid in spirit, but differs on
both immediate lanes: **not a raw 24-hour main, and not generic
algebraization**. The iron should amplify a structural reduction; the theory
lane should be Q2/J plus one Row-24 probe.

## Why C moved to the top

The previous `msolve -e 45` lane asked F4 to discover an elimination that is
already visible in the exact grading. A direct audit of the banked D21 rows
gives a materially smaller task:

- There are no high-high monomials. All 42 emitted high tails are
  affine-linear.
- Bands 6, 8, and 10 contain no high tails. The six level-42 no-log variables
  can be substituted out, rather than appended as six extra equations.
- In bands 12, 14, 16, 18, and 20, the newly introduced high blocks have
  ranks `2, 2, 4, 4, 4`. Their coefficients are independent of the low data;
  each is one Laurent monomial in the nonzero `W_i` times an E-unit.
- Across all four h-sign branches, the same 16 pivots occur: the `tf1` and
  `tf2` variables at levels `43,44,45,46,47,48,50,52`. The exact claim-4
  replay on both certified low seeds leaves 32
  residual rows with **no remaining high coefficient**. The 26 g/g0 highs
  are reconstruction-free directions once compatibility holds.

That last observation is strong evidence, not yet the symbolic proof. The
compiler must verify coefficientwise that the residual high coefficients
reduce to zero modulo the early-band equations. Two seeds cannot replace
that identity.

The correct C implementation is therefore not “seven independent small
GBs.” Later bands recouple earlier free directions. It is a single exact
triangular/module computation:

1. hard-substitute the six level-42 pins;
2. consume the certified C6 rank-1 and C8 rank-2 E-unit pivots;
3. echelon each new-level block, carry every nonpivot direction forward, and
   reduce later rows modulo earlier conditions;
4. use the fixed 16 Laurent-unit high pivots through the joint 18/20 endgame;
5. emit the resulting 32 low-data compatibility polynomials.

The expected full output is about 32 equations in 36 prime-field variables
after the 42 highs and six pins are removed, including the radical and
saturation bookkeeping. On a fixed E/sign factor of chamber `a0`, the target
is the already identified **32 equations in 15 active base variables**. This
is the first object worth giving to F4, not the 84-variable source.

### C acceptance and stop criteria

Accept the transform only if all of the following hold:

- the symbolic residual has exactly the registered 32 labels and no high
  coefficient;
- its pivot set and result agree on all four h-sign branches and reproduce
  both claim-4 seeds;
- random exact points satisfy `rank(A)=rank([A|b])` exactly when the 32
  compatibilities vanish;
- solving the pivots and back-substituting verifies every untouched original
  row, including the `+42` row and all saturation equations;
- `ctl0` remains satisfiable and the known `a3` `[1]` result is reproduced.

Stop C as an acceleration if the first guarded emission exceeds one million
terms or the raw pinned term mass, needs more than roughly eight genuinely
different rank branches, or gives less than a 3x improvement in same-degree
`-v 2` matrix/RSS telemetry. Failure of the acceleration is not a
mathematical survival verdict.

Estimated cost is one to three engineering days, less than $100 for the
first fleet pilot, and $500-$1,000 for a serious compressed run. I put the
chance of a valid compressed emission at **80-90%**, and the chance that it
produces a system-level modular verdict within a week at **25-45%**.

## Bigger iron: what the measurements actually say

The campaign does not contain degree or Macaulay-matrix telemetry: the long
jobs ran at `-v 0` and discarded progress output. Therefore it is impossible
to tell from the record whether 12 TB buys one F4 degree or five. What is
known is:

- the three R2 primes were trajectory clones at about 96-98 GiB after 15
  hours;
- they were about 500 GiB per lane at 48 hours and still climbing;
- the order variants also timed out, and long R2 phases used only about
  1.06-1.17 cores per lane;
- the 48-hour failures were wall caps, not 2 TB per-lane OOMs.

Two deliberately crude fits show the uncertainty:

| two-point RSS model | reaches 1 TB | reaches 2 TB | reaches 6 TB | reaches 12 TB |
|---|---:|---:|---:|---:|
| constant log-slope (doubling every 14 h) | 62 h | 76 h | 98 h | 112 h |
| power law through the same two points | 78 h | 128 h | 280 h | 457 h |

The first is the pessimistic memory-runway scenario. In it, 12 TB buys only
about 14 additional hours over 6 TB--quite plausibly one large degree step.
The second says memory is irrelevant for days and wall time dominates. The
record cannot distinguish them. Both agree on the actionable fact: at 24
hours a restart is only around 150 GiB under the faster-growth model and has
not even reached the already-failed frontier.

At the account's current us-east-1 Linux on-demand rates checked today:

| instance | RAM / vCPU | hourly | 24 h | 48 h | 72 h |
|---|---:|---:|---:|---:|---:|
| `u-6tb1.56xlarge` | 6 TiB / 224 | $46.40391 | $1,114 | $2,227 | $3,341 |
| `u-6tb1.112xlarge` | 6 TiB / 448 | $54.60 | $1,310 | $2,621 | $3,931 |
| `u-12tb1.112xlarge` catalog entry | 12 TiB / 448 | $109.20 | $2,621 | $5,242 | $7,862 |

The 56xlarge is the rational old-U choice: it has the same 6 TiB and still
far more cores than the observed phase uses. A 12 TB run exhausts the whole
monthly envelope before it even reaches the prior 48-hour frontier. AWS now
recommends U7i for new high-memory workloads, and sales of legacy 9/12/18/24
TiB U-1 capacity ended in 2025; current capacity must be confirmed rather
than inferred from a catalog SKU. See the [AWS instance specifications](https://docs.aws.amazon.com/ec2/latest/instancetypes/mo.html)
and [High Memory page](https://aws.amazon.com/ec2/instance-types/high-memory/).

There is also an immediate operational blocker: the read-only account check
on 2026-08-16 reports quota **0** for “Running On-Demand High Memory
instances,” no pending increase, and no Spot offering for `u-6tb1`. The
literal “u-6tb spot today” lane is unavailable. File the quota/capacity
request now, but do not let it block C.

If raw iron is nevertheless chosen, fund at least 72 hours, isolate one lane,
capture `-v 2`, and use a 6 TB 56xlarge. My estimate for a raw modular verdict
by 72 hours is only **10-25%**; for a proof-tier decision in the same week,
**5-12%**. A raw 24-hour verdict is below **5%**.

## Ranked marginal instruments

Probabilities below are subjective one-week estimates. They are correlated
and must not be added. “Screen” means a mathematically interpretable modular
GB or an exact modular point; “proof” means a characteristic-zero certificate
or a rigorous characteristic-zero nonemptiness lift.

| rank | instrument | first-week cash cost | useful/decisive probability | hard stop |
|---:|---|---:|---:|---|
| 1 | **C: symbolic band/unit elimination** | <$100 pilot; $500-$1,000 escalation | valid compression 80-90%; screen decision 25-45%; proof 15-30% | symbolic equivalence gate fails, >1M terms, or <3x telemetry gain |
| 2 | **B: bounded alternate-engine bakeoff** | $100-$500 plus any license | main-prime screen 20-35%; proof follow-through 10-20% | cannot reproduce `a3`, or <3x speed and >1/2 raw RSS at same frontier |
| 3 | **F\': Q2/J intersection + one Row-24 probe** | <$100 before GB; $300-$1,500 after a good reduction | useful locus reduction 35-50%; full residue-A kill 2-8% | wrong-variable/gauge map, or D25 repeats +conditions=+tails |
| 4 | **D: chamber v3, only after C** | $160-$360 calibration; $1,000-$2,500 run | one more chamber 30-50%; all six 5-15% | best chamber reaches 1 TB/24 h without degree or pair-queue convergence |
| 5 | **A: raw bigger iron** | $3,341-$3,931 for the minimum useful 72 h | screen 10-25%; proof 5-12% | no quota, no telemetry, or next matrix exceeds safe 6 TB runway |
| 6 | **E: more short primes / lifting now** | $100-$800 | any short-cap verdict <10%; 10x lucky prime 1-5% | already met: three prime trajectories are clones and no trace exists |

The recommended **G\*** bundle--C, a small B bakeoff, F' in parallel, then
one gated 6 TB run--has an estimated first-week cost of $1,500-$3,500, a
**30-50%** chance of a full modular screen decision, and a **15-30%** chance
of a proof-tier decision. The original G (raw 24-hour main plus generic
algebraization) ranks below D and only slightly above raw A because neither
half reaches its decisive frontier.

## B. Which second GB engine is worth trying?

No engine changes the degree of regularity by magic. The point of a bakeoff
is to find a materially better matrix representation or pair strategy before
renting memory.

1. **GamBa first.** It is a single-threaded Monte-Carlo F4 binary for primes
   below `2^31`, including the banked primes. Single-threading is not a
   handicap against a phase in which `msolve -t 24` used roughly one core.
   Its published speed claims are self-reported, so require an A/B test. Run
   two hours/160 GiB on compressed `a0`; only a favorable result earns a
   six-hour/512 GiB main pilot. See [GamBa](https://github.com/gblanco92/gamba).
2. **Magma V2.29 second, if licensed for the cloud host.** It has a mature,
   optimized finite-field F4 implementation with sparse/dense selection and
   parallel linear algebra. It is the best proprietary cross-check, but is
   not installed locally and license entitlement is unknown. See the
   [Magma F4 handbook](https://magma.maths.usyd.edu.au/magma/handbook/text/1313).
3. **Groebner.jl third.** Parts derive from msolve, so this is not maximally
   independent, but its public `groebner_learn`/`groebner_apply` trace is the
   best follow-on once one prime finishes. See the
   [Groebner.jl interface](https://sumiya11.github.io/Groebner.jl/examples/).
4. **Maple/FGb fourth.** `method=fgb` is compiled Monte-Carlo F4 for rational
   and `p<2^31` coefficients and supports two-block orders. Expect a possible
   constant factor, not a new asymptotic regime. Maple is not installed; the
   license must be obtained. See [Maple's algorithm table](https://de.maplesoft.com/support/help/maple/view.aspx?path=Groebner%2FBasis_algorithms).
5. **Singular `slimgb`** is a useful memory-shape diagnostic, especially over
   Q/function fields, but is unlikely to beat optimized finite-field F4 here.
   **Macaulay2** exposes useful degree/strategy controls but its linear-algebra
   GB path is experimental; **OpenF4** is an integration project, not a likely
   drop-in win. Do not spend a day porting either before the first four tests.

Also test `msolve -q 1` and probabilistic `-l 44` on the compressed chart,
not on the raw monolith. Any probabilistic `[1]` must be reproduced with the
default exact path and an independent parser. `msolve` itself documents that
only several components are threaded and that `-e` supplies one two-block
elimination order; see its [official repository](https://github.com/algebraic-solving/msolve).

## D. Chamber map v3

The chamber theorem remains useful, but v3 should be a consumer of C, not a
replacement for it. Static input proxies did not predict the observed
behavior: `a0/a1/a2/b1`, spanning roughly 12k-68k terms, all crossed 120 GiB
in under two hours, while `a3` was instant and `b2/b3` hit wall caps.

Use a 30-90 minute `-v 2` calibration to record working degree, symbolic
matrix rows/columns, density, pair queue, wall and RSS. Predict the next
matrix, then set a dynamic fence at about 1.3 times that estimate. Prioritize
progress per GiB; adjacency to the dead `a3` chamber makes `a2`, then `a1`,
better first tests than raw file size alone. Closing residue-A by chambers
still requires all six open chamber classes (and every non-isomorphic E
factor), not one attractive leaf.

## E. Modular and lifting

Do not launch more primes at shorter caps. The three banked primes had almost
identical 15-hour RSS and all timed out at 48 hours; short lanes repeat the
same deterministic support preprocessing and never reach the late frontier.

Trace reuse becomes valuable **after** one learning prime completes. Then:

- for `[1]`, retain a change matrix/Nullstellensatz representation, replay its
  support at further primes, CRT/rational-reconstruct it, and verify the
  characteristic-zero identity independently;
- for `GB != [1]`, extract and raw-row-verify a finite-field point. A smooth
  point with the correct saturation guards can be Hensel-lifted to a p-adic
  point, which rigorously proves the characteristic-zero ideal is proper.

One anomalously easy prime by itself is only screening evidence, and may be
easy precisely because it is exceptional.

## F. Theory-first, narrowed

The theory lane should not be “park compute and try algebraization” in the
abstract.

1. **Q2 `l12` intersection first.** The origin chart is the banked
   characteristic-zero-empty `l13` stratum; the three nonzero charts already
   exist as leaves 11/12/13. Build a guarded common-variable map to J/nolog,
   verify gauge and B-place normalization, and apply exact relaxation/rank
   screens before any GB. Emptying all three charts kills the `l12` quotient
   stratum, not residue-A globally; a forcing theorem or a lower-stratum
   intersection cover is still required.
2. **One D25/Row-24 probe.** D23 added ten independent conditions and ten new
   highs, while making the high block quadratic. Row 24 is worth one bounded
   run because it is the recorded h2/b2 resonance. Continue only if it creates
   a tail-independent defect, adds more independent conditions than absorbing
   tails, or makes the pinned monomial relaxation inconsistent. Otherwise park
   rows 25-41. Estimated useful-relation probability is 20-30%; full kill
   3-5%.
3. **Algebraization last.** The promoted 16,443-by-5,461 Hermite-Pade matrix is
   full rank at two primes only for fixed arbitrary completions, which are not
   points of the D21/J locus. A uniform version needs an as-yet undefined
   depth-5,481 saturated joint locus, roughly 16,354 tail variables, and
   degree-up-to-126 matrix entries. Sample full rank is Zariski-open and can
   never exclude the existential closed rank-drop locus. Revisit only after C
   or Q2 gives a low-dimensional parametrized component, or after proving
   finite determinacy/recurrence for the post-window tails.

The algebraization kill criterion is a characteristic-zero saturated
unit-ideal/maximal-minor certificate, or a tail-independent forbidden
orbit-norm coefficient. Another full-rank sample does not count.

## Single concrete action today

**Build the exact pinned band-elimination emitter and run the guarded
`p105337` `a0` A/B pilot on Box02.** Its deliverable is the 32-condition
compatibility system, not another GB timeout.

Before giving it more than two fleet hours, require: the fixed 16-pivot
identity, all 32 pure residual labels, all-four-sign/claim-4 replay,
untouched-row back-substitution, `ctl0` and `a3` controls, and an emission
below one million terms. Then compare 30-90 minutes of `-v 2` telemetry
against the raw hard-pin `a0`. A 3x improvement unlocks GamBa/Magma and the
6 TB quota; failure redirects immediately to the Q2/J map and Row-24 probe.

In parallel, file the High Memory quota request. Do not launch a raw main,
more primes, or another generic algebraization sample today.
