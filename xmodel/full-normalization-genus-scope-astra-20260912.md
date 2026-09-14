# Full-normalization genus: source scope and pencil history

MANUAL / PRODUCER-CHECKED / UNPROMOTED. First action 2026-09-12 07:01:56 UTC; owned targets absent and all seven inputs pinned. Original reserve 07:18 / HARD 07:21 UTC unchanged. Text-only task; no scientific execution, coefficients, network, worker, protected-tree access or shared edit. Scope: extend the SOURCE attachment, not ascend a genus ladder or assert a genus ceiling.

## 1. Full-field source attachment

Claim: let F=(f,g):A2_C->A2_C be a hypothetical noninvertible Keller map, A=C[f,g], K=C(x,y), and B the integral closure of A in K. Let Phi:Ybar->P2 be the finite normal projective normalization in K and L=Phi^*O(1). Then the general smooth member of |L|, and the smooth projective completion of a generic pencil fiber alpha f+beta g=t, have genus at least two. The NEW work is attaching the full field; the geometric genus-zero/one arguments are accepted inputs.

Together with the accepted proper-K versions, this gives the sectional-genus condition for every Frac(A) strictly contained in K contained in or equal to C(x,y). The direct equality with SOURCE-pencil genus below is asserted only for the full field.

B is finite over A. Every b in B is integral over C[x,y] as well, because its monic equation has coefficients in A. Since b lies in C(x,y) and C[x,y] is normal, B is literally contained in C[x,y]. This defines j:A2->Y=Spec B with F=g2 j. The map j is finite type and its fibers lie in fibers of the etale, hence quasi-finite, F. It is therefore quasi-finite; it is birational because both fraction fields are K. Birational quasi-finite Zariski Main Theorem with normal target gives an OPEN IMMERSION. It is not asserted proper or surjective.

The restriction of Ybar over the target affine chart is exactly Y by uniqueness of normalization. Normal surfaces are CM, so the finite map g2:Y->A2 is flat over the regular surface base (local miracle flatness). On j(A2) it is etale, being identified with F. Thus its non-etale locus is missed by j.

For N=[K:Frac A]>1, divisorial ramification is nonempty: otherwise purity of the branch locus for a finite dominant map from a normal variety to a regular variety makes g2 etale everywhere. Connected finite etale covers of complex A2 are trivial, contradicting N>1. These are the same characteristic-zero purity/simply-connectedness foundations retained by BD-GAL, not a smoothness assumption on Y. A birational Keller map has N=1 and is invertible: then B=A and F is an open immersion; any missed divisor in the factorial target would be principal and contradict the next paragraph, so its complement has codimension at least two. Normal Hartogs gives the same global coordinate ring, making this affine open immersion an isomorphism. Hence noninvertibility indeed gives N>1.

The missing-principal and class-lattice arguments extend without d1>=2. A nonzero b in B whose nonempty zero set is entirely missed pulls back to a nowhere-zero polynomial, hence a nonzero constant. The literal inclusion B subset C[x,y] then makes b that constant, a contradiction. More generally, if div_Y(a) is supported on missed prime divisors, restriction to j(A2) makes a and a^-1 regular there, so both are units of C[x,y] and a is constant. Thus the free divisor group on missed codimension-one components injects into Cl(Y). In particular every ramification-component class has infinite order.

The nonfree-dual extension can be checked directly, rather than extending BD-GAL's label by fiat. Fix the ABSOLUTE canonical sheaf from the structure morphism to Spec C. Finite duality gives omega_Y=Hom_A(B,omega_A), canonically via composition of upper shriek and open restriction; omega_A=A df wedge dg. This is not an arbitrarily invertibly twisted dualizing module. The pullback of df wedge dg defines a section s of omega_Y: construct it on Y_reg and extend by reflexivity. At each height-one DVR it has order e_T-1, nonnegative in characteristic zero, and positive exactly on ramification components. If omega_Y were free, choose a global generator eta and write s=b eta, b in B. On j(A2), eta is a generator of omega_A2, hence a nonzero constant multiple of dx wedge dy. Keller makes s another nonzero constant multiple. Therefore j^*b is a nonzero constant, and the literal inclusion makes b constant in B. This contradicts the nonempty divisorial zero set of s. Thus Hom_A(B,A) is NOT free for this full normalization too.

## 2. Reusing the geometric arguments at their exact hypotheses

The source rational map P2-->Ybar resolves by point blowups to a proper birational map Z->Ybar. Normality gives pushforward O_Z=O_Ybar and the low-degree Leray injection H1(Ybar,O)->H1(Z,O)=0. Equivalently this is the accepted trace/Leray bridge with degree one. No rational-singularity assertion is used.

If the sectional genus were zero, the accepted proof's sections 2-4 apply verbatim after this source attachment: h0(L)=N+2, the complete-series map is finite birational onto a normal minimal-degree surface, and classification leaves smooth fiber-degree-one scrolls or the plane/Veronese/rational-normal-cone cases. The scroll donor theorem already allows ANY dominant everywhere-defined first leg, including this open immersion. It excludes the actual source in the complement of ramification and the chosen infinity divisor. The remaining cases have rational Weil-class rank one; quotienting by the nonzero ample infinity class makes Cl(Y) torsion, contradicting the full-model missed-divisor lattice just proved. No new classification or singular Picard-rank substitution is introduced.

If the genus were one, the accepted normal-surface lemma yields omega_Ybar tensor L=O: CM Serre duality lifts an elliptic differential, its effective divisorial zeros have L-degree zero, and reflexivity extends the resulting trivialization across singular points. Restricting to Y trivializes L. The canonical structure-morphism dualizing complex restricts and composes with g2^!, so omega_Y is exactly Hom_A(B,A), not a possible invertible twist. Its resulting freeness contradicts section 1. This uses the new gate's explicit canonicity clarification. Thus genus zero and one are both impossible for the full field, independently of whether any proper intermediate field exists.

## 3. Complete series versus the original line net

One must NOT equate individual curves or linear systems. The original net V=Phi^*H0(P2,O(1)) is a three-dimensional SUBSPACE of H0(Ybar,L), possibly proper. It is nevertheless base-point free and defines the finite map Phi. A general member C_net avoids the finite singular set and is smooth and integral by characteristic-zero Bertini for this non-pencil system. The same holds for a general C_complete in the complete series. Both are effective Cartier divisors of class L. The exact sequence 0->L^-1->O_Ybar->O_C->0 makes their Euler characteristics equal. As both curves are smooth connected, their geometric genera coincide. This proves equality of the generic genera, not equality of the members or genericity of every net member in the complete series.

Moreover C_net meets the open j(A2) densely: a general member is not contained in its fixed proper closed boundary. This intersection is exactly F^-1(ell). Hence C_net is the smooth projective completion of that smooth integral affine curve. A generic target affine line is alpha u+beta v=t, so for generic direction and generic t the genus of alpha f+beta g=t is the same sectional genus, at least two. No claim is made for every direction, every t, or every special fiber. For a proper intermediate K instead, the source curve maps to the block curve with first-leg degree d1; their genera are NOT automatically equal. The full-field open immersion is essential to the direct pencil attachment.

## 4. Historical comparison and precise remaining client

The entire charged September 2 pencil report was read as HISTORY/CONTEXT at its recorded tiers. Its section 9 explicitly calls its new results PROVED-HERE/UNREVIEWED; its reported 61 genus computations, cell pricing, driver outputs and measured resources were not replayed, independently validated, or promoted here. No linked input was followed. The present theorem is not based on those numerical data.

That text distinguishes three useful formulas: adjunction on a resolved source gives 2g_L-2=N+Z.K; its FORK-GENUS expression is 2g_L-2=N-kappa-Lambda+Psi; and under its retained H2/profile hypotheses its Riemann--Hurwitz expression is 2g_L-2=-N+n(W-S)-kappa. Here Lambda is leaf mass and Psi fork mass. None of these identities supplies an upper bound for g_L. Its chain ceiling requires the unproved Psi=0 (and a stronger variant also requires a designated leaf). Its Suzuki/Euler ledger is explicitly another identity. Its relaxed non-Keller examples illustrate why profile data alone need not cap genus; their computational verification is old context, not new evidence.

If those formulas are used at their independently applicable historical tiers, substituting the newly attached g_L>=2 gives only

    Psi-Lambda >= kappa+2-N,
    n(W-S) >= N+kappa+2  [only with the old H2/profile hypotheses].

These are LOWER bounds. They do not bound fork excess, n, delta_aff, satellite mass, polynomial degree, or the size of an enumeration. No H2-specific theorem is promoted here. The old report explicitly leaves the condition kappa=1 => g_L>=1 as its recorded OPEN[MF-DEFECT]; the new source theorem would imply that displayed condition, more strongly and without kappa=1. This is a comparison to a dated document, NOT a claim that the campaign still has that OPEN or a reopening of any closed degree case. No N=4 consequence, cell price, primitive exclusion or new computation is claimed.

Verdict: USEFUL SOURCE-SCOPE EXTENSION, including full normalization and primitive-source situations; NOT a genus ladder. It is not already stated in the charged pencil report, which lacks this global affine-dual argument. But NO_DECISIVE_CEILING_OR_FINITE-SEARCH_CLIENT is supplied: the history comparison reveals no accepted upper bound with which to close a contradiction for all survivors. The concrete conditional client is simply any independently established generic-line genus <=1. No such new upper bound is proved or imported, and there is no literature-wide novelty or whole-portfolio assertion.

## 5. Controls, read scope and custody

The N>1/noninvertible condition is essential: an automorphism has full normalization P2 with L=O(1), sectional genus zero, and empty affine ramification, so the contradiction deliberately does not apply. Finite covers alone remain unrestricted by the source step: the accepted P1 times P1 degree-eight example has genus one and free affine dual, but no admissible Keller source. Rationality alone supplies no upper bound: P2 with polarization O(4) has sectional genus three, as in the charged genus-zero control. Nothing here excludes genus at least two or proves JC2. Missing divisors may be nonprincipal; ZMT does not turn the open immersion into surjectivity. Different curve systems may have equal generic genus without having equal individual members.

Quantity settled at producer tier: full-field genus >=2 and its exact generic-line attachment. No mathematical GAP remains subject to the named standard imports (normalization finiteness, ZMT, purity and finite-etale triviality of complex A2, CM flatness, canonical finite duality, and Bertini), plus the already accepted geometric lemmas. The unresolved DECISIVE CLIENT is an upper bound or another incompatible invariant, not the source map. Cheapest next test: one focused different-model FIRST on the full-model lattice/nonfree-dual extension and line-net identification; <=15 minutes is UNMEASURED review planning only. No downstream authority or further task follows.

All seven pins matched before charged body reads. FRESH_WHOLE: the new terminal genus-one gate; the entire 739-line old pencil report in ranges 1-200,201-390,391-570,571-739 (the final requested range extended to EOF). REUSED_WHOLE after current pins: own genus-one report, fully read 06:46:54 today; own genus-zero report and BD-GAL, fully read 06:42:37; genus-zero gate, fully read after its 06:42:37 pin; COORDINATION, all 806 lines read in four ranges during 05:51-05:53. The new gate's explicit upper-shriek canonicity is retained; its unrelated sanity-check embellishments are not premises.

PINS records the exact modes. Own report/PINS WHOLE readback, unchanged postpins, owned-target collision and quantity/client checks precede the last marker. Normal transactional close/finalize and expected-manifest verification follow, then custody with all input/owned hashes excluding itself. All earlier reports remain immutable. This is a manual source-scope/history result awaiting FIRST, with zero scientific execution.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12887`.
- Body SHA-256:
  `411e75effae268de2c0132aa1eeacbe55dd5456d43c2495f563c8a78defa7704`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
