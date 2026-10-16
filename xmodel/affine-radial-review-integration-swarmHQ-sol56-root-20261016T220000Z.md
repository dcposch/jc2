# Independent review of the affine radial donor obstruction

Producer: swarmHQ ROOT, gpt-6-astra, recording and integrating native gpt-5.6-sol FIRST
Date: 2026-10-16 UTC
Basis: b4d747e010535281ae0040ec8d4bec7cf844efc6
Evidence tier: PROMOTED / MANUAL, with the producer's two accepted classical-import premises
Lifecycle: PRODUCER-CHECKED; different-model hostile review CONFIRMED

## Statement and scope

The [frozen producer proof](affine-radial-obstruction-swarmHQ-root-20261016T214900Z.md)
is accepted at exactly this scope: for
\[
 t=X/Y,\qquad P=A(t)Y+B(t),\qquad Q=C(t)Y+D(t),\qquad
 A,B,C,D\in\mathbb C(t),\quad J_{X,Y}(P,Q)=1,
\]
a genuinely rational pair cannot become a whole-plane polynomial Keller pair
under any finite rational source-field embedding in the unchanged target
coordinates \(P,Q\). Polynomial members of this class are affine automorphisms.

This is an all-degree construction filter, not a normal-form theorem for general
Keller pairs, a claim about arbitrary birational target repairs, or a resolution
of JC2. It does not prove invertibility of an arbitrary later Keller substitution
when the donor itself is polynomial. The producer's historical UNPROMOTED header
remains unchanged; this integration records the subsequent review disposition.

## Dependencies and prior work

The producer's branch-attachment/A1-normalization premise and its
integral-back-coordinate criterion retain their previously accepted classical
tiers. FIRST checked their applicability and the new argument, not the proofs of
the external source theorems. No stronger smoothness premise was imported.
The rational generating-family and homogeneous examples in the producer are
controls, not new construction candidates or separate JC2 claims.

## Argument or computation

The following is the complete author-complete review message from native
gpt-5.6-sol, preserved verbatim apart from Markdown quotation prefixes.
The short final terminal message also confirmed completion; ROOT independently
observed the task completed before recording this integration.

> AUTHOR-COMPLETE DIFFERENT-MODEL FIRST REVIEW — native gpt-5.6-sol
> VERDICT: CONFIRMED, conditional exactly on the two accepted classical-import premises stated in the frozen report. No gap/refutation found.
> Scope: for t=X/Y and P=A(t)Y+B(t), Q=C(t)Y+D(t), A,B,C,D∈C(t), J_(X,Y)=1, a genuinely rational pair cannot become a polynomial Keller pair after any finite rational SOURCE field embedding while target coordinates P,Q stay fixed. Polynomial members are affine. This does NOT imply invertibility of an arbitrary later Keller substitution, allow arbitrary birational target repair, or give a normal form/general JC2 result.
> Independent attack: dX∧dY=Y dt∧dY gives A'C−AC'=1 and B'C−AD'=0. When (B,D) is nonconstant, the generic Y=0 divisor maps generically finitely to Δ; separability of t→C(B,D) means contraction by (t,Y)→(tY,Y) is irrelevant to the divisorial field valuation. The transverse Jacobian order is 1, hence ramification index 2. Accepted import 1 therefore requires normalization(Δ)=A1 in any hypothetical polynomial Keller landing; no smoothness or projective-smooth-branch premise was smuggled in.
> Writing its normalization parameter h (possibly [C(t):C(h)]>1) gives B=b(h),D=d(h). Δ cannot be a line: constant B or an affine relation D=αB+β forces A=0 or C=αA, contradicting the Wronskian. An SL2 target change thus gives 0<m=deg b<n=deg d. Cancelling nonzero h' in B'C=AD' is valid in char0 and yields b'C=Ad'. Then b d'−d b'−P d'+Q b'=0 has degree m+n−1 and nonzero constant leader (n−m)lc(b)lc(d), so h, B,D are integral over R=C[P,Q].
> Homogeneous lemma survives all valuations, including higher rank and infinity. For any valuation ring V⊃C[AY,CY], restriction to C(t) is trivial or centered on P1. Trivial restriction makes A,C,t units. At finite a, Y∉V would force A,C to have positive value, hence both vanish at a, contradicting A'C−AC'=1. At infinity, s=1/t, a=sA(1/s),c=sC(1/s), with a'c−ac'=−1; X∉V would force a,c both vanish at s=0. Thus X,Y lie in every such V and are integral over C[AY,CY].
> Completion: if B,D constant, this directly applies. Otherwise B,D integral over R makes AY=P−B and CY=Q−D integral; the generated intermediate ring is integral over R, so transitivity makes X,Y integral over R. Accepted import 2 excludes a genuinely rational donor. If normalization(Δ)≠A1, import 1 already excludes landing.
> Polynomial endpoint checked independently: radial scaling fixes t and splits each output into weights 1 and 0; polynomiality forces only linear+constant homogeneous parts, hence an affine pair, and J=1 makes that pair an affine automorphism only. It says nothing about an arbitrary further substitution.
> Controls all pass: (Y,−X) is the required polynomial exception; (X²/Y,Y²/(3X)) has J=1 and X³=3P²Q,Y³=9PQ², exercising constant translation plus finite/infinite valuations; cusp donor (Y−3t²,−tY+2t³) has t³+Pt+Q=0 and exercises A1 normalization without smooth image.
> Reads/gates: whole-set pre-gate passed for all 12 files (regular, nonsymlink ancestry, supplied full hashes/sizes/modes; proof+manifest exactly 0444). Read HQ AGENTS23, POLICY112, RESEARCH_POLICY157, frozen git blob 5ab7e19:STATE.md 292 lines/20888 bytes, RUNBOOK397, RESTRICTIONS177; public AGENTS22, README, COORDINATION, APPROACHES875, FALLACY-v2 whole; then manifest whole before proof whole228. No linked evidence bodies followed.
> Exact verifier from /home/ubuntu/jc2 returned status VERIFIED, basis20924a378586de8d42fcdb71e0b7f685be898893, proof full sha45e5cbf…, manifest sha8a89429…. Postpins rechecked unchanged for every input; frozen STATE still 20888 bytes sha bb3a009e…; proof/manifest remain 0444.
> Clock: ACK/start 2026-10-16T21:57:43Z; terminal postpin 21:59:21Z, before early partial22:06, hard22:20:44, bank22:30:44. Deviations: none. No writes, children, CAS/science code, network, external adapters, source/history/report/receipt/log expansion, or protected-tree access.

## Replay and negative controls

Desk-only. The producer contains the complete proof and the three controls
independently checked above. ROOT collected the terminal review at measured
21:59:55 UTC and independently reverified the unchanged producer artifact:

- Full proof SHA256: 45e5cbfdecd1ce92e8cd3025bf232d6e45058501d8483cbd95888d47da607fbf;
  10866 bytes, mode0444.
- Manifest SHA256: 8a89429f4ab849b57dc807e2e541efe64287b55e4350c5274af34eb4b820e5f6;
  716 bytes, mode0444.
- Artifact basis: 20924a378586de8d42fcdb71e0b7f685be898893;
  frozen contribution commit: b4d747e010535281ae0040ec8d4bec7cf844efc6.
- Native task: affine_radial_first_sol56_2157; configured reviewer model
  gpt-5.6-sol. The separate native Astra check was same-model, not FIRST.

The review's 12 files comprise ten instruction files and the canonical proof/
manifest pair; the separately named frozen STATE is a Git blob, not a thirteenth
working-file read. Its full SHA256 is
bb3a009e7f097e2fa22cce4bd8bbf148a2b3c5e0e2122ebe936840f11eda0de7.
ROOT's integration does not retroactively alter any frozen instruction, input,
producer header, author clock or review verdict.

From the repository root, verify both canonical artifacts:

~~~sh
python3 ops/artifact_finalize.py verify --final xmodel/affine-radial-obstruction-swarmHQ-root-20261016T214900Z.md
python3 ops/artifact_finalize.py verify --final xmodel/affine-radial-review-integration-swarmHQ-sol56-root-20261016T220000Z.md
~~~

Each should return VERIFIED against its adjacent manifest. No scientific
computation or benchmark is claimed by these custody checks.

## Limitations and next test

The scope is fixed-target finite source repair of affine-radial donors only.
Actual Keller finite-normalization emptiness, a general source-compatible
normal form, and arbitrary birational target repair remain open. This result
removes one broad construction family from consideration; it does not authorize
a coefficient farm or automatic degree-by-degree successor.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `b4d747e010535281ae0040ec8d4bec7cf844efc6` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8295`.
- Body SHA-256:
  `861d275801238ef8fa3b203530b0dafe07b613d29f19ee4d3a0675e506c8d579`.
- Frozen basis: `b4d747e010535281ae0040ec8d4bec7cf844efc6`.
