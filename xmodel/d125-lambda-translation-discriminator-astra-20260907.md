# D125 lambda translation: exact action, forbidden leading terms

2026-09-07. **NO-GAIN for the proposed unchanged-u affine translation.** This is a bounded DESK obstruction, not a general classification of permissible source changes. The baseline is unchanged. Terminal contract pins and reading scope are in `box/d125-lambda-translation-discriminator-20260907/inputs.json`; the provisional zero-lambda lemma motivates the question but is not used in the proof. Its live gate was not read.

## Exact rational transition

Use w=p+g, so the source map is u=g^4*w+lambda2*g²+lambda3*g³, v=g^-1. Define the translated source pair by P'(u,v)=P(u,v+b), Q'(u,v)=Q(u,v+b), with u unchanged. Write t=1+b*g and use primed parameters for the new receiver. The old coordinates satisfy

    g0=g/t,
    w0=t^4*w+(lambda2'*t^4−lambda2*t²)/g²
                  +(lambda3'*t^4−lambda3*t)/g.

Requiring this coordinate transition to be regular at g=0 first gives lambda2'=lambda2 from the g^-2 coefficient, then

    lambda3'=lambda3−2b*lambda2.

These equations use no field extension. With that choice, w0=t^4*w+E_b(g), where

    E_b=(3b*lambda3−3b²*lambda2)
        +(6b²*lambda3−8b³*lambda2)g
        +(4b³*lambda3−7b^4*lambda2)g²
        +(b^4*lambda3−2b^5*lambda2)g³.

Thus p0=t^4*p+(terms independent of p), the only remaining coordinate denominator being t. Multiplying the source-u identity by t^4 verifies it literally; translating by −b with the updated parameters is the inverse on the corresponding rational coordinate charts. The coordinate Jacobian is t², since (g0)_g=t^-2 and (p0)_p=t^4. Hence the complete rational bracket c*g² is preserved, with the same c: t²*c*(g/t)²=c*g².

Ordinaryness can remove the t-poles without repairing the degree defect below. Indeed, if the old source P is polynomial, P'(g^4*w+lambda2*g²+lambda3'*g³,g^-1) lies in R[g,g^-1,w]; the displayed transition lies in R[g,t^-1,w]. Their intersection is R[g,w], since g and t are comaximal (t−bg=1), and both are non-zero-divisors even over an arbitrary coefficient ring. Equivalently t is a unit modulo every power of g, which proves the intersection directly. The same holds for Q. This establishes polynomiality under the regular transition, not the original small support bounds.

## First decisive full-chart obstruction

Every charged A has total degree≤15 and coefficient a_(0,15)=1. Consequently its entire coefficient of p^15 is exactly1; no other old monomial can contribute to new p^15. Independently of the choice of new lambdas,

    [p^15] A(g0,p0)=t^60,       [p^25] B(g0,p0)=t^100.

Thus the forbidden slots g*p^15 and g*p^25 have coefficients **60b and100b**. They already exceed the total-degree15/25 envelopes of every case. Over any Q-algebra, preserving those literal support bounds forces b=0. Over a field with b≠0, the further terms b^60*g^60*p^15 and b^100*g^100*p^25 make the failure especially visible. In physical coordinates the same calculation is [u^15]P=v^60 becoming (v+b)^60 after translation.

On lambda2 invertible, choosing b=lambda3/(2lambda2) does set lambda3'=0, but preserves the small chart only if lambda3 was already0. This is not a proof that lambda3 is nonzero anywhere in the unknown complete source quotient, nor that an abstract isomorphism between empty schemes is impossible. It shows that this particular normalization cannot be licensed without already proving lambda3=0 on that open. No nontrivial quotient consequence of that kind is assumed here.

The first upper-support condition therefore fails before one can claim preservation of the entire inner faces, unequal a=1/fixed c, or common mu=1 normalizations. The unchanged scalar and polynomiality do not cure this. Target constant translations or nonzero scalar rescalings cannot remove the offending leading-p coefficients. Additional source-u changes or more general target adjustments have not been classified or ruled out; they would be a separate, presently unlicensed problem.

## Exact old-pass/new-fail control and stop

The tiny source member A=p+g=w with lambda2=1,lambda3=2 has the ordinary lift v^4*u−v²−2v, degree1 receiver, zero receiver origin and monic p. Taking b=1 gives lambda3'=0 and the polynomial receiver

    A'=(1+g)^4*(p+g)+3+4g+g²,

of total degree5, not1. Subtracting its constant3 does not remove g^4*p. This is a toy degree/support control, not a degree15/25 full-face or Keller point. The universal leading-coefficient identity above handles the actual contracts without constructing such a point.

Owned standard-library `check.py` checks the symbolic transition, three exact Fraction inverse fixtures, the leading polynomials for D=1,15,25, and the toy coefficientwise. Normal/-O pass; an actual wrong parameter sign or deleted forbidden term fails in both modes. Six-run batch≤1.38s under30wall/25CPU/512MiB. Only a transition and single leading-coefficient polynomials were expanded, never a full client. No CAS, AWS, solver, additional agent, baseline/shared/protected edit, live peer read, new properness or global JC2 implication. **STOP and idle; no normalization or descendant computation is authorized.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5197`.
- Body SHA-256:
  `9d79071b15aff6efb85813ee6a4ef1a492b578f23e2373207f293c9360edc2ca`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
