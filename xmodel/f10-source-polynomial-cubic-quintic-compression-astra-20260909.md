# F10 actual-source polynomial cubic/quintic compression

2026-09-09. Pure factored proof; ZERO mathematical subprocesses. Basis `0d39df3c9fd69c939a8420c54d03228b9077777d`. **PROVISIONAL and conditional on the new coalesced-reference parent.** This is its single authorized child, not a descendant of the separated-cubic report.

## 1. Exact assertion and dependencies

Suppose an actual ordinary rectangular F10 source at the accepted 16k scope produces the normalized receivers A,B, with increasing exponents

    r=q+1>=1, m=3r+1, n=5r+2,
    [A,B]_(g,p)=c g, c!=0.

Assume coalescence and the conclusions of the PROVISIONAL coalesced-reference theorem. In particular, with field scalars ell=a2/3 and h=a1/3,

    z=p^2-g+ell p+h,
    R=p z^3-z^2+u z+v0,                         (1)

and, writing the entire outputs as A'(p,z), B'(p,z), their monomials p^i z^j satisfy ordinaryness, the parent's rectangles, and

    m i-r j<=m for A',  m i-r j<=n for B'.       (2)

The canonical homogeneous identity agrees with R_s^m through order seven; its scalar corrections start at fourteen and its remainder starts at j0=7q+9>7. Here j0 is a contact order, not the monomial exponent j in (2).

Then actual reverse-source polynomiality forces

    u=-h.                                       (3)

In the birational coordinates (R,t), t=1/z, both ENTIRE outputs become ordinary polynomials, denoted Ahat(R,t), Bhat(R,t), with exact t-degrees three and five. Put

    S=R-v0,
    Pi=t-u t^2+S t^3,
    Delta=1+u t-ell t Pi-t Pi^2.                 (4)

Their exact Jacobian is

    [Ahat,Bhat]_(R,t)=c Delta.                   (5)

Their coefficient bounds, including all lower terms, are

    Ahat=sum_{k=0}^3 A_k(R)t^k,  deg A_k<=m-rk,
    Bhat=sum_{k=0}^5 B_k(R)t^k,  deg B_k<=n-rk.  (6)

The coefficients of R^m and R^n are exactly one. Hence the actual ordinary degrees in (R,t) are m,n, not three and five unless one means degree in t alone. The leading t-coefficients are exactly C0(R-v0), D0(R-v0)^2, with C0 D0=c!=0.

This is a full-polynomial compression, not a formal initial or finite jet. It is a necessary construction from the stated actual source. It does not prove existence, give a solution of any coefficient ideal, or turn the new pair into a constant-Jacobian pair. The finite inverse-polynomiality conditions are retained in section 7.

Scientific inputs were pinned BEFORE their WHOLE reads:

* PROVISIONAL `xmodel/f10-coalesced-source-reference-coordinator-20260909.md`, SHA256 `e87e5133a0072c309b6acdc4ab692b07bc4f6f545214c37df39a3042edf1ef70`.
* ACCEPTED 16k `xmodel/f10-all-parameters-source-interface-astra-20260909.md`, SHA256 `cc6edcb767bd22bddcdbe7dd89cfe1cfd260f66b145122889d50edd585c7c021`.
* Accepted source gate `xmodel/f10-all-parameters-source-gate-fable5-20260909.md`, SHA256 `9dc342bdd00a4fc7e1a22d5540a4544962acf7eb2f699fc4ae2e93bdb1fb0052`.

No primary/provenance path named by these reports was followed. No pending parent gate, separated gate, peer report, or mutable canonical entry was read. Accepted interiors are imported at their stated scope, not independently re-proved here. The parent reference and full bounds are conditional premises throughout.

## 2. The normalized receiver really has a canonical ordinary source

This step uses actual source attachment, not just the receiver's two faces. Use different names for the 16k normalization constants to avoid confusion with r and u in (1). Its pre-normalization source map is

    u_old=g0^3 p0+lambda g0^2-r0,
    v_old=g0^-1,

where lambda!=0. The normalized receiver substitutes g0=kappa g, p0=mu p, with kappa*mu=lambda and mu^3=a0*lambda, and divides the outputs by their nonzero top scalars. Therefore

    u_old=kappa^3 mu (g^3p+g^2)-r0,
    v_old=kappa^-1 g^-1.

Set U=(u_old+r0)/(kappa^3 mu), V=kappa*v_old, and absorb the already licensed nonzero output scalars into the original polynomials. This is an invertible affine source change over the same finite coefficient extension as 16k. It gives ordinary polynomials P(U,V), Q(U,V) such that, after the explicit output swap if needed,

    A(g,p)=P(g^2(1+gp),g^-1),
    B(g,p)=Q(g^2(1+gp),g^-1).                    (7)

The inverse is exactly

    g=V^-1, p=V^3 U-V.                          (8)

The determinant of (U,V) with respect to (g,p) is +g. Thus [P,Q]_(U,V)=c. This sign already incorporates the choice of output order; c is nonzero but is not normalized to one. Equation (7) is a rational identity between actually supplied ordinary polynomials, not a claim that every receiver admits such P,Q.

For the weighted homogenization A_s=s^{7m}A(g/s^2,p/s), substitute

    g=V^-1, p=V^3 U-s^3 V.                     (9)

The source coordinates in (7) become U/s^7 and s^2 V. Consequently

    A_s|_(9)=s^{7m}P(U/s^7,s^2V),
    B_s|_(9)=s^{7n}Q(U/s^7,s^2V).               (10)

Both expressions are ordinary in U,V,s. Indeed the source expression has no negative V powers, while the receiver expression on the left is a polynomial in s with Laurent-polynomial U,V coefficients: substitution (9) introduces no negative s powers. Equality in the common Laurent ring proves the assertion. No assertion about a generic source's unverified degree bound is needed for this argument.

## 3. The one possible reference pole forces a scalar relation

Homogeneously (1) is

    z_s=p^2-g+ell s p+h s^2,
    R_s=p z_s^3-s^3 z_s^2+u s^5 z_s+v0 s^7.    (11)

Under (9), write z_s=-V^-1+E_s(U,V), where E_s is polynomial and E_s(U,0)=h s^2. The only possible negative V powers in (11) are obtained from the displayed pole and the constant term of E_s. The negative parts of the three potentially singular terms are respectively

    p z_s^3:       s^3 V^-2-3h s^5 V^-1,
    -s^3 z_s^2:   -s^3 V^-2+2h s^5 V^-1,
    u s^5 z_s:    -u s^5 V^-1.

There is no other pole. Thus

    R_s|_(9)=Rpoly(U,V,s)-(u+h)s^5/V.           (12)

At s=0 the polynomial part is the nonzero expression

    R0_source=U(U^2 V^7-1)^3,
    R0_source(U,0)=-U.                          (13)

All coefficients of orders below five in (12) are ordinary. Since the scalar reference corrections start at fourteen and the full remainder starts above seven, the coefficient of s^5 in A_s equals that in R_s^m, even after (9). Substitution does not lower s order. Its possible simple pole has residue

    -m(u+h)(-U)^(m-1).

Equation (10) says this residue vanishes identically. Characteristic zero and the polynomial domain force u+h=0. This proves (3), and (12) now proves that the ENTIRE reference R reverses to a polynomial R_source(U,V). No saturation, parameter inversion, generic U value, or dropping of a source stratum was used. The proof uses actual source ordinaryness; it cannot be inferred from the receiver's bracket alone.

## 4. First finite bound: Laurent degrees at most three and five

On z!=0, the rational inverse to (R,z) is

    p=(R+z^2-u z-v0)/z^3=Pi(R,t), t=1/z.

Thus A',B' give finite Laurent polynomials in k[R,t,t^-1]. A monomial p^i z^j becomes Pi^i t^-j, whose highest t degree is 3i-j (when i>0 its leading coefficient is S^i). Negative t powers are not yet discarded.

For A, (2) says

    r(3i-j)+i<=3r+1.

If i>=1 this implies 3i-j<=3; if i=0 the degree is -j<=0. For B the corresponding bound is

    r(3i-j)+i<=5r+2.

For i>=2 it gives 3i-j<=5; for i<=1 the degree is at most three. Therefore the entire Laurent outputs have t degrees at most three and five, irrespective of cancellations.

The maximum-degree slots are unique. For A, 3i-j=3 together with (2) forces i=1,j=0. For B, 3i-j=5 forces i=2,j=1. The parent's exact negative-weight faces are

    p C(T), p^2 z D_ode(T), T=p^r z^m,

where C,D_ode are monic of degrees three and five and satisfy

    n T C' D_ode-m T C D_ode'-C D_ode=-c.

At T=0 this gives C0 D0=c!=0. Accordingly the exact leading Laurent t-coefficients are

    [t^3]Ahat=C0 S, [t^5]Bhat=D0 S^2.            (14)

They are nonzero polynomials, so these are actual t degrees. A specialization R=v0 can lower the degree of a fiber polynomial; it does not alter the degree of the full two-variable polynomial and no such specialization is imposed.

## 5. Source ordinaryness removes EVERY negative t power

Use u=-h. From (1) and (4),

    p=Pi,
    g=Pi^2+ell Pi-u-t^-1=-Delta/t,
    V=g^-1=-t/Delta.                            (15)

Delta is an ordinary polynomial in R,t, and Delta(R,0)=1 identically, including R=v0. The source coordinate U in (7) becomes

    U=Delta^2/t^2 * (1-Delta*Pi/t).              (16)

Here Pi/t=1-u t+S t^2. The constant term of Delta*Pi/t is one and its linear coefficient is zero: the +u t in Delta cancels the -u t in Pi/t. Hence its difference from one is divisible by t^2 in k[R,t]. Equation (16) is an ORDINARY polynomial in R,t, not just a rational function regular at a generic point.

By (7), the full outputs belong to k[R,t,Delta^-1]. By section 4 they also belong to k[R,t,t^-1]. These rings have intersection k[R,t] inside k(R,t), because t is prime and Delta is coprime to t. Explicitly, if a Laurent polynomial had a negative t order, multiplication by any power of Delta, whose residue modulo t is one, could not remove that order. This contradicts its expression with denominator a power of Delta only.

Thus Ahat and Bhat are ordinary in BOTH R and t, with no retained or silently omitted negative row. The argument proves regularity along the entire divisor t=0, rather than just along a generic reference fiber. It uses the full actual-source P,Q and does not replace A by a polynomial in R.

## 6. Exact Jacobian and all coefficient-degree bounds

The polynomial change (g,p)->(p,z) has determinant +1, so the parent's full bracket is c g. The rational change (p,z)->(R,t) has determinant

    R_p t_z-R_z t_p=z^3*(-z^-2)=-z.

Since g=-Delta/t and z=1/t, the chain rule gives (5) with the PLUS sign. All terms of Delta in (4) remain. In particular its highest t term is -S^2 t^7, so Delta is not constant. As a useful independent sign check, (14) gives the t^7 coefficient of the Jacobian as

    5(C0 S)'(D0 S^2)-3(C0 S)(D0 S^2)'
       =-C0 D0 S^2=-c S^2,

exactly the coefficient in c Delta. This is a single factored coefficient calculation, performed by hand, not an expansion of either full output.

Give R weight one and t weight r. The polynomial Pi has weight m=3r+1, with unique leading term R t^3; its other terms have smaller weight. Consequently each Pi^i t^-j has maximum weight at most mi-rj. Applying (2), then the polynomiality just proved, gives precisely (6). The bounds are on every coefficient polynomial, not only on the two exposed faces.

The associated graded substitution p->R t^3, z->t^-1 is injective on Laurent monomials: (i,j) maps to (i,3i-j). Thus no top-weight cancellation was assumed away. It transports the parent's exact faces to

    ell_(1,r)(Ahat)=R t^3 C(R^r/t),
    ell_(1,r)(Bhat)=R^2 t^5 D_ode(R^r/t).         (17)

Both right sides are ordinary polynomials: the degrees of C,D_ode are three and five. Monicity yields the exact terms R^m,R^n with coefficient one. Because r>=1, total degree is bounded above by this positive weighted degree, while R^m,R^n attain it. This proves the actual total degrees m,n and completes the stated compression.

## 7. Retained inverse obligations and an exact ring boundary

No coordinate map here is asserted to be a polynomial automorphism of the whole receiver plane. The inverse t=1/z is rational and its finite boundary must be retained. For a proposed small polynomial pair, the first inverse expressions are

    A'(p,z)=Ahat(p z^3-z^2+u z+v0, z^-1),
    B'(p,z)=Bhat(p z^3-z^2+u z+v0, z^-1).        (18)

They must have every negative z coefficient equal to zero. Then substitute z=p^2-g+ell p-u and require the specified receiver support, both exact normalized faces, and any claimed canonical/coalesced constraints. Merely imposing (5)-(6) does not supply these conditions.

There is a useful exact simplification, but not a lost lift condition: once (3) and polynomiality in (18) hold, actual reverse ordinaryness follows by a second intersection argument. The reconstructed receiver is polynomial in g,p, so (8) gives an element of k[U,V,V^-1]. On the other hand R_source is polynomial by (12), and

    z_source=-V^-1+polynomial(U,V),
    t_source=-V/(1-V*polynomial(U,V)).

The denominator is one modulo V. Thus any polynomial Ahat(R,t) substituted there is regular at V=0; intersecting with k[U,V,V^-1] removes all negative V powers. The same holds for Bhat. This establishes, in the fixed common rational function field, the ring identity

    k[g,p] intersection k[U,V]
      = k[p,z] intersection k[R,t],              (19)

under the displayed identifications and u=-h. The forward inclusion is section 5, which did not use the degree bounds for regularity; the reverse inclusion is the present argument. It is not the assertion that k[R,t] alone equals the full-source ring.

The rational maps also recover the constant source bracket c from (5) if all inverse ordinaryness conditions are satisfied. This observation does not license a counterexample endpoint from a small pair alone: exact source support, faces, degree/standard-chain attachment, and the other hypotheses of whatever endpoint is claimed must still be checked. No complete coefficient ideal has been emitted or solved here.

## 8. Manual controls, field scope, and stop

All controls below are hand-checkable changed objects or hypotheses; none is claimed to be a Keller pair.

* Dropping reverse ordinaryness: the receiver polynomial z transforms to t^-1, so receiver polynomiality and a rational reference fiber do not eliminate positive z powers. Its reverse has the actual pole -V^-1. This is precisely the boundary used in section 5.
* Changing the scalar relation: if u+h!=0, (12) has a nonzero pole and the s^5 residue in A_s cannot be canceled by a remainder beginning after seven. Likewise the linear term of Delta*Pi/t fails to cancel if the g constant is h rather than -u. Source ordinaryness and the reference-contact order are both load-bearing.
* A rational reference fiber does not make an output a function of R alone: the actual global polynomial p reverses to V^3 U-V and becomes Pi(R,t), which is nonconstant in t. The proof retains this dependence and all higher output coefficients.
* Replacing the target by a constant deletes the actual term -c(R-v0)^2 t^7 and contradicts the leading-coefficient calculation in section 6. The compressed pair is not a Keller pair in its new coordinates.
* Keeping a small polynomial pair but omitting (18) admits t itself, whose receiver inverse is z^-1. Thus the inverse-polynomiality equations are indispensable even though the forward compressed outputs are ordinary.

The inherited finite scalar extension from 16k suffices; these new steps introduce no additional roots. Division uses only the nonzero normalization scalars already licensed, characteristic-zero integers, and the explicitly localized coordinate boundaries. No parameter value R=v0, u=0, ell=0, or v0=0 is removed. Statements are over fields; a general nilpotent parameter-ring equivalence is not asserted because the parent is a field theorem.

There is no solver/runtime claim. The result is the full-source-attached cubic/quintic representation (5)-(6), with the inverse obligations above, conditional on the parent reference theorem. It does not exclude coalescence, F10, an actual numerical degree pair, or JC2. No further child or follow-on computation is authorized. All mathematical reasoning was manual; only hashing, documentary reads, own collision checks and existing transactional publication were executed.

## OPEN(S) RAISED

None. The parent's review dependency remains explicit, not replaced by a new open-problem identifier.

## COLLISIONS

status: EMPTY

- NONE — own-only raised-OPEN check, no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15867`.
- Body SHA-256:
  `051b0ed13123a8b97d2c1df799f56c36f40bbfa87d21bcb1755da68130b7eac9`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
