# Genus ladder through conductor 28: recursive braid compiler and exact S4 census

Date: 2026-08-31 UTC  
Author: Sol 5.6 Ultra (`genus_ladder_next` lane)  
Frozen basis: `b6a73150edc586af1f14a14a9c86efa3b10e2958`  
Lifecycle: **FINAL+VERIFIED NARROW THEOREM / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Theorem and exact verdict

Let `B` be a reduced irreducible complex affine plane curve in the charged
one-place packet.  Assume

```text
normalization(B)=A1
```

and assume that `pi1(A2-B)` has a transitive representation to `S4` sending
every positive generic meridian to a transposition.  Then

```text
Delta_aff(B) != 11 and Delta_aff(B) != 14.             (0.1)
```

Equivalently, the complete reduced delta-sequence rows of conductors `22` and
`28` all fail the quartic full-`S4` boundary gate.  Together with the already
sealed conductor-10/16 result, the excluded rungs are now

```text
Delta_aff = 5, 8, 11, 14.                              (0.2)
```

The same exact computation completely classifies the intervening conductors
`12,14,18,20,24,26`.  Writing only the rows with nonzero labelled full-`S4`
meridian-transposition count gives

| conductor | `Delta_aff` | surviving delta-sequence: labelled count |
|---:|---:|---|
| 12 | 6 | `(6,4,9):72`, `(9,6,4):72` |
| 14 | 7 | `(8,3):24`, `(8,6,3):72`, `(12,8,3):168`, `(12,8,6,3):360` |
| 18 | 9 | `(15,6,4):24` |
| 20 | 10 | `(8,6,9):72`, `(9,6,8):72`, `(12,8,6,9):360` |
| 22 | 11 | none |
| 24 | 12 | `(9,4):24`, `(9,6,10):144`, `(12,8,10,9):72`, `(12,9,4):384`, `(18,4,9):72`, `(18,12,4,9):72`, `(18,12,9,4):432`, `(21,6,4):24` |
| 26 | 13 | `(8,6,15):72`, `(15,6,8):24`, `(27,6,2):144`, `(27,18,2):144`, `(27,18,6,2):1872` |
| 28 | 14 | none |

Every row omitted from the last column has count zero.  Independently changing
the sign of the base torus exponent and of every later cabling meridian leaves
every displayed count unchanged; all `2^h` sign versions were checked for a
sequence of length `h+1`.

This does **not** exclude one-place curves of any displayed genus.  It excludes
only the zero-count rows from carrying the charged quartic boundary
representation.  It does not address reducible branch curves, several places
at infinity, normalization other than `A1`, nonminimal rank-four packets,
higher-rank blocks, or JC2 itself.

## 1. Frozen interfaces

The charged one-place, genus, cabling, and meridian-surjection inputs are

```text
03865aae3cc11a5f7de264ef7a66d1e3600ccb983ea8f95079c50d8a28b0b5aa
  xmodel/block-descent-a1-total-delta-two-iterated-knot-s4-obstruction-sol56-20260830.md

03b16c2deba48605482963ae7f98f5e74aca26ce0e1761bbeab653a164bec4b4
  xmodel/block-descent-a1-genus-three-cable-b1-obstruction-sol56-20260830.md

070faa884a26b0c96aaacafa7738cb39746407803d156a5a327d360eabf613e5
  xmodel/block-descent-a1-genus-four-cable-b1-obstruction-sol56-20260831.md
```

They supply, in the charged scope,

```text
g_3(K_infinity)=Delta_aff(B),
K_infinity is an iterated cable and is prime or trivial,
pi1(S3-K_infinity) ->> pi1(A2-B), preserving meridians. (1.1)
```

The sealed arithmetic core and its conductor-14 primary-source control are

```text
a076e204121e1ed291edab8a94b09a9832afd3f04fda2a10cd94d36e5397258a
  ops/block_descent_a1_genus_ladder_s4_replay.py

e802ab6bcca9a27058ca8b33232f56e5abdd9f90df1c60c28d308fad0cd9a863
  xmodel/block-descent-a1-genus-ladder-conductor10-16-s4-obstruction-sol56-20260831.md
```

That core implements the complete Assi--Garcia-Sanchez recursion, not a
coordinate box, and reproduces their printed ten-row conductor-14 example.
The primary arithmetic source remains Assi--Garcia-Sanchez, *On curves with
one place at infinity*, arXiv:1407.0490v1, especially Proposition 2, the
delta-sequence definition before Proposition 13, and Section 5:

```text
https://arxiv.org/abs/1407.0490
PDF SHA-256 05081acd04a51c85d231ff288c8522b83e79d75b28af7f99868c2f5149683bf9.
```

The new replay verifies the pinned core hash before import.  No conclusion
below silently depends on a later edit to that core.

## 2. Recursive signed delta-sequence-to-braid compiler

For a reduced delta sequence `R=(r0,...,rh)`, let

```text
w = gcd(r0,...,r_(h-1)).                               (2.1)
```

If `h=1`, the compiler uses the `r1`-strand torus braid

```text
(sigma1 ... sigma_(r1-1))^r0,                          (2.2)
```

whose closure is `T(r1,r0)`.  If `h>1`, the normalized prefix

```text
R'=(r0/w,...,r_(h-1)/w)                                (2.3)
```

is again a reduced delta sequence, and the standard Puiseux/cabling
dictionary gives

```text
K(R) = C_(w,rh)(K(R')).                                (2.4)
```

The compiler realizes (2.4) for an arbitrary signed companion braid, not only
the winding-two/two-braid family.  Let `beta` be an `s`-strand companion word,
let `e(beta)` be its exponent sum, and let `Cab_w(beta)` replace each
`sigma_i` by the positive permutation braid that interchanges the adjacent
blocks of `w` parallel strands.  Put

```text
delta_w = sigma1 ... sigma_(w-1)
Beta_(w,q) = Cab_w(beta) delta_w^(q-w e(beta)).          (2.5)
```

Here `delta_w` acts on the first parallel block.  Blackboard parallelization
contributes `w e(beta)` to the pattern meridian, so the final exponent in
(2.5) is exactly the zero-framing correction.  The closure of (2.5) is the
zero-framed cable `C_(w,q)(closure(beta))`.  Negative companion crossings use
the inverse block switch, and negative `q` uses the signed inverse power.

Induction in (2.2)--(2.5) gives a braid on exactly `r1` strands for every
delta sequence, including the deep rows and the 18-strand rows at conductor
26.  The compiler checks that every signed word closes to one component.

The framing convention is fail-closed by four independent controls:

1. On `(6,4,7)` its word is byte-for-byte the previously sealed
   `X^3 sigma1^(7-6)` winding-two word.
2. For every row and every independent sign version, the Burau determinant at
   `t=-1` equals the recursive satellite determinant.
3. Full Laurent Alexander polynomials, up to Laurent units, agree with

   ```text
   Delta_C(w,q)(K)(t)=Delta_T(w,q)(t) Delta_K(t^w)      (2.6)
   ```

   for all signs of `T(3,8)`, winding-two and winding-three controls, and a
   positive winding-four/eight-strand control.
4. Deleting the framing correction makes the replay fail before any new
   coloring verdict is consumed.

Thus the compiler is not using Alexander polynomials to infer knot identity;
the satellite construction supplies the identity, while Alexander data are
an independent signed/framing control.

## 3. An all-family S4 criterion via V4 and Fox colorings

The direct six-color search is unnecessary.  Let `V4` be the normal Klein
four subgroup of `S4`.  The action on the three partitions of four letters
into two unordered pairs gives

```text
1 -> V4 -> S4 -> S3 -> 1.                              (3.1)
```

Each of the six transpositions of `S4` maps to a transposition of `S3`, and
each `S3` transposition has exactly two transposition lifts.  Therefore the
quotient of an `S4` transposition coloring is an ordinary Fox 3-coloring.
For a closed `n`-braid the quotient fixed-point equations are linear over
`F3`; the replay computes their nullspace exactly.

Fix a nonconstant Fox coloring `rho`.  It is onto `S3`.  Choosing one of the
two transposition lifts at each braid meridian gives `n` bits.  Conjugation of
transpositions in each fixed quotient-color pair is affine in those bits, so
the braid closure equations define an affine `F2` solution space `L_rho`.

There are exactly four non-full lifts in `L_rho`: composing `rho` with the
four sections `S3 -> S4` whose images are the four point stabilizers.  Conversely,
any lift image projects onto `S3`.  Its intersection with `V4` is invariant
under `S3`; since `S3` acts transitively on the three nonidentity elements of
`V4`, that intersection is either trivial or all of `V4`.  The former case is
one of the four complements, and the latter case is all of `S4`.  Hence

```text
number of labelled full-S4 colorings
  = sum over nonconstant rho of (|L_rho|-4),            (3.2)

full S4 exists iff dim_F2(L_rho) >= 3 for some rho.     (3.3)
```

Equations (3.2)--(3.3) are an exact all-knot-family criterion, not a heuristic
pattern in the first few conductors.  They reduce the old `6^(n-1)` search to
linear algebra over `F3` and `F2`.  The replay independently constructs the
actual `S4` lifts and compares their generated subgroups with all 24 elements
on every tiny row of at most four strands.  Those labelled counts equal the
old direct Hurwitz enumeration exactly.  A deliberate mutation of the affine
lift table fails this complement/lift gate.

## 4. Complete censuses and row verdicts

The exact recursive censuses are as follows.  In each display, `*N` marks a
surviving row with labelled full-`S4` count `N`; every unmarked row has count
zero.

```text
C=12:
  (5,4), (6,4,9)*72, (7,3), (9,6,4)*72, (10,4,5), (13,2)

C=14:
  (6,4,11), (8,3)*24, (8,6,3)*72, (9,6,5), (10,4,7),
  (12,8,3)*168, (12,8,6,3)*360, (15,2), (15,6,2),
  (15,10,2)

C=18:
  (7,4), (8,6,7), (9,6,7), (10,3), (10,4,11), (10,6,3),
  (12,8,6,7), (14,4,7), (15,6,4)*24, (15,10,3), (19,2)

C=20:
  (6,5), (8,6,9)*72, (9,6,8)*72, (10,4,13), (10,6,5),
  (11,3), (12,8,5), (12,8,6,9)*360, (12,8,10,5),
  (14,4,9), (15,6,5), (21,2), (21,6,2), (21,14,2)

C=22:
  (8,6,11), (10,4,15), (12,8,6,11), (14,4,11),
  (15,10,4), (23,2)

C=24:
  (7,5), (8,6,13), (9,4)*24, (9,6,10)*144, (10,4,17),
  (10,6,9), (12,8,10,9)*72, (12,9,4)*384, (13,3),
  (14,4,13), (15,6,7), (18,4,9)*72, (18,12,4,9)*72,
  (18,12,9,4)*432, (21,6,4)*24, (25,2), (25,10,2)

C=26:
  (8,6,15)*72, (9,6,11), (10,4,19), (10,6,11), (12,8,7),
  (12,8,10,11), (12,8,14,7), (14,3), (14,4,15), (14,6,3),
  (15,6,8)*24, (18,4,11), (18,12,4,11), (21,14,3), (27,2),
  (27,6,2)*144, (27,18,2)*144, (27,18,6,2)*1872

C=28:
  (8,5), (8,6,17), (10,6,13), (10,8,5), (12,8,10,13),
  (14,4,17), (18,4,13), (20,8,5), (20,8,10,5), (29,2)
```

Conductor 28 dies already in the `S3` quotient: every row has determinant
prime to three, so only the three constant Fox colorings exist.  At conductor
22, four rows die the same way.  The remaining rows `(10,4,15)` and
`(15,10,4)` each have six nonconstant Fox colorings, but every corresponding
lift space has size exactly four.  Those are precisely the four complement
lifts, so no full `S4` coloring remains.  Conductors 24 and 26 have the
displayed positive rows, proving that 28, not merely the next conductor
examined, is the next completely excluded rung after 22.

The survivor pattern is not monotone and should not be extrapolated.  For
example, conductors 12, 14, 18, 20, 24, and 26 all retain rows.  Formula (3.3),
not divisibility of a determinant alone, is the reusable successor.

## 5. Replay, controls, and scope

```text
e01c7815a9ef3be93305ae54d7cdc2747e0e11909f9185031fd2762c4605367b
  ops/block_descent_a1_genus_ladder_next_s4_replay.py

1cb799cc8c6686ee17f0d8c2e0f6a605f2998264637ef48de025f6d8fa2e91b6
  canonical stdout under python3, python3 -O, and python3 -OO

07155183a332cd9cbfbe48befe7fd989a32c4c80657621d2737f3c11e4dc3a0c
  payload_sha256 (before inserting the payload hash field)
```

The normal replay completes on the coordinator in well under one minute and
uses low memory.  Its census phase never performs a `6^(strands-1)` search;
the largest braid has 18 strands, but is handled by the linear quotient/lift
criterion.  No CAS, numerical root finder, heavy local process, swap, or AWS
capacity was used.

Each mutation

```text
--mutate-framing
--mutate-quotient
--mutate-promote-zero
```

exits nonzero at an intended gate.  The normal, `-O`, and `-OO` stdout bytes
are required to be identical before finalization.

The theorem remains conditional on the charged one-place/cabling and
infinity-to-affine meridian-surjection interfaces.  It classifies reduced
plane-embedding delta sequences, not merely abstract coordinate rings;
isomorphic one-place curves may have inequivalent embeddings and different
delta sequences.  A different-model hostile review should independently
check the recursive cabling winding, the general block-switch word, the
blackboard correction `q-w e(beta)`, the `V4/S3` lift argument, the complete
censuses, and the full-image counts before canonical promotion.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12348`.
- Body SHA-256:
  `3ada14c5de524e5f8aaf3d0a3b6ac84745a568795c49dce284a62bd795144341`.
- Frozen basis: `b6a73150edc586af1f14a14a9c86efa3b10e2958`.
