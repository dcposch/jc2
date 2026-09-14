# F10 r1 third band: exact affine k1 elimination

2026-09-09. NEW/PROVISIONAL manual theorem, pending independent review. First action17:37:58UTC; controlling stop17:49:58UTC. ZERO mathematical subprocesses of any size. Basis0d39df3c9fd69c939a8420c54d03228b9077777d is provenance only.

## 1. Outcome and exact scope

Over the accepted leading coefficient algebra Lambda, the literal third-band rows [S^5]E1 and [S^6]E0 are affine-linear in k1, with all six earlier coefficients d0,v1,k3,u,v0,k2 kept independent. Their coefficient column has an EXPLICIT polynomial left inverse using only the already-required unit a. Consequently k1 is eliminated losslessly and precisely one compatibility polynomial is retained. All other original residual rows, all boundary conditions, all guards and the free scaling survive by substitution.

This is a direct consequence of accepted16r/17b, NOT a composition with either earlier-band report. Applied alone to the accepted17b presentation it gives seven polynomial unknowns and the unit s over B, with at most16 retained scalar slots. No equations were emitted or implementation changed. No claim of a full point, unit ideal, runtime gain, or independence/nonvanishing of the new compatibility polynomial is made.

Exactly three inputs were hashed current before their WHOLE reads:

- xmodel/f10-whole-mate-euler-elimination-astra-20260909.md, SHA a5ab487c4619742b6252e2503488eea4d6e927b58fd2821207cc85bcba7cf8d5.
- xmodel/f10-r1-leading-coefficient-compression-astra-20260909.md, SHA ead39705189f7faf338bab7937488e96c3ddf296c9ba0eed328ea63442619fb7.
- xmodel/f10-r1-leading-univariate-gate-fable5-20260909.md, SHA 1708746e6d54d745b7a33df54dd339b197df7ec33b1a67c79877ab2429e6946e.

Their accepted scope overrides historical producer-only headers. No other mathematical report, code, live review, earlier-band proof, corpus or primary source was read. The initial combined tool output truncated one input; that input was reread separately to EOF. All new derivation below is manual.

## 2. Accepted leading ring and actual homogeneous pieces

Use Lambda=B[s,s^-1], where B=Q[v]/(p(v)) is precisely the accepted degree-seven leading algebra. Retain its accepted elements w,f5,L and the proved units s,w,f5,L. In particular

    F=v/(w*s), H=1/(w*s^2), a=1/(w*s^3),
    b=1/(s^5*f5), omega=w*s^8*f5.

No field factor or s=1 chart is selected. The scalar v in B is distinct from the coefficient polynomial v(S) of16r. Put theta=t/S, solely to write homogeneous polynomial pieces. Reversing the accepted leading polynomials gives

    A4=S^4 C(theta), C=theta^3+F theta^2+H theta+a,
    B7=S^7 D(theta), D=sum_(i=0)^5 D_i theta^i,
    D5=1, D0=b,
    4 C D'-7 C'D=-theta^7.                    (1)

Primes in this report mean theta derivatives unless explicitly stated otherwise. The D_i notation is the reverse of the coefficient indexing in the accepted producer. Equation(1) is its exact entire leading equation, not an asymptotic replacement.

The actual lower pieces of A from f=S d-u and h=1-u d+S v are

    A3=S^3 Z, Z=d0 theta^2+v1 theta+k3,
    A2=S^2 X, X=-u theta^2+(v0-uF)theta+k2,
    A1=S Y,  Y=y theta+k1, y=1-u*d0.          (2)

There is no weight-zero A piece after the accepted k(0)=0 gauge. All six coefficients in Z,X remain independent here; neither earlier-band lower equation is imposed. The variable ell first appears below the present target weight and therefore does not enter this band.

For any homogeneous expressions S^i f(theta),S^j g(theta), direct differentiation gives

    [S^i f,S^j g]_(S,t)
       =S^(i+j-2)(i f g'-j f'g).              (3)

This identity fixes the orientation used throughout.

## 3. Earlier mate pieces directly from the accepted upper equations

Write B6=S^6 J(theta), B5band=S^5 K(theta), and B4band=S^4 V(theta). These symbols denote homogeneous pieces of the WHOLE reconstructed mate, not its t-indexed coefficients B_j(S). They satisfy

    deg J<=4, deg K<=4, deg V<=2.              (4)

Here is a complete small recurrence definition of the pieces needed in this proof, directly from16r. Coefficients outside the displayed degrees are zero. In descending order j=4,3,2,1,0, choose J_j so that every coefficient theta^(j+2) vanishes in

    4CJ'-6C'J+3ZD'-7Z'D.                      (5)

The diagonal coefficient of J_j is 4j-18, namely -2,-6,-10,-14,-18. Thus these five steps are fixed-rational inversions and define J without assuming its two remaining coefficients vanish. Explicitly, if c3=1,c2=F,c1=H,c0=a, the coefficient contribution from the first two terms at theta^(j+2) is

    sum_(i+l=j+3) (4l-6i)c_i J_l.

The same descending convention chooses K_j so that coefficients theta^(j+2) vanish in

    4CK'-5C'K+2XD'-7X'D
                    +3ZJ'-6Z'J-2u theta^6.   (6)

Its diagonal is 4j-15, namely1,-3,-7,-11,-15; its first two terms contribute sum_(i+l=j+3)(4l-5i)c_i K_l. Equations(5),(6) specify every forcing term and all five upper steps. They are coefficient-projection prose, not emitted polynomials or executed algebra. The two lower rows of each expression remain original rows and are NOT presumed zero.

The leading coefficients from these recurrences are

    J4=d0/2, K4=-2u.                          (7)

For (5), its theta^6 coefficient is -2J4+d0. For (6), its theta^6 coefficient is K4+4u-2u. The possible theta^7 terms vanish by homogeneity. These checks agree with the exact accepted formula B_4(S)=-2uS+(d0/2)S^2+(6F/5)S^3.

The degree restriction on V requires care: literal B_5(S)=S^2 contributes no weight4 coefficient, so V5=0; the displayed B_4 has no constant term, so V4=0; and the accepted beta=[S]B_3=0 gauge gives V3=0. This is an already-accepted global mate gauge, not a new bandwise normalization. Its other lower effects remain in the full recurrence.

## 4. Exact third-band forcing, including the target cancellation

Define the polynomial

    W=3ZK'-5Z'K+2XJ'-6X'J.                    (8)

It depends on the six retained earlier coefficients, not on k1. Its degree is at most5. The exact weight6 target is -2S t^5, so (3) yields

    4CV'-4C'V+YD'-7Y'D=-2theta^5-W.           (9)

No intervening homogeneous piece has been discarded: the four possible pairs of weights summing to8 are (4,4),(3,5),(2,6),(1,7), exactly the four contributions above.

Move the known y part to the right and write

    N=-2theta^5-W-y(theta D'-7D).

Then the unknown k1 enters only as

    4CV'-4C'V+k1 D'=N.                       (10)

The apparently problematic theta^5 row is an exact identity. From (7),

    W5=2*d0*K4-4*(-u)*J4=-2u*d0,
    N5=-2-W5+2y=0.                           (11)

Thus the target coefficient -2 is load-bearing. Dropping it would produce N5=2 and a false upper compatibility failure, even though all source/gauge coefficients were otherwise kept. There is no theta^6 row because V3=0 and both sides have degree at most5.

For i=0,...,4 the remaining forcing coefficients are exactly

    N_i=-W_i-y(i-6)D_(i+1).                  (12)

They are independent of k1. All the earlier nonlinear products in W and y are retained, including every u=0 case.

## 5. All upper read-back and the two literal residuals

Put k=k1 in this section. The theta^4,theta^3,theta^2 equations of(10), in descending order, give

    V2=(5k-N4)/4,
    V1=(4D4*k-N3)/8,
    V0=(-4F V1+4H V2+3D3*k-N2)/12.           (13)

The corresponding operator diagonal coefficients before moving terms are -4,-8,-12. Together with the automatic theta^5 row(11) and the fixed V3,V4,V5, this is every upper-row obligation for this homogeneous band. No t^1 or t^0 equation was used in deriving(13).

The two remaining exact coefficients of the target difference are

    R1=8aV2-8F V0+2D2*k-N1 = [S^5]E1,
    R0=4aV1-4H V0+D1*k-N0 = [S^6]E0.        (14)

Indeed weight6 times theta equals S^5t, while its constant theta coefficient is S^6. This independently fixes the literal indexing, not merely the homogeneous shape.

Writing R=(R1,R0)^t, equations(12)-(14) have the form

    R=h*k+c,

where c is their ACTUAL value at k=0, not an independently adjustable pair. Define

    zeta=(-2F D4+5H+3D3)/12,
    h1=10a-8F*zeta+2D2,
    h0=2aD4-4H*zeta+D1.                      (15)

Then h=(h1,h0)^t is exactly the coefficient column: the homogeneous mate variation is

    V_h=k*((5/4)theta^2+(D4/2)theta+zeta).

This verifies the candidate coefficients by direct upper-row computation. It does not assume any chosen h_i is a unit.

## 6. A literal global left inverse using only a

Here is an explicit finite coefficient prescription for a Lambda-linear functional lambda on any ordered pair (r1,r0). Let

    e_i=[theta^i]C(theta)^(-2), 0<=i<=5,
    e_(-1)=0,
    I_r(theta)=sum_(i=1)^6
                (r0*e_(i-1)+r1*e_(i-2))*theta^i/i,
    P_j(r)=[theta^j] C(theta)^2 I_r(theta),
    lambda(r)=F*P_6(r)-P_5(r)/2.              (16)

The coefficient notation is a finite formal definition in Lambda. Since C(0)=a is an accepted unit, each e_i is a specified polynomial in F,H,a,a^-1 with rational coefficients; for example e0=a^-2. The formal identity C^2 sum e_i theta^i=1 modulo theta^6 determines these coefficients uniquely using only a^2. No analytic series, new field extension, executed coefficient calculation, determinant, factorization, or unproved denominator is hidden. Formula(16), rather than an existential Bezout choice, is the actual left inverse used below.

To prove it, take the homogeneous variation U=k constant, let V=V_h from(15), and set

    T=4CV-7kD, deg T<=5.

Its upper rows hold and its remaining polynomial is r1 theta+r0, where r=h*k. Direct differentiation of(10) and use of(1) give

    T'=8(C'V-kD')+r1 theta+r0,
    C T'-2C'T=2k theta^7+C(r1 theta+r0).      (17)

Also the leading coefficient of T is

    T5=4*(5k/4)-7k=-2k.                     (18)

Divide(17) by the unit formal series C^3. Integrating coefficientwise at zero, through degree6 only, gives

    T=C^2*(T0/a^2+I_r) modulo theta^7.        (19)

The k term starts in degree8 after integration and hence cannot affect this formula. Since deg T<=5 and [theta^6]C^2=1,

    0=T0/a^2+P6(r).

Since [theta^5]C^2=2F, its degree5 coefficient and(18) give

    -2k=-2F P6(r)+P5(r).

Therefore lambda(h*k)=k, and in particular

    lambda(h)=1.                             (20)

This proof is an identity over Lambda and remains valid over EVERY Lambda-algebra, including nonreduced coefficient rings. It is stronger than generic rank: h generates a direct summand, has rank one over every residue field, and has the specified left inverse(16). No entry h1 or h0 is separately asserted invertible.

For completeness the same formula also rules out a hidden homogeneous kernel. If both residuals vanish then(20) gives k=0. Alternatively(19) with r=0 would make T proportional to C^2 through degree6, inconsistent with deg T<=5 unless the proportionality and then k vanish. This argument uses a unit, not an inference from reducedness.

## 7. Exact elimination and the single retained compatibility

Let lambda1=lambda((1,0)), lambda0=lambda((0,1)); these are the explicit elements defined by(16). Equation(20) reads

    lambda1*h1+lambda0*h0=1.

The matrix with columns h and (-lambda0,lambda1)^t has determinant one. Thus the following is a literal unimodular row transformation, over the whole coefficient ring:

    (R1,R0) -> (lambda1 R1+lambda0 R0,
                -h0 R1+h1 R0).

Substitute R=h*k+c. The two rows are equivalent to

    k=-lambda(c),
    Psi=-h0*c1+h1*c0=0.                     (21)

This is the promised all-strata affine elimination and complete two-row read-back. Conversely, substituting the first formula and Psi=0 gives R=0 by the determinant-one inverse. No u, d0, earlier residual, h_i, or Psi is inverted. The parameter ell, although absent from this band, remains in every lower original row.

Starting ONLY with the accepted17b system, replace k1 by(21), retain Psi, and retain all the other original scalar residuals after that substitution. The resulting ambient ring is

    Lambda[u,ell,d0,v0,v1,k2,k3].

The retained scalar slots are E1 indices0..4,6,7 and E0 indices0..5,7,8, together with Psi: at most16. In particular BOTH earlier bands remain literally imposed. No first-band or second-band elimination is composed here. The leading rows and omega guard were already handled by accepted17b; their exact unit-based read-back remains unchanged. The reconstructed whole A/B, their complete inverse-polynomiality conditions, the gauges and the retained scaling all follow by the unchanged accepted16r map.

The displayed row transformation and substitution give an exact quotient-ring isomorphism with the original retained presentation; it is not merely a field-point projection. The forward inverse adds back k1=-lambda(c). Source/Keller consequences, if all retained equations ever have a guarded point, are exactly the accepted16r scope and no stronger. No such point or ideal decision is supplied.

## 8. Changed-object controls and limitations

Actual target control: with the exact source coefficients and gauge, W5=-2ud0 and y=1-ud0. Deleting the target term -2S t^5 changes N5 from zero to2, independent of every parameter. The resulting false incompatibility would occur before the three upper pivots and cannot be repaired by k1. This is a real changed equation, not a numerical sample or a full-source counterexample.

Forcing control: setting W to zero while retaining arbitrary u,d0 changes the automatic theta^5 equation to -2+2(1-ud0)=-2ud0. Thus the earlier-band nonlinear forcing cannot be discarded merely because earlier residuals are retained. This control uses the derived actual W5, without assuming any earlier-band theorem or actual full point.

Two-row control: the literal residual vector r*=(-lambda0,lambda1)^t satisfies lambda(r*)=0 but -h0 r1*+h1 r0*=1. Dropping Psi would therefore fail to preserve the two-row equation under the very same determinant-one transformation. This is an exact changed-residual control, NOT a claim that r* is attained by the source parameters. Similarly lambda(h)=1 shows deleting the first transformed row would lose the unique k1 value. The proof does not assert that Psi is a nonzero polynomial of the retained parameters, or that it is independent of their other full rows; those stronger claims have not been checked.

No computation, equation artifact, implementation revision, performance estimate, complete-system point/unit, all-r extension or higher-band result is reported. This gives one exact permitted simplification; it does not authorize implementing it or composing unreviewed prior bands. No new gauge or component localization has been introduced.

## 9. Completion and custody

The targets were absent and all three input hashes matched at the first action17:37:58UTC; the cap is17:49:58UTC, not reset. All three inputs were read WHOLE; their exact paths, bytes and current hashes accompany the owned packet. Only own metadata/publication tools and manual prose were used. No mathematical subprocess of ANY size, network, remote host, source/row emission, code edit, external agent, corpus/protected read, live gate or earlier-band report was used. Own WHOLE read and own-only raised-OPEN/collision check precede the sole completion marker. All writers are IDLE at terminal handoff.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only extraction; no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15437`.
- Body SHA-256:
  `964297c57043988378a3c08b09b994f986fac431ae1ea1328acd176b1847bd26`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
