# Bounded residual-degree audit: F10 low-residual uniform obstruction (Fable 5.1)

tag=f10-low-residual-degree-gate-fable5-20260909
frozen_basis=0d39df3c9fd69c939a8420c54d03228b9077777d (provenance only)
reviewer=Claude Fable 5.1 (claude-fable-5-1); different-model gate of one Astra hand lemma
launch=root actual invitation; actual lane start 12:08:47 UTC (recorded, not reset); hard stop = earlier of 12:20:47 and 12:22:00 UTC, i.e. 12:20:47 UTC
subprocesses=ZERO mathematical subprocesses. Only date, ls, mkdir, sha256sum, sort, cat, grep, head, wc, cut ran. Every identity below is hand-derived factored algebra.

## 0. Custody and read scope

All FOUR charged objects under /tmp/jc2-lane.8nj6It/inputs were hashed (box/f10-low-residual-degree-gate-fable5-20260909/input-pins.sha256) at 12:08:47 UTC BEFORE their WHOLE reads, in the invitation's order: 7f4d0ff6 (new low-residual lemma, PROVISIONAL, Astra), 07e92682 (its artifact: body_bytes 12339, body_sha256 46ec8e48, opened 11:51:30Z, closed 12:05:47Z), 77d59f7b (Euler complete-presentation gate, now ACCEPTED16r per root, not provisional as the frozen producer states), 26687318 (boundary cubic module, ACCEPTED16q). All four hashes equal the invitation's list. The producer's body hash was recomputed from the file's unique standalone BODY-END line: 12339 bytes, 46ec8e48..., equal to its seal and artifact. Accepted interiors (16r, 16q) were not re-hardened; only the new lemma, its controls and its exact attachment to the accepted 16r presentation were audited. No other report, provenance path, live review, log, receipt or corpus was opened.

Object identification. The lemma's A, B, f=Sd-u, h=1-ud+Sv, k, B5=S^2, a=[S^m]k, b=[S^n]B0, guard omega a b-1, bounds deg d<=r, deg v<=2r, deg Bj<=n-rj are exactly the 16r gate's normalized objects (its section A, E). The lemma's E0, E1 are the 16r gate's t^0 and t^1 rows E0_res, E1_res (its section E). The module's cubic test (8) and quintic test (11) are used by the lemma only in its control (9). tau denotes deg h throughout; t is the chart variable.

## A. E0 consequences: h!=0, gcd(k',h)=1, deg N and its leader. CONFIRMED.

Row re-derivation. With [A,B]=A_S B_t-A_t B_S, the pair A_k t^k, B_l t^l contributes (l A_k' B_l-k A_k B_l') t^(k+l-1). t^0 (k+l=1): (1,0) gives -hB0', (0,1) gives k'B1; delta_0=1. So E0=k'N-hP-1 with N=B1, P=B0': the printed row, signs included. t^1 (k+l=2): (2,0) gives -2fB0', (1,1) gives h'B1-hB1', (0,2) gives 2k'B2; delta_1=u. So E1=2k'B2+h'N-hN'-2fP-u: the printed row.

h!=0. If h=0 then E0=0 reads k'N=1. Over a characteristic-zero field a!=0 gives [S^(3r)]k'=m a!=0, so deg k'=3r>=3 and k'N has degree >=3 or is zero; neither equals 1. Uses only a!=0 and char 0.

Coprimality. k'N-hP=1 is a Bezout relation in K[S], so every common divisor of k' and h divides 1: gcd(k',h)=1 with multiplicities, over the field itself, no closure. The lemma's remark that (3) is forced, not a generic open set, is right.

Degree of N. b!=0 and char 0 give deg P=n-1=5r+1 with lc(P)=n b. deg(hP)=tau+5r+1>0, so the constant 1 is below the top and lc(1+hP)=H n b at degree tau+5r+1. Since k'N=1+hP is nonzero, N!=0 and deg N=tau+5r+1-3r=tau+2r+1, with m a nu=H n b, i.e. nu=n b H/(m a)!=0. Exactly (4). Consistency with the retained envelope: tau+2r+1<=n-r=4r+2 iff tau<=2r+1, which is the given bound deg h<=2r+1, so no envelope is violated and the degree of N is exact, not merely bounded. a and b are retained as moving nonzero scalars in both (4) and (7); nowhere are they set to 1. The formulas divide only by m, n, 2, a, b, all nonzero in every characteristic-zero field. CONFIRMED over every such field.

## B. The identity (5)/(6), degrees, leaders and the excluded (r,tau). CONFIRMED.

Full identity, no division. h E1-2f E0 = h(2k'B2+h'N-hN'-2fP-u)-2f(k'N-hP-1) = 2hk'B2+hh'N-h^2N'-2fhP-uh-2fk'N+2fhP+2f. The -2fhP and +2fhP cancel exactly; nothing else touches P. Collecting: 2k'(hB2-fN)-(h^2N'-hh'N-2f+uh). This is the printed (6) with every sign, and (5) is its value at E0=E1=0. Given E0=0 and h!=0, (5) is hE1=0, equivalent to E1=0 in the domain K[S]; the lemma correctly claims this only over fields, not over a nilpotent coefficient ring.

Leader of h^2N'-hh'N. h=H S^tau+..., N=nu S^(tau+2r+1)+.... The top of h^2N' is (tau+2r+1)H^2 nu S^(3tau+2r); the top of hh'N is tau H^2 nu S^(3tau+2r) (zero when tau=0, since then h'=0). Difference: (2r+1)H^2 nu S^(3tau+2r), nonzero in char 0 because H!=0, nu!=0 by (4). Exact degree 3tau+2r. Only leading coefficients enter, so repeated roots of h, k' and the value u=0 are irrelevant to this step.

Strict comparison. -2f+uh has degree <=max(r+1,tau). 3tau+2r>tau always. 3tau+2r>r+1 iff 3tau+r>1, true for r>=2 (all tau) and for r=1, tau>=1; it fails ONLY at r=1, tau=0 where both sides equal 2. So the failure set of the comparison is exactly {r=1, tau=0}, as printed.

Degree of D and its leader. Off that set the right side of (5) is nonzero of degree 3tau+2r and equals 2k'D, D=hB2-fN. Hence D!=0 and 3r+deg D=3tau+2r, so deg D=3tau-r>=0, i.e. 3tau>=r, i.e. tau>=ceil(r/3): this is (1), and it is vacuous at r=1 (tau>=1 gives 3tau>=1). Leader: 2(m a)lc(D)=(2r+1)H^2 nu, so lc(D)=(2r+1)H^2 nu/(2 m a)=(2r+1) n b H^3/(2 m^2 a^2): exactly (7). Envelope: deg(hB2)<=tau+3r+2 and deg(fN)<=(r+1)+(tau+2r+1)=tau+3r+2, so deg D<=tau+3r+2; 3tau-r<=tau+3r+2 iff tau<=2r+1, the given bound. So the excluded set is precisely {r>=2, 3tau<r}; nothing at r=1 is excluded; no upper restriction on tau is produced.

u=0. h=1+Sv, never zero. v=0 gives tau=0, excluded for r>=2 by the same comparison. v!=0 gives tau=1+deg v and (1) becomes deg v>=ceil(r/3)-1; no localization at u anywhere. Gauge. B->B+beta A+gamma sends N->N+beta h, B2->B2+beta f, P->P+beta k'. D->h(B2+beta f)-f(N+beta h)=D. E0->E0+beta(k'h-hk')=E0. E1->E1+beta(2k'f+h'h-hh'-2fk')=E1. deg N=tau+2r+1>tau, so nu is unchanged. Translation of k by a scalar changes no derivative. All CONFIRMED.

## C. r=1, tau=0 and the hand control (9). CONFIRMED.

Tied cancellation. At r=1, tau=0: m=4, n=7, deg k'=3, h=H a nonzero scalar, h'=0, deg N=3. The right side of (5) is H^2N'-2f+uH of degree <=2<3=deg k'. It equals 2k'D, a multiple of k', so it is zero, and then D=0 in the domain. This gives exactly (8): H B2=f N and H^2N'=2f-uH. lc(N')=3nu=3(7 b H)/(4a)=21 b H/(4a), so [S^2](2f)=21 b H^3/(4a) and [S^2]f=21 b H^3/(8a), nonzero: deg f=2 exactly, deg d=1=r. The printed coefficient is right, and no contradiction arises from these two rows alone.

Control (9), r=1, u=ell=0, d=S, v=0. f=S^2, h=1 (H=1), k=S^4, a=1, m=4; B0=(8/21)S^7-S^4-S, b=8/21; N=(2/3)S^3-1; B2=(2/3)S^5-S^2; B3=(2/3)S^4; B4=0; B5=S^2. Bounds: deg d=1<=1, deg v=0<=2, deg B1=3<=6, deg B2=5<=5, deg B3=4<=4, deg B4=0<=3; k(0)=B0(0)=[S]B3=0. Leader check: nu=7(8/21)/4=2/3=[S^3]N. E0: k'N=4S^3((2/3)S^3-1)=(8/3)S^6-4S^3; hB0'=(8/3)S^6-4S^3-1; E0=0. E1: 2k'B2=(16/3)S^8-8S^5; h'N=0; hN'=2S^2; 2fB0'=(16/3)S^8-8S^5-2S^2; E1=(16/3)S^8-8S^5-2S^2-(16/3)S^8+8S^5+2S^2=0. (8): HB2=B2=(2/3)S^5-S^2=S^2 N=fN; H^2N'=2S^2=2f. Both hold. [S^2]f=1 against the formula 21(8/21)/8=1: agrees.

Inverse boundaries via the accepted module. Cubic test (8) of the module on A: f3=S, f2=S^2, f1=1, f0=S^4: a_mod=1, d_mod=S^2/S=S, b_mod=(1-1)/S=0, all polynomial, so A=k+p+S y at u=0 (p=t+St^3, y=St^2): printed. Quintic test (11) on B: f5=S^2, f4=0, f3=(2/3)S^4, f2=(2/3)S^5-S^2, f1=(2/3)S^3-1: d_star=1, b_star=0, a=((2/3)S^4-S)/S=(2/3)S^3-1=N, d=((2/3)S^5-S^2)/S=(2/3)S^4-S, b=(N-N)/S=0, all polynomial, so B=B0+N p+((2/3)S^4-S+p) y: printed. Both boundary conditions hold without deleting any test.

Missing upper row. t^6 coefficient of [A,B] (k+l=7): (3,4) gives 4B4-3SB4'=0; (2,5) gives 5f'B5-2fB5'=5(2S)S^2-2S^2(2S)=6S^3; delta_6=2uS=0. So [A,B]-Delta has t^6 coefficient 6S^3!=0: the printed failed arrow, exact. Cross-check against the 16r reconstruction: its j=4 row (2+3 theta)e=(1+5 theta)d at d=S gives e=(6/5)S, B4=(6/5)S^3, and 4B4-3SB4'=(24/5-54/5)S^3=-6S^3 would cancel the 6S^3; so (9) is a deliberately changed object, not a reconstructed mate, and it is NOT an Euler, complete or source point. t^7 holds trivially (5S^2-6S^2=-S^2=delta_7).

Changed-object controls. B2->B2+1: E0 has no B2 term, unchanged zero; E1 gains 2k'=8S^3, printed. Sign flip -2f->+2f on the right of (5) at (9): H^2N'+2f=2S^2+2S^2=4S^2, printed. Both controls are genuine changed polynomials and behave as stated. CONFIRMED.

## D. Composition with ACCEPTED16r and the exact limit. CONFIRMED, with one reformulation.

Attachment. By 16r (accepted), every characteristic-zero field point of L_r supplies polynomials with exactly the lemma's hypotheses: f=Sd-u, h=1-ud+Sv with deg d<=r, deg v<=2r; k with k(0)=0 and a=k_m; B* reconstructed by fixed-rational diagonal inversions with deg Bj<=n-rj, B5=S^2, b=[S^n]B0* a polynomial in the variables; the guard omega a b-1 makes a,b nonzero at every field point; E0, E1 are the t^0, t^1 rows. So the lemma applies at EVERY field point of L_r, equivalently (16r section A) of I_r, over every characteristic-zero field: for r>=2, deg h>=ceil(r/3); at r=1, tau=0, the conditions (8) and [S^2]f=21 b H^3/(8a) are necessary. The lemma's own "conditional on the still-provisional Euler report" is now discharged by the 16r acceptance; nothing in the lemma depended on a property of 16r beyond the polynomial hypotheses listed above, so rerooting was not needed.

No new ideal row. Each S-coefficient of h E1-2f E0 is a Z-combination of products (coefficient of h or f)x(coefficient of E1 or E0), hence lies in L_r. So (5)/(6) adds no element outside L_r; the pruning is a statement about degree strata of the variety, exactly as the lemma says. Exact ideal form of the same result (a reformulation, not a new independent row): for r>=2 and 3 tau0<r, no characteristic-zero field point of L_r lies in the closed stratum {[S^j]h=0 for all j>tau0}; by the weak Nullstellensatz over Q (16r's endpoint mechanism) 1 lies in L_r+([S^j]h : j>tau0). This is a unit of a STRATUM ideal, never of L_r or I_r; the lemma is right to refuse promotion to the whole ideal.

Why tau=2r+1 exhausts the margin. The only upper information is deg D<=tau+3r+2 from the envelopes of hB2 and fN; combined with deg D=3tau-r it yields tau<=2r+1, already the given bound, with equality at tau=2r+1 (both sides 5r+3). So at the top stratum the leading term (7) is carried by the leading terms of hB2 and fN with no cancellation, and for ceil(r/3)<=tau<2r+1 the 4r+2-2tau top coefficients of hB2-fN must cancel, which is a system of consequences of E0, E1, not a contradiction. The lemma's degree/Bezout mechanism therefore ends exactly where stated. No full F10 exclusion, no unit of L_r or I_r, no JC2 claim, no point, and no runtime follow. No stronger conclusion is earned beyond the stratum reformulation above.

## Verdicts and strongest surviving scope

A CONFIRMED, B CONFIRMED, C CONFIRMED, D CONFIRMED. No sign error, missing case, hidden division, generic pivot or mislabelled control was found. Strongest exact conclusion: for every r>=2 and every characteristic-zero field K, every K-point of the accepted 16r ideal L_r (equivalently of I_r) has deg h>=ceil(r/3), with the gauge-invariant D=hB2-fN of exact degree 3tau-r and leader (2r+1) n b H^3/(2 m^2 a^2); equivalently 1 lies in L_r+([S^j]h : j>tau0) whenever 3 tau0<r. At r=1 nothing is excluded; the tau=0 stratum carries the necessary conditions (8). Whether L_r is proper or unit remains open in both directions for every r. No authored seal, no exit-price line, no continuation, builder, solver or launch authority.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN check, no corpus scan.

<!-- BODY-END -->
