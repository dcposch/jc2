# Exact-square affine-`mu2` face: hand elimination of `c != 0`

Date: 2026-08-26

Status: **CHARACTERISTIC-ZERO HAND ELIMINATION FOR THE SIX NON-TARGET
LAURENT ROWS.  THE SOURCE/REES IDENTIFICATION AND ALL CORRECTION,
TERMINAL, AND TAYLOR PROLONGATIONS REMAIN OPEN.**

## 1. System and integer conventions

Put

```text
Q=z^4+p*z^2+c*z+r,
H=sqrt(Q)*(Q^2+beta*Q+gamma),
H-[H]_+ = sum_(ell>=1) h_ell*z^(-ell).              (1.1)
```

The affine-target common-load face is

```text
h1=h3=h4=h5=h6=h7=0,          h2=mu2.               (1.2)
```

Let `Eell` denote the integerized numerators emitted by the exact-square
Pell source, so that

```text
(h1,h2,h3,h4,h5,h6,h7)
 =(E1/256,E2/1024,E3/512,E4/2048,
   E5/2048,E6/32768,E7/4096).                       (1.3)
```

Only the six zero equations in (1.2) are used below.  No equation is imposed
on `E2`; it defines `mu2` through (1.3).

## 2. The `c=0` split

Directly from the emitted polynomials,

```text
E4|_(c=0)=-p*E2|_(c=0),
h4|_(c=0)=-(p/2)*h2|_(c=0).                         (2.1)
```

Consequently, on `D(p)` the affine target is forced to zero:

```text
mu2=0.                                              (2.2)
```

The system then returns to the seven-zero-tail square/Chebyshev
classification.

At `p=c=0`, all odd rows and `h4` vanish identically, while

```text
E6=-256*r^2*(5*r^2+8*r*beta+16*gamma),              (2.3)
E2=  64*r*(5*r^2+6*r*beta+8*gamma).                 (2.4)
```

Thus either `r=0`, in which case `Q=z^4`, `beta,gamma` are arbitrary and
`mu2=0`, or

```text
5*r^2+8*r*beta+16*gamma=0,
mu2=h2=r^2*(5*r+4*beta)/32.                         (2.5)
```

The nonzero-`r` family (2.5) is larger than the zero-target Chebyshev
subfamily.  The latter is recovered at

```text
beta=-5*r/4,       gamma=5*r^2/16,       mu2=0.      (2.6)
```

For the correction successor it is useful to rationalize the whole family.
Put

```text
x=z^2,                  t=5*r+4*beta.                (2.7)
```

Then (2.5) is

```text
beta=(t-5*r)/4,
gamma=r*(5*r-2*t)/16,
mu2=r^2*t/32.                                      (2.8)
```

The polynomial part and loaded polynomial become

```text
A=[H]_+
 =x^5+((t+5*r)/4)*x^3+(r*(5*r+4*t)/16)*x,

P(Q)=x^4+((t+3*r)/4)*x^2+r*(r+2*t)/16.             (2.9)
```

They satisfy the exact generalized Pell remainder identity

```text
A^2-Q*P(Q)^2
 =-(r^2*t/16)*x^4
  -(r^2*t*(t+5*r)/64)*x^2
  -r^3*(r+2*t)^2/256.                              (2.10)
```

The next possible negative coefficient is

```text
h10=-r^4*(t-r)/512.                                (2.11)
```

Thus `t=0` is precisely the Chebyshev constant-remainder subfamily, while
`t=r` is a distinct next-tail cancellation worth keeping as a source
sentinel.  Viewed as a quadratic in `x^2`, the cleared remainder in (2.10)
has discriminant

```text
16*t*(t-r)^2*(t-4*r).                              (2.12)
```

Equations (2.10)--(2.12) are algebraic identities on (2.8); they do not by
themselves impose the next source grade or a terminal condition.

## 3. No `c != 0` component

Work on `D(c)` and write

```text
Fj=Ej/c          for j=1,3,5,7,
Delta=p^2-4*r.                                      (3.1)
```

The first two odd rows have the exact combination

```text
F3+p*F1=4*c^2*(5*p^2-20*r-8*beta).                 (3.2)
```

Since `c` is a unit, `F1=F3=0` gives

```text
beta=5*Delta/8.                                     (3.3)
```

In `Delta` coordinates the first row is

```text
F1=15*Delta^2-40*p*c^2-48*Delta*beta+128*gamma.
```

Hence (3.3) and `F1=0` give

```text
gamma=(15*Delta^2+40*p*c^2)/128.                   (3.4)
```

Substitution of (3.3)--(3.4) into the next two odd rows is elementary and
gives the exact remainders

```text
F5=5*Delta^3+40*p*Delta*c^2+24*c^4,                (3.5)

F7=-5*p*(3*Delta^3+24*p*Delta*c^2+8*c^4).          (3.6)
```

If `p != 0`, equations (3.5)--(3.6) imply

```text
(3.5) - (5/3)*[-F7/(5*p)] = (32/3)*c^4=0,          (3.7)
```

contradicting `c != 0` in characteristic zero.

It remains to put `p=0`.  Then `Delta=-4*r`, and (3.3)--(3.5) become

```text
beta=-5*r/2,
gamma=15*r^2/8,
F5=8*(3*c^4-40*r^3).                               (3.8)
```

The sixth non-target numerator specializes, after (3.8), to

```text
E6=-3840*r^4.                                       (3.9)
```

Thus `E6=0` forces `r=0`, and then `F5=0` forces `c=0`, again contradicting
the open `D(c)`.  This exhausts both `p` cases and proves

```text
V(h1,h3,h4,h5,h6,h7) intersect D(c) = empty        (3.10)
```

over every characteristic-zero field.

## 4. Consequence and exact scope

Set-theoretically, every affine-`mu2` seven-tail point has `c=0`.  On
`D(p)` it also has `mu2=0` and is routed back to the square/Chebyshev
zero-target system.  The only new affine-target support occurs at
`p=c=0` and is exactly the family (2.5), together with its `r=0` square
limit.

This is a Laurent-system statement.  It does not prove the P2 compiler
custody, a raw nonreduced ideal equality, or a total-Rees base change.  It
does not prolong (2.5) through correction grades, the terminal `[6,2]`
row, or either Taylor family.  It does not exclude `k10=0`, close the
all-load receiver, the square branch, order two, `(8,12)`, maximum twelve,
or JC2.
