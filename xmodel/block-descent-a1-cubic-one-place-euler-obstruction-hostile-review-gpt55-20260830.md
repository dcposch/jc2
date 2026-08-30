# Hostile review: cubic one-place Euler obstruction

Date: 2026-08-30
Reviewer: GPT-5.5 hostile audit lane
Scope: only the seven charged local files named in the prompt, plus primary-source web check for Chau's theorem.

## 0. Custody

CONFIRMED.  All seven charged SHA-256 hashes matched the prompt:

```text
8b457a752434ac0c7cb6a2a83dd680b4a66dbe3631ab761c43dc789965ff2d2d  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-sol56-20260830.md
f98149567b865f15a97b1e53c8f1ccd15fde116292e2d0c64a2935d3c45d95ae  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-sol56-20260830.md.artifact.json
931afe2d89c890d841575780bf66c3625ae54e7aa51a275ef6f27da7fb0955f2  ops/block_descent_a1_cubic_euler_replay.py
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d  xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
b72e39220f9e8d75e94214d2e5669bda072fcbbd644cfed97f97d9a2b820ad57  xmodel/block-descent-a1-euler-ledger-sol56-20260830.md
```

The artifact JSON for the principal report records the same full hash and body hash.  No receipt was charged or inspected; receipt status is therefore ABSENT as expected.

## 1. Chau theorem and `B subset A_F`

CONFIRM_WITH_CORRECTIONS.

Primary source checked: Nguyen Van Chau, "Note on the Jacobian condition and the non-proper value set", Annales Polonici Mathematici 84 (2004), 203-210, DOI `10.4064/ap84-3-2`, published by IMPAN with free PDF at `https://www.impan.pl/shop/en/publication/transaction/download/product/85283`.  The IMPAN page identifies the article, pages and DOI and states the one-point-at-infinity abstract.  In the published PDF, Theorem 1 assumes a Keller map with suitable source coordinates and says every irreducible component of `A_F` has a nonconstant polynomial parametrization with the displayed leading form.  Corollary 2 says that if `A_F` is nonempty, the whole curve `A_F` has one point at infinity and describes the branches at that point.  The arXiv source `https://arxiv.org/abs/math/0305088` has the same Theorem 1 and Corollary 2.

The charged report correctly separates these statements at `xmodel/block-descent-a1-cubic-one-place-euler-obstruction-sol56-20260830.md:89`: componentwise polynomial parametrization is not the same as saying the possibly reducible whole curve has one analytic place.  "One point at infinity" is set-theoretic for the projective closure of `A_F`; several analytic branches may meet there.

The component equality is sound.  The structure integration gives `R` nonempty pure divisorial and `g2(R) subset A(F)` at `xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md:63` and `:72`.  Since `g2` is finite, images of irreducible components of `R` are curves.  Any irreducible component `B_i` of `B=g2(R)_red` is a closed irreducible curve contained in an irreducible component of the plane curve `A_F`, hence equals that component.  The proof does not show `B=A_F`; components caused only by first-leg nonproperness may remain outside `B`.

The normalization transfer from polynomial parametrization is also sound.  A nonconstant polynomial map `A1 -> B_i` lifts to the normalization, extends to a nonconstant map `P1 -> \bar B_i^nu`, and forces genus zero by Luroth.  Because all finite source points map into the affine curve, the preimage of the punctures is contained in the single point at infinity of `P1`; hence the affine normalization has exactly one puncture and is `A1`.

Correction: the monic-coordinate clause should be read as a harmless generic source-coordinate normalization of the published theorem, not as an intrinsic target statement.

## 2. Rank-three local fibre criterion

CONFIRMED.

Let `A=O_{A2,z}` and `B=O_{Y,y}` for a closed point `y` over `z`.  The map is finite flat of finite presentation and the target is smooth over `C`.  Since `C` is algebraically closed, all closed residue fields are `C`.  The standard fibre criterion says `g2` is etale at `y` iff the local geometric fibre algebra `(B/m_zB)_y` is etale over `C`.  A finite local `C`-algebra is etale iff it is reduced, equivalently iff it is `C`, equivalently iff its length is one.

Thus every non-etale source point in a closed fibre has local fibre length at least two.  A rank-three fibre has total scheme length three, so over any `z in B(C)=g2(R)(C)` there is at least one and at most one reduced source point of `R`.  This includes singular points of the normal surface `Y`: if the local fibre length were one, finite flatness would make the local algebra rank one over `A` and hence etale, so `Y` would be smooth there.  It also includes totally ramified fibres: partition `(3)` has exactly one reduced source ramification point and no unramified point.

The criterion proves only the rank-three uniqueness of the reduced source ramification point over a branch value.  It does not prove the existence of an unramified sheet over that value.

## 3. `R_red -> B_red`

CONFIRMED.

Because `R_red` is closed in `Y` and `Y -> A2` is finite, `R_red -> A2` is finite.  Since its topological image is the closed reduced curve `B`, the map factors through `B_red`; finiteness descends to this factorization.  The rank-three criterion above gives exactly one closed source point of `R_red` over every closed point of `B_red`, and none are missing because `B` is the finite image.

Therefore `R_red(C) -> B_red(C)` is a finite point-bijective map.  Its analytification is proper and bijective between locally compact Hausdorff analytic spaces, hence a homeomorphism.  This justifies the topological equalities `e_c(R)=e_c(B)` and `b0(R)=b0(B)` used in the charged report at `xmodel/block-descent-a1-cubic-one-place-euler-obstruction-sol56-20260830.md:169`.

No scheme isomorphism follows.  Finite bijective maps such as normalizations of cusps show why conductor data can remain scheme-theoretic even when the analytic topology is fixed.  In characteristic zero the map is generically separable; closed-point bijectivity forces generic degree one on each component, so corresponding components are birational and have the same normalization.  Hence every component of `R_red` also has normalization `A1`.

## 4. Affine incidence forest and Euler sign

CONFIRMED.

The morphic rational-forest correction is charged and states that an everywhere-defined dominant morphism `A2 -> U` forces every smooth projective strict-SNC completion boundary of `U` to have rational components and forest dual multigraph with parallel edges retained; see `xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md:18` and `:83`.  The ruling-transfer integration supplies the actual block open `U=Y minus R`, smooth affine, with the first leg factoring as a dominant etale quasi-finite morphism `A2 -> U`; see `xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md:18` and `:92`.

For `R`, take a projective compactification of the normal affine surface `Y` and resolve the pair consisting of the closure of `R` plus infinity.  Over an affine singular point of `R`, embedded resolution separates branches.  Over a singular point of the normal surface `Y`, the exceptional fibre is connected and lies in the boundary because `Sing(Y) subset R` is charged at `xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md:63`.  Contracting each connected exceptional cluster over an affine multibranch point gives the incidence vertex; deleting infinity vertices and unibranch exceptional twigs gives a minor or subdivision of the actual SNC boundary graph.  Minors, subdivisions and vertex deletions of a forest remain forests.

The multigraph must retain parallel edges.  A self-node of one irreducible affine component is represented by two parallel edges between the component vertex and the singular-point vertex; that is already a two-edge cycle and is forbidden by the boundary forest.  Unibranch cusps have one normalization preimage, contribute no normalization Euler defect, and their exceptional twigs are harmless trees.

Normalization additivity gives

```text
e_c(R)=sum_i e_c(A1)-sum_p(r_p-1)=c-sum_p(r_p-1),
```

where `p` ranges over affine multibranch singular points and `r_p` is the number of normalization preimages.  If `Gamma_R` has `c+s` vertices, `E=sum r_p` edges, and `h` connected components, the forest identity `E=(c+s)-h` gives `e_c(R)=h=b0(R)`.  By the homeomorphism in section 3, `e_c(B)=b0(B)>=1`.

## 5. Cubic Euler equations

CONFIRM_WITH_CORRECTIONS.

Conditional on the finite `S0`/generic fixed-sheet input, the cubic Euler arithmetic is correct.  The charged Euler ledger derives

```text
u(z)=3  outside B,
u(z)=1  on B minus S0,
u(z)=0  on S0,
e(U)=3-2e(B)-|S0|
```

at `xmodel/block-descent-a1-euler-ledger-sol56-20260830.md:230`.  The principal report repeats the same census at `xmodel/block-descent-a1-cubic-one-place-euler-obstruction-sol56-20260830.md:244`.  With `e(B)=b0(B)>=1` and the ruling identity `e(U)=e(C)+Q`, `Q=sum_t(q_t-1)>=0`, the displayed conclusions follow:

```text
C=P1:  2b0(B)+|S0|+Q=1, impossible.
C=A1:  2b0(B)+|S0|+Q=2, hence b0(B)=1, S0=empty, Q=0.
```

The meanings need to stay narrow.  `S0=empty` means every target point has at least one unramified block sheet; over a branch value in rank three it is exactly one unramified sheet plus the unique ramified source point.  It does not make `g2|U` finite flat of degree three.  `Q=0` means every reduced ruling fibre has one `A1` component; it does not assert reduced scheme fibres, multiplicity one, or absence of special values.

Correction and gap in the allowed packet: the finite `S0`/generic fixed-sheet theorem is cited as promoted input in the principal report, but its listed source is an uncharged `block-descent-galois` integration at `xmodel/block-descent-a1-cubic-one-place-euler-obstruction-sol56-20260830.md:70`.  I did not read it because it was outside the allowed charged-file list.  Within the seven-file packet, a whole branch component with generic partition `(3)` is not independently excluded.  If that escape were allowed, `S0` would contain a curve and the cubic census above would not be the right Euler formula.  Therefore the Euler closure is confirmed only after explicitly charging the fixed-sheet input.

## 6. Degree-four and conductor attacks

CONFIRMED.

The obstruction is rank-three-only.  The rank-three bridge uses the length inequality `2+2>3`; at degree four the partition `(2,2)` allows two reduced source ramification points over one target branch value.  Then `R_red -> B_red` need not be point-bijective.  A finite image can identify two source points, glue branches, lower Euler characteristic, or create target conductor topology not visible on the source forest.  This is not a technical inconvenience; it is exactly the target-conductor escape that the cubic length argument closes.

The report therefore correctly refuses to exclude degree-four blocks, the surviving affine-base cubic row, the existence of a proper block, an actual Keller counterexample, or JC2.  The affine-base survivor after the cubic obstruction is still only constrained by `b0(B)=1`, `S0=empty`, and `Q=0`.

## 7. Replay

CONFIRMED.

The replay source `ops/block_descent_a1_cubic_euler_replay.py` uses explicit `require(...)` guards and catches `RuntimeError` in `main`; see lines `17` and `99`.  It has zero Python AST `assert` nodes.

I reran it with bytecode writes disabled:

```text
env PYTHONDONTWRITEBYTECODE=1 python3 ops/block_descent_a1_cubic_euler_replay.py
env PYTHONDONTWRITEBYTECODE=1 python3 -O ops/block_descent_a1_cubic_euler_replay.py
env PYTHONDONTWRITEBYTECODE=1 python3 -OO ops/block_descent_a1_cubic_euler_replay.py
```

All three runs printed the same data:

```text
branch_fibre_rows = [(3) with u=0, (2,1) with u=1]
forest_checks = 1014
a1_solutions = [(1,0,0)]
p1_solutions = []
result = "BD-A1-CUBIC-EULER PASS"
payload_sha256 = 294c5674644c2b9de8a4a21be8391d1c2ee45f10d33b9aa846eb06107ecc7532
```

The mutations fail as intended:

```text
--mutate-rank-four       exit 1, FAIL:cubic fibre length is not three
--mutate-drop-one-place  exit 1, FAIL:one-place normalization is required for forest Euler positivity
```

The software verifies only finite partition arithmetic, finite forest-row arithmetic, and the terminal nonnegative-integer Euler equations.  It does not verify Chau's theorem, the block-structure theorem, the fixed-sheet theorem, the morphic rational-forest theorem, the rank-three local fibre criterion, or the analytic homeomorphism argument.

## 8. Maximum-safe theorem

CONFIRM_WITH_CORRECTIONS.

The maximum safe theorem from the charged packet is conditional:

> Assume the promoted proper cubic block sandwich, the charged morphic `A2 -> U` rational-forest theorem, the charged ruling Euler identity, Chau's published nonproper-value theorem, and additionally the fixed-sheet input that makes `S0=A2 minus g2(U)` finite on the target branch.  Then `R_red -> B_red` is finite and point-bijective, hence an analytic homeomorphism; every component of `R_red` and `B_red` has normalization `A1`; the affine incidence graph of `R` is a forest; and `e_c(B)=b0(B)>=1`.  Consequently `C=P1` is impossible for such a proper cubic block, while `C=A1` forces `b0(B)=1`, `S0=empty`, and `Q=0`.

This theorem is not a scheme-isomorphism statement for `R_red -> B_red`, not an exclusion of the affine-base survivor, not a degree-four theorem, not a proper-block existence or nonexistence theorem, and not a proof of JC2.

## 9. Cheapest useful successor

GAP.

The cheapest useful successor is to isolate and hostile-audit the fixed-sheet theorem for this exact cubic block interface: prove, without importing an uncharged packet, that every irreducible component of `B` has a generically unramified point of `g2|U` over it, equivalently that the generic branch partition is `(2,1)` rather than `(3)`.  That single input turns the currently conditional Euler closure into a closed seven-file theorem.  If it fails, the immediate counterexample shape is a target branch component contained generically in `S0`, and the displayed cubic Euler equation must be replaced.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14484`.
- Body SHA-256:
  `b16c4bc1ed5756ad39db1f44bc1bdf0fb462de9a0afdc5a5285ae27e712b4fe1`.
- Frozen basis: `f86884a5ab78e5248977942f93547fbf25b5be8e`.
