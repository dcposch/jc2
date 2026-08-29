# Direct exact sparse D43 source route: preflight

**Status:** `GO_SMALL_QUADRATIC_SOURCE_REBUILD`, with a hard boundary:
this report does **not** exhibit an exact characteristic-zero D43 point.
It also does not identify the banked normal-form presentation with the
pristine source scheme, and it proves or disproves nothing about JC2.

**Scope:** residue A, `B=84`, fibre `a00pp`, `PIN42`, and the x-side
coordinates `Xf_alpha=Xg_beta=0`.

The companion fail-closed checker is
`cases/d43_exact_sparse_source_preflight.py`, with tests in
`cases/test_d43_exact_sparse_source_preflight.py`.

## Verdict in one paragraph

There is a credible faster route that bypasses formal smoothness and all 509
normal-form traces: rebuild the 184 selected Euler rows directly over the
exact source coefficient algebra, specialize to the common sparse support,
solve the resulting small exact nonlinear J system, and replay all 184 source
rows.  Such a solve gives only a point of the relaxed finite J scheme until
the separate template equations are bridged mechanically.  The route is not
an affine-linear solve.  The published 89- and
101-variable slices are already nonlinear in the banked modular presentation;
on the common 22-coordinate support that presentation collapses to 29 live
quadratic rows.  The exact D21 bank proves source-first that the lower band is
affine over the radical/W ring; its two registered modular specializations
have rank four in ten lower variables, so the data do not by themselves
select the exact lift of the banked D25 normal-form origin.  The missing
decisive artifact is an exact source-only emission of all 184 rows on the
proposed support.

## 1. What is actually exact already?

The committed `directionb_tails_D21.pkl` is symbolic `R_ext` source data, not
data reconstructed from residues.  After the literal `a00pp` collapse
`HW_i=h W_i`, and after setting every lower coordinate outside the proposed
support to zero, its row-20 block has:

| object | exact count |
|---|---:|
| selected eta rows | 10 |
| lower tail variables | 10 |
| tail monomials, including constants | 109 |
| coefficient W-monomials | 119 |
| maximum degree in lower tail variables | 1 |

The ten variables are

```text
x4  = tf1_47    x7  = tf1_52
x12 = tf2_47    x15 = tf2_52
x20 = tg1_47    x23 = tg1_52
x28 = tg2_47    x31 = tg2_52
x36 = tg01_52   x41 = tg02_52.
```

Every retained coefficient collapses mechanically to a polynomial in `W1,W2`
whose coefficients lie in

```text
K0 = Q(zeta_42, r3, A1, A2, h),     [K0:Q] <= 12*2*3*3*2 = 432.
```

Specializing these exact source formulas at both registered root frames and
the two banked modular points gives ten zero residuals at each prime.  At both
primes the 10-by-10 coefficient matrix and its augmentation have rank four.
This is a direct source-row replay; it does not use a reduced D25/D43
normal-form coefficient.  It certifies an exact symbolic rank of at least
four, but not an exact rank upper bound on the characteristic-zero E5
quotient.

Consequently the answer to “can lower coordinates be generated source-first
without CRT?” is qualified:

* **Yes for a source-side partial parameterization.**  The exact affine block
  is in hand, so a four-by-four minor that survives the registered
  specializations can express four pivot coordinates in terms of the other
  six coordinates and W.  The remaining rows may impose compatibility
  equations; the exact rank on the E5 quotient is not yet certified.
* **Not yet for the uniquely banked `a00pp` normal-form section.**  Rank four
  at each modular residue leaves six local directions in this block.  The
  modular D25 reconstruction chooses a section, but the D21 source rows alone
  do not canonically recover its exact characteristic-zero lift.  Claiming the
  exact banked-origin coordinates still requires either an exact D25/source
  section or solving the source rows jointly.

The W coordinates are not elements of the rank-432 algebra as currently
encoded: `R_ext` deliberately treats them as free polynomial coordinates.
Their E5 quartic relations must be supplied from the exact source/template
construction and checked mechanically.  One may then work over
`K=K0(W1,W2)`, with `[K:K0] <= 16`, or retain the two quartic equations during
elimination.  Reconstructing W quartics or roots from their two modular values
would be an unjustified CRT shortcut.

## 2. Sparse support and the affine-linearity question

The two floor-passing modular full points have the same 22-coordinate support:

```text
tf1_57 tf1_62 tf1_67 tf1_72
tf2_57 tf2_62 tf2_67 tf2_72
tg01_62 tg02_62 tg1_57 tg2_57
x12 x15 x20 x23 x28 x31 x36 x4 x41 x7
```

All other graph coordinates, including both x-side coordinates, vanish.  The
support agrees at `p=105337` and `p=105673`.

This support was tested against `d43_full_pointbank_p*.pkl`.  Those files are
an **internal, unreviewed, modulo-p banked evaluated graph-row presentation**;
their coefficients passed through the reduced D25 normal-form checkpoints.
They are therefore useful shape evidence, not the missing exact source
emission.

| specialization of the 184 banked rows | live rows | terms | max degree | nonlinear rows |
|---|---:|---:|---:|---:|
| published 101-variable slice | 175 | 83,557 | 6 | 151 |
| published 89-variable/67-zero set applied to all 184 rows | 156 | 4,541 | 3 | 102 |
| common 22-coordinate support | 29 | 1,003 | 2 | 18 |

The counts are identical at both primes.  Thus neither the 89-variable nor the
101-variable slice makes the 184-row banked system affine.  The 89-variable
artifact itself contains only the 89 late rows, and its decoded graph witness
fails the source floor (`s9_d43_residual_184_zero` and `s9_nu_ge_43`).  It is
not a source point and must not seed the exact route.

On the 22-coordinate support, the 29 live banked rows occur only in three
bands:

| band | rows | new variables | rank after earlier witness bands are substituted |
|---:|---:|---:|---:|
| 20 | 10 | 10 | 4 |
| 30 | 9 | 8 | 4 |
| 40 | 10 | 4 | 4 |

Each block is affine in its *new* variables after the earlier variables are
specialized.  This does not make the global system affine: left-kernel
compatibility conditions on earlier variables are quadratic.  A linear
reduced Groebner basis at a modular isolated point is an output of nonlinear
elimination, not evidence that the input equations were linear.

For the pristine exact source rows the honest answer is still **not emitted,
therefore not certified**.  The exact rebuild must first emit all 184 rows
after the zero specialization and prove which rows vanish identically.  It may
only then replace “184” by the 29-row count predicted by the modular bank.

## 3. Smallest decisive exact artifact

The smallest useful next producer should do only the following:

1. Construct the pure-y source jets over `K0[W1,W2]` with
   `Xf_alpha=Xg_beta=0`, retaining only the common 22 graph coordinates and
   setting their complement literally to zero.
2. Add the inhomogeneous `+42` source target at row 20.  Do not add relation
   E, `HM`, `s1F`, E5, or E6 to this row-emission object.
3. Emit all 184 canonical `(eta,slot)` source rows, with exact-zero rows kept in
   the audit manifest rather than silently omitted.
4. Check exact polynomial degree/support.  If the source emission confirms the
   predicted sparse core, solve it by an exact quadratic Groebner basis or by
   three band-compatibility eliminations.  Add `Wi*uWi-1` if the UU chart is
   claimed.  The result at this stage is a point only of the relaxed finite
   184-row J scheme.
5. For promotion to the intended template-conform locus, mechanically impose
   the two individual exact E5 W quartics with their correct `HM`
   normalization, the relevant E6 transport/cube tie, the required unit and
   nonzero `HM/s1F` conditions, or a proved elimination-equivalent system.
   The reduced relation E is a compatibility consequence on the intended E5
   locus; it is not a substitute for the two E5 equations.
6. Replay all 184 pristine source equations exactly at every candidate.
7. Specialize the exact answer to both registered primes and compare with the
   floor-passing modular points as a regression gate, not as a reconstruction
   method.

The evaluator is smaller and logically cleaner than importing the 32 parked
rows, the compressed solve-back blocks, or any of the 509 normal-form traces.
Those objects are irrelevant to direct finite D43 source existence.  They are
still required if one later claims equivalence with the banked normal-form
component.

The modular 22-coordinate shape is tiny, but exact coefficient arithmetic is
not: adjoining both W fourth roots can raise the Q-vector-space degree from
432 to at most 6,912.  A support-specialized source emitter should still be a
seconds-to-minutes task; an exact Groebner solve is plausibly minutes to hours,
not something this preflight certifies.  It should run on AWS with memory/time
limits and checkpointed output, not as an unbounded local job.

## 4. Faster exact row production by partitioning `jrows`

The live box01 build is reported to have completed all seven orbit checkpoints
(about 515 MB total).  Its multi-day silent phase is the two full `jmul` calls
inside `directionb_strike.jrows`, not orbit construction.  Waiting for the
monolithic Cartesian products is unnecessary because each requested output
component is separable:

```text
R[n,s] = sum_(na+nb=n, sa+sb=s) A[na,sa] * Gamma_eta[nb,sb]
       - sum_(na+nb=n, sa+sb=s) Phi_eta[na,sa] * B[nb,sb].
```

A partitioned producer is therefore a sound acceleration.  The first launch
should use 19 disjoint band shards, one for each even slot 6 through 42.  Their
target counts are

```text
6:9, 8:10, 10:9, 12:9, 14:10, 16:10, 18:9, 20:10, 22:10, 24:9,
26:10, 28:10, 30:9, 32:10, 34:10, 36:10, 38:10, 40:10, 42:10.
```

The worker should not call the current unfiltered `jmul`.  For each assigned
target `(n,s)`, it should index one transformed jet and look up only the exact
complement `(n-na,s-sa)` in the other jet, accumulating `vmul` results for that
target.  If a band shard exceeds its memory cap, it can be split further into
individual eta components without changing the merge contract.

Each shard manifest should fail closed on:

* schema version, `D=43`, `VDEG_CAP=43`, registry hash, and the canonical
  184-target registry hash;
* SHA-256 of the final cumulative f/g orbit checkpoint inputs and hashes of
  `r1_experiment.py`, `directionb_strike.py`, and the partitioned producer;
* the exact disjoint target list assigned to the shard;
* absence of the high-degree sentinel in every output expression;
* a canonical semantic digest per `(eta,slot)`, formed from sorted tail
  monomials and sorted normalized `R_ext` terms, rather than trusting pickle
  insertion order.

The merge should assert identical input/registry/code hashes, disjointness,
and exact coverage of all 184 targets; verify every per-target semantic digest;
write `byk[slot][eta]` atomically; and record a global semantic digest.  It
should then replay the exact D21 prefix, specialize at both registered primes,
and compare all available rows with the committed modular evaluator.  `PIN42`
must be an explicit consumer gate.  The row-42 x-side sidecar is absent by
design here because alpha and beta are frozen to zero.

If both the monolithic and partitioned builders finish, equality of their
global semantic digests is an additional independent regression.  The running
monolithic job should not be interrupted or modified.

## 5. Alpha/beta and `P4P1` caveats

The two floor-passing modular full points have
`Xf_alpha=Xg_beta=0`.  At row 42 the x-side correction is

```text
42 * S_M * G_M * (3*alpha - 2*beta) * P4P1[a].
```

It therefore vanishes identically on the scoped exact route, and no `P4P1`
sidecar is needed for value evaluation.  This does not license deleting the
two tangent directions from a general smoothness calculation.

If nonzero alpha or beta is allowed, the present pure-y `source_rows` value
evaluator is insufficient.  The exact x-side value formula and the ten-entry
`P4P1` table must be appended, while alpha and beta remain independent
coordinates even though row-42 values depend on `3*alpha-2*beta`.  The current
pure-y bank also carries the named `CONJECTURE X-SIDE-30` caveat; this report
does not upgrade that statement.

## 6. Claim boundary

The row producer itself establishes only exact emission.  A solution of the
184 emitted J rows (plus any claimed chart-unit equations) would be an exact
point of the **relaxed finite D43 J scheme**.  It is a point of the intended
template-conform source locus only after the E5/E6/unit bridge described above
has been imposed or proved elimination-equivalent.  None of these finite
claims would, by itself, be:

* a proof that the banked NF presentation is the same scheme or component;
* an all-depth compatible point or inverse limit;
* a convergent/algebraic global Keller pair;
* a JC2 counterexample.

## Reproduction

```text
python3 cases/d43_exact_sparse_source_preflight.py
python3 -m unittest cases/test_d43_exact_sparse_source_preflight.py
python3 -m py_compile cases/d43_exact_sparse_source_preflight.py \
    cases/test_d43_exact_sparse_source_preflight.py
```

Observed locally on 2026-08-28: preflight `PASS`; five tests passed in under
one second.  No AWS job was launched and no heavy local computation was run
for this report.
