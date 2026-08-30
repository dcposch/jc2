# Coordinator integration: corrected rank-four branch-cycle theorem

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `6ed236c23e2fce71d1a279ca541239a405a757bf`  
Lifecycle: **REVIEW-INTEGRATED PROVISIONAL THEOREM**

## 0. Verdict

The Opus 5 hostile review confirms the rank-four fibre census, constructible
Euler ledger, connected acyclic-branch obstruction, Cohen--Macaulay
specialization inequality, and normalized cubic-resolvent construction.  Its
corrections strengthen the usable theorem:

> For every actual rank-four proper block, the reduced target branch `B` has
> `b1(B)>=1`; hence there is at least one `(2,2)` fibre.  After binding Chau's
> published polynomial-parametrization theorem as done below, the full
> monodromy is `S4`, and
>
> ```text
> n22 >= h-k+1,                 m >= 2h-1.              (0.1)
> ```
>
> Here `h=b0(R_red)`, `k=b0(B)`, `n22` counts `(2,2)` fibres, and `m` is the
> number of irreducible components of `B`.

The former disconnected acyclic horn is empty.  At a totally supported `(4)`
fibre the local decomposition group is `A4` or `S4`, never `D4`.  Accordingly
the normalized cubic resolvent has corrected special-fibre table

```text
quartic fibre  (2,1,1)  (2,2)  (3,1)  (4)
resolvent      (2,1)    (2,1)  (3)    (3).             (0.2)
```

This integration repairs the producer's uncharged Chau dependency and deletes
the over-generous `D4` resolvent row.  It does not exclude the surviving cyclic
`S4` horn, prove that a proper block occurs, treat the primitive/no-proper-block
case, or prove JC2.

## 1. Charged packet

```text
768cf08fe2be7a72e9e17cd15acd56976b6743cefa293bf11472a4fb4e701805
  xmodel/block-descent-a1-quartic-branch-topology-acyclic-obstruction-sol56-20260830.md
4b5d046fc9618f59e1608babd72615cb178dd6bcf7ad0d2c770632ada3a1e317
  xmodel/block-descent-a1-quartic-branch-topology-acyclic-obstruction-hostile-review-opus5-20260830.md
8b457a752434ac0c7cb6a2a83dd680b4a66dbe3631ab761c43dc789965ff2d2d
  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-sol56-20260830.md
e544a654d3cead096658502f34b0e6e5560b4a0ea8bf97a53b2a76081aceda4d
  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-hostile-review-gpt55-20260830.md
cf157e17db8179b590f15808aab84447717df343735416578e005a2085d73d4e
  xmodel/block-descent-a1-quartic-minimal-cycle-nodal-control-threat-map-sol56-20260830.md
ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778
  xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md
94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d
  xmodel/bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29
  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8
  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
41245c20b1b61a0dcf8116340672d037b977e6759d5d99054fc06c292d5c36fc
  refs/arzhantsev_zaidenberg_acyclic_curves_arxiv1110.3028v2.pdf
```

The fourth charged file independently checked the Chau primary source and the
normalization transfer.  The exact source is Nguyen Van Chau, *Note on the
Jacobian condition and the non-proper value set*, Ann. Polon. Math. 84 (2004),
203--210, DOI `10.4064/ap84-3-2`, Theorem 1 and Corollary 2; the official IMPAN
PDF and arXiv `math/0305088` contain the same statements.

## 2. Repair of the polynomial-parametrization dependency

Let

```text
A2 --g1--> Y --pi=g2--> A2,        deg(pi)=4,
R=NonEt_Y(pi)_red,                 B=pi(R)_red,
U=Y-R.
```

The block structure theorem gives `B subset A_F`, where `A_F` is the
nonproper-value curve of the original Keller map.  Since `pi` is finite, the
image of every irreducible component of `R` is a closed irreducible curve.
Thus every irreducible component `B_i` of `B` is contained in an irreducible
component of `A_F` of the same dimension and is equal to it.

Chau Theorem 1 gives a nonconstant polynomial parametrization
`A1 -> B_i`.  It lifts to the normalization and extends to a nonconstant map
from `P1` to the smooth projective normalization.  Luroth gives genus zero.
All finite points of the source map into the affine curve, so every puncture
of the affine normalization lies under the single point at infinity of the
source `P1`; surjectivity allows at most one puncture and affineness requires
one.  Therefore

```text
normalization(B_i) = A1.                                  (2.1)
```

The generic branch partition is `(2,1,1)` or `(3,1)`, with one ramification
point.  The corresponding component of `R` is birational to `B_i`, so its
normalization is also `A1`.  This supplies the one-place input that the
quartic producer used without charging.  No assertion that `B=A_F`, or that
the whole reducible curve has one analytic branch at infinity, is made.

## 3. Correct source-forest and quotient-graph statement

The morphic forest theorem concerns a resolved strict-SNC boundary.  On the
affine ramification curve it permits several components to meet at one point:
after blowing up, the configuration may be a star.  It permits unibranch
cusps as well.  What it forbids is a cycle in the component/singular-point
incidence graph, including a self-node or two distinct intersections between
the same components.

With (2.1), each connected component of `R` is consequently a tree of
contractible pieces and is contractible.  Put `h=b0(R)`.  The finite map
`R->B` is point-bijective except that a `(2,2)` fibre identifies one pair of
distinct source points.  Hence `B` is homotopy equivalent to the graph formed
from `h` vertices by adding `n22` edges.  If `k=b0(B)`, then

```text
e(B)=h-n22,
beta=b1(B)=n22-h+k.                                    (3.1)
```

This graph is the quotient graph, not the naive pairwise-intersection graph
of unrevolved affine components.

## 4. Every rank-four survivor has a branch cycle

The producer proves that a connected simply connected `B` forces
`e_c(U)<=0`, contradicting the promoted ruling identity

```text
e_c(U)=e(C)+Q >= 1,       C in {A1,P1}, Q>=0.           (4.1)
```

The review closes the disconnected case.  If every connected component of
`B` is simply connected and `B` is disconnected, Arzhantsev--Zaidenberg
Corollary 1.2 makes it a union of `r>=2` parallel lines.  On each line the
producer's Cohen--Macaulay specialization inequality gives at most two
unramified sheets at every point.  Therefore

```text
e_c(U) <= 4(1-r)+2r = 4-2r <= 0,                       (4.2)
```

again contradicting (4.1).  Thus some connected component of `B` has a cycle:

```text
beta=b1(B)>=1.                                         (4.3)
```

By (3.1), `n22>=h-k+1>=1`.  In particular every proper rank-four block has a
`(2,2)` conductor fibre; the disconnected acyclic successor proposed in the
producer must not be launched.

## 5. Monodromy and local-group corrections

Divisorial inertia is a transposition or a three-cycle.  Meridians normally
generate the global monodromy, excluding the regular `C4,V4` actions and
`D4`, whose transpositions generate only an intransitive order-four subgroup.
If the group were `A4`, all divisorial inertia would be a three-cycle.  A
`(2,2)` local group preserves two pairs and meets `A4` in a group containing
no three-cycle, so `n22=0`.  Then (3.1) makes every branch component
contractible.  The `h=1` row falls to Section 4; for `h>=2`, the exact Euler
ledger gives `e(U)=4-3h-n4<1`.  Hence

```text
G=S4.                                                   (5.1)
```

At any closed branch point the plane-curve local complement group is generated
by its branch meridians, not merely normally generated by them.  Therefore a
local decomposition group at a `(4)` fibre must be generated by its own
transpositions and three-cycles.  `D4` fails this test, so only `A4` or `S4`
can occur.  Passing through `S4->S3` on the three pairings yields (0.2).  The
formerly listed `(4),D4 -> (2,1)` row is empty.

The normalized resolvent is still not a proper cubic block: its field need
not embed in `C(x,y)`, and no etale first leg `A2->Z` is supplied.  Thus the
promoted cubic block theorem cannot be applied to it.  The cover-side cubic
acyclic lemma is also unavailable because (4.3) forces cyclic branch.

## 6. A global component lower bound

Let `B_1,...,B_m` be the irreducible components.  Their generic numbers of
unramified sheets are `u_j=2` or `1`.  For a finite set `Sigma` containing all
singular and exceptional branch points, normalization additivity gives

```text
e_c(U)=4-4e(B)+sum_j u_j
       +sum_(z in Sigma)(u(z)-sum_(branches j at z)u_j). (6.1)
```

The local orbit/specialization argument makes every bracket nonpositive.  At
each `(2,2)` point at least two transposition-generic branches occur, so its
bracket is at most `-4`.  Using `sum_j u_j<=2m`, (3.1), and (4.1),

```text
1 <= e(U) <= 4-4(h-n22)+2m-4n22 = 4-4h+2m.
```

Thus `2m>=4h-3`, equivalently

```text
m>=2h-1.                                               (6.2)
```

This is vacuous at the minimal `h=1` row but constrains every multi-component
source survivor.

## 7. Exact remaining frontier

The first surviving row is

```text
h=k=1, beta=n22=1, n4=0.                               (7.1)
```

The separate threat-map packet shows that only three arithmetic subrows remain:
no finite `(3,1)` values with `(C,Q)=(A1,1)` or `(P1,0)`, and one finite
`(3,1)` value with `(C,Q)=(A1,0)`.  Two active attacks split these into the
infinity-transport and unique-cusp/companion-divisor horns.  The named nodal
cubic is only a topology/control example: its complement has cyclic fundamental
group and cannot itself realize the two disjoint node transpositions, but that
does not classify all one-place `b1=1` curves.

## 8. Replay and firewalls

The producer replay verifies the bounded graph/Euler and finite `S4` subgroup
calculations, but does not encode the corrected resolvent table or Chau's
theorem.  Its literal field `acyclic_positive_euler_survives` has no independent
evidentiary force.  This integration relies on the sealed hostile review and
the separately sealed Chau source audit for those facts.

No claim here constructs or excludes every rank-four cover, excludes a
primitive counterexample, proves the existence of a proper block, or resolves
JC2.  The maximum promoted conclusion is the corrected cyclic-`S4` theorem
above.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10493`.
- Body SHA-256:
  `82ca4333f8bdcf3a6474c8e3f0dfe23dcbc1ad4bf767179bb78e44a91ddffac6`.
- Frozen basis: `6ed236c23e2fce71d1a279ca541239a405a757bf`.
