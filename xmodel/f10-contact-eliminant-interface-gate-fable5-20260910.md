# FIRST gate: whole finite-contact eliminant interface, exact four-generator presentation (producer f10-contact-eliminant-interface-astra-20260910)

2026-09-10. Gate lane fable5. First action 03:49:25 UTC; fixed stop 04:03:25 UTC (first+14 min, earlier than 04:04:00); publication reserve from 04:01:25 UTC. Charged inputs: the nine ordered SHA256 pins of the lane brief, all nine verified byte-identical in /tmp/jc2-lane.MLUpzm/inputs at 03:49:25 before any body read (c1ec52ca producer 13710 B; 4049d133 ROOT-CARD 5438 B; c18309e4 accepted17zn producer 8126 B; 504fa198 accepted17zn gate 13451 B; 96deb541 accepted17zi producer 10488 B; f4f51690 accepted17zi gate 11573 B; 54e6c2b2 accepted17zj gate 14371 B; 4bbecd35 accepted17w producer 18506 B; 4a46e7f6 accepted17w gate 12680 B). All nine read WHOLE via parallel reads; no clipping. The accepted17zj producer (521ec17b, listed on the ROOT-CARD) is NOT a charged input; its result dim_Q M < infinity is consumed only through its accepted gate 54e6c2b2. Premises: accepted17zi (literal quartics, four remainder rows, whole ten-factor G, rank-two cover, closed V=1/3 slice), accepted17zj gate (unguarded dim_Q M finite), accepted17zn (c^2 numerator identities, U unit on R[c^-1], its equations (7)), accepted17w (5/3<x<y<2, Gamma>0, Omega>0, u-normalization as a field-point fact). The single-client packet and older unreviewed dimension reports are not inputs. ZERO mathematical subprocesses; every identity below was recomputed by hand. No Seal, no charge_basis.

## 0. Verdict table

| Item | Verdict | Smallest actual defect |
|---|---|---|
| A literal a3..a0, c,d,e,f,g; A,B,C = c^2U, c^2T, c^2Z; I1,I2 = c^5 times the 17zn rows (denominators c^4/c^5); I3 = A*q; I4 localization; N = D both directions with nilpotents; P/I = N[X]/(X^2-sX+p) free rank two, involution, not etale, not the two-evaluation ring; finite without G, zero ring allowed | CONFIRMED | F1 (documentary): (3) cited as "coefficient multiplication" without the remainder forms of U,T,Z; closed in A |
| B P/I -> R[c^-1][X]/(q) via the 17zn A-unit; N[G^-1] = R[c^-1]; guarded c=0 slice = six 17zi points, none prescribed; every prescribed (r,j) contact satisfies every G factor and c!=0; normalization limits retained; no source closure | CONFIRMED | none |
| C (9) existence by Cayley-Hamilton or F=1; I cap S0 = J:t^infinity; conversion (11) exact including N0=0; V=W=0 control A=B=C=0, spurious X-line, three true quadratics | CONFIRMED | none |
| D F(x)=F(y)=0 by the involution; 3n-5m=1; 3r+1 divides a_D; finite divisor list; interval (5/3,12/7]; one-distinct-root criterion; (X-2) removal pointwise only; K(R) nonzero, K(0)=P1(2), r divides P1(2); constants, repeated roots; survivor pair not a contact | CONFIRMED | F2 (documentary): numerator half n divides a_0 is a free unused filter |

Overall: the four-generator presentation, both ring maps, the finiteness argument, the certificate contract and the rational-root interface stand on independent manual recomputation. NEW theorem/interface reviewed once by this gate; PROVISIONAL. No explicit F, coefficient, root list, exclusion, source implication, promotion, execution or follow-on authority.

## A. Literal ideal, powers and signs, both maps, cover, finiteness

Literal check. a3..a0 are byte-for-byte accepted17zi section 2. c=4-12V and d,e,f,g are byte-for-byte accepted17zn section 2 (c*a3=-56+288V-360V^2, so g=d-c*a3=8-54V+120V^2-90W). A,B,C are exactly the accepted17zn numerators c^2U=c^2a2-ce+dg, c^2T=c^2a1-cf+eg, c^2Z=c^2a0+fg. CONFIRMED.

Identity (3), closing F1: U=A/c^2=a2-e/c+d(d-ca3)/c^2=a2-v-a3u+u^2, T=a1-w-a3v+uv, Z=a0+(u-a3)w; (Y+a3-u)(Y^3+uY^2+vY+w)=Y^4+a3Y^3+(v+a3u-u^2)Y^2+(w+a3v-uv)Y+(a3-u)w, and a minus this is UY^2+TY+Z. CONFIRMED.

Powers and signs. Rows (5) are accepted17zn (7). With U=A/c^2, T=B/c^2, Z=C/c^2, u=d/c, v=e/c, w=f/c: UZ=AC/c^4, T^2=B^2/c^4, uUT=dAB/c^5, vU^2=eA^2/c^5; times c^5 gives cAC-cB^2+dAB-eA^2=I1. uUZ=dAC/c^5, TZ=BC/c^4, wU^2=fA^2/c^5; times c^5 gives dAC-cBC-fA^2=I2. Denominators c^4 on the u,v,w-free terms and c^5 on the rest, exactly as displayed. I3: A(Y^2+(B/A)Y+C/A)=AY^2+BY+C with s=-B/A, p=C/A. I4=zt-1, t=cA. CONFIRMED.

Units. If xy is a unit then x and y are units (x*(y*(xy)^-1)=1); so c, A and U=A/c^2 are units in N and in D. CONFIRMED.

D -> N. In N=M[t^-1]: rows (2) give q|a and q|b; c a unit gives q|h; by (3), q|UY^2+TY+Z=q*m. Over any ring, q monic of degree 2 gives deg(qm)=2+deg m with the leading coefficient of m, so m is a constant, m=U, and T=-sU, Z=pU exactly (the 17zn gate's identities); U a unit gives s=-B/A, p=C/A, i.e. (4). rem_q(h)=[s^2-p+us+v]Y+[w-p(s+u)] (17zj gate F, 17zn gate C). Multiplying by the unit U^2 and substituting (4): U^2(s^2-p+us+v)=T^2-UZ-uUT+vU^2 and U^2(w-p(s+u))=wU^2+TZ-uUZ; q|h therefore gives both rows (5), and c^5 times them gives I1=I2=0 in N. t^-1 exists in N. So V,W,z -> V,W,t^-1 is a ring map D -> N. CONFIRMED.

N -> D. In D, c, A, U are units; I1=I2=0 with c^5 a unit gives (5); U^2 a unit gives rem_q(h)=0 for q=Y^2+(B/A)Y+C/A, i.e. h=q(Y+u+s)=q(Y+u-T/U); then a=(Y+a3-u)h+Uq is divisible by q and b=a-ch likewise, so all four rows (2) vanish at s=-B/A, p=C/A: this is (6). t^-1 -> t^-1. Composites: D->N->D fixes V,W,t^-1, the identity; N->D->N sends s to -B/A=s and p to C/A=p by (4), the identity. N=D as rings, nilpotents retained. CONFIRMED.

Cover. Q[z,V,W]/(I1,I2,I4)=Q[V,W,t^-1]/(I1,I2)=D with z=t^-1. In D[X], (I3)=(A(X^2-sX+p))=(X^2-sX+p) because A is a unit. So P/I=D[X]/(X^2-sX+p)=N[X]/(X^2-sX+p), free with basis 1,X (N -> P/I injective without any discriminant), and X -> s-X preserves X^2-sX+p since (s-X)^2-s(s-X)+p=X^2-sX+p. Etale would need (2X-s)^2=s^2-4p invertible; it is not inverted and is correctly not claimed. The naive ordered ring Q[x,y,V,W]/(a(x),a(y),b(x),b(y)) differs at x=y (one evaluation does not force (Y-x)^2|a); the base here is (2), as the producer says. Variable names: the producer's Y is the formal variable of a,b,q,h in N[Y]; X is the class in P/I; (7) is evaluation Y -> X, and s,p in N correspond to -B/A, C/A in D. CONFIRMED.

Finiteness. dim_Q M finite (17zj gate, unlocalized M). M is Artinian, a product of local Artinian rings, in each of which t is a unit or nilpotent; M[t^-1] is the product of the factors where t is a unit, finite-dimensional, zero if t is nilpotent everywhere. P/I is free of rank two over N, so dim_Q P/I=2dim_Q N, finite, possibly zero. No G was used. t is NOT a unit on M: at V=W=0, t=cA=0 (section C) while M has three field points there; the producer correctly makes no such assertion. A CONFIRMED.

## B. Guarded chart direction, c=0 slice, prescribed points

R=M[G^-1] with the literal ten-factor G of accepted17zi; R_c=R[c^-1]=R[(3V-1)^-1] since c=4(1-3V). Accepted17zn: U is a unit in R_c, so A=c^2U and t=cA are units there, and M -> R_c factors through N=M[t^-1] by the universal property. N[G^-1]=M[(tG)^-1]=R[t^-1]=R_c[A^-1]=R_c. Hence (8), P/I=N[X]/(q) -> R_c[X]/(q), is exactly localization of (7) at G, and every field point of the guarded ordered c-unit chart composes to a field point of P/I. Spec(P/I) may contain G=0 or W=0 points; no prescribed point is lost, and A=0 carries no guarded c-unit point. CONFIRMED.

c=0 slice. c=0 iff V=1/3; accepted17zi: W=1/27 forced, quartic (Y-1/3)(Y-2/3)(Y-4/3)(Y-5/3), six ordered guarded points with x,y in {1/3,2/3,4/3}, all below 5/3. Prescribed x=(5r+2)/(3r+1)>5/3, so no prescribed contact is a guarded c=0 point. The statement concerns the guarded slice only; unguarded c=0 points (for example with W=0) are not claimed excluded. CONFIRMED.

Prescribed points satisfy G. For r>=2, m=3r+1, n=5r+2, 1<=j<=r-1: x=5/3+1/(3m), y=(n+j)/m<=(6r+1)/m<2, d=y-x=j/m>0, 10/3<s<4. Hence W!=0 (cubic), p=xy!=0, (x-1)(y-1)!=0, (3x-5)(3y-5)!=0, (2-x)(2-y)!=0, Delta=d^2!=0, s-3!=0, 4-s!=0, Gamma>0 (17w (13)), Omega>0 (17w (27)); x(x-1)(x-2)!=0 makes A_x,B_x equivalent to the contact rows. The u-normalization is the accepted16l/17w field-point fact (u!=0 at the exponent x) or the explicit u-unit chart and stays a premise; no reality or rationality of V,W is used or inferred from real x,y. So each prescribed field contact is a field point of C[c^-1] and, via (8), of P/I with X=x (and X=y after the swap). No affine source, companion or JC2 closure follows, as the producer states. B CONFIRMED.

## C. Certificate contract and saturation control

(9). P/I is finite-dimensional over Q. If nonzero, multiplication by X is a Q-linear operator with a monic nonzero characteristic polynomial chi; Cayley-Hamilton gives chi(X)=0 in P/I, i.e. chi(X) in I, so chi(X)=sum Hi*Ii for some Hi in P: an explicit instance of (9) exists. If P/I=0 then 1 in I and F=1. Only existence: no degree, dimension, matrix, coefficient or root is asserted, and a name, header, float or uncomputed Groebner claim is not (9). CONFIRMED.

(10)-(11). P/I=S0[z]/(J,zt-1)=(S0/J)[t^-1] with t=cA in S0, so the kernel of S0 -> P/I is J:t^infinity=I cap S0 (saturation, not radical). Given t^N0 F=K1I1+K2I2+K3I3: z^N0 sum Ki Ii=(zt)^N0 F and (zt-1) sum_{k<N0}(zt)^k=(zt)^N0-1, so the right side of (11) equals (zt)^N0 F-((zt)^N0-1)F=F; H_i=z^N0 K_i for i<=3 and H_4=-F sum_{k<N0}(zt)^k, all in P; N0=0 gives the empty sum and F=sum Ki Ii. CONFIRMED.

Control. At V=W=0: c=4, d=-48, e=188, f=-240, g=8; A=16*71-4*188-48*8=1136-752-384=0; B=16*(-154)+4*240+188*8=-2464+960+1504=0; C=16*120-240*8=0. So I1=I2=I3 vanish identically on (V,W)=(0,0) with X free (and z free if retained): J=(I1,I2,I3) has a positive-dimensional component and no nonzero member of Q[X], since such an F would vanish at every X. The unguarded M at V=W=0: a=(Y-2)(Y-3)(Y-4)(Y-5), b=(Y-3)(Y-4)(Y-5)(Y-6), gcd=(Y-3)(Y-4)(Y-5) squarefree, exactly three monic quadratics over a field, finite as 17zj requires. t=0 there, so N and P/I omit these W=0 points; I4 removes the spurious line, and 17zn guarantees t!=0 on the guarded c-unit chart, so nothing prescribed is removed. CONFIRMED.

## D. Both exponents, integer filters, interval, Möbius filter

F(x)=F(y)=0. A prescribed contact is a field point of P/I with X=x; composing with the involution X -> s-X, an N-algebra automorphism of P/I, gives a field point with X=y. Both are roots of the one certified F. CONFIRMED.

Divisor filter. 3n-5m=3(5r+2)-5(3r+1)=1, so gcd(n,m)=1. m^D P0(n/m)=a_D n^D+m(...)=0 gives m|a_D n^D, hence m=3r+1 divides a_D (D>0, a_D!=0): (12). Candidates r=(m-1)/3 for the divisors m>=7, m=1 mod 3, of |a_D|, then exact substitution at x=(5m+1)/(3m) (n=(5m+1)/3). |a_D|<7, or no such divisor, excludes every r. D=0: a nonzero constant in I means P/I=0 and no field point at all. CONFIRMED. F2: n divides a_0 when a_0!=0 is a further filter the producer does not use; an omission, not a defect.

Interval. x=5/3+1/(3(3r+1)) is decreasing with x=12/7 at r=2: x in (5/3,12/7]. y=(n+j)/m<(6r+2)/m=2 and y>x. Both are distinct roots of P0 in (5/3,2), so at most one distinct real root there excludes every prescribed pair, and no real root in (5/3,12/7] excludes every first exponent. Repeated roots do not matter; distinct roots are what is counted. CONFIRMED.

Möbius. Removing (X-2) factors: if P0(x)=0 with x!=2 then P1(x)=0; ideal membership is not preserved and not claimed. K(R)=(3R+1)^d1 P1((5R+2)/(3R+1)) lies in Z[R], each a_i X^i becoming a_i(5R+2)^i(3R+1)^(d1-i). Nonzero: X=(5R+2)/(3R+1) is a Möbius map with inverse R=(2-X)/(3X-5), an automorphism of Q(X), so P1!=0 gives K!=0. K(0)=P1(2)!=0. If P1(x_r)=0 then K(r)=0, K=(R-r)K' with K' in Z[R] (division by a monic), K(0)=-rK'(0), so r divides P1(2); |P1(2)|=1 excludes all r>=2; constant P1 has no root and excludes all. CONFIRMED.

Limits. A surviving pair of roots of F is only necessary: it need not share V,W, satisfy G, or satisfy the affine/source equations; no polynomial, root list or exclusion exists; source and JC2 remain outside. Correct as stated. D CONFIRMED.

## E. Smallest actual defects

F1 (documentary, A). Identity (3) is introduced as "follows by coefficient multiplication" with U=A/c^2 etc., without displaying the remainder forms U=a2-v-a3u+u^2, T=a1-w-a3v+uv, Z=a0+(u-a3)w that make it a one-line check; recomputed in A. Content unaffected.
F2 (documentary, D). The numerator half of the rational-root theorem, n=5r+2 divides a_0 when a_0!=0, is a free additional filter the producer does not mention. Content unaffected.
No mathematical defect was found in A-D.

## OPENS RAISED

- NONE new. The assigned GAP stays as the producer recorded it, no new canonical ID: QUANTITY the number of explicit certified univariate eliminants F with (9) or (10) supplied is = 0 (existence is proved, 0 <= dim_Q P/I < infinity); the prescribed-root classification and any source/affine/JC2 implication remain undetermined; no computation is authorized here.

## COLLISIONS

status: EMPTY

- NONE — own-only check: xmodel/f10-contact-eliminant-interface-gate-fable5-20260910.md and box/f10-contact-eliminant-interface-gate-fable5-20260910/ were ABSENT at 03:49:25 UTC before the skeleton; no corpus, ledger, provenance, Git, live-file or other-lane scan performed.

Own WHOLE reread and own-only raised-OPEN/collision extraction done before the 04:01:25 publication reserve; the box hash rows are generated from sha256sum output and cross-checked against the lane brief pins. Written: this report and box/f10-contact-eliminant-interface-gate-fable5-20260910/READ-SCOPE.md, documentary writes only. No mathematical subprocess of any size, code, coefficient artifact, network, AWS, SSH, process inspection, agent, Git/shared/protected work or other-lane read occurred. Root retains custody and any further review; this gate gives no promotion, execution or follow-on authority.

<!-- BODY-END -->
