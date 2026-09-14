# FIRST gate: faithful symmetric contact equations and exact exceptional slice (producer f10-contact-symmetric-remainder-astra-20260910)

2026-09-10. Gate lane fable5. First action 01:07:30 UTC; fixed stop 01:19:30 UTC (earlier than launch+15 min, 01:22:30); publication reserve from 01:17:30 UTC. Charged inputs: the four ordered SHA256 pins in the lane brief, all four verified byte-identical in /tmp/jc2-lane.HwN6Sj/inputs before any body read (96deb541 producer 10488 B; 59b8311a ROOT-CARD 3457 B; 4bbecd35 discriminator 18506 B; 4a46e7f6 accepted17w gate 12680 B). All four read WHOLE; no clipping. Premises: the literal A_X,B_X of accepted17w and its gate, the card's G,H. The earlier unreviewed dimension<=1 report is not an input. ZERO mathematical subprocesses; all algebra below is manual. No Seal, no charge_basis.

## 0. Verdict table

| Item | Verdict | Smallest actual defect |
|---|---|---|
| A eight coefficients of 720A_X, 5040B_X; reductions; equations (1) | CONFIRMED | none |
| B C ~= R[x]/(x^2-sx+p), G=dH, Delta=d^2, both directions, etale free rank 2, faithful, dim transport | CONFIRMED | none |
| C V=1/3 slice: (3), W=1/27 via s-3, quartic (4), three pairs, all guard values, Q^6/Q^3, invariants, no nilpotents | CONFIRMED | none |
| D saturation (6), predicate (7) <=> generic chart zero/zero-dimensional, whole finiteness | CONFIRMED | F1: "x,y satisfy the quartic" lives in C, needs (2) |
| E emptiness REFUTED by six guarded points; none in 5/3<x<y<2; finiteness GAP; guards load-bearing; no forcing/closure/JC2 claim | CONFIRMED as scoped | none |

The four equations (1) are an exact, verified representation and MAY be consumed by a separately registered elimination (section E). Whole-locus finiteness is NOT decided here or by the producer. This is a new unreviewed result reviewed once; no promotion authority.

## A. Eight nonleading coefficients and the four remainder equations

Scalar products, by hand: (X-2)(X-3)(X-4)(X-5)=(X^2-7X+10)(X^2-7X+12)=X^4-14X^3+71X^2-154X+120; (X-2)(X-3)(X-4)=X^3-9X^2+26X-24; (X-2)(X-3)=X^2-5X+6. Then 720A_X = 360W^2+720(X-2)VW+120(X-2)(X-3)W+120(X-2)V^3+180(X-2)(X-3)V^2+30(X-2)(X-3)(X-4)V+(X-2)(X-3)(X-4)(X-5). Collecting: X^3: -14+30V. X^2: 71-270V+180V^2+120W. X: -154+780V-900V^2+120V^3-600W+720VW. X^0: 120-720V+1080V^2-240V^3+720W-1440VW+360W^2. All four match a3..a0; no V^2W term, correctly.

(X-3)(X-4)(X-5)(X-6)=(X^2-9X+18)(X^2-9X+20)=X^4-18X^3+119X^2-342X+360; (X-3)(X-4)(X-5)=X^3-12X^2+47X-60; (X-3)(X-4)=X^2-7X+12. Then 5040B_X = 2520W^2+2520V^2W+2520(X-3)VW+210(X-3)(X-4)W+840(X-3)V^3+420(X-3)(X-4)V^2+42(X-3)(X-4)(X-5)V+(X-3)(X-4)(X-5)(X-6). X^3: -18+42V. X^2: 119-504V+420V^2+210W. X: -342+1974V-2940V^2+840V^3-1470W+2520VW. X^0: 360-2520V+5040V^2-2520V^3+2520W-7560VW+2520V^2W+2520W^2. All four match b3..b0. Eight of eight nonleading coefficients confirmed.

Reductions: X^2=sX-p; X^3=s(sX-p)-pX=(s^2-p)X-sp; X^4=(s^2-p)(sX-p)-spX=(s^3-2sp)X+(p^2-s^2p). Confirmed. Remainder of a monic quartic X^4+c3X^3+c2X^2+c1X+c0 is then [(s^3-2sp)+c3(s^2-p)+c2 s+c1]X+[(p^2-s^2p)-c3 sp-c2 p+c0], exactly (1) for c=a and c=b. Division is by the monic q, over any Q-algebra; no leading coefficient inverted, no field assumption. A CONFIRMED.

## B. Ordered cover C ~= R[x]/(x^2-sx+p): guards, difference identity, etale rank two

Q[x,y] is free over Q[s,p] with basis 1,x, and y=s-x; q(y)=(s-x)^2-s(s-x)+p=x^2-sx+p=0. Factor identities: xy=p; (x-1)(y-1)=p-s+1; (3x-5)(3y-5)=9p-15s+25; (2-x)(2-y)=p-2s+4; (y-x)^2=s^2-4p=Delta; x+y-3=s-3; 4-x-y=4-s; Gamma, Omega are the card's forms under s=x+y, p=xy. Hence G=(y-x)H. Since y-x divides H, inverting G in Q[x,y,V,W] equals inverting H; and Delta unit <=> d unit. Guards match in both directions; W and every factor kept.

Ideal identity, formal over any coefficient ring: a(X)=q(X)h(X)+F_a1 X+F_a0 in R0[X] (R0=Q[s,p,V,W,G^-1]). Evaluating at x and at y: a(x)=F_a1 x+F_a0, a(y)=F_a1 y+F_a0. So F_a1=F_a0=0 gives a(x)=a(y)=0, i.e. A_x=A_y=0 (720 a unit). Conversely a(x)-a(y)=F_a1(x-y); x-y is a unit, so F_a1 in (a(x),a(y)), then F_a0=a(x)-F_a1 x also. Same for b with 5040. Thus (A_x,A_y,B_x,B_y)S_G=(F)S_G, and C=S_G/(F)=(R0/F)[x]/(x^2-sx+p)=R[x]/(x^2-sx+p) by right exactness. Nilpotents retained; no field point used.

Etale/faithful: R[x]/(x^2-sx+p) is free of rank two; (2x-s)^2=4(sx-p)-4sx+s^2=Delta is a unit, and 2x-s=x-y, so the derivative is a unit and the algebra is standard etale. Free of positive rank gives R -> C injective and faithfully flat: R=0 <=> C=0. Integral and injective gives dim R=dim C (Cohen-Seidenberg), a total-dimension statement, not a generic-fibre one. B CONFIRMED.

## C. The closed V=1/3 slice

a-b coefficients in general: X^3: 4-12V. X^2: -48+234V-240V^2-90W. X: 188-1194V+2040V^2-720V^3+870W-1800VW. X^0: -240+1800V-3960V^2+2280V^3-1800W+6120VW-2520V^2W-2160W^2. At V=1/3: cubic 0; quadratic 10/3-90W; linear -10+270W (2040/9-80/3=200); constant 360-440+760/9=40/9, W-terms -1800+2040-280=-40, so 40/9-40W-2160W^2=(40/9)(1-27W)(1+18W) since (1-27W)(1+18W)=1-9W-486W^2. Each equals (10/3)(1-27W) times 1, -3, 4/3+24W. Factorization (3) CONFIRMED in full.

Modulo q: X^2-3X+4/3+24W == (s-3)X+(4/3+24W-p). In R/(3V-1), F_a1-F_b1=0 reads (10/3)(1-27W)(s-3)=0; s-3 is a factor of G, hence a unit, so 27W=1 as an ideal consequence; 1-27W is never inverted. CONFIRMED. Then a=b at (1/3,1/27): a3=10-14=-4; a2=71-90+20+40/9=49/9; a1=-154+260-100+(40-200+80)/9=-26/9; a0=0+(-80+240-160)/9+40/81=40/81. Elementary symmetric functions of {1/3,2/3,4/3,5/3}: 4, 49/9, 26/9, 40/81. (4) CONFIRMED. Independent cross-check: at V=1/3, W=1/27, c(t)=(1+t/3)^3, so [t^6]c^X=C(3X,6)/729 and [t^7]c^X=C(3X,7)/2187 vanish exactly at 3X in {0..5} resp. {0..6}; after removing X(X-1) resp. X(X-1)(X-2) both leave the roots {1/3,2/3,4/3,5/3}. So (4) is the perfect-cube degenerate family, not a physical point.

In C/(3V-1): W=1/27 forced (as above, or a(x)-b(x), a(y)-b(y) differ by (10/3)(1-27W)d(s-3)). Q[x,y]/(a*(x),a*(y)) = Q^16 (split squarefree quartic), the ordered pairs from {1/3,2/3,4/3,5/3}. H kills x or y=5/3 and x=y; no root is 0,1,2. Six ordered pairs remain. Guard values per unordered pair {1/3,2/3},{1/3,4/3},{2/3,4/3}: s=1,5/3,2; p=2/9,4/9,8/9; (x-1)(y-1)=2/9,-2/9,-1/9; (3x-5)(3y-5)=12,4,3; (2-x)(2-y)=20/9,10/9,8/9; Delta=1/9,1,4/9; s-3=-2,-4/3,-1; 4-s=3,7/3,2; Gamma=8+9-114+181=84, 16+25-190+181=32, 32+36-228+181=21; Omega=15-8-30+35=12, 125/3-16-50+35=32/3, 60-32-60+35=3; W=1/27. All nonzero: the producer's table and ALL guard factors CONFIRMED. Hence C/(3V-1)=Q^6 (localizing a product of fields at H keeps exactly the factors where H!=0). R/(3V-1) is the invariant ring of the swap x<->y on the free rank-two algebra: u+vx invariant iff v=-v iff v=0 (char 0; equivalently v(2x-s)=0 with 2x-s a unit), so it is Q^3, one factor per unordered pair; consistent with rank two. Reduced, so no nilpotent multiplicity hidden. These are points of the guarded contact locus with exponents outside 5/3<x<y<2; no physical/Keller/source meaning and no positive-dimensional component. Isolation in the full R is not claimed and is not proved. C CONFIRMED.

## D. Finiteness equivalence and predicate (7)

Spec R = D(3V-1) union V(3V-1); V(3V-1) is the three points of C. So the whole locus is finite iff R[(3V-1)^-1]=T[(G(3V-1))^-1]/F is zero or zero-dimensional; for a finite-type Q-algebra (Jacobson) finitely many primes <=> dim<=0, and by B this transports to C. Saturation: I T_loc = F T_loc and I = F T_loc cap T.

(7) => dim 0: f(V) in I nonzero gives f(V)=0 in R_loc, so V is algebraic in every residue field; same for W. Pass to C_loc=R_loc[x]/(x^2-sx+p): at any prime of C_loc, x and y are roots of the monic quartic a with coefficients in Q[V,W], hence algebraic, hence s=x+y, p=xy algebraic. Every prime of R_loc has a prime of C_loc over it with a larger residue field, so all residue fields of R_loc are algebraic over Q, so every prime is maximal: dim<=0 or the zero ring. Converse: a zero-dimensional finite-type Q-algebra is Artinian with residue fields finite over Q, so finite-dimensional over Q; multiplication by V has a nonzero annihilating polynomial f (Cayley-Hamilton), f(V) in F T_loc, so (G(3V-1))^N f(V) in F, f(V) in I; same for W; the zero ring gives f=1. Equivalence CONFIRMED. No eliminant, no isolation of the slice points, no hidden divisor exclusion is asserted by the producer, and none is needed for the equivalence. D CONFIRMED; documentary defect F1 only.

## E. Scope and control audit; consumability

Emptiness of the ENTIRE guarded complex locus is REFUTED by the six explicit ordered points of C (and three of R); each has x,y in {1/3,2/3,4/3}, all below 5/3, so none lies in 5/3<x<y<2. Whole FINITENESS is GAP at (7); no curve is exhibited and none is claimed. Guards are load-bearing: without s-3 the linear remainder (10/3)(1-27W)(s-3) vanishes on s=3 and W=1/27 is not forced (the constant then only gives p=4/3+24W); without Delta (diagonal), x=y makes a(x)=a(y) one equation and F_a1 is not recovered; a producer that drops either would describe a different object. Producer states no all-r late forcing, companion/source closure, counterexample or JC2 conclusion; correctly. Incidental: the accepted17w gate's Cramer value e_y should read +12(1+L)E/Gamma (det of [[1+L,-L],[Q_y,-Q_x]] is Gamma/12, e_y=(1+L)E/det), as ROOT-CARD states; the ideal identity is unaffected. u=1 is a field-point/explicit unit-chart fact only.

Consumability: YES. The four equations (1) with the coefficients verified in A, the guard G with every factor, and the ring transport of B form an exact representation of the guarded locus; a separately registered elimination may consume them as stated, provided it (i) keeps G entire, including W, Delta and s-3; (ii) either works in the saturation (6) or localizes at 3V-1 with the closed slice recorded as the three points of C; (iii) reports (7) as membership facts, not a generic count; (iv) treats the six points as a nonemptiness witness only. Whether (7) holds is not decided here.

## F. Smallest actual defects

F1 (documentary, D). Section 5 says "x,y then satisfy the monic quartic a" inside an argument about primes of the localized symmetric ring; x,y live in the ordered cover, and the step needs the lying-over/residue-field inclusion supplied by (2) and the faithful transport of section 3. Content unaffected.
F2 (documentary, C). Section 4 states R/(3V-1)~=Q^3 from the invariant argument; the direct reason v=-v => v=0 is the same argument, no gap. Nothing mathematical was found wrong in A-E.

## OPENS RAISED

- NONE new. The assigned gap stays as the producer recorded it, no new canonical ID: QUANTITY whether I cap Q[V] and I cap Q[W] are nonzero for I=F:[G(3V-1)]^infinity, presently undetermined; equivalently whether the generic chart is zero/zero-dimensional. Cheapest test unknown and not authorized here.

## COLLISIONS

status: EMPTY

- NONE — own-only check: the report and box were absent before the lane; no corpus, ledger or provenance scan performed.

Own WHOLE reread (66 lines, 11019 bytes, marker count 0) and own-only raised-OPEN/collision extraction done at 01:12:21 UTC, before the 01:17:30 publication reserve. Written: this report and box/f10-contact-symmetric-remainder-gate-fable5-20260910/READ-SCOPE.md, both via apply_patch only. No mathematical subprocess of any size, code, coefficient artifact, network, process inspection, agent, Git/shared/protected work or other-lane read occurred. Root retains custody and any further review; this gate gives no promotion authority.

<!-- BODY-END -->
