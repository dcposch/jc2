# General-squarefree rational modes R4

This additive exact case transports the reviewed R3 rational homogeneous
classification from `H=X^8-1` to every nonconstant squarefree `H` at
`(alpha,beta,N)=(12,8,22)`.  It proves the same six-mode normal form and
excludes the exact `H^2/H^3` endpoint whenever `deg H>=2`.

The nonsquarefree follow-up stops at the exact mutation

```text
H=X^2, F=X^4, n=22, r=X^(-5),
t^22 F^(-5/4)=t^22 X^(-5),
```

which is a new charged-weight homogeneous mode.  No general `H=A^2B`, raw
provenance, or GGV-family statement is made.

Replay from repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_keller_face_general_squarefree_modes_r4_20260827/verify_r4.py
```
