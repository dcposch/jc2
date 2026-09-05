# Ideation round 20260905T0000Z — coordinator synthesis (five blind submissions sealed; first round with Astra on the roster, though these five predate the Astra directive)

Submissions: fable5 (61KB), grok46 (48KB), sol56 (46KB), opus5 (43KB), gpt55 (27KB); coordinator blind submission committed pre-read.

## 1. TWO board-changing findings (independent, both need a gate)

**(A) N1 is closable by CITATION, not by five joint-chart kills (Fable Q2).** Replaying the charged whole-tree screen driver (box/centre-gate-20260903/rerun_screens.py, imports unmodified) on the eight (1)–(13)-admissible (99,66) skeletons: SEVEN of eight DIE under the PROMOTED operative screen — S1, S4, S5, S6 at the gap-free partition level (Moh Theorem p.200 (4)–(7)); S2, S3, S7 under ungated Prop 5.6 (17(hh) LEMMA[ZERO-FACTOR-CENTRE]); only S8 = V(8,8) survives (killed by the joint chart, 17(bbbbbb)). So N1 closes by citing promoted deltas (17(r) whole-major-tree necessity, 17(hh), 17(ll) operative screen) + the S8 joint chart; the running batch-3 lane is a REDUNDANT exact cross-check, not the critical path. Moh's "private program" = the p.200 Theorem (4)–(7) + Props 5.5/5.6, recovered as 17(ll). ⇒ if gated, DEGREE-WIDE (99,66) NO-KELLER-PAIR is PROVABLE by citation. CAVEAT (Fable, important): this does NOT resolve "Moh's ≤100 theorem" — the operative screen leaves 14 EXCESS rows at n ≤ 100 ((90,60)×4, (96,64)×4, (96,72)×6, all s ≥ 4, u_s = 1; OPEN[MOH-PROGRAM-ARTIFACT] 17(ll)) whose u_s = 1 descents must also be killed.

**(B) The eight skeletons descend onto ONE LINE; the (H2) census compresses ~4.6× (Opus).** PROVED-HERE §2.1 (regenerated from the frozen enumerator, matches the batch-2 table row for row): u_s = d_s − V_s, (n′,m′) = ((n/d_s)u_s, (m/d_s)u_s), ℓ = d_s − 1 − 2u_s; every (1)–(13)-admissible (99,66) skeleton descends onto 2K′ + 3ℓ = 30 — only FOUR distinct descended data, two already dead; the five "open" skeletons are only THREE descended charts (S2,S3,S7 coincide). The k=4 ray is just the slice ℓ=4 of the (K,ℓ) LATTICE — demote it from "the unifying object" to a slice; D=108 is the lattice point (K,ℓ)=(8,4). Over 16 ≤ n ≤ 200 the u_s≥2 census compresses 6209 → 1359 distinct (n′,m′,ℓ,V₂′) (4.57×), or → 586 with V₂′ a parameter (10.6×). ⇒ the efficient (H1)/(H2) route is a DESCENDED-CLASS sweep on the (K,ℓ) lattice, not per-row.

## 2. A CORRECTNESS FLAG (Opus, highest priority) — Prop 6.3's radius hypothesis
Opus: Prop 6.3's radius hypothesis (δ* ≥ v_s/u_s licensing the descent) is AUTOMATIC only when u_s = 1; EVERY u_s ≥ 2 kill the campaign owns — INCLUDING D=108 (K=8, the no-split arm) and the k=4-ray no-split rows — is "sitting on it" undischarged. If the hypothesis is not discharged for those, the descents (hence the kills that depend on them) are conditional. This must be checked before D=108 CLOSED and the k=4-ray/no-split kills are treated as unconditional. (Note: the SPLIT-branch kills — (99,66) B/C via the joint chart, D=108 δ=3 — do NOT use Prop 6.3, so they stand; the flag is specifically the DESCENT-based no-split kills.)

## 3. K16 (Q1) — consensus: retarget to (8.1), decide t=11, the resultant is ill-posed
- (V0) is one atom too strong (Fable, Sol, Opus, GPT-5.5); the JC2-relevant all-t target is (8.1) = τ_t ∈ √I_{t,+} (the b₃-axis is z-type, in V(τ_t); a positive-dim cone is allowed). Four lanes over-invested in (V0).
- Opus: A_t = Q(√(3(t+1))); the "wrong root" hazard is only at the 8 split indices t = 3m²−1 < 200; the one failure (t=2, y=1/5) is exactly a₀ = 0; the LIVE question is "do the weights + a₀ ≠ 0 already force dim 0?"; the resultant target four lanes chased is ILL-POSED (not scale-invariant).
- Fable: FALSIFICATION target — t=11 has rational fibres (t+1 = 3·2²) exactly like t=2, and its b₄=1 chart timed out in both t11 lanes; decide the d=−k fibre at t=11 BEFORE another structural lane. Reformulation: (V0)_t = the G_r are an hsop of the DOUBLE COVER R_t = P_t[X]/(a₀X²+b₀X+c₀), W_r = a₀·N(G_r) norms, X_rs mixed traces; a p-adic valuative Gröbner degeneration at p=4t+1 (immune to the refuted routes) is a new mechanism, one instance dead, typed OPEN.
- Astra (gpt-6-astra) is already on this (k16-8point1-astra, launched per the DC directive): targeting (8.1)/nonzerodivisor with valuation/specialization/intersection angles — the right seat for the hardest OPEN. Add t=11 falsification + the a₀≠0 question to its scope via a fast companion.

## 4. Dispositions and launches
1. N1 by citation: GATE Fable's screen-replay claim (different model) — if 7/8 die under the promoted screen, DEGREE-WIDE (99,66) closes by citation. LAUNCHED n1-screen-gate-grok46. Batch-3 (Opus, running) becomes the exact cross-check — keep it.
2. Prop 6.3 radius hypothesis: VERIFY for the u_s≥2 descent kills (D=108, k=4-ray no-split). LAUNCHED prop63-radius-gate-opus5 (correctness).
3. (H1)/(H2) census: build the (K,ℓ)-lattice descended chart + descended-class sweep (Opus's §3) — QUEUED (after the radius gate, since the sweep's kills inherit the same hypothesis).
4. K16: Astra on the atom (running); add t=11 falsification.
5. Moh ≤100: the 14 excess u_s=1 rows (OPEN[MOH-PROGRAM-ARTIFACT]) are the residual for the published theorem beyond (99,66) — QUEUED (u_s=1 descents, radius-automatic, so unaffected by the flag).
STOP: further (V0)-as-flagship K16 lanes; the five-joint-chart N1 plan (superseded by the screen citation + the descended chart).

## 5. OPENs raised: OPEN[K16-8.1-RADICAL] (τ_t ∈ √I, the JC2 target), OPEN[K16-T11-FIBRE] (falsification), OPEN[PROP63-RADIUS-USABILITY] (u_s≥2 descent hypothesis — correctness), OPEN[N1-SCREEN-CITATION] (7/8 die, gate pending), OPEN[KL-LATTICE-SWEEP] (descended-class census), OPEN[MOH-PROGRAM-ARTIFACT] (14 excess u_s=1 rows for ≤100), OPEN[ROUTING-MAPS] (the reduction interface, unproved).

<!-- BODY-END -->
