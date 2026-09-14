# Hostile all-strata low-pivot gate: F10 r=1 unit pivot (Fable 5.1)

tag=f10-r1-low-pivot-gate-fable5-20260909
frozen_basis=0d39df3c9fd69c939a8420c54d03228b9077777d (provenance only)
reviewer=Claude Fable 5.1 (claude-fable-5-1); different-model review of a NEW/PROVISIONAL Astra derivation
launch=root actual invitation; actual lane start 12:51:43 UTC (recorded, not reset); hard stop = earlier of 13:06:43 and 13:07:00 UTC, i.e. 13:06:43 UTC
subprocesses=ZERO mathematical subprocesses. Only date, ls, mkdir, sha256sum, cat, wc, head, tail, grep, od, sed ran. Every identity below is hand-derived factored algebra.

## 0. Custody and read scope

All FIVE charged objects under /tmp/jc2-lane.wbs2qn/inputs were pinned (box/f10-r1-low-pivot-gate-fable5-20260909/input-pins.sha256) BEFORE their WHOLE reads. Hashes match the invitation's ordered list exactly: 07517656 (root body, 234 lines), 5478e877 (its artifact: body_bytes 12882, body_sha256 d6305dbf, opened 12:27:42Z, closed/finalized 12:38:08Z, mode 0444, consistent with the body's own seal and its stated 12:27:42 pin / 12:42 stop), a5ab487c (16r Euler elimination, 251 lines), 77d59f7b (my own accepted 16r gate, 89 lines), 26687318 (16q cubic module, 244 lines). Accepted 16r/16q are used only as interfaces; their interiors were not re-hardened. No newer maximal-h theorem, live gate, ledger, log, provenance path, web or remote state was opened. No corpus scan.

Object identification. Root's recursion (line 26) is 16r's (5) at r=1 with beta=gamma=0, k(0)=0, B5=S^2; root's (delta0..delta7) is 16r's (4); root's E0,E1 are 16r's (12) E0_res,E1_res; root's guard omega*a*b-1 is 16r's (13) with a=k4, b=[S^7]B0. Root's H0..H3 are 16r's h=1-ud+Sv coefficients: H0=1-u d0, H1=v0-u d1, H2=v1, H3=v2. All consistent.

## A. Low jets (1) and exact variations (2)-(4). CONFIRMED.

j=4. Q4=2uS-5f'S^2+4fS with f=-u+d0 S+d1 S^2: Q4=-2uS-d0 S^2-6d1 S^3; eigenvalues 1,-2,-5 give B4=-2uS+(d0/2)S^2+(6d1/5)S^3. So (B4)_1=-2u, (B4)_2=d0/2, (B4)_3=6d1/5, matching 16r's e0=d0/2, e1=6d1/5.

j=3. Constant of Q3: -u^2+2(-u)(-2u)=3u^2, eigenvalue 3, (B3)_0=u^2. S-slot: -2+8u d0-6u d0+2H0=0, so beta=(B3)_1=0 is the gauge slot. S^2-slot: -4(d0^2/2-4u d1)+2(-18u d1/5+d0^2-2u d1)-5H1+2H1=(24/5)u d1-3H1, eigenvalue -3, (B3)_2=H1-(8/5)u d1. Matches root and 16r's zeta at e1=6d1/5.

j=2. Constant: 2u-3d0 u^2-2uH0=-u^2 d0, eigenvalue 2, (B2)_0=-u^2 d0/2. S-slot of Q2: -ell-6u^2 d1+(-4uH1+32u^2 d1/5)+8uH1+(H0 d0-2uH1)=-ell+d0-u d0^2+2uH1+(2/5)u^2 d1, eigenvalue -1, (B2)_1=ell-d0+u d0^2-2uH1-(2/5)u^2 d1. Matches root, and equals 16r's w at beta=0.

j=1. Constant of Q1: ell u-1-2d0(B2)_0-2u(B2)_1-3u^2 H1 (the k' term is -4k'B4 and (B4)_0=0; h B3' constant is H0*(B3)_1=0), eigenvalue 1. Substituting: -1-u ell+2u d0-u^2 d0^2+u^2 H1+(4/5)u^3 d1=-H0^2-u ell+u^2 H1+(4/5)u^3 d1. Root's (1) exact.

Variation q1 S+q2 S^2. B4,B3 fixed (k enters j=4,3 only through B7,B6=0). j=2: delta Q2=-5(q1+2q2 S)S^2, eigenvalues -4,-7: delta B2=(5/4)q1 S^2+(10/7)q2 S^3, root's (2). j=1: delta Q1=-2f' delta B2+2f delta B2'-4 delta k' B4. Constant 0. S-slot: 2(-u)(5/2)q1-4 q1(-2u)=3u q1, eigenvalue -2, delta(B1)_1=-(3/2)u q1. S^2-slot: -2 d0(5/4)q1+2[(-u)(30/7)q2+d0(5/2)q1]-4[(d0/2)q1-4u q2]=(d0/2)q1+(52/7)u q2, eigenvalue -5, delta(B1)_2=-(d0/10)q1-(52/35)u q2. Root's (3) exact, including the intermediate 3u q1 and (d0/2)q1+(52/7)u q2. j=0: S-slot of delta Q0 from -f' delta B1+2f delta B1'-2h' delta B2+h delta B2'-3 delta k' B3: (-d0+2d0)delta(B1)_1-4u delta(B1)_2+2H0 delta(B2)_2-3(2q2)(B3)_0 = d0 delta(B1)_1-4u delta(B1)_2+2H0 delta(B2)_2-6u^2 q2, root line 75 exact (the +d0 is -d0 from -f'B1 plus 2d0 from 2fB1'). Substituting: [(5/2)H0-(11/10)u d0]q1-(2/35)u^2 q2; eigenvalue -3; delta B0'(0)=[-(5/6)H0+(11/30)u d0]q1+(2/105)u^2 q2. With H0=1-u d0: -(5/6)+(25/30+11/30)u d0=-5/6+(6/5)u d0. Root's (4) exact in both coefficients and signs.

k3/k4 independence. For q S^j, j>=3: delta k' starts at S^(j-1); delta Q2=-5 delta k' S^2 starts at S^(j+1), so delta B2 does; delta Q1 terms f' delta B2, f delta B2', delta k' B4 start at S^(j+1), S^j, S^(j-1+1)=S^j, so delta B1 starts at S^j; delta Q0 terms start at S^j, S^(j-1), S^(j+1), S^j, S^(j-1) (delta k' B3 with (B3)_0=u^2), so delta B0 starts at S^(j-1)>=S^2. The four entries (B1)_0,(B1)_1,(B2)_0,(B0)_1 used by e0=k1(B1)_0-H0(B0)_1-1 and e1=2k1(B2)_0+H1(B1)_0-H0(B1)_1+2u(B0)_1-u are untouched. Confirmed. (Corollary, stronger than root: the constants c0,c1 and R0 lie in Q[u,ell,d0,d1,v0,v1]; v2,k3,k4,omega do not enter them.)

Affine, not infinitesimal. The recursion is linear in (B2,B1,B0) with k entering only through k' (linear) times the FIXED B5,B4,B3 and through the affine B2,B1: so B2,B1,B0 are affine in (k1,..,k4) as polynomials, and the exact differences above ARE the linear parts. In e0, k1 multiplies the k-independent (B1)_0; in e1, k1 multiplies the k-independent (B2)_0, and (B1)_1,(B0)_1 are affine. Hence e0,e1 are exactly affine in (k1,k2), no quadratic term. Confirmed.

## B. Constants (5), row R, literal J,L,R0 (6), Bezout (7)-(8). CONFIRMED.

e0 k1-coefficient (B1)_0-H0(-5/6+(6/5)u d0)=-H0^2+(5/6)H0-(6/5)u d0 H0-u ell+u^2 H1+(4/5)u^3 d1=H0[-1+u d0+5/6-(6/5)u d0]+...=-H0(1/6+u d0/5)-u ell+u^2 v0-u^3 d1/5=Acoef. k2-coefficient -(2/105)H0 u^2. e1 k1-coefficient 2(B2)_0+(3/2)uH0+2u(-5/6+(6/5)u d0)=-u^2 d0+(3/2)u-(3/2)u^2 d0-(5/3)u+(12/5)u^2 d0=-u/6-u^2 d0/10=Q. k2-coefficient 2u(2/105)u^2=(4/105)u^3. (5) exact; c0,c1 are e0,e1 of the same recurrence at k1=k2=0, polynomials, not variables.

R=e0-(d0/2)e1: k2-coefficient -(2/105)u^2(H0+u d0)=-(2/105)u^2=L, using only H0+u d0=1 (no division). k1-coefficient Acoef-(d0/2)Q=-(1-u d0)(1/6+u d0/5)+u d0/12+u^2 d0^2/20-u ell+u^2 v0-u^3 d1/5=-1/6+u d0(-1/30+1/12)+u^2 d0^2(1/5+1/20)-u ell+u^2 v0-u^3 d1/5=-1/6+u(d0/20-ell)+u^2(d0^2/4+v0-u d1/5). (6) exact: j1=d0/20-ell, j2=d0^2/4+v0-u d1/5, R0=c0-(d0/2)c1. Row operation invertible: e0=R+(d0/2)e1 with e1 a generator, so (e0,e1,rest)=(R,e1,rest) over the polynomial ring.

Bezout. sJ=-6(1+6u j1)(-1/6+u j1+u^2 j2)=(1+6u j1)(1-6u j1-6u^2 j2)=1-36u^2 j1^2-6u^2 j2-36u^3 j1 j2=1-u^2 M with M=36j1^2+6j2+36u j1 j2; zL=-(105/2)M*(-(2/105)u^2)=u^2 M; sJ+zL=1. (7) exact over T=Q[u,ell,d0,d1,v0,v1,v2,k3,k4,omega], hence over every T-algebra and every u,J,H0 stratum (u=0: s=-6,J=-1/6; J=0: u^2 M=1). Matrix [[J,L],[-z,s]] has det Js+Lz=1; its adjugate [[s,-L],[z,J]] is the inverse: product [[Js+Lz, -JL+LJ],[-zs+sz, zL+sJ]]=I. So psi: X=Jk1+Lk2, Y=-zk1+sk2 and phi: k1=sX-LY, k2=zX+JY are mutually inverse T-algebra automorphisms; (8) exact. Under phi, R=Jk1+Lk2+R0=X+R0, coefficient ONE on every stratum.

## C. Quotient isomorphism 12/20 to 11/at most 19. CONFIRMED.

L1 in T[k1,k2] (12 variables) is generated by the 10 E0 slots (degree<=9=7r+2), 9 E1 slots (degree<=8=6r+2), and omega*k4*b-1: 20 slots. Step 1 replaces e0 by R (same ideal). Step 2 applies the automorphism above (ideal transported isomorphically; R becomes X+R0 with R0 in T). Step 3: T[X,Y]/(X+R0, G_i)=T[Y]/(G_i(-R0,Y)) since X+R0 is linear in X with unit coefficient 1; this holds over any ring. The composite gives T[k1,k2]/L1 isomorphic to T[Y]/L1' where L1' is generated by e1, (E0)_i (i=1..9), (E1)_i (i=1..8) and omega*k4*b-1 with (9) k1=-sR0-LY, k2=-zR0+JY substituted: 1+9+8+1=19 slots, 11 variables. Every original generator is transported by substitution, none dropped; X+R0 is solved, not discarded. Y=-zk1+sk2 is a polynomial combination of source coordinates, no new gauge. Ring isomorphism gives bijection of points over every Q-algebra and transports unitness/properness exactly. No ambient-ring or ungauged-point bijection is asserted beyond this. Confirmed.

Observation (not a flaw): b=[S^7]B0 is in fact independent of k1,k2, since the variation delta B0 has degree<=5 (delta k degree<=2, delta B2<=3, delta B1<=4, delta B0<=5 by the same recursion) while n=7; so the transported guard is literally the original omega*k4*b-1. Root's "fully transported" statement remains correct.

## D. Controls and composition. CONFIRMED.

u=0 boundary. f=d0 S+d1 S^2, h=1+v0 S+v1 S^2+v2 S^3, B4=(d0/2)S^2+(6d1/5)S^3, (B3)_0=(B3)_1=0, (B3)_2=v0. (B2)_0=0, (B2)_1=ell-d0. S^2-slot of Q2: -3d0 v0+4d0 v0-2d0 v0+(18d1/5+d0 v0)-5k1=18d1/5-5k1, eigenvalue -4: (B2)_2=(5/4)k1-(9/10)d1. (B1)_0=-1. S-slot of Q1: -2d0(ell-d0)+2d0(ell-d0)+2v0=2v0, eigenvalue -2: (B1)_1=-v0. S-slot of Q0: (d0 v0+2d1)-2d0 v0-2v0(ell-d0)+[(5/2)k1-(9/5)d1+v0(ell-d0)]=d1/5-ell v0+(5/2)k1, eigenvalue -3: B0'(0)=-(5/6)k1-d1/15+ell v0/3. Then e0=-k1+(5/6)k1+d1/15-ell v0/3-1=-k1/6+d1/15-ell v0/3-1 and e1=0+v0(-1)-(-v0)+0-0=0: root's (10) exact, consistent with (5)-(6) at u=0 (J=-1/6, L=0, Q=0, c1=0). (9) gives k1=6R0=6c0=(2/5)d1-2ell v0-6; Y=-zk1-6k2 still parametrizes k2 bijectively. Delta k1=6 gives delta e0=-1 by the -1/6 coefficient, so the row is a retained target-1 equation, not automatic. Confirmed.

J=0 upper/guard control. u=1, ell=d0=d1=0, v0=1/6, v1=0, v2=1, k=S^4: j1=0, j2=1/6, J=0, L=-2/105, M=1, s=-6, z=-105/2. f=-1, f'=0, B4=-2S, h=1+S/6+S^3, h'=1/6+3S^2. [S^4]Q3=-5*3+2*1=-13, eigenvalue -9: [S^4]B3=13/9. [S^5]Q2=-5*4=-20 (only -5k'S^2 reaches S^5), eigenvalue -13: [S^5]B2=20/13. [S^7]Q0=-2*3*(20/13)+1*5*(20/13)-3*4*(13/9)=-20/13-52/3, eigenvalue -21: b=(20/13+52/3)/21=((20/13)+12(13/9))/21, positive, nonzero, a=k4=1; omega=1/b meets the guard. Matrix [[0,-2/105],[105/2,-6]] has det 0+1=1; with the lower-left entry omitted (z=0) det 0. Root's control exact; it is an upper/guard control only, not a full point, and the root labels it so. Confirmed.

Composition with accepted 16r. 16r gives, for every characteristic-zero field K, existential equivalence of K-points of L1 and the complete compact system, and 1 in L1 iff 1 in I1. The new ring isomorphism T[k1,k2]/L1=T[Y]/L1' preserves K-points bijectively and unitness exactly, so the exact 112/196 source decision (proper => Qbar-point => Keller non-automorphism of degrees 112,196; unit => r=1 stratum excluded) is preserved unchanged. It establishes no point, no properness or unit, no exclusion, no emitted nonzero-row count (19 is an envelope) and no runtime. Confirmed as stated by the root.

Inflation flag. By hand: deg s<=2, deg z=deg M<=4, deg R0<=7 (c0<=7 via H0*(B0)_1 with the 16r bound 5 on B0 coefficients; c1<=6). So the images of k1,k2 under (9) have degree<=9 and <=11. E0,E1 coefficients are quadratic in (k1,k2) (k'*B1 and k'*B2 terms), so a slot of original degree<=7 can reach degree about 27 after substitution, with term counts driven by squares of R0. Eleven variables is not a speed claim; the root correctly claims none.

## Verdicts and strongest surviving scope

A CONFIRMED, B CONFIRMED, C CONFIRMED, D CONFIRMED. No sign error, dropped stratum, generic division, extra gauge or dropped row was found. Strongest exact conclusion: over T=Q[u,ell,d0,d1,v0,v1,v2,k3,k4,omega], with J,L,R0,s,z,M as in the root's (6) and section 5, sJ+zL=1 identically; the T-algebra automorphism (8) and the coefficient-one elimination X=-R0 give a ring isomorphism between Q[12 vars]/L1 and T[Y]/L1', L1' generated by the 19 substituted slots; every Q-algebra point and the unit question transfer exactly, and composition with accepted 16r preserves the r=1 112/196 decision. Properness or unitness of L1' is open in both directions. No authored seal, no exit-price line, no promotion or follow-on authority.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN check, no corpus scan.

<!-- BODY-END -->
