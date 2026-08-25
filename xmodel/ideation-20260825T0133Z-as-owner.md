# Blind whole-portfolio ideation — AS owner, 2026-08-25 01:33Z

Status: **INDEPENDENT STRATEGY NOTE; NOT MATHEMATICAL EVIDENCE.**

## Blind contract and inputs

I formed this note before reading any other agent's post-trigger ideation
submission.  I reread all 46 rows of `APPROACHES.md`, their current gaps, the
current-day `PROGRESS.md`/live ledger, and the newest producer evidence for
TD6 two-center coverage, the selected-Q8 infinity passport, Q8 Galois
primitivity/global quotient custody, the terminal-classification erratum,
and the corrected AS Q9 gate.  Their SHA-256s at intake were respectively

```text
APPROACHES                                      8dc7654a036128bb...
PROGRESS                                        6b38184970acde79...
TD6 two-center report                          2ada2d70fbdb9db2...
Q8 infinity-contact report                     89691023f2703eba...
Q8 primitivity report                          9f37fc3fc7933b91...
Q8 global-quotient custody                     64d01a190ddd729f...
terminal Belyi erratum                         0221a683fc88dae...
AS Q9 producer                                 6fb2ce4bcea7ab3....
```

I did not read a sibling `20260825T0133Z` (or later) ideation file.  The
three cards below are proposed experiments, not promoted deductions.

## Portfolio judgment

The near-term proof race should remain led by maximum twelve, with TD6 as an
orthogonal finite-family proof lane.  AS is producing unusually clean exact
carry geometry and should continue, but its current payoff is a bounded
characteristic-three seed obstruction, not a characteristic-zero
counterexample or a global no-lift theorem.  The maximum-partial-degree-eleven
theorem creates a new high-variance global bridge target: land every minimal
counterexample in a source direction of actual partial degree at most eleven.

The most useful common abstraction across maximum twelve and TD6 is not
another large coefficient elimination.  It is a **one-point-at-infinity
divisor test**.  A polynomial source trajectory extends from `A1` to `P1`;
on the normalization of its coefficient component, every pole of every
required coefficient function must pull back to the sole source point at
infinity.  Surjectivity therefore kills any candidate component whose
required pole/boundary support contains two distinct target points.  The Q8
multi-contact argument is the first instance of this general test.

## Ranked card 1 — Q8 normalization, genus, and pole-support dichotomy

**Connection.** Combine avenues 7, 25, 26, and 28 with the exact Q8
primitivity reducer.  Primitivity leaves only one component through all eight
Q8 contacts or eight conjugate singleton components.  The first alternative
is already conditionally killed by the one-source-point argument.  In the
singleton alternative, any nonconstant rational source path forces the
component normalization to have genus zero (Lüroth/Riemann--Hurwitz).  If it
is rational, polynomial Taylor reconstruction further forces the union of
poles of all 23 charged coefficient functions to be supported at at most one
point of that normalization.

**Exact discriminator.** For one selected branch over
`K=Q[v]/(Q8)`, compute the normalized component function field, its genus,
and the reduced union of pole divisors of the quotient coordinates and all
true-center Taylor coefficients.  Outcomes are fail-closed:

1. genus positive: no nonconstant `P1` trajectory;
2. genus zero but at least two required pole points: no polynomial
   trajectory by surjectivity;
3. genus zero and at most one pole point: freeze an explicit rational
   parametrization and feed it to the terminal/Davenport--Zannier equations.

The registered `e_pass=2` noncube terminal control must survive the terminal
subsystem; it need not survive the coefficient component.

**First experiment.** On AWS, use the frozen global quotient equations and
Q8 branch prime to discover normalization/genus/pole support at two good
primes.  Promote nothing modular.  Reconstruct the smallest exact
characteristic-zero certificate: a rational parametrization, a canonical
differential showing positive genus, or two exact distinct pole primes.  A
root-free norm/resultant of the pole divisor should avoid eight duplicate
number-field calculations.

**Falsifier.** A rational singleton component with exactly one required pole
point is a genuine survivor, not a failure; it becomes the smallest exact
Taylor/terminal trajectory core.

## Ranked card 2 — TD6 compatibility class as a projective cokernel section

**Connection.** The exact empty sections `(C,1,1)` and now `(C,1,U)` suggest
that the repeated unit `-k/50` is the value of one compatibility class in the
cokernel of the first-band row module, rather than a coincidence of sampled
charts.  This joins the TD6 boundary-tree lane to Fitting/Rees/projective
methods (avenues 2, 28, and 31) without pretending that the present
two-center slice is the full TD6 moduli space.

**Exact discriminator.** First produce a source-licensed list of every
remaining center, dead-stretch, and boundary modulus and every genuine
scaling/gauge weight.  Only then form the original-row module `M` and
compatibility vector `b` over that parameter ring.  Compute augmented Fitting
ideals chartwise.  Seek polynomial left syzygies whose pairings with `b` are
`(-k/50)` times explicit chart factors; factor-zero loci are recursively
rebuilt from raw transport, exactly as the successful `U,H,B,T,P` cover did.

**First experiment.** Test whether the known generic and B-local witnesses
are restrictions of one homogeneous/unimodular cokernel functional after
clearing their verified denominators.  If yes, compile a weighted-projective
atlas and attack the first boundary divisor `c2=0` on AWS with original-row
certificates.  If no licensed scaling sends general data to `c2=1`, stop the
projective inference and retain the theorem as a two-center section only.

**Falsifier.** Freeze the first rank-jump component on which
`rank[M|b]=rank M`, with an explicit compatible representative.  Do not bury
it under a generic-open certificate or claim a neighbourhood kill.

## Ranked card 3 — directional-width landing into the maximum-eleven theorem

**Connection.** The campaign now has a reviewed theorem for every Keller pair
whose maximum actual partial `y`-degree is at most eleven, but no global
landing theorem.  Define for a source direction `ell` the directional width

```text
w_ell(P)=max_d (d-ord_ell(P_d)),
```

where `P_d` is the degree-`d` homogeneous part; after aligning `ell` with the
source axis this is exactly the surviving partial degree contributed by that
layer.  The global target is not the implausible statement for arbitrary
polynomials, but the minimal-counterexample statement

```text
min_ell max(w_ell(P),w_ell(Q)) <= 11                 (∗)
```

after all licensed affine/target normalizations.  This packages the missing
landing problem into a concrete common-root-multiplicity invariant connecting
avenues 1, 2, 3, 5, and 38 to the maximum-eleven theorem.

**First experiment.** Build a provenance-bearing width calculator and run it
on (i) high-degree polynomial automorphism controls, (ii) every currently
materialized GGV corner family through degree 150, and (iii) TD6/max12
normalized leading layers.  Record which exact boundary datum controls the
minimum width.  If `(∗)` is false even for a source-licensed hypothetical
book, identify the weakest additional minimality/dicritical hypothesis that
fails rather than tuning the bound after the fact.

**Falsifier.** One valid normalized Keller-compatible book with certified
minimum width above eleven kills `(∗)` as a landing theorem.  Mere Newton
prevariety points or unproven GGV-to-Sigray transport do not count either way.

## AS successor and software accelerators

The Q9 gate leaves affine fibres of dimensions 16, 17, and 19; enumerating
its `8.1e12` relevant completions is the wrong degree-eight algorithm.  Derive
the full integer `G8` row first, then restrict it to each canonical Q9 affine
fibre.  It should become a vector-valued polynomial of degree at most two in
the free coordinates.  Compute its polar matrices, common radical,
Hamiltonian directions, and cap-boundary directions; quotient only directions
proved invisible to every degree-eight row.  Canonical finite-field quadratic
forms can collapse thousands of predecessor states to a small set of exact
normal forms.  Any dependence on an omitted digit or representative is an
immediate type failure, not a cue to enumerate more.

Three campaign-wide software changes would increase speed and safety:

1. **Proof-carrying state records.** Every accepted digit state should store
   its canonical integer representative, divided-carry residues, source-row
   hashes, and the exact list of spectator directions.  Generate later rows
   only from that record.  This directly prevents the recent omitted-
   Frobenius and divided-linear-carry failures.
2. **Cost-balanced sharding.** Partition by a cheap exact predecessor-count
   prefix, not equal structural-base intervals.  In the Q9 run, shard zero
   took `3:51.69` while the other 26 took `11.77--16.71` seconds.  A prefix
   cost scan plus deterministic cumulative partition would recover nearly
   all parallel speed while preserving an ordered Merkle certificate.
3. **Reusable normalization/pole-divisor compiler.** Given a one-dimensional
   coefficient component and required rational functions, output genus,
   normalized pole primes, and a one-point-at-infinity certificate or the
   smallest survivor.  This serves maximum twelve immediately and can serve
   TD6/projective escape and the correctly typed asymptotic-variety lane.

## Allocation recommendation

Keep reviews nonblocking.  Allocate the next proof capacity approximately
`45%` to Q8 normalization/pole support, `30%` to TD6 projective cokernel
coverage, `15%` to the directional-width landing falsifier, and `10%` to
source derivation of AS degree eight.  Once an AS `G8` normal-form compiler is
typed, AWS can absorb its census without taking a reasoning slot.  Do not
reopen refuted implication ladders, generic sparse rectangles, real Pinchuk
deformations, or untyped depth expansion.

No item in this note proves or disproves JC2.
