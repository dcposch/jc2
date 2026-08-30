# Coordinator integration: exact K00 ramification calendar, without a recurrence claim

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`  
Lifecycle: **BINDING INTEGRATION / DIFFERENT-MODEL-CONFIRMED CALENDAR ONLY**

## 0. Evidence and custody

This integration binds the conservative intersection of

```text
9a94cd3bc58c04331b430f66d6fbabaa41ccee1eebcb4f18315e514fc0850c65
  xmodel/k00-ramified-em-calendar-finite-type-gate-sol56-20260830.md
7accef5786e5c161d356aec4260df3a8eb47d451e766f9c2bfafc0f9112fe0a4
  xmodel/k00-ramified-em-calendar-meta-replay-sol56-20260830.py
46f86f6b76d176e17b8d5da970597140c629ba4981f489f27ef8985e80c32539
  xmodel/k00-ramified-em-calendar-finite-type-gate-hostile-review-opus5-20260830.md
```

The Opus verdict is `CONFIRM_WITH_CORRECTIONS`.  It independently rebuilt
the 569-tail source, sparse rows, graph substitution, complete Pareto
antichains, exact-graph degrees, ratio walls, and 3,812-byte certificate.
Every displayed calendar formula survived.  This integration removes the
producer's ambiguous no-finite-quotient wording, corrects the state labels
and successor ranking, and makes the tangentiality condition explicit.

Custody is clean.  The receipt's original and post-run prompt hashes match;
the original and post-run adapter, validator, fallacy appendix, and composed
model-prompt hashes also match pairwise.  The human-readable prompt and the
composed model prompt are different files and are not expected to share one
hash.

## 1. Exact raw source calendar

On the frozen V20R2 generic K00 source, put

```text
Lambda=tau^e,       e>=2,       ord_tau(d)=m>=1,       C6=1.
```

Let the boundary orders be `h10,hJ>=0` (or infinity) and
`h6,h2,hmu2,hmu4,hmu6>=1` (or infinity).  The seven rows are exactly

```text
Phi_l = R_l(d)
      + tau^(2e)  k10 A10_l(d)
      + tau^(6e)  k6  A6_l(d)
      + tau^(10e) k2  A2_l(d)
      - targets_l,
```

with targets on rows 2,4,6,7 at shifts `14e,16e,18e,19e`.  The exact
minimum `d`-degrees by row are

```text
R:    2,2,2,2,2,3,2
A10:  2,2,2,2,2,2,2
A6:   1,1,1,2,1,2,1
A2:   1,1,1,1,1,1,1.
```

The corresponding raw first-possible arrivals are therefore

```text
R:       2m (rows 1,2,3,4,5,7), 3m (row 6)
K10:     2e+h10+2m
K6:      6e+h6+m, or 6e+h6+2m on rows 4,6
K2:      10e+h2+m
mu2/4/6: 14e+hmu2, 16e+hmu4, 18e+hmu6
Jdet:    19e+hJ.
```

These are source arrival floors, never claims that a coefficient survives
earlier equations or is attained on a branch.

## 2. Exact graph-normal calendar

In the global polynomial coordinates `d=D(S,T)+N`, with

```text
D(S,T)=(2S+S^2,(1+S)T/8,S+16T^2,T,S,2T),
```

the producer's complete tangential/normal Pareto-antichain table is exact.
In particular, on the exact graph the surface degrees are

```text
A10: 3,3,3,infinity,3,4,3
A6:  2,2,2,infinity,2,3,2
A2:  1,1,1,infinity,1,2,1.
```

On a branch already known to be tangential to the graph, with
`ord(S,T)=m` and `ord(N)=n>m`, the first possible main-row and row-six K10
grades are

```text
2e+h10+min(2n,m+n,3m),
2e+h10+min(2n,2m+n,4m).
```

The antichain table itself is a polynomial identity and is unconditional;
these branch-arrival formulas require the stated tangentiality.  The
grade-`2m` quadratic cone is larger than the tangent plane, so tangentiality
may not be inferred from the calendar.

The exact ratio walls and congruences in the producer are confirmed.  They
give a finite semilinear calendar for a fixed load-order vector, not a finite
classification of transition functors.

## 3. What the no-go evidence actually says

The evidence proves only the following negative statements:

1. a recurrence keyed on the fresh cone and its rank alone is false;
2. a calendar keyed on the reduced ratio `m/e` alone is false;
3. a DVR uniformizer change preserves `(e,m)`;
4. ramified base change and taking deck invariants reach only coefficient-
   sparse subfunctors and do not cover the full target cell;
5. graph recentering retains later surface/normal jets; and
6. `J^5 subset I subset J^2` supplies a growing valuation window, not a
   recurrence.

No lower bound on the number of transition types is proved, and no argument
rules out a richer finite stratification using `(e,m,n)`, retained jets, and
load orders.  The producer string `NO_FINITE_TRANSITION_QUOTIENT_THEOREM`
must be read only as “no such theorem was established by the tested
operations,” never as an impossibility theorem.

The replay contains one real graph mutation and several provenance/literal
checks advertised under the same mutation banner.  The reviewer supplied an
independent five-constant mutation battery; the calendar is not promoted on
the strength of the ambiguous banner.

## 4. Corrected scheduling consequences

Four exact unit-ray cells are separately different-model confirmed and bound
by `k00-ram-e2m2-e3m2-coordinator-integration-sol56-20260830.md`:

```text
(e,m)=(2,1) through G7,
      (3,1) through G9,
      (2,2) through G10,
      (3,2) through G12.
```

Their terminal grades happen to equal `2e+3m`; this four-cell observation is
not an induction or recurrence.

The cheapest unopened K10-boundary cleanup is `(2,1),h10=1`, reopening at
G8, followed by `(3,1),h10=1` at G10.  Every finite `h10>=1` and the
`h10=infinity` face remain distinct until a literal transition theorem joins
them.  The already-open `(2,2),h10=1` child reaches G11 but is not the
cheapest boundary face globally; its retention must include the mixed
surface-normal derivative block and `k10[2]` wherever their grades permit.

The cheapest untouched **unit-ray** cell is `(e,m)=(4,1)` through G11.  It is
the cleanest next test of whether a richer state-complete transition pattern
exists.  At G13, `(2,3)` and `(5,1)` tie by the calendar; `(2,3)` has extra
source-completeness value because it is the next transverse-order residue of
the `m=2` result.

None of these statements supplies an arc, compatible all-order point,
source-completeness theorem, actual polynomial map, counterexample, or JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6073`.
- Body SHA-256:
  `12d91699f33ea345664388f0c8739ea918fe1d8451ca30746bee4530feef8252`.
- Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`.
