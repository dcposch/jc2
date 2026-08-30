# Rank-four `R4-CYCLE-1`: cyclic birational deck transformations and the line-complement control

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`rank4_cycle1_function_pair` lane)  
Frozen basis: `69d0199b4d949e96aacb19a7795ca904769a066f`  
Lifecycle: **FINAL+VERIFIED EXACT CONDITIONAL SUCCESSOR / COMPLEMENT CLASSIFIED / PSEUDO-PLANE COUNTERCONTROL / HORN OPEN**

## 0. Verdict

Work conditionally under the verified `R4-CYCLE-1` producer.  Write

```text
H=(H_1,H_2)=pi o f_mu : X=A2 -> A2,
L=C(x,y),             K=C(H_1,H_2),
M=C(U)=K(x^mu),       mu>=2,
```

and let `sigma` generate the cyclic deck group of `L/M`, with
`sigma(x)=zeta x` for a primitive `mu`-th root `zeta`.  Formanek gives both
`L=K(x)` and `L=K(y)`.

The off-diagonal graph of every `sigma^k`, `1<=k<mu`, is an irreducible
component of the etale fibre product

```text
X times_H X.
```

Both graph projections are birational etale maps and hence open immersions.
Their domains can be identified exactly from the full cyclic cover.  If
`L_0,...,L_(mu-1)` are the cyclic lines and `X` retains `L_0`, then every
nontrivial deck graph is the graph of an isomorphism

```text
D = X-L_0  -->  D = X-L_0.                         (0.1)
```

The maps do **not** create `mu-1` new affine complements.  All off-diagonal
graphs share the same missing affine line.  On the full cover `sigma^k`
sends `L_0` isomorphically to the already deleted line `L_k`; it neither
contracts `L_0` nor needs another finite exceptional curve.  Thus the lost
domain in (0.1) is a pole-to-an-existing-boundary event for an auxiliary
correspondence, not a new Orevkov--Chau contribution for `H`.

There is also an exact coordinate classification.  Since `H o sigma=H` and
`J(H)` is a nonzero constant, `J(sigma)=1`.  Every automorphism of
`D=Spec C[x,x^(-1),y]` with `sigma(x)=zeta x` therefore has the form

```text
sigma(x)=zeta x,
sigma(y)=zeta^(-1)y+h(x),       h in C[x,x^(-1)].    (0.2)
```

Finite order is equivalent to the absence from `h` of every Laurent
monomial `x^n` with

```text
n = -1 mod mu.                                      (0.3)
```

Moreover (0.2) is rationally conjugate, by `Y=y+g(x)`, to

```text
(x,Y) |-> (zeta x,zeta^(-1)Y).                      (0.4)
```

The function `h` must have a negative Laurent term: otherwise the conjugacy
is polynomial, the action has a finite fixed point, and etaleness of `H`
forces the action to be the identity.  If `r` is its leading pole order,
then the new exact necessary condition is

```text
r != 1 mod mu.                                      (0.5)
```

Condition (0.5) is not a contradiction.  In fact the affine surfaces

```text
Z_(r,mu): x^r z=w^mu-1,
gamma(x,w,z)=(zeta x,zeta w,zeta^(-r)z),             (0.6)
```

with `r=2 mod mu`, give a global sharp control.  The action is free, its
quotient `U_(r,mu)=Z_(r,mu)/<gamma>` is smooth affine, and

```text
K_(U_(r,mu))=0,        Pic(U_(r,mu))=Z/mu,
div(t)=mu Phi for t=x^mu,
```

with exactly one multiple `A1` fibre.  The full cover has `mu` disjoint
lines over that fibre, and deleting all but one gives `A2`.  In the retained
chart the deck generator is exactly

```text
(x,y) |->
(zeta x,
 zeta^(1-r)y+(zeta-1)zeta^(-r)x^(-r)),              (0.7)
```

which is volume-preserving precisely for `r=2 mod mu`.  It has only the
single affine pole line `x=0` and realizes the entire cyclic valuation orbit
without an extra affine event.

Therefore neither finite order, `K_U=0`, `Pic(U)=Z/mu`, the multiple-fibre
geometry, nor line-complement classification closes the horn.  The quartic
Keller map remains essential.  The sharp successor gate is now one of:

1. prove that the quartic map and its saturated `(3,1)+(2,2)` census force
   a pole order incompatible with `r!=1 mod mu` (the pseudo-plane model
   predicts the sharper class `r=2 mod mu`);
2. prove that an endpoint of the cyclic valuation orbit must be an
   additional **nonconstant `H`-dicritical**, not merely another component
   in an equivariant completion; or
3. exclude two invariant Keller polynomials in the Laurent-Jonquieres model
   by exploiting the degree-four intermediate extension.

The earlier monogenic-index route remains dead at its exact scope: an index
divisor does not become an Orevkov term without such a global coupling.

## 1. Frozen inputs and scope

The exact inputs are the following sealed artifacts.

```text
0a6272060a03c0071ad8b4c71aef00f3c724284d9590dcab61a2e75169a8713f
  xmodel/block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md
32780967e3567ae1acc325e70798d78157d86127b7304f52079fef798009b6f1
  xmodel/block-descent-a1-quartic-cycle1-function-pair-hostile-review-gpt55-20260830.md
bcc5148aba1a6cb095401ae8871e184ba6bb3e540395a23c40edc16cb0e363a8
  xmodel/block-descent-a1-quartic-cycle1-kummer-inverse-collision-control-sol56-20260830.md
4eb16c9422fd167646d7161a359d05f95deaf5925d4650b3822b395329e124b4
  xmodel/block-descent-a1-quartic-cycle1-index-at-infinity-resultant-control-sol56-20260830.md
```

The producer supplies a connected finite-etale cyclic cover

```text
q: Z=tilde U -> U
```

of degree `mu`.  Above the unique multiple fibre `Phi`, its reduced inverse
image is a disjoint union

```text
q^* Phi = L_0+...+L_(mu-1),      L_j=A1,
```

and the deck group acts transitively on these lines.  Put

```text
X_j=Z - union_(i!=j) L_i = A2,
D=Z - union_i L_i.
```

The retained source is `X=X_0`.  Thus `D=X-L_0=A1* times A1`.  The cyclic
base coordinate is normalized so that

```text
t=rho o f_mu=a+c x^mu,
sigma(x)=zeta x.
```

The quartic map `pi:U->A2-B` and the cover give the Keller map `H` on `X`.
The group fixes `U`, hence fixes both `H_1,H_2` in the function field.

This report classifies the resulting open deck transformations and gives a
global pseudo-plane control.  It does not construct a quartic `pi`, a Keller
counterexample, or a realization of the saturated companion census.

## 2. The off-diagonal components are open immersions

Let

```text
W=X times_H X
```

with projections `p_1,p_2`.  Because `H` is etale, each projection is its
base change and hence is etale.  In particular `W` is regular.  Its
irreducible components are therefore disjoint open-and-closed smooth
surfaces.

For `1<=k<mu`, the rational identity

```text
H o sigma^k=H
```

puts the generic graph of `sigma^k` in `W`.  Its closure `C_k` is an
irreducible component of `W`.  Both maps

```text
p_i|C_k:C_k->X
```

are etale and birational.  An etale map is quasi-finite and separated; by
Zariski Main Theorem a birational quasi-finite map to the normal surface
`X` is an open immersion.  Consequently `C_k` is the graph of an
isomorphism between two open subsets of `X`.

This conclusion is stronger than merely saying that `sigma^k` is a Cremona
map.  It rules out finite ramification and contractions inside its maximal
graph domain.  It does not say that the open subset is all of `X`.

## 3. Exact domains from the full cyclic cover

The deck automorphism is regular on all of `Z` and satisfies

```text
sigma^k(L_j)=L_(j+k).
```

Every point of `D` stays in `D`, so `sigma^k` restricts to an automorphism
of `D`.  On the other hand, for `1<=k<mu`, a point of the retained line
`L_0` is sent to `L_k`, which is absent from `X_0`.  Therefore the graph map
inside `X times X` has domain exactly

```text
Dom_X(sigma^k)=D=X-L_0.                              (3.1)
```

There cannot be a hidden finite extension across a point of `L_0`.  Indeed,
`sigma^k:X->Z` is already a regular map and sends that point into `L_k`.
Any extension to `X` composed with the open immersion `X->Z` would agree
with this regular map on a dense open set, hence everywhere by separatedness
of `Z`; its value would have to lie simultaneously on `L_k` and in `X`, an
impossibility.

The inverse argument gives the same target domain.  Thus

```text
C_k = Graph(sigma^k|D),
p_1(C_k)=p_2(C_k)=D.                                 (3.2)
```

In particular:

* all `mu-1` off-diagonal graph components omit the **same** line `L_0` in
  the retained affine plane;
* `L_0` is not contracted--it is mapped isomorphically to `L_k` in `Z`;
* there are no additional finite base points or finite exceptional curves;
* the apparent failure of regularity is solely the use of the wrong affine
  chart on the target.

On `X_k`, the same deck map is regular across `L_0`.  Thus `Z`, or just the
two charts `X_0` and `X_k`, resolves the affine pole without a blow-up.

## 4. Valuation orbit and the saturated budget

Let `v_j` be the divisorial valuation of `L_j` on `Z`.  Its centre on the
retained `X` is

```text
centre_X(v_0)=L_0,
centre_X(v_j) is at infinity for j!=0.                (4.1)
```

The deck generator cyclically permutes these `mu` valuations.  The common
core `D` is exactly the open set on which none of them has a centre.

In the saturated Orevkov--Chau ledger for `H`, the `mu-1` deleted lines
`L_1,...,L_(mu-1)` already contribute one apiece.  Equations (3.1)--(4.1)
do not add another term:

1. `L_0` is an affine curve of the source of `H`, not a source boundary
   dicritical;
2. the deletion of `L_0` occurs only when one asks that an auxiliary deck
   correspondence have both source and target in the same affine chart;
3. on `Z`, `L_0->L_k` is an isomorphism, so no local mapping multiplicity
   jumps there;
4. resolving an equivariant projective completion may add endpoint
   divisors, but Orevkov's identity counts a component only when `H` is
   nonconstant on it.  Finite group geometry alone does not imply that.

Thus “one off-diagonal graph, one new budget unit” is false.  The graph
components reuse the same cyclic valuation orbit that produced the already
charged deleted lines.

## 5. Coordinate classification on `A1* times A1`

The coordinate ring of `D` is

```text
R=C[x,x^(-1),y].
```

Because `sigma(x)=zeta x`, `sigma` preserves the Laurent subring
`C[x,x^(-1)]`.  An automorphism of the one-variable polynomial ring over
this subring has degree one in `y`; hence

```text
sigma(y)=u(x)y+h(x),
u in C[x,x^(-1)]^*,       h in C[x,x^(-1)].           (5.1)
```

The Keller identity determines the unit.  Since `H o sigma=H` as rational
maps and `J(H)=c_H in C*`, the chain rule gives

```text
c_H=c_H J(sigma),       so J(sigma)=1.
```

Using `sigma(x)=zeta x` in (5.1) gives `J(sigma)=zeta u(x)`.  Therefore

```text
u(x)=zeta^(-1),
sigma(x,y)=(zeta x,zeta^(-1)y+h(x)).                  (5.2)
```

This is a volume-preserving Laurent-Jonquieres transformation.  It is an
automorphism of `D`, while negative terms of `h` are exactly its affine pole
along `L_0`.

Formanek's second equality `L=K(y)` adds primitivity, not regularity.  It
ensures that no nontrivial deck element fixes `y`, but (5.2) already makes
that clear from its nontrivial linear coefficient.  It gives no reason for
`h` to lie in `C[x]`.

## 6. Finite order, rational linearization, and the pole congruence

Iterating (5.2) gives

```text
sigma^mu(y)
 =y+sum_(j=0)^(mu-1) zeta^(-(mu-1-j))h(zeta^j x).    (6.1)
```

For a Laurent monomial `a_n x^n`, its contribution to the sum is a nonzero
constant times

```text
sum_(j=0)^(mu-1) zeta^(j(n+1)).                      (6.2)
```

The sum in (6.2) vanishes unless `n=-1 mod mu`.  Hence `sigma^mu=1` is
equivalent to

```text
a_n=0 whenever n=-1 mod mu.                          (6.3)
```

For every allowed exponent, solve coefficientwise

```text
h(x)=zeta^(-1)g(x)-g(zeta x).                        (6.4)
```

Then the Laurent change `Y=y+g(x)` conjugates (5.2) to

```text
sigma(x,Y)=(zeta x,zeta^(-1)Y).                      (6.5)
```

If `h` had no negative term, (6.4) could be solved with `g in C[x]`; the
conjugacy would be a polynomial automorphism of `A2`.  The linear action in
(6.5) has a fixed point, so the original action would also have a finite
fixed point `p`.  Since `H` is etale, it is analytically injective near `p`.
The identity `H o sigma=H` would force `sigma` to be the identity germ and
hence the identity rational map, contradicting `zeta!=1`.  Thus `h` has a
pole at `x=0`.

If `r>=1` is the largest integer for which an `x^(-r)` term occurs, (6.3)
gives the exact constraint

```text
r != 1 mod mu.                                       (6.6)
```

This is the first nontrivial numerical information obtained from the
finite-order Keller symmetry.  The next sections show why it is not yet a
contradiction.

## 7. A local complement control for every `mu`

For every `mu>=2`, take

```text
tau(x,y)=(zeta x,zeta^(-1)y+x^(-2)).                 (7.1)
```

The exponent `-2` is nonresonant for every `mu`, so (6.1) proves
`tau^mu=1`.  Its order is exactly `mu` because its first coordinate is
multiplied by the primitive root `zeta`.  It has Jacobian one and is regular
on `D=A1* times A1`; its sole affine pole divisor is `x=0`.

With

```text
g(x)=x^(-2)/(zeta^(-1)-zeta^(-2)),
Y=y+g(x),
```

the action is `(x,Y)|->(zeta x,zeta^(-1)Y)`.  It is free on `D`, and

```text
C[x,x^(-1),Y]^<tau>
  =C[X,X^(-1),S],       X=x^mu,       S=xY.           (7.2)
```

Thus `D->Spec C[X,X^(-1),S]` is a finite-etale cyclic cover of degree `mu`.
This exact model has a full finite-order complement action, a retained
valuation that escapes to infinity under every nontrivial iterate, and no
additional affine exceptional curve.  It does not carry an invariant
Keller pair on all of `A2`; it is a firewall against a conclusion based
only on finite order, Jacobian one, or line-complement geometry.

## 8. Global pseudo-plane control with `K=0` and `Pic=Z/mu`

The stronger control is the smooth affine hypersurface

```text
Z=Z_(r,mu)={x^r z=w^mu-1} in A3,                    (8.1)
```

where `r>=1`, together with

```text
gamma(x,w,z)=(zeta x,zeta w,zeta^(-r)z).             (8.2)
```

### 8.1 Smoothness, freeness, and the cyclic fibre

The roots of `w^mu-1` are simple, so (8.1) is smooth, including along
`x=0`.  A nontrivial `gamma^k` cannot fix a point with `x!=0`.  If `x=0`,
then `w^mu=1`, so `w!=0`, and it cannot fix `w` either.  Hence the action is
free and the quotient

```text
q:Z->U=Z/<gamma>
```

is finite etale of degree `mu`, with `U` smooth affine.

The invariant function `t=x^mu` defines an `A1`-fibration on `U`.  For
`t!=0`, the `mu` choices of `x` are permuted simply transitively and each
chosen fibre is `A1_w`.  At `t=0`, the cover fibre is the disjoint union

```text
L_alpha={x=0,w=alpha}=A1_z,       alpha^mu=1,
```

and these `mu` lines are again permuted simply transitively.  Their quotient
is one reduced line `Phi`, while

```text
div_U(t)=mu Phi.                                      (8.3)
```

Thus this is exactly the cyclic multiple-fibre geometry used in the horn.

### 8.2 The `A2` retained charts and the pole order

Fix a root `alpha`.  Deleting the other `mu-1` lines gives

```text
X_alpha=Z-union_(beta!=alpha)L_beta = A2.
```

Indeed, with

```text
y_alpha=(w-alpha)/x^r,
Q_alpha(w)=(w^mu-1)/(w-alpha),
```

the inverse coordinate formulas are

```text
w=alpha+x^r y_alpha,
z=y_alpha Q_alpha(alpha+x^r y_alpha).                 (8.4)
```

For the retained root `alpha=1`, write `y=y_1`.  Re-expressing (8.2) in the
same retained chart on the common core gives

```text
x' =zeta x,
y' =(zeta w-1)/(zeta^r x^r)
   =zeta^(1-r)y+(zeta-1)zeta^(-r)x^(-r).              (8.5)
```

This has exactly one affine pole line.  It sends the retained line to the
next deleted line on `Z`, and its nontrivial iterates share the same affine
domain `x!=0`.

### 8.3 Canonical class

The residue form

```text
omega=dx wedge dw / x^r                              (8.6)
```

is regular and nowhere zero on `Z`: in every chart (8.4), it is
`dx wedge dy_alpha`.  Under the deck generator,

```text
gamma^*omega=zeta^(2-r) omega.                        (8.7)
```

Consequently, whenever

```text
r=2 mod mu,                                          (8.8)
```

the form descends to a nowhere-zero two-form on `U`, and `K_U=0`.  In the
same congruence class, (8.5) has linear coefficient `zeta^(-1)` and
Jacobian one, exactly as forced by the Keller calculation (5.2).

Thus `K_U=0` is compatible with the pole.  In this standard family it
selects `r=2 mod mu`, which is safely nonresonant rather than contradictory.

### 8.4 Picard group

Localizing (8.1) at `x` gives

```text
O(Z)[x^(-1)]=C[x,x^(-1),w],
```

a UFD.  Hence `Pic(Z)=Cl(Z)` is generated by the `mu` components `L_alpha`
of `x=0`.  The only relation is

```text
sum_alpha [L_alpha]=div(x)=0.                         (8.9)
```

Indeed, a rational function with divisor supported on `x=0` is a unit after
localization, hence is `c x^n`.  Therefore

```text
Pic(Z)=Z^mu / Z(1,...,1).                             (8.10)
```

The cyclic permutation has no invariant in this quotient: if a vector and
its shift differ by a diagonal vector, summing coordinates shows that
diagonal difference is zero, and the original vector is diagonal.

Also `O(Z)^*=C*`.  The low-degree descent sequence for the free cyclic cover
then gives

```text
0 -> H^1(C_mu,C*) -> Pic(U) -> Pic(Z)^(C_mu),
```

so (8.10) yields

```text
Pic(U)=Hom(C_mu,C*)=Z/mu.                             (8.11)
```

Equations (8.3), (8.8), and (8.11) simultaneously realize all three
pseudo-plane invariants that might otherwise have been expected to force an
extra cyclic boundary event.

For completeness, `e(Z)=mu`: the `x!=0` part contributes
`e(C*)e(A1)=0`, while the zero fibre contributes `mu`.  Since the action is
free, `e(U)=1`.

## 9. The remaining quartic algebraic gate

Use the Laurent linearization from (6.4):

```text
X=x^mu,             Y=y+g(x),             S=xY.
```

Then

```text
M=L^<sigma>=C(X,S),
M=K(X),             [M:K]=4.                          (9.1)
```

Write the two invariant Keller polynomials as rational functions

```text
H_i=F_i(X,S).
```

The quotient coordinates have the exact logarithmic Jacobian

```text
J_(x,y)(X,S)=mu x^mu=mu X,
J_(X,S)(F_1,F_2)=J(H)/(mu X).                         (9.2)
```

Thus the unresolved algebraic problem is very concrete: two rational
functions `F_i` in the fixed field must pull back, after the Laurent shift,
to polynomials in `x,y`, have the logarithmic Jacobian (9.2), and generate a
quartic subfield `K` with the already fixed boundary census.  The
pseudo-plane countercontrol satisfies everything before the existence of
these two quartic Keller functions.

This suggests two bounded computational attacks, to be run on AWS rather
than locally.

1. For fixed small `(mu,r)` with `r=2 mod mu`, parameterize polynomial
   invariants of the transformation (8.5), impose constant Jacobian, and
   eliminate coefficients degree by degree.  A proof requires a symbolic
   pattern or theorem; finite failure is only reconnaissance.
2. Express the quartic minimal polynomial over `K` in `(X,S)` coordinates
   and impose the exact `(3,1)+(2,2)` boundary factorization.  Test whether
   it forces a resonant `x^(-1 mod mu)` term, which (6.3) forbids, or an
   additional nonconstant endpoint valuation.

The most attractive theoretical lemma is:

> **Quartic pole lemma sought.**  In the one-cusp minimal quartic horn, the
> saturated boundary packets force the transition exponent of the cyclic
> retained chart to be `1 mod mu`, or force a further `H`-dicritical.

The exact pseudo-plane family proves that `K_U=0`, `Pic(U)=Z/mu`, and the
multiple fibre cannot replace the words “quartic” and “boundary packets” in
this lemma.

## 10. Quarantine and row separation

Do not promote any of the following statements.

1. Every off-diagonal graph component costs a new Orevkov unit.
2. A finite-order birational self-map of `A2` is automatically regular.
3. The missing line in the deck graph is an exceptional curve contracted
   by the deck action.
4. `L=K(y)` makes `sigma(y)` polynomial.
5. `K_U=0` or `Pic(U)=Z/mu` forces pole order one.
6. Every divisor needed in an equivariant projective completion is an
   `H`-dicritical.
7. The model (8.1) carries the quartic etale map `pi`, realizes the companion
   census, or is a Jacobian counterexample.
8. A monogenic index divisor contributes to the Orevkov budget; the sealed
   index-at-infinity control has already disproved that implication at its
   stated level of generality.

For the strict-block horn, `d_1>=2` and the conditional minimal-degree
replacement gives `mu=d_1`.  The canonical `d_1=1` pseudo-plane row remains
empty under `mu>=2` and `mu|d_1`.  The global controls above exist for every
`mu>=2`; they are controls on the pseudo-plane and cyclic-symmetry inputs,
not promotions to arbitrary canonical rank-four configurations.

No replay is attached.  All finite-order, Jacobian, Picard, and chart
identities above are symbolic for arbitrary `mu` and `r`; finite sampling
would add no verification.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20767`.
- Body SHA-256:
  `2627602bb77fa8583fc592e51e9cdf5c53fdbceac93cf16c9df2724495c6c271`.
- Frozen basis: `69d0199b4d949e96aacb19a7795ca904769a066f`.
