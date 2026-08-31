# Conductor 10 and 16 genus-ladder gate: exact one-place census and S4 obstruction

Date: 2026-08-31 UTC  
Author: Sol 5.6 Ultra (`genus_ladder` lane)  
Frozen basis: `c0d1c47f5b5f8b8db243ce0499719316285d0958`  
Lifecycle: **FINAL+VERIFIED NARROW THEOREM / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Theorem and verdict

Let `B` be a reduced irreducible complex affine plane curve in the charged
one-place packet.  Assume

```text
normalization(B)=A1
```

and assume that `pi1(A2-B)` has a transitive representation to `S4` sending
every positive generic meridian to a transposition.  Then

```text
Delta_aff(B) != 5 and Delta_aff(B) != 8.               (0.1)
```

The exact reduced delta-sequence censuses are

```text
conductor 10:  (11,2), (6,4,7),
conductor 16:  (17,2), (10,4,9).                       (0.2)
```

Under the charged delta-sequence/cabling dictionary, the four infinity knots
are respectively

```text
T(2,11), C_(2,7)(T(2,3)), T(2,17), C_(2,9)(T(2,5)).   (0.3)
```

Every one has zero labelled full-`S4` meridian-transposition colorings.  Both
signs of each torus exponent and all four cable-sign/companion-mirror versions
of each satellite were counted.  Thus the meridian-preserving surjection from
the infinity-knot group to the affine complement group contradicts the
charged quartic monodromy in both genera.

This does **not** say that one-place curves with affine delta five or eight do
not exist.  It says that none can carry the required quartic full-`S4`
boundary representation.  It does not address reducible branch curves,
multiple places at infinity, non-`A1` normalization, nonminimal rank-four
packets, higher-rank blocks, or JC2 itself.

## 1. Frozen interfaces and primary-source correction

The charged topology and one-place inputs are

```text
03865aae3cc11a5f7de264ef7a66d1e3600ccb983ea8f95079c50d8a28b0b5aa
  xmodel/block-descent-a1-total-delta-two-iterated-knot-s4-obstruction-sol56-20260830.md

03b16c2deba48605482963ae7f98f5e74aca26ce0e1761bbeab653a164bec4b4
  xmodel/block-descent-a1-genus-three-cable-b1-obstruction-sol56-20260830.md

070faa884a26b0c96aaacafa7738cb39746407803d156a5a327d360eabf613e5
  xmodel/block-descent-a1-genus-four-cable-b1-obstruction-sol56-20260831.md
```

They supply the already charged statements

```text
g_3(K_infinity)=Delta_aff(B),
K_infinity is an iterated cable and is prime or trivial,
pi1(S3-K_infinity) ->> pi1(A2-B), preserving meridians. (1.1)
```

The arithmetic source is Assi--Garcia-Sanchez, *On curves with one place at
infinity*, arXiv:1407.0490v1, especially Proposition 2, the delta-sequence
definition before Proposition 13, and Section 5:

```text
https://arxiv.org/abs/1407.0490
PDF SHA-256 05081acd04a51c85d231ff288c8522b83e79d75b28af7f99868c2f5149683bf9.
```

One wording in the Opus ideation report needed correction.  That report
imposed `r_k/d_(k+1)>=2` at every stage.  The paper's exact reduced condition
is instead

```text
r0 > r1 > d2 > d3 > ... > d_(h+1)=1.                  (1.2)
```

Together with freeness and the product ordering, (1.2) is what the replay
uses.  Replacing the stronger report wording by the exact definition changes
neither census in (0.2), nor the previously charged conductor-six/eight
lists.  Thus the reported numerical conclusion survives, while its interface
is now exact.

## 2. Complete recursive census

For a delta-sequence `(r0,...,rh)`, put

```text
d1=r0, d_(k+1)=gcd(d_k,r_k), e_k=d_k/d_(k+1).
```

The replay checks exactly:

```text
e_k*r_k in <r0,...,r_(k-1)>                         (freeness),
r_k*d_k > r_(k+1)*d_(k+1) for 1<=k<h               (ordering),
C=sum_k (e_k-1)r_k-r0+1                             (conductor),
```

as well as (1.2).  Membership implies that `e_k` is the least positive
multiplier: every earlier semigroup element is divisible by `d_k`, while
`gcd(r_k/d_(k+1),d_k/d_(k+1))=1`.

The enumeration is not a guessed coordinate box.  It implements the exact
recursion in Section 5.  The one-stage case is

```text
C=(r0-1)(r1-1).                                       (2.1)
```

For `h>1`, deleting the last stage gives a delta-sequence of conductor
`C_prefix` and

```text
C=d_h*C_prefix+(d_h-1)(r_h-1),                        (2.2)
2<=r_h<=C-2,
2<=d_h<=C/(r_h-1)+1,
gcd(d_h,r_h)=1.                                       (2.3)
```

Equations (2.1)--(2.3), followed by the exact axioms, are a finite complete
recursion.  As a primary-source control, the implementation reproduces all
ten conductor-14 delta-sequences printed in Example 18, in the same sorted
list:

```text
(6,4,11), (8,3), (8,6,3), (9,6,5), (10,4,7),
(12,8,3), (12,8,6,3), (15,2), (15,6,2), (15,10,2).
```

It also reproduces the charged conductor-six and conductor-eight lists
exactly before producing (0.2).  Dropping freeness or dropping the product
ordering changes these control censuses and makes the replay fail closed.

For a three-term sequence, let `d=gcd(r0,r1)`.  The normalized prefix is the
companion torus knot `T(r1/d,r0/d)`, while the last stage is a winding-`d`,
meridional-`r2` cable.  Hence

```text
(6,4,7)  -> C_(2,7)(T(2,3)),
(10,4,9) -> C_(2,9)(T(2,5)),                           (2.4)
```

and the two-term sequences in (0.2) give the two torus rows in (0.3).

## 3. Exact S4 coloring calculation

A fixed coloring of a closed braid by the six transpositions of `S4` is a
meridian-transposition representation of its knot group.  The replay uses the
signed Artin/Hurwitz action

```text
sigma_i:(A,B) -> (A*B*A^-1,A)
```

and retains a coloring only when its entries generate all 24 elements of
`S4`.  Simultaneous conjugation is transitive on the six possible first
transpositions, so fixing the first color and multiplying by six is exact.

The torus rows are structurally dead.  A `T(2,q)` group has a two-meridian
generating set, while two transpositions generate a subgroup of order at most
six and cannot act transitively on four letters.  Direct braid enumeration of
`q=+/-11,+/-17` independently returns zero.

For a two-cable of a two-braid companion, put

```text
X=sigma2 sigma3 sigma1 sigma2.
```

The zero-framed braid used by the replay is

```text
C_(2,q)(T(2,n)): X^n sigma1^(q-2n).                   (3.1)
```

Every braid in (3.1) closes to one four-strand component in the charged rows.
An independent reduced-Burau calculation returns, up to Laurent units,

```text
Delta_T(2,q)(t) * Delta_T(2,n)(t^2),                  (3.2)
```

for all eight sign/mirror instances used here.  This checks both the block
switch and the blackboard-framing correction before the coloring verdict is
consumed.

The exact labelled full-`S4` counts are

| row | all sign/mirror counts |
|---|---:|
| `T(2,+/-11)` | `0` |
| `C_(2,+/-7)(T(2,+/-3))` | `0,0,0,0` |
| `T(2,+/-17)` | `0` |
| `C_(2,+/-9)(T(2,+/-5))` | `0,0,0,0` |

No determinant-only inference is used.

## 4. A reusable winding-two theorem

The same finite calculation gives more than the four rows above.  On the
entire set of `6^4` transposition-valued four-strand states, the action of `X`
has exact order 12 and that of `sigma1` has exact order 6.  Therefore (3.1)
depends only on

```text
n mod 12 and q mod 6.                                  (4.1)
```

Exhausting the six odd residues of `n` and the three odd residues of `q`
proves

```text
C_(2,q)(T(2,n)) has a full-S4 transposition coloring
iff 3 divides n and 3 divides q;                       (4.2)
when nonempty, the labelled count is exactly 72.       (4.3)
```

This includes the charged conductor-six survivor
`C_(2,3)(trefoil)` with 72 colorings as a positive control, and kills both
new cable rows for different reasons: `7` is not divisible by three in the
first, while `5` is not divisible by three in the second.

There is also a degree-independent group floor: transposition generators of a
transitive subgroup of `S_d` form a connected graph on `d` vertices, hence
require at least `d-1` distinct edges.  In degree four this forces meridional
rank, and therefore bridge number, at least three.  This explains every
two-bridge kill without enumeration.  Formula (4.2) is the next reusable
piece for the winding-two/two-braid tower.

This is not yet an all-genus obstruction.  Other conductors contain
winding-three and deeper iterated rows, and the boundary sieve is known to be
sporadic rather than monotone.  The optimal general successor is a recursive
delta-sequence-to-braid compiler paired with the same finite-state action;
higher-strand rows should be sharded on AWS once `6^(strands-1)` ceases to be
desk-scale.

## 5. Replay, controls, and scope

```text
a076e204121e1ed291edab8a94b09a9832afd3f04fda2a10cd94d36e5397258a
  ops/block_descent_a1_genus_ladder_s4_replay.py

b2a4418172aab4834fef9b1e09cffa2e921132770e4029d6f532e8c6b3ee437c
  canonical stdout under python3, python3 -O, and python3 -OO

1061ea3423bd77c208419f39beb3ad0a597b4ee85865f539ed67b90228fe50ba
  payload_sha256 (before inserting the payload hash field)
```

Each mutation

```text
--mutate-drop-freeness
--mutate-drop-ordering
--mutate-promote-cable-coloring
```

exits nonzero at its intended gate.  The normal, `-O`, and `-OO` stdout bytes
are identical.  Runtime is under two seconds for all three normal modes on the
coordinator host, so this was a small exact enumeration under the local-work
policy; no CAS, numerical root finder, heavy process, swap, or AWS capacity
was used.

The theorem remains conditional on the already charged one-place/cabling and
infinity-to-affine meridian-surjection interfaces.  The replay classifies
plane-embedding delta-sequences, not merely abstract coordinate rings; this
distinction is essential because isomorphic one-place curves can have
inequivalent embeddings and different delta-sequences.  A different-model
hostile review should check the recursive census, the delta-to-cable
dictionary, the signed satellite braid, and the full-image filter before
promotion into the canonical obstruction ledger.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9942`.
- Body SHA-256:
  `5930919f3abf7d4d79566b30a66cb103c724d922930d1b2a00eade0a67c995c5`.
- Frozen basis: `c0d1c47f5b5f8b8db243ce0499719316285d0958`.
