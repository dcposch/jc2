# Global dualizing freeness and radial descent: bounded discriminator

Status: MANUAL CO-RESEARCH / GAP. Neither a normality theorem nor a counterexample to the full package is established. No FIRST or mathematical promotion.

First action: 2026-09-12 14:28:14 UTC. Original publication reserve 14:40 UTC; hard stop 14:43 UTC. Exactly two frozen inputs, both freshly read WHOLE after matching current hashes. No scientific execution or external research.

## Exact question

Let R=C[x,y] be the finite birational normalization of a finitely generated complex domain B. Assume Spec R -> Spec B is everywhere unramified, B is Cohen–Macaulay with a globally free dualizing module, and a Kähler one-form on B pulls back to alpha=(x dy-y dx)/2. Must B=R? Neither arbitrary area exactness nor local Gorensteinness replaces these hypotheses.

## Result

Global freeness supplies an exact principal-conductor description. It does not, by the reconstructed duality argument, supply an Euler derivation on B. The derivation actually obtained is cE, and its preservation of B and of the conductor is automatic. Thus this route loses the radial-descent hypothesis at precisely the proposed normality step. The full question remains open in this bounded investigation; the two supplied examples are not counterexamples to it.

## 1. What finite duality actually gives

Write omega=dx wedge dy, E=(x partial_x+y partial_y)/2, and alpha=i_E omega. Use the canonical dualizing module, with finite duality identified generically by the identity trace of the birational function-field extension; an arbitrary invertible twist is not being introduced. Since B is a two-dimensional Cohen–Macaulay finite-type domain and R is its finite smooth normalization, finite canonical duality identifies

    Hom_B(R,omega_B)=omega_R.

Inside the common function field, Hom_B(R,B) is the conductor I: a multiplier q with qR contained in B already belongs to B by evaluating at 1. If omega_B=B eta, write eta=q omega as a rational two-form. Duality therefore says Iq=R. Consequently

    I=cR,    eta=omega/c,    0 != c in I subset B.

Changing the chosen global generator only multiplies c by a nonzero constant: a unit of B is a unit of R, and R has only constant units. This uses global freeness, not merely local Gorensteinness. It permits arbitrary conductor multiplicities; it says neither that c is squarefree nor that its zero set is conical.

The pullback of the specified beta is alpha, and its exterior derivative pulls back to omega. These statements alone do not identify a nowhere-vanishing generator of omega_B: relative to eta the latter two-form has coefficient c, which can vanish on the conductor.

## 2. The exact failed cancellation

On the common function field, the vector field determined by contracting eta with the descended beta is

    delta=cE,    i_delta eta=alpha.

For every b in B, E(b) is a polynomial in R, so delta(b)=cE(b) belongs to cR subset B. Thus delta is indeed a B-derivation. But this conclusion holds for *every* intermediate B with conductor cR, even without a descended beta. Similarly, for r in R,

    delta(cr)=c E(c)r+c^2 E(r) belongs to cR.

Preserving I by delta is therefore automatic too. Cancelling c in either inclusion is invalid: c need not be a B-unit, and I is not assumed saturated for multiplication by c. No E(B) subset B or E(I) subset I follows.

There is no extra vanishing hidden in the corresponding Lie-derivative calculation. Since div_omega(E)=1,

    L_delta(omega/c)
      = (E(c)+c-E(c)) omega/c
      = c eta = omega.

This is precisely compatible with d alpha=omega, not a contradiction. It holds as a rational-form identity and has a regular canonical-module right-hand side. In particular, interpreting d beta as a volume form *on the singular target* would silently replace its possibly vanishing coefficient c by a unit.

At an ordinary double locus the global generator imposes the usual opposite-residue matching. Radial descent imposes equality of the pulled-back tangential one-forms. Their combination need not be read as separate vanishing on either branch: a paired opposite-value relation is not an individual Euler-tangency relation. Nothing here excludes higher multiplicities or additional branches by reducing them without proof to a transverse pair.

## 3. Exact control separation

The TASK's first control is B0=C[t^2-1,t(t^2-1),s] inside C[t,s]. It is the nodal hypersurface cylinder v^2=u^2(u+1), so its dualizing module is globally free. At the identified points (1,s) and (-1,s), however, the radial form restricts respectively to ds/2 and -ds/2 along the common tangent. A pulled-back Kähler form would have equal restrictions. Hence B0 fails the specific radial-descent assumption. Its nonnormality cannot refute the question.

For the second control set a=x^2, b=xy, u=a-1, d=ux, e=uy, and B1=C[x^2,xy,y^2]+uR. Its displayed Kähler expression has pullback

    db/2-e dd-((4-3a)/2)b da
      = (y dx+x dy)/2
        - y[(a-1)(3a-1)+(4-3a)a] dx
      = alpha.

The bracketed polynomial is 1 by direct expansion. This is the exact radial form, not just another primitive of omega.

Here R is finite over B1 because x and y are integral, and their recovery as d/u and e/u makes the extension birational. Its relative differentials vanish: da=2x dx and dd=(3x^2-1)dx give 3x da-2 dd=2 dx; then x db-de+xy dx=dy. Thus the normalization is everywhere unramified.

Modulo uR the subring is the diagonal graph identifying (1,t) with (-1,-t). The largest ideal of the two-component normalization algebra contained in that graph is zero, so its conductor is exactly uR. Locally the gluing is a transverse nodal cylinder, hence Cohen–Macaulay and locally Gorenstein. If a global dualizing generator existed, the duality calculation above would force eta=kappa omega/u for a nonzero constant kappa. On the first branch its residue is kappa dt/2. On the second, parametrized by (-1,-t), both dy and the normal derivative of u change sign, and the residue is again kappa dt/2. A nodal dualizing form requires opposite residues under the gluing. Therefore no such global generator exists. This example fails precisely the global-freeness hypothesis; local Gorensteinness does not repair it.

These are controls of the proposed inference only, not new examples or a new family. In particular B1 must not be presented as a counterexample with all the requested hypotheses, nor as a hypersurface in affine three-space. No extra hypersurface hypothesis was added to the question or used to claim its resolution.

## 4. Endpoint, missing property and next discriminator

The missing property is a non-tautological implication from the *global descended radial one-form plus global dualizing trivialization* to c being a unit, or to some separately sufficient global normality criterion. The contraction construction furnishes only cE and does not establish that implication. Conversely, an exact counterexample would have to verify the global dualizing trivialization as well as radial Kähler descent; omitting either repeats one of the failed controls above.

Verdict: GAP / NO_NEW_MECHANISM beyond the specified duality-and-descent bridge. This report supplies no normality proof and no counterexample to the full package. In particular it supplies no actual Keller counterexample, canonical-graph normality, invertibility, or JC2 conclusion.

The remaining quantity is one exact theorem/counterexample question, not a coefficient computation. Cheapest next test would be a single independent manual audit of the cancellation issue and the full hypotheses; planning allowance 10 minutes, UNMEASURED, with no execution or follow-on authorization. Repeating conductor-shape lemmas, locally Gorenstein examples, or arbitrary area primitives would not discriminate this question.

## Scope and publication audit

Only COORDINATION.md and this task's TASK.md were scientifically charged, both hash-matched and freshly read WHOLE; no inherited report, prior proof, peer body, linked reference or external text was used. The canonical finite-duality theorem and the nodal opposite-residue description are explicitly named standard mathematical inputs reconstructed at the stated hypotheses, not newly consulted literature. All calculations above were manual. No scientific/helper/interpreter/CAS execution, network, worker, protected-tree access, fixture or source change occurred. Administrative finalization alone used the existing publication tool.

Owned outputs are this transactional report, its generated manifest, PINS.json and custody.json; the ROOT-owned TASK is unchanged. Final report/manifest/custody target absence was checked before beginning, and final report/manifest absence is checked again before sealing. No canonical OPEN ledger is edited. The precise mathematical GAP above remains raised; its cheapest test and unmeasured planning quantity are stated rather than converted into a claimed pass. Final custody records exact postpins, expected-manifest verification and terminal all-writers-idle time.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9100`.
- Body SHA-256:
  `2c299d14e09479e930b7c00c66eaa7ee76b7f78045b0c73699e918e93baba35b`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
