# Preregistration: exact rank-jump/Fitting residual census r1

Date: 2026-08-28

## Frozen target

Continue the authorized recursive Fitting analysis only on the genuine
generic-endpoint-dead strata of the frozen 106 by 105 receiver matrix.  The
endpoint remains the homogeneous quadratic
`E=x14*x72+x1*x97`; this job does not test it and therefore cannot produce a
survivor or a component-death theorem.  It is a bounded exact census which
reduces the next Fitting problem before any maximal-minor computation.

The matrix is the exact file with SHA-256
`56f09440c924ba7c32ca15c74e585533ab79023c8dfaf17bc6abd47077132d7c`.
The exact P/factor census is taken byte-for-byte from the terminal r6 P
archive with SHA-256
`cfd2c020b204beecaca5b60ee062aed8a1fe274a399c2ebda93d0d300a00c0f4`.
The source census files inside it have SHA-256 values:

```text
a2002b0695f66ca43e42b58cc253c4de27db645529c9eda2b84a33db602187e8  C8P_FACTORS.tsv
79120ec6fce795cc1ce49bde672e656e277cfef8c42a351cd18326f59f582ad2  Q1P_FACTORS.tsv
611530c6c53675fa53a2a5d5e40000205628f326f01c664f822d9e739475185c  TRIPLE_FACTORS.tsv
e1bccda07823fe3b500244f757b49857de2f1b779e9638a68f3981682e1bd6ea  P_EXACT.txt
```

The factor census is interpreted literally.  `C8P` entry 01 is the unit 1;
`Q1P` entry 01 and `TRIPLE` entry 01 are the unit 16.  These are
`EMPTY_UNIT_FACTOR`, not geometric components, and are recorded but never
entered into a quotient ring.  No content, multiplicity, or factor is
cancelled.  The genuine strata are:

```text
C8, Q1, P, C8_Q1,
C8P02,
Q1P02, Q1P03 (q2, raw multiplicity 4),
TRIPLE02, TRIPLE03 (q2, raw multiplicity 4).
```

## Exact reduction licensed

On each stratum, specialize only its named zero parameters and, where
needed, form the exact proper irreducible quotient ring by its frozen factor.
For a quotient, require an ambient exact reducer replay of the factor,
require `reduce(1,std(I)) != 0`, and record the nonempty qring defining ideal.

Then repeatedly choose the lexicographically first nonzero matrix entry in
the trailing block which is literally degree zero.  Such a pivot lies in
`Q*`.  Swap only trailing rows/columns and use exact elementary row/column
operations to isolate it.  At every step verify that its complete row and
column are zero off the pivot and that the pivot remains degree zero.  No
parameter polynomial may be inverted.  Bank the ordered rational pivots and
every exact entry of the residual matrix.  Compute only the generic rank of
that residual matrix.  The isolated block proves
`rank(M)=unit_pivots+rank(residual)` on that stratum.

This r1 job does **not** form a full Groebner basis or any next Fitting minor.
Its only strict mathematical output is an exact residual-size/rank census.
Every successful lane terminates `NO_VERDICT_FITTING_CENSUS_ONLY`; every
parse, reducer, unit/proper-ideal, invariant, rank, resource, swap, hash, or
custody failure is an adapter/resource `NO_VERDICT`, never mathematics.

## Frozen lanes and custody

```text
base_a  r6a i-02cb2b4a379ffcc64 r6i.4xlarge 16/128
        ggv_lambda0_fitting_census_base_a_r1_20260828T150500Z_r6a
base_b  r6b i-0f089e64c378f5da3 r6i.4xlarge 16/128
        ggv_lambda0_fitting_census_base_b_r1_20260828T150500Z_r6b
pair    r6c i-040b7a1c2ed72d4cc r6i.4xlarge 16/128
        ggv_lambda0_fitting_census_pair_r1_20260828T150500Z_r6c
triple  r6d i-07eeaf8ba6f0bc419 r6i.8xlarge 32/256
        ggv_lambda0_fitting_census_triple_r1_20260828T150500Z_r6d
```

Each lane has one CPU (`taskset --cpu-list 1`), a 96-GiB address-space cap,
32-GiB output cap, 7,200-second process-group cap, per-component 1,500-second
cap, zero total swap before and after every stage, exact EC2/DMI/job-tag
checks, immutable source, continuous PID/starttime custody, and final
no-orphan census.  Lanes are independent.  No HENS namespace is touched.

