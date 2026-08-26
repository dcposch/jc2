# `(8,12)` order-four nonzero-load residual cusp and deck-genus gate

Date: 2026-08-26  
Status: **EXACT PRODUCER THEOREM FOR THE RECONSTRUCTED PLANE; APPLICATION TO
THE SOURCE IS PROVISIONAL PENDING THE COMPONENTWISE PROJECTION GATE AND
HOSTILE REVIEW.**

## 0. Result and firewall

Let `P(q,v)` be the exact irreducible residual polynomial in Section 1 and
let `X` be the normalization of its closure in the toric surface of its
Newton polygon.  Then

```text
g(X)=0,
div_X(v)=8 P_0-P_ul-P_A-6 P_B.                         (0.1)
```

Here `P_B` is one `(2,7)` cusp branch over `q=-4/27`, not two smooth
branches.  The Kummer curve

```text
Y: y^4=v                                                (0.2)
```

is geometrically irreducible of degree four over `X` and its complete
normalization has

```text
g(Y)=1.                                                 (0.3)
```

Consequently, the exact-order-four `mu_4 != 0` source leaf is empty if the
following still-open projection gate holds componentwise: every relevant
component of the corrected, `r_7`-saturated coefficient fibre maps
nonconstantly to the irreducible curve (0.2) by

```text
q=a_5^2/a_6^3,      y=a_6^2,      v=y^4=a_6^8.         (0.4)
```

Indeed the source deck quotient is `P^1_x`; properness extends its rational
map across poles, and there is no nonconstant map `P^1 -> Y` when `g(Y)=1`.
The terminal coordinate `rho=r_7^4` is known to be nonconstant, but that
alone does **not** prove that `(q,y)` is nonconstant.  Exact dominance, or
an exact graph relation making `rho` algebraic over `(q,y)` on every
relevant component, remains mandatory.  No genus-based source elimination
is promoted in this note.

## 1. Exact reconstructed plane

Write

```text
P(q,v)=q H(q)v^3+L_2(q)v^2+L_1(q)v+L_0,
```

where

```text
H(q)=1+(10341/484)q-(177147/1936)q^2
       -(53636175/7744)q^3-(2681119845/30976)q^4
       -(63407820033/123904)q^5-(750433487193/495616)q^6
       -(3587901148629/1982464)q^7,

L_2(q)=5184+(16537365/121)q+(15077178/11)q^2
       +(6133360581/968)q^3+(3027619377/242)q^4
       +(192547983033/30976)q^5,

L_1(q)=-419904/11+(865008801/484)q-(1745783685/484)q^2,
L_0=8503056/121.
```

The 32-prime reconstruction is stable after 16, 24, and 32 primes.  An
independent exact characteristic-zero replay proves:

```text
P is irreducible over Q;
P(a_5^2/a_6^3,a_6^8), after clearing the displayed monomial,
  belongs to the corrected r_7-saturated source ideal;
the torus singular scheme has length 4;
the Hessian determinant is a unit on that scheme.
```

Thus the four torus singularities are reduced ordinary nodes.  The exact
membership is not an elimination-equality or dominance certificate.

The Newton polygon is

```text
Delta=conv{(0,0),(0,2),(1,3),(8,3)}.                  (1.1)
```

It has area `23/2`, lattice-boundary length `11`, and hence seven interior
lattice points.

## 2. Every toric boundary point

All four vertex coefficients of `P` are nonzero, so the closure misses the
toric fixed points.  The four open boundary divisors give the following
complete list.

### 2.1 Left edge

At `q=0`,

```text
P(0,v)=(1296/121)(22v-81)^2.
```

There is one boundary point with `v=81/22`.  The exact transverse
coefficient is

```text
123466498884/14641 != 0.
```

Consequently the curve is smooth there, tangent to the boundary with
intersection order two.  On its normalization `ord(q)=2` and `ord(v)=0`.
This point contributes no delta invariant.

### 2.2 Primitive upper-left edge

The edge from `(0,2)` to `(1,3)` has primitive lattice length one.  Its
two-term face polynomial has one simple torus root.  The corresponding
smooth branch has

```text
(ord(q),ord(v))=(1,-1).                              (2.1)
```

This is the branch approaching `(q,v)=(0,infinity)` in the ordinary affine
coordinates; it is not an omitted toric corner.

### 2.3 Top edge

With `w=1/v`, the top face factors exactly as

```text
H(q)=(-1/1982464)(9261q-484)(27q+4)^6.               (2.2)
```

The root `q_A=484/9261` is not a root of `L_2`; hence it is one smooth
branch with `ord(v)=-1`.

At `q_B=-4/27`, the first transverse coefficient has order three:

```text
L_2(q)=(81/30976)
       (120771q^2+189396q+30976)(27q+4)^3.            (2.3)
```

The weighted local quadratic in `(Q,w)`, `Q=q+4/27`, has coefficients

```text
A=-29/209088,   B=7047/484,   C=-46235367/121,
B^2-4AC=0,
```

and repeated slope `w=(1/52488)Q^3+...`.  Exact
Hamburger--Noether expansion gives one branch, characteristic exponents
and semigroup `(2,7)`, conductor six, and local delta three.  Therefore,
for a uniformizer `tau`,

```text
Q=tau^2*(unit),
w=(1/52488)tau^6+O(tau^7),
ord(v)=-6.                                            (2.4)
```

The tempting split into two branches of pole order three is false.  It is
also incompatible with the zero discriminant and delta three.

### 2.4 Primitive lower edge

The edge from `(8,3)` to `(0,0)` has primitive lattice length one.  Its
two-term face has one simple boundary point, with

```text
(ord(q),ord(v))=(-3,8).                               (2.5)
```

This is the only zero of `v`.

## 3. Normalization genus and the divisor of `v`

The toric arithmetic genus is the seven interior lattice points.  The only
singularities of the closure are the four ordinary torus nodes and the one
top `(2,7)` cusp.  The left tangency and the two primitive-edge points are
smooth, and there are no toric-fixed-point intersections.  Hence

```text
g(X)=7-4*1-3=0.                                       (3.1)
```

Equations (2.1), (2.4), and (2.5) give the complete principal divisor

```text
div_X(v)=8P_0-P_ul-P_A-6P_B.                          (3.2)
```

The zero and pole degrees are both eight, an independent completeness
check.  The left tangency is absent from (3.2) because `v=81/22` is a
unit there.

## 4. Exact Kummer Riemann--Hurwitz

The odd valuations at `P_ul` and `P_A` show that the class of `v` has exact
order four in `Q(X)^*/Q(X)^{*4}`.  Thus (0.2) is an irreducible cyclic
degree-four cover.  A place of valuation `n` contributes

```text
4-gcd(4,n)
```

to the ramification divisor.  The complete table is

| place | `ord(v)` | points above | inertia | contribution |
|---|---:|---:|---:|---:|
| `P_0` | `8` | 4 | 1 | 0 |
| `P_ul` | `-1` | 1 | 4 | 3 |
| `P_A` | `-1` | 1 | 4 | 3 |
| `P_B` | `-6` | 2 | 2 | 2 |

Therefore `R=8`, and Riemann--Hurwitz gives

```text
2g(Y)-2=4(2g(X)-2)+8=-8+8=0,
g(Y)=1.                                                 (4.1)
```

This calculation includes every point at infinity and does not use the
false nondegenerate-polygon genus `37` for `P(q,y^4)`.

## 5. Evidence ledger and next exact gate

Charged exact outputs:

```text
706505e02f57e6991170e230738d6a8b96b5ac82ed2ec3fa83b1ba8ff498508d
  reconstructed candidate JSON
9b0e08c2d826286364f07f6a6fba9560e23ca8ea4fcba15cbbcf373152badbe3
  exact membership/irreducibility/four-node stdout
b7aa07121bc761acd8dd0a3342bb8f5321da8e38c4068859edb23e0b8d0094ff
  exact face identities, discriminant, and left-transverse stdout
4791594d69326fc6725e72bd15b6900988cc04f18fa7aaf050fa306c63c33a0a
  exact local-delta stdout
59c2c35f2288f6c983925dba4a855a28e49eadc9d9db5ef84aa78b6bed2a971d
  exact Hamburger--Noether stdout
```

The highest-priority successor is componentwise, exact characteristic-zero
elimination from the corrected ideal:

1. verify `a_6` saturation causes no chart loss;
2. compute every relevant minimal component of the `r_7`-saturated source;
3. prove its contraction to `Q[q,y]` is the irreducible equation
   `P(q,y^4)` (or at least has one-dimensional image);
4. prove `rho=r_7^4` cannot vary in a vertical `(q,y)` fibre.

Only after this projection gate and a hostile review may (4.1) be promoted
to a complete elimination of the `mu_4 != 0` order-four leaf.  If the gate
fails on a component, that component must be treated separately; neither
the residual genus zero nor the terminal passport alone removes it.
