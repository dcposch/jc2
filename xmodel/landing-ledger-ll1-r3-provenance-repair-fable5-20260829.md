# LANDING-LEDGER LL-1 R3 — provenance repair: exact source pins, honest engine-parity gate, fail-closed drift firewall

Date: 2026-08-29 (UTC). Lane: Fable 5, producer (same lane as R2).
Charge: the narrow provenance/test-quality repair required by the R2
hostile review. The R2 mathematics PASSED at LL-1 scope and is not
re-litigated here; R2 is treated as immutable and its packet re-verified
untouched this session. R3 changes only the provenance layer and the A1
engine-parity gate.

Status: **SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW.** R3 cannot promote
itself and does not authorize AWS or canonical promotion.

## 0. Inputs (read in full; all hashes computed this session)

- `xmodel/landing-ledger-ll1-r2-repair-fable5-20260829.md` (my R2 report) —
  full `19df817d055f4124fb92ce5ba2d08d7610814a9c3c11d8fcf4da6a0711457530`,
  body `29e892dab4fa31c6ff122706fc751cde32108b200af30f116dce9949b3fecd2b`
  (matches its printed self-hash and the review's pin).
- `xmodel/landing-ledger-ll1-r2-hostile-review-grok46-20260829.md` —
  full `8f56d1e4f2b159bbddf170010d9ac85337639e00e3b4ea537e0cc218a7b9bcf0`,
  body `3673da4736301d645edc4ab08ea3cb60b1563df6c565200eac7cdaa57972472f`
  (matches its printed self-hash). Verdict PASS_AT_LL1_SCOPE with two
  non-killing items: (i) the R2 pins for `ladder/BOOK-OFFAXIS.md` and
  `ladder/REDUCTION.md` do not reproduce; (ii) A1's engine-parity check is
  the tautology `all(2*nu+2 == 2*nu+2 ...)`.
- R2 packet `cases/landing_ledger_ll1_r2_20260829/` — IMMUTABLE, untouched;
  `shasum -a 256 -c MANIFEST.sha256` re-run this session: all six files OK.
- Campaign sources, read at the cited sections and pinned byte-exact in §1
  (`jc2-lean` untouched; no global `git status`; no workspace-wide search).

No web, AWS, Singular/msolve/Sage/PARI, no commit/push, no canonical edit.
All computation is bounded exact-rational Python inside the fresh packet
directory plus targeted `git show`/`git diff` on the two re-pinned files.

## 1. Deliverables and pins

- Packet: `cases/landing_ledger_ll1_r3_20260829/` (`ll1_compiler.py`,
  `ll1_validator.py`, `test_ll1_r3.py`, `INVENTORY.md`, `MANIFEST.sha256`,
  `out/ll1_book.json`, `out/ll1_summary.json`).
- This report.

Packet manifest (verified with `shasum -a 256 -c`, all OK):

    839d3801757b40f405bde985766ff702d0f9f116860b126fb3d866c5cf8080b6  ll1_compiler.py
    76cfec348a5eed39e1fa0f9b95c0b761741234d33275eac06bc2c45b6e0f7cae  ll1_validator.py
    2cebe74b47b5ecd29e467a8d5f7c34bf7dae7dcef71aabe5f10872ab718d851a  test_ll1_r3.py
    5acc4b79a85173820c69f83cf01a758eb3deb57e8ee53f08b87bb6cbf87faf72  INVENTORY.md
    205e7f5825604e0e334d1a822b13a595dfe6b9ce06d0f011b199a0ddcb725a1e  out/ll1_book.json
    7c7cfd3b8feab21ec4d08da8a765458ffbbf43652e57c56c7da6069ef6cb9a04  out/ll1_summary.json

Source pins (mandate 1) — verified at compile time AND validate time by the
packet itself; any drift fails closed:

| file | R3 pin (exact current bytes) | status vs R2 |
|---|---|---|
| `ladder/SHEET6-MULTIPOLE.md` | `93adb7acedf4cf0fd56ffc68e4571649a04eab12e1271431449a79465a964bcb` | unchanged (R2 pin reproduces) |
| `ladder/SHEET6-DEPTH.md` | `ad9ced6c0420902f8cf63edf3636bed8633be511e925f208d24a24c35d71036d` | unchanged (R2 pin reproduces) |
| `ladder/BOOK-OFFAXIS.md` | `7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77` | **RE-PINNED** |
| `ladder/REDUCTION.md` | `0a88db0d136001a6c18343f941a80ecfaef5ceffcbe84e05c739a853d13c1936` | **RE-PINNED** |
| `ladder/SHEET6-DEPTH-REVIEW.md` | `841fa120fa2ae801578834c7b52c5aad600eb48df73b683e1db5c954caf7f7ac` | **NEW** (engine-record fixture for the A1 gate) |

The two re-pinned values equal the R2 hostile review's session hashes
exactly, so that review's clause re-derivation ("the P0/P1/§4/T7 sentences
the packet actually consumes are present in the files now in `ladder/`")
applies to precisely the bytes R3 pins. R2's stale pins are recorded in the
book under `provenance.r2_superseded_pins` for the audit trail and are
never verified.

Provenance reconstruction of the R2 miss (targeted `git show`, no status):
HEAD blobs hash `26f0c64e8cb80ee6bac62e69f91d21dea74b01187150fbc786551f6885a35eb0`
(BOOK-OFFAXIS) and `f0fca49811349483c437d674ab819065eb09500330516d161978868c71bf6371`
(REDUCTION). R2's printed pins (`34f5ea9d…`, `6b9376e0…`) match neither
HEAD nor the current worktree: R2 hashed intermediate uncommitted
working-tree states that no longer exist anywhere. The uncommitted
HEAD-to-worktree edits (93 and 298 diff lines respectively) comprise: the
2026-08-28 root-classification correction and mixed-merge-at-`m=2` header
(this IS the `MRW` certificate the packet consumes), the §3 reframing of
the 2691 rows as diagnostic skeletons, the R2.0/R2.1 case-I root-window
displays, §8 Step 4's corrected branch and the td-7 "RETRACTED HISTORICAL
CLAIM" header, the 2026-08-29 stage_rp_census correction (69-not-70
states; resolvent identity), the REDUCTION frontier overlay, T7
source/hypothesis expansions (SOL-PROP58/Chau; audit `47eef092…`), and the
CRITICAL 5 rewrite. None of these touches the content of a consumed LL-1
clause; several are corrections R2 had already adopted.

## 2. Consumed clauses re-derived against the exact pinned bytes (mandate 2)

Every clause below is (a) anchor-gated: its verbatim text is one of the 43
`CONSUMED_ANCHORS` substrings the compiler and validator require in the
pinned bytes, failing closed if absent; and (b) re-derived: the R3 compile
re-runs the R2 machinery (`entry_menu`, `dirty_cells`, `terminal`,
`residue_enumeration`, `classify_family_I`) against nothing but these
formulas, and every reviewed output is unchanged.

- **T7 (REDUCTION.md §T7).** `Λ(F) = a_F b_F αβ/ν_F`, `M_F = b_F`, ν-menu
  `ν|α ∧ ν|bβ−1` or `ν|β ∧ ν|bα−1`, `Λ ≥ β ≥ 3`, finite menu; SOL-PROP58/
  Chau every-fibre replacement still cited for Prop 5.8. Re-derived entry
  at `td=6, m=2` with MP4 forcing: unique on-axis `Λ=(3,3)`, type `(2,3)`,
  `(a,b,ν)=(1,1,2)` both poles, `kbar=5`, `(M,ρ,w0)=(1,1,2)`; and the
  `td=7` pointer `Λ=(3,4)`, `(1,1,2)+(1,2,3)`. **Decision unchanged.**
- **BOOK-OFFAXIS §4.** "td 6, 9 (all m); m=4 td 12: off-axis sector EMPTY
  (0 raw entries)." — the `OFFAXIS-EMPTY-TD6` certificate. **Unchanged.**
- **P0 (BOOK-OFFAXIS §10).** Transport `κ̄_F = l·w_G·dq/E ∈ ℤ (ν ≥ 2)`,
  `w_F = l·w_G(dq−1)/(νE)`, `M_F = gcd(dp, dq)`; AF2 price
  `λ_F ≥ Σ_j max(1, ⌈X_F/m_j − κ̄_F⌉) + [ε ≥ 1]·max(1, ⌈(X_F/ε − κ̄_F)/ν⌉)`;
  finiteness `E | l·num(w_G)·T`, `T := Sm + l − ε(1+k+lex) ≥ 1`; pure-b
  collapse `w_F = l·w_G/(l−ε)`, `M_F = gcd(l−ε, ν+1)`; and the printed
  four-escape menu from `(3/2, 2)`. Re-derived first step: exactly
  `{(21,15) λ2 → (2/3,3), (20,16) λ2 → (3/4,4), (7,5) λ3 M=1,
  pure-b λ3 M=1}`, no resonant survivor — the printed menu, with the AF2
  formula values honoring the printed `λ ≥` floors. **Unchanged.** (P0
  menu completeness per state remains CITED, exactly as in R2.)
- **P1 (BOOK-OFFAXIS §10).** `ψ = ⌈1/(1−w_G)⌉ − 1`, shared budget
  `Σ λ ≤ td − 1 − ψ` (St 9.4 (25)), `j := M_G·(1 − w_G) ∈ ℕ*`,
  `ψ = ⌈M/j⌉ − 1`; P1's own worked examples ("w = 2/3: ψ = 2, budget
  td − 3; w = 3/4: ψ = 3, budget td − 4") give at `td=6` exactly the
  packet's boundary budgets 3 and 2. Re-derived terminals and the whole
  budget-exhaustion residue book: 2 boundary + 2 deeper slack-1 + 9
  equality-fragile ALIVE rows and 9 route-dead states, byte-identical to
  the reviewed R2 rows. **Unchanged.**
- **Supporting clauses from the two re-pinned files** (all anchor-gated,
  all consumed as in R2, none decision-changed): R1.0 (`dq ≡ 1 (mod ν)`,
  `gcd(M,ν)=1`); R2.1 case-I/II and case-III handshakes; the MRW root
  window in both the 2026-08-28 header and the R2.1 sharpening
  (`X_R = μ_e(1−w_e) = A/B`, `w_e ∈ (0,1)`); R2.2 (S)/(R)/(D) and
  `dq = (r₀ + k + l)ν + 1`; §3 mixed-menu OPEN; the §11 quarantined band
  (`d_p | d_q ⇔ kbar ∈ {3,4}` — at family I `(2, 2+L)` this is
  `2 + 4/L ∈ {3,4} ⇔ L ∈ {2,4}`, legacy `l ∈ {1,3}`, so the R2 quarantine
  reading survives verbatim and D9 still carries every even `L`); §11a
  "promoted H5a: 17 cells; forced-ν: 2 cells" (LL-2 baseline); §1a td-7
  witness; CRITICAL 5 (`s≥3` parenthetical false) and HIGH 1 (scope
  firewall cites). The MULTIPOLE MP9 cap flag ("excluded only for l ≤ 4")
  is anchor-gated as PRESENT-NOT-INHERITED: the cap firewall still refuses
  it as a decision.
- **Findings that could have changed a decision, checked and cleared:**
  the 2026-08-29 corrections in BOOK-OFFAXIS (69-not-70 chain states at
  budget 5; `OPEN_UNBOUNDED_MIXED_OR_POSTJUMP` re-reading) concern the
  td-7 off-axis chain-2 closure and the b≥2 grid — not consumed at LL-1,
  whose residue book is the packet's own td=6/budget-4 BFS, re-derived
  in-packet. The td-7 panel retraction header affects only LL-2 pointers,
  which the packet already states as obligations, not claims.

**`provenance.rederivation.decision_changes = []` — no intervening edit
changes any LL-1 decision.** The validator enforces that this list is
empty; any entry is a finding that blocks SOURCE_READY.

## 3. The A1 repair: honest frozen-fixture engine parity (mandate 3)

The R2 check `chk(all(2*nu+2 == 2*nu+2 for nu in range(2, 27)), ...)`
compared an expression to itself. It is deleted. The charged 26-shape /
351-route family claim is now handled in both of the ways the mandate
allows, split by what is honestly checkable:

**(a) What is parity-checked (derived vs parsed, never constant vs
itself).** The frozen record lives in two pinned promoted files:
SHEET6-DEPTH.md §6/check 6 and SHEET6-DEPTH-REVIEW.md (whose reviewer
re-ran `twopole_check.py l1only` and recorded "26 shapes, RESIDUE child
(1/2, 3, 2, 5) at 351 parent pairs, ZCH suffix-DEAD ×276, ν=1 ODE-dead
601 — and the w-formula PREDICTS the child: 2·(10, 6, 1)/4 = (κ̄, D/i, ρ)
= (5, 3, 1/2)"). The compiler parses these sentences with **count-free
regexes** (no expected number appears in any pattern; every figure in the
emitted `engine_record` is a captured group from the pinned bytes),
enforces seven internal cross-consistency identities (shape counts agree
across both files; 351 agrees with both `351/351` depth-invariance
sentences; the child tuples agree; the merge ledger's 601/276 agree with
the named counts; the printed prediction identity is arithmetically true),
and then runs six derived-vs-parsed parity checks:

1. parsed residue child `(ρ,ν,M,κ̄) = (1/2,3,2,5)` equals the packet's
   IIa-uniqueness-derived child `Q=(6,12,3,2,5)` in shape space
   (`ρ = 6/12`, `M = gcd(6,10)`);
2. parsed prediction inputs `w·(dq,dp,1)/Δ` are the derived cell
   `(dp,dq)=(6,10)`, `Δ=4`, `w ∈ W(2)`;
3. the DS4 identity recomputed on the parsed inputs gives `(5, 3, 1/2)`,
   equal to both the parsed outputs and the derived `(κ̄, X, X/dp)`;
4. the parsed frame family `(2, ν, 2ν+2)` has `w` equal to the derived
   entry `w0 = 2` with `W(2) = {2}` and ν-coefficient equal to `w`
   (fixed-w family, not e.g. `3ν+2`);
5. the w-map `(κ̄−ρ)/ν` on the parsed family returns the parsed `w` for
   `ν = 2..26` at chain `ρ = 2`, and on the derived entry frame
   `(ρ,ν,κ̄) = (1,2,5)` returns `2`;
6. the record's scope states the engine is NOT re-run, with `cited_from`
   exactly the two fixture files.

**(b) What is removed from proved scope.** The raw counts — 26 shapes
(24 μ1 + 2 ν=1-zch), 351 parent pairs, 351/351 invariance, ledger
18427/17199/601/276 — are **not** re-derived and the engine is **not**
re-run. They are recorded as FIXTURE-CITED under the new trust id
`ENGINE-REC`, with an explicit scope-firewall line in the book: the packet
claims only the six parity checks above, nothing more. Parity is never
manufactured: a drifted or missing charged sentence aborts the compile
(§4), and the test suite pins the parsed figures as regressions whose
values come from the parse, not from the parser.

## 4. Source-drift firewall (fail closed) and the rest of the controls

`compile_book()` refuses to emit and `validate()` refuses to pass unless,
against the byte-exact files on disk: all five pins hash correctly, all 43
consumed-clause anchors are present, the fixture parses, cross-consistency
holds, and the parity checks pass. The new A6 battery proves each branch
fails closed (10 checks): a single flipped byte anywhere in a re-pinned
source (pin gate + compile refusal); `351 → 352 parent pairs` with the
hash gate bypassed (caught by cross-consistency against the untouched
`351/351` sentences); a deleted charged sentence (parse fails, no silent
default); a deleted P0 finiteness clause (anchor gate, independent of the
hash); a tampered in-book pin, a tampered in-book 351 count, a deleted
provenance section, a fabricated `decision_changes` entry, and drifted
bytes fed to the validator (all caught).

All reviewed R2 controls re-pass unchanged inside the 139: empty-UNCOVERED
as the pass condition with the planted sealed-5.4 row theorem-killed
(A2); the four-presentation normalization of `(2,8)` and the family-I
split (A4-1/A4-2); the D9 suite (`n=2..6` binomials, even-`L`
inconsistency with `s(0)=0`, kernel `span{p^{L/2}}`, `L=1` positive
control); the cap firewall (CAP-tier cert under COVERED fails; the
synthetic probe stays UNCOVERED); the residue book regression and
route-death fixpoint (A3); the 17-mutation hostile battery (A4); recompile
byte-identity and no absolute paths (DET).

## 5. Test and validation record (exact)

    cd cases/landing_ledger_ll1_r3_20260829
    python3 ll1_compiler.py        # LL1-R3 compile OK (5 pins, 43 anchors, fixture parsed + parity)
    python3 ll1_validator.py       # exit 0: records + summary + pins/anchors/fixture re-verified
    python3 test_ll1_r3.py         # mode: ordinary        passed: 139  failed: 0
    python3 -O test_ll1_r3.py      # mode: OPTIMIZED (-O)  passed: 139  failed: 0
    python3 -O ll1_validator.py    # exit 0 (validator is assert-free)
    shasum -a 256 -c MANIFEST.sha256   # all six OK

**139/139 checks in both modes** (`chk` helper, never `assert`);
139 = 122 (R2 suite) − 1 (deleted tautology) + 8 (A1 honest gate)
+ 10 (A6 drift battery). Recompilation is byte-identical across repeated
runs (book `205e7f58…`, summary `7c7cfd3b…`; canonical JSON, sorted keys,
no timestamps, no absolute paths). The R2 packet's own manifest was
re-verified untouched this session (all six OK) — R2 remains immutable.

## 6. Complete R2 → R3 change inventory (mandate: every byte/function)

R3 files are byte-copies of R2 with exactly these edits (full list also in
the packet's `INVENTORY.md`; verified by `diff`):

- `ll1_compiler.py` (1204 → 1639 lines; 457 diff lines): docstring
  replaced (R-6/R-7 header over the retained R-1..R-5 lineage);
  `import re`; TRUST gains `ENGINE-REC` (no existing entry touched); new
  constants `SOURCE_PINS`, `R2_SUPERSEDED_PINS`, `CONSUMED_ANCHORS` (43),
  six count-free `_RX_*` regexes; new functions `_repo_read`,
  `load_sources`, `verify_source_pins`, `verify_clause_anchors`,
  `_search`, `parse_engine_fixture`, `engine_parity_checks`,
  `build_provenance`; `compile_book` gains `readers=None` and calls
  `build_provenance` first, the chain records' `why` gains the R-7 pointer
  and their `cert_chain` gains `ENGINE-REC`, the book gains `provenance`
  and the packet string becomes `LL1-R3 (td=6, m=2)`, one scope-firewall
  line added; `derive_summary` gains four derived fields; `main` prints
  the pins. **Every mathematical/classification function is
  byte-identical to R2** (`entry_menu` … `synthetic_cap_probe`, the full
  list is in INVENTORY.md).
- `ll1_validator.py` (305 → 351 lines; 60 diff lines): docstring;
  `validate` gains `readers=None` and the leading provenance section
  (disk re-hash, anchor re-check, fixture re-parse, parity re-run,
  superseded-pin trail, NOT-re-run scope, empty `decision_changes`);
  R3 OK banner. All R2 checks below it unchanged.
- `test_ll1_r2.py` → `test_ll1_r3.py` (571 → 728 lines; 171 diff lines):
  docstring; in `test_a1` the one tautological check is replaced by the
  eight-check honest gate; new `test_a6_source_drift` (10 checks);
  `main` calls it. A2/A3/D9/A4/A5/determinism/LL2-pointer unchanged.
- `INVENTORY.md`, `MANIFEST.sha256`, `out/*.json`: regenerated for R3.

## 7. Scope firewall and verdict

Unchanged from R2 and restated: this packet tests the corrected LL-1
quotient and hand-run at `td=6, m=2` only. It is not a proof that
`Cand(s) = CFG`; it does not bound segment depth; it proves no source
landing, ceiling, Keller, or JC2 statement; no output touches `G2-PSC`,
`G2-BD`, `RPMC(C)`, or the cofinal degree ceiling. Single-pole composite
configurations (REDUCTION HIGH 1) and realizability are out of scope;
ALIVE families are conservative supersets; recorded λ are AF2 lower
bounds; P0 menu completeness per state is cited; the mixed all-`μ≥2`
emission menu is OPEN in general. The 26/351 figures are fixture-cited
frozen engine history, not re-derived. LL-2 (`td=7`, off-axis entry, H5a
pin, 17-vs-2 books) remains the next obligation exactly as the R2 review
§5 specifies.

**Verdict: SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW.** Both R2 review
items are repaired: the pins now reproduce against the exact current
bytes (and equal that review's own session hashes), the consumed
P0/P1/§4/T7 clauses are re-derived against those bytes with zero decision
changes, and the A1 gate is an honest frozen-fixture parity check with a
fail-closed source-drift firewall. No AWS launch and no canonical
promotion are authorized by this report.

---
Report-body self-hash (sha256 of every byte above this line): d2876414c67a5b9fd692fb79977094bca4c6424eaf979f7f3455fe36785bffa1
