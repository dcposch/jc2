# f10 middle cubic cover gate (fable5, 2026-09-10): FIRST hostile mathematical gate

lane=f10-middle-cubic-cover-gate-fable5-20260910
gate_model=claude-fable-5-1 (first different-model review of the new composition)
launch=2026-09-10 05:17:58 UTC (first own command); controlling_stop=min(05:33:00 UTC, first+14min)=05:31:58 UTC; reserve 05:29:58 UTC; never reset
owner_writes=xmodel/f10-middle-cubic-cover-gate-fable5-20260910.md, box/f10-middle-cubic-cover-gate-fable5-20260910/ (both absent before first write)
mode=pure manual algebra. Tools: date, ls, wc, sed, grep, sha256sum, cat, heredoc appends (skeleton without marker first, bounded sections, marker last). ZERO CAS, Python, subprocess, compile, test or coefficient evaluation of any size. No network, AWS, SSH, process, agent, Git, corpus, shared, protected, other-lane or live-file read. No uncharged artifact referenced by the charged texts was opened. Premises: the accepted 17o (critical producer + gate) and 17s (middle producer + gate) interfaces exactly as charged; 16l/16r are not re-hardened and no provenance is followed. No Seal, no charge_basis (no exit-price assertion is made).

## 0. Custody (seven ordered immutable snapshots, hashed BEFORE any body read)

| # | file | sha256 | status |
|---|------|--------|--------|
| 1 | f10-middle-cubic-cover-astra-20260910.md | 1551407bc0e890d385f80250f751bffcfb56a738cce52da08a38f5a223868358 | MATCH (equals the charged list) |
| 2 | READ-SCOPE.md | 76814b3664a2ae92c6c71bcf71a89f62bba003d449f8c55dd2ad35fc4e3e1159 | MATCH (equals the charged list) |
| 3 | ROOT-CARD.md | 8d793b0bb9c3784e22567b98135a88fb56de0c95ed223f80fa2b8f26f00e973c | MATCH (equals the charged list) |
| 4 | f10-all-r-critical-band-astra-20260909.md | b5de468d2283b732cde7cfde02eb4457a70713743682870ed1e7940129cef3a2 | MATCH (equals the charged list) |
| 5 | f10-all-r-critical-band-gate-fable5-20260909.md | 568436589b21637c0a44ebff79221b822618edbb50e4fc56d3a86bc93815a164 | MATCH (equals the charged list) |
| 6 | f10-all-r-middle-band-astra-20260909.md | 5282cf73f7be20ecdf0bef9613764a78fd4ec030b01dc78257a4b1c1d86dee8c | MATCH (equals the charged list) |
| 7 | f10-all-r-middle-band-gate-fable5-20260909.md | 3d3f0490d81b3c5b9969c9bae83020c33f85740167697c40fe88de1f7a7823e2 | MATCH (equals the charged list) |

All seven read WHOLE after the match. Producer Seal cross-check, documentary only: bytes through the marker line = 13969, sha256 = 8c11ddf977cf19766172d651abae97fe0e8f1ab27231c7f297a902ee47bb247d; the producer's Seal states 13969 / 8c11ddf977cf19766172d651abae97fe0e8f1ab27231c7f297a902ee47bb247d. Producer timeline (first action 05:05:59, reserve 05:15:59, cap 05:17:59) is consistent with READ-SCOPE, ROOT-CARD (first+12 min earlier than 05:20) and the charged writers-IDLE 05:13:21 / root COMPLETED 05:14:19. The card, READ-SCOPE and the four 2026-09-09 hashes agree with rows 3-7.

## A. Same L and H attachment: CONFIRMED

Both charged producers define L identically: C=theta^3+F theta^2+H theta+a, D=sum D_i theta^i with D5=1, D0=b, mCD'-nC'D=-theta^7, ab a unit (17o (2) is 17s (3) verbatim), the same theta=t/S^r, F=d_r, H=v_(2r), a=k_m, b=[S^n]B_0, and the same target sign (theta^7 coefficient 5m-3n=-1). ab a unit gives a and b units separately (b(ab)^-1 inverts a). 17o section 6 with its gate C proves H a unit of L: the transported monic cubic is Chat=(1/a)+(F/a)T+(H/a)T^2+T^3, 16l's u is its T^2 coefficient H/a, u!=0 at every characteristic-zero field point, hence H lies in no maximal ideal of L. The unit is therefore H, attached through H/a and not F/a, and the reciprocal normalization stays inside 17o's proof; the interface carries C and H unchanged. The middle F7(X)=[theta^7](1+z)^X, z=(H/a)theta+(F/a)theta^2+(1/a)theta^3, uses the same H/a as its theta-linear coefficient, and the report's (2) is 17s (27)-(28) verbatim. Map L -> source (not displayed by the report, but described correctly): F->d_r, H->v_(2r), a->k_m, D_j->[S^(n-rj)]B_j, b->[S^n]B_0; the theta^7 row is automatic, the theta^6..theta^2 rows hold by the Euler reconstruction of D_4..D_0 (pivots mj-3n, never zero), and the theta^1, theta^0 rows are exactly the retained top residuals [S^(6r+2)]E1_res, [S^(7r+2)]E0_res (17o gate doubt B1). The report retains them and asserts no L-identity in the free coefficient ring. The only ring changes in the whole report are the flat localizations L -> L[Delta_E^-1] and the two-sided tower isomorphisms of D; neither imposes a relation on the source. Unit in L passes to every L-algebra, nilpotents included, vacuously on the zero algebra. CONFIRMED.

## B. Leading X^7 coefficient, monic normalization, four evaluations, unit identity: CONFIRMED

(1+z)^X=sum_k binom(X,k) z^k; z^k has theta-order k, so theta^7 receives only k=3..7; binom(X,k) has X-degree k with leading coefficient 1/k!; so X^7 arises solely from k=7 with [theta^7]z^7=(H/a)^7, giving c=(H/a)^7/7!, a unit (H, a units, 7! a nonzero rational). The quartic X(X-1)(X-2)(X-nu) is monic, so [X^3]S_r=c and M_r=c^-1 S_r is a monic cubic in every L-algebra: degree exactly 3 in every nonzero base (1!=0 there), all identities holding in the zero ring. This removes 17s's "S_r may be zero on a component" caveat exactly, and only for that reason: 17s deliberately did not consume 17o. alpha_h=(8r+3-h)/m=2+(2r+1-h)/m lies in [2+1/m, 2+(r-1)/m] for h in {r+2..2r}; alpha_h-nu=(m-h)/m>=(r+1)/m; 1<nu<2 because nu-1=(2r+1)/m and 2-nu=r/m. Hence alpha_h, alpha_h-1, alpha_h-2, alpha_h-nu and alpha_h-alpha_k=(k-h)/m (h!=k) are nonzero rationals, units of any Q-algebra; w_h and eta_(h,J) are units. Lagrange over an arbitrary commutative ring: P=M_r-sum_h M_r(alpha_h) prod_(k!=h)(X-alpha_k)/eta_(h,J) has degree <=3 and vanishes at the four points; monic division P=(X-alpha_1)Q_1 is exact; P(alpha_2)=(alpha_2-alpha_1)Q_1(alpha_2) with a unit factor forces Q_1(alpha_2)=0; after three steps a constant q times a unit at alpha_4 vanishes, so q=0 and P=0. No domain, reducedness or field is used. Comparing X^3 gives 1=sum M_r(alpha_h)/eta_(h,J); with f_h=c w_h M_r(alpha_h) this is 1=sum lambda_(h,J) f_h, lambda_(h,J)=1/(c w_h eta_(h,J))=7!(a/H)^7/(w_h eta_(h,J)), explicit units of L. (5)-(7) CONFIRMED for every four-subset J (needs d>=4, i.e. r>=5; vacuous below, as the report says).

## C. Local three-exception bound, principal-open cover, small r, control: CONFIRMED

Local bound: in a nonzero local L-algebra with maximal ideal p, four nonunit f_h would put 1 in p by (7); so at most three f_h are nonunits, equivalently at most three vanish in any residue field (also: a monic cubic over a field has at most three roots and the alpha_h stay distinct in characteristic 0). Cover: for a prime p of any L-algebra A, Z={h: f_h in p} has |Z|<=min(3,d)=e; choose E containing Z with |E|=e (possible since e<=d); every factor of Delta_E is outside p, so Delta_E is outside p. Thus the D(Delta_E) cover Spec A, and the ideal generated by the Delta_E is (1): a proper ideal would lie in a maximal, hence prime, ideal missing some Delta_E. Exact, no radical, stable under every base change because (7) base-changes; the zero algebra has no primes and (1)=(0) there. Small r: r=1 (I empty, E=empty, Delta=1) and r=2,3,4 (E=I, Delta=1) give one chart with no localization and nothing eliminated, which the report states. d>=3 gives binom(d,3) charts, one at d=3; no minimality claimed. Inverse (9) f_h^-1=prod_(k in I\E, k!=h) f_k/Delta_E is correct. Control: over Q[z] with M=X^3-z, each M(alpha_h)=alpha_h^3-z is nonconstant, hence a global nonunit, for all d of them; any two differ by the nonzero rational alpha_h^3-alpha_k^3 (cubes of distinct positive rationals are distinct), a unit, so at most one vanishes at any prime while (7) still holds. It refutes "local <=3 implies global <=3" and is correctly labelled abstract: not a leading-ODE solution, no stratum fabricated. CONFIRMED.

## D. Exact increasing-h tower substitution, source maps, denominators, local-to-global: CONFIRMED

Step: 17s (22) gives A_prev[l_h,k_(m-h)]/(two rows (14)) isomorphic to A_prev[Y_h]/(H7_h Y_h+J_h) over A_prev, accepted (17s gate B). L -> L_E is flat and commutes with polynomial extension and quotient, so the tower base-changes termwise. For h outside E, f_h is a unit of L_E and B[Y]/(fY+J') -> B, Y -> -f^-1 J', is an isomorphism whose inverse is the structure map (the row identifies the class of Y with -f^-1 J'); for h in E nothing is inverted and row (13) is kept. Induction over increasing h gives a two-sided isomorphism of the localized middle tower onto (A_0 tensor L_E)[Y_E]/(rows (13)); extending each step Z-linearly to all later variables gives Q_E isomorphic to (A_0 tensor L_E)[Y_E,Z]/(rows (13), sigma(K)). Nothing is discarded: each eliminated row uniquely solves its own variable and every constraint it induces elsewhere survives inside sigma(K) and the later J's. Maps: (14) is 17s (15)+(21) with rho=Y_h, R=-c_h1 theta-c_h0, and N_V/theta^7=V_lin(U) (the five pivots force it, 17s section 4); (15) is 17s (23) including v_(2r-h)=U1+u d_(2r+1-h), the -ud shift of 17s (5)-(6); (16) is 17s (24) with the V_part(0) subtraction, 17s (25) showing the WHOLE constant is Y_h+ma V_part(0). All three match. T7 sufficiency: 17s (20) U2=(delta4/kappa)T7 with T7=H7_h Y_h+J_h, and V4=0 follows from [theta^7](mCV-nDU)=mV4-nU2; so the single row T7=0 equals the two actual rows in the invertible affine coordinates. That is accepted 17s (22) and is consumed here as a premise, not re-proved; nothing in the new report changes it. Forcing: J_h reaches W_h through W_h -> V_part -> c_h -> R -> J_h (17s (12),(13),(21)); the report displays (11) and states this chain at (14), with the earlier V_part terms and the modified-u ancestry inside W_h. Denominators: Y_h^*=-(prod_(k outside E, k!=h) f_k) sigma_prev(J_h)/Delta_E with numerator in L, so exponent 1 plus the monomial maximum, exactly (17); representative-dependent, honestly labelled a bound; the only other denominators are a^-1 and fixed rationals from (14), which add no Delta_E power. Clearing denominators is exact only with Delta_E invertible or with z_E Delta_E-1, correctly flagged. Local-to-global (18): Q is an L-algebra once the two top rows and guard are imposed, so the Delta_E generate (1) in Q; if Q!=0, a maximal ideal misses some Delta_E and Q[Delta_E^-1] surjects onto the nonzero (Q/m)[Delta_E^-1]; equivalently Q_E=0 for all E means Delta_E^(N_E)=0 for all E, and those powers generate (1), so 1=0. Conditional only; no vanishing asserted, no uniform-r or JC2 consequence drawn. CONFIRMED.

## Verdicts, smallest defect, strength versus utility

| item | verdict |
|---|---|
| A same L, same H, H/a attachment, top rows retained, no silent quotient | CONFIRMED |
| B c=(H/a)^7/7! unit, M_r monic cubic in every base, four alpha_h, explicit lambda, sum lambda f=1 over nonreduced rings | CONFIRMED |
| C at most three nonunits LOCALLY, cover of Spec of every L-algebra, (Delta_E)=(1), small r, Q[z] control | CONFIRMED |
| D localized tower isomorphism with <=3 retained Y and all rows, maps (14)-(16) equal 17s, T7 row, denominators, conditional (18) | CONFIRMED |

Surviving scope: exactly sections 1-5 of the report at its hypotheses (commutative Q-algebra over L with (1) exact, ab a unit, H a unit by accepted 17o, 17s (22) accepted). GAP: none. REFUTED: none.

Smallest real defect: no mathematical error found. Three precision items, none changing a verdict: (P1) section 2 headlines "no prime of L contains four distinct f_h" while section 3 and D use primes of arbitrary L-algebras; the base-change sentence in section 2 covers this and the headline should say so. (P2) the map L -> source and the two rows that make the source an L-algebra are described, not displayed; one line (as in A above) closes it. (P3) recipe (17) returns b_h=1 when sigma_prev(J_h)=0, where Y_h^*=0 needs no denominator; harmless as a bound.

Ring-theorem strength: exact over every L-algebra, nilpotents and the zero ring included; monic normalization, explicit unit identities, finite cover with ideal exactly (1), exact two-sided localized tower, conditional local-to-global. Utility, which is smaller: r<=4 yields nothing (Delta_E=1). For r>=5 there are binom(r-1,3) charts, growing cubically; on each chart r-4 middle coordinates are eliminated and three stay with their rows, while the r+1 early parameters, the critical k_r band, all later data, the full W forcing and sigma(K) with Delta_E denominators remain and are r-dependent. Which f_h are global units, the H7_h=0 stratum over A_prev, and 17s's OPEN[F10-ALLR-MIDDLE-H7-UNIT] (r=2,h=4 quotient) are untouched. No finite r bound, source existence, degree or JC2 consequence follows, and none is claimed. The Q[z] control shows the global-count overread is genuinely false, so the old global H7-unit question is not settled by this composition.

## OPEN(S) RAISED

None. The three precision items have no bounded quantity to test and are not promoted; no new OPEN ID is raised.

## COLLISIONS

status: EMPTY

- NONE. Own-only check: this lane wrote exactly xmodel/f10-middle-cubic-cover-gate-fable5-20260910.md and box/f10-middle-cubic-cover-gate-fable5-20260910/input_custody.md; no corpus scan, no rerun of 16l/16r/17o/17s, no Seal, no charge_basis.

## Completion

Own WHOLE read, raised-OPEN check (none) and collision check (EMPTY) done before the marker and before the 05:29:58 reserve; the marker below is the only standalone marker in this file and nothing follows it. All writers idle at the marker.

<!-- BODY-END -->
