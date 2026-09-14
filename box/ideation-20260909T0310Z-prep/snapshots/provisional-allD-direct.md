# Direct late-contact obstruction: no global minimality is needed

2026-09-09. ROOT PURE-PROSE CANDIDATE, UNREVIEWED. This is a separate strengthening of the sealed conditional all-D descent report, not a replacement of its bytes. No mathematical subprocess, high-power expansion, source system or computer-algebra calculation was used.

The exact admitted parent inputs are the accepted finite late-T lemma in xmodel/late-contact-triple-endpoint-astra-20260909.md (b541308788da31f52e9f7985c7767e206231e8f3251ff53c1b2bd9c96b64f097) and its different-model gate (c9a399a87dc91d78bfc4f811249996ea3e217eda075be679cf27b41af5795c26). Both were whole-read with their recorded earlier terminal/current-pin checks. The new general constant-Jacobian reference construction in xmodel/late-contact-keller-descent-astra-20260909.md (857b2e2fa93cc14acb24fa590a2ffa76961a0d136113908f12b213e126889672) is PROVISIONAL. Root verified its terminal transaction, five owned and two current source pins BEFORE whole reading at02:47:41+, then independently checked its degree, wedge and reference-scalar reasoning. The direct lemma below is self-contained; its actual-source application explicitly charges that general framework for joint independent review. No pending triple/contact gate is an input.

## 1. A self-contained degree obstruction

Let K have characteristic zero. Fix polynomials r,f,g in K[u,v]. Assume:

- D=deg r>=3, with top homogeneous form H, and polynomial Hamiltonian centralizer ker[H,-]=K[H].
- m=deg f and n=deg g are positive integers satisfying D/2<m<D and n<=2m-D.
- [f,g]=c is a nonzero FIELD SCALAR.
- alpha,tau,delta,b4 are FIELD SCALARS, and t(Z) is in K[Z].
- The exact polynomial identity is

    (3r²+alpha)g-(tau*r+delta)f
          -(5r/3+2b4/3)f²=t(r).                 (C)

These hypotheses are inconsistent. In particular, no global or within-subclass minimality assumption is needed, and no polynomial inverse of(f,g) is assumed.

Proof. Set L=D+2m. The inequalities give 2D<L<3D. Every term on the left side of(C) has degree at most L:

    deg(3r²g)=2D+n<=D+2m=L,
    deg((5/3)rf²)=D+2m=L,
    deg(tau*rf)<=D+m<L,
    deg(delta*f)<=m<L,
    deg((2b4/3)f²)<=2m<L,
    deg(alpha*g)<=n<L.

A zero scalar only removes its term; it cannot introduce a higher degree. The mandatory coefficients3 and5/3 are nonzero.

If n<2m-D, the UNIQUE degree-L contribution is -(5/3)H*f_m², nonzero in the polynomial domain. The left side would then have degree L. But a nonzero nonconstant t(r) has degree D*deg t, a multiple of D, and L lies strictly between2D and3D. Constant or zero t also cannot have degree L. Thus this case is impossible.

If n=2m-D, its degree-L coefficient is

    3H²*g_n-(5/3)H*f_m².

It MUST vanish by the same multiple-of-D argument, also when t is zero or constant. Therefore

    g_n=(5/9)*f_m²/H                             (R)

as an identity in K(u,v); the left side is already an actual polynomial. This is not an assumption that an arbitrary rational quotient is polynomial.

Since D>=3 and m>D/2, one has m>=2; since n>=1, m+n-2>=1. The top homogeneous coefficient of the constant bracket[f,g] must therefore vanish:

    [f_m,g_n]=0.

Differentiate(R) in the rational function field, where H is a nonzero unit. The Leibniz rule gives

    [f_m,g_n]=-(5/9)*(f_m²/H²)*[f_m,H].

Its nonzero scalar/rational multiplier and the field property force [H,f_m]=0. The EXPLICIT polynomial centralizer now gives f_m in K[H]. A nonzero homogeneous polynomial of positive degree in K[H] has degree aD for a positive integer a: different powers of H have distinct degrees and cannot cancel. This contradicts 0<m<D. All cases are exhausted.

## 2. Application to the proposed all-D framework

Assume the exact source(S) and canonical construction of the PROVISIONAL general descent report: D>=3, A,B have ordinary degrees3D,5D and topsH³,H⁵, [A,B]=c in K*, and ker[H,-]=K[H]. Its A-only division constructs the finite combined-homogeneous R of degreeD and F of degree3D, with R0=H and nonzero first order1<=j<=3D-1. All five B scalar kernels give finite G of degree5D with ord_s G>=2j. Its exact wedge is

    [A_s,B_s]=[R,T]+[F,G]=c*s^(8D-2),
    T=(3R²+alpha_s)G-(tau_s R+delta_s)F
           -(5R/3+2beta4/3)F²,

where alpha_s=alpha*s^(2D), beta4=b4*s^D, ord tau_s>=3D, ord delta_s>=4D, and T is a POLYNOMIAL of combined homogeneous degree7D.

Suppose 3j>7D. Since8D-2>7D for D>=3, the exact bracket identity and ord[F,G]>=3j give ord[R,T]>7D. The accepted finite lemma, with its stronger finite-subtraction proof, yields

    T=sum_(i=0)^7 t_i*s^((7-i)D)*R^i,
    [R,T]=0,  [F,G]=c*s^(8D-2),

with ALL t_i in K. Polynomiality, combined homogeneity and K[H] are required; mere formal commutation does not assert this scalar polynomial representation.

Specialize s=1. Set r=R(1), f=F(1), g=G(1). These are finite polynomials in the ORIGINAL two coordinates; r has top H and degreeD. The bracket is [f,g]=c. Thus g cannot be zero or constant. Different s-coefficients of F have distinct ordinary degrees, so

    m=deg f=3D-j<2D/3<D,
    1<=n=deg g<=5D-2j=2m-D.

The positive n forces m>D/2. If its displayed upper bound is nonpositive, the nonzero bracket itself already contradicts the hypotheses. Otherwise all hypotheses of the lemma in§1 hold, including its exact(C) with scalar t(Z)=sum t_i Z^i. Contradiction.

Consequently the joint candidate conclusion is:

    Every ACTUAL source with this explicit3:5/closed-H/constant-J
    interface has canonical j<=floor(7D/3).

This removes global minimality from the earlier weaker statement. It does NOT remove the3:5 degree ratio, D>=3, the centralizer hypothesis, the canonical finite reference identities, or constant Jacobian. No coordinate-automorphism criterion or inverse theorem is used in this strengthening.

## 3. Independent boundary/dependency controls, manual only

1. The closed-H hypothesis is substantive. For arbitrary D it is not automatic; a proper power H=h^k,k>1 has [H,h]=0 but generally h is not in K[H]. A contradiction derived from [H,f_m]=0 cannot proceed without the stated centralizer or another exact replacement. This is a control of the proof dependency, not a counterexample source.
2. Constant t is allowed throughout, and t=0 does not evade the highest-degree cancellation. Allowing coefficients of t to depend on u or v destroys the multiple-of-D argument; that is expressly forbidden.
3. A nonconstant target[f,g] is not covered: its leading homogeneous term could cancel [f_m,g_n]. In particular the actual monomial-J triple receiver is NOT an instance of this theorem.
4. n<=0, including G=0 or G polynomial in s alone before specialization, directly contradicts [f,g]=c. Such endpoints are not called smaller Keller pairs.
5. If m+n=2, a leading bracket can be constant rather than zero. The source hypotheses avoid that boundary explicitly: D>=3,m>D/2,n>=1 imply m+n>=3.
6. If m=D, then L=3D is an allowed degree of t(r), and if m=D/2 then n<=0. The open interval is not replaced by an unqualified weak inequality.
7. D=2 has target8D-2=7D, so the strict finite late-T inference is unavailable. This addendum gives no D2 extension. Equality3j=7D is also outside its proof.
8. The scalar constants may be zero. Neither the leading cancellation nor the rational bracket differentiation divides by alpha,tau,delta or b4. Only nonzero H, f_m,3,5 and field operations are used.
9. After extending K, the direct lemma is valid if its centralizer hypothesis holds over the new field. Unlike the coordinate obstruction, this proof does not silently assert that the centralizer hypothesis survives every extension; that is an additional interface check when used.
10. The general descent report's result remains a logically correct weaker conditional consequence if its proof passes review. This strengthening supersedes its minimality requirement for the BOUND, not its frozen custody, original statement or narrower claimed novelty status.

## 4. Theorem-interface pass and review boundary

The accepted finite polynomial late-T lemma and the provisional general canonical framework discharge the exact premises of§2. The specialized wedge has precisely the scalar coefficients required in§1; no rational-to-polynomial coordinate inference is needed. This is a new candidate composition, not yet an accepted theorem.

The obvious source mismatch is the running triple proof's nonconstant Jacobian c*g². Other arbitrary-degree sources need an actual3:5 leading-degree interface and polynomial centralizer, not a numerical degree coincidence. Low-D cases may already be excluded by classical degree-gcd results; this report makes no source novelty or all-degree JC2 coverage claim. A separate source-admissibility screen is underway, and no source family is retired by this unreviewed addendum.

Independent different-model review must check BOTH the new leading-form contradiction and every proposed general-framework premise, including full B kernels, scalar t(R), source degree bounds and constant target. The source-descent gate is in preparation, not already a passing review. No expensive computation, publication or speculative descendant is authorized by this report.

All reasoning is hand polynomial-degree and bracket algebra. This report is the only root mathematical output lease. The report is written by apply_patch, whole-reread, checked for own raised-OPEN collisions, and closed/finalized/verified before terminal invitation. Metadata hashes and actual terminal timestamps are recorded separately; no computational check is claimed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9601`.
- Body SHA-256:
  `146b3af7452d232bae0c79bce1c3b3cbafd9a31c71772a075b3e4510affa70a4`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
