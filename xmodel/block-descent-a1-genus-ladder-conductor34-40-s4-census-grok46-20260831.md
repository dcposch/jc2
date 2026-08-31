# Genus ladder through conductor 40: exact S4 census at the next even rungs

Date: 2026-08-31 UTC  
Author: Grok 4.6 (`genus_ladder_c34_c40` lane)  
Lifecycle: **PROVISIONAL** (depends on two parent packets that the coordinator
labels PROVISIONAL / different-model review required)

## 0. Theorem and exact verdict

Let `B` be a reduced irreducible complex affine plane curve in the charged
one-place packet.  Assume

```text
normalization(B)=A1
```

and assume that `pi1(A2-B)` has a transitive representation to `S4` sending
every positive generic meridian to a transposition.  Then the complete
reduced delta-sequence rows of even conductors `30,32,34,36,38,40` are the
lists in Section 4, and the labelled full-`S4` meridian-transposition counts
are the numbers displayed there.  In particular the next two terms of the
parent complete-exclusion progression are **not** exclusions:

```text
Delta_aff(B) = 17 is compatible with the boundary gate
  via the unique conductor-34 survivor (12,8,14,15), labelled count 72;
Delta_aff(B) = 20 is compatible with the boundary gate
  via three conductor-40 survivors, labelled counts 72, 24, 72.     (0.1)
```

The parent complete-exclusion list (**PROVISIONAL**)

```text
Delta_aff = 5, 8, 11, 14
```

is therefore **not** extended by this computation.  The arithmetic
progression `C = 10+6k` is not a theorem past conductor 28: it is a pattern
in four previously computed rungs, and the first two further terms fail it.
Zero-count rows at the six computed conductors remain excluded from carrying
the charged quartic boundary representation.  Positive-count rows are not
existence theorems; they are exact compatibility of the compiled infinity
knot with a full-`S4` transposition colouring.

This does **not** exclude one-place curves of any displayed genus.  It does
not address reducible branch curves, several places at infinity,
normalization other than `A1`, nonminimal rank-four packets, higher-rank
blocks, odd conductors, conductors larger than 40, or JC2 itself.  Every
numerical claim below that consumes a parent census, compiler convention, or
colouring criterion is **PROVISIONAL**.

## 1. Frozen-input hashes and next conductors

Every parent byte was read from the coordinator-frozen copies in
`/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.3TUzlG/inputs`.
SHA-256 was checked before any mathematical consumption:

```text
e802ab6bcca9a27058ca8b33232f56e5abdd9f90df1c60c28d308fad0cd9a863
  block-descent-a1-genus-ladder-conductor10-16-s4-obstruction-sol56-20260831.md
  PROVISIONAL

1500eeb24e1a9f4b2d27daeca85f6ed735a962ae2f7d26e8f923f38ea7d1de7a
  block-descent-a1-genus-ladder-conductor12-14-18-20-22-28-s4-census-sol56-20260831.md
  PROVISIONAL

a076e204121e1ed291edab8a94b09a9832afd3f04fda2a10cd94d36e5397258a
  block_descent_a1_genus_ladder_s4_replay.py
  PROVISIONAL (pinned arithmetic core)

e01c7815a9ef3be93305ae54d7cdc2747e0e11909f9185031fd2762c4605367b
  block_descent_a1_genus_ladder_next_s4_replay.py
  PROVISIONAL (pinned braid compiler and V4/S3 counter)
```

All four hashes matched.  Workspace copies of the two replay scripts were
byte-identical to the frozen copies.  No charged file, canonical ledger, or
`jc2-lean` tree was edited or inspected.

The first parent treats even conductors `10` and `16`.  The second parent
states that, together with those two rungs, it supplies "the complete
even-conductor ladder through 28", with explicit list
`(12, 14, 18, 20, 22, 24, 26, 28)` and with `Delta_aff = C/2` on every
displayed row.  That identification is the packets' translation of the
charged one-place interface `g_3(K_infinity) = Delta_aff(B)` through
symmetry of a one-place-at-infinity numerical semigroup.  Odd conductors
are outside both parent censuses; this lane does not add them.

The complete-exclusion rungs already recorded by the parents
(**PROVISIONAL**) are `C = 10, 16, 22, 28`.  That is the arithmetic
progression `C = 10+6k`, whose next two terms are `34` and `40` — the
source of the expected pair.  The second parent does **not** compute only
those progression terms.  It classifies every intervening even conductor,
and it uses the surviving rows at `24` and `26` to refuse a monotone
extrapolation from `22` to `28`.  The same refusal is an explicit axiom of
this lane.

Therefore the packets' own parametrization of the next complete even
ladder is

```text
C in {30, 32, 34, 36, 38, 40},
Delta_aff in {15, 16, 17, 18, 19, 20}.
```

This **differs** from the two-term expectation `{34, 40}`.  Conductors `34`
and `40` remain the next two complete-exclusion *candidates*.  Conductors
`30, 32, 36, 38` are required intervening rungs.  No claim in this report
extrapolates past a computed conductor.

The exact Assi--Garcia-Sanchez axioms consumed below are those of the first
parent replay (**PROVISIONAL**):

```text
d1 = r0, d_(k+1) = gcd(d_k, r_k), e_k = d_k / d_(k+1),
e_k * r_k in <r0,...,r_(k-1)>                         (freeness),
r_k * d_k > r_(k+1) * d_(k+1) for 1 <= k < h          (ordering),
r0 > r1 > d2 > d3 > ... > d_(h+1) = 1                 (reducedness),
C = sum_k (e_k-1) r_k - r0 + 1                        (conductor).
```

The complete recursion is the one-stage identity `C = (r0-1)(r1-1)` together
with the higher-stage reconstruction

```text
C = d_h * C_prefix + (d_h-1)(r_h-1),
2 <= r_h <= C-2,
2 <= d_h <= C/(r_h-1)+1,
gcd(d_h, r_h) = 1.
```

Dropping freeness or dropping product ordering is a fail-closed mutation in
the parent core; this lane keeps both inequalities.

## 2. Complete recursive census

The enumeration is the parent recursion, not a coordinate box.  As a
primary-source control it reproduces the ten conductor-14 delta-sequences
printed in Assi--Garcia-Sanchez Example 18, in the same sorted list, and it
reproduces the parent conductor-28 list (**PROVISIONAL**) before any new
row is consumed.  Census sizes at the six targets are

```text
C=30: 28 rows, max r1=18, max length 5
C=32: 29 rows, max r1=22, max length 4
C=34: 13 rows, max r1=14, max length 4
C=36: 26 rows, max r1=16, max length 5
C=38: 41 rows, max r1=26, max length 5
C=40: 15 rows, max r1=12, max length 4
```

Total 152 reduced sequences, far below the 50,000 freeze threshold.
Enumeration itself is under a hundredth of a second.  Every enumerated row
satisfies the exact reduced axioms and reconstructs its target conductor.

Two one-stage checks, by hand.  For `C=34` the factorisation
`(r0-1)(r1-1)=34` with `r0>r1>gcd(r0,r1)` and last gcd equal to 1 yields
only `(35,2)`.  For `C=40` it yields `(41,2)` and `(11,5)`.  Both match
the recursion.  The unique conductor-34 survivor is the four-term sequence
`(12,8,14,15)`:

```text
gcds = (12, 4, 2, 1),
e = (3, 2, 2),
ordering: 8*12=96 > 14*4=56 > 15*2=30,
freeness: 24 in <12>, 28 in <12,8>, 30 in <12,8,14>,
C = 1-12 + 2*8 + 1*14 + 1*15 = 34.
```

The exact lists are recorded in Section 4 and frozen in the replay.

## 3. Signed iterated-torus dictionary

The parent compiler (**PROVISIONAL**) is used unchanged.  For a reduced
delta sequence `R=(r0,...,rh)`, put `w = gcd(r0,...,r_(h-1))`.  If `h=1`
the compiler uses the `r1`-strand torus braid `(sigma1 ... sigma_(r1-1))^r0`,
closing to `T(r1,r0)`.  If `h>1` the normalized prefix is again a reduced
delta sequence and

```text
K(R) = C_(w, rh)(K(R')).
```

Negative companion crossings use the inverse block switch; negative `q`
uses the signed inverse power.  Blackboard parallelization contributes
`w e(beta)` to the pattern meridian, so the final exponent is the
zero-framing correction `q - w e(beta)`.  Every signed word in this census
closes to one component.  The winding-two specialisation on `(6,4,7)`
remains byte-for-byte the previously sealed `X^3 sigma1^(7-6)` word.

Surviving rows convert as follows.  All `2^h` independent sign versions of
a length-`(h+1)` sequence were coloured; each displayed count is constant
across those signs.

```text
C=30, Delta_aff=15:
  (12,8,10,15) -> C_(2,15)(C_(2,5)(T(2,3)))           *72
  (12,9,7)     -> C_(3,7)(T(3,4))                     *24
  (16,3)       -> T(3,16)                             *24
  (16,6,3)     -> C_(2,3)(T(3,8))                     *72
  (16,12,3)    -> C_(4,3)(T(3,4))                     *168
  (16,12,6,3)  -> C_(2,3)(C_(2,3)(T(3,4)))            *360
  (18,4,15)    -> C_(2,15)(T(2,9))                    *72
  (18,12,9,7)  -> C_(3,7)(C_(2,3)(T(2,3)))            *72
  (18,12,15,4) -> C_(3,4)(C_(2,5)(T(2,3)))            *24
  (24,16,3)    -> C_(8,3)(T(2,3))                     *168
  (24,16,6,3)  -> C_(2,3)(C_(4,3)(T(2,3)))            *360
  (24,16,12,3) -> C_(4,3)(C_(2,3)(T(2,3)))            *744
  (24,16,12,6,3)-> C_(2,3)(C_(2,3)(C_(2,3)(T(2,3)))) *1512
  (27,6,4)     -> C_(3,4)(T(2,9))                     *72
  (27,18,6,4)  -> C_(3,4)(C_(3,2)(T(2,3)))            *936

C=32, Delta_aff=16:
  (8,6,21)     -> C_(2,21)(T(3,4))                    *72
  (9,6,14)     -> C_(3,14)(T(2,3))                    *144
  (12,8,9)     -> C_(4,9)(T(2,3))                     *168
  (12,8,18,9)  -> C_(2,9)(C_(2,9)(T(2,3)))            *360
  (12,9,8)     -> C_(3,8)(T(3,4))                     *384
  (18,12,8,9)  -> C_(2,9)(C_(3,4)(T(2,3)))            *72
  (18,12,9,8)  -> C_(3,8)(C_(2,3)(T(2,3)))            *432
  (21,6,8)     -> C_(3,8)(T(2,7))                     *24

C=34, Delta_aff=17:
  (12,8,14,15) -> C_(2,15)(C_(2,7)(T(2,3)))           *72

C=36, Delta_aff=18:
  (9,6,16)     -> C_(3,16)(T(2,3))                    *72
  (12,9,10)    -> C_(3,10)(T(3,4))                    *168
  (16,6,9)     -> C_(2,9)(T(3,8))                     *72
  (16,12,6,9)  -> C_(2,9)(C_(2,3)(T(3,4)))            *360
  (18,4,21)    -> C_(2,21)(T(2,9))                    *72
  (18,12,9,10) -> C_(3,10)(C_(2,3)(T(2,3)))           *792
  (18,12,21,4) -> C_(3,4)(C_(2,7)(T(2,3)))            *24
  (24,16,6,9)  -> C_(2,9)(C_(4,3)(T(2,3)))            *360
  (24,16,12,6,9)-> C_(2,9)(C_(2,3)(C_(2,3)(T(2,3)))) *1512
  (33,6,4)     -> C_(3,4)(T(2,11))                    *24

C=38, Delta_aff=19:
  (12,8,18,15) -> C_(2,15)(C_(2,9)(T(2,3)))           *360
  (12,9,11)    -> C_(3,11)(T(3,4))                    *24
  (15,9,8)     -> C_(3,8)(T(3,5))                     *24
  (18,12,8,15) -> C_(2,15)(C_(3,4)(T(2,3)))           *72
  (18,12,9,11) -> C_(3,11)(C_(2,3)(T(2,3)))           *72
  (18,12,15,8) -> C_(3,8)(C_(2,5)(T(2,3)))            *24
  (20,3)       -> T(3,20)                             *24
  (20,6,3)     -> C_(2,3)(T(3,10))                    *72
  (20,12,3)    -> C_(4,3)(T(3,5))                     *24
  (20,12,6,3)  -> C_(2,3)(C_(2,3)(T(3,5)))            *72
  (20,15,3)    -> C_(5,3)(T(3,4))                     *24
  (27,6,8)     -> C_(3,8)(T(2,9))                     *72
  (27,18,6,8)  -> C_(3,8)(C_(3,2)(T(2,3)))            *936
  (30,20,3)    -> C_(10,3)(T(2,3))                    *72
  (30,20,6,3)  -> C_(2,3)(C_(5,3)(T(2,3)))            *72
  (30,20,15,3) -> C_(5,3)(C_(2,3)(T(2,3)))            *72

C=40, Delta_aff=20:
  (12,8,14,21) -> C_(2,21)(C_(2,7)(T(2,3)))           *72
  (20,8,9)     -> C_(4,9)(T(2,5))                     *24
  (20,8,18,9)  -> C_(2,9)(C_(2,9)(T(2,5)))            *72
```

The parent winding-two residue theorem (**PROVISIONAL**), that
`C_(2,q)(T(2,n))` has a full-`S4` colouring if and only if `3` divides both
`n` and `q`, does **not** apply to a cable whose companion is already a
satellite.  The conductor-34 survivor is `C_(2,15)` of `C_(2,7)(T(2,3))`,
not of a torus; applying the residue theorem to the outer stage would
falsely kill it.  Likewise the conductor-16 row `C_(2,9)(T(2,5))` has count
zero, while its further cable `C_(2,9)` of that companion is a
conductor-40 survivor of count 72.  The sieve is not monotone under
cabling.

Burau-at-minus-one determinants equal the recursive satellite formula on
every all-positive compiled braid, on every independent sign vector when
`r1 <= 12`, and on both global orientations when `r1 > 12`.  The last
restriction is only a local-runtime bound: the 26-strand integer Burau
product is the cost, while colouring itself exhausts all `2^h` signs on
every row.  Full Laurent Alexander polynomials, up to Laurent units, agree
with `Delta_C(w,q)(K)(t) = Delta_T(w,q)(t) Delta_K(t^w)` for `T(3,16)`,
`T(4,11)`, and the winding-four conductor-40 survivor `C_(4,9)(T(2,5))`.

## 4. Exact `V4 -> S4 -> S3` colouring census

The parent all-family criterion (**PROVISIONAL**) is used unchanged.  The
quotient of an `S4` transposition colouring is a Fox 3-colouring, solved
linearly over `F3`.  Each nonconstant Fox colouring `rho` lifts through an
affine `F2` space `L_rho`, of which exactly four points are the
point-stabiliser complements; the remainder are full `S4`.  Thus

```text
labelled full-S4 count = sum_rho (|L_rho| - 4),
full S4 exists iff some dim_F2(L_rho) >= 3.
```

On every row with `r1 <= 4` this labelled count equals the parent direct
`6^(n-1)` Hurwitz enumeration.  The unique conductor-34 survivor was
independently group-validated: six nonconstant Fox colourings, 96 lifts, 72
full-`S4` images, and exactly four complement lifts per `rho`.  The parent
conductor-28 census remains all-zero.

In each display, `*N` marks a surviving row with labelled full-`S4` count
`N`.  Every unmarked row has count zero.  Death at the `S3` quotient is
`fox=3, lifts=0`.  Death by complement-only lifts is `fox>3, lifts=4`
times the number of nonconstant Fox colourings, full count zero.

```text
C=30:
  (7,6), (8,6,19), (9,6,13), (10,6,15), (11,4),
  (12,8,10,15)*72, (12,8,14,11), (12,9,7)*24,
  (14,4,19), (14,6,7), (15,6,10), (15,10,6),
  (16,3)*24, (16,6,3)*72, (16,12,3)*168, (16,12,6,3)*360,
  (18,4,15)*72, (18,12,9,7)*72, (18,12,15,4)*24,
  (21,6,7), (22,4,11),
  (24,16,3)*168, (24,16,6,3)*360, (24,16,12,3)*744, (24,16,12,6,3)*1512,
  (27,6,4)*72, (27,18,6,4)*936, (31,2)

C=32:
  (8,6,21)*72, (9,5), (9,6,14)*144, (10,6,17), (10,8,9),
  (12,8,9)*168, (12,8,10,17), (12,8,14,13), (12,8,18,9)*360, (12,9,8)*384,
  (14,4,21), (14,6,9), (15,6,11), (15,9,5), (17,3), (18,4,17), (18,12,5),
  (18,12,8,9)*72, (18,12,9,8)*432, (18,12,10,5), (18,12,15,5),
  (20,8,10,9), (21,6,8)*24, (21,14,4), (22,4,13), (25,10,4),
  (33,2), (33,6,2), (33,22,2)

C=34:
  (8,6,23), (10,6,19), (12,8,10,19), (12,8,14,15)*72,
  (14,4,23), (15,10,7), (18,4,19), (20,8,7), (20,8,14,7),
  (22,4,15), (35,2), (35,10,2), (35,14,2)

C=36:
  (9,6,16)*72, (10,6,21), (10,8,13), (12,8,14,17), (12,8,18,13),
  (12,9,10)*168, (13,4), (14,4,25), (14,6,13), (15,6,13),
  (16,6,9)*72, (16,12,6,9)*360, (18,4,21)*72, (18,12,8,13),
  (18,12,9,10)*792, (18,12,10,9), (18,12,21,4)*24, (19,3),
  (20,8,10,13), (21,6,10), (22,4,17),
  (24,16,6,9)*360, (24,16,12,6,9)*1512, (26,4,13), (33,6,4)*24, (37,2)

C=38:
  (9,6,17), (10,6,23), (10,8,15), (12,8,11), (12,8,14,19),
  (12,8,18,15)*360, (12,8,22,11), (12,9,11)*24, (14,4,27), (14,6,15),
  (15,6,14), (15,9,8)*24, (15,10,8), (16,6,11), (16,12,6,11),
  (18,4,23), (18,12,8,15)*72, (18,12,9,11)*72, (18,12,10,11),
  (18,12,15,8)*24, (20,3)*24, (20,6,3)*72, (20,8,10,15), (20,8,14,11),
  (20,12,3)*24, (20,12,6,3)*72, (20,15,3)*24, (21,6,11), (21,14,5),
  (22,4,19), (24,16,6,11), (24,16,12,6,11), (26,4,15),
  (27,6,8)*72, (27,18,6,8)*936,
  (30,20,3)*72, (30,20,6,3)*72, (30,20,15,3)*72,
  (39,2), (39,6,2), (39,26,2)

C=40:
  (10,6,25), (10,8,17), (11,5), (12,8,14,21)*72, (12,8,18,17),
  (14,6,17), (18,4,25), (18,12,8,17), (20,8,9)*24, (20,8,10,17),
  (20,8,18,9)*72, (22,4,21), (25,10,6), (26,4,17), (41,2)
```

Exact exclusion sets at the two obstruction candidates:

```text
C=34 zero rows (12 of 13):
  S3 death: (8,6,23), (10,6,19), (12,8,10,19), (14,4,23),
            (18,4,19), (20,8,7), (20,8,14,7), (35,2), (35,10,2), (35,14,2)
  complement-only: (15,10,7), (22,4,15)
  survivor: (12,8,14,15)*72

C=40 zero rows (12 of 15):
  S3 death: (10,6,25), (10,8,17), (11,5), (12,8,18,17), (14,6,17),
            (18,4,25), (18,12,8,17), (20,8,10,17), (25,10,6), (26,4,17), (41,2)
  complement-only: (22,4,21)
  survivors: (12,8,14,21)*72, (20,8,9)*24, (20,8,18,9)*72
```

Every `T(2,q)` row dies, as required by the parent two-transposition floor:
two transpositions generate a subgroup of order at most six.  When `3`
divides `q` the death is complement-only (`(33,2)`, `(39,2)`); otherwise it
is already at the `S3` quotient.

## 5. `Delta_aff` consequence, and what remains OPEN

In the charged irreducible one-place quartic-transposition class, a
zero-count row cannot occur as the plane-embedding delta-sequence of `B`.
That is a row-level exclusion, conditional on the parent
infinity-to-affine meridian-surjection and cabling dictionary
(**PROVISIONAL**).  It is not a genus-level exclusion.

Because conductors `34` and `40` each retain at least one positive row, this
lane does **not** obtain

```text
Delta_aff(B) != 17,     Delta_aff(B) != 20.
```

The intervening computed genera `15,16,18,19` likewise retain survivors, so
they are not excluded either.  A positive labelled count is exact
compatibility of the compiled knot with a full-`S4` transposition
representation.  It is not attainment of an affine curve, not a
`FULL_ACTUAL_EXIT`, and not a proof that the delta-sequence is realised by
an embedded one-place plane curve.  Isomorphic one-place coordinate rings
may have inequivalent embeddings and different delta-sequences; this census
classifies reduced plane-embedding sequences, as the parents do.

OPEN, typed, with no cap or analogy:

1. Existence of a reduced irreducible `A1`-normalised one-place plane curve
   with any surviving delta-sequence and with the charged quartic
   meridian-transposition representation.
2. The parent packets themselves, both labelled PROVISIONAL and under
   separate different-model review.  A rollback of either parent rolls back
   this census mechanically.
3. Odd conductors, which neither parent enumerates.
4. Every even conductor strictly larger than 40.  In particular it is OPEN
   whether any later term of `C = 10+6k` is a complete exclusion.  No
   monotone extrapolation is licensed.
5. Realisability of each enumerated sequence by an actual plane embedding,
   as opposed to an abstract numerical semigroup.

No AWS registration is required.  The largest census is 41 sequences; the
largest braid has 26 strands; colouring of all 806 sign variants took 3.6
seconds; the full replay, including Burau-at-minus-one controls, completed
in about two minutes on one core.  No Singular, msolve, CAS, or
uncertain-duration computation was used.

## 6. Replay, controls, and scope

```text
bfb746d50a5fae31606fda09ec4d78542a89d175417e80d7ee86493ea41fa3d4
  ops/block_descent_a1_genus_ladder_c34_c40_s4_replay.py

60c044ac2bc4d83f413e62212f031b9dd4fdeba874189efe22143cddcd869dbc
  canonical stdout under python3, python3 -O, and python3 -OO

bff3544b42ba2dac140e3d9fa208b460050b80eff027ce02d2eea64753831860
  payload_sha256 (before inserting the payload hash field)
```

The replay pins both parent hashes before import.  It is pure stdlib.  The
normal, `-O`, and `-OO` stdout bytes are identical.  Each mutation exits
nonzero at an intended gate:

```text
--mutate-drop-freeness
  fails the published conductor-14 example (old-pass of the arithmetic core)

--mutate-framing
  zeros companion writhe; fails the winding-two specialisation (6,4,7)
  before any new colouring verdict is consumed

--mutate-quotient
  corrupts the affine V4 lift table; fails "four complement lifts exist"
  on the first tiny-row group-validation

--mutate-promote-exclusion
  asserts that conductors 34 and 40 have no survivors.
  This is the deliberate old-pass / new-fail control: the same assertion
  would have passed on the parent rungs 22 and 28, which are all-zero, and
  it fails here because both 34 and 40 have positive rows.
```

The theorem remains conditional on the charged one-place/cabling and
infinity-to-affine meridian-surjection interfaces, all of which this lane
consumes as PROVISIONAL.  A different-model hostile review should
independently check the recursive census at the six even conductors, the
signed cabling dictionary, the `V4/S3` counts, the unique conductor-34
survivor, and the three conductor-40 survivors before any canonical
promotion.  This lane asserts no new exit price.

<!-- BODY-END -->
