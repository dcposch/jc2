# Positive-genus ramification obstructs rational target postcomposition

Producer: swarmHQ ROOT (gpt-6-astra). September15,2026.
Basis: d038e755e7d29f7567bc8a154689ac7141e29f05.
Evidence: MANUAL / BOOK-relative. Lifecycle: PRODUCER-CHECKED, UNPROMOTED.
This is a source-attached donor filter and a scope correction, not JC2.
The geometric ingredients are classical; no novelty claim.

## Exact statement

Let K0 be a complex rational function field of transcendence degree two,
and let K/K0 be finite. Let v be a divisorial valuation of K, trivial on
C, with normalized restriction v0 to K0. Assume

    e(v/v0)>1,     genus(kappa(v))>=1.

Genus here means that of the smooth projective curve with the indicated
one-variable function field, NOT sectional genus or local geometric genus.
Then there is no C-field embedding K into L=C(x,y), of any finite degree,
and no pair p',q' in K0 satisfying K0=C(p',q'), for which their images
are polynomials in x,y with nonzero constant Jacobian.

Thus the obstruction is invariant under replacing the target coordinates
by any rational generating pair of the SAME target field. The corollary
below also covers every rational dominant target postcomposition, including
passage to a smaller rational subfield. It does not cover adjoining new
target elements or changing to a field not contained in K0.

## 1. A positive-genus valuation cannot hide outside a plane

Let w be a divisorial valuation of C(x,y) with residue genus at least one.
Choose a normal proper surface model realizing w as a prime divisor E.
Resolve the birational map from P2 to that model by point blowups. The
resulting surface W has a proper birational morphism to the normal model,
which is an isomorphism at the generic point of E. Hence its strict
transform Ew represents w with the same residue field.

Every curve contracted by W->P2 is rational, since W is obtained by point
blowups of a smooth complex surface. Ew cannot be one of them. Its image
is therefore a curve in P2, birational to Ew. That curve cannot be the
line at infinity either. It meets A2 in an irreducible affine curve Cw,
and w is exactly its normalized order-of-vanishing valuation.

The resolution input is [Stacks, Lemma54.4.3, Tag0C5H](https://stacks.math.columbia.edu/tag/0C5H).
The corresponding smooth-surface factorization is
[Lemma54.17.1, Tag0C5R](https://stacks.math.columbia.edu/tag/0C5R).
ROOT read both statements and their displayed proofs. Standard additional
inputs: existence of a proper model for a divisorial valuation, normality
at codimension one, and the rationality of point-blowup exceptional curves.
No assertion says an arbitrary rational map A2-->U is defined on all A2.

## 2. Proof of the field obstruction

Suppose the stated embedding and polynomial Keller pair exist, and identify
K0 subset K subset L by that embedding. Extend v to a valuation w of L.
Finite extensions preserve divisoriality and give a finite residue-field
extension kappa(w)/kappa(v). Characteristic-zero Riemann--Hurwitz gives

    2g(w)-2 = f*(2g(v)-2)+R,     f>=1, R>=0,

so g(w)>=1. Multiplicativity of ramification indices gives

    e(w/v0)=e(w/v)*e(v/v0)>1.                         (1)

Section1 puts w on an actual affine source curve Cw in A2_(x,y).
The polynomial map F=(p',q'):A2->A2 is etale, hence quasi-finite. It cannot
contract Cw to a point. Let D be the closure of its image, an irreducible
target curve. The restriction of w to K0 has center at the generic point
of D, so its normalized valuation is ord_D: a valuation ring dominating
the target DVR with the same fraction field equals that DVR.

The local map O_(A2,D)->O_(A2,Cw) is essentially etale between DVRs.
Its ramification index is one, contradicting (1). This proves the claim.

Notably, no genus condition on kappa(v0) was assumed. The hypothetical
polynomial etale map itself forces its affine divisorial center. The
argument uses neither a bound on [L:K] nor a polynomial parametrization
theorem for nonproperness curves.

**Target-subfield corollary (ROOT's additional deduction).** In fact no
algebraically independent pair p',q' anywhere in K0 can work. Put
K00=C(p',q'). The extension K0/K00 is finite, and the normalized restriction
v00 satisfies e(v/v00)=e(v/v0)*e(v0/v00)>1. Apply the proved theorem with
base K00. Thus dominance, not birationality, of a rational target
postcomposition suffices for exclusion. Algebraic dependence would already
force the final Jacobian to vanish.

## 3. Attachment to the accepted Pinchuk donor

Use exactly the fields K0=C(p,q) and K=C(f,h) in the
[accepted literal donor report](pinchuk-donor-branch-swarmHQ-root-20260915T143100Z.md)
and its [Sol review](pinchuk-donor-review-swarmHQ-sol-20260915T144100Z.md).
Their normalization chart is B_f=C[f,f^-1,h]. The irreducible critical
divisor in that chart has genus one and is ramified over K0 (index two).
These accepted facts instantiate v in the theorem.

Consequently the exclusion extends to EVERY algebraically independent
rational target pair p',q' in C(p,q), after EVERY finite-degree source
embedding of K into C(x,y). Neither p' nor q' is required to be regular in the old
target coordinates; polynomiality is required only after the proposed
source substitution. This does not exclude other Pinchuk field
presentations or a target subfield of K not contained in the original K0.

This is also a correction to the old reports' unqualified wording that
source-divisor genus alone is insufficient. For their proof through
TARGET nonproperness, branch-image genus was indeed needed; their separate
six-critical-value argument correctly supplied it. But once a genuine
ramified divisorial valuation is attached, positive SOURCE residue genus
already excludes the donor by Section2. The old proof, algebra, branch-image
genus conclusion and seals remain valid. Only the claimed necessity of
that extra step for donor exclusion is withdrawn.

## 4. Prior scope and controls

The [promoted morphic rational-forest correction](bd-a2-rational-forest-morphic-correction-coordinator-integration-sol56-20260830.md)
already excludes positive-genus omitted ramification in actual proper-block
models. This report does not replace that theorem, re-audit its proof, or
claim the source-genus idea is new. The delta is the intrinsic valuation
formulation, target-field invariance, and its attachment/correction above.

- An arbitrary critical curve on an unrelated rational presentation does
  not suffice: one must prove e(v/v0)>1 for the stated field extension.
- Rational ramification is not excluded. K=C(s,t), K0=C(s^2,t) has a
  ramified source valuation at s=0 with rational residue field. Its
  polynomial map has Jacobian2s, not a Keller condition; the genus premise
  fails, so the theorem makes no claim about that field extension.
- An elliptic curve valuation in the identity extension C(s,t)/C(s,t)
  has index one. Its positive genus alone causes no contradiction.
- Arbitrary rational domination still imposes no boundary-genus condition:
  A2-->P2 minus a smooth cubic remains the old counterexample. Section2
  instead assumes the final pair is polynomial and etale on the WHOLE plane.
- No general Keller source is shown to contain positive-genus ramification.
  The all-rational-ramification case, target fields not contained in K0, and JC2
  remain unresolved. No donor family or computation is selected.

## Provenance and review boundary

Whole local dependencies were read with hashes:

    literal producer c2d14db83f1abced4a0e68b65bf3e0aca94b48e057c49c59d707248dbd7a0e14
    Sol review       21800e50dee5807d55d5feccd206bf31be9ba725a1446d421139f43973d7ab8c
    forest correction94a5968a7b412e80536b855b753c33db8d5cafff6698fa6abf8b7f0c99734c1d

Targeted history searches recovered older genus-two ramification clients
and the corrected morphic theorem; they are not an exhaustive priority
search. No Campbell/formula, degree-bound or complete forest-theorem reaudit
was performed. No scientific code, numerical calculation or paid/AWS job
was used. Different-model review of this new scope is required before
promotion or dependent research.

Native Astra completed an independent message-only co-check at15:24:48 UTC,
returning CONFIRMED for the same-target-field theorem, Pinchuk attachment
and precise scope correction. All three named local inputs were wholly
read with matching hashes; no sources or mathematical code were executed.
ROOT collected its terminal answer before completing this report. The
additional target-subfield corollary was not assigned to that co-check;
it and the entire frozen report remain subject to different-model review.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

ROOT's canonical scanner completed exit0 before15:25:17 UTC. This lexical
identifier check is not a mathematical proof or novelty certificate.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8903`.
- Body SHA-256:
  `9db61cfac2ed54087001dc6c6eb175ae87609672e1e187982d49ae7c3c8fc39d`.
- Frozen basis: `d038e755e7d29f7567bc8a154689ac7141e29f05`.
