# Two elliptic special-fiber components — independent Fable FIRST

Reviewer: independent Fable, requested model=fable/effort=max; hosted identity
self-reported, not independently attested. Publication editor: swarmHQ ROOT
(Astra), September18, 2026.
Evidence: MANUAL independent reconstruction, no scientific computation.
Verdict: CONFIRMED for the producer's four exact items. This is an auxiliary
counterexample, not a Keller pair or resolution of JC2.

Frozen producer commit: db26943e39cfdada4ee17889d362928aaff5512a.
[Producer](reducible-elliptic-fiber-swarmHQ-root-20260918T065100Z.md),
full SHA-256 ac6ce54b1de8bdfb1f36bc41b9b9d68313fafb12fe1e622976e1ad5976fe33ff.

This publication preserves verbatim the terminal review's contiguous
mathematical text from “Verdicts” through the end of “Findings.” Operational
headers, paths and duplicate custody tables are omitted; this is NOT a
byte-identical copy of the entire original. The original remains preserved
unchanged at full SHA-256
1b27429a67f93850b35e6022dfef56edf6a7dd79908108b84639854eea86de6a
(14306 bytes). Its legacy completion/hash custody is distinct from this
publication's own author-completion and canonical artifact seal.

The reviewer read the producer, FALLACY-v2, COORDINATION and APPROACHES
whole. The cited earlier cubic-base comparison reports, AUDIT, PROGRESS
and historical journal were not read and are not proof premises.
All four input hashes were unchanged before/after review and at collection.
The supervisor and descendants were independently terminal before receipt-
first intake; ROOT then read the WHOLE original review and log. Custody
and model agreement do not substitute for the proof.

## Begin verbatim mathematical review

## Verdicts

1. Polynomial expansion / inverse chart / Jacobian sign / nonsingularity (incl. x=0 chart): **CONFIRMED**
2. Two disjoint reduced irreducible components, no hidden x-factor, smooth cubic models, genus one: **CONFIRMED**
3. No polynomial constant-nonzero-Jacobian mate: **CONFIRMED** (polynomial Q only; no rational-mate inference made)
4. Scope (auxiliary shortcut only; not JC2, not a Keller pair, not a rational-mate theorem); total degree 36: **CONFIRMED**

No REFUTED item. No GAP. One presentational nit under item 2 (repeated-factor case),
closed by the producer's own smoothness argument; not a gap.

## Findings

Every calculation below was reconstructed by hand from the producer's definitions;
nothing was accepted on the producer's word.

### 1. Expansion, chart, Jacobian sign, nonsingularity — CONFIRMED

Expansion. Put t = x^2 + x^6*y, so a = 1 + t and a^3 = 1 + 3t + 3t^2 + t^3 with
t^2 = x^4 + 2x^8 y + x^12 y^2 and t^3 = x^6 + 3x^10 y + 3x^14 y^2 + x^18 y^3. Hence
a^3 = 1 + 3x^2 + 3x^4 + x^6 + 3x^6 y + 6x^8 y + 3x^10 y + 3x^12 y^2 + 3x^14 y^2 + x^18 y^3
and 3a x^2 = 3x^2 + 3x^4 + 3x^8 y. The x^2 and x^4 terms cancel and 6x^8 y − 3x^8 y = 3x^8 y:
B = a^3 − 3a x^2 = 1 + x^6 + 3x^6 y + 3x^8 y + 3x^10 y + 3x^12 y^2 + 3x^14 y^2 + x^18 y^3,
exactly the producer's eight terms. x^6*C = x^6 + 3x^6 y + 3x^8 y + 3x^10 y + 3x^12 y^2 + 3x^14 y^2 + x^18 y^3,
so B = 1 + x^6 C term by term. Then 1 − B^2 = −2x^6 C − x^12 C^2 = −x^6 C (2 + x^6 C) = −x^6 C K,
so P = (1 − B^2)/x^6 = −C K is a polynomial identity (no deletion of x = 0).

Chart. z = 1/x, v = a/x = x^{-1} + x + x^5 y. Inverse: x = z^{-1},
y = (v − z − z^{-1}) z^5 = z^5 v − z^6 − z^4. Both compositions checked:
v -> z + z^{-1} + z^{-5}(z^5 v − z^6 − z^4) = v and
y -> x^{-5}(x^{-1} + x + x^5 y) − x^{-6} − x^{-4} = y. So C[x,x^{-1},y] ≅ C[z,z^{-1},v]
as C-algebras (map declared, generator order (x,y) -> (z,v), coefficient field C).

Jacobian sign. z_x = −x^{-2}, z_y = 0, v_y = x^5, so
J_xy(z,v) = z_x v_y − z_y v_x = −x^3 = −z^{-3}: negative sign, NONCONSTANT.
Cross-check from the inverse: x_z = −z^{-2}, x_v = 0, y_v = z^5 give
J_zv(x,y) = −z^3 = 1/(−x^3), consistent.

P in the chart. g(v) = v^3 − 3v = (a^3 − 3a x^2)/x^3 = B/x^3, so
P = x^{-6} − (B/x^3)^2 = z^6 − g(v)^2.

Nonsingularity on x != 0. (dz, dv) is a cotangent basis at every point because the
chart Jacobian is a unit there; dP = 6z^5 dz − 2 g g' dv and 6z^5 != 0. Direct
cross-check in (x,y): P_y = P_v x^5; if P_y = 0 then P_v = 0 and
P_x = P_z z_x = 6z^5·(−x^{-2}) = −6 x^{-7} != 0.

Omitted chart x = 0. C(0,y) = 1 + 3y, K(0,y) = 2, so P(0,y) = −2(1 + 3y) = −2 − 6y and
(∂P/∂y)(0,y) = d/dy P(0,y) = −6 != 0 for every y. No critical point on the line
x = 0. Together: no critical point anywhere on A^2. The x = 0 gap is closed.

### 2. Exactly two disjoint reduced elliptic components — CONFIRMED

Disjoint, no x-factor. K − x^6 C = 2, so C = 0 and K = 0 share no point. C(0,y) = 1 + 3y
and K(0,y) = 2 are nonzero, so x divides neither C nor K, hence not P; no component of
P = 0 lies in x = 0 (such a component would be the line x = 0, forcing x | C or x | K).

Chart forms. C = (B − 1) z^6 = (z^{-3} g − 1) z^6 = z^3 (g(v) − z^3) and
K = 1 + B = 1 + g(v)/z^3 = z^{-3}(g(v) + z^3); z^{±3} are units. So
V(C) ∩ {x != 0} ≅ {z^3 = g(v), z != 0} and V(K) ∩ {x != 0} ≅ {z^3 = −g(v), z != 0}.

Smooth cubics. F_ε = Z^3 − εV^3 + 3εVW^2; F_Z = 3Z^2, F_V = −3ε(V^2 − W^2), F_W = 6εVW.
Common zero: Z = 0, VW = 0, V^2 = W^2, hence V = W = 0, not a point. By Euler
(3F = Z F_Z + V F_V + W F_W) a singular point is exactly a common zero of the partials,
so E_1 and E_{−1} are smooth projective cubics.

Irreducible AND reduced (the step the producer compresses). Any factorization
F = F_1 F_2 with deg F_i >= 1, INCLUDING F_1 = F_2, has V(F_1) ∩ V(F_2) != ∅ in P^2
(Bezout), and at such a point all three partials of F vanish. So F_ε is irreducible as
a form; homogenization is multiplicative, so f_ε = v^3 − 3v − εz^3 is irreducible in
C[z,v]. It is prime in the UFD C[z,v] and not associated to z (f_ε(0,v) = v^3 − 3v != 0),
so it stays prime in C[z,z^{-1},v]. Hence C and K are prime in C[x,x^{-1},y]. An
irreducible factor of C in C[x,y] that becomes a unit after inverting x is c·x^k, i.e.
associated to x, excluded by x ∤ C. So C and K are irreducible in C[x,y]; they are
non-associate (degrees 15 != 21; coprime by K − x^6 C = 2). P = −C K is squarefree
with exactly two irreducible components, each of multiplicity one. The producer's
sentence "a reducible plane cubic would have intersecting components" states only the
distinct-factor case; the repeated-factor case is covered by the same smoothness
argument. Presentational nit, not a gap.

Genus one. Smooth plane cubic: genus (3−1)(3−2)/2 = 1. V(C) is irreducible, so its open
part x != 0 is dense and its function field is that of E_1; geometric genus 1. Same for
V(K) and E_{−1}. Both affine components are smooth: at a point of V(C),
dP = −K dC with K != 0, so dC != 0 by item 1; symmetrically for K.

Missing-chart points. V(C) meets x = 0 only at (0, −1/3) (C_y = 3 there, smooth);
V(K) never. Consistency check: along C = 0 as x -> 0 with y bounded, z/v -> 1 and
1^3 = 1 = ε for E_1, whereas s = 1 is not a root of s^3 = −1, matching K(0,y) = 2.
Adding or removing finitely many smooth points does not change geometric genus.

### 3. No polynomial constant-nonzero-Jacobian mate — CONFIRMED

Chain-rule factor. [P_z P_v; Q_z Q_v] = [P_x P_y; Q_x Q_y]·[x_z x_v; y_z y_v], so on x != 0
J_zv(P,Q) = c · J_zv(x,y) = c·(−z^3) = −c z^3, NOT c. The nonconstant chart Jacobian is
correctly retained by the producer.

Restriction to the special fiber. On E°_ε = V(g − εz^3) ∩ {z != 0} the pullback of dP is
zero: P_z dz + P_v dv = 0 with P_z = 6z^5 != 0, so dz = −(P_v/P_z) dv and
d(Q|E) = Q_z dz + Q_v dv = (P_z Q_v − P_v Q_z)/P_z · dv = (−c z^3)/(6 z^5) dv = −(c/6)·dv/z^2.
This is an identity of rational 1-forms on E_ε because E° is dense. Q|E is a genuine
rational function since Q ∈ C[x,y] is regular on the affine curve; this is the only
place polynomiality of Q is used. Both components work; one suffices.

Holomorphic differential ω = dv/z^2 on E_ε, all three point types:
(i) finite, z != 0: F_z = 3z^2 != 0, so v is a local parameter; dv regular nonzero,
z^{-2} a regular unit.
(ii) finite, z = 0: v ∈ {0, √3, −√3}; g'(v) = 3(v^2 − 1) equals −3, 6, 6, all nonzero, so
the roots are simple and z is a local parameter; 3z^2 dz = ε g'(v) dv gives
dv/z^2 = 3 dz/(ε g'(v)), regular and nonzero. Order count: ord(v − v_0) = 3,
ord(dv) = 2, ord(z^{-2}) = −2, total 0.
(iii) infinity, W = 0: V != 0 (else Z = 0 too); u = W/V, s = Z/V, s^3 = ε(1 − 3u^2); at
u = 0, s^3 = ε != 0 and G_s = 3s^2 != 0, so u is a local parameter; v = 1/u, z = s/u,
dv = −du/u^2, dv/z^2 = −du/s^2, regular and nonzero.
These cover E_ε (W != 0 split by z = 0 or not; W = 0). ω is holomorphic, nowhere zero,
and nonzero as a form (v is nonconstant on E_ε; characteristic zero).

Exactness contradiction. If Q|E is nonconstant it has a pole of order m >= 1 at some
point of the projective curve; with local parameter t, Q = t^{-m} u, u(0) != 0, and
dQ = t^{-m-1}(−m u + t u') dt has a pole of order m + 1 because −m u(0) != 0 in
characteristic zero, contradicting d(Q|E) = −(c/6) ω holomorphic. If Q|E is constant,
d(Q|E) = 0 != −(c/6) ω since c != 0 and ω != 0. Contradiction either way; no polynomial
Q with J_xy(P,Q) = c ∈ C* exists.

Scope guard honoured. The argument needs Q to restrict to the fiber. It says nothing
about a rational Q whose denominator vanishes identically on V(C) or V(K), and the
producer says so (lines 130-132, 167-168). I draw no rational-mate conclusion.

### 4. Scope and total degree 36 — CONFIRMED

Leading terms. C's unique top-degree term is x^12 y^3 (degree 15). K = 2 + x^6 C has
unique top term x^18 y^3 (degree 21). P = −C K has top term −x^30 y^6: total degree 36,
no cancellation possible (unique top monomials). The producer's descriptors (C: 15,
P: 36) are correct.

Scope wording. Items 1-3 together show: a nonsingular polynomial can have a reducible
zero fiber with NO rational component (both components genus one). That refutes only
the auxiliary shortcut "nonsingular + reducible special fiber => rational component".
It is not a Keller pair (item 3 proves P has no polynomial mate at all), not a JC2
statement, not a rational-mate theorem, and says nothing about all Keller fibers. The
producer's lines 26-32 and 164-171 assert exactly this and no more; no overreach found.
The producer's negative control (item 3) and both missing-chart restrictions
(C(0,y) = 1 + 3y, K(0,y) = 2) were reconstructed above and are correct.

Not checked, not a premise: the comparison paragraph's statements about the accepted
cubic-base example (every closed fiber irreducible) and the pre-admission search
statements. They are not premises of the proof and were outside this review's scope.

Dependency completeness note: beyond the producer's listed facts, the irreducibility
step uses Bezout in P^2 and the UFD property of C[x,y] and of its localization at x.
Standard; recorded for completeness, not a gap.

FALLACY-v2 pass: ring map declared with generator order and coefficient field and
image-checked both ways; pole identities applied only on a smooth projective curve in
characteristic zero with every hypothesis checked; g'(v) is a genuine derivative
(defined by "differentiating z^3 = εg(v)"), not a label; no exit claim, so no
charge_basis line applies; no sat()/remainder items apply (no CAS).

## End verbatim mathematical review

## ROOT integration and scope

ROOT independently checked the expansion, inverse chart, negative
nonconstant chart Jacobian, missing-source line, factor count, cubic
smoothness and genus, and the special-fiber differential argument.
No correction of a mathematical claim is needed. The review's repeated-
factor clarification is valid: any nontrivial homogeneous factorization,
including repeated factors, gives a projective zero of both factors
and a zero gradient, inconsistent with the displayed smoothness check.

The claim is limited to this explicit P and the stated auxiliary
implication under nonsingularity. A statement that uses the existence
of an ACTUAL polynomial Jacobian mate is not refuted. Indeed this P has
no such mate. The special-fiber argument does not permit restriction
of arbitrary rational Q whose denominator vanishes on that fiber, so
NO rational-mate exclusion is promoted. No all-fiber classification,
construction family, historical novelty, or JC2 conclusion follows.

Dependencies are elementary characteristic-zero algebra, localization of
a polynomial UFD, projective plane intersection, the genus formula for a
smooth plane cubic, and pole orders of differentials on smooth projective
curves. No earlier campaign theorem or unreviewed result is a premise.

Four charged input SHA-256 pins, unchanged at ROOT collection:

- Producer: ac6ce54b1de8bdfb1f36bc41b9b9d68313fafb12fe1e622976e1ad5976fe33ff.
- FALLACY-v2: e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.
- COORDINATION: 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e.
- APPROACHES: 34ac40c113bbd5d68ea21fbc534303cd2bf3c1f76949997f505545ff4162dbd6.

Desk-only review. No CAS, numerical test, scientific Python or new
source retrieval. Original reviewer collision check NOT RUN; the
publication editor's administrative check follows, not attributed to Fable.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

ROOT publication COMPLETE September18 07:04 UTC: the verbatim mathematical
extract was compared equal to the original contiguous text; all charged
pins matched at collection and the collision tool returned this block.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13774`.
- Body SHA-256:
  `1065e33e9f0cd4e96a877fb48abdf3e3f16066ccc84a35043778ca31575f25bb`.
- Frozen basis: `db26943e39cfdada4ee17889d362928aaff5512a`.
