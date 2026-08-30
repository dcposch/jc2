# Rank-four `R4-CYCLE-1`: invariant-ring polynomiality and the sharp quartic gate

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`rank4_cycle1_function_pair` lane)  
Frozen basis: `def7eadcef743e041b1fbd0a508fd450512af49c`  
Lifecycle: **FINAL+VERIFIED EXACT CONDITIONAL SUCCESSOR / POLYNOMIALITY CLASSIFIED / DEGREE-INDEPENDENT NO-GO NEGATIVE / QUARTIC GATE OPEN**

## 0. Verdict

Continue conditionally from the sealed cyclic-deck classification.  Put

```text
A=C[x,y],                       L=Frac(A),
K=C(H_1,H_2),                   M=C(U),
X=x^mu,                         M=K(X),
[L:M]=mu,                       [M:K]=4.
```

After a polynomial vertical change and a Laurent translation, the deck
generator has

```text
Y=y+g(x),
sigma(x,Y)=(zeta x,zeta^(-1)Y),
S=xY,
M=L^<sigma>=C(X,S).                                  (0.1)
```

The polynomiality intersection has an exact intrinsic answer:

```text
A intersect M = O(U).                                (0.2)
```

Moreover, if `Phi` is the unique multiple fibre and
`nu=ord_Phi`, then

```text
O(U-Phi)=C[X,X^(-1),S],
O(U)=C[X,X^(-1),S] intersect O_(U,eta_Phi),           (0.3)
```

inside `M`.  Equivalently, an invariant Laurent polynomial is a polynomial
in the retained `(x,y)` chart exactly when its single possible pole at the
divisorial valuation `nu` cancels.  If `r>=2` is the leading pole order of
`g`, then

```text
nu(X)=mu,                     nu(S)=1-r.              (0.4)
```

Thus polynomiality is not a second independent boundary condition: it is
regularity on the pseudo-plane itself.

The Keller equation becomes the exact logarithmic Jacobian equation

```text
H_i=F_i(X,S) in O(U),
J_(X,S)(F_1,F_2)=c/(mu X),          c in C*.           (0.5)
```

The apparent pole in (0.5) is the coordinate expression of the nowhere-zero
canonical form on `U`; it is compatible with `K_U=0` and is not by itself a
contradiction.

In the primitive single-pole case there is a completely explicit invariant
ring.  Let `r>=2`, `d=r-1`, `g=x^(-r)`, and assume `gcd(d,mu)=1`.  Set

```text
w=1+x^r y,                   z=(w^mu-1)/x^r.
```

Then the full cover and quotient are

```text
Z: x^r z=w^mu-1,
gamma(x,w,z)=(zeta x,zeta^d w,zeta^(-r)z),
O(U)=O(Z)^<gamma>.                                  (0.6)
```

Every invariant polynomial is a linear combination of monomials

```text
x^a w^b z^c,       a+d b-r c=0 mod mu,               (0.7)
```

modulo the displayed hypersurface relation.  Its pullback to the retained
plane is explicitly polynomial.  The restriction `O(U)->O(Phi)=C[y]` is
surjective, and there are two explicit invariant functions whose pulled-back
Jacobian is the nonzero constant `mu` **along the whole retained line**.
So neither polynomiality nor first-order etaleness along `Phi` obstructs an
immersive nodal `C_0`.

Degree four first enters only after this ring theory.  At the generic point
of `C_0`, `nu|K` is unramified with residue degree one, and the other three
quartic sheets can remain etale.  An exact split-DVR model with primitive
element values `(u^mu,1,2,3)` realizes this for every `mu`.  Hence no local
valuation or discriminant argument can close the horn.

The remaining problem is genuinely global and quartic:

> Exclude a subfield `K=C(F_1,F_2)` of index four in `M=C(X,S)` for which
> `F_i` lie in the single-valuation intersection (0.3), satisfy (0.5), and
> have the already saturated `(3,1)+(2,2)` boundary census.

Section 8 gives a bounded AWS reconnaissance packet.  It should be treated
as a pattern finder, not a proof.

## 1. Frozen input and exact scope

The direct input is the sealed deck-control artifact

```text
422bddb764966c9191703c16490d741d3f75d851277a706c6618ba78fdc4395d
  xmodel/block-descent-a1-quartic-cycle1-cyclic-birational-deck-control-sol56-20260830.md
```

together with its verified producer and the inverse-Kummer/index controls.
The deck artifact proves that every nontrivial cyclic graph has common
domain

```text
D=A2-{x=0}=A1* times A1
```

and that its action on `D` has the form (0.1), where `g` is Laurent and has
a negative term.  The cyclic cover `q:tilde U->U` is finite etale, and the
retained open `f_mu:X=A2->U` is surjective etale.

This report characterizes the intersection ring for the actual conditional
horn.  The hypersurface in (0.6) is an exact global control for the
single-pole case; it is not asserted that every pseudo-plane in the horn has
this presentation.

The same universal-cover hypersurfaces and free cyclic actions occur in the
primary pseudo-plane literature: A. Dubouloz and K. Palka, *The Jacobian
Conjecture fails for pseudo-planes*, Adv. Math. 339 (2018), 248--284,
DOI `10.1016/j.aim.2018.09.020`, preprint
`https://arxiv.org/abs/1701.01425`.  That paper also proves that broad
classes of pseudo-planes admit nonproper etale endomorphisms.  This is used
only as an external warning against a degree-independent properness claim;
all ring identities below are proved directly.

## 2. Descent identifies the intersection with `O(U)`

View `M=C(U)` as a subfield of `L=C(x,y)` through `f_mu`.  The inclusion

```text
O(U) subseteq A intersect M
```

is immediate.  For the reverse inclusion, take `f in A intersect M`.  It is
a rational function on the normal smooth surface `U` whose pullback to `X`
is regular.

For every prime divisor `E` on `U`, surjectivity of `f_mu` gives a prime
divisor `E'` on `X` above it.  Since `f_mu` is etale, its ramification index
at these generic points is one, and

```text
ord_E(f)=ord_(E')(f_mu^*f)>=0.
```

A rational function on a normal affine variety is regular exactly when all
of its codimension-one orders are nonnegative.  Hence `f in O(U)`, proving

```text
C[x,y] intersect M=O(U).                              (2.1)
```

This also follows from faithfully flat descent, but the valuation proof
makes the later boundary statement transparent.

## 3. Only one valuation controls polynomiality

Remove the multiple fibre.  The full cyclic cover restricts to

```text
D -> U-Phi,
```

a finite-etale Galois cover with group `C_mu`.  Since the Laurent change
`Y=y+g(x)` is regular on `D`,

```text
O(D)=C[x,x^(-1),Y].
```

The diagonal action in (0.1) has invariant ring

```text
O(D)^(C_mu)=C[X,X^(-1),S],
X=x^mu,                         S=xY.                 (3.1)
```

Indeed every invariant monomial `x^aY^b` has `a-b=0 mod mu` and, because
`x` is invertible, is a Laurent power of `X` times a power of `S`.
Therefore

```text
O(U-Phi)=C[X,X^(-1),S].                               (3.2)
```

The complement of `U-Phi` in the smooth normal surface `U` is the single
prime divisor `Phi`.  The Krull-domain intersection theorem gives

```text
O(U)=O(U-Phi) intersect O_(U,eta_Phi)
    =C[X,X^(-1),S] intersect O_(U,eta_Phi)            (3.3)
```

inside `M`.  Write `nu=ord_Phi`.  The etale line `L_0->Phi` has degree one,
so `nu` is computed after pullback by the `x`-adic order at the generic
point of `L_0`.  Since

```text
X=x^mu,                  S=xy+xg(x)
```

and `g` has leading term `c_r x^(-r)`, `c_r!=0`, one obtains

```text
nu(X)=mu,                nu(S)=1-r.                   (3.4)
```

Concretely, every element of (3.2) is a finite Laurent polynomial
`F(X,S)`.  Substitute `X=x^mu` and `S=xy+xg(x)` and collect powers of `x`.
Membership in (3.3) is exactly cancellation of all negative powers.  The
coefficients retain the residue parameter `y`, so cancellations, rather
than a naive scalar weight inequality, matter.

This is the degree-independent polynomiality classification.  It contains
no reference to the quartic subfield `K`.

## 4. The logarithmic Jacobian equation

The Laurent translation has determinant one, and

```text
dX wedge dS
 =d(x^mu) wedge d(xY)
 =mu x^mu dx wedge dy
 =mu X dx wedge dy.                                  (4.1)
```

Write `H_i=F_i(X,S)` using `H_i in M`.  The chain rule and the constant
Jacobian `J_(x,y)(H_1,H_2)=c` yield

```text
J_(X,S)(F_1,F_2)=c/(mu X).                            (4.2)
```

On `U-Phi`, the right side is a unit.  Across `Phi`, the pair `(X,S)` is not
a regular coordinate system: `X` vanishes to order `mu` and `S` has a pole.
Consequently the pole in (4.2) is not ramification of `pi`.  It is the
Laurent expression of the regular nowhere-zero form

```text
dx wedge dy=(dX wedge dS)/(mu X).                     (4.3)
```

This is precisely compatible with `K_U=0`.

The field condition is separate:

```text
K=C(F_1,F_2),                 [M:K]=4,
M=K(X).                                              (4.4)
```

Equations (3.3), (4.2), and (4.4), together with the boundary packet, are
the exact quartic algebraic gate.  Dropping any one of them loses essential
information.

## 5. Explicit intersection in the primitive single-pole model

This section gives a sharp global control on (3.3).  Fix `r>=2`, put
`d=r-1`, assume `gcd(d,mu)=1`, and take

```text
g(x)=x^(-r),             Y=y+x^(-r),
w=x^rY=1+x^r y,
z=(w^mu-1)/x^r
 =y(1+w+...+w^(mu-1)).                                (5.1)
```

Both `w` and `z` are polynomials in the retained `(x,y)` chart.  Let

```text
B=C[x,w,z]/(x^r z-w^mu+1).                            (5.2)
```

The diagonal action

```text
gamma(x,w,z)=(zeta x,zeta^d w,zeta^(-r)z)             (5.3)
```

preserves (5.2).  It is free: away from `x=0` the first coordinate has no
nontrivial stabilizer, while at `x=0` one has `w^mu=1`, and multiplication
by `zeta^d` is free on those roots because `gcd(d,mu)=1`.

The zero fibre consists of `mu` disjoint lines `x=0,w=alpha`.  The action
permutes them transitively.  Deleting all but `w=1` gives the retained `A2`
chart (5.1), and these translated charts cover `Spec B`.

If `f in C[x,y] intersect M`, invariance makes `f` regular on every
translated chart, hence on `Spec B`; conversely an invariant element of `B`
is polynomial on the retained chart.  Therefore

```text
C[x,y] intersect M=B^(C_mu).                          (5.4)
```

Because (5.3) is diagonal and its defining relation is invariant, (5.4) is
spanned as a `C`-vector space, and generated as an algebra, by the residue
classes of monomials

```text
x^a w^b z^c,
a,b,c>=0,                 a+d b-r c=0 mod mu.         (5.5)
```

Their retained-chart pullbacks are the explicit polynomials

```text
x^a(1+x^r y)^b
 y^c(1+w+...+w^(mu-1))^c,
w=1+x^r y.                                          (5.6)
```

Equations (5.5)--(5.6) are a finite Hilbert-basis description suitable for
bounded computation.  They also show why simply comparing the two weights
`nu(X),nu(S)` misses cancellations.

## 6. Polynomiality permits arbitrary line functions and an etale first jet

On the retained line `x=0`, formulas (5.1) give

```text
w=1,                         z=mu y.                  (6.1)
```

For any `c>=0`, choose `b>=0` with

```text
d b-r c=0 mod mu;
```

this is possible because `d` is invertible modulo `mu`.  The invariant
monomial `w^b z^c` restricts to `(mu y)^c`.  Hence

```text
B^(C_mu) -> C[y]
```

is surjective.  In particular, polynomiality imposes no degree or
injectivity restriction on the normalization parametrization of `C_0`.

There is also no first-order obstruction.  Choose `b,c` modulo `mu` so that

```text
1+d b=0 mod mu,
d c-r=0 mod mu.                                      (6.2)
```

Then

```text
u=x w^b,                    v=w^c z                  (6.3)
```

are invariant polynomials.  Along the entire retained line,

```text
u=x+O(x^(r+1)),             v=mu y+O(x^r),
J_(x,y)(u,v)|_(x=0)=mu.                                (6.4)
```

Thus the quotient already has explicit functions which are etale to first
order along `Phi` and give a coordinate on it.

They do not form a global Keller pair.  A direct calculation with the form
`dx wedge dw/x^r` gives

```text
{u,v}
 =w^(b+c-1)
   [(c+b r+mu)w^mu-(c+b r)],                          (6.5)
```

which specializes to `mu` at `w=1` but is nonconstant.  Equation (6.5) is
a useful sharp control: all polynomiality and local-etaleness conditions can
hold while the global constant-Jacobian equation remains the only failure.

## 7. What degree four does and does not force locally

Let `eta` be the generic point of `C_0`.  Since `pi|Phi` is the immersive
normalization of degree one and `pi` is etale at the generic point of
`Phi`, the valuation `nu` restricts to the `C_0`-adic valuation of `K` with

```text
e(nu/K)=1,                       f(nu/K)=1.             (7.1)
```

The other three sheets of the quartic extension can be etale as well.  This
is not merely a dimension count.  Put `k=C(y)`, `A_0=k[[u]]`, and consider
the rank-four etale algebra

```text
E=A_0 times A_0 times A_0 times A_0.
```

The element

```text
T=(u^mu,1,2,3)                                       (7.2)
```

is primitive, with polynomial

```text
(Z-u^mu)(Z-1)(Z-2)(Z-3).                             (7.3)
```

Its discriminant is a unit: the four residues `0,1,2,3` are distinct.  On
the first sheet `ord(T)=mu`, exactly as `nu(X)=mu`, while all four branches
are unramified and one has residue degree one.  A global quartic field can
have precisely this split completed algebra at the place.

Therefore the facts

```text
[M:K]=4,      M=K(X),      nu(X)=mu,
e=f=1 on Phi
```

do not force an index, discriminant, or local-degree correction.  To gain a
contradiction one must use the global minimal polynomial of `X`, the other
places above `C_0`, and the fixed `(3,1)+(2,2)` behavior over `B`.

The nodal self-identification of `C_0` also remains locally harmless: its two
normalization points are distinct etale points, so each has a completed
local model of the form (7.1).

## 8. Bounded AWS reconnaissance packet

No heavy computation was run locally.  The following packet is small enough
to shard over the available AWS cores and precise enough to return reusable
certificates.

### 8.1 Rings and bounds

Start with

```text
(mu,r)=(2,2),(3,2),(3,3),(4,2),(5,2),
d=r-1,                       gcd(d,mu)=1,
```

and source total-degree bounds `D=6,8,10,12`.  Generate the invariant
monomials (5.5) whose pullbacks (5.6) have degree at most `D`.  Compute a
minimal algebra generating set once, then express generic pairs `H_1,H_2`
in the bounded vector spaces.

### 8.2 Equations and filters

For each shard:

1. impose that every nonconstant coefficient of
   `J_(x,y)(H_1,H_2)` vanishes and the constant coefficient is nonzero;
2. work first modulo several good primes, then lift only zero-dimensional or
   structurally repeated components to characteristic zero;
3. use target affine changes and the explicit first-jet normalization (6.4)
   to remove redundant coefficients;
4. for a surviving symbolic component, compute the generic fibre degree of
   `(H_1,H_2)` and retain only degree `4mu`, equivalently test that `X` has
   degree four over `K=C(H_1,H_2)`;
5. only then impose the quartic boundary specialization and the
   `(2,1,1)/(3,1)/(2,2)` packet.

The output must include the monomial basis, the exact ideal, prime and
characteristic, Groebner/elimination certificate, and a characteristic-zero
verification for every promoted claim.  Empty bounded searches are
reconnaissance only.  A positive solution would be a plane Keller
counterexample and must be quarantined until exact independent verification.

### 8.3 Theoretical pattern to mine

The useful output is not “no solution through degree `D`.”  It is a stable
leading-form identity explaining why (4.2) cannot have a constant pullback,
or why every solution forces the degree of `X` over `K` away from four.
Equation (6.5) gives the first candidate pattern: a local symplectic pair
acquires an unavoidable nonconstant polynomial in the semi-invariant `w`.

## 9. Maximum-safe conclusion and quarantine

Promote exactly the following conditional statement.

> **Invariant-ring quartic gate.**  In the one-cusp cyclic horn,
> `C[x,y] intersect C(U)=O(U)`.  Removing the multiple fibre gives
> `O(U-Phi)=C[X,X^(-1),S]`, and reattaching it is the single valuation
> intersection (3.3).  The Keller condition is the logarithmic Jacobian
> equation (4.2), while the rank-four condition is the independent field
> condition (4.4).  In the primitive single-pole model, (5.4)--(5.6)
> explicitly characterize all polynomial invariants.  They realize arbitrary
> restrictions to `Phi` and an etale first jet.  A split quartic DVR model
> realizes the local degree-four data.  Hence a contradiction must use the
> global quartic boundary packet, not polynomiality, `K_U=0`, or one
> valuation alone.

Do not promote any of the following.

1. `A intersect M` is a polynomial ring; it is the pseudo-plane ring
   `O(U)`, generally with `Pic(U)=Z/mu`.
2. The pole `1/X` in (4.2) is ramification of `pi`.
3. The two values `nu(X),nu(S)` alone decide membership in `O(U)`; residue
   cancellations matter.
4. Every Laurent shift is conjugate to the single-pole model (5.1).
5. First-order etaleness of two invariant functions extends to a global
   Keller pair; equation (6.5) explicitly shows the gap.
6. The split algebra (7.2) is a global quartic field, realizes the cusp/node
   packets, or proves existence of `pi`.
7. Nonproper etale endomorphisms of pseudo-planes give plane Keller
   counterexamples; their target is the pseudo-plane, not `A2`.
8. A bounded AWS search proves a degree-independent theorem.

For the strict-block horn, `mu=d_1>=2` under the provisional minimal-degree
replacement.  The canonical `d_1=1` pseudo-plane row remains empty from
`mu|d_1`; nothing here changes that row separation.

No replay is attached.  The intersection, monomial, Jacobian, and split-DVR
controls are exact symbolic identities for arbitrary allowed parameters.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17661`.
- Body SHA-256:
  `922d978132064282164e8d607a26a4c62e474d52885dd9f7566a7846e4d64951`.
- Frozen basis: `def7eadcef743e041b1fbd0a508fd450512af49c`.
