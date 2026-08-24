# SHEET6: Feasibility of extending the degree-≤5 topological-degree exclusion to 6

Status: HISTORICAL FEASIBILITY MEMO (completed 2026-08-04). The realized
census and survivor ledger supersede the estimates below; see
`SHEET6-CAMPAIGN.md`, `SHEET6-AF3.md`, `SHEET6-LROOT.md`, and
`SHEET6-LT-REVIEW.md`.  The later local strictness disposition is in
`xmodel/d73-strict-or-equality-20260824.md`.

## Canonical checksum (2026-08-24)

- Żołądek's Theorem 6.12 closes topological degree at most five; the first
  open sheet degree is six. The official paper is now banked as
  `refs/zoladek2008_official.pdf`.
- Sigray's thesis *states* the same lower bound, but it is **not a complete
  independent reproof as printed**. The campaign found the omitted row
  coverage and terminal-kill problems recorded in `SHEET6-REVIEW.md`; the
  later M-pin, H3q/psi-budget, and Case-III work repair the campaign
  recomposition, not the original one-line proof.
- The realized arithmetic census is **14 rows at Lambda <= 7**, with **six**
  Lambda=6 rows. The td=6 configuration census is six single-pole entries
  plus the one two-pole `(3,3)` configuration, not seven Lambda=6 rows or
  seven partition shapes.
- After the M-pin and chain composition, the terminal-class book has
  **eight** classes: four single-pole `r9/M2` classes and four two-pole
  residue-A classes. The two-pole sector passes through one merged datum
  `Q(G_m)=(6,12,3,2,5)@lambda=0`; "one merged child" does **not** mean one
  terminal class or one global survivor.
- Blanket H3, the raw Case-III tail list, and an unrestricted two-pole
  analogue are no longer the live to-do list. Blanket H3 is false, the
  proposed extra root charge is forced to be `lambda_root=0`, and the
  coefficient template survived the reviewed lift.  An exact Jacobian-one
  analytic germ subsequently showed that a multiple direction root can attain
  equality in the local delta bound, so multiplicity alone cannot provide a
  strictness kill. A later dual-confirmed global-compatibility control showed
  that the bare `x=t s^4` divisibility obstruction disappears under the
  LR2-legal shared centering `T=xy^4-y^3`; fixed-rectangle controls reach only
  finite Jacobian order, while arbitrary one-sided orders require dropping the
  degree cap. A dual-confirmed two-chart numerical specialization is nonempty
  at its first shared band (rank `3508/3602`) but its entire 94-dimensional
  affine family dies one x row later at
  `[s^-1 t^13]J=-18858/3125`. This is not uniform in the licensed moduli and
  kills no terminal class.  The symbolic-moduli continuation makes that row
  `(6/5)(5E2-2E1^2)`: its complex zero curve carries a 56-dimensional paired
  finite-band survivor.  One algebraic point dies at the next centered row;
  uniformly on the curve, that row cuts to an irreducible sextic and a later
  exact left-syzygy is nonzero at all 18 pole-normalized conjugates.  Thus the
  whole **fixed normalized reduced-boundary family** is empty, but the
  x-boundary, dead-stretch, centering, and other boundary moduli were not
  quantified.  The first q-boundary deformation `q_B=t+B*t^2+t^25` is
  dual-confirmed empty at `B=1` and one exact adaptive value at the centered
  `t^4` row, with a genuinely `B`-sensitive residue; these two points do not
  kill the family.  The live local/global surface is fraction-free
  elimination over `E[B]` with every pivot/rank-jump stratum treated
  separately, alongside the reviewed R6/deeper-tower plus redesigned-R1
  coefficient path toward template algebraization. At campaign scope, full
  landing/coverage and the distinct `G2-PSC` / `G2-BD` obligations remain;
  this sheet ledger alone is not an unconditional reduction of JC2.

## 1. Source acquisition
- **Żołądek 2008** (Topology 47(6) 431–469, DOI 10.1016/j.top.2008.04.001):
  the official PDF was subsequently obtained and is banked as
  `refs/zoladek2008_official.pdf`. Theorem 6.12 gives the topological-degree
  <=5 result. The neighboring gcd claims have a separate audit history and
  should not be conflated with that theorem.
- **Obtained (free, in `refs/`)**: Orevkov 1986 3-sheet paper (`jc86.pdf`, author-hosted English), Domrina–Orevkov 1998 4-sheet I (`do.pdf`), and — the decisive find — **Sigray's full 66-page 2008 ELTE PhD thesis "Jacobian trees and their applications"** (`sigray_full.pdf`, teo.elte.hu/minosites/ertekezes2008/sigray_i.pdf; booklet `sigray_i.pdf`), advisor A. Némethi.
- **1b. Egorov identified**: G. V. Egorov, "Example of a five-sheeted exotic covering over C²", Mat. Zametki 71:4 (2002) 532–547 (mathnet.ru/eng/mzm364, free).
- **1c. Independent-reproof claim withdrawn**: Sigray's thesis Theorem 9.1
  states `td(f,g) >= 6` and uses machinery distinct from Żołądek's, but
  `SHEET6-REVIEW.md` confirms that the proof is incomplete as printed:
  Statement 9.12 does not supply its advertised terminal kill, and the
  one-line Theorem 9.1 proof omits the other td<=5 table rows. Later campaign
  work repairs those gaps inside the audited Sigray frame; it does not make
  the printed thesis an independent complete proof. Sigray remains useful as
  the source of the tree engine and is cited for the bound by
  Makar-Limanov (arXiv:2106.06869) and Borisov (arXiv:1901.04073). The
  documented GGV criticism of Żołądek's neighboring gcd argument is separate
  from Żołądek's Theorem 6.12. The later source audit of arXiv:2407.13795
  (Moskowicz, 2024) is dual-confirmed `REFUTED-AS-PROOF`: its first case uses
  a false universal degree-two inference, so its no-prime headline is not a
  usable theorem. This does not disprove that headline. Its repaired second
  case gives only the independent membership implication
  `xy in C(P,Q) => automorphism`.

## 2. Method skeleton (two structurally distinct engines, not two audited proofs)
Both: compactify, resolve indeterminacy at infinity, then add Abhyankar-type ARITHMETIC of Puiseux data to the topology.
- **(A) Żołądek's Newton–Puiseux charts** (originally reconstructed from zbMATH + Nguyen Van Chau arXiv:0804.3172v2 + MIMUW seminar abstract; now checkable against the banked official paper): resolve (f,g) at infinity in BOTH source and target; near each divisor use multivalued charts (x^{−1/m}, ξ) — truncated fractional-power series x(Σc_k x^{−k/m} + ξx^{−n/m}) where ξ replaces the Puiseux tail ("left and right Newton-Puiseux charts", Chau). The Keller map becomes near-monomial in charts; jac≡1 forces rigid exponent+leading-coefficient relations. Topological degree = sheets over infinity = Σ local degrees over dicritical divisors, with Orevkov's identity Σ(ramification excess at infinity) = td − 1. Case analysis = finite enumeration of dicritical/chart configurations for td ≤ 5; each killed by exponent arithmetic or analytic contradiction.
- **(B) Sigray's decorated Eggers–Wall trees** (verbatim, thesis in hand): Abhyankar normal form (§2: Newton polygons in rectangles, fibers with 2 points at infinity); Eggers–Wall tree of Puiseux expansions of f-fiber branches at infinity (§3); extended Abhyankar fundamental theorem + partial order (§4); td and pole orders of g computed from tree data (§5, Props 5.5/5.8); tree structure symbols ↘↗ (§6); finite critical values budget (§7, Cor 7.1); Jacobian-forced number theory linking neighboring vertices (§8, Prop 8.1); §9: decoration Q(F) = (D_F, deg p_F, ν_F, M_F, κ_F(1−π(F))) propagates along the "characteristic sequence" F₀→…→(0,y), under Diophantine constraints and budget Σλ_{F_i} ≤ td−2 (St 9.4). The intended td≤5 closure is incomplete as printed; the campaign's repaired row selection and terminal arithmetic produce the zero-class result inside this frame.
- **Intended anchor structure of Sigray §9**: one 11-row multiplicity-data
  table (Prop 9.1) plus six propagation lemmas (St 9.6–9.11), each reduced
  to small Diophantine equations, followed by Statement 9.12. The printed
  `(75,51)` member of the sample St 9.6 list is spurious; exact reproduction
  leaves `(21,15)` and `(20,16)`. The campaign also had to repair the row
  coverage and terminal disposition described above.

## 3. Why complexity grows with sheet count; what exploded between 4 and 5
- **Orevkov/Domrina (3,4) were quasi-topological**: splice/Eisenbud–Neumann diagrams of the resolution boundary, homology, intersection form, canonical class K̃ = F*K + B of the branched cover; leaf kills by unimodularity/negative-definiteness/Abhyankar–Moh determinant arithmetic. Case tree at 4: ~19 configurations → 8 final diagrams (Domrina 2000), a few dozen leaves.
- **The 4→5 explosion is NOT case count — it is a provable method failure.** Egorov 2002 constructed a proper 5-sheeted "exotic covering" of C² (branching along two planes F₁*,F₂*; H²_c ≅ Z²; S₁² = −3, S₂² = −15, S₁·S₂ = −3; K(S₁)=K(S₂)=1) consistent with EVERY quasi-topological invariant Domrina–Orevkov use. So 5 required a new analytic layer: Żołądek's proof and Sigray's distinct tree program inject Abhyankar approximate-root/Puiseux-coefficient arithmetic (pole orders of g along f-branches; jac=1 exponent identities) that sees strictly more than the topology. That is the conceptual jump; the case tree itself only grew ~2×.
- **The forecasted wall-at-9 reading is superseded at td=6**: Sigray
  exhibits a decorated Eggers–Wall tree at td=9 with bidegree `(48,64)`,
  showing that his printed local constraints cannot settle all higher
  degrees. The completed campaign also found consistent terminal data already
  at td=6—the eight classes in the checksum—so nine is not the first local
  survivor and must not be described as the current wall.

## 4. Degree-6 case tree: forecast versus realized census
- **Leaf table**: the forecast was 20–30 rows at Lambda <= 7. The exact
  engine census is **14 rows**, three beyond the 11-row Lambda<=6 table;
  exactly **six** rows have Lambda=6: `{2,3,6,8,9,11}`.
- **Configuration layer**: the forecast of seven partition shapes was too
  coarse. Since every pole contributes Lambda>=3, td=6 has exactly **six
  single-pole table entries plus one double-pole `(3,3)` configuration**.
  The M-pin then kills four single-pole entries at entry, `r8/M3` closes,
  and `r9/M2` supplies the four single-pole terminal classes.
- **Propagation work**: the historical 12–20-lemma forecast became roughly
  30–90 solved propagation steps per live entry before deduplication. The
  aggregate forecast of 150–400 exact elementary verifications was the right
  order of magnitude; the arithmetic stages ran in seconds to minutes.
- **Endpoint**: the double-pole configuration funnels to the single merged
  datum above and then branches into four terminal classes. Together with
  the four `r9/M2` classes, the terminal-class count is eight.

## 5. Fan-out design
- **Per-case task format** (one agent = one case): JSON {case_id; hypotheses: Q(G) parametric tuple, type row, Prop-9.3 branch (I/II/III/IV), mult(p,c) value; goal: complete list of admissible Q(F) or proof of emptiness; required output: solution families + machine-checkable trace}.
- **Verification standard**: exact arithmetic only (PARI/SymPy; no floats, no Gröbner needed at this layer). Every "no solution" needs a certificate: explicit congruence obstruction (with modulus), or monotone bound + finite sweep below it. Two independent implementations per case (repo's dual-build culture); spot-formalize the Diophantine kills in Lean post-verdict. Symbolic residue computations are NOT needed for the Sigray engine (they belong to Żołądek's chart engine, which we'd hold in reserve as cross-check).
- **Coordination**: (i) trunk agent formalizes §§2–8 into a small library (Q-tuples; propagation relations Prop 8.1 + Prop 9.3(a)–(m); λ-budget); (ii) leaf agents consume (row × branch) cases; (iii) merge agent assembles the St-9.12-analogue induction; (iv) independent audit lane re-derives Prop 9.3(a)–(m) and Prop 8.1 from scratch. Pipeline mirrors the (72,108) chart/complement split that already works in this repo.

## 6. Non-mechanizable parts (historical forecast; superseded endpoint noted)
1. **Foundations audit (remaining source risk)**: Sigray's unrefereed §§3–8
   remain the trust perimeter for this tree program. The official Żołądek
   paper is now banked, and the documented gap in a neighboring gcd argument
   must not be projected onto Theorem 6.12.
2. **Lambda/td bookkeeping at 6**: this forecasted task was carried out. The
   reviewed Euler ledger forces `lambda_root=0`, one x-side cv vertex with
   `kappa=1`, and total rigidity on the four slack-zero classes.
3. **Survivor scenario**: this scenario occurred. The exact local survivor
   ledger has eight terminal classes, and the reviewed coefficient lift of
   the two-pole template is a formal candidate rather than a kill. The live
   questions are therefore global polynomial realizability/opposite-side
   balance, the reviewed R6/deeper-tower and redesigned-R1 coefficient path
   toward algebraization, and the global landing/coverage/delay obligations.
   The exact equality control in
   `xmodel/d73-strict-or-equality-20260824.md` retires direction multiplicity
   alone as a local strictness route.  Another raw row or Case-III sweep is
   not the current task.

## 7. Verdict + pilot
- **Historical verdict**: the proposed exact-arithmetic campaign was
  feasible and was run. It did **not** prove `td>=7`: it produced the
  eight-class local book described above. The official Żołądek PDF has also
  since been acquired. Any present campaign claim must use the canonical
  checksum, not this memo's original estimates.
- **Historical pilot (completed)**: mechanically re-derive **Prop 9.1's
  11-row table and Statement 9.6**, diff against thesis pp. 45–53, then
  extend the table to Lambda=7. The gate and 14-row extension both passed;
  see `SHEET6-CAMPAIGN.md` §§0–1.

## Refs (in `refs/`)
`zoladek2008_official.pdf` (official td<=5 paper) · `sigray_full.pdf` (66pp
thesis, tree-engine working text) · `sigray_i.pdf` (booklet) · `jc86.pdf`
(Orevkov 3-sheet) · `do.pdf` (DO 4-sheet I) · Egorov:
mathnet.ru/eng/mzm364 · Domrina II: mathnet.ru/eng/im273 · GGV gap report:
arXiv:1401.1784 · Chau chart description: arXiv:0804.3172v2.
