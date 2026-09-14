# Fixed constant graph: polynomial area primitive

Manual co-research, not promotion. First action2026-09-12 10:38:03 UTC; original reserve11:00/HARD11:03 unchanged. TASK and all three inputs matched before charged bodies; all owned destinations absent. No scientific execution or external input.

## Quantity and scope

For the literal constant graph z=1, determine whether dx wedge dy is the differential of A(p,q,r)dp+B(p,q,r)dq+C(p,q,r)dr with target POLYNOMIAL coefficients. An exact primitive is necessary, not sufficient, for a Keller pair in the subalgebra. The old nonclosed beta and known collision are not negative answers to this question.

## Manual result

**GAP on the requested YES/NO.** I obtain an exact all-degree logarithmic-divergence criterion, with an exact specification of the image ideal. I do not construct its required derivation or prove that none exists. In particular neither the known collision nor the old nonclosed beta decides this criterion. No fixed-degree ansatz, local primitive or source coefficient outside the target algebra is substituted for the requested certificate.

## 1. Exact image ideal without a computed eliminant

Write T=C[U,V,W], phi:T→C[x,y] for substitution by the given p,q,r, and S=Spec(T/ker phi). The supplied identity

    (r/4)J(p,q)+(q/4)J(p,r)−(p/2)J(q,r)=1

implies differential rank two everywhere, in particular transcendence degree two. Thus ker phi=(F) for an irreducible polynomial F, unique up to a nonzero constant: this is a height-one prime of the polynomial UFD. No normality, finite normalization or injectivity of the graph map is assumed.

The chart gives a completely specified elimination ideal, not an uncomputed assertion about a resultant's value. Introduce s,t,tinv and impose

    f = W s^3−2s^2+V s−2U = 0,
    2t = 3W s^2−4s+V,
    g = W t^3+3st−5t^2+1 = 0,
    t*tinv = 1.

The intersection of this ideal with T is exactly (F). Indeed eliminating U,V gives U=s^2+st−Ws^3, V=4s+2t−3Ws^2; eliminating W using g identifies the quotient with C[s,t,t^−1]. The inverse chart x=1/t,y=s−t identifies it with the x≠0 part of the literal z=1 graph, dense in A2. This proves the kernel assertion, including the t≠0 condition; no extraneous t=0 component is silently retained. F itself and a logarithmic-derivation module were not expanded or computed.

## 2. The exact surviving equation

Let Omega=dU wedge dV wedge dW and

    beta=(W/4)dU wedge dV+(V/4)dU wedge dW
                                      −(U/2)dV wedge dW.

Its graph pullback is dx wedge dy and d beta=−Omega/2. The question is equivalent to existence of POLYNOMIALS a,b,c,h in T such that

    a F_U+b F_V+c F_W=hF,
    a_U+b_V+c_W=1.                                  (*)

Equivalently there must be a polynomial vector field delta tangent to the image hypersurface whose ambient divergence is exactly one. This is not a unit statement in the Jacobian-minor module: its second equation is an additional differential constraint on the entire correction.

Proof in both directions is elementary. Every ambient polynomial two-form is uniquely i_X Omega. Such a form pulls back to zero on the graph exactly when X(F) lies in (F). To see this, on the dense smooth locus of S, contraction vanishes on its tangent plane exactly when X is tangent. The graph's dominant separable map has generic differential rank two, so vanishing can be checked after pullback. Irreducibility then converts generic vanishing into divisibility by F. This argument neither assumes the graph map birational nor treats a point collision as a whole-surface relation.

If an ambient polynomial one-form alpha has d(phi*alpha)=dx wedge dy, then gamma=d alpha−beta has zero graph pullback and d gamma=Omega/2. Write gamma=i_X Omega and delta=2X. Its divergence is one and it is tangent, proving (*).

Conversely a solution delta to (*) makes

    beta_closed=beta+(1/2)i_delta Omega

closed, with the same graph pullback as beta. It has a GLOBAL polynomial primitive, not just an analytic or formal one. Decompose it by ordinary coefficient degree m≥0. Each component beta_m is closed, and for the ordinary radial field E0=U∂U+V∂V+W∂W, Cartan's formula gives

    alpha=sum_m i_E0(beta_m)/(m+2),   d alpha=beta_closed.

The sum is finite, denominators are nonzero complex constants, and alpha has exactly the required polynomial target coefficients. The proof exhausts arbitrary kernel corrections and arbitrary polynomial degree. Changing F by a nonzero scalar does not change (*).

## 3. Controls on the new criterion

The same ambient beta is nonclosed even on the plane U=1. Nevertheless its restriction there is −dV wedge dW/2, with polynomial primitive −V dW/2. Correspondingly delta=V∂V is tangent to U−1 and has divergence one. Thus nonclosure of this particular beta really is compatible with a positive global primitive; no kernel correction can be dismissed solely for that reason.

The divergence criterion is not automatic for hypersurfaces. On the independent control UVW=1, substitute W=(UV)^−1. Beta restricts to

    −(1/2) U^−1 V^−1 dU wedge dV.

This is not the derivative of any algebraic one-form on that torus. For Laurent polynomial A,B, the U^−1 V^−1 coefficient of A_U or B_V is zero: the needed original exponent is zero and differentiation kills it. The indicated coefficient in beta is nonzero. Therefore no divergence-one tangent field can solve (*) for this control F. This is an all-degree coefficient proof, not a sampled period or finite ansatz. Neither control identifies the actual graph surface with a plane or a torus, or supplies a Keller pair.

## 4. Exact remaining gap and stop

The missing property is whether the explicitly specified actual principal image ideal admits a polynomial logarithmic derivation with divergence one. I have neither a literal solution to (*) nor an obstruction annihilating divergences of ALL such derivations. Module membership supplies beta but not this property; computing one failed correction, or observing the known collision, would not fill the gap.

The cheapest remaining discriminator is an exact solution of (*) or a linear functional vanishing on its possible divergences but not on1, for this one actual ideal. Its cost is UNMEASURED; the TASK's20-minute manual allocation is not a runtime estimate. No eliminant/degree ladder, new family, automatic computation or successor is authorized. Result: one exact global reformulation, **no decision of the original primitive existence question**, no exclusion of the subalgebra and no JC2 conclusion. No new canonical OPEN or charge_basis.

## Read scope and closeout

TASK and both graph reports were freshly read WHOLE after current hashes. COORDINATION is reused at its unchanged exact-pin same-agent whole read on2026-09-12 05:51–05:53. No linked inputs, scratch, coefficients, code, scientific execution, network, worker or peer output. Final own readback/postpins/scope/collision and quantity check precede the unique marker.

## COLLISIONS

status: EMPTY

- Own-only identifier/scope check; the already-known geometric collision is neither rederived nor republished as a result. The unresolved quantity is stated explicitly, with its cheapest exact discriminator and unmeasured cost.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7314`.
- Body SHA-256:
  `0c9b2c97f1926beda134f260ba1ef8a7216d02c3972d153b3f211cb0ac84c1f3`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
