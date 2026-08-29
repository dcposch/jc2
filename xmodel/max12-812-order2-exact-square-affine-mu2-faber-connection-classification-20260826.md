# `(8,12)` order two: corrected affine-`mu2` Faber connection and support

Date: 2026-08-26

Status: **PRODUCER THEOREM: CHARACTERISTIC-ZERO HAND CLASSIFICATION PLUS
DUAL-AWS EXACT-SOURCE REPLAY.  HOSTILE REVIEW PENDING.  NO TOTAL-REES
ACCESSIBILITY, CORRECTION, TERMINAL, TAYLOR, OR ORDER-TWO VERDICT.**

## 0. Correction first

The exploratory affine-`mu2` client

```text
cases/max12_812_order2_exact_square_affine_mu2_20260826/
```

correctly classifies the raw negative **`z`-Laurent** system

```text
h1=h3=h4=h5=h6=h7=0,       h2=mu2.                 (0.1)
```

It does not classify the ordinary Faber target system.  When `mu2` is
nonzero, the unitriangular Laurent-to-Faber connection has nonzero later
entries.  Weighted homogeneity carries the Faber rows to Faber rows; it
does not turn them coefficientwise into (0.1).

Consequently the following previously frozen design is navigation-only:

```text
fec7c140b8ceae57926895c88c4d43ed49753c17a2858f2824e49d872df8d276
  xmodel/max12-812-order2-exact-square-affine-mu2-dvr-rigidity-p3-design-20260826.md
```

Its Laurent-valuative theorem remains correct for (0.1), and its Gate A
was explicitly fail-closed.  Its four-pivot block must not be imported into
the ordinary source, because Gate A does not identify (0.1) with the Faber
target.

The corrected Faber support is larger: on its new component `p` is free.

The corrected exact-Q producer and independent good-prime control are
frozen at

```text
86d9da43b1f7823a4673ed219478b1c6ff60503eccbb2892894733979468b19c
  cases/max12_812_order2_exact_square_faber_affine_mu2_20260826/RESULT.md

8e56b7ab944e956b9d67993e54bfc8996f02b16803889ac7dfbaa59e2ee0447c
  cases/max12_812_order2_exact_square_faber_affine_mu2_20260826/EVIDENCE.sha256

a779cdeb5be36ad70c09b1497c3719b8c0659c03b48798414d90464156993970
  cases/max12_812_order2_exact_square_faber_affine_mu2_20260826/FREEZE.sha256

1a4b7a9de049eaf82c3fb2682511ebcb441004a30af03abac241165717c34a12
  cases/max12_812_order2_exact_square_faber_affine_mu2_20260826/compile_faber_affine_mu2.py
```

Both V2 validators report `PASS_FABER_AFFINE_MU2_PROBE`.  The exact-Q run
independently reconstructed all seven connections (1.4), computed the raw
ideal and its radical, proved both ideal containments against the proposed
two-prime intersection, found no support on `D(c)`, and returned exactly
two minimal primes.  Characteristic 65521 returned the same endpoint as a
control.  V1 is preserved as parser-negative custody and has no mathematical
status.

## 1. Exact connection through row seven

Put

```text
Q=z^4+p*z^2+c*z+r,
w=Q^(1/4),
H=sqrt(Q)*(Q^2+beta*Q+gamma),
H-[H]_+=sum_(ell>=1) h_ell*z^(-ell).                (1.1)
```

Let `z=z(w)` be the monic inverse of `w=Q^(1/4)`.  Direct substitution in
`Q(z(w))=w^4` gives

```text
z(w)=w-(p/4)*w^-1-(c/4)*w^-2
       +(p^2/32-r/4)*w^-3
       +(p^3/128-p*r/16-c^2/32)*w^-5+O(w^-6).       (1.2)
```

There is no `w^-4` term.  If

```text
sum_(ell>=1) R_ell*w^(-ell)
  =(H-[H]_+)(z(w)),                                 (1.3)
```

then expansion of `z(w)^(-ell)` gives

```text
R1=h1,
R2=h2,
R3=h3+(p/4)*h1,

R4=h4+(p/2)*h2+(c/4)*h1,

R5=h5+(3*p/4)*h3+(c/2)*h2
      +(p^2/32+r/4)*h1,

R6=h6+p*h4+(3*c/4)*h3
      +(p^2/8+r/2)*h2+(p*c/8)*h1,

R7=h7+(5*p/4)*h5+c*h4
      +(9*p^2/32+3*r/4)*h3+(3*p*c/8)*h2
      +(-p^3/128+3*p*r/16+3*c^2/32)*h1.            (1.4)
```

These are polynomial identities over every characteristic in which the
displayed powers of two are invertible.  In particular,

```text
R4=h4+(p/2)*h2                                      (1.5)
```

when `h1=0`.  On `c=0`, the Laurent identity
`h4=-(p/2)h2` therefore makes the Faber row `R4` vanish identically; it
does not force `p*mu2=0`.

The ordinary affine target is

```text
R1=R3=R4=R5=R6=R7=0,        R2=mu2.                (1.6)
```

## 2. The corrected reduced support

Set

```text
Delta=p^2-4*r.                                      (2.1)
```

After geometric base change over a characteristic-zero field, the reduced
support of (1.6) is the union of

```text
square:
  c=0,
  Delta=0,
  mu2=0;                                            (2.2)

affine Faber:
  c=0,
  15*Delta^2-64*beta*Delta+256*gamma=0,
  Delta^2*(5*Delta-16*beta)-2048*mu2=0.             (2.3)
```

The square component permits arbitrary `(beta,gamma)`.  On `D(Delta)`,
(2.3) is a rational graph over `(p,Delta,beta)` and is the only new
affine-target component.  Its zero-target section is exactly the reviewed
Chebyshev family

```text
16*beta=5*Delta,
256*gamma=5*Delta^2.                                (2.4)
```

## 3. Raw fifth-power certificate and exclusion of `c != 0`

The printed Laurent polynomials and (1.4) satisfy the exact raw identity

```text
R5=-c^5/128+(3*p/4)*R3+(3*p^2/32+r/4)*R1.          (3.1)
```

Equivalently,

```text
c^5+128*R5-96*p*R3-(12*p^2+32*r)*R1=0.             (3.2)
```

No predecessor equation, division, radical, or localization is used in
(3.1)--(3.2).  In particular the raw ideal `(R1,R3,R5)` contains `c^5`.
This records both the reduced support `c=0` and the exact transverse
nilpotence/contact-raising exponent five.

Because `R1=h1`, equation `R1=0` is `h1=0`.  Equation `R3=0` then reduces
to `h3=0`.  On `D(c)`, the first and third Laurent rows give exactly

```text
beta=5*Delta/8,
gamma=15*Delta^2/128+5*p*c^2/16.                   (3.3)
```

Put

```text
U=Delta^3+8*p*Delta*c^2+8*c^4.                     (3.4)
```

Substitution of (3.3) into the integerized Laurent rows gives

```text
h2=-5*U/1024,
h5=c*(5*U-16*c^4)/2048.                            (3.5)
```

Since `h1=h3=0`, connection (1.4) reduces to

```text
R5=h5+(c/2)*h2=-c^5/128.                            (3.6)
```

Thus `R5=0` contradicts `c != 0` in characteristic zero.  No Groebner
basis, radical, or later row is needed.  Every geometric point of (1.6)
has `c=0`.

## 4. Classification on `c=0`

Put

```text
D=Delta/4,
T=z^2+p/2,
Q=T^2-D.                                            (4.1)
```

The polynomial part of `H` is a polynomial in `T`, and its first two
possible negative `T`-coefficients are

```text
a=[T^-1]H=-(D/16)*(5*D^2-6*beta*D+8*gamma),
b=[T^-3]H=-(D^2/128)*(5*D^2-8*beta*D+16*gamma).     (4.2)
```

At the inverse point,

```text
w^4=Q=T^2-D,
T(w)=sqrt(w^4+D),
T(w)^-1=w^-2-(D/2)*w^-6+O(w^-10),
T(w)^-3=w^-6+O(w^-10).                              (4.3)
```

Therefore the only possibly nonzero Faber rows through seven are

```text
R2=a,
R6=b-(D/2)*a
   =(D^2/128)*(15*D^2-16*beta*D+16*gamma).          (4.4)
```

If `D=0`, then `Q=T^2`, the whole loaded expression is polynomial, and
(2.2) follows.  If `D!=0`, row `R6=0` gives

```text
gamma=beta*D-15*D^2/16.                             (4.5)
```

Substitution into `R2=mu2` gives

```text
mu2=D^2*(5*D-4*beta)/32.                            (4.6)
```

Clearing `D=Delta/4` in (4.5)--(4.6) yields exactly (2.3).  This proves the
geometric union (2.2)--(2.3).

The two-row Jacobian on `D(Delta)` is also useful.  With rows
`(R6,R2-mu2)` and variables `(beta,gamma)`, its determinant is

```text
D^4/64=Delta^4/16384.                               (4.7)
```

Thus `(beta,gamma)` are exact correction pivots on the new component.
The tangent parameters `(p,D)` remain free; in particular no correct
Faber argument sets `p=0`.

## 5. Generalized Pell identity on the corrected graph

For terminal and Taylor controls, put

```text
s=5*D-4*beta,             mu2=D^2*s/32.             (5.1)
```

On (4.5)--(4.6), the loaded polynomial and polynomial part are

```text
P(Q)=T^4-((s+3*D)/4)*T^2+D^2/16,

A=[H]_+
 =T^5-((s+5*D)/4)*T^3+(D*(2*s+5*D)/16)*T.          (5.2)
```

Direct multiplication gives the exact generalized Pell remainder

```text
A^2-Q*P(Q)^2
 =-(D^2*s/16)*T^4
  +(D^2*s*(s+3*D)/64)*T^2
  +D^5/256.                                         (5.3)
```

As a quadratic in `T^2`, its discriminant is

```text
D^4*s*(s+D)^2*(s+4*D)/4096.                        (5.4)
```

The first Faber coefficient after the seven source rows is

```text
R10=-D^4*(s+D)/512.                                 (5.5)
```

Thus `s=0` is the Chebyshev constant-remainder section, `s=-D` is the
sharp next-tail and double-discriminant sentinel, and `s=-4*D` is the
other repeated-remainder sentinel.  Row `R10` is outside the ordinary
seven-row source; (5.4)--(5.5) are compiler and terminal/Taylor controls,
not additional source equations.

## 6. Correct weighted-section consequence

Faber homogeneity says

```text
R_ell(lambda^(8-i)*a_i,
      lambda^2*k10,lambda^6*k6,lambda^10*k2)
 =lambda^(12+ell)*R_ell(a,k).                       (6.1)
```

Consequently the exact-square weighted section

```text
Q_lambda(z)=lambda^4*Q(z/lambda),
f_lambda=Q_lambda^2
```

pulls the divided ordinary rows back to (1.6), not to (0.1).  A correct
`P2F` source replay must reconstruct the frozen ordinary Faber tails and
then verify (1.2)--(1.6) coefficientwise.  Reusing only the Laurent
recurrence is an intentional negative control.

For a pure reduced-domain arc specializing to (2.3) on `D(Delta)`, Section
3 applied over the fraction field forces `c` to vanish identically, while
(4.5)--(4.6) hold identically.  This is the corrected horizontal rigidity:
`p` and `D` may move, but `c` may not.  Transverse total-source forcing can
invalidate the unforced equations and must be emitted before this
valuative statement is consumed.

## 7. Smallest corrected successor

The next client should:

1. run exact Q and an independent good prime from the complete ordinary
   Faber source and verify (1.4) as a compiler self-control;
2. confirm the reduced union (2.2)--(2.3), retaining the raw nonreduced
   ideal;
3. on `D(k10*Delta)`, use only the two pivots (4.7), keep `(p,D)` and every
   square-normal/load/target jet, and Schur-reduce the other five rows;
4. route `Delta=0` to the square receiver, `mu2=0,Delta!=0` to Chebyshev,
   and `k10=0` to the two-load boundary; and
5. pull every survivor independently to terminal `[6,2]` and both Taylor
   families.

The identity (3.2) is a raw contact-raising certificate and a strong
negative control for the transverse chart.
It does not license replacing a forced correction by `c=0`; a source term
tying `R5` can balance a positive-order `c`, potentially after
ramification.  Such a balance belongs to the correction Newton fan.

## 8. Explicit nonclaims

The exact-Q producer identifies the radical of this normalized seven-row
Faber ideal, but this note does not prove that the component is accessible
in the interior- and `J`-saturated total-Rees boundary.  It does not classify
forced transverse corrections, the `k10=0` boundary, the terminal passport,
or either Taylor family.  It constructs and excludes no strict source arc
and does not close the square branch, order two, `(8,12)`, maximum twelve,
or JC2.
