# TD6 fixed-A3 q2-beta whole-`H=0` composition theorem (V71)

Status: **exact composition of four hostile-reviewed source packages.**

The normalized TD6 compatibility system has no solution on the entire raw
center divisor

```text
H=C-3U^2=0
```

inside the fixed source-typed A3 section `(c1,c2,c3)=(C,V,U)` with
`q_beta(t)=t+beta*t^2+t^25`, for every beta.  The exact reviewed cover is

```text
V64   H=0, D(U V P3 QH),
V62D  H=V=0, D(U),
V65   H=P3=0, D(U),
V65   H=QH=0, D(U),
V70   U=0,
```

where

```text
P3=V^4-32V^2U^3+128U^6,
QH=V^4+8V^2U^3-64U^6.
```

Indeed, a putative point on `H=0` either has `U=0`, where reviewed V70
applies, or lies in `D(U)`.  On `D(U)`, a zero among `V,P3,QH` is covered by
V62D or one of the two V65 theorems; if none vanishes, V64 applies.  This is
an exhaustive Boolean split and uses no specialization through a localized
echelon.  Each leaf is independently source-replayed and unit-certified.

The V65 check also gives the normalized identity

```text
((5T-136)(T^2+8T-64)-(5T+64)(T^2-32T+128))/512=1,
T=V^2/U^3,
```

so its P3 and QH leaves are disjoint on `D(U)`; disjointness is a consistency
check, not needed for exhaustiveness.

Dependencies and reviews are hash-pinned in
`cases/td6_c1_c2_c3_q2_h_complete_cover_v71_20260825/`.  Its verifier is a
lightweight custody and set-cover audit, not a new algebraic replay.

Exact scope: whole `H=0` only in the fixed normalized A3 q2-beta section.
This does not cover `H!=0`, vary any other source modulus, prove whole A3 or
TD6, prove SP-2/landing, or resolve JC2.
