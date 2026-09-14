# Hostile gate: Mellin rank and annihilator-selection controls (Fable5.1)

tag: bass-mellin-selection-gate-fable5-20260911
reviewer: Fable5.1 (independent, different-model; no deference to Astra or ROOT)
opened_utc: 2026-09-11T22:18:44Z
deadline: reserve 22:35Z, HARD 22:38Z, 2026-09-11 (no extension)
method: documentary manual mathematics only; hash, text and PDF-to-stdout reads; no code, CAS, network, Git, or live artifacts

## 0. Custody (prepins, freshly hashed before reading)

All five snapshots in the lane inputs directory hashed with sha256sum before any read; every digest equals the expected pin by basename:

- keller-mellin-rank-astra-20260911.md 180c9a64c98d8cf89e791fabd9f4d1ac690c33128235b073875a25475651e8e1 (read WHOLE)
- bass-nonmonic-control-root-20260911.md 80a1ce08a20b880516779d6722bfd0133a437f0e3922f5806c92efe772fef312 (read WHOLE)
- bass-rankone-selection-root-20260911.md 79a4cdc51503d81365df572d56b0b7e1c5c1ccf8d9e81edbc7343d28d2621582 (read WHOLE)
- bbkp-v2.pdf 91f0760061245ccb930c5cd431534fc17bf28284d65b2edf680d0676be91a94e (pdftotext pages 20–22 to stdout)
- loeser-sabbah-corrected.pdf 0a9791aaea66156c2bfa88b7c12c59595c5dbe05cbfcf2b4575395e75854a48f (pdftotext pages 5–6 to stdout; printed pp.1263–1264)

Read-scope limits. LS p.1263 statement of Théorème 2(1), "χ((G_m)^p, M) = dim_{C(s)} M(s)" for a holonomic D-module M on (G_m)^p, is legible and is the charged statement. The p.1264 proof of point 1 has its displayed formulas dropped by OCR (the hypersurface {b=0} base change and the recursion display are blank). I do not reconstruct that proof: the full LS proof of Théorème 2(1) is EXTERNALLY TRUSTED. BBKP pp.20–22 are legible: Theorem 35, its torus reduction, (3.5)–(3.7), Proposition 36 and Corollary 37 with footnote 16. Appendix B was not in scope and is not adjudicated.

## A. Actual Keller rank attachment — CONFIRMED (conditional on named externals)

Setup as charged: F=(p,q):X=A^2→Y=A^2 with nonzero constant Jacobian, A=C[p,q]⊂R=C[x,y], N=R/A, B=C[e_p,e_q] with e_p=p∂_p, e_q=q∂_q acting through the lifted derivations, E=Frac(B).

Direct image without properness. F is étale, so the differentials dp,dq form a basis of Ω^1_X and the transfer bimodule D_{X→Y}=O_X⊗F^{-1}D_Y is free of rank one over D_X. Hence D_{Y←X}⊗^L_{D_X}O_X is O_X concentrated in degree zero with the lifted connection, and no relative-dimension shift arises. F is affine, so F_* is exact on quasi-coherent sheaves. Therefore F_+O_X=F_*O_X=R in degree zero with D_Y acting by the lifted ∂_p,∂_q. No finiteness or properness is used; only étaleness and affineness. Holonomicity of F_+O_X is external premise (i) (direct image preserves holonomicity for any morphism of smooth varieties). Astra's statement is exact.

Torus localization. T={pq≠0}, X_T=F^{-1}(T), R[1/(pq)]=O(X_T), which is the localization ι^*R and is holonomic. The reduction dim_E(E⊗_B R)=dim_E(E⊗_B R[1/pq]) is BBKP's Theorem 35 step; I rechecked its inverse: from ∂_i x_i=1+θ_i and x_i(1+θ_i)=θ_i x_i, the element (1+θ_i)^{-1}∂_i is a two-sided inverse of x_i on E⊗_B(−). Correct.

Shift and sign. BBKP (3.6) places r-forms in degree r−N and (3.10) carries (−1)^N. Because F is étale, Ω^•_T⊗F_*O_{X_T} is F_*Ω^•_{X_T} with the ordinary de Rham differential, so χ(DR)=Σ_r(−1)^{r−2}dim H^r_dR(X_T)=χ_dR(X_T). At N=2 the shift is sign-neutral, so the value is (+1)χ(X_T) under either the shifted or the unshifted convention; Astra's "(+1)χ(X_T), not its negative" is correct and is convention-independent here. Grothendieck comparison (external (iii)) turns χ_dR into the topological χ.

Torsion of A. Each monomial p^i q^j is a common eigenvector of e_p,e_q, so a finite product ∏(e_p−i) kills any polynomial: A is B-torsion and E⊗_B A=0. E is flat over the commutative domain B, so E⊗_B N≅E⊗_B R. Correct.

Inclusion–exclusion. X_T=X∖({p=0}∪{q=0}); for complex algebraic varieties χ=χ_c, and χ_c is additive, so rank_B N=χ(X_T)=1−χ(p=0)−χ(q=0)+#({p=0}∩{q=0}). The intersection is F^{-1}(0,0), finite by quasi-finiteness and reduced by étaleness, so the count is a plain point count. Correct.

Controls and caveats. Identity map: R=A, N=0, χ((C^*)^2)=0; consistent, and χ(X)=1 in place of χ(X_T) would fail this control, as Astra notes. Generic translated origin: over a dense open of Y the map is finite étale of degree d=[C(x,y):C(p,q)], but translating (p,q) changes e_p,e_q to (p−a)∂_p,(q−b)∂_q and the curves to {p=a},{q=b}; Astra correctly states that curves and operators translate together and that this is not rank invariance. No rank-vanishing inference is drawn; Astra's remark that rank 0 with stipulated B-torsion-freeness would force N=0 is a conditional, flagged as a further source problem. LS rank-one classification (Thm 2(2), Remark 1) is not imported. Bass B-torsion-freeness is stipulated, not audited, and the rank formula itself does not use it.

Externals for A, all named and none reproved here: corrected LS Théorème 2(1) (statement charged, proof externally trusted); holonomic direct image; algebraic de Rham comparison plus additivity of χ. Verdict: CONFIRMED as a conditional source attachment.

## B. Astra rank-2 control — CONFIRMED

Commutators. With δ=p∂_q: δe_p=p^2∂_p∂_q=(e_p−1)δ and δe_q=δ+pq∂_q^2=(e_q+1)δ. So σ(e_p)=e_p−1, σ(e_q)=e_q+1; with z=e_p, t=e_p+e_q one has σ(z)=z−1, σ(t)=t. In the (p,q)-graded Weyl algebra the degree-(k,−k) component is Bδ^k for k≥0, so U=⊕Bδ^k is the Ore extension B[δ;σ]. Correct.

Module. δ(b_1v_1+b_2v_2):=σ(b_1)v_2+σ(b_2)zv_1 is σ-semilinear, hence a left U-module structure; B-free of rank 2, so torsion-free with dim_E(E⊗M)=2. U-torsion: m,δm,δ^2m are E-dependent, and left coefficients can be cleared to B, giving a nonzero Ore annihilator valid in M by injectivity of M→E⊗M; (δ^2−z)v_1=0 is an instance. Localized δ has semilinear matrix [[0,z],[1,0]] of determinant −z≠0 and σ is an automorphism of E, so δ is bijective on E⊗M. Correct.

No stable line, for every vector. Ev_1 and Ev_2 are not stable. Any other line is E(av_1+v_2) with a∈E^*; stability forces λ=σ(a) and aσ(a)=z. Over C(t), translation z↦z−1 preserves deg_z, so the left side has even degree and z has degree 1: contradiction, with all poles and zeros of a included. This argument is not about v_1: any nonzero m∈M with (b_1δ+b_0)m=0 and b_1≠0 makes Em a stable line in E⊗M, and b_1=0 contradicts torsion-freeness. So no nonzero vector of M has a first-order relation. Positive control: δv_2=v_1 gives aσ(a)=1, solved by a=±1, so E(v_1±v_2) are stable; the odd-degree multiplier is load-bearing. Limitations correctly stated: M is a difference module only, not a Weyl or Keller module, and it refutes exactly the inference "torsion-free + U-torsion + finite Mellin rank ⇒ first-order relation".

## C. ROOT nonmonic control — CONFIRMED

h=q(p+q), f=(1−h)^{1/2} with constant term 1 in C[[p,q]], algebraic. Nonpolynomial: p=0 would give a polynomial square root of 1−q^2, which has simple roots. T=(p+2q)∂_p−q∂_q gives T(h)=(p+2q)q−q(p+2q)=0, and 2f·Tf=T(1−h)=0 with f a unit, so Tf=0.

Recomputation of Φ=δT: p∂_q(p+2q)∂_p=2p∂_p+p(p+2q)∂_p∂_q and −p∂_q q∂_q=−p∂_q−pq∂_q^2. Now 2e_p(e_q+1)=2p∂_p+2pq∂_p∂_q, δe_p=p^2∂_p∂_q, δe_q=p∂_q+pq∂_q^2, so Φ=2e_p(e_q+1)+δ(e_p−e_q) exactly, and Φf=δ(Tf)=0. Composition orders check; T itself is outside U because of 2q∂_p, as ROOT says.

Left normalization. From (e_q+1)δ=δe_q one gets (e_q+1)^{-1}δ=δe_q^{-1}, so [2(e_q+1)]^{-1}Φ=e_p+δ[(e_p−e_q)/(2e_q)]. The shift is exactly right; the coefficient is rational with denominator 2e_q, so the operator is in the r=0 slot of the family only with a nonpolynomial G. Correct.

Rejection on actual R. If p,q are a Keller pair and f∈R with f^2=1−q(p+q), the lifted derivations preserve R, and 2f∂_pf=−q, 2f∂_qf=−(p+2q) put q and p in fR; then 1=f^2+q(p+q)∈f^2R, so f is a unit of C[x,y], a constant, and q(p+q) would be constant, contradicting algebraic independence. Correct. Scope correctly limited: this rejects one control on actual R and does not prove the general selection theorem.

## D. ROOT rank-1 control — CONFIRMED

M=Ev, δ(bv)=σ(b)a(z)v with a=z(z−t−1)/(z−t/2−1). Semilinearity δ(b·cv)=σ(b)δ(cv) holds, so M is a U-module; E is B-torsion-free; δ(bv)=[σ(b)a/b](bv) with denominators cleared gives a first-order U-annihilator for every vector; rank 1; δ is bijective because σ is an automorphism and a≠0. Orientation check: a is exactly the multiplier making v a solution of the normalized operator of C, so the "orientation only" remark is consistent.

The claim, for every nonzero w=bv. Applying z−r+δH(z,t), H(z,t)=G(z,t−z)∈C[z,t], gives (z−r)+H(z−1,t)a(z)b(z−1)/b(z)=0 after dividing by b. Since b(z−1)/b(z)→1 at z=∞ over C(t) and a(z)∼z, the product has deg_z equal to deg_zH+1 exactly (degrees add for nonzero rational functions), so no higher term can cancel: deg_zH=0 and the leading coefficient forces H=−1, i.e. G=−1. Then b(z−1)/b(z)=(z−r)(z−t/2−1)/(z(z−t−1)). For any b∈C(t)(z)^*, ord_α b(z−1)=ord_{α−1}b(z), so the divisor of b(z−1)/b(z) telescopes to total multiplicity 0 on every orbit α+Z in the algebraic closure of C(t); nonlinear factors split there. On the right, r and 0 share an orbit and cancel in total (directly at r=0); t/2+1 and t+1 lie in distinct orbits from each other and from Z because t/2 and t/2+1 are not integers for transcendental t. The orbit of t/2+1 carries total multiplicity +1. No rational b exists.

Gauge. The choice of generator bv ranges over all nonzero vectors of M, so the obstruction is stated for every vector and survives any rational gauge; it is not the failure of one normalization. The claim is not that the formal-germ U-module equals M, and no Weyl, holonomic, finite-B or source realization is asserted. Correct.

## E. Composition and the homogeneous-lifting adjudication — CONFIRMED (lifting is discharged; no new OPEN)

Grading. Give p,q degree 1 and ∂_p,∂_q degree −1. Then e_p,e_q,δ=p∂_q all have total degree 0, so every element of U=B[δ;σ] preserves total (p,q)-degree; on C[[p,q]] it acts componentwise on homogeneous parts, and δ sends p^iq^j to j·p^{i+1}q^{j−1}.

Embedding. At a source point P with F(P)=0, étaleness makes p,q formal coordinates, so R↪O_{X,P}↪C[[p,q]] (localization of a domain, then Krull intersection). Write f∈R as Σ_d f_d with f_d homogeneous of degree d; each f_d is a polynomial in p,q and therefore an element of A⊂R.

Lifting. Suppose Φ∈U and Φf∈A, of degree D. Since Φ preserves degree, (Φf)_d=Φ(f_d), so Φ(f_d)=0 for all d>D. Put prefix=Σ_{d≤D}f_d∈A and tail=f−prefix. Then tail∈R (difference of two elements of R), tail≡f in N, and Φ(tail)=Σ_{d>D}Φ(f_d)=0 in C[[p,q]], hence in R by injectivity. The zero-RHS case Φf=0 works with any cutoff D≥0 (then Φ(prefix)=0 too). So the "correction by an element of A" that Astra §3 lists as separately required is supplied by the finite homogeneous prefix, for every U-relation. The lifting OPEN is not needed; I do not promote it.

What remains genuinely missing, and which neither the rank formula nor the two controls supply:

1. First-order selection: existence, for an actual nonzero Keller N, of a δ-stable E-line in E⊗_B N, equivalently (given stipulated torsion-freeness, clear denominators both ways) a nonzero class with some first-order U-relation. Control B shows finite rank alone does not give it.
2. Polynomial-G/resonant normalization: putting such a relation into the form e_p−r+δG(e_p,e_q) with integer r≥0 and polynomial G. Control D shows rank 1, torsion-freeness, U-torsion and invertible δ do not give it; control C shows a first-order relation on an algebraic germ can be nonmonic with a rational normalized coefficient.

Given 1 and 2 for a class [f], the lifted tail is an algebraic germ (x,y are algebraic over C(p,q)) killed by the family, so an algebraic-germ polynomiality theorem for that family would place tail in A and kill the class. That composition is only as strong as 1 and 2, which are absent. Astra's own statement that no such composition is available yet is correct; its lifting caveat is superseded by the prefix argument above.

## F. Verdict table, external scope, and non-claims

| Item | Verdict | Basis |
|---|---|---|
| A rank formula rank_B N=1−χ(p=0)−χ(q=0)+#F^{-1}(0) | CONFIRMED (conditional) | étale/affine direct image, torsion of A, flat localization, χ additivity; externals named below |
| A no-properness identification F_+O_X=R | CONFIRMED | D_{X→Y} free over D_X under étaleness; F affine |
| A sign at N=2 | CONFIRMED | (−1)^{r−2}=(−1)^r; convention-neutral |
| B rank-2 control, no first-order relation on any nonzero vector | CONFIRMED | aσ(a)=z parity; line argument applies to every m |
| C Φ=2e_p(e_q+1)+δ(e_p−e_q), Φf=0, left normalization | CONFIRMED | recomputed |
| C rejection on actual R | CONFIRMED | p,q∈fR ⇒ f unit ⇒ contradiction |
| D rank-1 control excludes the family on every vector | CONFIRMED | degree forces G=−1; orbit multiplicity +1 at t/2+1 |
| E lifting already discharged for U-relations | CONFIRMED | degree-0 prefix subtraction |
| E remaining missing steps | GAP (typed, pre-existing) | first-order selection; polynomial-G normalization |

External scope, stated plainly. The rank attachment in A is a conditional source attachment resting on: corrected LS Théorème 2(1) (statement read at p.1263; proof at p.1264 externally trusted because the OCR drops its displays), BBKP Theorem 35 as the affine restatement with its localization step (checked), holonomic direct image, and algebraic de Rham comparison with additivity of χ. Bass B-torsion-freeness of the actual N is stipulated, not freshly audited. By contrast, B, C, D and E are elementary and are confirmed outright; they depend on no external theorem.

Non-claims. No rank value or vanishing is asserted for any hypothetical noninvertible Keller map; no LS rank-one classification is imported; no claim that arbitrary rank has a line; the family is not expanded; no novelty or JC2 claim. The BBKP Appendix B remark in Astra §3 is outside this gate's read scope and non-load-bearing; nothing here promotes or certifies a full-paper error, and Astra itself states it is not a refutation of the rank theorem. No charge_basis line is declared; no exit-price assertion is made.

Timing. Substantive body completed before the 22:35Z reserve. Own whole readback and input postpins follow; the standalone marker is appended last and no edit follows it.

Postpins at 2026-09-11T22:24:32Z: all five input digests re-hashed after reading and identical to the prepins listed in section 0. Whole readback of this file completed at 22:24Z with no placeholder text remaining.

<!-- BODY-END -->
