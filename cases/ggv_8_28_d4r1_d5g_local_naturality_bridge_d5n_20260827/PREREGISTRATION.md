# D5N preregistration: reviewed D4R1 to direct D5G naturality bridge

Date: 2026-08-27

## Frozen question

After the independent D4R1 hostile-review PASS, construct the smallest exact
typed bridge from its factor-local Morse outputs to D5G's authoritative raw
determinant.  The bridge must:

1. identify both sides as images of the same literal raw `F,G` rows;
2. derive the constant-channel identity without treating a local coordinate
   as a global polynomial automorphism;
3. enumerate and gate every coefficient of `D0,...,D21` before simplifying
   the weight-22 identity;
4. recover only the factor remainder from local data; and
5. retain the direct global quotient `Q22`, rejecting any target claim that
   lacks either `R22=1` or `Q22=0`.

No raw Keller specialization is to be solved in this case.

## Rings and maps

Let

```text
C = Q[the 400 named positive-weight D3 raw slots],
S = C[X,t]/(t^23),
A = C[c]/(c^8-1),
H = X^8-1.
```

D5G supplies `D=sum_(n=0)^22 D_n(X)t^n` in `S`.  D4R1 supplies
`s,U,q0,V` in `A[[t]]/(t^23)`, where `xi=c+s`, `F=U+u^2`,
`q0=u_X|_(u=0)`, and `V=G_u|_(u=0)`.  Define

```text
ev_xi : S -> A[[t]]/(t^23),
raw_slot |-> the same raw leaf,
t |-> t,
X |-> c+s(t).
```

The exact bridge identity to prove is

```text
ev_xi(D)=q0*C,
C=V*(t*U'-8*U).
```

Equivalently `C_n=sum_(i+j=n) V_i*(j-8)*U_j`.

## Lower-row gate and endpoint quotient

Every `X`-coefficient polynomial of `D0,...,D21` must be named and hashed.
Let `I_<22` be the ideal they generate in `C`.  Only after base change to
`Cbar=C/I_<22` may the bridge simplify to

```text
D22(c)=H'(c)*C22.
```

Before that base change, Taylor shifts of lower `D_n` are retained.  A
nonzero lower row or missing coefficient reference is a fail-closed stop.

## Global custody and mutations

Use D5G's exact monic division

```text
D22=H*Q22+R22,  deg_X R22<8.
```

The factor map sees `R22(c)=D22(c)` and cannot see `Q22`.  The normalized
global target is exactly

```text
R22=1 and Q22=0.
```

The mutation `D22 -> D22+H` must leave every local/factor value and `R22`
unchanged while incrementing `Q22`.  A bridge that accepts the mutated target
from local data fails.

## Maximum scope

A PASS proves a typed raw/local naturality square, an exact lower-row quotient
gate, and preservation of the global `H`-multiple.  It does not prove the
gate ideal has a point, satisfy the target, land a GGV object, exclude an
`8_28` face/family, prove `G2-PSC`, `G2-BD`, or resolve JC2.
