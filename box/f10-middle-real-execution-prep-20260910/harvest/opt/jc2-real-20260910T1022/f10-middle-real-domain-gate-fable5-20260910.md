# f10-middle-real-domain-gate-fable5-20260910 — FIRST Fable5.1 hostile gate: exact whole-domain certificate contract

status: UNSEALED (adapter seals; no Seal section and no charge_basis authored here; the standalone BODY-END marker is the last line)
lane: f10-middle-real-domain-gate-fable5-20260910
first_action_utc: 2026-09-10T08:36:38Z
stop_utc: 2026-09-10T08:50:38Z (first+14 min, earlier than 08:52:00Z); reserve 08:48:38Z; never reset
mode: manual math/text/hash only; zero subprocess/CAS/script arithmetic; every number below is hand arithmetic
owned: xmodel/f10-middle-real-domain-gate-fable5-20260910.md, box/f10-middle-real-domain-gate-fable5-20260910/ (both absent at first action, ls 08:36:38Z); all writes apply_patch

## 0. Charged inputs (sha256, hashed BEFORE any body was read)

ROOT custody 5df8860d / expected transaction 8044d57e / writers idle 08:25:59 are taken as stated by the charge, not re-derived. Premises: accepted 17zz (E_X, Q_X, P, ell, Z), 17zzb (D_u, K_u, beta, gamma, ell unit), 17zzd (D/K division, Bezout, S, T, seven-point reduction) at their inherited scopes; the inherited 17o/17s/17zw excerpt-read qualification is preserved. Later residue/ell/r2-source reports are not inputs.

| # | file | sha256 | status |
|---|------|--------|--------|
| 1 | f10-middle-real-domain-astra-20260910.md | 3f79cabecdb2c0f480bde3db644eac91ea5c8d3d472a3477f575b356993347ea | MATCH |
| 2 | READ-SCOPE.md | 0496a56a58b755f6439f6354024d5f9730633d78271fca8e37b4036fd4ec6e31 | MATCH |
| 3 | ROOT-CARD.md | c920e030caba5b5a516b8b93a3ee1f0c3580feeac233cfcd8d206ae26b3b3c2b | MATCH |
| 4 | f10-middle-resonance-unit-astra-20260910.md | 8cf54b2f78840ced62fd35722da6d0d969eedd3344aa07d4ab08ff62c50df012 | MATCH |
| 5 | f10-middle-resonance-unit-gate-fable5-20260910.md | dc43ef1cfba68da21d0e26f6422e6af626d15a75d551858e72e78c7236ac27ad | MATCH |
| 6 | f10-middle-full-boundary-astra-20260910.md | 82f11ed717d1691bb37c36242fdd9eb1eea23ec5eb46b42db5590b1997db18e6 | MATCH |
| 7 | f10-middle-full-boundary-gate-fable5-20260910.md | 8a80bcc8ad7dd9068b503e9b1e18b4a5e6532d70f559658e3aa7077ec1928491 | MATCH |
| 8 | f10-middle-univariate-unit-astra-20260910.md | 890e5c9c63a333bf873e963821c368d2dc080476eaf12c9fc6a10dce53db75e5 | MATCH |
| 9 | f10-middle-septic-gate-fable5-20260910.md | cff18a06c050d64074ba9af70cea61b28b15614a61691125ebf26d3012577c62 | MATCH |

All nine equal the charged list; all nine were read WHOLE after the match (rows 1-3 by cat, rows 4-9 by whole-file read), including the accepted premise reports. No provenance followed, no other file opened. The producer's Seal was not recomputed (nothing here depends on it).

## A. Triangle, rectangle map, real-tau Bezout, real-tau guard: CONFIRMED

Triangle. tau=r/(3r+1) is 2/7 at r=2 and increases to 1/3, so 2/7<=tau<1/3. alpha=(8r+3-h)/m over h=r+2..2r runs from (6r+3)/m=3-3tau (h=2r) to (7r+1)/m=1+4tau (h=r+2); check 3m-3r=6r+3 and m+4r=7r+1. Width 7tau-2=(7r-6r-2)/m=(r-2)/m, zero exactly at r=2: the collapsed edge is the single actual point (2,4), alpha=15/7.

Rectangle. tau=(6+t)/21 gives 7tau-2=(42+7t-42)/21=t/3, so t in [0,1) is exactly 2/7<=tau<1/3, t=1 being tau=1/3 (r infinite, excluded). alpha=3-3tau+(7tau-2)s=(63-18-3t)/21+7ts/21=(45-3t+7ts)/21, equal to ROOT-CARD's 15/7-t/7+ts/3. Surjective: t=21tau-6, and for t>0 s=(alpha-3+3tau)/(7tau-2) lies in [0,1]; at t=0 every s gives alpha=15/7. s=0 is h=2r (delta=4tau-1), s=1 is h=r+2 (delta=1-3tau): both actual edges. CONFIRMED.

Real-tau Bezout. K=qD+56f(V-v*), D=e+(V-v*)J are polynomial identities in (tau,V) (accepted 17zzd (1), rechecked by the septic gate); AD+BK=(D-(V-v*)J)/e=1 needs only f,e nonzero. f=(2tau-1)(3tau-1)(3tau-2) vanishes at 1/3,1/2,2/3; e=(1+tau)(6tau-1)/49 at -1,1/6; neither in [2/7,1/3). Q_u-7E_u=K+210DW is a polynomial identity in u, so for every real tau, in F[V,W]/(E,Q) with F=Q(tau,alpha) one has K=-210DW and D(A-210BW)=1. S=245D^2E_nu(V,-K/(210D)) is formal in tau; lc_V S=-245*120*144*tau is nonzero (tau>=2/7), so F[V]/(S) is a 7-dimensional F-algebra; gcd(S,D)=1 from S=2K^2 mod D and (BK)^2=1 mod D. Hence F[V,W]/(E,Q)=F[V]/(S) at every real tau of the triangle, with only f,e inverted. CONFIRMED.

Real-tau guard. nu=2-tau lies in (5/3,12/7], so (nu)_2,(nu)_3 are nonzero and E=Q=0 gives t6(nu)=t7(nu)=0, d=c^nu+O(z^8). Then c d'-nu c'd=c(nu c^(nu-1)c'+O(z^7))-nu c'(c^nu+O(z^8))=O(z^7), degree <=7, z^7 coefficient 5Wt5-3nu Wt5=(5-3nu)Wt5: the displayed identity is exact (it is 17zz's -Wt5 z^7 divided by m). In a maximal residue field kappa of the finite F-algebra (a finite, possibly non-real extension of F), Wt5=0 forces c d'=nu c'd in kappa[z]. deg c=p in {1,2,3} (z-coefficient 1), deg d=q>=1 (z-coefficient nu nonzero; q=0 would force c'=0). Leading terms give q=nu p. Ratios q/p with p<=3, q<=5 near the interval: 3/2, 5/3, 2, 4/3; none lies in the open-closed interval (5/3,12/7] (5/3 is excluded because tau<1/3 strictly). So Wt5 lies in no maximal ideal and is a unit of the whole finite algebra; complex V,W are allowed, no etale or reducedness hypothesis is used. CONFIRMED. (The nonvanishing of 5-3nu=3tau-1 is not even needed: the argument only uses that the right side is zero when Wt5 is.)

## B. Degrees of S,T, three-step division by the unit 10080: CONFIRMED

Own total degrees in (tau,V) from the accepted displays: D has terms V^2, tauV, tau^2: <=2. K: V^3, tau^2V^2, tau^3V, tau^4: <=4, deg_V 3. gamma=tau[(1+tau)(2+tau)(3+tau)-30(1+tau)(2+tau)V+180(1+tau)V^2-120V^3]: <=4, deg_V 3. So 2K^2<=8, 140tau(1+tau-6V)KD<=1+1+4+2=8, 245gamma D^2<=8; deg_V S=7 with V^7 coefficient -4233600tau. T=DP-ellK: A=sigma-7, B2, B3 have (tau,alpha)-degree 1,2,3 and alpha-degree 1,2,3, so P has total degree <=3, alpha-degree <=3; DP<=5 with V^5 coefficient 12*840=10080 (parameter-free); ellK<=1+4=5, alpha-degree 1, deg_V 4. Hence deg_V T=5, totaldeg T<=5, deg_alpha T<=3, lc_V T=c0=10080. Coefficientwise: S_i has parameter degree <=8-i, T_j<=5-j. CONFIRMED.

Division: q2=S_7/c0, q1=(S_6-q2T_4)/c0, q0=(S_5-q2T_3-q1T_4)/c0: three steps, denominators c0,c0^2,c0^3; Frem=S-QdivT has denominator c0^3 and deg_V<=4. Degrees: q2<=1, q1<=max(2,1+1)=2, q0<=max(3,1+2,2+1)=3, i.e. Qdiv_i<=3-i; Frem_i<=max(8-i,(3-k)+(5-i+k))=8-i. Upper bounds survive any degree drop of Frem, and the contract keeps the zero slots. No parameter coefficient is inverted. CONFIRMED.

## C. Padded 9x9 Sylvester map, adjugate identity, c0^15, degree bounds, resultant relation, deg_alpha R=21: CONFIRMED

Columns V^i Frem (i=0..4, degree <=8) and V^j T (j=0..3, degree <=8), rows V^0..V^8: the Sylvester matrix of (Frem at formal degree 4, T at degree 5), size 4+5=9. Madj(M)e_0=det(M)e_0 says sum a_iV^iFrem+sum b_jV^jT=det M as polynomials, so A Frem+B T=det M with deg_V A<=4, deg_V B<=3; substituting Frem=S-QdivT gives A S+(B-A Qdiv)T=det M, hence (2) with U=c0^15A, Wcof=c0^15(B-A Qdiv), deg_V Wcof<=max(3,4+2)=6. Denominators: det M has five Frem columns, c0^15; a_i is a cofactor omitting one Frem column, c0^12; b_j omits a T column, c0^15; A Qdiv costs c0^12*c0^3. So U, Wcof, R are integral. Equivalently R is literally the determinant of the integer matrix with columns V^i(c0^3Frem), V^jT. CONFIRMED.

Weights: entry (row k, column V^iFrem) is Frem_(k-i), degree <=(8+i)-k; entry (k, V^jT) is T_(k-j), degree <=(5+j)-k. Column weights sum to (40+10)+(20+6)=76, row weights to 36, so deg R<=40. Cofactor omitting row 0 and Frem column i: 76-(8+i)-36=32-i; omitting T column j: 35-j; Wcof_j collects b_j and a_iQdiv_(j-i) of degree <=(32-i)+(3-j+i)=35-j. All four bounds CONFIRMED.

Resultant relation: Res(S,T)=-Res(T,S)=-lc(T)^(7-deg Frem)Res(T,Frem), and the padded determinant is (up to sign) lc(T)^(4-deg Frem)Res(T,Frem); the quotient is c0^3 independent of the actual degree of Frem, and both sides vanish together if Frem=0. So det M=+-c0^-3 Res_V(S,T), drop-safe; R=+-c0^12 Res_V(S,T). CONFIRMED.

alpha-degree: [alpha^3]B3=[alpha^3](alpha+nu)^3=1, B2 and A have lower alpha-degree, ellK has alpha-degree 1, so [alpha^3]T=D(V) exactly. Res(S,T)=lc(S)^5 prod T(v_i) over the seven roots of S, whose alpha^21 coefficient is lc(S)^5 prod D(v_i)=lc(S)^3 Res(S,D). For every tau of the triangle lc(S) is nonzero and gcd(S,D)=1, so this coefficient is nonzero pointwise in tau: for each fixed tau, R(tau,alpha) is a polynomial of exact alpha-degree 21. Its tau-degree is <=3+16=19=40-21, consistent. This is nonvanishing of one coefficient, hence R not identically zero and a fixed alpha-degree; the producer says exactly "not necessarily nonzero everywhere" and never upgrades generic to pointwise nonvanishing of R itself. CONFIRMED.

## D. Rectangle substitution, licensed (1-t)^j, fixed Bernstein test, excluded-edge vanishing: CONFIRMED

A monomial tau^a alpha^b (a+b<=40, b<=21) becomes 21^(40-a-b)(6+t)^a(45-3t+7ts)^b: integral, t-degree <=40, s-degree <=21. Rhat=21^40 R(...) has bidegree <=(40,21). At tau=1/3: D=12V^2-8V+4/3=12(V-1/3)^2; f(1/3)=0 so K=qD; then S=D^2(2q^2-140tau(1+tau-6V)q+245gamma) and T=D(P-ell q). Common factor D of positive degree gives Res_V(S,T)=0 for every alpha, so Rhat(1,s)=0 and (1-t)|Rhat: j>=1 is a theorem, and (1-t)^j>0 on t<1 licenses its removal. t, s, 1-s are the actual edges t=0, h=2r, h=r+2 and may not be removed. CONFIRMED.

Bernstein. G of bidegree <=(40-j,21) has a unique expansion in the tensor Bernstein basis of bidegree (A,21). Every basis element is >=0 on [0,1]x[0,1]; for t<1 the i=0 row is (1-t)^A>0 times the degree-21 basis in s, and (1-s)^21, s^21 are never simultaneously zero. So b>=0 for all (i,jj) and b_00,b_0,21>0 give G>0 at every t<1, s in [0,1], including t=0, s=0, s=1. Then R(tau,alpha) is nonzero on the whole triangle, and specializing the identity (2), which lives in Z[tau,alpha,V], any common complex root of S,T would give R=0: no common root. Failure of this sufficient test proves nothing, and the contract correctly says INCONCLUSIVE with no automatic elevation, subdivision, extra factor or sample. CONFIRMED.

Own precision (not a defect): on the collapsed edge Rhat(0,s)=21^40 R(2/7,15/7) is constant in s, so b_0,jj=eps*Rhat(0,0)=|Rhat(0,0)| for every jj; the condition b_0,21>0 is automatic once eps is fixed, and equality of all 22 entries b_0,jj is a free consistency check on any future expansion.

## E. Verification contract, refutation contract, outcome semantics: CONFIRMED

Success: an independent checker reconstructs S,T from the pinned formulas, multiplies U S+Wcof T, and compares every (tau,alpha,V)-coefficient with R (including that every V^k, k>=1, coefficient is zero), then checks Rhat=eps(1-t)^jG and the exact Bernstein expansion equality and signs. None of this uses the determinant engine, a resultant, or the degree bounds (3) except to size the expansion; a wrong bound is caught by the identity failing. Denominators: only integer constants, as required. CONFIRMED.

Refutation: a point of the triangle is a pair of real algebraic numbers, given in one number field Q[x]/(p) with p squarefree and an isolated real root; domain membership is the exact sign of 21tau-6>=0, 1-3tau>0, alpha-3+3tau>=0, 1+4tau-alpha>=0 at that root; the witness is a monic common factor of the specialized S,T of degree 1..5 (deg T=5), with both exact divisibilities. Since gcd over F[V] equals gcd over C[V], such a factor exists over F whenever one exists over C, so the contract loses nothing. lc(T)=10080 and lc(S) nonzero on the triangle mean R=0 there is equivalent to a common root, but the exhibited factor is the stronger, engine-independent form. A float, a t=1 point (where R vanishes identically) or an unsupported/capped/negative Bernstein output is INCONCLUSIVE, exactly as stated. The 360 s/330 CPU s/2 GiB/16 MiB figures are unmeasured and unauthorized in the producer; they carry no performance meaning here. No actual-integer resonance, source-exclusion or JC2 theorem is asserted, and success would only give H7-unitness at every actual pair through the accepted seven-point reduction, nothing about full sources. CONFIRMED.

## Verdicts, smallest correction, GAP

| item | verdict |
|---|---|
| A triangle bounds, collapsed t=0 edge, s=0/s=1 actual, t=1 excluded, Bezout with only f,e inverted at every real tau, guard by the q/p ratio table without etale | CONFIRMED |
| B totaldeg S<=8, T<=5, deg_alpha T<=3, deg_V 7/5, lc_V T=10080, three steps, c0^3, Qdiv_i<=3-i, Frem_i<=8-i drop-safe | CONFIRMED |
| C 9x9 padded map, A Frem+B T=det M, R=US+WcofT, c0^15 integrality, U_i<=32-i, Wcof_j<=35-j, deg R<=40, det M=+-c0^-3 Res, [alpha^3]T=D so deg_alpha R=21 pointwise in tau, no generic-to-pointwise upgrade of R | CONFIRMED |
| D 21^40 integrality, bidegree (40,21), only (1-t)^j removed with j>=1 proved, corner-term strictness on t<1, INCONCLUSIVE on failure, tau=1/3 factor D^2/D | CONFIRMED |
| E engine-free success check, exact real-algebraic refutation contract with domain/denominator/common-factor obligations, INCONCLUSIVE semantics, caps unmeasured, no resonance/source/JC2 theorem | CONFIRMED |

REFUTED: none. Attacks tried and failed: a hidden parameter denominator (only f,e in Bezout and c0 in division); a degree drop of S or T on the triangle (lc are tau and 10080); a ratio q/p=nu with p<=3, q<=5 (none in (5/3,12/7]); a wrong cofactor denominator count (Frem cofactors c0^12, T cofactors c0^15); a wrong weight sum (76-36=40); a padding defect when Frem drops degree (absorbed by lc(T) powers); an admissible edge hidden in (1-t)^j (only tau=1/3); a nonreal V,W escape in the guard (residue fields handled directly).

Smallest correction before any source implementation: none mathematical. Two contract precisions only. (P1) State that j>=1 is forced and that b_0,jj must all equal |Rhat(0,0)|; an artifact returning j=0 or unequal b_0,jj is defective and must be INCONCLUSIVE, not merely "sufficient test failed". (P2) The identity check must explicitly assert that U S+Wcof T has zero V^k coefficients for k>=1 (R is V-free by construction only if the artifact is what it claims). Neither changes a verdict, and neither is a scope upgrade.

GAP (unchanged, restated at the contract's scope): no whole-triangle nonresonance theorem exists; the contract is a sufficient certificate whose outcome is unknown, and a failure would not refute anything. Real-algebraic zeros of R off the linked integer lattice would refute only the strengthened real route, not any actual pair. No computation was run, requested or authorized here.

## OPEN(S) RAISED

None. No new canonical OPEN ID; the sole unresolved quantity remains gcd(S,T)=1 uniformly at actual (r,h), now with one fully specified bounded exact test (identity (2)-(3) plus the fixed Bernstein witness) that ROOT may register; nothing here registers, prices or executes it.

## COLLISIONS

status: EMPTY

- NONE. Own-only check: this lane wrote exactly xmodel/f10-middle-real-domain-gate-fable5-20260910.md and box/f10-middle-real-domain-gate-fable5-20260910/input_custody.md, both absent at first action; apply_patch only; no Seal, no charge_basis, no coefficient artifact, no subprocess, no rerun of any accepted report. Every 64-hex token in this file equals a charged input hash from live sha256sum output.

## Completion

Authoring attestation: both owned files were written by apply_patch only (custody file 08:42, body 08:43, this section 08:44 UTC); no Write/Edit tool, no heredoc redirection, no helper inspection. Own WHOLE read of this report completed 08:44:11 UTC with a hex-token audit against the live sha256sum output (no foreign token) and a marker-absence check; raised-OPEN check (none) and collision check (EMPTY) precede the marker and the 08:48:38 reserve. No follow-on, computation, registration or seal is authored. The marker below is the only standalone marker in this file and nothing follows it. All writers idle at the marker.

<!-- BODY-END -->
