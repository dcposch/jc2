# Hostile review: proper-cubic affine-survivor funnel

Date: 2026-08-30
Reviewer: GPT-5.5 hostile reconstruction
Scope: charged files only, plus the permitted temporary arXiv fetch of Miyanishi
`1504.07179`.

## Input custody

All seven charged repository SHA-256 hashes matched the prompt:

```text
2e6d82035df6717d1a39f31dc19b23b7c727bb940d4730d2c7ea9400e5433cce  xmodel/block-descent-a1-cubic-affine-survivor-funnel-sol56-20260830.md
a38d1ba420fa8388fbf453051bd9d570edbfe99f0a1ff240f1f297d1e6718fcd  xmodel/block-descent-a1-cubic-affine-survivor-funnel-sol56-20260830.md.artifact.json
aa198a357ce3c7dd3df6c97019f76553f27c76e5f4b7928ed3e52104de3f3915  ops/block_descent_a1_cubic_affine_survivor_replay.py
8ccb92fd3676e9f8b58e3ace4eb9157d0fa290ea24abc84d9913e94ec407e16d  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-coordinator-integration-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db  refs/jc86.pdf
```

Miyanishi arXiv `1504.07179` was fetched only into `/tmp`.  Its SHA-256
matched the expected
`ab4eb0cb74e4051e3fb1f702a253d29cb1a658632f11bc6f4b04a8bb9e7daaa4`.
I did not inspect `jc2-lean`, sibling external-model prompts, logs, reports,
receipts, canonical ledgers, or unrelated repository files.

Receipt status: `ABSENT`, as expected.  This review makes no exit-price
assertion.

## Itemized audit

1. `CONFIRM_WITH_CORRECTIONS`: Miyanishi input and transverse source line.

Miyanishi Lemma 1.4.16 is general for a smooth affine surface with an
`A1`-fibration over `A1`; it is not restricted to the later typed
`(d,n,r)` pseudo-planes.  Since `h=rho o g1` is a nonconstant polynomial on
`A2`, a general affine source line has nonconstant `h|L`, hence gives a
nonconstant morphism `A1 -> U` transverse to `rho`.  This uses dominance of
`g1`, not any compatibility of `g1` with the ruling.

The Picard and acyclicity package needs the full affine-base and one-component
fibre hypotheses.  Miyanishi Lemma 1.4.3 gives fibres as disjoint unions of
affine lines, the Picard product by fibre multiplicities when every fibre is
irreducible over base `A1`, and `Q`-homology acyclicity under the same
one-component hypothesis.  Corollary 1.4.4 then gives cyclic order `m` when
there is exactly one multiple fibre `mF`.  Thus the funnel may use
`Pic(U)=Z/m<[F]>` only after importing the affine survivor row `Q=0` and after
the no-multiple row is excluded.

2. `CONFIRM_WITH_CORRECTIONS`: no-multiple-fibre row.

If every reduced fibre is one `A1` and there are no multiple fibres, each
scheme fibre is a reduced smooth affine line.  For a morphism from a smooth
surface to a smooth curve this gives flatness by equidimensionality and then
smoothness by smooth fibres.  One still needs the standard theorem that a
smooth `A1`-fibration over a smooth curve is an `A1`-bundle.  Over `A1`, the
line-bundle and additive torsor classes vanish, so `U ~= A2`.

Only at that point does Orevkov apply.  Theorem 1.1 of `refs/jc86.pdf` is about
two- or three-sheeted polynomial maps `C2 -> C2` with nonzero constant
Jacobian.  After `U ~= A2`, the etale map `pi:U -> A2` is such a polynomial
Keller self-map of generic degree three.  Orevkov is not licensed directly on
an arbitrary pseudo-plane.

3. `CONFIRMED`: localization and the Hartogs/Zariski-Main warning.

Let `V=g1(A2)`.  Since `g1` is etale, `V` is open in `U`.  If a divisor
supported in `U - V` were principal, say `div(b)`, then `b` and `b^-1` are
regular on `V`; pulling back to `A2` gives inverse polynomials, hence scalars.
Dominance makes `b` scalar.  Therefore the free abelian group on missed prime
divisors injects into `Pic(U)`.  Since `Pic(U)` is finite, no missed divisor
exists, so `U - g1(A2)` is finite.

This proves only the target statement "no divisorial component is missed in
`U`."  It does not say that the Zariski-Main finite normalization has finite
boundary over `A2`.  Miyanishi Lemma 2.5.2 is exactly the countercontrol: the
cyclic etale cover splits the multiple fibre into `m` affine lines, and deleting
`m-1` of them leaves an open `A2` still mapping surjectively to the pseudo-plane;
the deleted divisors map onto an already attained target fibre.

4. `CONFIRMED`: Kummer divisibility and canonical class.

Choose the base coordinate with `div_U(t)=mF`.  Since `g1` is etale, the pullback
of the reduced smooth Cartier divisor `F` is reduced.  In the UFD `C[x,y]`,
`div(g1^*t)=m g1^*F` therefore gives `g1^*t=cP^m` with `c in C*`.

For each prime `p|m`, if `t/c=s^p` in `C(U)`, then `s` is integral over
`O(U)` and hence regular because `U` is normal affine.  Its divisor would be
`(m/p)F`, contradicting the exact order `m` of `[F]` in `Pic(U)`.  Since `C`
contains all roots of unity, the usual Kummer binomial criterion has no
composite-`m` or fourth-root exception here.  Thus `X^m-t/c` is irreducible
over `C(U)`, `C(U)(P)` has degree `m`, and the tower law gives `m|d1`.

Separately, etaleness of `pi:U -> A2` gives
`omega_U ~= pi^* omega_A2`, hence `K_U ~ 0`.  The typed Miyanishi theorem
2.5.10 is not a coverage theorem: it applies only after the additional
`(d,n,r)` boundary type is proved.

5. `CONFIRM_WITH_CORRECTIONS`: companion section over `B`.

The conclusion `T=U times_(A2) B -> B` is an isomorphism is correct, including
at singular and reducible points of the reduced curve `B`, but the proof should
not pass through finiteness of `U -> A2`.  The right argument is local:
finite-flat rank three plus `S0=empty` gives, over every geometric branch value,
one non-etale length-two point and one etale length-one companion point.  Base
change of the etale locus gives an etale morphism `T -> B` with one geometric
point in every fibre.  Hence it is surjective, radicial, and etale; an etale
radicial morphism is an open immersion, and surjectivity makes it an
isomorphism.

For each irreducible component `B_i=(b_i=0)` of the reduced plane curve,
`U times B_i -> B_i` is the corresponding component `T_i`, and etale pullback
of the reduced Cartier divisor gives `div_U(pi^*b_i)=T_i` with coefficient one.
This is componentwise principal Cartier data, not an identification with a
ruling fibre or an original source sheet.

6. `CONFIRM_WITH_CORRECTIONS`: complement cover and local companion groups.

`W=U-T` is the same open as `Y - g2^{-1}(B)`.  Since `g2:Y -> A2` is finite flat
of rank three, `W -> A2-B` is finite etale of degree three.  Since `Y` is
integral, this nonempty open is connected.  The monodromy is transitive; the
generic inertia along a branch component has type `(2,1)`, so the image contains
a transposition and is therefore `S3`.

At any affine point of `B`, henselian idempotent lifting splits the completed
rank-three algebra into a rank-one etale companion factor and a rank-two
ramified factor.  Thus the local complement group fixes a companion sheet.
However, that is a local statement after choosing paths from the global
basepoint.  It does not by itself produce a single globally fixed sheet.

Control against the stronger inference: the cubic surface

```text
S = Spec C[x,y,z]/(z^3 - 3z + 2 + xy) -> A2_{x,y}
```

is finite flat of rank three.  Its branch support is
`xy(xy+4)=0`; fibres over `xy=0` have root pattern `(z-1)^2(z+2)`, and fibres
over `xy=-4` have pattern `(z+1)^2(z-2)`, so every branch value has a local
companion.  At the node `(0,0)`, the completed algebra has one companion factor
and one double ramified factor.  The total surface is integral, and its only
singularity is the isolated hypersurface point `(0,0,1)`, hence it is normal.
The line `y=1` sees the one-parameter cubic
`z^3-3z+2+q` over `q in A1-{0,-4}`, whose two transposition inertias generate
`S3`; therefore the global monodromy has no fixed sheet.  This is not a
survivor because its branch is disconnected and not the campaign `U`, but it
blocks any proof that promotes local companion-fixing to a global label without
using the connected one-place forest hypotheses.

7. `CONFIRM_WITH_CORRECTIONS`: smooth branch contradiction; singular/reducible
case remains open.

If `B` is smooth and connected, Chau's theorem gives normalization `A1`, hence
`B ~= A1`.  Abhyankar-Moh rectifies the embedding to a coordinate line, so
`A2-B ~= Gm times A1` and `pi_1(A2-B)=Z`.  A connected degree-three cover with
cyclic monodromy must be generated by a 3-cycle, while the branch meridian from
the finite-flat cubic has transposition inertia.  This contradiction is solid.

Nothing comparable is proved for singular or reducible contractible one-place
forests.  Their complement groups need not be cyclic, and the local companion
subgroups do not yet have a proved common global label.  The remaining escape
is precisely global braid/infinity monodromy compatible with all affine local
groups landing in companion-fixing `S2` subgroups.

8. `CONFIRMED`: replay.

Ordinary, `-O`, and `-OO` all produced the same payload:

```json
{"charged_cyclic_action_transitive": false, "charged_fibre_type": [2, 1], "payload_sha256": "a602c5ca9ca141166143b504b32d835b064ea06b4f5d3618876d1b26faefd834", "s3_order": 6, "status": "PASS-CUBIC-AFFINE-SMOOTH-BRANCH-MONODROMY", "three_cycle_count": 2, "transposition_count": 3}
```

The deliberate mutation `--mutate-transposition-to-3cycle` was rejected in all
three modes with `RuntimeError: mutation changed the charged cubic fibre type`.
The script uses explicit `require` calls, not Python `assert`, so optimization
does not erase the checks.

The replay verifies only a finite `S3` permutation fact: a cyclic subgroup
generated by a transposition is not transitive on three letters, while a
3-cycle is.  It does not verify the Miyanishi hypotheses, no-multiple-to-bundle
step, Orevkov applicability, Picard/Kummer package, companion-section theorem,
normality, branch topology, Chau, Abhyankar-Moh, or any singular/reducible
forest obstruction.

## Maximum-safe theorem

For an actual promoted proper cubic affine survivor, assuming the charged
proper-block, ruling-transfer, fixed-sheet, and one-place Euler inputs, the
following is safe:

```text
rho:U -> A1 has exactly one multiple fibre mF with m>=2.
Pic(U)=Z/m<[F]>.
H_i(U;Q)=0 for i>0.
U - g1(A2) is finite.
m divides d1.
K_U ~ 0.
T=U times_(A2) B -> B is an isomorphism.
W=U-T -> A2-B is connected finite etale of degree three with S3 monodromy.
Every affine local complement group fixes its local companion sheet.
B is not smooth.
```

With the imported one-place/forest theorem, `B` is therefore singular or
reducible, connected, contractible, and one-place in the charged sense.  The
theorem does not exclude that remaining singular/reducible branch, does not
prove global companion-label propagation, does not place arbitrary `U` in
Miyanishi's typed `(d,n,r)` class, and does not make any statement about degree
at least four or the primitive/no-block horn.

## Cheapest useful successor

The cheapest successor is a topology-and-realization check, not another
Picard/Kummer pass:

1. Build van Kampen or splice presentations for connected contractible
   one-place forest curves, keeping every affine local subgroup and the infinity
   group separate.
2. Search first for explicit `S3` representations in which each affine local
   group lands in a companion-fixing `S2`; only after that fails should one try
   to prove common-label propagation.
3. In parallel, test whether the proper-block boundary forces the ramification
   resolution arms into the linear situation used by Orevkov's local knot
   argument.  That added hypothesis would push the branch back to the smooth
   contradiction.

Typed result for the unresolved gate: `OPEN`.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11904`.
- Body SHA-256:
  `302f12e6ba08291a14b7c0cd5651c4e2ede664f44cf486244ca04f2c20b0507b`.
- Frozen basis: `384d3d6b64887989b9f2e50b787b573c9d01b179`.
