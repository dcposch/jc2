# DIVREVIEW0650 hostile mathematical review

Reviewer: requested existing Sol adapter/model gpt-5.6-sol; hosted identity unverified.  
Object: the frozen NEGATIVEWHOLE0612 argument. This is a first independent review; the reviewer did not author the co-designed candidate.  
Verdict: **PASS_CONDITIONAL**.

## Exact verdict and hypotheses

For the exact normalized hypothetical polynomial Keller map \(H\) used by
NEGATIVE0100, with field degree \(N>1\), the new implication is valid:

\[
 H_\bullet|_{D}\text{ noninjective},\quad D=\{A<0\}
 \quad\Longrightarrow\quad
 \exists\text{ divisorial }v\in D\text{ with }f_v>1.
\]

This verdict retains the predecessor's hypotheses that \(D\) is a convex weak
valuative tree, \(H_\bullet:D\to D\) is continuous and finite-to-one, and the two
specified zero-thinness inverse ends force its noninjectivity. It also retains the
standard surface-valuation facts explicitly used below: finite algebraic extensions
preserve rational rank and residue transcendence degree; irrational valuations admit
finite monomial charts and finite principalization of any fixed finite set of rational
functions along the valuation; divisorial tangent directions are residue-curve
places; and surface rational-map indeterminacies resolve by finitely many point
blowups. These named foundations were not source-audited here.

The verdict does **not** assume the central all-direction correspondence. That
correspondence, including incoming directions and indeterminacy points, follows from
the rank-two restriction calculation below. The candidate's co-design JSON was not
treated as independent evidence.

## 1. Weak-tree nested loops: PASS, with a local repair

Use the following precise germ hypothesis. For every parameterized source arc and
each interior parameter \(t\), some punctured interval on each side of \(t\) maps
into a single component of the target tree minus \(f(t)\), and the two components
are distinct.

Suppose a continuous finite-to-one \(f\) is not injective on an arc. Choose
\(I_0=[a_0,b_0]\) whose endpoints have common image \(p_0\) and whose interior has
no \(p_0\)-preimage. Given \(I_i=[a_i,b_i]\) with this property, let \(m_i\) be its
ordinary parameter midpoint and \(q_i=f(m_i)\ne p_i\). If \(m_i\) is the only
\(q_i\)-preimage in \(I_i\), each half joins \(q_i\) to \(p_i\) without meeting
\(q_i\) again. Connectedness then puts both one-sided germs at \(m_i\) in the
\(p_i\)-component, a contradiction.

Otherwise take either interval from \(m_i\) to an adjacent \(q_i\)-preimage. Its
endpoints both map to \(q_i\), its interior avoids \(q_i\), its parameter length is
at most half that of \(I_i\), and both endpoints are strictly inside \(I_i\) because
\(q_i\ne p_i\). Call it \(I_{i+1}\). If the construction never stops, the nested
intervals shrink to one parameter \(t_*\), which is interior to every \(I_i\).
Their left and right endpoints converge to \(t_*\), while the two endpoints of each
\(I_i\) have the same image \(p_i\ne f(t_*)\). For all large \(i\), that same point
\(p_i\) would therefore lie in both distinct side components at \(f(t_*)\), impossible.

Thus no target metric, finite subdivision, uniform weak neighborhood, or target
limit theorem is needed. The candidate's requested “away from the old root” side
also exists: at a first or last \(q_i\)-preimage the exterior side is the old-root
direction, so the adjacent interior side is different; at an internal preimage at
most one adjacent side is the old-root direction. Choosing it makes the target
components nested by tree separation. However, that extra choice is unnecessary.
The sentence that the whole closed \(I_{i+1}\) maps into an open component is
literally false at its endpoints; “the interior maps into it” is the correction.
This wording defect does not affect the repaired proof above, and special target
endpoints cause no exception: they cannot support two distinct side germs.

## 2. Irrational interior points: PASS_CONDITIONAL on the named local facts

Let \(v\) be irrational and \(w=H_\bullet v\). For the finite field extension,
the value-group quotient is finite and the residue extension algebraic, so \(w\)
again has rational rank two and residue transcendence degree zero. Choose target
monomial parameters \(U,V\) at \(w\), whose values are rationally independent.
Resolve the rational map at the center of \(v\), and principalize the two fixed
pullbacks along \(v\). After finitely many point blowups there are source monomial
parameters \(u,z\) and units \(\epsilon_1,\epsilon_2\) with

\[
 H^*U=u^a z^b\epsilon_1,\qquad
 H^*V=u^c z^d\epsilon_2
\]

on one cone containing the irrational ray. This is finite local principalization
of two functions, not a global monomialization assertion.

Writing \(\alpha=v(u)\), \(\beta=v(z)\), rational independence of the two target
values forces
\(\det\begin{pmatrix}a&b\\c&d\end{pmatrix}\ne0\); otherwise those values would be
rationally dependent. Shrink the slope cone so the same centers and expressions
apply. Units then have value zero, including at nearby rational slopes, and the
target slope is a fractional-linear function of \(\alpha/\beta\) with nonzero
derivative. Scalar normalization in \(H_\bullet\) cancels from that ratio. Hence
the two sides of the irrational ray map to the two distinct target sides. Exact
monomial-times-unit expressions also rule out the proposed cancellation problem.

## 3. Every divisorial direction: PASS

Take raw divisorial valuations \(v=\operatorname{ord}_E\) and
\(w=\operatorname{ord}_D\), scaled so that on the target field

\[
 v|_{K_{\rm tgt}}=e\,w.
\]

Restriction gives an inclusion of residue fields
\(\iota:\mathbf C(D)\hookrightarrow\mathbf C(E)\), hence a rational map
\(\phi:E\dashrightarrow D\). Both curves are smooth complete rational curves, so
\(\phi\) extends across every point, independently of whether a chosen surface
model for \(H\) is indeterminate there. Its degree is \(f_v\).

For every closed point \(p\in E\), including the point representing the incoming
direction, form the composite rank-two valuation “first \(\operatorname{ord}_E\),
then \(\operatorname{ord}_p\) on the residue field.” If \(q=\phi(p)\), restriction
to the target has the triangular form

\[
 (n,m)\longmapsto (e n,\;c_p n+r_p m),
\]

where \(r_p>0\) is the local degree of \(\phi\) at \(p\). The coefficient \(c_p\)
is precisely where zeros or poles of the normal-coordinate unit contribute. It
changes the secondary weight of a target uniformizer but not the residue place
\(q\). Likewise, normalizing \(H_*v\) subtracts a multiple of the first component
from the second and cannot change \(q\) or erase the positive \(r_p m\) term.

Rank-one points on the \(p\)-side converging to \(v\) approximate this composite
valuation, so their images lie eventually in the \(q\)-direction at \(w\). This
is the required arc-germ statement. At a surface indeterminacy point, finitely
resolve the map on the source; the strict transform of \(E\), its residue map, and
the composite-place restriction are unchanged. Thus the calculation covers
distinguished, incoming, and initially indeterminate directions, not merely a
generic affine part of \(E\).

If \(f_v=1\), \(\phi:\mathbf P^1_E\to\mathbf P^1_D\) is an isomorphism, so
\(r_p=1\) and distinct source directions have distinct target directions for
**all** \(p\). This establishes the central divisorial step rather than adding it
as a hypothesis.

Combining Sections 2 and 3, if every negative divisorial \(v\) had \(f_v=1\), the
two sides at every interior point of every arc in \(D\) would have distinct image
germs. Section 1 would make \(H_\bullet\) injective on each arc, hence on convex
\(D\), contradicting the inherited noninjectivity. The claimed divisorial witness
therefore follows.

## 4. Auxiliary normal-to-residual transfer: PASS

Let negative \(E\) map to \(D\) with normal index \(e>1\). Choose a general closed
point of \(E\) where the surface map is regular, no other pullback component meets
\(E\), and the separable residue map is unramified. With target parameters
\(D=(U=0)\) and \(V\) tangential with \(V(H(p))=0\), set the **source** parameter
\(w=H^*V\) exactly. Then, for a source normal parameter \(u\),

\[
 H^*U=u^e a(u,w),\qquad H^*V=w,\qquad a(0,0)\ne0.
\]

Thus there are no lower-\(u\) tangential terms to discard. The free-blowup
valuation \(\nu(u)=\nu(w)=1\) restricts to primitive target weights \((e,1)\), so
its normal index is one. If \(s=\operatorname{res}(u/w)\), then

\[
 \operatorname{res}(H^*(U/V^e))=a(0,0)s^e,
\]

and the residue-field degree is exactly \(e\). For the actual constant-Jacobian
map, the raw discrepancy/thinness relation is \(a_E=e\,a_D\); a free blowup gives
\(a_{\rm new}=a_E+1=e\,a_D+1<0\), since the negative raw integer \(a_D\le-1\)
and \(e>1\). This auxiliary lemma is valid, with the stated genericity, but is not
needed for the main arc proof.

## 5. Application and remaining gap

The final contradiction uses exactly the predecessor's normalized \(H\), its
field degree \(N>1\), and its already established noninjectivity on \(D\). It does
not assume \(D\) open or locally compact, use a weak-tree metric maximum, invoke
scalar norm or atomic-measure identities, infer that every polynomial residual
degree is one, or derive gonality, properness, or \(N=1\).

The rational constant-Jacobian pole-bearing donor remains compatible with this
reduction. What remains open is the genuinely global polynomial statement that
**all** negative divisorial valuations of an actual hypothetical Keller map have
residue degree one (or another theorem excluding every such residual fold). The
candidate proves no such exclusion. Accordingly this is a conditional reduction,
not a JC2 result; JC2 remains open.

No exit-price assertion is made, so no charge_basis object applies.

## Reviewer coverage

- input-manifest.json lines 1–132, whole, read first. Copied-file metadata was
  checked in groups of eight and six before body reading. A preceding metadata-only
  stat against a nonexistent provenance-prefixed location read no body.
- Whole governors: HQ-AGENTS.md 1–23; HQ-POLICY.md 1–112;
  HQ-RESEARCH_POLICY.md 1–162; HQ-RESTRICTIONS.md 1–259;
  HQ-RUNBOOK.md 1–507; PUBLIC-AGENTS.md 1–22; PUBLIC-README.md 1–102;
  PUBLIC-COORDINATION.md 1–107; PUBLIC-FALLACY-v2.md 1–36. Total 1,330 LF.
- HQ-STATE.md lines 1–200, whole, completed after the governors and before any
  mathematical body; counted separately.
- Scientific inputs, all whole: candidate-root.md 1–18;
  candidate-astra.json 1–12; predecessor-negative0100.md 1–13;
  predecessor-independent-review.md 1–123. Total 166 LF.
- Total non-STATE body coverage: 1,628 LF (manifest 132 + governors 1,330 +
  scientific inputs 166). Repeated body LF: 0. Clipped or cropped windows: 0.
  Primary-source body LF: 0. No archive body, whole APPROACHES.md, unlisted
  source, source/history query, download, CAS, control family, or protected tree
  was inspected.
- Named but unaudited foundations were limited to the inherited predecessor
  valuation-tree/thinness/inverse-end facts and the finite-extension, finite-blowup,
  local-principalization, resolution, and rank-two tangent-place facts stated above.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11285`.
- Body SHA-256:
  `6723d10cd6a6fd521d9e6951820f0a7ba2313f4d5501b6dc6211fca60524050d`.
- Frozen basis: `8b2578db54ebb4eef46291b642cf61146f83dbdb`.
