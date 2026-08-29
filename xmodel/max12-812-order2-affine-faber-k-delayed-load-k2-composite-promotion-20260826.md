# Promotion: delayed-load affine-Faber `K` face excluded by repaired K2 composition

Date: 2026-08-26

Status: **PROMOTED AFTER DIFFERENT-MODEL HOSTILE REVIEW OF THE REPAIRED
COMPOSITE.**

## Charged composite and reviews

```text
6178089bb11efebb304b2eb24dca6eb654bde060396fbf4f4456f515cae28989
  xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composition-exclusion-20260826.md
dc4273c7d52552402c9232a9dff90bca5b943bc6e960740c18c5c94e9ad7bdde
  xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composition-hostile-review-grok-20260826.md
7c731df0fdf699119973c2d9c80a7096adab40bec7fb95d70f10cf9b1009ff64
  xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composition-source-coordinate-addendum-v2-20260826.md
abce4bc138a52dddc09b2848c176950b50840c7b01980fa4023f0abf80961026
  xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composite-v2-hostile-review-grok-20260826.md
```

The first hostile review correctly returned **REPAIR** because the immutable
producer omitted the source-coordinate-zero/early-kernel Newton face.  The
controlling V2 addendum supplies the correct strict transform

```text
L^2*(6*u3-L*m^3)  ->  6*u3-L*m^3
```

after saturation for the closure of `D(Lambda)`.  The intermediate addendum
SHA `8b17b8c1...` has a wrong post-transform power and is superseded.  Fresh
hostile review of the producer plus controlling V2 returns **CONFIRMED**.

## Promoted theorem

In characteristic zero, on `D(D)` and on the delayed-load graph

```text
k10=Lambda^12*K10,
k6 =Lambda^8*K6,
k2 =Lambda^4*K2,
```

the complete-source exceptional affine-Faber `K` face has no formal or
Puiseux successor.

- On `D(r)`, the quartic `Q0=z^4+p*z^2+r` is squarefree.  The reviewed
  first-normal condition `Q0 | N1^2` forces `N1=0`, contradicting the
  projective `K` coordinate.
- On `r=0`, the sole first-normal survivor is
  `Q0=z^2(z^2+p)`, `N1=p*x*z*(z^2+p)`, `p*x!=0`.  It maps to the
  discriminant point `(b,e,m)=(0,p,p*x)` on `D(e*m)`, not to the square
  intersection.
- For the balanced/later source-coordinate chart `L!=0`, delayed loads have
  `kappa=0`; the reviewed e-open K2 unit and the exact lower-unitriangular
  source/analytic row bridge exclude the point before any `b` localization.
- For the early root-splitting/kernel chart `L=0`, the homogeneous rows
  `u3=-2*y*h` and `u4=h^2-e*y^2` force `y=h=x=0` on `D(e*m)`; the two unit
  complementary pivots then leave no projective leading coordinate.  This
  includes unequal and fractional valuations.

The dual sigma-through-15 moving-double-root unit is corroboration only; the
weighted strict-transform proof supplies valuative/root-splitting
exhaustiveness.

## Firewall

This theorem removes only the exceptional delayed-load affine-Faber `K` face
on `D(D)`.  The exceptional `A` face, `D=0`, other load slopes, the
exact-square/Pell receiver, the total source fan, order two, `(8,12)`, maximum
twelve, and JC2 remain open.
