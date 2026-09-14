# All-r affine endpoint: exact last-target column, no closing obstruction

Owner: model_productivity / Astra. Status: **NO_CLOSING_OBSTRUCTION**. The identities below are a new manual measurement from the charged accepted equations, not a promoted exclusion. No mathematical computation or source execution occurred.

First action 2026-09-09T23:52:29.617226289Z; both owned targets absent. Controlling stop 2026-09-10T00:12:00Z; final three minutes reserved for publication. Exactly the thirteen objects in owned PINS.json were charged, beginning with the root NEXT-AFFINE-PINS manifest. Current hashes matched before the reads/reuse recorded in READ-SCOPE.md. No other scientific input or provenance was read.

## 1. Result and exact stopping point

There is an honest last-target affine parameter: **ell**. The complete reconstructed mate, and hence every remaining residual coefficient, is affine in ell over the algebra of the A coefficients. This remains true after the accepted early, middle and critical band maps and after retaining all late-band equations. It does NOT mean that all remaining A/kernel coordinates form a solved linear system.

The genuinely terminal retained row selected here is

    E0_res(0)=k1*B1(0)-(1-u*d0)*B0'(0)-1.                 (1)

It is never one of the positive-S rows consumed by the charged band maps. Its ell coefficient is exactly

    L0=-u*k1-(1-u*d0)*(v0/3-7*u*d1/15).                  (2)

The paired terminal E1 row has coefficient

    L1=u*(-v0/3+u*d1/15).                                (3)

All symbols in these formulas mean their **full substituted values** after any accepted band maps, with every compatibility and every remaining k coordinate retained. In particular they are not independent free scalars merely because a short formula uses them.

For these two equations the elementary annihilator (L1,-L0) gives a definite candidate obstruction, but its target value is a multiple of u. No proof that u, or that candidate value, is a unit in the actual guarded earlier quotient is supplied by the charged results or by this derivation. The u=0 boundary instead has a consistent rational pivot for the two constant equations before the other equations are imposed. This blocks this particular shortcut; it neither proves that the boundary survives the full system nor rules out a different, genuinely global annihilator.

## 2. Accepted presentation and the coefficient base

For every integer r>=1, m=3r+1 and n=5r+2, use the accepted normalized presentation

    A=S*t^3+f*t^2+h*t+k,
    f=S*d-u,  h=1-u*d+S*v,  k(0)=0,
    deg d<=r, deg v<=2r, deg k<=m,
    B=sum_(j=0)^5 B_j*t^j, B5=S^2,
    Pi=t-u*t^2+S*t^3,
    [A,B]=1+u*t-ell*t*Pi-t*Pi^2.

The beta and gamma mate gauges are [S]B3=0 and B0(0)=0. The top-product guard is omega*a*b=1, with a=k_m and b=[S^n]B0; neither top is normalized again. The Euler recursion is exactly 16r (5), with E_j=j-3*S*d/dS. The two full residuals are exactly

    R1=2k'*B2+h'*B1-h*B1'-2f*B0'-u,
    R0=k'*B1-h*B0'-1.                                    (4)

Start over the universal rational coefficient algebra with those envelopes and gauges. All identities below are polynomial identities there and therefore survive arbitrary quotients, including nonreduced algebras. Guard localization is retained throughout.

Let Gamma denote the actual charged triangular maps through the early, modified-u, middle and critical steps, whenever those maps are used. Keep all their introduced coordinates and compatibility equations. In a late step, 17v identifies the column ideal with a paired-contact ideal; it does not itself give a solved source compatibility. Thus no late k_j is silently removed. A proved unimodular-column elimination, if available at a particular qualified scope, must retain its companion compatibility as well. No such extra elimination is needed here.

For a precise relative affine presentation, let Qprev be the resulting guarded coefficient algebra, further quotiented by every still-retained coefficient of R1 above S^(3r+1) and R0 above S^(4r+1). These equations are ell-independent by section 3. Equivalently one can retain the original A coefficients and every high row rather than change coordinates at all. This defines an actual quotient; it does not assume its properness, finiteness, reducedness, or that any kernel coordinates are algebraically independent.

Over Qprev the remaining full system is the polynomial algebra Qprev[ell] modulo **all** the remaining coefficients of R1 and R0. This is a one-column relative affine problem over a possibly complicated earlier algebra. It is not an all-r reduction to a field, to a finite algebra, or to one genuinely independent variable over Q.

## 3. The entire ell column, including both boundary conditions

Differentiate the accepted Euler reconstruction formally with respect to ell, holding every A coefficient and u fixed. This is coefficient differentiation, not a source specialization. Write dot B_j for the resulting coefficients. The upper recursion gives

    dot B5=dot B4=dot B3=0,
    dot B2=S,
    dot B1=-u+S*J,
    J=sum_(i=0)^r (2i/(3i+2))*d_i*S^i,  J(0)=0.          (5)

Indeed E2(dot B2)=-S and E1(dot B1)=u-2S*f'+2f=-u-2S^2*d'. Both inversions use only fixed nonzero rational numbers. The zero beta gauge prevents an additional S term in dot B3.

Set G=dot B0, with G(0)=0. It is determined exactly by

    -3S*G'=-1-f'*(-u+S*J)+2f*(S*J)'-2S*h'+h.            (6)

The right side has zero constant coefficient: -1+u*d0+h(0)=0 and J(0)=0. Thus (6) has a unique polynomial solution with the stated gauge, using the same nonresonant Euler inverse. It has degree at most 2r+1. This includes u=0; there is no division by u, S as a parameter, or a coefficient of d or v.

The original recurrence is linear in the mate and the target is affine in ell. Successively subtracting its ell=0 solution proves the **entire** identity

    B_j=B_j^0+ell*dot B_j,                                (7)

not just its first-order or dual-number version. Both complete inverse-polynomiality conditions continue to hold because these are the actual accepted reconstruction coefficients. Since deg G<=2r+1<n, b=[S^n]B0 is ell-independent; the guard is therefore genuinely a guard in the coefficient base.

Substitution in (4) gives R_i=R_i^0+ell*L_i(S), where

    L0(S)=k'*(-u+S*J)-h*G',
    L1(S)=2S*k'+h'*(-u+S*J)-h*(S*J)'-2f*G'.              (8)

The bounds are deg L0<=4r+1 and deg L1<=3r+1. Consequently every higher residual row is ell-independent. The accepted early/middle/critical rows lie strictly above these respective bounds. The late rows for k_j, 1<=j<=r-1, are at E1/S^(3r+1+j) and E0/S^(4r+1+j), also strictly above them. Thus their actual mixed forcing and their exact quotient maps have no ell dependence. This justifies section 2 without guessing that a map is homogeneous after a specialization.

The first ell target has weight 4r+1, from -ell*S*t^4. No pending low-band theorem, r1 slice, or univariate model is used here. The corrected critical coefficient uses D_i, not D_(i+1); replacing the actual earlier mates by their homogeneous pieces is not part of Gamma.

## 4. An exact finite read-back of the terminal rows

There is no need to suppress the dependence on earlier parameters behind a leading term. Write f_i=[S^i]f, h_i=[S^i]h, k_i=[S^i]k and b_(j,i)=[S^i]B_j. The following small **manual specification**, not an emitted coefficient artifact, recovers the exact terminal jets from the whole Euler recurrence:

    (j-3i)b_(j,i)=delta_(j+2,i)
      +sum_(p+q=i+1) (2q-(j+1)p)*f_p*b_(j+1,q)
      +sum_(p+q=i+1) (q-(j+2)p)*h_p*b_(j+2,q)
      -(j+3)*sum_(p+q=i+1) p*k_p*b_(j+3,q).              (9)

Here B5=S^2, B6=B7=0, and delta is the ENTIRE accepted target list. Descend j=4,3,2,1,0, retaining 0<=i<=j+1, with b_(3,1)=b_(0,0)=0 and the two automatic resonance identities respected. To recover a coefficient at a given step, the next polynomial is needed only one degree higher; that coefficient lies inside the next retained range. The additional shifts by two or three in j only enlarge that available range. B4(0)=0 and B5=S^2 are used, not guessed vanishing of a free coefficient.

This read-back needs only d0,...,d3, v0,...,v2, k1,k2, u and ell; indices beyond the original envelope are zero. For example h3=v2-u*d3 and f4=d3 can reach b_(0,1) through the descending recursion. Thus no unwarranted independence from v2 or higher low jets is asserted. The earlier band substitutions for these entries may themselves depend on the full earlier parameter set and its mixed forcing; substitute those exact values into (9).

In this notation the two selected terminal equations are literally

    R0(0)=k1*b_(1,0)-h0*b_(0,1)-1,
    R1(0)=2k1*b_(2,0)+h1*b_(1,0)
             -h0*b_(1,1)-2f0*b_(0,1)-u.                 (10)

They are retained with every other coefficient of (4). Formula (9) is an exact dependence specification, not a claim that only leading ODE variables enter (10).

For the explicit ell coefficients, (6) at S gives

    G'(0)=v0/3-7u*d1/15.                                 (11)

For clarity, J_1=2d1/5; the S coefficient on the right of (6) is 3u*d1-4u*J_1-v0=(7/5)u*d1-v0. Applying -1/3 proves (11). Since (S*J)'(0)=0, (8) now gives exactly (2) and (3). These signs use the original bracket orientation, the -ell target at t^2, and the -2f'B2 term in the j=1 Euler equation.

## 5. The annihilator test and the unsolved unit question

Let a_i=R_i^0(0), i=0,1, considered as elements of Qprev via the exact read-back. Then the selected two-row system has the named affine form

    L*ell=bvec,
    L=(L0,L1)^T,  bvec=(-a0,-a1)^T.                      (12)

The explicit row sigma=(L1,-L0) satisfies sigma*L=0 over any commutative algebra. Its target is

    Dterm=sigma*bvec=L0*a1-L1*a0.                        (13)

If Dterm were proved a unit in Qprev, these two retained rows alone would contradict the full system. No pointwise or generic nonvanishing would suffice.

There is a concrete obstruction to claiming this unit without further proof. Universally R1(0) is divisible by u. This follows directly at u=0: f(0)=0, h(0)=1, B2(0)=0, B1(0)=-1 and B1'(0)=-v0, so (10) gives R1(0)=0 identically. The same applies at ell=0; hence a1 is a multiple of u. Equation (3) shows that L1 is also a multiple of u. Thus

    Dterm is in the ideal (u) in the universal algebra
    and in every Qprev obtained by the accepted maps.    (14)

In particular a unit proof for this Dterm would also prove that u is a unit in Qprev. The charged leading guard ab does not itself state that, and the qualified contact progress does not supply such a conclusion. Conversely (14) is NOT a proof that Dterm is nonunit in the actual quotient: its u=0 stratum may be killed by earlier retained equations. No existence of that stratum is asserted.

The full residual vector has the exact one-column L specified by (8), not just these two entries. An annihilator using other rows could behave differently. No complete syzygy module, unit certificate or all-row obstruction is derived here. The first unsolved issue is precisely the forcing values and their unit ideal in Qprev, with its actual earlier compatibilities. It is not the homogeneous contact column again.

## 6. Changed-object and boundary controls

At u=0 the exact small read-back gives

    B2[S]=ell-d0,
    B2[S^2]=5k1/4-9d1/10,
    B1(0)=-1, B1[S]=-v0,
    B0[S]=-d1/15-5k1/6+ell*v0/3.

For example the j=2/S^2 forcing is 3e1-5k1, with e1=6d1/5 and Euler eigenvalue -4; the j=0/S forcing then is d1/5+5k1/2-ell*v0, with eigenvalue -3. All d0*v0 terms cancel between the displayed full recurrence terms. Therefore

    R1(0)=0,
    R0(0)=-k1/6+d1/15-ell*v0/3-1.                        (15)

The two constant equations alone allow the fixed rational pivot

    k1=2d1/5-2ell*v0-6.                                 (16)

This is a control on the raw terminal equations, not a new complete-system elimination. After earlier band maps k1 need not be free: for r=1 it is already a critical coordinate, and in other cases it is subject to the retained late equations. Neither (16) nor u=0 is imposed on the actual system. These formulas demonstrate why a terminal constant target does not by itself produce a contradiction and why dividing u would discard a genuine algebraic stratum before proving it empty.

Changing only ell while using the ell=0 mate would omit exactly ell*L_i(S). At u=0 it misses -ell*v0/3 in R0(0). Thus a fixed-mate or leading-only calculation cannot substitute for (7)-(10). The error of replacing the j=1 coefficient -2f'B2 by -3f'B2 would already change (5) and fail its zero-constant resonance; this is an index control, not a computed test.

The accepted 16r section 8 family supplies the separate guarded-upper-row control R0(0)=-1. It obeys the complete Euler reconstruction, both boundary conditions and the top guard, but does not establish a point of Qprev with all high residual rows. It proves the terminal row is not an automatic identity of reconstruction; it must not be misreported as a counterexample satisfying the earlier band compatibility equations.

No real/complex positivity, field factorization, reducedness, or denominator-dependent branch was used in the new identities. A product such as u*Dtilde cannot be discarded over a ring with nilpotents or over an unproved u=0 stratum. The diagonal Euler divisions in (5),(6),(9) are rational units and are the only new divisions.

## 7. Decision, exact remaining quantity and scope

Decision: **NO_CLOSING_OBSTRUCTION**. The measured terminal row and its full ell dependence are exact, and (8) supplies the whole affine column over the actual retained coefficient base. The two-row candidate annihilator (13) has no proved unit target. Its factor u identifies a concrete necessary extra unit claim for that candidate; no claim that every possible annihilator shares this factor is made.

No earlier relation has been deleted, no parameter normalized, and no all-r late system declared solved. The remaining nonlinear/parameter-dependent object is the earlier quotient Qprev together with the forcing a0,a1 of (9)-(10), and ultimately every other coefficient of (4). The short ell formulas do not erase that dependence. A successful next use of this approach would have to exhibit a literal sigma for the full column with sigma*b a unit in that quotient, or prove such an obstruction using an exact retained-row combination. Homogeneous column regularity alone is insufficient.

Smallest measured candidate: Dterm of (13), with (14) mandatory. Cheapest documentary/manual discriminator would be an actual guarded-base unit identity for Dterm, necessarily including a proof that u is a unit there, or an explicit reason to use a different retained-row annihilator. Cost is unknown; no coefficient construction, ideal solve, runtime estimate or new task is authorized. This is the existing selected affine-endpoint question, not a newly opened campaign mechanism.

OPEN(S) RAISED: none. No new canonical OPEN ID, source point, properness/unit verdict, all-r F10 exclusion, JC2 result, solver license, or dependent task is produced. The formulas remain unreviewed if a future consumer wishes to charge them; a limitation report alone requests no review farm.

COLLISIONS: EMPTY (own-only check; no corpus search). Publication checklist: whole own body read before the sole completion marker; exact current source pins and owned metadata retained; no placeholders or earlier temporary formula retained; all writers idle at terminal custody handoff.

Own whole-read completed 2026-09-10 at 00:03Z, using the full body and overlapping final-section read. The owned raised-OPEN check found only the explicit none declaration; the final target remained absent. All thirteen source hashes matched again before completion. No mathematical subprocess was run. Terminal publication/custody occurs before the unchanged 00:12Z stop.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16000`.
- Body SHA-256:
  `93ad0c5be0abd329351d8fd85aa3265ba4ef9a3064bcd3fb342cf7b4be4cda30`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
