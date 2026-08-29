# Registration: exact-square affine-`mu2` receiver

Date: 2026-08-26

Status: **PREREGISTERED EXPLORATORY EXACT-SUPPORT CLIENT.**

This is client `P2` from the correction-aware collision/Pell successor.  For

```text
Q=z^4+p*z^2+c*z+r,
H=sqrt(Q)*(Q^2+beta*Q+gamma),
```

let `E_l` be the coefficient of `z^-l` in `H`.  The literal simultaneous
load/target face is

```text
E1=0, E2=mu2, E3=...=E7=0.
```

The client reconstructs the seven coefficients from the frozen recurrence,
keeps `mu2` as an affine target coordinate, and computes the exact reduced
support.  It independently prints the `D(c)`, `c=0,D(p)`, and `p=c=0,D(r)`
strata.  A proposed three-component union is only a checked hypothesis:

```text
square: c=0, p^2-4*r=0, mu2=0;
Chebyshev: c=0, 16*beta=5*(p^2-4*r),
                 256*gamma=5*(p^2-4*r)^2, mu2=0;
p=0 affine target: c=p=0,
                    5*r^2+8*r*beta+16*gamma=0,
                    32*mu2=r^2*(5*r+4*beta).
```

An exact-Q lane is the theorem-producing computation.  An independent
`F_65521` lane is a software/control comparison only.  Both run on AWS with
hard memory and time caps.  The endpoint is exploratory even if the proposed
union matches: no total-Rees pullback, correction prolongation, terminal,
Taylor, order-two, maximum-twelve, or JC2 conclusion follows.

