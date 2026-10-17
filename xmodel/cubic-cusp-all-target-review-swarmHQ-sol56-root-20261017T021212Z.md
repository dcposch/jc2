# Cubic-cusp donor: independent all-target FIRST and integration

Verdict: CONFIRMED / PROMOTED / MANUAL with named accepted classical imports.
Claim ID: CUBIC-CUSP-ALL-TARGET-1.
Producer: swarmHQ ROOT with native Astra co-check.
Independent reviewer: native gpt-5.6-sol; terminal2026-10-17 02:12:12 UTC.
Integration: swarmHQ ROOT. Public basis322919a438bf9e95f4e175dd931fbdbf08341492.
Operational review admission: swarmHQ270772ea294ad708f162c30c11add95fb980757b.

## Frozen proof and exact scope

[Producer proof](cubic-cusp-all-target-swarmHQ-root-astra-20261017T020131Z.md),
11883 bytes, mode444, full SHA256
bd2524a665840827858501cacf797a937da91775c43ee79d94bedacb3bc8d98b.
Its actual `.artifact.json` manifest is721 bytes, mode444, SHA256
f77b766c2b725cfb8646a0bff9fe0d0dd6a658fef136b9fb8bb59eb94db69570.
The original UNPROMOTED header and seals remain unchanged. This integration
promotes the following claim, not a stronger donor classification:

Over C, for t=X/Y, p=Y-3t^2, q=-tY+2t^3, no birational rational target change
with nonzero constant Jacobian, followed by any finite rational source-field
embedding C(X,Y) -> C(x,y), yields two polynomials with nonzero constant
Jacobian on the entire affine source plane.

The geometric intermediate assertion is also confirmed: a NONPOLYNOMIAL
birational constant-J target map sends the standard cusp to a genuine affine
curve whose normalization is not A1, or which is itself a smooth A1.

The review consumes the already reviewed CUSP-AVOIDANCE-1 and the accepted
surface/attachment interfaces in SYMPLECTIC-TARGET-SMOOTH-BRANCH-1. It checks
their applicability and the new implication, not every classical source proof.
No theorem for nonconstant-J target maps, all affine-radial or other rational
donors, general Keller normal forms, actual finite-normalization emptiness,
or JC2 is promoted. External novelty is unknown.

## Independent geometric attack

The reviewer checked the distinction between a morphism A2 -> P2 and one into
A2. The accepted basepoint lemma supplies only the first, and this is exactly
what the proof uses. In a resolution unchanged on the old affine plane, a
polar component E cannot dominate new infinity: the generic DVR identification
would equate area-form orders0 and-3. Thus it is exceptional and smooth rational.
Its affine part is closed rational with no assumed puncture bound.

The cusp cannot be exceptional, because its singular affine point is untouched
while exceptional curves are smooth. Nor can it dominate new infinity, by the
same area-order contradiction. Hence its finite image C' is genuine and its
projective normalization is birationally identified with P1_t.

Assuming normalization(C')=A1 gives exactly one removed parameter t0. An affine
pole curve meets the cusp by CUSP-AVOIDANCE-1, and projective regularity sends
every such intersection to infinity. Therefore t0 is finite. If H defines the
pole curve, h(t)=H(t^2,t^3) is nonzero, has a root, and has no root except t0.
So h=a(t-t0)^k. Since h'(0)=0 and the characteristic is zero, t0 cannot be
nonzero. The k=1 case is impossible outright; for k>=2 the only possibility
is t0=0. Thus the old cusp point goes to new infinity.

The inverse-resolution step was checked without forbidding blowups at the old
cusp. The strict transform can be singular only above that old point, since
all other points of the projective cusp, including old infinity, are smooth.
For any finite new point b above old0, the identity tau composed with sigma=rho
on sigma^-1(A2_old) would imply b=tau(0) is at new infinity. This is impossible.
All points above the potential singularity are therefore outside the unchanged
new affine plane. C' is smooth; under the normalization assumption it is A1.
No assumption that an infinity exchange is impossible was used.

## Donor, polynomial-target case, and controls

The reviewer independently checked K=C(p,t), q=-t^3-p*t, degree3, and generic
ramification index2 along 3t^2+p=0. Its image4p^3+27q^2=0 is linearly equivalent
to the standard cusp. The surviving affine image remains ramified under the
target-field identification and every finite source extension. The accepted
attachment theorem forces it to be an actual nonproperness component of a
hypothetical polynomial Keller landing. The two alternatives are then excluded
respectively by polynomial coverage and the no-smooth-A1-component theorem.
Additional branch components cannot undo this already attached contradiction.

For polynomial target changes, the reviewer checked the birational Keller
argument: etale quasi-finite plus Zariski Main gives an open immersion; a
divisorial complement contradicts the units of C[x,y]; codimension-two inverse
extension gives an automorphism. Undoing it invokes the prior fixed-target
affine-radial obstruction. This does not assume any later Keller source
substitution is invertible and does not assume JC2.

Controls independently passed:

- Identity is polynomial and retains the singular cusp, so the intermediate
  image-curve dichotomy correctly excludes polynomial targets.
- (p,q)->(1/p,-p^2*q) has J=1 and sends the cusp to u^7*v^2=1, with
  normalization C*. On q=0 it exchanges zero and infinity while retaining a
  line, confirming that infinity exchange itself is not ruled out.
- (p,q)->(q/p,p-q^2/p^2) sends the cusp to a line but has J=-1/p and a
  finite projective basepoint. It tests the necessity of the constant-J
  basepoint premise, not existence of a Keller repair outside the scope.

## Custody and disposition

Reviewer ACK/start02:11:25 and terminal postpins02:12:12. Original partial02:20:07,
hard02:30:07 and bank02:40:07 were not renewed. Whole-set pre-gate passed for
ten governing files and both proof/actual manifest: regular-file, nonsymlink-
ancestor, exact-mode, size and full-hash checks. Nine unchanged prior whole
governing reads were reused, changed APPROACHES894 read wholly, and frozen
270772e:STATE.md read wholly (441 lines/32237 bytes), SHA256
11ad5a8476e30fb85630818dfeb25d33d64417ed0b133f9f69a21abeb5989b58.
The producer216 lines including seal and actual manifest were read whole.
artifact_finalize verify returned VERIFIED. All inputs' postpins matched.
The optional legacy proof body was not opened in this review.

The reviewer corrected one ambiguous read-count phrase in a follow-up: exactly
nine unchanged governing reads were reused. This was a record clarification,
not a mathematical change or deviation. No writes, children, extra queries or
bodies, sources/network, CAS/scientific subprocesses, cloud/paid CLI, external
adapters or protected-tree access occurred. ROOT records the complete scoped
verdict here; no new descendant is automatically authorized by this promotion.
No exit-price declaration applies, and no Keller-compatible example is claimed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6826`.
- Body SHA-256:
  `27706ad23d1e54c5e51c8c8d41d86c31abbd385cd2a73caa7251f19c4a0612ef`.
- Frozen basis: `322919a438bf9e95f4e175dd931fbdbf08341492`.
