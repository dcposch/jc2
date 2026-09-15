# Hostile review: fixed-high-coefficient marked-root slices

Reviewer: swarmHQ Sol (gpt-5.6-sol). Frozen public commit
`689a6fce2633c2529df934e89dccd8b0130cdbe8`; producer report SHA-256
`a56a1de74b34a283e1c4f32bc4e316f0da372f4c75a18c60afd1fd96589333e5`.
Evidence: MANUAL. Lifecycle verdict: independent different-model FIRST,
`CONFIRMED` at exactly the displayed-formula scope. Novelty remains UNKNOWN.
This is neither an audit of the external manuscript nor a JC2 result.

## Claim-by-claim verdict

1. **CONFIRMED uniformly for every `n>=4`.** Fixing all high coefficients gives
   `U=Spec C[x,y,1/(1+xy)]`, plus exactly `n-2` reduced affine planes precisely
   when `c_n=0` and `c_(n-1)!=0`.
2. **CONFIRMED.** The CRT identity is global and excludes hidden gluing and
   embedded components; the triangular determinant is `p^(2n-3)`.
3. **CONFIRMED.** On each extra plane the low outputs are the stated affine
   automorphism, with determinant `rho^5/2`.
4. **CONFIRMED.** No dominant morphism `A2->U` exists by the nonconstant-unit
   obstruction.
5. **CONFIRMED with the stated caveat.** Arbitrary polynomial substitutions with
   Keller low outputs must dominate an extra plane, but then merely reproduce an
   arbitrary plane Keller pair up to affine recombination; they are not excluded.

## Independent algebraic attack

Let `p=1+xy`, `m=n-1`, and `b=p*z_n+(-1)^m y^m`. Direct highest-coefficient
extraction gives `C_n=pb`. Using `1-p=-xy` gives
`x^m b=p*x^m*z_n+(1-p)^m`, and the displayed Bezout formula evaluates to
`p sum_{j=0}^{m-1}(1-p)^j+(1-p)^m=1`. Thus `(p,b)=1` already in the
original ring and remains so after every other coefficient quotient.

On `D(p)`, variables `z_n,...,z_4` occur successively with diagonal `p^2`
and `z_3` with `p^3`. There are `n-3` former variables, so the determinant is
`p^(2(n-3)+3)=p^(2n-3)`. This proves the whole localized ring is `C[x,y,1/p]`.
If `c_n!=0`, `pb=c_n` makes `p` a unit. If `c_n=0`, comaximality yields the
scheme-level product of the `p=0` and `b=0` quotients, not merely a pointwise
cover; the `b=0` factor again has `p` invertible.

In the `p=0` quotient, `x` is invertible and `y=-1/x`. Expanding the defining
formula gives the producer's equation (3), whose `T^(n-1)` coefficient is
`-x^{-(n-2)}`. Hence this factor is zero when `c_(n-1)=0`; otherwise
`x^(n-2)=-1/c_(n-1)` has `n-2` distinct nonzero complex roots. CRT across
those simple roots and the remaining triangular equations leave exactly
`C[z3,z4]` on each factor, with no nilpotents or embedded pieces. Reading the
`T^2` and constant coefficients gives
`A2=rho^2 z4-(n-1)(n-2)/(2rho)` and
`A0=(n+2)rho/2-rho^3 z3/2`; their determinant in `(z3,z4)` is `rho^5/2`.
The `n=4` endpoint is consistent: there are no `z5,...,zn` equations and two
simple root planes in the exceptional case.

The unit argument is also scheme-correct. A dominant map `A2->U` would inject
`C[x,y,1/p]` into `C[s,t]`; the unit `p` must map to a scalar `lambda`, killing
the nonzero element `p-lambda`. For a substitution `h`, dominance of its Keller
low outputs forces its image closure to have dimension two and hence equal a
component of the two-dimensional slice. Connectedness puts it in one CRT factor;
the unit obstruction eliminates `U`. On an extra plane the low outputs are only
an invertible affine change of `(z3 o h,z4 o h)`. This is JC2 passthrough, not
an exclusion unless `h` was already known to parametrize the plane isomorphically.

## Controls and exclusions

- The explicit `n=4` coefficients verify the signs and the Bezout endpoint.
- Exceptional planes are positive controls for reducedness and low-output
  invertibility; `c_n!=0` is a positive control yielding only `U`.
- Changing target-coordinate combinations, nonlinear constraints, rational
  substitutions, or other donors is outside scope. No generic degree, full Keller
  property of the donor, source existence, or plane counterexample follows.
- The formula is taken as the definition. No external theorem/source audit or
  network access was needed.

## Custody

Work began `2026-09-15T12:59:23Z`. Before reading I verified the input against
artifact basis `18be9c16c95318c2eea9a2cef76e9ea476985482` and manifest SHA-256
`40652ba983ce4dba9fd8337830b16947ddf502e25d7a43fcf5c3acc648909204`;
report and manifest were `0444`. Whole-read pre/post hashes were the unchanged
expected producer hash above. No network, CAS, science Python, AWS, paid lane,
agent, successor, shared edit, Git mutation, or protected-tree access occurred.

## COLLISIONS

status: EMPTY

- NONE -- canonical checker found no explicit `OPEN[...]` entry.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4633`.
- Body SHA-256:
  `8b139280dc9a114569e0fa71785ce4afbb896db22e276aeb4c5a85d8d6a2dfcf`.
- Frozen basis: `689a6fce2633c2529df934e89dccd8b0130cdbe8`.
