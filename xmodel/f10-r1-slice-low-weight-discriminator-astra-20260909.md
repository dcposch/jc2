# F10 r1: a unit low-weight coefficient and a faithful univariate interface

2026-09-09. NEW/PROVISIONAL conditional child of the frozen weighted-composition theorem, whose independent gate remains unread. First action18:29:54UTC; controlling stop18:41:54UTC. ZERO mathematical subprocesses of any size. Basis0d39df3c9fd69c939a8420c54d03228b9077777d is provenance only.

## 1. Exact result and dependency boundary

Conditional on the frozen weighted-composition theorem at its stated complete-source scope, the weight-three compatibility has a PROVED UNIT coefficient on z. This licenses an x-unit chart globally on the guarded full system; the x=0 locus is proved empty, not discarded. It gives an exact univariate presentation over the FULL accepted leading algebra B, with nine polynomial equations of degrees at most5 and a guard polynomial of degree at most5. No division by the coefficient of xy, no factor choice, and no exception branch is lost.

The complete four-band algebra is recovered by an explicit monic cubic cover of this univariate algebra. A univariate field point therefore reconstructs a full point after a field extension of degree at most3; a full point maps to the univariate coordinate over the SAME field. The cover is a parameter-space cover, not a claim that the source Keller map has degree3.

No coefficient arrays, matrices, equations or source artifacts were emitted or computed. All finite formulas below are mathematical prescriptions using the accepted recurrences. No point, unitness/properness of the remaining ideal, nonzero equation, finite solution count, runtime or implementation claim follows.

Only the frozen composition report SHA d91b3e389aee3c1086737b58da9747408cc7a04a8e9bb22161c26f2ddda8147c and its eleven named accepted inputs were used. All twelve current hashes were checked before reuse; the eleven accepted inputs had been read WHOLE in the preceding task, and the composition report was read WHOLE here. No live gate, new source, ledger, code or peer was read. PINS.json records the exact current inputs. This is one provisional dependency generation, not acceptance of the parent by assertion.

## 2. Normalization and finite formulas for all seven coefficients

Use the parent's normalized variables x,y,z of weights1,2,3 and the full coefficient ring B=Q[v]/p(v), with all its accepted unit data retained. Write the leading polynomials as

    C(theta)=theta^3+F theta^2+H theta+a0,
    D(theta)=sum_(i=0)^5 D_i theta^i,
    F=v/w, H=a0=1/w, D5=1, D0=b0=1/f5,
    4CD'-7C'D=-theta^7.                       (1)

All these are identities in B; no residue field is selected. This notation separates a0,b0 from the compatibility coefficients a,b below. The third compatibility uses precisely the CORRECTED coefficient rule from the accepted gate, not the shifted-index formula in its producer.

Weight alone gives exactly

    Phi3=a*x^3+b*x*y+c*z,
    Phi4=d*x^4+e*x^2*y+f*y^2+g*x*z,           (2)

with a,...,g in B. Coefficients may vanish, except c is proved a unit in section3. Here are finite exact formulas determining them without any high-source expansion.

Define a polynomial evaluation functional F3(X,Y,Z), over B, by this fixed sequence:

1. Form the first-band vector beta^(1)*X and its entire mate band J by the accepted first-band recurrence, normalized using(1).
2. Form W2=3Z1*J'-6Z1'*J, where Z1 is that first A band. Use the accepted second-band completed matrix N2 and its actual forcing c2(Z1) to obtain (q,l,k2)=N2^-1*(-c2,1,-c2,0,Y). Set U=-q, Vcal0=l-Fq, and form the entire second mate band K by its five upper steps. All first-band and second-band kernels here are the normalized parent maps; neither a free J nor a free K is substituted.
3. Put A2=q theta^2+l theta+k2, y0=Z-U*Dcal0, and W3=3Z1*K'-5Z1'*K+2A2*J'-6A2'*J. Define

       N=-2Z theta^5-W3-y0(theta D'-7D),
       N_i=-W3_i+(7-i)y0 D_i, i=0,...,4.     (3)

   The theta^5 coefficient cancels exactly. At k1=0 compute

       V2=-N4/4, V1=-N3/8,
       V0=(-4F V1+4H V2-N2)/12,
       r1=8a0 V2-8F V0-N1,
       r0=4a0 V1-4H V0-N0.                  (4)

   Here N2 in(4) is the theta^2 COEFFICIENT of N, not the completed matrix of step2.
4. With the accepted third-band column and left inverse, write

       zeta=(-2F D4+5H+3D3)/12,
       chi1=10a0-8F*zeta+2D2,
       chi0=2a0 D4-4H*zeta+D1,
       lambda1*chi1+lambda0*chi0=1.

   Set F3(X,Y,Z)=chi1*r0-chi0*r1. The third back-map is Kcal1=-lambda1*r1-lambda0*r0.

Define F4(X,Y,Z) by first taking exactly that Kcal1 back-map and then the full normalized upper mate recurrence at E=0, with Ahat and Pihat as in the parent. The upper target is -tau*Pihat^2. Form its entire two residuals at [S^4 tau] and [S^5], call them P,Q. If Acol,Bcol are the accepted normalized fourth-band column, set

    F4(X,Y,Z)=Bcol*P-Acol*Q.                 (5)

Thus all intervening and lower coefficients are included; P,Q are not leading-ODE substitutes. These definitions use finitely many coefficient projections and the exact fixed Euler inverses already stated in the charged reports. No new map, algorithm or equation artifact is introduced.

The seven desired coefficients are now explicitly

    a=F3(1,0,0),
    b=F3(1,1,0)-F3(1,0,0),
    c=F3(0,0,1),
    d=F4(1,0,0), f=F4(0,1,0),
    e=F4(1,1,0)-F4(1,0,0)-F4(0,1,0),
    g=F4(1,0,1)-F4(1,0,0).                  (6)

These follow from the exhaustive monomial lists(2), so they are exact finite recurrence formulas rather than numerical interpolation assumptions. The evaluations at Z=0 are polynomial coefficient prescriptions, NOT guarded source points or a claim that the parent permits z=0. Their actual values are not executed here. No unit assertion about a,b,d,e,f,g is made.

For a more literal checkpoint on c, let

    M=2F D3-3H D4-5D2,
    r1,z=-6a0 D4-(2F/3)M-6D1,
    r0,z=-2a0 D3-(H/3)M-7b0.

Then the specialization in(3),(4) gives exactly

    c=chi1*r0,z-chi0*r1,z.                  (7)

Indeed at x=y=0, N4=3zD4,N3=4zD3,N2=5zD2,N1=6zD1,N0=7zb0. Formula(7) retains the corrected indices and signs.

## 3. The coefficient c is a unit: exact theta-seven obstruction

At x=y=0 both earlier A bands vanish by their exact normalized back-maps: the first is linear in x and the second is quadratic in x plus beta^(2)y. Thus the third A band is Y=z theta+k, where k=Kcal1, and the mate variation has degree at most2. Its ENTIRE third-band equation, before the two residuals are imposed, is

    4CV'-4C'V+YD'-7Y'D=-2z theta^5+r,
    r=r1 theta+r0.                           (8)

The accepted upper recurrence fixes V and leaves only these two residual coefficients. Set

    T=4CV-7DY, deg T<=6.

Differentiate(8) and use(1). Direct cancellation yields

    T'=8(C'V-D'Y)-2z theta^5+r,
    CT'-2C'T=2theta^7Y-2z C theta^5+C r.     (9)

No bracket term or shift is suppressed. Divide by the formal unit C^3. Then

    (T/C^2)'=2theta^7Y/C^3
                         -2z theta^5/C^2+r/C^2.

Formal integration has zero chosen constant for the last two terms. The first displayed term contributes only degrees>=8 after integration, including when k is nonzero. The constant of integration times C^2 has degree6. Since T has degree<=6, its theta^7 coefficient is zero, and hence

    0=-2z*[theta^7]C^2*int(theta^5/C^2)
                             +[theta^7]C^2*int(r/C^2). (10)

Every integral here denotes a finite formal coefficient calculation with rational denominators; no analytic function is used. Only the accepted units a0,H are divided below.

The load-bearing coefficient in the first term is elementary:

    C^-2=a0^-2-2H*a0^-3*theta+O(theta^2),
    [theta^7]C^2*int(theta^5/C^2)
       =a0^2*(-2H*a0^-3)/7
                    +(2a0 H)*a0^-2/6
       =H/(21a0).                            (11)

Thus(10) is the exact identity

    z=(21a0/(2H))*[theta^7]C^2*int(r/C^2).    (12)

The normalized H=a0=1/w is a unit on ALL B. No generic root argument or factor test is needed.

After the third-band k back-map, its determinant-one residual transformation gives

    (r1,r0)=(-lambda0,lambda1)*Phi3.

At this specialization Phi3=c*z. Therefore the explicitly defined element

    gamma=(21a0/(2H))*[theta^7]C^2*
                  int((-lambda0*theta+lambda1)/C^2)  (13)

satisfies c*gamma=1 in B. This follows by substituting into(12) and comparing the coefficient of the indeterminate z. It is a ring identity, not merely a nonzero value in each field. Formula(13) uses coefficients of C^-2 only through degree6, so it is a literal finite formula in the accepted leading units and the already-explicit third left inverse. No existential Bezout choice, matrix computation, field extension or positive-real assumption is hidden.

This proves c is a unit; it does NOT prove b is a unit. The latter is unnecessary for the reduction below and remains unassessed.

## 4. Faithful x-chart and exact univariate coefficient ring

Return to the complete normalized parent system BEFORE the z=1 slice. Its z is a unit, and Phi3=0 gives

    x*(a*x^2+b*y)=-c*z.

The right side is a unit, so x itself is a unit over every commutative coefficient algebra. Thus the x=0 chart is impossible on the guarded system, including over product rings. Define new coordinates

    t=y/x^2, r=z/x^3.

The variable t here is a PARAMETER, not the source t of16r or the homogeneous theta. To avoid any hidden normalization, x remains a variable until the final monic cubic equation. Then

    Phi3/x^3=a+b*t+c*r,
    r=r(t):=-(a+b*t)/c.                       (14)

No b division occurs. Since x,z are units, r is a unit; this condition will be retained explicitly. The fourth compatibility becomes the degree-at-most-two polynomial

    P4(t)=d+e*t+f*t^2+g*r(t).                (15)

Now use the parent's nine homogeneous G equations, with Phi3 one of them. For its seven original low rows of weights7,6,5;8,7,6,5 substitute

    G_w(x,y,z)=x^w*G_w(1,t,r(t)).

Retain all seven specialized polynomials, retain P4, and define

    h0(t)=H0(1,t,r(t)),
    h1(t)=H1(1,t,r(t)), ubar(t)=U(1,t,r(t)).

The remaining homogeneous target relation zH1-UH0 specializes to

    P11(t)=r(t)*h1(t)-ubar(t)*h0(t).          (16)

Set qguard(t)=r(t)*h0(t). The promised univariate algebra is

    Runi=B[t,qguard(t)^-1]/
       (the seven specialized low rows, P4, P11). (17)

There are nine equation slots, not a claim of nine independent/nonzero polynomials. Both factors r,h0 are units in(17). This retains all source rows and the unsquared-target information through the construction below. No branch is selected from B, no point is assumed, and no equation has been replaced solely by a resultant condition.

## 5. Exact cubic cover and whole-source back-map

The one nonhomogeneous parent equation H0^2=z^7 becomes

    x^18*h0^2=x^21*r^7,
    x^3=h0^2/r^7.                            (18)

Consequently the full four-band parameter algebra is recovered as

    Runi[x]/(x^3-h0^2/r^7).                  (19)

All divisions in this expression are by the guard units in(17). The monic cubic makes(19) free of rank3 over Runi and hence faithfully flat; x is automatically a unit because its cube is a unit. Its derivative3x^2 is also a unit, so it is a finite etale parameter cover. In particular Runi is the zero ring if and only if the complete covered ring is the zero ring: properness/unit equivalence is algebraic, not only a passage to algebraic-closure field points. These are purely ring-theoretic properties of the displayed monic equation, not a source-map degree claim or a nonemptiness assertion.

For an exact back-map from(19), put

    y=x^2*t, z=x^3*r,
    s=h0/r^3.                                (20)

Equation(18) gives z=h0^2/r^6=s^2. Further,

    H0(x,y,z)=x^9*h0=h0^7/r^21=s^7.

The equation P11=0 is precisely zH1=UH0 after multiplying by the unit x^11. Since z is a unit, H1=U*H0/z=U*s^5, so the original UNSQUARED target is recovered. All other homogeneous zero rows follow by their powers of the unit x. This recovers the parent's full11-slot normalized system, not only Phi3/Phi4.

Then use its exact maps Y1=x/s^8,Y2=y/s^8, all four band reconstructions, and

    u=U/s, d=Dcal/s, v=Vcal/s^2,
    k=Kcal/s^3, ell=E/s^3,
    A(S,t_source)=s^-3*Ahat(S,s*t_source),
    Bmate(S,t_source)=s^-5*Bhat(S,s*t_source).

The guard is omega=w*s^8*f5. Accepted16r then restores the original output leading factors and complete inverse-polynomiality conditions. Every literal residual follows by the preserved row maps; no lower equation is bypassed.

Conversely a full guarded point or coefficient-algebra solution gives x a unit by section4; take t=y/x^2,r=z/x^3. Formula(14) holds, and all nine rows in(17) follow from the full homogeneous rows. Since H0=s^7 is a unit, h0=H0/x^9 is a unit, so the guard holds. The remaining equation is(18). Thus these maps are inverses at the parameter-ring level CONDITIONAL on the parent's exact composition. In particular the cubic cover(19), not Runi by itself, is the ring-isomorphic complete presentation.

A Runi point over a characteristic-zero field K lifts after adjoining a root of(18), an extension of degree at most3. A full point gives t in the SAME field with no extension at all. Hence field existence over algebraic closures is exactly equivalent. Neither a rational point nor a field point of B alone is a full-source certificate. The actual accepted endpoint remains ordinary source degrees112/196 only if every guarded equation is satisfied; no maximal-degree or JC2 conclusion follows here.

## 6. Degree and artifact-envelope bounds, not measured speed

A monomial x^i y^j z^k of weight w obeys i+2j+3k=w. At(1,t,r(t)), where r is affine-linear, its degree in t is at most j+k<=floor(w/2). This proves the following exact envelopes without coefficient expansion:

- Seven low equations: degrees<=3,3,2,4,3,3,2.
- P4: degree<=2; P11: degree<=5.
- h0: degree<=4; h1: degree<=4; ubar: degree<=1.
- qguard=r*h0: degree<=5.

Thus the nine equation envelopes contain at most36 coefficients in B. The guard polynomial has at most6 coefficients in B. In the accepted rank-seven rational basis this is at most252 rational basis-monomial slots for the nine rows and42 for qguard; the literal polynomial guard xi*qguard-1 adds its separate constant term, so at most43 such slots for that row. These counts exclude a separate encoding of p(v)=0 if one chooses to represent B as an ordinary rational polynomial quotient. They say nothing about coefficient height, cancellations, nonzero-row counts or elapsed time.

For comparison, the parent's z=1 slice has at most73 B-monomial slots across its ten equations: for weight w the count is sum_(k=0)^floor(w/3)(floor((w-3k)/2)+1). The nine G weights give57 and the weight11 relation gives16. The degree9 h0 has at most12 such slots. This is an a priori envelope, not a measured artifact. The direct x-chart avoids needing a unit coefficient of xy and gives a smaller univariate decision object.

No positive finite-degree assertion about the full algebra follows just from these bounds. On a field factor of B, all nine polynomials could conceivably be zero; then the guarded locus may be an open line. If one is nonzero, its degree is at most5, but which factors or equations have that property is not established. The full product algebra, zero polynomials, degree drops and guard-zero loci must all remain in a future exact decision.

## 7. Changed-object controls and decision boundary

The c-unit proof uses the ACTUAL normalized target -2z theta^5. Replacing it by zero removes the -2zH/(21a0) term from(10); no z-unit conclusion is then obtained. Replacing the corrected N_i by the producer's shifted D_(i+1) formula similarly changes the particular residual and invalidates(7). The accepted homogeneous left inverse alone cannot catch that forcing corruption.

The x-unit step uses BOTH c and z units. If c were left unproved, dividing x would drop a potentially nonempty x=0 stratum; equation(13) is the missing certificate that makes this safe. If the guard z were dropped, x=0,z=0 would satisfy Phi3 independently of y, so that altered presentation is not covered by the x-chart. This is a changed-hypothesis compatibility control, not a full-source point.

No b inversion is needed: (14) still makes sense when b=0 on a component. If r(t) vanishes on any component or at any root, the guard in(17) removes exactly the locus with z=0 after reconstruction, not an admissible full point. If h0 vanishes, the original nonzero target/scale cannot be reconstructed; that is why it is retained in the guard rather than canceled casually.

Keeping only P4 or a resultant of Phi3/Phi4 would not be a faithful decision: the seven low rows, P11 and guard are all required in(17). Dropping the cubic equation would also discard the exact relationship between target and scale. Every displayed change is reversible with those rows retained.

Cheapest meaningful next decision interface, not execution authority: compute the finite B coefficients of the nine degree<=5 polynomials and qguard by the exact recurrences, then perform an exact univariate ideal/guard test over the FULL B. Any componentwise method must retain every factor and all zero-polynomial cases. A proper guarded quotient gives a residue-field point and hence, via(19), a full point; a unit certificate must cover every factor and guard. No such coefficients, gcd, saturation, certificate or point were calculated. There is no b-unit claim, independence claim, solver-policy change or automatic follow-on.

## 8. Completion

Both targets were absent at18:29:54UTC and all twelve science hashes matched before reuse. Only the frozen composition and its eleven unchanged inputs were consumed; prior accepted whole reads were reused, and the composition was read WHOLE here. No live gate or new source was read. All new algebra is manual, with ZERO mathematical subprocesses of ANY size, code/data artifacts, network, remote host, process inspection, agent or shared/protected write. Only documentary metadata, apply_patch and existing transaction tools ran. Own WHOLE and own raised-OPEN/collision checks precede the marker. This new theorem stays PROVISIONAL under its explicit provisional parent; all writers IDLE before18:41:54UTC.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only extraction; no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18355`.
- Body SHA-256:
  `326372711573d0e05c69573b679c5657498f72ee5b8f73dd3b3c0fcb3ba737f6`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
