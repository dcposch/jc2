# Hostile review: F9 exact reverse-polynomiality and complete small source contract (Fable 5.1)

tag=f9-exact-reverse-source-contract-gate-fable5-20260909
frozen_basis=0d39df3c9fd69c939a8420c54d03228b9077777d (provenance only)
reviewer=Claude Fable 5.1 (claude-fable-5-1), different model from the root/Astra authors
launch=root invitation; inputs hashed 05:54:18 UTC; absolute deadline 2026-09-09 06:16:00 UTC
subprocesses=ZERO mathematical subprocesses. Only date, ls, mkdir, cat, sha256sum and this report write were run. Every identity below is hand-derived factored prose.
evidence=box/f9-exact-reverse-source-contract-gate-fable5-20260909/charged-input-hashes.sha256

## 0. Custody and read scope

All six charged copies in /tmp/jc2-lane.Nw9Sdf/inputs were hashed before reading and match the invitation pins token by token: reverse contract f1fd6624..., its artifact a2c27170..., source composition 8c88c027..., receiver map 8bad927c..., cubic ratio 571d1fae..., joint gate f33820d2.... The artifact records body bytes 11462 and body SHA 032bfcb3..., consistent with the seal block of the reverse contract; the seal was not re-hashed and no seal is authored here. All six were read WHOLE. The four upstream proofs/gate are consumed exactly at their stated accepted perimeter: every actual complex 84/140 source gives a normalized ordinary 21/35 receiver with the two stated faces and [A,B]=c*g. No AUDIT, cross, live lane, canonical file, PINS source path or historical checker was opened. No primary text was needed: the new material is elementary.

## 1. Target A: anti-diagonal bijection and reverse criterion — CONFIRMED

Re-derived independently. In K[g,g^-1,p]=K[g,g^-1,q] with q=gp+1, p=(q-1)/g, each g^i p^j equals g^(i-j)(q-1)^j, so W=sum_s g^s f_s(q) with f_s=sum_(i-j=s) a_ij (q-1)^j, a genuine polynomial in q since j>=0. The monomials g^s q^k are a K-basis of K[g^(+-1),q], so the regrouping is unique. Under g=v^-1, p=u v^3-v one has gp=u v^2-1, hence q=u v^2, and g^s q^k maps to u^k v^(2k-s). The assignment (s,k)->(k,2k-s) is injective (k is read from the u exponent, then s from the v exponent), so no two anti-diagonals can cancel and the coefficient of u^k v^(2k-s) in the image is exactly [q^k]f_s. u exponents are never negative. For s<=0 every 2k-s>=0, so no condition; for s>0 the image is ordinary iff every k with [q^k]f_s!=0 satisfies k>=s/2, i.e. q^ceil(s/2) | f_s. The binomial expansion [q^k](q-1)^j=(-1)^(j-k)binom(j,k) gives exactly the displayed linear row L_(m,s,k), vanishing for j<k, with only slots (j+s,j) in S_m present and absent slots identically zero. Row count: ceil(s/2) for s=1..2m sums to m(m+1), i.e. 12 and 30, total 42. Redundancy of the s=2m rows: the (1,-1) face fixes a_(2m+t,t)=d^m binom(m,t) for t=0..m, so f_(2m)=d^m((q-1)+1)^m=d^m q^m. No division by a coefficient, no pivot, no generic stratum. Verified on the report's own controls: W=g gives L_(3,1,0)=a_10=1, fails; W=g^3p+g^2 gives a_20-a_31=0, passes and maps to u.

One remark, not a defect: the criterion holds over any commutative coefficient ring, since it is a monomial-basis statement; characteristic zero is only needed downstream for d=-3/2 and the Jacobian context.

## 2. Target B: degrees, corner, determinant, Jacobian on all of A^2 — CONFIRMED

Each g^i p^j contributes monomials u^k v^(2k+j-i) with 0<=k<=j. From S_m, i>=0 and 2i+j<=7m give j<=7m, so k<=7m and 2k+j-i<=3j<=21m; the rows supply the lower bound 0. Total degree of such a monomial is 3k+j-i<=4j-i<=28m, with equality iff k=j, i=0, j=7m. So u^(7m)v^(21m) is the unique monomial of total degree 28m, and its coefficient is a_(0,7m), which the (2,1) face fixes to the p^(7m) coefficient of H^m, namely 1 (H=p^7-(7/2)g p^5+4g^2p^3-(3/2)g^3p, monic in p). Actual degrees are therefore exactly 84 and 140 with no top cancellation. Determinant: g_u=0, g_v=-v^-2, p_u=v^3, p_v=3u v^2-1, so det=0-(-v^-2)(v^3)=v, agreeing with the receiver report's +v. Chain rule: [P,Q]_(u,v)=([A,B]∘φ)·det=c·v^-1·v=c in K[u,v,v^-1]; since P,Q are ordinary the left side lies in K[u,v], and equality of two elements of K[u,v] inside the Laurent ring is equality in K[u,v], so [P,Q]=c on all of A^2 including v=0. 84 and 140 do not divide one another, so a Keller pair of these actual degrees is a counterexample.

Import named, not invented: this last step uses exactly one external theorem, that an automorphism of the plane has one coordinate degree dividing the other (Jung–van der Kulk; the accepted source proof calls it the Division Lemma). The reverse contract names it but gives no citation; it is used here at statement trust. Nothing else in the sufficiency direction is imported.

## 3. Target C: affine compatibility of the accepted normalization, coverage vs sufficiency — CONFIRMED

The receiver map gives A_old(g,p)=P0(g^3p+lambda g^2-r0, g^-1) up to output constants, and the cubic-ratio report's normalization is the diagonal change (g,p)->(kappa g, mu p) with kappa=lambda/mu, i.e. kappa*mu=lambda, followed by division by alpha*mu^21 (beta*mu^35 for B). Hand check: A_old(kappa g, mu p)=P0(kappa^3 mu g^3 p+lambda kappa^2 g^2-r0, kappa^-1 g^-1), and lambda kappa^2=kappa^3 mu, so the first argument is kappa^3 mu (g^3p+g^2)-r0. Hence A_new(g,p)=P_new(g^3p+g^2, g^-1) with P_new(u,v)=P0(kappa^3 mu u-r0, kappa^-1 v)/(alpha mu^21), an ordinary polynomial because the substitution is an invertible affine map (kappa, mu nonzero). Substituting g=v^-1, p=u v^3-v into g^3p+g^2 gives u, so the reverse of A_new is P_new itself, ordinary, and by Target A every row holds. I also re-derived the normalized faces: with mu^3=a lambda, a kappa/mu^2=1 and b kappa/mu^2=b/a=3/2, so the upper face is H^m; the lower scalar r(0)^m kappa^(2m) lambda^m/mu^(7m)=(-a^2 b)^m a^(-3m)=(-3/2)^m=d^m, and gp+lambda becomes lambda(gp+1). Output translations to A_00=B_00=1 touch only slot (0,0), which has weight 0 for both positive faces, appears in no row (rows use s>=1), and leaves bracket and degrees unchanged.

Distinction kept: coverage (every actual complex source gives a point) rests on 16a/b plus the cube root mu^3=a lambda, hence is over C; sufficiency (every characteristic-zero point gives a counterexample) is elementary and uses only support, faces, rows, bracket and guard. The report states this separation correctly.

## 4. Target D: complete guarded ideal and exact properness equivalence — CONFIRMED at the 16a/b import tier

Generators re-derived: all (2,1) slots 2i+j=7m (i=0..3m, including zero targets), all (1,-1) slots (2m+t,t), A_00-1, B_00-1, all 42 rows, all bracket coefficients sum(il-jk)a_ij b_kl over i+k-1=I, j+l-1=J minus c at (1,0), and z*c-1. Bracket bound: max g-degrees 9 and 15 (at (9,3),(15,5)), max p-degrees 21 and 35, so I<=23, J<=55 is exhaustive; 24*56=1344 slots. Consistency check the report asserts but does not perform: the two faces coincide at (3m,m). H^m there is d^m (only the (3,1) term of H can supply g^(3m) in m factors), and the lower face gives d^m binom(m,m)=d^m. They agree, so the coincidence introduces no nonzero constant. Both face brackets vanish, [H^3,H^5]=0 and [(g^2(gp+1))^3,(g^2(gp+1))^5]=0 up to scalars, so neither top-weight bracket row is a constant either. Changed-object counterobject: if the lower-face scalar were d^(m-1) at the shared vertex, the ideal would contain d^m-d^(m-1)!=0 and be trivially the unit ideal; the report's scalars avoid this.

Equivalence: a point of I_F9 over any characteristic-zero field yields ordinary P,Q (rows), actual degrees 84/140 (corner), [P,Q]=c!=0 (guard), hence a counterexample; a complex counterexample yields, through 16a/b and Section 3 above, a complex point with z=1/c. Properness over Q gives a Qbar-point by the weak Nullstellensatz, and a complex point forbids 1 in the ideal. So proper iff an actual complex 84/140 counterexample exists, exactly as stated, and the exclusion side would kill only this degree pair. The report claims no properness, unit, rational point or ideal equality with Moh or source charts, and none is inferred here. First not-locally-verified premise on the coverage side: the 16a/b conclusion itself, accepted upstream and not re-proved.

## 5. Target E: counts and controls — CONFIRMED

S_3 by hand: i=0..6 give 22,20,...,10 (sum 112), i=7,8,9 give 7,4,1; total 124. S_5: i=0..10 give 36 down to 16 (eleven terms, sum 286), i=11..15 give 13,10,7,4,1; total 321. 445 variables, 447 with c,z. Controls re-derived: epsilon*g at slot (1,0) lies on neither face and inside N(A), shifts L_(3,1,0) by epsilon, so support alone is insufficient. d^m g^(2m)(gp+1)^(m-1) has f_(2m)=d^m q^(m-1), one order short, producing v^-2. The zero-Jacobian control: H has support (0,7),(1,5),(2,3),(3,1) with s=-7,-4,-1,2, so D=H+d g^2 has f_2=d(q-1)+d=dq and D is reverse-ordinary; D lies in Delta; A=D^3+1, B=D^5+1 have (2,1) faces H^3,H^5, (1,-1) faces d^m g^(2m)(gp+1)^m, constants 1, supports in 3Delta,5Delta, ordinary reverses, and [A,B]=0. Consequence the report leaves implicit: the unguarded ideal has the rational point (D^3+1, D^5+1, c=0), so any unit certificate for I_F9 must use z*c-1 essentially, and I_F9 is proper iff c is not nilpotent modulo the unguarded ideal. Counts prove no rank, dimension, complexity, runtime or solver advantage, and the report says so.

## 6. Verdict summary

- A CONFIRMED. B CONFIRMED. C CONFIRMED (coverage over C at the 16a/b tier; sufficiency elementary). D CONFIRMED at the import tier, with the shared-vertex consistency now checked. E CONFIRMED.
- No REFUTED item and no GAP with a missing exact hypothesis. The only external statement in the sufficiency chain is the plane-automorphism degree-divisibility theorem, uncited in the report and used at statement trust.
- Nothing here licenses a builder, an emission, an allocation or a properness claim; the object is an honest finite contract whose decision is undecided.

## 7. Own-only OPEN and collision check

Reread whole before closing. No OPEN[...] entry is raised, no seal or charge_basis is authored, no exit price is declared, no shared, canonical or public write was made, and no other lane's files were read or touched.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — no OPEN identifier is raised; own-only check, not a corpus audit.
<!-- BODY-END -->
