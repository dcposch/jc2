# Blind ideation submission — round 20260904T0000Z — Fable 5

Lane `ideation-20260904T0000Z-fable5`, basis `ce00e907`, written 2026-09-04 08:25Z–~10:50Z.
Packet `ideation-20260904T0000Z-packet.md` (sha256 `ba345ef1…`, incl. the 08:30Z addendum §4).
Custody: the receipt's paired `charged_input_<i>_sha256=` / `_basename=` lines were turned into a
manifest by `awk` and piped to `sha256sum -c`: **4/4 OK**, no digit retyped. Read before writing:
the packet, the 1200Z synthesis, FALLACY-v2, COORDINATION (full-spectrum contract), AUDIT deltas
17(tttt)–(ccccc), the newest LIVE STATE (08:22Z), APPROACHES (overlay + rows 1–46), the PROGRESS
digest, and the sealed reports g9966-delta52-kill-gate-gpt55, g9966-independent-engine-opus5,
g108-minor-classification-opus5, g108-joint-band-sol56, g108-outer-bridge-grok46,
k16-toptail-quadratics-fable5, k16-hilbert-regseq-sol56, k16-chain-gate-grok46,
order-chart-general-gpt55, plus Moh p.209 (image). No ideation-20260904T0000Z-* file, no ledger
edit, no jc2-lean, no in-progress report (the four RUNNING receipts were checked for
`final_status` and their `.md` files were not opened). Desk CAS: two Singular/Python tests under
`box/ideation-0904-fable5/` (seconds each, one core). No exit-price assertion is made, so no
`charge_basis` line is due.

## 0. Headline — direct answers

```text
ALL-DEGREE PROGRAM (one sentence).  Every Moh skeleton is reduced — by Prop 6.3/6.4 descent
  (u_s = 1), by the INNER joint chart (u_s > 1 with a genuine principal-minor split), or by
  conditional descent (u_s > 1 without a split) — to a MONOMIAL-JACOBIAN RECEIVER datum
  (P, Q) in K[γ,π]², J(P,Q) = c·γ^k, with a prescribed two-point order datum; the theorem that
  finishes Moh's line is RECEIVER-EMPTINESS for every descended datum, and (99,66), D = 108,
  (25,15) and the K = 16 ray are its instances (Moh p.209 already writes branch A as (27,18; X⁴)
  and branch B as an Ω-transformed pair with J = x; the K16 ray is (12t+4, 8t+4; k = 1);
  (25,15; 21; 2) has k = 2; the D = 108 no-split alternative is (24,16; k = 4)).
THE COORDINATOR'S Q4 TRICHOTOMY IS FALSE.  "family / census / structural theorem" are one
  object with three price tags: the census is the theorem's instance list, the K16 ray is the
  census's only infinite piece under the operative screen, and the "structural statement about
  two points at infinity" is the receiver statement.  Price: §5.
REVISED Q1 (closed form of Res_w(R_1..R_{t−1}) in t): NO — typed IMPOSSIBLE-AS-FORMULA (§1.1):
  the system's variable count is t−1, its Macaulay matrix grows like a partition count, and
  only the truncated-spine coefficients a_r (fixed r) are rational functions of (t,d).
  Two structural routes are CLOSED here by desk tests (MEASURED, exact, t = 3..6):
    E1  the cone rows admit NO second grading (nullity 1 at every t) — the two-torus
        rigidity argument does not exist for I_{t,+} as it stands;
    E2  no degeneration weight ω ∈ {−1,0,1}^t makes ⟨in_ω(rows)⟩ zero-dimensional at
        t = 3, 4 (best dim 1, only for ω = −e_i) — the Gröbner-degeneration-of-generators
        route is dead on the structured set.
  The route that is open is a CHANGE OF TARGET: the cone V(I_{t,+}) is (conjecturally, §1.2)
  the locus of ansatz pairs with J ∈ K·γ, so (V0) = (T) ∧ (no algebraically dependent
  ansatz pair besides the bare tower); the second conjunct FAILS at t = 2, y = 1/5 (the
  b₃-axis) and nothing proved excludes its failure at some t ≥ 8.  The uniform target must
  be (8.1) τ_t ∈ √I_{t,+}, with dim I_{t,+} = 0 an instrument that may legitimately fail.
Q2 (re-posed): the two kills are INNER kills — every row that reaches a certificate lives at
  t-power ≤ 8, below the outer onset (A₂/A₃/B₂ enter at r ≥ 21); the 5,774 outer pivots are
  dimension bookkeeping, not kill content.  Hence the minimal necessity dossier is a
  CERTIFICATE SLICE (Card A) of a few hundred rows, not the 7,161-coordinate chart.  The soft
  dependency points a referee will attack are listed in §2.1 (five, none fatal in my reading).
Q3: the uniform mechanism behind the engine is LEMMA INJ (PROVED-HERE from the banked factored
  Jacobian, §3.1): below the outer onset the first-point Jacobian band at t-power n annihilates
  B₁'s level n−1 unless d₃ | n, where the kernel is the one-dimensional h₃-power direction
  (w^6(w−1)^16 at n = 11, h₃ itself at n = 22 for (99,66); 9 | n at D = 108).  This is the
  "minor Prop 5.6" in embryo: a genuine split pins low-level coefficients that the injective
  bands force to zero.  The cheapest second-client selector is the INCIDENCE EXCESS
  (§3.2): (#nonzero incidence labels) − (#free h₃ coordinates) − (#branch parameters); it
  is −3 at (99,66) on both branches (survives to the Jacobian/pole stage) and +2 at D = 108
  (preflight death); definition in §3.2.
Q4 price: §5.  Single first lane: CARD C (K16 target split), then CARD B.  Systems: UPGRADE
  (round-trigger autonomy; this round fired 8.5 h late for a non-mathematical reason).
```

## 1. Q1 — the K = 16 uniform statement

### 1.1 The revised question has a negative answer, and the reason is structural

The revised Q1 asks whether ρ_t := Res_w(R_1, …, R_{t−1}) ∈ A_t is computable in closed form in t.
It is not, and not for lack of effort:

* **The system is not a fixed object indexed by t.** R_r lives in t−1 variables (b₄, q_{2,0}, …,
  q_{t−1,0}) of weights 1, …, t−1 and has weight 4t+4+2r. Its monomial support is *every*
  monomial of that weight (17(wwww) measured no sparsity in b_r, c_r at t = 3..7). The weighted
  Macaulay matrix whose determinant carries ρ_t is indexed by the monomials of weight
  σ+1 = Σ deg R_r − Σ wt + 1 in t−1 weighted variables — a partition-type count. A "closed form in
  t" of a determinant whose size is a partition function is not a formula anyone will write.
* **What IS stable in t is the truncated spine.** 17(wwww) proved that the b₃²-coefficients a_r
  of the top tail depend only on q_{2..r} and are rational functions of (t,d) for fixed r. Every
  other coefficient (b_r, c_r) carries the whole 2t+1-step spine and is a t-indexed *sequence*
  with denominators in the pivot norms F_C(t,j), F_Q(t,j) (17(iiii) §4), not a polynomial in t.
  Re-indexing from the top (q̃_j := q_{t−j,0}) does not help: c_r contains both top-indexed
  quadratic monomials q̃_j q̃_{j'} b₄^{2+r+j+j'} and bottom-indexed cubic ones; the support mixes
  both ends of the variable list.
* **Consequence for the running lane** (`k16-square-resultant-fable5`, my own model, receipt
  RUNNING): its valuable outputs are N(ρ_t) at t = 3, 4 (a nonzero norm is a clean fixed-t
  certificate of Lemma SQUARE's hypothesis) and the t = 2 factor check; the "closed form"
  sub-goal should be declared INCONCLUSIVE-BY-STRUCTURE when its budget is spent, not
  retried.

Typed: `IMPOSSIBLE-AS-FORMULA[RES-CLOSED-FORM]` (argument above; no computation needed).
The non-vanishing ρ_t ≠ 0 remains exactly as OPEN as (V0).

### 1.2 What the cone IS, and why (V0) is the wrong uniform target

Read the banked definition (17(zzz), my 17(iiii) §2): T_{t,k} = −[w^{4t+1−k}] σ_t(Δ) + yg·[k=0],
where Δ(w) = κv − ũψ is the level-0 Jacobian identity (D0) of the h-adic chart and σ_t is the
spine substitution; the rows k ≥ 1 are the w^{2t+2..4t} coefficients of Δ, the constant row is
"[w^{4t+1}]Δ = yg", and the w^{1..2t+1} coefficients are the spine pivots (units). Hence:

```text
V(I_{t,+}) = { residual points p : every Jacobian coefficient of the chart vanishes except
               [w^{4t+1}]Δ, which equals −τ_t(p) }.
```

By the weight torus, a cone point with τ_t(p) ≠ 0 rescales to a solution of the full terminal
system (this is Lemma CONE, banked). A cone point with τ_t(p) = 0 is a point where **Δ ≡ 0**:
all level-0 Jacobian coefficients vanish while the higher levels (D1)–(D3) are satisfied by the
spine. If Δ ≡ 0 together with (D1)–(D3) is the statement J(P,Q) ≡ 0 for the actual polynomial
pair of the chart — which is what the derivation of (2.1) suggests but which I have NOT
re-derived line by line (the scalar g = g₃ enters (D1)–(D3) as a leading-form scalar, and I
cannot exclude from the banked text that it is also the Jacobian constant) — then:

```text
CONJECTURE DEP.  V(I_{t,+}) ∩ {τ_t = 0} = { ansatz pairs (P,Q) with J(P,Q) ≡ 0 }
               = { ansatz pairs with P = φ(H), Q = ψ(H) }   (Gordan–Noether/Schinzel, char 0),
and (V0)  ⟺  (T) ∧ [ no such dependent pair other than the bare tower P = h^{3t+1}, Q = h^{2t+1} ].
```

Two banked facts make DEP more than a slogan. (i) At t = 2, y = 1/5 the cone is the b₃-axis and
τ_2 vanishes on it (17(cccc)): a one-parameter family of cone points with Δ ≡ 0 — under DEP, a
family of algebraically dependent pairs in the t = 2 ansatz shape. (ii) The b₃-axis theorem
(b₃ killed by a unit for t ≥ 3) removes exactly that family for t ≥ 3, and nothing more: it
says nothing about dependent pairs off the b₃-axis. Fixed-t certificates exclude them at
t ≤ 7; at t ≥ 8 nothing does.

**Why this matters for the program.** (V0) is the campaign's certification instrument (a
closed, properness-promotable dim-0 statement) but it is STRONGER than the theorem (T). If a
dependent pair exists in the ansatz shape at some t ≥ 8, then dim I_{t,+} > 0 there, every
cone-based lane at that t will report failure, and (T) may still be true. The campaign should
(a) split its uniform target into (8.1) [the theorem] and DEP-EMPTY [the instrument's
hypothesis], (b) test DEP-EMPTY by a *different and much smaller* system than the cone: impose
P = φ(H), Q = ψ(H) directly (H = h + lower h-adic terms with free coefficients of the chart's
support; φ, ψ univariate of degrees 3t+1, 2t+1; linear in φ, ψ for fixed H) intersected with the
order rows and gauges; (c) if DEP-EMPTY fails at some t, retarget the cone lanes to
τ_t ∈ √I_{t,+} directly (Rabinowitsch on the cone with 1 − zτ_t, as the banked
homogeneous-cone note already prescribes for dim > 0). Cheapest test: CARD C.

### 1.3 Two structural routes closed by desk tests (MEASURED, exact)

`box/ideation-0904-fable5/bigrading.py` loads the banked exact rows
`box/k16toptail-20260903/rows_t{3,4,5,6}_exact.sing` in the declared ring
`(0,yy),(b₄,q_{2,0},…,q_{t−1,0},b₃)` with `minpoly = H_t`, dumps every monomial exponent of every
row, and computes over Q the null space of all within-row exponent differences (the space of
weight vectors for which every row is homogeneous):

| t | rows | terms per row | difference vectors | nullity | basis |
|--:|--:|---|--:|--:|---|
| 3 | 5 | 16,12,12,9,9 | 53 | **1** | (1,2,4)/4 |
| 4 | 7 | 54,47,40,34,29,24,20 | 241 | **1** | (1,2,3,5)/5 |
| 5 | 9 | 171,…,44 | 866 | **1** | (1,2,3,4,6)/6 |
| 6 | 11 | 484,…,84 | 2678 | **1** | (1,…,5,7)/7 |

So I_{t,+} carries exactly the one known grading. A second torus would have forced every
positive-dimensional component of the cone onto "resonant" lines where two weight vectors are
proportional on the support — closed sub-chart statements, the kind the chain proves. That
argument is unavailable: the rows are not bihomogeneous. (Term counts agree with 17(iiii).)

`omega_search.py` computes, for every ω ∈ {−1,0,1}^t (modulo multiples of the grading, which
leave initial forms unchanged), the ideal generated by the ω-initial forms of the 2t−1 rows and
its dimension (exact std over A_t):

| t | ω tested | dim histogram | best ω |
|--:|--:|---|---|
| 3 | 26 | {1: 3, 2: 23} | −e_{b₄}, −e_{q₂}, −e_{b₃} (dim 1) |
| 4 | 80 | {1: 4, 2: 8, 3: 68} | −e_{b₄}, −e_{q₂}, −e_{q₃}, −e_{b₃} (dim 1) |

The only ω reaching dim 1 are the coordinate restrictions x_i = 0 (whose initial forms are
free of x_i, so x_i is a free direction — dim ≥ 1 is forced). Since
dim⟨in_ω(rows)⟩ ≥ dim in_ω(I) = dim I, a dim-0 initial system would have been a degeneration
certificate; none exists on the structured set. This generalises Grok's confirmed failure of
the sub-chart initial-form upgrade (17(xxxx)) — that failure is the trivial x_i-free case.
Random rational ω were not sampled (out of budget); a card-level test would sample 10³ ω at
t = 4 mod p in minutes, but I would not fund it: the (D3)-level structure (all rows' wp-leaders
are b₄-powers, 17(vvvv) §6) makes a monomial-rich initial system implausible.

### 1.4 What remains structural, priced

(a) *Induction in t.* No map of the (t+1)-cone to the t-cone is visible: the residual variable
list grows by one (q_{t,0} joins) and the spine re-solves every pivot. Price: unbounded; STOP
as a target. (b) *Hilbert/regular sequence.* Sol's corrected tail is an hsop at t = 3..6 with
the CI length t/(t+1)·C(3t+1,t) (an integer — the necessary degree-consistency check passes,
which is no evidence). Uniform regularity needs the same open-chart head as the chain. (c)
*Initial ideals.* Closed by 17(vvvv) §6 and §1.3. (d) *Deformation reading.* §1.2 is the
honest version: the cone is the J ∈ K·γ locus; its τ_t = 0 part is classical (dependent
pairs), its τ_t ≠ 0 part IS (T). No cohomological injectivity statement short-cuts (T).
**Recommendation:** keep the ray as the canonical *test family* for any proposed receiver
theorem (§5), certify DEP-EMPTY separately, and stop buying uniform-(V0) lanes.

## 2. Q2 — (99,66) after the promotion: what a referee attacks, and what the kills consist of

### 2.1 The dependency gates, hostile reading (receipts and sealed reports only)

The promoted verdict rests on: 17(sss) (split classification exhaustive on the detector
window), the design/outer/source gates (row-family necessity), the K2c unit-triangular ledger,
17(pppp) (δ = 2, unit 6264 at stage 4), 17(tttt) (δ = 5/2, unit 64 at stage 8), and the
clean-room agreement (Opus). My reading of the soft points, in decreasing order of referee
attention:

1. **Exhaustiveness must name branch A explicitly.** Moh p.209 (image read) states the fourth
   case's dichotomy as "either a power of a linear polynomial [→ the (27,18; 21; 8; −1; 0; X⁴)
   row] or the 9-th power of a cubic with precisely two roots [→ the Ω-transformed pair with
   J = x]"; Xu added the three-root cubic at δ = 5/2. The GPT-5.5 gate already flags that if
   17(sss) classifies *genuine splits* only, the unsplit alternative (branch A, killed by
   17(tt) through Moh's descent) is a separate dependency. The dossier must list it as such,
   with the descent's variable map (the same OPEN[DESCENT-SUPPORT/VARIABLE-MAP] shape that
   blocks D = 108's no-split alternative — is the (27,18; X⁴) kill of 17(tt) in a chart proved to
   receive every branch-A pair? that is the one place where I would expect a GAP).
2. **The equality face (π³−1)⁸ and its scale.** Opus derives "three clusters of eight" from the
   D₂/D₁ multiplicities (24, 8) and fixes the scale a = 1 by recentring. The dossier needs the
   sentence "a ≠ 0 because the face has three distinct roots; a = 1 by the π-scaling gauge, which
   is free because no other row has been normalised with it". Not fatal; must be written.
3. **The imported Hc_11_0 = 0** (Xu's T₃ ODE at level 1) is dimension-only (Opus §8.6: +1
   everywhere, residue unchanged). The dossier should drop it from the necessary system and
   keep it as a remark; then OPEN[EFFECTIVE-T2-T3-BRIDGE] does not touch the theorem at all.
4. **Pole rows.** Their necessity is "a polynomial pair has no Laurent coefficient below the
   face along the minor branch"; the face orders are Xu §7.3 / Prop 6.1 exact leading orders.
   Fine, provided the dossier states the branch series (t = s², w = u s⁴ + v s⁶ + π s⁷) as a
   *declared place*, not as the flag coordinate (FALLACY flag/place/series).
5. **The kill row is a G pole row at local power 16 = Laurent exponent −110.** Its vanishing is
   necessary because G is a polynomial; the certificate 1 = (1/64)·row is a rational identity
   after 66 rational pivots none of which involves c. Nothing soft here.

Verdict on (a): the promotion stands in my reading; the dossier's only real exposure is item 1.

### 2.2 The kills are INNER kills — this changes the necessity dossier and Q3

Opus's clean-room engine (17(tttt)) proved something the coordinator has not yet used: through
t-power 21 the identities KF = K2³ and KG = K2² + t·K_{B1}·K2 are *exact* after the outer D₂
preblock (A₂, B₂ survive only for r ≥ 21, A₃ for r ≥ 53), and every band that reaches either
certificate lives at t-power ≤ 8. Hence:

* the outer blocks enter the kills only as *zero facts* at low r (the D₂ preblock), never as
  live coefficients; the 5,598 D₂ pivots and 176 D₁ pivots are dimension bookkeeping;
* the killing system is the INNER joint chart: h₃ (21 free coordinates), the h₂ tower (C₂, C₃;
  106 low-q directions after D₂, 99 after D₁), B₁ through level 7, the branch face, the G pole
  rows, and the Jacobian bands at t-powers 1..8 (which, by Lemma INJ below, are B₁-linear);
* the T₂/T₃ bridge and the outer A/B blocks are not needed for the theorem, only for the
  counting bounds — so 17(uuuu)'s unfinished elimination is irrelevant to the promotion.

The minimal necessity dossier is therefore obtainable mechanically: trace the certificate
backwards through the pivot ledger (CARD A). Prediction: ≤ 300 rows, all sourced to Theorem
1.2 (h₃/h₂/B₁ order rows), the branch face, Laurent polynomiality (pole rows) and J = 1.

### 2.3 (b) Counterexample side

There is none left at (99,66): both branches die on rational constants; no REPRESENTATIVE
exists to recompose. The recomposition test (F_xG_y − F_yG_x ≡ 1) is the right last step for the
*first surviving* inner chart on a 166-group client (§3.3), not here.

## 3. Q3 — the u_s > 1 stratum: the uniform mechanism and the second client

### 3.1 Lemma INJ (PROVED-HERE from banked identities; typed UNREVIEWED)

Setting (17(tttt), Opus §3 "Mechanism"): with A = K2 = A₀ + tA₁ + … and B = K_{B1} = Σ t^j B_j,
below the outer onset the normalised Jacobian factors as
KJ = t·A³(N·A·B_w − (N−3)·B·A_w) + 3t²A³(A_w B_t − A_t B_w), N = deg F, and once
B₀ = … = B_{n−2} = 0,

```text
[t^n] KJ = A₀³ · L_n(B_{n−1}),     L_n(B) := N·A₀·B′ − (N − 3n)·A₀′·B,    A₀ = (top form of h₃)^{d₂/d₃}.
```

(Re-derived here from the two-term factored form: the first term contributes
N·A₀B′ − (N−3)A₀′B at t^n, the second contributes 3(n−1)A₀′B; sum = N·A₀B′ − (N−3n)A₀′B.)
The kernel of L_n on polynomials is B = C·A₀^{(N−3n)/N} = C·A₀^{(d₂−n)/d₂} (using N = 3d₂ in the
3+2 tower). With A₀ = w^{u d₂/d₃}(w−1)^{v d₂/d₃}, gcd(u,v) = 1, this is a polynomial iff
d₃ | (d₂ − n) iff **d₃ | n**, and then

```text
ker L_n = K · (top form of h₃)^{d₂/d₃ − n/d₃}     (dimension 1);   ker L_n = 0 otherwise.
```

Instances. (99,66): d₃ = 11, d₂ = 33; n = 11 → w⁶(w−1)¹⁶ = P², n = 22 → P = w³(w−1)⁸,
n = 33 → constants; every other n ≤ 20 is injective. (108,72): d₃ = 9, d₂ = 36; n = 9, 18, 27 →
(w²(w−1)⁷)^{3,2,1}; injective otherwise (valid for n ≤ 16, the A₂/B₂ onset r = 17).

Consequences. (i) The Jacobian bands below the onset are a *theorem*, not a computation: each
band n with d₃ ∤ n forces B₁'s level n−1 to vanish outright (this is the "9 pivots per stage" of
the ledger; the observed drops 9 → 8 → 7 are D₁ columns already zeroed, Opus §7). (ii) The
kernel levels n = d₃, 2d₃, … are exactly the *Tschirnhausen ambiguity* (B₁ ∝ a power of h₃),
i.e. the freedom the tower already quotiented — so below the onset a Keller pair's B₁ is rigid.
(iii) A genuine principal-minor split pins low-level h₃/B₁ coefficients to *nonzero* values
through the face (c_{2,9} = 3u, c_{3,8} = −3v, c_{7,4} = c − 3u²v, … at (99,66)); the pole rows
transport those pins into B₁-levels; an injective band then returns a nonzero constant. That
is the whole shape of both (99,66) deaths (Jacobian row at n = 4, k = 35 for δ = 2; G-pole row
at local power 16 for δ = 5/2 — the branch asymmetry is the parity of the pole rows under
t = s², Opus §7). This is the "minor Prop 5.6" the packet asks for, in embryo:

```text
CONJECTURE MINOR-5.6.  For every 3+2-tower skeleton with u_s > 1, a genuine principal-minor
split (face p with ≥ 2 distinct roots) is inconsistent with the inner joint chart below the
outer onset; the only faces compatible with Lemma INJ's kernel structure are h₃-power faces
(p a linear power) — Moh's branch A — which descend.
```

Cheapest tests: (1) rerun Opus's engine with the Jacobian band imposed *only* at n = 11 and
verify a one-dimensional kernel spanned by w⁶(w−1)¹⁶ (minutes; falsifies the lemma if the
kernel is larger); (2) the same at D = 108, n = 9 (the g108 engine, minutes); (3) run the
(99,66) engine with A₂ = A₃ = B₂ ≡ 0 imposed *as an identity* (not as bands) and check both
deaths reproduce at the same stages — if they do, the inner chart is the uniform object.

### 3.2 The second client: incidence excess as the selector

D = 108 died at preflight on the common-h₃ incidence (17(aaaaa)); (99,66) did not. The
difference is countable before any band runs. Define, for a branch,

```text
excess := (# incidence normal forms left after Q*-pivots on the h₃ leader block)
          − (# branch parameters not pinned by the face)         [face modulus excluded]
```

(99,66): 0 residual rows (18 resp. 20 pivots on 21 free h₃ coordinates) minus 3 free parameters
→ **−3** on both branches: preflight cannot kill; the decision moves to the pole/Jacobian
stages. (108,72): 5 residual normal forms (7 pivots on 7 free coordinates) minus 3 parameters
(jet₁, jet₂, c) → **+2**: a localized unit is generic, and it occurred. Rule: excess > 0 ⇒ expect
preflight death (the incidence compiler alone decides); excess ≤ 0 ⇒ the inner chart needs the
pole/Jacobian stages (Lemma INJ predicts which levels can carry a residue: the injective ones).
The 166 groups can be triaged in an afternoon with the row-generic split driver
(`box/g108minor-20260903/g108_minor_driver.py`, which already classifies splits for any
(n,m,M,V)) plus the h₃ free-coordinate count from the outer-weights rule (Grok 17(bbbbb),
`vmin(r)`): no chart, no bands. This is the cheapest uniformisation step and it precedes the
"incidence compiler ahead of the scheduler" that Sol asks for.

Second client after D = 108: pick the first group with excess ≤ 0 and d₃ ∤ (first pole level) —
that is the first client that tests Lemma INJ's *mechanism* rather than the incidence block.
The (120,80)/(120,100) rows named in the packet should be triaged by the same count before
any engine time is spent.

### 3.3 Uniformisation: what the engine family is

A chart family indexed by (skeleton, split datum) exists and is small: the inner joint chart
of §2.2, parameterised by (n, m, d₂, d₃, u_s, v_s; δ, partition, face). Its row families are:
Theorem-1.2 rows for h₃ and the h₂ tower (Grok's general W₀/E₀ formulae, 17(bbbbb)), the D₂
zero-facts on the outer blocks at low r, the incidence block (compiler), the pole rows
(schedule from ord_t(t^{deg}X) = deg + (deg/d_s)(u_sδ − v_s)), and the Jacobian bands, which
by Lemma INJ need no Gröbner at all below the onset: they are the linear maps L_n. The
scheduler then runs stage n = 1, 2, … until a residue; Lemma INJ says a residue can only appear
at an injective level from a pinned coefficient, so the engine can *predict* its own killing
stage from the pole schedule — which is the right diagnostic to print.

## 4. Q4 — the all-degree program, the theorem, and the price

### 4.1 The program in one sentence and its theorem

**Program.** Boundary pins N = O(1) (PROMOTED); the whole-major-tree ∧ ODE ∧ Xu screen is a
fail-closed target generator that never empties (PROMOTED, cofinal K16 ray); the proof is a
coefficient theorem in a *descended* coordinate where the Jacobian is a monomial:

```text
RECEIVER-EMPTINESS(𝒟).  For every descended two-point datum D = (n', m'; M₂'; V₂'; k) ∈ 𝒟 there is
no pair (P,Q) ∈ K[γ,π]² of π-degrees (n', m') with J(P,Q) = c·γ^k (c ≠ 0) whose order data at
the second point are (M₂', V₂')  —  where 𝒟 is the set of data reached from Moh's census by
Prop 6.3/6.4 descent (u_s = 1), by the no-split conditional descent (u_s > 1, δ* ≥ v_s/u_s), and
— in the un-descended form of the inner joint chart — by the genuine-split branches (u_s > 1).
```

Every promoted or provisional kill the campaign owns is an instance: Moh's five Appendix-II
rows; the K16 ray at t = 1..7 (k = 1); (27,18; 21; 8; k = 4) = branch A of (99,66) (Moh p.209,
17(tt)); the inner joint-chart kills of branches B and 5/2 (un-descended instances); (24,16;
18; 7; k = 4) for D = 108's no-split alternative (conditional); (25,15; 21; 2; k = 2) (provisional);
the validation rows (16,12), (28,20), (33,22), (45,30), (15,10), (21,14). The K16 ray is the
only *infinite* instance family in sight, and it is exactly the receiver at k = 1.

So the answer to "family, census, or theorem" is: **the theorem, whose instance list is the
census, of which the family is the only infinite piece.** Three price tags:

| object | what it costs | what it buys |
|---|---|---|
| census through D ≤ 200 (166 u_s > 1 groups + 10 open two-point rows) | engine-weeks: incidence-excess triage (afternoon), inner joint charts for excess ≤ 0 groups (hours each), order charts for the descended rows (seconds–minutes each, gates included) | Moh's line to D = 200, paper-grade if the dossier template (Card A) is reused |
| K16 ray uniform (T) | UNPRICED: needs an invariant of monomial-Jacobian pairs that sees (M₂', V₂') uniformly in t; Lemma INJ is already consumed there (it *is* the spine, §4.2) | JC2 along the only cofinal screened family |
| RECEIVER-EMPTINESS in general | the same invariant, plus the descent's variable maps as theorems (OPEN[DESCENT-SUPPORT/VARIABLE-MAP], OPEN[TWISTED-64]) | Moh's line for all D, hence — with the boundary pin — JC2 |

### 4.2 Why the K16 ray is the hard residue and not a shortcut

On the census, Lemma INJ is new information (§3.1). On the ray it is not: the 2t+1 "high
pivots" of the spine, solved by proved nonzero diagonals p_j (17(zzz) (2.9)–(2.12)), are
precisely the injective Jacobian levels of the receiver pair, and the terminal family
T_{t,0..2t−1} is what injectivity leaves — the kernel-side residue. This is why every
one-point/axis/sub-chart statement on the ray is a unit (the injective part keeps working
on sub-charts) and why the head (C0) is not: the head is the first genuinely non-injective
question. A proof of (T) for all t therefore needs an invariant that is *not* Jacobian
injectivity. The two candidates I would fund, in order: (α) the dependent-pair structure of
§1.2 — it settles the τ_t = 0 part of the cone by classical theory and turns the instrument
question into a small system; (β) the Brieskorn/Gauss–Manin class of the receiver pencil
(row 29) restricted to the k = 1 receiver, where "J = cγ" says the class of dx∧dy is
γ-torsion — a statement one can at least *compute* on the K16 ansatz at t = 2, 3.

### 4.3 Where the coordinator's framing is wrong

1. *Revised Q1 asks for a formula.* No formula exists (§1.1); the right question is whether
   the instrument (V0) is even true for all t (§1.2), and the answer is "not known, and it
   failed once already on the y = 1/5 fibre".
2. *Q3 treats the 7,161-coordinate chart as the engine.* The kills are inner (§2.2); the
   uniform object is the inner chart + incidence compiler + Lemma INJ, an order of magnitude
   smaller, and the outer bands should be demoted to counting bounds in the dossier.
3. *Q4's trichotomy* is one object with three prices (§4.1).
4. *"(25,15) is the smallest open u_s > 1 row"* — it is the descended datum with u' = K − V₂' = 3;
   the packet should say so, because the gate must decide whether the *sparse prefix tower*
   of the order chart (5 parameters, 7 support monomials inside the 13-monomial Lemma-2.1
   envelope) is the full h-chart for that row or a SLICE of it (§7).
5. *Q2's "what would a surviving family look like"* is moot at (99,66); it is the right
   question for the first excess ≤ 0 client that survives its injective levels (§3.2).

## 5. Disposition vector (APPROACHES rows, changes only) and bottlenecks

* Row 1 (GGV corner families / [P,Q] = x^k): **RAISE to the top** — it is the receiver of
  §4.1; every promoted kill is an instance. Retarget its engine to the descended data list
  𝒟 (Card A's dossier gives the first entries).
* Row 3 (vertex-gap / strip ODEs, "the campaign's actual theorem"): **RAISE** — Lemma INJ is a
  strip-ODE statement (L_n is a first-order linear operator on one band with kernel a
  monomial power); the row's Żołądek-A.7 rigidity is exactly ker L_n.
* Row 29 (LND / Gauss–Manin κ(P)): **RAISE one notch** as the only non-injectivity invariant
  candidate for the ray (§4.2 (β)); compute before believing.
* Row 36 (guided CE search): **RETARGET** to the dependent-pair locus of the K16 ansatz at
  t = 8 (Card C) — not a counterexample hunt but the instrument's falsifier.
* Row 46 (Lean / formal certification): **RAISE for rigor only** — the (99,66) certificate slice
  (Card A) is a finite rational identity of a few hundred rows, the first campaign object
  worth formalising end-to-end; no discovery value.
* Row 2 (boundary trees): unchanged (closed as ceiling). Rows 6, 7, 25, 26, 32: unchanged.
  Row 8/9 (formal inverse, Lee–Li): unchanged LOW. Row 20 (char p): unchanged diagnostic.
* Queued fronts: 166-group census — **REDESIGN** (incidence-excess triage first, inner chart
  only, Lemma INJ scheduler); uniform-(V0) K16 lanes — **STOP** buying them until Card C
  reports; k16-square-resultant — let it finish, then STOP the formula sub-goal.

**Bottlenecks reranked.** Proof side: (P1) DEP-EMPTY vs (T) on the ray — decides the K16
target (Card C, hours); (P2) the certificate slice as the dossier template (Card A, hours;
paper-grade (99,66)); (P3) Lemma INJ gate + incidence-excess triage of the 166 groups (Card B,
a day) → the second and third clients; (P4) the descent variable maps as theorems
(OPEN[DESCENT-SUPPORT/VARIABLE-MAP], OPEN[TWISTED-64]) — without them the no-split
alternatives of the stratum stay conditional; (P5) the receiver invariant (§4.2) —
unpriced. Disproof side: (C1) the first excess ≤ 0 client whose injective levels all pass
(a SURVIVES of the inner chart) — then the outer bands and the bridge decide, and a
recomposition test is finally meaningful; (C2) a dependent family on the ray at t ≥ 8 —
breaks the instrument, not the conjecture; (C3) a REPRESENTATIVE on a descended k ≥ 2 datum
of the seven large two-point rows once the order chart is gated (the (25,15) slice question
§7 is the first place a false kill could hide).

## 6. Idea cards (three)

**CARD A — CERTIFICATE SLICE (the minimal necessity dossier by backward pivot tracing).**
Target obstruction: paper-grade necessity for (99,66) (revised Q3). Mechanism: the engine's
ledger records every Q*-pivot (row, variable, rational coefficient); starting from the unit
row (stage8_G_local16_coord0 = 64; stage4_J_d159_k35 = 6264) collect recursively the pivot
rows whose substituted variables occur in it, and the D₂/D₁ zero-facts that removed
coordinates from those rows. Object: a directed acyclic graph of ≤ 66 + 35 pivots plus their
support. Dependencies: `box/g9966band-20260903/` ledgers (exist), Opus's engine (33 s per
branch). Cheapest discriminator: run the trace; count rows per family. Outcomes: (i) slice ≤
300 rows with no outer A₂/A₃/B₂ *coefficient* — the dossier is short and the outer bands are
bookkeeping (expected, §2.2); (ii) an outer coefficient appears — the dossier must source the
outer D₁ rows too (still finite); (iii) the trace touches a T₂/T₃ bridge row — impossible
(none is imposed). Stop: none needed (deterministic). Information gain: high — it fixes the
size and the sources of the theorem, and it is the template every later client reuses.

**CARD B — LEMMA INJ + INCIDENCE EXCESS (the minor Prop 5.6 programme).** Target
obstruction: uniformisation across the 166 groups (Q3). Mechanism: §3.1's operator L_n with
kernel (top h₃)^{d₂/d₃ − n/d₃} at d₃ | n and zero otherwise; §3.2's excess count.
Dependencies: Opus's factored KJ (verified by Opus term-by-term at truncation 5), the g108
split driver, Grok's vmin rule. Cheapest discriminator: (1) at (99,66) impose the Jacobian
band only at n = 11 and print the kernel (expect 1-dim, w⁶(w−1)¹⁶); at n = 4 (expect 0); (2)
at D = 108, n = 9 (expect 1-dim); (3) triage the 166 groups by excess. Outcomes: kernel as
predicted → the scheduler can pre-announce killing stages and the dossier's Jacobian section
becomes one lemma; kernel larger → my derivation missed a term (then the factored form's
validity range is the issue) — either way information. Excess triage: a histogram; groups
with excess > 0 are preflight kills by the compiler alone. Stop: if (1) fails at n = 4 (kernel
≠ 0 where injectivity is claimed). Information gain: high on the stratum; nil on the ray.

**CARD C — DEPENDENT-PAIR LOCUS (split the K16 target).** Target obstruction: the uniform
K16 statement (Q1). Mechanism: §1.2 — cone ∩ {τ_t = 0} = dependent ansatz pairs
(CONJECTURE DEP); DEP-EMPTY by a direct small system. Dependencies: the banked t = 2 records
(`terminal_laurent_t2.json`), the chart definition in the Sol/Fable terminal-proof reports
(to rebuild the actual (P,Q) from a residual point), Gordan–Noether/Schinzel. Cheapest
discriminator, three steps: (1) at t = 2, y = 1/5, take a b₃-axis point, rebuild (P,Q), compute
J(P,Q) — DEP predicts J ≡ 0 exactly (minutes); if J ≠ 0 there, DEP is false and the card stops;
(2) if J ≡ 0, exhibit H with P = φ(H), Q = ψ(H) (gcd of fibres; minutes); (3) at t = 8 (where the
cone is Gröbner-exhausted, 17(yyyy)), solve the *dependent-pair system* — H = h + Σ ε_j h^{−j}
in the chart's support, φ, ψ univariate, order rows and gauges imposed — expected far smaller
than the cone (linear in φ, ψ for fixed H). Outcomes: DEP-EMPTY holds at t = 8 → (V0) is not
refuted there, and the instrument stands one step further; DEP-EMPTY fails at t = 8 → (V0)
FAILS at t = 8, the campaign switches to (8.1) and stops all cone-dim lanes; DEP itself false
at step (1) → §1.2 is withdrawn and the cone's τ = 0 part needs a different reading. Stop: any
step returning a witness settles the card. Information gain: highest of the three — it
decides what "the uniform K16 statement" even is.

## 7. Lanes — continue / redesign / stop (receipts only) and the single first lane

Six packet-listed lanes, all `final_status=DONE` by receipt: k16-subchart-q-opus5
(22:19Z), k16-t6-sol56 (23:13Z), k16-t11-cone-gpt55 (23:52Z), preprocess-native-gpt55
(22:44Z), g9966-branchB-kill-gate-gpt55 (22:46Z), g9966-delta52-stage8-sol56 (23:06Z).
Dispositions: **STOP** further fixed-t cone attempts at t ≥ 8 (exhausted, 17(yyyy)); **STOP**
the native preprocessing line (superseded by the order chart, 17(zzzz)); the rest need no
action.

Four lanes RUNNING by receipt (no `final_status`; reports not opened):

* `g108-delta3-kill-gate-gpt55` (08:25Z): **CONTINUE**. Its hostile item — is "the two
  12-packets share h₃" a necessity or a convention — is the right one; §3.2 predicts the
  branch dies on the incidence block *whatever* gauge is chosen because excess = +2, so a
  weakened block should still return a unit unless it frees ≥ 3 coordinates.
* `g9966-chart-necessity-opus5` (08:25Z): **CONTINUE, REDESIGN scope** — organise the dossier
  around the certificate slice (Card A): the sourced rows are those the certificate consumes;
  the outer D₂/D₁ bands and the T₂/T₃ bridge are counting bounds; branch A (17(tt)) must be a
  named dependency with its descent map (§2.1 item 1).
* `k16-square-resultant-fable5` (08:25Z): **CONTINUE to its budget, then STOP the formula
  sub-goal** (§1.1). Keep N(ρ_t) at t = 3, 4 and the t = 2 factor check as its deliverables.
* `row2515-order-gate-sol56` (08:25Z): **CONTINUE, with one added question**: the order chart
  builds h from a *sparse approximate-root prefix tower* (5 parameters, 7 support monomials)
  and only checks that its support lies *inside* the corrected Lemma-2.1/D₁ envelope (the
  report prints parameters/support 5/7 for (25,15) and 11/13, 15/20 for two validation rows,
  but not the envelope's own size). If a Keller pair's h can carry envelope monomials the
  prefix tower cannot produce, SATURATED-EMPTY is a SLICE, not a kill (the same failure class
  as the single-equation support artefacts found by the 09-03 twopoint-kills gate). The gate
  must either prove the prefix tower is the full h-chart for this row (as it
  is for K16, where the banked charts coincide) or rerun with the full envelope.

**Single first lane:** **CARD C** (`k16-dependent-locus`, any adapter; ≤ 120 min; steps (1)–(2)
are minutes and decide the reading; step (3) is the first t = 8 statement about the ray that
does not need a Gröbner basis). Second: CARD B(1)–(2) (`inj-kernel-gate`, minutes each).
Card A is a redesign input to the running dossier lane, not a new seat.

## 8. Campaign-systems check — UPGRADE (round-trigger autonomy)

Evidence: this round was scheduled at 00:00Z and fired at 08:30Z because the coordinator seat
paused on credits (17(ccccc)); COORDINATION's 12-hour cadence was broken by a non-mathematical
cause, and the coordinator's own blind submission is now partly superseded by ten seals it
could not see. Upgrade: `ops/round_trigger.sh` — a cron-fired job, independent of the
coordinator process, that at each scheduled round (i) freezes the packet from the newest LIVE
STATE + the sealed reports since the last round (a mechanical template with the packet's
fixed sections), (ii) writes the launch manifest and receipts, (iii) launches the blind lanes
through the pinned adapters with a hard credit/balance check per adapter, and (iv) leaves
synthesis to the coordinator when it returns. Smallest useful test: a dry run at the next
scheduled round that only freezes the packet and writes the manifest (no launches), diffed
against the coordinator's hand-written packet. Regression risk: low (no ledger writes).
Runner-up (recorded, not chosen): a Singular wrapper that greps each `.out` for
`div. by 0` / `error occurred` and returns non-zero, since Singular errors are not fail-stop
(two lanes were bitten on 09-03).

## 9. OPENs raised, FALLACY-v2 check, typed block

OPENS RAISED

- `OPEN[K16-DEPENDENT-LOCUS]` — is V(I_{t,+}) ∩ {τ_t = 0} the locus of algebraically dependent
  ansatz pairs (CONJECTURE DEP, §1.2)? Bounded: one Jacobian evaluation at a t = 2, y = 1/5
  b₃-axis point. Cheapest test: Card C step (1).
- `OPEN[K16-V0-VS-T]` — can dim I_{t,+} > 0 while (T) holds at some t ≥ 8 (as at t = 2, y = 1/5)?
  Bounded: the dependent-pair system at t = 8 (≤ 3t+1 + 2t+1 univariate coefficients plus the
  h-adic perturbations of H in the chart's support). Cheapest test: Card C step (3).
- `OPEN[INJ-KERNEL-D3]` — Lemma INJ: below the outer onset ker L_n = K·(top h₃)^{d₂/d₃ − n/d₃}
  for d₃ | n and 0 otherwise, for every 3+2-tower skeleton. Bounded: one first-order ODE per
  skeleton. Cheapest test: (99,66) at n = 4, 11; (108,72) at n = 9 (Card B (1)–(2)).
- `OPEN[INCIDENCE-EXCESS-SCREEN]` — does the sign of the excess of §3.2 predict preflight
  death across the 166 u_s > 1 groups? Bounded: 166 evaluations of the split driver + vmin
  count; calibration (99,66) → −3 (survives preflight), (108,72) → +2 (dies). Cheapest test:
  Card B (3).
- `OPEN[CERTIFICATE-SLICE]` — the minimal row set consumed by the two (99,66) certificates.
  Bounded: ≤ 101 pivot rows plus their D₂/D₁ zero-facts (≤ 300 rows predicted). Cheapest
  test: Card A.
- `OPEN[RECEIVER-STATEMENT]` — the exact class 𝒟 of descended data for which
  RECEIVER-EMPTINESS is claimed, with the descent maps typed (theorem / conditional / inner
  chart). Bounded: the list of §4.1 (13 entries today). Cheapest test: write it; run the order
  chart on each descended entry (all already [1] except the conditional maps).
- `OPEN[2515-PREFIX-TOWER-SLICE]` — is the sparse approximate-root prefix tower of the general
  order chart the full h-chart for (25,15; 21; 2; k = 2), or a slice of the Lemma-2.1 envelope?
  Bounded: one support comparison (7 vs the envelope's count) and one rerun with the full
  envelope. Cheapest test: the running gate (§7).
- `OPEN[RES-CLOSED-FORM]` — CLOSED NEGATIVE here (typed IMPOSSIBLE-AS-FORMULA, §1.1); not
  re-raised.

FALLACY-v2. No exit-price assertion (no `charge_basis` line due). Flag/place/series: §2.1
item 4 and §3.1 keep the major flag (t = s^{A₂}), the minor place (the branch series) and the
cover series distinct; Lemma INJ is stated at the first point only. Per-ray/exit-set charge:
none. Carrier/attainment: the excess count and Lemma INJ are *predictions* of where a kill can
occur, never kills; §1.3's dim-1 initial systems are lower bounds on nothing (a dim-1 initial
ideal proves no dimension of I). Pole/interior: the pole rows are used only as Laurent
polynomiality, with the branch series declared. Floor/attainment: Theorem 1.2 rows are ≥;
the CI length integrality in §1.4 is a consistency check, explicitly "no evidence".
`sat()`: not used; the desk tests use exact `std` over the declared field with `minpoly`,
generator order printed in the scripts. Raw remainder degree: not used. Variable/ring map:
the desk scripts declare `(0,yy),(b₄,q_{2,0},…,b₃),wp(1,2,…,t−1,t+1)` and read the banked
row files unchanged; ω-initial forms are computed from exponent vectors, not from a term
order. Prime label/derivative: B′, A₀′ in §3.1 are d/dw, stated. Merge-free/M-descent,
target/arrival index: not touched. CONJECTURE DEP and MINOR-5.6 are typed conjectures with
tests, not promotions; Lemma INJ is PROVED-HERE/UNREVIEWED from a banked identity whose
validity range (below the outer onset) is stated.

```text
SUBMISSION   ideation-20260904T0000Z-fable5 (Fable 5), basis ce00e907, packet ba345ef1 (4/4 OK)
Q1           closed form of Res_w: IMPOSSIBLE-AS-FORMULA; second grading: NONE (t=3..6, exact);
             degeneration weight in {-1,0,1}^t: NONE (t=3,4, exact); uniform target should be
             (8.1) with DEP-EMPTY as the instrument's separate hypothesis (CONJECTURE DEP)
Q2           promotion stands; exposure = branch A as a named dependency; kills are INNER
             (t-power <= 8); minimal dossier = certificate slice
Q3           Lemma INJ (PROVED-HERE/UNREVIEWED): ker L_n = K*(top h3)^(d2/d3 - n/d3) iff d3 | n;
             incidence excess: (99,66) -3, (108,72) +2; uniform object = inner joint chart
Q4           RECEIVER-EMPTINESS(D) is the theorem; census = instance list; K16 = infinite piece
FIRST LANE   Card C (k16-dependent-locus); then Card B (inj-kernel-gate)
SYSTEMS      UPGRADE round-trigger autonomy (dry run at next round)
DESK         box/ideation-0904-fable5/{bigrading.py,omega_search.py,*.sing,*.out,*.json};
             Singular 4.3.2, exact over A_t, < 2 s per test, one core
```

Reproduction: `cd box/ideation-0904-fable5 && python3 bigrading.py && python3 omega_search.py`
(reads `box/k16toptail-20260903/rows_t{3..6}_exact.sing`; writes `bigrading_t*.{sing,out,json}`,
`omega_t{3,4}.{sing,out}`).

## COLLISIONS

Scan: `python3 ops/open_collision.py --root . xmodel/ideation-20260904T0000Z-fable5.md`, filtered
in the shell with `grep -v "ideation-20260904T0000Z-"` before display (0 same-round lines were
removed; the raw and filtered outputs are byte-identical, `box/ideation-0904-fable5/collision_*.md`).
Status: CANDIDATES. Reading of each hit set (lexical candidates, none a closure):

- `OPEN[K16-DEPENDENT-LOCUS]`, `OPEN[K16-V0-VS-T]`, `OPEN[INJ-KERNEL-D3]`,
  `OPEN[INCIDENCE-EXCESS-SCREEN]`, `OPEN[RECEIVER-STATEMENT]`, `OPEN[2515-PREFIX-TOWER-SLICE]`: NONE.
- `OPEN[CERTIFICATE-SLICE]`: hits at `AUDIT.md:16903` (17(vv), the gated (132,88)/(180,120)
  descended kills — a different object), `AUDIT.md:17539` (17(iiii), the properness lemma —
  shares the word "certificate" only), `notes.md:20770` (admissible covers), three 08-2x
  reports and `preprocess-native-gpt55-20260903.md:93` (Q*-pivot pattern on K16 controls — the
  same pivot *mechanism*, not a slice of the (99,66) certificate). No prior trace of a
  certificate back through the (99,66) pivot ledger exists; the OPEN stands.
- `OPEN[RES-CLOSED-FORM]` (closed negative here): hits at `AUDIT.md:17672` (17(tttt), unrelated
  "closed" wording), `notes.md:20770`, `ideation-20260828T1707Z-cross-grok.md:183`. None
  concerns the weighted resultant; the negative typing stands.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `45443`.
- Body SHA-256:
  `a456ddd27d56128d90992a35d0eb1ece668115b0e24be020b2e558b8d54bab53`.
- Frozen basis: `ce00e907002c40891a1d441badbc569100789e29`.
