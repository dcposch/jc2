# `(8,12)` terminal-power/Belyi theorem and the order-one pure-power core

Date: 2026-08-25  
Status: **PRODUCER THEOREM; FROZEN FOR HOSTILE REVIEW**

## Theorem

Let `L` be a characteristic-zero field, enlarged by the already licensed
finite constant extension so that the required roots of unity and leading
scalar roots are present.  Let `j in L*` be the constant Jacobian.

### A. Nontrivial Kummer orders

For `e in {2,4}`, let

```text
C: u^e=d(x)
```

denote the smooth projective normalization of the minimal Kummer extension,
where the class of `d` has exact order `e` and

```text
deg d=eU,       U>=1.
```

Thus `d=h` in the order-four leaf, while in the order-two leaf `h=v^2` and
`d=v`.  Suppose the reviewed terminal tail exists:

```text
8 r_7'=j/u,                                             (0.1)
```

and has the inverse Kummer character, as it does in the `(8,12)` source.
Put

```text
T=r_7^e.
```

Then `T` is a nonconstant element of `L(x)` and

```text
d(T')^e=(e j/8)^e T^(e-1).                            (0.2)
```

Equivalently,

```text
e=2:  v(S')^2=(j^2/16)S,       S=r_7^2,              (0.3)
e=4:  h(T')^4=(j^4/16)T^3,       T=r_7^4.             (0.4)
```

Over an algebraic closure, (0.2) gives the following exact local dictionary
at every finite point `a`.  Write `k=ord_a(d)`.

```text
1<=k<e  <=>  T has a zero of order e-k at a;
k=e            is impossible;
k>e       <=>  T has a pole of order k-e at a.        (0.5)
```

A zero of `T` of order exactly `e` is allowed at a point with `k=0`.
Away from `T=0,infinity`, the rational map `T:P^1_x -> P^1` has no finite
critical point.

At `x=infinity`, `T` has no pole.  There are exactly two possible local
forms:

```text
T(infinity)=lambda in L*:
  ord_infinity(T-lambda)=U-1;

T(infinity)=0:
  ord_infinity(T)=e(U-1).                              (0.6)
```

In particular `U=1` is impossible.  For `U>=2`, every branch value of `T`
belongs to

```text
{0,infinity,lambda},                                  (0.7)
```

where the third value is omitted when `T(infinity)=0`, and may be
unbranched when `U=2`.  Thus, after a constant target Mobius
transformation, `T` is a three-value/Belyi-type rational map.  Formula
(0.2), not merely its passport, reconstructs the minimal radicand:

```text
d=(e j/8)^e T^(e-1)/(T')^e.                          (0.8)
```

### B. Trivial Kummer order

On the order-one leaf, write after the same licensed scalar extension

```text
h=q^4,       u=q in L[x],       U=deg q,
```

and suppose the terminal row (0.1) has a rational solution
`r_7 in L(x)`.  Then exactly one of the following holds:

```text
U=0:  q is a nonzero constant;

U>=2: q=c(x-a)^U for c in L*, a in L.                 (0.9)
```

There is no solution for `U=1`.  Conversely, every polynomial in (0.9),
and every nonzero constant, has a rational terminal primitive.  Explicitly,

```text
U=0:  r_7=(j/(8c))x+C;

U>=2: r_7=(j/(8c(1-U)))(x-a)^(1-U)+C,                (0.10)
```

with `C in L`.  Consequently the terminal equation collapses the whole
order-one polynomial-core profile space to the constant core and one
single-root power in each degree `U>=2`.

This is a terminal necessary condition only.  It does not solve the other
six tails, the Faber constants, either original Taylor membership family,
coefficient growth, or polynomial Keller existence.

## 1. Charged inputs and exact character

This theorem consumes only the following frozen sources:

```text
30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07
  xmodel/max12-partial-y-kummer-preflight-20260824.md
2951856cabe309fe07f564693a6b48a38cd7108616ffe41305d9583611da90fe
  xmodel/max12-partial-y-kummer-preflight-review-claude-20260824.md
d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036
  xmodel/max12-partial-y-shared-faber-probe-20260824.md
e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c
  xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md
1cd824c9553a800ddf390bc972a29656e1286699406b1ca46bbc94bdfe18084b
  xmodel/max12-812-terminal-exact-differential-divisor-theorem-20260825.md
db67f16dbda759b8481fcbf32491fe77c37483bb5fe70830eb42e95541767251
  xmodel/max12-812-terminal-exact-differential-divisor-review-grok-20260825.md
```

The universal Faber theorem supplies (0.1) in every Kummer order.  If the
deck generator sends `u -> zeta u`, then the charged tail convention sends

```text
r_7 -> zeta^7 r_7=zeta^(-1)r_7
```

for both `e=4` and `e=2`.  Hence `r_7^e` is invariant and belongs to the
fixed field `L(x)`.  Exactness of the Kummer class makes that fixed field
statement literal; no larger intermediate field is being used.

## 2. Derivation of the terminal-power identity

Let `r=r_7` and `T=r^e`.  Differentiate in `x` and use (0.1):

```text
T'=e r^(e-1)r'
  =(e j/8) r^(e-1)/u.                                (2.1)
```

Raising to the `e`-th power and using `u^e=d` gives

```text
(T')^e=(e j/8)^e r^(e(e-1))/d
      =(e j/8)^e T^(e-1)/d,
```

which is (0.2).  Its two specializations have constants

```text
(2j/8)^2=j^2/16,       (4j/8)^4=j^4/16.
```

Since (0.1) has nonzero right side, `r` is nonconstant.  If `T` were
constant, differentiating `T=r^e` in characteristic zero would force
`r'=0`; thus `T` is nonconstant as claimed.

## 3. Finite local dictionary and branch locus

Work over an algebraic closure and use `t=x-a` at a finite point.  First
suppose

```text
n=ord_a(T) != 0.
```

Then `ord_a(T')=n-1`.  Taking orders in (0.2) gives

```text
k+e(n-1)=(e-1)n,
```

or

```text
k=e-n.                                                (3.1)
```

If `n>0`, polynomiality of `d` gives `1<=n<=e`; a charged root `k>0`
therefore has `n=e-k` and `1<=k<e`.  The endpoint `n=e` is precisely an
uncharged zero of `T`.  If `n=-m<0`, (3.1) reads

```text
k=e+m,
```

so a pole of order `m` is precisely a root of multiplicity `e+m`.

Now suppose `T(a)` is finite and nonzero.  If

```text
T-T(a)=c t^s+...,       c!=0,
```

then `ord_a(T')=s-1`, and (0.2) gives

```text
k=-e(s-1).                                            (3.2)
```

Because `d` is a polynomial, (3.2) forces `s=1` and `k=0`.  Hence no
finite critical point lies away from the zero and pole fibres.  Equations
(3.1)--(3.2) also show directly that `k=e` cannot occur.  This recovers the
previous residue exclusion and strengthens it to the rational-map
dictionary (0.5).

## 4. Infinity and the three-value conclusion

Put `q=1/x`.  The derivative in (0.2) is the `x`-derivative, so

```text
d/dx=-q^2 d/dq.                                      (4.1)
```

Since `d` has degree `eU`, its order at infinity is `-eU`.

If `T(infinity)=lambda in L*` and
`T-lambda=cq^s+...`, then (4.1) gives
`ord_q(T')=s+1`.  Taking orders in (0.2) yields

```text
-eU+e(s+1)=0,
```

so `s=U-1`.

If `T` has a zero of order `n>0` at infinity, then
`ord_q(T')=n+1`; (0.2) gives

```text
-eU+e(n+1)=(e-1)n,
```

so `n=e(U-1)`.

Finally, if `T` had a pole of order `m>0`, then
`ord_q(T')=1-m`, and the same calculation would give

```text
m=e(1-U),
```

which is impossible for `U>=1`.  For `U=1` the two finite-value cases
would require order zero rather than a nonconstant local expansion, and the
pole case would require `m=0`; hence no terminal solution exists.

For `U>=2`, Section 3 places every finite critical value in `{0,infinity}`.
The only remaining domain point is `x=infinity`, whose value is either zero
or the single constant `lambda`.  This proves (0.6)--(0.7).  No assertion
that every abstract passport is realized is made.

## 5. Order-one classification

On the trivial Kummer leaf the preflight writes `h=q^4`, and the chosen
fourth root `u=q` is polynomial after the licensed constant scaling.  Put

```text
R=(8/j)r_7.
```

Then the terminal equation is exactly

```text
R'=1/q.                                               (5.1)
```

The constant case is immediate.  Suppose `U=deg q>=1` and work over an
algebraic closure.  A simple root of `q` would give a nonzero logarithmic
residue in (5.1), impossible for a rational derivative.  Thus every root
has multiplicity at least two.  Let the distinct roots have multiplicities

```text
m_1,...,m_N,       sum m_i=U.
```

At the `i`-th root, the leading term of `1/q` has pole order `m_i`, so a
rational primitive has a pole of exact order `m_i-1`.  If `U=1`, the
simple-pole obstruction already proves impossibility.  If `U>=2`, then
`R'=x^(-U)(c+O(x^-1))`, with `c!=0`; consequently `R` is finite at infinity
and

```text
ord_infinity(R-R(infinity))=U-1.                     (5.2)
```

As a rational map, `R:P^1 -> P^1` has degree equal to its total finite pole
degree:

```text
deg R=sum_i(m_i-1)=U-N.                              (5.3)
```

The local mapping degree at infinity is `U-1` by (5.2), and a local degree
cannot exceed the global degree.  Hence

```text
U-1 <= U-N,
```

so `N<=1`.  Since a nonconstant polynomial has a root over the algebraic
closure, `N=1`, proving `q=c(x-a)^U`.  The unique root is Galois-stable, so
`a` lies in the original coefficient field after the stated constant
extension.  Direct integration gives (0.10) and proves the converse.

## 6. Consequence and scope firewall

The terminal source tree is now

```text
order four or two:
  a rational three-value terminal-power map satisfying (0.2);

order one:
  U=0, or one pure finite root of multiplicity U>=2.  (6.1)
```

This is a necessary-terminal-profile theorem.  It does not classify all
three-value maps or prove that a passport lifts to the lower Faber fibre.
It does not impose the first six tail constants, any order-two or order-one
Faber load, either original `P`/`Q` Taylor membership family, a strict Rees
boundary, rational coefficient reconstruction, polynomiality, or existence
of a Keller pair.  It closes no complete Kummer leaf, no whole `(8,12)`
cell, no maximum-twelve frontier, and no part of JC2 by itself.
