# Endpoint-survivor parametrization and codimension — R6

Date: 2026-08-27  
Author: Sol / coordinator  
Status: **PROVISIONAL PRODUCER THEOREM; DEPENDS ON R5 REVIEW**

## Result

The R5 endpoint criterion does more than exclude a generic leading
polynomial: it explicitly parametrizes every survivor and cuts the monic
degree-`h` coefficient space by at least `floor(h/2)` dimensions.

Work over an algebraically closed characteristic-zero field and let `H` be
monic of degree `h`.  Write uniquely

```text
H=A^2B,
```

with monic `A` and monic squarefree `B`; put `a=deg A`, `b=deg B`, so
`2a+b=h`.  For `b>=1`, R5 says the rational endpoint survives exactly when

```text
A=N_B(v):=Bv'+(3/2)B'v.                              (0.1)
```

If it survives, necessarily

```text
r:=deg v=a-b+1=(h-3b+2)/2 >= 0.                      (0.2)
```

Conversely, choose a monic squarefree degree-`b` polynomial `B` and a
degree-`r` polynomial `v` whose leading coefficient is fixed so that
`N_B(v)` is monic.  Then

```text
H=N_B(v)^2 B                                           (0.3)
```

is exactly an endpoint survivor with squarefree part `B`.  Thus (0.3) is a
complete normalized parametrization, not merely a necessary equation.

For fixed positive `b`, the stratum has dimension

```text
b+r=a+1=(h-b+2)/2
```

and codimension in the monic degree-`h` space

```text
h-(a+1)=(h+b-2)/2.                                   (0.4)
```

If `b=0`, the perfect-square endpoint is always rationally soluble and the
stratum `H=A^2` has dimension `h/2` and codimension `h/2`.

It follows that the full rational-endpoint survivor locus has codimension at
least

```text
floor(h/2).                                           (0.5)
```

The generic squarefree `H` lies far outside it.  This converts the endpoint
theorem into a concrete search compiler: future raw-support or landing tests
should parameterize `(B,v)` and form (0.3), rather than search all `h`
coefficients of `H`.

## Proof

For `b>=1`, the degree law is

```text
deg N_B(v)=deg v+b-1,
lc N_B(v)=(r+(3/2)b) lc(v),                           (1.1)
```

so `N_B` is injective and (0.2) is forced.  Once `B` is monic, the nonzero
coefficient in (1.1) fixes the leading coefficient of `v`; its remaining
`r` coefficients and the `b` free coefficients of monic `B` give dimension
`b+r=a+1`.  The decomposition of a monic `H` into `A^2B` is unique, and
`N_B` is injective, so the normalized map `(B,v)->H` is injective on this
squarefree-`B` stratum.  Hence the dimension count is exact.

The degree-survival condition `r>=0` is equivalent to

```text
3b<=h+2.                                              (1.2)
```

For even `h`, `b=0` gives codimension `h/2`, while every positive allowed
`b` has codimension at least `h/2`.  For odd `h`, the least possible
`b=1` has codimension `(h-1)/2`, and every larger allowed `b` has greater
codimension.  This proves (0.5).

Shared factors of `A` and `B` cause no ambiguity: their exponent in
`A^2B` remains odd, so they correctly stay in the squarefree part.  The
parametrization is constructible because only the open discriminant
condition on `B` is added.

## Degree eight

For `h=8`, parity permits `b=0,2,4,6,8`.  Condition (1.2) leaves exactly:

```text
b=0: H=A^2,                    deg A=4, dimension 4;
b=2: H=N_B(v)^2 B,             deg B=2, deg v=2, dimension 4.
```

Both are codimension four in the eight-dimensional monic coefficient space.
The `b=4,6,8` strata are empty at the rational endpoint.  In centered
quadratic coordinates, the `b=2` parametrization is equivalent to R5's sole
linear cokernel equation `4a0+D*a2=0`.

## Strategic use and firewall

If R5 passes review, (0.3) should replace ambient leading-`H` searches in
the raw `2S/3S` and other common-square/cube edge clients.  For degree eight
it halves the leading parameter dimension before any determinant recurrence
is compiled.  It also provides a finite constructible atlas indexed by `b`,
which can be sharded independently on AWS.

R6 inherits R5's rollback.  It parameterizes rational endpoint survivors
only.  It proves neither that a survivor extends to a formal jet nor that a
formal jet is a polynomial/source object.  It supplies no GGV landing or
family exclusion, global automorphism, `G2-PSC`, `G2-BD`, cofinal degree
bound, counterexample, or JC2 result.
