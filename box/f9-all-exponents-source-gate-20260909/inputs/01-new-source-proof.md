# F9 for all exponents: the necessary ordinary receiver arrow

Status: **PROVED HERE AT THE EXPLICIT RECTANGULAR-SOURCE SCOPE; UNREVIEWED.** This is a factored, all-parameter source-interface proof, not a receiver exclusion. No mathematical subprocess, source expansion or numerical test was used.

## 1. Exact statement and the incoming source boundary

Let K have characteristic zero. Write the family parameter as q>=0, and put m=q+2, n=2q+3. Then m,n>1 and gcd(m,n)=1. Suppose P0,Q0 in K[u,v] have nonzero constant Jacobian c0 and satisfy the following ACTUAL-source conditions:

1. For e=m,n respectively, their supports lie in [0,7e] x [0,21e], with (7e,21e) attained.
2. They form an ordinary standard (m,n)-pair whose actual F9 chain starts with A0=(7,21), A0'=(1,0), direction (7,-2), type II.b, and selected child A1=(11/7,2). These are the source endpoints and selected multiplicity data, not just an admissible table label.

Then after a common constant translation, the indicated rational change of variables, a nonzero diagonal change over a finite algebraic extension, and independent nonzero output scalings, the source gives ORDINARY polynomials A,B with

    ell_(2,1)(A)=H^m,  ell_(2,1)(B)=H^n,
    H=p(p^2-g)^2(p^2-3g/2),  [A,B]_(g,p)=c*g,  c!=0.

Their full supports lie in e*Delta, where

    Delta={ (I,J): I,J>=0, 2I+J<=7, I-J<=2 }.

Their other exposed faces are exactly

    ell_(1,-1)(A)=(-3/2)^m*g^(2m)*(gp+1)^m,
    ell_(1,-1)(B)=(-3/2)^n*g^(2n)*(gp+1)^n.

Consequently their ordinary total degrees are 7m,7n, with unique total leaders p^(7m),p^(7n), and their g-degrees are 3m,3n. The three nonzero vertices e(2,0),e(3,1),e(0,7) are attained. The origin may be made attained by harmless output constants; it is not a source nonzero guard.

In fact, the proof of this mapping uses only coprime m,n>1 and the same source profile, not n=2m-1. The latter is the arithmetic family supplied by the printed F9 row. No assertion is made that other m,n realize that profile.

**Imported incoming arrow, separately typed.** GGHV1708, introduction pp.1–2, explicitly starts with ordinary attained rectangles of a normalized counterexample; its Section5 table gives F9 with exactly the displayed family and chain data. GGV1401 Proposition5.20 standardizes an ordinary pair by the identity or a constant v-translation in its proof, preserving an already given rectangle and its corner. GGHV Theorem2.20, notably(6),(8),(13), supplies the ACTUAL endpoints, selected-root multiplicity and starting-triple interpretation. Thus the theorem above applies to every representative in this precisely named ordinary rectangular F9 normalization stratum. The general normalization, ordinary standardization, complete-chain/admissibility and published table imports remain imports. No enumeration was rerun.

Accepted16a additionally proves that every actual complex degree84/140 source enters this stratum with m=3,n=5. It does NOT say that every source with numerical degrees28m,28n belongs to F9 for arbitrary q. Nor does it say that every counterexample has an F9 representative. We do not generalize that fixed-degree filtering step. An inverse normalizing automorphism can change the original degrees; the rectangle itself has normalized source degrees28m,28n.

**Broader reading remains GAP.** GGV Definition4.3 permits a 'standard' pair in L^(1)=K[u,u^-1,v]. That word alone supplies neither ordinaryness nor the two coordinate bounds above. The present theorem is not asserted for every bare Laurent standard pair or every combinatorial F9 label. This distinction is a source hypothesis, not an obstruction to the intended ordinary normalized stratum.

## 2. The ordinary starting face and the common vertical translation

At (7,-2), the two source weights are 7m,7n; their leading Jacobian vanishes because the expected bracket weight is 7(m+n)-5>0. GGV1401 Proposition2.1 therefore gives a common ORDINARY homogeneous root R, up to the independent nonzero output scalars. Its endpoints are (1,0),(7,21). Every ordinary monomial of weight7 is u^(1+2k)*v^(7k), k>=0. Hence

    ell_(7,-2)(P0)=alpha*R^m,
    ell_(7,-2)(Q0)=beta*R^n,
    R=u*r(z),  z=u^2*v^7,

where r is a monic cubic with r(0)!=0, after absorbing its leading coefficient into alpha,beta.

Theorem2.20(8) reads the child y-coordinate as m_lambda/m. Its value2 is exactly selected multiplicity2m in the leading polynomial; similarly it is2n for the other member. Passing between z and the fractional variable v*u^(2/7) preserves multiplicity at nonzero roots in characteristic zero. Therefore r has one double nonzero root a and one distinct simple nonzero root b:

    r(z)=(z-a)^2(z-b).

There is no remaining degree for a third root or a triple selected root. Over an arbitrary K, the double root is the unique root of the monic gcd(r,r'), so a lies in K; then b lies in K as well. One can alternatively work over an algebraic closure throughout this step. No fractional child polynomial is used as an ordinary source.

Let f(u) be the highest-v coefficient of P0, at v-degree21m. Its degree is7m. GGV Theorem2.6 at (0,1) supplies an ORDINARY Euler polynomial v*a0(u). Thus

    21m*a0'*f-a0*f'=f.

If deg a0=r>=2, the highest coefficient on the left is proportional to 21m*r-7m!=0 and has degree7m+r-1>7m. A constant a0 also cannot satisfy the degree equation. Consequently a0=A*u+B, with 14m*A=1, and

    f(u)=alpha*(u+r0)^(7m),  r0=B/A.

The highest-v coefficient h(u) of Q0 has degree7n. The top coefficient of the full constant-Jacobian identity is

    21n*f'*h-21m*f*h'=0.

It forces h=beta*(u+r0)^(7n), with the SAME r0. This follows either by logarithmic differentiation over K(u), or by comparing root multiplicities. The translation parameter is in K; it is not a separately chosen root for each polynomial.

Replace both sources by P0(u-r0,v),Q0(u-r0,v). This preserves their rectangles and corners, and makes the top v-coefficients pure powers of u. Since the weight of u is positive7, translation changes every (7,-2)-face monomial only by strictly lower-weight terms. Thus the entire starting face, its roots, and its selected multiplicity remain unchanged. The maximal-u coefficient was already a pure v^(21e): at u-degree7e the starting-face inequality 7i-2j<=7e forces j>=21e, and the rectangle gives equality. It remains unchanged by this translation.

After swapping (u,v)=(y,x), call the polynomials P,Q. Their bracket is -c0. For each e=m,n their common coordinatewise dominating vertex is

    C_e=(21e,7e),

and it is the unique point of maximum x-degree AND the unique point of maximum y-degree. They have total degrees28m,28n, y-degrees7m,7n, and the unchanged face direction d0=(-2,7) has normalized start (21,7), other endpoint (0,1), and weight7e. The total-degree and y-degree ratios required in opposite-edge Corollary7.4 are exactly m/n.

## 3. The cubic Euler equation, including its actual denominator

Apply the POLYNOMIAL clause of Theorem2.6 to the original ordinary source and weight (7,-2). If its Euler element is E, then [mE,R]=R. Every ordinary weight5 monomial is u^(1+2k)*v^(1+7k), k>=0. Write mE=u*v*f0(z). Direct formal differentiation, without expanding any source power, gives

    5z*r'*f0-7z*r*f0'-r*f0=r.                    (1)

Divide by r. At its distinct nonzero roots the poles force f0(a)=f0(b)=0. If deg f0=d>2, the leading coefficient of the left side of (1) is proportional to 14-7d and cannot vanish. Therefore f0=C(z-a)(z-b), and (1) becomes

    C*((3a-2b)z-ab)=1.

Hence b=3a/2 and C=-1/(ab). Conversely these satisfy this Euler equation; that is NOT a converse to the full Keller source.

The Euler endpoint is exactly (5,15)=(5/7)(7,21), for every m. Under the swap, use minus the swapped Euler polynomial to preserve the Euler bracket sign. At d0 its start is (15,5)=(5/7)(21,7). Thus the reduced positive denominator needed in GGV Corollary7.4 is q_E=7, not the family parameter q. This also agrees with Theorem7.6(3), whose type-II clause includes its index zero. Here the explicit Euler calculation independently determines the endpoint.

We will use this denominator after the Laurent cut as well. In K[x,x^-1,y], the common d0-face root is

    R0=y*r(x^7*y^2),  ord_y(R0)=1.

Two d0-homogeneous weight5 Euler elements for the same face differ by a weight5 Z commuting with R0. If Z!=0, Proposition2.1 gives Z^7=constant*R0^5. Its y-valuations would satisfy 7*ord_y(Z)=5, impossible in this Laurent ring. The Euler element is therefore unique at this face. This uniqueness is important: an arbitrary Euler solution cannot simply be substituted into a corollary that names the element constructed by Theorem2.6.

## 4. First opposite edge: all hypotheses and the integer cut

From C_e go clockwise to the nearest lower edge in the union of the two polygons. Its primitive normal is d=(rho,sigma), with rho>0>sigma. Until that direction, both support functions are attained at C_m,C_n.

At least one of P(x,0),Q(x,0) is nonconstant. Otherwise P_x and Q_x both vanish identically on y=0, contradicting their nonzero constant bracket there. Since the source is ordinary and rho>0, this supplies a strictly positive d-value for at least one member. Values at the proportional C_e then give

    3rho+sigma>0

for both. Positivity holds on the WHOLE angular interval [d,d0], not just its endpoints: each direction there has the same maximizing corner, and the shorter sector is the positive cone of its endpoint directions. Indeed 7rho+2sigma>rho>0, so its angle is less than pi. The common corner has positive value at each endpoint and therefore throughout. Thus d is within the exact positive interval defining the stopping direction in Proposition7.3.

At d the expected leading bracket weight is

    (m+n)*7(3rho+sigma)-(rho+sigma)
      =(7(m+n)-1)(3rho+sigma)+2rho>0.            (2)

This is the all-exponent replacement for the old 167rho+55sigma calculation. It uses m+n>=5, not m=3,n=5. Consequently the faces commute. Since one has an edge and both weights are positive with ratio m/n, common powers force the other also to have an edge with the same support slope; a monomial power cannot equal a nonmonomial power in this domain.

Apply Corollary7.4 with l=1, normalized start (21,7), 7<21, d0 in V_{>=0}, positive d0-weight, the just-proved whole-interval positivity, and q_E=7. Its conclusion gives a 7e-th power face root with normalized endpoint (3,1). Scalar roots can be adjoined for that assertion; they do not change its support. At this FIRST cut the face polynomial is ordinary. A Laurent root whose positive power is ordinary must itself have nonnegative minimal x-exponent. Thus the root is ordinary, has y-degree1 and is nonmonomial. It has precisely the form

    a1*x^3*y+b1*x^(3-k),  a1*b1!=0,

with k an INTEGER and d=(1,-k). Positivity says k<3. Guccione–Guccione1605 Corollary1.6 excludes k=1, and its Proposition2.1 applies to this ordinary Jacobian pair and endpoint C_e with 21e>7e>0, excluding 0<k<1. Those statements do not assume m=3,n=5 or global minimality. It follows that

    k=2.

The shared root is x^3(y-lambda*x^-2), up to a scalar, with lambda!=0. The lambda for P and Q is the same by common powers. It lies in K: it is recovered from the next coefficient of the monic y-polynomial of degree7e by division by7e. The exact faces are

    ell_(1,-2)(P)=eta_m*x^(21m)*(y-lambda*x^-2)^(7m),
    ell_(1,-2)(Q)=eta_n*x^(21n)*(y-lambda*x^-2)^(7n).

No printed exponent-specific prefactor from the 2022 proposition is imported.

## 5. No hidden rational edge between slopes2 and3

Apply the common Laurent automorphism psi: x->x, y->y+lambda*x^-2. Its determinant is1. The (1,-2) faces become the single monomials at C_e. The points C_e remain unique maxima of both coordinates and of total degree: every changed term lowers x by2t, y by t and total degree by3t. The d0-face is unchanged because the two substituted terms have d0-weights7 and4. The degree ratios required by Corollary7.4 are therefore still m/n.

Suppose the next lower edge at C_e has rational slope kappa with 2<kappa<3. Its value is 7e(3-kappa)>0. The same common-corner argument supplies positivity on the WHOLE interval to d0, and (2) supplies commutation and a common edge. At d0 the actual constructed Euler element is still the old one: the face is unchanged and uniqueness was proved in Section3. Hence q_E remains7.

Corollary7.4 again gives a root with y-degree1 and endpoint (3,1). Now it need only be Laurent in x, but its x-exponents are still integers. The other monomial has exponent3-kappa, so kappa must be an integer, a contradiction. This is the required exclusion of ALL rational intermediate slopes, not merely integer directions that happened to be sampled.

There is a next lower edge because the polynomial is nonmonomial. Its slope is therefore at least3. No opposite-edge theorem is applied at slope3, where the corner value is zero. The supporting inequality at an actual edge of slope kappa>=3 and the independent bound j<=7e give, for EVERY support point (i,j),

    i-21e<=kappa*(j-7e)<=3*(j-7e),

so i<=3j. This argument also covers the case that the next edge is at slope3. It is a full-support conclusion, not a claim about only the retained faces.

## 6. Full support transport and the exact Jacobian sign

Before psi, ordinaryness and the starting face give i,j>=0 and -2i+7j<=7e. Thus

    i-2j >= (3/7)i-2e >= -2e,

with equality only at (i,j)=(0,e). Each term produced by psi changes (i,j) to (i-2t,j-t), 0<=t<=j. It preserves i-2j, decreases -2i+7j by3t, and retains j>=0. Together with Section5 the complete post-cut support satisfies

    j>=0, i<=3j, -2i+7j<=7e, i-2j>=-2e.       (3)

Now substitute x=g^-1, y=g^3*p. On each literal monomial the exponent map is

    (i,j) -> (I,J)=(3j-i,j).

Equation(3) proves I,J>=0, 2I+J<=7e and I-J<=2e. Thus BOTH entire receivers are ordinary polynomials. No cancellation of unspecified negative powers is assumed, and the fractional L^(7) child is never substituted as the source.

The composite from the unshifted source is exactly

    (u,v)=(g^3*p+lambda*g^2-r0, g^-1).          (4)

Its determinant in (g,p) is g: u_p=g^3 and v_g=-g^-2, while v_p=0. Equivalently, the swap has determinant-1 and the last toric map has determinant-g. Therefore the resulting unnormalized receivers satisfy [Abar,Bbar]=c0*g, not -c0*g and not constant c0.

The upper (2,1) faces are alpha*Hbar^m,beta*Hbar^n, where

    Hbar=p(p^2-a*g)^2(p^2-b*g),  b=3a/2.

For the other face, equality i-2j=-2e had only the original point (0,e). Its full psi expansion therefore gives exactly

    alpha*r(0)^m*g^(2m)*(gp+lambda)^m,
    beta*r(0)^n*g^(2n)*(gp+lambda)^n.

In particular, the vertex(2e,0) has the unique nonzero contribution proportional to lambda^e; it cannot be canceled by some other original point. The starting endpoints give (0,7e),(3e,e). All these arguments hold for arbitrary e=m,n.

## 7. Simultaneous normalization, fields and exact limits

Choose mu!=0 with mu^3=a*lambda, and put kappa=lambda/mu. Make the diagonal substitution (g,p)->(kappa*g,mu*p), then divide Abar by alpha*mu^(7m) and Bbar by beta*mu^(7n). These are invertible algebraic-closure operations, not an unsupported same-field normalization. They give

    a*kappa/mu^2=1,  b*kappa/mu^2=3/2,
    lambda/(kappa*mu)=1.

Thus the normalized faces are exactly those of Section1. The lower-face factor is also correct: r(0)=-a^2*b=-3a^3/2, and the per-root scalar transforms to

    r(0)*kappa^3/mu^6 = -3/2.

The new Jacobian coefficient is

    c = c0*kappa^2*mu / (alpha*beta*mu^(7(m+n))) != 0.

No normalization c=1 was imposed. Output constants may be changed after these operations without affecting either face or the Jacobian.

The mapping theorem is valid over a finite algebraic extension of any characteristic-zero coefficient field satisfying the stated ordinary rectangle/chain hypotheses. When starting from an arbitrary actual characteristic-zero counterexample through the imported complex normalization, one may first embed its finitely generated coefficient field into C. That preserves the hypothetical counterexample but does not make its chosen normalizer descend to the original field. The proof introduces no new arithmetic restriction on receiver variables or rational-point requirement.

The inverse of(4) is rational. An arbitrary polynomial receiver with the two faces and bracket c*g need not lift to an ordinary source: all reverse polynomiality conditions remain additional source conditions. Necessity here does not need a reverse theorem. No ideal, unit, properness, explicit point, source existence, family exclusion, maximum-degree exclusion or JC2 conclusion is obtained.

## 8. Discriminating scope controls and exact audit outcome

These are manual controls, not executed examples or hypothetical full Keller pairs.

- **Rectangle omission:** adding u^(7m-1)*v^(21m+1) to a polynomial with the stated corner preserves its maximal-u endpoint, its total degree28m, and its (7,-2) face, since the extra weight is7m-9. It breaks the v-degree bound needed by Section2. This does not preserve the full Keller equation; it proves only that endpoint/degree/face metadata alone do not license the rectangle. No broader Laurent theorem is refuted or asserted.
- **Wrong root ratio:** equation(1), after f0=-((z-a)(z-b))/(ab), has multiplier 1-(3a-2b)z/(ab). A changed ratio b!=3a/2 leaves a genuinely nonconstant error. The restriction concerns the ordinary polynomial Euler equation, not a face ansatz offered as a Keller pair.
- **Coefficient ring matters:** replacing the post-cut integer x-lattice by fractional exponents would allow the formal two-term root x^3*y+x^(3-kappa) for a noninteger 2<kappa<3. The integer-cut proof would then fail exactly at that step. This is why the original ordinary source and subsequent L^(1) cut, rather than the L^(7) child, are retained.
- **Jacobian type matters:**(4) has determinant g. Applying a theorem for constant-J receivers, or for c*g^2, to its result would be an unlicensed different target.

**Audit outcome.** At the intended ordinary rectangular actual-F9 source scope, the all-parameter necessary arrow is proved by Sections2–7, with named primary imports. The fixed m=3,n=5 numerical restrictions in the old proof have been replaced explicitly; no hidden exponent bound remains in the translation, Euler denominator, whole-positive interval, integer gap, full support transport or root normalization. At the broader bare-standard/Laurent scope, the first missing implication remains ordinaryness plus rectangle; at the broader same-numerical-degrees scope, the missing implication is selection of the F9 chain. Neither is repaired by this theorem.

## 9. Evidence and publication perimeter

The four accepted parent reports were freshly pinned BEFORE WHOLE reads:

- fixed-degree source8c88c02728753173733e206e50bb2003071a8ae18f312fba59d4f3a220765b82;
- ordinary map8bad927c8ef369a211fe3b1467efe6f9f40f26141e6338c1a470eb918a2fa50c;
- root ratio571d1fae2682c64c86a13599f0db827b6371f9b5f63b50b186ab8112adb9594c;
- accepted joint gatef33820d2bf5f4f75229938b3cfb6d03d21cd05bb8c09a9cf340e3edaa351f7bd.

Primary texts: GGV1401v3 e3694dde3f83c2ab6ed8d957fc6b53472e6a6dd55486af1dff345eade39e37b1; GGHV1708v1 49df06d11bbc4556a9b09771cdd60ca40a75b7542d327bbb622e09434e6a467e; lower-side1605v2 77ae98339d7a70c476d89c01a2d38ba3aa1af98fbb0ba9da32c1759fde87a221. Exact paths, byte lengths, selected primary read intervals and source roles are in the owned input-pins.json and READ-SCOPE.md. No published enumeration, mirrored Corollary7.4 foundation or general normalizer was independently reproved here. The universal manual argument is the proof; no finite test is a substitute.

New source-interface proof only, UNREVIEWED pending independent review. The accepted16a/b parents are not edited. No pending uniform-exclusion proof, 0730 blind or live reviewer was read or consumed. No new raised campaign item is proposed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20018`.
- Body SHA-256:
  `8d197aa2f8cd422ad0bbbf72f093b2fd76e9b6c9defcae10fc1272e0a362bf21`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
