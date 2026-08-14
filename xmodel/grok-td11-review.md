**VERDICT: SOUND-WITH-ERRATA — the entry-tier kill (Lemma CAP-DEN on the intended X-family, Lemma 11A-RES on the unpadded 5/8, one-step empty windows, conservative caps) replays; the closure-wide “budget-9 / 437-state” lift and the compiler emptiness certificate are not earned as written.**

Reviewer: Grok 4.6 (hostile referee). Date: 2026-08-14.
Target: `TOWER-TD11.md` (whole doc, focus §§7–14 / Theorem TD11-CLASH) and `cases/tower_td11.py`.
Panel-precursor claim under review: every td-11 class-B/C configuration under the E5F-corrected discipline (H8 = `P/μ`, all realizations including `Pi = 5^k` and in-perimeter neutrals) dies at the tower tier, per-entry, over the three L6 entries.
Method: line-read of `TOWER-TD11.md` against `xmodel/sol-td11-13-scope.md` §§2–3, `xmodel/sol-normalform.md` (1.4)/(4.5)–(4.6)/584–599, `NF-D.md` D5, `TOWER-UNIFORM.md` N2/N3, `xmodel/grok-tower-review.md` Case C, `cases/scratch_offaxis_pricing/px2.py` + `px5.py`. Independent exact `Fraction` replay of CAP-DEN (strong form and all residuals), of 11A-RES (`M'` and `v_2`), of the cap-candidate lattice, and of the four near-misses. `python3 cases/tower_td11.py`: exit 0, **46/46 PASS**, 122 s. Independent `px5.close_with_cells` at budget 5 and budget 9 on `(3,2)`; seed-level `chain_steps` on `(3,2)`, `(3,1)`, `(2,1)`, `(3/2,2)`. No other repo file modified. No git.

---

## Findings (worst first)

### 1. Severity: erratum — Claim OB-6 / §12(iii). The closure-wide audit ran the td-7 budget and the td-7 dirty-menu caps, not the gross budget-9 discipline the perimeter advertises. `(3,2)` is 21 states at budget 5 and **743** at budget 9.

- File: `TOWER-TD11.md:226-248,354-363,379`; `cases/tower_td11.py:409-410`; `cases/scratch_offaxis_pricing/px5.py:63`; `cases/scratch_offaxis_pricing/px2.py:32,82,87`; `xmodel/sol-td11-13-scope.md:77-79,324-329`
- Claim: the three opponent seeds close at 21 + 347 + 69 states; every depth-`≥2` gap is `< 1/2` by a growth/ratio law; “closure audits ran the gross budget 9 discipline of the scope tables”; resonance census over “all 437 engine states.”
- How checked.

  **The gate calls `px5.close_with_cells(*seed)` with the default `budget=5`.** That is `td−2` at td-7 (`px2.py:32`), not `td−1−ψ ≤ 9` at td-11. Independent rerun:

  | seed | budget 5 (what the gate ran) | budget 9 (what §12 claims) |
  |---|---:|---:|
  | `(3,2)` | **21**, `M ∈ {1,2,3,4,5,7}` | **743**, `M` up to **97**, `w` up to 6 |
  | `(3/2,2)` | **69** | not finished here (already larger than 69 at the same engine) |
  | `(4/3,3)` | **347** (gate) | not rerun |

  21 + 347 + 69 = 437 is the budget-5 count. It is not a budget-9 count.

  **The dirty menu is px2’s td-7 loop.** `chain_steps` enumerates `k ∈ {0,…,6}` and `lex ∈ {0,…,40}`. Scope §1.2 literally says “do not inherit px2’s td-7 loop caps.” Scope §3.2 says the one-step tables are at gross budgets 9/11 and `k ≤ 9` at td-11. Seed-level “no rows beyond `k=5`” (scope:324–327) does not license the same cap on descendant states.

  **The growth/ratio law is not a state-independent bound.** Clean ratio is `n + 1/ν` with `n` controlled by `num(w)`. At budget 9, `(3,2)` already reaches `w = 6`, so clean ratios can reach `7/2`. st96 ratio `ℓ·dq/dp → ℓ(1+k+lex)/(ℓ+S_m)` is in principle `O(k+lex)` at large `ℓ`; `ℓ | M` and `M` reaches 97. I did not finish an R* sweep of all 743 states (large-`M` dirty menus dominate). I therefore **do not claim** a budget-9 counterexample with gap `≥ 1/2`. I do claim the written law `R* = 5/2, 3, 5/2` is an empirical maximum on the budget-5 slice, not a proved bound on the td-11 closure.

  **What survives.** Seed-level one-step menus are the frozen scope §3.2 tables (budget 9, including the `5/8`). Those do not need the multistep closure. Depth-`≥2` from a *budget-5-reachable* state, under px2’s menu, has `R* < p` and `mult ≥ 2` (gate OB6a/b, and the seed `(3,2)` menu independently: unique clean is `D3n2nu2` with ratio `5/2`, every st96 ratio `≤ 7/4`, every recorded `dp/ℓ ≥ 2`). That is a real but strictly smaller object than “the three multistep closures at budget 9.”

  **Erratum to write.** Replace “gross budget 9 / 437 engine states” by: *the px2/px5 closures at budget 5, under px2’s `k ≤ 6`, `lex ≤ 40` menu, totalling 21 + 347 + 69*. Configurations that use `λ ∈ {6,7,8,9}` or a `k ≥ 7` dirty cell sit outside the checked set and must be reported OPEN until a budget-9 (or shape-theoretic `R*` bound) audit exists. Perimeter clause (iii) currently asserts the opposite.

### 2. Severity: erratum — Claim (6), §10. The census implication is not an emptiness certificate. It is a *conditional template*, and the written condition misses the §12 perimeter.

- File: `TOWER-TD11.md:326-339,287-303,374-382`; `cases/tower_td11.py:481-488`
- Claim: any future td-11 class-B/C census row that passes the E5F-corrected enumeration discipline contains a synchronized spine in one of the three entry shapes (or fails H8 = spine-death) and therefore emits `TOWER-DEAD`. “That statement — not a cell count — is the emptiness certificate.”
- How checked.

  **The compiler does not exist.** Scope §1.1 still marks the Q+E5/E5F refile **UNKNOWN**. §10’s title admits this. A certificate quantified over a nonexistent row set is a *schema*: *if* a row is one of the three entry shapes *and* lies in the theorem’s configuration class, *then* stamp `TOWER-DEAD` with `(entry, packet, cap, CAP-DEN or 11A-RES)`.

  **§10 is conditional on the enumeration discipline and on a mapping to `{11-A,11-B,11-C}`.** That much is written, and Rule 6 for unmapped rows is the right hedge. The mapping claim itself is not a theorem: the three L6 entries are the entry layer, but a future compiler can emit nested/mixed/post-jump decorations that are labelled 11-C and are not the audited seed closures.

  **The missing conjunct is the §12 perimeter.** Nested inner-merge orders that create chart states before the candidate clash (clause (i); 11-C’s 145-row skeleton “enumerated but not state-audited”), `ν = 1` insertions (iv), multi-word NF-Z coexistence (ii), and the actual (budget-5) horizon (iii, after finding 1) are *outside the theorem* and “reported OPEN, never certified.” §10’s “therefore emits `TOWER-DEAD`” has no such rider. A compiler that implements §10 as written will stamp nested-11-C rows that §12 forbids it to certify.

  **The gate is a tautology.** `check(..., True)` at `tower_td11.py:488`. It does not test mapping, perimeter, or a single census row.

  **Erratum to write.** The compiler consumes: `TOWER-DEAD` *if and only if* the row maps to one of the three packets **and** the configuration is inside the (corrected) §12 perimeter; otherwise `OPEN` / Rule 6. Do not call this an emptiness certificate. It is a per-row classifier for a book that has not been enumerated.

### 3. Severity: residual — “46 machine-checked rows” overstates the obligation discharge. Four theorem-level checks are `True`, and several others are identities.

- File: `cases/tower_td11.py:260-261,366-367,457-460,463-469,481-488`; `TOWER-TD11.md:355-363`
- Claim: blocks 0–13 are 46 machine-checked rows discharging OB-1/4/5/6/7/8/10 and the theorem aggregate.
- How checked. Count of `check()` calls is 46 and all pass. The following do not constrain arithmetic:

  | row | what it evaluates |
  |---|---|
  | OB7e Case B | `True` |
  | OB8b no sibling-X tie | `True` |
  | OB10 realization dichotomy | `True` |
  | census implication | `True` |
  | B1 “not td-7-frozen” | `Fr(5,4) == Fr(5,4)` |
  | C2 menu identity | `{2/5, 5/14} == {2/5, 5/14}` |
  | OB1c pole degrees | `(2,4) == (1*2, 2*2)` and cyclic |

  OB-8 composition, OB-10 realization, and Case B are *cited* (no-skip descent, E5F dichotomy, third-pole cap-shrink). That is legitimate law-coverage, and §12’s “law-covered” list already says so. It is not legitimate to count those citations as machine rows that discharge the obligation. The honest machine core is the domain law, the three one-step windows, packets, H8 inhabitation, cap examples, the `α`-lattice / den-sweep / CAP-DEN residuals, the budget-5 closure audit, and 11A-RES `v_2`.

### 4. Severity: residual — Lemma 11A-RES. The `5/8` in-window route always drops `M` and the `v_2` mismatch fires; the written `M'` formula is the `n = 1` law, not the resonance law. No in-window non-drop route found.

- File: `TOWER-TD11.md:270-283,48-52,101-104`; `cases/tower_td11.py:102-106,129-140`; `px2.py:46-60`; `xmodel/sol-normalform.md:561-599`
- Claim: the resonance `(Δ,n,ν) = (3,2,2)` is an M-drop `2 → 1`, so `μ | M' = 1` forces `μ = 1`; `v_2(8AB) ≥ 3` vs `v_2(2·Pi) = 1`; H8_EQUAL_QUOTIENT_VP_MISMATCH on every route shape.
- How checked.

  **Engine `M'` is `gcd(ℓ, dq) = gcd(ℓ, 5)`, not `gcd(ℓ, ν+1) = gcd(ℓ, 3)`.** The latter is the clean `n = 1` update (NF-D D5). Gate block 1 checks `gcd(ℓ, 3)`. Both formulas give `M' = 1` on `ℓ | 2`, so the drop conclusion is correct and the citation is not.

  **Uniqueness at the seed.** `chain_steps(3, 2)` has exactly one clean row, `D3n2nu2`, landing at `(w,M) = (2,1)` with `λ = 0`. Nine st96 rows and one pure-b; none has ratio `5/2`. Gap at seed `p = 4` is ratio/`4`; only ratio `5/2` produces `5/8`. Padded copies `5/(8A)` for `A ≥ 2` sit below `1/2` (gate A3, replayed).

  **The drop is forced at every small `M` that can host the same clean cell:** `(3,1)`, `(3,2)`, `(3,3)` all emit `D3n2nu2` with `M2 = 1`. After the drop the state is `(2,1)`. That state has *no* st96/pure-b (`ℓ < 2` skips both) and no clean `n ≥ 2` (`Δ` range is empty at `a = 2`). `M` cannot rebound. D5-irreversibility is stronger than needed: L-A freeze of `(2,1)` already kills the “raise `M`, pick `μ` to cancel `v_2`” route. (Charged steps *can* raise `M` — the budget-5 `(3,2)` closure already contains `M ∈ {3,4,5,7}` via st96 — but only *before* the resonance, at which point the subsequent `5/8` copy is padded and out of window.)

  **`v_2` is identity, not a stack-length fact.** `v_2(8) = 3`. A `w = 3` prefix `A` is 3-free and may be even (`ν = 2` is legal); extra 2-adic valuation only enlarges the left side. A `w = 2` suffix `B` is odd, so `v_2(B) = 0`. Chain-1 is frozen at `M = 1`, `μ = 1`, `Pi` odd, `v_2(2·Pi) = 1`. Replayed on all stacks of length `≤ 2` with letters `< 40`: zero failures. The promoted certificate at `sol-normalform.md:584–599` is exactly this comparison and assumes `μ = (1,1)`, which the drop now forces.

  **Hunt result.** The only in-window `5/8` is the unpadded seed-level clean step. Every legal `ℓ` drops `M`. No route shape was found where that step preserves `M`. The `μ = M` escape of grok-nfd finding 1 is closed on this branch.

### 5. Severity: clear — Claim (1), OB-7 / Lemma CAP-DEN. The `ν`-quantifier closes algebraically on the intended X-family. It is not an overclaim once `ν = 1` is read out of the X-interval. The 2-adic residuals replay exactly.

- File: `TOWER-TD11.md:199-224,347`; `cases/tower_td11.py:304-367`; death equation from `xmodel/grok-tower-review.md:38-41` and `t9_15_direct.json:716`
- Claim: `k_m = den(α_m − 1 + gap(X))` is legal iff that denominator divides the cap `c`; `num ≡ c (mod ν)` so `den | c ⇒ ν | c²`; odd `ν ≥ 3` divides none of `{1,4,16,36}` (11-B domain removes 3, 9); residuals `ν ∈ {2,4}` refuse 2-adically; sweep `ν ≤ 300` plus resonant `5/4` has zero escapes.
- How checked.

  **Death equation is the promoted one.** `ℓ/k = gap(X) + α − 1`. Existence of integers `ℓ, k` with `k | c` is equivalent to `c · r ∈ ℤ`, i.e. `den(r) | c`. Confirmed against the Case C display `ℓ_m/k_m = α_m − 1/2 + 1/(2ν_X)`.

  **Stronger criterion, independent of the register.** For `gap = (ν+1)/(2ν)`,
  `den(r) | c  ⇔  2ν | c(ν+1)`
  for every residue `a/c`. Checked on `c ∈ {1,2,4,6}`, `ν = 1..79`, all residues: identity. In particular `den | c ⇒ ν | c` (since `gcd(ν, ν+1) = 1`), which is stronger than the document’s `ν | c²`. The weaker form is still a correct necessary condition and is what they use to list residuals.

  **Complete escape list for `ν = 1..400`.** Exactly six pairs `(c,ν)` have some residue with `den(r) | c`:

  | `c` | `ν` | why it is not an entry escape |
  |---|---:|---|
  | 1,2,4,6 | 1 | `gap = 1` lies outside every stated X-interval (`(1/2,2/3]` / `(1/2,3/4]`); §12(iv) sends `ν = 1` to NF-P |
  | 4 | 2 | 11-A/C require odd `ν` at `w = 2`; 11-B’s caps are `{1,2,6}`, not 4 |
  | 6 | 3 | 11-B domain `3 ∤ ν` at `w = 3` (near-miss #1) |

  Zero escapes remain on 11-A/C odd `ν ≥ 3` against `{1,2,4}`, and on 11-B `3 ∤ ν ≥ 2` against `{1,2,6}`, including resonant `X = 5/4`.

  **2-adic residuals, exact dens:**

  | formula | dens | divides the target cap? |
  |---|---|---|
  | `(2a−3)/12` (`ν=2`, `c=6`) | `{4,12}` | no |
  | `(4a−9)/24` (`ν=4`, `c=6`) | `{8,24}` | no |
  | `(2a−1)/4` (`ν=2`, `c=2`) | `{4}` | no |
  | `(4a−3)/8` (`ν=4`, `c=2`) | `{8}` | no |
  | `(2a+3)/12` (resonant `5/4`, `c=6`) | `{4,12}` | no |
  | `(2a+1)/4` / `(4a+1)/4` (`5/4`, `c=2,1`) | `{4}` | no |

  The prose union `{4,8,12,24}` is the union of those dens. Gate OB7c checks the `c=6` pair and the congruence `num ≡ c (mod ν)` on a sample; the sweep OB7b covers the rest, including `c=2` and `5/4`.

  **`α`-lattice is a genuine superset, via fractional parts.** `den(α − 1 + g)` is period-1, so sweeping `a = 0..c−1` is equivalent to sweeping every register on the `1/c` lattice, including `α_1 ∈ {3/2, 5/2}`. Prefix step `α ↦ α + ℓ(k−1)/k` with `k | c` stays on that lattice for every `ℓ` (checked to `ℓ = 30`). The `ℓ < 12` loop in the gate is redundant but not wrong.

  **td-7 regression holds.** Cap `c=2`, residues `{0,1/2}`: `den` is `ν` or `2ν`, never divides 2 for odd `ν ≥ 3`. Matches “`k=1` forces `2ν | rν+1`, `k=2` forces `ν | 1`.”

  **The one residual they should have named.** `ν = 1` *does* divide every `c²` and *does* give `den | c` at every cap, and `legal(w,1)` is true at `w ∈ {2, 3, 3/2}`. At the actual starting register `α = 3/2`, `r = 3/2` and `den = 2` divides every positive 11-A/C cap: this is a Case-A escape `k = 2 | 2`. It is excluded by the *interval* description of X in §§1–3, not by the domain law and not by the residual list. The theorem statement §9 says “domain-legal `ν_X`.” Write `ν ≥ 2` (or keep the interval) in the theorem line. This is a wording hole, not a live escape for the pole-adjacent family the clash uses.

### 6. Severity: clear — Claim (4), OB-5. Conservative `{1,2,4} / {1,2,6} / {1,2}` is complete for the stated formula `k | gcd(pdeg_P, i_first · P_pre)` with `pdeg_P` the *seed* pole-pattern degree.

- File: `TOWER-TD11.md:186-197`; `cases/tower_td11.py:286-302`; `xmodel/sol-td11-13-scope.md:171-172`
- Claim: 11-A candidates `{2,4}` from `gcd(4, i·P_pre)`, `i ∈ {2,4}`, `P_pre` parity free; 11-B `{2,6}` from `gcd(6, i·P_pre)`, `i ∈ {2,6}`, `P_pre` odd 3-free; 11-C `{2}` by the td-7 port; divisor closure `{1}`.
- How checked.

  Seed pole-pattern degrees are `(2,4)`, `(2,6)`, `(2,4,4)` (scope §3.1 packets). The joint cap divides `gcd(pdeg_P, ·)` hence divides `4` or `6`. Checking the *largest* candidate is the conservative direction for a kill: if `den(r)` divides no divisor of 6, it divides no actual cap `| 6`.

  Independent lattice:

  * 11-A, `pdeg = 4`: `gcd(4, i·P)` ∈ `{1,2,4}` for every `i, P`. Even `P_pre` is realized (`legal(3,2)`), giving 4. Odd `P_pre` gives 2.
  * 11-B, `pdeg = 6`, `P` odd 3-free: `i = 2` gives only 2; `i = 6` gives 6; `i = 3` (if `ℓ = 3` were used as `i`) gives 3, which still divides 6 and is covered by the `c = 6` sweep.
  * 11-C: odd `P_pre` at the td-7 seed, `gcd(4, 2·odd) = 2`.

  **If `pdeg_P` meant the *grown* full degree**, extra primes appear (`gcd(4m, i·P)` can be 8, 10, 12, …). That reading is not the N3 formula: N3’s td-7 instance uses pole *exponent* 4, not the current `pdeg` after steps. A later-created vertex can only *add* a constraint (intersection / shrink). The original pole remains alive until the clash (Case B otherwise). Conservative = complete on this reading.

  **Slop, not a hole:** “`i ∈ {2,4} (ℓ | 2)`” conflates first-charge exponent with `ℓ`. The large values they need are the pole degrees themselves. Gate OB5b checks a handful of examples, not the lattice above; the lattice is in the prose.

### 7. Severity: clear — Claim (5). The four near-misses are exact. The 11-B `3 ∤ ν` exclusion is load-bearing and correct.

- File: `TOWER-TD11.md:341-351,227-231`; `cases/tower_td11.py:227-231`
- How checked.

  | # | claim | replay |
  |---|---|---|
  | 1 | `ν_X = 3`, cap 6: `k = 6 | 6` | `6 % 6 == 0`, and `legal(3, 3)` is false (`gcd(3,3) ≠ 1`). Exact. |
  | 2 | `ν_X = 2`, cap 6: `ν | c²` holds, 2-adic saves it | `2 | 36`; dens of `(2a−3)/12` are `{4,12}`, neither `| 6`. Exact. |
  | 3 | 11-A cap 4 has a nonempty prefix menu; lattice still refuses X | `k | 4` is strictly larger than td-7’s `k | 2`; CAP-DEN on the `1/4` lattice has no odd-`ν ≥ 3` escape (finding 5). |
  | 4 | `ν_X = 3` clears the `5/8` (`2/3 > 5/8`) and dies by `3 ∤ 16` | `2/3 > 5/8`; `3` does not divide `16 = 4²`. Exact. |

  Two domain-excluded escapes that belong in the same ledger and are not listed: `(c,ν) = (4,2)` (11-A domain, even `ν` at `w = 2`) and `(c,ν) = (*,1)` (X-interval / §12(iv)). Neither is live. The clash does use the letter domain, not just the gap order — X4 is the right load-bearing row.

### 8. Severity: residual — several local honesty nits that do not reopen a kill.

- `den(α_1) | c` is false for the divisor-closure candidate `c = 1` (`den(3/2) = den(5/2) = 2`). The `c = 1` sweep still refuses X (wrong registers, right answer). OB1b’s “`den(α_1) = 2` divides every cap candidate” silently drops `{1}`.
- Gate A4 / stacks only go to length 2 and `ν < 16`; the `v_2` identity does not need more.
- §1 still says realization is “the ONLY question for 11-A”; §7.7 claims the dichotomy closed it. Stale round-1 sentence.
- §6 still says “PROSPECT (not yet a theorem)” above a §9 theorem. Status header is the round-2 one; fine if read as history, confusing if read as the live claim.
- D5 is cited for “drops irreversible” as if it governed all steps. D5 is the *neutral* ledger `M' = gcd(ℓ, u+1)`. Charged/st96 steps raise `M` (already at budget 5). On the 11A-RES branch this does not matter (finding 4).
- Packet law for type `(2,3)` matches `t9_15_direct.json:662,671-675` (`α_1 = 3/2`, top `5/2`, `m^2 = σ_0 λ^3`). Type `(2,5)` is the same Z1 formula, not an inference from `(2,3)`. That part of OB-1 is clean.

---

## The six requested attacks

| # | attack | result |
|---|---|---|
| 1 | OB-7 algebraic `ν`-closure (`den\|c ⇒ ν\|c²`) plus 2-adic residuals | **Holds** on the intended X-family. Stronger iff `den\|c ⇔ 2ν \| c(ν+1)` is an identity. Residuals `{2,4}` and resonant `5/4` refuse as written. `ν = 1` is the only extra residual; it is outside the X-interval. Finding 5. |
| 2 | Lemma 11A-RES: hunt a route where `M` does not drop | **No such in-window route.** Unique seed clean cell, `M' = 1` for every legal `ℓ`, lands on frozen `(2,1)`, `v_2` is an identity. Written `M'` formula is the `n=1` law; conclusion survives. Finding 4. |
| 3 | OB-6 21+347+69, all depth-`≥2` gaps `< 1/2`; 10-state adversarial sample | **Budget-5 slice holds; budget-9 claim is false.** Spot-check below. Finding 1. |
| 4 | OB-5 conservative `{1,2,4}/{1,2,6}/{1,2}` complete? | **Yes**, for seed pole-pattern `pdeg_P`. Largest candidate is the right conservative object. Finding 6. |
| 5 | Perimeter + near-miss ledger, especially 11-B `3 ∤ ν` | **Exact** on the four listed rows. Two unlisted domain-excluded escapes (`(4,2)`, `ν=1`) are not live. Finding 7. |
| 6 | Census implication as emptiness certificate for a nonexistent compiler | **Not earned as written.** Conditional on discipline + entry mapping, *not* on the §12 perimeter. Finding 2. |

### Ten-state spot-check (OB-6)

| # | state | what was checked | result |
|---|---|---|---|
| 1 | `(3,2)` seed | full `chain_steps` (13 rows) | unique clean `D3n2nu2`, ratio `5/2`, `M2=1`; st96 ratios `∈ {11/8,7/4,10/7,8/5,3/2}`; every `dp/ℓ ≥ 2`; boundary mult `= 2` is the `5/8` itself |
| 2 | `(3/2,2)` seed | full `chain_steps` (6 rows) | no clean; max st96 ratio `8/5`; `m ≥ 7/2` |
| 3 | `(4/3,3)` seed | gate OB6b/c (347-state close) | `R* = 3 < 6`, no at-seed resonance. Independent full menu not re-derived here (this close dominates the 122 s gate) |
| 4 | `(3,1)` | full `chain_steps` (2 rows) | exactly `{D3n2nu2, neutral-drop}`; `M2 = 1` |
| 5 | `(2,1)` | full `chain_steps` (1 row) | empty clean `n ≥ 2`; only `neutral-drop`. L-A freeze, engine-confirmed |
| 6 | `(3,3)` | clean cell only | `D3n2nu2` still `M2 = 1` |
| 7 | `(3,2)` st96 child `(2/3,3)` | destination of `l2e0k1S1x0nu16` | reached by ratio `11/8`, `m = 24`, `λ = 5`. Depth 1, gap `11/32 < 1/2` (already in the frozen 11-A charged menu) |
| 8 | `(3,2)` st96 child `(6/7,7)` | destination of `l2e0k5S5x0nu8` | `M` *raised* to 7, ratio `7/4`, `m = 28`. Illustrates D5-not-for-charged (finding 8) and that budget 5 already leaves `M = 2` |
| 9 | `(3,2)` budget-9 closure | `close_with_cells(..., 9)` | **743** states, `w ≤ 6`, `M ≤ 97`. Not in the gate. Finding 1 |
| 10 | large-`M` budget-9 states | attempted R* sweep | not finished; clean ratios bounded by `7/2 < 4` given `max num(w) = 6`; st96 ratios at `M ~ 97` were not enumerated |

No spot-checked in-perimeter state produced a depth-`≥2` gap `≥ 1/2` or a multiplier `< 2` on a `ν ≥ 2` step. The boundary multiplier `2` is the `5/8` resonance, correctly treated as the unique depth-1 exception.

---

## What the theorem actually delivers

On the object that was honestly checked — the three L6 entries, H8 = `P/μ` with `μ | M`, the one-step scope §3.2 menus, the `α`-lattice den-criterion under the conservative caps, the unpadded 11-A `5/8` with the forced `μ = 1` comparison, and the budget-5 px2 closures — **every synchronized spine dies at the tower tier.** The `Pi = 5^k` family is in the inhabited window and dies by the same Case-A / CAP-DEN refusal; no depth cap is required *for those spines*. That is the NF-D byproduct, and it is the right reason to run this clash before a depth bound.

It does **not** deliver a compiler emptiness certificate for a td-11 class-B/C book that has not been enumerated, and it does **not** close configurations that leave the budget-5 / px2-menu / merge-free-seed slice. Those must stay OPEN.

Suggested status line after errata: *entry-tier clash proved on the budget-5 px2 slice, within a corrected §12; census implication is a per-row template, not an emptiness certificate.*

Machine gate: `python3 cases/tower_td11.py` — exit 0, `RESULT: ALL 46 TOWER-TD11 CHECKS PASS` (122 s). Companion gates not rerun. No git commit.
