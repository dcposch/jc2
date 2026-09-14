# Golden H-divisible correction: hostile review of the coalesced/separated M-source composition

2026-09-09 UTC (lane frozen 2026-09-08 23:55 UTC). Fable 5.1, independent hostile referee, prose-first, one tiny scalar control. **VERDICT: six CONFIRMED, no GAP, no REFUTED.** Both producer proofs are correct on their exact field-source scope. They use the identical actual F, Morse chart, coefficients c_n and balance r, and their hypotheses kappa>=2r and kappa<2r partition [1,infinity]. The composition excludes exactly the union of the two strata {M does not divide C} and {LM divides C} of the H-divisible first correction F_j=HC, for every kappa including infinity, and nothing more. The stratum M|C with L not dividing C stays outside. No simple-L, whole-golden, common, D125, reverse-lift, scheme, properness or JC2 conclusion is drawn or licensed. Root alone decides promotion.

## 0. Inputs (frozen bytes only, pins checked first)

| file | bytes | sha256 |
|---|---:|---|
| coalesced-input-pins.json | 766 | `180b2b64e2bea86b2f1890927297229716c65bc596efef24a3eaadc97d837cea` |
| coalesced-transaction.json | 705 | `2f36b75b2ea2857b2264df0e992019300bad76a50461a498c8b937a42eedd9fa` |
| separated-transaction.json | 686 | `bed766fae3fdaeff28d6ca82bab381267fa7ed5fc7c5686d06958e0193c12174` |
| source-transaction.json | 702 | `a80659d8c6b38fd4800b7eb70b650af57a0065e0c67b077f2878c1c24377c8af` |
| coalesced-custody.json | 2581 | `63afa4581f3e9834e607a9932e569b0311ac5ff9323321c24925c9b970da2091` |
| scope.md | 3111 | `ee258be548eed733f000a1bcbacf8ec1217bf47e3a11f83d1933474d5aef6690` |
| source-framework.md | 18157 | `14c4cdeddf9b1166046759022378775fc7ebc147c7d939579cf93f6b78aa51c6` |
| coalesced-proof.md | 12442 | `fd04a5fd0bbbbbe89e10a50310d931bbf72d442512422912b1dd62cdcaa38654` |
| separated-proof.md | 14320 | `e8ae9f1ab4c319f12af4514ad9cb70f3b3b48541e0bf82d9acd55cd81e67ca87` |
| audit-15m.md | 5348 | `b02ae267bb8cfef6956d6e0cec0b6188196b222d3d9d78e3d1582f4a5cc1a440` |

Agreement: the source pin in coalesced-input-pins.json equals the frozen source-framework.md hash; the audit pin equals audit-15m.md; each transaction's full_sha256 equals its frozen proof file; the coalesced custody packet lists the same three charged inputs. The third pinned entry (the accepted non-H gate) was hash-lookup only in both producers and was not read here. Transactions and custody served as provenance only; no referenced report, live gate, log or receipt was opened.

## 1. Target as reviewed

Common literal source (source-framework section 1): K of characteristic zero containing either rho with rho^2-3rho+1=0, t=1-rho, L=p+g, M=p+tg, H=p^2 L M^2, deg A=15, deg B=25, tops H^3 and H^5, w(g)=5, w(p)=-7, w(A)<=3, w(B)<=5, [A,B]=c g^2 with c nonzero, no parity. Canonical A-only references R_s=H+sum s^a R_(5-a), alpha s^10 R_s, a0 s^15, F=A_s-R_s^3-alpha s^10 R_s-a0 s^15, j=ord_s F, and the H-divisible branch F_j=HC nonzero with 1<=j<=9, deg C=10-j, w(C)<=2, deg_g C<=2 (source section 7). The B reference retains all five kernels b_i s^(25-5i) R_s^i, q_s(R_s)F and G with ord G>=2j (source section 2). Morse chart at g0=-p/t: R_s=xi_s+zeta^2, g=g_c+w_s(zeta) in E[[s,zeta]], E=Kbar(p^(1/2)), kappa=ord xi_s, F(g,p)=sum c_n zeta^n, r=min over n<=d of ord(c_n)/(6-n), d=2 on {C(g0,p) nonzero}, d=3 on {LM|C}.

## 2. Verdict 1, references, field, leading coefficients: CONFIRMED

Independent derivations (the scalar ones are replayed by the control in section 9).

- Units. t^2=rho, 1/t=2-rho, t-1=-rho, t(t-1)=2rho-1, with norms -1, 1, -1 under the norm form a^2+3ab+b^2. All are units for both embeddings, so p, L, M are distinct and rho p^2 is the g^3 coefficient of H.
- Degree-5 identity. L(g0+w)=p(t-1)/t+w and M(g0+w)=tw give H(g0+w,p)=t(t-1)p^3 w^2+rho p^2 w^3 exactly. So a_0=t(t-1)p^3, the Morse coordinate zeta=w sqrt(a_s+rho p^2 w) needs only a=sqrt(t(t-1)) in Kbar and p^(3/2) in E, and the inverse w_s(zeta) has nonnegative s-orders because a_s+rho p^2 w=a_0(1+O(s)+O(w)); its p-poles live in E and do not touch s-orders.
- Shapes. In a domain w(HC)=w(H)+w(C) with w(H)=1, so w(C)<=2; deg_g F_j<=5 gives deg_g C<=2. If LM|C then C=D LM with deg_g D=0, hence D=lambda p^(8-j) and w(C)=7j-46<=2 forces j<=6; j=7 gives weight 3 and is rejected. Order j: [s^j]F(g,p)=F_j(g0+w_0(zeta),p)=zeta^2 C(g0+w_0(zeta),p), since H(g0+w_0(zeta),p)=zeta^2 at s=0.
- d=2: [s^j]c_2=C(g0,p)=C(-1/t,1)p^(10-j) nonzero, [s^j]c_0=[s^j]c_1=0.
- d=3: M(g0)=0 with L(g0)=p(t-1)/t nonzero, so C(g0)=0 and the zero is simple; C_g(g0)=lambda p^(8-j) t L(g0)=lambda(t-1)p^(9-j); w_0'(0)=1/(a p^(3/2)); therefore [s^j]c_3=lambda(t-1)p^(15/2-j)/a nonzero and [s^j]c_n=0 for n<=2. Coalesced (3) and separated lines 85-87 state exactly this.
- Signs and embeddings. zeta to -zeta sends c_n to (-1)^n c_n and preserves every ord(c_n), r and kappa; the second embedding only changes unit values. r is finite (ord c_d=j) and positive (all ord c_n>=j>=1), with r<=j/4<=9/4 or r<=j/3<=2.
- Retained constants. alpha s^10 R_s and a0 s^15 are later than 6r (coalesced, r<5/2) and than 3eta (separated, eta<5). The five B kernels sit inside E_s=B_s-R_s^5 in sK[s,g,p] (coalesced) or are explicit with orders 25-5i+i eta, later than 5eta by (5-i)(5-eta)>0 (separated).
- No nilpotent object is used anywhere; every ring is E, E[[s^(1/N)]] or E[Y].

Attacks tried: a p-pole moving an s-order (impossible, orders are s-adic); C(g0,p) vanishing in stratum 1 (excluded by definition); a g-dependent quotient D (excluded by deg_g C<=2). No hidden hypothesis found.

## 3. Verdict 2, coalesced kappa>=2r: CONFIRMED

Replay. With zeta=s^r Y after one Puiseux extension, c_n zeta^n has order ord(c_n)+nr. For n<=d this is >=6r with equality for some n by the definition of r; for n>d it is >=j+(d+1)r>=(6-d)r+(d+1)r=7r. So F has a nonzero initial U(Y) of degree<=d at order 6r, and distinct Y-degrees cannot cancel. Under kappa>=2r, R_s=s^(2r)(Y^2+b+...) with b=xi_(2r), zero unless kappa=2r and zero at kappa=infinity where xi_s=0; b has p-degree 5-2r=2h, matching Y^2. Then P=(Y^2+b)^3+U(Y) is monic of degree 6 at order 6r, the A scalars being later by 10+2r>6r and 15>6r.

B control. e_n zeta^n with ord e_n>=1 has order>=1+nr, so at any nu<=10r only n<=10-1/r<10 enters; R_s^5 supplies the unique monic Y^10 at 10r. If the first B initial Q sits at nu<10r its degree obeys nr<=nu-1. The chain rule gives [A,B] in (zeta,p) equal to g_zeta times c s^36 g^2, of order exactly 36 with leading c p^(1/2)/(t^2 a); passing to (Y,p) multiplies by s^r, so [P,Q]_(Y,p)=0 whenever 5r+nu<36, which holds since 15r<=135/4 or 30. The Y^(5+n) coefficient of [P,Q] is 6 times the p-derivative of q_n because P_p has degree<=5 and Q_Y degree n-1; Euler gives p q_n'=(25-nu-nh)q_n with 25-nu-nh>(5/(2r))(10r-nu)>0, so q_n=0, n=0 included. Hence nu=10r, Q monic of degree 10, D Q=10hQ and D P=6hP with h=5/2-r>0. Then p[P,Q]=h(10P_Y Q-6P Q_Y)=0, Q^3/P^5 is Y-constant and by monicity equals 1, and UFD in E[Y] gives P=W^3 with W=Y^2+uY+v. The Y^5 coefficient of W^3 is 3u, so u=0; the Y^4 coefficient is then 3v while P's is 3b because U of degree<=3 cannot reach Y^4; so v=b, W^3=(Y^2+b)^3 and U=0, contradiction. The degree bound d<=3 is exactly what defeats the harmless common-quadratic case.

Attacks: sign cancellation inside U between attaining n (impossible, distinct degrees); an E-term of degree 10 at 10r (excluded by ord e_n>=1, and the producer's own -zeta^10 remark correctly marks (5) as load-bearing); infinite ord c_0 or c_1 (harmless, the minimum is attained at finite orders); kappa=infinity (b=0, everything else unchanged). No gap.

## 4. Verdict 3, separated even/odd regrouping: CONFIRMED

U_l=sum over m>=l of binom(m,l) c_(2m)(-xi_s)^(m-l), and V_l likewise with c_(2m+1). The m-th term has order>=j+(m-l)kappa, tending to infinity because kappa>=1, so each U_l and V_l converges s-adically with order>=j, and U(xi_s+zeta^2)=sum c_(2m)zeta^(2m) holds by rearrangement, since below any s-order only finitely many (m,l) enter. Strictness of (2) survives summation because the value group is discrete and cancellation only raises order. ord U_1=j for d=2: the m=1 term is c_2 of order j, and every m>=2 term has order>=j+kappa>j. ord V_1=j for d=3 from c_3 identically. These are properties of the actual moving series, not static branch values. Sheets zeta_pm=pm a_s(1-z/xi_s)^(1/2) with a_s^2=-xi_s: the leading xi_kappa is const p^(5-kappa), so a_s lies in E[[s^(1/2)]] with order kappa/2. Before z=s^eta Z the binomial tail carries negative s-orders kappa/2-b kappa; the proof never treats that pre-substitution object as a positive-order series, and the sheet compositions converge because for fixed z-degree the orders ord c_n+n kappa/2 tend to infinity. No reduction of the double component to a reduced product occurs; both sheets remain field objects throughout.

## 5. Verdict 4, r-to-eta arrow and the depressed cubics: CONFIRMED

kappa<2r gives r>kappa/2. For n<=d, ord c_n>=(6-n)r>(6-n)kappa/2; for n>d, ord c_n>=j>=(6-d)r>(6-d)kappa/2; in both cases ord(c_n)+n kappa/2>3kappa, infinite orders included. Through the binomials, ord U_l+l kappa>3kappa and ord V_l+kappa/2+l kappa>3kappa, hence q0>3kappa, q1>2kappa and eta=min(q0/3,q1/2)>kappa; q1 is finite by ord U_1=j or ord V_1=j; eta<=j/2 for d=2 and eta<=j/2+kappa/4<2j/3 for d=3, so eta<j and eta<5. After z=s^eta Z the b-th binomial correction of any base term is later by b(eta-kappa)>0; this is the only place strictness is consumed and it is genuinely needed, since at eta=kappa the shift is zero (control). Terms with l>=2 have order>=j+2eta>3eta, the l<=1 base families have order>=3eta, and one attains it by the definition of eta. alpha and a0 are later because eta<5. On each sheet the A initial is Z^3+u Z+v at 3eta; the tuple (u_+,v_+,u_-,v_-) is nonzero because each attained base contributes (alpha+beta, alpha-beta) with (alpha,beta) nonzero in characteristic zero, while one whole sheet may vanish when alpha=beta. Grading: Z has degree h=5-eta>0 and every coefficient is a constant times a rational power of p, so (p d_p+hZ d_Z)P_pm=3h P_pm sheet by sheet with no constant shared across sheets. A Z^2 term at 3eta could only come from l=2 bases, which are later, so both cubics are depressed. Identifying the two signs would be unsound, since (a+b,a+b) vanishes at a=-b nonzero (control); the proof does not identify them.

## 6. Verdict 5, global earliest G and complete B: CONFIRMED

The coalesced positivity lemma is correctly not imported: on a sheet e_n zeta_pm^n spreads over all Z-degrees with orders 1+n kappa/2+b(eta-kappa), which bounds no Z-degree below 5eta. Instead ord_s G>=2j from the source, with every kernel retained, gives ord [z^l]U_G and ord [z^l]V_G>=2j after the same regrouping. The global earliest order nu of G on the pair equals the minimum of the base orders ord U_(G,l)+l eta and kappa/2+ord V_(G,l)+l eta: binomial corrections are strictly later than their own base, distinct l have distinct Z-degrees, and at each attaining l the pair alpha_l pm beta_l is nonzero on at least one sheet. If nu<5eta then 2j+l eta<=nu<5eta forces l=0 for d=2 (2j>=4eta) and l<=1 for d=3 (2j>3eta); on the sheet where Q is nonzero it is B's initial because R_s^5, the kernels and q_s(z)F sit at or above 5eta. The transformed bracket in (z,p) is (dg_pm/dz) c s^36 g_pm^2 with dg_pm/dz=g_zeta/(2 zeta_pm), of order exactly 36-kappa/2 and leading pm c p^((kappa-4)/2)/(2 t^2 a sqrt(-xi_kappa) const), whose p-degree 34-(36-kappa/2) matches the combined degree 34 of the bracket. Passing to (Z,p) multiplies by s^eta, so the (z,p)-order of [P,Q] is 2eta+nu<7eta<36-kappa/2 in both strata (15j/4<=135/4 and 5j<=30). The Z^(n+2) coefficient of [P,Q] is 3 q_n' because P_p has degree<=1, and Euler p q_n'=(25-nu-nh)q_n with 25-nu>0 for n=0 and 20-nu+eta>20-4eta>0 for n=1 kills q_n; P's homogeneity is not used here. Hence every base order is >=5eta, corrections at 5eta are still absent, and G contributes at most ell_pm Z+e_pm at 5eta by the same degree bound; both are retained. The complete B initial is Q_pm=Z^5+(5/3)Z^2(u_pm Z+v_pm)+ell_pm Z+e_pm: the q_s terms (4/3)b4 s^5 zF and (b3-5alpha/9)s^10 F are later by 5-eta and 10-2eta, kernels by (5-i)(5-eta), so Z^5 is the unique leader with coefficient 1. No earlier term, competing leader or later implicit correction was missed.

## 7. Verdict 6, target, Euler and composition scope: CONFIRMED

On each sheet [P_pm,Q_pm]=0 at (z,p)-order 3eta+5eta-eta=7eta<36-kappa/2, with h=5-eta>0 and both initials homogeneous of Euler degrees 3h and 5h over the field E. Then p[P,Q]=h(5P_Z Q-3P Q_Z)=0, Q^3/P^5 is Z-constant and equals 1 by monicity, UFD in E[Z] gives P=W^3 with W=Z+w0 linear monic, and the vanishing Z^2 coefficient forces w0=0, so u_pm=v_pm=0 on that sheet. On both sheets this contradicts the nonzero tuple; a sheet with identically zero correction yields no contradiction by itself and none is claimed. Identity of objects: both reports use the identical A-only F, the identical chart (same g_c, xi_s, Hessian a_s, E, sign freedom), the identical c_n and the identical r formula with the same d per stratum; kappa>=2r and kappa<2r partition [1,infinity]. Composition: for every literal source pair with F_j=HC nonzero and either M not dividing C or LM dividing C, no kappa is possible. Nothing is asserted for M|C with L not dividing C, for the non-H-divisible branch beyond the accepted 15m record, or for simple-L, whole golden, common, D125, reverse lift, coefficient schemes, properness or JC2. The lower-B step uses only q_n'=0 and Lambda distinct from nh; the final step uses two homogeneous monic initials over a field; neither is ported to dual numbers.

## 8. Non-fatal hazards for the next reader

- The separated proof reuses the symbol a_s for sqrt(-xi_s) at line 129, while the source and the coalesced proof use a_s for the Hessian half (1/2)R_(s,gg)(g_c,p). Each text is internally consistent; a merged text must rename one.
- The prime in q_n' means the p-derivative in both proofs, fixed by the bracket definition rather than by a sentence.
- The coalesced 5r+nu and the separated 2eta+nu are (zeta,p)- and (z,p)-orders; both account for the s^r or s^eta from d_zeta or d_z.
- The separated pre-substitution sheets live in E((s^(1/N)))[[z]] with negative orders in the binomial tail; the text handles this only implicitly through eta>kappa. Correct, but one sentence would remove the ambiguity.

## 9. Evidence, budget and stop

Control scalar_control.py: exact Q(rho)/(rho^2-3rho+1) pairs with norm form a^2+3ab+b^2, expanding only the degree-5 identity H(g0+w,p) and the degree-2 factor LM; 22 positive identities (units and norms, the H expansion, (LM)(g0)=0 and its transverse derivative (t-1)p, the weight law 7j-46, all four 15r and 7eta+kappa/2 chains, both lower-B positivity bounds, the two-sheet tuple logic, the W^3 projections) and 4 changed-object rejections (rho=2 breaks t^2=rho and the H expansion; identified signs vanish at a=-b; eta=kappa gives zero binomial shift). Both modes rc=0 and 26/26 as expected; normal 0.02 s wall, 12 MB; optimized 0.09 s wall, 17 MB; under prlimit CPU 25 s and 512 MiB with python3 -I -B and -O, no inner timeout, no gating asserts. No H/R powers, A15/B25, degree 6/10 pair, CAS, solver, AWS, SSH, web, new agents, canonical edits, protected-tree inspection, live peers or external messages.

| box file | sha256 |
|---|---|
| scalar_control.py | `919003eefe8317f81d84f61be10d9a210270201df52a90d5d08620d5968a03af` |
| argv.txt | `3a7f49a102b8e4b321e1e1d3408b38379d2ae8d2480e37edac90cd5c5a07bbfe` |
| run_normal.stdout | `3259cb2f122067a78ccf50f7df8566a75f86c698612eb4db6e9668cd79df8bd8` |
| run_optimized.stdout | `d496ba2a6f059929d71afcc6d1ec971755c7e27e7873a4094bbad6fdbb64f651` |

Finite checks illustrate; the proofs above are the evidence. Unresolved targets: none. All writers terminal/IDLE; the lane publisher owns the seal.

<!-- BODY-END -->
