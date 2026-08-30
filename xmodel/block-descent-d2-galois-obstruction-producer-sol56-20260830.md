# Producer: Galois block obstruction and closure of `BD-D2`

Producer: Sol 5.6 Ultra  
Date: 2026-08-30 UTC  
Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`  
Lifecycle: **EXACT DESK PRODUCER / `BD-D2` PROVED / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Verdict

Let `F=(f,g): A^2_C -> A^2_C` be a hypothetical non-invertible Keller
map, and let

```text
C(f,g) proper-subfield K proper-subfield C(x,y),
d1=[C(x,y):K] >= 2,       d2=[K:C(f,g)] >= 2
```

be a proper intermediate block field.  Use the promoted block-descent
factorization

```text
A^2 --g1--> Y=Spec(B_K) --g2--> A^2,
```

where `B_K` is the integral closure of `C[f,g]` in `K`.  The promoted
theorem supplies that `B_K subset C[x,y]`, `g1` is dominant, quasi-finite,
and everywhere etale, `g2` is finite flat, and `g1(A^2)` misses the entire
non-etale locus `R` of `g2`.

The exact conclusion of this packet is:

> **Theorem BD-GAL.**  The extension `K/C(f,g)` cannot be Galois.  In
> particular `d2 != 2`; hence a hypothetical Keller counterexample has no
> proper quadratic intermediate field over its target function field.

There are two independent proofs of the quadratic case below.  The first
comes from a general fixed-sheet theorem and proves the Galois
strengthening.  The second puts every rank-two finite-flat algebra into its
global trace-zero normal form and gives a direct principal-ramification
contradiction.  Neither proof uses polynomial parametrization of `A(F)`, a
converse about nonproperness, smoothness of `Y`, properness of `g1`, or a
minimal-topological-degree assumption.

## 1. A principal divisor cannot be wholly missed

Write `A=C[u,v]` and `S=C[x,y]`.  The inclusion `B_K subset S` is the
coordinate-ring map of `g1` and is injective.

**Lemma 1 (missed-principal-divisor obstruction).**  If `0 != b in B_K` is
a nonunit and the set `V_Y(b)` is contained in `Y minus g1(A^2)`, then a
contradiction follows.

Indeed, the image of `b` in `S` has no zero on `A^2(C)`.  By the weak
Nullstellensatz it is a unit of `S`, hence a member of `C^*`.  Injectivity
then says that `b` was the same nonzero constant in `B_K`, contrary to its
being a nonunit.

Consequences that hold for every proper block, in every degree, are:

1. no nonempty principal closed set of `Y` can be supported inside `R`;
2. no irreducible component of `R` can have principal height-one prime;
3. `B_K` is not factorial, so `Cl(Y) != 0`; and
4. the finite-flat algebra `B_K/A` cannot be monogenic.

For item 4, if `B_K=A[t]/(P(t))` with `P` monic, then
`Omega_(B_K/A)=B_K/(P'(t)) dt`.  Thus `R=V_Y(P'(t))`; it is nonempty by the
promoted theorem and is missed by `g1`, contradicting Lemma 1.  This
general nonmonogenicity statement is useful, but it does not say that every
higher-degree cover is impossible: finite locally free algebras of rank at
least three need not be globally monogenic.

## 2. Every branch component has an unramified sheet

**Theorem 2 (fixed-sheet theorem).**  Let `D=V_A(p)` be any irreducible
component of the branch/discriminant divisor of `g2`, with `p in A`
irreducible.  Then `g2^{-1}(D)` has an irreducible component dominating `D`
whose generic point is outside `R`.  Equivalently, geometric
codimension-one inertia on the `d2` sheets has at least one fixed sheet.

**Proof.**  A Keller map is etale, hence dominant and quasi-finite.  Its
pullback `A -> S`, `u |-> f`, `v |-> g`, is therefore injective.  Thus
`p(f,g)` is a nonconstant, nonunit polynomial: if it were a constant `c`,
then the nonzero polynomial `p-c` would lie in the kernel.

Choose an irreducible curve `E` in `V_S(p(f,g))`.  Its image under `F` lies
in `D`.  Quasi-finiteness forbids a curve from being contained in one fibre,
so `E` maps dominantly to `D`.  Let `T` be the closure of `g1(E)` in `Y`.
The same quasi-finiteness argument makes `T` a curve, finite and dominant
over `D`; hence it is an irreducible component of the set-theoretic inverse
image of `D`.

Every point of `g1(E)` lies outside the closed set `R`.  Therefore `T` is
not contained in `R`, and its generic point is a point where `g2` is etale.
Over the geometric generic point of `D`, this is an inertia orbit of length
one.  This proves the assertion. `square`

The closed-point-to-generic step here is load-bearing: merely finding one
special unramified point would not suffice.  The curve `E`, quasi-finiteness,
and closure `T` show that the unramified point belongs to a component that
dominates `D`, so the corresponding ramification index really is `e=1` at
the divisorial valuation.

## 3. Galois factors are impossible

Assume that `K/C(f,g)` is Galois.  For every height-one prime `(p)` of `A`,
the Galois group acts transitively on the height-one primes of `B_K` above
`(p)`, and all their ramification indices are equal.  The promoted theorem
gives a nonempty ramification divisor, so choose a component of its image
`D=V(p)`.  At least one prime above `(p)` is ramified.  Theorem 2 supplies a
prime above the same `(p)` with ramification index one.  Galois uniformity
makes these two statements incompatible.  Hence no proper block field can
be Galois over `C(f,g)`.

This proof uses branch nonemptiness already established in the promoted
block theorem.  It is not circular in properness of `g1`: that theorem gets
nonemptiness from the impossibility of a connected nontrivial finite-etale
cover of `A^2`, while `g2`—not `g1`—is the finite map.  Section 4 also gives
an entirely algebraic rank-two verification of nonemptiness.

In characteristic zero every quadratic field extension is Galois.  Thus
`d2=2` is impossible, proving `BD-D2`.

## 4. Independent rank-two normalization audit

This section proves the quadratic case directly and keeps singular `Y`
visible.

Assume `d2=2` and put `B=B_K`.  Since `B` is finite flat of rank two over
`A`, its trace satisfies `Tr(1)=2`.  The retraction `b |-> Tr(b)/2` gives

```text
B = A*1 direct-sum M,       M=ker(Tr),
```

where `M` is a projective `A`-module of rank one.  Since
`Pic(A^2_C)=0` (equivalently, every rank-one projective module over
`C[u,v]` is free), choose a generator `w` of `M`.  Relative to the basis
`1,w`, write `w^2=a+bw`.  The multiplication matrix of `w` has trace `b`,
whereas `Tr(w)=0`; hence `b=0`.  With `h=a`, multiplication gives an
isomorphism

```text
B = A[w] = A[T]/(T^2-h).
```

The fact that `B` is a domain makes `h` nonzero and nonsquare.  In
particular `h` cannot be constant: every nonzero complex constant is a
square, while `h=0` gives a nonreduced algebra.  Thus `D=V_A(h)` is a
nonempty curve without invoking properness or any topological assertion.

Normality forces `h` to be squarefree.  If an irreducible `q` satisfied
`q^2 | h`, then `w/q` would lie in `Frac(B)` and satisfy the monic equation

```text
(w/q)^2-h/q^2=0.
```

It would therefore be integral over `B`, hence in `B`.  Writing it as
`alpha+beta*w` with `alpha,beta in A` and multiplying by `q` would force
`q*alpha=0` and `q*beta=1`, impossible for a nonunit `q`.

The trace discriminant in the basis `1,w` is `4h`, and

```text
Omega_(B/A) = B/(2w) dw.
```

Consequently

```text
R = V_Y(w),
g2^{-1}(D)_red = V_Y(w) = R.
```

The hypersurface Jacobian also gives

```text
Sing(Y) = V_Y(w, partial_u h, partial_v h) subset R.
```

Squarefreeness makes this singular set finite, but it need not be empty.
Thus neither smoothness of `Y` nor smoothness of the branch curve has been
smuggled into the argument.

Now `w` is an actual element of `B subset S`.  Because `g1(A^2)` misses
`R=V_Y(w)`, its image in `S` is a nowhere-zero polynomial, hence a constant
unit.  Injectivity would make `w` that same constant element of `B`, which
contradicts `Tr(w)=0` and `Tr(c)=2c`.  This is Lemma 1 in the canonical
rank-two coordinate.

Equivalently, degree two has the special set equality above: every point
over the branch curve is ramified.  Hence a hypothetical composite `F`
would avoid `D`, so `h(f,g)` would be a unit; but injectivity of `F^*` says a
nonconstant `h` cannot pull back to a constant.  This is the same
contradiction expressed downstairs.

## 5. Why the argument is degree-two-specific

For a rank-two cover, trace splitting has rank-one kernel, `Pic(A)=0` makes
that kernel globally cyclic, and the single trace-zero coordinate cuts out
the whole ramification set.  Moreover the full reduced inverse image of the
branch divisor equals that ramification set.  These statements fail in
general rank.

For degree at least three a branch fibre can contain both a ramified point
and simple unramified points.  The model

```text
(w,v) |-> (u=w^3-3w, v)
```

is finite flat of degree three.  Its branch lines are `u=2` and `u=-2`;

```text
w^3-3w-2  = (w-2)(w+1)^2,
w^3-3w+2  = (w+2)(w-1)^2.
```

Each branch value therefore has a ramified double root and an unramified
simple root.  Codimension-one inertia is a transposition with a fixed sheet,
exactly as Theorem 2 requires.  This is a control for the local conclusion,
not a Keller sandwich: its intermediate surface is `A^2` and its algebra is
monogenic, both forbidden for a proper block by the preceding results.

Thus the downstairs shortcut "the composite avoids the discriminant" is
valid in degree two and false in higher degree.  What survives in all
degrees is only the fixed-sheet condition.  Higher non-Galois block
quotients remain open.

## 6. Complement monodromy and log/topological bookkeeping

In the quadratic normal form, set

```text
V=A^2 minus D,       U=Y minus R.
```

Then `U -> V` is the connected etale double cover `w^2=h`, represented by
the sign character of `pi_1(V)` that is nontrivial on a meridian of each
squarefree branch component.  If the hypothetical `g1` existed, the
composite would map `A^2` into `V` and `w o g1` would be a global lift.
Simple connectivity of `A^2(C)` makes such a topological lift unsurprising;
it is not itself a contradiction.  The contradiction is algebraic and
logarithmic: the lift is an invertible regular function on `A^2`, whose unit
group is only `C^*`, while

```text
2 div(w o g1) = div(h(f,g)) = F^*D.
```

Dominance makes the right-hand principal divisor nonzero, whereas avoidance
would make it zero.  No Euler-characteristic, log-Chern, or link-at-infinity
estimate is needed, and none is silently assumed.

A boundary control shows why topology alone is too weak.  Let
`Y=Spec C[u,v,w]/(w^2-uv)`, a normal quadric cone singular at the origin,
and let `U=Y minus V(w)`.  For `m>=2`, the connected cover

```text
X_m=Spec(O(U)[s]/(s^m-w)) -> U -> Y
```

is etale of generic degree `m`, quasi-finite and nonproper as a map to `Y`,
misses all ramification of the degree-two map `Y -> A^2_(u,v)`, and its
composite is etale and avoids `V(uv)`.  It is consistent because `X_m` is
not `A^2` and has nonconstant units.  This control retains a singular
non-`A^2` intermediate surface, so the failure is precisely the source
unit/log-boundary input rather than a hidden smoothness assumption.

If avoidance is dropped, the elementary map `(w,v) |-> (w^2,v)` meets its
ramification line and has nonconstant Jacobian.  This confirms that the
Keller-derived avoidance of `R` is also load-bearing.

## 7. Exact monodromy disposition

Let `E/C(f,g)` be a Galois closure, `G=Gal(E/C(f,g))`,
`H=Gal(E/C(x,y))`, and `J=Gal(E/K)`.  Then

```text
H subset J subset G,
d1=[J:H]  (size of each block),
d2=[G:J]  (number of blocks).
```

The theorem proves:

1. `J` cannot be normal in `G` for a proper block field `K`, because that is
   exactly the condition that `K/C(f,g)` be Galois;
2. in particular `[G:J]=2` is impossible, since an index-two subgroup is
   normal; and
3. every divisorial inertia permutation on the `d2` blocks has at least one
   fixed block.

It does **not** exclude `[J:H]=2` (blocks containing two source sheets), an
even topological degree, every quotient of prime degree, or all imprimitive
monodromy.  For example, the wreath-product action `C2 wr S3` on three
blocks of size two has `d1=2`, `d2=3`; a transposition in the `S3` quotient
fixes one block and is compatible with the fixed-block condition.  This is
a permutation control only, not an asserted Keller realization.

Therefore the precise promoted consequence should be "no two-block system
and no proper Galois block quotient," not "monodromy is primitive" and not
"two-element blocks are impossible."

## 8. Next discriminator and nonclaims

`BD-D2` is closed on the prove side.  The cheapest exact successor is not a
blind degree-three repetition; Theorem 2 already says what survives there.
The next discriminator is:

> **BD-FIX3.**  For `d2=3`, every branch inertia is a transposition (cycle
> type `(2)(1)`), so the cubic quotient is necessarily non-Galois and its
> normalization is necessarily nonmonogenic and nonfactorial.  Determine
> whether those three constraints, together with the etale `A^2` first leg,
> force a contradiction; otherwise construct a normal finite-flat cubic
> control satisfying them.

This packet does not prove JC2, primitivity, nonexistence of `d1=2` blocks,
or exclusion of any non-Galois `d2>=3` block.  It does not identify all of
`A(F)`, use polynomial parametrization of its components, or infer an
attained polynomial map from formal/boundary data.  It used desk algebra
only: no web search, local CAS, AWS job, or formalization tree was used.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13338`.
- Body SHA-256:
  `f03368f61177ea1cd1819832184d6df559412e3afdc20d30cef5aeb43f3d2bf8`.
- Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`.
