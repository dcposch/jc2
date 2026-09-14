# Independent nodal-chart audit

Only named frozen inputs were read. This note supplies exact proofs and counts, not a nilpotence decision.

## Diagonal and first transverse coefficient

Let epsilon=+1 for degree99 and epsilon=−1 for degree108. Let X=G+(a+b²/4)/3, Y=epsilon*(F−(bG+c)/2), j=J(X,Y)=−epsilon*C. Complete the target cubic to R=X³+pX+q−Y². The major actual face gives X(x,x) monic quadratic and Y(x,x) monic cubic, and deg R(x,x)≤1. If X(x,x)=x²+l*x+d, put u=x+l/2, so x=u−l/2. Write X0=u²+B. Cancellation of degrees5,4,3,2 gives Y0=u³+(3/2)B*u, p=−3B²/4; its degree1 residual is identically zero. R0=q+B³/4. The coefficient map adjoining l (or l/2) is polynomial and invertible; this is translation of the diagonal parameter, not another source gauge. The minor normalized arcs must be transformed too if one physically changes x.

With z=y−x, dx∧dy=du∧dz. Write X=sum Xk(u)z^k, Y=sum Yk(u)z^k. Coefficient z^r of J(X,Y)=j gives

(r+1)(2u*Y[r+1]−(3u²+3B/2)*X[r+1]) + S_r = j*delta[r,0],

S_r=sum_{a+b=r+1,a≥1,b≥1}(b*X_a'*Y_b−a*X_a*Y_b').

Thus H_r=(j*delta[r,0]−S_r)/(r+1). Over Q[B,B^−1,j,...][u], every polynomial solution is uniquely

X[r+1]=−2H_r(0)/(3B)+2u*A_r,
Y[r+1]=(H_r+(3u²+3B/2)*(-2H_r(0)/(3B)))/(2u)+(3u²+3B/2)*A_r.

The numerator is divisible by u in the polynomial ring; u is not inverted. Conversely A_r=(X[r+1]−X[r+1](0))/(2u). The exclusion of B=0 is legitimate for constant nonzero j: both X0' and Y0' vanish at u=0, so evaluation of the zeroth Jacobian row forces j=0 there. Algebraically the zeroth equation modulo B evaluated at u=0 is j. After j is inverted, B is a unit (its inverse follows from the same row).

At r=0,
X1=−2j/(3B)+2u*A0,
Y1=−j*u/B+(3u²+3B/2)*A0,
and direct multiplication gives R1=−j*(u²+3B/2). Therefore [u²z]R=−j=epsilon*C, with the desired opposite client signs. Since u differs from x by a scalar, [x²z]R1=[u²z]R1.

The full finite recurrence requires all out-of-support coefficients vanish, all strips after polynomial termination vanish, and all residual Jacobian coefficients through z-degree n+m−1 vanish. Imposing only the displayed recursive solvability equations before termination does not give a polynomial solution. Each eliminated X/Y coefficient has the stated inverse map, but the final quotient equivalence requires every transported boundary/tower/characteristic equation and the termination rows.

## Exact two-boundary affine chart (before nonlinear recurrence)

Fix n and write K(t,w)=t^n P(t^−1,w/t)=sum_{r=0}^n t^r K_r(w), deg K_r≤n−r. K0 is the full fixed source top polynomial. The major direction is w=1 and the minor direction is w=b(t)+pi*t^gamma, with b(0)=0. For delta52, work in the cover t=s²; b(t) remains polynomial in t. For D108, retain the free mean in the leading minor target; do not center it.

At each r≥1 the full major floor INCLUDING its equality face prescribes the Taylor coefficients at w=1 for degrees0≤k<a_r. The full minor floor INCLUDING its equality target prescribes the coefficients at w=0 for degrees0≤k<b_r, after subtracting expressions in the already reconstructed K_i, i<r. This is because substitution w=W+b(t) is triangular in t with diagonal identity. The equality rows subtract the entire actual target, including its lower coefficients.

Multiplicities:
* 99 F/G major: a_r=max(0,floor((288/192−3r)/4)+1).
* 108 F/G major: a_r=max(0,floor((420/280−4r)/5)+1).
* delta2 F/G minor: b_r=max(0,floor((81/54−r)/3)+1).
* delta52 F/G minor: b_r=max(0,floor((189/126−2r)/7)+1).
* 108 F/G minor: b_r=max(0,floor((96/64−r)/4)+1).

For every r≥1, a_r+b_r≤n−r+1. At r=0 the supplied full top gives the known compatibility between the two leading monic targets; it is not set to zero.

An exact rational Hermite chart is as follows. Let M_r(w−1) be the prescribed major Taylor polynomial of degree<a_r, and N_r(w) the prescribed minor Taylor polynomial of degree<b_r after subtraction of lower bands. Define

S_r = ((N_r−M_r)*(w−1)^(-a_r)) mod w^b_r,
K_r = M_r+(w−1)^a_r*S_r+w^b_r*(w−1)^a_r*E_r,
deg E_r < n−r+1−a_r−b_r.

The inverse of (w−1)^a modulo w^b exists over Z because its constant coefficient is ±1; its coefficients are explicit signed binomial coefficients. There is no center, separation, B, j, or pivot-minor denominator. This gives a polynomial two-way coefficient map over Q[all minor centers, separation], with inverse exact division by w^b(w−1)^a. Its generator order may be r increasing, then E_r monomial exponent increasing; physical variables t,w are absent after extraction.

The exact numbers of free E coefficients after BOTH complete boundary conditions, with physical top fixed, are:

| client | F ambient lower | F rows | F free | G ambient lower | G rows | G free | pair free |
|---|---:|---:|---:|---:|---:|---:|---:|
|99 delta2|4950|4614|336|2211|2065|146|482|
|99 delta52|4950|4796|154|2211|2146|65|219|
|108 free mean|5886|5631|255|2628|2518|110|365|

These do not count minor center/separation variables, characteristic target scalar variables, B or j as extra parameters. Max free widths per t-band for F/G are7/5,4/2,5/3 respectively. These numbers are exact across all center/separation strata: they use only confluent Hermite interpolation at0 and1 with unit difference. They are not counts AFTER eliminating the nonlinear Jacobian recurrence, and must not be described that way. D1 and tower conditions must additionally be transported; these tables describe the full two-boundary F/G necessary enlargement only.

## Raw major-strip recurrence parameter count

For X=G+constant and Y=epsilon*(F−bG/2−constant), the major and total-degree caps in z^k are

dX(k)=min(m−k,2+floor(k/L)), dY(k)=min(n−k,3+floor(k/L)),

L=3 or4. A_{k−1} has degree≤min(dX(k)−1,dY(k)−2) where both are supported; if this is negative it has no free coefficients, but compatibility rows remain. Enumerating k≥1 gives625 A coefficients for99,610 for108, maximum A degree17/15. These are counts before the other boundary constraints and characteristic/tower rows. The ODE matrix of dimension17/22 does not by itself decide the full localized chart. The two-boundary counts482/219/365 and recurrence counts625/610 are different presentations at different elimination stages, so none can be subtracted from the others as a proven final nonlinear count.

## Typing

A proper ODE face ideal (and likewise a proper two-boundary affine chart) is not a proof that the complete necessary chart is proper. Only a complete localized ideal or an exact witness satisfying every specified generator licenses an existential necessary-chart survivor. For full necessary ideal I, D(s) empty iff s belongs sqrt(I) iff I+(zs−1) is unit. Proper localization has the opposite conclusion s nonnilpotent. No nilpotence or properness of the complete chart is established in this note.

## D108 complete tower row formulas and source derivation

Use physical h3 monic degree9 with top y²(y−x)^7 and h2 monic degree36 with top y⁸(y−x)^28. The canonical identity is h2=h3⁴+C2*h3²+C3*h3+C4, deg_y Ci<9 and total degree Ci≤9i−1 (i=2,3,4); the missing cubic-root-power coefficient is the approximate-root definition. Normalize Ci by t^(9i). At D2, weight4r+5q floors are35i, namely70,105,140. The h3 and h2 floors are35 and140. The equality h3 polynomial is H=pi⁷+kappa*pi³, while h2face=(pi⁴−1)^7. The Ci equality spaces are U=span(pi⁶,pi²), V=span(pi⁵,pi), W=span(pi⁸,pi⁴,1); comparing pi²⁴ in H⁴+U*H²+V*H+W derives kappa=−7/4. No h3/Ci D1 floor is licensed by another transfer.

For the D1 radius, the selected21-root F child gives physical F order −3+21*(delta1−1/4). Printed Prop4.6(3), r=1, and Def5.1(4) give contact order108*(delta1−1)/(108−(−72))=(3/5)*(delta1−1). Equating yields delta1=3/8. (The transport-proof agent independently checked this printed-source calculation.) Thus use t=e⁸ and normalized z=e¹⁰+Pi*e¹¹, i.e. physical x=e⁻⁸,y=e⁻⁸+e²+Pi*e³. Physical F/G/h2 orders are−3/8,−1/4,−1/8; normalized h2 floor is287. The h2 child has multiplicity7=21/3, not divisible by4, so no additional fourth approximate-root transfer at D1 follows.

For outer F=h2³+A2*h2+A3 and G=h2²+B1*h2+B2, all block y-degrees are below36, and actual total degree normalizers D=(71,107,35,71). D2 floors are(276,416,136,276); D1 floors are(566,853,279,566). The latter exact numbers also appear explicitly in the frozen cone-vertex report. D1 equations at normalized weightW=4r+5q are the binomial moment rows sum binom(q,k)c_(r,q)=0 for2W+k strictly below the block threshold. The inherited equality face disappears only after those rows prove it, not by a floor alone.

For minor physical y=j0+u*t+v*t²+pi*t³, retain the free mean mu in target T=((pi−mu)²−c), with c nonzero. The h3 normalized floor8 has whole target−T; h2 floor32 has whole targetT⁴; F/G floors96/64 have targetsT¹²/T⁸. Normalized Ci floors are8i=(16,24,32). Outer actual-normalizer minor floors are(63,95,31,63), corresponding to effective whole-expression floors(64,96,32,64). Remainder equations are strict-below only, with equality coefficients left free. Centre translations transport the full arc and mu; they do not allow an arbitrary mu=0 restriction.

The rational canonical-root inverse is finite: recursively solve the top y coefficients of F=h2³+lower h2 powers for the unique monic h2, then solve those of h2=h3^L+lower h3 powers for unique monic h3 (L=3/4). Polynomial division by these monic roots recovers every remainder. Thus rawF/G to the tower uses only rational denominators3 andL. The exact source chart is recovered only after pulling back all the listed degree/support/face/D1/minor equations. Keeping merely rawF/G two-boundary conditions is a necessary enlargement, even though the coefficient coordinate operations themselves are bijective.

## The diagonal does not alone eliminate raw F/G coefficients

The boundary chart permits five scalar diagonal coefficients: G0=x²+g1*x+g0, epsilon*F0=x³+f2*x²+f1*x+f0. The upper-degree condition on R0 solves four target constants a,b,c,d (the cancellation degrees5,4,3,2); e0 stays free. The nodal lemma therefore replaces diagonal coordinates and target constants; it need not remove any of the raw F/G affine dimensions482/219/365. Counting five diagonal equalities as five new independent raw-pair eliminations would overstate compression.

## Review of recurrence_stream.py and exact_controls.py

The reviewed recurrence has k=r+1. Its residual method computes H_{k−1}=−(S−j*delta[k,1])/k with exactly the cross terms1≤i,b≤k−1. The X/Y support caps and A count are correct. For dx<0, it emits H(0)=0 before dropping X entirely. For dx≥0, dropping the constant term of H+(3u²+3B/2)*a is exact modulo B*Binv−1. Y overflow rows are retained before truncation, so reconstruction preserves the original equations modulo those rows. The terminal range k=n+1,...,n+m−1 represents Jacobian powers n,...,n+m−2. No further power is missing: the possible z^(n+m−1) term vanishes identically because X_m,Y_n are constants in u. The characteristic support cap min(D2−k,floor((k+2d−1)/d)) is correct, and powers through3m=2n cover the whole polynomial. Syntactically nonzero circuit rows can represent zero polynomials; row counts are not ranks.

The current routine is a recurrence presentation until physical source scalars are restored: G(x,y)=X(x+h,y−x)−A0/3, F(x,y)=epsilon*Y(x+h,y−x)+(bG(x,y)+c)/2, with h,A0,b,c retained. The full target inverse determines a,d,e0 from A0,p,q,b,c. Every boundary, D1, tower and characteristic row then pulls back through this map. Restoring these scalars is not a new gauge.

There are immediate exact rational coordinate eliminations available because [u^i]X_k=2*A_(k−1,i−1) for i≥1. In99 the G major face fixes16 A coefficients, and its homogeneous top (u+z)^18*z^48 fixes18, with one overlap, so33 distinct variables are direct pivots. For108 the corresponding numbers are14 and16 with one overlap, giving29. This reduces the presentation counts625→592 and610→581 before other transported rows. The k=m top constant has no A coefficient; retain its compatibility equation. No conclusion about algebraic dimension follows.

One exact way to combine the boundary and recurrence maps is to adjoin Hermite E coordinates, impose every physical coefficient agreement, and eliminate E monically using the proved inverse Hermite map. This leaves the A presentation with all boundary residual equations imposed. Counting these remaining A generators is valid as a presentation count, but must not be advertised as the dimension or as the result of exhaustive minor-boundary rational pivoting. Such further pivots can have coefficients depending on A0 or j/B and need localization/stratum analysis.
