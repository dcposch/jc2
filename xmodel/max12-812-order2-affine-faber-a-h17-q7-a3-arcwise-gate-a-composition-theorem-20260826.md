# Provisional theorem: arcwise Gate A for the H17/q7/a3 receiver

Date: 2026-08-26

Status: **PROVISIONAL ARCWISE SOURCE COMPOSITION.**  This theorem is
conditional on confirmation of the frozen grade-51 reduction and of the
companion all-orders normalized implicit-function theorem.  It is not a
global total-Rees atlas and must receive a separate hostile review.

## 1. Literal source cell

Let `R` be a complete characteristic-zero DVR with uniformizer `sigma`.
Consider the literal delayed-load source

```text
Lambda=sigma^3,
k10=Lambda^12*K10,
k6 =Lambda^8 *K6,
k2 =Lambda^4 *K2,                                  (1.1)
```

and assume `K10` is a unit.  Perform exact monic square division of the
centered octic:

```text
C=Q^2+Delta,
Q=z^4+q2*z^2+q1*z+q0,       deg(Delta)<=3.          (1.2)
```

The registered H17/q7/a3 cell is

```text
ord_sigma(Delta)=17,
Q mod sigma=z^2*(z^2+p),                 p a unit,
ord_sigma(a)=3,
min(ord_sigma(U),ord_sigma(V))=7,
ord_sigma(R0,R1,S0,S1)>=14,                         (1.3)
```

with at least one of the leading `U,V` kernel coefficients nonzero.  The
exact coefficient variables `a,E,U,V,R0,W0` are defined in Section 3.
The cell also includes the affine load predecessor congruences

```text
K10=kappa,
K6 =(15/32)*kappa*E^2+sigma^6*d6,
K2 =(15/256)*kappa*E^4+sigma^6*d2,
mu2=-(5/4096)*kappa*E^6+sigma^6*dm,
mu4=d4,                                            (1.4)
```

where `kappa` is a unit.  Equations (1.3)--(1.4) name a single closed
Newton cell; this theorem does not assert that every literal source arc
enters it.

## 2. The first literal source block

The exact expansion

```text
(Q^2+Delta)^(3/2)
 =Q^3+(3/2)Q*Delta+(3/8)Delta^2/Q
   -(1/16)Delta^3/Q^3+...                           (2.1)
```

has polynomial first two terms.  At normal order 17, the first possible
negative block is

```text
(3/8)*sigma^34*[N0^2/Q0]_-,
Delta=sigma^17*(N0+higher),
Q0=z^2*(z^2+p).                                    (2.2)
```

Every delayed load and `mu2` target begins at sigma weight 42, while the
intrinsic cubic begins at 51.  Thus no forcing ties (2.2).  The promoted
ordinary-first-four divisibility bridge gives

```text
Q0 divides N0^2.                                   (2.3)
```

Since `Q0=A0^2*D0` with `A0=z`, `D0=z^2+p`, and `p` a unit, `A0` and
`D0` are coprime and `D0` is squarefree.  The declared nonzero first
normal therefore has

```text
N0=m*z*(z^2+p),                  m a unit.          (2.4)
```

This is correction-independent: moving coefficients raise the grade-34
block, and neither a load nor a target can enter before weight 42.

The charged bridge, review, and promotion are

```text
56123a6f2b110284871fe65d664ffed89cb5004d1498e59a81719c2278c59f23
  xmodel/max12-812-order2-square-normal-first-block-divisibility-bridge-theorem-20260826.md
85389a28a69b5e030fa689ccce9dcccee484dae9169679053d0870cfe1e9f0ff
  xmodel/max12-812-order2-square-normal-first-block-divisibility-bridge-hostile-review-grok-v2-20260826.md
eb3032522265c27f2eed46ef0de7458453ad80b9b4f3a636ab32ce3afe1b6bf0
  xmodel/max12-812-order2-square-normal-first-block-divisibility-bridge-promotion-20260826.md
```

## 3. Exact two-sided affine coefficient map

Factor the declared first normal exactly as

```text
Delta=sigma^17*N,
N=n3*z^3+n2*z^2+n1*z+n0,
```

so that `n3 mod sigma=m` is a unit by (2.4).  On `D(n3)`, set

```text
M  =n3,
a  =n2/M,
E  =q2+6*a^2,
U  =q1-2*a*(4*a^2-E),
R0 =q0-a^2*(E-3*a^2)+a*U,
V  =n1-(E-5*a^2)*M,
W0 =n0+a*(E-3*a^2)*M+a*V-M*U/2.                  (3.1)
```

These formulas invert exactly

```text
q2=E-6*a^2,
q1=2*a*(4*a^2-E)+U,
q0=a^2*(E-3*a^2)+R0-a*U,
n3=M,
n2=a*M,
n1=(E-5*a^2)*M+V,
n0=-a*(E-3*a^2)*M-a*V+M*U/2+W0.                 (3.2)
```

After multiplying (3.2)'s four normal coefficients by the common factor
`sigma^17`, these are the literal affine-Faber graph formulas with
`lambda=sigma^17`.  The central values forced by (2.4) are

```text
(a,E,U,R0,M,V,W0)=(0,p,0,0,m,0,0).               (3.3)
```

Split the positive-order series `U,V` at order seven into kernel series
`X,Y`, and split the remainders and `W0,R0` according to the order-14
complement condition in (1.3).  This coefficient splitting is two-sided
arcwise.  On `D(X_0)` or `D(Y_0)` it lands exactly in one of the two
projective charts of the confirmed grade-48 predecessor.  It introduces
no root extension, Rees torsion, or one-way specialization.

The monic square division (1.2) is itself a polynomial coordinate
isomorphism over `R[1/2]`: its inverse is `C=Q^2+Delta`.  Hence the
composition from literal coefficient arcs to (3.1), and back by
(3.2)+(1.2), is exact in both directions on `D(M)`.

## 4. Source rows equal the normalized graph rows

Under `Lambda=sigma^3`, the effective delayed loads in the literal source
all begin at weight 42.  The effective target timings are

```text
mu2:42,  mu4:48,  mu6:54,  J/4:57.                (4.1)
```

Substitution of (3.2) and (1.4) into the complete ordinary-Faber tails is
the exact source substitution used by the frozen H17 producer: no Laurent
row replaces an ordinary row and no target is projected.  The polynomial
weight-42/45 load identities cancel precisely the predecessor terms below
weight 48.  Thus, on the named literal cell, the complete source rows are
the complete normalized graph rows coefficient for coefficient.

This is the missing arcwise Gate-A statement.  It uses exact coordinate
isomorphisms on one DVR, so it does not require a monolithic Rees algebra
or commutation of saturation with specialization.  It also does not claim
an atlas covering neighboring valuation cells.

### 4.1 Lift back to the strict two-parameter source

The promoted one-parameter reduction is not being used as a
completion-to-global heuristic.  It gives the literal flat pullback

```text
Lambda=tau^3*varrho,
R=1+tau,
C_i=B_i                    (i even),
C_i=R*B_i                  (i odd),
J=R*j.                                                (4.2)
```

For the present one-parameter arc `Lambda=sigma^3`, make the finite
ramification `sigma=s^4` and choose

```text
tau=s^3,       varrho=s^3.                            (4.3)
```

Then `tau^3*varrho=s^12=sigma^3` exactly, while both `tau` and `varrho`
have positive order.  Since `R=1+s^3` is a unit, (4.2) has the explicit
inverse `B_even=C_even`, `B_odd=C_odd/R`, `j=J/R`.  Thus the arc lifts to
the strict two-parameter source after finite ramification; it is not only
a point of a projected one-parameter closure.  All load variables are
retained, and a unit source determinant remains a unit after division by
`R`.

The reviewed reduction chain used here is

```text
5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md
1da9974dde45fd73c757eb315d50bc9e8abaa028ebb8d5894ca2ea4b2bd6d2de
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-review-grok-20260826.md
82167b862a779d1104e3fb904d71627b799f48074241d8496fc1051d0a7afa2f
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-promotion-20260826.md
```

This toric lift is existence for the named arc, not a unique overlap or a
global fan chart.  Other positive rational splittings of
`v(Lambda)=3v(tau)+v(varrho)` are not classified here.

## 5. Consequence of the normalized formal lift

The finite grade-51 reduction supplies, on both projective charts, the
receiver

```text
5*kappa(0)*a3^3*p^5-8*m^3=0.                      (5.1)
```

The companion complete-local theorem has dependent Jacobian

```text
45*x*m^2*a3^4*p^16/2^19
```

on `D(X_0)` and the same determinant with `x` replaced by `y` on
`D(Y_0)`.  Consequently it lifts (5.1) uniquely to all orders in the seven
dependent graph series.  Because every map in Sections 2--4 is two-sided,
the inverse produces a literal formal coefficient arc satisfying all seven
source rows.

Choose the original determinant target series to have unit constant term.
Its effective occurrence is `sigma^57*J/4`, as in (4.1), so the resulting
literal source arc has `J` nonzero over the fraction field.  Also
`Q0^2=z^4*(z^2+p)^2` has nonzero coefficients and (5.1) makes `K10`
a unit.  Thus the arc is not deleted by the coefficient-irrelevant,
`Lambda`, `K10`, or `J` opens named in this cell.

This is a literal **source-row** survivor, not yet a polynomial Keller
pair.  It makes the finite Taylor gates, rather than another infinity-row
prolongation, the decisive next tests.

## 6. What is and is not covered

The statement covers exactly

```text
H=17, q=7, ord(a)=3,
D(p*m*K10),
the load graph (1.4),
the two projective opens D(X_0) and D(Y_0).
```

It does not cover a different factor type, `p=0`, `m=0`, `K10=0`, unit
kernel, unequal kernel order outside the registered split, another center
order, another load slope, or the rest of the source fan.  It does not
construct a global total-Rees/Cech atlas or prove overlap with all other
charts.

Most importantly, it does not supply the invariant rational coefficient
functions needed at the two finite branches.  Terminal infinity is already
part of the complete seven-row formal solve, but terminal-to-global
algebraization and both finite Taylor polynomiality pullbacks remain open.
It therefore does not produce a Keller map or counterexample, and does not
settle order two, `(8,12)`, maximum twelve, or JC2.
