# Hostile review — principal-part/UFD saturation-slice erratum V2 of the `(8,12)` order-two first normal gate

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-20260826.md` |
| Target SHA-256 | `4c9d9cfc58eb4ca2a33c9bf83beb485c15f0796fa36d2ffe4826c3fdeeac374d` |
| Frozen V1 | `xmodel/max12-812-order2-first-normal-principal-part-ufd-theorem-20260826.md` |
| Frozen V1 SHA-256 | `988d659f0a25f14a612d316608a8dc7c36d839c3f253c35e7e785d33e5923fb5` |
| Frozen V1 review | `xmodel/max12-812-order2-first-normal-principal-part-ufd-review-grok-20260826.md` |
| Frozen V1 review SHA-256 | `affd9b6004abc8078e2ae5b3ddc88307d7242d3ac8aa18eac36a21da0fed3639` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer. Charged reviews were opened only because they are named; no producer status line and no charged `CONFIRMED`/`REPAIR` string is evidence |
| Method | source reading and hand derivation only; SHA-256 of the target, frozen V1, and frozen V1 review; no Singular, Sage, msolve, Lean, or substantive exact Python |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `574e873d4753b57dbaeb0fb83e320fbef3694724` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the target is
`4c9d9cfc58eb4ca2a33c9bf83beb485c15f0796fa36d2ffe4826c3fdeeac374d`,
matching the required pin. Independently recomputed SHA-256 of the two
artifacts pinned in target §0 match those pins. Producer verdict language,
the target's own status line, charged review tokens, and the dual-prime
endpoint were not used as evidence. No file other than this review was
written.

---

## Verdict

**CONFIRMED.**

The erratum withdraws exactly the V1 §4 saturation-before-slice equality
that the charged V1 review marked `REPAIR`, and does not reopen any
confirmed coefficient identity. Sequential multi-generator saturation
`I* = ((I:A^infinity):B^infinity)` is the reviewed first-normal ideal
`Q1*`, formed in the full eight-space before the slice `k10=0`. The
sliced-then-saturated object `I0*` is the colon the V1 argument actually
controlled. Reduced support of `I0*` is exactly the union of the two named
affine closures. On the actual first-contact open `O`, saturation-before-
slice agrees with that union. Both closures, including every zero-normal
and weighted-origin boundary point, embed into `V(I*) intersect V(k10)`.
Every residual point of the unsaturated-before-slice fibre lies on the
zero-normal section with nonsquare `K`. The characteristic-zero Padé
support statement `(4.1)` empties that residual as a reduced set: the
square locus is closed and disjoint from the squarefree locus, so neither
a `k10!=0` branch, nor a vertical special-fibre component, nor an
embedded or nonreduced primary can add a new reduced point. V1 is not
silently promoted: `(1.1)`, `(1.2)`, both parameterizations, and the
arbitrary-load square solution survive, and no radical, reducedness,
scheme, or strict-arc claim is made.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-order2-first-normal-principal-part-ufd-erratum-v2-20260826.md` | `4c9d9cfc58eb4ca2a33c9bf83beb485c15f0796fa36d2ffe4826c3fdeeac374d` | target (matches required pin) |
| `xmodel/max12-812-order2-first-normal-principal-part-ufd-theorem-20260826.md` | `988d659f0a25f14a612d316608a8dc7c36d839c3f253c35e7e785d33e5923fb5` | frozen V1 (matches target §0) |
| `xmodel/max12-812-order2-first-normal-principal-part-ufd-review-grok-20260826.md` | `affd9b6004abc8078e2ae5b3ddc88307d7242d3ac8aa18eac36a21da0fed3639` | frozen V1 review (matches target §0); confirmed identities charged as context, not as proof of the repaired slice logic |

The V1 review's confirmed identities `(1.1)`, `(2.1)`, `(3.1)`--`(3.6)`,
including every sign and constant, and the arbitrary-`k10` square solution
of the full first gate, are used only as charged algebraic input. The
repaired statements `(2.1)`, `(2.2)`, `(3.1)`--`(3.4)`, and the conditional
emptiness of `E` under `(4.1)`, are rederived below from those identities
together with the definition of multi-generator saturation. Dual-prime
component counts are not used.

---

## Strongest exact theorem that survives

Work over a characteristic-zero field `L` in the first-normal chart, with
the charged identities `(1.1)` and `(1.2)` and the two closed families

```text
S: K=(z^2+s)^2,
   N=(z^2+s)*(alpha*z+beta),
   k10=0,

D: K=(z-a)^2*(z^2+2*a*z+d),
   N=lambda*(z-a)*(z^2+2*a*z+d),
   k10=0,
```

and with `I=(q1,...,q7)`, `A=(p,c,r)`, `B=(n0,n1,n2,n3,k10)`. Let

```text
I*  = ((I:A^infinity):B^infinity),
I0* = (((I+(k10)):A^infinity):B^infinity),
O   = V(k10) intersect D(A) intersect D(n0,n1,n2,n3),
E   = (V(I*) intersect V(k10)) \ (S union D).
```

Then, as reduced supports of closed sets in the affine eight-space:

1. `I*` is the reviewed gate `Q1*`. Saturation is by the multi-generator
   ideals `A` and `B`, in that order, in the full space, before any slice.
   Geometrically `V(I*)_red = cl(V(I) \ (V(A) union V(B)))`. This is not
   saturation by the product `p*c*r`, which would delete the coordinate
   faces and in particular delete `S` (on which `c=0` identically).

2. `V(I0*)_red = S union D`. The zero-normal three-space
   `Z={N=0, k10=0, K arbitrary}` is an irreducible component of
   `V(I+(k10))` supported wholly on `V(B)` and is deleted. Both `S` and
   `D` meet `D(A)` and `D(n0,n1,n2,n3)` in a dense open, so neither
   component is deleted, and taking closures restores every boundary
   point.

3. `(V(I*) intersect O)_red = ((S union D) intersect O)_red`. Saturation
   does not change geometric points on `D(A) intersect D(B)`, and every
   raw first-gate point of `O` is classified by `(1.2)`.

4. `S union D subset V(I*) intersect V(k10)`, including the weighted origin
   `s=0` or `(a,d)=(0,0)` and the zero-normal boundaries
   `(alpha,beta)=(0,0)` or `lambda=0`.

5. `E subset V(k10,n0,n1,n2,n3) intersect {K nonsquare}`. Every
   hypothetical `k10!=0` specialization that can leave `S union D` must
   kill `N` and land on a nonsquare `K`; a square limit is already in
   `S`.

6. If `k10!=0` and `q1=...=q7=0` imply that `K` is square, then `E` is
   empty as a reduced set, and
   `V(I*)_red intersect V(k10) = S union D`. No vertical, embedded, or
   nonreduced primary creates an extra reduced point. This implication is
   not proved here.

This is a corrected reduced-support theorem for the first-contact slice.
It does not prove `(4.1)`, equality of nonreduced ideals, absence of
embedded components, reducedness of `I*`, a characteristic-zero radical,
a strict arc, higher-contact geometry of the zero section, the terminal
`[6,2]` passport, either Taylor boundary, exclusion of order two, closure
of `(8,12)`, maximum twelve, or JC2.

---

## Attack 1 — definitions and order of `I*`, `I0*`; multi-generator irrelevant saturation

**CONFIRMED.**

Ambient coordinates are `(p,c,r,n0,n1,n2,n3,k10)`. The charged jet theorem
writes

```text
mK = (p,c,r),
mN = (n0,n1,n2,n3,k10),
Q1* = (Q1 : mK^infinity) : mN^infinity.
```

Target `(2.1)` is that colon with `I=Q1`, `A=mK`, `B=mN`. Saturation
occurs in the full eight-space; `k10` is still a coordinate. That is
exactly the object whose global reduced-support equality V1 overclaimed.

Target `(2.2)` forms the sliced ideal `I+(k10)` first, then applies the
same two colons. That is the object the V1 §4 argument actually proved
statements about.

Multi-generator saturation has the standard geometry, already recorded in
the charged V1 review:

```text
V((I:A^infinity):B^infinity)_red
  = cl( V(I) \ (V(A) union V(B)) ).
```

`V(A)` is the weighted-projective origin `(p,c,r)=(0,0,0)`, not the union
of the three coordinate hyperplanes. `V(B)` is the simultaneous zero
section `N=0` and `k10=0`, not the union of the five coordinate
hyperplanes. Sequential order `A` then `B` is the reviewed order; for
reduced support the order is immaterial, because `V(A) union V(B)` is
symmetric. Saturation by the sum `A+B` would be a different operation
(`cl(V(I) \ (V(A) intersect V(B)))`) and is not what is written.

The product-saturation alternative `(p c r)^infinity` is incompatible
with the rest of the note: `S` is contained in `V(c)`, hence would be
deleted entire, and the later claim that `S` meets `D(A)` densely would
be false. The notation `D(A)` is used throughout as the complement of
the origin, which is the multi-generator convention.

On the slice `k10 in I+(k10)`, the two colons by `B=(n0,...,n3,k10)` and
by `(n0,...,n3)` coincide. Indeed if `J` contains `k10` and
`(n0,...,n3)^M f subset J`, then every monomial generator of `B^M f` is
either already in `J` by the `k10` factor or is a degree-`M` monomial in
the `n_i` times `f`. Conversely `B` contains `(n0,...,n3)`, so the colon
by `B` is a priori smaller. Thus on `V(k10)` one has
`D(B) intersect V(k10) = D(n0,n1,n2,n3) intersect V(k10)`, which is the
target's sentence after `(2.2)`.

`k10` remains in `I0*` because `I+(k10) subset I0*`. No `k10!=0` point is
reintroduced by the colon.

---

## Attack 2 — sliced-then-saturated equality `V(I0*)_red = S union D`

**CONFIRMED.**

By charged `(1.2)`, geometric points of `V(I) intersect V(k10)` are
exactly the points with `k10=0` and `K | N^2` in `L[z]`. Charged UFD
gives `K | N^2` iff `D_K | N`. With `deg K=4` and `deg N <= 3` the
odd-multiplicity kernel of `K` has degree `0`, `2`, or `4`:

- degree `0` is the square family `S`, including its zero-normal locus
  `alpha=beta=0`;
- degree `2` is the discriminant family `D`, including its zero-normal
  locus `lambda=0`, and covering partitions `[2,1,1]` and `[3,1]`;
- degree `4` forces `N=0`, i.e. squarefree `K` on the zero-normal
  section.

Let `Z = {N=0, k10=0, K arbitrary}`. Then as reduced sets

```text
V(I+(k10)) = S union D union Z.
```

`S` is cut out by the `L`-equations `c=0`, `p^2=4r`, `2 n1 = p n3`,
`2 n0 = p n2`, `k10=0`, hence closed and isomorphic to `A^3` on
`(p,n3,n2)`. `D` is the image of the polynomial map
`(a,d,lambda) |-> (3.6)` of charged V1; equivalently, on `k10=0`, the
closed locus `disc(K)=0` together with the closed remainder conditions
`D_K | N`. Every depressed quartic with a multiple root is of the form
`(z-a)^2 (z^2+2 a z+d)`, so the `K`-projection of `D` is exactly
`V(disc)`. Both loci are closed. Their union does not contain the
squarefree open of `Z`.

`Z` is isomorphic to `A^3` on `(p,c,r)`, irreducible, and not contained
in `S union D`. It is therefore an irreducible component of
`V(I+(k10))`. It is supported wholly on `V(B)`, so `B`-saturation deletes
it as a component.

It remains to see that neither `S` nor `D` is deleted, and that the
closure of what remains is the full union. Write
`U_0 = V(I+(k10)) \ (V(A) union V(B))`. Then
`V(I0*)_red = cl(U_0)`. Since `Z subset V(B)`,

```text
U_0 = (S union D) intersect D(A) intersect D(n0,n1,n2,n3).
```

On `S`, `V(A)` is the single point `s=0` and `V(B)` is the plane
`alpha=beta=0`. The complement `s!=0` and `(alpha,beta)!=(0,0)` is a
nonempty Zariski-open of the irreducible `A^3`, hence dense in `S`. On
`D`, `V(A)` is the single parameter point `(a,d)=(0,0)` (if `a=0` then
`p=d` and the origin forces `d=0`; if `a!=0` then `a^2 d=0` forces
`d=0` and `p=-3 a^2 !=0`). Also `N=0` iff `lambda=0`, because
`(z-a)(z^2+2 a z+d)` is monic of degree three. Thus `lambda!=0` and
`(a,d)!=(0,0)` is a nonempty open of the irreducible image, hence dense
in `D`. Therefore

```text
cl(U_0) = S union D,
```

which is `(3.1)`. The zero-normal boundaries of `S` and of `D` are
restored as affine-closure points of retained components; they are not
retained as a residual piece of the deleted component `Z`. The identity
is reduced support, not equality of nonreduced ideals.

---

## Attack 3 — equality on `O = V(k10) intersect D(A) intersect D(n0,n1,n2,n3)`

**CONFIRMED.**

On the two saturation opens, taking closure does not add geometric
points:

```text
V(I*) intersect D(A) intersect D(B)
  = V(I) intersect D(A) intersect D(B).
```

Intersecting with `V(k10)` and using Attack 1's identification
`D(B) intersect V(k10) = D(n0,...,n3) intersect V(k10)` yields
`V(I*) intersect O = V(I) intersect O`. Charged `(1.2)` classifies
`V(I) intersect O` as the points of `O` with `K | N^2` and `N!=0`. The
squarefree locus is absent from `O` because `N=0` there, and the origin
is absent because it is not in `D(A)`. The remaining points are exactly
`(S union D) intersect O`. This is `(3.2)`.

The identity does not use the Padé lemma. A hypothetical `k10!=0`
nonsquare branch that specializes to a point of `O` has limit with
`k10=0` and `N!=0`, hence is already named by `(1.2)`. Extra points of
`V(I*) intersect V(k10)`, if any, cannot land in `O`.

---

## Attack 4 — full affine closures `S`, `D` lie in `V(I*) intersect V(k10)`

**CONFIRMED.**

`S subset V(I)` by charged `(1.2)` on `k10=0`, and in fact the same
equations solve every first-normal row for arbitrary `k10` because both
`N^2/K = (alpha z+beta)^2` and `K^(5/2) = (z^2+s)^5` are polynomials.
`D subset V(I)` by charged `(1.2)`, since `K | N^2` on `D`. Both families
meet `D(A)` and `D(B)` in a dense open (Attack 2). Therefore

```text
S = cl(S intersect D(A) intersect D(B))
  subset cl(V(I) \ (V(A) union V(B)))
  = V(I*),
```

and likewise for `D`. Restricting to `k10=0` is `(3.3)`.

Explicit boundary points, all retained:

| point | in | why retained |
|---|---|---|
| `s=0`, `(alpha,beta)` arbitrary | `S cap V(A)` | limit of `s=epsilon`, same `(alpha,beta)` |
| `alpha=beta=0`, `s` arbitrary | `S cap V(B)` | limit of `alpha=epsilon`, `beta=0`, same `s` |
| `(a,d)=(0,0)`, `lambda` arbitrary | `D cap V(A)` | limit of `(a,d)=(epsilon,0)` or `(0,epsilon)` |
| `lambda=0`, `(a,d)` arbitrary | `D cap V(B)` | limit of `lambda=epsilon`, same `(a,d)` |
| the common origin | `S cap D cap V(A) cap V(B)` | simultaneous limits as above |

None of these points is deleted by saturating a component that is not
contained in `V(A)` or `V(B)`.

---

## Attack 5 — exceptional-set containment `(3.4)`; hypothetical `k10!=0` specializations

**CONFIRMED.**

Let `x` be a point of `V(I*) intersect V(k10)` outside `S union D`. By
`(3.2)`, `x` is not in `O`, so `x` lies in `V(A)` or in `V(n0,...,n3)`.
Always `V(I*) subset V(I)`, so `x` satisfies charged `(1.2)`.

- If `N!=0` and `(p,c,r)=0`, then `K=z^4` is square, and `K | N^2`
  forces `z^2 | N`, which is `S` at `s=0`. Such an `x` is not in `E`.
- If `N=0` and `K` is square, then `x` is the zero-normal locus of `S`,
  not in `E`.
- If `N=0` and `K` is nonsquare with a multiple root, then `x` is the
  zero-normal locus of `D`, not in `E`.
- The residual is therefore `N=0`, `k10=0`, and `K` squarefree, which
  is contained in `V(k10,n0,n1,n2,n3) intersect {K nonsquare}`.

This is `(3.4)`. The right-hand side is slightly larger than the exact
residual `Z_sf := {N=0, k10=0, K squarefree}` — it also contains the
zero-normal locus of `D`, which is not in `E` — but the displayed
relation is a containment, and it is correct. The following sentence of
the target already names the unresolved possibility as a squarefree
zero-normal limit, which is the exact residual.

Hypothetical `k10!=0` specializations, charged one by one:

1. `k10!=0`, `K` nonsquare, `N!=0`, specializing to `N=0`, `k10=0`, and
   a squarefree `K_0`. The limit lies in `Z_sf subset` right-hand side
   of `(3.4)`, and lies in `E` if it lies in `V(I*)`. No escape from
   `(3.4)`.
2. `k10!=0`, `K` nonsquare, `N=0` already (pure load cancellation
   `[K^(5/2)]_-` having seven vanishing coefficients), then `k10 -> 0`.
   The limit has `N=0`, `k10=0`, same `K`. If that `K` is squarefree the
   limit is in `E` and in the right-hand side; if it has a multiple root
   the limit is in `D`, not in `E`.
3. `k10!=0`, `K` nonsquare, `N!=0`, specializing to `N!=0`, `k10=0`. The
   limit lies in `O` or at the origin. Attack 3 puts it in `S union D`,
   not in `E`.
4. `k10!=0` along the actual square/load family. The limit lies in `S`,
   not in `E`.
5. any of the above specializing to the origin. The origin lies in
   `S cap D`, not in `E`.

A point of `Z_sf` lies in `V(I*)` if and only if it lies in
`cl(V(I) \ (V(A) union V(B)))`. It cannot be approached from `U_0`,
because `cl(U_0)=S union D` is closed and disjoint from `Z_sf`. Any
approximating net in the complement of `V(A) union V(B)` must therefore
have `k10!=0`. That is precisely a `k10!=0` branch of `V(I)` specializing
onto `Z_sf`, which charged V1 §5 and the present `(4.1)` leave open. No
such net is constructed or excluded here, and none is needed for the
containment.

---

## Attack 6 — does `k10!=0 => K square` empty `E`, or does a vertical / embedded / nonreduced component leave a reduced-support gap?

**CONFIRMED** that `(4.1)` empties `E` as a reduced set. No remaining
reduced-support gap.

Assume every geometric point of `V(I)` with `k10!=0` has `K` square.
The square locus `{c=0, p^2=4r}` is Zariski closed in `(p,c,r)`-space.
The squarefree locus `{disc(K)!=0}` is open and disjoint from it. A net
of square `K` cannot accumulate at a squarefree `K`.

Consequently

```text
cl( V(I)_red intersect D(k10) ) intersect {K squarefree} = empty.
```

The only other points of `V(I)_red \ (V(A) union V(B))` lie in
`U_0 subset S union D`, whose closure is disjoint from `Z_sf`. Therefore
`Z_sf intersect V(I*) = empty`, i.e. `E=empty` as a set of geometric
points. Combined with `(3.3)` this restores
`V(I*)_red intersect V(k10) = S union D`.

The same conclusion in components:

- Every irreducible component of `V(I)_red` whose generic point has
  `k10!=0` is contained in the closed square locus. Its special fibre
  at `k10=0` therefore has square `K`. Intersecting with `V(I)` and
  using `(1.2)` puts that special fibre in `S`. (Once `K` is square the
  load term `[K^(5/2)]_-` vanishes identically, so vanishing of the
  `q_ell` further forces `K | N^2` and the two linear relations of
  `S`; this N-refinement is not required to empty `E`, because a square
  limit is already excluded from `E` by definition.)
- Every irreducible component of `V(I)_red` contained in `k10=0` is a
  component of `V(I+(k10))_red = S union D union Z`. After deleting
  components supported wholly on `V(A)` or `V(B)`, only `S` and `D`
  remain. These are the vertical components of the special fibre. There
  is no further reduced vertical component, because there is no further
  reduced point of `V(I) intersect V(k10)`.
- An embedded primary, or a nonreduced thickening in the `k10`
  direction supported at a point of `Z_sf`, has radical containing `B`.
  Colon by `B^infinity` deletes that primary. Reduced support of
  saturation sees only `cl(V(I)_red \ V(B))` and cannot acquire a new
  closed point from nilpotents. A fattening along `k10` at a squarefree
  zero-normal point is in any case forbidden as a reduced `k10!=0`
  point by `(4.1)`, and as a purely infinitesimal thickening it is
  supported on `V(B)` and dies under the colon.

Thus `(4.1)` is a geometric-point support statement and is sufficient
for the reduced-support recovery the target claims. It is not sufficient
for reducedness of `I*`, for absence of embedded primes along `S` or
`D`, or for equality of nonreduced ideals. The target does not claim
those, and records that the two-prime minAss agreement is navigation
evidence for `(4.1)`, not a proof.

---

## Attack 7 — V1 is not silently promoted

**CONFIRMED.**

Retained from charged V1, with numbering as in the erratum:

- principal-part identity `(1.1)`, both signs positive, evaluation at
  `z0(w)`, unitriangular change of the first seven negative coefficients;
- exact `k10=0` criterion `(1.2)` (charged V1 `(2.1)`);
- the two parameterizations `(1.3)`, `(1.4)` (charged V1 `(3.3)`,
  `(3.5)`), covering `[2,1,1]` and `[3,1]`, with squarefree `K` forcing
  `N=0`;
- the equations of `S` solving every first-normal row for arbitrary
  `k10`.

The V1 displayed equality

```text
V(I*)_red intersect V(k10) = S union D
```

is explicitly withdrawn. Its exact unconditional replacements are
`(3.1)`--`(3.4)`. The only route back to the withdrawn equality is the
unproved Padé implication `(4.1)`.

Section 5 refuses, in a single list: `(4.1)` itself; equality of
nonreduced ideals; absence of embedded components; reducedness of `I*`;
a complete characteristic-zero radical; a strict arc; control of the
higher-contact zero section; the terminal `[6,2]` passport; either
Taylor boundary; exclusion of order two; closure of `(8,12)`; maximum
twelve; JC2. Dual-prime minAss is confined to navigation. No scheme-
theoretic identification of `I*` with `I(S union D)` or with the
four-dimensional square/load family appears.

The new open equality `(3.2)` is strictly weaker than the withdrawn
global claim and is what Attack 3 proves. It is not a promotion of V1
§4.

---

## Attacks that failed to break a numbered claim

Reading `A^infinity` as saturation by the product `p c r` (internally
inconsistent with `S` meeting `D(A)` densely, and with `c=0` on `S`).
Treating sequential colons by `A` and by `B` as saturation by the sum
`A+B` (that would retain components in `V(A)` not in `V(B)`, and
conversely). Claiming `I0*` can acquire `k10!=0` points (the generator
`k10` survives the colon). Claiming `Z` remains as reduced support of
`I0*` because its intersection with `S union D` is nonempty (that
intersection is the non-squarefree zero-normal boundary of retained
components; the complementary open `Z_sf` is deleted with `Z`). Claiming
`s=0` or `lambda=0` is deleted by saturation (those are points of
retained components). Claiming `(3.2)` requires the Padé lemma (limits
landing in `O` already have `N!=0` and are classified by `(1.2)`).
Producing a point of `E` with `N!=0` (the origin in `K` with `N!=0` is
`S` at `s=0`; every other `N!=0` slice point is in `O` or already named).
Reading `(3.4)` as an equality with `{K nonsquare}` (it is a containment;
the exact residual is the smaller squarefree locus, which the following
sentence records). Claiming a family of square `K` can specialize onto
`Z_sf` (`{K square}` is closed and disjoint from `{disc != 0}`). Claiming
an embedded or nonreduced primary supported on `Z_sf` survives in
`V(I*)_red` (its radical contains `B`; reduced support of saturation
does not see it). Importing two-prime minAss as a radical statement
(the target forbids this). Importing a strict arc, `[6,2]`, a Taylor
boundary, or order-two closure (none is used).

---

## Scope that remains open

Whether a nonsquare `K` with `k10!=0` can cancel the first seven
coefficients of `(1.1)`. Emptiness or nonemptiness of `E` in the absence
of `(4.1)`. The characteristic-zero radical of `I*`, its reducedness,
embedded primes, and nilpotent structure. The `Lambda,J`-saturated
divided-family boundary. Higher-contact jets, including the zero
section. Either Taylor family. The terminal `[6,2]` passport. Emptiness
or nonemptiness of a strict arc. Closure of order two, of `(8,12)`, of
maximum twelve, or of JC2.

CONFIRMED
