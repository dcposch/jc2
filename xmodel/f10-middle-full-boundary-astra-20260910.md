# F10 middle full-equation boundary: the denominator is a global unit

Producer Astra /root/nonemptiness_certificate. First action 2026-09-10 06:34:10 UTC; cap 06:49:10, reserve 06:47:10. Exactly the two accepted 17zz reports plus ROOT-CARD are current-pinned inputs. Manual proof only; zero scientific execution. ROOT suggested cancelling W²; every identity and inequality below is independently derived. This is a new producer theorem, not its independent review.

## 1. Statement and exact scope

Fix integers r>=2 and r+2<=h<=2r. Set

    m=3r+1, nu=(5r+2)/m, alpha=(8r+3-h)/m,
    ell=12V+alpha+nu-7.

Let E_nu and Q_nu be the accepted normalized leading polynomials (17zz (5)). Then ell is a unit already in

    A_nu=Q[V,W]/(E_nu,Q_nu).                              (1)

In particular it is a unit in the guarded leading algebra B_nu, every B_nu-algebra and the actual middle resonance quotient B_nu/(Z). Thus the full ell=0 boundary is empty without any assumption that the standalone rational scalar P0 is nonzero. No P0 integer theorem is imported or proved.

Consequently the accepted row Z=P(V)+210ell W permits the exact substitution W=-P(V)/(210ell) throughout its resonance quotient, retaining both leading equations and the W*t5 guard. This does NOT say that this resulting quotient is zero, or that H7_h is a unit. Earlier/forcing/full-source equations and JC2 are outside this theorem.

## 2. Actual parameters and the square cancellation

Put

    d=h-r-1, tau=r/m=2-nu, delta=d/m.

Then

    2/7<=tau<1/3,
    1-3tau<=delta<=4tau-1<1/3,
    alpha+nu=4-delta,
    ell=12(V-v0),  v0=(3+delta)/12.                       (2)

These follow directly from 1<=d<=r-1 and m=3r+1; in particular delta>0. Only these inequalities will be used. They concern rational parameters, not an assumed ordering on unknown coefficients.

For a temporary exponent u, direct subtraction of the accepted E_u,Q_u yields

    Q_u-7E_u=K_u(V)+210D_u(V)W,

    D_u(V)=(u-3)(4-3u)+12(1-u)V+12V²,

    K_u(V)=-2(3u-4)(u-3)(u-4)(u-5)
            +42(u-3)(u-4)(5-4u)V
            +840(u-3)(1-u)V²-840V³.                     (3)

Indeed W² has coefficient 2520-7*360=0; the coefficients of W, VW and V²W in the difference are respectively 210(u-3)(4-3u), 2520(1-u), 2520. The constant, V, V² and V³ differences give the four displayed terms of K. No source equation has been dropped.

Write D=D_nu(v0), K=K_nu(v0). On ell=0, (3) is the scalar-coefficient linear equation

    K+210D W=0.                                         (4)

The following two steps show D>0 and that E_nu(v0,W) has negative discriminant. Thus (4) cannot coexist with E=0, even for complex W.

## 3. The linear coefficient never vanishes

Substitute u=2-tau and V=v0 in (3):

    12D=delta²+(12tau-6)delta-3+24tau-36tau².              (5)

Its derivative with respect to delta is 2delta+12tau-6. On (2) this is at most 20tau-8<-4/3, so the right side decreases with delta. Evaluation at the allowed upper bound gives

    12D >= 4(7tau²-5tau+1)
          =28(tau-5/14)²+3/7 >0.                        (6)

Therefore D is a strictly positive nonzero rational for every actual pair. In ANY Q-algebra quotient with ell=0 and E=Q=0, equation (4) fixes

    W=w0=-K/(210D) in Q.                                (7)

No nonunit or generic coefficient is inverted; 210D is an explicitly proved nonzero rational. In particular this rules out evading the next argument by choosing complex or nilpotent W.

## 4. The remaining quadratic has negative discriminant

At u=2-tau, the accepted E polynomial is

    E_nu(V,W)=360W²+beta W+gamma,
    beta=120tau(1+tau-6V),
    gamma=tau[(1+tau)(2+tau)(3+tau)
              -30(1+tau)(2+tau)V
              +180(1+tau)V²-120V³].                    (8)

Its discriminant is Delta=beta²-1440gamma=1440tau J(tau,V), where

    J=120V³-180(1-tau)V²
       +30(1+tau)(2-3tau)V+(1+tau)(9tau²+5tau-6).

After V=(3+delta)/12 let Phi(tau,delta)=72J. Expanding only this scalar polynomial manually gives

    Phi=5delta³+(90tau-45)delta²
         +(-45+360tau-540tau²)delta
         -27+198tau-612tau²+648tau³.                    (9)

Its tau derivative has the exact completed-square form

    Phi_tau=90delta²+(360-1080tau)delta
              +1944(tau-17/54)²+16/3 >0                (10)

for delta>=0, tau<=1/3. Holding delta fixed and increasing tau to 1/3 therefore yields

    Phi(tau,delta)<Phi(1/3,delta)=5(delta-1)³<0.          (11)

The last inequality uses delta<1/3<1. Since tau>0, equations (9)-(11) prove Delta<0. All coefficients here are rational for an actual (r,h).

By (7), the only candidate W=w0 is rational. Completing the square shows explicitly

    e:=E_nu(v0,w0)
      =360(w0+beta/720)²-Delta/1440 >0,                 (12)

where beta,Delta are evaluated at v0. Thus e is a nonzero rational, a unit in every Q-algebra. Equations E=Q=ell=0 force e=0, a contradiction. This proof uses positivity solely to prove a rational scalar nonzero; it never requires unknown leading coefficients or their field to be real.

## 5. Explicit whole-ring unit construction

Here is a finite algebraic witness recipe, not just a field-point argument. Define the polynomial in W

    A(W)=[360(W+w0)+beta]/(210D),

using only the nonzero rational D. At V=v0,

    E_nu(v0,W)-A(W)[Q_nu(v0,W)-7E_nu(v0,W)]=e.          (13)

This is ordinary division of a quadratic by W-w0, since the bracketed term is 210D(W-w0). Consequently

    J0(V,W)={E_nu(V,W)-A(W)[Q_nu(V,W)-7E_nu(V,W)]-e}
                /(V-v0)                               (14)

is a polynomial over Q: its numerator vanishes identically at V=v0. Division is by a monic linear polynomial, not by an element of the coefficient algebra. Using ell=12(V-v0), the polynomial identity is

    1 = E_nu/e - (A/e)(Q_nu-7E_nu) - ell*J0/(12e).       (15)

Therefore -J0/(12e) is an explicit inverse recipe for ell in (1). It involves only rational divisions by 210D and e, both proved nonzero. It is valid with nilpotents and on the zero ring and survives localization by W*t5 and every subsequent base change. No root decomposition, field selection, computed resultant or coefficient artifact is used.

This proves more than emptiness of the ell=0 part of B_nu/(Z): the denominator is already a global unit before imposing Z. The independent middle-resonance equation itself is still present, now with a licensed denominator. Nothing asserts that its remaining one-variable equations are incompatible.

## 6. Meaningful changed-equation control

Dropping Q is a genuine failure of this mechanism even while keeping the normalization guard. For any actual pair, the quadratic E_nu(v0,W)=0 has the two nonreal roots

    W_±=(-beta ± i*sqrt(-Delta))/720.

They are nonzero because Delta<0 implies gamma>0. The coefficient of W in t5(nu) is

    (nu)_3/2+(nu)_2*v0=(nu)_2*(v0-tau/2),

obtained from the z^5 partitions containing one W. It is a nonzero rational: v0>1/4 and tau/2<1/6. Thus t5 is a real affine polynomial with nonzero slope, whose only possible zero is real; it does not vanish at W_±. Both changed objects satisfy ell=E=0 and W*t5!=0, but fail Q=0 because (4) would require W rational. They are expressly NOT allowed leading points. This control shows why negative discriminant alone, without the second equation forcing rational W, would not exclude complex solutions.

Dropping ell instead also removes the specialization V=v0, so this report supplies no positivity or reality statement for arbitrary complex leading V,W. Likewise (15) does not make Z a unit. The two distinctions prevent upgrading this denominator theorem to global H7-unitness or source closure.

## Scope, OPEN quantity and own review

Producer verdict: PROVED denominator-column unitness for every actual r,h at the accepted 17zz interface, with explicit whole-ring witness recipe (15). No actual P0 integer result, no leading/source point, no full forcing elimination, no finite r bound or JC2 consequence. No code, data artifact, scientific subprocess or execution permission.

No new canonical OPEN ID. The existing remaining quantity is global H7_h-unitness, equivalently the guarded resonance quotient after the now-licensed W substitution. Its cheapest genuinely new mathematical test is compatibility of those retained one-variable leading equations with their guard; no such test is performed or authorized here.

Own-only box/report absence was checked before writing; all inputs remain immutable. Only the charged two accepted reports and card were used, with explicit current-pin/WHOLE reuse. No previous unreviewed boundary result or other-lane body was consumed. Own WHOLE, exact-sign/rational-division review, raised-OPEN quantity/cheapest-test and collision check precede the completion marker. Independent review remains ROOT's responsibility; no follow-on authority.

Own WHOLE read completed 06:39:55 UTC. Manual rechecks covered all coefficients in (3), the discriminant factor and completed square (8)-(11), the sign of the inverse in (15), and the guarded changed-equation control. No remaining mathematical action is pending within this task.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9143`.
- Body SHA-256:
  `18bc8c94f1d8b2183fa17bac18a3f12800852a7793b68bc0783a928e75b2edff`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
