# Linear/cubic resultant-one SL2 quotient — hostile Sol FIRST

Reviewer: swarmHQ native Sol fallback, requested gpt-5.6-sol; exact runtime model identity is not independently exposed. September 16, 2026. Frozen public commit: `97a752da7c5a86691a690d80dac32e7d981b9eb1`. Evidence: MANUAL algebraic review, no scientific code or CAS. No promotion authority.

Verdict for **LINEAR-CUBIC-SL2-QUOTIENT-1: CONFIRMED** at its exact scope. For the whole resultant-one source of a binary linear form and cubic form, the canonical-frame map is a global polynomial isomorphism `Z ≅ SL2 × A2_(u,v)`. Multiplication to binary quartics induces `(u,v) -> (I,J)=(-3u,-27v)` on the stated affine invariant quotients. The quotient map is an automorphism, despite multiplication itself being a different higher-dimensional morphism. This is not a plane Keller counterexample or a general exclusion of other factor constructions.

## Frozen inputs and conventions

The whole producer report `xmodel/linear-cubic-sl2-quotient-swarmHQ-root-20260916T174200Z.md` was read only after its full SHA-256 `f5781c10bbc848ef39b140312b8f0d8e3871a6df0cd1f4208f661566fc4fa593`, artifact-manifest SHA-256 `78156edf7faadef10a97310cca77d6895361630816fd2dfaa52dba5b4336d8ac`, and embedded basis `d71be3003c4555a0775c21675edeb12ce0435d44` matched the charge. `artifact_finalize.py verify` returned `VERIFIED` with that basis and manifest digest. Those are custody checks, not substitutes for the proof below.

Take `L=aX+bY`, `e=(-b,a)`, cubic `Q`, and **the producer's exact resultant convention** `Res(L,Q)=Q(e)=1`. This convention is essential to the signs and scale factors below; it is not replaced by a differently normalized resultant. It forces `L != 0` and gives a global polynomial equation, with no condition on a particular coefficient or on discriminants.

## 1. Global frame, degenerate charts, and polynomial inverse — CONFIRMED

Define `M=(Q_X(e)X+Q_Y(e)Y)/3`. Euler's cubic identity gives `-b Q_X(e)+a Q_Y(e)=3Q(e)=3`, so `det(L,M)=1`. Also `M(e)=det(L,M)=1` and `L(e)=0`. The entries of `M` are polynomial in all six original coefficients, and the determinant is the constant 1 on `Z`. Hence `X=dL-bM`, `Y=-cL+aM` when `M=cX+dY`; the inverse frame has polynomial coefficients and no chart denominator. This checks in particular `a=0`, `b=0`, or repeated roots of `Q`.

Write `Q=c_0M^3+c_1LM^2+uL^2M+vL^3`. Evaluation at `e` gives `c_0=1`. The gradient of `M^3` at `e` is `3M(e)^2 grad M=grad Q(e)` by the definition of `M`. The gradient of the remaining expansion at `e` is `c_1 grad L`; since `L != 0`, this forces `c_1=0`. Thus `Q=M^3+uL^2M+vL^3` globally. Substituting the displayed polynomial inverse frame into `Q` makes `u,v` polynomial functions in the original coefficients; no root extraction or localization occurs.

In the other direction take any determinant-one frame `(L,M)` and any `u,v`, and define `Q=M^3+uL^2M+vL^3`. At `e`, `L(e)=0`, `M(e)=1`, so `Q(e)=1`. Moreover `grad Q(e)=3 grad M`, because the `L^2` and `L^3` terms have zero gradient at `L=0`. The canonical-gradient recipe therefore returns exactly the original `M`, then coefficient extraction returns `u,v`. These are two-sided polynomial inverses on the **entire** affine schemes, proving `Z ≅ SL2 × A2`, not merely a birational parametrization or an isomorphism on `a != 0`.

As a direct boundary test, `L=Y,Q=-X^3` has `e=(-1,0)`, resultant 1, and the recipe returns `M=-X`, giving determinant 1 even though `a=0`. The repeated-root point `L=X,Q=Y^3` gives `M=Y,u=v=0`. Conversely, for resultant zero, e.g. `L=X,Q=X^3`, the recipe produces no determinant-one frame; this confirms that the source equation is load-bearing.

## 2. Equivariance and source invariants — CONFIRMED

For `g in SL2` acting by simultaneous substitution of the variable column, the coefficient row of `L` changes from `ell` to `ell g`; its perpendicular vector changes as `e' = g^{-1}e`, using `det g=1`. Thus `Q'(e')=Q(e)`, and the chain rule gives `grad Q'(e')=g^T grad Q(e)`. The canonical `M` therefore transforms by the *same substitution* as `L,Q`. Equivalently it is the unique determinant-one complement for which the `LM^2` coefficient vanishes: another complement `M+sL` changes that coefficient by `-3s`, so uniqueness holds in characteristic zero. The parameters `u,v` are fixed, and the group translates the full frame factor transitively.

If `f` is a regular invariant on `SL2 × A2`, then `f(g,u,v)=f(1,u,v)` for every `g`, since left or right translation on the frame factor is transitive. Evaluation at the identity frame is a polynomial in `u,v`; conversely every such polynomial is invariant. Therefore the **global coordinate ring** is `C[Z]^SL2=C[u,v]`. This does not infer the invariant ring from generic orbits alone and does not treat `Z` as affine five-space.

## 3. Quartic invariants, dominance, and quotient map — CONFIRMED

For `H=AX^4+BX^3Y+CX^2Y^2+DXY^3+EY^4`, put `I=12AE-3BD+C^2` and `J=72ACE+9BCD-27AD^2-27B^2E-2C^3`. For the shear `X -> X+tY`, the infinitesimal derivation satisfies `Delta(B,C,D,E)=(4A,3B,2C,D)`. Directly, `Delta(I)=12AD-3(4AD+2BC)+6BC=0`. For `J`, the contributions are `216ABE+72ACD`, `36ACD+27B^2D+18BC^2`, `-108ACD`, `-216ABE-27B^2D`, and `-18BC^2`, which sum to zero. The swap `(X,Y)->(Y,-X)` sends `(A,B,C,D,E)` to `(E,-D,C,-B,A)` and preserves both displayed polynomials. Shear and swap generate the opposite shear and hence `SL2`, so `I,J` are genuine global invariants without a black-box quartic invariant-ring import.

In the frame `L=X,M=Y`, multiplication gives `H=vX^4+uX^3Y+XY^3`, i.e. `(A,B,C,D,E)=(v,u,0,1,0)`. Substitution gives **exactly** `I=-3u`, `J=-27v`, with the unnormalized coefficient convention above. Equivariance carries these identities to every source point, including singular and repeated-root quartics; no discriminant inverse enters them.

The multiplication map `m:Z -> V` is dominant. Every squarefree complex quartic has a chosen linear factor `L_0` and complementary cubic `Q_0` with `R=Q_0(e_0) != 0`. Rescaling `(L_0,Q_0)` to `(lambda L_0,lambda^{-1}Q_0)` preserves the quartic and changes the resultant by `lambda^3*lambda^{-1}=lambda^2`, because `e` scales with `L` and `Q` is cubic. A complex `lambda` with `lambda^2R=1` therefore puts that factorization in `Z`. The image contains the dense squarefree open set. This proves only dominance; it does **not** give a globally polynomial choice of factor or assert multiplication is an isomorphism.

Now any quartic invariant `f` pulls back to some polynomial `h(u,v)` by section 2. The polynomial `h(-I/3,-J/27)` on `V` has the same pullback, and dominance makes `m^*:C[V]->C[Z]` injective. Hence `f=h(-I/3,-J/27)` and `C[V]^SL2=C[I,J]`; the equalities `m^*I=-3u`, `m^*J=-27v` also prove algebraic independence. Thus the induced affine quotient map is the diagonal linear automorphism stated in the producer, inverse `(I,J)->(-I/3,-J/27)`, determinant 81. This argument covers the entire target coefficient space, not only squarefree quartics, because it proves equality of polynomial functions by density.

## Exact excluded conclusions

The source-to-quartic multiplication morphism should not be confused with its two-dimensional invariant quotient. A generic squarefree quartic even has several chosen linear factors and resultant-normalizing scalars; those choices disappear in the quotient calculation. This review confirms only the natural simultaneous-`SL2` quotient under the **fixed resultant-one equation**. It does not exclude other quotient groups, added cuts, nonlinear target surfaces, different factor degrees, arbitrary source parametrizations, or a Keller map obtained by an unrelated construction. The quotient automorphism itself is not a nonautomorphic Keller example. No JC2 resolution or literature priority claim follows.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7964`.
- Body SHA-256:
  `fb0a4992e5336f755d1d44410d93e4ec078ca8942f30f187992a5f753d398147`.
- Frozen basis: `97a752da7c5a86691a690d80dac32e7d981b9eb1`.
