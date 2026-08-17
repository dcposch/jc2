# Instrument round 3: what now decides residue-A?

**Date:** 2026-08-17  
**Scope:** the D21 B-frozen, no-log residue-A window on the W₁W₂ ≠ 0
chart. Modular screens remain evidence until promoted by a
characteristic-zero certificate or a verified characteristic-zero lift.

## Decision

**Do not continue any current 43-variable core file, and do not rent 6 TB
today.** The next instrument is a guarded **CORE2** emission followed by a
30-minute msolve -v 2 A/B test.

The reason is not a speculative solver preference. The delivered “true core”
still contains two large, exact presentation defects:

1. its advertised degree profile counts template variables only, whereas
   msolve sees common invertible W-powers that raise the actual input degree
   as high as **2741**; and
2. the FLINT pass stopped before **six further globally valid unit pivots**.

A read-only FLINT replay, repeated at all three banked primes, gives an
equivalent unsplit CORE2 with **27 variables, 45 equations, 6,311 terms, and
actual degree at most 10**. On every one of the 36 finite radical fibers at
p = 105337, constant row-echelon and unit normalization give the same
**22-variable, 26-equation, 5,348-term, degree-at-most-8** shape. This object
has not been run. The 12-hour/221 GB record therefore does not measure the
object we should now solve.

My ranked route is:

1. **CORE2: finish the symbolic compression and normalize the localized
   equations.** Pilot the unsplit object against one fully split fiber.
2. **CORE2 chamber cover:** only if the baseline resists, extend the old
   support hierarchy to an exact 11-class source-level cover and re-eliminate
   inside each class.
3. **Engine diversity on measured CORE2 holdouts:** Magma F4 first for a
   different optimized matrix implementation; Singular slimgb as the truly
   memory-orthogonal algorithm; FGb if already accessible.
4. **D23/D25 only as a bounded shape census, in parallel.** The proposed
   “more equations, same variables” gain is a hypothesis contradicted by the
   first reactivation audit, not a current fact.
5. **One 48-hour big-iron CORE2 holdout** only after the preceding gates.
6. **Park** if the named telemetry and shape gates fail.

msolve -e is not the first action. Once the six missed unit pivots are
consumed, the eight purported surviving highs disappear, so there is no
remaining elimination block aligned with the 32-condition structure. The
right elimination is the exact FLINT elimination already visible in the
band algebra.

Probabilities below are subjective, conditional, and strongly correlated;
they must not be added.

## 1. Forensic correction: the 43-variable run was not a degree-8 run

The emitter computes its displayed degree at
[fastelim.py:360](../cases/fastelim.py) by summing exponents only over the
template coordinates. It excludes Aᵢ, Wᵢ, and HWᵢ. Fraction-free pivoting
then leaves enormous common Laurent-unit content in the emitted rows:

| current-core rows | common factor | actual max degree | after dividing the factor |
|---|---:|---:|---:|
| 43–47 | W₁⁸W₂² | 19 | 9 |
| 48 | W₁⁷W₂² | 19 | 10 |
| 49–53 | W₁¹³⁶W₂³⁴ | 180 | 10 |
| 54–59 | W₁²¹⁸⁴W₂⁵⁴⁶ | 2741 | 11 |

These powers are visible literally in
[directionb_core_p105337.ms](../cases/directionb_core_p105337.ms). Division
does not change the chart ideal: the emitted relations uWᵢWᵢ − 1 make every
Wᵢ a unit. Algebraically, (Wᵢᵃf, uWᵢWᵢ − 1) and
(f, uWᵢWᵢ − 1) are the same ideal. This normalization should occur after
every fraction-free pivot, not merely at final printing.

All three banked primes split the remaining finite radical equations. For a
fixed r₃ embedding there are

> 3 A₁-roots × 3 A₂-roots × 2 HW₁/W₁ signs × 2 HW₂/W₂ signs = 36 fibers.

Direct census confirmed that each current-core fiber has 38 variables,
62 equations, and actual degree at most eight after unit normalization. Thus
even the 43-to-38 reduction alone would invalidate extrapolation from the old
run.

There is a stronger reduction. The current engine only searches its automatic
pivots among high variables in rows k ≥ 12
([fastelim.py:158](../cases/fastelim.py)), although the banked band ranks
already expose low unit pivots. After the banked 16 high pivots, the following
six coefficients each lattice-reduce to one nonzero radical/Laurent monomial
and hence are units on every chart factor:

~~~text
tf1_38 <- Row_6[eta^2]
tf1_40 <- Row_8[eta^0]
tf2_40 <- Row_8[eta^3]
tf1_39 <- Row_12[eta^8]
tf1_41 <- Row_14[eta^6]
tf2_41 <- Row_14[eta^9]
~~~

The replay takes about five seconds per prime and gives the identical shape at
105337, 105673, and 200257:

| object | variables | equations | terms | actual total degree | status |
|---|---:|---:|---:|---:|---|
| emitted “true core” | 43 | 67 | 21,870 | **2741** | actually run, 12 h timeout |
| same file, unit-normalized | 43 | 67 | 21,870 | 11 | not run |
| current-core finite fiber | 38 | 62 | 21,870 | 8 | not run |
| unsplit **CORE2** | **27** | **45** | **6,311** | **10** | replayed in memory, guards owed |
| finite-fiber **CORE2** | **22** | **26** | **5,348** | **8** | 36/36 identical census, guards owed |

The unsplit CORE2 has 38 window generators on only these 18 occurring
template coordinates:

~~~text
tf2_38;
tg1_{38,39,40,41}, tg2_{38,39,40,41};
tg01_{38,40}, tg02_{38,40};
uf18;
vf1_{34,36}, vf2_{34,36}.
~~~

The eight advertised leftover tg highs, uf24, and the remaining
reconstruction directions cancel or cease occurring. On each of the 36
radical fibers the 38 window generators have constant polynomial-row rank 24;
with the two W-saturation equations this gives the 22-by-26 object.

This is not yet a promoted artifact. It is strong enough to determine the
first action, but the exact equivalence and emission gates in section 7 must
run before a solver does.

## 2. Honest reading of the old F4 growth curve

The endpoint phrase “221 GB steady” is incomplete. The retained host sysstat
record for the two core lanes, which ran from about 06:04 to 18:04 UTC, shows:

| UTC | host memory used | interpretation |
|---:|---:|---|
| 09:10 | 299 GB | after the overlapping PILOT12 process exited |
| 14:50 | 702 GB | both cores growing |
| 15:20–15:50 | 804.4–804.8 GB | peak plateau |
| 16:00 | 573 GB | a large allocation/matrix was completed or freed |
| 16:10–17:50 | 573–575 GB | next long phase |
| 18:10 | 110 GB | both cores gone; persistent farm baseline |

Subtracting the roughly 110 GB farm baseline gives about
95 → 347 → 232 GB per core lane. Commit peaked near 4.68 TB, but there was
no swap or I/O wait; committed virtual memory is not resident memory. The
sharp 16:00 release is real forward progress. The final “steady” interval was
only about two hours.

That curve supports neither “convergence is near” nor “plateau forever.” A
completed F4 batch can be followed by a larger one, and no degree, selected
pair, matrix, or basis telemetry was saved. More decisively, this was progress
on rows of actual degree up to 2741. It has essentially no predictive value
for a normalized 22-variable degree-8 CORE2 fiber.

Therefore:

- never extend or restart a current directionb_core_p*.ms file;
- collect -v 2 on every new lane; and
- use the existing roughly 1 TB host to size CORE2 before buying 6 TB.

Conditional on perversely continuing the old malformed file, I would assign
only 10–25% probability of a terminal result by 48 hours and 20–35% by 96
hours. That is now the wrong experiment even if compute is free.

## 3. Ranked plan, costs, and probabilities

| rank | instrument | direct cost / effort | chance of useful terminal progress | decision |
|---:|---|---|---|---|
| 1 | **Guarded CORE2 + short plain-grevlex pilot** | 4–8 engineering hours; seconds to emit; about 1 lane-hour to calibrate | valid emitter 90–97%; modular verdict within 2 h 55–75% | **Do today** |
| 2 | **CORE2 finite fibers, then gated 11-class cover** | 18 lane-hours for a 30 min 36-fiber wave or 72 lane-hours at 2 h; chamber emission seconds-cheap | one-prime 36-fiber decision after a strong pilot 35–60%; full chamber decision after baseline failure 15–30% | Conditional go |
| 3 | **Alternate engine on an actual CORE2 holdout** | 1–3 h conversion plus license/access; 12–48 solver hours | Magma 30–50%; FGb 25–45%; slimgb 20–35%, all conditional on an msolve holdout | Conditional go |
| 4 | **D23/D25 shape census + Q2 forcing theory** | 0.5–2 engineering days; a few CPU-hours before any F4 | compact taller core meeting gate 15–25%; direct kill 3–5% | Parallel bounded lane |
| 5 | **One 48 h 6-TB CORE2 holdout** | about $2,227 on legacy U on-demand; Spot varies | 40–60% by 48 h after the promotion gate; another 20–35 points conditionally by 96 h | Last compute escalation |
| 6 | **Park** | $0 | 0 immediate | Mandatory if revisit gates fail |

“Useful terminal progress” means a complete [1], a complete proper basis or
verified point, or an exact structural reduction that passes its stated gate.
A timeout and a zero-byte output remain no result.

### First action today

Extend the FLINT emitter to consume exactly the six additional pivots above,
remove common localized unit content after every pivot, and emit:

1. the unsplit p = 105337 CORE2; and
2. one representative fully split 22-variable fiber.

After the equivalence gates pass, run both for 30 minutes with
msolve -g 2 -t 4 -v 2, alongside a freshly unit-normalized 43-variable
control if memory permits. Record working degree, selected-pair backlog,
matrix rows/columns/density, reduced rows, basis size, wall time, peak RSS, and
commit. Do not start the 36-fiber wave, a chamber wave, or big iron until this
A/B lands.

Promote a representative fiber to two hours if it terminates or improves the
same-degree matrix/RSS/time frontier by at least 3x. Fan all 36 fibers only if
the representative is at least 3x better than unsplit CORE2 and measured
aggregate RSS fits safely. One proper fiber is already a modular survival
signal; one [1] fiber is not global emptiness. All 36 fibers must be [1]
at one prime, then the whole cover must be repeated at a second prime.

## 4. Option (b): which msolve -e block targets the 32 conditions?

**After CORE2, none.** The 32-condition interpretation arose after the first
16 high pivots. The six missed pivots change the residual module: all eight
purported leftover highs disappear, as does uf24. Asking F4 to rediscover an
elimination on the 43-variable file is dominated by the exact five-second
FLINT computation.

On a fully split CORE2 fiber the only auxiliary elimination block is
{uW1,uW2}. Reordering those first and using -e 2 computes the contraction
toward the 20 physical coordinates, but it is output-oriented, not an
emptiness accelerator. The retained elimination ideal describes the closure
of the open projection; the full block-order GB still decides the original
ideal, but it will normally be harder than grevlex. Give this at most 10%
incremental decision value and run it only if a completed proper GB makes an
auxiliary-free description useful.

If the CORE2 equivalence gate unexpectedly fails, the fallback on a normalized
38-variable current-core fiber is:

- first block x17,x19,x25,x27,x32,x33,x37,x38 for -e 8; or
- those eight plus uW1,uW2 for -e 10, retaining exactly the 28 geometric
  low/seed/scale variables.

That is a contingency, not today's portfolio. The raw 84-variable -e 45
timeout says little about it, but CORE2 currently makes it obsolete.

## 5. Option (d): what the instant a3 result actually teaches

The a3 result is not evidence that a giant nonlinear F4 computation was
almost finished. It is a low-band support death. With all level-38 variables
and the tf40/tg40 pairs zero, Row 8 restricts to a rank-two linear system
on tg01_40,tg02_40. At every tested cubic-root branch modulo 105337, those
two columns are independent, so both variables vanish, contradicting the
a3 fence. This explains the instant 512-byte [1].

Two immediate theory chores follow:

1. certify the norm of this exact 2-by-2 determinant in the radical algebra,
   promoting a3 from two-prime evidence to a characteristic-zero pre-dead
   chamber; and
2. run the analogous determinant check at level 41, which predicts that the
   later d2 chamber is also linearly pre-dead.

Thus a3 supports **band-matroid preprocessing**, not the inference that all
nearby chambers are solver-easy.

If CORE2 resists, use a source-level first-nonzero cover on all ten
τ-pairs, ordered

~~~text
tf38, tg38, tg0_38,
tf40, tg40, tg0_40,
tf39, tg39,
tf41, tg41.
~~~

This gives ten first-nonzero classes plus the all-low-zero class:

| class | preceding zero blocks; representative fence | current status |
|---|---|---|
| b1 | none; tf1_38 ≠ 0 | open, likely bottleneck |
| b2 | tf38 = 0; tg1_38 ≠ 0 | open |
| b3 | tf38 = tg38 = 0; tg01_38 ≠ 0 | open |
| a1 | all 38s zero; tf1_40 ≠ 0 | open |
| a2 | plus tf40 = 0; tg1_40 ≠ 0 | open |
| a3 | plus tg40 = 0; tg01_40 ≠ 0 | two-prime empty; exact norm owed |
| c1 | all even lows zero; tf1_39 ≠ 0 | open |
| c2 | plus tf39 = 0; tg1_39 ≠ 0 | open |
| d1 | plus all 39s zero; tf1_41 ≠ 0 | open |
| d2 | plus tf41 = 0; tg1_41 ≠ 0 | predicted linear death |
| z0 | all 20 low tails zero | exact-dead by §6.V(3) |

The representative leaf and its exact τ-image form each class. Machine-check
the partition on all 2²⁰ support patterns. Do not split the six
dead-stretch/merge parameters initially: §6.V(4)'s two certified seeds show
that they genuinely move every one of the 32 labels, but supply no support-unit
lever.

Apply each chamber's zero substitutions **before** selecting the six new low
pivots. A globally valid pivot cannot be reused verbatim when its pivot
coordinate has itself been set to zero; re-echelon each chamber and emit its
own CORE2. Use a3 as the negative control, then try d2, d1, c2, and a2, but
test b1 early because it determines whether the full cover can finish. Stop
the chamber campaign if b1 reaches 128 GB or two hours without at least a 3x
same-frontier improvement over unsplit CORE2. Easy late-leaf deaths do not
compensate for an intractable cover bottleneck.

At two-hour caps the eight genuinely open representatives cost about 16
lane-hours per prime, or 32 lane-hours for two primes. A full modular empty
cover must use verdicts at the same prime; never mosaic [1] leaves from
different characteristics.

## 6. Option (e): the taller-core premise and the actual theory lane

### 6.1 Two-seed dependence

The two certified cascade seeds in §6.V(4) produce different values at all 32
residual labels. This proves that the obstruction is genuine low-data
dependence, not a fixed hidden contradiction. It neither gives a point nor an
emptiness certificate. CORE2 exploits more unit directions in this same
module; it does not turn the two samples into a theorem of existence.

### 6.2 D23/D25 counts

The phrase “more equations, same variables” is the upside case to test, not a
banked fact. Row 22 has ten components and exact first-occurrence rank 4/10,
so after its four frontier pivots it can add six compatibility equations.
Row 24 has nine components and exact rank 4/10, so it can add at most five
more for the existential problem. But D23 also makes the high block quadratic
([§8](../SHEET6-DIRECTIONB.md)); the current fastelim.py is a D21-affine
engine and cannot simply re-emit the nonlinear projection in seconds.

Use the exact normalized, fully split/echelon CORE2 as the comparison:

| object | projected shape | equation/variable ratio | improvement gate |
|---|---:|---:|---|
| D21 CORE2 | 22v / 26eq | 1.182 | baseline |
| D23 | (22+r)v / 32eq | 32/(22+r) | improves ratio only if r ≤ 5 |
| D25 | (22+r+s)v / 37eq | 37/(22+r+s) | improves ratio only if r+s ≤ 9 |
| D25 same-vars upside | 22v / 37eq | 1.682 | attractive but unproved |

Here r is the number of D21 directions reactivated by Row 22 after the full
projection, and s is the further number reactivated by Row 24. A fixed-fiber
diagnostic before the six low substitutions found 22 nonpivot candidate
directions outside CORE2 that Row 22 may reactivate, in addition to the six
low pivot coordinates themselves. Naive exact substitution already reached
4.57 million terms at the fifth of the six low pivots. This does not prove
r = 22, but it makes r ≤ 5 a low-probability condition that must be measured.

The longer-row census is also not an equation-growth argument: Rows 24–40
have 88 observed components against 90 first-occurrence variables, and the
pure-y construction stops at Row 41. No asymptotic extrapolation is a kill.

Pre-register the D23/D25 gate:

- normalize every common W-unit and split all 36 radical fibers;
- replay all 22 D21 pivots, the Row22/Row24 rank-four frontiers, +42, both
  claim-4 seeds, τ, two primes, scalar projection, and full back-substitution;
- continue to F4 only if r ≤ 5 at D23 and r+s ≤ 9 at D25;
- require actual degree at most eight and term mass near 5,348, with 2x as the
  warning/stop threshold unless -v 2 gives a compensating improvement; and
- then allow only a 30–60 minute telemetry pilot.

Estimated cost is 0.5–2 engineering days plus a few CPU-hours. The targeted
Row24 symbol takes about 25 seconds, but the full nonlinear projection is the
job. I assign 75–90% to obtaining an honest structural census, 15–25% to a
compact D25 object meeting the ratio gate, 5–15% to a terminal modular result
in a subsequent 12-hour run, and 3–5% to a direct residue-A kill.

### 6.3 Q2/l12

The l12 eta0 candidate is obsolete on the literal B-frozen bank. It was
independent of relation E but solvable at both tested primes. The later exact
quotient-row/saturation certificate proves

> V_bank ∩ Q2_l12 = ∅

before eta0 is imposed: leaf 11 is characteristic-zero empty, leaves 12 and
13 conflict with B = 0, and the origin is the banked empty l13 stratum
([sol-algkill.md:469](sol-algkill.md)). Re-running eta0 adds nothing.

The live theoretical task is now one of:

- prove a forcing theorem that every relevant B-frozen/algebraizing point
  lies in the l12 quotient tier;
- extend the common-variable elimination to the earlier l8/l4 directions; or
- rebuild the J-window with B unfrozen, where the l12 domain exclusions and
  eta0 map must be reconsidered.

This theory lane is worth running in parallel because it can produce a proof,
but its one-week direct-decision probability is lower than CORE2's.

## 7. Pre-registered gates

### G0 — CORE2 equivalence gate

No solver launch until all items pass:

1. exactly 22 sequential pivots; each of the six new coefficients is a single
   radical/Laurent monomial at all three primes and is nonzero on every tower
   factor;
2. identical 38-residual-row / 6,311-term / 18-template shape at all three
   primes;
3. every removed monomial factor is recorded, and multiplication reconstructs
   the pre-normalized row exactly;
4. independent scalar replay of every pivot, full reconstruction/back-
   substitution into all 76 source rows including the unique +42, and the six
   no-log pins;
5. parser round-trip, τ-conjugacy, pattern-positive anchor, and ctl0
   satisfiability;
6. reproduction of a3 = [1] at 105337 and 200257; and
7. on fiber emission, exhaustive 36-factor cover for the chosen r₃ embedding,
   A₁ ≠ A₂, exact τ transport to the conjugate r₃ embedding, and exact
   22-variable / 26-equation / 5,348-term / actual-degree-at-most-8 census on
   every fiber.

### G1 — short solver gate

Run unsplit CORE2 and one representative fiber for 30 minutes with -v 2.

- **Verdict:** verify it immediately and fan only what its semantics requires.
- **No verdict but at least 3x same-degree matrix/RSS/time improvement:**
  extend the winning lane to two hours.
- **No verdict and less than 3x improvement:** do not blindly fan 36 copies;
  activate the support/determinant preprocessing and engine bakeoff.

For a proper modular basis, back-substitute all 22 pivots and verify every raw
row. Seek a smooth guarded point and Hensel-lift it; a smooth Qₚ lift is
characteristic-zero nonemptiness, whereas one finite-field point by itself is
only screening evidence. For [1], require all 36 fibers at the same prime,
repeat at a second prime, then recover and independently check a
characteristic-zero Nullstellensatz/GB certificate.

### G2 — chamber gate

Require the exact 2²⁰-pattern cover, τ identities, source-level zero
substitution, per-leaf pivot replay, and the a3 control. Stop if b1 reaches
128 GB or two hours without 3x same-frontier improvement. Do not spend on a
collection of easy leaves that cannot close the bottleneck.

### G3 — alternate-engine gate

Only port a measured CORE2 holdout. Require identical
variable/equation/term/degree census, three independent random evaluations,
ctl0, and instant a3 reproduction. Promote an engine only for a terminal
result or at least 3x same-frontier time/RSS improvement.

### G4 — big-iron gate

One normalized CORE2 fiber must first:

- time out for 12 hours in msolve and resist one alternate engine;
- show completed F4 degrees/batches, not merely stable RSS; and
- either approach 700 GB resident memory or have -v 2 predict that the next
  matrix will not safely fit the existing host.

Then run one prime for 48 hours. Extend to 96 only if a degree completed in
the preceding 12 hours, selected-pair/matrix backlog fell, and RSS remains
below 70–75% of physical memory. Otherwise stop.

### G5 — taller-core gate

Use the r ≤ 5, r+s ≤ 9, degree-at-most-8, term-mass, replay, and
30–60-minute telemetry gates from section 6. Failure parks Rows 26–41; it is
not evidence that residue-A survives.

## 8. Option (c): engine diversity

Port only a normalized CORE2 fiber that actually remains hard.

1. **Magma F4 first, if a usable license is immediately available.** Its
   optimized finite-field sparse/dense machinery and monomial representation
   give meaningful implementation-level memory diversity, although it retains
   F4's Macaulay-matrix asymptotics. Use grevlex and non-dense settings. On an
   msolve CORE2 holdout, estimate 30–50% terminal probability inside 12 hours.
   See the [Magma F4 handbook](https://magma.maths.usyd.edu.au/magma/handbook/text/1313).
2. **Singular slimgb is the genuinely different memory behavior.** It is a
   Buchberger-family method designed to keep intermediate polynomials slim,
   rather than accumulating giant F4 matrices. Peak memory may be much lower,
   with a potentially much longer wall time. Estimate 20–35% inside 24–48
   hours. The local installation is Singular 4.4.1; fleet execution and a
   guarded converter are still required. See the
   [official slimgb manual](https://www.singular.uni-kl.de/Manual/latest/sing_358.htm).
3. **FGb third, unless it is already licensed/available.** It is an independent
   high-performance F4/F5 implementation and may win by a large constant, but
   its matrix-memory failure mode remains correlated with msolve/Magma.
   Estimate 25–45% inside 12–24 hours on a holdout. See the
   [official FGb page](https://www-polsys.lip6.fr/~jcf/FGb/index.html).

Do not sum these probabilities. Magma and FGb share the fundamental matrix
cliff; slimgb is the hedge, not the expected speed winner. msolve's official
interface confirms that -e is a two-block order and -v 2 exposes per-step
matrix telemetry; see the
[official msolve repository](https://github.com/algebraic-solving/msolve).

No Magma, Maple/FGb, or FGb executable is present locally. Singular is present.
That access fact makes a same-day Magma/FGb bakeoff conditional on license and
installation, not part of today's critical path.

## 9. Option (a): big iron, cost, and the 48-to-96-hour gate

A live AWS read-only check on 2026-08-17 contradicts the premise that
u-6tb1.56xlarge is a Spot lane: its supported usage class is on-demand only.
The current us-east-1 Linux price is about $46.40391/hour:

| lane | cash cost |
|---|---:|
| 48 hours | about $2,227 |
| 96 hours | about $4,455 |

Spot-capable 6-TB x8i quotes sampled roughly $4.87–$48.74/hour depending on
type and availability zone. A 48–96-hour non-checkpointed msolve run makes
interruption probability part of the effective cost; a cheap quote is not a
free decisive lane.

If G4 is met, choose the single best normalized CORE2 fiber/ordering at
p = 105337, not duplicate primes. Conditional on that strong gate, I assign
40–60% probability of termination by 48 hours. A 96-hour extension adds
roughly 20–35 percentage points only if the last-12-hour progress gate is met.
Without that gate, extra wall time is not an instrument.

The present 221 GB endpoint is not itself a reason to run long: it followed a
347 GB/lane peak and a batch release, and it came from the malformed
degree-2741 presentation. CORE2 telemetry must replace it.

## 10. Option (f): when to park and when to return

Do **not** park today: a new, much smaller, equivalent core is untested.

Park the Gröbner campaign—not the residue-A branch—when all of the following
have occurred:

1. CORE2 passes equivalence gates but neither unsplit nor representative
   fibers meet the 3x/terminal pilot gate;
2. the b1 support bottleneck fails its two-hour/128-GB chamber gate;
3. Magma/FGb or slimgb supplies neither a terminal result nor a 3x telemetry
   improvement on the same holdout; and
4. D23/D25 fails its reactivation, degree, or term-mass gate.

Revisit only on at least one named state change:

- a solver or version demonstrates at least a 3x improvement at the same
  completed degree/frontier;
- a D23/D25 normalized projection proves the r ≤ 5 or r+s ≤ 9 compact shape;
- a Q2 forcing theorem, l8/l4 intersection, or unfrozen-B map removes a
  substantial set of active directions;
- the a3/d2 determinant mechanism extends to the b1 bottleneck;
- a reusable modular trace/change matrix or characteristic-zero certificate
  becomes available; or
- checkpoint-capable compute makes a genuinely new 48–96-hour strategy
  possible.

Parking under these conditions is an instrument verdict: current Gröbner
methods have failed on the correctly presented object. It is not a
mathematical survival verdict.

## Bottom line

The choice is no longer “96 hours versus theory.” The existing campaign has
not yet run the actual small core. Finish the six missed unit pivots, remove
the invertible monomial swell, validate the 27-variable CORE2 and its
22-variable fibers, and spend the first 30 solver minutes there. If that
fails, the exact 11-class source cover and one memory-orthogonal engine are
the next discriminating instruments. D25 and 6-TB runs earn resources only
after their pre-registered gates.
