# Preregistration: V26R1 chart-free W=0 descendant

Date: 2026-08-27

Status: **FROZEN BEFORE DESCENDANT TARGET ALGEBRA.**

## Dependency and purpose

This descendant preserves the corrected V26 scaffold frozen by
`SOURCE_FREEZE_SCAFFOLD.sha256` (SHA-256
`24ee5ddaebf911387423d077cc2acf07589ae4fb79df16f856d21283e3dee306`).
It is triggered provisionally by the unpromoted V24R6R1 exact producer and
its additive exact replay:

```text
W = A1*Q1 + A3*Q3 + A4*Q4  in Q[x0,...,x5].
```

Until the independent V24R6R1 hostile review passes, every V26R1 artifact
must say `PROVISIONAL_DEPENDENCY_V24R6R1_UNREVIEWED`; it may guide work but
may not be promoted.  V24R2 and V24R5 remain independent live cross-checks
and are not stopped or silently replaced.

The objective is the representation-independent Lambda-grade-seven
compatibility locus on the only surviving complement of `D(W)`, retaining
all rank-drop branches and never defining a stratum by one chosen minor.

## Exact structural reduction

The V26 six-variable base

```text
B = (Q1,...,Q6,F10)
```

and the full prior ideal `P6` both contain `Q1,Q3,Q4`.  Therefore the frozen
identity makes `W=0` redundant modulo both `B` and `P6`.  The producer must
replay coefficientwise

```text
W - A1*Q1 - A3*Q3 - A4*Q4 = 0
```

from serialized bytes in a fresh exact process, and separately replay that
the normal forms of `W` modulo tracked bases of `B` and `P6` are zero.  A
drop and an add mutation in `A1` must make the polynomial identity nonzero.
This proves that the `W=0` descendant is the whole prior base; it does not
permit dropping any Fitting ideal or rank stratum.

## First gate: six-variable rank classification

Reconstruct `A` only from the frozen V20R2 DAG through the corrected V26
compiler.  Replay all `6 x 6` minors of `A` as zero.  In
`Q[d0_1,...,d5_1]`, decide exactly

```text
Jpre = B + I5(A).
```

- If `Jpre=(1)`, serialize and freshly replay a coefficientwise Bezout
  certificate.  Then rank `A` is exactly five at every geometric point of
  `B`, and ranks zero through four stop.
- If `Jpre` is proper, serialize a tracked standard basis/transform, replay
  it in a fresh exact process, require `NF(1)=1` and an exact nonnegative
  dimension, and retain every rank zero through four branch.

Normal-form telemetry without a serialized tracked identity is not an
endpoint.  Unit/proper forced controls, certificate/transform drop and add
mutations, and a mutation deleting one nonzero `I5(A)` generator are
mandatory.

## Full chart-free Fitting strata

Let `E=[A|-b]`.  For every rank `r=0,...,5`, preserve the closed ideal

```text
Jr = P6 + I_(r+1)(A) + I_(r+1)(E).
```

Cover `D(I_r(A))` by every distinct nonzero exact `r x r` minor `m` of `A`.
Each exact chart is

```text
Jr + (z*k10_0*m-1).
```

No V23 witness or substitute minor defines the rank-five locus.  Deduplicate
only byte-identical exact minors while retaining all source row/column
labels.  If the prepass proves rank five everywhere, only the rank-five
charts may launch; otherwise all ranks remain eligible.  A rank stratum is
empty only after every chart has a freshly replayed exact unit certificate.
A proper chart requires a tracked basis/transform, exact nonnegative
dimension, fresh replay, and mutations.  Atlas aggregation is a separate
reviewed step and may not infer an uncomputed chart.

## Required source and controls

1. rebuild all grade-seven rows, `A`, `b`, `E`, `P6`, and determinant DAGs
   from V20R2; V23/V24 are comparison controls only;
2. preserve restriction-before-extraction, including the `k6_0` restoration
   negative control;
3. keep `Jdet` distinct from `J1/J2` and absent at this grade;
4. compare all exact `A` minors and distinguished augmented minors to the
   corrected V26 scaffold;
5. replay the R6R1 `W` syzygy and its mutations before releasing any worker;
6. retain the complete Fitting/rank-drop ideal on `W=0`; deleting a rank or
   replacing `I_r(A)` by `W` must be caught by a manifest mutation;
7. run heavy determinant/Groebner work only on registered AWS lanes, one
   core each, with hard time/RSS caps, zero-swap telemetry, immutable source,
   and fresh output directories.

## Allowed outcomes and firewall

```text
PASS_V26R1_W0_DESCENDANT_COMPILED_NO_STRATUM_DECISION
PASS_V26R1_EXACT_PREPASS_RANK5_EVERYWHERE_PROVISIONAL
PASS_V26R1_EXACT_PREPASS_LOWER_RANK_LOCUS_SURVIVES_PROVISIONAL
PASS_V26R1_EXACT_GRADE7_ATLAS_EMPTY_PROVISIONAL
PASS_V26R1_EXACT_GRADE7_SURVIVING_RANK_STRATA_PROVISIONAL
RESOURCE_CAP_NO_VERDICT
DEPENDENCY_OR_SOURCE_OR_REPLAY_FAILURE
```

Even after review, this descendant decides at most pointwise solvability of
the normalized valuation-one, `C6=1`, `k10_0!=0` prefix through Lambda grade
seven.  It does not decide nilpotent lifting, grades 8--19, a full jet,
formal or convergent arcs, the later honest `Jdet`-open source, K00 closure
incidence, order two, maximum twelve, JC2, or a counterexample.
