# Coordinator integration: canonical normalization excludes generic degree three

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `497bb97c5fde00b12dd40942e058303d24012346`  
Lifecycle: **PROMOTED THEOREM / DIFFERENT-MODEL CONFIRMED**

## 0. Promoted endpoint

> **Theorem.**  If `F=(F,G):A2_C -> A2_C` is a polynomial Keller map, then
>
> ```text
> [C(x,y):C(F,G)] != 3.                                 (0.1)
> ```

GPT-5.5 independently reconstructed and confirmed the proof.  Its only
correction is a scope repair: the old ruling and forest integrations were
stated for a strict intermediate block, whereas the canonical normalization
has first-leg degree one.  Their proofs, not their strict-block labels, apply
at this endpoint because the required input is the actual dominant open
immersion `A2->U`.  Sections 3--4 below bind that recheck explicitly.

This is a theorem about generic function-field/geometric degree.  It says
nothing about either coordinate degree or total polynomial degree and does not
resolve JC2.

## 1. Charged packet and custody

```text
28f29711366f58f4a1c9e6e5d7f16d8e6ca29fddf730bfd436100da04e4d2eda
  xmodel/block-descent-all-degree-acyclic-companion-obstruction-sol56-20260830.md
3d0b72c7001bf403fa334f746dd09a21d8a55fc8074f9b4680e249b92f73beb3
  xmodel/block-descent-all-degree-acyclic-companion-obstruction-sol56-20260830.md.artifact.json
8ccb92fd3676e9f8b58e3ace4eb9157d0fa290ea24abc84d9913e94ec407e16d
  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-coordinator-integration-sol56-20260830.md
c229cbc4eb93722eb9d5c247c5e0616901a0e5cfce0278613cffc7f9e4fcbe85
  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-coordinator-integration-sol56-20260830.md
b3bdd87cb27b614ca4bac476fd7f4c676b9551026397f3a895dbf84f4f195419
  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-coordinator-addendum-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d
  xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
41245c20b1b61a0dcf8116340672d037b977e6759d5d99054fc06c292d5c36fc
  refs/arzhantsev_zaidenberg_acyclic_curves_arxiv1110.3028v2.pdf
b1f75e63c074e264946fcf8c58f1bdbb60088b5f75a748b76c32da8c627d6e82
  xmodel/block-descent-canonical-normalization-degree3-hostile-review-gpt55-20260830.md
997abd2707f082eb1f74ad9eb73a6a1c5b855443c0fc450043e047dd26fdebc8
  xmodel/block-descent-canonical-normalization-degree3-hostile-review-gpt55-20260830.run.v2
```

The external receipt records raw review-body hash
`93a88664971b36c08a699286a8c1db9adda091681724a71d2e8c7c3b1a6aa094`,
matching the sealed report's body hash.  Prompt, composed prompt, adapter,
launcher, sandbox profile, charge validator, fallacy appendix, report and log
hashes were reproduced before the report was read.  The lane exited zero with
`charge_basis_status=ABSENT`, as expected because it asserts no exit price.

## 2. Canonical finite-flat normalization

Put

```text
A=C[F,G],       K=Frac(A),       L=C(x,y),
S=integral closure of A in L,    Y=Spec(S).
```

The Keller condition makes `F,G` algebraically independent and `L/K` finite
separable.  Since `A` is excellent, `S` is finite over `A`.  Every `s in S` is
integral over `A` and hence over `C[x,y]`; normality of `C[x,y]` in `L` gives
`S subset C[x,y]`.  Thus there is a factorization

```text
j:A2 -> Y,          pi:Y -> A2,          F=pi o j.      (2.1)
```

The map `j` is affine-separated, finite type, birational and quasi-finite: its
fibres lie in fibres of the etale, hence quasi-finite, Keller map.  Zariski
Main makes `j` an open immersion.  The normal surface `Y` is Cohen--Macaulay;
finite miracle flatness over the regular target makes `pi` finite flat of rank
`[L:K]`.

Let `R=NonEt_Y(pi)_red`, `U=Y-R`, and `B=pi(R)_red`.  The open chart `j(A2)`
avoids `R`.  If `R` were empty and the rank exceeded one, `Y->A2_C` would be a
nontrivial connected finite etale cover, impossible.  Purity then makes `R`
nonempty and divisorial.

## 3. Generic companion sheets

For every irreducible component `D=V(p_D)` of `B`, the polynomial
`p_D(F,G)` is nonzero and nonconstant.  Some component of its zero curve
dominates `D`; all its points lie in `j(A2)`, disjoint from `R`.  Hence the
generic fibre above `D` contains at least one unramified factor.  If its residue
degree is `f>1`, geometric inertia fixes `f` sheets; no false globally labelled
sheet is asserted.

This argument is deliberately generic.  It does not supply a rank-one
henselian factor at every singular or conductor value.  That pointwise upgrade
will be forced only after the degree-three Euler calculation.

## 4. Ruling and forest at first-leg degree one

The endpoint does not cite the old strict-block theorem label.  Instead its
hypotheses are rechecked directly:

- `U` is smooth affine because it is the maximal etale open of the finite map
  from normal affine `Y` to `A2`.
- `C(U)=C(x,y)`, so `U` is rational.
- Pullback along the dominant open immersion `j:A2->U` injects units into
  `C[x,y]^*=C^*`; hence `O(U)^*=C^*`.
- Log-Kodaira monotonicity along `j` gives `bar-kappa(U)=-infinity`.
- The Miyanishi--Sugie/global-extension mechanism supplies an `A1`-fibration
  `rho:U->C`, with `C=A1` or `P1`, reduced fibres unions of affine lines, and

  ```text
  e_c(U)=e_c(C)+Q,       Q=sum_t(q_t-1)>=0.             (4.1)
  ```
- The morphic rational-forest theorem needs only an everywhere-defined
  dominant morphism `A2->U`; `j` supplies exactly that.  Every strict-SNC
  completion boundary has rational components and forest dual multigraph.

No strict intermediate field, `d1>=2`, surjectivity of `j`, or etaleness of
`j` beyond its open-immersion property is used here.

## 5. Rank-three source-to-target topology

Assume for contradiction that `[L:K]=3`.  A non-etale point in a closed fibre
of `pi` consumes local fibre length at least two.  Since the total length is
three, every branch value has exactly one reduced non-etale source point.
Therefore

```text
R -> B
```

is finite point-bijective and is a homeomorphism on complex analytic spaces;
it need not be a scheme isomorphism.

Moreover `R` lies in the boundary `Y-j(A2)`.  Approaching it through the dense
source chart produces an escaping source sequence with convergent `F`-image,
so `B subset A(F)`.  The finite image of each irreducible `R` component is a
curve and therefore an entire irreducible component of the plane curve `A(F)`.
Chau's published theorem polynomially parametrizes each such component.  Its
normalization, and the normalization of the corresponding `R` component, is
`A1`.

Resolving affine multibranch points retains self-branches and parallel edges
in the component/singular-point incidence multigraph.  That graph is a minor
or subdivision of the completion-boundary forest and is therefore a forest.
Normalization additivity then gives

```text
e_c(B)=e_c(R)=b0(R)=b0(B)=h>=1.                        (5.1)
```

## 6. The unique Euler row

Let `S0=A2-pi(U)`.  Generic companion sheets make `S0` finite.  The only cubic
fibre rows are

```text
off B:  (1,1,1), u=3;      B-S0: (2,1), u=1;
S0:     (3),     u=0.
```

Constructible additivity and (5.1) give

```text
e_c(U)=3-2h-|S0|.                                      (6.1)
```

Combining (6.1) with (4.1), the `C=P1` equation
`2h+|S0|+Q=1` is impossible.  The `C=A1` equation has the unique solution

```text
C=A1,        h=1,        S0=empty,        Q=0.          (6.2)
```

Thus `B` is connected and its affine-line component incidence is a forest, so
`B` is topologically contractible.  Because `S0` is empty, every branch value
has a local length-one factor; finite-flat idempotent splitting over the
henselian base makes it a rank-one henselian companion.

## 7. Monodromy contradiction

Over `A2-B`, the degree-three cover is connected and finite etale, so its
monodromy is transitive.  Normality gives nonidentity generic inertia.  With a
fixed companion sheet, generic inertia is a transposition.

Arzhantsev--Zaidenberg classify every reduced connected simply connected plane
curve into the comb/line and weighted-cone families.  In the comb family the
spine meridian is central; its transposition centralizer preserves the fixed
sheet and is intransitive.  In the weighted-cone family the origin henselian
companion splits analytically, and a weighted sublevel inside its ordinary
splitting ball retracts radially onto the global complement.  The global image
therefore lies in a point stabilizer and is again intransitive.  Both contradict
connected-cover transitivity, proving (0.1).

## 8. Replay, corroboration and firewalls

The all-degree replay passes identically under ordinary, `-O` and `-OO`, with
stdout hash `71499353da07d047ec0d222454649779769e331db013845a5af3370fe7ebd35b`
and payload hash
`3586519ac48ca485bf4c91e8d32a5a89b3ebf3f77329b2e925abefd2e805f492`.
The `--mutate-drop-centrality` mutation is rejected.  It verifies finite
permutation arithmetic only; none of Sections 2--6 is software-certified.

Orevkov's classical three-sheeted theorem is external corroboration, not a
dependency of this proof.  This integration does not promote claims about
coordinate degrees, strict-block occurrence, generic degree four or higher,
primitive monodromy, or JC2.  The next canonical frontier is to combine the
open immersion, constant-unit `A1` ruling and one-place nonproperness
components to exclude the branch cycle now forced in every higher-degree
hypothetical counterexample.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9953`.
- Body SHA-256:
  `b8a6e40e2df7216b8d857d0f450270b2aef7414ce686b936e0950ff5b8c59032`.
- Frozen basis: `497bb97c5fde00b12dd40942e058303d24012346`.
