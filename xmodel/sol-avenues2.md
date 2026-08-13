# Fresh proof/disproof avenues after the depth-21 and off-axis repairs

## Executive summary — five lines

1. The best new lever is exact: Keller symplectic exactness forces the level-\(\kappa\) coefficient of every infinity series to vanish; at sheet 6 this gives nine level-42 pins, six of them immediately usable in the live residual system.
2. The best direct attack on the nonlinear depth-21 survivor is to restore the toric relations discarded by the successful 5,106-column monomial relaxation; exact inconsistency would kill, while a reconstructible point would seed a disproof lift.
3. The cheapest off-axis reducer is a proof-level classification of equality in every summand of Statement 9.4, aimed at the 1,390 exact-budget \(td=7\) routes; the sharp \((10,15)\) route is an important negative control.
4. Two more global proof tests are worth pilots: Mittag-Leffler/adjoint compatibility of the Keller primitive and a genuinely gauge-free, depth-invariant coefficient holonomy—not another per-cell T1 solve.
5. The explicit disproof lane is to positively lift a surviving exact-fit off-axis cell through successive Puiseux/Jacobian windows; the remaining multibranch-semigroup idea is cheaper but much more speculative.

## State calibration and ranking

Two checked repository facts postdate or qualify the state in the prompt.

- `SHEET6-DIRECTIONB.md` §6.V records the 83-tail-variable depth-21 window as **completed and NOT EMPTY-BY-KILL**: the 77-by-5,106 independent-monomial relaxation is consistent, the tangent and the closed-form affine strata are inconsistent, and the honest survivor is a nonlinear residual with roughly 28 low parameters and 32 conditions. The emitted charted system has 84 variables. Depth 23 was running when that section was written. I therefore do not propose building the depth-21 window again.
- `BOOK-OFFAXIS.md` §10 P5 explicitly voids the old \(td=11:12\) and \(td=13:129\) stage-R counts as alphabet artifacts. I treat 12/129 as campaign-designated target labels if they reflect newer unfiled state, not as certified counts from the checked repository. The honest, fully priced object used below is \(td=7\): 62 cells, 1,689 routes, 1,390 exact-budget routes, and 299 routes with slack (`BOOK-OFFAXIS.md` §10 P4).

The score is a qualitative \((\text{chance of useful new codimension}\times\text{payoff})/\text{one-week cost}\) index, not a calibrated probability.

| rank | avenue | side | useful-codimension chance | payoff | first-week cost | ratio score |
|---:|---|---|---|---|---|---:|
| 1 | Keller action residues / level-42 no-log pins | proof | high | very high | very low | 9.3 |
| 2 | Toric-circuit closure of the monomial relaxation | dual | medium | very high | medium | 7.1 |
| 3 | Termwise equality classification in Statement 9.4 | proof | medium-low | high | low | 6.5 |
| 4 | Mittag-Leffler and Rosenlicht-adjoint obstruction | proof | medium-low | very high | medium-high | 5.8 |
| 5 | Gauge-free, depth-invariant coefficient holonomy | proof | low-medium | high/uniform | low-medium | 5.1 |
| 6 | Positive formal lift of an exact-fit off-axis cell | **disproof** | low | enormous | high | 4.7 |
| 7 | Multibranch Gorenstein value-semigroup symmetry | proof | low | high | low pilot | 3.0 |

An immediate cleanup is deliberately **not** ranked as a fresh avenue. The sole class-B \((3,9)\) cell has \(p=R\), \(q=Rs\), \(\deg R=3\), and \(\deg s=6\), so its T1 equation is \(Rs'-2R's=c\ne0\); Theorem A forces \(\deg R\le1\). This kills that cell, but it is exactly the already-banked family-I integer-ratio mechanism (`MATHIEU.md` §5 and `BOOK-BASH-R2.md`), not a new method. The fresh off-axis work below is aimed primarily at the 61 class-C cells.

## 1. Keller action residues give exact level-42 no-log pins

**Label: EXACT LEMMA; SPECULATIVE only as a standalone depth-21 kill.**

### (a) Idea — five lines

1. From \(J(f,g)=1\), both \(f\,dg-x\,dy\) and \(g\,df-y\,dx\) are closed polynomial one-forms.
2. Polynomial de Rham exactness on \(\mathbb A^2\) gives polynomial primitives for both forms.
3. On a fibre \(f=a\), \(y\,dx\) is exact; on a fibre \(g=b\), \(x\,dy\) is exact.
4. If \(x=t^{-\kappa}\) and \(y=\sum_m c_m t^m\), the relevant residue is \(\pm\kappa c_\kappa\), hence \(c_\kappa=0\).
5. At sheet 6, \(\kappa=42\), so this pins the very level-42 tails used by the nonlinear escape from \(0=-42\).

### (b) Why it could work here

The calculation is short and exact:

\[
d(f\,dg-x\,dy)=(J-1)\,dx\wedge dy=0,
\qquad
d(g\,df-y\,dx)=(1-J)\,dx\wedge dy=0.
\]

On \(f=a\), the second identity makes \(y\,dx\) exact, and

\[
\operatorname {Res}(y\,dx)
=\operatorname {Res}\!\left(-\kappa\sum_m c_m t^{m-\kappa-1}dt\right)
=-\kappa c_\kappa.
\]

The first identity gives the analogous statement on \(g=b\). This is one condition per analytic place—not 42 independent conditions from the conjugate series—but the orbit generators used by the campaign expose those coefficients directly. In the current notation the full sheet-6 consequences are

\[
\begin{aligned}
f\text{-root series: }&tf1_{42}=tf2_{42}=bf_{42}=0,\\
g\text{-root series: }&tg1_{42}=tg2_{42}=tg01_{42}=tg02_{42}
=bg42_{42}=bg21_{42}=0.
\end{aligned}
\]

For a size-21 orbit written in \(u=t^2\), this is the \(u^{21}\) coefficient. The P1/P2 equations are unambiguous; the B-place parameter normalization should be guard-checked before the last three equations are banked.

Six of the nine variables occur in the emitted depth-21 object:

\[
tf1_{42},tf2_{42},tg1_{42},tg2_{42},tg01_{42},tg02_{42}
=x46,x51,x56,x61,x64,x67.
\]

The current Row 10 has only rank two on this six-variable block, so these are not already present as six independent rows. They remove part of the level-42 quadratic escape that `SHEET6-DIRECTIONB.md` §6.T says must cooperate with levels 38–41 to cancel the six obstruction characters \(\eta^{12},\eta^{15},\ldots,\eta^{27}\). The number 42 is therefore not cosmetic: it is simultaneously the pole order in \(x=t^{-42}\), the residue selector, and the source of the inhomogeneous \(-42\) Jacobian row. The rigid \(2\pm\sqrt3\) pole pair supplies two separate placewise equations rather than only a Galois-symmetric sum.

The same lemma is depth-independent and applies to every off-axis genome once its \(\kappa\) is known. On the x-side expansion from `SHEET6-CLASSICAL.md` §0,

\[
x=c'_0+c'_1y^{-1}+c'_2y^{-2}+\cdots,
\]

exactness of \(y\,dx\) also gives \(c'_1=0\) at every x-place. Thus the lemma can couple to the still-unpinned x-tail and to exact-budget off-axis routes without any new \(\lambda\)-charge.

A cheap read-only pre-screen already rules out overoptimism: after all six P-side substitutions, the independent-monomial relaxations remain consistent (Row 20: 10-by-2,295, rank 10; full reduced window: 76-by-4,351, rank 56). The nonlinear residual—not another rank test—is the correct target.

Relevant anchors: `SHEET6-DIRECTIONB.md` §§1, 3, 6.T–6.V; `cases/directionb_residual32.rows.txt`; `cases/r1_experiment.py` around the P1/P2/B root-series registry; `SHEET6-CLASSICAL.md` §0.

### (c) First concrete computation this week

Append the six exact residue rows to the already guard-certified `cases/directionb_residual32.ms`, rerun every round-trip/pattern/saturation guard, and screen the three banked good primes. Emit an independently hard-substituted twin and require matching verdicts.

- Append-only system: 84 variables, 85 \(\to\) 91 equations, 79,590 \(\to\) 79,596 expanded terms; about 2.0 MB.
- Hard-substituted twin: 78 variables, 84 equations, 67,717 terms; Row 10[\(\eta^{28}\)] becomes identically zero and drops.
- If either modular screen looks empty, demand an exact characteristic-zero Gröbner/Nullstellensatz certificate before promotion.
- In parallel, add the remaining B-side three pins to the Q2/R1 emitters conceptually—not by mutating them during this experiment—and check whether they remove the currently expensive low-slot components.

This is an hours-to-one-day launch; the nonlinear solve may of course run longer.

### (d) Kill criterion for the avenue

The lemma itself should never be abandoned. Abandon only the claim that its six D21 rows are a standalone killing instrument if the augmented saturated system has a certified characteristic-zero point, or a verified smooth \(\mathbb Q_p\) point with a complete Hensel lift. A merely nonempty reduction at one or two primes is only a deprioritization signal. Even after a standalone failure, retain all nine no-log rows permanently in depth 23+, Q2, and off-axis builds because they are exact and essentially free.

## 2. Restore toric circuits discarded by the depth-21 relaxation

**Label: SPECULATIVE DUAL PROOF/DISPROOF ALGORITHM.**

### (a) Idea — five lines

1. The 5,106-column test replaced every occurring tail monomial by an independent variable \(z_e\).
2. Genuine monomial values lie on a sparse toric image and satisfy \(z_u z_v=z_{u'}z_{v'}\) whenever \(u+v=u'+v'\).
3. Add short quadratic circuits to the affine linear Row 6–20 solution space before attempting the full 28-variable Gröbner problem.
4. Exact inconsistency of even a subset of valid circuits is a sound proof of emptiness.
5. A reconstructible circuit solution, checked back in the original tails and then extended to rows 21/22, is a disproof-side seed.

### (b) Why it could work here

`SHEET6-DIRECTIONB.md` §6.V identifies the exact gap: the \(-42\) target lies in the span when monomials are independent, but not in the differential at the zero-tail point. Hence every actual solution must exploit nonlinear dependencies among the low tail monomials. Toric circuits attack precisely the dependency erased by the successful relaxation; they are not another unconstrained monomial rank calculation and not the monolithic residual32 Gröbner run already staged.

The \(\mu_{42}\)-character grading separates the ten Row-20 components, while the \(\mathbb Q(\sqrt3)\) pole swap separates symmetric and antisymmetric circuit blocks. The six obstruction characters \(12,15,18,21,24,27\) give a principled sparse-circuit priority. Depth conservation fixes the discrete exponent alphabet, so circuits found at depth 21 remain valid when rows 21/22 arrive.

There is an important soundness asymmetry. Any subset of genuine toric binomials still contains the true monomial image, so characteristic-zero UNSAT is a valid kill. SAT for a partial circuit set says almost nothing: boundary points and missing high-degree toric relations can be spurious. Include \(z_0=1\), all available degree-one coordinates, and the intended nonzero-chart saturations from the start. A modular UNSAT result is evidence only until lifted to a characteristic-zero certificate.

Relevant anchors: `SHEET6-DIRECTIONB.md` §6.T (2,034 Row-20 monomials and the six obstruction characters) and §6.V (5,106-column relaxation and nonlinear residual); `TEMPLATE-ATTACK.md` §4 only as a reminder that this is unrelated to the failed Galois/quantum shields.

### (c) First concrete computation this week

Export exponent vectors for the 2,034 monomials in Row 20, canonicalize coefficients separately from exponents, and hash all unordered pair sums. That is about 2.07 million pair hashes before character and pole-swap splitting. Retain a sparse basis of collisions that touches the six obstruction characters, substitute the existing affine row-echelon parametrization, and run the resulting quadratic system at \(p=105337,105673\), plus one fresh good prime.

Expected pilot size: \(10^4\)–\(10^5\) short circuits after deduplication, hours of generation/selection, and less than roughly 10 GB if stored sparsely. If it gains codimension, enlarge from Row 20 to the reduced 47-band support. If a finite-field point appears, reconstruct every \(z_e\) from the degree-one tail coordinates and verify all original Row 6–20 equations before calling it a candidate; only then append rows 21/22 and try Hensel continuation.

### (d) Kill criterion for the avenue

Abandon the **short-quadratic-circuit** route if the selected circuits add zero codimension at three good primes, no short circuit couples to the six obstruction characters, and the first cubic-circuit census is projected to exceed \(10^7\) relations. That does not certify survival and does not invalidate the full toric ideal; it says this low-cost approximation has no leverage. Conversely, do not call a partial-circuit SAT point a disproof seed unless it reconstructs to the original tail coordinates exactly.

## 3. Classify equality in every summand of Statement 9.4

**Label: SPECULATIVE PROOF-SIDE; new off-axis deployment of a known strictness surface.**

### (a) Idea — five lines

1. Re-read the proof of Statement 9.4 and expose every nonnegative local defect hidden behind each \(\lambda\), ceiling, cv-subtree, and terminal \(\psi\) bound.
2. An exact-budget route can exist only when every one of those local inequalities is an equality.
3. Classify equality from the actual multiplicity, gap, direction type, and eventual cv-fibre data—not merely from the scalar route budget.
4. One forced strict unit kills every exact-fit route with the same local signature.
5. Quotient signatures by the conserved depth variable \(w=(\bar\kappa-\rho)/\nu\), so arbitrary neutral depth does not create an infinite audit.

### (b) Why it could work here

The honest \(td=7\) book has 1,390 exact-budget routes out of 1,689. Those routes cannot absorb even one additional unit; the 299 slack routes can. This makes proof-level equality classification much sharper here than another budget recomposition. The latter has already been exhausted on the residue-A template (`TEMPLATE-ATTACK.md`); the proposed object is the equality case of every constituent ramification estimate on the repaired off-axis routes.

The depth invariant collapses all neutral chain repetitions to finitely many charged transition signatures. Exact cell data fixes the gaps and multiplicities. Thus a strictness lemma, even one covering only repeated NE multiplicities or a terminal \(k_f>\deg p_G\) sector, could delete a large route fraction without solving Prop. 8.1(iv).

There is strong negative evidence that must be built into the pilot. The sharp class-C route is

\[
(w,M)=(3/2,2)
\xrightarrow[(d_p,d_q)=(21,15)]{\lambda=2}
(2/3,3)
\xrightarrow[\mu_0=3,\nu_H=7]{\text{merge}}
(\bar\kappa,X,d_p,d_q,\nu_G,M_G)=(6,4,10,15,7,5),
\]

followed directly by \(w=4/5\), \(\psi=4\), so \(2=td-1-\psi=\sum\lambda\). Its sole charged A-step has a multiplicity-one NE orbit and lies in the proved equality case of the current Prop. 7.3 estimate. The \(\mu_0=3\) zero-direction is an **arriving pole direction**, not a free zero-root, and the merge currently costs zero. Therefore “\(\mu_0\ge2\) automatically gives +1” is not a valid proposed lemma. This avenue is more likely to be a powerful classifier than a universal one-line kill.

The \(-42\) and \(2\pm\sqrt3\) structures do not enter this audit; that orthogonality is a virtue. Relevant anchors: `BOOK-OFFAXIS.md` §10 P0–P4, especially the \((10,15)\) route and the equality/slack totals; `SHEET6-LROOT.md` equality/\(\delta\)-strictness discussion; `SHEET6-DEPTH.md` §§1 and 7.

### (c) First concrete computation this week

Instrument the current \(td=7\) adjudicator to emit, for every route, a provenance record

\[
(\text{vertex type},\nu,\epsilon,l,(m_j),\bar\kappa,X,
\text{gap},\text{eventual fibre multiplicity},\text{charged summand}).
\]

Start with the 1,390 exact routes, but regenerate the route JSON first: the main verdict and prompt say 1,390, while a reproduction comment in the same file reports a different exact-fit subtotal. Each route has at most five positive-cost vertices, so 6,950 charge records is a safe upper bound before hashing. Run local gcd, discriminant, and jet/ramification checks only on distinct signatures. Current cell degrees are at most 297, so this is comfortably a 1–3 day computation; pilot \((10,15)\), then one representative of every signature.

### (d) Kill criterion for the avenue

Abandon it as a **universal off-axis closure** if the \((10,15)\) route has a complete zero-defect equality model and every remaining exact-fit signature also realizes all local equalities, or if every apparent repeated multiplicity occurs only on arriving pole directions to which the proof assigns no defect. Retain any certified strict signatures as partial kills; do not force a universal theorem if the balanced route is genuine.

## 4. Global Mittag-Leffler/adjoint compatibility of the Keller primitive

**Label: SPECULATIVE PROOF-SIDE; exact premise, speculative finite extraction.**

### (a) Idea — five lines

1. The no-log lemma gives a local meromorphic primitive \(T_P=\int x\,dy\) at every infinity place of \(C_a=\{f=a\}\).
2. For a Keller pair, these local principal parts come from the single global function \(ag-S\), where \(dS=f\,dg-x\,dy\).
3. Mittag-Leffler/Serre duality says they glue only if \(\sum_P\operatorname{Res}_P(T_P\omega)=0\) for every holomorphic differential \(\omega\).
4. Represent \(\omega\) by Rosenlicht adjoints \(H(x,y)\,dx/f_y\) and evaluate the pairings on the existing Puiseux jets.
5. This tests a distinguished primitive on the fibre, not merely the realizability of its degree-six monodromy passport.

### (b) Why it could work here

The placewise level-42 equation is only the local absence of a logarithm. Global principal-part compatibility is stronger. The P1/P2 principal parts are unusually rigid because their coefficients are tied by \(a_1/a_2=2\pm\sqrt3\); the \(-42\) chart fixes the integration index exactly. The depth theorem fixes the characteristic valuations, while the budget and place inventory make the B/x completion a finite menu once its remaining tails are supplied.

This is genuinely different from the completed monodromy test: `GROK-MONODROMY.md` realizes the admissible \(S_6\) passports, but does not ask whether the particular differential \(x\,dy\) has a global polynomial primitive with those principal parts. It is also different from the parked Hermite-Padé sampling in `SOL-ALGEBRAIZATION.md`: no fixed arbitrary completion is being asked to satisfy a full polynomial relation.

In the generic B-unramified/x-simple passport recorded in `GROK-MONODROMY.md` §1e, the compactified fibre has genus 18, hence 18 independent pairings. The recorded genus-zero specialization has no holomorphic differentials and is an honest no-traction sector; any proof claim must enumerate that sector rather than silently use \(g=18\) universally.

Because the affine fibre is smooth under \(J=1\), a meromorphic function on its compactification with poles only at infinity is regular on the affine curve and therefore is represented in its coordinate ring. Thus Mittag-Leffler is the correct global compatibility problem, not an irrelevant compact-curve embellishment.

Relevant anchors: avenue 1 above; `SHEET6-CLASSICAL.md` §0 for the place/contact inventory; `GROK-MONODROMY.md` §§1e–2 for the genus/passport sectors; `SHEET6-TEMPLATE.md` §1 for the rigid coefficients.

### (c) First concrete computation this week

Run a Rosenlicht-adjoint pilot for the generic genus-18 sector.

1. Start with the 13,861 monomials \(H=x^iy^j\) of projective degree at most \(165=168-3\).
2. Impose local holomorphy/cancellation conditions for \(H\,dx/f_y\) at P1, P2, B, and x infinity places; the kernel should have dimension 18 in the pilot sector.
3. Integrate \(x\,dy\) locally after imposing the no-log rows, extending the current jets only to the residue order required (a first cap near level 84 is reasonable).
4. Form the 18 residue pairings and reduce them modulo the augmented D21/Q2 ideal at two good primes, then exactly on any surviving rows.

The upfront sparse adjoint reduction has 13,861 columns; the final global block has only 18 rows and should touch on the order of hundreds, not thousands, of active tail monomials. Estimate: 2–5 days and a few GB for the pilot. The first gate is to find adjoints vanishing enough at unresolved B/x places to isolate P1/P2; if that subspace is zero, enumerate the finite B/x passport sectors rather than pretending the poles decouple.

### (d) Kill criterion for the avenue

Abandon this as a new constraint source if, in every viable positive-genus passport sector, all adjoint pairings lie in the radical of the existing J plus no-log ideal and give no rank/codimension gain at two generic primes followed by an exact leading-symbol check. Also abandon it until more tail data exists if unresolved B/x coefficients enter before every usable residue order. A genus-zero sector merely gives no conditions in that sector; it does not by itself refute the positive-genus computation.

## 5. A gauge-free, depth-invariant coefficient holonomy

**Label: HIGH SPECULATION; only the uniform eliminant is new.**

### (a) Idea — five lines

1. Encode leading-coefficient transport on every incoming edge, merge, and trunk as binomial relations in scale variables.
2. Quotient all independent vertex gauges by taking the Smith normal form of the exponent lattice.
3. Any surviving cokernel character is a scale-free product/cross-ratio comparing the two incoming paths at the merge.
4. Use conservation of \(w\) to prove that neutral depth acts by a fixed transition and leaves that character unchanged.
5. Evaluate the resulting character on the rigid Prop. 8.1(iv) solution; an incompatible constant kills the whole depth-signature at once.

### (b) Why it could work here

Ordinary “solve Prop. 8.1(iv), then match coefficients to incoming ratios” is already the stated next layer in `SHEET6-MULTIPOLE.md` §8, `BOOK-ENUM.md` §5, and the concurrent 62-cell T1 work. That is not this proposal. The only potentially new object is a **single gauge-invariant eliminant**, derived once and expressed solely in depth-stable cell data, rather than 62 unrelated coefficient solves.

The residue-A identities provide a positive control: the two paths close at the exceptional ratio \(2\pm\sqrt3\). Exact-budget off-axis routes leave no hidden charged vertex to absorb a mismatch, and the Jacobian inhomogeneity (\(-42\) on sheet 6, \(-\kappa\) in a general chart) fixes the last global scale. Depth conservation is essential: without it the eliminant would merely restate a finite per-route computation.

The main risk is structural and should be tested first. The characteristic graph is tree-like; after allowing every legitimate independent scale, the proposed “holonomy” may have no nontrivial cokernel character at all. If so, the idea collapses to the already-planned coefficient match and must be dropped.

Relevant anchors: `SHEET6-MULTIPOLE.md` §8; `BOOK-ENUM.md` §5; `SHEET6-TEMPLATE.md` coefficient-transport checks; `SHEET6-DEPTH.md` conservation and menu stabilization.

### (c) First concrete computation this week

Use the exact-fit \((10,15)\) route as the gauge audit. Build only its leading-scale system: approximately 8–20 scale variables and at most 30 binomial/algebraic transport equations. Compute the exponent-matrix Smith form, identify its gauge cokernel, and eliminate the remaining rigid constants over \(\mathbb Q\) and three good primes. If a nontrivial character exists, repeat on five nonisomorphic class-C signatures and attempt to express it in \((w,M,\bar\kappa,X,\nu)\). Estimated cost: hours for the pilot, 1–3 days for the representative batch.

### (d) Kill criterion for the avenue

Abandon immediately if the quotient exponent lattice has no non-gauge character. Also abandon if the only characters are identities already implied by covariance/Prop. 9.3, or if \((10,15)\) and five nonisomorphic cells all solve them with a free scale and no depth-independent constant remains. Do not relabel ordinary per-cell coefficient matching as holonomy.

## 6. Disproof side: positively lift an exact-fit off-axis cell

**Label: SPECULATIVE DISPROOF-SIDE CONSTRUCTION.**

### (a) Idea — five lines

1. Take the first class-C cell that survives the concurrent local T1 law, using \((10,15)\) first if it survives.
2. Reconstruct its explicit two-chain/merge/root genome positively, including all leading-scale glue and the exact-action residue pins.
3. Extend through the first characteristic Puiseux window while imposing \(J(f,g)=1\), rather than searching for another negative scalar obstruction.
4. Search for a smooth solution over several good finite fields and Hensel-lift the resulting component.
5. Continue successive windows while the depth invariant freezes the discrete genome; call success a formal candidate, not a polynomial counterexample.

### (b) Why it could work here

The \((10,15)\) route is unusually sharp: it uses the minimum chain cost \(\lambda=2\), has a zero-cost class-C merge, terminates immediately at \(w=4/5\), and saturates Statement 9.4 with \(\psi=4\). There is almost no discretionary combinatorial data. That makes it a better construction seed than a generic member of the 62-cell superset.

This is not another residue-A deep-tail stratum: the entry state, the \((21,15)\) jump, the multiplicity-three arriving zero-direction, and the terminal \(M=5\) are all different. It therefore probes whether the off-axis book is merely a permissive combinatorial superset or contains an honest formal Keller genome. The general \(-\kappa\) Jacobian row fixes normalization just as \(-42\) does on residue-A, while the action-residue lemma supplies cheap consistency rows. The depth invariant prevents a positive lift from evading failure by silently changing its route.

This avenue must begin **after** the in-flight local T1 solver: rerunning the 62 Prop. 8.1(iv) solves is not new. If \((10,15)\) dies locally, use the next nonisomorphic minimum-\(\lambda\) survivor.

Relevant anchor: `BOOK-OFFAXIS.md` §10 P4 for the exact route and totals; `SHEET6-DEPTH.md` for depth stability; the template-lift machinery in `SHEET6-TEMPLATE.md` is a reusable implementation pattern, not evidence that this off-axis genome exists.

### (c) First concrete computation this week

Stage 0 should contain roughly 20–50 pattern/gluing variables. The first honest characteristic window should use about 100–300 active series coefficients and \(10^3\)–\(10^4\) sparse transport/Jacobian equations. Screen three good primes, saturating root-simplicity, pole-count, and nonzero-scale guards before interpreting a component. Run characteristic zero only for a smooth or otherwise structurally promising component. Estimate: 2–7 days.

If a smooth modular component survives, Hensel-lift it and add two or three successive characteristic blocks. Each lifted point must be substituted back into the original, non-relaxed equations and the action-residue rows. A finite formal jet is valuable, but it is not a disproof of JC2; algebraization and a polynomial Jacobian check would remain.

### (d) Kill criterion for the avenue

Abandon the broad counterexample hunt if \((10,15)\) and two other nonisomorphic minimum-cost class-C cells all have saturated characteristic-zero EMPTY certificates, or if every modular component is forced into a guard violation (multiple prescribed roots, wrong pole count, or zero normalization scale). Convert any common failure equation into a proof lemma. Failure at one prime, or failure of one arbitrary gauge choice, is not an abandonment certificate.

## 7. Multibranch Gorenstein value-semigroup symmetry at y-infinity

**Label: HIGH SPECULATION; cheap theorem-perimeter gate first.**

### (a) Idea — five lines

1. The projective generic fibre has a reduced plane-curve germ at the common y-side infinity point, hence a one-equation Gorenstein completed local ring.
2. Its multivalue semigroup and conductor vector obey Gorenstein/Delgado symmetry constraints.
3. Compute the semigroup from the orbit-compressed parametrizations of \(x,y,h_1,h_2\) and their standard-basis cancellations.
4. Those cancellations see coefficients and can change when the forced levels 38–42 turn on, even though the splice graph passes.
5. A failed conductor symmetry or missing required value would kill analytic plane-curve realizability of the template.

### (b) Why it could work here

All 126 Puiseux series enter one projective point, but they are **not** 126 analytic branches: the analytic branches are P1, P2, and the as-yet partitioned B places, i.e. \(2+r_B\). The existing classical test checked splice determinants, genus, and one-place valuation consequences; it explicitly notes that the one-place Abhyankar-Moh semigroup theorem does not apply globally (`SHEET6-CLASSICAL.md` §§1–2). A multibranch local-ring computation is therefore a different object.

The exact \(2\pm\sqrt3\) cancellation and the \(-42\)-forced low tails are precisely coefficient data erased by the topological splice diagram. Depth invariance pins the characteristic generators, while the finite B-place/budget menu bounds the possible branch partitions. The pole branches have \(\delta(P_i)=1139\), giving a concrete conductor scale.

The risk is severe: Gorenstein symmetry may be automatic from any realizable Puiseux/contact tree and may add nothing beyond the already-passing splice data. This is why the avenue ranks last and begins with a theorem-perimeter check rather than a large SAGBI run.

Relevant anchors: `SHEET6-CLASSICAL.md` §§0–2; `SHEET6-TEMPLATE.md` §1; `SHEET6-DIRECTIONB.md` §6.T–6.V.

### (c) First concrete computation this week

First spend at most a few hours determining, from the multibranch semigroup literature/formulae, whether the conductor symmetry for a reduced plane-curve germ is already determined solely by the checked contact tree. If it is not, run an orbit-compressed local standard-basis pilot on the P1/P2 subgerm, then add each allowed B partition. Use \(x,y,h_1,h_2\) and the forced low-tail generators, enumerate value vectors only to the conductor box, and test the symmetry involution.

Expected pilot size: at most about ten orbit-level generators, coordinate conductor cutoffs of a few thousand (consistent with \(\delta(P_i)=1139\)), and laptop hours to two days. If tails beyond the current depth enter before the conductor, record the first missing coefficient order rather than filling it arbitrarily.

### (d) Kill criterion for the avenue

Abandon immediately if the symmetry is a formal consequence of the already-passing splice/contact tree. Also abandon until deeper data exists if unpinned B tails enter below the conductor in every allowed partition, or if two genuinely different low-tail completions give the same automatically symmetric semigroup. A pass on the P1/P2 pilot is not evidence for the full \(2+r_B\)-branch germ.

## Recommended launch order

Launch avenue 1 first: it is an exact theorem and changes the live system for negligible engineering cost. Run avenue 2 in parallel because it reuses the already-emitted monomial support and can return either a sound proof obstruction or a verified construction seed. Instrument avenue 3 while those algebra runs execute. Start the avenue-4 adjoint pilot only after the no-log guards pass; start avenue 5 only if its Smith-form gate finds a genuine non-gauge character. Reserve the positive off-axis lift for the first class-C cell surviving the concurrent T1 solver, and give avenue 7 only its cheap automaticity gate unless that gate is positive.

Nothing above reopens the completed Mathieu-Zhao/strip, monodromy, algebraization-sampling, every-fibre Prop. 5.8, p-curvature, valuative-tree, Galois, budget-composition, quantum, or zero-tail lanes.
