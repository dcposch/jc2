# Internal adversarial audit: delayed-load affine-Faber `K` face to K2

Date: 2026-08-26

Status: **THE ORIGINAL PRODUCER NEEDS ITS TWO SOURCE-COORDINATE ADDENDA;
THE COMPOSITE WITH THE CONTROLLING V2 ADDENDUM IS CONFIRMED.**

## 0. Targets and verdict

The frozen producer is

```text
6178089bb11efebb304b2eb24dca6eb654bde060396fbf4f4456f515cae28989
  xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composition-exclusion-20260826.md
```

Its weighted-blowup paragraph omits the projective face on which the local
normal/source coordinate is zero.  Thus the producer **alone** needs repair.
The first nonmutating repair is

```text
8b17b8c116d1e3a9c5858713b91837d10216f540fe30d2f72a2c6482d01a874a
  xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composition-source-coordinate-addendum-20260826.md
```

It identifies the right missing face and the right equations there, but its
claim that the strict-transform intrinsic term is `-L^3*m^3` is not the
correct homogenization.  The controlling repair is

```text
7c731df0fdf699119973c2d9c80a7096adab40bec7fb95d70f10cf9b1009ff64
  xmodel/max12-812-order2-affine-faber-k-delayed-load-k2-composition-source-coordinate-addendum-v2-20260826.md
```

It gives the correct undivided factor

```text
L^2*(6*u3-L*m^3)
```

and the correct strict-transform row

```text
6*u3-L*m^3.
```

With that V2 controlling, the missing source-coordinate face is empty and
the producer's narrow `K`-face conclusion is valuatively exhaustive.  I find
no surviving root-splitting or fractional-order counterface.

## 1. First-normal split and repeated point

Put

```text
Q0=z^4+p*z^2+r,
D=(p^2-4*r)/4,
N0=y*z^3+(2*D*x+(p/2)*y)*z.
```

On `D(D)`, if `r` is a unit, the quartic discriminant is a nonzero scalar
multiple of `r*D^2`; hence `Q0` is squarefree.  The reviewed condition
`Q0 | N0^2` then gives `Q0 | N0`, and `deg N0<4` gives `N0=0`.  Its two
coefficients force `y=0` and then `x=0`, contrary to projectivity.

If `r=0`, then `D=p^2/4` and `p` is a unit.  Now

```text
Q0=z^2*(z^2+p).
```

The factor `z^2` forces `z | N0`, already visible, and the coprime
squarefree factor `z^2+p` forces

```text
2*D*x-(p/2)*y=0,
```

or `y=p*x`.  Consequently

```text
N0=p*x*z*(z^2+p),                 p*x != 0.
```

In the discriminant coordinates

```text
A=z-a,
K0=A^2*(A^2+b*A+e),
N0=m*A*(A^2+b*A+e),
```

this is exactly

```text
(a,b,e,m)=(0,0,p,p*x).
```

Thus `e*m` is a unit.  This is not the routed square intersection
`b=e=0`.

## 2. Tangent absorption and the actual weighted valuation

The discriminant family is smooth at this point.  The map

```text
(a,d,m) -> (p,n2,n3)
```

has determinant `-m` up to ordering, so after a common ramification every
root-preserving tangent series is absorbed uniquely into moving
`a(s),d(s),m(s)`.  The remaining transverse Jacobian has the two-dimensional
kernel

```text
delta K=x*A,
delta N=y*A+m*x/2,
delta k=0,
```

and two source-accessible complementary coordinates; the third analytic
complement is the first load coordinate, which is zero on this delayed
predecessor.

It is useful to distinguish the global one-parameter source coordinate
from the local radial normal coordinate.  Write the latter as `tau`.  The
K-ray has the primitive relation

```text
Lambda_global=sigma^3,       t=sigma^5,
```

so its unloaded first-normal and K2 grades are respectively `t^2=sigma^10`
and `t^3=sigma^15`.  The delayed effective lower loads first occur at
`Lambda_global^14=sigma^42`.  Therefore the local K2 predecessor really has
`kappa=0`; neither an earlier fractional correction nor the exact tie can
import a delayed load.

After the first-normal `tau^2` total factor has been divided out, assign

```text
weight(kernel)=1,
weight(complement)=2,
weight(tau)=2.
```

For a DVR arc let

```text
alpha = minimum valuation of a kernel coordinate,
beta  = minimum valuation of a complementary coordinate,
gamma = valuation of tau.
```

After further finite ramification, use a weighted scale whose doubled
valuation is

```text
delta=min(2*alpha,beta,gamma).
```

At least one leading kernel, complement, or source coordinate is nonzero.
If `gamma=delta`, the leading source coordinate `L` is nonzero and can be
normalized to one after the permitted ramification.  If `gamma>delta`, its
leading coordinate is `L=0`.  These are all relative valuations; in
particular, a kernel/root-splitting correction earlier than the half-weight
tie is exactly the `L=0` face, while a later correction appears on the
`L!=0` face with zero leading kernel coordinate.

The strict-transform formula matters here.  Before source saturation,
`tau=rho^2*L` gives at total `rho` degree six

```text
L^2*(6*u3-L*m^3),
```

not `6*u3-L^3*m^3`.  Saturating the closure of `D(tau)` removes the common
`L^2` total-transform factor, leaving

```text
6*u3-L*m^3.
```

This is precisely the correction made by the controlling V2 addendum.

## 3. The omitted `L=0` face

After the two unit complementary pivots, the five high rows on `L=0` and
`kappa=0` are `u3=...=u7=0`, where

```text
sum u_n*T^n = T^2*(y-h*T)^2/(1+b*T+e*T^2),
h=m*x/2.
```

At the repeated K point `b=0`, direct expansion gives

```text
u2 = y^2,
u3 = -2*y*h,
u4 = h^2-e*y^2,
u5 = 2*e*y*h,
u6 = e^2*y^2-e*h^2,
u7 = -2*e^2*y*h.
```

Over the residue field, `u3=u4=0` and `e!=0` imply

```text
y*h=0,
h^2=e*y^2,
```

and hence `y=h=0`.  Since `m` is a unit, `h=m*x/2` gives `x=0`.  Once the
quadratic kernel coordinates vanish, the two low rows, whose complementary
diagonal pivots are nonzero rational multiples of `m` and `m^2`, force both
source-accessible complement coordinates to vanish.  The delayed graph
already gives `kappa=0`.  Thus every projective coordinate vanishes, a
contradiction.  This proves emptiness of the source-zero face, including
unequal kernel valuations and an earlier root-splitting lead.

Positive-valuation motion of `b,e,m` does not change this initial form:
their residues remain `0,p,p*x`, with `e*m` a unit, and every term containing
the positive-valuation `b` is strictly later.

## 4. The `L!=0` face and coordinate subfaces

Normalize `L=1`.  The strict-transform rows are the reviewed analytic K2
rows.  The exact V3 lower-unitriangular identity identifies their ideal with
the complete frozen-source K2 ideal before any `b` localization.  In

```text
R_m=Q[b,e,h,y,kappa,m][m^(-1)]
```

the reviewed support theorem gives

```text
((I_K2+(kappa)):e^infinity)=(1).
```

At the repeated point `e*m` is a unit and the delayed graph has `kappa=0`,
so no K2 point exists.  The other reviewed identity

```text
(I_K2:kappa^infinity)=(1)
```

would also exclude a hypothetical tied nonzero load, although that chart is
not needed for the delayed timing.

This includes the later-than-half-weight coordinate face: if all kernel
coordinates have valuation larger than half the local source valuation,
their K2 leading coordinates are zero, while `L=1`; the intrinsic
`-m^3` row and the unit ideal still exclude the point.  If a complementary
coordinate leads strictly before both the kernel square and `tau`, its unit
linear pivot gives an even earlier contradiction.  Hence there is no third
valuation regime between the two source-coordinate cases.

## 5. Reconciliation with the sigma-through-15 computation

The frozen finite recursion has

```text
2ce2cb39f671fbfb545a5e9f44b6a0a75927b3624f0a6b87eecf80685f28dfe1
  cases/max12_812_order2_affine_faber_k_moving_discriminant_sigma15_20260826/RESULT.md
```

It permits arbitrary moving-double-root parameters through sigma order five
and arbitrary normal corrections at orders six through ten, and obtains the
unit ideal from all rows in grades ten through fifteen on `D(p*lam)`.
That is consistent corroboration of the root-preserving integral charts.
It does not contain a half-integral correction at the exact half-weight tie
and it keeps the quartic on the moving discriminant, so it does not certify
the root-splitting or arbitrary-Puiseux cases.  Sections 2--4 above supply
exactly those missing cases; no conclusion here is inferred from the finite
recursion alone.

## 6. Custody and scope

Additional consumed exact artifacts rehash as follows:

```text
4c9d9cfc58eb4ca2a33c9bf83beb485c15f0796fa36d2ffe4826c3fdeeac374d
  xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-20260826.md
2c917b9fe9af3c23d615a3f9061a5c981d26e5e69a75138aacb33f308619ecf5
  xmodel/max12-812-order2-first-normal-pade-support-theorem-20260826.md
ddbc758039621f70eae586b5482be3bfdd92754e990cdb015fa4c6d2e0eac0b1
  xmodel/max12-812-order2-discriminant-rank-halfweight-kuranishi-20260826.md
f1cbb203ca26c66c3c57178460912610ba978206043b2bf22bc1b2b73aaac68b
  xmodel/max12-812-order2-discriminant-halfweight-k2-support-theorem-v2-20260826.md
d0327db2e2214bc897be85d4373bf35e063c2a540254b2b33986f88755eca0e8
  cases/max12_812_order2_disc_halfweight_kuranishi_v3_row_identity_20260826/RESULT.md
5f752982019a94d335bafa9bfdb34f372d8dd95ad69e902d0570fece7e2b9a4a
  cases/max12_812_order2_affine_faber_k_delayed_source_cubic_20260826/RESULT.md
```

The exact-Q identities are the characteristic-zero evidence.  Finite-field
lanes are software controls only.

The confirmed composite statement is confined to the projective exceptional
affine-Faber `K` face on `D(D)` for this delayed-load source ray.  It does not
cover the `A` face, `D=0`, another load slope, the square/Pell receiver,
terminal or Taylor gates on other branches, order two, `(8,12)`, maximum
twelve, or JC2.

**Composite verdict (producer + controlling V2 addendum): CONFIRMED.**
