# f10 r1 leading univariate gate (fable5, 2026-09-09)

lane=f10-r1-leading-univariate-gate-fable5-20260909
launch=2026-09-09T16:22:17Z deadline=2026-09-09T16:37:17Z (launch+15m, earlier than 16:38:00Z)
owner_writes=xmodel/f10-r1-leading-univariate-gate-fable5-20260909.md, box/f10-r1-leading-univariate-gate-fable5-20260909/
tools_used=sha256sum, ls, date, cat/heredoc appends, Read (six inputs WHOLE). ZERO CAS, zero arithmetic subprocess, zero network.

## 0. Input custody (checked before reading)

| # | file | sha256 | status |
|---|------|--------|--------|
| 1 | f10-r1-leading-coefficient-compression-astra-20260909.md | ead39705189f7faf338bab7937488e96c3ddf296c9ba0eed328ea63442619fb7 | MATCH |
| 2 | f10-r1-leading-coefficient-compression-astra-20260909.md.artifact.json | 698d9b66520bb7eab65f3a19637ac637aca881e4f0cb6be3f7fd79dfef8e1c02 | MATCH |
| 3 | f10-cubic-resonance-ode-discriminator-astra-20260909.md (accepted 16l) | 38cf3fb95cdc7a0298fa5b35f56ab08dec5b64a40f4d2fc8d7976d189b23538c | MATCH |
| 4 | f10-compact-counterexample-contract-coordinator-20260909.md (accepted 16q) | 6c6fe089033832c9d33639f8438a43c3dbfd8a28d06e05ef76ee141438de6d7f | MATCH |
| 5 | f10-whole-mate-euler-elimination-astra-20260909.md (accepted 16r) | a5ab487c4619742b6252e2503488eea4d6e927b58fd2821207cc85bcba7cf8d5 | MATCH |
| 6 | f10-leading-dz-tree-gate-fable5-20260909.md (accepted 17a, restricted clauses) | 8679623bb1e947b8ab8b654f3d5c5f370a1dda9e5109da25aed1feed1f1b2c4d | MATCH |

Input 6 is used ONLY for: guarded leading ODE, primary geometric correspondence, free scaling, exactly 7 geometric orbits per fixed r. Its degenerate strata, weighted-Bezout/reducedness, fields-of-moduli/bachelor descent and seconds-of-solving clauses are NOT used.
Both previous complete-Q solves were INCONCLUSIVE and are not premises here.

## A. Recurrence, q6/q7, H!=0, map to 16l: CONFIRMED (recovered, not new)

Own derivation. Grade S:1,t:1 (r=1, m=4, n=7). From 16r (3): weight-4 part of A = S t^3 + d_1 S^2 t^2 + v_2 S^3 t + k_4 S^4 = S t^3 C(T), T=S/t, C=1+F T+H T^2+a T^3, F=d_1,H=v_2,a=k_4. Weight-7 part of B = S^2 t^5 D(T), D_i=[S^(2+i)]B_(5-i), D_0=[S^2]B_5=1, D_5=[S^7]B_0=b. With T_S=T/S, T_t=-T/t: A_S B_t-A_t B_S = S^2 t^7[(C+TC')(5D-TD')-(3C-TC')(2D+TD')] = S^2 t^7[7TC'D-4TCD'-CD] (T^2C'D' cancels). Weight-9 part of Delta is -S^2 t^7 only, so (1) 7TC'D-4TCD'-CD=-1 holds exactly at every complete point.

[T^j] of the left side is sum_(i+k=j)(7i-4k-1)c_i D_k, c=(1,F,H,a). j=0: -1 (ok). j>=1: -(4j+1)D_j+(10-4j)F D_(j-1)+(21-4j)H D_(j-2)+(32-4j)a D_(j-3)=0, i.e. input 1's (2). Solving: D1=6F/5; 9D2=12F^2/5+13H so D2=(12F^2+65H)/45; 13D3=-2F D2+9H D1+20a=(-24F^3-130FH+486FH)/45+20a so D3=(-24F^3+356FH+900a)/585; 17D4=-6F D3+5H D2+16a D1; 21D5=-10F D4+H D3+12a D2. j=6 (coefficient 25 on D6=0): q6=14F D5+3H D4-8a D3. j=7: q7=7H D5-4a D4. j=8: pivots 33 D8, 22F D7, 11H D6 all on zero coefficients and (32-32)a D5=0: identically zero. j>=9: empty. So q6,q7 are ALL upper conditions. Input 1's (2),(3), D1..D5 CONFIRMED verbatim.

H=0 check (own replay): q7 gives D4=0 (a!=0); D5=12aD2/21=4aD2/7; q6 gives 8aF D2-8a D3=0 so D3=F D2=4F^3/15; D3 recurrence at H=0 gives (-24F^3+900a)/585=4F^3/15, i.e. 900a=180F^3, F^3=5a; D4 recurrence gives -6F^2(4F^2/15)+96aF/5=0, i.e. F(F^3-12a)=0. F^3=5a!=0 forces F!=0 then 7a=0: contradiction. H!=0 CONFIRMED on the guarded system (uses only a!=0). Same content as 16l's u!=0 (at s=1, (u,v,w)_16l=(H/a,F/a,1/a) is a nonzero triple, so 16l forces H/a!=0). NOT new.

Map to 16l. 3x(1) is 16l's (1) at m=4 ((5m+1)=21, 3m=12, exponent a_16l=(5m+1)/(3m)=7/4) with k=-3, for C(0)=D(0)=1 instead of monic. T=s z with s=H/a: C(sz)/(a s^3)=z^3+(H/(as))z^2+(F/(as^2))z+1/(as^3)=z^3+z^2+v z+w with v=Fa/H^2, w=a^2/H^3 (H/(as)=1, as^3=H^3/a^2=1/w). T d/dT is scale invariant and (1) is bilinear, so the monic pair (C_m,D_m)=(C(sz)/(as^3),D(sz)/(bs^5)) satisfies 16l (1) with k~=-3/(a b s^8). 16l's k=-3 C_m(0) D_m(0)=-3 w f5 then gives b s^5=1/f5, i.e. input 1's (4). The z^2 coefficient is 1 exactly because s=H/a (16l's u=1 slice), possible iff H!=0. Reciprocal c(x)=1+x+v x^2+w x^3, d=sum f_N x^N, f_N=[x^N]c^(7/4) finite partition sums. CONFIRMED: exponent 7/4, monic reciprocal recipe, D_m=sum f_i z^(5-i).

Symbol hygiene: normalized v (=d_1 k_4/v_2^2) is a scalar, distinct from 16r's polynomial v(S) whose S^2 coefficient is H; s=H/a is a scalar, distinct from the source variable t; 16l's u (=1 here) is not the source u. Own check of 16l's contact sign: with 4cy'=7c'y for y=c^(7/4), W=12cd'-21c'd for d=y-(f6x^6+f7x^7+f8x^8+...) has [x^5]W=-72f6, [x^6]W=-3(28f7+17f6), [x^7]W=-3(32f8+21f7+10v f6); at f6=f7=0 this gives k=-96 f8, i.e. [x^8](d-c^(7/4))=k/96=k/(24m). Consistent with 16l section 4.

## B. Finite-partition constants, E/L/R, p of degree 7, both directions of (8): CONFIRMED

Falling products for 7/4: (7/4)(3/4)=21/16; x(-1/4)=-21/64; x(-5/4)=105/256; x(-9/4)=-945/1024; x(-13/4)=12285/4096; x(-17/4)=-208845/16384 (12285x17=208845). Partition sums (own enumeration, u=1): f6 has the 7 terms (i,j,l)=(6,0,0),(4,1,0),(2,2,0),(0,3,0),(3,0,1),(1,1,1),(0,0,2); f7 the 8 terms (7,0,0),(5,1,0),(3,2,0),(1,3,0),(4,0,1),(2,1,1),(0,2,1),(1,0,2). These match 16l's displayed f_6,f_7.

f6 = 273/65536 -(315/8192)v +(105/1024)v^2 -(7/128)v^3 +(35/512)w -(21/64)vw +(21/32)w^2 (e.g. a_6/720: 12285/720=273/16; a_5/24: 945/24=315/8; a_3/6=-7/128; a_4/6=35/512). Times 65536/7: 39 -360v +960v^2 -512v^3 +640w -3072vw +6144w^2. E6 and E(v)=39-360v+960v^2-512v^3 CONFIRMED.

f7 = -663/262144 +(819/32768)v -(315/4096)v^2 +(35/512)v^3 -(315/8192)w +(105/512)vw -(21/128)v^2 w -(21/128)w^2 (a_7/5040: 208845/5040=41+7/16=663/16; a_6/120: 12285/120=819/8; a_5/12=-315/4096; a_4/2=105/512; a_3/2=-21/128). f6/4 = 273/262144 -(315/32768)v +(105/4096)v^2 -(7/512)v^3 +(35/2048)w -(21/256)vw +(21/128)w^2. Sum: w^2 cancels; w-part = w[-(21/128)v^2+(63/512)v-175/8192] = -7(192v^2-144v+25)w/8192 = -112 L w/131072; constant part = (7/128)v^3-(105/2048)v^2+(63/4096)v-195/131072 = (7168v^3-6720v^2+2016v-195)/131072 = R/131072. (5) CONFIRMED with L=192v^2-144v+25, R=7168v^3-6720v^2+2016v-195.

Division (6): ((112/3)v-7)L = 7168v^3-5376v^2+(2800/3)v-1344v^2+1008v-175 = 7168v^3-6720v^2+(5824/3)v-175; R minus this = (224/3)v-20 = (4/3)(56v-15). L(15/56) = (43200-120960+78400)/3136 = 640/3136 = 10/49 != 0. Hence (L,R)=(1) in Q[v]. CONFIRMED.

(7): substitute w=R/(112L) into E6 and multiply by (112L)^2/256: 6144/256=24, 112(640-3072v)/256=280-1344v, 112^2/256=49, giving p=24R^2+(280-1344v)LR+49EL^2. Degrees 6,6,7: only 49EL^2 reaches degree 7, leading coefficient 49(-512)(192^2)!=0. deg p=7 EXACTLY. CONFIRMED.

(8) both directions (field points, any characteristic-zero field). (=>) f6=f7=0 gives E6=0 and 112Lw=R; if L(v)=0 then R(v)=0, contradicting (6); so w=R/(112L), and E6=0 times the nonzero (112L)^2/256 gives p(v)=0. (<=) p(v)=0: if L(v)=0 then p=24R^2 forces R(v)=0, contradiction, so w=R/(112L) is defined; then 112Lw-R=0 gives f7+f6/4=0 and (112L)^2 E6/256=p=0 gives E6=0, so f6=0, so f7=0. CONFIRMED.

Ring level, nilpotents included. (f6,f7)=(E6,112Lw-R) in Q[v,w] (unit multiple and unimodular triangular change). In Q[v,w], (112L)^2 E6 == 6144R^2+(640-3072v)R(112L)+E(112L)^2 = 256p mod (112Lw-R), so p lies in (E6,112Lw-R). Since (L,p)=(1) in Q[v] (at a root of L, p=24R^2!=0 by (6)), AL+Cp=1 makes L a unit in Q[v,w]/(E6,112Lw-R) and in B=Q[v]/(p); this is a Bezout identity, not a generic localization. With L invertible, (E6,112Lw-R)=(E6,w-R/(112L)) and eliminating w gives Q[v]/(256p/(112L)^2)=Q[v]/(p). So Q[v,w]/(f6,f7) ~= B, nilpotents and all. CONFIRMED. dim_Q B=7 as a vector space (monic-degree-7 quotient); no distinct-root claim at this stage.

Units without generic localization: an element of a commutative ring is a unit iff it lies in no maximal ideal; every residue field of B is a finite extension of Q in which (v,w=R/(112L)) is a normalized f6=f7 point by (8)(<=); 16l section 4 proves w!=0 and f5!=0 at every such point. So w, f5 are units of B. L is a unit by the Bezout identity. Escapes: L=0 impossible ((6)); w=0, f5=0 impossible (16l at every residue field); v=0: own manual evaluation p(0)=24(195^2)+280(25)(-195)+49(39)(625)=912600-1365000+1194375=741975!=0, so v is also a unit of B (no v division was ever made; this is a check, not a needed step); algebraic-field stratum: all constants are fixed nonzero rationals and the equivalence is over every characteristic-zero field and over B itself, so no stratum escapes. No gcd, factorization or root list was computed.

## C. Retained full-scale map (4), D(T), b, omega, both directions: CONFIRMED formally; no rows emitted

Map check. From F=v/(ws), H=1/(ws^2), a=1/(ws^3): H/a=s, Fa/H^2=v, a^2/H^3=w. Conversely from (F,H,a) with H,a!=0: s=H/a, w=a^2/H^3!=0, v=Fa/H^2 reproduce F,H,a (v/(ws)=(Fa/H^2)/(a/H^2)=F, ws^2=1/H, ws^3=1/a). So {(F,H,a):H,a!=0} <-> {(v,w,s):w,s!=0} bijectively; no zero-v chart is discarded. C(T)=(1/w)C_m(T/s) reproduces 1+FT+HT^2+aT^3 term by term. D(T)=b s^5 D_m(T/s), D(0)=b s^5 f5=1 forces b=1/(s^5 f5) and D(T)=D_m(T/s)/f5; [T^5]D=1/(s^5 f5)=b consistent. (4) CONFIRMED. Guard: a b=1/(w s^8 f5), so omega a b-1=omega/(w s^8 f5)-1, equivalently omega=w s^8 f5 after multiplying by the unit w s^8 f5 of B[s,s^-1]. omega is therefore eliminated, not free; it is not set to 1. CONFIRMED.

Top rows. [S^8]E1_res and [S^9]E0_res are the weight-9 (t^1,t^0) parts of [A,B]-Delta, hence exactly [T^6],[T^7] of (1): -q6 and -q7 (own extraction above); nothing of lower weight reaches those slots. After substitution they lie in (f6,f7)Q[v,w^(+-1),s^(+-1)] up to units: the seven equations [T^1..T^7] of (1) are affine-linear in the D-unknowns with constant pivots; 16l pivots the five lowest x-powers of W (=highest T-powers) leaving f6,f7, input 1 pivots [T^1..T^5] leaving q6,q7; both are chart descriptions of the same closed D-line subscheme over Q[v,w][1/w], on which both chart coordinates (D_m(0)=f5 and b) are units by 16l, so the two elimination ideals coincide. Hence q6,q7 and the guard vanish EXACTLY in Lambda:=B[s,s^-1], not only at residue fields.

Existence both ways (field points over any characteristic-zero K). (->) A K-point of L_1 has a!=0,b!=0 (guard), H!=0 (A); put s=H/a, v=Fa/H^2, w=a^2/H^3; (1) holds, the scaled monic pair satisfies 16l (1), 16l section 3 gives f6=f7=0 and D_m=sum f_i z^(5-i), (8) gives p(v)=0 and w=R/(112L); the K-point of Lambda[u,ell,d0,v0,v1,k1,k2,k3] kills every substituted row, and omega=1/(ab)=w s^8 f5. (<-) A K-point of the substituted system gives v with p(v)=0, w=R/(112L)!=0, s!=0, f5!=0; define d1,v2,k4 by (4) and omega=w s^8 f5; every row of L_1 evaluates to the substituted row (zero), and the top rows/guard are zero by the identity. Inverse-pole conditions: 16r retains them by parametrization (A via (3)) and by the proved consequence of the upper rows (B via (8)-(10) of 16r); neither uses d1,v2,k4 as free symbols, so both are preserved verbatim under substitution. CONFIRMED as FORMAL substitution correctness. NOT done by anyone: the 17 retained rows ([S^0..S^7]E1_res, [S^0..S^8]E0_res) have never been substituted, emitted or read back; this report emits none.

Free coefficients after substitution at r=1: u, ell, d0, v0, v1, k1, k2, k3 (8 polynomial unknowns) and the unit s, over the 7-dimensional algebra B (v with p(v)=0; w, f5, L, omega determined). Eliminated: d1,v2,k4 (into v,s) and omega (guard). Rows: 20-2-1=17 at most. Any further linear elimination of the deficit-one band (d0,v1,k3) from [S^7]E1_res,[S^8]E0_res is NOT derived here. Honest degrees: the source pair has ordinary degrees 28m=112 and 28n=196 (16q) if every retained row holds; 7 is dim_Q B, an auxiliary leading-face algebra dimension, never a source or map degree. A B-point is not a full point.

## D. Composition with 17a's seven orbits: CONFIRMED (separability of p), no Galois/irreducibility claim

Bijection. Scaling tau.(F,H,a)=(tau F,tau^2 H,tau^3 a) (T->tau T) preserves (1), C(0)=D(0)=1, and the guard; it is free on the guarded face set X (tau^3 a=a and tau^2 H=H with H!=0 force tau=1). The invariants v=Fa/H^2 and w=a^2/H^3 are tau-invariant (weights 1+3-4, 6-6). Fibre of (F,H,a)->(v,w) over a point of V(f6,f7) with w!=0 is {(v/(ws),1/(ws^2),1/(ws^3)):s!=0} by C, and tau sends s to s/tau, so each fibre is exactly one scaling orbit. Surjectivity: for any (v,w) in V(f6,f7)(Qbar), w!=0 and f5!=0 (16l), and the s=1 lift C=C_m/w, D=D_m/f5 satisfies 21TC'D-12TCD'-3CD=k~/(w f5)=-3 w f5/(w f5)=-3, i.e. (1), with a=1/w!=0, b=1/f5!=0. So X/scaling <-> V(f6,f7)(Qbar) <-> roots of p in Qbar (via (8), v -> (v,R/(112L))) are explicit bijections.

Count. 17a (accepted clause): X has exactly 7 scaling orbits at r=1. Hence p has exactly 7 distinct roots in Qbar; with deg p=7 (B) it is squarefree. Independently, deg p=7 already caps the orbit count at 7, so only 17a's lower bound (existence of the seven trees) is load-bearing. Therefore B=Q[v]/(p) is reduced, a product of number fields, i.e. finite etale over Q, and Q[v,w]/(f6,f7)~=B is reduced. No weighted Bezout formula, no gcd, no factorization used. NOT inferred: irreducibility of p, seven rational factors, any Galois partition, or reducedness of the full 17-row source system; the last is untouched by this leading algebra.

## Cheapest next discriminator (named, not authorized)

Exact substitution of (4) and omega=w s^8 f5 into the 17 retained rows over B[s,s^-1][u,ell,d0,v0,v1,k1,k2,k3], with read-back of each row and a measured term-count/byte comparison against the original 12-variable rows. Wall: minutes if charged. No solve, no budget escalation. No execution authority is created by this report.

## OPEN(S) RAISED

- OPEN[F10-R1-RETAINED-ROWS-READBACK] QUANTITY: number of nonzero retained rows after substitution, value <= 17, and their maximal term count relative to the 12-variable rows. CHEAPEST TEST: the exact substitution/read-back named above. WALL: <= 10 minutes if charged.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN check (this report and its box only); no corpus scan.

## Scope, GAPs and own whole-read check

Read/tool scope: exactly the six inputs, whole, after hash match; no provenance followers, no other bodies, no network, no CAS, no arithmetic subprocess. Every number above is hand arithmetic shown inline. Nothing was emitted as a residual artifact; no solve, builder or budget is authorized. Hash custody: all six 64-hex tokens in this report equal the input hashes (diff empty).

Verdicts: A CONFIRMED (recovered, not new); B CONFIRMED (E,L,R,(6),(7),(8) both ways, ring isomorphism with nilpotents, units by Bezout identity and 16l residue-field nonvanishing); C CONFIRMED as formal substitution correctness with existence both ways and omega eliminated, 17 rows retained and unemitted; D CONFIRMED conditional only on 17a's accepted seven-orbit count: p squarefree of degree 7, B finite etale over Q.

GAPs (left open, not filled): (i) irreducible factorization of p, Galois orbits, whether any root is rational; (ii) reducedness or properness of the full 17-row retained system; (iii) any deficit-one band linear elimination; (iv) representation size after substitution (the raised OPEN). Both earlier complete-Q solves remain INCONCLUSIVE and were not used. No Seal and no charge_basis are authored here.

Own whole-read at 16:32:14Z: sections 0, A, B, C, D, discriminator, OPEN(S) RAISED (one entry with quantity, cheapest test, wall, relation token), COLLISIONS, this section. No marker before this line.

<!-- BODY-END -->
