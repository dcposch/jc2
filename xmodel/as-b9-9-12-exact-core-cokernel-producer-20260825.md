# Producer report: normalized B9 exact rational/SNF core

Date: 2026-08-25  
Status: **PROVISIONAL PRODUCER; DIFFERENT-MODEL REVIEW PENDING**

## Exact object

For the displayed normalized B9 parent, write the all-row determinant
equation after the outer factor `243` is removed as

```text
E(T) = b + A*T + 243*J(T).
```

Here `A` has 276 source rows and 146 columns, with SHA-256
`c073c6e6aec5a0d19f2296ff218f02d269c5bc6c54b129915ef54f2c22bd49ae`;
`b` has SHA-256
`da68b06f556f6b261f657822945eab64ee7fe131964133a07824d67605edf773`.
Both are regenerated from parent source SHA-256
`fb4f16d808dfba754582fb1b5fe10dfa0e69bca0888b38f92586e1f5534724e2`.

## Exact rational and Smith data

FLINT gives

```text
rank_Q(A)       = 142
dim ker_Q(A)    = 4
dim ker_Q(A^T)  = 134
rank_Q([A|-b])  = 143.
```

Thus the linear equation `A*T=-b` is rationally inconsistent.  Primitive
integer bases of the two rational kernels are emitted at SHA-256
`9d1e26f24492c380530bbf29f072fc85d23a1ef1cfc5ad24c432fd8d8aad37f3`
and checked exactly against every matrix entry.

The complete nonzero Smith diagonal is in the machine result.  Its 3-adic
valuation histogram is

```text
v3 : count
 0 : 85
 1 : 30
 2 : 12
 3 :  2
 5 :  2
 6 :  2
 8 :  3
10 :  1
12 :  2
13 :  1
17 :  1
18 :  1
```

The cumulative counts below valuations 1 through 5 are exactly
`85,115,127,129,129`, explaining the displayed mod-3 linear-window ranks.
The exact rational rank 142 therefore corrects, rather than contradicts, the
earlier heuristic extrapolation `129`.

## Projected nonlinear compatibility system

Let the rows of `C^T` be the emitted primitive basis of `ker_Q(A^T)`.  The
compiler expands every P-Q term of `J(T)` and stores

```text
H(T) = C^T (b + 243*J(T)).
```

The constant vector is nonzero and has content valuation 21 at 3.  There are
4556 nonzero P-Q coefficient vectors, whose rational span has rank 68.  The
coefficient content valuations range from 5 through 31 and are recorded
exactly in `result.json`.  The deterministic compressed polynomial payload
has SHA-256
`22fc1efca220a21c178b5a393f1e2cf122c1b59e826c7622a7522ceb6b31890d`;
its uncompressed canonical JSON has SHA-256
`89915399932a4c827723dd19b0de880522ee47db6e63132f9c9e82b9298a8912`.

This establishes a finite 134-row nonlinear compatibility object.  It does
**not** establish that object has no zero: cokernel projection is necessary,
and image-coordinate reconstruction remains part of any sufficiency claim.

## Custody and scope

The r6d run completed in 34.85 seconds with maximum RSS about 236 MiB.
Machine result SHA-256 is
`28d19d18578641e1dc0f0e0f996409234afa5a70b2daa1ede55153c84650f794`.
The run uses python-flint 0.9.0 and a source closure whose manifest SHA-256 is
`d4e4dfcf94aacce4fe99eff4715b451e9161773f5558d63627defc079b8481b9`.

Scope is one normalized `(9,12)` coefficient box over one fixed B9 mod-243
parent.  No common-cubic conclusion, complete earlier-fibre coverage,
all-depth point or exclusion, maximum-twelve theorem, counterexample, or JC2
claim follows.
