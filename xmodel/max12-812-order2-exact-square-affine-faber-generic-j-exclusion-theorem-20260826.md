# `(8,12)` order two: generic affine-Faber complete-local `J` exclusion

Date: 2026-08-26

Status: **CHARACTERISTIC-ZERO HAND THEOREM IN THE NORMALIZED ORDINARY-FABER
COEFFICIENT SPACE.  HOSTILE REVIEW AND A LITERAL TOTAL-REES CHART
IDENTIFICATION ARE PENDING.  THE TWO EXCEPTIONAL DIVISORS ARE NOT
CLASSIFIED HERE.**

## 0. Result

On the non-square exact-square affine-Faber graph, put

```text
Delta=p^2-4*r,              D=Delta/4,
s=5*D-4*beta.
```

In the completed ordinary-Faber coefficient space, the three zero-target
odd rows

```text
R1=R3=R5=0
```

force every odd coefficient deformation to vanish, scheme-theoretically,
on

```text
U = D(D*(5*D+2*s)*(5*D-2*s)).                     (0.1)
```

Consequently `R7=0` and hence `J=4*R7=0` to all orders there.  After adding
the source equation `J-4*R7`, saturation by `J` is the unit ideal in this
completed neighborhood.  Thus no `J`-nonzero formal arc can specialize to
the affine-Faber graph on `U`.

Only the disjoint divisors

```text
A-face:  5*D+2*s=0   <=> 15*Delta-32*beta=0,
K-face:  5*D-2*s=0   <=>  5*Delta-32*beta=0        (0.2)
```

remain on `D(Delta)`.  Every first-order kernel direction on either divisor
also has `dR7=0`, so any survivor there begins nonlinearly.

This theorem is stronger than a tangent-space obstruction: it is an
all-orders complete-local exclusion on (0.1).

## 1. Frozen inputs and evidence level

The corrected seven-row exact-square affine-Faber support and its dual-AWS
replay are frozen at

```text
77a3a2f0a04263eb5a476b3e4f3ec9da7db5500481ec73a483d504906e63a89e
  xmodel/max12-812-order2-exact-square-affine-mu2-faber-connection-classification-20260826.md

86d9da43b1f7823a4673ed219478b1c6ff60503eccbb2892894733979468b19c
  cases/max12_812_order2_exact_square_faber_affine_mu2_20260826/RESULT.md
8e56b7ab944e956b9d67993e54bfc8996f02b16803889ac7dfbaa59e2ee0447c
  cases/max12_812_order2_exact_square_faber_affine_mu2_20260826/EVIDENCE.sha256
a779cdeb5be36ad70c09b1497c3719b8c0659c03b48798414d90464156993970
  cases/max12_812_order2_exact_square_faber_affine_mu2_20260826/FREEZE.sha256
```

The literal one-parameter ordinary source and its independent source review
are frozen at

```text
82167b862a779d1104e3fb904d71627b799f48074241d8496fc1051d0a7afa2f
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-promotion-20260826.md
b7666bb12ef454f5047074898e0384968393916d97bd06673d3a1f20ab70f50d
  xmodel/max12-812-order2-u2-62-strict-rees-compiler-v2-source-review-20260825.md
```

The support, connection, and source inputs above are AWS/review backed.  The
Jacobian calculation and the complete-local argument below are exact hand
algebra and have not yet had an independent hostile review.  No modular
calculation is used as a characteristic-zero proof.

## 2. Exact ambient coefficient coordinates

Work over a characteristic-zero field `k`.  A centered monic octic has the
form

```text
F=z^8+a6*z^6+a5*z^5+a4*z^4+a3*z^3+a2*z^2+a1*z+a0.
```

There is a unique square-division presentation

```text
Q=z^4+p*z^2+c*z+r,
N=n3*z^3+n2*z^2+n1*z+n0,
F=Q^2+N.                                            (2.1)
```

Indeed, the coefficient change is the triangular polynomial isomorphism

```text
a6=2*p,
a5=2*c,
a4=p^2+2*r,
a3=2*p*c+n3,
a2=c^2+2*p*r+n2,
a1=2*c*r+n1,
a0=r^2+n0.                                         (2.2)
```

Its triangular Jacobian determinant is `2^3`, a unit in characteristic
zero.  Thus (2.1) neither loses nor introduces an octic coefficient
direction.

The involution `z |-> -z` fixes

```text
p,r,n2,n0,beta,gamma
```

and negates exactly

```text
c,n3,n1.                                           (2.3)
```

The unit change

```text
u=n1-(p/2)*n3                                      (2.4)
```

shows that `(c,u,n3)` is a basis for **all** odd coefficient directions.
There is no fourth hidden odd octic direction in the centered chart.
Any moving translation or uncentered coefficient in a total-Rees compiler
must therefore either be gauge-fixed by a printed unit coordinate change or
be retained as an additional odd variable before this theorem is imported.

The normalized loads `(1,beta,gamma)`, all even targets
`(mu2,mu4,mu6)`, and every even coefficient jet are parity-fixed
parameters.  They may move arbitrarily in the complete-local argument.

## 3. Base graph and the ordinary rows

At the exact-square central point set `c=n3=n2=n1=n0=0`.  On `D(D)`, the
corrected affine-Faber graph is

```text
beta=(5*D-s)/4,
gamma=D*(5*D-4*s)/16,
mu2=D^2*s/32.                                      (3.1)
```

With

```text
T=z^2+p/2,                 Q=T^2-D,
```

the polynomial part of the loaded exact-square expression is

```text
A=T^5-((s+5*D)/4)*T^3+(D*(2*s+5*D)/16)*T.         (3.2)
```

Let `R_ell` denote the literal ordinary Faber rows from the frozen source,
not the raw `z`-Laurent coefficients.  The source targets are

```text
(delta1,...,delta7)=(0,mu2,0,mu4,0,mu6,J/4),
```

so after the even targets solve the even rows, the only constraints relevant
to `J` accessibility are

```text
R1=R3=R5=0,                  J=4*R7.               (3.3)
```

If every odd coordinate in (2.3) is zero, `F` is even, every relevant Faber
polynomial is even, and the inverse root at infinity is odd.  Therefore

```text
R1=R3=R5=R7=0                               (3.4)
```

identically for arbitrary values and jets of all parity-fixed parameters.
This is the parity-fixed solution used below.

## 4. Exact first differential

For reference, at fixed inverse-root coordinate the first square-normal
variation can be written as the negative part of the rational Padé
differential

```text
delta R(w) = [ N*A'(z)/(2*Q*Q'(z)) ]_- ,           (4.1)
```

with the ordinary Faber sign convention of the charged source.  Expanding
(4.1), including the moving inverse root, and independently differentiating
the exact-square `c` column gives the following three-row block.

Put

```text
C0=(5*D-3*s)/4,
K0=5*D*(5*D-2*s)/16,
B0=-p^2/32-D/4,
q0=D*(5*D+2*s)/32.                                 (4.2)
```

In rows `(R1,R3,R5)` and columns `(c,u,n3)`, the Jacobian is

```text
          c                 u                    n3
R1        q0                C0/4                 0
R3       -p*q0/4           -p*C0/16              K0/4
R5        q0*B0             (C0*B0+K0)/4         -p*K0/16.  (4.3)
```

Subtracting `(C0/(4*q0))` times the first column from the second, wherever
`q0` is a unit, makes the determinant transparent.  As a polynomial identity
the result is

```text
det(4.3)=-q0*K0^2/16
 =-25*D^3*(5*D+2*s)*(5*D-2*s)^2/2^17.             (4.4)
```

Thus the block is invertible precisely on (0.1).  Notice that `C0=0` is not
an exceptional divisor: it does not occur in (4.4).

## 5. Complete-local proof

Let `x` be a point of the graph (3.1) lying in `U`, and complete the full
ordinary-Faber coefficient/load/target ring at `x`.  Denote all parity-fixed
parameters collectively by `E` and put

```text
O=(c,u,n3),                 Phi=(R1,R3,R5).
```

By (3.4), `Phi(E,0)=0` identically, including for arbitrary nilpotent or
formal jets in `E`.  By (4.4), `d_O Phi` is a unit matrix at `x`.  The formal
implicit-function theorem therefore gives a unique solution `O=psi(E)` in
the completed local ring.  Since `O=0` is already a solution for every `E`,
uniqueness gives

```text
psi(E)=0.
```

Equivalently, scheme-theoretically in the completion,

```text
(R1,R3,R5)=(c,u,n3).                               (5.1)
```

Parity now gives `R7 in (c,u,n3)`, so (5.1) implies `R7=0`.  After adjoining
the source equation `J-4*R7`, one obtains `J=0`.  Hence

```text
((R1,R3,R5,J-4*R7):J^infinity)=(1)                (5.2)
```

in the completed local ring.  Equation (5.2) excludes not merely a reduced
point but every nilpotent thickening and every formal arc whose closed point
lies on `U` and whose generic point has `J != 0`.

The two-pivot determinant

```text
det d(R6,R2-mu2)/d(beta,gamma)=D^4/64             (5.3)
```

from the corrected support theorem is a compatible preliminary block on
`D(D)`.  It establishes the graph before (5.1) is applied.  In subsequent
source corrections the smaller implementation is to let
`mu2,mu4,mu6` solve the three even rows directly and apply (5.1) only to the
odd rows.

## 6. Exceptional-divisor audit

The all-orders conclusion does not extend across either factor in (0.2).
The first differential nevertheless gives a sharp starting point.

### 6.1 `A`-face

On `5*D+2*s=0`, one has

```text
q0=0,             C0=25*D/8,       K0=25*D^2/8.
```

The block (4.3) has rank two.  Its sole kernel is the `c` direction.  Direct
differentiation of (3.2) shows that this direction has polynomial first
variation; hence every first-order tail, including `dR7`, vanishes on it.
The first exact-square transverse control is cubic, not quintic:

```text
128*R3+32*p*R1=c^3*(5*Delta-8*beta).               (6.1)
```

On the `A`-face the right coefficient is `5*Delta/4`, a unit on `D(D)`.
This identifies the primitive balance

```text
ord(5*D+2*s)=2*ord(c)                              (6.2)
```

for the exceptional correction fan.  The global raw fallback

```text
c^5+128*R5-96*p*R3-(12*p^2+32*r)*R1=0             (6.3)
```

remains a mandatory compiler control.

### 6.2 `K`-face

On `5*D-2*s=0`, one has

```text
q0=5*D^2/16,       C0=-5*D/8,       K0=0.
```

The block (4.3) has rank one.  A basis of its two-dimensional kernel is

```text
v_c:  (c,u,n3)=(1,2*D,0),
v_3:  (c,u,n3)=(0,0,1).                            (6.4)
```

In the original normal coordinates, `v_c` has `n1=2*D`, while `v_3` has
`n1=p/2`; their normal polynomials are respectively `2*D*z` and
`z^3+(p/2)z=z*T`.  Both directions have polynomial first variation, so all
first-order tails, including `dR7`, vanish.  Quadratic Kuranishi terms are
therefore the first possible accessibility test on this face.

The two exceptional divisors are disjoint on `D(D)`.  Their nonlinear
classification is deliberately left to a separate exact-source correction
fan.

## 7. Literal-source consumption gate

Before (5.2) is promoted to the total-Rees campaign ledger, a complete-source
replay must print all of the following:

1. the centered coefficient change (2.2), including any moving-center gauge,
   and proof that `(c,n1,n3)` exhaust the odd coefficient directions;
2. the ordinary Faber rows, inverse-root convention, and exact target tie
   `(0,mu2,0,mu4,0,mu6,J/4)`;
3. the two-sided normalization of `k10` and the exact identification of
   `(1,beta,gamma)` after all Rees powers are retained;
4. the two pivots (5.3), the block (4.3), and determinant (4.4), over exact
   `Q` from the complete source;
5. parity equivariance of every retained correction variable and absence (or
   explicit gauge removal) of an additional odd moving-center variable; and
6. the raw identities (6.1) and (6.3) before radical, saturation, or support
   substitution.

Failure of any item stops the import.  A good-prime replay is an independent
software control only.

## 8. Explicit nonclaims

This note does not classify the `A`- or `K`-face, `Delta=0`, or `k10=0`.
It does not assert that a normalized face automatically equals a
total-Rees chart without Section 7, and it does not apply to an omitted
odd moving-center or torsion direction.  It does not run terminal `[6,2]`,
either Taylor family, or any finite-branch compatibility test.  It does not
construct or exclude a global strict source arc, close the complete square
branch, order two, `(8,12)`, maximum twelve, or JC2.
