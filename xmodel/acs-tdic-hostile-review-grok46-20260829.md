# Hostile mathematical review: ACS / deficit-Euler / TDIC

Date: 2026-08-29
Reviewer: Grok 4.6, different-model expert referee
Charge: `ACS`, deficit-Euler `(★)`, `ACS-2`, and `TDIC` only, from the
Opus 5 ideation report.  No other `20260829T0002Z` submission was opened,
listed, or searched.  No AWS, web, CAS, canonical-ledger edit, repository-wide
inventory, commit, push, delegation, or `jc2-lean` access.

## Verdict table

| Claim | Verdict |
|---|---|
| `ACS-1`: `F: C^2 \ F^{-1}(A) -> C^2 \ A` is a connected finite étale cover of degree `td` | **CONFIRMED** |
| `ACS-1(i)`: `e(C^2 \ F^{-1}A) = td · e(C^2 \ A)` | **CONFIRMED** |
| `ACS-1(ii)`: `κ-bar` equality under the covering | **CONFIRMED** (standard; computes nothing for any genome) |
| `ACS-1(iii)`: `F^{-1}(A) -> A` étale, singularities are copies, "multiplicity `d-δ(p)`" | **REPAIR** |
| Deficit-Euler identity `(★)` as written | **REPAIR** |
| `(★)` as a termwise-positive decomposition of `td-1` | **REFUTED** |
| `ACS-2`: `A(F)` empty or smooth and irreducible `=>` automorphism | **REPAIR** (theorem true; proof incomplete) |
| `TDIC` per irreducible component, unmarked meridian class | **CONFIRMED** |
| `TDIC` marked inertia type, including `e=1` ends vs affine 1-cycles | **REPAIR** (true, but not by conjugacy in `S_td`) |
| `TDIC-SET` as a global set-equality theorem | **REPAIR** |
| Banked residue-A `TDIC-SET` test | **`NOT-TYPED`** |

Headline: the covering lemma is correct for Keller maps and is the only
load-bearing new setup.  The Euler identity is true after compactly-supported
additivity and a refined stratification, but `e(C)` can be negative and `(★)`
does not decompose `td-1` into nonnegative summands.  `ACS-2` is true by a
shorter argument than the one given.  Per-component meridian conjugacy is
standard; the proposed residue-A set test is not computable from banked data.

This review licenses no originality claim, no literature attribution, no
avenue raise, no cofinal ceiling, no residue-A kill, and no repair of van
Dobben §5.4.

---

## 0. Custody

Charged report, SHA-256 verified on this host before reading:

```text
542f6212a10f46c843ff886e7241155dc43963806e23738846082f3902fd8ac9  xmodel/ideation-20260829T0002Z-opus5.md
```

Cited local files read in full; SHA-256 recomputed on this host after reading:

```text
459bfe8e3e8e57cf554c019d8051475e74d1e8f44e23991f87ae4cbe26030a2e  ladder/SHEET6-CLASSICAL.md
0f201502716ca9c9bf33718412739e0254981c2eb7204657dc78ee7fbcd653c1  xmodel/g2-finite-end-asymptotic-monodromy-connection-sol-ultra-20260827.md
82a67d207b404676a1ab35d02428a50cf436f3a644f1dcafdefe17ecfb76bbc8  xmodel/vandobben2608-projective-bundle-jc2-boundary-infinity-review-codex-20260828.md
```

Scope fence: D43, Card C, `K0`, Rail E, landing, `RPMC`, `G2-PSC`, `G2-BD`,
and every avenue-ranking sentence are out of charge.

Notation.  `F=(f,g): C^2 -> C^2` is a polynomial map, `J(f,g)=1` unless a
countermodel drops it, `d = td(F)` is the geometric degree (generic affine
fibre cardinality), `A = A(F)` is Jelonek's nonproperness set, and
`δ(y) = d - #F^{-1}(y)` is the affine-fibre deficit.  Euler numbers written
`e_c` are compactly supported; on a smooth complex manifold they coincide
with ordinary `e`.

---

## 1. `ACS-1`: the covering, properties separated

### 1.1 Corrected statement

**Theorem ACS-1.** Let `F: C^2 -> C^2` be a polynomial map with `J(F) ∈ C*`.
Let `A = A(F)` and `d = td(F)`.  Then

```text
F :  C^2 \ F^{-1}(A)  -->  C^2 \ A
```

is a connected finite étale morphism of degree `d`, hence a connected
degree-`d` topological covering space.  Equivalently, after basepoints it
corresponds to an index-`d` subgroup of `π_1(C^2 \ A)`.

Keller is essential.  Generic finiteness is not an extra hypothesis: `J=1`
already implies étale, hence dominant, hence generically finite.

### 1.2 Proof, property by property

**Étale.** `J(F)` is a nonzero constant, so `dF` is invertible at every point
of `C^2`.  Over `C` this is equivalent to `F` being a local biholomorphism.
Étale morphisms are stable under restriction of source and target, so the
displayed restriction is étale.

**Quasi-finite.** An étale morphism of finite type is quasi-finite: every
fibre is a finite discrete scheme.  This holds on all of `C^2`, not merely
off `A`.  In particular every fibre of a Keller map is 0-dimensional, so
positive-dimensional fibres cannot occur.

**Proper over the complement of `A`.** By Jelonek's definition, `A(F)` is
exactly the locus of target points at which `F` fails to be proper, it is
closed, and for a dominant polynomial map `C^2 -> C^2` it is empty or a
curve.  Thus `F: F^{-1}(C^2 \ A) -> C^2 \ A` is a proper morphism of
varieties.  The source identity `F^{-1}(C^2 \ A) = C^2 \ F^{-1}(A)` is
set-theoretic and scheme-theoretic.

**Finite.** A morphism is finite if and only if it is proper and
quasi-finite.  Both have been established on `C^2 \ A`.  (Zariski's main
theorem is the same statement in the separated finite-type setting: a
quasi-finite morphism factors as an open immersion into a finite morphism,
and properness kills the open-immersion factor.)

**Surjective.** A finite morphism is closed.  An étale morphism is open.
The target `C^2 \ A` is connected in the Zariski topology (complement of a
proper closed subset of a normal variety of dimension 2) and in the classical
topology (complement of a complex curve in `C^2`).  A nonempty open-and-closed
subset is the whole target, so the finite étale map is surjective.  The
unrestricted map `F: C^2 -> C^2` need not be surjective: points of `A` may
fail to be attained.  That does not affect surjectivity off `A`.

**Degree `d`.** A finite étale morphism onto a connected scheme has constant
fibre cardinality, equal to the rank of the structure sheaf.  The set
`C^2 \ A` is Zariski-open dense, so it contains generic points of `C^2`,
where the fibre cardinality is the geometric degree `d` by definition.  Hence
the covering degree is `d` at every point of `C^2 \ A`.

Equivalently, for a Keller map Jelonek's properness criterion identifies
`A(F)` with the closed set `{ y : #F^{-1}(y) < d }`.  Off `A` one therefore
has `#F^{-1}(y) = d` identically, which is the same constancy.

**Connectedness of the source.** `A` is empty or a curve.  The scheme-theoretic
preimage `F^{-1}(A)` is étale over `A`, hence pure of dimension 1 if nonempty,
so it is a curve or empty.  It cannot be all of `C^2`: `A` is not open.  The
complement of a curve (or of the empty set) in `C^2` is connected classically
and Zariski.  A connected finite étale cover of a connected space is a
connected covering space.

If `A` is nonempty, `F^{-1}(A)` is nonempty as well.  Otherwise `F: C^2 ->
C^2 \ A` would be a degree-`d` covering, so `π_1(C^2) = 1` would inject as an
index-`d` subgroup of `π_1(C^2 \ A)`.  For a nonempty reduced curve the group
`H_1(C^2 \ A; Z)` is free of rank equal to the number of irreducible
components, so the complement is not simply connected and admits no finite
cover by `C^2`.  Thus `F^{-1}(A)` is a nonempty curve whenever `A` is.

**Topological covering.** Over `C`, a finite étale morphism of finite-type
varieties is a finite-sheeted covering map in the classical topology.  This
is the comparison theorem, or equivalently: finite étale implies local
biholomorphism with compact (finite) fibres, hence a covering space.

**Empty-set sanity.** If `A = ∅`, the theorem says `F: C^2 -> C^2` is a
connected finite étale cover of degree `d`.  Simple connectedness of `C^2`
forces `d = 1`, so `F` is an automorphism.  This is the standard proper-Keller
inversion, recovered as the empty case of `ACS-1`.

### 1.3 Immediate consequences, audited

**(i) Euler multiplicativity.** Both `C^2 \ F^{-1}(A)` and `C^2 \ A` are
smooth complex 4-manifolds.  For a finite covering of degree `d` one has
`e(X) = d · e(Y)`, and on a smooth complex manifold ordinary `e` equals
`e_c`.  Confirmed.

**(ii) Log Kodaira dimension.** If `U' -> U` is finite étale between smooth
varieties, a log smooth compactification may be chosen so that
`K_{X'}+D' = φ^*(K_X+D)`.  Iitaka dimensions therefore agree:
`κ-bar(C^2 \ F^{-1}A) = κ-bar(C^2 \ A)`.  Confirmed as a standard invariance.
It does not compute either number for any campaign genome, and it does not
touch the `SHEET6-CLASSICAL` §3b `NEEDS-DATA` on unpinned `B`/`x` tails of an
Orevkov log surface.  Those are different objects.

**(iii) Singularities of `F^{-1}(A)`.** Base change preserves étaleness, so
`F^{-1}(A) -> A` is étale as a morphism of (possibly singular) schemes.  Over
`C`, étale is a local analytic isomorphism, so every germ of `F^{-1}(A)` is
isomorphic to the germ of `A` at its image.  That much is true.

What is false or sloppy in the charged writeup:

- The map `F^{-1}(A) -> A` is **not finite** and **not a covering**.  Points
  escape to infinity along `A`; that is the deficit.  It is étale quasi-finite
  onto its image.
- It need not be surjective.  Points of `A`, including singular points, may
  have empty fibre.  Singularities of `F^{-1}(A)` are copies of singularities
  of `A` that are attained; the converse can fail on a finite set.
- "`d-δ(p)` copies" is the correct count of germs over an attained point `p`.
  Calling this a "multiplicity" collides with the multiplicity of a plane
  curve singularity and should be dropped.
- "Self-similar pair of plane-curve complements" is rhetoric, not a theorem.
  The two complements are related by a finite étale cover; the two curves
  are related by a non-proper local analytic isomorphism onto a dense open.

### 1.4 What the charged three-line argument skipped, and why it survives

The charged proof says: étale everywhere, proper off `A`, proper +
quasi-finite is finite, finite + étale is a covering, plane-curve complements
are connected.  That is the right skeleton.  The missing justifications are:
étale implies quasi-finite on all of `C^2`; connectedness of `C^2 \ A` in the
classical topology; constancy of degree from connectedness of the target
plus density; and nonemptiness of `F^{-1}(A)` when `A` is nonempty, by
`π_1`.  None of these is a gap in the statement.

---

## 2. `(★)`: stratification, covering of strata, Euler identity

### 2.1 The charged identity

With `A° = {A smooth and δ locally constant}` and `S = A \ A°` finite, the
report asserts that `F^{-1}(A) -> A` covers each component `C` of `A°` to
degree `d-δ_C`, and

```text
sum_C  δ_C · e(C)  +  sum_{p in S} δ(p)  =  td - 1.          (★)
```

Derivation claimed: `e(F^{-1}A) = sum_C (d-δ_C)e(C) + sum_p (d-δ(p))`,
`e(F^{-1}A) = 1 - d(1-e(A))`, and `e(A) = sum_C e(C) + #S`.

### 2.2 Does constant fibre cardinality make a quasi-finite étale curve map finite étale?

Not of the closure, and not in the Zariski topology.  Yes of the stratum, in
the classical topology, after the standard Hausdorff argument.

**Countermodels showing the missing hypotheses.**

- Open immersion `C* ↪ A^1`.  Étale, quasi-finite, fibre cardinality 1 on
  `C*` and 0 at the origin.  Not a covering of `A^1`.  The jump locus must
  be excluded.
- `z ↦ z^n: C* -> C*`.  Étale, finite, constant cardinality `n`.  A covering.
  This is the good case.
- Normalization of a node, `A^1 ->` nodal cubic.  Bijective on the smooth
  locus, not étale at the two points over the node.  Singular points belong
  in `S`.
- `exp: C -> C*`.  Local biholomorphism, not algebraic, infinite fibres.
  Finite cardinality is essential.
- `F(x,y)=(x,xy)`, restricted to `{x=0} -> {x=0}`.  Not étale; the map is
  constant.  Keller is essential for the stratum map to be a local
  isomorphism.

**Positive lemma, used below.** Let `C` be a smooth connected locally closed
curve in `C^2`, and let `φ: X -> C` be a morphism of finite-type `C`-varieties
which is étale with every fibre of cardinality `n ≥ 1`.  Then `φ` is a finite
étale covering of degree `n`, and in the classical topology it is an
`n`-sheeted covering map.

Proof.  Over `C`, étale is a local biholomorphism, so `X` is a smooth curve
and `φ` is a local homeomorphism of Hausdorff 2-manifolds.  Let `y ∈ C` have
preimages `x_1,...,x_n`.  Choose disjoint slice neighbourhoods `U_i ∋ x_i`
mapped homeomorphically onto neighbourhoods of `y`, and shrink to a common
target `V`.  Over any `v ∈ V` the `n` slices already supply `n` preimages;
constant cardinality forbids extra sheets.  Thus `V` is evenly covered, and
`φ` is a topological covering of degree `n`.  A finite-sheeted covering map
is proper in the classical topology.  A morphism of finite-type `C`-varieties
that is proper classically is proper algebraically, hence finite.  Finite +
étale gives the algebraic statement.

If `n=0`, the empty map to a nonempty `C` is **not** a covering.  The Euler
count below still holds numerically because both sides are zero.

Algebraic route to the same lemma: Zariski's main theorem factors a separated
quasi-finite morphism as an open immersion into a finite morphism.  Étale +
constant positive degree + surjectivity onto a connected curve force the open
immersion to be an isomorphism, by comparing ranks.

**The charged report skipped this lemma.**  The conclusion for strata with
`n ≥ 1` stands.

### 2.3 Corrected stratification

Let `S ⊂ A` be the finite set of points at which at least one of the
following holds:

1. `A` is not smooth (including every intersection of distinct irreducible
   components, and every singular point of a component);
2. the constructible function `δ` is not locally constant.

Each of these loci is finite: the singular locus of a curve is finite, and a
constructible integer function on a curve is constant on a Zariski-open of
each component.  Let `{C_i}` be the connected components of `A \ S`.  Each
`C_i` is a smooth connected locally closed curve, `δ|C_i ≡ δ_i`, and by
Jelonek J-1 each irreducible component of `A` is rational with one place at
infinity, so each `C_i` is isomorphic to `A^1` minus finitely many points.

On `C_i` one has `n_i = d - δ_i`.  If `n_i ≥ 1`, §2.2 supplies a finite étale
covering `F^{-1}(C_i) -> C_i` of degree `n_i`.  If `n_i = 0`, the preimage is
empty.  Over `p ∈ S` there are exactly `n(p) = d - δ(p)` points of
`F^{-1}(A)`, each a 0-stratum.

Semicontinuity: because `F` is a local biholomorphism, affine preimages cannot
collide.  They can only escape to infinity.  Thus `#F^{-1}` is lower
semicontinuous along `A` in the classical topology, `δ` is upper
semicontinuous, and `δ(p) ≥ δ_i` for every `p` in the closure of `C_i`.
Also `1 ≤ δ_i ≤ d` on any component of `A` that actually lies in `A(F)`
(Jelonek: points of `A` are exactly the deficit points, for Keller maps).
The value `δ_i = d` (entirely missed component) is allowed; `δ_i = 0` is not,
on a component of `A`.

### 2.4 Which Euler number, and the identity

Ordinary `e` is not additive for noncompact singular spaces.  Compactly
supported `e_c` is additive for a closed-open decomposition: if `Z ⊂ X` is
closed, `e_c(X) = e_c(Z) + e_c(X \ Z)`.

`C^2` is contractible of real dimension 4, so `e_c(C^2) = 1`.  For any closed
algebraic `Z ⊂ C^2`,

```text
e_c(C^2 \ Z) = 1 - e_c(Z).
```

If `Z` is a curve, `C^2 \ Z` is a smooth 4-manifold, so `e = e_c` there.  The
charged formula `e(C^2 \ Z) = 1 - e(Z)` is therefore legitimate if and only
if `e(Z)` means `e_c(Z)`.  For a possibly singular curve that is the honest
convention; it is not the homotopy-type Euler number of a singular space
unless the two happen to coincide.

On a smooth complex curve, Poincaré duality identifies `e` with `e_c`.  Each
stratum `C_i` is smooth, and points have `e_c = 1`.  Thus

```text
e_c(A) = sum_i e_c(C_i) + #S,
e_c(F^{-1}(A)) = sum_i n_i e_c(C_i) + sum_{p in S} n(p),
```

where the second line uses covering multiplicativity on each `C_i` with
`n_i ≥ 1`, and `0 = 0` when `n_i = 0`.

From `ACS-1(i)` and additivity on the complements,

```text
1 - e_c(F^{-1}A) = d ( 1 - e_c(A) ),
```

hence `e_c(F^{-1}A) = d e_c(A) - (d-1)`.  Substitute the two stratum
expansions and rearrange.  Every term with a factor of `d` cancels, and one
obtains

```text
sum_i δ_i e_c(C_i)  +  sum_{p in S} δ(p)  =  d - 1.           (★_c)
```

This is the charged identity, with `e` interpreted as `e_c` and with `S`
explicitly containing singularities, component intersections, and δ-jumps.
The three-line algebra is correct under that reading.

### 2.5 `e(C)` can be negative; the sum is not a positive decomposition

Each `C_i ≅ A^1 \ {k_i points}`, so `e_c(C_i) = 1 - k_i`.  This is

- `1` if the component is a closed embedded `A^1` with no special points,
- `0` if one special point is removed (`C*`),
- negative as soon as `k_i ≥ 2`.

The last case is the typical one for a component that meets two other
components, or that has two nodes, or one intersection and one δ-jump.  By
`ACS-2` a counterexample has `A` reducible or singular, so special points
are expected.

The terms `δ_i e_c(C_i)` are therefore of mixed sign.  The special-point terms
`δ(p)` are positive, but at an intersection `p ∈ A_j ∩ A_k` the rewritten
excess `δ(p) - δ_j - δ_k` need not be nonnegative.  There is no termwise
positive decomposition of `d-1`.

A schematic numerical example, not asserted to arise from a Keller map:
three lines in general position, each `C_i ≅ A^1 \ {2 pts}`, `e_c = -1`,
generic `δ_i = 1`, three nodes with `δ(p) = 2`.  Left-hand side
`-1-1-1+2+2+2 = 3`, so `d = 4`.  The negative stratum terms are essential.

Upper semicontinuity `δ(p) ≥ δ_i` does not restore positivity of `(★_c)`.

### 2.6 Automorphism and non-Keller controls

- Automorphism: `A=∅`, `d=1`, both sides of `(★_c)` are `0`.  Passes.
- `F(x,y)=(x,xy)`: `J=x`, not étale along `{x=0}`.  Geometric degree 1,
  `A={x=0} ≅ A^1`.  Generic points `(0,b)`, `b≠0`, have empty fibre so
  `δ=1`; `(0,0)` has a positive-dimensional fibre.  The stratum map
  `F^{-1}(A) -> A` is constant onto the origin, not étale.  Naive
  substitution `δ e(A^1) = 1` against `d-1 = 0` fails.  The identity does
  not fire off-hypothesis.  That control is correctly described in the
  charged report; it tests `(★)`, not `ACS-2` (see §3.6).

### 2.7 Corrected theorem

**Theorem (deficit-Euler).** Let `F` be Keller of geometric degree `d`, with
nonproperness set `A`.  Let `S` and `{C_i}` be the stratification of §2.3,
and write `δ_i` for the constant value of `δ` on `C_i`.  Then `(★_c)` holds
with compactly supported Euler characteristic.  It is an identity in the
constructible function `δ` on `A`, equivalently `⟨e_c, δ⟩_A = d-1`.  It is
not a sum of nonnegative terms, and it is not a bound on `d`.

---

## 3. `ACS-2`: every step attacked, then a repaired proof

Charged statement: if `A(F)` is empty or smooth and irreducible, then `F` is
a polynomial automorphism.

### 3.1 Smooth irreducible `A(F)` is an embedded `A^1`

Jelonek J-1: every irreducible component of `A(F)` is the image of a
polynomial map `C -> C^2`, hence rational with one place at infinity.  A
smooth complete rational curve is `P^1`.  One place at infinity therefore
gives a closed subvariety of `C^2` isomorphic to `A^1`.  This step is
correct, over `C`.

### 3.2 Classification of connected finite étale covers of `G_m × A^1`

After Abhyankar-Moh-Suzuki, a closed embedding `A^1 ↪ C^2` is equivalent to a
coordinate axis.  So `C^2 \ A ≅ G_m × A^1`, with `π_1^{top} = Z`.

Topologically there is a unique connected degree-`d` covering, corresponding
to the unique index-`d` subgroup `dZ ⊂ Z`, realized by
`(u,v) ↦ (u^d, v)`.

Algebraically: `π_1^{ét}(G_m × A^1) ≅ Ẑ`, by the Künneth sequence and
algebraic simple connectedness of `A^1`.  Unique index-`d` open subgroup,
unique connected finite étale cover of degree `d`, the same power map.  In
the other direction, Riemann existence algebraizes the unique topological
cover uniquely.  The classification is therefore algebraic, not merely
topological.  The charged report asserted this without naming either
comparison; the statement is true.

Consequently `C^2 \ F^{-1}(A)` is isomorphic to `G_m × A^1` **as a variety**.
The isomorphism is as covering spaces of `C^2 \ A` after choosing
coordinates, which is stronger than an abstract isomorphism, but the next
steps only need the abstract type of the source complement.

### 3.3 Unit rank, irreducibility, and `u^{±1}` versus `u^n`

Let `Γ = F^{-1}(A)_{red}`.  Then `O(C^2 \ Γ) ≅ C[u,u^{-1},v]`, whose unit
group is `C* × u^Z`, free rank 1.  For a reduced plane curve the unit group
of the complement is `C* × Z^r` with `r` the number of irreducible
components (Nagata-Rosenlicht; equivalently `H_1(C^2 \ Γ; Z) ≅ Z^r`).  Thus
`Γ` is irreducible.  This step is correct and is load-bearing: smoothness
plus `e_c(Γ)=1` alone does not kill an extra `C*` component, because
`e_c(A^1 ⊔ C*) = 1+0 = 1`.  The closed embedding `{y=0} ∪ {xy=1}` realizes
that Euler number; its complement has unit rank 2 and is not `G_m × A^1`.

The charged sentence "h corresponding to `c u`" is the gap.  An algebra
isomorphism `C[x,y][1/h] ≅ C[u,u^{-1},v]` sends the generator `u` of the
unit group modulo `C*` to `c h_1^{±1}`, where `h_1` is the unique irreducible
factor of a square-free `h`.  The exponent is `±1` because it is a generator,
not because of the covering degree `d`.  The `n` in the charged "units are
`c u^n`" parametrizes the unit group of the complement; it is not a licence
to identify `h` with `u^d`.  If `h` is non-reduced, `h = h_1^m`, the
primitive generator is still `h_1`, not `h`.

The sign `u^{-1}` versus `u` does not matter for the next sentence: both
`{u = λ}` and `{u^{-1} = λ}` are isomorphic to `A^1`.  Identifying `h` with
a higher power `u^n`, `|n|≠1`, would be wrong and is not forced.

The charged report never says why the abstract ring isomorphism makes the
level sets `{h=λ}` closed embeddings of `A^1` in `C^2`.  That is true, once
`h` (or `h_1`) is a regular function on `C^2` whose restriction generates
the units of the complement: `{h=λ}` for `λ ≠ 0` is the zero set of
`ψ(u-λ)` in the complement, hence isomorphic to `C[v] ≅ A^1`, and is closed
in `C^2` as a fibre of a polynomial.  Then AMS applies to `{h=λ}`.  This
path can be made to work, but it was not written.

Mixing the `G_m`-coordinate of the unique cover `(u,v) ↦ (u^d,v)` with the
equation of `A = {v=0}` is a second confusion.  The curve `F^{-1}(A)` is the
pullback of `{v=0}`, so it is cut by `v ∘ F`, not by the `u`-coordinate.
The covering degree `d` appears in `v ∘ F = c y^m` only after both curves
are coordinatized, and is then killed by the Jacobian, not by unit-group
arithmetic.

### 3.4 Nonzero fibres, AMS, and the triangular Jacobian

Once `h` is known to be a coordinate, `{h=λ} ≅ A^1` for every `λ` is
tautological and AMS is redundant.  The charged order (fibres of `h` are
`A^1` for `λ ≠ 0`, AMS, then `h` is a variable) is the longer correct path
sketched in §3.3, provided the ring isomorphism is in hand.

After source and target automorphisms, `A = {v=0}` and `F^{-1}(A) = {y=0}`
as reduced sets.  Then `v ∘ F` vanishes exactly on `{y=0}`, and
`C[x,y]^* = C*`, so `v ∘ F = c y^m`.  There is no missing `x`-dependence:
a polynomial vanishing set-theoretically on `{y=0}` and nowhere else is
`c y^m` with `c` a nowhere-zero polynomial, hence a constant.

Jacobian:

```text
J(P, c y^m) = P_x · (c m y^{m-1}) - P_y · 0 = c m y^{m-1} P_x = 1.
```

Thus `m=1` and `P_x` is constant, so `F(x,y) = (αx + q(y), c y)` is
triangular, an automorphism.  **No missing factor.**  This calculation is
correct and is the only place the Jacobian of `F` is used after the covering
lemma.

Source and target automorphisms preserve the Keller condition up to a
nonzero constant, which can be scaled to 1.

### 3.5 Cleanest repaired theorem and proof

**Theorem ACS-2.** Let `F: C^2 -> C^2` be a polynomial map with `J(F) ∈ C*`.
If `A(F)` is empty, or is smooth and irreducible, then `F` is a polynomial
automorphism.  In particular, a Keller counterexample has `A(F)` reducible
or singular.

**Proof.** The empty case is the last paragraph of §1.2.

Now let `A` be smooth and irreducible.  By Jelonek J-1 and smoothness, `A` is
a closed subvariety isomorphic to `A^1`.  By Abhyankar-Moh-Suzuki there is a
target automorphism sending `A` to `{v=0}`.  Replace `F` by the composite;
it remains Keller.  Then `C^2 \ A ≅ G_m × A^1`.

By Theorem ACS-1, `F: C^2 \ F^{-1}(A) -> C^2 \ A` is a connected finite étale
cover of degree `d`.  By the classification in §3.2, the source is isomorphic
to `G_m × A^1` as a variety.  Let `Γ = F^{-1}(A)_{red}`.

- Smoothness of `Γ`: `F` is a local biholomorphism and `A` is smooth, so `Γ`
  is smooth.
- Irreducibility: `H_1(C^2 \ Γ; Z) ≅ Z^r` with `r` the number of irreducible
  components, while `H_1(G_m × A^1; Z) ≅ Z`, so `r=1`.
- Euler: `e_c(G_m × A^1) = 0`, so `e_c(Γ) = 1` by additivity in `C^2`.
- Type: a smooth irreducible affine curve has `e_c = 2-2g-n` with `n ≥ 1`
  the number of places at infinity.  Then `2-2g-n = 1` forces `g=0`, `n=1`,
  so `Γ ≅ A^1`.

Abhyankar-Moh-Suzuki supplies a source automorphism sending `Γ` to `{y=0}`.
Write `F=(P,Q)` in the new coordinates.  Then `Q = c y^m`, and the Jacobian
computation of §3.4 forces `m=1` and `P = αx + q(y)`.  Thus `F` is a
triangular automorphism.  □

This proof never discusses δ-jumps on `A`, never classifies fibres of an
abstract `h`, and never identifies a unit with `u^d`.  The jumps are absorbed:
once both curves are coordinate axes, the Jacobian forbids `d>1`.

### 3.6 Countermodel showing Keller is essential for `ACS-2`

`F(x,y) = (x, xy)` has `A(F) = {x=0}`, which is smooth, irreducible, and
isomorphic to `A^1`.  The conclusion "automorphism" is false.  The charged
negative control was run only against `(★)`, not against `ACS-2`.  Étaleness
is used in ACS-1, in smoothness of `Γ`, and in the Jacobian identity
`J=1`.  Drop any of these and `ACS-2` fails.

A second control: `F(x,y)=(x,y^2)` is finite, hence proper, so `A=∅`, but
it is ramified and not an automorphism.  Empty nonproperness set does not
imply invertibility without the Keller condition.

A third control, for the cover classification: if `A` is reducible, say two
transverse lines, then `C^2 \ A ≅ G_m × G_m` with `π_1 = Z^2`.  There is no
longer a unique connected degree-`d` cover, and the argument that the source
complement is `G_m × A^1` is false.  Irreducibility is essential.

A fourth control, for smoothness of `A`: the cusp `{y^2=x^3}` has `e_c=1` and
is one-place rational, but `π_1(C^2 \ cusp)` is the trefoil group, not `Z`.
Smoothness of `A` is essential for the complement to be `G_m × A^1`, and is
also how smoothness of `Γ` is obtained.

### 3.7 Scope of the repaired theorem

The theorem is unconditional for complex Keller maps.  It is a qualitative
rigidity statement: a counterexample's `A(F)` is reducible or singular.  It
does not bound `td`, does not construct `A(F)`, and does not kill the
residue-A genome.  `SHEET6-CLASSICAL` §4a already records at least two
component families of `A(F)` for that template, which is compatible with
`ACS-2`.

---

## 4. `TDIC`

### 4.1 Meridian conjugacy for one irreducible component

Let `A = ∪_j A_j` be the decomposition into irreducible components, and let
`A_j°` be the smooth locus of `A_j` minus intersections with the other
components.  Then `A_j°` is connected (an irreducible complex curve minus a
finite set).  A meridian of `A_j` is the boundary of a small disc in `C^2`
transverse to `A` at a point of `A_j°`.  Transporting the disc along a path
in `A_j°` conjugates meridians.  Hence all meridians of `A_j` are conjugate
in `π_1(C^2 \ A)`.  This is standard for an irreducible divisor in a smooth
variety, and irreducibility is essential: meridians of distinct components
need not be conjugate, and typically are independent in `H_1`.

### 4.2 Exact local monodromy cycle type, including fixed points

Let `ρ: π_1(C^2 \ A) -> S_d` be the monodromy of the covering in Theorem
ACS-1.  Connectedness of the cover makes `ρ` transitive.  This representation
is well-defined up to conjugacy in `S_d`.

Take a small disc transverse to `A` at a generic point `q ∈ A_j°`, with
coordinate `z` vanishing at `q`.  The covering over the punctured disc has
`d` sheets.  Of these:

- `n(q) = d - δ(q)` sheets extend holomorphically across `q`, because `F` is
  a local biholomorphism at the `n(q)` affine preimages of `q`.  The meridian
  acts as the identity on those sheets.
- the remaining `δ(q)` sheets escape to infinity.  By the finite-end
  correspondence of
  `xmodel/g2-finite-end-asymptotic-monodromy-connection-sol-ultra-20260827.md`
  equation (1), `δ(q) = sum_{S: q_S=q} e_S`, and locally `z = unit · t^{e_S}`
  at each finite end.  The meridian acts as an `e_S`-cycle on the sheets
  associated to `S`.

The resulting permutation `σ_q ∈ S_d` therefore has cycle type consisting of
the parts `(e_S)_{S over q}` together with `1^{d-δ(q)}`.  Equation (2) of
that audit is confirmed: `δ(q) = sum e_S`, `support(σ_q) = sum_{e_S>1} e_S`,
and `index(σ_q) = sum (e_S-1)`.

An `e_S=1` end is a 1-cycle of `σ_q` that is **not** an affine sheet across
`q`.  The unmarked conjugacy class in `S_d` cannot distinguish it from an
affine fixed point.  That is the marked-versus-unmarked distinction already
recorded in the 2026-08-27 audit, and it is load-bearing for any CSP use.

### 4.3 What conjugacy actually transports

Conjugacy of meridians in `π_1(C^2 \ A)` implies that `ρ(μ_j)` has a
well-defined **unmarked** conjugacy class in `S_d`.  In particular the
unmarked cycle type is independent of the transverse disc, hence independent
of which coordinate pencil is used to present a transverse meridian.

The **marked** type — the partition of 1-cycles into finite ends versus
affine sheets, equivalently the pair `(cycle type, δ(q))` — is **not** an
invariant of a conjugacy class in `S_d`.  It is constant along `A_j°` for a
geometric reason: the finite-end profile of a generic transverse disc is
locally constant on the smooth locus of an irreducible component (constructible
and integer-valued on a connected curve).  Marked `TDIC` is therefore true,
but the charged report's deduction "conjugate in `π_1`, therefore marked
cycle type is pencil-independent, and this sees `e=1` ends because
`d-δ` is part of the cycle type" conflates two facts.  The unmarked class
does not see `e=1` ends.  The marked profile does, and it is locally constant
rather than conjugacy-invariant in `S_d`.

### 4.4 Recovery from coordinate pencils; tangencies; vertical/horizontal
components; multiplicities

Let `L_a = {u=a}` and `M_b = {v=b}` be the target coordinate pencils.

A loop in `L_a` around a point `q ∈ A ∩ L_a` is a meridian of the component
through `q` if and only if `L_a` is transverse to `A` at `q` and `q` is not
an intersection point or a δ-jump.  In that case its monodromy is `ρ(μ_j)`.

Failure modes, each of which produces a different permutation:

- **Tangency.**  Contact order `k ≥ 2`: the loop in the line is freely
  homotopic to `μ_j^k`, cycle type that of `σ^k`, not of `σ`.
- **Passing through an intersection or a singular point.**  The loop is a
  product of meridians of the local branches, not a single meridian.
- **The line contains a component.**  If `A_j ⊂ {u=a_0}`, a generic vertical
  line misses `A_j` entirely and supplies no meridian of `A_j`.

Genericity of `a` (the finite exceptional set in the 2026-08-27 setup: smooth
irreducible fibre, transverse to every `A_j`, avoiding `S` and exceptional
values of the boundary maps) kills the first two.  The third is the
vertical-component problem.

Write `ν_j: A^1 -> A_j` for the normalization, `k_j = deg(f ∘ ν_j)`,
`l_j = deg(g ∘ ν_j)`.  A generic vertical line meets `A_j` in `k_j` points,
a generic horizontal line in `l_j` points.  The charged T-A of the
2026-08-27 audit states `k_j > 0`; Chau's component-degree ratio, as banked
there, gives `k_j = α h_j` and `l_j = β h_j` with `h_j ≥ 1`, hence both
strictly positive.  **Granted that banked ratio, no Keller component of
`A(F)` is vertical or horizontal in the coordinates of `F`.**  Then each
component contributes its type to both generic pencils.

If the Chau ratio is not granted, set equality of types can fail for a map
whose `A` has an axis-parallel component: the generic vertical pencil sees
only non-vertical components.  A generic linear change of target coordinates
restores `k_j, l_j > 0` without Chau.  The charged `TDIC-SET` is stated in
the campaign's fixed `(f,g)` coordinates, so it needs either Chau or that
change.

**Multiset equality is false** even with Chau.  Component `A_j` contributes
`k_j` copies of `τ_j` vertically and `l_j` copies horizontally, and
`k_j / l_j = α/β`.  For residue-A one has `α=2`, `β=3`, so the two
multisets of types cannot coincide unless empty.

**Weighted equality is the correct global numerical form**, and is already
the marked component-block law (6) of the 2026-08-27 audit:

```text
n_τ(a) = α sum_{j: τ_j=τ} h_j,     n_τ(b) = β sum_{j: τ_j=τ} h_j,
```

hence `n_τ(a)/α = n_τ(b)/β`.  This needs component types only through their
equality classes, not through identification of individual ends with
components.

**Set equality** of the types appearing on a generic vertical line with
those on a generic horizontal line is a correct necessary condition for
Keller maps, granted Chau (or a generic target-coordinate change) and
generic transversality.  It is strictly weaker than the weighted form, and
it does not see `h_j` or `α,β`.  The charged reason — "each component
contributes exactly one class to each set, with multiplicities equal to its
intersection numbers" — correctly motivates using a set rather than a
multiset.  The multiplicities are not equal across pencils; that is why the
object is a set.

### 4.5 Corrected statements

**Theorem TDIC-COMPONENT.** Let `F` be Keller.  For each irreducible
component `A_j` of `A(F)`:

1. meridians of `A_j` are conjugate in `π_1(C^2 \ A)`, so the unmarked
   conjugacy class of `ρ(μ_j)` in `S_d` is well-defined;
2. the marked generic transverse inertia type `τ_j` (the unordered collection
   of end indices `(e_S)`, together with the count `d-δ` of affine 1-cycles)
   is locally constant on `A_j°`, hence independent of which transverse
   pencil is used to compute it.

**Theorem TDIC-SET (repaired).** Granted Chau's component-degree ratio, or
after a generic linear change of target coordinates: the set of unmarked
(resp. marked) generic transverse inertia types appearing on a generic line
`{u=a}` equals the corresponding set on a generic line `{v=b}`.  Equality of
multisets is not asserted.  The sharp global form is the weighted count
`n_τ(a)/α = n_τ(b)/β`.

### 4.6 The proposed residue-A `TDIC-SET` test is `NOT-TYPED`

The experiment in the charged §5 asks for the set of generic inertia cycle
types in the `{u=a}` pencil and in the `{v=b}` pencil, from banked finite-end
data and `SHEET6-CLASSICAL` §4a, for the frozen `td=6`, `m=2` residue-A
template.

**Vertical side is not a determined set.**  `SHEET6-CLASSICAL` §4a records
two *families* of finite ends on the generic vertical fibre `{f=a}` (B-side
and x-side), a per-value swallow ceiling `sum e_p ≤ 6`, and
`Sum(e_p-1) = 2g+6 ≥ 6`.  The B-side place partition and the x-side place
partition are unpinned (§2b, §2c, §3b).  Cycle type at a point of
`A ∩ L_a` depends on which ends share an asymptotic value: six x-side ends
of index 2 may be six meridians of type `(2)` or three of type `(2)(2)`, and
similarly for mixed B/x coincidences.  Feasible assignments exist with
different groupings.  The 2026-08-27 audit already filed component
identification as `SCOPE-CONFLICT`.  Set equality cannot be evaluated on a
set that is not determined.

The residue-A passport `(2)^a (2,2)^b (2,2,2)^c` with `a+2b+3c=42` is an
x-side branch-value count for the compactified `g` on the vertical fibre.  It
is not the set of meridian classes of `ρ` in `S_6`.

**Horizontal side is absent.**  Both B-side and x-side data in
`SHEET6-CLASSICAL` are punctures of `{f=a}`.  There is no banked finite-end
list for a generic `{g=b}`.  Chau's mass identity `M_f/α = M_g/β` couples
total weighted deficits, not cycle types.  Equation (2) of the 2026-08-27
audit is a local dictionary, not a horizontal computation.

**Stop condition of the charged Card B is already met:** the horizontal
pencil inertia cannot be derived from banked template data in one bounded
desk pass.  The correct output of the proposed experiment is `NOT-TYPED`,
not a match or a mismatch.

### 4.7 Van Dobben §5.4 is not repaired

Target meridians live in `π_1(C^2 \ A)`.  Source-end meridians live in the
plumbing of a compactification of the source.  Theorem ACS-1 defines `ρ` on
the former.  It supplies no word map from the latter to the former.  The
charged claim that ACS-1 "changes one of [van Dobben's] named blockers
(§5.4 target-meridian custody)" is false.  The objects remain distinct, as
that review stated.

---

## 5. Countermodels, collected

| Model | Hypothesis dropped | What fails |
|---|---|---|
| `F=(x,xy)` | étale / Keller | ACS-1: `F^{-1}A -> A` constant, not a covering. `(★)`: naive `1=0`. ACS-2: `A ≅ A^1` but `F` is not an automorphism |
| `F=(x,y^2)` | étale; `A=∅` | ACS-1: ramified, not a covering of `C^2`. ACS-2 empty case fails |
| `C* ↪ A^1` | constant cardinality on the closure | quasi-finite étale is not a covering of `A^1` |
| `z ↦ z^n` on `C*` | (none; positive control) | finite étale of constant degree is a covering of the stratum |
| node normalization | étale at `S` | singularities must lie in `S` |
| `{y=0} ∪ {xy=1}` | irreducibility of the missing curve | `e_c=1` but unit/`H_1` rank 2; complement is not `G_m × A^1` |
| two transverse lines as `A` | irreducibility of `A` | `π_1 = Z^2`; unique cover `z ↦ z^d` is false |
| cusp `{y^2=x^3}` | smoothness of `A` | `π_1` is the trefoil group, not `Z` |
| axis-parallel component of `A` | `k_j>0` | generic vertical pencil misses that component; `TDIC-SET` fails |
| tangent line to `A_j` | transversality | loop is a power of a meridian |
| `exp: C -> C*` | algebraicity / finite fibres | local biholomorphism is not a finite covering |

No explicit complex Keller counterexample to the repaired ACS-1, `(★_c)`, or
ACS-2 is produced, and none should be expected: those statements are
theorems.  The table exposes the hypotheses, not the conclusions.

---

## 6. What `(★)` adds to the fibre-side identity, and what it does not

Banked fibre-side identity (2026-08-27 T-A / Chau (4.4)):

```text
sum_{S in N_a} e_S  =  sum_j k_j δ_j  =  d + b_1(C_a) - 1.
```

Both sides are data of a generic source fibre `C_a = f^{-1}(a)` and of the
projection degrees of the components of `A`.  As a bound on `d` it is
circular, which the campaign already recorded.

The repaired `(★_c)` is

```text
sum_i δ_i e_c(C_i)  +  sum_{p in S} δ(p)  =  d - 1.
```

The left-hand side is a pairing of `δ` against target Euler geometry of
`A(F)`.  It does not mention `k_j` or `b_1(C_a)`.  That is the only new
information: a second linear constraint on the same function `δ`, with
different coefficients.

Special case, for orientation: if `A` were a disjoint union of closed
embedded `A^1`s with no δ-jumps, then `S=∅`, `e_c=1`, and `(★_c)` would
read `sum_j δ_j = d-1`, while T-A would read `sum_j k_j δ_j = d-1+b_1`.
Together those would constrain the projection degrees against fibre
topology.  By ACS-2 that case does not occur for a counterexample.

`(★_c)` is not a degree ceiling.  The charged report says it is not, and
that part is honest.  The surrounding rhetoric is not: "the cofinal-ceiling
problem is now a statement about the singularities and component count of
one plane curve" does not follow.  Because `e_c(C_i)` can be negative, a
bound on component count and on `#S` yields only an `O(d)` estimate of the
left-hand side of `(★_c)`, which is compatible with the right-hand side
`d-1` for all large `d`.  Bounding `δ(p)` by `d` re-enters on the right of
any naive inequality, which the charged §4.1 already names as the crux.
Jelonek J-2 as quoted in `SHEET6-CLASSICAL` §4 has enormous slack on the
residue-A genome (ceiling 251) and does not close that crux.

Evaluating `(★_c)` on the frozen residue-A template is **`NOT-TYPED`**:
`A(F)` is not constructed, the numbers `e_c(C_i)`, `#S`, and the grouping
of ends into points of `A ∩ L_a` are not banked, and `SHEET6-CLASSICAL` §4a
supplies only a swallow ceiling and an excess lower bound on the vertical
fibre.  Compatibility with ACS-2 ("reducible or singular") is already
visible from "at least two component families" and is not a kill.

---

## 7. Standard theorems and their exact roles

| Theorem | Role |
|---|---|
| Inverse function theorem / étale = local biholomorphism over `C` | ACS-1 étale; smoothness of `F^{-1}(A)` over smooth `A`; local cycle structure of meridians |
| Étale of finite type `=>` quasi-finite | ACS-1 fibres 0-dimensional on all of `C^2` |
| Jelonek: `A(F)` empty or a curve; `F` proper off `A`; for Keller maps, `A = {δ>0}`; J-1 one-place rationality | properness, degree constancy, `A` a curve, `ACS-2` input, one-place type of each `C_i` |
| Proper + quasi-finite `=` finite; ZMT | ACS-1 finiteness; stratum-covering lemma |
| Finite étale over `C` `=` finite topological covering; Riemann existence | ACS-1 covering space; algebraicity of the unique cover of `G_m × A^1` |
| `C^2` simply connected; `H_1(C^2 \ curve) ≅ Z^r` | empty-case inversion; nonemptiness of `F^{-1}(A)`; irreducibility in ACS-2 |
| `e_c` additivity; `e=e_c` on smooth complex manifolds; covering multiplicativity of `e` | `(★_c)` and ACS-1(i) |
| Iitaka: `κ` invariant under finite étale | ACS-1(ii) only |
| Abhyankar-Moh-Suzuki | ACS-2: embedded `A^1` is a coordinate, source and target |
| `π_1^{ét}(G_m × A^1) ≅ Ẑ` | unique connected algebraic degree-`d` cover |
| Nagata-Rosenlicht units, equivalently `H_1` rank | ACS-2 irreducibility (alternative to `H_1`) |
| Chau 1999 (4.4) and component-degree ratio, as banked in the 2026-08-27 audit | fibre-side identity; `k_j,l_j>0`; weighted `TDIC` |
| Conjugacy of meridians of an irreducible divisor | unmarked `TDIC` |
| Local constancy of a constructible integer function on a connected curve | marked `TDIC`; δ-stratification |

No literature-originality claim is made or endorsed.  The charged
`KNOWN`/`NEW`/`UNVERIFIED` labels are out of charge for this review.

---

## 8. Downstream consequences and the cheapest sound next discriminator

Licensed:

- Theorem ACS-1 as setup for any later argument that needs the covering
  `C^2 \ F^{-1}A -> C^2 \ A`.
- Theorem ACS-2 as a qualitative constraint: a counterexample has `A(F)`
  reducible or singular.
- `(★_c)` as an Euler identity in the constructible function `δ` on `A`,
  once `A` is known.
- `TDIC-COMPONENT` as a per-component statement, marked by local constancy
  and unmarked by conjugacy.

Not licensed:

- Any cofinal `td` ceiling, any residue-A kill, any claim that `(★)` is a
  positive decomposition, any evaluation of `(★)` or `TDIC-SET` on banked
  residue-A data, any raise of Avenues 6/7/25/26/27/28/30/31 on the strength
  of these claims, any assertion that ACS-1 retires `SHEET6` T3 `NEEDS-DATA`
  or van Dobben §5.4, any construction of `A(F)`.

**Cheapest sound next discriminator.**  Card B's own stop condition is
already satisfied: `TDIC-SET` on residue-A is `NOT-TYPED`, and the missing
horizontal (and even vertical grouped) inertia cannot be produced from
banked data in one desk pass.  Do not run the test.  Do not fund component
construction or a braid project from these cards.

The independent re-derivation of `(★)` that Card A named as its first
discriminator is this review: the identity survives as `(★_c)`, the
positivity/ceiling reading does not.  Card A's second step, plugging
residue-A numbers into `(★)`, is likewise `NOT-TYPED`.

What remains usable at zero extra cost is the repaired ACS-2: it is
compatible with the already-banked "at least two component families" and
does not change the residue-A status.  The standing Avenue 7 debt —
construct the normalized components of `A(F)` — is not cheapened by `(★)`
or `TDIC-SET`.

---

## 9. Charge-by-charge answers, compressed

1. ACS-1 is true for Keller maps.  Étale from `J ∈ C*`; quasi-finite from
   étale; proper off `A` from Jelonek; finite from proper + quasi-finite;
   surjective from finite étale onto a connected target; degree `td` from
   constancy plus density; connectedness from plane-curve complements, with
   `F^{-1}(A)` nonempty when `A` is, by `π_1`.
2. Constant fibre cardinality on a smooth locally closed curve stratum does
   make the restricted quasi-finite étale morphism a finite étale /
   topological covering of that stratum, for `n ≥ 1`, by the Hausdorff
   slice argument (or ZMT).  It does not make `F^{-1}(A) -> A` a covering.
   Refine `S` to singularities, component intersections, and δ-jumps.
   The identity holds for `e_c`.  `e(C)` can be negative.  The right-hand
   side is not a positive decomposition.
3. `ACS-2` is true.  The charged proof is incomplete at the algebraic cover
   classification, the unit-to-coordinate step, and the identification of
   `h` with a primitive unit rather than a power.  The triangular Jacobian
   has no missing factor.  The repaired proof is §3.5.
4. Meridian conjugacy holds per irreducible component and gives unmarked
   classes.  Marked types, including `e=1` ends, are locally constant, not
   conjugacy invariants in `S_td`.  Pencil recovery requires transversality
   and `k_j, l_j > 0`.  Equality is a per-component statement, or a set
   (not a multiset) globally, or a Chau-weighted count.  Residue-A
   `TDIC-SET` is `NOT-TYPED`.
5. Countermodels: §5.
6. `(★_c)` is a second linear form in `δ`, against target Euler rather than
   against `k_j` and `b_1`.  It is not a ceiling.
7. Standard theorems: §7.

Nothing in the charged ACS/TDIC block proves or disproves JC2, closes
`td=6`, or constructs `A(F)`.

The SHA-256 below is the digest of the on-disk bytes of this file strictly
above the delimiter, computed after the final write.

<!-- self-hash -->
75405dc8cd5df8e845cfbb11ab246a4ba596db4f8cc655a4d81b99f086392757  report body above this delimiter
