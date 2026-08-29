# LL1-R4 full-actual-floor packet — hostile software review

**Reviewer:** Fable 5 (different-model hostile software reviewer)
**Date:** 2026-08-29
**Basis HEAD:** `ccb6cd52eeab95f169b40f0a48668c3acd7a607e` (verified; packet committed at this basis; `cases/`, `ladder/`, `FALLACY.md`, and the evidence files are git-clean before and after this review)
**Packet:** `cases/landing_ledger_ll1_r4_20260829/`
**Producer report:** `xmodel/landing-ledger-ll1-r4-full-actual-floor-software-report-sol56-20260829.md`
**Environment:** Python 3.9.6, macOS; all executions and all mutations ran in an isolated full-relative-layout mirror under `/tmp` (no repository file was modified or rewritten by this review).

## Verdict

`PASS`

Maximum safe software promotion: **promote as the LL1-R4 typed software
consumer of the already-promoted carrier inputs, at LL-1 scope only** (td=6,
m=2, one fixed fibre, two-pole path union): explicit carrier typing, the
canonical piecewise floor, the exact four-mover replay, and the 13->7
reduced-superset inventory, all `LOWER_FLOOR_ONLY` with `attainment=false`.
Nothing here promotes occurrence, realization, attainment, candidate-grammar
completeness, a degree ceiling, td!=6, Keller, or JC2; generic MP8/MFE stays
`REPRESENTATIVE`; the 26-shape/351-route engine record stays fixture-cited
(not re-run, per instruction and per the packet's own scope firewall). No
counterexample found.

charge_basis={"delta":"2/3","branch":"q>=2","flag_count":1,"citation":"ladder/BOOK-OFFAXIS.md:489"}

(The only exit-price change this packet applies: each of the four movers
charges exactly one nonzero flag, `mults=(3,)`, at nonintegral
`delta = X/m - kbar = 17/3 - 5 = 2/3`, under the canonical nonintegral branch
`ceil(2*delta) = 2`; the basis is declared by the pinned BOOK-OFFAXIS floor
block, not inferred.)

## 1. Custody — every declared hash reproduced byte-exactly

Producer report file
`c2d627a002d9bb60cb467e65b5ffebc8969dba9bcde0ded1fb1426f5db72fbf5`; sealed
body = first 6753 bytes =
`f645432f935fd39515ae3c59f8c4835dac8181fe5b6eed051e2012a04438b43a`; the
declared neighbor cuts at 6752/6754
(`ad01c681db638c889bd602c2b89dff70cb8d522a61bae85b24865dd6445f3d91`,
`a126013be309f339b15c63f49c53baa4765bdfa6d37c8db33e7d56bd87a97cb5`) also
reproduce, so the byte convention is pinned, not guessed.

`MANIFEST.sha256` hashes
`23e56710ad5ba6e2b8a0c9e8e2a4cb802f7ef545dadea22164f9aacdb185998a` and
verifies 6/6 against the working tree:

```text
314947ef2068b736d57119b2dca1f59b1a868781f30e0d673d4fb86b3f5416a0  ll1_compiler.py
09a731b7dea0b71442fda193f31a245a4e3210c143ef2193b6f3ad7c7d019dd5  ll1_validator.py
32cf3fddb828b0651b3c5ee1ab246c006d45450d0138b3165307631fd0dfd744  test_ll1_r4.py
25e3fd3c0300e53b041054dd06e0bddd60fc9e0dfc4153af07e276aac8a78c68  INVENTORY.md
7715083c811a3d9fd011aeed245c23ede31c56d9fbf055a571c11bfe08aaef04  out/ll1_book.json
29bc125bea86dc35d9d181d445b4927babb154ce88e9c9720efb60d0ee33c689  out/ll1_summary.json
```

The packet directory contains exactly these six files plus `out/` — nothing
unmanifested.

All seven canonical source pins reproduce on the current bytes
(`ladder/BOOK-OFFAXIS.md b3993495…`, `ladder/SHEET6-MULTIPOLE.md f11cbe1f…`,
`ladder/SHEET6-2POLE.md c66ff941…`, `FALLACY.md c63bd167…`,
`ladder/REDUCTION.md 29270ff6…`, `ladder/SHEET6-DEPTH.md ad9ced64…`,
`ladder/SHEET6-DEPTH-REVIEW.md 841fa120…`), exactly matching report §3.

All eight evidence pins reproduce, exactly matching report §4 and
`EVIDENCE_PINS`:

```text
82d2f6c3eb2c3985569da428def3d5c2e125ca5b0aa29ebfc7973b68ee843a7a  m2-two-pole-full-actual-first-separation-theorem-r1-sol56
f7853d39a17fd7329feaec101f1767ef5edddd07a2f0d5f8030a0cb023f95efe  m2-two-pole-full-exit-attachment-primary-opus5-76c
32402983a357ef25de363a9532a47fa9a2cb4b4e8e1bab918d6f6e07a3fb3a10  …cross-comparison-sol56-opus5-76c
1b3be27da8ba495d80cbf473d844055583a672d136ccea40611dfe9fc0b7023e  …hostile-review-grok46-76c…b
aaa7496bd6182bd124935b8534307ad3167fffe9393efad3e56cf349942ddeb7  m2-exit-safe-floor-legacy-reprice-r1-sol56
3e3cea4aa6e0bda907dd291a0f1e62e1ffa744e84463e5596c2e0e0e408a166b  …stable-hostile-rereview-opus5…b
205e7f5825604e0e334d1a822b13a595dfe6b9ce06d0f011b199a0ddcb725a1e  frozen LL1-R3 out/ll1_book.json
6ca098b8145f091884d7f11ab1d6aac49dadaab91a6ba7ed18f7c022efce99b5  frozen legacy reprice check.py
```

All six sealed-body prefix pins recomputed independently with `head -c`
(21235→`0c808734…`, 61389→`2fe6a14c…`, 9484→`1026e3a2…`, 32456→`3be6ab6b…`,
12149→`2d873e68…`, 34525→`7b23f8ca…`): all match `EVIDENCE_BODY_PINS`.

Frozen-R3 baseline re-hashed and equal to report §6: compiler `839d3801…`,
validator `76cfec34…`, test `2cebe74b…`, inventory `5acc4b79…`, book
`205e7f58…`, summary `7c7cfd3b…`; legacy checker `6ca098b8…`. The R3 packet
and the legacy checker are byte-for-byte unchanged at this basis.

## 2. Execution replay — ordinary and `-O`, all four programs

All runs `PYTHONDONTWRITEBYTECODE=1`, rc=0, stderr empty, ordinary and `-O`
stdout byte-identical, every hash equal to the producer report:

```text
compiler   stdout SHA-256  f1a5f8756f1775f1df46fb776615c6fcd2ad023d498c8d91ebe8b5cdecdc7998
validator  stdout SHA-256  5001bdea3c9ddd59c1d0bd61ec4f8c3548151f233ed4aee9fb181e3dfd716088
acceptance stdout SHA-256  a078cdd81f4d735c283db3dcb528a84f90fb4ccd8fd3cd02b3af0d57b0c54eb9
                           (LL1-R4 acceptance passed: 166 failed: 0; ALL TESTS PASS (166 checks))
legacy chk stdout SHA-256  4498beacf2f119d4f3d1b1750e857549e98f76900899983dd32db5d4e5da0011
                           (verdict PASS_EXACT_REPRICE; run standalone in both modes,
                            and again by the suite as a subprocess in both modes)
```

Compiler banner confirms `7 canonical source pins + 8 evidence pins verified,
49 consumed-clause anchors present` (49 = `len(CONSUMED_ANCHORS)`, counted).

**Determinism / manifest:** the compiler was executed three separate times in
the mirror (ordinary, `-O`, and after mutation-restore); each run emitted
`out/ll1_book.json` and `out/ll1_summary.json` byte-identical to the committed
artifacts (`7715083c…` / `29bc125b…`), so `MANIFEST.sha256` re-verifies 6/6
after regeneration. `canonical_json` (sorted keys, fixed separators,
ensure_ascii) plus a FIFO BFS with sorted emission makes the output
order-deterministic; no absolute path appears in the book (checked by the
suite and confirmed by grep).

**No `assert` anywhere** in `ll1_compiler.py`, `ll1_validator.py`, or
`test_ll1_r4.py` (grep; the only occurrences are prose). Every gate raises
`LLError` or collects failure strings, so `-O` cannot strip any check —
consistent with the byte-identical `-O` stdout observed on all four programs
and with mutation M4 below, which was run under `-O` and still failed closed.

## 3. R4 delta isolated and read in full

`diff` R3→R4: compiler 537 diff lines, validator 111, test 193. The delta is
exactly: the four type constants; `EVIDENCE_PINS`/`EVIDENCE_BODY_PINS` and
their fail-closed verifier; `EXPECTED_CHANGED_CELLS` /
`EXPECTED_REMOVED_ALIVE` / `EXPECTED_FULL_ALIVE`; the
`FULL-ACTUAL-FIRST-SEPARATION` trust entry; source pins expanded 5→7 (adds
SHEET6-2POLE.md and FALLACY.md; BOOK-OFFAXIS/REDUCTION re-pinned at the
current carrier-rider bytes) with six new `R4/*` anchors; the typed price
functions (`representative_nonzero_floor`, `full_actual_nonzero_floor`,
`representative_epsilon_zero_floor`, `typed_exit_price`,
`representative_af2_price`); carrier threading through
`dirty_cells`/`residue_enumeration`; `_alive_inventory` /
`_legacy_r3_alive_inventory` (hash-gated) / `repricing_audit`; and the
book/summary additions. All R3 mathematical machinery is byte-identical to
the reviewed R3 packet. The R3-inherited middle sections contain no pricing
code (grep-verified).

The floor implementation matches the pinned canonical text exactly
(`ladder/BOOK-OFFAXIS.md:479-489`): `delta = X/m - kbar > 0` per nonzero up
direction; floor `delta` when delta is a positive integer, `ceil(2*delta)`
when nonintegral; AF2 stays valid for one selected ray (`REPRESENTATIVE`);
the rider at lines 505-509 explicitly licenses "the LL-1 reprice at exactly
four nonintegral cells, changing total floors to `3,3,3,2` and the
reduced-superset inventory `13 -> 7`", so the packet's expected constants are
anchored to hash-pinned promoted canonical text.

## 4. Independent recomputation (no packet code imported)

I wrote a standalone checker that reads only the two hash-gated book JSONs
(frozen R3 `205e7f58…`, new R4 `7715083c…`) and re-derives everything with its
own arithmetic. All checks pass:

- **16 unique legacy cells** extracted from the frozen R3 book (16 exactly,
  no key collisions). For every key, my independently recomputed
  representative price (`max(1,ceil(delta))` per flag + legacy epsilon term)
  equals the frozen R3 `lam`. This is per-cell frozen parity, one level
  stronger than the packet's own alive-inventory parity gate.
- **All 16 full prices** recomputed; where the cell appears in the R4 walk,
  R4's `lam` equals my full total and R4's `lam_representative` equals my
  representative total and the frozen R3 value.
- **Exact four-mover exhaustiveness:** recomputing both floors over all 16
  keys yields exactly four movers — `(17,5)@nu2 2→3`, `(51,15)@nu7 2→3`,
  `(85,25)@nu12 2→3`, `(119,35)@nu17 1→2`, each with a single nonzero flag at
  `delta=2/3` and epsilon/zero floors `1,1,1,0` (independently:
  `(17/3-5)/2=1/3→1`, `(17/2-5)/7=1/2→1`, `(17-5)/12=1→1`, eps=0→0). The
  16-cell delta spectrum is `{1, 1/2, 1/3, 1/4, 1/6, 2, 2/3}`; `2/3` is the
  only value where the two rules differ (`2δ=1` at `δ=1/2` lands on the
  integral seam and does not move), so the four-mover set is sharp, not
  coincidental.
- **Graph-coverage argument verified empirically:** the R4 (full-carrier)
  walk's cell set is a strict subset — 11 of the 16 legacy keys; the five
  pruned keys are the three eps-bearing movers (now priced over budget where
  they fired) and the two deep l=7 cells `(55,11)@nu5`, `(247,39)@nu19`.
  Since per-cell full ≥ representative and pure-b/neutral steps are
  unchanged, every full-walk state is reached along a representative-walk
  path with pointwise smaller lam, so the full walk can never emit a cell key
  outside the legacy 16: auditing over the legacy key set is exhaustive for
  both graphs. Confirmed: `R4 keys ⊆ R3 keys`.
- **Inventory delta:** ALIVE inventories recomputed from both books' terminal
  records: 13 → 7; removed rows exactly
  `("2/7",7,3,ALIVE)`, `("1/2",2,4,AF)`, `("1/2",4,4,AF)`, `("2/11",11,4,AF)`,
  `("2/13",13,4,AF)`, `("2/5",5,4,AF)`; **added rows: none**; survivors
  exactly the seven expected. The book's `repricing_audit` tables equal my
  recomputation.
- **Terminal arithmetic re-derived from scratch** for every terminal row in
  both books (`j=M(1-w)∈N*`, `psi=ceil(1/(1-w))-1`, budget `td-1-psi`,
  verdict and slack): all agree.
- **Lower-floor vs attainment metadata:** a full-tree walk of the R4 book
  found every `attainment` key `false` (none `true` anywhere), and
  `LOWER_FLOOR_ONLY` on the policy, the carrier-theorem provenance, every
  component, every audit row, and the two scope-firewall strings.

**Independent cross-implementation agreement:** the frozen legacy checker
(`check.py`, differently authored, hash-pinned, reads only the frozen R3
book) independently reports the same 16 unique cells, the same four movers
with `delta=2/3`, `nonzero 1→2`, totals `2→3,2→3,2→3,1→2`,
`zero_separate 1,1,1,0`, `old_alive 13`, `new_alive 7`, and the identical
removed/new row lists, verdict `PASS_EXACT_REPRICE`, stdout hash `4498beac…`
pinned by the acceptance suite in both modes. This is genuinely independent
replay, not same-code.

## 5. Carrier-leakage attack — no leakage found

- Call-site audit: `typed_exit_price` is called only from `dirty_cells`
  (carrier threaded), `repricing_audit` (both carriers, labeled), and
  `representative_af2_price` (REPRESENTATIVE). The floor functions are called
  nowhere else. The synthetic CAP probe, merge/entry/chain layers, and the
  epsilon paths cannot reach the full floor.
- Book scan: the FULL token appears only in `pricing_policy`,
  `provenance.carrier_theorem`, the four `repricing_audit.changed_cells`
  rows, the `pricing.nonzero` components of residue-step cells, and the three
  `SUFFIX/dirty-*` records. Zero occurrences in merge/entry/chain records or
  the synthetic probe.
- Per-component: all 17 nonzero components in the emitted book are typed
  `FULL_ACTUAL_FIRST_SEPARATION` / cert `FULL-ACTUAL-FIRST-SEPARATION` with
  floors matching my recomputation; both epsilon components and all 14
  pure-epsilon rows are `REPRESENTATIVE` under their legacy rules
  (`legacy-AF2-epsilon-zero`, `legacy-P0-pure-epsilon`).
- Suffix cert chains carry the FULL rule exactly when `mults` is non-empty
  (checked for all suffix records; non-dirty suffix records never carry it).
- The reverse direction (epsilon priced by the full rule) is excluded by
  construction and by mutation M6 below.
- `typed_exit_price`'s non-positive-defect raise is unreachable for
  enumerated cells (the strict NE law `m·dq < dp` is checked before pricing,
  which forces `delta = kbar(dp-m·dq)/(m·dq) > 0`); it is defensive only.

## 6. Negative mutation battery (mirror only; restored and re-verified green after each)

The packet's own battery (A6 readers-level source drift, evidence tamper
R4-12, book tampers, 166 checks) passes. I added nine disk- and code-level
mutations of my own:

| # | mutation | result |
|---|---|---|
| M1 | flip 1 byte in the carrier-theorem evidence file | compiler rc=1 `EVIDENCE DRIFT`; validator rc=1, same |
| M2 | flip 1 byte in the frozen R3 book | compiler rc=1 `EVIDENCE DRIFT`; legacy checker rc=1 `LL1 input hash drift` |
| M3 | flip 1 byte in the frozen legacy checker | compiler rc=1 `EVIDENCE DRIFT` |
| M4 | flip 1 byte in BOOK-OFFAXIS, run under `-O` | compiler rc=1 `SOURCE DRIFT` (fail-closed survives `-O`) |
| M5 | full floor → always `ceil(2*delta)` (kill integral branch) | compiler rc=1 `changed-cell set drift: ((7,5,2),(17,5,2),(20,16,5),(21,15,7),(51,15,7),(85,25,12),(119,35,17))` — the integral branch is load-bearing and the audit sees the three integral-delta cells that would move |
| M6 | leak the FULL floor into the epsilon direction | compiler rc=1 `representative total drift at (7,5,2,…)` — first eps-bearing cell caught |
| M7 | delete one row of `EXPECTED_CHANGED_CELLS` | compiler rc=1 `changed-cell set drift` — the audit genuinely compares |
| M8 | edit one digit in the committed `out/ll1_book.json` | validator rc=1 `repricing audit drift against exact representative/full replay` |
| M9 | **coordinated mutant**: M5 + all six repricing-audit gates deleted | compiler still rc=1: the R3-inherited P0 first-step menu pin fires (`P0 first-step dirty menu drift: [(20,16),(21,15)]` — mutated (7,5) prices out of the menu); neutering that too trips a fourth gate (`(2/3,3) terminal budget drift`). The suite additionally holds its own copies of the mover/inventory constants, the committed-book determinism check, the manifest, and the independent legacy-checker stdout hash. |

Defense in depth is real: a pricing error must simultaneously defeat the
audit constants, the R3-inherited menu and boundary-terminal pins, the frozen
R3 alive parity, the suite's independent constants and committed-artifact
comparison, the manifest, and the independent legacy checker.

## 7. Validator-independence assessment

`ll1_validator.py` imports `ll1_compiler` and re-runs its functions; its
re-derivation is independent of the **emitted book**, not of the compiler
code (same structure as the reviewed R3 packet). This is not a defect but
should not be over-read: the compensating genuinely independent gates are the
frozen R3 book (hash-gated, per-cell parity confirmed by me), the pinned
canonical rider carrying `3,3,3,2` / `13 -> 7`, the committed artifacts under
`MANIFEST.sha256`, the suite's own constant pins, and above all the frozen
legacy checker — a separate implementation whose output hash the suite pins
in both modes. M9 demonstrates the layered gates empirically. The validator's
R4-specific checks (per-row carrier typing, floors metadata, totals,
pure-epsilon firewall) read the book JSON directly and are meaningful even
under a same-code compiler.

## 8. Minor observations (no repair required)

1. `EVIDENCE_BODY_PINS` are mathematically redundant given the full-file pins
   (a prefix of hash-pinned bytes is determined); their value is certifying
   the *declared seal convention* against the bytes, which I confirmed
   independently. Fine as designed.
2. The canonical `3,3,3,2` / `13 -> 7` rider is bound by substring anchor
   (`R4/four-cell-totals`), not parsed into the audit; a coordinated
   constants+rule mutation would not trip the anchor itself. Caught anyway by
   the M9 gate stack; recorded for completeness.
3. `representative_af2_price` has no internal caller (exported audit hook
   only). Harmless.
4. The producer report's §5 "both rc=0; byte-identical stdout" claims are all
   reproduced exactly; no discrepancy of any kind was found between report
   and artifacts.

## 9. Scope firewall check (FALLACY.md discipline)

- Carrier/attainment: `REPRESENTATIVE` and `FULL_ACTUAL_FIRST_SEPARATION`
  are kept as distinct emitted types with the alias `FULL_ACTUAL_EXIT`
  declared floor-valued; `attainment=false` everywhere (full-tree walk).
- Floor/attainment: every price is emitted as `LOWER_FLOOR_ONLY`; the book,
  summary, inventory, and scope-firewall strings all repeat that no
  attainment or occurrence is asserted; `ALIVE` remains a reduced-superset
  predicate.
- Per-ray/exit-set: each nonzero flag is charged once (one component per
  `mults` entry; the four movers each have `flag_count=1`); carrier
  distinctness is supplied by the promoted theorem input, which this packet
  consumes and does not re-prove.
- No occurrence/completeness inference: the engine record remains
  fixture-cited with the `NOT re-run` scope string, enforced by the validator.

## 10. Files read

Every file under `cases/landing_ledger_ll1_r4_20260829/` (compiler,
validator, test suite, INVENTORY.md, MANIFEST.sha256, both out/ JSONs), the
full R3→R4 diffs of all three executables, the frozen R3 packet files (hashed;
book parsed and independently recomputed), the frozen legacy checker (read;
run four times), the producer report, and the pinned carrier-rider passages of
`ladder/BOOK-OFFAXIS.md`. The historical heavy engine was not re-run and no
occurrence/completeness claim is inferred from its fixture counts.

<!-- END-SEALED-BODY::landing-ledger-ll1-r4-software-hostile-review-fable5-ccb-20260829 -->

## Seal (outside the sealed body)

Convention: the sealed body is the byte range from the first file byte through
and including the newline terminating the unique `END-SEALED-BODY` marker
immediately above. This seal section is excluded.

```text
sealed-body bytes      18898
sealed-body SHA-256    42eed3cc26ae4b74d0be79910f7cc38f7b28e640d316e3f0d36faab968d84ce8
cut at 18897 bytes     7c507ddaa32bdcd8ca8fa4efb43df8cb45b1fa48dcbfc986730dc772690938d1
cut at 18899 bytes     1c4703c4fe80379340b59c49955bee3225a5daf7cae9526edefebcd8290b0491
```
