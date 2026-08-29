# LL1-R3 packet inventory — cases/landing_ledger_ll1_r3_20260829/

Narrow provenance/test-quality repair of the immutable R2 packet
(`cases/landing_ledger_ll1_r2_20260829/`), per the Grok 4.6 hostile review
`xmodel/landing-ledger-ll1-r2-hostile-review-grok46-20260829.md`
(PASS_AT_LL1_SCOPE; two non-killing items: two stale source pins, one
tautological A1 engine-parity check).  The R2 mathematics, compiler and
validator semantics, and every reviewed LL-1 decision are preserved.
Producer report:
`xmodel/landing-ledger-ll1-r3-provenance-repair-fable5-20260829.md`.

| file | role |
|---|---|
| `ll1_compiler.py` | R2 compiler (T7 entry solve, DS3 closure, `nu=1` family-I normalization, D9 log-obstruction with exact linear-algebra verification, IIa uniqueness theorem, ZCH/root laws, P0 priced-step enumerator, P1/St 9.4 terminals, budget-exhaustion residue BFS, synthetic UNCOVERED probe, deterministic JSON emission) **plus the R-6/R-7 provenance layer**: five byte-exact source pins, 43 consumed-clause anchors, count-free regex parse of the frozen 26-shape/351-route engine record, derived-vs-parsed engine parity checks.  `compile_book()` fails closed on any source drift. |
| `ll1_validator.py` | R2 fail-closed validator (re-derives every record's arithmetic and the whole summary; token whitelists; CAP-tier prohibition; `M = gcd(dp,dq)`; UNCOVERED discipline; theorem-kill check; residue re-enumeration) **plus provenance re-verification**: re-reads the five pinned sources from disk, re-hashes, re-checks anchors, re-parses the engine fixture, re-runs parity, and enforces the empty `decision_changes` list.  No `assert` statements. |
| `test_ll1_r3.py` | R2 acceptance tests A1–A5 + hostile battery, with A1's tautological `2*nu+2 == 2*nu+2` check replaced by the honest frozen-fixture parity gate, **plus the new A6 source-drift battery** (10 fail-closed mutations).  139 checks; identical under `python -O`. |
| `out/ll1_book.json` | Deterministic compiled book (canonical JSON, sorted keys, no timestamps or absolute paths); now carries the `provenance` object. |
| `out/ll1_summary.json` | Derived summary (recomputed, never hand-written); now echoes pins, clause count, engine-record headline, and the zero decision-change count. |
| `INVENTORY.md` | This file. |
| `MANIFEST.sha256` | SHA-256 of every packet file (excluding itself). |

## Source pins (R-6)

Verified at compile time AND validate time; any drift fails closed:

    93adb7acedf4cf0fd56ffc68e4571649a04eab12e1271431449a79465a964bcb  ladder/SHEET6-MULTIPOLE.md   (unchanged from R2)
    ad9ced6c0420902f8cf63edf3636bed8633be511e925f208d24a24c35d71036d  ladder/SHEET6-DEPTH.md       (unchanged from R2)
    7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77  ladder/BOOK-OFFAXIS.md       (RE-PINNED at current bytes)
    0a88db0d136001a6c18343f941a80ecfaef5ceffcbe84e05c739a853d13c1936  ladder/REDUCTION.md          (RE-PINNED at current bytes)
    841fa120fa2ae801578834c7b52c5aad600eb48df73b683e1db5c954caf7f7ac  ladder/SHEET6-DEPTH-REVIEW.md (NEW fixture pin, R-7)

The two re-pinned values equal the R2 hostile review's session hashes, so
that review's clause re-derivation applies to exactly these bytes.  R2's
stale pins (`34f5ea9d…`, `6b9376e0…`) are recorded in the book under
`provenance.r2_superseded_pins` for the audit trail only.

## Complete R2 → R3 change inventory

R2 files were copied byte-for-byte and then edited; every difference is
listed here (verified by `diff`; no other line changed).

`ll1_compiler.py` (1204 → 1639 lines):

- module docstring: R2 header replaced by the R3 header describing R-6/R-7
  (the R-1..R-5 lineage text is retained below it);
- `import re` added;
- `TRUST`: one NEW id `ENGINE-REC` (tier promoted, FIXTURE-CITED engine
  record); no existing entry touched;
- NEW constants: `SOURCE_PINS`, `R2_SUPERSEDED_PINS`, `CONSUMED_ANCHORS`
  (43 anchors), six `_RX_*` compiled regexes (count-free);
- NEW functions: `_repo_read`, `load_sources`, `verify_source_pins`,
  `verify_clause_anchors`, `_search`, `parse_engine_fixture`,
  `engine_parity_checks`, `build_provenance`;
- `compile_book`: signature gains `readers=None`; first statement now calls
  `build_provenance(readers)`; the chain records' `why` text is extended
  with the R-7 pointer and their `cert_chain` gains `ENGINE-REC`; book dict
  gains `"provenance"` and its `"packet"` string becomes
  `"LL1-R3 (td=6, m=2)"`; one scope-firewall line added (26/351 figures
  are fixture-cited);
- `derive_summary`: four NEW derived fields (`source_pins`,
  `consumed_clauses_present`, `engine_record_headline`,
  `rederivation_decision_changes`);
- `main`: prints the five verified pins and the R3 banner.
- UNCHANGED (byte-identical): `frac`, `is_pos_int`, `ceil_frac`, `cert`,
  `entry_menu`, `entry_frame`, `w_closure`, `normalize_nu1_merge`,
  `binom_neg`, `poly_mul`, `poly_deriv`, `d9_operator`, `solve_linear`,
  `d9_ode_status`, `d9_kernel_is_p_power`, `d9_residue_check`,
  `classify_family_I`, `iia_cell`, `iia_admitted`, `join_handshake`,
  `step_legal`, `zch_join`, `root_meet`, `root_local_cell`, `af2_price`,
  `dirty_cells`, `neutral_reachable_M`, `terminal`, `budget_verdict`,
  `residue_enumeration`, `synthetic_cap_probe`, `_f`, `canonical_json`
  — i.e. every mathematical/classification function.

`ll1_validator.py` (305 → 351 lines):

- module docstring: R3 header;
- `validate`: signature gains `readers=None`; NEW leading provenance
  section (pin re-verification from disk, anchor re-check, fixture
  re-parse, parity re-run, superseded-pin trail, NOT-re-run scope,
  empty `decision_changes`); every R2 check below it unchanged;
- `main`: R3 OK banner.

`test_ll1_r2.py` → `test_ll1_r3.py` (571 → 728 lines):

- module docstring: R3 header;
- `test_a1`: the single tautological check
  `chk(all(2*nu+2 == 2*nu+2 for nu in range(2, 27)), ...)` is REPLACED by
  the eight-check honest gate (pins verify + parse == book record +
  parsed-figure regression pin + frozen residue child + parity table +
  DS4 identity on parsed inputs + fixture-cited scope + empty
  decision-changes); nothing else in A1 touched;
- NEW `test_a6_source_drift` (10 fail-closed mutations: flipped byte at
  the pin gate; compile refusal; 351→352 cross-consistency; deleted
  charged sentence; deleted P0 finiteness clause at the anchor gate;
  tampered in-book pin; tampered in-book 351 count; deleted provenance
  section; fabricated decision change; drifted bytes at the validator);
- `main`: calls `test_a6_source_drift`;
- A2, A3, D9, A4, A5, determinism, LL2-pointer tests: unchanged.

Check count: 122 (R2) → 139 (R3) = −1 tautology + 8 A1-gate checks
+ 10 A6 checks.

## Reproduction

    cd cases/landing_ledger_ll1_r3_20260829
    python3 ll1_compiler.py      # verifies pins/anchors/fixture, emits out/*.json
    python3 ll1_validator.py     # exit 0 iff the book AND the sources validate
    python3 test_ll1_r3.py       # 139 checks
    python3 -O test_ll1_r3.py    # identical under -O
    shasum -a 256 -c MANIFEST.sha256

Scope firewall: this packet tests the corrected LL-1 quotient and hand-run
at `td=6, m=2` only.  It is not a proof that the candidate grammar equals
all geometric configurations, does not bound depth, and proves no source
landing, ceiling, Keller, or JC2 statement.  The 26-shape/351-route
figures are fixture-cited frozen engine history; the engine is not re-run
and those counts are not re-derived here.  R3 cannot promote itself or
authorize AWS.
