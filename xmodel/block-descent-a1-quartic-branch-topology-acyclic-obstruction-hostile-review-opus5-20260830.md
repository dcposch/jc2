# Hostile review: rank-four branch topology and the acyclic obstruction

Reviewer: Opus 5, independent co-researcher lane  
Date: 2026-08-30 UTC  
Target: `xmodel/block-descent-a1-quartic-branch-topology-acyclic-obstruction-sol56-20260830.md`  
Verdict: **CONFIRM_WITH_CORRECTIONS** — two refutations, one typed `GAP`, one
sharpening; the central obstruction survives and is strengthened.

## 0. Custody and reproduction

All ten charged hashes reproduce byte-exactly. The artifact's own seal
reproduces independently: body 18735 bytes through the unique standalone
`<!-- BODY-END -->`, body SHA-256
`3585d344b20ae2ac7a307d719d87746bd37e4c471a6a20b8e3b2e2e8db0cee48`, full
SHA-256 `768cf08f...05`, matching `.artifact.json`. The second textual
occurrence of the end marker is inline inside backticks in the seal and is not
standalone.

One custody remark. Section 1 of the artifact charges a sixth mathematical
input, `xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-obstruction-sol56-20260830.md`
at `5be2e2af...`, which is **not** in this review's charged list. I verified
only that the file exists with exactly that hash; I did not read it. The
charged
`...-cubic-acyclic-branch-monodromy-coordinator-integration-...` binds the same
packet and I used that instead.

No repository file other than the single output was written, and Git state was
not touched.

## 1. Item 1 — fibre partitions, the ramification-to-branch map, the quotient graph

**CONFIRMED.**

*Census.* The partitions of `4` with at least one part `>=2` are exactly
`(2,1,1)`, `(3,1)`, `(2,2)`, `(4)`; a local factor has length one iff `pi` is
etale there, so a generically unramified sheet is exactly a part equal to `1`.
The fixed-sheet theorem (charged Galois integration, item 2, in its
`sum_(e_i=1) f_i >= 1` residue-degree form) therefore kills `(2,2)` and `(4)`
generically. I checked the residue-degree bookkeeping exhaustively: with
`sum e_j f_j = 4` and some `e_j=1`, the only generic partitions are
`(2,1,1)` (from `[e=2,f=1]+[e=1,f=2]` or `[e=2,f=1]+2x[e=1,f=1]`) and `(3,1)`
(from `[e=3,f=1]+[e=1,f=1]`). No fifth generic type was overlooked. `S22` and
`S4` contain no generic point of `B`, hence are finite. `(2.2)` holds as a
constructible decomposition.

*Reduced preimage count.* `pi^-1(z) intersect R_red` is the set of local
factors of length `>=2`. That is `1`, `1`, `2`, `1` for the four rows. So the
map is point-bijective except for exactly two preimages at `(2,2)` points —
**confirmed, and the count is exact, not generic.** Consequently
`e_c(R_red)=e_c(B)+n22` follows from additivity plus the fact that a finite
bijective morphism of complex varieties is an analytic homeomorphism. `(3.2)`
is right.

*Contractibility of `R_red` components.* Correct, but the artifact's phrase
"affine incidence multigraph ... with self-branches and parallel branches
retained" needs the right reading, and I record it because a wrong reading
would silently over-prove. The promoted forest theorem is about the **dual
multigraph of a strict-SNC boundary `D` of a completion of `V=g1(A2)`**, with
one vertex per component and one edge per intersection point of the *resolved*
boundary. Its actual consequences for `R_red subset Y` are:

```text
(a) no two components of R_red meet in two or more distinct points;
(b) no component of R_red has a point with two or more local branches;
(c) no cycle in the component/point incidence structure.
```

It does **not** forbid three or more components of `R_red` meeting at a single
common point: blowing that point up separates them onto one exceptional curve
and yields a star, which is a tree. It also does not forbid unibranch
(cuspidal) singularities, again because their resolution is a chain. Under
(a)-(c), each `R_i` is unibranch everywhere, so `R_i` is homeomorphic to the
normalization of `R_i`; if that is `A1` then each connected component of
`R_red` is a tree of contractible pieces glued at single points, hence
contractible, and `(3.1)` `e_c(R_red)=b0(R_red)=h` holds.

This matters immediately downstream: in Section 6 the weighted cone has all
`m` components of `B`, hence all `m` components of `R_red`, concurrent at the
single point over the vertex. Under the naive "one edge per unordered pair"
reading, `m>=3` would already be a forest violation and Section 6 would be
partly vacuous. The artifact does not make that error, and no consumer may.

*Quotient-graph homotopy.* Correct. `R_red -> B` is finite surjective, hence a
topological quotient map; its classes are singletons except `n22` disjoint
pairs, and the `2*n22` identified points are pairwise distinct across
different `S22` values. For CW pairs, `X/(x~y) ~= X cup_{x,y} I`, so iterating
gives `Gamma` with `h` vertices and `n22` edges, loops included when both
points lie in one component. Hence `e(B)=h-n22`, `b1(B)=beta=n22-h+k`, and for
connected `B`, acyclicity iff `n22=h-1`, a cycle iff `n22>=h`. Since `B` is
homotopy equivalent to a graph, "acyclic", "simply connected" and
"contractible" coincide for it, which is what the Arzhantsev--Zaidenberg input
requires.

*Ledger check.* I reran the `(3.2)`/`(3.3)`/`(4.1)`/`(0.3)` identities on my
own sweep of 22,848 rows (`h<=7`, `|e(T31)|<=8`, `n4<=5`), building `e(U)`
from the strata rather than from the producer's closed form. All identities
hold, including the exact rearrangement

```text
e(T211) = e(C) + Q - 4 + 3 e(B) + n22 + n4,                      (R.1)
```

which I use below and which the artifact does not record.

## 2. Item 2 — the constructible Euler ledger

**CONFIRMED**, with one dependency flagged in Section 8 below.

`u(z)` is `4, 2, 1, 0, 0` off `B` and on the four rows. Refining strata so the
finite map is a covering on each piece, `e_c` multiplies by the degree, and

```text
e_c(U) = 4(1-e(B)) + 2 e_c(T211) + e_c(T31)
       = 4 - 2 e(B) - e(T31) - 2(n22+n4),
```

which is `(4.1)`. Substituting `e(B)=h-n22` cancels `n22` exactly and gives
`(0.3)`. Both ruling equations `(0.4)` follow from the charged
`e(U)=e(C)+sum_t(q_t-1)`, `e(C)=1` or `2`, `Q>=0`.

The artifact is correct and explicit that `e(T31)` is a *signed* constructible
Euler number and that `(0.4)` alone is not a positivity argument. That is the
right posture and matches the charged Euler-ledger packet's own warning that
`D2` has no sign. I found no place where positivity of `e(T31)` is smuggled
in. The whole ledger reproduces the Section 6.1 control exactly: there
`h=1, n22=0, n4=1, e(T31)=0`, giving `e(U)=4-2-0-2=0`, matching the
independent computation `U ~= A1 x Gm`.

One scope note: `(0.3)` and `(0.4)` are the `h`-form and inherit the
polynomial-parametrization dependency of Section 8. The `e(B)`-form `(4.1)` is
unconditional.

## 3. Item 3 — the connected-acyclic obstruction

**CONFIRMED**, including the Cohen--Macaulay inequality, its direction, and
the control.

*Classification input.* I read Theorem 1.3(b) directly from the charged PDF
(page 3, printed lines 124--135). It reads exactly as the artifact's `(5.1)`,
with `eps_x, eps_y in {0,1}`, `p` with simple roots, `a,b >= 1`,
`gcd(a,b)=1`, `r>0`, `kappa_i` pairwise distinct. AZ define acyclic as
`pi0=pi1=1`. So `a,b>=1` and `gcd(a,b)=1` are charged, which is what makes
each `y^a - kappa_i x^b` irreducible, smooth away from the origin, and passing
through the origin; and the components meet only at the origin.

*Comb family (I).* The horizontal meridian generates the central `Z` factor of
`pi1((C - roots(p)) x C*) = F_d x Z`; its image is a transposition or a
three-cycle, so the whole image lies in a centralizer of order `4` or `3`,
both intransitive. I checked the degenerations the artifact compresses into
one clause: `eps_y=0` with `d>=2` is disconnected and excluded by hypothesis;
`eps_y=0, d=1` and `eps_y=1, d=0` give `pi1=Z` and a cyclic intransitive
image. Complete.

*Cone family (II).* Positive weighted radial flow identifies the global
complement group with the origin-local one. The artifact states this in a
single line; the charged cubic integration states the same step through
*punctured weighted sublevel neighborhoods* and cofinality with Euclidean
balls, a qualification a prior review found necessary. The quartic artifact
drops that qualification. It is the same promoted argument, so this is a
presentation regression, not a mathematical gap.

Then, because `Y` is normal, the points of a fibre correspond to the *orbits*
of the local group (each analytic local component is normal and connected, and
stays connected after deleting the branch preimage), so a fibre with any part
`<4` forces an invariant proper subset and intransitivity. Hence `(5.2)`: the
vertex fibre is `(4)`. The remark that two rank-two factors do not help,
because their idempotents live over the henselian base, is correct.

*The Cohen--Macaulay inequality `(6.1)`.* Reconstructed and **confirmed**.
`C=O_(Y,y)` is free over the regular 2-dimensional `O_(A2,z)`, hence CM of
dimension two and a domain; `p` is a nonzerodivisor, so `C/pC` is CM of
dimension one and `q` is a parameter for it. For a one-dimensional CM local
ring, `length((C/pC)/q) = e(q; C/pC)`, and the associativity formula gives

```text
e(q; C/pC) = sum_P length((C/pC)_P) * e(q; (C/pC)/P) >= e_i * 1,
```

taking `P` the minimal prime of `E_i`, where `length((C/pC)_P) = ord_(E_i)(p)
= e_i` and all other terms are nonnegative. Smoothness of `B_i` at `z` is
genuinely needed so that `(p,q)` are *regular parameters* and
`length_C C/(p,q) = length_C C/m_z C` is the local factor rank; on
`B_i - {0}` that holds because the cone components are smooth off the vertex
and pairwise disjoint there. **Direction:** larger local length at the ramified
point leaves fewer length-one factors, so `u(z) <= 4 - e_i = u_i`. Correct.

I also verified independently that the same bound holds at *every* point of
`B_i`, smooth or not, by the normal-cover orbit argument: `D_z` contains a
conjugate of the generic meridian, of cycle type `(e_i, 1^(4-e_i))`, so
`Fix(D_z) subset Fix(sigma)` has at most `4-e_i` elements. The artifact does
not need this, but it is the robust form and I use it in Section 6 below.

*Aggregation `(6.3)`--`(6.4)`.* `e(C* - P_i) = -|P_i|`, so the contribution of
`B_i - {0}` is `sum_(P_i)(u(z)-u_i) <= 0`; `e_c(B)=1` gives `e_c(A2-B)=0`; and
`u(0)=0`. Hence `e_c(U) <= 0`, contradicting `e(U)=e(C)+Q >= 1`. Confirmed.

*Control `w^4+a*w+b`.* Independently recomputed in sympy. `disc_w = 256b^3 -
27a^4`; the ramification is `a=-4w^3`, `b=3w^4`; on `(a,b)=(-4t^3,3t^4)` the
fibre factors as `(w-t)^2 (w^2+2tw+3t^2)` with cofactor discriminant `-8t^2`
and cofactor value `6t^2` at `w=t`, so the partition is `(2,1,1)` for `t != 0`
and `(4)` at the origin. The resolvent cubic is `z^3 - 4bz - a^2`, and solving
it for `b` exhibits `C(a,b)[z]/(res) = C(a,z)`, a field, so the resolvent is
irreducible and `3 | |G|`; `256b^3-27a^4` is squarefree, hence not a square,
so `G = S4`. Finally `U = {a+4w^3 != 0} ~= A1_w x Gm`, `e(U)=0`. The control
is exactly as claimed, saturates `(6.4)`, and correctly is not a block.

The load-bearing remark that a generic `(3,1)` specializing to a special
`(2,1,1)` would be the only positive correction on a punctured cone component
is right, and `(6.1)` is exactly what forbids it.

## 4. Item 4 — forcing global monodromy `S4`

**CONFIRM_WITH_CORRECTIONS.**

*Normal generation.* `A2` simply connected makes meridians normally generate
`pi1(A2-B)`, so the inertia images normally generate `G`. Because the set of
elements of a fixed cycle type inside `G` is closed under `G`-conjugation, the
subgroup they *generate* already equals their normal closure — so the
producer's replay shortcut is legitimate, and taking *all* transpositions and
three-cycles of `G` is the correct a-fortiori direction.

*Recomputed independently* (my own permutation code, dict-free, different
composition convention): transitive subgroup orders `[4,8,12,24]` with four
transitive order-four subgroups (three `C4`, one `V4`, all regular) and three
`D4`. Fixed-inertia ledger: order 4 gives 0 elements and closure order 1;
`D4` gives 2 transpositions, closure order 4, intransitive; `A4` gives 8
three-cycles, closure `A4`; `S4` gives 14, closure `S4`. Centralizers of a
transposition and a three-cycle have orders `4` and `3` and orbit types
`(2,2)` and `(3,1)`, both intransitive. `A4 intersect (S2 x S2) = {1,(12)(34)}`
with no three-cycle. Every finite claim in Sections 5 and 7 reproduces.

*`C4`/`V4`/`D4`.* Confirmed and unconditional.

*`A4`.* The argument is valid but **not unconditional**: it needs
`e(B)=h`, hence the polynomial-parametrization input of Section 8. Given that
input, `n22=0`, all components are contractible, `h=1` falls to the acyclic
theorem, and for `h>=2`, `T31=B-S4` gives `e(U)=4-3h-n4<=-2`. I verified the
substitution: `e(T31)=e(B)-n4=h-n4`, so `e(U)=4-2h-(h-n4)-2n4=4-3h-n4`.
Without that input only `e(B)<=h` is available, `3e(B)+n4<=3` no longer forces
`h=1`, and the `A4` row survives. Flagged, not refuted.

*Overlooked inertia types.* I looked for them and found none at the divisorial
level. At isolated points I found a **sharpening the artifact misses**: for a
plane-curve germ the local complement group is *generated* (not merely
normally generated) by the meridians of its branches, so for every `z in B`

```text
D_z = < all elements of D_z of cycle type (2,1,1) or (3,1) >.     (R.2)
```

`D4` fails `(R.2)` (its two transpositions generate an order-four subgroup).
Consequences are recorded in Item 5.

The final paragraph of Section 7 — a `(3,1)`-generic component cannot pass
through an `S22` point, since a three-cycle is not in `S2 x S2` — is correct
and I use it below.

## 5. Item 5 — the normalized cubic resolvent

**CONFIRM_WITH_CORRECTIONS.** One row of table `(8.5)` is empty.

*Construction.* Correct. `L^{D4}` has degree three; `Z` is the normalization
of `A2` in it, integral and normal; two-dimensional normal local rings are CM
by Serre `S2`, and a finite CM module over a regular local ring of the same
dimension is free by Auslander--Buchsbaum, so `Z -> A2` is finite flat.
Connected because the field is a field. Correct.

*Branch support.* I recomputed `phi: S4 -> S3` on the three pairings from
scratch: it is onto with kernel the normal `V4` (order 4), a transposition maps
to a transposition, a three-cycle to a three-cycle. So every component of `B`
is in the branch of `Z`, and `Z` is etale over `A2-B`, giving equality of
reduced branch support. Confirmed.

*Fibre table.* Recomputed as orbit types of `phi(D_z)` on the three pairings,
which is legitimate because `Z` is normal:

```text
(2,1,1)   C2 = <(12)>          -> (2,1)      CONFIRMED
(3,1)     C3                   -> (3)        CONFIRMED
(3,1)     S3                   -> (3)        CONFIRMED
(2,2)     full S2 x S2         -> (2,1)      CONFIRMED
(2,2)     diagonal <(12)(34)>  -> (1,1,1)    (the excluded alternative)
(4)       D4                   -> (2,1)      REFUTED: row is empty
(4)       A4                   -> (3)        CONFIRMED
(4)       S4                   -> (3)        CONFIRMED
```

*The `(2,2)` row is correct and its justification is load-bearing.* The
diagonal really would give a totally split, unramified cubic fibre, so this is
not a cosmetic distinction. The exclusion is valid: the fibre being `(2,2)`
forces the orbits of `D_z` to be `{1,2},{3,4}`, so `D_z subset S2 x S2`; by
Section 7 every branch through an `S22` point is transposition-generic, so
`D_z` contains a transposition, say `(12)`; having orbit `{3,4}` then forces
`(34) in D_z`; hence `D_z = S2 x S2`, the full pair group, not only its
diagonal. Confirmed exactly as claimed.

*The `(4)` row is over-generous.* The artifact says "transitivity and the
presence of allowed divisorial inertia leave `D4`, `A4`, or `S4`". By `(R.2)`,
`D_z` must be generated by its own transpositions and three-cycles. `D4` is
not. Therefore at every `(4)` point `D_z in {A4, S4}` and the cubic-resolvent
fibre is always `(3)`. The `D4` row of `(8.5)` is empty and the `(2,1)`
column entry for `(4)` must be deleted. This *strengthens* the artifact's own
conclusion: the resolvent has no unramified sheet over any `T31` component
**or** any `(4)` point, so it is even further from satisfying a cubic
fixed-sheet hypothesis.

*Methodological warning.* The artifact's instruction to use the local
decomposition group rather than the roots of a possibly nonnormal classical
resolvent polynomial is correct and I followed it; I did not read fibre types
off `z^3 - 4bz - a^2` anywhere except for the *generic* Galois-group
computation in the control, where irreducibility over the function field is all
that is used.

*Applicability of the cubic theorem.* The artifact's conclusion — no live horn
falls to it — is right, but its stated reason is incomplete. The promoted
cubic result is a **block** theorem ("no strict intermediate field with
`[K:C(f,g)]=3`"); `Z` is not a block, since its field need not embed in
`C(x,y)` and there is no etale `A2 -> Z`. So the promoted theorem cannot apply
to `Z` at all, for a reason prior to branch topology. What *could* apply is the
cover-side acyclic-branch monodromy lemma inside that packet, and it is blocked
by `beta>=1` and, after the correction above, by the `(3)` fibres.

## 6. Item 6 — surviving horns, and a refutation of one of them

**REFUTED IN PART.** The dichotomy `(0.5)` is not tight, and the artifact's own
proposed disconnected successor is already dead on a charged page.

AZ Corollary 1.2 sits immediately above the charged Theorem 1.3 (page 3,
printed line 118): *any disconnected, simply connected, reduced plane curve is
equivalent to a union of `r >= 2` parallel lines.* Combine it with the
artifact's own Section 6 lemma:

> **Refutation of the disconnected-acyclic row.** Suppose `B` is disconnected
> with `beta = 0`. Then every connected component of `B` is contractible, so
> `B` is reduced, disconnected and simply connected; by AZ Corollary 1.2,
> `B` is a union of `r = k >= 2` pairwise disjoint lines. Every point of `B` is
> a smooth point on exactly one line, so `(6.1)`--`(6.2)` apply verbatim at
> every `z in L_j`, giving `u(z) <= u_j = 4 - e_j <= 2`. Therefore
>
> ```text
> e_c(U) = 4 e_c(A2-B) + sum_j [ u_j e_c(L_j) + sum_(z in P_j)(u(z)-u_j) ]
>       <= 4(1-r) + sum_j u_j  <=  4 - 4r + 2r  =  4 - 2r  <=  0,
> ```
>
> contradicting `e(U) = e(C) + Q >= 1`. Hence `beta >= 1` in the disconnected
> horn too.

I confirmed this by exhaustive sweep over `2 <= r <= 6`, all `2^r` assignments
of generic type, and all special-point patterns: the maximum attainable
`e(U)` is `0`, at `r=2`. I also confirmed it against the exact ledger: for two
parallel lines `h=k=2`, `n22=0`, `e(B)=2`, so `e(U) = -e(T31) - 2 n4`, and
enumerating the three type assignments gives `e(U) <= 0` in every case.

Consequently the corrected threat dichotomy is a single condition:

```text
b1(B) >= 1,   equivalently  n22 >= h - k + 1 >= 1,
in both the connected and the disconnected horn.                  (R.3)
```

In particular **every rank-four survivor has at least one `(2,2)` fibre**, and
by Section 7 every branch through it is transposition-generic. This is
strictly stronger than `(0.5)`, and it costs one corollary on the same printed
page as the classification the artifact already charges.

The consequence for the artifact's successor plan is concrete. Section 8's last
sentence proposes to test "the minimal disconnected row [with] two acyclic
components". That row is `k=2, beta=0`, which is exactly what `(R.3)` refutes.
It must not be launched.

*Does any live horn fall to the promoted cubic theorem?* No, and after
Item 5 the answer is more robust than the artifact states: the promoted cubic
theorem is a block theorem inapplicable to `Z`, and the cover-side lemma needs
an acyclic branch, which `(R.3)` forbids.

*A further Chau-conditional constraint.* Aggregating the same lemma globally
gives an identity I did not find in the artifact. Writing `Sigma` for a finite
set containing `Sing(B) u S22 u S4` and all points where `u` differs from its
generic value, and `N(z) = sum` of `u_i` over the local branches at `z`,

```text
e_c(U) = 4 - 4 e(B) + sum_j u_j + sum_(z in Sigma) [ u(z) - N(z) ],
every bracket <= 0.                                              (R.4)
```

`(R.4)` reproduces `e(U)=0` for the Section 6.1 control and `e_c(U)<=0` for the
whole weighted cone. Since every `(2,2)` point has at least two branches, all
transposition-generic, its bracket is at most `-4`, and using
`n22 = beta + h - k`, `e(B) = k - beta`, one gets `2m >= 4h - 3`, i.e.

```text
m >= 2h - 1,     m = #components of B = #components of R_red.    (R.5)
```

`(R.5)` is vacuous at `h=1` and so does not decide the minimal row, but it is a
free constraint on every `h>=2` survivor.

*Cheapest useful successor.* The artifact's `(8.2)` minimal row
`h=k=1, beta=n22=1, n4=0` is the right target and survives all of the above.
Its exact ledger is tight: `e(B)=0`, so by `(R.1)`
`e(T211) = e(C)+Q-3` and `e(T31) = 2 - e(C) - Q`, i.e. `e(T31)=1-Q` on the
`A1` base and `-Q` on the `P1` base. This is arithmetic, not a contradiction,
so the row genuinely needs geometry — the artifact's assessment is right.

Two corrections to the plan. First, the nodal curve `(8.3)` is a **control**,
not a decisive test: `y^2=x^2(x+1)` parametrized by `x=t^2-1, y=t(t^2-1)`
does have `b1=1` with the node identifying `t=+-1` (verified), but deciding one
curve decides one curve. Its projective closure is moreover tangent to the line
at infinity to order three, so Deligne--Fulton nodal-abelianness does **not**
apply and the complement group must actually be computed by
Zariski--van Kampen, which is not desk-cheap. Second, and cheaper: the decisive
invariant is the branch first Betti number itself. Used through AZ Corollary
1.2 it settles the entire `beta=0` stratum at desk cost, as above. Beyond
`beta=0` I did **not** find an invariant cheaper than the artifact's; the
honest next question is the classification-flavoured one,

> does there exist a reduced plane curve with `b1 = 1`, all components
> polynomial curves glued in a forest plus exactly one extra identification,
> carrying an `S4` cover with all divisorial inertia of the two allowed types,
> the pair-preserving local group `S2 x S2` at the identification point, and
> local groups obeying `(R.2)` everywhere?

The sharpened table of Item 5 is the right tool for it, and `(R.2)` is a free
extra filter at every special point.

## 7. Item 7 — replay

**CONFIRMED.**

Ordinary, `-O` and `-OO` runs all print the identical payload with
`payload_sha256 = f5cebda8549f140000fba45d3e569b524a7a82667a8c683d96d6c1c2bc7c6081`,
matching the artifact. The mutation `--mutate-allow-cone-rank-drop` is rejected
in **all three** modes with
`RuntimeError: specialization cannot lower the local ramified factor rank`.
The script contains zero Python AST `Assert` nodes — `require()` raises
explicitly — so it does not fail open under `-O`, which is the trap that has
bitten this campaign before. `ledger_rows_checked = 9555` reproduces as
`(sum_{h=1..6} 7h) x 13 x 5 = 147 x 65`. `cone_defect_fixture = -4`
reproduces as `0-1-2+0-1` over the five fixture rows.

Separation of software from mathematics, checked line by line:

```text
software-verified: S4 cycle-type censuses; centralizer orders and
  intransitivity; local-factor subgroup orders and intransitivity; the
  transitive-subgroup order list and regularity of the order-four rows; the
  fixed-inertia closure ledger per group order; A4 & S2xS2; the graph/Euler
  identities on a bounded box; the cone-defect fixture and its mutation.

NOT encoded, and correctly disclaimed: the polynomial-parametrization input,
  the forest theorem, the CM/parameter-multiplicity inequality, the AZ
  classification, weighted radial equivalence, cubic-resolvent normalization,
  and the existence of any cover.
```

Two replay observations the artifact does not make. First,
`"acyclic_positive_euler_survives": False` is a **producer-authored literal**
in the payload dictionary; nothing in the script computes it, so it carries no
evidential weight and must not be cited as a check. Second, the entire
Section 8.1 resolvent table has **zero replay coverage** — the script never
constructs `phi: S4 -> S3` — which is exactly where I found the empty `D4`
row. I recomputed that table independently.

## 8. Typed `GAP`: the polynomial-parametrization input

**GAP (citation/promotion), not a mathematical refutation.**

Section 3 asserts: "Each irreducible component `B_i` is an irreducible
component of the Keller nonproper-value curve, so Chau's polynomial-
parametrization theorem makes its normalization `A1`." The first half is fine:
`g2(R) = V(Disc) subset A(F)` is charged, and `A(F)` is a pure one-dimensional
hypersurface, so an irreducible curve inside it is a component of it. The
second half is the problem:

1. No source is charged. There is no reference, no theorem number, no page, and
   no PDF in the charged list. The artifact gives only an author surname.
2. The charged structure integration, section 3 item 5, states explicitly:
   "The stronger wording that discriminant components are polynomially
   parametrized components of `A(F)` is citation-dependent and unnecessary for
   the structural result. Only the proved inclusion
   `g2(R)=V(Disc(g2)) subset A(F)` is promoted here." So the exact decoration
   being consumed was deliberately withheld at the point where it was first
   raised.
3. The charged Euler-ledger packet, section 7 item 3, anticipates this import
   and conditions it: "If external nonproperness-curve theorems are imported
   later, apply them separately to `B subset A(F)` and to the first-leg image
   residue." The artifact imports it once and does not record the condition.
4. The charged cubic integration obtains the same fact (`(2.3)`, "every
   component normalization is `A1`") from a *different*, separately reviewed
   packet, `block-descent-a1-cubic-one-place-euler-obstruction-...`, which is
   cubic-scoped and is not charged here.

I want to be precise about what is and is not at stake. The underlying fact is
very likely true and standard — `C`-uniruledness of the non-properness set of a
dominant polynomial map forces each planar component to be a polynomial curve,
whose normalization is then `A1` because a smooth affine curve dominated by
`A1` has only constant units and one place at infinity. I reconstructed that
last implication. What I cannot do in this lane is verify an uncharged
attribution, and the campaign's own coordinator explicitly declined to promote
it. Note also that the charged forest theorem supplies only that boundary
components are **rational**; rationality gives `P1` minus `s_i` points and
`e_c(R_i)=2-s_i`, so without a one-place input one gets only
`e_c(R_red) <= h`, hence `e(B) <= h - n22` — an inequality in the wrong
direction for the `A4` row.

Exact blast radius, which I checked item by item:

```text
INDEPENDENT of the input (unconditional):
  the fibre census (2.1)/(2.2) and the S22 double-preimage count;
  e_c(R_red)=e_c(B)+n22;
  the strata identity (4.1);
  the entire quartic acyclic obstruction of Sections 5-6 and its control;
  my refutation of the disconnected-acyclic row in Item 6;
  the C4, V4 and D4 exclusions in Section 7;
  the whole cubic-resolvent construction and the corrected table (8.5).

CONDITIONAL on it:
  e(B)=h-n22 and hence (0.2), (0.3), (0.4);
  the quotient-graph reading of beta and the statement "beta>=1 iff n22>=h";
  the A4 exclusion, hence the unqualified claim (7.3) that the monodromy is S4;
  (R.3)'s translation into n22, and (R.5).
```

The repair is cheap and should be done before any consumer: charge the source
with a theorem number, or re-derive the one-place property for `B subset A(F)`
inside the block sandwich, and restate `(7.3)` with its dependency visible.

## 9. Maximum-safe theorem

Everything below is unconditional given the charged promoted inputs, and does
**not** use the Section 8 gap.

> **Quartic simply-connected-branch obstruction (strengthened).** Let
> `pi: Y -> A2_C` be finite flat of degree four with `Y` integral and normal,
> `R = NonEt_Y(pi)`, `U = Y - R`, `B = pi(R)_red`. Assume every irreducible
> component of `B` has a generically unramified sheet. If **every connected
> component of `B` is simply connected** — `B` need not be connected — then
>
> ```text
> e_c(U) <= 0.
> ```
>
> Consequently no such cover is an actual proper block of rank four, since the
> promoted `A1`-ruling gives `e_c(U) = e(C) + Q >= 1`.
>
> *Proof.* Connected case: the artifact's Sections 5--6, verified above.
> Disconnected case: AZ Corollary 1.2 makes `B` a union of `r >= 2` parallel
> lines, and the Section 6 specialization lemma gives
> `e_c(U) <= 4 - 4r + 2r <= 0`.

> **Corrected rank-four threat row.** For an actual proper block of rank four,
> the reduced branch satisfies `b1(B) >= 1`; there is at least one `(2,2)`
> fibre; every branch component through a `(2,2)` point is
> transposition-generic and the local group there is the full pair group
> `S2 x S2`; the monodromy is not `C4`, `V4` or `D4`; at every `(4)` point the
> local group is `A4` or `S4`; and the normalized cubic resolvent
> `Z -> A2` is a connected finite-flat normal cubic with the same reduced
> branch `B` and fibre table
> `(2,1,1),(2,2) -> (2,1)` and `(3,1),(4) -> (3)`.

With the Section 8 input repaired, add: the monodromy is `S4`, the ruling
equations `(0.4)` hold as stated, and `n22 >= h - k + 1` with `m >= 2h - 1`.

## 10. Firewalls

This review asserts no exit price and emits no `charge_basis` line; receipt
status `ABSENT` is expected. Nothing here constructs a Keller map, proves a
rank-four proper block exists or does not exist, touches the primitive /
no-proper-block horn, or bears on JC2. The rank-four block remains **open**,
now on the single row `b1(B) >= 1`. No heavy local CAS was run; the only
computations were desk-scale permutation enumeration, one sympy discriminant
and factorization, and integer ledger sweeps. `jc2-lean` was not inspected,
listed, searched, built, modified or controlled, and no sibling external-model
prompt, log, report or receipt was read.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `30310`.
- Body SHA-256:
  `998f9f3b4fccb32e03fd9e24dba13425e9cf2e8ad5e130323247fe7d9f9d0692`.
- Frozen basis: `85f0be854c5f46e863d7784a9d677a35873c36b9`.
