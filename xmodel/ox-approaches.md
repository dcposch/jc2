# Ox independent survey: the JC2 approach landscape

Date: 2026-08-22. Scope: all top-level routes to prove or disprove JC2 that I
can articulate, including bad and exotic ones. This is deliberately written as
a fresh survey; where it overlaps `APPROACHES.md`, overlap is noted, but no
attempt was made to preserve that document's merged labels or scores.

Scoring: for every approach not substantively tried by this campaign, I give a
1–10 promise score for the cheapest concrete experiment. The score means
"expected decisive information per unit effort," not probability of solving
JC2. For campaign-tried lanes, no new score is assigned.

## Executive verdict

- The campaign's central structural gap remains exactly what `REDUCTION.md`
  says: there is no universal landing theorem from an arbitrary Keller pair to
  the enumerated sheet/book data, and no absolute ceiling on topological degree.
  Almost every book-side success below is therefore a necessary-condition mill.
- The strongest live theorem cluster is: vertex-gap/residue rigidity,
  GGV-to-Sigray normalization transport, td-7 tower closure, and modular
  D23/D25 nonemptiness with a D43 prolongation obstruction. The last item is
  the most important recent change in the landscape.
- The best untried high-leverage directions are now: (1) global symplectic
  primitive/action-residue geometry beyond the already-derived local pins;
  (2) primitive monodromy plus coupled two-cover descent as a td bound; (3)
  graph-Picard/torsion obstruction at infinity; (4) HC4 degree-five module,
  now sharpened by the valid HC4⇒JC2 bridge; and (5) certificate-mining across
  the existing farm rather than another isolated solve.
- Several apparently novel-looking computational ideas are already present in
  the repo's lateral memos but have never been run; I mark them explicitly.

## A. Direct plane algebra and geometry

### A1. Newton-polygon corner families and finite degree farms

**Essence:** enumerate admissible Newton supports/corners below a cutoff and
prove each coefficient system empty.

**Campaign:** yes. This is the repository's origin and active farm:
`README.md`, `CAMPAIGN.md`, `lib/jc.py`, `lib/reduce.py`–`reduce4.py`,
`lib/families.py`, `SECTION4-AUTOMATION.md`, `AUDIT.md`.

**Obstruction:** every completed case is conditional on the reduction chain,
and no degree/type ceiling makes the census finite. Large exact certificates hit
a memory wall; see `CERT-UPGRADE.md`. The (72,108) settlement proves a bounded
theorem, not JC2.

### A2. Sheet-number / Eggers–Wall / dicritical tree exclusion

**Essence:** resolve infinity, decorate the boundary tree, and exclude all
compatible topological-degree configurations.

**Campaign:** yes, extensively. See `SIGRAY-AUDIT.md`,
`SHEET6-CAMPAIGN.md`, `BOOK-OFFAXIS.md`, `TOWER-UNIFORM.md`,
`TOWER-TD11.md`, `BOOK-TD12.md`.

**Obstruction:** `REDUCTION.md` records no universal endpoint/landing theorem
and no td ceiling. Even promoted td results are book-relative unless coverage is
proved separately. Composite/off-axis/post-jump sectors retain open residue.

### A3. Vertex-gap, strip ODEs, and the residue functional

**Essence:** use face valuations to isolate a low-dimensional strip equation and
extract a nonzero residue obstruction.

**Campaign:** yes; one of the campaign's real theorem clusters.
`LEMMA.md`, `SURPLUS.md`, `SURPLUS-EXT.md`, `RESIDUE.md`, `MATHIEU.md`, and
`paper1/main.tex`.

**Obstruction:** scope is thin strips, depth-two columns, and favorable axis
conditions. Extra columns introduce simultaneous residues instead of one ODE,
and no theorem places an arbitrary Keller pair in that geometry.

### A4. Formal Puiseux/jet prolongation and algebraization of a germ

**Essence:** prolong J=1 at increasing depth; either kill every finite window or
certify a compatible formal/algebraic counterexample germ.

**Campaign:** yes, deeply and currently live. See `SHEET6-DIRECTIONB.md`,
`DEPTH-STAB.md`, `SOL-ALGEBRAIZATION.md`, `notes.md` D23/D25/D43 entries, and
`xmodel/sol-round6.md`.

**Obstruction:** nonempty modular windows do not imply characteristic-zero
germs; stabilization of projections does not imply inverse-limit points. The
new D43 result says sampled D25 cells fail to prolong, but family-wide emptiness
still requires the symbolic compatibility ideal, and any surviving formal germ
still needs algebraization and polynomiality.

### A5. Jung–van der Kulk degree descent for Keller pairs

**Essence:** imitate elementary automorphism reductions until a Keller component
degree drops.

**Campaign:** not as a general program. `TRANSPORT.md` proves simultaneous
normalization, not descent; `AM-CHECK.md` tests a different criterion.

**Obstruction:** the cusp leading forms block triangular shears, and the
amalgamation theorem applies only after invertibility is known. The precise
cusp-avoidance lemma is missing.

**Cheapest untried experiment — 5/10:** enumerate reduced Jung words of length
≤6 over Q and F101 and test whether any coordinate has an (m,n)-initial face in
the relevant cusp ideal. This proposal appears in `xmodel/sol-lateral3.md` but
has not been executed.

### A6. Abhyankar–Moh coordinate recognition

**Essence:** force a component/fiber/place to be one-place, then apply the
coordinate theorem.

**Campaign:** partial and negative on the tested object. See `AM-CHECK.md`.

**Obstruction:** the current template fibers are multi-place. The correct
one-place objects would be components of the nonproperness/asymptotic set, whose
global structure is unpinned.

**Cheapest untried extension — 6/10:** compute all place semigroups of the
asymptotic-set components for one smallest surviving book, then test the AMS
inequalities there.

### A7. Nonproperness set and Jelonek asymptotic values

**Essence:** JC2 is equivalent to emptiness of the asymptotic-value set; classify
that set directly.

**Campaign:** partial consistency checks only. `SHEET6-CLASSICAL.md` and
`TEMPLATE-ATTACK.md` pass classical checks but never construct A(F).

**Obstruction:** constructing A(F) is nearly as hard as resolving the unknown
map at infinity. Local pole data do not determine component intersections or
cross-fiber correspondence.

**Cheapest untried experiment — 7/10:** for one minimal μ=6 survivor menu,
compute elimination/valuation data for all asymptotic branches, including
component intersections and exceptional preimages.

### A8. Generic-fiber differential, adjoints, and Gauss–Manin constraints

**Essence:** exploit exactness of f dg − x dy and g df − y dx through fiberwise
cohomology, adjoint pairings, or Gauss–Manin variation.

**Campaign:** partially adjacent. `RESIDUE.md`, `MATHIEU.md`, and the level-42
no-log pins in `SHEET6-DIRECTIONB.md` use local action residues, but the global
Mittag-Leffler/adjoint test proposed in `xmodel/sol-avenues2.md` has not been
run.

**Obstruction:** Poincaré exactness also holds for genuine counterexamples, so
the missing content must be a global boundary/primitive constraint, not local
closedness.

**Cheapest untried experiment — 7/10:** in the generic genus-18 residue-A
passport sector, construct Rosenlicht adjoints and evaluate all residue pairings
against the Keller primitive's principal parts.

### A9. Global symplectic primitives and action residues

**Essence:** integrate the closed Keller forms globally and demand compatibility
of their polar/principal-part data at infinity.

**Campaign:** local pins are proved (`SHEET6-DIRECTIONB.md` §7), but the global
primitive lemma is unexecuted. Adjacent proposals occur in
`xmodel/sol-avenues2.md` and `APPROACHES.md`.

**Obstruction:** polynomial primitives exist for counterexamples too. The route
dies unless polar divisors, residues, or monodromy of the primitive produce an
illegal invariant.

**Cheapest untried experiment — 8/10:** compute explicit polynomial primitives
for tame automorphisms and a degree-(3,4) product; compare their polar divisors
with the residue-A leading pair. If the automorphism controls already saturate
the observable invariant, retire it cheaply.

### A10. Off-diagonal collision ideal / injectivity route

**Essence:** prove the saturated ideal of two distinct points with equal image is
empty.

**Campaign:** partial only. Resultants and eliminants appear throughout, e.g.
`lib/reduce*.py`, `SHEET6-R1.md`, `SOL-ALGEBRAIZATION.md`, but the saturated
collision ideal has not been attacked directly.

**Obstruction:** collision components can close only at infinity; direct
elimination doubles variables and explodes. Injectivity is essentially the full
conjecture.

**Cheapest untried experiment — 6/10:** on `open_8_28_c2`, exploit linearity in
Q-coefficients and compute generic Fitting consistency ideals chart by chart.

### A11. Locally nilpotent derivations and commuting flows

**Essence:** show the Hamiltonian derivation with slice D_P(Q)=1 is locally
nilpotent, or that both dual flows are complete polynomial G_a-actions.

**Campaign:** not directly. `TRANSPORT.md` uses LNDs locally, but no global
completeness attack exists. `xmodel/sol-lateral3.md` records the direct
boundary witness proving LND failure at finite-g punctures.

**Obstruction:** a derivation with a slice need not be locally nilpotent; LND
would immediately imply the conjecture. Completeness encodes properness.

**Promise as standalone proof route: low.** The useful variant is not to prove
LND but to classify pole divisors obstructing completeness.

### A12. Affine-surface classification, Makar–Limanov, cancellation

**Essence:** derive a contradiction from the affine-surface invariants of the
hypothetical source/target/graph.

**Campaign:** not as a JC2 program.

**Obstruction:** standard ML/cancellation invariants do not see the embedding or
the Keller presentation; stabilizing usually destroys the object.

**Cheapest untried probe — 4/10:** compute the ML invariant of the residue-A
leading graded ring. It is cheap, but likely only a sanity check.

### A13. Integrality, Rees valuations, and étale finiteness

**Essence:** prove x,y integral over C[P,Q], then invoke triviality of finite
étale covers of A².

**Campaign:** not attempted directly. A multi-Rees/b-divisor reformulation is
proposed in `xmodel/sol-ideas-0821.md` but not executed.

**Obstruction:** finiteness is precisely the missing global assertion; ZMT adds
a boundary instead of removing it.

**Cheapest untried experiment — 6/10:** compute Rees valuations of
C[P,Q]⊂C[x,y] for one complete boundary book and test integral dependence
directly.

## B. Topology, surfaces, covers, and monodromy

### B1. Links/splice diagrams and plumbing at infinity

**Essence:** encode resolved fibers as links and exclude impossible splice
diagrams.

**Campaign:** yes on residue-A templates. `SHEET6-CLASSICAL.md`.

**Obstruction:** topological admissibility does not imply algebraic
realizability; multiplace/moduli-rich survivors remain.

### B2. Log-surface inequalities and BMY

**Essence:** use log Chern/adjunction inequalities on a resolved pencil.

**Campaign:** partial. Classical ledgers pass identically; BMY is marked
needs-data in `SHEET6-CLASSICAL.md` because resolution tails are unpinned.

**Obstruction:** without complete normal-crossings tails and discrepancies, the
numerical inequality has no input. Naive BMY fails because κ̄(C²)=−∞.

**Cheapest untried experiment — 6/10:** complete one smallest survivor to all
minimal tails and compute log Chern pairs for each completion.

### B3. Fiber monodromy, Hurwitz passports, dessins

**Essence:** constrain the td-sheeted cover using branch-cycle factorizations.

**Campaign:** yes for single-cover residue-A passports. `GROK-MONODROMY.md`
finds all 169 passports admissible.

**Obstruction:** Riemann existence is too generous, and one-coordinate passports
ignore coupling with the second fibration and Jacobian contacts.

**Cheapest untried extension — 7/10:** build a coupled branch-cycle CSP encoding
both coordinate fibrations, infinity contacts, and Jacobian pairing.

### B4. Primitive monodromy group bound on td

**Essence:** use primitivity/classification of transitive subgroups of S_td to
bound td or force a block system.

**Campaign:** not executed. Proposed in `xmodel/sol-lateral3.md`; adjacent to
the passport audit above.

**Obstruction:** A_td/S_td are primitive at every td, and geometric inertia may
be too generous. Even a forced block needs a hard descent theorem back to a
polynomial Keller map.

**Cheapest untried experiment — 7/10:** enumerate inertia types for td=6..9
against primitive-group databases, using the known Orevkov td=9 configuration
as a negative control before attempting block descent.

### B5. Graph compactification and Picard/torsion obstruction

**Essence:** study the closure of the graph X⊂P²×P² and its discriminant class
in Pic(X); force torsion/order constraints incompatible with large td.

**Campaign:** no. This framing appears only in `xmodel/grok-lateral1.md` and has
not been run.

**Obstruction:** the class may depend heavily on compactification, and toric
shadows may miss the actual exceptional configuration.

**Cheapest untried experiment — 8/10:** compute Picard lattices and
nonproperness/discriminant classes for three tame automorphism controls, then
for the residue-A leading-form toric shadow.

### B6. Du Val/deleted-centers residual pencil and Δ²≥−2

**Essence:** delete proportional edge-power centers; identify the residual pencil
singularities as ADE and obtain Δ²≥−2, yielding a td ceiling.

**Campaign:** not executed. `TDBOUND.md` contains related mass experiments, and
`xmodel/grok-lateral2.md` proposes the Du Val interpretation.

**Obstruction:** support on an ADE lattice is insufficient; one must prove the
relevant class is an actual root/integral class and that deleted centers really
are proportional.

**Cheapest untried experiment — 7/10:** compute residual intersection matrices
for residue-A and two tame controls; check whether Δ² lies in {0,−2} and whether
the configuration is ADE.

### B7. Euler-characteristic identity for the complement cover

**Essence:** from F⁻¹(U)→U finite étale over U=A²∖A(F), derive
1−χ_c(preimage S)=td(1−χ_c(S)).

**Campaign:** no. Proposed as a "new global lane" in `xmodel/sol-avenues3.md`;
not implemented.

**Obstruction:** the identity is exact but leverage requires computing χ_c of
the unknown nonproperness curve and all exceptional preimages.

**Cheapest untried experiment — 7/10:** instantiate the identity for one fully
enumerated B/x component menu, including intersections, and test divisibility/
sign constraints.

## C. Algebraic reformulations and stronger conjectures

### C1. Dixmier conjecture DC(2)

**Essence:** prove every endomorphism of A₂ is surjective; DC(2)⇒JC2.

**Campaign:** bounded slices tried. `DC2-PROGRAM.md`: degree ≤2 holds, degree-3
reveals quantum/classical divergence, degree-4 parked.

**Obstruction:** no Schur normal form in A₂; centralizers are unclassified; the
statement is strictly harder than JC2.

**Cheapest untried refinement — 5/10:** decompose first quantum corrections into
Sp₄ irreducibles before further brute force.

### C2. End(A₁) disproof / Zheglov audit

**Essence:** find a non-surjective endomorphism of A₁, or expose a fatal gap in
a claimed DC(1) proof.

**Campaign:** partial defensive audit. `ZHEGLOV-SCOPE.md`,
`ZHEGLOV-LTEST.md`.

**Obstruction:** no candidate exists; even refuting a paper yields no JC2
counterexample.

**Cheapest remaining task — 3/10:** symbolic replay of the flagged T2 steps.
Worth only as provenance hygiene.

### C3. Spectral surfaces / commuting PDOs

**Essence:** import Burchnall–Chaundy/spectral theory into two variables and run
DC(2) there.

**Campaign:** no.

**Obstruction:** the needed two-dimensional spectral dictionary is itself an
open research program.

**Cheapest viability test — 3/10:** classify rank-one commutative subalgebras
for the simplest quantized plane pair and check whether any invariant survives
classical specialization.

### C4. D-module/holonomic index

**Essence:** attach a holonomic index or characteristic-cycle invariant to a
Keller endomorphism and prove preservation forces invertibility.

**Campaign:** no concrete invariant named anywhere in the repo.

**Obstruction:** index preservation is too coarse; the actual challenge is
constructing a finite invariant sensitive to nonproperness.

**Cheapest first experiment — 4/10:** compute characteristic cycles for the
graph/direct-image D-module of several polynomial maps, starting with tame
automorphisms versus known rational nonproper maps, and look for a determinant-
sensitive term.

### C5. Mathieu/Zhao/image-conjecture ladder

**Essence:** prove a stronger analytic/moment statement implying JC.

**Campaign:** partially explored and now largely dead. `MATHIEU.md`,
`FACE-ISOLATION.md`; broader status recorded in `APPROACHES.md`.

**Obstruction:** unrestricted higher-dimensional versions are refuted; the plane
identity gives one bilinear condition, not an infinite moment tower.

### C6. Lee–Li Conjecture E / Magnus remainder vanishing

**Essence:** prove uniform remainder vanishing in the formal-inverse expansion;
E⇒JC2 via the stated ladder.

**Campaign:** small instances tried. `conjectureE-plan.md`, `lib/conjE.py`,
tests.

**Obstruction:** no finite reduction or uniform truncation bound; the theorem is
the universal quantifier.

**Cheapest untried extension — 6/10:** mine short sparse cofactor identities
from the next parameter tuple and search for a recurrence matching existing
two-row certificates.

### C7. HC4⇒JC2 and the degree-five Hessian module

**Essence:** if h=y₁P+y₂Q always satisfies det Hess h=(det J)², proving HC4 in
constant-determinant form proves JC2; attack degree five.

**Campaign:** initially untried, then adjudicated on 2026-08-21.
`xmodel/hc4-adjudication.md` verifies the bridge and defines a finite quintic
obstruction-module experiment; `notes.md` records the adjudication.

**Obstruction:** degree ≥5 layers can cancel; the full quintic case tree is
paper-scale. Quintic success alone would only reprove classical low-degree JC2
unless the mechanism extends uniformly in degree.

**Next concrete experiment — 7/10:** implement the adjudication's HC4-Q5 spec:
quartic replay, cone-normalized quintic layer module, GL₄ decomposition, y-linear
sector control, and Meng–Yang Schur-descent kill-probe.

### C8. Bass–Connell–Wright/Yagzhev cubic stabilization

**Essence:** reduce higher-dimensional Keller maps to cubic/Drużkowski form and
prove that class invertible.

**Campaign:** not viable as stated; reconnaissance only in `RECON.md`.

**Obstruction:** unrestricted target classes contain known higher-dimensional
counterexamples; plane-origin subclass lacks recognizing invariants.

**Cheapest salvage probe — 4/10:** compute stable invariants separating BCW
images of plane maps from the known dim-3 counterexample.

### C9. Graded/equivariant/GIT reduction

**Essence:** degenerate to weighted-homogeneous Keller maps and use symmetry.

**Campaign:** partial normalization/template work only; graded CE hunt is closed.
`TEMPLATE-ATTACK.md`, `RECON.md`.

**Obstruction:** graded plane Keller maps are already automorphic, while orbit
limits lose nonproperness or change the property under study.

**Cheapest probe — 4/10:** compute stabilizers/orbit limits on a live coefficient
variety and test preservation of collision/nonproper branches.

### C10. Free associative lift

**Essence:** lift commutative words to free variables, use free Jacobian
invertibility, abelianize.

**Campaign:** no.

**Obstruction:** commutative det=1 does not imply free matrix invertibility;
finding commutator corrections is the whole problem.

**Cheapest negative control — 2/10:** attempt degree-by-degree free corrections
on the smallest unresolved support; expected immediate failure.

## D. Arithmetic, analytic, and dynamical routes

### D1. Positive characteristic collisions and Witt lifting

**Essence:** find separable char-p Keller collisions and lift through Witt towers
to characteristic zero.

**Campaign:** yes. `MONDELLO-CHECK.md`, Witt/Bockstein work summarized in
`AUDIT.md`; searched stratum is totally W₂-obstructed.

**Obstruction:** even one W₂-survivor would require compatible lifts through all
Witt levels and a fixed-support limit.

**Cheapest untried extension — 6/10:** search low-support F₃/F₅ collisions and
compute first Witt obstructions immediately.

### D2. p-adic injectivity/Hensel/model-theoretic transfer

**Essence:** prove uniform p-adic bijectivity for almost all p and transfer to
characteristic zero.

**Campaign:** tools used locally; global implication untested. See
`SHEET6-DIRECTIONB.md` and Hensel discussions.

**Obstruction:** transfer requires a uniform degree/support bound—the same
missing compactness.

**Cheapest untried experiment — 4/10:** Hensel-lift certified smooth F_{p²}
points on a D25 component until the first compatibility equation fails.

### D3. Diophantine integral points/thinness

**Essence:** use Siegel/height/Hilbert irreducibility to force properness or
finitely many sheets.

**Campaign:** no.

**Obstruction:** finiteness theorems classify wrong-direction behavior; uniformity
over an unknown pencil is inaccessible.

**Cheapest probe — 3/10:** on one surviving formal fiber model, compute genus,
punctures, and effective S-unit conditions.

### D4. Analytic metric completeness/Hadamard

**Essence:** prove pullback metric completeness, hence covering/injectivity.

**Campaign:** no direct attempt.

**Obstruction:** constant determinant controls volume, not minimum singular
value; holomorphic analog is false and higher-dimensional counterexamples exist.

**Cheapest probe — 4/10:** compute asymptotic singular values along a live
formal branch and test finite-versus-infinite pullback length.

### D5. Real JC/Pinchuk deformation

**Essence:** deform Pinchuk-type real maps to constant Jacobian or use real
global-injectivity theory.

**Campaign:** no.

**Obstruction:** Pinchuk examples have nonconstant Jacobian; complex collisions
need no real locus; SOS/CAD is orthogonal to complex emptiness.

**Cheapest probe — 3/10:** solve bounded-degree perturbations of one Pinchuk map
for constant-Jacobian reality; expected only to document the obstruction.

### D6. Descent of dimension ≥3 counterexamples

**Essence:** restrict/quotient/project a known higher-dimensional Keller
counterexample to a plane Keller counterexample.

**Campaign:** recon and negative controls only; no systematic descent. Related
LND-descent idea proposed in `xmodel/sol-lateral.md`.

**Obstruction:** constant 3×3 determinant does not induce a constant 2×2 minor;
natural quotients acquire extra factors and destroy étaleness.

**Cheapest concrete experiment — 6/10:** enumerate low-degree triangular target
LNDs on the explicit 3D example, impose D⁸=0 on lifted generators, and solve
exactly. This specific experiment is written in `xmodel/sol-lateral.md` but not
run.

### D7. Rational étale maps and two-dimensional pole removal

**Essence:** start with a rational noninjective étale plane map and cancel poles
by birational operations.

**Campaign:** no.

**Obstruction:** clearing poles changes the Jacobian or creates base points;
there is no spare dimension to absorb denominators.

**Cheapest experiment — 6/10:** classify one-pole rational constant-Jacobian
maps up to triangular birational equivalence and solve polynomial-output
divisibility equations.

### D8. Tropical coefficient ideals

**Essence:** tropicalize the saturated coefficient ideal, not merely P,Q, and
find inconsistent initial degenerations.

**Campaign:** no direct tropical computation.

**Obstruction:** tropical prevariety overapproximates and loses saturation/chart
data.

**Cheapest experiment — 5/10:** tropicalize one unresolved 12–27-variable
saturated chart retaining saturation variables and test lifting of every cone.

### D9. Cohomology/K-theory/motivic/A¹-degree cluster

**Essence:** find a cohomological, K-theoretic, motivic, or enriched-degree
obstruction to nonproper étale self-cover.

**Campaign:** no executed invariant computation; a local A¹-degree proposal
appears in `xmodel/sol-lateral.md`.

**Obstruction:** no named class/vanishing theorem sees J=1; ordinary local degree
is +1 everywhere.

**Cheapest experiment — 5/10:** compute Scheja–Storch/EKL forms at infinity for
tame controls and one truncated residue-A place, checking for discriminant/Hasse
constraints absent from integer counts.

### D10. Markus–Yamabe/vector-field realization

**Essence:** reinterpret Keller pairs as polynomial vector fields satisfying
spectral stability hypotheses.

**Campaign:** no.

**Obstruction:** constant Jacobian does not imply Hurwitz spectral condition; the
arrow is generally wrong.

**Score: 2/10.**

## E. Computational proof/disproof engines

### E1. Direct Gröbner/F4 saturation and Nullstellensatz certificates

**Essence:** fix supports, impose Keller equations, split charts, certify empty
or extract a point.

**Campaign:** yes, at scale. `lib/reduce*.py`, `lib/chartelim.py`, `AUDIT.md`,
`CERT-UPGRADE.md`, `CROSSCHECK.md`.

**Obstruction:** exponential growth, false chart deaths, modular-to-characteristic
lifting walls, and no census completeness.

### E2. Certificate mining across the farm

**Essence:** recover sparse Nullstellensatz identities from many EMPTY cases,
anti-unify supports, interpolate a parametric theorem.

**Campaign:** no. Fully specified in `xmodel/sol-lateral.md`; not run.

**Obstruction:** certificate extraction may be unavailable or huge, and motifs
may be emitter artifacts.

**Cheapest experiment — 8/10:** extract/minimize degree ≤6 cofactors on twelve
clean EMPTY systems; train on eight, hold out four, include NONEMPTY controls.

### E3. Sparse SOS/Positivstellensatz certificates

**Essence:** realify complex coefficient systems and seek exact rational SOS
witnesses of −1.

**Campaign:** no. Proposal in `xmodel/sol-lateral.md`.

**Obstruction:** SDP degrees may explode; numerical feasibility is worthless
without exact rational reconstruction.

**Cheapest experiment — 6/10:** validate chordal degree-2/4 certificate search
on one tiny EMPTY and one NONEMPTY control.

### E4. Homotopy continuation from a solvable degeneration

**Essence:** deform ctl0 to residual32, track singular arcs, reconstruct exact
endpoints.

**Campaign:** no. Specific guard-to-main Rees deformation proposed in
`xmodel/sol-lateral.md`.

**Obstruction:** highly singular endpoints, path loss, and exact reconstruction.

**Cheapest experiment — 7/10:** emit weighted initial systems for d≤12, solve
modular starts, and track a small isolated subset with exact endpoint checks.

### E5. Finite-state/normal-form compilers for books

**Essence:** quotient infinite neutral histories to a finite Markov state space.

**Campaign:** yes, with failures and scoped successes. `NF-Z.md`, `NF-P.md`,
`NF-M.md`, `NF-D.md`.

**Obstruction:** coarse quotients merge states with different futures; exact fat
states remain infinite.

### E6. Contextual live-kernel quotient

**Essence:** quotient histories relative to a fixed consumer/context, allowing
finiteness even when absolute histories differ.

**Campaign:** proposed only. `xmodel/sol-lateral3.md`.

**Obstruction:** backward preimage closure may fail, or an infinite fooling set
may exist within one context.

**Cheapest experiment — 6/10:** compute backward residuals for td-11 pure-neutral
contexts and test whether all co-scaled tuples absorb before deep history.

### E7. First-disagreement rigidity for multiple neutral words

**Essence:** prove a well-founded mismatch measure kills jointly live multiword
histories.

**Campaign:** proposed only. `xmodel/sol-lateral3.md`.

**Obstruction:** ordered cap changes can distinguish otherwise identical products;
unbounded mismatch skeletons may survive.

**Cheapest experiment — 5/10:** enumerate depth ≤6 legal word pairs in td-11/13
windows and search for a decreasing divisor measure.

### E8. Hall-deficiency/flow dual of tower obstructions

**Essence:** model later repair slots as capacities and prove every realizable
tower induces a matching; Hall deficiency becomes a reusable kill.

**Campaign:** proposed only. `xmodel/sol-lateral.md`.

**Obstruction:** the bridge from legal tower routes to the claimed flow must be
proved; otherwise min-cut is decoration.

**Cheapest experiment — 7/10:** instrument td-7 traces into demand/repair graphs
and search for parameterized deficient subsets explaining multiple deaths.

### E9. Forbidden minors/WQO compilation of tree records

**Essence:** define sound contractions under which death is hereditary; finish by
Higman/Dickson or a finite forbidden-minor basis.

**Campaign:** proposed only. `xmodel/grok-lateral2.md`; nearest failed NF-Z
program is distinct.

**Obstruction:** register-only minors may become live, and event alphabets may
require unbounded additions.

**Cheapest experiment — 6/10:** test proposed contractions against all td-7 dead
routes and td-11 open rows; one false reduction retires the embedding.

### E10. Compactification of transition state space

**Essence:** invert unbounded registers (e.g. T=1/ν) and compactify the off-axis
transition scheme; finite integral points become the book.

**Campaign:** proposed only. `xmodel/grok-lateral1.md`.

**Obstruction:** some transition may remain indeterminate at T=0 or require new
unnamed blowups.

**Cheapest experiment — 7/10:** rewrite FC5 transitions in T=1/ν coordinates and
tabulate regular/pole/base-point behavior at T=0 for all priced families.

### E11. Edge-power comb/fan transport functor

**Essence:** convert GGV edge powers into a finite predicted Eggers–Wall comb or
toric fan with pole bits.

**Campaign:** proposed only. `xmodel/grok-lateral2.md`; nearest neighbors are
Newton-cut proposals, but this avoids jets.

**Obstruction:** root-sharing pattern may be insufficient to determine labeled
pole trees; fan may be too coarse.

**Cheapest experiment — 7/10:** generate abstract combs for four gate-B chains
and validate pole predictions on tame automorphisms and the residue-A shadow.

### E12. SL₂ pushforward of admissible chains

**Essence:** rectangularizing linear changes act on valuation directions;
push the GGV walk forward and read the Sigray type.

**Campaign:** normalization transport is proved, but this directional-chain
dictionary is not. See `TRANSPORT.md`, `xmodel/grok-lateral1.md`.

**Obstruction:** different admissible matrices may yield inequivalent types, and
target mixing may contaminate source valuation data.

**Cheapest experiment — 7/10:** enumerate rectangularizing matrices for four
gate-B chains and compare pushed types on automorphism controls.

### E13. GGV intersection numbers as Sigray masses

**Essence:** identify approximate-root intersection numbers with Λ_i, making
entry menus computed rather than independently assumed.

**Campaign:** no. Proposed in `xmodel/grok-lateral1.md`; GGV6 theorem unused.

**Obstruction:** the pairings may be between wrong objects or omit ν-denominators.

**Cheapest experiment — 6/10:** tabulate permitted pairings for four chains and
compare termwise with T7 entry arithmetic.

### E14. Greenberg function/finite-depth jet decision

**Essence:** find a finite D* such that V_{D*}=∅ iff the formal jet scheme is
empty.

**Campaign:** adjacent depth-stabilization attempts exist, but the Greenberg
formulation is unrun. `DEPTH-STAB.md`, `xmodel/grok-lateral2.md`.

**Obstruction:** the ambient ring may change with depth, or the image may shrink
forever; Greenberg bounds can be enormous.

**Cheapest experiment — 7/10:** eliminate D23 deep-tail variables onto CORE2 and
test whether J_D stabilizes in a fixed Noetherian ambient.

### E15. Ascending-window ideal in a fixed CORE2 ring

**Essence:** project each depth's ideal back to the original variable set and
detect stabilization or finite-depth emptiness.

**Campaign:** proposed specifically in `xmodel/grok-lateral2.md`; D23 core exists
but this projection experiment is not banked.

**Obstruction:** conditions may live fiberwise, requiring enlarged moduli; the
inverse system may be non-Noetherian in practice.

**Cheapest experiment — 8/10:** eliminate the ten Row_22 deep variables from the
existing D23-core modulo one good prime, replay dead samples, and compare with
J_21.

### E16. Toric circuit closure of relaxed monomial systems

**Essence:** add quadratic binomial relations among falsely independent tail
monomials; inconsistency proves emptiness.

**Campaign:** no. Fully specified in `xmodel/sol-avenues2.md`.

**Obstruction:** partial circuits may add zero codimension; SAT points may be
spurious unless reconstructed in original coordinates.

**Cheapest experiment — 7/10:** hash Row-20 exponent-vector pair sums, select
circuits touching six obstruction characters, and screen at three primes.

### E17. Fitting/left-kernel compression

**Essence:** treat high tails linearly, compute polynomial compatibility modules
chartwise, and avoid eliminating them.

**Campaign:** pointwise ranks observed; polynomial compression not materialized.
See `xmodel/sol-accel2.md`.

**Obstruction:** minors may be dense/irreducible and rank-drop strata as hard as
the original.

**Cheapest experiment — 8/10:** fence one certified rank-16 minor, emit adjugate
compatibility rows, and compare term mass with raw hard-pin input.

### E18. High-tail kernel as gauge action

**Essence:** determine whether the apparent nullspace of the high-tail linear
block integrates to harmless reparametrization gauge.

**Campaign:** candidate nullspace observed; integration test not performed.
`xmodel/sol-accel2.md`.

**Obstruction:** exact characteristic-zero kernel may vanish, or may fail to
preserve factorization/no-log/saturation constraints.

**Cheapest experiment — 7/10:** lift the candidate kernel over the radical
algebra and compare with infinitesimal t→t+εt^r substitutions.

### E19. Tau-paired fence-power identities

**Essence:** prove z^N∈I on a fenced leaf with tiny row subsets, yielding 1
after multiplying by u^N.

**Campaign:** no bounded sidecar implemented. Proposal in
`xmodel/sol-accel2.md`.

**Obstruction:** required N/support may exceed the pilot bounds.

**Cheapest experiment — 6/10:** rediscover known singleton C6/C8 certificates,
then search N≤3, row subsets ≤4, multiplier degree ≤3 at two primes.

### E20. Character-blocked F4 and invariant-only certificates

**Essence:** decompose Macaulay matrices by finite group characters or search
only the trivial-isotypic Nullstellensatz block.

**Campaign:** no backend implementation. Analysis in
`xmodel/sol-ideas-0821.md`.

**Obstruction:** character spaces multiply rather than form ideals; speedup is
conjectural and engine-specific.

**Cheapest experiment — 6/10:** prototype bucketed character blocks on one
mid-sized union Macaulay matrix and measure memory/time.

### E21. Schur–Laurent triangular certificates

**Essence:** exploit unit minors to pivot Laurent-linear blocks and emit
reversible reconstruction DAGs.

**Campaign:** yes at D25, promoted modularly. `AUDIT.md` D25 entry,
`xmodel/sol-ideas-0821.md`, `cases/d25_certificate_replay.json`.

**Obstruction:** works only when such unit pivots exist; still chart/fiber-local
and not a characteristic-zero proof by itself.

### E22. Weighted degeneration/initial-ideal certificates

**Essence:** find a weight vector whose initial monomial ideal has controlled
dimension, giving an upper-bound certificate.

**Campaign:** not automated. Conjectural proposal in
`xmodel/sol-ideas-0821.md`.

**Obstruction:** ILP search may find no useful weight, and inclusion gives only
one-sided information unless paired with a lower-bound witness.

**Cheapest experiment — 5/10:** search weights among derived pivot supports on
D25-like compressed systems.

### E23. Hilbert-series truncation/border basis checker

**Essence:** prove a Hilbert-function plateau exact via regularity/border
closures.

**Campaign:** plateau observations exist; certified method not implemented.

**Obstruction:** plateau alone proves nothing without regularity or border
closure.

**Cheapest experiment — 5/10:** homogenize a small compressed quotient and test
border-basis closure against the known terminal algebra.

### E24. Guided sparse/SAT/ML counterexample search

**Essence:** impose J=1 plus an explicit collision on structured sparse supports,
then reconstruct and verify exactly.

**Campaign:** structured reduced systems yes; broad guided search no.
`lib/fastcoef.py`, `lib/linprobe.py`, `lib/planeprobe.py`; discussion in
`APPROACHES.md`.

**Obstruction:** counterexamples are a very thin locus; dense searches explode;
bounded misses prove nothing.

**Cheapest worthwhile version — 6/10:** choose the smallest μ=6 two-pole support
with explicit collision, quotient symmetries, inspect treewidth, and run block
elimination.

### E25. Finite-field census of Keller maps

**Essence:** count/enumerate finite-field Keller maps and look for lift-worthy
extras.

**Campaign:** diagnostics only, not census.

**Obstruction:** char-p extras often have Frobenius/Witt obstructions and die
past tiny degree.

**Score: 2/10.**

### E26. Lean/formal certification as a discovery engine

**Essence:** formally verify generators, reductions, and leaves—or use proof
search to discover missing lemmas.

**Campaign:** leaf/identity layer only. `README.md` mentions Lean-checked
example; `xmodel/grok-vertexgap-fidelity.md` reviews fidelity.

**Obstruction:** formalization cannot create the missing finite universe or
landing theorem.

**Best next formal target — 5/10:** formalize one bracket derivation plus one
chart-split preservation theorem, not another endpoint identity.

### E27. Moskowicz prime-td claim triage

**Essence:** test/adapt an unvetted claim excluding prime topological degree.

**Campaign:** flagged only.

**Obstruction:** claim strength exceeds its length/publication status, and prime
td=3 exists in char 2.

**Score: 2/10**, but testing the first substantive lemma against td=9 controls
is cheap.

### E28. Differential Galois/Liouvillian inverse analysis

**Essence:** analyze inverse differential equations by Kovacic/Galois methods.

**Campaign:** no.

**Obstruction:** inverse PDE is tautological; univariate reductions reproduce
known Żołądek rigidity.

**Score: 3/10.**

### E29. Ritt decomposition/composite coordinates

**Essence:** force one coordinate composite and reduce.

**Campaign:** no.

**Obstruction:** degree divisibility/coarse primality and automorphism reduction
already collapse most cases.

**Score: 3/10.**

### E30. Lagrangian generating functions/Hamilton–Jacobi charts

**Essence:** represent inverse branches through generating functions and impose
polynomiality.

**Campaign:** no.

**Obstruction:** charts are local and mixed-coordinate; global gluing recovers
the nonproperness problem.

**Score: 4/10.**

## F. Novel routes I can articulate that are not clearly in the repo

These are speculative and lower confidence than the above, but distinct enough
to record.

### F1. Twisted arc space and Cambrian/cluster valuation fans

**Essence:** replace ordinary Puiseux depth with a fan of clustered valuations
adapted to simultaneous P,Q roots, hoping cancellations become monomial in the
cluster coordinates.

**Campaign:** no direct match; nearest objects are toric circuits and fan
transport.

**Obstruction:** cluster mutation may not respect the Jacobian relation, and the
fan may proliferate like arbitrary resolution trees.

**Cheapest experiment — 4/10:** on one two-root residue-A seed, mutate the
cluster at each root and check whether the first ten Jacobian coefficients
become support-preserving monomial maps.

### F2. Nonarchimedean maximum principle for analytic continuation sheets

**Essence:** interpret escaping Keller sheets as a nonarchimedean maximum/minimum
principle on a Berkovich skeleton and derive an impossible boundary extremum.

**Campaign:** no direct match; p-adic escape-mass and valuative trees are only
adjacent.

**Obstruction:** the skeleton depends on unknown compactification, and the
maximum principle may simply encode td counting.

**Cheapest experiment — 4/10:** build the Berkovich skeleton for a rational
étale nonproper control and test whether the boundary functional distinguishes
td=2 from td=3.

### F3. Persistent homology of coefficient solution strata across depth

**Essence:** track birth/death of modular solution components across D21→D23→D25
and predict the next cut from persistence barcodes rather than symbolic
elimination.

**Campaign:** no; D43 provides the right data but not this representation.

**Obstruction:** finite-field sampling can miss high-codimension cuts, and
barcodes are not proofs.

**Cheapest experiment — 5/10:** sample the existing 36-fiber atlas at D21/D23
and compute persistent Betti snapshots as a guide to where symbolic compat rows
will bite.

### F4. Interpolation of the Jacobian as a section of a canonical extension

**Essence:** view dP∧dQ as a nowhere-vanishing section of K_{A²}; extend it to a
log canonical bundle on a chosen compactification and classify possible zero/pole
bundles directly.

**Campaign:** adjacent residue/log work, but no bundle-section classification.

**Obstruction:** the compactification and extension are unknown; the section may
extend noncanonically.

**Cheapest experiment — 5/10:** for tame maps, compute all natural extensions of
dP∧dQ on a minimal log resolution and identify which extension is
automorphism-invariant.

### F5. Galois descent on coefficient fields to force rational impossibility

**Essence:** if the only formal survivors lie over forced number fields, prove
their Galois conjugates cannot be glued to a rational polynomial pair.

**Campaign:** coefficient conjugates and selector torsors are studied, but this
specific global descent criterion is not formulated as a solver gate.

**Obstruction:** survivors may be defined over Q already, or conjugate glueing
may be automatic.

**Cheapest experiment — 5/10:** replay the D25 terminal certificate over Q(√3)
and test whether conjugate swaps force any coefficient antisymmetry incompatible
with rational reconstruction.

## Comparative ranking of untried next moves

Highest value per cost:

1. E15/E14 fixed-ring depth projection — directly attacks the live formal-germ
   wall using existing D23 data. Score 8.
2. A9/A8 global symplectic primitive and adjoint pairings — cheap controls,
   potentially a genuinely global obstruction. Score 7–8.
3. B5 graph Picard/torsion — new invariant aimed at the td ceiling. Score 8.
4. E17 Fitting compression — converts an existing observed rank drop into a
   smaller symbolic object. Score 8.
5. E2 farm certificate mining — turns thousands of past solves into theorem
   candidates. Score 8.
6. B3/B4 coupled and primitive monodromy CSP — attacks the second missing
   global bridge. Score 7.
7. C7 HC4 quintic module — now mathematically validated as an implication, with
   a finite first experiment. Score 7.
8. B6/B7 surface/Euler global identities — promising if one complete tail set
   can be produced. Score 6–7.

Bad or deprioritized despite superficial appeal:

- Naive deformation to linear part: falsified by higher-dimensional
  counterexamples.
- Free-associative lift: assumes a strictly stronger invertibility condition.
- Generic ML/random dense search: thin locus plus exact verification makes
  information yield negligible.
- Real SOS as a proof of complex emptiness without exact rational certificates:
  numerically seductive, logically fragile.
- “Prove a stronger n-variable statement” except HC4: mostly refuted terrain.

## Coverage note

This file lists 75 numbered entries: 70 main-line routes A1–E30, plus five
additional novel candidates F1–F5; some broad clusters are intentionally
subdivided when the missing theorem differs materially. The aim is coverage of
mechanisms, not exhaustive enumeration of tactics inside an already filed book.
