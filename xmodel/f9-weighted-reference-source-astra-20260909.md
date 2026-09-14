# F9 weighted reference: polynomial first contact is H-divisible

Author: Astra /root/model_productivity, 2026-09-09. Basis 0d39df3c9fd69c939a8420c54d03228b9077777d is provenance. Status: NEW PROSE PROOF, UNREVIEWED. Absolute deadline 06:34 UTC. ZERO mathematical subprocesses of any size; no source/pair expansion or coefficient emission. The source/map/ratio inputs are accepted at AUDIT16a/b; the theorem below is not yet promoted.

## 1. Exact conclusion and source scope

Let k be a characteristic-zero field. Suppose A,B in k[g,p] have (2,1)-weighted degrees21,35, weighted leaders H^3,H^5, and

    H=p*(p^2-g)^2*(p^2-(3/2)g),     [A,B]_(g,p)=c*g, c in k*,

where the bracket orientation is X_g Y_p-X_p Y_g. These are necessary conditions of the normalized actual F9 source supplied by accepted16a/b. The full lower faces and inverse ordinaryness are NOT additional premises used in this proof. We prove a necessary polynomial-reference conclusion, not existence or nonexistence of such a pair.

Set A_s=s^21 A(s^-2 g,s^-1 p) and B_s=s^35 B(s^-2 g,s^-1 p). There are finite polynomials R_s,F,G in k[s,g,p], scalars alpha,a0,b0,...,b4 in k, with the precise decomposition in Sections3–4, such that:

1. R_s is combined-weight7 for wt(s,g,p)=(1,2,1), has s=0 value H, and is polynomial without localization at p.
2. F=A_s-R_s^3-alpha*s^14*R_s-a0*s^21 is nonzero. Its first s-order j satisfies1<=j<=13.
3. F_j=H*C for a nonzero weighted-homogeneous C of weight14-j, and H does NOT divide C. Equivalently H^2 does not divide F_j.
4. With all five lower B scalar kernels retained, ord_s G>=2j, including infinity, and the exact identity [A_s,B_s]=[R_s,T]+[F,G] holds with every alpha,b4,tau,delta term as stated below.

The stronger bound and divisibility use the order3j equation, not merely the earlier square-divisibility equation. The intermediate independent conclusion is rad(H)|F_j and j<=16. No claim eliminates the remaining H-divisible branch; in particular the p-sensitive direction H^2/p at j=8 remains compatible with these necessary conclusions.

Accepted source coverage is over C after a finite coefficient-field embedding; the present algebraic theorem is over any characteristic-zero k satisfying its displayed hypotheses. It supplies no chosen normalization descending to an arbitrary original field, no scheme-level statement over nilpotents, no reverse lift, ideal certificate or JC2 conclusion.

## 2. Exact quadratic cover and elementary polynomial centralizer

Use new independent variables a,b and the injective substitution g=a^2,p=b. Write the pulled-back source as mathcal A(a,b),mathcal B(a,b), and put

    M=b^2-a^2,   V=b*(b^2-(3/2)a^2),   K=M^2*V.

Then mathcal A,mathcal B have ordinary degrees21,35 with top forms K^3,K^5, are even in a, and

    [mathcal A,mathcal B]_(a,b)=2*c*a^3.

The factor2a comes from the cover Jacobian, so it multiplies c*a^2; the sign is positive. The cover is not declared birational or a Keller transformation. Its even subring is exactly k[a^2,b], so polynomial objects shown even in a descend uniquely.

Here ker[K,-]=k[K] on k[a,b], with no generic-fibre theorem needed. If a nonzero homogeneous U of degree r commutes with K, Euler gives

    a*K_a+b*K_b=7K,    a*U_a+b*U_b=rU.

In k(a,b), proportionality of dU,dK from their zero wedge, followed by these two Euler identities, gives dU=(rU/(7K))*dK. Hence both partial derivatives of U^7/K^r vanish. A rational function over a characteristic-zero field with both partial derivatives zero belongs to k, so U^7=lambda*K^r for lambda in k*. Because ord_b K=1, valuation at the polynomial prime b gives7 ord_b U=r. Thus r=7n for an integer n>=0. The same differential identity now gives d(U/K^n)=0, hence U/K^n is in k. No seventh root in a coefficient-field extension is presumed.

For the rational-constant assertion used here, view a rational function first as an element of k(b)(a): zero a-derivative in characteristic zero puts it in k(b); zero b-derivative then puts it in k. For an arbitrary polynomial U, the brackets with its different ordinary homogeneous components have distinct degrees r+5. Each component therefore commutes separately and the preceding argument applies. This proves the claimed polynomial centralizer over k itself. The simple b valuation is used explicitly; reducedness of the whole K=0 divisor is neither true nor used.

Define the finite homogeneous dilations

    mathcal A_s=s^21*mathcal A(a/s,b/s),
    mathcal B_s=s^35*mathcal B(a/s,b/s).

Give s,a,b degree1 and differentiate only a,b. Then

    [mathcal A_s,mathcal B_s]=2*c*s^51*a^3.             (2.1)

Indeed the bracket contributes s^(21+35-2) and the substituted target contributes s^-3. Both sides have combined degree54. This is the target51, not the constant-J target54 or the old degree15/25 target36. On descent it is equivalently [A_s,B_s]=c*s^51*g for weighted dilation wt(g,p)=(2,1).

## 3. Canonical polynomial A reference; no division by b

Fix lexicographic monomial division a>b. The leading monomial of K is (-3/2)*a^6*b and that of K^2 is (9/4)*a^12*b^2. The leading coefficients are fixed field units.

Starting with K, construct

    R=K+sum_(q=1)^7 s^q R_(7-q)

successively. At stage q divide the order-q coefficient of mathcal A_s minus the cube of the reference already constructed by3K^2. Use the homogeneous quotient as R_(7-q). The division remainder contains no monomial divisible by a^12*b^2. Adding this coefficient to R changes its cube at order q by exactly3K^2 R_(7-q), and only later orders otherwise. Single-divisor monomial division terminates and preserves homogeneity; it inverts only the fixed leading coefficient, never b or K.

At order14 divide the degree7 residual of mathcal A_s-R^3 by K. Its quotient is a scalar alpha. Put alpha_s=alpha*s^14 and choose the scalar a0 to kill the remaining order21 constant after subtracting alpha_s R. Define

    F=mathcal A_s-R^3-alpha_s*R-a0*s^21.              (3.1)

The first seven residuals are LM(K^2)-normal; F_14 is LM(K)-normal; F_21=0. The reference includes its order7 constant correction, so a possible scalar quadratic term of A's reference is absorbed rather than omitted. No target shear or deletion of an original source coefficient has been performed.

F is nonzero. Otherwise (2.1) would factor over k(s)[a,b] as

    (3R^2+alpha_s)*[R,mathcal B_s]=2*c*s^51*a^3.

The first factor has ordinary(a,b)-degree14 and the nonzero right side degree3. Degrees add for a nonzero product in this polynomial domain, a contradiction. Thus

    1<=j=ord_s F<=20,    deg_(a,b) F_j=21-j.         (3.2)

Also K^2 does not divide F_j: for j<=7 a nonzero K^2 multiple cannot be LM(K^2)-normal, and for j>=8 its degree is at most13<14. This is polynomial normality, not normality after inverting b.

All these objects are even in a. At every division step an even-a dividend and even-a divisor with even-a leading monomial give an even-a quotient and remainder: subtracting a quotient monomial preserves that parity. Scalar operations do so as well. Consequently R,F descend to k[s,g,p], with combined weights7,21. No odd TOTAL parity has been imposed; every order1,...,7 of the reference is allowed.

## 4. All five B kernels and the exact identity

For i=0,...,4 set beta_i=b_i*s^(35-7i), with b_i in k. Define, in an independent scalar variable z,

    f_B(z)=z^5+beta4*z^4+beta3*z^3+beta2*z^2+beta1*z+beta0,
    q(z)=(5/3)z^2+(4/3)beta4*z+beta3-(5/9)alpha_s,
    tau=2beta2-(4/3)beta4*alpha_s,
    delta=beta1-beta3*alpha_s+(5/9)alpha_s^2,
    G=mathcal B_s-f_B(R)-q(R)*F.

Primes below mean differentiation in z, not a,b. The exact scalar identity is

    f_B'(z)=(3z^2+alpha_s)q(z)+tau*z+delta.

Taking the exterior product in the FORMAL independent R,F,G symbols, with s constant, gives

    [mathcal A_s,mathcal B_s]=[R,T]+[F,G],
    T=(3R^2+alpha_s)G-(tau*R+delta)F
                         -((5/3)R+(2/3)beta4)F^2.     (4.1)

The respective dR wedge dF, dR wedge dG and dF wedge dG coefficients are -(tau R+delta)-q'(R)F, 3R^2+alpha_s, and1. This verifies the identity without expanding any actual source power. In particular alpha_s, beta4, both tau summands, all three delta summands, a0 and beta0 have not disappeared. Constants a0,beta0 have zero a,b differential but remain in the decomposition.

Orders are ord alpha_s>=14, ord beta4>=7, ord tau>=21 and ord delta>=28, with infinity allowed when a scalar vanishes. G is a finite even-a polynomial of combined degree35, and T is such a polynomial of combined degree49, or zero.

One may make the B choice canonical as well. Initialize the five reference coefficients b_i to zero, without changing mathcal B_s. In the order l=7,14,21,28,35, project the current homogeneous G_l of degree35-l onto the scalar multiple of K^(5-l/7) by the same single-divisor monomial division. Choose the corresponding b_(5-l/7) to remove that scalar quotient; at l=35 the divisor is1 and this removes the constant. Each is a scalar coefficient choice, not an additional source equation. For an increment e, the exact changes in G are respectively

    -e*s^7*(R^4+(4/3)R*F),
    -e*s^14*(R^3+F),
    -e*s^21*R^2,    -e*s^28*R,    -e*s^35.            (4.2)

They affect the designated order and later orders only. Thus each selected coefficient remains normal in the final G. This retains all five kernels, including ones above the first-contact range, without declaring any original B coefficient zero.

Now ord_s G>=2j. If the first nonzero G_l had l<2j, all earlier coefficients in (4.1) would vanish and the order-l equation would be

    [K,3K^2 G_l]=0.

The reasons are exact: F^2 begins at2j; (tau R+delta)F begins no earlier than21+j>2j by j<=20; [F,G] begins at j+l>l; alpha_s and non-leading R coefficients cannot affect the first G order; the target begins at51>2j because2j<=40. The polynomial centralizer forces G_l to be a scalar K-power. Its degree35-l permits only l=7,14,21,28,35. The chosen scalar projection at that very order then makes G_l zero, a contradiction. Hence

    ord_s G>=2j.                                     (4.3)

The proof covers G=0. It does not import the false general3e/5e estimate: here the actual scalar remainder has first possible order21>j, whereas that inequality failed in the accepted proper-power low-order control.

## 5. The order2j equation: an independent j<=16 bound

At2j<51, all terms of (4.1) other than the leading G and F^2 contributions are later. Therefore

    [K,3K^2 G_(2j)-(5/3)K F_j^2]=0.                (5.1)

The inner polynomial has degree49-2j. For integer1<=j<=20 the only possible nonzero homogeneous polynomial-centralizer values are a scalar K^5 at j=7, or a scalar K^3 at j=14. Otherwise it is zero. All are divisible by K^2, so (5.1) implies

    K divides F_j^2.

M and V are coprime and squarefree in k[a,b]; their irreducible factors have the stated multiplicities2 and1 in K=M^2V. This remains true if b^2-(3/2)a^2 is irreducible over k. Unique factorization therefore gives

    F_j=M*V*C0,   deg C0=16-j,    1<=j<=16.         (5.2)

No coefficient-field root choice is needed. At the same time

    G_(2j)=(5/9)*V*C0^2 + Z,

where Z=0 except possibly a scalar K^3 at j=7 or a scalar K at j=14. These scalar possibilities must not be silently discarded. They will be handled in the next section.

## 6. All lower T terms can be removed without changing the identity

By (5.2), 3j<=48<51. Also [F,G] has order at least3j. Begin with T from (4.1), which has order at least2j. For each successive q<3j, after its earlier coefficients have been removed, the coefficient equation is

    [K,T_q]=0.

T_q is homogeneous of degree49-q. If nonzero, it is e_q K^n for n=(49-q)/7 a nonnegative integer. Subtract e_q*s^q*R^n from T. This kills that coefficient and changes only later coefficients; it has combined degree49 and commutes EXACTLY with R. Thus it does not change [R,T], F, G, or the source identity. All q used here are below48 and below49, so a nonzero such n is positive; zero coefficients are simply skipped.

After these finitely many subtractions obtain a polynomial Ttilde with ord_s Ttilde>=3j and

    [mathcal A_s,mathcal B_s]=[R,Ttilde]+[F,G].

The procedure is not an assertion that T already vanishes below3j. In particular it retains and removes, when appropriate, the scalar K^5/K^3 term at2j together with the later R corrections it generates. Every beta4, alpha, tau, delta and reference correction remains in Ttilde unless absorbed by an exactly commuting scalar polynomial in R.

At order3j, with no target term because3j<51, the COMPLETE equation is

    [K,Ttilde_(3j)]+[F_j,G_(2j)]=0.                 (6.1)

There is no omitted mixed term: R's positive-order coefficients multiply Ttilde coefficients below3j, all zero, and the only product of F/G coefficients of total order3j is F_j with G_(2j). This exact isolation is what permits the following restriction; no unproved source-isolation hypothesis is added.

## 7. The two M branches force one more factor

Every partial derivative of K=M^2V is divisible by M, so [K,Ttilde_(3j)] is divisible by M for ANY polynomial Ttilde_(3j). The possible scalar Z in G_(2j) also causes no problem: for each positive n, [F_j,K^n]=n K^(n-1)[F_j,K] is divisible by M. Thus (6.1) modulo M reduces to

    [M*V*C0,(5/9)*V*C0^2]=0 modulo M.               (7.1)

The product rule, keeping the terms not already divisible by M, gives

    (5/9)*V*C0^2 * ( [M,V]*C0 + 2V*[M,C0] )        (7.2)

modulo M. Let d=deg C0=16-j>=0. There are two distinct factors b-epsilon*a with epsilon=+1,-1, both over k. Direct degree-three differentiation and Euler homogeneity give

    [M,V]=3a^3,
    V(a,epsilon*a)=-(epsilon/2)a^3,
    [M,C0](a,epsilon*a)=-2epsilon*d*C0(a,epsilon*a).

The last identity is Euler's a*C0_a+b*C0_b=d*C0 restricted to that line; it does not assume a monomial C0 or generic nonvanishing of a point. Substituting into (7.2) yields

    (5/9)*(3+2d)*a^3*V(a,epsilon*a)*C0(a,epsilon*a)^3=0

as a polynomial identity in the domain k[a]. The scalar3+2d is nonzero in characteristic zero, and a^3 V(a,epsilon*a) is a nonzero polynomial. Hence C0(a,epsilon*a)=0 identically for BOTH signs. The two distinct linear primes divide C0; their product M divides C0. No localization at a or passage to a point of the line was required.

Consequently

    K divides F_j.                                  (7.3)

This includes vanishing G_(2j), vanishing scalar Z, and both exceptional scalar orders j=7,14. It uses the strict3j<51 obtained from the separate radical bound. Were the target to appear at3j, (6.1) would have an extra right-hand side and this argument would not prove (7.3).

Write F_j=K*C. Its degree is21-j, so deg C=14-j. If j>14, divisibility is impossible by degree. If j=14, C is a scalar and the chosen LM(K)-normal F_14 cannot be a nonzero scalar K. Therefore

    1<=j<=13,   F_j=K*C,   deg C=14-j,   K does not divide C.

The last assertion is the independent K^2-normality from Section3. This is the claimed conclusion on the cover, with no new local consumer.

## 8. Descent, retained p-sensitive direction, and scope controls

R,F,G and K are even in a. Since K is nonzero, the quotient C=F_j/K is even in a as well. All therefore descend uniquely through g=a^2,p=b to k[s,g,p], and ordinary homogeneous degree on the cover becomes (2,1)-weighted degree. T in (4.1) is even by its displayed products too. Each bracket of two even polynomials is2a times the pullback of its (g,p)-bracket; cancellation of the nonzero polynomial2a in the domain gives the descended exact identity. K-divisibility and K^2-nondivisibility descend to the corresponding statements for H in the polynomial ring, not its localization. This proves Section1.

The p-sensitive direction survives. On the cover the polynomial K^2/b has degree13 and so corresponds to j=8. It is divisible by K but not by K^2 in k[a,b]. Its quotient K/b is polynomial, vanishes on the M and b^2-(3/2)a^2 branches, but lacks the b factor. On descent this is H^2/p, the face-interior direction from the0445 cross. It satisfies the new first-contact divisibility conclusion, not the full Jacobian equation or a source-realization theorem. No complete pair is constructed by mentioning that one factored coefficient. This proof gives no right to absorb its quotient1/b into a polynomial R or to replace the full polynomial normality by a generic two-branch field test.

Manual changed-hypothesis controls are part of the prose, not executed tests:

- The ramified cover has determinant2a; omitting it changes the target and its order. The correct cover target is2c*s^51*a^3.
- F=0 is excluded by factor degree14 versus target degree3, not by a constant-J assumption.
- Dropping the b4 kernel removes both its contribution to q and its contribution to tau and the F^2 coefficient; (4.1) would then describe a different decomposition.
- K^2 is not absorbed by a Laurent quotient: only monomial polynomial division using fixed field units is used. K^2/b demonstrates the difference.
- A hypothetical target at3j invalidates the homogeneous zero equation (6.1); a characteristic with3+2d=0 invalidates the final scalar step. Neither is within the theorem's hypotheses.
- Using only one M branch would not justify the product factor without further symmetry; this proof restricts to both, even though the actual cover has even-a symmetry.

No assertion is made over a nilpotent coefficient ring; domain and characteristic-zero arguments are explicit. No claim excludes the remaining H-divisible source, all84/140 sources, maximum140, or JC2. No reverse-polynomiality result, live reverse gate or D108 argument was consumed.

## 9. Read scope, history and terminal obligations

The three accepted source/map/ratio reports were whole-read in the preceding fixed cross packet and their CURRENT originals were rehashed unchanged before this proof. The independent joint gate was then read WHOLE. Exact hashes are retained in owned input-pins. The relevant complete16a/b entries in AUDIT were read at their accepted scope. A scoped label search incidentally returned one older accepted high-alpha ledger sentence; it is not a mathematical premise and no underlying report was opened.

Reference comparison was restricted to late-contact-keller-descent-astra-20260909.md §§3–4 and d125-weightfree-reference-source-astra-20260909.md §§2–4, each at the exact parent-supplied current hash. A clipped portion of the first reference was reread separately. Their source hypotheses and conclusions were NOT imported wholesale: Sections2–7 above rederive the centralizer, cover target, polynomial normalizations, all order comparisons, and third-order restriction for this actual source. The old degree5 boundary can have3j=36 at j12; our independent degree7 radical bound gives3j<=48<51, explaining the additional strict step rather than asserting a theorem rename.

This is a new campaign proof candidate, not a literature-novelty assertion. Only pure factored prose was used. No mathematical subprocess of any size, old checker, source power construction, coefficient stream, CAS, web, AWS/SSH, agent, shared/protected/public edit, live gate or D108 report read occurred. After whole-own-body and owned OPEN extraction, the report will be transactionally sealed and all writers returned IDLE. No follow-on is authorized.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — no explicit OPEN identifier is raised; no corpus scan is claimed.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19513`.
- Body SHA-256:
  `b20ac98196bd5b7e523c6fe030244c159d4488bc9c9585ce1e23a4e759262e36`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
