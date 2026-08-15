# Sol acceleration second opinion + lateral scan, round 1

**Date:** 2026-08-14  
**Scope:** second opinion on the live solver allocation, followed by ideas not in
`xmodel/sol-lateral.md` and not already in flight. No computation below is a
mathematical verdict unless explicitly labelled as one.

## Executive verdict

1. **Keep the sunk R2 main lanes, but stop allocating 24 threads to future
   copies.** The four long-lived `-t 24` jobs are in effectively serial phases:
   process accounting gives roughly 1.06--1.17 utilized cores per lane over
   almost 15 hours, and a live five-second sample gave one core per lane. Several
   `-t 8` leaves used all eight cores in the same sample, so this is not a broken
   OpenMP host. For new work, six-ish genuinely different `-t 8` lanes have
   higher EV than four `-t 24` lanes.
2. **The order portfolio is a good lottery ticket; the current support portfolio
   is a poor implementation of a good theorem.** Its cover is sound, but the
   three `b` leaves are the full monolith plus an inverse variable, and the
   cover has heavy within-family overlaps. Replace them with hierarchical
   first-nonzero charts.
3. **The highest-EV screen acceleration is exact preprocessing already latent in
   the banked algebra:** hard-substitute the six no-log pins, consume the unit
   `C6/C8` pivots, and materialize the high-tail compatibility module. F4 is
   currently rediscovering all three facts inside every lane.
4. **Box03 is unsafe as launched.** It has 495 GiB and no swap, while the same
   three jobs previously occupied about 975 GiB in aggregate. Fifteen minutes
   after launch they had already reached 191 GiB. It is a one-job-at-a-time box,
   and `c2.q` may not fit even alone.
5. **The broad HELD calls are mostly right.** More primes, raw homotopy, raw
   Macaulay, and SOS should remain held. Two qualifications matter: the 47
   echelon conditions are not binomial starts, and SOS is logically sound for
   complex emptiness after realification--it is held because it is enormous,
   not because it proves the wrong statement.

---

## Part 1. Acceleration list: verdicts

### (a) Order-portfolio lanes -- **AGREE, qualified**

The reverse and seeded-shuffle copies are honest variable-order variants: the
polynomial body is identical and only the header order changes. Grevlex/F4 is
order-sensitive, so two cheap tickets are rational. I would not, however, treat
the stated `10--100x` as measured on this object, and I would not fund more
blind reverse/shuffle copies ahead of the structural reductions below.

The next order portfolio should contain:

- the original high-first order as a control;
- a level-block order keeping tau pairs adjacent;
- a graph/min-fill order from the actual variable-interaction graph;
- one seeded shuffle, not several;
- one bounded algorithm variant (`-q 1` or probabilistic sparse linear algebra
  `-l 44`) as **screen-only** evidence, replicated under default exact linear
  algebra if it lands.

`msolve` itself documents that only several components--not the whole run--use
multiple threads; see the official
[multi-threading description](https://github.com/algebraic-solving/msolve#multi-threading).
That matches the live process measurements.

### (b) Support-split leaf portfolio -- **DISAGREE as emitted; AGREE with the cover theorem**

The tau involution check and the 4096-pattern cover are sound. The acceleration
claim is the problem:

- `b1/b2/b3` hard-zero no support variables. Each retains all 77 window rows and
  all 79,571 raw window terms, then adds a Rabinowitsch fence variable. It is an
  85-variable copy of the 84-variable monolith, not a reduction.
- `a1/a2/a3` all contain the same `{all 38s = 0}` open set and differ only in
  which 40-variable witnesses nonzeroness.
- The cited pre-dead chambers are mathematically real, but the broad emitted
  leaves do not subtract them; the portfolio pays for large overlaps.
- Every `_nolog` leaf still appends six pure equations instead of substituting
  the six variables out.

Use a **hierarchical first-nonzero tau-orbit cover** instead. In order:

1. `b1`: fence the `tf38` orbit representative.
2. `b2`: zero the `tf38` pair, fence `tg38`.
3. `b3`: zero the `tf38` and `tg38` pairs, fence `tg0_38`.
4. After all 38s are zero, do the same successive construction at level 40.
5. `a0`: all twelve even lows zero.

After also substituting the no-log pins, the exact input counts are:

| leaf | window rows | expanded terms | variables, including a fence where present |
|---|---:|---:|---:|
| `b1` | 76 | 67,698 | 79 |
| `b2` | 76 | 50,229 | 77 |
| `b3` | 76 | 36,042 | 75 |
| `a1` | 67 | 24,741 | 73 |
| `a2` | 67 | 19,983 | 71 |
| `a3` | 67 | 15,737 | 69 |
| `a0` | 48 | 12,079 | 66 |

This is an orbit-stratified first-nonzero cover and strictly dominates the
current broad leaves at the input level. Runtime still needs an A/B test; input
shrinkage is not a promise of proportional F4 shrinkage.

### (c) Box03 for the three stuck7 cores -- **DISAGREE with concurrency; AGREE only as a sequential isolated lane**

Live snapshot: Box03 has 495 GiB usable RAM, no swap, and all three cores were
launched concurrently at `-t 16/-t 16/-t 24` with no memory fence. On Box02 the
same jobs had reached approximately:

| job | prior RSS |
|---|---:|
| `c10.RED` | 244 GiB |
| `c1.RED` | 308 GiB |
| `c2.q` | 423 GiB |
| **sum** | **975 GiB** |

At fifteen minutes the new launch was already at 191 GiB and climbing. This is
not a marginal sizing error; arbitrary kernel OOM selection is the likely
outcome.

Recommended use: run `c10.RED` alone, then `c1.RED` alone, each with a roughly
440--450 GiB hard fence. Decompose `c2.q`, or return it to a 2 TiB host after the
residue screens drain. Its earlier 423 GiB was not a completion footprint, so
even solo placement on Box03 is unsafe.

### (d1) More primes -- **AGREE HELD**

At the same 53.7 ks age, the three R2 prime lanes were trajectory clones:
roughly 96--98 GiB RSS, about one utilized core, zero-byte output, no verdict.
An additional prime repeats almost the same symbolic preprocessing. Add a new
prime only after a transformed lane lands, to test a bad-prime anomaly or
replicate a claimed verdict.

### (d2) Homotopy continuation -- **AGREE HELD for a real run; UNHOLD only a reduced mixed-volume pilot**

The premise “47 mostly binomial-ish echelon rows” is false in the relevant
sense. On one radical/sign branch, those 47 rows have support
min/median/max `6/141/1346`, 15,918 terms total, and **zero** binomials or
trinomials. The pivots are monomial-coordinate pivots such as products of
several tail variables; Gaussian echelon in the lifted monomial space is not a
triangular solve in the original variables.

The actual nolog decider is 77 raw window rows plus five radical rows, three
saturation rows, and six pins: 91 equations in 84 variables, about 79,596
expanded terms, and total degree up to 12 after coefficient-ring expansion.
The good fact is that all 42 high tails occur linearly at D21. The bad facts are:

- `ctl0` starts at a singular, positive-dimensional point; the measured
  differential rank is only 29 in 76 tail columns;
- a generic squaring-up has a formal two-block multihomogeneous Bezout number
  of about 34.7 billion even on the zero-heavy `a0` leaf, while the actual
  rank-16 system remains positive-dimensional when compatible;
- the D23 Row 22 block already introduces quadratic old-high terms, so D21's
  affine-linear high block is a truncation advantage, not a permanent
  binomial structure.

The only justified HC pilot is downstream of exact elimination:

1. Hard-substitute the six pins and take one certified finite radical/sign
   branch of `a0`.
2. The honest remaining high system is 48 affine-linear rows in 42 highs over
   15 active base variables. At `p=105337`, exact finite-field evaluations of
   its high matrix have rank 16 on all four tested sign branches; on one valid
   branch the augmented matrix had rank 17 at ten random base points.
3. On a certified nonzero rank-16 minor chart, emit the resulting **32 chart
   compatibility polynomials in 15 base variables** by fraction-free
   elimination. Direct `msolve` on this fenced chart has priority over numerical
   tracking.
4. Only then compute a stable mixed volume for randomized 15-by-15 square
   subsystems on that chart. Track nothing if MV exceeds `10^6`, the
   compatibility emission exceeds `10^6` terms, or the support census costs
   more than 30 minutes / 16 GiB.

A point on one branch proves that modular screen branch alive after exact
back-substitution into all original rows. An empty branch is not global
emptiness without the remaining branch/rank-drop cover.

### (d3) Macaulay/Nullstellensatz -- **AGREE HELD broadly; UNHOLD a tiny targeted sidecar**

The raw degree-one Macaulay/toric closure is already consistent. At degree two,
the recorded system reaches about 6.94 million columns and 87.1 million
nonzeros on only one fixed fiber. The new conjE two-row identity is excellent
evidence for motif mining, but it comes from a 12--14-variable debug family and
does not provide a degree bound for residual-32.

Therefore:

- do not run an unrestricted `1 in I` search on the raw screen;
- revisit cofactor extraction after an authenticated EMPTY leaf, or on the
  compressed 32-in-15 compatibility ideal;
- run the bounded **fence-power** search in Part 2, idea 5. It asks for
  `z^N in I` with named `z`, tiny `N`, and a tiny row subset, which is a
  different cost class from the held Macaulay job.

### (d4) SOS -- **AGREE HELD, DISAGREE with the reason**

Complex feasibility can be realified exactly: write each complex variable as
`x+iy` and impose the real and imaginary parts of every equation. A real
Positivstellensatz/SOS infeasibility identity for that realified system would
indeed prove complex emptiness. So “real-only, wrong for C-emptiness” is not the
right objection.

The right objection is cost and lack of exploitable order structure: 84 complex
variables become roughly 168 real variables, holomorphic sparsity is damaged,
and exact PSD recovery is harder than a direct equality-ideal certificate.
Keep it held unless the 32-in-15 reduction makes a genuinely small realified
problem.

## Box02 threading answer and concrete reallocation

**Yes: `-t 24` is past the observed scaling knee for the phase consuming the
current runs.** A five-second `pidstat` sample showed each long R2 main at almost
exactly one core, with 24 LWPs present. Lifetime CPU accounting over almost 15
hours gives the same conclusion. Several `-t 8` leaf processes simultaneously
used all eight cores, proving the scheduler and OpenMP build can parallelize
when the algorithm reaches a parallel matrix step. Box02 also had about 1.3 TiB
available at the snapshot.

I would allocate as follows:

1. Preserve the three sunk `-g 2` R2 mains to their registered caps.
2. If memory is needed, the `-e 45` probe is the first main to cull: about
   286 GiB versus about 97 GiB for each emptiness main, one utilized core, and a
   less immediate verdict.
3. Keep the two existing order tickets unless a corrected emitter is ready
   immediately; do not create more blind reorderings of the uncompressed input.
4. Replace the broad `b` leaves with hard-pin hierarchical leaves. The current
   `a` leaves are at least genuine reductions, but corrected twins still
   dominate them.
5. Use `-t 8` (at most `-t 12`) for the next 4--6 structured variants. Capture
   `-v 2` output instead of discarding all progress telemetry, and distribute
   lanes across the two NUMA nodes / 64 physical cores.
6. Give one bounded slot each to `-q 1` and `-l 44` on the smallest corrected
   leaf. A probabilistic hit is only a screen; reproduce it with the default
   exact linear algebra and another prime.

There is no paired completed-run benchmark, so I would not restart the
15-hour mains merely to lower their thread flag. The recommendation applies to
new/retry work.

## Higher-EV acceleration missed by (a)/(b)

In priority order:

1. **Compile the six no-log pins.** Main: 84 to 78 variables, 77 to 76 window
   rows, 79,571 to 67,698 window terms; `Row_10[eta^28]` vanishes. The `a0`
   term reduction is about 33%. This is exact and should be the base of every
   new lane. `msolve` may internally exploit pure linear rows, so measure the
   wall gain rather than assuming it.
2. **Consume certified E-unit pivots.** `C6` has unit rank one on the six
   level-38 lows, so one 38-variable can be eliminated globally. On
   `{all 38s=0}`, `C8` is pure-linear with unit rank two, so two of the six
   40-variables can be eliminated before F4. The banked algebra already has the
   required exact inverse routine.
3. **Emit the high-tail compatibility module.** Write D21 as
   `A(low) h + b(low)=0`. Generic sampled rank of the 77-by-42 high matrix is
   19; at `p=105337`, `a0` has rank 16 across all four tested sign branches. A
   one-prime coefficientwise probe also exposes a 12-dimensional modular
   candidate nullspace. Lift and verify any such kernel exactly before
   quotienting it, then emit compatibility equations on fenced rank-minor
   charts. Cover determinant/rank-drop strata explicitly--never silently invert
   a generic minor.
4. **Only then portfolio the solver.** Structural orders and algorithm variants
   are more orthogonal than extra primes. Fitting compression has the largest
   upside; hard pins and hierarchical leaves have the least implementation
   risk.

---

## Part 2. Fresh lateral scan

Hall deficiency remains an attractive fallback, and DG4 makes its monotonicity
premise more credible. It is **not new**, however: it was idea 5 in
`xmodel/sol-lateral.md`, so I do not count it below. The new two-rung evidence
suggests trying a cheaper arithmetic meta-theorem before building the Hall
bridge.

### Rank 1. Sharp CAP-DEN compiler: a parameterized early-clash theorem

#### Pitch

Both promoted rungs have the same core shape: a pole-adjacent `X` sits above
the `1/2` barrier; every competitor is below `1/2` or separately H8-dead;
prefixes live in a bounded denominator lattice; and every divisor of the cap
refuses the X-death. Package an entry by

```text
(X multiplicity i, inherited maximal cap C, alpha lattice,
 letter congruence domain, opponent max-gap, finite H8-dead intruders)
```

and prove the clash from this signature, before enumerating routes or a book.

There is already a sharper exact arithmetic lemma hiding in the td-11 proof.
Let `alpha=a/d`, let the current cap be `c`, put

```text
g_X = (nu+1)/(i nu),
k   = den(alpha - 1 + g_X).
```

If `k | c`, then

```text
nu | lcm(c,d).
```

For `p^n || nu`, the unreduced numerator is

```text
N = i*a*nu + d*(1-(i-1)*nu).
```

If `v_p(d)<n`, its second summand has valuation exactly `v_p(d)` while
the first has valuation at least `n`; reduction therefore leaves `p^n` in
`k`, so `p^n|c`. If `v_p(d)>=n`, then `p^n|d`. Along the inherited cap lattice
`c,d|C`, this gives the route-independent conclusion `nu|C`.

Combine it with the letter law at weight `A/D`:
`gcd(A,nu)=1` and `D|(nu+1)`, hence `gcd(A*D,nu)=1`. If
`rad(C)|A*D`, every `nu>=2` is impossible. Under the exact letter domain this
removes the neutral-X case in td-7 and td-11 A/C in one line. The promoted
td-7 proof intentionally keeps a conservative `nu=2` over-approximation; its
existing exact denominator row still refuses that case. For 11-B,
`C=6,w=3` leaves only `nu=2` (and the named resonant `X=5/4`); both are already
refused by the recorded exact denominator rows.

#### Novelty relative to the board

`TOWER-TD11.md` instantiates CAP-DEN at `i=2`, uses the weaker necessary
condition `nu|c^2`, and retains a finite sweep. `TOWER-UNIFORM.md` contains the
same arithmetic in A/B/C form. There is no packet-level classifier or sharp
`nu|C` lemma. This is not the earlier Hall dual: it removes most candidate
demands before any matching graph exists.

#### First concrete test

1. Add an exact standalone gate for the sharp lemma, including the dynamic-cap
   near-miss `(C,d,c,nu)=(4,4,2,2)`; the conclusion is `nu|C`, not
   necessarily `nu|c`.
2. Replace the td-11 `nu<=300/c^2` support sweep by the divisor statement and
   replay td-7 plus 11-A/B/C, including dagger's newly added `c=3`.
3. Run each currently filed compatible packet family through the gate and group
   uncovered signatures symbolically rather than by rung. Use the single-pole
   td `<=40` census only as exploratory coverage, not as if every row were an
   equivalent multipole entry packet.
4. For each uncovered group, prove the `X-first` half: opponent gaps below the
   barrier, with finite H8 dispatch of any intruder.

#### Kill criterion

Kill the **uniform compiler** if a legal infinite packet family has an opponent
gap at least `1/2` that is not separately H8-dead, if cap primes grow without a
letter-domain exclusion, or if replaying td-7/11 requires route history not
present in the advertised signature. The sharp CAP-DEN lemma itself survives
those failures as a reusable exact reduction.

### Rank 2. Fitting/left-kernel compression of residual-32

#### Pitch

At D21 all 42 high tails occur linearly. Write the exact window as

```text
A(low) h + b(low) = 0.
```

Instead of asking F4 to eliminate `h`, compute the class of `b` in
`coker A`. On a chart where a certified rank minor is inverted, fraction-free
adjugate/Schur elimination gives compatibility conditions. Compare the
determinantal ranks of `A` and `[A|b]`; cover and saturate the determinant-zero
strata with alternate minors. A polynomial left kernel by itself is not a
global membership oracle over the unlocalized polynomial ring.

#### Novelty relative to the board

`-e 45` merely asks a generic GB engine to discover the elimination. Section
6.V evaluated the rank pointwise and recorded 32 obstructions, but never
materialized the polynomial module. This is different from the prior toric
circuit idea (relations among lifted monomials), continuation (tracking a
special fiber), and broad Macaulay search (ideal membership).

There is concrete traction: after `a0` zeros and the six no-log substitutions,
exact finite-field evaluations of the 48-by-42 high matrix have rank 16 on
all four tested h-sign branches at `p=105337`; one valid branch has augmented
rank 17 at ten generic low points. Thus each certified rank-16 chart presents
32 compatibility equations in 15 active base variables, not an 84-variable
black box. On the full leaf, five random assignments at each of all three
banked primes give rank 19. Stacking split-branch evaluations has rank only 28,
which supplies a modular candidate kernel to lift and test--not yet an exact
constant kernel.

This is the cross-part bridge from the missed acceleration above; it is counted
once here among the five lateral proposals.

#### First concrete test

1. Lift the modular high-tail candidate kernel over the exact radical algebra
   and verify every vector against untouched VExpr rows; proceed without this
   quotient if the exact kernel is smaller or zero.
2. On `a0`, fence a certified rank-16 minor and form fraction-free
   adjugate/Schur compatibility equations. Check the determinantal rank of
   `A` versus `[A|b]` and compare with direct solvability at random points.
3. Emit one certified rank chart at `p=105337`, with the minor explicitly
   fenced, and a separate rank-drop branch. Compare terms and a 10-minute
   `msolve -v 2` trace with the hard-pin raw `a0` leaf.
4. Repeat on the first hierarchical `b` chart only if `a0` compresses.

#### Kill criterion

Kill this optimization if every usable minor is dense/irreducible, the first
compatibility emission exceeds the raw hard-pin term mass (hard cap `10^6`
terms for the pilot), or the rank-drop branch is as hard as the original and
cannot be covered by a small alternate-minor set. Never infer global emptiness
from a generic-rank chart alone.

### Rank 3. Certificate-preserving forbidden minors of tower trees

#### Pitch

Turn the two promoted clash proofs into hereditary obstructions. Allow only
proved monotone contractions:

- prune a competing subtree wholly below X after full-alpha-lattice exhaustion;
- contract a co-scaled M-preserving neutral string when X is reached before its
  deep deaths;
- replace a cap by a divisor while retaining or overapproximating the inherited
  alpha/register lattice and prefix history;
- delete an H8-dead spine.

The td-7 and td-11 direct/dagger kills then become small forbidden tree minors.
If every higher multipole tree contains one, the tower theorem becomes a finite
obstruction-basis theorem rather than a rung-by-rung census.

#### Novelty relative to the board

Current certificates are cells/routes or per-entry packets. DG4 proves one
monotonicity fact--extra deep vertices only shrink caps and remove prefixes--but
there is no hereditary contraction order, forbidden-minor basis, or antichain
test. This is also distinct from Hall matching: it simplifies the primal tree
while preserving a known certificate.

#### First concrete test

1. Implement the four contractions on read-only copies of all 233 td-7 routes
   and the 145 decorated td-11 skeleton rows.
2. Require every promoted killed route to reduce to a named core.
3. Use the **67 OPEN nested td-11 rows as mandatory negative controls**: none
   may reduce until its merged-emission/NF-M hypotheses are actually present.
4. Compute the minimal antichain on the available td-13/higher skeletons and
   inspect whether its size stabilizes.

#### Kill criterion

Kill on the first false reduction of an OPEN/legal row, if an extra branch can
change alpha/window data despite the proposed premise, or if the minimal
antichain grows rung by rung with no stable finite basis. Partial sound
contractions remain useful compiler simplifications.

### Rank 4. Integrate the universal high-tail kernel as a gauge action

#### Pitch

A coefficientwise probe of the D21 77-by-42 high-tail matrix--treating every
low monomial and radical-basis coefficient independently--has rank 30 at one
fresh good prime, producing a **12-dimensional modular candidate nullspace**.
Split radical branches produce an enlarged 14-dimensional sampled candidate.
Either may shrink or disappear in characteristic zero, so no invisible
direction is asserted until it lifts and verifies exactly.

Recover the kernel exactly, map its basis to the six root series, and ask
whether it is the infinitesimal action of formal reparametrizations/root-chart
gauge. If it integrates to a free additive action with a polynomial slice,
quotient it before every residue solve and separate genuine survivor dimension
from chart freedom.

#### Novelty relative to the board

The repo records pointwise ranks and upstream scaling gauges, but no universal
kernel of the D21 high block and no integrated action on its tail variables.
This is more than a matrix optimization if the same action persists at D23 and
beyond.

#### First concrete test

1. Compute the exact Q/radical-algebra nullspace and verify every vector
   coefficientwise in all 77 banked rows.
2. Compare the basis with infinitesimal substitutions `t -> t + eps*t^r` and
   permitted changes of root-series representatives.
3. Check preservation of factorization, the six no-log pins, saturation data,
   and the D23 Row 22 block.
4. If it integrates, construct a polynomial slice and re-emit the D21 system in
   quotient coordinates; compare dimension/rank with the current residual.

#### Kill criterion

Kill immediately if the exact characteristic-zero nullspace is zero. Kill the
**structural gauge** claim if any exactly verified directions do not integrate,
violate the root-factorization rows, or are detected by Row 22. In the last
case only the exactly verified directions remain a D21 linear-algebra
optimization; they do not shortcut the formal endgame.

### Rank 5. Tau-paired fence-power certificates

#### Pitch

A fenced leaf has ideal

```text
I + <u*z - 1>.
```

To kill it, it is enough to prove `z^N in I`; multiplying by `u^N` then gives
`1`. Search for `N<=3` identities using only two to four tau-paired band rows
and multiplier degree at most three. This targets the exact nonzero witness of
the leaf instead of asking for an unrestricted Nullstellensatz certificate.

#### Novelty relative to the board

The held Macaulay lane asks for `1 in I` at unknown degree. Prior lateral idea 4
mines completed farm `[1]` outputs. This proposal is pre-verdict, leaf-local,
and targets a named fence power. The new conjE square identity and the twelve
pre-dead singleton chambers are unusually strong positive controls for exactly
this pattern.

#### First concrete test

1. Automatically rediscover the known `C6` singleton-38 and restricted `C8`
   singleton-40 certificates.
2. Canonicalize supports under tau and search subsets of size 2--4 for
   `z,z^2,z^3` membership over `p=105337` and `105673`.
3. Use a verified common zero with the target fence variable `z` nonzero as the
   negative control. If none is banked, omit the negative control rather than
   misclassifying the origin-satisfiable `a0-ctl0` system, where `z=0` would not
   refute `z^N in I`.
4. Lift any stable small support over the exact radical algebra and multiply out
   the identity independently before using it.

#### Kill criterion

Kill this bounded sidecar if it cannot recover every registered positive
control, or if no new fence-power identity appears at both primes within
`N<=3`, row-subset size `<=4`, and multiplier degree `<=3`. That negative
result says nothing about higher-degree or full certificates--which remain
held.

## Ranked action summary

| rank | action | expected value | first gate |
|---:|---|---|---|
| 1 | Sharp CAP-DEN packet compiler | highest uniform-theorem EV | exact td-7/11 replay, then packet scan |
| 2 | High-tail Fitting compression | highest residue-screen EV | hard-pin `a0`, emit/guard 32-in-15 |
| 3 | Forbidden tower-tree minors | high uniform upside, medium risk | 233 + 145 rows; 67 OPEN negatives |
| 4 | Universal high-tail gauge | medium-high residue upside | lift modular kernel + D23 test |
| 5 | Tau fence-power certificates | cheap bounded sidecar | rediscover singleton controls |

My order for the next compute/theory cycle is therefore:

```text
urgent Box03 correction
  -> hard pins + hierarchical leaves at t8
  -> a0 fenced rank-chart compatibility emission
  -> sharp CAP-DEN gate and packet scan
  -> only then more GB order/algorithm tickets
```

The Hall dual remains the fallback if the packet classifier fragments; generic
homotopy, raw Macaulay, extra primes, and SOS remain held.
