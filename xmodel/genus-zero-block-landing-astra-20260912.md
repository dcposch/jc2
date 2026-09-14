# Genus-zero finite block landings: normal surfaces included

MANUAL / PRODUCER-CHECKED / UNPROMOTED. First actual action2026-09-12 06:18:42UTC; owned targets absent. Original reserve06:36/HARD06:39UTC unchanged. No scientific execution, code, coefficient payload, worker, network or shared/protected edit. The scroll theorem and BD-GAL are accepted premises, not re-hardened. The new proof concerns their exact genus-zero interface only.

Claim: let C(f,g) be a proper subfield of K, itself a proper subfield of C(x,y), for a hypothetical complex plane Keller map. Let Phi:Ybar->P2 be the finite NORMAL projective normalization in K and L=Phi^*O(1). A general member of |L| cannot have genus0. Degrees are unbounded; this is a necessary condition on actual proper-block landings, not exclusion of all covers or all normal surfaces.

## 1. Source attachment and H1 without rational singularities

Use the accepted BD-GAL sandwich A2 --g1--> Y --g2--> A2, with g1 dominant etale quasi-finite, Y normal, and g2 finite. The restriction of Ybar over the chosen target affine chart is this SAME Y: normality, finiteness and function field K identify the normalization uniquely. No resolution is substituted for this finite model. Composing g1 with its inclusion gives a dominant rational map P2-->Ybar, regular on the source A2.

Only H1(Ybar,O)=0 is needed. Here is a direct source proof avoiding even a separate rationality classification. Resolve that rational map by point blowups Z->P2, obtaining a proper generically finite map Z->Ybar, with H1(Z,O)=0. Its Stein factorization is Z->W->Ybar, where W->Ybar is finite of generic degree n>0 and (Z->W)_*O_Z=O_W. Normality of Ybar makes field trace send O_W into O_Ybar: traces of integral elements are integral and lie in the normal base's fraction field. The normalized trace Tr/n splits O_Ybar->(W->Ybar)_*O_W in characteristic0. Hence

    H1(Ybar,O) injects into H1(W,O),
    H1(W,O) injects into H1(Z,O)=0.

The second injection is the low-degree Leray edge map, not an assertion that R1 vanishes. This proves the required vanishing from the actual source. Equally, once a rational resolution S->Ybar is known, normality gives rho_*O_S=O_Ybar and Leray injects H1(Ybar,O) into H1(S,O)=0. Neither route assumes rational singularities; the direct trace route is the one used here.

## 2. Genus zero forces a minimal-degree embedding

Put d=L^2=deg(Phi)>0. L is ample and globally generated. The singular locus of the normal surface is finite. A general C in |L| avoids it, since vanishing at any one of those points is a proper linear condition. Bertini gives smoothness on the smooth locus, and ample-divisor connectedness gives connectedness; thus C is a smooth connected projective curve. These facts do not require rational singularities or a smooth Ybar.

Assume the sectional genus is0, so C is P1. The effective Cartier sequence

    0 -> O_Ybar -> L -> L|C -> 0

and H1(O_Ybar)=0 imply h0(L)=1+h0(L|C)=d+2, since deg L|C=d. The COMPLETE series defines psi:Ybar->X subset P^(d+1). It is finite: a positive-dimensional projective fiber contains a curve, but every contracted curve has L-degree0, contradicting ampleness. Its reduced irreducible image X is nondegenerate. The primary minimal-degree inequality and the projection formula give

    deg X >= 1+codim X=d,
    d=L^2=deg(psi)*deg X.

Therefore deg(psi)=1 and deg X=d: X is a surface of minimal degree. This uses the complete series, not a claim that the original three-section net embeds Ybar.

## 3. Classification and the NORMALITY step

The charged primary Theorem0.1 classifies minimal-degree varieties as linear spaces, quadrics, rational normal scrolls, or cones over the Veronese surface. In dimension2 this list becomes P2, smooth quadrics, the Veronese surface itself, smooth rational normal surface scrolls S(a,b) with 1<=a<=b, and rational normal cones S(0,d). A positive-dimensional cone over a Veronese surface has dimension at least3 and is not a further surface case. Irreducible singular quadrics are the d=2 rational normal cone; reducible or double quadrics cannot be the reduced integral X.

Normality must not be inferred merely from the normal source of a finite birational map. It holds separately for every classified X. The plane, smooth quadric, Veronese P2 and smooth scrolls are smooth. For S(0,d), d>=2, the vertex chart is the d-th Veronese subring of C[u,v], equivalently the invariant ring under scalar mu_d. This is integrally closed: an element of its fraction field integral over the invariant ring is integral over C[u,v], hence in C[u,v], and is invariant. Away from the vertex the cone is smooth, being the corresponding line-bundle chart over the rational normal P1. Thus the cone is normal too.

Consequently finite birational psi onto normal X is an isomorphism. The classification applies to Ybar itself with its actual L, not merely to a birational resolution.

For S(a,b), a,b>0, the projective-bundle description gives Ybar=F_(b-a), L=E+b f and L.f=1. The smooth quadric is S(1,1)=F_0. The newly promoted scroll theorem applies to the ACTUAL finite Phi and the chosen target line ell. Its forbidden open is Ybar minus (supp Ram(Phi) union supp Phi^*ell). The actual g1 lands in that open: its target chart avoids Phi^*ell, and the Keller chain rule (or the accepted sandwich) avoids ramification. It is a dominant everywhere-defined A2 first leg. Contradiction, for every degree of that leg and without any generic-net assumption.

## 4. Cones: compute WEIL classes, then use BD-GAL

For the normal cone X=S(0,d), d>=2, its resolution is F_d->X given by |E+d f|. It contracts exactly the section E with E^2=-d and is an isomorphism off E onto X minus the vertex v. This description follows directly from the projective bundle O direct-sum O(d): the O(d) coordinates parameterize the rational normal curve, and the remaining coordinate is the cone direction. The whole section with those curve coordinates zero maps to v; elsewhere they determine the base and the fiber coordinate uniquely.

Removing v, a codimension-two subset of normal X, does not change Weil divisor classes. Localization on the smooth resolution therefore gives

    Cl(X)=Cl(X minus {v})=Cl(F_d minus E)
         =Pic(F_d)/Z[E]=(Z E direct-sum Z f)/Z E=Z[f].

The hyperplane class maps to [E+d f]=d[f]. This is an explicit Weil-class quotient, NOT substitution of the Picard rank of a singular model or of its resolution. Plane and Veronese cases are abstractly P2, so their Weil groups are likewise rank1; the Veronese polarization is O_P2(2), not O_P2(1).

Now apply the actual affine-normalization attachment. For any of these rank-one Ybar, let D_i be the DISTINCT components of Phi^*ell and put Y=Ybar minus union D_i, the same finite affine normalization as in section1. Weil-divisor localization is right exact:

    direct-sum_i Z[D_i] -> Cl(Ybar) -> Cl(Y) ->0.

The ample Cartier class L=sum m_i[D_i] is nonzero in Cl(Ybar) tensor Q: a torsion Cartier class has square0, whereas L^2=d>0. At least one boundary class is nonzero rationally and therefore spans the one-dimensional rational class group. It follows that Cl(Y) tensor Q=0; every affine class is torsion, with no finite-generation assumption required for this implication.

The accepted BD-GAL proper-block package requires the free lattice on missed divisorial components to inject into Cl(Y), and in particular a ramification-component class of infinite order. Its nonempty divisorial ramification assertion uses the retained purity/absence-of-nontrivial-finite-etale-covers-of-A2 facts; these are existing BD-GAL foundations, not a new smoothness assumption on Y. That infinite-order class cannot occur in a torsion group. Thus every rank-one case is impossible for this ACTUAL proper block. No Galois hypothesis is needed for the lattice implication.

The classified alternatives are exhausted: smooth scrolls contradict the promoted all-line donor theorem; plane/Veronese/normal cones contradict the old proper-block class lattice. Hence sectional genus0 is impossible. The conclusion concerns the genus of a general smooth complete-series section of the NORMAL FINITE model. It does not replace that model by a possibly nonfinite resolved map.

## 5. Controls, retained imports and scope

Positive-genus/rank-one control: the finite morphism P2->P2 given by [X:Y:Z]|->[X^4:Y^4:Z^4] has degree16, L=O(4), general sectional genus3 and Cl(P2)=Z. Thus rank1 does NOT imply sectional genus0, and finite positive-genus covers certainly exist. Its ramification divisor is three times the coordinate triangle, so (P2,R/2) has coefficient3/2 along each coordinate line and is NOT log canonical there. This explicitly prevents importing the old finite-cubic R/2 argument to all degrees. The example is not a Keller block; the old class-lattice condition already excludes it from that source role, and no positive-genus donor theorem is refuted or proved by the example.

A rank-two scope control is also elementary: compose the finite degree-two quotient P1 times P1->Sym^2(P1)=P2 with the target coordinate-square map. The resulting finite degree-eight cover has L=O(2,2), sectional genus1, and Weil rank2. Its ruling fiber degree is2, not1. The present genus-zero reduction and the rank-one screen therefore do not exclude it merely by these invariants; no claim of an admissible Keller first leg is attached to this cover.

Multiplicity control: localization uses the reduced components D_i but retains positive m_i in L=sum m_i D_i. Repeated or reducible infinity divisors cannot evade the spanning argument. Singularity control: no rational-singularity vanishing is used; no Picard-rank substitution is used for a cone. Normality of the minimal-degree IMAGE is proved before finite-birational isomorphism. Source control: a finite cover alone has no BD-GAL missed-divisor lattice; the literal actual A2 factorization is essential.

Named imports retained: BD-GAL's promoted factorization, missed-divisor lattice and its nonempty branch foundations; the promoted scroll theorem; standard surface resolution/indeterminacy elimination, blowup invariance of H1, Stein factorization/trace/Leray, Bertini and ample connectedness, projection formula, proper quasi-finite finiteness, and Weil localization. The primary minimal-degree inequality(*) and Theorem0.1 are charged from Eisenbud--Green--Hulek--Popescu, printed pages1-2 ONLY. Their classification proof and remaining25pages were NOT read or audited. No other primary theorem from those two pages is invoked.

The genus-zero part of the earlier smooth-cubic report is a narrower known client. The rank-one screen and log obstruction are also known mechanisms. This report supplies an all-degree NORMAL actual-block attachment; it does not assert global novelty. Previously closed d2=2/3 are not new frontiers. No primitive/no-block theorem, first-leg-degree restriction, all quartic/all rational-surface exclusion, positive-genus exclusion, actual Keller pair or JC2 conclusion follows. Any surviving actual proper-block finite model must have sectional genus at least1 and evade the old rank-one class-group screen.

QUANTITY settled at producer tier: genus-zero impossibility for the stated actual proper-block finite normal model. No mathematical OPEN remains in this precise argument, subject to the named imports. CHEAPEST NEXT TEST: one different-model FIRST on the H1 trace, minimal-degree normality/classification and cone-to-affine lattice attachment; <=20 minutes is an unmeasured planning estimate, not execution authority. No downstream promotion follows from this producer label.

## 6. Exact read scope and custody

All seven supplied pins matched before body reads. Fresh WHOLE text reads: new scroll gate59lines, BD-GAL integration156lines, smooth-cubic prior241lines (a clipped combined output was recovered in1-125 and126-241), rank-one prior126lines. Same-agent exact-current-pin WHOLE reuse: own scroll report, fully read at05:57UTC; COORDINATION806lines, fully read during05:51-05:53UTC. No linked provenance or live peer output was opened.

The primary PDF was whole-file HASH_ONLY except printed pages1-2 freshly read WHOLE using pdftotext -f1 -l2 -layout to stdout. The selected two-page extracted-text SHA is b805b4cfd491509da5e4c10ae6147fef83da961fbb5671ae7f71099848cecc06. No network or later PDF page was used. PINS records these modes. Own report/PINS readback, unchanged input postpins and own-target collision check precede the last marker; normal transaction and expected-manifest verification follow. Final custody includes exact input/owned pins and excludes itself. Old corrected-flow/scroll artifacts remain untouched.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12729`.
- Body SHA-256:
  `25c4bde75bdb67c0eb1b490849f754dac7d3d32e5924b9e8c6e15706a62caa19`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
