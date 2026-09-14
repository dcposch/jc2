# Independent Fable gate: simple-L root discriminator for the H-divisible golden source

2026-09-08, 23:35 UTC start. HOSTILE REVIEW of the cross's Section 2 "simple-L discriminator" and its generalized lower-B lemma, at the literal scope of scope.md. Only the nine frozen inputs in the lane inputs directory were read. No live peer, canonical, jc2-lean, web, AWS/SSH, CAS or solver access; no new agent; no replay of the accepted source checker. One tiny exact control (a degree-5 factor and free 3/5 coefficient identities) ran in my box; it is illustration, never the proof. All derivations below are my own, not restatements.

## 0. Verdicts

| # | Target | Verdict |
|---|---|---|
| 1 | Literal assumptions, canonical references, P0_j=P2_j=0, P1_j=C | CONFIRMED |
| 2 | Moving simple L root: inverse over K(p), unit derivative for both rho | CONFIRMED |
| 3 | Actual q, eta, A initial Z^3+uZ+v with (u,v)!=0, Euler degree 3h | CONFIRMED |
| 4 | All B terms; earlier-B constant excluded; monic quintic with linear+constant | CONFIRMED |
| 5 | Target order 36, commutation 7eta<36, 3/5 common power, lower-B lemma | CONFIRMED (lemma must state m>=1) |
| 6 | Conclusion and field scope: at most L divides C | CONFIRMED |

Net: under (S), the accepted references and F_j=H*C with 1<=j<=9, the hypothesis C(-p,p)!=0 is contradictory over the field K(p), for both roots rho, for every finite or infinite q and nu, with no parity, sign, or rationality assumption. Any remaining H-divisible source therefore has L | C. Nothing beyond that follows.

## 1. Pins and reading

- All nine sha256 pins in the lane's charged-inputs list match the frozen files (recomputed with sha256sum). The first 9849 bytes of cross-proof.md hash to `a336ca31de9d522bc7e21d243b52155edb93dbb409a8d30c86d41c8e76e721a9`, matching cross-transaction.json; the seal after the body is the publisher's.
- cross-input-pins.json and cross-custody.json were read as provenance only. None of their 23 referenced paths was opened.
- prior-gate.md was consulted only for its Target 1/2 wording on normal division and the centralizer; it is not re-reviewed. audit-15m.md supplies the accepted framework (references, wedge identity, kernel induction, ord G>=2j, H | F_j^2, j<=12) and nothing about the new conclusion.
- Scope read whole; cross read whole; source proof read whole.

## 2. Target 1: literal assumptions and normal division. CONFIRMED

Framework facts used (source §1–2, accepted in 15m): R_s=H+sum s^r R_(5-r), cubic in g with g^3 coefficient rho*p^2; F=A_s-R_s^3-alpha*s^10*R_s-a0*s^15 with ord F=j and F!=0; B_s=f_B(R_s)+q(R_s)F+G with all five kernels b_i*s^(25-5i) retained and ord G>=2j after the kernel induction; combined grading deg s=deg g=deg p=1.

Normal division. Division by R_s in K[g,p,s], leading monomial rho*g^3p^2 in lex g>p>s, terminates, keeps combined homogeneity, never lowers s-order, and lowers the weight bound by one per R_s factor: ord P_i>=j, w(P_i)<=3-i, deg P_i=15-5i, and P3=0 because the (g,p)-degree of F is at most 14. A normal monomial g^a p^b with a>=3 has b<=1 and weight>=8, so every normal block of weight<=5 has g-degree<=2.

H | F_j forces P0_j=0: at order j, F_j=P0_j+H*P1_j+H^2*P2_j, so P0_j=H*(C-P1_j-H*P2_j). A nonzero H-multiple has lex-leading monomial divisible by g^3p^2 and is not normal. Hence P0_j=0.

P2_j=0 and P1_j=C. For j>=6 the (g,p)-degree of P2_j is 5-j<0. For j<=5, F_j is the H^2-normal residual of the reference construction (no monomial divisible by g^6p^4). If deg_g C>=3, the g-leading monomial g^a p^b of C satisfies 5a-7b<=2, so b>=2, and F_j contains rho*c_a*g^(a+3)p^(b+2), divisible by g^6p^4: contradiction. So deg_g C<=2 for every j, and C-P1_j=H*P2_j with a left side of g-degree<=2 forces P2_j=0. This is the one place where the H^2-normality of orders 1..5 is load-bearing; the prior gate's remark that it is unused holds for the non-H branch only.

Robustness: even if P2_j were nonzero, the linear coefficient u below would still equal C(-p,p), because H(-p,p)=0. The range j<=9 is forced because alpha makes F_10 H-normal and deg F_j<5 for j>=11. Every constant alpha, a0, b4..b0 appears explicitly in Sections 4–5 and none is dropped.

## 3. Target 2: the moving simple L root. CONFIRMED

R_0=H=p^2*L*M^2. At g=-p: L=0, M=(1-t)p=rho*p, and H_g=p^2(M^2+2tLM) evaluates to rho^2*p^4, nonzero for both roots rho (control CHECK1; the changed object M:=L makes it vanish, as it must for a double root). Hence R_s(g,p)=z has a unique solution g=G(s,z) in K[p,1/p][[s,z]] with G(0,0)=-p, by the formal implicit function theorem; the only denominators are powers of rho^2*p^4. No algebraic closure and no square root is needed; the cross's Kbar(p) is harmless. Every coefficient has nonnegative s- and z-order; p-poles are allowed and nothing is asserted at p=0. Uniqueness under simultaneous scaling of (s,z,p) with deg z=5 gives combined degree 1: the s^a z^b coefficient is a Laurent monomial p^(1-a-5b). The moving simple root is g_L(s,p)=G(s,0).

## 4. Target 3: actual q and the A initial. CONFIRMED

Write At=A_s(G,p)=z^3+alpha*s^10*z+a0*s^15+Ft with Ft=F(G,p)=P0(G,p)+z*P1(G,p)+z^2*P2(G,p). Independently of the blocks, Ft=sum_k s^k F_k(G,p) and H(G,p)=z-sum_(r>=1) s^r R_(5-r)(G,p), so s^j F_j(G,p)=s^j(z+O(s))(C(-p,p)+O(s,z)).

Term census of Ft by (s-order a, z-degree b): the constant theta(s):=Ft(s,0)=P0(g_L,p) has order q>=j+1 because F_j(-p,p)=0, with q=infinity allowed; the single term s^j*C(-p,p)*z with C(-p,p)=c_L*p^(10-j), c_L in K, nonzero iff L does not divide C; everything else has (a>=j+1, b>=1) or (a>=j, b>=2). This covers every positive-z implicit term of P0(G,p), since P0 has order>=j+1 and substitution cannot lower s-order, the P1 remainder, and z^2*P2. No other term has bidegree (j,1): alpha*s^10*z would need j=10.

Put z=s^eta*Z with eta=min(j/2,q/3). Orders: 3eta (Z^3), j+eta (uZ), q (v), >=j+1+eta, >=j+2eta, 10+eta, 15. Because eta<=j/2<(j+1)/2 and eta<=9/2<5, all of j+1+eta, j+2eta, 10+eta, 15 exceed 3eta strictly; j+eta>=3eta with equality iff eta=j/2; q>=3eta with equality iff eta=q/3. So the initial is P=Z^3+uZ+v with u=c_L*p^(10-j) present iff eta=j/2 and v=theta_q present iff eta=q/3; the minimum is attained at least once and the attained coefficient is nonzero (c_L!=0 by hypothesis; theta_q!=0 by definition of the order, and q is finite whenever q/3<j/2). There is no Z^2 term at 3eta. Euler: the coefficient p-degree is 15-a-5b=(3-b)h with h=5-eta>0, so EP=3hP for E=p*d_p+h*Z*d_Z, and every exponent is an integer: no p^(1/2) field is needed, unlike the double-root chart. The inequalities q>j and eta>j/3 are true but not load-bearing; what is used is eta<=j/2, eta<=q/3, eta<5.

## 5. Target 4: every B term. CONFIRMED

Bt=z^5+b4*s^5*z^4+b3*s^10*z^3+b2*s^15*z^2+b1*s^20*z+b0*s^25+[5z^2/3+(4b4/3)s^5*z+(b3-5alpha/9)s^10]*Ft+Gt, with Gt=G(G(s,z),p)=sum z^i Q_i(G,p) of s-order>=2j.

Orders after z=s^eta*Z, using ord Ft=3eta exactly with initial uZ+v: kernel i sits at 25-5i+i*eta=5eta+(5-i)(5-eta)>5eta for i<5. (5/3)z^2*Ft contributes (5/3)Z^2(uZ+v) at exactly 5eta; the b4 term is at 5+4eta>5eta; the b3/alpha term at 10+3eta>5eta, and its Z^0 part s^10*theta at 10+q>5eta in every case. Gt: a Z^n term with n>=1 has order>=2j+n*eta>=2j+eta>=5eta, with equality only for n=1 and eta=j/2, giving a linear term lambda*Z at 5eta with lambda in K*p^(4h). The Z^0 terms of Gt, namely G(g_L,p), have integer orders m>=2j and may lie below 5eta when eta>2j/5.

Earlier B initial. Let nu=ord_s G(g_L,p) and suppose nu<5eta. The coefficient e=e0*p^(25-nu), e0 in K*, is a coefficient-field element of Euler degree 25-nu, strictly between 2 and 25. In (Z,p) coordinates the s^(3eta+nu) coefficient of the bracket is exactly [P,e]=P_Z*e'=(3Z^2+u)e', since every other product of terms has strictly larger order. As 3eta+nu<8eta<=36<36+eta, it must vanish, so e'=(25-nu)e0*p^(24-nu)=0, impossible in characteristic zero. Hence Bt has no Z^0 term below 5eta; only the lowest such term is needed, so all are excluded at once.

At 5eta: Q=Z^5+(5/3)uZ^3+(5/3)vZ^2+lambda*Z+e, monic. No competing Z^5 leader: Ft has no Z^3 at 3eta (any Z^3 of Ft sits at>=j+3eta), b4*z^4 is Z^4 at a higher order, and Gt gives only Z^0 and Z^1 at 5eta. Consistency, not needed for the proof: the accepted order-2j identity gives G_(2j)=(5/9)H*C^2 (plus (e/3)H^3 at j=5), whence G_(2j)(-p,p)=0 and lambda=(5/9)u^2; the linear term is genuinely present when u!=0, so it must not be deleted at eta=j/2. EQ=5hQ by the count (5-b)h.

## 6. Target 5: target order, commutation, common power, lower-B lemma. CONFIRMED

Jacobian factor. For functions of (g,p) and z=R_s(g,p), the chain rule gives [A,B]_(g,p)=R_(s,g)*[At,Bt]_(z,p). Hence [At,Bt]_(z,p)=c*s^36*G^2/R_(s,g)(G,p), a unit of K(p)[[s,z]] times s^36 with constant term c/(rho^2*p^2), nonzero in both embeddings: exact order 36. With z=s^eta*Z one has d_z=s^(-eta)d_Z, so [At,Bt]_(Z,p) has exact order 36+eta. The initial bracket s^(8eta)[P,Q]_(Z,p) must vanish because 8eta<36+eta, i.e. 7eta<36, true since 7eta<=63/2. Only the lower bound 36 on the target order is load-bearing; c!=0 is not used by this arrow.

Common power, derived independently. EP=3hP and EQ=5hQ give p[P,Q]=h(5P_Z*Q-3P*Q_Z), so [P,Q]=0 makes d_Z(Q^3/P^5)=0 in K(p)(Z); in characteristic zero Q^3=phi*P^5 with phi in K(p), and monicity gives phi=1. In the UFD K(p)[Z], exponent comparison 3f=5e on each irreducible factor forces P=W^3 and Q=W^5 with W monic of degree 1, W=Z+w. The Z^2 coefficient of P is 3w=0, so P=Z^3 and u=v=0, contradicting (u,v)!=0. The terms lambda and e never enter. Control CHECK3: the top-down monic cube root of P^5 leaves a nonzero residual for a depressed instance and a zero residual for (Z+p)^3, showing the depressed hypothesis is exactly what is used.

Lower-B lemma (cross §2, generalized form). Let P be monic of Z-degree m>=1 and Q!=0 of degree n>=0 with leading coefficient q_n, over a characteristic-zero differential field with derivation ' = d/dp, and [P,Q]_(Z,p)=0. Then deg P_p<=m-1 and deg Q_Z<=n-1, so the Z^(m+n-1) coefficient of [P,Q] is m*q_n', hence q_n'=0. If EQ=Lambda*Q for E=p*d_p+h*Z*d_Z, the Z^n coefficient gives p*q_n'=(Lambda-nh)q_n, so Lambda=nh. Correct as stated, including n=0, where the Z^(m-1) coefficient is m*q_0'. P need not be Euler-homogeneous; only its leading coefficient must be p-constant. Two hypotheses the cross leaves implicit: m>=1 (P=1 commutes with everything), and q_n must be a non-zero-divisor for the last division, which is exactly what a nilpotent leading coefficient would break. This review uses the lemma only over the field K(p), with m=3 and n=0. Control CHECK2: the Z^7 coefficient vanishes for a monic cubic against a quintic, and equals -5=-n*p_m'*q_n for the changed object p*Z^3+uZ+v.

## 7. Target 6: exact conclusion and field scope. CONFIRMED

Used: (S), the accepted references, ord G>=2j, H | F_j with 1<=j<=9, and C(-p,p)!=0. Not used: parity, a rational point, a square-root sign, or a choice of embedding beyond rho!=0; the root g=-p is rational and fixed. q=infinity gives eta=j/2, v=0, u!=0; nu=infinity removes the earlier constant. Conclusion: every H-divisible source has L | C, i.e. C(-p,p)=0. Not concluded: the M-value or M-derivative cases, coalesced or separated sheets, hidden jets, whole golden/common/D125, nilpotent or scheme-valued sources (the Euler and UFD steps are field steps), reverse lift, or JC2. The cross's closing sentence claims exactly this and no more.

## 8. Attacks attempted

1. Missing term at bidegree (j,1): only alpha*s^10*z could collide, at j=10, outside the range. Closed.
2. P2_j!=0 for j<=5: excluded by H^2-normality plus weight, and harmless anyway because H(-p,p)=0. Closed.
3. Z^0 terms of Bt below 5eta from f_B or q(R)F: b0*s^25 (25>5eta) and s^10(b3-5alpha/9)theta (10+q>5eta: eta=j/2 gives q>=3j/2 and 10>j; eta=q/3 gives q<=13<15). Only G(g_L,p) remains. Closed.
4. Coincidence with the target: 8eta=36+eta needs eta=36/7>9/2; 3eta+nu=36+eta needs 2eta+nu=36>7eta. Closed.
5. Fractional p-exponents: none arise; every coefficient is an integer Laurent monomial. Closed.
6. Dependence on c!=0: not needed; the order lower bound suffices. Noted, not a gap.
7. Lemma at m=0 or over a ring: fails; the two implicit hypotheses are recorded in Section 6. Not a gap for the application.
8. Puiseux bookkeeping: with eta in (1/2)Z or (1/3)Z all series live in K(p)[Z][[s^(1/6)]]; s is constant for both derivatives, so orders compare as rationals and initial forms are well defined. Closed.

## 9. Tiny control evidence

Box: box/golden-hdiv-simple-l-gate-fable5-20260908/. Script control.py, pure Python with Fraction arithmetic in Q[rho]/(rho^2-3rho+1); materialises only H (degree 5) and degree<=15 polynomials in (Z,p). Invocation per mode: `timeout 30 prlimit --cpu=25 --as=536870912 python3 -I -B [-O] control.py MODE`, no inner timeout, no gating assert. Modes: positive; wrong-root (changed object M:=L, must fail CHECK1 only); nonmonic (changed object p*Z^3+uZ+v, must fail CHECK2 only). Each mode ran normal and -O; stdout was byte-identical between the two, rc=0 everywhere, stderr empty. Outcomes: positive PASS/PASS/PASS; wrong-root FAIL/PASS/PASS; nonmonic PASS/FAIL/PASS. Finite instances only.

- `control.py` `8d6d15d53e6b630a6e68ae85624022791c0098012e74542f885f2bdd79414562`
- `out_nonmonic.rc` `93ff7811a209e2a8479230bbb9b6bc19f7f311d3af383ec350c1db2a7e7d5494`
- `out_nonmonic.stderr` `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `out_nonmonic.stdout` `4a2f580ea13504bb70c6adcbdb74eda8efdee4f46c4f77394c1768caa22aaaa0`
- `out_nonmonic_O.rc` `93ff7811a209e2a8479230bbb9b6bc19f7f311d3af383ec350c1db2a7e7d5494`
- `out_nonmonic_O.stderr` `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `out_nonmonic_O.stdout` `4a2f580ea13504bb70c6adcbdb74eda8efdee4f46c4f77394c1768caa22aaaa0`
- `out_positive.rc` `93ff7811a209e2a8479230bbb9b6bc19f7f311d3af383ec350c1db2a7e7d5494`
- `out_positive.stderr` `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `out_positive.stdout` `d9eb8b166a40a9748ea67cba83d7cf9f534f5c4f66e4b469e5d6a8666d4e3e3a`
- `out_positive_O.rc` `93ff7811a209e2a8479230bbb9b6bc19f7f311d3af383ec350c1db2a7e7d5494`
- `out_positive_O.stderr` `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `out_positive_O.stdout` `d9eb8b166a40a9748ea67cba83d7cf9f534f5c4f66e4b469e5d6a8666d4e3e3a`
- `out_wrong-root.rc` `93ff7811a209e2a8479230bbb9b6bc19f7f311d3af383ec350c1db2a7e7d5494`
- `out_wrong-root.stderr` `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `out_wrong-root.stdout` `901b1b0d9ffefe5b293d07c62df602f50c4a9ab5a4cb9be1749c4cf02ca2ff27`
- `out_wrong-root_O.rc` `93ff7811a209e2a8479230bbb9b6bc19f7f311d3af383ec350c1db2a7e7d5494`
- `out_wrong-root_O.stderr` `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `out_wrong-root_O.stdout` `901b1b0d9ffefe5b293d07c62df602f50c4a9ab5a4cb9be1749c4cf02ca2ff27`

## 10. Corrections and closing

- Cross wording: Kbar(p) is unnecessary at the simple root; K[p,1/p] suffices. The lemma should state m>=1 and its field (non-zero-divisor) scope.
- Source/prior-gate wording: H^2-normality of orders 1..5 is load-bearing in this branch for P2_j=0 at j<=5, though the conclusion survives without it.
- Nothing in this gate promotes a golden, common, D125 or JC2 exclusion. No exit-price line is authored: no new price is asserted. No seal is authored; the lane publisher owns it. All writers and the six control subprocesses are terminal. STOP/IDLE.

<!-- BODY-END -->
