# Hostile FIRST review: rational exact-area map with no invariant pencil (CONFIRMED at scope)

status: COMPLETE (review written, whole-author readback done; not sealed)
lane: rational-area-no-pencil-first-20260920T213000Z
reviewer: Fable 5.1 (requested; hosted identity unattested), independent of ROOT producer
utc_start: 2026-09-20T21:29:41Z
contribution_commit: d9d50a11e21c9eb308e4ae1a27845d28442f2522
producer_basis: 339707ae305f39b08920849e5c7ce100736093bf
hq_governance_basis: 3d8b961fb5e660b98620c5ce01b62ce8884c5e79

## Pin manifest (pre-read)

Seven charged snapshots under /tmp/jc2-lane.4TVxwA/inputs, sha256 measured before reading,
all EQUAL to the contract values:

    README.md        7181a9dd4cf928e5327ee5324ccf7861098e2b7321395852418aa8c7808fbbdf
    AGENTS.md        31f54fa5b1a9f76dc5455dd6c42615e565b47b96499c6fc69f389980e762a96f
    COORDINATION.md  9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e
    APPROACHES.md    127a838cbd9b77ef3b82905250f0355ca9e1acc0a8149537959b4ad71b1f7f1e
    FALLACY-v2.md    e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5
    xmodel/rational-area-no-pencil-swarmHQ-root-20260920T211700Z.md
                     5eac76fbe32a7be2ea2bad8f56f8db51c06cf62f04004705c4c41a2c41957cdd
    ...artifact.json bdd3229d88c2b4c25afc8851a2e506dd3869817874ed426451ada1a0bcbc9998

All seven whole-read (APPROACHES.md in four byte-range chunks). The ROOT body hash
7f8131d6300255fea6d894ee79e32a35a5980fb47091f925b6a1449850c59b61 / 9088 bytes in the
artifact record matches the report's own seal text (not independently recomputed).

HQ governance at 3d8b961fb5e660b98620c5ce01b62ce8884c5e79 via git show, whole-read,
all EQUAL to the contract pins: AGENTS.md 06ba4c08..dd0c34f (1520 B), POLICY.md
29d6bcea..a38c42393 (5412 B), RESEARCH_POLICY.md 710fcf0c..fca910778 (7008 B),
RUNBOOK.md ac18350c..97c3bef3da (15416 B, two chunks).

Post-read pins: appended in the completion section.

## Verdicts

Overall: CONFIRMED at the report's stated scope. Evidence tier MANUAL with the
named Dinh--Nguyen import; lower bound lambda1(F)>=3 only; no polynomial, Keller,
foliation, web or JC2 conclusion. I found no unsupported implication, so there is
no "first failing step" to report. Two citation-precision notes (items 5 and 7)
do not affect the mathematics. Reviewer does not promote; ROOT integrates.

### 1. Jacobians, field degree, domains: CONFIRMED

dD = [[2x,0],[-y/(2x^2),1/(2x)]], det = 2x*(1/(2x)) = 1. dH = [[0,1],[-1,4v^3]],
det = 0 - (1)(-1) = 1. H^{-1}(s,t) = (s^4-t,s) checked both ways. F = H(D(x,y)) =
(y/(2x), (y/(2x))^4 - x^2) = (y/(2x), y^4/(16x^4) - x^2) by substitution. On {x!=0}
the chain rule gives det dF = 1, so F^*(dx^dy) = dx^dy as rational 2-forms.
Field: F^*C(x,y) = D^*(H^*C(u,v)) = D^*C(u,v) = C(x^2, y/x) =: C(p,q) since H^* is
an automorphism of C(u,v). C(x,y) = C(p,q)(x) with x^2 = p, so the degree is <= 2.
p,q are algebraically independent (x,y are algebraic over C(p,q), trdeg 2), so
C(p,q) is a pure rational function field in which p is prime, hence not a square:
degree exactly 2. The generic fiber is exactly {(x,y),(-x,-y)}, not merely "at
least two points". lambda2(F) = topological degree = 2 (source, actual read:
"d_k(f) is also called the topological degree ... equal to the number of points in
a generic fiber of f"). Domains: D and F are rational with poles along x=0; H is a
polynomial automorphism of A^2. F|{x!=0} is a morphism with unit Jacobian, hence
etale. F(x,0) = (0,-x^2) lies on the pole line, so {x!=0} is NOT forward invariant
(a witness; the report only says "not asserted", which is consistent).

### 2. Rational conjugacy: CONFIRMED

T(x,y) = (x, y/(2x)), T^{-1}(u,v) = (u,2uv); T T^{-1} = id and T^{-1} T = id checked.
F(T^{-1}(u,v)) = F(u,2uv) = (v, 16u^4v^4/(16u^4) - u^2) = (v, v^4-u^2); then
T(v, v^4-u^2) = (v, (v^4-u^2)/(2v)) = G. So G = T F T^{-1} and G^n = T F^n T^{-1}:
a genuine birational conjugacy, direction irrelevant since T and T^{-1} are both
birational. Dynamical degrees are bimeromorphic-conjugacy invariants (source, actual
read, introduction recalling Dinh--Sibony: "if f and g are conjugate, they have the
same dynamical degrees"; Prop 3.5 for relative degrees). Only conjugacy is used to
transfer lambda1; lambda2 was computed directly in (x,y). det dG = u/v checked;
T^{-1*}(dx^dy) = 2u du^dv and G^*(2u du^dv) = 2v*(u/v) du^dv = 2u du^dv checked.
Reviewer remark, not a claim expansion: Phi = F T^{-1} = (v, v^4-u^2) is polynomial
with det dPhi = 2u, nonconstant. The non-area-preserving precomposition is exactly
what makes it polynomial, which is why the report's polynomialization disclaimers
are needed and correct.

### 3. Weighted-degree induction: CONFIRMED

With weights (1,3), delta(PQ) = delta(P)+delta(Q) because weighted leading forms
multiply to a nonzero form in a domain; hence delta(P/Q) = delta(P)-delta(Q) is
independent of the representative. Cancellation rule: for A = P1/Q1, B = P2/Q2,
A+B = (P1Q2+P2Q1)/(Q1Q2), and the numerator terms have weights delta(A)+delta(Q1Q2)
and delta(B)+delta(Q1Q2); when these differ the leading form survives, so
delta(A+B) = max. Recursion: G^{n+1} = G(G^n) gives u_{n+1} = v_n and
v_{n+1} = (v_n^4-u_n^2)/(2v_n) = v_n^3/2 - u_n^2/(2v_n) (same rational functions as
G^n(G)). Base n=0: (1,3). Step: delta(v_n^3/2) = 3*3^{n+1} = 3^{n+2};
delta(u_n^2/(2v_n)) = 2*3^n - 3^{n+1} = -3^n; distinct, so v_{n+1} has a nonzero
leading form of weight 3^{n+2}, in particular v_{n+1} != 0 and the next division is
legitimate. delta(u_{n+1}) = 3^{n+1}. Valid for every n. Hand checks: v_1 =
(v^4-u^2)/(2v), delta = 12-3 = 9; v_2 = ((v^4-u^2)^4 - 16v^6)/(16v^3(v^4-u^2)),
delta = 48-21 = 27. No CAS, no sampled fit.

### 4. Passage to projective degree, lower bound only: CONFIRMED

Let [P0:P1:P2] be a reduced homogeneous representative of G^n of degree d_n. P0 != 0
(dominance: image not inside the line at infinity), and P0(u,v,1) != 0 because P0
is homogeneous nonzero; P2(u,v,1) != 0 because v_n != 0. As elements of C(u,v),
v_n = P2(u,v,1)/P0(u,v,1); removing common factors does not change delta of the
quotient. delta(P0(u,v,1)) >= 0 (nonnegative weights) and delta(P2(u,v,1)) <=
3*deg <= 3 d_n. Hence 3^{n+1} <= 3 d_n, i.e. d_n >= 3^n. d_n is the degree of
(G^n)^*H on P^2, so lambda1(G) = lim d_n^{1/n} >= 3 (limit exists by
submultiplicativity). Check at n=1: G = [2vw^3 : 2v^2w^2 : v^4-u^2w^2] has no common
factor, d_1 = 4 >= 3, so the bound is not sharp and equality is correctly NOT
claimed (FALLACY floor/attainment respected).

### 5. Product-formula attachment: CONFIRMED, with one citation-precision note

Theorem 1.1 of arXiv:0903.2621v1, ACTUAL READ: "Let X and Y be projective manifolds
of dimension k and l respectively with k >= l. Let f: X->X, g: Y->Y and pi: X->Y be
dominant meromorphic maps such that pi o f = g o pi. Then d_p(f) =
max_{max{0,p-k+l} <= j <= min{p,l}} d_j(g) d_{p-j}(f|pi) for 0 <= p <= k."
There is no polynomiality, properness, finiteness or connected-fiber hypothesis.
Disconnected generic fibers are explicitly handled: the proof of Proposition 3.6
(actual read) states "for non-critical values y of pi, the fibers L_y are not
necessarily connected but they contain the same number s of components".
Instantiation: X = P^2, Y = P^1 (projective), k=2, l=1, f = F^m, pi = r (a
nonconstant rational function is a dominant meromorphic map to P^1), g = phi, which
is nonconstant because r o F^m is nonconstant for dominant F^m. p=1: j in {0,1},
d_1(F^m) = max(d_0(phi) d_1(F^m|r), d_1(phi) d_0(F^m|r)). p=2: j=1 only,
d_2(F^m) = d_1(phi) d_1(F^m|r) = a b. With d_0(phi) = 1 (verbatim "1 = d_0(f)") and
d_0(F^m|r) = 1, d_1(F^m) = max(a,b). Positivity: Proposition 3.6 verbatim,
"d_p(f|pi) >= 1 for 0 <= p <= k-l", so b >= 1; a = d_1(phi) = deg phi >= 1. For reals
>= 1, max(a,b) <= ab; no integrality or generic-fiber interpretation is needed.
Powers: verbatim "d_p(f^n) = d_p(f)^n for n >= 1", so lambda1(F^m) >= 3^m > 2^m =
lambda2(F^m), contradiction. No iterate preserves any rational pencil.
Citation-precision note: the captured statement of Proposition 3.6 is log-concavity
of p -> log d_p(f|pi) plus d_p(f|pi) >= 1; it does not itself state d_0(f|pi) = 1.
That equality follows from the displayed definition lambda_p(f^n|pi) =
<(f^n)^*(omega_X^p) ^ pi^*(omega_Y^l), omega_X^{k-l-p}> (actual read, proof of
Prop 3.5) at p = 0, where (f^n)^*(1) = 1 under the paper's graph-pullback
convention, the same convention behind the verbatim 1 = d_0(f); the "in particular
>= 1" clause of Prop 3.6 presupposes it. The sentence stating d_0(f|pi) = 1
explicitly (probably near Proposition 3.3 or the definition) was not in my bounded
excerpts, so the report's attribution "Proposition 3.6 and its proof" is
approximately right but not verified to the sentence. Mathematics unaffected.

### 6. Poles and excluded stronger readings: CONFIRMED

Poles along x=0; the regular etale open is not forward invariant (witness in item
1). The report explicitly disclaims a polynomial Keller counterexample, any
foliation/web exclusion, polynomialization, and exact lambda1; all disclaimers are
present and correct. Consistency with the promoted rational exact-area invariant
theorem (APPROACHES, September 19): that theorem assumes a preserved nonconstant
rational function and concludes birationality; here no such function exists for
any iterate, so there is no conflict and no new implication about Keller maps.

### 7. Dependencies, source scope, tier: CONFIRMED with minor notes

MANUAL tier with one named import (Theorem 1.1, Prop 3.6 positivity, iterate rule,
topological-degree interpretation) is honest; PRODUCER-CHECKED/UNPROMOTED is the
right lifecycle. The source-scope disclosure matches the actual read: PDF stamp
"arXiv:0903.2621v1 [math.DS] 15 Mar 2009", typeset line "November 4, 2018", abs page
"[Submitted on 15 Mar 2009]", 23 pages, Tien-Cuong Dinh and Viet-Anh Nguyen; the
abstract and Theorem 1.1 use PROJECTIVE manifolds, satisfied by P^2 and P^1.
Minor notes: (a) the item-5 citation location; (b) absolute-degree conjugacy
invariance is recalled in the paper's introduction (Dinh--Sibony) while Section 3
(Prop 3.5) gives the relative version; either suffices for the report's use.
No first unsupported implication exists; no replacement family, exact lambda1, or
new theory is proposed here.

## Primary-source read record

- https://arxiv.org/abs/0903.2621 : ONE acquisition, curl -sL --max-time 30, HTTP 200,
  38690 bytes, no redirect, 21:34:29Z. Read: title, authors, submission line
  "[Submitted on 15 Mar 2009]", abstract, comments "23 pages", subjects, MSC.
- https://arxiv.org/pdf/0903.2621v1 : ONE acquisition, HTTP 200, 262766 bytes,
  content-type application/pdf, no redirect, 21:34:41Z. Bytes held only in a
  shell-local base64 variable; text via pdftotext -layout on stdin to a shell-local
  variable (1157 lines, 64651 chars); PDF sha256
  c673394d498d4b542c446863f3668b7bb0ae5a7ba291e0e9fa428fb5a12d8d49. No file written.
- Sections ACTUALLY READ (bounded excerpts): header/abstract and introduction
  opening (semi-conjugacy definition, bimeromorphic invariance recall, relative
  degree description); statement index; Theorem 1.1 with its index-range remark and
  Corollary 1.2; log-concavity recall "1 = d_0(f) < ..."; Section 3 opening
  (definition of lambda_p(f^n), "d_p(f^n) = d_p(f)^n", topological degree = number
  of points in a generic fiber); Proposition 3.5 statement and proof (relative
  bimeromorphic invariance, displayed definition); Proposition 3.6 statement and
  first half of proof (disconnected fibers, s components).
- NOT read: Section 2, Propositions 3.1-3.4 bodies, Section 4 (proof of Theorem
  1.1), Corollaries 1.3-1.4 bodies, applications. Memory versus read: every quoted
  statement above is from the actual text; the only inferred item is the exact
  location of the sentence d_0(f|pi) = 1 (item 5). No other source, version, mirror,
  API or retry was used; no Diller--Lin reread.

## Deviations / harness persistence

- Authored files: the 444 ACK and this report only. No scratch, cache, notes,
  memory, index, settings or credential writes. CLAUDE_CODE_DISABLE_AUTO_MEMORY=1
  observed. Harness-side transcript persistence is outside reviewer control and is
  disclosed as possible.
- Every tool output was bounded below 16 KiB (large inputs read in byte ranges).
- No Git mutation, model subcalls, CAS or scientific code, cloud, protected-tree,
  jc2-lean/jc2-web, STATE, journal or peer-payload access. HQ files read only via
  git show at the pinned basis.
- Collision checker not run by the reviewer (no OPEN entries raised; left to ROOT).
- Startup ACK written once and chmod 444 at 21:29Z; initial DRAFT/INCOMPLETE report
  written at 21:30Z before any lengthy read. The service cap (1200 s from launch)
  may end before the 21:50Z partial target; this body is the checked partial.

## Measured completion

- Post-read pins measured 21:40:43Z with sha256sum -c against the seven contract values
  (quiet mode prints only mismatches): "rc=0 " (rc=0 means all seven EQUAL).
- Whole-author readback of this report completed 21:40Z (12903 bytes read in full).
- Body word count excluding the pin/read manifest is below 2200.
- Measured completion UTC: 2026-09-20T21:40:43Z. Not sealed or finalized; parent retains legacy
  receipt/hash custody. No descendants, no claim expansion, no promotion by reviewer.

<!-- BODY-END -->
