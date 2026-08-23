# Independent survey: top-level approaches to JC2

Surveyor: Grok 4.6. Date: 2026-08-21. Repo: `/Users/dc/code/math/jc72108`.
Write-scope: this file only.

**Charge.** List the landscape of ways a well-read researcher *or a creative outsider* might try to prove or disprove the plane Jacobian Conjecture, independently of the campaign’s current framing. Completeness over depth. Bad approaches included, and named as such. Fashionable answers treated as suspects.

**Scoring.** Promise scores (1–10) appear **only for approaches the campaign has not tried**. The score is P(this lane produces a checkable proof of JC2 **or** an explicit characteristic-zero polynomial counterexample, pursued at serious intensity for a few years) — not “interesting mathematics,” not “fits the current book,” not “sounds modern.” 1 is noise. 10 would be a missing lemma that already almost exists.

**Tried** means the campaign ran a real computation, proof, or audit against that approach and left files. A literature note in `RECON.md` is not a try. A one-paragraph “we could also…” in an xmodel memo is not a try.

**The one campaign fact that must color every local-at-infinity entry.** `REDUCTION.md` is the honest dependency audit: there is **no theorem** sending an arbitrary planar Keller counterexample into a currently enumerated sheet-book, and **no proved upper bound on topological degree**. Any approach that only kills `td ≤ 14` configurations, or only the residue-A chart, is not a JC2 program. It is a necessary-condition mill. The campaign knows this on paper and then proceeds as if the mill were the theorem. That is the central self-deception to refuse.

---

## Index

| # | Approach | Side | Campaign | Promise if untried |
|---:|---|---|---|---|
| 1 | GGV Newton-polygon / degree-bound farm | both | tried | — |
| 2 | Sheet-number / Eggers–Wall / Newton–Puiseux at infinity | proof | tried | — |
| 3 | Vertex-gap / strip ODEs / residue \(R_{k,d_2}\) | proof | tried | — |
| 4 | Coefficient-level Puiseux windows (residue-A and kin) | both | tried | — |
| 5 | Jung–van der Kulk degree-lowering of Keller maps | proof | not | 5 |
| 6 | Abhyankar–Moh embeddings / one-place semigroups | proof | tried (wrong object) | — |
| 7 | Properness / Jelonek asymptotic variety \(A(F)\) | proof | tried (shadow only) | — |
| 8 | Formal inverse is polynomial | proof | not | 4 |
| 9 | Dixmier DC(2) | proof | tried (slices) | — |
| 10 | Dixmier DC(1) as *disproof* of JC2 | disproof | tried (T1 only) | — |
| 11 | Mathieu conjecture | proof | dead; DvdK used | — |
| 12 | Poisson PC(2) / GMC / Hessian / Zhao cousins | proof | dead / ported | — |
| 13 | Lee–Li Conjecture E / Magnus remainder vanishing | proof | tried (tiny) | — |
| 14 | BCW / Yagzhev / Drużkowski cubic reduction | proof | not | 1 |
| 15 | Graded / equivariant / weighted Keller maps | both | noted, not owned | — |
| 16 | Descent of dim-\(\ge 3\) counterexample mechanisms | disproof | recon only | 2 |
| 17 | Characteristic \(p\), separable JC, Witt lifts | both | tried | — |
| 18 | Random / SAT / fewnomial search for a pair | disproof | not | 2 |
| 19 | Dessins, Hurwitz, monodromy of \(\hat g\) | proof | tried (one template) | — |
| 20 | Face isolation / \(p\)-adic multinomials | proof | analysis only | — |
| 21 | Compactification, BMY, log Kodaira of the pencil | proof | tried (needs tails) | — |
| 22 | Affine surface classification / LNDs / ML invariant | proof | not (as JC2) | 4 |
| 23 | Étale topology, primitive monodromy, \(td\) from groups | proof | not (as global bound) | 5 |
| 24 | Algebraization of a formal germ at infinity | disproof | tried (Padé + depth) | — |
| 25 | Collision ideals / “hidden inertia” | proof | not | 2 |
| 26 | Spectral surfaces / commuting PDOs in two variables | proof | not | 3 |
| 27 | Symplectic exactness / action residues as a *global* lemma | proof | pins used, lemma not | 6 |
| 28 | Bézout / BKK / mass inequalities as a \(td\) ceiling | proof | tried (conjecture) | — |
| 29 | Pinchuk maps / real JC as a complexification obstruction | both | not | 3 |
| 30 | Ritt decomposition / composite coordinates | proof | not | 3 |
| 31 | Finite-field census of Keller maps | both | not | 2 |
| 32 | Markus–Yamabe / chain-realization vector fields | both | not | 2 |
| 33 | Tropical geometry *beyond* Newton polygons | both | not | 2 |
| 34 | Hodge, K-theory, anabelian, derived/prismatic | proof | not | 1 |
| 35 | Lean / AI “proofs” with unproved axioms | proof | not | 1 |
| 36 | Holomorphic JC / Fatou–Bieberbach / univalent fns | — | analog is false | 1 |
| 37 | Moskowicz “no prime \(td\)” | proof | not | 2 |
| 38 | Differential Galois / Liouvillian inverse | proof | not | 3 |
| 39 | Height / Arakelov / small-coefficient search | disproof | not | 2 |
| 40 | Lagrangian generating functions / 2D Hamilton–Jacobi | proof | not | 3 |

Forty is not a complete list of *tactics*. It is the list of *directions* that do not collapse into each other. Sub-tactics of (2) and (4) — tower uniform, NF-D, two-pole templates, D25 Schur certificates, Galois/Weyl “shields” — are not top-level JC2 approaches. They are how this campaign spends its days inside (2)+(4).

---

## 1. GGV Newton-polygon classification and the degree-bound farm

**(a)** A minimal-degree plane counterexample, if it exists, has one of a finite list of Newton-polygon “corner families”; transcribe \([P,Q]=x^k\) on each family as a bilinear system and prove emptiness (or find a point).

**(b) Tried.** Origin of the repo. Generator A and the reduction cascade: `lib/jc.py`, `lib/reduce.py`–`reduce4.py`, `cases/emit.py`, `CAMPAIGN.md`, `AUDIT.md`, `plan-72-108.md`. The leftover pair below 125 is \((72,108)\), GGHV Prop. 4.3, family \(A_0=(8,28)\). Subcase (2) emptied over \(\mathbb Q\) (chartG symbolic \(-1\), cCa2/cCa6 Gröbner); subcase (1) settled by audited Helali/Suzuki artifacts plus three-way transcription agreement (`CROSSCHECK.md`). Family enumeration: `lib/families.py`, `lib/FAMILIES.md`, `SECTION4-AUTOMATION.md`. Frontier farm \(\deg\le 150\): `lib/farm.py`, `systems/farm/`, `README.md`. External concurrent claims: Helali, Suzuki, Santibañez-Leal, Ishihara (`RECON.md`).

**(c) Stuck.** (i) The method is finite only *below a degree cutoff*. Raising 108→125 is a theorem about that cutoff, not about JC2. (ii) GGV §4 reductions are load-bearing and still not a fully implemented coefficient-free engine for every family (`SECTION4-AUTOMATION.md` is a design; farm still emits 7 families “honestly out of reduce4 scope”). (iii) Char-0 certificates for the large cores are a memory wall: cCa2/cCa6 lifts retired by last-chance rule; farm “2 boxes grinding.” (iv) Helali/Suzuki beat the campaign to *claiming* \((72,108)\) with unaudited Zenodo packs; the authority slot is audit+arXiv, not novelty of emptiness. (v) A nonempty core would be a candidate tower, not yet a polynomial pair.

This is the only computational program that has historically moved the plane bound (Moh 100, GGV 108, claimed 125). It will never, by itself, prove JC2: there is always a next pair. As a *disproof* search it is honest — the same Gröbner that empties a family would exhibit a point — and that is its real dual use.

---

## 2. Sheet-number / topological degree at infinity (Orevkov–Domrina–Żołądek–Sigray)

**(a)** Compactify a Keller map, resolve the dicritical divisors at infinity, and show that no Puiseux / Eggers–Wall decoration with topological degree \(td=[\mathbb C(x,y):\mathbb C(f,g)]\) in \(\{6,7,8\}\) (and, if one is greedy, higher) can exist; \(td\le 5\) is classical; a consistent local datum exists at \(td=9\), bidegree \((48,64)\) (Moh / Orevkov “JC at infinity”).

**(b) Tried — the campaign’s active endgame.** `SHEET6.md`, `SHEET6-CAMPAIGN.md`, `SIGRAY-AUDIT.md`, `SHEET6-PILOT.md`, `SHEET6-2POLE.md`, `SHEET6-TEMPLATE.md`, `SHEET6-CLASSICAL.md`, `SHEET6-MULTIPOLE.md`, `BOOK-*.md`, `TOWER-*.md`, `TOWER-UNIFORM.md`, `TOWER-TD11.md`, `TRANSPORT.md`, `SOL-PROP58.md`, `REDUCTION.md`. Engine: `cases/sheet6_campaign.py` and a swarm of book/tower checkers. Sigray td≥6 as printed is incomplete (errata E1–E10; H3; rows 1,5,7,10 untreated). Campaign closed td≤5 independently of AF2; td=6 single-pole to 4 r9/M2 classes; two-pole (3,3) funneled to residue-A with rigid \(a_1/a_2=2+\sqrt 3\); td=7 tower panel claimed closed (17/17); td=11 entry-clash promoted with named OPEN residue.

**(c) Stuck, precisely.**

1. **No \(td\) ceiling.** Local-at-infinity methods are known to admit a consistent tree at 9. Anything \(\ge 9\) is invisible to this engine. `TDBOUND.md` tried to manufacture a ceiling; the empirical correlation is mostly a census artifact (see §28).
2. **Landing is not a theorem.** `REDUCTION.md`: GGV selects *some* globally minimal pair; Sigray normalizes *some* pair in a different equivalence; there is no functor from GGV corners to a fiber-tagged decorated tree; off-axis \(b\ge 2\) books have no completeness certificate.
3. **Coefficient wall.** Combinatorial λ-budgets and merge arithmetic kill most cells and then stop. Survivors are rigid templates whose remaining content is Puiseux *coefficients* (L1/R1/R2). Galois descent, panel budgets, and vertex-local Weyl quantization were proved to have **zero traction** against those templates (`TEMPLATE-ATTACK.md` shields S1–S3). That is the campaign admitting the combinatorial program is finished and the algebra has not started.
4. **Foundations.** Sigray is an unrefereed thesis; Żołądek’s neighboring-gcd sections have a documented GGV gap. Prop 5.8 was repaired (`SOL-PROP58.md`) using Chau’s exceptional-value theorem as external trust. The engine is only as strong as that ledger.

The 4→5 jump is the warning the field already paid for: Egorov’s 5-sheeted exotic covering of \(\mathbb C^2\) is consistent with every quasi-topological invariant Domrina–Orevkov used. Topology is not enough. The campaign rediscovered this the hard way at residue-A.

---

## 3. Vertex-gap, strip ODEs, and the residue functional \(R_{k,d_2}\)

**(a)** On reduced strip pairs with \([P,Q]=x^k\), a Minkowski-vertex normalization plus a gap on the bottom corners produces a self-contained near-origin block; the leftover is a logarithmic residue \(R_{k,d_2}\); rigidity of \(AC'-kA'C=1\) forces \(\deg A\le 1\).

**(b) Tried, and this is the campaign’s actual theorem.** `LEMMA.md`, `SURPLUS.md`, `SURPLUS-EXT.md`, `RESIDUE.md`, `MATHIEU.md`, `paper1/main.tex`. Theorem A / conj:R promoted, then priority-corrected: the ODE rigidity is Żołądek 2008 Appendix A.7 (Liouville), used by Żołądek *inside plane JC* at (3.14). The campaign’s novel content is the block↔ODE bridge, strip uniformity, and the char-\(p\) boundary (`paper2/SCOPE.md`, `paper2/PRIORITY.md`). Mondello stress test: `MONDELLO-CHECK.md`.

**(c) Stuck.** Scope is strip pairs with vertex normalization and \(k,d_2\ge 2\). It empties the generic chart of \((8,28)\) subcase (2) and describes the depth-two block at every such cell. It does **not** cover: \(k=1\); non-strip shapes; deeper Minkowski columns; the \(y\)-axis column that blocked subcase (1) of (8,28); \(k\ge 3\) leftover vanishing (`SURPLUS-EXT.md` §2). Char \(\{2,3,5\}\) exclusions are necessary — Mondello is the existence proof that the even lattice-determinant pivots die in char 2. This is a theorem about a class of polygons, not a JC2 proof. Treating it as “the mechanism” of JC2 is how one writes Paper 1 and then forgets to leave.

---

## 4. Coefficient-level Puiseux windows (residue-A and relatives)

**(a)** Take a combinatorially surviving infinity-configuration, pin the rigid leading data, write the Jacobian identity as a recursive window on tail coefficients, and Gröbner/quotient the window until empty or a germ appears.

**(b) Tried to exhaustion.** `SHEET6-DIRECTIONB.md`, `SHEET6-R1.md`, `SHEET6-DEPTH.md`, `DEPTH-STAB.md`, `SOL-ALGEBRAIZATION.md`, `xmodel/sol-conjecture-k.md`, `xmodel/sol-codim2.md`, `xmodel/sol-toric.md`, `xmodel/sol-ideas-0821.md`, plus the D21/D23/D25 emission swarm under `cases/` and `systems/r1/`. Depth-21 monomial relaxation consistent, tangent at zero inconsistent, nonlinear residual the honest object. Subsequent depths: modular loci **nonempty**, with D25 (as of 2026-08-21 internal notes) a union of affine cells rather than a unit ideal. Toric-circuit closure: no kill at tier 1 (`xmodel/sol-toric.md`). Hermite–Padé algebraization: full rank on a *fixed* completion, locus-wide algebraizability not tested (`SOL-ALGEBRAIZATION.md`).

**(c) Stuck.** The window is a chart: B-frozen, no-log, `PIN42`, \(W_1W_2\neq 0\), often one radical fiber. Nonemptiness modulo good primes is **not** a germ, **not** characteristic 0, **not** a polynomial pair. Depth stabilization (`DEPTH-STAB.md`) says that if *all* depths stay nonempty then a mod-\(p\) formal germ exists — König on a Noetherian chain — and the campaign has been watching that chain *not die*. The disproof side then needs: char-0 lift, all places, all depths, then algebraization. None of those arrows is even armed. Continuing to add two depths and another 48-hour F4 job is the definition of a local maximum. Fashionable inside the repo: “the D-series *is* JC2.” It is not (`REDUCTION.md`).

---

## 5. Jung–van der Kulk: reduce a Keller map by elementary automorphisms

**(a)** \(\mathrm{Aut}(\mathbb C[x,y])\) is generated by affine and elementary (Jonquière) maps. JC2 is equivalent to: every Keller map is a finite composition of those. Strategy: given Keller \((P,Q)\) of degree \(>1\), produce an elementary automorphism that strictly drops \(\max(\deg P,\deg Q)\).

**(b) Not tried as a JC2 program.** `TRANSPORT.md` proves a *coordinate-cusp* lemma with an LND argument and uses weighted JvdK for GGV↔Sigray *normalization transport*, not for degree-lowering an arbitrary Keller pair. A crank Lean file (Reed, `RECON.md`) “proves JC2” by JvdK circularity; the campaign correctly discarded it.

**(c) Field obstruction.** This *is* how low-degree theorems are proved (Wang degree 2; the inductive step in Moh-style bounds). The obstruction at large degree is exactly that the leading forms of a hypothetical counterexample are powers of a common form (GGV), so the obvious triangular substitutions *do not* drop degree — they ride the cusp \(d^m U^n - c^n V^m\). That is why GGV exists. A proof of JC2 along this line is a proof that those leading-form cusps still admit a degree-dropping tame generator after all, or that no such pair can satisfy \(J=1\) beyond the leading face. The campaign’s transport theorem attacks the *normalization* of an already-minimal pair, which is the other direction.

**(d) Cheapest experiment.** Enumerate reduced Jung words of length \(\le 6\) over \(\mathbb Q\) and \(\mathbb F_{101}\), triangular exponents \(2..8\), and test whether any word’s \((m,n)\)-initial face lies in the cusp ideal \((d^m U^n-c^n V^m)\) for coprime \(2\le m<n\le 13\) (`xmodel/sol-lateral3.md` already wrote this test and it was not run as a JC2 lane). If a word hits the cusp, the degree-lowering strategy is dead in that range and one should stop. If none hit, one has evidence for a cusp-avoidance lemma, which is the actual theorem to prove. **Promise: 5.** This is classical, unfashionable, and aimed at the exact leading-form rigidity GGV isolated. It is also where a century of experts already stalled, so 5 is not optimism.

---

## 6. Abhyankar–Moh–Suzuki embeddings / one-place semigroups

**(a)** A polynomial embedding \(\mathbb C\hookrightarrow\mathbb C^2\) is equivalent to a linear embedding; a Keller pair in which \(f\) (or \(g\)) has one place at infinity is an automorphism. Strategy: show a counterexample cannot exist because some associated curve is forced one-place and then AM applies.

**(b) Tried, on the wrong object.** `SHEET6-CLASSICAL.md` T2 (AM valuation form along the fiber: poles pass with zero slack; one x-side alternative killed). `AM-CHECK.md`: the one-place *inequality* does not bind on residue-A fibers — they are multi-place, and the P-places are finite-center type; the inequality’s violation is a certificate of that, not a kill. The objects AM can kill are components of Jelonek’s \(A(F)\), whose place data the single-fiber template does not pin.

**(c) Stuck.** A counterexample’s \(f\) is *necessarily* not one-place (AM-JAC). The fiber of a surviving template is therefore on the mandatory side of the dichotomy. The live AM attack is on \(A(F)\) components (§7), which requires the cross-fiber asymptotic-value correspondence the campaign explicitly did not derive. Running AM on Puiseux germs of \(f=a\) is a category error the campaign has now documented twice. Field-level: AM is the reason “one coordinate is a coordinate” implies JC2; the whole difficulty is that neither coordinate is.

---

## 7. Properness and Jelonek’s asymptotic variety \(A(F)\)

**(a)** A proper Keller map is an automorphism. A counterexample is therefore non-proper; \(A(F)\) is a nonempty curve whose irreducible components are rational with one place at infinity. Constrain \(A(F)\) until it cannot exist.

**(b) Tried as a consistency check, not as a construction of \(A(F)\).** `SHEET6-CLASSICAL.md` T4: geometric degree \(\mu(F)=6\), non-properness excess \(\ge 6\), *passes*. `AM-CHECK.md` names the A(F) route and leaves it “not run here.” `SOL-PROP58.md` uses Chau’s theorem on exceptional-value curves to kill a specialization defect — that is adjacent (exceptional values, not the full asymptotic set).

**(c) Stuck.** Describing \(A(F)\) for a general Keller map is historically as hard as JC2 (Jelonek, Vitushkin, Kaliman). The campaign computed numerical constraints *assuming* the residue-A genome, which any actual pair in that template would have to obey — a consistency check, not a non-existence proof. The missing object is an equation for \(A(F)\) from \(J=1\) and the pinned Newton data, or a contradiction between AM on \(A(F)\) components and the forced pole orders. Field obstruction: \(A(F)\) is defined from the map at infinity; computing it is the compactification problem again.

**(d)** Not scored — the *instrument* was tried; the *A(F)-as-the-object* program was not. If one insists on a first experiment for the unrun half: from the residue-A genome, construct the candidate asymptotic values \(c_p(a)\) as algebraic functions of \(a\) by matching B-side finite \(g\)-values across the pencil, then apply AM-SG to each irreducible component of the resulting plane curve. If the correspondence cannot even be written as a finite algebraic correspondence, the route is not cheaper than rebuilding the compactification. I would not start here.

---

## 8. The formal inverse is a polynomial

**(a)** \(J(F)\in\mathbb C^*\) implies \(F\) is locally invertible; the formal inverse series exists. JC2 ⇔ that series is polynomial ⇔ all sufficiently high multi-degree coefficients vanish. Attack via Bass–Connell–Wright / Abhyankar / McKay–Wang inversion formulae, degree bounds on the inverse, or recursive vanishing of homogeneous components.

**(b) Not tried.** `phase0-mo-answer-draft.md` mentions the McKay–Wang formula as something MathOverflow already knows. No inversion-coefficient campaign exists in the repo.

**(c) Field obstruction.** There is no uniform degree bound on the inverse in terms of \(\deg F\) independent of the (hypothetical) counterexample; that bound *is* JC2. The inversion formulae express inverse coefficients as polynomials in the jet of \(F\) divided by powers of \(J\), and \(J=1\) simplifies the denominators without forcing vanishing. In dimension \(\ge 3\) the inverse of a Keller map can be a well-defined formal series that is not polynomial — that is what the Alpöge map *is*. In dimension 2 the same formulae do not know they are in dimension 2. The 2-dimensional input has to be injected by hand (e.g. Jung generation of the inverse, or a 2-variable residue vanishing). Without that, this is a rewriting of the problem.

**(d) Cheapest experiment.** Take the inversion formula in 2 variables, truncate at inverse-degree \(N=2d^2\) (the automorphism bound when the map *is* invertible), and for a generic degree-\(d\) Keller jet with \(d=4,5\) (already known to be automorphisms) verify that the formula’s coefficients above \(\deg^{-1}=d\) vanish identically as polynomials in the jet. Then push \(d\) to the first GGV-open range and see whether the vanishing identities continue to hold formally (as polynomial identities on the Keller locus) or require the pair to already be an automorphism. If they hold on the Keller locus at \(d=4\) by representation-theoretic accident rather than invertibility, the identities are not a proof method. **Promise: 4.** Cheap to pilot, structurally unlikely to scale past the degrees already killed by Moh.

---

## 9. Dixmier conjecture DC(2)

**(a)** Every endomorphism of the second Weyl algebra \(A_2\) is an automorphism. DC(2) \(\Rightarrow\) JC(2). Prove DC(2).

**(b) Tried, then parked.** `DC2-PROGRAM.md`, `DC2-REVIEW.md`, `cases/dc2_slice.py`, `cases/dc2_deg3.py`, `systems/dc2/`. Degree \(\le 2\): all quadruples are automorphisms (slice theorem). Degree-3: quantum/classical divergence is real and carried by six deg-0 vertex equations; DC(2) consistent with HOLDS on loci reached; degree-4 sized and parked.

**(c) Stuck — and the fashionable slogan is wrong.** `RECON.md` and the campaign’s own notes call DC(2) “the strongest surviving *proof* route.” That sentence is true as an implication and false as advice. DC(2) is *strictly stronger* than JC(2). Both statements above it on the ladder — JC(4) and PC(2) — are now *false*. The only known bridge from Weyl endomorphisms to commutative Keller maps (Belov–Kontsevich, reduction mod \(p\), Poisson structure on the huge center) consumes JC(4)/PC(2) and is therefore dead as a proof of DC(2). Native \(A_2\) strategy dies at step zero: there is no Schur normal form for a two-variable operator, and centralizers are huge and noncommutative (`DC2-PROGRAM.md` §2). A DC(2) *counterexample* would **not** disprove JC(2). Long’s near-miss Poisson lift is the actual disproof-of-the-route to watch, not a JC2 attack. Slicing Bernstein degree 3 is the correct cheapest experiment; the campaign already ran it and learned that quantization is rigidifying exactly where the classical shadow is false, which is interesting and not a proof.

Continuing DC(2) at degree 4 is a computational black hole larger than (72,108), aimed at a stronger statement, with no reduction theory analogous to GGV. Promise as a *JC2* method if restarted: I would score it 3, but it is not untried.

---

## 10. Zheglov’s DC(1) as a disproof of JC2

**(a)** JC(2) \(\Rightarrow\) DC(1). Therefore a counterexample to DC(1) yields a counterexample to JC(2). Audit, or refute, Zheglov arXiv:2410.06959v5.

**(b) Tried, shallowly.** `ZHEGLOV-SCOPE.md`, `ZHEGLOV-LTEST.md`, `tests/ltest_polynomials.py`, `zheglov/`. T1: Lemma L:polynomials passed 640/640 exact instances. T2 (symbolic replay of S6 Steps 4–7, the twice-rewritten endgame) was named as the live next action and **not done**.

**(c) Stuck.** Even a verified DC(1) proof would **not prove JC2**. Even a refutation of Zheglov would not produce a DC(1) counterexample. The disproof route needs an actual non-surjective endomorphism of \(A_1\). None is known; the paper’s whole point is that none exist. The remaining risk mass is a 400-line hand calculation in a private vector-form calculus plus an N-independence lemma, under journal review with no acceptance after a year. Auditing T2 is defensive recon, as the campaign itself recorded, and then it wandered off to sheet-6.

---

## 11. Mathieu’s conjecture (and why “Mathieu” in this repo is a different object)

**(a)** Mathieu (1995): if a function on a compact connected Lie group has all moments vanishing, then so do all multiples past some degree. Mathieu \(\Rightarrow\) JC. Prove Mathieu.

**(b) The conjecture is dead as a JC route.** Long, arXiv:2607.19012: Mathieu fails for SU(2). The campaign used the *abelian* Duistermaat–van der Kallen theorem (ker of the constant-term map on Laurent polynomials is Mathieu) as a *mechanism* for the strip residue, then discovered Żołądek/Liouville already had the ODE (`MATHIEU.md`, `paper2/PRIORITY.md`). GMC(2) is true (Wilson); GMC(\(n\ge 3\)) is false (Long).

**(c) Stuck = refuted.** Invoking “Mathieu–Zhao theory” as a JC2 strategy in 2026 is either ignorance of Long or a bait-and-switch in which one means DvdK on a torus. DvdK on a torus is a 1998 theorem and does not know about Keller maps; the campaign already extracted the one lemma it gives. SC1 (Mathieu property of \(\mathrm{Im}(A\partial-kA')\) on a multiply-punctured line) is an exported question for the MZ community, not a JC2 lever (`paper2/SCOPE.md`).

---

## 12. Poisson, Gaussian moments, Hessian, and the rest of the Zhao ladder

**(a)** A web of implications: Mathieu \(\Rightarrow\) GMC \(\Rightarrow\) JC; Hessian conjecture; Poisson conjecture PC\(_n\) \(\Rightarrow\) DC\(_n\) \(\Rightarrow\) JC\(_n\); stably JC \(\Leftrightarrow\) DC \(\Leftrightarrow\) PC.

**(b) Status, not a campaign program.** PC(2) false (Long, Lean \(\neg\)PC(2)\(\Rightarrow\neg\)JC(4)). GMC(\(n\ge 3\)) false. Hessian false except possibly HC(4) (`RECON.md`). FACE-ISOLATION.md ports Wilson’s GMC(2) *technique* (face isolation / Kummer valuation) to Keller pairs; the port is “partial-real”: architecture matches slots already filled by vertex-gap; the infinite moment tower vs one bilinear identity is the disanalogy.

**(c)** These were never JC2 methods. They were hope that a stronger, more analytic statement would be easier. After July 2026 the ladder above JC(2) is a pile of counterexamples, and the dim-2 positives (GMC(2), graded-equivariant JC2) are consistent with JC2 being true without proving it. Face isolation as a *new* Keller tool is the only salvage; the campaign analyzed it and did not run a p-adic face-isolation proof of anything beyond what surplus already gives.

---

## 13. Lee–Li Conjecture E (Magnus remainder vanishing)

**(a)** A nested chain E\(\Rightarrow\)D\(\Rightarrow\)C\(\Rightarrow\)B\(\Rightarrow\)A\(\Leftrightarrow\)JC2 (Abhyankar degree-divisibility). E is a remainder-vanishing statement about a Tschirnhausen / weighted-homogeneous expansion. Prove E.

**(b) Tried at toy scale.** `conjectureE-plan.md`, `lib/conjE.py`, `tests/test_conjE.py`, `runs/conjE_results.txt`, `systems/conjE/` (hundreds of msolve files). Seven smallest instances: 6 HOLD with char-0 Gröbner certificates, 1 degenerate, 0 fail. Commuting-pair gate passed.

**(c) Stuck.** E is a *stronger* family of identities, parametrized by a mess of discrete data \((a,b,m,n,\delta,i,B,\mu)\), each instance a sizable bilinear/algebraic system. Holding at \(\delta=1\), \((a,b,m,n)=(2,3,2,4)\) is the least surprising thing in the world if JC2 is true. The next instances scale badly (`notes.md`: “scale-up when compute frees” — compute never freed). There is no reduction of E to a finite check. The Magnus-formula program of Glidewell–Hurst–Lee–Li has had no new installment since 2024 (`RECON.md`). This is an implication-ladder with a worse generating function.

---

## 14. Bass–Connell–Wright / Yagzhev / Drużkowski cubic reduction

**(a)** JC in all dimensions reduces to the invertibility of cubic homogeneous (or cubic-linear Drużkowski) maps. Prove those; get all of JC, hence JC2.

**(b) Not tried.** Correctly.

**(c) Hollow for the plane.** The reduction *raises dimension*. Cubic Keller maps in two variables are already automorphisms by the degree bound. Drużkowski maps that could be counterexamples live in dimension \(\gg 2\). After Alpöge, the cubic reduction is a machine for manufacturing *more* high-dimensional counterexamples, which the internet already did (Gallagher’s 98 maps, Gao’s tangent-sweep). Citing BCW as a JC2 strategy in 2026 is a category error that still appears in survey talks.

**(d) Experiment:** none worth running. **Promise: 1.**

---

## 15. Graded, equivariant, and weighted-homogeneous Keller maps

**(a)** Restrict to maps homogeneous for some \(\mathbb G_m\)-action (or a character). Prove they are automorphisms, or find a graded counterexample.

**(b) Not proved by the campaign; used as negative space.** Shaska arXiv:2607.20210v2: in dimension two, graded-equivariant Keller maps are automorphisms for *every* weight sign pattern. Homogeneous (ordinary \(\mathbb G_m\)) plane Keller maps being linear is classical and easy. Campaign cites this in `paper1/main.tex` and `RECON.md`. No independent graded search.

**(c) Closed as a counterexample hunt, open as a hint.** There is no graded plane counterexample. A hypothetical JC2 counterexample has no \(\mathbb G_m\)-symmetry. That is consistent with GGV: the interesting polygons are *not* cones from the origin in a single weight. Searching for quasihomogeneous CEs is a dead disproof lane. As a proof lane, “reduce to the graded case” is false.

---

## 16. Descend a dimension-\(\ge 3\) counterexample to the plane

**(a)** Alpöge / Gallagher weighted-lifts / Gao tangent-sweep / Speyer \(\mathbb P^1\times\mathrm{Sym}^2\mathbb P^1\to\mathrm{Sym}^3\mathbb P^1\) produce Keller maps that are finite-to-one of degree \(\ge 3\) in dimension \(\ge 3\). Specialize, project, take invariants, or write a 2-variable analog.

**(b) Recon and negative controls, not a construction program.** `RECON.md` records Speyer-thread Picard obstruction: the direct generalization \(\mathbb P^1\times\mathbb P^{d-1}\to\mathbb P^d\) fails for \(d\ge 4\) by a class-group obstruction \(\mathbb Z/(d-2)\); “only \(d=3\) threads the needle.” Shaska: the Alpöge map is equivariant for weights \((1,-1,-2)\), a pattern that cannot occur for a plane graded map. Mondello is a char-2 plane CE *derived from* a 3-variable char-2 map — that descent *works in char 2* and the campaign verified it (`MONDELLO-CHECK.md`). CryptoJuudaime’s claimed “provable failure” of a 2D Alpöge analog is unvetted (`RECON.md`).

**(c) Stuck.** The geometric reason dim 3 works (forget-a-root on binary cubics; sheets escaping to infinity together) uses a 3-dimensional moduli of cubics. There is no analogous forgetful map of affine 2-space with Jacobian 1 and degree \(>1\). Weighted lifts require a third variable. Tangent-sweep uses projective duality of plane *curves* to build maps on higher-dimensional spaces. Every known mechanism is silent on \(\mathbb A^2\), and the silence looks structural rather than a missing trick. Fashionable post-July-2026 activity was “factory of 3-variable maps.” That factory does not have a 2-variable product.

**(d) Cheapest experiment.** Write the most naïve 2-variable forgetful maps — e.g. \((x,y)\mapsto(x, y^2+p(x)y+q(x))\) and elementary variants — impose \(J\in\mathbb C^*\), and Gröbner the coefficient conditions at \(\deg p,q\le 8\). Expected output: only automorphisms (elementary + affine). If something nonempty and non-tame appears, one has a story. This has been done by hand for decades in low degree; the value is only as a machine-checked negative. **Promise: 2.**

---

## 17. Characteristic \(p\), separable JC, and Witt lifts

**(a)** Study Keller maps over \(\overline{\mathbb F}_p\). Either find a char-0 lift of a positive-char counterexample (disproof of JC2), or prove that obstruction classes in Witt / crystalline cohomology forbid lifts (support for JC2), or prove separable JC in char \(p\) (does not imply char 0).

**(b) Tried on the one object that matters.** Mondello arXiv:2608.02634: explicit plane Keller pair over \(\overline{\mathbb F}_2\), \(\det J=1\), 3-to-1, separable. Verified: `cases/mondello_verify.py`, `MONDELLO-CHECK.md`. Collapse over \(\mathbb Q\) at even-determinant M2 pivots. Witt–Bockstein: `xmodel/sol-witt.md`, `cases/witt_check.py` — on the registered Mondello-hull-plus-one-shell stratum, the unrestricted \(W_2(\mathbb F_2)=\mathbb Z/4\) obstruction **never vanishes** (1,152 Keller-collision data, 0 unobstructed).

**(c) Stuck.** Separable JC is *false* in char 2 in the plane. That kills “JC2 because étale+affine+dim 2 is formal.” It does not kill char-0 JC2: the lift obstruction on the Mondello shape is real and, in the searched stratum, total. The open questions: (i) other supports / other primes, (ii) whether a char-\(p\) plane CE with vanishing Witt obstruction exists, (iii) whether a char-0 proof can be written as “reduction mod \(p\) for infinitely many \(p\) plus vanishing of obstruction.” (iii) is a genuine arithmetic program the campaign touched once and did not professionalize. Fashionable “prismatic JC” without a concrete obstruction class is §34.

---

## 18. Random, SAT, homotopy, or fewnomial search for a pair

**(a)** Sample polynomial maps of degree \(d\), impose \(J=1\) (linear in mixed coefficients), and search for non-injectivity: collisions, nontrivial generic fiber, or non-invertible leading forms plus a completed series.

**(b) Not tried as a search.** The campaign’s Gröbner work is *emptiness of reduced families*, the dual of this. Line/plane probes (`lib/lineprobe.py`, `lib/planeprobe.py`) tested codimension of solution loci of *already reduced* systems, not random maps.

**(c) Why it is a bad disproof method at naïve degree.** Wang: no degree-2 CE. Moh: no CE with \(\max\deg\le 100\). A random search below the GGV cutoff is a search in a region theorems already emptied, unless one drops Newton-polygon constraints and hopes to luck into a pair the classification missed — i.e., a bug in GGV. Above the cutoff the coefficient space is enormous, the Keller condition is underdetermined, and almost every solution is an automorphism (tame, huge moduli). Detecting “not an automorphism” is itself the problem (properness tests, Gröbner of the inverse, collision search at infinity). Fewnomial restriction is more interesting: sparse supports *are* Newton polygons, i.e. this collapses to §1.

**(d) Cheapest experiment.** SAT/SMT on 0-1 coefficients, support inside a 6×6 box, \(J=1\), plus “three distinct points map to one” over \(\mathbb F_p\) for a 10-bit prime, then attempt a char-0 lift of any hit. Budget: a night. Expected: only affine/elementary collisions (none) or char-\(p\) artifacts that do not lift (Mondello-type). **Promise: 2.** The one scenario where this is not stupid is a bug-hunt against GGV’s completeness.

---

## 19. Dessins d’enfants, Hurwitz, and monodromy of \(\hat g\)

**(a)** A generic fiber \(f=a\) compactifies to a curve \(\overline C\) with \(\hat g:\overline C\to\mathbb P^1\) of degree \(td\). Ramification lives at infinity (Keller kills affine critical points). The monodromy representation \(\pi_1(\mathbb P^1\setminus B)\to S_{td}\) plus Riemann existence is a topological constraint; some passports may be unrealizable, killing the configuration.

**(b) Tried on residue-A.** `GROK-MONODROMY.md`, `cases/grok_monodromy.py`: \(S_6\), pole type \((3,3)\), 169 passports of 2-cycles with \(a+2b+3c=42\); **every one admits a transitive tuple multiplying to 1**. Template survives. Suzuki’s (8,28) exclusion used a 5-class dessin analysis of the *top edge* (`RECON.md`) — a different, finite, successful use of the same language on a Newton-edge polynomial, not on the compactified fiber.

**(c) Stuck.** Riemann existence is generous: once you allow enough 2-cycles at infinity, \(S_n\) (or \(A_n\)) fillings exist. Kistner–Shaska’s dim-3 result that geometric monodromy is full \(A_n/S_n\) except at degree 3 is the *opposite* of a kill — it says monodromy is generic. Qiu’s “\(A_{21}\) monodromy excludes (72,108)” is artifact-less and should be ignored (`RECON.md`). The one historically successful dessin attack (Suzuki) is a dressed Bézout certificate on an edge polynomial, i.e. §1 in costume. A global “the monodromy cannot be primitive of degree \(td\)” statement would be §23, and is untried.

---

## 20. Face isolation / \(p\)-adic separation of Newton faces

**(a)** Wilson’s GMC(2) proof: a global vanishing identity, after a good prime is chosen, has \(p\)-adic valuation that isolates a single Newton face via Kummer carries on multinomials; the face identity then forces one-sided support.

**(b) Analyzed, not executed as a proof.** `FACE-ISOLATION.md`: the transferable core is “valuation-counting discipline”; its TL1 is the surplus-condition theorem the campaign already proved by other means. No independent face-isolation identity for \([P,Q]-x^k\) was written and run.

**(c) Stuck.** GMC has an infinite tower of moment vanishings \(E(P^m)=0\) for all \(m\), which supplies arbitrarily large \(p\)-powers. Keller supplies **one** bilinear identity (plus the polynomiality of \(P,Q\)). There is no integer \(m\) to send to infinity. Unless one manufactures a substitute tower (powers of a leading form, or Mathieu-type powers of an element in a residue kernel — circular), the method has nothing to isolate. Surplus already *is* the face-counting of that one identity.

---

## 21. Compactification, BMY, and logarithmic Kodaira of the resolved pencil

**(a)** Build the log surface of the resolved \(f\)-pencil (vertical boundary + sections). Apply Miyaoka–Yau / Bogomolov–Miyaoka–Yau in orbifold form, or \(\bar\kappa\) constraints, or unimodularity of the splice diagram (Orevkov/Domrina), and obtain a numerical contradiction for a counterexample.

**(b) Tried on the pinned skeleton.** `SHEET6-CLASSICAL.md` T3: full \((K+D)^2\le 3 e_{\mathrm{orb}}\) **needs B- and x-internal resolution data the template does not pin**. Euler/delta/genus ledger **passes identically**. Integrality witnesses exist (including rational-fiber candidates). Orevkov 3-sheet and Domrina–Orevkov 4-sheet papers are in `refs/` and were the reason td=5 needed a new analytic layer (Egorov).

**(c) Stuck.** \(\mathbb C^2\) has \(\bar\kappa=-\infty\), so BMY does **not** apply to a naïve compactification of the source. The Orevkov-style surface is an auxiliary construction whose graph *is* the unpinned tail. Quasi-topological invariants were already known to be insufficient at 5 sheets. Computing Euler numbers of a configuration that was built to satisfy them will not contradict them: the ledger “passes identically” is the predicted non-result. Completing T3 after pinning B/x partitions is a finite continued-fraction computation (`SHEET6-CLASSICAL.md` §3b) and might still kill *some templates*; it will not kill JC2, and it did not kill residue-A at chi-level.

---

## 22. Affine surface theory: LNDs, Makar-Limanov, Gizatullin, Kaliman

**(a)** \(\mathbb A^2\) is characterized among affine surfaces by some package (trivial Makar-Limanov invariant, two independent LNDs, isomorphism with a Gizatullin surface of a certain type, cancellation, etc.). A non-proper étale endomorphism would produce a surface (graph, image, or finite cover) that violates the package.

**(b) Not tried as a JC2 program.** LNDs appear in `TRANSPORT.md` as the *proof method of the coordinate-cusp theorem* (a self-contained LND argument, deliberately avoiding extra JvdK dependency). That is the right algebraic geometry used locally. There is no ML-invariant computation of \(\mathbb C[f,g]\subset\mathbb C[x,y]\) for a hypothetical pair, no Gizatullin-form classification of the compactified graph, no Kaliman-style contractibility argument.

**(c) Field obstruction.** \(\mathrm{ML}(\mathbb C[x,y])=\mathbb C\). For a Keller pair, \(\mathbb C[f,g]\cong\) a copy of a polynomial ring sitting of finite index in the fraction field, and typically \(\mathrm{ML}(\mathbb C[f,g])=\mathbb C\) too — the invariant does not see the embedding. LNDs on \(\mathbb C[x,y]\) are completely classified (Rentschler): triangular in suitable coordinates. A JC2 proof via LNDs is close to JvdK again (§5). Kaliman–Koras–Russell technology is strongest in dimension 3 (exotic \(\mathbb A^3\), Koras–Russell cubic). Dimension 2 affine surfaces are “too classified”: the classification tends to assume facts equivalent to what one wants.

**(d) Cheapest experiment.** For the residue-A *numerical* degree pair \((\deg f,\deg g)=(168,252)\), compute the Makar-Limanov invariant of the graded ring of the leading forms (a 2-generator graded algebra with a cusp relation) and see whether it already differs from \(\mathbb C\) in a way forbidden by a Keller leading-form constraint. This is a one-afternoon computer-algebra check on the associated graded, not on the pair. **Promise: 4.** Modest, because any contradiction visible at leading-form level is probably already a GGV face identity.

---

## 23. Étale topology: primitive monodromy and a group-theoretic \(td\) bound

**(a)** Over \(\mathbb A^2\setminus A(F)\) a counterexample is a connected finite étale cover of degree \(td\), monodromy a transitive subgroup \(G\le S_{td}\). Use topology of the complement (or the log fundamental group of the compactified pair) to forbid primitive \(G\) for large \(td\), or to force a block decomposition that reduces \(td\).

**(b) Not tried as a global bound.** `GROK-MONODROMY.md` tests *realizability* of a passport for one template (survives). `xmodel/sol-lateral3.md` proposed a primitive-monodromy bound and was not executed. No computation of \(\pi_1(\mathbb A^2\setminus C)\) for a candidate branch curve.

**(c) Field obstruction.** \(\pi_1(\mathbb A^2\setminus C)\) for a plane curve is a classical monster (Zariski, van Kampen, Libgober). For the unknown \(C=A(F)\) of a hypothetical counterexample it is not even defined in the campaign’s data. Primitive-group bounds from Riemann–Hurwitz plus “all ramification at infinity” *could* be cheap — that is the experiment below — but they tend to permit \(A_n\) and \(S_n\), which is what one expects from Kistner–Shaska in dim 3.

**(d) Cheapest experiment.** Assume only: ramification of \(\hat g:\overline C\to\mathbb P^1\) supported at \(\le N\) points at infinity, Riemann–Hurwitz, transitivity, primitivity. Enumerate possible ramification types for \(td=6,7,8,9\) and check which primitive groups in the Magma/GAP primitive-group databases admit such types. If primitive \(G\) is forbidden for \(td=9\) with the Orevkov \((48,64)\) place counts, one has a contradiction with a known “JC at infinity” example (so the hypotheses are too strong). If it is permitted, the bound is not a bound. This is a weekend GAP script. **Promise: 5.** Highest among the untried *cheap* tests, because a negative control against \((48,64)\) at infinity is built in and would immediately discipline the idea. I do not expect a JC2 theorem; I expect to learn that \(A_{td}\) is allowed.

---

## 24. Algebraize a formal germ at infinity (the honest disproof lane)

**(a)** Produce a formal (or mod-\(p\) formal) solution of the Jacobian identity in Puiseux series at the dicritical places; then prove the series are algebraic, hence come from a polynomial pair; then check it is not an automorphism.

**(b) Tried, and it refused.** Hermite–Padé / bounded support algebraization: `SOL-ALGEBRAIZATION.md` — the prescribed rectangular Ansatz for a *fixed* residue-A completion has full column rank at two good primes (not algebraizable with that support). Depth windows (§4) have not produced a certified germ, only nonempty finite-depth schemes. `DEPTH-STAB.md` is the meta-lemma that infinite nonempty depth \(\Rightarrow\) mod-\(p\) germ.

**(c) Stuck.** Algebraization of a *nonexistent certified germ* is vapor. Algebraization of a germ that is B-frozen, no-log, and modular is not a polynomial Keller pair over \(\mathbb C\). The Padé test killing one completion is being over-read if one says “residue-A cannot algebraize”: the unpinned tails are exactly where an exceptional algebraic completion would hide, as the algebraization note itself warns. The disproof lane is real. It is also the lane in which the campaign has the most compute and the least theorem.

---

## 25. Collision ideals and “no hidden inertia”

**(a)** Encode non-injectivity as an ideal of collisions; show that \(J\in\mathbb C^*\) forces the collision ideal to be \((1)\) except on a locus that “hidden inertia” would have to occupy; axiomatically exclude hidden inertia.

**(b) Not tried.** Watched: chloeallegra228, GitHub `what-social-construct/collision-ideals`, Lean 4, explicitly conditional on unproved `PlanarNoHiddenInertia` (`RECON.md`). Not on arXiv.

**(c) Hollow.** The axiom *is* JC2, or a close relative (no unexpected sheets). Formalizing the rest in Lean does not move the mathematics. The collision-ideal language is a reasonable *reformulation* (the fiber product of \(F\) with itself off the diagonal); the campaign already meets the same object as “generic fiber cardinality \(td\).” There is no new obstruction.

**(d) Experiment:** read the Lean axiom and write it in ordinary algebraic geometry in one page. If it is “the map is quasi-finite and étale implies injective in dim 2,” stop. **Promise: 2.**

---

## 26. Spectral surfaces and commuting PDOs (Parshin–Zheglov–Kurke)

**(a)** In one variable, Burchnall–Chaundy + Schur + Wilson’s adelic Grassmannian coordinatize commuting ODOs; Zheglov’s DC(1) lives there. In two variables, commuting PDOs correspond (conjecturally) to spectral *surfaces* plus sheaves. Build that dictionary and run a DC(2)/JC(2) contradiction on the surface side.

**(b) Not tried.** Named as the missing theory in `DC2-PROGRAM.md` §2 (“incomplete and partly conjectural”).

**(c) Stuck at the existence of the theory.** This is someone else’s research program (Zheglov, Kurke, Osipov), decades old, not a JC2 tactic one “attempts.” Using an incomplete dictionary to prove DC(2) is how one writes a 78-page preprint with a moving endgame.

**(d) Cheapest experiment.** Take one explicit commuting pair of PDOs in two variables (e.g. a trivial tensor of two 1-variable BC pairs) and check whether any deformation with \([Q_i,P_j]=\delta_{ij}\) exists to first order in the Bernstein filtration that is *not* Hamiltonian. This is a linear PDE / linear algebra problem on symbols of degree \(\le 3\), i.e. a rewrite of the DC(2) degree-3 slice the campaign already ran. **Promise: 3.** The slice is the experiment; the “spectral surface” language does not cheapen it.

---

## 27. Global symplectic exactness / Keller action residues

**(a)** \(J(f,g)=1\) iff \(f\,dg-x\,dy\) and \(g\,df-y\,dx\) are closed, hence (polynomial Poincaré lemma) exact. Residues of the primitives on fibers force vanishing of specific Puiseux coefficients (the “no-log” / level-\(\kappa\) pins). Promote this from a local pin to a global identity that cannot be satisfied unless the map is tame.

**(b) Pins used; the global lemma not run as a JC2 proof.** `xmodel/sol-avenues2.md` wrote the exact residue calculation (\(\mathrm{Res}(y\,dx)=-\kappa c_\kappa\)) and proposed appending six level-42 pins to the D21 system. Those pins are in the residue-A lore (`PIN42`). The campaign did not, as far as the repo shows, write a global argument that the two polynomial primitives’ existence forbids dicritical structures of type \((2,3)\) at \(td=6\).

**(c) Local obstruction.** On \(\mathbb A^2\) the Poincaré lemma *always* produces polynomial primitives for closed polynomial 1-forms. That is true for automorphisms and for counterexamples alike. The residue vanishing \(c_\kappa=0\) is a *normalization* of the local parameter, or a genuine constraint on a *badly normalized* series — it is not, by itself, a contradiction. Treating it as a “kill instrument” is the overclaim `sol-avenues2` already labeled as such. The global content would have to be a comparison of the two primitives \(f\,dg-x\,dy=dF\), \(g\,df-y\,dx=dG\) with the compactification, e.g. an adjoint/Rosenlicht residue at infinity that sees more than \(c_\kappa\).

**(d) Cheapest experiment.** For the elementary automorphism \((x,y+x^n)\) and for a tame product of two elementaries of degrees \(3,4\), compute the primitives \(F,G\) explicitly and their polar residues at infinity in the standard compactification. Then do the same formally for the residue-A leading pair (without tails). If the polar divisor of \(F\) is already illegal for the \((2,3)\) genome, one has a leading-form kill independent of Sigray. If it matches, the primitives see no more than \(J=1\). **Promise: 6.** Highest untried score: the identities are exact, cheap, dimensionally 2-specific (Poincaré lemma + 1-forms), and not a rewrite of Eggers–Wall combinatorics. The risk is that they are *only* \(J=1\) in costume. The experiment is designed to detect that.

---

## 28. Bézout, BKK, and mass inequalities as a \(td\) ceiling

**(a)** \(td \le \deg f\cdot\deg g\) by Bézout on a compactification; sharpen to \(td\le mn\) in Sigray type \((m,n)\), or to \(\sum a_F b_F/\nu_F\le 1\), and thereby bound \(td\) absolutely.

**(b) Tried as a conjecture, evidence downgraded.** `TDBOUND.md`: CONJECTURE TD-BOUND unfalsified but coincidence-risk; 21/22 “violations” largely forced by census construction. Reformulation \(\sum a_F b_F/\nu_F\le 1\) or \(\Delta^2\ge -2\) names a missing Jacobian/proximity lemma at divergence centers. The one below-bound td-12 entry died cheaply by other means; the equality case is residue-A.

**(c) Stuck.** Bézout *in terms of \(\deg f,\deg g\)* is true and useless as a JC2 bound (degrees are unbounded a priori). An absolute bound on \(td\) independent of degrees would finish the sheet program’s missing G5 (`REDUCTION.md`). The mass inequality is a restatement, not a proof. FC5 does not telescope to it (`xmodel/sol-avenues3.md`). This is the campaign trying to will a ceiling into existence because the runway ends at 9.

---

## 29. Pinchuk maps and the real Jacobian conjecture

**(a)** Pinchuk constructed real polynomial maps \(\mathbb R^2\to\mathbb R^2\) with \(J>0\) that are not injective. The real JC is false. Study why Pinchuk maps do not complexify to a complex Keller counterexample, and turn the obstruction into a complex proof — or deform a Pinchuk map in a way that complexifies.

**(b) Not tried.**

**(c) Field fact.** Pinchuk maps have nonconstant Jacobian (positive, not constant) in the usual presentations, or at any rate they are not polynomial automorphisms of \(\mathbb C^2\) upon complexification: complexification of a non-injective real map may become dominant of degree \(>1\) with *nonconstant* Jacobian, or fail to be Keller. The real counterexamples live in a different equation. The useful question is the *obstruction to holding \(J\) constant* while keeping real non-injectivity.

**(d) Cheapest experiment.** Take a standard Pinchuk example, compute \(J\) as a polynomial, and Gröbner the condition that a bounded-degree perturbation (real coefficients) makes \(J\) a nonzero constant. If the only solutions have \(J\) constant *and* are injective over \(\mathbb R\) (hence tame), Pinchuk cannot be deformed into a real-Keller non-injective map at that degree. That is expected (real Keller with constant \(J\) is still open in some formulations, but constant \(J\) over \(\mathbb R\) plus complexification would be a complex Keller map). **Promise: 3.** Good hygiene; unlikely to yield JC2.

---

## 30. Ritt theory: one coordinate is composite

**(a)** If \(f=a\circ b\) with \(\deg a,\deg b>1\), Ritt’s decomposition theory plus \(J(f,g)=1\) should force a tame reduction. Reduce to \(f\) prime in the Ritt sense.

**(b) Not tried.**

**(c)** Keller maps that are automorphisms *can* be composite (e.g. \(x+y^n\) composed with affine). For a counterexample, Abhyankar divisibility already says \(\deg f\nmid\deg g\) and vice versa, so both are “prime” in a coarse degree sense. Ritt’s theorem is about composition in one variable. A two-variable polynomial can be composite in more ways (coordinate changes). After reducing by Aut, this tends to become “leading forms are powers,” which is GGV again.

**(d) Cheapest experiment.** On GGV family tables, mark which admissible degree pairs have a nontrivial Ritt decomposition of the *univariate* leading-edge polynomials, and check that the campaign’s surviving polygons are Ritt-prime on both edges. If a surviving family is composite on an edge, a new reduction exists. **Promise: 3.**

---

## 31. Finite-field census

**(a)** Enumerate polynomial maps \(\mathbb F_q^2\to\mathbb F_q^2\) of degree \(\le d\) with \(\det J\in\mathbb F_q^*\), count how many are bijective, compare to \(|\mathrm{AGL}|\) times tame generators, look for extras.

**(b) Not tried.** Fiber histograms in `MONDELLO-CHECK.md` are for one map, not a census.

**(c)** In char \(p\), \(J\in\mathbb F_q^*\) does not mean étale in the same way as char 0 (Frobenius, inseparable phenomena). Separable JC is the right analog and is false (Mondello). A census will find extras. They will not lift (§17). Over large \(q\) in char 0 residue fields, enumerating degree-\(d\) maps is impossible past tiny \(d\).

**(d) Cheapest experiment.** Exhaustive census over \(\mathbb F_5\) of maps with total degree \(\le 3\), Jacobian a unit, and report bijectivity. Degree 3 over \(\mathbb F_5\) is small enough to enumerate by affine gauge-fixing. **Promise: 2.** Will rediscover that char \(p\) is a different problem.

---

## 32. Markus–Yamabe and chain-realization of Keller maps as vector fields

**(a)** Markus–Yamabe: a vector field on \(\mathbb R^n\) whose Jacobian at every point has eigenvalues in the left half-plane has a unique global attractor. True for \(n=2\) (Fessler, Gutiérrez, Glutsyuk), false for large \(n\). Castañeda–Honorato–Valenzuela-Henríquez (arXiv:2608.05392) turn Keller maps into Hurwitz vector fields whose singularities biject with a fiber. A dim-2 converse might constrain plane Keller maps.

**(b) Not tried.** Flagged as periphery in `RECON.md`.

**(c)** MY(2) is a theorem about *real* vector fields with a spectral hypothesis, not about polynomial maps with constant Jacobian. The chain-realization *uses* a Keller counterexample to kill MY in dimension 14. The arrow points the wrong way. A converse “every plane Keller map gives an MY field with one singularity, hence is bijective” needs the spectral hypothesis, which constant Jacobian \(=1\) does not give (eigenvalues of \(JF\) need not have negative real part).

**(d) Experiment:** compute the eigenvalues of \(JF\) for elementary automorphisms and for Pinchuk maps; observe they do not satisfy Hurwitz. Stop. **Promise: 2.**

---

## 33. Tropical geometry beyond Newton polygons

**(a)** Tropicalize a Keller map as a piecewise-linear map \(\mathbb R^2\to\mathbb R^2\), constrain by \(\det = 1\) as a tropical volume condition, and classify tropical Keller maps.

**(b) Not tried under that name.** Newton polygons, \((\rho,\sigma)\)-gradings, and Minkowski sums *are* the tropicalization of the pair. The campaign lives there already (§1, §3).

**(c)** Fashionable renaming. Tropical \(\mathrm{SL}_2\) maps are linear (or at least piecewise \(\mathrm{SL}_2\)), which is the leading-form story. The discrepancy between tropical invertibility and algebraic invertibility is the tail — i.e. §§2–4. There is no extra tropical invariant that does not already have a Newton name.

**(d) Cheapest experiment.** Tropicalize \([P,Q]=1\) as a condition on the mixed volume of faces and check it reproduces GGV’s vertex-determinant \(\pm 1\) condition. If yes, stop. **Promise: 2.**

---

## 34. Hodge theory, algebraic K-theory, anabelian geometry, derived / prismatic / crystalline slogans

**(a)** Some cohomology theory of \(\mathbb A^2\) or of \(\mathrm{Aut}\) or of the graph compactification carries an obstruction to a non-proper étale endomorphism.

**(b) Not tried.** Correctly. `xmodel/sol-lateral-prompt.md` already warned: “Apply anabelian geometry without a …” is the failure mode.

**(c) Hollow unless a specific class is named.** Mixed Hodge structures of \(\mathbb A^2\setminus C\) are those of a plane curve complement: they know the mixed Hodge of the cohomology of the curve, which is the compactification again (§21). \(K_1(\mathbb C[x,y])\) / \(SK_1\) will not see a finite étale endomorphism. Anabelian reconstruction of \(\mathbb A^2\) from \(\pi_1\) is a theorem about schemes, not about endomorphisms. Prismatic/crystalline cohomology in char 0 is a language for the Witt obstruction of §17; without an actual class (the campaign *did* write one, \(o_2(F)\in H^2_{\mathrm{dR}}(\mathbb F_2[x,y])\)) it is noise. I include this cluster because outsiders will propose it, and because post-2026 AI-math culture rewards the vocabulary.

**(d) Experiment:** refuse to start until the proposer writes a 10-line definition of the actual cohomology class that vanishes for automorphisms and, on residue-A leading data or Mondello, does not. The Witt class already exists; compute its analog for \(W_2(\mathbb F_3)\) on a random degree-4 Keller pair over \(\mathbb F_3\). That is §17, not this section. **Promise: 1.**

---

## 35. Lean / LLM proofs conditional on unproved axioms; “AI will settle JC2 shortly”

**(a)** Formalize a purported proof, or search for a proof with an LLM, or register a Palomar/Lean artifact.

**(b) Not tried as a proof method.** The campaign uses machine exact arithmetic and adversarial review, which is a different thing. Watched and correctly dumped: Reed’s JvdK Lean “resolution”; chloeallegra228’s axiom; Fortune-Didier “bidegree-extinction strategy” (`xmodel/websweep-2026-08-21.md`); Santibañez-Leal mass-output Zenodo. Long publicly predicted an AI+expert proof “shortly” while reporting his own attempts “probably too difficult for current AI” (`RECON.md`).

**(c) Hollow as a *route*.** Formalization can certify a finished proof (good) or launder an axiom (bad). LLM search without a program is what this repo *is*, except the campaign picked programs. Treating “more AI” as an approach to JC2 is the fashionable answer the charge asked me to be hostile to. The July 2026 dim-3 counterexample *was* AI-assisted and real; the plane is the case where the same style has already produced a residue-A nonempty scheme and a pile of Zenodo. Those are not the same outcome.

**(d) Experiment:** none. **Promise: 1** as a standalone approach. (As a labor multiplier *inside* a real program, it is already priced into every other score.)

---

## 36. Holomorphic Jacobian conjecture, Fatou–Bieberbach, univalent functions

**(a)** Replace polynomials by entire maps \(\mathbb C^2\to\mathbb C^2\) with \(J\equiv 1\); or import 1-variable univalence criteria.

**(b) Analog is false.** Fatou–Bieberbach: there exist injective holomorphic maps \(\mathbb C^2\to\mathbb C^2\) whose image omits nonempty open sets; they can be arranged with Jacobian 1. The holomorphic JC is false. One-variable Bieberbach/univalence is a different subject.

**(c)** The polynomial condition is the entire content. Methods that do not use polynomiality (or at least rational properness at infinity) cannot distinguish JC2 from a false statement. **Promise: 1.** Included because the analogy is repeatedly proposed.

---

## 37. Moskowicz: no Keller map of prime field-extension degree

**(a)** arXiv:2407.13795 (8pp, unpublished) claims no Keller map has prime \(td\). Then \(td\ge 6\) plus not-prime would leave \(6,8,9,\ldots\) and kill 7.

**(b) Not tried.** Flagged in `SHEET6.md` as unvetted.

**(c)** If true, it would be a genuine \(td\)-parity/primality constraint and would make the campaign’s td-7 tower work *optional*. An 8-page unpublished claim of that strength is almost certainly wrong or conditional on JC2. Prime \(td=3\) *exists* in char 2 (Mondello). Any proof must use char 0 in an essential way.

**(d) Cheapest experiment.** Read the 8 pages. Extract the first lemma that is not a restatement of known Abhyankar divisibility. Test that lemma on Orevkov’s holomorphic \(td=9\) example (not a global polynomial automorphism, but a local-at-infinity Keller object) and on a tame automorphism (td=1, not prime, should be out of scope). If the lemma already fails on a tame pair’s perturbation or on a standard 3-sheeted Orevkov configuration, dump it. **Promise: 2.**

---

## 38. Differential Galois theory of the inverse

**(a)** The formal inverse satisfies a differential equation coming from \(DF^{-1}=(DF)^{-1}\circ F^{-1}\). If the inverse is Liouvillian / Darbouxian / has finite differential Galois group, force it to be polynomial; if not, derive a contradiction from \(J=1\) in dimension 2.

**(b) Not tried.** Adjacent: Żołądek’s use of Darboux / Liouville on the ODE \(AC'-wA'C=c\) (`MATHIEU.md` priority note) is a *univariate* differential-algebra argument, already consumed.

**(c)** The inverse’s differential equation is tautological from the chain rule. In several variables, differential Galois theory is not a finished machine (Malgrange’s Galois groupoid, etc.). Reducing to the univariate ODEs along a pencil is, again, Żołądek charts.

**(d) Cheapest experiment.** Restrict the inverse PDE to a generic line \(y=tx\), obtain an ODE for the inverse components as Puiseux series in one variable, and run a Kovacic-style algorithm at low degree. Compare with Żołądek A.7; if the output is A.7, stop. **Promise: 3.**

---

## 39. Height bounds and small-coefficient search

**(a)** If a counterexample exists, there is one of bounded bit-size (by effective Nullstellensatz on the complement of Aut inside the Keller variety, if that complement were Zariski-constructible of known degree). Search small-height maps.

**(b) Not tried.** The farm searches *supports*, not heights.

**(c)** The Keller variety contains Aut, which has maps of unbounded height and degree. There is no effective “smallest CE” bound without already knowing Aut is the whole Keller variety — i.e. JC2. Searching height-1 coefficients on GGV-admissible supports is a sub-case of §1/§18.

**(d) Experiment:** brute-force \(\{-1,0,1\}\)-coefficients on the smallest GGV family that is not already emptied, with torus gauge-fixing. That family is below degree 125 and should be empty. A hit is a GGV/transcription bug. **Promise: 2.**

---

## 40. Lagrangian generating functions (2-dimensional Hamilton–Jacobi)

**(a)** A map \(\mathbb C^2\to\mathbb C^2\) with Jacobian 1 is (locally) symplectic for \(dx\wedge dy\). Exact symplectic maps have generating functions \(S(x,Y)\) with \(y=S_x\), \(X=S_Y\). Polynomiality of the map becomes a functional equation on \(S\). Classify polynomial generating functions.

**(b) Not tried.** Related to §27 (primitives of \(f\,dg-x\,dy\)).

**(c)** Generating functions are local and typically involve mixed old/new coordinates; polynomiality in \((x,y)\) does not give polynomiality of \(S\). For automorphisms, \(S\) can still be polynomial (e.g. elementary maps have cubic \(S\)). The classification of polynomial \(S\) producing polynomial maps is plausible in dimension 2 and might be equivalent to JvdK.

**(d) Cheapest experiment.** Write \(S\in\mathbb C[x,Y]\) of degree \(\le 4\), form \((X,y)=(S_Y,S_x)\), impose that \(x,y\) can be expressed as polynomials in \(X,Y\) (Gröbner elimination), and list the maps. Expected: tame automorphisms of degree \(\le 3\). Push to degree 6. If only tame maps appear, one has computational JvdK in the generating-function chart up to that degree — not news, but a clean test that the chart sees only Aut. **Promise: 3.**

---

## Cross-cutting judgments (hostile)

**The implication-ladder instinct is exhausted.** Mathieu, GMC(\(n\ge 3\)), Hessian, PC(2), JC(\(n\ge 3\)) are false. DC(2) remains, and is harder. Conjecture E remains, and is messier. “Prove a stronger statement” has been the wrong bet for thirty years and is now a documented massacre.

**The campaign’s real theorems are in §3 (and transport, Prop 5.8, some tower combinatorics).** Its real *settlement* is §1 at \((72,108)\), shared with Helali/Suzuki. Its labor is in §2+§4, which is a necessary-condition mill without a \(td\) ceiling and without a landing theorem.

**The fashionable dim-3 geometry does not descend.** Anyone still looking for a “plane Alpöge” without a new 2-dimensional mechanism is doing tourism.

**Formalization is not an approach.** Neither is “more compute on D\(n+2\).”

**The two untried directions I would actually spend a week on, if this were my campaign and I were forbidden to continue residue-A F4 jobs:** §27 (global primitives / residues — cheap, 2-specific, falsifiable on leading forms) and §5/§23’s weekend negative controls (cusp-versus-Jung words; primitive groups versus Orevkov \(td=9\)). Everything in the 1–2 band is listed so that it is not “rediscovered” as a fresh idea next month.

**Disproof.** The only disproof lanes that are not fantasies are: (i) a nonempty GGV family with a char-0 point that algebraizes (§1 dual), (ii) a certified germ at infinity that algebraizes (§24), (iii) a Witt-unobstructed char-\(p\) pair that lifts (§17). The campaign has run (i) below 125 and found empty, run (ii) and found modular nonempty *windows* rather than germs, and run (iii) on Mondello’s support and found total obstruction. That is consistent with JC2 being true. It is also consistent with the counterexample living at \(td\ge 9\), off every current book, with a Newton polygon past the farm’s memory envelope. The sheet program cannot see that object. The farm, in principle, can — slowly, never as a proof.

---

## What I did not count as a top-level approach

- Per-cell tower certificates, NF-M/P/Z/D, e-ladder primitivity, zero-chain laws, H29 dichotomies, ECO carrier–obstruction, 36-character splits: tactics inside §2+§4.
- Dual-build / msolve-parenthesis / FLINT ports: engineering.
- Palomar registration, Leiden norms, GGV email: publication.
- Wang degree 2, Moh 100, Żołądek/Sigray \(td\le 5\): theorems, not approaches still available to take.
- “Assume JC2 and derive a contradiction with something unrelated” without a mechanism.
