# Middle coefficient unitness for every 7-divisible r

First 2026-09-10 07:42:58 UTC; stop 08:00:58, reserve 07:58:58. Seven exact current-pinned inputs; manual proof, zero scientific execution. The prior three-family report is not an input or premise.

## Theorem and retained interface

For every integer r>=7 divisible by 7 and EVERY h in {r+2,...,2r}, the accepted middle Z is a unit of the entire B_nu, hence H7_h is a unit of B_nu[s,s^-1] and every further base change. Equivalently gcd(S,T)=1 over Q. All seven leading points and all guards remain; no full-source/forcing exclusion follows.

Set m=3r+1, tau=r/m, nu=2-tau, alpha=(8r+3-h)/m. Work in an algebraic closure of Q_7 with valuation v(7)=1. Write k=v(tau)=v(r)>=1. The parameters tau,nu,alpha and coefficients of (1)-(2) are 7-integral since m is a unit. The accepted formulas are

    D=12V²-12(1-tau)V+(1+tau)(2-3tau),
    K=-840V³+840(1-tau²)V²
       +42(1+tau)(2+tau)(4tau-3)V+k0,
    k0=2(2-3tau)(1+tau)(2+tau)(3+tau),
    beta=120tau(1+tau-6V),
    gamma=tau[(1+tau)(2+tau)(3+tau)
              -30(1+tau)(2+tau)V+180(1+tau)V²-120V³],
    E_nu=360W²+beta W+gamma,
    K+210DW=Q_nu-7E_nu,
    S=2K²-140tau(1+tau-6V)KD+245gamma D²,
    T=DP-ell K=DZ,  deg(T)=5, lc(T)=10080.              (1)

Here ell=12V+A, A=alpha+nu-7 and

    P=840V³+420A V²+42B2 V+B3,
    B2=alpha²+alpha*nu+nu²-12(alpha+nu)+47,
    B3=[f(alpha)-f(nu)]/(alpha-nu),
    f(X)=(X-3)(X-4)(X-5)(X-6).                         (2)

The divided difference in (2) is a polynomial, so causes no 7-adic division even if alpha-nu is divisible by 7. Accepted17zzd identifies B_nu=Q[V]/S, with D and W*t5 units and W=-K/(210D).

## 1. All possible V-valuations

Write S=sum a_i V^i. Since k0 is 24 modulo 7 and K's nonconstant coefficients are divisible by 7, (1) gives

    v(a0)=0; v(a_i)>=1 for 1<=i<=3;
    v(a_i)>=2 for 4<=i<=6; v(a6)=2; v(a7)=k+2.        (3)

Indeed the degree-six term of 2K² is 2*840², with valuation two; all other degree-six contributions have valuation at least k+2>=3. The degree-seven coefficient is -245*120*144*tau. Lower-degree bounds follow by writing K=k0+7L: terms not divisible by 49 in 2K² have degree at most three; the other summands have the displayed additional factors.

For any root V of S, put t=v(V). If t>-1/3 the constant term is uniquely least-valued. If -k<t<-1/3, degree six is uniquely least: degrees 1..3 differ by at least -1+(i-6)t>0, degrees 4,5 by (i-6)t>0, degree seven by k+t>0, and the constant is higher. If t<-k, degree seven is uniquely least: degree six differs by -k-t>0, and every lower degree is still higher using k>=1 and (3). A uniquely least term cannot sum to zero. Hence

    t=-k or t=-1/3.                                    (4)

No count of roots in either class, factorization, or irreducibility assertion is needed.

## 2. The t=-k roots never resonate

Writing T=sum c_i V^i, (1)-(2) give v(c5)=1, v(c4),v(c3)>=1 and v(c2),v(c1),v(c0)>=0. At t=-k, its leading term has valuation 1-5k, strictly below every other term: the nearest low-degree bound differs by 3k-1>0. Thus T(V)!=0 for every h.

## 3. The t=-1/3 roots and h not divisible by 7

At these roots, v(D)=-2/3, v(beta)=k-1/3, v(gamma)=k-1. The quadratic E_nu=0 forces

    w:=v(W)=(k-1)/2.                                  (5)

For w below this value, 360W² is uniquely least; above it gamma is uniquely least, since the beta W term is strictly higher at the proposed balance. Consequently v(K)=v(210DW)=w+1/3>0. Put u=7V³, a valuation-zero element. The only valuation-zero terms in K are k0-120u, hence in the residue field

    u=3.                                               (6)

The coefficient c2 is 12B3 modulo 7, while c3,c4 are divisible by 7. Divide T(V) by V². Every term except c2+10080V³ has positive valuation. Its residue is

    12B3+1440u=5B3+1
      =5(alpha-3)(alpha²+alpha+6).                     (7)

For the last equality reduce nu to 2 in the polynomial divided difference: B3 specializes to alpha³-16alpha²+87alpha-168. The quadratic in (7) has discriminant 5 modulo 7, a nonsquare. Here alpha is a rational residue in F_7, even though V,W may have larger residue fields. Since alpha=3-h modulo 7, (7) is nonzero whenever 7 does not divide h. Thus T(V)!=0 in that entire case.

## 4. The linked 7-divisible h case

Now let 7 divide h and put e=(r+h)/m, so alpha=3-e and l:=v(e) is a positive INTEGER. Positivity r+h>0 makes e nonzero. Formula (5) remains valid, and u still has residue 3. Use the accepted full Q_alpha rather than divide another coefficient. Its constant and cubic-V terms combine exactly as

    e[(1+e)(2+e)(3+e)-120u],                           (8)

with valuation l, since the bracket has residue 6-3=3. The term 2520V²W has valuation

    a=1/3+w=(3k-1)/6,                                 (9)

which is NOT an integer for any integer k. The other terms of Q_alpha have the following valuations or lower bounds:

    42(alpha-3)(alpha-4)(alpha-5)V:       l+2/3,
    420(alpha-3)(alpha-4)V²:             l+1/3,
    210(alpha-3)(alpha-4)W:              l+1+w,
    2520(alpha-3)VW:                    l+2/3+w,
    2520W²:                             1+2w=k>a.

Every term in this list exceeds min(l,a). Because l!=a, exactly one of the combined term (8) and the term (9) is least-valued. Therefore Q_alpha(V,W)!=0. But E_nu=Q_nu=0 and the accepted identity Q_alpha-Q_nu=(alpha-nu)Z would force Q_alpha=0 at a resonance. This excludes every remaining root, for all valuations of r+h, without an extra congruence assumption.

## 5. Whole-ring conclusion, controls and limits

Every root of S in Q_7's algebraic closure is covered by (4) and one of sections 2-4. None is a root of T. Thus gcd(S,T)=1 over Q: a common rational polynomial factor would retain a root after scalar extension. A rational Bezout identity aS+bT=1 exists, giving the inverse bD of Z in Q[V]/S. This is an existence proof of the exact inverse, not a computed gcd or coefficient certificate. Unitness survives every base change, including nonreduced ones; the accepted rational-unit prefactor then gives H7_h-unitness without specializing the free Laurent scale.

Controls: stopping at (7) would lose all actual h divisible by 7; section 4 retains and settles that boundary. Arbitrary W is not licensed: without E_nu, (5) fails and the decisive nonintegral valuation (9) need not hold. Likewise tau=0 is not an actual parameter: S loses degree and the original guard argument cannot be replaced by that specialization. Valuation (4) alone never proves coprimality; the full T and Q_alpha identities are essential. No reality of V,W or rationality of their points was assumed.

No new OPEN ID. The requested r-divisible-by-7 coefficient-unit family is proved; no omitted actual (r,h) remains within that family. Other r, full forcing/source equations, source existence or exclusion, finite-r bounds and JC2 are outside this task. No scientific execution, source-code or fixture artifact, scripted coefficient computation, worker action, or follow-on authority. Own WHOLE read and final valuation/sign/OPEN/collision review completed 07:49 UTC before this marker. No unfinished writer, placeholder or raised unquantified OPEN remains.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7259`.
- Body SHA-256:
  `c214de8112e52b3f8b8b586340dbff09a4102d09107cd0c2a57ce699afd414ee`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
