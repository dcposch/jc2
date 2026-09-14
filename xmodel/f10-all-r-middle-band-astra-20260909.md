# All-r middle bands: exact one-row compatibility with the H7 locus retained

2026-09-09. NEW MANUAL PRESENTATION, UNREVIEWED. First action20:04:04.312446UTC; controlling stop20:19:04.312446UTC. Exactly accepted16r and accepted17q early-tower producer/gate are inputs. ZERO mathematical subprocesses or source coefficients evaluated/emitted. No full-source exclusion, computation or later-band claim.

## 1. Setting and precise result

Fix r>=2 and a gap

    r+2<=h<=2r,
    m=3r+1, n=5r+2, kappa=m+n-h, alpha=kappa/m.      (1)

For r=1 this interval is empty. Use the complete16r normalization

    A=S t^3+(Sd-u)t^2+(1-u d+Sv)t+k,
    deg d<=r, deg v<=2r, deg k<=m, k(0)=0,
    B5=S^2, [S]B3=B0(0)=0,
    Delta=1+ut-ell*t*Pi-t*Pi^2,
    Pi=t-ut^2+St^3.                                 (2)

The whole B is the accepted Euler reconstruction. Its two remaining polynomials are E1_res,E0_res, with EVERY coefficient and the original top-product guard retained unless explicitly replaced below. The leading algebra L has

    C(theta)=theta^3+Ftheta^2+Htheta+a,
    D(theta)=sum_(j=0)^5 D_j theta^j, D5=1,D0=b,
    mCD'-nC'D=-theta^7, a*b a unit.                  (3)

Here theta=t/S^r, F=d_r,H=v_(2r),a=k_m. L can be the full universal guarded Q-algebra defined by(3), or any algebra over it, with nilpotents allowed. No existence, reducedness, finite-dimensionality or selected leading-field factor is presumed. The final gate attribution of all-r nonemptiness to17a/17b is not a premise of this report.

RESULT. Let A_prev be the algebra of all earlier data, retaining its earlier equations; it may already include the accepted early/modified tower and previous middle compatibilities. The actual two source coefficients at this gap are equivalent to one coordinate Y_h and ONE retained row

    H7_h*Y_h+J_h=0,
    H7_h=[theta^7](C/a)^alpha.                      (4)

The coefficient J_h is explicitly defined below from ALL actual mixed forcing. No division by H7_h is made. The equivalence is an exact quotient-ring isomorphism over A_prev and all its algebras, not merely a generic field-point statement. Every other original row, mate coefficient, boundary condition and guard receives the same back-substitution.

There is a precise optional rank/unit discriminator: the actual two-by-two homogeneous residual determinant is a proved unit multiple of H7_h. Over any nonzero residue FIELD its rank is2 when H7_h!=0, and1 when H7_h=0. This neither proves that an exceptional field exists nor excludes it. The uniform unit question is left open at the explicit cubic factor criterion in section7.

## 2. Actual middle supports, shifted variable and absent target

The actual A weight is m-h, between r+1 and2r-1. A t^2 monomial would require S exponent r+1-h<0, so none exists. The t coefficient has S exponent i=2r+1-h, where1<=i<=r-1. Thus its FULL band is

    A_(m-h)=S^(m-h)U(theta),
    U=l_h theta+k_(m-h),
    l_h=v_(2r-h)-u*d_(2r+1-h).                     (5)

The constant1 in h(S)=1-u d+Sv is absent because i>=1. In particular l_h is not the unshifted v coefficient. The product u*d_(2r+1-h) is earlier data: the accepted first r steps consume every d_0,...,d_(r-1), and its modified next step consumes u. Before those substitutions it can equally be treated as an unchanged earlier parameter. The inverse on actual source coefficients is

    v_(2r-h)=l_h+u*d_(2r+1-h).                     (6)

No parameter division is involved.

The B band has weight n-h. Since B5 is purely leading and accepted16r gives

    B4=-2uS+S^2 e(S),

it has no t^4 contribution: the required S exponent r+2-h is0 at h=r+2 and negative thereafter, while B4 has only positive powers of S. Therefore

    B_(n-h)=S^(n-h)V(theta), deg V<=3.               (7)

The t^3 coefficient occurs at S exponent2r+2-h>=2, so the beta*S gauge is not involved; the gamma constant is still lower. This supports the original ordinary polynomial source at every boundary, without a generic S inversion.

The Jacobian weight here is7r+2-h, lying in the entire integer interval[5r+2,6r]. The neighboring target weights are6r+1 from2uS*t^6 and5r+1 from-2S*t^5; none lies inside. The term -ell*S*t^4 has weight4r+1, NOT5r+1. All other literal target terms lie outside as well. Hence the direct target in this band is zero, although the earlier u-dependent target has already affected the actual earlier B bands and must remain inside the mixed forcing.

## 3. Full mixed forcing and a formal auxiliary completion

Write all actual earlier bands as A_(m-i)=S^(m-i)U_i(theta) and B_(n-j)=S^(n-j)V_j(theta). Define

    W_h=sum_(i+j=h; i,j>=1)
       ((m-i)U_i V_j'-(n-j)U_i'V_j).                (8)

This includes the modified u step and every previous particular solution, not only homogeneous kernel representatives. It depends only on gaps strictly less than h. Since earlier U_i have degree<=2 and earlier V_j degree<=4, deg W_h<=5. No earlier low residual is assumed zero when defining this polynomial; subsequent substitution of accepted equations is explicit.

For the proof introduce AUXILIARY spaces deg U<=2,deg V<=4 and

    L_h(U,V)=mCV'-(n-h)C'V+(m-h)UD'-nU'D.          (9)

Their extra U2,V4 are algebraic construction coordinates, not permissible additional source monomials at these gaps. We impose U2=0 below, which also forces V4=0. In particular a formal theta^4 term that would correspond to a negative S exponent is never asserted to be an ordinary source term.

With c0=a,c1=H,c2=F,c3=1, the literal coefficient formula is

    [theta^k]L_h=
      sum_(i+l=k+1)(m*l-(n-h)i)c_i V_l
       +sum_(i+l=k+1)((m-h)l-ni)U_i D_l.            (10)

At theta^(j+2), j=4,3,2,1,0, the V_j pivot is

    delta_j=m*j-3(n-h),
    delta4=3(h-r)-2>0,
    delta3=3h-6r-3<=-3,
    delta_j=delta3-m(3-j)<0 for j<3.                (11)

All are fixed nonzero rational units throughout(1). Thus the same five descending equations define the homogeneous linear upper solution V_lin(U), and a particular solution V_part with U=0 and

    [theta^k](L_h(0,V_part)+W_h)=0, k=6,...,2.      (12)

Since W_h has no theta6 term, delta4*V_part,4=0, so V_part,4=0 exactly. Define the ENTIRE particular residual

    c_h1 theta+c_h0=L_h(0,V_part)+W_h.             (13)

No forcing coefficient has been suppressed. The actual auxiliary upper solution is V_lin(U)+V_part. Its two residuals are the homogeneous pair of L_h(U,V_lin(U)) plus(c_h1,c_h0).

The two exact source slots consumed by this comparison are

    r1=[S^(6r+2-h)]E1_res,
    r0=[S^(7r+2-h)]E0_res,                        (14)

because the full band is S^(7r+2-h)(L_h+W_h). Powers theta6 through theta2 are the five upper rows; after the actual support restrictions theta6 is automatic and V3,...,V0 are the four ordinary upper unknowns. No residual below(14) is dropped.

## 4. Extend the unmodified algebraic inverse, without extending its old source claim

The accepted inverse mechanism can be used on these auxiliary spaces: its proof needs only nonzero pivots(11), exact(3), and the unit a, not the old early-gap source support. For completeness the finite formulas and their identities are checked here.

For any prescribed R=R1 theta+R0 and rho define

    G_h=(C/a)^alpha,
    T=trunc_(degree<=7)
        [G_h*(rho+integral_0^theta R/G_h)],
    N_U=(m/kappa)C*(T'-R)-C'T,
    N_V=(n/kappa)D*(T'-R)-D'T.                     (15)

These are formal finite-coefficient prescriptions. Equivalently t0=rho and

    a*i*t_i=sum_(j=1)^min(3,i)((alpha+1)j-i)c_j*t_(i-j)
                         +[theta^(i-1)]C R,
    i=1,...,7.                                     (16)

No coefficient was computed or emitted. All denominators are fixed rationals and the already-unit a. The formal differential identity T'-R=alpha(C'/C)T holds through order theta6, so N_U is divisible by theta7. Its degree<=9 gives U=N_U/theta7 of degree<=2. Further,

    C N_V-(n/m)D N_U=(theta7/m)T.                  (17)

Since C is a unit modulo theta7, N_V is also divisible, with V=N_V/theta7 of degree<=4. Division-free cancellation using nC'D-mCD'=theta7 gives

    mCV-nDU=T,
    C'V-D'U=(T'-R)/kappa,
    L_h(U,V)=R.                                    (18)

The signs are fixed by the literal leading equation, not by a reciprocal-variable convention alone. Theta7 is a nonzerodivisor in the polynomial ring even over a nonreduced coefficient algebra.

The five upper pivots make V=V_lin(U); T(0)=ma*V_lin(U)(0)-nb*U0=:rho_h(U). Conversely any U with its V_lin(U) satisfies(18), and polynomial divisibility of N_U forces exactly recurrence(16) through degree7. Since deg T<=7, it is recovered uniquely from R and rho. Thus(15) defines a two-sided linear inverse Phi_h of

    N_h:U -> ([theta1]L_h(U,V_lin(U)),
              [theta0]L_h(U,V_lin(U)),rho_h(U)).    (19)

It is valid over every L-algebra. This statement is about the formal completion, not an assertion that its U2 or V4 is present in the source.

The leading theta9 coefficient of N_U gives a particularly useful exact identity:

    U2=(7m/kappa-3)T7=(delta4/kappa)T7.             (20)

Both delta4 and kappa are nonzero rationals here. Therefore the actual source restriction U2=0 is EXACTLY T7=0, over any coefficient algebra. The theta7 coefficient of mCV-nDU=T is mV4-nU2=T7, so V4=0 follows as well. This is also the theta6 upper equation with U2=W6=0. No extra source-support condition is omitted.

## 5. The one retained compatibility and both quotient maps

Use(15) with

    R=-c_h1 theta-c_h0, rho=Y_h,
    H7_h=[theta7]G_h,
    J_h=[theta7]G_h*integral_0^theta
                      (-c_h1 tau-c_h0)/G_h(tau) dtau. (21)

Thus T7=H7_h Y_h+J_h. The displayed coefficient extraction in J_h applies to the ENTIRE product and integral; all coefficients c_h come from(12)-(13). This is not a leading-only or homogeneous-forcing replacement.

Let A_prev include the earlier parameters and their actual retained relations. Begin with the auxiliary quotient imposing its two residuals and U2=0. The invertible affine completion(19) carries the two residuals to zero and U2 to the rational-unit multiple(delta4/kappa)(H7_h Y_h+J_h). Consequently

    A_prev[l_h,k_(m-h)]/(the two actual rows(14))
          ~= A_prev[Y_h]/(H7_h Y_h+J_h).            (22)

The identification on the left uses the source's actual U2=V4=0 and the four remaining upper rows, exactly as established in section4. This is a quotient-ring isomorphism, including nilpotents and all coefficient strata. It uses NO inverse of H7_h.

The forward construction from the right of(22) is explicit. Form T,N_U,N_V by(15),(21), obtain U,V_lin, then set

    l_h=U1, k_(m-h)=U0,
    v_(2r-h)=U1+u*d_(2r+1-h),
    V_actual=V_lin+V_part.                         (23)

The retained row(4) makes U2=V4=0. All five auxiliary upper equations therefore agree with the actual ordinary upper equations, and(18),(13) kill BOTH residuals(14). Rebuild the whole B using the original16r recursion with this coefficient substitution; uniqueness of each upper row ensures its band equals(23).

Conversely start with actual source coefficients satisfying the two rows. Form U=l_h theta+k_(m-h), subtract the full particular V_part from the actual B band, and set

    Y_h=ma*(V_actual(0)-V_part(0))-nb*k_(m-h).      (24)

The completed inverse then recovers precisely U,V_lin. Their degree bounds give T7=0, hence the retained row(4). The two compositions are identities by(19), not just a bijection of reduced field points.

Equation(24) distinguishes homogeneous rho from the whole constant. The latter is

    [theta0](mC V_actual-nD U)=Y_h+ma*V_part(0).    (25)

Feeding that whole value into(21) without subtracting the shift is not the proved map. All previous V_part terms also stay inside W_h; they cannot be replaced by homogeneous kernel representatives.

One may compose these exact middle substitutions in increasing h. The new pair at each step is the previously unconsumed v_(2r-h),k_(m-h); the shift uses earlier u,d data. The next coefficient algebra may contain previous H7 Y+J relations and nilpotents, which cause no difficulty because the inverse only divides a and fixed rational units. The interval contains r-1 such steps, and retains r-1 compatibility rows rather than claiming r-1 free coordinates. Together with the accepted first r+1 steps, this supplies exact transport up to gap2r only. Every remaining E1/E0 coefficient, leading relation, full mate, inverse-polynomiality condition, original gauge and guard receives the same literal substitution. No statement for h>=2r+1 is used or claimed.

## 6. Exact rank locus, not a generic elimination

Let M_act be the homogeneous two-by-two residual matrix in the actual coordinates(l_h,k_(m-h)), at fixed earlier data. Translation by the fixed -u*d term only changes the affine residual, not this matrix. It is the last two columns of the auxiliary homogeneous residual map in(19), whose full three-by-three completion N_h has columns(U2,U1,U0) and rows(R1,R0,rho).

The rho-kernel generator is Phi_h(0,0,1). By(20) its first coefficient is(delta4/kappa)H7_h. The cofactor formula for the(1,3) entry of N_h^-1 therefore gives

    det(M_act)=det(N_h)*(delta4/kappa)*H7_h.         (26)

The sign is positive because the relevant cofactor removes row3,column1. Det(N_h) is a unit by the explicit two-sided inverse; no determinant was evaluated. Thus the determinant ideals differ only by a unit, over L and every base extension.

Over a NONZERO RESIDUE FIELD, M_act has rank2 off H7_h=0. On H7_h=0 its rank is at most1; it is at least1 because the auxiliary two-by-three residual map is surjective and adjoining one column to a rank0 two-by-two map could give rank at most1. Hence its rank is exactly1 on that field locus. This is not evidence that such a residue field of the guarded leading algebra exists. Over nonreduced algebras one retains the equation(4), not a field-rank slogan or a branchwise specialization.

If H7_h is a unit then Y_h=-J_h/H7_h is a legitimate further elimination, but unitness is NOT proved here. If its image is zero in a field, the row instead requires J_h=0 and leaves Y_h free when that holds, or rejects that field stratum when it does not. A nonunit that is neither zero nor invertible must not be replaced by either field case in the base ring. The presentation(22) covers all of them without a branch farm.

## 7. A finite residual factor criterion; no unit conclusion

For an indeterminate X put

    Hcal7(X)=[theta7](C/a)^X in L[X].               (27)

Its finite binomial definition has degree at most7 in X. It vanishes at X=0,1,2 because the corresponding polynomials in theta have degree0,3,6. It also vanishes at nu=n/m, as an EXACT guarded leading-ring identity, not just at field points. To verify this fourth root, set Gnu=(C/a)^nu. From(3),

    (D/Gnu)'=-theta7/(m*C*Gnu),
    D=b*Gnu+O(theta8).

Since D has degree5 and b is a unit, [theta6]Gnu=[theta7]Gnu=0. No existence of a leading pair or reducedness was used.

The four numbers0,1,2,nu are distinct rationals; their differences are units because1<nu<2. Repeated monic division in L[X] therefore gives a literal factorization

    Hcal7(X)=X(X-1)(X-2)(X-nu)*S_r(X),
    deg_X S_r<=3.                                  (28)

The quotient S_r may have vanishing coefficients or even be zero on a component. No coefficient, factor or root of it was computed. At the actual middle gaps,

    2+1/m<=alpha<=2+(r-1)/m<7/3,
    nu<2.                                          (29)

Thus every one of the four rational prefactors in(28), evaluated at alpha, is a nonzero rational unit. Consequently

    (H7_h)=(S_r(alpha)) as ideals of L,
    H7_h a unit <=> S_r(alpha) a unit.              (30)

This is the exact remaining discriminator, not a proof of unitness. The numerical interval(29) supplies no positivity or real-root restriction on S_r over complex leading fields. Removing the four known roots leaves a cubic which could still vanish at an intermediate rational alpha on some leading component. Whether that actually happens for any fixed integer(r,h) remains unproved here. In particular, no nonemptiness/count attribution from the accepted gate's closing prose is adopted.

The first bounded unresolved case is r=2,h=4: m=7,n=12,alpha=15/7,nu=12/7. Its exact question is whether L_2/(S_2(15/7)) is the zero ring with every guarded leading relation retained. That is a future separately authorized exact check, not a calculation or a review/solver invitation made by this report. Even a unit decision for that one case would not establish all r.

## 8. Manual negative controls and boundaries of the result

1. DROPPED H7 ROW. In the auxiliary completed coordinates, choose prescribed residuals/read-back N_h(1,0,0). The exact inverse returns U2=1. The row T7=0 rejects that object because(20) then gives T7=kappa/delta4, a nonzero rational unit. Dropping the compatibility admits an auxiliary quadratic A band which is not present in the actual middle source. This is a genuine altered-band control whenever the base is nonzero, not a claim that those prescribed residuals equal an actual W_h or yield a complete point.

2. WRONG -ud SHIFT. Replacing l_h by v_(2r-h) changes the literal coefficient of S^(2r+1-h)t in A by u*d_(2r+1-h). That product belongs to earlier data but is not declared zero by the source formula. The formal changed-object choice u=d_(2r+1-h)=1,v_(2r-h)=0 has actual coefficient-1 and wrongly unshifted coefficient0. It tests the parameter-to-polynomial identity, not a full-source solution. Formula(6) is essential in BOTH directions.

3. HOMOGENEOUS INSTEAD OF ACTUAL EARLIER MATE. If an earlier gap j has V_j=V_lin,j+V_part,j, omitting V_part,j deletes from(8) the exact term

       (m-i)U_i V_part,j'-(n-j)U_i'V_part,j

   for each i+j=h. There is no hypothesis making it zero. The altered W changes(13),(21), including the affine constant in rho. The present maps retain these terms and do not infer their vanishing from the accepted first gap, where the particular part alone happens to be zero.

4. UNLICENSED H7 INVERSION. As an abstract compatibility-row control, over a field the row0*Y+0 leaves Y free, while0*Y+1 is inconsistent. Over Q[e]/(e^2), the row eY=0 defines a nonzero ring with torsion, whereas inverting e gives the zero ring. These are changed-coefficient algebra controls, not assertions that such coefficients occur on an allowed leader. They demonstrate why the exact base relation(4), rather than an unproved localization, is the valid uniform interface.

5. OUTSIDE THE INTERVAL. At the excluded value alpha=2, Hcal7 is identically zero because C^2 has degree6. This corresponds to h=2r+1, outside this task. It refutes a blanket H7-unit assertion across that boundary but does not settle any middle value. No theorem about that next source band is imported or derived here.

6. PREVIOUS ROWS AND GUARDS. Imposing only(4) with a fabricated J or a leading ODE holding merely at samples is insufficient. The construction requires all actual W coefficients from the original upper recurrence and exact(3) in the base, plus the untouched lower residuals and guard. A middle compatibility solution alone is not a compact/Keller/source point.

No mathematical subprocess, actual coefficient expansion, determinant, norm, resultant, matrix, field factor, point or unit certificate was computed. No source or solver policy was changed.

## 9. Completion

Outcome: exact middle-band presentation and rank-locus criterion PROVED manually; uniform unitness of H7_h is UNRESOLVED, reduced to(30) without losing its closed locus. Every source coefficient and row is transported explicitly, including the -ud shift, modified-u ancestry and homogeneous-versus-whole rho distinction. The task stops at h=2r. It makes no all-r exclusion, solvability, dimension, performance or nonemptiness claim.

All three science pins were checked before use. The current accepted gate was read WHOLE; unchanged prior WHOLE16r and own tower reads were explicitly reused after those checks. Only their named equations and accepted scope were used. No provenance, other report, current/live review, code/data, network/AWS/SSH/web/process, agent or shared/frozen/protected write occurred. Documentary metadata, apply_patch and existing begin/close/finalize/verify tools only. Own WHOLE and own-only OPEN/collision checks precede the unique marker; all writers IDLE before20:19:04.312446UTC.

## OPEN(S) RAISED

- OPEN[F10-ALLR-MIDDLE-H7-UNIT] QUANTITY: for each fixed r>=2, the number of middle integer gaps h with nonunit S_r((m+n-h)/m), unknown between0 andr-1; no existence of any such field stratum is asserted. CHEAPEST TEST: the exact r=2,h=4 guarded leading quotient L_2/(S_2(15/7)) above, preserving all components; an applicable exact norm/resultant or ideal test would require a separate registration and authorization. No runtime estimate or computation is supplied. This is the unresolved coefficient discriminator of the proved presentation, not a new full-source exclusion task.

## COLLISIONS

status: EMPTY

- NONE — own-only extraction; no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `21115`.
- Body SHA-256:
  `3b6d5920f54f0b0804a3eb789d2a8a2b8576e28c327248e92e66447194000645`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
