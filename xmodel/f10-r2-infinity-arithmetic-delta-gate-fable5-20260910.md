# FIRST delta gate (Fable 5.1): unreplayed r2 mod-89 arithmetic of the compatibility-infinity report

status=UNSEALED (no Seal, no charge_basis authored; adapter seals)
lane=f10-r2-infinity-arithmetic-delta-gate-fable5-20260910
gate_model=claude-fable-5-1
first_action_utc=2026-09-10T10:52:18Z (hash command); stop = earlier of 11:06:18Z (first+14 min) and 11:09:00Z ROOT TERM; final-2-min reserve from 11:04:18Z; never reset
mode=manual math/text/hash only; ZERO CAS/Python/subprocess/scripted arithmetic; tools date, ls, sha256sum, cat, sed, wc, apply_patch only
owned=xmodel/f10-r2-infinity-arithmetic-delta-gate-fable5-20260910.md, box/f10-r2-infinity-arithmetic-delta-gate-fable5-20260910/ (both absent at 10:52:18Z)

## 0. Custody and read scope
All 8 snapshots under /tmp/jc2-lane.DzByBh/inputs were hashed by sha256sum at 10:52:18Z BEFORE any body read; all 8 equal the charged pins (rows copied from the sha256sum output into box/input_custody.md; no digest typed in this body). Both owned targets absent at 10:52:18Z; skeleton by apply_patch at 10:56:51Z. Read WHOLE after the match: the charged producer (to its Seal), the previous FIRST gate (to its marker), produce.py and arithmetic.py (source of every operator, pivot, column and psi formula used below), the reconstruction report and its STATIC gate, the full-source gate, and the transfer report (clipped at 2 KB in the aggregate read; recovered WHOLE by bounded reads 1-120, 121-245, 246-end, ending at its Seal). Nothing executed, imported or parsed; every residue below is my own hand arithmetic mod 89 from C=T^3-6T-6, D=T^5-27T^3+39T^2+38T+37, 7a=47, 12b=88, U=-15q, d0=50p (FIRST-checked premises, not re-derived). Operator L_h(A,V)=7CV'-(12-h)C'V+(7-h)AD'-12A'D as in produce.py `op`; upper pivots 7j-3(12-h); columns ([T^1]res,[T^0]res,7a V_j(0)-12b A_j(0)); psi=base[1]*c1-base[0]*c0 with base=([T^1],[T^0]).

## A. Item 1: gap-2 and gap-3 full 3x3 matrices, pivots, determinants: PASS
Own upper solves for A=T^j (j=0,1,2), V of degree <=4, rows T^6..T^2. Gap 2 (pivots -2,-9,-16,-23,-30; A-parts 5D'=(12,34,40,0,25), 5TD'-12D=(1,1,11,8,0,13), 5T^2D'-24TD=(0,2,79,77,65,0,1)): V_0=(52,0,85,0,0), V_1=(21,22,0,41,0), V_2=(54,50,73,0,45); columns (14,17,42), (41,70,8), (21,72,46). Gap 3 (pivots 1,-6,-13,-20,-27; A-parts 4D'=(63,45,32,0,20), (1,52,22,0,0,8), (0,2,41,88,57,0,85) plus target +2T^6 in the residual): V_0=(19,0,70,0,0), V_1=(77,13,0,31,0), V_2=(60,41,69,0,2); columns (39,21,4), (30,53,59), (38,5,61). All 18 entries equal the producer's two displayed triples. Full determinants (columns k,l,u2; rows T,1,rho): det M2=11, det M3=78, both units mod 89. Their (k,l) residual 2x2 blocks have determinants 16=-73 and 13=-76 (the producer's 73/76 up to the column-order sign), and the Schur complements (rho per unit u2 after solving the two residual rows) are 73 and 6, so det M = det(2x2) x rho-coefficient holds in both gaps: 16*73=1168=11 and 13*6=78. These are three distinct objects and all are units. Cramer regularity: every matrix entry lies in O_(89,Z) (pivot inverses and 7a,12b are 89-integral) and det M is a unit there, so M^-1 has entries in O_(89,Z) and the characteristic-zero solution M^-1(0,0,rho) is (89,Z)-integral with reduction equal to the displayed tuple; the mod-89 tuple is not merely a solution of the homogeneous residue equations. Back-solve: gap 2 gives (k,l,u2)=(37,65,1)u2, rho=73u2, 1/73=50, so A2=(70,46,50)p and V2=70V_0+46V_1+50V_2=(8,41,77,17,25): both equal the FIRST-checked tuples. Gap 3 gives (62,19,1)u2, rho=6u2, 1/6=15, so A3=(40,18,15)q, U=-15q, V3=(20,48,8,24,30): equal. The previous gate's determinant GAP is closed.

## B. Item 2: W4, A4, V4, middle shift: PASS
Own products: V2'=(41,65,51,11), A2'=(46,11), A2V2'=(22,28,66,47,30,16), A2'V2=(12,16,77,27,2,8); W4/p^2=5A2V2'-10A2'V2=(79,69,5,54,41): equal. Gap 4 (pivots 4,-3,-10,-17,-24): basis V_0=(21,0,46,0,0) with column (19,54), V_1=(74,63,0,1,0) with column (36,17), particular V_part=(66,66,13,0,0) with base (85,30)=(-4,30). Rows 19k+36l-4=0 and 54k+17l+30=0, determinant 19 (order l,k), 1/19=75, k=52, l=32: A4/p^2=(52,32) equal; V4=V_part+52V_0+32V_1=(55,35,2,32), [T^4]V4=0: equal, so the 'middle V4' and 'middle U2' checks pass with u2=0 forced by the H7 unit as in produce.py. Middle shift: l is the coefficient v0-U*d1 with d1=[T^2]A1=0 on X1=0 (gap 1 zero), so no new free coordinate; the forced middle value rho_4=7a(V4-V_part)(0)-12b*52=47*78-37=-20=69 p^2 (derived, not consumed by alpha/beta/gamma).

## C. Item 3: alpha: PASS except the five low W5 entries (replay GAP, exact list)
Critical homogeneous column: A_var=1, h=5 (pivots -7,-14,-21, A-part 2D'=(76,67,16,0,10)): V_var=(53,0,65), residual pair (36,77): equal to the displayed column. y-term: y=-U*d0=-(-15q)(50p)=+750pq=38pq (product, not an equality of -15 and 50), and the y part of the operator is y(2TD'-12D)=38*(1,65,44,73,0,87)=(38,67,70,15,0,13). Target -2zT^5 vanishes at X1=0. Resonant T^5 row: 13+W5_5 must be 0, and the displayed W5_5=76 satisfies it, so that entry is confirmed independently of the products. N=-W5-ypart: (28,60,46,47,42,0) equal. Particular solve L_V(V)=N: v2=83, v1=3, v0=31 (equal), residual pair (88,80) equal. alpha=psi=80*36-88*77=-3896=20: equal, and the pair arises from the actual specified source (forcing plus unshifted y D_i plus zero target), not from an unverified pair. Remaining unreplayed: W5/(pq) entries T^0..T^4 = (23,51,62,27,47), which are the four products 5A2V3'-9A2'V3+4A3V2'-10A3'V2 with the replayed A2,V2,A3,V3; nothing else in item 3 is open.

## D. Item 4: beta and gamma: GAP (cap), exact remaining list
Not recomputed within the 14-minute cap: W6/(p^3)=(29,73,85,18,0) from 5A2V4'-8A2'V4+3A4V2'-10A4'V2; W6/(q^2)=(79,49,50,72,18,79) from 4A3V3'-9A3'V3; the late homogeneous column (62,23) and variation (7,0,68) (A_var=1, h=6, operator coefficient -6, pivots -4,-11,-18, A-part D'); the particular pairs (47,17) and (70,41); beta=62*17-23*47=62 and gamma=62*41-23*70=42 (the last two products were confirmed by the previous gate as arithmetic on the displayed inputs). Confirmed structurally only: the fixed U^2T^3 with U^2=47, target -47T^5, and the T^5 row 3U^2+W6_5=-U^2 giving W6_5=79 (previous gate). Denominators: Psi6 is formed before its own scalar substitution, gap 1 is zero so the critical band feeds neither axis coefficient, and only the pivots, 7a, 12b, dL, W, t5, H7 and the replayed unit determinants enter; no late/ell completion inverse is needed before Psi6. All denominators listed are 89-units; the item-4 GAP is replay only, not a refutation.

## E. Item 5: exact closed theorem now licensed
Over B=Q[Z]/P7, with H5,H6,H7 the z=0 top forms: alpha is a B-unit UNCONDITIONALLY given the replays in A-C plus the five W5 entries (the only unreplayed input to alpha). beta and gamma are B-units exactly when the item-4 list reduces to the displayed residues 62 and 42. Under those two conditions, on X1=0 and on every geometric component of B, H5=alpha*pq=0 forces pq=0 and H6=beta*p^3+gamma*q^2 forces the remaining coordinate to vanish, so the closed divisor X1=0 of V(H5,H6,H7) has no geometric point; every geometric point lies in the chart X1=1 and is detected by the producer's Q-saturated gcd of F,G plus the retained fibre (8). Nothing about weighted Proj, the 35-basis, source zero or JC2 follows. ROOT corrections recorded, not consumed: the previous gate's parenthetical L0^35 -> w^-96 K0_0^35 is wrong; with weight 16, L0=w^-32 K0_0 (z=w^10), so L0^35=w^-1120 K0_0^35; the parent's projection/faithful-cover argument stays conditionally correct and no scaling re-review was done. Early determinant units do not by themselves license the force/pair values; those are established here only where replayed (A, B, C).

## Verdicts
| item | verdict |
|---|---|
| 1 gap-2/3 3x3 matrices, pivots, det 11/78, 2x2 vs Schur 73/6, Cramer regularity | PASS |
| 2 W4, A4, V4, middle shift | PASS |
| 3 column (36,77), y=38pq, N, particular (31,3,83), pair (88,80), alpha=20 | PASS; W5 entries (23,51,62,27,47) unreplayed |
| 4 W6/(p^3), W6/(q^2), column (62,23), variation (7,0,68), pairs, beta/gamma | GAP (cap), exact list in D |
| 5 closed theorem | stated conditionally in E |
REFUTED: nothing. Every replayed entry agreed with the producer.

## OPEN(S) RAISED
None. The remaining quantities are the exact coefficient lists in C and D; neither is a new canonical OPEN. No execution, registration, promotion or follow-on authority is issued.

## COLLISIONS
status: EMPTY

- NONE. Own-only check: this lane wrote exactly xmodel/f10-r2-infinity-arithmetic-delta-gate-fable5-20260910.md and box/f10-r2-infinity-arithmetic-delta-gate-fable5-20260910/input_custody.md, both absent at 10:52:18Z; all writes by apply_patch; no Seal, no charge_basis, no corpus scan, no other lane, no network, no scientific subprocess.

## Completion
Authoring attestation: every byte of both owned files was written by apply_patch; no Write/Edit tool, no shell redirection, no helper, no source edit, no execution, no network. Own WHOLE read of this report and of box/input_custody.md done before the marker with the custody rows rechecked against live sha256sum. Timeline: hashes 10:52:18Z, skeleton 10:56:51Z, body before the 11:04:18Z reserve, stop 11:06:18Z, never reset. The marker below is the only standalone marker in this file and nothing follows it. All writers idle at the marker.

<!-- BODY-END -->
