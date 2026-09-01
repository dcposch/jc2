# SHAPE-2-FINISH Hostile Review (GPT-5.5)

## Hash Verification

The frozen inputs were hashed before inspection with `shasum -a 256`.
All three values match the charge:

```text
ca016cdac79da2ba29ad6127fbb23e18c07c2d863e3c158b9b5db1baae0310e1  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.AOxbGv/inputs/shape-2-finish-sol56-20260901.md
0213fcae67bbde4d426a50f2d5d17c71db907d78718860459f14ff50e2ce4a01  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.AOxbGv/inputs/shape-kill-hostile-review-grok46-20260901.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.AOxbGv/inputs/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

The report below uses `SOL`, `GROK`, and `COORD` for those three frozen
files in charge order.  I did not inspect `jc2-lean`, did not edit any
charged or canonical ledger file, and ran no CAS or long computation.
No exit-price assertion is made.

## Scope And Method

Review posture was default refutation.  I checked only the charged frozen
copies and primary literature streams needed for the triple-cover and
delta-sequence claims.  The relevant external streams were hashed, not
saved:

```text
b37e8d45381a299e489516fd479ec896a016f06c402b16ae049d310aa1618153  https://arxiv.org/pdf/1211.2526v1
0bfbaaf77c3c795189d5645466dd3d3ee32b872f5c962309751142d65535f875  https://www.math.colostate.edu/~miranda/preprints/TripleCoversInAG.pdf
637acfd15d3d73b47f2ddc75b713063ee6e236ff6fef271417d96d5846d5a4c9  https://arxiv.org/pdf/0910.2613v2
808c7959381560b53a6c5c860d1ee3ef33a1cd9b2d956e91fb8dddf9c9575999  https://arxiv.org/pdf/math/0110110v1
```

Shirane and Miranda were used only for the normal triple-cover
Tschirnhausen structure, the branch-divisor determinant relation, and the
special degree-six classification.  Galindo-Monserrat was used for the
delta/maximal-contact conversion underlying SOL's family-2 valuation
calculation.  Ben-Itzhak-Teicher is corroborative for Hurwitz graph
invariants; the actual inner-braid conclusions below are checked directly.
No primary source inspected here gives the missing general-degree
index-one Cardano identity.

One custody note: SOL's own audit section records the frozen root and
input hashes from its production lane, not the current `AOxbGv` charge
(SOL:421-430).  I treat that as historical provenance only; the current
hash verification is the one in the previous section.

## Findings

No refutation found at the stated scope.  SOL should be promoted as a
scoped pin, not as a full family-2 kill.

The promoted content is:

1. consume the reviewed SK-2/SK-2' kill of the `g=2`, `(d,n)=(2u,2)`
   column only at `g=2`;
2. consume the reviewed SK-4 kill of `g=2`, `(d,n)=(2u,4)` for
   `u` odd and `u not congruent to 3 mod 6`;
3. promote the degree correction for the surviving `g=2`,
   `u=3k>=9` row: the branch degree is `d=2u=6k`, not `2u+4`;
4. promote resolvent descent for that surviving row, because the total
   product lies in `V_4`;
5. promote the conditional NO-TORUS proposition: assuming both affine
   `A_{2l-1}` exhaustiveness and an index-one Cardano equation
   `F=4A^3+27B^2` of degrees `(6k;2k,3k)`, the row contradicts the
   affine delta budget and the one-place infinity germ;
6. promote the `g=4`, product-one sub-stratum kill inside family 2;
7. keep the general `g>=3` family-2 case open at the actual inner word
   action.

The non-promoted content is equally important.  SOL does not prove that
all affine singularities in the residual row are odd `A` double points;
does not prove that the descended normal triple cover supplies an
index-one Cardano representative; and does not replace the actual
geometric inner braid by an arbitrary braid with matching exponent.  Those
are exactly the FALLACY-v2 failure modes this lane had to avoid.

## Consumption Scopes

The consumption of reviewed SK results is correct.

For `(d,n)=(2u,2)`, SOL only consumes the `g=2` two-transposition
block argument (SOL:396).  The reviewed source says exactly that: at
`g=2`, product-one blocks are diagonal, every `B_2` inner braid fixes
them, the outer cycle forces constancy, and the nontrivial block products
are confined to `S_3` or `V_4` rather than `S_4` (GROK:82-86).  This is
uniform in `u`, but not a statement about arbitrary `g` in the `(u,1)`
family.  SOL does not leak it into `g>=3`; later it explicitly treats
`g>=3` as open at the inner word (SOL:379-388, 401).

For `(d,n)=(2u,4)`, SOL uses the reviewed SK-4 scope: `g=2`, reduced
shape `(u,2)`, `u` odd, and the outer equation
`X W^m X = W^{m+1}` with `W=XY` (SOL:51-57; GROK:90-103).  The
reviewed `A_4` classification kills exactly `u not congruent to 3 mod 6`
and leaves `u congruent to 3 mod 6` as surviving outer data, with total
product a double transposition in `V_4` (SOL:58-66; GROK:126-144).  That
is a representation obstruction, not a delta-sequence census and not an
existence theorem for the surviving row.

The `(6,4)` row is also kept in its own compartment.  SOL marks
`u=3`, hence `(d,n)=(6,4)`, dead only by the already promoted explicit
ROW-NF/ROW-KILL input (SOL:398), not by the generalized
`u=3k>=9` valuation argument.

COORD's integration note still called SHAPE-KILL provisional and stated
that Tschirnhausen splitting "would close family 3" (COORD:44-50).
GROK already rejected the family-3 part (GROK:228-230, 267), and SOL does
not rely on it.  In SOL, Tschirnhausen splitting is only a sufficient
route to an index-one equation on the descended family-2 `g=2`,
`u=3k` row (SOL:158-163, 403-413).

## Generalized Torus And Valuation Route

This is the strongest part of SOL, and it is correctly typed as
conditional.

The route starts with the corrected degree.  In the surviving `g=2`
family-2 row, `u=3k` with `k>=3` odd and `(d,n)=(2u,4)`, so the branch
degree is `d=2u=6k` (SOL:47-49, 94-97).  This repairs the bad
`2u+4` degree count and removes the old divisibility contradiction:
`6 | d` is automatic (SOL:140-142).

The descent step is valid and degree-free.  The surviving outer tuples
have total product `Pi` a double transposition, hence `Pi in V_4`
(SOL:58-66).  Projectivising kills the infinity meridian, so the
composite `pi_1(A^2-D) -> S_4 -> S_3` factors through
`pi_1(P^2-\bar D)` (SOL:84-93).  The associated normal degree-three
quotient has generic transposition inertia along `\bar D`; in Shirane's
weighted branch notation this gives `T_pi=0` and `Delta_pi=\bar D`
(SOL:99-109).  The local `Z/3` unramified assertion is consumed only at
affine nodes, because the charged review had not checked tangential
`A_{2r-1}` points (SOL:111-117; GROK:200-210).

The triple-cover-to-torus step is exactly where the first hard stop
occurs.  Miranda's structure gives a rank-two Tschirnhausen module and
Shirane records `O(Delta_pi)=(det T_pi)^(-2)`, which here says only
`det T_pi=O(-3k)` (SOL:121-129).  A split triple-section model
`T_pi=O(-k) plus O(-2k)` would give
`F=4A^3+27B^2` with `deg A=2k`, `deg B=3k` (SOL:131-139), but neither
Miranda nor Shirane gives that split in general degree.  Shirane's
torus conclusion is special to `deg Delta=6`; SOL correctly refuses to
use it for `6k`, `k>1` (SOL:144-156).  Thus
`OPEN[SHAPE-2-CARDANO-INDEX-ONE]` is necessary unless a different
divisor-class argument on the double plane replaces it.

Assuming the index-one equation exists, the valuation proof checks out.
The Abhyankar-Moh delta sequence is forced to
`Delta=(6k,4,eta)` with `eta` odd, `3k<=eta<12k`, and
`2eta in <6k,4>`; the conductor calculation gives
`delta_aff=(6k+eta-3)/2`, and the maximal-contact conversion gives
local infinity data `(6k-4; 6k, 18k-eta)` (SOL:167-190).  I find no
missing branch in this enumeration: the gcd chain is `6k,2,1`, and once
gcd one is reached there is no further nontrivial delta quotient.

The second hard stop is affine exhaustiveness.  Under the hypothesis
that every affine singularity is an `A_{2l-1}` pair of smooth branches
(SOL:192-199), each affine common zero of `A` and `B` contributes
`delta_P=3r_P/2`, so with `sum r_P=2s` one obtains
`3s<=delta_aff` (SOL:207-220).  Bezout then forces
`I_Q(F,A)>12k^2-12k+2` at infinity (SOL:222-232).  The local weights
`(6k-4,6k)=2(3k-2,3k)` make the least term of `A` unique; divisibility
forces total degree `q=2k` (SOL:234-244).  The two Newton-face cases
then both contradict one-place behavior at infinity: with `j=0` the
face is not a square, and with `j>0` the toric transform splits into two
analytic branches (SOL:246-268).

Without affine `A`-odd exhaustiveness, the base-point delta estimate can
fail, so the lower bound at infinity is not forced.  SOL's explicit
torus negative control has the same infinity orders and a valid
`Delta=(6k,4,9k)` but positive normalization genus, so it proves exactly
that infinity data alone cannot close the row (SOL:270-302).

## g >= 3 Inner Analysis

SOL's correction of the earlier `g=2` intuition is sound.  For a block
`T=(t_1,...,t_g)`, the left Hurwitz generator sends
`(t_i,t_{i+1})` to `(t_i t_{i+1} t_i^{-1},t_i)`.  It fixes that adjacent
pair exactly when `t_i=t_{i+1}` (SOL:304-314).  Thus the argument used
for `g=2` product-one blocks does not extend: for even `g>=4`,
product one does not imply a diagonal block, and for odd `g` product one
is impossible by sign (SOL:316-320).

The proposed invariant is the right one for this level of information:
work on the labeled Hurwitz fiber, with the stabilizer of the actual
block tuple, not on the block product alone.  Hurwitz moves preserve the
component vertex sets of the factor graph and the ordered product
(SOL:322-338).  Because `u` is odd, the shift `i -> i+2` is a single
cycle on the `u` blocks, so fixedness requires the actual inner word to
transport each labeled fiber around that cycle and return inside the
starting stabilizer (SOL:329-338).

The `g=4`, product-one sub-stratum kill is valid.  A connected graph on
four letters with transposition product one needs at least six factors:
three joins are needed to connect four letters, and the cycle count must
be cut back by the same number to return to the identity.  With only four
factors the factor graph is disconnected, hence the block subgroup is a
proper Young subgroup.  Since Hurwitz transport preserves the labeled
support partition and the block shift is one cycle, every block remains
inside the same proper subgroup, so the total image cannot be `S_4`
(SOL:340-345, 399-400).

The remaining `g>=3` case cannot be killed by product or exponent data.
SOL's witness blocks have the stated products and generate `S_4`:
`((12),(34),(23))` has product `(1243)` at `g=3`;
`((23),(23),(12),(34))` has product `(12)(34)` for even `g>=4`; and
`((34),(34),(23),(23),(12))` has product `(12)` for odd `g>=5`, with
padding by equal pairs preserving product and generation (SOL:352-360).
Repeating the same block gives `X=Y=c`, hence the outer relation holds.

The exponent adjustment also survives review.  The full twist
`Z_g=(sigma_1...sigma_{g-1})^g` has exponent `g(g-1)` and acts by
simultaneous conjugation by the block product; SOL's cabled
`delta_u^2` formula then gives a fixed repeated tuple after placing
`Z_g^{-u}` in the last two inner components (SOL:362-370).  For
`g>=4`, an equal adjacent pair supplies a stabilizer of exponent one, so
the total exponent can be adjusted arbitrarily.  For `g=3`,
`sigma_1^2` stabilizes the first disjoint pair, and the required
geometric exponent is even (SOL:371-377).  This proves only that the
known exponent is non-obstructive.

SOL keeps the decisive distinction: these are abstract tubular fixed
tuples, not residual curves and not the actual geometric inner braid
(SOL:379-388).  Therefore the open problem is correctly word-level:
recover the real inner Nielsen action from Puiseux/resolution data and
test it on the product-indexed labeled fibers.

## OPEN Necessity

`OPEN[AFFINE-ALL-A_ODD]` is necessary.  The valuation kill needs the
local formula `delta_P=3r_P/2` at affine common zeros of `A` and `B`,
which SOL derives only under the hypothesis that the affine singularity
is an `A_{2l-1}` pair of smooth branches (SOL:192-219).  GROK had
already warned that the earlier local `Z/3` argument was nodal and did
not cover tangential `A` points (GROK:200-210).  Without this OPEN, the
affine delta budget does not force enough intersection to occur at
infinity.

`OPEN[SHAPE-2-CARDANO-INDEX-ONE]` is necessary.  Resolvent descent gives
a normal degree-three cover, but the branch determinant relation gives
only `det T_pi=O(-3k)` (SOL:121-129).  A global equation
`F=4A^3+27B^2` with `deg(A,B)=(2k,3k)` follows from a split
triple-section model, not from normality alone (SOL:131-156).  The
missing point is also weaker than full Tschirnhausen splitting: it asks
for an index-one branch representative, or an equivalent divisor-class
statement on the double plane (SOL:158-163).

`OPEN[INNER-NIELSEN-WORD-ACTION]` is necessary.  The `g>=3` analysis
exhibits `S_4`-generating abstract fixed tuples with the correct outer
relation and adjustable total exponent (SOL:352-377).  Since those
tuples are not generated from the actual Puiseux/resolution braid, they
are counterexamples only to coarse attacks, not witnesses for residual
curves.  The remaining obstruction must see the actual word action
(SOL:379-388).

Two inherited route labels should remain typed but not overpromoted.
`OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]` is a sufficient way to obtain the
index-one equation in the descended `g=2`, `u=3k` family-2 row, but it is
stronger than SOL needs and does not close family 3 non-constant
(SOL:403-413; GROK:224-230).  `OPEN[SHAPE-2-INFINITY-Z3]` is the direct
double-plane alternative: it would have to account for the infinity
singularity and tangential affine `A` points, not just nodal local
inertia (SOL:407-413).

## Promotion Recommendation

Recommendation: **PROMOTE SOL as scoped**.

Promote:

| Item | Recommendation |
|---|---|
| `(2u,2)` column | Promote the uniform kill only at `g=2`, as consumed from reviewed SK-2/SK-2'. |
| `(2u,4)`, `u not congruent to 3 mod 6` | Promote the uniform `g=2` kill from the reviewed `A_4` outer classification. |
| `(2u,4)`, `u congruent to 3 mod 6`, `u>=9` | Promote the correction `d=2u=6k`, the `S_3` resolvent descent, and the conditional NO-TORUS obstruction under the two stated hypotheses. |
| `g=4`, `X=Y=1` family-2 sub-stratum | Promote the support-partition kill. |
| General `g>=3` family 2 | Promote only the pin: outer/exponent data are non-obstructive; the case remains open at the actual inner word action. |

Keep open:

| OPEN | Status |
|---|---|
| `OPEN[AFFINE-ALL-A_ODD]` | Necessary for the affine delta estimate in the torus contradiction. |
| `OPEN[SHAPE-2-CARDANO-INDEX-ONE]` | Necessary to turn the descended normal triple cover into the exact torus equation used by the valuation proof. |
| `OPEN[INNER-NIELSEN-WORD-ACTION]` | Necessary for the `g>=3` family-2 inner analysis. |
| `OPEN[TRIPLE-COVER-TSCHIRNHAUS-SPLIT]` | Keep as a sufficient route to Cardano index one, not as a consumed theorem and not as a family-3 closure. |
| `OPEN[SHAPE-2-INFINITY-Z3]` | Keep as the direct double-plane route, with tangential affine points and the infinity singularity included. |

Do not promote: existence of any residual curve in the surviving
`u=3k>=9` row; a kill of general family 2 at `g>=3`; a Cardano
divisibility kill; Shirane's degree-six classification outside degree
six; or COORD's obsolete parenthetical that Tschirnhausen splitting would
close family 3.

Final verdict: SOL is a valid narrowing and pinning report.  It closes
the charged `g=2` killed scopes, explains exactly why the generalized
torus route stops, and leaves the remaining obstructions typed rather
than filled by analogy.

<!-- BODY-END -->
