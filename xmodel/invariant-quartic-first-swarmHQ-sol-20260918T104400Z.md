# Independent FIRST: fixed-seed invariant polynomial graphs

Reviewer: swarmHQ (gpt-5.6-sol, high reasoning), independently commissioned
with fresh context. Producer: ROOT (gpt-6-astra). ROOT transcribed the
completed review below after receiving its terminal final and observing
COMPLETED; ROOT owns only the wrapper and integration, not the independent
verdict. Model agreement is not a substitute for the displayed calculation.
Date: September 18, 2026 UTC.
Basis reviewed: ad40ccbb840ff69df89448325809e07510c24fb8.
Evidence: MANUAL with the campaign-accepted Gwozdziewicz Theorem1.1 import.
Lifecycle: completed independent hostile review; all five items CONFIRMED.

## Frozen inputs and read coverage

The reviewer read exactly these three WHOLE frozen files and reported
matching pre/post SHA256 pins:

- [Producer](invariant-quartic-graph-swarmHQ-root-20260918T103700Z.md):
  fc40c79d12f51c4c155ebad9ddd89fb6534c92fb3ff6cd3b2177a3be7092f252.
- FALLACY-v2.md: e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.
- COORDINATION.md: 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e.

No peer result or live coordinator state was supplied. The sole named
import is [Gwozdziewicz, Injectivity on one line, Theorem1.1](https://arxiv.org/abs/alg-geom/9305008):
a complex polynomial plane Keller map injective on an affine SOURCE line
is an automorphism. ROOT checked the primary theorem statement this turn;
the reviewer consumed this precise accepted premise, not a new proof of it.
No scientific computation or new source theorem was used.

## Verbatim completed mathematical review message

Independent hostile review completed 10:42:21 UTC, frozen HEAD ad40ccbb840ff69df89448325809e07510c24fb8. Pre/post SHA256 exact matches all three pins. CONFIRMED (1) w=1−xy/6+x²(z−7y²/6)+x³yz; F=4w²−5w³=−1−7(w−1)−11(w−1)²+…, G=3w²−4w³=−1−6(w−1)−9(w−1)²+…. B numerator x-coeff y/6; A numerator constant/linear zero, x²-coeff 31y²/4−6z; hence whole polynomials and g0=(y/6,31y²/4−6z), Jg0=−1. CONFIRMED (2) T_h≡g0 mod(h), h(T_h)=hγ implies h|h∘g0 with full multiplicity. Shear S(y,v)=(y,v+9y²/7) gives S⁻¹g0S=(y/6,−6v); H=h∘S divides H∘D, equal total degree forces H∘D=λH, λ≠0. If neither y nor v divides H, pure v^j and y^i terms have eigenvalues (−6)^j and 6^(−i); abs equality forces i=j=0, λ=1; no higher pure-v term, so h(0,z)=c≠0. CONFIRMED (3) on y=0 x=c,w=1+c²z, at z=−c⁻² both B_h' = c(8w−15w²) and A_h'=6w−12w² vanish while (hγ)'=(cw)'=c³≠0, contradiction. CONFIRMED (4) remaining y|h gives source y=0 map (0,−6z); or (z−9y²/7)|h gives source sheared v=0 map (y/6,y²/28). Each injective; source shear determinant 1 retains constant nonzero J; accepted Gwozdziewicz Thm1.1 then automorphism. CONFIRMED (5) exact scope is fixed seed, same invariant graph x=h(y,z), all polynomial h; no arbitrary graph construction, no JC2 resolution. No gap/refutation found. Read only exact frozen report, FALLACY-v2, COORDINATION; no peers/current STATE, no protected trees, no files/network/code/CAS/Git mutations.

## ROOT integration and limits

ROOT checked the same expansions and source-line maps. The zero graph
h=0 gives the triangular automorphism g0; every nonzero constant is
excluded by the derivative contradiction. The divisibility statement
retains full multiplicities; no reduced-divisor shortcut or degree bound
on h is used. The plane Keller hypothesis is separately assumed.

This supports promotion of precisely the producer's fixed-seed invariant
x-graph exclusion and its intermediate axes-divisibility implication.
No arbitrary embedded plane, other seed/orientation, graph sent to a
different graph, arbitrary output change, or JC2 conclusion is included.
The proof does not require an ambient Jacobian/generic-degree assertion.
No successor family or new exit-price claim follows from this review.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4087`.
- Body SHA-256:
  `54258547de8cd682c20e90d60a3eb7ff6bb29c1a3c56daf051a2313df614ceea`.
- Frozen basis: `ad40ccbb840ff69df89448325809e07510c24fb8`.
