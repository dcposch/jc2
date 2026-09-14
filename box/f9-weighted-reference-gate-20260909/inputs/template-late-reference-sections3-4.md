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

