# Hostile gate: power-trace cutoff and trace-kernel splitting

tag: keller-trace-shortcuts-gate-fable5-20260911
reviewer: Fable5.1 (independent different-model gate of Astra mathematics)
skeleton_written_utc: 2026-09-11T20:48:06Z
hard_deadline_utc: 2026-09-11T21:05:00Z (no extension)

## Inputs and scope

Pre-pins matched at 20:48:16Z; all three files read WHOLE from /tmp/jc2-lane.jZEGa6/inputs.

- keller-trace-powers-astra-20260911.md bf94cc3ebf702f85a6971b80560ac3076d84e8873b74778c645333cf173503f0
- keller-trace-kernel-astra-20260911.md 7d943729d2ff5b101e38e015df006ab596651e3fea3d4915bdf01d9b45b6b2bd
- keller-trace-image-root-20260911.md 76fa7291c32150f8728b704116fdc92171ad40bf4c468bddfb1f01e0bf55c025

TRACE-IC-1, theorem (T) with node specialization (6) and height-one fullness (2), is consumed at exact scope. Nothing from its Section 8 is used. The IC/normalization comparison and every holonomic duality fact in the kernel report are treated as stipulated hypotheses. No literature, code or live artifact was used.

## A. Power cutoff h_m — CONFIRMED

Expansion recomputed: h_m^k = sum_j C(k,j) u^((m+1)j-k) v^(-j). For 1<=k<=m+1 the j=0 term is a pure u-pole and each j>=1 term has u-exponent >= m+1-k >= 0. At k=m+2 the j=1 term is (m+2)/(uv); j=0 is pure and j>=2 has u-exponent >= m. So k=m+2 is the first failure. The criterion n/(u^a v^b) in B iff n in (u^a,v^b) is right: B=S[1/u]+S[1/v] is exactly the span of Laurent monomials not doubly negative. The numerator v+u^(m+1) is prime to u and v, so both divisorial pole orders are 1 for every m; what grows is the contact of v+u^(m+1)=0 with v=0.

Rank-N controls audited. In K^N the element (h_m,0,...,0) has Tr(h^k)=h_m^k for k>=1 and Tr(1)=N, componentwise pole orders (1,1); this is the control that refutes rank plus pole orders. The connected control K(a), a^N=u: T^N-u is Eisenstein at the prime u of the UFD S, hence irreducible, and Tr=N h_m^k. There the pole orders of h_m are 1 in K but N in the normalized valuations of K(a); the report does not claim otherwise. Both refute any cutoff C(N) or C(N, pole orders).

The true criterion is correctly separated: if Tr(h),...,Tr(h^N) lie in a Q-subalgebra A of K, Newton puts the characteristic coefficients in A, Cayley-Hamilton puts all Tr(h^k) in A and makes h integral over A; the converse holds for normal A with Frac(A)=K. B violates the ring axiom (1/u * 1/v not in B), which is exactly what the recurrence needs. No gap.

## B. Connected open and component idempotent — CONFIRMED

h^k = sum_j C(k,j) u^(2j-k) v^(k-2j); exponent sum 0, never doubly negative, so S[h] is inside B (B is an S-module). T=S[1/(uv)] is a domain of rank 1 with Tr=id, and 1/(uv) is not in B. One-branch Kummer: S[1/u][a]/(a^e-u) is free on a^i and etale (e a^(e-1) a unit); a^(-k) a^i = u^q a^r is diagonal iff e|k, so Tr(a^(-k)) = e u^(-k/e) when e|k and 0 otherwise; Tr(T_u)=S[1/u] by the free trace and Tr(f/e)=f. Both-branch: S[t]/(t^e-uv)[1/t] equals S[1/(uv)][t]/(t^e-uv) because t^e=uv; Eisenstein at u since uv is not in (u^2); Tr(t^(-e))=e/(uv) after e-1 vanishing traces. All identities verified.

Finite S-linear-combination argument audited. R tensor_A K is a domain of finite K-dimension, hence equals L, so by flatness R tensor_A S embeds in L_S := L tensor_K Frac(S), and Tr tensor id_S : T -> M tensor_A S = S*M = B (by (6)) is the restriction of the etale-algebra trace of L_S over Frac(S). Hence Tr(sum s_j tensor r_j) = sum s_j Tr(r_j) lies in B; no global idempotent is needed. If T = T_i x T' with uv a unit of T_i, then T_i is S-flat, so n_i = rank(T_i tensor Frac S) > 0 and Tr(eps_i/(uv)) = n_i/(uv), not in B: contradiction at the first trace. Caveat confirmed: eps_i must lie in the ordinary tensor product R tensor_A S. A decomposition of L_S, or of a henselized or completed fibre algebra, supplies no such element; T_u itself has uv invertible generically but not in T_u. Generic splitting is insufficient, and all-power tests on one element are strictly weaker than cluster disjointness.

## C. R cap K = A and Hom_A(M,R)=0 — CONFIRMED

(2): take a/b reduced with an irreducible ell dividing b. ell(P,Q) is nonconstant by algebraic independence; pick an irreducible factor g. F is etale, hence quasi-finite, so g=0 is not contracted and dominates the irreducible curve ell=0. Then v_g(b(P,Q)) >= 1 while v_g(a(P,Q)) = 0, since otherwise a vanishes on a dense subset of ell=0 and ell divides a. As v_g >= 0 on R, a/b is not in R. Only quasi-finiteness is used.

(3): M is a nonzero A-submodule of K, so M tensor_A K = K; phi tensor K is multiplication by r = phi_K(1) in L, and phi(m) = r m. Take ell dividing d, g as above, eta the generic point of ell=0. For s in A outside (ell), v_g(s(P,Q)) = 0 by the same density argument, so v_g >= 0 on R_eta = A_eta R. Accepted M_eta = K gives ell^(-n) in A_eta M, so r ell^(-n) lies in R_eta and v_g(r) - n v_g(ell(P,Q)) >= 0 for all n, forcing r=0. This kills every A-linear map M -> R, hence every A-linear and every W-linear section, assuming only that D is nonempty; properness is never presumed. Conversely, if D is empty then R is integral over the normal ring A, M=A, and m/N is a W-linear section. So a splitting of Tr is equivalent to properness, and any splitting premise is circular. No gap.

## D. Conditional cohomology — CONFIRMED as conditional

Stipulation used: H^j(L_i) = H^(j-1)(N_i), N_i the normalization of D_i. Since N_i is connected, H^0(L_D)=0, H^1(L_D)=C^c and H^2(L_D) = direct sum of H^1(N_i). From 0->A->M->L_D->0 and the Poincare lemma for A: H^0(M)=C, H^1(M)=C^c, H^2(M) = direct sum of H^1(N_i). Accepted (1), H^2(M)=0, then forces H^1(N_i)=0, consistent with A^1 normalizations; the H^1 count itself needs only connectedness, not the A^1 fact. From 0->E->R->M->0, with H^0(R)=C and H^1(R)=H^2(R)=0 because the delta-frame complex is the de Rham complex of C[x,y] (dp wedge dq = c dx wedge dy): H^0(R)->H^0(M) is multiplication by N, an isomorphism, so H^0(E)=H^1(E)=0 and the connecting map H^1(M)->H^2(E) is an isomorphism. Verified.

Obstruction: for h in E take d alpha = h dp wedge dq and beta = Tr(alpha), closed because Tr commutes with delta_p, delta_q. Changing alpha by db changes beta by d Tr(b); [beta]=0 iff a trace-zero primitive exists (lift m to b, replace alpha by alpha - db). This is the inverse of the connecting isomorphism. Verified.

Residues: beta_i = dd_i/d_i has coefficients in M by (T) and is closed. Res along D_j of beta_i is delta_ij, and Res of dm for rational m vanishes (the t^(-1) dt coefficient of d of a Laurent series is zero), so residue is well defined on H^1(M) and the c classes are independent; with dim H^1(M)=c they are a basis. e_i = delta_p b_i - delta_q a_i lies in E because the mixed partials of log d_i agree, and its class is the nonzero image of [beta_i]. Verified. The identity licenses nothing further: H^2(E)=0 iff c=0 iff properness, so it renames the goal rather than approaching it.

## E. Open-immersion control and duality — CONFIRMED

0->A->A[1/p]->H_p->0: every element of H_p is killed by a power of p while A[1/p] is a domain, so Hom_W(H_p,A[1/p])=0 (even Hom_A), no section exists, and B0 is a nonsplit length-two module under the stipulated simplicity of H_p. Dualizing with the stipulated exact duality and self-duality of A and H_p gives 0->H_p->D(B0)->A->0; D(B0) has p-torsion and B0 has none, so B0 is not self-dual although its generic trace pairing is the identity. This is the j_* versus j_! distinction, invisible to the rational pairing. The control has H^1_DR(B0)=C on dp/p, H^2=0 and trace kernel 0; it violates H^1(source)=0, so it does not instantiate (1) and refutes nothing about an A^2 source. Correctly scoped: it defeats only the inference from rational self-duality to a global self-duality or decomposition of a nonproper direct image.

## Strongest safe surviving scope

- Safe: (T) with (6) at exact scope; no rank-only or rank-plus-pole-order power cutoff exists; all-powers-of-one-element tests do not certify branch-cluster disjointness; R cap K = A; Hom_A(M,R)=0 exactly when D is nonempty; A- or W-splitting of Tr is equivalent to properness; conditionally H^2(E) is isomorphic to H^1(M) = C^c with the logarithmic residue basis; for a nonproper etale direct image j_* and j_! differ and rational trace self-duality yields no global self-duality or decomposition.
- Not licensed: H^2(E)=0, properness, any JC2 resolution or novelty. The IC comparison and the duality facts remain stipulated. No source-attached mixed coefficient certificate is supplied. The cluster contradiction is checked only in its ordinary-tensor idempotent form.
- GAPs: no logical gap in the charged deductions. Two hypotheses stay unverified by this gate: the IC/normalization de Rham comparison (D) and the regular-holonomic simplicity/self-duality inputs (E). Future trace, kernel or dynamical methods are not refuted.

## Custody

Own WHOLE readback of this file and postpins of all three inputs performed before the final marker; the postpin hashes must equal the three pre-pin values above. No charge_basis declaration; no exit-price claim. No artifact_finalize.

<!-- BODY-END -->
