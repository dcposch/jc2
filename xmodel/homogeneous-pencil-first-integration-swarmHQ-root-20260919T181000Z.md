# Homogeneous-pencil composition: FIRST integration and binding scope correction

Producer/integrator: swarmHQ ROOT (Astra).
Independent reviewer: Fable 5.1, requested through the Claude adapter;
hosted identity and effort are not independently attested.
Date: September 19, 2026 UTC.
Basis: 9dd3b42ea224c5c18753de30bfda0be2e158f4f0.
Evidence: MANUAL, retaining named published dynamical imports.
Lifecycle: PRODUCER-CHECKED integration; AUDIT owns mathematical promotion.

## Result and exact scope

Fable independently CONFIRMS all four steps of the frozen
[producer report](homogeneous-pencil-composition-swarmHQ-root-20260919T175300Z.md).
No correction of the producer's claim or proof is required. ROOT narrows
two REVIEWER additions below; these do not change the producer's theorem.

For polynomial F:C^2 -> C^2 with constant det DF=c, 0<|c|<=1, let
r=a/b with coprime algebraically independent a,b in C[x,y]. If
r composed F=phi composed r, where phi:P^1->P^1 has degree d>=1,
then d=N(F)=1 and F is an automorphism by the inherited birational
Keller theorem. No existence of a pencil, dependent-pair case (including
polynomial r), |c|>1 extension or arbitrary-Keller conclusion follows.

Producer full SHA256:
45c5c50e94a73272b5b5ad6c387035d1defc9553c7dcb825ead2b85e8db9a854;
manifest SHA256:
3c1004b6255ea6ea0989539f0007a26fc70c38db156f4dbcffb85493eab135c9.
Reviewed publication commit is the basis above, not the producer's earlier
pre-authoring basis 48faaca89be082590151a4a545095fb4a4fff610.
The original producer and raw reviewer bytes remain unchanged.

## Independent mathematical review, condensed by ROOT

1. **CONFIRMED: constant-factor lift.** Quasi-finiteness of F prevents
   a source curve mapping into the finite common zero locus of a,b.
   Thus a(F),b(F) remain coprime. The homogeneous forms A_d,B_d defining
   phi have radical ideal (U,V), so a common prime factor after substitution
   would divide both a and b. Equality of reduced fractions therefore
   yields a common constant k in C*. For H=(a,b), G=k(A_d,B_d), HF=GH.
2. **CONFIRMED: generic degree.** H is dominant generically finite; no
   finiteness or integrality of H is assumed. G is finite homogeneous,
   with generic degree d^2. The reviewer additionally checks this by
   Bezout: the two homogenized generic fiber equations have no common
   point at infinity, and their generic affine intersection is reduced
   in characteristic zero. The tower law on the shared field
   C(a(F),b(F)) gives N(H)N(F)=N(H)d^2, hence N(F)=d^2.
3. **CONFIRMED: elementary iterate bound.** Fixed algebraic relations
   for x and y over C(a,b), after clearing denominators and composing
   with F^n, have polynomial coefficients of total degree <=C*d^n.
   Dominance keeps each chosen leading coefficient nonzero. If a
   coordinate of F^n had larger degree, the term with largest power of
   that coordinate would have uniquely largest total degree and could
   not cancel. Hence deg(F^n)<=C*d^n and lambda_1(F)<=d. Nonmonic
   relations suffice; no semiconjugacy dynamical theorem is needed.
4. **CONFIRMED at the accepted import tier.** Apply N(F)<=lambda_1(F)
   to this SAME F with 0<|c|<=1. Then d^2<=lambda_1<=d forces d=N=1.
   The [accepted dynamical report](keller-dynamical-degree-swarmHQ-root-20260914.md),
   [its FIRST](keller-dynamical-degree-gate-fable51-20260914.md) and
   [binding AUDIT scope](../AUDIT.md#keller-dynamical-degree-1--2026-09-14)
   retain Dinh--Nguyen--Truong arXiv:1303.5992v1 Theorem1.1 and the
   preceding equilibrium-measure property. The compact-bump correction
   remains binding. No fresh analytic-proof audit or Lyapunov alternative
   is consumed.

The reviewer checks base points versus base-free pencils, both gcd uses,
the d=1 endpoint, dependence exclusions, absence of a target normalization,
and the existing identity and (x^2,y^2) controls. Geometric irreducibility
of the generic pencil is not inserted. Mathematical confirmation is not
a literature-novelty determination.

## Binding correction of reviewer additions

The review's non-binding note1 says the square-degree relation and
lambda_1=d=sqrt(N) hold for EVERY dominant polynomial F with such a
pencil, Keller or not. This drops the quasi-finiteness needed for the
constant-factor lift. That stronger wording is NOT accepted.

A direct ROOT check shows the problem: T=(x^2*y,x*y^2) is dominant,
preserves r=x/y with d=1, but contracts both axes to the origin. Its
reduced pair (x,y) is independent, while the two substituted coordinates
share the nonconstant factor xy. Generic degree is 3: over target (u,v)
with uv!=0, x/y=u/v and x^3=u^2/v give three distinct points. Its iterates
are homogeneous of degree 3^n, so lambda_1(T)=3, not1. Also det DT=3x^2*y^2,
so it is NOT Keller and contradicts none of the producer's hypotheses.
This fixed desk-only check diagnoses the reviewer overreach; it is not
a new construction family or a JC2 counterexample.

Read the review's general observation ONLY after the constant-factor
semiconjugacy HF=GH has been justified, for example under quasi-finiteness
and the producer's reduced-pair hypotheses. Under those conditions steps
2--3 give N=d^2 and lambda_1<=d; the optional opposite inequality uses
the separate standard log-concavity import and is not needed here.
Likewise hostile-check1's "no Jacobian needed" for the d=1 degree argument
means no FURTHER Jacobian use AFTER the lift, not permission to discard
the quasi-finiteness hypothesis that supplied it. No broader theorem is
promoted by this integration.

The small citation-range note is harmless: the producer read AUDIT
22558--22598, while the reviewer read 22557--22596 including the correct
header and entire relevant entry. Neither changes its mathematical scope.

## Read coverage and custody

Raw reviewer report retained under the stem
`homogeneous-pencil-first-swarmHQ-fable-20260919T180000Z`, full SHA256
7bb2970681451f66057ec066521cfb982a178d4c89f546926d0706e8dceb04f2.
Its raw log SHA256 is
12caf5f2dd847f53d4ea059ec7aed92c6bd0f8be620b2e54a5ab6754e9e69323;
receipt SHA256 is
d43b0eb4ad4819375e8ee59a46c9be2457b2efaf715cb2b757e679ed8dedddc1.
These raw operational artifacts remain local; this public report is a
ROOT-authored mathematical integration, not a verbatim reviewer transcript.

Reviewer declares whole reads of all charged public entry documents,
FALLACY-v2, producer/manifest, and both accepted dynamical reports; only
the specified AUDIT range was read. Ten charged input pins and four
governance pins match before/after; ROOT rechecked the original pins.
Neither DNT's proof nor the birational Keller theorem was re-audited.
One oversized context output was automatically persisted by the harness;
the reviewer reports recovering the text from the charged snapshot.
An early draft/partial was saved, followed by a same-path final rewrite.
No authored extra output is declared; final-only logs do not independently
certify a complete tool trace, output boundary or hosted model identity.

Author readback completion18:07:07 UTC, successful terminal receipt18:07:25.
ROOT verified terminal supervisor and absent exact descendants before
receipt-first collection, then read the whole receipt, report and log.
Report/log/receipt were frozen444 with unchanged hashes. Producer lifecycle
verification passed again. Integrity checks certify custody, not the theorem.
No exit price, scientific computation, new source import or descendant.

## OPENS RAISED

None. A pencil for an arbitrary hypothetical counterexample is not supplied;
the general source implication remains open. No automatic family successor.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

This checks explicit open-item collisions, not literature novelty.

Integrator readback complete, clock measured 2026-09-19 18:11:40 UTC.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7883`.
- Body SHA-256:
  `7ff33905161eb07720a726221e722b448080aa3f4d98ea224cd94e5ed36821c7`.
- Frozen basis: `9dd3b42ea224c5c18753de30bfda0be2e158f4f0`.
