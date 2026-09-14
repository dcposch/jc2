# F10 r1 second subleading band: exact affine rank-two elimination

2026-09-09. NEW/PROVISIONAL manual theorem. Basis0d39df3c9fd69c939a8420c54d03228b9077777d is provenance only. First action17:20:44 UTC; controlling stop17:32:44 UTC. ZERO mathematical subprocesses.

## 1. Result and independence

Directly over the accepted17b leading coefficient ring Lambda=B[s,s^-1], the two rows [S^6]E1 and [S^7]E0 are affine-linear in (u,v0,k2), with coefficients in Lambda and with their inhomogeneous parts in Lambda[d0,v1,k3]. Their 2-by-3 coefficient matrix has rank exactly2 over EVERY leading residue field. A specified linear completion has a proved unit determinant and yields a lossless affine elimination of two variables, preserving the first-band equations and EVERY other original residual.

The three first-band coefficients d0,v1,k3 stay independent. No first-band rank/kernel theorem or reduced-coordinate substitution is used. Only the three current-pinned accepted16r/17b reports in PINS.json were read WHOLE. This is not a dependent composition with an unreviewed previous report, not a full-system point/unit result, and not an implementation or dispatch license.

## 2. The exact graded pieces from accepted16r

Use the complete17b substitution

    F=d1=v/(w*s), H=v2=1/(w*s²), a=k4=1/(w*s³),
    w=R(v)/(112L(v)), b=1/(s^5*f5), omega=w*s^8*f5.

The polynomials p,L,R and f5 are exactly those defined in the accepted leading report; B=Q[v]/(p), without selection of any factor. All denominators displayed here are accepted units. The scalar v in B is distinct from the original coefficient polynomial v(S), and s remains an unrestricted unit.

Put theta=t/S, reciprocal to17b's leading variable. In weights wt(S)=wt(t)=1, the leading parts are

    A4=S^4 C(theta), C=theta³+F theta²+H theta+a,
    B7=S^7 D(theta), D=sum_(i=0)^5 D_i theta^i,
    D5=1, D0=b,
    4C D'-7C'D=-theta^7.                          (1)

D_i are indexed by theta powers, the reverse of the leading producer's indexing. Equation (1) is an identity in Lambda, by the accepted leading substitution, not merely a field-point equality.

The NEXT TWO parts of A follow from f=-u+d0S+FS² and h=(1-u d0)+(v0-uF)S+v1S²+HS³:

    A3=S³ Z(theta), Z=d0 theta²+v1 theta+k3,
    A2=S² U(theta), U=q theta²+l theta+k,
    q=-u, l=v0-uF=v0+Fq, k=k2.                   (2)

Thus (q,l,k) is an invertible linear change of (u,v0,k2), with inverse u=-q,v0=l-Fq,k2=k. No coefficient or stratum is normalized.

Write the mate's corresponding homogeneous pieces as B6=S^6 J(theta) and B5band=S^5 V(theta). Both J,V have degree<=4: the literal coefficient B_5(S)=S² has no lower homogeneous piece. The name B5band is NOT a change to B_5(S).

## 3. Reconstruct J directly, without imposing its two residuals

Let Z2=d0,Z1=v1,Z0=k3. The weight-eight upper equations are obtained from16r by taking the indicated homogeneous coefficients. Their polynomial is

    4C J'-6C'J+3Z D'-7Z'D.

For j=4,3,2,1,0, set its theta^(j+2) coefficient to zero. With J_i=0 for i>4 and D_i=0 outside0..5, the exact five-step recurrence is

    (4j-18)J_j=-(4j-8)F J_(j+1)
                   -(4j+2)H J_(j+2)-(4j+12)a J_(j+3)
                   -sum_(i=0)^2 (3j+9-10i)Z_i D_(j+3-i). (3)

Its diagonal values -2,-6,-10,-14,-18 are fixed rational units. Hence J is a specified homogeneous linear polynomial in the kept Z coefficients. The theta and constant coefficients of this polynomial are NOT set to zero in this task; they remain the two first-band equations among the full original residuals.

Define the explicit forcing polynomial

    W=3Z J'-6Z'J.                                (4)

It depends only on d0,v1,k3 and the leading ring. It is homogeneous quadratic in these three kept coefficients. Its degree is at most4: the apparent theta^5 coefficient cancels since 3*4-6*2=0. No unknown u,v0,k2 enters it. Definition (3), not an independent unconstrained J, is essential.

## 4. Literal second-band equation and all five upper steps

The weight-seven part of the actual target is 2u*S*t^6; all other target pieces have weight9 or at most6. The degree-seven Jacobian comprises (A4,B5band), (A3,B6), and (A2,B7), and no others. Therefore

    4C V'-5C'V+2U D'-7U'D = -2q theta^6-W.       (5)

In particular the target is NOT zero in this band. The first term on the right is linear in the same q which is the theta² coefficient of U.

Writing V=sum_(j=0)^4 V_j theta^j, the exact theta^6..theta² equations give

    V4=2q,
    V3=(6F V4+3l-6D4 q+W5)/3,
    V2=(2F V3+11H V4+10k+D4 l-8D3 q+W4)/7,
    V1=(-2F V2+7H V3+16a V4
                              +8D4 k-D3 l-10D2 q+W3)/11,
    V0=(-6F V1+3H V2+12a V3
                              +6D3 k-3D2 l-12D1 q+W2)/15. (6)

Here W_i=[theta^i]W, and W5=0 by (4); retaining that symbol makes the extraction explicit. Before solving the diagonals are1,-3,-7,-11,-15. More generally the coefficient on V_j is4j-15; the other C_i V_h terms have coefficient4h-5i and U_i D_h terms coefficient2h-7i, with i+h=j+3. At theta^6, the left side before the target is V4-4q, while the target is -2q, proving V4=2q=-2u exactly as16r's B4 requires.

After (6) the two literal residuals are

    R1=[S^6]E1
       =8a V2-H V1-10F V0
                             +4D2 k-5D1 l-14b q+W1,
    R0=[S^7]E0
       =4a V1-5H V0+2D1 k-7b l+W0.             (7)

Indeed the band is S^7 times its theta polynomial, so theta and constant give these exact S slots. Formula (6) makes (7) affine-linear in (q,l,k); hence also in (u,v0,k2). The inhomogeneous part is quadratic in the kept first-band coefficients. Neither ell nor k1 enters this band. Equations (3),(4),(6),(7) are a small exact read-back, not a coefficient artifact or a projected source system.

## 5. Independently derive the homogeneous kernel with its target term

For differences of two second-band solutions with the same Z, W cancels but the q term of the target does NOT. Thus the homogeneous matrix problem is

    L2:=4C V'-5C'V+2U D'-7U'D=-2q theta^6,
    U=q theta²+l theta+k.                        (8)

Set T=4C V-7DU; it has degree<=7. Direct differentiation of (8) yields

    T'=9(C'V-D'U)-2q theta^6.

Using the determinant7C'D-4CD'=theta^7 from (1) gives

    U=N_U/theta^7,
    N_U=(4/9)C(T'+2q theta^6)-C'T,
    V=N_V/theta^7,
    N_V=(7/9)D(T'+2q theta^6)-D'T.                (9)

The polynomiality of U forces the coefficients of N_U through theta^6 to vanish. Define h0=1 and h1,...,h7 by

    4a*i*h_i=-sum_(j=1)^min(3,i)(4i-13j)c_j*h_(i-j),
    c1=H,c2=F,c3=1, i=1,...,7.                   (10)

This finite recurrence is the purely formal shorthand h_i=[theta^i](C/a)^(9/4); all its denominators are fixed rationals and the already-proved unit a. For a general solution, the equations below theta^6 give T_i=T0*h_i for i<=6. The theta^6 equation gives

    T7=T0*h7-(2/7)q.

Independently the leading theta² coefficient of U in (9) is (T7+8q)/9. It must equal q, so

    T7=q, q=(7/9)T0*h7.                         (11)

This leading consistency is load-bearing. The naive unmodified truncation of (C/a)^(9/4) would not account for the actual 2u theta^6 target.

Take T0=1, set q_star=7h7/9 and

    T_star=sum_(i=0)^6 h_i theta^i+q_star theta^7.

Construct U_star,V_star from (9). N_U is divisible by theta^7 by (10),(11); its degree<=9 gives deg U_star<=2, with theta² coefficient exactly q_star. The identity

    C N_V=(7/4)D N_U+(theta^7/4)T_star

and the unit C modulo theta^7 imply that N_V is also divisible by theta^7; it has degree<=11, so deg V_star<=4. These are polynomial arguments over arbitrary Lambda-algebras, not a localization at a root or a squarefree assumption. Substitution gives T=4CV-7DU and T'+2q theta^6=9(C'V-D'U), recovering (8).

The kernel coefficient vector beta in column order(q,l,k) is explicitly

    beta2=q_star,
    beta1=2F*q_star-h6/3,
    beta0=3H*q_star+(2/3)F*h6-(7/9)h5.          (12)

Conversely every solution of (8), including over a nonreduced coefficient algebra, is T0 times this solution: (10),(11) determine its whole T, and (9) then determines U,V. This rederivation uses only the accepted leading identity and the present band, not any preceding-band kernel result.

## 6. Rank everywhere and the exact affine completion

Over any leading residue field, U_star cannot be zero. If it were, q_star=0 and T_star has degree<=6. Equation (9) would give 4C T_star'-9C'T_star=0. Its highest coefficient is (4 deg T_star-27) times the nonzero leading coefficient of T_star, since C is monic of degree3. This cannot vanish in characteristic zero when deg T_star<=6; T_star(0)=1 also prevents the zero polynomial. Thus beta is nonzero in EVERY residue field, without assuming a generic v, simple roots or a selected irreducible factor of p.

Let M be the 2-by-3 coefficient matrix of (7) in (q,l,k); it is computed by (6) with W=0. The five fixed diagonals ensure V is uniquely determined from U. Section5 shows its joint kernel has dimension exactly1 in every residue field, so rank M=2 everywhere. Its maximal minors generate the unit ideal; this does not say that a single specified2-by-2 minor is a unit.

Let V^h(U) denote (6) with W=0 and define

    rho(U)=4a V^h_0(U)-7b k.                    (13)

On beta this is the constant coefficient of T_star, namely1. Form N by stacking the two rows of M and the row rho. On every residue field its first two rows have kernel spanned by beta and its last row sends beta to1. Hence det N is a UNIT in Lambda. This is a proved unit determinant of a specified completed3-by-3 matrix, not a computed determinant value or individual unit minor. The formula N^-1=adj(N)/det(N) is consequently defined over the full leading ring.

Write (7) as M U+c(Z), with c(Z) obtained by putting U=0 in the ENTIRE recurrence (6),(7). It is not a new free parameter. The exact affine back-map is

    (q,l,k)^T=N^-1*(-c1(Z),-c0(Z),Y)^T,
    u=-q, v0=l-Fq, k2=k,                        (14)

where Y=rho(U) is unrestricted. Equivalently use the particular solution N^-1*(-c1,-c0,0)^T plus beta*Y. The inverse read-back is (13). Every coefficient depends only on the leading ring and the kept independent Z coefficients; no division by u, a first-band residual, or a new parameter is used.

This proves lossless affine elimination on all strata, before imposing either first-band equation. The completed matrix and c are specified by short finite recurrences; no actual inverse coefficient list, minor, factorization or implementation was computed. The exact ring argument remains valid after any coefficient-algebra base change because the displayed determinant is already a unit.

## 7. Retain the whole source system, including the earlier band

Start from accepted17b's17 residual slots over Lambda[u,ell,d0,v0,v1,k1,k2,k3]. Replace only u,v0,k2 by (14). The resulting presentation is over

    Lambda[d0,v1,k3,ell,k1,Y].

Retain EVERY original residual except the two equations solved in (7): this means [S^0..S^5]E1 together with [S^7]E1, and [S^0..S^6]E0 together with [S^8]E0, at most15 slots. In particular the two first-band equations are explicitly retained; they have not been solved, substituted or presumed. All complete mate coefficients, inverse conditions, original leading read-back and omega=w*s^8*f5 are transported by the same map. No row is dropped by projection, no source scalar s is normalized, and Y is not an output gauge.

The two affine coordinates M U+c(Z) and Y form an invertible affine coordinate change over Lambda[Z]; quotienting the first two by zero proves the polynomial-quotient isomorphism and its inverse (13),(14). The counts are envelopes, not emitted rows or dimensions. No composition with a provisional previous elimination, full-system point, properness/unit decision, source/JC2 exclusion or measured speedup is asserted. The frozen17-row code is unchanged.

## 8. Exact changed-object controls and stop

The forcing W is genuinely needed even before earlier residuals are imposed. Set d0=v1=0,k3=1, so Z=1. Directly from (3), J4=J3=0,J2=3/2, and J1=(6D4-3F)/7. Therefore W=3J' has W1=9 and W0=3J1, with all W_i for i>=2 zero. Taking U=0 in (6) then gives V=0, so the TRUE second-band row R1 is9. Omitting W would falsely give both rows zero at this same changed object. This is a guarded leading/upper-stage control, NOT a full-source point: its earlier and later residuals are not asserted zero.

The normalized nonzero beta is a second control: adding beta to the particular solution in (14) preserves both affine rows and changes Y by1. Thus this band does not force all three new variables to prescribed constants or give a contradiction. Dropping one row would enlarge the kernel; concretely the unit N supplies N^-1*(1,0,0)^T, whose homogeneous row values are exactly(1,0) and whose read-back is0. This is an exact manual changed vector, not a sampled numerical rank.

Finally, deleting the actual 2u theta^6 term would change V4=2q into V4=4q and change (11). That is a different linearized problem. The preserved target term, complete W forcing, independent earlier variables and both residual rows are all load-bearing.

Only the specified three accepted reports were read. The proof is restricted to r1 and this second band; no all-r/higher-band extension or further task is authorized. No mathematical subprocess, code change, emitted residual/source artifact or remote action occurred. Own whole/raised-OPEN checks precede the marker; terminal custody verifies unchanged inputs and all writers idle.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN extraction; no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13647`.
- Body SHA-256:
  `8ee7676df4c15b55df21c7127dbca9b90b4d506b6e40489b556780a3fd4d4e6d`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
