# `(8,12)` order two: exact nonzero-load Padé lemma and complete first-normal support

Date: 2026-08-26

Status: **PRODUCER THEOREM.  THE NONZERO-`k10` PADÉ SUPPORT LEMMA IS
PROVED IN CHARACTERISTIC ZERO; HOSTILE REVIEW IS REQUIRED BEFORE
PROMOTION.**

## 0. Frozen inputs

```text
4c9d9cfc58eb4ca2a33c9bf83beb485c15f0796fa36d2ffe4826c3fdeeac374d
  xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-20260826.md
08a5ca51461afb1753b21ee7fcf4bf8ed3719cb6edafb7d2020043ad63ab9efa
  xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-review-grok-20260826.md
827e76bde5d394ab17f7c05561a1bf254b6fdf8fc3453dd60400d16e80061fdc
  xmodel/max12-812-order2-first-normal-divisibility-jet-theorem-20260826.md
27275f3d13471521bec0016d4fbc6e12d5bf8e539deeb4694fe0c01f04b025bd
  xmodel/max12-812-order2-first-normal-divisibility-jet-review-grok-20260826.md
```

The first frozen pair proves, with independently checked signs and
constants, the principal-part identity

```text
K = z^4+p*z^2+c*z+r,
N = n3*z^3+n2*z^2+n1*z+n0,
F = (3/8)*N^2/K+k10*K^(5/2),

sum_(ell>=1) q_ell*w^-ell = [F]_-^z evaluated at z=z0(w),       (0.1)
```

and proves that the change from the first seven negative `z` coefficients
to the first seven negative `w` coefficients is unitriangular.  It also
proves the exact `k10=0` UFD classification and the saturation statements
used in §4 below.  The second frozen pair supplies the exact chart and
identifies these seven `q_ell` with the first-normal gate.

All square roots and fractional powers below use the formal branch at
infinity with leading terms

```text
K^(1/2)=z^2+O(1),       K^(7/2)=z^14+O(z^12).
```

## 1. Padé lemma

Let `L` be a field of characteristic zero.  Then

```text
k10 != 0 and q1=...=q7=0   =>   c=0 and p^2=4*r.               (1.1)
```

Consequently

```text
K=(z^2+p/2)^2,                                                 (1.2)
```

so `K` is a square already over `L`, not merely after algebraic closure.

### 1.1 Removing `N`

By the unitriangular statement charged in §0, vanishing of the first
seven negative `w` coefficients is equivalent to vanishing of the first
seven negative `z` coefficients of `F`.  If `P=[F]^z_+` is the polynomial
part at infinity, this says

```text
F-P = O(z^-8).                                                  (1.3)
```

Multiply by `K` and put

```text
A=K*P-(3/8)*N^2 in L[z].                                       (1.4)
```

Then

```text
k10*K^(7/2)-A = O(z^-4).                                       (1.5)
```

Because `A` is a polynomial and `k10` is nonzero, the coefficients of
`z^-1,z^-2,z^-3` in `K^(7/2)` must vanish.  This necessary consequence
depends only on `K`; no elimination in the four coefficients of `N` is
needed.

### 1.2 Three explicit coefficients

Set

```text
t=z^-1,        d=p^2-4*r.
```

Since

```text
K^(7/2)=z^14*(1+p*t^2+c*t^3+r*t^4)^(7/2),                     (1.6)
```

the three coefficients in (1.5) are the coefficients of
`t^15,t^16,t^17` in the last factor.  Direct binomial expansion gives

```text
[t^15] = (7*c/2048)*A0,
[t^16] = (35/32768)*C0,
[t^17] = (7*c/4096)*B0,                                       (1.7)
```

where

```text
A0 = -5*d^3+40*p*c^2*d-8*c^4,
B0 =  5*p*d^3-10*c^2*d*(d+4*p^2)+24*p*c^4,
C0 =  d^4-48*p*c^2*d^2+32*c^4*(d+2*p^2).                     (1.8)
```

For an auditable coefficient check, before the substitution
`d=p^2-4*r` the numerators of (1.7) are

```text
2048*[t^15]
 = 7*c*(320*r^3-8*c^4-160*p*c^2*r-240*p^2*r^2
        +40*p^3*c^2+60*p^4*r-5*p^6),

32768*[t^16]
 = 35*(256*r^4-128*c^4*r-768*p*c^2*r^2-256*p^2*r^3
       +96*p^2*c^4+384*p^3*c^2*r+96*p^4*r^2
       -48*p^5*c^2-16*p^6*r+p^8),

4096*[t^17]
 = 7*c*(-160*c^2*r^2-320*p*r^3+24*p*c^4
        +240*p^2*c^2*r+240*p^3*r^2-50*p^4*c^2
        -60*p^5*r+5*p^7).                                    (1.9)
```

Expanding (1.8) recovers (1.9), so (1.7) can also be checked without a
factorization oracle.

### 1.3 Elementary contradiction off the square locus

Equation (1.5) makes all three expressions in (1.7) zero.

If `c=0`, then `C0=d^4=0`, hence `d=0` and (1.1) follows.

Suppose instead that `c!=0`.  Then `A0=B0=0`.  Their combination is

```text
B0+p*A0 = 2*c^2*(-5*d^2+8*p*c^2),                             (1.10)
```

so

```text
p*c^2=(5/8)*d^2.                                               (1.11)
```

Substitution into `A0=0` gives

```text
c^4=(5/2)*d^3.                                                 (1.12)
```

Finally, (1.11)--(1.12) turn the third equation into

```text
C0
 = d^4-48*(5/8)*d^4+32*c^4*d+64*(p*c^2)^2
 = 76*d^4.                                                     (1.13)
```

Characteristic zero and `C0=0` imply `d=0`; then (1.12) implies `c=0`,
contrary to the case assumption.  The case `c!=0` is impossible.  This
proves (1.1).

## 2. Exact raw support

Work geometrically after base change to an algebraic closure of `L`.  Let

```text
I=(q1,...,q7).
```

Define the following closed sets:

```text
Lsq: K=(z^2+s)^2,
     N=(z^2+s)*(alpha*z+beta),
     k10 arbitrary;

D:   K=(z-a)^2*(z^2+2*a*z+e),
     N=lambda*(z-a)*(z^2+2*a*z+e),
     k10=0;

Z:   N=0,
     k10=0,
     K arbitrary.                                              (2.1)
```

Then

```text
V(I)_red = Lsq union D union Z.                                (2.2)
```

Indeed, on `k10=0` this is exactly the charged UFD classification.  On
`k10!=0`, §1 forces `K` to be square.  For square `K`, the
`k10*K^(5/2)` term is a polynomial, so vanishing of the first gate is
equivalent to the charged condition `K|N^2`; equivalently the quadratic
square root of `K` divides `N`.  This is precisely `Lsq`.  Conversely,
each family in (2.1) satisfies all seven rows by the charged identities.

In affine coordinates `Lsq` is the closed locus

```text
c=0,  p^2=4*r,  2*n1=p*n3,  2*n0=p*n2,                       (2.3)
```

with arbitrary `k10`.  Thus no closure claim is hidden in (2.2).

## 3. Complete saturated first-normal support

Retain the charged notation

```text
Aideal=(p,c,r),
Bideal=(n0,n1,n2,n3,k10),
Istar=((I:Aideal^infinity):Bideal^infinity).                   (3.1)
```

Then

```text
V(Istar)_red = Lsq union D.                                    (3.2)
```

The component `Z` in (2.2) is supported wholly on `V(Bideal)` and is
deleted.  Both `Lsq` and `D` meet the complements of `V(Aideal)` and
`V(Bideal)` densely, so saturation retains their full affine closures.
This also makes the residual set `E` of the frozen V2 erratum empty and
recovers, unconditionally,

```text
V(Istar)_red intersect V(k10) = S union D.                     (3.3)
```

Here `S=Lsq intersect V(k10)` is the square family used in the frozen
erratum.

## 4. What this closes and what remains

The nonzero-load Padé gap in the exact first-normal gate is closed.  The
complete reduced support of that gate consists of the arbitrary-load square
family and the zero-load discriminant family.

This does **not** show that either family lifts through the next divided
jet, realizes a strict `Lambda!=0` arc, or satisfies the terminal `[6,2]`
passport and the two Taylor boundaries.  It does not control arcs whose
first normal/load contact occurs after order one.  Therefore it does not
exclude order two, close `(8,12)`, prove maximum twelve, or prove JC2.
