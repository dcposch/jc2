# Genus-one normal proper-block landing — hostile gate (Fable 5.1)

- lane=genus-one-block-landing-gate-fable5-20260912
- reviewer=Fable5.1 (independent hostile), status=MANUAL/PROVISIONAL, no descendants
- first_action_utc=2026-09-12T06:51:20Z (skeleton written 06:51:2x, before any body read)
- reserve=07:08Z HARD=07:11Z (never extend)
- target=xmodel/genus-one-block-landing-astra-20260912.md

## 0. Custody (prepins, hashed before any body read)

Rows generated from sha256sum at 06:51:27Z on /tmp/jc2-lane.agWjFA/inputs. Every row equals the expected value in the charge.

648861914149486b54c6852f8d606a366d34fe82c93f4138b09116c318465a11  prepin genus-one-block-landing-astra-20260912.md
cc1eaca421d769e576ef454780421b88a7fceb30c3bb87f7c386ccb0dd25a59b  prepin genus-zero-block-landing-gate-fable5-20260912.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8  prepin block-descent-galois-coordinator-integration-sol56-20260830.md

Read mode: each snapshot read WHOLE by one cat, including seals. No reference followed, no other source, no code/CAS/arithmetic execution, no network/git/process inspection. Every check below is manual.

## 1. Claim under review and accepted premises

Claim: C(f,g) strictly inside K strictly inside C(x,y) for a hypothetical complex Keller map; Phi: Ybar -> P2 the finite normal projective normalization of P2 in K; L = Phi^*O(1). Then the general smooth member of |L| cannot have genus one, all degrees, singular Ybar allowed. Mechanism: reflexive adjunction gives omega_Ybar = L^(-1); restricting to the affine normalization Y = Spec B over A = C[f,g] gives Hom_A(B,A) free over B, against the accepted BD-GAL section 2 nonfree relative dual.

Accepted, not re-hardened: the H1(Ybar,O)=0 trace/Leray bridge and the promoted genus-zero exclusion (predecessor gate A, B); the BD-GAL sandwich A2 --g1 etale quasi-finite--> Y=Spec B --g2 finite flat--> A2 with B the integral closure of A in K, and its section 2 nonfree Hom_A(B,A). The predecessor's all-line affine ramification counts are not used anywhere below.

## 2. Verdicts A–F

### A. CM, reflexive dualizing sheaf, H1(omega)=0, good |L| member: CONFIRMED

Normal means R1 and S2. On a two-dimensional scheme S2 forces depth 2 at every closed point, so every closed local ring is CM; height-one local rings are regular by R1; the generic point is a field. Hence Ybar is CM and equidimensional of dimension 2, projective over C. Such a scheme has a dualizing sheaf omega (Hartshorne III.7 sense, equal to H^(-2) of the dualizing complex), and on a CM scheme it is maximal CM. A maximal CM module over an integral CM local ring has associated primes among the minimal primes, so omega is torsion-free of rank one; torsion-free plus S2 on a normal integral scheme is reflexive. Serre duality for projective CM equidimensional X and the locally free sheaf O gives H1(X,omega) dual to H1(X,O), hence zero. Every hypothesis (projective, CM, equidimensional, F locally free) is met; invertibility of omega is nowhere assumed.

General member: L is base-point free and ample as the pullback of O(1) under a finite morphism. For a point p the members through p form a hyperplane of |L| (evaluation at p is onto the fibre), so a general member avoids the finite set Sing(Ybar). Bertini in characteristic zero on the smooth open gives smoothness; Jouanolou-Bertini irreducibility for the complete-series morphism, whose image is a surface, gives irreducibility, hence connectedness. So a smooth connected C in |L| disjoint from Sing exists, and under the hypothesis it has genus one. No gap.

### B. Adjunction sequence with noninvertible omega; lifting: CONFIRMED

Let s be the section of L defining C. Multiplication by s, omega -> omega tensor L, is injective because omega is torsion-free and s is nonzero. Let U = Ybar minus Sing (open, contains C, smooth) and V = Ybar minus C (open). On U the sequence 0 -> omega_U -> omega_U(C) -> i_*omega_C -> 0 is ordinary smooth Cartier adjunction, exact. On V the section s is a unit of L, the first map is an isomorphism, and i_*omega_C is zero, so the sequence is exact there. U and V cover Ybar, including every singular point. The cokernel of the first map is supported on C, which lies inside U, so it is determined by its restriction to U and equals i_*omega_C globally; the residue map is therefore globally defined. No skyscraper at a singular point is possible: at such a point s is a unit. Exactness is local, so the global sequence is exact.

Lifting: H0(omega tensor L) -> H0(omega_C) -> H1(omega) = 0 by A, so restriction is onto. On a smooth connected genus-one curve h0(omega_C)=1 and deg omega_C = 0, so a nonzero regular differential eta has an effective zero divisor of degree zero, i.e. no zeros. A preimage sigma of eta is a nonzero global section of the rank-one reflexive sheaf F = omega tensor L. No gap.

### C. Effective Weil divisor, zero intersection, reflexive extension: CONFIRMED

At every codimension-one point Ybar is regular, F is invertible, and sigma has a well-defined order there, nonnegative because sigma is a regular section. Finitely many prime divisors carry positive order (sigma is nonzero on the integral surface), so Z = div(sigma) is an effective Weil divisor with class K+L in Cl(Ybar).

Intersection without Q-Cartier: for an ample Cartier L and an effective Weil Z, L.Z := sum n_D deg(L|_D) is strictly positive unless Z=0, since every integral curve D has deg(L|_D) > 0. To compute L.Z one needs only that c_1(L) acting on 1-cycles descends to rational equivalence (Fulton, Chapter 2) and that for the Cartier divisor C not containing any component of Z, c_1(O(C)) cap [Z] is the intersection cycle C.Z, which is supported inside U where Z is Cartier. There deg = deg(O_U(Z)|_C) = deg(F|_C) = deg(omega_C) = 0 by the adjunction isomorphism F|_C = omega_C of B. So L.Z = 0 and Z = 0. The class K is never treated as Q-Cartier; only the Weil divisor Z of a section of a reflexive sheaf is intersected with the Cartier C.

Alternative zero-locus argument, verified: if Z had a component D, then deg(L|_D) > 0 forces D to meet C at some point p, which lies in the smooth open U. Near p, F is invertible and sigma lies in I_D F_p, so sigma(p) = 0 in the fibre and hence eta(p) = sigma|_C(p) = 0, contradicting that eta is nowhere zero. This uses nothing but ampleness on curves and the smoothness of Ybar along C. Both routes agree.

Extension: sigma: O -> F is an isomorphism at the generic point and at every codimension-one point (order zero means sigma generates the local invertible F). Its failure locus is a finite set T. Both O and F are reflexive on the normal integral Ybar, so each equals j_* of its restriction to Ybar minus T (Hartshorne, Stable reflexive sheaves, Prop. 1.6, complement of codimension at least 2). Applying j_* to the isomorphism on the big open gives the global isomorphism O = F. The producer correctly distinguishes this from a point ideal, which is torsion-free but not reflexive and would not extend. Hence omega tensor L = O, so omega = L^(-1), invertible; Gorensteinness is a consequence. Elliptic-cone sanity check done by hand: the projective cone over an elliptic normal curve has H1(O)=0 (the Leray edge map into R^1 is injective), a smooth genus-one hyperplane section off the vertex, and omega = O(-1) = L^(-1), consistent with the lemma at a non-rational singularity. No gap.

### D. Same affine normalization, trivialized L, finite duality, FREE dual: CONFIRMED (one load-bearing import named)

Identification of the model: normalization of P2 in K restricted over the chart A2 = Spec A is Spec of the integral closure of A in K, which is BD-GAL's B (finite over A, normal, fraction field K). So Ybar over the chart is literally Y = Spec B and Phi there is g2; no resolution or replacement model enters.

Trivialization: the section of O(1) cutting the target line at infinity is nowhere zero on A2, so its pullback is a nowhere-zero section of L on Y = Phi^(-1)(A2). Hence L|_Y = O_Y and, from C, omega_Ybar|_Y = O_Y.

Finite duality: A is regular of dimension two with omega_A = A df dg free; B is CM (normal surface) and finite over A, hence maximal CM over A, hence locally free over A (also supplied by the accepted finite flatness). Therefore RHom_A(B,A) = Hom_A(B,A) in degree zero, and g2^!(O_A[2]) = Hom_A(B,A)[2], with B acting through the first argument. Changing the generator of omega_A changes nothing up to B-isomorphism.

The one point a hostile reader must insist on: a dualizing module of a NON-local CM ring is unique only up to tensoring with an invertible module, and BD-GAL itself warns that an invertible nonfree dual is not forbidden; Cl(Y) is infinite, so the ambiguity is not vacuous. The producer's "the dualizing complex of B" is only correct because the chain is canonical: omega_Ybar = H^(-2)(pi^! C) for the projective structure map; upper shriek restricts to opens, so its restriction to Y is H^(-2)(pi_Y^! C); pi_Y = pi_A2 o g2 gives pi_Y^! = g2^! pi_A2^!; and pi_A2^! C = O_A[2]. Every arrow is the standard functoriality of upper shriek for separated finite-type morphisms (composition and open restriction). With that import, the module whose triviality C proves IS Hom_A(B,A) as a B-module, not a twist of it. The producer states the conclusion correctly but does not spell out this canonicity; I record it as the load-bearing import rather than a gap, since it is a named standard theorem and no alternative reading survives it.

Match with BD-GAL: section 2 states that omega_(B_K/A) = Hom_A(B_K,A) is not a free B_K-module, same A = C[f,g], same B, same module, same action; free of rank one means isomorphic to B. The trivialization gives exactly Hom_A(B,A) = B. Contradiction, so genus one is impossible. No trace element, different generator, finite-resolution substitute or block-existence hypothesis is used; the statement is a conditional exclusion and is consistent with no block existing. Globality is genuine: C's isomorphism is on all of Ybar, so the restriction to Y is a global generator, not a local one. No gap.

### E. Controls: CONFIRMED (verified by hand)

Degree eight. Sym^2(P1) = P2 by the bidegree (1,1) forms [ac : ad+bc : bd], degree two, pullback O(1,1). Composed with [X:Y:Z] -> [X^2:Y^2:Z^2] (degree four, pullback O(2)) the composite is finite of degree eight with L = O(2,2), L^2 = 8, general member of genus (2-1)(2-1) = 1, H1(O)=0, omega = O(-2,-2) = L^(-1). Over the preimage of a target chart L is trivial, so the relative dual is free, exactly as the lemma predicts. It is a cover, not a source: the accepted nonfree dual is what bars it from the block role. No predecessor all-line count is used.

Elliptic ruled. X = E x P1, A of degree b >= 3 on E, L = A boxtimes O(1): very ample by Segre, H1(X,O) = 1 by Kunneth. With H = E x pt, F = pt x P1: L.F = 1 and L.H = b give L = H + bF; K_X = pr_2^*O(-2) = -2H; L^2 = 2b; (K+L).L = (-H+bF).(H+bF) = 0, so a smooth connected section has genus one. H0(omega tensor L) = H0(E,A) tensor H0(P1,O(-1)) = 0 by Kunneth, so no lift exists; consistent with H1(omega) = 1 obstructing. Finite net: embed by L in P^N; a general linear space of dimension N-3 misses the surface (dimension sum N-1 < N); projection from it is a morphism given by a base-point-free net inside |L|, pulls back O(1) to L, contracts no curve since L is ample, so it is finite and, having two-dimensional closed image, surjective onto P2. Existence is established without coefficients. The source-side H1 bridge would contradict H1 = 1, so this surface cannot be a block landing; the control shows H1(O)=0 is essential and source-supplied. Both controls are correct and meaningful; neither is a source.

### F. Composition and scope: CONFIRMED, no stronger reading proved

With the promoted genus-zero theorem, every actual proper-block finite normal projective landing has sectional genus at least two. This is a necessary condition on actual proper intermediate fields only. Not proved and not claimed, correctly: any genus >= 2 exclusion (deg omega_C = 2g-2 > 0 leaves Z free to be nonzero, so the mechanism has no purchase); any full-field K = C(x,y) or no-block statement (BD-GAL's nonfree dual is stated for proper K, and the charge excludes the full field); primitive/nonprimitive monodromy; any first-leg degree restriction; nonrationality of Ybar (rational surfaces carry genus >= 2 ample sections, e.g. plane quartics); nonexistence of finite genus-one covers of P2 (refuted by the degree-eight control); JC2. Genuine proof gap: none found. The only item short of fully explicit is the canonicity import named in D.

## 3. Summary verdict

- A CONFIRMED. B CONFIRMED. C CONFIRMED. D CONFIRMED with the named upper-shriek functoriality import closing the invertible-twist loophole. E CONFIRMED. F CONFIRMED.
- Overall: the reflexive-adjunction argument holds against the exact accepted H1 bridge and the exact BD-GAL section 2 nonfree dual. No REFUTED item, no GAP. Result remains MANUAL/PROVISIONAL; promotion, custody and terminal receipt belong to ROOT. No descendants launched.
- Writes: this report only; skeleton replaced by write 1, write 2 appended, postpin rows appended from sha256sum output, marker appended last. No artifact_finalize, no charge_basis (no exit-price assertion is made), no seal.

## 4. Postpins (generated from sha256sum after the review text was written)

648861914149486b54c6852f8d606a366d34fe82c93f4138b09116c318465a11  postpin genus-one-block-landing-astra-20260912.md
cc1eaca421d769e576ef454780421b88a7fceb30c3bb87f7c386ccb0dd25a59b  postpin genus-zero-block-landing-gate-fable5-20260912.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8  postpin block-descent-galois-coordinator-integration-sol56-20260830.md
- postpin_utc=2026-09-12T06:57:15Z

<!-- BODY-END -->
