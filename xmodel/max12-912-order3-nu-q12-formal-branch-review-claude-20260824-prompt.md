# Hostile review — `Q12` non-parity formal branch

Act as a hostile different-model mathematical reviewer in
`/Users/dc/code/math/jc2`. Read in full:

- `xmodel/max12-912-order3-nu-q12-formal-branch-20260824.md`;
- every file in `cases/max12_912_order3_nu_q12_formal_branch_20260824/`;
- the frozen parity-normal `Q12` predecessor and its case; and
- the reviewed parity/Faber dependencies actually named by those packages.

Charged hashes:

```text
report    fd4db3e2125a11c05dac3c9613b8f4305942150d0e92a3200259e595c2afce62
manifest  3ced488452275f29a4645efb098c87a987e54eb3df85b9f5646da8da8bdbe099
freeze    aa17408d0f860158fdd55577315299f9d9298599f8c7d37c72cb306fbb29b83c
```

Independently reconstruct and attack:

1. the seven-row/eight-variable fibre and the involution block decomposition;
2. the exact rank-three normal and invariant minors at every `Q12` root,
   including all chart units and the loaded equation;
3. existence of the charged algebraic parity points and the claims
   `gcd(Q12,Q12')=gcd(Q12,num(R6'))=1`;
4. the simultaneous six-variable formal elimination and why equivariance and
   uniqueness really leave exactly one odd equation `t*Phi(s,t^2)=0`;
5. the Schur-complement identity `Phi(s,0)=unit*det(J_N)` and why `Q12` has a
   simple zero along the fixed loaded curve rather than merely in the ambient
   `v` coordinate;
6. the second implicit-function step and the conclusions that both branches
   are reduced, smooth, and distinct; and
7. the strict scope: a completed high-row coefficient fibre, not an
   algebraic/rational trajectory, Taylor-compatible pair, or counterexample.

Run the replay but also give an independent formal-local proof.  Attack the
possibility that the parity theorem means there is no legitimate algebraic
base point, that an eliminated equation was omitted, that the odd equation
has an extra unit or nilpotent factor, that `s` is not a local coordinate,
or that a formal branch was overpromoted to an algebraic/global component.

Write exactly
`xmodel/max12-912-order3-nu-q12-formal-branch-review-claude-20260824.md`.
Do not edit producer, case, canonical, coordination, or other review files.
End with exactly one verdict: `CONFIRMED`, `GAP`, or `REFUTED`, and identify
the smallest failing identity or hypothesis if applicable.
