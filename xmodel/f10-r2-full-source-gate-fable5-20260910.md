# FIRST Fable5.1 hostile gate: complete r2 full-source transfer and finite envelope

status=UNSEALED (no Seal, no charge_basis authored; adapter seals)
lane=f10-r2-full-source-gate-fable5-20260910
gate_model=claude-fable-5-1
first_action_utc=2026-09-10T08:47:55Z (hash command); stop 09:02:00Z ROOT TERM, final-2-min reserve 09:00:00Z, never reset
mode=manual math/text/hash only; ZERO CAS/Python/subprocess/scripted arithmetic; tools date, ls, sha256sum, cat, sed, wc, apply_patch only
owned=xmodel/f10-r2-full-source-gate-fable5-20260910.md, box/f10-r2-full-source-gate-fable5-20260910/ (both absent at 08:54:31Z before first write)

## 0. Custody and read scope

All 24 snapshots under /tmp/jc2-lane.51Drkf/inputs were hashed by sha256sum at 08:47:55Z BEFORE any body read; every one of the 24 digests equals the charged list byte for byte (recorded in box/input_custody.md). Read WHOLE after the match: the primary report (362 lines, two bounded segments 1-200 and 200-362, both ending at the Seal), its artifact JSON, READ-SCOPE, ROOT-CARD, and all 20 accepted reports (each cat ended at its Seal or marker; no clipping occurred, so no recovery read was needed). Only the 20 accepted reports are mathematical premises; root ell suggestion, real-domain design and the unreviewed affine endpoint are not inputs. The report OWN r2 ell proof (section 7) was reconstructed by hand below. Inherited qualifications kept: positive theta7 sign, critical forcing uses D_i, -ell S t^4 at weight 4r+1 (=9 at r=2).

## A. Leading ring L=B[s,s^-1], gauges, guard, full Euler recurrence, row/degree bounds: CONFIRMED

Own replay at r=2, m=7, n=12, tau=2/7, nu=12/7. dL, KL, gammaL, Sept and the leading coefficient -245*120*144*tau are the accepted 17zzd/17zzf displays with V renamed Z; P7 irreducible over Q by 17zzf (r=2 is the 7|3r+1 chart), so B=Q[Z]/(P7) is a field of rank 7 and dL, W=-KL/(210 dL), t5 are units of the WHOLE B (17zzd A, B). Normalization a=1/(W s^3), H=1/(W s^2), F=Z/(W s), b=1/(t5 s^5) and the back maps s=H/a, Z=Fa/H^2, W=a^2/H^3 are 17zz (3) verbatim; ab W t5 s^8=1, hence omega=1/(ab)=W t5 s^8: CONFIRMED. The 16r leading subring: F=d2, H=v4, a=k7 free, D4..D0 fixed by the five weight-12 Euler rows with pivots j-3(12-2j)=7j-36 (=-8,-15,-22,-29,-36), the two rows [S^14]E1, [S^16]E0 are exactly the theta^1, theta^0 rows of 7CD-12CD=-theta^7, and omega inverts ab: so the quotient by those two rows with ab inverted is the universal guarded L of 17zz, which needs H a unit (accepted 17o section 6): CONFIRMED. Recurrence (3), the delta list (1,u,-ell,ell u-1,2u-ell S,-u^2-2S,2uS,-S^2), residual polynomials (4) and envelopes 14=6r+2, 16=7r+2 equal 16r (4),(5),(12): CONFIRMED. Gauges k(0)=0, [S]B3=0, B0(0)=0 unchanged. The report states explicitly that fieldness/finite rank of B does not make (1) finite, reduced, nonzero or proper: CONFIRMED as stated, no such inference appears.

## B. Seven ordered band maps: CONFIRMED with ONE display defect (late operator)

Gap indices at r=2: h=1 (d1,v3,k6), h=2 (d0,v2,k5), kappa=19-h in {18,17}; modified h=3 (q=-u, l=v1-uF, k4), kappa=16=7r+2, T=Tbase-(2q/7)theta^7, q=7[Tbase]_7/16, numerators with T+2q theta^6-R: 17q section 7 verbatim; rho=7a V_lin(0)-12b U0 with the 7a V_part(0) subtraction: 17q (28). Middle h=4: l=v0-u d1 (17s (5),(6)), kappa=15, alpha=15/7, T7=H7 Y4+J4 with H7=s^7 t7(15/7); unit by 17zzf (r=2 mod 7 gives Z a unit for every h) and 17zz (8); Y4=-J4/H7 then kills both rows [S^10]E1,[S^12]E0 and no variable remains: CONFIRMED. Critical h=5: y=1-u d0, N_i=-(W5)_i+(12-2i) y D_i (unshifted), the five pivots 7,14,21 and rows r1,r0 are 17o (11)-(13) at r=2; Lambda, lambda chi=1, k2 and Psi5 replacement (8): 17o (15)-(21), determinant one: CONFIRMED. Late h=6, j=1: A band constant k1; B band deg<=2 with the fixed theta^3 coefficient u^2 (16r (7)) and target -u^2 theta^5 (weight 10) in the affine part; rows [S^8]E1,[S^10]E0; pivots -4,-11,-18 (=7l-18): CONFIRMED. DEFECT: the displayed operator Llate=7CV-18CV+kD is wrong; with h=6, n-h=6, the 17v operator is 7CV-6CV+kD (coefficient -(n-m+j)=-6). The printed -18 is 3(n-h), the theta^2 pivot, not the operator coefficient; with -18 the pivots would be -40,-47,-54, contradicting the report own list. Corrected scope: replace -18 by -6; the column g is also the k1-coefficient of the two actual rows of (3), and the ideal identity (g1,g0)=(H6(13/7),H7(13/7)) is imported from 17v with the correct operator, so the theorem survives the correction, but any checker following the display verbatim would compute a wrong column. Unit column: a maximal ideal of L containing t6(13/7),t7(13/7) would give a field point with W a unit, c=1+z+Zz^2+Wz^3, two contacts at 12/7 and 13/7, both in the 17w range 5/3<x<y<2, i.e. a point of the 17w guarded cubic algebra, which 17y proves is zero at r=2 (r=2 mod 7): so (g1,g0)=L, CONFIRMED; no single entry is asserted a unit. Homogeneity g1=s^-3 gbar1, g0=s^-4 gbar0: own check with C=a c(s theta), D=b d(s theta), b/a=W/(t5 s^2) gives V proportional to s^-2 and residuals s^-3, s^-4: CONFIRMED. The ordered extended-Euclid witness prescription is a finite existence prescription; it computes nothing and the report says so: CONFIRMED (existential, not possessed).

## C. NEW r2 ell column: CONFIRMED by independent derivation

Affineness: A is ell-free and (3) is linear in the targets delta_2=-ell, delta_3=ell u-1, delta_4=2u-ell S, so B and both residuals are affine in ell; highest ell target -ell S t^4 has weight 9, gap 7, below gaps 1-6: CONFIRMED. A band at weight 0 is k(0)=0; B band at weight 5 is S^5 Q with deg Q<=2 (S^i t^j, i+2j=5); operator 7CQ-5CQ (h=7, n-h=5, U=0). Own expansion: theta^4: 14Q2-15Q2=-Q2=-1 so Q2=1; theta^3: -8Q1+4F=0 so Q1=F/2; theta^2: 9H-(3/2)F^2-15Q0=0 so gE=(6H-F^2)/10; theta^1: 14a+FH-10F gE=L1; theta^0: (7/2)aF-5H gE=L0: (10) CONFIRMED. (11): 7aL1-2HL0=98a^2+7aFH-70aF gE-7aFH+10H^2 gE=98a^2+(10H^2-70aF)gE: CONFIRMED; in L/(L1,L0), gE(10H^2-70aF)=-98a^2 with a a unit makes gE a unit. Then (Q/C^beta)=-theta^4/(7C^(beta+1)) gives Q=gE(C/a)^(5/7)+O(theta^5); deg Q=2 and gE a unit force s^3 t3(5/7)=s^4 t4(5/7)=0, s a unit. Own finite identities: t3(X)=XW+(X)_2 Z+(X)_3/6, t4(X)=(X)_4/24+(X)_3 Z/2+(X)_2 Z^2/2+(X)_2 W, so 24(t4/(X)_2-t3/X)=12Z^2-12XZ+(X-2)(1-3X); at X=5/7=1-tau this is 12Z^2-12(1-tau)Z+(1+tau)(2-3tau)=dL(Z): (12) CONFIRMED (divisors 5/7, -2/7, 24 nonzero). dL is a unit of B, so the quotient is zero and (L1,L0)=L: CONFIRMED with no field or reducedness assumption. Rows E1[S^7],E0[S^9] (=6r+2-7, 7r+2-7); no theta^5 at weight 9 (needs S^-1): CONFIRMED. Lbar scaling: gE=s^-2(6W-Z^2)/(10W^2), L1=s^-3(14/W+Z/W^2-Z(6W-Z^2)/W^3), L0=s^-4(...): CONFIRMED. Determinant-one replacement (13) retains Psi7 and every lower row; cofactors existential only: CONFIRMED.

## D. Exact 19 retained slots and both quotient maps: CONFIRMED

Variables 6r+6=18: u, ell, d0-d2, v0-v4, k1-k7, omega. Consumed: leading (d2,v4,k7,omega) into L; (d1,v3,k6)->Y1; (d0,v2,k5)->Y2; (u,v1,k4)->Y3; (v0,k3) by the H7 unit; k2, k1, ell by determinant-one completions: 4+9+2+3=18, all accounted, none double-counted. Rows: E1 slots 0..14 and E0 slots 0..16 = 32; removed 14/16 (leading), 13/15, 12/14, 11/13 (early, modified), 10/12 (middle), and pairs 9/11, 8/10, 7/9 each replaced by one Psi: 32-2-6-2-3=19 = E1[0..6] (7) + E0[0..8] (9) + Psi5,6,7 (3): CONFIRMED. Forward map: ordered reconstruction with actual W_h, V_part, then (8),(9),(13), then (3); inverse: leading Z,s,omega, homogeneous rho with the 7a V_part(0) subtraction, forced Y4, k2,k1,ell forced by the three determinant-one identities; both are ring identities over L (17q C, 17s B, 17o B, and the same 2x2 argument for gaps 6,7): CONFIRMED as quotient-ring maps, not point bijections. Guard omega=W t5 s^8, inverse-polynomiality and gauges come from the unchanged 16r formulas: CONFIRMED.

## E. Scale normalization (15)-(17): CONFIRMED, every scaling replayed

Ahat=s^3 A(S,vartheta/s)=S vartheta^3+(S Dpar-U)vartheta^2+(z-U Dpar+S Vpar)vartheta+Kpar with U=su, Dpar=sd, Vpar=s^2 v, Kpar=s^3 k, z=s^2: CONFIRMED. Pihat=s^3 Pi(S,vartheta/s)=z vartheta-U vartheta^2+S vartheta^3. Bracket: Ahat_S=s^3 A_S, Ahat_vartheta=s^2 A_t, Bhat_S=s^5 B_S, Bhat_vartheta=s^4 B_t, so [Ahat,Bhat]=s^7[A,B]=s^7 Delta=s^7+U s^5 vartheta-E vartheta Pihat-vartheta Pihat^2 with E=s^3 ell: (16) CONFIRMED, targets s^7 and U s^5 exact. Leading: theta_new=s theta_old, Ahat_7=S^7(theta^3+sF theta^2+s^2 H theta+s^3 a)=S^7 c(theta)/W, Dbar=d/t5, Bhat5=S^2, Ahat3=S: CONFIRMED. Band coefficients scale by s^(3-i) (U) and s^(5-i) (V), so rho scales by s^8 including the V_part(0) subtraction, X_i=s^8 Y_i: CONFIRMED. Residual pair (s^6 r1, s^7 r0) (s^7 times the band, theta^1 divided by s); columns (s^3 c1, s^4 c0) (variable scaled by s^3 for k2,k1,ell); Psihat=s^10 Psi: CONFIRMED. Critical witnesses: own s-order of P5,P6 gives lambda1 ~ s^3, lambda0 ~ s^4, so normalized witnesses lie in B: CONFIRMED. K1_i=s^6 E1[S^i] (i>=1), K1_0-U s^5=s^6 E1[S^0], K0_i=s^7 E0[S^i], K0_0-s^7=s^7 E0[S^0]: (20) is (14) times units: CONFIRMED.

## F. Weighted envelopes (18)-(21): CONFIRMED

Weights S=1, vartheta=2, X1,X2,X3=1,2,3, z=5, E=7; [S^i]Dpar 2-i, [S^i]Vpar 4-i, [S^i]Kpar 7-i, U=3. Every monomial of Ahat has weight 7 (S vartheta^3:7; S Dpar vartheta^2: (2-i)+(i+1)+4; U vartheta^2: 7; z vartheta: 7; U Dpar vartheta: 3+(2-i)+i+2; S Vpar vartheta: (4-i)+(i+1)+2; Kpar: 7): CONFIRMED. Pihat weight 7, upper targets weight 16, the low targets s^7, U s^5 vartheta are not weight-16 (s has no integral weight) and enter only rows t^0, t^1, kept separate in (20): CONFIRMED. Gap weights: 1,2,3 (linear in X_h with B coefficients), 4 (shift U*[S]Dpar weight 4, H7bar a B-unit), 5 (y=z-U d0 weight 5, target -2z theta^5), 6 (U^2 and -U^2 theta^5 weight 6), 7 (E): CONFIRMED; only B constants inverted. Envelopes deg_S Ahat_j<=7-2j (7,5,3,1), deg_S Bhat_j<=12-2j (12,10,8,6,4,2), Jacobian deg_S[t^j]<=16-2j giving 17+15+13+11+9+7+5+3=80 slots versus 32 residual slots; K1_i weight 14-i, K0_i weight 16-i; ordinary degree a1+a2+a3+d<=a1+2a2+3a3+5d=w; coefficients in the basis 1,Z,..,Z^6: CONFIRMED. No height, time, certificate or dimension claim appears: CONFIRMED.

## G. Controls and checker contract: CONFIRMED

Controls 1-8 are genuine changed-object controls (forcing 1, unshifted v0, D_(i+1) blind to the k column, j=0 gauge with coincident contacts, dropped compatibility leaves (-lambda0,lambda1)Psi, deleted theta^4 target removes (10)-(12), s=1 discards the s^7/U s^5 factors and s^10, fieldness is not properness). Checker contract (P7 read-back, every inverse over the full basis, band maps with actual forcing, all 32 residuals and omega ab-1 modulo the 19 rows, inverse-polynomiality) is stated without any computed cofactor, row array or PASS: CONFIRMED. No degree frontier, general family, all-r F10 or JC2 inference is made.

## Verdicts

| item | verdict |
|---|---|
| A leading ring, gauges, guard, recurrence, bounds | CONFIRMED |
| B seven band maps | CONFIRMED except the late operator display (-18 must be -6); corrected scope given, theorem intact |
| C ell column (10)-(13) | CONFIRMED by independent hand derivation |
| D 19 slots, two quotient maps | CONFIRMED |
| E scale normalization | CONFIRMED, every scaling replayed |
| F weighted envelopes | CONFIRMED |
| G controls, checker contract | CONFIRMED |

Smallest defect: the single coefficient -18 in Llate (section 6), a display slip that contradicts the report own pivots -4,-11,-18; corrected operator 7CV-6CV+kD. It is not theorem-breaking because the column ideal is imported from 17v and the rows come from (3). No other equality failed replay. GAP (unchanged, honest): all inverse constants, Bezout cofactors and rows remain uncomputed; existence only, no certificate. REFUTED: the -18 display only.

## OPEN(S) RAISED

None. The sole remaining quantity is the producer own: whether the full quotient (1) with all 19 rows (20) is zero; cheapest prerequisite is the independent finite reconstruction and inverse read-back over the full B basis. No computation is requested or authorized here; no follow-on authority.

## COLLISIONS

status: EMPTY

- NONE. Own-only check: this lane wrote exactly xmodel/f10-r2-full-source-gate-fable5-20260910.md and box/f10-r2-full-source-gate-fable5-20260910/input_custody.md, both absent at 08:54:31Z; all writes by apply_patch; no Seal, no charge_basis, no corpus scan, no other lane, no network, no subprocess beyond documentary metadata.

## Completion

Authoring attestation: every byte of both owned files was written by apply_patch; no Write/Edit tool, heredoc redirection or script. Own WHOLE read of this report (sections 0, A-G, Verdicts, OPEN(S) RAISED none, COLLISIONS EMPTY) done before the marker. Two typed custody rows (critical-band gate, septic-irred gate) contained typing slips; both were corrected by apply_patch and all 24 rows were rechecked row by row against live sha256sum at 08:57:54Z: 24/24 match. This report body contains no hex digest; the digests live only in box/input_custody.md. Timeline: first action 08:47:55Z, skeleton 08:56:42Z, marker 08:57:27Z before the 09:00:00Z reserve, ROOT TERM 09:02:00Z, never reset. The marker below is the only standalone marker in this file and nothing follows it. All writers idle at the marker.

<!-- BODY-END -->
