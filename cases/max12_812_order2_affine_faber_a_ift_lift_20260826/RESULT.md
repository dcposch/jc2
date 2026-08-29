# Result: normalized affine-Faber `A`-face formal `J` arc

Date: 2026-08-26

Status: **DUAL-AWS PRODUCER RESULT; NORMALIZED ORDINARY-FABER FORMAL ARC.
TOTAL-REES SOURCE TYPING AND HOSTILE REVIEW PENDING.**

Both exact-Q and characteristic-65521 validators report `PASS_A_IFT`.
The finite-field lane is a software control only.

Use the square-division coordinates

```text
F=Q^2+N,
Q=z^4+p*z^2+c*z+r,
N=n3*z^3+n2*z^2+n1*z+n0,
D=(p^2-4*r)/4.
```

On the `A`-face take

```text
D=1, p=0, r=-1, k10=1, beta=15/8, gamma=15/16,
c=t,
n3=t^3*v,
n2=0,
n1=t^3*u,
n0=t^2*e0.
```

The ordinary odd Faber rows `R1,R3,R5,R7` are all exactly divisible by
`t^3`.  At

```text
(t,u,v,e0)=(0,0,-1/20,0)
```

the first three divided rows vanish and

```text
4*R7/t^3=-5/32.
```

The Jacobian of `(R1,R3,R5)/t^3` in `(u,v,e0)` at that point is

```text
[ 25/32       0       5/8  ]
[   0        25/32     0   ]
[ 75/128      0      -5/32 ]
```

with determinant

```text
-3125/8192.
```

It is a characteristic-zero unit.  The formal implicit-function theorem
therefore gives unique `u(t),v(t),e0(t) in Q[[t]]` through the displayed
point for which `R1=R3=R5=0` identically.  Since `4R7/t^3` has nonzero
constant term, this normalized formal arc has generic `J=4R7 != 0`.
The even targets are defined coefficientwise by
`(mu2,mu4,mu6)=(R2,R4,R6)`.

The next nontrivial even divided jet is independently emitted as

```text
u(t) = (13/800)*t^2+O(t^4),
v(t) = -1/20+O(t^4),
e0(t)=-(21/640)*t^2+O(t^4).
```

The `t^2` coefficient of `4R7/t^3` is zero after this solve.

This is a theorem in the normalized ordinary-Faber coefficient space once
the exact-Q identities are accepted, but it is not yet a literal
total-Rees/source arc.  Here `t` is the exceptional contact uniformizer; it
cannot be identified with the source `Lambda` without a two-sided weighted
chart map and omission/torsion audit.  General contact order requires
`t=Lambda^a` or a ramified base.  Terminal `[6,2]`, both Taylor families,
order two, `(8,12)`, maximum twelve, and JC2 remain open.
