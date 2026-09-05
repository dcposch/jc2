# Guided-GB timeout contract: typed per-stage expiry, no inner cap under an outer watchdog

Lane `guided-gb-timeout-fix-grok46-20260905`. Instrument patch only: no class
kill, no survivor, no new exit price. Frozen gi70 job (b) remains
`OPEN / COMPUTE-BOUND`.

## 0. Headline

`box/lib/guided_gb.py` now owns a Hilbert-seed stage and a timeout contract
that cannot raise a bare driver error. An internal per-stage cap is
configurable (Python API and CLI). Declaring an outer watchdog suppresses the
inherited 1800 s std cap. Expiry returns typed `INCONCLUSIVE_TIMEOUT` with
`timeout_stage` in `{hilbert_seed, std}`. `PromotionPolicy.exact_q` and
modular-unit-not-promoted are unchanged. Census-sweep controls replay
identically.

## 1. Frozen-input verification

Receipt `xmodel/guided-gb-timeout-fix-grok46-20260905.run.v2`,
`lane_inputs_dir=/tmp/jc2-lane.e7Tt2C/inputs`. Manifest built with awk from
`charged_input_<i>_sha256=` / `_basename=` (not transcribed) and checked with
`sha256sum -c`. **4/4 OK**. Workspace copies match.

| frozen input | SHA-256 |
|---|---|
| `gi70-longsolve-sol56-20260905.md` | `9b4c986f1722a37bd0c7237e6b7bc69380894c70f702b8a1bc3781b128ce74cb` |
| `census-sweep-grok46-20260905.md` | `58146fdb40740b9491b7d0390f8f8b38b164bfffba83b81d00e0f5972fc1e404` |
| `guided_gb.py` | `501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3` |
| `FALLACY-v2.md` | `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5` |

No ledger, `jc2-lean`, or `ideation-*` file was edited. No fleet.

## 2. Failure mode (read, then reproduced)

Frozen `guided_gb.py` had one wait cap: `RunConfig.timeout_seconds = 1800`,
applied by `process.wait(timeout=config.timeout_seconds)` to the whole
Singular std script. There was no Hilbert-series stage in the library.
gi70 job (b) therefore rolled its own seed: `subprocess.run(..., timeout=9_900)`
inside a GNU `timeout 10200s` wrapper, then `RunConfig(timeout_seconds=9_600)`
for guided std. The 9,900 s cap fired during `std(S)` of the seed, before any
`HNUM`, guided run, or CRT. Uncaught `TimeoutExpired` became wrapper rc 1
("driver error 1"). The library std path already mapped wait-expiry to
`INCONCLUSIVE_TIMEOUT`, but with the unstaged note
`"no accepted result before timeout"`.

Reproduction, synthetic ideal, cap 1 s, Singular `system("sh","sleep 3")`:

- gi70-style `subprocess.run(..., timeout=1)` → `TimeoutExpired` at 1.003 s
  (the driver-error-1 path if uncaught).
- unpatched `guided_groebner(..., timeout_seconds=1)` →
  `INCONCLUSIVE_TIMEOUT`, note without a stage, no `timeout_stage` key.

## 3. Patch

Patched SHA-256
`95d12f5b23975e8699b634b1ba8c6f0e6fc4e24abfcd4bad2db936e1c74e9826`
(898 → 1129 lines). Header comment in the module docstring and on
`RunConfig`.

| knob | default | meaning |
|---|---|---|
| `timeout_seconds` | 1800 | legacy std cap |
| `hilbert_seed_timeout_seconds` | None | seed-stage cap; None = none |
| `std_timeout_seconds` | None | std-stage cap; else inherit legacy |
| `outer_watchdog_seconds` | None | if set, inherited std cap is not applied |

CLI: `--timeout` (legacy, still default 1800), `--std-timeout`,
`--hilbert-timeout`, `--outer-watchdog`, `--hilbert-seed`.
`<= 0` means no internal cap. `process.wait()` is used when the resolved cap
is None. `TimeoutExpired` is converted to `timed_out=True` and never
propagated. Seed-stage abort returns immediately; std/CRT are not started.

`guided_groebner(..., hilbert_seed=system)` runs `std` then weighted `hilb`
and feeds the numerator as `HilbertHint` with `predicted_length=None`.

## 4. Diff (against frozen `501f3b1f…`)

`git diff --stat box/lib/guided_gb.py`:

```text
 box/lib/guided_gb.py | 261 ++++++++++++++++++++++++++++++++++++++++++++++++---
 1 file changed, 246 insertions(+), 15 deletions(-)
```

Full patch: `box/guided-gb-fix-20260905/guided_gb.py.diff`.

Added: `STAGE_HILBERT_SEED`, `STAGE_STD`, `_positive_or_none`,
`resolve_stage_timeout`, `emit_hilbert_seed_script`,
`parse_hilbert_numerator`, `run_hilbert_seed`; fields on `RunConfig` and
`SingularRunResult`; `hilbert_seed=` on `guided_groebner`; CLI flags.

Byte-identical (ast source segment): `emit_guided_script`,
`_emit_one_analysis`, `_controls_accepted`, `parse_marker_controls`,
`crt_pair`, `crt_many`, `rational_reconstruct`, `reconstruct_invariants`.
`PromotionPolicy.exact_q` is still
`cls(PromotionScope.EXACT_Q, True, False, note)`. The modular-unit note is
still `"modular unit ideal was not promoted to characteristic zero"`.
Non-timeout promotion notes are unchanged. The timeout note gained
` at stage {timeout_stage}`.

## 5. Tests (`box/lib/tests/test_guided_gb_timeout.py`)

12/12 PASS, wall 6.1 s (`box/guided-gb-fix-20260905/unit-test-results.json`).

| test | result |
|---|---|
| `resolve_stage_timeout` (legacy 1800; seed none; outer watchdog suppresses 9900; explicit per-stage wins; 0/None = none) | PASS |
| `PromotionPolicy.exact_q` fields | PASS |
| known-empty `(c, Tc-1)` → `UNIT_IDEAL_CHAR0` dim −1 | PASS |
| known-nonempty `(c-1, Tc-1)` → `DIM0_CHAR0` non-unit | PASS |
| tame automorphism → `DIM0_CHAR0`, unit false, dim 0, inverse/forward markers 0 | PASS |
| modular unit + `exact_q` → `MODULAR_ONLY`, note unchanged | PASS |
| std cap 1 s / sleep 3 → `INCONCLUSIVE_TIMEOUT` at `std` | PASS |
| seed cap 1 s / sleep 3 → `INCONCLUSIVE_TIMEOUT` at `hilbert_seed`; no std run | PASS |
| `timeout_seconds=1` + `outer_watchdog_seconds=30` + sleep 2 → completes `DIM0_CHAR0` | PASS |
| explicit `std_timeout_seconds=1` with outer watchdog still expires at `std` | PASS |
| seed then std on `(x,y,z)` mod 32003 → `DIM0_CHAR0` under properness | PASS |
| `run_hilbert_seed` does not raise `TimeoutExpired` | PASS |

## 6. Census-sweep control replay (FALLACY-v2)

`python3 box/lib/census_sweep.py controls --dest box/guided-gb-fix-20260905/census-controls --timeout 180`
→ `ALL CONTROLS PASSED`. Compared to frozen
`box/census-sweep-20260905/controls/*/certificate.json`:

| control | old | new | unit | dim |
|---|---|---|---|---|
| D108 δ=3 common-h₃ | DEAD / UNIT | DEAD / UNIT | T/T | −1/−1 |
| (99,66) δ=2 stage-4 | DEAD / UNIT | DEAD / UNIT | T/T | −1/−1 |
| K=8 D=108 no-split | DEAD / UNIT | DEAD / UNIT | T/T | −1/−1 |
| K=9 case A | DEAD / UNIT | DEAD / UNIT | T/T | −1/−1 |
| tame auto | SURVIVES | SURVIVES | F/F | 0/0 |

Tame `guided_verdict` remains `DIM0_CHAR0`. Known-empty / known-nonempty
synthetics in §5 are the `sat()`-style `(c, Tc-1)=(1)` and `(c-1, Tc-1)≠(1)`
controls from the sweep prelude. An instrument change did not alter any
verdict.

No `charge_basis` line: this lane asserts no new exit price.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6684`.
- Body SHA-256:
  `cac9aaa7d758ce3a128dd1ad45f4727d07d111fe89db0041433e0e51e3f2dea6`.
- Frozen basis: `37a09e5f24de67baab62a739e1c21dfe8d2e697c`.
