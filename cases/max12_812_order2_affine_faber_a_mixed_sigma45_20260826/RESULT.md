# Result: exact complete-source mixed sigma-45 `A^-3` identity

Date: 2026-08-26

Status: **DUAL-AWS PASS.  EXACT-Q IDENTITY IN THE REGISTERED CORRECTION NORMAL FORM.**

## Exact setup

Write `s=sigma`, `A=z-a`, and use the repeated-root moving-discriminant
quartic with

```text
a=s^5*x,
e=p,
K0=A^2*(A^2+4*a*A+e).
```

The client retains the correction-complete K2 normal-form terms capable of
entering grade 45:

```text
K=K0+s^15*(R1*A+R0),
E=s^15*m*A*(A^2+4*a*A+e)+s^30*(S1*A+S0).
```

It also retains arbitrary jets of all three effective delayed loads and
the `mu2` target in every grade 42,43,44,45.  The central load values are
the repeated `A` affine-Faber point

```text
K6/K10=15*p^2/32,
K2/K10=15*p^4/256,
```

with `K10=kk` retained rather than set to one.  All seven rows are rebuilt
from the complete frozen ordinary-Faber tails.

Let `P_l` be those seven source rows, including the `mu2` target in row
two, and put `b=4*a`.  The exact moving-root analytic `A^-3` row is

```text
H3=P3-(b/2)*P2+(5*b^2/32-e/4)*P1.                 (1)
```

Formula (1) is the inverse of the frozen lower-unitriangular
Laurent-to-Faber connection through row three.

## Exact-Q outcome

Every coefficient of `H3` below sigma grade 45 is zero.  At grade 45 the
complete rows are

```text
[s^45]P1=-(3/8)*R1*m^2+(3/4)*S0*m,
[s^45]P3=-(3/32)*R1*m^2*p-(1/16)*m^3+(3/16)*S0*m*p.
```

Since `b` starts in grade five, (1) gives the correction-independent
identity

```text
[s^45]H3=-(1/16)*m^3.                              (2)
```

Thus neither arbitrary quadratic predecessor complements `R,S` nor any
load/target jet through grade 45 can cancel the cubic-normal obstruction.
On `D(m)`, this registered normal-form source chart is empty at grade 45.

The exact-Q output printed

```text
A_SIGMA45_H3_LOWER_ZERO=1
A_SIGMA45_H3_G45=-1/16*m^3
A_SIGMA45_CERT=1
A_SIGMA45_ENDPOINT=PASS_COMPLETE_SOURCE_H3_MINUS_M3_OVER_16
```

The characteristic-65521 lane independently printed the reduction
`4095*m^3=-m^3/16` and the same fail-closed endpoint.  It is a software
control only; the characteristic-zero claim is proved by the exact-Q lane.

## AWS custody

```text
Box03 exact Q:
  max12_812_order2_affine_faber_a_mixed_sigma45_20260826T150900Z_q
r6d F65521:
  max12_812_order2_affine_faber_a_mixed_sigma45_20260826T150900Z_p65521

exact-Q stdout:
  db48465ed6aa8f898e491f7accf2eb31c33bebcd76b44c7721484b5a8742eb87
F65521 stdout:
  50c710a93c62af5461c3093324f3b6f83a88e3e00d7b740ce092cab412a1792e
both validation files:
  65e45ef104a5e322d40b4691c66003628b112f56cb20a5cad1b8d04023481ce4
```

## Scope firewall

The computation proves (2) in the displayed source normal form.  Promotion
to an exhaustive repeated-`A` theorem additionally requires the valuative
normal-form argument that earlier root-splitting/kernel faces are empty and
all tangent jets absorb into `(a,d,m)`; that argument is recorded
separately and must be hostile-reviewed.  The face `m=0` (including a
later first normal), grades 46 and above, the terminal and Taylor
conditions, other load slopes, total fan, order two, and JC2 are not
claimed.
