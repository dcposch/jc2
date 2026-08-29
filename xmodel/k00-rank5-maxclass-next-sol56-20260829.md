# K00 `MAX5CLASS`: the rank-five locus is empty on the leading base

Author: Sol 5.6, independent rank-five lane  
Date: 2026-08-29  
Basis: `92ebe92ad5986a47f01af9ed901260595dfed869`  
Lifecycle: **PROVISIONAL EXACT DISCOVERY / DIFFERENT-MODEL REVIEW REQUIRED**  
Binary disposition: **`PASS_K00_MAX5CLASS_ZERO_RANK5_CHARTS`**

## Executive result

The registered `MAX5CLASS` comparison closes in the empty direction.  In the
six-variable exact ring

```text
R0 = Q[d0_1,d1_1,d2_1,d3_1,d4_1,d5_1],
```

let `A` be the frozen `7 x 7` grade-seven newest-variable matrix and write

```text
q1,...,q6 = the six nonzero literal grade-two rows 1,2,3,4,5,7,
B2 = (q1,...,q6),
B  = B2 + (F10).
```

This `q6` means literal grade-two row 7.  It is **not** the older V24 logical
slot called `Q6`, which was zero.

An independent exact reconstruction of all 441 literal `5 x 5` minors finds
90 nonzero minors and exactly two scalar-proportionality classes.  The first
is the reviewed `W` class.  For the second, take

```text
M = det A[rows (0,1,2,3,5); columns (0,1,2,3,6)].
```

The reviewed identity puts `W` in `(q1,q3,q4)`.  A new exact membership
certificate gives

```text
M = C1*q1 + C2*q2 + C4*q4 + C6*q6,
```

with degree-four coefficients and no use of `q3`, `q5`, or `F10`.
Consequently

```text
I5(A) subset B2 subset B,
B + I5(A) = B,
V(B) intersect {rank(A)=5} = empty.
```

Thus the exact number of nonredundant rank-exact-five charts remaining is
**zero**, both on the leading base and over the full prior scheme `V(P6)`.
No rank-five AWS job should be launched.

## Frozen reconstruction

The exact source was

```text
d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501
  cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827/
  aws_box02_r2_held_compile/output/ATLAS_EXACT_POLYNOMIALS.json
```

The independent checker parsed `exact_terms`, not the displayed Singular
strings.  The row-by-row entry-term census of the reconstructed matrix was

```text
      columns 1  2  3  4  5  6  7
row 1           2  2  3  3  3  3  6
row 2           2  3  3  3  3  3  9
row 3           3  3  3  3  3  3  8
row 4           3  3  3  3  3  3 11
row 5           3  3  3  3  2  2  9
row 6           0  0  0  0  0  0 12
row 7           2  2  2  2  2  2  9
```

Columns are source-labelled
`(d0_6,d1_6,d2_6,d3_6,d4_6,d5_6,k10_3)`.  Columns 1--6 are linear in the
leading variables and column 7 is quadratic.  The base source profile is

| source row | terms | frozen polynomial SHA-256 |
|---|---:|---|
| `q1` / literal row 1 | 8 | `50d500469b167f5bb9f22d7ac4eb62e80fcaad57a3990a3e22d80c57fbdec43a` |
| `q2` / literal row 2 | 11 | `cc3f86357d1ffc53b5a0155ed41518949ea3d79ba270142377df220e17562a7a` |
| `q3` / literal row 3 | 9 | `c37cfca55ddf2c3a35b4633e00f308a2fedb9578597c0456ef27bec860991204` |
| `q4` / literal row 4 | 12 | `cdeae0ee8f884b0994abb3cc29e7c925625e19f7bbd4ec1dca9af7495f351fe3` |
| `q5` / literal row 5 | 8 | `29898d786353e0f9c0ea2b5e56acaaee23ffeae43d503207b826a3d8a30a1c29` |
| `q6` / literal row 7 | 6 | `da061b29ff155501758e3383961cbd524b8f80cb6290ef662a27e0f35db6256e` |
| `F10` | 30 | `6a0dcbcbdb5492978c29119e95f95517a4a3f27d73578a2ee4b89faf212a5945` |

The three constant-kernel identities were then recomputed coefficientwise:

```text
l0 A = 0,
l0 = (5/1024, 0, 3/128, 0, 1/8, 0, 1),

A v1 = 0,
v1 = (2, 0, 1, 0, 1, 0, 0)^T,

A v2 = 0,
v2 = (0, 1/16, 0, 1/2, 0, 1, 0)^T.
```

The two right vectors are independent, so they structurally explain
`rank(A) <= 5` and `I6(A)=0` before any base equation.  Adding `1` to the
first nonzero coefficient of each of `l0`, `v1`, and `v2` made the
corresponding identity nonzero.  The same exact reconstruction gives
`l0*b != 0`, with 690 terms, and matches the frozen serialization byte-bound
by

```text
88516f87868cb27a78ac9b35d15d6aeef3ea555182710424d9520b2f9bfb565e.
```

The kernel identities alone do not prove the new rank-four ceiling on
`V(B)`; the two class memberships below do.

## Complete maximal-minor census with source labels

Every `5 x 5` determinant was recomputed by exact sparse-polynomial Laplace
expansion from `A`.  The resulting 441 polynomials agreed entrywise with the
frozen compound ledger

```text
17d13f45fd64b8b3cb584e7451891d9f9f2201b18be70b280d2a04014e1a0e58
  .../output/A_COMPOUND_MINORS.json.
```

For each nonzero polynomial, division by the coefficient of its
lexicographically first monomial gives a canonical scalar-class key.  There
are exactly two keys.  Their complete label sets have a compact Cartesian
description.  In zero-based indexing, set

```text
C = {01236, 01256, 01346, 01456, 02356,
     03456, 12346, 12456, 23456},

RW = {01234, 01236, 01346, 12346},
RM = {01235, 01345, 01356, 12345, 12356, 13456}.
```

Then the nonzero literal minors are exactly

```text
W class: RW x C,  4*9 = 36 literal minors,
M class: RM x C,  6*9 = 54 literal minors.
```

The other 351 literal minors vanish.  Within the two literal classes there
are respectively 23 and 31 distinct exact polynomials, reproducing the
reviewed 54-distinct-polynomial census.  The representatives are

```text
W = det A[01234 | 01236], 226 terms,
    frozen polynomial SHA-256
    a78701cd74655f3c1514a954b081a1a602ff657bc39b2477de6fb99a2b0f722e,

M = det A[01235 | 01236], 236 terms,
    frozen polynomial SHA-256
    de45e3764cd19dc78397c4302b47439140cd2166665a2b5dc982075f82589f5e.
```

`W` and `M` have different normalized keys.  Replacing either representative
by the other therefore fires the registered cross-class mutation rather than
silently selecting the same class.

The full reconstruction used 23.25 seconds wall time, 738,426,880 bytes
maximum resident memory, one local process, and zero swaps.  This is below
the delegated desk bound of 60 seconds and 1 GB; no heavy local computation
or AWS resource was used.

## The two exact memberships

The first class is already independently reviewed.  The exact identity

```text
W in (q1,q3,q4)
```

is established by the V24R6R1 review and the Opus cross-audit, whose current
full-file hashes are respectively

```text
f9d2afcb01c1ad1161783d0ff51d9d47d1a6aa5831b508936072f0c9170012b9
d9e653150d14bc2791e366c2e425de5790f0f4390ab5790469bb9fe6ef4b644b.
```

For the second class, two fresh Singular 4.4.1 exact-Q processes computed
`std(B)` and the Rabinowitsch ideal `(B,z*M-1)`.  Both produced the
byte-identical 76-byte transcript with SHA-256

```text
1716caed1bb9c9e58037470a7d313bab5b661979b88d01231b0d11e199a3de8f
```

and the markers

```text
B_NF_ZERO=1
B_NF_TERMS=0
CHART_UNIT=1
CHART_DIM=-1
CHART_NGEN=1
M_TERMS=236
```

More importantly, a direct `lift(B,ideal(M),U,"slimgb")` proposed a literal
seven-entry membership column.  Two fresh processes reproduced the same
6,985-byte labelled transcript, SHA-256

```text
ad2455e06f9072f78931466f9130c845648728313fd612c788f3d7a04670363c.
```

In source order `(q1,q2,q3,q4,q5,q6,F10)`, the coefficient term counts and
hashes of the exact `string(poly)` serializations (without a trailing
newline) are

| coefficient | terms | SHA-256 |
|---|---:|---|
| `C1` | 56 | `9a708aed18ac32bfb61d96e3072087e797d1d822d6a5c9265fa8d7768190844a` |
| `C2` | 49 | `8b05adee8f287ebdfab2c3c3795a953bbc33e05bc2648047748ca6c95d525af7` |
| `C3=0` | 0 | `5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9` |
| `C4` | 38 | `fc30f54da1a54e0aee21d4c610dad936f68e3a118dec97b2df19b990715071e7` |
| `C5=0` | 0 | `5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9` |
| `C6` | 56 | `4303323cd5661a36871cadc2c26c4427a0cd6e4df8782ca0d2b25243a101f34d` |
| `C7=0` | 0 | `5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9` |

Concatenating those seven serializations in order, one newline after each,
has SHA-256

```text
a9a983acbc4a5b208e2c8c30a11ae399d7c7566d6279fa23ba4d95b88a82d0d4.
```

A separate pure-Python verifier parsed these proposed coefficients into
sparse polynomials over `Fraction`, multiplied them by the seven frozen base
generators, and checked coefficientwise that the residual is zero.  It also
checked that the mutation `C1 -> C1+1` changes the residual to the nonzero
polynomial `q1`.  Thus the proof of membership does not trust a standard-
basis attribute or a producer status string.

The certificate/replay pass took 3.36 seconds and 733,085,696 bytes maximum
resident memory including the child process, with zero swaps.  No repository
case packet is needed: the exact source objects are already frozen, the
representative has a literal row/column label, and the short replay is
deterministically regenerated from those bytes.

## Exact consequence and chart count

Every literal maximal minor is zero or a nonzero rational scalar multiple of
`W` or `M`.  Both representatives lie in `B2`.  Therefore the full Fitting
ideal satisfies `I5(A) subset B2` scheme-theoretically, not just after taking
a radical.  It follows that

```text
Spec(R0/B) has rank(A) <= 4 everywhere,
Spec(R0/B)[1/m] is empty for every 5 x 5 minor m,
the rank-exact-five principal-open cover has 0 surviving charts.
```

Because the full prior ideal `P6` contains `B`, every full-P6 rank-five
localizer is also exactly unit.  For example, if
`L=z*k10_0*M-1`, the membership `M in P6` gives

```text
1 = z*k10_0*M - L in P6 + (L).
```

The analogous identity holds for every other maximal minor.  A full-P6
Groebner computation would only re-prove this inherited unit certificate and
must not be launched.

There is also a useful composition with the already reviewed V27 R1/R2
containments.  The Fable review (SHA-256
`738f46030a73fea2a06a8e3139ed9aa5e2001b72a579e459357af81f6801647a`)
proved

```text
I4(A), I3(A) subset B + I5(A).
```

Combining that reviewed input with the new equality `B+I5(A)=B` gives

```text
I3(A) subset B,
rank(A) <= 2 on all of V(B).
```

This corollary uses no result from the concurrently reviewed provisional
grade-three rank-two theorem.

## Smallest successor and deduplication

After the reviewed V27 containments are composed with this result, the first
nonredundant compatibility gate is the chart-free grade-three one, not a
rank-five or full-P6 chart.  Let the seven literal grade-three rows be
written, directly from their source labels, as

```text
P3 = C*u + c3,
u  = (d0_2,d1_2,d2_2,d3_2,d4_2,d5_2)^T,
C  = A[:, columns 1..6],
E3 = [C | c3].
```

On `V(B)`, `rank(C) <= rank(A) <= 2`.  Hence a grade-three solution implies
`I3(E3)=0`.  The smallest chart-free exact target is therefore

```text
H3 = B + I3(E3)  in R0.
```

This is precisely the independently produced `K00-G3-R2-CHARTFREE/v1`
packet now undergoing adversarial review.  I did not consume its provisional
endpoint, repeat its calculation, or create a competing packet.  If its
source reconstruction or power certificate fails review, `H3` remains the
correct registered target; if it passes, no full-P6 rank-two minor chart is
needed.

For a later lower-rank branch that survives the grade-three gate, the
smallest full-P6 chart-free grade-seven screen is the single constant-left-
kernel equation

```text
c7 = l0*b,
Kleft = P6 + (c7, t*k10_0-1).
```

Solvability of `A*y=b` forces `c7=0` at every rank.  This screen is strictly
weaker than full Fitting compatibility but is a valid unit-ideal kill test.
It should not run ahead of the grade-three review.  If it becomes live, its
AWS preregistration is:

- inputs: the atlas `d7ec6d18...`, the 35 literal nonzero `P6` generators,
  the exact 690-term `c7` serialization `88516f87...`, and the then-promoted
  grade-three/lower-rank dependency;
- ring/ideal: exact `Q` in the frozen 33-variable order followed by `t`,
  frozen `dp` order, target `Kleft` exactly as displayed;
- outputs: typed `UNIT`, `PROPER`, or `RESOURCE_CAP_NO_VERDICT`; serialized
  basis, `NF(1)`, dimension when proper, and an entrywise checked lift of `1`
  when unit;
- controls: reconstruct `l0*A=0` and `c7=l0*b`, break both by the registered
  `l0[1]+1` mutation, retain the `-1` in the localizer, use `ncols()` for all
  positional loops, force a unit ideal and replay a named proper control;
- cap/stop: one exact-algebra process, 3,600-second wall cap, 64-GB address-
  space cap, zero swap; any warning, cap, signal, missing byte, or swap use is
  `RESOURCE_CAP_NO_VERDICT`, not evidence;
- replay: fresh exact process reconstructs all inputs from `exact_terms`,
  verifies both ideal inclusions and every tracked identity coefficientwise,
  and rederives the endpoint without status-string trust.

No AWS lane was launched in this task.

## Firewall

This report proves an exact statement about the frozen coefficient matrix on
the leading grade-two/F10 base.  It does not prove that a lower-rank point
solves grade three or grade seven, satisfies the normalized source open,
lifts through grades 8--19, defines a finite jet or arc, lies in K00 closure,
or comes from a polynomial Keller map.  It proves no order-two or
maximum-twelve theorem, no counterexample, and no result on JC2.

The binary disposition remains provisional until a different model replays
the two-class census and the new `M` membership certificate.  The concurrent
rank-two grade-three result was used only to deduplicate scheduling, never as
a premise.

## Seal

- Body length: `13199` bytes (all bytes before this heading).
- Body SHA-256: `5c0397492ad5a739944343686407a909a17d0e7cc37555cb18221ba40548e200`.
- Full-file SHA-256: reported out of band after sealing.
