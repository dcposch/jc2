# Uniform mixed-kernel scalar: bounded manual evaluation

Owner /root/contact_collision_geometry. Actual first action 2026-09-11 13:45:05 UTC. Original publication reserve 14:05 UTC / HARD 14:08 UTC, unchanged. MANUAL CO-RESEARCH / UNREVIEWED.

Sole scientific input: box/f10-mixed-kernel-scalar-astra-20260911/TASK.md, SHA256 dc9e3a27ed8e3052e89e598eb00cae060c9eaf3a5216c6a61b75bc0b0a3835f3, freshly read WHOLE after matching its pin. Own report/manifest/PINS/custody were absent; ROOT's TASK is preserved.

## Exact scope

Work over the entire commutative Q-algebra specified in TASK, including nilpotents and all components. Its units a,b,H, identity mCD'-nC'D=-theta^7, and both uniquely normalized finite inverse pairs are stipulated inputs. No field factor, source coefficient array, or previous potential claim is assumed. The target is Gamma(W) for the entire mixed forcing, not its top coefficient or a source-zero conclusion.

## 1. Result: an exact remaining cubic factor, not a unit verdict

Put nu=n/m, alpha=(7r+3)/m=2nu-1 and beta=(7r+2)/m=4-nu. Define units and normalized parameters

    lambda=H/a,  X=aF/H^2,  Y=a^2/H^3,
    u=lambda*theta,  phi(u)=1+u+X*u^2+Y*u^3.

For s in Q let T_s(u) be the truncation through degree 7 of phi(u)^s. Then the ENTIRE mixed scalar is exactly

    Gamma(W) = 21*lambda^14 * B_r(X,Y),
    B_r(X,Y) = [u^14] (phi'(u)/phi(u))*T_alpha(u)*T_beta(u).       (1)

This B_r is an explicitly specified rational polynomial of ordinary degree at most 7, independent of D and of the modified-inverse correction. Section 4 gives a finite binomial-sum formula, with no inverse pairs or antiderivative remaining. The relevant universal coefficient algebra is

    S_r = Q[X,Y,(Y*d_5)^-1]/(d_6,d_7),
    d_k = [u^k] phi(u)^nu.                                      (2)

The original universal leading algebra is S_r[lambda,lambda^-1], with the reconstruction below. Consequently the only unevaluated factor in Gamma is B_r in this exact localized algebra. I have NOT proved B_r to be a unit or zero there for every actual r>=2. This is an exact reduced-factor result, but NO NEW CLOSING DISCRIMINATOR for the proposed model comparison. It is not merely the original finite-inverse definition: the modified pair, D, the integral and six forcing coefficients have all been eliminated by identities.

## 2. Entire-forcing antiderivative and cancellation of the modification

Write P=P_-, Q=Q_-, R=P_+, S=Q_+, a_1=m-r, a_2=m-r-1, b_1=n-r, b_2=n-r-1. We have a_1+b_2=a_2+b_1=2m. Direct differentiation, using the whole leading identity, gives the following rational-function identity, valid formally at theta=0 since C(0)=a is a unit:

    E = -b_2*P*S/C^2 - b_1*R*Q/C^2 + 2n*D*P*R/C^3,
    E' = W/C^2
         -2*(R*L_r(P,Q)+P*L_(r+1)(R,S))/C^3
         -6*theta^7*P*R/C^4.                                  (3)

One can verify (3) by collecting the P' S, R' Q, P S', R Q' terms first; the remaining D' and C'D terms combine by mCD'-nC'D=-theta^7. Inserting the stipulated L-values gives

    W/C^2 = E' -4e*theta^6*P/C^3 +6*theta^7*P*R/C^4.

After integration from 0 and multiplication by C^2, the E(0) term has degree at most 6; so do P*S and R*Q. The last displayed integral starts in degree 8. The other integral contributes -4e*P(0)/(7a) to coefficient 7. Therefore

    Gamma(W) = (21an/H)*[theta^7](D*P*R/C) -6e*P(0)/H.          (4)

This calculation uses the COMPLETE W, not just its leading term.

Now let T_beta be the UNMODIFIED theta-truncation of (C/a)^beta, and set

    R_0=(C*T_beta'/beta-C'*T_beta)/theta^7,
    S_0=(n*D*T_beta'/(m*beta)-D'*T_beta)/theta^7.

The given modified formulas imply exactly

    R=R_0+(2e/7)C',   S=S_0+(2e/7)D'.

Indeed the derivative of the subtracted (2e/7)theta^7 cancels the added 2e theta^6 in the given numerator. Thus R_0,S_0 are polynomials with degrees at most 2,4; no new divisibility assumption is needed. Also L_h(C',D')=-7theta^6, obtained by differentiating the leading identity, so this correction accounts for the FULL modified row.

The leading identity additionally yields

    [theta^7](D*P*C'/C)=P(0)/(na),

because nDC'/C=mD'+theta^7/C and deg(PD')<=6. Substituting R=R_0+(2e/7)C' in (4) cancels the explicit -6eP(0)/H term EXACTLY. No division by e, P(0) or another unproved unit occurs.

Finally the minus inverse gives mCQ-nDP=T_alpha. Hence, using deg(QR_0)<=6,

    n*[theta^7](D*P*R_0/C)
      =-[theta^7](T_alpha*R_0/C)
      =[theta^14](C'/C)*T_alpha*T_beta.

For the last equality, substitute R_0; the discarded product T_alpha*T_beta' has degree at most 13. This proves (1) after u=lambda theta. It is a coefficient identity, not a residue-at-infinity argument. Every inverse used so far is a rational scalar, a power of the stipulated unit a, or a formal power series with unit constant term. All calculations therefore survive arbitrary base change and nilpotents.

## 3. Exact whole-leading presentation and its guards

Write D(theta)=b*d(lambda theta), with d(0)=1. Monicity gives b*lambda^5*d_5=1, and monicity of C gives a*Y*lambda^3=1. Thus lambda,Y,d_5 are units. The leading identity becomes

    m*phi*d' - n*phi'*d = -Y*d_5*u^7.                         (5)

Its coefficients below degree 7 show d=phi^nu modulo u^8: divide by the unit series phi^(nu+1), integrate in Q[[u]], and use d(0)=1. Since d has degree 5, d_6=d_7=0. Conversely, suppose (2), and put d=sum_(k=0)^5 d_k*u^k. The equations d_6=d_7=0 force the coefficients below degree 7 of the left side of (5) to vanish. Its degree-7 coefficient is

    (5m-3n)*Y*d_5 = -Y*d_5,

because 5m-3n=-1 for EVERY actual r. Thus (5) holds identically. Given a unit lambda, reconstruction is

    a=1/(Y*lambda^3),  H=1/(Y*lambda^2),  F=X/(Y*lambda),
    b=1/(lambda^5*d_5), C=a*phi(lambda theta), D=b*d(lambda theta).

These maps are mutually inverse on the universal algebras, without taking radicals, choosing factors, or assuming reducedness. Any particular stipulated leading algebra receives this presentation by base change. The displayed inversions are exactly proved units; no discriminant or extra divisor was inverted.

For a compact literal description, with binomial(nu,j) denoted c_j,

    d_5 = c_5+4c_4 X+3c_3(X^2+Y)+2c_2 XY,
    d_6 = c_6+5c_5 X+c_4(6X^2+4Y)
                +c_3(X^3+6XY)+c_2 Y^2,
    d_7 = c_7+6c_6 X+c_5(10X^2+5Y)
                +c_4(4X^3+12XY)+3c_3(X^2Y+Y^2).

Thus the remaining factor is tested on two explicit cubics, with precisely Y*d_5 inverted. Merely being nonzero as a polynomial would not make B_r a unit in this algebra.

## 4. Explicit finite formula and degree envelope

For k>=0 define the rational polynomial

    b_k(s)=sum_(i,j>=0; 2i+3j<=k)
      (s)_(falling k-i-2j) * X^i Y^j
        / ((k-2i-3j)! i! j!).

It is exactly [u^k]phi^s; falling order zero means 1. For k>=1 put

    ell_k=k*sum_(i,j>=0; 2i+3j<=k)
      (-1)^(k-i-2j-1) * (k-i-2j-1)! * X^i Y^j
        / ((k-2i-3j)! i! j!).

Here k-i-2j>=1 automatically, and ell_k=[u^(k-1)]phi'/phi. The exact remaining factor in (1) is the following FIXED finite expression, valid uniformly in the actual rational parameters alpha,beta:

    B_r(X,Y)=sum_(i=0)^7 sum_(j=0)^7
                   b_i(alpha)*b_j(beta)*ell_(15-i-j).           (6)

All indices of ell are between 1 and 15. Formula (6), together with the two literal cubics above, is an explicit finite-sum specification of the reduced scalar polynomial; no finite inverse, forcing row or antiderivative is left to interpret. It is not an emitted computational coefficient artifact.

Restoring a variable L in phi=1+L*u+X*u^2+Y*u^3 shows each term before L=1 has weight 15 for weights (1,2,3). Hence every monomial X^iY^j in B_r has 2i+3j<=15, so ordinary degree is at most 7. This is a proved envelope, not a measured degree or runtime forecast. The prefactor 21*lambda^14 is a unit, so unitness of Gamma is exactly unitness of this B_r in the appropriate whole leading algebra.

There are also FOUR removable parameter factors, before imposing d_6=d_7=0. Regard the right side of (6) as B(nu,X,Y), a polynomial in nu as well. At nu=1 or 3/2 we have alpha=1 or 2: the integrand in (1) becomes respectively phi'*T_beta or phi'*phi*T_beta, of degrees at most 9 or 12. At nu=3 or 2, the same argument applies with beta=1 or 2. In each case coefficient 14 is identically zero for every phi. Polynomial divisibility over Q therefore gives

    B(nu,X,Y)=(nu-1)*(2nu-3)*(nu-2)*(nu-3)*K(nu,X,Y),           (7)

where K is a rational polynomial, still of degree at most 7 in X,Y. Formula (6) followed by exact division by the displayed four linear factors specifies K without any source specialization. For every actual r>=2,

    5/3 < nu <= 12/7 < 2,

so all four factors are nonzero rational units. Thus the smallest factor isolated here is K evaluated at the actual nu, on precisely the algebra (2). Its unitness remains unresolved; (7) does not assert it.

## 5. Changed-parameter control and precise stopping point

The following control is OUTSIDE every finite actual r. Change nu to 5/3 and set phi=(1+u/3)^3, so X=1/3, Y=1/27. Then phi^nu=(1+u/3)^5, d_6=d_7=0 and d_5=1/3^5 is a unit. Moreover alpha=beta=7/3 and T_alpha=T_beta=(1+u/3)^7. Therefore

    (phi'/phi)*T_alpha*T_beta=(1+u/3)^13,

whose coefficient of u^14 is zero. Thus the reduced polynomial family has a genuine zero with Y*d_5 nonzero at the limiting parameter. This does NOT give a zero for any actual r, nor does it satisfy the original leading equation for a finite m. It demonstrates why a unit proof using only the two cubics and their guards, while forgetting the actual restriction 3nu-5=1/m nonzero, would be invalid.

OPEN QUANTITY: whether B_r is a unit in (2) for every integer r>=2, or whether an exact actual-r component has B_r zero. Neither is proved here. The concrete remaining object is (6) on the two stated cubics, not the unevaluated mixed inverse. No generic nonvanishing, sampled parameter or one-factor conclusion is substituted for the requested whole-algebra verdict.

CHEAPEST TEST used: manual differentiation, finite coefficient identities and the explicit changed-parameter control. Planning wall: 15 minutes, UNMEASURED predictive cost. No scientific subprocess, coefficient payload or additional source was used. There is no new canonical OPEN ID, implementation queue, computation authorization or descendant. This necessary scalar test alone would not establish a potential, actual highest regularity, source emptiness, an all-F10 result or JC2 even if a future unit proof succeeds.

## Read scope and collisions

The sole TASK was pinned before FRESH_WHOLE reading; no other scientific file was read. ROOT's optional algebra messages were independently checked within this same stipulated algebra, not used as extra file premises. Prior task reports remain untouched. Publication uses only own documentary writes, input postpin and own WHOLE/collision checks. COLLISIONS: EMPTY at first action; ROOT's pre-existing TASK is excluded from ownership. Final result: EXACT REDUCED FACTOR, UNIT STATUS OPEN / NO NEW CLOSING DISCRIMINATOR. All scientific exploration stops here.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11124`.
- Body SHA-256:
  `e9e3e61ba2df279a49ba1a7de283429828ad1250ef01bc6bc2b83fdb8fb686b0`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
