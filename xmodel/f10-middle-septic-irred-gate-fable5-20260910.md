# FIRST Fable5.1 hostile gate: uniform septic irreducibility families

status=UNSEALED
lane=f10-middle-septic-irred-gate-fable5-20260910
owner=Fable 5.1 (claude-fable-5-1)
start_utc=2026-09-10T07:39:49Z
stop_utc=2026-09-10T07:53:49Z (actual first + 14 min; earlier than ROOT TERM 07:55:00)
mode=manual math/text/hash only; zero scientific subprocess

## 0. Custody (hashed BEFORE any body was read)

| snapshot | sha256 |
|---|---|
| f10-middle-septic-irreducibility-astra-20260910.md | 460129a51fce4ee17d5d71815be014cbb4075dee71a39bb269721761ba29e97d |
| READ-SCOPE.md | b1d13d02bf7a8d0f6256e479f8679cd73e76027e40723a98f827ef6f32fbf282 |
| ROOT-CARD.md | f80dd703f9faf344b0ec1193ab80e5373917dafb33fefed2425c639678f63cc1 |
| f10-middle-full-boundary-astra-20260910.md | 82f11ed717d1691bb37c36242fdd9eb1eea23ec5eb46b42db5590b1997db18e6 |
| f10-middle-full-boundary-gate-fable5-20260910.md | 8a80bcc8ad7dd9068b503e9b1e18b4a5e6532d70f559658e3aa7077ec1928491 |
| f10-middle-univariate-unit-astra-20260910.md | 890e5c9c63a333bf873e963821c368d2dc080476eaf12c9fc6a10dce53db75e5 |
| f10-middle-septic-gate-fable5-20260910.md | cff18a06c050d64074ba9af70cea61b28b15614a61691125ebf26d3012577c62 |

All seven recomputed by sha256sum at 07:39:49Z and match the charged list exactly. Targets confirmed absent before this skeleton was written.

## A. Valuation profile (r = 1,3 mod 7)

Verdict: CONFIRMED. Premises taken as accepted (17zzb (3),(8); 17zzd A-B): D=12V^2-12(1-tau)V+(1+tau)(2-3tau); K=-840V^3+840(1-tau^2)V^2+42(1+tau)(2+tau)(4tau-3)V+k0, k0=2(2-3tau)(1+tau)(2+tau)(3+tau); gamma=tau[(1+tau)(2+tau)(3+tau)-30(1+tau)(2+tau)V+180(1+tau)V^2-120V^3]; S=2K^2-140tau(1+tau-6V)KD+245gamma D^2; tau=r/m, m=3r+1.

Residues (own table, m=3r+1 mod 7 and tau=r/m mod 7 by r mod 7): r=0: m=1, tau=0. r=1: m=4, tau=1/4=2 (4*2=8=1). r=2: m=0 (pole; 7|3r+1 iff r=2 mod 7). r=3: m=3, tau=1. r=4: m=6, tau=4*6=24=3 (6^-1=6). r=5: m=2, tau=5*4=20=6. r=6: m=5, tau=6*3=18=4 (5^-1=3). So the denominator is a 7-adic unit exactly for r not 2 mod 7, and tau=2,1 mod 7 exactly for r=1,3 mod 7. CONFIRMED.

Unit factors of k0. tau=1: 2-3tau=-1, 1+tau=2, 2+tau=3, 3+tau=4, all units; k0=2(-1)(2)(3)(4)=-48=1 mod 7. tau=2: 2-3tau=-4, 3, 4, 5, all units; k0=2(-4)(3)(4)(5)=-480=-4=3 mod 7. The factors vanish mod 7 only at tau=3 (2-3tau), 6 (1+tau), 5 (2+tau), 4 (3+tau). CONFIRMED.

Integrality. For tau in Z_7 every displayed coefficient of D,K,gamma is in Z_7, and the multipliers 2, -140tau(1+tau-6V), 245 are in Z_7[V]; hence S=sum a_i V^i has all a_i in Z_7. K-k0=7[-120V^3+120(1-tau^2)V^2+6(1+tau)(2+tau)(4tau-3)V]=7L with L in Z_7[V], deg L<=3, L(0)=0 (840=7*120, 42=7*6). CONFIRMED.

Ledger by term, all degrees and 7-adic factors accounted for:
- 2K^2=2k0^2+28k0L+98L^2. 2k0^2: degree 0, unit. 28k0L: degrees 1..3 only, v>=1. 98L^2=2*49L^2: degrees 2..6, v>=2. Degree 7: none.
- -140tau(1+tau-6V)KD=-140tau k0(1+tau-6V)D-980tau(1+tau-6V)LD. v(140)=1 (140=7*20). First part: degree <=3, v>=1. Second part: 980=49*20, v>=2, degree <=6. Degree 7: none (1+3+2=6).
- 245gamma D^2: 245=5*49, v>=2 in every degree; degree 7 coefficient 245*(-120tau)*(12)^2=-245*120*144*tau; 120=119+1=1 mod 7, 144=140+4=4 mod 7, tau unit, so v(a7)=2 EXACTLY.
Sums: a0=2k0^2+(7Z_7), a unit, so v(a0)=0 exactly (unit plus nonunit is a unit; no cancellation possible). a1..a3: every contribution has v>=1. a4..a6: contributions are 98L^2, the 980 part and the 245 term, all v>=2. a7: single contribution, v=2. Cancellation can only raise the intermediate valuations, which are used as lower bounds only; a zero coefficient has v=infinity and satisfies every bound. Profile (1) CONFIRMED with no real ordering and no sampled evaluation.

## B. Root-valuation -2/7 irreducibility argument

Verdict: CONFIRMED. Extend v=v_7 to an algebraic closure of Q_7 (unique extension); let x be a root of S, t=v(x). Values v(a_i x^i)=v(a_i)+it.
- t>-2/7: v(a0 x^0)=0. i=1,2,3: v>=1+it>1-2i/7>=1-6/7=1/7>0 (uses i<=3<7/2). i=4,5,6: v>=2+it>2-2i/7>=2-12/7=2/7>0 (uses i<7). i=7: 2+7t>0. Constant term uniquely minimal.
- t<-2/7: v(a7 x^7)=2+7t. i=1,2,3: difference >=1+it-2-7t=-1-(7-i)t>-1+2(7-i)/7>=-1+8/7=1/7>0. i=4,5,6: difference >=(i-7)t=-(7-i)t>0 since t<0. i=0: -2-7t>0. Leading term uniquely minimal.
A sum with a uniquely least-valued term is nonzero (ultrametric), so every root has t=-2/7 exactly; in particular no root is 0. Both sides and all intermediate coefficients checked; the constant/leading exactness (A) is what makes both minima unique, and the 3/4 split is exactly the Newton-polygon condition 1>2i/7 iff i<3.5 and 2>2i/7 iff i<7, with no lattice point on the line (i=3.5 is not an integer).

Proper factor. If S=GH in Q_7[V] with deg G=d, 1<=d<=6, and lc(G)=g_d, then G(0)/g_d=(-1)^d prod(roots of G) has v=-2d/7. G(0)!=0 because no root is 0, so G(0)/g_d is in Q_7^x and its valuation is an integer. 7|2d forces 7|d, impossible. Nonmonic G is handled by the ratio G(0)/g_d; no monic normalisation is needed. S in Q[V] (tau rational), and a factorisation over Q is one over Q_7, so S is irreducible over Q. CONFIRMED; no computed Newton polygon or factorisation test is used anywhere.

## C. r = 2 mod 7 chart

Verdict: CONFIRMED. r=2 mod 7 iff 7|3r+1=m; then r is a unit and b=1/tau=m/r lies in 7Z_7 with v(b)=v(m)>=1 arbitrary. Own substitution V=tau X:
- tau^-2 D(tau X)=12X^2-12((1-tau)/tau)X+(1+tau)(2-3tau)/tau^2=12X^2+12(1-b)X+(1+b)(2b-3): Dbar CONFIRMED.
- tau^-4 K(tau X): -840tau^3X^3/tau^4=-840bX^3; 840(1-tau^2)tau^2/tau^4=840(b^2-1); 42(1+tau)(2+tau)(4tau-3)tau/tau^4=42(b+1)(2b+1)(4-3b); k0/tau^4=2(2b-3)(b+1)(2b+1)(3b+1): Kbar CONFIRMED.
- tau^-4 gamma(tau X)=tau^-3[(1+tau)(2+tau)(3+tau)-30(1+tau)(2+tau)tauX+180(1+tau)tau^2X^2-120tau^3X^3]=(1+b)(1+2b)(1+3b)-30(1+b)(1+2b)X+180(1+b)X^2-120X^3: gbar CONFIRMED.
- tau(1+tau-6tauX)=tau^2(1+b-6X), so tau^-8 S(tau X)=2(tau^-4K)^2-140(1+b-6X)(tau^-4K)(tau^-2D)+245(tau^-4gamma)(tau^-2D)^2=Sbar as displayed. CONFIRMED.
Integrality: b in Z_7 makes every coefficient of Dbar,Kbar,gbar 7-integral. Kbar constant 2(2b-3)(1+b)(1+2b)(1+3b)=2(-3)(1)(1)(1)=-6 mod 7 (unit); nonconstant coefficients -840b, 840(b^2-1), 42(...) are all divisible by 7, so Kbar=kbar0+7Lbar with Lbar(0)=0, deg<=3. lc(Dbar)=12, lc(gbar)=-120, so lc(Sbar)=245*(-120)*144=-245*120*144, v=2 exactly; consistent with tau^-8*(-245*120*144*tau)*tau^7. The ledger of A applies verbatim (2kbar0^2=72=2 mod 7 unit; 28kbar0 Lbar and 140kbar0(1+b-6X)Dbar of degree <=3; the rest v>=2), giving (1) for Sbar and irreducibility over Q_7 by B.
Arbitrary v(3r+1): only b=0 mod 7 is used, never v(b)=1. CONFIRMED. Rescaling: S(V)=tau^8 Sbar(V/tau) with tau a nonzero rational, and G(V)H(V)=S(V) would give tau^-8 G(tauX)H(tauX)=Sbar(X), a proper factorisation over Q; so Sbar irreducible implies S irreducible over Q (and over Q_7). CONFIRMED. The third family is exactly {r>=2: 7|3r+1}, starting at r=2.

## D. Implication through accepted 17zzd

Verdict: CONFIRMED. Accepted 17zzd: B_nu=A_nu=Q[V]/(S) (guard W t5 automatic, no localisation), D a unit of A_nu, DZ=T=DP-ell K in A_nu, deg T=5 exactly with LC 12*840=10080 for every actual (r,h) (P has LC 840 from 17zz (6); ell K has degree 4). Hence T is a nonzero element of Q[V] of degree 5<7 for EVERY allowed h, r+2<=h<=2r. With S irreducible of degree 7, any common divisor of S and T is 1 or S, and S does not divide T (degree), so gcd(S,T)=1 in the PID Q[V]. Euclid gives a S+b_Bez T=1 with a,b_Bez in Q[V] (b_Bez is the Bezout cofactor, unrelated to the chart b=1/tau of C). In B_nu: b_Bez T=1, so Z=D^-1 T is a unit with Z^-1=T^-1 D=b_Bez D. This holds in the ENTIRE B_nu (no component discarded, no residue field chosen, guard retained), hence in every B_nu-algebra: the Laurent scale extension L=B_nu[s,s^-1], every base change, nonreduced ones included, since ring maps send units to units. Equivalently B_nu/(Z)=0, i.e. all seven geometric normalised leading points of 17zzd are nonresonant, for every h at every r=1,2,3 mod 7. CONFIRMED.

## E. Scope and negative control

Infinite families, genuinely. The only hypotheses used are 7-adic residue conditions on tau: tau=1 or 2 mod 7 (r=3,1 mod 7) or 1/tau=0 mod 7 (r=2 mod 7). Each is an infinite arithmetic progression of integers r>=2 (r=3,10,17,...; r=8,15,...; r=2,9,16,...) and the argument never specialises r beyond its residue, never uses generic-tau irreducibility over Q(tau) (which would not descend to specialisations), and never evaluates a sample. CONFIRMED as an infinite-family theorem: 3 of the 7 residue classes.

Negative control (own failure map, with k0 and a7 from A): r=0 mod 7 gives tau=0, so k0 stays a unit but v(a7)>=3 (and the whole 245gamma D^2 term has v>=3): the leading exactness fails. r=4 (tau=3): 2-3tau=0 mod 7. r=5 (tau=6): 1+tau=0. r=6 (tau=4): 3+tau=0. In these three classes v(a0)>=1 and the constant exactness fails. So exactly one hypothesis of (1) fails in each uncovered class, and failure of (1) is NOT reducibility: the 7-adic polygon simply is not determined by this pattern, and nothing here exhibits a reducible S or a resonant point. Also, 17zzd's squarefree/etale rank-7 statement gives seven distinct roots only; a squarefree septic can share a factor of degree <=5 with a quintic, so it does not license the degree argument of D; irreducibility (B) is what does. Producer states both limits correctly.

Precision items (no verdict change): (P1) the letter b denotes both the chart 1/tau and the Bezout cofactor in the producer; kept distinct above. (P2) the r=1 mod 7 family starts at r=8 since r>=2. (P3) the producer sketches the ledger of A in prose; the term-by-term reconstruction above is independent. Not asserted by anyone and not asserted here: full source, forcing, all-r, JC2, or any factorisation on r=0,4,5,6 mod 7.

## F. Verdict table

| claim | verdict |
|---|---|
| A: r=1,3 mod 7 have unit denominator, tau=2,1 mod 7; k0 factors units; S,gamma,K=k0+7L integral; v(a0)=0, v(a1..3)>=1, v(a4..6)>=2, v(a7)=2 exactly, all contributions and cancellations accounted | CONFIRMED |
| B: unique-minimum contradiction on both sides of -2/7 including constant/leading and every intermediate coefficient; proper degree-d factor has integer valuation -2d/7, impossible for 1<=d<=6; nonmonic handled; Q_7 irreducible implies Q irreducible | CONFIRMED |
| C: r=2 mod 7 chart V=tau X, Sbar=tau^-8 S(tau X); Dbar/Kbar/gbar exactly as displayed; 7-integral; Kbar constant -6 mod 7, nonconstant coefficients divisible by 7; LC -245*120*144; valid at every v(3r+1)>=1; rescaling preserves irreducibility | CONFIRMED |
| D: through accepted 17zzd, deg T=5 with LC 10080 for all allowed h, gcd(S,T)=1, Bezout, Z^-1=b_Bez D in the entire B_nu, all components/guards, Laurent extension and all base changes | CONFIRMED |
| E: infinite families (not generic Q(tau), not samples); four uncovered classes with named failing hypothesis; failure is not reducibility; squarefree is not irreducibility | CONFIRMED |

REFUTED: none. GAP: none within the charged claims. Hostile attacks tried and failed: a hidden degree-7 contribution outside 245gamma D^2 (none: the other terms have degree <=6); a 7 in 120 or 144 (120=1, 144=4 mod 7); a nonunit factor of k0 at tau=1,2 (all listed); cancellation lowering v(a0) or v(a7) (single unit contribution each); a lattice point on the polygon line (none); a root at 0 (excluded by v=-2/7); a degenerate T at some h (LC 10080 is h-independent); a dependence on v(3r+1)=1 in C (none used).

## OPEN(S) RAISED

None. No new canonical OPEN ID. The remaining quantity is unchanged in substance and now named exactly: uniform irreducibility, or uniform gcd(S,T)=1, on the four actual residue families r=0,4,5,6 mod 7. Cheapest next obligation per the producer: a uniform obstruction there (e.g. a different prime or a different chart), not samples.

## COLLISIONS

status: EMPTY

- NONE. This lane wrote exactly xmodel/f10-middle-septic-irred-gate-fable5-20260910.md and box/f10-middle-septic-irred-gate-fable5-20260910/README.md, both absent at 07:39:49Z. No Seal, no charge_basis (no exit-price assertion is made), no source modification, no coefficient artifact, no subprocess, no rerun of any accepted report, no network, no other lane touched. Every 64-hex token in this file equals a charged input hash from live sha256sum output.

Box contents: README.md and worksheet.md (hand residue table and valuation ledger, text only).

## Completion

Own WHOLE read of this file at 07:44:22Z preceded the marker: no PENDING, OPEN(S) RAISED none, COLLISIONS EMPTY, every 64-hex token equal to a live pin hash. Timeline: first action 07:39:49Z, all sections written 07:44:12Z, marker written before the 07:51:49Z reserve and the 07:53:49Z stop; never reset. No Seal and no charge_basis authored; the adapter seals. Summary: A, B, C, D and E CONFIRMED; REFUTED none; GAP none within the charged claims. The result is a partial uniform middle-nonresonance theorem on the three residue families r=1,2,3 mod 7, with r=0,4,5,6 mod 7 expressly uncovered. The marker below is the only standalone marker in this file and nothing follows it. All writers idle at the marker.

<!-- BODY-END -->
