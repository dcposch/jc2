# Coordinator integration: complete irreducible genus-three rank-four row

Date: 2026-08-31 UTC  
Author: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `ef7e0721dca0daedd09972f577be1ec1e3f8e887`  
Lifecycle: **TWO-MODEL REVIEW-INTEGRATED PROMOTED THEOREM**

## 0. Verdict

Fable 5 and Opus 5 independently reviewed the complete genus-three packet.
Both return `CONFIRM_WITH_CORRECTIONS`; neither found a counterexample or a
load-bearing failure. Fable found one substantive presentation issue:
arbitrary polynomial embeddings may contain redundant leading stages, while
the delta-sequence census and degree-three projection are stated for a
reduced embedding. Section 3 below supplies the required target-shear
normalization. The remaining corrections make the adapted local basis,
small-ball comparison, and coordinate-projection interface explicit.

The promoted campaign conclusion is:

> In an actual minimal cyclic rank-four proper-block packet with reduced
> irreducible target branch `B`, `normalization(B)=A1`,
> `b1(B)=n22=1`, `n4=0`, global transitive meridional `S4` monodromy, and
> generic meridians transpositions, one has `Delta_aff(B)>=4`.

Equivalently, every irreducible charged `Delta_aff=3` subrow allowed by the
proper-block ruling is empty. This is not a rank-four nonexistence theorem:
reducible forests, `Delta_aff>=4`, nonminimal quartic packets, and the
primitive/no-proper-block horn remain outside this statement.

## 1. Frozen evidence and custody

```text
5d7df7ce0ad3548e88fd23734917212d6b3fbd3ada4cab81514b12bb76ea64de
  xmodel/block-descent-a1-quartic-branch-topology-coordinator-integration-sol56-20260830.md
03865aae3cc11a5f7de264ef7a66d1e3600ccb983ea8f95079c50d8a28b0b5aa
  xmodel/block-descent-a1-total-delta-two-iterated-knot-s4-obstruction-sol56-20260830.md
03b16c2deba48605482963ae7f98f5e74aca26ce0e1761bbeab653a164bec4b4
  xmodel/block-descent-a1-genus-three-cable-b1-obstruction-sol56-20260830.md
bcfc47b0467d839f7f19a36620c9ca1436fa3fd3f653faa228b20b1a383ada9f
  xmodel/block-descent-a1-genus-three-m0-complete-obstruction-sol56-20260830.md
2b3cc0b7dd7db7a9e0f34cec4c76df97424615e3e5205f9a6fc391c5d3bb8d3d
  xmodel/block-descent-a1-genus-three-t34-m0-projection-rank-obstruction-sol56-20260830.md
17ace150a1773ffa89e92e4c9f112f0c383857f98d7605a31d8d7953b759b4bd
  xmodel/block-descent-a1-genus-three-t34-m1-projection-ramification-obstruction-sol56-20260830.md
be4c287fe56c067208496f39a7388c56592c562a93fe46665e693958ad972a3a
  xmodel/post-ledger-dependency-hash-corrigendum-sol56-20260831.md
4e793993eeded7aeb2412f8ebf803d31baeb3cb75a13b4b7e265d0cf87393ef3
  xmodel/block-descent-a1-genus-three-combined-hostile-review-fable5-20260831.md
7d054d2da5c2d67d847f18ce327ac8e9734b66c0c5c6964341f16adec5569846
  xmodel/block-descent-a1-genus-three-combined-hostile-review-opus5-20260831.md
9064d7e22b831328848eafc40518f35730338eb7032dd314bae40fb838cb1c92
  xmodel/block-descent-a1-genus-three-combined-hostile-review-fable5-20260831.run.v2
a5a02d25aaf3f2c047a1ec09e37fe602db4cfc748a4015429b03af355daeb374
  xmodel/block-descent-a1-genus-three-combined-hostile-review-opus5-20260831.run.v2
```

Both external lanes completed with exit code zero and
`charge_basis_status=ABSENT`. For each lane the coordinator read the
terminal receipt first, then independently reproduced the prompt, adapter,
launcher, sandbox profile, validator, appendix, composed model prompt, raw
report, and log hashes. The raw Fable/Opus report bodies were respectively
`e997a9a9...` and `2a58b600...`. Each report was sealed on its run basis,
verified, committed, and pushed before mathematical reading. The cable
producer's older misbound review hash is a provenance-only defect repaired by
the charged corrigendum above; neither present review relies on it.

## 2. Total-delta and cable reduction

The charged one-place interfaces give

```text
g(K_infinity)=Delta_aff(B)=3,
pi1(S3-K_infinity) ->> pi1(A2-B), preserving meridians. (2.1)
```

The reduced conductor-six delta-sequences are exactly

```text
(7,2), (4,3), (6,4,3).                                 (2.2)
```

The corresponding genus-three iterated-knot rows are screened with every
sign and mirror. `T(2,7)` has no transitive transposition image; the
winding-three cable fails freeness and the coloring screen. The winding-two
`(6,4,3)` row has 72 labelled full-`S4` colorings but its exact normal form

```text
U=(t^2+h)^2+c*t,
V=(t^2+h)^3+(3/2)c*t*(t^2+h)+(3/8)c^2,       c!=0       (2.3)
```

has self-pair sums at the roots of `s^3+4hs-c`. That cubic cannot have a
triple root, so at least two distinct normalization pairs force `b1(B)>=2`.
Thus only the `(4,3)` / `T(3,4)` row survives, and it has 24 labelled
boundary colorings.

## 3. Binding reduced-embedding repair

A raw one-place embedding can have a trivial leading stage with
`r1|r0`; examples at conductor six include `(6,3,4)` and `(8,4,3)`. Such a
presentation need not display a degree-three coordinate, so (2.2) must not
be described as a census of all raw coordinate presentations.

If `r1|r0`, the leading terms satisfy

```text
LT(X)=c*LT(Y)^(r0/r1).
```

The elementary triangular target automorphism

```text
(X,Y) |-> (X-c*Y^(r0/r1),Y)                            (3.1)
```

strictly decreases the larger coordinate degree. Iteration terminates and
produces the reduced delta-sequence presentation. Polynomial target
automorphisms preserve the embedded curve up to ambient isomorphism, its
normalization fibres, `b1`, affine delta, complement meridians, cover fibre
partitions, and monodromy. Composing the finite cover with the same target
automorphism also preserves finiteness, flatness, normality, and the charged
proper-block occurrence.

Consequently every raw charged row may first be reduced by (3.1). The
`(7,2)` reduction is killed by the two-meridian transposition graph, and the
`(6,4,3)` reduction by (2.3). The only survivor has reduced coordinate
degrees `(4,3)`. After the ambient polynomial automorphism, its degree-three
coordinate is literally a coordinate of `A2`; its fibres form a pencil of
affine lines. This is the exact projection used below.

## 4. Degree-three generation and local transport

For the reduced `(4,3)` embedding, the quartic projective closure has total
delta three in the affine plane and hence is smooth at its unique point at
infinity. A pencil through that point gives an affine coordinate `X` for
which

```text
X|_B:B -> A1
```

is finite of degree three. Equivalently, the resultant equation is monic of
degree three in the complementary affine coordinate. Affine
Zariski--van Kampen then says the three meridians of a regular vertical fibre
generate `pi1(A2-B)`.

At a critical value, choose a small ball around each target point and route
all meridians of one ramification cluster through one common connector. Such
cluster meridians extend to a geometric basis of the punctured fibre. The
small-ball conic/henselian comparison puts their images in one conjugate of
the complete local decomposition group and identifies its sheet orbits with
the local finite-algebra factors. Any two geometric bases differ by Hurwitz
moves, and basepoint change simultaneously conjugates the whole tuple.
Hence the generated subgroup, duplication of cluster colors, and containment
in an intransitive local group survive transport. Individual colors are never
identified across unrelated tails.

## 5. Exhaustion of the allowed subrows

The proper-block Euler/ruling ledger gives `e(U)=2-|T31|>=1`, so only
`|T31|=0` and `|T31|=1` occur in the charged irreducible genus-three row.

For `|T31|=0`, the length-two critical divisor of the cubic has a critical
parameter outside the unique conductor pair. Its local partition is
`(2,1,1)`, whose complete local group is `C2`; the two cluster meridians have
the same transposition image. The generating triple therefore has at most
two distinct transposition edges and cannot act transitively on four sheets.

For `|T31|=1`, every allocation of the length-two critical divisor is
intransitive:

- a double root at the `(3,1)` point saturates the cubic fibre and traps the
  whole triple in a fixed-sheet `S3`;
- a double root at a conductor endpoint violates `3+1<=3`;
- a double root elsewhere lies in a local `C2`;
- with two simple roots, at most one is the unique `(3,1)` point, while the
  other either creates a duplicated `(2,1,1)` cluster or lies at a conductor
  endpoint; in the latter case the saturated divisor `2a+b` traps the whole
  triple in the pair-preserving `C2 x C2`;
- two conductor endpoints violate `2+2<=3`.

This closes both subrows. The argument can be phrased uniformly as the
ramification-cluster dichotomy: a saturated critical fibre lies in one
intransitive local group; otherwise a ramified cluster duplicates enough of
the degree-three meridian tuple to leave at most two distinct edges.

## 6. Review corrections and evidentiary limits

The producer notation used `m` both for number of branch components and for
`|T31|`; downstream text must use qualified symbols. The objects in (2.2)
are delta-sequences of reduced embeddings, not merely abstract numerical
semigroups: `(6,4,3)` and `(4,3)` generate the same value semigroup but have
different plane degrees and infinity knots.

The exact replays are fail-closed under normal, `-O`, and `-OO` Python and
all declared mutations exit nonzero. Some printed geometric verdict lines
are string summaries gated by theorem-layer checks; they are not independent
machine proofs. The replay does not prove Schubert/Neumann--Rudolph topology,
Zariski--van Kampen, the small-ball comparison, or the proper-block ruling.
Those are explicit mathematical interfaces, reconstructed in both reviews.

The result assumes irreducibility. For a reducible branch forest,
`b1(B)` is not simply the sum of normalization-fibre deficits and the
one-parametrization/projection argument does not apply. No conclusion here
touches higher affine delta, nonminimal quartic rows, higher block degree, or
the primitive horn. The subsequently reviewed genus-four integration
`0ffb6f82...` is a separate theorem, not an inference from this one.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10152`.
- Body SHA-256:
  `f43de5c82503c004c799037cb4466ce1785311d2c18679f230439fd265cae333`.
- Frozen basis: `ef7e0721dca0daedd09972f577be1ec1e3f8e887`.
