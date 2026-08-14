**VERDICT: SOUND-WITH-ERRATA — the panel-closure claim holds: every E5-corrected td-7 class-B/C cell dies at the tower tier; the in-flight WIN correction (entry hosts only `l|2` with ratio `≤ 8/5` → max gap `2/5`) re-derives cleanly and is the true load-bearing step; AM and E5F closed forms hold; five adversarial witnesses match the frozen table by independent exact recomputation; no third kill-breaking realization class found (the two prior gaps `M_U=4` and neutral insertions stay closed). Errata: the written menu-ratio “sup = 2 over the full 69-state closure” is false as a raw menu fact (counterexample ratio `5/2`), and two uniform-mode lemma checks are vacuous/tautological — neither touches the kill.**

Reviewer: Grok 4.5 (hostile referee). Date: 2026-08-14.
Target: `TOWER-UNIFORM.md` + `cases/tower_check.py` uniform mode.
Under review: PANEL-CLOSURE THEOREM — every cell of the E5-corrected td-7 class-B/C book (BOOK-OFFAXIS §11a, 17 cells) dies at the tower tier (4 promoted certificates + 13 witness instantiations), full perimeter, reading-independent. The 4 certificates are not re-reviewed; focus is the lemmas, witnesses, perimeter, and gates.
Method: line-read of `TOWER-UNIFORM.md` and `uniform_mode` / `UNIFORM_*` in `cases/tower_check.py`; independent exact `Fraction` re-derivation of WIN (entry menu, growth, resonant audit, parametric identities, 242 path-state max gap), AM (entry menu + M=1 absorption + all M≥2 path first-charged), E5F (charged/pad closed forms + minimal-pad ≡ −2 + family `kbar_U=1` ≡ −1 + m=23 pad-only); adversarial recomputation of five witness rows; perimeter hunt for a third realization class beyond the two prior kills (`M_U=4`, neutral insertions); `python3 cases/tower_check.py` (**1550/1550 PASS**, exit 0, final line `UNIFORM (17 cells): THEOREM`). No other repo file modified. No git.

---

## Summary judgment

The theorem is true for the stated perimeter. The panel-constant clash (imported, promoted) plus L-A / AM / WIN / E5F plus one E5-legal witness row per remaining cell is a coherent kill: every realization’s level-1 window `(gap(X), 5/2)` is empty of chain-2 death gaps, first-charged is in `{(A),(C)}` with `i=2` (or joint-cap `k|2` under insertions via N1–N4), and the universal A/B/C + N1–N4 blocks fire. The in-flight WIN correction is correct and necessary; the older “menu-ratio sup = 2 everywhere” slogan is not.

---

## Findings (worst first)

### 1. Severity: erratum — WIN ingredient (i) overclaims “menu-ratio sup = 2 over the full 69-state closure”; the load-bearing entry bound is correct and the window stays empty

- File: `TOWER-UNIFORM.md:95-111`; `cases/tower_check.py:1571-1607`
- Claim (authors): every non-resonant step has `l d_q/d_p ≤ 2` (sup attained by `(10,5) l=4`); entry deg-4 hosts only `l|2` steps with ratio `≤ 8/5`, so entry children have gap `≤ 2/5`; non-entry parents have deg `≥ 8`, so deeper children have gap `≤ 1/4`.
- How checked (re-derived from scratch).

  **Death-gap identity.** On a framed step with parent full-degree `D` and step data `(d_p, d_q, l)`,
  ```
  gap = d_q / D_child = d_q · l / (D · d_p) = (l d_q / d_p) / D = ratio / D.
  ```

  **Entry (the load-bearing correction).** At `(w,M)=(3/2,2)`, `D=4`. St 8.4 forces `l|2`, so `l ∈ {1,2}`. Exact entry menu (px2):

  | step | `l` | cell | ratio `l d_q/d_p` | child gap `= ratio/4` |
  |---|---:|---|---|---|
  | (C) st96 | 2 | (20,16) | **8/5** | **2/5** |
  | (A) st96 | 2 | (21,15) | 10/7 | 5/14 |
  | st96 | 2 | (7,5) | 10/7 | 5/14 |
  | pure-b l2e1 | 2 | (1+2ν, ν+1) | ≤ 6/5 (at ν=2) | ≤ 3/10 |
  | neutral-drop | 1 | — | 3/2 | 3/8 |

  Max entry child gap is exactly `2/5`, attained only by (C). And `2/5 < 1/2 ≤ gap(X) = (ν_X+1)/(2ν_X)` for every `ν_X ≥ 2`. **This is the corrected WIN step; it holds.**

  **Growth.** Over the full 69-state P0 menu, every step has `d_p/l ≥ ν ≥ 2` (0 counterexamples: clean/ndrop, pure-b, and all st96). So `D` at least doubles each step; every non-entry parent has `D ≥ 8`. No deg-shrinking steps (`l > d_p`) exist in the menu.

  **Menu-ratio sup = 2 is FALSE as a raw 69-state fact.** Independent scan of all non-resonant steps on the 69-state closure finds exactly one ratio `> 2`:
  ```
  st96 l5e0…nu2(14,7) at state (3/5, 5):  ratio = 5·7/14 = 5/2.
  ```
  Ratio `= 2` is attained (including by `(10,5) l=4` at `(1/2,4)`), but it is not the menu supremum. Resonant clean `n=2` also has ratio `5/2` (handled under (iii)).

  **Why the kill still holds.** Even with raw-menu `R_max = 5/2`:
  - non-entry: gap `≤ (5/2)/8 = 5/16 < 1/2`;
  - resonant states (exactly 3): min framed realization deg `≥ 6`, child gap `≤ (5/2)/6 = 5/12 < 1/2`;
  - the `(14,7)` host `(3/5,5)` is reachable only at `λ = 5` (budget saturated), so the `dl=2` step is budget-blocked; framed enum records 0 accepted `(14,7)` steps;
  - full framed path enum (242 path-states): max gap `= 2/5` exactly, attained only on paths whose first charged step is (C).

  The gate’s `ratio_bad` audit only sees framed accepted steps (where non-resonant sup is indeed 2), so it passes while the writeup’s “full 69-state closure” sentence is overstated.

  **Erratum to write.** Replace “every non-resonant step has ratio `≤ 2` (sup at `(10,5)`)” by: (i′) entry hosts only `l|2` with ratio `≤ 8/5` → max gap `2/5`; (i″) raw-menu non-resonant ratio is bounded by `5/2` (one st96 outlier + resonant cleans), and with growth every non-entry gap is `≤ 5/16 < 1/2`. The sharp global maximum on realizations remains `2/5` (witness (C)).

  The WIN *conclusion* — window `(gap(X), 5/2)` empty — stands.

### 2. Severity: suggestion — two uniform-mode “lemma” checks are rubber stamps; the content is checked elsewhere, but the named lemma lines do not compute

- File: `cases/tower_check.py:1613-1616`, `1733-1738`, `1725-1727`
- Claim: E5F charged closed form is machine-checked at lemma level; negative controls catch tampering; m=23 has no legal direct.
- How checked.
  - `check("E5F charged closed form: …", True)` — the boolean is the constant `True`. No lattice, no formula evaluation.
  - Negative controls: `not (0 >= 1)` and `Fr(4*7-43,15)==-1 and not (-1>=1)` — tautologies that cannot fail.
  - m=23 “no legal direct”: only asserts `UNIFORM_EXPECTED[(90,135,67,45)][1] == 'pad nu=45'` (frozen-string equality), not a recomputation that every direct at that cell has `n < 1`.

  Per-cell witness rows *do* verify the charged closed form on every direct, and the independent recompute below confirms m=23’s sole cellmap direct `(11,23)` has `n = −1`. The defect is check quality, not math.

  **Suggestion.** Replace the charged E5F lemma check with the same lattice used for the pad form; replace negative controls with a mutation of a live witness that must fail; recompute m=23 directs from cellmap + E5F rather than reading the frozen table.

### 3. Severity: clear (attack fails) — AM absorbing-M lemma: first-charged menu of every class-C realization is exactly `{(A),(C)}`

- File: `TOWER-UNIFORM.md:83-93`; `cases/tower_check.py:1458-1482`
- Claim: from ENTRY, St 8.4 forces `l|2`; `l=1` neutral; charged `l=2` menu is `{(A),(C)}`; other charged first steps land `M=1`, which is absorbing; class-C needs `μ0|M_U` with `μ0≥2`, unreachable from `M=1`.
- How checked.
  - Entry charged menu: exactly four charged steps — (A)`(21,15)→(2/3,3)`, (C)`(20,16)→(3/4,4)`, st96`(7,5)→(2,1)`, pure-b`→(3,1)`. The last two land `M=1`. The first two both have `λ=2` and `i=4/l=2`.
  - `M=1` absorbing: `gcd(ν, nν+1)=1` on the full lattice; from `(3/2,1)` the menu has **no** charged step at all.
  - Neutral-only reachability from entry: only states `{(3/2,2),(3/2,1)}`. Charged menus with `M_child≥2` from those states: only (A) and (C).
  - Path proof: among all framed paths ending at `M≥2`, first charged cell is in `{(21,15),(20,16)}` in **155/155** cases; **0** counterexamples.

  AM holds. Class-C cannot open with pure-b/eps and later climb back to `M≥2`.

### 4. Severity: clear (attack fails) — E5F closed forms: minimal-pad ≡ −2, family `kbar_U=1` ≡ −1, m=23 pad-only

- File: `TOWER-UNIFORM.md:113-133`; `cases/tower_check.py:1611-1628, 1710-1717`
- Claim: on E5-matching charged arrival, `n=(X ν_U − ν_G)/μ0`; on clean pad, `n=((ν_U+1)X − μ0 kbar_G)/μ0`; minimal pad `ν_U=μ0−1` gives `n=X−kbar_G=−2` identically; family `kbar_U=1` directs `ν_U=(m−1)/2` give `n=−1`; m=23 has no legal direct (pad `ν=45`, `n=2`).
- How checked (independent derivation).

  **Charged.** With `w=(kbar_G(μ0−1)+2)/(μ0 ν_G)` and `ρ_U=1/μ0`,
  ```
  kbar_U = w ν_U + 1/μ0,
  n = ν_U kbar_G − ν_G kbar_U = (X ν_U − ν_G)/μ0,   X := kbar_G − 2.
  ```
  Verified on all 12 direct witness rows (and the five adversarial recomputes below).

  **Pad.** `kbar_U = w(ν_U+1)` gives `n=((ν_U+1)X − μ0 kbar_G)/μ0`. At `ν_U=μ0−1`:
  ```
  n = (μ0−1)kbar_G − (kbar_G(μ0−1)+2) = −2.
  ```
  Identity holds for all panel frames `(X,kbar)∈{(3,5),(4,6),(5,7)}` and all `μ0∈[2,30)`.

  **Family `kbar_U=1`.** On the `2/(2k+1)` family (`kbar_G=6`, `X=4`, `ν_G=3m−2`, `μ0=m`, `w=2/m`): charged `ν_U=(m−1)/2` has `kbar_U=(2ν_U+1)/m=1` and
  ```
  n = (4·(m−1)/2 − (3m−2))/m = −1
  ```
  for every odd `m∈{15,…,25}` — including the three named instances `(7,15),(9,19),(11,23)`.

  **m=23 pad-only.** Cellmap at `w=2/23` is exactly `{(11,23)}`; charged offset `n=−1`. First legal pad `ν=45` has `kbar=4`, `n=2`, matching the frozen witness. No legal direct.

  E5F is SOUND. The seven-row rollout erratum it encodes is correctly diagnosed (prior review).

### 5. Severity: clear (attack fails) — five adversarial witness instantiations match the frozen table by independent recomputation

Picks (adversarial: remaining family members, even-`μ0` N1 cell, biggest cell):

| cell @ μ0 | why adversarial | independent best | frozen | match |
|---|---|---|---|---|
| `(66,99,49,33)@17` | family remaining (m=17) | direct ν=25, deg 541450, n=3, i_G=31850, P=15925, maxgap=5/14, first=(A) | same | **YES** |
| `(74,111,55,37)@19` | family remaining (m=19) | direct ν=47, deg 116090, n=7, i_G=6110, P=3055, maxgap=2/5, first=(C) | same | **YES** |
| `(82,123,61,41)@21` | family remaining (m=21) | direct ν=31, deg 553350, n=3, i_G=26350, P=13175, maxgap=2/5, first=(C) | same | **YES** |
| `(21,35,17,7)@4` | even-μ0 N1 pad cell | pad ν=7, deg 214200, n=1, i_G=53550, P=26775, maxgap=2/5, first=(C); refuted min pad ν=3 n=−2 | same | **YES** |
| `(90,135,67,45)@23` | biggest cell, pad-only | pad ν=45, deg 36773550, n=2, i_G=1598850, P=799425, maxgap=2/5, first=(C); refuted direct ν=11 n=−1 | same | **YES** |

Additional checks on each: E5F closed form identity; `n≥1`; `P=i_G/2≥2` integral; first-charged in `{(A),(C)}`; maxgap `≤ 2/5`; prefix-menu deltas `D_f g − kbar` positive-integral for `g∈{3/2,1,2}` at every witness vertex; deg transport from 4 along the framed path (and ×ν_U for pads).

Biggest-cell ledger (independent):
```
entry deg 4
 → (C)(20,16) l=2     deg 40
 → (119,35) l=4       deg 1190
 → (247,39) l=7       deg 41990
 → (253,23) l=13      deg 817190   (refuted direct kbar_U=1, n=−1)
 → pad ν=45           deg 36773550 (n=2)
```

All five are complete clash instantiations. No freeze-table drift.

### 6. Severity: clear (attack fails) — perimeter: no third kill-breaking realization class found

- Claimed quantifier: filed routes, all arrivals/`M_U`, free characteristics, neutral padding, zero-cost insertions, terminals, E5-reroutes.
- Prior gaps closed: `M_U=4` (now `M%μ0==0`, e.g. M=8 for μ0=4 on `(21,35)`); neutral insertions (N1–N4 in certificate suites, N4 identity in WIN).
- Hunt for a third class (constructive attempts):

  | candidate | status | why not a kill-break |
  |---|---|---|
  | raw-menu ratio-5/2 step `(14,7)` | blocked | host only at λ=5; even if fired at D≥8, gap≤5/16<1/2 |
  | free pure-b non-minimal ν | covered | path enum samples min ν (worst gap, min deg); parametric pure-b ratio `≤3/2` |
  | first-charged after pure-neutral prefix | empty | only (A)/(C) with M₂≥2 from neutral-reachable states |
  | M_U proper multiple of μ0 | covered | witness enum uses `M%μ0==0`; clash uses μ0 not M_U for i_G |
  | resonant n≥2 clean | covered | only n=2, 3 states, max path gap 1/4 |
  | deg-shrinking steps | absent | 0 menu steps with `l>d_p` or `d_p/l<2` |
  | post-first-charged large gaps | absent | 0 path vertices with gap>2/5 after first charged |
  | entry insertion before (A)/(C) | helps WIN | raises D, shrinks (C) gap below 2/5; N3 restores `k|gcd(4,2P)=2` for odd P |
  | non-integral kbar paths | out of perimeter | BOOK requires integral kbar; enum correctly drops them |
  | class B | empty by trust set | §11a; not re-audited here |
  | alt H5a reading / U_7C | moot | 15/17 cells Q-only; (9,15)+(10,15) die in both; forced-nu empty |

  **Closest residual (not a third class):** uniform mode does not re-run N1–N3; it imports insertion closure from the five certificate suites run earlier in the same gate and from WIN’s N4 identity. That is a process dependency on already-reviewed material, not a new unquantified realization family. Stacked/interleaved insertions remain under the joint-cap + gap-shrink arguments of N3/N4 (prior Sol final review: SOUND).

  I did **not** find a third class that escapes the quantifier and survives the clash. If one exists, it is not among the patterns that killed the two prior versions.

### 7. Severity: confirmed — 1550-gate suite green; reading-independence claim is consistent with the book structure

```
python3 cases/tower_check.py
→ 1550/1550 PASS, exit 0
→ UNIFORM (17 cells): THEOREM
→ certificates: t9_15_direct, t9_15_trunk, t10_15, t58_87, t25_35 all OBSTRUCTED
→ 21/21 perturbations
```

Census parity on the 16 uniform cells: raw sum 234; plus `(9,15)`’s 4 raw → 238, matching §11a. Equality counts match `UNIFORM_CENSUS` row-by-row in the gate.

Reading-independence (as claimed, not re-derived from H5a): the tower verdict on the two dual-reading cells is already certified; the other 15 exist only under the promoted Q-reading, so every coherent reading’s td-7 book is empty at this tier. U_7C is correctly declared moot for td-7.

---

## Re-derived WIN (clean form, for the erratum)

**Lemma WIN.** Every realization vertex death-gap is `≤ 2/5 < 1/2 ≤ gap(X)`; the level-1 window `(gap(X), 5/2)` is empty.

*Proof sketch (machine-audited).*
1. **Entry.** `D_{P2}=4`, `l|2`, max ratio `8/5` at (C) → max child gap `2/5`.
2. **Growth.** Every P0 step has `d_p/l ≥ 2`, so non-entry parents have `D≥8`.
3. **Raw ratio bound.** Non-resonant menu ratios are `≤ 5/2` (unique outlier `(14,7)`); resonant cleans are exactly n=2 at 3 states with min realization deg ≥6. In all cases child gap `< 1/2`.
4. **Parametric families.** Pure-b: `l(ν+1)/(lν+ε) ≤ (ν+1)/ν ≤ 3/2`. Insertions (N4): `(ν+1)/(D_prev ν) ≤ 3/8` for `D_prev≥4`.
5. **gap(X).** `(ν+1)/(2ν) ∈ (1/2, 3/4]` for all `ν≥2`.
6. **Enumeration.** 242 framed path-states, max gap `= 2/5` (only (C)).

The in-flight correction (entry `l|2`, ratio `≤8/5`, max gap `2/5`) is the sharp step; “sup = 2 on the full closure” is not needed and not true.

---

## What was not re-reviewed

- The four promoted certificates’ internal C3/Case-C/N1–N4 writeups (scope: instances only).
- §11a under-enumeration as a census question (trust set; beyond-perimeter charged steps are to be flagged, not absorbed).
- Formal-tier claims outside the filed route perimeter (convergence, P-realizability, global polynomiality) — correctly disclaimed in §4.

---

## Gate transcript (tail)

```
RESULT: ALL CHECKS PASS (incl. perturbation suite) -- all certificates validated;
tower tier verdicts: t9_15_direct.json: OBSTRUCTED, t9_15_trunk.json: OBSTRUCTED,
t10_15.json: OBSTRUCTED, t58_87.json: OBSTRUCTED, t25_35.json: OBSTRUCTED,
UNIFORM (17 cells): THEOREM
```
(1550 PASS, 0 FAIL, exit 0.)

---

## Disposition

| item | verdict |
|---|---|
| Lemma L-A (chain-1 freeze) | SOUND (gcd + shape; not the focus, checked) |
| Lemma AM (absorbing M + first-charged menu) | **SOUND** |
| Lemma WIN (window emptiness) | **SOUND-WITH-ERRATUM** on ingredient (i) writeup; conclusion holds |
| Lemma E5F (offset law + closed forms) | **SOUND** (lemma-level charged check vacuous; content holds) |
| 13 witness instantiations (5 spot-checked adversarially) | **SOUND** |
| Perimeter (third class hunt) | **no kill-breaking third class found** |
| Reading-independence | **consistent** with claimed book structure |
| 1550-gate suite | **PASS** |
| **Panel-closure theorem** | **SOUND-WITH-ERRATA** — promote after WIN (i) rewrite + optional check hardening |

No cell resisted. The td-7 off-axis book is empty at the tower tier for the stated perimeter.
