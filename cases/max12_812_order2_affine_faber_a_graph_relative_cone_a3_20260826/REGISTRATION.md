# Registration: graph-relative `v(a)=3` direct-unit cone

Date: 2026-08-26

Status: preregistered support analysis; no source or fan theorem.

## Question

On the fixed delayed normal-15 schedule, impose the exact leading affine
load graph and give its transverse coordinates strictly positive excess:

```text
v(a)=3, v(lambda)=15, v(K10)=42,
v(d6),v(d2),v(dm)>42, v(d4)>=48,
v(X),v(Y)>=q, v(R0),v(R1),v(S0),v(S1)>=2q.
```

Does the frozen graph-relative support prove that
`-E*M^3*lambda^3/16` is the unique initial term of `K=E*H3+H5` for
every `q>=6`?  This is the first routed center face below the older
`v(a)>=5` cone.

## Exact controls

- rehash the exact-Q and `F_65521` graph-relative stdout;
- require 365 terms and byte-identical exponent sequences;
- require the intrinsic exponent and coefficient sentinel in exact Q;
- enumerate every weight-45 competitor at `q=6`;
- accept equality only when it contains at least one of `d6,d2,dm`, whose
  excess valuation is strictly positive;
- reject any nonintrinsic term of base weight below 45, any nondeviation
  tie, or any central `K10` graph term at or below weight 45;
- compute the exact rational threshold rather than sampling `q`.

The result concerns the normalized functional support only.  It cannot be
consumed as a source theorem until the predecessor equations force the
leading affine graph and all lower-`q` faces are covered.

Run only on AWS; exact Q is evidence and the prime lane is a software
control.
