# Hostile review: total-delta and Fox/localization quartic obstructions

Date: 2026-08-30
Reviewer: GPT-5.5 hostile pass
Scope: only the charged files named in the prompt were hash-checked and audited.
No sibling prompt/report/log/run/receipt was read. No `jc2-lean` path was inspected.
Receipt status: ABSENT.

## Custody

All charged SHA-256 hashes matched exactly:

- `03865aae3cc11a5f7de264ef7a66d1e3600ccb983ea8f95079c50d8a28b0b5aa`
  for `xmodel/block-descent-a1-total-delta-two-iterated-knot-s4-obstruction-sol56-20260830.md`.
- `6d495706aaab256710a263681816dfab6b9c562f163aa9efe11dd4a025429a00`
  for its artifact JSON.
- `f5438492f6092eaa032371fdecf3215dca1a74aea67dd53b53dbe3e983166923`
  for `ops/block_descent_a1_total_delta_two_iterated_knot_s4_replay.py`.
- `60ba8f433f4ecd98ead9820dc627c9a88f927851d3289af07de2c68b005824a0`
  for `xmodel/block-descent-a1-quartic-double-plane-fox-localization-kernel-sol56-20260830.md`.
- `5e628a08e5d3cedbdbb657d7df64dc5aede5d40f1c2ca93c7557faff70417921`
  for its artifact JSON.
- `a83e110935c96f934b80b61a2cd5a2323d4f6cbfd3212004b3be4b3256b5b39c`
  for `xmodel/block-descent-a1-quartic-double-plane-constant-unit-pic3-reduction-sol56-20260830.md`.
- `43c83d47d864537aae6fec7203111aaa3c6c52fa4bbc0e95c6877c61aa86ad57`
  for `xmodel/block-descent-a1-quartic-cycle0-polynomial-link-obstruction-sol56-20260830.md`.
- `c61f0cebdc06bdca88ad76f3714047a1998ff7aeb885a79e84b060a091c23329`
  for `xmodel/block-descent-a1-one-ordinary-node-all-degree-meridional-rank-obstruction-sol56-20260830.md`.

Primary sources fetched only under `/tmp/jc2_hostile_sources.7fD4Hw`:

- Neumann--Rudolph, "Corrigendum: Unfoldings in knot theory", Math. Ann. 282
  (1988), 349-351, DOI `10.1007/BF01456981`, fetched from
  `https://link.springer.com/content/pdf/10.1007/BF01456981.pdf`.
  Interface used: corrected definition of good polynomial and Lemma 7.1
  "A Knot at Infinity is Good" in the PDF text lines 20-42, plus the
  proof interface at lines 98-112.
- Rudolph, "Some knot theory of complex plane curves", arXiv `math/0106058`,
  fetched from `https://arxiv.org/pdf/math/0106058`.
  Interface used: bidisk cabling definitions and iterated torus knots at text
  lines 96-123, polynomial-parametrized large-bidisk infinity knot at lines
  368-371, and the algebraic local braid at infinity restriction at lines
  799-802.
- Neumann--Le Van Thanh, "On irregular links at infinity of algebraic plane
  curves", arXiv `alg-geom/9202008`, fetched from
  `https://arxiv.org/pdf/alg-geom/9202008`.
  Interface used: large-sphere link at infinity is well-defined and toral at
  text lines 15-18, RPI root/splice notation at lines 55-66, and regularity
  equivalence Theorem 1.2 at lines 76-89.
- Neumann, "Complex algebraic plane curves via their links at infinity",
  Invent. Math. 98 (1989), 445-489, DOI `10.1007/BF01393832`.
  The Springer fetch returned article metadata/abstract HTML rather than the
  PDF theorem text; Celebratio likewise exposed bibliographic data and a
  generic media link only. I therefore do not treat the page-447/page-450
  theorem wording as independently source-verified in this pass.
- Schubert, "Knoten und Vollringe", Acta Math. 90 (1953), 131-286, DOI
  `10.1007/BF02392437`.
  The Springer fetch returned subscription metadata/abstract HTML, and the
  Project Euclid download endpoint returned an access-control iframe. I use
  the standard Schubert genus/primeness/Alexander interfaces as stated in the
  charged artifact, but the exact source theorem text was not independently
  fetched here.

## Itemized review

1. CONFIRMED - Nearby-fibre genus and boundary.

For irreducible `B` with normalization `A1`, the projective normalization is
`P1` with one deleted point, so the link at infinity has one component. The
corrected Neumann--Rudolph lemma applies to a reduced fibre with knot link at
infinity and makes the defining polynomial good. Goodness is the needed
hypothesis: it prevents extra vanishing cycles at infinity and keeps the
infinity link fixed for a small regular value.

The Euler characteristic computation in the total-delta artifact is correct.
Start from a disk core of the normalization, remove one small disk for each
local branch over every affine singular point, and glue in the connected local
Milnor fibre with `chi = 1 - mu_p` and `mu_p = 2 delta_p - r_p + 1`. The result
is connected, has the original single boundary component, and has
`chi = 1 - 2 sum delta_p`, hence genus exactly `Delta_aff(B)`. I found no
missing infinity or disconnected-fibre counterexample under the corrected
goodness hypothesis.

2. CONFIRM_WITH_CORRECTIONS - One place gives an iterated cable, not a
connected sum.

The claim is safe, but the proof should not rest solely on the unfetched
Neumann 1989 Theorem 2(i) wording. The accessible Rudolph interface is enough:
for a polynomial parametrization `(p(t),q(t))`, the very large bidisk boundary
is an iterated torus knot. Finite affine self-identifications occur in a compact
parameter set and cannot create a connected-sum operation in the one tail seen
at infinity.

After deleting winding-one or unknot-producing steps, a nontrivial one-place
infinity knot is a nontrivial iterated cable. The standard Schubert primeness
interface then gives prime or unknot. The correction is bibliographic, not
mathematical: the rooted-splice source theorem text was not independently
available in this environment, so Rudolph's parametrized theorem is the cleaner
primary interface for this review.

3. CONFIRMED - Genus zero, one, and two graph-knot census.

Using the stated Schubert formulas
`g(J#L)=g(J)+g(L)` and
`g(C_(p,q)(J))=p g(J)+(p-1)(|q|-1)/2`, with `p>=2` and trivial steps removed:

- genus zero leaves only the unknot;
- genus one leaves only `T(2,+/-3)`, the trefoils;
- genus two leaves exactly `T(2,+/-5)`,
  `T(2,+/-3)#T(2,+/-3)` with independent mirrors, and
  `C_(2,+/-1)(T(2,+/-3))` with companion mirror allowed.

The winding/sign conventions do not change the conclusion because the formulas
use `|q|` and mirrors preserve determinant. The cable determinant calculation
is also correct:
`Delta_C(t)=Delta_T(2, +/-1)(t) Delta_J(t^2)` and
`Delta_T(2, +/-1)=1`, so evaluation at `t=-1` gives
`det C_(2,+/-1)(J)=|Delta_J(1)|=1`. Thus the prime genus-two candidates have
determinants `5` and `1`; the composite has determinant `9`.

4. CONFIRMED - Determinant lemma and boundary-to-affine passage.

A transitive subgroup of `S4` generated by transpositions is all of `S4`.
The sign composite with the knot group is the unique mod-two abelianization
sending a meridian to `1`. Restricting to the mod-two kernel surjects onto
`A4`; filling the unbranched double cover to the double branched cover kills
the lift of the meridian square, already trivial in `S4`. Therefore
`pi1(Sigma_2(K)) ->> A4`, and abelianization gives a quotient `C3`. Since
`|H1(Sigma_2(K),Z)|=det(K)`, `3 | det(K)`.

The affine use is also in the right direction. Zariski--van Kampen imposes the
finite braid relations separately, while the boundary knot group imposes only
their product, so `pi1(S3-K_infinity) ->> pi1(A2-B)`. Any affine `S4`
transposition representation pulls back to the boundary group.

5. CONFIRMED - Replay and delta-three mutation.

I reran
`ops/block_descent_a1_total_delta_two_iterated_knot_s4_replay.py` normally,
under `python3 -O`, and under `python3 -OO`. The three stdout files were
byte-identical with SHA-256
`6d71e9d93ed96b2f435893a1229601c5bf2f881bfc18523fd7b62996ca38f666`.

The mutation
`--mutate-exclude-delta-three` exited with status `1` and raised
`RuntimeError: false delta-three exclusion`. The replay's `T(3,4)` coloring is
independently correct under the displayed Artin convention:
`((12),(13),(14))` returns to itself under `(sigma1 sigma2)^4`, and the three
star transpositions generate `S4`.

The replay proves only finite arithmetic and group checks: genus-two
Diophantine census, determinant constants, the composite `S4` witness, the
`T(3,4)` coloring count, and `<3,4>` gaps. It does not certify goodness at
infinity, local Milnor theory, Schubert primeness, rooted splice theory,
Zariski--van Kampen, or the double-branched-cover group identification.

6. CONFIRMED - Constant units, Kummer, normality, and anti-invariance.

For `R=C[x,y,s]/(s^2-q)` with `q` squarefree nonconstant and `V(q)` connected,
the unit proof is sound. If `u=a+bs` is a unit, its norm
`a^2-qb^2` is constant. After scaling to norm one,
`(a-1)(a+1)=q b^2`. Since `a-1` and `a+1` have no common nonconstant factor,
the odd supports of the two sides partition the connected branch curve. The
iteration through `r_i^2-c_i` forces an impossible infinite degree-halving
unless `a` is constant; then `b=0`.

The Kummer sequence for `mu_3` on the etale site is valid on the possibly
singular affine scheme because `3` is invertible. Since `R*=C*` and `C*` is
divisible, the unit term vanishes and
`H^1_et(D,F3) ~= Pic(D)[3]`. Squarefree `q` makes `D` normal: it is a
hypersurface, hence `S2`, and its singular locus is finite over the singular
locus of the reduced plane curve, hence codimension two. Normality is needed
only for the later Weil/Picard firewall, not for Kummer exactness.

The norm identity for the finite flat double cover gives
`L tensor iota^*L` pulled back from `Pic(A2)=0`; hence `iota^*[L]=-[L]` on
`Pic(D)`. Therefore all etale `F3` classes are anti-invariant.

7. CONFIRM_WITH_CORRECTIONS - Localization kernel.

The exact statement should be cohomological:

`Pic(D)[3] ~= ker[H^1(U,L_sign) -> direct_sum_p H^1(M_p,F3)]`.

With that correction, the identification is sound. The sign local system on
`U=A2-B` corresponds to the unramified double cover
`D - pi^{-1}(B)`. Filling the smooth ramification divisor kills meridian
squares; every sign cocycle vanishes on those squares because
`z(m^2)=z(m)-z(m)=0`. Thus smooth ramification imposes no extra local gate.

At isolated singular points of `D`, conical neighborhoods imply that passing
from `D_reg` to `D` normally kills the images of the link groups `pi1(M_p)`.
Degree-one cohomology therefore injects into `H^1(D_reg,F3)` with image the
simultaneous kernel of restriction to all `M_p`. No anti-invariant quotient is
missing: the source classes are already anti-invariant, but extension requires
zero in the full local group, so mapping to full `H^1(M_p,F3)` is harmless and
stronger in notation.

The representation translation is also correct. A sign cocycle gives an
`S3=F3 semidirect C2` meridian-transposition representation. Vanishing on the
local even subgroup is equivalent, up to `A3` conjugacy/coboundary, to the
local image being a conjugate `C2`.

8. CONFIRM_WITH_CORRECTIONS - Infinity injection, Fox identity, and false
positives.

The injection
`Pic(D)[3] -> H^1(S3-K_infinity,L_sign)` follows from the boundary-to-affine
group surjection and degree-one inflation. For a knot, the usual Fox
identification gives
`H^1(S3-K,L_sign) ~= H^1(Sigma_2(K),F3)`, with reduced Fox 3-colorings
corresponding to nonzero classes. Consequently `3 | det(K)` is necessary and
sufficient for a nonzero boundary Fox class, but only necessary for a global
Picard class on `D`.

The trefoil tangency control checks out exactly. For
`X=t^4+t^3-t`, `Y=t^2`, the only nontrivial identification is `{1,-1}`,
the two tangent vectors have determinant `-8`, the affine van Kampen relations
are `a=b` and `[a,b]=1`, and the affine complement group is `Z`. Since
`H^1(Z,F3^sign)=0`, the trefoil boundary coloring dies after imposing the
separate affine tangency relation.

The infinite family
`X=t^3`, `Y=t^(3r+1)(t+1)` also checks out. Substitution cancels in the
displayed implicit equation. The only two-point identification is
`{zeta,zeta^2}`, it is transverse, and the origin has unibranch type
`(3,3r+1)`. For even `r`, the local determinant `det T(3,3r+1)=1` and the
infinity determinant `det T(3,3r+2)=3`. The local `C2` condition forces all
three projection meridians to the same transposition, hence the resulting
class is a coboundary and the global kernel is zero. This is a genuine
determinant false-positive family, not a counterexample.

9. CONFIRMED - Combined quartic consequence and exclusions.

The total-delta theorem alone gives the relevant quartic exclusion: if `B` is
irreducible with normalization `A1` and `pi1(A2-B)` has a transitive
meridian-transposition representation to `S4`, then
`Delta_aff(B) >= 3`. Therefore a connected generically simply ramified degree
four cover cannot have an irreducible `A1`-normalized branch curve with total
affine delta at most two.

The Fox/localization artifact is compatible with, but not needed for, this
low-delta exclusion. It clarifies why determinant screens are only necessary
and why the remaining double-plane problem is a Picard/localization kernel.

The `T(3,4)` delta-three control does not pass the local `C2` gate. Its single
local cusp already carries the three star transpositions generating `S4`; after
passing to the resolvent `S3` language, the local image is not conjugate to
`C2`. Thus it is a sharp total-delta counter-control for the group obstruction,
not a DP3/localization survivor.

No reducible, multi-place, non-transposition, disconnected-cover, or non-simple
lane is licensed by this combination. Those cases have different boundary
links, different normalization/Euler ledgers, or different monodromy
hypotheses.

10. GAP - Higher-delta global-overlap kernel remains open.

No reviewed artifact proves universal vanishing of the higher-delta global
overlap kernel. A general Alexander-module or splice-diagram argument may be a
good attack, but determinant and boundary cyclotomic data alone are too weak:
the trefoil control and the infinite family show boundary classes can die only
after separate affine and singular-link restrictions are imposed.

The safe successor is linear and exact. Work over `F3` at sign `t=-1`; compute
the full twisted Fox/Alexander kernel for the affine braid presentation; impose
each finite braid relation separately; then impose the restriction-zero maps to
the double-plane singular links. Splice diagrams are useful for boundary
screening and for organizing local data, but the theorem must be an
intersection statement for this affine/local kernel.

## Maximum-safe theorem

Let `B` be a reduced irreducible affine plane curve over `C` with
normalization `A1`. If `pi1(A2-B)` admits a transitive representation to `S4`
sending every positive generic meridian to a transposition, then
`Delta_aff(B) >= 3`.

Equivalently, no connected generically simply ramified quartic cover has an
irreducible `A1`-normalized complete branch curve with total affine delta at
most two.

For any reduced connected branch curve `B=V(q)` with squarefree `q`, the double
plane `D={s^2=q}` satisfies

`H^1_et(D,F3)^- = H^1_et(D,F3) ~= Pic(D)[3]`

and, after comparison over `C`,

`Pic(D)[3] ~= ker[H^1(A2-B,L_sign) -> direct_sum_p H^1(M_p,F3)]`.

This theorem makes no assertion for reducible branches, multi-place infinity
links, non-transposition inertia, disconnected covers, or total affine delta at
least three.

## Concrete successor

The cheapest exact falsification test is:

1. Produce an explicit charged branch curve or complete braid monodromy.
2. Compute the sign-specialized Fox matrix over `F3` for the affine complement,
   not just `det K_infinity`.
3. Exhibit a nonzero vector in the affine kernel.
4. Verify that its restriction to every double-plane singular link is zero.
5. Only then try to realize the survivor by the quartic/ruling/Keller gates.

A determinant-divisible infinity knot, a nonzero boundary Fox coloring, or a
punctured local `A2` class is not enough. The first real falsifier is a
nonzero vector surviving the full affine plus singular-link localization map.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15818`.
- Body SHA-256:
  `73e7405deb6e3530c3be461f2c92ded4f6839e2f92f3dc47371db769948b582a`.
- Frozen basis: `a9de85a3258e4c4128b873c23ae9eef08be8daba`.
