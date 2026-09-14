# FIRST hostile gate: 7-adic obstruction to simultaneous contacts (producer f10-two-contact-seven-adic-coordinator-20260909)

2026-09-09. Gate lane fable5. Launch 21:36 UTC; controlling stop 21:52:00 UTC (earlier than launch+18 min), never reset. Charged inputs: exactly the seven ordered SHA256 pins in the brief, all seven verified byte-identical in the charged order before any read. Scientific premises: accepted 17w (18506 bytes, 4bbecd35...) with the brief's Cramer qualification (e_y = +12(1+L)E/Gamma; re-derived below, producer determinant argument unaffected), accepted 16l (12982 bytes, 38cf3fb9...) for single-contact existence/control only, and the one external premise the brief admits: the normalized 7-adic valuation extends to an algebraic closure of Q7 with rational values, and a number field embeds there. No irreducibility or ramification-degree theorem is used. The producer under review is the 9586-byte WHOLE (1a490ff5...). ZERO mathematical subprocesses; every valuation, residue and coefficient below was checked by hand. No Seal, no charge_basis.

## 0. Verdict table

| Item | Verdict | Smallest actual defect |
|---|---|---|
| A valuation lemma (section 3): support, zero unknowns, nonnegative/mixed/negative cases, 3a=2b, P²Q versus constant, exact -2/7,-3/7 | CONFIRMED | none mathematical; the 3a<2b list omits 2b, which is the case hypothesis itself |
| B application to literal A_z,B_z at z integral, z mod 7 in {0,1}; v7(5040)=1; negative case V=zP,W=z²Q, /z⁴, all 7+8 scaled coefficients, any h | CONFIRMED | none; section 7 says the excluded-residue coefficients "need not be" units, they are never units (understatement only) |
| C degree obstruction (degree 0..6 terms, fractional part -2/7), 17w monic cubic J3 in normalized V, embedding, residue table r=1,2,3 mod 7, every j, r=2 j=1 | CONFIRMED | none |
| D zero guarded algebra including nilpotents via a field quotient; no Bezout, no all-r/source/Keller/JC2 closure; j=0 and single contact survive; excluded residues fail exactly one hypothesis | CONFIRMED | none; no overclaim of residual classes or novelty found |

Accepted scope is exactly the producer's: for r = 1,2,3 mod 7 (r>=2) and every 1<=j<=r-1 the normalized guarded cubic algebra of 17w is the zero ring, hence no cubic with two distinct contact exponents exists. This is a necessary-system obstruction on three residue classes. It is not a complete F10 exclusion, not a source/Keller/JC2 result, and r = 0,4,5,6 mod 7 stay undecided by the x-criterion.

## A. Valuation lemma

Hypotheses are read as hypotheses: A has support Q²,PQ,Q,P³,P²,P,1 with all coefficients integral and Q²,P³ units; B has support Q²,P²Q,PQ,Q,P³,P²,P,1 with all nonconstant coefficients integral, P²Q a unit, constant of valuation exactly -1. Zero coefficients (valuation infinity) are allowed everywhere else. Unknowns P,Q in Q7bar, a=v7(P), b=v7(Q), infinity permitted. Only the ultrametric rule "unique strictly least term => nonzero sum" is used.

Both nonnegative (including P=0 or Q=0 or both): every nonconstant B term has valuation >=0, the constant has -1, unique least, B!=0. Mixed a>=0,b<0 (a=infinity allowed): in A the unit Q² term sits at 2b; PQ>=a+b>=b>2b, Q>=b>2b, P³,P²,P,1>=0>2b; unique least, A!=0. Mixed a<0,b>=0: unit P³ at 3a; Q²>=2b>=0>3a, PQ>=a+b>=a>3a, Q>=0>3a, P²>=2a>3a, P>=a>3a, 1>=0>3a; A!=0. So P,Q are both nonzero with a,b<0.

3a<2b: then b>3a/2, and since a<0, 2a>3a, a>3a, b>3a/2>3a, a+b>5a/2>3a (5a/2-3a=-a/2>0), 0>3a; P³ uniquely least in A. 2b<3a: then b<3a/2<a, so 3a>2b, 2a>2b, a>b>2b, b>2b, a+b>2b, 0>2b; Q² uniquely least in A. Hence 3a=2b; with t=-a/2>0, a=-2t, b=-3t. In B the unit P²Q term is at -7t; Q² at >=-6t, PQ >=-5t, Q >=-3t, P³ >=-6t, P² >=-4t, P >=-2t, all strictly above -7t; constant exactly -1. If -7t<-1 the P²Q term is the unique least; if -7t>-1 the constant is; either way B!=0. So -7t=-1, v7(P)=-2/7, v7(Q)=-3/7. Every case, including the zero unknowns, is closed; integrality and units were never inferred from the unknowns. (L) CONFIRMED.

## B. Literal A_z, B_z at the two exponent types

Formula check. The producer's A_z, B_z are term-for-term the 17w displays (6),(7), which the accepted 17w gate re-derived from the 16l partitions (H6=z(z-1)A_z, H7=z(z-1)(z-2)B_z, z(z-1)(z-2)!=0 on 5/3<z<2, so H6=H7=0 iff A_z=B_z=0). Cramer qualification re-checked: with determinant -qstar=Gamma/12, e_x=12LE/Gamma and e_y=+12(1+L)E/Gamma; then (1+L)e_x-Le_y=0 and Q_y e_x-Q_x e_y=12E(LQ_y-(1+L)Q_x)/Gamma=E. The 17w ideal identity (16) stands.

Integral z, z mod 7 in {0,1}, P=V, Q=W. A_z coefficients: 1/2 (unit), z-2, (z-2)(z-3)/6, (z-2)/6, (z-2)(z-3)/4, (z-2)(z-3)(z-4)/24, (z-2)(z-3)(z-4)(z-5)/720; 2,4,6,24,720=2⁴·3²·5 are 7-units, so all integral; P³ coefficient (z-2)/6 has z-2 = 5 or 6 mod 7, a unit. B_z: 1/2, 1/2 (P²Q, unit), (z-3)/2, (z-3)(z-4)/24, (z-3)/6, (z-3)(z-4)/12, (z-3)(z-4)(z-5)/120, (z-3)(z-4)(z-5)(z-6)/5040; 12 and 120=8·15 are units, so the seven nonconstant ones are integral; 5040=7·720 gives v7(5040)=1 exactly; z-3,z-4,z-5,z-6 are 4,3,2,1 (z=0) or 5,4,3,2 (z=1) mod 7, all units, so the constant has valuation exactly -1. Lemma applies: (I) v7(V)=-2/7, v7(W)=-3/7. CONFIRMED.

Negative case v7(z)=-h, h a positive integer (z rational, so integral valuation), z!=0. Substituting V=zP, W=z²Q and dividing by z⁴, recomputed term by term. A: W²/2 -> Q²/2; (z-2)VW=(z-2)z³PQ -> (1-2/z)PQ; (z-2)(z-3)W/6=(z-2)(z-3)z²Q/6 -> (1-2/z)(1-3/z)Q/6; (z-2)V³/6 -> (1-2/z)P³/6; (z-2)(z-3)V²/4 -> (1-2/z)(1-3/z)P²/4; (z-2)(z-3)(z-4)V/24 = (...)zP/24 -> (1-2/z)(1-3/z)(1-4/z)P/24; constant -> (1-2/z)(1-3/z)(1-4/z)(1-5/z)/720. B: W²/2 -> Q²/2; V²W/2=z⁴P²Q/2 -> P²Q/2; (z-3)VW/2 -> (1-3/z)PQ/2; (z-3)(z-4)W/24 -> (1-3/z)(1-4/z)Q/24; (z-3)V³/6 -> (1-3/z)P³/6; (z-3)(z-4)V²/12 -> (1-3/z)(1-4/z)P²/12; (z-3)(z-4)(z-5)V/120 -> (1-3/z)(1-4/z)(1-5/z)P/120; constant -> (1-3/z)(1-4/z)(1-5/z)(1-6/z)/5040. All fifteen agree with the producer's lists. v7(k/z)=h>0 for k=2..6, so each 1-k/z is a unit: A is integral with Q²,P³ units; B nonconstant integral with P²Q=1/2 a unit and constant of valuation exactly -1, for every h. Lemma: v7(P)=-2/7, v7(Q)=-3/7, hence (N) v7(V)=-h-2/7, v7(W)=-2h-3/7. The rescaling is a change of unknowns inside the valuation argument, not a new normalization or a division by V or W. CONFIRMED.

## C. Degree obstruction and the residue classes

If V is algebraic with v7(V)=k-2/7, k an integer, and sum a_i V^i=0 with rational a_i, degree<=6, then two nonzero terms i!=j have valuation difference (v7(a_i)-v7(a_j))+(i-j)k-2(i-j)/7, an integer minus 2(i-j)/7, nonzero because 7 does not divide 2(i-j) for 0<|i-j|<=6. So all nonzero terms have distinct valuations, the sum has a unique least term and cannot vanish; V satisfies no nonzero rational polynomial of degree<=6 (equivalently [Q(V):Q]>=7, though only the degree-3 instance is used). Both (I) and (N) have fractional part -2/7 mod 1. (The same holds for W with 3/7, unused.)

17w (29), confirmed by its gate: any normalized simultaneous contact point over an algebraically closed characteristic-zero K has u!=0 (from exponent x, or from any exponent outside {0,1,2}), V a root of the monic rational cubic J3 in the normalized V=v/u², and W=W(V) a rational polynomial in V. So Q(V) is a number field containing W; embed it into Q7bar (external premise). The rational-coefficient equations A_z=B_z=0 persist under the embedding, so (I) or (N) applies to whichever prescribed exponent z meets the 7-adic condition, contradicting J3(V)=0 with deg J3=3<=6. Either exponent may serve; no real-coefficient assumption enters; the "source-map" degree is not used, only J3. CONFIRMED.

Residues of x=(5r+2)/(3r+1), gcd always 1 since 3(5r+2)-5(3r+1)=1. r=1: numerator 7=0, denominator 4, x integral, x=0 mod 7. r=2: numerator 12=5 (unit), denominator 7=0, so v7(x)=-v7(3r+1)<0 whatever the power of 7 in the denominator. r=3: numerator 17=3, denominator 10=3, x=1 mod 7. These use z=x only, so every 1<=j<=r-1 is covered at once; r=2,j=1 has x=12/7, h=1, v7(V)=-9/7, no sample needed. Complement, checked to confirm the producer's exclusion list: r=0 gives x=2 (A's P³ coefficient (z-2)/6 not a unit); r=4 gives x=1·6⁻¹=6; r=5 gives 6·2⁻¹=24=3; r=6 gives 4·5⁻¹=12=5 (B's constant numerator has a factor 0 mod 7, valuation not -1). Exactly the four undecided classes. CONFIRMED.

## D. Zero algebra, controls, overclaim check

Zero algebra. The 17w guarded algebra Q[V,W(V)⁻¹]/(J3,Z0,Z1) is finite-dimensional (0..3). If nonzero it has a maximal ideal whose residue field is a number field in which W(V) is invertible and J3=Z0=Z1=0; the 17w read-back (an ideal identity valid in every Q-algebra) restores A_x=B_x=A_y=B_y=0 there. Section C then contradicts. Hence the algebra is zero, nilpotents included, with no Bezout certificate, no irreducibility claim on any leading algebra, and no extra coordinate division. V=0, W=0 were handled inside the lemma rather than assumed away. CONFIRMED.

Controls. j=0: d=0, 17w's divisions by y-x and the cubic bound do not exist, and the lemma alone yields only v7(V)=-2/7 (or -h-2/7), i.e. a degree>=7 floor that is consistent with 16l's existence and finiteness statements (16l claims no degree bound and no seven-point count). Single contact survives. Excluded residues: at z=2 mod 7 exactly the A-P³ unit hypothesis fails; at z=3,4,5,6 mod 7 exactly the B-constant valuation -1 fails; the producer's section 7 names these correctly ("need not be" a unit understates: they never are). Overclaim check: the title, section 1, custody (uniform_contact_exclusion=false, source_exclusion=false, excluded_r_residues_mod7=[1,2,3]) and section 7 all confine the result to three residue classes of the necessary two-contact system; no F10 source exclusion, Keller/JC2 or novelty claim appears. The producer's general statement ("either exponent with v7(z)<0 or integral z=0,1 mod 7") is correctly scoped and correctly not turned into a classification via y.

## E. Read scope and custody

All seven hashes matched in the charged order before reading. Documentary checks only: the producer's first 9254 bytes hash to 8e7469...c57, equal to its Seal, artifact and custody records; 17w's first 18173 bytes hash to e78827...399, equal to its Seal. Artifact/custody timestamps are consistent (opened 21:31:46Z, finalized 21:34:22Z, controlling stop 21:43, status TERMINAL-UNREVIEWED, review PENDING). Written: this report and box/f10-two-contact-seven-adic-gate-fable5-20260909/READ-SCOPE.md only, via apply_patch. No provenance, corpus, ledger, peer, protected path, web, network, process or agent access.

## OPENS RAISED

- NONE new. The producer's own recorded gap stands: r = 0,4,5,6 mod 7 undecided by the x-criterion. Documentary note only, derived by hand from the producer's already-proved either-exponent statement and not a new theorem: for those classes y=(5r+2+j)/(3r+1) is integral and lands in {0,1} mod 7 exactly at j = 5,6 (r=0), j = 6,5 (r=4), j = 1,3 (r=5), j = 3,1 (r=6) mod 7. Cheapest next step remains the producer's: apply the criterion to y, manually; nothing computed or authorized here.

## COLLISIONS

status: EMPTY

- NONE — own-only check: both owned targets were absent at launch (21:36 UTC) and are the only paths written; own WHOLE reread, raised-OPEN check and this collision check completed 21:42 UTC before the marker. No corpus, ledger or provenance scan performed.

<!-- BODY-END -->
