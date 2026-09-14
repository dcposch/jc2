# f10 leading-DZ tree gate (Fable 5.1, 2026-09-09)

launch=2026-09-09 16:06:52 UTC; deadline=min(launch+15m, 16:22:00Z)=16:21:52Z
lane=/tmp/jc2-lane.mMnfbI; owned box=box/f10-leading-dz-tree-gate-fable5-20260909/

## 0. Custody

All five input SHA256 verified at 16:06:52Z against the ordered list (order 1-5 = astra discriminator, artifact.json, coordinator contract, whole-mate Euler elimination, Pakovich-Zvonkin arXiv 1306.4141 PDF). Inputs 3/4 are accepted 16q/16r interfaces and are consumed, not re-audited.

Scope actually exercised: manual reading of inputs 1-4 whole; PDF 5 text extracted (pdftotext) into the owned box only; no CAS, no arithmetic subprocess, no network, no other bodies.

## A. Highest-weight interface: CONFIRMED (strengthened)

Independent derivation, not agreement. Grade S:1, t:r; m=3r+1, n=5r+2, N=3n=5m+1. From the accepted 16r normal form A=S t^3+f t^2+h t+k (f=S d-u, h=1-u d+S v, deg d<=r, deg v<=2r, deg k<=m) and B_5=S^2, deg B_j<=n-rj, the weight-m part of A is S t^3 C(T) with T=S^r/t, C=1+d_r T+v_(2r) T^2+k_m T^3, and the weight-n part of B is S^2 t^5 D(T), deg D<=5, D(0)=1, [T^5]D=[S^n]B_0=b. C(0)=1 because the t^3 coefficient is exactly S; D(0)=1 because B_5=S^2. Both hold at every guarded point, including u=0, ell=0, d_r=0, v_(2r)=0.

Weight bookkeeping. d/dS lowers weight by 1 and d/dt by r, so [A,B] has weight <= m+n-1-r=7r+2 and its weight-(7r+2) component is exactly [A_top,B_top]. Delta's coefficients (input 4, eq. (4)) have weights 7r+2 for -S^2 t^7 and at most 6r+1 for every other term (delta_6=2uS: 6r+1; delta_5=-u^2-2S: 5r+1; lower ones smaller). Hence [A_top,B_top]=-S^2 t^7 is an exact identity on every complete point, not a generic statement.

Direct computation with T_S=rT/S, T_t=-T/t:
A_S=t^3(C+rTC'), A_t=S t^2(3C-TC'), B_S=S t^5(2D+rTD'), B_t=S^2 t^4(5D-TD'). Then
A_S B_t - A_t B_S = S^2 t^7 [(C+rTC')(5D-TD') - (3C-TC')(2D+rTD')]
= S^2 t^7 [ -CD -(3r+1)TCD' +(5r+2)TC'D ]  (the rT^2C'D' terms cancel).
So nTC'D - mTCD' - CD = -1 identically in T (distinct monomials S^(rj)t^(-j)). Eq. (1) of input 1 CONFIRMED.

Coefficient form (my own, used below): with C=sum c_i T^i, D=sum D_k T^k, [T^j] of the left side is sum_(i+k=j)(ni-1-mk)c_i D_k. j=0 gives -1 (ok); j>=1 gives the pivot -(1+mj)D_j + (terms with i>=1), pivots nonzero, so D_1..D_5 are determined by (c_1,c_2,c_3): D_1=(n-1)/(m+1) c_1, matching input 4's e_r=(1+5r)/(2+3r) d_r. [T^8]=(3n-1-5m)c_3D_5=0 automatically. The two remaining conditions are [T^6]=[T^7]=0: weighted-homogeneous of weights 6 and 7 in (c_1,c_2,c_3) with weights (1,2,3). These are precisely the top S-coefficients (S^(6r+2), S^(7r+2)) of input 4's residuals E1_res, E0_res.

Roots. At C(alpha)=0: n alpha C'(alpha)D(alpha)=-1, so alpha!=0, C'(alpha)!=0, D(alpha)!=0; at D(beta)=0: m beta C(beta)D'(beta)=1. All eight roots simple, nonzero, pairwise disjoint, given deg C=3 (a=k_m!=0) and deg D=5 (b!=0). CONFIRMED.

Strata (new, manual). If a=c_3=0: [T^7] reduces to (2n-1-5m)c_2D_5=-(5r+2)c_2D_5 and [T^6] to -(10r+4)c_1D_5 (after c_2=0), so b!=0 forces C=1, then -mTD'-D=-1 forces D=1, b=0: contradiction. If a=b=0: descending j=6,5,4,3,2 with pivots -(2r+1),r,4r+1,7r+2,10r+3 (if c_2!=0) forces D_4=..=D_1=0 and then (2n-1)c_2=0, contradiction, so c_2=0; then (if c_1!=0) pivots -(7r+3),-(4r+2),-(r+1),2r+1 and finally (n-1)c_1=0. If b=0, a!=0: [T^7],[T^6],[T^5],[T^4] with coefficients (3r+1),(6r+2),(9r+3),(12r+4) force D_4=D_3=D_2=D_1=0 and [T^3]=(15r+5)c_3!=0: contradiction. Conclusion: every NONZERO (c_1,c_2,c_3) solving the face system has a!=0 and b!=0; the only degenerate solution is C=D=1, i.e. d_r=v_(2r)=k_m=0, which the source monicity (input 3 cond. 2, input 4 guard) forbids. No lower-support or parameter stratum escapes; on the face, a!=0 <=> b!=0. Zero-coordinate charts d_r=0 or v_(2r)=0 alone are NOT excluded by this and are retained.

Phi and passports. Phi=(b^m/a^n)C^n/(T D^m): Phi'/Phi=nC'/C-1/T-mD'/D=(nTC'D-CD-mTCD')/(TCD)=-1/(TCD). CONFIRMED. Phi'=-(b^m/a^n)C^(n-1)/(T^2D^(m+1)); its degree at infinity is 3(n-1)-2-5(m+1)=(3n-5m)-10=-9 with leading coefficient -(ab)^(-1), so Phi-1=(1/(8ab))T^(-8)+..., exact order 8. P_DZ=b^mC^n, Q_DZ=a^nTD^m both have degree N and leading coefficient a^nb^m; P_DZ-Q_DZ=(Phi-1)Q_DZ has degree N-8 and leading coefficient a^(n-1)b^(m-1)/8. CONFIRMED (3). Coprimality: C(0)=1 and disjoint roots. Fibres: over 0 (n,n,n); over infinity (m^5,1) with T=0 the simple pole; over 1: infinity with multiplicity 8 plus the N-8 roots of P_DZ-Q_DZ, all simple because finite zeros of Phi' lie only at roots of C where Phi=0. No other critical value exists (Phi' has no other zeros; poles are accounted). Riemann-Hurwitz: 3(n-1)+5(m-1)+7=3n+5m-1=2N-2. Bound (9) of PZ: deg R>=(N+1)-(3+6)=N-8, attained.

## B. Pakovich-Zvonkin import: CONFIRMED, with one GAP on fields

Exact statements used (PZ 1306.4141, read at pp.2-10 of the extracted text):
- Prop 2.4 / Prop 2.12: bound (9) attained iff a bicolored plane map with passport (alpha,beta,gamma), gamma=(n-r,1^r), exists.
- Prop 2.6-2.8: dessin f^-1([0,1]) is a connected bipartite plane map; face degrees = pole multiplicities.
- Prop 2.11 (Riemann existence): for every bicolored plane map there is a Belyi f with that dessin, unique up to a Mobius change of x.
- Sec. 2.3 first sentence: some Mobius-equivalent f has algebraic coefficients. Def 2.16/Rem 2.17: bachelors (unique-degree vertex/face); up to three may be placed at rational points without leaving the field of moduli.
- Sec. 2.4 + Def 2.19-2.21 + Thm 2.24: maps with all finite faces of degree 1 <-> weighted bicolored plane trees (parallel-edge bundles -> weights); Def 2.20 isomorphism is orientation-preserving and weight-respecting; bound (9) attained iff a weighted tree with passport (alpha,beta) exists. Thm 3.1 (not needed, consistent): p+q<=n/d+1 holds trivially here since gcd(n,m,1)=1.

Object. With f=Phi/(Phi-1)=P_DZ/(P_DZ-Q_DZ): f=0 at roots of C (black, degrees n,n,n), f=1 at roots of Q_DZ (white, degrees m^5 and 1 at T=0), poles at the N-8 simple roots of P_DZ-Q_DZ (faces of degree 1) and at T=infinity (order N-(N-8)=8, the unique nonsimple face). CONFIRMED. Tree-ness independently: each edge is incident to exactly one face (Def 2.7); deleting from each of the N-8 degree-1 faces its unique incident edge keeps connectivity (the digon's other edge remains) and leaves 9 vertices, 8 edges, one face: a spanning tree; deleted edges form consecutive parallel bundles with a surviving tree edge, giving well-defined positive weights summing to N. So the object is precisely a weighted bicolored plane tree with passport ((n^3),(m^5 1)), 8 edges, outer face degree 8=number of tree edges. Weighted-tree isomorphism classes = dessin isomorphism classes by Def 2.20.

Converse (independent). Given such a tree, Prop 2.11 gives f; move the degree-8 pole to infinity and the degree-1 white vertex to 0 (both bachelors); the residual Mobius freedom is exactly T->tau T. Write Phi=f/(f-1)=P/Q with P=lambda C^n, Q=mu T D^m, C(0)=D(0)=1, deg C=3, deg D=5, 8 distinct nonzero roots (distinct vertices). Set E=nTC'D-mTCD'-CD; then Phi'=const C^(n-1)E/(T^2D^(m+1)). Phi' has no finite zeros besides the roots of C (all finite faces simple, all white vertices give poles), so E has no roots; degree count at infinity: (3n-3)+deg E-2-5(m+1)=deg E-9 must equal -9 (outer face degree 8), so E is a constant, and E(0)=-C(0)D(0)=-1. Eq. (1) is recovered. Residue reading of input 1 CONFIRMED.

Equivalence and scaling. Two normalized pairs give isomorphic dessins iff Phi_2=Phi_1(tau T): Mobius maps preserving the marked 0 and infinity are scalings. Stabilizer: C(tau T)=C(T) needs tau^3 a=a, D needs tau^5 b=b, so tau=1 (a,b!=0, gcd(3,5)=1): free action CONFIRMED. Scaling classes of solutions of (1) with a,b!=0 <-> isomorphism classes of weighted trees with the passport. Combined with A: the nonzero solution set of the two face equations is exactly the union of the 7 (by C) scaling orbits.

Rational tuples vs orbits. Setting a=1 picks tau with tau^3=a_i^-1, three values, giving three DISTINCT pairs per orbit by freeness: 21 monic representatives over Qbar, CONFIRMED as input 1 states; normalizing b=1 gives 35, a=b gives 14. Over a non-closed field the count depends on cube roots, so tau must stay a variable. Field of definition: both bachelors sit at 0 and infinity, so by Rem 2.17 (citing [7]) each dessin has a Belyi function over its field of moduli K_i, [K_i:Q]=size of its Galois orbit, sum over Galois orbits=7. GAP: which of the 7 are Galois-conjugate and whether any K_i=Q is not derivable from the theorems imported here (Prop 2.18 needs a UNIQUE tree; here there are seven). Input 1 correctly claims no field-of-moduli or rationality conclusion. No scheme component or multiplicity statement follows from PZ; Thm 2.24 is a set-level existence criterion.

## C. Tree classification: CONFIRMED, 3+4=7 for every integer r>=1

Independent count. Data: 3 black vertices of degree n=5r+2; white vertices: five of degree m=3r+1, one of degree 1; 8 edges, positive integer weights, bipartite tree (no parallel edges, no cycles). Inequalities used: n>m (2r+1>0), 2m>n (r>0), all displayed weights positive (r>=1). Nothing else.

1. No black leaf: its single edge would have weight n>m>=degree of its white end. So black valencies are >=2, sum 8: multisets (2,2,4) or (2,3,3).
2. The degree-1 white is a leaf of weight 1. The five heavy whites have valencies >=1 summing to 7: exactly one white of valency 3, or exactly two of valency 2. CONFIRMED.
3. Valency-3 white W: its three edges reach three distinct blacks (tree), the other five whites are leaves (4 heavy of weight m, 1 light). A black carrying two heavy leaves has degree >=2m>n. So at most 3 heavy leaves: impossible. CONFIRMED (no hidden assumption).
4. Two valency-2 whites: deleting the four white leaves leaves 5 vertices, 4 edges, whites of valency 2, blacks of valency (1,1,2): the path E1-W1-M-W2-E2. Leaves: 3 heavy, 1 light; at most one heavy per black and each end needs >=1 leaf, so exactly one heavy leaf per black; the light leaf sits at M (case a) or at an end (case b; path reversal identifies the two ends abstractly).
   Case a weights: E-edges n-m=2r+1; W1,W2 remainders m-(2r+1)=r; M check r+r+m+1=5r+2=n. Weights (2r+1,r,r,2r+1). Total 3m+1+6r+2=15r+6=N.
   Case b weights from the light end: E1 edge n-m-1=2r; W1 remainder r+1; M remainder n-m-(r+1)=r; W2 remainder 2r+1; E2 check m+2r+1=n. Weights (2r,r+1,r,2r+1). Total 15r+6=N. All CONFIRMED.
5. Plane structures. Whites have valency <=2 (trivial cyclic order). Case a: E1,E2 valency 2; M valency 4 with branches L,R (isomorphic rooted branches W(r)-E(2r+1)-leaf(m)), heavy leaf H, light leaf l. Automorphisms of the abstract tree fix M,H,l and may swap L,R. Cyclic orders with origin l: 6 sequences of {L,R,H}; modulo L<->R exactly 3 classes = position of H (first, second, third). The classes H-first and H-third are mirror images; H-second is achiral. 3 classes CONFIRMED.
   Case b: E1 valency 3 with branches heavy leaf (m), light leaf (1), path (2r): pairwise distinct, 2 cyclic orders; M valency 3 with branches toward E1 (weight r+1, contains the light leaf), heavy leaf (m), toward E2 (weight r): distinct, 2 orders; E2 valency 2. The light leaf fixes E1, hence the path orientation, hence trivial automorphism group: 2x2=4 distinct classes, forming two mirror pairs. CONFIRMED.
6. r=1: weights (3,1,1,3) and (2,2,1,3). At M in case a the path edges have weight 1 = light-leaf weight, but they end at whites of degree 4 (valency 2), not at a degree-1 leaf, so no new identification; in case b all branch weights at E1 (4,1,2) and at M (2,4,1) are distinct. No zero weight, no coincidence. Total 7 at r=1 CONFIRMED.

Total 3+4=7 for all r>=1; no correction, no counterexample. Consistency remark (count only, not a scheme claim): the two face equations have weights 6 and 7 in the weighted plane P(1,2,3), whose intersection number is 42/6=7, matching seven simple points away from the orbifold points a=0 (which A shows carry no nonzero solutions). Reflection: the seven are 1 achiral + 3 mirror pairs; complex conjugation swaps mirror pairs, so the Galois orbit structure must respect this, but nothing further is derived.

## D. Theorem-interface composition: what it buys, what remains

Bought (CONFIRMED, manual). In input 4's presentation L_r, the two rows of top S-degree (S^(6r+2) of E1_res, S^(7r+2) of E0_res) are exactly the T^6 and T^7 coefficients of (1), depend only on (d_r,v_(2r),k_m) with scaling weights (1,2,3), and their nonzero solution set is precisely 7 scaling orbits, each with a!=0 and b!=0 automatically. Hence, over Qbar, every point of L_r has (d_r,v_(2r),k_m)=(tau d^(i),tau^2 v^(i),tau^3 a^(i)) for exactly one i in 1..7 and exactly one tau in Qbar^* (tau^3=a/a^(i), so tau is algebraic). Substituting the i-th exact representative and retaining tau as a variable removes 3 variables, adds 1, consumes 2 rows, and turns the guard omega*a*b-1 into omega*tau^8*a^(i)b^(i)-1, i.e. tau!=0. At r=1: from 12 variables/<=20 rows to 10 variables/<=18 rows PER BRANCH, over the number field K_i. Lossless as a FIELD-point interface: Qbar-points of L_r = disjoint union over i of Qbar-points of the seven substituted systems. Existence needs any one branch; exclusion needs all seven, or one per Galois orbit (a Q-defined system has no Qbar-points on a branch iff none on its conjugates). Since input 3 turns any characteristic-zero point into a complex counterexample and properness over Q is equivalent to a Qbar-point, this is the right existential scope.

Not bought. No representative (C_i,D_i) is constructed; no minimal polynomials, no fields K_i, no Galois orbit sizes. No reducedness or nilpotent statement about L_r or its face scheme (the Bezout remark in C concerns the two face equations alone). No speedup: number-field arithmetic per branch may cost more than the 2 removed unknowns save; the two INCONCLUSIVE 12/20 solves stay inconclusive. The lower rows of both residuals, the variables u,ell,d_0..d_(r-1),v_0..v_(2r-1),k_1..k_(m-1),omega and tau all remain (at r=1: u,ell,d_0,v_0,v_1,k_1,k_2,k_3,omega,tau). Nothing about h or any coefficient's nonvanishing is imported. Zero-coordinate charts d_r=0 or v_(2r)=0 are retained inside the representatives if they occur; only the all-zero face is excluded, and that by source monicity, not by choice.

Cheapest exact remaining discriminator (named, not authorized): derive by hand the two face equations [T^6]=[T^7]=0 at r=1 (m=4,n=7; at most 3 and 2 nonzero terms after the pivot recursion) and solve them exactly at a=1 in (c_1,c_2), expecting 21 points in 7 scaling classes; factor the resulting univariate over Q to read the Galois orbits and fields K_i. Wall: minutes by hand for the equations, seconds of exact univariate work if a solver is later charged. It decides whether any branch is over Q and confirms the count independently of C.

## E. Limitations, scope and raised OPEN

Scope: inputs 1-4 read whole after hash match; PZ read at pp.2-10 (Sec. 1 statement through Thm 2.24 and the start of Sec. 3), pdftotext output kept only in the owned box. All algebra above is manual; no CAS, no arithmetic subprocess, no other body or network. Inputs 3/4 consumed as accepted interfaces; input 2's body hash and byte count agree with input 1's printed seal. This review changes no theorem and no clock. Incomplete: fields of moduli/Galois orbits of the seven trees (GAP in B); reducedness of the face scheme rests on a Bezout count and is not promoted; the weighted-Bezout formula itself is cited from memory, not from a charged source. The relation between the seven leading orbits and the previous inconclusive solves is untested.

## OPEN(S) RAISED

- OPEN[F10-TOPFACE-GALOIS-R1] QUANTITY: number of Galois orbits among the seven leading trees at r=1, value <=7, and whether any field K_i = Q. CHEAPEST TEST: the r=1 face system at a=1 named in D, exact univariate factorization over Q. WALL: <=15 minutes manual derivation plus seconds of exact solving if charged.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN check; no corpus scan.

<!-- BODY-END -->
