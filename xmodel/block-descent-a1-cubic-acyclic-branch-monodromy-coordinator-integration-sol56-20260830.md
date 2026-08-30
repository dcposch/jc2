# Binding integration: strict cubic second-leg block closure

Date: 2026-08-30 UTC  
Integrator: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `2aa49d87c6a5d1823849fdc712582e064874bc8b`  
Disposition: **FINAL+VERIFIED / PROMOTE AT EXACT CUBIC SECOND-LEG SCOPE**

## 0. Binding verdict

Let `F=(f,g):A2_C->A2_C` be a hypothetical non-invertible Keller map.  There
is no strict intermediate field

```text
C(f,g) proper-subfield K proper-subfield C(x,y)
```

for which

```text
[K:C(f,g)]=3.
```

Equivalently, no strict intermediate block of a hypothetical counterexample
has finite-flat second-leg degree `deg(g2)=3`.

The word **strict** (historically, "proper block") modifies the intermediate
field.  It does not assert that the first-leg morphism is proper.  In fact the
promoted sandwich theorem proves that the first leg is dominant,
quasi-finite, everywhere etale, open, and nonproper, while the second leg is
finite flat and therefore proper.  The contradiction below never changes
those roles.

This integration adopts the GPT-5.5 verdict `CONFIRM_WITH_CORRECTIONS`.  It
uses the full promoted topology package to obtain contractibility, not Euler
characteristic alone, and it states the weighted-cone comparison through
punctured weighted sublevel neighborhoods.  It also records explicitly that
the tempting Picard/Zariski--Main/Hartogs shortcut is false and is not a
dependency of the closure.

## 1. Frozen evidence and custody

Primary producer and independent hostile review:

```text
5be2e2af32c0f6201637a652d28a0ff5f6992c5ebde696b1198d7b94e4829cf7
  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-obstruction-sol56-20260830.md
  body 1153c316bedf4df9daf8536e3128bfaf5ff0993f399dffad3a1a43dcb160e8c6
5fd8b854452bf4e42a96ccaea89ca8b4be09310dc0cff424ae6dd0261392a455
  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-obstruction-sol56-20260830.md.artifact.json
a9e9323bfeb0522c827defb4b60184369b2a7249dedddbf3a791ce0f47b14843
  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-hostile-review-gpt55-20260830.md
  body 3bbad2b21b1fa5bf59ba5ea14576ff8f7afe00a130f5dbd14f16efd3acc12340
```

The review reproduced all charged hashes, reconstructed the classification,
local splitting, complement groups, and proper-block interface, and returned
`CONFIRM_WITH_CORRECTIONS`.  Its producer and review bases are respectively
`f91e7510...` and `03a4d8dc...`; both packets are committed beneath the frozen
basis of this integration.

Charged prior funnel and topology integrations:

```text
2e6d82035df6717d1a39f31dc19b23b7c727bb940d4730d2c7ea9400e5433cce
  xmodel/block-descent-a1-cubic-affine-survivor-funnel-sol56-20260830.md
9e32b0fe8835b6ea6002036b95e2261a612754d73d796cb10edda347cf3cf65e
  xmodel/block-descent-a1-cubic-affine-survivor-funnel-hostile-review-gpt55-20260830.md
8ccb92fd3676e9f8b58e3ace4eb9157d0fa290ea24abc84d9913e94ec407e16d
  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-coordinator-integration-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d
  xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
```

The exact primary source and desk replay charged by the reviewed producer are
also frozen:

```text
41245c20b1b61a0dcf8116340672d037b977e6759d5d99054fc06c292d5c36fc
  refs/arzhantsev_zaidenberg_acyclic_curves_arxiv1110.3028v2.pdf
648022d35191b67d9f1e1eec61cddc95bbee745001410ad1fbbffa1044417389
  ops/block_descent_a1_cubic_acyclic_branch_monodromy_replay.py
```

## 2. Exact proper-block interface

Normalize `C[f,g]` in `K` and put `Y=Spec(B_K)`.  The promoted sandwich gives

```text
A2 --g1--> Y --g2--> A2,
```

where `Y` is integral and normal, `g2` is finite flat of degree three, and
`g1` is dominant quasi-finite etale and nonproper.  Let

```text
R=NonEt_Y(g2)_red,              B=g2(R)_red.
```

The promoted ruling/topology package first excludes the complete ruling base.
In the remaining affine-base equality row it gives

```text
b0(B)=1,                 S0=empty,                 Q=0,             (2.1)
R -> B finite and point-bijective, hence an analytic homeomorphism, (2.2)
every component normalization is A1, and the affine incidence graph
of R (with loops and parallel edges retained) is a forest.          (2.3)
```

Contractibility does not follow from `e_c(B)=1` alone.  It follows from the
whole package (2.1)--(2.3): the analytic homeomorphism transfers the source
topology to `B`; each normalized `A1` component is contractible; unibranch
singularities do not alter its component topology; and every multibranch
identification is recorded by the connected forest incidence graph.  Thus

```text
B is a reduced connected topologically contractible plane curve.   (2.4)
```

At every `b in B`, finite flatness gives total fibre length three.  Branching
supplies a non-etale local factor of length at least two, while `S0=empty`
supplies an unramified local factor of length one.  Hence every geometric
branch fibre has exactly the partition

```text
(2,1).                                                            (2.5)
```

Finally, if `V=Y-g2^(-1)(B)` and `W=A2-B`, then `V->W` is finite etale of
degree three.  The nonempty open `V` in integral `Y` is connected, so its
monodromy action on the three sheets is transitive.

## 3. Acyclic-branch monodromy contradiction

For any `b in B`, henselian idempotent lifting applied to (2.5) splits the
local rank-three algebra into rank-two and rank-one factors.  A unital
finite-flat rank-one algebra over the local base is the base itself.  Thus the
whole local complement group fixes the companion sheet and maps into one
conjugate of `S2`; a generic component meridian maps to a transposition.

Arzhantsev--Zaidenberg classify every reduced connected simply connected
plane curve, hence (2.4), into two normal-form families.

1. In the line/comb family, a connected nontrivial comb has complement group
   `F_s x <h>`, where the spine meridian `h` is central.  Its image is a
   transposition, and the centralizer of a transposition in `S3` is precisely
   its order-two subgroup.  Therefore the entire monodromy image lies in an
   intransitive `S2`.  The one-line degenerations give the same conclusion.
2. In the weighted-cone family, positive weighted radial flow makes both the
   global complement and every sufficiently small **punctured weighted
   sublevel neighborhood** of the origin deformation retract onto the same
   weighted link complement.  Ordinary Euclidean balls and weighted
   sublevels are cofinal neighborhoods, so the global complement group is
   the origin-local complement group.  The local companion splitting at the
   origin therefore puts the whole global monodromy image in one intransitive
   `S2`.

These families exhaust (2.4).  In every case the global monodromy is
intransitive, contradicting the transitivity of `V->W`.  The assumed strict
intermediate field with `deg(g2)=3` cannot exist.

## 4. Picard/Zariski--Main firewall

On the affine survivor open `U=Y-R`, the reviewed funnel validly proves

```text
Pic(U)=Z/mZ<[F]>,                 U-g1(A2) is finite.      (4.1)
```

Equation (4.1) is only a statement about the target complement.  Strong
Zariski Main factors the first leg as

```text
A2 open--> Xbar finite--> U,
```

but (4.1) does not make `Xbar-A2` finite.  A boundary divisor of `Xbar` can
dominate a divisor of `U` that another source sheet already attains.  The
reviewed Miyanishi pseudo-covering control realizes exactly this behavior by
deleting affine-line boundary components above an already-attained multiple
fibre.

Therefore no Hartogs identification `Xbar=A2`, no finite or finite-etale
first leg, and no Euler equation `1=d1` follows.  Indeed, the binding sandwich
proves `g1` nonfinite and nonproper for a hypothetical counterexample.  The
Picard, Kummer, and cofinite-image conclusions remain correct, but none is
consumed by the monodromy contradiction in Sections 2--3.  No promoted claim
depended on the discarded shortcut.

## 5. Maximum-safe conclusion and campaign scope

Promote exactly:

> A hypothetical non-invertible plane Keller map admits no strict
> intermediate field whose associated finite-flat second leg has degree
> three.

This closes the entire cubic second-leg block, including the previously live
affine Picard/Kummer and D3 sectioned-presentation proof lanes.  Their frozen
artifacts remain useful controls, but they are no longer proof-side gates for
`d2=3`.

The following remain open and are not changed by this theorem:

```text
strict intermediate blocks with deg(g2)>=4;
whether a hypothetical counterexample has any strict intermediate block;
the primitive/no-block horn;
JC2 itself.
```

In particular, rank-four `(2,2)` fibres can destroy the rank-one companion
mechanism, so no higher-degree statement may be inferred by analogy.

## 6. Verification

The producer and manifest pass `artifact_finalize.py verify`; the GPT-5.5
report passes `seal.py verify`.  On the frozen integration basis, ordinary,
`python3 -O`, and `python3 -OO` replay executions returned byte-identical JSON
with

```text
status=PASS-CUBIC-ACYCLIC-BRANCH-MONODROMY
payload_sha256=0e1afb3f3d226393fa143d972620607d46ee3db7daf8b37751fee2d2402db740
acyclic_images_transitive=false
disconnected_control_transitive=true.
```

The replay checks the finite `S3` image calculations and controls.  It does
not replace the independently reviewed classification, topology,
finite-flatness, henselian splitting, or proper-block-interface arguments.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9978`.
- Body SHA-256:
  `3b09fc7eecc5a2801abcc56e3c420261866893ea32805b1a1a5be35b003faa40`.
- Frozen basis: `2aa49d87c6a5d1823849fdc712582e064874bc8b`.
