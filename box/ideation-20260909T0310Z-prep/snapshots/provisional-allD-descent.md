# A coordinate obstruction and conditional all-D late-contact Keller descent

September9 2026. **PURE-PROSE PROOF / PROVISIONAL, awaiting independent review.** The proposed polynomial-coordinate obstruction is valid. It supplies the missing NONAUTOMORPHY step in the late-contact descent below. This is a conditional source bound for globally minimal Keller counterexamples with a stated3:5/centralizer interface, not a proof of JC2 or an assertion that every counterexample has that interface.

Only the accepted late-contact producer b541308788da31f52e9f7985c7767e206231e8f3251ff53c1b2bd9c96b64f097 and its Fable gate c9a399a87dc91d78bfc4f811249996ea3e217eda075be679cf27b41af5795c26 were charged, pinned before bodies and read WHOLE. Their general finite lemma is used at its explicit polynomial/homogeneous/centralizer scope. Their triple-specific monomial-J endpoint and any pending triple/cubic proof are NOT premises. The general reference pattern is rederived below with constant Jacobian and arbitrary D. No primary-web/history novelty check was undertaken or claimed.

## 1. Exact statement

Let K be any characteristic-zero field. Let D>=3 be an integer and H in K[u,v] a nonzero homogeneous polynomial of degree D whose polynomial Hamiltonian centralizer is EXACTLY

    ker([H,-]:K[u,v] -> K[u,v])=K[H],
    [P,Q]=P_u Q_v-P_v Q_u.

Assume ordinary polynomials A,B in K[u,v] satisfy

    deg A=3D, deg B=5D, A_(3D)=H³, B_(5D)=H5,
    [A,B]=c in K*,                         (S)

where c is a NONZERO CONSTANT, not c*u² or another monomial. Construct the canonical homogeneous reference and j described in§3. If

    3j>7D,                                (L)

then the specialized remainders f=F(1,u,v),g=G(1,u,v) are a Keller pair with [f,g]=c and

    deg f=3D-j<2D/3,
    1<=deg g<=5D-2j<D/3.                 (D)

They are NOT a polynomial coordinate pair, even after extending the coefficient field. When a displayed upper bound for deg g is nonpositive, the hypotheses are simply impossible; no zero/constant component is called a Keller pair.

Consequently a Keller counterexample of globally minimal maximum component degree, among ALL nonautomorphic Keller pairs over K, cannot satisfy(S)+(L). If such a global minimum has this3:5/centralizer interface, its canonical first contact obeys

    j<=floor(7D/3).

The word globally is essential: the smaller pair need not have degrees in ratio3:5 or a centralizer of the same form. Minimality only within this subclass would not give the corollary.

## 2. Polynomial-coordinate obstruction, with every degree case

**Lemma.** Let x,y be algebraically independent over a characteristic-zero field K. For arbitrary alpha,tau,delta,b4 in K and t(T) in K[T], there is NO nonconstant polynomial r in K[x,y] satisfying

    (3r²+alpha)*y-(tau*r+delta)*x
       -(5r/3+2b4/3)*x²=t(r).             (C)

If deg_y r=0, then r lies in K[x]. The y coefficient of(C) is3r²+alpha, so it must vanish. A nonconstant polynomial r in K[x] cannot have a constant square in a domain. Thus this case forces r constant, excluded by the lemma.

Now let n=deg_y r>=1 and let a(x) be its nonzero y-leading coefficient. The left side of(C) has y-degree EXACTLY2n+1, with leading coefficient3a(x)²: the other terms have y-degree at most n or1. Hence t is neither zero nor constant. If m=deg t, the right side has degree mn, with nonzero leading coefficient t_m*a(x)^m. No leading cancellation is possible. Therefore

    mn=2n+1, so (m-2)n=1,
    n=1 and m=3.

Write r=a(x)y+b(x), a!=0. Over K(x), r is an affine coordinate in y and y=(r-b)/a, so coefficient comparison in the polynomial ring K(x)[r] is legitimate. Equation(C) becomes

    (3/a)r³-(3b/a)r²
    +(alpha/a-tau*x-5x²/3)r
    -alpha*b/a-delta*x-2b4*x²/3 = t(r).

The r³ coefficient is the nonzero FIELD SCALAR t3, so a=3/t3 belongs to K*. The r² coefficient is t2 in K, so b=-a*t2/3 belongs to K. The r coefficient would then require

    alpha/a-tau*x-5x²/3=t1 in K,

impossible because the quadratic coefficient−5/3 is nonzero in characteristic zero. This covers every zero choice of alpha,tau,delta,b4 and every t, including the impossible constant/zero t cases. The temporary passage to K(x) compares coefficients only; it asserts no polynomial inverse for an unrelated map.

**Manual dependency controls.** Constants r really are excluded: r=0,alpha=delta=b4=0,t=0 gives(C), for instance with tau=0. If the mandatory term−(5/3)r*x² is deleted, take r=y, all four scalars zero and t(T)=3T³; the altered identity holds. If t is allowed coefficients depending on x, the original identity with r=y and zero scalars holds with t_x(T)=3T³-(5/3)x²T. Thus scalar coefficients of t, not merely a formal label t(r), are load-bearing. None is a Keller-source point or a computational test.

## 3. Canonical A reference for arbitrary D

Introduce s of degree1 together with u,v, and use the polynomial homogeneous dilations

    A_s=s^(3D)A(u/s,v/s),
    B_s=s^(5D)B(u/s,v/s).

These are combined-HOMOGENEOUS of degrees3D and5D. Differentiating only in u,v gives

    [A_s,B_s]=c*s^(8D-2).                 (1)

The exponent has no additional subtraction for a target variable: the original c is constant. Every assertion below uses this distinction from the accepted triple receiver's c*u² target.

Fix one monomial order, say lex u>v. Starting with H, successively construct

    R=H+sum_(a=1)^D s^a R_(D-a).

At stage a divide the ordinary degree3D-a coefficient of A_s-R³ by3H²; its homogeneous quotient has degree D-a and its remainder is monomial-normal for LM(H²). Use that quotient as R_(D-a). The new cube changes order a by exactly3H²R_(D-a), and only later orders otherwise. Single-divisor division terminates, preserves homogeneity and uses only fixed nonzero coefficients in K. This does not presume any factor shape or bounded degree in one variable.

At order2D divide the ordinary degree D residual by H. Its quotient is a scalar alpha. Subtract alpha*s^(2D)R, and choose the scalar a0 to remove the remaining order3D constant. Define

    alpha_s=alpha*s^(2D),
    F=A_s-R³-alpha_s*R-a0*s^(3D).         (2)

The first D residuals retain LM(H²)-normality, F_(2D) is LM(H)-normal and F_(3D)=0. These normalization facts make the reference unambiguous for the chosen division order, but no extra factor-cover conclusion is assumed.

F is nonzero. Otherwise, over K(s), equation(1) would factor as

    (3R²+alpha_s)*[R,B_s]=c*s^(8D-2).

The first factor has ordinary(u,v)-degree2D>0 with leading form3H²; the right side has degree0. A nonzero polynomial product over a field has the sum of its factor degrees, so this is impossible. Thus

    1<=j=ord_s F<=3D-1,
    deg_(u,v) F_j=3D-j.                  (3)

R and F are finite polynomials, combined homogeneous of degrees D and3D. At s=1, R(1) has ordinary degree D with top H and is nonconstant. Different s-coefficients of F have distinct ordinary degrees, so specialization at s=1 cannot cancel its nonzero highest coefficient F_j. In particular deg F(1)=3D-j exactly.

## 4. All five B kernels, not an odd-only or truncated reference

For i=0,...,4 write beta_i=b_i*s^((5-i)D), with b_i in K. Put

    f_B(z)=z5+beta4*z4+beta3*z3+beta2*z²+beta1*z+beta0,
    q(z)=5z²/3+4beta4*z/3+beta3-5alpha_s/9,
    tau_s=2beta2-4beta4*alpha_s/3,
    delta_s=beta1-beta3*alpha_s+5alpha_s²/9,
    G=B_s-f_B(R)-q(R)*F.

Then ord tau_s>=3D and ord delta_s>=4D; vanishing scalars may raise these orders to infinity. All objects have their indicated combined degrees. The scalar derivative identity is

    f_B'(z)=(3z²+alpha_s)q(z)+tau_s*z+delta_s.

Taking the exterior product of the FORMAL differentials in the independent symbols R,F,G, with s constant, gives the exact identity

    [A_s,B_s]=[R,T]+[F,G],               (4)
    T=(3R²+alpha_s)G-(tau_s*R+delta_s)F
           -(5R/3+2beta4/3)F².          (5)

For completeness the dR wedge dF coefficient is−(tau_s R+delta_s)−q'(R)F, the dR wedge dG coefficient is3R²+alpha_s, and the dF wedge dG coefficient is1. Differentiating the last term of T supplies−q'(R)F[R,F]. Thus no alpha, b4, tau, delta or constant reference was dropped. T is a finite polynomial combined-homogeneous of degree7D, or zero.

Choose the five scalars b_i so that

    ord_s G>=2j.                         (6)

Here is the full induction. Initially G0=0. If its first nonzero coefficient is G_l with l<2j, the order-l equation of(4) is

    [H,3H²G_l]=0.

Indeed F² begins at2j, the tau/delta times F term begins at least3D+j>2j because j<=3D-1, [F,G] begins at j+l>l, and the target begins at8D-2>2j since2j<=6D-2. As3H² is nonzero, this gives[H,G_l]=0. The ASSUMED polynomial centralizer says G_l lies in K[H]. Its ordinary degree5D-l and l>0 permit only

    l=D,2D,3D,4D,5D,
    G_l a scalar times H4,H3,H²,H,1, respectively.

Changing b4,b3,b2,b1,b0 by a scalar e changes G by, respectively,

    -e*s^D*(R4+4RF/3),
    -e*s^(2D)*(R³+F),
    -e*s^(3D)*R²,
    -e*s^(4D)*R,
    -e*s^(5D).

Each kills its designated leading coefficient and affects no earlier order. The induced changes preserve the tau/delta lower bounds. The induction is finite, with at most these five orders; it yields(6), including G=0 if the bound exceeds its possible polynomial degree. This is an identity-based choice of reference scalars, not a polynomial target shear or an omitted equation.

## 5. The late contact gives an EXACT scalar polynomial t(R)

Under(L), equations(1),(4),(6) imply

    ord_s[R,T]>=min(8D-2,3j)>7D.          (7)

Both strict inequalities matter:3j>7D is the contact hypothesis, and8D-2>7D holds because D>=3. The accepted finite late-contact lemma applies to the polynomial R of combined degree D, its initial H with centralizer K[H], and the polynomial T of degree7D. It gives the STRONGER representation

    T=sum_(i=0)^7 t_i*s^((7-i)D)*R^i,
    t_i in K,                            (8)

and hence[R,T]=0 exactly. This is not merely a rational centralizer claim. To recall why the coefficients are scalars: a first nonzero T_l centralizes H, so its ordinary homogeneity makes it a scalar H^i; subtract t_i*s^(7D-Di)R^i and repeat. The polynomial's s-order increases and is bounded by7D. Finite subtraction exhausts it. No convergence, localization of the source or assumed algebraic inverse is involved.

It follows from(4) that

    [F,G]=c*s^(8D-2)                      (9)

as an exact polynomial identity, not only at its first nonzero coefficient. Evaluating at s=1 gives[f,g]=c for f=F(1),g=G(1). Both are nonconstant; in particular G=0 or a polynomial in s alone is now impossible. Combined homogeneity and(6) give deg g<=5D-2j. If that bound is<=0, equation(9) is already a contradiction. Otherwise (D) follows from3j>7D. Also deg f+deg g<=8D-3j<D, whereas the original sum is8D.

At s=1 let r0=R(1), T1=T(1). Equation(8) supplies

    T1=t(r0), t(Z)=sum_(i=0)^7 t_i Z^i in K[Z].

This is the precise field/ring arrow required by the coordinate obstruction. Merely knowing[R,T]=0 without scalar polynomial representation would not be the stated proof.

## 6. Why the descended pair is NONAUTOMORPHIC

Suppose for contradiction that(f,g) is a polynomial automorphism of the affine plane over K. The homomorphism K[x,y] -> K[u,v] taking x to f and y to g is then an isomorphism. Its polynomial inverse expresses the nonconstant r0 as r(x,y) in K[x,y]; r remains nonconstant because the isomorphism preserves constants.

Specialize(5),(8) at s=1 and transport through that isomorphism. With the scalars alpha,tau=tau_s(1),delta=delta_s(1),b4 unchanged, one obtains EXACTLY

    (3r²+alpha)y-(tau*r+delta)x
          -(5r/3+2b4/3)x²=t(r).

Lemma(C) forbids this nonconstant polynomial r. Therefore(f,g) is NOT a polynomial coordinate pair. The same contradiction applies after any field extension: the identities and nonconstant leading H persist and the lemma holds over that characteristic-zero extension. No general theorem “smaller Keller pair is nonautomorphic,” no unproved equality K(u,v)=K(f,g), and no rational-to-polynomial inverse inference is used. The assumed POLYNOMIAL inverse is precisely what is contradicted.

This proves the descent claim even without assuming the original(A,B) nonautomorphic. For the minimal-counterexample application, choose(A,B) globally minimal among all nonautomorphic Keller pairs over the chosen field, and suppose it has(S). The new pair is another nonautomorphic Keller pair with strictly smaller maximum component degree (indeed both bounds are below2D/3), contradicting that minimality. Thus(L) cannot hold there, giving j<=floor(7D/3).

## 7. Boundary checks, usefulness and what remains open

The distinction between CONSTANT and monomial Jacobian is essential: (1) is c*s^(8D-2), and(9) specializes to a genuine Keller pair. With a variable monomial target, the descended bracket is generally still variable, so no smaller Keller counterexample follows from this proof. The earlier triple c*u² endpoint is not an application of this constant-Jacobian theorem.

D>=3 is the scope in which the ACCEPTED STRICT late-T threshold is used. At D=2,8D-2=7D, so(7)'s target inequality fails; this packet makes no D2 descent claim. At D1 the claimed late interval is empty under j<=3D-1. No improved late-T threshold or small-D classification is inferred here. Similarly3j=7D is not covered; cancellation might or might not improve the order, and no automatic conclusion is taken from it.

The centralizer K[H] is an EXPLICIT source hypothesis, not a property asserted for every homogeneous H. The scalar form of t in(8), the finite polynomial nature and combined homogeneity are mandatory. The coordinate lemma's controls show why allowing t coefficients in K[x] destroys the contradiction. The bound G>=2j is derived with all five B kernels; it is not a formal power-series limit or an odd-parity shortcut.

The specializations f,g are genuine finite polynomials in the ORIGINAL coordinates u,v. No actual pair, high H/R powers, source coefficient system or inverse was expanded to prove this universal statement. The strongest result is a conditional ALL-D descent/first-contact bound for this interface. It neither excludes every3:5 Keller source nor proves that a globally minimal counterexample has3:5 degrees, a closed H, or late first contact. The descended pair need not retain this interface, so iterating the same lemma automatically would be unjustified. Early contacts remain a separate mathematical problem.

No novelty or complete campaign-history claim is made before a source/literature check. The two named reports are the exact accepted history used: their finite lemma is KNOWN; this coordinate-obstruction composition and arbitrary-D constant-Jacobian descent are new PROVISIONAL work in this packet, not a promoted external theorem. Independent hostile review is the next evidence step, not a solver or compute allocation. No shared ledger, OPEN identifier, source-family retirement or JC2 announcement is made.

## 8. Custody and terminal status

Owned box: box/late-contact-keller-descent-20260909/. Input-pins records the two whole source/report hashes and read scope, checked before bodies and again at publication. All reasoning is manual polynomial degree, coefficient comparison and formal exterior-product algebra; no mathematical subprocess of ANY size, web/CAS/AWS/SSH, agents, pending source/gate/cross body, full pair/high-power expansion, shared/canonical edit or protected-project inspection occurred. Metadata scripts only perform hashes and the required begin/close/finalize/verify transaction. All substantive claims above are complete at their stated provisional scope; all writers are IDLE after terminal publication, before the unchanged02:48UTC deadline.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15805`.
- Body SHA-256:
  `def446a906f4d914d323e6af543a5e9a9e56750ea835706b59b48770513fd23c`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
