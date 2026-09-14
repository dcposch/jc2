# f10 r1 third-band gate (fable5, 2026-09-09)

lane=f10-r1-third-band-gate-fable5-20260909
launch=2026-09-09T17:47:20Z (first action) controlling_stop=2026-09-09T18:02:00Z (earlier than launch+16m=18:03:20Z). Never reset.
owner_writes=xmodel/f10-r1-third-band-gate-fable5-20260909.md, box/f10-r1-third-band-gate-fable5-20260909/ (dir created, empty).
tools_used=date, ls, sha256sum, head -c (body-hash custody only), mkdir, Read (five inputs WHOLE, in parallel), apply_patch. ZERO CAS, zero arithmetic/mathematical subprocess of any size, zero network/SSH/AWS/process census/agents, zero code read or execution. Every number below is hand algebra shown inline.

## 0. Input custody (ordered, checked 17:47:20Z before reading)

| # | file | sha256 | status |
|---|------|--------|--------|
| 1 | f10-r1-third-band-astra-20260909.md (17b-successor, under review) | 440a66c3e51bc401d3133c49a12edb1894ee6503f43da86b25fb011723fc55a6 | MATCH |
| 2 | f10-r1-third-band-astra-20260909.md.artifact.json | b181b33fc435d1898cba1ef6716b7517010cb8bf4e0670047d61e4680e01c8df | MATCH |
| 3 | f10-whole-mate-euler-elimination-astra-20260909.md (accepted 16r) | a5ab487c4619742b6252e2503488eea4d6e927b58fd2821207cc85bcba7cf8d5 | MATCH |
| 4 | f10-r1-leading-coefficient-compression-astra-20260909.md | ead39705189f7faf338bab7937488e96c3ddf296c9ba0eed328ea63442619fb7 | MATCH |
| 5 | f10-r1-leading-univariate-gate-fable5-20260909.md (accepted 17b) | 1708746e6d54d745b7a33df54dd339b197df7ec33b1a67c79877ab2429e6946e | MATCH |

Artifact custody: input 2 records body_bytes 15437, body_sha256 964297c57043988378a3c08b09b994f986fac431ae1ea1328acd176b1847bd26, full_sha256 equal to row 1. Own `head -c 15437 | sha256sum` of input 1 reproduces 964297c5...bd26 exactly, and the Seal in input 1 quotes the same two values. MATCH. Accepted scope used: 16r sections 2-7 (normalization, (3),(5),(6),(11),(12), beta=gamma=0 gauge, L_r) and 17b sections B-C (Lambda=B[s,s^-1], units s,w,f5,L,a,b, D1..D5, 17 retained rows). No first-band or second-band theorem, coefficient or row is imported: J,K below are re-derived from 16r's (5) only.

## A. Homogeneous pieces, recurrences, weight 6, N_i, (13),(14),(15): CONFIRMED except (12) REFUTED as printed (index misprint, corrected below); one wording defect

Grading S:1, t:1, theta=t/S, r=1 (m=4,n=7). From 16r (3) with k0=0: f=-u+d0 S+d1 S^2, h=(1-u d0)+(v0-u d1)S+v1 S^2+v2 S^3, k=k1 S+k2 S^2+k3 S^3+k4 S^4. Sorting A=S t^3+f t^2+h t+k by weight: weight 4 = S^4(theta^3+F theta^2+H theta+a) with F=d1,H=v2,a=k4 (C as in input 1, the theta-reversal of 17b's C(T), T=1/theta); weight 3 = S^3(d0 theta^2+v1 theta+k3)=S^3 Z; weight 2 = S^2(-u theta^2+(v0-uF)theta+k2)=S^2 X; weight 1 = S(y theta+k1), y=h(0)=1-u d0; weight 0 = k0 = 0. (2) CONFIRMED. B: B5=S^2 gives S^7 theta^5, so B7=S^7 D, D_5=1, D_0=[S^7]B_0=b, D_i(here)=D_(5-i)(17b). (4): J_i=[S^(6-i)]B_i so J_5=[S]B_5=0, deg J<=4; K_i=[S^(5-i)]B_i, K_5=[S^0]B_5=0, deg K<=4; V_i=[S^(4-i)]B_i, V_5=0, V_4=[S^0]B_4, V_3=[S]B_3. CONFIRMED.

Identity (3), own derivation: for P=S^i f(theta), Q=S^j g(theta): P_S=S^(i-1)(i f-theta f'), P_t=S^(i-1)f', likewise Q; P_S Q_t-P_t Q_S=S^(i+j-2)[(i f-theta f')g'-f'(j g-theta g')]=S^(i+j-2)(i f g'-j f' g). CONFIRMED, orientation fixed.

Delta by weight, from 16r (4): delta_7 t^7=-S^2 t^7 weight 9; delta_6 t^6=2uS t^6 weight 7; delta_5 t^5=(-u^2-2S)t^5 weights 5 and 6; delta_4 t^4=(2u-ell S)t^4 weights 4,5; below that weights <=3. So weight 8 target is ZERO, weight 7 target 2u S^7 theta^6, weight 6 target -2 S^6 theta^5; ell first enters at weight 5. Pairs (i,j), i+j-2=weight: weight 9 (4,7) gives 4CD'-7C'D=-theta^7 = (1). Weight 8 (4,6),(3,7): 4CJ'-6C'J+3ZD'-7Z'D=0 = (5) with zero target. Weight 7 (4,5),(3,6),(2,7): (6) with the -2u theta^6 moved left. Weight 6 (4,4),(3,5),(2,6),(1,7): 4CV'-4C'V+[3ZK'-5Z'K+2XJ'-6X'J]+YD'-7Y'D=-2theta^5, i.e. (8),(9). No pair omitted. CONFIRMED, target -2theta^5 exact.

Diagonals: [theta^(j+2)](4CJ'-6C'J) from theta^3 in C is (4j-18)J_j = -2,-6,-10,-14,-18, and equals 16r's E_j eigenvalue on S^(6-j): j-3(6-j)=4j-18. Likewise (4j-15)K_j = 1,-3,-7,-11,-15 = j-3(5-j); and (4j-12)V_j = 4,0,-4,-8,-12 = j-3(4-j). All J,K pivots nonzero, so J,K are defined by the five upper rows of (5),(6) alone; the theta^1,theta^0 rows of each are the original [S^7]E1,[S^8]E0 and [S^6]E1,[S^7]E0 and are NOT imposed here. CONFIRMED.

(7): [theta^6](5) = -2J4+3 d0*5-7*2 d0 = -2J4+d0, so J4=d0/2 (=e_0 of 16r (6), CONFIRMED). [theta^6](6): K4*1+[2XD'-7X'D]_6-2u+[3ZJ'-6Z'J]_6 = K4+(2(-u)5-7(-2u)(1))-2u+0 = K4+4u-2u, so K4=-2u (=[S]B_4 of 16r (6)). theta^7 rows empty by degree (3+3, 2+4, 2+4, 1+5). CONFIRMED.

V5=V4=V3=0: V5=[S^-1]B5=0; V4=[S^0]B_4: 16r's j=4 row at [S^0] is 4[S^0]B_4=[S^0]Q_4 with Q_4=2uS-5dS^2+2(Sd-u)(2S)=-2uS-dS^2, constant term 0, so V4=0 is FORCED by the existing j=4 row (equivalently B_4=-2uS+S^2 e). V3=[S]B_3=beta=0 is the accepted 16r section 7 gauge. No new normalization. CONFIRMED. Wording defect: the theta^6 row of (9) is 4V_4=0 (V_3 never reaches theta^6: [theta^6](4CV'-4C'V) is 16V_4-12V_4), so "no theta^6 row because V3=0" should read "because V4=0". Smallest correction: replace V3 by V4 in that sentence. Nothing downstream changes.

W5, N5: [theta^5](3ZK'-5Z'K)=3 d0*4K4-5*2d0*K4=2 d0 K4; [theta^5](2XJ'-6X'J)=2(-u)4J4-6(-2u)J4=4u J4. W5=2d0(-2u)+4u(d0/2)=-2u d0. CONFIRMED. YD'-7Y'D=(y theta+k1)D'-7yD=y(theta D'-7D)+k1 D', [theta^i](theta D'-7D)=(i-7)D_i, so at theta^5: -2y; k1 D' has degree 4; V has degree 2 so 4CV'-4C'V has degree 4. theta^5 row of (9): -2y=-2-W5, i.e. N5=-2-W5+2y=-2+2u d0+2-2u d0=0. CONFIRMED (11). Independent cross-check through 16r: [S^1] of the t^5 row is E_3 B_3 term 0*beta plus 4[f'B_4]_1-2[fB_4']_1=4(-2u d0)-2(-2u e0-2u d0)=-2u d0, plus 5[h'B_5]_1-[hB_5']_1=0-2y; sum -2u d0-2y = delta_5 at S^1 = -2: identical to N5=0, and to 16r's first-resonance cancellation 2u d0-4u e0=0.

(12) REFUTED as printed. With N=-2theta^5-W-y(theta D'-7D) and N_i=[theta^i]N, the correct formula for i=0..4 is N_i=-W_i-(i-7) y D_i = -W_i+(7-i) y D_i (N_4=-W_4+3yD_4, ..., N_0=-W_0+7yb). The printed -y(i-6)D_(i+1) is the theta^(i+1) coefficient shifted down; it contradicts the report's own (11) at i=5 (it would give N5=-W5, missing 2y) and the 16r cross-check ([S^(4-j)] of -yB'_(j+2) is -(5-j)yD_(j+2)). Smallest correction: one-line replacement of (12). Downstream (13)-(21) use N_i only as k1-independent symbols, so no other line changes. N_i are k1-free: W depends on Z,X,J,K (built from d0,v1,k3,u,v0,k2 and Lambda), y=1-u d0. CONFIRMED.

(13),(14): 4CV'-4C'V for V=V2 theta^2+V1 theta+V0 equals -4V2 theta^4-8V1 theta^3+(-12V0-4FV1+4HV2)theta^2+(8aV2-8FV0)theta+(4aV1-4HV0), own expansion. k1 D' contributes 5k,4D4 k,3D3 k,2D2 k,D1 k at theta^4..theta^0. Rows theta^4,3,2 give (13) verbatim; rows theta^1,theta^0 give (14) verbatim. Indexing: S^6 theta=S^5 t so theta^1 is [S^5]E1, theta^0 is [S^6]E0. CONFIRMED. (15): at N=0, V2=5k/4, V1=D4 k/2, V0=k(-2FD4+5H+3D3)/12=k zeta; h1=8a(5/4)-8F zeta+2D2, h0=4a(D4/2)-4H zeta+D1. CONFIRMED verbatim.

## B. Left inverse (16)-(20): CONFIRMED

With N=0 and V=V_h the theta^5,4,3,2 rows of (10) vanish (theta^5: both sides degree<=4; theta^4: -5k+5k; theta^3: -4D4k+4D4k; theta^2: -12k zeta-2FD4k+5Hk+3D3k=0), so 4CV'-4C'V+kD'=r1 theta+r0 exactly, r=hk. T=4CV-7kD, deg<=max(3+2,5)=5, T5=4(5k/4)-7k=-2k (18). T'=4C'V+4CV'-7kD'=4C'V+(4C'V-kD'+r1theta+r0)-7kD'=8(C'V-kD')+r1theta+r0. CT'-2C'T=8CC'V-8kCD'+C(r1theta+r0)-8CC'V+14kC'D=2k(7C'D-4CD')+C(r1theta+r0)=2k theta^7+C(r1theta+r0) by (1). (17) CONFIRMED. (T/C^2)'=(CT'-2C'T)/C^3; C(0)=a=1/(w s^3) is a unit of Lambda, so C^-2,C^-3 are formal series with coefficients in Q[F,H,a,a^-1]; e_i=[theta^i]C^-2 needs only a^-2 (e0=a^-2). (r1theta+r0)C^-2=sum(r0 e_i+r1 e_(i-1))theta^i; formal antiderivative = sum_(i>=1)(r0 e_(i-1)+r1 e_(i-2))theta^i/i = I_r through i=6 (uses e_0..e_5 only). The 2k theta^7 C^-3 term integrates into degree>=8. Hence T=C^2(T0/a^2+I_r) mod theta^7 (19), a correct truncation at degree 6. [theta^6]C^2=1, [theta^5]C^2=2F: degree 6 gives 0=T0/a^2+P6(r); degree 5 gives -2k=2F(T0/a^2)+P5(r)=-2F P6(r)+P5(r), so k=F P6(r)-P5(r)/2=lambda(r) with r=hk. Lambda-linearity and k an indeterminate give lambda(h)=1 in Lambda (20): a polynomial identity, valid in every Lambda-algebra including nonreduced B. Only a and rationals 1/i (i<=6) inverted; no field factor, no existential minor, no analytic branch. Kernel: r=0 forces k=lambda(0)=0. CONFIRMED.

## C. Determinant-one transformation, k1=-lambda(c), Psi, quotient map, 16 slots: CONFIRMED

lambda(r)=lambda1 r1+lambda0 r0, lambda1 h1+lambda0 h0=1. P=[[lambda1,lambda0],[-h0,h1]] has det lambda1 h1+lambda0 h0=1, entries in Lambda (h_i,lambda_i are Q[F,H,a,a^-1]-expressions in Lambda), so P is in GL_2(Lambda) and of the ambient ring. P(hk+c)=(k lambda(h)+lambda(c), -h0(h1k+c1)+h1(h0k+c0))=(k+lambda(c), -h0c1+h1c0): (21) CONFIRMED, k cancels in the second row. R=0 iff PR=0 iff k1=-lambda(c) and Psi=0. c=R|_(k1=0): c1=8aV2^0-8FV0^0-N1, c0=4aV1^0-4HV0^0-N0 with V2^0=-N4/4, V1^0=-N3/8, V0^0=(-4FV1^0+4HV2^0-N2)/12, a definite element of Lambda[u,d0,v0,v1,k2,k3] (ell-free), not a free pair. Quotient map: O=Lambda[u,ell,d0,v0,v1,k1,k2,k3]/(17b rows) -> O'=Lambda[u,ell,d0,v0,v1,k2,k3]/(other 15 rows at k1=-lambda(c), Psi), k1 |-> -lambda(c); inverse is the inclusion of the seven-variable ring followed by the quotient, since (R1,R0)=(k1+lambda(c),Psi) as ideals and k1+lambda(c) is monic linear in k1 with k1-free tail. Both directions CONFIRMED. Affineness in k1 of exactly the weight-6 rows: J,K come from weights 8,7 which contain A4,A3,A2 only; V from (13) is affine in k1; ell enters first at weight 5. Row count: 17b rows are [S^0..7]E1, [S^0..8]E0; remove [S^5]E1,[S^6]E0, add Psi: E1 0-4,6,7 (7), E0 0-5,7,8 (8), Psi (1) = 16. Seven lower parameters u,ell,d0,v0,v1,k2,k3 plus unit s over B. CONFIRMED. Nothing composed with first/second band; no emitted row, point, unit, properness, exclusion or speedup claimed, and none is licensed here.

## D. Controls: CONFIRMED as algebraic changed-object controls; no attainment claim

Target control: delete -2S t^5, then N5=-W5+2y=2u d0+2-2u d0=2, parameter-free, and the theta^5 row (which has no k1 and no V) reads 0=2. This is a row-operation control on the equation, not a source point. CONFIRMED. W5 control: W:=0 gives N5=-2+2(1-u d0)=-2u d0, so the earlier-band nonlinear forcing is load-bearing except on u d0=0. CONFIRMED. Residual-vector control: r*=(-lambda0,lambda1): lambda(r*)=-lambda1 lambda0+lambda0 lambda1=0 and -h0(-lambda0)+h1 lambda1=1. So r* is killed by the first transformed row and not by the second; dropping Psi loses it. The producer correctly states r* is NOT asserted attained by the parameters and that Psi's nonvanishing/independence is unchecked; neither is required for (21). CONFIRMED. Distinction kept: every control above is an algebraic operation on rows in Lambda[...], none an attained source-parameter point. Defects found: two, both typographical ((12) index; V3/V4 wording), each with its smallest correction in A; no implementation, no higher band. Existing code untouched and unexecuted.

## Read scope, limitations

Read: exactly the five charged inputs, WHOLE, after hash match; nothing else (no corpus, provenance, code, data, peer body, earlier band reports). Not verified by me: numerical values of D2..D4 in Lambda (taken as 17b's accepted recurrence outputs; only D5=1, D0=b and the structural degrees enter above); explicit expansion of c, Psi, lambda_i (not needed for the verdicts and not claimed by the producer). Every calculation here is manual; no tool computed any coefficient.

## OPEN(S) RAISED

None. (The (12) misprint is a defect with an exact one-line correction, not an open quantity.)

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN check (this report and its box only); no corpus scan.

## GAPs and own whole-read check

Verdicts: A CONFIRMED except (12) REFUTED as printed (index misprint; correct N_i=-W_i+(7-i) y D_i, i=0..4) plus one V3/V4 wording defect, both with smallest corrections and no downstream effect; B CONFIRMED; C CONFIRMED; D CONFIRMED.

GAPs (left open, not filled, none blocking the verdicts): (i) no explicit expansion of c, Psi, lambda0, lambda1 or e_1..e_5 was done by anyone; (ii) whether Psi is a nonzero polynomial of the seven retained parameters, or independent of the other 15 rows, is unchecked (explicitly not claimed by the producer); (iii) reducedness/properness of the 16-row retained system untouched; (iv) D1..D4 taken as 17b's accepted recurrence outputs, not re-derived here. No Seal and no charge_basis are authored here; no exit claim is made.

Own whole-read at 17:54:34Z (sed -n, full file): sections 0, A, B, C, D, read scope, OPEN(S) RAISED (none), COLLISIONS (EMPTY, own-only), this section. Hex-token cross-check: the six 64-hex tokens in this file are exactly the five input hashes plus the producer body hash reproduced by own head -c. No marker before the next line; nothing follows it.

<!-- BODY-END -->
