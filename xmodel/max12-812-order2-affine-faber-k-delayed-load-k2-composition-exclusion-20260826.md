# `(8,12)` order two: delayed-load affine-Faber `K` face excluded by discriminant K2 composition

Date: 2026-08-26

Status: **PRODUCER COMPOSITION THEOREM PENDING HOSTILE REVIEW.**

## 0. Charged theorems and exact source bridge

Reviewed first-normal divisibility and support:

```text
4c9d9cfc58eb4ca2a33c9bf83beb485c15f0796fa36d2ffe4826c3fdeeac374d
  xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-20260826.md
08a5ca51461afb1753b21ee7fcf4bf8ed3719cb6edafb7d2020043ad63ab9efa
  xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-review-grok-20260826.md
2c917b9fe9af3c23d615a3f9061a5c981d26e5e69a75138aacb33f308619ecf5
  xmodel/max12-812-order2-first-normal-pade-support-theorem-20260826.md
73c30502e0466bcc6757605e5be736dabf14d2f3bfaacd302d88b94cd12dc8e6
  xmodel/max12-812-order2-first-normal-pade-support-review-grok-20260826.md
```

Reviewed analytic discriminant K2 support, with its controlling scope
repair:

```text
20fa404c10c6fdafe59247967db8234f3479ae9a06740b521650b8a8aa88e341
  xmodel/max12-812-order2-discriminant-halfweight-k2-support-theorem-20260826.md
f93ecb4320fadff500638fc6fa7bdfca904ed5556b7a13add4cddb9b40a76b70
  xmodel/max12-812-order2-discriminant-halfweight-k2-support-review-terra-20260826.md
f1cbb203ca26c66c3c57178460912610ba978206043b2bf22bc1b2b73aaac68b
  xmodel/max12-812-order2-discriminant-halfweight-k2-support-theorem-v2-20260826.md
```

Exact complete-source/analytic K2 row equality:

```text
6e00100d10f5d05b5351d2ca7fd8535a9b0df49671860d51862b73d64e6319c9
  cases/max12_812_order2_disc_halfweight_kuranishi_v3_row_identity_20260826/FREEZE.sha256
d0327db2e2214bc897be85d4373bf35e063c2a540254b2b33986f88755eca0e8
  cases/max12_812_order2_disc_halfweight_kuranishi_v3_row_identity_20260826/RESULT.md
6eb104a3288bf663aced9b8aa6f0bdac3a91c9cb6bd26d44e4b4989a5efe7c36
  cases/max12_812_order2_disc_halfweight_kuranishi_v3_row_identity_20260826/RESULTS.sha256
```

The V3 identity is polynomial and lower unitriangular: for all seven rows,
`16*S_l=sum_(j<=l)T_(l,j)(b,e)*H_j`.  Thus the reviewed analytic K2 ideal
is the complete frozen-source K2 ideal after every localization used below.

## 1. The affine-Faber `K` initial normal

Put

```text
Q0=z^4+p*z^2+r,
D=(p^2-4*r)/4,
N1=y*z^3+(2*D*x+(p/2)*y)*z.                       (1.1)
```

Work on the exceptional affine-Faber `K` face on `D(D)`; its projective
coordinate satisfies `(x,y)!=(0,0)`.  The unloaded predecessor is the
reviewed exact condition

```text
Q0 divides N1^2.                                    (1.2)
```

If `r` is a unit, `Q0` is squarefree because its discriminant is a nonzero
multiple of `r*D^2`.  Then (1.2) forces `N1=0`, and (1.1) forces
`x=y=0`, contradicting projectivity.  This disposes of the squarefree
open without any higher-jet argument.

It remains to consider the special fibre `r=0`.  There `D=p^2/4`, so `p`
is a unit, and

```text
Q0=z^2*(z^2+p),
(1.2)  iff  y=p*x,
N1=p*x*z*(z^2+p),
p*x != 0.                                           (1.3)
```

In discriminant coordinates

```text
A=z-a,
Q0=A^2*(A^2+b*A+e),
N1=m*A*(A^2+b*A+e),                                (1.4)
```

the point (1.3) is exactly

```text
a=0,  b=0,  e=p,  m=p*x.                           (1.5)
```

In particular both `e` and `m` are units.  Although `b=0`, this is not
the routed square intersection `b=e=0`; it lies in the `e`-unit K2 chart.

## 2. K2 unit at the repeated-root point

Let `I_K2` be the complete source K2 ideal, identified with the analytic
ideal by the V3 bridge.  In

```text
R_m=Q[b,e,h,y,kappa,m][m^(-1)]
```

the reviewed support theorem gives

```text
(I_K2:kappa^infinity)=(1),
((I_K2+(kappa)):e^infinity)=(1).                    (2.1)
```

The delayed source loads

```text
k10=Lambda^12*K10,
k6 =Lambda^8*K6,
k2 =Lambda^4*K2                                     (2.2)
```

arrive strictly after this unloaded predecessor, so their K2 initial
coordinate is `kappa=0`.  Equations (1.5) and the second identity in (2.1)
therefore make the complete source K2 ideal the unit ideal.  In fact the
first identity in (2.1) shows that a load tying this K2 face with
`kappa!=0` could not restore it either.

## 3. Valuative exhaustiveness, including root splitting

We record the normalized-blowup lemma used in this composition.  Let a
formal or Puiseux source arc have the first nonzero square-normal initial
form (1.3).  Pass to a common ramified DVR.  On `D(m)`, the discriminant
first-normal component is smooth in its parameters `(a,d,m)`: the map to
coefficient coordinates has Jacobian determinant `m`, up to sign.
Consequently every root-preserving tangent jet can be absorbed uniquely,
order by order, into moving series `a(s),d(s),m(s)`.

Transversely, the exact first-normal Jacobian has three unit pivots and a
two-dimensional kernel

```text
delta K=x*A,
delta N=y*A+(m*x)/2,
delta k=0.                                          (3.1)
```

Give the two kernel coordinates weight one and the three complementary
coordinates, including the first load coordinate, weight two.  For any
remaining DVR deformation, choose the least weighted valuation.  If a
complementary coordinate occurs below twice the kernel order, its leading
linear pivot is nonzero and the arc already fails an earlier initial row.
Otherwise, after ramification and division by the least weighted power,
the leading coefficients define a point of the half-weight K2 chart.  If
all kernel coordinates have larger order, their leading coefficients are
zero: this is a coordinate face of the same K2 chart, not a missing
ordinary chart.  The intrinsic `-m^3` term prevents an all-zero escape.

This argument also covers root splitting.  A motion that splits the double
root is precisely a transverse quartic coefficient after tangent motion
inside `(a,d,m)` has been removed.  It either meets an earlier linear pivot
or supplies a kernel/complement leading coefficient in (3.1), hence a K2
point.  It cannot bypass (2.1) by occurring at a fractional intermediate
sigma order.  Root-preserving intermediate jets are absorbed; root-splitting
jets are seen by the weighted initial ideal.

Thus every formal/Puiseux successor of (1.3), with arbitrary intermediate
normal, tangent, centre, and load jets, has a necessary K2 point on
`D(e*m)`.  The reviewed unit identities say that no such point exists.

## 4. Conclusion

Combining Sections 1--3:

> On `D(D)`, the entire projective exceptional affine-Faber `K` face for
> the delayed-load source ray is empty at a necessary complete-source
> gate.  The `r!=0` open is killed by reviewed first-normal UFD
> divisibility; the `r=0` fibre, including every root-preserving and
> root-splitting ramified correction, is killed by the reviewed K2 unit on
> `D(e*m)` plus the exact V3 source/analytic row bridge.

No terminal `[6,2]` row or finite Taylor pullback is required for this
face: later equations cannot restore a branch whose necessary K2 ideal is
the unit ideal.

## 5. Independent finite-recursion corroboration and firewall

A dual-AWS correction-complete moving-double-root recursion through sigma
grade 15 independently prints the unit standard basis on `D(p*lam)`:

```text
2ce2cb39f671fbfb545a5e9f44b6a0a75927b3624f0a6b87eecf80685f28dfe1
  cases/max12_812_order2_affine_faber_k_moving_discriminant_sigma15_20260826/RESULT.md
7f94b11f3527927e34b94a53d3b1bdb6c236a9c18d42f80a52dafe7bb7fd2133
  cases/max12_812_order2_affine_faber_k_moving_discriminant_sigma15_20260826/EVIDENCE.sha256
```

That finite computation is corroboration only; the K2 normalized-blowup
composition supplies the root-splitting and arbitrary-fractional-jet
exhaustiveness.

This theorem is scoped to the exceptional affine-Faber `K` face on
`D(D)` for the delayed-load source ray.  It does not exclude the exceptional
`A` face, the divisor `D=0`, other unregistered source/load slopes, the
remaining exact-square/Pell receiver, the total order-two fan, order two,
`(8,12)`, maximum twelve, or JC2.
