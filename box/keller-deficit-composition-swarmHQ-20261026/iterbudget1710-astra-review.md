# ITERBUDGET1710 — independent hostile review
Verdict: PASS / MANUAL at the stated all-Keller-parent scope. No material mathematical failure found.
Reviewer: retained configured Astra; independent review of ROOT's new composition proof, not a re-certification of every underlying parent dependency. Actual hosted identity and cost are unmeasured.
Reviewed ROOT report: briefs/iterbudget1710-root.md,75LF,SHA25663790b3c7b5084a4a0f45de90282319dcdea8609dce6f8b0832e21d0a678547d.
Accepted parent: public all-keller-sheet-budget-swarmHQ-root-astra-sol56-20261026T005000Z.md,97LF,SHA2565c4baaef7e6d5d1ab6edc68a1eb249b02732f001f5846e294557ee701eee5907.
Both reports, including seals, were personally read whole after complete metadata and canonical gates. No coverage was inferred from a successful verifier or borrowed from ROOT.
## Exact claim reviewed
For whole-plane complex Keller maps F,G, write N_H for field degree, a_H(y)=N_H-#H^-1(y), C_H for its codimension-one generic-deficit cycle, B_H for the sum of that cycle's coefficients, and S_H=N_H-1-B_H.
The reviewed identities are C_(F o G)=N_G C_F+F_*C_G, B_(F o G)=N_G B_F+B_G, and S_(F o G)=N_G S_F+S_G.
Consequently B_(F^n)=B_F sum_(j=0)^(n-1)N^j and S_(F^n)=S_F sum_(j=0)^(n-1)N^j. Iterating only B_H<=N_H-1 produces no stronger scalar inequality.
This is neutrality of the particular sum-of-coefficients budget, not of all information carried by the curves, valuations, local lengths or iterates.
## 1. Polynomial-curve image and finiteness — PASS
Let nu:A1->D be a finite birational normalization and let phi=F composed nu. Ambient etaleness implies quasifiniteness, so phi cannot be constant. Equivalently a local analytic inverse for F preserves nonconstancy of the branch germ.
Write phi(t)=(p(t),q(t)) and A'=C[p,q] inside C[t]. One component, say p, is nonconstant. Dividing p(T)-p(t) by its constant leading coefficient gives a monic equation for t over A', so C[t] is finite over A'. The image is the closed affine curve D'=Spec(A'). This does not assume F is proper on the plane.
The normalization B of A' in its function field embeds in C[t], since its elements are integral over C[t] and C[t] is integrally closed. The finite map A1->D' factors through this smooth normalization and remains finite.
For completeness, extend the induced map to smooth projective completions. Riemann-Hurwitz for the nonconstant map from P1 makes the target completion rational. Each removed target point must have a preimage among the single removed source point at infinity; the nonempty affine boundary therefore consists of exactly one point. Hence the target normalization is A1, and its induced map g from A1 is a nonconstant polynomial.
The author's later use of finiteness of F|D is justified by an implicit elementary step: C[D] is an intermediate finitely generated algebra A' subset C[D] subset C[t]. Every element is integral over A', because C[t] is integral over A'. Thus C[D] is finite over A', so F|D:D->D' is finite. No global properness of F is needed.
## 2. No ramification on the affine normalizations — PASS
The relevant assertion is local injectivity, not immersion of a singular curve parametrization. A normalization parameter disc at t0 maps injectively onto its selected analytic branch germ. One can shrink away from the other finitely many normalization points over the singular point and from all other singular points; away from that point, normalization is an isomorphism on the smooth branch. The cusp parametrization may have zero derivative and is still locally injective.
Because F is locally biholomorphic in the ambient smooth plane at nu(t0), phi=F composed nu is locally injective on this disc. If g had ramification index k>1 at t0, arbitrarily nearby distinct parameters would have the same g-value and therefore the same phi-value. This contradicts local injectivity, independently of whether nu' is an immersion.
This argument applies at every parameter, including each separate branch over a multibranch point. Thus g' has no zero on C. A nonconstant complex polynomial with this property has degree one.
The conclusion is degree one on normalizations. It does not imply global injectivity of F|D into a singular image: different normalization points can be identified by the target normalization map. It also does not imply delta_i=1 for omitted curves under the parent's finite h, which is not assumed ambient etale there.
## 3. Pointwise fibre counts and generic deficits — PASS
The parent finite normalization is flat of rank N_H and contains the whole marked source as an open subset. At source points the local fibre lengths are one, since H is etale. Consequently 0<=#H^-1(y)<=N_H at every y.
At a general point of a fixed omitted-image curve D, each omitted component over D contributes delta_i points of local length r_i. The generic deficit is therefore sum_(i over D)r_i delta_i, including coincident omitted images. This validates the identification of B_H with the parent's sum and S_H with its nonnegative local-excess slack.
Fibre counting for composition uses only finite sets: #(F o G)^-1(y)=sum_(z in F^-1(y))#G^-1(z). Generic field degrees multiply by the field tower, N_(F o G)=N_F N_G. Subtracting yields a_(F o G)=N_G a_F+F_!a_G pointwise.
In particular the multiplier on a_F is N_G, the degree of the INNER map. This order has been checked directly rather than inferred from an iteration convention.
## 4. Curve parts, exceptional points and coalescence — PASS
The parent gives finitely many omitted-image curves, each with finite A1 normalization. On each such curve the deficit equals its generic coefficient outside a finite set. Singularity and branch points, variation of local lengths and intersections of distinct components are also confined to finite sets for these algebraic curves.
A polynomial map sends a finite exceptional set to a finite set. Each curve of C_G is mapped finitely and with normalization degree one by sections1–2. Thus its contribution at a generic point of its image is exactly its old coefficient; no unproved properness or surjectivity of the whole-plane F enters this step.
When different components of C_G have the same image, remove the images of their pairwise intersections. Their generic preimage points are then distinct and all coefficients add. If the image also supports C_F, the two nonnegative terms in the pointwise identity add there as well. Neither overlap nor coalescence cancels a contribution.
Taking the curve part therefore gives exactly C_(F o G)=N_G C_F+F_*C_G, with the ordinary generic-degree definition of cycle pushforward on these finite curve restrictions.
The sum of coefficients is linear on curve cycles and preserved here because every transport degree is one. Coalescing components reduce the number of distinct supports, but do not reduce the sum of their coefficients. This proves B_(F o G)=N_G B_F+B_G. It would not prove preservation of projective degree or of valuation-weighted mass.
## 5. Slack, iteration and edge cases — PASS
Using the definition of S, direct subtraction gives N_F N_G-1-N_G B_F-B_G=N_G(N_F-1-B_F)+(N_G-1-B_G). Thus S_(F o G)=N_G S_F+S_G with the same order as the B identity.
For F fixed and G=F^(n-1), B_n=N^(n-1)B_1+B_(n-1), with B_0=0, and the same recurrence holds for S. Summing gives the displayed geometric series for every n>=1.
For N>1, N^n-1=(N-1)sum_(j=0)^(n-1)N^j with positive factor. Hence all iterated scalar inequalities are equivalent to B_F<=N-1. For N=1, the formula is nB_F and nS_F; parent effectivity and the budget imply B_F=S_F=0. No division by N-1 is used in that case.
An automorphism has empty omitted cycle and zero slack, consistent with all identities. The review does not require an assumed classification of degree-one Keller maps to verify this edge case.
## Verdict, qualifications and disposition
PASS: the claimed composition identities and exact scalar-budget neutrality follow at the accepted parent scope. The finite-restriction and selected-branch explanations above make implicit steps explicit; they do not require changes to the statement or sealed author bytes.
The parent all-Keller budget is an admitted dependency; this review read its entire97LF synthesis but did not fetch or newly audit the linked underlying reports. No additional scientific source, history query, calculation family or external theorem source was accessed. Standard normalization, complex inverse-function, curve-completion and finite-field-tower arguments were checked directly within this review.
This verdict does not supply properness, global injectivity on singular images, surjectivity, a common finite model, stabilization, valuation-weight control, projective image-degree control, pointwise redistribution of slack, N=1, or a proof/counterexample of JC2. It closes only amplification of this particular scalar budget by iteration.
All32 fixed inputs,12 physical/current-launch archive blobs,STATE equality and two canonical inputs passed before review. WholeSTATE200 completed17:17:30 UTC. Exact fresh reading windows, conservative inclusive count, lifecycle custody and terminal postpins are in the four companion JSONs.
## OPENS RAISED
None. No successor proposed or independent review of a different mechanism implied.
## COLLISIONS
No new history/source query was authorized or made. ROOT's frozen history coverage is not claimed as reviewer reading or as a novelty certificate; existing tower and degree-budget stops remain binding.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9510`.
- Body SHA-256:
  `8f562d37ce73ef84166a48ae5344ee10fc9e905c1b2cd3a96534b2b972e91492`.
- Frozen basis: `ced1b3d61cbbf01394274dc0a2e9144cddf7ee60`.
