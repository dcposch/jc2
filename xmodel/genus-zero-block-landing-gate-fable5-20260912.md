# FIRST gate (Fable 5.1, hostile reviewer): genus-zero proper-block landing

- started_utc=2026-09-12T06:30:16Z
- reviewer=Fable5.1 (independent of Astra)
- target=xmodel/genus-zero-block-landing-astra-20260912.md
- status=REVIEW WRITTEN; the standalone BODY-END marker is appended last and only after whole readback
- hard_deadline_utc=2026-09-12T06:51:00Z reserve 06:48Z

## 0. Custody (prepins, hashed before any body read)

Four /tmp/jc2-lane.GyvznX/inputs snapshots hashed at 06:30:26Z before any body read. Rows below are generated from sha256sum output. Every row equals the expected value in the charge.

697b1128c95d5a8155a25f1fae739a223447fb36414b1fc65965270f2bcefd77      prepin genus-zero-block-landing-astra-20260912.md
1aede0f67970ff01b9a599352086a7c72d51cf610e1ae52db088f9e3fc2f0997      prepin scroll-fiber-one-donor-astra-20260912.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8      prepin block-descent-galois-coordinator-integration-sol56-20260830.md
39c85a00fe9b133134acadddbeb0bdaeafbffb5d1bcb9f71536624e8597032b4      prepin eghp-minimal-degree.pdf

Selected PDF extraction (pdftotext -f 1 -l 2 -layout, stdout only), generated:

b805b4cfd491509da5e4c10ae6147fef83da961fbb5671ae7f71099848cecc06    pages1-2 extraction (expected b805b4cf...)

## 1. Scope read

Read modes: the three Markdown snapshots were read WHOLE by a single cat each (landing report sections 1-6 plus seal; scroll donor report sections 1-6 plus seal; BD-GAL integration sections 0-4 plus seal). The PDF was read ONLY on printed pages 1-2 through pdftotext to stdout; a tee copy into the read-only lane directory failed harmlessly and no file was created. Pages 3-27 were not read, no reference was followed, and the classification proof is not audited here. From those two pages only the inequality (*) deg(X) >= 1 + codim(X, span X) and Theorem 0.1 (linear space, quadric hypersurface in a linear space, rational normal scroll, cone over the Veronese surface) are used, as named classical imports, exactly as in the old cubic client. No code, CAS, arithmetic execution, network, git or process inspection was used; every check below is manual.

Accepted premises, not re-hardened: the promoted scroll theorem (every e, every finite Phi: F_e -> P2 with L.f = 1, every target line, arbitrary first leg); BD-GAL's sandwich A2 --g1 etale quasi-finite--> Y = Spec(B_K) --g2 finite flat--> A2, its missed-divisor class-lattice injection into Cl(Y), and its nonempty divisorial branch foundation. Exact target checked: sectional genus of the finite normal projective normalization Phi: Ybar -> P2 in K, with L = Phi^*O(1), cannot be 0, all degrees. Nothing about block existence, primitive/no-block exclusion, positive-genus exclusion, d1 = 2, or JC2 is asserted, and the report says so.

## A. Normalization and H1(O_Ybar) = 0: CONFIRMED

Identification. Normalization of a scheme in a finite extension of its function field is local on the base. Over the affine target chart Spec C[f,g] the normalization of P2 in K is Spec of the integral closure of C[f,g] in K. BD-GAL's B_K is finite over C[f,g] (g2 finite) and integrally closed with fraction field K (Y normal), so B_K equals that integral closure. Hence Ybar restricted over the chart is literally Y, and Phi restricted is g2. No resolution is substituted.

Vanishing. The composite A2 -> Y -> Ybar is a dominant morphism from the affine source, so P2 --> Ybar is a rational map to a projective variety, regular on A2; indeterminacy on a smooth surface is resolved by finitely many point blowups, giving Z -> Ybar proper and generically finite with H1(Z,O) = H1(P2,O) = 0 (blowup invariance). Stein factorization Z -> W -> Ybar has W integral, W -> Ybar finite of degree n = d1 > 0, and (Z->W)_*O_Z = O_W. Trace: over an affine piece Spec A of Ybar with preimage Spec B, A is a normal domain with fraction field K, B is integral over A, and C(x,y)/K is separable, so Tr(B) lies in K and is integral over A, hence in A. Thus (1/n)Tr splits the inclusion O_Ybar -> pi_*O_W as O_Ybar-modules, and H1(Ybar,O) injects into H1(Ybar, pi_*O_W) = H1(W,O) (finite morphisms are affine, no higher direct images). Then the Leray five-term sequence gives 0 -> H1(W, sigma_*O_Z) -> H1(Z, O_Z), which is the edge map alone; with sigma_*O_Z = O_W this injects H1(W,O) into H1(Z,O) = 0. Both injections are checked; the chain closes.

Attacks. Flatness of Phi is never used (it happens to hold, a normal surface is Cohen-Macaulay, but nothing depends on it). Rational singularities: not used; the argument never asserts R1 rho_*O = 0 for any resolution. Rationality of Ybar: not used; the dominating Z is rational but Ybar's own rationality is not invoked. R1 vanishing: not needed, injectivity of the low-degree edge map suffices. The alternative route in the report (a rational resolution S with rho_*O_S = O_Ybar) is also valid but is explicitly not the route used. Characteristic 0 enters only through 1/n and separability. No gap.

## B. General member, h0(L) = d + 2, birational minimal-degree image: CONFIRMED

L is the pullback of O(1) by a finite morphism, so it is ample and globally generated, with L^2 = deg(Phi) = d = [K:C(f,g)] by the projection formula. Sing(Ybar) is finite (normal surface). Because |L| is base-point free, the members through a fixed point form a hyperplane of the complete |L|; finitely many points give finitely many hyperplanes, so a general member avoids Sing. Bertini for a base-point-free system on the smooth quasi-projective open gives smoothness there; Jouanolou-Bertini irreducibility applies because the complete-series morphism has two-dimensional image, so the general member is irreducible, hence connected. None of this needs a smooth Ybar or rational singularities.

If the general member C has genus 0 it is P1. C is an effective Cartier divisor (zero scheme of a nonzero section of a line bundle on an integral surface) with O(C) = L, deg L|_C = L.C = L^2 = d, so h0(L|_C) = d + 1, and the sequence 0 -> O -> L -> L|_C -> 0 with H1(O_Ybar) = 0 from A gives h0(L) = d + 2. The complete series defines psi: Ybar -> P^(d+1), a morphism since L is base-point free; a positive-dimensional fibre would contain a curve of L-degree 0, contradicting ampleness, so psi is quasi-finite and projective, hence finite. Its image X, with reduced structure, is an irreducible surface, and nondegenerate since a hyperplane containing X would be a section of L vanishing identically. Inequality (*) with span X = P^(d+1) gives deg X >= 1 + (d - 1) = d, while d = L^2 = deg(psi) deg X. Hence deg psi = 1 and deg X = d. This uses only the complete series; no claim that the original net embeds anything is made or needed. No gap.

## C. Exhaustive dimension-2 list and independent image normality: CONFIRMED (Theorem 0.1 as named import)

Theorem 0.1 as printed lists linear spaces, quadric hypersurfaces in a linear space, rational normal scrolls, and cones over the Veronese surface in P5. Restricting to surfaces: P2 (d = 1); an irreducible quadric surface in P3 (d = 2), which is smooth (S(1,1) = F_0) or the rank-3 cone (S(0,2)); rank <= 2 quadrics are reducible or nonreduced and cannot be the integral X; two-dimensional rational normal scrolls S(a,b), 0 <= a <= b, a + b = d, smooth for a >= 1 and the rational normal cone for a = 0 (standard convention includes the cones; the report reads it that way, which is the inclusive and therefore safe reading); the Veronese surface itself (d = 4), since a cone over it with nonempty vertex has dimension >= 3. The list in the report is exactly this. Exhaustiveness rests on the classical theorem as charged, not on an audited proof; that is the agreed framing.

Normality is proved per case and not inferred from the normal source, as the charge demands. Smooth cases are trivial. For S(0,d), d >= 2: the chart containing the vertex is the affine cone over the rational normal curve, i.e. Spec of the d-th Veronese subring of C[u,v], which is the invariant ring of the scalar mu_d action. An element of Frac of the invariant ring integral over it is integral over C[u,v], lies in C[u,v] by normality, and is invariant, so it lies in the invariant ring; off the vertex the cone is the total space of O_P1(d), smooth. So X is normal in every case, and finite birational psi onto normal X is an isomorphism because psi_*O_Ybar is a finite O_X-algebra inside the function field. The polarization is identified correctly: L = psi^*O_X(1), so P2 carries O(1) (d = 1, impossible anyway since K is proper over C(f,g)), the Veronese surface carries O_P2(2) with d = 4, the smooth quadric carries O(1,1), S(a,b) with a >= 1 is F_(b-a) with L = E + b f (L^2 = -(b-a) + 2b = a + b, L.f = 1), and S(0,d) carries the hyperplane class of the cone. No gap.

## D. Smooth scroll leg lands in the exact donor open: CONFIRMED

For S(a,b) with a >= 1, Ybar is F_e, e = b - a, and L = E + b f with L.f = E.f = 1 for the ruling f (for e = 0 take the ruling of degree 1; one always exists). The promoted theorem quantifies over every e >= 0, every finite complex morphism Phi: F_e -> P2 with Phi^*O(1).f = 1, every target line, and every dominant everywhere-defined first leg, finite or not. The actual Phi composed with the isomorphism of C is such a morphism. Take ell the line at infinity of the target chart. Then Y = Ybar minus supp(Phi^*ell) is exactly the affine normalization, and the donor open is U = Y minus supp Ram(Phi). The actual g1: A2 -> Y is an everywhere-defined dominant morphism. It misses Ram(Phi): the image lies in the smooth locus (etale over a smooth source), and there dF = dg2 o dg1 with dF invertible (Keller) and dg1 invertible (etale), so dg2 is invertible at every image point; equivalently g2 is etale at g1(p) because g2 o g1 and g1 are. Since Ram(Phi) restricted to Y is the Jacobian divisor of g2, g1 lands in U and dominates it. This contradicts the promoted theorem for every degree d = 2b - e and with the specific line ell, no genericity of the line being used. No gap.

## E. Cone class group and torsion after line removal versus BD-GAL: CONFIRMED

Cone. The morphism F_d -> S(0,d) given by |E + d f| (E^2 = -d) contracts E, since (E + d f).E = 0, and is an isomorphism from F_d minus E onto X minus v; both sides are the total space of O_P1(d) over the rational normal curve, so the report's projective-bundle description is right. Removing the vertex, a codimension-two point of a normal surface, leaves Cl unchanged; the localization sequence Z -> Cl(F_d) -> Cl(F_d minus E) -> 0 with 1 -> [E] and Cl(F_d) = Pic(F_d) = Z E + Z f gives Cl(X) = Z[f], free of rank one. The hyperplane class pulls back to E + d f and restricts to d[f]; consistency check: the affine cone then has Cl = Z/d, the known value. This is a Weil computation, not a Picard rank of a singular model or of its resolution. P2 and the Veronese image are abstractly P2 with Cl = Z.

Affine part. With D_i the distinct components of Phi^*ell, the sequence (+) Z[D_i] -> Cl(Ybar) -> Cl(Y) -> 0 is exact for the same Y as in A. The Cartier class L = sum m_i [D_i] is not torsion: n L ~ 0 would give n^2 L^2 = 0 against L^2 = d > 0. In Cl(Ybar) = Z any nonzero subgroup has finite index, so Cl(Y) is finite, in particular torsion, with no finite-generation input. BD-GAL's class-lattice injection (its section 2, proved from the source-unit mechanism on a normal Y, no smoothness and no Galois hypothesis) makes every codimension-one component of Z = Y minus g1(A2) of infinite order in Cl(Y). Every component of Ram(g2) lies in Z (D above), is of codimension one by purity, and exists by the accepted nonempty-branch foundation. An infinite-order class in a torsion group is impossible, so no rank-one case occurs. The hidden-hypothesis attacks fail: multiplicities m_i are kept, reduced components are used only for the localization, and the contradiction uses BD-GAL exactly as promoted. No gap.

## F. Controls: CONFIRMED, with the bound stated

Degree 16. [X:Y:Z] -> [X^4:Y^4:Z^4] is finite of degree 16, L = O(4), L^2 = 16, and a general quartic has genus 3; Cl(P2) = Z. Ramification: in the chart Z = 1 the Jacobian is 16 x^3 y^3, and globally R = K - Phi^*K = -3H + 12H = 9H = 3 times the coordinate triangle. So (P2, R/2) has coefficient 3/2 on each line and is not log canonical. This verifies that rank one does not force genus 0 and that the finite-cubic R/2 log-canonicity mechanism cannot be imported to higher degree; the report says exactly that and nothing more.

Degree 8. The symmetric quotient P1 x P1 -> P2 is given by bidegree (1,1) forms, so composing with the target squaring map gives L = O(2,2), L^2 = 8 = degree, sectional genus (2-1)(2-1) = 1, Weil rank 2, and L.f = 2. It is outside the L.f = 1 donor hypothesis and outside the rank-one screen, and it has positive genus, so the new theorem says nothing about it.

Why neither is an admissible first leg. For ell = {Z = 0} both affine parts are A2 with Cl = 0, while the ramification of g2 is nonempty (the axes x = 0, y = 0 in degree 16; the diagonal and the axes in degree 8). The accepted BD-GAL lattice injection then fails, so neither can be the sandwich Y. For any other line the free group on the distinct ramification components (three lines; six curves including the diagonal) cannot inject into a class group of rank at most 1 or 2. Both exclusions come from the old lattice premise, not from the new genus-zero theorem, and the report claims no block role for either. Neither refutes a positive-genus statement, because none is proved or asserted: the theorem forbids genus 0 only. Bound: any surviving actual proper-block finite normal model has sectional genus >= 1 and must still pass the old rank-one class-group screen; the log-canonical control is a scope fence, not a higher-degree theorem.

## Verdict

- A CONFIRMED. B CONFIRMED. C CONFIRMED (exhaustiveness = charged Theorem 0.1 import). D CONFIRMED. E CONFIRMED. F CONFIRMED.
- Overall: the new source/classification attachment holds against the exact promoted statements of the scroll theorem and BD-GAL. No GAP, no REFUTED item.
- Minor clarifications, not gaps: (i) for e = 0 the ruling with L.f = 1 must be the one chosen; (ii) Cl(Y) in the rank-one cases is finite, stronger than torsion; (iii) the cone chart normality is the classical Veronese-subring statement.
- Not asserted here, consistent with the charge: block existence, primitive/no-block exclusion, positive-genus exclusion, d1 = 2 exclusion, novelty, JC2. Previously closed d2 = 2/3 are unaffected. Result remains PROVISIONAL; promotion, custody and terminal receipt belong to ROOT. No descendants launched.
- Writes: this report only; append-only after the placeholder skeleton was replaced; no artifact_finalize, no charge_basis (no exit-price assertion is made).

## Postpins

Unchanged input pins re-hashed after the review text was written (rows generated from sha256sum):

697b1128c95d5a8155a25f1fae739a223447fb36414b1fc65965270f2bcefd77    postpin genus-zero-block-landing-astra-20260912.md
1aede0f67970ff01b9a599352086a7c72d51cf610e1ae52db088f9e3fc2f0997    postpin scroll-fiber-one-donor-astra-20260912.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8    postpin block-descent-galois-coordinator-integration-sol56-20260830.md
39c85a00fe9b133134acadddbeb0bdaeafbffb5d1bcb9f71536624e8597032b4    postpin eghp-minimal-degree.pdf

- postpin_utc=2026-09-12T06:38:42Z

<!-- BODY-END -->
