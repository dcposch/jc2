# TD6 reverse/deferred unit-pivot negative diagnostic (V52)

This immutable custody package records the AWS V52 replay that tested an
independent post-transport elimination order for the fixed source-typed
`(C,V,U)` center family with `q_beta=t+beta*t^2+t^25`.

V52 reverses the row schedule and always chooses the largest available
beta-independent unit pivot, deferring every row whose remaining
coefficients are beta-dependent.  The exact transport replay passes with
rank `3470/3602`, two transport events, beta-independent matrix, affine beta
RHS, and exact x/pole sections.  At the first post-transport stage, the unit
closure stops with six unresolved original rows:

```text
('X-2',7), ('X-2',5), ('X-2',3),
('X-2',2), ('X-2',1), ('X-2',0).
```

Their surviving coefficient degrees reach nine.  V52 then intentionally
raises `reverse unit-pivot cover incomplete`; AWS rc is one.  This is a clean
negative result for this **strict all-unit reverse chart**, not a Jacobian
compatibility obstruction, not a failure of the V50 forward source replay,
and not a denominator or open-cover theorem.  No beta-dependent coefficient
was inverted.

The exact successor is V54: fraction-free elimination of these same six rows
while preserving their original-row combinations and emitting every nonunit
pivot polynomial and coefficient denominator.  Each such factor remains a
charged stratum.

Replay on an AWS host with the campaign Python environment:

```sh
tar -xzf source/td6-aws-handoff-20260825-v52.tar.gz
cd td6-aws-handoff-20260825-v52
sha256sum -c SOURCE.sha256
sha256sum -c V52_SOURCE.sha256
mkdir -p artifacts
TD6_OUTPUT_DIR="$PWD/artifacts" ./run_v52.sh > v52.stdout 2> v52.stderr
test "$?" -eq 1
```

The nonzero exit is expected only together with the exact terminal traceback
and six unresolved-row diagnostics frozen here.  This package licenses no
fixed-A3, all-beta, TD6, SP-2, or JC2 conclusion.
