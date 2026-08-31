# Quartic invariant-ring pilot: `(mu,r,D)=(2,2,6)`

This is the first bounded reconnaissance cell specified in
`xmodel/block-descent-a1-quartic-cycle1-invariant-ring-quartic-gate-control-sol56-20260830.md`.
It is a pattern finder, not a degree-independent theorem and not a Keller
counterexample search outside the stated invariant subspace.

For `mu=r=2`, put

```text
A=x^2,
U=x+x^3 y,
Z=2y+x^2 y^2.
```

The invariant quotient ring is

```text
R=C[A,U,Z]/(U^2-A-A^2 Z).
```

As a `C[A,Z]`-module it has basis `{1,U}`.  The complete pullback-degree-at-
most-six vector space has basis

```text
1, A, A^2, A^3, Z, A Z, U, A U.
```

The leading pullback monomials of the even and odd module summands are
distinct, so no omitted higher standard monomial can cancel down into this
degree bound.

For a constant-Jacobian pair, the coefficient matrix of `(U,Z)` is invertible:
at `x=0`, `J(U,Z)=2`.  Target affine normalization and removal of constants
therefore put every pair in the bounded cell into the form

```text
H1 = U + a1 A + a2 A^2 + a3 A^3 + a4 A Z + a5 A U,
H2 = Z + b1 A + b2 A^2 + b3 A^3 + b4 A Z + b5 A U,
J(H1,H2)=2.
```

`generate_mu2_d6.py` expands the Jacobian in `Q[a1,...,b5,x,y]`, extracts
every `(x,y)` coefficient without factoring it, and emits an exact Singular
ideal over either `Q` or a named prime field (composite characteristics are
rejected).  `aws_mu2_d6_run.sh` is an AWS-only, source-hash- and git-basis-
pinned, memory-capped runner.  A target-Jacobian-`3` mutation must return the
unit ideal because the normalized first jet fixes the constant term at `2`.
`launch_mu2_d6_lane.sh` supplies a Linux `setsid`/`nohup` boundary so an
orchestrator exit does not cancel the remote computation.

The first result to inspect is the exact parameter ideal and its reduced
Groebner basis.  A positive-dimensional solution set is expected to contain
automorphisms.  No component is relevant to the quartic horn until an exact
field-degree calculation proves `[C(x,y):C(H1,H2)]=8`, equivalently degree
four after the cyclic quotient.  Bounded emptiness or the absence of such a
component is reconnaissance only.
