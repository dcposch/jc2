# Hostile FIRST: literal coordinate fibers of normalized weighted lifts

Reviewer: swarmHQ Sol (gpt-5.6-sol), different-model from producer ROOT (gpt-6-astra). Date: September 16, 2026 UTC. Review basis: `1f54811bf8f97241643e69a62a0cbc1efb6c5e4b`. Evidence: MANUAL algebra and surface geometry with the named accepted MORPHIC rational-forest theorem and standard smooth surface completion/factorization. Lifecycle: completed independent FIRST; ledger promotion remains with the coordinator.

## Frozen input and verdict

The authoritative [replacement producer](weighted-lift-coordinate-fibers-swarmHQ-root-20260916T133700Z.md) at commit `60b8dd6b32b20b3c3355d3f966cc5de233060d3a` has full SHA256 `eb7bb701c28f3b22683a454375098ea688e2ac210d56f8bb5f3a6921c2170041`, adjacent manifest SHA256 `8ef0bf6dd18a95ae2ee2437da58ac9db15e308a4869bfd1e4ca64f4d524b9359`, and body SHA256 `693985866276ab870f65ffbe76e3adf7d58929174f162d39218a723f4b85ff0d`. Both files were mode 0444. The [original producer](weighted-lift-coordinate-fibers-swarmHQ-root-20260916T133200Z.md) remains sealed with full SHA256 `cb418ea1d5981a7281fc95bdc2951930b9aa7afda94a697cd3c29dd26225c35d` and manifest SHA256 `adecc0ec003523d78bb6e5dc7ea12ae42f19ecd3eef0669d43920a8a3b81f7a3`. An exact unified diff shows only the mathematical/publication-basis split, the previously omitted EMPTY collision block and its provenance note, and corresponding seal metadata; every mathematical assertion and proof byte is unchanged. Artifact verification of the original returned VERIFIED before review, and the replacement is independently verified before sealing this report. The all-seed, all-literal-coordinate-level claim is **CONFIRMED** at its stated scope. This is an exclusion of a specific fiber mechanism, not a general descent theorem or a JC2 result.

## Polynomiality and the surviving plane — CONFIRMED

From `q'=w p'`, `p(0)=q(0)=0`, integration gives `q=wp-integral_0^w p`. The integral condition makes `q(1)=-1`; `q'(1)=k`. A linear seed would be `p=-w` and violate the integral condition, hence degree `n>=2`. Then `r=p/w` and `s=q/w^2` are polynomials of degree `n-1>=1`. At `w=1`, `r=s=-1`, `r'=k+1`, `s'=k+2`.

For `u=1+xy`, `gamma=1+a xy+x^2z`, `w=u gamma`, the coefficient of `xy` in `beta=1+u r(w)` is `k+a(k+1)=-1/(k+2)` and its constant term vanishes. The coefficient of `xy` in `alpha=u+u^2s(w)` is `(k+1)+a(k+2)=0`; its constant term vanishes, and the `x^2z` coefficient is `k+2`. Thus `x|beta`, `x^2|alpha` in `C[x,y,z]`, so all outputs in (1) are whole-source polynomials. Their restrictions to `x=0` are `B=-y/(k+2)` and `A=eta y^2+(k+2)z` for some seed-dependent scalar `eta`. The inverse displayed by the producer follows directly, so the remaining pair is a triangular automorphism with Jacobian 1. The dense-open determinant check is consistent: `det d(P,Q)/d(w,gamma)=-gamma`, `det d(C,P,Q)/d(x,u,gamma)=-gamma^3`, `det d(C,P,Q)/d(A,B,C)=-C^3`, and `det d(x,u,gamma)/d(x,y,z)=x^3`; hence `JF=1` as a polynomial identity. This does not make a two-dimensional coordinate fiber a Keller counterexample.

## A, B=0 and C fibers — CONFIRMED

The factorization `A=uD`, `x^2D=1+u s(w)` is polynomial because `u` and `x` are coprime. At `A=c!=0`, `u` is a unit; at `A=0`, each surface component lies in `u=0` (where `x` is a nonconstant unit) or `D=0` (where `u s=-1`, so `u` is a unit). The unit cannot be a constant on a surface component: `u=u0!=1` gives irreducible `xy=u0-1` and nonconstant gamma-dependence through nonconstant `s`; `u=1` has surface pieces `x=0` and `y=0`, and (2) or the nonconstant `s(1+x^2z)` excludes constant A on either. The `u=0` surface is `Gm x A1` and `x` varies. A dominant morphism from A2 cannot land in any such component because its ring pullback sends every unit to a constant.

For `B=0`, `xB=1+u r(u gamma)=0`, so `u` is globally a unit. It is nonconstant on the dense open `Gm_x x H`, where `H` is identified with `Spec C[w,1/r(w)]` by `u=-1/r(w)`, `gamma=-w r(w)`. Since `r` is nonconstant, this excludes A2 domination. The open is smooth irreducible, while `x=0` contributes only a line and `B_y=-1/(k+2)` there; hence no hidden surface component or singular point changes the conclusion.

For `C=c!=0`, `x` is a nonconstant unit on `Gm_x x A1_u`. For `C=0`, the two components are `x=0` and `gamma=0`; on the latter `x(a y+xz)=-1`, so `x` is a nonconstant unit. Exactly the former is an A2 plane and is dominated by A2.

## Nonzero B levels and the boundary cycle — CONFIRMED with exact import

For `b!=0`, the inverse `x=h(u,gamma)/b`, `y=(u-1)/x`, `z=(gamma-1-a(u-1))/x^2` identifies `S_b minus V(x)` with `A2_(u,gamma) minus H`. The `x=0` line maps to `(1,1) in H`; it has codimension one in the irreducible hypersurface, not a second surface component. `B_y=-1/(k+2)` along it, so `S_b` is smooth. The morphism `pi=(u,gamma):S_b->A2` is birational and regular on all of `S_b`; no rational first leg is being mistaken for a morphism.

The smooth curve `H` has function field `C(w)` and missing places `w=infinity` plus the distinct roots of nonconstant `r`, hence `e>=2`. In a smooth projective completion of `S_b` extending `pi` to a proper birational `f:X->P2`, strict-SNC boundary resolution can be performed outside the already smooth open `S_b`. The reduced preimage `T` of the target infinity line lies wholly in the boundary and is a connected rational tree: point blowups over the line add a leaf or subdivide an edge. The strict transform of the projective closure of `H` is another rational boundary component. Each of its `e` distinct normalized infinity places meets `T`; strict-SNC resolution separates any coincident plane limits, and the distinct points yield `e` boundary edges. Thus `T` plus this component contains a cycle (`b1=e-1>=1`) even if further boundary components exist. This contradicts the accepted [MORPHIC rational-forest theorem](bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md), SHA256 `94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d`, for an everywhere-defined dominant `A2->S_b`. Its morphic hypothesis is indispensable; the punctured-plane inverse (4) does not qualify.

## Composition and exclusions

If polynomial `j:A2->A3` has two-dimensional image and one literal output coordinate is constant, the closure of its irreducible image is a surface component of that fiber and `j` dominates it. The preceding cases force `C=0` and image in `x=0`. The remaining outputs are the triangular automorphism `G` composed with `(j_y,j_z)`, so the chain rule and composition give exactly the producer's Keller/invertibility equivalences. Arbitrary initial `j` can already contain the full JC2 problem; no new plane counterexample is created by this coordinate-fiber step. This does **not** cover non-coordinate target surfaces or output projections, target changes, rational first legs with poles, or arbitrary weighted-lift constructions. I found no GAP within the stated claim and do not infer a successor family.

Desk-only hostile review; no network, CAS, scientific script, worker or new theorem import. No exit-price assertion.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7294`.
- Body SHA-256:
  `d7bc7241f41e4f32f56d6af7361cb452f5a8b176254c2cc05f30a9c6ef402144`.
- Frozen basis: `1f54811bf8f97241643e69a62a0cbc1efb6c5e4b`.
