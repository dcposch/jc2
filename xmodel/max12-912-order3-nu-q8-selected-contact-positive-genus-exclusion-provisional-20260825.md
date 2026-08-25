# Selected-Q8 positive-genus trajectory exclusion — provisional composition

Date: 2026-08-25  
Status: **PROVISIONAL EXACT COMPOSITION; point-count hostile review and this
composition's independent hostile review pending**

## 1. Theorem at the registered scope

Assume the already reviewed cube/Faber and global-quotient reductions place
an **actual** order-three trajectory in the strict selected leaf

```text
k=mu=0,  nu!=0,
```

and its coefficient image meets a corrected-Q8 contact.  Consume the exact
positive-genus point count below.  Then no such trajectory exists.

This is a theorem only conditional on the registered selected-leaf landing.
It is not an exclusion of every `nu!=0` component, the polynomial core,
`(8,12)`, all `(9,12)`, maximum twelve, an arbitrary `(6,9)` pair, an
arbitrary Keller pair, or JC2.

## 2. Immutable inputs

| Input | Producer / successor SHA-256 | Independent review SHA-256 | Consumed statement |
|---|---|---|---|
| Selected global quotient | `2102e5d730af7d9bd4a434a99ea9b7213cdf08016becd0e49061f5210ec0feaa` | `49e8d9092e257a003f39171d0ec53fca91cc8f5c6e02841816f88aad127e6b39` | same six-row selected source and actual-trajectory quotient |
| Mod-127 source component | `7d28a7b4b7d3ecd3179efc73f0251754fbfea87614b6eb6daef2d7d649dba202` | `ebd0024dfe2ea1623f22ba483b93d76dd9ff2aabe5f9f96eabc7b115928c7164` | an integral relevant source component dominates `H`, separably |
| Plane `H` integrality | `b3cddbce9a118c60bf789df374941367a327b6608871a562ddffceebc3b900d0` | `f2e24aa5baa336067479eab7549f74bd2ceda7f61b5da2a049ea75be73d835dc` | `H/F_127` is geometrically integral |
| Rational full contact on `H` | `c470fd253d59cc2f3377e5a2c03baa345c22b365522a3eb17ae320992fb5d925` | `658341959f39cdcad00e5f42d440af8bdb7fb2454b6676c96e6b00bddb10b562` | at least one of `v=26,58,67` lies on an `H`-supported source component |
| Arithmetic full-contact bridge | `39ae622919f5eba41e4e1a18d6777749d38c34a1be4a10569f65295815a11490` | `571221ad8a87c23a1ad15b4b77da3c8b9332c4d93a521d2ef6c143d5f143046d` | common integral source, contact completion `R[[w]]`, same generic selected germ |
| Positive genus of `H` | `c4c4ebdf59a95ff84c37ebbedcd46608fb32f34077790c9bdbdaac776f64a00a` | **pending in this version** | exact `F_(127^2)` count gives `g(H)>0` |
| Conditional curve-theory audit | `53830f8b28a20491e2ef08810070c029101b9ca95db52f2d6814de29cb654c18` | `4842ff192308c2c0577be48dd370af589d822747b4f0b1109ef938aa83d26c75` | proper/residue-genus obstruction, conditionally sound |
| Infinity and primitive grouping | `89691023f2703eba5c0cd29d65bc8732d837905fe41b01f64ae9d3b908068168`; `9f37fc3fc7933b911bea56258f677da77a823caa8daf9ce01c03b0884c502c8f` | `c77a73307bfda48fdde7792c523e09ee4d565c5782bcf71ed13d13b1d613a57c` | nonconstant trajectory map and partition `8` or `1+...+1` |

Positive-genus case custody is additionally fixed by manifest SHA
`8de0e649576effad425482583fa5a474b422a5e991446888fdad9743c12578b7`
and FREEZE SHA
`7f134d213c45512883eb65f79b5882c160b917e1d3c21a2cc9875ca9e8fa49fd`.
The corrected no-merger lemma is **not** used: neither global all-contact
grouping nor a degree-one coordinate graph is needed below.

## 3. Exact genus input

Two independent complete AWS partitions of

```text
F_(127^2) = F_127[a]/(a^2-a+3)
```

give for the pinned `H(w,v)`:

```text
affine points       16174
singular affine         6
smooth affine       16168
#P1(F_(127^2))      16130.
```

Every smooth affine point lifts uniquely to an `F_(127^2)`-point of the
smooth projective normalization `Htilde`.  The reviewed rational smooth point
on `H` gives a rational point on `Htilde`.  If `g(Htilde)=0`, then
`Htilde ~= P1`, contradicting

```text
#Htilde(F_(127^2)) >= 16168 > 16130.
```

Therefore `g(Htilde)>0`.  This paragraph remains producer-tier until the
separate point-count hostile review closes.

## 4. Whole-source local attachment

Choose the rational full contact `q` whose existence is supplied by the
reviewed `40960>37010` theorem.  Thus `q` lies on an integral mod-127 source
component `C` whose plane projection dominates `H`.

Work after a complete unramified splitting-DVR extension `R`, with fraction
field `K`, residue field `k`, and uniformizer 127.  Let `X/R` be the common
eight-equation localized source from the reviewed arithmetic bridge.  That
bridge proves, for the **whole source local ring** rather than a chosen plane
section,

```text
O^hat_(X,q) ~= R[[w]].                                (4.1)
```

It also identifies the unique generic formal germ with the reviewed selected
characteristic-zero component `Y`.

Let `Z` be the scheme-theoretic closure of `Y` in `X`.  In the completed
domain `R[[w]]`, the defining ideal of `Z` vanishes after inverting 127,
because `Y` is the unique generic component through the contact.  Since
`R[[w]]` is 127-torsion-free, that ideal is zero.  Hence

```text
O^hat_(Z,q) ~= R[[w]],
O^hat_(Z_k,q) ~= k[[w]].                              (4.2)
```

In particular the special fibre of the horizontal closure has exactly one
reduced branch through `q`, with multiplicity one.  The same regular local
ring permits only one special source component through `q`.  Since the
reviewed contact theorem places `q` on the `H`-supported component `C`, the
branch in (4.2) is the local branch of `C`.  This is the load-bearing
component identity.  Point incidence in the plane curve alone would not imply
it; the whole-source completion (4.1) does.

## 5. The special component has positive genus

The nonconstant projective map from the normalization `Ctilde` to `Htilde`
is finite.  It is separable: the reviewed source-component theorem makes `w`
a local parameter at `q`, and its pullback differential is nonzero.  A
generically inseparable extension of one-variable function fields in
characteristic 127 would annihilate every pulled-back differential.
Riemann--Hurwitz therefore gives

```text
g(Ctilde) >= g(Htilde) > 0.                            (5.1)
```

Only strict positivity is consumed; source degree one is unnecessary.

## 6. A rational generic trajectory cannot specialize this way

Suppose an actual trajectory existed.  The reviewed infinity theorem gives a
nonconstant morphism from its source `P1_x` to the projective normalization
`Ytilde` of its selected coefficient component.  In characteristic zero,
Lueroth (equivalently Riemann--Hurwitz) makes `Ytilde` a genus-zero curve.

Properify the closure `Z` without changing the affine neighborhood (4.2),
normalize it, and extend the divisorial valuation determined by `C` to the
finite rational function-field extension induced by
`P1_x -> Ytilde`.  After an algebraic residue-field extension, the ruled-
residue theorem says that a residually transcendental divisorial valuation of
`K(P1)` has rational residue function field.  Its residue field contains a
finite extension of `k(C)`.  Lueroth then forces the normalization of `C` to
be rational, contradicting (5.1).

Equivalently, after finite base change and semistable reduction, a genus-zero
generic curve specializes to a tree of rational normalized components; the
reduced multiplicity-one positive-genus component supplied by (4.2)--(5.1)
cannot occur.  Properization is essential; no affine point-count argument is
being transported directly to characteristic zero.

Thus the particular selected characteristic-zero component attached at `q`
admits no nonconstant map from `P1`.

## 7. Primitive alternatives

The reviewed Galois action permits exactly:

```text
one component containing all eight corrected-Q8 contacts, or
eight singleton Galois-conjugate components.
```

The all-eight component already carries no registered actual trajectory by
the reviewed infinity theorem: two distinct contact points cannot both be the
single image of `x=infinity`.  In the singleton case, the component attached
at `q` has positive-genus obstruction by Sections 4--6, and all eight
singleton normalizations are Galois conjugate, hence have the same genus.
No singleton admits a nonconstant `P1` map.  Therefore neither primitive
alternative carries the registered actual selected-Q8 trajectory.

## 8. Firewall and sole review debt

This report consumes no generic degree-190 length, global coordinate graph,
all-eight mod-127 component, Padé reconstruction, Taylor-pole enumeration, or
the repaired global no-merger lemma.  Components disjoint from corrected-Q8
contacts remain untouched.

The composition is frozen as **provisional** because two independent hostile
verdicts are still outstanding in this version:

1. the exact extension-field point-count review; and
2. the proper/ruled-residue composition review.

No broader maximum-twelve or Jacobian-conjecture statement may consume this
file even if both verdicts confirm it.
