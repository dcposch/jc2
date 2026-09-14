# F10: an exact first-r early-band tower with all mixed forcing

2026-09-09. NEW MANUAL THEOREM, UNREVIEWED. First action19:29:08.936624UTC; controlling stop19:44:08.936624UTC. Exactly accepted16r and the accepted first-band producer/gate are scientific inputs. No unreviewed critical-band, univariate or later-band result is used. ZERO mathematical subprocesses, evaluated/emitted source coefficients or implementation.

## 1. Statement, accepted comparison and coefficient-ring scope

Fix r>=1 and m=3r+1,n=5r+2. Take the complete normalized16r presentation with

    A=S t^3+(Sd-u)t^2+(1-u d+Sv)t+k,
    deg d<=r, deg v<=2r, deg k<=m, k(0)=0;
    B=sum_(j=0)^5 B_j(S)t^j, B5=S^2,
    [S]B3=B0(0)=0,
    [A,B]_(S,t)=Delta=1+ut-ell*t*Pi-t*Pi^2,
    Pi=t-ut^2+St^3.                                 (1)

The B_j are the SAME five descending Euler reconstructions of16r. Every coefficient of E1_res,E0_res and the top guard omega*a*b-1 is retained except for the specifically eliminated rows below. No new gauge, output normalization or source specialization is introduced.

With weights wt(S)=1,wt(t)=r and theta=t/S^r, write

    A_m=S^m C(theta), B_n=S^n D(theta),
    C=theta^3+Ftheta^2+Htheta+a, D5=1,D0=b,
    mCD'-nC'D=-theta^7, a*b a unit.                  (2)

The algebraic theorem works over ANY commutative Q-algebra in which C,D satisfy(2) and a is a unit. The source also retains b as a unit. No reducedness, root simplicity, finite-etale property, factor choice or field-point existence is needed. In particular the base can be the full universal guarded leading algebra of(2); no all-r analogue of an r1 finite algebra is presumed.

THEOREM. For EVERY gap h=1,...,r, the exact two rows

    [S^(6r+2-h)]E1_res, [S^(7r+2-h)]E0_res           (3)

are affine-linear in the THREE actual coefficients

    d_(r-h), v_(2r-h), k_(m-h),                     (4)

with all earlier-band forcing retained. Their homogeneous coefficient map has an explicitly invertible three-by-three completion over the WHOLE leading algebra. Thus each triple can be replaced losslessly by one unrestricted coordinate Y_h. Composing these substitutions in increasing h gives an exact first-r-band tower with r such coordinates, retaining every other original row, every mate coefficient, boundary condition and guard by substitution.

The h=1 case is accepted in the charged first-band gate's separately labeled all-r section; the sealed producer itself proves r1. The NEW scope here is every early gap2<=h<=r, all their mixed forcing, and a direct prescribed-residual inverse avoiding a residue-field determinant proof. Section7 additionally proves the separately MODIFIED h=r+1 step, with its actual u-dependent target, from the same accepted inputs. No statement about gaps h>=r+2, the full ideal's properness/unitness, a source point or computation time follows.

## 2. Exact early supports, target gap and full cross term

Fix1<=h<=r. The homogeneous source band is exactly

    A_(m-h)=S^(m-h)U_h(theta),
    U_h=U2 theta^2+U1 theta+U0,
    (U2,U1,U0)=(d_(r-h),v_(2r-h),k_(m-h)).           (5)

Indeed the S exponents of its t^2 and t terms are r+1-h and2r+1-h. The former is at least1, so the -u t^2 term is absent. The latter is at least r+1, strictly greater than deg d; hence the -u d*t term contributes nothing. The constant t term has weight r and is also later. All indices in(4) are valid and distinct from the leading F=d_r,H=v_(2r),a=k_m.

Because B5=S^2 is purely leading,

    B_(n-h)=S^(n-h)V_h(theta), deg V_h<=4.           (6)

Every coefficient allowed here has nonnegative S exponent; for its highest possible t power4, that exponent is r+2-h>=2. The beta*S*t^3 gauge has weight m and occurs at gap n-m=2r+1>r, while gamma has weight0. Thus neither gauge interferes with these five early upper equations.

For homogeneous factors the chain rule is

    [S^p P(theta),S^q Q(theta)]
      =S^(p+q-r-1)(pP Q'-qP'Q).                    (7)

The leading target weight is7r+2. Its NEXT possible weight is6r+1, from2uS*t^6. Thus there is NO direct target term at weights7r+2-h for1<=h<=r. All terms involving u in A begin at gap r+1; ell's target terms are still later. This verifies the literal whole-positive early interval, not an omission based only on the leading equation.

For every previous gap i let U_i,V_i be the actual bands extracted from A and the reconstructed B. Define

    W_h=sum_(i+j=h; i,j>=1)
         ((m-i)U_i V_j'-(n-j)U_i'V_j).              (8)

This is EVERY cross term of positive gaps summing to h. It is zero at h=1 only; it is not set to zero at higher gaps. Since deg U_i<=2 and deg V_j<=4, deg W_h<=5. It depends on earlier A bands and earlier reconstructed B bands, not on the new triple(4) or any later coefficient. This triangular dependence follows either from homogeneous weight in(7), or by grading each of the original descending Euler equations. Earlier residuals need not already vanish for this statement.

Set

    L_h(U,V)=mCV'-(n-h)C'V+(m-h)UD'-nU'D.          (9)

Then the FULL weight7r+2-h part of [A,B]-Delta is

    S^(7r+2-h)(L_h(U_h,V_h)+W_h).                  (10)

The theta^1 and theta^0 slots are precisely(3). No theta substitution localizes the source ideal at S: it is only an identity of homogeneous coefficients, valid over arbitrary coefficient algebras since multiplication by S is injective in a polynomial ring.

## 3. Five exact upper equations and the homogeneous row map

Use c0=a,c1=H,c2=F,c3=1, with all other c_i zero. For arbitrary U of degree<=2 and V of degree<=4, the coefficient of theta^k in(9) is

    sum_(i+l=k+1)(m*l-(n-h)*i)c_i V_l
      +sum_(i+l=k+1)((m-h)*l-n*i)U_i D_l.           (11)

Negative or out-of-envelope indices mean zero. This specifies every coefficient and its index without an expansion. At theta^(j+2), the coefficient of V_j is

    delta_j=m*j-3(n-h), j=4,3,2,1,0.               (12)

All other V_l in that row have l>j. Moreover

    delta_4=3(h-r)-2<=-2,
    delta_j=delta_4-m(4-j)<0.

Thus all five pivots are fixed nonzero rationals, for every integer r>=1 and1<=h<=r. There is no parameter rank stratum or resonance in these rows. They are exactly16r's Euler eigenvalues at the S slot n-h-rj, since

    j-3(n-h-rj)=(3r+1)j-3(n-h)=delta_j.

Let V_lin(U) be the unique solution of the theta6,5,4,3,2 equations L_h(U,V)=0 at those powers, using(11)-(12). It is linear in the three coefficients of U. Define

    M_h U=(R1(U),R0(U)),
    R1 theta+R0=L_h(U,V_lin(U)),
    rho_h(U)=m*a*[theta0]V_lin(U)-n*b*U0.           (13)

The whole L_h has degree<=6, so these two residuals are all that remains after those five upper equations. The completed map is

    N_h:U -> (R1(U),R0(U),rho_h(U)).                (14)

We now give its exact inverse, not a generic-rank assertion.

## 4. Direct inverse for ANY prescribed low residual and read-back coordinate

Put kappa=m+n-h and alpha=kappa/m. These are fixed nonzero rationals. For arbitrary prescribed R(theta)=R1 theta+R0 and rho0 in the coefficient algebra, define a polynomial T of degree<=7 by the finite prescription

    G=(C/a)^alpha,
    T=trunc_(theta degree<=7)
       {G(theta)*(rho0+integral_0^theta R(tau)/G(tau) dtau)}. (15)

No analytic choice or actual series computation is involved. The normalized constant C/a=1+O(theta) makes the formal rational power unique. An equivalent seven-step definition, with T=sum t_i theta^i and t0=rho0, is

    a*i*t_i=
      sum_(j=1)^min(3,i) ((alpha+1)j-i)c_j*t_(i-j)
      +[theta^(i-1)]C R,  i=1,...,7.                (16)

Only the already-unit a and fixed nonzero integers are divided. This recurrence also makes the linear dependence on(R1,R0,rho0) literal.

Define the two numerators

    N_U=(m/kappa)C*(T'-R)-C'T,
    N_V=(n/kappa)D*(T'-R)-D'T,                      (17)

and set U=N_U/theta^7,V=N_V/theta^7. We prove these are actual polynomials with the required degrees.

The untruncated formal expression in(15) satisfies

    T'-R=alpha*(C'/C)*T.

Truncating at degree7 changes T by O(theta8) and its derivative by O(theta7). Consequently N_U is divisible by theta^7. It has degree<=9, so its quotient U has degree<=2. The identity

    C N_V-(n/m)D N_U=(theta^7/m)T                  (18)

follows directly from(2). Since C has unit constant a, it is a unit modulo theta^7 over ANY coefficient algebra. Hence N_V is divisible by theta^7 too; its degree<=11 gives deg V<=4. These are polynomial divisibility arguments, not rational expressions with an unchecked pole at theta=0.

The signs in(17) are essential. Direct cancellation, using nC'D-mCD'=theta^7, gives

    mCV-nDU=T,
    C'V-D'U=(T'-R)/kappa.                         (19)

To justify canceling theta^7 here, it is a nonzerodivisor in the polynomial ring even if the coefficient algebra has nilpotents. Differentiate the first identity. Algebraically

    L_h(U,V)=T'-kappa*(C'V-D'U)=R.                 (20)

Also T(0)=m*a*V0-n*b*U0=rho0. Thus(17) gives a pair satisfying every upper equation, exactly the prescribed TWO residual coefficients, and the prescribed read-back coordinate.

In particular V equals V_lin(U), by uniqueness from(12), because R has degree<=1. Let Phi_h(R1,R0,rho0) be the three coefficients of this U. Equations(19)-(20) prove

    N_h Phi_h=identity.                            (21)

Conversely take any U and its V_lin(U); put R=L_h(U,V_lin(U)) and T=mCV_lin(U)-nDU. Differentiation gives the second identity in(19). Therefore

    theta^7 U=(m/kappa)C*(T'-R)-C'T,
    theta^7 V=(n/kappa)D*(T'-R)-D'T.                (22)

The first equation forces precisely recurrence(16) through degree7, with rho0=T(0); since deg T<=7, it determines all of T. Thus(15)-(17) reconstruct the original U,V, proving Phi_h N_h=identity as well. This rederivation uses the POSITIVE theta^7 sign displayed in(22); a misleading intermediate sign in the older gate is not a premise.

We have exhibited the entire inverse of(14) over every leading Q-algebra, with no determinant evaluation, field-factor decomposition, maximal-ideal argument or new parameter inversion. Its first two rows consequently form a split surjection of rank2 and its joint kernel is free of rank1. A specified generator is

    beta_h=Phi_h(0,0,1), rho_h(beta_h)=1.           (23)

Thus beta_h is nonzero over every nonzero residue field, and over every nonzero coefficient algebra at least one of its entries survives. It is unnecessary to prove that a particular entry or two-by-two minor is a unit. The three-by-three completion is invertible over the base, with the explicit two-sided inverse above.

## 5. All mixed forcing and the correct affine rho convention

For the actual W_h in(8), let V_part be obtained by the SAME five descending equations with U=0 and

    [theta^k](L_h(0,V_part)+W_h)=0, k=6,...,2.      (24)

All divisions are the fixed delta_j. Define the entire remaining particular residual

    c_h1 theta+c_h0=L_h(0,V_part)+W_h.             (25)

It has degree<=1 by construction, and it depends only on earlier bands and leading data. The actual upper-reconstructed band decomposes exactly as

    V_actual=V_lin(U_h)+V_part.

Hence its two full residuals are

    M_h U_h+(c_h1,c_h0).                           (26)

Choose a new unrestricted coefficient Y_h, and substitute

    U_h=Phi_h(-c_h1,-c_h0,Y_h).                    (27)

The two residuals then vanish identically; conversely every solution of them has uniquely Y_h=rho_h(U_h), by(21)-(22). This is an exact affine polynomial isomorphism over the earlier-parameter algebra, including all nonreduced algebras. The coefficient functions may contain powers of the already-unit a^-1; no new localization has been introduced.

The rho convention is not optional: rho_h uses V_lin(U), not an unexamined full constant coefficient. Indeed for the whole band

    [theta0](mC V_actual-nD U_h)
           =rho_h(U_h)+m*a*V_part(0).              (28)

Thus using the whole constant as Y_h without subtracting this known earlier-dependent term would give a different, generally wrong back-map. Equations(24)-(28) retain that affine shift literally. No previous low residual has been used to suppress it.

## 6. Composition through gaps1,...,r, and complete row retention

Proceed in increasing h. At h=1 the sum W_1 is empty, V_part=c_1=0, and(27) reduces to U_1=beta_1 Y_1, recovering the accepted first-gap content. At h>=2 form W_h from EVERY pair of already reconstructed earlier bands, after their previous substitutions. The finite inversions(12),(16) and the maps(24)-(27) are then defined over the algebra in the previous Y_i and the still-unreplaced source coefficients.

Because the triples(4) are disjoint and W_h depends only on earlier gaps, this induction has no circular dependence. Its inverse is obtained by the same ordered extraction of U_h and rho_h(U_h). It eliminates precisely the pairs(3) for h=1,...,r and replaces the3r original coefficients by r unrestricted coordinates. Those coordinates are independent only in the quotient by these early rows; the retained later rows can impose further conditions on them.

For clarity the consumed coefficients are

    d_0,...,d_(r-1);
    v_r,...,v_(2r-1);
    k_(2r+1),...,k_(3r).

The unconsumed u,ell,v_0,...,v_(r-1),k_1,...,k_(2r), leading F,H,a and the original top-product restoration remain, as do ALL other residual coefficients after back-substitution. In particular the leading rows that impose(2), every row below the early interval, both full inverse-polynomiality conditions, the whole mate B*, and the guard are not discarded. This is an exact quotient-ring presentation over the leading algebra, compatible with the16r field/source back-map. If one keeps leading relations in the original coefficient presentation rather than in the base, they must simply remain explicit there.

Nothing sets a Y_h to zero or to1. They are not output-shear gauges. The existing beta=gamma=0 and k(0)=0 gauges remain unchanged. No full-system point, properness/unit decision, source exclusion, source degree change, expression-size improvement or runtime claim is established. The result is an exact early-band elimination tower, not a whole all-r solver or a theorem about later supports.

## 7. Separate NEW MODIFIED step at h=r+1

This optional in-cap addition was rederived manually from(1),(2), not from any later-band report. It does NOT apply the preceding zero-target source formula unchanged. At h=r+1 the source A weight is2r and its literal band is

    U=q theta^2+l theta+k0,
    q=-u, l=v_(r-1)+Fq, k0=k_(2r).                 (29)

Here k0 is a temporary name for this band's constant coefficient, not the fixed original k(0). The change from the three actual variables (u,v_(r-1),k_(2r)) is invertible without parameter division: u=-q, v_(r-1)=l-Fq. The actual target at this weight is2u theta6=-2q theta6. Thus the modified homogeneous operator to invert is

    Ltilde(U,V)=L_(r+1)(U,V)+2U2 theta6.            (30)

The full residual adds the entire W_(r+1) from(8), using all r earlier gaps. That forcing depends only on earlier data, not q,l,k0. No ell term occurs at this weight. The original B band still has degree<=4, and its V4=2q matches the actual term -2uS in B4. The five upper pivots on V_j are now

    delta_4=1, delta_j=1-m(4-j), j<4,

all nonzero rational scalars for r>=1. The theta6 contribution of U is -4q before the new target is included, so its modified row is V4-2q=0. This checks the special top row rather than silently carrying over the previous zero-target operator.

Put kappa=7r+2, alpha=kappa/m. For ANY prescribed low residual R=R1 theta+R0 and homogeneous read-back rho0, form

    Tbase=trunc_7[(C/a)^alpha
                   *(rho0+integral R*(C/a)^(-alpha))],
    t7=[theta7]Tbase,
    q=7*t7/kappa,
    T=Tbase-(2q/7)theta7.                          (31)

Use the numerators

    N_U=(m/kappa)C*(T'+2q theta6-R)-C'T,
    N_V=(n/kappa)D*(T'+2q theta6-R)-D'T,             (32)

and divide both by theta7 to define U,V. The quotient and degree proofs are literal: T'+2q theta6-R=Tbase'-R. Relative to the unmodified first numerator built from Tbase, N_U adds (2q/7)C' theta7. It is therefore divisible by theta7, with quotient degree<=2. The same identity(18), with T as in(31), makes N_V divisible and gives degree<=4.

The key consistency is that this constructed U really has U2=q, so the target in(32) has not introduced an independent hidden parameter. Since

    7m-3kappa=1,

the coefficient theta2 of the unmodified numerator quotient is t7/kappa. The added term contributes6q/7. Hence

    U2=t7/kappa+6q/7=q.                            (33)

Equivalently T7=t7-2q/7=rq, and the highest coefficient in(32) is (T7+2mq)/kappa=q. Both forms verify the same normalization.

The division-free recoveries become

    mCV-nDU=T,
    C'V-D'U=(T'+2q theta6-R)/kappa.

Consequently L_(r+1)(U,V)=-2q theta6+R, and (30) equals R exactly. T(0)=rho0 still. Upper uniqueness identifies this V with the homogeneous modified Euler solution Vtilde_lin(U).

For the converse, start with any U and Vtilde_lin(U), put q=U2,R=Ltilde(U,V),T=mCV-nDU. Setting Tbase=T+(2q/7)theta7, divisibility of the first numerator forces the SAME seven low coefficient equations defining Tbase in(31), with its given constant. The highest-coefficient identity forces q=7[theta7]Tbase/kappa by(33). Thus(31)-(32) reconstruct the original U,V. This is a two-sided completed inverse over every leading algebra, not only a surjectivity or residue-field rank statement.

Define rho_tilde(U)=ma*Vtilde_lin(U)(0)-nb*U0. For the actual mixed W_(r+1), construct V_part with U=0 by the five upper equations and take

    c1 theta+c0=Ltilde(0,V_part)+W_(r+1).

The modified inverse applied to (-c1,-c0,Y_(r+1)) solves the full pair; the whole constant is again rho_tilde(U)+ma*V_part(0), so the affine correction is retained. The literal residual rows are [S^(5r+1)]E1 and[S^(6r+1)]E0. Every other original row and guard remains under substitution.

This separately modified step can therefore be composed after section6, leaving r+1 kernel coordinates for these first r+1 bands. It uses the new triple(29), disjoint from the triples already consumed, and returns its three source coefficients by their explicit inverse. It is not an unmodified application of(27) with a nonexistent d_(-1). At h>=r+2 the t^2 coefficient is no longer a freely available third coefficient; further source/target analysis is not supplied. No later-band rank, overall solution, coordinate-unit or speed claim follows.

## 8. Changed-object controls and the first failed unmodified extension

1. PRESCRIBED RESIDUAL CONTROL. Phi_h(1,0,0) is an exact coefficient vector whose homogeneous upper equations hold but whose residual is theta, not zero. Phi_h(0,1,0) has residual1. Thus deleting either low row admits a real changed band object. Neither is claimed to be a complete source point. These follow from the two-sided algebraic inverse, not sampled arithmetic.

2. MIXED-FORCING CONTROL. Deliberately replace W_h by the constant polynomial1. Then V_part=0, c_h=(0,1). The homogeneous formula beta_h Y_h alone leaves residual1; the correct affine map is Phi_h(0,-1,Y_h). This proves why(25)-(27) cannot be replaced by a homogeneous first-band repetition. It is a changed prescribed-forcing control, not an assertion that the actual W_h has this isolated value at some source point.

3. SIGN/INDEX CONTROL. The recovery identity is nC'D-mCD'=theta^7. Replacing it by its negative in(17),(22) reverses the recovered T and residual. Formula(11) also keeps separate coefficient pairs c_i V_l and U_i D_l with i+l=k+1. A shifted or reversed D index is not licensed by using the reciprocal theta coordinate; the exact basis and(2) fix the convention.

4. KERNEL COORDINATE CONTROL. Phi_h(0,0,0)=0, whereas rho_h(Phi_h(0,0,1))=1. Hence the band does not force all three coefficients to vanish, and freezing Y_h=0 would lose band solutions. This is not a claim about solutions of the remaining full equations.

5. THE RANGE h<=r IS LOAD-BEARING FOR THE SOURCE ARROW. At h=r+1, the actual A band has weight2r and is

       U=-u*theta^2+(v_(r-1)-uF)*theta+k_(2r),

   not the nonexistent triple(d_(-1),v_(r-1),k_(2r)). The actual target now contributes2u*theta^6, from2uS*t^6. Both the new variable coupling and the direct high target must be retained. The zero-target residual map for three independent early coefficients is therefore not the literal next source band. Section7 proves its MODIFIED completed inverse with these changes; no later-band architecture follows. Omitting the correction -(2q/7)theta7 would instead leave U2=t7/kappa, incompatible with the required choice q=7t7/kappa except on a restricted sublocus. A statement that one failed unmodified extension proves all uniform approaches impossible would equally be unsupported.

6. WHOLE-rho CONTROL. Omitting m*a*V_part(0) from the comparison(28) identifies the wrong affine coordinate whenever that term is nonzero. The proved construction uses the homogeneous variation functional and preserves the shift, without asserting it vanishes in the actual earlier-parameter ring.

These are manual symbolic controls and exact finite prescriptions. No coefficient values, matrix entries, rank experiment, inverse matrix, source polynomial, CAS or test script was produced.

## 9. Completion and scope of the remaining problem

The new theorem supplies a specified two-sided inverse for each early completed coefficient map and a faithful composition through h=r, plus the separately derived modified h=r+1 step. The interval starting h=r+2 and every remaining full residual are outside this result. The smallest next interface gap is its reduced source support, not a missing proof of rank in the already-covered interval. The optional extension was authorized and completed within the ORIGINAL cap using the same three sources, not a new input or deadline. No new OPEN task, implementation, computation or descendant is authorized here.

Exactly three permitted scientific objects were current-hash checked before WHOLE reads. The first aggregate output truncated part of the gate; it was reread separately in full. No unreviewed critical-band theorem or current gate, later-band/univariate science, provenance follower, code/data, web/network, AWS/SSH/process, agent or shared/protected artifact was accessed. All algebra is manual; only documentary metadata, apply_patch and existing publication tools ran. Own WHOLE and own-only raised-OPEN/collision checks precede the unique completion marker. All writers IDLE before19:44:08.936624UTC.

## OPEN(S) RAISED

None. The early interval and the explicitly modified next step are complete at their stated scope; further band changes remain outside it. Any future actual use must transport every retained row under the appropriate back-map, with independent authorization; no such rows are emitted here.

## COLLISIONS

status: EMPTY

- NONE — own-only check; no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `22994`.
- Body SHA-256:
  `747074cf3f8f581b87b96ad6c004ca3d437d071a107f0d0740915fd85a0ad712`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
