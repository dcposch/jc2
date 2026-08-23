# SHEET6-R6-REVIEW.md — Adversarial review of the R6 closure (456c634)

Reviewer: Claude (adversarial pass, 2026-08-09). Status: COMPLETE.
Scope: SHEET6-R6.md + cases/r6_window.py layer2() — the claim "all 8
deeper-tower window cases DEAD; R6 CLOSED; R1 decisive for the whole
residue-A configuration". Ground truth: refs/sigray_full.pdf re-read
on-page this review (pp. 15-21, 31-39, 40-44). Engines re-run:
r6_window.py (layer 1 + 2, output matches doc verbatim),
sheet6_campaign.py gate (PASS). Independent verifier written for this
review (/tmp/r6_review_check.py, own Fraction code, all checks pass).

Verdicts:
- Front 1 (L2 exactness of vertex transport): **CONFIRMED, citation
  corrected** — the equality IS printed (St 3.17(i) p. 18; verbatim
  "mult(p_G,c) = deg(p_F)" in St 8.3's proof p. 41); and the six-case
  kill does not even need it (second, vertex-local route).
- Front 2 (L4 dead-member mult law): **CONFIRMED on-page, twice**
  (Prop 8.1 proof p. 40 via Prop 6.3; Cor 6.1 proof p. 32 via Prop 6.7);
  both level-0 cross-checks exact.
- Front 3 (μ₂ = 3/2 + (k1−1)r): **CONFIRMED** (Prop 4.2(iv)+(9) p. 19,
  α_0 = 0; all 8 values recomputed).
- Front 4 ((2,3)/(2,5) h2 pole-edge kill): **REFUTED** — d_h1@P = 1/7,
  not 1/21; the h1-side (not the f-side) wins h2's top at P on the
  ENTIRE window; deg p_h2@P = 2k1, and (D) then PASSES (4 ≤ 5, 4 ≤ 7).
  (2,3) and (2,5) are NOT killed by the banked argument.
- Front 5 (escapes): premerge **CONFIRMED closed**; M-menu **CONFIRMED
  no freedom** (doubly); the (2,3) echo "dies at (D)" **REFUTED** — the
  echo is real, forced (r2 = μ₂ − 1/6 exact), and OPEN. NEW finding:
  the banked window MISSES (k1,l1) = (1,2) at 6r = 12.
- Front 6 (engines/arithmetic): **CONFIRMED faithful** — every printed
  number reproduces; the error is in one formula's premise (front 4),
  not in the code paths or the gate.

**NET: R6 is NOT CLOSED.** Corrected status: 6/8 DEAD (the merge-vertex
kill, now doubly grounded), (2,3) and (2,5) OPEN (self-similar
recursion forced, next rung not run), plus the un-enumerated (1,2)
branch OPEN. "m_{G_m} = 1 forced" is not established; **R1's "decisive
for the whole configuration" label does NOT survive** — R1 reverts to
per-branch labeling (LT-REVIEW 7c) unless the three residual branches
are closed on paper first.

## 1. Front 1 — the transport laws, pinned on-page

The engine's law ledger (layer2() docstring) checks out against print,
with one citation repair and one scoping note.

- St 3.9 (p. 15) is the ELEMENTARY-step law: for ANY polynomial h and
  one grid step F → F∗c, (i) mult(p_{h,F},c) = deg(p_{h,F∗c}) EXACT,
  (ii) lead = Taylor coefficient, (iii) d drops by mult/κ. Along
  COMPOSITE edges the per-step equality degrades, for general h, to the
  monotone count law St 3.11(i) (p. 16): mult(p_{h,F′},c) ≥
  deg(p_{h,F}) — printed with the ≥ in exactly the direction the kills
  need (engine L3 ✓).
- For the VERTEX pattern p_F := p_{f,F} (Not 3.13) the equality
  survives composition: St 3.17(i) (p. 18): F = G + c ∈ V_a ⟹
  deg(p_F) = mult(p_G, c). The identical sentence opens St 8.3's proof
  (p. 41): "From Statements 3.9 and 3.16 one has mult(p_G,c) =
  deg(p_F)" — so the engine's cite "L2 (p.41, St 3.9+3.16)" is the
  thesis's own derivation line; the clean citation is St 3.17(i),
  p. 18. CITATION EDIT, not an error.
- St 8.3(ii) (p. 41): member equality deg(p_{h_j,F}) = mult(p_{h_j,G},c)
  for 0 ≤ j ≤ m_F, m_F the DEEPER vertex's depth, INCLUDING the dead
  member j = m_F. Scoping check (both used correctly by the engine):
  on the suffix edge j ≤ m_{G_m} = 2, so the h2-equality is available;
  on the merge edges m_{P_i} = 0, so only h_0 = g gets equality there —
  h1, h2 at pole edges get only St 3.11(i). ✓
- Load-bearing consequence probed: had the vertex law been ≤ only, the
  six-case transport kill would FAIL (2 ≤ 6μ_i is satisfiable). It is
  an equality, so the kill stands — AND it stands anyway without any
  transport: see front 5(i) (the >1-root route is vertex-local at G_m).
  The six-case verdict is doubly safe.

## 2. Front 2 — the L4 dead-member law, on-page

**CONFIRMED.** Printed twice, in the exact form banked:

- Prop 8.1's proof, p. 40: "from Proposition 6.3, we obtain that for
  any root of p_F c, one has mult(p_{h_F},c) − (μ−1)mult(p_F) = 1" —
  i.e. mult(p_{h_m,F},c) = (μ_F−1)mult(p_F,c) + 1 for ANY root c of
  p_F. Also on p. 40: the dead-member level formula d_{h,F} =
  (μ_F−1)d_F + 1 − u (first substitution of the "constant l" line) —
  used below in front 4/5 arithmetic.
- Cor 6.1's proof, p. 32 (via Prop 6.7): "for any root of p, say c one
  has mult(q,c) = (μ−1)mult(p)+1" (q := p_{h,F}), driving the printed
  "k = 1, so F ∉ V_a" root-count contradiction — the same mechanism the
  R6 kills re-use.
- Cross-checks recomputed: G_m level-0: (3/2−1)·2+1 = 2 = mult(pq,c_i)
  (1+1, E5) ✓; F_s: (25/6−1)·12+1 = 39 = 19·2+1 (E4/E7 banked pattern
  p^19·q with mult(q,c_m) = 1) ✓. Engine assert line correct. The
  equivalence L4 ⟺ Prop 8.1(ii) + mult(q,c) = 1 checked:
  k·mult(p_red,c) + 1 = i(μ−1)mult(p_red,c) + 1 = (μ−1)mult(p_F,c)+1 ✓.

## 3. Front 3 — μ₂, re-derived from Prop 4.2

**CONFIRMED.** Prop 4.2 (p. 19), eq. (9): α_j = Σ_{j′<j}(k_{j′}−1)
l_{j′}/k_{j′}, α_0 = 0, μ_F = α_{m_F} (item (iv)). With the level-0
tower start (k0,l0) = (2,3) (banked, d_g = (3/2)d): μ₂ = 3/2 +
(k1−1)l1/k1. All 8 values recomputed independently: 3, 4, 29/6, 37/6,
41/6, 32/3, 37/3, 47/3 — match the engine, hence 2μ₂−1 ∈ {5, 7, 26/3,
34/3, 38/3, 61/3, 71/3, 91/3} ✓. Bonus on-page harvest (p. 20, proof):
d_{h_{j+1},F} < k_j d_{h_j,F} = l_j d_F STRICT — the printed hierarchy
that gives the window's upper bound r < 3 and the r2 < l1 bound used in
front 5. Also δ_j ∈ N printed (window integrality 6r ∈ N).

## 4. Front 4 — the (2,3)/(2,5) kill: **REFUTED**

The kill rests on "the m=2 transport pins d_h1@P = 1/21". That value is
wrong; the correct value is d_h1@P = 1/7, and the kill inverts.

- Vertex-local recomputation at P (variant-independent): h1 = g²−s0f³;
  tops sit at 2d_g@P = 3d@P = 6/42 = 1/7. With m_i² = s0λ_i³ (forced by
  the count AND automatic via the transported tower relation — same as
  level-0 E5; the transport factors are exponent-trivial for p_f = P^i,
  p_g = P^{3i/2}), the z-identity z(z−(3/2)w²)² − (z−w²)³ = −(3/4)w⁴z +
  w⁶ leaves a NONZERO deg-2 pattern. A nonzero pattern means NO level
  drop: d_{h1,P} = 1/7 with p_{h1,P} = −(3/4)s0λ³w⁴(η²−(4/3)w²). The
  engine's "d_h1@P = 3/21 − 4/42 = 1/21" treats the in-vertex DEGREE
  drop 6 → 2 as four elementary transport steps — a misapplication of
  St 3.9(iii) (d drops only via mult along steps, not via cancellation
  inside one level).
- The promoted record already says so: TEMPLATE §1a table lists
  d_h1@P_i = 1/7; TEMPLATE E6 computes h2's pole top from "levels
  18/42 > 8/42" — h1-side dominant — giving p_{h2,P} = (p_{h1,P})³,
  deg 6 = 2k1 (NOT 2l1 = 8). The level-0 genome itself refutes the
  doc's f-side formula.
- Consequence for the window: h2 = h1^{k1} − s1f^{l1} at P compares
  k1·(3/21) vs l1·(1/21); the f-side wins iff l1 > 3k1 ⟺ r > 3 — never
  in the window (r < 3 printed, front 3). So on the ENTIRE window the
  h1-side wins: p_{h2,P} = (p_{h1,P})^{k1}, deg 2k1, pure power, no
  cancellation (strict level gap). TEMPLATE §3 R6's original l1 > 3k1
  kill threshold was correct; the doc's "upgrade to all l1 > k1" is
  precisely the bug.
- Corrected (D): 2k1 ≤ mult(p_{h2,G_m},c_i) = 2μ₂−1 = 2 + 2(k1−1)r ⟺
  k1 ≤ l1 — TRUE on the whole window, slack 2(k1−1)(r−1) > 0:
  (2,3): 4 ≤ 5; (2,5): 4 ≤ 7. NOT DEAD. Consistency confirmed by the
  d-ladder: (2,3): d_h2@Gm = (μ₂−1)d+1−π = 17/21 (deg 34 = 4·6+10),
  five merge steps with counts (5,5,4,4,4) → d_h2@P = 17/21 − 22/42 =
  2/7 = k1·(1/7) ✓ exact closure with a 1-branch leak (allowed for
  non-members at pole edges: St 3.11(i) only; the analogous h1 leak is
  3 → 2).
- What actually remains for (2,3)/(2,5): every printed-tier test passes
  — (A) with i = 2, μ_i = 1 forced (orbit fit AND St 8.4: mult(p_red,c_i)
  | M_P = 1), (B) identity, (C) 2 ≤ 2r, corrected (D). The suffix
  h2-equality (St 8.3(ii), j = 2 = m_{G_m}, legitimately applicable) is
  NOT moot and FORCES the echo: 12r2 = deg p_h2@Gm = 34 resp. 46, i.e.
  r2 = 17/6 resp. 23/6 = μ₂ − 1/6 exactly, (k2,l2) = (6,17), (6,23).
  (Stronger than the engine's "minimal q-shape" hedge: deg q = 10 is
  forced by the d-arithmetic alone.) The recursion is real: the next
  rung is the level-3 dead-member count at F_s — deg p_h3@Gm ≤
  (α_3−1)·12+1 (e.g. (2,3): generic 204 vs 195) — forcing a 3-coefficient
  W₂-collapse in 2 unknowns (s2, b): overdetermined by one, level-0-E4
  sized, NOT run anywhere. That computation (or an equivalent) is the
  actual remaining closure work.

## 5. Front 5 — escapes

### 5(i) Premerge depth 1: **CONFIRMED closed** (both shapes)

- Six cases: the obstruction is G_m-vertex-local and needs no transport:
  M*_Gm = 2 ⟹ p_red = L·η² (St 3.16's frame p_F = η^l·p̃(η^ν), ν_Gm = 3,
  p. 17: deg 2 forces the pure monomial), a SINGLE root — but G_m ∈
  V_{2,a} (the configuration's merge/separation vertex) and St 3.16's
  printed iff (p. 17) demands > 1 root; equivalently St 8.2's proof
  (p. 41) asserts "p has more than one root" verbatim at non-pole chain
  V_a vertices. Two pole subtrees need two distinct root directions at
  G_m whether or not intermediates exist. Robust. (The transport form
  and the L4 non-integrality {26/3,...,91/3} stand as corroborations.)
  Nit: the doc's third form cites St 7.2 for the axis exclusion;
  St 7.2 (p. 35) says cv-rays avoid poles — the actual closure is that
  a single root cannot carry two subtrees + the configuration pins the
  merge at G_m. Decorative miscite, no weight.
- (2,3)/(2,5): the doc's intermediate-Q argument is printed-tier VALID:
  deg p_f@Q = mult(p_f@Gm,c_i) = 2 (St 3.17(i)); m_Q = 1 (Cor 6.1
  p. 32 strict m-growth: 0 < m_Q < 2); family {f,g} ⟹ M*_Q = gcd(2,3)
  = 1 (Not 8.1) ⟹ p_red,Q deg 1, single root ⟹ Q ∉ V_a (St 3.16 iff) —
  no vertex can exist there. CONFIRMED — though it now guards OPEN
  cases rather than completing kills. (Any count-kill is in any case
  premerge-robust: St 3.11(i) composes monotonically through
  intermediates.)
- SCOPE PATCH the doc needs (m_{G_m} ≥ 3 is never dispatched, and
  "eliminated entirely" requires it): (a) six shapes — the family only
  grows, M* = gcd(2, …) stays ≤ 2: same kill at any depth. (b) (2,3):
  δ₂(G_m) = 6r2 − 17 > 0 with r2 < 3 and 6r2 ∈ N is EMPTY. (c) (2,5):
  r2 ∈ {14/3, 29/6} ⟹ 12r2 ∈ {56, 58} ⟹ M*_Gm = gcd(6,12r2) = 2 ⟹
  the six-case kill applies. One paragraph, all printed-tier; should be
  added when R6 is re-banked.

### 5(ii) M-menu freedom at G_m: **CONFIRMED — none** (doubly)

- Not 8.1 (p. 39): M*_F := gcd(deg p_F, deg p_{h_0}, …, deg p_{h_{m−1}})
  — the alive family is definitional, h1 is in it once m_{G_m} = 2, and
  Prop 8.1 (pp. 39-40) sets i := deg(p_F)/M*_F with deg p_red = M*_F
  EXACT ("As we noticed, deg(p) = M*_F"). No menu exists: i_Gm = 6 is
  forced for k1 ∈ {3,6} (12r ≢ 0 mod 3 and 4 rechecked for all six).
- Independent closure even without the gcd law: polynomiality of the
  alive powers (Prop 8.1 proof: i·l_j/k_j ∈ N) forces 2 | i and k1 | i,
  so i ∈ {6, 12} for k1 ∈ {3,6} — and i = 12 gives deg p_red = 1,
  killed by the same single-root argument. i ∈ {2,3} is impossible
  (p_g = p_red^{3i/2} or p_h1 = p_red^{ir} non-polynomial). Closed.

### 5(iii) The (2,3) self-similar echo: **REFUTED as handled**

The engine's closing line "no isomorphic-genome survivor (the (2,3)
self-similar echo dies at (D))" fails with (D): the echo is forced
(front 4) and OPEN. (2,5)'s echo (k2,l2) = (6,23) likewise. Note the
echo exponents are window-shaped ((6,17) is literally a level-1 window
member), so the recursion is genuinely self-similar and needs its own
terminating argument (the W₂-collapse rung, front 4), not a label.

### 5(iv) NEW — window completeness: (1,2) is missing

The banked window (TEMPLATE §3 R6, LT-REVIEW 7c, R6 §0 — all three
quote the same 8) omits (k1,l1) = (1,2) at 6r = 12, which passes every
stated test: 4/3 < 2 < 3, 6r ∈ N, gcd(1,2) = 1, and k_j = 1 ∈ N* is
allowed by Prop 4.2 (p. 19; a (1,l)-step is legal when h1⁺ is exactly a
constant times (f⁺)^l, contributes 0 to μ). Independent re-enumeration
from the printed constraints (δ₁(G_m) = 6r − 8 ∈ N, > 0; hierarchy
r < 3; grid 6r ∈ N) yields NINE candidates, the banked eight plus
(1,2). Layer-2 behavior: (A) passes (i = 2), corrected (D) passes AT
EQUALITY (2 ≤ 2), and the suffix h2-equality forces r2 = 4/3, i.e.
(k2,l2) = (3,4): the tower (2,3),(1,2),(3,4),… — the MINIMAL genome
with a re-indexed tower (dead-member data at G_m is byte-identical:
p·q, deg 16, d = 8/21; same L1c layer downstream). It is nonetheless a
DISJOINT branch of the configuration: it pins d_h1@Gm = 12/21 with
quotient ∝ P⁴ (vs minimal 8/21 with quotient pq) — mutually exclusive
values of the same quantity, hence a different constraint set on (f,g)
that R1's staged depths as specced (G_m: 18/21 → 8/21, quotient p·q) do
NOT cover. Disposition required: either a k1 = 1 exclusion argument
(none is on record; none found in print by this review) or add the
branch to R1's enumeration (cheap: one extra staged resonance level).

## 6. Front 6 — engines and independent arithmetic

- cases/r6_window.py: runs clean; layer-1 (all 8 ladder-integral,
  M*_Fs/i_Fs as printed) and layer-2 output match SHEET6-R6.md line for
  line. sheet6_campaign.py gate: PASS (Prop 9.1 11/11, St 9.6 pairs +
  erratum reproduced).
- All eight verdict arithmetics recomputed independently
  (/tmp/r6_review_check.py): M*_Gm = gcd(6,12r) ∈ {6,6,2,2,2,2,2,2},
  i_Gm ∈ {2,2,6,…}, 6μ_i ≥ 6 ≠ 2, 2μ₂−1 non-integers for the six, L4
  cross-checks — every number the engine prints is faithfully computed
  FROM ITS FORMULAS. The refutation (front 4) is a wrong premise
  (d_h1@P), not an implementation bug.
- Engine nits, no verdict weight: (a) layer2() (C)'s "w_i^4 pinned as
  level-0 E5" glosses the forced 3 → 2 leak — the lead transport now
  passes through a free dead-stretch coefficient, so w_i⁴ is solvable-
  for rather than cleanly pinned (still no obstruction); (b) the (A)
  orbit-fit check tests 3μ_i ≤ M* for one pole; the two-pole fit needs
  3μ₁+3μ₂ ≤ M* (6 ≤ 6 exact for i = 2 — happens to be unaffected);
  (c) the layer-1 "M*_Fs = 63, i_Fs = 2 smell" for (2,3)/(2,5) is
  superseded at layer 2 by the h2-in-family gcd (e.g. gcd(63, 126·17/6)
  = 21, i_Fs = 6) — worth a note when re-banking.

## 7. Overall verdict

**SHEET6-R6 (456c634): REFUTED AS A CLOSURE; PARTIALLY CONFIRMED AS A
KILL.** What survives adversarial review, strengthened: the six
k1 ∈ {3,6} cases are DEAD by two independent printed-tier routes
(vertex-local single-root contradiction at G_m — St 3.16 + Not/Prop 8.1;
and the St 3.17(i) transport 6μ_i ≠ 2), robust to premerge depth,
M-choices, and m_{G_m} ≥ 3. What does not survive: the (2,3)/(2,5) kill
(front 4 — d_h1@P error inverts the h2 pole-top; (D) passes with slack),
hence the headline "ALL 8 DEAD", "m_{G_m} = 1 FORCED", and "no
isomorphic-genome survivor" are all WITHDRAWN pending: (a) the level-3
W₂-collapse computation for (2,3) and (2,5) (their echoes (6,17)/(6,23)
are forced, self-similar, and open); (b) disposition of the missed
(1,2) window member (minimal genome re-indexed; disjoint branch).

**R1's "decisive" label: does NOT survive.** Per LT-REVIEW 7c's own
gate, R1-UNSOLVABLE kills the whole residue-A configuration only if R6
is closed. It is not. Until (2,3), (2,5), (1,2) are dispatched, R1
must be run and labeled per-branch (minimal genome), and its branch
enumeration should be extended to (1,2) (one extra staged level) —
which would make R1 decisive for {minimal, (1,2)} while (2,3)/(2,5)
remain a paper obligation. The cheapest path back to "R1 decisive for
everything": run the W₂-collapse rung for (2,3)/(2,5) (finite,
E4-sized, 3 conditions / 2 unknowns) and write the one-paragraph
m_{G_m} ≥ 3 patch (§5(i)) plus a k1 = 1 disposition.

Required edits to SHEET6-R6.md before any re-bank: fix d_h1@P = 1/7 and
the h2 pole-top to (p_h1@P)^{k1} deg 2k1 (§1.1, §1.2, §1.3-1.8 backup
sentence, layer-2 note); re-verdict (2,3)/(2,5) as OPEN-AT-LAYER-2 with
the forced echoes; add (1,2) to §0's window table or exclude it with an
argument; correct the L2 citation to St 3.17(i) (p. 18); drop or
re-scope the St 7.2 cite; add the m ≥ 3 paragraph. Status header must
revert from CLOSED until the recursion rung runs.

Canonical book: unchanged (8 = 4 single-pole + 4 two-pole residue-A);
within the two-pole configuration the live structure set is now
{minimal (3,4) genome, (1,2) re-indexed variant, (2,3) tower, (2,5)
tower} — smaller than pre-R6 (six window cases genuinely dead) but not
the singleton the closure claimed.

Artifacts: no engine or doc changes made (review-only); independent
verifier /tmp/r6_review_check.py (window re-enumeration, corrected (D)
table, forced-echo derivation, m ≥ 3 patch arithmetic — ALL PASS);
engines re-run bit-identical.
