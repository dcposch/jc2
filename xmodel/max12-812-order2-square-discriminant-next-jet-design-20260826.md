# `(8,12)` order two: componentwise next divided jets on the square and discriminant strata

Date: 2026-08-26

Status: **SOURCE-TYPED AWS DESIGN; MATCHED-VALUATION CHARTS ONLY; NO
ORDER-TWO VERDICT.**

## 1. Charged source

The design consumes the reviewed one-parameter family and first-normal
theorem, together with the corrected principal-part/UFD support theorem:

```text
5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md
827e76bde5d394ab17f7c05561a1bf254b6fdf8fc3453dd60400d16e80061fdc
  xmodel/max12-812-order2-first-normal-divisibility-jet-theorem-20260826.md
4c9d9cfc58eb4ca2a33c9bf83beb485c15f0796fa36d2ffe4826c3fdeeac374d
  xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-20260826.md
08a5ca51461afb1753b21ee7fcf4bf8ed3719cb6edafb7d2020043ad63ab9efa
  xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-review-grok-20260826.md
```

Write `Phi_l=Lambda^2 Theta_l`.  The first boundary rows are
`q_l=Theta_l mod Lambda`.  Provisionally consuming the separately reviewed
nonzero-`k10` Padé lemma, the geometric first-normal support has only the
square/load component and the `k10=0` discriminant component.

## 2. Square/load chart `Lsq`

The square component is the smooth affine four-space

```text
c=0,
4r-p^2=0,
2n1-p*n3=0,
2n0-p*n2=0,
```

with coordinates `(p,n2,n3,k10)`.  Its source-relevant first-contact open is

```text
p != 0,
(n2,n3,k10) != (0,0,0).
```

The exact matched-valuation normal chart is

```text
c=Lambda*cs,
r=(p^2+Lambda*rs)/4,
n1=(p*n3+Lambda*v1)/2,
n0=(p*n2+Lambda*v0)/2.                         (2.1)
```

On `D(Lambda)`, (2.1) is invertible with
`cs=c/Lambda`, `rs=(4r-p^2)/Lambda`,
`v1=(2n1-p*n3)/Lambda`, and `v0=(2n0-p*n2)/Lambda`.
The arbitrary value of `k10` is retained.  The compiler must verify, rather
than assume, that every pulled `Phi_l` is divisible by `Lambda^3`, then form

```text
Lsq_l=(Phi_l after (2.1))/Lambda^3 mod Lambda.         (2.2)
```

It saturates only by the declared base opens, not by the four transverse
variables; their common zero is the still-live higher-contact section.

## 3. Nonsquare discriminant chart `D`

On the nonzero-normal open the discriminant component has `lambda!=0` and

```text
p=d-3a^2,
c=2a(a^2-d),
r=a^2*d,
n3=lambda,
n2=a*lambda,
n1=(d-2a^2)*lambda,
n0=-a*d*lambda,
k10=0.                                                (3.1)
```

The coordinates `(p,n3,n2)` have Jacobian determinant `lambda` with respect
to `(d,lambda,a)`, so tangent motion is absorbed exactly on `D(lambda)`.
The five matched transverse coordinates are

```text
c=2a(a^2-d)+Lambda*cs,
r=a^2*d+Lambda*rs,
n1=(d-2a^2)*lambda+Lambda*v1,
n0=-a*d*lambda+Lambda*v0,
k10=Lambda*kappa.                                    (3.2)
```

The source open also excludes `(a,d)=(0,0)`.  The intersection with the
square component is `d=a^2`; this first D client localizes away from it,
assigning the intersection to the square lane.  The compiler forms

```text
D_l=(Phi_l after (3.2))/Lambda^3 mod Lambda           (3.3)
```

only after exact divisibility checks, then saturates successively by
`lambda`, `(a,d)`, and `d-a^2`.

## 4. Valuation firewall

These charts cover arcs for which the four or five component equations have
valuation at least `ord(Lambda)`.  They are the generic next Kuranishi jet
when the first-normal rows cut the selected smooth component transversely.
They do not automatically cover slower transverse approach at a
scheme-singular point, the square/discriminant intersection, or a ramified
Puiseux slope.  Such loci require an exact Jacobian/transversality lemma or
separate weighted Rees charts.  A unit endpoint in either matched chart is
therefore not complete component exclusion without that closure argument.

The clients retain the zero-transverse section and all lower/target loads
until the compiler proves they are absent from this grade.  They do not
project finite loads, impose the terminal `[6,2]` passport or either Taylor
boundary, construct/exclude a strict arc, close order two, close `(8,12)`,
prove maximum twelve, or prove JC2.
