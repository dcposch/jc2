# `(8,12)` order two: delayed-load source exclusion of the affine-Faber `A` cubic

Date: 2026-08-26

Status: **CHARACTERISTIC-ZERO PRODUCER THEOREM FOR THE PRIMITIVE
UNIT-`J` CUBIC BALANCE ON THE DELAYED-LOAD RAY.  HOSTILE REVIEW IS
PENDING.  THIS IS NOT A COMPLETE TOTAL-REES OR ORDER-TWO EXCLUSION.**

## 0. Frozen inputs

```text
5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md
1da9974dde45fd73c757eb315d50bc9e8abaa028ebb8d5894ca2ea4b2bd6d2de
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-review-grok-20260826.md

4c9d9cfc58eb4ca2a33c9bf83beb485c15f0796fa36d2ffe4826c3fdeeac374d
  xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-20260826.md
08a5ca51461afb1753b21ee7fcf4bf8ed3719cb6edafb7d2020043ad63ab9efa
  xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-review-grok-20260826.md

40b6d15eb23fc85038182146d8f044dee3d37c7c7e6fc4880e0ac3d223297d5f
  xmodel/max12-812-order2-affine-faber-exceptional-cubic-forms-source-ray-triage-20260826.md
```

The first pair licenses the literal one-parameter source.  The second pair
proves the exact unloaded first-normal criterion `Q | N^2`.  The last file
records the four exact `A`-face cubic forms emitted by the exact-`Q` AWS
ordinary-Faber compiler.  The finite-field lane is a software control and is
not used below.

## 1. Literal delayed-load face

The source equations are

```text
Phi_l = r_l(C,Lambda^2*k10,Lambda^6*k6,Lambda^10*k2)
        -Lambda^(12+l)*delta_l,

(delta_1,...,delta_7)=(0,mu2,0,mu4,0,mu6,J/4).       (1.1)
```

Insert the integral load graph

```text
k10=Lambda^12*K10,
k6 =Lambda^8*K6,
k2 =Lambda^4*K2.                                    (1.2)
```

Every effective lower load in (1.1) is then `Lambda^14` times its
capitalized coordinate.  The ordinary tail map is affine-linear in the
three lower loads.  Hence, on an exact square `C=Q^2`, its grade-fourteen
face is exactly

```text
R1=R3=R4=R5=R6=R7=0,              R2=mu2,           (1.3)
```

for the ordinary loaded polynomial with loads `(K10,K6,K2)`.  Row four's
target begins at relative order two, row six's at relative order four, and
row seven's at relative order five.  Thus (1.2), rather than a weighted
coefficient contraction to the irrelevant origin, is the literal source
of the normalized affine-Faber leading receiver.

The graph ideal of (1.2) is prime and `Lambda`-torsion-free.  On
`D(Lambda)` its inverse is the three displayed divisibility quotients.  For
the present existence/exclusion calculation we specialize the leading
coordinate to `K10=1`; no claim that this specialization normalizes every
point of `D(K10)` is needed.  No assertion about exhaustiveness of all load
valuations is made.

## 2. Predecessor imposed by an octic normal defect

Work at a central point

```text
Q0=z^4+p*z^2+r,               D=(p^2-4*r)/4 != 0.    (2.1)
```

Let the first coefficient displacement transverse to the exact-square
locus be `epsilon^h*N`, with `deg(N)<=3`; tangent motion is absorbed into a
moving quartic `Q(epsilon)`.  If this normal displacement occurs before the
grade-fourteen loaded face, the exact first nonzero unloaded rows are the
first seven tails of

```text
(3/8)*N^2/Q0.                                      (2.2)
```

The reviewed first-normal theorem gives, without taking a radical,

```text
all seven rows of (2.2) vanish  iff  Q0 divides N^2. (2.3)
```

There are only two cases on `D(D)`.

1. On `D(r)`, the quartic `Q0` is squarefree: its discriminant is a nonzero
   scalar times `r*D^2`.  Equation (2.3) then forces `Q0 | N`, and
   `deg(N)<deg(Q0)` forces `N=0`.
2. On `r=0`, one has `D=p^2/4`, so `p` is a unit and

   ```text
   Q0=z^2*(z^2+p),       D_Q0=z*(z^2+p).              (2.4)
   ```

   The reviewed UFD criterion says (2.3) is equivalent to `D_Q0 | N`.
   In particular a normal of degree at most two is zero, while a cubic
   normal is necessarily a scalar multiple of `z*(z^2+p)`.

This is the source predecessor that the normalized ordinary-Faber IFT does
not impose.

## 3. Primitive `A`-face balance

On the exceptional `A` face use the exact normalized weights

```text
c=t*x,
n2=t^2*e2,                 n0=t^2*e0,
n3=t^3*v,                  n1=t^3*(u+(p/2)*v),
K6=15*D/8+t^2*b,           K2=15*D^2/16+t^2*g.       (3.1)
```

Here `x*D` is a unit.  The first possible normalized terminal value is the
cubic `J3*t^3`.  Since the literal terminal target occurs five orders after
the loaded face, a unit source `J` requires

```text
3*v(t)=5*v(Lambda).                                  (3.2)
```

Equivalently, after primitive ramification,

```text
Lambda=sigma^3,                 t=sigma^5.            (3.3)
```

The normals in (3.1) then occur at sigma-orders ten and fifteen.  Their
unloaded quadratic rows occur no later than sigma-order thirty, strictly
before the loaded face `Lambda^14=sigma^42`.  They must therefore satisfy
the predecessor (2.3).

First the degree-at-most-two normal must vanish:

```text
e0=e2=0.                                             (3.4)
```

On `D(r)`, (2.3) also gives

```text
u=v=0.                                               (3.5)
```

The exact cubic row `A1=0` then solves

```text
g=(5/16)*x^2*p+(3/2)*b*D.                           (3.6)
```

Substitution in the exact row `A3` cancels every `p`- and `b`-term and
leaves

```text
A3=(5/128)*x^3*D,                                   (3.7)
```

a unit.  Thus the primitive cubic is impossible on `D(r*D*x)`.

It remains to check the repeated-root divisor `r=0`; it cannot be discarded
by the squarefree argument.  From (2.4), the only allowed cubic normal is

```text
N=v*z*(z^2+p),             u=(p/2)*v.                (3.8)
```

Substitute `D=p^2/4`, (3.4), and (3.8) in the exact emitted forms.  The
first two rows give

```text
v=-x^3/(5*p^2),
g=45*x^2*p/128+3*b*p^2/8.                            (3.9)
```

All `b`-terms cancel in the third row, whose residual is

```text
A5=5*x^3*p^3/1024.                                  (3.10)
```

This is a unit on `r=0,D*x!=0`.  Equations (3.7) and (3.10) cover all of
`D(D*x)`.  Therefore the delayed-load source predecessor has **no primitive
`A`-face cubic solution with unit leading `J`**, even though the untyped
normalized ordinary-Faber system has exact rational `J`-nonzero formal
arcs.

## 4. Direct rejection of the rational normalized witness

At the frozen normalized point

```text
D=1, p=0, x=1, v=-1/20,
b=g=e0=e2=u=0,                                      (4.1)
```

the first normal is `N=-(t^3/20)z^3`.  Under (3.3), its unloaded quadratic
term occurs at relative `Lambda`-order ten:

```text
(3/8)*N^2/Q0
 = Lambda^10*(3/3200)*z^6/(z^4-1).                  (4.2)
```

Its negative Laurent coefficients at `z^-2` and `z^-6` are both
`3/3200`; in the ordinary connection this gives nonzero predecessor rows
`R2=3/3200` and `R6=3/6400`.  No load or target exists at that order.
Thus the specific normalized formal arc is rejected at `Lambda`-order ten,
four orders before the loaded face and nine orders before its proposed
terminal balance.

## 5. Scope

This theorem closes the primitive cubic `A` client only on the integral
delayed-load ray (1.2), after the ramified unit-`J` balance (3.3).  It does
not prove that (1.2) exhausts all load Newton faces, classify a branch whose
first normalized `J` term occurs after cubic order, classify the `K` face,
handle `D=0` or `K10=0`, compute the full nonreduced total-Rees boundary,
impose terminal `[6,2]` beyond its valuation, or impose either Taylor
family.  It does not close order two, `(8,12)`, maximum twelve, or JC2.
