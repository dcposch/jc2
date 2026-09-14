# FIRST gate: explicit global U pivot on the guarded generic contact chart (producer f10-contact-finite-discriminator-astra-20260910)

2026-09-10. Gate lane fable5. First action 02:31:42 UTC; fixed stop 02:42:30 UTC (earlier than first+12 min, 02:43:42); publication reserve from 02:40:30 UTC. Charged inputs: the six ordered SHA256 pins of the lane brief, all six verified byte-identical in /tmp/jc2-lane.5SBO5P/inputs at 02:31:42 before any body read (c18309e4 producer 8126 B; e93e4027 ROOT-CARD 3602 B; 96deb541 accepted17zi producer 10488 B; f4f51690 accepted17zi gate 11573 B; 521ec17b accepted17zj producer 11813 B; 54e6c2b2 accepted17zj gate 14371 B). All six read WHOLE via parallel reads; no clipping. Premises: accepted17zi (exact quartics, four remainders, full G, faithful rank-two cover, closed V=1/3 slice: three symmetric points in R, six ordered in C, x,y in the cover needing lying-over) and accepted17zj (total UNGUARDED finite Q-dimension; optional cubic-remainder identities). Those are premises, not re-reviewed. ZERO mathematical subprocesses; every identity below was recomputed by hand. No Seal, no charge_basis.

## 0. Verdict table

| Item | Verdict | Smallest actual defect |
|---|---|---|
| A d,e,f,g literal; c=4-12V; three c^2 numerator identities; ACTUAL U0,T0 after dividing by 60; identity (3) coefficientwise; identity (4) | CONFIRMED | none |
| B U=0 forces T=Z=0 over arbitrary rings; both branches of (3) and their overlap; V=0/W=0 and V=1/3 exclusions; V=1/4 gives W=1/108; a0,u,a3,w,Z=5/54; R_c/(U)=0 with nilpotents; U unit | CONFIRMED | F1: 17zj finiteness is cited but not needed for the field point (any nonzero ring has a maximal ideal); documentary |
| C single quadratic pivot q=X^2+(T/U)X+Z/U, s=-T/U, p=Z/U; both equations (7); both directions and ring isomorphism after substituted G unit; h=q(X+u-T/U), a=(X+a3-u)h+Uq | CONFIRMED | none |
| D changed-object control dropping ONLY W: V=W=0, x=3,y=4, s=7,p=12, factorizations, U=T=Z=0, Delta=1, Gamma=256, Omega=128, all other G factors nonzero; Z=0 indispensable at (1/4,1/108); prescribed finite points GAP | CONFIRMED as scoped | none |

Overall: the new claim, U is a unit on the ENTIRE c-unit chart R_c=R[(3V-1)^-1] with nilpotents retained, stands on independent manual recomputation. It is a NEW result reviewed once by this gate; PROVISIONAL, no promotion, execution or follow-on authority.

## A. Literal numerators and the actual polynomials U0, T0

a-b from the accepted17zi coefficients: X^3: (30V-14)-(42V-18)=4-12V=c. X^2: 71-119=-48, -270+504=234, 180-420=-240, 120-210=-90, so d=-48+234V-240V^2-90W. X: -154+342=188, 780-1974=-1194, -900+2940=2040, 120-840=-720, -600+1470=870, 720-2520=-1800, so e=188-1194V+2040V^2-720V^3+(870-1800V)W. X^0: -240, 1800, -3960, 2280, -1800, 6120, -2520 (V^2W), -2160 (W^2): f as printed. So h=(a-b)/c=X^3+uX^2+vX+w with u=d/c, v=e/c, w=f/c. CONFIRMED.

g=d-c*a3: c*a3=(4-12V)(30V-14)=-56+288V-360V^2, so g=8-54V+120V^2-90W. CONFIRMED. Expansion (X+a3-u)h=X^4+a3X^3+[v+(a3-u)u]X^2+[w+(a3-u)v]X+(a3-u)w gives a-(X+a3-u)h=UX^2+TX+Z with U=a2-v-a3u+u^2, T=a1-w-a3v+uv, Z=a0+(u-a3)w. Multiplying by c^2: c^2U=c^2a2-ce-c a3 d+d^2=c^2a2-ce+d(d-c a3)=c^2a2-ce+dg; c^2T=c^2a1-cf-c a3 e+de=c^2a1-cf+eg; c^2Z=c^2a0+(d-c a3)f=c^2a0+fg. All three of (1) CONFIRMED.

Actual expansion of c^2U with c^2=16-96V+144V^2. c^2a2: 1136-11136V+39024V^2-56160V^3+25920V^4+(1920-11520V+17280V^2)W. ce: 752-7032V+22488V^2-27360V^3+8640V^4+(3480-17640V+21600V^2)W. dg: -384+4464V-20316V^2+41040V^3-28800V^4+(3600-16200V+10800V^2)W+8100W^2. Sum c^2a2-ce+dg: constant 1136-752-384=0; V: -11136+7032+4464=360; V^2: 39024-22488-20316=-3780; V^3: -56160+27360+41040=12240; V^4: 25920-8640-28800=-11520; W: (1920-3480+3600)+(-11520+17640-16200)V+(17280-21600+10800)V^2=2040-10080V+6480V^2; W^2: 8100. Dividing by 60: U0=6V-63V^2+204V^3-192V^4+(34-168V+108V^2)W+135W^2. The producer's form: 2(54V^2-84V+17)=108V^2-168V+34; 3V(1-4V)(16V^2-13V+2)=3V(-64V^3+68V^2-21V+2)=-192V^4+204V^3-63V^2+6V. U0 (2) CONFIRMED.

Actual expansion of c^2T. c^2a1: -2464+27264V-111456V^2+200640V^3-141120V^4+17280V^5+(-9600+69120V-155520V^2+103680V^3)W. cf: -960+10080V-37440V^2+56640V^3-27360V^4+(-7200+46080V-83520V^2+30240V^3)W+(-8640+25920V)W^2. eg: 1504-19704V+103356V^2-259200V^3+283680V^4-86400V^5+(-9960+46080V+18000V^2-151200V^3)W+(-78300+162000V)W^2. Sum c^2a1-cf+eg: constant 0; V: 27264-10080-19704=-2520; V^2: -111456+37440+103356=29340; V^3: 200640-56640-259200=-115200; V^4: -141120+27360+283680=169920; V^5: 17280-86400=-69120; W: (-9600+7200-9960)+(69120-46080+46080)V+(-155520+83520+18000)V^2+(103680-30240-151200)V^3=-12360+69120V-54000V^2-77760V^3; W^2: (8640-25920V)+(-78300+162000V)=-69660+136080V. Dividing by 60: T0=-42V+489V^2-1920V^3+2832V^4-1152V^5+(-206+1152V-900V^2-1296V^3)W+(-1161+2268V)W^2. Producer: 27(84V-43)=2268V-1161; 3V(1-4V)(96V^3-212V^2+107V-14)=3V(-384V^4+944V^3-640V^2+163V-14)=-1152V^5+2832V^4-1920V^3+489V^2-42V. T0 (2) CONFIRMED; every numerator coefficient is divisible by 60, so 60 is the correct rational unit.

Identity (3). W^2: 135(84V-43)-135(84V-43)=0, exact cancellation. W: 5(-206+1152V-900V^2-1296V^3)-(84V-43)(34-168V+108V^2)=(-1030+5760V-4500V^2-6480V^3)-(-1462+10080V-18756V^2+9072V^3)=432-4320V+14256V^2-15552V^3=432(1-10V+33V^2-36V^3), and (1-4V)(1-3V)^2=(1-4V)(1-6V+9V^2)=1-10V+33V^2-36V^3; right side W coefficient 48*9=432 times the same. W^0: 3V(1-4V)[5(96V^3-212V^2+107V-14)-(84V-43)(16V^2-13V+2)]=3V(1-4V)[(480V^3-1060V^2+535V-70)-(1344V^3-1780V^2+727V-86)]=3V(1-4V)(-864V^3+720V^2-192V+16)=48V(1-4V)(1-12V+45V^2-54V^3), and (1-3V)^2(1-6V)=1-12V+45V^2-54V^3. (3) CONFIRMED coefficientwise.

Identity (4). With W=(6V^2-V)/9: 135W^2=(5/3)(36V^4-12V^3+V^2)=60V^4-20V^3+(5/3)V^2; (108V^2-168V+34)W=(648V^4-1116V^3+372V^2-34V)/9=72V^4-124V^3+(124/3)V^2-(34/9)V; plus -192V^4+204V^3-63V^2+6V. V^4: 60+72-192=-60; V^3: -20-124+204=60; V^2: 5/3+124/3-63=-20; V: -34/9+54/9=20/9. Total (20/9)V(1-9V+27V^2-27V^3)=(20/9)V(1-3V)^3. (4) CONFIRMED. A CONFIRMED.

## B. The U=0 divisor is empty: every branch, arbitrary rings, nilpotents

Chart: R_c=R[c^-1] with R=Q[s,p,V,W,G^-1]/(F) as in accepted17zi; c=4(1-3V), so c unit <=> 3V-1 unit; every G factor, including W, stays inverted. In R_c[X]: q|a and q|b (the four rows), c a unit gives q|h, hence q|a-(X+a3-u)h=UX^2+TX+Z. Write UX^2+TX+Z=q*m. Over ANY ring, q monic of degree 2 times m of degree k with nonzero leading coefficient has degree exactly k+2 with that leading coefficient, so m is the constant U and q*U=UX^2-sUX+pU. Hence the exact ring identities T=-sU and Z=pU hold in R_c with nilpotents; modulo U they give T=Z=0. This is slightly stronger than the producer's "monicity and degree force T=Z=0" and contains it. CONFIRMED.

Field points of R_c/(U): a ring map to a field K containing Q. There c, 1-3V, W, 48, 60, 9 are nonzero in K; U=0 gives T=0 (from T=-sU) and Z=0 (from Z=pU); U0=c^2U/60=0 and T0=0. Identity (3) in K: 48(1-4V)(1-3V)^2[9W+V(1-6V)]=0, so (1-4V)=0 or 9W+V(1-6V)=0, K being a field. Branch 1, 9W+V(1-6V)=0 with V arbitrary: (4) gives (20/9)V(1-3V)^3=0, so V=0 (V=1/3 is off the chart); then W=0, contradicting the inverted W factor. Branch 2, V=1/4 with W arbitrary: U0=135W^2+2(54/16-21+17)W+0=135W^2-(5/4)W=(5/4)W(108W-1); W nonzero forces W=1/108. Overlap of the branches (V=1/4 and W=1/72) is covered by branch 2 and is inconsistent with W=1/108 anyway; the two branches exhaust the disjunction. At (1/4,1/108): c=1; a3=15/2-14=-13/2; d=-48+117/2-15-5/6=-16/3=u; f: constant part -240+450-495/2+285/8=-15/8, W part -1800+1530-315/2=-855/2, W^2 part -2160, so w=-15/8-95/24-5/27=(-405-855-40)/216=-325/54; a0: constant part 120-180+135/2-15/4=15/4, W part (720-360)/108=10/3, W^2 part 360/11664=5/162, so a0=(1215+1080+10)/324=2305/324; u-a3=-32/6+39/6=7/6; Z=2305/324-(7*325)/324=(2305-2275)/324=30/324=5/54, nonzero. This contradicts Z=0. Row (5) CONFIRMED digit by digit. Also T0 vanishes there automatically by (3) (both right-side factor 1-4V and the U0 term are zero), so U=T=0 alone would NOT kill this point; the retained row Z=0 is indispensable, as the producer says.

Zero ring: no field point exists. If R_c/(U) were nonzero it would have a maximal ideal; its residue field is a field containing Q, and the quotient map is a field point of the excluded kind. So R_c/(U)=0, i.e. (U)=R_c, U is a unit in R_c with nilpotents retained. No reality or rationality of V,W was used; the argument is over an arbitrary field K of characteristic 0. Only the c chart and the W factor were consumed; no further divisor was inverted; the c=0 slice is the separate accepted17zi three/six-point slice and is not a domain of U. Finiteness (accepted17zj) is stronger than needed here: existence of a maximal ideal needs only that the ring is nonzero, and the field point argument needs only a field over Q. Citing it does not invalidate the proof (F1, documentary). B CONFIRMED.

## C. The licensed single quadratic pivot and its two equations

With U a unit, UX^2+TX+Z=U*(X^2+(T/U)X+Z/U) and, by B, equals U*q, so q=X^2+(T/U)X+Z/U, s=-T/U, p=Z/U in R_c. Division of h by q, over any ring: (X^2-sX+p)(X+u+s)=X^3+uX^2+(p-su-s^2)X+p(u+s), so rem_q(h)=[s^2-p+us+v]X+[w-p(s+u)] (matching the accepted17zj gate's section F). Substituting s=-T/U, p=Z/U and multiplying by the unit U^2: first coefficient becomes T^2-UZ-uUT+vU^2, i.e. UZ-T^2+uUT-vU^2=0; second becomes wU^2+TZ-uUZ, i.e. uUZ-TZ-wU^2=0. Both equations (7) CONFIRMED exactly, and q|h <=> (7) since U^2 is a unit. The cofactor is X+u+s=X+u-T/U, so h=q(X+u-T/U). CONFIRMED.

Both directions. In R_c: s=-T/U, p=Z/U hold as identities (B), and (7) holds because q|h. Conversely, in the ring S=Q[V,W][c^-1,U0^-1,Gsub^-1]/(7), where Gsub is G with s=-T/U, p=Z/U substituted: (7) gives q|h, hence a=(X+a3-u)h+Uq is divisible by q and b=a-ch likewise, so all four symmetric rows vanish at (s,p)=(-T/U,Z/U); G maps to the inverted Gsub. The map R_c -> S (s,p to -T/U, Z/U) and the map S -> R_c (V,W to V,W) are mutually inverse because s=-T/U and p=Z/U already hold in R_c. Ring isomorphism R_c ~= S CONFIRMED, nilpotents retained. No elimination of (7), no count, no rational point, no source conclusion is claimed by the producer or established here; the new content is the explicit closure of the U divisor, (2)-(6). C CONFIRMED.

## D. Changed-object control and scope

Drop ONLY the W factor from G and take V=W=0. Then a=(X-2)(X-3)(X-4)(X-5), b=(X-3)(X-4)(X-5)(X-6) (accepted17zi scalar factors), c=4, a-b=(X-3)(X-4)(X-5)[(X-2)-(X-6)]=4(X-3)(X-4)(X-5), h=(X-3)(X-4)(X-5)=X^3-12X^2+47X-60, u=-12, a3=-14, a3-u=-2, a=(X-2)h exactly, so U=T=Z=0. q=(X-3)(X-4)=X^2-7X+12, s=7, p=12, divides both quartics. Guard values: p=12, p-s+1=6, 9p-15s+25=28, p-2s+4=2, Delta=49-48=1, s-3=4, 4-s=-3, Gamma=432+441-798+181=256, Omega=735-432-210+35=128, all nonzero; x=3,y=4 are not 0,1,5/3,2 and s is not 3 or 4. So the unit statement cannot extend over W=0, and W is load-bearing exactly as claimed; the producer correctly says this is not a point of the actual guarded problem. CONFIRMED. The second control, Z=0 at (1/4,1/108), was recomputed in B: U=T=0 there, Z=5/54. CONFIRMED.

Scope as the producer states and this gate confirms: the U=0 divisor on the c-unit chart is empty, licensing the global pivot; the prescribed rational-exponent exclusion, enumeration of the finite guarded points, all-r source implication and JC2 closure remain GAP, untouched. The abandoned 7-adic residue route is not a premise. No execution authority and no review farm.

## E. Smallest actual defects

F1 (documentary, B). Section 3 says accepted17zj finiteness supplies the maximal ideal and field point; any nonzero ring has a maximal ideal, and the field-point exclusion only needs a field over Q. The proof does not depend on 17zj, which only strengthens the context. Content unaffected.
F2 (documentary, B). "Monicity and degree force T=Z=0" is true; the sharper exact identities T=-sU, Z=pU in R_c are what the pivot in section 4 actually uses. Content unaffected.
No mathematical defect was found in A-D.

## OPENS RAISED

- NONE new. The assigned GAP stays as the producer recorded it, no new canonical ID: QUANTITY the set of guarded generic finite points at the prescribed rational exponents is > 0 or = 0, presently undetermined; the U-unit pivot and equations (7) may be consumed once Root accepts this gate, but no elimination of (7) is authorized here.

## COLLISIONS

status: EMPTY

- NONE — own-only check: xmodel/f10-contact-global-pivot-gate-fable5-20260910.md and box/f10-contact-global-pivot-gate-fable5-20260910/ were ABSENT at 02:34:30 UTC before the skeleton; no corpus, ledger, provenance, Git, live-file or other-lane scan performed.

Own WHOLE reread (68 lines, 13134 bytes before this completion edit, marker count 1) and own-only raised-OPEN/collision extraction done at 02:36:22 UTC, before the 02:40:30 publication reserve; the six box hash rows were cross-checked against the generated input hashes. This completion edit adds this sentence only. Written: this report and box/f10-contact-global-pivot-gate-fable5-20260910/READ-SCOPE.md, documentary writes only. No mathematical subprocess of any size, code, coefficient artifact, network, AWS, SSH, process inspection, agent, Git/shared/protected work or other-lane read occurred. Root retains custody and any further review; this gate gives no promotion, execution or follow-on authority.

<!-- BODY-END -->
