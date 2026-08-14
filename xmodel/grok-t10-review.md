**VERDICT: SOUND — `(10,15,7,5)@μ0=3` is tower-dead by the same level-1 clash; the depth-1 (H8)-on-one-vertex configuration is a legitimate edge-local instantiation, not a new law; the arrival-superset rider is applied as Risk 4 requires; L-A covers the 18 slack routes (budget-free chain-1 freeze is a corollary of promoted R1.3 + P3, not a new shape); Case B arithmetic replays exactly on both menu gaps; `ν_U=ν_G=7` makes the displayed kill reading-independent and empties the forced-ν book; three rollout-row values re-derived independently match the spine.**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-14.
Target: `TOWER-10-15.md` + `cases/towers/t10_15.json` + the parameterized `cases/tower_check.py`.
Kill under review: the second cell-level tower kill, `(10,15,7,5)@3`, built as an exact-match instantiation of the panel-constant clash apparatus (`TOWER-ROLLOUT.md` arithmetic row). The `(9,15)` kill machinery is triple-reviewed and promoted — **not re-reviewed**. Scope is what is NEW: (1) depth-1 (H8)-on-one-vertex; (2) arrival-superset rider on menu-style variants; (3) L-A carrying 18 slack routes; (4) Case B on gaps `4/7` vs `5/14`, `2/5`; (5) U_7C-mootness; (6) three independent rollout-row spot-checks.
Method: line-read of the three artifacts against `TOWER-ROLLOUT.md` §1–§2 / Risk 4 / U-OB1, `BOOK-OFFAXIS.md` R1.3 / P0–P3 / §11a, `AUDIT.md` H5a / U_7C, design (H7)–(H8), design §2.3 terminal table; `python3 cases/tower_check.py` (exit 0, **937/937** PASS, 17/17 perturbations including the three new `(10,15)` controls); independent exact `Fraction` replay of the displayed spine (every vertex identity, both H8 instances, E5/H5a/H6, all five edges' `N_e/r_f/r_g`, BOOK(2.1), both pole identities), both menu Case B rows, prefix-menu δ at `{G,U,X,(C)}`, L-A as an identity (not a lattice), T1 `C` at U (four sample points) and at G/X (two points), the 47-row terminal table, and the `T_a^&` criterion at G/U/X. No other repo file modified. No git.

---

## Findings (worst first)

### 1. Severity: suggestion — L-A as written is the clean-shape special case of a stronger promoted identity; the checker lattice is tautological. Slack is still covered. The kill stands.

- File: `TOWER-10-15.md:120-124`; `cases/tower_check.py:400-408`; certificate `tower.obstruction.dependencies`
- Claim: the 18 slack routes leave budget residue, but chain-1 stays uncharged by L-A — an `l=1` cell `(ν, n·ν+1)` admits no charged direction because `m·d_q < d_p = ν` is impossible for `m ≥ 1` (machine-checked lattice).
- How checked.

  **The written form assumes the clean shape `d_p = ν`.** That is the cell you already have after a clean `l=1` arrival from the pole. A hostile reader asks: what if extras are already present, so `d_p = ν(1+Σ m_j) > ν`, and a further NE orbit fits `m·d_q < d_p`? The finite checker does not close this:

  ```
  all(not (m * (n * nu + 1) < nu)
      for m in range(1, 6) for n in range(1, 6) for nu in range(2, 30))
  ```

  This does not read the certificate, does not mention `ε`, and does not induct from the pole. It is a constant that always passes. The lattice is also strictly weaker than the identity: the surplus `m(nν+1) − ν` is at least `1` for every `m,n ≥ 1`, `ν ≥ 2` (checked on a `20×20×80` box; the minimum is exactly `1`, attained at `(m,n,ν)=(1,1,2)`).

  **The budget-free claim is nevertheless a corollary of promoted facts, and it does cover slack.**

  1. P3 (promoted): chain 1 is frozen at `(μ, w, M) = (1, 2, 1)`. St 8.4 forces every subsequent arriving multiplicity to divide `M = 1`, hence `l = 1` all the way to G. Slack residue on the *terminal* side cannot raise this `M`.
  2. R1.3 (promoted), μ=1 clause: “For μ=1 arrivals no dirty vertex exists (`d_q > d_p` makes every root searrow).” Charged = non-clean (P0: NE extras or `ε`; every non-clean step costs `λ ≥ 1`).
  3. Shape, without assuming `d_p = ν`. Own searrow is `E = l·d_q − d_p > 0`. At `l=1` this is `d_p < d_q`. An NE extra needs `m·d_q < d_p`. Combined: `m·d_q < d_p < d_q`, hence `m < 1`. Same for `ε`. This is the rollout’s own L-A sentence (`TOWER-ROLLOUT.md:64-72`) and is strictly stronger than the clean-shape lattice in the probe writeup.
  4. Induction from the pole: P1 is reduced type `(2,3)`, `M=1`. The first chain-1 vertex therefore arrives clean `l=1`, cannot accept extras, stays `M=1`. Every subsequent vertex is the same. Clean `n ≥ 2` steps are `λ = 0` (P0) so they do not spend slack; they drop `w` below 2 with no return (`Δ − n = (n−1)(ν−1) ≥ 1`, already promoted). The merge handshake pins chain-1 arrival at `w=2`.

  Slack leftover can only buy a `λ ≥ 1` step. On chain 1 that step is shape-impossible. Therefore the 18 slack routes do **not** reopen a charged chain-1 family, and the `(9,15)` “budget saturation” door (§6 item 4) is redundant here exactly as the rollout predicted.

  **Erratum to write (cosmetic, not load-bearing).** Replace the clean-shape lattice sentence by the searrow+NE form, cite R1.3 + P3 explicitly, and either drop the finite lattice or keep it as an instantiation of the identity `m(nν+1) − ν ≥ 1`. U-OB1 for the uniform theorem can be discharged as “L-A = R1.3(μ=1) + P3, budget-free.”

### 2. Severity: suggestion — menu-style C3-V does not lock `first_charged_gaps` to the variant gap set

- File: `cases/tower_check.py:721-735, 763-800`; certificate `tower.first_charged_gaps`, `variants`
- Claim: both menu gaps `5/14` and `2/5` enter Case B.
- How checked. Case B loops over `tower.first_charged_gaps`. The menu-style variant loop checks each variant’s own `gap = d_q/(i d_p) < 1/2` and prefix-δ, then returns early. Nothing asserts

  ```
  set(variant gaps) == set(first_charged_gaps).
  ```

  The filed certificate is consistent (`["5/14","2/5"]` matches variants A/C). The new perturbation drops *both* the `(C)` variant *and* its Case-B gap together, so it does not catch a desync. A tampered cert with `first_charged_gaps = ["2/5"]` and both variants still present would pass C3 and skip the `5/14` Case-B row.

  This is a checker-hygiene gap on the *new* two-gap parameterization, not a hole in the filed kill: both identities are true independently (`ν = −7/2` and `ν = −5`, see Finding 6) and both rows are present in the certificate that was actually checked. Fix: one set-equality check in the menu-style branch. The UNIVERSAL Case-B block still only carries the inherited `2/5` identity `5(ν+1)−4ν = ν+5 ≥ 7`; the `5/14` identity `14(ν+1)−10ν = 4ν+14 ≥ 22` lives only in the per-cert loop. Harmless given Finding 6, but the new gap should sit in the UNIVERSAL block the same way.

### 3. Severity: nit — “H8 twice on U” is two edges, not two values of `deg p_{f,U}`

- File: `TOWER-10-15.md:59-60, 147-148`; certificate `obstruction.statement`
- Claim: “`(H8)` twice on U (`deg p_{f,U} = i_G·μ0 = 42` and `deg p_{f,P2} = i_U·2 = 4`).”
- How checked. Design (H8) is the edge-local identity `deg p^{full}_{f,U} = i_L μ_e`. The two instances are

  | edge | L → U | μ_e | i_L | H8 reads |
  |---|---|---:|---:|---|
  | G → U (III-E5) | G → U | 3 = μ0 | 14 | `deg p_{f,U} = 42` |
  | U → P2 (II) | U → P2 | 2 | 2 | `deg p_{f,P2} = 4` |

  The second equality is `deg p_{f,P2}`, not a second evaluation of `deg p_{f,U}`. A reader who took “twice on U” as two constraints on the same degree would invent a clash that is not there. Both instances close (independent replay below). The depth-1 novelty is configurational — U is the unique vertex incident to both edges — not a new hypothesis of St 3.17 / (L1). Wording only.

### 4. Severity: nit — “this cell’s kill does not consume H5a” is slightly stronger than the arithmetic

- File: `TOWER-10-15.md:29-31, 131-143`
- Claim: `ν_U = ν_G = 7` ⇒ every case-III transport is identical under Q-value and forced-ν, so the kill does not consume H5a; U_7C is moot for td-7 at this tier.
- How checked. The *clash* (gaps, `k | 2`, window, A/B/C) is reading-independent on the displayed realization because the two coherent H5a readings produce the same numbers when `ν_U = ν_G` (H6 vs the BOOK/px5 mixed pin coincide; `κ_G = ν_G κ_U / ν_U` collapses to `κ_G = κ_U = 7`). The *spine C1 block* still *uses* the E5/H5a formulas; they happen to be the forced-ν formulas too. Realizations with `ν_U ≠ 7` (neutral `ν ≡ 2 (mod 3)`, some `(C)`-first arrivals) exist only in the Q-value book and *do* consume H5a — they are simply absent from the forced-ν book, so they are not needed for U_7C-mootness.

  The parenthetical in §3 (“the other 15 Q-value cells remain ARITH-DEAD-PREDICTED only”) saves the scope. U_7C still decides whether those 15 exist at all; they are outside this probe’s certified residue. At the *tower tier*, the only certified cells of either book are the two forced-ν members, both dead. That is the correct mootness claim. Soften “does not consume H5a” to “does not *choose* a coherent H5a reading.”

### 5. Severity: clear — Attack (1) fails. Depth-1 (H8)-on-one-vertex is a legitimate use of the printed edge-local identity

- File: `TOWER-10-15.md:35-45, 59-60`; design `xmodel/sol-gluing-design.md:452-470`; `cases/tower_check.py:308-312`
- Claim: U is simultaneously first-charged, arrival, and P2-adjacent; (H8) may be read on both incident edges.
- How checked.

  **Hypotheses of (H8).** Design: St 3.17 supplies (H7) `deg p_{h,U} = mult(p_{h,L}, c_e)` for `h = f−a` across a composite vertex edge; (L1) rewrites this as (H8) `deg p^{full}_{f,U} = i_L μ_e`. The only merge-level extra is “all incoming values in (H8) must give the same `i_G`.” None of these mention chain depth, or forbid the child of the merge from being pole-adjacent.

  **Two distinct edges, no circularity.** `i_G = deg p_{f,G}/d_{p,G} = 140/10 = 14` is read from the merge pattern (terminal `k_f = 140` on this arrival, or equivalently from the chain-1 H8 `deg p_{f,X} = i_G · 1 = 14`). Then H8 on G→U gives `deg p_{f,U} = 14·3 = 42`. Then `i_U = 42/21 = 2`. Then H8 on U→P2 gives `deg p_{f,P2} = 2·2 = 4`, which is the *entry* fact `deg p_{f,P2} = 4` (G1 / Risk 6: this `2` is the pole multiplicity, **not** μ0=3). The i-sync at G from the two poleward edges:

  ```
  deg p_{f,X} / μ_{G→X} = 14/1 = 14,
  deg p_{f,U} / μ_{G→U} = 42/3 = 14.
  ```

  **The checker does not special-case depth-1.** The same `U["deg_p_f"] == L["i"] * μ_e` line runs on both edges and both pass. That is the right test: if depth-1 needed a new hypothesis, the inherited formula would have had to change.

  **Cap carrier is still `k | 2`, not `k | 4`.** Hostile attempt: when U is P2-adjacent, the full pattern is `p_{f,U} = S[(t−A)²(t−B)]²` so `(t−A)` has exponent 4, and Case A at `ν_X = 2` has `k_1 = 4`, which would pass a `k | 4` cap. This fails. Prop 8.1’s load-bearing integrality is `i ℓ/k ∈ ℕ` at `i_U = 2` (the simple reduced factor `(t−B)`), hence `k | 2`. The exponent-4 factor is `i` times the reduced A-mult, matching `deg p_{f,P2} = 4`; it is the weaker constraint. N3’s joint cap `gcd(4, 2P_{pre}) = 2` for odd `P_{pre}` (here `P_{pre} = 1`) restores `k | 2` even under pre-U insertions. Displayed product is 7, so `ν_X | 7` never hits the `ν_X = 2` corner anyway; universality still needs the `k | 2` cap for even products under insertions.

  **`T_a^&` still holds at U**, so St 8.3 / Cor 6.1 apply on U→P2:

  ```
  (1−π) deg p_f / d_f  =  15 (G),  15 (U),  8 (X)   all > 1.
  ```

  U is not a pole. Being P2-adjacent does not eject it from `T_a^& ∩ V_a \ {(0,y)}`.

  **P2 handoff is the same algebra as F1→P2 on `(9,15)`**, just with no intermediate chain-2 vertices: dead member `η(t−A)³(t−B)²` has `mult(·, c) = 3 = deg p_{h1,P2}` at two sample points (checker + independent `k = i(α_1−1) = 1`).

  Hypothesis use is legitimate. The novelty is that both H8 instances touch one vertex; the law is unchanged.

### 6. Severity: clear — Attack (4) fails. Case B arithmetic on `gap(X)=4/7` vs `{5/14, 2/5}` is exact

- File: `TOWER-10-15.md:80-96`; `cases/tower_check.py:721-735`; certificate `tower.first_charged_gaps`, `variants`
- How checked. Independent `Fraction` replay, not the checker’s output.

  Menu gaps from the P2 handoff `deg p_f = 4` and `i = 4/l = 2`:

  ```
  (A)=(21,15):  gap = 15/(2·21) = 15/42 = 5/14,
  (C)=(20,16):  gap = 16/(2·20) = 16/40 = 2/5.
  ```

  Displayed `gap(X) = (7+1)/(2·7) = 4/7`. Comparisons:

  ```
  4/7 = 8/14 > 5/14,
  4/7 = 20/35 > 14/35 = 2/5,
  4/7 > 1/2 > 2/5 > 5/14.
  ```

  Case B (first-charged dies first) needs `gap(X) =` fc-gap, i.e. `(ν+1)/(2ν) = g`:

  ```
  g = 5/14:  ν = 1/(2g−1) = −7/2.   Identity 14(ν+1)−10ν = 4ν+14 ≥ 22 ≠ 0.
  g = 2/5:   ν = 1/(2g−1) = −5.     Identity  5(ν+1)− 4ν =  ν+ 5 ≥  7 ≠ 0.
  ```

  No `ν ≥ 2`. Equivalently, the level-1 death pair is `ℓ/k = g + 1/2` (`α_1 = 3/2`):

  | fc-gap | `ℓ/k` | `(k,ℓ)` | X-exponent `2ℓ/k` |
  |---|---|---|---|
  | `5/14` | `6/7` | `(7,6)` | `12/7 ∉ ℕ` |
  | `2/5` | `9/10` | `(10,9)` | `9/5 ∉ ℕ` |

  These are exactly the pairs the writeup quotes. Prefix-menu δ at the three pairs `(1,2),(2,3),(2,5)` (gaps `3/2, 1, 2`):

  | vertex | `(D_f, κ̄)` | δ for `g=3/2,1,2` |
  |---|---|---|
  | U (A) | `(14, 5)` | `16, 9, 23` |
  | (C) | `(10, 4)` | `11, 6, 16` |
  | G | `(56, 6)` | `78, 50, 106` |
  | X | `(28, 16)` | `26, 12, 40` |

  All positive integers. Matches the rollout G3 row and the Sol-table `(C)` row (because `(C)` *is* `(9,15)`’s F1). Window `(4/7, 5/2)` contains none of `{5/14, 3/28, 5/2}`. Case A displayed pair is `(14, 15) = (2ν_X, 2ν_X+1)`, refused by `k | 2`.

  Nothing new in the clash algebra except that the first-charged gap is `5/14` on the displayed spine rather than `2/5`. Both sit strictly below `1/2 < gap(X)`.

### 7. Severity: clear — Attack (2) fails. The arrival-superset rider is applied as Risk 4 requires, and this cell’s M=3 filter pins the first-charged menu without U-OB2

- File: `TOWER-10-15.md:98-102`; `TOWER-ROLLOUT.md:353-358`; `cases/tower_check.py:763-800`; certificate `arrival`, `variants[1]`
- Claim: `(C)`-first DAGs and the ν=4 direct list entry / neutral family are covered parametrically (window bound + universal exhaustion), never relied on for realizability.
- How checked.

  **Risk 4, quoted:** a kill may COVER a direct arrival but must never RELY on its realizability; neutral classes close by identity + lattice, not instantiation lists. The certificate’s arrival provenance says exactly that for “the ν=4 direct list entry and the neutral family.” The `(C)` variant record says the same for “deeper arrival vertices.” The menu-style checker instantiates `(C)` only as a first-charged *cell* (gap, BOOK-2.1 from ENTRY, prefix-δ) and does **not** build a `(C)`-first spine or an `i_G`/product ledger for it. That is COVER, not RELY.

  **First-charged menu on *this* cell does not need the unproved absorbing-M lemma (U-OB2).** P0 (promoted) gives a complete one-step menu from ENTRY: `{(A), (C), ε(7,5), pure-b}`. The last two land at `M=1`. Arrival here is `M_U = 3`. `M` is non-increasing (gcd). `M=3` cannot descend from `M=1`. Hence every realization of this cell has first-charged ∈ `{(A),(C)}`. The writeup correctly lists U-OB2 as remaining for the *uniform* theorem, not as a load-bearing citation for this kill.

  **Deeper arrivals cannot escape the window.** `(C)`-first paths have depth ≥ 2, so `deg p_{f,U}` is strictly larger than the displayed 42 and `P = i_G/2` is strictly larger than 7 (empty-stack is the opposite direction). Charged gaps shrink under degree growth. Inserted neutrals: N4, `D_{prev} ≥ 4`, gap `≤ 3/8 < 1/2`. Padding at the arrival state `(2/3, 3)`: `D_{prev} ≥ 42`, gap `= (ν+1)/(42ν) ≤ 3/84 < 2/5`. Trunk / G: `deg p_f ≥ 140` (the *minimum*, displayed; larger realizations only increase it, because `i_G` is pinned from the chain-2 side and `k_f = i_G d_{p,G}`). This cell’s window emptiness is structural, not merely an engine-audit shadow.

  **Neutral family** `ν ≡ 2 (mod 3)` is closed by the C3-N state `(2/3, 3)` lattice (54 samples, every gap `< 2/5` at `D_{prev} ≥ 42`), not by a ν-list. Correct.

  The rider is the right quantifier form. The 16 DAGs are a census probe, not a completeness claim.

### 8. Severity: clear — Attack (5) fails. `ν_U = ν_G = 7` on the displayed realization; the forced-ν book is empty at the tower tier

- File: `TOWER-10-15.md:29-31, 131-143`; `BOOK-OFFAXIS.md:791-802`; `AUDIT.md:687-698`
- Claim: both members of `{(9,15),(10,15)}` are tower-dead in both coherent readings, so U_7C no longer gates any td-7 conclusion at this tier.
- How checked.

  **The book is exactly those two cells.** `BOOK-OFFAXIS.md:793-794`, promoted §11a: under forced `ν_G = ν_U` the book is EXACTLY `(9,15,7,3)@2` and `(10,15,7,5)@3`. `(9,15)` is promoted tower-dead (not re-reviewed). This probe kills `(10,15)`.

  **Displayed numbers coincide.** `ν_U = ν_G = 7` is the filed decoration, not a derived wish:

  ```
  H5a Q-value:  κ_G = ν_G κ_U / ν_U = 7·7/7 = 7 = κ_U,
  E5 (h'):      κ̄_G = (7·5 + 7)/7 = 6,
  E5 (g'):      D_G  = (7·14 + 7·42)/7 = 56,
  H6:           X_G  = 3(6 − 7·2/3) = 3(4/3) = 4,
  mixed pin:    X_G  = 3(6 − ν_U·2/3)  equals H6 iff ν_U = ν_G.
  ```

  One case-III edge (G→U), `n=7`. Congruence `n ≡ −ν_G κ̄_U (mod ν_U)` is `7 ≡ 0 (mod 7)` either way.

  **Forced-ν book vs Q-value book.** Forced-ν realizations of this cell are exactly those with arrival `ν_U = 7` (displayed `(A)`, plus any `(C)`-first path that lands at a `ν=7` vertex — covered by Finding 7, and still `ν_U = ν_G` so transports still coincide). Q-value-only realizations (`ν_U ≠ 7`) are not in the forced-ν book. Killing the displayed spine plus the parametric clash therefore empties the forced-ν book without choosing a reading.

  **Mootness scope is the tower tier.** If U_7C is true, the td-7 book is 2 cells, both tower-dead. If U_7C is false, the book is the 17-cell Q-value list, of which 2 are tower-dead and 15 remain ARITH-DEAD-PREDICTED. U_7C no longer gates a *tower-tier certified* residue; it still gates existence of the 15. That is what §3 says once the parenthetical is included.

### 9. Severity: clear — Attack (6): three rollout-row values re-derived independently; all match the spine and the engine row

- File: `TOWER-ROLLOUT.md:233`; `TOWER-10-15.md:70-76`; certificate `sources.rollout`
- How checked. Computed from the cell tuple `(d_p,d_q,ν_G,M_G,μ0)=(10,15,7,5,3)` and the P2 entry degree 4, without reading the engine output.

  **(i) `κ̄`, `X`, arrival `w_U`.**

  ```
  κ̄ = 2 d_q / (d_q − d_p) = 30/5 = 6,
  X  = κ̄ − 2 = 4,                         (chain-1 handshake, w_X = 2, μ_e = 1)
  H6: 4 = 3(6 − 7 w_U)  ⇒  w_U = 2/3.
  ```

  Displayed arrival `2/3 (2; M3)`: `M = gcd(21,15) = 3`, `μ0 | M`, λ-cost of `(A)` is 2, displayed terminal `ψ=4` has budget `6−4=2` (saturated). Matches.

  **(ii) `min deg p_{f,U} = 42`, `i_G = 14`, `P_min = 7`.**
  First charged step `(A)`, `l=2`: `deg p_{f,U} = 4 · 21 / 2 = 42` (U *is* `(A)` on the direct rec. `ν=7` path). Then `i_G = 42/μ0 = 42/3 = 14`, stack product `P = i_G / deg p_{f,P1} = 14/2 = 7`. Matches the engine witness and the constructed spine (`deg p_{f,U}=42`, `i_G=14`, `chain1_product=7`).

  **(iii) Menu gaps and BOOK-2.1 from ENTRY.** Already in Finding 6: `5/14` and `2/5`. BOOK from the P2 frame `(ρ,κ̄)=(1/2,5)`, `l=2`:

  ```
  (A): n=10,  (1/2+10)/(5+10) = 21/30 = 21/(2·15),
  (C): n= 7,  (1/2+ 7)/(5+ 7) = 15/24 = 20/(2·16).
  ```

  Both match the variant records (`book21_n` 10 and 7) and the displayed U→P2 continuation `n=10`.

  Census parity `47(29)` is not one of the three spot-checks but was re-derived from the certificate table: 1 displayed eq + 28 eq trunk + 5 slack trunk-1 + 13 slack trunk-2 = 47 raw / 29 eq, matching design §2.3 *and* the §11a row, every row’s `j ∈ ℕ*`, `ψ = ⌈1/(1−w)⌉−1`, and `λ = 6−ψ` iff `eq`.

### 10. Severity: clear — Attack (3) remainder: L-A covers slack; the 937-gate suite is green; the displayed spine is internally exact

- File: `cases/tower_check.py`; `cases/towers/t10_15.json`
- How checked.

  **Suite.** `python3 cases/tower_check.py` from the repo root: exit 0, `937` `[PASS]` lines, `0` `[FAIL]`, three certificates `OBSTRUCTED`, 17/17 perturbations caught (the three new ones: U-cell `B=(2/3)A` raises 2 failures; slack trunk-1 `ψ` tamper raises 1; `(C)` variant + Case-B gap dropped raises 1).

  **Spine, independent of the checker’s printout** (every identity re-derived):

  | check | value |
  |---|---|
  | all six non-root `κ̄ = κ(1−π)`, `D_f = κ d_f = ρ deg p_f` | close |
  | G/U/X: `w=(κ̄−ρ)/ν`, `M=gcd`, `i=deg/d_p`, Cor 6.1 `d_q = κ̄ deg/D_f`, `θ = X/κ̄` | close |
  | death gaps `κ̄/D_f` | U `5/14`, G `3/28`, X `4/7`, poles `5/2` |
  | G→U E5 / H5a / H6 / (J4) / (H8) | as Finding 8 |
  | U→P2 BOOK(2.1), `κ_P2=21`, `(J4)` `10/21`, (H8) `4` | close |
  | G→X R2.1-II `n=26`, `κ_X=49`, `(J4)` `26/49`, (H4) `X=4` | close |
  | X→P1 R1.2 `τ=4`, `n=27`, `κ̄_X=16`, `ρ_X=2` | close |
  | R0→G case IV, both pole Prop 4.1 | `5/98`, `5/21` |
  | `K=294=lcm(1,7,49,98,21)`; all five edges `N_e/r_f/r_g` | 42/1764/2646, 140/560/840, 156/2184/3276, 81/162/243, 42/5880/8820 |
  | T1 `C` at U, four points | `21 A²/10` (A ∈ `{5, −3/7, 2, 11/3}`) |
  | T1 `C` at G (`ε=3`) and X | `−7A²/6`, `−7A/8` |

  **Insertions on this cell.** The P2-anchored `(6,4)` example replays: `i_U: 2→6`, `gap(U): 5/14→5/42`, `i_G: 14→42`, product `7→21`, continuation `(3/2+9)/15 = 21/30` with `κ̄_U=5` preserved, joint cap N3 restores `k | 2`. Eligible-state tables are the four states this cell actually has; `(2/3,3)` is the new post-U padding state (`D_{prev}≥42`), replacing `(9,15)`’s deeper chain-2 list. Form is generic, list is cell-correct.

  Wrong-object tripwire (Risk 6) is clean: μ0=3 is used only as an edge multiplicity on G→U; the constants 2 and 4 in `gap(X)` and N3 are pole degrees, and they do *not* equal μ0 on this cell.

---

## What is not claimed

- U-OB2 (absorbing-M lemma, panel-wide) and U-OB3 (parametric closure-wide window lemma) remain for the uniform theorem. This cell does not need them: M=3 plus P0 pins the first-charged menu, and the window is structural (Finding 7).
- The other 15 Q-value cells remain ARITH-DEAD-PREDICTED. This review does not promote them.
- L-A as a *named* lemma can be restated as a one-line corollary of R1.3+P3 (Finding 1). That is a writeup upgrade, not a missing kill ingredient.
- The `(9,15)` three-case exhaustion, N1–N4 identities, and single-ladder reading were not re-opened.

---

## Reproduction

```bash
cd /Users/dc/code/math/jc72108
python3 cases/tower_check.py           # exit 0, 937 PASS, 17 perturbations
# independent replay of Findings 6 and 9 is in this file, not in the checker
```
