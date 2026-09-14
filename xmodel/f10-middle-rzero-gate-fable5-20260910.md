# f10-middle-rzero-gate-fable5-20260910 — FIRST Fable5.1 hostile gate: middle unitness for all 7-divisible r

status: UNSEALED (adapter seals; no Seal section and no charge_basis authored here)
lane: f10-middle-rzero-gate-fable5-20260910
first_action_utc: 2026-09-10T07:54:16Z
stop_utc: 2026-09-10T08:08:16Z (first+14 min, earlier than 08:10:00Z); reserve final 2 min; never reset
mode: manual math/text/hash only; zero subprocess/CAS/Python/script arithmetic; every number below is hand arithmetic
authoring: apply_patch only (stdin heredoc input); no Write/Edit tool, no heredoc redirection
owned: xmodel/f10-middle-rzero-gate-fable5-20260910.md, box/f10-middle-rzero-gate-fable5-20260910/ (both absent at first action, checked by ls)

## 0. Charged inputs (sha256, hashed BEFORE any body was read)

| # | file | sha256 | status |
|---|------|--------|--------|
| 1 | f10-middle-rzero-unit-astra-20260910.md | f6419218e5073c13c8f315210ae84410a10cc47af8ce382025e4d1a7dfc6bcd9 | MATCH |
| 2 | READ-SCOPE.md | db3dc2c29e2a5469640bfd654047493ce3a8c1999434cd2f42387ea34839890f | MATCH |
| 3 | ROOT-CARD.md | ca3c61462e0e2911d83aa1e8ebe6a5b642eb53ddcc0bb11cc1a4ca365ba18df0 | MATCH |
| 4 | f10-middle-resonance-unit-astra-20260910.md | 8cf54b2f78840ced62fd35722da6d0d969eedd3344aa07d4ab08ff62c50df012 | MATCH |
| 5 | f10-middle-resonance-unit-gate-fable5-20260910.md | dc43ef1cfba68da21d0e26f6422e6af626d15a75d551858e72e78c7236ac27ad | MATCH |
| 6 | f10-middle-full-boundary-astra-20260910.md | 82f11ed717d1691bb37c36242fdd9eb1eea23ec5eb46b42db5590b1997db18e6 | MATCH |
| 7 | f10-middle-full-boundary-gate-fable5-20260910.md | 8a80bcc8ad7dd9068b503e9b1e18b4a5e6532d70f559658e3aa7077ec1928491 | MATCH |
| 8 | f10-middle-univariate-unit-astra-20260910.md | 890e5c9c63a333bf873e963821c368d2dc080476eaf12c9fc6a10dce53db75e5 | MATCH |
| 9 | f10-middle-septic-gate-fable5-20260910.md | cff18a06c050d64074ba9af70cea61b28b15614a61691125ebf26d3012577c62 | MATCH |

All nine equal the charged list and ALL NINE were read WHOLE after the match (rows 1-3 directly; rows 4-9 whole via one concatenated capture read in six contiguous line slices 1-110, 111-220, 221-330, 331-440, 441-550, 551-671 with no gap). No provenance followed, no other file opened. Producer custody df79d477 / expected transaction 11748643 / all writers idle 07:51:09 are taken as charged. Premises: accepted 17zz (E_X,Q_X display (5), Z/P/ell (6), identity (7), unit prefactor (8)), 17zzb (D_u,K_u identity (3), beta/gamma (8)), 17zzd (B_nu=Q[V]/(S), D unit, guard automatic, T=DZ of degree 5, lc 10080) exactly at their inherited read-scope qualifications. The prior three-family theorem is NOT used. No Seal, no charge_basis.

## A. Coefficient bounds (3) and root valuations (4)

Setup. 7|r, r>=7: m=3r+1 is 1 mod 7, a unit; tau=r/m has v(tau)=v(r)=k>=1; nu=2-tau is 2 mod 7; alpha=(8r+3-h)/m is 7-integral with residue 3-h. K=k0+7L with L=-120V^3+120(1-tau^2)V^2+6(1+tau)(2+tau)(4tau-3)V; k0=2(2-3tau)(1+tau)(2+tau)(3+tau) has residue 2*2*1*2*3=24=3 (nonzero); 120,6,(1)(2)(-3) are units, so L has exactly-unit coefficients in degrees 1,2,3. beta=120tau(1+tau)-720tau V: both coefficients valuation k (720=7*102+6). gamma: constant, V, V^2, V^3 coefficients have valuations exactly k (6, 30=2, 180=5, 120=1 mod 7). D=12V^2-12(1-tau)V+(1+tau)(2-3tau), unit coefficients.

S=2K^2-140tau(1+tau-6V)KD+245gamma D^2. 2K^2=2k0^2+28k0L+98L^2: degree 0 valuation 0; degrees 1-3 from 28k0L valuation exactly 1; degrees 2-6 from 98L^2 valuation >=2, degree 6 exactly 98*14400=2*840^2, valuation 2. Middle term: 140=7*20, so every coefficient >=k+1>=2; its degree-6 coefficient -140tau(-6)(-840)(12) has valuation 1+k+1=k+2>=3. Third term: 245=49*5 and gamma has valuation k, so every coefficient >=k+2>=3; degree 7 is 245*(-120tau)*144, valuation exactly k+2. Hence (3): v(a0)=0, v(a_i)>=1 (i=1..3, in fact =1), v(a_i)>=2 (i=4,5,6), v(a6)=2, v(a7)=k+2. CONFIRMED.

Roots. S(0)=a0 is a unit, so V=0 is not a root and t=v(V) is finite. t>-1/3: degree 0 has valuation 0; degrees 1-3 have >=1+it>1-i/3>=0; degrees 4-6 have >=2+it>2-i/3>=0; degree 7 has k+2+7t>k-1/3>0. -k<t<-1/3: degree 6 has 2+6t; degrees 1-3 exceed it by >=-1+(i-6)t>-1+(6-i)/3>=0; degrees 4,5 by (i-6)t>0; degree 7 by k+t>0; degree 0 by -2-6t>0. t<-k: degree 7 has k+2+7t; degree 6 exceeds by -k-t>0; degree 0 by -k-2-7t>6k-2>0; degrees 1-3 by >=-k-1+(7-i)(-t)>3k-1>0; degrees 4,5 by >=-k+(7-i)(-t)>k>0. In each open interval one term is uniquely least, so no root there (ultrametric). Endpoints t=-k and t=-1/3 are the only possibilities; -k is a negative integer and never equals -1/3. No multiplicity, root count or factorization is used. (4) CONFIRMED. Newton-polygon consistency (own remark, not needed): vertices (0,0),(6,2),(7,k+2) give six roots at -1/3 and one at -k, matching ROOT's exploratory picture.

## B. T bounds, the t=-k roots, the t=-1/3 valuations, (5) and (6)

T=DP-ell K, P=7(120V^3+60AV^2+6B2 V)+B3, ell=12V+A, D=12V^2+d1V+d0 with d1=-12(1-tau), d0=(1+tau)(2-3tau); A,B2,B3 7-integral for every h. c5=12*840=10080=7*1440, 1440=7*205+5: v(c5)=1 exactly. c4=12*420A+840d1+10080: all multiples of 7, v>=1. c3=12*42B2+420Ad1+840d0-840(12(1-tau^2)-A): v>=1. c2=12B3+42B2d1+420Ad0-12*42(1+tau)(2+tau)(4tau-3)-840A(1-tau^2): c2=12B3 mod 7, v>=0. c1=d1B3+42B2d0-12k0-42A(1+tau)(2+tau)(4tau-3), c0=d0B3-Ak0: v>=0. CONFIRMED.

t=-k: c5V^5 has valuation 1-5k; c4V^4 exceeds by >=k, c3V^3 by >=2k, c2V^2 by >=3k-1, c1V by >=4k-1, c0 by >=5k-1, all positive for k>=1. Unique least term, T(V)!=0 for every h. CONFIRMED. Precision: the nearest competitor is c4 (gap k), not the 3k-1 quoted; the quoted gap is the nearest among the weaker v>=0 bounds; conclusion unchanged.

t=-1/3: v(12V^2)=-2/3 < v(12(1-tau)V)=-1/3 < v(d0)=0, so v(D)=-2/3. v(120tau(1+tau))=k > v(720tau V)=k-1/3, so v(beta)=k-1/3. gamma terms k, k-1/3, k-2/3, k-1: v(gamma)=k-1. All CONFIRMED. E_nu(V,W)=0 with w=v(W): terms 2w, k-1/3+w, k-1. If 2w=k-1 then the middle term is k-1/3+(k-1)/2=(3k-5/3)/2, exceeding k-1 by (3k-5/3)/2-(k-1)=(k+1/3)/2>0. If w<(k-1)/2 then 2w<k-1 and 2w<k-1/3+w (as w<k-1/3), 360W^2 uniquely least. If w>(k-1)/2 then k-1<2w and k-1<k-1/3+w (as w>-2/3), gamma uniquely least. Balances 360W^2/betaW (w=k-1/3, gamma strictly lower) and betaW/gamma (w=-2/3, 360W^2 strictly lower) are impossible. So (5) w=(k-1)/2 follows from the full E_nu, never from a generic W. CONFIRMED. K=-210DW (Q_nu-7E_nu=0 at the point) gives v(K)=1-2/3+w=w+1/3>0. In K the terms 840(1-tau^2)V^2 and 42(...)V have valuations 1/3 and 2/3; the valuation-zero part is k0-840V^3=k0-120u, u=7V^3, v(u)=0. v(K)>0 forces residue 3-1*ubar=0, so ubar=3 in the residue field of the point (an element of F_7). (6) CONFIRMED.

## C. Residue (7) for every h not divisible by 7

T/V^2=c5V^3+c4V^2+c3V+c2+c1/V+c0/V^2 at t=-1/3: valuations 0, >=1/3, >=2/3, >=0, >=1/3, >=2/3. Residue of the valuation-<=0 part: 1440*ubar+c2bar=1440*3+12*B3bar; 1440=5, 5*3=15=1, 12=5 mod 7: residue 5*B3bar+1. (7) CONFIRMED. B3 is the polynomial divided difference of f(X)=(X-3)(X-4)(X-5)(X-6)=X^4-18X^3+119X^2-342X+360 at (alpha,nu), i.e. sigma^3-2sigma pi-18(sigma^2-pi)+119sigma-342, so no division by alpha-nu (which is a 7-nonunit when h is 1 mod 7) occurs. Reducing nu to 2: B3bar=[f(alpha)-f(2)]/(alpha-2) with f(2)=24; synthetic division of X^4-18X^3+119X^2-342X+336 by X-2 gives 1,-16,87,-168 with zero remainder: B3bar=alpha^3-16alpha^2+87alpha-168. Then 5B3+1=5alpha^3-80alpha^2+435alpha-839 = 5alpha^3+4alpha^2+alpha+1 mod 7 (80=3, 435=1, 839=6). And 5(alpha-3)(alpha^2+alpha+6)=5alpha^3-10alpha^2+15alpha-90 = 5alpha^3+4alpha^2+alpha+1 mod 7. Equal. CONFIRMED. Discriminant of alpha^2+alpha+6: 1-24=-23=5 mod 7; squares mod 7 are 0,1,2,4; 5 is a nonsquare; direct check alpha=0..6 gives 6,1,5,4,5,1,6, never 0. alpha is a rational 7-adic integer, so alphabar lies in F_7 even though V,W have residues in an extension; ubar=3 is also in F_7. alpha-3 has residue -h. Hence for every h with 7 not dividing h the residue is nonzero and T(V)!=0 at every t=-1/3 root. Uniform in the residue class of h, not a sample. CONFIRMED.

## D. The 7|h boundary via the full Q_alpha

7|h. e=(r+h)/m: 3-e=(9r+3-r-h)/m=(8r+3-h)/m=alpha. r+h>0 so e!=0; v(e)=v(r+h)-v(m)=v(r+h)>=1, a positive integer l (arbitrarily large when r+h is highly 7-divisible; the argument below is uniform in l). (5) and (6) depend only on tau, so they persist. Q_alpha from accepted 17zz (5) at X=3-e (X-3=-e, X-4=-(1+e), X-5=-(2+e), X-6=-(3+e)): constant e(1+e)(2+e)(3+e); V: -42e(1+e)(2+e)V; V^2: 420e(1+e)V^2; V^3: -840eV^3=-120e*u; W: 210e(1+e)W; VW: -2520eVW; V^2W: 2520V^2W; W^2: 2520W^2. Eight terms, none dropped. Constant+cubic = e[(1+e)(2+e)(3+e)-120u], bracket residue 6-1*3=3!=0, valuation exactly l. (8) CONFIRMED. 2520=7*360, v=1; v(2520V^2W)=1-2/3+(k-1)/2=(3k-1)/6=a; 3k-1 is 2 or 5 mod 6, never 0, so a is not an integer and a!=l. (9) CONFIRMED. Table: 42-term 1+l-1/3=l+2/3; 420-term 1+l-2/3=l+1/3; 210W-term 1+l+w; 2520VW-term 1+l-1/3+w=l+2/3+w; 2520W^2: 1+2w=k, and k>a since 6k>3k-1. Every listed term strictly exceeds min(l,a) (w>=0). So exactly one term of Q_alpha is least-valued and Q_alpha(V,W)!=0. CONFIRMED. At a common root of S and T: D(V)!=0 (gcd(S,D)=1 accepted), so Z=T/D=0; Q_nu=0 at the point; the polynomial identity Q_alpha-Q_nu=(alpha-nu)Z gives Q_alpha=0, contradiction. No unit property of alpha-nu is needed. Signs, 840/2520 valuations, and the residue 3 were rechecked. CONFIRMED. Notation: the producer's u=7V^3 is not 17zzb's temporary exponent u; flagged by the producer, no confusion in the proof.

## E. Whole-ring conclusion, controls, scope

Cover: every root of S in the algebraic closure of Q_7 has t=-k or t=-1/3 (A); t=-k roots are not roots of T for any h (B); t=-1/3 roots are not roots of T when 7 does not divide h (C) and not roots of Z, hence of T=DZ, when 7|h (D). So S,T have no common root over Qbar_7; a common factor over Q of positive degree would have a root in Qbar, which embeds in Qbar_7. gcd(S,T)=1 in Q[V]. Bezout aS+bT=1 in Q[V]; in Q[V]/(S)=B_nu (accepted 17zzd, guard automatic, no localization) bT=1 and T=DZ give Z^-1=bD in the ENTIRE B_nu. No component, guard, nilpotent or source/forcing equation is deleted; irreducibility of S is neither used nor claimed, and squarefreeness is not needed. H7_h=s^7(alpha)_3(alpha-nu)Z/5040 with rational-unit prefactor (accepted 17zz (8)), so H7_h is a unit of B_nu[s,s^-1] and of every base change, since ring maps preserve units. CONFIRMED.

Controls, each a genuine changed object: (i) omitting 7|h: the residue (7) is 5(alpha-3)(...) and alpha-3 has residue -h, so (7) vanishes identically on that class and section 3 alone proves nothing there; section 4 is load-bearing. (ii) dropping E_nu: w is then free, a=1/3+w can equal l (e.g. w=l-1/3), and the unique-minimum argument in D fails; likewise (6) needs v(K)>0 which comes from w>=0. (iii) tau=0: a7=0, beta=gamma=0, S=2K^2 of degree 6 with repeated roots; the theorem needs finite k=v(tau), i.e. actual tau!=0, and does not specialize. (iv) valuation-only: (4) restricts roots but cannot separate S from T; a split S with T a product of five of its factors has the same valuations. Controls CONFIRMED as meaningful.

Scope. Covered exactly: r in 7Z, r>=7, every h in {r+2,...,2r} (7|r forces r>=7, and only k>=1 is used). Not covered: r not divisible by 7 (then v(a7)=v(a6)=2, nu is not 2 mod 7, and every residue step changes); other primes; full source, forcing, earlier rows, finite-r bounds, JC2. Consistent with the producer's stated limits.

## Verdicts, smallest defect

| item | verdict |
|---|---|
| A (3) exact a0,a6,a7 and bounds; V=0 excluded; unique minima on all three open intervals; (4) | CONFIRMED |
| B c5 exact, c4/c3>=1, c2/c1/c0>=0; t=-k unique leader; v(D),v(beta),v(gamma); (5) from full E_nu; v(K)>0; ubar=3 | CONFIRMED |
| C residue 5B3+1=5(alpha-3)(alpha^2+alpha+6); polynomial B3, no nonunit division; disc 5 nonsquare; alphabar rational; all 7-nondivisible h | CONFIRMED |
| D alpha=3-e, l positive integer; all eight Q_alpha terms; (8) valuation l; (9)=(3k-1)/6 nonintegral; table; Q_alpha!=0; Z=0 forces Q_alpha=0 | CONFIRMED |
| E cover, gcd(S,T)=1, Z^-1=bD in entire B_nu, H7_h unit via accepted prefactor; four controls; exact scope | CONFIRMED |

REFUTED: none. GAP: none within the stated family. Smallest defect: no mathematical error found. Precision items, none changing a verdict: (P1) section 2's "nearest ... 3k-1" understates the c4 competitor at gap k, still positive; (P2) "k0 is 24 modulo 7" means residue 3; (P3) v(a_i)=1 exactly for i=1..3, stronger than the stated bound; (P4) the u-name collision with 17zzb's exponent. Hostile attacks tried and failed: a lost root at V=0 or at an interval endpoint; a second balance in E_nu (both alternatives strictly excluded); a nonunit alpha-nu (never inverted); l=a (impossible by parity of 3k-1 mod 6); large l (then (9) is least); h with alpha-3 residue zero outside 7|h (none, since alpha-3 has residue -h); k=1 edge cases (w=0, a=1/3, all gaps positive).

## OPEN(S) RAISED

None. No new canonical OPEN ID. The theorem closes the requested 7|r family; the global H7-unit question for r not divisible by 7 remains the existing unresolved quantity, unchanged by this review.

## COLLISIONS

status: EMPTY

- NONE. Own-only check: this lane wrote exactly xmodel/f10-middle-rzero-gate-fable5-20260910.md and box/f10-middle-rzero-gate-fable5-20260910/input_custody.md, both absent at first action (ls 07:54:16 UTC); both authored by apply_patch only. No Seal, no charge_basis, no source modification, no coefficient artifact, no subprocess, no rerun of any accepted report, no other-lane or live file touched.

## Completion

Producer Seal cross-check not recomputed (no dependence on it); the producer's stated timeline (first 07:42:58, reserve 07:58:58, stop 08:00:58, own WHOLE 07:49) agrees with READ-SCOPE and ROOT-CARD (first+18 min earlier than 08:02). Overall verdict: A, B, C, D, E all CONFIRMED by independent hand algebra; the theorem "for every r>=7 with 7|r and every h in {r+2,...,2r}, Z is a unit of the entire B_nu, hence H7_h is a unit of B_nu[s,s^-1] and of every base change, equivalently gcd(S,T)=1 over Q" stands PROVISIONAL-CONFIRMED at the accepted 17zz/17zzb/17zzd interface with their inherited read-scope qualifications. No exit-price assertion is made, so no charge_basis line. Own WHOLE read (08:00:27 UTC), the one hash correction (row 5, regenerated from live sha256sum, then every 64-hex token in this file and in the box custody file cross-checked against the live list), raised-OPEN check (none) and collision check (EMPTY) all precede the marker and the 08:06:16 reserve. Authoring mechanism attested: apply_patch via stdin heredoc for the skeleton, every section, the hash correction and this completion; no Write/Edit tool, no redirection, no subprocess, no scientific execution of any kind. The marker below is the only standalone marker in this file and nothing follows it. All writers idle at the marker.

<!-- BODY-END -->
