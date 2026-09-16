# All-seed tangent graphs / linear outputs — hostile Sol FIRST

Reviewer: swarmHQ native Sol fallback, requested gpt-5.6-sol; exact hosted model identity is not independently exposed. September 16, 2026. Frozen public commit: `1ad910a81993a4f95fc717bd3d2100860e718b35`. Evidence: MANUAL characteristic-zero polynomial review; no scientific code, CAS, or sampled search. No promotion authority.

Verdict for **TANGENT-GRAPH-LINEAR-1: CONFIRMED** at the producer's exact scope. When `d=deg p>=2`, `gamma != 0`, `q'=wp'/2`, and all of `C,D,E` extend polynomially over the whole source plane, the three Jacobian minors have the claimed nonzero leading coefficients and distinct positive partial-`y` degrees. Every constant rank-two affine-linear projection of `(C,D,E)` consequently has nonconstant Jacobian; rank less than two gives zero. Polynomial postcomposition of such a projected pair and polynomial source reparametrization cannot make a Keller pair. This is a graph/linear-output construction exclusion, not a general plane Keller theorem.

## Frozen input, charged maps, and field of calculation

The producer `xmodel/tangent-graph-linear-projections-swarmHQ-root-20260916T182800Z.md` was read WHOLE only after its full SHA-256 `bc688cbf61e6e9b4adb1c93054bac5feb54d8b85feb867c4464849969824d317`, manifest SHA-256 `613d224a6ce3a68e7feb6b0f3b074a8997401d8d24fde00552e309d479a2280b`, and embedded basis `670ac5214197aea555a2aa590e01ce5974a089c4` matched the charge. `artifact_finalize.py verify` returned `VERIFIED` with that exact basis and manifest digest. Custody does not replace mathematical review.

All leading-term work is in `k(x)[y]` with `k` characteristic zero, while the final constant/unit claim is in the **whole** polynomial ring `k[x,y]`. Write `gamma=h(x)y^n+lower`, `n>=0`, `h != 0`, and `a=xh`. Then `a != 0` and `a'=h+xh' != 0`: in `h=sum h_i x^i`, the coefficient of `x^i` in `a'` is `(i+1)h_i`, so characteristic zero precludes annihilating every nonzero coefficient. This handles `n=0` and arbitrary nonconstant `h`, without assuming `x` is a unit on the source.

## A. Exact leading terms and all three minors — CONFIRMED

The top `y`-term of `w=gamma(1+xy)` is `a y^(n+1)`. If `alpha` is the nonzero leading coefficient of `p`, then `p(w)` has degree `d(n+1)` and leading coefficient `alpha a^d`. This is strictly above the degree `n` of `2gamma`; division by `C=xgamma` with top term `a y^n` gives

`D=alpha a^(d-1)y^M+lower`, where `M=(d-1)n+d`.

The derivative relation gives `deg q=d+1` and nonzero `beta=d alpha/[2(d+1)]`, with unrestricted additive constant. The top degree `(d+1)(n+1)` of `q(w)` exceeds `deg_y(gamma w)=2n+1` by `(d-1)n+d>0`. Dividing by `C^2` gives

`E=beta a^(d-1)y^(M+1)+lower`.

The whole-plane polynomiality of `D,E` is indispensable here: the rational quotients have these leading terms in `k(x)[y]`, and the hypothesis says they are actual polynomials on all of `A2`. No localization at `xgamma` is smuggled into the final theorem.

For `f=A(x)y^r+lower`, `g=B(x)y^s+lower`, direct differentiation gives the coefficient of `y^(r+s-1)` in `J(f,g)=f_xg_y-f_yg_x` as `sA'B-rAB'`. Terms below the top `y`-degrees cannot reach that exponent. If `r=0`, the second term is simply zero, so the identity is still valid; it does not pretend `f_y` has a top term. Apply it to `C` (top `a y^n`) and `D` (top `alpha a^(d-1)y^M`): the coefficient is `alpha a^(d-1)a'[M-n(d-1)]=d alpha a^(d-1)a'`, at degree `n+M-1=d(n+1)-1`. The same calculation with `E` gives `(d+1)beta a^(d-1)a'` at degree `n+M=d(n+1)`. Both are nonzero, including `n=0`.

For `J(D,E)`, the two leading coefficient functions are proportional but the `y`-exponents are `M` and `M+1`, not equal. The top coefficient is `alpha beta(d-1)a^(2d-3)a'[(M+1)-M]=(d-1)alpha beta a^(2d-3)a'`, at degree `2M`. It is nonzero because `d>=2`, `alpha beta != 0`, `a a' != 0`. The degrees are ordered strictly:

`d(n+1)-1 < d(n+1) < 2M`, with `2M-d(n+1)=(d-2)n+d>0`.

In particular the lowest degree is at least one. No same-degree cancellation is possible for `d=2`, `n=0`, or any larger values. This establishes every equality and nonvanishing assertion in the producer's formula (1), rather than only a generic leading bound.

## B. Linear projection, postcomposition, and reparametrization — CONFIRMED

For a constant `2×3` linear matrix `L`, Cauchy--Binet gives the projected Jacobian as `minor_CD(L) J(C,D)+minor_CE(L) J(C,E)+minor_DE(L) J(D,E)`. Rank two means at least one minor is nonzero. Choose the active minor with largest `y`-degree; its nonzero leading coefficient cannot be canceled by active terms of lower degree, so the projected Jacobian is nonconstant. Rank zero or one makes all minors zero. Target translations have no effect. This is an exact rank argument, not a finite sample of projection matrices.

If a polynomial pair `H` is postcomposed with the fixed projected pair `T`, then `J(H∘T)=J(H)(T)J(T)`. Both factors lie in `k[x,y]`, whose units are nonzero constants. Since `J(T)` is either zero or a nonunit, the product is never a nonzero constant. This proves only postcomposition through **one fixed linear projection**; an arbitrary polynomial map from all three outputs has source-dependent Cauchy--Binet coefficients and is not addressed. For a polynomial source automorphism `psi`, inverse chain rule makes `J(psi)` a nonzero constant and `psi^*` reflects constants, so `J(T∘psi)=J(T)(psi)J(psi)` has the same obstruction. A noninvertible source parametrization is outside this statement.

## C. Literal graph attachment and controls — CONFIRMED

In the literal three-dimensional tangent presentation `gamma=gamma0+b1xy+b2x^2z` with `gamma0 != 0` and `b2 != 0`, substituting any polynomial `z=Z(x,y)` yields `gamma(0,y)=gamma0`; therefore the graph polynomial `gamma` is nonzero. If the ambient `C,D,E` are whole-source polynomials, their graph pullbacks remain whole-plane polynomials. Since `xgamma` is a nonzero polynomial on the graph, the displayed rational formulas agree with those pullbacks in the graph function field. The theorem applies to every such graph, every admissible seed degree, and every constant linear output pair. The prior first-pair theorem derives `d>=2` for its literal full-triple admissibility; the present abstract theorem states `d>=2` explicitly rather than silently assuming it for arbitrary `gamma,p,q`.

I checked the displayed boundary examples manually. With `gamma=1`, `p=-2w^2+2w-2`, `q=-(2/3)w^3+(1/2)w^2-5/6`, substitution of `w=1+xy` gives `C=x`, `D=-2y-2xy^2`, `E=-(3/2)y^2-(2/3)xy^3`. Direct derivatives give minors `-2-4xy`, `-3y-2xy^2`, and `(14/3)y^3+(4/3)xy^4`, exactly the predicted degrees `1,2,4` and top coefficients `-4x,-2x,(4/3)x`. This is a valid `n=0` plane control, not a claim that it is an ambient whole-triple seed.

For the fixed-core values `gamma=2-3xy`, `p=-3w^2+4w`, `q=-w^3+w^2`, the product `w=(2-3xy)(1+xy)` and the rational formulas reduce to `C=2x-3x^2y`, `D=y+12xy^2+9x^2y^3`, `E=4y^2+7xy^3+3x^2y^4`. For `E`, a direct factorization is `q(w)+gamma w=gamma^2(1+xy)(xy)^2(4+3xy)`, so no denominator is missed. With `n=1,d=2,a=-3x^2,a'=-6x`, the three top-minor coefficients are `-108x^3,-54x^3,54x^3`, at degrees `3,4,6`.

Dropping `d>=2` changes the result: `gamma=1`, `p=-2w`, `q=-w^2/2-1/2` gives the whole triple `(x,-2y,-y^2/2)`, whose first pair has constant Jacobian `-2`; the third formula would contain the vanishing factor `d-1`. The alternative source plane `x=0` of the fixed core is parametrized by `(y,z)` with outputs `(z+4y^2,y,0)`, and the first pair has Jacobian `-1` and a polynomial inverse. This shows why a theorem for all graph orientations or arbitrary embedded planes would be false; it does not conflict with `z=Z(x,y)`.

## History and exact verdict boundary

The whole earlier first-pair report `xmodel/tangent-graph-first-pair-swarmHQ-root-20260915T180230Z.md` has SHA-256 `4a2b0b3b92ca94b54c8807c39fa1afed0fd6bf60e3b866fdb4fa588a0ab2de3d`; it covers arbitrary seeds/graphs but polynomial target pairs only through `C[C,D]`. The whole September 6 fixed-core report `xmodel/alpoge-polynomial-graph-obstruction-astra-20260906.md`, SHA-256 `1ab4e6791e6a38fd9a8313161a546554a57efcf5207bc32d42dfa4b492dd8e21`, covers all polynomial graphs and linear projections for one fixed core. The whole September 12 report `xmodel/equivariant-graph-nonlinear-obstruction-root-20260912.md`, SHA-256 `8ae6ee53450d7a7ef4e688cf768903ca9900f8e4f176088076c3c8bf9cdde828`, covers arbitrary polynomial outputs only on its restricted one-sided graph wedge for that fixed core. The charged theorem combines a different scope: E and all constant linear projections for every seed degree under whole `C,D,E` polynomiality. Those previous reports were context, not an unproved three-minor import.

Nothing here excludes arbitrary nonlinear three-output target maps, rational output changes with poles, other graph orientations, general embeddings, or arbitrary plane maps. No complete Keller source is constructed or ruled out. JC2 remains unresolved. No new exit-price claim, scientific execution, historical novelty determination, or descendant is made.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9297`.
- Body SHA-256:
  `34f1b6a0633bb21aa92f03dd1fa5b6727f8849e9d97743dcece1fa93cea11509`.
- Frozen basis: `1ad910a81993a4f95fc717bd3d2100860e718b35`.
