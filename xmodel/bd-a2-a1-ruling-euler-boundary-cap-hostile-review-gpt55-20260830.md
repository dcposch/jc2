# Hostile review: `A1` ruling and Euler boundary cap

Overall verdict: `CONFIRM_WITH_CORRECTIONS`.

The producer is mathematically sound in its main theorem, but promotion should
carry four wording repairs: the actual `A2 -> U` morphism is a charged
proper-block input, not reconstructed from the compactification; the
Miyanishi-Sugie citation should be stated as the surface `A1`-ruled theorem
together with the standard extension-to-fibration form; the fibre class
equations live only on an adapted completion; and all Euler counts must use
reduced distinct support components, not divisor multiplicities.

## Sources Checked

Local custody is consistent. The reviewed file has full SHA-256
`a2d4a7eef07700983c039d12763d9730efde0f373840e5909a7b6e276f620016`,
and its artifact record gives body SHA-256
`3cb1243350658fc146671cf7723b96c65c6836f8852582e72cd0781546df596d`.
The four charged integrations match their advertised full hashes:

- `xmodel/bd-a2-normal-singular-quadratic-incidence-coordinator-integration-sol56-20260830.md`
- `xmodel/bd-a2-rational-forest-coordinator-integration-sol56-20260830.md`
- `xmodel/bd-a2-normal-singular-f5-bridge-coordinator-integration-sol56-20260830.md`
- `xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md`

External theorem check used:

- Miyanishi-Sugie, `doi:10.1215/kjm/1250522319`, https://doi.org/10.1215/kjm/1250522319
- Dubouloz-Kishimoto, Section 1.2.2, https://www.numdam.org/articles/10.24033/bsmf.2692/ and https://arxiv.org/pdf/1212.0521
- Gurjar-Miyanishi, Lemmas 2.2-2.3, https://doi.org/10.1307/mmj/1114021083

## Itemized Verdict

1. `U = X minus Supp(H+R_X)`: `CONFIRM_WITH_CORRECTIONS`.

The open is the correct maximal open for this packet, provided the promoted
proper-block hypothesis is stated explicitly as an actual dominant morphism
`g1:A2 -> U`. The block integration gives an actual morphic first leg in the
proper block setting; it is not a rational map and no argument here should
replace it by the image or by a smaller open. If older packets delete
additional named missed loci, their image is still contained in this larger
`U`; dominance is not lost by allowing missed points to remain in `U`.

Affineness is correct: `H+R_X ~ 3A+B`, the restriction of an ample ambient
class, so the complement of its support is affine. Smoothness is correct
because the normal-singular incidence integration proves
`Sing X subset Supp(R_X)`. Rationality is supplied by the resolved conic
fibration. Units are constant because pullback along dominant `A2 -> U` sends
`O(U)^*` into `C[x,y]^*=C^*`. Negative log Kodaira dimension follows by
injecting logarithmic pluricanonical forms along the dominant generically
finite surface morphism. Affine coefficient basepoint rows remain outside the
finite-near-infinity scope; Stein-contracted affine ramification carriers are
still carriers in `Supp(R_X)` and must be counted in support.

Repair: state "charged actual dominant morphism `A2 -> U`" every time this
input is used. Do not derive it from the compactification or from the
first-leg image.

2. Miyanishi-Sugie and the base: `CONFIRM_WITH_CORRECTIONS`.

The exact usable theorem is: over an algebraically closed field of
characteristic zero, a smooth affine surface has `bar-kappa = -infinity`
iff it is `A1`-ruled; in the surface case the cylinder projection extends on
the surface itself to an `A1`-fibration over a smooth curve, with general fibre
`A1`. No finite base change is part of this surface conclusion. Finite base
changes appear in deformation or family contexts, not here.

Thus `rho:U -> C` is legitimate after replacing the base by the smooth image,
and it is surjective by definition. Rationality of `U` gives rationality of
`C` by Luroth: `C` has function field a one-dimensional subfield of
`C(U)=C(x,y)`. Hence the smooth projective model of `C` is `P1`, and
`C=P1 minus S` for finite `S`. The pullback `O(C)^* -> O(U)^*` is injective;
since `O(U)^*=C^*`, an affine rational base can have at most one point at
infinity. The complete base is not excluded. The exact dichotomy is
`C=A1` or `C=P1`; `G_m` and `P1` minus at least two points are killed by units.

Repair: cite the theorem as Miyanishi-Sugie plus the standard surface
extension-to-fibration formulation recorded in Dubouloz-Kishimoto 1.2.2, not
as a weaker "there exists a cylinder somewhere" statement and not as a
finite-base-change theorem.

3. Adapted completion: `CONFIRMED`.

After resolving only boundary base points of the rational extension of
`rho`, one obtains a smooth SNC completion `(V,D)` with a `P1`-fibration.
For the completed general fibre class `L`,
`L^2=0`, `K_V.L=-2`, and `D.L=1`. These are just fibre self-intersection,
adjunction on a general `P1`, and the fact that the open fibre is `A1`.
The class is primitive because it meets the unique horizontal boundary section
once; it is nef, effective, and basepoint-free because it is a morphism fibre.
There is exactly one horizontal component `S0`, with `L.S0=1`, and all other
boundary components are vertical.

For affine base `A1`, the completion over `P1` contains a complete boundary
fibre above the missing point, with connected fibre graph and primitive
positive multiplicity vector spanning the fibre intersection kernel. For
complete base `P1`, no such boundary fibre is forced.

The producer is right that these equations cannot be imposed on the current
raw `D9` marking. Polynomial rulings such as `x+y^n` on `A2` show unbounded
boundary base-point resolution before the fibre class acquires
`L^2=0`, `K.L=-2`, `D.L=1`. Fixed-completion lattice finiteness is safe only
after an adapted completion has been chosen: then the boundary supports an
ample divisor, the orthogonal complement is negative definite, and integral
solutions with a chosen horizontal component are finite before the separate
primitivity, nefness, effectivity, and semiampleness tests.

4. Euler identity: `CONFIRMED`.

On the minimal Du Val resolution, `e(Xtilde)=13`: adjunction gives
`K=-A+B`, hence `K^2=-1`, and rationality gives `chi(O)=1`, so Noether gives
`e=12-K^2=13`. Picard rank is therefore `11`.

Let `r` be total ADE rank, `c` the number of distinct nonexceptional strict
components of `Supp(H+R_X)`, and `b` the number of later embedded-resolution
boundary blowups. Every ADE exceptional curve is in the resolved ramification
support. `Supp(R_X)` is connected because `R_X` is an effective ample Cartier
divisor of class `2A+B`; `Supp(H)` is connected in the reduced finite
quadratic infinity scope; and `H.R_X=8` forces the connected supports to meet
unless they share a carrier, in which case the union is connected anyway.
The rational-forest theorem makes the final boundary a connected rational
tree.

After the `b` boundary blowups, `e(V)=13+b`, the boundary has
`N=r+c+b` components, and `e(D)=2N-(N-1)=N+1`. Hence
`e(U)=e(V)-e(D)=12-r-c`. Each boundary blowup adds one to both `e(V)` and
`e(D)`, so all embedded-resolution blowups cancel.

Repair: keep `c` as a reduced support count. If `H` and `R_X` share a strict
carrier, count it once. Do not assume the projective ramification divisor is
reduced; multiplicities never enter the Euler formula. In the reviewed F5
scope only, the local `h,h_z` argument excludes common nonexceptional
`H/R_X` components and gives `c=s+k=3+k`.

5. Fibre Euler and caps: `CONFIRMED`.

Gurjar-Miyanishi Lemma 2.2 applies to the normal affine surface `U` and says
that every reduced fibre support of an `A1`-fibration is a disjoint union of
curves isomorphic to `A1`; scheme multiplicities do not affect topological
Euler characteristic. If `r_t` is the number of reduced irreducible components
of the fibre over a degenerate value, stratification gives

```text
e(U)=e(C)+sum_t(r_t-1).
```

All summands are nonnegative. Combining this with `e(U)=12-r-c` and
`C=A1` or `P1` yields `r+c<=11`, and in the complete-base branch
`r+c<=10`. If `r+c=11`, then `e(U)=1`, so `C=A1` and every reduced fibre is
irreducible. Multiple irreducible fibres are not excluded.

In F5, `s=3` and `k>=1`, so `c=3+k` and the cap becomes
`r+k<=8`; hence `r<=7`, and `k>=2` gives `r<=6`.

The weak cap `r+c<=11` duplicates the unit/Picard localization injection:
`O(V)^*/O(U)^*=0` injects the free group on the `r+c+b` boundary components
into `Pic(V)`, whose rank is `11+b`. The new content is the `A1`-fibration,
the `P1` sharpening, the equality classification, and the adapted ruling
class, not the weak numerical cap by itself.

6. Controls: `CONFIRMED`.

The `A2` control is valid. Start with
`P1 x P1 minus (one horizontal ruling union one vertical ruling)`, and blow up
nine boundary points. The open remains `A2`, while `e(V)=13` and the boundary
has eleven rational tree components. This shows the weak Euler/Picard cap is
numerically sharp as a completion invariant, not that such a boundary occurs
in the incidence problem.

The complete-base control is also valid. On `F_n`, let
`S ~ C0 + mF` be a smooth ample section with `m>n`, and put
`U0=F_n minus S`. Then `U0` is smooth rational affine, and projection to
`P1` has every fibre `P1` minus one point, hence `A1`. The exact sequence for
the complement of the single irreducible section gives
`O(U0)^*=C^*`, because `[S]=C0+mF` is non-torsion in `Pic(F_n)`.
Over any affine line in the base, the complement is a trivial `A1`-bundle,
so it contains a dense open `A2`; the inclusion is etale and dominant.
This control has generic degree one, so it does not rule out a future
proper-block obstruction using `d1>=2`.

7. Scope: `CONFIRMED`.

This packet is not a bounded completion-adaptation theorem, not a
reduced-ramification theorem, not an effective `D9` configuration, not a
finite-algebra result, not an etale proper block, not a map, not a
counterexample, and not a JC2 result. It is a surface-theoretic necessary
condition inside the charged normal exact-quadratic proper-block first-leg
scope.

## Promotion-Ready Theorem

Let `X subset P2 x P1` be a normal irreducible quadratic incidence surface of
class `2A+3B` in the promoted proper cubic-block first-leg scope. Let
`H~A`, let `R_X~2A+B` be the effective Cartier ramification divisor, and put
`U=X minus Supp(H+R_X)`. Assume the charged actual dominant morphism
`A2 -> U`.

Then `U` is a smooth rational affine surface with `O(U)^*=C^*` and
`bar-kappa(U)=-infinity`. Consequently `U` admits a surjective
`A1`-fibration `rho:U -> C` over a smooth curve, with no finite base change,
and `C` is exactly `A1` or `P1`.

If `r` is the total ADE rank and `c` is the number of distinct
nonexceptional strict support components of `Supp(H+R_X)`, then

```text
e(U)=12-r-c,        r+c<=11.
```

If `C=P1`, then `r+c<=10`. If `r+c=11`, then `C=A1` and every fibre has
irreducible reduced support, although an irreducible fibre may be multiple.
On any adapted completion resolving the boundary base points of `rho`, the
general completed fibre class `L` is primitive, nef, effective, and
basepoint-free, satisfies `L^2=0`, `K.L=-2`, `D.L=1`, and meets exactly one
horizontal boundary section once. These lattice equations are not valid on
the raw `D9` marking before adaptation.

In the reviewed reduced finite F5 scope, `H` and `R_X` have no common
nonexceptional component, `c=3+k` with `k>=1`, and therefore

```text
r<=7,        k>=2 => r<=6.
```

## Cheapest Successor

First apply `r+k<=8` to the F5-decorated global fibre rows, keeping affine
ADE trees and ramification carriers distinct and preserving support
multiplicities only where they are actually used. Split the equality cell
`r+k=8`: it is necessarily `A1`-base with all reduced fibres irreducible.
In parallel, prove either a bounded boundary-adaptation lemma before running
any raw `D9` fibre-class enumeration, or a block-specific `d1>=2`
obstruction to the `P1`-base control. Those are the cheapest exact next
gates; Euler caps alone do not close another stratum.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11922`.
- Body SHA-256:
  `f6de61b9940677436f5303538c028ebda6c97b7ae56ce77da480cfeba4703941`.
- Frozen basis: `b0f4d09cf8b9aa3524247cb746a2610a6e49542f`.
