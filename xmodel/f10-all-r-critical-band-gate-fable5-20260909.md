# Gate: ALL-r critical k_r band and zero-earlier-band obstruction (first hostile gate)

lane=f10-all-r-critical-band-gate-fable5-20260909
gate_model=claude-fable-5-1 (first different-model gate)
launch=2026-09-09 19:27 UTC; controlling_stop=min(19:48:00 UTC, launch+20min)=19:47 UTC, never reset
mode=pure manual reasoning; ZERO CAS/subprocess/arithmetic script; documentary metadata only

## 0. Custody

Verified all four ordered SHA256 before reading (sha256sum, documentary):

| # | file | sha256 (first 8) | status |
|---|------|------------------|--------|
| 1 | f10-all-r-critical-band-astra-20260909.md | b5de468d | match |
| 2 | f10-all-r-critical-band-astra-20260909.md.artifact.json | 84c13511 | match |
| 3 | f10-whole-mate-euler-elimination-astra-20260909.md | a5ab487c | match |
| 4 | f10-cubic-resonance-ode-discriminator-astra-20260909.md | 38cf3fb9 | match |

Accepted premises: 16r and 16l only. No 17-series, r=1, univariate theorem, code, data, ledger, peer or provenance used.

## 1. Scope read

Producer WHOLE (260 lines, sections 1-8, OPENS, COLLISIONS, Seal) read in full after hash match. Its artifact body_sha256 f7b24be7 / body_bytes 18544 / frozen_basis 0d39df3c agree with the Seal block (documentary read only, not recomputed). 16r read WHOLE for the interface actually consumed: normalized presentation (2)-(3), target coefficients (4), recurrence (5), B4 formula (6) with e_0=d_0/2, the j=3 S-coefficient 2u d_0-4u e_0, the shear/translation gauges (11), residuals (12), guard (13). 16l read WHOLE for equation (1), the reciprocal contact system (3), the converse in section 3, k!=0 in section 4, and the u!=0 argument in section 6. Nothing else was read; no 17-series, r=1 band, code, data, ledger, review or provenance. Zero CAS; every displayed coefficient below is hand-derived and small.

Reading convention used throughout: gap g = (7r+2) - (Jacobian weight); A gap d = m - wt, B gap e = n - wt; a weight-w Jacobian row collects exactly the pairs with d+e = g because m+n-r-1 = 7r+2. This is the producer's (7)-(8) restated and is what all independence claims below rest on.

## A. Critical gap 2r+1 and earlier forcing W

**Verdict: CONFIRMED for every integer r>=1.** Every displayed identity re-derived; no step needs an earlier residual row.

Chain rule (7). With U=S^a P(theta), theta=t S^-r: U_S = a S^(a-1) P - r S^(a-1) theta P', U_t = S^(a-r) P'. The cross terms r theta P'Q' cancel in U_S V_t - U_t V_S, leaving S^(a+b-r-1)(a P Q' - b P' Q). Confirmed as written.

Leading bands. Weight-m part of A: S t^3 (weight 1+3r=m), [S^(r+1)](S d)=d_r=F, [S^(2r+1)]h=v_(2r)=H (u d has degree <=r<2r+1), k_m=a. Weight-n part of B: S^2 t^5 gives D5=1, [S^n]B0=b. Theta^7 coefficient of mCD'-nC'D is 5m-3n=-1, matching -theta^7. Confirmed.

A band at weight r (4). S^i t^j has weight i+rj=r only for (i,j)=(r,0),(0,1); j=2 needs i=-r<0. So Y=h(0)theta+k_r=(1-u d_0)theta+k_r. Confirmed; no t^2 term, no other k coefficient.

B band at weight m (6), including r=1. i+rj=3r+1: j=5 needs i=1-2r<0; j=4 needs i=1-r, i.e. i=0 at r=1, and B4(0)=0 from 16r (6) B4=-2uS+S^2 e, so no B4 contribution at any r>=1; j=3 needs i=1 and [S]B3=beta=0 by the unchanged 16r shear gauge, giving V3=0 separately; j=2,1,0 give V2=[S^(r+1)]B2, V1=[S^(2r+1)]B1, V0=[S^m]B0, all inside 16r's envelopes deg B_j<=n-rj. Confirmed: deg V<=2 by support, the V3=0 gauge is a separate fact, and no theta^6 row exists.

Target at weight 5r+1. delta_5 t^5=(-u^2-2S)t^5 contributes -2S t^5 (weight 5r+1) and -u^2 t^5 (weight 5r); delta_6=2uS t^6 has weight 6r+1>5r+1 (gap r+1<=2r, an EARLIER gap for r>=1); delta_7 is gap 0; ell terms sit at weights 2r,3r,4r+1 (gaps 5r+2,4r+2,3r+1, all >2r+1). Only -2S t^5 = -2 S^(5r+1) theta^5. Confirmed, and ell is absent from every A band. Indirect ell: the gap-e B band is fixed by the gap-e row, whose only unknown-B term is the d=0 pair [A_m,B_(n-e)]; the eigenvalue of that pair on the t^j coefficient is jm-3n+3e, which vanishes only at e=2r+1 (j=3, the beta slot) and e=n (j=0, gamma). So for gaps 1..2r each B band is a unique polynomial function of A bands at gaps <=e and targets at gaps <=e. ell first enters a target at gap 3r+1>2r+1, and k_r (A gap 2r+1) cannot enter gaps <=2r. Confirmed: W is independent of k_r, of lower A bands and of ell, with no residual equation assumed.

Degree of W: nonleading A bands have theta-degree <=2 (t^2 at most), nonleading B bands <=4 (theta^5 would need [S^(2-e)]S^2=0). deg(P Q')<=5, deg(P' Q)<=5. Confirmed.

W5 and the theta^5 row (10). theta^5 in W needs deg P=2 and deg Q=4, i.e. f-coefficient S^p t^2 against B4-coefficient S^q t^4 with gaps (r+1-p)+(r+2-q)=2r+1, so p+q=2 with p<=r, q<=r+1: pairs (p,q)=(0,2): -u against e_0, and (1,1): d_0 against -2u; (2,0) vanishes since B4(0)=0. Band formula: (0,2) gives 2r(-u)(4e_0)-(4r+2)(-2u)e_0=4u e_0; (1,1) gives (2r+1)d_0(-8u)-(4r+1)(2d_0)(-2u)=-4u d_0. Sum 4u(e_0-d_0)=-2u d_0 by e_0=d_0/2. Same value as the S-coefficient of 4f'B4-2fB4' (S-primes): -8u d_0+4u d_0+4u e_0. On the left, [theta^5](rYD'-nY'D)=(5r-n)y=-2y and m(CV'-C'V) has degree <=4. Row: -2y=-2-W5, i.e. -2-(-2u d_0)+2(1-u d_0)=0. Identity for all u including u=0. Confirmed. Cross-check: this row is 16r's j=3 S-coefficient 2u d_0-4u e_0=0 read at gap 2r+1, consistent.

Residual slots (3). theta^i at Jacobian weight 5r+1 is S^(5r+1-ri)t^i: i=4,3,2 are the j=2,1,0 Euler rows at S^(r+1),S^(2r+1),S^(3r+1) with eigenvalues -(3r+1)=-m, -(6r+2)=-2m, -(9r+3)=-3m, exactly the pivots m,2m,3m of (12); i=1,0 are [S^(4r+1)]E1_res and [S^(5r+1)]E0_res. Confirmed (3), and confirmed that the sign of rpoly is Jacobian minus target, matching 16r (12).

## B. Literal N_i rows, T identity, Lambda, back-map k*

**Verdict: CONFIRMED.** Full expansion redone by hand.

Rows. rYD'-nY'D = y(r theta D'-nD)+r k_r D', so N=-2theta^5-W-y(r theta D'-nD) has N_i=-W_i+(n-ri)y D_i for i<=4 (unshifted D_i) and N5=-2-W5+2y=0. The separate k_r term is r k_r (i+1) D_(i+1) (shifted). Confirmed (11), both indexings.

CV'-C'V with C=theta^3+F theta^2+H theta+a, V=V2 theta^2+V1 theta+V0: theta^4: -V2; theta^3: -2V1; theta^2: HV2-FV1-3V0; theta^1: 2aV2-2FV0; theta^0: aV1-HV0. Hence

    V2=(5r k_r-N4)/m,  V1=(4r D4 k_r-N3)/(2m),  V0=(mH V2-mF V1+3r D3 k_r-N2)/(3m),
    r1=2ma V2-2mF V0+2r D2 k_r-N1,  r0=ma V1-mH V0+r D1 k_r-N0.

Confirmed (12)-(13), fixed rational pivots. k_r-column (14): v2=5r/m, v1=2rD4/m, v0=r(5H-2F D4+3D3)/(3m), chi1, chi0 as displayed. Confirmed.

T identity (16). T=mCV-nDk, T'=mC'V+mCV'-nD'k. CT'-2C'T=mC(CV'-C'V)-nk(CD'-2C'D). Substituting m(CV'-C'V)=R-rkD' gives CR-(r+n)k CD'+2nk C'D=CR-2k(mCD'-nC'D)=CR+2theta^7 k, using n+r=2m and (2). Confirmed. deg T<=5, T6=0, T5=m v2 k-nk=(5r-n)k=-2k. Confirmed (17).

Formal series. C(0)=a is a unit, so C^-2, C^-3 are in L[[theta]]; L is a Q-algebra so integration is defined. (T/C^2)'=2theta^7 k/C^3+R/C^2; the first term integrates to O(theta^8). T=K C^2+C^2 int R/C^2+O(theta^8). [theta^6]C^2=1 gives K=-P6(R); [theta^5]C^2=2F gives -2k=P5(R)-2F P6(R), so k=F P6(R)-P5(R)/2=Lambda(R). With R=chi*k this is the polynomial identity lambda1 chi1+lambda0 chi0=1 in L, not only at field points. Confirmed (18)-(19).

Back-map (20)-(21). Write (b1,b0)=alpha(chi1,chi0)+Psi'(-lambda0,lambda1). Dotting with (lambda1,lambda0) gives alpha=Lambda(b)=-k*; dotting with (-chi0,chi1) gives Psi'=chi1 b0-chi0 b1=Psi, since that functional kills chi and is 1 on (-lambda0,lambda1). Then rpoly=(alpha+k_r)chi+Psi(-lambda0,lambda1); at k_r=k* it equals (-lambda0,lambda1)Psi, and conversely both residuals vanish iff k_r=k* and Psi=0 because the matrix [[chi1,-lambda0],[chi0,lambda1]] has determinant 1. Confirmed as an exact ideal-level equivalence over every L-algebra; no entry of chi or lambda is required to be a unit.

Retention. k_r appears in A only at S^r, so a=k_m (m>r), b, D_i, F, H, and every B band at gap <=2r are k_r-free; the substitution touches only rows at gaps >=2r+1 and the report keeps them all. Confirmed.

Doubt B1 (presentational, no repair to the mathematics). The identity (19) lives in L, i.e. modulo the theta^1 and theta^0 rows of (2). In the source ring those two rows are the top coefficients [S^(6r+2)]E1_res and [S^(7r+2)]E0_res, which are retained rows of the ideal. The equivalence "(r1,r0)=0 iff k_r=k*, Psi=0" is therefore exact modulo those two retained rows plus the guard, not in the free polynomial ring. The producer's phrase "over every leading algebra" is correct; stating which two source rows make the source ring an L-algebra would remove the only ambiguity.

## C. H unit via reciprocal transport to 16l

**Verdict: CONFIRMED.** Transport, hypotheses and the nonvanishing consequence were each checked before the maximal-ideal step.

Transport. With theta=1/T, d/dtheta=-T^2 d/dT. From C=T^-3 Cdagger: C'(theta)=3T^-2 Cdagger-T^-1 Cdagger'; from D=T^-5 Ddagger: D'(theta)=5T^-4 Ddagger-T^-3 Ddagger' (primes on daggered objects are T-derivatives). Then mCD'-nC'D=T^-7[(5m-3n)Cdagger Ddagger+T(n Cdagger' Ddagger-m Cdagger Ddagger')]. Equating to -theta^7=-T^-7 and using 5m-3n=-1: n T Cdagger' Ddagger-m T Cdagger Ddagger'-Cdagger Ddagger=-1. Confirmed as displayed.

Match to 16l (1). 16l reads (5m'+1)T C'D-3m'T CD'-3CD=k with m'=3q+4. At q=r-1: m'=3r+1=m and 5m'+1=15r+6=3n. So 16l's left side is exactly 3(nTC'D-mTCD'-CD). Put Chat=Cdagger/a, Dhat=Ddagger/b (a,b units, both then monic of exact degrees 3,5 with constants 1/a,1/b); bilinearity gives 16l's equation with k=-3/(ab)!=0, and q=r-1>=0 because r>=1. [T^2]Chat=H/a, [T]Chat=F/a, [T^0]Chat=1/a. Confirmed: this is 16l's literal equation with its parameter range, and the T-derivative convention agrees with 16l's.

Consequence used. 16l section 3 (converse direction: char 0, c(0)=d(0)=1 from monicity, deg d<=5) turns any solution of (1) into a point (u,v,w) of its contact system f6=f7=0; here (u,v,w)=(H/a,F/a,1/a), nonzero because w=1/a. 16l section 6 proves u!=0 at every nonzero point; the direct two-line form: u=0 gives f7=(a)_3 v^2 w/2=0 so v=0 (w!=0), then f6=(a)_2 w^2/2=0 forces w=0, contradiction. Both (a)_2,(a)_3 are nonzero rationals since a=(5m+1)/(3m) is not in {0,1,2}. So H!=0 at every characteristic-zero field point of (2) with a,b!=0; algebraic closure is harmless and not even needed for this direction. Confirmed.

Unit in L. If H is a nonunit of L!=0, pick a maximal ideal containing H; the residue field has characteristic 0, keeps a,b nonzero and (2), and sends H to 0, contradicting the previous paragraph. Hence H is a unit of L, therefore of every L-algebra including nonreduced ones; vacuous if L=0. This is an existence proof of H^-1, sufficient for the functional Gamma in D; no explicit inverse or residue formula is claimed or needed. Confirmed. No extra guard, r=1 count or separability import was used.

Doubt C1 (presentational). The report's global convention "primes mean theta derivatives" is silently switched to T-derivatives in section 6; the transported equation is right only under the T convention. One sentence would close this.

## D. Changed control W0, Y = z theta + k, zero-earlier-A-band stratum

**Verdict: CONFIRMED at exactly the stated stratum scope.**

Control rows. W=0, Y=z theta+k, target -2z theta^5. theta^5 row: (5r-n)z=-2z equals the target; cancels. N_i=(n-ri)z D_i, N5=0, rows (12)-(13) unchanged with y=z; everything is linear homogeneous in (z,k), so the k=0 residual is z b^(1) and Psi=z c_z with c_z in L and no constant term. Confirmed.

T identity (22). T=mCV-nDY, deg T<=6 (DY has degree 6). CT'-2C'T=mC(CV'-C'V)-nY(CD'-2C'D)-nzCD. The control equation gives mC(CV'-C'V)=-2zC theta^5+CR-rYCD'+nzCD; the nzCD terms cancel and -(r+n)YCD'+2nYC'D=-2Y(mCD'-nC'D)=2theta^7 Y. Result 2theta^7 Y-2zC theta^5+CR. Confirmed, for any k.

theta^7 coefficient (23)-(24). (T/C^2)'=2theta^7 Y/C^3-2z theta^5/C^2+R/C^2; first term integrates to O(theta^8); K C^2 has degree 6; T7=0. C^-2=a^-2-2H a^-3 theta+O(theta^2); int theta^5/C^2=a^-2 theta^6/6-2H a^-3 theta^7/7+O(theta^8); C^2=a^2+2aH theta+...; [theta^7] of the product = -2H/(7a)+2H/(6a)=H/(21a). So 0=-2zH/(21a)+[theta^7]C^2 int R/C^2, giving Gamma(R)=z with Gamma=(21a/(2H))[theta^7]C^2 int(.)/C^2, which is defined because a and H are units (C above). Confirmed (24)-(25).

(26). Gamma(R)=z holds identically in L[z,k]. Substituting k=k*(z) (linear in z) gives R=(-lambda0 theta+lambda1)Psi=(-lambda0 theta+lambda1) c_z z, so gamma c_z z=z in the free polynomial ring L[z]; comparing z-coefficients, gamma c_z=1 in L. Confirmed: c_z is a unit of L and of every L-algebra. Side identity, consistent: at z=0 the same computation gives Gamma(chi)=0.

Attachment to the stratum. Nonleading A bands at gaps 1..2r are the coefficients of weight r+1..3r: -u (t^2, weight 2r, gap r+1<=2r for r>=1), d_0..d_(r-1) (S^(i+1)t^2), h_1..h_(2r), k_(r+1)..k_(3r). Their vanishing gives u=0 and d_0=0, hence y=1, hence Y=theta+k_r, i.e. z=1. Target terms at gaps 1..2r: only 2uS t^6 at gap r+1, now zero. W is a sum over pairs with an A factor P_d, 1<=d<=2r, so W=0 directly; the producer's additional statement that all earlier B bands also vanish is correct by the eigenvalue list in A (jm-3n+3e!=0 for 1<=e<=2r) but is not needed. The actual gap-(2r+1) rows r1,r0 are then literally the control at z=1, k=k_r; they force Psi=c_z, a unit, to be zero. Contradiction on the stratum. Confirmed for every r>=1, both fixed gauges (beta=0 entered via V3=0, gamma=0 is below) and the earlier target (only 2uS t^6) checked.

Scope check. The proof uses exactly W=0 and y=1; the theta^5 row forces y=1 whenever W5=0, so the true hypothesis is "W vanishes identically at gap 2r+1", of which the zero-earlier-A-band stratum is a sufficient case. The producer claims only the stratum, which is the correct conservative statement. Confirmed that nothing here excludes arbitrary all-r sources, makes any earlier coordinate a unit for r>1, or asserts a triangular architecture, runtime, field degree or JC2 consequence; the report says so explicitly and the algebra supports no more.

## E. Negative controls (manual)

All five requested controls are present in producer section 8 and scoped correctly; I re-ran each by hand.

- Deleted target. Without -2z theta^5 the theta^5 row becomes -2z=0 and (23) reads [theta^7]C^2 int R/C^2=0, i.e. Gamma(R)=0; the coefficient H/(21a) never enters and (26) is lost. Correctly scoped as a changed object.
- Zero z. z=k=0, W=0 gives N=0, V=0, R=0 for every guarded leading pair; z=1 alone then fails by (26). Correctly a band control, not a source point.
- Wrong index. Replacing (n-ri)yD_i by a shifted D_(i+1) changes N_0=-W_0+nyb; (19) concerns only the chi column and is blind to this. Correctly stated.
- Dropped residual. Setting k_r=k* alone leaves (-lambda0,lambda1)Psi, and D shows Psi is a unit on the stratum. Correctly stated.
- Omitted top guard. a=0 kills the formal expansion of C^-2 at theta=0; omitting the leading ODE kills (16) and the transport in C. Correctly scoped as no statement.
- Chosen entry. (19) is a combination identity, not a claim that chi1 or chi0 is a unit. Correct.

## F. Verdict table

| item | verdict | basis |
|---|---|---|
| A gap 2r+1 band, supports incl. r=1, V3 gauge, target -2S t^5 only, W independence, W5=-2u d_0, slots (3) | CONFIRMED | sections A above, every identity re-derived |
| B rows (11)-(14), T identity, T5=-2k, Lambda(chi)=1 in L, determinant-one back-map, retention | CONFIRMED | section B; doubt B1 presentational |
| C H unit via transport to 16l at q=r-1, k=-3/(ab) | CONFIRMED | section C; doubt C1 presentational |
| D control (22)-(26), gamma c_z=1, stratum exclusion only | CONFIRMED | section D |
| Producer non-claims (no all-r exclusion, no coordinate unit for r>1, no architecture/runtime/JC2) | CONFIRMED as stated | sections D, E |

Overall: the provisional manual theorem passes this first different-model gate at its literal scope. Two presentational repairs (B1, C1), no mathematical gap found, no OPEN raised.

## G. OPENS RAISED

None. Both doubts are one-sentence wording repairs with no bounded quantity to test; they do not change any verdict and are not promoted to OPEN.

## H. Collision / own-only scope

status: EMPTY

- NONE. Own-only check: this lane wrote exactly xmodel/f10-all-r-critical-band-gate-fable5-20260909.md and box/f10-all-r-critical-band-gate-fable5-20260909/custody.md, both via apply_patch. No corpus scan, no rerun of 16r/16l, no Seal, no charge_basis (no exit-price assertion is made), no network, no subprocess beyond sha256sum/ls/date/cat/grep for documentary metadata.

Completion: own WHOLE read, raised-OPEN check (none) and collision check (EMPTY) done at 2026-09-09 19:37 UTC, before the 19:47 UTC controlling stop. No Seal block follows by instruction.

<!-- BODY-END -->
