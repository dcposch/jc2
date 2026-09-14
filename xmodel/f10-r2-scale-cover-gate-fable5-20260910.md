# FIRST Fable5.1 gate: exact r2 faithful fifth-root/cubic scale cover

status=UNSEALED (no Seal, no charge_basis authored; adapter seals)
lane=f10-r2-scale-cover-gate-fable5-20260910
gate_model=claude-fable-5-1
first_action_utc=2026-09-10T09:03:53Z (hash command); stop = earlier of 09:17:53Z (first+14 min) and 09:19:00Z ROOT TERM, final-2-min reserve from 09:15:53Z, never reset
mode=manual math/text/hash only; ZERO CAS/Python/subprocess/scripted arithmetic; tools date, ls, wc, sha256sum, head, tail, od, grep, sed, apply_patch only
owned=xmodel/f10-r2-scale-cover-gate-fable5-20260910.md, box/f10-r2-scale-cover-gate-fable5-20260910/ (both absent at 09:03:53Z before first write)

## 0. Custody and read scope

Exactly the six snapshots in /tmp/jc2-lane.6CCcPE/inputs were hashed by sha256sum at 09:03:53Z BEFORE any body read; all six digests equal the charged list byte for byte (recorded in box/input_custody.md). Then ALL SIX were read WHOLE in parallel bounded reads: the cover (131 lines by wc -l, ending at its Seal), its artifact JSON (one line), READ-SCOPE (9 lines), ROOT-CARD (59 lines), the accepted parent transfer (362 lines, ending at its Seal) and the accepted parent gate (70 lines, ending at its marker). No read was clipped, so no recovery read was needed. Both body seals were replayed by head -c and sha256sum and match. No provenance, ledger, code, corpus, network, other lane or live file was accessed. Charged premise: the accepted corrected 19-row parent interface, with the late operator read as 7CV'-6C'V+kD' (gate correction), NOT the parent's printed -18C'V. The cover body contains no occurrence of "Llate" or "-18" (grep count 0); it consumes only the 19 rows, the weights and the two low-row forms, so the mandatory correction changes nothing in it and no premise re-review is claimed.

## A. Rank-5 monic cover and coordinate change: CONFIRMED

D=A[w]/(w^5-s) is free over A on 1,w,w^2,w^3,w^4 (division by a monic polynomial); free of positive rank is faithfully flat. w*(w^4/s)=w^5/s=1 with s^-1 in A, so w is a unit: CONFIRMED. Eliminating s=w^5 and s^-1=w^-5 gives D=B[w,w^-1,X1,X2,X3]/I19(s=w^5), and X_i=w^(2i)Y_i is an automorphism of B[w,w^-1][X] with inverse Y_i=w^(-2i)X_i: CONFIRMED. For a weight-k row, the monomial cX^a z^d with a1+2a2+3a3+5d=k maps to c w^(2a1+4a2+6a3+10d) Y^a = c w^(2k) Y^a, coefficients in B untouched, so F_k(X,z)=w^(2k)F_k(Y,1) and every retained row differs from its slice by the unit w^(2k): CONFIRMED. The seventeen weights 5,6,7; 13..8; 15..8 are the parent's Psihat5,6,7 and K1_i (14-i, i=1..6), K0_i (16-i, i=1..8): CONFIRMED against parent (20) and section 9.

## B. Both low rows and the triangular row change: CONFIRMED

K0_0 has weight 16 and s^7=w^35, so K0_0-s^7 = w^32 L0 - w^35 = w^32(L0-w^3). K1_0 has weight 14, U weight 3 (so U involves no z, U0=U(Y)), s^5=w^25: K1_0-U s^5 = w^28 L1 - w^6 U0 w^25 = w^28(L1-w^3 U0): (4) CONFIRMED. Own replay of the identity L1-w^3U0=(L1-U0L0)+U0(L0-w^3): the right side is L1-U0L0+U0L0-U0w^3: CONFIRMED. The row change (L0-w^3, L1-w^3U0) -> (L0-w^3, L1-U0L0) is unimodular triangular (add -U0 times row one), no row deleted: CONFIRMED. In the quotient L0=w^3 is a unit because w is, so localizing L0 changes nothing and the stratum L0=0 is already empty in D, not discarded: CONFIRMED. Cosmetic slip only: line 47 says the difference of the two rows "is U0 times the first"; that is the order (L1-w^3U0)-(L1-U0L0), and the other order gives -U0 times it. Line 59 is the exact signed identity, so nothing depends on the wording.

## C. Common algebra D ≅ C[w]/(w^3-L0), rank 3, zero-ring equivalence: CONFIRMED

D = B[Y,w,w^-1]/(seventeen F_k(Y,1), L0-w^3, L1-U0L0). On the other side, in C[w]/(w^3-L0) the element L0 is a unit of C, so w is a unit with inverse w^2/L0; and conversely in B[Y,w,w^-1]/(w^3-L0) the element L0=w^3 is a unit. Hence both algebras equal B[Y,w,w^-1,L0^-1]/(seventeen slices, L1-U0L0, w^3-L0): (3) CONFIRMED. Well-definedness replayed on every generator: forward, w^5-s -> 0; F_k(X,z) -> w^(2k)F_k(Y,1)=0; K0_0-s^7 -> w^32(L0-w^3)=0; K1_0-Us^5 -> w^28((L1-U0L0)+U0(L0-w^3))=0; s^-1 -> w^-5 = w/L0^2 exists. Inverse, F_k(Y,1) -> w^(-2k)F_k(X,w^10)=w^(-2k)F_k(X,z)=0; L1-U0L0 -> w^-28(K1_0 - w^-10 U K0_0) = w^-28(K1_0 - U s^5)=0 using K0_0=w^35; L0^-1 -> w^-3 with L0 -> w^-32 K0_0 = w^3; w^3-L0 -> -w^-32(K0_0-s^7)=0. Composites are the identity on s, s^-1, X_i, w and on Y_i, L0^-1, w: CONFIRMED. C[w]/(w^3-L0) is free over C on 1,w,w^2, so faithfully flat of rank three; D free of rank five over A. M⊗D=M^5 and N⊗C[w]/(w^3-L0)=N^3, so A=0 iff D=0 iff C=0, and every step (monic adjunction, unit inversion, unimodular row change) commutes with arbitrary base change B->B', nilpotents allowed: CONFIRMED. The cover states explicitly it is not A≅C and not s=1: CONFIRMED as stated. Row count 17+1 in C plus w^3-L0 equals the 19 of D: CONFIRMED.

## D. Guard, full-source read-back, field points, etale: CONFIRMED

omega=W t5 s^8 = W t5 w^40 with W, t5 the parent's B-units: CONFIRMED. D is an A-algebra, so every parent identity (band maps, Euler mate, inverse-polynomiality, gauges, all 32 residual read-backs modulo the 19 rows) holds in D unchanged; the cover additionally checks BOTH low rows in (4) and reads all nineteen rows back through the inverse map: CONFIRMED, no receiver-only or leading-only point is used. Field points: a C-point over a field k has L0 in k^x; adjoining a root of w^3=L0 is a field extension of degree at most 3, then s=w^5, X_i=w^(2i)Y_i; an A-point has s in k^x, adjoining a root of w^5=s is of degree at most 5, and then L0=w^-32 K0_0 = w^-32 s^7 = w^3 is nonzero: CONFIRMED, no embedding, real root or point is asserted. Etale: 5w^4 and 3w^2 are units because w is a unit and 5, 3 are units in every Q-algebra (B is a Q-algebra): CONFIRMED, and correctly declared unnecessary for the zero-ring equivalence.

## E. Finite envelopes, weights, degree bounds: CONFIRMED

M_k: a weight-k monomial X^a z^d has a1+2a2+3a3 = k-5d <= k with k-(a1+2a2+3a3)=5d, ordinary degree a1+a2+a3 <= a1+2a2+3a3 <= k, and d=(k-a1-2a2-3a3)/5 is unique, so no two slots of one row merge: CONFIRMED. Final row: z K1_0 has weight 5+14=19 and U K0_0 has weight 3+16=19, so z K1_0-U K0_0 is homogeneous of weight 19 and its z=1 slice is L1-U0L0; own support check: L1 has Y-weights {14,9,4} and U0L0 has {3}+{16,11,6,1}={19,14,9,4} = M_19, degree bound 19, NOT 14: CONFIRMED. L0 has support M_16, degree bound 16: CONFIRMED. Over B: four variables Y1,Y2,Y3,J and 18+1 rows with J L0-1 of degree at most 17: CONFIRMED. Over Q: add Z and P7, five variables, twenty slots; sliced weight-k row degree at most k+6, mixed low row at most 25, guard row at most 23, P7 degree 7: CONFIRMED. Six variables and 21 slots in the parent versus five and 20 here: CONFIRMED as a count only; the cover asserts no height, runtime, coefficient-count, dimension or finiteness claim and says the combined row has the larger bound 19: CONFIRMED. Zero, dependent or nilpotent-L0 cases are flagged (line 61) and never treated as row deletion; nilpotent L0 in the 18-row quotient makes C=0, consistent with D=0 since a nilpotent unit forces the zero ring: CONFIRMED.

## F. Changed-object controls and non-claims: CONFIRMED

1. Without the L0 localization the stratum L0=0 survives in the 18-row quotient while its lift needs a unit w with w^3=0, impossible in a nonzero ring; the equivalence would fail: genuine control. 2. w=1 forces L0=1 (and s=1); in Q[T,T^-1,w]/(w^3-T) the parameter T is free and w=1 kills it: genuine control against the source operation s=1. 3. Dropping the second low row: with L0 an invertible parameter, U0=0 and L1 a free variable, L0-w^3 does not kill L1: genuine control. 4. Q[eps]/(eps^2)->Q has the same field points but Q is eps-torsion, not flat: genuine control against pointwise root-taking. Non-claims: no Y1 unit; Y-rescaling preserves a sliced row only for fifth roots of unity because Y-weights within one row differ by multiples of five (own check); no S translation because Ahat3=S is forced; no source point, UNIT certificate, all-r coverage or JC2 theorem: all CONFIRMED as stated.

## Verdicts

| item | verdict |
|---|---|
| A rank-5 cover, unit w, X=w^(2i)Y, w^(2k) scaling | CONFIRMED |
| B both low rows (4), triangular row change, L0 localization | CONFIRMED (order wording at line 47 cosmetic) |
| C common algebra (3), both maps, rank 3, A=0 iff C=0 | CONFIRMED |
| D guard w^40, full read-back, field points, etale | CONFIRMED |
| E M_k, weights, row 18 weight 19, degree bounds 17/25/23/7 | CONFIRMED |
| F four controls, non-claims | CONFIRMED |

Smallest defect: the unsigned phrase "their difference is U0 times the first parenthesized row" (line 47), whose sign depends on subtraction order; minimal exact correction: read it as (L1-w^3U0)-(L1-U0L0)=U0(L0-w^3), which is the displayed identity at line 59. Not theorem-breaking. REFUTED: nothing. GAP (unchanged, honest): all coefficients, the eighteen sliced rows, the L0 inverse and the outcome C=0 are uncomputed; existence and exactness of the covers only. Promotion scope: the proved ring interface (3) with faithful ranks 5 and 3 and the eighteen-row localized decision quantity, conditional on the accepted corrected parent; nothing beyond it.

## OPEN(S) RAISED

None. The sole remaining quantity is the producer's own: whether C, with ALL eighteen rows and L0 inverted, is zero. No computation is requested or authorized; no follow-on authority.

## COLLISIONS

status: EMPTY

- NONE. Own-only check: this lane wrote exactly xmodel/f10-r2-scale-cover-gate-fable5-20260910.md and box/f10-r2-scale-cover-gate-fable5-20260910/input_custody.md, both absent at 09:03:53Z; all writes by apply_patch; no Seal, no charge_basis, no corpus scan, no other lane, no network, no scientific subprocess.

## Completion

Authoring attestation: every byte of both owned files was written by apply_patch; no Write/Edit tool, heredoc redirection or script. Own WHOLE read of this report (sections 0, A-F, Verdicts, OPEN(S) RAISED none, COLLISIONS EMPTY) done before the marker. The report body carries no hex digest; the six digests live only in box/input_custody.md and were rechecked against live sha256sum after writing. Never reset. The marker below is the only standalone marker in this file and nothing follows it. All writers idle at the marker.

<!-- BODY-END -->
