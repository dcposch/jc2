# `(8,12)` order two: discriminant rank, matched obstruction, and half-weight Kuranishi map

Date: 2026-08-26

Status: **PRODUCER THEOREM FOR THE FORMULAS BELOW; THE HALF-WEIGHT
KURANISHI ZERO LOCUS IS NOT YET CLASSIFIED.  NO ORDER-TWO VERDICT.**

## 0. Frozen input and scope

This note consumes the exact one-parameter reduction, the reviewed
first-normal/principal-part theorem, and the now-reviewed Padé support
classification:

```text
5abd181a99d8e568635067320260ccc4555a3613949a600ce21560697eba1b6b
  xmodel/max12-812-order2-u2-62-oneparameter-rees-reduction-20260826.md
827e76bde5d394ab17f7c05561a1bf254b6fdf8fc3453dd60400d16e80061fdc
  xmodel/max12-812-order2-first-normal-divisibility-jet-theorem-20260826.md
27275f3d13471521bec0016d4fbc6e12d5bf8e539deeb4694fe0c01f04b025bd
  xmodel/max12-812-order2-first-normal-divisibility-jet-review-grok-20260826.md
4c9d9cfc58eb4ca2a33c9bf83beb485c15f0796fa36d2ffe4826c3fdeeac374d
  xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-20260826.md
08a5ca51461afb1753b21ee7fcf4bf8ed3719cb6edafb7d2020043ad63ab9efa
  xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-review-grok-20260826.md
2c917b9fe9af3c23d615a3f9061a5c981d26e5e69a75138aacb33f308619ecf5
  xmodel/max12-812-order2-first-normal-pade-support-theorem-20260826.md
73c30502e0466bcc6757605e5be736dabf14d2f3bfaacd302d88b94cd12dc8e6
  xmodel/max12-812-order2-first-normal-pade-support-review-grok-20260826.md
```

Thus the saturated first-normal reduced support is the union of the
square/load family and the zero-`k10` discriminant family.  The charged
principal-part identity identifies its seven rows with the first seven
negative coefficients, up to an invertible unitriangular change.

Everything below is local on the discriminant open `m!=0`.  It neither
closes the square/discriminant intersection nor asserts that a zero of the
half-weight Kuranishi map lifts to a strict arc.

## 1. Discriminant coordinates

Put

```text
A=z-a,
Q=z^2+2*a*z+d=A^2+b*A+e,
b=4*a,
e=d+3*a^2,
K0=A^2*Q,
N0=m*A*Q,                 m!=0.                    (1.1)
```

These are the discriminant parameters

```text
p=d-3*a^2,  c=2*a*(a^2-d),  r=a^2*d,
n3=m, n2=a*m, n1=(d-2*a^2)*m, n0=-a*d*m, k10=0.   (1.2)
```

The map `(a,d,m)->(p,n2,n3)` has Jacobian determinant `m`, up to
sign.  Hence on `D(m)` the five coefficient directions
`(c,r,n1,n0,k10)` form a transverse coordinate system.

## 2. The transverse Jacobian has rank three, not five

Write a transverse variation in `A` coordinates as

```text
delta K=C1*A+C0,
delta N=S1*A+S0,
delta k=k.                                             (2.1)
```

Differentiating the charged first-normal principal part

```text
(3/8)*N^2/K+k*K^(5/2)
```

at `(K0,N0,0)` gives

```text
(3/4)*m*delta N/A-(3/8)*m^2*delta K/A^2+k*H,
H=A^5*Q^(5/2).                                       (2.2)
```

The first rational summand has negative part supported only in
`A^-1,A^-2`; `S1` contributes only a polynomial.  Therefore the seven by
five transverse Jacobian has rank at most three everywhere.  On the open
where the `H` column has a nonzero coefficient in `A^-3,...,A^-7`, its
rank is exactly three.  After multiplying (2.2) by sixteen, the minor in
rows `A^-1,A^-2,A^-3` and columns `(S0,C0,k)` is
`-1152*m^3*c13`.  On the square intersection `d=a^2`, one has
`Q=(A+2*a)^2`, so `H=A^5*(A+2*a)^5` is polynomial and the rank is two.

In particular every five by five minor is identically zero.  The two
excess normal-kernel directions are exactly

```text
C0=0,
2*S0=m*C1,
k=0.                                                 (2.3)
```

In the original transverse coordinates this is

```text
delta r=-a*delta c,
delta n0=-a*delta n1+(m/2)*delta c,
delta k=0.                                           (2.4)
```

Consequently emptiness of the ordinary matched `O(Lambda)` chart cannot
be upgraded to local exclusion by a transverse-Jacobian argument.  The
missing directions naturally occur at weight one half.

## 3. Exact elimination of the ordinary matched chart

Let

```text
H=A^10*sum_(n>=0) c_n*A^-n,
(1+b*t+e*t^2)^(5/2)=sum_(n>=0)c_n*t^n.                (3.1)
```

At the next ordinary matched grade, after harmless nonzero rescaling, the
negative part is

```text
[-m^3/(16*A^3)
 +(3/4)*m*S/A
 -(3/8)*m^2*R/A^2
 +kappa*H]_- .                                       (3.2)
```

Here `R,S` are linear polynomials.  They can affect only the `A^-1` and
`A^-2` rows.  The `A^-3,A^-4,A^-5` rows are

```text
-m^3/16+kappa*c13=0,
kappa*c14=0,
kappa*c15=0.                                         (3.3)
```

The coefficients in (3.1) satisfy the differential-equation recurrence

```text
(n+1)*c_(n+1)
 = b*(5/2-n)*c_n+e*(6-n)*c_(n-1).                    (3.4)
```

Since `m!=0`, the first equation in (3.3) forces both `kappa` and `c13`
nonzero.  At `n=14`, recurrence (3.4) and `c14=c15=0` give
`e*c13=0`, hence `e=0`.  At `n=13`, the same recurrence gives
`b*c13=0`, hence `b=0`.  But then the series in (3.1) is `1`, so
`c13=0`, a contradiction.  Thus the ordinary matched discriminant chart
has no point over any characteristic-zero field.  This is an exact hand
theorem, not an inference from the dual-prime unit endpoints.

## 4. The required half-weight chart

Set the original Rees parameter to `Lambda=rho^2`.  After absorbing tangent
motion into `(a,d,m)`, put

```text
K=K0+rho*K1+rho^2*K2,
N=N0+rho*N1+rho^2*N2,
k10=rho^2*kappa,                                      (4.1)

K1=x*A,
N1=y*A+m*x/2,                                         (4.2)
```

where (4.2) is precisely the two-dimensional kernel (2.3), while `K2,N2`
are arbitrary linear polynomials.  The tail-relevant expansion is

```text
f^(3/2)
 = polynomial
 +(3/8)*Lambda^2*N^2/K
 -(1/16)*Lambda^3*N^3/K^3+O(Lambda^4),                (4.3)
```

and the `k10` load contributes
`rho^6*kappa*K0^(5/2)` at this grade.  The coefficient of `rho^6` in the
negative tail is therefore

```text
[
 (3/8)*(y*A-m*x/2)^2/(A^2*Q)
 +(3/4)*m*N2/A
 -(3/8)*m^2*K2/A^2
 -m^3/(16*A^3)
 +kappa*A^5*Q^(5/2)
]_- .                                                 (4.4)
```

Formula (4.4) is the quadratic Kuranishi map on the two excess kernel
directions, together with all complementary normal directions and the
first possible `k10` load.  Multiplying by sixteen, its first seven
`A^-j` rows can be generated without fractional-power ambiguity: use the
recurrence (3.4) for the load column and the recurrence obtained from

```text
sum r_j*t^j
 = t^2*(y-m*x*t/2)^2/(1+b*t+e*t^2)                   (4.5)
```

for the quadratic column.

## 5. Firewalls and next gate

The exact result of §3 eliminates only normal approaches whose component
equations have valuation at least `ord(Lambda)`.  Because §2 proves that
the first-normal scheme is singular along `D`, slower approaches are real
scheme-theoretic possibilities, not a technical nuisance.  The next
decisive gate is the zero locus of (4.4), first on
`m*(d-a^2)*(d+3*a^2)!=0`, then on the triple-root divisor `d+3*a^2=0`.
The square intersection `d=a^2` belongs to the separate rank-two square
analysis.

No statement here imposes the terminal `[6,2]` passport or either Taylor
boundary, constructs or excludes a strict arc beyond the stated chart,
closes exact order two, closes `(8,12)`, proves maximum twelve, or proves
JC2.
