# Addendum: source-coordinate face in the delayed-load affine-Faber `K` to K2 composition

Date: 2026-08-26

Status: **NONMUTATING SOURCE-COORDINATE REPAIR TO THE PRODUCER COMPOSITION THEOREM; HOSTILE REVIEW REQUIRED.**

## 0. Repaired target

This addendum repairs the weighted-blowup exhaustiveness argument in

```text
6178089bb11efebb304b2eb24dca6eb654bde060396fbf4f4456f515cae28989
  xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composition-exclusion-20260826.md
```

without changing those charged bytes.  The target correctly treats the
chart in which the local source/Rees parameter has weight-two leading
coefficient one.  It omitted the projective face on which that coefficient
is zero and a weight-one kernel/root-splitting correction leads earlier.

## 1. Homogenized K2 face

Retain the target's discriminant coordinates and put

```text
K0=A^2*(A^2+b*A+e),
N0=m*A*(A^2+b*A+e),
K1=x*A,
N1=y*A+h,
h=m*x/2.                                             (1.1)
```

Let `L` be the weight-two leading coordinate of the local source/Rees
parameter.  Homogenizing the exact analytic K2 formula replaces the
intrinsic cubic term `-m^3` by `-L^3*m^3`.  On the source-zero face
`L=0`, the delayed-load graph also has `kappa=0`, and after the two unit
complementary pivots the five high rows are

```text
u3=u4=u5=u6=u7=0,                                   (1.2)

sum_(n>=0) u_n*t^n
 = t^2*(y-h*t)^2/(1+b*t+e*t^2).                    (1.3)
```

The power `L^3` is forced by the cubic source term: under the half-weight
substitution `Lambda=rho^2*L`, the coefficient at `rho^6` is
`-L^3*m^3/(16*A^3)`.  The quadratic kernel term in (1.3) is independent
of `L`.

## 2. The omitted face is empty at the repeated `K` point

The repeated affine-Faber `K` point is

```text
b=0,  e=p,  m=p*x0,              e*m != 0.          (2.1)
```

At `b=0`, (1.3) begins

```text
u2 = y^2,
u3 = -2*y*h,
u4 = h^2-e*y^2,
u5 = 2*e*y*h,
u6 = e^2*y^2-e*h^2,
u7 = -2*e^2*y*h.                                   (2.2)
```

Already `u3=u4=0` gives, set-theoretically on `D(e)`,

```text
y*h=0,
h^2=e*y^2
   => y=h=0.                                        (2.3)
```

Since `m` is a unit and `h=m*x/2`, (2.3) also gives `x=0`.
The first two analytic rows are unit-triangular in the two complementary
coordinates with diagonal coefficients a nonzero rational multiple of
`m` and of `m^2`; hence those coordinates vanish as well.  There is no
projective exceptional point on `L=0` after saturation by the kernel or a
complementary leading coordinate.

This is exactly the face produced when a kernel/root-splitting correction
occurs earlier than the half-weight tie.  It is killed by the quadratic
kernel rows, rather than by the intrinsic `-m^3` row.

## 3. Repaired exhaustive dichotomy

After common ramification and absorption of tangent motion into the smooth
discriminant parameters `(a,d,m)`, the normalized weighted blowup has two
source-coordinate cases:

1. `L!=0`: normalize `L=1`.  The reviewed K2 unit identities on
   `D(e*m)`, transported to complete source rows by V3, give the target
   theorem's contradiction.
2. `L=0`: equations (2.2)--(2.3) kill every weight-one kernel/root-splitting
   direction, and the unit complementary pivots kill every weight-two
   complementary direction.  Hence this projective face is empty.

Thus the source-coordinate omission does not create a surviving delayed-
load `K` arc.  The conclusion and firewalls of the repaired target remain
unchanged.

The argument is set-theoretic/valuative, which is sufficient to exclude a
formal or Puiseux arc.  It does not claim a new raw nonreduced K2 scheme
identity, treat a different load graph, treat the exceptional `A` face, or
close order two or JC2.
