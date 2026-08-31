# Reducible rank-four branch component-tree ledger

Date: 2026-08-31 UTC
Lane: bounded primary research; not a review and not a promotion
Git HEAD: `a48c3e27da15508dfda8d405f7f3abe7dc49e05f`
Packet bases: genus-three combined hostile packet precursor `86ca482f...`; genus-four cable-b1 hostile packet coordinator basis `59f25428`; rank-four `S4` integration `5d7df7ce0ad3548e88fd23734917212d6b3fbd3ada4cab81514b12bb76ea64de`
Scope: actual rank-four proper block of a hypothetical complex plane Keller map; reduced target branch `B` with at least two irreducible components

This report asserts no new exit price. Genus-ladder conductor exclusions and the one-cusp Poisson narrowing are not used as killing theorems; where a sentence mentions them it is labelled `PROVISIONAL` and a variant without them is kept.

## 0. What is consumed

Promoted constraints, from the 2026-08-30/31 `AUDIT.md` current-state block, `notes.md` LIVE STATE `2026-08-31 06:55Z`, and the charged `S4` integration `5d7df7ce...`:

- Every actual rank-four proper block has monodromy `G=S4`, `b1(B)>=1`, at least one `(2,2)` fibre, `n22>=h-k+1`, and `m>=2h-1`, with `h=b0(R_red)`, `k=b0(B)`, `m=#Irr(B)`, `n22=|S22|`.
- Every irreducible component of `B` is an irreducible component of the nonproper-value curve `A_F` and has `normalization = A1` (Chau Theorem 1, as bound in `5d7df7ce...` §2). Equivalently, each component has geometric genus zero and exactly one analytic place at infinity.
- The whole curve `A_F` has one set-theoretic point at infinity (Chau 2004, Corollary 2). Every component of `B` therefore passes through that same infinite point; the link at infinity of a reducible `B` is an `m`-component algebraic link, not a knot. This is why the irreducible one-place census does not transfer through the normalization-fibre formula `g(K_infinity)=Delta_aff`.
- Source incidence of `R_red` is a forest (morphic rational-forest theorem). Self-nodes and two distinct intersections between the same pair of components are forbidden on `R`. Stars (several components through one point) are allowed. The finite map `R_red -> B` is point-bijective except that each `(2,2)` fibre identifies one pair of source points, and `e(B)=h-n22`, `b1(B)=n22-h+k`.
- Some connected component of `B` has nontrivial `pi1` (all-degree acyclic-companion theorem, integration `9579d3a1...`).
- Divisorial inertia is a transposition or a three-cycle. Every `(2,2)` pairing in the connected cyclic horn is supported only on `(2,1,1)`-generic components (`5d7df7ce...` §5 and the acyclic-obstruction producer §7). A `(3,1)`-generic meridian cannot lie in the pair-preserving local group at an `S22` point.
- The exact rank-four Euler/ruling ledger (`768cf08f...` (0.3)--(0.4), bound by `5d7df7ce...`):

```text
e(U)=4-2h-e(T31)-2n4 = e(C)+Q,     Q>=0,   C in {A1,P1},
C=A1:  2h + e(T31) + 2n4 + Q = 3,
C=P1:  2h + e(T31) + 2n4 + Q = 2.
```

The one-node meridional obstruction (producer `c61f0ceb...`, Opus review `CONFIRM_W_CORR`) is used only in its stated scope: irreducible one-place `A1`-normalized curve, sole affine singularity an ordinary two-branch node, generic meridians transpositions, connected simple cover of degree `d>=4`. AUDIT still lists the producer as review-gated in the 2026-08-30 23:06Z block; LIVE STATE 2026-08-31 06:55Z does not repeat a promotion. Rows killed only by this theorem are marked `ONE-NODE` and a variant without it is kept.

Not used as killing theorems: the genus-three complete row (`2f28d30f...`) and the genus-four `b1=1` row (`0ffb6f82...`) both require reduced irreducible `B`. The genus-ladder conductor list and one-cusp Poisson narrowing are `PROVISIONAL`.

Orevkov's degree-at-infinity formula is the published identity (Orevkov 1987 Lemma 4.2; Chau 1999 Remark 4.9)

```text
deg_geo(F)-1 = sum_{l subset L_F} [ mu_l + sum_{u in l} (deg_u F* - mu_l) ],
```

with every displayed correction nonnegative. Dicritical images cover `A_F` (Chau 2004 Lemma 1). Nodes obtained by identifying two distinct immersed parameter values are budget-free (Chau Lemma 4.3, as used in `5d7df7ce...` clients). Unibranch critical parametrization values are not.

## 1. Combinatorial type

Write `B = union_{i=1}^m B_i` reduced, `m>=2`, each `B_i` irreducible. Let `R_i` be the unique irreducible component of `R_red` dominating `B_i`; the generic fibre partitions `(2,1,1)` and `(3,1)` have a single ramification point, so `R_i -> B_i` is birational and `normalization(R_i)=A1` (`5d7df7ce...` §2). Thus `#Irr(R)=#Irr(B)=m`.

Per component `B_i` the exact type is the tuple

```text
(g_i, pinf_i, paff_i, inertia_i, rho_i, Delta_i^unibranch, Delta_i^node)
```

with the following forced values.

- `g_i=0`: normalization genus, Chau Theorem 1.
- `pinf_i=1`: one analytic place at infinity, same theorem. All `m` infinite places occupy the single set-theoretic infinite point of `A_F`.
- `paff_i`: number of finite normalization places lying over affine singularities of the reduced curve `B` (self-singularities of `B_i`, intersection points with other components, and `(2,2)` identifications incident to `R_i`). This is a nonnegative integer, at least the number of incident forest edges.
- `inertia_i in {T211, T31}`: generic fibre partition, equivalently generic meridional image a transposition or a three-cycle in `S4`. Write `m211` and `m31` for the corresponding component counts, `m=m211+m31`.
- `rho_i`: conjugacy class of that generic meridian in `S4`. Transpositions have three conjugacy-class-as-transpositions-up-to-global-conjugacy types once a `(2,2)` pairing `12|34` is fixed: equal to one of the two pairing transpositions, or overlapping (moving one letter from `{1,2}` and one from `{3,4}`). Three-cycles are even and cannot be the generic inertia of a component that carries an `S22` point.
- Affine singularity budget: unibranch singularities of `B_i` (cusps and higher `A_{2p}`) are critical values of the polynomial parametrization `A1 -> B_i` and charge a positive Orevkov correction. Ordinary two-branch nodes coming from `(2,2)` identifications, and transverse intersections of distinct components already present in the source forest, do not.

The incidence tree of `R` is the affine incidence multigraph of `5d7df7ce...` §3: vertices are the `m` normalization components together with the finite set `Sigma` of intrinsic affine points at which the normalization of `R` has at least two preimages; one edge per local branch. This graph is a forest with `h` connected components. Parallel edges (a self-node of `R`) are forbidden.

The target `B` is that forest after `n22` two-point identifications. Identifications may join points on one component (a self-node of that component in `B`, absent from `R`) or on different components (an extra target connection, possibly merging source components). They cannot lie on a `T31`-generic component.

## 2. Finite bound

The Euler identity does not bound `m` or `n22`. The `(2,2)` count cancels from `e(U)` (`768cf08f...` (0.3)), and the estimate `e(U)<=4-4h+2m` of `5d7df7ce...` (6.2) is only a lower bound `m>=2h-1`. Finiteness of the *incidence-tree* ledger at canonical geometric degree four is the content of Lemmas 2.1--2.3. Finiteness of embedded curves is not claimed: `n22` is Orevkov-budget-free.

**Lemma 2.1 (Euler packet).** For an actual rank-four proper block, the tuple `(C,h,e(T31),n4,Q)` is one of the following, up to replacing a one-dimensional `T31` locus by its signed Euler number.

1. `T31` is finite. Then `e(T31)=t>=0` and `h=1`. The solutions are exactly the three threat-map rows of `cf157e17...` (0.1):

```text
(E1) C=A1, Q=0, n4=0, t=1,
(E2) C=A1, Q=1, n4=0, t=0,
(E3) C=P1, Q=0, n4=0, t=0.
```

No row with `t>=2` or `n4>=1` occurs. Connected `R` forces connected `B`, so `k=1` and `n22=b1(B)>=1`.

2. `T31` is one-dimensional, i.e. `m31>=1`. Then `h>=2` is possible. The `(3,1)` components carry no `S22` point, so their incidence graph is a subforest of `R` and `e(B_31)=h31`. Removing the finite special set of cardinality `sigma` (S4 points on `B_31` and mixed `T31`--`T211` intersections) gives `e(T31)=h31-sigma`. The forest has at most `m-h` mixed intersection points, hence `sigma <= n4+(m-h)` and

```text
2h + e(T31) + 2n4 + Q  >=  3h + h31 - m + n4 + Q.
```

The left side is 2 or 3, so `3h-m <= 3`. Together with `m>=2h-1` this does not bound `m`. It does bound `h` once `m` is bounded: `h <= (m+3)/3`.

*Proof.* Finite `T31` and `n4,Q>=0` force `2h<=3` in the `C=A1` equation and `2h<=2` in the `C=P1` equation. The three displayed rows are the nonnegative integer solutions at `h=1`. Identifications of a connected space remain connected, so `h=1` implies `k=1`. The estimate on `sigma` uses that a forest on `m` component-vertices with `h` components has at most `m-h` edges, and a `k`-fold star has strictly fewer intersection points than the corresponding resolved 2-fold tree. QED.

**Lemma 2.2 (safe Orevkov bound at geometric degree four).** Let `F` be a Keller map of geometric degree `N=4`, and let `B` be the reduced branch of an actual rank-four proper block of `F` (equivalently: the canonical normalization, `d1=1`). Then `m=#Irr(B)<=3`.

*Proof.* Chau 2004 Lemma 1 realises every irreducible component of `A_F` as `f_phi(C)` for a dicritical series `phi`. Each such component is therefore the image of at least one dicritical line `l subset L_F`, and `mu_l >=1` because `deg f_phi>0`. Orevkov's identity then gives `N-1 = 3 >= sum_l mu_l >= #Irr(A_F)`. Every component of `B` equals a component of `A_F`, so `m<=3`. Extra `A_F` components not in `B` only tighten the inequality. QED.

The same argument at first-leg degree `d1>1` yields only `m <= 4*d1-1`. That is the precise unbounded direction if the ledger is asked to cover intermediate rank-four blocks of unbounded-degree Keller maps. The remainder of this report is the canonical `N=4` ledger. No truncation of that broader direction is made.

**Lemma 2.3 (missing-multiplicity strengthening).** Keep the hypotheses of Lemma 2.2. Assume in addition that at a generic closed point `z` of each component `B_i` one has the fibre identity

```text
N = f(z) + sum_{l maps onto B_i} mu_l,                 (2.3)
```

where `f(z)=#F^{-1}(z)` is the number of finite source preimages. Then `m=1`: there is no reducible target branch.

*Proof.* Polar and constant boundary of Orevkov's collapse map to the target point at infinity, not to the finite point `z`. Corrections in Orevkov's sum are supported at special points of dicritical lines, hence vanish at generic `z`. Thus (2.3) is the identification of missing geometric preimages with the Orevkov base terms over `B_i`. Summing over `i` and adding the global nonnegative correction sum produces

```text
sum_i (N - f(B_i)) + corr = N-1 = 3.
```

The companion-sheet theorem gives `f(B_i)>=1`. The rank-four fibre census gives `f(B_i) <= d1 * u_i = u_i`, and `u_i=2` on `T211`, `u_i=1` on `T31`. Hence `N-f(B_i) >= 2` on every component, so the left side is at least `2m`. Then `2m<=3`, hence `m=1`. A `T31` component only increases the missing multiplicity. Extra `A_F` components likewise. QED.

The identity (2.3) is the unique load-bearing bridge in Lemma 2.3. It is the same comparison the function-pair producer used for a cyclic cover of degree `4 mu` (`0a627206...` §4), specialised to `mu=1` and to the Keller map `F` itself rather than to that cyclic replacement. It is not a promoted theorem. Rows below are therefore recorded in two columns: killed by Lemma 2.3, or still live if only Lemmas 2.1--2.2 and promoted theorems are granted.

**Unbounded remainder, even at `N=4`.** The count `n22` of `(2,2)` identifications is Euler-cancelled and Orevkov-budget-free. On every tree with `h=k=1` one has `n22=b1(B)>=1` with no promoted upper bound. The ledger below is therefore a finite ledger of *incidence trees and inertia types*, each carrying an `n22`-family. That is not a silent truncation: the family is named on every surviving row. No desk-scale computation decides it.

Unibranch singularities are not free. At `N=4` the leftover budget after charging one unit per component is `3-m` under Lemma 2.2, or empty under Lemma 2.3. A unibranch critical parametrization consumes at least one leftover unit. An ordinary conductor node consumes none.

## 3. Incidence trees

With `m in {2,3}` from Lemma 2.2 and `h <= (m+3)/3` from Lemma 2.1, the possible source forests are the following, up to labelling of components. Intersections are recorded as the set `Sigma` of multi-branch points of `R`; each such point is one vertex of the incidence graph.

```text
T2      m=2, h=1.  Unique tree: B1 meet B2 at a single point p, r_p=2.
        Two distinct intersection points would be a cycle, forbidden.
T3path  m=3, h=1.  Chain: B1 meet B2 at p, B2 meet B3 at q, p!=q, r=2,2.
T3star  m=3, h=1.  Star: B1,B2,B3 through a single point p, r_p=3.
T3split m=3, h=2.  Disjoint union of T2 with an isolated component.
```

No other forest on at most three `A1`s exists: a 3-cycle is forbidden, a second edge on `T2` is forbidden, and `h=3` with `m=3` would be three isolated lines, contradicting `m>=2h-1=5`. The split `2+1` is the unique partition of 3 into two nonempty connected sizes.

Places away from infinity, before `(2,2)` identifications, are exactly the incident branches: `paff=(1,1)` on `T2`; `(1,2,1)` on `T3path` in chain order; `(1,1,1)` on `T3star`; `(1,1,0)` on `T3split` with the isolated component last. Each `(2,2)` identification incident to a component adds one finite place on that component's normalization.

Meridional `S4` image. After conjugacy so that one `(2,2)` pairing is `12|34`, the generic transposition of a `T211` component is one of

```text
pair-aligned:    (12) or (34),
overlapping:     (13),(14),(23),(24).
```

Disjoint from both pairing transpositions is impossible in `S4`. A `T31` generic meridian is a 3-cycle fixing one letter; it cannot be assigned to a component that carries an `S22` point. Global monodromy `S4` requires `m211>=1` (otherwise all divisorial inertia is even and the `A4` row of `768cf08f...` §7 is empty). Two pair-aligned transpositions equal to `(12)` and `(34)` generate with no overlapping letter a copy of `C2 x C2` or, with a transporter, at most `D4`, which does not normally generate `S4` (`cf157e17...` §4). An overlapping transposition together with the pairing `(12),(34)` generates `S4`; this is the 72-packet count of that threat map, used here only as a group-generation screen, not as an existence theorem.

## 4. Row ledger

Each row is a pair (Euler packet, incidence tree, inertia assignment). The column `kill` is the strongest statement that closes the row; `OPEN` means live if Lemma 2.3 is not granted. Citation keys: `S4` = `5d7df7ce...` / `768cf08f...` §7; `EULER` = Lemma 2.1; `OREV-SAFE` = Lemma 2.2; `OREV-MISS` = Lemma 2.3; `PI1` = all-degree theorem `9579d3a1...`; `FOREST` = morphic forest as bound in `5d7df7ce...` §3; `ONE-NODE` = `c61f0ceb...` (0.1)--(0.3), applied only when every hypothesis holds; `G3`/`G4` = genus-three / genus-four integrations, which never fire at `m>=2`.

Inertia is written `211^a 31^b` for `(m211,m31)=(a,b)`. The `(2,2)` count is `n22>=n22_min` with `n22_min=h-k+1` and `k` recorded; it is never a killing bound.

### 4.1 Finite-T31 packet (E1, E2, E3): all components `T211`

Here `m31=0`, `t=|T31| in {0,1}`, `h=1`, `k=1`, `n22>=1`, `m211=m in {2,3}`. Every conductor pairing is legal. Unibranch leftover under Lemma 2.2 is `3-m`; E1's unique affine `(3,1)` point consumes one leftover unit if that point is a unibranch critical parametrization.

| id | Euler | tree | inertia | n22_min | leftover | kill | citation |
|---|---|---|---|---|---|---|---|
| R1 | E1 | T2 | 211^2 | 1 | 0 after the cusp | OREV-MISS; else OPEN | Lemma 2.3; G3/G4/ONE-NODE do not apply |
| R2 | E1 | T3path | 211^3 | 1 | -1 | OREV-SAFE (cusp overfills leftover 0) | Lemma 2.2 plus Chau Lemma 4.3 |
| R3 | E1 | T3star | 211^3 | 1 | -1 | OREV-SAFE | same as R2 |
| R4 | E2 | T2 | 211^2 | 1 | 1 | OREV-MISS; else OPEN | Lemma 2.3 |
| R5 | E2 | T3path | 211^3 | 1 | 0 | OREV-MISS; else OPEN | Lemma 2.3; leftover saturated with no unibranch |
| R6 | E2 | T3star | 211^3 | 1 | 0 | OREV-MISS; else OPEN | Lemma 2.3 |
| R7 | E3 | T2 | 211^2 | 1 | 1 | OREV-MISS; else OPEN | Lemma 2.3 |
| R8 | E3 | T3path | 211^3 | 1 | 0 | OREV-MISS; else OPEN | Lemma 2.3 |
| R9 | E3 | T3star | 211^3 | 1 | 0 | OREV-MISS; else OPEN | Lemma 2.3 |

`T3split` is absent: it has `h=2`, incompatible with finite `T31` by Lemma 2.1.1.

E1 on `T2` (row R1) is the unique leftover-zero two-component cusp tree: one ordinary or higher intersection at `p`, one affine `(3,1)` point on one of the two components, one or more conductor nodes on the `T211` support (the whole tree). The hanging component supplies an extra meridian, so the one-node obstruction does not apply even if the unique `(2,2)` is an ordinary node on one component and that component has no other singularity. `PROVISIONAL` genus-ladder statements about conductors 10,16,22,28 are irreducible-one-place statements and do not close R1.

### 4.2 One-dimensional `T31` packet: `h=2`, tree `T3split`

Lemma 2.1 plus `m<=3` force `h=2` and `m=3`, hence `T3split`. Write the isolated component as `I` and the pair as `P1,P2` meeting at `p`. Euler:

```text
(A1) e(T31)+2 n4 + Q = -1,
(P1) e(T31)+2 n4 + Q = -2.
```

`n4=0` is the cheapest. Then `e(T31)=h31-sigma` equals `-1` or `-2` according as `C=A1` with `Q=0` or `C=P1` with `Q=0` (or more negative if `Q>0`, which only increases `sigma`). The isolated component of `R` can be joined to the pair in `B` by `(2,2)` identifications; `k=1` needs at least one such joining identification, `k=2` needs none. All-degree `PI1` requires that some connected component of `B` is not simply connected, so `n22>=1` on at least one piece.

Inertia assignments with `m211>=1` and `S22` supported only on `211` components:

| id | C | (m211,m31) | 31-support | sigma needed (n4=Q=0) | kill | citation |
|---|---|---|---|---|---|---|
| R10 | A1 | (2,1) | I isolated | h31=1, sigma=2 | OREV-MISS; else OPEN | two special points on an isolated A1 |
| R11 | A1 | (2,1) | one of the pair | h31=1, sigma=2 | OREV-MISS; else OPEN | two special points on a component that already meets p |
| R12 | A1 | (1,2) | the pair | h31=1, sigma=2 | OREV-MISS; else OPEN | S22 must then live on the isolated 211 component |
| R13 | A1 | (1,2) | I plus one of the pair | h31=2, sigma=3 | OREV-MISS; else OPEN | three special points on a disconnected 31-subforest |
| R14 | P1 | any of the above | as above | one more special point than R10--R13 | OREV-MISS; else OPEN | EULER plus Lemma 2.3 |
| R15 | * | (0,3) | all three | -- | S4 | `768cf08f...` §7: no transposition, A4 empty |
| R16 | * | (3,0) | empty | e(T31)>=0 | EULER | h=2 forbids finite T31 |

For R10, the two special points on the isolated `T31` component cannot be `S22` (wrong inertia). They are mixed intersections or `S4` or unibranch `(3,1)` points already in `T31`. The isolated component does not meet the pair in `R`, so mixed intersections with the pair are absent on `R`. Hence those two points are `S4` and/or extra unibranch points. Then `n4>=1` or leftover unibranch is required, which feeds back into the Euler equation and only increases the needed `sigma`. The replay checks this bookkeeping; it does not close the row without Lemma 2.3.

`h>=3` is empty at `m<=3` by `m>=2h-1`.

### 4.3 Rows the irreducible census does not close, and rows it must not be applied to

`G3` closes only reduced irreducible `Delta_aff=3` in the charged minimal packet. `G4` closes only reduced irreducible `Delta_aff=4`, `b1=1`, transposition meridians. Neither row of this ledger is of that type.

`ONE-NODE` closes only an irreducible one-place curve whose unique affine singularity is an ordinary node, with every generic meridian a transposition, in a connected simple cover of degree at least four. No row with `m>=2` satisfies irreducibility. A degeneration in which a hanging `T2` component becomes a line through the node of the other component still has two meridians; applying the trefoil-rank bound to one component while ignoring the other is an over-application and is not done. Nonsimple inertia (`T31` generic, or local `(4)` with `A4`/`S4`) is likewise outside that theorem.

The irreducible `m=1` trees are not rows of this ledger. Under Lemma 2.3 they are the only remaining rank-four branch type, and they are the object of the already promoted genus-three and genus-four closures together with the open irreducible higher-delta ladder (`PROVISIONAL` conductors `10,16,22,28`).

### 4.4 Summary counts

The replay in `ops/block_descent_a1_rank4_reducible_tree_ledger_replay.py` enumerates the rows of §4.1--4.2, verifies the Euler arithmetic, the forest list, the `m>=2h-1` inequality, the `S4` inertia screen, the leftover test for E1 on three components, and the one-node scope failure at `m>=2`. It does not encode (2.3), Chau, or the forest theorem.

```text
enumerated rows:                        16
killed independently of (2.3):          4  (R2, R3 leftover; R15 S4; R16 EULER)
surviving if only Lemmas 2.1--2.2:      12 (R1, R4--R14), each with n22 unbounded
surviving if Lemma 2.3 is granted:      none
```

## 5. Survivors, ranked

Assume only Lemmas 2.1--2.2, so that Lemma 2.3 is not charged. The live rows are R1, R4--R14. Apparent fragility, cheapest discriminator, one per row class.

1. **R1 (E1+T2, one cusp, two components).** Most fragile. The unique affine `(3,1)` point plus one overlapping transposition already generates `S4` abstractly (`cf157e17...` §4), so group theory does not kill it. Cheapest discriminator: the two-component link at infinity of a union of two `A1`s through one affine point and one infinite point, with one ordinary cusp on one component and one conductor node. This is a two-component graph link; its meridional rank is the direct analogue of the trefoil-rank bound, now with four meridians (two infinite, one node pair, one cusp) subject to the splice relations of the unique infinite point (Chau Corollary 2). Desk-scale: enumerate Eisenbud--Neumann splice diagrams with two leaves at infinity, one affine cusp weight, and one affine node, and test transposition colourings in `S4`. If that census exceeds desk scale, freeze it as an AWS splice-colouring job; do not run it here.

2. **R4, R7 (E2/E3 + T2, no affine cusp).** Same tree, no `(3,1)` point. Full `S4` must come from overlapping transport at infinity or from the conductor pairing plus an overlapping generic transposition on one component. Cheapest discriminator: the pair-aligned-versus-overlapping screen of `cf157e17...` §4, now with two component meridians. If both generic transpositions are pair-aligned, they are among `{(12),(34)}` and generate a conjugate of `C2 x C2`, order four, not `S4`. A transporter taking one to its disjoint mate enlarges this at most to `D4`, which still does not normally generate `S4` (`cf157e17...` §4; `768cf08f...` §7). This is a finite `S4` check, done in the replay. Surviving subrow: at least one overlapping generic transposition.

3. **R5, R6, R8, R9 (three `T211` components, leftover 0).** Saturated Orevkov with no unibranch. Cheapest discriminator: same overlapping screen. Only two pair-aligned transpositions exist in `S4` once the conductor pairing is fixed, and they generate `C2 x C2`. Survivors have at least one overlapping meridian.

4. **R10--R14 (`h=2` split, one-dimensional `T31`).** Least fragile combinatorially: negative Euler of `T31` demands several special points on an `A1`, and `S22` is confined to the `211` piece. Cheapest discriminator: the local-group incompatibility already promoted — a `(3,1)` component cannot meet an `S22` point — together with the requirement that the isolated piece acquire two special points that are not mixed intersections in `R`. If those points are forced to be `S4`, the Euler equation with `n4>=1` overfills. This bookkeeping is exact and desk-scale; the replay records it as a constraint, not as a kill, because a pair of unibranch points on the isolated `T31` component remains an OPEN geometric realisation question.

In every live row the single cheapest *next* computation after the group screens above is the two-or-three-component splice-colouring census of item 1, restricted first to `n22=1`. That census is finite for each fixed splice diagram. The list of diagrams at unbounded `n22` is not finite; freeze `n22>=2` as a separate AWS registration keyed to `n22`, do not run an unbounded sweep on this machine.

If Lemma 2.3 is granted, the ranking is vacuous: no reducible row survives, and the remaining rank-four object is the irreducible one-place ladder already under promotion and `PROVISIONAL` genus-ladder review.

## 6. Replay

The script `ops/block_descent_a1_rank4_reducible_tree_ledger_replay.py` is a pure-stdlib enumerator. It does not import a CAS, does not touch the network, and contains no `assert`. It recomputes Lemmas 2.1--2.2 arithmetic, the forest list, leftover signs, the `S4` pair-aligned screen, and the one-node scope failure at `m>=2`. Ordinary, `-O`, and `-OO` executions are required to be byte-identical. Documented mutations, all required to exit nonzero:

```text
--mutate-allow-h-two-finite-t31     accept h=2 with e(T31)>=0
--mutate-apply-one-node-to-T2       apply ONE-NODE to m=2
--mutate-drop-overlapping-screen    treat pair-aligned T2 as generating S4
```

Ordinary, `-O`, and `-OO` stdout are byte-identical, with

```text
stdout SHA-256:
54df64d29d363581e4d1aa8c19c67da54a2b7c070e5aedd58d77d5e70ded2baa
payload_sha256=bd6cedfd0328f68780c60844a4c7cb428a2a1d6fa55218911e2476588e27c283
status=PASS-RANK4-REDUCIBLE-TREE-LEDGER
```

All three mutations exit nonzero. What the replay does not prove: identity (2.3), Chau's parametrization, the morphic forest theorem, Zariski--van Kampen, or any splice classification.

## 7. Firewalls

- Flag, place, and series remain distinct: infinite places are Chau places of components, not cv flags, and not cover series of `pi`.
- No exit-price assertion is made. Promoted prices are consumed without a `charge_basis` line.
- `REPRESENTATIVE` trees (T2, T3path, T3star, T3split) are the complete forest list on `m<=3`, not a sample of an infinite family of trees. The infinite family is `n22`, named as such.
- Floor versus attainment: `m>=2h-1` is a lower bound; equality is not claimed. `m<=3` is an upper bound from `mu_l>=1`; equality would require three dicriticals of multiplicity one and zero corrections, which is not attained in any row that also carries a unibranch cusp.
- Lemma 2.3 is typed `OPEN` as a promotion candidate: its gap is exactly (2.3). If (2.3) fails, the safe replacement is Lemma 2.2 together with the live rows R1, R4--R14, not a cap.

Maximum safe statement: *for a canonical geometric-degree-four Keller map, every reducible rank-four proper-block branch has at most three irreducible `A1`-normalised components, incidence forest one of T2, T3path, T3star, T3split, Euler packet one of E1--E3 or the negative-`e(T31)` split packet, and monodromy `S4` with at least one `T211` component; the irreducible one-place census, the one-node obstruction, and the genus-three/four theorems do not apply; `n22` is unbounded on every live tree; if the missing-multiplicity identity (2.3) holds then no such reducible branch exists.* This is not JC2, not a rank-four exclusion, and not a statement about primitive maps without a proper block.

<!-- BODY-END -->
