# Hostile FIRST: exact degree and no foliation for one rational area map

Reviewer: Fable 5.1 (hosted identity not independently attested), independent of
the ROOT (gpt-6-astra) producer. Lane rational-area-no-foliation-first-20260921T001000Z.
Date: September 21, 2026 UTC. Evidence tier of the review: MANUAL desk check with the
producer's named imports read at the sections listed below. Lifecycle: FIRST review of a
PRODUCER-CHECKED, UNPROMOTED report; promotion is AUDIT's call, not mine.

Reviewed target: xmodel/rational-area-no-foliation-swarmHQ-root-20260921T000430Z.md
(body SHA-256 985358ee..., full SHA-256 3170a730...). Frozen contribution commit
5bcc24c69b4d453e55eff6c2112df0cad7128708; producer basis 80a39666a7f1ddb4f6a127a63e6d4f7cef179ad7;
HQ governance basis 47d13ff0d490b7cb3dd8116cebfb04bedf32811d.

## Verdict

Both new claims survive at the producer's stated scope: for the fixed rational map
F = (y/(2x), y^4/(16x^4) - x^2), the first dynamical degree is exactly 4, and no positive
iterate preserves an algebraic foliation on P2. The proof is conditional only on the
named Favre--Pereira classification and the Dinh--Nguyen degree comparison, at the
scopes fixed below. No first unsupported implication was found. Four binding
clarifications (no gaps) are recorded in the section "Clarifications". This confirms
no no-web theorem, no polynomialization obstruction, no Keller statement and no JC2
consequence; F has a pole along x = 0 and is not a Keller map.

| # | Interface | Verdict |
| --- | --- | --- |
| 1 | Degree-4 tuple, basepoints, contracted curves, fixed exceptional image | CONFIRMED |
| 2 | No divisorial cancellation in every iterate; algebraic stability | CONFIRMED |
| 3 | No-first-integral reduction, classification exhaustiveness, cyclic-cover lift | CONFIRMED at import scope |
| 4 | Same-dimensional Dinh--Nguyen attachment | CONFIRMED, citation clarified |
| 5 | Five fibration normal forms excluded upstairs by the product formula | CONFIRMED |
| 6 | Torus row: algebraic integers, spectral identities, 2^-m impossible | CONFIRMED |
| 7 | Monomial row: spectral radius, determinant, integrality | CONFIRMED |
| 8 | Negative control, all-iterate quantifier, rational scope | CONFIRMED |

## 1. Homogeneous presentation

Independently recomputed. T(x,y) = (x, y/(2x)) has inverse (u, 2uv); F(u,2uv) = (v, v^4 - u^2),
so G = T F T^-1 = (v, (v^4 - u^2)/(2v)) = (v, v^3/2 - u^2/(2v)). With u = U/Z, v = V/Z the
common denominator is 2VZ^3, giving [2V^2Z^2 : V^4 - U^2Z^2 : 2VZ^3]. The middle entry is
congruent to -U^2Z^2 modulo V and to V^4 modulo Z, so the tuple is reduced of degree 4.
Simultaneous zeros: V = 0 forces U^2Z^2 = 0, giving [0:0:1] and [1:0:0]; Z = 0 forces
V = 0, giving [1:0:0] again. Exactly two basepoints.

Contracted curves: on VZ != 0 the map fixes v and u^2, so every fiber has at most two
points and no curve there is contracted or sent to infinity. On V = 0 the tuple is
[0 : -U^2Z^2 : 0], on Z = 0 it is [0 : V^4 : 0]; both lines go to a = [0:1:0], and a is
regular and fixed since G(a) = [0:1:0]. The line at infinity is therefore accounted for
as one of the two contracted lines. CONFIRMED.

## 2. Algebraic stability for every iterate

A divisorial common factor in the tuple of G composed with G^n exists exactly when
some curve C has G^n(C) equal to a basepoint of G (vanishing at finitely many points
is not a divisor). Tracking generic images: each C_k is a curve until the first
contraction, which can only occur through V = 0 or Z = 0, producing a, and a is
fixed and not a basepoint. Hence no iterate maps a curve to b0 or binf, and
deg(G^n) = 4^n. This is the standard exceptional-orbit criterion, applied correctly;
it is an all-n argument, not a fit.

Independent hand control: the tuple of G^2 has entries 8V^2Z^6(V^4 - U^2Z^2)^2,
(V^4 - U^2Z^2)^4 - 16V^6Z^10, and 16V^3Z^9(V^4 - U^2Z^2). The middle entry is
U^8Z^8 modulo V, V^16 modulo Z, and -16V^6Z^10 modulo each factor V^2 -+ UZ, so
there is no common factor and deg(G^2) = 16. Birational invariance gives
lambda1(F) = 4; the reviewed generic degree gives lambda2 = 2; the power rule gives
(4^m, 2^m) for G^m. Consistent with the promoted bound lambda1 >= 3. CONFIRMED.

## 3. Reduction and classification transfer

First-integral case. If the foliation has a rational first integral, take a
primitive one r; its base is dominated by P2, hence rational (Lueroth), and G^m
maps generic leaves to leaves, so r composed G^m lies in the relative algebraic
closure of C(r), which is C(r) itself: r composed G^m = phi(r) with phi nonconstant.
Composing with T gives (r composed T) composed F^m = phi composed (r composed T), a
preserved pencil for F^m, contradicting the promoted no-pencil theorem. CONFIRMED.

No-first-integral case. Favre--Pereira Theorem A (page 1) requires a holomorphic
singular foliation on a projective surface without rational first integral and a
dominant non-invertible rational map preserving it. P2 is projective, G^m has
topological degree 2^m >= 2, and the report's definition of algebraic foliation is
the saturated rational 1-form direction, which is exactly their object. Section 4.5
(page 16, read): Miyaoka and McQuillan give a model with reduced singularities and
nef cotangent bundle; Proposition 3.4 gives (T^*F)^2 = 0, excluding general type;
the remaining trichotomy is modular, kod 0, kod 1; the modular case is excluded by
Proposition 4.7, which forces a biholomorphism, so a map of topological degree 2^m
is impossible there; rational fibrations are excluded by the no-first-integral
hypothesis. Exhaustiveness is an inherited import, not re-audited here.

Lift. Lemma 4.1 (page 9, read) lifts phi itself, not a power, to the cyclic cover
once the foliation is phi-prepared, which Proposition 3.5 and Definition 3.6
(page 8, read) supply after contracting finitely many curves. The proof on page 10
constructs phi-hat with pi composed phi-hat = phi composed pi. The proof of
Corollary B (page 16, read) states the output form used by the report: a projective
surface X-hat, a dominant map, a cyclic group G of automorphisms commuting with it,
with (phi, X, F) birationally conjugate to the quotient. For Kodaira dimension 1
the same output is asserted by the same proof ("the arguments are essentially the
same"), and Theorem 4.4's statement carries the cover generated by an automorphism
tau; the branched double-cover step on page 12 relies on total invariance of the
transverse critical curve. This is import scope, consistent with the producer's
declared tier. No iterate replacement is needed; the report's hedge is harmless.
CONFIRMED at import scope.

## 4. Same-dimensional Dinh--Nguyen attachment

Read at arXiv:0903.2621v1, page 2. Theorem 1.1 is stated for PROJECTIVE manifolds
X, Y of dimensions k >= l with dominant meromorphic f, g, pi and pi composed f
= g composed pi. Its index range 0 <= j <= l, 0 <= p - j <= k - l forces j = p when
k = l, giving d_p(f) = d_p(g) d_0(f|pi). The relative degree of order zero is the
n-th root of a mass that does not depend on n, hence 1; the cover degree N never
enters. Dinh--Nguyen also state the same-dimensional conclusion directly as
Corollary 1.2 (page 2): for compact Kaehler X, Y of the same dimension, semiconjugate
f and g have equal dynamical degrees, and they note that generic fibers of pi are
finite of constant cardinality with f inducing bijections between them.
Proposition 3.6 (page 13) treats disconnected generic fibers explicitly, and the
remark after Proposition 3.3 (page 11) records d_p(f^n|pi) = d_p(f|pi)^n.

Applicability: every upstairs surface in Theorems 4.3 and 4.4 (torus, ruled surface
over an elliptic curve, P1 x P1, P1 x E) is smooth projective, P2 is projective, and
pi is the finite quotient followed by the birational map to P2, a dominant
meromorphic map. The singular intermediate model is bypassed. The topological
degree identity is also elementary from multiplicativity along pi. CONFIRMED.

## 5. Fibration rows upstairs

kappa0(2), kappa0(3): ruled surface X-hat -> E with the map (x^k, ky) or (zeta x + b,
zeta y) covering a dominant endomorphism of E. kappa0(4): (x^k, ky) on P1 x P1 covers
y -> ky. kappa1(1): (lambda x, x^m y^k) covers x -> lambda x. kappa1(2): (lambda x,
lambda^(n+1) y) on P1 x E covers both projections. With a curve base, Theorem 1.1
gives lambda1 = max(d_1(g), d_1(f|pi)) and lambda2 = d_1(g) d_1(f|pi), both factors
at least 1 by Proposition 3.6, so lambda1 <= lambda2. Applied to phi-hat upstairs,
where interface 4 already gives (4^m, 2^m), this is 4^m <= 2^m, false for all m >= 1.
No descent through the cyclic group is used or needed. CONFIRMED.

## 6. Torus row

The lift is affine z -> Lz + c with L complex-linear preserving a rank-4 lattice;
as a real map it is an integral 4 x 4 matrix whose complexification is L direct sum
its conjugate, so alpha, beta, and their conjugates are its eigenvalues and are
algebraic integers. H^2 of the torus is the second exterior power of H^1, and the
(1,1) part carries eigenvalues alpha alpha-bar, alpha beta-bar, beta alpha-bar,
beta beta-bar; the spectral radius is |alpha|^2, matching the report's Hermitian
mass argument, and Jordan blocks change nothing after n-th roots. The topological
degree is |det L|^2 = |alpha beta|^2. Then beta beta-bar = lambda2/lambda1 = 2^-m,
a rational non-integer that is a product of algebraic integers: impossible. The case
|alpha| = |beta| is covered by the same equation. CONFIRMED.

## 7. Monomial row

Favre--Pereira write M in GL(2,Z) but impose |ad - bc| >= 2, so M is an integral
nonsingular matrix, as the report says. lambda2 = |det M| is the topological degree
on the torus; lambda1 = rho(M) because the degree of the n-th iterate on P1 x P1 is
comparable to the entrywise norm of M^n and Gelfand's formula gives rho(M). Nonreal
eigenvalues are conjugate with |det M| = rho(M)^2, giving 16^m = 2^m, false. For real
eigenvalues, one is +-4^m and the other is +-2^-m; even more simply, the second
equals trace minus the first, an integer of modulus strictly between 0 and 1.
CONFIRMED.

## 8. Negative control and quantifiers

M = [[3,1],[1,1]]: determinant 2, trace 4, eigenvalues 2 +- sqrt 2, so lambda1 = 2 +
sqrt 2 >= 3 > 2 = lambda2. The eigenvectors of the transpose have irrational slope,
so the two logarithmic eigenfoliations have no rational first integral and this is a
genuine kappa0(5) example that meets the OLD promoted bound lambda1 >= 3 with
lambda2 = 2. Hence lambda1 > lambda2, and even lambda1 >= 3, cannot exclude the
torus and monomial rows; the exact integer value 4 is load-bearing, as the report
says. The proof fixes an arbitrary m >= 1 throughout and each contradiction holds
for every such m, so the all-positive-iterate quantifier is honored. The scope is
rational: the constant-multiplier argument of the polynomial foliation theorem is
not used, and no finite-web or construction-family extension is made. CONFIRMED.

## Clarifications (binding wording, not gaps)

1. The same-dimensional Dinh--Nguyen statement should be cited as Corollary 1.2, with
   Theorem 1.1's stated hypothesis being projectivity of X and Y, which holds here.
2. The reduction dichotomy should read "rational first integral", matching Theorem A.
   An algebraic first integral yields a rational one through symmetric functions,
   so the report's wording is harmless.
3. The Kodaira-dimension-1 lift is taken from the Corollary B proof and Theorem 4.4's
   statement, at import scope; the report already declares this tier.
4. "GL(2,Z)" in Theorem 4.3 means integral nonsingular with |det| >= 2.

## Source coverage actually read

Favre--Pereira, cached PDF SHA-256 fb63dcf42b7ebe436f819749751011aadbfc6a59e5e790c2be4af41ac2cb2f9a,
308050 bytes, mode 444, unchanged. Pages read via bounded pdftotext stdout: 1, 2, 8,
9, 10, 11, 12, 16 (eight of the ten allowed). Not read: 3 to 7, 13 to 15, 17.

Dinh--Nguyen, one acquisition of https://arxiv.org/pdf/0903.2621v1 at 00:20 UTC, streamed
into a shell variable, 23 pages parsed, no persistent copy. Targeted extracts read on
pages 2 (Theorem 1.1, Corollary 1.2), 12 (Proposition 3.5), 13 (Proposition 3.6); a
heading index also emitted one truncated line each from pages 1, 3, 9, 10, 11, 14, 18,
20, 21. Whole pages were not read. DEFECT: my command redirected curl's header dump
into the hashed stream, so the measured value (263445 bytes, SHA-256
9ad5e24bd58641a69f1228ed3298262fc18d590d7183152fec34bc36867472e2) covers HTTP headers
plus body and is NOT comparable with the earlier review's c673394d... PDF hash; the
HTTP status and redirect chain were not captured. No retry was made. The parsed text
is unmistakably the Dinh--Nguyen paper with the expected theorem numbering.

## Delivery deviations

- Only the two authorized files were written: the 444 ACK and this report. No git
  mutation, no subcalls, no CAS, no protected-tree access, no scratch or cache files.
- The report was rewritten in full at 00:23 UTC by an apply_patch delete-and-add of
  the same path (draft and checked partials at 00:12, 00:16, 00:21 UTC preceded it).
- The trusted collision checker was not run; ROOT runs it after termination.
- Each tool output stayed below 16 KiB. APPROACHES.md was read in four chunks to EOF.

## Pin/read manifest

Charged inputs under /tmp/jc2-lane.pPzk5V/inputs, pre-pins measured 00:12 UTC, all equal
to the admission list: README.md 7181a9dd..., AGENTS.md 31f54fa5..., COORDINATION.md
9b7a45ae..., APPROACHES.md 5b51a06a..., FALLACY-v2.md e47fd16c...,
rational-area-no-foliation-swarmHQ-root-20260921T000430Z.md 3170a730..., its
.artifact.json aba9f54c..., rational-area-no-pencil-integration-swarmHQ-root-20260920T215300Z.md
bf9dbcdb.... All eight whole-read. HQ files via git show at 47d13ff0: AGENTS.md
06ba4c08..., POLICY.md 29d6bcea..., RESEARCH_POLICY.md 710fcf0c..., RUNBOOK.md
ac18350c..., all whole-read and matching. Post-pins: see the line appended below.

## OPENS RAISED

None.

## COLLISIONS

status: NOT RUN by this reviewer (no explicitly raised OPEN entries; ROOT runs the checker).

Post-pins measured 00:23:34 UTC: all eight charged snapshots UNCHANGED (same SHA-256
prefixes 7181a9dd, 31f54fa5, 9b7a45ae, 5b51a06a, e47fd16c, 3170a730, aba9f54c, bf9dbcdb).

Author whole-body readback completed 00:23 UTC (225 lines, EOF confirmed). Measured
author completion: 2026-09-21T00:23:49Z. Not sealed; parent retains receipt/hash custody.
<!-- BODY-END -->
