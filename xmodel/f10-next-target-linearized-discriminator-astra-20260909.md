# The next-target linearized problem is uniformly compatible

September9,2026; owner /root/model_productivity. **UNREVIEWED standalone linearized theorem.** The only scientific premise is the literal polynomial ODE below, as a hypothesis. No source realization, intervening-weight theorem, previous fixed-A obstruction or live review is a premise. ZERO mathematical subprocesses; all arguments are manual and factored.

## 1. Exact result

Let K be a characteristic-zero field, q>=0 an integer, and

    r=q+1,       m=3r+1,       n=5r+2,       k0=2m+r=7r+2.

Let monic C,D in K[T], of degrees3,5, satisfy

    nTC'D-mTCD'-CD=-c,       c!=0.                        (1)

Put T=p^r Z^m, A0=pC(T), B0=p^2 ZD(T). Consider precisely the weight-drop-k0 polynomial variations with the degree bounds in the task. They are exactly

    deltaA=(Z/p)U(T),       U(0)=0, deg U<=3,
    deltaB=Z^2 F(T),        deg F<=5.                      (2)

The equation

    [A0,deltaB]+[deltaA,B0]=-cZ                            (3)

has a solution for EVERY pair C,D satisfying(1). In fact its ENTIRE solution set within(2) is the affine line, with parameter a in K,

    U_a=-(m/2)TC'+a T(TC'-3C),
    F_a=-(D+mTD')/2+a T(TD'-5D).                          (4)

There is no exceptional coefficient sublocus hidden in this conclusion. The nonzero constant c is essential to the completeness argument. The parameter a here is a scalar, not a source or cover coordinate.

For epsilon^2=0 these formulas give the exact identity

    [A0+epsilon*deltaA, B0+epsilon*deltaB]
        =c(p^2-epsilon*Z)

in K[p,Z,epsilon]/(epsilon^2). This rules out an impossibility argument based only on the stated linearized system. It neither supplies an actual source pair nor a polynomial solution at epsilon=1.

## 2. Rechecking the whole starting bracket and variation space

In the actual polynomial coordinates(p,Z), direct differentiation gives

    (A0)_p=C+rTC',            (A0)_Z=m p T C'/Z,
    (B0)_p=pZ(2D+rTD'),       (B0)_Z=p^2(D+mTD').

Quotients here abbreviate ordinary polynomials, since r>=1,m>=4. Thus

    [A0,B0]=p^2{CD+mTCD'-(2m-r)TC'D}=c p^2,

using 2m-r=n and(1). The positive sign is fixed in(p,Z); no source change of coordinates is being assumed.

For the integer grading wt(p)=m,wt(Z)=-r, T has weight0, A0 has weight m, and B0 has weight2m-r=n. At drop k0 the required variation weights are -m-r and-2r respectively.

A monomial p^i Z^j of weight -m-r satisfies m(i+1)=r(j-1). Since gcd(m,r)=1, it has

    i=r*l-1,       j=m*l+1,

where ordinaryness forces l>=1. These are exactly the monomials(Z/p)T^l. Their positive degree for deg_(1,2), meaning degree weight1 on p and2 on Z, is k0*l+1. As7m=3k0+1, the bound<=7m is EXACTLY l<=3. No negative p exponent occurs, even at q=0,r=1.

Likewise mi-rj=-2r implies i=r*l,j=m*l+2 with l>=0. These are exactly Z^2 T^l, of positive degree k0*l+4. Since7n=5k0+4, the bound<=7n is EXACTLY l<=5. This proves completeness of(2), not just containment. The original spaces have dimensions3 and6 over K.

The grading isolates only the stated linearized weight. There is no claim that an actual source has no corrections at other weights, or that nonlinear products of such corrections cannot contribute later.

## 3. The exact linearized operator

For deltaB=Z^2F(T), the same product rule gives

    [A0,deltaB]=Z{mTCF'+(2rTC'+2C)F}.

For deltaA=(Z/p)U(T),

    (deltaA)_p=(Z/p^2)(-U+rTU'),
    (deltaA)_Z=(1/p)(U+mTU').

Combining these with the derivatives of B0 yields

    [deltaA,B0]=Z{-nTDU'-((m+r)TD'+3D)U}.

The tied T^2 U'D' terms cancel, and r-2m=-n. Therefore(3) is precisely L(U,F)=-c, where

    L(U,F)=mTCF'+(2rTC'+2C)F
              -nTDU'-((m+r)TD'+3D)U.                    (5)

The equality is in the entire ordinary polynomial ring. No matrix or finite-parameter computation has been performed.

## 4. A polynomial change of unknowns with determinant c

Introduce polynomial h,v by

    U=C h+TC'v,
    mF=nD h+(D+mTD')v.                                   (6)

The matrix of(6) has determinant

    C(D+mTD')-nDTC'=CD+mTCD'-nTC'D=c,

by(1). Since c is a nonzero field scalar, (6) is an invertible POLYNOMIAL change of unknowns, not localization at a coefficient polynomial. Explicitly

    h=((D+mTD')U-mTC'F)/c,
    v=(mCF-nDU)/c.                                       (7)

Equation(1) at T=0 gives C(0)D(0)=c, so C(0),D(0)!=0. Hence U(0)=0 is equivalent to h(0)=0 in(6).

The operator simplifies to the exact identity

    L(U,F)=(c/m){(m-2r)h+2v+mTv'}.                      (8)

Here is a factored verification that also checks its orientation. In the localization K[p,p^-1,Z] define k=(v-rh)/m and the auxiliary rational vector field

    X=(Z/p)h(T)*partial_p+(Z^2/p^2)k(T)*partial_Z.

It satisfies X(T)=(Z/p^2)T v, and(6) gives X(A0)=deltaA, X(B0)=deltaB. Differentiating a two-by-two determinant gives

    [X(A0),B0]+[A0,X(B0)]
       =X([A0,B0])+[A0,B0] div X
       =div(c p^2 X).

The last expression is

    cZ{h+2k+rTh'+mTk'}
       =(cZ/m){(m-2r)h+2v+mTv'},

which proves(8). All variations specified in(2) are polynomial, and the original polynomial ring embeds in this localization, so this proves their polynomial identity. X is a proof device, NOT a claimed regular coordinate change or source gauge.

In particular the simple choice h=0,v=-m/2 gives k=-1/2 and

    X=-Z^2/(2p^2)*partial_Z.

Its images of A0,B0 are the polynomial variations in(4) with a=0. Their Jacobian variation is div(-cZ^2/2*partial_Z)=-cZ. Thus compatibility already has an explicit verified representative before the completeness argument.

## 5. Complete classification under the degree restrictions

Set b=m-2r=r+1!=0. The required equation becomes

    b h+2v+mTv'=-m,       h(0)=0.                        (9)

Its constant term forces v(0)=-m/2, and

    h=(-m-2v-mTv')/b.

Suppose deg v=s>=2 and its leading coefficient is v_s!=0. The leading coefficient of h is -(2+ms)v_s/b. Since C is monic cubic, the term of degree s+3 in U=Ch+TC'v has coefficient

    {3b-2-ms}v_s/b = m(1-s)v_s/b,

using3b-2=m. It is nonzero in characteristic zero. This contradicts deg U<=3. Thus v has degree at most1. Together with its constant term, necessarily

    v=-m/2+aT,       h=-3aT,

because m+2=3b. Substitution in(6), using3n=5m+1, gives exactly(4).

Conversely every a in K gives admissible degrees: TC'-3C has degree<=2 and TD'-5D has degree<=4, since C,D are monic of degrees3,5. Thus U_a has degree<=3 and zero constant, F_a has degree<=5, and(9) proves L=-c. This verifies both directions and every degree endpoint without a computed rank.

The associated homogeneous kernel is exactly

    K*( T(TC'-3C), T(TD'-5D) ).

It is nonzero, since the first component has T-coefficient -3C(0)!=0. Hence the nine-dimensional coefficient operator into polynomials of degree<=8 has kernel dimension1 and rank8. Its image need not be all nine-dimensional target space, but the PARTICULAR constant target -c is always in that image. This distinction prevents an irrelevant cokernel count from being mistaken for an obstruction to the requested target.

## 6. Optional highest-form preservation remains compatible

The stated problem imposes degree bounds, not an additional fixed-top condition. For clarity, even this natural extra linear condition causes no obstruction. Put lambda=[T^2]C and d4=[T^4]D. The coefficient of degree7 in(1), whose degree8 term cancels, is

    m d4-n lambda=0.

Thus d4=(n/m)lambda. Moreover lambda!=0 follows from the ODE alone: write f(x)=x^3C(1/x), d(x)=x^5D(1/x), so f(0)=d(0)=1 and

    m f d'-n f'd=-c x^7.

With a0=n/m, formal integration of the logarithmic derivative gives d-f^a0=O(x^8). If lambda=0, write f=1+mu x^2+nu x^3, with nu=C(0)!=0. The degree6,7 coefficients of f^a0 must vanish and are

    (a0)_2 nu^2/2+(a0)_3 mu^3/6,
    (a0)_3 mu^2 nu/2.

Here a0 is neither0,1,2. The second forces mu=0 and the first then contradicts nu!=0. This is a manual coefficient projection, not a sampled or executed test.

The notation (a0)_j in these formulas means the falling factorial a0(a0-1)...(a0-j+1).

In(4) the highest U and F coefficients are

    U_3=-3m/2-a lambda,
    F_5=-3n/2-a d4.

Therefore the UNIQUE choice a=-3m/(2lambda) makes BOTH zero. By Section2 this lowers the positive degrees of the variations strictly below7m,7n and preserves the displayed highest deg_(1,2) forms of A0,B0. It still says nothing about any other source boundary, polynomial inverse, canonical reference or nonlinear integrability.

### 6.1. Additional polygon and fixed-opposite-face tests

These are EXTRA literal coefficient conditions, not hypotheses of the original linearized problem or an actual-source exhaustiveness claim. Substitute g=p^2-Z and let Delta={I,J>=0,2I+J<=7,I-J<=2}. For a variation term(Z/p)T^k, its greatest anti-diagonal degree I-J in(g,p) is

    (m-r)k+2=(2r+1)k+2.

For a term Z^2T^k it is the SAME expression. This follows by taking the maximal g monomial in the Z power; the positive degree remains exactly the value computed in Section2. All p exponents are nonnegative.

If U_3!=0, its maximal anti-diagonal degree is2m+3, outside mDelta. No lower k has the same maximal weight to cancel it. Similarly F_5!=0 produces degree2n+3 outside nDelta. Therefore the full support envelopes themselves force U_3=F_5=0, selecting exactly the top-preserving solution already found.

For that solution, k<=2 in U and k<=4 in F. Their greatest possible anti-diagonal degrees are4r+4 and8r+6. They are below2m and2n by2r-2. Thus for r>1 the variations lie in the full polygons and strictly below BOTH opposite faces, preserving those existing faces. For r=1,q=0 they still lie in the polygons, but their k=2 and k=4 terms attain the opposite faces. Requiring ZERO change of those faces imposes U_2=F_4=0.

Write mu=[T]C. The unique top-preserving solution has

    U_2=m(3mu/lambda-lambda),
    F_4=(n/m)U_2.                                       (10)

To verify the second formula, the reciprocal contact already proved gives

    d3:=[T^3]D=(n/m)mu+((n/m)(n/m-1)/2)lambda^2.

Insert this and d4=(n/m)lambda into

    F_4=-(1+4m)d4/2+(3m/lambda)d3;

using3n=5m+1 gives(10). Hence at q=0 the extra zero-face-variation condition is exactly mu=lambda^2/3.

### 6.2. The q=0 ODE forbids that extra fixed-face condition

Here m=4,n=7. The monic scaling C_t(T)=t^-3C(tT), D_t(T)=t^-5D(tT) preserves(1), with c replaced by t^-8c. Taking t=lambda!=0 normalizes lambda=1. The extra condition becomes mu=1/3. The reciprocal polynomial is then

    f(x)=1+x+x^2/3+w x^3=(1+x/3)^3+b x^3,
    b=w-1/27.

The degree6 and7 coefficients of f^(7/4) must both vanish. Up to degree7, its binomial decomposition has exactly the three factored terms

    (1+x/3)^(21/4)
      +(7/4)b x^3(1+x/3)^(9/4)
      +(21/32)b^2 x^6(1+x/3)^(-3/4).

Set P6=binom(21/4,6)/3^6 and Q6=(7/4)binom(9/4,3)/3^3. Direct cancellation of these short rational products gives

    Q6=35/4608,       s:=P6/Q6=221/17280.

The two coefficients are exactly

    f6=P6+Q6*b+(21/32)b^2,
    f7=-P6/28-Q6*b/16-(21/128)b^2.

For example the ratios -1/28 and-1/16 are the respective adjacent binomial-coefficient ratios, and the last coefficient uses[x](1+x/3)^(-3/4)=-1/4. Thus f7+f6/4=0 forces b=-(8/7)s=-221/15120. At that unique candidate,

    f6=s(6s-Q6)/7=(221/17280)*(177/17920)!=0.

This is a nonzero rational number in every characteristic-zero field, not an appeal to an order or a numerical sample. The two contact conditions contradict each other. Consequently q=0 has no solution to the EXTRA test which simultaneously freezes these opposite-face coefficients and the highest forms, whereas q>=1 retains the unique compatible solution with those zero-variation requirements.

### 6.3. Why this is NOT a q=0 source obstruction

The source base-point premise fails for this extra test. The constructed A0,B0 themselves have collapsed opposite faces

    (-1)^m g^(3m)p^m,       (-1)^n g^(3n)p^n,

not the fuller binomial faces (-1)^e g^(2e)(gp+1)^e. To check this independently, in p*T^i and p^2Z*T^j the maximal anti-diagonal degrees are i(m-r)-1 and j(m-r)-1. Their unique maxima occur at i=3,j=5 and at the maximal g term in each Z power, giving the two monomials above. In particular the nonzero g^(2e) constant-p source vertices are absent.

Freezing the existing faces of A0,B0 therefore does not impose the actual binomial source equations at a valid source base point. A relevant source deformation might need a NONZERO prescribed face variation, not the zero variation tested here. Lower-weight terms may also contribute nonlinearly at the target gap. For instance a reference term -Z^2 relative to pZ^3 has grading drop2r+1; at q=0 this is3, and products of three such drops reach9=k0. This is only a direct weight calculation illustrating the missing implication, not an imported or proved complete source normal form.

Thus the q=0 finding is a changed-hypothesis fixed-face TEST ONLY. It neither excludes an actual source nor shows that intervening corrections vanish. The original uniform dual-number compatibility and affine-line classification remain exactly as stated.

## 7. Meaningful controls and exact limits

All controls are manual, not executable test claims.

- Allowing U matters. If U is frozen to0 and F!=0 has degree s, the F-part of(5) has degree s+3 and leading coefficient (ms+6r+2)F_s!=0. It cannot equal -c. This restricted failure is not the answer with BOTH variations allowed; the explicit U in(4) changes it.
- The c!=0 hypothesis is load-bearing for completeness. Outside it, C=T^3,D=T^5 obey(1) with c=0, since3n-5m-1=0. Then U=T,F=(n/m)T^3 satisfy L=0. More generally F=(n/m)T^2U works for any U divisible by T of degree<=3. The determinant in(6) is now zero and the preceding affine-line classification cannot be imported. This is a changed-hypothesis control, not a solution of the c!=0 problem.
- Dropping U(0)=0 gives a term U(0)Z/p, which is not an ordinary polynomial and cannot cancel against its distinct nonnegative-p terms. Conversely at r=1, the allowed U_1 term has p-exponent0, so the boundary q=0 is genuinely included rather than accidentally excluded by an overly strict divisibility condition.
- The top-degree terms in T(TC'-3C) and T(TD'-5D) cancel exactly. Replacing them by uncanceled arbitrary T*C or T*D would introduce forbidden U_4 or F_6; the degree restrictions were checked, not waived for a putative symmetry.
- The rational vector field X proves a POLYNOMIAL first variation because its two images are polynomial. It is not a globally regular polynomial flow or coordinate automorphism. In particular there is no evaluation epsilon->1 from K[epsilon]/(epsilon^2) to K: such an evaluation would send0=epsilon^2 to1. A full target requires an additional integration argument that is not present here.

## 8. Scope, provenance and terminal status

This theorem is independent of the earlier fixed-A report. Its chain rule, support space, operator and cokernel/kernel statements have all been rederived from(1). Neither the optional accepted standalone ODE producer/review nor any live or mutable source report was needed or read. Root's separate source-reference discussion is not a scientific premise; the requested conditional weight illustration in Section6.3 is not used to treat this deformation as exhaustive.

The exact conclusion is UNIFORM COMPATIBILITY and a complete affine-line classification for the stated finite polynomial first-order deformation space, conditional on its literal ODE pair. It is not a whole F10, degree112/196, source-realization or JC2 result. Nonlinear contributions from intervening weights, coordinate changes and all additional boundary requirements remain outside the claim. No independent existence promotion is made here.

The owned INPUT.md and READ-SCOPE.md freeze this problem and the no-source perimeter. No mathematical subprocess of any size, matrix/resultant calculation, CAS/toy script, coefficient emission, source powers, AWS/SSH, external model, agent, protected project or shared/public write occurred. Metadata and existing own transactional publication only. Own whole/open check precedes BODY-END; terminal custody is the final metadata write, then all writers IDLE. No follow-on is authorized.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16270`.
- Body SHA-256:
  `89364311f3f14985fb4ca4a4f391bcfc6e48e441af663469d5b994ae116f7c34`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
