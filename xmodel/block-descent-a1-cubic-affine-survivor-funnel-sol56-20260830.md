# Proper-cubic affine survivor: pseudo-plane funnel and companion section

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`cubic_affine_survivor` lane)  
Frozen basis: `1d35fe69987a4e346c7e97ab2a227ccce49ef60d`  
Lifecycle: **EXACT PROVISIONAL THEOREM / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Verdict

Charge the promoted proper-cubic survivor

```text
A2 --g1, etale quasi-finite dominant of degree d1>=2--> U
   --pi=g2|U, etale quasi-finite surjective of degree 3--> A2,

rho:U->A1 an A1-fibration,
b0(B)=1, S0=empty, Q=0.
```

Here `B=g2(R)_red`, `R=NonEt_Y(g2)_red`, and `U=Y minus R`.  Then:

1. `rho` has at most one multiple fibre.
2. It cannot have none.  Hence it has a unique fibre `mF`, with `m>=2`,
   and

   ```text
   Pic(U)=Z/mZ<[F]>,       U is a Q-homology plane,
   U minus g1(A2) is finite,       m divides d1,       K_U~0.       (0.1)
   ```

3. The rank-three companion over the branch globalizes scheme-theoretically:

   ```text
   T:=U times_(A2) B  --> B
   ```

   is an isomorphism.  Thus `B` occurs as a principal reduced Cartier curve
   in the smooth surface `U`, component by component.
4. Put `W=U minus T`.  Then

   ```text
   W -> A2 minus B
   ```

   is a connected finite etale cover of degree three with monodromy `S3`.
   At every affine point of `B`, including its singular points, the local
   monodromy fixes the companion sheet and lies in one conjugate of `S2`.
5. `B` cannot be smooth.  Consequently every actual survivor has a singular
   or reducible connected contractible one-place branch curve whose complement
   has an `S3` quotient, while every affine local branch group preserves a
   companion sheet.  The unresolved monodromy must therefore be supplied by
   global braid/infinity topology, not by an affine triple-fibre point.

This is a strict reduction, not cubic-block nonexistence and not JC2.  The
tempting Hartogs shortcut from the finiteness of `U minus g1(A2)` is false:
boundary divisors of the Zariski-Main finite normalization can map onto target
divisors already reached by other source sheets.

## 1. Frozen inputs and primary sources

Binding campaign inputs:

```text
8ccb92fd3676e9f8b58e3ace4eb9157d0fa290ea24abc84d9913e94ec407e16d
  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-coordinator-integration-sol56-20260830.md

7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md

f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
```

They supply the sandwich, smooth rational affine `U`, constant units, the
actual morphic first leg, the `A1`-ruling, the cubic fibre census, the
one-place component/forest theorem, and the exact survivor equalities.

Primary surface source:

```text
Masayoshi Miyanishi,
Lectures on Geometry and Topology of Polynomials --
Surrounding the Jacobian Conjecture,
arXiv:1504.07179, especially Lemmas 1.4.3, 1.4.16, 2.5.2 and
Theorem 2.5.10.

downloaded PDF: 806236 bytes
SHA-256: ab4eb0cb74e4051e3fb1f702a253d29cb1a658632f11bc6f4b04a8bb9e7daaa4
```

Primary degree-three source:

```text
S. Yu. Orevkov, On three-sheeted polynomial mappings of C2,
Theorem 1.1.

f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db
  refs/jc86.pdf
```

The statements below use the general Picard and multiple-fibre lemmas from
Miyanishi.  They do **not** assume that an arbitrary affine pseudo-plane has
the special typed boundary graph `(d,n,r)`.

## 2. There is at most one multiple fibre

The composite

```text
h=rho o g1:A2->A1
```

is a nonconstant polynomial.  Choose a general affine line `L subset A2` on
which `h` is nonconstant.  Then `g1|L:A1->U` is a nonconstant curve transverse
to `rho`.

Miyanishi Lemma 1.4.16 says that an `A1`-fibration over `A1` with at least
two multiple fibres admits no such transverse morphism from `A1`.  Its proof
is the exact polynomial-power obstruction: over two multiple values one gets

```text
p(s)^a-q(s)^b=constant,       a,b>=2,
```

and factorization/Mason--Stothers (equivalently the positive-genus
superelliptic curve after removing the common gcd) makes both polynomials
constant.  Therefore `rho` has at most one multiple fibre.

The use of a general source line is essential.  No assertion that `g1`
preserves the ruling, is finite, or maps a generic source fibre to a ruling
fibre is made.

## 3. The no-multiple row is impossible

If there is no multiple fibre, every scheme fibre is a smooth `A1`.  The
equidimensional morphism from the smooth surface to the smooth curve is flat,
hence smooth.  It is an `A1`-bundle.  Over `A1`, its line-bundle and additive
torsor classes vanish (`Pic(A1)=H^1(A1,O)=0`), so

```text
U isomorphic to A2.                                           (3.1)
```

Under (3.1), `pi:U->A2` becomes a polynomial Keller self-map of geometric
degree three.  Orevkov Theorem 1.1 excludes polynomial maps of `C2` with
nonzero constant Jacobian and geometric degree two or three.  Hence the
no-multiple row is empty.

This is the only place where Orevkov is consumed.  It is not applied directly
to a pseudo-plane.

## 4. Exact unique-multiple-fibre package

Write the unique multiple fibre as `mF`, `m>=2`.  Since every reduced ruling
fibre is one `A1`, Miyanishi Lemma 1.4.3 gives

```text
Pic(U)=Z/mZ<[F]>,                                      (4.1)
H_i(U;Q)=0 for every i>0.
```

### 4.1 Missed divisors and the cofinite image

Let `V=g1(A2)`, an open subset of `U`.  The free group on the prime divisors
contained in `U minus V` injects into `Pic(U)`.  Indeed, if a rational
function `b` has divisor supported there, then `b` and `b^-1` are regular on
the normal open `V`.  Their pullbacks are mutually inverse polynomials on
`A2`, hence scalars.  Dominance makes `b` the same scalar, so its divisor was
zero.  This proves linear independence of all missed prime divisors.

The finite group (4.1) contains no nonzero free subgroup.  Thus `U minus V`
has no curve component.  It is a finite set:

```text
g1:A2->U is an affine pseudo-covering.                         (4.2)
```

### 4.2 The multiple-fibre order divides the first-leg degree

Choose the ruling coordinate `t` so that `div_U(t)=mF`, and put
`L=C(x,y)`, `K=C(U)`.  Etaleness makes `g1^*F` a reduced divisor.  Since
`C[x,y]` is factorial,

```text
g1^*t=c P^m,       c in C*, P in C[x,y] nonconstant.          (4.3)
```

The binomial `X^m-t/c` is irreducible over `K`.  For if `t/c=s^p` in `K`
for a prime `p|m`, normality first gives `s in O(U)` and then

```text
div_U(s)=(m/p)F,
```

contradicting the exact order `m` of `[F]` in (4.1).  Since `C` contains all
roots of unity, the standard Kummer binomial criterion has no further
exception.  Equation (4.3) therefore embeds a degree-`m` field

```text
K(P) subset L.
```

The tower law gives

```text
m divides [L:K]=d1.                                        (4.4)
```

Finally, etaleness of the second leg gives the exact canonical condition

```text
K_U=pi^*K_A2~0.                                             (4.5)
```

### 4.3 Typed theorem: useful but not a coverage theorem

For a pseudo-plane already known to have Miyanishi's special boundary type
`(d,n,r)`, Theorem 2.5.10 computes `K_U~(r-2)F` and excludes an etale map to
`A2` unless the exceptional `r=2` row occurs.  Nothing charged here proves
that an arbitrary `U` satisfying (4.1)--(4.5) belongs to that typed class.
The source explicitly introduces the typed boundary graph as an additional
condition.  Therefore one may record

```text
typed client => exceptional r=2,
arbitrary survivor => type coverage OPEN,
```

but not replace the second line by the first.

## 5. Why the Zariski-Main/Hartogs shortcut fails

Strong Zariski Main factors `g1` as

```text
A2 open--> Xbar finite--> U,
```

with `Xbar` the normalization of `U` in `L`.  Equation (4.2) does **not**
make `Xbar minus A2` finite.  A boundary divisor can dominate a divisor of
`U` which is simultaneously attained by another open source sheet.

Miyanishi Lemma 2.5.2 is an exact countercontrol.  For any such unique-
multiple-fibre Q-homology plane, the cyclic degree-`m` cover `Utilde->U`
has `m` affine-line components over `F`.  Deleting `m-1` of them leaves an
open `A2` which still maps surjectively and etale to `U`; the deleted
divisors all map onto the already attained `F`.  Thus Hartogs cannot identify
`Xbar` with `A2`, and no finite-etale conclusion follows from (4.2).

This countercontrol is exactly aligned with (4.3)--(4.4), not an unrelated
pathology.

## 6. The rank-three companion is an actual section over `B`

For every geometric `z in B`, finite flat rank three and `S0=empty` give the
unique fibre partition

```text
one non-etale point of local length 2
+ one etale companion point of local length 1.               (6.1)
```

Define the scheme-theoretic base change

```text
T=U times_(A2) B.
```

Because `pi` is etale on `U`, `T->B` is etale.  By (6.1), every geometric
fibre consists of exactly one reduced point.  Hence the map is surjective
and radicial; a surjective radicial etale morphism is an isomorphism:

```text
T isomorphic to B.                                           (6.2)
```

Equivalently, over the henselian or completed local ring at every point of
`B`, the rank-three algebra splits canonically as

```text
rank 1 trivial companion factor  times  rank 2 ramified factor. (6.3)
```

For each irreducible equation `b_i` of `B`, etale pullback gives

```text
div_U(pi^*b_i)=T_i
```

with coefficient one.  Thus every companion component is principal.  This
does not identify it with a ruling fibre or with an original source sheet.

Now

```text
W=U minus T=g2^(-1)(A2 minus B)
```

is a nonempty irreducible open of the integral finite cover `Y`, so

```text
W->A2 minus B
```

is connected, finite etale, and degree three.  Its monodromy is transitive.
It contains a transposition by (6.1), hence its image is `S3`, not the cyclic
transitive subgroup `A3`.

At any affine point `z in B`, (6.3) says more than generic inertia: the image
of the entire local complement group in `S3` lies in one order-two subgroup
fixing the local companion sheet.  Distinct local companion labels may still
be conjugated by global loops.  That last possibility is the live escape.

## 7. Smooth branch is impossible

If `B` were smooth, connectedness would make it irreducible.  Chau's
one-place theorem gives `B isomorphic to A1`; the Abhyankar--Moh theorem then
rectifies its embedding in `A2` to a coordinate line.  Therefore

```text
A2 minus B isomorphic to Gm times A1,
pi1(A2 minus B)=Z.
```

A connected degree-three cover of this complement has cyclic transitive
monodromy generated by a 3-cycle.  But (6.1) makes a meridian act as a
transposition, which is not transitive on three letters.  Contradiction.

The desk replay enumerates this last `S3` statement:

```text
aa198a357ce3c7dd3df6c97019f76553f27c76e5f4b7928ed3e52104de3f3915
  ops/block_descent_a1_cubic_affine_survivor_replay.py

ordinary / -O / -OO payload SHA-256:
a602c5ca9ca141166143b504b32d835b064ea06b4f5d3618876d1b26faefd834

AST Assert nodes: 0
deliberate (2,1)->(3) mutation: rejected in ordinary mode.
```

Thus

```text
B is singular or reducible.                                  (7.1)
```

By (6.2), component normalizations `A1`, and the promoted affine incidence
forest, the connected analytic curve `B` is contractible: unibranch
singularities do not change its component topology, and multibranch gluing
has a tree incidence graph.  Contractibility does not make its complement
group cyclic; cuspidal curves are the warning control.

## 8. Maximum-safe theorem and cheapest unresolved gate

> **Cubic affine-survivor funnel.**  Every actual proper cubic block in the
> promoted affine-base equality row has exactly one multiple ruling fibre
> `mF`, with `m|d1`, `Pic(U)=Z/m`, `K_U~0`, and cofinite first-leg image.
> Its cubic companion locus is scheme-isomorphic to the connected branch.
> The branch is a singular or reducible contractible one-place plane curve,
> and its complement has an `S3` quotient whose restriction to every affine
> local branch group fixes a companion sheet.

The cheapest remaining gate is now one precise topology problem:

```text
Can a connected contractible one-place plane curve with forest incidence
support an S3 quotient of its complement such that every affine local group
lands in a companion-fixing S2, while the associated normal cubic filling
has partition (2,1) at every branch point?
```

A negative answer closes the cubic affine survivor.  A positive topological
passport is only a control; it must still realize the normal finite-flat
cubic algebra, the pseudo-plane `K_U=0` package, and the etale `A2` first leg.

The first exact successor should do both sides concurrently:

1. run van Kampen/splice presentations for singular and reducible one-place
   forest curves, retaining the local companion subgroup at every affine
   singularity and the sole infinity group;
2. seek an explicit `S3` counterrepresentation before asserting common-label
   propagation;
3. in parallel, determine whether the proper-block boundary forces the
   ramification resolution arms to be linear.  Under that additional linear
   condition, Orevkov's local knot argument makes `B` smooth and Section 7
   closes the row.

No statement here excludes rank at least four, the primitive/no-block horn,
an arbitrary pseudo-plane, or any singular/reducible `B` before this final
gate is discharged.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13589`.
- Body SHA-256:
  `f2ca4b74ea0e3478603fbb1ed9012bf8bdd39b2b08106e75b7d1497046de59f9`.
- Frozen basis: `1d35fe69987a4e346c7e97ab2a227ccce49ef60d`.
