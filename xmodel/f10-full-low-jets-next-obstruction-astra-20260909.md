# F10 full low jets: exact compatibility and the limit of a second global pivot

2026-09-09. NEW/PROVISIONAL manual discriminator, not a source exclusion. Basis0d39df3c9fd69c939a8420c54d03228b9077777d is provenance only. First exact local check12:55:40 UTC; conservative stop13:10 UTC. ZERO mathematical subprocesses.

## 1. Decision

The proposed remaining Y coefficient is correct. It is not a fixed unit. A retained polynomial family shows that the constant residual, after the first pivot, is exactly u²/2 times the next S coefficient. Thus that apparent obstruction can be a genuine compatibility relation, rather than an inconsistency. On u=0 the next coefficient instead supplies a further rational-unit pivot for v1. Neither finding supplies an all-strata second elimination: its first missing arrow is a global polynomial row/coordinate completion retaining every residual, not a license to divide by u or by the other displayed factor.

Outcome for the requested NEW all-strata obstruction: NO GAIN within this bounded pass. The report proves precise low-row identities, a changed-object compatibility control, and the boundary pivot; it does not prove a universal symmetry of the full source or a no-go for every possible global completion. Separately, the already found first pivot extends to every r>=1 by the same low-jet argument. This is only a scope extension of that mechanism.

Only the four pinned reports in PINS.json were read as science. The Euler producer/gate and cubic module are accepted16r/16q. The own first-pivot report was charged PROVISIONALLY; no newly reported gate body was consumed. New calculations below are independently obtained from the accepted recurrence. All other source and ideal endpoints remain precisely those of16r.

## 2. Complete retained object and notation

For r>=1, m=3r+1,n=5r+2, use

    A=S t³+f t²+h t+k, B5=S²,
    f=S d-u, h=1-u d+S v, k(0)=0,
    deg d<=r, deg v<=2r, deg k<=m.

The entire mate is the accepted Euler reconstruction, with [S]B3=0 and B0(0)=0:

    (j-3S∂S)Bj=delta_(j+2)
      -(j+1)f'B_(j+1)+2fB'_(j+1)
      -(j+2)h'B_(j+2)+hB'_(j+2)
      -(j+3)k'B_(j+3), j=4,3,2,1,0,

    (delta0,...,delta7)
      =(1,u,-ell,ell*u-1,2u-ell*S,-u²-2S,2uS,-S²).

Every coefficient of

    E0=k'B1-hB0'-1,
    E1=2k'B2+h'B1-hB1'-2fB0'-u                  (1)

and omega*a*b-1 is retained, with a=k_m,b=[S^n]B0. The bounds are deg E0<=7r+2, deg E1<=6r+2. The inverse boundaries and all upper Jacobian coefficients are exactly those already proved by16r. No new independent Bj or residual coefficient is introduced. Write e0=E0(0), e1=E1(0), and e11=[S]E1.

For r=1, write d=d0+d1S and h=H0+H1S+v1S²+v2S³, where H0=1-u d0,H1=v0-u d1. For larger r, H2=v1-u d2 etc.; missing d_i mean zero. That distinction must be preserved in any wider inhomogeneous calculation.

## 3. First pivot and the exact remaining Y coefficient

Here are the low-jet facts needed to re-root the calculation in the accepted recurrence. For a change k -> k+q1S+q2S², B4,B3 do not change, and

    delta B2=(5/4)q1S²+(10/7)q2S³,
    delta(B1)_0=0,
    delta(B1)_1=-(3/2)u q1,
    delta(B1)_2=-(d0/10)q1-(52/35)u q2,
    delta B0'(0)=(-5/6+(6/5)u d0)q1+(2/105)u²q2.

These follow successively by eigenvalues -4,-7; -2,-5; and -3 in the displayed full recurrence. For example the j=0 S variation before its -3 division is d0*delta(B1)_1-4u*delta(B1)_2+2H0*delta(B2)_2-6u²q2. Terms starting k_j S^j,j>=3 cannot reach these entries. B2,B1,B0 are affine in k, so these are exact differences, not just tangent coefficients.

Also (B2)_0=-u²d0/2 and

    (B1)_0=-H0²-u ell+u²H1+(4/5)u³d1.

Consequently, with c0,c1 denoting evaluation at k1=k2=0,

    e0=Acoef*k1-(2/105)H0*u²*k2+c0,
    e1=Q*k1+(4/105)u³*k2+c1,
    Q=-u/6-u²d0/10,
    Acoef=-H0*(1/6+u d0/5)-u ell+u²v0-u³d1/5.

The elementary row R=e0-(d0/2)e1 is

    R=J k1+L k2+R0,
    L=-(2/105)u², R0=c0-(d0/2)c1,
    J=-1/6+u j1+u²j2,
    j1=d0/20-ell, j2=d0²/4+v0-u d1/5.          (2)

For completeness the polynomial inverse certificate is

    M=36j1²+6j2+36u j1j2,
    s=-6(1+6u j1), zeta=-(105/2)M,
    sJ+zeta L=1.

Set X=Jk1+Lk2, Y=-zeta*k1+s*k2. The inverse is k1=sX-LY,k2=zeta X+JY. Solving R=0 gives

    k1=-sR0-LY, k2=-zeta R0+JY.                (3)

There is no inversion of u,J,H0. Substitute (3) in EVERY remaining equation and the guard. The coefficient of Y in the remaining constant e1 is exactly

    -QL+(4/105)u³J
       =(2/105)u²(Q+2uJ)
       =(2/105)u³ W,
    W=-1/2-2ell*u+2u²j2.                       (4)

The middle simplification uses cancellation of the d0 term in 2j1-d0/10=-2ell. In the polynomial parameter ring (4) is not a unit; W also has parameter-dependent zero sets. The already required guard concerns a*b, not u or W. This calculation alone supplies no proof that the full ideal makes either factor invertible.

At u=0, the full recurrence gives e1=0 for all remaining parameters, so the polynomial e1 is divisible by u before and after the regular substitution (3). This is a boundary identity, not a proof of a full-source symmetry, and not an authorization to replace the equation by e1/u. Over arbitrary coefficient algebras that replacement also removes torsion/nilpotent possibilities unless separately justified. No such saturation identity is proved here.

## 4. Exact relation to the next row on a retained family

The following uses r=1 and an actual specialization of the accepted free input parameters, not a guessed mate or a commuting leading pair:

    d=ell=v0=0,
    h=1+H S²+V S³,
    k=k1S+k2S²+k3S³+aS4.                       (5)

Thus H=v1,V=v2 are free, u is unrestricted. Keep the entire Euler mate and every residual; the following individual entries suffice. Direct descent gives

    B4=-2uS,
    B3=u²+(4/3)H S³+(13/9)V S4,
    (B2)_0=(B2)_1=0,
    (B2)_2=(5/4)k1-(3/2)uH,
    (B2)_3=(10/7)k2-(94/63)uV,
    (B2)_4=(3/2)k3,
    (B1)_0=-1,
    (B1)_1=-(3/2)u k1,
    (B1)_2=-(52/35)u k2+(1/105)u²V-(4/5)H,
    (B1)_3=-(3/2)u k3-(13/18)V,
    (B0)_1=-(5/6)k1+(2/105)u²k2
                 +(4/315)u³V-uH/15,
    (B0)_2=-(5/7)k2+uV/42.                    (6)

Some checks exposing all relevant terms: the j=2 S² and S³ forcing coefficients are 6uH-5k1 and (94/9)uV-10k2. The j=1 S² forcing is (52/7)u k2-u²V/21+4H. The j=0 S forcing is (5/2)k1-(2/35)u²k2-(4/105)u³V+uH/5; its S² forcing is (30/7)k2-uV/7. Dividing by their respective Euler eigenvalues yields (6). In particular no derivative or k3 contribution is silently discarded; the k3 terms cancel in the last S² forcing.

Here R=e0, J=-1/6,L=-2u²/105,s=-6,zeta=0, and

    R0=-1+uH/15-(4/315)u³V,
    k1=6R0+(2/105)u²Y, k2=-Y/6.               (7)

From the ENTIRE formula (1), the next coefficient before the pivot is

    e11=-(2/5)H+(4/35)u k2+(8/105)u²V.

For example its terms are -2H-2(B1)_2+4u(B0)_2; the k'B2 term has S-order at least two on (5). The exact post-pivot identities are

    e1=-(u²/105)(21H+uY-4u²V),
    e11=-(2/105)(21H+uY-4u²V),
    e1=(u²/2)e11.                              (8)

Equivalently before the pivot e1-uR=(u²/2)e11 on (5). This is an exact polynomial identity over arbitrary Q-algebras, not a field-only cancellation. Thus the next row can absorb the displayed constant row, rather than contradict it. On this family alone it has a fixed coefficient -2/5 on H and solves H=(4u²V-uY)/21. Every other residual and the guard still have to vanish; no full point is thereby constructed. Specializing the parameters to this family is a CONTROL, not an all-strata replacement for the full client.

The boundary is not structurally removed by the upper equations and required top guard. For instance u=H=k2=k3=0,V=a=1,k1=-6 obeys R=0 and both rows in (8). The upper reconstruction has (B3)_4=13/9,(B2)_5=20/13 and

    b=((20/13)+12*(13/9))/21 !=0.

Hence a=1,omega=1/b retain the exact top-product guard. Other residual coefficients are not asserted zero. Changing H while retaining (7) changes e11 by -2/5 times that change; it is a genuine remaining equation, not an automatic vanishing. Setting u=0 makes e1 blind to this change. This is a changed-object control against dropping e11 merely because e1 has the factor u.

Formula (6) also settles a possible hidden-parameter mistake: at H=k=0, V remains in (B0)_1=(4/315)u³V. Therefore c0=R0=-1-(4/315)u³V and c1=-u+(8/315)u^4*V. They are NOT generally independent of v2. This does not affect the earlier pivot: its polynomial base ring always included v2. No new review assertion is used as a premise.

## 5. The full u=0 boundary has a second unit pivot, not a contradiction

Now keep all r=1 coefficients, but set u=0. A hand evaluation of the full recurrence gives

    (B2)_1=ell-d0, (B2)_2=(5/4)k1-(9/10)d1,
    (B1)_0=-1, (B1)_1=-v0,
    (B1)_2=-d0*k1/10+(2/5)ell*d1+v0²/5-(4/5)v1,
    (B0)_1=-(5/6)k1-d1/15+ell*v0/3.

The -d0*k1/10 coefficient includes the term -4k'B4 in the j=1 forcing; omitting it would incorrectly produce -d0*k1/2. This is a load-bearing sign/coefficient check.

The first row is e0=-k1/6+d1/15-ell*v0/3-1, hence

    k1=(2/5)d1-2ell*v0-6.

Before that substitution the next row is

    e11=(2ell-2d0/15)k1-(2/5)v1
       -(4/5)ell*d1-(2/5)v0²
       +(2/15)d0*d1-(2/3)d0*ell*v0.

Thus it has the fixed unit coefficient -2/5 on v1. After the first pivot it solves exactly

    v1=-v0²-10ell²*v0-30ell
                  +(d0*d1)/5-d0*ell*v0+2d0.         (9)

On the quotient by u=0 this is an honest polynomial coordinate elimination, with a complete back-map obtained by these two displayed substitutions in EVERY other row and the guard. It is not a global extra gauge or a proof that a full point lies on u=0. Setting d0=d1=ell=v0=0 reduces (9) to H=0, as (8) requires. Changing v1 by one changes e11 by -2/5. In contrast e1 remains zero identically there. This verifies the distinction between the two low rows by a literal changed coefficient.

## 6. Uniform-r extent of the original pivot

The exact differences and the constant entries used in section3 depend only on f0=-u,f1=d0,f2=d1,H0=1-u d0,H1=v0-u d1. They do not use the upper degree r=1 cut. For all r>=1, changing k1,k2 leaves these input jets unchanged; the same Euler eigenvalues and the same displayed variation proof apply. All higher d_i,v_i,k_i belong to the polynomial base ring and are retained in c0,c1,R0 whenever they actually enter. In particular this extension does NOT assert that the inhomogeneous low constants ignore v2 or other permitted jets.

Consequently (2)–(3) prove the same determinant-one first elimination for the COMPLETE L_r for every r>=1. The exact resulting presentation has 6r+5 variables and at most13r+6 coefficient slots: replace e0 by R, perform the invertible coordinate change, solve X+R0, and substitute in every other residual and omega*a*b-1. These are envelope counts, not emitted counts or dimensions. The inverse maps are the explicit polynomial maps in section3. This is a quotient-ring isomorphism over arbitrary Q-algebras; subsequent source interpretation retains the accepted field-point scope. It is a scope extension of the existing pivot, not a new obstruction, new symmetry, normalization or measured acceleration.

## 7. Precise stopping boundary

No all-strata second coordinate-one row has been proved. The missing arrow is a polynomial completion for the FULL remaining equations that handles u=0 and W=0 without inverting them. The family identity (8) and boundary pivot (9) show why a nonzero-looking factor in the constant row is not already such a proof. They do not establish a universal row identity e1=(u²/2)e11 for arbitrary d,ell,v0, nor a full-source symmetry, nor a universal impossibility of another completion. Nor is it proved that u is a unit modulo the full guarded ideal. Cancelling it would require that missing assertion, including its algebra-level scope.

Every complete residual and inverse condition remains. There is no newly constructed field point, properness/unit decision, full F10 or JC2 exclusion, builder modification, coefficient stream, runtime claim, branch farm, or follow-on authority. This is one bounded discriminator, ending with NO GAIN on a new global obstruction and the exact positive/control results above. All calculations were manual and independent of live reports. Own whole and own-only raised-OPEN checks precede the marker; final custody verifies all four unchanged input pins and all writers idle.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN extraction; no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12593`.
- Body SHA-256:
  `22b68b1b554735f5da1a7054eecbb607df043de71db2ee8918047c55c151ccae`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
