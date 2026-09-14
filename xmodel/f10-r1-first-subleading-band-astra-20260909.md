# F10 r1: exact first subleading band and lossless rank-two elimination

2026-09-09. NEW/PROVISIONAL pure manual proof. Basis0d39df3c9fd69c939a8420c54d03228b9077777d is provenance only. First action16:57:35 UTC; controlling stop17:09:35 UTC. ZERO mathematical subprocesses.

## 1. Result and precise scope

Over the accepted leading coefficient ring Lambda=B[s,s^-1], B=Q[v]/(p), the two exact rows [S^7]E1 and [S^8]E0 are homogeneous linear forms in (d0,v1,k3). They have rank EXACTLY TWO over EVERY residue field. Their joint kernel has a globally specified generator and an explicit polynomial read-back coordinate. Consequently these three variables can be replaced losslessly by one unrestricted coordinate Y, retaining every other full residual and the accepted source reconstruction.

This is stronger than a generic-v rank assertion. No individual 2-by-2 minor is asserted to be a unit or computed. Rather, the maximal minors generate the unit ideal, and a specified completion with the read-back row has a proved unit 3-by-3 determinant. The inverse on the zero band is given explicitly below without computing either determinant. It is not a new gauge or an assertion of a full point, unit ideal, source exclusion, or performance gain.

Only accepted16r and the two17b reports listed in PINS.json were read whole after their current hashes matched. No current code, other mathematical report or live gate was read. This report does not change the frozen17-row implementation or authorize an execution.

## 2. Leading ring and the exact weight-eight equation

Use the accepted r=1 substitution

    F=d1=v/(w*s), H=v2=1/(w*s²), a=k4=1/(w*s³),
    w=R(v)/(112L(v)), b=1/(s^5*f5),
    omega=w*s^8*f5.

Here p,E,L,R,f5 and their exact definitions are those of17b; B is its complete degree-seven leading algebra, not a chosen factor. The elements s,w,f5,L,a,b are proved units. No s=1 normalization is made. The symbol v in B is not the coefficient polynomial v(S) of16r.

For the present calculation use theta=t/S, the RECIPROCAL of the leading producer's T=S/t. Write

    A4=S^4 C(theta), C=theta³+F theta²+H theta+a,
    B7=S^7 D(theta), D=sum_(i=0)^5 D_i theta^i,
    D5=1, D0=b.

D_i here are indexed by powers of theta: they are the reverse of the leading producer's D_i. From the accepted leading identity, or directly from the weight-nine Jacobian,

    4C D'-7C'D=-theta^7.                         (1)

All these are identities IN Lambda, not merely pointwise identities. The first subleading A part is exactly

    A3=S³ U(theta), U=d0 theta²+v1 theta+k3.       (2)

Indeed f=-u+d0S+FS², h=(1-u d0)+(v0-uF)S+v1S²+HS³, and k=k1S+k2S²+k3S³+aS4. Thus u,ell,v0,k1,k2 occur in lower weights, not in (2). Since B5=S² has no lower term, the weight-six part of B is

    B6=S^6 V(theta), deg V<=4.

The target Delta has no weight-eight term. Its top is -S²t^7 of weight9; the next term involving u has weight7, and the other terms are lower. Therefore the ENTIRE first subleading bracket equation is

    L(U,V):=4C V'-6C'V+3U D'-7U'D=0.             (3)

This follows by applying the homogeneous chain rule separately to (A4,B6) and (A3,B7). No lower source term or product of two lower bands can reach weight8.

## 3. Five fixed-rational steps and the two literal residuals

Write U2=d0,U1=v1,U0=k3, and V=sum_(j=0)^4 V_j theta^j. Setting the theta^6 through theta² coefficients of (3) to zero gives exactly the accepted upper Euler band. A convenient full read-back is

    V4=U2/2,
    V3=(4F V4+8U1-2D4 U2)/6,
    V2=(10H V4+15U0+5D4 U1-5D3 U2)/10,
    V1=(-4F V2+6H V3+16a V4
                         +12D4 U0+2D3 U1-8D2 U2)/14,
    V0=(-8F V1+2H V2+12a V3
                         +9D3 U0-D2 U1-11D1 U2)/18. (4)

These are linear forms in U over Lambda. The relevant diagonal coefficients before moving signs are -2,-6,-10,-14,-18, all fixed rational units. Equivalently the j-th equation has coefficient 4j-18 on V_j; the terms involving C_i V_l have coefficient 4l-6i, and those involving U_i D_l have coefficient 3l-7i, with i+l=j+3. This checks every term of (4).

After (4), the remaining two coefficients are precisely

    R1=[S^7]E1
       =8a V2-2H V1-12F V0
                            +6D2 U0-4D1 U1-14b U2,
    R0=[S^8]E0
       =4a V1-6H V0+3D1 U0-7b U1.               (5)

The reason these exact S slots occur is S^8 L(theta): its theta coefficient is S^7t and its constant is S^8. The target has zero coefficients in those slots. No additional residual is hidden in the band; degrees of (3) are at most6, and (4) already kills the other five coefficients. Let M be the 2-by-3 matrix of (5) in column order (U2,U1,U0).

## 4. An exact description of the whole kernel

Define a degree-at-most-seven polynomial T from a solution of (3) by

    T=4C V-7D U.

Differentiating and using (3) gives

    T'=10(C'V-D'U).

The determinant of these two linear equations for V,U is theta^7, by (1). In the rational function ring, and therefore as exact divisibility identities,

    U=((2/5)C T'-C'T)/theta^7,
    V=((7/10)D T'-D'T)/theta^7.                  (6)

Because C(0)=a is a unit, polynomiality of U says that the coefficients through theta^6 of (2/5)C T'-C'T vanish. They determine T uniquely from T0. Define t0=1 and t1,...,t7 by the fixed finite recurrence

    2a*i*t_i=-sum_(j=1)^min(3,i) (2i-7j)c_j*t_(i-j),
    c1=H,c2=F,c3=1, i=1,...,7.                  (7)

All denominators are already-proved units a and nonzero rationals. In formal shorthand this is

    T_star=trunc_(theta degree<=7)(C/a)^(5/2).

The shorthand denotes only (7), not an analytic choice or an executed series calculation. Every solution of (3) has T=T0*T_star, including over an arbitrary Lambda-algebra with nilpotents.

Conversely T_star gives polynomial U_star,V_star by (6). The first numerator is divisible by theta^7 by (7), and has degree<=9, hence U_star has degree<=2. For the second numerator N_V, with first numerator N_U, the useful identity is

    C*N_V=(7/4)D*N_U+(theta^7/4)T_star.

Since C is a unit modulo theta^7, N_V is also divisible by theta^7; its degree is at most11, so deg V_star<=4. This argument uses no localization at a root of C. Substitution in (6) gives 4C V_star-7D U_star=T_star and C'V_star-D'U_star=T_star'/10, which recover (3). Thus these are actual kernel polynomials, not merely formal approximations.

The coefficient vector beta=(beta2,beta1,beta0) of U_star is explicitly

    beta2=-t7/5,
    beta1=(4/5)F*t7-(3/5)t6,
    beta0=(9/5)H*t7+(2/5)F*t6-t5.              (8)

Equations (4),(7),(8) are the promised small exact coefficient prescription; no full residual or large source polynomial was emitted.

## 5. Rank on EVERY residue field, and the completed unit determinant

Over any residue field of Lambda, U_star is NONZERO. Otherwise the first numerator in (6) vanishes identically, giving 2C T_star'-5C'T_star=0. The derivative of T_star²/C^5 is then zero. In characteristic zero it is a nonzero scalar, since T_star(0)=1 and a!=0. Hence 2 deg T_star=5 deg C=15, impossible for an integer degree. This argument does not assume generic coefficients, simple roots, reducedness of B, a particular number field or a factorization of p.

For any kernel solution the recurrence (4) uniquely determines V from U. Section4 then says U=T0*U_star. The kernel of M over every such field therefore has dimension exactly1, and M has rank exactly2. The ideal generated by its 2-by-2 minors is consequently the unit ideal in Lambda: a proper ideal of minors would lie in a maximal ideal, where the rank would drop. This does NOT say that one specified 2-by-2 minor is a unit.

There is nevertheless a completely specified completion. For arbitrary U define the linear functional

    rho(U)=4a V0(U)-7b U0,                      (9)

using the recurrence (4). On U_star, (9) is the constant coefficient of T_star, namely1. On every kernel vector it is exactly T0. Let N be the 3-by-3 matrix whose rows are R1,R0,rho in the same three columns. Over every residue field, its first two rows have one-dimensional kernel spanned by beta and its last row takes beta to1. Thus N is invertible in every residue field. Its determinant is a UNIT of Lambda, by the maximal-ideal criterion.

This is a proved unit determinant of the SPECIFIED COMPLETED matrix, not an assertion about an individually computed maximal minor of M. No determinant value, factorization, Euclidean certificate or inverse coefficient list has been calculated. The exact inverse can be specified as adj(N)/det(N), dividing only this now-proved unit. On the zero band its much simpler explicit form is

    U2=beta2*Y, U1=beta1*Y, U0=beta0*Y,
    Y=rho(U).                                    (10)

Section4 proves (10) over arbitrary Lambda-algebras directly, not just on reduced field points. In particular it supplies both polynomial maps on the quotient. No rank stratum is removed and no source parameter s is normalized.

## 6. Lossless full-system interface

The accepted17b retained system has eight polynomial variables u,ell,d0,v0,v1,k1,k2,k3 and the unit s over B, with all17 remaining residual slots. Replace (d0,v1,k3) by (10), keeping Y unrestricted, and substitute this back-map in EVERY other residual and the full reconstructed mate. The inverse on the band is the exact functional (9).

This gives a quotient-ring isomorphism to a presentation over

    B[s,s^-1][u,ell,v0,k1,k2,Y]

whose remaining envelopes are EVERY coefficient [S^0..S^6]E1 and EVERY coefficient [S^0..S^7]E0: at most15 rows. These are formal presentation counts, not emitted nonzero-row counts, dimensions or runtime estimates. The two rows (5) are removed only after the proved coordinate-one elimination; no lower equation, inverse condition, fixed leading value or restored top-product guard is dropped. The accepted guard remains omega=w*s^8*f5, and the leading coefficient read-back remains the original17b substitution.

The mate and every lower coefficient must still satisfy their ENTIRE substituted equations. Y is not an output-shear parameter or a new gauge and is not set to zero. This statement preserves the accepted field/source endpoints but supplies no point, properness/unit decision, F10/JC2 exclusion or measured speedup. Powers of a^-1 in (7) and subsequent substitutions may increase expression size. The frozen implementation is unchanged; future exact read-back would be a separate authorized task.

## 7. Changed-object controls and limits

The nonzero U_star itself is a meaningful control: Y=0 and Y=1 give distinct band solutions, since rho(U_star)=1. Thus the two exact band equations do not force all three subleading source coefficients to vanish. Declaring A3=0 would delete an actual one-dimensional family of solutions to this band; none is asserted to solve the lower residuals.

For a row-deletion control, the proved unit matrix N defines the coefficient vector Z=adj(N)*(1,0,0)^T/det(N). It is an exact vector over the same ring, with R1(Z)=1,R0(Z)=rho(Z)=0. Dropping R1 therefore admits this changed object, while the true pair (5) rejects it. Swapping the first two standard coordinates gives the corresponding control for dropping R0. These are manual algebraic controls with exact values, not sampled ranks or an executed inverse.

If the target were changed by a weight-eight term epsilon*S^8, the second row would instead be R0=epsilon. The homogeneous zero-band back-map (10) would no longer apply without its inhomogeneous part. This makes the absence of weight8 in the ACTUAL Delta a load-bearing hypothesis; one cannot infer the result merely from the weight-nine leading ODE.

No optional all-r generalization is proved here. The exact r1 rank, recurrence, read-back and complete lower-row transport are the new scope. No individual 2-by-2 unit minor or actual retained polynomial artifact is claimed. All computations are manual and only the three prescribed reports were read; current pins, own whole/raised-OPEN check and terminal custody accompany publication. All writers idle at handoff; no further authority.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN extraction; no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12207`.
- Body SHA-256:
  `179854443e867b15859058b3f293307b7d1ffcb376a83a0e95ac77454b4d4d5b`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
