# Hostile review: conductor-10/16 genus-ladder S4 obstruction

Date: 2026-08-31 UTC  
Reviewer: Grok 4.6 (independent different-model audit)  
Assignment: `xmodel/block-descent-a1-genus-ladder-conductor10-16-hostile-review-grok46-20260831.prompt.md`  
Assignment SHA-256: `b2866480d49afebb54593b55be40cb78d4bc2876a0f02e7294e704922934951b`  
Frozen basis named in the charged artifact: `c0d1c47f5b5f8b8db243ce0499719316285d0958`

## Verdict

**CONFIRM**

The claimed one-place obstruction is true at its exact charged scope. The
Assi--Garcia-Sanchez reduced axioms, the Section 5 recursion, the
conductor-14 published control, the conductor-10 and conductor-16 censuses,
the four-row cabling dictionary, the signed zero-framed satellite braids,
every labelled full-`S4` count, and the residue theorem

```text
C_(2,q)(T(2,n)) has a full-S4 transposition colouring
iff 3 divides n and 3 divides q
```

all survive independent re-derivation. No missing delta-sequence, wrong
reducedness inequality, swapped cable parameters, blackboard-framing error,
full-image filter error, or embedding-versus-abstract-semigroup overclaim
was found. No downstream promotion is implied. This review asserts no new
exit price.

## Custody

Every charged SHA-256 was reproduced before the corresponding file was read.

```text
e802ab6bcca9a27058ca8b33232f56e5abdd9f90df1c60c28d308fad0cd9a863
  xmodel/block-descent-a1-genus-ladder-conductor10-16-s4-obstruction-sol56-20260831.md
373aa3b1790084848710291d09b5b4af7840818242833a6faf94f71b44c1b33f
  xmodel/block-descent-a1-genus-ladder-conductor10-16-s4-obstruction-sol56-20260831.md.artifact.json
a076e204121e1ed291edab8a94b09a9832afd3f04fda2a10cd94d36e5397258a
  ops/block_descent_a1_genus_ladder_s4_replay.py
03865aae3cc11a5f7de264ef7a66d1e3600ccb983ea8f95079c50d8a28b0b5aa
  xmodel/block-descent-a1-total-delta-two-iterated-knot-s4-obstruction-sol56-20260830.md
03b16c2deba48605482963ae7f98f5e74aca26ce0e1761bbeab653a164bec4b4
  xmodel/block-descent-a1-genus-three-cable-b1-obstruction-sol56-20260830.md
070faa884a26b0c96aaacafa7738cb39746407803d156a5a327d360eabf613e5
  xmodel/block-descent-a1-genus-four-cable-b1-obstruction-sol56-20260831.md
```

All six matched. No charged file, canonical ledger, or `jc2-lean` tree was
edited or inspected. The Assi--Garcia-Sanchez arXiv `1407.0490v1` PDF was
fetched independently; its SHA-256 is
`05081acd04a51c85d231ff288c8522b83e79d75b28af7f99868c2f5149683bf9`,
which agrees with the hash recorded in the charged genus-three artifact.

The obstruction body is 9942 bytes through its unique body-end marker,
SHA-256
`5930919f3abf7d4d79566b30a66cb103c724d922930d1b2a00eade0a67c995c5`,
matching the artifact JSON.

## Exact theorem

Let `B` be a reduced irreducible complex affine plane curve with
`normalization(B)=A1`. Suppose `pi1(A2-B)` admits a transitive representation
to `S4` sending every positive generic meridian to a transposition. Then

```text
Delta_aff(B) != 5 and Delta_aff(B) != 8.
```

Equivalently: the complete reduced one-place delta-sequence lists at
conductors 10 and 16 are

```text
conductor 10:  (11,2), (6,4,7),
conductor 16:  (17,2), (10,4,9);
```

their infinity knots are `T(2,11)`, `C_(2,7)(T(2,3))`, `T(2,17)`, and
`C_(2,9)(T(2,5))` respectively; and every sign and companion-mirror version
of each of these four knots has zero labelled full-`S4` meridian-transposition
colourings. The meridian-preserving surjection from the infinity-knot group
onto the affine complement group therefore contradicts the charged quartic
monodromy.

The statement does not assert that one-place curves of affine delta five or
eight fail to exist. Assi--Garcia-Sanchez Example 5 already exhibits a
one-place polynomial whose approximate-root sequence is `(6,4,7)`. The
obstruction is only the required `S4` boundary representation.

This is not an exit-price assertion.

## 1. Assi--Garcia-Sanchez axioms and completeness of the recursion

A sequence `(a0,...,as)` of coprime nonnegative integers, with `D1=a0` and
`D_k=gcd(D_{k-1},a_{k-1})`, is a delta-sequence in the sense of the
definition immediately before their Proposition 13 if and only if

1. `<a0,...,as>` is free with respect to that arrangement
   (`e_k a_k` lies in the prefix semigroup, and `e_k` is the least such
   multiplier);
2. `a_k D_k > a_{k+1} D_{k+1}` for `1<=k<=s-1`;
3. `a0 > a1 > D2 > D3 > ... > D_{h+1}=1`.

Proposition 2(ii)--(iv) records the same freeness, the same Newton
inequalities (reindexed as `r_{k-1} d_{k-1} > r_k d_k` for `2<=k<=h`), and
the conductor formula

```text
C = sum_k (e_k-1) r_k - r0 + 1.
```

The replay's `is_delta_sequence` implements exactly these three clauses.
Membership of `e_k r_k` in the prefix semigroup automatically makes `e_k`
minimal: every prefix element is divisible by `d_k`, and
`gcd(r_k/d_{k+1}, d_k/d_{k+1})=1`. The reduced chain `r0>r1>d2` together
with strict decrease of the gcd tower is (3). The product test
`r_k d_k > r_{k+1} d_{k+1}` is (2). There is no off-by-one between
Proposition 2, the delta-sequence definition, and the code.

The stronger Opus wording `r_k/d_{k+1}>=2` is implied by reducedness on
every sequence that actually arises. Because `d_{k+1}` divides `r_k`, the
ratio is an integer, and the only integer below 2 that could occur is 1,
i.e. `r_k=d_{k+1}`. For `k=1` this contradicts `r1>d2`. For `k>=2` it
forces the prefix (divided by `d_k`) to contain 1, hence to have conductor
0, which the `h>1` recursion excludes. Independently, every sequence in
the conductor-6, 8, 10, 14, and 16 lists satisfies the stronger bound, so
replacing the Opus wording by the exact definition changes none of those
lists. The interface correction is exact and numerically idle on the
charged range.

Section 5 of the paper is the recursion the replay implements. For `h=1`,
`C=(r0-1)(r1-1)`. For `h>1`, Proposition 4(ii) at `k=h` is

```text
C = d_h C_prefix + (d_h-1)(r_h-1),
```

with `gcd(d_h,r_h)=1`, `2<=r_h<=C-2`, and `2<=d_h<=C/(r_h-1)+1`. These
bounds are complete: `r_h=1` would require a conductor-zero prefix;
`r_h=C-1` would require a conductor-one prefix, and no symmetric numerical
semigroup has conductor 1; the upper bound on `d_h` is the positivity of
the remainder. The enumeration is therefore a finite complete recursion,
not a guessed coordinate box.

As a primary-source control, the implementation reproduces Example 18 of
the paper on the nose. Their GAP call `DeltaSequencesWithFrobeniusNumber(13)`
prints the ten sequences of conductor 14, in the same order the replay
uses:

```text
(6,4,11), (8,3), (8,6,3), (9,6,5), (10,4,7),
(12,8,3), (12,8,6,3), (15,2), (15,6,2), (15,10,2).
```

Independently of the recursion, every tuple of length 2 through 5 with
entries in `{1,...,C+1}` was tested against the three axioms at
`C in {6,8,10,14,16}`. The brute-force lists equal the recursive lists,
including the previously charged conductor-six and conductor-eight rows
and the two new rows at each of 10 and 16. The box is large enough:
Remark 17 gives `r0>=sqrt(C)+1`, the torus row `(C+1,2)` gives
`r0<=C+1`, and `r_h<=C-2`. The height bound `C>=2(2^h-1)` from their
citation of Assi, *C. R. Acad. Sci.* 1994, Proposition 6.7, allows
`h<=3` at conductor 16, so length-four sequences are possible in
principle (conductor 14 realises one, `(12,8,6,3)`). None exists at
conductors 10 or 16.

Dropping freeness or dropping the product ordering changes the control
censuses, as claimed. The extras inside a slightly larger box include

```text
C=10, no freeness:   (10,4,3),
C=16, no freeness:   (8,6,5), (14,4,5), (12,8,6,5), ...
C=16, no ordering:   (6,4,13).
```

The row `(8,6,5)` would be the winding-two cable `C_(2,5)(T(3,4))`, a
satellite of a knot already known to have 24 full-`S4` colourings, and it
is a six-strand braid the winding-two/two-braid compiler would never see.
Freeness is therefore load-bearing against a genuine group-level threat,
not a cosmetic filter. It is nonetheless the primary-source axiom, so
excluding that row is correct.

## 2. Conductor-10 and conductor-16 censuses, and the four knots

One-stage solutions of `(r0-1)(r1-1)=C` with `r0>r1>1` and coprimality
are exactly `(11,2)` at conductor 10 and `(17,2)` at conductor 16. No
`T(3,*)` or `T(4,*)` occurs: `(6,3)` is not coprime, and `(5,3)` has
conductor 8.

The three-term solutions that pass all three axioms are exactly `(6,4,7)`
and `(10,4,9)`. Schubert's formula on the converted cables returns genus
5 and 8 respectively, matching `C=2g`. The remaining topological
genus-five and genus-eight satellites fail freeness; typical corpses are
`(14,4,5)=C_(2,5)(T(2,7))` and `(8,6,5)=C_(2,5)(T(3,4))`.

The Puiseux/cabling dictionary used by the obstruction is the same one
already charged at conductors six and eight. For a three-term sequence
with `d=gcd(r0,r1)`, the normalised prefix is the companion torus knot
`T(r1/d, r0/d)` and the last stage is a winding-`d`, meridional-`r_h`
cable. Thus

```text
(11,2)   -> T(2,11),
(6,4,7)  -> C_(2,7)(T(2,3)),
(17,2)   -> T(2,17),
(10,4,9) -> C_(2,9)(T(2,5)).
```

The torus-coordinate order is harmless: `T(2,3)=T(3,2)` and `T(2,5)=T(5,2)`
as knots, and the economical 2-braid presentation is the one subsequently
cabled. Swapping cable parameters would break genus: `C_(7,2)(T(2,3))`
has genus 10, not 5. The written order is the only one compatible with
Schubert and with the charged `(6,4,3)=C_(2,3)(trefoil)` and
`(6,4,5)=C_(2,5)(trefoil)` rows.

Assi--Garcia-Sanchez Section 6 (Examples 20 and 22, Remark 21) shows that
isomorphic one-place curves can have inequivalent embeddings and different
delta-sequences. The obstruction enumerates sequences, not semigroups.
That is the correct object: Example 18 itself has ten sequences and only
five distinct semigroups. Two embeddings of one abstract coordinate ring
would still both appear in the census, and both knots are killed. There is
no embedding-versus-abstract overclaim. Reduction of a non-delta
characteristic sequence (their Example 12) shortens the sequence while
preserving the semigroup and, after deleting winding-one and
unknot-producing steps as in the charged total-delta paper, preserves the
knot type.

## 3. Signed cable braids, framing, closure, and Alexander control

The Artin action is the charged convention

```text
sigma_i : (A,B) |-> (A B A^{-1}, A),
```

with inverse `(A,B)|->(B, B^{-1} A B)`. The positive permutation braid
interchanging two blocks of two strands is obtained by bubble-sorting
`(0,1,2,3)` to `(2,3,0,1)` and equals `X=sigma2 sigma3 sigma1 sigma2` on
the nose, matching the genus-three predecessor. The zero-framed word

```text
C_(2,q)(T(2,n)) : X^n sigma1^(q-2n)
```

is the same blackboard-framing correction used for trefoil companions:
the 2-braid `sigma1^n` has writhe `n`, so the blackboard 2-parallel
contributes `2n` to the meridional parameter, and `sigma1^(q-2n)` restores
zero framing. Negative exponents are inverse words.

Every one of the eight sign/mirror instances closes to a single 4-cycle,
hence to a knot. An independent reduced-Burau calculation returns, up to
Laurent units, the Seifert--Schubert cable polynomial

```text
Delta_T(2,q)(t) * Delta_T(2,n)(t^2)
```

for all eight. The numerator identity used in the replay,
`(1-t) det(I-Burau_red) = Delta(t) (1-t^4)`, is the standard
`s`-braid formula with `s=4`. This checks both the block switch and the
framing correction before any colouring verdict is consumed. The braid is
the geometric cable, not an Alexander homonym.

The opposite Hurwitz convention was enumerated separately on the two
charged cables and on the conductor-six positive control. It returns the
same counts `0,0,72`. The convention is therefore not a hidden degree of
freedom in the vanishing.

## 4. Full-`S4` counts and the winding-two residue theorem

Simultaneous conjugation acts transitively on the six transpositions of
`S4`, and the Artin action is equivariant, so fixing the first colour and
multiplying by six is exact for labelled counts. Independently, the
two-strand torus rows were exhausted without that shortcut (`6^2=36`
states) and still return zero. The two charged positive cables were
likewise exhausted without the shortcut (`6^4=1296` states) and still
return zero.

A transposition-generated subgroup of `S4` is the full `S4` if and only if
it is transitive on four letters, if and only if the corresponding graph
on four vertices is connected. Checking `|G|=24` is therefore equivalent
to transitivity, and is the correct full-image filter. The filter is live:
`C_(2,+7)(T(2,+3))` admits one first-colour-`(12)` fixed colouring, which
is not transitive and is correctly discarded. No determinant-only
inference is used. That last point is load-bearing for one row:

```text
det T(2,11)=11,   det T(2,17)=17,
det C_(2,7)(T(2,3))=7,
det C_(2,9)(T(2,5))=9.
```

The double-cover lemma of the charged total-delta paper is one-way: a
full-`S4` transposition representation forces `3|det`. It kills the first
three rows and does not kill the fourth. The vanishing of the labelled
count on `C_(2,9)(T(2,5))` is the actual obstruction there.

Two transpositions generate a subgroup of order at most six, so no
two-meridian generating set can be transitive on four letters. This
kills every two-bridge knot, hence every `T(2,q)`, without enumeration.
A nontrivial satellite is never two-bridge, so the same floor does not
touch the two cable rows; those require the four-strand count.

On the set of all `6^4` transposition-valued four-strand states, the
action of `X` has order 12 and the action of `sigma1` has order 6. The
word `X^n sigma1^(q-2n)` therefore depends only on `n mod 12` and
`q mod 6`. Odd knot exponents reduce to the six-by-three table of odd
residues. Every cell with `3|n` and `3|q` has labelled count 72; every
other cell has count 0. Negative exponents are identified with the same
table because `X^{-1}` acts as `X^{11}` and `sigma1^{-1}` acts as
`sigma1^5`, and `3|n` is invariant under `n <-> n mod 12` on odd
residues. Direct sign-by-sign enumeration of the four charged cables
confirms the table on those geometric words, not merely on residue
representatives.

The conductor-six survivor `C_(2,3)(trefoil)` is the cell `(n,q)=(3,3)`,
count 72, matching the charged genus-three table on all four
sign/chirality versions. The two new cables die for different reasons:
`7` is not divisible by three, while in `C_(2,9)(T(2,5))` it is the
companion exponent `5` that is not.

## 5. Meridian surjection and maximum-safe scope

The charged total-delta paper supplies three interfaces, all consumed and
none re-proved here:

- `g_3(K_infinity)=Delta_aff(B)`, from the nearby-fibre Euler
  characteristic and Neumann 1989, Theorem 1;
- `K_infinity` is the unknot or a prime iterated cable, from Rudolph's
  parametrized cabling / Neumann's rooted valency one, plus Schubert
  primeness;
- `pi1(S3-K_infinity) ->> pi1(A2-B)`, meridians preserved, because
  Zariski--van Kampen imposes each local braid relation while the closed
  boundary braid imposes only the total word.

Assi--Garcia-Sanchez Lemma 3 identifies the conductor with `mu(f)=2g` of
a smooth pencil member. For an `A1`-normalised special fibre the charged
genus formula then gives `C=2 Delta_aff(B)`, so conductors 10 and 16 are
exactly affine delta 5 and 8.

The surjection is used in the only direction an obstruction needs: a
meridian-transposition representation of the affine complement pulls back
to one of the knot group. Zero knot colourings imply zero affine
colourings. Because all meridians of a knot are conjugate, and conjugates
of transpositions are transpositions, it is enough to colour the strand
meridians of a closed braid. `Aut(S4)=S4`, so there is no outer embedding
of the target that the labelled count could miss.

The following are not used and not obtained.

- `b1(B)=1`. Unlike the genus-three and genus-four predecessors, both
  new cables already die at the boundary colouring, so the Betti
  constraint is idle. The theorem is therefore strictly stronger than a
  `b1=1` packet statement.
- Existence or non-existence of a one-place curve of delta 5 or 8.
- Reducible branches, forests, more than one place at infinity, or
  non-`A1` normalisation.
- Non-transposition inertia, disconnected covers, or degree other than
  four.
- Nonminimal rank-four packets, higher-rank blocks, a finite algebraic
  cover, a proper block, a Keller map, or JC2.
- An all-genus vanishing. Other conductors contain winding-three and
  deeper rows, and the winding-two/two-braid theorem itself produces
  survivors as soon as `3` divides both exponents.

FALLACY-v2 is idle on this artifact: there is no flag/place/series
identification, no `sat()` identity, no pole-class identity, no
merge-free `M`-descent, no target/arrival-index comparison, and no
floor treated as attainment. The colouring counts are exact enumerations.
The identification `g_3=Delta_aff` is consumed as a charged equality, not
as a lower bound.

## 6. Replay

Interpreter: CPython 3.14.7. The replay contains no `assert` statements;
checks are `require()` and survive `-O`/`-OO`. Ordinary, `python3 -O`,
and `python3 -OO` executions are byte-identical:

```text
stdout SHA-256:
b2a4418172aab4834fef9b1e09cffa2e921132770e4029d6f532e8c6b3ee437c
payload_sha256:
1061ea3423bd77c208419f39beb3ad0a597b4ee85865f539ed67b90228fe50ba
status=PASS-A1-GENUS-LADDER-CONDUCTOR-10-16-S4-OBSTRUCTION
```

The three mutations exit nonzero at their intended gates:

- `--mutate-drop-freeness` fails the recursive census;
- `--mutate-drop-ordering` fails the recursive census;
- `--mutate-promote-cable-coloring` fails the vanishing of the cable
  counts, after forcing the `(2,+7)` companion-positive row to 72.

Runtime is well under two seconds. No CAS, numerical root finder, heavy
process, or AWS capacity is used.

The replay proves the finite arithmetic, the conductor-14 control, the
two-transposition order bound, knot closure of every charged braid, the
cable Alexander polynomials, the labelled colouring table, the action
orders 12 and 6, and the six-by-three residue table. It does not prove
Schubert genus or primeness, Neumann--Rudolph goodness, the nearby-fibre
Euler identity, the infinity-to-affine surjection, or the Assi--Garcia-Sanchez
existence theorem. Those remain the written primary interfaces.

## Remaining assumptions

The following are assumptions, not theorems of the present artifact.

- The three charged total-delta interfaces listed in Section 5, including
  goodness of a one-place reduced equation and the identification of the
  compact nearby fibre with the minimal Seifert surface.
- Characteristic zero, as in Assi--Garcia-Sanchez, and complex (not
  merely topological) orientation of the one-place branch. Extra braid
  signs are retained only as a stronger screen.
- That every abstract iterated knot need not be polynomially realisable:
  the argument never claims the converse, and uses AGS freeness to
  discard the non-realisable rows.

## Maximum safe statement, blast radius, and repair

**Safe statement.** There is no reduced irreducible complex affine plane
curve `B` with normalisation `A1`, one place at infinity, affine delta
invariant 5 or 8, and a transitive meridians-to-transpositions
representation `pi1(A2-B)->S4`.

**Blast radius.** This closes the irreducible one-place charged quartic
`S4` boundary at affine delta 5 and 8, including the `b1>=2` embeddings
in those degrees, before any approximate-root normal form or
normalisation-pair count is needed. It does not:

- exclude existence of one-place curves of those deltas;
- exclude reducible branches, forests, or more than one place at
  infinity;
- exclude non-transposition inertia, disconnected covers, or degree
  other than four;
- treat conductor 12 / genus six, or any higher iterated cable;
- construct or exclude a finite algebraic cover, a proper rank-four
  block, or a Keller map;
- prove JC2, rank-four emptiness, or anything about primitive packets.

**Repair.** None required. Presentation nits that do not affect the
theorem: prose (0.2) lists the torus row first while the replay sorts
tuples lexicographically; the drop-freeness mutation tests only that the
census changes, and does not colour the six-strand extra `(8,6,5)`; one
non-transitive transposition colouring of `C_(2,+7)(T(2,+3))` exists and
is correctly discarded by the full-image filter. None of these is an
invalid implication.

**Best next falsification test.** Independently enumerate the
conductor-12 reduced delta-sequences and their full-`S4` colourings. A
complete box at conductor 12 yields exactly

```text
(5,4), (6,4,9), (7,3), (9,6,4), (10,4,5), (13,2).
```

The winding-two theorem already predicts that `(6,4,9)=C_(2,9)(T(2,3))`
has 72 labelled colourings, so the pure boundary sieve of the present
artifact fails at the very next even conductor. The remaining honest
work at genus six is therefore the 3-braid row `T(3,7)`, the winding-three
row `C_(3,4)(trefoil)`, and a genus-three-style approximate-root /
normalisation-pair attack on the winding-two survivor `(6,4,9)`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `21096`.
- Body SHA-256:
  `d58e15bd828147a1c486823d761f349cb0b7fa96d0e4120a996e095c183d2fe4`.
