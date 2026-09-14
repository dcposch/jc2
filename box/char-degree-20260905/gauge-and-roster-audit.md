# Supplementary gauge and family-C audit

No existing ledger is edited. This appendix supplies the missing group
action behind the already used beta=1 slice and audits the supplementary
roster count independently of its prose report.

## The beta normalization is a source dilation, not a conjugate choice

The statement “choose the D1 conjugate pi=1” cannot by itself turn an
arbitrary nonzero orbit parameter beta into 1. A choice among roots of
`pi^L=beta` changes the selected root, not beta. The required action is
the remaining simultaneous source dilation, compensated by target
scales. For `alpha in k^*`, define

\[
F_\alpha(x,y)=\alpha^{-n}F(\alpha x,\alpha y),\qquad
G_\alpha(x,y)=\alpha^{-m}G(\alpha x,\alpha y).
\]

For every canonical degree-d auxiliary root the induced action is
`h_alpha=alpha^(-d)h(alpha*x,alpha*y)`. Monic division commutes with
this action. In normalized coordinates,

\[
K_{h_\alpha}(t,z)=K_h(t/\alpha,z),\qquad
c_{r,q}\longmapsto\alpha^{-r}c_{r,q}.
\]

The two placed directions y=0 and y=x are invariant under this
simultaneous dilation. The leading homogeneous forms and F/G monicity
are restored exactly by the displayed compensating scales. This is
the residual group action preserving those earlier gauge choices;
it is not a second independent use of the target-monicity parameters.
The zero major ordinary center stays zero. Minor jet0 remains a free
coordinate, transforming as `jet0 -> alpha^(-1)*jet0`.

For (99,66), the h2 D2 face has sites
`(r,q)=(4j,24-3j)` and coefficients from `(pi^3-beta)^8`.
Their scaling is `alpha^(-4j)`, so

\[
\beta\longmapsto\beta\alpha^{-4}.
\]

For D108, the sites are `(5j,28-4j)` in `(pi^4-beta)^7`, giving

\[
\beta\longmapsto\beta\alpha^{-5}.
\]

Because beta is nonzero and the geometric coefficient field is
algebraically closed, choose alpha with `alpha^4=beta` or
`alpha^5=beta`. This uses the residual dilation **once** and produces
the beta=1 slice. Only after that normalization does choosing one
conjugate legitimately put the selected D1 root at pi=1. There is
finite residual root-of-unity symmetry; no unique rational product
decomposition of the slice is claimed.

The frozen D108 gauge description is therefore incomplete at that
line, but its beta=1 chart has a valid orbit-coverage justification.
No other recorded action uses this residual simultaneous dilation:
placing directions used their relative slope/scale, while canonical
auxiliary monicity follows internally. Minor separation c and the
characteristic leader remain free; assigning them values in isolated
point controls is not a chart-wide normalization.

## The characteristic leader must transform and remain free

Let `L=2n=3m` be the ambient weight of
`Q=G^3-F^2+aG^2+bFG+cF+dG+e0`. The target coefficient transformation
which gives `Q_alpha=alpha^(-L)Q(alpha*x,alpha*y)` is

\[
a\mapsto a\alpha^{-m},\quad b\mapsto b\alpha^{-(n-m)},\quad
c\mapsto c\alpha^{-n},\quad d\mapsto d\alpha^{-2m},\quad
e_0\mapsto e_0\alpha^{-L}.
\]

Consequently a degree-D characteristic leader transforms as
`lambda -> alpha^(D-L)*lambda`, namely

\[
\lambda_{55}\mapsto\alpha^{-143}\lambda_{55},\qquad
\lambda_{63}\mapsto\alpha^{-153}\lambda_{63}.
\]

It is kept nonzero by its own Rabinowitsch equation; it is never
simultaneously set to 1. Its inverse coordinate scales oppositely.
Likewise `Jc -> alpha^(2-n-m)*Jc`; beta normalization does not also
normalize the Jacobian scalar. All homogeneous target-subtraction
rows are covariant under the displayed action. Thus the repaired
gauge accounting supports the augmented chart without spending any
new parameter on the characteristic face.

## The supplementary roster contains 36 leaves, not 38

The roster is supplementary evidence, distinct from the seven charged
inputs. The independent check mechanically extracted its digest from
the `_basename=roster.jsonl` and paired `_sha256` fields of
`family-c/residual65.supplementary.run.v2` with awk, then ran
`sha256sum -c` on the copied roster. Result: OK, hash
`c1c3b86fa7a19c0ff059aaac8da6fd5b1809911603c34cbe0414c7148efe2e8b`.
The generated manifest is `gauge-roster.sha256`.

Filtering actual roster records by `source.u_s>=2` yields **20
parents**. Summing their `split_window.leaf_count` yields **36**;
every recorded count equals the length of that parent's `leaves`
array. Thus the count discrepancy with the supplementary report's
38 is exactly two. This audit identifies a prose/count discrepancy;
it does not invent missing records or silently relabel them.

`gauge-roster-controls.json` also independently recomputes the
characteristic degrees from each parent's M sequence and checks
the existing `family-c/instrument-manifest.json`. All 20 parents
have `M_s=n-2`; every child is marked prefix-only. Their recursive
attainment defects range from **7 to 320**, agreeing with the
manifest and giving no uniform small-depth bound.

The uniform characteristic necessity belongs to a **realized parent
coefficient pair**. To apply it to one of these typed ES leaves,
one must build and audit that leaf's parent coefficient lift and
transport every row through the actual coordinate map. The roster's
incomplete child prefix does not acquire a Keller hypothesis or an
attained terminal characteristic degree merely from its labels.
Neither 36 nor the older prose count 38 is a count of proved kills.

No exit price is asserted, and no charge-basis line applies.
