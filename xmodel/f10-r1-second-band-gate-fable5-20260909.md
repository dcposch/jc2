# f10 r1 second-band gate (fable5, 2026-09-09)

lane=f10-r1-second-band-gate-fable5-20260909
launch=2026-09-09T17:37:14Z stop=2026-09-09T17:56:00Z (original absolute stop, earlier than launch+20m=17:57:14Z)
owner_writes=xmodel/f10-r1-second-band-gate-fable5-20260909.md, box/f10-r1-second-band-gate-fable5-20260909/
tools_used=date, ls, sha256sum, Read (five inputs WHOLE, in parallel), apply_patch (all writes). ZERO CAS, zero arithmetic subprocess, zero network, zero process census, no code edits.

## 0. Input custody (checked 17:37:14Z, before any read)

| # | file | sha256 | status |
|---|------|--------|--------|
| 1 | f10-r1-second-subleading-band-astra-20260909.md | 3dc7a2503eff441b35745dd153a6b90a534dae63644b0afc3d6968799c9f559a | MATCH |
| 2 | f10-r1-second-subleading-band-astra-20260909.md.artifact.json | e4841159534bc3ba93c021f0ac9460ccc5457f61b7a1a18b82233c2e9825fdbf | MATCH |
| 3 | f10-whole-mate-euler-elimination-astra-20260909.md (accepted 16r) | a5ab487c4619742b6252e2503488eea4d6e927b58fd2821207cc85bcba7cf8d5 | MATCH |
| 4 | f10-r1-leading-coefficient-compression-astra-20260909.md (17b) | ead39705189f7faf338bab7937488e96c3ddf296c9ba0eed328ea63442619fb7 | MATCH |
| 5 | f10-r1-leading-univariate-gate-fable5-20260909.md (17b gate) | 1708746e6d54d745b7a33df54dd339b197df7ec33b1a67c79877ab2429e6946e | MATCH |

Input 2 records body_sha256 8ee7676df4c15b55df21c7127dbca9b90b4d506b6e40489b556780a3fd4d4e6d and body_bytes 13647, equal to the Seal of input 1; not independently rehashed (the body-only hash is not a charged pin). Inputs 3-5 are consumed as accepted 16r/17b mathematics, not re-gated. Nothing else was read: no first-band report, no peer, no code, no ledger.

## A. Literal weight-seven extraction

Verdict: CONFIRMED (own extraction; every displayed coefficient reproduced).

Setup (own, from 16r (3),(4) at r=1, m=4, n=7, k0=0): f=-u+d0 S+d1 S^2, h=(1-u d0)+(v0-u d1)S+v1 S^2+v2 S^3, k=k1 S+k2 S^2+k3 S^3+k4 S^4. With F=d1,H=v2,a=k4 and theta=t/S (wt S=wt t=1) the weight pieces of A are A4=S^4(theta^3+F theta^2+H theta+a)=S^4 C, A3=S^3(d0 theta^2+v1 theta+k3)=S^3 Z, A2=S^2(-u theta^2+(v0-uF)theta+k2)=S^2 U, A1=S((1-u d0)theta+k1), no A0. So q=-u, l=v0-uF=v0+Fq, k=k2: input 1's (2) CONFIRMED; the change (u,v0,k2)->(q,l,k) is unimodular over Lambda (F in Lambda).

B-pieces: deg B_j<=7-j gives top weight 7. B7=S^7 D(theta), D_j=[S^(7-j)]B_j, D5=[S^2]B_5=1, D0=[S^7]B_0=b. Producer's D_i^(17b)=[S^(2+i)]B_(5-i)=D_(5-i) here: reversed indexing CONFIRMED (e.g. D4 here = 17b's D1 = 6F/5 = e_1 of 16r (6)). B6=S^6 J, J_j=[S^(6-j)]B_j, J5=[S]B_5=0 so deg J<=4; B5band=S^5 V, V_j=[S^(5-j)]B_j, V5=0 so deg V<=4. B_5(S)=S^2 unchanged. CONFIRMED.

Graded bracket (own): for A_i=S^i P(theta), B_j=S^j Q(theta), theta_S=-theta/S, theta_t=1/S give [A_i,B_j]=S^(i+j-2)(i P Q'-j P' Q). Weight 9: S^9(4CD'-7C'D); target delta_7 t^7=-S^2 t^7=-S^9 theta^7, so 4CD'-7C'D=-theta^7; check [theta^7]: 4*1*5-7*3*1=-1. (1) CONFIRMED (sign and theta^7). Weight 8: pairs (4,6),(3,7) only: 4CJ'-6C'J+3ZD'-7Z'D; target weight 8 is empty (delta_6 t^6=2uS t^6 has weight 7, delta_5 t^5 weights 5,6). Weight 7: pairs (4,5),(3,6),(2,7); (1,8) is empty; target 2uS t^6=2u S^7 theta^6=-2q S^7 theta^6. Hence 4CV'-5C'V+2UD'-7U'D=-2q theta^6-W with W=3ZJ'-6Z'J: (4),(5) CONFIRMED; the target is NOT zero and enters only at theta^6.

Coefficient rule (own): [theta^N](alpha C X'-beta C'X)=sum_(i+h=N+1)(alpha h-beta i)c_i X_h with c=(a,H,F,1) by theta power. J recurrence at theta^(j+2): (4j-18)J_j+(4j-8)F J_(j+1)+(4j+2)H J_(j+2)+(4j+12)a J_(j+3)+sum_i(3(j+3-i)-7i)Z_i D_(j+3-i)=0, and 3(j+3-i)-7i=3j+9-10i. (3) CONFIRMED verbatim; diagonals -2,-6,-10,-14,-18. Top degree of the weight-8 polynomial is 6 (CJ',C'J,ZD',Z'D all <=6), so j=4..0 use theta^6..theta^2 and the theta^1,theta^0 slots are S^7 t and S^8: exactly the first-band rows [S^7]E1,[S^8]E0, which stay unimposed. j=4 gives -2J4=-(21-20)d0*D5, J4=d0/2=[S^2]B_4=e_0 of 16r: consistent. J is Lambda-linear homogeneous in (d0,v1,k3) (only forcing is ZD).

W: [theta^5]W=3*4 d0 J4-6*2 d0 J4=0, so deg W<=4, W5=W6=0; W quadratic homogeneous in Z. CONFIRMED.

V recurrence (own, rule (4h-5i) on c_i V_h, (2h-7i) on U_i D_h, i+h=j+3, coefficient 4j-15 on V_j): theta^6: V4+(10-14)q=-2q so V4=2q=-2u=[S]B_4 of 16r (6). theta^5: -3V3+(16-10)F V4+(8-14)q D4+(10-7)l=-W5. theta^4: -7V2+(12-10)F V3+(16-5)H V4+(6-14)q D3+(8-7)l D4+10k=-W4. theta^3: -11V1+(8-10)F V2+(12-5)H V3+16a V4+(4-14)q D2+(6-7)l D3+8k D4=-W3. theta^2: -15V0+(4-10)F V1+(8-5)H V2+12a V3+(2-14)q D1+(4-7)l D2+6k D3=-W2. Solving reproduces (6) term by term including 6F,3l,-6D4q; 2F,11H,10k,D4 l,-8D3 q; -2F,7H,16a,8D4 k,-D3 l,-10D2 q; -6F,3H,12a,6D3 k,-3D2 l,-12D1 q. CONFIRMED.

Residuals: theta^1 (i+h=2): 8a V2-H V1-10F V0+4D2 k-5D1 l-14b q+W1; theta^0 (i+h=1): 4a V1-5H V0+2D1 k-7b l+W0. (7) CONFIRMED. Slots: S^7 theta=S^6 t is [S^6]E1_res and S^7 is [S^7]E0_res of 16r (12); the weight-7 part of delta_1=u is empty, so no target enters these two slots. Independence: ell sits in delta_2..delta_4 (weights 2-5) and k1 in A1, whose partner B8 is empty; neither enters. d0,v1,k3 enter only through Z,W and are never solved. CONFIRMED.

## B. Homogeneous kernel (8)-(12) over Lambda-algebras

Verdict: CONFIRMED (own rederivation; rank 2 and unit det N hold in every residue field of Lambda=B[s,s^-1]).

T derivative: T=4CV-7DU, deg<=7. T'=4C'V+4CV'-7D'U-7DU'; (8) gives 4CV'-7DU'=-2q theta^6+5C'V-2UD', so T'=9(C'V-D'U)-2q theta^6. CONFIRMED.

Inversions: the linear system 4C V-7D U=T, 9C' V-9D' U=T~:=T'+2q theta^6 has determinant -36CD'+63C'D=9(7C'D-4CD')=9 theta^7 by (1) (an identity in Lambda[theta], input 5 section C). Cramer: V=(7D T~-9D'T)/(9 theta^7), U=(4C T~-9C'T)/(9 theta^7), i.e. (9) with N_U=(4/9)C T~-C'T, N_V=(7/9)D T~-D'T. 9 theta^7 is a unit times a monic, hence a non-zero-divisor in every Lambda-algebra: recovering the system from (9) is licit. CONFIRMED.

h recurrence: [theta^N]((4/9)CT'-C'T)=(1/9)sum_(j+i=N+1)(4i-9j)c_j T_i, c_0=a,c_1=H,c_2=F,c_3=1. For N<=5 the q term is absent; with i=N+1: 4i a T_i=-(4i-13)H T_(i-1)-(4i-26)F T_(i-2)-(4i-39)T_(i-3). This is (10) verbatim (j=1,2,3 give 13j=13,26,39), so T_i=T0 h_i for i<=6; h_1=9H/(4a)=[theta](C/a)^(9/4) checks the shorthand. At N=6 the extra term is (8/9)q c_0: 28a T7+15H T6+2F T5-11T4+8qa=0, and the i=7 instance of (10) turns this into T7=T0 h7-(2/7)q. Leading coefficient of U: deg N_U<=9 and [theta^9]N_U=(1/9)(28-27)T7+(8/9)q=(T7+8q)/9; equating to q gives T7=q, hence q=(7/9)T0 h7. (11) CONFIRMED; the naive truncation T7=T0 h7 would give q=T0 h7/9 instead, so the target term is load-bearing.

Divisibility and converse: with T=T_star (T0=1, q=q_star=7h7/9) the theta^0..theta^5 coefficients of N_U vanish by (10) and the theta^6 coefficient is a(28q_star-28h7+8q_star)=a(36*7/9-28)h7=0. deg N_U<=9 gives deg U_star<=2 with [theta^2]U_star=q_star. Identity C N_V-(7/4)D N_U=-CD'T+(7/4)C'DT=(T/4)(7C'D-4CD')=(theta^7/4)T: CONFIRMED; C(0)=a is a unit in every Lambda-algebra, so N_V is divisible by theta^7, deg N_V<=11, deg V_star<=4. Substitution back recovers (8) as shown. Converse: any solution of (8) over any Lambda-algebra gives T with (9), and polynomiality of U forces (10) for i<=6, (11) and [theta^2]U=q, so T=T0 T_star and (U,V)=T0(U_star,V_star) by linearity of (9) in (T,q). CONFIRMED, nonreduced algebras included (only fixed rationals and the unit a are inverted).

beta (own, [theta^(7+m)]N_U with c_j and the (8/9)q c_(N-6) term): m=2: (1/9)(28-27)q_star+(8/9)q_star=q_star. m=1: (1/9)[(24-27)h6+(28-18)F q_star]+(8/9)F q_star=2F q_star-h6/3. m=0: (1/9)[(20-27)h5+(24-18)F h6+(28-9)H q_star]+(8/9)H q_star=3H q_star+(2/3)F h6-(7/9)h5. All three of (12) CONFIRMED.

Rank in every residue field kappa (char 0, since Lambda is a Q-algebra): if U_star=0 in kappa then q_star=0, so T_star has degree d<=6 and T_star(0)=1 forces T_star!=0; N_U=0 with q=0 reads 4CT'-9C'T=0 whose theta^(d+2) coefficient is (4d-27)T_d (C monic cubic); 4d-27 is odd, never zero, contradiction. So beta!=0 in every kappa; no generic v, simple-root or selected-factor assumption. ker M over kappa = {U : (U,V^h(U)) solves (8)} = kappa*beta by the converse, so rank M=2 in every kappa. CONFIRMED. The maximal minors generate (1) in Lambda; no single 2x2 minor is claimed a unit, and none is computed here either.

rho and det N: rho(U)=4a V^h_0(U)-7b k=[theta^0](4CV-7DU); on beta this is T_star(0)=h0=1 (V^h(beta)=V_star because (U_star,V_star) solves (8) and the five diagonals 1,-3,-7,-11,-15 make V unique). Over each kappa, N x=0 gives x=c beta then c=rho(x)=0, so N is invertible over every residue field; det N in Lambda lies in no maximal ideal, hence is a unit. This is the completed 3x3 determinant argument, valid without computing it; CONFIRMED as stated. N^-1=adj(N)/det N is defined over Lambda.

## C. Exact affine quotient-ring maps (13),(14)

Verdict: CONFIRMED (as a standalone presentation; nothing emitted, no point/unit/properness/speedup asserted or checked).

c(Z): with U=0 the recurrence (6) gives V4=0, V3=W5/3=0, V2=W4/7, V1=(-2F V2+W3)/11, V0=(-6F V1+3H V2+W2)/15, and then c1=8a V2-H V1-10F V0+W1, c0=4a V1-5H V0+W0. This is the ENTIRE forcing: every inhomogeneous term of (6),(7) is a W_i, and the W_i are the only Z-dependence, so c(Z) in Lambda[d0,v1,k3] is quadratic homogeneous and contains no new symbol. M (the U=0-free part) has entries in Lambda only: F,H,a,b,D1..D5. CONFIRMED.

Coordinate change: (q,l,k) -> (R1-c1,R0-c0,rho(U)) = N U is Lambda-linear with det N a unit (B), so U -> (R1,R0,Y) is an invertible affine change over Lambda[Z]; composing with the unimodular (u,v0,k2)<->(q,l,k) of A gives (14) with inverse read-back (13). Quotienting Lambda[Z,ell,k1][u,v0,k2] by (R1,R0) is therefore isomorphic to Lambda[Z,ell,k1][Y] with Y a free polynomial coordinate, not a gauge: two solutions with the same Z differ by Y only, and Y=rho(U) is an honest function of the original unknowns. CONFIRMED. No division by u, by a first-band residual or by a Z-dependent quantity occurs; N^-1 involves only Lambda.

Retention: 17b's 17 slots are [S^0..S^7]E1_res and [S^0..S^8]E0_res. Solving [S^6]E1 and [S^7]E0 leaves [S^0..S^5]E1 (6), [S^7]E1 (1), [S^0..S^6]E0 (7), [S^8]E0 (1): 15 slots, an envelope not a count of nonzero rows. Both first-band rows [S^7]E1,[S^8]E0 (linear homogeneous in Z over Lambda, from the theta^1,theta^0 slots of the weight-8 polynomial of A) are retained unimposed; the mate coefficients, inverse-pole conditions (16r by parametrization/consequence, not by free d1,v2,k4), leading read-back (4) of 17b and omega=w s^8 f5 are transported by the same substitution. CONFIRMED as literal statement. No composition with any earlier elimination, no all-r or higher-band claim: input 1 restricts itself to r=1 and this band, and I checked nothing beyond.

## D. Changed-object controls and remaining doubts

Verdict: CONFIRMED (all three controls replayed by hand; they are upper-stage witnesses only).

Z=1 (d0=v1=0,k3=1): (3) at j=4: -2J4=-(21)Z0 D7=0; j=3: -6J3=-(18)Z0 D6=0; j=2: -10J2=-15 Z0 D5=-15, J2=3/2; j=1: -14J1=4F J2-12 D4=6F-12D4, J1=(6D4-3F)/7. W=3J'=9 theta+3J1, so W1=9, W0=3(6D4-3F)/7, W_i=0 for i>=2. With U=0, (6) gives V=0 and R1=W1=9, R0=W0. Dropping W gives V=0 and R1=R0=0 at the same object: false pass. CONFIRMED; the lower rows of this object are not asserted zero, so it is not a point.

Kernel shift: M beta=0 and rho(beta)=1, so adding beta to any solution of (14) keeps both affine rows and moves Y by 1: Y is a genuine free coordinate. Row necessity: N^-1(1,0,0)^T exists because det N is a unit; it violates R1 by exactly 1 while keeping R0=0 and Y=0, so deleting R1 (or symmetrically R0 via (0,1,0)) enlarges the solution set. CONFIRMED as an exact manual vector; it was not computed and need not be.

Missing target: at theta^6 the equation becomes V4-4q=0, V4=4q; in B the (8/9)qC theta^6 term disappears, [theta^9]N_U=T7/9 forces T7=9q and (11) becomes q=T0 h7/9. Different kernel and different V: CONFIRMED that the 2uS t^6 term is load-bearing.

Concrete remaining doubts (none blocks the verdicts):
- (d1) The Lambda-level identity (1) is imported from input 5 section C (chart-equivalence of q6=q7=0 in B[s,s^-1]); it was not re-derived here. Its failure would demote the Cramer determinant to a field-point identity but leave rank 2 in every residue field intact.
- (d2) No entry of N^-1, of c(Z), or of any of the 15 retained rows has been displayed by anyone; whether some retained slot is identically zero after (14) is unknown (envelope only).
- (d3) R0 at the Z=1 control equals 3(6D4-3F)/7, an element of Lambda not shown to be nonzero; the control uses only R1=9.
- (d4) d0,v1,k3 remain free in the target ring, so this band alone yields no reduced coordinate for the first band; any such step is a separate gate.

## OPEN(S) RAISED

None. Doubt (d2) is the read-back of the retained rows, which input 5 already raised as OPEN[F10-R1-RETAINED-ROWS-READBACK] (quantity <= 17 nonzero rows, cheapest test exact substitution read-back, wall <= 10 minutes if charged); it is consumed, not re-raised, and the 15-slot envelope here only lowers its bound by two.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN check (this report and its box only, grep for OPEN[ tokens at 17:45:18Z returned none); no corpus scan, no campaign-novelty claim.

## Scope, GAPs and own whole-read check

Read/tool scope: exactly the five charged inputs, whole, after the ordered hash match; no first-band report, peer, provenance, code, ledger, network or process census. Every number above is hand arithmetic shown inline; ZERO mathematical subprocess of any size; all writes via apply_patch. Terminal custody at 17:45:56Z: the five sha256 values are unchanged from 17:37:14Z.

Verdicts: A CONFIRMED (own graded-bracket extraction reproduces (1)-(7) with signs, D indexing, q=-u, l=v0+Fq, slots [S^6]E1/[S^7]E0, no ell/k1, d0/v1/k3 free, W and the -2q theta^6 target both retained); B CONFIRMED (T derivative, both Cramer inversions with determinant 9 theta^7, (10) verbatim, T7=T0 h7-(2/7)q and q=(7/9)T0 h7, all three beta entries, beta!=0 and rank M=2 in every residue field by the odd coefficient 4d-27, rho(beta)=1 and det N a unit by the residue-field argument on the completed 3x3 matrix); C CONFIRMED (c(Z) is the whole W-forcing, N U+(c,0) is an invertible affine change over Lambda[Z] making Y a free coordinate, 15-slot envelope with both first-band rows, mate, inverse conditions, leading read-back and omega retained; no artifact, point, unit, properness, speedup, composition or higher-band claim); D CONFIRMED (Z=1 gives J2=3/2, W1=9, R1=9 while W-less gives 0; beta shifts Y by 1; N^-1(1,0,0) shows row necessity; missing target gives V4=4q and q=T0 h7/9).

GAPs (left open, not filled): (i) doubt (d1), the Lambda-level status of (1), rests on input 5 section C and was not re-derived; (ii) no entry of N, N^-1, c(Z) or any retained row exists in explicit form anywhere; (iii) reducedness, properness, points or units of the 15-slot system are untouched; (iv) the first band (d0,v1,k3) stays free and any elimination there is a separate gate. This static manual verdict is not execution evidence. No Seal and no charge_basis are authored here.

Own whole-read at 17:45:18Z: sections 0, A, B, C, D, OPEN(S) RAISED, COLLISIONS, this section; marker count was 0 before this closing write. No marker before the next line.

<!-- BODY-END -->
