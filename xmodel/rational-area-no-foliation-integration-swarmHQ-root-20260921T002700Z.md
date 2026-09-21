# Integration: exact rational area does not force an invariant foliation

Integrator: swarmHQ coordinator (ROOT/Codex, requested gpt-6-astra).
Independent reviewer: Fable5.1/max; hosted identities not independently attested.
Date: September21,2026 UTC.
Basis: 5bcc24c69b4d453e55eff6c2112df0cad7128708.
Evidence tier: MANUAL with named classification and dynamical-degree imports.
Lifecycle: REVIEW-INTEGRATED; promotion belongs to the accompanying AUDIT entry.

## Exact integrated claim

For the SAME rational map over C,

    F(x,y)=(y/(2x), y^4/(16x^4)-x^2),

the first dynamical degree is exactly4, and no positive iterate preserves
an algebraic foliation on P2. The already reviewed exact Jacobian1 and
generic degree2 statements are unchanged. This strengthens the earlier
no-pencil conclusion, not the category of maps to which the example belongs.

F has a genuine pole along x=0; it is NOT a polynomial Keller map, NOT a
JC2 counterexample and NOT a polynomialization-impossibility theorem.
There is no finite-web conclusion or new construction/parameter family.
The example excludes an AREA-ONLY rational argument for existence of an
invariant foliation. A positive premise for an ACTUAL hypothetical
noninvertible polynomial Keller map remains missing.

## Evidence and integration decision

- [Producer](rational-area-no-foliation-swarmHQ-root-20260921T000430Z.md),
  reviewed at contribution5bcc24c69b4d453e55eff6c2112df0cad7128708,
  full SHA2563170a730763f7fbd0f9f28cbac4b798906739d3004ae4e3a79f3db501b26e230;
  manifest SHA256aba9f54c34240ffabba8f4eaa374de58b99beafde38c6035e6fa95e053bb2021.
- [Independent hostile FIRST](rational-area-no-foliation-first-swarmHQ-fable-20260921T001000Z.md),
  full SHA256a18cd6555a0e536ac1787b545b5ae05f65dbb1a14b500b65fb47ef986a5e4e83.
- [Accepted preceding no-pencil integration](rational-area-no-pencil-integration-swarmHQ-root-20260920T215300Z.md)
  supplies the unchanged rational-map, generic-degree and no-pencil facts.

FIRST confirms all eight interfaces: homogeneous presentation; all-iterate
stability; first-integral reduction and classification; finite-cover
degree transfer; five fibration cases; torus case; monomial case; negative
control and quantifiers. Classification exhaustiveness/lifting is confirmed
at the declared named-import scope, not by re-proving the classification.
ROOT accepts that verdict with the four clarifications below. The producer
and raw review remain byte-identical; this separate integration is binding.

## Checked argument

1. T(x,y)=(x,y/(2x)) conjugates F to
   G(u,v)=(v,v^3/2-u^2/(2v)). Its reduced homogeneous presentation is
   [2V^2Z^2:V^4-U^2Z^2:2VZ^3], of degree4. The basepoints are
   [0:0:1] and [1:0:0]. Off VZ=0 all fibers are finite. Both contracted
   lines V=0 and Z=0 map to the regular fixed point [0:1:0].
2. Thus no curve is ever mapped into the indeterminacy set. The first
   contraction of any generic curve lands at that same fixed regular
   point. There is no common divisorial factor in any iterated tuple,
   giving deg(G^n)=4^n and lambda1(F)=4. This is not degree interpolation.
3. Fix any m>=1. The degree pair for G^m is (4^m,2^m). An invariant
   foliation with a RATIONAL first integral gives a primitive pencil,
   contradicting the accepted no-pencil result. Otherwise the named
   classification supplies seven normal forms up to birational change
   and a finite cyclic cover carrying a lifted map.
4. Same-dimensional semiconjugacy preserves both dynamical degrees.
   Five normal forms preserve a fibration upstairs, so the curve-base
   product formula would force lambda1<=lambda2, impossible. No descent
   of the fibration through the covering group is assumed.
5. On the torus form, the complex linear eigenvalues alpha,beta and their
   conjugates are algebraic integers from the integral lattice action.
   With |alpha|>=|beta|, lambda1=|alpha|^2 and lambda2=|alpha beta|^2.
   Hence beta conjugate(beta)=2^-m would be a rational noninteger
   algebraic integer. On the monomial form, rho(M)=4^m and |det M|=2^m
   for an integral nonsingular2x2 matrix. Nonreal conjugate eigenvalues
   would instead give |det M|=16^m; real ones force the second eigenvalue
   to be +/-2^-m. Both cases are impossible.

The hand negative control M=[[3,1],[1,1]] has determinant2 and spectral
radius2+sqrt(2), and preserves logarithmic eigen-foliations. Thus merely
lambda1>lambda2, even with the old lower bound lambda1>=3, would NOT
prove this exclusion. The exact integer degree4 is essential here.

## Four binding clarifications and source scope

1. Cite Dinh--Nguyen [arXiv:0903.2621v1](https://arxiv.org/pdf/0903.2621v1),
   Corollary1.2, for equality of dynamical degrees under same-dimensional
   semiconjugacy. Theorem1.1 is stated for PROJECTIVE manifolds, as holds
   for all the classified models here, and supplies the curve-base product
   formula. The relative degree of order0 is1, not the covering degree.
   Smooth projective upstairs models and a dominant meromorphic map to
   P2 bypass the possibly singular intermediate quotient. Invariance
   under iteration and birational change retain their accepted import scope.
2. Use the dichotomy "has a rational first integral / has no rational
   first integral" to match Favre--Pereira. The producer's broader wording
   is not needed. Relative algebraic closure makes the pencil primitive;
   the base dominated by P2 is rational and the induced base map dominant.
3. In Favre--Pereira [Foliations invariant by rational maps](https://www.cmls.polytechnique.fr/perso/favre.charles/ratfol6.pdf),
   July8,2009 author PDF, the kodaira-zero lift is supplied by Lemma4.1
   and the prepared-model reduction. The kodaira-one lift is consumed
   from Theorem4.4 and the CorollaryB proof at named-import scope. Section4.5
   gives exhaustiveness; the modular possibility is excluded there.
   The proof does not replace this source with an unsupported assertion
   that an arbitrary finite cover lifts an arbitrary rational self-map.
4. In Theorem4.3's monomial row, use "nonsingular integral2x2 matrix with
   |det M|>=2". The source prints GL(2,Z) alongside that determinant
   condition; unimodularity is not assumed or used.

ROOT's producer source read covered Favre--Pereira body pages1--3,10--12,
16--17 and heading navigation, not its full dependency proof. FIRST read
pages1,2,8,9,10,11,12,16 of the same cached308050-byte PDF, mode444, SHA256
fb63dcf42b7ebe436f819749751011aadbfc6a59e5e790c2be4af41ac2cb2f9a.
FIRST's ONE Dinh--Nguyen acquisition succeeded in producing parsed paper
text; its selected body extracts were pages2,12,13, plus a heading index.
The paper's dependency proofs were not audited in full. The old review's
iteration/birational/topdegree imports are not retroactively expanded.

Source-custody defect: the new Dinh--Nguyen stream hash includes HTTP
headers plus PDF body, so it does NOT certify PDF byte identity with the
older acquisition. FIRST disclosed this and did not retry. Its parsed
text contained the named paper and numbered statements; the explicit
selected-statement review supports the named import, not a file-identity
or whole-paper certification. ROOT made no additional acquisition for
this integration and does not silently relabel that mixed-stream hash.

## Custody and delivery distinctions

The external review ended00:24:04 UTC with exit0/DONE; its author measured
completion00:23:49. The exact supervisor, descendants and cgroup were
verified absent00:25:21 BEFORE ROOT read the whole82-line terminal
receipt. ROOT then froze report/log/receipt444, whole-read the232-line
report and20-line log, and verified unchanged pre/post content hashes.
All eight charged snapshots were unchanged. Current charged files, four
governance pins, prompt, separate ACK, cached source and unchanged
launcher/adapter matched. The canonical producer manifest verified again.

The legacy receipt says BODY_SEALED/CLEAN; this is a marker boundary,
NOT a canonical seal. Direct verification of the raw FIRST fails for
missing Body bytes declaration, as expected under that legacy contract.
Its bytes are preserved, not retrofitted. This separate integration
uses the canonical begin/close/finalize/verify workflow.

The reviewer reports an early draft and checked partials, then a full
rewrite of its OWN unsealed report before completion. It reports only
the two permitted authored outputs and no prohibited persistence or
extra acquisition. The final-only CLI log is not a complete filesystem
side-effect audit, so those statements retain their self-reported scope.
Existing CLI settings warnings did not change the actually observed
read-only protected mounts; no shared settings or launcher repair was
made. Hosted identity and no-memory behavior are not independently
attested. These limits do not substitute for mathematical evidence.

The trusted collision checker run by ROOT after termination returned
EMPTY for the raw FIRST; the raw NOT RUN annotation is retained. No
scientific computation, cloud job or formal certificate was used.
Operational accounting remains in the separate HQ workspace.

## Strategy consequence and exclusions

The rational AREA-ONLY foliation shortcut is closed at this fixed
countertest. It is not evidence against the conditional polynomial
pencil/foliation/web theorems. Their missing source-specific existence
premise remains the actual gap. There is no finite-web successor,
parameter search or donor repair selected by this result; a new task
must change a global closing argument, not merely strengthen this example.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Author whole-body readback completed September21 00:29:05 UTC; only
the collision result and this completion footer followed.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9856`.
- Body SHA-256:
  `d8bb6af23265b0c826832c9d58c2fb68652b0e566641ba6f3ddf84f6e4355d69`.
- Frozen basis: `5bcc24c69b4d453e55eff6c2112df0cad7128708`.
