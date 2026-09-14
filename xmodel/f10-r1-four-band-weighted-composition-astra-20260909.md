# F10 r1 four-band composition and two-coordinate field-existence compression

2026-09-09. NEW/PROVISIONAL integration theorem; independent review is still required for this report. First action18:07:08UTC; controlling stop18:22:08UTC. ZERO mathematical subprocesses of any size. Basis0d39df3c9fd69c939a8420c54d03228b9077777d is provenance only.

## 1. Result, dependencies, and the corrected third band

There are two distinct conclusions.

A. The four specified band eliminations compose triangularly into an exact quotient-ring presentation over B[s,s^-1][Y1,Y2] with at most11 scalar slots. Every original residual, complete mate, inverse condition, leading coefficient and guard is preserved by explicit back-maps. No circular dependence or new gauge is introduced.

B. A further weighted construction gives a field-existence presentation in TWO coordinates X,Y over B, with10 polynomial equations and one required invertible polynomial h0(X,Y). A point reconstructs a full guarded r1 point after adjoining a root of eta^3=h0, a field extension of degree at most3. Conversely a full point yields a point of this presentation after an extension of degree at most3. Over an algebraically closed characteristic-zero field this is exact nonemptiness equivalence. It is NOT an unqualified quotient-ring isomorphism, a same-field rational-point assertion, or an s=1 gauge.

No polynomial rows, source powers, matrices or coefficient arrays were executed or emitted. The equations below are finite mathematical definitions via the accepted recurrences. Counts are envelopes, not dimensions, independence, measured sparsity or speed. There is no point, ideal decision, source exclusion or execution authority.

The initial ten science inputs were current-pinned before WHOLE reads: accepted16r,17b producer/gate, first-band producer/gate, second-band producer/gate, third-band producer/correction gate, and the then-provisional fourth-band producer. Root subsequently released the TERMINAL fourth-band gate (SHA005c9ce2e36d9c6521070707300028bd72062290fd5befbd5be5554cc1cf901d), with unchanged producer scope. Its hash was checked before its WHOLE read; it is the only added input. Thus all four band conclusions used here have their accepted review, while this NEW integration remains provisional. No live gate was read. Exact eleven paths/hashes/bytes are in PINS.json.

The third-band producer is consumed ONLY WITH its correction gate d11175469b643e6dc119ca9c16f19856b132c7f6b585c5b495d1c6e3fbad213a. In particular its actual forcing is

    N=-2theta^5-W-y_old*(theta D'-7D),
    N_i=-W_i+(7-i)*y_old*D_i, 0<=i<=4.       (1)

The printed shifted-index formula is not used. The theta^6 row vanishes because V4=0, not V3=0; V3=0 is the separate accepted mate gauge. The fourth-band derivative envelopes are <=4 and <=5, not assertions that either individual leading column entry is nonzero everywhere.

## 2. Exact triangular composition over the original leading ring

Let Lambda=B[s,s^-1] be the exact accepted17b ring, with B=Q[v]/p(v), the full degree-seven algebra rather than a selected factor. Its fixed elements w,L,f5 and their inverses are as accepted. The leading coefficients and guard are

    F=v/(w*s), H=1/(w*s^2), a=1/(w*s^3),
    b=1/(s^5*f5), omega=w*s^8*f5.             (2)

Use theta=t/S, C=theta^3+Ftheta^2+Htheta+a and D indexed by theta powers, D5=1,D0=b. The entire leading equation is 4CD'-7C'D=-theta^7 in Lambda[theta]. There are initially eight polynomial coordinates u,ell,d0,v0,v1,k1,k2,k3 and17 retained residual slots.

Define Z=(d0,v1,k3)^t. The first-band producer specifies its finite recurrence beta^(1), its completed unit matrix, and read-back rho1. Its exact maps give

    Z=beta^(1)*Y1, Y1=rho1(Z),                (3)

solving precisely [S^7]E1,[S^8]E0. Their coefficients contain none of u,v0,k2,k1,ell, so these stay free. Its kernel coordinate is not a gauge.

For the second band write q=-u,l=v0-uF,k=k2 and U2=(q,l,k)^t. Use the second producer's specified completed unit matrix N2 and ACTUAL quadratic forcing c2(Z), obtained from the entire preceding mate band. Its maps are

    U2=N2^-1*(-c2,1(Z),-c2,0(Z),Y2)^t,
    Y2=rho2(U2), u=-q, v0=l-Fq, k2=k.        (4)

Here rho2 is defined from the homogeneous mate response, exactly as in that producer. N2 depends only on Lambda, not on Z or any remaining parameter. Consequently (4) remains an invertible affine coordinate change after substituting(3); its determinant remains the SAME unit. This solves [S^6]E1,[S^7]E0 without inverting a first-band equation. Its particular part is quadratic in Z, and beta^(2)Y2 is its homogeneous part. Neither k1 nor ell enters it.

After(3),(4), use the CORRECTED third-band forcing(1), the exact whole earlier mate pieces, and its specified left inverse lambda3. Its pair of rows has form h3*k1+c3, with c3 independent of k1 and ell, and lambda3(h3)=1. Set

    k1=-lambda3(c3),
    Psi3=-h3,0*c3,1+h3,1*c3,0.              (5)

Retain Psi3=0. This replaces [S^5]E1,[S^6]E0 by one compatibility and removes k1. All other rows are substituted, not discarded. The correction changes c3 and therefore is essential even though the homogeneous left inverse was correct in the original producer.

Finally the fourth-band full response gives rows Acol*ell+P and Bcol*ell+Q. Its fixed leading-ring left inverse lambda4,A,lambda4,B remains valid after(3)-(5). P,Q are the ENTIRE ell=0 rows with all previous substitutions, not leading approximations. Put

    ell=-lambda4,A*P-lambda4,B*Q,
    Psi4=Bcol*P-Acol*Q.                      (6)

Retain Psi4=0. Neither the first/second maps nor(5) depends on ell. Thus the last substitution cannot change an already-used map or compatibility. Conversely each step has its specified inverse; quotienting successively and adjoining the remaining variables commutes with those maps. This proves triangularity and the composite quotient-ring isomorphism, over every Lambda-algebra.

The result is the presentation over Lambda[Y1,Y2] with exactly the following formal slots:

    [S^0..S^3]E1, [S^0..S^4]E0, Psi3, Psi4. (7)

There are4+5+2=11. The eight original band slots were replaced by two compatibilities, so17-8+2=11; the eight coordinates were reduced by2+2+1+1 to two. No assertion of nonzero/independent slots follows. Every whole B_j is still the accepted16r recurrence evaluated at the composite map. That recurrence preserves the complete inverse-polynomiality conditions and beta=gamma=k(0)=0 gauges; the exact leading read-back(2) restores its top guard. This is a composition of proved all-row maps, not a projection retaining only the high equations.

## 3. An invertible change of scale, with the exact target

To expose a useful grading, introduce new notation

    tau=s*t, U=s*u, Dcal(S)=s*d(S),
    Vcal(S)=s^2*v(S), Kcal(S)=s^3*k(S),
    E=s^3*ell, z=s^2,
    Ahat(S,tau)=s^3*A(S,tau/s),
    Bhat(S,tau)=s^5*B(S,tau/s).               (8)

Here z is an auxiliary scalar, NOT the earlier inverse-source coordinate, and E is a scalar, NOT either residual E0/E1. Dcal is distinct from the leading quintic D(theta). The accepted leading coefficients become the elements

    Fbar=v/w, Hbar=1/w, abar=1/w, bbar=1/f5  (9)

of B, independent of s. The source boundary formula becomes exactly

    Ahat=S*tau^3+(S*Dcal-U)tau^2
                    +(z-U*Dcal+S*Vcal)tau+Kcal,
    Pihat=z*tau-U*tau^2+S*tau^3.             (10)

These equations follow term by term from accepted16r, not from a free coefficient ansatz.

The determinant factor is important. Differentiating(8),

    [Ahat,Bhat]_(S,tau)=s^7*[A,B]_(S,t)|t=tau/s.

Moreover Pi(S,tau/s)=Pihat/s^3. Therefore the ENTIRE target becomes

    [Ahat,Bhat]
      =s^7+U*s^5*tau-E*tau*Pihat-tau*Pihat^2. (11)

For example the original term u*t contributes s^7*(U/s)*(tau/s)=U*s^5*tau. All signs and powers in(11) are fixed by this calculation. No coefficient field extension is needed for(8); s was already a unit. This is not a source symmetry preserving the old target verbatim.

## 4. The normalized two coordinates and polynomial homogeneity

Define

    x=s^8*Y1, y=s^8*Y2.                     (12)

These exponents are justified by the read-back coordinates, not guessed from the variables' names. If theta=t/S and vartheta=tau/S, then

    Cbar(vartheta)=s^3*C(vartheta/s),
    Dbar(vartheta)=s^5*D(vartheta/s).

The first subleading A and B polynomials similarly acquire factors s^3 and s^5. Thus their read-back polynomial 4CV-7DU acquires factor s^8 and has constant coefficient x. The second producer uses the homogeneous mate response in rho2; exactly the same scaling applies to it, giving constant coefficient y. Consequently the normalized first and second maps are literally the same recurrences as(3),(4), but with Cbar,Dbar, their fixed coefficients in B, and coordinates x,y. No arbitrary rescaling of their particular solutions has occurred.

Now regard z as a separate polynomial indeterminate temporarily and assign

    wt(S)=wt(tau)=wt(x)=1,
    wt(y)=2, wt(z)=3.                        (13)

The four maps give polynomial coefficients in B[x,y,z], with no z inverse:

- The first normalized coefficients (Dcal0,Vcal1,Kcal3) are linear in x, hence weight1. Its completed matrix is over B.
- The second normalized coefficients (-U,Vcal0-U*Fbar,Kcal2) are the quadratic forcing in x plus beta^(2)*y, hence weight2. Its completed matrix and inverse lie in B and do not involve x,y,z.
- In the normalized third band the linear-tau coefficient is z-U*Dcal0, weight3. Every earlier forcing term is of weight3 (first times second bands); the coefficient of the actual target -2z*S*tau^5 has weight3. The corrected polynomial N and its coefficient rule transport exactly. The normalized third-band left inverse has coefficients in B, so Kcal1 is weight3 and its normalized compatibility Phi3 is homogeneous of weight3.
- The fourth-band target terms are -U^2*tau^5-E*S*tau^4 at ordinary source weight5. Its full forcing after the previous maps has parameter weight4. The normalized column and the chosen Gram-adjugate left inverse have coefficients in B. Hence E is weight4 and its normalized compatibility Phi4 is homogeneous of weight4.

This explicitly shows the weights of every free or reconstructed coefficient of Ahat: the coefficient of S^i tau^j has parameter weight4-i-j. The forms(10) are homogeneous of total weight4, and Pihat is homogeneous of weight4. The normalized compatibilities differ from their original(5),(6) by powers of the already-unit s (and possibly the fixed sign convention in(6)); they define the same zero rows. In fact with their displayed determinant conventions both may be taken as s^10 times the corresponding original compatibility. No vanishing or invertibility of an individual column entry is used.

The entire mate is homogeneous of weight7. Here is a proof that includes the lower mate rather than just four bands. In the tau-degree-at-least-two upper equations of(11), neither s^7 nor U*s^5*tau occurs. Their target is solely

    -E*tau*Pihat-tau*Pihat^2,

which is homogeneous of weight9. Every upper Euler operator j-3S*d/dS preserves coefficient weight, and its nonresonant inversions divide fixed rationals. Starting at Bhat_5=S^2, descending induction therefore gives coefficients of weight7-j in Bhat_j(S), with the corresponding parameter weights for each S coefficient. Both resonance gauges are zero, hence homogeneous. Their automatic compatibilities remain identities: after substituting z=s^2 they are the accepted identities under(8), and B[z]->B[s,s^-1], z->s^2, is injective (distinct nonnegative powers map to distinct Laurent monomials), so those polynomial identities hold before that substitution as well.

This also proves that no odd residual power of s or hidden z denominator occurs in the reconstructed polynomials. The finite recurrences use only B-units after normalization; all variable divisions are avoided. The nine zero equations below inherit their weights from the full source, not merely from the first four bands.

## 5. The eleven equations after scaling

After the normalized composite reconstruction define the SINGLE polynomial

    Jhat=[Ahat,Bhat]+E*tau*Pihat+tau*Pihat^2.  (14)

Its total weight is9. Write

    H0(x,y,z)=[S^0 tau^0]Jhat,
    H1(x,y,z)=[S^0 tau^1]Jhat.

Thus wt(H0)=9, wt(H1)=8, and the reconstructed U(x,y,z) has weight2. These may be zero polynomials on some components; no nonvanishing is assumed before imposing the guard.

The nine homogeneous zero equations are the following exact polynomials G_i:

    [S^i tau]Jhat, i=1,2,3;
    [S^i]Jhat, i=1,2,3,4;
    Phi3, Phi4.                              (15)

Their respective weights are7,6,5;8,7,6,5;3,4. All tau-degree-at-least-two coefficients of Jhat were solved by the entire mate recurrence. The higher low-tau slots removed by the first two bands vanish identically; those replaced in the third and fourth bands are the specified leading-ring multiples of Phi3 and Phi4 under their invertible two-row transformations. Thus no higher low-tau slot is silently omitted. The remaining eleven equations are precisely

    G_i(x,y,z)=0 (nine slots),
    H0=s^7, H1=U*s^5, z=s^2, s invertible.    (16)

The relation z=s^2 is a defining substitution, not an additional unknown in the original11-slot ring. Formula(16) is exactly(7) under(8),(12), not a collection of necessary leading equations. In particular H0 and H1 are the ENTIRE constant-S low equations, retaining their original nonzero targets.

One can eliminate s from the enlarged presentation without choosing a square root:

    z*H1-U*H0=0, H0^2=z^7, z invertible,
    s=H0/z^3.                                (17)

Indeed (17) implies s^2=z and s^7=H0, since H0^2=z^7; also s^5=H0/z, giving H1=U*s^5. Conversely(16) implies(17). This step is an exact algebraic read-back over any coefficient ring with z a unit. It preserves the sign of s through H0, rather than silently identifying the two square-root choices.

The full equation H0^2=z^7 is NOT homogeneous for(13): its weights are18 and21. Consequently weighted scaling is NOT a symmetry of the complete guarded system. The next step is a finite-cover field-existence construction, not a quotient by an unproved symmetry.

## 6. Two coordinates, ten equations, and the finite cubic reconstruction

Put

    g_i(X,Y)=G_i(X,Y,1),
    h0=H0(X,Y,1), h1=H1(X,Y,1),
    ubar=U(X,Y,1).

Define the exact localized B-algebra

    Tsmall = B[X,Y,h0^-1]/
             (g_1,...,g_9, h1-ubar*h0).       (18)

This has TWO polynomial coordinates before localization and ten specified equation slots. If a literal polynomial guard variable xi is preferred, replace the localization by xi*h0-1; that encoding has three polynomial variables and eleven slots. No equations in(18) have been expanded or solved. A field-valued point of B is a choice of embedding of some residue field; the whole algebra B is retained in the presentation.

Forward reconstruction from a Tsmall point over any characteristic-zero field K: h0 is nonzero. Adjoin a root eta of eta^3=h0, obtaining a field extension of degree at most3. Set

    mu=eta^2, s=eta^3=h0,
    z=eta^6=mu^3,
    x=eta^2*X=mu*X, y=eta^4*Y=mu^2*Y.       (19)

All nine G_i vanish by homogeneity. The same homogeneity gives

    H0(x,y,z)=mu^9*h0=eta^21=s^7,
    H1(x,y,z)=mu^8*h1=eta^19*ubar,
    U(x,y,z)=mu^2*ubar=eta^4*ubar.

Thus H1=U*s^5 and z=s^2, proving every equation(16). This verifies the exact target, not just its square. Use the normalized composite back-map, then invert(8),(12):

    Y1=x/s^8, Y2=y/s^8,
    u=U/s, d=Dcal/s, v=Vcal/s^2,
    k=Kcal/s^3, ell=E/s^3,
    A(S,t)=s^-3*Ahat(S,s*t),
    B(S,t)=s^-5*Bhat(S,s*t).                 (20)

The result is a full point of the accepted17b/16r presentation, with all original rows and inverse conditions, and omega=w*s^8*f5. Restoring the accepted output factors A/a and B/b recovers exactly the original compact-source guard and endpoint. No new same-field claim is made if eta is absent from K.

Conversely take a full point over K. By PartA and(8),(12), it gives(16). Adjoin a cube root mu of z=s^2, a field extension of degree at most3; set

    X=x/mu, Y=y/mu^2.

Homogeneity gives g_i=0 and

    h0=H0/mu^9=s^7/s^6=s!=0,
    h1=H1/mu^8=ubar*s=ubar*h0,
    ubar=U/mu^2.

Hence this is a point of(18). For an exact reciprocal cover check put eta=s/mu. Then

    eta^2=s^2/mu^2=mu,
    eta^3=s^3/mu^3=s=h0.

So(19) returns the original s,x,y,z, not merely a scaled equivalent target. No square-root choice or field embedding was silently discarded. Both directions preserve the original B-map under the finite extension, and allow every characteristic-zero residue field of B.

Therefore full guarded r1 field existence and Tsmall field existence are equivalent allowing finite field extension (bounded by3 in each displayed direction), and exactly equivalent over an algebraically closed field. This is NOT a same-K rational-point bijection, nor an assertion that the complete full ring is isomorphic to Tsmall. The cubic cover may split; only the existence of a root in a finite extension is used.

## 7. Controls, limits and cheapest meaningful verification

The corrected third coefficient rule is indispensable. The polynomial theta*D'-7D has theta^i coefficient(i-7)D_i, so substituting the old D_(i+1) formula changes the actual third-band particular solution while leaving its homogeneous rank unchanged. Rank alone does not validate the composite source map.

No circular elimination control: changing a lower coefficient ell cannot alter any of(3)-(5), because their exact source weights exclude it, whereas the full mate response to ell DOES enter lower rows. Thus the sequence is triangular but the final lower-row substitution cannot be omitted. Similarly Y1,Y2 are genuine kernel/read-back coordinates, not gauges to be set to zero.

Scale control: simply setting s=1 in the full source would force H0=1. Formula(18) instead retains arbitrary invertible h0, and reconstructs s=h0 with a cubic cover. Dropping h0 invertibility would allow a formal attempted reconstruction with s=eta=0, at which the original leading read-back and guard are undefined. No assertion that the ten equations actually have such a zero-h0 point is needed or made; it is the exact domain of the back-map. The weights18 versus21 in(17) provide an independent check that a naive full-system weighted quotient is not licensed.

Target-sign control: retaining only H0^2=z^7 but losing H0 in the formula for s would leave a sign ambiguity. The exact read-back s=H0/z^3 and H1=U*H0/z removes it and recovers the unsquared target. No reality or positivity of any coefficient field is assumed; the only Gram positivity imported from the fourth producer concerns a rational coefficient matrix.

Gained: a complete triangular11-slot quotient presentation, and a further TWO-coordinate localized ten-equation field-existence model with a fully specified finite reconstruction. Not gained: an expanded residual artifact, independent-equation count, point, properness/unit certificate, source exclusion, generic dimension, term/degree bound for the final rows, or measured acceleration. Accepted16r's actual source endpoint remains ordinary degrees112/196 for a full point, not a maximal-degree theorem or JC2 conclusion. Every classical import used for that endpoint stays at the accepted16r tier.

The cheapest subsequent discriminator, only under new independent authorization, is exact all-row read-back of the eleven composed slots and the ten slice equations plus guard, including the unsquared low target after(19),(20). No such computation is requested or performed here. Expression growth may offset the reduction in coordinate count. This report supplies no implementation, solver, descendant or launch authority.

## 8. Read scope and completion

The ten initial inputs and the single explicitly released terminal fourth gate were all current-pinned before WHOLE reads. All exact paths/bytes/hashes accompany this report. The fourth producer was provisional when the task began; its released same-scope gate changes only that dependency status. This NEW composition/scaling proof remains provisional. No other scientific body, live gate, peer, ledger, source artifact or code was read. No mathematical subprocess of ANY size, network, remote worker, process inspection, agent or shared/protected write occurred. Only documentary metadata, apply_patch and existing transaction tools were used. Own WHOLE and own-only raised-OPEN/collision checks precede the marker. All writers IDLE at handoff before the fixed18:22:08 cap.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only extraction; no corpus scan.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20761`.
- Body SHA-256:
  `12a3cf99230d8bd4394bc5d0cf4f02e11b7be54c55527754f58c92e080d243ab`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
