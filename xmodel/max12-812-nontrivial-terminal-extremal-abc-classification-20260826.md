# `(8,12)` nontrivial terminal maps are balanced extremal abc triples

Date: 2026-08-26  
Status: **PRODUCER THEOREM; FROZEN FOR HOSTILE REVIEW**

## Theorem

Let `L` be a characteristic-zero field after the already licensed finite
constant extension.  Let `m in {2,4}` be the exact order of a nontrivial
Kummer leaf, let `d in L[x]` be its minimal polynomial radicand, and write

```text
deg d=mU,       U>=1.
```

Thus `d=v` on the order-two leaf and `d=h` on the order-four leaf.  Suppose
the reviewed terminal-power equation holds:

```text
d (T')^m = C T^(m-1),       C=(m j/8)^m in L*,       T in L(x).       (0.1)
```

Then the zero-at-infinity alternative is impossible.  Necessarily

```text
U>=2,       T(infinity)=lambda in L*.                              (0.2)
```

Work over an algebraic closure and normalize `T/lambda=A/B`, where `A,B`
are coprime monic polynomials.  There is an integer `D>=1` such that

```text
deg A=deg B=D.                                                     (0.3)
```

Put

```text
G=A-B,       W=A'B-AB'.                                           (0.4)
```

Let the distinct roots of `A` have multiplicities
`alpha_1,...,alpha_r`, and the distinct roots of `B` have multiplicities
`beta_1,...,beta_s`.  Then

```text
1<=alpha_i<=m,                  beta_j>=1,
r+s=U,
deg G=D-U+1,
G is squarefree (a nonzero constant is allowed),                  (0.5)
```

and, for some `kappa!=0`,

```text
W = kappa A B/(rad(A) rad(B)).                                    (0.6)
```

Consequently

```text
deg rad(A B G)=D+1,                                               (0.7)
```

so `A-B=G` is an equality case of polynomial abc.  The exact passport of
the rational map `T/lambda` is

```text
over 0:        (alpha_1,...,alpha_r),
over infinity: (beta_1,...,beta_s),
over 1:        (U-1, 1^(D-U+1)),                                  (0.8)
```

where the first entry over `1` is the point `x=infinity`.  These three
fibres saturate Riemann--Hurwitz.  In particular

```text
U-1 <= D <= m(U-1).                                               (0.9)
```

The radicand is recovered, up to its nonzero scalar, by

```text
d = C_hat A^(m-1) B^(m+1)/W^m
  = c product_i (x-a_i)^(m-alpha_i)
      product_j (x-b_j)^(m+beta_j),                               (0.10)
```

where `C_hat=C/lambda`.  Because the licensed constant extension removes
constant-class artifacts, its Kummer class has exact order `m` precisely
when

```text
gcd(m, alpha_1,...,alpha_r, beta_1,...,beta_s)=1.                  (0.11)
```

Conversely, a coprime equal-degree triple `A-B=G` satisfying (0.5), with
the multiplicities and gcd condition above, produces through (0.10) a
polynomial radicand of degree `mU` and an exact terminal solution of (0.1),
after the harmless scalar normalization.  This converse is only for the
terminal differential equation; it does not produce the other six tails or
a Keller pair.

## Charged input

This theorem consumes the following frozen theorem and its independent
hostile review:

```text
a4d7d6a1173b5a0b785aa61a4c80ad5f46e4ea83f1d73103917c425608666633
  xmodel/max12-812-terminal-power-belyi-order1-theorem-20260825.md
e322d508c2af66aebb408b2794bd017b05e96cf9ca67f0fc74be8407406f67e1
  xmodel/max12-812-terminal-power-belyi-order1-review-grok-20260825.md
```

The charged theorem supplies (0.1), exact minimal order `m`, `deg d=mU`,
the complete finite local dictionary, absence of finite critical points off
`T=0,infinity`, and the two infinity alternatives.  Everything below is a
new elementary Wronskian and divisor argument from those statements.

## 1. Wronskian orders

First do not assume that the numerator and denominator have equal degree.
Write a reduced presentation

```text
T=A/B,       W=A'B-AB'.                                           (1.1)
```

Equation (0.1) gives

```text
d = C A^(m-1) B^(m+1)/W^m.                                       (1.2)
```

At a root of `A` of multiplicity `alpha`, coprimality gives

```text
ord(W)=alpha-1,
ord(d)=(m-1)alpha-m(alpha-1)=m-alpha.                             (1.3)
```

Polynomiality of `d` therefore forces `alpha<=m`.  At a root of `B` of
multiplicity `beta`,

```text
ord(W)=beta-1,
ord(d)=(m+1)beta-m(beta-1)=m+beta.                               (1.4)
```

At a finite point off `A B`, any zero of `W` would give a pole of `d` of
positive order divisible by `m`.  This is impossible.  Hence all finite
zeros of `W` are already forced by (1.3)--(1.4), and

```text
W = kappa product_i (x-a_i)^(alpha_i-1)
          product_j (x-b_j)^(beta_j-1).                           (1.5)
```

This proves (0.6) whenever the degrees are balanced and also supplies the
degree comparison used next.

## 2. The zero-at-infinity alternative contradicts exact Kummer order

The charged theorem says `T` has no pole at infinity, so
`deg A<=deg B`.  Suppose strictly that

```text
a=deg A < b=deg B.
```

The leading term of the Wronskian has coefficient
`(a-b) lc(A) lc(B)`, nonzero in characteristic zero, and therefore

```text
deg W=a+b-1.                                                       (2.1)
```

On the other hand (1.5) has degree

```text
(a-r)+(b-s)=a+b-r-s.                                              (2.2)
```

Thus `r+s=1`.  Since `B` is nonconstant, `s>=1`; consequently `s=1`,
`r=0`, `A` is constant, and

```text
B=b_0 (x-b_1)^b.                                                  (2.3)
```

Formula (1.4) shows that `d` has the single geometric root `b_1`, of
multiplicity `m+b`.  Since `deg d=mU`,

```text
m+b=mU,       b=m(U-1),
d=c (x-b_1)^(mU).                                                 (2.4)
```

The unique geometric root descends, and after the licensed scalar extension
the right side is an `m`-th power.  This contradicts exact Kummer order
`m`.  The strict inequality is impossible.  Therefore (0.2)--(0.3) hold.

This closes, rather than merely describes, the `T(infinity)=0` branch of the
charged terminal theorem on both nontrivial leaves.

## 3. Balanced degree, the third fibre, and polynomial abc equality

Set `lambda=T(infinity)`.  Replace `T` by `T/lambda`; this changes the
nonzero scalar in (0.1) from `C` to `C_hat=C/lambda` and makes the value at
infinity equal to one.  Multiply numerator and denominator by a common
scalar so that the coprime degree-`D` polynomials `A,B` are monic.

The charged infinity formula is

```text
ord_infinity(T/lambda-1)=U-1.                                    (3.1)
```

Since `T/lambda-1=G/B` with `G=A-B!=0`, this is equivalent to

```text
deg G=D-U+1.                                                       (3.2)
```

In particular `D>=U-1`.  If `G` has a finite root of multiplicity at least
two, that point is neither a root of `A` nor of `B`, and it is a finite
critical point with value one.  This contradicts the charged finite local
dictionary.  Thus `G` is squarefree.

Using `A=B+G`,

```text
W=G'B-GB'.                                                        (3.3)
```

The leading coefficient is `(deg G-D) lc(G) lc(B)=(1-U)lc(G)lc(B)`,
which is nonzero because `U>=2`.  Hence

```text
deg W=2D-U.                                                       (3.4)
```

Comparison with (1.5), whose degree is `2D-r-s`, gives

```text
r+s=U.                                                            (3.5)
```

Now `A`, `B`, and `G` are pairwise coprime, `G` is squarefree, and

```text
deg rad(A B G)=r+s+deg G=U+(D-U+1)=D+1.                           (3.6)
```

This is exact equality in Mason--Stothers for `A-B=G`.  Formula (1.5)
becomes (0.6).

Because `A` and `B` both have positive degree, `r,s>=1`.  Since
`D=sum alpha_i`, `alpha_i<=m`, and `r<=U-1`,

```text
D<=m r<=m(U-1).                                                   (3.7)
```

Together with (3.2), this proves (0.9).

## 4. Passport and Riemann--Hurwitz

The zero and pole fibres have the multiplicities of `A` and `B`.  The finite
roots of `G` are simple, while infinity lies over one with ramification
index `U-1`.  This is exactly (0.8).  Its total ramification is

```text
sum_i(alpha_i-1)+sum_j(beta_j-1)+(U-2)
  =(D-r)+(D-s)+(U-2)
  =2D-2,                                                          (4.1)
```

using `r+s=U`.  Thus the three displayed fibres exhaust
Riemann--Hurwitz; there is no hidden fourth branch value.

## 5. Radicand divisor and exact class

Substitute (0.6) into (1.2).  The exponent at each `A` root is
`m-alpha_i`; the exponent at each `B` root is `m+beta_j`.  Their sum is

```text
sum_i(m-alpha_i)+sum_j(m+beta_j)
  =m(r+s)-D+D=mU,                                                 (5.1)
```

so (0.10) is a polynomial of the required degree.

Modulo `m`, these exponents are `-alpha_i` and `beta_j`.  The infinity
valuation is `-mU`, already divisible by `m`, and the licensed constant
extension makes the leading scalar an `m`-th power.  Therefore the order of
the class of `d` in the Kummer quotient is

```text
m/gcd(m,alpha_1,...,alpha_r,beta_1,...,beta_s).                    (5.2)
```

This proves (0.11).  In particular, an order-two passport needs at least one
odd part, and an exact order-four passport also needs at least one odd part;
all-even order-four data belong to the order-two or order-one leaf instead.

## 6. Converse at terminal scope

Suppose `A,B,G` have the properties stated in the theorem.  Local
differentiation forces `A/rad(A)` and `B/rad(B)` to divide `W`.  Their total
degree is

```text
(D-r)+(D-s)=2D-U.
```

Equation `G=A-B`, together with `deg G=D-U+1`, gives `deg W=2D-U` as in
(3.3)--(3.4).  Thus there is no remaining factor and (0.6) holds.  Formula
(0.10) is consequently polynomial, has degree `mU`, and satisfies (0.1) by
construction.  Formula (5.2) gives exact Kummer order under (0.11).

This converse reconstructs only the minimal Kummer radicand and terminal
primitive.  It does not reconstruct the original coefficients of `f,g` or
verify any lower tail.

## 7. Campaign consequence and firewall

For each fixed `U`, the nontrivial terminal search is now finite at the
passport level:

```text
U-1<=D<=m(U-1),
r+s=U,
partition D=(alpha_1+...+alpha_r)=(beta_1+...+beta_s),
alpha_i<=m,
gcd(m,all parts)=1.                                               (7.1)
```

Each surviving passport asks for an extremal polynomial abc triple, hence a
finite dessin problem at fixed `D`; the exact differential, not the passport
alone, remains the source condition.  This supplies a clean enumerator and a
bridge to the live coefficient/Taylor clients.

Nothing here bounds `U`, verifies the six lower Faber tails, fixes the nine
remaining Faber constants, proves either Taylor polynomiality family,
constructs or excludes an original polynomial Keller pair, closes order two
or order four, resolves `(8,12)` or maximum twelve, or proves or disproves
JC2.
