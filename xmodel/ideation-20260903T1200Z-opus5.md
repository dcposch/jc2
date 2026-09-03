# Blind ideation submission — round 20260903T1200Z — Opus 5

Lane: ideation-20260903T1200Z-opus5. Charged input:
xmodel/ideation-20260903T1200Z-packet.md (sha256
c90fa6876b069478f658845be6efa2bd056b2e340af7284104af4d042e6c4f95, verified).
Basis 4250a6e4. Blind: no 20260903T1200Z submission read; no in-progress lane
report read (final_status checked in .run.v2 before opening any .md).

STATUS: COMPLETE. All submission-contract items delivered (§1-§13).

## Contents
0. Headline
1. Disposition vector — APPROACHES.md rows (changes only)
2. Disposition vector — Q1-Q4 candidates and queued fronts
3. Reranked bottlenecks (proof / disproof)
4. NEW avenue
5. NEW cross-connection
6. Strongest proof attack
7. Strongest counterexample attack
8. Decisive experiment / software acceleration
9. Campaign-systems check
10. Idea cards
11. Lane dispositions (continue / redesign / stop)
12. The single first lane
13. OPEN ledger raised here (bounded quantity + cheapest test)

---

## 0. Headline

Six claims, in descending order of what I think they are worth. Everything
tagged MEASURED below was computed in this lane with the banked instruments
(`box/mohprog-drivers-20260903/full_tree_partition.py` + `repro/moh_skeleton_full.py`,
desk-scale, < 3 min total); the screen reproduces **658 → 60 → 58** and, run
fresh at n = 108, **217 → 21 → 20**, matching delta 17(r) to the row.

**H1 (hostile, on a delta promoted 14 minutes before the freeze).** The rule
just promoted as delta 17(t) — δ_i' = (k+1)·Def 5.1(3)(n', m', M_i', V_i'; s')
— is **undefined on two thirds of the current frontier**. Def 5.1(3) as
transcribed carries the factor 1/(n − M_s − 1), which is identically 1 for a
Keller pair (M_s = n − 2) and is therefore *never exercised in the source*.
After descent M_{s'}' = M_{s−1}/d_s, and the anchor n' − M_{s'}' − 1 vanishes
exactly when **M_{s−1} = n − d_s**. MEASURED: this holds on **38 of the 57
descendable C_FULL_TREE_ODE survivors at n ≤ 100**, on **12 of the 20 n = 108
screened survivors**, and on **three of Moh's printed six** (the (84,56)
rows M = [−56, 42, 77, 82] and [−56, 70, 77, 82], d_s = 7, which descend to
(12,8) with M_3' = 11 = n' − 1). Moh's p.207 descent table prints (64,48),
(75,50), (84,56) *with d_s = 4* and excludes (99,66) — i.e. **every printed
descended row has a non-degenerate anchor**, and the d_s = 7 (84,56) rows are
not in the table at all. → `OPEN[DESCENT-ANCHOR]` (§13). This does not refute
delta 17(t) on its 10/10 printed rationals; it says the rule is confirmed on a
proper subfamily and the frontier lives outside it.

**H2 (positive control for H1, and an independent reproduction of delta 17(t)).**
I re-derived the descent map on characteristic data from scratch —
n' = n/d_s, m' = m/d_s, M_i' = M_i/d_s (i ≤ s−1), d_i' = d_i/d_s, V_i' = V_i,
s' = s − 1, k = V_s − u_s − 1 with u_s = d_s − V_s — and evaluated
(k+1)·Def 5.1(3) blind. It returns **(δ₂', δ₁') = (−1, 1/2)** on
(75,50) → (15,10; M₂' = 11, V₂' = 3, k = 2) and **(−1, 1/4)** on
(64,48) → (16,12; M₂' = 13, V₂' = 3, k = 1) — the two numbers
`descent-radii-grok46` obtained by numerical Newton–Puiseux. Two independent
routes, exact agreement. Delta 17(t)'s rule is right where it is defined.

**H3 (Q1, direct answer, and a correction to the packet's framing).** The
"uniform kill mechanism" (b_min = P mod A₂ > h = d₂/(n − M₂) ⇒ forced major
zero ⇒ Prop 5.6) **cannot be turned into an all-degree statement, and the
campaign's own data already says so.** MEASURED at the selected path, level 2,
n ≤ 100: of the 60 C_FULL_TREE survivors, **25 have b > h** and survive
anyway; of the 598 killed rows, 21 have b = 0. The kill is a three-way
conjunction — (i) b > h, (ii) the forced zero subtree is infeasible *or*
(iii) the Lemma 5.3 danger flag still reaches D₁ — and (iii) is a
**path-dependent, non-scalar** datum. Any theorem built on "b > h" alone is
refuted by 25 witnesses. The packet's sentence "the uniform kill mechanism …
is uniform: can it be turned into an all-degree statement" should be retired
and replaced by the sharper true statement in H4.

**H4 (the arithmetic core of the screen, stated cleanly).** In the driver,
`lo` = d_j/(n − M_j) and P_j/Q_j = d_j/(n − M_j) **identically**: the threshold
*is* P_j/Q_j. Hence when Q_j > P_j (⟺ n − M_j > d_j) the threshold is < 1 and
"no forced major zero at node j" is exactly the **divisibility A_j | P_j**.
The screen is therefore, on that stratum, a *system of congruences along the
tree*, with A_j the reduced denominator of L·δ_j. This is the correct object
for both a cofinality construction (§7) and an all-degree theorem attempt
(§6): congruence systems have positive density along progressions unless an
obstruction is proved, which is why I expect the screened space to be
**cofinally nonempty** and why I would not stake the proof on the screen.

**H5 (a new avenue, proposed, implemented, and closed NEGATIVE in this lane).**
"Screen the descended pair" — compose C_FULL_TREE with the descent, since the
descent is a functor on characteristic data and the screen only needs
characteristic data. Delta 17(t) unblocked exactly this. I built it and ran
it: on the 19 descendable-and-evaluable screened survivors, the descended
level-2 node has a forced major zero in **0 cases**, and A₂' = 1 (trivial
Galois capacity) in 8 of 19. The composite screen is **vacuous**. This is the
strongest available evidence for the coordinator's own Q4 dichotomy: after
descent the tree stops constraining, which is *why* Moh had to compute
coefficients. Reporting a negative avenue is cheaper than someone else
proposing it next round. → §4.

**H6 (the single first lane).** `appendix2-uniform-shape-opus5` — not another
census lane. Rationale and design in §12.

---

## 1. Disposition vector — APPROACHES.md 46 rows (changes only)

Unlisted rows: NO CHANGE. All moves are relative priority within the campaign,
not re-typing of any promoted claim.

| Row | Move | Reason (today's ledger) |
|---|---|---|
| 1 GGV corner families / `[P,Q] = x^k` | **UP, to co-first** (was "tried, stuck") | Theorem (T) (delta 17(q)) *is* row 1's object: monomial-Jacobian pairs, bounded tower height s' = 2, unbounded degree, one-place data compressed to four integers. Row 1's stuck-point ("always a next pair", no degree ceiling) is now **exactly** the missing uniform obstruction in (n', m', M₂', V₂'). The campaign's certificate machinery is the right engine and has never been pointed at a *tower-constrained* family. |
| 6 Abhyankar–Moh one-place | **UP, from "category error" to LIVE (restricted)** | The category error was applying AMS to fibres. The descended pair is a different object: total degree = π-degree and leading forms L_P = H^{p}, L_Q = H^{q} with H monic of degree gcd(n',m') — an **approximate-root** configuration (Moh: f = h² + 2β, g = h³ + G₁h + G₀). This is AMS's home category, applied to h, not to a fibre. New cross-connection, §5. |
| 25 dessins / Hurwitz passports | **DOWN to CLOSED-AS-KILL** | `dessin-tower-dim-grok46`: expdim = max(k−2,0) ≥ 0 everywhere; 0 negative in the D ≤ 120 slice. Hurwitz combinatorics cannot finish. Retain only the 19 rigid (expdim 0) assignments as CE candidates — and note they must now be re-run against C_FULL_TREE, which nobody has done. |
| 32 collision ideal / saturation accelerator | **UP** | Row 32's promoted accelerator `I : Δ = I : Δ^∞ = I + (det A)` (three-generator presentation, no saturation) is precisely the bottleneck in Appendix-II-style endgames: m2-descent's (15,10) kill and descent-radii's 12-unknown slice both ended in a Rabinowitsch saturation. Re-target row 32 from "prove the ideal is (1)" (= JC2) to "**be the saturation engine for the descended systems**". This is a tooling upgrade with an immediate client. |
| 36 guided CE search | **REDIRECT, priority UP** | The search space is no longer "enormous": after C_FULL_TREE it is a congruence-defined thin set (H4). Retarget from random/sparse supports to **solving the congruence system A_j \| P_j along the tree** for a one-parameter family (§7). |
| 2 boundary trees / Eggers–Wall | **DOWN in relative priority (no re-typing)** | Still the deepest banked structure, but it computes N and the boundary, and the frontier moved to multiplicity + coefficient level. Its td-ceiling gap is unchanged and untouched by today. |
| 4 formal-germ certification / D-series windows | **HOLD, with one new client** | The descended pair's γ-adic expansion at γ = 0 is a D-series-type window with a *monomial* Jacobian; row 4's window machinery could certify emptiness of the γ-adic prolongation of (T) at bounded order. Cheap, and it is the only row-4 client with a finite target. |
| 3 vertex-gap / strip ODEs | **HOLD, cross-connected** | Row 3's ODE rigidity and Moh Prop A.3's (3.7) are the same phenomenon in two dialects; §5 names the dictionary and the degeneration of (3.7) under a monomial Jacobian. |
| 19 char-p / Witt, 20 p-curvature, 21 p-adic | **DOWN** | No contact with the tree/coefficient frontier; freeze. |
| 5, 8–11, 13, 14, 17, 22–24, 37–46 | **NO CHANGE** | Nothing today touches them. |

---

## 2. Disposition vector — Q1–Q4 candidates and the queued fronts

| Candidate | Disposition | One-line reason |
|---|---|---|
| **Q1** "screened space is cofinally nonempty" | **LIKELY TRUE — do not stake the proof on the screen** | H4: on the Q > P stratum the screen is a congruence system; congruence systems are cofinally satisfiable unless obstructed. Growth 113 (D ≤ 120) → 1,516 (D ≤ 200) is superlinear. |
| **Q1** "b_min > h ⇒ Prop 5.6" as an all-degree theorem | **REFUTED as posed** | 25 of 60 survivors satisfy b > h (MEASURED, §0 H3). Needs the danger flag, which is path-dependent. |
| **Q1** exhibit a screened cofinal family (closed form) | **PROMOTE to the CE-side target** | §7 gives the construction recipe and the exact algebra to solve. |
| **Q2** "(T) is the uniform form of SIBLING-COEFFICIENTS" | **PARTLY — (T) is the *terminal* form, not the uniform form** | (T) applies only after descent, i.e. only when u_s = 1 (57/58 at n ≤ 100 — good) *and* the anchor is non-degenerate (19/57 — bad, H1). SIBLING-COEFFICIENTS is the pre-descent statement and is strictly larger. |
| **Q2** tree-decorated moment engine | **CONTINUE, but reprice DOWN** | The whole tree supplies the *combinatorial* decoration (which factor extends where); three lanes (d105-rank-gate, fixed-n6, a2six) independently hit the wall that the *analytic* decoration (contact, tail support, sharing) is **not** determined by the skeleton + tree. The tree does not close that gap; it renames it. Dictionary in §5, with the missing entries marked. |
| **Q2** cheapest exact discriminator on the first D = 108 survivor | **the descended Appendix-II system, not the moment matrix** | §8. |
| **Q3** attack (T) via row-1 machinery | **PROMOTE** | See §6; the leading-form rigidity L_P = H^{n'/d}, L_Q = H^{m'/d} is free and unexploited. |
| **Q3** uniform obstruction in (n', m', M₂', V₂') | **OPEN, and I give the shape it must have** | §6: it must be a statement about the **γ-adic order ladder**, because the unknown count grows like d² and no bounded Gröbner argument can be uniform. |
| **Q4** "the proof must be the coefficient computation" | **I AGREE, with one named escape** | H5 is the strongest evidence: the tree is vacuous after descent. The escape is §4's (N2). |
| Queued: tree-decorated moment engine | **CONTINUE at reduced priority** | Above. |
| Queued: P202 residue (52 rows) through the sibling system | **STOP as posed; REDESIGN** | It targets OPEN[MOH-PROGRAM-ARTIFACT], which is a *historical* question (what Moh's CDC listing did), not a mathematical one. Zero resolution value. Redesign as: run the 52 rows through the **descent + anchor test** (H1) — that is a 10-minute job with resolution value. |
| Queued: box01 restart for heavy Gröbner | **CONTINUE — and it now has a real client** | The descended systems (42 unknowns for G2) are over the desk cap. This is the one genuine compute need on the board. Human gate: the fleet key. |

---

## 3. Reranked bottlenecks

### Proof side (what stands between the campaign and a theorem)

1. **`OPEN[DESCENT-ANCHOR]` (NEW, this lane).** Def 5.1(3) is ill-defined on
   the descended data of 38/57 screened survivors and 3 of Moh's six. Until
   this is repaired, *the descent programme does not reach the frontier* —
   theorem (T) can only be posed on 19 of 57 rows. This displaces everything
   below it because it is upstream of all of them and costs half a day.
2. **A uniform obstruction for (T)** in (n', m', M₂', V₂', k). Previously
   ranked #1; still the theorem that ends the campaign along Moh's line, but
   it is now gated by #1 and by MINOR-DICHOTOMY.
3. **`OPEN[MINOR-DICHOTOMY]` (u_s > 1).** MEASURED: only 1 of 58 survivors at
   n ≤ 100 has u_s > 1, and 1 of 20 at n = 108. **This is much less of a
   bottleneck than the packet implies** and should be demoted from the
   "(T) + descent + MINOR-DICHOTOMY = JC2" triple to a small residue: the
   overwhelming majority of the screened frontier is u_s = 1. Reprice: it was
   4,012/14,016 groups at 48 ≤ D ≤ 200 *before* the screen; the right number
   is the post-screen one, which nobody has computed (10-minute job).
4. **`OPEN[SIBLING-COEFFICIENTS]` at a node** — genuinely the residual Moh
   names on p.143, and the only pre-descent coefficient-level statement.
5. **`OPEN[FULL-TREE-RECENTER]`** (55 → 20; a quantifier change on Prop 5.4).
   High leverage per unit of source-reading: it is a *reading* question with a
   3× effect on the census. Cheap, and nobody is on it.
6. `OPEN[PASSPORT-SHARPNESS]` (3 rows, EXTERNAL) — low value, keep parked.
7. `OPEN[MOH-PROGRAM-ARTIFACT]` — **demote to zero**. It is archaeology.

### Disproof side (what stands between the campaign and a counterexample)

1. **A screened cofinal family in closed form** (§7). Now the sharpest CE-side
   object, because the screen is congruence-shaped (H4) and both previously
   promoted rays died to a *congruence*, not to a geometric obstruction. If
   the congruence can be satisfied identically along a ray, the skeleton route
   is closed as a proof route in one stroke.
2. **The 19 rigid (expdim 0) dessin assignments, re-run against C_FULL_TREE.**
   Nobody has intersected these two lists. If any rigid assignment survives the
   screen it is the single most concrete CE candidate the campaign owns —
   rigid means *no moduli to search*, so it can be solved exactly.
3. Realisation of a D = 108 survivor at the coefficient level (the sibling
   system). Expensive; only after 1 and 2.
4. Everything else (char-p lifts, sparse search, Pinchuk) — unchanged, low.

---

## 4. NEW avenue

### (N1) THE DESCENT LADDER / COMPOSITE SCREEN — proposed, built, MEASURED, and closed NEGATIVE

*Idea.* The descent (Prop 6.3/6.4) is a **functor on characteristic data**:
(n, m, M_i, d_i, V_i, s) ↦ (n/d_s, m/d_s, M_i/d_s, d_i/d_s, V_i, s−1), and
C_FULL_TREE consumes nothing but characteristic data. Delta 17(t) unblocked
(8)–(13) on descended pairs. Therefore the screen **composes along the
descent**: screen at level s, descend, screen at level s−1, …, a ladder of
depth ≤ s − 1 ≤ 4 whose composite is a strictly finer screen on the original
row, uniform in D, computable today.

*Executed.* Implemented the descent map, validated it against p.207/p.208
(H2: (−1, 1/2) and (−1, 1/4) reproduced exactly), then evaluated the
descended level-2 Galois node — A₂' = denominator of L'·δ₂', P₂', Q₂',
b' = P₂' mod A₂', h' = d₂'/(n' − M₂') — on every descendable
C_FULL_TREE_ODE survivor at n ≤ 100.

*Result (MEASURED).* 57/58 survivors are descendable (u_s = 1); 38 are
blocked by `OPEN[DESCENT-ANCHOR]`; of the **19 evaluable, 0 have a forced
major zero** at the descended level-2 node, and **8 of 19 have A₂' = 1**
(trivial Galois capacity — no congruence at all). Sample:

```
parent          descended                k   δ₂'    δ₁'   A₂' A₁'  P'  Q'  b'  h'   forced0
(64,48,V₃=3) -> (16,12, M₂'=13, V₂'=3)   1   -1     1/4    1   4    4   3   0  4/3   False
(75,50,V₄=4) -> (15,10, M₂'=11, V₂'=3)   2   -1     1/2    1   2    5   4   0  5/4   False
(84,56,V₃=3) -> (21,14, M₂'=16, V₂'=2)   1   -1/2   7/6    2   3    7   5   1  7/5   False
(90,60,V₄=4) -> (18,12, M₂'=9,  V₂'=3)   2   -3/2  -3/4    2   2   10  15   0  2/3   False
(96,64,V₃=3) -> (24,16, M₂'=12, V₂'=3)   1    0     1/3    1   1    4   6   0  2/3   False
```

*Reading — and this is the real content.* **The composite screen is vacuous,
and that is a theorem-shaped fact about the architecture of Moh's proof.**
After one descent the Galois capacity collapses (A₂' = 1 on 8/19; h' > 1 on
most rows so even b' = 1 is harmless), so no multiplicity/orbit argument can
say anything more. This is *why* Appendix II is a coefficient computation and
not a fifth filter. It is the strongest evidence in the campaign for the
coordinator's Q4 dichotomy, and it is a genuinely new datum: the previous
argument for "the proof must be coefficients" was the absence of a working
filter, not a measurement that the filter is *empty*.

*Caveats, typed.* The descended pair is **not Keller**: J = cγ^k. Two screen
ingredients are therefore not licensed verbatim: (i) Prop A.3's (3.7)
(P − Qu)q_a(a) = c degenerates to = cγ^k, whose right side **vanishes on
γ = 0** — exactly the locus the descended discs live on, so the ODE
non-degeneracy that took 60 → 58 is *unavailable* after descent; (ii) Prop
5.6's hypotheses are unverified for a monomial Jacobian. Since the probe
returned no kills, neither caveat changes a conclusion — the negative result
is robust to both (weakening the screen cannot create kills). If a future lane
wants to claim a *kill* from the composite screen, both must be closed first.
`OPEN[DESCENDED-TREE-LICENSE]` (§13).

### (N2) THE ESCAPE FROM Q4'S DICHOTOMY: RIGIDITY-FIRST, NOT DEGREE-FIRST

The three layers (boundary → N, tree → multiplicities, coefficients →
freedom) are all indexed by **degree**, and every one of them has now failed
to produce a ceiling in D. A mechanism outside all three: **index by moduli
instead.** `dessin-tower-dim-grok46` computed expdim = max(k−2, 0) and found
**19 assignments with expdim 0** in D ≤ 120. A rigid assignment has *no
continuous freedom at the coefficient level either* — the sibling system is
zero-dimensional by construction, so the Appendix-II endgame on it is a finite
exact solve with no shape reduction needed. Nobody has intersected the 19 with
C_FULL_TREE. This is a mechanism that is neither boundary, nor tree, nor
"coefficients as freedom": it is **coefficients as no freedom**, and it turns
the hardest step (an underdetermined system in growing unknowns) into the
easiest (a zero-dimensional ideal). It cannot prove JC2 — it is a finite list
— but it is the cheapest possible route to a counterexample or to a decisive
negative, and it costs one afternoon. Card 2 (§10).

---

## 5. NEW cross-connections

**(X1) The descended pair is an approximate-root object — row 6 (Abhyankar–Moh)
re-enters, correctly this time.** Since deg_total P = deg_π P = n' and
deg_total Q = deg_π Q = m' (delta 17(q): "the descended pair has total degree
= π-degree"), the degree-(n'+m'−2) part of J(P,Q) is J(L_P, L_Q) where L_P,
L_Q are the binary leading forms. For k < n' + m' − 2 (true on every row I
measured: k ≤ 11, n' + m' − 2 ≥ 8 and usually ≫) this forces
**J(L_P, L_Q) = 0**, hence for binary forms L_P^{m'} ∝ L_Q^{n'}, hence
**L_P = H^{n'/d}, L_Q = H^{m'/d} with H monic of degree d = gcd(n', m')**.
Check against Moh: (15,10) ⇒ d = 5, p:q = 3:2 — and Moh's Appendix II writes
exactly f = h² + 2β, g = h³ + G₁h + G₀ with **h monic of degree 5**
(m2-descent, delta 17(q)); (21,14) ⇒ d = 7, same 3:2. So Moh's h *is* the
approximate root whose leading form is H, and Appendix II is an
Abhyankar-approximate-root computation. Consequence: the campaign may import
the approximate-root calculus (Abhyankar's expansion, the (n'/d, m'/d)-adic
expansion, Moh's own 1973 theory) wholesale into (T). **Nothing in the banked
reports names this.** It also predicts the unknown counts: h has
d(d+1)/2 coefficients (15 for d = 5, minus 1 normalisation = **14** — exactly
descent-radii's "14 (h)"), and β has the residual — the counts are *derived*,
not empirical.

**(X2) Prop A.3's (3.7) ↔ row 3's strip ODE, and its degeneration.** The ODE
consequence promoted in delta 17(r) — (P − Qu)q_a(a) = c at a simple q-root,
so P − Qu ≠ 0 — is row 3's "face valuation orders bracket equations; the strip
block collapses to a rigid ODE" in Moh's coordinates. The cross-connection has
teeth in one direction: under descent the constant c becomes cγ^k, and the
non-vanishing conclusion **fails on γ = 0**. So the ODE filter is a
*Keller-only* filter; it took 60 → 58 before descent and takes nothing after.
Row 3's known scope limit ("d₁ = 1, depth two, k ≥ 2 only") is the same
restriction seen from the other side. Actionable: row 3's Ore/resultant
depth-three extension, if it exists, is the missing "(3.7) for a monomial
Jacobian".

**(X3) The threshold *is* a ratio of the two Galois data.** `lo` = P_j/Q_j
identically (H4). So Moh's Prop 5.3 threshold "V_r > d_r/(n − M_r)" is not an
external inequality — it says a factor is major iff its multiplicity exceeds
**deg p_j / deg q_j**, i.e. iff it is above the *average* p-multiplicity per
q-root. That is a clean, uniform, source-faithful restatement worth putting in
the ledger, and it makes the "capacity" picture (Q = ε + AS) and the threshold
one object rather than two.

**(X4) Row 32's saturation accelerator is the missing engine for Appendix II.**
Both endgames that have actually killed something (m2-descent's corrected
(15,10) Case 2, descent-radii's 12-unknown slice) ended in a Rabinowitsch
saturation. Row 32 owns a promoted theorem — for a Keller secant matrix A,
I : Δ = I : Δ^∞ = I + (det A), a three-generator presentation with **no
saturation needed**. Whether it transports to a *monomial* Jacobian is a
one-page check (replace det A = 1 by det A = cγ^k). If it does, every
Appendix-II endgame loses its most expensive step. `OPEN[SAT-MONOMIAL]` (§13).

---

## 6. Strongest proof attack

**Target: theorem (T), attacked through the leading form, not through the
coefficient system.**

The received plan for (T) is "reduce to Appendix-II size, then exact-solve".
That plan cannot be uniform: by (X1) the unknown count is d(d+1)/2 + O(d²) with
d = gcd(n', m') → ∞, so no fixed Gröbner computation covers all degrees. A
uniform obstruction must be a statement whose *size does not grow*. There is
exactly one such datum available: the **γ-adic order ladder** of the pair.

*The attack.* Write the pair in the H-adic (approximate-root) expansion of
(X1): P = h^{p} + Σ_{i<p} A_i h^{i}, Q = h^{q} + Σ_{j<q} B_j h^{j}, with
p = n'/d, q = m'/d, gcd(p,q) = 1, h monic of π-degree d. m2-descent already
proved the ladder's first rung, source-checked on pp.208–210: **Lemma 2.1 for
a monomial Jacobian — g_j ∈ k for j < m' − 1 and deg_x g_{m'−1} = k + 1.**
That is a *degree-independent* statement: all but O(1) of the expansion
coefficients are **constants**. Conjecture to attack:

> **(T-LADDER).** For a monomial-Jacobian pair with total degree = π-degree,
> the H-adic coefficients A_i, B_j are constants for all but at most a bounded
> number of indices, and the non-constant ones have γ-degree ≤ k + 1.

If (T-LADDER) holds with an absolute bound, then the whole moduli of the pair
is a **bounded** number of unknowns of **bounded** degree plus the coefficients
of h — and h is then determined by the (n', m', M₂', V₂') data via Def 5.1's
radii. That is a uniform obstruction: (T) becomes a finite computation
independent of d, and the campaign's row-1 certificate machinery finishes it.

*Bounded quantity.* The number of non-constant H-adic coefficients, and their
γ-degrees, for the pairs at hand. *Cheapest test (< 10 min, desk):* take
Moh's own (15,10; M₂'=11, V₂'=3, k=2) and (16,12; M₂'=13, V₂'=3, k=1) shapes
from `box/descentradii-drivers-20260903/` (the h/β shapes are already coded in
`g2_fullh_mohbeta.py`, `g2_newton_solve.py`), compute the H-adic expansion of
the *general* pair in the shape, and read off which coefficients the Jacobian
equation forces to be constants. Positive control: Moh's own reduction
"22 [15 or 13] unknowns" for (15,10) must come out; negative control: run the
same on a Keller (k = 0) automorphism witness from m2-descent's twelve, where
the ladder must *fail* to be bounded (automorphisms exist in all degrees).

*Interpretation.* If the bound is absolute → (T) is finite, and the proof of
JC2 along Moh's line reduces to one computation plus MINOR-DICHOTOMY (which
is a 1-in-58 residue, §3). If the bound grows with d → (T) has no uniform
obstruction of this shape, and Q4's dichotomy resolves against the coefficient
route as well; the honest conclusion would then be that Moh's line does not
close and the campaign should re-weight to row 2's ceiling problem.

*Why this beats the alternatives.* The screened-census route (Q1) is refuted
as a theorem generator by H3; the moment-engine route is walled by
non-intrinsic decoration (three independent lanes); the composite screen is
vacuous (H5). (T-LADDER) is the only remaining candidate with a
degree-independent statement, and its first rung is already proved and
source-checked.

`charge_basis={"delta":"3/2","branch":"q>=2","flag_count":1,"citation":"refs/moh1983_jram340_configurations_of_roots.pdf:p.208-210 (Prop 6.3 expansion; Lemma 2.1 for a monomial Jacobian)"}`

---

## 7. Strongest counterexample attack

**Do not search the screened census. Solve its congruences.**

Both promoted cofinal rays died to the *same arithmetic accident*: Sol's
L = 8a + 5 ray died because b_min = 10a + 7 > h = (8a+5)/(16a+11) — i.e.
because b_min ≠ 0 and h < 1; the A₂ = 6 ray died because b = 3 > 3/5. By H4,
what killed them is **A₂ ∤ P₂**, and nothing else. So the construction is:

> Build a one-parameter family (n(t), m(t), M_i(t), V_i(t)) satisfying
> (1)–(13) with **A_j(t) | P_j(t) for every j on the selected path and every
> sibling branch**, where P_j = V_{j+1}d_j/d_{j+1} and A_j is the reduced
> denominator of L·δ_j from Def 5.1(3).

This is solvable in principle because both sides are *explicitly rational in
t*: the δ_i are ratios of products of linear forms in the V's and M's, so
along a ray with M_i(t), V_i(t) linear in t, the denominators A_j(t) are
eventually periodic in t and P_j(t) is linear — a congruence
P_j(t) ≡ 0 (mod A_j(t)) with eventually-constant modulus, hence solvable on
an arithmetic progression **unless** the residue is constant and nonzero. The
two dead rays are exactly the "constant and nonzero" case. Nobody has asked
whether that is *forced*.

*Bounded quantity.* For each of the 20 n = 108 screened survivors and each
group at D = 112, 120: the pair (A_j, P_j mod A_j) along the selected path,
and whether the family obtained by the obvious linear extension in t keeps
b_j ≡ 0. *Cheapest test (< 5 min):* the level-data routine used in this lane
(`TreePartition.level_data`) already emits (A, P, Q, P mod A, lo) per node;
run it over the n = 108/112/120 screened survivors with V_2 varying and read
whether b = 0 is attained on a progression. If yes, extend to a ray and hand
it to the realisation clients. If the residue is provably constant and nonzero
along every linear extension, that is a **new all-degree kill mechanism** —
and it is the theorem Q1 was fishing for, in its correct (congruence) form
rather than its false (b > h) form.

*Second CE target, cheaper still.* Intersect the 19 rigid dessin assignments
(expdim 0, D ≤ 120) with C_FULL_TREE_ODE. Rigid ⇒ zero-dimensional
coefficient system ⇒ exactly solvable. Ten minutes of list intersection; if
nonempty, the resulting system is the most concrete CE candidate in the
campaign. If empty, that is itself a clean statement: *the screen kills
exactly the rigid stratum*, which would be strong evidence for the proof side.

---

## 8. One decisive experiment / software acceleration

**DECISIVE EXPERIMENT: the anchor audit of the descent programme (H1).**

*Statement.* Determine whether Moh's Prop 6.3/6.4 descent, and the promoted
δ' rule, are defined when M_{s−1} = n − d_s (equivalently M_{s'}' = n' − 1,
equivalently the Def 5.1(3) anchor n' − M_{s'}' − 1 = 0).

*Why decisive.* It gates 38 of the 57 descendable screened survivors at
n ≤ 100, 12 of the 20 at n = 108, and **three of Moh's printed six**. If the
descent is undefined there, theorem (T) as stated does not cover the frontier
and (T) must be restated (or a second reduction found) — a change to the
proof programme, not a detail. If it *is* defined under a different
normalisation, then the promoted rule needs a repair and every δ'-consuming
computation (including the Appendix-II shape reductions) must be re-run.

*Cost.* Half a day, desk-scale. *Method.* (a) Read Moh pp.207–208 as images:
does the printed descent table contain any row with M_{s−1} = n − d_s?
(prediction: no — it prints (64,48), (75,50) and the d_s = 4 rows of (84,56),
and excludes (99,66)). (b) Read Def 5.1(3) at p.179: is the factor
1/(n − M_s − 1) in the source, or a transcription artefact of the Keller
normalisation M_s = n − 2? (prediction: in the source — setting the
denominator to 1 gives δ₂' = −3 instead of −1/3 on (15,10), measured here).
(c) If it is in the source and vanishes after descent, the descended pair has
top characteristic exponent n' − 1: decide from Prop 6.3 (pp.196–199) whether
that is possible at all. It may be that anchor-zero rows simply **do not
descend**, in which case `OPEN[MINOR-DICHOTOMY]` is far larger than the 1/58
count suggests.

*Positive control (must pass).* (75,50) → (−1, 1/2) and (64,48) → (−1, 1/4),
already reproduced twice (H2). *Negative control.* Any candidate repaired
normalisation must still reproduce all 10 printed p.207 rationals.

*Interpretation matrix.* undefined-and-non-descendable → (T) is incomplete,
restate the programme; undefined-but-repairable → repair delta 17(t), re-run
the composite screen (§4) on the newly evaluable 38 rows (this is the one way
H5's negative could flip); defined-as-is with a limit interpretation
(δ' = −∞, i.e. the descended disc degenerates) → that is itself a *kill*
candidate, and the 38 rows may die outright, which would be the largest
single cut since delta 17(r). All three outcomes are informative; there is no
null outcome. *Stop condition:* a verdict on (a)+(b), or 4 hours.

**SOFTWARE ACCELERATION (secondary, cheap).** Add a `descend()` +
`anchor_ok()` pair to `box/mohprog-drivers-20260903/full_tree_partition.py`
(≈ 30 lines; I wrote and validated both in this lane) and emit, for every
screened row, the tuple (n', m', M_i', V_i', k, δ', A_j', P_j', b_j',
anchor_ok). That single table is the input to (T), to the anchor audit, to
the composite screen, and to the Appendix-II compiler — four lanes currently
recomputing it separately. One hour of work; it removes a recurring cost.

---

## 9. Campaign-systems check

**UPGRADE — one card, smallest useful test.**

*Observation.* Delta 17(t) was promoted at 11:58Z and the round froze at
12:00Z. Within 20 minutes of desk work in this blind lane, the promoted rule
turned out to be **undefined on two thirds of the frontier it was promoted to
serve**, including three of Moh's printed six. The different-model hostile
gate did its job on the *source fidelity* question (10/10 printed rationals)
and did not ask the *coverage* question (on how many live rows is the new
object even defined?). This is a systematic blind spot: every recently
promoted filter/rule has been validated against Moh's printed rows, which are
a **6-row, non-random, historically-selected sample** of a 1,500-group
frontier.

*UPGRADE card — "COVERAGE LINE".* Every promotion of a rule, filter or formula
must carry one additional printed line before it can be consumed by the
frontier:

```
coverage={"defined_on": <count>, "of_live_rows": <count>, "undefined_reason": "<string>",
          "printed_controls_covered": <count>/<count>}
```

*Smallest useful test (do this once, retroactively, ~20 min).* Compute the
coverage line for the four rules promoted today — C_FULL_TREE (17r),
the ODE consequence (3.7) (17r), the δ' rule (17t), and the descent map
(17q/t) — on the 58 screened survivors at n ≤ 100 and the 20 at n = 108. I
have already done it for two of them: δ' rule = 19/57 defined (reason: anchor
zero), descent map = 57/58 defined (reason: u_s > 1). If any other rule comes
in below 100 %, the ledger has an undeclared restriction.

*Why this and not a process change.* The hostile-gate discipline is working —
I am not proposing more review, only one more *number* per promotion, which is
mechanical and would have caught H1 before the round froze.

*Everything else: NO_CHANGE, with evidence.* Lane sealing/receipt discipline
held (I could check `final_status` in `.run.v2` for all six named lanes and
correctly opened only the two DONE ones); the blind-packet mechanism worked
(hash verified, single charged input); the instruments reproduced their
headline numbers on first run with no repair (658 → 60 → 58; 217 → 21 → 20 at
n = 108) — that is a strong signal for the driver hygiene of
`box/mohprog-drivers-20260903/`.

---

## 10. Idea cards (three)

### CARD 1 — `descent-anchor-audit` (the H1 repair)

*Dependencies.* Moh pp.179, 196–199, 207–208 as images; the descent map
(validated here); `box/descentradii-drivers-20260903/`. No compute beyond desk.
*Cheapest discriminator.* Does any printed p.207 descended row have
M_{s−1} = n − d_s? Prediction: no. Second: is 1/(n − M_s − 1) present in
Def 5.1(3) at p.179? Prediction: yes (dropping it breaks the 10/10 match —
measured here).
*Interpretation of each outcome.* See §8's matrix (three outcomes, all
informative, none null).
*Stop condition.* Verdict on both questions, or 4 hours.
*Expected information gain.* HIGH. It re-prices theorem (T)'s coverage from
"the frontier" to "19/57 of the frontier" or repairs it; either way it changes
what the next flagship should be. It is also the only item on this board that
can *invalidate* a promotion made today.
*Risk.* Low; pure source + arithmetic.

### CARD 2 — `rigid-stratum-intersect` (the cheapest CE shot the campaign has)

*Dependencies.* The 19 expdim-0 assignments from `dessin-tower-dim-grok46`
(§6.4 of that report); `full_tree_partition.py`; `nested_pack.py`.
*Cheapest discriminator.* Intersect the 19 with C_FULL_TREE_ODE survivors
(list intersection, minutes). Then, for any survivor, the coefficient system
is zero-dimensional — solve it exactly with the row-32 accelerator.
*Interpretation.* Nonempty → the single most concrete CE candidate in the
campaign, with **no moduli to search**, solvable exactly; empty → "the screen
kills exactly the rigid stratum", a clean structural statement supporting the
proof side and worth a ledger line.
*Stop condition.* The intersection is computed; if nonempty, one exact solve
per survivor, capped at 30 unknowns (else hand to box01).
*Expected information gain.* MEDIUM-HIGH, and the cost is one afternoon. This
is the highest information-per-hour item on my board after Card 1.
*Risk.* expdim is a *Hurwitz* dimension, not the coefficient dimension; expdim
0 does not strictly imply the sibling system is zero-dimensional. Type it as a
heuristic selection, not a theorem — it is still the right list to solve first.

### CARD 3 — `t-ladder` (the proof attack of §6)

*Dependencies.* Card 1's verdict is *not* a blocker (the ladder can be tested
on the 19 evaluable rows and on Moh's own shapes); `descentradii-drivers`'
h/β shape code; sympy.
*Cheapest discriminator.* On Moh's (15,10; k = 2) and (16,12; k = 1) shapes,
expand the general pair H-adically and count how many coefficients the
Jacobian equation forces to be constants, and the γ-degree of the rest.
Positive control: Moh's own "22 [15 or 13] unknowns" must be recovered.
Negative control: a k = 0 automorphism witness from m2-descent's twelve, where
the ladder must be unbounded.
*Interpretation.* Absolute bound → (T) is a finite computation and JC2 along
Moh's line reduces to it plus a 1-in-58 residue; bound growing in d → no
uniform obstruction of this shape, Moh's line does not close, re-weight to
row 2.
*Stop condition.* The two shapes are expanded and the count is printed, or
150 min.
*Expected information gain.* HIGHEST of the three if it succeeds, but with the
highest variance — this is the flagship, not the first lane. It should be
launched *after* Card 1 tells us which rows (T) must cover.

---

## 11. Lane dispositions

| Lane | Disposition | Reason |
|---|---|---|
| `whole-tree-review-opus5` (2nd gate, RUNNING) | **CONTINUE** | It gates the round. Nothing here bears on it: H1 is downstream of the tree obligation and does not touch Props 4.6/5.3/5.6. |
| `sibling-coefficients-sol56` (RUNNING) | **CONTINUE, with a redirect at harvest** | The right lane on the right OPEN. Redirect: its D = 108 survivor should be chosen with `anchor_ok = True` if it is going to be descended, and its (90,60) row should be checked against §6's H-adic ladder rather than solved raw. |
| `screened-census-grok46` (RUNNING) | **CONTINUE, redesign the cofinality half** | The census-to-D ≤ 400 half is valuable and irreplaceable. The "search for a screened cofinal family" half should be replaced by §7's **construction** (solve A_j \| P_j) — searching a congruence-defined set for a ray is strictly worse than solving the congruence. Feed this in at the next harvest, not by interrupting. |
| `descent-radii-grok46` (DONE, delta 17(t)) | **REOPEN as Card 1** | Its result is correct and reproduced here; its *coverage* is 19/57. Card 1 is the natural successor and belongs to the same lane family. |
| `a2six-ray-moment-sol56` (DONE, witness-only) | **STOP** | Sealed; the ray is dead under the screen; the moment-engine programme is correctly closed pending a tree-decorated engine, and §2 prices that down. No successor. |
| `appendix2-compiler-grok46` (RUNNING) | **CONTINUE — this is the right flagship** | It is the only running lane pointed at the coefficient level in a *uniform* way. At harvest, hand it §6's (T-LADDER) framing and (X1)'s approximate-root dictionary; both make its shape reduction derived rather than empirical. Also hand it (X4): if row 32's accelerator transports to a monomial Jacobian, its saturations get cheaper. |
| Queued: tree-decorated moment engine | **CONTINUE at reduced priority** | Three lanes have now shown the analytic decoration is not skeleton-determined; the tree supplies the combinatorial half only. Worth doing, but it is not the frontier. |
| Queued: P202 residue (52 rows) | **REDESIGN** (§2) | Archaeology as posed; run the 52 rows through descent + anchor instead. |
| Queued: box01 restart | **CONTINUE; escalate the human gate** | It now has a named client (42-unknown descended systems, > desk cap). Worth asking DC for the fleet key on this basis. |

---

## 12. The single first lane

**`descent-anchor-audit`** (Card 1), 4-hour cap, source + desk arithmetic,
any seat (this is reading and rationals, not a flagship).

*Why this and not the obvious alternatives.* The obvious first lane is a
flagship on (T) or on the screened cofinal family. Both are more exciting and
both are, right now, **pointed at rows where the machinery they depend on is
undefined**. Card 1 costs four hours, is the only item that can invalidate a
promotion made today, and determines the domain of theorem (T) — which is the
input to every downstream choice. It is also the highest-leverage kind of work
this campaign does: a bounded source question with a measured, falsifiable
prediction attached (Moh's p.207 table contains no anchor-degenerate row).

*If a second seat is free:* Card 2 (`rigid-stratum-intersect`), because it is
an afternoon and it is the campaign's cheapest counterexample shot.

---

## 13. OPEN ledger raised here

Each with its bounded quantity and cheapest test, per contract.

**`OPEN[DESCENT-ANCHOR]`** — Is the descent (Prop 6.3/6.4) and the promoted
δ' = (k+1)·Def 5.1(3) rule defined when M_{s−1} = n − d_s (⟺ the Def 5.1(3)
anchor n' − M_{s'}' − 1 = 0)?
*Bounded quantity:* 38 of the 57 descendable C_FULL_TREE_ODE survivors at
n ≤ 100; 12 of the 20 at n = 108; 3 of Moh's printed six (the (84,56),
d_s = 7 rows, descending to (12,8) with M_3' = 11 = n' − 1); and the count of
p.207 printed rows with the property (predicted 0).
*Cheapest test:* read Moh p.207–208 and p.179 as images (pdftoppm, ~20 min)
and check (a) whether any printed descended row is anchor-degenerate,
(b) whether 1/(n − M_s − 1) is in Def 5.1(3) at the source. Measured here:
dropping the factor breaks the match (δ₂' = −3 instead of −1/3 on (15,10)),
so it is required by the printed data.

**`OPEN[DESCENDED-TREE-LICENSE]`** — Do Prop 5.3's threshold argument, the
p.200 Theorem (4) and Prop 5.6 hold for a pair with J = cγ^k rather than
J = const?
*Bounded quantity:* three propositions; the ODE (3.7) is already known to
degenerate on γ = 0 (X2), so at most two remain.
*Cheapest test:* re-read pp.190–195 and p.200 asking only "where is J used,
and is J = const or J ≠ 0 needed?" — 45 min. Only matters if someone wants a
*kill* from the composite screen; the negative result of §4 is robust without
it.

**`OPEN[SAT-MONOMIAL]`** — Does row 32's accelerator (I : Δ = I : Δ^∞ =
I + (det A)) transport when det A = cγ^k instead of a unit?
*Bounded quantity:* one lemma; two controls (the m2-descent (15,10) Case 2
saturation, which must give the same SATURATED-EMPTY verdict, and a negative
control that must not).
*Cheapest test:* one page of algebra plus the two reruns in
`box/m2descent-drivers-20260903/moh_1510_control*.py` — under an hour.

**`OPEN[T-LADDER]`** — Is the number of non-constant H-adic coefficients of a
monomial-Jacobian pair (total degree = π-degree) absolutely bounded, with
γ-degrees ≤ k + 1?
*Bounded quantity:* the count and the γ-degrees on Moh's (15,10; k = 2) and
(16,12; k = 1) shapes; must reproduce Moh's "22 [15 or 13]".
*Cheapest test:* Card 3's discriminator, < 10 min of sympy on shapes already
coded in `box/descentradii-drivers-20260903/g2_fullh_mohbeta.py`.

**`OPEN[SCREEN-CONGRUENCE-RAY]`** — Along a linear family (n(t), m(t), M_i(t),
V_i(t)) satisfying (1)–(13), is the residue b_j(t) = P_j(t) mod A_j(t)
eventually constant and nonzero, or can it be driven to 0 on a progression?
*Bounded quantity:* (A_j, P_j mod A_j) at the selected path for the 20 n = 108
and the D = 112/120 screened survivors, as V_2 varies.
*Cheapest test:* `TreePartition.level_data` already returns the tuple; a
5-minute scan. This is Q1's true all-degree question, in congruence form.

---

## Method note / reproduction

All MEASURED numbers in this submission come from
`box/mohprog-drivers-20260903/full_tree_partition.py` +
`repro/moh_skeleton_full.py` run under `python3 -O`, plus a ~40-line descent
map written in this lane (n' = n/d_s, m' = m/d_s, M_i' = M_i/d_s,
d_i' = d_i/d_s, V_i' = V_i, s' = s − 1, k = V_s − u_s − 1, u_s = d_s − V_s)
and the radii rule δ' = (k+1)·Def 5.1(3)(descended data). Controls passed
before any number was printed: the screen reproduces 658 → 60 → 58 at
n ≤ 100 and 217 → 21 → 20 at n = 108 (delta 17(r)); the descent map reproduces
p.207's (64,48) → (16,12,13; X), (75,50) → (15,10,11; X²),
(84,56) → (21,14,16/18; X); the radii rule reproduces
descent-radii's independently measured (−1, 1/2) on (15,10) and (−1, 1/4) on
(16,12). Total wall time under three minutes; no run exceeded 4 GB.

Nothing in this submission re-types a promoted claim. H1 is a **coverage**
finding against delta 17(t), not a refutation of it: the rule's 10/10 match on
the printed rationals is confirmed here by a second, independent derivation.

Blind-lane compliance: charged input hash verified before reading; no
`ideation-20260903T1200Z-*` submission opened; `final_status` checked in
`.run.v2` for every named running lane before any `.md` was opened (only
`descent-radii-grok46` and `a2six-ray-moment-sol56` were DONE, and neither was
needed for the results above — the p.207/p.208 δ' values quoted for
cross-validation are the ones recorded in AUDIT delta 17(t)); no canonical
ledger edited; `jc2-lean` not inspected.

<!-- BODY-END -->
