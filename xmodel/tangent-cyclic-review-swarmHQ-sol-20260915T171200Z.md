# Hostile review of the cyclic tangent-coordinate obstruction

Reviewer: swarmHQ Sol (gpt-5.6-sol), September 15, 2026. Actual startup
2026-09-15 17:12:27 UTC. MANUAL / BOOK-relative review.

Reviewed contribution commit: `6b083ecba093ba987062b8fcf7ea97e9318b0db7`.
Frozen producer full SHA256
`93c560753a0475cafeff9c13a0e489d34a30d1fbc192eb8aa29c0bec5892dd81`,
manifest `36fbad531f746944496fcc54949c348fe7e2cef33cc41b4cbdbf27fcfb9e56f5`.
Publication addendum full SHA256
`a95c9427bd3108d663d8acff2e22a0b9fc1bf1f449732a494115890db089014b`,
manifest `01b4dc4ab288f006258bbd1f83f8f8549e69d93ab948d0bce0260cc3efebac71`.
The producer and addendum were whole-read after their seals, modes, manifests,
and commit blobs were checked. The producer's pre-review and post-review hashes
are identical. The earlier accepted theorem and its Fable intake were also
whole-read for scope comparison, not re-reviewed as foundations.

## Verdict

**CONFIRMED**, exactly for condition (S0) in the literal WHOLE tangent
construction, relative to the producer's named classical imports: polynomial
A1 parametrization of plane-map nonproperness curves (Jelonek),
Abhyankar--Moh--Suzuki straightening, triviality of finite etale covers of A1
over C, and constructible compactly supported Euler characteristic. I found no
missing mathematical implication in the charged chain.

This does not cover common nonzero roots of A and B, arbitrary tangent donors,
arbitrary projections or embeddings, all Keller maps, or JC2. It confirms an
unbounded construction-route exclusion, not all-family closure.

## Hostile reconstruction

1. Put n=m+1. The map `(s,t) -> (C,w,D,E)` has the stated mu_n symmetry.
Bezout applied to `w^(m-1)A^2` and B gives the monic relation for `t^n`;
the monic p-relation gives integral w, and `s^n=C` gives integral s. The
image is consequently the closed sweep surface. Since `deg q=deg p+1`,
the degree of `C(w)/C(p,q)` divides consecutive integers, so it is one;
the invariant normal ring is therefore the normalization, not a larger
auxiliary cover. After the possible order-two reflection quotient, the
residual weights `(1,-e)` are faithful on either punctured axis and hence
the cover is etale away from the origin. At a=0 its whole reduced image is
the E-axis, by finiteness.

2. Admissibility forces a nonzero root alpha of p': if there were none,
p and q would be the forced monomials, and their two values at gamma0
would contradict polynomiality. Along `a^e t=alpha`, the normalization
map loses t-rank away from the quotient origin, excluding a coordinate
plane. Thus a hypothetical target/source coordinate pair has nonconstant
restriction to the sweep.

3. On C nonzero, the monic W-cover has precisely the actual source after
deleting gamma=0. A generic coordinate cut does not acquire a whole deleted
component; deleted points remain in its closure and force x to infinity.
Hence their images are actual nonproperness curves of the same plane Keller
restriction. A generic normalization cut avoids the isolated quotient point
and exceptional locus componentwise. The named curve imports then make its
pullback generic fibre a disjoint union of A1s, so the disconnected-fibre
argument gives `f=P(z0)` for a plane coordinate z0.

4. The generalized coordinate lemma is sound. On the critical C-star,
the restricted Laurent polynomial has nowhere-zero derivative; its derivative
is a monomial, and the logarithmic exponent is excluded because it cannot be
a Laurent derivative. The coordinate fibre at the integration constant is
disjoint from the critical C-star. Its invertible function
`a^e t-alpha` is constant; a nonzero value would make both a and t units on
A1 and hence constants. The fibre is therefore one coordinate axis, and the
t-derivative condition selects a. Residual invariance then gives
`h(phi)=P0(a^r)=P0(C)` with positive degree.

5. For generic c, the C=0 target cut avoids D=0. The x=0 source component
maps triangularly and bijectively, while gamma=0 maps by `(D,E)=(2/x,u/x^2)`
bijectively to D nonzero. These are disjoint source components, so the count
is exactly two sheets. Since N>2 and the plane restriction is etale, every
point of the cut is nonproper. Its smooth curve components are therefore
whole nonproperness components and, by the named import, A1s; thus l is a
nonnegative integer and the boundary Euler contribution is 2l.

6. Differentiating W gives W'=gamma. At a deleted root its multiplicity is
`2+ord(p')`; all other roots are simple. Summing over the complete w-line
gives `2+deg p'=N`. Coincident target images do not cancel distinct root
deficits. Finite-map Euler pushforward yields the open contribution
`N(1-l-k)`, and adding the boundary gives
`1=N-Nk-(N-2)l<=0`, the required contradiction. The control h=C produces
zero, as it should, rather than a false coordinate fibre.

7. In the displayed family, direct differentiation gives `q'=wp'/2`,
the two reduced factors have distinct nonzero roots, and evaluation at w=1
gives the stated divisibility cancellations. The x=0 triangular coefficients
are nonzero. Hence the theorem's stratum is genuinely nonempty for every
m>=2 and its mapping degrees are unbounded.

## Publication qualification

The producer omitted the required COLLISIONS block and the review invitation
preceded the contribution commit. Those are real custody/contract defects but
not mathematical counterexamples. The separately sealed addendum records a
terminal-zero EMPTY scan and discloses the sequencing error; commit 6b083ecb
banks the unchanged producer plus addendum. This review was completed only
after checking that commit and all four exact hashes. No producer byte changed.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5796`.
- Body SHA-256:
  `274ce827feb4749a8cdca850989afa023f8ab142ac4b7376df9b98c41db402d7`.
- Frozen basis: `6b083ecba093ba987062b8fcf7ea97e9318b0db7`.
