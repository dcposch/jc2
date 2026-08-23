# BOOK-OFFAXIS-REVIEW.md — Adversarial review of BOOK-OFFAXIS.md (b9db83e + 36505a6), the off-axis closure package

Reviewer: Claude (adversarial deep-dive, 2026-08-12). Status: COMPLETE.
Scope: the off-axis soundness repair in full — the census (§1–§5), the two
closure lemmas R1 (§6) and R2 (§7), the td = 7 kill (§8), the stage-R
recount (§9), and cases/book_offaxis.py — re-derived from the printed
record independently, plus cross-model pass. Ground truth: refs/
sigray_full.pdf re-read on-page this session: pp. 17–18 (St 3.16–3.18,
Prop 3.2, St 3.17), pp. 39–45 (Not 8.1, St 8.1, Prop 8.1(i)–(v), St
8.2–8.5 + proofs, Prop 8.2, Cor 8.1, Props 8.3–8.4), pp. 48–52 (Not
9.1–9.3, St 9.1–9.5, Props 9.2–9.3(a)–(m) + proof, **St 9.6(i)–(v) +
proof, cells (A)/(B)/(C)**). Engines re-run: cases/book_offaxis.py (exit
0, all gates PASS, every headline number reproduced: 27 raw / 23 L6 /
2691 cells / 700 mixed / 2251 DEAD / 440 alive / 0 open / td=7 asserted
CLOSED). Independent hand recounts: td=8 m2 panel (11 dead / 3 alive —
match) and td=11 m2 (2,3)+L8 panel (4 dead / 2 alive, incl. the pinned
(κ̄,X)=(4,2) survivor — match); the "14 pinned T1-rigidity targets"
verified by instrumentation (12× (μ,w)=(1,2)⊕(2,3) M=3, 1× (1,3/2)⊕(3,2)
M=4, 1× (1,4/3)⊕(2,3/2) M=3). Adversarial machine extension: engine
rerun with the contested M-law removed (§3 below).

## Verdicts

- **Front 1 (R1 derivation): SPLIT.** R1.0 **CONFIRMED** (new
  q-multiplicity rigidity lemma: sound, genuinely load-bearing, §1).
  R1.1 **CONFIRMED** (p-shape is verbatim in St 8.5's printed proof;
  q-shape follows from R1.0). R1.2 **CONFIRMED** — the cancellation
  claim is real: deg(p_G) = i_F·l_F makes l_F drop out of Prop 9.3(b)
  exactly, and the DS2 lowest-terms step is validly replaced (§2). The
  resonance conditions Δ | num(w), den(w) | dq re-derive cleanly.
  R1.3 **GAP** and R1.4–R1.5 **REFUTED AS STATED** (§3): the dirty-vertex
  shape list omits the η^ε family, and the M-descent claim
  "M_F = gcd(dp,dq) | M_parent" at V_{2,a} vertices is CONTRADICTED by
  the thesis's own printed St 9.6(iii)/(iv).
- **Front 2 (R2 handshakes): CONFIRMED.** All four case formulas
  re-derived from Prop 9.3 (c),(d) i-normalized, (g),(h), and (i)–(m)
  + St 9.2 (§5). The searrow law (S) — the k=0 replacement, flagged as
  the likeliest error site — is literally St 8.2's printed iff and is
  SOUND. One prose overstatement in R2.2(D) (§5c).
- **Front 3 (td = 7 kill): REFUTED AS PROVED.** Steps 1, 3, 4 replay
  correctly by hand *given the alphabets*; Step 2 (chain-2 frozen at
  3/2) fails through two independent holes, each of which concretely
  reopens the panel (§3–§4). Removing the unproven M-law from the
  engine's own menu gives **td=7: 4 DEAD / 2 ALIVE** — the doc-§8/§9
  claim "td=7 CLOSED, exclusion RESTORED" does NOT stand.
- **Front 4 (engine fidelity): CONFIRMED with 3 findings.** Gates pass,
  all counts reproduce, two panels independently recounted, loop bounds
  re-proved (§6). Findings: the dirty-step menu embeds the refuted
  M-law and omits the ε-cells (load-bearing); inner-edge arrival μ is
  conflated with emitted M (m ≥ 3 completeness risk); merge-side
  cell_check handles ε ≥ 1 correctly (more conservative than §7 prose).
- **Front 5 (consistency with promoted on-axis record): CONFIRMED — no
  contradiction.** R1.2|_{l=1} = DS2 verbatim; R2.1|_{μ≡1} = DS4
  §5a/5c/5d verbatim; on-axis gate unchanged; both counterexample
  channels live strictly off-axis (Cor 8.1's M=1 hypothesis blocks them
  on-axis), and the promoted suffix record killed the St 9.6(iii)/(iv)
  cells by λ-budget — never by M-descent — which is exactly the repair
  route available here (§7).
- **Front 6 (cross-model pass): [see §8]** — both external referees run
  on the R1+R2 proofs; verdicts and reconciliation below.

**Bottom line: R1.0–R1.2 and R2.1–R2.3 are real, promotable lemmas; the
td = 7 restoration and the 2251/440 recount are NOT sound as printed
and must be retracted to "open pending R1.3/R1.4 repair". Do not
promote §8–§9.**

---

## 1. R1.0 re-derived (CONFIRMED)

From Prop 8.1(iv) δpq′ − (1−u)p′q = ⊖p, valuation at a p-root ξ of
mult μ★: v(q) = 0 gives LHS-v = μ★−1 < μ★ = RHS-v; v(q) ≥ 2 gives both
LHS terms v ≥ μ★+1 (equal leading valuations can only cancel upward);
so v(q) = 1 — every p-root simple in q. Order-μ★ coefficient:
q′(ξ)(δ − (1−u)μ★) ≠ 0 forces dp ≠ μ★·dq via δ/(1−u) = dp/dq (St 8.2's
proof). Off-p q-roots: v(q) ≥ 2 makes LHS vanish at ξ₀ against
⊖p(ξ₀) ≠ 0. At η = 0, ν ≥ 2: semi-invariance (St 3.16: p_F = η^l·p̃(η^ν);
St 8.5's proof step via Prop 4.6) + the constant term of (iv) kill
e₀ = 0 and e₀ ≥ 2, so η ‖ q; hence dq ≡ 1 (mod ν) and (via Prop 8.1(v)
M = gcd(dp,dq) | dq) gcd(M_F, ν_F) = 1. All steps check; hypotheses
δ ≠ 0, 1−u ≠ 0 are the same ones St 8.2's printed proof consumes.
This is the best new lemma of the package — it grounds the MP6(d)
backbone at every vertex with no M or μ hypothesis.

## 2. R1.2 re-derived (CONFIRMED) — the cancellation is real

Prop 9.3(b) at a chain edge G → F, i-normalized with deg(p_G) = i_F·l_F
(St 3.17(i): deg(p_G) = mult(p_F, c) = i_F·mult(p_F^red, c), St 8.3(ii)/
Prop 8.1(i)): dp_F/dq_F = l_F(ρ_G + n_e)/(κ̄_G + n_e). With R1.1's
(dp, dq) = (l_Fν_F, n_Fν_F + 1) the LHS is l_Fν_F/(n_Fν_F+1) and l_F
cancels EXACTLY, leaving ν_F/(dq_F) — in lowest terms since
gcd(ν_F, n_Fν_F+1) = 1. So ρ_G + n_e = tν_F, κ̄_G + n_e = t·dq_F,
t = w_Gν_G/Δ_F, and (c),(d) give κ̄_F = t·dq_F/ν_G, ρ_F = t/ν_G,
**w_F = w_G·n_F/Δ_F** — DS2's law verbatim in orbit degree, independent
of l_F. Resonance: κ̄_F = w_G·dq_F/Δ_F ∈ ℤ (DS1(c), M-free) with
gcd(Δ_F, dq_F) = 1 forces both den(w_G) | dq_F and Δ_F | num(w_G) —
the doc's two conditions, both correct (the second alone, as in DS3,
would be insufficient off-axis; the doc strengthens correctly).
The §2(c2) diagnosis (DS2's lowest-terms step breaks at M ≥ 2) and this
repair are both right. **R1.2 stands.**

## 3. The two holes in R1.3/R1.4 (the load-bearing failures)

### 3a. G1 — the M-descent claim is refuted by the printed record

R1.4 asserts "M_F = gcd(dp,dq) | M_parent"; §8 Step 2 kills the dirty
cells (dp,dq) = (21,15) and (20,16) by "M_G ∤ M_H = 2 — dead (St 8.5)".
But St 8.5's hypothesis is **G ∉ V_{2,a}** — it excludes precisely the
dirty vertices being discussed (the doc's own §2(c1) says so). And the
thesis REFUTES the extension: **St 9.6(iii)/(iv) (p. 51) print
Q(F) = (7j, 21j, 7, 3, 5) and (5j, 20j, 5, 4, 4) as possible children
of a Q(G) = (j, 2j, 3, 2, 5) parent** — i.e. M jumps 2 → 3 and 2 → 4
across exactly the cells Step 2 kills; the thesis keeps them, charged
λ_F ≥ 2. Worse for §8: the td = 7 chain-2 entry IS that frame —
Q(entry₂) = (2, 4, 3, 2, 5) = (j, 2j, 3, 2, 5) at j = 2, with r = 1
(St 9.6's regularity hypothesis holds at chain positions). Replaying
St 9.6's own Diophantine solutions as R1.4 transport steps from this
entry:

    (A) (21,15): E = 9,  κ̄_F = 5, M_F = 3, w_F = 2/3, n_e = 10 ∈ ℕ*
    (C) (20,16): E = 12, κ̄_F = 4, M_F = 4, w_F = 3/4, n_e = 7  ∈ ℕ*

and κ̄_F = 5, 4 and n = 10, 7 are the thesis's own printed values for
(A) and (C) — the match is exact. So w = 2/3 and 3/4 are, at printed
tier, in chain-2's alphabet (with a λ ≥ 2 charge the doc's R3 concedes
it cannot price), and W_off(3/2, 2) = {3/2} is false.

Downstream kill: with w₂ = 2/3, M₂ = 3, the interior-merge arrangement
"chain 2 at the 0-direction, μ₀ = μ₁ = 1, ν_{H₂} = w₁/w₂ = 3" passes
every R2 law: handshakes consistent (κ̄ − X = 2), κ̄ = 3, X = 1, cell
(dp,dq) = M·(1,3) = (3,9), ε = μ₀ = 1, one arriving orbit (ν_G = 2,
l_ex = 3), dq ≡ 1 (mod 2), searrow 9 > 3 both edges, M = 3 ≥ 2 (MP2).
Verified against the engine's own solver: solve_arr([(1,2)],
(1, 2/3, 3), [], 3) = ALIVE, cell_check(3, 1, [1], 1, 3) = True.
**Mechanical confirmation:** deleting the single unproven check
(`b % gcd(dp, dq)`) from w_closure_off and re-running stage R yields
W_off(3/2, 2) = {3/16, 3/8, 4/9, 2/3, 3/4, 3/2} and **td=7:
4 DEAD / 2 ALIVE** — the §8 kill and the §9 "0 open / td=7 CLOSED"
gate both fail on the engine's own arithmetic.

### 3b. G2 — the dirty shape list omits the η^ε family, which is PRINTED
### as St 9.6(II)(b) (independent hole, also refuted-by-print)

R1.3 claims "R1.0 + semi-invariance force" shapes with no η^ε factor,
and R1.4/w_closure_off parameterize dp = ν(l + Σm_j). But St 3.16
prints p_F = η^l·p̃(η^ν) with l ∈ ℕ free; a northeast 0-root (ε ≥ 1,
ε·dq < dp) at a V_{2,a} chain vertex contradicts nothing (St 3.18's
F∗0 exists but is NE, so r = 1 is untouched; the regularity/St 6.2
argument in St 9.6's proof only bounds ε < l). And the thesis PRINTS
the omitted family: **St 9.6's case (II) list has TWO shapes, (a) AND
(b) with p(η) = ⊖η(η^ν−c^ν)²Π(η^ν−c_i^ν)** — (b) is exactly the ε = 1
class R1.3 declares impossible; the doc cites "(II)(a)" and silently
drops (b). (Side finding FOR the package: (b)'s printed q carries
(η^ν−c^ν)², which violates the (iv)-valuations — R1.0, which is sound,
corrects (b)'s q to the simple-orbit form. A thesis typo caught by the
new lemma.) Concrete escapes at l = 2 from the td-7 chain-2 entry,
both passing EVERY stated law (searrow, NE bounds, R1.0, κ̄ ∈ ℤ,
n_e ∈ ℕ*) — and both EXPANDING w:

    (ε,l,ν,k)=(1,2,2,1): (dp,dq) = (7,5),  κ̄_F = 5, M_F = 1, n_e = 10,
        w: 3/2 → 2   [grok's cell; it solved Prop 8.1(iv) exactly for
        it, and this review re-verified independently by exact
        rational arithmetic: (7/5)pq′ − p′q = (3/5)p identically at
        d² = (3/2)c² — the cell is ODE-REALIZED, not merely
        menu-passing];
    (ε,l,ν,k)=(1,2,ν,0): (dp,dq) = (2ν+1, ν+1), κ̄_F = 3(ν+1),
        M_F = 1, n_e = 9ν+4, w: 3/2 → 3 (doubling, any ν ≥ 2).

Since M_F = 1, both SATISFY the G1 M-law (1 | 2): granting R1.4
entirely does not close this hole. Chain 2 then arrives (μ, w) = (1, 2)
(directly, or via 3 → 2 by the clean Δ = 3 step) — an equal-(μ,w) join
with chain 1 (κ̄ free, e.g. the IIa (2,3,1) M=2 cell): ALIVE. **A
second, independent reopening of td = 7.** Fixing R1.3 means adding the
ε-cells ((II)(b) and its general-l analogues) to the R1.4 menu and the
engine; since these steps EXPAND w, R1.5's finiteness argument must be
redone (the l = 2 ε-family self-limits only because it drops M to 1;
a general proof is needed for l ≥ 3, ε ≥ 2 with k > 0).

## 4. td = 7 replay (Steps 1, 3, 4 CONFIRMED; Step 2 fails; net: OPEN)

Step 1 ✓: b=1 chain is MP5-clean; W(2) = {2} (Δ | 2 empty); μ = 1
arrivals have dq > dp, so every root is searrow and no dirty vertex
exists — sound and fully printed. Step 3 ✓ (given alphabets): all five
0-arrangement branches re-derived by hand, including the μ₀ = 2 shape
solve (A ∈ {7,10}, A=7 → (dp,dq) = (5,7), M = 1, MP2-dead) — the
exhaustiveness guards (dq > dp ⟹ k = 0 = ε-extras; R1.0 kills doubled
q-orbits) are correct. Step 4 ✓: case-IV w < 1 vs w₁ = 2, printed
(St 9.2 + (i)–(m)). Step 2 ✗: "no clean resonant step" is CORRECT
(Δ = 3 forces dq = 5, den = 2 ∤ 5 — a nice catch), the ν = 2 and k ≥ 3
dirty branches are correctly dead, but the (A)/(C) kills rest on G1 and
the menu misses G2's ε-family. **Consequence: the td = 7 panel returns
to OPEN (2 live stage-R cells on the engine's own recount, plus the G2
channel), td = 7/11/13 are all unrestored, and the §0/§8/§9 CLOSED
claims must be retracted.** The correct printed-tier statement of
chain-2's alphabet is: {3/2} at λ-spend 0 (St 9.6(v) is exactly the
w ≡ 3/2 family), plus {2/3 (λ≥2), 3/4 (λ≥2)} via (iii)/(iv), plus
M=1-children (St 9.6(i)) whose w-values are UNPRICED by shape at
printed tier (G2).

## 5. R2 re-derivations (CONFIRMED; two notes)

(a) Cases I/II: (d) κ̄_G = (κ̄_e + n_e)/ν_e and (c) i-normalized with
deg(p_{H_e}) = i_G·μ_e give X_G = μ_e(ρ_e + n_e)/ν_e; eliminating
n_e = ν_eκ̄_G − κ̄_e yields **X_G = μ_e(κ̄_G − w_e)** — checks. Case III:
(g),(h) scale by the CHILD's ν (consistent with DEPTH §5c's promoted
reading), giving X_G = μ₀(κ̄_G − ν_ew_e) — checks. Case IV: (i) ν = κ,
(j) κ̄_e < ν_e force n∗ = ν_e − κ̄_e in the (k)-equation, and κ̄_{(0,y)}=1
(St 9.2(iii)) gives w_e = 1 − D/(μ_ei₀) < 1 — checks, for every μ_e.
The pin κ̄ = (μ_aw_a − μ_bw_b)/(μ_a − μ_b) is exact.
(b) The searrow law (S) — the k = 0 replacement — is St 8.2 verbatim:
G∗c ∈ T_a↘ iff mult(p,c)·dq > dp, with ≠ unconditional; arriving
edges are searrow, NE roots need m_j·dq < dp (via the same D5(c)/
Prop 6.8 manufacture rider the promoted MP6 already carries). Sound;
correctly strictly weaker than MP6(a)'s k = 0.
(c) R2.2(D) prose says subadditivity is "GROUNDED whenever dq > dp" —
needs ε = 0 (a 0-chain of mult μ₀ gives dp = μ₀ + νΣ′μ and M | Σμ_e
does not follow); §9's restatement "dq > dp, ε = 0" is the correct one.
R2.3(i) checks (R1.0 kills h ≥ 2; the degree count kills h = 1);
(ii)'s honesty about MP7 failing at mixed merges, with the ν = 1
(S)-pruning example 2(2ν+1) > 5ν, is verified.

## 6. Engine audit (Front 4)

Reproduction ✓ (all counts, both gates, ~0.2 s). Independent panels ✓
(§0 above; td-8 recount includes re-deriving the (1,2)-pin kill through
cell_check's ν-loop by hand). Loop bounds ✓: μ₀ < μ menu bound
ν_H < μw/(μ₀w₀); μ = 1 partner bound via dq−dp ≤ num(w)·M_G,
ν_G | μ₀ + (dq−dp) − 1, dp ≤ μ₀ + ν_G·Σμ — each re-proved, incl. the
ν_G = 1 subfamily (κ̄ ≤ w(dp+1) ≤ w·dqmax). Verdict lattice
(DEAD > OPEN > ALIVE per-node, kills only on proof) is the right
superset semantics. Findings:
1. **w_closure_off embeds G1 and omits G2** (the `b % gcd(dp,dq)`
   check is the refuted M-law; no ε-cells in the dirty menu). This is
   where the recount's soundness dies: 2251/440/0 and "td=7 CLOSED"
   are artifacts of the two holes. With G1 alone removed the sweep
   gives td=7 alive = 2; a G2-complete menu grows W further (and the
   corrected alphabets feed every panel, so ALL per-td alive counts
   are lower bounds pending repair).
2. **Inner-edge μ = emitted M conflation** (expand/expand2): the
   docstring says "inner μ_e | emitted M of the child merge" but the
   code sets the parent's arriving μ_e equal to the child's emitted M.
   Configurations (M_child, μ_e) with μ_e a proper divisor of M_child
   are represented only by the surrogate cell M_child′ = μ_e, whose
   CHILD-side shape solve uses the wrong M. m = 2 (hence td = 7) is
   unaffected; the m ≥ 3 recounts (td 11 m3, td 13 m3/m4, td 14) are
   not superset-complete as counted.
3. cell_check's ε-handling at merges (ε = μ₀ exactly when a 0-chain
   arrives; ε ∈ {0..(dp−1)//dq} otherwise when dq < dp) is CORRECT and
   more conservative than the §7 prose "(else 0)" — the stage-R merge
   solves do not depend on the unproven ε-exclusion; only the CHAIN
   menu does (G2).
4. (From grok's classification note, engine implication mine.) A
   0-edge into a ν_G = 1 merge is Prop 9.3 case (I), not (III): its
   handshake is κ̄ − X/μ₀ = w_e, un-scaled by ν_H. solve_arr applies
   the ν_H-scaled case-III form to every 0-arrangement and rejects
   ν_H = 1 via nu_ok (unless ν_i = 1), so family-I cells fed by a
   0-chain can be over-killed. No damage at td = 7 (§8's family-I row
   dies on the non-0 handshakes alone, re-checked), but a kill-side
   risk for the global recount.
Minor: §1's headline "td13 m2: [2,5]" should read [1,5] (the engine
and §1a are correct); "14 T1-rigidity targets" verified.

## 7. Consistency with the promoted record (Front 5) + the repair route

No contradiction found with DS1–DS4, MP0–MP9, BOOK-ENUM, or the
on-axis 23-entry book: R1.2 restricts to DS2 at l = 1; R2.1 restricts
to the DS4 handshakes at μ ≡ 1; the erratum correction ("mixed merges
legal already at m = 2 off-axis") is right (both b_i ≥ 2 need no
upstream jump); the on-axis gate is byte-identical. Critically, BOTH
holes are invisible on-axis: Cor 8.1 (M = 1) excludes V_{2,a} escapes
there, and the promoted td = 6 record disposed of St 9.6(iii)/(iv) in
the M = 2 SUFFIX via λ ≥ 2 + St 9.5 budget composition — never via
M-descent. That is also the honest repair route here: the (iii)/(iv)
escapes carry PRINTED λ_F ≥ 2 charges, so an off-axis budget lemma
(the doc's own R3, resolved in the "charge" direction: price the NE
orbits/dirty vertices against Σλ ≤ td − 2) is the natural instrument —
at td = 7 the budget is 5, so a bare λ ≥ 2 does not kill; the repair
must either compose charges along the whole configuration or find a
new arithmetic kill for the (3,9)-cell family. G2 needs its own
lemma-let (ε = 0 at dirty vertices, or menu extension + a new
finiteness proof for R1.5).

## 8. Cross-model pass (Front 6)

Protocol: both external referees run on a self-contained brief
(R1 + R2 + the td-7 Step-2 questions, incl. the ε-exhaustiveness and
St 8.5-hypothesis probes), 2400 s each, outputs /tmp/xr_grok.out,
/tmp/xr_codex.out.

**Grok verdicts: R1 REFUTED / R2 CONFIRMED / TD7 REFUTED.** Full
agreement with this review on every load-bearing point, reached
independently: R1.0 and R1.2 re-derived and held (incl. closing the
1−u ≠ 0, δ ≠ 0 hypotheses via Prop 8.2 / St 3.16); R1.3 refuted by the
η^ε NE-0-root family "that St 3.16 and St 9.6(II)(b) allow"; the
St 8.5 citation in Step 2 flagged as ungrounded (child ∈ V_{2,a});
searrow law = St 8.2 confirmed; R2.3(i) confirmed. Grok's sharpest
contribution is the REALIZED ε-cell (7,5) (§3b) with an exact solution
of (iv), upgrading the G2 hole from "menu-passing" to "ODE-realized",
and the case-(I)-vs-(III) 0-edge classification note (finding 4, §6).
One disagreement: grok judged the G1 cells (21,15)/(20,16) "harmless
for td=7" because their pinned non-0 joins have X < 0 — it missed the
chain-2-at-0, μ₀ = μ₁ = 1, ν_H = 3 arrangement, which this review's
engine-verified replay shows ALIVE ((dp,dq) = (3,9), κ̄ = 3, X = 1,
M = 3; patched-engine recount td=7: 4 DEAD / 2 ALIVE). Resolution: the
mechanical check overrides — G1 is independently fatal, not only a
citation error; grok's own TD7 refutation goes through its (7,5)
ε-route, so the bottom lines agree. Grok also notes the reopened
equal-w IIa join at td = 7 carries λ ≥ 2 (St 9.3: 14/2 − 5 = 2) but
"nothing printed kills it" (budget 5) — matching §7's assessment of
the repair route.

**Codex verdicts: R1 REFUTED / R2 CONFIRMED / TD7 REFUTED.** Complete
three-way convergence, reached independently: R1.0's valuations and
R1.2's l-cancellation re-derived and held ("Δ | num(w_G) and
den(w_G) | dq are sound for all l ≥ 2"); R1.3 "omits legal dirty
η-root cells" — codex produced BOTH ε-families of §3b on its own (the
doubling family (2ν+1, ν+1) "satisfies (iv), has a northeast
zero-root, and sends w ↦ 2w", and the (7,5) cell with d² = 3c²/2,
n_e = 10, (X, κ̄) = (7,5), w: 3/2 → 2, λ = 3 ≤ 5); R1.4 "misapplies
St 8.5", which "cannot kill (21,15) or (20,16), which St 9.6 itself
permits with M: 2→3, 4 and w = 2/3, 3/4" — the same
refutation-by-print as §3a. Codex additionally pinned the exact
interior IIa cell where the escaped chain meets chain 1:
(dp, dq, M, κ̄, X) = (6, 10, 2, 5, 3); confirmed the St 9.6(b) squared
q-factor is a thesis typo (independently matching the R1.0-based
observation in §3b); confirmed the searrow law and R2.3(i) at merges;
flagged "M | Σμ_e iff ε = k = 0" as holding only in the narrow/
sufficient direction (§5c agrees); noted the naive (w,b)-only closure
over the missing step is infinite but that tracking its emitted M = 1
may repair reachability (matching §3b's finiteness caveat); and
concluded "the stage-R 2251/440/0 recount and its td=7 CLOSED gate are
not certified", with Steps 1/3/4 correct only conditional on the
(false) frozen alphabets.

**Reconciliation.** All three reviewers agree on every load-bearing
verdict: R1.0–R1.2 sound; R1.3/R1.4 broken by the printed record
itself (St 9.6(II)(b) η-shapes; (iii)/(iv) M-jumps); R2 sound; td = 7
NOT restored. The only inter-referee discrepancy (grok judging the G1
cells harmless downstream) is resolved against grok by this review's
engine-verified (3,9) live cell and codex's independent
non-certification of the recount. Confidence in the composite verdict
is correspondingly high.

## 9. Required actions

1. **Retract** §0/§8/§9's "td = 7 CLOSED / exclusion RESTORED" and the
   "2251 DEAD, 440 alive, 0 open" recount; annotate §6 R1.3–R1.5 as
   GAP/REFUTED-as-stated per §3 above. td = 7 rejoins td = 11/13 as
   open panels of the off-axis frontier.
2. **Keep and promote** (after normal review cycle): R1.0, R1.1, R1.2,
   R2.1, R2.2 (with the (D) prose fix), R2.3, the §1–§3 census, the
   Step-1/3/4 arguments of §8 (as conditional kills given alphabets),
   and the §9 solver architecture (bounds are sound).
3. Repair path: (a) λ-charge/budget lemma for V_{2,a} escapes
   (St 9.6(iii)/(iv) + St 9.5); (b) ε-exclusion or ε-extended menu +
   new R1.5 finiteness; (c) fix engine findings 1–2; then re-run the
   recount and re-adjudicate td = 7.
4. Typo/prose: §1 [2,5] → [1,5]; R2.2(D) add "ε = 0".
