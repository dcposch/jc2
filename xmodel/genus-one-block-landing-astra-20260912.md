# Genus-one finite block landings: reflexive adjunction and the nonfree dual

MANUAL / PRODUCER-CHECKED / UNPROMOTED. First actual action 2026-09-12 06:40:04 UTC; owned targets absent and the original three input pins matched. Original reserve 06:57 / HARD 07:00 UTC unchanged. No scientific execution, code, coefficients, worker, network, shared edit or protected-tree access. The fourth input, the terminal genus-zero FIRST gate, was separately authorized and pinned before reading; ROOT has now promoted that predecessor. No live review was consumed.

Exact claim: for a proper intermediate field C(f,g) strictly contained in K strictly contained in C(x,y) of a hypothetical complex plane Keller map, let Phi:Ybar->P2 be its finite NORMAL projective normalization and L=Phi^*O(1). A general smooth member of |L| cannot have genus one. This is an all-degree actual proper-block restriction, not nonexistence of finite genus-one covers. The new argument below does not require the genus-zero conclusion, a surface classification, rational singularities, prior Gorensteinness, or higher-degree log-canonicity bounds.

## 1. Source attachment and H1 bridge

The accepted BD-GAL factorization is A2 --g1--> Y=Spec B --g2--> A2=Spec A, with g1 dominant etale quasi-finite and g2 finite flat. Here A=C[f,g] is a polynomial ring and B is its normal integral closure in K. Normalization commutes with restriction to an open base chart. Thus Ybar over the chosen target A2 is this SAME Y, and Phi restricted there is g2; no resolution is substituted for the finite model.

For completeness the needed H1 bridge is reconstructed, although it is now independently accepted in the added gate, section A. The actual first leg yields a dominant rational map P2-->Ybar. Resolve its indeterminacy by point blowups Z->P2 to obtain a proper generically finite map Z->Ybar. Blowup invariance gives H1(Z,O)=0. In its Stein factorization Z->W->Ybar, the second arrow is finite of degree n>0 and the first has pushforward O_Z=O_W. On each normal affine base, field trace carries integral elements of O_W into O_Ybar: their traces are integral over the base and belong to its fraction field. Characteristic zero makes Tr/n a splitting of O_Ybar into the finite pushforward of O_W. Consequently

    H1(Ybar,O) injects into H1(W,O)
                 injects into H1(Z,O)=0.

The second arrow is only the low-degree Leray injection. No vanishing of a higher direct image, rational-singularity hypothesis or rationality classification of Ybar is used. This proves H1(Ybar,O)=0 directly from the actual source, independently of either sectional-genus conclusion.

## 2. Normal-surface adjunction really gives a global section

Here is the more general surface lemma used. Let X be a normal integral projective complex surface, L an ample globally generated line bundle, H1(X,O)=0, and C a smooth connected genus-one member of |L| disjoint from Sing(X). Then

    omega_X tensor L is isomorphic to O_X,
    hence omega_X is isomorphic to L^(-1).

Normality implies Serre S2. In dimension two S2 is Cohen--Macaulay at every local ring, including the closed points; dimension-one normal local rings are regular. A projective CM surface has a dualizing sheaf omega_X, a rank-one reflexive sheaf, and its dualizing complex is omega_X[2]. Serre duality therefore gives H1(X,omega_X) dual to H1(X,O_X), hence zero. These are CM duality statements, not an assumption that omega_X is invertible.

The Cartier divisor C is contained in the smooth locus. The sequence

    0 -> omega_X -> omega_X tensor L -> i_*omega_C -> 0

is exact. One can check it locally without assuming X Gorenstein: near C the surface is smooth, so this is ordinary Cartier adjunction; off C its defining section is a unit and the first map is an isomorphism. These opens cover X, including every singular point. The first map is multiplication by the section defining C. In particular no spurious skyscraper cokernel at a singular point has been omitted.

Since H1(omega_X)=0, the restriction H0(omega_X tensor L)->H0(omega_C) is surjective. A smooth connected genus-one curve has a nonzero regular differential eta with no zeros: its canonical bundle has degree zero and eta's effective zero divisor consequently has degree zero. Lift eta to a global section sigma of F=omega_X tensor L. This is a nonzero section of a rank-one reflexive sheaf, not a guessed rational differential.

In the present application, L is ample and globally generated because Phi is finite. Sing(Ybar) is finite. A general complete-series member avoids it by the finitely many proper vanishing conditions, is smooth by Bertini, and is connected (equivalently one can use Bertini irreducibility for the finite complete-series morphism). Thus the surface lemma's C is available under the hypothesized sectional genus one.

## 3. Zero Weil divisor implies reflexive trivialization

At every codimension-one point X is regular and F is locally free of rank one. The regular section sigma has nonnegative orders there, defining an effective Weil divisor Z. Its class is K_X+L. Intersecting a Weil divisor with the Cartier polarization L is defined even when K_X is not Q-Cartier. Because C lies in the smooth locus, adjunction gives

    L.Z = (K_X+L).L = deg(omega_C) = 0.

Every nonzero effective Weil divisor on a projective surface has strictly positive intersection with an ample Cartier divisor: each of its integral curve components has positive L-degree. Hence Z=0. Alternatively, sigma restricts to the nowhere-zero eta on C; any divisorial zero would meet the ample C and give a zero of eta in the smooth neighborhood of that intersection. This is the same contradiction without any Q-Cartier interpretation of K_X.

The map O_X->F given by sigma is an isomorphism at the generic point and every codimension-one point. Its possible failure locus has codimension at least two. Both O_X and F are reflexive on the normal surface; restricting to the complementary big open and applying reflexive extension j_* recovers each sheaf. The isomorphism therefore extends across the finite omitted set. This removes any possible purely codimension-two defect: a nonreflexive ideal of a point would not justify this step, but F is reflexive. Thus F is globally trivial, not merely numerically trivial or trivial away from singularities. Invertibility of omega_X, and hence Gorensteinness in this CM setting, is a CONSEQUENCE.

## 4. The actual affine dual is exactly the forbidden free module

Let ell be the target line complementary to Spec A. Its standard section trivializes O_P2(1) on that affine chart, so its pullback trivializes L on Y=Phi^(-1)(A2). Canonical sheaves restrict to open subschemes, and the surface lemma yields omega_Y isomorphic to O_Y.

For the actual finite map g2:Spec B->Spec A, finite duality identifies

    omega_B = Hom_A(B,omega_A).

Here A is regular of dimension two, with omega_A free, and B is CM of the same dimension. The accepted sandwich already supplies finite flatness. Equivalently, its finite locally free A-module structure makes RHom_A(B,omega_A[2]) equal to Hom_A(B,omega_A)[2], the dualizing complex of B. Choosing the usual generator of omega_A identifies the displayed module with Hom_A(B,A). This is an isomorphism of B-modules with its usual action, not merely an A-module dimension equality. No choice of trace element or generator of the different is assumed.

The global trivialization of omega_Y says precisely

    Hom_A(B,A) is isomorphic to B as a B-module.

BD-GAL section 2 explicitly forbids this FREE relative dual for an actual proper intermediate field. Its distinction matters: invertible but nonfree duals are not forbidden by that statement, whereas the present argument gives a free module on the whole actual affine normalization. This is the contradiction. No local complete-intersection assertion alone would suffice, and none is substituted for the global trivialization.

Therefore the actual finite normal projective block landing cannot have sectional genus one. Combined with the now separately promoted genus-zero theorem, any surviving actual proper-block landing has sectional genus at least two. This combined necessary condition does NOT exclude genus at least two, all proper blocks, primitive/nonprimitive monodromy, any first-leg degree, all rational surfaces or JC2.

## 5. Meaningful controls and exact limits

Finite genus-one covers certainly exist, even with H1=0. The symmetric quotient P1 times P1->Sym^2(P1)=P2 is a finite map of degree two, with hyperplane pullback O(1,1). Compose it with the degree-four target coordinate-square map. The composite has degree eight, L=O(2,2), and a general member has genus one. Here H1(O)=0 and omega=L^(-1), exactly as the surface lemma predicts. On the preimage of a target affine chart the relative dual is therefore free. This is a cover-side example, not a Keller pair or a proper-block source attachment; the accepted nonfree-dual condition explains why it cannot serve in that source role. No all-line component count from the predecessor reviewer is used.

Dropping H1 genuinely breaks the lifting argument, and an elliptic ruled control can be verified directly. Let E be a smooth elliptic curve, A a line bundle of degree b>=3 on E, and X=E times P1 with L=A external-tensor O_P1(1). This L is very ample (the product embeddings followed by Segre), and H1(X,O)=1. If H=E times {point} and F={point} times P1, then H^2=F^2=0, H.F=1, L has numerical class H+bF, and K_X=-2H. Thus L^2=2b and (K_X+L).L=0. A general smooth connected section has genus one by adjunction. But

    H0(X,omega_X tensor L)
      = H0(E,A) tensor H0(P1,O(-1)) = 0.

It is even a finite-cover control: embed X by L in P^N. A general linear center of dimension N-3 misses this surface, since its dimension sum with X is N-1. Projection from it gives a base-point-free three-section net and a morphism X->P2 with pullback O(1)=L. Ampleness forbids a contracted curve, so this projective map is finite and surjective. This establishes existence without enumerating any family or choosing coefficients. The surface is not dominated as required by the actual source: the trace/Leray argument would contradict its H1=1. Thus the H1 hypothesis is essential and source-supplied, not automatic for arbitrary finite covers.

Reflexivity control: absence of codimension-one zeros does not trivialize a general torsion-free rank-one sheaf; ideal sheaves of points illustrate the missing codimension-two condition. The proof uses the actual reflexive canonical sheaf. Singularity control: CM follows from normality in dimension two only; no analogous higher-dimensional normal-only assertion is made. Globality control: a local dual generator or numerical K+L=0 alone does not contradict BD-GAL; the lifted nowhere-divisorial-zero section and reflexive extension supply the required global generator. Genus control: for genus at least two, deg omega_C=2g-2>0, so the effective divisor need not vanish. The argument has no conclusion in that range.

Named standard imports retained: surface indeterminacy resolution and blowup H1 invariance; Stein factorization, finite trace and the low-degree Leray injection; normal implies S2, CM surface duality and reflexivity of the canonical sheaf; smooth Cartier adjunction, projective Serre duality, Bertini/connectedness; positive degree of an ample line bundle on a curve; reflexive extension across codimension two; finite duality. Their hypotheses have been attached explicitly above. No del Pezzo classification, local ramification-degree estimate, log-canonical theorem or rational-singularity vanishing is imported.

QUANTITY settled at producer tier: the exact genus-one exclusion for actual proper-block finite normal projective landings, via the global dual trivialization. No mathematical OPEN remains within this stated claim, subject to the named standard imports and accepted BD-GAL. CHEAPEST NEXT TEST: one different-model FIRST focused on the singular-surface adjunction/reflexive extension and the affine finite-dual identification; at most 15 minutes is an UNMEASURED review-planning estimate, not a runtime bound or authorization. ROOT retains promotion. No global novelty claim, constructed source point or runtime result is asserted.

## 6. Exact read scope and publication

Initial census: three frozen inputs. All matched before body access. BD-GAL and the own genus-zero report were freshly read WHOLE at 06:42 UTC, including seals. COORDINATION was reused WHOLE at its fresh matching pin: this same agent had read all 806 lines in four consecutive ranges during 05:51-05:53 UTC today. The separately authorized fourth input, the terminal genus-zero gate, was hashed at 06:42:37 before a fresh WHOLE read. Its accepted H1 bridge and ROOT-promoted genus-zero scope are available; the new genus-one argument remains producer-only. The review's unnecessary all-line ramification-component embellishment is expressly not imported. No receipt, linked provenance, excluded appendix, live peer report, coefficient artifact or other local body was opened.

PINS records all four input hashes and these read modes. Own report/PINS WHOLE readback, unchanged input postpins and own-target collision checks precede the standalone marker appended LAST; normal close/finalize and exact expected-manifest verification follow. Custody includes input and owned hashes but excludes its own self-hash. Earlier genus-zero, scroll and corrected-flow artifacts are immutable and untouched. This task produced text only and grants no downstream execution or further task authority.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13657`.
- Body SHA-256:
  `9cebaef19f7359386352d33913b857c074d2eb08b103a75eb96f8be391f7c5d2`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
