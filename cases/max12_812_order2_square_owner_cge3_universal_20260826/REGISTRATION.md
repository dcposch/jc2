# Registration: universal `c>=3`, `r>=1` generic-square receiver

Date: 2026-08-26

Work on the reviewed generic-square chart `D(p*k0)` after the half-weight
radical has forced the leading `C` and `R` sections to vanish.  Put

```text
Lambda=sigma^2,
K=L(sigma)^2+sigma^2 R(sigma),
D=L(sigma) A(sigma)+C(sigma),
L(sigma)=z^2+p(sigma)/2,
ord_sigma(C)>=3, ord_sigma(R)>=1.
```

The compiler retains every coefficient which can enter absolute grades
13--15:

```text
p=p0+2 sigma ell1+2 sigma^2 ell2,
A=A0+sigma A1+sigma^2 A2,
R=sigma B1+sigma^2 B2+sigma^3 B3,
C=sigma^3 E3+sigma^4 E4+sigma^5 E5,
k10=k0+sigma k1+sigma^2 k2corr.
```

It reconstructs all seven frozen loaded Faber rows, proves exact division
through grades 13, 14 and 15, and compares them coefficientwise with the
negative Laurent part of

```text
 (3/4) sigma^10 A C/L
-(3/8) sigma^12 R A^2/L^2
-(1/16)sigma^15 A^3/L^3
+(5/16)sigma^10 k R^3/L
+(5/8) sigma^11 k R C/L
-(5/32)sigma^13 k R^2 A/L^2
+(5/32)sigma^14 k A^2/L.
```

The row change is the exact lower-unitriangular `q^2+(p(sigma)/2)v^2=1`
change, expanded through second order in `sigma`.  For the common numerator
over `L(sigma)^3`, the compiler recursively removes the polynomial parts at
grades 13 and 14.  Its grade-15 reduction modulo `L(0)` must then equal
`-A0^3`.  This is the moving-base divisibility correction: derivatives of
lower-grade polynomial parts are absorbed before the final reduction.

On PASS, seven zero source rows at each grade force the three Laurent
coefficients to be polynomial.  Hence `L(0)|A0^3`; on `D(p)`, the squarefree
quadratic `L(0)` cannot divide the cube of a linear polynomial unless
`A0=0`.

The exact-Q lane is the proof-producing gate.  `F_65521` is an independent
control only.  Use 32 GiB VM, 10-minute compiler and two-hour engine caps on
registered AWS hosts.  Any mismatch, diagnostic, timeout, or nonzero exit is
no verdict.

This package addresses only `c>=3,r>=1` on the generic square chart after
the reviewed first-normal and half-weight gates.  The `c=1,2` rays, `p=0`
square/discriminant intersection, terminal and Taylor receivers, square
branch closure, order-two closure, `(8,12)`, maximum twelve, and JC2 remain
outside its scope.
