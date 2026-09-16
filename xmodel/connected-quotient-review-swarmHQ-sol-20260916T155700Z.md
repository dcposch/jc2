# Connected-quotient tower — hostile different-model FIRST

Reviewer: swarmHQ Sol fallback, requested gpt-5.6-sol; exact runtime model ID is not independently exposed to this session. September 16, 2026. Frozen public commit: `4c0416feb6ed5974c368c10f9df71ac86b8ebe74`. MANUAL mathematical review, no scientific execution. No promotion authority.

Verdict for **CONNECTED-QUOTIENT-TOWER-1: CONFIRMED, conditional on the three accepted Keller/block premises at their existing tiers**. This verifies the new endpoint-relative-closure and field-step argument, not the old small-degree or strict-block theorems. JC2 remains unresolved.

## Frozen input and tested statement

The producer `xmodel/connected-quotient-tower-swarmHQ-root-20260916T155300Z.md` has full SHA-256 `24611d38c316c0a4f65d7a7911222a9cd421d23c3dcb17c8e29f5d0f2d5efd6f`; its artifact manifest has SHA-256 `477b2ba0e9d2aefd8e698fe9e6ad9c64a12d99093bdaee754bceb6885ce7f0cf`. Both match the charge. Its manifest records basis `3be38d75eb885c9fde1fd1229c18f7be06d36f7c`, and `artifact_finalize.py verify` returned `VERIFIED` with that exact expected basis and manifest digest. I read the complete frozen report after these checks.

The assertion is: for a finite tower of dominant generically finite rational maps of integral complex varieties, each ambient function-field degree at most three, compatible dominant rational quotients at the two ends to affine planes with **geometrically integral generic fibers**, a descended whole-plane polynomial map with nonzero constant Jacobian is an automorphism. This is a statement about the actual rational-map square and both endpoint field embeddings. It is not about arbitrary output projection or a quotient existing for every tower.

## Independent field reconstruction and attacks

Write `E_0 subset ... subset E_m` after pulling every ambient function field into `E_m`. Pull the bottom target plane and top source plane fields into `E_m` as `K` and `L`. Commutativity identifies `K subset L` with the actual Keller inclusion `C(h_1,h_2) subset C(s_1,s_2)`: the two target generators pull back to `h_1,h_2` in the top quotient field. Keller dominance and equal plane dimensions make `L/K` finite. This embedding identification is load-bearing; treating similar coordinate names as equal would not prove it.

For a dominant rational quotient `q:X --> A2`, geometric integrality of its generic fiber implies that the base field `B=C(A2)` is relatively algebraically closed in `C(X)`. Here is a direct check. If `a` in `C(X)` has degree `d>1` over `B`, then characteristic zero makes its minimal polynomial separable. The injection `B(a) -> C(X)` remains injective after tensoring with an algebraic closure of `B`. But `B(a) tensor_B overline(B)` is a product of `d` copies of `overline(B)`, whereas geometric integrality makes `C(X) tensor_B overline(B)` a domain. The product's nontrivial idempotents cannot inject into that domain. This uses the **geometric generic** fiber, not special fibers, properness, normality, or geometric connectedness alone. Thus `K` is relatively algebraically closed in `E_0`, and `L` in `E_m`.

Set `C_i=E_i intersect L` inside `E_m`. Every `C_i/K` is finite since `L/K` is. At the bottom, every element of `C_0` is algebraic over `K` and belongs to `E_0`, so bottom relative closure yields `C_0=K`. At the top, `C_m=L`. For any `i`, if `a in E_i` is algebraic over `C_i`, it is algebraic over `K`, hence over `L`; top relative closure in `E_m` puts `a in L`, and therefore `a in C_i`. Thus `C_i` is relatively algebraically closed in `E_i`. The passage through `K` is justified by finiteness; no reverse containment is assumed.

For each adjacent step, let `a` generate the finite separable extension `C_i/C_(i-1)` and let `P` be its irreducible monic polynomial. A monic factor of `P` over `E_(i-1)` would have coefficients algebraic over `C_(i-1)`: they are symmetric expressions in roots of `P`. Those coefficients also lie in `E_(i-1)`, so relative closure of `C_(i-1)` in `E_(i-1)` places them back in `C_(i-1)`, contradicting irreducibility. Thus `P` remains irreducible over `E_(i-1)` and

`[C_i:C_(i-1)] = [E_(i-1) C_i:E_(i-1)] <= [E_i:E_(i-1)] <= 3`.

Here the compositum is actually contained in `E_i`, so the left degree even divides the ambient step by the tower law. This divisibility is specific to the relatively closed lower-field situation; it must not be confused with the false general divisibility claim for arbitrary composita. The argument would already work with only the inequality.

If `L != K`, choose the **first** index `j` with `C_j != K`. All earlier `C_i` equal `K`, hence `M=C_j` has `[M:K]=2` or `3`. If `M=L`, this is the whole Keller mapping degree, excluded by accepted premise 1. If `M<L`, it is a strict proper intermediate field of the *actual* Keller extension with **second-leg** degree `[M:K]=2` or `3`, excluded by accepted premise 2. There is no assumption on `[L:M]`; it may be arbitrarily large. Consequently `L=K`, and accepted birational Keller automorphy gives the conclusion. Equal adjacent fields and an empty ambient tower are included. No polynomial descent through the intermediate `C_i` is asserted or needed.

## Historical-premise and scope checks

The whole `low-fiber-tower-transfer-gate-sol-20260913.md` (SHA-256 `63e69b73ced5f3b5026632f4c6e70c70a83daaa90ae39d6e1da3f4688b6418d5`) explicitly accepts exactly the whole-degree 2/3, strict second-leg 2/3, and birational premises. Its older field theorem would apply directly to the *reversed* newly constructed tower `L=C_m >= ... >= C_0=K`; the new contribution is the endpoint-fibration construction of that tower, not a new Keller degree theorem. The whole `cubic-block-priority-recovery-root-20260912.md` (SHA-256 `18d41c9b42de44625b9dda6090b4b252f0c31edff641adf3d47e92f16f67679e`) and binding `block-descent-a1-cubic-acyclic-branch-monodromy-coordinator-addendum-sol56-20260830.md` (SHA-256 `b3bdd87cb27b614ca4bac476fd7f4c676b9551026397f3a895dbf84f4f195419`) state the strict cubic target-block exclusion without a restriction on first-leg degree or a smooth source normalization. The current ledger also states that scope. I have not re-proved those imported results or enlarged their evidence tier. The addendum's historical 0664-versus-0444 mode discrepancy remains real: matching bytes and body/basis seal, not a currently successful artifact transaction, support its prior acceptance. No old file or mode was changed.

I also checked the geometric-versus-connected control. In `X: u^2=t v^2` over `(t,w)`, `X` is integral and the geometric generic fiber is two intersecting lines, hence connected but reducible. In the field of `X`, `u/v` is algebraic of degree two over `C(t,w)`. Thus geometric connectedness alone does **not** justify the relative-closure step on arbitrary nonnormal sources. Conversely, neither the proof nor its conclusion requires every special fiber to be integral or even connected. The vertical map `(x,y,z) -> (x,y,z^3)` under `(x,y)` quotient shows that ambient degree need not equal descended degree; two horizontal cubic steps produce descended degree nine, so a total-degree-at-most-three shortcut would be false. That degree-nine example is non-Keller, as required.

The claimed application to any accepted cubic core, identity stabilizations, and coordinate changes is valid **only when** their actual ambient generic degrees are at most three and the stated commuting endpoint quotients with geometrically integral geometric generic fibers are independently supplied. The old every-fiber theorem is one sufficient source for that ambient degree bound; it does not automatically supply endpoint quotients. Arbitrary projected sections can have the opposite field containment, exceptional restrictions can have degree at least four despite an ambient generic degree one, and removing either endpoint-integrality hypothesis breaks the closure argument. None of these off-scope cases is excluded here. No counterexample construction, global reduction of JC2, or further descendant follows.

Evidence: MANUAL / DIFFERENT-MODEL FIRST at the observable Sol fallback provenance, conditional on accepted premises. Exact verdict: **CONFIRMED** for the charged theorem and application with the stated independently checked hypotheses; **NO CLAIM** for geometric connectedness in place of integrality, one-ended quotient hypotheses, arbitrary projections, ambient degree at least four, or a theorem for all Keller maps.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8626`.
- Body SHA-256:
  `6cc8e0495dd746ec80a34b9c758e4b9ac428c9637b1141860d543baa33945afd`.
- Frozen basis: `4c0416feb6ed5974c368c10f9df71ac86b8ebe74`.
