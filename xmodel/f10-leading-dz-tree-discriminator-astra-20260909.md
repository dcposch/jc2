# F10 leading face: Davenport–Zannier tree discriminator

Basis0d39df3c9fd69c939a8420c54d03228b9077777d. First action2026-09-09 15:51:12 UTC; controlling cap16:03:12 UTC. PRODUCER-ONLY, pending independent review. All mathematics is manual. The exact two accepted16q/r local inputs were hashed before whole reads. No coefficient artifact, other local body, solver or running review was consumed.

## Verdict and scope

The proposed count is correct: **for each fixed integer r>=1 there are seven orientation-preserving weighted-plane-tree classes, hence seven geometric leading-pair orbits under T scaling**. Their two underlying shapes and positive edge-weight formulas are uniform in r. This is not seven rational coefficient tuples, seven rational ideals, a finite set across all r, or an exclusion. The univariate scaling parameter must remain, and every full residual, pole condition and guard remains binding. The correspondence uses the named primary theorem below; no complete source point or computational speedup is supplied.

## 1. Source leading identity and exact ramification

Give S,t weights1,r and put m=3r+1,n=5r+2,N=3n=5m+1. Accepted16r gives normalized weighted leaders

    A_top=S*t^3*C(T), B_top=S^2*t^5*D(T), T=S^r/t,
    C(0)=D(0)=1, deg C=3, deg D=5,
    lc(C)=a!=0, lc(D)=b!=0.

Here C=1+d_r*T+v_(2r)*T^2+k_m*T^3; the nonzero leading guard is essential. Scalar mate shear/translation is below the B leading weight. Taking the full bracket's highest weight gives -S^2*t^7. Direct differentiation of the two displayed factors yields exactly

    n*T*C'*D-m*T*C*D'-C*D=-1.                 (1)

No lower term can enter this weight. At a root alpha of C, (1) reads n*alpha*C'(alpha)*D(alpha)=-1. At a root of D it reads m*alpha*C(alpha)*D'(alpha)=1. Thus all eight roots of C,D are simple, disjoint, and away from zero. These conclusions include all parameter degeneracies compatible with the leading guard, not a generic-coefficient assumption.

Define

    Phi=(b^m/a^n)*C^n/(T*D^m),
    P_DZ=b^m*C^n, Q_DZ=a^n*T*D^m.

Equation(1) gives

    Phi'/Phi=-1/(T*C*D),
    Phi'=-(b^m/a^n)*C^(n-1)/(T^2*D^(m+1)).  (2)

P_DZ,Q_DZ have equal degree N and equal leading coefficient a^n*b^m. At infinity Phi tends to1, and (2) has leading term -(ab)^-1*T^-9. Consequently Phi-1 has exact order8 there, with leading coefficient1/(8ab), and

    deg(P_DZ-Q_DZ)=N-8,
    lc(P_DZ-Q_DZ)=a^(n-1)*b^(m-1)/8.         (3)

The critical-value partitions of Phi are (n,n,n) over0, (m,m,m,m,m,1) over infinity, and (8,1^(N-8)) over1. There are no other critical values: (2) accounts for every finite zero/pole ramification, and infinity supplies the remaining index8. The finite roots of P_DZ-Q_DZ are simple. Thus this is precisely a DZ pair with nine distinct roots between P_DZ and Q_DZ and degree difference N+1-9.

## 2. Exact primary correspondence and remaining scaling

Pakovich–Zvonkin §§1–2 define this equality case and relate it to weighted bicolored plane trees. Their Proposition2.11 supplies existence and uniqueness up to a fractional-linear change; §2.4 collapses parallel edges and Theorem2.24 supplies the weighted-tree criterion. Apply their construction to f=Phi/(Phi-1): black and white degrees are respectively (n,n,n) and (m,m,m,m,m,1); the unique non-simple face has degree8. These are imported theorem statements, not a new proof of Riemann existence. [Primary §§1–2](https://arxiv.org/pdf/1306.4141).

There are nine vertices and eight ordinary tree edges; their weights sum to N. The unique white vertex of weighted degree1 is T=0; the unique degree8 face corresponds to T=infinity. Fixing those two points leaves exactly T↦tau*T, tau!=0. Normalizing C(0)=D(0)=1 introduces no further continuous parameter. Conversely each such tree gives a rational function with these marked points; factoring its zeros/poles and normalizing the constants yields C,D. Its logarithmic derivative has numerator constant over TCD, and its residue at zero fixes that constant to -1, recovering(1).

Algebraic representatives exist by the paper's §2.3 statement, so these are seven geometric orbits also describable over finite algebraic extensions, not necessarily over Q itself. No field-of-moduli degree or unitree-rationality conclusion is used. The scaling action on pairs is free: a stabilizer must satisfy tau^3=tau^5=1, hence tau=1. Setting a=1 for a coefficient calculation would therefore leave three cube-root choices per orbit, potentially21 normalized tuples—not seven tuples. No such normalization is licensed on the full source merely by this leading correspondence.

## 3. Exhaustive manual tree count

Use topological valency to count incident edges, and weighted degree for n,m,1. A black leaf is impossible: its single edge would have weight n>m, exceeding the degree of its white endpoint. The light white vertex of degree1 is a leaf. The sum of white valencies is eight, so the six white vertices have total valency excess two. There are exactly two possibilities.

**One white valency-three vertex.** It joins all three black vertices; the other five whites are leaves, four heavy of weight m and one light. Since 2m>n, no black vertex can support two heavy leaves. Four heavy leaves on three black vertices are impossible. This rules out the star without a hidden leaf-distribution assumption.

**Two white valency-two vertices.** Both are heavy. Removing the four white leaves leaves a path of three black vertices, subdivided by these two whites. The leaves are three heavy and one light. Again no black vertex can have two heavy leaves, so each black vertex has exactly one heavy leaf. The light leaf is at the middle black vertex or at an end; reversing the abstract path does not create a third case.

If the light leaf is at the middle, the four path-edge weights, in order, are

    2r+1, r, r, 2r+1.

Each end has residual degree n-m=2r+1; each internal white's two weights sum to m. The middle has residual degree n-m-1=2r. All weights are positive. Only its valency-four cyclic order matters: two identical end branches, one heavy leaf and one light leaf. Fix the light leaf as cyclic origin; the heavy leaf has three positions. Hence exactly three oriented plane classes, not a reflection quotient.

If the light leaf is at an end, the ordered path weights from that end are

    2r, r+1, r, 2r+1.

The marked end and middle each have valency three and three distinguishable branches, giving two cyclic orders each. The light leaf distinguishes the ends, so no path automorphism identifies these choices. Hence exactly four classes. The total is3+4=7.

At r=1 some internal weights become1, but an internal branch with further vertices is not a light single-edge leaf. Likewise the two middle branches in the end-marked case remain distinguishable by their marked-end structure. No extra plane identifications or zero weights appear. Complex conjugation reverses cyclic orders and is not automatically quotiented. This checks the smallest parameter without numerical sampling or enumeration code.

## 4. What a lossless redesign would still require

This adds a finite leading-shape classification to the already-known differential identity; it does not solve either full residual. For each fixed r, one may prospectively choose an exact algebraic representative (C_i,D_i) for each orbit and retain tau as a nonzero variable in C_i(tau*T),D_i(tau*T). Such a substitution could cover all geometric FIELD points after finite extension while retaining all remaining coefficients and every full equation. It is not yet an emitted decomposition, an equality of possibly nonreduced schemes, or a same-field normalization. In particular u,ell,d1,v2,a cannot be fixed for free; for general r the face coordinates are d_r,v_(2r),a, and all lower coefficients remain.

A small manual consistency check is the coefficient of T in(1): D_1=(n-1)/(m+1)*C_1=(5r+1)/(3r+2)*C_1, matching the accepted upper Euler coefficient. Higher coefficients of D are determined successively by nonzero rational pivots mk+1, but their last compatibility equations and all source residuals must still be checked. Tree existence alone is not an extension to a full mate.

Changed-hypothesis controls are explicit: without positive weights the leaf inequalities fail; identifying mirror embeddings undercounts; without a,b!=0 the root passport and exact index8 can collapse; dropping the full low residuals is invalid by accepted16r's section8 guarded upper-row family with final constant residual -1. Keeping only one rational tree or setting tau=1 would discard unlicensed field/scaling possibilities.

OPEN (implementation interface only): exact coefficient representatives constructed here =0 of7 orbits, and full residual substitutions certified =0. The cheapest next discriminator, if separately chosen after review, is an exact r1 scaling-invariant coefficient description/read-back proving all seven orbits and any zero-coordinate charts are retained, before considering branchwise source work. No branch farm, builder, solve, point or performance claim is authorized. Allr still means an unbounded integer parameter; seven shape formulas do not decide that unbounded problem. Own whole-read and one existing-interface check precede sealing; no new global open ID is raised. All writers are idle at terminal handoff.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9372`.
- Body SHA-256:
  `cf14e0af93c846d7b1615ac988f1476a24338bf21ad0cb978280b9bdd0aa3420`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
