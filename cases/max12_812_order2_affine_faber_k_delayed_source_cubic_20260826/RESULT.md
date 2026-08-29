# Result: integral-`t` repeated-root `K` source cubic

Date: 2026-08-26

Status: **DUAL-AWS EXACT THEOREM FOR THE INTEGRAL `Q[[t]]` CELL.  THE
FULL RAMIFIED `Q[[sigma]]` COMPLETION IS NOT CLASSIFIED.**

The exact-Q producer and characteristic-65521 software control both report
`PASS_K_SOURCE_CUBIC`.  The prime lane is a software control only.

Let

```text
Q0=z^2*(z^2+p),                         p*x != 0,
N1=p*x*z*(z^2+p).
```

This is the repeated-root survivor of the reviewed first-normal condition
`Q0 | N1^2`: in the normalized `K` coordinates it is exactly `y=p*x`.
In the integral `t` cell the client retains

```text
Q=Q0+t*(pp*z^2+x*z+rr)+...,
N=t*N1+t^2*(w3*z^3+w2*z^2+w1*z+w0)+...,
```

and sets the delayed loads to zero because they are unavailable at this
source grade.  All seven complete ordinary-Faber rows vanish below `t^2`.
Their `t^2` coefficients also vanish.  At `t^3`, among the emitted rows,

```text
R1=(-3/8)*x^3*p^2+(3/4)*w0*x*p,
R2=(-3/8)*rr*x^2*p^2,
R3=(-5/32)*x^3*p^3+(3/16)*w0*x*p^2,
```

and the exact correction-independent combination is

```text
[t^3](R3-(p(t)/4)*R1)=-(1/16)*x^3*p^3.             (1)
```

Here coefficient extraction expands `p(t)=p+t*pp`, so (1) is implemented
as `R3_3-(p/4)R1_3-(pp/4)R1_2`.  It is independent of
`w0,w1,w2,w3,pp,rr`.  Thus the integral `Q[[t]]` repeated-root cell is
empty on `D(p*x)` before any delayed load can enter.

On the squarefree part of `D(D)`, the reviewed first-normal UFD theorem is
stronger and valuation-independent: it forces the leading normal to zero,
hence `x=y=0`, incompatible with the projective `K` face.

The repeated root is the discriminant coordinate locus `b=0,e=p!=0`.
It is outside the reviewed nonsquare discriminant K3 theorem's open
`D(b*m)`; equation (1) is a new earlier mixed-chart certificate, not an
application of that theorem.

Scope firewall: on the unit-`J` ramification
`Lambda=sigma^3,t=sigma^5`, a general source arc may have normal and
tangent corrections at intermediate `sigma` orders 6 through 14.  This
client retains only integral powers of `t`, so it does not prove that those
intermediate corrections reduce to the displayed `t^2` compatibility.
The full repeated-root completion requires a correction-complete
`sigma`-adic recursion through `sigma^15`.  No total fan, terminal/Taylor,
order-two, or JC2 verdict is asserted.
