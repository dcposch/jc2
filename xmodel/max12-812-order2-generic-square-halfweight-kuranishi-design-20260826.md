# `(8,12)` order two: generic-square correction-aware half-weight receiver

Date: 2026-08-26

Status: **SOURCE-TYPED NORMALIZED-RAY DESIGN; NO SQUARE-BRANCH OR
ORDER-TWO VERDICT.**

## 1. Frozen centre and the missing correction chart

On the generic square open write

```text
L=z^2+p/2,                  p!=0,
K=L^2+Lambda*R,             R=cs*z+rs/4,
N=L*M+Lambda*S.
```

The reviewed first-normal component and the exact third-tail divisibility
gate route the generic reduced support to `M=0`; first-contact saturation
then gives `k10!=0`.  The ordinary zero-correction fourth/fifth-grade slice
finds quadratic thickness in `S` and a cubic `k10*R^3/L` term.  It is not
correction-aware: higher `M,S` corrections can tie that cubic term.

The primitive normalized tie is

```text
Lambda=sigma^2,
M=sigma^3*A,                A=a1*z+a0,
S=sigma*C,                  C=(c1*z+c0)/2.            (1.1)
```

Indeed, (1.1) gives exactly

```text
f=K^2+Lambda*N
 =(L^2+sigma^2*R)^2+sigma^5*(L*A+C).                  (1.2)
```

This retains the higher corrections that the ordinary fifth-grade slice
froze to zero.

## 2. Hand Kuranishi calculation

Put `D=L*A+C`.  From (1.2),

```text
f^(3/2)
 =K^3+(3/2)*sigma^5*K*D+(3/8)*sigma^10*D^2/K+O(sigma^15).
```

The first two terms are polynomial in `z`.  The scaled `k10` load is
`sigma^4*k10*f^(5/4)`.  Its first nonpolynomial term occurs at total grade
ten:

```text
sigma^4*k10*K^(5/2)
 = polynomial +(5/16)*sigma^10*k10*R^3/L+O(sigma^12).
```

The `D*K^(1/2)` cross term at grade nine is polynomial; `k6`, `k2`, and all
targets occur too late.  Therefore the complete grade-ten negative receiver
is

```text
[(3/8)*D^2/L^2+(5/16)*k10*R^3/L]_- .                 (2.1)
```

After multiplication by sixteen, polynomiality of (2.1) is equivalent to

```text
L^2 | 6*D^2+5*k10*R^3*L.                             (2.2)
```

Since `D=L*A+C`, reduction of (2.2) modulo `L` gives `L|6*C^2`.  On `D(p)`,
`L` is squarefree and `deg C<deg L`, so `C=0`.  Then (2.2) gives `L|R^3`;
because `deg R<deg L` and `k10` is a unit, `R=0`.  Thus the expected reduced
support is exactly

```text
C=R=0,                                               (2.3)
```

with `A` free.  The raw nonreduced ideal must be retained.

The numerator in (2.1) has degree at most five and the denominator `L^2`
has degree four.  Hence vanishing of the first four negative Laurent
coefficients already implies (2.2); the frozen seven canonical tail rows,
related by the charged unitriangular convention, are sufficient.

## 3. Complete-source AWS contract

The compiler must reconstruct all seven exact frozen loaded rows and make
the substitutions

```text
Lambda -> sigma^2,
c      -> sigma^2*cs,
r      -> (p^2+sigma^2*rs)/4,
n3     -> sigma^3*a1,
n2     -> sigma^3*a0,
n1     -> sigma^3*(p*a1+c1)/2,
n0     -> sigma^3*(p*a0+c0)/2,
k10    -> sigma^4*k10,
k6     -> sigma^12*k6,
k2     -> sigma^20*k2,
target row ell -> sigma^(2*(12+ell))*delta_ell.
```

It must fail unless every row is divisible by `sigma^10`, verify the seven
quotient identities before specialization, and prove the divided rows are
independent of `k6,k2,mu2,mu4,mu6,J`.  After saturation by `p` and `k10`, it
must compare the exact radical with `(c0,c1,cs,rs)` using per-generator
normal forms.  Run exact `Q` and one independent good-prime lane on AWS.

## 4. Scope and fan obligation

This receiver classifies the primitive correction tie (1.1), including its
faces `A=0`, `C=0`, and `R=0`.  It does not by itself prove that every
valuation centred at the generic square component lies in this normalized
chart.  A promotion beyond this ray requires an explicit lowest-weight/Newton
fan argument routing smaller or larger valuations to an earlier gate, this
chart, or a higher-contact successor.

It does not handle `p=0`, the square/discriminant intersection, the terminal
or Taylor receivers, construct or exclude a strict arc, close order two,
close `(8,12)`, prove maximum twelve, or prove JC2.
