# Fable 5 hostile review: complete irreducible charged genus-three row

Date: 2026-08-31 UTC  
Reviewer: Fable 5, independent hostile referee  
Packet: `xmodel/block-descent-a1-genus-three-combined-hostile-review-packet-20260831.md`  
Packet SHA-256 (reproduced):
`f26953c6ba20fb5b03db890c99a1964c12cbaa96f7961469565f8ca5927cf85e`

## 0. Summary verdict

| Claim | Verdict |
|---|---|
| 1. Total-delta reduction to `T(3,4)/(4,3)` | `CONFIRM_WITH_CORRECTIONS` |
| 2. `m=0` obstruction | `CONFIRM_WITH_CORRECTIONS` |
| 3. `m=1` obstruction | `CONFIRM_WITH_CORRECTIONS` |
| 4. Global interface (generation + transport) | `CONFIRM_WITH_CORRECTIONS` |
| 5. Scope | `CONFIRMED` |

The proposed exclusion of the complete irreducible charged rank-four
genus-three row stands.  Every load-bearing finite computation was reproduced
or independently replaced; every displayed exact identity was re-derived
symbolically with reviewer-authored code; each claim survived an attempted
failure model.  Three corrections are required, one of them substantive: the
conductor-six delta-sequence classification is complete only for reduced
plane embeddings, and the producers' proofs implicitly work in the reduced
embedding.  The gap is closed below by an explicit elementary-shear
normalization in `Aut(A2)` that preserves every charged structure.  No
verdict is downgraded to `GAP` or `REFUTED`.

## 1. Custody

All hashes were reproduced before any mathematical reading.

1. Packet hash: reproduced exactly (header above).
2. All twenty charged files: SHA-256 reproduced exactly as listed in the
   packet, including the corrigendum
   `xmodel/post-ledger-dependency-hash-corrigendum-sol56-20260831.md`
   (`be4c287f...`).
3. Body seals: for all eight charged `.md` files, the body defined as every
   byte through the unique standalone `<!-- BODY-END -->` line reproduces the
   sealed byte count and body SHA-256.  The marker string also occurs inside
   each seal's prose in backticks; only the standalone line is unique, as the
   seal text specifies.
4. Artifact receipts: all seven `.artifact.json` files are internally
   consistent with their sealed bodies (byte counts, body hashes, full-file
   hashes, frozen bases).
5. Replays: all five charged replays were run under `python3`, `python3 -O`,
   and `python3 -OO`; each is byte-identical across modes.  Reproduced stdout
   SHA-256:

   ```text
   total-delta:  6d71e9d93ed96b2f435893a1229601c5bf2f881bfc18523fd7b62996ca38f666
                 (no hash sealed; mode-invariance claim verified)
   cable-b1:     8887e27ce81d4ca54ee114bbcbb6b4a503cef2fdd525d5d73934bd0e653a67ed  (matches seal)
   m0-complete:  42074e7effccc2d3beb75074a281f83c121ba5e0aaa3278b96d922f3bf4a8013  (matches seal)
   t34-m0:       3d502c2a70391497024dfa6ec5d438d5b57710e533051899e3d78f94e4bd6e41  (matches seal)
   t34-m1:       bd215282fcf28572401de5d2318c1cf7894ee56739e546a532d9c20cf6f9819a  (matches seal)
   ```

6. Mutations: all nine declared mutation flags exit nonzero at their intended
   gates, including spot checks under `-O` and `-OO`.  All five scripts use
   `require`/`check` functions rather than `assert`, so the mutation gates are
   fail-closed under optimization (unlike the earlier campaign fail-open
   incident).  The cable mutation raises exactly the sealed message
   `distinct self-pairs force affine b1 at least two`.

No `CUSTODY_FAIL`.  Custody is clean.

## 2. Independent verification log

All items below were re-derived or re-computed with reviewer-authored code
(sympy or hand-rolled permutation/semigroup code), not by rerunning producer
scripts.

1. **Genus censuses (Schubert).**  Genus-1 iterated cables: trefoils only, no
   satellites.  Genus-2: `T(2,5)`, `C(2,+/-1)(trefoil)`, composite `(1,1)`.
   Genus-3: torus `{(2,7),(3,4)}`, cables `{(2,3,1),(3,1,1)}`; no three-stage
   tower fits (`p*g(J)<=3` forces a genus-one companion).  Matches (0.3) of
   the cable artifact and the census in the total-delta artifact.
2. **Delta sequences.**  Conductor formula re-implemented; the `h=1`
   arithmetic `(r0-1)(r1-1)=6` gives exactly `(7,2),(4,3)`; the `h=2`
   arithmetic forces `d=2`, `(a,b,r2)=(3,2,3)`, so `(6,4,3)` — reproducing
   (3.2)/(3.5) — **for essential first stages** (see Correction C1).
   `(9,6,1)` has conductor 6 but fails freeness (`3 notin <9,6>`), exactly as
   claimed; the winding-three row is semigroup-forbidden.
3. **`(6,4,3)` normal form.**  Full scratch re-derivation with `a3` and `b5`
   retained: `[t^11](V^2-U^3)=2b5-3a3`, so parameter translation (`a3=0`)
   forces `b5=0`; the unique solution of the degree-11..6 system reproduces
   (4.3) exactly, and the degree-5 residual is `-3a1(4a0-a2^2)/8`, reproducing
   (4.4).  The short-Weierstrass identity (4.5) verifies symbolically with
   `t`-degree 3; `Res_t(U',V')=-1728c^5` verifies exactly (4.6); resultant
   elimination of the two divided differences yields
   `s^8(s^3+4hs-c)^2`, the same root set as the artifact's `s^4 H(s)`
   (`s=0` excluded by `c!=0`); `p=c/s-h` and the endpoint discriminant
   `-3c/s` verify mod `H`.
4. **Betti bound.**  `H''=6s` has only the root `s=0`, and `H(0)=-c!=0`, so no
   triple root; at least two distinct roots, nonzero, each giving a genuine
   distinct-endpoint pair; two distinct pairs sharing an endpoint would force
   equal images, so either two multi-point fibres or one fibre of at least
   three points; `b1(B)>=2` in every configuration.  The quotient formula
   `b1(B)=sum_z(#nu^{-1}(z)-1)` is the standard contractible-quotient count.
5. **`(4,3)` coincidence scheme and strata.**  Elimination yields `G(s)^2`
   with `G=s^3+(2a-b)s-c` and no extraneous factor; `X'(s/2)=-D(s)/4`; and
   `G(2t)+Y'(t)=4t*X'(t)`, so `G(2t)=-Y'(t)` exactly on the critical locus,
   confirming (3.4) and the diagonal/nonimmersion identification.  All four
   strata factorizations and diagonal-flag patterns in (3.6) verify
   symbolically, and the case list is complete for a depressed cubic with
   exactly one distinct admissible root.  In stratum II the endpoint
   quadratic factors as `(z-2r)(z+r)`: the cusp parameter `-r` is a conductor
   endpoint **and** an `X`-critical point, and `X(2r)=X(-r)=2r^3`.
6. **Smoothness at infinity.**  The `(4,3)` closure has the single infinity
   point `[0:1:0]` with local expansion `u=r+O(r^3)`, `v=r^4(1+O(r^2))`:
   smooth, so total affine delta is exactly `p_a(quartic)=3`.
7. **Group censuses (own implementation, both Artin conventions).**  96
   ordered full-`S4` transposition triples (= 16 spanning trees by Cayley's
   formula times 6 orderings); 0 duplicate triples generate `S4`, maximal
   duplicate subgroup order 6; `T(3,4)` boundary word fixes exactly 24
   full-`S4` colorings **under both conjugation conventions**; `T(2,7)` fixes
   0, and independently *no* two transpositions act transitively on four
   letters, so the two-bridge row dies before any braid relation; the
   displayed evolution table (7.4) reproduces line-for-line; triples inside a
   fixed-sheet `S3` or inside `<(12),(34)>` are never transitive; positive and
   negative Hurwitz moves preserve the generated subgroup on all 216 triples.
8. **Determinants and covers.**  `det T(3,4)=3`, `det T(2,7)=7`,
   `det(trefoil#trefoil)=9`, `det C(2,+/-1)(J)=|Delta_J(1)|=1`; the composite
   presentation (6.1)-(6.2) satisfies both braid relations, generates order
   24, with `(12),(34)` commuting.  The double-branched-cover lemma re-proved:
   sign is the unique mod-two abelianization, the kernel surjects onto `A4`,
   `pi1(Sigma_2)` is the kernel mod squared meridian, so `3 | det`.  The `E6`
   correction is right: `x^2+y^3+z^4` is `E6`, link group binary tetrahedral
   of order 24, abelianization `C3`, consistent with `det=3`; binary
   octahedral is `E7`, and the `(2,3,4)` triangle mnemonic fails because the
   exponents are not pairwise coprime.
9. **Expected cable Alexander polynomials.**
   `Delta_{C(2,3)(trefoil)}=(t^2-t+1)(t^4-t^2+1)` and
   `Delta_{C(3,1)(trefoil)}=t^6-t^3+1` re-derived from the cable formula;
   these are what the producer replay checks its braid words against, so the
   framing convention is pinned by an invariant, not by trust.
10. **Threat-map spectator.**  (6.1)-(6.6) re-verified: branch `(4t-4t^3,
    2t^2-3t^4)`; unique ordinary node from `t^2+tu+u^2=1`, `u=-t`, `t^2=1`
    (the alternative branch forces `(t-u)^2=0`); `(2,2)` fibre
    `(w-1)^2(w+1)^2` at `(0,-1)`; cusps at `t^2=1/3` with fibre
    `(w-r)^3(w+3r)`; `U isomorphic to Gm x A1`, Euler number 0, nonconstant
    unit.  The ruling rows (0.1) follow from `e(U)=2-m` and
    `e(U)=e(C)+Q>=1`.
11. **Ledger identities.**  (3.1), (4.2), (6.2) of the coordinator re-checked
    arithmetically; `D4`'s transpositions generate an intransitive order-four
    subgroup; `A4` has no transposition.

## 3. Claim 1: total-delta reduction — `CONFIRM_WITH_CORRECTIONS`

**Statement audited.**  Under the charged irreducible one-place
`b1=1,n22=1,n4=0` packet with transitive meridional `S4` and every positive
generic meridian a transposition, total affine delta three leaves only the
infinity knot `T(3,4)` with delta sequence `(4,3)`.

**Weakest exact hypotheses.**  `B` reduced irreducible affine plane curve;
`normalization(B)=A1` (Chau interface, coordinator Section 2);
`Delta_aff(B)=3`; `b1(B)=1`; a representation `pi1(A2-B)->S4`, transitive,
sending every positive generic meridian to a transposition; the three sealed
interfaces `g_3(K_infinity)=Delta_aff(B)`, prime-iterated-cable-or-unknot,
and the meridian-compatible surjection `pi1(S3-K_infinity)->>pi1(A2-B)`.

**Adjudication.**  The four-row census (0.3) is complete (item 2.1).  Row
kills: `T(2,7)` is doubly dead (0 colorings; moreover any transposition image
of a two-generator group is intransitive on four letters; determinant 7).
The winding-three row is doubly dead (semigroup freeness failure of
`(9,6,1)`, which I verified is *forced* by conductor six once the first stage
is the trefoil with `d=3`; and 0 colorings).  The winding-two row survives
every group gate (72 labelled colorings; the count is convention-dependent
but not load-bearing) and is killed exactly by the algebraic normal form:
every `(6,4,3)` parametrization has the complete form (0.4), its self-pairs
are the roots of the cubic `H`, `H` has at least two distinct roots, and
`b1(B)>=2` follows in every collision pattern (items 2.3-2.4).  Only
`T(3,4)/(4,3)` remains, with 24 boundary colorings, so the boundary gate
cannot close it and the row correctly passes to claims 2-3.

**Sign/mirror conventions.**  Harmless, by an exact argument the artifact
only sketches: a tuple is fixed by a braid `beta` iff it is fixed by
`beta^{-1}`, and the mirror closed braid is conjugate to the inverse braid,
so mirror rows have identical coloring counts; the delta-sequence arithmetic
uses absolute characteristic data; and my convention-B recount reproduces 24.

**Corrigendum.**  Followed and charged.  The cable artifact's Section 1 binds
the GPT-5.5 review path to hash `72cf5510...`, which the corrigendum states
belongs to an ideation file; the corrected custody chain is recorded there.
I could not and did not inspect the review itself (not charged; sibling
report).  This does not matter mathematically: the three consumed interfaces
are proved in the charged total-delta artifact and were independently
desk-verified here (Section 6 below), so the cable conclusion does not rest
on the misbound receipt.  Any promotion must charge the corrigendum alongside
the cable artifact.

**Attempted failure model.**  (a) Engineer `b1=1` in the `(6,4,3)` row via
shared endpoints or coincident images of the two pairs — fails: shared
endpoint forces equal images, and one fibre of at least three points already
contributes two.  (b) Flip the Artin convention to break the coloring counts
— counts invariant.  (c) Embed the row redundantly so the delta-sequence
census misses it — this *works* against the literal census statement and is
Correction C1; it is repaired by shear reduction, after which the census is
complete.  No failure survives.

**Blast radius if wrong.**  If the winding-two `b1` bound failed, the
`C(2,3)(trefoil)` row would reopen with 72 surviving colorings and no
degree-three coordinate, and the genus-three closure would be lost.  It does
not fail; the bound is fully symbolic and was re-derived.

## 4. Claim 2: `m=0` — `CONFIRM_WITH_CORRECTIONS`

**Adjudication.**  (i) *Critical point outside the conductor pair.*  The
cubic `X` restricted to the normalization is a monic degree-three polynomial
map, so every scheme fibre has length exactly three.  Both endpoints critical
needs `2+2>3`; a double root at an endpoint needs `3+1>3`; so some critical
`c notin {a,b}` exists, and `X(c)` differs from the conductor value (else
length at least `3+1+1` or `2+1+1+...` exceeds three; in the totally ramified
case `3c` saturates the fibre by itself).  Verified in all four strata; in
stratum II one endpoint (`-r`) *is* critical and the proof correctly survives
on the other root `+r`, which I checked lies outside the pair
`{2r,-r}`.

(ii) *`T211/C2` duplication.*  The henselian rank decomposition `(2,1,1)`
makes the local monodromy orbits have sizes at most `2,1,1`, so the local
decomposition group embeds in `C2`; the length-one factors are reduced points
and cannot carry the ramification, so the rank-two factor does.  Transported
cluster meridians are generic meridians, hence transpositions, hence both
equal the unique nonidentity element.  `C2` is abelian with singleton
conjugacy classes, so this is path-independent inside the local frame.  The
argument correctly does *not* assume the normalization is immersive: `nu(c)`
may be a point-bijective unibranch singularity (strata II-IV contain cusps
and a `(2,5)` point), and the charged fibre-table interface — not
smoothness — supplies `C2`.  The t34-m0 audit's warning that "diagonal root
implies `(3,1)` fibre" is false without the cover algebra is correct and is
respected: `m` counts quartic `T31` fibres, not cusps of `B`, so all four
strata legitimately sit in the `m=0` row.

(iii) *Braid tail.*  Elementary Hurwitz moves are Nielsen transformations;
verified exhaustively in both directions on all 216 triples; basepoint change
is simultaneous conjugation.  A duplicate triple has at most two distinct
support edges, cannot connect four vertices, and generates order at most six;
no duplicate triple generates `S4` (0 of 96 duplicates).  The original triple
generates `pi1(A2-B)` (claim 4), whose charged image is transitive `S4`;
contradiction.

(iv) *Four nonimmersion strata.*  Classification (3.6) verified complete and
correct (item 2.5).

**Weakest hypotheses.**  Charged row (0.1) of the m0 artifact; the henselian
local table; the two transport lemmas of claim 4; reduced embedding
(Correction C1).

**Attempted failure model.**  (a) Hide the ramification of a `(2,1,1)` fibre
in a length-one factor — impossible, reduced points are unramified.  (b)
Enlarge the local group past `C2` by monodromy mixing factors — impossible,
orbits refine the factor decomposition for a small ball.  (c) Use
three-cycle generic meridians — excluded by the charged hypothesis; and
independently, an irreducible `B` through a `(2,2)` point cannot be
three-cycle-generic, since its generic meridian is conjugate into the
`(2,2)`-point's local group inside `S2 x S2`, which contains no three-cycle.
This last argument (not in the artifacts) grounds the charged
transposition-genericity for the irreducible row rather than leaving it a
bare assumption.  All fail.

**Blast radius.**  Confined to `m=0`; if the henselian-orbit argument failed
both claims 2 and 3 would fall, but it is sound.

## 5. Claim 3: `m=1` — `CONFIRM_WITH_CORRECTIONS`

**Adjudication.**  The critical divisor of the cubic has length two; the case
analysis is exhaustive and each case intransitive.

* *Double root at `c` (the `T31` preimage).*  The fibre is `3c`, saturated,
  so by properness all three punctures enter one ball around `z31`; a
  common-connector adapted basis places all three images in the local
  `S3` fixing the fourth sheet — intransitive.  The disjointness `c notin
  {a,b}` (claim's "why a conductor endpoint is impossible" for the cusp) is
  forced because one scheme point has one partition: `T31` and `S22` are
  disjoint strata, so `z31 != n`.
* *Double root at a conductor endpoint.*  Length `3+1>3` — impossible.
* *Double root elsewhere.*  `T211`; all three meridians in `C2`; triple
  `(tau,tau,tau)`.
* *Two simple roots.*  At most one can be `c` (two distinct parameters, one
  point).  Pick `r != c`.  If `r notin {a,b}`: `T211` duplicate
  `(tau,tau,rho)`.  If `r in {a,b}`: the fibre `2a+b` has length three,
  saturated — verified: no remote fourth contribution exists, and both
  cluster limits `a,b` map to the *same* target point `n`, so all three
  punctures enter one ball around `n` and the whole triple lies in the local
  group of the `(2,2)` point.  That group embeds in the pair-preserving
  `<(12),(34)>` because its orbits are the two rank-two henselian factors;
  an element exchanging the pairs would merge the factors.  This is
  intransitive (orbits `{1,2},{3,4}`) and must not be confused with the
  transitive diagonal Klein group, which is not a subgroup of
  `S2 x S2` in this embedding.  Both roots at the two endpoints: `2+2>3` —
  impossible.

The earlier caution that a lone `(3,1)` point permits overlapping
transpositions is correctly retired: the cubic always has a second unit of
ramification, or both units coalesce inside the fixed-sheet `S3`.

**Weakest hypotheses.**  Charged row (0.1) of the m1 artifact including
`Delta_aff=3` and the disjoint stratification; local table (1.1); claim 4
lemmas; reduced embedding (C1).

**Attempted failure model.**  (a) Transitive local group at `S22` — blocked
by factor orbits.  (b) `z31=n` merged fibre — blocked by partition
uniqueness.  (c) Overlap at a simple `T211` cluster — blocked, `C2` forces
equality not overlap.  (d) Critical value colliding with the conductor value
(`X(r)=X(a)` with `r` outside the pair) — blocked, length `2+1+1>3`, so the
`T211` cluster is automatically isolated from the conductor fibre.  All
fail.

**Blast radius.**  Confined to the `m=1`, `Delta_aff=3` row; together with
claim 2 it closes the complete irreducible charged genus-three packet.

## 6. Claim 4: global interface — `CONFIRM_WITH_CORRECTIONS`

This is the highest-risk bridge, and it holds, with two lemmas that should be
made explicit (Corrections C2, C3).

**Generation.**  For the reduced `(4,3)` embedding,
`F(x,y)=Res_t(X(t)-x,Y(t)-y)` is, up to sign, `prod_i(y-Y(t_i))` over the
three roots of `X(t)=x`: monic of degree three in `y`.  So `B` is proper over
the `x`-line, every vertical line meets `B` in scheme length exactly three,
and a horizontal section at large `|y|` avoids `B`.  The complement fibres
over `A1_x` with fibre a line minus at most three points; since the base has
trivial fundamental group and a section exists, the three meridians of one
generic vertical fibre generate `pi1(A2-B)`.  This is the standard affine
Zariski--van Kampen generation statement under exactly the monic-in-`y`
hypothesis, which is *verified*, not assumed.  **Proved.**

**Transport.**  Moving the based generic fibre along a path in the base
transforms the geometric meridian basis by a braid — a composition of
elementary Hurwitz moves and inverses — plus one simultaneous conjugation for
basepoint change; the generated subgroup is preserved up to conjugacy
(verified exhaustively at the `S4` level).  Two points need to be explicit:

* (C2) *Adapted bases exist and are braid-equivalent.*  In the near-critical
  fibre, choose meridians for the local cluster that share one common
  connecting path into the small ball `N` and loop inside `N-B`; such a
  system extends to a geometric basis, and any two geometric bases of a
  punctured disk differ by a braid (Artin transitivity) plus conjugation.
  With the common connector, the cluster images are simultaneous conjugates
  of elements of the local decomposition group by a *single* element, so
  duplicates and containments survive into the global frame.  Without the
  common-connector choice the two cluster meridians would only be separately
  conjugate into the local group, and the duplicate-color step would fail;
  this is the precise content the producers' phrase "local projection frame"
  must carry.  The m1 artifact's Section 3 states the locality and properness
  correctly; the adapted-basis/Artin step is implicit in all three proofs.
* (C3) *Local groups via small balls.*  Meridians chosen inside `N-B` land in
  `H_z` by definition once `N` is small enough for the conic structure and
  for `pi^{-1}(N)` to split into fibre-point neighborhoods; the sheet orbits
  then refine the henselian factors.  This is standard but load-bearing and
  should be cited once.

**Saturated fibres.**  For `3c` and `2a+b`, all three punctures lie in one
ball (properness plus, in the second case, `nu(a)=nu(b)=n`), so the entire
triple is local and the argument needs no remote meridian at all — the
strongest and cleanest form of the bridge, correctly identified by the m1
artifact.

**Attempted failure model.**  (a) Independent conjugation of individual
entries under basepoint change — impossible, one connector conjugates the
whole group.  (b) Extra generators or relations from atypical behavior at
infinity in the fibre direction — excluded by monicity.  (c) Escape of a
cluster puncture from `N` — excluded by properness/finiteness.  All fail.

## 7. Claim 5: scope — `CONFIRMED`

The combined result closes exactly the irreducible charged minimal rank-four
`Delta_aff=3` row: both `m=0` and `m=1` subrows, which are the only subrows
consistent with the ruling rows (0.1) of the threat map (`e(U)=2-m>=1`).  The
`m>=2` exclusion and the `(2,1,1)`-genericity it needs are available for the
irreducible charged row (Section 4's three-cycle argument).  Each artifact's
own firewall list is accurate.  Not covered, and correctly disclaimed:
reducible source forests (the prime-cable theorem, the single polynomial
parametrization, and the one-projection Zariski--van Kampen argument all fail
for several components); `Delta_aff>=4` (the group-level `T(3,4)` escape at
delta three shows the topology alone cannot do more; delta four is untested);
nonminimal quartic rows; higher generic degree; the primitive/no-proper-block
horn; JC2.  Together with the sealed total-delta theorem, the promotable
consequence for the irreducible charged row is `Delta_aff(B)>=4`.

## 8. Corrections required

* **C1 (substantive).**  The conductor-six classification
  `(7,2),(4,3),(6,4,3)` is complete only for *reduced* embeddings: the
  producers' `h=2` arithmetic assumes `a>b>=2`, but raw one-place embeddings
  with a trivial first stage (`r1 | r0`) also occur at conductor six —
  e.g. `(6,3,4)`, `(8,4,3)`, `(12,4,3)`, and longer prefixes such as
  `(24,12,3,4)` — and for such an embedding *no linear coordinate of degree
  three exists*, so the claims 2-4 projection arguments do not literally
  apply.  Repair (verified concretely on `(t^12+t^3, t^4)`): if `r1 | r0`
  the leading terms satisfy `LT(x)=c*LT(y)^{r0/r1}`, so the elementary shear
  `x -> x-c*y^{r0/r1}` is a polynomial automorphism of the target plane that
  strictly reduces the degree; iterating terminates in a reduced embedding.
  Shears preserve the block data, the complement, the meridian classes, the
  monodromy, the fibre stratification, `b1`, and `Delta_aff`.  At conductor
  six the reduced row cannot be `(7,2)` (wrong abstract semigroup) or
  `(6,4,3)` (forces `b1>=2`), so the charged row lands on `(4,3)` with
  coordinate degrees `(4,3)`, as the proofs require.  The producers'
  normalizations must be widened from "affine changes of the target" to
  "affine changes plus elementary shears", or equivalently the theorems
  should state the reduced-embedding normalization as a first proof step.
* **C2.**  State the adapted-basis lemma: cluster meridians with one common
  connector form part of a geometric basis, and geometric bases are a single
  braid orbit (Artin), so local duplicates/containments transfer to the
  original frame up to Hurwitz moves and one simultaneous conjugation.
* **C3.**  Cite once the small-ball/henselian comparison that puts local
  meridians in the decomposition group and identifies sheet orbits with the
  local factors.
* **Minor.**  (a) The `(6,4,3)` derivation should include the degree-11
  coefficient `2b5-3a3`, which is what forces `b5=0` after the parameter
  translation; as printed, (4.2) silently assumes it.  (b) The cable
  artifact's (5.2) exponent (`s^4 H`) differs from the resultant computation
  (`s^8 H^2`); root sets agree, no consequence.  (c) Promotions consuming the
  cable artifact must charge the corrigendum (hash misbinding of the GPT
  review); noted in claim 1.

## 9. Maximum-safe theorem and next falsification test

**Maximum-safe theorem.**  Let an actual rank-four proper block be given with
its charged packet: reduced target branch `B` irreducible,
`normalization(B)=A1`, `b1(B)=n22=1`, `n4=0`, finite `T31` locus, global
meridional monodromy `S4` with every positive generic meridian a
transposition.  Then `Delta_aff(B)>=4`.  In particular the complete
irreducible charged minimal-cycle genus-three row — every `Delta_aff=3`
subrow, `m=0` and `m=1` alike — is empty, and this exhausts the subrows
permitted by the proper-block ruling.

**Next falsification test.**  Run the same screen at conductor eight.  My
independent census gives the reduced genus-four delta-sequence rows
`(9,2)`, `(5,3)`, `(6,4,5)`, and — newly free at this genus — `(9,6,2)`,
beside three-stage knot candidates such as `C(2,+/-1)` on a genus-two
companion.  The first concrete gate: compute the labelled meridian-
transposition full-`S4` coloring count of the `T(3,5)` boundary braid
`(sigma_1 sigma_2)^5` and of the `C(3,2)(trefoil)` and `C(2,5)(trefoil)`
words.  If `T(3,5)/(5,3)` retains colorings, attempt the direct analogue of
the present closure: the `(5,3)` row still has a degree-three coordinate, its
critical divisor still has length two, but the conductor budget changes
(`b1=1` now coexists with delta four), so the four-strata classification of
`X=t^3+at, Y=t^5+...` must be redone; a surviving stratum whose two critical
points are both absorbed compatibly would falsify the hope that the
projection obstruction extends beyond genus three.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `26640`.
- Body SHA-256:
  `e997a9a90a2bcd794bf9c87aef747aa2b7f5394c056f28f6a307b2997dc545ad`.
- Frozen basis: `892179b5d833f89123852b2562afd4b65a4fb1e2`.
