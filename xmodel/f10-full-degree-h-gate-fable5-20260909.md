# Fable5.1 gate: constant-h theorem, full-degree-h addendum, and the leading-ODE history interface

tag=f10-full-degree-h-gate-fable5-20260909
frozen_basis=0d39df3c9fd69c939a8420c54d03228b9077777d (provenance only)
reviewer=Claude Fable 5.1 (claude-fable-5-1); different-model review of two NEW PROVISIONAL Astra derivations
launch=root actual invitation; pin/first read 12:25:22 UTC; hard stop = earlier of actual+15min (12:40:22) and 12:42:00, i.e. 12:40:22 UTC
subprocesses=ZERO mathematical subprocesses. Only date, ls, mkdir, sha256sum, cat, grep, wc, od, tail, sed ran. Every identity below is hand-derived factored algebra.

## 0. Custody and read scope

All EIGHT charged objects under /tmp/jc2-lane.bvBraJ/inputs were pinned to box/f10-full-degree-h-gate-fable5-20260909/inputs.sha256 BEFORE their WHOLE reads, in the charged order: 59c2cda8 (constant-h report, body 11697 B, body sha e05a71c6), 11594bc9 (its artifact: same body bytes/sha, opened 12:11:22Z, closed 12:15:20Z, consistent with its seal), 5e5d56c8 (full-degree addendum, body 8900 B, body sha 8a0eb64f), c4cde21c (its artifact: same body bytes/sha, opened 12:16:59Z, closed 12:19:22Z, consistent), 77d59f7b (accepted 16r gate), 26687318 (accepted 16q module), 95221835 (accepted 16o discriminator), 295008d6 (accepted 16o gate). The four accepted objects are interfaces only; their interiors were not re-audited. No provenance path, live report, log, receipt, ledger, root builder-review file, peer body or corpus was opened.

Object identification. Both new reports use the 16r-gate normalized system: A=St^3+ft^2+ht+k, B=sum B_j t^j, B_5=S^2, [A,B]_(S,t)=Delta, f=Sd-u, h=1-ud+Sv (the 16q cubic test at A_3=S), deg d<=r, deg v<=2r, deg k=m=3r+1 with a=[S^m]k, deg B_0=n=5r+2 with b=[S^n]B_0, deg B_j<=n-rj, ab!=0 retained (16r gate A, E). Notation clash, not an error: the constant-h report's H is the constant value of h; root's part-D mapping uses H for [S^(2r+1)]h=[S^(2r)]v. Below I write Hc for the constant and H for the top coefficient.

## Rederived common formulas (used in A, B, D)

Bracket contribution of A_i t^i and B_l t^l is (l A_i' B_l - i A_i B_l') t^(i+l-1). At t^(j+2), k=3 gives jB_j-3SB_j', k=2 gives (j+1)f'B_(j+1)-2fB_(j+1)', k=1 gives (j+2)h'B_(j+2)-hB_(j+2)', k=0 gives (j+3)k'B_(j+3). Moving all but the diagonal term right reproduces both reports' formula (2)/(C) term by term. t^1: 2k'B_2+h'B_1-hB_1'-2fB_0'=u; t^0: k'B_1-hB_0'=1. Delta: tp=t^2-ut^3+St^4, tp^2=t^3-2ut^4+(u^2+2S)t^5-2uSt^6+S^2t^7, so (delta_0..delta_7)=(1,u,-ell,ell u-1,2u-ell S,-u^2-2S,2uS,-S^2). All CONFIRMED.

## A. Constant-h theorem (r=1 full rows; r>=2 low rows). CONFIRMED.

Hc=0: k'B_1=1 with deg k'=3 is impossible. Hc!=0: k'B_1=1+HcB_0', deg B_0'=6 with coefficient 7b!=0, so deg B_1=3 exactly and 4a*nu=7Hc*b, nu=[S^3]B_1!=0. Multiplying the t^1 row by Hc and substituting HcB_0'=k'B_1-1: 2k'(HcB_2-fB_1)=Hc^2B_1'-2f+uHc. Right side has degree<=2, left side is 0 or of degree>=3, so HcB_2=fB_1 and Hc^2B_1'=2f-uHc. B_1' has leading coefficient 3nu!=0, so deg f=2, d_1=[S]d!=0; explicitly 3Hc^2 nu=2d_1. d_1=0 and u=0 are thereby settled, not assumed (u=0 gives Hc=1, v=0).

Upper rows, every tied term checked. j=4 at S^3: -5e_1=-5(2d_1)+4d_1=-6d_1, e_1=6d_1/5 (delta_6=2uS lower). j=3 at S^4: -9C=-4(2d_1)e_1+2d_1(3e_1)=-2d_1e_1, C=4d_1^2/15!=0 (h'=0; hB_5'=2HcS and delta_5 of degree 1; B_6=0). j=0 at S^7: -21b=-3(4a)C (f'B_1, fB_1', hB_2' all of degree<=4; delta_2 constant), b=4aC/7, then nu=HcC. HcB_2=fB_1 at S^5: HcD=d_1nu, D=d_1C!=0. j=2 at S^5: -13D=-3(2d_1)C+2d_1(4C)-5(4a)=2d_1C-20a (hB_4' of degree<=2, delta_4 of degree<=1), so 15d_1C=20a and with C=4d_1^2/15: d_1^3=5a. j=1 at S^6: left side is zero because deg B_1=3 (forced by the full t^0 row, not a support cut); right side -2(2d_1)D+2d_1(5D)-4(4a)e_1=6d_1D-16ae_1 (hB_3' of degree<=3, delta_3 constant), so D=16a/5 and with D=d_1C=4d_1^3/15: d_1^3=12a. Hence 7a=0, contradiction. Both scalar chains replayed exactly.

Gauges. B->B+beta A+gamma adds degrees <=4,0,2,1,absent to B_0..B_4 (k, Hc, f, S, nothing), leaving b, nu, D, C, e_1 and HcB_2-fB_1 unchanged; A->A-k(0) changes nothing used. All u, ell covered; no root, extension or division by u.

Control (14) replayed: k'B_1-hB_0'=4S^3((2/3)S^3-1)-((8/3)S^6-4S^3-1)=1; 2k'B_2-hB_1'-2fB_0'=(16/3)S^8-8S^5-2S^2-(16/3)S^8+8S^5+2S^2=0=u; module expression B=B_0+B_1p+((2/3)S^4-S+p)y reproduces B_0..B_5 exactly. t^6 residual with B_4=0: 5f'B_5-2fB_5'-delta_6=10S^3-4S^3-0=6S^3!=0, i.e. e_1=0 against d_1=1. Changed object B_2+1 shifts the t^1 row by 2k'=8S^3. The control is a low-compatible non-point that fails the full t^6 row by 6S^3, exactly as stated; it is not a source point.

r>=2: deg B_1=2r+1, the same elimination gives 2k'(HcB_2-fB_1)=Hc^2B_1'-2f+uHc with right side of exact degree 2r (deg f<=r+1<2r) and left side divisible by k' of degree 3r: impossible. Uniform in u, ell. CONFIRMED.

## B. All-r addendum: deg h=2r+1 at every field point. CONFIRMED.

h=0 impossible as in A. tau=deg h<=2r: from the t^0 row deg(hB_0')=tau+5r+1 exactly (b!=0), so deg B_1=tau+2r+1<=4r+1 and [S^(4r+2)]B_1=0: (D) exact. Coefficient rows, each tie checked by me:
(E1) j=4 at S^(r+2): -(3r+2)E=[-5(r+1)+4]F; delta_6 of degree 1<r+2.
(E2) j=3 at S^(2r+2): -(6r+3)C=[-4(r+1)+2(r+2)]FE=-2rFE; -5h'S^2+2hS of degree<=tau+1<=2r+1; delta_5 of degree 1.
(E3) j=2 at S^(3r+2): -(9r+4)D=[-3(r+1)+4(r+1)]FC-5ma; h terms of degree<=tau+r+1<=3r+1; delta_4 of degree<=1.
(E4) j=1 at S^(4r+2): 0=[-2(r+1)+2(3r+2)]FD-4maE; h terms <=tau+2r+1<=4r+1; delta_3 constant.
(E5) j=0 at S^(5r+2): -3nb=-3maC; f'B_1, fB_1' <=r+4r+1; h terms <=tau+3r+1<=5r+1; delta_2 constant.
b!=0 forces C!=0 (and a!=0), then F,E!=0 by (E2),(E1). t^1 row at S^(6r+2): 2maD-2Fnb=0 since h'B_1, hB_1' have degree<=2tau+2r<=6r; with (E5): D=FC. (E3): (10r+5)FC=5ma. (E4): (4r+2)F^2C=2F(2r+1)FC=2maF=4maE, F=2E. (E1): 3r+2=2(5r+1), 7r=0. Contradiction; so deg h=2r+1, equivalently [S^(2r)]v!=0 because deg(ud)<=r<2r+1. Nothing is normalized to 1 and no stratum is dropped: u=0, all ell, h constant and h=0 are inside the hypothesis tau<=2r. At r=1 the two chains agree: F^3=5a from (F2) with C=(4/15)F^2, F^3=12a from D=16a/5.

Gauge: under B+beta A+gamma the slots E,C,D,b and the S^(4r+2) slot of B_1 receive degrees absent,1,r+1,m,<=tau, all strictly below. CONFIRMED.

Why tau=2r+1 defeats the chain: with H=[S^(2r+1)]h!=0 the h terms reach the SAME slots: j=3 at S^(2r+2) gains -5(2r+1)H+2H=-(10r+3)H (matching the 16r gate's control Q_3), j=2, j=1, j=0 and the t^1 row at S^(6r+2) all gain H-terms (2tau+2r=6r+2), and deg B_1=4r+2 makes the (E4) left side nonzero. Only (E1) is H-free. The comparisons then close to a consistent system, not a contradiction (the 16r gate's family u=ell=d=0, v=S^(2r), k=S^m realizes the upper rows with H=1). Maximal degree is therefore the exact boundary of this method. CONFIRMED.

## C. Controls, gauges, composition. CONFIRMED with one nuance.

Nonzero b is load-bearing: (D) and (E5) both use it. Nuance: (E5) b=maC/n shows that, given b!=0, a!=0 is a CONSEQUENCE rather than an extra input, so the guard's a-half is not independently needed for B; the reports' statement that both are essential is harmless (both are in the accepted guard). Zero u, repeated roots, all scalar gauges: retained, see A and B. No nilpotent-base theorem: both reports are field-point statements (exact degrees need a domain); the 16r gate's residue-field transport is what carries a finite Q-algebra point to a field point, and nothing here strengthens that. Exact consequence: for every characteristic-zero field point of L_r (equivalently, by 16r gate A, of the complete contract I_r), [S^(2r)]v!=0 in the normalized coordinates; degrees are invariant under the kappa_A, kappa_B scalings and the k(0) translation, so this is a statement about every complete point. It says nothing about properness or 1 in L_r, F10, degrees 112/196, or JC2; no point is exhibited. Builder: adding w*v_(2r)-1 would be field-point-neutral by the theorem but is a change of the ideal and is NOT licensed by either report or by this gate. CONFIRMED.

## D. Historical deduplication: the top-weight mapping. CONFIRMED (exact), verdict RECOVERED.

Weights w(S)=1, w(t)=r. Top weight of A is 3r+1: St^3, FS^(r+1)t^2, HS^(2r+1)t, aS^(3r+1), where F=[S^r]d, H=[S^(2r)]v (since deg(ud)<=r). So A_top=St^3(1+FT+HT^2+aT^3)=St^3C(T), T=S^r/t. Every B_j slot S^(n-rj)t^j has weight 5r+2, and n-rj-2=r(5-j), so B_top=S^2t^5 D(T) with D=sum_j beta_j T^(5-j), beta_j=[S^(n-rj)]B_j: D(0)=beta_5=1, [T]D=E, [T^2]D=C, [T^3]D=D_scalar, [T^4]D=[S^(4r+2)]B_1, [T^5]D=b. Delta's top weight is 7r+2, carried only by -S^2t^7 (t*p^2 top; -ell tp tops at 4r+1). With T_S=rT/S, T_t=-T/t: A_S=t^3(C+rTC'), A_t=St^2(3C-TC'), B_S=St^5(2D+rTD'), B_t=S^2t^4(5D-TD'), and [A_top,B_top]=S^2t^7[(C+rTC')(5D-TD')-(3C-TC')(2D+rTD')]=S^2t^7[(5r+2)TC'D-(3r+1)TCD'-CD], the T^2C'D' terms cancelling. Hence nTC'D-mTCD'-CD=-1, exactly as root wrote; T^0 gives -C(0)D(0)=-1 consistently and [T^8]=ab(3n-5m-1)=0 so no t^(-1) term arises. Dividing C by a and D by b (both nonzero by the guard) gives monic degree-3/5 polynomials with nTC'D-mTCD'-CD=-1/(ab): the accepted 16o ODE (1) with c=1/(ab)!=0, matching the 16r gate's c_orig=1/(ab). Orientation check: 16r gate D gives [A,B]_(p,z)=-z[A,B]_(S,t), and -S^2t^7 with S~pz^3, t=z^-1 is -p^2/z, so [A,B]_(p,z) tops at +p^2, the 16o sign at c=1. lambda=[T^2](C/a)=H/a.

16o section 6 (re-verified in the 16o gate E and by me: with lambda=0, [x^7]f^(a0)=(a0)_3 mu^2 nu/2 forces mu=0, then [x^6]=(a0)_2 nu^2/2!=0 since a0=n/m is in (5/3,7/4] and nu=C(0)!=0) proves lambda!=0 for every monic solution with c!=0. So H!=0, i.e. deg h=2r+1, follows from the top-weight identity plus the guard plus the accepted lemma.

Exactness audit. The addendum's (E1)-(E5), its t^1 comparison and (D) are precisely the T^1..T^7 coefficients of the ODE with H=0: I replayed [T^1]: (n-1)F-(m+1)E=0 is (E1); [T^5] with beta_1=0: (9r+3)aC=3nb is (E5); [T^7]: ma*beta_1=nHb is (D)'s slot. The addendum's "lower" terms are exactly the sub-top-weight terms, its cancellations are the T^2C'D' cancellation, and its constant normalization C(0)=D(0)=1 differs from 16o's leading-coefficient normalization by the scaling that produces c=1/(ab). No weight, tie, cancellation or sign mismatch. Source scope differs: 16o took the ODE as a hypothesis from the 16l/16k source initials; here the ODE is a derived consequence of the complete L_r bracket at top weight, with c fixed by the guard. Therefore the addendum's theorem is the accepted lambda!=0 nonvanishing RECOVERED by a second, T-coefficient proof, with a direct COMPLETE-L_r attachment (the two-line top-weight identification above). It is not a new independent geometric obstruction and gives no faster full exclusion. The constant-h theorem (A) is the r=1, tau=0 stratum of the same fact. The direct proofs in A and B are independently valid and are not contaminated by this identification.

## Verdicts

| Item | Verdict | First exact failure |
|---|---|---|
| A constant-h, r=1 full rows and r>=2 low rows, control 6S^3 | CONFIRMED | none |
| B deg h=2r+1 at every complete field point, v_(2r)!=0, tau=2r+1 boundary | CONFIRMED | none |
| C guard essential (b-half load-bearing, a-half implied), gauges, field-point scope, no builder change | CONFIRMED | none |
| D top-weight mapping to 16o ODE, c=1/(ab), lambda=H/a | CONFIRMED exact; addendum = RECOVERED leading-ODE nonvanishing with complete-L_r attachment | none |
| GAP | none found in the charged claims; open remain properness/unit of L_r, F10, JC2 | n/a |

## Perimeter and own checks

Read: the eight charged inputs only, WHOLE, after pins matched. Written: this file and box/f10-full-degree-h-gate-fable5-20260909/ (inputs.sha256, pin-time.txt, README) only. No CAS, Python, toy, coefficient or matrix script, solver or old checker ran; all algebra is manual and factored. No OPEN token is raised, consumed or closed; no seal line and no exit-charge declaration line are authored; no follow-on authority. Own whole-body read and own-only raised-OPEN/collision check precede the marker.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN check, no corpus scan.
<!-- BODY-END -->
