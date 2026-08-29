# `(8,12)` order two: exact exceptional cubic forms and delayed-load source triage

Date: 2026-08-26

Status: **EXACT-Q AWS-EMITTED NORMALIZED FORMS PLUS HAND SOURCE-RAY
TRIAGE.  THE UNLOADED QUADRATIC NORMAL OBSTRUCTION AND TOTAL-REES MAP ARE
NOT YET CERTIFIED.**

## 1. Coordinates

Put

```text
F=Q^2+N,
Q=z^4+p*z^2+c*z+r,
N=n3*z^3+n2*z^2+n1*z+n0,
D=(p^2-4*r)/4,
u=n1-(p/2)*n3.
```

On the exceptional `A`-face `5D+2s=0`, use

```text
c=t*x,
n3=t^3*v,
n1=t^3*(u+(p/2)*v),
n2=t^2*e2,
n0=t^2*e0,
beta=15*D/8+t^2*b,
gamma=15*D^2/16+t^2*g.                            (1.1)
```

The exact ordinary Faber rows `R1,R3,R5,R7` have no terms below `t^3`.
The following are their exact `t^3` coefficients, with `J3=4[t^3]R7`.

## 2. Full emitted forms

```text
A1 = -5/32*x^3*p
     -3/4*b*x*D
     -5/16*e2*x*p
     +5/8*e0*x
     +1/2*g*x
     +25/32*u*D.

A3 =  5/128*x^3*p^2
     +5/128*x^3*D
     +3/16*b*x*D*p
     +5/64*e2*x*p^2
     -25/64*e2*x*D
     +25/32*v*D^2
     -5/32*e0*x*p
     -1/8*g*x*p
     -25/128*u*D*p.

A5 =  5/1024*x^3*p^3
     +35/512*x^3*D*p
     +3/128*b*x*D*p^2
     +5/512*e2*x*p^3
     +3/16*b*x*D^2
     +45/256*e2*x*D*p
     -25/128*v*D^2*p
     -5/256*e0*x*p^2
     -1/64*g*x*p^2
     -25/1024*u*D*p^2
     -5/32*e0*x*D
     -1/8*g*x*D
     +75/128*u*D^2.

J3 =  5/1024*x^3*p^4
     -165/1024*x^3*D*p^2
     +3/128*b*x*D*p^3
     +5/512*e2*x*p^4
     -15/128*x^3*D^2
     -9/16*b*x*D^2*p
     -95/512*e2*x*D*p^2
     -25/256*v*D^2*p^2
     -5/256*e0*x*p^3
     -1/64*g*x*p^3
     -25/1024*u*D*p^3
     -25/64*e2*x*D^2
     +25/32*v*D^3
     +15/32*e0*x*D*p
     +3/8*g*x*D*p
     -25/128*u*D^2*p.
```

These bytes are transcribed from the exact-Q AWS stdout for tag

```text
max12_812_order2_affine_faber_exceptional_p3_20260826T132135Z_q_v2.
```

The characteristic-65521 lane emitted their reductions as a software
control.  The broad `K` standard-basis endpoint was still running when this
triage note was frozen; it is not evidence for Sections 3--4.

## 3. Delayed-load source ray

In the literal one-parameter source, choose delayed source loads

```text
k10=Lambda^12*K10,
k6 =Lambda^8*K6,
k2 =Lambda^4*K2.                                  (3.1)
```

After the source substitutions
`(Lambda^2*k10,Lambda^6*k6,Lambda^10*k2)`, every loaded tail has absolute
`Lambda`-order fourteen.  The leading exact-square loaded face is therefore
the affine ordinary system: only row two has a target at order fourteen;
the row-four, row-six, and row-seven targets occur later.

For a cubic normalized `J` term to reach the row-seven target at relative
order five, the primitive ramified tie is

```text
Lambda=sigma^3,                  t=sigma^5.         (3.2)
```

But a square-normal defect first contributes to the unloaded `F12` tails
quadratically.  Thus `n2,n0~t^2` contribute at `t^4=sigma^20`, and
`n3,n1~t^3` contribute at `t^6=sigma^30`, both before the loaded face at
`Lambda^14=sigma^42`.  They cannot be retained in a source candidate unless
the complete unloaded quadratic rows prove a special null direction.

## 4. Exact no-normal cubic obstruction

Set

```text
u=v=e0=e2=0,
```

but retain both load jets `b,g`.  On `D(D*x)`, `A1=0` gives

```text
g=(5/16)*x^2*p+(3/2)*b*D.                         (4.1)
```

Substitution in `A3` cancels all `p` and `b` terms and leaves

```text
A3=(5/128)*x^3*D.                                 (4.2)
```

This is a unit on the chart.  Hence **load jets alone cannot support the
`A`-face cubic direction**.  Every normalized `A`-face `J` witness uses a
square-normal leading defect.

## 5. Immediate exact clients

The next source-ray client must precede any terminal/Taylor work:

1. Expand the unloaded `F12` ordinary rows for (1.1) through `t^6`, from the
   complete frozen tails.
2. At orders `t^4,t^5,t^6`, retain raw nonreduced ideals and determine
   whether the first seven rows force `e0=e2=u=v=0` on `D(D*x)` or leave a
   quadratic null cone.
3. Only on a null-cone survivor, add the loaded cubic forms in Section 2 and
   impose the even row-six divisibility through relative `Lambda`-order four.
4. Test `J3` only after those predecessor ideals; never saturate by `J`
   first.

If the unloaded rows force all four normal defects to zero, equations
(4.1)--(4.2) kill the `A` face on the delayed-load ray.  If a null cone
survives, it becomes the sole input to the literal total-Rees chart and
terminal/Taylor clients.

This note does not identify `t` with `Lambda`, prove total-Rees
accessibility, classify the `K` face, impose terminal `[6,2]` or either
Taylor family, or close order two, `(8,12)`, maximum twelve, or JC2.
