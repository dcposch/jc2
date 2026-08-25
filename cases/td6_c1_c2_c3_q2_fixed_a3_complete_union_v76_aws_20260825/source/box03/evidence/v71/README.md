# TD6 fixed-A3 q2-beta complete `H=0` cover (V71)

Status: **composition of four hostile-reviewed exact source packages.**

This package performs no new elimination.  It hash-pins the reviewed V64,
V62D, V65, and V70 source theorems and checks their exact set-theoretic
cover.  In the fixed source-typed normalized A3 section
`(c1,c2,c3)=(C,V,U)` with

```text
H  = C - 3 U^2,
P3 = V^4 - 32 V^2 U^3 + 128 U^6,
QH = V^4 + 8 V^2 U^3 - 64 U^6,
q_beta(t) = t + beta t^2 + t^25,
```

the reviewed leaves are:

```text
V64   H=0, D(U V P3 QH),
V62D  H=V=0, D(U),
V65   H=P3=0, D(U),
V65   H=QH=0, D(U),
V70   U=0 (hence in particular H=U=0).
```

For a point of `H=0`, first split on `U`.  If `U=0`, V70 applies.  On
`D(U)`, split successively on `V`, `P3`, and `QH`; a zero factor is covered
by V62D or V65, while all four factors nonzero are covered by V64.  Thus

```text
V(H)
 = [V(H) intersect D(U V P3 QH)]
   union [V(H,V) intersect D(U)]
   union [V(H,P3) intersect D(U)]
   union [V(H,QH) intersect D(U)]
   union V(H,U).
```

Every leaf is an original-row unit/incompatibility theorem for polynomial
beta in the same fixed source section, so the normalized compatibility
system has no solution anywhere on `H=0` in that section, for every beta.

Run `python3 verify.py` for a lightweight hash, verdict-marker, and Boolean
cover audit.  It does not rerun any producer algebra.

Scope firewall: this is not a theorem on `H!=0`, not whole A3, not another
center/boundary/dead-stretch/F1/pole modulus, not TD6, not SP-2, not a
landing theorem, and not a resolution of JC2.
