# Two distinct cubic contact exponents: a faithful cubic exceptional algebra

2026-09-09. Independent MANUAL discriminator; UNREVIEWED. First action20:44:51.005130624UTC; controlling stop20:59:51.005130624UTC. Sole accepted science input:16l, exact pin in the owned PINS. No other report or theorem is a premise. ZERO mathematical subprocesses, sampling, coefficient-code execution or source computation.

## 1. Exact outcome and remaining question

Let K be algebraically closed of characteristic zero. Put

    r>=2, m=3r+1, n=5r+2,
    x=nu=n/m, y=alpha=(n+j)/m, 1<=j<=r-1.

The question is whether a cubic c(t)=1+u t+v t^2+w t^3, w!=0, can satisfy H6(x)=H7(x)=H6(y)=H7(y)=0, where H_i(X)=[t^i]c(t)^X.

This report does NOT prove uniform nonexistence or produce a solution. It proves an exact exceptional-algebra criterion with no coefficient-zero branch discarded. After the licensed normalization u=1, the entire four-row system is isomorphic to

    Q[V,W(V)^-1]/(J3(V), Z0(V), Z1(V)),            (1)

where J3 is uniformly MONIC of degree3, Z0,Z1 have degree at most2, and W has degree exactly3. A monic quartic intermediate is derived first; section6A then proves a second rational-unit pivot and the sharper cubic form. All coefficients are explicitly specified rational functions of the prescribed rational exponents x,y, with denominators proved nonzero. The formulas below require no root selection, field factor, generic coefficient inversion or actual polynomial expansion by software.

Thus the simultaneous-contact question is reduced to whether this particular guarded finite algebra is zero. This is NOT a uniform emptiness proof. Any normalized solution, if one exists, has v algebraic of degree at most3 over Q and w in Q(v). No source/Keller/JC2 implication is asserted.

The key uniform identity is that the two potentially troublesome w-coefficients generate the unit ideal in Q[V]. Their Bezout constant is -Gamma/12, where

    Gamma=36xy+9(x+y)^2-114(x+y)+181>0.             (2)

This inequality concerns the two rational exponents only. No reality or positivity assumption on the unknown coefficients v,w is used.

## 2. Normalization and exact parameter range

The accepted16l reciprocal contact theorem applies to x=n/m because 3n-5m=1 and m=3(r-1)+4. A nonzero contact point for this exponent has u!=0. For clarity its elementary argument is also visible directly: at u=0,

    H6(x)=(x)_2 w^2/2+(x)_3 v^3/6,
    H7(x)=(x)_3 v^2 w/2.

Here x is none of0,1,2 and w!=0. The second equation forces v=0 and the first then contradicts w!=0. Therefore the replacement t->t/u gives

    c(t/u)=1+t+(v/u^2)t^2+(w/u^3)t^3.

Every H_i at EITHER exponent is multiplied by u^-i, so both pairs of zero equations are preserved simultaneously. We henceforth write V,W for the normalized quadratic and cubic coefficients. The omitted original u is an arbitrary nonzero scale, not a value inferred to equal1 in the original coordinates.

The rational ranges needed throughout are

    5/3 < x < y < 2,
    d=y-x=j/m>0,
    s=x+y>10/3, p=xy.                              (3)

Indeed x=5/3+1/(3m), and the largest numerator n+j is6r+1<2m. These statements prove every division by x(x-1), y(y-1), x-2, y-2, d and s-3 below is by a nonzero rational. No assertion about arbitrary rational exponents or j=0 is smuggled into this range.

## 3. Literal finite coefficient formulas and their linear difference

Write (X)_k=X(X-1)...(X-k+1). The sole accepted input gives the literal normalized formulas

    H6(X)=(X)_6/720+(X)_5 V/24+(X)_4 V^2/4
            +(X)_3 V^3/6+(X)_4 W/6+(X)_3 VW
            +(X)_2 W^2/2,

    H7(X)=(X)_7/5040+(X)_6 V/120+(X)_5 V^2/12
            +(X)_4 V^3/6+(X)_5 W/24+(X)_4 VW/2
            +(X)_3 V^2W/2+(X)_3 W^2/2.            (4)

These finite partitions were read, not executed. Define

    A_X=H6(X)/(X(X-1)),
    B_X=H7(X)/(X(X-1)(X-2)).                       (5)

Both are polynomials in X,V,W, with rational coefficients. More explicitly,

    A_X=W^2/2+(X-2)(V+(X-3)/6)W
       +(X-2)V^3/6+(X-2)(X-3)V^2/4
       +(X-2)(X-3)(X-4)V/24
       +(X-2)(X-3)(X-4)(X-5)/720.                 (6)

For B_X the terms are

    W^2/2+V^2W/2+(X-3)VW/2+(X-3)(X-4)W/24
       +(X-3)V^3/6+(X-3)(X-4)V^2/12
       +(X-3)(X-4)(X-5)V/120
       +(X-3)(X-4)(X-5)(X-6)/5040.                (7)

The identical W^2/2 terms cancel. Subtracting term by term gives

    24(A_X-B_X)=P_X(V)+Q_X(V)W,                    (8)

where

    Q_X=(X-3)(3X-4)+12(X-1)V-12V^2,

    P_X=4V^3+4(X-3)(X-1)V^2
       +(X-3)(X-4)(4X-5)V/5
       +(3X-4)(X-3)(X-4)(X-5)/105.                (9)

For example the unscaled constant of A_X-B_X is (3X-4)(X-3)(X-4)(X-5)/2520, the unscaled V^3 term is V^3/6, and the unscaled V^2W term is -V^2W/2. These fix the subtraction sign and the potentially important negative coefficient. The desired four equations are EXACTLY equivalent to

    A_x=0, A_y=0,
    P_x+Q_xW=0, P_y+Q_yW=0.                       (10)

Neither individual Q is assumed nonzero or a unit.

## 4. Both zero coefficients are impossible, with a global Bezout identity

Let

    Vstar=(13-3s)/12,
    L(V)=(x-1-V-Vstar)/d.

Directly from(9),

    Q_y-Q_x=12d(V-Vstar),
    Q_x(Vstar)=-3p+12-12Vstar-12Vstar^2
               =-Gamma/12=:qstar,                (11)
    Q_x(V)-qstar=12(V-Vstar)(x-1-V-Vstar).

Consequently the following identity holds in Q[V]:

    (1+L)Q_x-LQ_y=qstar.                          (12)

It remains to prove qstar is a unit, rather than merely name it. Put xi=x-5/3>0 and eta=y-5/3>0. Expanding ONLY the scalar expression(2) gives

    Gamma=1+6(xi+eta)+9xi^2+54xi*eta+9eta^2>0.     (13)

Thus qstar is a nonzero rational for EVERY prescribed(r,j). This proves Q_x,Q_y have no simultaneous zero, even over an arbitrary extension field, and more strongly that they generate the unit ideal over any Q-algebra. An individual Q may still vanish. Formula(12) handles those cases without choosing a chart or dividing by that individual coefficient.

In particular the apparently dangerous locus Q_x=Q_y=0 cannot occur for the prescribed exponents: subtracting them would force V=Vstar, and then Q_x=qstar!=0. No assumption that V is real was used; the only inequality was the explicit rational calculation(13).

## 5. Global elimination of W and a uniformly monic quartic

Define the polynomial

    N(V)=(1+L(V))P_x(V)-L(V)P_y(V),
    W(V)=-N/qstar=12N/Gamma,                      (14)

and the cross-equation

    E(V)=Q_y(V)P_x(V)-Q_x(V)P_y(V).                (15)

Because the cubic coefficients of P_x and P_y are both4, their difference has degree<=2. Hence N and W have degree<=3, despite the initially displayed product of a linear and a cubic polynomial.

The exact ideal identity, over Q[V,W], is

    (P_x+Q_xW, P_y+Q_yW)=(W-W(V), E(V)).           (16)

To prove both directions without saturation, combine the two left generators by(12): the result is qstar*(W-W(V)). Their Q_y,-Q_x combination is E. Conversely, after imposing W=W(V), call their remainders e_x,e_y. They satisfy

    (1+L)e_x-Le_y=0,
    Q_y e_x-Q_x e_y=E.

The determinant of this two-by-two system is -qstar, a rational unit. Thus E=0 forces both remainders to vanish in EVERY coefficient algebra, with nilpotents allowed. This is an ideal identity, not a point-only equivalence.

The coefficients needed to check exact degrees are small. From(9),

    [V^2](P_x-P_y)=-4d(s-4),
    [V]L=-1/d,
    [V^3]N=4+4(s-4)=4(s-3),
    [V^3]W=48(s-3)/Gamma.                         (17)

This last coefficient is a nonzero rational, so W has degree EXACTLY3. Similarly the V^5 terms of(15) cancel, while

    [V^4]E=48d(s-3)!=0.                           (18)

For verification of the latter sign, the degree4 contribution is

    -48{(x-3)(x-1)-(y-3)(y-1)}+48(y-x)
      =48d(s-3).

We therefore have a uniformly defined MONIC quartic

    M(V)=E(V)/(48d(s-3)).                          (19)

All divisions in(14),(19) are by proved rational units, not by parameter polynomials. No zero leading-coefficient stratum has been omitted.

## 6. The two remaining rows become cubics, with exact read-back

Substitute W=W(V). Let

    F0(V)=A_x(V,W(V)),
    F1(V)={A_y(V,W(V))-A_x(V,W(V))}/d.             (20)

Equation(6) shows deg F0<=6. The W^2 terms cancel in F1 and the coefficient of W in their divided difference is V+(s-5)/6. Thus deg F1<=4 and

    [V^4]F1=48(s-3)/Gamma.

For a completely finite formula, that divided difference is

    F1=(V+(s-5)/6)W(V)+V^3/6+(s-5)V^2/4
       +(s^2-p-9s+26)V/24
       +(s^3-2ps-14(s^2-p)+71s-154)/720.           (21)

The numerator in(21) comes from the divided differences of the cubic and quartic scalar factors in(6); no evaluation at actual parameters was run.

Define

    R1=F1-E/(d*Gamma),
    R0=rem_M(F0).                                 (22)

The leading coefficients(18),(20) cancel in R1, giving deg R1<=3. The remainder R0 is uniquely and finitely specified by division by the monic quartic M; deg R0<=3. Since deg F0<=6, this requires only the formal cancellation of its degree6,5,4 coefficients. No such coefficient calculation was executed. Zero or lower-degree R0,R1 are allowed; no independence or nonzero row assertion is made.

Combining(10),(16),(19)-(22) proves the promised exact isomorphism of guarded normalized rings:

    Q[V,W,W^-1]/(A_x,B_x,A_y,B_y)
       ~= Q[V,W(V)^-1]/(M,R0,R1).                 (23)

The map is W->W(V), V->V. For the inverse, M=0 gives E=0; R1=0 then gives F1=0; R0=0 gives F0=0. Therefore A_x=A_y=0, and(16) gives P_x+Q_xW=P_y+Q_yW=0, hence B_x=B_y=0. Every original contact equation and the W!=0 guard is restored. Base extension of(23) to ANY Q-algebra preserves the identity, including nilpotents. The initial u-normalization is a field-point assertion (or the explicitly localized u-unit coordinate chart); it is not a claim that arbitrary nonunit u can be scaled in an arbitrary ring.

Over an algebraically closed characteristic-zero field, simultaneous normalized contacts exist exactly when the monic greatest common divisor

    G(V)=gcd(M(V),R0(V),R1(V))                     (24)

has a root at which W(V)!=0. Constants and zero residuals are retained in this formulation. Equivalently, since deg G<=4, nonexistence holds exactly when G divides W^4; multiplicities up to4 are then all covered. In ideal language it is exactly the vanishing of the guarded quotient(23). No gcd, resultant, norm, factorization or certificate was calculated.

As a precise remaining quantity, the dimension over Q of(23) is an integer between0 and4. It is zero exactly in the nonexistence case. This dimension includes nilpotent multiplicity and is not a count of distinct points. If a field point exists, its V is a root of the rational monic quartic M, and W is the explicit polynomial(14), so the generated coefficient field has degree<=4. The original unnormalized scale u may of course be arbitrary in K; this finite-degree statement concerns the normalized coefficients only.

## 6A. A second uniform unit: monic cubic and two quadratic rows

The cubic row R1 in(22) is not merely of bounded degree. Its leading coefficient is a nonzero rational uniformly on(3). Here are the finite scalar-coefficient calculations that prove this without computing a whole remainder:

    [V^2]N=(-3s^2+86s-71-72p)/15,
    [V^3]E/d=(48s^2-288p-96s+496)/5.              (25)

For the first identity use [V^2]P_x=4(x-3)(x-1),

    ([V]P_x-[V]P_y)/(-d)
        =(4(s^2-p)-33s+83)/5,

and L=(x-1-Vstar)/d-V/d in(14). The second follows by collecting exactly the three degree3 products Q2*P1, Q1*P2, Q0*P3 in(15). Thus it includes the previously easy-to-miss Q0*P3 contribution.

From(21),(22),(17),(25),

    [V^3]R1=1/6-4(s-3)^2/Gamma
       =-Omega/(6Gamma),
    Omega=24(s-3)^2-Gamma
          =15s^2-36p-30s+35.                      (26)

Again the required sign is a statement only about rational exponents. With xi,eta as in(13),

    Omega=5/3+10(xi+eta)+12(xi^2+eta^2)
                           +3(xi-eta)^2>0.       (27)

Consequently R1 has degree EXACTLY3 and its leading coefficient is a proved rational unit. Define

    J3=-(6Gamma/Omega)R1,
    Z0=rem_(J3)F0,
    Z1=rem_(J3)M.                                 (28)

J3 is monic cubic; Z0,Z1 have degree<=2 and may vanish. Their remainders are literal finite monic divisions, not executed coefficient constructions. In the quotient by J3, R1=0 already, and E is a rational multiple of M. Therefore(23) becomes the still stronger exact identity

    Q[V,W,W^-1]/(A_x,B_x,A_y,B_y)
       ~= Q[V,W(V)^-1]/(J3,Z0,Z1).                (29)

Both directions follow by reading back J3->R1, Z1->M and Z0->F0, then section6; no row is discarded. This is the final exceptional algebra(1). Its Q-dimension lies between0 and3, including possible nilpotents. Its nonexistence criterion is equivalently that gcd(J3,Z0,Z1) divides W^3. A surviving normalized coefficient field has degree<=3. No gcd, root or unit verdict for this cubic algebra has been computed or proved uniformly. These are exact bounds and maps, not evidence of existence or an independence claim for the two quadratic rows.

## 7. What was not proved and the smallest exact future discriminator

The transformation has not shown gcd(J3,Z0,Z1)|W^3 uniformly. In particular neither the unit identity for Q_x,Q_y nor the nonzero cubic leading coefficient is a unit identity for the four contact rows. They license only the stated eliminations. The monic cubic and quadratic bounds do not guarantee a surviving root or exclude one. Applying a single-contact existence theorem to conclude that two-contact solutions exist would be invalid.

For each fixed(r,j), the exact unresolved quantity is the dimension0..3 in section6A, or equivalently whether its degree<=3 gcd has a factor not supported on W. The smallest allowed parameter is r=2,j=1, with x=12/7 and y=13/7. Its cheapest exact discriminator is the gcd/remainder test of the LITERAL three finite polynomials(28), with the W guard, and an exact read-back if a zero/unit claim is made. Its cost and coefficient heights are unknown here. This is a description of a possible separately authorized test, not a registration, implementation or execution request. A verdict at this first parameter would not prove a uniform result for all r,j.

No claim of literature novelty or a new canonical OPEN identifier is made. The existing assigned two-exponent question remains unresolved at the explicit finite exceptional-algebra criterion(29).

## 8. Manual changed-hypothesis and zero-locus controls

1. COINCIDENT EXPONENTS MUST SURVIVE. If j=0, then d=0 and the above distinct-exponent elimination is inapplicable. The accepted16l theorem supplies single-contact normalized cubics for every stated x, so the four rows then merely repeat two consistent rows. Formulas dividing by d cannot be extended across that locus. This is the essential changed-hypothesis control against an accidental single-contact impossibility proof.

2. SUBTRACTION SIGN AND TERM INDEX. At the formal exponent X=3, outside the requested interval but permitted as an identity check in(5), the formulas give

       A_3=V^3/6+VW+W^2/2,
       B_3=V^2W/2+W^2/2.

   Thus 24(A_3-B_3)=4V^3+(24V-12V^2)W, exactly P_3+Q_3W. In particular the V^2W sign in(8) is negative. No cubic contact point at X=3 is asserted.

3. BOTH COEFFICIENTS, NOT ONE. At a zero of Q_x, (12) still makes the complementary combination a unit; the proof never discards that locus by using W=-P_x/Q_x. The actual assertion that BOTH vanish is refuted by(11)-(13). No generic-point reasoning is substituted for the exact Bezout identity.

4. RETAIN THE CROSS EQUATION. Replacing the two linear equations only by W=W(V) is insufficient: their second independent combination is E. The determinant argument in section5 needs E=0. Similarly dropping either R0 or R1 is not justified by monicity of M. The proof deliberately retains all three resulting polynomial rows.

5. GUARD AND NILPOTENTS. A root with W=0 does not solve the stated cubic problem. The localization in(23) remains explicit even if a separate field argument would show it redundant on some contact locus. Over nonreduced rings the precise quotient identity is retained; a count of reduced roots cannot replace it. Conversely the presence of a possible nilpotent quotient is not evidence of a field point unless the guarded algebra is nonzero.

6. POSITIVITY PERIMETER. Formula(13) uses only x,y as the prescribed real rational numbers. It gives no positivity of V,W,M,R0,R1 and is not a real-root argument over K. It cannot be used to conclude that the remaining quartic/cubic intersection is empty.

## 9. Read scope and completion

The sole accepted16l source was current-pinned before a new WHOLE read, including its literal finite coefficients and normalization. Its historical UNREVIEWED header is not a new lifecycle claim; root assigned the accepted theorem at that exact content. No other report, provenance, late-contact/middle source, runtime, ledger, peer or current review was read. No mathematical subprocess of any size, sample, CAS, arithmetic code, coefficient artifact, network, process inspection, AWS, agent, shared/frozen/protected edit or downstream launch occurred. Only documentary metadata, apply_patch and the existing publication transaction were used.

Result: exact cubic exceptional relation, two quadratic residuals and all-strata W elimination proved manually; requested uniform existence/nonexistence decision remains GAP. Own WHOLE/raised-OPEN/collision checks precede the unique completion marker. All writers become IDLE by the original20:59:51.005130624UTC cap.

## OPEN(S) RAISED

- UNRESOLVED ASSIGNED QUESTION, no new canonical ID: QUANTITY dim_Q of the guarded finite algebra(29), an integer0..3 for each(r,j), presently undetermined. CHEAPEST TEST the exact r=2,j=1 cubic/two-quadratic gcd with W guard and read-back; cost unknown and no computation authorized or run. This records the assigned gap rather than registering a new research avenue.

## COLLISIONS

status: EMPTY

- NONE — own-only extraction; no corpus/history scan beyond the one permitted input.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18173`.
- Body SHA-256:
  `e788274ae1c26b04e948ad3a62f5c4fc46868283ad61a29deb9a9478a17a8399`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
