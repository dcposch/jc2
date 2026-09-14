# Scroll fiber-degree-one donor exclusion — Fable5.1 hostile gate (FIRST)

started_utc=2026-09-12T06:04:16Z (skeleton written before any input read). Reviewer: Fable5.1, independent hostile gate of Astra. Scope: producer-proof only, provisional FIRST, no descendants. The August 30 two-section log theorem, including its nonproper dominant-pullback clause, is an ACCEPTED PREMISE. The cubic report is scope/history only. MANUAL mathematics; the only execution was date, sha256sum, cat and edits of this file. HARD 06:23Z.

## 0. Custody

Hashed at 06:04:23Z before whole reads; all three equal the expected values:
- scroll-fiber-one-donor-astra-20260912.md 1aede0f67970ff01b9a599352086a7c72d51cf610e1ae52db088f9e3fc2f0997
- bd-a2-firstleg-log-kodaira-coordinator-integration-sol56-20260830.md ff25ba27388c02698013483e2e5537f18ed39e918e5cb0cb4c099a75ef42f298
- cubic-scroll-donor-exclusion-root-20260912.md f5abd9086559b1cfdd6900baafcf339c1a8ad394917ab3141d23bc999403545a

Whole reads of all three snapshots including seals. No links followed, no other file, no peer output, no corpus sweep.

## 1. Exact claim

Y=F_e, e>=0, pi the ruling, E^2=-e, f a fiber. Phi:Y->P2 finite, L=Phi^*O(1), L.f=1, ell ANY line, D=Phi^*ell, R=Ram(Phi), U=Y minus (supp D union supp R). Claim: no dominant everywhere-defined morphism A2->U, first leg of arbitrary degree, not assumed finite, etale or proper. Nothing else is claimed.

Overall: CONFIRMED at producer level modulo the accepted premise. Every step was re-derived below; no REFUTED item; residual GAPs are in section 4 and lie outside the exact statement.

## 2. Verdicts A-C

### A. CONFIRMED.
Finite implies surjective (closed image of dimension 2) and L ample (finite pullback of ample). L=aE+bf with a=L.f=1. Ample on F_e iff a>0 and b>ae, so b>=e+1 and d=L^2=2b-e>=e+2>=2. K_Y=-2E-(e+2)f gives K_Y+3L=E+(3b-e-2)f. Characteristic 0 makes Phi generically etale, so the Jacobian section of omega_Y tensor Phi^*omega_{P2}^{-1}=O(K_Y+3L) is nonzero; R is its zero divisor, effective, R~K_Y+3L, R.f=1. D is effective with D.f=L.f=1.
Support split: for an irreducible curve C, C.f=0 iff C is a fiber (f nef, fibers of F_e irreducible), otherwise C.f>=1. Fiber degree 1 with positive integer multiplicities forces exactly one horizontal component, of fiber degree 1 and multiplicity 1, in each of D and R; vertical components are unconstrained. No genericity of ell enters, so special lines are covered.
Section: C horizontal integral, possibly singular a priori. pi|C is a nonconstant morphism of projective curves, hence finite; its degree is deg O(f)|C=C.f=1, hence birational. A finite birational morphism onto the normal curve P1 is an isomorphism (O_{P1} -> pi_*O_C is a finite birational extension of an integrally closed sheaf, so equality). C is the image of a section and therefore smooth. Normality of C is never assumed; the logic is sound.

### B. CONFIRMED.
Suppose C_D=C_R=:C. By A the coefficient of C in D=Phi^*ell is 1, so at the generic point eta of C over the generic point xi of ell the local equation v of ell pulls back to a uniformizer: e(eta/xi)=1. The residue extension C(ell) in C(C) is separable (characteristic 0). An unramified extension of DVRs has Omega_{Y/P2,eta}=0, and over the DVR O_{Y,eta} the Jacobian order equals the length of Omega_{Y/P2,eta} (Smith normal form), so it is 0 and C is not in supp R. Contradiction.
Direct check: at a general p in C off the vertical components D=C locally, so x:=Phi^*v generates the ideal of C and, C being smooth, dx(p) is nonzero; complete to (x,t); Phi=(g,x); the Jacobian is -dg/dt; on x=0 it is the derivative of t->g(0,t), the map C->ell, nonconstant, whose derivative is not identically zero in characteristic 0. Both routes are correct and never use ell generic. Consequence I checked: if ell is a branch line, the component of R mapping onto ell lies in supp D, cannot be C_D by B, hence is a fiber F with mult_F(D)=e_F>=2. A branch line therefore always lands in the N>=3 branch of C.

### C. CONFIRMED.
Let B_1..B_N be the distinct prime divisors in supp D union supp R; N>=2 by B. Pic(F_e)=ZE+Zf is free of rank 2 (Hartshorne V.2.3), so this is linear equivalence, not numerical. N>=3 gives integers n_i not all 0 with sum n_i[B_i]=0 in Pic, hence sum n_i B_i=div(h). The B_i are distinct primes and some n_i is nonzero, so div(h) is nonzero and h is nonconstant. Y is smooth and div(h) is supported in Y minus U, so h is a unit on U. For psi:A2->U dominant of any degree, with no properness, psi^*h is a unit of C[x,y], hence a constant c, and psi^* is injective on function fields, so h=c. Contradiction. Multiplicities are irrelevant: a fiber shared by D and R, or a multiple fiber, is one distinct component and still the third one. Any vertical component in D or R closes the case.

## 2b. Verdicts D-F

### D. CONFIRMED.
N=2 means supp D={C_D}, supp R={C_R}, no vertical components; multiplicity 1 by A, so D=C_D and R=C_R are reduced smooth sections with D~L. h=Phi|D:D->ell is finite of degree deg L|D=L.D=L^2=d>=2.
Scheme identity at EVERY p in D: take target coordinates (u,v) at Phi(p) with ell={v=0}. Since Phi^*ell=D is reduced and smooth at p, x:=Phi^*v generates the ideal of D at p, so dx(p) is nonzero (if x=a x_0 with dx_0(p) nonzero then dx(p)=a(p)dx_0(p)). Complete to coordinates (x,t). Then Phi=(g(x,t),x) and the Jacobian determinant is det[[g_x,g_t],[1,0]]=-g_t, well defined up to units under coordinate changes, so R=div(g_t) near p and R|D=div(g_t(0,t))=div(h'(t)) with h(t)=g(0,t). Ram(h) is locally div(h') (ord_p h'=e_p-1 in characteristic 0) and h' is not identically zero because h is nonconstant. Hence Ram(h)=R|D as effective Cartier divisors at every point; a tangency of D and R is only a higher-order zero of h'; the restriction is legitimate because D is not inside R (B); whether ell is special never enters. Cross-check: deg R|D=R.L=4b-2e-2=2d-2=deg Ram(h) by Riemann-Hurwitz for P1->P1.
Two base points: e_p(h)<=d because the e_q over h(p) sum to d, so a single point carries at most d-1<2d-2. Thus supp Ram(h)=D cap R has at least two points; pi|D is an isomorphism, so they lie over two DISTINCT base points; S:=pi(D cap R) has |S|>=2. Target values of h play no role. No hidden genericity: the inputs are N=2, characteristic 0 and d>=2 only.

### E. CONFIRMED against the accepted premise.
Premise (Aug 30 section 1): P->P1 a P1-bundle, D_infinity a section, R' closed in P minus D_infinity with R'->P1 minus S an isomorphism, D_0 the closure of R'; then P_n-bar of P minus (D_0 union D_infinity) equals n(|S|-2)+1 for |S|>=2, independent of contact orders, and no dominant A2 first leg exists. Fit: P=F_e, D_infinity=D, R'=R minus D. Because pi|R is an isomorphism and its preimage of S is exactly R cap D, R' is closed in Y minus D and R'->P1 minus S is an isomorphism; the closure of R' is R (irreducible), meeting D exactly over S; the resulting open is U. |S|>=2 by D gives P_n-bar(U)>=1 and kappa-bar(U)>=0. The premise's pullback clause applies verbatim: A2->U dominant between surfaces is generically finite, U is smooth quasi-projective, nonproper is allowed, and P_n-bar(A2)=0 contradicts P_n-bar(U)>=1. No finiteness, etaleness or properness of the first leg is inserted; arbitrary degree is exactly what the premise covers. The premise makes no assumption on which section is named D_infinity, so D as infinity is legitimate.

### F. CONFIRMED.
Control: F_0=P1_t x P1_w, D_infinity={w=infinity}, D_0={w=t}, meeting only at (infinity,infinity). The map (w,z)->(t=[wz+1:z],w) is everywhere defined ([wz+1:z] is never [0:0]), lands in U (t=w would need wz+1=wz; z=0 gives t=infinity, not w), and (t,w)->(w,t_1/(t_0-w t_1)) is regular on U (the denominator vanishes only at t=[w:1], since t_1=0 forces t_0=0). Compositions: z/(wz+1-wz)=z and [w t_1+t_0-w t_1:t_1]=t. So U is A2 and kappa-bar=-infinity, matching |S|=1 in the premise. Why it is not a finite-map D/R boundary: with f={t=c}, E={w=c}, e=0, the classes are D_infinity~E and D_0~E+f, while finite fiber-degree-one data need D~E+bf, b>=1, and R~E+(3b-2)f; D=D_0 forces b=1 and R~E+f, not [D_infinity]; D=D_infinity forces b=0, not ample; under the other ruling D_infinity is a fiber of degree 0. Independently, D proves |S|>=2, so a one-collision boundary never occurs. The control shows two smooth sections with positive contact are not by themselves an obstruction; the real obstruction is the finite-map ramification count.

## 3. Scope boundary

L.f=1 is used in three load-bearing places: uniqueness and multiplicity one of the horizontal components (A), pi|D an isomorphism so distinct points give distinct base points (D), and the two-SECTION shape of the premise (E). For L.f=a>=2 a horizontal component can be an irreducible singular a-section, D or R can have two horizontal components with N=2 and no forced unit, and two ramification points of h can share a fiber; the premise's multisection version does not exist. Pic rank 2 and the P1-bundle structure are used in C and E. Hence nothing follows for other rational surfaces, other compactifications, quartic or arbitrary covers, block quotients, Keller realizations or JC2. The cubic F_1 report is the instance e=1, b=2, d=3: its quartic F_alpha not being a fourth power is exactly |S|>=2 with e_p<=3, so the new theorem subsumes it without its net classification. Priority checksum stays with ROOT.

## 4. Residual GAPs (none inside the exact statement)

- G1, external premise: the Aug 30 theorem and its nonproper pullback clause are accepted, not re-proved here.
- G2, standard imports cited not re-proved: Pic(F_e)=Z^2, the ampleness criterion, finite birational onto normal is an isomorphism, unramified iff Omega=0 for DVRs, Riemann-Hurwitz.
- No numerical or CAS check was run or authorized. Existence of instances is not needed, but the quadric double cover (e=0,b=1) and cubic scroll (e=1,b=2) show the family is nonempty.

Verdict: CONFIRMED. Provisional FIRST, producer-proof only, no descendants; this report authorizes no execution, allocation, downstream theorem or promotion.

<!-- BODY-END -->
