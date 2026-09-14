# Full-plane hypersurface radial pinching control

MANUAL CO-RESEARCH / EXPLICIT COUNTEREXAMPLE VERIFIED BY AUTHOR, not FIRST or promoted evidence. The example satisfies the complete relaxed package, including the affine-three-space hypersurface condition, but is nonnormal.

First action 2026-09-12 14:47:15 UTC. Original reserve 15:00 UTC / hard stop 15:03 UTC, never reset. Exactly COORDINATION.md and TASK.md, current-pinned before fresh WHOLE reads. One clipped combined output was recovered and TASK reread after the completed protocol read. No scientific execution or external input.

## Exact object and question

Over C let R=C[x,y], z=x-1, T=zy+3, c=yz^2+3z-1, and U=z^2, V=zc, W=(1+3z)y+9. Test B=C[U,V,W] inside R as a nonnormal hypersurface with finite birational everywhere-unramified normalization, globally free dualizing module, and a global Kähler lift of alpha=(x dy-y dx)/2. No Keller pair is supplied.

## 1. Exact algebra and the full hypersurface relation

Direct substitution gives

    c=UW-3V-1,   cz=V,   z^2=U,
    y=A-3Wz,    A=(1+9U)W-27V-9 in B.

For the last equality, (1-3z+9z^2)(1+3z)=1+27z^3; subtracting 27V+9 cancels precisely the extra y and constant terms. Therefore R=B[z]=B+Bz, a finite B-module. Since c is a nonzero polynomial, z=V/c and the formula for y show Frac B=Frac R. As R is integrally closed, it is exactly the normalization: an element of the common field integral over B is also integral over R and hence lies in R.

For independent indeterminates u,v,w put

    P(u,v,w)=v^2-u(uw-3v-1)^2.

It vanishes on (U,V,W). Its coefficients as a quadratic in w are

    -u^3,  2u^2(3v+1),  v^2-u(3v+1)^2.

They have greatest common divisor 1: a common irreducible factor would divide u, but the last coefficient is v^2 modulo u. Over C(u,v), a root w would make v/(uw-3v-1) a square root of u. This is impossible because the u-adic valuation of u is 1. Conversely adjoining a square root supplies both roots. Thus the quadratic is irreducible over C(u,v), and Gauss's lemma makes P irreducible in C[u,v,w].

The image B has dimension 2, since it has the same fraction field as R. Hence the prime kernel of C[u,v,w] -> B has height 1. It contains the irreducible P, so it is exactly (P). This proves the full presentation, not just a vanishing relation:

    B = C[u,v,w]/(P).

In particular B is a two-dimensional Cohen–Macaulay domain with a globally free canonical dualizing module, by hypersurface adjunction over the polynomial ring. Neither normality nor rational singularities is assumed in that adjunction statement.

## 2. The complete pinching and exact conductor

Because c and cz belong to B and R=B+Bz, one has cR contained in B. Set D=V_R(c). In R/(c), the relation z(zy+3)=1 makes z invertible. Taking t=T=z^{-1} gives the exact isomorphism

    R/(c)=C[t,t^{-1}],
    (x,y,z)=(1+t^{-1}, t^2-3t, t^{-1}).

The inverse is t=zy+3. The embedded curve is smooth: c_y=z^2 is a unit on D. The residues of U,V,W are respectively t^{-2},0,t^2, so

    B/(cR)=C[t^2,t^{-2}] inside C[t,t^{-1}].

This also proves B is the entire inverse image of that even subring. Indeed, if r has even residue, choose b in B with that residue; then r-b belongs to cR contained in B. It is not only a necessary matching condition.

Consequently the restriction of the normalization to D is the free two-sheeted map C* -> C*, t -> t^2. Its pairs are exactly t and -t; there are no fixed points because t is nonzero. Away from D, z=V/c shows B_c=R_c, so there are no additional identifications. The odd element T has residue t and therefore is not in B. Hence B is a proper, nonnormal subring of its normalization.

For exactness of the conductor, suppose rR is contained in B. Then both r and rT are in B. Writing their residues as q(t) and tq(t), both must be even. Thus q is even and tq is simultaneously odd and even; characteristic zero forces q=0. Therefore r belongs to cR. Together with the already proved reverse inclusion,

    I=Ann_B(R/B)=cR

as actual ideals, with no replacement by radicals or congruence truncations.

## 3. Everywhere unramified, including the apparent exceptional locus

On D, z is a unit and J(U,c)=2z^3, so dU and dc span source cotangents. Off D the map is an isomorphism. A stronger global check avoids any support argument. Differentiating V=zc and U=z^2, and using zT=c+1, gives the literal identity

    dz=(T/2)dU-dV+z dc.

Differentiating y=A-3Wz gives dy=dA-3z dW-3W dz. Since A,c are in B, these express both dz and dy in the R-span of differentials of B. Thus Omega_(R/B)=0 globally. The finite morphism is everywhere unramified; it is not asserted étale across its nonnormal target.

The target singular locus can also be checked without discarding U=0. Write C0=uw-3v-1. Then P_w=-2u^2 C0, P_v=2v+6u C0, and P_u=-C0^2-2uw C0. At u=0, P=0 forces v=0, C0=-1 and P_u=-1, so all such target points are smooth. Where u is invertible, (u,v,C0) are coordinates, P=v^2-u C0^2, and the singular locus is precisely v=C0=0, uw=1. Étale locally adjoining a square root of the unit u exhibits an ordinary transverse double surface. This confirms, rather than substitutes for, the exact nonnormality argument above.

## 4. Global Kähler descent: the module issue and a finite lift

On D, dx=-t^{-2}dt and dy=(2t-3)dt, so

    alpha|D=(t-3/t)dt
            = ((1-3t^{-2})/2) d(t^2).

Thus beta0=((1-3U)/2)dW in Omega_B^1 has the same image in Omega_D^1. This equality by itself is not the global lift; the following is the needed additional argument.

Let M be the image of Omega_B^1 in Omega_R^1. It is a B-module, not necessarily an R-submodule. The proved vanishing of Omega_(R/B) means every element of Omega_R^1 is a finite R-linear combination of differentials of B. After multiplying by c, every coefficient belongs to cR contained in B. Hence c Omega_R^1 is contained in M. For any a in R, ca lies in B and

    a dc=d(ca)-c da belongs to M.

The ordinary global conormal exact sequence for the quotient R -> R/(c) has kernel c Omega_R^1+R dc. Therefore its entire kernel lies in M. Since alpha-beta0 lies in that kernel, alpha lies in M. This is a statement about global modules on affine schemes, not local primitives whose gluing was left unchecked. It supplies an actual element beta of Omega_B^1. Naturality of the exterior derivative then gives pullback(d beta)=dx wedge dy.

A direct finite expression independently checks the conormal step. Define elements of R

    a=(9z+3-2T)/2,    k=3(y-3)-6zW.

Expanding the two coefficients of alpha-beta0 gives

    alpha-beta0 = a dc + c[((4y-9)/2)dz+z dy]
                = d(ca)+c[3(y-3)dz+2z dy].

Using the global expressions for dz and dy above, one possible beta is

    beta = ((1-3U)/2-6cU)dW + d(ca)
           +(ckT/2)dU - ck dV + ckz dc + 2V dA.

Every displayed coefficient is an element of B: those involving a,k,T,z are multiplied by c and therefore lie in the already proved conductor cR. Also A,c,ca are in B, so every differential written is a differential in Omega_B^1. No division by c, z, U, or a parameter occurs in this global lift. Applying the natural pullback map to Omega_R^1 recovers precisely alpha; injectivity of that map is not claimed. Thus tangential agreement has been upgraded to global Kähler descent in two mutually checking ways.

## 5. Global dualizing generator, volume factor and Euler failure

Hypersurface adjunction supplies a global free generator eta, whose rational expression on the appropriate smooth open is du wedge dv/P_w. Direct source differentiation yields

    J(U,V)=2z^4,     P_w(U,V,W)=-2z^4 c,
    eta|Frac(R) = -dx wedge dy/c.

The cancellation is in rational forms; it does not declare J(U,V) a unit. It remains valid as a rational identity at the locus z=0 where the original numerator and denominator both vanish. This agrees with the conductor cR under finite canonical duality and verifies the exact volume factor in the chosen generator.

For the residue sign, differentiate c=zT-1 and T=zy+3 to obtain

    dc wedge dT=(c+1) dx wedge dy.

Near D the factor c+1 is a unit. With dc first, the residue of (dx wedge dy)/c is dt. Under the actual identification t -> -t this becomes -dt, exactly the required opposite matching for an ordinary node. The residue of eta is -dt and obeys the same matching. Global freeness therefore survives this pinching; it is not merely local Gorensteinness.

For E=(x partial_x+y partial_y)/2, direct differentiation gives

    E(c)=[(z+1)(2yz+3)+yz^2]/2,
    E(c)|D=t-3/t.

This is a nonzero odd Laurent polynomial. The exact inverse-image characterization of B therefore proves E(c) is not in B although c is in B. Since its restriction to D is nonzero, E(c) is not in cR either. Consequently E(B) is not contained in B and E(I) is not contained in I; the reduced boundary is not Euler-invariant. The paired Euler values are opposite, generically nonzero. No assertion of nonvanishing at every point is needed or true.

## 6. Verdict, controls and exact limits

The explicit B is a proper nonnormal affine hypersurface in A3, is Cohen–Macaulay with globally free dualizing module, and has finite birational everywhere-unramified normalization from the entire A2. Its Kähler module contains a form pulling back to the specified radial alpha. It is therefore an exact counterexample to the proposed implication of this complete relaxed package to normality, even with the extra hypersurface condition, and to the accompanying Euler-stability implications.

Positive check: B=R has beta=alpha, the ordinary free canonical module, identity normalization and unit conductor. Negative check against a false Keller reading: the displayed pair (U,V) has Jacobian 2(x-1)^4, which vanishes on x=1, rather than a nonzero constant. Nothing supplies any pair f,g in B with J(f,g)=1 and a compatible beta=dH+f dg for H in B. A descended one-form is not a polynomial Darboux presentation. The report neither excludes all possible Keller pairs in B nor produces one; it is not a Keller or JC2 counterexample.

No source normality, invertibility, global novelty, descendant or FIRST claim follows. This is same-model co-research; a separate different-model FIRST is needed before promotion. The bounded quantity was this one explicit example, and it is resolved at the manual author-checked tier. No new mathematical OPEN or successor family is raised. Cheapest proposed next test is one focused manual hostile check of the exact ring and lift, planning 10 minutes UNMEASURED and not an execution authorization.

## Read scope and publication

Exactly two pinned bodies were read: fresh WHOLE COORDINATION.md and TASK.md. A combined-output clipping in COORDINATION lines 441-660 was recovered by a standalone full-range read, and TASK was then reread WHOLE. No old report, peer output, linked provenance, external source, corpus or protected tree was read. Standard Gauss's lemma, the conormal sequence and hypersurface adjunction were used at their explicit algebraic hypotheses, not newly researched or computationally tested.

All algebra and differential identities were derived manually. No scientific interpreter/helper/CAS/import/AST/syntax/test/fixture execution, network, worker or agent action occurred. Only inert text/hash/presence/clock checks, apply_patch and the existing administrative finalizer were used. The report, PINS and custody are own-only; TASK and all older artifacts remain unchanged. Preseal WHOLE readback, current input postpins, exact target absence and unique marker-last publication precede close/finalize/expected VERIFY. Custody binds all owned outputs except itself, records actual clocks and completes the all-writers-idle handoff.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11704`.
- Body SHA-256:
  `7addb22e10fece0cdccecb3766ccde1cba3a95f037f0f87bf96cd7e1b5082020`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
