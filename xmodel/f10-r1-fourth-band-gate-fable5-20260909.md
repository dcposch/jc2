# f10 r1 fourth-band gate (fable5, 2026-09-09)

lane=f10-r1-fourth-band-gate-fable5-20260909
launch=2026-09-09T17:56:09Z stop=2026-09-09T18:13:00Z (earlier of 18:13:00Z and launch+18m=18:14:09Z, never reset)
owner_writes=xmodel/f10-r1-fourth-band-gate-fable5-20260909.md, box/f10-r1-fourth-band-gate-fable5-20260909/
tools_used=date, ls, sha256sum, cat (five inputs WHOLE, read in parallel), apply_patch (all writes). ZERO CAS, zero arithmetic subprocess, zero network, zero process census. Every number below is hand arithmetic shown inline.

## 0. Input custody (checked before reading)

| # | file | sha256 | status |
|---|------|--------|--------|
| 1 | f10-r1-fourth-band-astra-20260909.md (producer, under review) | 879d6ab9e951c90aa72c46bde3685789290bd38a057025d320f7eb5deb418a41 | MATCH |
| 2 | f10-r1-fourth-band-astra-20260909.md.artifact.json | c900e17ba29011edf4eca09f300f6e6a1a9dee25ce4e5f565f69a1856cfb8e94 | MATCH |
| 3 | f10-whole-mate-euler-elimination-astra-20260909.md (accepted 16r, premise) | a5ab487c4619742b6252e2503488eea4d6e927b58fd2821207cc85bcba7cf8d5 | MATCH |
| 4 | f10-r1-leading-coefficient-compression-astra-20260909.md (17b producer) | ead39705189f7faf338bab7937488e96c3ddf296c9ba0eed328ea63442619fb7 | MATCH |
| 5 | f10-r1-leading-univariate-gate-fable5-20260909.md (accepted 17b gate, premise) | 1708746e6d54d745b7a33df54dd339b197df7ec33b1a67c79877ab2429e6946e | MATCH |

Accepted 16r/17b are premises only; no earlier-band (weight 8,7,6) report or theorem is used. u,d0,v0,v1,k1,k2,k3,ell and every retained row stay independent. Read scope: exactly these five files, whole, after hash match; nothing else local, no provenance followers.

## A. Full affine ell response of the entire 16r reconstruction: CONFIRMED

Delta vector (own expansion). Pi=t-ut^2+St^3, Pi^2=t^2-2ut^3+(u^2+2S)t^4-2uSt^5+S^2t^6, so Delta=1+ut-ell t Pi-t Pi^2 = 1+ut-ell t^2+(ell u-1)t^3+(2u-ell S)t^4-(u^2+2S)t^5+2uSt^6-S^2t^7. All eight delta_j as displayed; d/d ell of the vector is (0,0,-1,u,-S,0,0,0). A=St^3+ft^2+ht+k is ell-free, B5=S^2 fixed, gauges beta=[S]B3=0 and gamma=B0(0)=0 are ell-independent constants, and 16r (5) is linear in (B_j) with fixed rational diagonal inverses. Hence every B_j is affine in ell and W_j=dB_j/d ell obeys (5) with delta replaced by its ell-derivative and W5=0.

j=4: forcing 0 (delta_6=2uS), E_4 eigenvalues 4-3i never 0, so W4=0. j=3: forcing 0 (delta_5 ell-free, W4=W5=0), kernel S is killed by the fixed gauge beta=0, so W3=0. j=2: E_2W2=-S, eigenvalue on S is 2-3=-1, W2=S. j=1: E_1W1=u-2f*S+2f with f=-u+d0S+FS^2, f*=d0+2FS (star = S-derivative): u-2d0S-4FS^2-2u+2d0S+2FS^2=-u-2FS^2; eigenvalues 1 on S^0 and 1-6=-5 on S^2, so W1=-u+(2F/5)S^2. j=0: E_0W0=-1-f*W1+2fW1*-2h*S+h with h=1-ud0+(v0-uF)S+v1S^2+HS^3, h*=(v0-uF)+2v1S+3HS^2, W1*=(4F/5)S. Terms: -f*W1=ud0+2uFS-(2Fd0/5)S^2-(4F^2/5)S^3; 2fW1*=-(8uF/5)S+(8Fd0/5)S^2+(8F^2/5)S^3; -2h*S=-2(v0-uF)S-4v1S^2-6HS^3. Constant: -1+ud0+(1-ud0)=0 (j=0 resonance automatic, gamma=0 fixes W0(0)=0). S: uF(2-8/5+2-1)-v0=(7uF/5-v0). S^2: (6Fd0/5-3v1). S^3: (4F^2/5-5H). Eigenvalues -3,-6,-9 give W0=(v0/3-7uF/15)S+(v1/2-Fd0/5)S^2+(25H-4F^2)S^3/45. Producer (2) CONFIRMED, both resonance constants and both gauges included; no division by any parameter.

Residuals (own extraction from the (lA_k*B_l-kA_kB_l*)t^(k+l-1) rule at k+l=2 and k+l=1): E1=2k*B2+h*B1-hB1*-2fB0*-u, E0=k*B1-hB0*-1, identical to 16r (12). Their ell-derivatives replace B_j by W_j: dE1/dell=2k*S+h*W1-hW1*-2fW0*, dE0/dell=k*W1-hW0*. With k*=k1+2k2S+3k3S^2+4aS^3 (deg 3), W1 deg 2, h deg 3, h* deg 2, f deg 2, W0* deg 2 with top (25H-4F^2)S^2/15: dE1/dell has degree exactly 4 and [S^4]=8a+(3H)(2F/5)-(H)(4F/5)-2F(25H-4F^2)/15=8a+2FH/5-50FH/15+8F^3/15=8a-44FH/15+8F^3/15=Acol. dE0/dell has degree exactly 5 and [S^5]=(4a)(2F/5)-H(25H-4F^2)/15=8aF/5-5H^2/3+4F^2H/15=Bcol. Signs and factors CONFIRMED; these are the highest S powers in which ell occurs at all (E1 slots S^5..S^8 and E0 slots S^6..S^9 are ell-free). Because E1_res,E0_res are affine in ell, [S^4]E1_res=Acol*ell+P and [S^5]E0_res=Bcol*ell+Q with P,Q the exact ell=0 values of the full rows: every cross product 2k*B2, h*B1, hB1*, fB0*, k*B1, hB0* of lower-band coefficients (u,d0,v0,v1,k1,k2,k3) is inside P,Q by definition, none is dropped, and the constant targets -u and -1 sit in lower slots. (1) CONFIRMED.

Homogeneous check (own): Cbar=theta^3+Ftheta^2+Htheta+a, V=theta^2+(2F/5)theta+c, c=(25H-4F^2)/45. 4CbarV*=8theta^4+(48F/5)theta^3+(8F^2/5+8H)theta^2+(8FH/5+8a)theta+8aF/5. 3Cbar*V=9theta^4+(48F/5)theta^3+(9c+12F^2/5+3H)theta^2+(6Fc+6FH/5)theta+3Hc. Difference: theta^4 -1; theta^3 0; theta^2 -4F^2/5+5H-9c=0 since 9c=5H-4F^2/5; theta^1 8a+2FH/5-(2F/15)(25H-4F^2)=Acol; theta^0 8aF/5-H(25H-4F^2)/15=Bcol. CONFIRMED. A theta^3 term V3 in V would leave 3V3 theta^5 against a target with no theta^5, so V3=0. This is the ell-derivative only: the weight-5 target of the full source is S^5(-u^2theta^5-ell theta^4) from delta_5,delta_4, and P,Q keep the earlier cross products; nothing asserted zero.

## B. Global no-common-zero of (Acol,Bcol): CONFIRMED

Leading recurrence replayed from 17b (2): i=1 5D1=6F; i=2 9D2=2FD1+13H; i=3 13D3=-2FD2+9HD1+20a; i=4 17D4=-6FD3+5HD2+16aD1; i=5 21D5=-10FD4+HD3+12aD2; i=6 (D6=0) q6=14FD5+3HD4-8aD3; i=7 q7=7HD5-4aD4. Accepted leading (ascending) indexing, not the reversed theta indexing. At a hypothetical common zero in a characteristic-zero field point of the guarded leading algebra: if F=0 then Acol=8a and a=1/(ws^3) is a unit, impossible. So F!=0; z=H/F^2, kappa=a/F^3, d_i=D_i/F^i (a contradiction-test rescaling only, not imposed on the source). Acol/F^3=8kappa-44z/15+8/15=0 gives kappa=(11z-2)/30. Bcol/F^4=8kappa/5-5z^2/3+4z/15=0; times 150 with kappa substituted: 88z-16-250z^2+40z=0, i.e. q(z)=125z^2-64z+8=0. (3) CONFIRMED.

d1=6/5. d2=(12+65z)/45. 13d3=-2d2+(54/5)z+20kappa=[-(24+130z)+486z+(330z-60)]/45=(686z-84)/45, d3=(686z-84)/585 (also from 17b D3 with 900kappa=30(11z-2)). 17d4=-6d3+5zd2+16kappa d1=-(1372z-168)/195+(12z+65z^2)/9+(176z-32)/25; over 2925: (-20580z+2520)+(3900z+21125z^2)+(20592z-3744)=21125z^2+3912z-1224, so d4=(21125z^2+3912z-1224)/49725 (49725=17*2925). Mod q: 21125z^2=169(64z-8)=10816z-1352, numerator 14728z-2576. CONFIRMED.

q7/F^7=7zd5-4kappa d4 and 7zd5=(z/3)(21d5)=(z/3)(-10d4+zd3+12kappa d2). Times 15: 15q7/F^7=(-50z-60kappa)d4+5z^2d3+60z kappa d2, and 60kappa=22z-4 gives (4-72z)d4+5z^2d3+60z kappa d2. Times 49725 with 49725/585=85 and 49725/45=1105: N=(4-72z)(14728z-2576)+425z^2(686z-84)+2210z(11z-2)(12+65z). Expansion: first term -1060416z^2+244384z-10304 (72*14728=1060416, 72*2576=185472, 58912+185472=244384); second 291550z^3-35700z^2; third (11z-2)(12+65z)=715z^2+2z-24, times 2210z: 1580150z^3+4420z^2-53040z. Sum 1871700z^3-1091696z^2+191344z-10304. CONFIRMED. Scalar: 15q7/F^7=N/49725 exactly modulo q, so no zero scalar cancelled.

Remainder: 125z^2=64z-8, 15625z^2=8000z-1000, 15625z^3=125(64z^2-8z)=64(64z-8)-1000z=3096z-512. Then 15625N == 1871700(3096z-512)-1091696(8000z-1000)+191344*15625z-10304*15625. Constant: -958310400+1091696000-161000000=-27614400 (1871700*512=958310400; 10304*15625=161000000). Linear: 5794783200-8733568000+2989750000=50965200 (1871700*3096=5794783200; 191344*15625=2989750000). 1200*42471=50965200 and 1200*23012=27614400, so N==(1200/15625)(42471z-23012) mod q. (4) CONFIRMED. disc q=4096-4000=96, not a rational square, so q is irreducible over Q: in ANY characteristic-zero field a root z of q is not rational, hence 42471z-23012!=0 (its only root is the rational 23012/42471). So q7!=0 there, contradicting q7=0, which holds exactly in Lambda by the accepted 17b gate. Only q7 and a!=0 are used; H!=0 is not needed. The F=0 chart, the F!=0 chart and every maximal ideal of B are covered; nothing is deleted from Lambda (alpha,beta are s-free, and s enters (Acol,Bcol) only through units). No rational-point restriction anywhere.

## C. alpha/beta, ideal (alpha,beta)=B, Gram-adjugate left inverse: CONFIRMED

(5) own substitution of F=v/(ws), H=1/(ws^2), a=1/(ws^3): 8a=8/(ws^3), FH=v/(w^2s^3), F^3=v^3/(w^3s^3), so Acol=[120w^2-44vw+8v^3]/(15w^3s^3)=4(30w^2-11vw+2v^3)/(15w^3s^3). aF=v/(w^2s^4), H^2=1/(w^2s^4), F^2H=v^2/(w^3s^4), so Bcol=[24vw-25w+4v^2]/(15w^3s^4)=((24v-25)w+4v^2)/(15w^3s^4). alpha,beta as displayed; both scalars 4/(15w^3s^3), 1/(15w^3s^4) are units of Lambda (w unit of B by 17b, s unit). CONFIRMED.

(alpha,beta)=B. B is a finite Q-algebra, so its maximal ideals have number-field residue fields K. At each, 17b (8) gives a normalized f6=f7 point (v,w=R/(112L)), w!=0, f5!=0, and the s=1 lift (F,H,a)=(v/w,1/w,1/w) satisfies the leading ODE with q6=q7=0 (17b gate C/D). Section B shows Acol,Bcol cannot both vanish there, and at s=1 they are unit multiples of alpha,beta. So alpha,beta lie in no common maximal ideal: (alpha,beta)=B, ring-level, nilpotents allowed, no factor chosen, no reality assumed. CONFIRMED. Unimodularity of the column in the full Lambda follows by the unit scalars; over T=Lambda[u,d0,v0,v1,k1,k2,k3] and every Lambda-algebra by base change.

Recipe. M_alpha,M_beta are the multiplication matrices of alpha,beta on B in the basis 1,v,..,v^6 (columns = remainders of alpha v^i, beta v^i mod p). The image of the 7x14 matrix (M_alpha M_beta) over Q is {alpha r+beta t}=(alpha,beta)=B=Q^7, so it has full row rank 7. K=(M_alpha M_beta)(M_alpha M_beta)^tr is rational symmetric; for real x!=0, x^tr K x=|M_alpha^tr x|^2+|M_beta^tr x|^2>0 because x^tr(M_alpha M_beta)=0 forces x=0 (full row rank). So K is positive definite over R, det K>0, and det K is rational since K is: a nonzero RATIONAL number, the only quantity ever divided. Then M_alpha rvec+M_beta tvec=K adj(K)e/det K=e, and e=(1,0,..,0)^tr is the element 1 in this basis, so alpha r0+beta t0=1 in B. CONFIRMED. The identity is on rational coefficient matrices; it says nothing about residue fields being real and divides no element of the product algebra.

(6): lambda_A Acol+lambda_B Bcol=(15/4)w^3s^3 r0*4alpha/(15w^3s^3)+15w^3s^4 t0*beta/(15w^3s^4)=alpha r0+beta t0=1, an identity in Lambda hence in every Lambda-algebra (T, T[ell], all residue fields). Literal finiteness: p is the explicit degree-7 polynomial 17b (7); w=R/(112L) needs L^(-1) mod p, which exists by (L,p)=(1) and is produced by the finite extended-Euclid step on (L,p) (the Bezout coefficients are specified, not written, in 17b and here). Every further step is a fixed 7x7 rational matrix operation. So (5)-(6) with det/adj is a literal finite unexpanded left inverse over all of Lambda and its algebras. Not evaluated, no size or speed claimed.

## D. ell_star, compatibility, quotient-ring map, changed-leading control: CONFIRMED

Signs (own). Row1=Acol ell+P, Row2=Bcol ell+Q, ell_star=-lambda_A P-lambda_B Q, compat=Bcol P-Acol Q. Row1(ell_star)=P(1-lambda_A Acol)-Acol lambda_B Q=lambda_B(Bcol P-Acol Q)=lambda_B*compat. Row2(ell_star)=-lambda_A Bcol P+Q(1-lambda_B Bcol)=-lambda_A*compat. Both producer signs CONFIRMED. Ideal equality in T[ell]: lambda_A Row1+lambda_B Row2=ell-ell_star and Bcol Row1-Acol Row2=compat; conversely Row1=Acol(ell-ell_star)+lambda_B compat, Row2=Bcol(ell-ell_star)-lambda_A compat. So (Row1,Row2)=(ell-ell_star,compat) exactly, and T[ell]/(Row1,Row2,rest) is isomorphic to T/(compat, rest|ell=ell_star): a quotient-ring isomorphism, not field-point coverage. ell_star lies in T (denominators only det K and the units s,w), so no new localization. All other rows, the mate reconstruction, the 17b guard restoration omega=ws^8f5 and every scale/parameter are untouched. Slot count: 17 formal retained slots minus the two ell rows plus compat = 16 formal equations; no nonzero-row count is measured or implied.

Changed-leading control (own): in Q[z]/(q), a field since q is irreducible, with F=1, H=z, a=(11z-2)/30: Acol=(88z-16)/30-88z/30+16/30=0; 150*Bcol=88z-16-250z^2+40z=-2q(z)=0; but q7=7zd5-4kappa d4=N/(15*49725)!=0 by B. Units: q(0)=8 so z=H!=0; q(2/11)=(500-1408+968)/121=60/121 so 11z-2 and a are nonzero. CONFIRMED: the column vanishes only off the leading ODE, so unimodularity is NOT a free coefficient identity. This point is not a source point and carries no leading/boundary guard. The full affine response (2) versus a leading-only V is a scope control: u,d0,v0,v1 genuinely occur in W0 and ell occurs in E1 slots S^0..S^4 and E0 slots S^0..S^5, so a leading-only elimination would misplace those terms. Neither ell_star nor any leading point solves the 15 substituted rows or compat; no composition with the weight 8,7,6 band eliminations is made or licensed here.

## E. Verdicts, remaining doubts, smallest repairs, scope

Verdicts: A CONFIRMED (W5=W4=W3=0, W2=S, W1=-u+(2F/5)S^2, all three W0 terms, both resonance constants, both gauges, full delta vector, Acol/Bcol with signs, homogeneous identity, P/Q as exact ell=0 rows). B CONFIRMED (kappa, q, d1..d5, the 15 scalar, N, the exact remainder 1200(42471z-23012)/15625, discriminant 96, all charts and all residue fields, characteristic zero generally). C CONFIRMED ((5), (alpha,beta)=B at every residue field, full row rank over Q, real positive definiteness of the rational Gram matrix, nonzero rational det K, alpha r0+beta t0=1, literal finite left inverse over all Lambda-algebras). D CONFIRMED (both substitution signs, exact ideal equality and quotient-ring isomorphism in T[ell], 16 formal slots, changed-leading control with units 8 and 60/121, scope-control reading only).

Concrete doubts and smallest repairs (none changes a verdict):
- Producer section 4 calls M_alpha,M_beta "entirely specified" while the Bezout coefficients giving L^(-1) mod p are unwritten in 17b and here. Repair: one sentence that L^(-1) is the finite extended-Euclid output on the explicit (L,p); nothing else is unspecified.
- W3=0 uses that the gauge beta=[S]B3=0 is imposed identically in ell (it is; a fixed constant). Repair: say so in section 2.
- Section 3 states the contradiction against q7 only; q6 and H!=0 are unused there. Repair: say "q7 alone" to avoid a reader importing 17b H!=0.
- P,Q remain unexpanded by design; compat=Bcol P-Acol Q is therefore a defined but unexpanded element of T. No claim that compat is nonzero, zero, or independent of the weight 8,7,6 rows is made or checked.

Not established here or by the producer: no emitted row, no source point, no unit or properness of any ideal, no F10 or global exclusion, no measured speedup, no higher band, no composition with other band eliminations. The 15 substituted rows and compat are untouched. Reducedness of B (17a-conditional in the 17b gate) is not needed for any verdict above.

Read/tool scope and deviations: exactly the five charged inputs, whole, from /tmp/jc2-lane.BzWKhh/inputs after sha256sum match; tools date, ls, mkdir (box dir only), sha256sum, cat, grep/sed/awk/diff on own files for the hex custody check, apply_patch for every write. No heredoc or cat write. ZERO CAS, arithmetic script, compile, test, network, SSH, AWS, process census or agent. One deviation: a temp file for the hex cross-check was first pointed at the read-only inputs directory and failed; redone without a file. Hash custody: every 64-hex token in this report equals one of the five input hashes (checked by diff below the own whole-read).

## OPEN(S) RAISED

- OPEN[F10-R1-FOURTH-BAND-LEFTINVERSE-COORDINATES] QUANTITY: number of nonzero rational coordinates among the 14 entries of (rvec,tvec) in the basis 1,v,..,v^6, value <= 14, together with the height (max numerator/denominator digit count) of det K. CHEAPEST TEST: exact rational extended Euclid on (L,p), two 7x7 multiplication matrices, Gram matrix, adjugate and determinant, then read back alpha r0+beta t0=1 mod p. WALL: <= 1 minute if charged; no execution authority created here.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN check (this report and its box only); no corpus scan. The 17b gate OPEN[F10-R1-RETAINED-ROWS-READBACK] concerns row read-back, a different quantity.

## GAPs (left open, not filled)

(i) explicit coordinates of r0,t0 and det K; (ii) expansion of P,Q and compat; (iii) any relation of compat to the weight 8,7,6 band rows; (iv) size of ell_star after substitution into the 15 rows. None is required by the four verdicts.

Own whole-read at 18:03:44Z (marker appended 18:03:58Z; this timestamp corrected 18:04Z from a mistyped 18:04:10Z): sections 0, A, B, C, D, E, OPEN(S) RAISED (one entry with quantity, relation token, cheapest test, wall), COLLISIONS, GAPs. No Seal and no charge_basis are authored here. No marker before this line.

<!-- BODY-END -->
