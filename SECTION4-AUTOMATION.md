# SECTION4-AUTOMATION — automating the GGV §4 per-family reductions

Design (no implementation) for the family-farm prerequisite identified in notes.md
(2026-07-29): replace the hand reductions of arXiv:2204.14178 §4 (Props 4.1–4.4)
by an algorithm that, given a family from the GGV5 enumeration, outputs the
reduced Newton polygons N(P), N(Q) and the bracket RHS x^k, together with a
machine-checkable justification log. Verified below to reproduce all seven
§4 outputs (the exact corner sets already transcribed in `cases/emit.py`).

Sources (local caches under /tmp/jcpapers/, fetched 2026-08-03; cite by arXiv id):
- **GGV22** = arXiv:2204.14178 "§4" = section *Reducing the size of the Newton
  polygon* (tex lines 457–1398). Prop 4.1 = case (9,27), 4.2 = (9,24) [3 subcases],
  4.3 = (8,28) [2 subcases, RHS x²], 4.4 = (7,21). Contains verbatim pseudocode
  `PossibleStartingPoints` (Algorithm 1, tex 698–719).
- **GGV1** = arXiv:1401.1784 (Dec-2015 arXiv version; §7 = "More conditions on B",
  §8 = "The case B=16"). Cor 7.2 (label `fracciones de F`), **Cor 7.4**
  (`fracciones de F1`), Thm 7.6 (`divisibilidad`, incl. the (q,d)-divisibility
  facts), **Prop 8.2** (`esquina de 83`), Prop 2.11(3) (power ⇒ single factor),
  §8 preamble = the operation alphabet (constants, Aut(L), Aut(L^(1))).
- **GGV2** = arXiv:1605.09430. **Prop 3.12** (`finitas direcciones`: the 3-case
  filter with N1, N2, ϑ), Remark `gap`, PLLC results (`cota`: b<a, b≤(a−b−1)²;
  `casos imposibles`: ℘(n′,n′−1) ∉ PLLC), last-possible-corner machinery.
- **GGV5** = arXiv:1708.07936. Family enumeration: complete chains
  (𝒜₀,𝒜₀′),…,𝒜_{j+1}, the (m,n)-families, eq. **(q_k)**:
  p_h = (ρ_h+σ_h)/g, q_h = v_{ρ_h,σ_h}(A_h)/g, g = gcd(ρ_h+σ_h, v_{ρ_h,σ_h}(A_h)),
  where (ρ_h,σ_h) = dir(A_h−A_h′); tables of all 34 cases with
  max(deg P,deg Q) ≤ 150 (§7) and the (m,n)-family tables (§6).
- GGV6 (Pro Mathematica 30, not on arXiv): Prop 2.5 (sharper predecessor filter,
  used once in Prop 4.3), Thm 7.3 (intersection numbers — NOT needed for
  reduction, only for discards like the 84-case; out of scope here).

Convention note: GGV22 freely flips orientation with φ₁ (x↔y). We fix: run the
whole reduction in "flipped" coordinates (A₀ = (a,b) with a>b after flip) and
state Cor 7.4 usage in that frame; unflip only in the final report if desired.

---

## 1. The common algorithm (what the four proofs actually do)

All four proofs are instances of one loop:

```
load family F = (A0, A0', chain [(A1,A1'),...], k, (m,n))     # GGV5 data
S := start polygon (1/m-units), P-support = m·S, Q-support = n·S
repeat (over boundary sections, low side first, chain order):
    1. CERTIFY an edge-power: Cor 7.4/7.2 at (ρ0,σ0)=dir(A_h−A_h') with
       q = q_h from (q_k)  ⇒  ℓ_{ρ,σ}(P) = λ·R^{q·m} on the adjacent
       direction interval; en(R) = (1/q)·A_h ∈ ℤ² forced.
    2. LOCATE st(R): finite candidate list via Algorithm 1 /
       GGV2 Prop 3.12 / GGV6 Prop 2.5; kill candidates by support-level
       contradictions (vdE 10.2.6, PLLC, Thm 7.6 divisibility).
    3. FACTOR-BRANCH: enumerate root-multiplicity partitions of R in
       z = x^K y; kill partitions via Prop 3.12(2) (forced multiplicity ϑ)
       and λ≠0 side-arguments.  ← subcase splits live HERE.
    4. CUT: apply e_K(λ₁): y ↦ y + λ₁x^{−K} (an Aut(L^(1)), bracket-
       preserving); the certified factor (z−λ₁)^{t₁qm} becomes z^{t₁qm}:
       the edge shortens or collapses; y^d prefactors spawn a Laurent
       tail (−K·d,0)-ward.  Iterate 1–4 while chain data remains.
until support stabilizes (no certifiable edge with q>1 remains cuttable)
5. TAIL RESOLUTION (only if a residual vertex with unknown following edge
   exists): opposite-vertex divisibility filter + GGV1 Prop 8.2 ⇒
   {en(P), en(Q)} = {(−k,0),(k+1,1)}, k forced (=1 in all §4 cases),
   P/Q assignment by a cross-product test. Supersedes provisional tails.
6. FINALIZE: ψ_j: x ↦ x^{−1}, y ↦ x^j y (L^(1)-morphism, NOT in Aut(K[x,y]))
   with j = ⌈max_{(i,j')∈supp, j'>0} i/j'⌉; supports (i,j') ↦ (j·j'−i, j');
   bracket: [ψP,ψQ] = −x^{j−2}[P,Q]  ⇒  RHS = x^{j−2} after scalar scaling.
report (N(P), N(Q), x^{j−2}, branch label, justification log)
```

**Why 4.3 yields x² and the others x:** the RHS exponent is j−2 and
j = ⌈b₀/a₀⌉ on the original corner A₀=(a₀,b₀) (= slope of the steep side that ψ_j
must rotate into the quadrant). (9,27),(9,24),(7,21): ⌈27/9⌉=⌈24/9⌉=⌈21/7⌉=3 ⇒ x.
(8,28): ⌈28/8⌉=⌈3.5⌉=4 ⇒ x². (Farm preview: (7,35)-type would give ⌈5⌉−2 ⇒ x³.)
The bracket exponent is thus pure lattice data, known before any branching.

**Why 4.4 has no tail-resolution stage:** its single cut collapses the edge
completely (st(R)=(1,0), no y-prefactor ⇒ the transformed edge is a monomial)
and the remaining boundary consists of original chain edges only — no residual
vertex with unknown continuation is created. In 4.1/4.2/4.3 the second cut leaves
the residual vertex (en − qm·t₁·(K,1)-type, e.g. (21,8), (24,7)) whose next edge
is unknown ⇒ step 5 runs.

---

## 2. Inputs

Per family, taken verbatim from GGV5 (§6 family tables; §7 deg≤150 tables):

1. `A0 = (a,b)`, `A0' = (a',b')` (usually (1,0), sometimes (2,0));
2. chain `[(A1,A1'), ..., A_{j+1}]` with fractional corners `A_i = (a_i/l_i, b_i)`
   (e.g. (11/3,8) for (9,24)/(9,27); (11/4,7) for (8,28); (11/7,2) for (7,21));
3. `k` (the family's k-invariant, column k of the tables) and the (m,n)-family
   formulas (m(j̃), n(j̃)); the farm instantiates concrete coprime (m,n);
4. derived per chain step h: `(ρ_h,σ_h) = dir(A_h − A_h')` and `(p_h, q_h)`
   via (q_k). Regression values: (9,27): q₀=9 at (−2,1)-edge, q₁=3 at (3,−1);
   (9,24): q=3 at (3,−1); (8,28): q=4 at (4,−1); (7,21): q=7 at (7,−2).
5. start polygon S (1/m-units): conv{(0,0), A0', A0} ∪ {integral chain corners}
   ∪ {(0,c)} with c = v_{ρ*,σ*}(A0) for the upper-left chain direction; for the
   §4 families: (9,27): {(0,0),(1,0),(9,24),(9,27),(0,9)}; (9,24):
   {(0,0),(1,0),(9,24),(0,6)}; (8,28): {(0,0),(1,0),(8,28),(0,4)}; (7,21):
   {(0,0),(1,0),(7,21),(0,7)}. NOTE: GGV22 partially re-derives these
   ("We will prove first that the corners are…"); the automation should
   re-derive (0,c) via rules R1–R3 below rather than trust a table, since
   this derivation is precisely steps 1–3 applied to the upper-left section.

The loader can start from the transcribed deg≤150 tables (34 rows, an
afternoon of typing) — reimplementing GGV5's `GetmnFamilies`/`Main algorithm`
(their §5–6 pseudocode is complete) is a later, separable task needed only
beyond deg 150.

---

## 3. State and primitive transformations (exact semantics)

**State** = (SuppP, SuppQ, Consts, Certs, Log), where SuppP/SuppQ are corner
lists of lattice polygons in ℤ² (Laurent allowed: x-exponents may be negative;
everything lives in L^(1) = K[x,x^{−1},y]); while P,Q are proportional the state
stores one 1/m-polygon S with SuppP = m·S, SuppQ = n·S (they individuate only at
the tail-resolution step). Consts = symbolic scalars (λ, α_i, …) each carrying
constraints from its introduction (≠0, mutual distinctness, "root of the edge
form with multiplicity t·qm"). Certs = active edge-form certificates. Log =
append-only justifications (rule id + verified hypotheses + branch labels).

Primitive ops (all exact on support sets; each records its bracket effect):

- **T-swap** φ₁: (i,j) ↦ (j,i). Bracket ↦ −bracket (absorb into scalar).
- **T-shift** e_K(λ): x ↦ x, y ↦ y + λx^{−K}, K ∈ ℕ. Automorphism of L^(1);
  bracket invariant. Naive support map: (i,j) ↦ {(i−Kt, j−t) : 0 ≤ t ≤ j}.
  Cancellation beyond the naive map happens ONLY on an edge covered by a
  certificate (below); elsewhere take the union/hull. Valid for cutting an
  edge of direction (ρ,σ) only when ρ = 1 after normalization, i.e. (1,−K)
  (else x^{−σ/ρ} ∉ L^(1); e.g. the (2,−7) branch of 4.3 is uncuttable and
  simply terminates as case a)). Only ever applied when a certificate names λ.
- **T-const**: add constants / scale by K^× (keeps (0,0) in supports; scales
  bracket).
- **T-final** ψ_j: x ↦ x^{−1}, y ↦ x^j y: (i,j') ↦ (j·j'−i, j'). Injective on
  supports (no cancellation possible); precondition: j·j'−i ≥ 0 on all support
  (choice of j) and all (i,0) have i ≤ 0. Bracket ↦ −x^{j−2}·bracket.

**Edge-form certificate** (the only place coefficient information enters):
for an edge E of direction (1,−K) (in cutting position) with en(E) = m·A,
a certificate is
`ℓ_{1,−K}(P) = λ_P · x^{c} y^{d} · Π_i (z−λ_i)^{q·m·t_i}`, z := x^K y,
with (c,d) = m·st-corner data, Σt_i = z-degree/q·m, λ_i distinct, nonzero.
Applying e_K(λ₁) to a certified edge rewrites it exactly:
(z−λ₁) ↦ z, (z−λ_i) ↦ (z−(λ_i−λ₁)), y^d ↦ (y+λ₁x^{−K})^d, giving new edge
support st′ = st + qm·t₁·(K,1) (shorten), or full collapse to en when the
partition is trivial (one root, d = 0); the (y+λ₁x^{−K})^d factor contributes
the Laurent tail corners {(c−K·d̃, 0)-direction points, d̃ ≤ d} — in practice a
provisional corner (i_st − K·d, 0), refined later by tail resolution.

## 4. Rule library (each rule = checkable preconditions ⇒ conclusion)

R1 **Edge power (GGV1 Cor 7.4 / 7.2).** Preconditions, verified on the state:
   [P,Q] ∈ K^× still (i.e. before T-final); v-ratios m/n at (1,1),(0,1) (resp.
   (1,0)); (ρ₀,σ₀) ∈ Dir(P), v_{ρ₀,σ₀}(P) > 0; (1/m)st (resp. en) = (a/l,b) ∈
   (1/l)ℤ×ℕ with b < a/l (7.4) or b > a/l (7.2); F-data st/en(F) = (p/q)(a/l,b)
   with p,q coprime — supplied by (q_k) from the chain. Conclusion: for every
   (ρ,σ) strictly between (ρ₀,σ₀) and the bounding direction (ρ̃,σ̃):
   ℓ_{ρ,σ}(P) = λR^{qm}, R (ρ,σ)-homogeneous. Corollary used constantly:
   en(R) = (1/(qm))·en of that edge must be a LATTICE point, and R's support
   lies on the segment [st(R), en(R)] with spacing gap-divisibility
   (GGV2 Remark `gap`: only exponents divisible by gap(ρ,l) occur).
R2 **q from chain data (GGV5 (q_k)).** q = v_{ρ,σ}(A_h)/gcd(ρ+σ, v_{ρ,σ}(A_h))
   at (ρ,σ) = dir(A_h−A_h′). Pure integer arithmetic.
R3 **Predecessor/start filter (GGV22 Algorithm 1 = `PossibleStartingPoints`;
   GGV2 Prop 3.12; GGV6 Prop 2.5).** Input corner (a/l,b); output finite list of
   (c/l,d) that can be st of the next edge, via s := (ρa+σlb)/gcd(ρa+σlb,
   l(ρ+σ)) and the test `(s | N₂ and d>0) or s ≤ N₁`, N₁ = gcd(a−c, b−d),
   N₂ = gcd(c,d). This is implementable verbatim from the paper's pseudocode.
R4 **Forced-multiplicity kill (GGV2 Prop 3.12(2)).** When the direction
   equation (ρ,σ) = −dir(t′·st(R)+ϑ(1,1)) has a solution with ϑ ≤ N₁,
   some linear factor of r(z) has multiplicity exactly ϑ ⇒ kills root
   partitions lacking a ϑ-multiplicity factor (e.g. 4.2: ϑ = s = 6 kills the
   3-distinct-roots partition of R = x²·(z-cubic)).
R5 **Zero-root exclusion (λ₁ ≠ 0).** Assume λ₁ = 0 ⇒ st of the edge moves ⇒
   re-run R3 on the hypothetical support ⇒ derive Pred ≤ (1,−3)-type bound ⇒
   contradiction with R6. Support-level reasoning only.
R6 **x-degree floor (vdE Prop 10.2.6).** P ∈ K[x,y] counterexample ⇒
   deg_x P(x,0) ≥ 1: the support must contain (d,0), d ≥ 1 (pre-Laurent
   stages). Kills candidate shapes whose lower side retracts past x¹.
R7 **PLLC checks (GGV2 `cota`, `casos imposibles`; GGV2 Prop 3.29 / Rem 3.31
   route used for (8,32)).** A last lower corner (a,b) needs b < a,
   b ≤ (a−b−1)², and (a,b) ∉ ℘(n′,n′−1). Used to kill branches whose cut
   would create a forbidden last corner; also powers the (8,32)-style instant
   discard (a bonus capability of the same engine).
R8 **Divisibility of d (GGV1 Thm 7.6(5)(8)).** q_h | d_i for later regular
   corners; with d·st(R) primitive-vector arithmetic this pins d₀ (used in
   GGV22's (8,32) discard: q₁ = 4 | d₀ and d₀ ≤ 4 ⇒ d₀ = 4 ⇒ edge form
   (λ x²y⁷(y−λ₁))^{4m}).
R9 **Tail resolution (GGV1 Prop 8.2 + GGV22's opposite-vertex filter).**
   Trigger: residual vertex V = (1/m)·(shortened-edge st), unknown next edge.
   (i) Enumerate opposite-vertex candidates (a″,b″) on the lattice strip below
   V; filter by the alignment congruence — with (a,b) := V: the next corner of
   F must satisfy (1,1)+c·(V−(a″,b″))/gcd = (p/q)V, giving the divisibility
   `(a·b″−b·a″) | v_{−b,a}(1,1)·gcd(a−a″, b−b″)` (the 13-gcd table of Prop 4.1).
   (ii) Prop 8.2 dichotomy: if en_{ρ₂,σ₂}(P) ≁ en_{ρ₂,σ₂}(Q) then ∃k:
   (k+1)b < a and {en(P), en(Q)} = {(−k,0), (k+1,1)}; enumerate k, kill values
   where the P/Q edges into those ends cannot be parallel (integer slope test;
   kills k=2 in 4.3); surviving aligned-case candidates are re-run and die on a
   direction clash (4.1: "different end for direction (−3,8)"). (iii) Assign
   (−k,0)/(k+1,1) to P/Q by the cross test (ρ,σ) × (st_{ρ,σ}(·) − candidate) ≠ 0.
   Effect on state: DISCARD all provisional tail corners (the e_K Laurent tails
   and A0′-image), set exact ends; P and Q polygons now differ beyond scaling.
R10 **Finalization.** j := ⌈max i/j′⌉ over support (j′>0); apply T-final;
   RHS = x^{j−2}; scale so the leading constant is 1. Emit.

## 5. Branching semantics — where subcases come from

Branch points, in decreasing frequency (each pushes a labeled node; the
algorithm explores the whole tree; a leaf = emitted case or contradiction):

B1 **Root partition of a certified R** (step 3). R has z-degree D/qm slots and
   support st(R)→en(R); enumerate partitions t₁ ≥ t₂ ≥ … of the slot count into
   distinct-root multiplicities; filter by R4 (ϑ must appear), R5 (zero root),
   chain data (the major root's multiplicity is fixed by A_{h+1}: mult/m =
   v_{01}(A−A′)/gap when the edge is "simple", GGV5 §3). — Prop 4.2: partitions
   of 3 = {3},{2,1},{1,1,1}; {1,1,1} killed by R4; {2,1} ⇒ subcase (1);
   {3} ⇒ continue. Prop 4.3 second cut: {8·} one-or-two-factor split:
   {2·4m,1·4m}-shape ⇒ case c) vs single ⇒ case b).
B2 **st-candidates after a full collapse** (step 2 re-run). When a cut removes
   an entire edge, the new predecessor start comes from R3's list. — Prop 4.2:
   st ∈ 3m{(0,0),(3,1)} ⇒ subcases (3) and (2). Prop 4.3 first cut:
   Pred ∈ {(1,−3),(2,−7)}: (2,−7) uncuttable ⇒ case a) terminates; (1,−3) ⇒
   continue into B1.
B3 **Aligned vs non-aligned ends** in R9 — in all §4 instances the aligned
   branch dies, but the design must carry it (it may survive in new families).

Branches that later converge (4.3's a) and b): different tails, same polygons
after R9 supersedes the tails) are merged by hashing the emitted state —
this is why 4.3 reports 2 subcases from 3 internal branches, and 4.2 reports 3.

## 6. Termination

- The chain provides ≤ j+1 certifiable sections; each e_K cut strictly reduces
  the lattice-point count of the current 1/m-polygon (edge slots consumed:
  st′ − st = qm·t₁·(K,1) with t₁ ≥ 1), so cutting terminates.
- B1/B2/B3 trees are finite (partitions of ≤ D ≤ b(A₀) slots; R3 lists are
  finite by construction; k in R9 bounded by a/b).
- Stop condition for the cut loop: no edge has both (a) an applicable
  certificate with q > 1 and (b) a legal e_K (ρ=1). Then R9 (if triggered),
  then R10. If a certificate exists but no rule resolves the branch, the
  algorithm STOPS with status `stuck` and dumps the state — it must never
  guess. (Soundness stance: under-reduction is acceptable, the emitted system
  is still a valid Generator-A input, just bigger.)

## 7. Verification hooks (regression gate)

G1 **§4 verbatim gate (mandatory).** Inputs: the four families with chains from
   GGV5 ((9,27)+(2,3); (9,24)+(2,3) [F17]; (8,28)+(3,2); (7,21)+(2,3) [F9]).
   Output must equal, corner-set for corner-set and RHS for RHS, the seven
   entries of `cases/emit.py` (reg_9_27; reg_9_24_c1/c2/c3; reg_7_21;
   open_8_28_c1/c2 with rhs x²) — including subcase counts (3 and 2) and merge
   behavior. Already validated by hand + a corner-arithmetic script during this
   design: the reconstructed T-ops reproduce all seven from the papers'
   mid-states exactly.
G2 **Discard regression.** (8,32)+(3,2) must exit with status `discarded`
   via R8+R1+R7 (the GGV22 §3 one-paragraph argument), not produce polygons.
G3 **Step invariants** (checked after every op): polygon convexity & lattice
   integrality of mandated corners; en(R) lattice test in R1; v_{ρ,σ}-consistency
   v(P)+v(Q) ≥ v([P,Q]) + ρ+σ; bracket bookkeeping (composition of recorded
   factors equals x^{j−2} at emit); (0,0) ∈ both supports; Cor 7.4 hypotheses
   logged with numeric witnesses.
G4 **Cross-check lane (optional, expensive).** For a solved family, Generator A
   on the UNREDUCED rectangle (cases/unreduced.py) and on the reduced output
   must agree on emptiness at one prime — ties the reduction to the msolve
   pipeline end-to-end.
G5 **Log audit.** Every emitted case carries the rule-by-rule log; a reviewer
   (or later, a proof assistant) can replay it against the paper propositions.
   This addresses the notes.md concern that Prop 4.3 is "trusted from the
   unrefereed GGV chain": the log makes the trust surface explicit.

## 8. Steps that require symbolic work on coefficients — honest list

The good news (established by the traces): for §4-class families the loop never
needs the VALUES of λ, α_i — only their existence, distinctness pattern, and
multiplicities. All kills are integer-arithmetic (R2–R9). What remains genuinely
symbolic, and how to handle it:

1. **The λ's of each cut**: introduced existentially by certificates; consumed
   by exactly one e_K. Handling: symbolic tokens with constraint sets; no
   arithmetic. Risk case (not hit in §4): two certificates sharing a root
   (would need relations between tokens) — detect and go `stuck`.
2. **Root multiplicity patterns** (B1): combinatorial enumeration + R4/R5
   filters; the "one or two linear factors" analysis of 4.3's proof is exactly
   GGV1 Prop 2.11(3) (a qm-th power with ≤ F-factor bound) + gap-divisibility;
   encode as: #distinct roots ≤ #factors(F̄) with multiplicities ≡ 0 mod m
   — integer-level, but the RULE must be implemented faithfully per hypothesis.
3. **λ₁ ≠ 0 side-conditions** (R5): implemented as sub-searches deriving
   support contradictions; no coefficient computation, but requires the
   recursive engine to be reentrant on hypothetical states.
4. **Aligned-end eliminations** (B3/R9): direction-clash detection = exact
   rational geometry; no coefficients.
5. **Out of scope / future**: GGV6 Thm 7.3 intersection-number discards
   (Puiseux/approximate-root data, genuinely analytic-symbolic) — not needed to
   REDUCE a family, only to discard some without solving; keep as a manual or
   later module.

## 9. Effort estimate

| Component | Size | Notes |
|---|---|---|
| Family loader (transcribe GGV5 deg≤150 tables + (q_k)) | 0.5 d | 34 rows |
| Lattice/state core (Laurent polygons, v/st/en/dir, T-ops) | 1–2 d | partly in `lib/jc.py` |
| R1–R2, R10 (certificates, finalization, bracket ledger) | 1–2 d | straightforward |
| R3 (Algorithm 1 verbatim) + R6, R7, R8 | 1–2 d | pseudocode given |
| R4, R5, R9 + branch manager + merge-by-hash | 3–5 d | the hard 40% |
| Logging, G1–G3 gates, `stuck` reporting | 1–2 d | |
| Shakedown on the 4 regressions + (8,32) | 2–3 d | expect rule-gap iterations |

Total: ≈ 2–3 weeks focused work, ~2–3 kLOC Python on top of `lib/jc.py`, for a
version that passes G1–G3. Reimplementing GGV5's enumeration (needed only past
deg 150) is +1–2 weeks, separable. Main risk: new families (chains of length
2–3, l>1 final corners such as (11/4,7), k=2 families F₄/F₁₁, A0′=(2,0) rows)
will exercise rules in combinations the four regressions don't; the `stuck`
outcome converts each gap into a bounded manual review instead of a wrong
polygon. Expect an initial farm pass to fully reduce roughly half the 34
families automatically, with the rest emitting sound partial reductions.

