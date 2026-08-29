# `(8,12)` order two: delayed-load total-Rees parity/Fitting import design

Date: 2026-08-26

Status: **SOURCE-TYPED DESIGN NOTE.  THE DELAYED-LOAD FILTRATION RULES OUT
THE PROPOSED FULL-BLOCK IMPORT BEFORE THE UNIT-`J` ROW.  A SMALLER
RANK-ONE GATE AND A QUADRATIC CORRECTION CONE (UNRAMIFIED CONTACTS
`h=8,9`) REMAIN TO BE REPLAYED FROM THE COMPLETE SOURCE.  NO TOTAL-REES OR
ORDER-TWO EXCLUSION IS CLAIMED.**

## 0. Charged inputs

The literal one-parameter source and its promoted reduction are

```text
5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md
82167b862a779d1104e3fb904d71627b799f48074241d8496fc1051d0a7afa2f
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-promotion-20260826.md
```

The normalized ordinary-Faber support, generic parity theorem, and its
independent hostile confirmation are

```text
817b96968a4a5abecfc785cc0fe2bba57c50d0a5cd52dabe2bccdef26e8846af
  xmodel/max12-812-order2-exact-square-affine-faber-support-promotion-20260826.md
fe1193abe8c45c590f7653d96998a7b053e8de0e09a751cd8fb686d2cbf72fc1
  xmodel/max12-812-order2-exact-square-affine-faber-generic-j-exclusion-theorem-20260826.md
08a6bec022613a1d26ac64a5685e6408e875423b609c50fee604326fbb5a15dc
  xmodel/max12-812-order2-exact-square-affine-faber-generic-j-exclusion-hostile-review-grok-20260826.md
```

Finally, the primitive `A`-face source exclusion is

```text
9419c08b4be09fee8ecae9b73c8c9c610770a7166e17a973251312d28b69a695
  xmodel/max12-812-order2-affine-faber-a-delayed-load-source-cubic-exclusion-20260826.md
```

That last theorem is producer-tier while its hostile review is live.  It is
used below only as a provisional leaf certificate.

## 1. Literal delayed-load quotient

The complete source rows are

```text
Phi_l = r_l(C,Lambda^2*k10,Lambda^6*k6,Lambda^10*k2)
        -Lambda^(12+l)*delta_l,

(delta1,...,delta7)=(0,mu2,0,mu4,0,mu6,J/4).       (1.1)
```

Impose the integral delayed-load ray

```text
k10=Lambda^12*K10,
k6 =Lambda^8*K6,
k2 =Lambda^4*K2.                                   (1.2)
```

Then all three effective loads in `r_l` have the same absolute order:

```text
Lambda^2*k10 = Lambda^14*K10,
Lambda^6*k6  = Lambda^14*K6,
Lambda^10*k2 = Lambda^14*K2.                       (1.3)
```

Write `U_l(C)=r_l(C,0,0,0)`.  Exact affine-linearity in the three lower
loads gives, on `D(K10)`,

```text
Lambda^-14*K10^-1*Phi_l
 = Lambda^-14*K10^-1*U_l(C)
   +R_l(C;1,beta,gamma)-T_l,                       (1.4)

beta=K6/K10,                    gamma=K2/K10,
T2=m2, T4=Lambda^2*m4, T6=Lambda^4*m6,
T7=Lambda^5*j/4,                T1=T3=T5=0,
(m2,m4,m6,j)=(mu2,mu4,mu6,J)/K10.                 (1.5)
```

Formula (1.4) is an identity only on a chart on which `U_l(C)` is known to
be divisible by `Lambda^14`; it is not permission to discard lower
unloaded rows.  Its zeroth divided grade on an exact square is precisely
the normalized ordinary-Faber face.  The terminal `J` target is at relative
grade five.

## 2. Complete coefficient and load inventory

Use the exact square-division chart

```text
K(Lambda)=z^4+p(Lambda)*z^2+c(Lambda)*z+r(Lambda),
C=K(Lambda)^2+Lambda*N(Lambda).                    (2.1)
```

If the actual first square-normal defect has order `h`, write

```text
N(Lambda)=Lambda^(h-1)*E(Lambda),
E_i=n3_i*z^3+n2_i*z^2+n1_i*z+n0_i,
u(Lambda)=n1(Lambda)-(p(Lambda)/2)*n3(Lambda).      (2.2)
```

Here `h` is an integer only when `Lambda` is a uniformizer.  For an
arbitrarily ramified arc the invariant notation is

```text
e=v(Lambda),                 H=v(C-K(Lambda)^2),    (2.3)
```

and every comparison below is homogeneous in `(e,H)`.

For an unramified `Lambda`-adic client, the raw variables that can enter by
absolute grade nineteen are exactly:

| family | raw power in (1.1) | needed jets through grade 19 |
|---|---:|---|
| `K10_j,K6_j,K2_j` | `14+j` after (1.3) | `j=0,...,5` |
| `mu2_j` | `14+j` | `j=0,...,5` |
| `mu4_j` | `16+j` | `j=0,...,3` |
| `mu6_j` | `18+j` | `j=0,1` |
| `J_j` | `19+j` | `j=0` on the unit-`J` ray |
| `p_j,c_j,r_j` in `K(Lambda)` | loaded term `14+j` | `j=0,...,5` |
| normal `E_i` | actual coefficient order `H+i e` | every `i` whose unloaded quadratic order is at most `19e` |

After ramification the coefficient series need not be series in `Lambda`;
the compiler must instead retain every uniformizer jet of valuation at most
the displayed cutoff.  The valuation formulation in Sections 4 and 6 is
the authoritative one in that case.

Dividing by the entire unit series `K10`, rather than only its leading
coefficient, replaces the first four rows of the table by the unitriangular
series coordinates `(beta,gamma,m2,m4,m6,j)`.  This is a coordinate change,
not a load projection.  A compiler must retain either complete list and
print the two-sided conversion.

The normal coordinates split under `z -> -z` as

```text
even: (n2_i,n0_i),             odd: (u_i,n3_i).     (2.4)
```

All load and target jets are even.  The centered source has one square-
tangent odd coordinate `c_i`.  If a literal total chart exposes an
additional moving-center odd coordinate, it must be added as a column;
silently gauging it away invalidates every Fitting claim below.

## 3. Exact normalized odd and terminal blocks

At the affine graph put

```text
D=(p^2-4*r)/4,                  s=5*D-4*beta,
C0=(5*D-3*s)/4,
K0=5*D*(5*D-2*s)/16,
B0=-p^2/32-D/4,
q0=D*(5*D+2*s)/32.                                 (3.1)
```

For odd rows `(R1,R3,R5)` and odd coefficient coordinates `(c,u,n3)`, the
confirmed normalized block is

```text
M = [ q0          C0/4                 0
     -p*q0/4     -p*C0/16              K0/4
      q0*B0       (C0*B0+K0)/4        -p*K0/16 ],   (3.2)

det(M)=-q0*K0^2/16
      =-25*D^3*(5*D+2*s)*(5*D-2*s)^2/2^17.         (3.3)
```

The exact row-seven derivative needed for an adjugate certificate is

```text
v=d_(c,u,n3)R7
 =(q0*B7,
   (C0/4)*B7-p*K0/16,
   (K0/4)*(D/4-p^2/32)),                            (3.4)

B7=[w^-7](z/T)=3*p*D/16-p^3/128,
T=z^2+p/2,                    w^4=T^2-D.            (3.5)
```

Indeed the three differential series are

```text
q0*z/T,
(C0/4)*z/T+(K0/4)*z/(T*(T^2-D)),
(K0/4)*z/(T^2-D),                                  (3.6)
```

so (3.2) and (3.4) are coefficients of the same literal ordinary-Faber
source series, not unrelated Jacobians.

Suppose a divided grade has full new odd vector `x=(c_*,u_*,n3_*)`, odd
residual `b=(b1,b3,b5)^t`, terminal residual `b7`, and terminal coefficient
`j_*`.  The exact augmented Fitting/adjugate block is

```text
F_full = [ M   b
           v   b7-j_*/4 ].                          (3.7)
```

On `D(det(M))`, the first three equations give

```text
det(M)*x=-adj(M)*b,                                 (3.8)
```

and the terminal compatibility is the single fraction-free identity

```text
det(F_full)
 =det(M)*(b7-j_*/4)-v*adj(M)*b=0.                  (3.9)
```

Off that open, the client must use the appropriate minors of the augmented
matrix; dividing by a chosen minor is not an exhaustive Fitting argument.

Before the two normal columns occur, the actual block is only

```text
m_c=(q0,-p*q0/4,q0*B0)^t,            v_c=q0*B7.    (3.10)
```

For a residual `(b1,b3,b5,b7-j_*/4)`, the exact rank-one Fitting conditions
are the `2 x 2` minors of

```text
F_c = [ q0          b1
       -p*q0/4     b3
        q0*B0      b5
        q0*B7      b7-j_*/4 ].                     (3.11)
```

On `D(q0)` they reduce without a hidden denominator to

```text
b3+(p/4)*b1=0,
b5-B0*b1=0,
b7-j_*/4-B7*b1=0.                                 (3.12)
```

Equations (3.7)--(3.12), rather than `det(M)` alone, are the literal
adjugate/Fitting import object.

## 4. Filtration obstruction

The unloaded first differential vanishes on an exact square.  A square-
normal defect of valuation `H` therefore first contributes unloaded terms
at valuation `2H`.  In contrast:

```text
common loaded face:                  14e,
unit-J terminal target:              19e,
loaded linear normal block:          14e+H,
unloaded quadratic normal block:     2H.            (4.1)
```

Consequently:

1. `2H<14e`: unloaded predecessor rows occur before the affine face;
2. `2H=14e`: the divided zeroth grade is affine plus a quadratic
   Kuranishi term, not the normalized affine support;
3. `14e<2H<=19e`: the base face is pure, but a quadratic normal residual
   enters no later than the unit-`J` row;
4. `2H>19e`: no normal term occurs through the unit-`J` row;
5. `H<14e`, `H=14e`, and `H>14e` respectively put the quadratic block
   before, tied with, or after the loaded linear normal block.

In unramified integer notation, the only pure-face contacts with a normal
quadratic at or before the terminal row are `h=8,9`; after ramification the
honest window is the whole rational cone

```text
7e < H <= 19e/2.                                   (4.2)
```

The full matrix `M` first becomes available at relative valuation `H`,
i.e. absolute valuation `14e+H`.  Purity already requires `H>7e`, whereas
the terminal is relative valuation `5e`.  Thus the full three-column block
can never occur before the unit-`J` target on this pure delayed-load face.
It is cleanly leading against the unloaded quadratic only when `H>14e`.
At `H=14e` it is a correction-dependent Kuranishi block; for
`7e<H<14e` quadratic equations precede it.

This is the promised incompatibility: generic invertibility of (3.2) does
**not** by itself propagate the normalized complete-local theorem into the
total-Rees unit-`J` problem.

## 5. What does propagate before the terminal row

On the high-normal-contact cone `2H>19e`, parity leaves only the square-
tangent `c` column through relative grade five.  After the zeroth affine
graph is imposed, (3.11) applies grade by grade.  On `D(q0)`, the first row
successively kills every `c` coefficient before and at the terminal grade;
the other odd rows are then automatic parity controls.  At relative grade
five, (3.12) forces the leading normalized `j` coefficient to vanish.

Thus a complete-source replay of (1.4), (3.10), and parity would exclude
the **unit-`J` delayed-load ray** on

```text
D(K10*D*(5*D+2*s)),              2H>19e.            (5.1)
```

Notably, the normalized `K` resonance `5D-2s=0` lies in this rank-one open:
there `q0=5D^2/16`.  It is exceptional for the late full block, but not for
the early unit-`J` gate.  The only affine resonance left by (5.1) is the
`A` face `5D+2s=0`.

On that face let

```text
a=v(c),                    d=v(5D+2s).              (5.2)
```

When normal terms are absent through `19e`, the exact cubic identity forces
the only possible unit-`J` Newton balance

```text
d=2a,                       3a=5e.                  (5.3)
```

Its primitive integral generator is

```text
(e,a,d)=(3,5,10),           Lambda=sigma^3,
c~sigma^5,                  5D+2s~sigma^10.         (5.4)
```

The producer theorem at SHA `9419c08b...` source-types this primitive cubic
cell, includes the earlier unloaded predecessor forced by its natural
normal corrections, splits `r!=0` from the repeated-root divisor `r=0`,
and excludes both.  Subject to its pending hostile review, it is the exact
`A`-leaf certificate for (5.3); an untyped normalized cubic witness is not a
source survivor.

Therefore the smallest unresolved unit-`J` part of the delayed-load affine
ray is the correction window (4.2), together with the tie `2H=14e`.  The
late determinant factor `K0` should not be used to manufacture an extra
pre-terminal branch.

## 6. Minimal finite valuation fan and exhaustiveness gate

To make the ray result useful beyond isolated contacts, the next theorem
must be a finite **literal-source initial-form cover**, not a bounded box of
integer weights.  Split the normal defect into its parity valuations

```text
H_plus = min valuation of (n2,n0),
H_minus= min valuation of (u,n3).                  (6.1)
```

After the `P` predecessor below has been routed, the finite support list
relevant to the first decision through the unit terminal is

```text
14e, 16e, 18e, 19e,
2*H_plus, H_plus+H_minus, 2*H_minus,
14e+a,
14e+d+a, 14e+3a.                                  (6.2)
```

The first line records the common load and three delayed targets; the
second is the complete parity decomposition of the unloaded quadratic
normal term; the third is the generic `c` column and the two `A`-face
linear/cubic modes.  Any extra source monomial found by literal replay must
be added before the fan is accepted.

The minimal exhaustiveness statement is:

> After arbitrary finite ramification, every unit-`J` arc on
> `D(K10*D)` whose three effective lower loads have common initial valuation
> `14e` has an initial form in the rational polyhedral fan cut out by all
> equalities and strict inequalities among (6.2).  Each cone is represented
> by a flat, source-equivalent Rees chart retaining every load, target,
> square-tangent, even-normal, and odd-normal leading coefficient.  The
> charts cover the original `J`-saturated arc functor, not merely its
> projection or reduced support.

For the unit-terminal decision, this fan has only four mathematical leaf
types:

```text
P:  min(2H_plus,H_plus+H_minus,2H_minus) < 14e
    (unloaded predecessor);
T:  the same minimum equals 14e
    (quadratic/affine tie);
Q:  14e < the minimum <= 19e
    (finite augmented rank-one Fitting/Kuranishi cells);
H:  the minimum > 19e
    (rank-one gate (5.1), plus the unique primitive A cell (5.4)).
```

`P` must route to the reviewed first-normal divisibility receiver rather
than be divided by `Lambda^14`.  `T` and `Q` require exact instances of
(3.11), with their raw nonreduced predecessor ideals.  `H` is the proposed
rank-one replay plus the provisionally excluded primitive `A` cell.  A
finite Hilbert-basis list of the cones, together with two-sided chart maps
and overlap checks, is the minimum acceptable exhaustiveness certificate;
sampling integer contact boxes is not.

This cover is global only for the fixed delayed-load, unit-`J`, `D(K10*D)`
ray.  Separate fans are still required for unequal effective load
valuations, positive valuation of capitalized `J`, `K10=0`, and `D=0`.

## 7. Exact compiler acceptance test

A narrow AWS client should:

1. emit (1.1) from the frozen ordinary tails, substitute (1.2), and verify
   coefficientwise divisibility and equality in (1.4), without projecting a
   load or target;
2. print the entire variable/power inventory of Section 2 and fail on an
   undeclared odd coordinate;
3. reproduce the affine zeroth face, (3.2), (3.4), and both columns of
   (3.11) over exact `Q`; use a good prime only as a software control;
4. run the high-contact quotient through relative grade five and prove the
   three identities (3.12), including `j_0=0` on `D(q0)`;
5. emit every monomial valuation in (6.2), compare it against the literal
   source support, and reject a missing support form before enumerating the
   rational cones;
6. compile separate flat charts for `P,T,Q,H`, preserve the raw nonreduced
   ideals, and check all overlaps before any union claim; and
7. use the primitive `A` theorem only after its hostile review confirms the
   source predecessor, ramification (5.4), and the `r=0` repeated-root
   coverage.

The cheapest falsifiers are an extra odd moving-center column, a source
monomial absent from (6.2), failure of exact `Lambda^14` divisibility, or a
`T/Q` cone whose augmented Fitting minors vanish without forcing `j_0=0`.

## 8. Firewall

This note identifies a source-filtration obstruction to the originally
proposed full-adjugate shortcut and replaces it by a smaller finite design.
It proves no chart cover, no `T/Q` Kuranishi emptiness, and no total-Rees
boundary exclusion.  It does not exhaust other load or `J` valuations,
`K10=0`, `D=0`, the terminal `[6,2]` passport, or either finite Taylor
family.  It does not close the square branch, order two, `(8,12)`, maximum
twelve, or JC2.
