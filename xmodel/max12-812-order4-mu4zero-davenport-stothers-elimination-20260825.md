# `(8,12)` order-four `mu_4=0` elimination by the unique order-four DS triple

Date: 2026-08-25  
Status: **EXACT ELIMINATION OF THE ORDER-FOUR `mu_4=0` TERMINAL STRATUM,
PLUS THE ORDER-TWO `U=2,[6,2]` ALL-ZERO-LOAD SUB-STRATUM; NO CLAIM ABOUT
THE REMAINING ORDER-TWO CLIENT OR JC2**

## Theorem

Let `L` be a characteristic-zero constant field, enlarged harmlessly to
contain `mu_4`, and let

```text
C: u^4=h(x),       h monic,       deg(h)=4U,
```

where the class of `h` in `L(x)^*/L(x)^{*4}` has exact order four.  Put
`M=L(C)`.  Consider a source-typed monic depressed `(8,12)` high-row client
over `M` with

```text
f in M[z],  deg_z(f)=8,       g=F_12(f),  deg_z(g)=12,
r_1=...=r_6=0,                8 dr_7/dx=j/u,  j!=0.   (0.1)
```

These are exactly the order-four equations after imposing `mu_4=0`; there
are no lower order-four Faber loads.  Then no such client exists.

Equivalently, the entire nontrivial order-four `mu_4=0` terminal stratum is
empty, for every `U>=1`.  This is a necessary-terminal-profile elimination:
it does not assume either Taylor family or a Keller pair exists, and it does
not address the separate `mu_4!=0` stratum.

## 1. Charged source and exact classification scope

The campaign-local source typing is charged through the following immutable
artifacts:

```text
092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e
  xmodel/max12-812-order24-coefficient-infinity-source-audit-20260825.md
2f0a03a99ba6563034cdaf84ffc06f6d78ddd377144201d40aa4352ac71c6b55
  xmodel/max12-812-order24-coefficient-infinity-review-grok-20260825.md
1cd824c9553a800ddf390bc972a29656e1286699406b1ca46bbc94bdfe18084b
  xmodel/max12-812-terminal-exact-differential-divisor-theorem-20260825.md
db67f16dbda759b8481fcbf32491fe77c37483bb5fe70830eb42e95541767251
  xmodel/max12-812-terminal-exact-differential-divisor-review-grok-20260825.md
```

The first hostile review's `REPAIR` is confined to its target's unrelated
§7 claim about the order-two lower-load differential.  It explicitly
confirms the order-four high row, complete tail targets, ordinary tail
definition, inverse character, and all core §§0--6 used here.  The terminal
divisor theorem and its different-model review independently confirm the
sign and constant in `8r_7'=j/u`, the inverse-character line, and the finite
and infinite local orders used below.

The primary source is T. Shioda, *Elliptic Surfaces and
Davenport--Stothers Triples*, Comment. Math. Univ. St. Pauli 54 (2005),
49--68:

```text
DOI:       10.14992/00008689
record:    https://rikkyo.repo.nii.ac.jp/records/8708
PDF:       https://rikkyo.repo.nii.ac.jp/record/8708/files/AA00610867_54-01_04.pdf
PDF SHA:   467701925109586976ca8f89ec614ee95c5ad740084b969a93ba3795b0cdb740
```

Shioda defines a DS triple of order `m` by

```text
F^3-G^2=H,       deg(F)=2m, deg(G)=3m, deg(H)=m+1,
```

states Stothers' enumeration `St(4)=1`, defines essential equivalence by

```text
t -> a t+b,       (F,G,H) -> (c^2 F,c^3 G,c^6 H),   ac!=0,   (1.1)
```

and in Example 5.1 / Theorem 5.1 gives the unique order-four representative

```text
F=t^8+6t^7+21t^6+50t^5+86t^4+114t^3+109t^2+74t+28,

G=t^12+9t^11+45t^10+156t^9+408t^8+846t^7+1416t^6
  +1932t^5+2136t^4+1873t^3+(2517/2)t^2+(1167/2)t+299/2,

H=F^3-G^2=-(27/4)(4t^5+15t^4+38t^3+61t^2+62t+59). (1.2)
```

The source works over an algebraically closed characteristic-zero field in
its algebraic setup and uses the complex/Stothers enumeration for the
classification.  Applying (1.2) over the algebraic closure of `M` is
licensed by the characteristic-zero Lefschetz principle: for fixed degrees,
existence of the affine/scaling parameters in (1.1) is a first-order
algebraic statement in finitely many coefficients.  A client over `M`
therefore becomes equivalent to (1.2) over `Mbar`.  The descent back to `M`
is proved explicitly in §3 rather than assumed.

## 2. The terminal tails force an order-four DS triple

Use the reviewed tail convention

```text
w=f^(1/8)=z+O(z^-1),
w^12-g(z(w))=sum_(ell>=1) r_ell w^-ell.              (2.1)
```

Under (0.1),

```text
g(z(w))=w^12-r_7 w^-7+O(w^-8).
```

Therefore, with `W=g^2-f^3`,

```text
W(z(w))=-2r_7 w^5+O(w^4)=-2r_7 z^5+O(z^4).          (2.2)
```

The terminal row makes `dr_7=(j/8)dx/u` nonzero, so `r_7` and `W` are
nonzero.  Hence `deg_z(W)<=5`.  Davenport's bound over the
characteristic-zero field `M` gives

```text
deg_z(g^2-f^3)>=8/2+1=5.
```

Thus equality holds, `deg_z(W)=5`, and `(f,g,f^3-g^2)` is a DS triple of
order four over `M`.  Its leading coefficient satisfies

```text
[z^5]W=-2r_7.                                        (2.3)
```

This lane uses equality in Davenport's bound only here.  It does not apply
when `mu_4!=0`: then `r_4=mu_4` contributes a degree-eight term to `W`.

## 3. Monic depression, the Hall constant, and descent of `alpha`

By uniqueness, over `Mbar` there are `alpha,c!=0` and `beta` such that

```text
f(z)=c^2 F(alpha z+beta),
g(z)=c^3 G(alpha z+beta).                             (3.1)
```

Both `f` and `g` are monic.  Their leading coefficients give

```text
c^2 alpha^8=1,       c^3 alpha^12=1.
```

Thus `(c alpha^4)^2=(c alpha^4)^3=1`, so

```text
c=alpha^-4.                                          (3.2)
```

The coefficient of `z^7` in (3.1) is
`alpha^-1(8 beta+6)`.  Depression forces the unique translation

```text
beta=-3/4.                                           (3.3)
```

Direct binomial expansion of `F(t)` after `t=alpha z-3/4` gives

```text
[z^6]f=(21/4)alpha^-2,
[z^5]f=(11/4)alpha^-3.                               (3.4)
```

For clarity, the unscaled constants are

```text
28(-3/4)^2+42(-3/4)+21 = 21/4,
56(-3/4)^3+126(-3/4)^2+126(-3/4)+50 = 11/4.
```

Both coefficients in (3.4) belong to `M`, and both displayed rational
constants are nonzero.  Hence `alpha^-2,alpha^-3 in M`, and their quotient
puts `alpha^-1`, therefore `alpha`, in `M`.  This is the required descent;
no affine parameter remains only over `Mbar`.

The leading coefficient of the Hall difference in (1.2) is `-27`.  From
(3.1)--(3.3),

```text
f^3-g^2=alpha^-24 H(alpha z-3/4)
        =-27 alpha^-19 z^5+O(z^4),

W=g^2-f^3=27 alpha^-19 z^5+O(z^4).                  (3.5)
```

Comparison with (2.3) gives the exact identity

```text
r_7=-(27/2)alpha^-19.                                (3.6)
```

Since `alpha in M^*`, every zero and pole order of `r_7` on the smooth
projective curve `C` is divisible by nineteen:

```text
div_C(r_7)=-19 div_C(alpha).                         (3.7)
```

## 4. Exact finite and infinite divisor audit

The terminal equation is the equality of differentials

```text
dr_7=(j/8) dx/u.                                     (4.1)
```

The already-confirmed infinity residue excludes `U=1`, so assume `U>=2`.

Let `a` be a finite root of `h` of multiplicity `m`, put
`d=gcd(4,m)`, and let `P` be any of the `d` places of `C` over `a`.  With a
local uniformizer `tau`,

```text
x-a=tau^(4/d),       u=tau^(m/d) times a unit,
ord_P(dx/u)=(4-m)/d-1.                               (4.2)
```

The cases are exact.

### 4.1. Small roots are impossible

If `m<4`, the inertia subgroup at `P` is nontrivial.  It acts on `r_7` by
the inverse Kummer character, so the regular value `r_7(P)` must be zero.
Integrating (4.2) then gives

```text
ord_P(r_7)=(4-m)/d = 3,1,1 for m=1,2,3.              (4.3)
```

None is divisible by nineteen, contradicting (3.7).  Thus `h` has no root
of multiplicity below four.

### 4.2. Multiplicity four is impossible

For `m=4`, (4.2) is a simple pole.  Its coefficient is a nonzero local unit,
so `(j/8)dx/u` has nonzero residue at each of the four unramified places
over `a`.  An exact differential has zero residue place by place.  Thus
multiplicity four is impossible.

### 4.3. Large roots give all finite poles

If `m>4`, (4.2) has order at most `-2`, and (4.1) forces

```text
-ord_P(r_7)=(m-4)/d.                                 (4.4)
```

In particular `19` divides `(m-4)/d` by (3.7).  There are `d` places over
`a`, so this root contributes total pole degree exactly

```text
d (m-4)/d=m-4.                                       (4.5)
```

At any finite point not over a root of `h`, `dx/u` has order zero.  A zero
of `r_7` there would consequently have order one, again contradicting
(3.7).  Therefore `r_7` has no finite zeros, and its finite poles are
exactly those in (4.4).

### 4.4. Every zero is at infinity

There are four unramified points over infinity, permuted transitively by
the deck group.  With `q=1/x` and `t=q^Uu` a unit,

```text
dr_7=-(j/8)q^(U-2)t^-1 dq.                           (4.6)
```

Thus `r_7` is regular at infinity.  It is nonconstant by (4.1), so on the
projective curve it has a zero.  No zero is finite, hence one occurs at
infinity.  The inverse-character action then makes all four infinite values
zero, with the same order.  Equation (4.6) gives

```text
ord_P(r_7)=U-1       at every P over infinity,       (4.7)
```

and (3.7) also gives `19 | (U-1)`.  The total zero degree is exactly
`4(U-1)`.

## 5. Degree balance forces a trivial Kummer class

Sections 4.1 and 4.2 show that every root multiplicity `m_i` of `h` is
strictly greater than four.  Let `N` be the number of distinct finite roots.
By (4.5), the total pole degree of `r_7` is

```text
sum_i (m_i-4)=4U-4N.                                 (5.1)
```

By (4.7), its total zero degree is `4(U-1)=4U-4`.
Degree zero of a principal divisor therefore gives

```text
4U-4=4U-4N,       hence N=1.                         (5.2)
```

Since `h` is monic of degree `4U`, this says

```text
h=(x-a)^(4U)=((x-a)^U)^4,                            (5.3)
```

whose Kummer class has order one, contradicting the order-four hypothesis.
Together with the separate `U=1` residue obstruction, this proves the
theorem for every `U>=1`.

## 6. Concrete order-two `U=2,[6,2]` zero-load corollary

The same DS argument has one exact order-two consequence.  Charge the
source-typed client

```text
e5e3472f052b2ae932daefc9dec7a17106ca4c13f8b920ba59da627d0653fec7
  xmodel/max12-812-order2-u2-62-strict-rees-client-20260825.md
```

with

```text
h=x^6(x-1)^2,       u^2=x^3(x-1),
T=u/x^2,            T^2=(x-1)/x,
r_7=(j/4)T.                                          (6.1)
```

Restrict only to the closed sub-stratum

```text
k_10=k_6=k_2=0,       mu_2=mu_4=mu_6=0.             (6.2)
```

Then `g=F_12(f)` and `r_1=...=r_6=0`, so §§2--3 apply verbatim over this
quadratic function field: the Hall classification and the `z^6,z^5`
descent again force

```text
r_7=-(27/2)alpha^-19,       alpha in M^*.            (6.3)
```

Thus every divisor order of `r_7` must be divisible by nineteen.  But the
normalization in (6.1) is the rational `T`-line, and

```text
div_C(r_7)=div_C(T)=[T=0]-[T=infinity].              (6.4)
```

Both orders are one.  Equations (6.3) and (6.4) contradict each other.
Therefore the all-lower-Faber-load-zero, all-lower-tail-load-zero
sub-stratum (6.2) of the concrete order-two `U=2,[6,2]` client is empty.

This does not eliminate the source-typed order-two client itself.  Any
survivor must have at least one of

```text
k_10,k_6,k_2,mu_2,mu_4,mu_6
```

nonzero, in which case `g^2-f^3` need not have degree five and the unique
order-four DS classification does not apply.

## 7. Consequence and scope firewall

The exact consequence is

```text
order-four, mu_4=0: EMPTY for every monic core degree 4U.             (7.1)
```

This is orthogonal to the common-quartic Rees lane: it uses the generic
finite polynomial `z`-degree of `g^2-f^3`, the unique equality case of
Davenport's bound at order four, descent of the affine parameter, and the
terminal differential divisor.  It requires no saturation and no Taylor
realization.

No statement here applies to:

- `mu_4!=0`, where `deg_z(g^2-f^3)<=8` and DS equality is unavailable;
- the remainder of the genuine order-two leaf outside the zero-load
  sub-stratum (6.2);
- the order-one leaf, bounded sectors, the full `(8,12)` cell, maximum
  twelve, a counterexample, or JC2.
