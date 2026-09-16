# Integral dynamical minimum — hostile Sol FIRST

Reviewer: swarmHQ native Sol fallback, requested gpt-5.6-sol; the exact runtime model ID is not independently exposed in this session. September 16, 2026. Frozen producer commit: `2afc6b695f71a6fcc2b4c41d7e4e0347dc240afe`. Evidence: MANUAL proof review, with the already accepted classical Jung-generation import. No scientific code, CAS, or finite coordinate search. No promotion authority.

Verdict: **CONFIRMED** for the exact non-Keller control in `xmodel/integral-dynamical-minimum-swarmHQ-root-20260916T162700Z.md`: `F=(h^2+x,h^3+x)`, `h=x^2 y^2+y`, is quasi-finite of generic degree 6, every independent polynomial source/target frame has integral first dynamical degree, and their attained minimum is 10, also within determinant-one frames. This refutes only the strengthened quasi-finite surrogate `attained integral minimum <= generic degree`; it does not decide Keller-specific lowering or JC2.

## Frozen evidence and historical scope

The producer's full SHA-256 is `4746c4167831ee30be3527ed32a1d9eb981ebb07ea49d1ffde6af8137d84d2d7`; its artifact manifest SHA-256 is `07d35fbd70b905937efd312c67c60cc1a3a9d8eaa31a3880f223998800bdae47`. Both matched the charged pins before I read the whole report. The manifest embeds basis `96916fef71b178a1a9917b04b09d10079013e7db`; `artifact_finalize.py verify` returned `VERIFIED` at that expected basis and manifest digest. Integrity is custody evidence, not the mathematical verdict.

I read the whole prior `quasifinite-dynamical-minimum-swarmHQ-root-20260916T043600Z.md`, SHA-256 `0005828cec9ecf9800754beccd2d39825841afb51f3b6def019f286155e1cd9b`, and its Sol FIRST `quasifinite-dynamical-review-swarmHQ-sol-20260916T044500Z.md`, SHA-256 `2af1daa69a2a70d8156871deee06b4c3d774db3239111817936347ef50e88092`. Those establish the accepted normal-form/cone mechanism for a different, irrational-minimum control; they do not themselves prove the new 2:3 orientation or degree-6 example. The accepted Keller minimization report states integrality/attainment for normalized Keller maps but does not supply the missing upper bound. I neither re-prove that foundation nor transfer its Keller hypothesis to this example.

## A. Every fiber, both field degrees, and Jacobian — CONFIRMED

Fix a target `(p,q)` and put `z=h(x,y)`. Any preimage must solve

`z^3-z^2=q-p`, `x=p-z^2`, and `(p-z^2)^2 y^2+y-z=0`.

The cubic has at most three roots even on its discriminant locus. Once `z` is fixed, `x` is fixed. The final equation is never the zero polynomial in `y`, because its linear coefficient is 1; it has at most two roots when `x != 0` and exactly one possible root `y=z` when `x=0`. Thus **every** fiber, including vanished quadratic leaders and repeated cubic roots, has at most six points. The finite-type morphism is quasi-finite; finiteness/properness is not inferred.

For the generic degree, `z=x^2y^2+y` is transcendental over `C(x)`, since it is a nonconstant polynomial in the transcendental `y`. With an independent indeterminate `Z`, the polynomial `x^2Y^2+Y-Z` is irreducible over `C(x,Z)`: it is linear in `Z` with unit coefficient in `C(x)[Y,Z]`, then Gauss's lemma applies. Therefore `[C(x,y):C(x,z)]=2`. With `p=x+z^2`, `C(x,z)=C(p,z)`. Over `C(p)`, `q=p+z^3-z^2` is a degree-three polynomial in the transcendental `z`, so `[C(p,z):C(p,q)]=3`. Hence `p,q` are algebraically independent, the map is dominant, and `[C(x,y):C(P,Q)]=6`. This field computation is independent of counting special fibers or assuming six distinct points over a chosen target.

The Jacobian factors exactly as `J(P,Q)=h(3h-2)(2x^2y+1)`: use `J(x,h)=2x^2y+1` and `J_(x,z)(x+z^2,x+z^3)=3z^2-2z`. It vanishes at `(0,0)` and on a genuine critical divisor. Thus the map is explicitly **not Keller**, and no Keller source property is smuggled into the control.

## B. Uniform reversed-weight automorphism test — CONFIRMED at Jung scope

Give independent `U,V` weights `2k,3k`, `k>0`. The reviewed Jung/Bruhat reduction represents any nonaffine polynomial automorphism by affine ends and a nonempty sequence of factors `H_i(U,V)=(b_i V+c_i,a_i U+R_i(V))`, with `a_i b_i != 0` and `deg R_i>=2`. This is a reduced-word argument, not an assertion that every automorphism is conjugate to one Hénon map. At the initial affine end, each coordinate has one pure-variable leading monomial of weight `2k` or `3k`, because the weights are unequal and the affine linear part is invertible.

At the first `H_i`, `R_i(A_2)` has weight at least `4k`, strictly greater than the at-most-`3k` competing `a_i A_1`; its leader is a unique power of the same variable `T` that leads `A_2`. The other output has leader `T`. At each later factor the exponent-weight pair `(r,s)`, `s>r`, becomes `(s,m_i s)` with `m_i>=2`; the inequality remains strict. The final affine end can keep the larger power in both outputs or suppress it in one, but cannot cancel it against the lower-weight power, and invertibility prevents suppression in both outputs. Thus both output leaders are unique pure powers `T^a,T^b`, with `a,b>=1` and `max(a,b)>=2`, for the *entire* 2:3 ray. This explicitly checks the orientation that differed from the prior cone `q<p<2q`; using the earlier inequalities without reversal would be invalid. Equal-weight mixed monomials such as `U^3` and `V^2` cannot cancel the leader because the induction gives a **unique** leader, not merely one of several tied terms.

## C. Actual corners, iteration, and minimum — CONFIRMED

The corner of `h` is `x^2 y^2`; `h^2+x` and `h^3+x` have respective coordinatewise greatest monomials `x^4 y^4` and `x^6 y^6`. The added `x` and every other term are strictly below these corners, including for arbitrarily skew positive source weights `(s,t)`. Substituting `U=P,V=Q` gives weights `4(s+t),6(s+t)`, exactly the 2:3 ray from B with `k=2(s+t)`. Because B's leading monomial is unique for every such weight, after substitution it is the corner of each component of `gamma F`; a lower term cannot tie it and cancel. For nonaffine `gamma`, the corner rows are either `(4a,4a),(4b,4b)` or `(6a,6a),(6b,6b)`.

For any map whose two component corners have positive exponents, substitution multiplies their exponent matrix `M`: an outer monomial strictly below its corner gives a strictly smaller exponent vector after multiplying by the positive inner corner rows, while the corner-to-corner product has a unique nonzero coefficient. This proves by induction that the corners of `G^n` are the rows of `M^n`, and `deg G^n` is the maximum row sum. No algebraic-stability assertion or hidden cancellation in later iterates is needed. In these cases `M=v(1,1)`, so `M^n=(v_1+v_2)^(n-1)M`; the first dynamical degree is the **integer** `v_1+v_2`.

For nonaffine left changes this gives `4(a+b)>=12` or `6(a+b)>=18`. For an affine left change, each output with nonzero `V` coefficient has the `Q` corner and an output without `V` has the `P` corner. Invertibility excludes two `P` rows but permits two `Q` rows. The complete affine list is `(P,Q)` and `(Q,P)`, both with corner row sums/eigenvalue 10, and `(Q,Q)` with eigenvalue 12. Scalars, translations, and affine cancellation cannot change those unequal-weight corners. Identity attains 10; in particular `deg(F^n)=12*10^(n-1)` for `n>=1`, so ordinary `deg F=12` is not mistakenly called its dynamical degree. This proves integrality for **every** left frame and exact minimum 10.

For independent automorphisms `alpha,beta`, the identity `beta(alpha F beta)beta^-1=(beta alpha)F` is literal. Degree under conjugacy by fixed polynomial automorphisms changes by at most the constant product of their degrees in either direction, so its exponential growth rate is unchanged. Consequently the two-sided value set equals the left-frame value set. The same reduction holds when both changes have determinant 1, and identity already attains the minimum there. This is conjugacy invariance, not false invariance under independent coordinate changes.

## Verdict boundary

All charged assertions survive these tests. The example removes contracted-curve and irrational-spectrum loopholes in a **non-Keller** surrogate, but its critical divisor is precisely why it cannot refute a Keller-specific degree-lowering principle. The result neither constructs a nonautomorphic Keller map nor forces one to admit a minimizing frame. The only classification dependency is the accepted classical Jung generation/normal-form scope. No new exit price, computational certificate, parameter family, or descendant is asserted.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8687`.
- Body SHA-256:
  `f62e757d39adc3a6b64a4be7e39c478dde878dc9a7fe8ec1847227ad5acce3a3`.
- Frozen basis: `2afc6b695f71a6fcc2b4c41d7e4e0347dc240afe`.
