# Ideation round 20260903T1200Z — coordinator's own blind submission (Opus 5, cloud seat)

Written before opening any submission of this round (five lanes live,
none read; running research lanes' reports unread). Packet c90fa687,
basis 4250a6e4. Everything below is PROPOSAL unless it cites a bound
integration.

## 0. Verdict up front

1. **Q1 — I predict the screened census is still cofinally nonempty, and
   that this is the right outcome.** The tree's kill mechanism at j = 2 is
   arithmetic: b_min = P mod A₂ > h = d₂/(n − M₂). It killed both rays and
   every D = 105/117 row because those rows have P ≢ 0 mod A₂ with a large
   remainder. Rows with A₂ | P (b_min = 0) or with tiny remainder pass; such
   rows exist at D = 108 and their density in D is governed by divisor
   structure, exactly as the unscreened census was. So a screened cofinal
   family should exist (the lane should find one by solving A₂ | V₃d₂/d₃ in
   closed form), and the proof cannot be "the census empties". The screen's
   value is different: it is the first source-derived condition that is
   UNIFORM in D and uses a GLOBAL datum (all siblings), and it says what a
   uniform theorem must look like — a statement about every node at once.
2. **Q2 — the coefficient level has one honest formulation, and it is
   Moh's own: the tree of Belyi/ODE data must be realised simultaneously.**
   At every node the Appendix-I equation D(P_j, Q_j, p_j, q_j) = c_j p_j
   (Prop A.3) is a Davenport–Stothers / Belyi condition on (p_j, q_j); the
   whole-tree obligation (promoted) says every major child's (p, q) is
   again such a pair, glued to the parent by "the child's chart is the
   parent's factor recentred": σ_{j−1} = σ_j-data + πt^{δ_{j−1}}, with the
   Galois action of order A_j identifying conjugate children. So the
   coefficient-level object is a TREE OF DESSINS with gluing — the previous
   round's DESSIN-TOWER, but with the sourced universal quantifier over
   siblings instead of one path. Card II computed expdim = max(k − 2, 0)
   for ONE path; with every sibling forced, each extra major child adds a
   Belyi constraint (its own ODE) and shares the parent's coefficients,
   and the count changes. **First experiment: recompute the expected
   dimension of the whole-tree dessin object (all siblings, per-node ODE,
   Galois identification) on Moh's six and on the 52 screened excess
   rows.** A negative expected dimension on the 52 with ≥ 0 on the six
   would be the uniform coefficient-level condition the campaign is
   looking for; if it stays ≥ 0, the coefficient level is genuinely
   polynomial-system work (theorem (T)) and no count will do it.
3. **Q3 — attack (T) by running Moh's OWN §5 theory on the descended pair.**
   The descended pair (P, Q) has J = cγ^k, total degrees (n', m'), one place
   at infinity, gcd K' = K/d_s ≥ 4, and — crucially — its tower has s' = 2
   (m2-descent, promoted): two characteristic pairs. For Keller pairs Moh's
   Prop 5.5 handles s = 2 completely: it derives (12)/(13) and then the
   inequality V₂ > V₂ − U₂ = C(D + E) ≥ D ≥ V₂, a contradiction — that is
   how he proves s ≥ 3 in the search. Prop 5.5's proof uses δ₂ = −1 (from
   Prop 5.4, M₂ = n − 2) and the s = 2 fraction δ₁ = ((n* + m*)U₂ − 1)/
   ((n* + m*)V₂ − 1). For the descended pair the radii obey the rule Φ:
   δ' = (k + 1)·Def 5.1(3), so δ₂' = −(k + 1)·(…) and the p.207 table shows
   δ₂' ∈ {−1, −1/2} — NOT always −1. **The lane to launch: generalise Props
   5.4–5.6 to J = cγ^k** — the exact machinery is "monomial-Jacobian
   tolerant" since ord J enters JAC-FIBRE additively (delta 17(i)); write
   the s = 2 contradiction of Prop 5.5 with k in it; test whether it kills
   Moh's five descended rows (p.207) without Appendix II's hand work, and
   G2/G3. If Prop 5.5(k) is a theorem, (T) is proved for every u_s = 1
   skeleton whose descended pair has δ₂' = −1, and the residual is the
   δ₂' ≠ −1 case plus OPEN[MINOR-DICHOTOMY]. This is the single cheapest
   route from "reduction" to "theorem" on the table, because it reuses a
   proof Moh already wrote.
4. **Q4 — the mechanism outside boundary/tree/coefficients: there isn't one
   the record needs.** The three layers are exhaustive for a one-place-at-
   infinity analysis: N (boundary), the admissible multiplicity structure
   (tree), the polynomials (coefficients). What the record lacks is the
   THEOREM at the third layer, and I claim its shape is now visible: at
   s' = 2 the descended problem is a two-characteristic-pair problem with a
   monomial Jacobian, and two-pair problems are exactly what Abhyankar–Moh
   expansion techniques settle (this is the (n, m) with one characteristic
   pair world of the AM epimorphism theorem, one level up). The proof, if
   Moh's line closes, is: whole tree (done) → descent (done) → Prop 5.5(k)
   (to do) → minor dichotomy (to do).

## 1. Dispositions (changes only)

APPROACHES: row 1 RAISE (the receiver of (T): [P,Q] = cx^k pairs; the
campaign's certificate machinery is the terminal table); row 5 RETYPE
(monomial-Jacobian descent, depth-bounded); row 6 RAISE (Moh's §5 at
s = 2 is AM one-place theory); row 25 RAISE (tree of dessins with the
universal quantifier); row 16/45/29 LOWER to receivers (the moment engine
needs the tree as decoration; Gauss–Manin gave nothing cofinal); row 20
unchanged (LOW); row 36 RETARGET to the D = 108 screened survivors and
the 52 excess rows.
Q1: expect cofinal nonemptiness; the screen is a lemma, not the proof.
Q2: the whole-tree dessin count (card 1) then (T). Q3: Prop 5.5(k) (card
2). Q4: closed as above.
Lanes: screened-census CONTINUE; sibling-coefficients CONTINUE (it is
card 1's algebraic form); appendix2-compiler CONTINUE (it is the machine
for the 52); whole-tree-review-opus CONTINUE (second gate); descent-radii
DONE; the moment-engine family (d105-rank-gate, fixed-n6, a2six) STOP —
their conclusion is that the tree is the decoration; relaunch only as a
tree-decorated engine after card 1.

## 2. Bottlenecks reranked

Proof: (1) Prop 5.5 for monomial Jacobians (= (T) at δ₂' = −1); (2) the
u_s > 1 minor dichotomy in uniform form; (3) the whole-tree dessin
dimension (coefficient-level count); (4) the screened cofinality
question (decides whether (1)–(3) must be all-degree theorems or a
finite check). Disproof: (1) a screened cofinal family in closed form;
(2) the first D = 108 screened survivor through the Appendix-II compiler
(a SURVIVES there is the first positive signal above 100 that is not
killed by any sourced condition); (3) nothing else.

## 3. New avenue (required): PROP 5.5(k)

Stated in §0.3. Bounded OPEN[PROP55-K]: does the s = 2 contradiction of
Moh Prop 5.5 (pp.186–188) survive J = cγ^k for each k ≥ 0 — a yes/no per
k with the proof; cheapest test: rerun the proof's inequality chain with
ord J = k inserted in JAC-FIBRE and in the radius formula, on Moh's five
descended rows (p.207) — 2 h, one seat, source open.

## 4. New cross-connection (required): WHOLE-TREE × DESSIN-TOWER

Card II's expdim assumed one path; the promoted tree forces every major
sibling to carry its own ODE. The two objects are the same Hurwitz space
once the siblings are added; the sign of the corrected expected dimension
on the 52 excess rows vs Moh's six is a computable discriminator of the
coefficient level (card 1). Second connection: the Appendix-II shape rule
(from δ₁' via Φ) IS the Belyi profile of the descended bottom star — the
compiler and the dessin count are the same computation in two languages.

## 5. Strongest attacks

Proof: Prop 5.5(k) → (T) at δ₂' = −1 → (with the tree and the descent)
JC2 for every u_s = 1 skeleton; then the minor dichotomy. Counterexample:
the D = 108 screened survivor with the smallest descended system through
the compiler; a SURVIVES with a positive-dimensional family → attempt the
inverse descent (OPEN[DESCENT-LIFT]).

## 6. Software / decisive experiment

The tree-decorated moment engine is now specifiable: node ↔ disc; factor
multiplicity ↔ V; A_j ↔ orbit size; b ↔ zero child; Φ ↔ radii; Def 5.1(1)
↔ root counts per disc; the shape rule ↔ Puiseux templates. But the
cheaper decisive experiment is card 1 (a count, one afternoon).
Campaign-systems check: UPGRADE — every census number a lane prints must
carry its screen label (PATH-ARITH / TREE / TREE+ODE / +nested) in the
same line; today's ledger has three incompatible "alive" counts in
circulation (670 / 587 / 45) and the confusion cost is real. Test: grep
the next three lane reports for unlabeled counts.

## 7. Idea cards

CARD 1 — WHOLE-TREE DESSIN DIMENSION. Deps: delta 17(r), Prop A.3, Card
II's formula. Discriminator: expdim_tree on Moh's six (must be ≥ 0) vs
the 52 excess rows. Outcomes: negative on the 52 → a uniform coefficient
condition, promote and run to D ≤ 200; ≥ 0 → the coefficient level is
polynomial-system work; stop: 4 h desk.
CARD 2 — PROP 5.5(k). Deps: Moh pp.186–188, the rule Φ, the descent.
Discriminator: the inequality chain with k; test on p.207's five rows and
G2/G3. Outcomes: theorem → (T) at δ₂' = −1 (the flagship result of the
campaign so far); fails → the exact k-dependent obstruction is named.
Stop: 6 h.
CARD 3 — MINOR DICHOTOMY IN UNIFORM FORM. Deps: Moh p.209, Props 6.1–6.4.
Discriminator: state the two alternatives for the minor-disc π-root of
any u_s > 1 skeleton and the descent each induces; test on (99,66) (Moh's
own) and on G1. Outcomes: uniform → the u_s > 1 branch joins (T); not →
it is case work. Stop: 4 h.

## 8. Single first lane

CARD 2 (Prop 5.5 for monomial Jacobians) on an Opus seat with the source
open — it is the only lane whose positive outcome is a THEOREM about all
degrees rather than a filter, and it costs one proof Moh already wrote
plus a k.

<!-- BODY-END -->
