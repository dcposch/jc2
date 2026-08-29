# LL1-R4 packet inventory — `cases/landing_ledger_ll1_r4_20260829/`

Date: 2026-08-29

Status: **PROVISIONAL SOFTWARE — independent different-model software review
still required before software promotion.** The mathematical carrier theorem
and its stable hostile review are already promoted inputs; this packet only
implements their typed LL-1 consumer.

## Delta from immutable LL1-R3

R3 and `cases/m2_exit_safe_floor_legacy_reprice_r1_20260829/check.py` remain
byte-for-byte unchanged. R4 preserves the R3 candidate grammar, merge/entry
classification, exact rational arithmetic, engine-fixture parity, and scope
firewall. It changes only the typed nonzero price and the derived replay:

- every actual nonzero up direction is explicitly
  `FULL_ACTUAL_FIRST_SEPARATION`, canonically aliased to `FULL_ACTUAL_EXIT`;
- its floor is `delta` for positive integral `delta`, otherwise
  `ceil(2*delta)`;
- legacy `REPRESENTATIVE` AF2 remains a separate callable and an emitted
  comparison field;
- epsilon/zero and pure-epsilon directions remain `REPRESENTATIVE` under the
  legacy rule;
- all prices are `LOWER_FLOOR_ONLY`, with `attainment=false`.

Exactly four of 16 unique LL-1 cells change:

| cell | representative total | R4 total | epsilon/zero |
|---|---:|---:|---:|
| `(17,5)@nu2` | 2 | 3 | 1 |
| `(51,15)@nu7` | 2 | 3 | 1 |
| `(85,25)@nu12` | 2 | 3 | 1 |
| `(119,35)@nu17` | 1 | 2 | 0 |

The reduced-superset terminal inventory changes exactly `13 -> 7`, with six
removed and no added row. `ALIVE` remains a conservative superset predicate,
not occurrence or realization.

## Files

| file | role |
|---|---|
| `ll1_compiler.py` | R3 compiler plus explicit carrier types, separate representative/full floor functions, per-component metadata, 7 canonical source pins, 8 evidence pins, 6 body seals, and exact old/new replay |
| `ll1_validator.py` | independent re-derivation of provenance, carrier typing, component prices, pure-epsilon firewall, exact four movers, and 13-to-7 inventory |
| `test_ll1_r4.py` | R3 regression/mutation suite plus carrier fixtures, evidence mutation, exact mover/survivor assertions, and frozen legacy-checker ordinary/`-O` parity |
| `out/ll1_book.json` | deterministic full record book |
| `out/ll1_summary.json` | deterministic derived summary |
| `MANIFEST.sha256` | SHA-256 manifest of the five executable/data payloads and this inventory |

No `assert` is load-bearing. Every gate is explicit and remains active under
`python -O`.

## Verification commands

Run from repository root with bytecode disabled:

```text
PYTHONDONTWRITEBYTECODE=1 python3 cases/landing_ledger_ll1_r4_20260829/ll1_compiler.py
PYTHONDONTWRITEBYTECODE=1 python3 cases/landing_ledger_ll1_r4_20260829/ll1_validator.py
PYTHONDONTWRITEBYTECODE=1 python3 cases/landing_ledger_ll1_r4_20260829/test_ll1_r4.py
PYTHONDONTWRITEBYTECODE=1 python3 -O cases/landing_ledger_ll1_r4_20260829/test_ll1_r4.py
```

Expected acceptance result: `ALL TESTS PASS (166 checks)`. Ordinary and
optimized stdout must be byte-identical.

## Scope firewall

One fixed fibre and the reviewed two-pole carrier only. Generic MP8/MFE stays
`REPRESENTATIVE`. No full finite-book theorem, source landing, realization,
attainment, degree ceiling, `td != 6`, Keller-map exclusion, or JC2 conclusion
is asserted. The frozen 26-shape/351-route engine record remains fixture-cited,
not re-run or re-derived.
