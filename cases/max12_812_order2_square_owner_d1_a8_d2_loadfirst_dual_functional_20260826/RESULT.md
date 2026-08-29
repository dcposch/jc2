# Result: D1 `a=8,d=2` load-first split

Date: 2026-08-26

Status: **TRIPLE-AWS EXACT-Q PRODUCER PASS; AWAITING HOSTILE REVIEW.**

## Exact producer theorem

After the registered square/D1 source gates, over characteristic zero on
`D(p*k0)`, the seven literal Faber equations have no point in the strict
contact tail

```text
ord(A)=8, ord(C)=10, ord(R)>=8.
```

No leading coefficient of `R` is inverted, so this is the entire closed
`ord(R)>=8` tail.  Write `k6=k60+sigma*k60_1+...`.  The proof is the
exhaustive scheme-theoretic split `D(k60) union V(k60)`.

## Load-open branch `D(k60)`

The complete independently mined source has the unique grade-27 primitive

```text
(3/4)*k60*C/L.
```

This is one grade before the row-2 target.  Its first two analytic rows are
exactly `(3/4)k60*c1` and `(3/4)k60*c0`; the literal seven-row bridge gives
the same coefficients.  On either exact-contact chart `D(c1)` or `D(c0)`,
these rows generate the unit ideal after inverting `k60`.

## Load-closed branch `V(k60)`

At grade 28, the first surviving column is exactly

```text
(3/4)*C*(A+k60_1)/L.
```

The producer reconstructs its two proper-numerator equations and the rank
determinant `Delta_C=c0^2+(p/2)c1^2`; off `Delta_C` they force the leading
linear form of `A+k60_1` to vanish.  The rank-one face is retained.

The complete source through grade 30 has six primitive columns, global pole
ceiling two, and sole pole-two primitive `(3/8)C^2/L^2` at grade 30.  On
the finite etale moving-root cover, both exact Faber functionals

```text
Psi_+ = Phi4+lambda*(Phi3+(p/4)*Phi1),
Psi_- = Phi4-lambda*(Phi3+(p/4)*Phi1)
```

annihilate every pole-one column and have terminal pair

```text
q_+=(3/8)*(c1*lambda+c0)^2,
q_-=(3/8)*(-c1*lambda+c0)^2.
```

Their ideal is the unit ideal on both exact `C` charts after inverting
`lambda` and `k0`.  This covers both rank chambers without dividing by
`Delta_C`; emptiness descends from the finite etale cover on `D(p)`.

## Complete source custody

The compiler independently enumerates the six primitives with a padded
cutoff control; derives all moving-`p`, `A,C,R`, `k10,k6,k2`, and target jet
ceilings; emits all seven literal source rows; and bridges them through
grade 30 to an independent analytic Laurent emitter.  Every sigma quotient,
moving-root coefficient, first-load/tie identity, pole-two recurrence,
dual pairing, and chart ideal passes.  The row-2 target and its jets from
grades 28 through 30 are retained; rows 1,3,4 are target-free, so the two
functionals are unaffected.

Exact Q is the characteristic-zero endpoint.  `F_65521` and `F_65519` are
independent host/software screens only.

## AWS custody and firewall

Box03 exact Q, r6d `F_65521`, and Box02 `F_65519` each return rc zero and
`PASS_D1_A8_D2_LOADFIRST_DUAL_EMPTY`, with byte-identical mathematical
stdout, empty compiler stderr, no Singular diagnostics, and zero swap.
Launch/resource custody is in `AWS_LAUNCH_METADATA.md`; every retrieved byte
is pinned by `EVIDENCE.sha256`.

This producer closes only the named `a=8,d=2,ord(R)>=8` tail after its cited
gates.  It does not cover `a=8,d=3`, whose first load grade 28 is already
row-2-target shadowed; `a=9`; equality faces; target-shadow successors;
another D1 face; `p=0`; `k0=0`; the square component; maximum twelve; or
JC2.
