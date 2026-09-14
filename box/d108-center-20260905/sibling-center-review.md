# (99,66) D2 centre and normalization review

This note addresses centre theory only for both `delta2` and `delta52` branches of the repository's `box/g9966band-20260903/band_engine.py`. No elimination is replayed here. The frozen-input hashes were checked by the parent lane before this task began. Moh references are to the frozen PDF, with the parent's extraction `box/d108-center-20260905/moh-layout.txt`. No ledger, jc2-lean, or ideation file was accessed or edited.

**Centre-theory conclusion.** The sole possible pre-radius D2 centre coefficient, after the two lines at infinity have been placed, is the physical constant intercept A in

    y = t^(-1) + A + pi*t^(1/3),
    w = 1 + A*t + pi*t^(4/3),   t=s^3.

Thus A*s^3 is the only centre term below s^4 in w. It can be removed simultaneously with the physical constant intercept B on the principal-minor line by the two-dimensional source-translation group. The metadata `"b0":"fixed_zero"` is an auxiliary ODE integration constant, not B and not a physical source-translation normalization. It consumes neither source translation. Once the explicit translation is applied, the D2 monomial floors in `h3_template`, `build_major_h2`, and the outer blocks have no remaining centre objection on either branch. This does not itself certify the separate elimination or resolve other source-to-chart issues.

## 1. Why no fractional exponent precedes the D2 radius

The data, recorded also in `xmodel/g9966-design-gate-grok46-20260903.md:55-58,87`, are

    n=99, m=66, d=(99,33,11,1), M=(-66,77,97), V3=V2=8,
    delta3=-1, delta2=1/3, delta1=4/9.

The top h3 form is P=y^3(y-x)^8. The pair has top forms P^9 and P^6. Hence its major residue at the outer disc is the rational residue 1, and its principal-minor residue is 0. At the D3-to-D2 step Moh Proposition 5.3, printed p.180 (extraction lines 2157-2179), defines the next disc as the minimal disc containing **all** roots of the indicated product g times the T_i whose difference from the selected root has order greater than delta3. For the residue-1 branch this is the set of roots with leading term t^(-1). This is a set defined over k((t)), because its condition is a rational leading residue.

Choose N divisible by all Puiseux denominators of the finitely many roots. Every automorphism t^(1/N) -> zeta*t^(1/N) of k((t^(1/N)))/k((t)) preserves that root set. The minimal disc D2 is therefore stable under these automorphisms. Every pair of its roots has difference of order at least 1/3. Consequently their truncations to exponents strictly below 1/3 agree. Let C(t) denote this common truncation. For every conjugation gamma, gamma(C) is the same common truncation, so gamma(C)=C. A monomial a_j*t^j with j nonintegral cannot be invariant under every gamma; therefore all coefficients at nonintegral j<1/3 vanish.

The degree bound supplies the lower endpoint without a normalization. If a root of a monic polynomial of total degree n had order lambda<-1, its y^n term would have strictly lower valuation than every other x^i*y^j with i+j<=n and j<n: the difference is (n-j)(-lambda)-i>0. This would contradict the root equation. Thus every pair root has order at least -1. In the residue-1 cluster the coefficient at exponent -1 is already 1, and the integers in [-1,1/3) are precisely -1 and 0. Therefore C=t^(-1)+A.

This is a Galois-stability argument using the actual D3-to-D2 construction. The general wording of Definition 5.1(4), printed p.179, alone would not exclude fractional centre terms for an arbitrary higher disc. The argument is also not the false statement that every root has integral Puiseux exponents: at order 1/3 and above, fractional exponents are required. They are simply absent in the common **strictly pre-D2** truncation.

The same reasoning applies to the principal-minor residue-0 cluster until its first split. The selected split hypotheses give the current chart's minor expansions

    delta=2:   y=B+u*t+zeta*t^2;
    delta=5/2: y=B+u*t+v*t^2+pi*t^(5/2).

The coefficients u (and v on the second branch) remain free. The constant B is distinct from the ODE integration constant b0 discussed below.

## 2. The two intercepts and their exact group element

Use pullback notation

    F_new(x,y)=F(x+c,y+b),   G_new(x,y)=G(x+c,y+b).

The Jacobian and monic leading forms are unchanged. A physical major branch y=x+A+O(x^(-1/3)) becomes y=x+(A+c-b)+O(x^(-1/3)); a minor branch y=B+O(x^(-1)) becomes y=(B-b)+O(x^(-1)). Thus

    (A,B) -> (A+c-b, B-b).

The choice

    b=B,   c=B-A

sets both intercepts to zero. In particular, using y-translation to set the minor intercept to zero still leaves x-translation to set the major intercept to zero. There is no need to claim A=B.

This action is preserved by the approximate-root chart: source translations preserve monicity, y-degree bounds, and total-degree bounds. If h is the unique monic approximate root of Q, then h(x+c,y+b) satisfies the defining approximation inequality for Q(x+c,y+b), so uniqueness identifies the translated approximate root. Missing powers in the Tschirnhausen expansions are construction identities, not independent source-translation gauges.

An exact intercept-product control is

    h=(y-B)^3*(y-x-A)^8,
    h(x+B-A,y+B)=y^3*(y-x)^8.

The coefficient of y^10 in h-P is -8A-3B. Setting that trace coefficient to zero with y-translation gives only 8A+3B=0. It does not imply A=B=0. However the full two-translation action sets both to zero and makes the trace normalization automatic. This corrects the one-dimensional gauge objection in `xmodel/g9966-chart-necessity-opus5-20260903.md:312-364`; the correction is already exhibited in `xmodel/g9966-gauge-gaps-grok46-20260903.md:117-211` and is independently checked here.

An x-translation does not spoil the branch parameters kept by the engine. It changes higher integer coefficients of the minor centre while retaining the forms above, with newly named u,v. The split radius and the packet partition are invariant. An at-radius translation of the local variable zeta to put the delta=2 double root at zeta=0 is a choice of the disc parameter, not another source y-translation.

## 3. Complete ledger of normalizations visible in this chart

1. **Placement of the two infinity points.** An invertible linear source transformation sends their independent linear forms to Lmin=y and Lmaj=y-x. This is the GL2 action, with target scalars subsequently restoring monicity. Its stabilizer retains the two source translations and a two-dimensional eigenline torus.
2. **Monic F,G and their fixed top coefficients.** Independent target scalings make the nonzero coefficients of P^9 and P^6 equal to 1. They do not change the source intercepts.
3. **J=1.** A remaining source torus direction, accompanied by monicity-restoring target scalings, normalizes the nonzero Jacobian constant. For the isotropic subgroup x,y -> s*x,s*y, the combined factor on J is s^(-163). Algebraic closure supplies the needed s. This leaves a nonisotropic torus direction; it consumes no translation.
4. **Major intercept A=0 and minor intercept B=0.** These consume the two translations just exhibited: (x,y) -> (x+B-A,y+B). If trace normalization of h3 is recorded separately, it is a consequence of this choice, not an additional condition.
5. **D1 face scale beta=1.** The correct residual torus preserving y=0 and y=x is

       A_(gamma,delta)(x,y)=(gamma*x+(delta-gamma)*y, delta*y).

   It satisfies P o A=gamma^8*delta^3*P. The restorers for F,G are gamma^(-72)*delta^(-27) and gamma^(-48)*delta^(-18), and the factor on J is gamma^(-119)*delta^(-44). For the D2 child face (pi^3-beta)^8, the scale changes by beta -> beta/(gamma^3*delta). Consequently preserve J=1 and set beta=1 by solving gamma^119*delta^44=1 and gamma^3*delta=beta, equivalently gamma^13=beta^44. Since beta is nonzero and k algebraically closed, this is possible. It preserves the two zero intercepts. The chosen D1 child is then w=1+e^12+Pi*e^13, t=e^9. Choosing its root is a local conjugate labeling; translating Pi at its own radius is a local parameter choice. Neither is a source translation.
6. **Missing h3^2 in h2 and h2^2 in F.** Canonical characteristic-zero approximate-root construction, not a group normalization. The bases are h2=h3^3+C2*h3+C3 and F=h2^3+A2*h2+A3; G=h2^2+B1*h2+B2. There is no hidden condition removing a physical y-intercept here.
7. **K2c output coordinates and seven D1 pivots.** The coordinate change has rational unit leading C2/C3 columns; the displayed seven affine pivots at engine lines 328-359 are elimination of necessary equations, not group gauges. The D2 floor is justified only after item 4, by the support calculation below. No normalization can be inferred merely from a coefficient being deleted.
8. **Principal-minor faces.** Delta=2 selects the [2,1] branch and uses the local at-radius parameter shift to write p=zeta^2*(zeta+3rho), with rho symbolic and nonzero. Delta=5/2 uses the Galois-compatible odd cubic p=pi*(pi^2-c), with c symbolic and nonzero. The engine does not set rho=1 or c=1. These facts are read directly from engine lines 260-278 and 283-304.
9. **The metadata b0=fixed_zero.** This is an auxiliary ODE integration-constant slice, discussed in section 4. There is no group element on physical (x,y) associated with the metadata. On the projected F/G/h incidence chart it is a spectator coordinate and can instead be adjoined freely, so no physical normalization is being consumed.
10. **Target additive constants.** The outer blocks carry constant coordinates where their support allows; no target-translation cut is used by this engine. The source records explicitly declare target translations available and unused. They are independent from source translations in any case.

This ledger lists the relevant normalizations; it does not turn a necessary support inequality into an equality face. The h2 face (pi^3-beta)^8 uses the tower's characteristic and Galois splitting data as well as the torus scale; Theorem 1.2 alone only gives the support inequality.

## 4. What b0 actually is

An AST scan of `band_engine.py` finds the literal `b0` exactly once, at line 278 in metadata. There is no b0 symbol, coefficient assignment, or generator in the F/G engine. Its antecedent is the reduced local ODE, with p=pi*(pi^2-c),

    q1'=-2*p^3,
    q1=-pi^10/5+3*c*pi^8/4-c^2*pi^6+c^3*pi^4/2+b0.

The derivative identity is exact for every b0. This integration constant does not equal the intercept B and does not shift pi. It changes q1 alone; a physical source translation changes the whole polynomial pair and its centres.

`box/g9966-20260903/xu_joint_extension/xu_joint_extension.py:202-210` expressly keeps a symbolic b0 in B[0]. Lines 317-329 then obtain the first nonzero cokernel row

    -(2/5)*c_11_0*pi=0

while b0 is still free. Thus the h coefficient identity c_11_0=0 used by the current branch map is independent of setting b0=0. More generally the reduced equation is written using derivatives of Q, so Q -> Q+constant is an additive symmetry of this auxiliary local equation. This is not a demonstrated source or target automorphism of a full Keller pair. A later effective-T3 membership bridge must not infer such an automorphism from the local integration freedom.

For the present F/G/h projected chart, adjoining b0 changes its coordinate ring R/I to (R/I)[b0], because all generators are independent of it. Therefore the projection onto h,F,G is identical with b0 arbitrary or with b0=0, and an exact unit certificate in R/I is unchanged after adjoining b0. This is the precise harmlessness relevant to the centre audit. Calling b0 a consumed physical translation is a variable-identification error. Calling the auxiliary slice a licensed global gauge without an explicit group element would also be an error.

## 5. The resulting support statements for both branches

After A is gauged to zero, K3(t,w)=t^11*h3(t^(-1),w/t) has the fixed top w^3*(w-1)^8. Write z=w-1. At t=s^3, z=pi*s^4, each monomial t^r*z^q maps to pi^q*s^(3r+4q). For fixed weight, different q have different powers of pi; for fixed q, the weight determines r. Cancellation cannot raise a nonzero minimum. The tower order ord_t h3(D2)=-1/3 is equivalent to ord_s K3=32. Its leading coefficient is pi^8, so every lower-box coefficient with 3r+4q<32 vanishes, and any additional coefficient at weight 32 also vanishes. Thus every unknown remaining beyond the fixed face satisfies

    3r+4q>=33.

For 1<=r<=11 and 0<=q<=11-r there are 66 lower positions and 21 survive. The engine's mixed basis t^r*z^vmin*w^(degree-vmin) has vmin=ceil((33-3r)/4) and is triangular in z. Hence its 45 zeroed positions are exactly the forbidden coefficients on this centered slice.

Similarly ord_t h2(D2)=-1 gives ord_s K2=96 for K2=t^33*h2. Once the tower face (pi^3-1)^8 is established, every coefficient off that face satisfies 3r+4q>=97, matching engine lines 317-326 and 363-374. This is the centre repair of that floor, not a fresh proof of the full K2c coordinate change or of all face identities.

For outer coefficient blocks, Moh's order lower bound and this same centered monomial argument justify the necessary inequalities 3r+4q>=W0 with W0=(189,285,93,189) for (A2,A3,B1,B2). Only strict-below rows are discarded as zero. No outer equality face is licensed by the support argument.

Both principal-minor branches use this same major D2 and the same translations. Their later local split orders 2 and 5/2 do not create extra centre coefficients in the major D2. Thus no centre coordinate needs to be freed after the valid simultaneous gauge, for either branch. On a deliberately ungauged chart the minimal geometric addition is the one major intercept A (or two intercepts A,B if neither translation has been used), with translated polynomial coefficient relations; it is not 45 unrelated independent h3 directions.

## 6. Checks performed here and limits

A foreground SymPy/AST check verified: (i) b0 occurs only in metadata at engine line 278; (ii) the translated intercept-product identity; (iii) P o A=gamma^8*delta^3*P; (iv) q1'+2p^3=0 with b0 free; (v) exactly 66 lower h3 positions and 21 above the proved floor. All passed over exact rational-symbolic arithmetic. The parent lane separately verifies the frozen inputs; this note reads the sibling engine from the repository as the user requested.

No assertion about exact-Q UNIT is made by this note. The verdict for centre theory alone is **DISCHARGED for both (99,66) branches**. The elimination lane should retain the independent b0 argument, the simultaneous translation map, and the Galois-stable D2-cluster lemma in any renewed necessity statement. An enlarged arbitrary support chart may be useful as a check, but its NONUNIT would not contradict this orbit-covering centre proof.
