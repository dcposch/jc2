# Hostile review: acyclic branch obstruction to a cubic block

Date: 2026-08-30
Reviewer: GPT-5.5 hostile reconstruction
Scope: charged repository files named in the prompt, plus the charged
Arzhantsev--Zaidenberg PDF.  I did not inspect `jc2-lean`, sibling
external-model prompts, logs, reports, receipts, canonical ledgers, or
unrelated repository files.

## Input custody

All nine prompt SHA-256 hashes matched:

```text
5be2e2af32c0f6201637a652d28a0ff5f6992c5ebde696b1198d7b94e4829cf7
  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-obstruction-sol56-20260830.md
5fd8b854452bf4e42a96ccaea89ca8b4be09310dc0cff424ae6dd0261392a455
  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-obstruction-sol56-20260830.md.artifact.json
648022d35191b67d9f1e1eec61cddc95bbee745001410ad1fbbffa1044417389
  ops/block_descent_a1_cubic_acyclic_branch_monodromy_replay.py
41245c20b1b61a0dcf8116340672d037b977e6759d5d99054fc06c292d5c36fc
  refs/arzhantsev_zaidenberg_acyclic_curves_arxiv1110.3028v2.pdf
2e6d82035df6717d1a39f31dc19b23b7c727bb940d4730d2c7ea9400e5433cce
  xmodel/block-descent-a1-cubic-affine-survivor-funnel-sol56-20260830.md
9e32b0fe8835b6ea6002036b95e2261a612754d73d796cb10edda347cf3cf65e
  xmodel/block-descent-a1-cubic-affine-survivor-funnel-hostile-review-gpt55-20260830.md
8ccb92fd3676e9f8b58e3ace4eb9157d0fa290ea24abc84d9913e94ec407e16d
  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-coordinator-integration-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
```

Receipt status: `ABSENT` is expected.  This review makes no exit-price
assertion.

## Itemized audit

1. `CONFIRM_WITH_CORRECTIONS`: Arzhantsev--Zaidenberg coverage and the
proper-cubic hypotheses.

The pinned PDF defines an acyclic curve as connected and simply connected,
then Theorem 1.3(b) states the broader classification for any reduced simply
connected plane curve.  That statement is not restricted to irreducible
curves; it explicitly includes reducible forms

```text
y^epsilon_y p(x)=0
x^epsilon_x y^epsilon_y product_i (y^a-kappa_i x^b)=0,
```

with `epsilon_x,epsilon_y in {0,1}`, `p` squarefree, `a,b>=1` coprime, `r>0`,
and distinct nonzero `kappa_i`.  Thus every reduced connected simply connected
plane curve is covered.  Connectedness is an extra specialization imposed on
the normal forms, not a missing source hypothesis.

The campaign interface must not infer contractibility from Euler
characteristic alone.  The charged proper-cubic path gives more: `R_red -> B`
is a finite point-bijective analytic homeomorphism, components have
normalization `A1`, the affine incidence graph is a forest, and the survivor
row has `b0(B)=1`.  A connected tree of contractible normalizations glued only
along the forest incidence pattern is topologically contractible.  That is the
safe route into the classification.  The new theorem's standalone assumption
that `B` is topologically contractible is therefore stronger than the Euler
identity and is safe when this full charged topology package is imported.

2. `CONFIRMED`: local cubic splitting and global transitivity.

Let `pi:Y -> A2_C` be finite flat of degree three with `Y` integral and normal,
and let `B` be the reduced branch support.  Over `U=A2-B`, the restriction
`V=Y-pi^{-1}(B) -> U` is finite etale of degree three.  Since `V` is a nonempty
open subset of integral `Y`, it is connected, so the topological monodromy on
the three sheets is transitive.

At any point `b in B`, including singular points of the reduced branch curve,
the henselian local finite algebra has special fibre with two support
idempotents of lengths two and one.  Henselian idempotent lifting splits the
rank-three algebra into rank-two and rank-one finite-flat factors.  A unital
rank-one finite-flat algebra over the local base is the base itself; analytically
this is the local companion section.  Hence the whole local complement group,
not just a smooth-branch meridian, fixes the companion sheet after a based
identification.  At a generic smooth point of a branch component, the rank-two
ramified factor contributes a nontrivial transposition.

This confirms both halves that must be kept separate: local groups fix local
companions, while the global complement cover is transitive.  In the promoted
cubic survivor the transitive image also contains a transposition, hence is
`S3`.

3. `CONFIRMED`: the comb case and based meridians.

For `y^epsilon_y p(x)=0`, connectedness leaves exactly these cases:

```text
one vertical line             epsilon_y=0 and p has one root;
one horizontal line           epsilon_y=1 and p is constant;
a genuine comb                epsilon_y=1 and p has s>=1 simple roots.
```

The line cases have complement fundamental group `Z`; the branch meridian maps
to a transposition, so the image has order two and cannot be transitive on
three letters.

For a comb with roots `alpha_1,...,alpha_s`,

```text
A2-B = (C-{alpha_1,...,alpha_s}) x C*
pi1(A2-B) = F_s x <h>,
```

where `h` is the based meridian of the horizontal spine and is central.  The
generic `(2,1)` fibre along the spine gives `rho(h)=tau`, a transposition.
For every based loop `gamma`, centrality gives `rho(gamma) tau = tau
rho(gamma)`.  The centralizer of a transposition in `S3` is exactly the
two-element subgroup generated by it, so the entire image lies in `<tau>` and
is intransitive.

This argument does not identify tooth companions by hand.  The common label is
forced only after the globally based central spine meridian has been mapped to
a transposition.

4. `CONFIRM_WITH_CORRECTIONS`: the weighted-cone case.

The weights in the charged proof are correct.  Under positive real scaling

```text
r.(x,y)=(r^a x,r^b y),
```

both `y^a` and `x^b` acquire weight `ab`, and the optional coordinate axes are
invariant.  With

```text
N(x,y)=|x|^(2/a)+|y|^(2/b),
```

one has `N(r.(x,y))=r^2 N(x,y)`, so every positive orbit in `A2-{0}` meets a
weighted link `N=const` exactly once.

The wording should be through punctured weighted sublevel neighborhoods:
`A2-B` and `{0<N<delta}-B` both deformation retract by this radial flow to the
same weighted link complement.  Ordinary Euclidean balls and these weighted
sublevels are cofinal neighborhoods of the origin, so this computes the usual
origin-local complement group.  With that wording, the global complement group
is the origin-local complement group.

Applying the henselian rank-one companion factor at the origin then places the
whole global monodromy image in a single companion-fixing `S2`.  This is enough:
an `S2` subgroup of `S3` is intransitive.  The proof covers optional axes,
`a=b=1` line arrangements through the origin, smooth weighted rows with one
exponent equal to one, and irreducible cusps.

5. `CONFIRMED`: edge-case controls.

One line gives `pi1=Z` and a transposition image, hence no connected cubic
cover.  One tooth gives `C* x C*`; its two meridians commute, so the spine
transposition forces the tooth transposition to be the same one.  Several teeth
are handled by the same product `F_s x Z`.  The coordinate axes `xy=0` are just
the one-tooth comb.  The `a=b=1` rows are central line arrangements and are
covered by the weighted-cone argument.  Irreducible cusps are weighted cones,
so their global complement is already the origin-local complement for this
purpose.

The two readings of "one point/place at infinity" do not enlarge the proof.
Componentwise one-place is not needed after the curve is known contractible and
classified.  A stronger single set-theoretic infinity point only deletes
nontrivial combs and most central line arrangements; it does not create a new
case.

The disconnected algebraic `S3` control from the prior review remains a real
warning.  The cubic `z^3-3z+2+xy=0` has local `(2,1)` companions and global
`S3` monodromy, but its branch support has two connected components.  The new
proof avoids that failure mode precisely by using the classified connected
contractible forms: a comb has a central global spine meridian, and a weighted
cone has one local group equal to the global group.

6. `CONFIRMED`: exact proper-block interface.

The standalone geometric theorem is a degree-three finite-flat branch theorem.
It does not require the whole Jacobian-conjecture machine, but the campaign may
apply it only after the charged proper-cubic inputs supply all of its
hypotheses: integral normal finite-flat cubic cover, reduced connected
topologically contractible branch support, connected complement cover, and
`(2,1)` fibre partition at every branch value.

With those inputs, the promoted proper cubic block is empty.  The earlier
affine-survivor funnel had already removed the smooth branch row; this
classification argument removes the singular and reducible connected acyclic
branch row.  The conclusion is only about the proper block with cubic second
leg `deg(g2)=3`.

Nothing here excludes proper blocks of degree at least four.  Nothing here
touches the primitive/no-proper-block horn.  No statement about JC2 itself
follows except the conditional corollary that a noninvertible Keller map cannot
pass through this promoted proper-cubic block configuration.

7. `CONFIRMED`: replay and its limits.

Ordinary, `-O`, and `-OO` executions all produced the same payload:

```json
{"acyclic_images_transitive": false, "comb_admissible_counts_by_teeth": {"1": 3, "2": 3, "3": 3, "4": 3, "5": 3, "6": 3}, "cone_image_order": 2, "disconnected_control_image_order": 6, "disconnected_control_transitive": true, "payload_sha256": "0e1afb3f3d226393fa143d972620607d46ee3db7daf8b37751fee2d2402db740", "s3_order": 6, "status": "PASS-CUBIC-ACYCLIC-BRANCH-MONODROMY", "transposition_count": 3}
```

The deliberate mutation `--mutate-drop-comb-centrality` failed in ordinary,
`-O`, and `-OO` modes with:

```text
RuntimeError: comb with 1 teeth must have one common transposition label
```

The script uses explicit `require` checks, not Python `assert`, so optimization
does not erase the validation.  Its scope is finite and deliberately narrow:
it checks the `S3` consequences of centrality and one local companion-fixing
subgroup.  It does not verify the Arzhantsev--Zaidenberg classification,
product complement, weighted radial deformation, henselian splitting,
finite-flat cover hypotheses, proper-block interface, or branch
contractibility.

## Maximum-safe theorem

The following is safe.

Let `pi:Y -> A2_C` be finite flat of degree three, with `Y` integral and
normal.  Let `B` be the reduced branch support.  Assume:

```text
B is connected and topologically contractible;
every geometric fibre over every point of B has partition (2,1).
```

Then no such cover exists.  Indeed, `Y-pi^{-1}(B) -> A2-B` is a connected
degree-three etale cover and therefore has transitive monodromy.  The
Arzhantsev--Zaidenberg normal forms for reduced simply connected plane curves
force the same monodromy image to be contained in a single order-two subgroup
of `S3`: by centrality of the spine meridian in the comb case, and by equality
of global and origin-local complement groups in the weighted-cone case.  This
contradicts transitivity.

Campaign corollary: subject to the charged proper-block integrations, the
proper cubic block `deg(g2)=3` is closed.  This is not a theorem about
`deg(g2)>=4`, not a primitive-horn theorem, and not JC2.

## Cheapest useful successor

First record the coordinator-level corollary only at this scope: promoted
proper cubic blocks are impossible.  Do not attach any higher-degree or
primitive consequence.

The cheapest new mathematical work is a degree-`>=4` feasibility screen before
another geometric proof attempt.  Enumerate transitive subgroups and allowed
local fibre partitions for classified connected acyclic branch supports, with
the comb central meridian and weighted-cone local/global identification kept
explicit.  The rank-four danger is visible already: `(2,2)` fibres can remove
the cubic rank-one companion mechanism, so the cubic proof should not be
generalized by analogy.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12263`.
- Body SHA-256:
  `3bbad2b21b1fa5bf59ba5ea14576ff8f7afe00a130f5dbd14f16efd3acc12340`.
- Frozen basis: `03a4d8dc557abf1e23e5a039ff5c995131935ff2`.
