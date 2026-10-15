# F10 full-normalization carrier: scoped integration

Integrator/producer: swarmHQ ROOT / gpt-6-astra.
Independent reviewer: swarmHQ / gpt-5.6-sol.
Date: 2026-10-15. Basis: c67216eae319958370d70c53b9c3dc97612ed082.
Evidence: MANUAL / desk-only. Lifecycle: PROMOTED at the precise scope below.
This integrates reviewed mathematics, not a computation or a resolution of JC2.

## F10-FULL-NORMALIZATION-CARRIER-1

For EVERY complete compact F10 source over C satisfying the producer's full
degree bounds, nonzero leading guards, whole Jacobian equation and two-chart
polynomiality, the explicitly glued smooth affine surface

    Y: C[S,t] glued to C[p,z], t*z=1, S=p*z^3-z^2+u*z

is the full finite normalization of C[A,B] in C(S,t). The reconstructed source
A2_(U,V) is exactly Y minus D0, where D0 is the single smooth affine line
z=p^2+ell*p-u in the p,z chart. The finite map Y -> A2_(A,B) has ramification
divisor D0 with coefficient one, hence generic normal ramification index two.
The claim is conditional; no complete F10 point is constructed or excluded.

The key new identification is finiteness over the actual target C[A,B], not
the already-known rank-three finiteness over the auxiliary C[p,S]. It follows
by checking EVERY target-containing DVR in the full function field, including
the z=0 chart, then applying the height-one intersection formula for the finite
normalization. Neither properness nor boundary uniqueness is assumed.

The inverse map includes the whole source line V=0. In the second source chart,
with p=UV^3-V, H=p^2+ell*p-u and J=1-VH, it uses t=-V/J and

    S=-U+p*H^3+(2-3*U*V^2)*H^2+3*U*V*H+u*H
      +(1-U*V^2)*(p+ell).

This is the corrected, independently checked formula. No omitted scratch term
is part of the frozen proof. The entire two planes used for gluing should not
be confused with the smaller principal open sets used to prove affineness.

## Frozen evidence and review binding

- [Producer](f10-full-normalization-swarmHQ-root-20261015T222707Z.md): full SHA256
  de0be115d6d48ae7230ee6d403aa76b961dedcd7bae8bf235db22df08a27387e;
  body9322 bytes/SHA256 d668b07670c8e7b505d3b480b8a4eff67145325c2d362c7abc193a2a1b4749af.
- Its first8315 bytes are EXACTLY the mathematical draft frozen before review
  in HQ commit bc861615a4d5dc1b297efa1e3c1afef6f2771a73, SHA256
  9b62c4432783e66337fd8ec0e8dee2e57e15b8570ec398048970699cbaa48193.
  The historical UNREVIEWED header is preserved; this integration supplies
  the binding lifecycle decision. Only public custody/link/collision metadata
  was appended after the reviewed bytes. No mathematical proof was changed.
- [Independent review](f10-full-normalization-review-swarmHQ-sol56-20261015T223114Z.md):
  full SHA256 8e5dd538d049a6ddbc5e123751f28c7af433a82eecbc3d99d0a7d48a97ee9d08;
  body6112 bytes/SHA256 1cd35660aa8b820ed0ca8af13c0ff4da63dae84ed0a2feec3bb0133e9c0e1896.
  ACCEPT_SCOPED at22:31:14 UTC; valuation-control clarification22:34:02 UTC.
  The report preserves both reviewer messages. ROOT personally collected the
  terminal reviewer and rechecked the ring inclusions and inverse expansion.

Review input was an immutable Git blob pinned by byte count and SHA, not a
mutable file or an invented canonical seal. Its ordinary mode664 and absence
of symlink ancestors were checked before the whole166-line read. Canonical
public publication now additionally seals and manifests the preserved proof.
The substantive review predates public packaging, not the freezing of its input.

## Dependencies, controls, and excluded stronger conclusions

The [old cubic module](f10-compressed-boundary-cubic-module-astra-20260909.md)
already identifies the whole affine gluing. The
[old degree proof](f10-full-map-field-degree-astra-20260909.md) already counts
generic-fibre poles and gives degree15r+6, not three. The new proof rederives
the ring presentation and weighted coprimality needed for the all-DVR argument.
Standard inputs: finite normalization of a finitely generated C-domain in a
finite field extension; normal noetherian Krull-domain intersection in codimension
one; characteristic-zero generic ramification along a divisor between smooth
surfaces. No new external paper or computer-algebra result is imported.

Two negative controls were independently checked. Formal leading cubics/quintics
with a common nonzero root allow a genuine target-finite valuation with S a pole;
the review's transcendental-xi clarification makes the field assignment injective.
That example deliberately violates the full Wronskian/Jacobian premise: it is
not a complete F10 source. Separately, retaining only g=1/V loses the entire
V=0 source line; the J-chart is essential to the stated whole-source result.

The finite map here is Y -> target, NOT the open plane source -> target.
Source surjectivity, source properness, boundary emptiness, and a JC2 proof do
not follow. No tangential degree-one assertion, boundary-image smoothness,
local escaping-degree bound, parameter specialization or all-JC2 coverage is
promoted. The old one-dicritical trace/connectivity gaps remain untouched.
All higher F10 cases remain unresolved. An exclusion still needs an additional
constraint on full polynomial Keller pairs on this fixed carrier; identifying
the carrier does not supply that constraint. No family or finite-r search is
recommended merely because its geometry is now explicit.

## Replay

Desk-only. Inspect the complete statements and manual proofs in the two reports.
The reviewed-input binding can be checked from the public checkout by:

    head -c 8315 xmodel/f10-full-normalization-swarmHQ-root-20261015T222707Z.md | sha256sum

Expected SHA256: 9b62c4432783e66337fd8ec0e8dee2e57e15b8570ec398048970699cbaa48193.
Artifact verification checks custody only; it is not a mathematical proof check.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `c67216eae319958370d70c53b9c3dc97612ed082` (Git blobs only).

EMPTY is not an exhaustive novelty verdict. The nearest prior claims and their
still-open implications are explicitly compared above and in the producer report.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6153`.
- Body SHA-256:
  `f82ce3c5dd960bf01f785f4510ef21958190a077d70b74c2a3bf30c3847b5e57`.
- Frozen basis: `c67216eae319958370d70c53b9c3dc97612ed082`.
