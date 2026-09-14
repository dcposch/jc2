# Complete all-r F10 source: uniform cubic scale cover

2026-09-10. NEW MANUAL RESULT, UNREVIEWED. First action 09:09:30.169621309 UTC; controlling stop 09:21:30.169621309 UTC, reserve 09:19:30.169621309 UTC. Accepted16r/17zz/17zzd only; ROOT proposed the shared mechanism. No r2 or new ell theorem is a premise.

## 1. Leading quotient and exact source variables

Fix r≥2, m=3r+1, n=5r+2, q=2r+1. Start with the literal COMPLETE gauge-fixed 16r ring: A=St³+(Sd-u)t²+(1-ud+Sv)t+k, k(0)=0; B5=S²; all B coefficients reconstructed by (16r.5), with [S]B3=B0(0)=0. Retain every coefficient of E1,E0 and omega*ab-1, a=[S^m]k, b=[S^n]B0. Hereafter A_r denotes this coefficient ring, not the ungauged space of output pairs.

The top ordinary S/t-weight pieces, with wt(S,t)=(1,r), are S^m C(t/S^r), S^n D(t/S^r). Their equation is

    mCD'-nC'D=-theta^7, C=theta³+Ftheta²+Htheta+a.

Indeed the leading upper coefficients in the five Euler inversions have pivots mj-3n, j=4,...,0, all nonzero. They determine the five lower D coefficients from F,H,a. The remaining two leading coefficients are EXACTLY E1[S^(6r+2)] and E0[S^(7r+2)]. No lower variable enters them. Thus their quotient, with ab inverted, is the accepted whole leading ring

    L=B_nu[s,s^-1], nu=n/m,
    B_nu=Q[V,W,(Wt5)^-1]/(t6(nu),t7(nu)),
    c(zeta)=1+zeta+V*zeta²+W*zeta³,
    t_i(X)=[zeta^i]c(zeta)^X,
    s=H/a, a=1/(Ws³), H=1/(Ws²), F=V/(Ws),
    b=1/(t5*s5).                                      (1)

The accepted two-sided normalization includes ab*W*t5*s8=1. The accepted septic description makes B_nu the whole finite-etale rank-seven algebra; it is NOT assumed a field. No middle-contact equation is imposed. Lower coefficients remain independent over L at this stage.

## 2. Full-mate normalization and homogeneity

Set vartheta=s*t and

    Ahat=s³ A(S,vartheta/s), Bhat=s5 B(S,vartheta/s),
    Dpar=s*d, Vpar=s²*v, Kpar=s³*k,
    U=s*u, E=s³*ell, z=s².

The leading coefficients of Dpar,Vpar,Kpar are V/W,1/W,1/W, respectively, in B_nu. Collect their lower coefficients d_i (0≤i<r), v_i (0≤i<2r), k_i (1≤i≤3r), together with U,E, as X_j: exactly 6r+2 variables. These d_i,v_i,k_i now denote NORMALIZED coefficients. The change is invertible because s is a unit.

Direct substitution gives

    Ahat=S*vartheta³+(S*Dpar-U)*vartheta²
         +(z-U*Dpar+S*Vpar)*vartheta+Kpar,
    Pihat=z*vartheta-U*vartheta²+S*vartheta³,
    [Ahat,Bhat]=s7+U*s5*vartheta
                  -E*vartheta*Pihat-vartheta*Pihat².    (2)

The derivative contributes s^-1, so the bracket factor is s7. Assign

    wt(d_i)=r-i, wt(v_i)=2r-i, wt(k_i)=m-i,
    wt(U)=r+1, wt(E)=m, wt(z)=q,
    wt(S)=1, wt(vartheta)=r.                           (3)

Then Ahat,Pihat have weight m and the upper target in (2) has weight 7r+2. In the descending Euler equation, the forcing of Bhat_j has weight n-rj. Every product term has that weight, including the complete mixed terms and the z,U,E target terms. Coefficientwise inversion by j-3i preserves it. The two missing eigenvalue slots are automatic polynomial identities by 16r, and their chosen zero gauges are homogeneous. Therefore the ENTIRE reconstructed Bhat has weight n and is polynomial in B_nu[X,z]. No extra s factor enters its upper reconstruction: the two nonhomogeneous targets occur only in vartheta^0,vartheta^1. Bounds remain deg_S Bhat_j≤n-rj and deg_S Ahat_j≤m-rj.

For precision concerning the auxiliary free z: the transformed automatic resonance identities initially hold at z=s². The substitution B_nu[X,z]→B_nu[X,s,s^-1], z↦s², is injective, even with nilpotents, by distinct Laurent monomials. Thus those identities also hold before this substitution; both zero-gauge Euler inversions genuinely define polynomials in B_nu[X,z].

This is a universal polynomial-identity argument, valid over arbitrary B_nu-algebras, including nilpotents. It uses no fieldwise cancellation or unproved new band elimination. All 16r boundary identities and gauges survive the invertible substitution; recovering originals uses s^(j-3),s^(j-5) on the respective jth coefficients. Explicit coefficient read-back is d=Dpar/s, v=Vpar/s², k=Kpar/s³, u=U/s and ell=E/s³, with leading values (1). The free-z intermediate is only an algebraic envelope; the source read-back always restores z=s².

## 3. Literal retained rows

Let K0_i,K1_i extract [S^i*vartheta^0],[S^i*vartheta^1] from

    [Ahat,Bhat]+E*vartheta*Pihat+vartheta*Pihat².

Their weights are 7r+2-i, 6r+2-i. The two top rows have already defined (1). Hence

    A_r ≅ B_nu[s,s^-1,X]/
      (K1_i:1≤i≤6r+1; K0_i:1≤i≤7r+1;
       K1_0-U*s5; K0_0-s7), z=s².                    (4)

There are 13r+2 positive-index slots and two low slots. Original E1 rows differ by the unit s6 and E0 rows by s7. Every original residual, guard and particular forcing is retained through (1),(4); no contact coefficient is inverted. The source guard is omega=W*t5*s8. The ring assertion concerns the literal normalized 16r presentation; its accepted equivalence to original compact pairs remains at the explicitly stated field/gauge scope.

## 4. Two faithful covers and every low row

Adjoin w with w^q=s. This gives a free rank-q extension of (4), with basis 1,...,w^(q-1) and w^-1=w^(q-1)/s. For a_j=wt(X_j), set X_j=w^(2a_j)Y_j. A homogeneous weight-k row becomes w^(2k) times its slice at (Y,1). Put

    L0=K0_0(Y,1), L1=K1_0(Y,1), U0=U(Y,1),
    C_r=B_nu[Y,L0^-1]/
      (all 13r+2 positive-index slices, L1-U0*L0).     (5)

The low rows become exactly

    w^(14r+4)(L0-w³),
    w^(12r+4)(L1-U0*w³),                             (6)

since 7q-(14r+4)=3 and 5q+2(r+1)-(12r+4)=3. Replace the second parenthesis by L1-U0L0 by subtracting U0 times the first. L0=w³ is a unit. This proves

    A_r[w]/(w^q-s) ≅ C_r[w]/(w³-L0).                 (7)

Forward maps: s↦w^q, X_j↦w^(2a_j)Y_j, w↦w. Inverse maps: Y_j↦w^(-2a_j)X_j, L0^-1↦w^-3, w↦w. The right-hand inverse of w is w²/L0. The identity L1-U0*w³=(L1-U0L0)+U0(L0-w³) checks the second low row, not merely its leading part. All other rows differ only by displayed units.

The right-hand basis is 1,w,w². Both extensions are faithfully flat: tensoring any module gives respectively q or three copies of that module. Consequently A_r=0 iff C_r=0, even after nonreduced base change. The guards reconstruct as omega=W*t5*w^(8q). A field point of C_r lifts after an extension of degree at most three, and the converse uses degree at most q; no point is constructed. The cover degree is not a source-map degree. No assertion A_r≅C_r or source specialization s=1 is made.

## 5. Finite interface, controls and stop

C_r has 6r+2 variables over B_nu, one localization, and 13r+3 retained slots. Each positive-index row has the weight/degree bound in section 3. The last row is the z=1 slice of z*K1_0-U*K0_0, weight 8r+3, NOT 6r+2. A weight-k slice has the precise envelope

    product Y_j^e_j, sum a_j e_j≤k,
    k-sum a_j e_j in q*N.

The former z exponent is unique. L0 has degree bound 7r+2; adjoining J with J*L0-1 gives degree bound 7r+3 for that row. These are envelopes, not actual nonzero counts, heights, ranks or runtime predictions. The complete algebra decision is uncomputed.

Abstract changed-object controls: dropping L0^-1 retains L0=0, impossible with unit w and w³=L0 in a nonzero ring; setting w=1 adds the unlicensed equation L0=1; dropping the second low row leaves the independent residual L1-U0L0. These are algebra controls, not source points. Faithfulness follows from bases, not only field-valued root-taking. Unresolved middle or late contacts are irrelevant to this UNELIMINATED construction. Commutation with other band eliminations is unneeded and unproved here.

Verdict: the proposed uniform full-source scale cover is proved from the assigned accepted inputs, pending independent review of this new derivation. No source exclusion, global classification, parameter bound, computation or follow-on authority follows.

## OPEN(S) RAISED

None new. Exact remaining quantity: C_r=0 with every row in (5) and L0 inverted, for each r≥2. Cheapest prerequisite is full-B reconstruction/read-back of this finite presentation; coefficients, cost and outcome are unknown.

## COLLISIONS

status: EMPTY

Owned targets absent before lease; no shared/frozen scientific file changed. Own whole/read-scope/raised-OPEN review precedes completion.

Own WHOLE proof and documentary scope were read before sealing; the final free-z injectivity and coefficient read-back clarification was separately reread. All seven input hashes remain unchanged. Zero scientific execution; no dependent task remains.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8698`.
- Body SHA-256:
  `beab00a9fbf5254ba246e84b7590ae7a48acc445fdfec467e091ac56fcb060fc`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
