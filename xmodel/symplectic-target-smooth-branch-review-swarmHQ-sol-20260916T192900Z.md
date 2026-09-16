# Smooth projective branch donors under constant-J birational targets — hostile Sol FIRST

Reviewer: swarmHQ native Sol fallback, requested gpt-5.6-sol; exact hosted model identity is not independently exposed. September 16, 2026. Frozen public commit `01916b439ca74e37e6cbeaf2b0edaf65f6aeaac4`. Evidence: MANUAL proof review with the explicitly named classical imports below. No scientific code, CAS, source fetch, or new theorem import. No promotion authority.

Verdict: **CONFIRMED** for **SYMPLECTIC-TARGET-SMOOTH-BRANCH-1** and its rational-`R` product-cover client, at the producer's stated hypotheses and inherited import tiers. The target change is required to be birational with nonzero **constant** Jacobian, every irreducible old *projective* branch component must be smooth, and the proposed final pair must be polynomial Keller on the **whole** affine source plane. The finite source embedding has no degree bound. This does not establish any general restriction on hypothetical Keller maps outside that donor class.

## Frozen evidence and imports

Before whole reading, the producer `xmodel/symplectic-target-smooth-branch-swarmHQ-root-20260916T192000Z.md` matched full SHA-256 `f839a4b8d6734d73e45850ed3253211f946ca192eab99c30d2663e0deaf8a85a`, artifact-manifest SHA-256 `3fd8d229b4cbc4c5ee51c52d63dd22818e6a1b95f0d4194074182329fdd1918c`, and embedded basis `9aab38787eb24fffc86dacd5859f9c63d439959f`; `artifact_finalize.py verify` returned `VERIFIED` with the expected basis/manifest. These are custody facts only.

The proof consumes, at their already recorded tiers, point-blowup resolution and factorization of birational morphisms of smooth surfaces (Stacks 0C5H/0C5R), connected blowup fibers, purity of the branch locus, trivial connected finite étale covers of complex `A2`, polynomial parametrization of components of a plane polynomial map's nonproper-value set (Jelonek), and Chau's no-`A1` component theorem for nonsingular polynomial plane maps. I check their exact logical uses here, not their underlying source proofs. The reviewed positive-genus and fixed-tripling reports are historical interfaces, not hidden premises; their producer pins match `a3a6793ba8f5c3ebccdd58e61ce8f1fa18ad4dd3d186950d2b961ac668a3a4b9` and `26404af7ecee290db7d0ee68b1a5fed5d8cdd7f7c39f14f2255b007feea3ef1c`.

## A. Projective regularity of the target change — CONFIRMED

Let `omega=dp∧dq` on the old `P2`, with divisor `-3 L_infinity`, and let `omega'=dp'∧dq'` on the new `P2`, with divisor `-3 L'_infinity`. A common point-blowup resolution of a birational `tau` gives smooth `Z` and birational morphisms `pi:Z->P2_old`, `psi:Z->P2_new`, with `psi^*omega'=c pi^*omega`, `c != 0`. Over any finite old point `a`, the first exceptional curve of `pi` has order `+1` in the pulled-back nowhere-zero local area form. At any later point blowup over `a`, the new exceptional order is `1` plus the sum of existing nonnegative zero-divisor multiplicities through its center. Hence **every** `pi`-exceptional divisor above `a` has positive order. There is no old pole over this finite point.

If such an exceptional divisor `E` were not contracted by `psi`, its generic point would map isomorphically to the generic point of a new projective curve. Pullback would then preserve the order of `omega'` along that curve, which is either 0 or -3, never positive. This contradicts the form equality. Thus every exceptional divisor above `a` is `psi`-contracted. The fiber `pi^-1(a)` is connected, so its image is one point; when `pi` is an isomorphism near `a`, the assertion is immediate. On the reduced graph closure of `tau`, the proper projection to `P2_old` consequently has a singleton fiber at `a`. Quasi-finiteness holds after shrinking around `a`, proper plus quasi-finite is finite, and a finite birational map to the normal plane is an isomorphism there. Therefore `tau` is defined at every affine old point **as a map to projective** `P2_new`. Apply the same argument to `tau^-1`, whose Jacobian is `c^-1`, to obtain projective definition on the entire new affine plane. This is not a claim that either rational coordinate pair is affine-valued or polynomial.

The control `tau(u,v)=(u+1/v,v)` has Jacobian 1 and an affine pole, yet its projective formula `[uv+1:v^2:v]` is defined at every finite `(u,v)`, sending `v=0` to `[1:0:0]`. Conversely `beta(u,t)=(t^2-u,t(t^2-u))` maps the smooth line `u=0` to the cusp `(t^2,t^3)` and has Jacobian `u-t^2`, not a nonzero constant. These controls test the exact projective-versus-affine and constant-versus-variable Jacobian distinctions.

## B. Every *new* affine branch component is smooth — CONFIRMED

Resolve `tau^-1` by blowups `pi':Z'->P2_new` and a morphism `psi':Z'->P2_old`. Since `tau^-1` is defined at every new affine point as a projective map, all basepoint blowups can be taken over the new line at infinity, so `A2_new` sits unchanged in `Z'`. A new affine branch component `D` of the finite normalization in `K` is therefore literally a curve in that open subset of `Z'`. The birational morphism `psi'` sends its closure either to an old curve `B` or to a point; there is no third case.

If `B` is a curve, `psi'` identifies the generic DVR of `D` with the generic DVR of `B`. The ramification index in `K/K0` cannot appear or disappear under this field-identification. Since `D` is branch, `B` is an irreducible component of the old projective branch locus. It is smooth by hypothesis, and its strict transform through the point blowups forming `psi'` is smooth; `D` is an affine open of that strict transform. If `psi'(D)` is a point, the closure of `D` is a `psi'`-exceptional curve. Factorization of a birational morphism between smooth surfaces makes every such component a smooth rational strict transform of a point-blowup exceptional curve. Thus `D` is smooth in this case also. In particular exceptional divisors over old infinity cannot be discarded: they may be the branch components visible in the new affine chart.

There must be at least one new affine branch component. If none existed, the connected normal finite cover of smooth `A2_new` supplied by the degree-`>1` field extension would be étale by purity; complex `A2` has no nontrivial connected finite étale cover. This uses neither smoothness of the covering surface nor disjointness of the branch components. Smoothness is componentwise; their union may meet and be singular.

## C. Ramification reaches the actual Keller nonproperness set — CONFIRMED

Assume a finite `C`-field embedding `K⊂L=C(x,y)` yields a whole-plane polynomial Keller pair `F=(p',q')`. For a ramified valuation `v` of `K` above `ord_D`, choose an extension `w` to `L`. Discrete valuation indices multiply in the finite tower, so `e(w/ord_D)=e(w/v)e(v/ord_D)>1`; no bound on `[L:K]` is used. In the finite normalization `T` of `A=C[p',q']` in `L`, `w` has a height-one center over `D`. If `F` were proper over an open neighborhood of the generic point of `D`, quasi-finite Keller `F` would be finite étale there. The normal source would then equal the finite normalization in its **full** function field `L` over that neighborhood, and every index over `ord_D` would be 1. Contradiction. Equivalently, by Zariski Main the source is an open of the full finite normalization; the ramified divisor is missing from that étale open and maps onto `D`.

Thus `F` is nonproper at the generic point of `D`. Its nonproper-value set is a proper closed curve (or empty) for a generically finite polynomial plane map, so the irreducible curve `D` is an actual component of that set, not merely a branch marker on an intermediate model. The argument would fail if one attached only an arbitrary source valuation with point center or silently identified the intermediate cover with the full normalization; the explicit index multiplication and full-field step avoid both errors.

By the named Jelonek input, an irreducible nonproperness component admits a nonconstant polynomial parametrization `A1 -> D`. Since Section B already proved `D` smooth, this map extends to a finite nonconstant map `P1` onto the smooth projective completion `B_D`. Riemann--Hurwitz forces `B_D` to have genus zero. No finite parameter point maps to `B_D\D`, so the preimage of every completion point lies at the sole parameter infinity; hence `B_D\D` has at most one point, and it is nonempty because `D` is affine. Therefore `D ≅ P1` minus one point `≅ A1`. Chau's named no-`A1`-component theorem for nonsingular polynomial plane maps contradicts this. This confirms the general exclusion at precisely those imported tiers; it does not independently reprove Jelonek or Chau.

## D. Rational product-cover client — CONFIRMED

For nonconstant rational `R(s)` of degree `m>=2`, characteristic zero makes `R'` a nonzero rational function. With `p=R(s)` and `q=t/R'(s)`, we recover `t=qR'(s)` in the field, so `K=C(s,t)=C(s,q)` and `K0=C(R(s),q)`. Since `q` is independent transcendental, adjoining it preserves `[C(s):C(R(s))]=m`; hence `[K:K0]=m>1`. Direct differentiation gives `J_(s,t)(p,q)=R'·(1/R')=1` as a rational identity, without asserting regularity at critical points or poles of `R`.

The normalization over the affine `(p,q)`-plane is the product of the finite cover `R:P1_s->P1_p` restricted above finite `p`, with the affine `q`-line. Its affine divisorial branch support is among the vertical lines `p=a` for finite branch values of `R`, including critical behavior at `s=∞` if that point maps to finite `p`. Each projective closure is a smooth line. Any additional divisorial branch component of the normalization over `P2_(p,q)` lies in the complement of the affine chart, namely the single smooth line at infinity. This does not assert unramifiedness at infinity or ignore rational poles. Thus **every** projective branch component satisfies the smoothness hypothesis, whether or not the branch lines intersect at infinity, and the general exclusion applies to all rational `R` of degree at least two.

Degree one is a genuine control: `R(s)=s` makes `K=K0` and the original pair the identity, so the nontrivial-cover/branch argument must not be extrapolated. No Galois, low-degree, simple-branch, polynomial-`R`, polynomial source substitution, or target affine-automorphism hypothesis was inserted.

## Exact limits and history

The product client is narrower in target-change class but broader in rational `R` and source degree than the historical fixed `s-s^109` repair attempt. The positive-genus ramification filter allows arbitrary rational target pairs at a different source-residue-genus hypothesis; it does not exclude this all-rational product cover. The fixed Legendre-tripling filter supplies the accepted valuation/nonproperness/no-line interface for one elliptic donor, not the smooth-projective-branch hypothesis for every donor. Neither previous result is silently substituted for the new branch-transport proof.

The conclusion is **not** invariant under birational target maps with nonconstant Jacobian; the cusp control shows why. It also does not cover old projective branch components with singularities, target subfields other than the fixed `K0`, arbitrary finite donors, or general Keller sources. The source embedding may be any finite rational embedding only because the *resulting* `p',q'` are assumed polynomial Keller on the full plane. No universal construction impossibility or JC2 resolution follows. No new source family, primary-literature priority claim, or automatic descendant is authorized by this review.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11688`.
- Body SHA-256:
  `0974e0b6876b3e511e7c91e7473ef475607d993d892e77cf3a10d30e1afb6883`.
- Frozen basis: `01916b439ca74e37e6cbeaf2b0edaf65f6aeaac4`.
