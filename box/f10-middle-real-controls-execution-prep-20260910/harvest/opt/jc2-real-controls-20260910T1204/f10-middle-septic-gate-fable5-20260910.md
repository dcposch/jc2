# f10-middle-septic-gate-fable5-20260910 — FIRST Fable5.1 hostile gate: exact septic leading algebra

status: UNSEALED (adapter seals; no Seal section and no charge_basis authored here; the standalone BODY-END marker is the last line)
lane: f10-middle-septic-gate-fable5-20260910
first_action_utc: 2026-09-10T07:13:58Z
stop_utc: 2026-09-10T07:27:58Z (first+14 min, earlier than 07:29:00Z)
mode: manual math/text/hash only; zero subprocess/CAS/script arithmetic
owned: xmodel/f10-middle-septic-gate-fable5-20260910.md, box/f10-middle-septic-gate-fable5-20260910/

## 0. Charged inputs (sha256, hashed before any body was read)

Producer custody: ALL WRITERS IDLE 07:11:21, ROOT custody e4be5552 WHOLE FIRST 07:12:14, expected transaction 06a232a6 VERIFIED are taken as stated by the charge; this lane is manual only and did not re-derive them. Premises: accepted 17zz (exact E_X, Q_X, Z/P/ell) and 17zzb (ell a unit of A_nu, identity (3) D_u/K_u, E_nu = 360W^2+beta W+gamma). The inherited 17zz qualification that 17o/17s/17zw were excerpt-read premises is preserved unchanged; no base re-hardening.

| # | file | sha256 | status |
|---|------|--------|--------|
| 1 | f10-middle-univariate-unit-astra-20260910.md | 890e5c9c63a333bf873e963821c368d2dc080476eaf12c9fc6a10dce53db75e5 | MATCH |
| 2 | READ-SCOPE.md | de3e82310c88b52b37c595e54074a5f02944ba2f933c930560d588314ecc7032 | MATCH |
| 3 | ROOT-CARD.md | aa461e726b8ac7b8fae0f7b5ceebcbeb4250f42c70c3ad67f2d22996c63d1c24 | MATCH |
| 4 | f10-middle-resonance-unit-astra-20260910.md | 8cf54b2f78840ced62fd35722da6d0d969eedd3344aa07d4ab08ff62c50df012 | MATCH |
| 5 | f10-middle-resonance-unit-gate-fable5-20260910.md | dc43ef1cfba68da21d0e26f6422e6af626d15a75d551858e72e78c7236ac27ad | MATCH |
| 6 | f10-middle-full-boundary-astra-20260910.md | 82f11ed717d1691bb37c36242fdd9eb1eea23ec5eb46b42db5590b1997db18e6 | MATCH |
| 7 | f10-middle-full-boundary-gate-fable5-20260910.md | 8a80bcc8ad7dd9068b503e9b1e18b4a5e6532d70f559658e3aa7077ec1928491 | MATCH |

All seven equal the charged list; all seven read WHOLE after the match. No link followed, no other file opened.

## A. D,K division / remainder / rational units / Bezout / unit in unguarded leading algebra

Objects at u=nu=2-tau from accepted 17zzb (3): u-3=-(1+tau), u-4=-(2+tau), u-5=-(3+tau), 4-3u=3tau-2, 1-u=tau-1, 3u-4=2-3tau, 5-4u=4tau-3. Hence
D(V)=12V^2-12(1-tau)V+(1+tau)(2-3tau),
K(V)=-840V^3+840(1-tau^2)V^2+42(1+tau)(2+tau)(4tau-3)V+2(2-3tau)(1+tau)(2+tau)(3+tau).

Division by q=-70V+70tau(1-tau). qD: V^3 -840; V^2 840(1-tau)+840tau(1-tau)=840(1-tau^2); V^1 -70(1+tau)(2-3tau)-840tau(1-tau)^2; V^0 70tau(1-tau)(1+tau)(2-3tau). Remainder K-qD: V^1 coefficient 42(4tau^3+9tau^2-tau-6)+(140-70tau-210tau^2)+(840tau-1680tau^2+840tau^3)=1008tau^3-1512tau^2+728tau-112=56(18tau^3-27tau^2+13tau-2); and (2tau-1)(9tau^2-9tau+2)=18tau^3-27tau^2+13tau-2=f. V^0 coefficient 2(2-3tau)(1+tau)[(2+tau)(3+tau)-35tau(1-tau)]=2(2-3tau)(1+tau)(36tau^2-30tau+6)=12(2-3tau)(1+tau)(2tau-1)(3tau-1)=-12(1+tau)f. So K=qD+56f(V-v*), v*=12(1+tau)/56=3(1+tau)/14. CONFIRMED.

D(v*)=(1+tau)[27(1+tau)-126(1-tau)+49(2-3tau)]/49=(1+tau)(6tau-1)/49=e. CONFIRMED. In r: 3tau-1=-1/m, 2tau-1=-(r+1)/m, 3tau-2=-(3r+2)/m, so f=-(r+1)(3r+2)/m^3; e=(4r+1)(3r-1)/(49m^2). Both nonzero for every r>=2 (indeed r>=1); f=0 only at tau in {1/3,1/2,2/3}, e=0 only at tau in {-1,1/6}, none in [2/7,1/3). D,K,f,e,v* depend on r only, not on h. No exceptional actual parameter.

Bezout. D-D(v*)=12(V^2-v*^2)-12(1-tau)(V-v*)=(V-v*)J, J=12(V+v*)+12(tau-1). With A=(1+Jq/(56f))/e, B=-J/(56fe): AD+BK=D/e+JqD/(56fe)-JqD/(56fe)-J(V-v*)/e=[D-(V-v*)J]/e=e/e=1. Signs CONFIRMED; only 56, f, e are inverted, all nonzero rationals. In Q[V,W]/(E_nu,Q_nu) the single relation Q_nu-7E_nu=K+210DW=0 gives K=-210DW, so AD-210BDW=1, i.e. D(A-210BW)=1. This uses no localization, no residue field, no component choice, and holds with nilpotents and on the zero ring. D unit of the ENTIRE unguarded A_nu: CONFIRMED. (Note E_nu is not even needed for this step; only the combination Q-7E.)

## B. S formula, factor 245, degree 7 / LC, gcd(S,D)=1, Q[V,W]/(E,Q) = Q[V]/S

245*E_nu(V,-K/(210D))*D^2 = 245*360/44100 K^2 - (245/210) beta K D + 245 gamma D^2 = 2K^2 - (7/6)*120 tau(1+tau-6V) K D + 245 gamma D^2 = 2K^2-140tau(1+tau-6V)KD+245gamma D^2 = S. 245=210^2/180 is the exact denominator-clearing factor (360/210^2=2/245, 120/210=4/7). CONFIRMED.

Degree: 2K^2 has degree 6; the middle term has degree 1+3+2=6; 245 gamma D^2 has degree 3+4=7 with LC 245*(-120tau)*144=-4233600 tau, nonzero since tau>=2/7. So deg S=7 exactly, LC -245*120*144*tau. CONFIRMED.

gcd: S = 2K^2 mod D. From AD+BK=1, (BK)^2 = 1 mod D, so S*(B^2/2) = 1 mod D: S is a unit mod D, hence gcd(S,D)=1 as a pure consequence of (1); no root is substituted, no ordering or reality used. CONFIRMED.

Isomorphism (3). psi: Q[V,W]->Q[V]/(S), V->V, W->-K/(210D), well defined because D is a unit of Q[V]/(S) (gcd(S,D)=1). psi(E_nu)=S/(245D^2)=0; psi(Q_nu)=psi(K+210DW)+7psi(E_nu)=K-K+0=0. So psi descends to psi_bar: A_nu->Q[V]/(S). phi: Q[V]->A_nu, V->V, extends to Q[V][1/D]->A_nu since D is a unit of A_nu (section A); the identity S=245D^2 E_nu(V,-K/(210D)) in Q[V][1/D] maps to 245D^2 E_nu(V,W)=0 because W=-K/(210D) in A_nu. So phi descends to phi_bar: Q[V]/(S)->A_nu. psi_bar phi_bar(V)=V; phi_bar psi_bar(V)=V, phi_bar psi_bar(W)=-K/(210D)=W in A_nu. Mutually inverse ring maps: exact, nilpotent-preserving, no reducedness assumed. CONFIRMED. Consequence not stated by the producer but immediate: dim_Q A_nu = 7, so the unguarded leading algebra is NONZERO for every r>=2.

Guard automatic. In A_nu, E_nu=Q_nu=0 give t6(nu)=t7(nu)=0, so d=c^nu+O(z^8) and m c d'-n c' d=-W t5 z^7 exactly (accepted 17zz section 2). Let kappa be any residue field of A_nu at a maximal ideal (a number field). If W t5=0 in kappa then m c d'=n c' d in kappa[z]. deg c=p in {1,2,3} (z-coefficient 1), deg d=q>=1 (z-coefficient nu nonzero; q=0 would force c'=0). Leading terms: m q = n p. gcd(m,n)=1 from 5m-3n=-1, so m | p, impossible as m>=7>3. Hence W t5 lies in no maximal ideal and is a unit of A_nu; B_nu=A_nu=Q[V]/(S). CONFIRMED, by polynomial-degree argument only; the W=0 and t5=0 cases are both covered by the same identity. No reality of V,W used anywhere in A or B.

## C. Finite-etale / rank 7: coprime simple c,d, degree 8, O(z^8), k=0, tangent 0, Nakayama

At a geometric point (Qbar-point) of A_nu, W t5 is a nonzero scalar (section B), so m c d'-n c' d=-W t5 z^7 with nonzero right side. A repeated root z0 of c, a repeated root of d, or a common root kills the left side at z0, forcing z0^7=0, contradicting c(0)=d(0)=1. So c, d are squarefree and coprime; also W nonzero gives deg c=3 exactly. CONFIRMED.

Tangent vector (e_V,e_W) at the point: over kappa[eps]/(eps^2), c_dot=e_V z^2+e_W z^3 (the z-coefficient of c is the constant 1, so no z^1 term), and t6=t7=0 to first order means d=c^nu+O(z^8) over kappa[eps], hence d_dot=nu c^(nu-1) c_dot+O(z^8). H=n c_dot d-m c d_dot=n c_dot c^nu-m nu c^nu c_dot+O(z^8)=0+O(z^8) since m nu=n; deg H<=3+5=8; so H=lambda z^8. CONFIRMED. k=lambda/(W t5) is defined. k z times the leading identity: m c(k z d')-n(k z c')d=-k W t5 z^8=-lambda z^8. Subtracting: n(c_dot-k z c')d-m c(d_dot-k z d')=lambda z^8-lambda z^8=0. Signs and factors CONFIRMED.

gcd(c,d)=1 and n a nonzero integer give c | (c_dot-k z c'); its degree is <=3=deg c, so c_dot-k z c'=mu c with mu a scalar. Constant term: 0-0=mu*1, so mu=0. z^1 term: 0-k*1=0 (z c'=z+2Vz^2+3Wz^3), so k=0. Then c_dot=0, e_V=e_W=0. CONFIRMED. Scaling: the only candidate tangent is the scale direction z c', and it is excluded precisely because the z-coefficient of c is frozen at 1; so fixing that coefficient does remove the Laurent scale from this coordinate algebra, exactly as the accepted normalization L=B_nu[s,s^-1] predicts. CONFIRMED.

Nakayama: A_nu tensor Qbar is Artinian, a product of local Artinian rings; zero tangent space at every point means each maximal ideal M has M/M^2=0, M=M^2, and M nilpotent gives M=0. So A_nu tensor Qbar = Qbar^7, A_nu is finite etale of rank 7 over Q, S is squarefree with seven distinct roots. The argument runs over the whole A_nu (no principal open, no localization), so every scheme component is retained and every one of the seven points satisfies the original guard. CONFIRMED. Consistency check: Res_W(E_nu, K+210DW)=(210D)^2 E_nu(V,-K/(210D))=180 S, degree 7, and the D=0 locus contributes nothing since gcd(D,K)=1.

## D. T = D*P - ell*K represents D*Z, degree 5 / LC 10080, nonresonant points, negative control

DZ=DP+210 ell D W=DP+ell(210DW)=DP-ell K=T in A_nu, using K+210DW=0 only. CONFIRMED. Degrees: DP has degree 2+3=5 with LC 12*840=10080 (P from accepted 17zz (6), LC 840); ell K has degree 1+3=4. So deg T=5 exactly, LC 10080, for every actual (r,h). CONFIRMED. Since D is a unit and A_nu is Qbar^7 with the seven distinct V-values being the roots of S, Z vanishes at a geometric point iff T does; a nonzero quintic vanishes at most at five of the seven, so at least two normalized leading points are nonresonant for each actual pair. CONFIRMED. B_nu/(Z)=Q[V]/(S,T)=Q[V]/(gcd(S,T)); Z is a unit iff gcd(S,T)=1. The producer asserts neither, exhibits no resonant point, and makes no source or JC2 claim: correct scope.

Negative control: S split with seven distinct roots and T a scalar times five of its linear factors satisfies separability, deg T=5 and the "at least two" count, yet gcd(S,T) has degree 5. It is a valid abstract changed-object control showing that nothing in sections A-C can prove coprimality; it is not derived from E,Q and is not claimed to be. CONFIRMED as a control; its limitation (abstract, not an actual leading instance) is stated by the producer.

## E. New useful simplification vs remaining GAP; per-claim verdict table

| claim | verdict |
|---|---|
| A: K=qD+56f(V-v*), f, v*, e=D(v*), f,e nonzero for all r>=2, Bezout signs, D unit of entire unguarded A_nu, no illicit localization or exceptional parameter | CONFIRMED |
| B: S=245D^2 E_nu(V,-K/(210D)), factor 245 exact, deg 7 with LC -245*120*144*tau, gcd(S,D)=1 from (1), two-sided nilpotent-preserving A_nu=Q[V]/(S), guard W t5 automatic by degree/gcd(m,n)=1 | CONFIRMED |
| C: simple coprime c,d at geometric points, H=lambda z^8, k z subtraction, division/degree, mu=0 then k=0, tangent 0, scale removed by the frozen z-coefficient, Nakayama, all components retained, rank 7 | CONFIRMED |
| D: T=DZ exactly, deg 5 LC 10080, at least two nonresonant points per actual pair, no coprimality/Z-unit/resonant-point/source/JC2 claim, meaningful abstract control | CONFIRMED |

REFUTED: none. Hostile attacks tried and failed: division of K by D with a wrong remainder sign (recomputed both remainder coefficients independently); f or e vanishing at an actual tau (closed forms in r above); degree drop of S (LC proportional to tau, never 0); a hidden division by D before its unitness (none: the Bezout step precedes every use of 1/D); an escaped tangent through W=0 (W is a unit so deg c=3 and the division argument applies); a lost component (no localization anywhere).

New useful simplification (genuinely new relative to 17zz/17zzb): (i) the unguarded leading algebra is exactly the seven-dimensional Q[V]/(S), hence nonzero, with W eliminated globally and no principal open; (ii) the W t5 guard is a theorem, not a hypothesis, so B_nu=A_nu; (iii) A_nu is etale of rank 7, so there are exactly seven geometric normalized leading points, all guarded, with no nilpotent to track; (iv) the whole middle unit question is now "gcd(S,T)=1 in Q[V]" per actual pair, with S depending on r only and T on (r,h), and at least two of the seven points are always nonresonant.

Remaining GAP (unchanged in substance, now sharper): uniform coprimality of the explicit septic S(tau;V) and quintic T(tau,delta;V) over all actual tau=r/(3r+1), delta=(h-r-1)/(3r+1). Equivalently the single rational Res_V(S,T)(tau,delta) is nonzero at every actual lattice point. This is precisely the "two univariate polynomials/resultant" restatement that ROOT-CARD declines to count as progress on its own; what the producer adds beyond it is (i)-(iv), and in particular the reduction from a possibly nonreduced guarded algebra to seven honest points. No sample can close the GAP; no uniform proof is offered here. Not asserted by anyone: an actual resonant point, global H7-unitness, any forcing/source/finite-r/JC2 consequence.

## F. Own-only OPEN / collision check

OPEN(S) RAISED: none. No new canonical OPEN ID; the existing global H7-unit question of 17s/17zz remains the sole unresolved quantity, now equivalent to gcd(S,T)=1 uniformly.

COLLISIONS: status EMPTY. This lane wrote exactly xmodel/f10-middle-septic-gate-fable5-20260910.md and box/f10-middle-septic-gate-fable5-20260910/input_custody.md, both absent at first action (ls at 07:13:58 UTC). No Seal, no charge_basis (no exit-price assertion), no source modification, no coefficient artifact, no subprocess, no rerun of any accepted report. Every 64-hex token in this file equals a charged input hash from live sha256sum output.

Own WHOLE read (07:19:57 UTC) precedes the marker; the marker below is the only standalone marker in this file and nothing follows it. All writers idle at the marker.

<!-- BODY-END -->
