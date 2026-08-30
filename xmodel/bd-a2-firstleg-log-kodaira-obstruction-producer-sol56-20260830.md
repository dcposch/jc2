# Producer: `BD-A2-FIRSTLEG` closes by logarithmic Kodaira dimension

Producer: Sol 5.6 Ultra  
Date: 2026-08-30 UTC  
Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`  
Lifecycle: **EXACT DESK PRODUCER / DIFFERENT-MODEL HOSTILE REVIEW REQUIRED**

## 0. Verdict

This packet takes as its exact input the residual geometry isolated in

```text
67e1305ba8dc452af6e120b37e24c102856ac5236d9140ffae9a0446c28261bc
  xmodel/bd-fix3-affine-linear-residual-control-producer-sol56-20260830.md
```

and the promoted block sandwich in

```text
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
```

The exact first-leg gate closes.

> **Theorem `BD-A2-FIRSTLEG`.**  Let `q:Y->P^1` be an affine-line torsor
> under a line bundle, and let `R subset Y` be a smooth curve such that
> `q|R:R->P^1 minus S` is an isomorphism, where `S` is a finite set with
> `#S>=2`, and the closure of `R` in the standard ruled compactification of
> `Y` meets the infinity section precisely over `S`.  Put `U=Y minus R`.
> Then
>
> ```text
> bar-kappa(U) >= 0.
> ```
>
> Consequently there is no dominant generically finite morphism
> `A^2_C->U`.

This is stronger than the requested exclusion.  It does not use etaleness,
quasi-finiteness at every point, the assertion that the image is `U` minus
finitely many points, the degree of the finite normalization, or any
restriction on redundant boundary sheets.  Those complications are real
for strong Zariski Main, but the log-Kodaira obstruction occurs before they
enter.

Applied to the affine-linear cubic residual, `#S=#Crit(rho)>=2` by the
degree-three Riemann--Hurwitz calculation already present in the input
producer.  Hence no `A^2` first leg exists.  Combined with `AL3-REDUCE`, this
provisionally excludes every affine-linear Miranda cubic block.

## 1. The ruled completion has two colliding sections

An affine-line torsor under a line bundle `L` on `B=P^1` has transition
functions

```text
y_i = ell_ij y_j + a_ij.
```

The same affine transformations act on `P^1`; adjoining the common point at
infinity therefore gives a smooth `P^1`-bundle

```text
qbar:P->B
```

with a distinguished infinity section `D_infinity` and

```text
Y=P minus D_infinity.
```

The closure `D_0` of `R` in `P` maps properly and with generic degree one to
`B`.  Since `B` is smooth, it is a section.  Over `B minus S`, it is the
given graph and is disjoint from `D_infinity`.  At a point of `S`, the graph
has no point in `Y`, so its unique limiting point lies on `D_infinity`.
Thus

```text
Supp(D_0 intersect D_infinity)=S,
U=P minus (D_0 union D_infinity).
```

Both sections are smooth.  They may be tangent, and their contact
multiplicities need not be one.  The proof below keeps those multiplicities
arbitrary.

The use of `O_P1(-3)` is therefore not load-bearing for this lemma.  It is
load-bearing upstream, where the cubic Miranda incidence construction
produces this torsor and identifies `S` with `Crit(rho)`.

## 2. A global logarithmic two-form

Because `D_0` and `D_infinity` both have fibre degree one, their class
difference is pulled back from `B`.  Hence there are a divisor `E` on `B`
and a rational function `phi` on `P` with

```text
div(phi)=D_infinity-D_0+qbar^*E
```

after possibly reversing `phi`.  The vertical term is harmless below.

Since `B=P^1` and `#S>=2`,

```text
deg(K_B+S)=#S-2 >= 0,
```

so choose

```text
0 != eta in H^0(B, Omega_B^1(log S)).
```

Define the rational two-form

```text
omega=qbar^*eta wedge dphi/phi.
```

It is nonzero: `eta` is nonzero and `phi` is nonconstant on the generic
fibre.  Multiplying `phi` by a rational function from `B` does not change
`omega`, because the extra base one-form wedges to zero with `qbar^*eta`.

Away from `D_0 intersect D_infinity`, the form has at worst a simple
logarithmic pole along each horizontal section.  A vertical zero or pole of
`phi` also causes no pole in `omega`: its singular contribution to
`dlog(phi)` is a base multiple of `dt/t`, whose wedge with the base form
`qbar^*eta` is zero.  The only point requiring a calculation is a collision
of the two sections.

## 3. Tangency audit: the form remains logarithmic

Fix `s in S`.  In smooth local coordinates `(t,w)` centered above `s`, take
`t` on the base and write

```text
D_infinity: w=0,
D_0:        w=a(t),
ord_t(a)=m>=1.
```

Up to multiplication by a base rational function,

```text
phi=w/(w-a(t)).
```

Because `eta` has at most a simple pole at `s`, write

```text
eta=h(t) dt/t
```

with `h` regular.  The base derivative in `d(w-a(t))` disappears after
wedging with `dt`, and one gets the exact local expression

```text
omega = -h(t) * (a(t)/t) * dt wedge dw / (w*(w-a(t))).       (3.1)
```

In particular, the apparent pole of `eta` is paid for by the collision
factor `a(t)`.

For completeness, resolve a contact of order `m` by the standard successive
point blowups.  In the chart at the `k`-th stage put

```text
w=t^k w_k,       1<=k<=m.
```

Ignoring units, the coefficient of (3.1) along the new exceptional divisor
is

```text
t^(m-1) * t^k / (t^k*t^k) = t^(m-k-1).
```

For `k<m` this has no exceptional pole.  At `k=m` it has exactly a simple
pole, while the two strict transforms meet the last exceptional divisor at
distinct points.  The denominators in the transverse coordinates are the
equations of the reduced boundary components, each to the first power.
The complementary blowup charts give the same valuation statement.

Thus on an embedded resolution

```text
rho:(P_tilde,D_tilde)->(P,D_0 union D_infinity),
D_tilde=(rho^-1(D_0 union D_infinity))_red,
```

the pullback `rho^*omega` is a nonzero global section of

```text
Omega^2_(P_tilde)(log D_tilde)
  = O_(P_tilde)(K_(P_tilde)+D_tilde).
```

Therefore the first logarithmic plurigenus is positive and

```text
bar-kappa(U)>=0.                                      (3.2)
```

This calculation is insensitive to repeated critical directions: it uses
the number of distinct collision fibres only to obtain `eta`, and retains
every contact multiplicity `m` in the resolution audit.

## 4. Why `A^2` cannot dominate `U`

The needed monotonicity is the elementary generically-finite case of the
logarithmic ramification formula:

> **Lemma 4.1.**  If `f:X->W` is a dominant generically finite morphism of
> smooth complex quasi-projective varieties, then
>
> ```text
> bar-kappa(X)>=bar-kappa(W).
> ```

Here is the complete argument in the present setting.  Take log-smooth
projective compactifications of `X` and `W`.  Resolve the rational extension
of `f`, using centers in the source boundary, to obtain a morphism

```text
fbar:(Xbar,D_X)->(Wbar,D_W)
```

with `D_X` simple normal crossing and containing the reduced inverse image
of `D_W`.  Pullback sends a logarithmic top form on `(Wbar,D_W)` to a
logarithmic top form on `(Xbar,D_X)`: locally, a generator `dy/y` pulls back
to `d(fbar^*y)/(fbar^*y)`, which has only simple logarithmic poles along the
reduced inverse-image divisor.  Tensor powers behave the same way.
Dominance and characteristic zero make pullback injective on nonzero top
forms.  Hence every logarithmic plurigenus of `W` is bounded above by the
corresponding one of `X`, proving the lemma.

For `A^2`, use the standard completion

```text
(P^2,H_infinity).
```

Then

```text
K_(P^2)+H_infinity=-2H_infinity,
```

so every positive logarithmic plurigenus is zero and

```text
bar-kappa(A^2)=-infinity.
```

A dominant map between irreducible surfaces is generically finite.
Therefore a dominant morphism `A^2->U`, together with (3.2) and Lemma 4.1,
would give

```text
-infinity=bar-kappa(A^2)>=bar-kappa(U)>=0,
```

a contradiction.

The classical source for the logarithmic ramification formalism is S.
Iitaka, *On Logarithmic Kodaira Dimension of Algebraic Varieties* (1977):

```text
https://doi.org/10.1017/CBO9780511569197.014
```

No citation-dependent step is left implicit here; the pullback proof above
is the full special case used.

## 5. Explicit-control replay

For the faithful residual control in the input producer,

```text
Phi=u X^3+X^2Y+XY^2+vY^3,
rho=[X^3:Y^3],
S={0,infinity},
q_0=3u lambda^2+2lambda+1,
R: q_0=0.
```

On the `lambda` chart, a concrete instance of the form above is

```text
omega = 3lambda * d(lambda) wedge du / q_0.             (5.1)
```

Indeed, over `G_m` the relative displacement from the ramification graph is
`q_0/(3lambda^2)`, and wedging its logarithmic differential with
`d(lambda)/lambda` gives (5.1).  At `lambda=0`, use `w=1/u`; the two boundary
branches are

```text
w=0,
3lambda^2+(2lambda+1)w=0,
```

with contact order two, and (5.1) becomes

```text
-3lambda * d(lambda) wedge dw
  / (w*(3lambda^2+(2lambda+1)w)).
```

This is exactly (3.1) with `m=2`.  The symmetric chart gives the same audit
at infinity.  Thus the explicit cover-side control has
`bar-kappa(U)>=0` (in fact it is the borderline two-collision case), so its
failure to supply an `A^2` first leg is forced rather than accidental.

The earlier redundant-sheet control

```text
(G_m minus {1}) x A^1 -> G_m x A^1
```

does not challenge the theorem.  Its target has logarithmic Kodaira
dimension `-infinity`, whereas the cubic residual target has a nonzero
logarithmic canonical form created by the two collision fibres.

## 6. Strong Zariski Main, Euler, classes, and units

The prior packet correctly warned that strong Zariski Main alone leaves a
loophole: boundary components of the finite normalization can map onto
curves already covered by interior sheets.  Nothing in this report asserts
that `g1` is finite or equal to its image, and no Hartogs shortcut is used.

Likewise, the following true statements are not load-bearing here:

```text
O(U)^*=C^*,
Cl(U)=0,
chi_c(U)=#S>=2,
g1(A^2)=U minus a finite set.
```

They explain why the elementary unit, class-group, and finite-cover Euler
arguments stop.  The logarithmic form retains boundary-collision data that
ordinary `Cl(U)`, units, and `chi_c(U)` do not see, and log pullback works
for a nonproper generically finite map.

## 7. Scope, review gate, and successor

There is no remaining internal mathematical gap in `BD-A2-FIRSTLEG` under
the stated two-section premise.  Promotion still requires a different-model
hostile review, with special attention to:

1. closure of `R` being a section and meeting infinity exactly over `S`;
2. the order-`m` collision blowup calculation;
3. absence of vertical poles in `qbar^*eta wedge dlog(phi)`; and
4. logarithmic-plurigenus monotonicity for a nonproper generically finite
   morphism.

After that review, the affine-linear cubic subfamily can be marked excluded:
all nonresidual rows die by `AL3-REDUCE`, and the residual row dies here.
The honest block-descent successor is no longer another redundant-boundary
lemma.  It is to remove the affine-linear coefficient hypothesis from the
cubic Miranda analysis, or to find an analogous log-positive two-section
quotient in the nonlinear cubic case.

This report proves no statement about a cubic block outside the
affine-linear reduction, no primitivity theorem, and no form of JC2 by
itself.  It used desk geometry only: no CAS, AWS computation, formalization
tree, or broad web sweep.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11262`.
- Body SHA-256: `0238ee718560116ef9672f05de7bad23d75dfefba5d302ce10bfd0f1d1127ef6`.
- Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`.
