# Stable-basis hostile rereview: M2 legacy full-exit safe-floor repricing R1

Date: 2026-08-29
Reviewer: Opus 5, independent adversarial mathematical referee
Basis: `c3598b92598c1596e6c6331f4c877619b432a115`
Target: `xmodel/m2-exit-safe-floor-legacy-reprice-r1-sol56-20260829.md`
Run: retry B (attempt A emitted no report and no verdict; nothing from it was
consumed, inherited, or assumed here)

## 0. Verdict

```text
UNTYPED_NO_PROMOTION
```

The arithmetic layer is **correct and independently reproduced**, including one
control the producer did not run. The carrier layer is **not** discharged.

- Every numerical claim under review replays exactly: both target seals, the
  canonical checker stdout under ordinary and `-O` modes, all 16 unique LL-1
  cell keys, the four changed cells, the retained zero summands, the ten dirty
  `td=12` rows with their `8/8/8/8` charges against budgets `9/8/6/2`, and the
  13-to-7 alive inventory. I found no arithmetic error.
- The decisive gate fails. LL-1 R3 is a **two-pole** packet (`td=6, m=2`, poles
  `P1,P2`, `Λ=(3,3)`). Its `Σλ ≤ td−1−ψ` budget is therefore governed by the
  multipole first-exit theorem (MFE), not by the singleton-pole Section-9 (4.3).
  In MFE, `lambda_F^exit` is **defined** as `Σ_(d∈D_F) price(F,d)` — one chosen
  Statement-7.3 witness per direction-orbit — and MFE explicitly quarantines
  "a claim that every actual cv flag is one of the selected witnesses".
- The full-set upgrade therefore needs MFE's own §4 escape hatch, whose
  load-bearing premise is the ambient orbit-tree attachment lemma. The frozen
  hostile review of MFE classifies that lemma as `BLOCKER` and states
  "Automatic promotion of current two-pole or MP8 consumers: NOT AUTHORISED".
- The upgrade needs a **strictly stronger** unlanded hypothesis than the legacy
  book: the strong form of the required lemma (covering every flag of
  `T_(a,cv)`), where the AF2 book needs only the weak form (selected directions
  and their 7.3 witnesses). That asymmetry is the finding.

The producer's own §0/§2/§6.1 name this risk honestly, and its recommendation to
quarantine LL-1 is right. But §2 discharges disjointness by asserting "the
first-separation/no-remerging partition", and at `m=2` that assertion **is** the
blocked object. `FULL_ACTUAL_EXIT` is declared, not proved. Per the standing
rule that a conditional correct calculation is not a pass when its actual LL-1
consumer is untyped, the weakest combined disposition governs.

No `charge_basis=` line is emitted. See §11.

## 1. Custody

Task specification, read and hashed before any other work, and re-hashed
immediately before this verdict:

```text
e470d5a66bb10be2cac04352e5d17cdd86808e18f37f6107265d6ba0c31dcc11
  xmodel/m2-exit-safe-floor-legacy-reprice-r1-stable-hostile-rereview-opus5-20260829a-prompt.md
```

Both readings agree. `git rev-parse HEAD` returned
`c3598b92598c1596e6c6331f4c877619b432a115` at both checkpoints.

### 1.1 Frozen 14-file perimeter, before and after

Command (identical both times):
`shasum -a 256 -c` against the declared list.

| # | file | declared SHA-256 | before | after |
|---:|---|---|:--:|:--:|
| 1 | `xmodel/m2-exit-safe-floor-legacy-reprice-r1-sol56-20260829.md` | `aaa7496b…4ddeb7` | OK | OK |
| 2 | `cases/m2_exit_safe_floor_legacy_reprice_r1_20260829/check.py` | `6ca098b8…ce99b5` | OK | OK |
| 3 | `cases/landing_ledger_ll1_r3_20260829/out/ll1_book.json` | `205e7f58…725a1e` | OK | OK |
| 4 | `xmodel/m2-arity-law-place-conservation-source-audit-sol56-20260829.md` | `05f68f4b…5784d84` | OK | OK |
| 5 | `xmodel/m2-arity-law-…-hostile-review-fable5-20260829.md` | `56e95db5…6174a34d` | OK | OK |
| 6 | `xmodel/sigray-section9-source-audit-sol-ultra-20260828.md` | `2763d970…89459933` | OK | OK |
| 7 | `xmodel/sigray-section9-source-audit-hostile-review-gpt55-20260828.md` | `0729a576…233e6b5bad` | OK | OK |
| 8 | `xmodel/sigray-multipole-global-first-exit-partition-sol-ultra-20260828.md` | `86b491ad…8bc83a8` | OK | OK |
| 9 | `xmodel/sigray-multipole-global-first-exit-partition-hostile-review-gpt56-20260828.md` | `ac49c025…5198cc04` | OK | OK |
| 10 | `xmodel/landing-ledger-ll1-r3-provenance-repair-fable5-20260829.md` | `f501bf91…7bff9aa6` | OK | OK |
| 11 | `xmodel/landing-ledger-ll1-r2-hostile-review-grok46-20260829.md` | `8f56d1e4…218c8b0` | OK | OK |
| 12 | `ladder/BOOK-OFFAXIS.md` | `40104334…70faaaa` | OK | OK |
| 13 | `ladder/REDUCTION.md` | `6bea12cc…83bdf2c39` | OK | OK |
| 14 | `refs/sigray_full.pdf` | `9bf9f032…e1623ae` | OK | OK |

14/14 OK before, 14/14 OK after. No `INPUT_MUTATED` condition arose.

### 1.2 Producer-cited sources outside the frozen 14

The target's §1 pins seven further files. I re-hashed each; all match the
values the target prints, so its citation custody is sound:

```text
599e2a91…584271  xmodel/m2-td12-u1-trunk-consumer-primary-grok46-20260829.md
91b36515…51f25c0f xmodel/m2-td12-u1-trunk-consumer-hostile-review-opus5-20260829.md
6f214a75…c00a038d7e cases/m2_td12_u1_trunk_consumer_grok46_20260829/trunk_consumer.py
dd09069b…ee8f6d90 xmodel/sol-h5a.md
9f4526f2…c79145f14 xmodel/sigray-multipole-selected-orbit-attachment-repair-gpt56-20260828.md
f55a00f5…2e94e216bb xmodel/sigray-multipole-selected-orbit-attachment-hostile-fable5-20260828.md
```

Note for the record: items 1–3 of that list carry the exhaustiveness of the
`td=12` thirteen-edge menu and are **not** in the mandated frozen perimeter.
My `td=12` conclusions are arithmetic on the ten dirty rows; the claim that the
menu has exactly thirteen rows is inherited, not re-derived (§12).

### 1.3 Target seals

```text
full-file  aaa7496bd6182bd124935b8534307ad3167fffe9393efad3e56cf349942ddeb7   VERIFIED
body       2d873e680cfdc464fc0bc707aec5c072ba9310ee0600a98786643c0ca8c93ac5   VERIFIED
body bytes 12149 of 12321 total                                              VERIFIED
```

The body convention resolves unambiguously: bytes `[0,12149)`, i.e. through and
including the newline after `*End of sealed report body.*`. The two neighbouring
cuts give `db1ded73…` (12150) and `7e42e5f3…` (12148), neither of which is the
declared value, so the convention is pinned rather than guessed.

## 2. Reproduction of the checker

```text
$ python3    cases/m2_exit_safe_floor_legacy_reprice_r1_20260829/check.py   # rc=0, stderr empty
$ python3 -O cases/m2_exit_safe_floor_legacy_reprice_r1_20260829/check.py   # rc=0, stderr empty
$ cmp        -> STDOUT IDENTICAL
$ shasum -a 256 (both) -> 4498beacf2f119d4f3d1b1750e857549e98f76900899983dd32db5d4e5da0011
interpreter: CPython 3.9.6 (Clang 15.0.0)
```

This equals the declared canonical stdout hash. The `-O` comparison is
*meaningful* rather than vacuous: `grep -n assert` on the checker returns
nothing, and every guard is the explicit `require()` helper (`if not condition:
raise RuntimeError`), which `-O` does not strip. Had the guards been `assert`,
the `-O` run would have proved nothing; they are not, so it does.

## 3. Independent arithmetic reconstruction

All reconstruction below was written from the formulas, not by importing the
checker, to catch shared-code error.

### 3.1 `td=12` dirty menu (ten rows)

From `dp = ε+ν(k+2)`, `dq = 1+ν(k+1)`, `E = 2dq−dp`, `κ̄ = 9dq/E`, `X = 9dp/E`:

| ε | k | ν | dp | dq | E | κ̄ | X | δ each | NE old | NE safe | zero | total |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 7 | 21 | 15 | 9 | 15 | 21 | 6 | 6 | 6 | 0 | 6 |
| 0 | 1 | 25 | 75 | 51 | 27 | 17 | 25 | 8 | 8 | 8 | 0 | 8 |
| 0 | 2 | 5 | 20 | 16 | 12 | 12 | 15 | 3 | 6 | 6 | 0 | 6 |
| 0 | 2 | 17 | 68 | 52 | 36 | 13 | 17 | 4 | 8 | 8 | 0 | 8 |
| 0 | 4 | 13 | 78 | 66 | 54 | 11 | 13 | 2 | 8 | 8 | 0 | 8 |
| 0 | 8 | 11 | 110 | 100 | 90 | 10 | 11 | 1 | 8 | 8 | 0 | 8 |
| 1 | 1 | 2 | 7 | 5 | 3 | 15 | 21 | 6 | 6 | 6 | 3 | 9 |
| 1 | 1 | 8 | 25 | 17 | 9 | 17 | 25 | 8 | 8 | 8 | 1 | 9 |
| 1 | 2 | 4 | 17 | 13 | 9 | 13 | 17 | 4 | 8 | 8 | 1 | 9 |
| 1 | 4 | 2 | 13 | 11 | 9 | 11 | 13 | 2 | 8 | 8 | 1 | 9 |

Every nonzero defect is a **positive integer**, so `L_safe(δ)=δ=⌈δ⌉` and no row
moves. Legacy totals `[6,8,6,8,8,8,9,9,9,9]` reproduce. Confirmed.

The four P1-shaped rows, budgets recomputed from `ψ=⌈1/(1−w_child)⌉−1`,
`budget = 12−1−ψ`:

```text
ν=25 k=1  w'=2/3   ψ=2  budget 9  charge 8  FITS
ν=17 k=2  w'=3/4   ψ=3  budget 8  charge 8  FITS (equality)
ν=13 k=4  w'=5/6   ψ=5  budget 6  charge 8  does not fit
ν=11 k=8  w'=9/10  ψ=9  budget 2  charge 8  does not fit
```

Exactly the first two fit, as claimed and as before repricing.

### 3.2 All 16 unique LL-1 cell keys

`lam` replays as `Σ_j max(1,⌈X/m_j−κ̄⌉) + [ε≥1]·max(1,⌈(X/ε−κ̄)/ν⌉)` on **all
16** cells. Beyond the checker's own test I also verified `total_old` equals the
actual charge increment `to[2]−from[2]` on every cell-bearing edge — an
independent tie between the stored `lam` and the graph. Both hold everywhere.

| cell | l | ε | mults | X | κ̄ | nonzero δ | NE old→safe | zero δ | z | total old→safe |
|---|---:|---:|---|---:|---:|---|---:|---:|---:|---:|
| (7,5)@2 | 2 | 1 | [1] | 7 | 5 | 2 | 2→2 | 1 | 1 | 3→3 |
| **(17,5)@2** | 4 | 3 | [3] | 17 | 5 | **2/3** | **1→2** | 1/3 | 1 | **2→3** |
| (20,16)@5 | 2 | 0 | [1,1] | 5/2 | 2 | 1/2,1/2 | 2→2 | – | 0 | 2→2 |
| (20,16)@5 | 2 | 0 | [1,1] | 5 | 4 | 1,1 | 2→2 | – | 0 | 2→2 |
| (21,7)@3 | 5 | 0 | [2] | 3 | 1 | 1/2 | 1→1 | – | 0 | 1→1 |
| (21,9)@4 | 3 | 1 | [2] | 7 | 3 | 1/2 | 1→1 | 1 | 1 | 2→2 |
| (21,15)@7 | 2 | 0 | [1] | 7 | 5 | 2 | 2→2 | – | 0 | 2→2 |
| (35,15)@7 | 3 | 0 | [2] | 7 | 3 | 1/2 | 1→1 | – | 0 | 1→1 |
| (40,16)@5 | 4 | 0 | [2,2] | 5 | 2 | 1/2,1/2 | 2→2 | – | 0 | 2→2 |
| **(51,15)@7** | 4 | 2 | [3] | 17 | 5 | **2/3** | **1→2** | 1/2 | 1 | **2→3** |
| (55,11)@5 | 7 | 0 | [4] | 5 | 1 | 1/4 | 1→1 | – | 0 | 1→1 |
| **(85,25)@12** | 4 | 1 | [3] | 17 | 5 | **2/3** | **1→2** | 1 | 1 | **2→3** |
| (117,27)@13 | 5 | 0 | [4] | 13 | 3 | 1/4 | 1→1 | – | 0 | 1→1 |
| **(119,35)@17** | 4 | 0 | [3] | 17 | 5 | **2/3** | **1→2** | – | 0 | **1→2** |
| (130,40)@13 | 4 | 0 | [3,3] | 13 | 4 | 1/3,1/3 | 2→2 | – | 0 | 2→2 |
| (247,39)@19 | 7 | 0 | [6] | 19 | 3 | 1/6 | 1→1 | – | 0 | 1→1 |

Exactly four cells move, and they are exactly the four claimed. The mechanism is
sharp: `L_safe` differs from `max(1,⌈δ⌉)` only for nonintegral `δ`, and for
`δ∈(0,1)` only when `δ>1/2`. The book's nonintegral defects are
`{2/3, 1/2, 1/3, 1/4, 1/6}`, and `2/3` is the only one above `1/2`. Nothing else
can move, and nothing else does.

### 3.3 Zero summands and epsilon safety

The three epsilon-bearing changed cells retain `⌈1/3⌉=1`, `⌈1/2⌉=1`, `⌈1⌉=1`
respectively, exactly as the target states, computed with `old_floor` on
`(X/ε−κ̄)/ν`. **No zero/epsilon direction is repriced.** I checked this two
ways: the checker's zero branch calls `old_floor` unconditionally, and for all
five epsilon-bearing cells `safe_floor` would coincide with `old_floor` anyway
(all zero defects are `≤1`), so no silent reprice is hiding behind the choice.
The nine `PURE-B` edges and the eight `NEUTRAL` edges carry their costs
unchanged, which is correct: pure-`b` has `k=lex=Sm=0` and therefore no nonzero
extra direction to reprice, and is priced by the separate collapse rule
`λ_F ≥ ⌈l·w_G/ε⌉`.

### 3.4 `L_safe` monotonicity

`L_safe ≥ old_floor` universally: for nonintegral `δ≤1/2` both are 1; for
nonintegral `δ∈(1/2,1)` it is 2 vs 1; for nonintegral `δ>1`,
`⌈2δ⌉ ≥ ⌈δ⌉+1`; for integral `δ`, both are `δ`. So costs only increase, and the
target's "no newly affordable edge can appear" is sound. The checker's
`new_alive − old_alive = ∅` assertion confirms it empirically.

## 4. The control the producer did not run

The 13-to-7 claim compares an inventory read out of the JSON (`old_alive`)
against one recomputed by the checker's own `terminal_verdict()` on repriced
states (`new_alive`). If `terminal_verdict()` disagreed with the book's verdict
logic, the delta would be an artifact. The checker never tests this. I did:

1. **Verdict-function fidelity.** `terminal_verdict(w,M,charge)` reproduces
   **all 23** frozen `residue_terminals` verdicts with **0 mismatches**
   (10 `ALIVE_FRAGILE`, 9 `TERMINAL-REJECTED`, 3 `ALIVE`, 1 `DEAD`).
2. **Old-cost replay.** Re-running the identical pooled BFS with *old* costs
   yields exactly the book's 23 states — `book_states − old_seen = ∅` and
   `old_seen − book_states = ∅` — and an alive set **equal** to the book's 13
   rows. New-cost replay gives 17 states, 7 alive, 6 removed, 0 added.

So the pooling/BFS machinery is faithful at the frozen basis, and the 13→7 delta
is genuinely attributable to the repricing rather than to the replay model. This
strengthens the target's arithmetic beyond what it claims for itself.

## 5. Pooling legitimacy after repricing

### 5.1 The displayed `(20,16,5)` collision is not a defect

Two cells share `(dp,dq,ν,l,ε,k,mults) = (20,16,5,2,0,2,[1,1])` yet carry
`(κ̄,X) = (4,5)` and `(2,5/2)`. I recovered the governing law and verified it on
**every** cell-bearing step:

```text
E = l·dq − dp,     κ̄ = w_src·l·dq/E,     X = w_src·l·dp/E,     X/κ̄ = dp/dq.
```

`(κ̄,X)` is therefore a function of the **source** `w`, not of the cell alone:
the two rows come from `w_src = 3/2` and `w_src = 3/4`. They are genuinely
distinct frames, `cell_key` separates them because it carries `(κ̄,X)`, and the
template key retains `src=(w,M)`, so no cross-contamination is possible. Their
defects `{1,1}` and `{1/2,1/2}` both price to 2 old and 2 safe, so neither is
among the four changes and the `expected_changed` comparison (which projects to
`(dp,dq,ν)`) is not exercised on an ambiguous key. I confirmed no `cell_key`
maps to records differing in `lam`, `M_child`, or `w_child`; 32 STEP rows give
32 distinct templates, so no dedup collapse occurs at all.

Residual, non-load-bearing: projecting `changed` to `(dp,dq,ν)` for the
set-equality test is a latent fragility, since `(20,16,5)` proves that projection
is not injective on this book. It is inert here.

### 5.2 The two paths to `(2/7,7,4)`

Enumerated exhaustively:

```text
OLD costs -> (2/7,7,3): 1 path   (3/2,2,0)→(3/4,4,2)→(2/7,7,3)  via (119,35)@17 cost 1
OLD costs -> (2/7,7,4): 1 path   (3/2,2,0)→(2/3,3,2)→(2/5,5,3)→(2/7,7,4)
NEW costs -> (2/7,7,3): 0 paths
NEW costs -> (2/7,7,4): 2 paths  both of the above, the first now at cost 2
```

This is exactly the target's §4.1 reading: the repriced `(119,35)@17` edge pushes
its arrival from charge 3 to charge 4, the `(2/7,7,3)` ALIVE row vanishes, and
`(2/7,7,4)` survives because the unchanged boundary route already reached it.
Confirmed.

### 5.3 Is pooling by reduced `(w,M)` still legitimate?

Yes, at the frozen basis, and the target's stated reason is close but not the
cleanest one. The correct argument is that the outgoing template set at a vertex
depends on `(w,M)` only, while the accumulated charge enters solely through the
`≤4` gate, which the replay re-applies. The one real risk is an edge omitted
from the book because it was unaffordable at every visited old charge. Since
costs only increase, no repriced path can reach `(w,M)` below its old minimum
charge — I verified this directly: no `(w,M)` is reached in the new run below its
old minimum, and no `(w,M)` appears in the new run that was absent from the old.
Hence any omitted edge is at least as unaffordable after repricing, and the
pooled replay cannot miss a survivor. Combined with §4's exact old-cost
reproduction, pooling is sound here.

## 6. The safe floor, reconstructed from source

`ladder/BOOK-OFFAXIS.md`, promoted header **"2026-08-29 FULL-EXIT FLOOR
CORRECTION (PROMOTED; attainment remains open)"**, and the arity-law audit §6.2
"Safe-floor lemma" agree verbatim with the checker:

```text
L_safe(δ) = δ        for integral δ>0
            ⌈2δ⌉     for nonintegral δ>0
```

Proof structure (arity audit §6.2), with the type distinctions kept separate:

- `m = mult(p_F,c*) = deg(p_G)` counts **cover-level Puiseux series**, not
  physical places; the place→flag map may be many-to-one (audit §2.1–2.3).
- `E_all(F,c*) = {I_P(u_0(P)) : P ∈ P(G)}` as a set of **distinct flags** is the
  full actual exit set (audit §3), certified by Statement 7.3 (universal in `P`),
  Statement 3.13 (one zero of `d` per ray), Definition 3.3 (no remerging).
- Branch A, `≥2` distinct flags: each `w_H = q_H(τ_H−κ̄) ∈ ℕ*` with `τ_H ≥ D/m`,
  so each `≥⌈δ⌉`, total `≥2⌈δ⌉`.
- Branch B, singleton with `q≥2`: `w ≥ 2δ` and integral, so `≥⌈2δ⌉`.
- Branch C, singleton with `q=1`: **needs full physical-place coverage** to
  exclude place divergence, plus `q=1` to exclude conjugate shedding; then
  `τ_0 = D/m` and `w = δ`, possible only for integral `δ`.

For `δ=2/3` branch C is impossible (`2/3 ∉ ℕ*`), and
`min(2⌈2/3⌉, ⌈4/3⌉) = min(2,2) = 2`. So `L_safe(2/3)=2` is correct **for the full
actual exit set**, and is a floor only — the audit says so twice and BOOK-OFFAXIS
repeats "It is never an attainment theorem". The target respects this throughout;
its §0 and §6.3 explicitly refuse attainment. No floor/attainment fallacy found.

The gap that this floor closes is exactly one unit at `δ=2/3`: a *representative*
witness supports only `w ≥ ⌈2/3⌉ = 1`, because without full coverage branch C
cannot be excluded and `τ_H > D/m` is unconstrained. The entire dispute over the
four cells is that single unit.

## 7. The central gate: which object does LL-1's P0 consumer charge?

### 7.1 What the frozen record actually says

- The book carries **no carrier tag**. Grepping for `FULL_ACTUAL_EXIT`,
  `carrier`, `full-exit`, `witness`, `selected` returns nothing relevant; the
  four hits are `normal_form_representative` in the merge section and a
  `SEC1A/td7-witness` anchor, both unrelated.
- Its only pricing provenance is the clause `P0/AF2-price`, anchored on
  `ladder/BOOK-OFFAXIS.md`:
  `λ_F ≥ Σ_j max(1,⌈X_F/m_j − κ̄_F⌉) + [ε≥1]·max(1,⌈(X_F/ε − κ̄_F)/ν⌉)`.
- `trust_snapshot.AF2` reads: "SHEET6-AF2 sec.2 as consumed by BOOK-OFFAXIS P0
  (**lam price per NE orbit** / free 0-root)".
- The LL-1 R3 scope firewall states in its own words: "**recorded λ are AF2 lower
  bounds**".
- `ladder/BOOK-OFFAXIS.md` states: "The AF2 formulas below remain valid for **one
  selected ray/witness**. They are not automatically the total price of a nonzero
  direction," and requires: "Every P0/P2 consumer must declare one of two types:
  `REPRESENTATIVE` … or `FULL_ACTUAL_EXIT`, which uses the piecewise floor above
  **and proves disjointness before summing**. … The frozen LL-1 R3 book used the
  old values and is quarantined from numerical promotion pending its reviewed
  full-exit reprice."

### 7.2 H-full versus H-representative, decided from sources

**H-full** has a genuine case, and I tested it rather than dismissing it. If
`λ_F` denotes the actual local exit charge and AF2 is merely a weak bound on it
(the `≥` sign invites this), then any stronger bound on the same quantity is
free. Section-9 §4.6 supports this shape: it defines
`E_i = Y_lit(F_i) \ Y_lit(F_(i−1))` as **all** cv vertices first separating at
`F_i`, sets `λ_i^exit = Σ_(H∈E_i) κ_H(π(H)−1)`, proves the `E_i` pairwise
disjoint from uniqueness of the first-separation index, and applies Corollary 7.1
**once** to `{x-side vertex} ⊔ (⊔ E_i)` to get `Σ λ_i^exit ≤ td−1−ψ`. Under that
theorem the upgrade would indeed follow with no new JSON field, because the
`c*`-slice of `E_i` contains `E_all(F_i,c*)` (arity audit §3.1).

**But that theorem is for a singleton pole.** Its own hostile review grades it
"H2 first-separation exit-set repair | **CONDITIONAL PASS** | The difference-set
construction is clean for **a singleton-pole characteristic path**". And §4.6
itself closes: it "makes no claim about the literal `lambda_F` of Notation 9.3".

**LL-1 is not a singleton-pole packet.** `packet = "LL1-R3 (td=6, m=2)"`, header
`Λ=(3,3)`, `m=2`, and `sections.entry[0].poles` lists two poles `P1` and `P2`,
each `(a,b,ν)=(1,1,2)`, with an eleven-record `merge` section. The governing
budget is therefore the **multipole** theorem, where the same symbol denotes a
different object:

```text
lambda_F^exit = sum_(d in D_F) price(F,d).                     (MFE 4.1)
kappa_(H(F,d))*(pi(H(F,d))-1) >= price(F,d),                   (MFE LP)
```

`(MFE)` is derived by applying `C7.1*` **once** to the x-side flag together with
the **witnesses** `H(F,d)` — one flag per direction-orbit. Its explicit
quarantine list contains "a claim that every actual cv flag is one of the
selected witnesses". This is precisely the arity audit's own review-risk #2:
matching notation is not set equality.

So `λ` as consumed by LL-1 is `Σ_d price(F,d)`, the `REPRESENTATIVE` object.
**H-representative is the source-supported reading.**

### 7.3 The escape hatch, and why it does not rescue the upgrade

MFE §4 does contain the bridge H-full would need:

> "If a stronger local theorem prices several distinct cv flags in one
> direction-component, include those flags as a set and use its proved local sum;
> **the same attachment argument** still separates it from every other
> component."

The arity audit's `E_all` with `L_safe` is exactly such a stronger local theorem.
But the hatch is conditioned on "the same attachment argument", and the frozen
hostile review of MFE (GPT-5.6, **PASS-WITH-REPAIR**) classifies that argument as
the blocker:

```text
Ambient quotient/orbit attachment certificate:             BLOCKER
Automatic promotion of current two-pole or MP8 consumers:  NOT AUTHORISED
```

with attack-ledger row "Can a cv witness leave and reattach/remerge with `U`?
Forbidden by the required orbit-tree lemma, but not by MP0–MP1 as presently
stated. **This is the load-bearing gap.**" The review also records: "**AF2 is a
singleton/local pricing theorem; its local direction-distinctness does not itself
update a multipole engine**," and passes the price-to-witness row only because
"**no unproved multiplicity of a *cluster* is being used here**" — which is
exactly what the full-set upgrade introduces.

Two further points make this decisive rather than merely cautious.

1. **The upgrade needs a strictly stronger hypothesis than the legacy book.** The
   review offers its repair in two forms: the strong form, an arborescence
   "containing every transition direction-orbit and **every flag in
   `T_(a,cv)`**", and the weak form, "stated only for the finite set of selected
   directions and their 7.3 witnesses". `(MFE)` with AF2 prices needs only the
   weak form. Charging `E_all` needs the strong form, because every member of
   `E_all(F,d)` — not just one witness — must have attachment `F` and must not
   remerge. Both forms are unlanded, so the legacy numbers and the repriced
   numbers are *both* conditional, but they are conditional on **different**
   hypotheses, and the new one is not implied by the old.
2. **The producer's disjointness justification is the blocked object itself.**
   Its §2 writes: "their full sets are disjoint by the first-separation/
   no-remerging partition … Along a trunk, every such set is assigned to its
   first exit vertex, so sets charged at different trunk vertices are also
   disjoint." At `m=2` the no-remerging/attachment fact is not available: the MFE
   review states the producer of MFE "labels the stronger fact 'divergent
   directions never remerge' without a supporting source theorem", and builds an
   explicit abstract countermodel in which the orbit quotient identifies two
   direction witnesses as one flag, so `λ_F^exit = 2` while `C7.1*` receives
   weight 1. The trunk-disjointness sentence is the singleton-pole §4.6 statement
   applied to a two-pole packet.

The target declares its interpretation ("The td12 and LL-1 calculations above use
that explicit full-direction interpretation") and flags the risk in §6.1. Per the
task's standing instruction, a declaration is not a license, and the fair-open
rule applies: the sources do not settle the bridge, so it fails open.

## 8. Cell-by-cell license table

For each upgraded cell: `l=4`, one nonzero root of multiplicity 3, `X=17`,
`κ̄=5`, `δ = 17/3 − 5 = 2/3`.

| cell | up direction? | NE strict | R1.0 filters | arithmetic `1→2` | full-set carrier proved? | disjointness across directions | disjointness across trunk vertices | license |
|---|---|---|---|---|---|---|---|---|
| `(17,5)@2` | **yes** — gap `δ=2/3>0`, BOOK-OFFAXIS P0 "every extra direction climbs … since its gap `>0` ⟺ NE" | `3·5=15<17`, `ε·dq=15<17` | `dq≡1 (mod ν)`: `5≡1(2)`; `gcd(M,ν)=gcd(1,2)=1` | correct | **NO** — consumer is `Σ_d price(F,d)` (MFE 4.1) | asserted, needs strong orbit-tree lemma (BLOCKER) | asserted from singleton-pole §4.6, not valid at `m=2` | `UNTYPED` |
| `(51,15)@7` | **yes**, same rule | `3·15=45<51`, `ε·dq=30<51` | `15≡1(7)`; `gcd(3,7)=1` | correct | **NO**, same | same | same | `UNTYPED` |
| `(85,25)@12` | **yes**, same rule | `3·25=75<85`, `ε·dq=25<85` | `25≡1(12)`; `gcd(5,12)=1` | correct | **NO**, same | same | same | `UNTYPED` |
| `(119,35)@17` | **yes**, same rule | `3·35=105<119`, `ε=0` | `35≡1(17)`; `gcd(7,17)=1` | correct | **NO**, same | same | same | `UNTYPED` |

`X = κ̄·dp/dq` verified exactly on all four. Every local precondition the AF2 rule
needs is present; the only missing item is the carrier bridge, and it is missing
identically in all four.

## 9. Answers to the six mandated questions

1. **Is the multiplicity-3 nonzero root an up direction in each cell?** Yes, at
   local P0/AF2 scope. `ladder/BOOK-OFFAXIS.md` §10 P0 states the priced extra
   direction "climbs REGULARITY-FREE since its gap `= X_F/mult − κ̄_F > 0` ⟺ NE",
   and all four have `δ=2/3>0` with the strict NE inequalities `m·dq<dp` and
   `ε·dq<dp` verified above. This makes Statement 7.3 available per ray.
2. **Does the charged object contain every distinct actual cv flag below that
   direction, or only one representative?** **Only one representative.** The
   consumer is `(MFE 4.1)`, `λ_F^exit = Σ_(d∈D_F) price(F,d)`, backed per
   direction by a single Statement-7.3 witness via `(LP)`. `E_all` is a different
   object, and MFE quarantines identifying them.
3. **Are different nonzero directions disjoint at the charged vertex?** Claimed
   by MFE ("distinct direction-orbits at one `F` lie in different components of
   `T\U`"), but that claim is itself downstream of the blocked orbit-tree lemma;
   the review's countermodel attacks exactly this by letting the quotient
   identify two directions' cv representatives. Moot for the numerics here — each
   of the four cells has a single nonzero direction (`k=1`) — but it is *not*
   moot for the separation of the nonzero direction from the retained ε summand
   in the three epsilon-bearing cells.
4. **Are full exit sets at successive trunk vertices disjoint by a typed
   first-separation assignment?** **Not proved at `m=2`.** The typed assignment
   exists in Section-9 §4.6 for a singleton-pole characteristic path (conditional
   pass), and the multipole lift is the blocked attachment/injectivity step. The
   producer's trunk-disjointness sentence is transported by analogy, which
   FALLACY.md forbids.
5. **Does Corollary 7.1's single global budget permit all these flags
   simultaneously without double counting?** For the **witnesses**, yes,
   conditional on injectivity — the review passes "Can C7.1* take all selected y
   flags and the x flag at once? Yes once distinctness is proved". For the **full
   sets**, this is unestablished: it requires the strong-form lemma covering every
   flag of `T_(a,cv)`, not merely the selected witnesses.
6. **Is any zero/epsilon direction accidentally repriced?** **No.** Verified in
   §3.3: the zero branch uses `old_floor` throughout; the retained summands are
   `1,1,1`; all five epsilon defects are `≤1` so no reprice could hide in the
   choice; and pure-`b` and neutral edges pass through at unchanged cost.

## 10. Findings against the target, classified

| # | finding | load-bearing? |
|---|---|---|
| F1 | §2's "disjoint by the first-separation/no-remerging partition" and "sets charged at different trunk vertices are also disjoint" transport the singleton-pole Section-9 §4.6 result into a two-pole packet. No-remerging at orbit level is the declared BLOCKER. | **Yes** — this is the whole license. |
| F2 | §4 presents the four upgrades and the 13→7 change as a "verdict change at the frozen LL-1 reduced-superset scope" without declaring the mandatory `REPRESENTATIVE`/`FULL_ACTUAL_EXIT` type that `ladder/BOOK-OFFAXIS.md` requires of every P0/P2 consumer, and without the disjointness proof that the `FULL_ACTUAL_EXIT` type demands. | **Yes.** |
| F3 | §5 states "The td12 and LL-1 calculations above use that explicit full-direction interpretation" — an interpretation chosen, not a consumer identified. The actual consumer is `(MFE 4.1)`. | **Yes.** |
| F4 | The upgrade silently requires the strong form of the orbit-tree lemma while the legacy book requires only the weak form; the target does not note that its conditional perimeter is *larger* than the book's. | **Yes** — it is the sharpest statement of the gap. |
| F5 | Projecting `changed` to `(dp,dq,ν)` for the set-equality test is not injective on this book (`(20,16,5)` occurs twice). Inert here. | No — robustness. |
| F6 | The `td=12` thirteen-row menu exhaustiveness (10 dirty + 2 clean-neutral + 1 pure-ε) is inherited from packets outside the mandated perimeter; the checker reconstructs only the ten dirty rows. The cited Opus review does corroborate "the complete 13-edge one-step menu" and "10 dirty edges", and notes the clean-neutral family is *asserted*. | No — inherited scope. |

Nothing in the target's mathematics is **false**. F1–F4 are license defects, not
arithmetic defects, which is why the disposition is `UNTYPED_NO_PROMOTION` and
not `REFUTED`.

What the target gets right and should be credited with: it refuses attainment
everywhere; it keeps epsilon, pole, and merge arrivals out of the rule; it
correctly reports the `td=12` menu as unchanged with the honest reason
(integral defects, not a repricing accident); its `td=7` control is correctly
computed and correctly labelled a sample; and its §0/§6.1 name the exact hazard
that sinks it.

## 11. Charge declarations

**Withheld.** The FALLACY.md rule permits a `charge_basis=` line only for an
affirmed exit claim, and requires that a basis be declared from a proved
carrier rather than inferred. The four upgraded cells have correct arithmetic
(`δ = 17/3 − 5 = 2/3`, one nonzero direction, `⌈2δ⌉ = 2`) but an unproved
`FULL_ACTUAL_EXIT` consumer, so the branch label and flag count cannot be
honestly filled: under `REPRESENTATIVE` typing the flag count is 1 and the
charge is 1, under `FULL_ACTUAL_EXIT` typing the floor is 2, and the sources do
not decide between them at `m=2`. Emitting a line would manufacture the very
basis under dispute. Typed result: `OPEN`.

For contrast, the legacy values that *are* licensed at the frozen perimeter
remain the AF2 prices already in the book; no new declaration is needed for them.

## 12. Limitations

1. This review is arithmetic plus source reading. No enumerator was run, no
   canonical, ladder, case, guardrail, or operations file was edited, and no file
   other than this report was created.
2. `refs/sigray_full.pdf` was verified by hash only. Printed Statements 3.13,
   7.3, Definition 3.3, and Corollary 7.1 were consumed through the frozen
   Section-9, multipole, and arity-law audits, not re-extracted from the PDF.
   A `pdftotext` re-extraction is a known hazard for stacked fractions and was
   not attempted.
3. The `td=12` thirteen-row menu exhaustiveness and the clean-neutral family are
   inherited from packets outside the mandated fourteen (F6). My `td=12`
   conclusion is: on the ten dirty rows, all nonzero defects are integral and no
   floor moves. That conclusion is unconditional; the row *count* is not.
4. The `td=7` route in target §5 is a three-cell sample, not a reprice of all 17
   `td=7` cells; its `δ ∈ {2, 1/2, 1/3}` all have `L_safe = old`, which I
   confirmed, and the `2+1+2=5` equality is unchanged.
5. The 13→7 inventory is a statement about the frozen LL-1 reduced-superset
   graph. It is not a landing, realizability, ceiling, Keller, or JC2 statement,
   and `ALIVE` remains a conservative superset.
6. Both the legacy and the repriced LL-1 budgets are conditional on an unlanded
   orbit-tree attachment lemma. This review does not resolve that lemma; it
   determines only that the repricing needs a strictly stronger form of it.
7. `jc2-lean` was not entered, enumerated, searched, read, built, modified,
   status-checked, or controlled. No commit, push, web, AWS, install, or heavy
   computation occurred.

## 13. Route to a promotable result

Not required, but the gap is narrow and worth stating precisely. The four
upgrades become licensed if either:

- the **strong** form of the MFE-review orbit-tree lemma is landed — the y-side
  quotient containing every flag of `T_(a,cv)` is a rooted arborescence, `U`
  rootward closed, each direction-orbit a distinct child edge — after which the
  MFE §4 escape hatch applies verbatim to `E_all` and `Σ L_safe ≤ td−1−ψ`
  follows; or
- a two-pole analogue of Section-9 §4.6 is proved directly, giving pairwise
  disjoint first-separation sets `E_i` over the union `U` of both pole paths with
  shared suffixes counted once.

Either would also let the LL-1 book carry an explicit `FULL_ACTUAL_EXIT` field,
which is what `ladder/BOOK-OFFAXIS.md` asks every P0/P2 consumer to declare.

---

Final disposition:

```text
arithmetic layer (seals, checker, td12, 16 cells, zero summands,
  pooling, terminal budgets, 13->7)                         VERIFIED
carrier/disjointness bridge for the four upgraded cells     NOT PROVED
combined (weakest)                                          UNTYPED_NO_PROMOTION
```

<!-- END-SEALED-BODY::m2-exit-safe-floor-legacy-reprice-r1-stable-hostile-rereview-opus5-20260829b -->

## Seal (outside the sealed body)

Convention: the sealed body is the byte range from the first byte of this file
through and including the newline that terminates the unique end marker line
`<!-- END-SEALED-BODY::m2-exit-safe-floor-legacy-reprice-r1-stable-hostile-rereview-opus5-20260829b -->`.
That marker occurs exactly once. Everything in this section lies outside the
sealed body and is excluded from the hash.

- Sealed-body bytes: `34525`
- Sealed-body SHA-256:
  `7b23f8cadfc8e4afcbebd64add68449bd8e08f2cacfc6dede26d651dc681e302`
