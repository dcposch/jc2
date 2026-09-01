# Research lane: Mathlib survey and formalization plan for Keystone 1

You are a bounded research lane opening the KEYSTONE 1 formalization
program (normalized-graph structure, four boxes, dicritical valuation
formula for noninvertible plane Keller maps). Read the statement in the
coordinator's brief below; full campaign proofs live in `xmodel/`
(`round1033-sheet-gate-opus5-20260831.md` and the block-descent
integrations) — consult them for the intended mathematical content, but
your deliverable is a LIBRARY SURVEY and an ordered LANE PLAN, not proofs.

## Keystone 1 statement (target)

F = (P,Q): C²→C² a noninvertible Keller map, d = [C(x,y):C(P,Q)] ≥ 2,
A = C[P,Q], B = integral closure of A in C(x,y), Y = Spec B, A_F the
Jelonek non-properness curve. Claims: (1) A ⊆ B ⊆ C[x,y], j: C² → Y an
open immersion (ZMT), q: Y → C² finite flat of degree d, q∘j = F;
(2) Y∖U nonempty, pure codim 1, A_F = q(Y∖U); (3) Σ_{y∈q⁻¹(p)} e_y = d,
and at a generic point of a branch of A_F the four-box sort: (U,e>1)
empty (étaleness), (U,e=1) has 1 ≤ a ≤ d−2 points, (Y∖U,e>1) nonempty
(purity); hence d ≥ 3; (4) for every dicritical/boundary prime B_j with
affine image: e_j = 1 + v_j(dx∧dy).

## Part A — Mathlib coverage survey (verify against CURRENT sources)

Two sources of truth, check BOTH and record which you used per item:
(i) the pinned Mathlib checkout on this machine (any
`.lake/packages/mathlib` under `~/code/math/jc2/jc2-lean/*/`, rev
`20bc12820422504f9e52ee6caebf8182a9015336`) — grep it directly;
(ii) current Mathlib master via GitHub search/web for anything that may
have landed since. For each item report: EXISTS (name the declarations),
PARTIAL (what exists, what's missing), or ABSENT, with evidence.

1. Zariski's Main Theorem — any form: classical (quasi-finite factors as
   open immersion ∘ finite), Grothendieck/EGA form, or the special case
   we need (normal B, birational finite-type inclusion into C[x,y]).
   Also: quasi-finite morphism API.
2. Zariski–Nagata purity of the branch locus — general, or any dim-2 /
   finite-over-regular special case; supporting depth theory:
   Auslander–Buchsbaum formula, Serre's criteria (R_k, S_k), depth API,
   Cohen–Macaulay modules/rings, miracle flatness (finite CM over
   regular ⇒ flat / free over local).
3. Finiteness of integral closure: for a finitely generated C-algebra
   domain / in a finite separable field extension of a Noetherian
   normal domain (trace-form argument). Krull domain API; localizations
   of a normal Noetherian domain at height-1 primes are DVRs.
4. Dedekind ramification: `sum_ramification_inertia`-style Σe·f = n and
   its hypotheses; different ideal, tame ramification in char 0;
   whether the semilocal reduction (localize base at a height-1 prime,
   extension becomes Dedekind) is smooth to set up.
5. Jacobian criterion for étale/unramified/smooth ring maps (invertible
   Jacobian ⇒ formally étale for polynomial algebras); standard smooth
   algebras API.
6. Kähler differentials: Ω¹, wedge/exterior powers (Ω² usable?), the
   valuation of a 2-form along a divisorial valuation — any bridge
   between `Module.KaehlerDifferential` and valuations/DVR uniformizers.
7. Scheme layer: is anything forced out of pure commutative algebra?
   Assess whether the whole of K1 can be stated ring-theoretically
   (height-1 primes of B; "open immersion" replaced by an explicit
   localization/unit statement) to avoid the AlgebraicGeometry library,
   and what statement-strength is lost if so.
8. Algebraic independence of P,Q from Jac(P,Q) ≠ 0 (char 0); C(x,y)
   finite over C(P,Q) with the degree-d API we need.
9. Jelonek non-properness set: anything at all (expect ABSENT); propose
   the minimal internal definition (e.g. the image of the boundary
   primes, taking (2) as the DEFINITION of A_F for the formalization,
   turning the Jelonek comparison into a separately-cited remark).

## Part B — ordered lane plan

Output a lane-by-lane plan in the max11 style (each step = one bounded
Lean lane with named consumables), with these constraints:
- Stage 0: a self-contained project skeleton (new lake project
  `keystone-graph/` beside the others; single package, Mathlib pinned to
  the same rev as the campaign; Palomar sandbox rules: one package, all
  build artifacts under its own .lake).
- Stage 1 (fast win): the (3)-sum + étale-box + (4) valuation-formula
  sub-theorem in the ring-theoretic recasting, using the Dedekind
  machinery found in Part A. Flag exactly which hypotheses (normality of
  B, finiteness of B over A, algebraic independence) enter as
  assumptions at this stage and which are discharged.
- Stage 2: finiteness/flatness of q and the codim-1 structure of Y∖U.
- Stage 3: the ZMT factorization and purity pillars — for each, either
  identify the Mathlib-shaped path (with the dim-2 shortcut spelled
  out: Auslander–Buchsbaum + reflexive modules, van der Waerden-style)
  or declare it a long-lane library project with an effort estimate.
- Mark every stage with: Mathlib coverage %, risk, and what can proceed
  in parallel with the Max-11 campaign without contending for the box.

## Report

Write `xmodel/k1-mathlib-survey-and-plan-opus5-20260901.md`. Evidence
per claim (declaration names, file paths, or search queries that came up
empty). UNVERIFIED labels where you could not check. No proofs, no
overclaims; the plan must be executable by Grok/Opus Lean lanes with the
campaign's box-verify contract.
