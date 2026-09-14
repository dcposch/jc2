# Supported monic quotient: repaired proof with all lower centres

This is an additional exact reduction, not a unit/properness verdict. It uses the complete actual minor R face and its floor, licensed only on the negative-order distribution-detector minor discs. It does not follow from the total degree of R alone.

Write z=y−x. Source major/minor valuations are measured by the normalized covers, so the corresponding integer negative pole bounds (vM,vN) are:

| client | major(lM,wM) | minor(lN,wN) | G(vM,vN) | R(vM,vN) | H difference |
|---|---|---|---|---|---|
|99 delta2|(3,4)|(1,3)|(6,12)|(5,10)|(1,2)|
|99 delta52|(3,4)|(2,7)|(6,6)|(5,5)|(1,1)|
|108 free mean|(4,5)|(1,4)|(8,8)|(7,7)|(1,1)|

Here l weights normalized t and w weights the transverse variable. The minor centre polynomial is retained as b(t)=j0*t+u*t²+v*t³; the at-level shift can be included in b for delta2, while the 108 free mean remains in the full minor target. All centre variables stay arbitrary.

The R whole minor faces are lambda*P^5 for99, with P=zeta²(zeta+3rho) or pi(pi²−c), and −lambda*T^7 for108, with T=(pi−mu)²−c. Prop6.1(2), printed pp.190–193, applies because the principal minor factor multiplicities3 and2 satisfy3<11/2 and2<9/2 and the physical F orders−18,−9/2,−12 are negative. Definition3.1(3),(4), p.161, supplies the5/9 or7/12 distribution ratios. The scalar is fixed by the entire homogeneous top: [x^40*y^15]R=lambda in99 and [x^49*y^14]R=−lambda in108. These are uniquely the largest minor-face pi coefficients under the total degree bounds. This minor licence was independently checked by the transport-proof agent against the print. Their physical actual-normalizer depths are45,105 (double cover),56, respectively. Major R faces are Pmajor*q from the already checked characteristic transport.

Work over any commutative Q-algebra A in which lambda is invertible and all the stated floor/face equations hold. The following coefficient identities are polynomial identities over that localized coefficient algebra; neither a field nor reducedness of A is required.

**Supported lifting lemma.** For each D=0,...,11 in99, or D=0,...,9 in108, every homogeneous degree-D polynomial satisfying the two leading direction multiplicities has a polynomial lift of degree at most D satisfying BOTH full valuation floors, with exactly the same highest homogeneous part. Put

 a_r=max(0,ceil((lM*(D−r)−vH_M)/wM)),
 b_r=max(0,ceil((lN*(D−r)−vH_N)/wN)), 0<=r<=D.

The exact finite check in h_quotient_preflight.py proves a_r+b_r<=D−r+1 at every one of these entries. Given the homogeneous leading coefficient polynomial K0(w), recursively reconstruct K_r(w) of degree<=D−r with prescribed Taylor jets at w=1 and w=0. The minor jet is the negative contribution from earlier K_i under w=W+b(t). This substitution is t-triangular with diagonal identity. The inverse of (w−1)^a modulo w^b has integral coefficients, so Hermite interpolation gives a lift over Q[j0,u,v] without dividing by any centre or separation. Set the optional lower free coefficients to zero to define one lift. The supplied script constructs each allowed leading basis element and checks EVERY original major and minor strict-floor row symbolically over Q[j0,u,v].

The degree-filtered supported basis degrees are:

* delta2:0,1,2,3,4,5,7,8,11;
* delta52:0,3,4,7,11;
* 108:0,1,4,5,9.

Thus the relevant supported spaces have dimensions9,5,5 over the centre coefficient ring before their equality faces are fixed. This is not a generic-rank statement: the interpolation pivots are units for every centre specialization.

**Division theorem.** There exist unique polynomials H,S with

 lambda*G=H*R+S, deg(H)<=11/9, deg(S)<55/63,

and H satisfies the difference valuation floors in the table. In particular this is the ordinary monic division by R in y, with a stronger TOTAL-degree remainder bound.

Proof: let E be the current residual, initially lambda*G. Suppose its highest total degree N is at least D_R=55/63. Its full valuation bounds force its highest homogeneous part E_N to be divisible by (y−x)^a*y^b, where

 a=ceil((lM*N−vG_M)/wM), b=ceil((lN*N−vG_N)/wN).

The argument for the minor multiplicity is coefficientwise: the lowest coefficient at each generic pi power receives its contribution from the highest homogeneous band before any positive-depth band; lower centres have positive t order. At N>=D_R, these a,b are at least40,15 for99 or49,14 for108, so E_N is divisible by the full homogeneous R top lambda*y^15*z^40 or lambda*y^14*z^49. Let Q_D=E_N/R_top, D=N−D_R. Because wM*a_R=lM*D_R−vR_M and wN*b_R=lN*D_R−vR_N are exact equalities, its two multiplicities are precisely the permitted H leading bounds. Apply the supported lifting lemma to Q_D and subtract the FULL supported lift times R from E. This preserves both valuation floors and strictly lowers total degree. Repeat until deg E<D_R. Summing the supported lifts gives H; E gives S. Since R has invertible scalar y-leader and deg_y S<D_R, uniqueness of monic division identifies these polynomials with the ordinary quotient and remainder.

This repair is essential: subtracting just Q_D*R need not preserve the minor floor when lower centres are nonzero. For instance xy−u can have a higher valuation than its homogeneous part xy along y=u/x+... . The proof above explicitly uses a full Hermite lift instead.

**Whole face determination and small H chart.** The total-degree remainder bound forces the major S face degree at most39/48 in pi, strictly below the R face degree40/49. Therefore ordinary polynomial division of the known G/R faces gives

 H99_major=pi²*(9*pi⁶−24*pi³+20)/9,
 H108_major=pi³*(4*pi⁴−7)/4.

At the minor cover the S face degree is at most14/13, below the R face degree15/14. Hence the whole H minor face is P in99 and −T in108, and the S minor equality face vanishes. No leading equality coefficient is replaced by zero in this derivation; the quotient is obtained by subtracting the complete target.

The exact symbolic linear map in h_quotient_preflight.py imposes both full H faces on the supported bases, retaining all centres and rho/c/mu. The remaining H coefficient counts are3,1,1 for delta2,delta52,108. These counts exclude the centre and separation parameters. The count1 coordinate in delta52/108 is the constant polynomial basis coefficient. Every face row is substituted back exactly. The driver additionally extracts and verifies a nonzero rational square pivot determinant, so this affine count holds on every centre/separation stratum, not merely over their fraction field. No chart coefficient is silently normalized and the h3 constant is not spent as a gauge.

The canonical h3 has the same two-boundary faces once the necessary inner minor remainder equations impose the corrected equality coefficient20/9 in99. Therefore, in delta52 and108, H−h3 is a scalar on this fully constrained source chart. This is equality of a quotient with a canonical auxiliary polynomial UP TO a scalar, not an identification by matching names. Recovering or solving that scalar still requires the canonical-root map.

**Limit.** The major face of S has constant coefficient lambda (after the stated normalization), whereas its minor floor is strictly better than G's. This does not force S=0 or lambda=0: the physical monomial x² has the required major equality and satisfies the improved minor lower bound on all three clients. The reduction has not decided the full localized ideal, and no new branch exclusion or necessary-chart survivor follows from H chart properness alone.

**Coefficient maps.** Let B0 be Q[all minor centres, rho/c, mu where relevant, lambda, lambda_inverse]/(lambda*lambda_inverse−1), with separation subsequently localized exactly as in the source chart. Let A_GR be its polynomial coefficient ring for the full degree-bounded G,R, modulo both complete support/face systems. Adjoin the finite division coefficients H,S with equations lambda*G−H*R−S=0, the degree bounds above, and the supported-lift consequences. Monic division and the theorem eliminate H,S uniquely from A_GR. Conversely, the coefficient map G↦lambda_inverse*(H*R+S), R↦R reconstructs A_GR from H,R,S when the original rows are pulled back; the two compositions are the identity modulo the declared coefficient equations. Thus no equality of names substitutes for the map. The full tower, nodal, Jacobian and characteristic equations must still be pulled back through it. Adding their images preserves the same quotient isomorphism, but neither their consistency nor a radical membership decision follows from the small H parameter count.

The reverse-division diagnostic in delta52 has a concrete non-obstruction control, checked in the adjacent driver. Set j0=u=v=0,c=1,C=1,lambda=−243/455, and write z=y−x. Then

 H=y³*z⁸−(8/3)*y²*z⁵+y*z³+(20/9)*y*z²,
 T=(262236/597051)*x*y³*z⁷−(706612/597051)*y³*z⁴+y²*z.

H has both forced quotient faces. T has total degree11, y-degree10, major face equal to the exact polynomial remainder of R_major/H_major, and minor cover valuation at least−4. All four cover assertions are checked by exact Laurent substitution after multiplying by the stated valuation normalizer. This is a witness for the H/reverse-remainder FACE CONTROL ONLY. It does not satisfy or certify the complete necessary chart and supplies no properness conclusion for that chart.
