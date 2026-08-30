# Hostile rereview: rational-forest morphic correction

Date: 2026-08-30 UTC
Reviewer: GPT-5.5
Scope: only the seven charged files named in the mandate were hash-checked and read. No sibling prompt, log, report, receipt, canonical ledger, Git state, charged input, or `jc2-lean` path was inspected or modified.

All seven charged SHA-256 hashes match the mandate exactly. No exit-price assertion is made; receipt status is ABSENT.

## 0. Verdict

Overall: **CONFIRM_WITH_CORRECTIONS**.

The correction is right on the main point. The rational-forest obstruction is a morphic obstruction, not a consequence of an arbitrary dominant rational map from `A^2` to the open surface. The previous hostile review and coordinator integration promoted a false strengthening at `bd-a2-rational-forest-multisection-hostile-review-opus5-20260830.md:107`-`111`, `344`-`350`, and `bd-a2-rational-forest-coordinator-integration-sol56-20260830.md:59`-`72`.

Itemized status:

```text
1. Smooth cubic U=P^2\E counterexample to rational-map gate          CONFIRMED
2. Everywhere-defined dominant morphism A^2 -> U gate                CONFIRMED
3. Shrinking and log-plurigenus monotonicity                          CONFIRM_WITH_CORRECTIONS
4. Actual proper-block use with V=g1(A^2)                             CONFIRMED
5. Downstream rational-domination wording                             REFUTED where log/boundary is inferred
6. Pure residue/multisection/classification algebra                   CONFIRMED, with morphic-use retagging
```

## 1. Smooth Cubic Counterexample: CONFIRMED

Let `E subset P^2` be a smooth plane cubic and set `U=P^2 \ E`, as in the correction at `bd-a2-rational-forest-morphic-correction-sol56-20260830.md:32`-`50`.

Choose the standard affine chart `A^2=P^2 \ L`. The identity on `P^2` restricts on

```text
A^2 \ (E cap A^2) = P^2 \ (E union L)
```

to a morphism into `U`. This defines a dominant rational map

```text
A^2 dashrightarrow U.
```

It is dominant because `P^2 \ (E union L)` is dense in the irreducible surface `U`. It is not an everywhere-defined morphism `A^2 -> U`, since every point of `E cap A^2` would have to map by the identity to a point outside `U`.

The log invariants are decisive. For the smooth strict-SNC completion `(P^2,E)`,

```text
K_{P^2}+E = -3H+3H = 0.
```

Hence for every `m>=1`,

```text
barP_m(U)=h^0(P^2, O)=1,
bar kappa(U)=0.
```

Also `p_g(P^2)=q(P^2)=0`. The boundary has one smooth component of genus one and no graph edge:

```text
sum_i g(E_i)=1,
b1(Gamma_E)=0,
tau(E)=1.
```

Thus the boundary is not a rational forest. Boundary blowups do not repair this: the strict transform of `E` still has genus one, and added exceptional curves only attach rational tree data.

The exact false step in the old proof is not ordinary resolution for a proper target; it is applying that instinct to the nonproper open target. A rational map to a projective completion `X` can be resolved, but the resulting morphism need not factor through `U=X\D`. In the cubic example, any alleged resolution `W -> A^2` and morphism `W -> U` extending the identity would, after composing with `U hookrightarrow P^2`, equal the blowdown/inclusion map to `P^2`. Points over `E cap A^2` would then map to `E`, contradicting that the image lies in `U`. To obtain a genuine morphism into `U`, one must delete the interior pole divisor from the source; that changes the open source from `A^2` to `A^2 \ E_aff`, whose log plurigenera are not those of `A^2`.

Therefore the rational-map extension is **REFUTED**.

## 2. Morphic Theorem: CONFIRMED

The strongest safe theorem is the morphic theorem, with no surjectivity, quasi-finiteness, or etaleness hypothesis added.

**Theorem.** Let `U` be a smooth quasi-projective complex surface and let

```text
f:A^2 -> U
```

be an everywhere-defined dominant morphism. For every smooth projective strict-SNC completion `U=X\D`, every component of `D` is rational and the dual multigraph `Gamma_D`, retaining parallel edges, is a forest.

Proof. Embed `A^2` in `P^2` with boundary line `L`. The composite `A^2 -> U hookrightarrow X` is regular on all of `A^2`, so the rational map `P^2 dashrightarrow X` has no indeterminacy over `A^2`; all centers needed to resolve it lie over `L`. After resolving and performing harmless boundary blowups,

```text
pi:W -> P^2,
F:W -> X,
B=(pi^{-1}L)_red,
W\B = A^2,
F^{-1}(D) subset B.
```

Here `W` is rational, `B` is strict SNC, and `F` is dominant and generically finite because `f` is dominant between surfaces. Quasi-finiteness is automatic only generically; it is not needed as an input.

Logarithmic pullback gives, for each `m>=1`,

```text
H^0(X, m(K_X+D)) hookrightarrow H^0(W, m(K_W+B)).
```

The right side is the `m`th log plurigenus of `A^2`, hence zero. For example on `(P^2,L)`, `K_{P^2}+L=-2H`, and boundary blowups over `L` do not create log pluricanonical sections. Thus

```text
barP_m(U)=0 for all m>=1.
```

Ordinary forms also pull back injectively along the generically finite map `F`:

```text
H^0(X,K_X) hookrightarrow H^0(W,K_W)=0,
H^0(X,Omega_X^1) hookrightarrow H^0(W,Omega_W^1)=0.
```

Since `W` is rational and `X` is smooth projective over `C`, this gives

```text
p_g(X)=0,
q(X)=0.
```

For a possibly disconnected reduced strict-SNC boundary `D=sum D_i`, the residue sequence

```text
0 -> omega_X -> omega_X(D) -> omega_D -> 0
```

and normalization of the nodal curve `D` give

```text
barP_1(U)=p_g(X)+tau(D)-rank(partial),
rank(partial)<=q(X),
tau(D)=sum_i g(D_i)+b1(Gamma_D).
```

If `V,E,c` denote the numbers of vertices, edges, and connected components of the dual multigraph, then `b1=E-V+c`; parallel intersections are separate edges. This is the correct formula for disconnected boundaries.

With `p_g=q=barP_1=0`, one obtains `tau(D)=0`. Both summands in `tau` are nonnegative, so every `D_i` has genus zero and `b1(Gamma_D)=0`.

Surjectivity onto `U` is not needed. Etaleness is not needed. Quasi-finiteness is not needed except as the generically finite consequence of dominance. The essential hypothesis is that the map from all of `A^2` to the chosen open `U` is everywhere defined.

## 3. Shrinking: CONFIRM_WITH_CORRECTIONS

Numerical monotonicity is true:

```text
U' subset U dense open  =>  barP_m(U') >= barP_m(U).
```

On a common smooth completion this is just `D' >= D`, hence `K_X+D' = K_X+D+effective`. Equivalently, adding boundary cannot remove a positive-genus component already present, and cannot destroy an existing graph cycle; it only adds vertices/edges or subdivides existing edges. Parallel edges must be kept, since two components meeting twice already give `b1=1`.

But this monotonicity is not a morphism-producing device. If `f:A^2 -> U` is a morphism and `U' subset U`, the theorem applies to `U'` only when the full image satisfies `f(A^2) subset U'`. Restricting the rational domain, or deleting from the source the preimage of the new boundary, does not give an everywhere-defined morphism from `A^2`.

This is exactly what the cubic example exposes. The open `P^2\E` is rationally reached from a dense open of `A^2`, but not morphically reached from all of `A^2`; its positive log plurigenus survives.

Therefore the correction's shrinking warning at `bd-a2-rational-forest-morphic-correction-sol56-20260830.md:160`-`161` is confirmed. The earlier integration sentence that "any one boundary subconfiguration ... forbids a dominant rational first leg" (`bd-a2-rational-forest-coordinator-integration-sol56-20260830.md:69`-`72`) must be reworded to "forbids an everywhere-defined dominant morphic first leg whose image lands in that open."

## 4. Proper-Block Use: CONFIRMED

The actual proper-block interface survives. The block-structure integration states that for a nontrivial intermediate block

```text
A^2 --g1--> Y --g2--> A^2
```

the map `g1` is everywhere-defined, dominant, quasi-finite, etale, and open, and

```text
g1(A^2) subset Y_sm \ R,
Sing(Y) subset R
```

at `block-descent-structure-coordinator-integration-sol56-20260830.md:61`-`68` and `103`-`112`.

Set

```text
V=g1(A^2).
```

Then `V` is an open smooth quasi-projective surface, and `g1:A^2 -> V` is an everywhere-defined surjective, hence dominant, morphism. This licenses the morphic rational-forest theorem directly. No equality `V=Y\R`, no properness of `g1`, and no rational-map strengthening is needed. Etaleness is used upstream to know that `V` is open and smooth; the rational-forest theorem itself does not require etaleness.

Now let `p in Y\V`, for example a singular point. On any common smooth projective resolution/completion

```text
mu:X -> compactification of Y
```

which is an isomorphism over `V`, the full fibre `mu^{-1}(p)` is disjoint from `V`; every complete exceptional component over `p` is therefore a boundary component of `X\V`. If the exceptional fibre contains a positive-genus component, the boundary violates the theorem. If its strict-SNC dual multigraph contains a cycle, including a cycle made from parallel edges, the boundary violates the theorem.

This obstruction persists under further common resolutions. Blowups subdivide edges or attach tree pieces; they do not remove the genus of a strict transform and do not reduce the first Betti number of an already embedded subgraph. Adding the rest of the boundary can only keep or increase graph cycle rank. Thus a complete exceptional fibre over a missed singular point is boundary on every relevant common resolution, and graph-cycle persistence is sound.

## 5. Downstream Disposition

**Correction packet.** `bd-a2-rational-forest-morphic-correction-sol56-20260830.md` is confirmed in substance. Its counterexample, morphic theorem, actual-first-leg interface, and scope repair are correct. The maximum safe wording should keep saying "everywhere-defined dominant morphism" and should not state any rational-map boundary theorem.

**Old hostile review.** `bd-a2-rational-forest-multisection-hostile-review-opus5-20260830.md` is refuted exactly where it upgrades the gate to dominant rational maps (`107`-`111`, `344`-`350`, and repair item `382`-`383`). Its residue formula, disconnected-boundary treatment, multisection edge counting, and pure combinatorial checks are not damaged.

**Old coordinator integration.** `bd-a2-rational-forest-coordinator-integration-sol56-20260830.md` is refuted in Section 1 where it makes rational domination load-bearing (`59`-`72`). Replace that section with the morphic theorem above. Section 2's exact multisection formula remains a mathematical formula. Section 3's `d>=3` projective `p_g>0` exclusion remains valid even against rational maps, because a rational map to a dense open of a smooth projective target gives a dominant rational map to the proper target and ordinary form pullback still forces `p_g=q=0`. The generic `d=2` infinity-genus exclusion is only a morphic first-leg exclusion, not a rational-domination exclusion.

**Producer.** `bd-a2-firstleg-rational-forest-multisection-producer-sol56-20260830.md` used a dominant morphism in its theorem (`86`-`95`), so its core gate survives after spelling out the boundary-over-infinity resolution. Its pure residue and multisection content survives. Any sentence later read as "dominant rational first leg" must be read as morphic unless the argument is purely projective `p_g>0`.

**Bidegree-(2,3) classification.** `bd-a2-bidegree23-rational-forest-classification-coordinator-integration-sol56-20260830.md` remains valid as a classification of reduced squarefree `(2,3)` infinity divisors with rational-forest resolution. Its campaign consequence at `147`-`150` must be retagged: the necessary condition `F1`-`F7` applies to an everywhere-defined dominant morphic `A^2` first leg landing in the corresponding open, not to arbitrary dominant rational maps.

**Block-structure integration.** `block-descent-structure-coordinator-integration-sol56-20260830.md` is not damaged by this correction. It supplies the actual morphic/etale first leg and the open smooth image `V`, which is the correct input for the theorem.

**Rational domination only.** Any open-surface boundary conclusion relying only on a dominant rational map from `A^2` is retracted or reopened as `OPEN`, unless it has an independent proof. The independent projective statement remains: for a smooth projective surface rationally dominated by `P^2` or by a dense open of `A^2`, ordinary `p_g=q=0` follows. What fails is the passage from rational domination to vanishing log plurigenera of a chosen complement.

## 6. Maximum-Safe Replacement

The replacement theorem to promote is exactly:

> Let `U` be a smooth quasi-projective complex surface. If there is an everywhere-defined dominant morphism `A^2 -> U`, then for every smooth projective strict-SNC completion `U=X\D`, one has `p_g(X)=q(X)=0`, `barP_m(U)=0` for all `m>=1`, and
>
> ```text
> barP_1(U)=p_g(X)+sum_i g(D_i)+b1(Gamma_D)-rank(partial),
> rank(partial)<=q(X).
> ```
>
> Hence every boundary component is rational and the dual multigraph, with parallel edges retained, is a forest.

Dependencies:

```text
field: C, characteristic 0
target: smooth quasi-projective surface U
map: everywhere-defined dominant morphism from A^2
completion: smooth projective strict-SNC X\D
proof inputs: resolution of P^2 dashrightarrow X with centers over L_infinity;
              logarithmic pullback;
              ordinary differential-form pullback;
              vanishing of log plurigenera of A^2;
              residue/normalization/duality for disconnected strict-SNC D
not required: surjectivity, etaleness, global quasi-finiteness
```

Typed disposition:

```text
CONFIRMED: morphic rational-forest theorem and actual proper-block use via V=g1(A^2).
CONFIRM_WITH_CORRECTIONS: shrinking language; it is numerical monotonicity, not image control.
REFUTED: arbitrary dominant rational-map rational-forest theorem.
REWORD: all "dominant rational A^2 first leg" boundary uses to "everywhere-defined dominant morphic first leg".
REOPEN: any open-boundary exclusion whose only input is rational domination.
RETAIN: projective p_g=q=0 consequences from rational domination of the projective target.
```

No block occurrence, polynomial map, exit price, counterexample to JC2, or JC2 conclusion is established here.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14308`.
- Body SHA-256:
  `4031939eab4b9533d3afccedbb15df468055b087d8e7ce09f18e6b361f511c44`.
- Frozen basis: `effb538eb858ff2c51d713a91f392d90796e786e`.
