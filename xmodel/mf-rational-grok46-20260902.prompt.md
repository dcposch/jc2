# Desk lane: MF-RATIONAL — can the generic member of a Keller pencil be rational?

Reviewed (integration #11/#12): for a noninvertible Keller map F = (P,Q)
of geometric degree N under H2 and a generic line L, the generic member
C_L = F^{-1}(L) = {alpha P + beta Q = gamma} of the pencil is a smooth
affine curve with n(W − S) = N − 2 + 2 g_L + theta_inf (MF-EXACT), and
2 g_L + theta_inf >= W − S + 1 (integration #12; independently >= 2 by
the charged Grok lane via Miyanishi–Sugie 1980 Lemma 1.6 / Kaliman 1992
/ Neumann–Norbury 1998). The charged lane raises OPEN[MF-RATIONAL]: can
g_L = 0 at all — i.e. can the generic fibre of the polynomial
submersion u∘F = alpha P + beta Q be a RATIONAL curve (then with
theta_inf >= 2 and theta_L = nS + theta_inf places at infinity)?
Bounded quantity: g_L in [0, p_a(D_F)]; a NO (g_L >= 1 always) adds one
more unit to every floor (n(W − S) >= N + 1) and lowers every crossing
price by one.
Task, classical and exact: (1) State what is known about polynomials
f: C^2 → C with NO critical points whose generic fibre is rational
(Zaidenberg–Lin; Kaliman's theorem that a polynomial with generic fibre
≅ C is a variable; the C^*-fibre case; Neumann–Norbury's classification
of "rational polynomials" with given fibre topology; Miyanishi–Sugie);
which of these apply to f = u∘F, a submersion of degree D_F whose
generic fibre has theta_L = nS + theta_inf >= 3 places at infinity
(S >= 1, n >= 2, theta_inf >= 2 in the rational case)? (2) Use the
Keller structure: every other pencil coordinate v = gamma P + delta Q
restricts to C_L as an étale degree-N map v: C_L → A^1 (since
{u, v} = const ≠ 0) whose non-properness set is the n points of L ∩ A_F;
for a RATIONAL C_L ≅ P^1 minus theta_L points, v extends to a rational
function of degree N on P^1 — write the Riemann–Hurwitz for it and the
constraint that its poles are exactly the theta_L places with the
meridian cycle-type ramification over the n points; decide whether a
rational function of degree N on P^1 with those escapes can exist for
N >= 2 (small cases N = 2, 3, 4 by hand, then the general argument), or
exhibit a numerical solution. (3) If g_L = 0 is not excluded by (1)–(2),
say exactly what additional Keller datum would be needed (the "rational
polynomial" classification gives the possible fibre topologies; which
of them are compatible with all fibres being smooth and the map being
étale of degree N onto the punctured line?). Deliver a proof of g_L >= 1
(THEOREM) or the exact obstruction, typed, with the +1 consequence
priced. Discipline: consume MF-EXACT, MERIDIAN-FLOOR+, MF-DEFECT at
their reviewed typings; case (A) EMPTY; no Z(G) = 1; no A2. Desk only;
state the bounded quantity of any OPEN you raise; literature from refs/
or exact citation with statement; do not edit canonical ledgers; do not
inspect jc2-lean.
Report: xmodel/mf-rational-grok46-20260902.md
Seal-at-completion; bounded writes; target 10-18KB; 60 minutes.
charged_input=xmodel/mf-defect-mult-vs-beta-grok46-20260902.md
charged_input=xmodel/meridian-floor-sharpen-opus5-20260902.md
charged_input=xmodel/meridian-floor-sharpen-review-gpt55-20260902.md
charged_input=xmodel/n-vs-mapdeg-review-gpt55-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
5c11369a6b5d6198206dce722d7c1d657d687d2b074003a5970eb883a5fdfa65  {{LANE_INPUTS}}/mf-defect-mult-vs-beta-grok46-20260902.md
4fa4b5f60692ade07b3ce45405ab2623edb4ef3aef1174e34beaf2373ce2f2a4  {{LANE_INPUTS}}/meridian-floor-sharpen-opus5-20260902.md
32c043320d11b619ef717cbb2dc5f3ca1ec7756abaa5f470d2ee0fb49dfe7b82  {{LANE_INPUTS}}/meridian-floor-sharpen-review-gpt55-20260902.md
05d59097a3712d855ffd050aa8dc585af1860b606f53675340d0e334ea05c10b  {{LANE_INPUTS}}/n-vs-mapdeg-review-gpt55-20260902.md
```
