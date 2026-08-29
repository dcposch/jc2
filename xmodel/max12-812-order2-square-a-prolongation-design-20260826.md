# `(8,12)` order two: generic-square surviving-`A` prolongation

Date: 2026-08-26

Status: **HAND-DERIVED CORRECTION-AWARE SUCCESSOR DESIGN; EXACT FROZEN-SOURCE
REPLAY AND HOSTILE REVIEW REQUIRED.  NO FAN OR SQUARE-BRANCH VERDICT.**

## 1. Input chart and why the zero-correction argument is insufficient

On `D(p*k10)`, put

```text
L=z^2+p/2,
Lambda=sigma^2,
K=L^2+sigma^2*R,
M=sigma^3*A,
S=sigma*C,
N=L*M+Lambda*S=sigma^3*(L*A+C).
```

The frozen halfweight receiver has reduced support `C=R=0`, with `A` free.
Setting every later correction to zero would expose the term
`(5/32)*k10*A^2/L` at total sigma grade fourteen.  That does **not** kill
`A` correction-awarely: a later `S` correction occurs at the same grade.

Write the first possible high-contact corrections as

```text
A=A0+sigma*A1+...,
R=sigma^2*(B0+sigma*B1+...),
C=sigma^4*(E0+sigma*E1+...),
k10=k0+sigma*k1+...,                 k0!=0.             (1.1)
```

Thus

```text
K=L^2+sigma^4*B0+sigma^5*B1+...,
N=sigma^3*(L*A0+sigma*L*A1+sigma^4*E0+sigma^5*E1+...).
```

This is one high-contact successor cone.  Lower valuations of `R` or `C`
must be routed separately by the full Newton-fan argument.

## 2. Exact analytic expansion through grade fifteen

Let `D=L*A+C`.  The only potentially nonpolynomial contributions through
grade fifteen come from

```text
f^(3/2)
 =K^3+(3/2)*sigma^5*K*D
   +(3/8)*sigma^10*D^2/K
   -(1/16)*sigma^15*D^3/K^3+O(sigma^16),

sigma^4*k10*f^(5/4)
 =sigma^4*k10*K^(5/2)
   +(5/4)*sigma^9*k10*D*K^(1/2)
   +(5/32)*sigma^14*k10*D^2/K^(3/2)+O(sigma^16).
```

The displayed `K^3` and `K*D` terms are polynomial.  In the second line,
all contributions before grade fourteen are polynomial on (1.1); the first
negative term is the displayed quadratic term.  The `k6`, `k2`, finite
targets, terminal target, and Taylor loads occur later at this successor
weight, but the exact source compiler must verify rather than assume that
firewall.

At grade fourteen the negative receiver is

```text
[
  (3/4)*A0*E0/L
 -(3/8)*B0*A0^2/L^2
 +(5/32)*k0*A0^2/L
]_- .                                                (2.1)
```

Equivalently,

```text
L^2 | A0*(24*L*E0 + A0*(5*k0*L-12*B0)).             (2.2)
```

This proves directly that the zero-correction `A^2/L` observation is not a
valid obstruction: the whole family

```text
B0=0,        E0=-(5*k0/24)*A0                       (2.3)
```

satisfies (2.2) with arbitrary `A0`.  There are also possible root-allocation
faces of (2.2), because reduction modulo `L` gives `L | B0*A0^2`; they must
not be deleted by saturating a resultant.

At grade fifteen, retaining all first tangent coefficients in (1.1), the
receiver is

```text
[
  (3/4)*(A0*E1+A1*E0)/L
 -(3/8)*(B1*A0^2+2*B0*A0*A1)/L^2
 +(5/32)*(k1*A0^2+2*k0*A0*A1)/L
 -(1/16)*A0^3/L^3
]_- .                                                (2.4)
```

After multiplication by `16*L^3`, every term except `-A0^3` is divisible by
`L`.  Therefore polynomiality of (2.4) implies

```text
L | A0^3.                                            (2.5)
```

Since `p!=0`, `L` is squarefree of degree two, while `deg(A0)<=1`.
Consequently (2.5) forces

```text
A0=0.                                                (2.6)
```

The key point is that (2.6) is insensitive to every grade-fourteen
root-allocation solution: `B0,E0,A1,B1,E1,k1` only contribute terms carrying
at least one factor of `L` in (2.4).

## 3. Required exact-source client

Compile the complete frozen seven-row source under

```text
Lambda -> sigma^2,
c      -> sigma^4*bs0 + sigma^5*bs1,
r      -> (p^2 + sigma^4*br0 + sigma^5*br1)/4,
n3     -> sigma^3*(a1 + sigma*aa1),
n2     -> sigma^3*(a0 + sigma*aa0),
n1     -> sigma^3*(p*(a1+sigma*aa1)
                    +sigma^4*(e1+sigma*ee1))/2,
n0     -> sigma^3*(p*(a0+sigma*aa0)
                    +sigma^4*(e0+sigma*ee0))/2,
k10    -> k0+sigma*k1,
k6,k2 and every target at their frozen Lambda weights.
```

The client must:

1. verify exact divisibility by `sigma^14` in all seven rows;
2. compare the grade-fourteen source rows with the frozen Faber transform of
   (2.1), before imposing (2.2);
3. quotient the grade-fourteen ideal rather than replacing it by its radical;
4. extract grade fifteen in the quotient/normal cone, retaining all tangent
   coefficients displayed above;
5. compare it with the Faber transform of (2.4);
6. certify (2.5) source-side on `D(p*k0)` without deleting the root-allocation
   faces of (2.2);
7. run exact `Q` and an independent good-prime control on AWS.

## 4. Scope firewall

If the source replay confirms (2.1)--(2.6), it eliminates the surviving `A`
direction only in the high-contact cone

```text
ord_sigma(R)>=2,       ord_sigma(C)>=4
```

after the reviewed halfweight support.  It does not route smaller valuations
of `R` or `C`, prove normalized-Rees/Newton-fan exhaustiveness, handle `p=0`,
the square/discriminant intersection, terminal or Taylor successors, close
the square branch, close order two or `(8,12)`, prove maximum twelve, or
prove JC2.
