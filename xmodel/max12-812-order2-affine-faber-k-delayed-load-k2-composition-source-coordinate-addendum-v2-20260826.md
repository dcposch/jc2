# V2 repair: strict-transform source coordinate in the delayed-load affine-Faber `K` to K2 composition

Date: 2026-08-26

Status: **CONTROLLING NONMUTATING WORDING REPAIR; HOSTILE REVIEW REQUIRED.**

## 0. Repaired artifact

This note corrects one homogenization sentence in

```text
8b17b8c116d1e3a9c5858713b91837d10216f540fe30d2f72a2c6482d01a874a
  xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composition-source-coordinate-addendum-20260826.md
```

and is controlling wherever the two differ.  The set-theoretic `L=0/1`
dichotomy and the `u3,u4` calculation in that addendum are unchanged.

## 1. Correct strict-transform derivation

Before strict transform, substitute

```text
Lambda=rho^2*L.
```

At total rho degree six, the quadratic kernel term carries `L^2` and the
intrinsic cubic term carries `L^3`.  Thus the undivided high row has the
common source factor

```text
L^2*(6*u3-L*m^3),                                  (1.1)
```

up to the same harmless nonzero scalar convention as the charged K2
formula.  The campaign studies the strict transform/closure of
`D(Lambda)`, so the total-transform factor `L^2` is removed by the source
saturation.  The controlling strict-transform row is therefore

```text
6*u3-L*m^3,                                        (1.2)
```

not `6*u3-L^3*m^3`.  The remaining high rows have the corresponding
strict-transform quadratic kernel coefficients `6*u4,...,6*u7`; on the
delayed-load source-zero face the graph gives no load contribution at this
grade.

Equivalently: the quadratic kernel expression is `L`-independent only
*after* removing the universal `L^2` total-transform factor, and the cubic
intrinsic term is then linear in `L`.

## 2. Consequences

- On `L=1`, (1.2) is the reviewed row `6*u3-m^3`; the K2 unit argument is
  unchanged.
- On `L=0`, (1.2) is `u3=0`, followed by `u4=0`.  At `b=0,e` a unit,
  `u3=-2*y*h` and `u4=h^2-e*y^2`, so `y=h=0`, then `x=0` from
  `h=m*x/2`; the complementary unit pivots remove the remaining
  projective coordinates.  The omitted source-zero face is still empty.

Therefore the repaired target's delayed-load `K` exclusion survives.  No
new scheme identity, load slope, `A`-face, order-two, or JC2 claim is made.
