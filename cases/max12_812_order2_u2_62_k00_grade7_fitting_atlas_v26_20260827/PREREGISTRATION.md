# Preregistration: V26 representation-independent grade-seven Fitting atlas

Date: 2026-08-27

Status: **FROZEN DESIGN; NO ALGEBRA RUN.**

## Objective

Replace the single-minor V23/V24 grade-seven chart by the complete
representation-independent degeneracy locus, including `W=0`, while retaining
the exact V24 theorem on `D(W)` as a mandatory localization check.

This is conditional on the reviewed V20R2 literal common-source compiler and
the reviewed V22 grade-six prefix.  Execution is held until the exact-Q
V24R2 `D(k10_0*W)` gate lands.  The endpoint and certificate bytes of that
gate must be added to the source freeze before launch; a modular outcome may
not fill this dependency.

## Exact source and reconstruction

The producer must rebuild, directly from the frozen V20R2
`LITERAL_140_EQUATION_DAG.json` and `SOURCE_COLUMNS.json`, the seven literal
Lambda-grade-seven equations after applying the boundary restrictions before
any solve or saturation.  The honest newest variables are exactly

```text
y = (d0_6,d1_6,d2_6,d3_6,d4_6,d5_6,k10_3).
```

It must prove each grade-seven equation is affine linear in `y` and write

```text
A*y + b = 0,
```

where `A` is `7 x 7`.  All second derivatives with respect to the entries of
`y` must vanish.  The reconstructed `A` and `b` must compare coefficientwise
to V23 and V24, but neither earlier serialization may substitute for the
V20R2 rebuild.

The forbidden boundary variable `k6_0` is zero before extraction.  Restoring
it must produce the known nonzero grade-seven K6 column and must change the
typed system.  `Jdet` remains distinct from `J1/J2`; it first belongs to a
later honest source grade and is not silently inserted here.

## Representation-independent compatibility locus

Let `I_j(M)` denote the ideal of all `j x j` minors of a matrix `M`, with
`I_0(M)=(1)`, and set

```text
E = [ A | -b ].
```

First replay exactly that all `6 x 6` minors of `A` vanish and that some
`5 x 5` minor is nonzero, so the generic rank is exactly five.  Do not use
the single V23 witness as the definition of the rank-five locus.

For each `r=0,...,5`, define the constructible geometric-point stratum

```text
X_r = V(P_6 + I_(r+1)(A) + I_(r+1)(E))
      intersect D(k10_0) intersect D(I_r(A)),
```

where `P_6` is the complete exact prior ideal consisting of all seven literal
row coefficients through Lambda grade six together with `F10=0`, after the
registered boundary zeros.  Here `D(I_r(A))` means that at least one
`r x r` minor is nonzero.  At a geometric prior point, `X_r` is exactly the
condition

```text
rank(A)=r and rank(E)=r,
```

hence exactly the existence of a grade-seven newest-coefficient solution.
The union `X_0 union ... union X_5` is the full pointwise grade-seven
compatibility locus; it includes all of `W=0`.

For an exact emptiness decision, compute or certify

```text
H_r = (P_6 + I_(r+1)(A) + I_(r+1)(E))
      : (k10_0)^infinity : I_r(A)^infinity.
```

`H_r=(1)` is an exact empty-stratum certificate.  `H_r` proper means only
that the finite grade-seven compatible constructible stratum is nonempty
over an algebraic closure; it is not a compatible later jet or arc.

## Six-variable coefficient-base prepass

Because `A` depends only on the six leading normal coordinates
`x=(d0_1,...,d5_1)`, classify its rank first in `Q[x]` on the exact V22 base

```text
B = (Q1,...,Q6,F10).
```

Replay `I_6(A)=0` and decide `B+I_5(A)` exactly with a tracked certificate or
tracked proper basis.  If `B+I_5(A)=(1)`, then every V22 geometric point has
rank exactly five and the lower-rank branches `X_0,...,X_4` stop before the
larger prior-jet solve.  If it is proper, recursively classify the nonempty
rank strata.  This coefficient-base prepass may select work but may not
replace the full `P_6` compatibility calculation.

## Mandatory agreement with V24 on `D(W)`

Let `W` be V23's frozen `5 x 5` minor.  On `D(W)`, prove by explicit exact
minor identities that

```text
I_6(E) localized at W = (C6,C7) localized at W,
```

where `C6,C7` are V24's two Cramer contractions.  It is acceptable to emit
bounded exponents and coefficient matrices proving both inclusions after
multiplication by powers of `W`; a numerical or modular comparison is not.
At minimum, identify `C6,C7` as signed distinguished `6 x 6` augmented
minors and derive every other augmented `6 x 6` minor from them after
inverting `W`.

Then consume the exact-Q V24R2 endpoint as follows:

- if V24R2 proves the prior ideal unit on `D(k10_0*W)`, V26 must replay that
  exact certificate and mark only the `W` chart empty;
- if V24R2 proves the prior chart proper, V26 must reproduce its exact
  compatibility membership/nonmembership branch from the localized Fitting
  ideal;
- a resource cap, custody failure, or modular-only endpoint blocks V26
  execution rather than being guessed around.

## Computational representation and caps

All determinants must be built fraction-free (Bareiss or an independently
replayed exterior-power compound matrix) and stored as canonical exact DAGs
before optional expansion.  Deduplicate equal minors by exact hash.  The
producer must report term/node counts for `I_j(A)` and `I_j(E)` and may split
rank strata into independent AWS jobs after the six-variable prepass.

Heavy Groebner, saturation, primary/radical, or determinant expansion runs
only on AWS.  Every job gets an immutable source, one-core execution, hard
wall/RSS caps, zero-swap telemetry, and a fresh output directory.  Modular
multi-prime ranks/saturations are discovery only and cannot promote any
exact stratum decision.

## Mandatory controls

1. coefficientwise replay of all 140 literal DAG roots needed through grade
   seven on two exact fixtures and one modular fixture;
2. V23 matrix and V24 inhomogeneous-vector comparison;
3. exact zero replay for all `6 x 6` minors of `A` and a nonzero rank-five
   witness independent of chart choice;
4. a sign mutation in `b` that changes at least one augmented minor;
5. a row/column-order mutation caught by the `D(W)` Cramer agreement;
6. restriction-order mutation restoring `k6_0`, which must produce the
   forbidden nonzero column before any saturation;
7. toy matrices covering rank five compatible/incompatible, rank drop to
   four compatible/incompatible, rank zero, and a case where one chosen
   maximal minor vanishes while another does not;
8. forced-unit and known-proper ideal controls for every exact saturation;
9. second-process replay of every claimed Bezout, membership, or dual
   nonmembership identity.

## Allowed producer outcomes

```text
PASS_V26_FITTING_ATLAS_COMPILED_NO_STRATUM_DECISION
PASS_V26_EXACT_ALL_GRADE7_COMPATIBLE_STRATA_EMPTY
PASS_V26_EXACT_NONEMPTY_GRADE7_COMPATIBLE_STRATA_IDENTIFIED
RESOURCE_CAP_NO_VERDICT
DEPENDENCY_OR_SOURCE_OR_REPLAY_FAILURE
```

A nonempty outcome must name every surviving rank and the exact saturated
ideal/certificate; an empty outcome must replay every rank-stratum unit
certificate.  If only the compiler lands, no constructible-stratum claim is
allowed.

## Scope firewall and both-outcome meaning

V26 is normalized `C6=1`, valuation-one, `k10_0!=0`, and conditional on the
complete honest prefix through grade six plus `F10=0`.  It decides at most
pointwise solvability of the Lambda-grade-seven newest-variable equations.
It does not decide nilpotent scheme lifting, compatible grades 8--19, a full
jet, formal or convergent arc, honest `Jdet`-open reachability, K00 closure
incidence, `W=0` strata outside this prefix, order two, maximum twelve, JC2,
or a counterexample.

If every `X_r` is empty, this eliminates only this normalized finite prefix
at grade seven.  If some `X_r` survives, it supplies only the exact next
constructible stratum and its rank; later source grades and `Jdet` still have
to be imposed.  Neither outcome may be inflated into arc exclusion or
existence.
