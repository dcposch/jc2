# Hostile review: genus-ladder conductor 12/14/18/20/22/28 S4 census extension

Reviewer: GPT-5.5 hostile pass, 2026-08-31.

Scope: frozen one-place S4 census-extension packet only. No promotion, no canonical ledger edits, no `jc2-lean` inspection, and no new exit-price assertion.

## Hash gate

CONFIRMED. I reproduced all six SHA-256 hashes against the frozen copies in
`/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.B1hLGF/inputs`
before mathematical reading:

- `1500eeb24e1a9f4b2d27daeca85f6ed735a962ae2f7d26e8f923f38ea7d1de7a`
- `731636008ad4ae0daa402a3f74b670b921d03776d81bd8fd172af78c3746918b`
- `e01c7815a9ef3be93305ae54d7cdc2747e0e11909f9185031fd2762c4605367b`
- `e802ab6bcca9a27058ca8b33232f56e5abdd9f90df1c60c28d308fad0cd9a863`
- `a076e204121e1ed291edab8a94b09a9832afd3f04fda2a10cd94d36e5397258a`
- `03865aae3cc11a5f7de264ef7a66d1e3600ccb983ea8f95079c50d8a28b0b5aa`

## Method and Limits

I read only the six frozen charged inputs named in the assignment, from the
temporary input directory. I did not inspect `jc2-lean`, did not edit any
charged input, and did not edit any canonical ledger. I used the Assi--Garcia-
Sanchez arXiv page only to check the reduced delta-sequence axioms and the
fixed-genus recursion against the cited primary source.

I ran no Singular, msolve, CAS, numeric root finder, or open-ended search. The
only substantive computations were the two named exact-Python replays and
short exact arithmetic checks of conductor formulas, gcd ladders, and the
`S4 -> S3` quotient argument.

## Replay Results

CONFIRMED. The extension replay
`block_descent_a1_genus_ladder_next_s4_replay.py` completed in all three modes:

```text
python3      stdout SHA-256 1cb799cc8c6686ee17f0d8c2e0f6a605f2998264637ef48de025f6d8fa2e91b6
python3 -O   stdout SHA-256 1cb799cc8c6686ee17f0d8c2e0f6a605f2998264637ef48de025f6d8fa2e91b6
python3 -OO  stdout SHA-256 1cb799cc8c6686ee17f0d8c2e0f6a605f2998264637ef48de025f6d8fa2e91b6
```

This matches the packet's recorded canonical stdout hash. Its payload hash was
`07155183a332cd9cbfbe48befe7fd989a32c4c80657621d2737f3c11e4dc3a0c`.

CONFIRMED. The extension mutations failed nonzero:

```text
--mutate-framing       RuntimeError: winding-two compiler specialization
--mutate-quotient      RuntimeError: four and only four complement lifts
--mutate-promote-zero  RuntimeError: all independent sign variants have the same count in the charged rows
```

I also ran the pinned predecessor core replay because the new script imports it
by hash. Its normal, `-O`, and `-OO` stdout hash was
`b2a4418172aab4834fef9b1e09cffa2e921132770e4029d6f532e8c6b3ee437c`,
matching the predecessor packet. Its three mutations also failed at their
advertised gates. This confirms reproducibility of the frozen core, but does
not promote the predecessor 10/16 theorem.

## Per-Claim Verdicts

| claim | verdict | hostile attack and finding |
|---|---|---|
| Frozen custody | CONFIRMED | All supplied SHA-256 hashes match the frozen copies before mathematical reading. |
| Reduced Assi--Garcia-Sanchez axioms are the ones used | CONFIRMED | The primary source defines freeness, product ordering, and `a0>a1>D2>...>1`; the core tests exactly positivity, primitive gcd ladder, freeness, and ordering. The earlier stronger `r_k/d_(k+1)>=2` wording is not used. |
| Census completeness for conductors 12, 14, 18, 20, 22, 28 | CONFIRMED | The recursion ranges over the last generator `r_h` and last gcd `d_h` with the source bounds, recursively enumerates the prefix conductor, and then rechecks the exact axioms and conductor. I found no missing row by desk checks at the dead conductors, and the replay matches the conductor-14 printed source control. |
| Survivor and exclusion counts | CONFIRMED | The replay payload gives the displayed positive rows and zero for every omitted row. In particular C=22 has no full `S4` survivor and C=28 has no full `S4` survivor. |
| `V4 -> S4 -> S3` quotient/lift reduction | CONFIRMED | The quotient map is constructed from the action on the three pair-partitions of four letters, not by hand labels. Each `S3` transposition fiber has two `S4` transposition lifts. The `F3` Fox rule and `F2` affine lift table are derived from actual conjugation in `S4`; the mutation of that table is caught. |
| No coloring lost at 18-strand rows | CONFIRMED, conditional on the group lemma | The counter has one `F2` variable per braid meridian, so the 18-strand rows are not truncated. It does not brute-force `6^18`; instead it uses the exact lemma that a lift over an onto `S3` quotient is either one of four complements or full `S4`. |
| Delta-sequence to iterated torus-knot conversion | CONFIRMED in charged scope | For `(r0,...,rh)`, the compiler uses base `T(r1,r0)` and then `C_(w,rh)` where `w=gcd(r0,...,r_(h-1))`; the resulting strand count is `r1`. The genus formula matches the conductor recursion, and Burau/Alexander controls catch the framing correction `rh - w*writhe(beta)`. |
| Scope translation C=22,28 to `Delta_aff=11,14` | CONFIRMED | The charged interface supplies `g_3(K_infinity)=Delta_aff`, and the delta-sequence conductor is twice that genus. Hence death of C=22 and C=28 gives `Delta_aff != 11,14` under the stated one-place quartic-transposition hypotheses. |
| Combined `Delta_aff notin {5,8,11,14}` | GAP as a standalone result of this review | The `5,8` part is inherited from the provisional 10/16 packet. If that packet is corrected, only the `5,8` portion and the phrase "already sealed" are affected; the new C=22/28 computation does not depend on those exclusions. |
| No monotone or interpolated exclusion | CONFIRMED | The packet explicitly leaves survivors at C=12,14,18,20,24,26 and does not infer death between or beyond computed conductors. |
| Embedding versus abstract semigroup scope | CONFIRMED | The packet says it classifies plane-embedding delta sequences, not abstract coordinate rings or semigroups up to isomorphism. This is consistent with Assi--Garcia-Sanchez's warning that isomorphic one-place curves may have inequivalent embeddings and different delta sequences. |

No new mathematical claim in the 22/28 extension packet was refuted by this
review. The only adverse verdict is the dependency gap for importing the
predecessor's `Delta_aff=5,8` exclusion into the combined set.

## Census Check

The exact rows and positive counts reproduced by the replay are:

```text
C=12: survivors (6,4,9):72, (9,6,4):72 among 6 rows.
C=14: survivors (8,3):24, (8,6,3):72, (12,8,3):168, (12,8,6,3):360 among 10 rows.
C=18: survivor (15,6,4):24 among 11 rows.
C=20: survivors (8,6,9):72, (9,6,8):72, (12,8,6,9):360 among 14 rows.
C=22: no survivors among 6 rows.
C=24: survivors remain, 8 positive rows among 17 rows.
C=26: survivors remain, 5 positive rows among 18 rows.
C=28: no survivors among 10 rows.
```

Desk attacks on the dead conductors found no axiom or conductor mismatch. For
example, at C=22 the rows
`(8,6,11)`, `(10,4,15)`, `(12,8,6,11)`, `(14,4,11)`,
`(15,10,4)`, `(23,2)` all satisfy the conductor formula

```text
C = 1 - r0 + sum_k (d_k/d_(k+1)-1) r_k
```

with strict reduced gcd ladder and product ordering. At C=28 the ten listed
rows likewise pass the same desk check; sample calculations are
`(8,5): (8-1)(5-1)=28`,
`(12,8,10,13): 16+10+13-12+1=28`, and
`(20,8,10,5): 32+10+5-20+1=28`.

The death mechanisms also reproduce exactly. For C=28 every row has only the
three constant Fox colorings, so the `S3` quotient already kills full `S4`.
For C=22, four rows die the same way; `(10,4,15)` and `(15,10,4)` have nine Fox
colorings, hence six nonconstant Fox colorings, but only 24 nonconstant `S4`
lifts in total, exactly four complement lifts per nonconstant quotient and no
full lift.

## Quotient/Lift Check

The split reduction survived the main hostile tests I could run within the
rules. The quotient map sends each `S4` transposition to its induced
transposition on the three partitions of `{0,1,2,3}` into two pairs. The code
checks that each quotient color has exactly two transposition lifts. The affine
table is then computed by evaluating `A B A^{-1}` in `S4` for all lift bits,
and only afterwards solving linear equations over `F2`.

The possible failure mode would be a full `S4` coloring whose quotient is
constant, or an onto Fox quotient whose non-full lifts are not exactly the four
point-stabilizer complements. The first cannot occur: a constant quotient
generates at most one transposition in `S3`, so it cannot be the image of a full
`S4` subgroup under `S4 -> S3`. For the second, if a lift subgroup maps onto
`S3`, its intersection with `V4` is invariant under the full `S3` action on the
three nonidentity elements of `V4`; hence the intersection is either trivial or
all of `V4`. The trivial case is a complement, and there are exactly four
point-stabilizer complements. Therefore subtracting four from each affine lift
space is exact.

The code validates this against direct `S4` enumeration on all rows of at most
four strands. The 18-strand rows are not directly enumerated, but the linear
encoding has no strand cap and the group-theoretic subtraction is not
strand-dependent.

## Cabling and Framing Check

The compiler's parameter order is consistent with the genus/conductor
recursion. The base two-term sequence `(r0,r1)` is represented by the
`r1`-strand torus braid `(sigma1 ... sigma_(r1-1))^r0`, i.e. `T(r1,r0)`.
For a longer row, putting `w=gcd(r0,...,r_(h-1))` gives the recursive cable
`C_(w,rh)` of the normalized prefix. Since `gcd(w,rh)=1`, these are knot
cables, and

```text
2 g(C_(w,rh)(K)) = w * 2g(K) + (w-1)(rh-1)
```

is the same recurrence used for the conductor.

The framing correction is the main place a silent sign/order error could enter.
The replay uses `rh - w*writhe(companion_word)` after replacing each companion
crossing by the positive block switch. I confirmed the specialization
`(6,4,7) -> C_(2,7)(T(2,3))` agrees with the predecessor word, and the replay's
Alexander-polynomial controls cover base `T(3,8)`, all signs for winding two
and winding three samples, and a positive winding-four sample. Changing the
writhe term is caught before any census result is accepted.

## Hypotheses and Dependency

The weakest exact hypotheses I find are:

```text
B is reduced and irreducible over C;
B lies in the charged one-place-at-infinity packet;
normalization(B)=A1;
pi1(A2-B) has a transitive S4 representation sending positive generic meridians to transpositions;
the charged infinity-knot interface gives a meridian-preserving surjection
  pi1(S3-K_infinity) ->> pi1(A2-B);
the infinity knot is the iterated cable encoded by the reduced delta sequence;
the delta-sequence conductor equals 2*Delta_aff(B).
```

Under those hypotheses, C=22 and C=28 are exactly excluded. The predecessor
10/16 packet is load-bearing only for adding `Delta_aff=5,8` to the displayed
set. A correction to the 10/16 packet would not change the new C=22/28 counts,
the quotient/lift criterion, or the adjacent survivor rows C=12,14,18,20,24,26.

## Best Next Falsification Test

The best next test is a second, non-shared implementation of the `S4 -> S3`
lift counter that enumerates every affine `F2` lift solution for the largest
18-strand rows, converts it back to actual `S4` transpositions, checks braid
closure by the original Hurwitz action, and computes generated subgroup order.
This avoids `6^18` while directly attacking the only remaining high-strand
trust point: that the affine lift equations and the four-complement subtraction
remain exact beyond the rows where direct enumeration was already run.

<!-- BODY-END -->
