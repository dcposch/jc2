# All-parameter F2: an ordinary polynomial receiver with the two degree-five tops

Status: **UNREVIEWED SOURCE-INTERFACE PROOF.** The requested necessary arrow holds at the explicitly ordinary rectangular actual-F2 scope. No uniform local exclusion theorem is consumed or asserted. Pure factored prose; ZERO mathematical subprocesses.

## 1. Exact source, result, and history boundary

Let K have characteristic zero, q be a nonnegative integer, m=q+2 and n=2q+3. Suppose P0,Q0 in K[u,v] have nonzero constant Jacobian c0 and are an ACTUAL ordinary rectangular standard F2 representative:

- For e=m,n respectively, support is contained in [0,5e] x [0,20e], with (5e,20e) attained.
- The actual starting triple has A0=(5,20), A0'=(1,0), direction(5,-1), typeII.b and selected child A1=(7/5,2), as in the literal F2 row of GGHV1708 Section5 and Theorem2.20. These are source data, not merely the name of an admissible row.

Then, over a finite algebraic extension of K if needed, there are ORDINARY polynomials A,B in K'[g,p] satisfying

    deg A=5m, deg B=5n,  A_(5m)=H^m, B_(5n)=H^n,
    [A,B]_(g,p)=c*g^2, c!=0,

where the subscripts denote the ENTIRE highest ordinary homogeneous parts, and H is one of

    H=p^2(g^3+p^3),
    H=p^2(p+g)(p+(1-rho)g)^2,  rho^2-3rho+1=0.

Both golden conjugates are retained. Every source coefficient is transported through explicit invertible Laurent substitutions; ordinaryness of the final ENTIRE pair is proved below, not assumed from its leading faces. A,B are monic in p of degrees5m,5n. The result imposes no parity, no c=1 normalization and no unproved inner-face coefficient constraints.

The proof actually uses only coprime m,n>1 with this same source profile. The equation n=2m-1 selects the printed F2 arithmetic family; it is not needed for the transport. For the displayed q-family, coprimality is immediate from n=2m-1.

**What is not generalized.** The accepted fixed(3,5) published-chain report continues after the selected upper cut and obtains three inner polygons, using an explicitly(3,5) unequal-endpoint assignment. The present proof STOPS BEFORE that successor classification. It asserts the full envelope I,J>=0, I+J<=5e and the exact tops H^e, not those three polygons, not their exact g-degree3e bounds, and not their unequal/common inner-face formulas for arbitrary q. No all-q coefficient census or ideal is constructed.

The incoming ordinary rectangle is a literal hypothesis. GGV Definition4.3 allows a bare 'standard' pair in K[u,u^-1,v], which is broader. General ordinary normalization and GGV Proposition5.20 may supply ordinary rectangular representatives before the actual complete chain is selected; those remain their named imported source interface, not a new theorem here. The identity or constant-v-translation in5.20 preserves a supplied rectangle, but the F2 chain is the chain of the resulting representative. We do not assert that every numerical degree pair(25m,25n), or every counterexample, selects F2. Inverse normalizing coordinates may change the original degrees. The source rectangle itself has normalized total degrees25m,25n.

The accepted minimal-map report and its two whole accepted chain parents were checked first. They supply the fixed(3,5) historical mechanism, both root forms and the rational-versus-polynomial warning. The scoped current-history search found no exact all-q F2 source arrow; this is no literature-novelty claim. The finished all-F9 argument provided bookkeeping inspiration only; its pending gate and any uniform local theorem are not premises.

## 2. Common ordinary face and the common vertical centering

The ACTUAL regular-corner source is joint: GGV1401 Definition5.5 and Corollary5.7 supply the proportional Q endpoint and weight, not merely a guessed copy of P's polygon. Thus the starting weights are5m,5n. Their expected leading bracket weight is5(m+n)-4>0, so the constant-Jacobian identity forces the leading forms to commute. GGV1401 Proposition2.1 gives a common ORDINARY root with endpoints(1,0),(5,20); the other member's starting endpoint scales by n through that same common-power identity. Thus, absorbing a nonzero root-leading scalar into alpha0,beta0,

    ell_(5,-1)(P0)=alpha0*R^m,
    ell_(5,-1)(Q0)=beta0*R^n,
    R=u*r(w), w=u*v^5,

where r is a monic quartic and r(0)!=0. This root is ordinary by the polynomial clause of the common-power result, not by using the fractional child as a source.

The selected child relation in Theorem2.20(8) is

    A1=(1,0)+(m_lambda/m)*(1/5,1).

Its second coordinate2 means selected multiplicity exactly2m in the first leading polynomial, hence exactly2 in r; the second leading polynomial has multiplicity2n. The fractional variable z=u^(1/5)*v has w=z^5, and at a nonzero root this substitution preserves multiplicity in characteristic zero. Therefore the quartic root patterns are precisely(2,1,1) and(2,2), with the selected root having multiplicity EXACTLY two. There is no zero root because r(0)!=0.

Let f(u) be the highest-v coefficient of P0, at degree20m. It has degree5m. The POLYNOMIAL Euler element supplied by GGV Theorem2.6 at(0,1) is v*a0(u), and

    20m*a0'*f-a0*f'=f.

For deg a0=d>=2 the leading factor20m*d-5m is nonzero and the left side has degree5m+d-1, impossible. A constant a0 is also impossible. Thus a0=A*u+B, with15m*A=1, and f=alpha0*(u+r0)^(5m), r0=B/A. The leading-v coefficient h of Q0 has degree5n. The full leading Jacobian row gives

    20n*f'*h-20m*f*h'=0,

so h=beta0*(u+r0)^(5n) with the SAME r0. Root multiplicities or logarithmic differentiation prove this identity over K; the shift is obtained from coefficient ratios, not chosen independently for P0,Q0.

Replace both sources by P0(u-r0,v),Q0(u-r0,v). All rectangle bounds and corners remain, and the top-v coefficients become pure powers. The whole(5,-1) face remains unchanged, because changing u to u-r0 lowers the weight of every changed monomial strictly. At u-degree5e the face inequality5i-j<=5e and the rectangle give j=20e, so the top-u coefficient is also pure and unchanged. We have not used the stronger historical affine/Roy pin normalization.

Let a!=0 be the selected double root of r, in a finite extension if necessary. Make the same diagonal source change u->a*u. It preserves all support and purity conclusions. Since

    r(a*w)=a^4*rhat(w),

the new common primitive face is u*rhat(u*v^5), the selected root is1, and the face scalars become alpha=alpha0*a^(5m), beta=beta0*a^(5n). The source Jacobian becomes c1=a*c0. These are nonzero scalar changes; no fifth-root source ramification is performed. Below write r for this normalized monic rhat.

## 3. Uniform quartic Euler classification and denominator5

Apply Theorem2.6 to the original ORDINARY normalized source at(5,-1). If its Euler element for P is E, then [mE,R]=R. Every ordinary weight4 monomial has exponents(1+k,1+5k), k>=0. Write

    mE=u*v*f(w).

Manual factored differentiation gives the exact equation

    4w*f*r' - 5w*f'*r - f*r = r.              (1)

This has RHS r, NOT r/3. The factor m has been removed, so the classification below is independent of the exponents.

At each distinct nonzero root lambda of r, division by r shows f(lambda)=0: otherwise the first term has an uncanceled simple pole. If d=deg f, the leading coefficient on the left of(1) is proportional to15-5d at degree d+4. Since r has at least two distinct roots, d>=2; degree comparison excludes d=2 and all d>3. Consequently d=3. At w=0, equation(1) gives f(0)=-1. Thus the actual Euler endpoint is(4,16)=(4/5)(5,20), for EVERY m. This obtains the reduced denominator q_E=5 directly, without importing a3/5-specific endpoint calculation or a successor assumption.

At a root lambda of r with multiplicity e, taking the finite value of(1)/r gives

    (4e-5)*lambda*f'(lambda)=1.               (2)

In particular each such root is simple in f. The following manual coefficient comparisons solve the two cases completely.

### The(2,1,1) case

Write r=(w-1)^2(w-a1)(w-b1) and f=C(w-1)(w-a1)(w-b1), where1,a1,b1 are distinct and nonzero. Equation(2) at the three roots gives

    3C(1-a1)(1-b1)=1,
    -a1*C(a1-1)(a1-b1)=1,
    -b1*C(b1-1)(b1-a1)=1.

Eliminating C yields a1(a1-b1)=3(1-b1) and its symmetric equation. Subtraction gives a1+b1=3, since a1!=b1; substitution gives a1*b1=3. The first equation then gives C=1/3. Hence

    r=(w-1)^2(w^2-3w+3),
    f=(w-1)(w^2-3w+3)/3.

These conditions verify the ENTIRE equation(1), not only its values at three points: after the root factors have removed its poles, the residual of(1)/r is a polynomial of degree at most2, and vanishes at all three distinct roots. The quadratic has discriminant-3 and neither root is0 or1 in characteristic zero.

### The(2,2) case

Write G=(w-1)(w-rho), r=G^2, and f=G(Cw+D). The finite equation is

    3w(Cw+D)G' - 5w*G*C - G(Cw+D)=1.         (3)

Put S=1+rho. Its cubic coefficient cancels identically; the quadratic, linear and constant coefficients give respectively

    5D+3SC=0,  -2SD-6rho*C=0,  -rho*D=1.

They force

    D=-1/rho,  C=(1+rho)/(3rho^2),
    (1+rho)^2=5rho, or rho^2-3rho+1=0.

Conversely these three coefficient equations verify all of(3). Both roots rho are nonzero, distinct from1, and distinct from each other. Here C!=0 as well, since rho=-1 does not satisfy the quadratic. Thus the two quartic forms are exactly

    r=(w-1)^2*h(w),
    h(w)=w^2-3w+3  OR  h(w)=(w-rho)^2,
    deg h=2, h(1)!=0.

Choosing the other double root as the selected root exchanges reciprocal golden parameters, not an omitted branch. No coefficientwise splitting over Q(rho), rational-point restriction or real-root assumption is made.

## 4. Opposite lower edges: whole intervals and every rational gap

Swap(u,v)=(y,x), obtaining P,Q in K'[x,y] with bracket -c1. The common coordinatewise dominating vertex for multiplier e is C_e=(20e,5e), unique at BOTH maximum x and maximum y. Total degrees and y-degrees have ratios m/n. The starting direction becomes d0=(-1,5), with normalized start(20,5), other endpoint(0,1), and positive value5e. Its Euler start is(16,4)=(4/5)(20,5); change the sign of the swapped Euler element to preserve the Euler identity.

Let d=(rho_d,sigma_d) be the clockwise-adjacent lower edge at these corners, taking the nearest of the two polygons. Then rho_d>0>sigma_d, and both maxima are still evaluated at C_e. At least one of P(x,0),Q(x,0) is nonconstant: otherwise their x-derivatives vanish on y=0 and so does their bracket. Ordinaryness then gives a positive d-value. Proportionality of the corners implies

    4rho_d+sigma_d>0

for BOTH members. The whole required arc from d to d0 has this common maximizing corner, and its positive cone has angle less than pi, since5rho_d+sigma_d>rho_d>0. The corner has positive value at both ends and on every intervening direction. This verifies the ENTIRE positive interval in GGV Proposition7.3/Corollary7.4; it is not an endpoint-only inference past a zero crossing.

The expected leading bracket weight is

    5(m+n)(4rho_d+sigma_d)-(rho_d+sigma_d)
       =(5(m+n)-1)(4rho_d+sigma_d)+3rho_d>0.  (4)

Thus the two faces commute. One edge cannot pair with a monomial face of positive proportional weight, by the homogeneous common-power lemma. Both therefore have an edge there.

Corollary7.4 applies with l=1, normalized start(20,5), 5<20, d0 in V_{>=0}, the positive interval just proved, both required degree ratios m/n, and q_E=5. It gives a5e-th power face root with endpoint(4,1), hence y-degree1. At the FIRST cut a Laurent root of an ordinary positive power is itself ordinary, since its minimal x-exponent multiplies by that power. Consequently the root has two terms and can be written

    a2*x^4*y+b2*x^(4-k),  a2*b2!=0,

where k is an INTEGER and d=(1,-k). Positivity gives k<4. The ordinary lower-side Proposition2.1 of1605, including its slope-one corollary, applies to the endpoint20e>5e>0 and gives k>1. Its statement is for a polynomial Jacobian pair, not restricted to global minimality. Thus k is2 or3.

Both members have the same nonzero root lambda_k of x^k*y-lambda_k by commutation/common powers. It is obtained from the next coefficient of a monic y-polynomial by division by5e, so it descends to the current coefficient field. Apply the same Laurent cut y->y+lambda_k*x^-k to both. The face collapses to the single corner; d0 is unchanged because k<5. Total degree and y-degree ratios and their unique maximizing corner remain unchanged: a changed term has exponents(i-kt,j-t), and total degree decreases by(k+1)t.

The Euler denominator persists after any such cut. The common d0 root is R0=y*r(x^5*y), with ord_y R0=1. Two weight4 Euler elements differ by a commuting weight4 Z. If Z!=0, Proposition2.1 gives Z^5=constant*R0^4, contrary to5ord_y Z=4 in K'[x,x^-1,y]. Thus the actual constructed Euler solution is unique at this face, including after the cuts. We do not apply Proposition2.11's positive-rho hypothesis to the negative-rho direction d0.

If the new clockwise-adjacent edge, again chosen nearest in the union of the two polygons, has rational slope kappa<4, its value is5e(4-kappa)>0. The common-corner argument again supplies positivity on the WHOLE interval to d0; equation(4) gives a common edge; Corollary7.4 gives a y-linear root with integer x-exponents and endpoint(4,1). Therefore kappa is an integer. It is strictly larger than the removed slope. The only remaining possibility after2 is3, and none remains below4 after3. This excludes ALL intermediate rational slopes, not merely a sampled integer list. At most two cuts suffice; write absent parameters as zero, obtaining a common sum lambda2*x^-2+lambda3*x^-3.

At the next lower edge of that union, kappa>=4. Both members still attain their support value at C_e, even if only one has an edge there. For EVERY support point(i,j), the supporting inequality and j<=5e give

    i-20e<=kappa*(j-5e)<=4*(j-5e).

Hence i<=4j throughout each entire polynomial. Equality is attained at C_e. No corollary is applied to the zero-valued boundary kappa=4, and it is not claimed absent. We have reached

    j>=0,  i<=4j,  -i+5j<=5e.                (5)

## 5. One selected upper cut, then stop and transport the entire pair

The selected root was normalized to1. Apply exactly the common cut y->y+x^-5. It changes the common d0 face root to

    R0'=(y+x^-5)*(x^5*y)^2*h(1+x^5*y).

All terms have d0-weight5; therefore the whole leading faces of the pair are alpha*(R0')^m and beta*(R0')^n. Since h(1)!=0, the least-y endpoint is exactly(5,2), not a further multiple root. No successor classification is required.

This upper cut PRESERVES the full bounds(5). On a changed term(i,j)->(i-5t,j-t), j-t remains nonnegative, i-4j decreases by t, and -i+5j is unchanged. Thus(5) remains true for the ENTIRE pair P1,Q1. Their bracket is still -c1. Stop at this stage: there is no later x^-3 or other upper cut in this proof.

Now use the unramified Laurent map

    T4: x=g^-1, y=g^4*p.

Its literal exponent map is(I,J)=(4j-i,j). By(5), I,J>=0 and I+J=-i+5j<=5e. Thus T4(P1),T4(Q1) are ORDINARY polynomials. This proves every negative-power cancellation obligation by full support containment before substitution, not by assuming the displayed top is polynomial.

At the top face the degree-five factor is

    T4(R0')=p^2(p+g)*[g^2*h(1+p/g)].

For h(w)=w^2-3w+3, this is

    p^2(p+g)(p^2-gp+g^2)=p^2(p^3+g^3).

For h(w)=(w-rho)^2 it is

    p^2(p+g)(p+(1-rho)g)^2.

These are ordinary, homogeneous degree-five polynomials, monic in p. The golden relation gives(1-rho)^2=rho!=0. The top forms are alpha*H^m,beta*H^n, with nonzero scalars; consequently total degrees are exactly5m,5n. This is precisely the requested pair of top patterns. It is not a claim that the top is a unique monomial or that its lower support is one of the old(3,5) polygons.

The coordinate Jacobian of T4 is -g^2. The earlier swap had determinant-1, while all cuts have determinant1. Relative to the original pair the entire rational coordinate map is explicitly

    u=a*(g^4*p+lambda2*g^2+lambda3*g^3+g^5)-r0,
    v=g^-1.                                  (6)

Its determinant is a*g^2: u_p=a*g^4, v_g=-g^-2, v_p=0. Therefore the unscaled final bracket is a*c0*g^2=c1*g^2, with the displayed positive sign. Dividing the two outputs by alpha and beta makes their entire tops H^m,H^n and gives

    c=c1/(alpha*beta)!=0.

Equivalently alpha=alpha0*a^(5m), beta=beta0*a^(5n). No arbitrary additional gauge has been imposed. If one merely checks the old optional total-homogeneous scaling, its correct general transformation is c->c*tau^(4-5(m+n)), not the fixed exponent-36 except when(m,n)=(3,5). This proof does not adopt a c=1 gauge.

## 6. Field, source-coverage and reverse limits

The initial selected quartic root a may require a finite algebraic extension. The common vertical shift r0 and every available lower cut are coefficient ratios in the then-current field. No choice of a fifth root is needed for the actual polynomial receiver map: the fifth-root child is used only to READ its selected multiplicity; the map itself is the integral Laurent map(6). The golden case is over a genuine coefficient field containing rho, retaining both embeddings. It is not encoded by splitting an equation into separate rational coefficients, and no K-rational-point requirement is introduced.

The table's family parameter is nonnegative, as GGHV Section3 Definition3.3 and(3.20) specify. The direct mapping proof works for every such q and uses no finite parameter cutoff. It starts with an actual ordinary rectangular representative supplying the named chain. It does not prove a fresh given-pair normalization or an all-degree selection into that chain. For general characteristic-zero original coefficients, the accepted complex normalization interfaces may first embed a finitely generated coefficient field into C; their chosen normalizer is not asserted to descend to the original K.

The inverse of(6) is rational. Arbitrary ordinary receivers with these tops and bracket c*g^2 need not return an ordinary Keller source under inverse substitutions. No reverse-lift theorem, full finite ideal, unit/properness certificate, source point or family exclusion follows from this necessary arrow alone. In particular this report does not consume or endorse a pending uniform degree-five local obstruction. It does not assert global JC2 coverage or same-numerical-degree-to-F2 selection.

## 7. Exact scope controls and remaining obligations

All controls below are manual, not executed tests or full-source points.

- Without the rectangle, adding u^(5m-1)*v^(20m+1) preserves the maximal-u corner and total degree25m, and is below the starting face by6 units, but breaks the highest-v coefficient bound needed for common centering. This is NOT a Keller-preserving mutation; it shows why endpoint/degree metadata alone is insufficient.
- In the quartic Euler equation normalized by mE, RHS is1 after division by r. Keeping the historical1/3 while allowing arbitrary m would misnormalize E. The explicit equations above determine the root patterns without that error.
- Replacing the post-cut integer x-lattice by fractional powers would permit x^4*y+x^(4-kappa) for noninteger kappa between the cuts. The integer-gap argument would fail precisely there. This is why the original source, not its L^(5) child, is retained.
- A later cut y->y+mu*x^-3 need not preserve i<=4j: the individual boundary monomial x^4*y acquires mu*x outside that half-plane. Stopping immediately after the x^-5 cut is load-bearing. This small support control is not a full Keller pair.
- The monomial-J pair(g,g^2*p) has bracket g^2, but its T4 inverse has first coordinate x^-1 and is not ordinary. It does not have the required large top forms and refutes no stronger guarded reverse theorem; it only prevents treating a monomial-J equation itself as a sufficient source certificate.

The exact new conclusion is the requested ALL-q necessary polynomial receiver/top-form arrow at the stated ordinary rectangular actual-F2 scope. No exponent-dependent obstruction appears before this stopping stage. The stronger all-q inner-polygon classification, arbitrary bare-Laurent standard scope, same-degree F2 selection, reverse sufficiency and a local receiver exclusion remain outside this report.

## 8. Sources, checksum and publication

Fresh hashes preceded WHOLE reads of:

- minimal map7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413;
- accepted chain producer9b439af269c23e349615d3e404e0732c9c7f491a9342d5500e061aab91ad4e88;
- accepted chain review5be50d001d285481233c8de415b2f4d22411a22cb930a0c1db287c0579b3cd7b.

Named primary imports are GGV1401v3 common powers, polynomial Euler element and opposite-edge Corollary7.4/Proposition7.3; ordinary lower-side1605v2 Proposition2.1 and its corollary; and GGHV1708v1 actual-chain/multiplicity and printed F2 family. The mirrored corollary and general normalization/census machinery are external-theorem inputs, not independently reimplemented foundations. The proof here independently supplies every changed all-exponent support, positivity, ODE, scaling and ordinaryness calculation. Proposition8.2 and the old unequal-endpoint enumeration are not premises.

Exact full-file pins, selected primary read scope and honest history perimeter are in the owned input-pins.json and READ-SCOPE.md. No code checker, CAS, source power, polynomial pair expansion, solver, AWS/SSH or mathematical subprocess was run. No existing artifact or canonical file was modified. This is a terminal UNREVIEWED source proof pending independent review, not a new promoted campaign result or raised item.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `21714`.
- Body SHA-256:
  `1371c1b34d59c2b86797b187f3f2e1508485bf21c6d8a8ebb8b2545338068c94`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
