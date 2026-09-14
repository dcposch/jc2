# Furter composition rigidity: independent primary-proof and interface gate

2026-09-07, Fable 5.1, bounded 30-minute review of the frozen packet. **Core contact theorem CONFIRMED by independent re-derivation. Consequences CONFIRMED at their stated scope modulo named imports. Campaign attachment: GAP at the first arrow. No JC2 proof or counterexample follows.**

## Verdict table

| # | Statement (producer numbering) | Verdict | Exact hypotheses / basis |
|---|---|---|---|
| 1 | Thm 1.2: ord_0(F−z) ≤ 1+Σ(deg f_i−1) | **CONFIRMED** | f_i ∈ C[z] nonconstant, F=f_s∘…∘f_1, F(0)=0, F'(0)=1, F≠z. Only F's normalization is used; actual degrees; distinct finite critical values. |
| 1' | Cor 1.3: R(m,n) for all m,n ≥ 1 | **CONFIRMED** | Indexing matches Furter p.2 (c_1=…=c_{m+n}=0 ⟺ a∘b−X = O(X^{m+n+2})). |
| 2 | Lemma 2.1: #attracting fixed points ≤ #CV(P) | **CONFIRMED** | deg P ≥ 2; self-contained; uses full basins only, no immediate-basin import. |
| 3 | Lemma 3.1: k ≤ #CV(f), perturbation proof | **CONFIRMED** | Identity (6) re-derived by hand and machine-checked; δ real, δ>0; k ≥ 1 including k=1. |
| 3' | Remark 3.3 petal sketch | IMPORTED, not load-bearing | Milnor §10 not charged; no defect found; Lemma 3.1 does not depend on it. |
| 4a | Remark 4.2 (char 0), Remark 4.3 (char p) | **CONFIRMED** | Embedding argument; a∘b = z−z^{p²} checked exactly for p=2,3,5. |
| 4b | Cor 5.1: R(m) | **CONFIRMED** | n ≥ 0 including n=0; converse R(m)⇒R(m,n) is Furter Lemma 2, p.7, imported. |
| 4c | Cor 6.1: C_{m,n} finite, flat, surjective, rank binom(m+n,m) | **CONFIRMED** | Given R(m,n), Furter Lemma 11 (v)⟺hsop (pp.15–16), and standard CM/hsop facts (Stanley I.5, BH 2.1). |
| 4d | Cor 6.2: sharpness with exact degrees m+1, n+1 | **CONFIRMED** | Uses surjectivity of 4c plus Thm 1.2. |
| 4e | Cor 7.2: length-two closure | **CONFIRMED conditional** | Furter Thm B (p.5) imported at its stated scope; order enumeration verified; one expository slip (below). |
| 4f | Cor 8.2: Strong Factorial on E^[m] | IMPORTED | EvdE14 Thm 2.25(5) not charged; restricted family only, not the full conjecture. |
| 5 | Attachment to the D125 source | **GAP** | First missing arrow: no source-derived one-variable composition identity exists; see §5. |

PDF versus Typst: the eight-page PDF (Typst 0.15.0, created 2026-09-07T04:19:18Z, matching the pinned commit time) agrees with the source in every statement, equation number (1)–(11), remark and reference.

## 1–3. Core proof audit (independently re-derived)

**Lemma 2.1.** Let p be attracting with 0<|λ|<1 and suppose B_p contains no critical point. B_p is open (union of preimages of a contracting disk) and bounded (escape radius R for deg ≥ 2). For D=D(p,ρ)⊂B_p, every point of P^{−n}(D) lies in B_p, so (P^n)' has no zero there. P^n: P^{−n}(D)→D is proper because P^n is proper on C; its restriction to a component U is still proper (U is clopen in P^{−n}(D)), has open and closed image, hence is a surjective proper local biholomorphism onto a simply connected disk, hence a biholomorphism. The component containing p gives u_n with u_n(p)=p and u_n'(p)=λ^{−n}; Cauchy on the circle of radius ρ/2 bounds |u_n'(p)| ≤ 2R/ρ, contradiction. Critical value P(ζ_p) ∈ B_p by forward invariance, and distinct fixed points have disjoint basins, so the map p ↦ P(ζ_p) is injective into CV(P). Every step verified; nothing about immediate basins is assumed.

**Lemma 3.1.** g_δ=(1+δ^k)f has the same critical points as f and CV(g_δ)=(1+δ^k)CV(f), so #CV is preserved. With z=δw the fixed-point equation divides exactly by δ^{k+1}w to give H(δ,w)=1+(1+δ^k)cw^k+δ(1+δ^k)w^{k+1}r(δw); H(0,w)=1+cw^k has k simple nonzero roots, so the implicit function theorem gives k distinct branches, and all k exist for every k ≥ 1 (k=1: the single root −1/c). Identity (6) is exact: expanding (k+1)(g_δ−z)/z and g_δ' and subtracting leaves 1+δ^k times the common bracket. At z_j(δ)=O(δ) the residual term is O(δ^{k+1}), so g_δ'(z_j)=1−kδ^k+O(δ^{k+1}) uniformly over the k branches; for real δ>0 with kδ^k<1 and Cδ<k/2 the modulus is below 1. The sign −kδ^k is right (the origin has multiplier 1+δ^k>1 and is repelling). No double counting: the k branches are distinct from each other and from 0. Lemma 2.1 applies since deg g_δ = deg f ≥ k+1 ≥ 2.

**Theorem 1.2.** k=ord_0(F−z)−1 ≥ 1. Chain rule: CV(a∘b) ⊆ CV(a) ∪ a(CV(b)), so #CV(F) ≤ Σ#CV(f_i) ≤ Σ(deg f_i−1); affine factors contribute 0 on both sides and the inclusion still holds. Only finite critical values are used anywhere; multiplicities are never counted. The factors need not fix 0 and may have any degree; the bound uses actual degrees, so for R(m,n) with a_m or b_n possibly zero the inequality only tightens. Cor 1.3: m+n+2 ≤ ord ≤ deg a+deg b−1 ≤ m+n+1 is a contradiction, so a∘b=z, degrees multiply to 1, normalization gives a=b=z. Sharpness (Remark 4.1) a∘b−z=−dz^{2d−1}+O(z^{3d−2}) checked exactly.

No false step found: the argument is Fatou's critical-point theorem plus subadditivity of critical values under composition.

## 4. Consequences

**Cor 5.1.** a^{−1}−b=O(z^{m+n+2}) with b the truncation; substitution into the polynomial a preserves the order; n ≥ 1 uses Cor 1.3, n=0 uses deg a ≤ m+1. Matches Furter's R(m) (p.3). The converse imports Furter Lemma 2 (p.7), read and correct.

**Cor 6.1.** R(m,n) says the only common zero of c_1,…,c_M is the origin. Furter Lemma 11 (v)⟺(i)⟺(vii)⟺(viii) (pp.15–16, ambient K algebraically closed, positive weights) turns this into hsop, finite, free, flat; Cor 12 (p.16) gives surjectivity. The producer's graded-Nakayama and Hilbert-series argument is also correct (a hsop in the Cohen–Macaulay ring S is a regular sequence; equal Hilbert series make the surjection from the free T-module an isomorphism; rank H_B(1)=M!/(m!n!)). The generic fibre statement uses only char 0 separability.

**Cor 6.2.** Surjectivity gives a∘b=z+z^{M+1}+O(z^{M+2}); Thm 1.2 forces deg a+deg b ≥ M+2, so both degrees are maximal. Correct.

**Cor 7.2.** The order is Furter's Definition p.5 (relations i–iii, merged entry d_j+d_{j+1}−1 is the smaller element, consistent with the Nagata example (3) ⪯ (2,2) on p.5). Elements below (d_1,d_2): ∅; (u,v) with 2 ≤ u ≤ d_1, 2 ≤ v ≤ d_2; (s) with 2 ≤ s ≤ d_1+d_2−1. The producer's invariant "sum minus length is non-increasing" is right and closes the enumeration. Theorem 7.1 is Furter Theorem B verbatim (p.5; proof pp.20–23 not replayed here, EXTERNAL-THEOREM at that scope). Closures: Furter takes closures in G, locally closed in E=C[X,Y]² (pp.3–4); the producer's "closure in G_{≤ d_1⋯d_l}" is equivalent because G_{≤N} is closed in G. Correction: the producer's Section 7 defines the multidegree from any word a_0∘b_1∘a_1∘…∘b_l∘a_l with b_j ∈ B∖A but omits Furter's reducedness condition a_i ∉ B for interior i (p.4); without it the sequence is not well defined (b_1∘id∘b_2 ∈ B). This is an expository slip only; the corollary consumes Furter's definition through Theorem B. The identification with the LPS19 Polydegree Conjecture "in their notation" is unverified here (LPS19 not charged).

**Cor 8.2.** Purely imported: EvdE14 Theorem 2.25(5) is not in the packet. Even if correct, it is the E^[m] family, not the Strong Factorial Conjecture.

## 5. Campaign interface: GAP

Client read: full14c ring N over E=Q[k,k^{−1}] with zk−1, the rank-six cover O_0 ≅ N ⊗_E Q[ℓ,ℓ^{−1}], k=ℓ^{−6}; the torsor S=U ∪ V glued by v=g^{−1}, u=g^4w+λ_2g²+λ_3g³, w=p+g, receiver f:S→A² with ramification divisor 2F, étale on U, quasi-finite by the monic fibre faces A(0,w), B(0,w) of degrees 15 and 25, with the open immersion S ⊂ N_target into the finite normalization and S=N_target unproved.

Every proved statement in the paper is about one polynomial in one variable composed with another (Thm 1.2, Cor 1.3, 5.1), the weighted coefficient map of that composition (Cor 6.1, 6.2), or closures of multidegree strata inside Aut(A²) (Cor 7.2). Checked candidates:

- **Forced high-contact composition.** Needs a source identity a∘b = z + O(z^{40}) with deg a=15, deg b=25 (bound 39). A(0,w) and B(0,w) are the two coordinates of the parametrized fibre curve w ↦ (A(0,w),B(0,w)); neither is composed with the other and neither is a compositional inverse of anything in the packet. No identity of the required form exists in any charged input. This is the FIRST missing arrow.
- **Properness / degeneration.** Furter Lemma 11 and Cor 6.1 give finiteness for weighted-homogeneous maps A^r → A^r that are hsops. The receiver f:S→A² is not a weighted map of affine spaces, and coefficient-map finiteness is not Keller-map properness. Nothing in the paper mentions normalizations, boundary curves, or S=N_target.
- **Automorphism polydegree.** A guarded full source point would be a Keller map that is not known to be an automorphism; it has no multidegree, and Cor 7.2 describes closures inside G, not limits in E leaving G. No attachment.
- **Cover / guard.** The Kummer cover T^6=k^{−1} and zk−1 are untouched by anything here.

Attachment status: NONE. No ring, coordinate or place map can be written because there is no composition in the client. No NEXT discriminator is licensed from this paper; the campaign's missing arrow (S=N_target or another exclusion) is unchanged.

## Controls run

One stdlib script, exact rationals, factor degrees ≤ 5, caps 30 s wall / 25 s CPU / 512 MiB, run normally and with -O with byte-identical output, zero Assert nodes. Positive checks (21): identity (6) and equation (5) for k=1,2,3 with generic r; Remark 4.1 for d=2..5; Remark 4.3 for p=2,3,5, the same pair attaining exactly 2p−1 in char 0. Changed-object negatives (14, all fail as expected): coefficient −(k+1)δ^k and sign +kδ^k in (6); a mutated H in (5); b=z+z^d in Remark 4.1. No CAS, solver, numeric root-finding, or census; the verdict on Lemmas 2.1 and 3.1 is desk proof.

## Custody

| File | Class | SHA-256 |
|---|---|---|
| campaign-approaches-0731.md | charged | `40783391db0780cab406e51d5e2deb42bc007a002b92258394a1520199bb039d` |
| campaign-moving-face-14c.md | charged | `19f0394c2ec97797d325afa234d57c598a94bd2d83cbfe1dd24bda52db0f45cc` |
| campaign-torsor.md | charged | `7beff9e113580e22aba68f79811ed45f2023e195f7998a51cd224163a775db5a` |
| furter-original-author.pdf | charged | `957fbaa09bf2158217905b5d43b313d97401f43be3ee362fd112de1e62186a7f` |
| furter-original-author.txt | charged | `56500fb7e191fb5a0ffa165cb5ba427c11407aad3839656f04fbb0bfd051a2fa` |
| input-pins.json | charged | `3efdcac76996fe011489bf509697ee05eb36610fd2d7891eee58bff57a1a207e` |
| producer-proof.pdf | charged | `0e9662c12bba4204c12ce6e1a2140687d138d33a520f771320f87129879f445d` |
| producer-readme.md | charged | `5e8a5036962501e6f61d3d5c4435de53e72ba7a3b7d60aa86fe61e8fd9b1c460` |
| producer-refs.yml | charged | `8d7ba42d801e9c5604ec2d65d08bfa2752535f9ff0e7e9ea7671faedcd6b0a12` |
| producer-rigidity.typ | charged | `8a6e152c797c227529e88572db140fcfb5b6c3ad61650c2a94fc6304cb334af6` |
| scope-and-provenance.md | charged | `a69faa96b62a80708257fec2c1ee34e99fd39a24c584f7adeb6dbab64a1f6c34` |
| controls.py | own | `f4213fd136bc446e159692944844e76ce24d9d76f438af7b05153994b07986b5` |
| controls.normal.out | own | `7f79a81f1b487175ebcc70dc8c939f76ea0035ec28971e47b6dd987b84a3bf95` |
| controls.O.out | own | `7f79a81f1b487175ebcc70dc8c939f76ea0035ec28971e47b6dd987b84a3bf95` |
| producer-proof.pdftotext.txt | own | `a606b21225f52e5662fcfa83776b04f21638eca2f29400fe2f3b4acac3e39435` |
| furter-original.pdftotext.txt | own | `56500fb7e191fb5a0ffa165cb5ba427c11407aad3839656f04fbb0bfd051a2fa` |
| run-receipt.txt | own | `6499c486389645866c2e6d5ae71dd5bc15d40479f29ee924869fedc466d3ecde` |

The charged convenience text is byte-identical to my own pdftotext -layout extraction of the charged Furter PDF (same hash). Access holes: LPS19, EvdE14, Milnor, Fur97, EF04, Stanley, Bruns–Herzog, the JLMS version of Furter and the producer's X account were neither charged nor fetched. Furter Theorem B's proof (pp.20–23) was read only for interface, not replayed. All writers idle; evidence only in box/furter-primary-gate-fable5-20260907/.

<!-- BODY-END -->
