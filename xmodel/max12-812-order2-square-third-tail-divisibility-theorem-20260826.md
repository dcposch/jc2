# `(8,12)` order two: square-component third-tail divisibility

Date: 2026-08-26

Status: **EXACT PRODUCER THEOREM FOR THE DISPLAYED THIRD TAIL; SOURCE-BYTE
REPLAY AND HOSTILE REVIEW PENDING.  NECESSARY GATE ONLY.**

## 0. Charged scope

The reviewed first-normal support theorem leaves an arbitrary-load square
component.  This note analyzes the next nonpolynomial coefficient in the
one-parameter family.  It does not assume that the square equations hold
globally along a source arc, and it retains the transverse square-chart
variables.

Put

```text
L=z^2+s,       R=a*z+b,       M=alpha*z+beta,       S=u*z+v,

K=L^2+Lambda*R,
N=L*M+Lambda*S.                                      (0.1)
```

Then, for the charged family `f=K^2+Lambda*N`, define

```text
T=2*L*R+M,
B=R^2+S.                                             (0.2)
```

Direct expansion gives

```text
f=L^4+Lambda*L*T+Lambda^2*B.                         (0.3)
```

## 1. Exact third negative tail

Using

```text
(1+X)^(3/2)=1+(3/2)X+(3/8)X^2-(1/16)X^3+O(X^4),
```

the coefficient of `Lambda^3` in the negative `z`-tail of `f^(3/2)` is

```text
[
  (3/4)*T*B/L-(1/16)*T^3/L^3
]_-
= [T*(12*B*L^2-T^2)/(16*L^3)]_-.                   (1.1)
```

The charged `k10` summand is `Lambda^2*k10*f^(5/4)`.  Its possible
`Lambda^3` cross term is

```text
(5/4)*k10*L^2*T,
```

which is polynomial and contributes no negative tail.  The `k6`, `k2`, and
terminal target loads begin later.  Thus (1.1) is the complete third
negative-tail obstruction at this grade.

The preceding negative-tail coefficient vanishes on the square first-normal
component: `N^2/K=M^2` and `K^(5/2)=L^5` are polynomial at the boundary.
Consequently the unitriangular change between the first seven Laurent
coefficients and the frozen ordinary tail coordinates has no lower-grade
inhomogeneous term to mix into (1.1).

## 2. Divisibility consequence

The denominator in (1.1) is the monic degree-six polynomial `L^3`.  If the
first seven negative coefficients vanish, its proper fraction is zero;
equivalently

```text
L^3 divides T*(12*B*L^2-T^2).                        (2.1)
```

Reducing (2.1) modulo `L` gives

```text
L divides M^3.                                       (2.2)
```

Therefore:

1. on the generic square chart `s!=0`, the quadratic `L=z^2+s` is
   squarefree.  Since `deg M<=1`, (2.2) forces

   ```text
   M=0,       i.e. alpha=beta=0;                     (2.3)
   ```

2. on the rank-drop chart `s=0`, (2.2) forces only

   ```text
   beta=0,                                             (2.4)
   ```

   and the direction `M=alpha*z` is not removed by this argument.

This split is exact over every characteristic-zero field.  The divisor
argument uses only squarefreeness of `z^2+s` on `D(s)`.

## 3. Source and lifting firewall

Equations (2.3)--(2.4) classify a necessary third-tail condition in the
square chart.  A genuine source arc can leave the reduced square component
through transverse corrections; hence one may not replace the complete
source family globally by `K=L^2,N=LM`.  The next receiver on `D(s)` must
set the leading `M` to zero while retaining `R,S,k10`, their permitted
corrections, all finite loads, and the terminal `[6,2]` and two Taylor
families at their exact valuations.  The `s=0,beta=0` chart is separate.

This note does not prove sufficiency of (2.1), construct or exclude a
strict arc, solve either square chart, impose terminal/Taylor data, close
order two, close `(8,12)`, prove maximum twelve, or prove JC2.
