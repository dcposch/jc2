# Pole-free zero support: independent hostile review

Status: CONFIRMED at the exact scope below; MANUAL, not a formal certificate.
Producer: [pole-free-zero-snc](pole-free-zero-snc-swarmHQ-root-20261020T104840Z.md).
Producer full SHA256:
`a438835a71f6c3ec69b6807064a047620f5676b3414654aff5e9b9259e7b0d5e`.
Producer manifest SHA256:
`eaed374d9e6d4cb80f4700ec3c08f4245f877e6292b4299d89f3f7db4e70b2a1`.
Independent reviewer: retained Sol5.6-assigned native seat
`/root/affine_radial_first_sol56_2157`; actual hosted model identity unverified.
ROOT transcribes the terminal review and integrates its exact scope; no paid
model-CLI receipt, formal verification, or external novelty is claimed.
ACK 2026-10-20T10:56:30Z; substantive partial10:58:01Z; terminal10:58:19Z.

## Confirmed statement

Let S be a smooth projective complex surface and omega a nonzero rational
two-form. Let U be its regular locus (zeros are allowed).
If C(S)=C(u,v) and omega=c du wedge dv for c in C*, the reduced positive
zero divisor on U is simple normal crossing: each irreducible component
is smooth, distinct components meet transversely, and at most two meet
at any point. Multiplicities need not equal one.

Thus cusps, self-nodes, tangencies and triple intersections of the reduced
positive support at a pole-free point obstruct FIELD-GENERATING rational
Darboux coordinates in the same function field.

## Independent proof and hostile checks

Set r=(u,v):S-->P2. Field equality makes r birational and
omega=r*(c du wedge dv); the target form has divisor -3L_infinity.
Resolve r as pi:W->S and h:W->P2.
For p in U, every pi-exceptional divisor over p has positive order:
writing omega=a ds wedge dt, the first blowup gives order
1+mult_p(a)>=1. The same local formula applies after further point
blowups, since pullback of a regular form remains regular.

If one such divisor dominated a target divisor, the corresponding
birational DVR valuations would agree, forcing order0 or-3, a
contradiction. Therefore h contracts every curve in the connected
pi-fiber to a point, and the whole fiber has one image.
The reduced graph over S has singleton fiber at p. Properness plus
the openness of the quasi-finite locus gives finiteness near p;
finite birational descent to normal S makes the graph projection
an isomorphism there. Thus r is regular throughout U.

Resolve the remaining indeterminacy only outside U, so pi is an
isomorphism over U. Every positive-order prime meeting U is
h-exceptional: its generic point lies in U, and domination of a
target divisor would again force order0 or-3.
The reduced h-exceptional divisor is SNC, because a birational
morphism of smooth projective surfaces factors into point blowups;
the total exceptional support remains SNC after each such blowup.
Every reduced subdivisor is SNC. Transporting it through pi|U
proves the claimed smoothness, transversality and absence of triple
points, hence also excludes cusps and self-nodes.

There is no hidden self-identification: pi is literally an
isomorphism over U. Nonexceptional positive components are excluded
by the valuation argument. Multiplicities are irrelevant after
reduction.

The descent step is an extension of the retained zero-free-model
descent argument from source nonvanishing to source regularity.
It is not a newly independent mechanism. Standard surface
resolution/factorization and normal finite-birational descent remain
the named mathematical imports; no new external source was admitted.

## Conditional finite-cover consequence and countercontrol

Let pi:X->Y be finite dominant between normal projective complex
surfaces, x and y=pi(x) smooth, and eta regular and nowhere zero
near y. Resolve X away from a smooth neighborhood of x.
Then pi*eta is regular near x and its order along each ramification
prime is e_E-1. If the reduced ramification divisor is non-SNC at
x, the surface theorem excludes field-generating rational Darboux
coordinates for pi*eta on C(X).

This does not cover finite SOURCE-FIELD enlargement. It does not
construct eta, permit arbitrary target area changes, or force a
non-SNC ramification point in any actual normalization.
Scalar-constant-Jacobian birational target changes preserve the
stated area form up to its allowed nonzero scalar.

For the control F=x, G=y^3/3-x^3*y, direct differentiation gives
dF wedge dG=(y^2-x^3) dx wedge dy, with a cuspidal zero divisor.
The induced field extension has degree3, not1, so this exact regular
form does not contradict the theorem. The control is NON-KELLER.
No CAS computation was used.

## Review custody and disposition

The reviewer reports WHOLE reads of packet1--110, producer1--134
and its manifest, and positive-zero FIRST1--126. The zero-free FIRST
1--67 was reused from the reviewer's own completed exact-pin whole read.
New whole governing reads: frozen STATE1--200, RUNBOOK1--434,
RESTRICTIONS1--253, APPROACHES1--959. Remaining required governing
inputs were reused only from the reviewer's own exact-pin whole reads.
Whole-set metadata preceded any body reads; artifact_finalize
verification returned VERIFIED. All pre/post hashes matched, including
the producer and manifest above and the contextual FIRST hashes:
positive-zero `35087973000fde198346039512be54f2ea49297a6669a4018c47b234d87f084b`;
zero-free `6d710eeaa9a0414cfa91eb00918920ede22c7b5cae331b0630145f962e33dca9`.
Producer/manifest remained regular0444,6888/694bytes.
Packet SHA `fdc13e103f7be0d38f799aecb56b4972eb4200e2bd90acd107d8cbbe5f44bd3d`;
frozen STATE SHA `8fe3cdc6830c2b585a5f34133793ec6fd6debdbc12fe5478d9052041ebff755e`.

No deviations, unread charged scope, writes, network, history queries,
CAS, Git mutation, model CLI, descendants, or protected-tree access
were reported. OPEN(S): none. ROOT verified terminal registry state,
matching canonical input/manifest/context/packet hashes and the
canonical artifact verifier before this integration.

Disposition: CONFIRMED only as a necessary birational volume criterion.
It strengthens the retained multibranch obstruction at pole-free
points; it does not supersede the separate shifted-order restriction
at SNC crossings. No forced actual boundary configuration, B=R,
JC2 proof/counterexample, or new degree bound follows.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6241`.
- Body SHA-256:
  `f5e2c22e5bc2f44b185d0829640f326e92bb878809597863e17cd6480cfe53f5`.
- Frozen basis: `407f3b23e3168e32c44404fe9087a91dc73d53fd`.
