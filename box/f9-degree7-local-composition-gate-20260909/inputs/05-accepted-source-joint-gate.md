# Joint hostile proof gate: F9 source attachment, opposite-edge receiver map, cubic root ratio (Fable 5.1)

tag=f9-source-receiver-joint-gate-fable5-20260909
frozen_basis=0d39df3c9fd69c939a8420c54d03228b9077777d (provenance only)
reviewer=Claude Fable 5.1 (claude-fable-5-1)
launch=root F9 invitation 05:24 UTC; review opened 05:27:15 UTC; absolute deadline 2026-09-09 05:59:00 UTC
subprocesses=ZERO mathematical subprocesses. Only date, ls, cat/sed, sha256sum and this report write were run. All algebra below is hand-derived factored prose.

## 0. Custody and read scope

All 16 lane copies under /tmp/jc2-lane.NBtAPv/inputs were hashed with sha256sum and compared token by token against PINS.json (13 entries plus PINS itself) and the root addition hashes: f9-cubic-root-ratio-coordinator-20260909.md = 571d1fae2682c64c86a13599f0db827b6371f9b5f63b50b186ab8112adb9594c, its artifact.json = 2a8639d5c97b720bc35f40e036559daa133ca3e80f0b9829e8a3cb30c1fd3916. All 16 match; PINS itself hashes 9baeb2cf57961302b8bb66cf3e5c086079dee8ea8b2ce57b6dce266a0b8984a4 as the charged list records. The gghv bundle header reads 1120-1258, matching root's provenance correction; lines 1100-1119 were not included and are not claimed read. No PINS source path, no historical report path, no 0445 blind/cross/live gate, no canonical replacement was opened.

Read WHOLE: read-contract.md, PINS.json, root-source-proof.md (body 10646 B), receiver-map-proof.md (body 18543 B), both transactions (provenance only), f9-source-intake.md, accepted-general-normalizer-proof.md and its gate, f9-cubic-root-ratio-coordinator-20260909.md (body 6320 B) and its artifact, primary-ggv-source-statements.txt (695-747, 1431-1461, 2259-2292), primary-ggv-opposite-interval.txt (128-188, 218-279, 360-397, 1581-1595, 1874-2154), primary-gghv-chain-tables.txt (205-338, 613-817, 910-1050, 1120-1258, 1362-1464), primary-lower-side.txt (200-311), and the page-12 image, inspected visually.

Not charged, therefore imported at statement scope where the producers cite them: ML 2025 normal form (consumed only through the accepted general proof section 3), GGV Props 5.13/5.14/5.16-5.18, Def 5.5, Remarks 5.8/5.10/5.12/6.3, Prop 2.11(5), the mirrored interiors of Prop 7.3/Cor 7.4 (printed "Mimic the proof"), GGHV Algorithms 8/9 exhaustiveness and Remark 2.22, the lower paper's Prop 1.4 interior.

## 1. Group 1: given-pair normalization at D=28

**Scope of the accepted theorem.** Accepted proof section 3 is stated for arbitrary coprime m,n>1 and D>0; only its section 4 specializes to D=25. The source proof consumes section 3 alone, and its Fable gate confirmed section 3 in that generality (ML applies to the given pair, proportional Q rectangle, unique maximiser of Mi+Nj, ratio derived not assumed). So D=28 is inside the actual scope. The D=25/F2 conclusion and the 15/25 receiver are not used as D=28 premises anywhere in the two new reports. CONFIRMED.

**Nonautomorphy, corner, identity.** 84 and 140 do not divide one another, so the Division Lemma makes the pair a counterexample; ML gives a polynomial source automorphism and a rectangle corner (r,s), 0<r<s; the bracket-monomial argument gives the proportional Q corner (t,u); coprimality gives (r,s)=3(a,b), (t,u)=5(a,b), 0<a<b; the inverse coordinates U,V of degrees M,N>=1 give 84=3(Ma+Nb), i.e. 28=Ma+Nb>=a+b. Definition 4.3 holds with the original ratio 3/5 (v_{1,-1}(en_{1,0})=3(a-b)<0 because a<b). CONFIRMED, at ML/Chau trust as in the accepted gate.

**Field passage.** The pair's finitely many coefficients and its Jacobian constant lie in a finitely generated field over Q, which embeds in C; the embedding preserves supports, degrees and the nonzero constant bracket. The complex normalizer is never claimed to descend to K, and nothing in A or B needs it (B's own parameters r, lambda are shown to lie in the working field by coefficient ratios). CONFIRMED.

## 2. Group 2: D=28 selection

**Row inventory, checked independently against the printed tables.** a+b<=28 holds exactly for F1 (16), F2-F6 (25), F7-F8 (21), F9-F11 (28), F18-F19 (24); F13, F20-F21 (30), F12, F22-F24 (32), F14-F17 (33) exceed 28. Both orientations are covered by requiring the unordered pair {3,5}; j is a nonnegative integer by (3.20). F1 (2j+3,3j+4): (3,4),(5,7),...; F2 (j+2,2j+3): (3,5) only at j=1; F3 (4j+3,3j+2): (3,2),(7,5); F4 second entry>=16; F5 first>=9; F6 second>=10; F7/F18 (j+2,4j+7) and F8/F19 (2j+3,5j+7) second>=7; F9 (j+2,2j+3): (3,5) only at j=1; F10 (5j+7,3j+4) first>=7; F11 (j+2,3j+5): (2,5),(3,8). Survivors: F2 j=1 and F9 j=1. CONFIRMED.

**F2 versus F9.** F2 has (a,b)=(5,20): 28=5M+20N is impossible since 5 does not divide 28. No F2 exclusion theorem is used. F9 has (a,b)=(7,21): 28=7M+21N gives 4=M+3N, so M=N=1 and the ML normalizer and its inverse are affine. The normalized degrees are 3*28=84 and 5*28=140. CONFIRMED.

**Prop 5.20 literal proof.** The charged proof text supplies phi=id or phi(x)=x, phi(y)=y+lambda, lambda in K^x, with phi in Aut(L) for polynomial input. Under y->y+lambda each x^i y^j becomes a sum of x^i y^k, 0<=k<=j, so neither coordinatewise bound grows; the coefficient at (21,63) can only receive contributions from i=21, j>=63, and the rectangle allows only j=63, so it is unchanged. The same holds for Q at (35,105). Total degrees and en_{1,0} are preserved by the statement and directly. So the rectangles, both corners and the actual total degrees survive, not merely en_{1,0}. CONFIRMED (interior via Props 5.13/5.16-5.18 imported).

**Starting triple and selected multiplicity.** A0=(7,21), A0'=(1,0); A0-A0'=(6,21)=3(2,7), so (rho0,sigma0)=(7,-2), value 7. A0' has v_{1,-1}=1>0, so the corner is II.b (Prop 2.5(4) proof). Thm 2.20(8): l1=lcm(7,1)=7, and (2.5) reads (11/7,2)=(1,0)+(m_lambda/3)(2/7,1), so m_lambda=6. Item (13): t=0, the pair has exactly one regular corner, A0' is its last lower corner, no preceding II.a segment. Since ordinaryness forces p_0(z)=r(z^7)^3 up to scalar with deg r=3 and r(0) nonzero, multiplicity 6 in z means multiplicity 2 in w=x^2 y^7: r=(w-a)^2(w-b), a,b nonzero, a distinct from b. The alternatives are excluded by the same filter: a triple root would give m_lambda=9 and A1=(13/7,3), which is the F10/F11 chain and admits no {3,5}; three simple roots would give A1=(9/7,1), absent from the table; m_lambda>=5 also follows from Prop 2.5(4). CONFIRMED at the published exhaustiveness trust (Algorithms 8 and 9 at M=35, not rerun).

## 3. Group 3: receiver preparation

**Ordinary source, fractional cut undone.** The receiver starts from the ordinary rectangular pair P0,Q0 in K[u,v], not from the L^(7) child; the intake's lambda1 x^(-2/7) cut is not used and the later Laurent cut y->y+lambda x^(-2) in L^(1) is a different object. CONFIRMED.

**Vertical Euler element and the common shift.** Thm 2.6 at (0,1): sum 1>0, v_{0,1}(P0)=63>0, bracket constant, so an ordinary F=v a(u) with [F, f v^63]=f v^63. Hand bracket: [v a, f v^63]=v^63(63 a' f - a f'), giving (2). Leading coefficients: deg a=k>=1 gives (63k-21)A alpha u^(k+20), nonzero, so k=1; constant a gives degree 20 on the left against 21 on the right. With a=Au+B: 42A=1 and 21 f=(u+r) f', so f=alpha(u+r)^21, r=B/A in K (also r = coefficient of u^20 over 21 alpha). Top v-part of the constant bracket: v^167(105 f' h - 63 f h')=0, so h=beta(u+r)^35. The shift u->u-r has determinant 1, keeps rectangles, corners, highest-u coefficients and strictly lowers (7,-2)-weight on every changed term, so the whole starting face, both endpoints and the standard conditions are unchanged. CONFIRMED.

**Swap and q=7.** (x,y)=(v,u), bracket -c. C_3=(63,21), C_5=(105,35) are the unique max-x points (pure v-leaders) and the unique max-y points (at j=21, -2i+7j<=21 forces i>=63). d0=(-2,7), normalized start (21,7), other endpoint (0,1). Thm 7.6(3) with the i=0 clause gives en_{7,-2}(E)=(5/7)(7,21)=(5,15); the swap negates brackets, so -E swapped is Thm 2.6's element for the swapped pair, with start (15,5)=(5/7)(21,7), q=7. Independently, the D file's ODE forces deg f=2, so the Euler support is (1,1),(3,8),(5,15) and en=(5,15): the i=0 clause is locally confirmed for this face. CONFIRMED.

**Cor 7.4 hypotheses.** (3,5) coprime >1; l=1, bracket -c; v_{1,1} ratio 84/140 and v_{0,1} ratio 21/35 (the corollary uses v_{0,1}, the mirrored form, and the receiver uses it correctly); (-2,7) in V_{>=0}, in Dir(Ps), value 21>0; (1/3)st=(1/5)st=(21,7) in Z x N; 7<21. Positive interval: some axis term x^k, k>=1, exists in Ps or Qs, otherwise both x-derivatives vanish on y=0 and the bracket is 0 there; both d-values are computed at C_3,C_5 in ratio 3/5, so 3rho+sigma>0. Then 21rho'+7sigma'>0 on the whole arc from d to d0 because d0 x d = -(7rho+2sigma) < -(rho) < 0, so the arc is under pi and every intermediate direction is a positive combination. Hence the Prop 7.3 lower endpoint is at or below d. Leading bracket weight 167rho+55sigma=55(3rho+sigma)+2rho>0 forces commutation; Prop 2.1(2b) with common value nonzero makes both leading forms powers of one R, so a monomial on one side forces a monomial on the other, and d is an edge of both. No corollary is applied at a zero-valued boundary. CONFIRMED.

## 4. Group 4: slopes

Cor 7.4 gives l_d(Ps)=R^21 with R in L^(1); minimum x-exponents multiply under powers in a domain, so R is ordinary; y-degree 21 of the edge gives y-degree 1 of R; the edge is nonmonomial, so R=a x^3 y+b x^(3-k) with rho*3+sigma=rho(3-k), whence sigma/rho=-k is an integer and d=(1,-k). Integrality is derived from the linear root, not assumed for polygon slopes. Positivity gives k<3. The lower paper's Cor 1.6 (P,Q in L, constant bracket, no slope-one edge) excludes k=1 directly, and Prop 2.1 there is stated for "a Jacobian pair in L" with (0,-1)<(rho,sigma)<(1,0) and en=(a',b'), a'>b'>0, before the section's minimal-pair paragraph; both apply to Ps with en_d=(63,21). So k=2. The common root parameter follows from Prop 2.1(2b) (R^3 and R^5 powers force R_P^7 proportional to R_Q^7); lambda in K from the coefficient of x^61 y^20 over -21 times the corner coefficient. psi(y)=y+lambda x^(-2) has determinant 1 and collapses the edge to its corner. CONFIRMED.

**No rational slope in (2,3).** psi preserves i-2j, so after it every point other than C_m has i-2j<21m-14m, and the next lower edge at C_m has kappa>2. If the nearer next edge had 2<kappa<3, then 3rho'+sigma'>0, the same commutation argument (valid in L^(1)) makes it common, and Cor 7.4 with the persisting q=7 would give a y-linear root with integer x-exponents, forcing integral kappa. q persists because the d0 face is unchanged: if a second weight-5 Euler solution differed by Z, [Z,R0]=0 with R0=y r(x^7 y^2), and Prop 2.1(2a) gives Z^7 = const R0^5, so 7 ord_y Z = 5, impossible; hence Z=0. So kappa>=3 for both polygons, giving i<=3j, with the corner attaining zero. CONFIRMED locally, at Cor 7.4 statement trust.

## 5. Group 5: literal transport

Support before psi: i,j>=0, -2i+7j<=7m; hence i-2j>=(3/7)i-2m>=-2m, equality only at (0,m). psi maps (i,j) to (i-2t,j-t), keeps i-2j, lowers -2i+7j by 3t, keeps j>=0. With i<=3j this is (5), and T3(x)=g^(-1), T3(y)=g^3 p sends (i,j) to (3j-i,j), turning (5) into I,J>=0, 2I+J<=7m, I-J<=2m, whose vertices are (0,0),(2m,0),(3m,m),(0,7m). Attainment: (0,7m) from the untouched corner; (3m,m) from (0,m), which no other term can reach because that would need d0-value above the maximum; (2m,0) from lambda^m times the (0,m) coefficient alpha r(0)^m, the unique i-2j=-2m term; (0,0) by an added output constant, which changes no bracket and no positive face. I+J=4j-i<=7m-I with equality only at (0,7m): total degrees 21 and 35, leaders single powers of p, g-degrees 9 and 15. Determinants: shift +1, swap -1, psi +1, T3 -g (det[[-g^-2,0],[3g^2 p,g^3]]); product +g; directly, (u,v)=(g^3 p+lambda g^2-r, g^-1) has determinant g in order (g,p), so [A,B]=c g. Inverse g=v^-1, p=v^3(u+r)-lambda v has determinant +v and is rational, not polynomial; arbitrary receiver points do not lift. Face records: R0=y r(x^7 y^2) becomes g^3 p r(p^2/g)=p(p^2-ag)^2(p^2-bg), polynomial; the i-2j=-2m line becomes alpha r(0)^m g^(2m)(gp+lambda)^m. CONFIRMED.

**Page-12 image.** The printed Prop 4.4 proof shows l_{1,-2}(P)=x^28 lambda_p (y-lambda x^-2)^14 and x^42 (y-lambda x^-2)^21 while its swapped polygon is {(0,0),(7,0),(21,7),(0,1)} times (2,3), with corners (42,14),(63,21). x^28 y^14 is not the corner (42,14); the corrected prefactors x^42, x^63 make the edge run from (14,0) and (21,0), which are the printed vertices 2(7,0), 3(7,0). The receiver's formula (3) with x^(21m) is independently right and the printed prefactor is a defect. It was not copied. CONFIRMED.

## 6. Group 6: composition and verdicts

**A (source attachment): CONFIRMED** at the trust tier ML/Chau/GGV Def 4.3 and Prop 5.20 statement/GGHV Thm 2.20, subsection 2.4, table exhaustiveness. First not-locally-verified premise: the published M=35 enumeration; first theorem interior not verified: Prop 5.20's via 5.16-5.18. No local gap.

**B (receiver map): CONFIRMED** at the trust tier GGV Thm 2.6, Prop 2.1 (proof read), Thm 7.6(3) (statement), Prop 7.3/Cor 7.4 (statement, printed "Mimic"), lower paper Cor 1.6/Prop 2.1 (proofs read). First not-locally-verified premise: the mirrored Cor 7.4 interior. Every inequality, guard, determinant, field descent and vertex was rechecked by hand above. No local gap.

**C (composition): CONFIRMED**, exactly this: every actual ordinary constant-J pair of degrees 84/140 over C, hence over any characteristic-zero field by embedding, yields ordinary A,B in C[g,p] of actual degrees 21 and 35, [A,B]=c g with c nonzero, polygons 3 and 5 times conv{(0,0),(2,0),(3,1),(0,7)}, (2,1)-faces alpha Hbar^3, beta Hbar^5 and (1,-1)-faces as recorded. It is NOT a constant-J 21/35 pair, NOT covered by the 15/25 theorem, NOT an exclusion of 84/140 or of degree 140, NOT a complete ideal or properness result, NOT a reverse lift. The bracket scalar is renamed c, never set to 1.

**D (cubic root ratio): CONFIRMED.** Thm 2.6 is applied to the ordinary source at (7,-2) (sum 5>0, value 7m>0), giving ordinary E of weight 5 with [E,alpha R^m]=alpha R^m; the domain gives [E,R]=R/m, so F=mE is needed and is polynomial. Weight-5 monomials are u^(1+2k) v^(1+7k), so F=uv f(z). Hand bracket (z_u=2z/u, z_v=7z/v): A_u=vf+2vzf', A_v=uf+7uzf', B_u=r+2zr', B_v=7uzr'/v, product u(5zr'f-rf-7zrf'), so (1) is right. Residues at a and b (both nonzero, distinct) force f(a)=f(b)=0; for d>2 the leading coefficient C(14-7d) is nonzero at degree d+3>3=deg r, so d=2; substitution gives C[(3a-2b)z-ab]=1, hence b=(3/2)a, C=-1/(ab); the double root is a. The converse holds by the same identity. The conclusion is independent of the bracket sign convention (only C's sign flips). D depends on A only through the double/simple profile of the F9-j1 face; it does not use B. It gives no attainment.

**E (conditional normalization): CONFIRMED conditional on B.** With mu^3=a lambda, kappa=lambda/mu: Hbar(kappa g, mu p)=mu^7 p(p^2-(a kappa/mu^2)g)^2(p^2-(b kappa/mu^2)g), and a kappa/mu^2=a lambda/mu^3=1, b kappa/mu^2=b/a=3/2 by D; the lower face factor lambda becomes lambda/(kappa mu)=1. Dividing by alpha mu^21 and beta mu^35 leaves the upper faces H_*^3, H_*^5 and the lower scalars r(0)^3 kappa^9 mu^-18 = (-(3/2)a^3)^3 a^-9 = (-3/2)^3 and likewise (-3/2)^5, using mu^27=a^9 lambda^9. The bracket becomes c kappa^2 mu g/(alpha beta mu^56), nonzero and not 1. The cube root may need an extension of K, so the statement is over C. Supports, hull and vertex guards survive diagonal scaling. No exclusion, point, ideal or lift follows.

**Dependencies.** C needs A and B. E needs B (face formulas) and D (ratio). D needs only A's face profile. A failure of A would leave B and D as conditional statements about the rectangular F9-j1 source; a failure of B would leave A, D intact and void E.

## 7. Controls (manual, changed objects, not computed tests)

- Endpoint-only instead of rectangle: a source with en_{1,0}=(21,63) and total degree 84 but an extra term x^20 y^64 keeps en_{1,0} and the total degree while breaking deg_v<=63; the v-leading coefficient is then not the degree-21 f(u) and the vertical Euler equation (2) is unavailable. The failed arrow is the pure v-leader of group 3.
- Fractional ring: applying the lower-side Prop 2.1 to the L^(7) child would violate its hypothesis P,Q in L; the receiver undoes the cut first.
- Wrong prefactor: x^(14m)(y-lambda x^-2)^(7m) ends at (14m,7m), not the corner; the failed arrow is the Cor 7.4 top at C_m.
- Wrong sign: psi(y)=y-lambda x^-2 turns the edge into x^(21m)(y-2 lambda x^-2)^(7m), which keeps the point (7m,0); there i<=3j fails and T3 produces g^(-7m). The failed arrow is ordinaryness via (4).
- Reverse polynomiality: (g, gp) has bracket g but inverse first coordinate v^-1; no source lift.
- D ratio control: any b different from 3a/2 leaves the residual 1-(3a-2b)z/(ab), so no polynomial Euler element exists; the failed arrow is Thm 2.6's guarantee, which would contradict constancy of the Jacobian.

## 8. Own-only OPEN and collision check

Reread whole before closing. This report raises no OPEN[...] entry, authors no seal, no charge_basis and no exit price; no shared, canonical or public write was made; no other lane's files were read or touched.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->
