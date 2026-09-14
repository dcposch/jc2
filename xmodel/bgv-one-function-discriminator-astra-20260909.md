# BGV one-function discriminator: persistent collision divisors

UNREVIEWED manual synthesis. First action22:42:06.530033935UTC; controlling stop23:00:06.530033935UTC, September9,2026. No new external proof review or campaign promotion.

## Result and decision

There is no established cheaper JC2 proof interface from generic primitive-element choice. There is a concrete useful restriction on that search: **a nonsaturated collision divisor cannot be repaired by any base-affine replacement of the chosen auxiliary polynomial**. This is proved below, together with a small example in which a generic linear combination of two good auxiliary functions creates exactly this obstruction. The example is finite étale between copies of G_m×A¹, NOT a Keller counterexample.

The cheapest remaining actual-source discriminator is therefore not primitive-element generation, a norm calculation, or a search through base-dependent translates. It is the saturation of individual divisors above the singular locus of ONE specified primitive graph. No such graph/divisor calculation for an actual F10 solution is supplied here. No speed advantage or new global ranking follows.

## 1. Exact primary interface

Work over an algebraically closed field K of characteristic zero. Let X=A², Y=A² and e=(P,Q):X→Y have nonzero constant Jacobian. Put R=K[P,Q] and S=K[x,y]. For π∈S primitive for Frac(S)/Frac(R), the map j=(π,e) is quasi-finite and birational onto its image closure Z. Primitive does not mean S=R[π].

BGV Definition22.2 additionally requires every irreducible divisor D of j⁻¹(Sing Z) to satisfy e⁻¹(e(D))=D, set-theoretically. Proposition27.5's proof then gives automorphy in characteristic zero. Its proof uses the condition “weak type≤1”; the definition's exact type1 excludes type0, while an automorphism has type0. Lemma22.5 supplies two auxiliary functions: its second function repairs finitely many divisorial approximations, giving a locally closed embedding outside codimension≥2. It does NOT supply a single generic combination preserving this property. [Exact primary source](https://arxiv.org/pdf/2609.05746v1), Definition22.2/Lemma22.5/Proposition27.5; frozen text ranges in READ-SCOPE.

To identify the algebra actually missing, let f(T,U,V) generate the prime kernel defining Z and let d=deg_T f. Characteristic zero gives f_T≠0 and deg_T f_T<d. Differentiating f(π,P,Q)=0 and using the invertible Jacobian shows, ON X,

    j⁻¹(Sing Z) = V(f_T(π,P,Q)).                         (1)

Saturation of each prime divisor in (1), not merely of their union, is the decisive condition. Its image closure has a prime equation h in R. Étaleness makes h(P,Q) generically reduced. Every prime component of its inverse image dominates that image divisor, so its image meets the dense image of D; saturation excludes every component other than D. Thus h(P,Q) is a defining equation of D up to a constant unit of S. Factoring (1) with multiplicities yields

    f_T(π,P,Q) ∈ R.                                     (2)

Then f divides f_T-b(U,V) for some b∈R. The latter has T-degree<d, hence is zero; characteristic zero forces d=1. This isolates BGV's load-bearing descent step. Normality of S alone does not imply (2), and taking the norm of f_T merely produces a base element automatically; it is not descent of f_T itself. This paragraph rederives the local source interface, not a new replacement for Proposition27.5.

## 2. Persistent-collision lemma

The following statement is independent of a hypothetical counterexample's existence. Let e:X→Y be a dominant quasi-finite morphism of smooth integral K-varieties of equal dimension, and let π be a regular function such that j=(π,e) is birational onto its image closure. Suppose an irreducible divisor D⊂X has a dense set of points x for which there is x'≠x with

    e(x')=e(x),  π(x')=π(x).                            (3)

If e⁻¹(e(D))≠D, then D obstructs the BGV divisor condition. Moreover, for EVERY regular a,b on Y with a≠0, the primitive function

    π'=a(e)π+b(e)                                      (4)

has the same obstruction D. This includes a which vanishes on e(D); no inversion of a on that divisor is used.

Proof. Equality (3) persists under (4). A quasi-finite birational morphism from a normal variety is an open immersion above the normal locus of its target: factor through normalization and apply the normal-target form of Zariski's Main Theorem. Consequently two distinct points with the same image cannot lie above a smooth point of the image closure. Thus the dense collision set is in j⁻¹(Sing Z), and its closure D is contained there. This closed set is proper because a birational morphism is an isomorphism on dense open subsets and the target is generically smooth. Hence D is an irreducible divisorial component, not merely a subvariety contained in a larger divisor.

The same reasoning applies to j'=(π',e). It remains birational because a is nonzero in K(Y), so π=(π'-b)/a in K(X); it remains quasi-finite since each of its fibers is contained in an e-fiber. The source divisor D and e⁻¹(e(D)) have not changed. Therefore D is still a forbidden component. QED.

The normal-target fact is stated explicitly; it is not a claim that Z itself is normal. No finite-flatness, properness or generic-degree bound is assumed in this lemma. It detects collision-type singular divisors only: absence of such a collision does NOT establish the BGV condition, since singularities can involve branches absent from the source or other nonnormal behavior.

For a∈K* the stronger elementary invariance holds for the entire singular pullback: (T,U,V)↦(aT+b(U,V),U,V) is an ambient automorphism. With compatible defining equations, f'_T(π',P,Q)=a^(d-1)f_T(π,P,Q). For nonconstant a only the collision-persistence assertion is used; an ambient polynomial inverse is not asserted.

## 3. A generic-projection countercontrol, with every dropped hypothesis

Take X=Spec K[x,x⁻¹,y], Y=Spec K[U,U⁻¹,y], e(x,y)=(x³,y), and choose a primitive cube root ζ. This is a finite étale degree3 morphism: x satisfies X³-U and 3x² is a unit on X. Both varieties are smooth and normal. For λ∈K set

    π_λ=x²+λx,  T=π_λ,
    f_λ(T,U)=T³-3λUT-U(U+λ³).                          (5)

Manual verification: the three conjugates have sum0, pair-product sum−3λU and product U(U+λ³), giving (5). Also

    x(T+λ²)=U+λT,

so π_λ is primitive for every λ; the denominator is not identically zero. The graph morphism is finite birational, and X is its normalization. These are stronger finiteness and smooth-source properties than mere generic birationality.

For every λ≠0 the three points over U=λ³ have x-values λ, λζ, λζ². The last two have T=−λ² and the first T=2λ². Thus the two distinct source divisors

    D₁={x=λζ}, D₂={x=λζ²}

collide. Direct differentiation gives

    f_T(π_λ,U)=3x²(x-λζ)(x-λζ²),
    e*(U-λ³)=(x-λ)(x-λζ)(x-λζ²).                     (6)

The singular point in the (T,U) curve is (−λ²,λ³): both derivatives in (5) vanish there; crossing with the y-line gives the singular divisor. Each e⁻¹(e(D_i)) contains all THREE displayed source lines, not D_i alone. The obstruction is exact, not inferred from a generic discriminant or from repeated roots without checking the source inverse image.

The pair of auxiliaries (x,x²), together with e, gives a closed embedding, since x and U⁻¹ recover x⁻¹=x²/U. Nevertheless a generic linear combination b x²+a x, with ab≠0, is a scalar multiple of π_(a/b) and fails the divisor condition. Thus “two functions work, so a generic combination works” fails even with a finite étale map and smooth normalization.

Changed-object controls: at λ=0, π=x² has no bad divisor on X, because f_T=3x⁴ is a unit; the same graph is a closed embedding, with x=U/T and T invertible. In (6), replacing a full inverse image by its selected branch D_i would falsely declare that divisor saturated; omitting only the third line instead falsely identifies the singular-pullback UNION with the entire fiber. Merely observing that the norm of f_T lies in the base cannot certify individual-divisor saturation. Finally, extending e to the whole affine plane gives Jacobian3x² with a zero divisor, not a Keller map. The example drops BOTH affine-plane source/target and the constant polynomial-Jacobian hypothesis; nonconstant units are available. It therefore does not refute Proposition27.5 or JC2, and it does not prove generic projections fail for every hypothetical affine-plane Keller map.

## 4. Faithful next interface and stop decision

For a SPECIFIED actual source and primitive π, examine the off-diagonal correspondence

    E=(X×_Y X)\Δ,  δπ=pr₁*π-pr₂*π.

A divisorial image D of a component of V_E(δπ), together with an actual point/valuation showing e⁻¹(e(D))≠D, is a certificate that this π AND its entire base-affine class (4) fail. This does not exclude another primitive element outside that class. Conversely, the absence of these collision witnesses is not an acceptance certificate: every component of (1), including those not detected on E, must satisfy the exact BGV condition.

This is a finite, precisely typed rejection interface, not a promised low-cost resultant or a registered computation. No actual source, primitive polynomial or source-divisor list was constructed. The campaign's finite cubic PARAMETER cover is not the normalization/function-field extension of a hypothetical Keller map. The frozen strategy's actual map-degree21 statement at r=1 concerns the latter; no degree3 monogenic shortcut follows.

Decision: **NO_NEW_JC2_PROOF_MECHANISM established.** Retain the persistent-collision lemma as an unreviewed search restriction and the explicit generic-projection countercontrol. No new source exclusion, properness/unit claim, literature-novelty claim, runtime forecast, theorem promotion or dependent task. A genuinely cheaper positive interface would have to prove the individual singular-divisor condition for one actual source class; this task has not done so.

## OPEN(S) RAISED

No new canonical OPEN ID. Exact remaining quantity: for one licensed actual source and one explicitly chosen primitive π, which prime divisors of f_T(π,P,Q) fail full e-saturation? Cheapest test is the manual/source-algebra correspondence test just specified; cost is unknown and no computation is authorized. It is not a replacement all-degree coverage theorem.

## Read scope, controls and custody

Exactly three scientific inputs plus one optional PDF provenance pin are in PINS.json; all matched before use and are rechecked at publication. WHOLE/selected ranges and the prior unchanged WHOLE reuse are in READ-SCOPE.md. All algebra above was manual, with the λ=0, missing-third-line and non-Keller extension controls explicitly stated. No mathematical subprocess, network, software execution, AWS/SSH/process inspection, agent, protected/corpus/peer or shared-ledger access. The new lemma and control remain UNREVIEWED pending separate first different-model review.

## COLLISIONS

status: EMPTY — own-only target and report check, no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11299`.
- Body SHA-256:
  `7ec892b41bcf56d9970dd35d71b47fd192c29a6aa425ac536c47d180a43978a1`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
