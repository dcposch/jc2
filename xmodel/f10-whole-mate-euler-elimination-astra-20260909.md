# F10 whole-mate Euler elimination

2026-09-09. NEW/PROVISIONAL pure hand proof; ZERO mathematical subprocesses. Basis0d39df3c9fd69c939a8420c54d03228b9077777d is provenance only. This is an exact elimination and smaller complete field-point presentation, not an exclusion, point, solver result or runtime claim.

## 1. Result and exact accepted inputs

For every r>=1, put m=3r+1,n=5r+2. Over any characteristic-zero field, the accepted complete F10 compact system is existentially equivalent to the explicit polynomial system in section7, with

    6r+6 variables and at most13r+7 rows;
    at r=1:12 variables and at most20 rows.       (1)

These are presentation counts, not dimensions or actual generated-file counts. All mate coefficients are reconstructed by five diagonal Euler inversions with fixed nonzero rational denominators. The two apparent resonance conditions are automatic. BOTH inverse-polynomiality conditions are retained exactly, one by parametrization and the other by a proved consequence of the upper Jacobian rows. Only the ENTIRE t^1 and t^0 residual polynomials and an invertible top-product guard remain. The mate is unique up to beta*A+gamma; an A constant is also an explicitly recorded target-translation gauge.

The scalar normalization does NOT keep both highest S powers monic: their nonzero coefficients a,b are retained, and restored at the end. No S,u,ell or boundary-value inversion is used. The proof is uniform in r; a hand family in section8 shows the final constant equation is not automatic, even after every eliminated row and the leading-degree guard.

Only these three reports were checked current before their WHOLE reads:

- Compact contract, SHA6c6fe089033832c9d33639f8438a43c3dbfd8a28d06e05ef76ee141438de6d7f.
- Cubic module, SHA26687318390a287fe08a803191e27d131d8a8fd4992d5b4d6d81a35f39d23954.
- Accepted independent gate, SHA1bf4c20c37a0d45874e110a3d991a481fe88165156c0f6fcb41f180c8514705b.

Exact paths/bytes and read/start scope are in the owned PINS.json and READ-SCOPE.md. Their accepted16q conclusions, not historical provisional headers, govern. No1110 blind, mutable ledger, source/provenance or live review was read. No initial-ODE existence theorem or fixed-A linearization is used to prove (1).

## 2. Normalization and the whole A boundary

Write S for the compact contract's translated R, and put

    p=Pi=t-u t^2+S t^3,
    Delta=1+u t-ell t Pi-t Pi^2,
    x=St, y=St^2-ut.

The accepted gate proves that every complete contract point has original leading t coefficients kappa_A S and kappa_B S^2, with kappa_A*kappa_B=c!=0. Divide the two outputs by these respective nonzero scalars. Thus the normalized pair has

    A=S t^3+f(S)t^2+h(S)t+k(S),
    B=sum_(j=0)^5 B_j(S)t^j, B_5=S^2,
    [A,B]_(S,t)=Delta.                           (2)

The leading coefficients a=[S^m]k and b=[S^n]B_0 are now kappa_A^-1 and kappa_B^-1. They MUST remain nonzero, but need not equal one. No extension of the original coefficient field is needed for this normalization.

The exact A boundary tests of the module are equivalent to

    f=S d-u, h=1-u d+S v,
    deg d<=r, deg v<=2r, deg k<=m.              (3)

Here v is a new coefficient polynomial, not the old translated reference constant. Equivalently A=k+p+v x+d y, so its inverse is ordinary along the WHOLE finite boundary, including u=0 and S=0. Conversely every A of (3) has the required coefficient bounds and inverse ordinaryness.

Target translation A -> A-k(0) is harmless; from now on k(0)=0 is an explicit gauge. It does not change any derivative, leading coefficient or boundary condition. The whole mate B is allowed to vary; this is not a fixed-A impossibility argument.

## 3. Exact descending operator and all target coefficients

For a polynomial F(S)=sum F_i S^i let theta=S*d/dS and E_j=j-3theta. Then E_j acts diagonally by j-3i on S^i. For j=4,2,1 it is invertible on every bounded polynomial space. For j=3 its kernel is K*S and its image omits only the S coefficient; for j=0 its kernel is K and its image omits only the constant coefficient. Inverses below simply divide each nonresonant coefficient by j-3i. These are fixed nonzero rational scalars, not functions of the source parameters.

The exact coefficients Delta=sum_(h=0)^7 delta_h t^h are

    delta_0=1, delta_1=u, delta_2=-ell,
    delta_3=ell*u-1, delta_4=2u-ell*S,
    delta_5=-u^2-2S, delta_6=2uS, delta_7=-S^2. (4)

They follow directly from the factored Pi formula. Set B_i=0 when i>5. For j=4,3,2,1,0, the coefficient of t^(j+2) in the whole Jacobian equation is precisely

    E_j B_j = Q_j,

    Q_j=delta_(j+2)
       -(j+1) f' B_(j+1)+2f B'_(j+1)
       -(j+2) h' B_(j+2)+h B'_(j+2)
       -(j+3) k' B_(j+3).                     (5)

Every term is present; primes mean S derivatives. This follows from the contribution (l A_k' B_l-k A_k B_l')t^(k+l-1). The t^7 coefficient is already -S^2 from A_3=S,B_5=S^2. No term above t^7 is possible. Thus (5) covers all coefficients t^6 through t^2 and ONLY those coefficients; t^1,t^0 are not yet solved.

Inductively each Q_j has degree at most n-rj. For example f'B_(j+1),h'B_(j+2),k'B_(j+3) have respective bounds r+(n-rj-r),2r+(n-rj-2r),3r+(n-rj-3r), all n-rj; the other terms and target obey the same bound. Euler inversion preserves degree. Consequently the reconstructed B_j satisfies exactly the original envelope deg B_j<=n-rj. The kernel terms S at j=3 and1 at j=0 also fit. No higher coefficient bound or generic leading noncancellation is assumed.

## 4. The first resonance cancels, without dividing u

The j=4 equation gives

    B_4=-2uS+S^2 e,
    (2+3theta)e=(1+5theta)d,
    e_i=(1+5i)/(2+3i)*d_i.                     (6)

This is an exact polynomial of degree<=r, with e_0=d_0/2 and e_1=6d_1/5. In particular the first mate boundary divisibilities already hold.

The j=3 forcing is

    Q_3=-u^2-2S-4f'B_4+2fB_4'-5h'S^2+2Sh.

Its constant coefficient is3u^2 and its S coefficient is2u*d_0-4u*e_0=0. Hence E_3 B_3=Q_3 ALWAYS has a polynomial solution. Write beta=[S]B_3; it is the one free scalar at this stage. Also

    [S^0]B_3=u^2,
    [S^2]B_3=H1-4u*d_1+2u*e_1,               (7)

where H1=[S]h. This is the needed next coefficient, obtained from the S^2 coefficient of Q3 and eigenvalue -3. All these identities hold also at u=0.

## 5. Every B boundary condition is forced before solving j=0

Continue (5) for j=2 and j=1, whose operators have no kernel. The exact quintic module test, with B5=S^2 and (6), first gives d_star=1,b_star=e and then requires polynomial quotients

    a_B=(B_3+uS e-S-u^2)/S,
    d_B=(B_2+u a_B-S e+u)/S,
    b_B=(B_1-a_B+u d_B)/S.                    (8)

The first numerator vanishes at S=0 by (7). To check the remaining two, let zeta=[S^2]B3 and w=[S]B2. Applying (5) at the indicated individual coefficients gives, by hand,

    B_2(0)=-u*beta-u^2*d_0/2,
    w=ell+d_0*beta+6u^2*d_1+4u*zeta-6u*H1
        -2e_0+2u*d_0*e_0,
    B_1(0)=ell*u-1-2d_0*B_2(0)-2u*w
        -3u^2*H1+(1-u*d_0)*beta.              (9)

These use respectively the constant and S coefficients of the j=2 equation, and the constant coefficient of the j=1 equation. The relevant eigenvalues are2,-1,1. Terms containing k' start too high in S to enter these three coefficients; they are NOT dropped from the full recurrence.

Now a_B(0)=beta+u e_0-1, so

    B_2(0)+u*a_B(0)+u=u^2(e_0-d_0/2)=0.

Thus d_B is polynomial. Its constant coefficient is w+u(zeta+u e_1)-e_0. Substitution of (9) into the final numerator in (8) gives exactly

    B_1(0)-a_B(0)+u*d_B(0)
      =u^2[d_0^2-2d_0*e_0-3zeta+3H1
                 +u(e_1-6d_1)]
      =u^3(6d_1-5e_1)=0.                    (10)

Here use e0=d0/2, zeta=H1-4u d1+2u e1, and e1=6d1/5 in that order. This proves b_B is polynomial. No division by u was used; all u=0 cases survive literally.

The module theorem now proves that the ENTIRE B constructed through j=1, with ANY polynomial B0, is inverse-ordinary. These are complete polynomial divisibility tests, not generic-S conditions or finitely sampled boundary values. B0 itself is a polynomial in S and introduces no inverse pole. The tests also yield exactly the accepted module coefficient-degree bounds, by the already proved bounds on B_j. Nothing on a missing branch of S=0 is assumed.

## 6. The second resonance, kernel and the two remaining equations

Take B0=0 temporarily, after j=1. All Jacobian coefficients t^7 through t^3 are correct, hence

    [A,B]-Delta=J2(S)t^2+J1(S)t+J0(S).

Under the inverse S=pz^3-z^2+uz,t=z^-1, both A and B are ordinary polynomials in p,z by (3),(8). The determinant of (p,z)->(S,t) is -z, and -z*Delta=p^2+ell*p-u-z is ordinary. Therefore

    -J2(S)/z-J1(S)-z*J0(S)

is ordinary in p,z. Since S has z-order at least one, its only possible negative-z coefficient is -J2(0)/z. It must vanish. But J2(0)=-Q0(0), because E0B0 has zero constant coefficient. Thus the j=0 resonance Q0(0)=0 is AUTOMATIC. This argument works unchanged if u=0 increases the z-order of S. It is a polynomial-boundary consequence, not a generic regularity assertion or a claim about source Jacobian divisibility in the wrong ring.

Solve E0B0=Q0 with B0(0)=0. Together with beta=0 at j=3 this defines a unique polynomial B*=B*(A,u,ell), satisfying every t^h equation for h>=2 and every inverse-pole condition. Each coefficient is a polynomial with rational coefficients in the chosen A,u,ell parameters: all inversions in (5) have fixed rational denominators. The automatic compatibilities are identities in these free parameters, as is seen either from (9)-(10) or by working over their rational function field in the boundary argument.

Within the stipulated t-degree-at-most-five class, every other polynomial mate with the same B5=S^2 and the same upper equations is

    B=B*+beta*A+gamma, beta,gamma in K.         (11)

Proof: subtract two such solutions. E4 forces their B4 difference to zero. E3 leaves beta*S. Subtract beta*A, which changes no Jacobian and kills that coefficient. Successive E2,E1 force the remaining B2,B1 differences to zero; E0 leaves only a constant gamma. This uses only the displayed diagonal operators, not an imported centralizer theorem. Both added functions are in the full boundary ring. Since m<n, neither beta*A nor gamma changes [S^n]B0, and all original bounds remain valid. Fixing beta=gamma=0 is therefore an honest mate shear/translation gauge, not an omitted stratum. It does not modify the remaining equations.

The EXACT remaining polynomials are

    E1_res=2k'*B2+h'*B1-h*B1'-2f*B0'-u,
    E0_res=k'*B1-h*B0'-1,                     (12)

where B_j are the reconstructed coefficients of B*. These are respectively the t^1 and t^0 coefficients of the full target difference. They are not Euler compatibilities and are not presumed zero. In particular the constant target1 survives the entire elimination. Their S-degree bounds are6r+2 and7r+2, respectively: in the first, each product has bound6r+2; in the second each has bound7r+2. Thus requiring EVERY coefficient of BOTH polynomials in (12) is exactly equivalent to requiring the whole Jacobian after reconstruction. No row has been replaced by a leading term, a residue alone, or the consistent initial ODE.

## 7. A smaller COMPLETE polynomial presentation

Fix r, and take the independent variables

    u,ell;
    d_0,...,d_r;
    v_0,...,v_(2r);
    k_1,...,k_m;
    omega.

Define d,v,k by these coefficients with k0=0; form A by (3); reconstruct B* by (5), taking beta=gamma=0 and B5=S^2. Let

    a=k_m, b=[S^n]B0*.

Both are specified polynomials in the displayed variables; b is NOT an extra free variable. Define the ideal L_r over Q by EVERY coefficient of both residuals (12), and

    omega*a*b-1.                               (13)

There are2+(r+1)+(2r+1)+(3r+1)+1=6r+6 variables. The residual envelopes have(6r+3)+(7r+3) scalar slots, and the guard adds one, giving at most13r+7 rows. Zeros or dependencies may reduce the number of nonzero rows; no builder or actual row enumeration has run.

This is a literal finite polynomial definition: the fixed diagonal inverses in (5) are coefficientwise rational maps, with no parameter-dependent pivot or branch. In particular every B_j is an explicitly defined polynomial in the input coefficients. Giving degree one to every independent variable, f has degree<=1, h degree<=2 and k degree<=1. The recurrence gives coefficient-degree bounds1,2,3,4,5 for B4,B3,B2,B1,B0 respectively. Consequently the two residual rows have coefficient degrees at most6 and7; a*b has degree at most6 and the guard omega*a*b-1 has degree at most7. These are rigorous upper bounds on algebraic degree, not measured sparsity, coefficient size, expression size or solver time. Eliminating bilinear variables can still make a computation worse.

Here is the exact equivalence over EVERY characteristic-zero field:

1. From a complete original compact point, its leading t constants are nonzero by the accepted gate. Normalize them as in section2, translate A to k0=0, and remove beta*A+gamma from B. Its mate is now precisely B*. The retained leading coefficients a,b are nonzero, the two residuals vanish, and omega=1/(ab) gives a point of L_r.
2. From any point of L_r, (3) and sections4–6 give polynomials A,B* with all bounds, BOTH complete inverse conditions, and full Jacobian Delta. The guard says a,b are nonzero. Set

       A_original=A/a, B_original=B*/b,
       c_original=1/(a*b), eta_original=a*b.

   This restores BOTH original monic top powers, retains the bounds and inverse conditions, and gives exactly [A_original,B_original]=c_original*Delta with eta_original*c_original=1. Thus it is a complete original compact point, not merely an ordinary receiver point or a formal initial.

Only existing nonzero field scalars were divided; no field extension, root choice, parameter specialization, coordinate dilation or source monicity loss is hidden. The maps are existentially equivalent with explicitly recorded output scalings/translations/shear; they are not asserted to be one-to-one on pairs before quotienting those gauges. The construction is compatible with scalar extension.

By the accepted16q compact contract, any characteristic-zero field point of L_r therefore reconstructs a Keller non-automorphism of EXACT ordinary degrees28m,28n, with the contract's named classical automorphism-theorem import. Properness of L_r over Q would give such a point over Qbar; a nonzero finite Q-algebra point satisfying every residual and guard would also suffice by passage to a residue field. No rational-point requirement is added. No such point, properness or unit is established. Conversely unitness for every r would exclude the accepted necessary F10 stratum, not prove JC2. The new presentation eliminates mate variables; it does not omit mate equations.

## 8. A uniform changed-object control: the last row really remains

The following is a manual symbolic family of inputs to the reconstruction, not a Keller source or a sampled computation. For every r>=1 take

    u=ell=0, d=0, v=S^(2r), k=S^m.

Then f=0,h=1+S^(2r+1),a=1. Put

    C=(10r+3)/(6r+3), L=5m/(3m+1).

Equations (5) give directly

    B4=0,
    B3=C*S^(2r+2),
    B2=L*S^(m+1).

Indeed the respective nonzero forcings for the last two are -(10r+3)S^(2r+2) and -5m S^(m+1), and their Euler eigenvalues are -(6r+3) and -(3m+1). B1 is the uniquely defined polynomial from j=1; its full formula is not needed for the check below. Since f=0, Q0 does not involve B1. Its exact two terms are

    Q0=L*(m+1)*S^m-(r*L+3m*C)*S^n,

because -2h'B2+hB2'-3k'B3 has those coefficients. Therefore

    B0= -L*(m+1)/(3m)*S^m
         +(r*L+3m*C)/(3n)*S^n.                 (14)

In particular b=(rL+3mC)/(3n) is a NONZERO rational number: all its displayed integer numerators and denominators are positive for r>=1, hence it remains nonzero in every characteristic-zero field. Taking omega=1/b satisfies the full top-product guard. All upper Jacobian rows t^7 through t^2, both boundary conditions and all degree/nonzero-top obligations hold, by the reconstruction proved above.

But m>=4 and n>=7 imply k'(0)=B0'(0)=0. The constant term of the retained t^0 residual is consequently

    E0_res(0)=k'(0)B1(0)-h(0)B0'(0)-1=-1.

Thus the remaining low equation is genuinely nonautomatic even on the guarded eliminated system. Dropping it would produce false complete-system candidates with correct upper equations and actual leading-degree shapes. This does not prove the retained low equations are inconsistent; it proves that the elimination has reached a real remaining compatibility problem rather than an automatic identity. Dropping the top-product guard would independently permit the source-degree collapse which section2 explicitly forbids.

The other useful negative scope control is built into (11): fixing B without allowing beta*A+gamma would artificially remove honest mates, while allowing arbitrary functions beta(S),gamma(S) is NOT licensed by the Euler kernels. The kernel scalars are constants of K, not extra coefficient polynomials. No fixed-A or first-order deformation failure is being promoted to a whole-system exclusion.

## 9. Decision, limitations and completion

Outcome: PROVED NEW PRESENTATION at the literal complete compact-system scope, pending independent review. The root Euler candidate is valid, and the extra boundary cancellations remove both apparent resonance constraints. The precise first nonautomatic obligations are the two full low residual polynomials (12); the constant residual has the explicit uniform negative control above. This is not just renaming the same number of unknown coefficients: all B coefficients and three honest additive/shear gauges are removed, while the two highest S coefficients remain guarded rather than normalized twice.

No full F10 exclusion, source point, ideal decision or measured acceleration follows. The source's consistent initial ODE is neither contradicted nor used as a lift. The algebraic degree increase and potential expression growth must be measured before any computational claim. This report authorizes no builder, solver, new gauge, descendant or review launch.

Timing/read scope: root invitation approximately11:23UTC, first exact local start and before-read pin check11:24:01UTC; conservative controlling stop11:48UTC, earlier than11:50. Exactly the three allowed reports were read WHOLE after their hashes matched. Only their stated accepted scope is imported. No1110 blind or live/uncharged report, ledger, primary/provenance, protected tree or remote machine was read. All new algebra is manual, with ZERO mathematical subprocesses of ANY size; only metadata and own transactional publication ran. Source postpins and owned custody accompany the sealed report. All writers and metadata children are terminal at handoff.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only extraction; no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18944`.
- Body SHA-256:
  `d4b86cfddc19af79f8c503c047ad0d7c924dcbfecdcda08886e807ba2c3411dc`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
