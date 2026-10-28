# NEGREVIEW0200 hostile mathematical review

Reviewer: requested Sol gpt-5.6-sol; hosted identity unverified.  
Object reviewed: frozen `candidate-negative0100.md`; the reviewer did not author it.  
Verdict: **PASS_CONDITIONAL**.

## Exact verdict

The candidate's structural lemma is sound for the particular normalized polynomial Keller representative (H), degree (N>1), and infinitely singular (A=0) eigenvaluation η named in `complete-inverse-splitting.md`, conditional on the external foundations listed below. Under those hypotheses,

- (f=H_\bullet:D=\{A<0\}\to D) is continuous, surjective, closed, compact-preimage proper, and has fibres of at most (N) points;
- if (f) were a local homeomorphism everywhere, it would be a one-sheeted covering and hence injective;
- the two specific distinct (A=0) inverse ends supplied by inverse splitting force noninjectivity on (D), so (f) is not a local homeomorphism somewhere on (D); and
- at a negative divisorial point, geometric residue degree (f_v>1) is indeed a sufficient local-fold mechanism, with the qualifications below.

This is not a proof that a hypothetical Keller counterexample cannot exist. It gives a necessary failure of local homeomorphism, not the missing Keller-specific control that would forbid that failure.

## Foundations retained as hypotheses

This review assumes, rather than re-proves:

1. The weak valuation space (V_0) is compact Hausdorff and is a rooted nonmetric topological tree; its tangent branches are open and convex, its closed arcs are compact, and it has convex arc-connected neighborhood bases, including at ends. Thinness (A) is lower semicontinuous and is strictly increasing on every nondegenerate ordered arc. The valuation-type facts include: every (A<0) point is a finite-valued rank-one valuation of the function field, and (H_\bullet) preserves the infinitely singular type where ρ is positive.
2. For this (H), ρ(v)=d(H,v) is continuous, (H_\bullet) is continuous on ρ>0, and
   \[
   A(v)=\rho(v)A(H_\bullet v)
   \]
   there. From the THIN1505 dependency, only the named-source conditional assertion ρ=0 ⇒ (A\geq\epsilon_H>0) is used. The three THIN1505 summaries are not treated as an independent proof of that assertion.
3. A finite-valued valuation prolongs through the finite field extension (H^*\mathbf C(x,y)\subset\mathbf C(x,y)), and the fundamental inequality bounds the number of distinct prolongations by (N). Equality with a sum of (ef)'s is not needed here.
4. `complete-inverse-splitting.md` supplies, for this same (H) and η, at least two distinct normalized preimages (v_1,v_2) with (A(v_i)=0); its named FJ and characteristic-zero defectless foundations remain external. No assertion about all (A=0) valuations, or about α, (V_1), or other inverse points, is imported.

## Hostile checks

### Compactness, sign invariance, compact preimages, and closedness

Lower semicontinuity makes (K_0=\{A\leq0\}) closed in compact (V_0), hence compact Hausdorff. The strict killed-set premise gives ρ>0 on all of (K_0), so (f) is continuous there. The thinness identity and ρ>0 give the two-way sign statements

\[
A(v)<0\iff A(f(v))<0,\qquad A(v)=0\iff A(f(v))=0
\]

for (v\in K_0).

If (C\subset D) is compact, then it is closed in the Hausdorff space (K_0). Thus (f^{-1}(C)), taken in (K_0), is closed and compact; sign invariance puts it in (D). This proves exactly compact-preimage properness. It does not use, and should not be reworded as depending on, openness or local compactness of (D), or on a uniform bound (A\leq-\delta) on (C).

If (C) is relatively closed in (D), then

\[
\overline C^{K_0}\cap D=C,
\qquad
f(C)=f(\overline C^{K_0})\cap D.
\]

The second equality follows because a point of the closure mapping into (D) must itself lie in (D). The compact set (f(\overline C^{K_0})) is closed in (K_0), so its intersection with (D) is relatively closed. The candidate's closed-map assertion is therefore correct without any hidden openness assumption on (D).

### Surjectivity and finite fibres

The finite-valued qualification is essential. For (y\in D), prolong (y) from (H^*K) to a field valuation (w) on (K=\mathbf C(x,y)). It cannot be affine-centered: otherwise (w(P),w(Q)\geq0), contradicting the normalization of the target infinity valuation (y). Hence

\[
b=-\min(0,w(x),w(y))>0,qquad u=w/b\in V_0.
\]

Then ρ(u)=1/b, (f(u)=y), and the thinness identity gives (A(u)=A(y)/b<0). This proves surjectivity onto (D).

Conversely, a point (u\in f^{-1}(y)) is finite-valued and has one unique positive rescaling whose restriction to (H^*K) is exactly (y). Thus fibre points inject into the set of prolongations. The fundamental inequality yields at most (N) such points. This is a point count only: it neither says that every negative fibre has (N) points nor identifies point count with \(\sum ef\).

### Closed local homeomorphism and the nonmetric tree

Let (p:X\to Y) be surjective, closed, a local homeomorphism, and have finite fibres, with (X) Hausdorff. Around the finitely many points over (y\), choose pairwise disjoint local-homeomorphism charts. Intersect their target images and delete the closed image of the complement of their union. The remaining neighborhood of (y) is evenly covered. Applying this to (f:D\to D) proves the finite-covering assertion; no local compactness theorem is involved.

The set (D) is convex because (A) increases away from the root, so it is connected and uniquely arc-connected. Its weak topology has convex arc-connected local bases; this remains true at an infinitely singular endpoint, where a basic neighborhood contains a terminal arc. Hence (D) is locally path connected despite being nonmetrizable.

There is also no hidden metrizability assumption in simple connectedness. A loop has compact image. In a weak topological tree, a connected subset is convex: omission of an interior point of the unique arc would separate it into open tangent branches. The loop image is therefore a compact uniquely arc-connected subtree; as a Hausdorff continuous image of a compact metric circle, it is metrizable, and it is a dendrite, hence contractible. Thus every loop in (D) is null-homotopic. Standard path and homotopy lifting now shows that a connected covering of (D) has one sheet. Since the covering's total space is the connected space (D), an everywhere local-homeomorphic (f) would be injective.

### The two inverse ends really contradict injectivity on (D)

Type preservation makes the distinct (v_1,v_2) infinitely singular ends, hence incomparable. Their meet (m) is strictly below each. Strict increase of (A) gives (A(m)<0), so (m\in D).

Put (a=f(m)\wedge\eta). Since (f(m)\in D) while (A(\eta)=0), (a<\eta) and (A(a)<0). Choose (t\in(a,\eta)). Strict increase gives (A(t)<0). The tangent branch (U) at (t) toward η is weakly open and convex, contains η, and excludes (f(m)).

Continuity at each (v_i), together with the fact that points of the arm ((m,v_i)) approach the endpoint, gives (u_i\in(m,v_i)) with (f(u_i)\in U). Strict thinness on each arm gives (u_i\in D), and convexity gives the compact arc ([u_1,u_2]\subset D), containing (m).

If (f|_D) were injective, its restriction to this compact arc would be an embedding into the Hausdorff target. Its image would be the unique arc between (f(u_1)) and (f(u_2)), which lies in convex (U). But the image also contains (f(m)\notin U), a contradiction. No end compactification, α-sign, or (V_1) claim is used.

### Residue degree greater than one

The residue-fold sentence is valid with the following exact meaning. Let (v\in D) be divisorial, let (w=f(v)), and realize the associated divisors (E,E') on models where (H) is a morphism at their generic points. Write

\[
f_v=[\mathbf C(E):\mathbf C(E')].
\]

If (f_v>1), the induced map φ:(E\to E') is generically separable in characteristic zero. A generic point (q\in E') therefore has (f_v) distinct unramified points (p_j\in E). These points represent distinct tangent directions at (v) mapping to the one direction represented by (q) at (w).

In local coordinates (E=(u=0)), (E'=(U=0)), one has (H^*U=u^{e_v}) times a unit, while at an unramified (p_j), a tangential parameter pulls back with nonzero linear tangential term. Consequently a sufficiently short valuative segment in every (p_j)-direction maps onto an initial segment in the same (q)-direction; (e_v) only rescales the segment parameter. Any relative weak neighborhood of (v) contains initial pieces of these arms, and (A(v)<0) keeps sufficiently short pieces inside (D). Two of the image segments overlap, producing two source points with the same image. Thus (f) is not locally injective at (v).

This does not say that (f_v=1) is sufficient for a weak local homeomorphism. Special tangent directions and a single uniform source neighborhood remain uncontrolled. Likewise (e_v=1), constant Jacobian, and absence of affine critical points do not replace the missing local-homeomorphism premise.

## Remaining JC2 gap

The proved-in-this-review implications are only the topological consequences above and the qualified divisorial fold. The valuation-tree, thinness, prolongation, and particular inverse-splitting statements remain assumed external foundations. The unresolved global Keller input is a theorem forcing (H_\bullet) to be a local homeomorphism throughout (D), or otherwise excluding every possible weak-topology fold. The candidate supplies neither. Accordingly the result is PASS_CONDITIONAL for this structural lemma only, not a JC2 result or a full audit of its cited sources.

The separate ROOT norm-degree inequality and the atomic-measure construction were not used. No new exit-price claim is made; no `charge_basis` object is appropriate for this topology-only review.

## Reviewer coverage and source tier

- Manifest: `input-manifest.json` lines 1–162, whole, read first.
- Whole operational governors: `HQ-AGENTS.md` 1–23; `HQ-POLICY.md` 1–112; `HQ-RESEARCH_POLICY.md` 1–162; `HQ-RESTRICTIONS.md` 1–259; `HQ-RUNBOOK.md` 1–481; `PUBLIC-AGENTS.md` 1–22; `PUBLIC-README.md` 1–102; `PUBLIC-COORDINATION.md` 1–107; `PUBLIC-FALLACY-v2.md` 1–36. Total: 1,304 LF.
- Current state: `HQ-STATE.md` lines 1–181, whole, completed before scientific reading; counted separately.
- Scientific inputs: `candidate-negative0100.md` 1–13; `complete-inverse-splitting.md` 1–76; `thin1505-terminal.json` 1–14; `thin1505-root-integration.json` 1–14; `thin1505-astra-result.json` 1–23, all whole.
- Fresh cached primary reading: `FJ2007.txt` 1383–1430 and 1735–1782 (96 LF total); `FJ2011.txt` 249–272 (24 LF). Total primary: 120 LF. These windows support only their displayed definitions and tree/topology/thinness statements; proofs and cited dependencies outside the windows, including the full Jacobian-thinness and inverse-splitting foundations, were not audited.
- Total non-STATE body reading: 1,726 LF, including the 120 primary LF. No truncation was relied on.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11005`.
- Body SHA-256:
  `235524858255a99ae9402050edecf1828fb28acb84511f209db6f2e2f91c4d0a`.
- Frozen basis: `8b2578db54ebb4eef46291b642cf61146f83dbdb`.
