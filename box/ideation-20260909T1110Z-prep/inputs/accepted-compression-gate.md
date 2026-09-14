# Independent hostile gate: F10 actual-source cubic/quintic compression (Fable 5.1)

tag=f10-source-polynomial-compression-gate-fable5-20260909
frozen_basis=0d39df3c9fd69c939a8420c54d03228b9077777d (provenance only)
reviewer=Claude Fable 5.1 (claude-fable-5-1)
launch=root actual invitation; lane clock opened 10:41:45 UTC; hard stop = earlier of 11:06:45 UTC (25 min after invitation) and 11:06 UTC, i.e. 11:06 UTC, no reset
subprocesses=ZERO mathematical subprocesses. Only date, ls, mkdir, sha256sum, cat/heredoc and grep were run. All algebra below is hand-derived factored prose.

## 0. Custody and read scope

All FIVE charged files under /tmp/jc2-lane.QtZsWe/inputs were pinned (sha256sum, recorded in box/.../PINS.sha256) BEFORE their WHOLE reads, and the five hashes match the invitation's ordered pins exactly: 9b77ece0... (producer body), 03143a58... (artifact json: body_bytes 15867, body_sha256 051b0ed1..., full_sha256 9b77ece0..., closed 10:36:04Z, consistent with the producer's own seal block), e87e5133... (coalesced reference, ACCEPTED at stated scope), cc6edcb7... (16k source interface, ACCEPTED), 9dc342bd... (accepted 16k source gate). No provenance path, peer/live gate, mutable canonical body, log or receipt was opened. The producer is treated as NEW/UNREVIEWED; the two parents are consumed as premises at their literal stated scope and their imported primaries (16l coalesced contact orders, GGV/GGHV interiors) are NOT re-audited.

Identical-object check (required by the invitation). The producer's A,B are the coordinator's increasing-exponent receivers after output swap: r=q+1, m=3r+1=3q+4, n=5r+2=5q+7. Its A_s=s^{7m}A(g/s^2,p/s) equals the coordinator's A'_s=s^{7m}A'(p/s,z/s^2) because z(g/s^2,p/s)=z_s/s^2. Its (11) is the coordinator's coalesced (2) homogenized with z_s=Z_s+(a2 s p+a1 s^2)/3, so ell=a2/3, h=a1/3. Its bound (2) is the coordinator's (7) with r0=r. Its faces p C(T), p^2 z D(T), T=p^r z^m, and the ODE nTC'D-mTCD'-CD=-c are the coordinator's section 5 initials. Contact orders: remainder j0=7q+9>7 and scalar corrections gamma_h s^{7(m-h)}, h<=m-2, hence order >=14, are the coordinator's section 1/2 statements. Every parent conclusion is applied to the same object it was proved for.

## 1. Target A: actual canonical source. CONFIRMED.

Rederived from the 16k interface, section 6. Composite from the unshifted source: u=g0^3 p0+lambda g0^2-r0, v=g0^{-1}, determinant +g0. Normalization g0=kappa g, p0=mu p with mu^3=a0 lambda, kappa=lambda/mu, so kappa mu=lambda, and lambda kappa^2=kappa^3 mu. Hence u=kappa^3 mu(g^3 p+g^2)-r0, v=kappa^{-1}g^{-1}: the producer's two displayed lines are exact. With U=(u+r0)/(kappa^3 mu)=g^2(1+gp) and V=kappa v=g^{-1}, the normalized receiver is A(g,p)=P0(kappa^3 mu U-r0, kappa^{-1}V)/(alpha mu^{7e}), an ordinary polynomial P(U,V) with coefficients in k(mu), the same finite extension 16k already licensed; the output swap only exchanges which of P0,Q0 feeds A and B and negates the scalar, absorbed into c. So (7) is an identity between actually supplied polynomials, not a claim for arbitrary receivers.

Determinant: U_g=2g+3g^2p, U_p=g^3, V_g=-g^{-2}, V_p=0, so U_gV_p-U_pV_g=+g. Hence [A,B]_(g,p)=[P,Q]_(U,V)*g and [P,Q]_(U,V)=c with the increasing order fixed; sign and order are consistent with 16k's +g composite determinant times the normalization scalar kappa mu absorbed in c. Inverse: g=V^{-1}; U=g^2+g^3p gives p=(U-g^2)/g^3=V^3U-V. Exact.

Homogeneous inverse (9): g'=g/s^2=(s^2V)^{-1}, p'=p/s=V^3U/s-s^2V. Then g'^2(1+g'p')=s^{-4}V^{-2}(1+s^{-3}V^2U-1)=U/s^7 and g'^{-1}=s^2V. So A_s|_(9)=s^{7m}P(U/s^7,s^2V) as rational functions. Polynomiality: A_s is in k[g,p,s] because 2I+J<=7m on the receiver support (accepted 16k), and substituting g=V^{-1}, p=V(V^2U-s^3) lands in k[U,V^{+-1},s] with no negative s power; the right side is visibly in k[U,V,s^{+-1}]. A Laurent monomial U^aV^bs^c lying in both rings has b>=0 and c>=0, so the common element is in k[U,V,s]. No degree bound on P is assumed; the bound 7a-2b<=7m on supp P is a consequence, not a premise. CONFIRMED.

## 2. Target B: canonical R pole and u=-h. CONFIRMED.

Under (9), z_s=(V^3U-s^3V)^2-V^{-1}+ell s(V^3U-s^3V)+hs^2=-V^{-1}+E_s with E_s polynomial, E_s=e0+e1V+e2V^2+..., e0=hs^2, e1=-ell s^4, e2=s^6, e3=ell sU, e4=-2s^3U, e6=U^2. Also p=p1V+p3V^3, p1=-s^3, p3=U, V-order exactly one. With w=-V^{-1}+E_s:
w^3 = -V^{-3} + 3e0 V^{-2} + (3e1-3e0^2) V^{-1} + (polynomial);
w^2 = V^{-2} - 2e0 V^{-1} + (polynomial).
Negative-V parts: p w^3 gives p1V(-V^{-3})+p1V(3e0V^{-2})=s^3V^{-2}-3hs^5V^{-1} (the p3V^3 term and the V^{-1} row of w^3 land at V^0 or higher); -s^3w^2 gives -s^3V^{-2}+2hs^5V^{-1}; us^5w gives -us^5V^{-1}; v0s^7 none. The V^{-2} terms cancel exactly and the total negative part is -(u+h)s^5V^{-1}: (12) is exact. There is no other pole: every negative V power must come from the displayed V^{-1} of z_s, the most singular product is p w^3 at V^{-2}, and the V-adic expansion above enumerates all such rows; positive V powers of E_s only raise V-order.

s=0 face: p=V^3U, z_0=V^6U^2-V^{-1}, R_0=V^3U*V^{-3}(U^2V^7-1)^3=U(U^2V^7-1)^3, and R_0(U,0)=-U. (13) exact.

Forcing u=-h. Accepted parent: A_s=f_s(R_s)+F with scalar corrections of s-order >=14 and ord_s F=7q+9>=9 in k[g,p,s] (F is even in a because A_s and f_s(R_s) are). Substitution (9) sends each s^iF_i(g,p) to s^i times an element of k[U,V^{+-1},s], so it never lowers s-order; thus [s^5](A_s|_(9))=[s^5]((R_s|_(9))^m). Write R_s|_(9)=Rpoly-(u+h)s^5V^{-1}, Rpoly=R_0+sR_1+.... The only way to reach s^5 with the pole is one pole factor times m-1 copies of R_0, so the V^{-1} coefficient of [s^5] is -m(u+h)R_0(U,0)^{m-1}=-m(u+h)(-U)^{m-1}; all other contributions are polynomial. By Target A, [s^5](A_s|_(9)) is a polynomial in U,V, so this residue is zero; m!=0 in characteristic zero and U^{m-1}!=0 force u+h=0. No later remainder or scalar term can cancel it: both start above order 5 and substitution cannot bring them down. With u=-h, (12) is polynomial for EVERY s, so R_source(U,V)=R(V^{-1},V^3U-V) is an ordinary polynomial, the whole R and not a jet. CONFIRMED.

## 3. Target C: whole compression to k[R,t]. CONFIRMED.

Inverse on z!=0: p=(R+z^2-uz-v0)/z^3=t-ut^2+St^3=Pi, S=R-v0. A monomial p^iz^j becomes Pi^it^{-j}, t-degree range i-j..3i-j, top coefficient S^i for i>=1.
A: (3r+1)i-rj<=3r+1, i.e. r(3i-j)+i<=3r+1. For i>=1 this gives 3i-j<=3; for i=0 the degree is -j<=0. B: r(3i-j)+i<=5r+2 gives 3i-j<=5 for i>=2 and <=3 for i<=1. Bounds 3 and 5 hold before any cancellation.
Unique slots: 3i-j=3 with i<=1 and j=3i-3>=0 forces (1,0); 3i-j=5 with i<=2 and j=3i-5>=0 forces (2,1). The monomials p and p^2z have weights m and 2m-r=n, the maxima, so their coefficients are the constant terms C0,D0 of the parent faces. The ODE at T=0 reads -C(0)D(0)=-c, so C0D0=c!=0. Hence [t^3]Ahat=C0S, [t^5]Bhat=D0S^2, nonzero polynomials: exact t-degrees 3 and 5.
Coordinates: z=p^2-g+ell p+h with h=-u gives g=Pi^2+ell Pi-u-t^{-1}=-Delta/t, V=-t/Delta, U=g^2(1+gp)=(Delta^2/t^2)(1-Delta Pi/t). Delta Pi/t=(1+ut-ell tPi-tPi^2)(1-ut+St^2): constant term 1, linear coefficient -u+u=0 because Pi has t-order 1 so the other two factors start at t^2 and t^3. So 1-Delta Pi/t=-t^2W with W in k[R,t] and U=-Delta^2W is an ordinary polynomial; Delta(R,0)=1 identically.
Intersection: A=P(U,V) lies in k[R,t,Delta^{-1}]; A'(Pi,t^{-1}) lies in k[R,t,t^{-1}]. If f=b/t^M with M>=1 minimal and f=a/Delta^N, then at^M=bDelta^N; t is prime in the UFD k[R,t] and t does not divide Delta (residue 1 mod t), so t divides b, contradicting minimality. So the intersection is k[R,t]. This is a statement in the polynomial ring, hence along the ENTIRE divisor t=0, and it uses the actual P,Q: without (7) a receiver polynomial such as z=t^{-1} survives. CONFIRMED.

## 4. Target D: exact target, sign, and all coefficient bounds. CONFIRMED.

Chain rule. (g,p)->(p,z): p_g=0,p_p=1,z_g=-1,z_p=2p+ell, determinant p_gz_p-p_pz_g=+1, so [A',B']_(p,z)=cg=c(p^2+ell p+h-z), the coordinator's (3). (p,z)->(R,t): R_p=z^3, t_z=-z^{-2}, t_p=0, determinant R_pt_z-R_zt_p=-z. So [Ahat,Bhat]_(R,t)=cg/(-z)=cg(-t)=c(-Delta/t)(-t)=+cDelta. PLUS sign exact.
Highest t term of Delta: tPi^2 has degree 7 with coefficient S^2, ell tPi has degree 4, so Delta=...-S^2t^7, nonconstant. Independent check: Ahat_R has t-degree <=3 and Bhat_t <=4, Ahat_t <=2 and Bhat_R <=5, so [t^7] of the bracket is (C0S)'(5D0S^2)-(3C0S)(D0S^2)'=5C0D0S^2-6C0D0S^2=-C0D0S^2=-cS^2, exactly the t^7 coefficient of cDelta. Sign and scalar agree.
Bounds. Weights w(R)=1, w(t)=r: Pi has terms of weight r,2r,3r and the unique top Rt^3 of weight m. So Pi^it^{-j} has weight <=mi-rj<=m (A) or <=n (B) by (2); a term R^at^k then satisfies a+rk<=e, i.e. deg A_k<=m-rk, deg B_k<=n-rk, on every coefficient. The t-range k<=3, k<=5 is Target C's (weight alone would allow k<=n/r for small r; the finer inequality of section 4 closes it). Consistency: deg A_3<=1 with A_3=C0S, deg B_5<=2 with B_5=D0S^2.
Associated graded. The top of Pi^it^{-j} is R^it^{3i-j}; (i,j)->(i,3i-j) is injective and preserves weight (i+r(3i-j)=mi-rj), lower terms of Pi stay strictly lower, so the (m,-r)-initial form of A' maps to the (1,r)-initial form of Ahat without cancellation: ell_(1,r)(Ahat)=Rt^3C(R^rt^{3r-m})=Rt^3C(R^r/t)=sum C_kR^{1+rk}t^{3-k}, and ell_(1,r)(Bhat)=R^2t^6t^{-1}D(R^r/t)=sum D_kR^{2+rk}t^{5-k}; both polynomial since k<=3, k<=5. Monicity: the parent's attained corner p^ez^{3e} has coefficient 1 (H->pz^3 exactly), and pC_3T^3=C_3p^{1+3r}z^{3m}, p^2zD_5T^5=D_5p^{2+5r}z^{15r+6}=D_5p^nz^{3n}, so C_3=D_5=1 and the coefficients of R^m,R^n are one. Total degree: a+k<=a+rk<=e for k>=0 (polynomiality is used here), attained by R^e, so the ordinary degrees are m,n and "three/five" is t-degree only. CONFIRMED.

## 5. Target E: inverse boundary and ring identity. CONFIRMED.

(18) is the correct retained boundary: t=1/z is rational, and a polynomial Ahat lifts only if every negative z coefficient of Ahat(pz^3-z^2+uz+v0,z^{-1}) vanishes; afterwards z=p^2-g+ell p-u, the e.Delta support, both normalized faces and the canonical/coalesced constraints must still be imposed. The producer says exactly this and asserts no polynomial automorphism of the receiver plane and no nilpotent-base equivalence.
Ring identity (19), both inclusions without (2) or (6). All four rings sit in one field: k[g,p]=k[p,z] by the polynomial automorphism, and (R,t)<->(p,z), (U,V)<->(g,p) are birational with the displayed inverses.
Forward: f in k[g,p] and k[U,V]. Then f in k[p,z] gives f in k[R,t,t^{-1}] (p=Pi, z=t^{-1}); f in k[U,V] gives f in k[R,t,Delta^{-1}] (U polynomial, V=-t/Delta, both needing only u=-h from Target B); the Target C intersection gives f in k[R,t]. No degree bound used.
Reverse: f in k[p,z] and k[R,t]. Then f in k[g,p] trivially, so by (8) f in k[U,V,V^{-1}]. Also R=R_source(U,V) is polynomial by (12) with u=-h, and z=-V^{-1}+E(U,V) with E=E_1 at s=1, E(U,0)=h, gives t=1/z=-V/(1-VE) with denominator 1 mod V; so f in k[U,V,(1-VE)^{-1}]. V is prime in k[U,V] and does not divide 1-VE, so the same minimal-exponent argument gives f in k[U,V]. Both inclusions hold; (19) is exact, and it is correctly NOT the claim that k[R,t] equals the source ring.
Consequences checked: given Ahat,Bhat polynomial with (5) and (18) satisfied, [A',B']_(p,z)=cDelta(-z)=cg, so [A,B]_(g,p)=cg, and by (19) A,B lie in k[U,V], i.e. P,Q exist as polynomials with [P,Q]_(U,V)=c: the source bracket is recovered, and reverse ordinaryness is a consequence of (18), not a lost condition. The producer correctly refuses to call this a counterexample endpoint. CONFIRMED.

## 6. Target F: scope, controls, outstanding obligation. CONFIRMED.

No special value is discarded. Target B divides only by m and uses U^{m-1}!=0 as a polynomial; Target C uses S=R-v0 as a nonzero polynomial in R, C0D0=c!=0 from the parent, and Delta(R,0)=1 for all u,ell,v0; Target D uses the coefficient 1 of Rt^3 and S'=1. u=0, ell=0, v0=0 and the fibre R=v0 are all retained. The field is the 16k extension k(mu); the new steps divide by 3 and m only.
Controls, each rederived: (z) z=t^{-1} is in k[p,z], not in k[R,t], and reverses to -V^{-1}+E, not in k[U,V]: both sides of (19) exclude it, and it is exactly the element the Target C intersection removes. (p) p=Pi in k[R,t] and p=V^3U-V in k[U,V]: in both sides of (19), nonconstant in t, so a rational reference fibre does not make outputs functions of R alone. (t) t in k[R,t] but t=1/z and t=-V/(1-VE), with 1-VE nonconstant and coprime to V, so t is in neither k[p,z] nor k[U,V]; dropping (18) would admit it. (wrong constant target) replacing cDelta by c deletes -cS^2t^7 and contradicts the independent t^7 coefficient in Target D; the compressed pair is not Keller in (R,t). (scalar relation) if u+h!=0 the s^5V^{-1} residue of Target B is nonzero and, equivalently, Delta_hPi/t has linear coefficient -(u+h) so U acquires the pole (u+h)/t: the same obstruction seen on both sides.
Scope: the producer claims a necessary full-source compression and the boundary equivalence (19); it claims no coefficient point, solved ideal, F10 or 112/196 exclusion, or JC2, and the compression is consistent, so no exclusion is manufactured here.
Exact outstanding lift/compatibility obligation (retained from the packet, no new theorem): a pair (Ahat,Bhat) in k[R,t]^2 satisfying (5),(6),(17) with monic R^m,R^n corresponds to an actual coalesced F10 receiver only if, in addition, (i) both (18) substitutions have zero negative-z part (by (19) this alone already yields polynomial P,Q); (ii) after z=p^2-g+ell p-u the receiver has support in e.Delta with both normalized faces H^e and (-1)^eg^{2e}(gp+1)^e; (iii) R is the canonical coalesced reference of A, i.e. A_s-f_s(R_s) has s-order 7q+9 with scalar corrections gamma_hs^{7(m-h)}, which (5)-(6) do not encode and which is what fixed u=-h, ell=a2/3, v0; and (iv) P,Q must carry the 16k source hypotheses (rectangle with attained corners and the actual standard (m,n) chain with selected child (13/7,3)). Sufficiency of (i)-(iv) for a source is outside this packet and is not asserted by it.

## 7. Verdicts and strongest conclusion

A CONFIRMED, B CONFIRMED, C CONFIRMED, D CONFIRMED, E CONFIRMED, F CONFIRMED. No failed implication was found; every displayed identity was rederived by hand and every parent conclusion is applied to the identical object. Strongest exact conditional conclusion: assuming the accepted 16k receiver and the coalesced reference (2)/(3) of the coordinator with j0=7q+9, the actual source forces u=-h, R reverses to a polynomial R_source(U,V), and the entire outputs are ordinary Ahat,Bhat in k[R,t] with [Ahat,Bhat]=cDelta, t-degrees exactly 3 and 5 with leaders C0(R-v0), D0(R-v0)^2, deg A_k<=m-rk, deg B_k<=n-rk, leading forms Rt^3C(R^r/t), R^2t^5D(R^r/t), monic R^m,R^n, and the ring boundary (19). This is a necessary compression conditional on the parents, not an existence, exclusion or JC2 statement. No authored seal, no exit-price declaration line, no promotion, no follow-on authority; all writers IDLE after this write.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN check, no corpus scan.

<!-- BODY-END -->
