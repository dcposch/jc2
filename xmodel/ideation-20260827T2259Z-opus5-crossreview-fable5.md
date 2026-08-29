# Fable5 hostile cross-review — sealed Opus5 `20260827T2259Z` ideation

Reviewer model: **Claude Fable 5 (Anthropic), exact model ID `claude-fable-5`.**
Date: 2026-08-27. Output path:
`xmodel/ideation-20260827T2259Z-opus5-crossreview-fable5.md` — the only file
written in the repository this session (desk scripts staged in `/tmp` and
reproduced verbatim in §13).

Reviewed object: `xmodel/ideation-20260827T2259Z-opus5.md`
(`66735327e17350a2884f73eb593cb30b4a587cd0fb37a12285505565fd67af98`).

## 0. Headline verdicts

| # | Claim | Verdict |
|---|---|---|
| 1 | `NU-LAW` (N1) degree decomposition, all constants and indices | **CONFIRMED** (symbolically re-verified, 41/41 coefficient identities on three fixtures) |
| 2a | (N2) as a receiver-**capacity upper bound** (three-case `R_ν`) | **CONFIRMED — and upgraded**: this review supplies a purely algebraic proof of the `ν≥0` cases Opus5 only asserted |
| 2b | (N2) as an exact dimension theorem for the effective receiver | **not claimed by Opus5, not established**; only the bound is licensed |
| 2c | "realized rank = `min(dim W_{n,d}, R_ν)` generically" | **GAP** — refuted as an exact law at the frozen windows by 2 of 42 entries (P row 35: 1 vs 2; control row 31: 6 vs 7), both disclosed by Opus5; no genericity theorem exists |
| 3 | (C1) unconditional `8 | n+2` polynomiality; rows `m ≡ 4 (mod 8)` dead in all degrees | **CONFIRMED** (proof verified incl. character licensing; desk-verified at `n=6,14` on three fixtures) |
| 4 | `ν = n+2−8d` is the correct source index; mapping to receiver `m = n+22` | **CONFIRMED** (`m−ν = 20+8d ≡ 0 (4)`, `k_m = k_ν`, gauge `H^{5+2d}` transports `V_ν ≅ V_m`) |
| 5 | `u = ps` untwisting; one-class formulation; reconciliation with R8 `(0.2)`/`b→b+2` | **CONFIRMED**; exact reconciliation exhibited; **no unlicensed `[q_n dX]` found** |
| 6a | `GATE-PR` telescoper existence, finite-dim module, X-free coefficients | **CONFIRMED** (self-contained; substantially duplicates R8 Thm 4.1 — blind convergence, hence different-model confirmation of R8) |
| 6b | Certificate-typing valuation lemma (§3.4) | **CONFIRMED** (re-derived independently, incl. the `k<0` Laurent tail and the discriminant-puncture repair) |
| 6c | Pointwise `N_0` decision bound | **CONFIRMED as an algorithm schema** (coarser display of R8 (6.4)); no numerical `N_0` exists — correctly not claimed |
| 6d | Uniformity claims | no overclaim beyond one sloppy phrase ("ρ is uniform" should be "uniformly bounded, pointwise operators"); Noetherian cell rider matches R8 §7.2 |
| 7 | `D_0..D_34` tower ceiling (§3.5) | **CONFIRMED** with precise scoping (set-theoretic domination, one-directional, not a row-34 index cutoff) |
| 8 | Lower-endpoint `∇_{−3}` connection (§9 primary) | **CONFIRMED** (one benign misattribution: `|Z|−1` formula cited out of its `ν≥0` scope; the number is nonetheless correct via `r−1+k_{−3}=1`) |
| 9 | "`H^1_dR(U,∇_ν) × H^1_dR(U,∇_{−ν}) → K` is perfect" (avenue 3 raise / 33 reopen) | **REFUTED AS STATED / REPAIRED-scope** — fails for `4|ν` (cup into `H^2` of an affine curve is 0) and is unproved at every resonant stratum; on the frozen P/Q fixtures `deg H = 8` makes `∞` **always** resonant |
| 10 | Card A `d=2` worked example | **REPAIRED** — arithmetic slip: `n=6, d=2` gives `ν = −8` (not `−10`) and capacity `r−1+k_{−8} = 4` (not `r−1 = 3`) |
| 11 | Card B one-slot discriminator display | **REPAIRED** — `Σ λ(p²y^n dX)z^n = λ(p²dX/(1−yz))` is a true identity about the **wrong series**; the gate series carries weights `c_n = (2/(n+2))C((n+2)/8,n)`, `c_1 = 1/4 ≠ 1` (frozen counterfixture `q_1 = 1/X ≠ 4/X = p²y`) |
| 12 | History check / `NEW` labels | **VERIFIED against the freeze state** (nontrivially: the canonical files were mutated mid-review-session by the post-seal synthesis — §1, §10) |

No custody violation by Opus5 found. The report's §11 ledger and blindness
disclosures are consistent with everything I can check.

## 1. Custody, inputs, and a mid-session mutation event

Session-start custody gate (all recomputed): the `2259Z` packet hash and all
ten section-1 values **matched exactly**, including
`f9ed44df… APPROACHES.md`, `aee767b1… AUDIT.md`, `743d684b… COORDINATION.md`,
`0d22e397… PROGRESS.md`, `654c358e… notes.md`. `HEAD` basis not re-verified
beyond the packet's declaration (no git state was needed for this review).

**Mutation event, fully disclosed.** Later in this same session,
programmatic re-hashing showed `APPROACHES.md`, `AUDIT.md`, and
`COORDINATION.md` **no longer match** the packet
(`a40e01cd…`, `6e4eac0c…`, `19b9c190…`; mtimes 23:35:37Z–23:39:10Z), while
`PROGRESS.md` and `notes.md` still match. The new `APPROACHES.md` carries a
"Superseding strategy overlay (2026-08-27 23:30Z)" stating the 22:59Z round is
sealed and merging adjudicated forms of the very claims under review. This is
the coordinator's licensed post-seal synthesis landing **concurrently with my
review session**; the packet's "will not be mutated until all blind
submissions seal" condition had been met. Consequences:

- Opus5's §0 custody pass is **consistent**: at their session the files were
  at freeze state (my session-start check independently caught the same
  state).
- Opus5's history check (§9), which a naive grep of the *current* files
  appears to refute, is in fact **verified**: see §10.
- I read lines 1–100 of the *mutated* `APPROACHES.md` (including the 23:30Z
  overlay) before recognizing the mutation. Contamination handling in §14.

Files read this session, with SHA-256 at time of reading:

```text
8674f511a6a88801818c7ffda5f1fdfa52ac57e871e72757234a5d0a28291240  xmodel/ideation-20260827T2259Z-packet.md          (full)
d8a01725bc2730ce49069c96f4287956fb867b64e324ea6828076e19986e6b15  xmodel/ideation-20260827T2255Z-packet.md          (full; scope appendix)
66735327e17350a2884f73eb593cb30b4a587cd0fb37a12285505565fd67af98  xmodel/ideation-20260827T2259Z-opus5.md           (full; object of review)
71befadb3496f5f6c8e3136e7019de95dec2f205f2655734eac2c84d8e0e24d1  xmodel/ggv-quarter-root-sector-gate-rec-theorem-r8-sol-ultra-20260827.md  (full)
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md (full; cited baseline, needed for §3.5/§9 adjudication)
7ab758fa002c75cd28d81540e8f63fd8cd0de97fad791afedfeb5fb610c6cb29  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-hostile-review-fable5-20260827.md (grep excerpts only: D35/D34 findings, lines 8–329)
5beb555075c662e76f8b86062efdf89b2c3a4dd0eb80ffd52fbf3c38bf130d55  xmodel/ideation-20260827T2137Z-fable-linear-vacuity-hostile-review-sol-ultra.md (grep excerpts: window dims, control table, corrected E0 language)
668d78c96088d168361874733f81d7dee724769a6177a723bd0561e60ad850d0  xmodel/ideation-20260827T2137Z-synthesis-sol.md   (grep excerpts: Γ_a packaging lines 133–136; residue-pairing lines 160–163)
654c358e7c8760fc93ffeb0cfb0ea4fd62163a338195dccba13db865c2c87038  notes.md (grep only: `telescop` line census — frozen state, still matching)
(freeze state, hash-verified at session start, since mutated)              APPROACHES.md f9ed44df…; AUDIT.md aee767b1…; COORDINATION.md 743d684b…
(mutated state, read/grepped in error or for diagnosis)                    APPROACHES.md a40e01cd… (lines 1–100); AUDIT.md 6e4eac0c… (grep hit headers only)
(hashed only, never read)                                                  PROGRESS.md 0d22e397…; xmodel/ideation-20260827T2137Z-opus5-crossreview-fable5.md b3f3886c…
```

Not touched: `jc2-lean` (never entered, listed, or read), AWS, running jobs,
all peer `2259Z` lane outputs and their hostile reviews (`fable5`, `sol`,
`grok46`, `*-hostile-review-sol-ultra`, `carrier-*`), all canonical files
beyond the reads listed above. No canonical file was edited.

## 2. Task 1 — `NU-LAW` (N1): CONFIRMED

Claim (Opus5 §2.1): with `F = H²(1+g)`, `g = Σ_{i≥1}(F_i/H²)tⁱ`, the promoted
all-row formula `q_n = (2/(n+2))[tⁿ]F^{(n+2)/8}` decomposes as

```text
[q_n]_{F-deg d} = (2/(n+2)) · C((n+2)/8, d) · p^ν · S_{n,d}(X),   ν := n+2−8d,
S_{n,d} = Σ_{i_1+…+i_d=n, i_k≥1} F_{i_1}···F_{i_d}   (ordered compositions).
```

Adjudication:

- The derivation is a two-line binomial rearrangement of the promoted (1.1)
  (`F^{(n+2)/8} = p^{n+2}Σ_d C((n+2)/8,d)g^d`, `[tⁿ]g^d = H^{−2d}S_{n,d}`,
  `H^{−2d} = p^{−8d}`), and I verified it does not smuggle in anything beyond
  (1.1). Conditionality: **N1 is exactly as strong as the promoted Lagrange
  formula (1.1)**, which is different-model confirmed per the 2255Z appendix
  §2.1 and is the "exact algebraic source" of R8 §1. Opus5 states this
  dependency correctly.
- All four of Opus5's hand anchors re-verified against the frozen R7R1 file
  (read in full): `q_0 = p²`, `q_1 = F_1/(4p⁵)`,
  `q_2 = F_2/(4H) − F_1²/(16H³)` are literally R7R1 (0.4); the `d=1` law
  `(1/4)p^{n−6}F_n` matches R8 (1.2) and the 2255Z packet §1; the single-slot
  `q_6 = F_6/4` is immediate (`ν = 0`, no `d ≥ 2` support).
- **Independent symbolic verification** (script 1, §13): series reversion of
  `t = u·(1+g(t))^{1/8}` (`u = ps`) over exact `ℚ(X)` arithmetic versus the
  N1 closed form with `S_{n,d}` computed by direct composition DP — **41/41
  coefficient identities match as rational functions** (not sampled), for
  `n = 0..14` on `H = X²(X−1)` (d=3), `H = (X²−1)²` (d=2), and `n = 0..10` on
  the frozen R7R1 counterfixture `H = X⁴, F = X⁸+4X⁴t` (reproducing the
  frozen anchors `q_0 = X²`, `q_1 = 1/X`).
- Convention audit: constant `2/(n+2)` ✓; generalized binomial `C((n+2)/8,d)`
  (nonzero for all `d` when `8∤n+2`; zero iff `d > (n+2)/8` when `8|n+2`) ✓;
  `ν = n+2−8d` ✓; ordered compositions (no symmetry factor) ✓; window
  truncation `F_i = 0, i ≥ 15` ✓. One display nit: the §2.1 sum is written
  `Σ_{d≥1}`, which drops the `d = 0` term needed for `n = 0` (row 22 — outside
  the tower rows; cosmetic).

**Verdict: CONFIRMED**, conditional only on promoted (1.1).

## 3. Task 2 — (N2): bound CONFIRMED (and now proved), min-law GAP

The task requires distinguishing three different things Opus5's (N2) block
mixes on one line.

### 3.1 The capacity bound `R_ν` — CONFIRMED, with proofs supplied here

Setup verified: the row-`m` condition on the degree-`d` piece is
`∇_m`-exactness of `p^{ν−m}S_{n,d} ∈ A` (well-typed: `4 | ν−m`), equivalently
`[S_{n,d} dX] = 0` in `V_ν` after the integer gauge
`∇_m(H^j f) = H^j∇_{m+4j}(f)`, `j = (ν−m)/4 = −(5+2d)`. Write
`Z_ν = {a_i : 4 ∤ e_iν}`, `z = |Z_ν|`.

- **`ν ≥ 0, Z_ν = ∅ ⇒ R_ν = 0`: proved, purely algebraically.** Here
  `T := Π(X−a_i)^{e_iν/4} ∈ K[X]` and `p^ν/T` is a `d/dX`-constant of `L`
  (equal log-derivatives), i.e. "polynomial up to a harmless constant" exactly
  as the 2255Z packet says. In-complex: for any `S ∈ K[X]`, `g := (∫TS)/T ∈ A`
  satisfies `∇_ν(g) = S` (the `T`-roots lie in `Z(H)`, so `1/T ∈ A`; the
  log-derivative cancellation is exact). Identical vanishing, all fixtures.
- **`ν ≥ 0, Z_ν ≠ ∅ ⇒ R_ν ≤ z−1`: proved, purely algebraically** — Opus5
  asserts this case without proof; the 42-entry regression was their only
  support. Proof: factor `p^ν = (const)·T·M`, `M = Π_{i∈Z_ν}(X−a_i)^{α_i}`,
  `α_i = e_iν/4 ∈ ℚ_{>0}∖ℤ`, `T` polynomial as above; since `T·K[X] ⊆ K[X]`
  it suffices to bound `span{[M·U dX] : U ∈ K[X]}`. Let `M₀ = Π_{i∈Z_ν}(X−a_i)`
  (radical, degree `z`). For `V₂ ∈ K[X]`, the primitive `M·M₀V₂` gives the
  exact form `M·𝒯(V₂)dX` with

  ```text
  𝒯(V₂) = M₀V₂′ + ( M₀′ + Σ_{i∈Z_ν} α_i·M₀/(X−a_i) ) V₂  ∈ K[X],
  deg 𝒯(V₂) = deg V₂ + z − 1,  leading coeff = deg V₂ + z + Σα_i  > 0.
  ```

  The leading coefficient never vanishes (all terms positive), so the image
  of `𝒯` contains monic-normalized elements of **every** degree `≥ z−1`, and
  every `[M·U dX]` reduces to `span{[M·Xⁱ dX] : i ≤ z−2}`: dimension `≤ z−1`.
  (Allowing the full primitive space `A` only shrinks the span; the bound
  stands in `V_m`.) For `z = 1` this gives the complete vanishing Opus5's
  table needs at Q rows where only `Z(B)` branches would remain with `z=1` —
  and the `z−1` count "explains" the frozen Q rows 30/34 rank-1 entries
  (`p² = A·B^{1/2}`, `p⁶ = A³B·B^{1/2}` — both rechecked).
- **Numeric mini-model check in the strict regime** (script 3, §13):
  `H = X²(X−1)(X−2)` (`r = 3`, `e = (2,1,1)`), `ν = 2`: claim `≤ z−1 = 1`
  **strictly below** the full receiver `r−1+k_ν = 2`. Computed span
  overestimate (truncation understates the exact space, hence overstates the
  span — the safe direction): **1** at truncations `K = 8, 12, 16`. Also
  `ν = 1, 3`: overestimate `2 = z−1` ✓; canary `H = X²(X−1)`, `ν = 2`
  (`z = 1`): **0** ✓ matching the algebraic proof.
- **`ν < 0 ⇒ R_ν = r−1+k_ν`: CONFIRMED** as the receiver dimension itself
  (promoted law `dim V_j = r−1+k_j`, R8 (3.3); `k_m = k_ν` since `k` depends
  on the index mod 4 and `m ≡ ν (mod 4)`).

### 3.2 Exact effective-receiver dimension — not claimed, not established

Opus5 writes "lands in, and its image is bounded by" — a bound, correctly.
Whether the polynomial-form image is **exactly** `z−1`-dimensional (for the
full polynomial family) is plausible (my numeric overestimates sit exactly at
`z−1`) but is proved nowhere and is not needed for any promoted use.

### 3.3 The realized-rank line — GAP

"realized rank: `min(dim W_{n,d}, R_ν)` generically" is **not a theorem**,
and the frozen windows — which are the campaign's actual objects — refute it
as an exact law at 2 of 42 entries (recomputed, script 2, §13):

```text
all 42 entries:  bound violations 0 ;  under-min entries exactly 2
  P row 35 (n=13, ν=7):  min(2,3)=2, measured 1
  control row 31 (n=9, ν=3):  min(7,7)=7, measured 6
row sums reproduce the packet:  P 26/27,  Q 35/37  (rows 23–34 / 23–36)
```

Opus5 disclosed both entries ("window-specific degeneracies … flagged as the
residual discrepancy"), which is honest, but "generically" does no licensed
work at a frozen point. **Repair:** state (N2) as
`realized rank ≤ min(dim W_{n,d}, R_ν)`, equality observed in 40/42 frozen
degree-one entries, equality **not** a theorem. Consequence for §5/§8 of the
report: (N2) may replace the harness only for **capacity/dead-row screening**;
realized ranks stay empirical, so the frozen exact-rank harness must be
retained as the decision instrument for nonzero rows (Opus5's own §5 keeps it
as a regression oracle; their §8 "replace" wording is too strong).

## 4. Task 3 — (C1) unconditional mod-8 row death: CONFIRMED

Theorem as stated: if `8 | n+2` then `q_n ∈ K[X]` for every `H` and every
`F`, and row `m = n+22 ≡ 4 (mod 8)` is identically vacuous in all `F`-degrees
(`m = 28, 36, 44, …`).

- One-line proof valid: `(n+2)/8 ∈ ℤ_{>0}` makes `F^{(n+2)/8} ∈ K[X][t]`.
- **Character licensing verified** (the "licensed gauge/sector shift" of the
  task): `8 | n+2 ⇒ m ≡ 4 (mod 8) ⇒ 4 | m`, so `p^{−m} = H^{−m/4} ∈ A` and
  `g := H^{−m/4}∫q_n ∈ A` satisfies `∇_m(g) = p^{−m}q_n` — the polynomial
  primitive lands in the correct character sector precisely because `4 | m`.
  (Conversely, for `4 ∤ m` a nonzero polynomial `q_n` could never satisfy the
  sector constraint `q_n ∈ p^{n+2}A` at all — consistency, not an extra
  assumption.) N1-consistency also verified: `C((n+2)/8,d) = 0` for
  `d > (n+2)/8`, and surviving `d` have `ν = 8((n+2)/8−d) ≥ 0` with `4|ν`.
- Desk-verified (script 1): `q_6` and `q_14` are exact polynomials on all
  three test fixtures, including mixed-multiplicity and counterfixture data.
- Receiver-side invisibility remark verified: `4|m ⇒ k_m = 1` ⇒ these rows
  have **full** receiver `r`; the death is source-side. Correct and the §10
  "period is 8, not 4" insight stands.
- One scoping nit: "strictly stronger than E0's `k_m = 1` statement" is true
  **on the `m ≡ 4 (mod 8)` rows** (all degrees vs degree-one). E0 additionally
  kills other `k_m=1` rows at `d=1` (e.g. P rows 30/34), which (C1) does not
  touch; neither statement implies the other in full. Read as row-scoped, the
  sentence is right.

## 5. Task 4 — the `ν` index and its receiver mapping: CONFIRMED

- `ν = n+2−8d ≡ n+2 ≡ m (mod 4)` (`m−ν = 20+8d`); the degree-`d` piece
  transports to `V_ν` by the **integer** gauge `H^{(m−ν)/4} = H^{5+2d}`;
  `k_m = k_ν`. In R8's sector language: coefficient sector `b = n mod 4`,
  receiver sector `m ≡ b+2 (mod 4)` — Opus5's `ν` satisfies
  `ν ≡ b+2 (mod 4)`, i.e. the same `b → b+2` shift, automatically.
- (C2) verified on the tables: `4|ν` rows (28/32/36; `ν = 0,4,8`) die at
  `d=1` on **all three** fixtures (unconditional in `H`); `Z_ν = ∅` with
  `4∤ν` (P rows 30/34, `ν = 2,6`) is fixture-dependent — dead on P, rank
  `z−1 = 1` on Q, alive (rank 7/3) on the squarefree control. The promoted
  `k_m = 1` hypothesis conflates these two mechanisms exactly as claimed.
- (C3) verified as a capacity statement (`ν ≥ 0` pieces all dead when
  `(n+2) mod 4` forces `4|ν`, leaving only `d > (n+2)/8`); the word "exactly"
  in Card A's `d=2` prose should be read as "provably vanishes there"
  (vanishing elsewhere is not excluded by capacity).

## 6. Task 5 — `u = ps` untwisting and the one-class formulation: CONFIRMED

- Algebra verified: `σ(u) = u`; `q̂_n = q_n/p^{n+2} ∈ A` by R8 (1.2);
  `G = Q/p² = Σ q̂_n uⁿ` has all-rational coefficients; `H²R⁸ = F(X, uR)`
  follows from R8 (1.3) with `t = uR`. The reversion in my script 1 is
  literally computed in this normal form (`t ∈ ℚ(X)[[u]]`), which is itself a
  desk demonstration that the untwisting works.
- **Exact reconciliation with R8 (task requirement).** R8's normalized class
  series is `Σ_k [p^{−(b+22)}q_{b+4k}dX]z^k` in `V_{b+22}` (0.2)/(3.7), where
  the `H^k` gauge disappears because `H^k p^{−4k} = 1` on the torsor. The
  Kummer identification (R8 (3.2)) is multiplication by `p^{m₀}`,
  `m₀ = b+22`, onto the `(b+2 mod 4)`-character part of `H¹_dR(V_H)`; it maps
  `[p^{−(b+22)}q_{b+4k}dX] ↦ [q_{b+4k}dX]`. Hence Opus5's
  `c_n = λ(q_n dX)` **is** R8's normalized gate class, transported to the
  cover, with the sector shift `b → b+2` carried automatically by the form's
  own character. No discrepancy of any kind; the two packagings are the same
  object.
- **Unlicensed-`[q_n dX]` scan (task requirement): none found.** Every class
  in the report carries its exact `p`-power inside the form: §2.2 uses
  `p^ν S_{n,d} dX`; §3.2/§7 use the physical `q_n dX` on the full cover
  `V_H`, where no gauge is needed; §3.1 divides by the exact `p^{n+2}`. The
  trap R8 (0.2) warns about — treating `Σ H^k q_{b+4k}z^k` as the gate
  transport, i.e. multiplying by a nonconstant `p`-power and calling it
  harmless — does not occur. Opus5's stronger rhetorical claim that in the
  `u`-normal form the trap "cannot arise" is fair in substance: the licensed
  bookkeeping is automatic there because the `p`-power is part of the object.
- Auxiliary checks: `q_n ∈ O(V_H)` ✓ (from `q_n ∈ p^{n+2}A`); the
  primitive-typing remark ✓ (valuation argument, unramified off
  `Z(H) ∪ ∞`); `b₁ = 4(r−1)+c` values `14/17/4/29` and `3b₁ = 42/51/12/87`
  recomputed ✓ (script 2; "one-root" = single root of multiplicity 4, where
  `c = 4`, matching the frozen R7R1 counterfixture `H = X⁴`). Disconnected-P
  reading is covered by R8 §1/(3.3) (component selection; no connectedness
  needed).

**One repair in this area — Card B's discriminator display (headline #11).**
The one-slot collapse `q̂_n = (2/(n+2))C((n+2)/8,n)(F_1/H²)ⁿ` is correct
(verified in closed form and numerically on the counterfixture). But the
displayed series `Σ_n λ(p² yⁿ dX) zⁿ = λ(p² dX/(1−yz))`, `y = pF_1/H²`, is
**not the gate series**: `q_n = c_n·p²yⁿ` with
`c_n = (2/(n+2))C((n+2)/8,n)` and `c_1 = 1/4 ≠ 1`. On the frozen R7R1
counterfixture the displayed series' `n=1` coefficient is `p²y = 4/X` while
the true `q_1 = 1/X`. The frozen algebra `(Q⁴−X⁸)² = 16X⁸s²Q` also shows `Q`
is algebraic of degree 8, not rational as the geometric kernel would make it.
**Repair that preserves the card:** the gate series is the Hadamard product
of the displayed rational-kernel series with the hypergeometric (P-recursive)
scalar sequence `c_n`; both factors are D-finite, so the discriminator
survives with the weights restored. The "fixed curve, moving pole divisor,
Griffiths–Dwork" framing applies to the repaired object, not the displayed
one.

## 7. Task 6 — `GATE-PR`: existence, module, typing, `N_0`, uniformity

- **Telescoper existence (§3.3): CONFIRMED.** `𝒪` (invert `H` **and the
  `P`-discriminant**) is stable under both derivations — inverting the
  discriminant is what makes `∂_s𝒪 ⊆ 𝒪`, and Opus5 does it; `𝒪 dX/d𝒪` is
  `H¹_dR` of a smooth affine curve over `K(s)`, finite-dimensional; among
  `ρ+1` classes `[∂_s^k Q dX]` there is a `K(s)`-dependence; clearing
  denominators gives (T) with `ℓ_k ∈ K[s]`, **free of `X`**. Self-contained;
  no literature needed for existence. `ρ ≤ dim_{K(s)}(𝒪dX/d𝒪)` ✓.
- **Typing lemma (§3.4): CONFIRMED** — re-derived independently. `C ∈ N ⊂
  L((s))` makes `C_k ∈ L` automatic (no trace descent needed — cleaner than
  R8 (4.3)–(4.4), which achieves the same by trace + pole-regularity); for
  `k < 0`, `∂_X C_k = 0` forces `d/dX`-constants (harmless); for `k ≥ 0`, at
  unramified places off `Z(H) ∪ ∞`, `v(C_k) = −a < 0` would force
  `v(∂_X C_k) = −a−1 < 0` against `∂_X C_k ∈ O(V_H)` — so `C_k ∈ O(V_H)`.
  This simultaneously repairs the certificate's a-priori discriminant-locus
  poles (allowed in `𝒪`, excluded in the conclusion). With `ℓ_k` `X`-free,
  `λ` commutes coefficientwise and `Σℓ_k(s)c^{(k)}(s) = 0` follows exactly;
  coefficient extraction gives the P-recurrence with `a_j ∈ K[n]`. **This is
  a valid answer to the 2137Z objection**, as claimed.
- **Pointwise `N_0` (§3.4 end): CONFIRMED as a schema.** It is a coarser
  display of R8 §6 (largest shift with nonzero `A_ℓ`, its last nonnegative
  integer root, plus the shift; startup indices). No numerical `N_0` exists;
  neither text claims one.
- **Uniformity (task: "any unsupported uniformity/order claim").** Findings:
  (i) "Order is uniformly bounded by the degree data, so `ρ` is uniform over
  the 124-slot window" — the *bound* is uniform (degree data are; the 124
  count itself re-verified against the frozen window dims
  `16,15,14,13,12,11,10,9,7,6,5,3,2,1`), but the operators are per-point and
  the minimal order can vary; the phrase should read "uniformly bounded".
  Not load-bearing. (ii) The uniform-`N_0`-by-Noetherian-stratification rider
  is stated as existence-only with an unbounded stratum count — this matches
  R8 §7.2 exactly (including R8's sharper `A(N,θ) = N−θ` warning that generic
  nonvanishing does not bound singular indices). No unsupported claim. (iii)
  The only literature-dependent step anywhere is effectivity of order/degree
  bounds (Chen–Kauers–Koutschan; Bostan–Chen–Chyzak–Li) — flagged by Opus5
  itself as unverified-from-memory, and R8 (0.1) leans on CKK Cor. 15. **Not
  verifiable in this sandbox**; keep it on the sweep list; existence needs
  none of it.
- **Duplication status.** §3.3–3.4 substantially reproves R8 Theorem 4.1
  (which existed at freeze; Opus5 saw its path and deliberately did not read
  it — disclosed). Per Card B's own protocol this direction is `DUPLICATE`;
  the surviving novel content is §3.1 (`u = ps`, removing R8's four-section
  projectors entirely) and §3.5. **The blind convergence is itself valuable:
  it is precisely the different-model confirmation R8 §9 asked for before
  funding the compiler**, on existence, X-free coefficients, typed
  certificate, and pointwise finite decision. The two proofs differ in the
  descent step (trace vs `N ⊂ L((s))`), which strengthens the confirmation.

## 8. Task 7 — the `D_0..D_34` ceiling and the lower endpoint: CONFIRMED

**Ceiling (§3.5).** Verified from the frozen R7R1 file read in full:

- R7R1 (0.1) is the exact identity `12F_XG − 8FG_X − t(F_XG_t − F_tG_X) =
  t²²`; (0.2) gives `w_{n+22}′ = −(n+2)q_n/16`, and R7R1 states
  "Consequently every `q_n dX` is exact in `L`" — the derivation direction is
  **identity ⟹ all rows**, exactly what the ceiling needs.
- `deg_t LHS ≤ 35` (`F` weight ≤ 14, `G` weight ≤ 21); the frozen R7R1
  hostile review (7ab758fa…) confirms `D_35 ≡ 0` identically (unique weight
  split `(14,21)`, `y`-free top corners) and **sharp** maximum `D_34`.
- Hence, set-theoretically: `{F : ∃G with the inhomogeneous system
  D_0=…=D_21=0, D_22=1, D_23=…=D_34=0} ⊆ {F : every tower row holds}`. The
  tower is a lossy, `G`-free consequence of the finite raw system and can
  never exclude a raw-system survivor. Opus5's statement ("its content is
  contained in the `G`-elimination of `D_0..D_34`; no row, and no number of
  rows, can ever exceed that finite object") is **CONFIRMED** with two
  scope pins that Opus5's text respects but promotion language must keep:
  (i) it is a one-directional domination, **not** a row-34 index cutoff for
  the tower; (ii) the converse direction fails typing — R7R1's converse
  builds only formal `L`-solutions with free constants ("need not descend to
  `K(X)` or produce polynomials"), so tower-passing `F` need not lift to a
  Keller `G`. Card C's void-condition ("if the rows are not derived from the
  finite identity") does not fire; the licensing direction is as Opus5 read
  it. Note the row-licensing fine print: for truncated clients only rows
  `n+22 < N` are licensed (R7R1); for the full Keller client all rows are.

**Lower endpoint (§9 primary): CONFIRMED.** `4Kg′ − 3K′g = 4K ⟺
∇_{−3}(g) = 1` with `∇_a = d + (a/4)K′/K` — exact. For
`K = ξ(ξ−ρ)^γ`, `Z_{−3} = {0, ρ}` iff `4 ∤ γ` (equivalently `4 ∤ 3γ`) ✓.
One **benign misattribution**: Opus5 cites "(N2) applies: … `|Z|−1 = 1`",
but `ν = −3 < 0` is outside the `|Z|−1` case of (N2); the licensed formula
there is `r−1+k_{−3} = 2−1+0 = 1`. The two coincide here because `Z` is all
roots and `k = 0`. The number, and the match with the frozen single forced
relation `h(ρ) = 4/(4−3γ)`, stand. The `γ ≡ 3 (mod 4) ⟺ 4 | deg K`
reading (an at-infinity/polynomial-primitive condition, not an affine one) is
exact (`deg K = γ+1`). The transfer-back question — does the upper client
impose a degree/support bound on `w_{n+22}` from `W = G/P¹²`, `deg_t G ≤ 21`
— is genuinely **open in the record**: R7R1's firewall says only that the
converse need not produce polynomials; nothing bounds the licensed
primitives. Well-posed question, correctly labeled a question. The secondary
(avenue 33 × 16) connection inherits the §9-pairing defect below.

## 9. Defects found (beyond the classifications above)

1. **Perfect-pairing overclaim — REFUTED AS STATED** (report §1 avenue-3
   raise, §7 rider 2, §9 secondary). Claim: "`H¹_dR(U,∇_ν) ×
   H¹_dR(U,∇_{−ν}) → K` is perfect." Counterexamples/gaps: (a) for
   `4 | ν` both factors are gauge-equivalent to untwisted `H¹_dR(U)` and the
   canonical pairing is cup product into `H²` of an **affine** curve, which
   is zero — dims are `r` each, so no canonical perfect pairing exists (e.g.
   `U = 𝔸¹∖Z(H)`, classes `dX/(X−a_i)`); (b) at resonant strata
   (some `e_iν/4 ∈ ℤ`, or integral exponent at `∞`) the natural pairing is
   `H¹ × H¹_c`, and `H¹_c → H¹` fails to be an isomorphism, so the
   `H¹ × H¹` statement needs — and does not have — a proof; (c) decisively
   for the campaign: on **both frozen fixtures** `deg H = 8`, so the
   `∞`-exponent `−ν·deg H/4 = −2ν` is **always** an integer — the fully
   nonresonant case never occurs on P or Q. Narrowest true statement:
   the pairing is perfect when every local exponent (all `e_iν/4` and
   `ν·deg H/4`) is non-integral; in general the perfect pairing lives on the
   image of `H¹_c → H¹` (the middle part), and whether the gate class pairs
   perfectly there is an open, well-posed question. **Consequence:** the
   avenue-3 raise and the avenue-33 reopen are not yet licensed as stated;
   the 2137Z synthesis line "rationality of the proposed residue pairings was
   not established" (frozen lines 160–163) remains in force. This is the one
   REFUTED-level defect in the report; it is not load-bearing for N1, N2,
   C1, `GATE-PR`, or the ceiling.
2. **Card A discriminator (ii) arithmetic slip — REPAIRED.** `n = 6, d = 2`
   gives `ν = 6+2−16 = −8`, not `−10`; and the P capacity is
   `r−1+k_{−8} = 3+1 = 4` ("full degree-2 receiver" is 4), not `r−1 = 3`
   (script 2 prints both). The other half of the prediction — P degree-2
   content provably vanishes at even `n ≥ 14` — is correct (`ν = n−14 ≥ 0`
   even ⇒ `Z_ν = ∅` on P). Any preregistration of the `d = 2` test must use
   the corrected numbers.
3. **Card B display — REPAIRED** (§6 above; Hadamard-weights repair).
4. Language notes, no math effect: "ρ is uniform" (§7 above); `Σ_{d≥1}`
   at `n = 0` (§2 above); "strictly stronger than E0" row-scoping (§4
   above); C3's "exactly" (§5 above).

## 10. History check and novelty labels — VERIFIED (nontrivially)

Because the canonical files mutated mid-session (§1), Opus5's history claims
must be judged against the **freeze state**:

- `notes.md` is still frozen (`654c358e…` matches): direct grep confirms the
  only relevant hit is line **9512**, "creative-telescoping or
  fixed-receiver recurrence compatible with de Rham" — a wanted/open item,
  exactly as Opus5 reported (`notes.md:9512`).
- `APPROACHES.md` freeze state (`f9ed44df…`, verified matching at session
  start): the current mutated file's only pre-overlay `telescop` hit is at
  line 78, inside the 22:40Z section; the 23:30Z overlay occupies lines
  16–57 (43 lines including the following blank); `78 − 43 = 35` — exactly
  Opus5's claimed `APPROACHES.md:35`. The mod-8 statement now at current
  line 38 sits **inside the post-seal overlay**, i.e. it was merged **from
  this round's synthesis** and did not exist at freeze. `AUDIT.md`: current
  pre-overlay hit at 186 versus Opus5's claimed 84 implies a 102-line
  overlay; the current mod-8 line 30 is inside it. Consistent throughout.
- The `Γ_a(X,z) = Σ H^k q_{a+4k} z^k` packaging is in the frozen synthesis
  (lines 133–136) as Opus5 says; R8 (0.2)/(2.3) had already corrected its
  gauge semantics at sector level; Opus5's §3.1 removes the sectioning
  entirely — a genuine further simplification, labeled correctly.

**Novelty verdicts:** N1, N2, C1, C2, C3 — genuinely `NEW` versus the freeze
record (the identical content now visible in the canonical overlay is this
round's own synthesis output, not anteriority). `GATE-PR` §3.3–3.4 —
`DUPLICATE` of R8 Thm 4.1 in the existence direction (blind, hence
confirmation-grade); §3.1 and §3.5 — `NEW` (the ceiling as an explicit stated
bound; Opus5's own "KNOWN in substance" hedge is fair since R7R1 contains the
derivation direction).

## 11. Narrowest promotable statements

1. **(P1, N1.)** For `n ≥ 1` and `d ≥ 1`, conditional on promoted (1.1):
   `[q_n]_{F-deg d} = (2/(n+2))·C((n+2)/8,d)·p^{n+2−8d}·S_{n,d}(X)` with
   `S_{n,d}` the ordered-composition sum; `q_0 = p²`.
2. **(P2, C1.)** If `8 | n+2` then `q_n ∈ K[X]` and row `m = n+22 ≡ 4
   (mod 8)` is identically vacuous in all `F`-degrees, for every `H` and
   every `F`; the `∇_m`-primitive is `H^{−m/4}∫q_n ∈ A` (licensed by
   `4 | m`).
3. **(P3, N2-capacity, now proved.)** With `ν = n+2−8d`, `Z_ν = {a_i : 4 ∤
   e_iν}`, `z = |Z_ν|`, the degree-`d` contribution of row `m` to `V_m` has
   rank at most: `0` if `ν ≥ 0, z = 0`; `z−1` if `ν ≥ 0, z ≥ 1`;
   `r−1+k_ν` if `ν < 0`. Proofs: §3.1 of this review (algebraic, char 0).
   Equality with `min(dim W_{n,d}, R_ν)` is **not** part of the promotable
   statement (40/42 frozen entries attain it; two do not).
4. **(P4.)** `m ≡ ν (mod 4)`, `k_m = k_ν`, and `H^{5+2d}` transports the
   degree-`d` class between `V_ν` and `V_m`; in sector language the receiver
   character is `b+2`, automatically carried by the physical form on `V_H`.
5. **(P5, normal form.)** `u = ps`, `G = Q/p² = Σ q̂_n uⁿ ∈ K(X)[[u]]`,
   `H²R⁸ = F(X,uR)`; gate row `m = n+22` ⟺ `λ(q_n dX) = 0` in
   `H¹_dR(V_H)`; and `λ(q_{b+4k}dX)` equals R8's normalized class
   `[p^{−(b+22)}q_{b+4k}dX]` under the Kummer identification
   (`H^k p^{−4k} = 1`).
6. **(P6, fixed instance.)** R8 Thm 4.1 ≡ Opus5 §3.3–3.4, now blindly
   double-derived: at fixed `(H,F)`, all gate coordinates satisfy one
   P-recurrence with `X`-free `ℓ_k ∈ K[s]` and an automatically
   `O(V_H)`-typed certificate; a pointwise `N_0` is computable by the
   singular-index schema. Not licensed: any numerical `N_0`, any
   cell-uniform `N_0`, any single cross-window operator, and (pending
   primary-text check) the explicit CKK order-bound constants.
7. **(P7, ceiling.)** Every solution of the inhomogeneous finite system
   `D_0..D_34` (with `D_22 = 1`) satisfies every tower row; the tower is a
   one-directional, `G`-free consequence of the finite raw system — a
   domination statement, not a row cutoff and not a converse.
8. **(P8, lower endpoint.)** The lower ODE is `∇_{−3}(g) = 1` on the
   `μ_4`-torsor of `K = ξ(ξ−ρ)^γ`; its affine obstruction space is
   `r−1+k_{−3} = 1`-dimensional (matching `h(ρ) = 4/(4−3γ)`), and
   `γ ≡ 3 (mod 4)` is the at-infinity condition `4 | deg K`.

## 12. Promotion advice

- **Promote** P1–P8 with the stated conditionalities. P3's proof is supplied
  here and should be same-model re-audited once before canonicalization.
- **Do not promote:** the realized-rank min law (keep as an observed
  40/42 heuristic); the perfect-pairing statement (REFUTED as stated; the
  avenue-3 raise and avenue-33 reopen should be held until a nonresonant/IH¹
  repair is written — on P/Q the `∞`-resonance is unavoidable); Card A's
  `d = 2` example as printed (use `ν = −8`, capacity 4); Card B's
  `1/(1−yz)` display (use the Hadamard repair).
- **Harness decision:** adopt (N2) for capacity screening and dead-row
  certification (rows `28, 32, 36` and all `m ≡ 4 (mod 8)` unconditionally;
  P rows 30/34 by `Z_ν = ∅`); **retain** the exact-rank harness for realized
  ranks — the two under-min entries show closed-form replacement is not
  licensed there. (Opus5 §5 keeps the harness as regression oracle; §8's
  "replace" wording should be weakened accordingly.)
- The `GATE-REC`/`GATE-PR` convergence satisfies R8 §9's precondition for
  funding the preregistered one-sector compiler (branch P, receiver `b+22`,
  normalization `p^{−(b+22)}S_b`, mutation controls) — AWS-only per standing
  rule.
- Contract compliance of the Opus5 report (2255Z §4 items 1–8): all eight
  present and well-formed; the disposition vector's raises of 1/16 are
  supported by the CONFIRMED content; the raise of 3 and reopen of 33 rest on
  the refuted pairing sentence and should be deferred.

## 13. Reproducible desk checks

All exact rational arithmetic (`fractions.Fraction`), no CAS, no AWS, total
runtime well under a minute. Scripts staged at `/tmp/f5xr_n1_check.py`,
`/tmp/f5xr_n2_check.py`, `/tmp/f5xr_zbound_check.py`; full text below.

Script 1 — N1/C1 (reversion vs closed form over `ℚ(X)`); output:
`ALL N1/C1 CHECKS PASS`, 41 `OK` lines, `C1 q_6/q_14 polynomial: YES` on all
fixtures, counterfixture anchors `q_0 = X², q_1 = 1/X` reproduced, and
`c_1 = 1/4` printed (Card B refutation).

```python
#!/usr/bin/env python3
# Fable5 cross-review desk check 1: NU-LAW (N1) + (C1) verification.
# Representation: rational functions over Q(X) whose denominators are powers of H,
# stored as (poly_numerator, H_exponent). Series in u = p*s with such coefficients.
# Reversion path: A(t) = (1+g)^(1/8) by binomial series; solve t = u*A(t) by iteration;
# qhat_n := [u^n] A(t(u))^2  (so q_n = qhat_n * p^(n+2); cf. R8 (1.2)).
# N1 path:   qhat_n = sum_d (2/(n+2)) * C((n+2)/8, d) * H^(-2d) * S_{n,d},
#            S_{n,d} = sum over ordered compositions (i_1..i_d), i_k>=1, of F_{i1}...F_{id},
#            computed by direct composition DP (independent of the g-power expansion).
# (C1): for 8 | n+2, q_n = qhat_n * H^((n+2)/4) must be a polynomial in X.
from fractions import Fraction as Fr

def pnorm(p):
    while p and p[-1] == 0: p.pop()
    return p
def padd(a,b):
    n=max(len(a),len(b)); r=[Fr(0)]*n
    for i,c in enumerate(a): r[i]+=c
    for i,c in enumerate(b): r[i]+=c
    return pnorm(r)
def pscale(a,c): return pnorm([x*c for x in a])
def pmul(a,b):
    if not a or not b: return []
    r=[Fr(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b): r[i+j]+=x*y
    return pnorm(r)
def pdivmod(a,b):
    a=a[:]; q=[Fr(0)]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and a:
        c=a[-1]/b[-1]; d=len(a)-len(b); q[d]=c
        for i,y in enumerate(b): a[d+i]-=c*y
        pnorm(a)
    return pnorm(q), a
class RH:
    __slots__=('num','e')
    def __init__(self,num,e=0): self.num=pnorm(list(num)); self.e=e
    def red(self,H):
        while self.e>0 and self.num:
            q,r=pdivmod(self.num,H)
            if r: break
            self.num=q; self.e-=1
        if not self.num: self.e=0
        return self
def rhadd(a,b,H):
    e=max(a.e,b.e)
    na=pmul(a.num,ppow(H,e-a.e)); nb=pmul(b.num,ppow(H,e-b.e))
    return RH(padd(na,nb),e).red(H)
def rhmul(a,b,H): return RH(pmul(a.num,b.num),a.e+b.e).red(H)
def rhscale(a,c): return RH(pscale(a.num,c),a.e)
def rheq(a,b,H):
    e=max(a.e,b.e)
    return pnorm(padd(pmul(a.num,ppow(H,e-a.e)), pscale(pmul(b.num,ppow(H,e-b.e)),Fr(-1))))==[]
def ppow(H,k):
    r=[Fr(1)]
    for _ in range(k): r=pmul(r,H)
    return r
ZERO=lambda: RH([],0); ONE=lambda: RH([Fr(1)],0)
def sadd(A,B,H,N):
    r=[]
    for i in range(N+1):
        x=A[i] if i<len(A) else ZERO(); y=B[i] if i<len(B) else ZERO()
        r.append(rhadd(x,y,H))
    return r
def smul(A,B,H,N):
    r=[ZERO() for _ in range(N+1)]
    for i,x in enumerate(A):
        if i>N: break
        if not x.num: continue
        for j,y in enumerate(B):
            if i+j>N: break
            if not y.num: continue
            r[i+j]=rhadd(r[i+j],rhmul(x,y,H),H)
    return r
def binom(alpha,d):
    r=Fr(1)
    for i in range(d): r*= (alpha-i)/ (i+1)
    return r
def run_fixture(name,H,Fs,N):
    print('==',name)
    g=[ZERO() for _ in range(N+1)]
    for i,Fi in Fs.items():
        if i<=N: g[i]=RH(Fi,2).red(H)
    A=[ONE()]+[ZERO() for _ in range(N)]
    gp=[ONE()]+[ZERO() for _ in range(N)]
    for j in range(1,N+1):
        gp=smul(gp,g,H,N)
        if all(not c.num for c in gp): break
        A=sadd(A,[rhscale(c,binom(Fr(1,8),j)) for c in gp],H,N)
    t=[ZERO() for _ in range(N+1)]
    for _ in range(N+1):
        At=subst(A,t,H,N)
        t=[ZERO()]+At[:N]
    At=subst(A,t,H,N)
    D=smul(At,At,H,N)
    S=[[None]*(N+1) for _ in range(N+1)]
    S[0][0]=RH([Fr(1)],0)
    for n in range(1,N+1):
        S[n][0]=ZERO()
        for d in range(1,N+1):
            acc=ZERO()
            for i,Fi in Fs.items():
                if i<=n and S[n-i][d-1] is not None:
                    acc=rhadd(acc,rhmul(RH(Fi,0),S[n-i][d-1],H),H)
            S[n][d]=acc
    ok=True
    for n in range(0,N+1):
        pred=ZERO()
        for d in range(0,n+1):
            if S[n][d] is None or (n>0 and d==0): continue
            c=Fr(2,n+2)*binom(Fr(n+2,8),d)
            pred=rhadd(pred,rhscale(RH(S[n][d].num,S[n][d].e+2*d),c),H)
        # (n=0,d=0 term already included by the loop above)
        m=rheq(D[n],pred,H)
        ok&=m
        tag='OK ' if m else 'FAIL'
        extra=''
        if (n+2)%8==0:
            q=RH(D[n].num, D[n].e-(n+2)//4)
            ispoly = q.e<=0
            if q.e<0: q=RH(pmul(q.num,ppow(H,-q.e)),0)
            else: q=RH(q.num,q.e).red(H); ispoly = q.e==0
            extra=' | C1 q_%d polynomial: %s'%(n,'YES' if ispoly else 'NO')
            ok&=ispoly
        print(' n=%2d N1 match: %s%s'%(n,tag,extra))
    return ok
def subst(A,t,H,N):
    r=[ZERO() for _ in range(N+1)]; r[0]=A[0]
    tp=[ONE()]+[ZERO() for _ in range(N)]
    for j in range(1,len(A)):
        tp=smul(tp,t,H,N)
        if all(not c.num for c in tp): break
        r=sadd(r,[rhmul(A[j],c,H) for c in tp],H,N)
    return r
allok=True
H=[Fr(0),Fr(0),Fr(-1),Fr(1)]
allok&=run_fixture('H=X^2(X-1), F1=X+2,F2=3X^2-1,F3=X', H,
   {1:[Fr(2),Fr(1)], 2:[Fr(-1),Fr(0),Fr(3)], 3:[Fr(0),Fr(1)]}, 14)
H=[Fr(1),Fr(0),Fr(-2),Fr(0),Fr(1)]
allok&=run_fixture('H=(X^2-1)^2, F1=2X, F2=X^2+X+1', H,
   {1:[Fr(0),Fr(2)], 2:[Fr(1),Fr(1),Fr(1)]}, 14)
H=[Fr(0)]*4+[Fr(1)]
allok&=run_fixture('R7R1 counterfixture H=X^4, F1=4X^4', H, {1:[Fr(0)]*4+[Fr(4)]}, 10)
print('== anchors on counterfixture ==')
print(' c_1 = (2/3)*C(3/8,1) =', Fr(2,3)*binom(Fr(3,8),1), ' (Card B geometric-kernel display needs c_n==1; c_1=1/4 refutes it)')
print('ALL N1/C1 CHECKS PASS' if allok else 'SOME CHECK FAILED')
```

Script 2 — N2 tables/b₁/Card-A; output: all 42 entries printed with
`R`, `dim W`, `min`, measured; `bound violations: 0`, `under-min entries: 2`
(P row 35, control row 31); sums `26/27` (P), `35/37` (Q); `b₁ =
14/17/4/29`, `3b₁ = 42/51/12/87`; `Card A d=2 example: n=6,d=2 -> nu = -8
(Opus5 wrote -10); P receiver R = 4 (Opus5 wrote r-1=3)`.

```python
#!/usr/bin/env python3
# Fable5 cross-review desk check 2: N2 receiver law vs the three frozen E0 tables.
W = {1:16,2:15,3:14,4:13,5:12,6:11,7:10,8:9,9:7,10:6,11:5,12:3,13:2,14:1}
fixtures = {
 'P (H=(X^4-1)^2)': dict(mult=[2,2,2,2],
    table=[3,4,3,4,3,0,3,0,3,0,3,0,1,0]),
 'Q (H=A^2B)':      dict(mult=[2,2,2,1,1],
    table=[4,5,4,4,4,0,4,1,4,0,4,1,2,0]),
 'control (r=8 squarefree)': dict(mult=[1]*8,
    table=[7,8,7,7,7,0,7,7,6,0,5,3,2,0]),
}
def R_nu(nu, mult):
    r=len(mult)
    Z=[e for e in mult if (e*nu)%4!=0]
    k=1 if not Z else 0
    if nu>=0:
        return 0 if not Z else len(Z)-1
    return r-1+k
def k_nu(nu,mult): return 1 if all((e*nu)%4==0 for e in mult) else 0
viol=0; under=0
for name,fx in fixtures.items():
    print('==',name)
    tot12=0; tot14=0
    for i,n in enumerate(range(1,15)):
        nu=n-6; m=n+22
        R=R_nu(nu,fx['mult']); mn=min(W[n],R); meas=fx['table'][i]
        tot14+=meas
        if n<=12: tot12+=meas
        flag=''
        if meas>R: flag=' BOUND-VIOLATION'; viol+=1
        elif meas<mn: flag=' UNDER-MIN (min=%d)'%mn; under+=1
        print(' row %d n=%2d nu=%3d  R=%d dimW=%2d min=%d measured=%d%s'%(m,n,nu,R,W[n],mn,meas,flag))
    print('  sum rows 23-34 =',tot12,' sum rows 23-36 =',tot14)
print('bound violations:',viol,' under-min entries:',under)
for name,mult,b1x in [('P',[2,2,2,2],14),('Q',[2,2,2,1,1],17),('one-root e=4',[4],4),('squarefree r=8',[1]*8,29)]:
    c=sum(1 for j in range(4) if k_nu(j,mult)==1)
    b1=4*(len(mult)-1)+c
    print('b1 %-16s = %d (expect %d) 3b1=%d'%(name,b1,b1x,3*b1))
n,d=6,2; nu=n+2-8*d
print('Card A d=2 example: n=6,d=2 -> nu =',nu,'(Opus5 wrote -10);',
      'P receiver R =',R_nu(nu,[2,2,2,2]),'(Opus5 wrote r-1=3)')
for n in (13,14,15,16):
    nu=n-14
    print('  P d=2 n=%d nu=%d capacity=%d'%(n,nu,R_nu(nu,[2,2,2,2])))
```

Script 3 — `|Z_ν|−1` bound, safe-overestimate rank check; output:
`H=X²(X−1)(X−2)` `ν=2`: span-overestimate `1` at `K = 8,12,16` (claim ≤ 1,
full receiver 2 — strict regime verified); `ν=1,3`: `2` (claim ≤ 2);
canary `H=X²(X−1)` `ν=2`: `0` (claim = 0, matching the algebraic proof).

```python
#!/usr/bin/env python3
# Fable5 cross-review desk check 3: the |Z_nu|-1 effective-receiver bound (N2, nu>=0 case).
# Method (safe direction): partial-fraction basis {X^k} u {(X-a)^-k}; exact forms from
# generators g in {X^k, (X-a)^-k, k<=K}; truncating the exact space UNDERSTATES it, so
# rank(tests mod truncated exacts) OVERSTATES the true span; result <= |Z|-1 verifies.
from fractions import Fraction as Fr

def run(roots, mults, nu, K, J, label):
    M = K + 3
    idx = {}
    def ix(key):
        if key not in idx: idx[key] = len(idx)
        return idx[key]
    for k in range(M+1): ix(('p',k))
    for a in roots:
        for k in range(1, M+1): ix((a,k))
    def vec(): return {}
    def vadd(v, key, c):
        if c:
            v[key] = v.get(key, Fr(0)) + c
            if not v[key]: del v[key]
    def mul_inv(v, a):
        r = vec()
        for key, c in v.items():
            if key[0] == 'p':
                k = key[1]
                for i in range(k):
                    vadd(r, ('p',i), c * Fr(a)**(k-1-i))
                vadd(r, (a,1), c * Fr(a)**k)
            else:
                b, k = key
                if b == a:
                    vadd(r, (a,k+1), c)
                else:
                    c0 = Fr(a - b)
                    cur = vec(); vadd(cur, (a,1), 1/c0); vadd(cur, (b,1), -1/c0)
                    for t in range(2, k+1):
                        nxt = vec()
                        for kk, cc in cur.items(): vadd(nxt, kk, cc/c0)
                        vadd(nxt, (b,t), -1/c0)
                        cur = nxt
                    for kk, cc in cur.items(): vadd(r, kk, c*cc)
        return r
    def deriv(v):
        r = vec()
        for key, c in v.items():
            if key[0] == 'p':
                k = key[1]
                if k > 0: vadd(r, ('p',k-1), c*k)
            else:
                a, k = key
                vadd(r, (a,k+1), -c*k)
        return r
    def nabla(v):
        r = deriv(v)
        for a, e in zip(roots, mults):
            w = mul_inv(v, a)
            for kk, cc in w.items(): vadd(r, kk, cc * Fr(nu*e, 4))
        return r
    gens = []
    for k in range(K+1):
        v = vec(); vadd(v, ('p',k), Fr(1)); gens.append(nabla(v))
    for a in roots:
        for k in range(1, K+1):
            v = vec(); vadd(v, (a,k), Fr(1)); gens.append(nabla(v))
    tests = []
    for j in range(J+1):
        v = vec(); vadd(v, ('p',j), Fr(1)); tests.append(v)
    def rank(vs):
        rows = []
        for v in vs:
            row = [Fr(0)]*len(idx)
            for kk, cc in v.items(): row[idx[kk]] = cc
            rows.append(row)
        r = 0; c = 0; n = len(idx)
        while r < len(rows) and c < n:
            piv = None
            for i in range(r, len(rows)):
                if rows[i][c]: piv = i; break
            if piv is None: c += 1; continue
            rows[r], rows[piv] = rows[piv], rows[r]
            pv = rows[r][c]
            for i in range(len(rows)):
                if i != r and rows[i][c]:
                    f = rows[i][c]/pv
                    for jj in range(c, n): rows[i][jj] -= f*rows[r][jj]
            r += 1; c += 1
        return r
    rk_e = rank(gens)
    rk_all = rank(gens + tests)
    print('%s nu=%d K=%d: span-overestimate = %d' % (label, nu, K, rk_all - rk_e))

roots3 = [0,1,2]; mults3 = [2,1,1]
for K in (8, 12, 16):
    run(roots3, mults3, 2, K, K-3, 'H=X^2(X-1)(X-2) [claim <=1, full receiver 2]')
for K in (8, 12):
    run(roots3, mults3, 1, K, K-3, 'H=X^2(X-1)(X-2) [claim <=2]')
    run(roots3, mults3, 3, K, K-3, 'H=X^2(X-1)(X-2) [claim <=2]')
roots2 = [0,1]; mults2 = [2,1]
for K in (8, 12):
    run(roots2, mults2, 2, K, K-3, 'H=X^2(X-1)   [claim  =0]')
```

(Script 1 had one reviewer-side bug during development — a double-counted
`n=0, d=0` term — found and fixed before any verdict was drawn; recorded so
it is not paid for twice.)

## 14. Process, contamination, and scope disclosure

- **Model identity:** Claude Fable 5 (`claude-fable-5`). Model identity is
  neither a vote nor evidence.
- **Execution:** shell available this session; all computations were exact,
  small, local desk scripts (seconds); no heavy algebra, no Gröbner, no CAS,
  no AWS contact, no live-lane inspection, no external communication, no web
  access (the CKK/BCCL literature step is therefore flagged, not checked).
- **Peer blindness:** I read no `2259Z` peer lane response (`fable5`, `sol`,
  `grok46`), no `2259Z` hostile review, and no cross-review prompt other
  than my own. A directory listing of `xmodel/` performed to locate my
  assigned output necessarily showed peer file **names, sizes, and mtimes**;
  no contents were opened.
- **Mutated-canonical contamination (the one real leak).** Before diagnosing
  the mid-session mutation (§1), I read lines 1–100 of the **post-seal**
  `APPROACHES.md`, whose 23:30Z overlay contains adjudicated forms of the
  claims under review (capacity-vs-realized distinction, row-30 candidate,
  ceiling scoping). Order of events, so the reader can weigh it: my
  recomputation of all 42 table entries, the two under-min findings, the
  capacity/realized split, the C1/ν-law verifications, and the ceiling
  direction check against R7R1 were all completed **before** that read; the
  perfect-pairing refutation, the Card A/Card B defects, both proofs in
  §3.1, and all scripts were derived independently of it (the overlay
  contains none of them). The overlay's agreement with my §3.3/§12 harness
  recommendation is convergent, not copied, but I flag it rather than smooth
  it over.
- **Memory disclosure.** My persistent memory index contains lines about
  this campaign, including one summarizing NU-LAW/GATE-PR-shaped claims
  (most plausibly written by the blind Fable5 *ideation* lane session earlier
  today — which I did not read this session). Every load-bearing fact in
  this review was re-derived or re-verified this session against the hashed
  artifacts and fresh computation; no verdict rests on memory.
- **`jc2-lean`:** never entered, listed, searched, read, built, statused, or
  modified. No command touched it; the only reference to it in my context is
  the system-provided git-status snapshot.
- **Canonical files:** none edited. This file is my only repository write.
- **Scope.** This review proves no face landing, no family exclusion, no
  Keller pair, no `D_22 = 1` solvability, no K00/LF40/coverage result, and
  no JC2 conclusion. It adjudicates the Opus5 `2259Z` lane report against
  the frozen record, supplies proofs for the N2 capacity bound, refutes one
  pairing overclaim, and repairs two card-level defects. Everything here is
  submitted for the same different-model hostile review the campaign imposes
  on every lane.
