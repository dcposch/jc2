# FIRST Fable5.1 gate: exact r2 cubic core and conditional 7-row test

status=UNSEALED (no Seal, no charge_basis authored; adapter seals)
lane=f10-r2-cyclic-core-gate-fable5-20260910
gate_model=claude-fable-5-1
first_action_utc=2026-09-10T11:17:37Z (hash command); stop = earlier of 11:33:37Z (first+16 min) and 11:34:00Z USER TERM; final-2-min reserve from 11:31:37Z; never reset
mode=manual math/text/hash only; ZERO CAS/Python/subprocess/scripted arithmetic; tools date, ls, wc, sha256sum, cat, sed, apply_patch only
owned=xmodel/f10-r2-cyclic-core-gate-fable5-20260910.md, box/f10-r2-cyclic-core-gate-fable5-20260910/ (both absent at 11:17:37Z; unsealed skeleton written first, then this body)
charged_input=xmodel/f10-r2-cyclic-core-astra-20260910.md
charged_input=xmodel/f10-r2-full-source-transfer-astra-20260910.md
charged_input=xmodel/f10-r2-full-source-gate-fable5-20260910.md
charged_input=xmodel/f10-r2-scale-cover-astra-20260910.md
charged_input=xmodel/f10-r2-scale-cover-gate-fable5-20260910.md

## 0. Custody and read scope

Exactly the five snapshots in /tmp/jc2-lane.HyJFTJ/inputs were hashed by sha256sum at 11:17:37Z BEFORE any body read; all five digests equal the charged list byte for byte (recorded only in box/input_custody.md; this body carries no hex digest). Then ALL FIVE were read WHOLE in parallel bounded reads: cyclic core (228 lines, ending at its Seal), scale cover (131, at Seal), scale-cover gate (65, at marker), full-source gate (70, at marker), full-source transfer (362, segments 1-200 and 200-362, at Seal). No read was clipped, so no recovery read was needed. No provenance, ledger, code, corpus, network, other lane, process or live file was accessed. Premises: the accepted 19-row transfer read with its FIRST gate's late-operator correction (7CV'-6C'V+kD', not the printed -18), and the accepted cover (3) as confirmed by its gate. No mod89 coefficient or initial-form report exists among the inputs and none is used. ROOT's derivation is tested, not assumed.

## 1. Verdicts

| item | verdict |
|---|---|
| A Z/5 grading from source weights; 15 generators; mixed row class 4 (=19 mod 5); L0 class 1; U0 class 3; 19 rows | CONFIRMED, unconditional |
| B gr R = B[Y]/(H5,H6,H7) by Rees/saturation; series S5 S7 (1-t+t^2); 7 per class; 35 | CONFIRMED CONDITIONAL on the s.o.p. hypothesis, which is UNKNOWN |
| C J0 = sum R_{-d} g; 7x105 over B, 49x735 over Q; C=0 iff t0^7 in J0 | CONFIRMED; exponent 7 and sizes conditional, nilpotency equivalence unconditional |
| D E = C0; C = E[T]/(T^5-t0) free rank 5 | CONFIRMED, unconditional |
| E D = E[w]/(w^15-t0); cover degree 3i; A = E[s]/(s^3-t0) free rank 3 | CONFIRMED, unconditional given the accepted cover |
| F maps (7),(8), inverses, all 19 rows, guard, transport | CONFIRMED; no omitted source condition found |
| G e<=7, 5e, 3e<=21, <=147 over Q; lengths not point degrees; controls | CONFIRMED CONDITIONAL |

## 2. Own replays

A. With wt(Y_i)=i, wt(z)=5, a weight-h monomial X^a z^d has a1+2a2+3a3 = h-5d, congruent to h mod 5, so every slice F_k(Y,1) is Z/5-homogeneous of class k mod 5 and (f5,f6,f7) is a homogeneous ideal: R is genuinely Z/5-graded by monomial weight, no root of unity used. Classes: K1_i (14-i, i=1..6) give 3,2,1,0,4,3; K0_i (16-i, i=1..8) give 0,4,3,2,1,0,4,3; L0 class 1 (16), L1 class 4 (14), U0 class 3 (U has weight 3 < 5, hence no z term, so U0 = U(Y) is exactly weight 3); U0 L0 has class 4 = class of L1, so the mixed row is homogeneous. Count 6+8+1 = 15 generators of J plus f5,f6,f7 = the cover's 18 rows; the 19th row K0_0 - s^7 is the cover relation w^3 = L0. CONFIRMED.

B. F_h(Y,t) = t^h f_h(t^-1 Y1, t^-2 Y2, t^-3 Y3) sends Y^a of weight w(a) <= h to t^(h-w(a)) Y^a with exponent a nonnegative multiple of 5: a polynomial, homogeneous of weight h with wt(t)=1, F_h(Y,0)=H_h, F_h(Y,1)=f_h. B is a field (P7 irreducible over Q, accepted), so B[Y] is Cohen-Macaulay and a weighted-homogeneous s.o.p. is a regular sequence. (t,F5,F6,F7) is regular: t is a nonzerodivisor on B[Y,t] and the quotient by t carries (H5,H6,H7). Graded permutability (four homogeneous elements of positive degree, S_0 = B a field; the kernel of t on S/(F) is graded, and a graded module vanishes iff it vanishes at the irrelevant ideal, where the local theorem applies) makes t a nonzerodivisor on S/(F5,F6,F7), so (F5,F6,F7) equals its t-saturation. Own replay of the two inclusions: for g in I=(f5,f6,f7), t^N g^h lies in (F), so I^h lies in (F):t^infinity = (F); conversely each homogeneous element of (F) is t^m times the homogenization of its dehomogenization, which lies in I. Hence (F) = I^h and setting t=0 gives in_w(I) = (H5,H6,H7), gr R = B[Y]/(H5,H6,H7): (1) CONFIRMED conditionally, an equality not a bound. Series: (1-t^5) = (1-t)S5, (1-t^7) = (1-t)S7, (1-t^6) = (1-t^3)(1+t^3), so the quotient is S5 S7 (1-t)(1+t^3)/(1-t^2) = S5 S7 (1+t^3)/(1+t) = S5 S7 (1-t+t^2): (2) CONFIRMED; value 5*7*1 = 35; modulo t^5-1, t^a S5 = S5, so the series reduces to S7(1)(1-1+1) S5 = 7 S5 and every class has dimension 7. Filtration compatibility: the ideal is Z/5-homogeneous, so F_n R meets R_j in the image of the weight-<=n polynomials of class j, and gr_n R lies in class n mod 5. The hypothesis (equivalently V(H5,H6,H7) = {0} over the algebraic closure, equivalently m-primary in dimension 3) is UNKNOWN and is not tested here.

C. For c in R and g in R_d, (cg)_0 = c_{-d} g, so J0 = sum_k R_{-d_k} g_k as a B-subspace; products of generators are not needed because J = sum R g_k is already an ideal. Under B each R_{-d} has a 7-element basis: at most 105 columns in the 7-dimensional R0, and 49 by 735 over Q. Q0 = (R/J)_0 = R0/J0 because J is homogeneous. C = Q[L0^-1] = Q[t0^-1] since L0^-1 = L0^4/t0 and t0^-1 = (L0^-1)^5. Q[t0^-1] = 0 iff t0 is nilpotent in Q iff nilpotent in Q0 (Q0 is a direct summand, so Q0 -> Q is injective and t0^n lies in Q0). Under dim_B Q0 <= 7 a nilpotent B-linear operator has index at most the dimension, so t0^7 = 0 in Q0, i.e. L0^35 lies in J0 as an element reduced in R0; conversely t0^7 = 0 kills the localization; the zero ring is included. (3) CONFIRMED; only the exponent 7 and the block sizes are conditional. No basis, rank, height or runtime is claimed, correctly.

D. Q is Z/5-graded with t0 in Q0, so Q[t0^-1] is the direct sum of the Q_j[t0^-1] and C0 = E. L0 is a homogeneous unit of class 1, so multiplication by L0^j is a bijection C0 -> C_j with inverse L0^-j, and C is the direct sum of the E L0^j, j=0..4. The ring map E[T]/(T^5-t0) -> C, T -> L0, is defined (L0^5 = t0), surjective componentwise, and injective because a vanishing sum of e_j L0^j has every graded component zero, forcing e_j = 0. Free basis 1..T^4; valid for arbitrary nilpotents and E = 0; no primitive root used. (4) CONFIRMED. Q0 (quotient degree zero) and E (its localization) are correctly distinguished throughout.

E. The core's C is the cover's C: three Psihat slices, fourteen low slices, the mixed row, L0 inverted. From the accepted (3), D = C[w]/(w^3-L0) = E[T,w]/(T^5-t0, w^3-T) = E[w]/(w^15-t0), free on 1..w^14, w a unit with inverse w^14/t0: (5) CONFIRMED. Cover grading: A[w]/(w^5-s) with A in degree 0 and w in degree 1 is Z/5-graded (w^5-s homogeneous) and D_0 = A on the free basis 1..w^4. Own check that the cover isomorphism is graded when C carries three times its original class: Y_i = w^(-2i) X_i has degree -2i = 3i; X_i = w^(2i) Y_i has degree 5i = 0; L0 (class 1) has degree 3, the degree of w^3, so w^3-L0 is homogeneous; E (class 0) stays in degree 0; T = L0 has degree 3 and w^3-T is homogeneous. Multiplication by 3 is a bijection of Z/5 fixing 0. In E[w]/(w^15-t0) the degree-0 part is E + E w^5 + E w^10 (j in 0..14 with j = 0 mod 5), and s = w^5 satisfies s^3 = w^15 = t0. Hence A = D_0 = E[s]/(s^3-t0), free of rank 3 over E: (6) CONFIRMED as an exact ring identity, not A = C, with no s = 1, L0 = 1 or point argument; consistency: in D, L0^5 = w^15 = s^3.

F. epsilon_i = Y_i L0^-i has class i-i = 0, so it lies in E, and L0^-i = L0^(5-i)/t0. In D: X_i = w^(2i) Y_i = w^(2i) epsilon_i L0^i = epsilon_i w^(5i) = epsilon_i s^i; s^-1 = s^2/t0: (7) CONFIRMED. (8): Y^a of weight 5k equals w^(-10k) X^a = s^(-2k) X^a and t0^-n = s^(-3n), so p/t0^n maps to sum p_a X^a s^(-2k(a)-3n) in A: CONFIRMED. Own composite: (7) after (8) on Y^a/t0^n gives epsilon^a s^(5k) s^(-2k-3n) = Y^a t0^-k t0^(k-n) = Y^a/t0^n; the other composite is the identity on X_i and s because (7) is the restriction of the accepted cover map to D_0 = A. Well-definedness: (8) yields an element of A whose image in D is the cover image of e, and A -> D is injective (A is a direct summand), so the element does not depend on the representative. The seventeen homogeneous rows transport by the units w^(2k); the low rows by w^32(L0-w^3) and w^28(L1-w^3 U0) = w^28((L1-U0 L0)+U0(L0-w^3)) (own expansion L1-U0L0+U0L0-U0w^3), as in the accepted cover. omega = W t5 s^8 is a unit because s is. Euler mate, inverse-polynomiality and gauges are identities inside A and pass unchanged. Omitted source condition: none found; all 19 rows, s^-1, the WHOLE B and the L0 localization (forced since w^3 = L0 is a unit) are accounted for. The late-operator correction touches no object used here: the core consumes only the 19 rows, their weights and the two low-row shapes.

G. Under B, Q0 is Artinian of dimension <= 7; localization at t0 is a direct factor (t0 is a unit or nilpotent in each local factor), so e = dim_B E <= 7 and E is a quotient of Q0. Then dim_B C = 5e by (4), dim_B A = 3e <= 21 by (6), dim_Q A = 7*3e <= 147. These are lengths: B[s]/(s^3-1) has the degree-one point s = 1, so residue-field degrees need not be divisible by 3; a valid changed-object control, not a source point. Controls: a class-0 L0 gives no bijection C0 -> C_j; dropping a generator changes J0; omitting localization retains the L0-nilpotent stratum; H5 = Y1^5, H6 = Y1^6, H7 = Y1^7 has the right weights but zero set {Y1 = 0} of dimension 2, so degrees 5,6,7 alone give neither 35 nor 7; labels without a basis give no matrix. All meaningful. CONFIRMED conditional.

## 3. Defects, smallest remaining consumer, non-claims

Smallest defect: none theorem-breaking. Cosmetic only: section 3 says the mixed row has "degree 19 modulo 5" while its convention names classes by a representative; 19, 14 and 4 are the same class, and "not a homogeneous-weight-14 replacement" refers to the ordinary-degree envelope 19 of the accepted cover, not to a different Z/5 class. Section 2's permutability sentence is terse but correct as replayed in B. REFUTED: nothing. No invalid map or ring was found, so no correction is proposed. GAP (honest, declared by the producer): whether the ACTUAL H5, H6, H7, three weighted-homogeneous B-polynomials of weights 5, 6, 7 in Y1, Y2, Y3, form a system of parameters is UNKNOWN; without it R need not be finite-dimensional and the 7x105 test and every bound in G are unavailable, while (4), (5), (6), (7), (8) still hold. Smallest remaining consumer, in order: (i) decide the s.o.p. property of H5, H6, H7 (zero-dimensionality of one weighted-homogeneous ideal in three variables over B); (ii) then construct a graded basis of R, the fifteen blocks R_{-d} g, the reduced target L0^35 in R0, and test membership. Independently of (i): C = 0 iff t0 is nilpotent in Q0, and A = 0 iff E = 0. Nothing is executed or authorized here; no source zero or nonzero, UNIT certificate, all-r statement or JC2 conclusion follows from anything above.

## OPEN(S) RAISED

None. The sole remaining quantities are the producer's own: the s.o.p. property of the actual H5, H6, H7, and the membership L0^35 in J0. No computation is requested or authorized; no follow-on authority.

## COLLISIONS

status: EMPTY

- NONE. Own-only check: this lane wrote exactly xmodel/f10-r2-cyclic-core-gate-fable5-20260910.md and box/f10-r2-cyclic-core-gate-fable5-20260910/input_custody.md, both absent at 11:17:37Z; all writes by apply_patch; no Seal, no charge_basis, no corpus scan, no other lane, no network, no scientific subprocess.

## Completion

Authoring attestation: every byte of both owned files was written by apply_patch; no Write/Edit tool, heredoc redirection or script. Own WHOLE read of this report (sections 0-3, Verdicts, OPEN(S) RAISED none, COLLISIONS EMPTY) done before the marker. The body carries no hex digest; the five digests live only in box/input_custody.md and were rechecked against live sha256sum after writing. Never reset. The marker below is the only standalone marker in this file and nothing follows it. All writers idle at the marker.

<!-- BODY-END -->
