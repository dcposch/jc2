# Gate: F10 r1 four-band composition and finite-cover slice (hostile manual)

2026-09-09. Gate of the NEW/PROVISIONAL report f10-r1-four-band-weighted-composition-astra-20260909.md. Launch 18:26:06 UTC; controlling stop 18:45:00 UTC (earlier of the fixed cap and launch+20 min, never reset). ZERO mathematical subprocesses, CAS, scripts, emitted rows or matrices; manual algebra and documentary metadata only. Writes: this file and box/f10-r1-weighted-composition-gate-fable5-20260909/ only, via apply_patch.

Verdicts: A CONFIRMED, B CONFIRMED (no factor correction needed), C CONFIRMED, D CONFIRMED. Remaining doubts and wording repairs are in E; none is a formula defect.

## 0. Custody and read scope

All 13 charged inputs were hashed with sha256sum in /tmp/jc2-lane.bbKhyq/inputs before any read; every digest matched the ordered list, in order:

- d91b3e389aee3c1086737b58da9747408cc7a04a8e9bb22161c26f2ddda8147c composition report
- bf45d1f6b82aaac044fb76efdc701f1b3de5b7cdd6abc2251ba99941a0f14973 artifact.json
- a5ab487c4619742b6252e2503488eea4d6e927b58fd2821207cc85bcba7cf8d5 16r whole-mate
- ead39705189f7faf338bab7937488e96c3ddf296c9ba0eed328ea63442619fb7 17b producer
- 1708746e6d54d745b7a33df54dd339b197df7ec33b1a67c79877ab2429e6946e 17b gate
- 650127bc1c6d347223030f74a746fce959ab4ca3f50784ab2d5e999e283cc38b first producer
- 41a5698f17b36b2ce26de1716d512bb64c6fc839f695c21673aeae694dc78a57 first gate
- 3dc7a2503eff441b35745dd153a6b90a534dae63644b0afc3d6968799c9f559a second producer
- 2e6210104eff67c7bdb3d8038ba4b8455f2f580eca80bd3dd1dcdf3fbaaa738d second gate
- 440a66c3e51bc401d3133c49a12edb1894ee6503f43da86b25fb011723fc55a6 third producer
- d11175469b643e6dc119ca9c16f19856b132c7f6b585c5b495d1c6e3fbad213a third gate
- 879d6ab9e951c90aa72c46bde3685789290bd38a057025d320f7eb5deb418a41 fourth producer
- 005c9ce2e36d9c6521070707300028bd72062290fd5befbd5be5554cc1cf901d fourth gate

Artifact JSON: body_bytes 20761, body_sha256 12a3cf99230d8bd4394bc5d0cf4f02e11b7be54c55527754f58c92e080d243ab, closed 18:15:56Z, consistent with the printed Seal; documentary only, body not re-hashed (that would be a script).

Read WHOLE: the composition report (262 lines) and its artifact. Component reports were read only at these ranges (grep hits by line, then sed), NOT whole:

- 16r: lines 24-40; grep hits 12, 47, 51, 68-70, 130-151, 180-185, 205-228.
- 17b gate: grep hits 24-70, 86 (F,H,a,b; omega; Lambda; 17 slots; 8 coordinates; B reduced conditional on 17a). 17b producer: hash only.
- first producer: 7, 9, 43-49, 71-75, 101-150; first gate: 20-42, 50.
- second producer: 7, 33-57, 87-91, 110-175; second gate: 22-48.
- third gate: 20-46. Third producer: hash only (consumed through its correction gate, as instructed).
- fourth producer: 23-30, 79-91, 108, 169-212; fourth gate: line 20 only.

No other file, corpus, code, ledger, peer, process or network.

## A. Triangular composition: CONFIRMED

Own derivations, grading S:1, t:1, theta=t/S. For A-band S^i P(theta) and B-band S^j Q(theta) the bracket is S^(i+j-2)(i P Q_prime - j P_prime Q).

1. Slot inventory. E1 has S-degree at most 8, E0 at most 9 (16r line 151). [S^8]E1, [S^9]E0 are -q6, -q7 = 0 in Lambda (17b). That leaves 17 slots [S^0..S^7]E1, [S^0..S^8]E0. Bands remove [S^7]E1,[S^8]E0 (weight 8), [S^6]E1,[S^7]E0 (weight 7), [S^5]E1,[S^6]E0 (weight 6), [S^4]E1,[S^5]E0 (weight 5). Remaining 4+5 slots plus Psi3, Psi4 = 11 = 17-8+2. Coordinates 8-(2+2+1+1) = 2. Confirmed.
2. First band. Z=(d0,v1,k3) are exactly the weight-3 A coefficients; its two rows involve only Z and Lambda (first gate line 42), so u,v0,k2,k1,ell stay free. rho1 is [theta^0](4CV-7DU) (first producer (9)); rho(beta)=1 makes Y1 a kernel coordinate, not a gauge. Confirmed.
3. Second band. q=-u, l=v0-uF, k=k2 are the weight-2 A coefficients; N2 is built from C, D coefficients only, so it lies in Lambda; the inhomogeneous part is quadratic in Z with no k1 or ell (ell sits at Delta weights 2-5, k1 in A1 whose partner B8 is empty; second gate line 36). Substituting (3) therefore leaves N2 and its unit determinant unchanged; (4) is an affine change with the same unit. Confirmed.
4. Third band, own re-derivation. Weight-6 pairs (4,4),(3,5),(2,6),(1,7), target -2 theta^5 from -2S t^5. The (1,7) pair with A1 = S(y theta + k1), y = 1-u d0, contributes y(theta D_prime - 7D) + k1 D_prime; [theta^i](theta D_prime - 7D) = (i-7)D_i, so moving it right gives N_i = -W_i + (7-i) y D_i for i<=4 and the extra -2 at i=5. The corrected rule (1) is right; the printed shifted-index rule is wrong. theta^6 row: only the (4,4) pair reaches it, 16V4-12V4 = 4V4 with V4=[S^0]B_4; that is the 16r Euler row j=4 at S^0 (eigenvalue 4) with zero forcing, so it FORCES V4=0. V3=[S]B_3 is the beta gauge and never reaches theta^6. Line 22 is correct. c3 is ell-free because ell first enters Delta at weight 5 and the B bands used (D,J,K,V) are fixed at weights 9,8,7,6; c3 is k1-free because the rows are affine in k1 with k1-coefficient h3 in Lambda (k1 D_prime plus the linear mate response). The matrix [[lambda1,lambda0],[-h0,h1]] has det lambda1 h1 + lambda0 h0 = 1, so k1 = -lambda3(c3) and Psi3 = -h3,0 c3,1 + h3,1 c3,0 (sign included) are an invertible two-row transformation. Confirmed.
5. Fourth band. Acol = 8a-44FH/15+8F^3/15 and Bcol = 8aF/5-5H^2/3+4F^2H/15 lie in Lambda. Own partial check: ell enters the weight-5 equation only through the target -ell theta^4, so [S^1]B_2 = ell + 6F[S^0]B_3 + (ell-free), and the 8a V_2 term of the theta^1 row yields the leading 8a of Acol. With lambda_A Acol + lambda_B Bcol = 1 the matrix [[lambda_A,lambda_B],[Bcol,-Acol]] has det -1; hence ell = -lambda_A P - lambda_B Q and Psi4 = Bcol P - Acol Q (fourth producer (7)) are equivalent to the two rows, and after substituting ell the original rows equal lambda_B Psi4 and -lambda_A Psi4. The overall sign of Psi4 is immaterial. P,Q are the entire ell=0 rows after (3)-(5). Confirmed.
6. No circularity: (3) uses Lambda; (4) uses Lambda and Z; (5) uses Lambda, Z, U2; (6) uses all. No later variable enters an earlier map. The whole mate, beta=gamma=k(0)=0, both inverse-pole conditions (A by parametrization, B by the upper-row consequence) and omega = w s^8 f5 are transported by substitution, not dropped. The first-gate intermediate sign issue is moot: theta^7 U = (2/5) C T_prime - C_prime T is correct; own check with T = 4CV-7DU, T_prime = 10(C_prime V - D_prime U): (2/5) C T_prime = 4 C C_prime V - 4 C D_prime U and C_prime T = 4 C C_prime V - 7 C_prime D U, difference -(4 C D_prime - 7 C_prime D) U = theta^7 U.

## B. Scaling and target: CONFIRMED

Own recomputation with tau=st, U=su, Dcal=sd, Vcal=s^2 v, Kcal=s^3 k, E=s^3 ell, z=s^2. s^3[S t^3+(Sd-u)t^2+(1-ud+Sv)t+k] at t=tau/s equals S tau^3+(S Dcal-U)tau^2+(z-U Dcal+S Vcal)tau+Kcal, and s^3 Pi(S,tau/s) = z tau - U tau^2 + S tau^3 (16r lines 28-29): (10) confirmed. Partials: Ahat_S = s^3 A_S, Ahat_tau = s^2 A_t, Bhat_S = s^5 B_S, Bhat_tau = s^4 B_t, so [Ahat,Bhat] = s^7 [A,B]. Delta terms: 1 -> s^7; u t -> U s^5 tau; ell t Pi -> E tau Pihat; t Pi^2 -> tau Pihat^2. (11) confirmed, all signs and powers. Expanding -E tau Pihat - tau Pihat^2 gives -zE tau^2, (EU - z^2) tau^3, (-ES + 2zU) tau^4, -(U^2 + 2zS) tau^5, 2US tau^6, -S^2 tau^7; each is weight 9 under (13) and equals s^7 times the matching 16r Delta monomial at t=tau/s (all eight checked, e.g. -2S t^5 -> -2zS tau^5, (ell u - 1)t^3 -> (EU - z^2)tau^3). No z inverse anywhere.

Read-backs. Every A band scales as s^3 P(vartheta/s) and every B band as s^5 Q(vartheta/s), so 4CV-7DU scales by s^8 and its constant coefficient by exactly s^8. rho1 (first producer (9)) and rho2 (second producer (13), the homogeneous response 4a V^h_0 - 7b k, not the affine mate) are both constant coefficients, so x = s^8 Y1 and y = s^8 Y2 hold. The homogeneous weight-7 equation is form-invariant with qbar = sq = -U (each pair term scales by s^7 and -2q theta^6 becomes -2 qbar vartheta^6). Leading data: sF = v/w, s^2 H = 1/w, s^3 a = 1/w, s^5 b = 1/f5, and Dbar_i = s^(5-i) D_i lies in B because the leading equation is form-invariant (4 Cbar Dbar_prime - 7 Cbar_prime Dbar = -vartheta^7). Confirmed.

Homogeneity. The coefficient of S^i tau^j in Ahat has weight 4-i-j: first band 1, second 2, third 3 (z - U Dcal0 and Kcal1), fourth 4 (E). Bhat_j has weight 7-j from Bhat_5 = S^2 and the weight-preserving operators j - 3S d/dS. Jhat has weight 9; G_i weights 7,6,5; 8,7,6,5; 3,4; wt H0 = 9, wt H1 = 8, wt U = 2. Confirmed.

s^10 factors. Jhat = s^7 J at t = tau/s, so E1 rows scale by s^6 and E0 rows by s^7. Third band: hbar3,1 = s^3 h3,1, hbar3,0 = s^4 h3,0, cbar3,1 = s^6 c3,1, cbar3,0 = s^7 c3,0, so Phi3 = s^10 Psi3. Fourth: Abar = s^3 Acol, Bbar = s^4 Bcol (matching fourth producer (5), where Acol carries s^-3 and Bcol s^-4), so Phi4 = s^10 Psi4. Both claims are right; no factor correction is needed and neither row is discarded.

Injection. B[x,y,z] -> B[s,s^-1][Y1,Y2] with x -> s^8 Y1, y -> s^8 Y2, z -> s^2 sends the monomial with exponents (a,b,c) to s^(8a+8b+2c) Y1^a Y2^b, which is injective on exponent vectors, hence an injective ring map. The resonance identities hold in Lambda[Y1,Y2] after the composite maps, so they hold in B[x,y,z]: the extension with free x,y is valid. Normalized completed matrices have determinants in B that are units of Lambda; an element of B invertible in B[s,s^-1] is invertible in B (in every residue field a constant is a unit iff nonzero), no reducedness needed. Confirmed.

## C. Inventory and s elimination: CONFIRMED

Removed rows: [S^8]E1,[S^9]E0 are identities in Lambda (17b); [S^7]E1,[S^8]E0 and [S^6]E1,[S^7]E0 vanish identically after (3),(4) by the first and second quotient isomorphisms; [S^5]E1,[S^6]E0 are Lambda-multiples of Psi3 and [S^4]E1,[S^5]E0 equal lambda_B Psi4, -lambda_A Psi4 (A.4, A.5). The tau>=2 rows are the 16r Euler recurrence with the weight-9 target and are solved for Bhat_4..Bhat_0. Nine G_i plus H0 = s^7, H1 = U s^5 is exactly (7) rescaled; H0, H1 keep the nonzero targets. Confirmed.

Over any B-algebra R with z a unit. From s^2 = z, s^7 = H0, H1 = U s^5: H0^2 = s^14 = z^7, zH1 - UH0 = U s^7 - U s^7 = 0, s = s^7/s^6 = H0/z^3. Conversely s := H0/z^3 gives s^2 = H0^2/z^6 = z, s^7 = H0 (H0^2)^3/z^21 = H0, s^5 = H0 (H0^2)^2/z^15 = H0/z, and U s^5 = UH0/z = H1 after dividing zH1 = UH0 by the unit z. H0 is a unit because H0^2 is. Only z and H0 are inverted; s is determined uniquely, so no sign is lost and no factor is deleted. Hence R[s,s^-1]/(s^2-z, s^7-H0, H1-Us^5) and R/(zH1-UH0, H0^2-z^7) are isomorphic R-algebras (natural map and s -> H0/z^3), over the full rank-7 product algebra B included. Confirmed.

## D. Finite cubic cover: CONFIRMED

Forward: eta^3 = h0 (degree at most 3), mu = eta^2, s = eta^3, z = mu^3 = eta^6 = s^2, x = mu X, y = mu^2 Y. G_i(x,y,z) = mu^(w_i) g_i = 0. H0(x,y,z) = mu^9 h0 = eta^21 = s^7. H1 = mu^8 h1 = eta^16 ubar h0 = eta^19 ubar. U = mu^2 ubar = eta^4 ubar, so U s^5 = eta^19 ubar = H1. The unsquared targets, s = h0 nonzero and omega = w f5 s^8 are recovered; (20) then gives a full point over K(eta) with the same B-map. Confirmed.

Backward: mu^3 = z = s^2 (degree at most 3), X = x/mu, Y = y/mu^2: g_i = mu^(-w_i) G_i = 0; h0 = s^7/mu^9 = s^7/s^6 = s, nonzero; h1 = U s^5/mu^8 = U s^5/(s^4 mu^2) = ubar s = ubar h0 with ubar = U/mu^2. Reciprocal: eta = s/mu gives eta^2 = s^2/mu^2 = mu and eta^3 = s^3/mu^3 = s = h0, so (19) returns s,x,y,z exactly. Each direction adjoins one cube root, degree at most 3, B-map preserved. Confirmed.

Over an algebraically closed characteristic-zero field both directions are same-field, so nonemptiness is exactly equivalent; over general K it is existence up to a cubic extension, not a same-field rational-point bijection and not a ring isomorphism. The weighted action is a symmetry of the nine G_i and of zH1 - UH0 only; H0^2 = z^7 (weights 18, 21) is satisfied by the choice of mu, which is precisely the cover. No s = 1 is set. The 112/196 endpoint is quoted only as the accepted 16r conditional endpoint. Confirmed.

## E. Deviations, limitations, remaining doubts

- Deviations: none from scope. The owned box directory is empty; hashes above were copied from the sha256sum output, not typed from the task.
- Consumed as accepted premises, not re-derived here: lambda3(h3) = 1 (third gate B), unimodularity and the Gram-adjugate left inverse of (Acol,Bcol) (fourth producer 4, fourth gate), the unit determinants of N1, N2 (first and second gates), q6 = q7 = 0 in Lambda (17b).
- Not read: the third producer body, the 17b producer body, and the producer bodies outside the ranges listed in 0.
- Smallest repairs, wording only: (i) line 22 could say the theta^6 row FORCES V4 = 0 (it is the Euler determination of [S^0]B_4); (ii) section 5 could add that H1 = U s^5 is also inhomogeneous (weights 8 and 19/2 with wt s = 3/2) and only zH1 - UH0 (weight 11) is homogeneous. Neither changes a formula.
- No measured acceleration, independence, dimension, nonzero-row count, properness, unit, source point or degree bound is asserted or checked.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only check: no prior xmodel/f10-r1-weighted-composition-gate-fable5-20260909.md existed (apply_patch Add succeeded) and the owned box directory was created empty; no corpus scan.

<!-- BODY-END -->
