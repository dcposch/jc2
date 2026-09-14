# Full-source collision surface: unit-group discriminator

MANUAL CO-RESEARCH / GAP on the requested unit group, not FIRST or promotion. First action 2026-09-12 15:24:01 UTC; original reserve 15:35 UTC / hard stop 15:38 UTC. Exactly two current-pinned inputs freshly read WHOLE in order. No scientific execution or external input.

## Exact question

Let F=(f,g) be a polynomial complex plane Keller map, J(f,g)=1. Put A=C[f,g], R=C[x,y], and C_F=R tensor_A R. After removing the clopen diagonal factor, does every nonempty connected off-diagonal factor S_i have only constant units? No off-component existence, finite projection, or global source counterexample is assumed.

## Verdict

Neither S_i^*=C^* nor an actual polynomial Keller counterexample to that assertion is established. The norm shortcut fails at a precise boundary step, and constant norm would not by itself close the argument. A genuine all-source restriction does hold: the subgroup of units on the FULL fibre square satisfying the multiplicative descent cocycle identity is trivial. That subgroup must not be identified with the units of a connected off-diagonal component.

## 1. The exact source object

The Jacobian criterion makes F étale, hence flat, open and quasi-finite; J=1 also makes f,g algebraically independent. Both projections of X=A2 fiber-product_(A2) A2 are base changes of F, so are étale. The diagonal is an open immersion because F is unramified, and a closed immersion because F is separated. Thus it is clopen and X splits as its diagonal A2 and the affine off locus. This is an actual product splitting of coordinate rings, not a localization informally removing coincident points.

X is smooth over C. In a noetherian regular scheme distinct irreducible components cannot meet, since a regular local ring is a domain. There are finitely many such components, so they are clopen. Consequently each connected component is integral and smooth. Each nonempty off component X_i=Spec S_i is therefore a smooth affine integral surface, closed in A4. Either projection has nonempty open image in the irreducible plane and hence is dominant. Its function-field extension is finite separable by quasi-finiteness. No finiteness or surjectivity of the projection follows.

A unit on one component can be made a unit of the full disconnected C_F by putting 1 on all other factors. This does not make it the pullback of a source unit. Conversely the many idempotent-wise constant units of C_F are irrelevant to whether S_i has nonconstant units. Flatness does not identify these two unit groups.

## 2. What the norm does and does not prove

Fix a projection pi:X_i -> Spec R and put L=Frac R, K=Frac S_i. Let Z be the normalization of Spec R in K. It is finite over Spec R (polynomial rings over C have finite normalization in finite field extensions). The normal version of Zariski's main theorem factors pi as the open immersion X_i -> Z followed by this finite map. This is the finite completion; it need not equal X_i.

For h in S_i^*, the rational function h on Z has divisor supported on Z minus X_i. At a prime divisor D of the source plane the field norm satisfies

    ord_D N_(K/L)(h)
      = sum_(E over D) [k(E):k(D)] ord_E(h).

This is the valuation formula for a finite extension of discrete valuation rings; it includes ALL prime divisors of Z over D, not just those retained by the open immersion. The terms from E whose generic points lie in X_i are zero. There is no supplied reason for the missing terms to be zero or cancel. Thus N(h) is certainly in L^*, but need not belong to R^*. Even a proof that N(h) is constant would not imply h constant without an additional norm-kernel argument.

The exact missing information is the boundary divisor of h in this finite completion, together with a mechanism controlling the norm-one kernel. Neither R^*=C^*, the two étale projections, nor factor swap supplies that information. Swap can exchange components; even on a preserved component it gives no automatic equality between a unit and its inverse.

One small control breaks both false norm inferences. Let

    Q=C[t,t^{-1},(t^2-1)^{-1},s],
    X0=t+t^{-1},   Y0=s.

Spec Q -> A2_(X0,Y0) is étale: dX0/dt=1-t^{-2} is a unit on this domain. It is quasi-finite and not finite onto the whole plane; its image omits X0=2 and X0=-2. In the quadratic function-field extension the conjugate of t is t^{-1}. The units t and t-1 satisfy

    N(t)=1,          N(t-1)=2-X0.

So a nonconstant unit can have constant norm, while the norm of another unit vanishes on a missing base divisor. This is only an abstract étale-projection control with localized source, not the fibre square of a full-plane polynomial Keller map. It is used solely to refute those norm steps, not the source statement.

## 3. A proved all-source restriction: multiplicative cocycle units

Write W=F(A2), an open subset of the target plane. Regard F:A2 -> W as a surjective étale morphism. It is quasi-compact: inverse images of affine opens are opens in the noetherian source and hence quasi-compact. Together with separatedness and the étale local finite-presentation condition, this gives finite presentation. Flatness and surjectivity make it faithfully flat, hence an fppf cover. Its double and triple overlaps are exactly the corresponding fibre products over the original target, since both maps already factor through W.

Claim: if a unit u in C_F^* satisfies

    u_12 u_23 = u_13

on A2 fiber-product_W A2 fiber-product_W A2, then u=1. The cocycle itself implies diagonal value 1, and inverse values after factor swap; those weaker conditions alone are not substituted for the displayed identity.

Here is the complete attachment. Such a unit is precisely a descent isomorphism between the two pullbacks of the trivial line bundle on A2, with the displayed identity as the cocycle condition. Effective faithfully flat descent for invertible sheaves therefore gives a line bundle L_W on W and a chosen trivialization of F^*L_W.

Every line bundle on W is trivial. Indeed W is regular integral, so its Picard group is its Weil divisor class group. Any Weil divisor on W extends, by taking closures of its finitely many prime components, to a Weil divisor on A2. The polynomial ring C[a,b] is factorial, so that extended divisor is principal. Restriction makes the original divisor principal too. Thus Pic(W)=0, without assuming W affine or F finite.

Choose a trivialization of L_W. Comparing its pullback with the chosen source trivialization multiplies by a unit a in R^*. The descent unit is consequently a ratio of the two pullbacks of a. Since R^*=C^*, that ratio is 1. This proves the claim using the full-plane source, not a finite-norm assertion. The only standard descent theorem used is faithfully flat descent of line bundles at the explicitly verified cover hypotheses.

This kills a precise cocycle subgroup of C_F^*, not its whole unit group. Extending an arbitrary h in S_i^* by 1 on the other factors creates a global unit, but does not manufacture the triple-overlap identity. That missing identity cannot be replaced by symmetry, diagonal normalization or an unproved assertion of descent. No implication from the claimed cocycle result to S_i^*=C^* is asserted.

Conversely the unit 1 is a cocycle and comes from the trivial line bundle with its trivial source trivialization. Thus the asserted cocycle subgroup is exactly {1}, not merely mapped trivially to Pic(W). This is a standard descent result attached to the precise source, not a new general unit theorem or a closing JC2 mechanism.

## 4. Matched dropped-polynomiality control

On the punctured source Spec C[x,x^{-1},y], let

    F0=(x^2,y/(2x)).

Its Jacobian is 2x times 1/(2x)=1. Equality of target coordinates in two copies gives u^2=x^2 and v=(u/x)y. Since x is a unit and characteristic is zero, the two factors u-x and u+x are comaximal. Besides the diagonal there is exactly the off graph (u,v)=(-x,-y), with coordinate ring C[x,x^{-1},y]. Its units are C^* x^Z and include the nonconstant x. The pole of y/(2x) at x=0 is genuine; this map is not a polynomial map from the whole plane. Thus it refutes a localization/abstract-étale replacement of the question, not the exact full-source assertion. An automorphism of the whole plane has no off component and supplies only a vacuous positive check.

The norm control in section 2 is the only additional control, and is directed specifically at norm extension and the norm-one kernel. No extra family, source degree, actual polynomial Keller collision, symplectic theorem or coefficient calculation is asserted.

## 5. Endpoint and next missing test

Exact verdict on every actual S_i having S_i^*=C^*: GAP. No full-plane counterexample is produced. The proved attachment is the triviality of full triple-compatible descent units; arbitrary off-component units remain outside it. Norms give an explicit finite-completion boundary formula, not a regular-unit certificate. Neither statement proves injectivity or excludes a source.

NO_NEW_MECHANISM closing the arbitrary-unit question was found. The remaining quantity is one source-specific theorem: control the divisor of an arbitrary off-component unit at missing branches, and the remaining norm kernel, or justify a different condition such as its required cocycle compatibility. The cheapest bounded next discriminator would be one manual check of a concrete proposed bridge at those exact hypotheses, estimated 10 minutes UNMEASURED; no such bridge, follow-on task or execution is authorized here. Repeating that norms are rational, or that Pic(W)=0, does not supply it.

## Read scope and custody

Exactly COORDINATION.md and TASK.md were current-hash checked before fresh WHOLE reads, in that order and without clipping. No inherited report, live peer, linked source, corpus, external text or protected tree was read. Standard Jacobian/étale facts, normal Zariski main theorem, the finite-normalization valuation formula and faithfully flat descent of line bundles are explicitly used at the displayed hypotheses; none was replaced by a computational or literature claim. All control algebra was manual.

No scientific interpreter/helper/CAS/import/AST/syntax/test/dummy/fixture execution, network, AWS, process inspection, other agent or shared edit occurred. Only inert UTC/hash/text/absence checks, own apply_patch writes and the existing administrative finalizer were used. Own WHOLE readback, input postpins and report/manifest/custody target absence precede the unique marker-last close/finalize/expected VERIFY. The mathematical GAP and its quantity/cheapest test are explicit; no canonical OPEN is created. Final custody binds report, manifest and PINS, records actual clocks, and is followed by an actual ALL WRITERS IDLE handoff with no later writes.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10855`.
- Body SHA-256:
  `8d05e75546be5ad81de3db4b6c0ca2d213f1f05fc8384ae84ef7cab32748636a`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
