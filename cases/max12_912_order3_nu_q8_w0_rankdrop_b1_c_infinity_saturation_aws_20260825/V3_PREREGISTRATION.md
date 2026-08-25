# V3 preregistration — selected Q8 coefficient-infinity source controls

V2 is immutable and remains live.  V3 adds three exact controls before the
same source-horizontal pointed coefficient-infinity calculation:

1. every `he_l` has constant declared total degree in `(C0,C1)`;
2. `C1=1,C0=c` reproduces the original pinned source row exactly; and
3. `(C0,C1)->(lambda*C0,lambda*C1)` multiplies `he_l` by
   `lambda^degree`.

Both Python dictionary equality and emitted Singular polynomial differences
are fail-closed.  Expected degrees in imposed order `(1,3,5,7,2,4)` are
`(1,2,3,3,2,2)`.

After the controls pass, V3 repeats the V2 construction: relative
homogenization before specialization, saturation by
`C1*w*x5*(x3-2*x5)`, contraction, then chart `C0=1,C1=0` and pointed landing
`v=w=u=x1=x3=x5=0` for `d4=1+v,d2=2+v+u`.

Acceptance requires rc0, empty generator stderr, all three exact control
markers once, one terminal PASS marker, and no Singular diagnostic pattern.
The chart covers coefficient infinity only with all other displayed
coordinates affine.  It does not cover their projective infinity, terminal
or Taylor conditions, trajectories, all `(9,12)`, maximum twelve, or JC2.
