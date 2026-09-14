# Real-window paired contact: bounded manual discriminator

Status: NEW exact fixed-rank positivity interface, UNREVIEWED. NO_CLOSING_DISCRIMINATOR: no interval exclusion or interval point is proved. V,W remain arbitrary complex numbers. The task is the stronger real-exponent window 5/3<x<y<2, not a source-point or Keller assertion.

First action 2026-09-10 19:16:12 UTC; fixed publication reserve 19:32:00 UTC and hard stop 19:35:00 UTC, never reset. Owner /root/contact_collision_geometry. Basis 0d39df3c9fd69c939a8420c54d03228b9077777d.

Exactly two accepted 17zi inputs were SHA-pinned before fresh WHOLE reads:

- xmodel/f10-contact-symmetric-remainder-astra-20260910.md: 96deb541bd4d39373bda331885f8b4fbffd224304a2c3533983946ef3b395c13.
- xmodel/f10-contact-symmetric-remainder-gate-fable5-20260910.md: f4f51690d293fff29b63a6a6e965b6168edecae70135dfeac8183bb9720e0093.

No finiteness proof, previous eliminant attempt, coefficient payload or other report is a premise. ROOT supplied contemporaneous symbolic suggestions; all identities used below were independently checked from these two charged reports, not treated as extra accepted inputs.

## Exact scope

Use s=x+y, p=xy, the four accepted quartic remainders F_a1,F_a0,F_b1,F_b0 and the ENTIRE accepted G. The accepted V=1/3 slice has no point in this interval. Further exceptional divisors must be retained. No realness of V,W or cubic roots is assumed.

## 1. Exact outcome and the complete guard

The four contact equations at fixed real s,p reduce EXACTLY to two equations in a monic quartic algebra. A real 4x8 coefficient matrix M defined below has rank four if and only if there is NO complex V,W contact point at these exponents. Consequently a single explicit-but-UNEVALUATED polynomial det(M M^T) gives an exact positivity test on the open real triangle. Neither this determinant nor its positivity is computed. This is a changed fixed-size discriminator, not the older whole-locus finiteness argument or a multivariate eliminant computation.

Put a=2-x, b=2-y, t=a+b, d2=ab. Then 0<b<a<1/3, s=4-t, p=4-2t+ab. All geometric factors of the accepted guard are nonzero: p, p-s+1, 9p-15s+25 and p-2s+4 are respectively xy, (x-1)(y-1), (3x-5)(3y-5), (2-x)(2-y); Delta=(y-x)^2; s-3>0 and 4-s>0. For the remaining factors use alpha=x-5/3, beta=y-5/3, both positive, T=alpha+beta:

    Gamma=1+6T+9T^2+36alpha*beta >0,
    Omega=5/3+10T+12(alpha^2+beta^2)+3(alpha-beta)^2 >0.

Thus only W needs a separate check. No V factor is added to G. The accepted exceptional slice V=1/3 has no window point; the new construction below nevertheless retains it, without division by 3V-1 or any other V-dependent expression.

## 2. W=0 is impossible already at one window exponent

This step works with COMPLEX V. Let c_j=[z^j](1+z+Vz^2+Wz^3)^X, as a formal binomial series. The literal multinomial formulas in the charged gate give

    c6=X(X-1)*a(X)/720,
    c7=X(X-1)(X-2)*b(X)/5040.

For example the W=0 terms of c6 are binom(X,6)+5V binom(X,5)+6V^2 binom(X,4)+V^3 binom(X,3); those of c7 are binom(X,7)+6V binom(X,6)+10V^2 binom(X,5)+4V^3 binom(X,4), reproducing the displayed quartics at W=0.

If W=V=0, c6=binom(X,6) is nonzero for 5/3<X<2. If W=0,V!=0, differentiating the formal identity gives

    (k+1)c_(k+1)=(X-k)c_k+(2X-k+1)V*c_(k-1).

Here 2X is strictly between 10/3 and 4, hence not integral. Starting from c6=c7=0, k=6,5,...,1 successively forces c5,c4,...,c0=0, contradicting c0=1. Every scalar divided in this induction is nonzero in the stated interval. Therefore a(X)=b(X)=0 cannot have W=0 at even one such X. The quartic matrix test need not retain a separate W-inverse variable: its solutions automatically satisfy the entire G in this window.

## 3. A global W-cubic and monic quartic, with no new exceptional divisor

Use F_a1,F_a0,F_b1,F_b0 exactly as in the accepted report. Define

    lambda=s-3, d=210lambda,
    K=p-(s-3)(s-4),
    D0=(-5s^3+62s^2-259s+394+(10s-62)p)/2,
    N(V)=420V^3-210(s-1)V^2+63K*V+D0.

Direct collection of the charged rows gives

    F_b1-(7/2)F_a1=N(V)-d*W.                 (1)

Checks: VW cancels (2520-(7/2)720=0); the W coefficient is 210(s-7)-420(s-5)=-210(s-3); the V^3,V^2,V coefficients are respectively 420, -210(s-1), 63K. The constant term is D0. Since lambda is an EXISTING nonzero geometric guard, (1) gives W=N/d at every point, including V=1/3 and all further coefficient divisors.

Write

    A(V)=120V^3+180(s-5)V^2
         +30(s^2-p-9s+26)V
         +s^3-2sp-14(s^2-p)+71s-154.

Then F_a1=A(V)+120(s-5+6V)W. Therefore

    Phi(V)=[d*A(V)+120(s-5+6V)N(V)]/302400   (2)

is a MONIC quartic in Q[s,p][V]: its V^4 coefficient is 120*6*420=302400, a fixed nonzero rational number before division. No parameter-dependent leading coefficient is inverted. Equations F_a1=F_b1=0 are exactly Phi=0,W=N/d when s!=3. No claim about reality of its roots is made.

For an independent convenient second constant combination, direct collection gives

    I(V,W)=F_b0-7F_a0
      =-840V^3+840(p-3)V^2
       +42[(4s-33)p+60]V
       +630[p-4+4V+4V^2]W+D1,
    D1=-6p^2+(6s^2-80s+378)p-480.             (3)

The W^2 coefficient vanishes; the VW and V^2W coefficients are both 2520. Define the actual polynomial substitutions

    Q0(V)=d^2*F_a0(s,p,V,N(V)/d),
    Q1(V)=d*I(V,N(V)/d).                     (4)

Both belong to Q[s,p][V]; their V-degrees are at most six and five. Clearing d,d^2 loses no point on the window. Thus ALL four original rows are equivalent to Phi=Q0=Q1=0,W=N/d there. Neither constant row is omitted, and no common-root assertion is extrapolated across an additional divisor.

## 4. Exact 4x8 rank and one real polynomial positivity target

Reduce Q0,Q1 modulo the monic Phi, obtaining q0,q1 of V-degree below four. In the FREE rank-four Q[s,p]-algebra E=Q[s,p][V]/(Phi), let M_i be multiplication by q_i in the basis 1,V,V^2,V^3. Precisely its jth column is the coefficient vector of rem(V^j Q_i,Phi), for j=0,1,2,3. Each matrix entry is a rational-coefficient polynomial in s,p; monic division introduces no new parameter denominators. Set

    M=[M_0 M_1],     D(s,p)=det(M M^T).       (5)

These definitions specify exact polynomials/matrices, not emitted or evaluated coefficient artifacts. For fixed real s,p with s!=3, E specializes to a four-dimensional real algebra E_sp, including all repeated roots and nilpotents. The image of M is exactly q0*E_sp+q1*E_sp. Therefore rank_R M=4 iff E_sp/(q0,q1)=0. A nonzero finite-dimensional real algebra has a residue field R or C; equivalently its scalar extension to C is nonzero and has a complex point. Hence this zero quotient condition is equivalent to NO complex common root of Phi,Q0,Q1, and by section 3 to no complex V,W solution of all four contact rows. No real-root or reducedness assumption appears.

For a real matrix, M M^T is positive semidefinite and has positive determinant exactly at full row rank. Equivalently Cauchy--Binet expresses D as the sum of the squares of all 4x4 column minors of M. Combining sections 1--4, the ENTIRE requested real-window contact locus is empty if and only if

    D(4-a-b, 4-2(a+b)+ab)>0
    for every 0<b<a<1/3.                     (6)

This equivalence includes W!=0 by section 2 and every other G factor by section 1. A single zero of D on that triangle would instead imply an actual guarded contact point with real window exponents and complex V,W; it would NOT imply a prescribed rational pair, a source point, or a Keller pair. This makes positivity a genuinely fixed-size exact discriminator without first proving coefficient reality. Neither side of (6) is decided here.

Finite envelope, checked manually: give s,V weight one and p weight two. N has weight at most three, Phi at most four, Q0 at most six, Q1 at most five. For Phi's V^i coefficient the bound is 4-i, so monic reduction preserves the weighted bound. Matrix column weights are 6,7,8,9 and 5,6,7,8, with row weights 0,1,2,3 subtracted. Every 4x4 minor has weight at most 9+8+8+7-(0+1+2+3)=26; hence D has weight at most 52. After the substitution in (6), its ordinary total degree in a,b is at most 52. This is an envelope, not an actual degree, coefficient count, positivity test result or measured runtime.

For the prescribed family only, m=3r+1 gives a=r/m, b=(r-j)/m. Thus a>=2/7, 1-3a<=b<=4a-1 and a<1/3. All prescribed pairs lie in the triangle with vertices (2/7,1/7),(1/3,0),(1/3,1/3), with its limiting a=1/3 edge omitted. Strict positivity on its whole CLOSED triangle is a stronger sufficient certificate for that discrete family, not an equivalence to discrete contacts. A boundary zero could defeat that stronger certificate without implying a permitted contact. No value of D on this smaller domain is computed.

## 5. A separately checked partial reality constraint

For a window solution, V is real if and only if W is real. Forward: the W coefficients of F_a1,F_b1 are 120(s-5+6V) and 210(s-7+12V). With real V all other coefficients are real; both displayed coefficients could vanish only if s=3, excluded. Thus W is real.

Conversely suppose W is real and V=u+iv, v!=0. Take imaginary parts divided by v. From F_a0+2F_a1 one obtains

    30(p-2s+4)(7-s-12u)=0,

so u=(7-s)/12. From F_b1-7F_a1 one then obtains

    W=(-2s^2-11s+31+12p)/180.

From F_b0+3F_b1 one obtains

    20[6W-(p-3s+9)]u+(9-s)(p-3s+9)=0,

so W=(4-s)(p-3s+9)/[15(7-s)]. Equality of these two expressions forces

    E0=36p+2s^3-39s^2+144s-215=0.

But with t=4-s=a+b and d2=ab,

    E0=9-15t^2-2t^3+36d2 >47/27 >0,

using 0<t<2/3 and d2>0. All divisions use nonzero v, p-2s+4=ab, or 7-s>3. This contradiction proves the converse. It does NOT force V,W real: the branch where both are nonreal remains possible. The exact Gram interface, unlike this partial lemma, covers that branch without a descent assertion.

## 6. Controls, GAP, and publication scope

Changed-object controls: testing only one column q_i for nonzero rank cannot replace full row rank; in R[V]/(V^4), multiplication by V is nonzero but the quotient by (V) is R, not zero. Discarding nilpotents is also unsafe: that same algebra has only one reduced point but dimension four. Replacing M M^T by a complex Hermitian positivity claim would change the argument; M is REAL because s,p are real, even when its algebra's points have complex V,W. Without s!=3, (1) does not solve for W, and clearing d could introduce false solutions. All these restrictions are enforced above.

NO_CLOSING_DISCRIMINATOR: no determinant, minor, positivity certificate, interval point, or prescribed rational exclusion is possessed. The exact remaining quantity is strict positivity in (6); the changed small test is available, but no computation is authorized. Whole-locus finiteness and the failed large eliminant attempt were not premises or retried. The prescribed rational subfamily is only a subset of this stronger open real-window test.

Both immutable inputs were fresh WHOLE reads after hashes matched, ending at their Seal/marker; no clipping or prior-turn reuse. No linked input, coefficient payload, network, process, code execution, worker, shared/protected write or follow-on. All new reasoning was manual. Prior involvement: this author wrote the accepted symmetric producer; this new report is not an independent review of it. ROOT owns terminal intake and any FIRST gate or promotion.

## OPEN(S) RAISED

Assigned GAP only: determine (6), or exhibit one exact zero on the triangle. No new canonical identifier and no execution/follow-on authority.

## COLLISIONS

status: EMPTY

Exact owned report/transaction/box targets were absent at first action. Own-only check; no corpus novelty claim. ROOT assigned the quartic/Gram bridge to this report and will not author a duplicate. Own WHOLE report/PINS read, own-only OPEN/collision check and BOTH unchanged input postpins completed at 19:29:27 UTC. Terminal custody records exact final hashes and expected transaction. No scientific execution, positivity claim, source conclusion or follow-on authority.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12035`.
- Body SHA-256:
  `1b923207a38fb85ad4e82b92fd485098786314601d7dd25d7a895df0e6677db2`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
