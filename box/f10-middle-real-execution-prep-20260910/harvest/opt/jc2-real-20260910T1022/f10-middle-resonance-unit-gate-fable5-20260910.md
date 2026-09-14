# f10 middle resonance unit gate (fable5, 2026-09-10): FIRST hostile mathematical gate

lane=f10-middle-resonance-unit-gate-fable5-20260910
gate_model=claude-fable-5-1 (first different-model review of the new normalization / affine-W row)
launch=2026-09-10 05:58:50 UTC (first own command); controlling_stop=min(06:12:00 UTC, first+14min=06:12:50)=06:12:00 UTC; reserve 06:10:00 UTC; never reset
owner_writes=xmodel/f10-middle-resonance-unit-gate-fable5-20260910.md, box/f10-middle-resonance-unit-gate-fable5-20260910/ (both absent before first write)
mode=pure manual algebra. Tools: date, ls, wc, sed, grep, sha256sum, cat, apply_patch (skeleton without marker first, bounded sections, marker last). ZERO CAS, Python, subprocess, compile, test or scripted coefficient evaluation of any size; every number below is hand arithmetic. No network, AWS, SSH, process, agent, Git, corpus, shared, protected, other-lane or live-file read. No uncharged artifact cited in the charged texts was opened. Premises: accepted 17o, 17s, 17zw exactly at their charged same-leading-ring scopes (H a unit of L, F7 factorization, local <=3 cover); their old existence attributions are not premises. No Seal, no charge_basis (no exit-price assertion is made).

## 0. Custody (nine ordered immutable snapshots, hashed BEFORE any body read)

| # | file | sha256 | status |
|---|------|--------|--------|
| 1 | f10-middle-resonance-unit-astra-20260910.md | 8cf54b2f78840ced62fd35722da6d0d969eedd3344aa07d4ab08ff62c50df012 | MATCH |
| 2 | READ-SCOPE.md | 2326197f9f6a2f0247e0fd3ca58ddf489d383c0231d015bdc6913e9936997a8f | MATCH |
| 3 | ROOT-CARD.md | e8c68510900f392c6b7c96e1f892b3674e6625b4ee67af8bd4e2fd2b71b9a0ff | MATCH |
| 4 | f10-all-r-critical-band-astra-20260909.md | b5de468d2283b732cde7cfde02eb4457a70713743682870ed1e7940129cef3a2 | MATCH |
| 5 | f10-all-r-critical-band-gate-fable5-20260909.md | 568436589b21637c0a44ebff79221b822618edbb50e4fc56d3a86bc93815a164 | MATCH |
| 6 | f10-all-r-middle-band-astra-20260909.md | 5282cf73f7be20ecdf0bef9613764a78fd4ec030b01dc78257a4b1c1d86dee8c | MATCH |
| 7 | f10-all-r-middle-band-gate-fable5-20260909.md | 3d3f0490d81b3c5b9969c9bae83020c33f85740167697c40fe88de1f7a7823e2 | MATCH |
| 8 | f10-middle-cubic-cover-astra-20260910.md | 1551407bc0e890d385f80250f751bffcfb56a738cce52da08a38f5a223868358 | MATCH |
| 9 | f10-middle-cubic-cover-gate-fable5-20260910.md | c64f87f3b5e84ddeafcb4e1f36192e6bd6bc5d7809ed26ea1ebba63fab245d05 | MATCH |

All nine equal the charged list and were read after the match: rows 1-3 and 8-9 WHOLE, rows 4-7 (accepted premises) by whole-line extraction of every t6/t7/H7/unit/OPEN statement plus their verdict tables. Producer Seal cross-check, own recomputation of bytes through the marker line: 11624 bytes, sha256 563a8cd062a120c74b5dab406fc48ec449b32873793a0dde5a1fcb21d5a6d178, equal to the producer's stated pair. Producer timeline (first action 05:45:12, reserve 05:55:00, cap 05:57:00) agrees with READ-SCOPE and ROOT-CARD (first+12 min earlier than 05:57) and with the charged writers-IDLE 05:54:46 / custody 05:55:59.

## A. Exact normalization L = B_nu[s,s^-1]: CONFIRMED

Ring. L: C=theta^3+F theta^2+H theta+a, D=sum D_i theta^i, D5=1, D0=b, mCD'-nC'D=-theta^7 (rows theta^0..theta^6 imposed, theta^7 automatic since 5m-3n=15r+5-15r-6=-1), ab a unit, and H^-1 an ELEMENT of L by accepted 17o (no adjoined guard). Forward coordinates s=H/a, V=Fa/H^2, W=a^2/H^3 are defined. Own check of C/a=c(s theta): s theta=(H/a)theta; V s^2=(Fa/H^2)(H^2/a^2)=F/a; W s^3=(a^2/H^3)(H^3/a^3)=1/a. Correct.

Integration. G=(C/a)^nu is a formal binomial series with G(0)=1; C(0)=a is a unit, so C, G are invertible in L[[theta]]. (D/G)'=(D'G-DG')/G^2=(D'-nu D C'/C)/G=(mCD'-nC'D)/(mCG)=-theta^7/(mCG), integrand O(theta^7), primitive O(theta^8) (L is a Q-algebra, integer divisions allowed), constant D(0)/G(0)=b. Hence D=bG+O(theta^8). deg D=5 and b a unit give [theta^6]G=[theta^7]G=0, i.e. s^6 t6(nu)=s^7 t7(nu)=0, so t6(nu)=t7(nu)=0 (s a unit); and D_i=b t_i(nu) s^i for i<=5, i.e. D/b=d(s theta). Monicity: b t5 s^5=1, so t5 is a unit; W is a unit since a,H are. So the map B_nu[s,s^-1] -> L (V,W,s as above) respects (t6,t7) and inverts W t5. Correct.

Inverse (3). a=1/(W s^3), H=1/(W s^2), F=V/(W s), b=1/(t5 s^5), C=a c(s theta), D=b d(s theta). Coefficients of C: theta^3: aW s^3=1 (monic); theta^2: aV s^2=V/(W s)=F; theta^1: a s=1/(W s^2)=H; theta^0: a. D: theta^5: b t5 s^5=1; theta^0: b t0=b. ab=1/(W t5 s^8), a unit. Target: in B_nu, d=c^nu+O(z^8), so c d'-nu c' d=c(nu c^(nu-1)c'+O(z^7))-nu c'(c^nu+O(z^8))=O(z^7); times m: m c d'-n c' d=O(z^7), a polynomial of degree <=3+4=7, hence equal to its z^7 term. Leading parts c=Wz^3+..., d=t5 z^5+... give [z^7](m c d'-n c' d)=(5m-3n)W t5=-W t5. Substituting z=s theta with d/dz=(1/s)d/dtheta: mCD'-nC'D=ab s[m c d'-n c' d](s theta)=-ab s W t5 s^7 theta^7=-ab W t5 s^8 theta^7, and ab W t5 s^8=(1/(W s^3))(1/(t5 s^5))W t5 s^8=1 exactly. So the image satisfies mCD'-nC'D=-theta^7 with factor exactly 1: no missing scalar or target relation. Correct.

Both compositions on generators (own display, the producer only asserts them). L->B->L: F -> V/(Ws) -> (Fa/H^2)/((a^2/H^3)(H/a))=(Fa/H^2)/(a/H^2)=F; H -> 1/(Ws^2) -> 1/((a^2/H^3)(H^2/a^2))=H; a -> 1/(Ws^3) -> 1/((a^2/H^3)(H^3/a^3))=a; t5 -> [theta^5](C/a)^nu/s^5=1/(b s^5), so b -> 1/(t5 s^5) -> b; D_i -> b t_i s^i -> b(D_i/(b s^i))s^i=D_i. B->L->B: s -> H/a -> (1/(Ws^2))/(1/(Ws^3))=s; V -> Fa/H^2 -> (V/(Ws))(1/(Ws^3))(Ws^2)^2=V; W -> a^2/H^3 -> (1/(W^2 s^6))(W^3 s^6)=W. Both identities hold in every commutative Q-algebra, nilpotents included; the zero ring satisfies everything vacuously. Generator/relation count is consistent: L has 8 generators (F,H,a,b,D1..D4) and 7 rows, B_nu[s^+-] has 3 generators and 2 rows, both of expected dimension 1 (the scale s). (2) CONFIRMED.

## B. H7_h=s^7 t7(alpha), unit retraction, actual exponents, no late-contact row: CONFIRMED

(C/a)^alpha=c(s theta)^alpha, so [theta^7]=s^7[z^7]c^alpha=s^7 t7(alpha): (4) correct. Unit test: s^7 is a unit of B_nu[s^+-]; if t7(alpha) has an inverse y(s) there, the B_nu-algebra retraction s->1 gives t7(alpha)y(1)=1 in B_nu; conversely a B_nu-inverse stays an inverse upstairs. This uses only the coefficient ring B_nu[s^+-]=L and never sets s=1 in a source; the producer says exactly this, and nowhere else in the text is s specialized. Correct. Exponents: m=3r+1, n=5r+2, h=r+2..2r, r>=2, alpha=(8r+3-h)/m. Own bounds: nu-5/3=1/(3m)>0, 2-nu=r/m>0; alpha-2=(2r+1-h)/m>=1/m>0, 7/3-alpha=(3h-3r-2)/(3m)>=4/(3m)>0; alpha-nu=(m-h)/m>=(r+1)/m>0. So alpha, alpha-1, alpha-2, alpha-nu, (nu)_2, (nu)_3, (alpha)_3 and the integers m, n, 2, 12, 72, 210, 720, 5040 are all units. Only t7(alpha) (one contact at alpha) is used; t6(alpha)=0 appears nowhere, and the producer's Outcome says so. CONFIRMED.

## C. E_X, Q_X term by term, the affine-W identity (7), the quotient (9): CONFIRMED

c=1+y, y=z+Vz^2+Wz^3, c^X=sum binom(X,K)y^K. A monomial z^i(Vz^2)^j(Wz^3)^k has K=i+j+k and contributes binom(X,K)K!/(i!j!k!)=(X)_K/(i!j!k!) times V^j W^k to [z^(i+2j+3k)]. Degree 7 partitions i+2j+3k=7: (7,0,0),(5,1,0),(3,2,0),(1,3,0); (4,0,1),(2,1,1),(0,2,1); (1,0,2): eight terms, (X)_7/7!, (X)_6 V/5!, (X)_5 V^2/12, (X)_4 V^3/6, (X)_5 W/24, (X)_4 VW/2, (X)_3 V^2 W/2, (X)_3 W^2/2. Multiplying by 5040/(X)_3 with (X)_K/(X)_3=(X-3)...(X-K+1): 1, 42, 420, 840, 210, 2520, 2520, 2520, exactly the eight coefficients of Q_X in (5). Degree 6 partitions: (6,0,0),(4,1,0),(2,2,0),(0,3,0); (3,0,1),(1,1,1); (0,0,2): seven terms (X)_6/720, (X)_5 V/24, (X)_4 V^2/4, (X)_3 V^3/6, (X)_4 W/6, (X)_3 VW, (X)_2 W^2/2; times 720/(X)_2: 1, 30, 180, 120, 120, 720, 360, exactly E_X in (5). Both displays CONFIRMED; at nu the divisors (nu)_2,(nu)_3 are units so (1) is E_nu=Q_nu=0.

Divided differences at (alpha,nu), sigma=alpha+nu, pi=alpha nu. (X-3)(X-4)(X-5)(X-6)=(X^2-9X+18)(X^2-9X+20)=X^4-18X^3+119X^2-342X+360; using (a^4-b^4)/(a-b)=sigma^3-2 sigma pi, (a^3-b^3)/(a-b)=sigma^2-pi, (a^2-b^2)/(a-b)=sigma, the difference quotient is sigma^3-2 sigma pi-18(sigma^2-pi)+119 sigma-342=B3. (X-3)(X-4)(X-5)=X^3-12X^2+47X-60 gives sigma^2-pi-12 sigma+47=B2. (X-3)(X-4)=X^2-7X+12 gives sigma-7=A. (X-3) gives 1. The V^2 W and W^2 terms are X-free and cancel. Hence Q_alpha-Q_nu=(alpha-nu)[840V^3+420A V^2+42 B2 V+B3+210 A W+2520 VW] and 2520=210*12, so the bracket is P+210(12V+A)W=Z: (6),(7) CONFIRMED coefficient by coefficient. In B_nu, Q_nu=0 gives Q_alpha=(alpha-nu)Z and t7(alpha)=(alpha)_3 Q_alpha/5040, so H7_h=s^7 (alpha)_3 (alpha-nu) Z/5040 with a unit prefactor: (8) CONFIRMED, and by B, H7_h is a unit of L iff Z is a unit of B_nu, i.e. iff B_nu/(Z)=0. Presentation (9) is B_nu/(Z) with E_nu, Q_nu replacing t6, t7 up to units: CONFIRMED as a whole-ring statement.

## D. Boundary P0, retained P0=0 branch, controls, scope: CONFIRMED

ell=12V+A=0 iff V=-A/12 (12 a unit). P(-A/12)=840(-A^3/1728)+420A(A^2/144)+42B2(-A/12)+B3: the cubic parts are -35A^3/72+210A^3/72=175A^3/72, the linear part -(7/2)A B2, so P0=B3-(7/2)A B2+(175/72)A^3: (10) CONFIRMED including the producer's two intermediate cubic terms. Division of P by the unit-leading linear ell is exact, P=P0+ell J with J quadratic; in B_nu/(Z), ell(J+210W)=-P0, so a nonzero rational P0 makes ell a unit there (any ring, nilpotents included) and licenses W=-P/(210 ell); if P0=0 then Z=ell(J+210W) and the field points of (9) split into ell=0 (V=-A/12 with both leading rows and the W t5 guard retained) and J+210W=0. The producer retains the P0=0 branch, claims neither that P0 is nonzero for all pairs nor that (9) is zero or nonzero, and correctly notes that a principal-open elimination alone is not a scheme cover when P0=0. CONFIRMED.

Own hand evaluation at the first bounded case r=2, h=4 (m=7, n=12, alpha=15/7, nu=12/7; not a producer claim, not a request for computation): sigma=27/7, pi=180/49, A=-22/7, B2=584/49, B3=-19080/343, giving P0=(-171720+404712-232925)/3087=67/3087. Cross-route: the W-free part of Q_X at V=11/42 is 3160/7203 at alpha and 3093/7203 at nu, difference 67/7203, divided by alpha-nu=3/7 gives 67/3087 again. So at (2,4) P0 is nonzero and ell is a unit of the resonance quotient, but the cancellation is near-total (terms of size about 130 leaving 67/3087), so nothing about other (r,h) follows and no uniform nonvanishing is asserted.

Controls. (1) t7(0)=t7(1)=t7(2)=0 by degrees 0,3,6 of (C/a)^0,(C/a)^1,(C/a)^2, t7(nu)=0 by A; formula (8) is consistent since (alpha)_3(alpha-nu) vanishes exactly at those four values and actual alpha avoids them. (2) With d only truncated, c^nu-d=t6 z^6+t7 z^7+O(z^8) and m c(c^nu)'-n c'c^nu=0 exactly, so m c d'-n c' d=-[m c(6t6 z^5+7t7 z^6+...)-n c'(t6 z^6+...)]: z^5 coefficient -6m t6, and after t6=0 the z^6 coefficient -7m t7. Both contacts are needed for the exact target; correct. (3) In a field with W t5 nonzero the target -W t5 z^7 vanishes at any repeated root of c or d and at any common root, forcing that root to be 0, contradicting c(0)=d(0)=1; correct, and no reality of roots is inferred. (4) ell is a polynomial that can vanish; its inverse is not taken. All four are meaningful changed-object or consistency controls; no leader is fabricated from Q[z]. Scope: the accepted local <=3 cover of the cubic-cover report is untouched; no global count, no elimination of a middle variable globally, no full-source, forcing, finite-r, existence or JC2 statement is made, and none follows from A-D. Real bounds on alpha,nu are used only for unit-ness of rationals, never as positivity of V,W. CONFIRMED.

## Verdicts, smallest defect, what remains GAP

| item | verdict |
|---|---|
| A two-sided normalization L = B_nu[s,s^-1], integration, all D_i, monicity, sign, ab W t5 s^8 = 1, nilpotents/zero ring/guard | CONFIRMED |
| B H7_h = s^7 t7(alpha), retraction unit test as a coefficient-ring test only, linked exponents, all rational factors units, no t6(alpha) row | CONFIRMED |
| C eight Q_X and seven E_X terms, B2/B3/A/840/420/42/210/12, identity (7), scalar (alpha)_3(alpha-nu)/5040, quotient (9) | CONFIRMED |
| D P0 formula (10), P0 nonzero => ell unit, P0 = 0 branch retained, four controls, cover/forcing/global/JC2 exclusions | CONFIRMED |

Surviving scope: sections 1-5 of the producer at its hypotheses (commutative Q-algebra over L, (3) exact, ab a unit, H a unit by accepted 17o). REFUTED: none. GAP (unchanged, not a win): uniform H7-unitness, now exactly "B_nu/(Z) = 0 for every linked (r,h)". Neither the producer nor this gate proves it or exhibits a guarded leading field point; the r=2,h=4 hand value P0 = 67/3087 only licenses the W elimination at that one pair.

Smallest real defect: no mathematical error found. Precision items, none changing a verdict: (P1) the two composition identities behind (2) are asserted, not displayed; section A above displays them. (P2) section 4 says a maximal residue field "may be any characteristic-zero extension"; B_nu is a finitely generated Q-algebra, so by Zariski's lemma its residue fields are number fields, which only sharpens the same statement (V,W algebraic, embeddable in C, still no positivity). (P3) the near-total cancellation in P0 at (2,4) is a reason to keep the P0 = 0 branch exactly as the producer does, not a defect.

## OPEN(S) RAISED

None. No new canonical OPEN ID; the existing global H7-unit question of 17s remains the sole unresolved quantity, sharpened to (9). No computation, resultant, norm, or positivity theorem is requested here.

## COLLISIONS

status: EMPTY

- NONE. Own-only check: this lane wrote exactly xmodel/f10-middle-resonance-unit-gate-fable5-20260910.md and box/f10-middle-resonance-unit-gate-fable5-20260910/input_custody.md; no corpus scan, no Seal, no charge_basis, no rerun of any accepted report.

## Completion

Own WHOLE read, raised-OPEN check (none) and collision check (EMPTY) done before the marker and before the 06:10:00 reserve; every 64-hex token in this file equals an input hash from live sha256sum output or the recomputed producer body hash. The marker below is the only standalone marker in this file and nothing follows it. All writers idle at the marker.

<!-- BODY-END -->
