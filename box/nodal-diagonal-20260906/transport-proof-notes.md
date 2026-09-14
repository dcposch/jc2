# Transport and nodal coefficient-map audit (frozen inputs only)

Hash audit was completed by the root agent before this subtask. Read sources: frozen ideation, char-degree instrument, corrected g9966 engine, joint-chart report, and printed Moh PDF. Page 170/171 formulas were visually checked against the print. No other ideation source was consulted.

## 1. Printed source and argument order

Work in characteristic zero. Physical variables are x,y. Moh's formal first target f is engine G (degree m), and formal second target g is engine F (degree n). Declare specialization

  psi: K[x][U,V] -> K[U,V], x -> 0, U -> U, V -> V,

and afterward evaluation

  ev: K[U,V] -> K[x,y], U -> G(x,y), V -> F(x,y).

Specializing the target coefficient x is not specializing physical x after evaluation. Prop 2.2 pp152–154 gives deg_y T_i^psi(G,F)=-mu_i when M_i<=e, with a scalar unit leader when M_i<e. The proof p154 explicitly uses monic to mean a unit leader. Here e=n-1 and M2=77<98 /81<107. Prop3.1 p157, its specialization remark p159, and n1=3 give the complete family

  R=G^3-F^2+aG^2+bFG+cF+dG+e0.

The permitted lower weights are 0,m,2m,n,n+m; equality weight 3m=2n has unique term -F^2. Preserve all five lower target constants. If two such family representatives both have total degree <=D2<m, their difference has successively distinct possible highest degrees n+m,2m,n,m>D2, so b,a,c,d agree. They differ only by a constant; hence every negative face agrees with the canonical representative. Characteristic lambda is a free scalar leader, not fixed to 1.

The total-degree and complete top targets are supplied by the charged char-degree proof via Prop4.5 p169 and its root-order argument p172:

  99: deg R=55, R55=lambda*y15*(y-x)40;
  108: deg R=63, R63=lambda*y14*(y-x)49.

Prop2.2 alone proves y-degree, not this total-degree conclusion.

## 2. Detector hypotheses and covers

To avoid conflating printed scale lambda with leader lambda, write ell for the scale. At the actual D2 major disc, Def5.1(4) p179 explicitly requires every hypothesis of Prop4.6. For r=2 the numeric tuples (n,d_r,M_r,-mu_r,delta,ell,v) are

  (99,33,77,55,1/3,-1/33,24),
  (108,36,81,63,1/4,-1/36,28).

The earlier scale inequality for i=1 holds against -2/495 /-1/240. Conditions (4),(5) have face degrees F=72/84 and R=40/49. Prop4.6(2) gives R-face P*q with exponent (-mu_r+M_r-n)/d_r=1 and deg q=v(n-M_r)/d_r=16/21. Actual F/G D2 faces are P^3/P^2, where

  d=3,k=8,P=(pi^3-1)^8, or d=4,k=7,P=(pi^4-1)^7.

Their actualness uses the charged source outer-equality rank argument; a valuation floor by itself would not supply them. Prop4.6 is not an unconditional theorem about all abstract upper-degree chart points.

Use the injective K-algebra map

  chi_d: K[x,y] -> K[pi][s,s^-1], x -> s^-d, y -> s^-d+pi*s.

Here z=y-x maps to pi*s, so distinct x^i z^k map to pi^k s^(k-di) and cannot cancel. The source determinant is J_(s,pi)(x,y)=-d*s^-d. Physical valuations are F=-3d, G=-2d, R=-(2d-1).

The p171 modified-Jacobian Remark explicitly treats J_(x,y)(f,g)=x^l and changes the scale numerator to -1-l+delta. It does not silently normalize engine C=J(F,G) a second time. For arbitrary nonzero scalar C, the same printed chain-rule proof is simply multiplied by C; no coordinate gauge is needed. Remember J(G,F)=-C in Moh argument order.

## 3. Exact transport identity and signs

In K[x,y] directly,

  J(F,R)=(3G^2+2aG+bF+d) C.

After chi_d, the s^-5d coefficient is

  -3d P^4 q' + 3(d-1)P^3 P' q = -3d C P^4.

Cancel the nonzero polynomial P^3 (over the coefficient field; the resulting polynomial equation is imposed directly on universal coordinates). With N=k(d-1), this is

  (pi^d-1) q' - N*pi^(d-1) q = C*(pi^d-1).

The two exact solutions are

  q99/C=pi-4pi4+(48/7)pi7-(216/35)pi10+(1296/455)pi13-(243/455)pi16,
  q108/C=pi-(21/5)pi5+(112/15)pi9-(448/65)pi13+(3584/1105)pi17-(2048/3315)pi21.

Substitution was rerun in SymPy over Q. Full coefficient matrices are 19x17 rank17 and25x22 rank22: at most22 unknown columns, not literally a full square matrix with both dimensions<=22. Select independent square rows then verify every omitted row if claiming a 17/22 square solve. A homogeneous polynomial solution would be a scalar multiple of (pi^d-1)^(N/d), with fractional root multiplicities16/3 or21/4, hence must vanish. A solution of degree>N is impossible by its leading coefficient. The displayed polynomial is therefore unique without a guessed cutoff.

Highest face coefficients are lambda=-243 C/455 and lambda=-2048 C/3315. The coefficient pi^1 in chi_d(R)'s leading face comes only from x^2 z. Since P(0)=(-1)^k,

  e=[x^2(y-x)]R = C = -455 lambda/243 (99),
  e=[x^2(y-x)]R = -C = 3315 lambda/2048 (108).

Ambient normalization puts this degree3 monomial at198-3=195 /216-3=213; actual-degree normalization puts it at55-3=52 /63-3=60. Transverse order1 does not change the old band-depth thresholds143/153 or constant-Jacobian depths163/178.

## 4. Target automorphism and diagonal lemma

Set A=a+b²/4, Btar=d+bc/2, Etar=e0+c²/4. The polynomial parameter-ring isomorphism is

  (a,b,c,d,e0) <-> (A,b,c,p,q),
  p=Btar-A²/3, q=Etar-A*Btar/3+2A³/27,
  a=A-b²/4, d=p+A²/3-bc/2,
  e0=q+A*p/3+A³/27-c²/4.

For epsilon=(-1)^k=+1/-1, the target polynomial automorphism over this parameter ring is

  X=G+A/3, Y=epsilon*(F-(bG+c)/2),
  G=X-A/3, F=epsilon*Y+(b*(X-A/3)+c)/2.

It gives R=X³+pX+q-Y² and j=J(X,Y)=-epsilon*C. This polynomial identity was checked exactly. It is a change of target presentation, retaining parameters, not an extra gauge normalization.

On z=0 the actual D2 faces give deg F(x,x)=3 with leader epsilon, deg G(x,x)=2 with leader1, deg R(x,x)<=1. The last fact follows because its s orders are multiples of d and >=-(2d-1). Write X0(x)=x²+Lx+M and set h=L/2, u=x+h, B0=M-h². Declare source map

  x=u-h, y=u-h+z; inverse u=x+h,z=y-x,

with determinant1; retain h unless an independently audited source translation slice already handles it. Then X0=u²+B0. Write Y0=u³+alpha*u²+beta*u+gamma. The u5,u4,u3,u2 coefficients of X0³+pX0+q-Y0² give respectively

  alpha=0, beta=3B0/2, gamma=0, p=-3B0²/4.

The u1 term is automatically zero. Thus

  X0=u²+B0, Y0=u³+(3/2)B0*u,
  R0=q+B0³/4 (constant).

This is exact division, not a genus assertion. It is a nodal parametrization when B0!=0: the two parameters u²=-3B0/2 have the same image X=-B0/2,Y=0. No consequence about realization follows from that description alone.

The B0 localizer is justified even scheme-theoretically on j!=0. The (u0,z0) Jacobian coefficient gives

  j=-(3B0/2)*X1(0), hence B0^-1=-3*X1(0)/(2j).

So adjoining B0^-1 loses no part of the j-unit locus. If the distinguished localizer is separation*lambda, the transport j=kappa*lambda likewise shows D(separation*lambda) lies inside D(B0). B0 has diagonal scaling weight2 and is not separately normalized.

## 5. Exact transverse recurrence and two-way maps

All assertions in this section refer to the augmented chart imposing EVERY coefficient of J(X,Y)=j, not merely the old characteristic-only chart. Work over any Q-algebra with B0 invertible. Expand X=sum_i X_i(u)z^i and Y=sum_i Y_i(u)z^i. Put D=3u²+3B0/2 and

  K_r=sum_(i=1..r) [(r+1-i)X_i'Y_(r+1-i) - i X_i Y'_(r+1-i)],
  H_r=(j*delta_(r,0)-K_r)/(r+1).

The exact coefficient equation is

  2u Y_(r+1) - D X_(r+1) = H_r.

Its entire polynomial solution module is

  a_r=-2H_r(0)/(3B0),
  X_(r+1)=a_r+2u A_r(u),
  Y_(r+1)=(H_r+D*a_r)/(2u)+D*A_r(u).

The numerator's constant term is zero, so division by u is exact; u is not inverted. Conversely a solution gives a_r=X_(r+1)(0) and A_r=(X_(r+1)-X_(r+1)(0))/(2u), again exact polynomial division. These formulas are inverse coefficient-ring homomorphisms inductively in r; every coefficient uses only preceding strips and rational denominators plus powers of B0. Thus the quotient isomorphism is constructive, not dimension counting.

At r=0 one obtains the particularly strong exact identity

  R1=-(u²+3B0/2)*j,

because 3X0²+p=(u²+3B0/2)D and Y0=u(u²+3B0/2). In particular [u²z]R=-j=epsilon*C. D2 support gives deg R1<=2, so diagonal translation leaves [x²z]R=[u²z]R unchanged.

For finite source degrees, impose ALL degree/support coefficients after the map. In particular

  deg_u X_i<=min(m-i,2+floor(i/d)),
  deg_u Y_i<=min(n-i,3+floor(i/d)),

with negative upper bounds meaning the strip is zero. Translation u=x+h preserves these upper bounds but changes coefficient equations. Every original minor and characteristic row must also be transported. If N=max z-degree, then beyond generated strips the rows r=N..2N-1 are terminal residual equations K_r=0 (the final identically absent degree may be omitted only after proof). Setting all further A_r to zero without these equations is not equivalent to polynomial termination. For unequal z-degree bounds impose the vanished X or Y strip separately as soon as its bound is exceeded.

The two-way statement is NOT a two-way map to the old CD T2-only chart: its points can have nonconstant Jacobian of degree20/25. First adding the constant-Jacobian rows gives a smaller necessary chart for actual Keller points; only then are the target/diagonal/transverse changes isomorphisms. A proper necessary chart is not a realized pair.

## 6. Minor R boundary, including its exact scalar

Prop4.6 alone is not the minor detector theorem. Use Prop6.1(2) pp190–193 and Def3.1(4) p161. For r=3, the principal minor p-root multiplicities are3<11/(99-97)=11/2 and2<9/(108-106)=9/2. The relevant negative F orders are -18, -9/2, and -12. Prop6.1 thus supplies a detector for F,T1,T2, even though the physical minor radii2,5/2,3 exceed1; its proof p193 explicitly treats that case.

Therefore ratios9:6:5 and12:8:7 force R orders -10,-5/2,-7 and faces proportional to P^5 /Q^7, where

  99 delta2: P=zeta²(zeta+3rho),
  99 delta5/2: P=pi*(pi²-c),
  108 free mean: Q=-((pi-mu)²-c).

The proportionality scalar is exactly lambda, not a new arbitrary parameter. By the total-degree bound and minor source center ord>=0, the largest minor pi power at the boundary (15 /14) receives its coefficient uniquely from x40 y15 /x49 y14 in the highest homogeneous target. It is lambda for99 and -lambda for108. Since P is monic and Q is negative-monic, all three full targets are

  Rminor=lambda*P^5 (99), Rminor=lambda*Q^7 (108).

This supplies both the strict support and the equality target. Do not zero the equality coefficient. The D108 mean mu stays free. The argument uses no new gauge, and no new exit-price claim is made.

## 7. Decision sign and limits

For a declared coefficient ring A over Q, ideal I, distinguished s=separation*lambda, and a NEW variable Z,

  D(s) in Spec(A/I) is empty
  iff s in radical(I)
  iff 1 in I*A[Z]+(Z*s-1).

Nilpotent s proves the necessary branch chart DEAD and hence excludes any realized Keller point mapping into it. Conversely a proper localized ideal proves an algebraic-closure point on the necessary chart, with separation and lambda nonzero; it does not establish a realized pair or a complete characteristic tower. A timeout or uncomputed residual block proves neither alternative. All universal source obligations outside the proved coordinate isomorphisms remain necessary-theorem maps from actual Keller inputs; no abstract partial chart point inherits those hypotheses automatically.

## 8. Three target affine factors, with canonical-source covariance

This is a proved product-coordinate change, not an extra scale normalization. For scalars alpha,beta,gamma define

  F'=F+beta*G+gamma, G'=G+alpha, t=beta*alpha-gamma.

The inverse action has parameters (-alpha,-beta,beta*alpha-gamma). Keep the physical polynomial R identical by changing family coefficients as follows:

  b'=b+2beta,
  a'=a-3alpha-b*beta-beta²,
  c'=c-b*alpha-2t,
  d'=d+3alpha²-2a*alpha+(b+2beta)t+b*beta*alpha-c*beta,
  e0'=e0-alpha³+a*alpha²-t²-b*alpha*t+c*t-d*alpha.

C and lambda are unchanged. A'=A-3alpha, and the completed invariants X,Y,p,q are unchanged. There is a unique section alpha=A/3,beta=-b/2,gamma=-c/2 for which A'=b'=c'=0. The global inverse presentation is already given above. Consequently A,b,c are three affine coordinates and can be factored out of an ideal whose complete transformed row blocks are invariant. A fixed numerical value of B0 is not chosen.

To verify source covariance, let H=h2, and use the exact canonical decomposition

  F=H³+A2*H+A3, G=H²+B1*H+B2,

with all coefficient polynomials of y-degree below k=33/36 and their established total-degree bounds. Set w=beta/3. The canonical h2 changes to H'=H+w: in F the perturbation beta*G has degree2k, so among the coefficients determining the monic cube approximate root it changes only its constant coefficient, by beta/3. The next canonical approximate root h3 is unchanged, since adding a constant to H does not affect any coefficient determining a monic approximate root of positive degree11/9. The explicit remainders are

  B1'=B1-2w,
  B2'=B2+alpha-w*B1+w²,
  A2'=A2+beta*B1-beta²/3,
  A3'=A3+beta*B2+gamma-w*(A2+beta*B1)+2beta³/27.

Both decomposition identities were symbolically verified over Q. If H=h3^r+sum_(i=2..r) Ci*h3^(r-i), only Cr'=Cr+w changes; all other Ci are unchanged. The inverse action gives the inverse coefficient maps. Total/y degree boxes are preserved. At every retained negative D2/D1/minor detector let ord H=-a<0: the respective bounds for A2,A3,B1,B2 are at least -2a,-3a,-a,-2a, and all added terms above have weaker bounds than the recipient. Constants have order0. Likewise the inner Cr recipient bound is negative. Therefore every complete support-zero block and every actual negative face remains invariant; the explicit formulas transport its generators in both directions. Existing source centers, h3 centers, free mean, and separation remain unchanged. This proof uses the complete transported row blocks; it does not license applying an unmodified old partial row list after changing variables.

If the only R constraints are upper total-degree/positive coefficient rows and negative faces, q is an additional independent affine factor: adding q changes only R's constant and changes no F,G or J row. It must remain if a separate actual canonical constant row is imposed; the existential T2 family used here has no such row.
