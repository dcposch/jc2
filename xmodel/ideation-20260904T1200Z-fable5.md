# Blind ideation submission — round 20260904T1200Z — Fable 5

Lane `ideation-20260904T1200Z-fable5`, basis `bb2a1a78`, written 2026-09-04 11:57Z–.
Packet `ideation-20260904T1200Z-packet.md` (sha256 `1ee8e07b…`). Custody: the receipt's paired
`charged_input_<i>_sha256=` / `_basename=` lines were turned into a manifest by `awk` and piped to
`sha256sum -c`: **4/4 OK**, no digit retyped (the lane mount is read-only, so the manifest was
streamed, not written). Read before writing: the packet, the 0000Z synthesis, FALLACY-v2,
COORDINATION (full-spectrum contract, seal and OPEN authoring rules), AUDIT deltas
17(tttt)–(ooooo) plus 17(pp)/(tt)/(uu)/(bbb)/(hhh)/(lll), the newest LIVE STATE (08:22Z) and the
EVENT lines through 11:36Z, APPROACHES (overlays + rows 1–46), PROGRESS, and the sealed reports
k16-dep-locus-fable5, k16-square-tail-stdhilb-gpt55, k16-hilbert-regseq-sol56,
k16-toptail-quadratics-fable5, k16-terminal-proof-sol56 (§2), minor-empty-disc-sol56,
minor-residue-formula-opus5, two-place-obstruction-core-sol56, g9966-chart-necessity-opus5,
g9966-gauge-gaps-grok46, order-basis-full-gpt55, row2515-order-gate-sol56,
g108-nosplit-descent-grok46, g108-delta3-kill-gate-gpt55, and — after its receipt showed
`final_status=DONE` at 12:03:36Z — k16-hsop-length-allt-opus5. No ideation-20260904T1200Z-*
submission was opened; no ledger edit; no jc2-lean. Desk CAS: `box/ideation-20260904T1200Z-fable5/`.
No exit-price assertion is made, so no `charge_basis` line is due.

## 0. Headline — direct answers

```text
Q1 (K16).  The tail-hsop / length statement is NOT provable for all t by weighted Froberg, by a
  triangular change of generators, or by a Bezout/resultant bound: the sealed hsop lane (Opus,
  12:03Z) PROVES all three impossible (NO-COPRIME-LEADERS for t not in {3,5}; DEGREE-BLIND — the
  two t = 2 fibres have identical degree data and opposite dimensions; the b3-eliminant costs
  exactly 2^{t-2}).  What survives is TAIL-SPLIT + criterion RANK: dim 0 <=> a NON-VANISHING
  ALONG A CURVE (the rank-<=1 locus of the (t-1)x2 matrix (C_r,B_r)) whose scalars are the
  spine-complete b_r, c_r.  So the sharpest PROVABLE all-t statement today is structural, not
  decisive: S_t/(T_{t,2t-1}) is free of rank 2 over P_t and (V0) <=> dim M_t/(G_1..G_{t-1}) = 0.
  Z-EMPTY_t is NOT the better all-t target: it is the same size as the cone and it is
  JC2-irrelevant (z-type pairs have the Jacobian line through the SIMPLE place; no receiver datum
  has that).  The JC2-relevant all-t statement is (8.1) alone: cone ⊂ V(τ_t).  RECOMMENDATION:
  demote (V0) from target to fixed-t instrument, STOP all-t K16 lanes after one cheap probe
  (§1.4: the exact radical-membership certificate τ_t^N ∈ I_{t,+} at t = 2 (y = 1/5), 3, 4 — the
  only place where (8.1) is FORCED to hold by an identity rather than by dim 0), and move the
  (H2) flagship to the k = 4 ray (§4).
Q2 ((99,66)).  Case (A) = (27,18; 21; 8; k = 4) is the K = 9 member of the two-point ray
  (3K, 2K; 3K-6; K-1; k = 4), (δ2',δ1') = (-1, 0), whose K = 7, 8 members are the open rows
  (147,98) → (21,14; 15; 6; 4) and (168,112) → (24,16; 18; 7; 4) — the latter ALSO the D = 108
  no-split datum (17(fffff)).  So case (A), D = 108 and the three δ1' = 0 two-point rows are ONE
  object.  Decide it structurally, uniformly in K, not by the 110–141-unknown full-basis Groebner
  runs (the emitted systems are 58–256 MB; slimgb has no chance; §3.3 gives the cheap fix).
  N1/N2: N2 is closable by a source read plus FOUR finite face-ODE runs (Xu §8(i)'s
  one-sentence elimination of δ ∈ {4/3, 3/2, 5/3, 7/3}, Cor 7.5-shaped) and one Galois argument
  (den(δ) ≤ u_s from Moh p.201 (8)–(11)); N1 is NOT closable by reading — Moh's printed (1)–(13)
  leave 8 V-assignments at (99,66) and his extra restrictions are unprinted — so THEOREM 8.1 can
  become unconditional as a ROW theorem, never as a DEGREE theorem, until the other seven
  (99,66) V-rows are killed or screened (§2.3).
Q3 ((H1)).  No uniform theorem route survives: Sol's O4 (the augmented Schur row) is exactly the
  content of each kill and is datum-specific (FILTRATION-PAGE-RULE).  Commit to the CENSUS, but
  price it honestly: the 166 u_s > 1 groups need the INNER joint chart + incidence compiler
  (hours/group after preflight), NOT the order chart.  Minimal compute change for the
  full-basis systems: replace one slimgb call on an inhomogeneous 472–598-row system by the
  (99,66) engine's staged Q*-pivot elimination (rows are affine in their band's new coefficients
  with unit pivots: Lemma INJ), branch on the PRODUCT rows that the top face leaves (the first
  emitted rows are literally 9·A2_2_7·B2_2_7 = 0), and Groebner only the residual.  A desk
  implementation of exactly this ran during this lane (§3.3, receipts in the box).
Q4.  Single most valuable object: the k = 4 ray (3K, 2K; 3K-6; K-1; k = 4) with J = c·γ^4 and
  e = 3, q = 2 — Moh's own p.208–209 method (g ≈ f^{3/2}, 10 coefficients at K = 9) made uniform
  in K.  It closes D = 108, (99,66) case (A) and three open two-point rows at once, and its tower
  has FIXED shape (only deg h = K grows), unlike K16 where the tower grows with t.
  Is (H1) ∧ (H2) complete?  As a reduction of the CENSUS, yes modulo N2 (den(δ) ≤ u_s; the ODE
  elimination at the four other orders; iterated splits are covered because the first-split
  chart is necessary for every refinement).  As a reduction of plane JC2, NO: the missing third
  configuration is not a split type but a SKELETON — every (1)–(13)-admissible V-assignment the
  screen does not kill is a census row that (H1)/(H2) must visit; at (99,66) alone there are
  seven besides Moh's printed one.  "JC2 along Moh's line" is the census statement, and the
  census is the theorem's instance list; the framing is right about that and wrong to call
  (99,66) "closed at skeleton level" for the DEGREES (99,66).
FIRST LANE   k4-ray-uniform (build the corrected full chart of the k = 4 ray at K = 4..7 with the
             staged pivot engine; find the K-uniform certificate).  SYSTEMS: UPGRADE — emit
             order charts as staged band files, not one 180 MB ideal (§8).
```

## 1. Q1 — K16: what is now proved impossible, and the sharpest provable statement

### 1.1 The three routes named in Q1, each with its verdict

The packet asks whether L_t = 2·binom(3t+1, t−1) is provable for all t by (a) weighted Fröberg,
(b) a triangular regular-sequence change of generators, or (c) a uniform Bézout/resultant bound.
The hsop lane sealed at 12:03Z (receipt `final_status=DONE`; opened only after that) answers all
three, and its answers are theorems, not timeouts:

* (a) and (c) — **Theorem DEGREE-BLIND**: at t = 2 the fibres y = 1/5 and y = 2/5 carry tail
  systems with identical degree data (rows of weight 6, 7; variables of weight 1, 3) and opposite
  answers (dim 1 versus dim 0 of length 14 = L_2). No invariant computed from the weighted
  degrees alone — Fröberg prefix, Bézout product, CI numerator — can certify dim 0. The length
  identity itself IS proved for all t (Theorem CI-SERIES: P_t(s) = (1+s^{t+1})·[3t+1 choose t−1]_s,
  nonnegative, palindromic), but it is the series the quotient *has if* the tail is an hsop; the
  implication never reverses.
* (b) — **Theorem NO-COPRIME-LEADERS**: for t ∉ {3,5} no monomial order and no generating set of
  J_t^tail makes the t leaders pairwise coprime (the degree window [2t+3, 3t+1] contains two
  primes for t ≥ 16 by Nagura, breaking Hall's condition; t ≤ 15 is a finite table). The
  "triangular change making the leading terms coprime powers" cannot exist.
* what survives — **Theorem TAIL-SPLIT**: a_0 = −α_t is a unit for every t ≥ 3 (norm
  −4(t−2)(2t+1)²(3t−1)²(3t+2)(27t³+17t²+t+2), vanishing only at t = 2), so
  M_t = S_t/(T_{t,2t−1}) is free of rank 2 over P_t = A_t[b4, q_{2,0..t−1,0}], the other t−1 rows
  become b3-LINEAR forms G_r = B_r b3 + C_r, and the tail is an hsop iff
  dim M_t/(G_1..G_{t−1}) = 0. **Criterion RANK** (exact): V(J_t^tail) = {0} iff (i) V(B, C) = {0}
  and (ii) along the rank-≤1 locus of the (t−1)×2 matrix N = (C_r, B_r) — expected dimension ONE —
  some W_r = a_0C_r² − b_0B_rC_r + c_0B_r² is nonzero. The residual is a non-vanishing along a
  curve whose scalars are values of b_r, c_r, which carry the whole 2t+1-step spine and have no
  closed form in t (my toptail report §3(c), Sol §6.3).

So the honest answer to Q1's first clause is: **not by any of the three named mechanisms, and
this is proved.** The tail-hsop statement remains true at every checked index (t = 3..6 both
fibres; t = 7 one fibre) and is verified at t = 2, y = 2/5 (length 14, new), but its all-t proof
needs an input that is neither degree data nor a monomial order: a unit statement along a curve.

### 1.2 Z-EMPTY is not the better target; it is the wrong target

Card C (my lane, 17(kkkkk)) proved J(Q_p, P_p) = cγ + π·E_t(h) at every residual point, hence
(V0) ⟺ (T) ∧ Z-EMPTY_t. Two consequences the packet under-weights:

1. Z-EMPTY_t is the cone plus ONE more homogeneous generator (T^hom_{t,0}) — it is not smaller
   than (V0), so it cannot be a cheaper all-t target; and at t = 8 its b4 = 1 chart is exactly
   the OPEN[B4-GLOBAL] chart Card A also timed out on.
2. Z-type pairs (J = c(γ−π), Jacobian line through the SIMPLE place [1:1]) are irrelevant to JC2
   unless some Prop 6.3/6.4 descent produces a datum whose Jacobian line passes through the simple
   place at infinity. It does not: Prop 6.3(3) gives J_{γ,π} = −(u_s/b)·γ^{v_s−u_s−1}, the line
   γ = 0 through the point [0:1], never through a place of the pair (the places are π-roots of the
   top form of h, which is monic in π). So OPEN[K16-Z-TYPE-RECEIVER] (my Card C §7.4) closes
   NEGATIVE by source: **no receiver datum is z-type**, and Z-EMPTY has no JC2 content.

Therefore (V0) is over-strong exactly by a JC2-irrelevant conjunct, and a dim > 0 at some t ≥ 8
would mean "a z-type family exists", not "the ray survives". The uniform statement the campaign
needs from the ray is **(8.1) alone: τ_t ∈ √I_{t,+}, i.e. every nonzero cone point has τ_t = 0**,
equivalently no chart pair with J = cγ exists — which is (T)_t, the receiver-emptiness statement
at k = 1, and cannot be easier than itself.

### 1.3 Sharpest provable statement (typed)

```text
PROVED (Opus 12:03Z, consumed): for every t >= 3, J_t^tail = (T_{t,2t-1}, G_1..G_{t-1}) with
  G_r b3-linear of weight 2t+2+r; hsop <=> dim M_t/(G) = 0; length then = 2 binom(3t+1,t-1).
PROVED-IMPOSSIBLE: Froberg / Bezout / coprime-leader routes (DEGREE-BLIND, NO-COPRIME-LEADERS).
OPEN (typed, this submission): OPEN[K16-RANK-CURVE] — criterion RANK clause (ii): on the
  rank-<=1 curve of N = (C_r,B_r) in Spec P_t, some W_r is nonzero.  QUANTITY: the number of
  irreducible components of {rank N <= 1} on which all W_r vanish, to be shown = 0 for every
  t >= 3 (it is >= 1 at t = 2, y = 1/5).  Cheapest test: at t = 3, 4 exact, compute the
  rank-<=1 locus (2x2 minors of N, t-1 choose 2 of them) and its dimension: if it is NOT a curve
  (dim 0 or empty) at small t the "curve" picture is already wrong and RANK degenerates to (i).
  ~5 min, Singular, box/k16hsop-20260903 rows.
```

### 1.4 The one cheap probe worth running before stopping all-t K16 work

(8.1) holds at t = 2, y = 1/5 while (V0) fails — so there τ_2^N ∈ I_{2,+} holds by an
IDENTITY, not by dimension. That fibre is the only place where the shape of a τ-membership
certificate can be read off without a Gröbner basis hiding it: compute the minimal N with
τ_2^N ∈ I_{2,+} on y = 1/5 and the cofactors (lift), then the same at t = 3, 4 exact (where the
cone is {0} and N exists trivially). If N and the cofactor weights follow a pattern
(e.g. N = 2t+2 matching the measured b4-exponent 2t+2 of in_wp), that is the first candidate for a
uniform syzygy-type proof of (8.1) — the only Gröbner-free route left that targets the
JC2-relevant statement. Cost: minutes (`lift`/`division` in Singular on the banked exact rows,
`box/k16toptail-20260903/rows_t{3,4}_exact.sing`; t = 2 rows from `terminal_laurent_t2.json`).
Outcomes: pattern → a lane; no pattern (N grows with the spine) → STOP all-t K16 lanes, keep the
ray as a fixed-t instrument (Opus V5/V7), and put the (H2) structural budget on the k = 4 ray (§4).
Typed OPEN[K16-TAU-CERTIFICATE-SHAPE] in §9.

## 2. Q2 — (99,66): case (A), and the literature gaps N1/N2

### 2.1 What case (A) is: the K = 9 member of a ray, not a stray row

Moh p.209 (image read this lane, `box/ideation-20260904T1200Z-fable5/moh_p209-70.png`): for the
first possibility (g_σ a power of a linear polynomial) "the data can be transformed to
n = 27, m = 18, M_2 = 21, V_2 = 8, δ_2 = −1, δ_1 = 0, Jacobian X⁴" and "the above mentioned
method can be used to reduce the number of coefficients to 10". The "above mentioned method" is
the p.208 reduction of (16,12): write g as the h-adic expansion of f^{n/m} (binomial coefficients
C(n/m, j); at (27,18) these are C(3/2, j) = 3/2, 3/8, −1/16, …), then use the order (accuracy)
bounds to force the corrections β₂β₃ = γh + γ*, β₂³ = δh² + δ* with deg_y γ*, δ* < deg h. Two
facts follow that the packet does not state:

* **Case (A) is the K = 9 member of the two-point ray**
  (n', m'; M₂'; V₂'; k) = (3K, 2K; 3K−6; K−1; 4), (δ₂', δ₁') = (−1, 0), u' = 1, e = 3, q = 2,
  whose K = 7 and K = 8 members are the open rows (147,98) → (21,14; 15; 6; 4) and
  (168,112) → (24,16; 18; 7; 4) (17(pp), 17(uu), 17(lll)); the K = 8 member is also the
  D = 108 no-split datum (17(fffff) §5 already lists the three together; the packet's Q2 and its
  D = 108 paragraph are the same question). The banked history of the three is identical: A/B
  slice "kills" (17(pp)), withdrawn as the −c artefact (17(uu)), corrected instrument (17(nnnnn))
  timing out. The coordinator's 12:07Z desk file `box/caseA-20260904/branch_A_drop_minusc_Q.out`
  (written after this lane started; read as data) confirms the sparse A/B chart of case (A)
  without the −c row is NONTRIVIAL (dim 11, raw dim 12): case (A) is open on the sparse chart
  and only the full chart or a theorem can decide it.
* **Moh's 10-coefficient chart is a SUB-chart of the campaign's full D₁ inventory**, by the
  same floor/attainment mechanism 17(ggggg) exposed: his reduction presumes the corrections lie
  in the filtered prefix basis {h-powers with deg_y remainder < deg h}. That is legitimate for
  Moh because he holds the coherent complete system (Prop 6.3's output) and reads Theorem 1.2
  on it; the campaign cannot certify it without OPEN[FULL-ORDER-BASIS]. So "Moh says 10" is not
  evidence that the corrected 130-unknown system is empty — but it IS evidence that the
  necessary rows the corrected instrument lacks (minor/pole rows in the descended coordinate,
  which Moh's accuracy bounds encode) would collapse it to ~10 unknowns.

### 2.2 How to decide case (A): structurally, on the ray, and not by the full-basis Gröbner run

Recommendation: **do not decide (A) by the corrected full-basis system in isolation.** Reasons:
(i) the emitted full systems are 58–256 MB (the K = 8 sibling is 181 MB for 472 rows in 110
unknowns) — the rows themselves are enormous, so any single Gröbner call is hopeless within a
lane budget, on any solver; (ii) the same computation must be repeated at K = 7, 8, 9 and any
later census member; (iii) a K-uniform argument exists in outline in Moh's own p.208–209 method
and the tower has fixed shape (e, q) = (3, 2): P = h³ + a₁h² + a₂h + a₃, Q = h² + b₁h + b₂
(h monic in y of degree K, top form y^{K−1}(y−x)), J(P,Q) = c·x⁴, with only the number of
lower coefficients of h growing with K. Concretely, with h the approximate square root of Q
(Q = h² + β, deg_y β < K):

```text
J(P,Q) = 2h^3 J(a1,h) + 2h^2 J(a2,h) + 2h J(a3,h) + 3h^2 J(h,β) + 2a1 h J(h,β) + h^2 J(a1,β)
         + a2 J(h,β) + h J(a2,β) + J(a3,β)                                            (2.1)
```

and the requirement J = c x⁴ (degree 4, against a generic degree 5K−2) is a triangular h-adic
band system whose top bands are LINEAR in the newest coefficients with unit pivots (the same
injective-band structure as Lemma INJ / the K16 spine) and whose first product rows
(9·A2_2_7·B2_2_7 = 0 is literally the first emitted row at K = 8) are the top-face splittings the
order chart has not resolved. The K-uniform statement to prove is that after the injective
bands are solved, the residual (the analogue of the K16 terminal cone) is a unit ideal for
every K ≥ 4 — Moh's "10 coefficients" is the size of that residual at K = 9. Card A (§6) prices
this; the first lane (§7) builds it at K = 4..7 where the systems are small.

Cheapest test that decides case (A) as a ROW (not the ray): the staged pivot elimination of §3.3
on the K = 9 corrected system (emit with `order_basis_full.py` after adding the row
`(27,18;21;8;k=4)` to its `ROWS` table — a one-line change), branching on product rows, mod
32051 then Q; if the residual is a unit on every branch the row is dead; PROVED-HERE via the
corrected instrument spec of 17(nnnnn). Estimate: minutes if the injective bands do what they do
at (99,66); hours if not (then the ray lane is the only route).

### 2.3 N1 and N2: what a source read can and cannot close

**N2 — closable by one lane.** Two statements: (a) den(δ) ≤ u_s for a split at order δ; (b) for
δ ∈ {4/3, 3/2, 5/3, 7/3}, Xu's ODE (7.1) forces q = p^{13}(π − c), impossible. (a) is the Galois
argument of Moh p.201 (8)–(11) (t̄ → ωt̄, ω an A_{r−1}-th root of unity, permuting the packet;
the necessity dossier §7 already names it); it is a write-up, not a discovery. (b) is four
finite face-ODE computations of the exact shape of the dossier's §4.3 / the minor-split screen
driver (`box/g108minor-20260903/g108_minor_driver.py`, whose CONTROL 2 replays (99,66) and
returns {2 [2,1], 5/2 [1,1,1]} — the four excluded orders are exactly the ones its resonance
rule rejects; the lane's job is to turn the rejection into a sourced proof per order:
(7.1) with deg p = 3, deg q = W·u_s + 1, the resonance r = W·m + 1 has no solution). Estimate:
one lane, ≤ 2 h, no new instrument. With N3/N4 discharged (17(jjjjj)) this makes THEOREM 8.1
unconditional AS A ROW THEOREM for the split branches.

**N1 — not closable by reading.** The dossier §0.3 runs Moh's printed (1)–(13) at (99,66) and
finds EIGHT admissible V-assignments (M₂ ∈ {−22, 22, 55, 77}, u_s ∈ {1,2,3,4}); Moh prints one
and says his program used more (the (75,50) remark). No source page supplies the missing
restrictions. Consequences: (i) THEOREM 8.1 is a theorem about the ROW M = (−66,77,97),
V = (8,8), never about the degrees (99,66), until the other seven rows are killed or screened
out; (ii) the packet's "(99,66) closed at skeleton level" must be read as "closed for Moh's
printed skeleton, split configurations only"; (iii) the paper-grade claim that can be made
today is Moh-relative: "the case Moh left open at his p.209 fourth case, second possibility, does
not occur" (branches B/C), plus (A) once the ray is closed. Cheapest test for N1's practical
content: run the operative screen (POLY_ODE ∧ XU) on the seven other (99,66) V-assignments and
report which survive — if all seven die on the screen, the degree statement needs only the
screen's soundness (banked); if some survive, they are census rows with their own u_s and join
the (H1)/(H2) queue. Minutes with the census driver. Typed OPEN[9966-OTHER-V-ROWS] in §9.

### 2.4 Referee posture after this round

Exposure ranking for the (99,66) dossier, sharpest first: (1) case (A) — open, on the k = 4 ray;
(2) N1 — degree-vs-row scope, cannot be removed, must be stated; (3) N2(b) — four ODE runs;
(4) N2(a) — a written Galois lemma; (5) OPEN[EFFECTIVE-T2-T3-BRIDGE] — an omission, harmless.
None touches the two kills (INNER, 8 and 7 rows, units over Q before localisation — 17(lllll)).

## 3. Q3 — (H1): theorem versus census, and the minimal compute change

### 3.1 Is there ANY uniform theorem route to MINOR-EMPTY? — No, and three lanes now agree on why

The three candidate mechanisms named in Q3 are the same object seen from three sides, and each
has been typed to the same missing statement:

* Schur/Fitting row (Sol 17(ooooo) O4): after the packet-evaluation block is inverted (which the
  discriminant guarantees), emptiness needs the AUGMENTED rows (incidence/pole/Jacobian with
  their inhomogeneous right-hand sides) to generate 1; the right-hand sides depend on the branch
  series, face normalisation, jets and low-tower coefficients — "the final Schur scalar is not
  determined by (d_s, u_s, V_s, δ, weights) alone" (17(lllll) FILTRATION-PAGE-RULE);
* Fitting-ideal / rank-jump: the same statement in determinantal form (Sol §5.1: the bordered
  minor is det(A)·Schur scalar); generic or fibrewise rank is not enough over the parameter ring;
* valuation / Newton polygon at the second point: this is what the incidence + order rows ARE;
  Xu's face ODE admits nondegenerate solutions on every one of the three flagship faces
  (Sol §4.1–4.2: p = π² + bπ − c with any disc; (8.2) at δ = 2; q₁' = −2p³ at δ = 5/2), so the
  valuative data at the second point never kill by themselves — the kill is always the
  interaction with a Jacobian or pole row at a page that varies by datum.

So the uniform theorem would have to be "for every fully specified admissible split datum the
augmented Schur ideal is (1)", which is a census statement wearing a theorem's clothes: its
proof IS the certificate at each datum. The honest typing is the one 17(ooooo) gives; I add only
that the three (H1) certificates' kill orders (0, 0, 1 for the declared opens) already show the
first obstruction page is not a function of the skeleton. **Commit to the census.**

### 3.2 Pricing the census honestly

The (H1) census is the 166 u_s > 1 groups at D ≤ 200 and the leftover two-point 4-tuples. Two
different instruments, two different prices:

* u_s ≥ 2 WITH a split (the (H1) proper): the inner joint chart + incidence compiler. Evidence
  on price: (99,66) both branches 33 s per branch on the clean-room engine after the outer
  bands were demoted to bookkeeping (kills INNER: 8 and 7 rows); D = 108 dies at stage 0 in
  seconds. The compiler is the cost — the incidence block must be generated per partition from
  the shared leader (Xu Cor 7.5's one p(π)); the excess screen of my 0000Z §3.2 (+2 at D = 108,
  −3 at (99,66)) predicts stage-0 deaths for free. Price: a compiler lane (days), then minutes
  per group. Not the order chart: the order chart is the (H2) instrument.
* u_s ≥ 2 WITHOUT a split and every u_s = 1 group (the (H2) census): Prop 6.3/6.4 descent, then
  the corrected order chart — currently 1800 s timeouts on every non-trivial row (17(nnnnn)),
  which is where the "minimal compute change" question actually lives.

### 3.3 The minimal compute change — measured, not guessed

I measured the two timed-out systems this lane (`box/ideation-20260904T1200Z-fable5/`):

```text
system                          rows  unknowns  file    mean row  max row   monomial  rows with raw   unknowns
                                                size    (chars)   (chars)   rows      unit pivot      pivotable
(24,16;18;7;k=4)  D=108 nosplit  472   110    181 MB   385,138   3,197,550   36        136             86 / 110
(25,15;21;2;k=2)  [3]            598   141     58 MB       —         —        11        218            119 / 141
```

("raw unit pivot" = a variable occurring in the row exactly once, in a degree-1 term with a
constant coefficient; `raw_pivot_census.py`, streaming, 1–2 min each.) Two conclusions:

1. **The instrument, not the solver, is the bottleneck.** 329 of 472 rows at (24,16) have more
   than 100 terms and the mean row is 385 KB because the emitter expands J(P,Q) in all 110
   coefficients at once. No term order, no modular+CRT, no targeted saturation fixes a 181 MB
   input; the (25,15) and D = 108 timeouts are input-size timeouts. Better term order / CRT are
   the wrong answers to Q3's last clause.
2. **The systems are nearly triangular by band**: 86 of 110 (resp. 119 of 141) unknowns have
   a unit pivot in the raw rows before any substitution, concentrated at h-powers 2–4
   (24,16: pivot rows 1/13/51/43/28 at h-powers 0–4) — the injective-band structure of
   Lemma INJ and the K16 spine, in the order chart. The 36 monomial rows at (24,16) are the
   unresolved top-face products (first row 9·A2_2_7·B2_2_7); they are case splits, not Gröbner
   work.

The minimal compute change is therefore: **emit band-wise and eliminate band-wise** — solve the
unit pivots in weight order (substituting into the not-yet-emitted bands, never into a 3 MB
expanded row), branch on the monomial rows, and run `std` only on the residual — i.e. transplant
the (99,66) engine's `joint_elimination` (pivot ledger, Q* pivots only, `c`/`T` forbidden) to the
order chart. A negative control on the WRONG implementation was also run: a Singular `subst`
loop over the already-expanded 181 MB / 58 MB ideals (`*_pivot.sing`, cap 540 s, one thread)
did not finish a single pass (exit 124; 3.9 GB and 1.8 GB RSS) — substituting into dense
expanded rows reproduces the slimgb failure, so the change must happen at emission (§8), not
after it. Typed OPEN[STAGED-ORDER-RESIDUAL] in §9 (cheapest test: (25,15) [3] mod 32051 through
a band-wise emitter; the discriminating quantity is the residual's size).

What this buys if it works: every descended row in minutes (the K16 rows already are), the
(H2) census as a batch, Card A's K = 4..7 charts in one lane, and — via the pivot ledger — a
certificate slice per row of the 17(lllll) kind, i.e. paper-grade output by construction.

## 4. Q4 — the single most valuable object; is (H1) ∧ (H2) complete?

### 4.1 The object: the k = 4 ray

```text
R_4 := { (3K, 2K; M2' = 3K−6; V2' = K−1; k = 4) : K >= 4 },  (δ2', δ1') = (−1, 0), u' = 1, e = 3, q = 2,
       descended pair (P, Q) in k[γ,π]^2, π-degrees (3K, 2K), J(P,Q) = c·γ^4, c != 0,
       h := approximate square root of Q, monic of degree K, top form y^{K−1}(y − x).
Members reached today:  K = 7  <- (147,98)      [two-point list, OPEN 17(lll)]
                        K = 8  <- (168,112)     [two-point list, OPEN]  = D = 108 no-split datum (17(fffff))
                        K = 9  <- (189,126)     [two-point list, OPEN]  = (99,66) case (A) (Moh p.209)
```

Why it is the most valuable object on the board: (i) one theorem — "R_4 is receiver-empty for
every K" — closes D = 108 at skeleton level, closes (99,66) case (A) (hence, with N2, Moh's
printed (99,66) row entirely), and kills the three open δ₁' = 0 rows, i.e. every open (H2)
datum below the seven large-stratum rows; (ii) unlike the K16 ray, where the approximate-root
tower itself grows with t (π-degrees (3t+1, 2t+1) in h), R_4 has a tower of FIXED shape — a
(3,2)-pair over one quasi-root h — and only deg h = K grows, so the uniform-in-K analysis is a
single h-adic computation (2.1) with K-indexed coefficient arrays, the same kind of closed
indexed recurrence Sol wrote for K16 but one level shallower; (iii) Moh did K = 9 by hand
(10 coefficients) and the K = 4 shape (16,12) with 17 coefficients and J constant, so the
uniform version is the natural generalisation of the only two hand computations in the source;
(iv) the K16 ray's remaining structural content (criterion RANK, §1) is a non-vanishing along a
curve with no closed form, whereas R_4's analogous residual has never been looked at — it is
the cheaper structural bet by every measure.

What its uniform proof must contain, in the campaign's vocabulary: the order rows at the second
point for u' = 1 (one non-centre root, V₂' = K−1 — the K16-style "one-direction" case whose
prefix tower IS validated, per 17(nnnnn)'s controls: the K16 rows (16,12) and (28,20) are exactly
u' = 1); the Jacobian bands of (2.1) in weight order; the top-face product rows (36 monomial rows
at K = 8, §3.3) resolved by case split; then the residual cone. The δ₁' = 0 stratum's zero-slope
centre-support directions (17(nnnnn)) are the only subtlety and they are uniform in K
(the x-directions x·y^j, j ≤ K−2, plus x).

### 4.2 Is (H1) ∧ (H2) complete as a reduction? Where the framing is right and where it is wrong

As a reduction of the CENSUS: complete, modulo three typed statements, none of which is a new
configuration:

1. den(δ) ≤ u_s at a split (N2(a)) and the ODE elimination at the non-surviving orders (N2(b)) —
   without them the split classification at a given row is a conjecture, and (H1)'s "genuine
   split" strata are not exhaustive;
2. iterated splits (a partition refining below the ceiling v_s/u_s) are COVERED, because the
   first-split joint chart is necessary for every refinement (rows are only added later); the
   packet need not fear a "split then split" third configuration;
3. the no-split alternative descends by Prop 6.3 only under δ*_{s−1} ≥ v_s/u_s, which for u_s ≥ 2
   is exactly "no split below the ceiling" (Moh Prop 6.1 order formula, memory
   [[moh-prop61-minor-Vr]]); Prop 6.4 makes it automatic at u_s = 1. So the dichotomy
   split/no-split is exhaustive at every u_s; what is NOT automatic is Map II — the identification
   of the descended (γ,π)-pair with the ordinary two-point order chart (17(fffff)
   OPEN[ORDINARY-SUPPORT]) — which is an instrument gap of (H2), not a configuration.

As a reduction of PLANE JC2: **not complete, and the missing piece is not a split type.** The
census is the theorem's instance list only if every Keller pair's Moh data land in it. Moh's
printed (1)–(13) are necessary (sourced), so every Keller pair has SOME (1)–(13)-admissible
skeleton — but the campaign's census then applies the operative screen (POLY_ODE ∧ XU), and the
(99,66) example (dossier §0.3) shows (1)–(13) alone leave eight V-assignments at one degree pair.
The "third configuration" the framing has not exhibited is therefore an ordinary census row
that the packet never counted: the seven other (99,66) V-assignments, and in general every
(1)–(13)-admissible group the screen leaves alive. The packet's "JC2 along Moh's line =
(H1) ∧ (H2)" is exactly right as a statement about the census and exactly wrong as the sentence
"(99,66) is closed at skeleton level" when read for the degrees (99,66). The honest paper-grade
sentence is Moh-relative (§2.3).

One more place the framing is wrong: it ranks "the K16 hsop-length identity" as structural
target (i). After 12:03Z the identity is PROVED (CI-SERIES) and its dimension content is
proved NOT to follow from it (DEGREE-BLIND); the target as worded no longer exists. Structural
target (ii) (Z-EMPTY via the linear-form Jacobian) is JC2-irrelevant (§1.2). The K16 ray keeps
its role as the (H2) PROTOTYPE with (T) proved at t ≤ 7; the (H2) FLAGSHIP is R_4.

### 4.3 Counterexample side, stated once

The first honest disproof signal in this program is not a surviving K16 cone point (a z-type
point is JC2-irrelevant; a τ ≠ 0 point is a pair with J = cγ, which must then be lifted through
Prop 6.3's Map II and the outer tower before it means anything) but a SURVIVES verdict on an R_4
chart at some K with the injective bands solved and the residual cone nonempty with a point
whose coefficients satisfy the zero-slope centre-support rows — the analogue of Moh's
p.208–209 hand computation returning a solution. Everything else on the board dies at a
declared necessary chart. Typed: REPRESENTATIVE at most; never FULL_ACTUAL_EXIT; no exit price.

## 5. Disposition vector (changes only) and bottleneck reranking

Rows are APPROACHES.md's master union table (1–46) with the 2026-09-03 and 2026-09-04 overlays.

* Row 1 (GGV corner / monomial-Jacobian receiver, [P,Q] = x^k): **RAISE and RETARGET** — the
  receiver's flagship instance is now the k = 4 ray R_4 (§4.1), not the K16 ray (k = 1); the row's
  engine should be the staged band elimination of §3.3, not the one-shot order chart.
* Row 3 (vertex-gap / strip ODEs): **RAISE** — the N2(b) closure is four face-ODE runs of exactly
  this row's shape (§2.3), and the R_4 top-face product rows are strip-ODE resonances.
* Row 6 (Abhyankar–Moh one-place / Moh's curve): **unchanged** (raised last round; nothing new).
* Row 29 (LND / Gauss–Manin κ(P)): **LOWER back one notch** — I raised it at 0000Z as the only
  non-injectivity invariant candidate for the K16 ray; with criterion RANK now exact and the
  residual identified as a curve non-vanishing in the spine coefficients, an external invariant
  would have to see b_r, c_r; no candidate does. Keep as a reference, not a lane.
* Row 36 (guided CE search): **RETARGET** to the R_4 residual cone at small K (§4.3) — the first
  place a SURVIVES could be honest; the K16 t = 8 b4 = 1 z-chart is dropped (z-type is
  JC2-irrelevant).
* Row 46 (Lean / formal certification): **unchanged** (rigor-only for the certificate slices,
  as at 0000Z).
* Rows 2, 7, 8/9, 20, 25, 26, 32: unchanged. Rows 10–24, 27, 28, 30, 31, 33–35, 37–45: unchanged
  (no new evidence this round).
* Program rows (overlay): (H1) MINOR-EMPTY — **LOWER from "flagship theorem" to "census with a
  priced engine"** (Q3); (H2) — **split**: K16 prototype **LOWER** (fixed-t instrument, (T) at
  t ≤ 7 stands), R_4 **RAISE to flagship**; "(99,66) closed at skeleton level" — **RE-SCOPE** to
  "Moh's printed row, split configurations" until R_4 at K = 9 and N2 close, and typed
  degree-incomplete until the seven other V-assignments are screened (OPEN[9966-OTHER-V-ROWS]).

**Bottlenecks reranked (proof side).** (P1) R_4 uniform receiver-emptiness — closes D = 108,
case (A) and three two-point rows; first lane. (P2) OPEN[FULL-ORDER-BASIS] as a THEOREM for the
u' = 1 stratum (the R_4 stratum): the prefix tower is validated there by the K16 controls
(17(nnnnn)), so the coverage lemma is easiest exactly where it is needed most. (P3) N2 (one
lane) → THEOREM 8.1 unconditional as a row theorem. (P4) the staged pivot engine for order
charts (§3.3, §8) — the instrument without which neither (P1) nor the 166-group census runs in
lane budgets. (P5) the 166-group (H1) census with the incidence compiler — bounded batch, not a
theorem. STOP: all-t K16 lanes after the §1.4 probe; the (H1) uniform-theorem hunt (residue
formula, disc route, Schur row) — three lanes have now typed the same O4 obstruction.

**Disproof side.** (C1) an R_4 SURVIVES at small K (§4.3); (C2) a surviving (1)–(13) V-row at
(99,66) or D = 108 that the screen does not kill and the engines have not visited
(OPEN[9966-OTHER-V-ROWS]); (C3) nothing on the K16 ray — a nonzero cone point is either
z-type (irrelevant) or a (T)-counterexample datum that still owes Map II and the outer tower.

## 6. Idea cards (three)

**CARD A — R_4-UNIFORM (the k = 4 ray as a K-indexed terminal cone).** Target obstruction: D = 108
no-split, (99,66) case (A), three open two-point rows, in one statement (Q2, Q4). Mechanism:
build the corrected full D₁ chart of (3K, 2K; 3K−6; K−1; k = 4) for K = 4, 5, 6, 7 (below and at
the first census member) with `order_basis_full.py` (add four `ROWS` entries), then run the
staged elimination of §3.3 (unit-pivot bands in weight order, case split on monomial rows,
Gröbner only on the residual) and record per K: the number of injective pivots, the residual
cone's generators, their weights, and the kill (unit) or the survivor. Dependencies: the
corrected instrument (17(nnnnn)); the staged engine (Card C below, or the (99,66)
`joint_elimination` transplanted — it exists in `box/g9966band-20260903/band_engine.py` and the
clean-room `box/g9966indep-20260903/indep_engine.py`); the zero-slope centre-support directions
(17(nnnnn)). Cheapest discriminator: K = 4 and K = 5 (systems of a few dozen unknowns) — do the
residual cones have a K-uniform shape (same number of generators, weights an affine function of
K)? Outcomes: (i) uniform shape and unit at K = 4..7 → write the indexed recurrence (the Sol
(2.1)–(2.13) analogue) and prove the residual unit for all K — the ray dies, D = 108 and case
(A) with it; (ii) unit at every K but no visible uniformity → a K-by-K batch (K = 7, 8, 9) closes
the three census rows anyway, at minutes each instead of > 1800 s; (iii) a survivor at some
K → §4.3: the first honest disproof signal of the program; recompose only after Map II.
Stop: any survivor at K ≤ 7 with the zero-slope rows imposed. Expected information gain: highest
on the board — it is the only card that can move two flagship rows and three census rows at once.

**CARD B — N2-CLOSURE (make THEOREM 8.1 unconditional as a row theorem).** Target: the two
literature gaps of the (99,66) dossier. Mechanism: (a) write the Galois lemma den(δ) ≤ u_s from
Moh p.201 (8)–(11) (the A_{r−1}-th root of unity acting on the packet must permute its u_s roots,
so the ramification index of the split order divides u_s); (b) for each δ ∈ {4/3, 3/2, 5/3, 7/3}
run Xu's (7.1) with deg p = 3, deg q = W·u_s + 1 and show the only solutions are
q = p^{13}(π − c)-type, which fail (7.1) — four Singular runs of the size of the dossier's
§4.3, using `box/g108minor-20260903/g108_minor_driver.py`'s face-ODE machinery (its CONTROL 2
already rejects these orders by the resonance rule; the lane turns the rule into a sourced
proof per order). Dependencies: Xu §7.3/§8 (frozen PDF; note the Cor 7.5 display exponent
error, memory [[minor-split-screen-driver]]). Cheapest discriminator: the δ = 7/3 run (the
only order above the Cor 7.5 threshold 9/4 besides 5/2; if the ODE admits a three-root
solution there, Lemma 7.1 is incomplete and (99,66) has a FOURTH configuration). Outcomes: all
four impossible → N2 closed, THEOREM 8.1 unconditional modulo N1 and case (A); δ = 7/3 admits a
solution → a new branch D to chart (same engine as B/C). Stop: none needed (four finite
computations). Information gain: medium-high; it is the cheapest paper-grade step left.

**CARD C — STAGED-ORDER-ENGINE (the minimal compute change, as an instrument).** Target: the
full-basis timeouts on every (H2) order chart (Q3). Mechanism: §3.3 — emit the corrected chart
as rows tagged by (h-power, x-power, y-power) (already in the TSV), order them by weight, run
unit-pivot elimination (a row affine in a variable with a constant coefficient and that
variable absent elsewhere in the row — 218 of 598 raw rows at (25,15) [3], touching 119 of 141
unknowns, measured this lane), re-scan after each substitution with a size cap on fill-in,
branch on monomial rows, and only then call `std` on the residual mod two primes and over Q.
Dependencies: `order_basis_full.py` row TSVs; Singular `subst`/`diff` or the (99,66) engine's
pivot ledger. Cheapest discriminator: (25,15) [3] mod 32051 — does the residual after
elimination finish in < 10 min where slimgb on the raw 598 rows did not in 1800 s? Outcomes:
finishes empty → (25,15) dies (PROVED-HERE, corrected instrument), and the 166-group census is
priced at minutes per row; finishes nonempty → the first honest surviving descended datum;
does not finish → the rows' density (mean 385 KB at (24,16)) must be attacked at emission
(band-wise Jacobian expansion, never the full product), which is the systems upgrade of §8.
Stop: 30 lane-minutes per row without a residual. Information gain: high and cheap; it is a
prerequisite for Card A and for the census.

## 7. Lanes — continue / redesign / stop; the single first lane

**Running lane (receipt only, as instructed).** `k16-hsop-length-allt-opus5-20260903`: receipt
showed `final_status=DONE`, `end_utc=2026-09-04T12:03:36Z` when checked at 12:04Z (its report was
opened only after that). Disposition: **STOP the all-t K16 line after the §1.4 probe** — the lane
delivered three impossibility theorems and an exact residual (criterion RANK) whose scalars are
spine-complete; nothing cheaper than a new invariant remains, and the JC2-relevant statement
((8.1)) is not made easier by any of it. Do not launch a successor "prove RANK for all t" lane.

**The single first lane: `k4-ray-uniform` (Card A).** Adapter: any with Singular; ≤ 150 min.
Steps: (1) add `(12,8;6;3;4)`, `(15,10;9;4;4)`, `(18,12;12;5;4)`, `(21,14;15;6;4)` to
`order_basis_full.py`'s `ROWS`; emit builders and row TSVs (minutes at K ≤ 6); (2) run the
staged elimination (Card C's script or the (99,66) engine) on each, mod 32051 and 32057, then Q
on the residual; (3) tabulate per K: pivots, residual generators and weights, verdict;
(4) if unit at K = 4..7, write the K-indexed residual and attempt the uniform unit
certificate; if a survivor, report the point and its zero-slope rows. Controls: the K16 rows
(16,12; 13; 3; 1) and (28,20; 25; 3; 1) through the same pipeline must return [1]
(banked); the tame automorphism control must survive. Second lane: Card B (N2). Third: Card C as
a standalone instrument if the first lane's step (2) needs it hardened.

## 8. Campaign-systems check — UPGRADE (band-wise chart emission; rotation: reproducibility and instrument cost)

Evidence (measured this lane): the corrected order-chart instrument writes each chart as ONE
Singular ideal whose rows are fully expanded polynomials in all unknowns — 472 rows / 110
unknowns at (24,16) occupy 181 MB (mean 385 KB per row, max 3.2 MB; 329 rows have > 100 terms);
(25,15) [3] is 58 MB for 598 rows. slimgb has no chance on that input in 1800 s, and even a
`subst`-based pivot loop spent its 540 s cap without finishing one pass (§3.3). Yet the same
rows carry 136 (resp. 218) raw unit pivots on 86 of 110 (resp. 119 of 141) unknowns — the
system is nearly triangular by band, exactly like the (99,66) charts the band engine solved in
33 s per branch. The density is an artefact of expanding the Jacobian in every coefficient at
once instead of band by band.

UPGRADE: `order_basis_full.py emit-system --staged` — emit the chart as a list of bands
(h-power, then weight), each band a small ideal in the band's NEW coefficients with the
already-solved ones substituted, and run the pivot/branch scheduler of §3.3 band by band
(the (99,66) `joint_elimination` ledger format, so every pivot is auditable as at
`box/g9966band-20260903/runs/*/stage*.json`). Smallest useful test: (25,15) [3] mod 32051 —
time to a residual and its size, against the 1800 s slimgb timeout; regression control: the
K16 rows (16,12) and (28,20) and the tame automorphism must return the banked verdicts through
the staged path. Regression risk: low (the one-shot path stays available; the staged path adds
a ledger). Mathematical opportunity cost: none — it unblocks Card A, Card C and the census.
Runner-up (recorded, not chosen): the round-trigger autonomy of 0000Z (queued in LIVE STATE,
still not shipped; this round fired on time, so its urgency dropped).

## 9. OPENs raised, FALLACY-v2 check, typed block

OPENS RAISED

- `OPEN[R4-RAY-UNIFORM]` — receiver-emptiness of the k = 4 ray (3K, 2K; 3K−6; K−1; k = 4),
  J = c·γ⁴, for every K ≥ 4. QUANTITY: the dimension of the residual cone after the injective
  bands, to be shown = −1 (unit ideal) for all K ≥ 4; bound the number of monomial-row branches
  by the number of top-face factorisations (≤ 2^{#monomial rows}). Cheapest test: Card A at
  K = 4, 5 (systems of a few dozen unknowns), corrected instrument + staged elimination, mod
  32051/32057 then Q; ≤ 1 lane-hour.
- `OPEN[STAGED-ORDER-RESIDUAL]` — does band-wise emission + unit-pivot elimination reduce the
  corrected (25,15;21;2;k=2) [3] chart to a residual that `std` decides? QUANTITY: the residual's
  number of unknowns ≤ 141 − 119 = 22 predicted from the raw census, and the residual `std` wall
  time ≤ 600 s. Cheapest test: the §8 upgrade's smallest test, mod 32051; ≤ 30 min.
- `OPEN[9966-OTHER-V-ROWS]` — of the eight (1)–(13)-admissible V-assignments at (99,66)
  (dossier §0.3), how many survive the operative screen POLY_ODE ∧ XU? QUANTITY: the count of
  survivors, to be shown = 0 (else each survivor is a census row for (H1)/(H2)). Cheapest test:
  the census driver on the seven non-printed rows; minutes.
- `OPEN[N2-FOUR-ORDERS]` — Xu §8(i)'s elimination of δ ∈ {4/3, 3/2, 5/3, 7/3} at (99,66) and the
  Galois bound den(δ) ≤ u_s. QUANTITY: the number of solutions of the face ODE (7.1) with
  deg p = 3 at each of the four orders, to be shown = 0. Cheapest test: Card B, four Singular
  runs of the size of the dossier's §4.3 (δ = 7/3 first); ≤ 2 lane-hours.
- `OPEN[K16-RANK-CURVE]` — criterion RANK clause (ii) on the K16 tail. QUANTITY: the number of
  components of the rank-≤1 locus of N = (C_r, B_r) on which every W_r vanishes, to be shown
  = 0 for all t ≥ 3 (it is ≥ 1 at t = 2, y = 1/5). Cheapest test: dimension of the 2×2-minor
  locus at t = 3, 4 exact (≤ 5 min, Singular, rows in `box/k16hsop-20260903/`).
- `OPEN[K16-TAU-CERTIFICATE-SHAPE]` — the exponent N and the cofactor weights in τ_t^N ∈ I_{t,+}
  at t = 2 (y = 1/5), 3, 4. QUANTITY: the minimal N, to be compared with the measured b4-exponent
  2t+2 of in_wp(I_{t,+}) (N ≤ 2t+2 or not). Cheapest test: Singular `lift`/`division` on the
  banked exact rows; ≤ 10 min. Outcome decides whether any all-t K16 lane is launched again.
- Closed negative here, not re-raised: `OPEN[K16-Z-TYPE-RECEIVER]` (no Prop 6.3 datum has its
  Jacobian line through a place of the pair; §1.2).

FALLACY-v2. No exit-price assertion (no `charge_basis` line due). Flag/place/series: the K16
places [1:0], [1:1] and the Jacobian lines γ = 0, γ − π = 0 are kept apart (§1.2); the R_4
descent's second point and the ordinary two-point chart are kept apart as Map I / Map II
(§4.2). Per-ray/exit-set charge: none. Carrier/attainment: a SURVIVES on an R_4 chart is typed
REPRESENTATIVE at most (§4.3); the raw-pivot census is a count of AVAILABLE pivots, not a claim
that the residual has 22 or 24 unknowns (fill-in can add and remove pivots) — it is stated as a
prediction to test. Pole/interior: no pole identity used. Floor/attainment: Moh's
10-coefficient chart is treated as a SUB-chart (floor on the campaign's inventory, never an
attainment) until OPEN[FULL-ORDER-BASIS] closes (§2.1); Theorem 1.2 rows are ≥ throughout.
`sat()`: not used; the negative-control preflight used the emitted Rabinowitsch row unchanged
and reports only a timeout. Raw remainder degree: not used. Variable/ring map: the census script
parses the emitter's own TSV (columns source_index|h_power|x_power|y_power|expr) and counts
variable occurrences by name within one row only — no cross-ring identification. Prime
label/derivative: primes in (2.1) are none; `p'`, `q'` in Xu's ODE are d/dπ (stated in the
sources cited). Merge-free/M-descent, target/arrival index: not touched. Nothing here is
promoted; every mathematical claim about the sealed reports is a consumption with its delta or
report cited; the two new structural claims (the R_4 ray identity of the three rows, and
"no receiver datum is z-type") are sourced to 17(fffff) §5 / Moh p.209 and to Prop 6.3(3)
respectively and typed as readings, not theorems.

```text
SUBMISSION   ideation-20260904T1200Z-fable5 (Fable 5), basis bb2a1a78, packet 1ee8e07b (4/4 OK)
Q1           Froberg / triangular / Bezout: PROVED-IMPOSSIBLE (Opus 12:03Z, consumed); residual =
             criterion RANK (curve non-vanishing in spine-complete b_r, c_r); Z-EMPTY is
             JC2-irrelevant (no receiver datum is z-type); target = (8.1) alone; one cheap probe
             (tau-certificate shape) then STOP all-t K16
Q2           case (A) = K = 9 of the k = 4 ray (3K,2K;3K-6;K-1;4) = {(147,98),(168,112)=D108,
             (189,126)=(99,66)A}; decide on the ray, structurally; N2 closable (Card B), N1 not —
             THEOREM 8.1 is a ROW theorem; seven other (99,66) V-rows must be screened
Q3           no uniform (H1) theorem (O4 = the certificate itself); CENSUS with the inner chart +
             compiler; minimal compute change = band-wise emission + unit-pivot elimination
             (measured: 86/110 and 119/141 unknowns raw-pivotable; rows mean 385 KB — the
             instrument, not the solver, times out)
Q4           object = the k = 4 ray R_4; (H1)∧(H2) complete for the CENSUS modulo N2; NOT a
             reduction of plane JC2 without N1 — the third configuration is an unvisited census row
FIRST LANE   k4-ray-uniform (Card A); then N2-closure (Card B); staged engine (Card C) as instrument
SYSTEMS      UPGRADE band-wise chart emission (order_basis_full.py emit-system --staged)
DESK         box/ideation-20260904T1200Z-fable5/{raw_pivot_census.py,*_pivot.sing,*.out,*.err,
             moh_p209-70.png,SHA256SUMS}; Singular 4.3.2 / python3, one core each, all foreground-
             equivalent with timeouts (540 s caps hit on the two Singular negative controls)
```

Reproduction: `python3 box/ideation-20260904T1200Z-fable5/raw_pivot_census.py box/orderbasis-20260903/rows/<row>_full_rows.tsv`
(1–2 min); the Singular negative controls regenerate from the emitted systems by
`sed '/^ideal G=slimgb(I);/,$d' <system>.sing` + `pivot_tail.sing` (they are expected to time out).

Collision scan run at seal time with `python3 ops/open_collision.py --root . <report> | grep -v "ideation-20260904T1200Z-"` (same-round lines filtered in the shell; the scanner's own corpus guard already excludes same-round submissions and unsealed reports). Hits are lexical review candidates, never closures; none names the same object.

## COLLISIONS

status: CANDIDATES

- `OPEN[R4-RAY-UNIFORM]` (report:572): NONE

### OPEN[STAGED-ORDER-RESIDUAL]

- `xmodel/ideation-20260827T0145Z-grok.md:492` — | Unordered standard `T-c1` as a separate chart | **stop** | Scope-hygiene, not a residual; `c1=0` is the `T-c0` overlap. |
- `xmodel/max12-812-order2-unit-k10-localizer-filing-hostile-review-grok-20260827.md:42` — | `k10=0` is one sibling load-timing family rather than two on-family chart residuals | **CONFIRMED** against double-counting `V(k)` and `V(k10)` as two Gate-T residuals; **GAP** as a single unstructured sibling | Complement of unit-`k10...
- `xmodel/max12-912-order3-nu-q8-normalization-jet-review-claude-20260824.md:81` — Checked by replay (frozen + asserts): the Rabin certificate; base-on-fibre; kernel residuals; the seven-row jet solve and residual; evenness/constancy patterns of `nu`, `r8`, `E`; unit certificates for `rho2`, `V2`, `e1` (with inverse), ...

### OPEN[9966-OTHER-V-ROWS]

- `notes.md:290` — - 2026-08-07 night 6: LROOT decided (SHEET6-LROOT.md, UNREVIEWED): lam_root>=1 REFUTED — stronger, lam_root = 0 is FORCED at every case-IV terminal (IV's own hypothesis (0,y) ∉ V_2a = "single root direction" by Def 3.4, so NO branch leav...
- `xmodel/as-fonly-d7-degree10-pointwise-review-grok-20260824.md:68` — **Do not promote this to:** a classification of every remaining next-carry row on the survivor locus; a statement about other associated-top branches; emptiness or nonemptiness of `FONLY_(3,7)(D=7)` or of the full depth-seven locus; all-...
- `xmodel/as-fonly-d7-postd10-d98-f3-corrected-source-review-grok-20260824.md:98` — | 2 | Vertical D9 is the displayed `4 x 9` with global section (5). After the six licensed D8 pivots and coordinates (6), the `7 x 5` core is the displayed Sylvester matrix and the affine column is the exact next AS source column in all ...
- `xmodel/as-fonly-d7-postd10-d98-f3-corrected-source-review-grok-20260824.md:99` — | 3 | After the three D10 pivots `g*c7_0,g*c7_3,g*c7_6`, the `g!=0` system is `17 x 14`, retains all six Frobenius directions as fibre variables, and contains the named terms `2 g fua x^4 y^5` and `g fa x^7 y^2`. Census `918/354294` with...
- `xmodel/as-fonly-d7-q3-q2q1-degree1-influence-review-grok-20260825.md:105` — Tried hard, and failed, to flip the Jacobian orientation; to reduce modulo 3 before exact division by 27 or 81; to make the 91-slot order anything other than `[x^i y^{d-i}]` for `d=0..12`; to make row 8 be `x y^2` or `x^3`; to replace th...
- `xmodel/as-fonly-d7-q3-q2q1-degree1-influence-review-grok-20260825.md:208` — `3 * 81 = 243` branches. Every branch has `row8_nonzero_raw_columns == []` and `consistent == false`. Slot 8 is `[2,1] = x^2 y`. The `/81` matrix SHA-256 is unique per parent (the linear map on inactive coordinates does not depend on the...
- `xmodel/as-fonly-d7-q3-q2q1-gaussian-exclusion-review-grok-20260825.md:97` — Tried hard, and failed, to flip the Jacobian orientation; to reduce modulo 3 before exact division by 27 or 81; to make the 91-slot order anything other than `[x^i y^{d-i}]` for `d=0..12`; to make row 8 be `x y^2` or `x^3`; to replace th...
- `xmodel/as-fonly-d7-q3-q2q1-gaussian-exclusion-review-grok-20260825.md:171` — No certificate contains `left_null_sparse` supported on any row other than 8, and none mixes `[[8,1]]` with `[[8,2]]` on the same parent. Branch 0 matrices (visible at the head of each JSON) have row 8 identically zero; a singleton left-...
- `xmodel/block-descent-a1-rank4-r1-splice-census-hostile-review-gpt55-20260831.md:26` — | `B=B1 union B2`, source tree T2, all components `T211`, row R1 finite stratum | census lines 21-31, parent lines 149-167 | R1 lies in the finite-`T31` Euler stratum; that stratum was confirmed. It is not one of the refuted split rows. ...
- `xmodel/block-descent-a1-rank4-r1-splice-census-hostile-review-gpt55-20260831.md:37` — Thus no F1 arithmetic conclusion is invalid merely because it rests on the refuted split rows. The damage is different: the census is only a conditional minimal-`A2`, `n22=1`, fixed-pairing splice calculation. It is not a licensed exhaus...
- `xmodel/codex-eval-20260812.md:1751` — - 2026-08-07 night 6: LROOT decided (SHEET6-LROOT.md, UNREVIEWED): lam_root>=1 REFUTED — stronger, lam_root = 0 is FORCED at every case-IV terminal (IV's own hypothesis (0,y) ∉ V_2a = "single root direction" by Def 3.4, so NO branch leav...
- `xmodel/codex-eval-20260812.md:3229` — notes.md:290:- 2026-08-07 night 6: LROOT decided (SHEET6-LROOT.md, UNREVIEWED): lam_root>=1 REFUTED — stronger, lam_root = 0 is FORCED at every case-IV terminal (IV's own hypothesis (0,y) ∉ V_2a = "single root direction" by Def 3.4, so N...
- `xmodel/d43-k0-field-certificate-r3-hostile-review-grok46-20260829.md:175` — **B. `RANK432_INDEPENDENCE`.** Completeness is sound. In a field, `r^2=3` has at most 2 roots and each `x^3=c` (c≠0) has 0 or 3; the gate exhibits 18 distinct verified points, hence the complete set. Python builds them as (registered fra...
- `xmodel/grok-67-final.md:6` — Method: line-read of the round-9 claim against `(2.8)–(2.11)` at `sol-normalform.md:316-365`, Lemma CAP-DEN at `TOWER-TD11.md:241-254`, the 145-row expander in `cases/tower_td11.py`, and the filed 11-C packet `L3a1b1n2 + 2 L4a1b2n3`. Ind...
- `xmodel/grok-census-review.md:5` — Claim under review: every configuration of the audited td-11 class-B/C layer (159 instrument-backed rows quotienting a ~2e8 raw route space, each row covering its full chain/word/arrival extension class) is TOWER-DEAD, with emptiness CON...
- `xmodel/grok-td11-block2-review.md:6` — Method: line-read of the three prose claims against `sol-normalform.md` §2.2, `TOWER-TD11.md` §7.4 Lemma CAP-DEN, and the 145-row expander. Independent exact `Fraction` replay of the all-`u_min` census (brute mixed words included), of th...
- `xmodel/ideation-20260827T2137Z-fable5.md:301` — | upper de Rham gates × affine endpoint | composes with licensing | The endpoint `m=22` is itself the first gate row (7-dim cokernel on the artificial `H`). Rows `>=23` require their determinant rows imposed; the live branch-P fixture de...
- `xmodel/k16-t5t6-grok46-20260903.md:127` — 5. Leading coefficients (lex, remaining in the name order above), t=2,3,4 heuristic: each LC is **degree 1 in y**, of the form `N*(a y - b)` with `N in Q*`. There is **no** single polynomial in `t` that equals every LC; the linear forms ...
- `xmodel/max12-812-order2-p0-a-lowcontact-c1-hostile-review-grok-20260826.md:81` — The two compiled `.sing` files become byte-identical after the single substitution `ring R=0` → `ring R=65521`. Both remote freeze checks are byte-identical and report every `FREEZE` row `OK`. Meta `argv` is `Singular -q` on the lane-loc...
- `xmodel/max12-812-order2-square-d1-c2-c8-first-connection-hostile-review-grok-20260826.md:170` — The first polar `k2` monomial is `k2*R` at grade `21+c=29`, coefficient `1/2`. Bare `k2` is ordinary (pole `-1`) at weight 20. Ordinary families through grade 26 include `k6*A` (pole 0, grade 25) and unloaded `A^2` (pole 0, grade 26). Sp...
- `xmodel/max12-812-order2-square-d1-c2-targetfree-c3c7-hostile-review-grok-20260826.md:199` — which is the same `2(12+row)` timing as the frozen CGE3 emitter. The compiled `FullPhi` rows contain the five copies of each of `-sigma^28*(mu2)`, `-sigma^32*(mu4)`, `-sigma^36*(mu6)`, `-sigma^38*(J/4)` and no earlier target. Extraction ...
- `xmodel/max12-812-order2-square-d1-tied-a1r2-cge6-maxpole2-hostile-review-grok-20260826.md:177` — which is the same `2(12+row)` timing as the frozen CGE3 emitter. The compiled `Phi` rows contain `sigma^6*c1` and `sigma^6*c0` (113 and 74 occurrences on the exact-`Q` script) and no `sigma^5*c`. Extraction divides by `σ^{16}`, substitut...
- `xmodel/max12-912-order3-d1-weighted-infinity-exceptional-support-review-grok-20260825.md:88` — with `t^3=s`. This matches: `(i\bmod 3)·wt(t)≡-i\pmod{3}` forces `wt(t)≡2`. The invariant row is `r_ℓ` divided by `t^{2ℓ\bmod 3}`, and the V2 quotient exponents `(0,2,1)` for `ℓ\bmod 3∈{0,1,2}` are exactly those. Every monomial of each t...
- `xmodel/p202-ten-rows-gate-audit-grok46-20260903.md:331` — (census-rebase: 578 rows, weak). Forcing `SQ=0` kills a printed row.
- `xmodel/pi1s4-84-row-kill-opus5-20260901.md:140` — `(8,4)` rows of the ROW-SWEEP census fall out of the same formula: `m=7,5,3` give
- `xmodel/review-dtransition-grok.md:38` — | Typed `X27 -> X25`: 10 band-26 rows, 10 first-occurrence coords, no lower-row change | **CONFIRMED** | census ≠ declared ten; new column support below band 26; undeclared eta at band 26; unit finite-difference mismatch |
- `xmodel/sol-xside-spec.md:753` — \(34+89=123\) rows: Row 30 has nine selected eta components, while each of
- `xmodel/td6-c1-raw-transport-fibres-review-grok-20260824.md:62` — **Promotion.** Accept as `TD6-C1-C0-C3-EMPTY / RAW-TRANSPORT-REBUILT / FULL-FIRST-ROW-POLYNOMIAL-CERTIFICATES / NOT-A-FAMILY-KILL` of the two fibres `C=0` and `C=3` **in this one fixed normalized section**. Bank the adaptive transport ra...
- `xmodel/td6-c1-raw-transport-fibres-review-grok-20260824.md:74` — | 1 | After specializing `C=0` and `C=3` before any elimination, each original 3,602-column two-chart transport system has rank `3470/3602`, zero dependent-row incompatibility, and 132 free parameters. Adaptive selected-minor digests are...
- `xmodel/td6-c1-raw-transport-fibres-review-grok-20260824.md:75` — | 2 | On each independently rebuilt chart the first centered band, compiled from source, is consistent of rank `38/132`. Rank is stable to reverse-row and max-column GE. The min-index echelon is triangular (`pivot = min(row)`), which is ...
- `xmodel/td6-paired-third-band-review-grok-20260824.md:53` — | 2 | Rebuilt 6547-row system over `K` has rank `3508/3602` (94 free, identity block), affine-replays every base row, and after independently compiled `[s^{-1}]J=0` and `[r^1](J-1)=0` has rank `38/94` leaving a consistent 56-dimensional ...

- `OPEN[N2-FOUR-ORDERS]` (report:586): NONE

### OPEN[K16-RANK-CURVE]

- `AUDIT.md:17722` — ## INTEGRATION #17 DELTA (ooooo) (2026-09-04T11:36Z, structural, producer Sol; the disc(p_red) theorem route for MINOR-EMPTY is REFUTED as a mechanism): OPEN[UNIVERSAL-MINOR-EMPTY-DISCRIMINANT] + REFUTED[disc-invertibility ALONE ⇒ incons...
- `AUDIT.md:17726` — - TAIL-SPLIT (uniform t ≥ 3): a₀ = −α_t is a UNIT of A_t, so M_t = S_t/(T_{t,2t−1}) is a FREE graded rank-2 P_t-module on {1, b₃} (P_t = A_t[b₄, q_{2,0..t−1,0}]); J_t^tail = (T_{t,2t−1}, G_1..G_{t−1}) with G_r = a₀T_{t,2t−1−r} − a_r T_{t...
- `AUDIT.md:17730` — - CRITERION RANK (EXACT iff, the reduction): with N the (t−1)×2 matrix of rows (C_r, B_r), V(J_t^tail) = {0} ⟺ (i) V(B_1..B_{t−1}, C_1..C_{t−1}) = {0} AND (ii) every p ≠ 0 with rank N(p) = 1 whose kernel has nonzero first coordinate has ...
- `AUDIT.md:17731` — MEASURED: t = 2 y = 2/5 dim 0 length 14 = L_2 (new); t = 3, 4 both roots of H_t mod 1009 dim 0 vdim 90, 572 (regenerated independently, agree with banked exact); TAIL-SPLIT verified exactly over A_t at t = 2,3,4,5 (a₀ unit, G_r weights, ...
- `notes.md:21060` — ## 2026-09-04T12:05Z EVENT — `k16-hsop-length-allt-opus5` sealed (40KB): MAJOR structural reduction. K16 (V0)-for-all-t ⟺ CRITERION RANK: (i) the b₃-coefficients B_r,C_r have no common zero AND (ii) a non-vanishing of the eliminants W_r ...
- `xmodel/k16-rank-criterion-fable5-20260903.prompt.md:1` — # STRUCTURAL proof lane (continues the 17(ppppp) breakthrough — the K16 ray's (V0)-for-all-t is now EXACTLY CRITERION RANK, a non-vanishing along a curve): prove, uniformly in t ≥ 3, (i) V(B_1..B_{t−1}, C_1..C_{t−1}) = {0} in Spec P_t (t...
- `xmodel/k16-rank-criterion-fable5-20260903.prompt.md:27` — CRITERION RANK PROVED for all t ≥ 3 (⇒ (V0), (8.1), (T) on the ray — write the

- `OPEN[K16-TAU-CERTIFICATE-SHAPE]` (report:594): NONE

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `62082`.
- Body SHA-256:
  `11bbcae1c9b0c3df09725e2bc19b37b07ede2176325b764e3a5352f8e2d6eb4c`.
- Frozen basis: `bb2a1a78491a2c85b4c11ee75803f47f1a43d60f`.
